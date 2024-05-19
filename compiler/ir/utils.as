var {ArrayList, StrTool, printf} = import('.compat');
var {StringMap} = import('.StringMap');

/**
 * Error classes and some utilities
 * 错误类和工具
 *
 * There are two major types of errors, InternalError and CompileError.
 * InternalError is due to the bugs in the complier. It shouldn't occur at any input.
 * CompileError is due to the user input. 
 * However, if something wrong should be rejected by the parser but not, InternalError should be thrown.
 * 
 * 错误分为两大类, 内部错误(InternalError)和编译错误(CompileError)
 * 内部错误是因为(编译器的)程序有问题(bug)导致的错误. 如果发现输入存在问题, 而这个问题本该由语法解析器报错的, 也应当产生此等错误.
 * 编译错误则是由输入的问题引起的错误. 正常情况下, 一般的输入问题不应该造成内部错误.
 */
public class InternalError extends Exception {

    public var extraInfo;

    public function InternalError(message, ...extras) {
        super(message);
        this.extraInfo = extras;
    }
}



/**
 * Error caused by the input
 *
 * 编译错误则是由输入的问题引起的错误.
 */
public class CompileError extends Exception {

    public var range:Range;
    public var info:String;

    public function CompileError(format:String, range:Range = null, ...rest) {
        var info = printf(format, rest);
        super(info);
        this.range = range;
        this.info = info;
    }

    public function toString():String {
        if(this.range === null) {
            return 'Line <unknown>: ' + this.info;
        }
        return printf('Line %d: %s', [this.range.startLine, this.info]);
    }

    public function __str__():String {
        return this.toString();
    }
}



/**
 * Error classes for conflict
 *
 * 冲突错误是一种编译错误, 用来对应于存在两个位置的错误.
 * 比如变量重定义, 企图赋值常量.
 */
public class ConflictError extends CompileError {
    public var rangeOrigin:Range;

    public function ConflictError(format:String, rangeOccur:Range = null, rangeOrigin:Range = null, ...rest) {
        super("%s", rangeOccur, printf(format, rest));
        this.rangeOrigin = rangeOrigin;
    }

    override public function toString():String {
        var s = super.toString();
        if(this.rangeOrigin !== null) {
            s += printf(' (originally defined in line %d)', [this.rangeOrigin.startLine]);
        }
        return s;
    }
}



/**
 * class for structure check
 */
public class ElementPattern {
    /**
     * the type of element
     *
     * 当前的类型
     */
    private var type:Class;

    /**
     * expected count of current type, 0 for any (with optional = false means >= 1)
     *
     * 当前类型需要出现的次数, 如果是0就表明可以出现任意次(如果optional是false则表明至少1次)
     */
    private var count:Number;

    /**
     * is this optional
     * if count != 0, this can only occur 0 or count times
     *
     * 当前类型是否是可选的, 如果optional是true且count非零则表明只能出现零次或count次
     */
    private var optional:Boolean;

    /**
     * internal counter
     */
    private var ncnt:Number = 0;

    /**
     * reset the internal counter
     */
    public function reset():void {
        this.ncnt = 0;
    }

    /**
     * check the current element
     * returns true if more element is need
     * returns false if this is satisfyed and e is not processed
     * throws if the element is wrong
     */
    public function meet(e:Element, s:String):Boolean {
        if(this.ncnt > 0 && this.ncnt === this.count) {
            return false;
        }
        if(e !== null && e instanceof this.type) {
            this.ncnt++;
            return true;
        }
        if(this.count === 0 && (this.optional || this.ncnt > 0)) {
            return false;
        }
        if(this.ncnt === 0 && this.optional) {
            return false;
        }
        throw new InternalError('malformed structure in ' + s + ', expected ' + StrTool.str(this.type) + ' but ' + StrTool.typeName(e) + ' is met');
    }

    /**
     * check the end of element
     */
    public function meetEOF(s:String):void {
        if(this.ncnt > 0 && this.ncnt === this.count) {
            return;
        }
        if(this.count === 0 && (this.optional || this.ncnt > 0)) {
            return;
        }
        if(this.ncnt === 0 && this.optional) {
            return;
        }
        throw new InternalError('malformed structure in ' + s + ', expected ' + StrTool.str(this.type) + ' but the end of the current element is met');
    }

    public function ElementPattern(type:Class, count:Number, optional:Boolean) {
        this.type = type;
        this.count = count;
        this.optional = optional;
    }
}



/**
 * the position of the code
 */
public class Range {

    // the position of the first char
    public var start;
    // the position after the last char
    public var end;
    // the first line (start from 1)
    public var startLine;
    // the column of the first char in the first line (start from 0)
    public var startColumn;
    // the last line (start from 1)
    public var endLine;
    // the column of the last char in the last line (start from 0)
    public var endColumn;

    public function Range(start, end, startLine, startColumn, endLine, endColumn) {
        this.start = start;
        this.end = end;
        this.startLine = startLine;
        this.startColumn = startColumn;
        this.endLine = endLine;
        this.endColumn = endColumn;
    }

    public static function fromAST(o) {
        var locs = o.loc;
        var rg = o.range;
        return new Range(
            rg[0],
            rg[1],
            locs.start.line,
            locs.start.column,
            locs.end.line,
            locs.end.column
        );
    }
}



/**
 * dump the IR tree to XML
 */
public class XMLDumper {
    private var all:ArrayList = new ArrayList();
    private var tabCnt:Number = 0;

    // info of current level
    private var attrs:StringMap;
    private var tagName:String;
    private var crange:Range;
    private function init():void {
        this.attrs = new StringMap();
        this.tagName = null;
        this.crange = null;
    }

    /**
     * set the tag name
     */
    public function tag(name:String):void {
        if(this.tagName !== null) {
            throw new InternalError('set the tagname again');
        }
        this.tagName = name;
    }

    /**
     * set the tag name
     */
    public function range(r:Range):void {
        if(this.crange !== null) {
            throw new InternalError('set the range again');
        }
        this.crange = r;
    }

    /**
     * set the attribute
     */
    public function attr(key:String, value:*):void {
        this.attrs.set(key, StrTool.str(value));
    }

    /**
     * add this to XML and convert the children
     */
    public function finalize(e:Element):void {
        // push this tag
        var ttag = this.tagName;

        if(ttag === null) {
            throw new InternalError('tag name is required');
        }
        var a = this.all;
        a.push(this.makeTabs(this.tabCnt) + '<' + ttag);

        // this's attr
        this.attrs.forEach(function(v, n, o) {
            a.push(' ');
            a.push(n);
            a.push('="');
            (new ArrayList(v)).forEach(function(c, k, z) {
                if(c === '<') c = '&lt;';
                if(c === '>') c = '&gt;';
                if(c === '&') c = '&amp;';
                if(c === '\'') c ='&apos;';
                if(c === '"') c ='&quot;';
                a.push(c);
            });
            a.push('"');
        });

        if(this.crange !== null) {
            a.push(' start-line="');
            a.push(StrTool.str(this.crange.startLine));
            a.push('" start-column="');
            a.push(StrTool.str(this.crange.startColumn));
            a.push('" end-line="');
            a.push(StrTool.str(this.crange.endLine));
            a.push('" end-column="');
            a.push(StrTool.str(this.crange.endColumn));
            a.push('"');
        }

        // enter children
        this.all = new ArrayList();
        var tc = this.tabCnt;
        this.tabCnt = tc + 1;

        var has = false;
        var init = this.init;
        var self = this;
        e.forEachChild(function(e, k, s) {
            has = true;
            init();
            e.dump(self);
        });

        // restore the context
        this.tabCnt = tc;
        if(has) {
            a.push('>\n');
            a.push(this.all.join(''));
            a.push(this.makeTabs(tc) + '</' + ttag + '>');
        } else {
            a.push('/>');
        }
        a.push('\n');
        this.all = a;
    }

    public function toString():String {
        return this.all.join('');
    }

    public function XMLDumper() {
        this.init();
    }

    private function makeTabs(n:Number):String {
        // two spaces
        var ts = '  ';
        var s = '';
        while(n-- > 0) {
            s += ts;
        }
        return s;
    }
}



