var {ArrayList, StrTool, printf} = import('.compat');
var {StringMap} = import('.StringMap');
var {ElementPattern, InternalError, XMLDumper} = import('.utils');
var CAS = import('tools.cas');

var pythonKeywords:StringMap = new StringMap();
// TODO: remove exec if python2 is no longer supported
pythonKeywords.sets(new ArrayList(['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', 'exec']), true);

/**
 * check if `name` is a python's keyword
 */
public function isKeyword(name):Boolean {
    return pythonKeywords.has(name);
}

/**
 * check if `name` needs to be encoded
 *
 * 检查是否为特殊标识符, 即包含非ASCII字符或美元符号
 * 对于其他情况, 需要由子类进行进一步的检查
 */
public function isSpecial(name):Boolean {
    var enc = false;
    var ars = new ArrayList(name);
    ars.forEach(function(c, k, a) {
        var ch = StrTool.codePointAt(c);
        // $
        if(ch === 36) {
            enc = true;
            return false;
        }
        if(ch >= 128) {
            enc = true;
            return false;
        }
    });
    return enc;
}

/**
 * base class of the attributes
 *
 * 各种标识符的基类, 不要直接使用这个类.
 */
public class BaseAttribute {
    /**
     * original name
     */
    public var name:String;

    /**
     * original range object of this, used for error reporting
     */
    public var range:Range;

    /**
     * wrapper for toString
     */
    public function __str__():String {
        return this.toString();
    }

    /**
     * to string, just output the name
     */
    public function toString():String {
        return this.name;
    }

    public function BaseAttribute(name:String, range:Range) {
        this.name = name;
        this.range = range;
    }
}


/**
 * class of the attribute (for property)
 *
 * 标签需要和Python本身的标签兼容
 */
public class Attribute extends BaseAttribute {
    public function toPython():String {
        return this.name;
    }

    public function Attribute(name:String, range:Range) {
        super(name, range);
        if(isSpecial(name)) {
            CAS.error(range, 'Attribute name with $ or non-ASCII characters is not allowed: %s', name);
        }
        if(isKeyword(name)) {
            CAS.error(range, 'Python keyword cannot be used as attribute: %s', name);
        }
    }
}


/**
 * descriptof of the class field, used by ClassElement
 *
 * ClassElement用来统计其成员信息的类, 注意类成员本身不应使用这个类, 而是要分别使用MethodTag和PropertyTag.
 * 应将静态和非静态成员放在不同的字典中.
 */
public class ClassFieldDescriptor extends Attribute {
    private var getter:MethodTag = null;
    private var setter:MethodTag = null;
    private var method:MethodTag = null;
    private var property:Boolean = false;

    private var priv:Boolean = false;
    private var publ:Boolean = false;

    private var isStatic:Boolean = false;

    /**
     * true if this is a property and should be declared in __slots__
     */
    public function get isProperty():Boolean {
        this.verify();
        return this.property;
    }

    /**
     * true if this is an accessor and should be created by property class
     */
    public function get isAccessor():Boolean {
        this.verify();
        return this.getter !== null || this.setter !== null;
    }

    /**
     * true if this has a getter
     */
    public function get isGetter():Boolean {
        this.verify();
        return this.getter !== null;
    }

    /**
     * true if this has a setter
     */
    public function get isSetter():Boolean {
        this.verify();
        return this.setter !== null;
    }

    /**
     * true if this is a method (but not accessor)
     */
    public function get isMethod():Boolean {
        this.verify();
        return this.method !== null;
    }

    /**
     * true if this is a private member
     */
    public function get isPrivate():Boolean {
        this.verify();
        return this.priv;
    }

    /**
     * called when a method with the same name is met
     */
    public function meetMethod(tag:MethodTag):void {
        if(tag.isStatic !== this.isStatic) {
            throw new InternalError('mismatched static flag');
        }
        if(this.property) {
            CAS.delayedError(tag.range, 'Incompatible override to property %s', this.name);
            CAS.note(this.range, "'%s' has previously defined here.", this.name);
        }
        if(this.method !== null ||
           (this.setter !== null || this.getter !== null) && !tag.isAccessor ||
           this.setter !== null && tag.isSetter ||
           this.getter !== null && !tag.isSetter) {
            CAS.error(tag.range, 'Duplicate method definition %s', this.name); 
        }
        if(this.priv && tag.isPublic || this.publ && !tag.isPublic) {
            CAS.delayedError(tag.range, 'A conflict exists with access modifier of definition %s', this.name);
            CAS.note(this.range, "'%s' has previously defined here.", this.name);
        }
        if(!tag.isAccessor) {
            this.method = tag;
        } else if(tag.isSetter) {
            this.setter = tag;
        } else {
            this.getter = tag;
        }
        if(tag.isPublic) {
            this.publ = true;
        } else {
            this.priv = true;
        }
        this.verify();
    }

    /**
     * called when a proporty with the same name is met
     */
    public function meetProperty(isPublic:Boolean, range:Range):void {
        if(this.property || this.method !== null || this.setter !== null || this.getter !== null) {
            CAS.delayedError(range, 'Incompatible override to property %s', this.name);
            CAS.note(this.range, "'%s' has previously declared here.", this.name);
        }
        this.range = range;
        this.property = true;
        if(isPublic) {
            this.publ = true;
        } else {
            this.priv = true;
        }
        this.verify();
    }

    /**
     * to method tag or accessor creator
     */
    public function toMethodName():String {
        this.verify();
        if(this.isProperty) {
            throw new InternalError('property is not method');
        }
        if(this.isMethod) {
            return this.method.toRawPython();
        }
        var g = this.isGetter ? this.getter.toRawPython() : 'None';
        var s = this.isSetter ? this.setter.toRawPython() : 'None';
        return '__x_prop(' + g + ', ' + s + ')';
    }

    private function verify():void {
        /*
         * the reserved class member
         *
         * 一些类成员的名称是不可使用的. 大多数是特殊方法(special method), 使用这些名称会和默认行为发生冲突.
         * 此外特殊方法只能作为实例方法使用, 不可以作为其他的成员. 
         */
        var rsvdMember = new StringMap();
        rsvdMember.sets(['__init__', '__new__', '__slots__', '__dict__',
                         '__getattribute__', '__getattr__', '__setattr__', '__delattr__',
                         '__instancecheck__', '__subclasscheck__', '__init_subclass__',
                         '__annotations__', '__bases__', '__cause__', '__class__', '__classcell__',
                         '__closure__', '__code__', '__context__', '__debug__', '__defaults__',
                         '__doc__', '__file__', '__future__', '__globals__', '__kwdefaults__', '__mro__',
                         '__name__', '__package__', '__path__', '__prepare__', '__qualname__', '__self__',
                         '__spec__', '__traceback__'
                        ], true);
        var rsvdStatic = new StringMap();
        rsvdStatic.sets([
            'mro'
        ], true);

        // 以双下划线开头和结尾的标签保留给魔术方法
        // 如果不是魔术方法, 就不可以双下划线开头, 以免导致意外的转义
        var na = new ArrayList(this.name);
        var dupre = na.length >= 2 && na.get(0) === '_' && na.get(1) === '_';
        // 如果只有双下划线(__), 也算双下划线结尾
        var dusuf = na.length >= 2 && na.get(-1) === '_' && na.get(-2) === '_';
        if(dupre && dusuf && (this.method === null || this.isStatic || !this.publ)) {
            CAS.error(this.range, 'names starting and ending with double underscores in class statement are reserved for special methods');
        }
        if(dupre && !dusuf) {
            CAS.error(range, 'names starting with double underscores in class statement are not allowed');
        }
        if(!this.isStatic && rsvdMember.has(this.name)) {
            CAS.error(range, 'class member %s is reserved', this.name);
        }
        if(this.isStatic && rsvdStatic.has(this.name)) {
            CAS.error(range, 'static member %s is reserved', this.name);
        }

        if(this.getter === null && this.setter === null && this.method === null && !this.property) {
            throw new InternalError('undefined class member');
        }

        if(!this.priv && !this.publ) {
            throw new InternalError('class member withput access modifier');
        }
    }

    public function ClassFieldDescriptor(name:String, range:Range, isStatic:Boolean) {
        super(name, range);
        this.isStatic = isStatic;
    }
}
