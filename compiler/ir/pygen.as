var {ArrayList, StrTool} = import('.compat');
var {CompileError, ElementPattern, Range, ConflictError, InternalError, XMLDumper} = import('.utils');

/**
* line number anchor
*/
public class LineNumber {
    /**
    * line number
    */
    public var lineNumber:Number = -1;

    /**
    * is put in the context
    */
    public var used:Boolean = false;

    /**
    * the current line or the previous line
    */
    public var prev:Boolean = false;

    public function LineNumber() {
    }
}



/**
 * class for the writer, used by span
 */
public class LineWriter {

    /**
     * the line spans
     */
    public var spans:ArrayList = new ArrayList();

    /**
     * write a span
     * @param {String} source
     * @param {*} linebreak
     *   - true: insert a line break now(without line continuation character)
     *   - false: do not break here
     *   - string: can break line here, insert linebreak (normally backslash) before the line break
     */
    public function write(source:String, linebreak:* = false):void {
        var breakHere, allowBreak, contchar;
        if(linebreak === false) {
            breakHere = false;
            allowBreak = false;
            contchar = null;
        } else if(linebreak === true) {
            breakHere = true;
            allowBreak = false;
            contchar = null;
        } else if(typeof linebreak === 'string') {
            breakHere = false;
            allowBreak = true;
            contchar = linebreak;
        } else {
            throw new InternalError('Illegal linebreak type');
        }
        this.spans.push(new LineSpan(source, breakHere, allowBreak, contchar));
    }

    /**
     * finalize this line
     *
     * @param {PyGenerator} genctx
     */
    public function finalize(genctx:PyGenerator):void {
        if(this.spans.length <= 0) {
            throw new InternalError('empty line');
        }
        var s = '';
        var l = 0;
        var first = true;
        this.spans.forEach(function(e, k, a) {
            s += e.source;
            l += e.length;
            var lb = false;
            if(e.breakHere) {
                lb = true;
                // always disable line break for the last span
            } else if(e.allowBreak && l > LINE_LENGTH && k !== a.length - 1) {
                s += e.contchar;
                lb = true;
            }
            if(lb && k !== a.length - 1) {
                first ? genctx.writeln(s) : genctx.write(s);
                first = false;
                s = '';
                l = 0;
            }
        });
        if(l > 0) {
            first ? genctx.writeln(s) : genctx.write(s);
        }
    }

    public function LineWriter() {
    }

}

/**
 * the maximun length for auto break line
 */
var LINE_LENGTH:Number = 100;

/**
 * class for a slice of the generated line
 */
class LineSpan {
    /**
     * py source
     */
    public var source:String;

    /**
     * source's length
     */
    public var length:Number;

    public var breakHere:Boolean = false;
    public var allowBreak:Boolean = false;
    public var contchar:String = '\\';

    public function LineSpan(source:String, breakHere:Boolean, allowBreak:Boolean, contchar:String) {
        this.source = source;
        this.length = StrTool.strlen(source);
        this.breakHere = breakHere;
        this.allowBreak = allowBreak;
        this.contchar = contchar;
    }
}

/**
 * the python generator
 */
public class PyGenerator {
    /**
     * the code
     */
    public var lines:ArrayList = new ArrayList();

    /**
     * true if add comment
     */
    public var allowComment:Boolean = true;

    /**
     * true if add blank line in some place
     */
    public var allowBlank:Boolean = true;

    /**
     * current indent (count in tabs)
     */
    public var tabs:Number = 0;

    /**
     * valid content in this indent level
     */
    public var outputed:Boolean = false;

    /**
     * tab
     * increase indent
     */
    public function tab():void {
        this.tabs++;
        this.outputed = false;
    }

    /**
     * shift+tab
     * decrease indent
     */
    public function TAB():void {
        // output pass for empty block
        if(!this.outputed) {
            this.writeln('pass');
        }
        this.tabs--;
        if(this.tabs < 0) {
            throw new InternalError('set tabs to negative');
        }
        this.outputed = true;
    }

    /**
     * write a multiline comment
     */
    public function appendComment(s:String):void {
        var sl = '';
        var comment = this.comment;
        (new ArrayList(s)).forEach(function(c, k, a) {
            if(c === '\n') {
                comment('%s', sl);
                sl = '';
                return;
            }
            sl += c;
        });
        if(sl !== '') {
            comment('%s', sl);
        }
    }

    /**
     * write a line comment
     * format:
     * %% : output %
     * %l : the line number (a LineNumber object should be the argument)
     * %s : output the string
     */
    public function comment(format:String, ...argv):void {
        this.lines.push(new Comment(this.tabs, format, new ArrayList(argv)));
        this.outputed = true;
    }

    /**
    * append a line number anchor
    * log the line number of the current line and use it in the comment
    */
    public function logLineNumber(o:LineNumber, prev:Boolean = false):void {
        if(o.used) {
            throw new InternalError('used line number anchor!');
        }
        o.used = true;
        o.prev = prev;
        this.lines.push(o);
    }

    /**
     * write a code line
     */
    public function writeln(line:String):void {
        this.lines.push(new Code(this.tabs, line));
        this.outputed = true;
    }

    /**
     * write a code line, without indent
     */
    public function write(line:String):void {
        this.lines.push(new Code(0, line));
    }

    /**
     * add blank line if necessary
     */
    public function blank():void {
        if(this.outputed) {
            this.lines.push(null);
        }
    }

    /**
    * get the python code
    */
    public function finalize():String {
        var s = '';
        var ln = 0;
        var allowBlank = this.allowBlank;
        // step 1: calculate the line number
        this.lines.forEach(function(line, k, a) {
            if(line instanceof LineNumber) {
                line.lineNumber = ln;
            } else if(line === null && allowBlank) {
                ln++;
            } else {
                ln++;
            }
        });
        // step 2: finalize
        this.lines.forEach(function(line, k, a) {
            if(line instanceof LineNumber) {
                return;
            }
            if(line === null) {
                if(allowBlank) {
                    s += '\n';
                }
                return;
            }
            s += line.finalize();
        });
        return s;
    }

    public function PyGenerator() {
    }
}

/**
 * class for code
 */
class Code {
    /**
     * py source
     */
    public var source:String;

    /**
     * indent (count in tabs)
     */
    public var tabs:Number = 0;

    /**
     * output the converted string
     */
    public function finalize():String {
        return makeTabs(this.tabs) + this.source + '\n';
    }

    /**
     * the constructor
     * @param {String} source
     * @param {Number} tabs
     */
    public function Code(tabs:Number, source:String) {
        this.tabs = tabs;
        this.source = source;
    }
}

/**
 * class for comment
 */
class Comment {
    /**
     * py source
     */
    public var source:String;

    /**
     * indent (count in tabs)
     */
    public var tabs:Number = 0;

    /**
     * arguments
     */
    public var argv:ArrayList;

    /**
     * output the converted string
     */
    public function finalize():String {
        var s = makeTabs(this.tabs) + '# ';
        var p = false;
        var argc = 0;
        var argv = this.argv;
        (new ArrayList(this.source)).forEach(function(c, k, a) {
            if(!p) {
                if(c === '%') {
                    p = true;
                } else {
                    s += c;
                }
                return;
            }
            if(c === '%') {
                s += '%';
            } else if(c === 'l') {
                var e = argv.get(argc++);
                if(!(e.lineNumber > 0 || e.lineNumber === 0 && !e.prev)) {
                    throw new InternalError('uninitialized line number anchor', e);
                }
                s += StrTool.str(e.lineNumber + (e.prev ? 0 : 1));
            } else if(c === 's') {
                s += StrTool.str(argv.get(argc++));
            } else {
                throw new InternalError('unknown comment formatter ' + c);
            }
            p = false;
        });
        if(p) {
            throw new InternalError('unprocessed comment formatter');
        }
        return s + '\n';
    }

    /**
     * the constructor
     * @param {Number} tabs
     * @param {String} source
     * @param {ArrayList} argv
     */
    public function Comment(tabs:Number, source:String, argv:ArrayList) {
        this.tabs = tabs;
        this.source = source;
        this.argv = argv;
    }
}

function makeTabs(n:Number):String {
    // four spaces
    var ts = '    ';
    var s = '';
    while(n-- > 0) {
        s += ts;
    }
    return s;
}

