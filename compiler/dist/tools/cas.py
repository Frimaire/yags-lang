# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("CompileError", "InternalError", "conflict", "delayedError", "error", "init", "note", "syntaxError", \
"warn")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global CompileError, InternalError, conflict, delayedError, error, init, note, syntaxError, warn

    # function definitions:

    def showRange(f, position, code):
        l = len(code)
        MAX_LENGTH = 100
        if __x_cb(__x_eq(range, None)):
            return
        # end if
        __r0 = position
        start = __r0.index
        line = __r0.line
        column = __r0.column
        k = 0
        while __x_cb(__x_cb(k <= MAX_LENGTH + 1) and k + start < l):
            if __x_cb(__x_at_has(ES_LINE_TERMINATOR, code[k + start])):
                break
            # end if
            __r1 = k
            k = __x_inc(__r1)
        # end while
        lineStart = start - column
        if __x_cb(lineStart < 0):
            raise InternalError((u"Invalid line start: %d-%d, %d"), start, column, line)
        # end if
        scnt = 0
        while __x_cb(scnt < column):
            if __x_cb(__x_not(__x_at_has(ES_WHITE_SPACE, code[scnt + lineStart]))):
                break
            # end if
            __r2 = scnt
            scnt = __x_inc(__r2)
        # end while
        column = column - scnt
        clipStart = False
        clipEnd = False
        if __x_cb(column + k <= MAX_LENGTH):
            lineStart = start - column
            lineEnd = start + k
            column2 = column
        elif __x_cb(column < 0.7 * MAX_LENGTH):
            lineStart = start - column
            lineEnd = lineStart + MAX_LENGTH
            column2 = column
            clipEnd = True
        elif __x_cb(k < 0.7 * MAX_LENGTH):
            lineEnd = start + k
            lineStart = lineEnd - MAX_LENGTH
            column2 = start - lineStart
            clipStart = True
        else:
            column2 = int(0.4 * MAX_LENGTH)
            lineStart = start - column2
            lineEnd = lineStart + MAX_LENGTH
            clipStart = True
            clipEnd = True
        # end if
        if __x_cb(__x_cb(__x_cb(__x_cb(__x_cb(lineStart < 0) or lineEnd < 0) or lineEnd < lineStart) or column2 < 0) or column2 > lineEnd - lineStart):
            raise InternalError((u"Invalid line position: %d-%d, %d"), lineStart, lineEnd, column2)
        # end if
        s = __x_at_slice(code, lineStart, lineEnd)
        if __x_cb(clipStart):
            s = (u"...") + String.slice(s, 3)
        # end if
        if __x_cb(clipEnd):
            s = String.slice(s, 0, -3) + (u"...")
        # end if
        f.write(s + (u"\n"))
        f.write(reg_nspace.sub((u" "), String.substr(s, 0, column2)) + (u"^\n"))
    # end function showRange

    def init(path, code, errorStream = (None)):
        __u_file__path.val = path
        __u_code__content.val = code
        __u_log__file.val = stderr if __x_cb(__x_eq(errorStream, None)) else errorStream
        __u_lastError.val = None
    # end function init

    def log(type, message, *argv):
        r = None
        m = message
        if __x_cb(__x_eq(message, None)):
            m = String(argv[0])
            argv = __x_at_slice(argv, 1)
        elif __x_cb(__x_iof(message, Marker)):
            r = message
            m = String(argv[0])
            argv = __x_at_slice(argv, 1)
        elif __x_cb(__x_iof(message, Range)):
            r = message.startMarker
            m = String(argv[0])
            argv = __x_at_slice(argv, 1)
        # end if
        m = m % argv
        __u_log__file.val.write(__u_file__path.val + (u":") + ((u"") if __x_cb(__x_eq(r, None)) else r.toString
()) + (u": ") + type + (u": ") + m + (u"\n"))
        if __x_cb(__x_ne(r, None)):
            showRange(__u_log__file.val, r, __u_code__content.val)
        # end if
        return m
    # end function log

    def error(message, *argv):
        __r0 = [(u"Error"), message]
        __r0.extend(argv)
        msg = log(*__r0)
        raise CompileError(msg)
    # end function error

    def syntaxError(message, *argv):
        __r0 = [(u"SyntaxError"), message]
        __r0.extend(argv)
        msg = log(*__r0)
        raise CompileError(msg)
    # end function syntaxError

    def delayedError(message, *argv):
        __r0 = [(u"error"), message]
        __r0.extend(argv)
        msg = log(*__r0)
        __u_lastError.val = CompileError(msg)
    # end function delayedError

    def warn(message, *argv):
        __r0 = [(u"warning"), message]
        __r0.extend(argv)
        log(*__r0)
        if __x_cb(__x_ne(__u_lastError.val, None)):
            raise __u_lastError.val
        # end if
    # end function warn

    def note(message, *argv):
        __r0 = [(u"note"), message]
        __r0.extend(argv)
        log(*__r0)
        if __x_cb(__x_ne(__u_lastError.val, None)):
            raise __u_lastError.val
        # end if
    # end function note

    def conflict(name, oldRange, nowRange):
        delayedError(nowRange, (u"Identifier '%s' has already been declared."), name)
        note(oldRange, (u"'%s' has previously declared here."), name)
    # end function conflict

    # class definitions:

    def __c_CompileError(__cexT):
        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __clsT = __x_dcls("CompileError", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "__init__": __csu})
        return __clsT
    # end class factory CompileError, __c_CompileError

    def __c_InternalError(__cexT):
        def __m_____str____(this):
            try:
                return (u"InternalError: ") + this.args[0] % this.extraInfo
            except __x_errT as e:
                return (u"InternalError: <invalid information>")
            # end try
        # end function __str__(__m_____str____)

        def __m_InternalError(this, message, *extras):
            __csu(this, message)
            this.extraInfo = extras
        # end function __m_InternalError

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __clsT = __x_dcls("InternalError", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("extraInfo",), 
"__str__": __m_____str____, "__init__": __m_InternalError})
        return __clsT
    # end class factory InternalError, __c_InternalError
    __u_code__content = __x_var()
    __u_file__path = __x_var()
    __u_lastError = __x_var()
    __u_log__file = __x_var()

    __r0 = __x_imp((u"sys"))
    stderr = __r0.stderr
    re = __x_imp((u"re"))
    __r1 = __x_imp((u".esstring"))
    String = __r1.String
    ES_LINE_TERMINATOR = __r1.ES_LINE_TERMINATOR
    ES_WHITE_SPACE = __r1.ES_WHITE_SPACE
    __r2 = __x_imp((u".range"))
    Range = __r2.Range
    Marker = __r2.Marker
    reg_nspace = re.compile((u"[^") + __x_at_join(ES_WHITE_SPACE, (u"")) + (u"]"))
    __u_file__path.val = (u"stdin")
    __u_code__content.val = None
    __u_log__file.val = None
    __u_lastError.val = None
    CompileError = __c_CompileError(Exception)
    InternalError = __c_InternalError(Exception)
# program end


__()
