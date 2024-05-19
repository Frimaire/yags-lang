var {ArrayList, StrTool, printf} = import('.compat');
var {StringMap} = import('.StringMap');
var {CompileError, ElementPattern, Range, ConflictError, InternalError, XMLDumper} = import('.utils');

// please DO NOT delete the headers like this
// #########= Identifier

/**
 * base class of the identifiers
 *
 * 各种标识符的基类, 不要直接使用这个类.
 */
public class Identifier {
    public static var radix36:ArrayList = new ArrayList('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ');
    public static var pythonKeywords:StringMap = new StringMap();

    /**
     * integer to radix 32
     */
    public static function encodeRadix32(n:Number):String {
        if(int(n) !== n || n < 0) {
            throw new InternalError('illegal n in encodeRadix32');
        }
        if(n >= (1 << 30)) {
            // 尽管触发这个可能是因为一个程序里要几十亿个临时变量, 但这基本不可能发生
            throw new InternalError('n too large in encodeRadix32');
        }
        if(n === 0) {
            return '0';
        }
        var k = 6, s = '';
        while(k > 0 && n > 0) {
            k--;
            var cn = Identifier.radix36.get(n & 31);
            s = cn + s;
            n >>= 5;
        }
        return s;
    }

    /**
     * original name
     */
    public var name:String;

    /**
     * original range object of this, used for error reporting
     */
    public var range:Range;

    /**
    * check if this is a python's keyword
    */
    public function get isKeyword():Boolean {
        return Identifier.pythonKeywords.has(this.name);
    }

    /**
     * check if s needs to be encoded
     *
     * 检查是否为特殊标识符, 即包含非ASCII字符或美元符号
     * 对于其他情况, 需要由子类进行进一步的检查
     */
    public function get isSpecial():Boolean {
        var enc = false;
        var ars = new ArrayList(this.name);
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
     * encode identifier
     *
     * 经过特殊编码的字符以下划线开头, 所以全部下划线转换成双下划线.
     * Python不支持美元符号, 因此美元符号需要进行编码. 编码成_d
     * 为了兼容起见, 所有的非ASCII字符也进行编码,
     * 1. 平面号(共17个平面, 编号0-16)和平面内码点(16位)的最高位编码成34进制, 共一个字符
     * 2. 平面内码点的低15位编码成32进制, 恰好三个字符
     * 该函数不会验证输入是否是个有效的标识符
     */
    public function encode():String {
        var se = '';
        (new ArrayList(this.name)).forEach(function(c, k, a) {
            var ch = StrTool.codePointAt(c);
            // $
            if(ch === 36) {
                se += '_d';
                return;
            }
            // _
            if(ch === 95) {
                se += '__';
                return;
            }
            if(ch < 128) {
                se += c;
                return;
            }
            var pn = ch >> 15;
            var cn = ch;
            var ss = '';
            ss = Identifier.radix36.get(cn & 31) + ss;
            cn >>= 5;
            ss = Identifier.radix36.get(cn & 31) + ss;
            cn >>= 5;
            ss = Identifier.radix36.get(cn & 31) + ss;
            ss = Identifier.radix36.get(pn) + ss;
            se += '_' + ss;
        });
        return se;
    }

    /**
     * to string, just output the name
     */
    public function toString():String {
        return this.name;
    }

    public function Identifier(name:String, range:Range) {
        this.name = name;
        this.range = range;
    }
}

// py's keyword
Identifier.pythonKeywords.sets(new ArrayList(['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', 'exec']), true);

// #########= Attribute

/**
 * class of the attribute
 *
 * 标签需要和Python本身的标签兼容
 */
public class Attribute extends Identifier {
    public function toPython():String {
        return this.name;
    }

    public function Attribute(name:String, range:Range) {
        super(name, range);
        if(this.isSpecial) {
            throw new CompileError('Illegal attribute name ' + name, range);
        }
        if(this.isKeyword) {
            throw new CompileError('Python keyword cannot be used as attribute ' + name, range);
        }
    }
}

// #########= Variable

/**
 * base class for variables
 */
public class Variable extends Identifier {
    /**
     * is assigned by =
     */
    public var assigned:Boolean = false;

    /**
     * is modified by the inner function
     */
    public var closure:Boolean = false;

    /**
     * the function where this is declared
     */
    public var at:BaseFunctionElement;

    /**
     * check if s needs to be encoded
     *
     * 检查是否为特殊标识符, 包括含非ASCII字符, 美元符号或者是Python关键字
     */
    override public function get isSpecial():Boolean {
        return super.isSpecial || super.isKeyword;
    }

    /**
     * check the redeclaration with the same name
     *
     * 检查该变量是否可以被重复声明. 注意, 如果发生了重复声明, 新的变量和旧的变量均需要调用该函数.
     */
    public function redeclare(from:BaseFunctionElement, range:Range = null):void {
        if(from !== this.at) {
            throw new InternalError('redeclare in defferent function scope');
        }
    }

    /**
     * check the reading from this
     */
    public function read(from:BaseFunctionElement, range:Range = null):void {
        throw new InternalError('read check is abstract');
    }

    /**
     * check the writing to this
     * constants should override this and throw error
     * @param {BaseFunctionElement} from, the function where this is assigned
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    public function write(from:BaseFunctionElement, range:Range = null):void {
        throw new InternalError('write check is abstract');
    }

    /**
     * to python identifier
     */
    public function toPython():String {
        return this.toRawPython();
    }

    /**
     * original name to python identifier (without closure suffix)
     */
    public function toRawPython():String {
        // 子类应当超按该函数以加上适当的前缀
        throw new InternalError('toRawPython is abstract');
    }

    /**
     * to comment string
     */
    public function toComment():String {
        var n = this.name;
        var s = this.toRawPython();
        if(this.isSpecial) {
            return n + '(' + s + ')';
        }
        return s;
    }

    /**
     * the constructor
     */
    public function Variable(name:String, at:BaseFunctionElement, range:Range) {
        super(name, range);
        this.at = at;
    }

}

// #########= BuiltinVar

/**
 * built-in variables
 *
 * 来自内部作用域的变量, 比如Infinity
 * 内部变量不允许直接赋值, 但是可以声明一个同名的变量.
 */
public class BuiltinVar extends Variable {
    /**
     * check the redeclaration with the same name
     */
    override public function redeclare(from:BaseFunctionElement, range:Range = null):void {
        // 该情况不可能出现
        throw new InternalError('redeclare BuiltinVar');
    }

    /**
     * check the reading from this
     */
    override public function read(from:BaseFunctionElement, range:Range = null):void {
    }

    /**
     * check the writing to this
     */
    override public function write(from:BaseFunctionElement, range:Range = null):void {
        throw new CompileError('Illegal assignment to bulit-in variables', range);
    }

    override public function toRawPython():String {
        return this.name;
    }

    /**
     * to string
     */
    override public function toString():String {
        return "builtin_var." + this.name;
    }

    /**
     * the constructor
     */
    public function BuiltinVar(name:String, at:BaseFunctionElement) {
        super(name, at, null);
    }
}

// #########= ClassFieldDescriptor

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
            throw new ConflictError('Incompatible override to property %s', tag.range, this.range, this.name); 
        }
        if(this.method !== null ||
           (this.setter !== null || this.getter !== null) && !tag.isAccessor ||
           this.setter !== null && tag.isSetter ||
           this.getter !== null && !tag.isSetter) {
            throw new CompileError('Duplicate method definition %s', tag.range, this.name); 
        }
        if(this.priv && tag.isPublic || this.publ && !tag.isPublic) {
            throw new ConflictError('A conflict exists with access modifier of definition %s', tag.range, this.range, this.name); 
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
            throw new ConflictError('Incompatible override to property %s', range, this.range, this.name); 
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
            throw new CompileError('names starting and ending with double underscores in class statement are reserved for special methods', this.range);
        }
        if(dupre && !dusuf) {
            throw new CompileError('names starting with double underscores in class statement are not allowed', range);
        }
        if(!this.isStatic && rsvdMember.has(this.name)) {
            throw new CompileError('class member ' + this.name + ' is reserved', range);
        }
        if(this.isStatic && rsvdStatic.has(this.name)) {
            throw new CompileError('static member ' + this.name + ' is reserved', range);
        }

        if(this.getter === null && this.setter === null && this.method === null && !this.property) {
            throw new InternalError('undefined class member');
        }

        if(!this.priv && !this.publ) {
            throw new InternalError('class member withput access modifier');
        }
    }

    public function ClassFieldDescriptor(name:String, isStatic:Boolean) {
        super(name, null);
        this.isStatic = isStatic;
    }
}

// #########= LocalVar

/**
 * class for local variables
 */
public class LocalVar extends Variable {
    /**
     * check if s needs to be encoded
     *
     * 检查是否为特殊标识符
     */
    override public function get isSpecial():Boolean {
        // 如果以双下划线开头就算特殊的
        if(StrTool.strlen(this.name) > 2 && StrTool.codePointAt(this.name, 0) === 95 && StrTool.codePointAt(this.name, 0) === 95) {
            return true;
        }
        return super.isSpecial;
    }

    /**
     * check the redeclaration with the same name
     * @param {Range} range, original range object from the parser, used for error reporting
     *
     * 检查该变量是否可以被重复声明. 注意, 如果发生了重复声明, 新的变量和旧的变量均需要调用该函数.
     */
    override public function redeclare(from:BaseFunctionElement, range:Range = null):void {
        // allow redeclaration
        super.redeclare(from, range);
    }

    /**
     * check the reading from this
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function read(from:BaseFunctionElement, range:Range = null):void {
        // currently nothing to check
    }

    /**
     * check the writing to this
     * constants should override this and throw error
     * @param {BaseFunctionElement} from, the function where this is assigned
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function write(from:BaseFunctionElement, range:Range = null):void {
        this.assigned = true;
        if(from !== this.at) {
            this.closure = true;
        }
    }

    /**
     * original name to python identifier (without closure suffix)
     */
    override public function toRawPython():String {
        if(this.closure) {
            return '__u_' + this.encode();
        }
        return this.toOriginPython();
    }

    /**
     * to python identifier
     */
    override public function toPython():String {
        var clsuf = this.closure ? '.val' : '';
        return this.toRawPython() + clsuf;
    }

    /**
     * original name to python identifier (without closure rename or closure rename)
     */
    public function toOriginPython():String {
        if(!this.isSpecial) {
            return this.name;
        }
        // 对于特殊变量名, 加__v_前缀
        return '__v_' + this.encode();
    }

    /**
     * to string
     */
    override public function toString():String {
        var n = this.name;
        return 'local.' + (n === null ? '?' : n) + (this.closure ? '@closure' : '');
    }

    /**
     * the constructor
     */
    public function LocalVar(name:String, at:BaseFunctionElement, range:Range) {
        super(name, at, range);
    }

}

// #########= ClassTag

/**
 * class's tag
 *
 * 类的标签. 和函数类似, 类也依据局部变量的规则命名, 同时, 类只能定义在全局区域.
 * 类实际上有三个名称:
 * 1. 类自身的类名(即本标签), toPython生成该名字.
 * 2. 类的生成函数, 以__c_为前缀, toFactoryName生成该名字.
 * 3. __clsT, 该变量用于在类内部提供整个作用域可用的类自身指针, 用来作为super的参数.
 */
public class ClassTag extends LocalVar {
    /**
     * check the redeclaration with the same name
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function redeclare(from:BaseFunctionElement, range:Range = null):void {
        throw new ConflictError("Duplicate class definition", range, this.range);
    }

    /**
     * check the writing to this
     * constants should override this and throw error
     * @param {BaseFunctionElement} from, the function holding this tag
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function write(from:BaseFunctionElement, range:Range = null):void {
        throw new ConflictError("Illegal assignment to class definition", range, this.range);
    }

    /**
     * to python identifier
     */
    override public function toPython():String {
        return this.toRawPython();
    }

    /**
     * to string
     */
    override public function toString():String {
        var n = this.name;
        var f = this.at;
        return 'class.' + (n === null ? '?' : n) +
            (f === null ? '' : '[' + this.at.functionToken + ']');
    }

    /**
     * to python identifier for the factory function
     */
    public function toFactoryName():String {
        return '__c_' + this.encode();
    }

    /**
     * the constructor
     */
    public function ClassTag(name:String, target:ClassElement, range:Range) {
        super(name, target, range);
        this.assigned = true;
    }
}

// #########= FunctionTag

/**
 * function's tag
 *
 * 函数定义的标签, 对于匿名的函数表达式, 参见FunctionExpTag
 * YAGS中, 函数定义是提升到函数体顶部的常量, 不能重复定义或者赋值
 * 但在函数内部, 可以定义一个和自身同名的变量或者函数, 但此时将无法递归调用
 * 和严格模式一样, 函数只能在函数体顶层定义
 */
public class FunctionTag extends LocalVar {
    /**
     * check the reading from this
     */
    override public function read(from:BaseFunctionElement, range:Range = null):void {
    }

    /**
     * check the redeclaration with the same name
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function redeclare(from:BaseFunctionElement, range:Range = null):void {
        throw new ConflictError("Duplicate function definition", range, this.range);
    }

    /**
     * check the writing to this
     * constants should override this and throw error
     * @param {BaseFunctionElement} from, the function holding this tag
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function write(from:BaseFunctionElement, range:Range = null):void {
        throw new ConflictError("Illegal assignment to function definition", range, this.range);
    }

    /**
     * to python identifier
     */
    override public function toPython():String {
        return this.toRawPython();
    }

    /**
     * to string
     */
    override public function toString():String {
        var n = this.name;
        var f = this.at;
        return 'def.' + (n === null ? '?' : n) +
            (f === null ? '' : '[' + this.at.functionToken + ']');
    }

    /**
     * the constructor
     */
    public function FunctionTag(name:String, target:FunctionElement, range:Range) {
        super(name, target, range);
        // 函数定义是提升的
        this.assigned = true;
    }
}

// #########= FunctionExpTag

/**
 * function expression's tag
 *
 * 函数表达式的标签
 * Python中没有函数表达式. 在这里, 函数表达式只能由具名函数表示, 因此就需要进行编号以区分不同的函数表达式.
 *
 * 函数表达式需要完整地列出其位置信息, 不然可能会发生混淆.
 * 函数表达式的标签是常量, 在具名的函数表达式内部, 不能对该函数名赋值.
 * 但在函数内部, 可以定义一个和自身同名的变量或者函数, 但此时将无法递归调用, 同时这个函数表达式的名字也没有意义了.
 */
public class FunctionExpTag extends FunctionTag {
    /**
     * check the writing to this
     * constants should override this and throw error
     * @param {BaseFunctionElement} from, the function holding this tag
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function write(from:BaseFunctionElement, range:Range = null):void {
        throw new ConflictError("Illegal assignment to function expression", range, this.range);
    }

    /**
     * to python identifier
     *
     * 函数表达式的标识符前缀是__e
     * 如果是具名的函数表达式, 则编码后的名字放最后
     */
    override public function toRawPython():String {
        var n = this.name;
        var s = '__f' + this.at.functionToken + '_';
        return n === null ? s : s + this.encode();
    }

    /**
     * to comment string
     */
    override public function toComment():String {
        var n = this.name;
        var s = this.toRawPython();
        if(n === null) {
            n = '<anonymous>';
        }
        return n + ' (' + s + ')';
    }

    /**
     * the constructor
     *
     * name可以是null, 对应一个匿名的函数表达式
     */
    public function FunctionExpTag(name:String, target:FunctionExpressionElement, range:Range) {
        super(name, target, range);
    }
}

// #########= GlobalVar

/**
 * superglobal variables
 *
 * 超全局变量, 主要是一些内部工具. 超全局变量是不会被用户代码接触到的. 
 * 超全局变量具有前缀__x, 以便和用户定义变量相区分, 并保证在整个代码范围内均可访问.
 */
public class GlobalVar extends Variable {
    /**
     * check the redeclaration with the same name
     *
     * 检查该变量是否可以被重复声明. 注意, 如果发生了重复声明, 新的变量和旧的变量均需要调用该函数.
     */
    override public function redeclare(from:BaseFunctionElement, range:Range = null):void {
        // 该情况不可能出现
        throw new InternalError('redeclare GlobalVar');
    }

    /**
     * check the reading from this
     */
    override public function read(from:BaseFunctionElement, range:Range = null):void {
    }

    /**
     * check the writing to this
     */
    override public function write(from:BaseFunctionElement, range:Range = null):void {
        throw new InternalError('Illegal assignment to superglobal variables');
    }

    /**
     * original name to python identifier
     */
    override public function toRawPython():String {
        return this.name;
    }

    /**
     * to string
     */
    override public function toString():String {
        var n = this.name;
        return 'global.' + (n === null ? '?' : n);
    }

    /**
     * the constructor
     */
    public function GlobalVar(name:String) {
        super(name, null, null);
        this.assigned = true;
    }
}

// #########= MethodTag

/**
 * method's tag
 *
 * 方法定义的标签
 */
public class MethodTag extends FunctionTag {
    /**
     * is this an accessor
     */
    public var isAccessor:Boolean;

    /**
     * is this setter (ignored when accessor is false)
     */
    public var isSetter:Boolean;

    /**
     * is this a static method
     */
    public var isStatic:Boolean;

    /**
     * is this a public member
     */
    public var isPublic:Boolean;

    /**
     * check the reading from this
     */
    override public function read(from:BaseFunctionElement, range:Range = null):void {
    }

    /**
     * check the redeclaration with the same name
     * @param {Range} range, original range object from the parser, used for error reporting
     */
    override public function redeclare(from:BaseFunctionElement, range:Range = null):void {
        throw new InternalError('declaration of method tag');
    }

    /**
     * to python identifier
     */
    override public function toRawPython():String {
        // 静态方法后移一个字母以区分
        var pf = this.isStatic ?
            (this.isAccessor ? (this.isSetter ? 't' : 'h') : 'n') :
            (this.isAccessor ? (this.isSetter ? 's' : 'g') : 'm');
        return '__' + pf + '_' + this.encode();
    }

    /**
     * to string
     */
    override public function toString():String {
        var n = this.name;
        return (this.isPublic ? 'public.' : 'private.') + (this.isStatic ? 'static.' : '') + (this.isAccessor ? (this.isSetter ? 'setter' : 'getter') : 'method') + '.' + (n === null ? '?' : n);
    }

    /**
     * the constructor
     */
    public function MethodTag(name:String, methodType:String, isStatic:Boolean, isPublic:Boolean, target:MethodElement, range:Range) {
        super(name, target, range);
        var am = new StringMap([['method', false], ['get', true], ['set', true]]);
        this.isAccessor = am.get(methodType);
        this.isSetter = methodType === 'set';
        this.isStatic = isStatic;
        this.isPublic = isPublic;
    }
}

// #########= TempVar

/**
 * temporary variable
 *
 * 临时变量用来存放一些需要简化的表达式的中间结果
 */
public class TempVar extends Variable {
    /**
     * the index of this variable
     */
    public var index:Number;

    /**
     * to python identifier
     *
     * 临时变量的编码是下划线接32进制的序号
     */
    override public function toRawPython():String {
        return '__r' + Identifier.encodeRadix32(this.index);
    }

    /**
     * to string
     */
    override public function toString():String {
        return 'temp[' + StrTool.str(this.index) + ']';
    }

    /**
     * the constructor
     */
    public function TempVar(index:Number, at:BaseFunctionElement) {
        super(null, at, null);
        this.assigned = true;
        this.index = index;
    }
}

