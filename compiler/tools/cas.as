/*
  Compiler Alerting System
  A module handling the errors and warnings.
*/

var {stderr} = import("sys");
var re = import("re");
var {String, ES_LINE_TERMINATOR, ES_WHITE_SPACE} = import('.esstring');
var {Range, Marker} = import('.range');

var reg_nspace = re.compile("[^" + ES_WHITE_SPACE.@join("") + "]");

var file_path = 'stdin';
var code_content = null;
var log_file = null;
var lastError = null;

/*
  Compile error(s) is an error caused by the input, thrown by error function
 */
public class CompileError extends Exception {
}

/*
  InternalError is due to the bugs in the complier (normally assertation failed). 
  InternalError (and the errors other than CompileError) shouldn't occur at any input.
*/
public class InternalError extends Exception {
    public var extraInfo;

    public function __str__() {
        try {
            return "InternalError: " + this.args[0] % this.extraInfo;
        } catch(e) {
            return "InternalError: <invalid information>";
        }
    }

    public function InternalError(message, ...extras) {
        super(message);
        this.extraInfo = extras;
    }
}

/*
  Write the code near the position specified by `range` in `code` into filestream `f`.
  Two lines will be written:
  1. The line containing the start position of range.
  2. A marker (^) to indicate the start position of range.
  example:
  var x = 10;
      ^
  If the line is too long, it will be clip to nearly 100 characters.
*/
function showRange(f, position, code) {
    var l = len(code);
    var MAX_LENGTH = 100;
    if(range === null) {
        return;
    }
    var {index: start, line, column} = position;
    // find the end of line
    var k = 0;
    while(k <= MAX_LENGTH + 1 && k + start < l) {
        if(ES_LINE_TERMINATOR.@has(code[k + start])) {
            break;
        }
        k++;
    }

    // remove indent
    var lineStart = start - column;
    if(lineStart < 0) {
        throw new InternalError("Invalid line start: %d-%d, %d", start, column, line);
    }
    var scnt = 0;
    while(scnt < column) {
        if(!ES_WHITE_SPACE.@has(code[scnt + lineStart])) {
            break;
        }
        scnt++;
    }
    column -= scnt;
    
    var clipStart = false, clipEnd = false, lineEnd, column2;
    if(column + k <= MAX_LENGTH) {
        // needn't clip
        lineStart = start - column;
        lineEnd = start + k;
        column2 = column;
    } else if(column < 0.7 * MAX_LENGTH) {
        // need clip
        // 1. try clip the tail only, keep column < 0.7 * MAX_LENGTH
        lineStart = start - column;
        lineEnd = lineStart + MAX_LENGTH;
        column2 = column;
        clipEnd = true;
    } else if(k < 0.7 * MAX_LENGTH) {
        // 2. try clip the head only
        lineEnd = start + k;
        lineStart = lineEnd - MAX_LENGTH;
        column2 = start - lineStart;
        clipStart = true;
    } else {
        // 3. clip the both side, make the start at about the 40% position
        column2 = int(0.4 * MAX_LENGTH);
        lineStart = start - column2;
        lineEnd = lineStart + MAX_LENGTH;
        clipStart = true;
        clipEnd = true;
    }

    // if column2 is line length, point to the position after the last character
    if(lineStart < 0 || lineEnd < 0 || lineEnd < lineStart || column2 < 0 || column2 > lineEnd - lineStart) {
        throw new InternalError("Invalid line position: %d-%d, %d", lineStart, lineEnd, column2);
    }
    
    var s = code.@slice(lineStart, lineEnd);
    if(clipStart) {
        s = "..." + String.slice(s, 3);
    }
    if(clipEnd) {
        s = String.slice(s, 0, -3) + "...";
    }
    
    f.write(s + "\n");
    // show the spaces as-is
    f.write(reg_nspace.sub(" ", String.substr(s, 0, column2)) + "^\n");
}

/*
  initialize the reporter
*/
public function init(path, code, errorStream = null) {
    // currently no options
    file_path = path;
    code_content = code;
    log_file = errorStream === null ? stderr : errorStream;
    lastError = null;
}

/*
  A generic message function.
  log(type, [range], format, ...argv)
  `message` is the message to output. 
  Optionally, `message` can be a `Range` or `Marker` object. 
  If so, the second parameter is message. The code near the position specified will be shown.
  The rest parameters will be used for format `message`.
*/
function log(type, message, ...argv) {
    var r = null, m = message;
    if(message === null) {
        // skip null range
        m = String(argv[0]);
        argv = argv.@slice(1);
    } else if(message instanceof Marker) {
        r = message;
        m = String(argv[0]);
        argv = argv.@slice(1);
    } else if(message instanceof Range) {
        r = message.startMarker;
        m = String(argv[0]);
        argv = argv.@slice(1);
    }
    m = m % argv;
    log_file.write(file_path + ":" + (r === null ? "" : r.toString()) + ": " + type + ": " + m + "\n");
    if(r !== null) {
        showRange(log_file, r, code_content);
    }
    return m;
}

/*
  error([range], format, ...argv)
  Show an error and throw a `CompileError` to terminate the compilation.
*/
public function error(message, ...argv) {
    var msg = log("Error", message, ...argv);
    throw new CompileError(msg);
}

/*
  syntaxError([range], format, ...argv)
  Show a syntax error and throw a `CompileError` to terminate the compilation.
*/
public function syntaxError(message, ...argv) {
    var msg = log("SyntaxError", message, ...argv);
    throw new CompileError(msg);
}

/*
  delayedError([range], format, ...argv)
  Show an error message and set `lastError`.
  Normally, `info` is called afterwards, which will throw `lastError`.
  This combination is used to retort the redefinition error.
*/
public function delayedError(message, ...argv) {
    var msg = log("error", message, ...argv);
    lastError = new CompileError(msg);
}

/*
  warn([range], format, ...argv)
  Show a warning.
  If `lasterror` is set, it will be thrown.
*/
public function warn(message, ...argv) {
    log("warning", message, ...argv);
    if(lastError !== null) {
        throw lastError;
    }
}

/*
  note([range], format, ...argv)
  Show a note.
  If `lasterror` is set, it will be thrown.
*/
public function note(message, ...argv) {
    log("note", message, ...argv);
    if(lastError !== null) {
        throw lastError;
    }
}

public function conflict(name, oldRange, nowRange) {
    delayedError(nowRange, "Identifier '%s' has already been declared.", name);
    note(oldRange, "'%s' has previously declared here.", name);
}
