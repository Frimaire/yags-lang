# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("ArgumentElement", "ArrayElement", "AssignDestructElement", "AssignElement", "AssignTempElement", \
"AttributeElement", "BaseFunctionElement", "BinaryLogicalElement", "BinaryOperatorElement", "BlockElement", \
"BodyElement", "BooleanLiteralElement", "BreakElement", "CallElement", "CatchElement", "ClassElement", \
"ClassGroupElement", "ClassInitElement", "ComplexLiteralElement", "CompoundAssignElement", "ConditionElement", \
"ContinueElement", "DeleteElement", "DestructGroupElement", "DestructObjectElement", "DestructPropertyElement", \
"DoWhileElement", "Element", "ElifElement", "ElseElement", "ExpressionElement", "ExpressionStatementElement", \
"FinallyElement", "FunctionDefinitionElement", "FunctionElement", "FunctionExpressionContainerElement", \
"FunctionExpressionElement", "FunctionGroupElement", "FundamentalLiteralElement", "GlobalElement", "IfBlockElement", \
"IfElement", "ImportElement", "InstanceGroupElement", "InstanceInitializerElement", "ItemElement", "KeyValueElement", \
"LvalueElement", "MagicCallElement", "MethodElement", "MethodGroupElement", "MethodParameterGroupElement", \
"NotOperatorElement", "NullLiteralElement", "NullishCheckElement", "NumberLiteralElement", "ObjectLiteralElement", \
"ParameterAssignElement", "ParameterElement", "ParameterGroupElement", "RestParameterElement", "ReturnElement", \
"SequenceElement", "SpreadElement", "StatementElement", "StaticGroupElement", "StaticInitializerElement", \
"StringLiteralElement", "SuperElement", "TernaryOperatorElement", "ThisElement", "ThrowElement", "TryBlockElement", \
"TryElement", "TupleElement", "UniaryOperatorElement", "UpdateElement", "VarElement", "WhileElement")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global ArgumentElement, ArrayElement, AssignDestructElement, AssignElement, AssignTempElement, AttributeElement, \
BaseFunctionElement, BinaryLogicalElement, BinaryOperatorElement, BlockElement, BodyElement, BooleanLiteralElement, \
BreakElement, CallElement, CatchElement, ClassElement, ClassGroupElement, ClassInitElement, ComplexLiteralElement, \
CompoundAssignElement, ConditionElement, ContinueElement, DeleteElement, DestructGroupElement, DestructObjectElement, \
DestructPropertyElement, DoWhileElement, Element, ElifElement, ElseElement, ExpressionElement, ExpressionStatementElement, \
FinallyElement, FunctionDefinitionElement, FunctionElement, FunctionExpressionContainerElement, FunctionExpressionElement, \
FunctionGroupElement, FundamentalLiteralElement, GlobalElement, IfBlockElement, IfElement, ImportElement, \
InstanceGroupElement, InstanceInitializerElement, ItemElement, KeyValueElement, LvalueElement, MagicCallElement, \
MethodElement, MethodGroupElement, MethodParameterGroupElement, NotOperatorElement, NullLiteralElement, \
NullishCheckElement, NumberLiteralElement, ObjectLiteralElement, ParameterAssignElement, ParameterElement, \
ParameterGroupElement, RestParameterElement, ReturnElement, SequenceElement, SpreadElement, StatementElement, \
StaticGroupElement, StaticInitializerElement, StringLiteralElement, SuperElement, TernaryOperatorElement, \
ThisElement, ThrowElement, TryBlockElement, TryElement, TupleElement, UniaryOperatorElement, UpdateElement, \
VarElement, WhileElement

    # function definitions:

    # class definitions:

    def __c_Element():
        def __n___getNode(this, e):
            return __cpm[e, "stnode"]
        # end function _getNode(__n___getNode)

        def __n___setNode(this, e, node):
            __r0 = e
            __cpm[__r0, "stnode"] = node
        # end function _setNode(__n___setNode)

        def __g_typeName(this):
            return (u"abstract")
        # end function __g_typeName

        def __g_complex(this):
            return True
        # end function __g_complex

        def __g_constantOnly(this):
            return False
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly

        def __g_parent(this):
            return theTree.parent(this)
        # end function __g_parent

        def __g_previousSibling(this):
            return theTree.previousSibling(this)
        # end function __g_previousSibling

        def __g_nextSibling(this):
            return theTree.nextSibling(this)
        # end function __g_nextSibling

        def __g_theStatement(this):
            return None
        # end function __g_theStatement

        def __g_theFunction(this):
            return this.parent.theFunction
        # end function __g_theFunction

        def __g_theClass(this):
            return this.parent.theClass
        # end function __g_theClass

        def __g_theGlobal(this):
            return this.parent.theGlobal
        # end function __g_theGlobal

        def __g_allowThis(this):
            return this.parent.allowThis
        # end function __g_allowThis

        def __g_allowSuper(this):
            return this.parent.allowSuper
        # end function __g_allowSuper

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall

        def __m_remove(this):
            theTree.remove(this)
        # end function __m_remove

        def __g_firstChild(this):
            return theTree.firstChild(this)
        # end function __g_firstChild

        def __g_lastChild(this):
            return theTree.lastChild(this)
        # end function __g_lastChild

        def __m_before(this, e):
            e.remove()
            theTree.insertBefore(this, e)
        # end function __m_before

        def __m_after(this, e):
            e.remove()
            theTree.insertAfter(this, e)
        # end function __m_after

        def __m_append(this, e):
            e.remove()
            theTree.appendChild(this, e)
        # end function __m_append

        def __m_prepend(this, e):
            e.remove()
            theTree.prependChild(this, e)
        # end function __m_prepend

        def __m_replaceWith(this, e):
            if __x_cb(__x_eq(this, e)):
                return
            # end if
            this.before(e)
            this.remove()
        # end function __m_replaceWith

        def __m_forEachChild(this, callback):
            def __fR_(e, k, a):
                return callback(e, k, self)
            # end function <anonymous> (__fR_)

            v = ArrayList()
            it = theTree.childrenIterator(this, False)
            k = 0
            while __x_cb(True):
                nx = it.next()
                if __x_cb(nx.done):
                    break
                # end if
                v.push(nx.value)
                __r0 = k
                k = __x_inc(__r0)
            # end while
            self = this
            v.forEach(__fR_)
        # end function __m_forEachChild

        def __g_structList(this):
            return ArrayList()
        # end function __g_structList

        def __m_checkStruct(this):
            def __fU_(e, n, s):
                while __x_cb(True):
                    if __x_cb(__x_eq(__u_k.val, sl.length)):
                        raise InternalError((u"malformed structure in ") + s.typeName + (u", expected the end of element, but ") + e\
.typeName + (u" is met;"))
                    # end if
                    p = sl.get(__u_k.val)
                    if __x_cb(p.meet(e, s.typeName)):
                        return
                    # end if
                    __r0 = __u_k.val
                    __u_k.val = __x_inc(__r0)
                # end while
            # end function <anonymous> (__fU_)

            __u_k = __x_var()
            sl = this.structList
            __u_k.val = 0
            this.forEachChild(__fU_)
            if __x_cb(__x_eq(sl.length, 0)):
                return
            # end if
            while __x_cb(__u_k.val < sl.length):
                sl.get(__u_k.val).meetEOF(this.typeName)
                __r0 = __u_k.val
                __u_k.val = __x_inc(__r0)
            # end while
        # end function __m_checkStruct

        def __m_checkAllStructure(this):
            def __f10_(e, k, s):
                e.checkAllStructure()
            # end function <anonymous> (__f10_)

            this.checkStruct()
            this.forEachChild(__f10_)
        # end function __m_checkAllStructure

        def __m_declareVariable(this):
            def __f12_(e, k, t):
                e.declareVariable()
            # end function <anonymous> (__f12_)

            this.forEachChild(__f12_)
        # end function __m_declareVariable

        def __m_checkVariables(this):
            def __f14_(e, k, t):
                e.checkVariables()
            # end function <anonymous> (__f14_)

            this.forEachChild(__f14_)
        # end function __m_checkVariables

        def __m_functionalize(this):
            def __f16_(e, k, t):
                e.functionalize()
            # end function <anonymous> (__f16_)

            this.forEachChild(__f16_)
        # end function __m_functionalize

        def __m_simplifyExpressions(this):
            def __f18_(e, k, t):
                e.simplifyExpressions()
            # end function <anonymous> (__f18_)

            this.forEachChild(__f18_)
        # end function __m_simplifyExpressions

        def __m_dump(this, ctx):
            ctx.tag(this.typeName)
            ctx.range(this.range)
            ctx.finalize(this)
        # end function __m_dump

        def __m_generatePython(this, ctx):
            raise InternalError((u"function generatePython in ") + this.typeName + (u" element is abstract"))
        # end function __m_generatePython

        def __m_Element(this, range):
            __csu(this)
            theTree.initialize(this)
            this.range = range
        # end function __m_Element

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "stnode"] = None
            this.range = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("Element", {"__slots__": ("stnode",)})
        __clsT = __x_dcls("Element", __x_objT, {"__slots__": (), "_getNode": __n___getNode, "_setNode": __n___setNode, 
"__init__": __csi}, {"__slots__": ("range",), "after": __m_after, "allowSuper": __x_prop(__g_allowSuper, None), 
"allowSuperCall": __x_prop(__g_allowSuperCall, None), "allowThis": __x_prop(__g_allowThis, None), "append": __m_append, 
"before": __m_before, "checkAllStructure": __m_checkAllStructure, "checkStruct": __m_checkStruct, "checkVariables": __m_checkVariables, 
"complex": __x_prop(__g_complex, None), "constantOnly": __x_prop(__g_constantOnly, None), "declareVariable": __m_declareVariable, 
"dump": __m_dump, "firstChild": __x_prop(__g_firstChild, None), "forEachChild": __m_forEachChild, "functionalize": __m_functionalize, 
"generatePython": __m_generatePython, "lastChild": __x_prop(__g_lastChild, None), "nextSibling": __x_prop(__g_nextSibling, None), 
"parent": __x_prop(__g_parent, None), "prepend": __m_prepend, "previousSibling": __x_prop(__g_previousSibling, None), 
"remove": __m_remove, "replaceWith": __m_replaceWith, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "theClass": __x_prop(__g_theClass, None), 
"theFunction": __x_prop(__g_theFunction, None), "theGlobal": __x_prop(__g_theGlobal, None), "theStatement": __x_prop(__g_theStatement, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_Element})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory Element, __c_Element

    def __c_ExpressionElement(__cexT):
        def __g_typeName(this):
            return (u"exprabstr")
        # end function __g_typeName

        def __g_complex(this):
            def __f1H_(e, i, s):
                if __x_cb(e.complex):
                    __u_c.val = True
                    return False
                # end if
            # end function <anonymous> (__f1H_)

            __u_c = __x_var()
            __u_c.val = False
            this.forEachChild(__f1H_)
            return __u_c.val
        # end function __g_complex

        def __g_theStatement(this):
            return this.parent.theStatement
        # end function __g_theStatement

        def __m_replaceWithTemp(this, optional = (True)):
            if __x_cb(__x_cb(optional) and this.tempVarOnly):
                return None
            # end if
            ate = AssignTempElement(this.theFunction.allocTempVar())
            this.replaceWith(ate.getLeftElement())
            ate.append(this)
            return ate
        # end function __m_replaceWithTemp

        def __m_insertTempAssign(this, e):
            if __x_cb(__x_eq(e, None)):
                return
            # end if
            this.theStatement.before(e)
            e.simplifyExpressions()
        # end function __m_insertTempAssign

        def __m_writePython(this, writer, contchr, parentType = (0)):
            raise InternalError((u"function generatePython in ") + this.typeName + (u" element is abstract"))
        # end function __m_writePython

        def __m_ExpressionElement(this, range):
            __csu(this, range)
        # end function __m_ExpressionElement

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

        __clsT = __x_dcls("ExpressionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"complex": __x_prop(__g_complex, None), "insertTempAssign": __m_insertTempAssign, "replaceWithTemp": __m_replaceWithTemp, 
"theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ExpressionElement})
        return __clsT
    # end class factory ExpressionElement, __c_ExpressionElement

    def __c_SequenceElement(__cexT):
        def __g_typeName(this):
            return (u"sequence-abstract")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 0, True)])
        # end function __g_structList

        def __g_hasSpread(this):
            def __f1T_(e, k, s):
                if __x_cb(__x_iof(e, SpreadElement)):
                    __u_f.val = True
                    return False
                # end if
            # end function <anonymous> (__f1T_)

            __u_f = __x_var()
            __u_f.val = False
            this.forEachChild(__f1T_)
            return __u_f.val
        # end function __g_hasSpread

        def __m_simplifyExpressions(this):
            raise InternalError((u"simplifyExpressions of ") + this.typeName + (u" is abstract"))
        # end function __m_simplifyExpressions

        def __m_makeList(this):
            def __f20_(m, k, s):
                if __x_cb(__x_cb(m.complex) or __x_iof(m, SpreadElement)):
                    __u_lc.val = k
                    return False
                # end if
            # end function <anonymous> (__f20_)

            def __f21_(e, k, s):
                if __x_cb(k < __u_lc.val):
                    init.append(e)
                    return
                # end if
                if __x_cb(__x_iof(e, SpreadElement)):
                    fn = (u"extend")
                    ee = e.firstChild
                else:
                    fn = (u"append")
                    ee = e
                # end if
                e.remove()
                cst = ExpressionStatementElement(None)
                s.theStatement.before(cst)
                cc = CallElement(None)
                cst.append(cc)
                ce = AttributeElement(Attribute(fn, None), None)
                cc.append(ce)
                tve = VarElement.getTempVar(tv)
                ce.append(tve)
                parg = ArgumentElement(None)
                cc.append(parg)
                parg.append(ee)
                cst.simplifyExpressions()
            # end function <anonymous> (__f21_)

            __u_lc = __x_var()
            this.checkStruct()
            __u_lc.val = -1
            this.forEachChild(__f20_)
            if __x_cb(__u_lc.val < 0):
                raise InternalError((u"redundant calling to makeList"))
            # end if
            tv = this.theFunction.allocTempVar()
            ate = AssignTempElement(tv)
            this.insertTempAssign(ate)
            init = ArrayElement(None)
            ate.append(init)
            this.forEachChild(__f21_)
            if __x_cb(__x_ne(this.firstChild, None)):
                raise InternalError((u"unfinished SequenceElement::makeList"))
            # end if
            return tv
        # end function __m_makeList

        def __m_writePython(this, writer, contchr, parentType = (0)):
            def __f23_(m, k, s):
                if __x_cb(k > 0):
                    writer.write((u", "), (u""))
                # end if
                m.writePython(writer, False)
            # end function <anonymous> (__f23_)

            this.forEachChild(__f23_)
        # end function __m_writePython

        def __m_SequenceElement(this, range):
            __csu(this, range)
        # end function __m_SequenceElement

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

        __clsT = __x_dcls("SequenceElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"hasSpread": __x_prop(__g_hasSpread, None), "makeList": __m_makeList, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_SequenceElement})
        return __clsT
    # end class factory SequenceElement, __c_SequenceElement

    def __c_ArgumentElement(__cexT):
        def __g_typeName(this):
            return (u"argument")
        # end function __g_typeName

        def __g_complex(this):
            l = this.firstChild
            r = this.lastChild
            if __x_cb(__x_eq(l, None)):
                return False
            # end if
            if __x_cb(__x_eq(l, r)):
                return this.firstChild.complex
            # end if
            return __x_cb(this.hasSpread) or (super(__clsT, this)).complex
        # end function __g_complex

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_cb(__x_iof(this.parent, CallElement)) or __x_iof(this.parent, MagicCallElement))):
                raise InternalError((u"malformed structure in argument (not in call)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __m_simplifyExpressions(this):
            if __x_cb(__x_not(this.complex)):
                return
            # end if
            l = this.firstChild
            r = this.lastChild
            if __x_cb(__x_eq(l, r)):
                if __x_cb(__x_iof(l, SpreadElement)):
                    l.firstChild.simplifyExpressions()
                else:
                    l.simplifyExpressions()
                # end if
                return
            # end if
            tv = this.makeList()
            sr = SpreadElement(None)
            this.append(sr)
            sr.append(VarElement.getTempVar(tv))
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"("), False)
            (super(__clsT, this)).writePython(writer, (u""))
            writer.write((u")"), contchr)
        # end function __m_writePython

        def __m_ArgumentElement(this, range):
            __csu(this, range)
        # end function __m_ArgumentElement

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

        __clsT = __x_dcls("ArgumentElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "complex": __x_prop(__g_complex, None), "simplifyExpressions": __m_simplifyExpressions, 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_ArgumentElement})
        return __clsT
    # end class factory ArgumentElement, __c_ArgumentElement

    def __c_ArrayElement(__cexT):
        def __g_typeName(this):
            return (u"array")
        # end function __g_typeName

        def __g_complex(this):
            return __x_cb(this.hasSpread) or (super(__clsT, this)).complex
        # end function __g_complex

        def __m_simplifyExpressions(this):
            if __x_cb(__x_not(this.complex)):
                return
            # end if
            tv = this.makeList()
            this.replaceWith(VarElement.getTempVar(tv))
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(this.hasSpread):
                raise InternalError((u"cannot generate python for array with spread syntax"))
            # end if
            writer.write((u"["), False)
            (super(__clsT, this)).writePython(writer, (u""))
            writer.write((u"]"), contchr)
        # end function __m_writePython

        def __m_ArrayElement(this, range):
            __csu(this, range)
        # end function __m_ArrayElement

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

        __clsT = __x_dcls("ArrayElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "complex": __x_prop(__g_complex, None), 
"simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ArrayElement})
        return __clsT
    # end class factory ArrayElement, __c_ArrayElement

    def __c_StatementElement(__cexT):
        def __g_typeName(this):
            return (u"statement-abstract")
        # end function __g_typeName

        def __g_theStatement(this):
            return this
        # end function __g_theStatement

        def __m_StatementElement(this, range):
            __csu(this, range)
        # end function __m_StatementElement

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

        __clsT = __x_dcls("StatementElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_StatementElement})
        return __clsT
    # end class factory StatementElement, __c_StatementElement

    def __c_AssignElement(__cexT):
        def __g_typeName(this):
            return (u"assign")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(LvalueElement, 1, False), ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_checkVariables(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            left.checkWrite()
            right.checkVariables()
        # end function __m_checkVariables

        def __m_simplifyExpressions(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            left.extractLeft()
            right.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            left = this.firstChild
            right = this.lastChild
            left.writePython(writer, False)
            writer.write((u" = "), (u"\\"))
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_AssignElement(this, range):
            __csu(this, range)
        # end function __m_AssignElement

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

        __clsT = __x_dcls("AssignElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_AssignElement})
        return __clsT
    # end class factory AssignElement, __c_AssignElement

    def __c_AssignDestructElement(__cexT):
        def __g_structList(this):
            return ArrayList([ElementPattern(DestructGroupElement, 1, False), ElementPattern(ExpressionElement, 1, 
False)])
        # end function __g_structList

        def __m_checkVariables(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            left.checkVariables()
            right.checkVariables()
        # end function __m_checkVariables

        def __m_simplifyExpressions(this):
            this.checkStruct()
            left = this.firstChild
            left.checkStruct()
            right = this.lastChild
            left.append(right)
            this.before(left)
            left.simplifyExpressions()
            this.remove()
        # end function __m_simplifyExpressions

        def __m_generatePython(this, ctx):
            raise InternalError((u"cannot generate python for AssignDestructElement"))
        # end function __m_generatePython

        def __m_AssignDestructElement(this, range):
            __csu(this, range)
        # end function __m_AssignDestructElement

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

        __clsT = __x_dcls("AssignDestructElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkVariables": __m_checkVariables, "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "__init__": __m_AssignDestructElement})
        return __clsT
    # end class factory AssignDestructElement, __c_AssignDestructElement

    def __c_AssignTempElement(__cexT):
        def __g_typeName(this):
            return (u"assigntemp")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_ne(__cpm[this, "aim"].at, this.theFunction)):
                raise InternalError((u"Mismatched scope for AssignTempElement"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __m_checkVariables(this):
            raise InternalError((u"Illegal stage 1 for AssignTempElement"))
        # end function __m_checkVariables

        def __m_getLeftElement(this):
            return VarElement.getTempVar(__cpm[this, "aim"])
        # end function __m_getLeftElement

        def __m_dump(this, ctx):
            ctx.attr((u"target"), __cpm[this, "aim"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            left = __cpm[this, "aim"]
            right = this.firstChild
            writer.write(__cpm[this, "aim"].toPython(), False)
            writer.write((u" = "), (u"\\"))
            right.writePython(writer, False)
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_AssignTempElement(this, aim):
            __csu(this, None)
            __cpm[this, "aim"] = aim
        # end function __m_AssignTempElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "aim"] = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("AssignTempElement", {"__slots__": ("aim",)})
        __clsT = __x_dcls("AssignTempElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "checkVariables": __m_checkVariables, "dump": __m_dump, "generatePython": __m_generatePython, 
"getLeftElement": __m_getLeftElement, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_AssignTempElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory AssignTempElement, __c_AssignTempElement

    def __c_LvalueElement(__cexT):
        def __g_typeName(this):
            return (u"lvalue-abstract")
        # end function __g_typeName

        def __m_checkWrite(this):
            this.checkVariables()
        # end function __m_checkWrite

        def __g_declarator(this):
            return False
        # end function __g_declarator

        def __m_extractLeft(this):
            raise InternalError((u"extractLeft is abstract in ") + this.typeName)
        # end function __m_extractLeft

        def __m_extractLeftAndDuplicate(this):
            raise InternalError((u"extractLeftAndDuplicate is abstract in ") + this.typeName)
        # end function __m_extractLeftAndDuplicate

        def __m_dump(this, ctx):
            ctx.attr((u"declare"), this.declarator)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_LvalueElement(this, range):
            __csu(this, range)
        # end function __m_LvalueElement

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

        __clsT = __x_dcls("LvalueElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkWrite": __m_checkWrite, 
"declarator": __x_prop(__g_declarator, None), "dump": __m_dump, "extractLeft": __m_extractLeft, "extractLeftAndDuplicate": __m_extractLeftAndDuplicate, 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_LvalueElement})
        return __clsT
    # end class factory LvalueElement, __c_LvalueElement

    def __c_AttributeElement(__cexT):
        def __g_typeName(this):
            return (u"attribute")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_extractLeft(this):
            this.checkStruct()
            left = this.firstChild
            ate = left.replaceWithTemp()
            this.insertTempAssign(ate)
            this.checkStruct()
        # end function __m_extractLeft

        def __m_extractLeftAndDuplicate(this):
            this.checkStruct()
            left = this.firstChild
            ate = left.replaceWithTemp(False)
            this.insertTempAssign(ate)
            v = AttributeElement(__cpm[this, "attribute"], this.range)
            v.append(ate.getLeftElement())
            this.checkStruct()
            return v
        # end function __m_extractLeftAndDuplicate

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_writePython(this, writer, contchr, parentType = (0)):
            cls = this.theClass
            pi = False if __x_cb(__x_eq(cls, None)) else cls.hasPrivateInstance(__cpm[this, "attribute"].name)
            ps = False if __x_cb(__x_eq(cls, None)) else cls.hasPrivateStatic(__cpm[this, "attribute"].name)
            object = this.firstChild
            if __x_cb(__x_cb(pi) and ps):
                psk = (u"__cpg")
            elif __x_cb(pi):
                psk = (u"__cpm")
            elif __x_cb(ps):
                psk = (u"__csg")
            # end if
            if __x_cb(__x_cb(pi) or ps):
                writer.write(psk, False)
                writer.write((u"["), False)
                object.writePython(writer, (u""))
                writer.write((u", \""), False)
                writer.write(__cpm[this, "attribute"].toPython(), False)
                writer.write((u"\"]"), contchr)
            else:
                object.writePython(writer, (u"\\"), 12)
                writer.write((u"."), False)
                writer.write(__cpm[this, "attribute"].toPython(), contchr)
            # end if
        # end function __m_writePython

        def __m_AttributeElement(this, attribute, range):
            __csu(this, range)
            __cpm[this, "attribute"] = attribute
        # end function __m_AttributeElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("AttributeElement", {"__slots__": ("attribute",)})
        __clsT = __x_dcls("AttributeElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"dump": __m_dump, "extractLeft": __m_extractLeft, "extractLeftAndDuplicate": __m_extractLeftAndDuplicate, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_AttributeElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory AttributeElement, __c_AttributeElement

    def __c_BaseFunctionElement(__cexT):
        def __g_typeName(this):
            return (u"basefunction")
        # end function __g_typeName

        def __g_functionToken(this):
            return encodeRadix32(__cpm[this, "functionId"])
        # end function __g_functionToken

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall

        def __g_theFunction(this):
            return this
        # end function __g_theFunction

        def __g_parentFunction(this):
            return this.parent.theFunction
        # end function __g_parentFunction

        def __g_functionDefinitions(this):
            raise InternalError(this.typeName + (u" have no inner function definition area"))
        # end function __g_functionDefinitions

        def __g_body(this):
            raise InternalError(this.typeName + (u" have no function body"))
        # end function __g_body

        def __m_getLocal(this, name):
            return __cpm[this, "vars"].get(name, None)
        # end function __m_getLocal

        def __m_setLocal(this, name, v):
            if __x_cb(__x_eq(v, None)):
                raise InternalError((u"set a null variable"))
            # end if
            __cpm[this, "vars"].set(name, v)
        # end function __m_setLocal

        def __m_registerFunctionDefinition(this, tag):
            if __x_cb(__x_not(__x_iof(tag, FunctionTag))):
                raise InternalError((u"Not a function tag!"))
            # end if
            name = tag.name
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                CAS.conflict(name, v.range, tag.range)
            # end if
            this.setLocal(name, tag)
        # end function __m_registerFunctionDefinition

        def __m_registerLocalVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                CAS.conflict(name, v.range, range)
            # end if
            v = LocalVar(name, range)
            __r0 = v
            __r0.at = this
            this.setLocal(name, v)
            return v
        # end function __m_registerLocalVar

        def __m_forEachLocalVar(this, callback):
            def __f4R_(e, k, a):
                return callback(e, k, self)
            # end function <anonymous> (__f4R_)

            self = this
            __cpm[this, "vars"].forEach(__f4R_)
        # end function __m_forEachLocalVar

        def __m_referVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar

        def __m_allocTempVar(this):
            __r0 = this
            __r1 = __cpm[__r0, "tempCounter"]
            __cpm[__r0, "tempCounter"] = __x_inc(__r1)
            tid = __r1
            return TempVar(tid, this)
        # end function __m_allocTempVar

        def __m_declareVariable(this):
            __cpm[this, "functionId"] = this.theGlobal.allocFunctionId()
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_dump(this, ctx):
            ctx.attr((u"id"), __cpm[this, "functionId"])
            ctx.attr((u"tempcnt"), __cpm[this, "tempCounter"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_BaseFunctionElement(this, range):
            __csu(this, range)
        # end function __m_BaseFunctionElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "vars"] = StringMap()
            __cpm[this, "assignedPublic"] = StringMap()
            __cpm[this, "functionId"] = 0
            __cpm[this, "tempCounter"] = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("BaseFunctionElement", {"__slots__": ("assignedPublic", "functionId", "tempCounter"
, "vars")})
        __clsT = __x_dcls("BaseFunctionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allocTempVar": __m_allocTempVar, "allowSuperCall": __x_prop(__g_allowSuperCall, None), "body": __x_prop(__g_body, None), 
"declareVariable": __m_declareVariable, "dump": __m_dump, "forEachLocalVar": __m_forEachLocalVar, "functionDefinitions": __x_prop(__g_functionDefinitions, None), 
"functionToken": __x_prop(__g_functionToken, None), "getLocal": __m_getLocal, "parentFunction": __x_prop(__g_parentFunction, None), 
"referVar": __m_referVar, "registerFunctionDefinition": __m_registerFunctionDefinition, "registerLocalVar": __m_registerLocalVar, 
"setLocal": __m_setLocal, "theFunction": __x_prop(__g_theFunction, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_BaseFunctionElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory BaseFunctionElement, __c_BaseFunctionElement

    def __c_BinaryOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"binary")
        # end function __g_typeName

        def __g_constantOnly(this):
            return __x_cb(this.firstChild.constantOnly) and this.lastChild.constantOnly
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            op = __cpm[this, "source"]
            a = this.firstChild
            b = this.lastChild
            opfMap = StringMap([[(u"instanceof"), (u"__x_iof")], [(u"==="), (u"__x_eq")], [(u"!=="), (u"__x_ne")]])
            fn = opfMap.get(op, None)
            if __x_cb(__x_eq(fn, None)):
                return
            # end if
            cc = CallElement(None)
            this.replaceWith(cc)
            callee = VarElement.getGlobalVar(fn)
            cc.append(callee)
            argv = ArgumentElement(None)
            cc.append(argv)
            argv.append(a)
            argv.append(b)
            cc.checkStruct()
        # end function __m_functionalize

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(__x_not(this.complex)):
                return
            # end if
            left = this.firstChild
            right = this.lastChild
            op = __cpm[this, "source"]
            if __x_cb(right.complex):
                ale = left.replaceWithTemp()
                this.insertTempAssign(ale)
                right.simplifyExpressions()
            else:
                left.simplifyExpressions()
            # end if
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            oppMap = StringMap([[(u"+"), 8], [(u"-"), 8], [(u"*"), 9], [(u"/"), 9], [(u"%"), 9], [(u"**"), 9], [(u">>"), 
7], [(u"<<"), 7], [(u"&"), 6], [(u"^"), 5], [(u"|"), 4], [(u"=="), 3], [(u"!="), 3], [(u"<="), 3], [(u"<"), 
3], [(u">="), 3], [(u">"), 3]])
            op = __cpm[this, "source"]
            left = this.firstChild
            right = this.lastChild
            if __x_cb(__x_not(oppMap.has(op))):
                raise InternalError((u"Cannot writePython for binary ") + op)
            # end if
            p = oppMap.get(op)
            lp = p
            rp = p + 1
            if __x_cb(__x_eq(op, (u"**"))):
                lp = 11
                rp = 11
            # end if
            if __x_cb(__x_eq(p, 3)):
                lp = 4
                rp = 4
            # end if
            ap = p < parentType
            lsp = (u"") if __x_cb(ap) else contchr
            if __x_cb(ap):
                writer.write((u"("), False)
            # end if
            left.writePython(writer, lsp, lp)
            writer.write((u" ") + op + (u" "), lsp)
            right.writePython(writer, lsp, rp)
            if __x_cb(ap):
                writer.write((u")"), contchr)
            # end if
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_BinaryOperatorElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_BinaryOperatorElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("BinaryOperatorElement", {"__slots__": ("source",)})
        __clsT = __x_dcls("BinaryOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "dump": __m_dump, "functionalize": __m_functionalize, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_BinaryOperatorElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory BinaryOperatorElement, __c_BinaryOperatorElement

    def __c_BinaryLogicalElement(__cexT):
        def __g_typeName(this):
            return (u"logic")
        # end function __g_typeName

        def __g_complex(this):
            if __x_cb(options.enableImplicitBooleanConversion):
                return True
            # end if
            return __x_cb(__x_eq(__cpm[this, "source"], (u"??"))) or (super(__clsT, this)).complex
        # end function __g_complex

        def __g_constantOnly(this):
            return __x_cb(this.firstChild.constantOnly) and this.lastChild.constantOnly
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            op = __cpm[this, "source"]
            a = this.firstChild
            b = this.lastChild
            if __x_cb(__x_cb(__x_not(options.enableImplicitBooleanConversion)) and (__x_cb(__x_eq(op, (u"&&"))) or 
__x_eq(op, (u"||")))):
                chk = CallElement.callGlobal((u"__x_cb"), a)
                this.prepend(chk)
                this.checkStruct()
            # end if
        # end function __m_functionalize

        def __m_simplifyExpressionsImplicitBooleanConversion(this):
            left = this.firstChild
            right = this.lastChild
            op = __cpm[this, "source"]
            atva = this.theFunction.allocTempVar()
            atvl = AssignTempElement(atva)
            this.theStatement.before(atvl)
            atvl.append(left)
            atvl.simplifyExpressions()
            ife = IfBlockElement(None)
            this.theStatement.before(ife)
            iife = IfElement(None)
            ife.append(iife)
            acond = ConditionElement(None)
            iife.append(acond)
            if __x_cb(__x_eq(op, (u"&&"))):
                acond.append(CallElement.callGlobal((u"__x_tob"), atvl.getLeftElement()))
            elif __x_cb(__x_eq(op, (u"||"))):
                acond.append(CallElement.callGlobal((u"__x_tnb"), atvl.getLeftElement()))
            elif __x_cb(__x_eq(op, (u"??"))):
                acondnc = NullishCheckElement(None)
                acond.append(acondnc)
                acondnc.append(atvl.getLeftElement())
            # end if
            atrue = BodyElement(None)
            iife.append(atrue)
            atvr = AssignTempElement(atva)
            atrue.append(atvr)
            atvr.append(right)
            ife.simplifyExpressions()
            this.replaceWith(atvl.getLeftElement())
        # end function __m_simplifyExpressionsImplicitBooleanConversion

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(options.enableImplicitBooleanConversion):
                __cpm[this, "simplifyExpressionsImplicitBooleanConversion"]()
                return
            # end if
            if __x_cb(__x_not(this.complex)):
                return
            # end if
            left = this.firstChild
            right = this.lastChild
            op = __cpm[this, "source"]
            atva = this.theFunction.allocTempVar()
            atvl = AssignTempElement(atva)
            this.theStatement.before(atvl)
            atvl.append(left)
            atvl.simplifyExpressions()
            ife = IfBlockElement(None)
            this.theStatement.before(ife)
            iife = IfElement(None)
            ife.append(iife)
            acond = ConditionElement(None)
            iife.append(acond)
            if __x_cb(__x_eq(op, (u"&&"))):
                acond.append(atvl.getLeftElement())
            elif __x_cb(__x_eq(op, (u"||"))):
                acondor = NotOperatorElement(None)
                acond.append(acondor)
                acondor.append(atvl.getLeftElement())
            elif __x_cb(__x_eq(op, (u"??"))):
                acondnc = NullishCheckElement(None)
                acond.append(acondnc)
                acondnc.append(atvl.getLeftElement())
            # end if
            atrue = BodyElement(None)
            iife.append(atrue)
            atvr = AssignTempElement(atva)
            atrue.append(atvr)
            atvr.append(right)
            ife.simplifyExpressions()
            this.replaceWith(atvl.getLeftElement())
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            op = __cpm[this, "source"]
            left = this.firstChild
            right = this.lastChild
            if __x_cb(__x_cb(__x_eq(op, (u"||"))) or __x_eq(op, (u"&&"))):
                ap = 2 <= parentType
                lsp = (u"") if __x_cb(ap) else contchr
                if __x_cb(ap):
                    writer.write((u"("), False)
                # end if
                left.writePython(writer, lsp, 3)
                writer.write((u" or ") if __x_cb(__x_eq(op, (u"||"))) else (u" and "), lsp)
                right.writePython(writer, lsp, 2)
                if __x_cb(ap):
                    writer.write((u")"), contchr)
                # end if
            else:
                raise InternalError((u"Cannot writePython for logic ") + op)
            # end if
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_BinaryLogicalElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_BinaryLogicalElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("BinaryLogicalElement", {"__slots__": ("source",), "simplifyExpressionsImplicitBooleanConversion": __x_smet(__m_simplifyExpressionsImplicitBooleanConversion)})
        __clsT = __x_dcls("BinaryLogicalElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "complex": __x_prop(__g_complex, None), "constantOnly": __x_prop(__g_constantOnly, None), "dump": __m_dump, 
"functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_BinaryLogicalElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory BinaryLogicalElement, __c_BinaryLogicalElement

    def __c_BlockElement(__cexT):
        def __g_typeName(this):
            return (u"block")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(StatementElement, 0, True)])
        # end function __g_structList

        def __m_generatePython(this, ctx):
            def __f61_(e, k, t):
                e.generatePython(ctx)
            # end function <anonymous> (__f61_)

            this.forEachChild(__f61_)
        # end function __m_generatePython

        def __m_BlockElement(this, range):
            __csu(this, range)
        # end function __m_BlockElement

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

        __clsT = __x_dcls("BlockElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_BlockElement})
        return __clsT
    # end class factory BlockElement, __c_BlockElement

    def __c_BodyElement(__cexT):
        def __g_typeName(this):
            return (u"body")
        # end function __g_typeName

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall

        def __g_structList(this):
            return ArrayList([ElementPattern(StatementElement, 0, True)])
        # end function __g_structList

        def __m_generatePython(this, ctx):
            def __f6A_(e, k, t):
                e.generatePython(ctx)
            # end function <anonymous> (__f6A_)

            this.forEachChild(__f6A_)
        # end function __m_generatePython

        def __m_BodyElement(this, range):
            __csu(this, range)
        # end function __m_BodyElement

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

        __clsT = __x_dcls("BodyElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "allowSuperCall": __x_prop(__g_allowSuperCall, None), 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_BodyElement})
        return __clsT
    # end class factory BodyElement, __c_BodyElement

    def __c_FundamentalLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"literal-abstract")
        # end function __g_typeName

        def __g_complex(this):
            return False
        # end function __g_complex

        def __g_constantOnly(this):
            return True
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return True
        # end function __g_tempVarOnly

        def __m_replaceWithTemp(this, optional = (True)):
            if __x_cb(optional):
                return None
            # end if
            return (super(__clsT, this)).replaceWithTemp(False)
        # end function __m_replaceWithTemp

        def __m_FundamentalLiteralElement(this, range):
            __csu(this, range)
        # end function __m_FundamentalLiteralElement

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

        __clsT = __x_dcls("FundamentalLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "complex": __x_prop(__g_complex, None), "constantOnly": __x_prop(__g_constantOnly, None), "replaceWithTemp": __m_replaceWithTemp, 
"tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_FundamentalLiteralElement})
        return __clsT
    # end class factory FundamentalLiteralElement, __c_FundamentalLiteralElement

    def __c_BooleanLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"boolean")
        # end function __g_typeName

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"True") if __x_cb(__cpm[this, "value"]) else (u"False"), contchr)
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"value"), __cpm[this, "value"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_BooleanLiteralElement(this, value, range):
            __csu(this, range)
            __cpm[this, "value"] = value
        # end function __m_BooleanLiteralElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("BooleanLiteralElement", {"__slots__": ("value",)})
        __clsT = __x_dcls("BooleanLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_BooleanLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory BooleanLiteralElement, __c_BooleanLiteralElement

    def __c_BreakElement(__cexT):
        def __m_generatePython(this, ctx):
            ctx.writeln((u"break"))
        # end function __m_generatePython

        def __m_BreakElement(this, range):
            __csu(this, range)
        # end function __m_BreakElement

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

        __clsT = __x_dcls("BreakElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"__init__": __m_BreakElement})
        return __clsT
    # end class factory BreakElement, __c_BreakElement

    def __c_CallElement(__cexT):
        def __g_typeName(this):
            return (u"call")
        # end function __g_typeName

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False), ElementPattern(ArgumentElement, 1, False)])
        # end function __g_structList

        def __m_checkVariables(this):
            callee = this.firstChild
            argv = this.lastChild
            supcall = __x_iof(this.firstChild, SuperElement)
            if __x_cb(__x_not(supcall)):
                callee.checkVariables()
            elif __x_cb(__x_not(this.allowSuperCall)):
                CAS.error(this.range, (u"super() statement unexpected here"))
            # end if
            argv.checkVariables()
            if __x_cb(supcall):
                fn = this.theFunction
                fn.meetSuper(this.range)
            # end if
        # end function __m_checkVariables

        def __m_functionalize(this):
            (super(__clsT, this)).functionalize()
            supcall = __x_iof(this.firstChild, SuperElement)
            if __x_cb(supcall):
                argv = this.lastChild
                argv.prepend(ThisElement(None))
            # end if
        # end function __m_functionalize

        def __m_simplifyExpressions(this):
            callee = this.firstChild
            argv = this.lastChild
            supcall = __x_iof(this.firstChild, SuperElement)
            if __x_cb(argv.complex):
                if __x_cb(__x_not(supcall)):
                    callee2 = callee.replaceWithTemp()
                    this.insertTempAssign(callee2)
                # end if
                argv.simplifyExpressions()
            elif __x_cb(callee.complex):
                callee.simplifyExpressions()
            # end if
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            callee = this.firstChild
            supcall = __x_iof(this.firstChild, SuperElement)
            argv = this.lastChild
            if __x_cb(supcall):
                writer.write((u"__csu"), False)
            else:
                callee.writePython(writer, contchr, 12)
            # end if
            argv.writePython(writer, contchr, 12)
        # end function __m_writePython

        def __m_CallElement(this, range):
            __csu(this, range)
        # end function __m_CallElement

        def __n_callGlobal(this, name, arg):
            cc = CallElement(None)
            callee = VarElement.getGlobalVar(name)
            cc.append(callee)
            argv = ArgumentElement(None)
            cc.append(argv)
            argv.append(arg)
            return cc
        # end function __n_callGlobal

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

        __clsT = __x_dcls("CallElement", __cexT, {"__slots__": (), "callGlobal": __n_callGlobal, "__init__": __csi}, 
{"__slots__": (), "allowSuperCall": __x_prop(__g_allowSuperCall, None), "checkVariables": __m_checkVariables, 
"functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_CallElement})
        return __clsT
    # end class factory CallElement, __c_CallElement

    def __c_CatchElement(__cexT):
        def __g_typeName(this):
            return (u"catch")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 1, True), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, TryBlockElement))):
                raise InternalError((u"malformed structure in CatchElement (not in TryBlockElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __m_generatePython(this, gen):
            writer = LineWriter()
            writer.write((u"except __x_errT as "), False)
            ex = this.firstChild
            body = this.lastChild
            if __x_cb(__x_eq(ex, body)):
                writer.write(this.theFunction.allocTempVar().toRawPython(), False)
            else:
                ex.writePython(writer, (u""))
            # end if
            writer.write((u":"), False)
            writer.finalize(gen)
            gen.tab()
            ex.generateRenameAssignment(gen)
            body.generatePython(gen)
            gen.TAB()
        # end function __m_generatePython

        def __m_CatchElement(this, range):
            __csu(this, range)
        # end function __m_CatchElement

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

        __clsT = __x_dcls("CatchElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_CatchElement})
        return __clsT
    # end class factory CatchElement, __c_CatchElement

    def __c_ClassElement(__cexT):
        def __g_typeName(this):
            return (u"class")
        # end function __g_typeName

        def __g_theClass(this):
            return this
        # end function __g_theClass

        def __g_structList(this):
            return ArrayList([ElementPattern(MethodGroupElement, 1, False), ElementPattern(StaticGroupElement, 1, 
False), ElementPattern(InstanceGroupElement, 1, False)])
        # end function __g_structList

        def __g_allowThis(this):
            return True
        # end function __g_allowThis

        def __g_allowSuper(this):
            return True
        # end function __g_allowSuper

        def __g_allowSuperCall(this):
            return __cpm[this, "hasSuper"]
        # end function __g_allowSuperCall

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions

        def __g_staticInit(this):
            this.checkStruct()
            e = this.firstChild.nextSibling
            return e
        # end function __g_staticInit

        def __g_instanceInit(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_instanceInit

        def __g_body(this):
            return None
        # end function __g_body

        def __m_referVar(this, name, range = (None)):
            if __x_cb(__x_eq(this.tag.name, name)):
                return this.tag
            # end if
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar

        def __m_registerFunctionDefinition(this, tag):
            def coerce(tag):
                if __x_cb(__x_not(__x_iof(tag, MethodTag))):
                    raise InternalError((u"only method is allowed in class"))
                # end if
                return tag
            # end function coerce

            tag2 = coerce(tag)
            st = tag2.isStatic
            o = __cpm[this, "staticMembers"] if __x_cb(st) else __cpm[this, "instanceMembers"]
            n = tag2.name
            cfd = o.get(n, None)
            if __x_cb(__x_eq(cfd, None)):
                cfd = ClassFieldDescriptor(n, tag2.range, st)
                o.set(n, cfd)
            # end if
            cfd.meetMethod(tag2)
        # end function __m_registerFunctionDefinition

        def __m_registerLocalVar(this, name, range = (None)):
            raise InternalError((u"only property is allowed in class"))
        # end function __m_registerLocalVar

        def __m_registerProperty(this, name, isPublic, isStatic, range):
            st = isStatic
            n = name
            o = __cpm[this, "staticMembers"] if __x_cb(st) else __cpm[this, "instanceMembers"]
            cfd = o.get(n, None)
            if __x_cb(__x_eq(cfd, None)):
                cfd = ClassFieldDescriptor(n, range, st)
                o.set(n, cfd)
            # end if
            cfd.meetProperty(isPublic, range)
        # end function __m_registerProperty

        def __m_hasPrivateInstance(this, name):
            o = __cpm[this, "instanceMembers"]
            cfd = o.get(name, None)
            if __x_cb(__x_eq(cfd, None)):
                return False
            # end if
            return cfd.isPrivate
        # end function __m_hasPrivateInstance

        def __m_hasPrivateStatic(this, name):
            o = __cpm[this, "staticMembers"]
            cfd = o.get(name, None)
            if __x_cb(__x_eq(cfd, None)):
                return False
            # end if
            return cfd.isPrivate
        # end function __m_hasPrivateStatic

        def __m_declareVariable(this):
            if __x_cb(__x_not(__x_iof(this.parentFunction, GlobalElement))):
                raise InternalError((u"Public member not in global"))
            # end if
            this.theGlobal.registerClassDefinition(this.tag, this.tag.range)
            if __x_cb(__cpm[this, "isPublic"]):
                this.theGlobal.declarePublic(this.tag.name, this.tag.range)
            # end if
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_createClassInitElement(this):
            return ClassInitElement(__cpm[this, "hasSuper"], this.tag, this.tag.range)
        # end function __m_createClassInitElement

        def __m_generatePython(this, gen):
            def __f8C_(p, k, s):
                if __x_cb(p.isPrivate):
                    __u_haspi.val = True
                    return False
                # end if
            # end function <anonymous> (__f8C_)

            def __f8D_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and p.isPrivate)):
                    return
                # end if
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u"\\"))
                # end if
                writer.write((u"\"") + p.toPython() + (u"\""), (u""))
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8D_)

            def __f8E_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and p.isPrivate)):
                    return
                # end if
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                if __x_cb(p.isMethod):
                    writer.write((u"__x_smet("), False)
                # end if
                writer.write(p.toMethodName(), False)
                if __x_cb(p.isMethod):
                    writer.write((u")"), False)
                # end if
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8E_)

            def __f8F_(p, k, s):
                if __x_cb(p.isPrivate):
                    __u_hasps.val = True
                    return False
                # end if
            # end function <anonymous> (__f8F_)

            def __f8G_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and p.isPrivate)):
                    return
                # end if
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u""))
                # end if
                writer.write((u"\"") + p.toPython() + (u"\""), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8G_)

            def __f8H_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and p.isPrivate)):
                    return
                # end if
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                writer.write(p.toMethodName(), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8H_)

            def __f8I_(p, k, s):
                if __x_cb(__x_not(p.isPrivate)):
                    return
                # end if
                p2 = sm.get(k, None)
                if __x_cb(__x_cb(__x_ne(p2, None)) and p2.isPrivate):
                    __u_haspis.val = True
                    return False
                # end if
            # end function <anonymous> (__f8I_)

            def __f8J_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and __x_not(p.isPrivate))):
                    return
                # end if
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u""))
                # end if
                writer.write((u"\"") + p.toPython() + (u"\""), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8J_)

            def __f8K_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and __x_not(p.isPrivate))):
                    return
                # end if
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                writer.write(p.toMethodName(), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8K_)

            def __f8L_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and __x_not(p.isPrivate))):
                    return
                # end if
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u""))
                # end if
                writer.write((u"\"") + p.toPython() + (u"\""), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8L_)

            def __f8M_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and __x_not(p.isPrivate))):
                    return
                # end if
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                writer.write(p.toMethodName(), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8M_)

            def __f8N_(f, k, a):
                if __x_cb(f.isConstructor):
                    __u_ctag.val = f.tag
                    return False
                # end if
            # end function <anonymous> (__f8N_)

            __u_ctag = __x_var()
            __u_haspi = __x_var()
            __u_haspis = __x_var()
            __u_hasps = __x_var()
            __u_ppl = __x_var()
            sm = __cpm[this, "staticMembers"]
            im = __cpm[this, "instanceMembers"]
            gen.blank()
            writer = LineWriter()
            writer.write((u"def "), False)
            writer.write(this.tag.toFactoryName(), False)
            writer.write((u"("), (u""))
            if __x_cb(__cpm[this, "hasSuper"]):
                writer.write((u"__cexT"), (u""))
            # end if
            writer.write((u"):"), False)
            writer.finalize(gen)
            gen.tab()
            this.functionDefinitions.generatePython(gen)
            this.staticInit.generatePython(gen)
            this.instanceInit.generatePython(gen)
            gen.blank()
            __u_haspi.val = False
            im.forEach(__f8C_)
            if __x_cb(__u_haspi.val):
                writer = LineWriter()
                writer.write((u"__cpiT = __x_dpif("), False)
                writer.write((u"\"") + this.tag.toPython() + (u"\""), False)
                writer.write((u", "), (u""))
                writer.write((u"{"), (u""))
                writer.write((u"\"__slots__\": ("), (u""))
                __u_ppl.val = 0
                im.forEach(__f8D_)
                if __x_cb(__x_eq(__u_ppl.val, 1)):
                    writer.write((u","), False)
                # end if
                writer.write((u")"), (u""))
                __u_ppl.val = 0
                im.forEach(__f8E_)
                writer.write((u"})"), False)
                writer.finalize(gen)
            # end if
            __u_hasps.val = False
            sm.forEach(__f8F_)
            if __x_cb(__u_hasps.val):
                writer = LineWriter()
                writer.write((u"__cpsT = __x_dpsf("), False)
                writer.write((u"\"") + this.tag.toPython() + (u"\""), False)
                writer.write((u", "), (u""))
                writer.write((u"{"), (u""))
                writer.write((u"\"__slots__\": ("), (u""))
                __u_ppl.val = 0
                sm.forEach(__f8G_)
                if __x_cb(__x_eq(__u_ppl.val, 1)):
                    writer.write((u","), False)
                # end if
                writer.write((u")"), False)
                __u_ppl.val = 0
                sm.forEach(__f8H_)
                writer.write((u"})"), False)
                writer.finalize(gen)
                gen.writeln((u"__csp = __cpsT()"))
            # end if
            __u_haspis.val = False
            im.forEach(__f8I_)
            writer = LineWriter()
            writer.write((u"__clsT = __x_dcls("), False)
            writer.write((u"\"") + this.tag.toPython() + (u"\""), False)
            writer.write((u", "), (u""))
            writer.write((u"__cexT") if __x_cb(__cpm[this, "hasSuper"]) else (u"__x_objT"), False)
            writer.write((u", "), False)
            writer.write((u"{"), (u""))
            writer.write((u"\"__slots__\": ("), (u""))
            __u_ppl.val = 0
            sm.forEach(__f8J_)
            if __x_cb(__x_eq(__u_ppl.val, 1)):
                writer.write((u","), False)
            # end if
            writer.write((u")"), False)
            __u_ppl.val = 0
            sm.forEach(__f8K_)
            writer.write((u", "), (u""))
            writer.write((u"\"__init__\": __csi"), False)
            writer.write((u"}, "), (u""))
            writer.write((u"{"), (u""))
            writer.write((u"\"__slots__\": ("), (u""))
            __u_ppl.val = 0
            im.forEach(__f8L_)
            if __x_cb(__x_eq(__u_ppl.val, 1)):
                writer.write((u","), False)
            # end if
            writer.write((u")"), False)
            __u_ppl.val = 0
            im.forEach(__f8M_)
            __u_ctag.val = None
            this.functionDefinitions.forEachChild(__f8N_)
            writer.write((u", "), (u""))
            if __x_cb(__x_eq(__u_ctag.val, None)):
                writer.write((u"\"__init__\": __csu"), False)
            else:
                writer.write((u"\"__init__\": "), False)
                writer.write(__u_ctag.val.toPython(), False)
            # end if
            writer.write((u"})"), False)
            writer.finalize(gen)
            if __x_cb(__u_haspi.val):
                gen.writeln((u"__cpm = __x_prmT(__clsT, __cpiT)"))
            # end if
            if __x_cb(__u_hasps.val):
                gen.writeln((u"__csg = __x_csgT(__clsT, __csp)"))
            # end if
            if __x_cb(__u_haspis.val):
                gen.writeln((u"__cpg = __x_cpgT(__clsT, __cpm, __csp)"))
            # end if
            gen.writeln((u"return __clsT"))
            gen.TAB()
            gen.comment((u"end class factory %s, %s"), this.tag.toPython(), this.tag.toFactoryName())
        # end function __m_generatePython

        def __m_dump(this, ctx):
            ctx.attr((u"tag"), this.tag)
            ctx.attr((u"public"), __cpm[this, "isPublic"])
            ctx.attr((u"extended"), __cpm[this, "hasSuper"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_ClassElement(this, tag, hasSuper, isPublic, range):
            __csu(this, range)
            this.tag = tag
            __r0 = tag
            __r0.at = this
            __cpm[this, "isPublic"] = isPublic
            __cpm[this, "hasSuper"] = hasSuper
            this.append(MethodGroupElement())
            this.append(StaticGroupElement())
            this.append(InstanceGroupElement(__cpm[this, "instanceMembers"]))
        # end function __m_ClassElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            this.tag = None
            __cpm[this, "isPublic"] = False
            __cpm[this, "hasSuper"] = False
            __cpm[this, "instanceMembers"] = StringMap()
            __cpm[this, "staticMembers"] = StringMap()
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("ClassElement", {"__slots__": ("hasSuper", "instanceMembers", "isPublic", "staticMembers"
)})
        __clsT = __x_dcls("ClassElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("tag",), 
"allowSuper": __x_prop(__g_allowSuper, None), "allowSuperCall": __x_prop(__g_allowSuperCall, None), "allowThis": __x_prop(__g_allowThis, None), 
"body": __x_prop(__g_body, None), "createClassInitElement": __m_createClassInitElement, "declareVariable": __m_declareVariable, 
"dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), "generatePython": __m_generatePython, 
"hasPrivateInstance": __m_hasPrivateInstance, "hasPrivateStatic": __m_hasPrivateStatic, "instanceInit": __x_prop(__g_instanceInit, None), 
"referVar": __m_referVar, "registerFunctionDefinition": __m_registerFunctionDefinition, "registerLocalVar": __m_registerLocalVar, 
"registerProperty": __m_registerProperty, "staticInit": __x_prop(__g_staticInit, None), "structList": __x_prop(__g_structList, None), 
"theClass": __x_prop(__g_theClass, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ClassElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ClassElement, __c_ClassElement

    def __c_ClassGroupElement(__cexT):
        def __g_typeName(this):
            return (u"classgroup")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ClassElement, 0, True)])
        # end function __g_structList

        def __m_ClassGroupElement(this):
            __csu(this, None)
        # end function __m_ClassGroupElement

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

        __clsT = __x_dcls("ClassGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ClassGroupElement})
        return __clsT
    # end class factory ClassGroupElement, __c_ClassGroupElement

    def __c_ClassInitElement(__cexT):
        def __g_typeName(this):
            return (u"classinit")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, __x_not(__cpm[this, "extended"]))])
        # end function __g_structList

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            writer.write(__cpm[this, "tag"].toPython(), False)
            writer.write((u" = "), (u"\\"))
            writer.write(__cpm[this, "tag"].toFactoryName(), False)
            writer.write((u"("), (u"\\"))
            if __x_cb(__cpm[this, "extended"]):
                sup = this.firstChild
                sup.writePython(writer, False)
            # end if
            writer.write((u")"), (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_dump(this, ctx):
            ctx.attr((u"tag"), __cpm[this, "tag"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_ClassInitElement(this, extended, tag, range):
            __csu(this, range)
            __cpm[this, "extended"] = extended
            __cpm[this, "tag"] = tag
        # end function __m_ClassInitElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("ClassInitElement", {"__slots__": ("extended", "tag")})
        __clsT = __x_dcls("ClassInitElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"dump": __m_dump, "generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_ClassInitElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ClassInitElement, __c_ClassInitElement

    def __c_ComplexLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"imag")
        # end function __g_typeName

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(parentType >= 12):
                writer.write((u"("), False)
            # end if
            s = ArrayList(__cpm[this, "source"])
            s.set(-1, (u"j"))
            writer.write(s.join((u"")), False)
            if __x_cb(parentType >= 12):
                writer.write((u")"), False)
            # end if
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"source"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_ComplexLiteralElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_ComplexLiteralElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("ComplexLiteralElement", {"__slots__": ("source",)})
        __clsT = __x_dcls("ComplexLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_ComplexLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ComplexLiteralElement, __c_ComplexLiteralElement

    def __c_CompoundAssignElement(__cexT):
        def __m_simplifyExpressions(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            ae = AssignElement(this.range)
            this.replaceWith(ae)
            ae.append(left)
            rv = left.extractLeftAndDuplicate()
            re = BinaryOperatorElement(__cpm[this, "operator"], None)
            ae.append(re)
            re.append(rv)
            re.append(right)
            re.simplifyExpressions()
            re.checkStruct()
            ae.checkStruct()
        # end function __m_simplifyExpressions

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "operator"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_generatePython(this, ctx):
            raise InternalError((u"cannot generate Python for CompoundAssignElement"))
        # end function __m_generatePython

        def __m_CompoundAssignElement(this, operator, range):
            __csu(this, range)
            m = StringMap([[(u"*="), (u"*")], [(u"**="), (u"**")], [(u"/="), (u"/")], [(u"%="), (u"%")], [(u"+="), 
(u"+")], [(u"-="), (u"-")], [(u"<<="), (u"<<")], [(u">>="), (u">>")], [(u"&="), (u"&")], [(u"^="), (u"^")], 
[(u"|="), (u"|")]])
            if __x_cb(__x_not(m.has(operator))):
                raise InternalError((u"unknown assignment operator ") + operator)
            # end if
            __cpm[this, "operator"] = m.get(operator)
        # end function __m_CompoundAssignElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("CompoundAssignElement", {"__slots__": ("operator",)})
        __clsT = __x_dcls("CompoundAssignElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"__init__": __m_CompoundAssignElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory CompoundAssignElement, __c_CompoundAssignElement

    def __c_ConditionElement(__cexT):
        def __g_typeName(this):
            return (u"cond")
        # end function __g_typeName

        def __g_theStatement(this):
            return this.parent.theStatement
        # end function __g_theStatement

        def __g_complex(this):
            this.checkStruct()
            return this.firstChild.complex
        # end function __g_complex

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            exp = this.firstChild
            cc = CallElement.callGlobal((u"__x_tob") if __x_cb(options.enableImplicitBooleanConversion) else (u"__x_cb"), 
exp)
            this.append(cc)
            this.checkStruct()
        # end function __m_functionalize

        def __m_simplifyExpressions(this):
            raise InternalError((u"cannot simplifyExpressions of ConditionElement"))
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            exp = this.firstChild
            exp.writePython(writer, contchr, parentType)
        # end function __m_writePython

        def __m_ConditionElement(this, range):
            __csu(this, range)
        # end function __m_ConditionElement

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

        __clsT = __x_dcls("ConditionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"complex": __x_prop(__g_complex, None), "functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_ConditionElement})
        return __clsT
    # end class factory ConditionElement, __c_ConditionElement

    def __c_ContinueElement(__cexT):
        def __m_generatePython(this, ctx):
            ctx.writeln((u"continue"))
        # end function __m_generatePython

        def __m_ContinueElement(this, range):
            __csu(this, range)
        # end function __m_ContinueElement

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

        __clsT = __x_dcls("ContinueElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"generatePython": __m_generatePython, "__init__": __m_ContinueElement})
        return __clsT
    # end class factory ContinueElement, __c_ContinueElement

    def __c_DeleteElement(__cexT):
        def __g_typeName(this):
            return (u"return")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_checkVariables(this):
            if __x_cb(__x_not(__x_iof(this.firstChild, LvalueElement))):
                CAS.error(this.range, (u"only left value can be deleted"))
            # end if
            (super(__clsT, this)).checkVariables()
        # end function __m_checkVariables

        def __m_generatePython(this, ctx):
            right = this.lastChild
            writer = LineWriter()
            writer.write((u"del "), False)
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_DeleteElement(this, range):
            __csu(this, range)
        # end function __m_DeleteElement

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

        __clsT = __x_dcls("DeleteElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DeleteElement})
        return __clsT
    # end class factory DeleteElement, __c_DeleteElement

    def __c_DestructGroupElement(__cexT):
        def __g_typeName(this):
            return (u"destrabstract")
        # end function __g_typeName

        def __g_declarator(this):
            return __cpm[this, "_declarator"]
        # end function __g_declarator

        def __m_checkStruct(this):
            def __fAK_(e, k, s):
                if __x_cb(__x_iof(e, DestructPropertyElement)):
                    if __x_cb(__x_ne(e.declarator, s.declarator)):
                        raise InternalError((u"malformed structure in ") + s.typeName + (u" (mismatched declarator property)"))
                    # end if
                else:
                    raise InternalError((u"malformed structure in ") + s.typeName + (u" (unknown child)"))
                # end if
            # end function <anonymous> (__fAK_)

            (super(__clsT, this)).checkStruct()
            this.forEachChild(__fAK_)
        # end function __m_checkStruct

        def __m_simplifyExpressions(this):
            raise InternalError((u"call abstract simplifyExpressions to ") + this.typeName)
        # end function __m_simplifyExpressions

        def __m_dump(this, ctx):
            ctx.attr((u"declare"), this.declarator)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_DestructGroupElement(this, declarator, range):
            __csu(this, range)
            __cpm[this, "_declarator"] = declarator
        # end function __m_DestructGroupElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("DestructGroupElement", {"__slots__": ("_declarator",)})
        __clsT = __x_dcls("DestructGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "declarator": __x_prop(__g_declarator, None), "dump": __m_dump, "simplifyExpressions": __m_simplifyExpressions, 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_DestructGroupElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory DestructGroupElement, __c_DestructGroupElement

    def __c_DestructObjectElement(__cexT):
        def __g_typeName(this):
            return (u"destrobj")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(DestructPropertyElement, 0, False)])
        # end function __g_structList

        def __m_simplifyExpressions(this):
            def __fAU_(e, k, s):
                e.checkStruct()
                e.append(ate.getLeftElement())
                s.before(e)
                e.simplifyExpressions()
            # end function <anonymous> (__fAU_)

            ate = AssignTempElement(this.theFunction.allocTempVar())
            this.before(ate)
            right = this.lastChild
            ate.append(right)
            ate.simplifyExpressions()
            this.forEachChild(__fAU_)
            this.remove()
        # end function __m_simplifyExpressions

        def __m_DestructObjectElement(this, declarator, range):
            __csu(this, declarator, range)
        # end function __m_DestructObjectElement

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

        __clsT = __x_dcls("DestructObjectElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DestructObjectElement})
        return __clsT
    # end class factory DestructObjectElement, __c_DestructObjectElement

    def __c_DestructPropertyElement(__cexT):
        def __g_declarator(this):
            return __cpm[this, "_declarator"]
        # end function __g_declarator

        def __g_typeName(this):
            return (u"destrprop")
        # end function __g_typeName

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, DestructObjectElement))):
                raise InternalError((u"malformed structure in DestructPropertyElement (not in DestructObjectElement)"))
            # end if
            e = this.firstChild
            if __x_cb(__x_cb(__x_ne(e, this.lastChild)) or __x_not(__x_cb(__x_iof(e, LvalueElement)) or __x_iof(e, 
DestructGroupElement))):
                raise InternalError((u"malformed structure in ") + this.typeName + (u" (unknown child)"))
            # end if
            if __x_cb(__x_ne(e.declarator, this.declarator)):
                raise InternalError((u"malformed structure in ") + this.typeName + (u" (disagreed declarator property)"))
            # end if
        # end function __m_checkStruct

        def __m_checkVariables(this):
            this.checkStruct()
            e = this.firstChild
            if __x_cb(__x_iof(e, LvalueElement)):
                e.checkWrite()
            else:
                e.checkVariables()
            # end if
        # end function __m_checkVariables

        def __m_simplifyExpressions(this):
            e = this.firstChild
            ro = this.lastChild
            re = AttributeElement(__cpm[this, "attribute"], None)
            re.append(ro)
            if __x_cb(__x_iof(e, LvalueElement)):
                dae = AssignElement(this.range)
                this.before(dae)
                dae.append(e)
                dae.append(re)
                dae.simplifyExpressions()
            elif __x_cb(__x_iof(e, DestructGroupElement)):
                ate = AssignTempElement(this.theFunction.allocTempVar())
                this.before(ate)
                ate.append(re)
                this.before(e)
                e.append(ate.getLeftElement())
                e.simplifyExpressions()
            else:
                raise InternalError((u"malformed structure in DestructPropertyElement (unknown child)"))
            # end if
            this.remove()
        # end function __m_simplifyExpressions

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            ctx.attr((u"declare"), this.declarator)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_DestructPropertyElement(this, declarator, attribute, range):
            __csu(this, range)
            __cpm[this, "_declarator"] = declarator
            __cpm[this, "attribute"] = attribute
        # end function __m_DestructPropertyElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("DestructPropertyElement", {"__slots__": ("_declarator", "attribute")})
        __clsT = __x_dcls("DestructPropertyElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "checkVariables": __m_checkVariables, "declarator": __x_prop(__g_declarator, None), 
"dump": __m_dump, "simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DestructPropertyElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory DestructPropertyElement, __c_DestructPropertyElement

    def __c_DoWhileElement(__cexT):
        def __g_typeName(this):
            return (u"dowhile")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __m_simplifyExpressions(this):
            this.checkStruct()
            cond = this.firstChild
            cond.checkStruct()
            body = this.lastChild
            nwhile = WhileElement(this.range)
            this.replaceWith(nwhile)
            nwhile.append(cond)
            conde = cond.firstChild
            conde.replaceWith(BooleanLiteralElement(True, None))
            ife = IfBlockElement(None)
            body.append(ife)
            iife = IfElement(None)
            ife.append(iife)
            acond = ConditionElement(None)
            iife.append(acond)
            acondn = NotOperatorElement(None)
            acond.append(acondn)
            acondn.append(conde)
            atrue = BodyElement(None)
            iife.append(atrue)
            abreak = BreakElement(None)
            atrue.append(abreak)
            (super(__clsT, this)).simplifyExpressions()
        # end function __m_simplifyExpressions

        def __m_generatePython(this, gen):
            raise InternalError((u"generate python for do-while"))
        # end function __m_generatePython

        def __m_DoWhileElement(this, range):
            __csu(this, range)
        # end function __m_DoWhileElement

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

        __clsT = __x_dcls("DoWhileElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DoWhileElement})
        return __clsT
    # end class factory DoWhileElement, __c_DoWhileElement

    def __c_ElifElement(__cexT):
        def __g_typeName(this):
            return (u"elif")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, IfBlockElement))):
                raise InternalError((u"malformed structure in IfElement (not in IfBlockElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __g_complex(this):
            return this.firstChild.complex
        # end function __g_complex

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(this.complex):
                raise InternalError((u"simplify a elif with complex condition"))
            # end if
            body = this.lastChild
            body.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions

        def __m_generatePython(this, ctx):
            cond = this.firstChild.firstChild
            body = this.lastChild
            writer = LineWriter()
            writer.write((u"elif "), False)
            cond.writePython(writer, (u"\\"), 1)
            writer.write((u":"), False)
            writer.finalize(ctx)
            ctx.tab()
            body.generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython

        def __m_ElifElement(this, range):
            __csu(this, range)
        # end function __m_ElifElement

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

        __clsT = __x_dcls("ElifElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"complex": __x_prop(__g_complex, None), "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ElifElement})
        return __clsT
    # end class factory ElifElement, __c_ElifElement

    def __c_ElseElement(__cexT):
        def __g_typeName(this):
            return (u"else")
        # end function __g_typeName

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, IfBlockElement))):
                raise InternalError((u"malformed structure in IfElement (not in IfBlockElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __m_generatePython(this, ctx):
            ctx.writeln((u"else:"))
            ctx.tab()
            (super(__clsT, this)).generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython

        def __m_ElseElement(this, range):
            __csu(this, range)
        # end function __m_ElseElement

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

        __clsT = __x_dcls("ElseElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "typeName": __x_prop(__g_typeName, None), "__init__": __m_ElseElement})
        return __clsT
    # end class factory ElseElement, __c_ElseElement

    def __c_ExpressionStatementElement(__cexT):
        def __g_typeName(this):
            return (u"exprstat")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall

        def __m_simplifyExpressions(this):
            (super(__clsT, this)).simplifyExpressions()
            c = this.lastChild
            if __x_cb(__x_cb(c.tempVarOnly) or (__x_cb(__x_iof(c, VarElement)) and c.declarator)):
                this.remove()
            # end if
        # end function __m_simplifyExpressions

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            right = this.lastChild
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_ExpressionStatementElement(this, range):
            __csu(this, range)
        # end function __m_ExpressionStatementElement

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

        __clsT = __x_dcls("ExpressionStatementElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuperCall": __x_prop(__g_allowSuperCall, None), "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ExpressionStatementElement})
        return __clsT
    # end class factory ExpressionStatementElement, __c_ExpressionStatementElement

    def __c_FinallyElement(__cexT):
        def __g_typeName(this):
            return (u"finally")
        # end function __g_typeName

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, TryBlockElement))):
                raise InternalError((u"malformed structure in TryElement (not in TryBlockElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
            __cpm[this, "checkJump"](this)
        # end function __m_checkStruct

        def __m_checkJump(this, e):
            def __fCI_(ee, k, a):
                cj(ee)
            # end function <anonymous> (__fCI_)

            if __x_cb(__x_cb(__x_cb(__x_iof(e, ReturnElement)) or __x_iof(e, BreakElement)) or __x_iof(e, ContinueElement)):
                CAS.error(this.range, (u"Jump statements occur in finally block"))
            # end if
            if __x_cb(__x_iof(e, ExpressionElement)):
                return
            # end if
            cj = __cpm[this, "checkJump"]
            e.forEachChild(__fCI_)
        # end function __m_checkJump

        def __m_generatePython(this, ctx):
            ctx.writeln((u"finally:"))
            ctx.tab()
            (super(__clsT, this)).generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython

        def __m_FinallyElement(this, range):
            __csu(this, range)
        # end function __m_FinallyElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("FinallyElement", {"__slots__": (), "checkJump": __x_smet(__m_checkJump)})
        __clsT = __x_dcls("FinallyElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "typeName": __x_prop(__g_typeName, None), "__init__": __m_FinallyElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory FinallyElement, __c_FinallyElement

    def __c_FunctionElement(__cexT):
        def __g_typeName(this):
            return (u"function")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(ParameterGroupElement, 
1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions

        def __g_parameters(this):
            this.checkStruct()
            e = this.firstChild.nextSibling
            return e
        # end function __g_parameters

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body

        def __m_referVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if
            if __x_cb(__x_cb(__x_ne(this.tag.name, None)) and __x_eq(this.tag.name, name)):
                return this.tag
            # end if
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar

        def __m_generatePython(this, gen):
            def __fCV_(v, n, s):
                if __x_cb(__x_not(v.closure)):
                    return
                # end if
                gen.writeln(v.toRawPython() + (u" = __x_var()"))
            # end function <anonymous> (__fCV_)

            def __fD0_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    CAS.warn(v.range, (u"Variable %s is never initialized."), v.name)
                    __u_nwv.val = True
                # end if
            # end function <anonymous> (__fD0_)

            def __fD1_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    gen.writeln(v.toRawPython() + (u" = 0"))
                # end if
            # end function <anonymous> (__fD1_)

            __u_nwv = __x_var()
            gen.blank()
            writer = LineWriter()
            writer.write((u"def "), False)
            writer.write(this.tag.toPython(), False)
            writer.write((u"("), (u""))
            this.parameters.toPrameterList(writer, (u""))
            writer.write((u"):"), False)
            writer.finalize(gen)
            gen.tab()
            this.functionDefinitions.generatePython(gen)
            gen.blank()
            this.forEachLocalVar(__fCV_)
            this.parameters.generatePython(gen)
            this.body.generatePython(gen)
            __u_nwv.val = False
            this.forEachLocalVar(__fD0_)
            if __x_cb(__u_nwv.val):
                gen.comment((u"Uninitialized variable:"))
                gen.writeln((u"return"))
                this.forEachLocalVar(__fD1_)
            # end if
            gen.TAB()
            gen.comment((u"end function %s"), this.tag.toComment())
        # end function __m_generatePython

        def __m_dump(this, ctx):
            ctx.attr((u"tag"), this.tag)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_FunctionElement(this, range):
            __csu(this, range)
        # end function __m_FunctionElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # initialize properties
            this.tag = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __clsT = __x_dcls("FunctionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("tag",), 
"body": __x_prop(__g_body, None), "dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), 
"generatePython": __m_generatePython, "parameters": __x_prop(__g_parameters, None), "referVar": __m_referVar, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_FunctionElement})
        return __clsT
    # end class factory FunctionElement, __c_FunctionElement

    def __c_FunctionDefinitionElement(__cexT):
        def __m_declareVariable(this):
            this.parentFunction.registerFunctionDefinition(this.tag)
            if __x_cb(__cpm[this, "isPublic"]):
                if __x_cb(__x_not(__x_iof(this.parentFunction, GlobalElement))):
                    raise InternalError((u"Public member not in global"))
                # end if
                this.theGlobal.declarePublic(this.tag.name, this.tag.range)
            # end if
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_dump(this, ctx):
            ctx.attr((u"public"), __cpm[this, "isPublic"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_FunctionDefinitionElement(this, tag, isPublic, range):
            __csu(this, range)
            this.tag = tag
            __r0 = tag
            __r0.at = this
            __cpm[this, "isPublic"] = isPublic
            this.append(FunctionGroupElement())
            this.append(ParameterGroupElement())
            this.append(BodyElement(None))
        # end function __m_FunctionDefinitionElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "isPublic"] = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("FunctionDefinitionElement", {"__slots__": ("isPublic",)})
        __clsT = __x_dcls("FunctionDefinitionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "declareVariable": __m_declareVariable, "dump": __m_dump, "__init__": __m_FunctionDefinitionElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory FunctionDefinitionElement, __c_FunctionDefinitionElement

    def __c_FunctionExpressionElement(__cexT):
        def __m_FunctionExpressionElement(this, tag, range):
            __csu(this, range)
            this.tag = tag
            __r0 = tag
            __r0.at = this
            this.append(FunctionGroupElement())
            this.append(ParameterGroupElement())
            this.append(BodyElement(None))
        # end function __m_FunctionExpressionElement

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

        __clsT = __x_dcls("FunctionExpressionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "__init__": __m_FunctionExpressionElement})
        return __clsT
    # end class factory FunctionExpressionElement, __c_FunctionExpressionElement

    def __c_FunctionExpressionContainerElement(__cexT):
        def __g_tag(this):
            return this.functionBody.tag
        # end function __g_tag

        def __g_functionBody(this):
            return this.firstChild
        # end function __g_functionBody

        def __m_writePython(this, writer, contchr, parentType = (0)):
            raise InternalError((u"cannot generate the code for FunctionExpressionElement"))
        # end function __m_writePython

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionExpressionElement, 1, False)])
        # end function __g_structList

        def __m_declareVariable(this):
            tag = VarElement.getFunctionExp(this.tag)
            fn = this.functionBody
            this.theFunction.functionDefinitions.append(fn)
            fn.declareVariable()
            this.replaceWith(tag)
            tag.declareVariable()
        # end function __m_declareVariable

        def __m_FunctionExpressionContainerElement(this, tag, range):
            __csu(this, range)
            this.append(FunctionExpressionElement(tag, range))
        # end function __m_FunctionExpressionContainerElement

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

        __clsT = __x_dcls("FunctionExpressionContainerElement", __cexT, {"__slots__": (), "__init__": __csi}, 
{"__slots__": (), "declareVariable": __m_declareVariable, "functionBody": __x_prop(__g_functionBody, None), 
"structList": __x_prop(__g_structList, None), "tag": __x_prop(__g_tag, None), "writePython": __m_writePython, 
"__init__": __m_FunctionExpressionContainerElement})
        return __clsT
    # end class factory FunctionExpressionContainerElement, __c_FunctionExpressionContainerElement

    def __c_FunctionGroupElement(__cexT):
        def __g_typeName(this):
            return (u"functiongroup")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionElement, 0, True)])
        # end function __g_structList

        def __m_FunctionGroupElement(this):
            __csu(this, None)
        # end function __m_FunctionGroupElement

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

        __clsT = __x_dcls("FunctionGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_FunctionGroupElement})
        return __clsT
    # end class factory FunctionGroupElement, __c_FunctionGroupElement

    def __c_GlobalElement(__cexT):
        def __g_typeName(this):
            return (u"global")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(ClassGroupElement, 1, 
False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions

        def __g_classDefinitions(this):
            this.checkStruct()
            e = this.firstChild.nextSibling
            return e
        # end function __g_classDefinitions

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body

        def __g_parent(this):
            return None
        # end function __g_parent

        def __g_theGlobal(this):
            return this
        # end function __g_theGlobal

        def __g_theClass(this):
            return None
        # end function __g_theClass

        def __g_parentFunction(this):
            return None
        # end function __g_parentFunction

        def __g_allowThis(this):
            return False
        # end function __g_allowThis

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall

        def __m_allocFunctionId(this):
            __r0 = this
            __r1 = __cpm[__r0, "functionCounter"]
            __cpm[__r0, "functionCounter"] = __x_inc(__r1)
            return __r1
        # end function __m_allocFunctionId

        def __m_registerClassDefinition(this, tag, range = (None)):
            name = tag.name
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                CAS.conflict(name, v.range, tag.range)
            # end if
            this.setLocal(name, tag)
        # end function __m_registerClassDefinition

        def __m_declarePublic(this, name, range):
            if __x_cb(__x_cb(isSpecial(name)) or isKeyword(name)):
                CAS.error(range, (u"public name must be a valid Python identifier: %s"), name)
            # end if
            an = ArrayList(name)
            if __x_cb(__x_cb(__x_eq(an.get(0), (u"_"))) and an.get(1) == (u"_")):
                CAS.error(range, (u"public name starts with double underscore is reserved: %s"), name)
            # end if
            ov = __cpm[this, "exports"].get(name, False)
            if __x_cb(ov):
                CAS.delayedError(range, (u"Duplicate public variable declaration: %s"), name)
                CAS.note(ov.range, (u"'%s' has previously declared here."), name)
            # end if
            __cpm[this, "exports"].set(name, True)
        # end function __m_declarePublic

        def __m_referVar(this, name, range = (None)):
            if __x_cb(__x_eq(name, (u"eval"))):
                CAS.error(range, (u"Eval is evil"))
            # end if
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if
            v2 = __cpm[this, "builtins"].get(name, None)
            if __x_cb(__x_ne(v2, None)):
                return v2
            # end if
            CAS.error(range, (u"%s is not defined"), name)
        # end function __m_referVar

        def __m_generatePython(this, gen):
            def __fEG_(v, n, a):
                exp.push(n)
            # end function <anonymous> (__fEG_)

            def __fEH_(v, k, a):
                if __x_cb(k > 0):
                    writer.write((u", "), (u"\\"))
                # end if
                writer.write((u"\"") + v + (u"\""), False)
            # end function <anonymous> (__fEH_)

            def __fEI_(v, k, a):
                if __x_cb(k > 0):
                    writer.write((u", "), (u"\\"))
                # end if
                writer.write(v, False)
            # end function <anonymous> (__fEI_)

            def __fEJ_(v, n, s):
                if __x_cb(__x_not(v.closure)):
                    return
                # end if
                gen.writeln(v.toRawPython() + (u" = __x_var()"))
            # end function <anonymous> (__fEJ_)

            def __fEK_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    __u_nwv.val = True
                    return False
                # end if
            # end function <anonymous> (__fEK_)

            def __fEL_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    gen.writeln(v.toRawPython() + (u" = 0"))
                # end if
            # end function <anonymous> (__fEL_)

            __u_nwv = __x_var()
            gen.comment((u"-*- coding: utf-8 -*-"))
            gen.writeln((u"from __future__ import print_function, absolute_import, division, generators"))
            gen.blank()
            exp = ArrayList()
            __cpm[this, "exports"].forEach(__fEG_)
            writer = LineWriter()
            writer.write((u"__all__ = ("), False)
            if __x_cb(exp.length > 0):
                exp.forEach(__fEH_)
                if __x_cb(__x_eq(exp.length, 1)):
                    writer.write((u","), False)
                # end if
            # end if
            writer.write((u")"), False)
            writer.finalize(gen)
            gen.blank()
            gen.blank()
            gen.writeln((u"def __():"))
            gen.tab()
            gen.writeln((u"from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not\
, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map,\
 __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_red\
uce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop,\
 __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf\
, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN"))
            gen.writeln((u"__x_imp = __x_imf(__name__)"))
            if __x_cb(exp.length > 0):
                writer = LineWriter()
                writer.write((u"global "), False)
                exp.forEach(__fEI_)
                writer.finalize(gen)
            # end if
            gen.blank()
            gen.comment((u"function definitions:"))
            this.functionDefinitions.generatePython(gen)
            gen.blank()
            gen.comment((u"class definitions:"))
            this.classDefinitions.generatePython(gen)
            this.forEachLocalVar(__fEJ_)
            gen.blank()
            this.body.generatePython(gen)
            __u_nwv.val = False
            this.forEachLocalVar(__fEK_)
            if __x_cb(__u_nwv.val):
                gen.comment((u"Uninitialized variable:"))
                gen.writeln((u"return"))
                this.forEachLocalVar(__fEL_)
            # end if
            gen.TAB()
            gen.comment((u"program end"))
            gen.blank()
            gen.blank()
            gen.writeln((u"__()"))
        # end function __m_generatePython

        def __m_dump(this, ctx):
            ctx.attr((u"function-counter"), __cpm[this, "functionCounter"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_setBuiltins(this, s, k, a):
            __cpm[this, "builtins"].set(s, BuiltinVar(s, this))
        # end function __m_setBuiltins

        def __m_GlobalElement(this, range):
            __csu(this, range)
            bis = __cpm[this, "builtins"]
            ArrayList([(u"ArithmeticError"), (u"AssertionError"), (u"AttributeError"), (u"BaseException"), (u"BufferError"), 
(u"BytesWarning"), (u"DeprecationWarning"), (u"EOFError"), (u"Ellipsis"), (u"EnvironmentError"), (u"Exception"), 
(u"False"), (u"FloatingPointError"), (u"FutureWarning"), (u"GeneratorExit"), (u"IOError"), (u"ImportError"), 
(u"ImportWarning"), (u"IndentationError"), (u"IndexError"), (u"KeyError"), (u"KeyboardInterrupt"), (u"LookupError"), 
(u"MemoryError"), (u"NameError"), (u"None"), (u"NotImplemented"), (u"NotImplementedError"), (u"OSError"), 
(u"OverflowError"), (u"PendingDeprecationWarning"), (u"ReferenceError"), (u"RuntimeError"), (u"RuntimeWarning"), 
(u"StandardError"), (u"StopIteration"), (u"SyntaxError"), (u"SyntaxWarning"), (u"SystemError"), (u"SystemExit"), 
(u"TabError"), (u"True"), (u"TypeError"), (u"UnboundLocalError"), (u"UnicodeDecodeError"), (u"UnicodeEncodeError"), 
(u"UnicodeError"), (u"UnicodeTranslateError"), (u"UnicodeWarning"), (u"UserWarning"), (u"ValueError"), 
(u"Warning"), (u"ZeroDivisionError"), (u"__debug__"), (u"__doc__"), (u"__import__"), (u"__name__"), (u"__package__"), 
(u"abs"), (u"all"), (u"any"), (u"apply"), (u"basestring"), (u"bin"), (u"bool"), (u"buffer"), (u"bytearray"), 
(u"bytes"), (u"callable"), (u"chr"), (u"classmethod"), (u"cmp"), (u"coerce"), (u"compile"), (u"complex"), 
(u"copyright"), (u"credits"), (u"delattr"), (u"dict"), (u"dir"), (u"divmod"), (u"enumerate"), (u"eval"), 
(u"execfile"), (u"exit"), (u"file"), (u"filter"), (u"float"), (u"format"), (u"frozenset"), (u"getattr"), 
(u"globals"), (u"hasattr"), (u"hash"), (u"help"), (u"hex"), (u"id"), (u"input"), (u"int"), (u"intern"), 
(u"isinstance"), (u"issubclass"), (u"iter"), (u"len"), (u"license"), (u"list"), (u"locals"), (u"long"), 
(u"map"), (u"max"), (u"memoryview"), (u"min"), (u"next"), (u"object"), (u"oct"), (u"open"), (u"ord"), 
(u"pow"), (u"print"), (u"property"), (u"quit"), (u"range"), (u"raw_input"), (u"reduce"), (u"reload"), 
(u"repr"), (u"reversed"), (u"round"), (u"set"), (u"setattr"), (u"slice"), (u"sorted"), (u"staticmethod"), 
(u"str"), (u"sum"), (u"super"), (u"tuple"), (u"type"), (u"unichr"), (u"unicode"), (u"vars"), (u"xrange"), 
(u"zip"), (u"BlockingIOError"), (u"BrokenPipeError"), (u"ChildProcessError"), (u"ConnectionAbortedError"), 
(u"ConnectionError"), (u"ConnectionRefusedError"), (u"ConnectionResetError"), (u"FileExistsError"), (u"FileNotFoundError"), 
(u"InterruptedError"), (u"IsADirectoryError"), (u"NotADirectoryError"), (u"PermissionError"), (u"ProcessLookupError"), 
(u"RecursionError"), (u"ResourceWarning"), (u"StopAsyncIteration"), (u"TimeoutError"), (u"__build_class__"), 
(u"__loader__"), (u"__spec__"), (u"ascii"), (u"exec"), (u"NaN"), (u"Infinity")]).forEach(__cpm[this, "setBuiltins"])
            this.append(FunctionGroupElement())
            this.append(ClassGroupElement())
            this.append(BodyElement(None))
        # end function __m_GlobalElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "exports"] = StringMap()
            __cpm[this, "builtins"] = StringMap()
            __cpm[this, "functionCounter"] = 0
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("GlobalElement", {"__slots__": ("builtins", "exports", "functionCounter"), "setBuiltins": __x_smet(__m_setBuiltins)})
        __clsT = __x_dcls("GlobalElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "allocFunctionId": __m_allocFunctionId, 
"allowSuperCall": __x_prop(__g_allowSuperCall, None), "allowThis": __x_prop(__g_allowThis, None), "body": __x_prop(__g_body, None), 
"classDefinitions": __x_prop(__g_classDefinitions, None), "declarePublic": __m_declarePublic, "dump": __m_dump, 
"functionDefinitions": __x_prop(__g_functionDefinitions, None), "generatePython": __m_generatePython, 
"parent": __x_prop(__g_parent, None), "parentFunction": __x_prop(__g_parentFunction, None), "referVar": __m_referVar, 
"registerClassDefinition": __m_registerClassDefinition, "structList": __x_prop(__g_structList, None), 
"theClass": __x_prop(__g_theClass, None), "theGlobal": __x_prop(__g_theGlobal, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_GlobalElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory GlobalElement, __c_GlobalElement

    def __c_IfBlockElement(__cexT):
        def __g_typeName(this):
            return (u"ifgroup")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(IfElement, 1, False), ElementPattern(ElifElement, 0, True), ElementPattern(ElseElement, 
1, True)])
        # end function __g_structList

        def __m_simplifyExpressions(this):
            def __fEV_(e, k, self):
                e.checkStruct()
                if __x_cb(__x_eq(k, 0)):
                    return
                # end if
                if __x_cb(__u_mcei.val):
                    __u_if2.val.append(e)
                    return
                # end if
                if __x_cb(__x_iof(e, ElseElement)):
                    e.simplifyExpressions()
                    return
                # end if
                if __x_cb(__x_not(e.complex)):
                    e.simplifyExpressions()
                    return
                # end if
                __u_mcei.val = True
                __u_else2.val = ElseElement(None)
                e.replaceWith(__u_else2.val)
                __u_if2.val = IfBlockElement(None)
                __u_else2.val.append(__u_if2.val)
                elif2 = IfElement(None)
                __u_if2.val.append(elif2)
                cond2 = e.firstChild
                body2 = e.lastChild
                elif2.append(cond2)
                elif2.append(body2)
            # end function <anonymous> (__fEV_)

            __u_else2 = __x_var()
            __u_if2 = __x_var()
            __u_mcei = __x_var()
            if __x_cb(__cpm[this, "simplified"]):
                raise InternalError((u"simplify if again"))
            # end if
            __cpm[this, "simplified"] = True
            this.checkStruct()
            this.firstChild.simplifyExpressions()
            __u_mcei.val = False
            __u_if2.val = None
            __u_else2.val = None
            this.forEachChild(__fEV_)
            if __x_cb(__u_mcei.val):
                __u_else2.val.simplifyExpressions()
            # end if
            this.checkStruct()
        # end function __m_simplifyExpressions

        def __m_generatePython(this, gen):
            def __fF1_(e, k, t):
                e.generatePython(gen)
            # end function <anonymous> (__fF1_)

            this.forEachChild(__fF1_)
            gen.comment((u"end if"))
        # end function __m_generatePython

        def __m_IfBlockElement(this, range):
            __csu(this, range)
        # end function __m_IfBlockElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "simplified"] = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("IfBlockElement", {"__slots__": ("simplified",)})
        __clsT = __x_dcls("IfBlockElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_IfBlockElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory IfBlockElement, __c_IfBlockElement

    def __c_IfElement(__cexT):
        def __g_typeName(this):
            return (u"if")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, IfBlockElement))):
                raise InternalError((u"malformed structure in IfElement (not in IfBlockElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __g_theStatement(this):
            return this.parent.theStatement
        # end function __g_theStatement

        def __g_complex(this):
            return this.firstChild.complex
        # end function __g_complex

        def __m_simplifyExpressions(this):
            this.checkStruct()
            this.firstChild.checkStruct()
            cond = this.firstChild.firstChild
            body = this.lastChild
            cond.simplifyExpressions()
            body.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions

        def __m_generatePython(this, ctx):
            cond = this.firstChild.firstChild
            body = this.lastChild
            writer = LineWriter()
            writer.write((u"if "), False)
            cond.writePython(writer, False, 1)
            writer.write((u":"), False)
            writer.finalize(ctx)
            ctx.tab()
            body.generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython

        def __m_IfElement(this, range):
            __csu(this, range)
        # end function __m_IfElement

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

        __clsT = __x_dcls("IfElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"complex": __x_prop(__g_complex, None), "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_IfElement})
        return __clsT
    # end class factory IfElement, __c_IfElement

    def __c_ImportElement(__cexT):
        def __g_typeName(this):
            return (u"import")
        # end function __g_typeName

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, CallElement))):
                raise InternalError((u"malformed structure in ImportElement (not in CallElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __g_constantOnly(this):
            return False
        # end function __g_constantOnly

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"__x_imp"), contchr)
        # end function __m_writePython

        def __m_ImportElement(this, range):
            __csu(this, range)
        # end function __m_ImportElement

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

        __clsT = __x_dcls("ImportElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"constantOnly": __x_prop(__g_constantOnly, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ImportElement})
        return __clsT
    # end class factory ImportElement, __c_ImportElement

    def __c_InstanceGroupElement(__cexT):
        def __g_typeName(this):
            return (u"instanceinit")
        # end function __g_typeName

        def __g_allowThis(this):
            return this.parent.allowThis
        # end function __g_allowThis

        def __g_allowSuper(this):
            return this.parent.allowSuper
        # end function __g_allowSuper

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, ClassElement))):
                raise InternalError((u"malformed structure in InstanceGroupElement (not in ClassElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body

        def __m_registerFunctionDefinition(this, tag):
            raise InternalError((u"register function definition in class property initializer"))
        # end function __m_registerFunctionDefinition

        def __m_registerLocalVar(this, name, range = (None)):
            raise InternalError((u"register local variable in class property initializer"))
            return None
        # end function __m_registerLocalVar

        def __m_referVar(this, name, range = (None)):
            return this.theClass.referVar(name, range)
        # end function __m_referVar

        def __m_generatePython(this, gen):
            def __fG5_(p, k, s):
                if __x_cb(p.isPrivate):
                    __u_haspi.val = True
                    return False
                # end if
            # end function <anonymous> (__fG5_)

            __u_haspi = __x_var()
            gen.blank()
            gen.writeln((u"def __csu(this, *argv):"))
            gen.tab()
            this.functionDefinitions.generatePython(gen)
            gen.blank()
            __u_haspi.val = False
            __cpm[this, "instanceMembers"].forEach(__fG5_)
            if __x_cb(__u_haspi.val):
                gen.comment((u"create the private field"))
                gen.writeln((u"__cpm.create(this)"))
            # end if
            gen.comment((u"initialize properties"))
            this.body.generatePython(gen)
            gen.comment((u"super"))
            gen.writeln((u"super(__clsT, this).__init__(*argv)"))
            gen.TAB()
            gen.comment((u"end instance initializer and super constructor __csu"))
        # end function __m_generatePython

        def __m_dump(this, ctx):
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_InstanceGroupElement(this, instanceMembers):
            __csu(this, None)
            __cpm[this, "instanceMembers"] = instanceMembers
            this.append(FunctionGroupElement())
            this.append(BodyElement(None))
        # end function __m_InstanceGroupElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("InstanceGroupElement", {"__slots__": ("instanceMembers",)})
        __clsT = __x_dcls("InstanceGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuper": __x_prop(__g_allowSuper, None), "allowSuperCall": __x_prop(__g_allowSuperCall, None), 
"allowThis": __x_prop(__g_allowThis, None), "body": __x_prop(__g_body, None), "checkStruct": __m_checkStruct, 
"dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), "generatePython": __m_generatePython, 
"referVar": __m_referVar, "registerFunctionDefinition": __m_registerFunctionDefinition, "registerLocalVar": __m_registerLocalVar, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_InstanceGroupElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory InstanceGroupElement, __c_InstanceGroupElement

    def __c_InstanceInitializerElement(__cexT):
        def __g_typeName(this):
            return (u"instanceprop")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, True)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.theFunction, InstanceGroupElement))):
                raise InternalError((u"malformed structure in InstanceInitializerElement (not in InstanceGroupElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __g_isInitializer(this):
            this.checkStruct()
            return __x_ne(this.firstChild, None)
        # end function __g_isInitializer

        def __m_declareVariable(this):
            this.theClass.registerProperty(__cpm[this, "attribute"].name, __cpm[this, "isPublic"], False, __cpm[this
, "attribute"].range)
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_simplifyExpressions(this):
            if __x_cb(this.isInitializer):
                aae = AssignElement(this.range)
                this.replaceWith(aae)
                attr = AttributeElement(__cpm[this, "attribute"], __cpm[this, "attribute"].range)
                aae.append(attr)
                attr.append(ThisElement(None))
                aae.append(this.firstChild)
            # end if
            this.remove()
        # end function __m_simplifyExpressions

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_InstanceInitializerElement(this, attribute, isPublic, range):
            __csu(this, range)
            __cpm[this, "isPublic"] = isPublic
            __cpm[this, "attribute"] = attribute
        # end function __m_InstanceInitializerElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("InstanceInitializerElement", {"__slots__": ("attribute", "isPublic")})
        __clsT = __x_dcls("InstanceInitializerElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "declareVariable": __m_declareVariable, "dump": __m_dump, "isInitializer": __x_prop(__g_isInitializer, None), 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_InstanceInitializerElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory InstanceInitializerElement, __c_InstanceInitializerElement

    def __c_ItemElement(__cexT):
        def __g_typeName(this):
            return (u"item")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(__x_not(this.complex)):
                return
            # end if
            left = this.firstChild
            right = this.lastChild
            atel = left.replaceWithTemp()
            this.insertTempAssign(atel)
            right.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions

        def __m_extractLeft(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            atel = left.replaceWithTemp()
            this.insertTempAssign(atel)
            ater = right.replaceWithTemp()
            this.insertTempAssign(ater)
            this.checkStruct()
        # end function __m_extractLeft

        def __m_extractLeftAndDuplicate(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            atel = left.replaceWithTemp(False)
            this.insertTempAssign(atel)
            ater = right.replaceWithTemp(False)
            this.insertTempAssign(ater)
            this.checkStruct()
            v = ItemElement(this.range)
            v.append(atel.getLeftElement())
            v.append(ater.getLeftElement())
            v.checkStruct()
            return v
        # end function __m_extractLeftAndDuplicate

        def __m_writePython(this, writer, contchr, parentType = (0)):
            object = this.firstChild
            index = this.lastChild
            object.writePython(writer, (u"\\"), 12)
            writer.write((u"["), False)
            index.writePython(writer, (u"\\"), 0)
            writer.write((u"]"), contchr)
        # end function __m_writePython

        def __m_ItemElement(this, range):
            __csu(this, range)
        # end function __m_ItemElement

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

        __clsT = __x_dcls("ItemElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "extractLeft": __m_extractLeft, 
"extractLeftAndDuplicate": __m_extractLeftAndDuplicate, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ItemElement})
        return __clsT
    # end class factory ItemElement, __c_ItemElement

    def __c_KeyValueElement(__cexT):
        def __g_typeName(this):
            return (u"kvpair")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, ObjectLiteralElement))):
                raise InternalError((u"malformed structure in KeyValueElement (not in ObjectLiteralElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __m_simplifyExpressions(this):
            raise InternalError((u"called simplifyExpressions of KeyValueElement"))
        # end function __m_simplifyExpressions

        def __m_replaceWithTemp(this, optional = (True)):
            raise InternalError((u"called replaceWithTemp of KeyValueElement"))
        # end function __m_replaceWithTemp

        def __m_writePython(this, writer, contchr, parentType = (0)):
            key = this.firstChild
            value = this.lastChild
            key.writePython(writer, False, 11)
            writer.write((u": "), (u""))
            value.writePython(writer, False, 11)
        # end function __m_writePython

        def __m_KeyValueElement(this, range):
            __csu(this, range)
        # end function __m_KeyValueElement

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

        __clsT = __x_dcls("KeyValueElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "replaceWithTemp": __m_replaceWithTemp, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_KeyValueElement})
        return __clsT
    # end class factory KeyValueElement, __c_KeyValueElement

    def __c_MagicCallElement(__cexT):
        def __g_typeName(this):
            return (u"magiccall")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False), ElementPattern(ArgumentElement, 1, False)])
        # end function __g_structList

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            cc = CallElement(this.range)
            this.replaceWith(cc)
            o = VarElement.getGlobalVar((u"__x_at_") + __cpm[this, "name"])
            cc.append(o)
            argv = this.lastChild
            self = this.firstChild
            argv.prepend(self)
            cc.append(argv)
        # end function __m_functionalize

        def __m_dump(this, ctx):
            ctx.attr((u"name"), __cpm[this, "name"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_MagicCallElement(this, name, range):
            __csu(this, range)
            allowFns = StringMap()
            allowFns.sets([(u"apply"), (u"bind"), (u"drop"), (u"every"), (u"filter"), (u"find"), (u"findIndex"), 
(u"flatMap"), (u"forEach"), (u"has"), (u"isEmpty"), (u"join"), (u"length"), (u"map"), (u"pop"), (u"push"), 
(u"reduce"), (u"shift"), (u"slice"), (u"some"), (u"splice"), (u"take"), (u"unshift")], True)
            if __x_cb(__x_not(allowFns.has(name))):
                CAS.error(range, (u"@%s is not a valid magic method"), name)
            # end if
            __cpm[this, "name"] = name
        # end function __m_MagicCallElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("MagicCallElement", {"__slots__": ("name",)})
        __clsT = __x_dcls("MagicCallElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"dump": __m_dump, "functionalize": __m_functionalize, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_MagicCallElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory MagicCallElement, __c_MagicCallElement

    def __c_MethodElement(__cexT):
        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(MethodParameterGroupElement, 
1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __g_allowThis(this):
            tag = this.tag
            return __x_cb(this.parent.allowThis) and __x_not(tag.isStatic)
        # end function __g_allowThis

        def __g_allowSuper(this):
            tag = this.tag
            return __x_cb(this.parent.allowSuper) and __x_not(tag.isStatic)
        # end function __g_allowSuper

        def __g_allowSuperCall(this):
            tag = this.tag
            return __x_cb(this.isConstructor) and this.parent.allowSuperCall
        # end function __g_allowSuperCall

        def __g_isConstructor(this):
            tag = this.tag
            return __x_cb(__x_not(tag.isStatic)) and __x_eq(tag.name, this.theClass.tag.name)
        # end function __g_isConstructor

        def __m_declareVariable(this):
            tag = this.tag
            if __x_cb(this.isConstructor):
                if __x_cb(__x_not(tag.isPublic)):
                    CAS.error(tag.range, (u"Class constructor may not be a private method"))
                # end if
                if __x_cb(tag.isAccessor):
                    CAS.error(tag.range, (u"Class constructor may not be an accessor"))
                # end if
            else:
                this.parentFunction.registerFunctionDefinition(this.tag)
            # end if
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_meetSuper(this, range):
            if __x_cb(__x_not(this.allowSuperCall)):
                return
            # end if
            if __x_cb(__cpm[this, "smet"]):
                CAS.error(range, (u"Super constructor may only be called once"))
            # end if
            __cpm[this, "smet"] = True
        # end function __m_meetSuper

        def __m_meetReturnOrThis(this, range):
            if __x_cb(__x_not(this.allowSuperCall)):
                return
            # end if
            if __x_cb(__x_not(__cpm[this, "smet"])):
                CAS.error(range, (u"Super statement cannot occur after a this, super or return statement"))
            # end if
        # end function __m_meetReturnOrThis

        def __m_checkVariables(this):
            (super(__clsT, this)).checkVariables()
            if __x_cb(__x_cb(__x_not(__cpm[this, "smet"])) and this.allowSuperCall):
                CAS.error(this.range, (u"Must call super constructor in derived class before returning from derived constructor"))
            # end if
        # end function __m_checkVariables

        def __m_referVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if
            if __x_cb(__x_cb(__x_ne(this.tag.name, None)) and __x_eq(this.tag.name, name)):
                if __x_cb(__x_not(this.isConstructor)):
                    CAS.error(range, (u"'this' is required for referring the method itself"))
                # end if
            # end if
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar

        def __m_functionalize(this):
            if __x_cb(__x_cb(this.isConstructor) and __x_not(this.allowSuperCall)):
                expr = ExpressionStatementElement(None)
                this.body.prepend(expr)
                ce = CallElement(None)
                expr.append(ce)
                ce.append(SuperElement(None))
                ce.append(ArgumentElement(None))
            # end if
            (super(__clsT, this)).functionalize()
        # end function __m_functionalize

        def __m_dump(this, ctx):
            ctx.attr((u"public"), this.tag.isPublic)
            ctx.attr((u"static"), this.tag.isStatic)
            ctx.attr((u"type"), ((u"set") if __x_cb(this.tag.isSetter) else (u"get")) if __x_cb(this.tag.isAccessor) else (u"method"))
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_MethodElement(this, tag, range):
            __csu(this, range)
            __r0 = tag
            __r0.at = this
            this.tag = tag
            this.append(FunctionGroupElement())
            this.append(MethodParameterGroupElement(tag))
            this.append(BodyElement(None))
        # end function __m_MethodElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "smet"] = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("MethodElement", {"__slots__": ("smet",)})
        __clsT = __x_dcls("MethodElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "allowSuper": __x_prop(__g_allowSuper, None), 
"allowSuperCall": __x_prop(__g_allowSuperCall, None), "allowThis": __x_prop(__g_allowThis, None), "checkVariables": __m_checkVariables, 
"declareVariable": __m_declareVariable, "dump": __m_dump, "functionalize": __m_functionalize, "isConstructor": __x_prop(__g_isConstructor, None), 
"meetReturnOrThis": __m_meetReturnOrThis, "meetSuper": __m_meetSuper, "referVar": __m_referVar, "structList": __x_prop(__g_structList, None), 
"__init__": __m_MethodElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory MethodElement, __c_MethodElement

    def __c_MethodGroupElement(__cexT):
        def __g_typeName(this):
            return (u"methods")
        # end function __g_typeName

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall

        def __g_structList(this):
            return ArrayList([ElementPattern(MethodElement, 0, True)])
        # end function __g_structList

        def __m_MethodGroupElement(this):
            __csu(this)
        # end function __m_MethodGroupElement

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

        __clsT = __x_dcls("MethodGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuperCall": __x_prop(__g_allowSuperCall, None), "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_MethodGroupElement})
        return __clsT
    # end class factory MethodGroupElement, __c_MethodGroupElement

    def __c_ParameterGroupElement(__cexT):
        def __g_typeName(this):
            return (u"params")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 0, True), ElementPattern(ParameterAssignElement, 0, 
True), ElementPattern(RestParameterElement, 0, True)])
        # end function __g_structList

        def __m_generatePython(this, ctx):
            def __fIC_(e, k, s):
                e.generateRenameAssignment(ctx)
            # end function <anonymous> (__fIC_)

            this.checkStruct()
            this.forEachChild(__fIC_)
        # end function __m_generatePython

        def __m_toPrameterList(this, writer, contchr, parentType = (0)):
            def __fIE_(e, k, s):
                if __x_cb(__u_o.val):
                    writer.write((u", "), (u""))
                # end if
                e.writePython(writer, (u""))
                __u_o.val = True
            # end function <anonymous> (__fIE_)

            __u_o = __x_var()
            __u_o.val = False
            this.forEachChild(__fIE_)
        # end function __m_toPrameterList

        def __m_ParameterGroupElement(this):
            __csu(this, None)
        # end function __m_ParameterGroupElement

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

        __clsT = __x_dcls("ParameterGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "toPrameterList": __m_toPrameterList, 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_ParameterGroupElement})
        return __clsT
    # end class factory ParameterGroupElement, __c_ParameterGroupElement

    def __c_MethodParameterGroupElement(__cexT):
        def __m_declareVariable(this):
            def __fIK_(p, k, s):
                __r0 = __u_pcnt.val
                __u_pcnt.val = __x_inc(__r0)
            # end function <anonymous> (__fIK_)

            __u_pcnt = __x_var()
            tag = __cpm[this, "tag"]
            __u_pcnt.val = 0
            this.forEachChild(__fIK_)
            if __x_cb(__x_cb(tag.isSetter) and __x_ne(__u_pcnt.val, 1)):
                CAS.error(this.range, (u"Setter must have exactly one formal parameter"))
            # end if
            if __x_cb(__x_cb(__x_cb(tag.isAccessor) and __x_not(tag.isSetter)) and __x_ne(__u_pcnt.val, 0)):
                CAS.error(this.range, (u"Getter must not have any formal parameters"))
            # end if
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_toPrameterList(this, writer, contchr, parentType = (0)):
            def __fIM_(e, k, s):
                writer.write((u", "), (u""))
                e.writePython(writer, (u""))
            # end function <anonymous> (__fIM_)

            writer.write((u"this"), (u""))
            this.forEachChild(__fIM_)
        # end function __m_toPrameterList

        def __m_MethodParameterGroupElement(this, tag):
            __csu(this)
            __cpm[this, "tag"] = tag
        # end function __m_MethodParameterGroupElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("MethodParameterGroupElement", {"__slots__": ("tag",)})
        __clsT = __x_dcls("MethodParameterGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "declareVariable": __m_declareVariable, "toPrameterList": __m_toPrameterList, "__init__": __m_MethodParameterGroupElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory MethodParameterGroupElement, __c_MethodParameterGroupElement

    def __c_NotOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"not")
        # end function __g_typeName

        def __g_constantOnly(this):
            return this.firstChild.constantOnly
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return this.firstChild.tempVarOnly
        # end function __g_tempVarOnly

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = parentType >= 2
            dst = this.firstChild
            if __x_cb(p):
                writer.write((u"("), False)
            # end if
            writer.write((u"not "), (u"") if __x_cb(p) else contchr)
            dst.writePython(writer, (u"") if __x_cb(p) else contchr, 4)
            if __x_cb(p):
                writer.write((u")"), contchr)
            # end if
        # end function __m_writePython

        def __m_NotOperatorElement(this, range):
            __csu(this, range)
        # end function __m_NotOperatorElement

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

        __clsT = __x_dcls("NotOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NotOperatorElement})
        return __clsT
    # end class factory NotOperatorElement, __c_NotOperatorElement

    def __c_NullLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"null")
        # end function __g_typeName

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"None"), contchr)
        # end function __m_writePython

        def __m_NullLiteralElement(this, range):
            __csu(this, range)
        # end function __m_NullLiteralElement

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

        __clsT = __x_dcls("NullLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NullLiteralElement})
        return __clsT
    # end class factory NullLiteralElement, __c_NullLiteralElement

    def __c_NullishCheckElement(__cexT):
        def __g_typeName(this):
            return (u"isnullish")
        # end function __g_typeName

        def __g_constantOnly(this):
            return this.firstChild.constantOnly
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return this.firstChild.tempVarOnly
        # end function __g_tempVarOnly

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = parentType >= 3
            dst = this.firstChild
            if __x_cb(p):
                writer.write((u"("), False)
            # end if
            writer.write((u"None is "), (u"") if __x_cb(p) else contchr)
            dst.writePython(writer, (u"") if __x_cb(p) else contchr, 4)
            if __x_cb(p):
                writer.write((u")"), contchr)
            # end if
        # end function __m_writePython

        def __m_NullishCheckElement(this, range):
            __csu(this, range)
        # end function __m_NullishCheckElement

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

        __clsT = __x_dcls("NullishCheckElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NullishCheckElement})
        return __clsT
    # end class factory NullishCheckElement, __c_NullishCheckElement

    def __c_NumberLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"real")
        # end function __g_typeName

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(parentType >= 12):
                writer.write((u"("), False)
            # end if
            writer.write(__cpm[this, "source"], False)
            if __x_cb(parentType >= 12):
                writer.write((u")"), False)
            # end if
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"source"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_NumberLiteralElement(this, value, source, range):
            __csu(this, range)
            __cpm[this, "value"] = value
            __cpm[this, "source"] = source
        # end function __m_NumberLiteralElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("NumberLiteralElement", {"__slots__": ("source", "value")})
        __clsT = __x_dcls("NumberLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NumberLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory NumberLiteralElement, __c_NumberLiteralElement

    def __c_ObjectLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"object")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(KeyValueElement, 0, True)])
        # end function __g_structList

        def __m_simplifyExpressions(this):
            def __fJT_(m, k, s):
                if __x_cb(m.complex):
                    __u_lc.val = k
                # end if
            # end function <anonymous> (__fJT_)

            def __fJU_(m, k, s):
                if __x_cb(k > __u_lc.val):
                    return False
                # end if
                m.checkStruct()
                key = m.firstChild
                value = m.lastChild
                ate = key.replaceWithTemp()
                this.insertTempAssign(ate)
                tas = value.replaceWithTemp()
                this.insertTempAssign(tas)
            # end function <anonymous> (__fJU_)

            __u_lc = __x_var()
            this.checkStruct()
            __u_lc.val = -1
            this.forEachChild(__fJT_)
            this.forEachChild(__fJU_)
            this.checkStruct()
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            def __fK0_(m, k, s):
                if __x_cb(k > 0):
                    writer.write((u", "), (u""))
                # end if
                m.writePython(writer, False)
            # end function <anonymous> (__fK0_)

            writer.write((u"({"), (u""))
            this.forEachChild(__fK0_)
            writer.write((u"})"), contchr)
        # end function __m_writePython

        def __m_ObjectLiteralElement(this, range):
            __csu(this, range)
        # end function __m_ObjectLiteralElement

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

        __clsT = __x_dcls("ObjectLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_ObjectLiteralElement})
        return __clsT
    # end class factory ObjectLiteralElement, __c_ObjectLiteralElement

    def __c_ParameterAssignElement(__cexT):
        def __g_typeName(this):
            return (u"optparam")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 1, False), ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_checkVariables(this):
            p = this.firstChild
            v = this.lastChild
            p.checkVariables()
            v.checkVariables()
            if __x_cb(__x_cb(v.complex) or __x_not(v.constantOnly)):
                CAS.error(v.range, (u"Default parameter must be constant"))
            # end if
        # end function __m_checkVariables

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = this.firstChild
            v = this.lastChild
            p.writePython(writer, False)
            writer.write((u" = "), (u""))
            writer.write((u"("), False)
            v.writePython(writer, (u""))
            writer.write((u")"), False)
        # end function __m_writePython

        def __m_generateRenameAssignment(this, ctx):
            p = this.firstChild
            p.generateRenameAssignment(ctx)
        # end function __m_generateRenameAssignment

        def __m_ParameterAssignElement(this, range):
            __csu(this, range)
        # end function __m_ParameterAssignElement

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

        __clsT = __x_dcls("ParameterAssignElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkVariables": __m_checkVariables, "generateRenameAssignment": __m_generateRenameAssignment, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_ParameterAssignElement})
        return __clsT
    # end class factory ParameterAssignElement, __c_ParameterAssignElement

    def __c_ParameterElement(__cexT):
        def __g_typeName(this):
            return (u"param")
        # end function __g_typeName

        def __m_declareVariable(this):
            __cpm[this, "target"] = this.theFunction.registerLocalVar(__cpm[this, "source"], this.range)
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_checkVariables(this):
            __cpm[this, "target"].write(this.theFunction, this.range)
        # end function __m_checkVariables

        def __m_simplifyExpressions(this):
            pass
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write(__cpm[this, "target"].toOriginPython(), False)
        # end function __m_writePython

        def __m_generateRenameAssignment(this, ctx):
            if __x_cb(__x_not(__cpm[this, "target"].closure)):
                return
            # end if
            writer = LineWriter()
            writer.write(__cpm[this, "target"].toPython(), False)
            writer.write((u" = "), False)
            writer.write(__cpm[this, "target"].toOriginPython(), False)
            writer.finalize(ctx)
        # end function __m_generateRenameAssignment

        def __m_dump(this, ctx):
            ctx.attr((u"name"), __cpm[this, "source"])
            ctx.attr((u"var"), __cpm[this, "target"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_ParameterElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_ParameterElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "target"] = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("ParameterElement", {"__slots__": ("source", "target")})
        __clsT = __x_dcls("ParameterElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkVariables": __m_checkVariables, "declareVariable": __m_declareVariable, "dump": __m_dump, "generateRenameAssignment": __m_generateRenameAssignment, 
"simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ParameterElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ParameterElement, __c_ParameterElement

    def __c_RestParameterElement(__cexT):
        def __g_typeName(this):
            return (u"rest")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 1, False)])
        # end function __g_structList

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = this.firstChild
            writer.write((u"*"), False)
            p.writePython(writer, False)
        # end function __m_writePython

        def __m_generateRenameAssignment(this, ctx):
            this.checkStruct()
            p = this.firstChild
            p.generateRenameAssignment(ctx)
        # end function __m_generateRenameAssignment

        def __m_RestParameterElement(this, range):
            __csu(this, range)
        # end function __m_RestParameterElement

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

        __clsT = __x_dcls("RestParameterElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "generateRenameAssignment": __m_generateRenameAssignment, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_RestParameterElement})
        return __clsT
    # end class factory RestParameterElement, __c_RestParameterElement

    def __c_ReturnElement(__cexT):
        def __g_typeName(this):
            return (u"return")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, True)])
        # end function __g_structList

        def __m_checkVariables(this):
            fn = this.theFunction
            if __x_cb(__x_iof(fn, MethodElement)):
                fn.meetReturnOrThis(this.range)
            # end if
            (super(__clsT, this)).checkVariables()
        # end function __m_checkVariables

        def __m_generatePython(this, ctx):
            right = this.lastChild
            if __x_cb(__x_eq(right, None)):
                ctx.writeln((u"return"))
                return
            # end if
            writer = LineWriter()
            writer.write((u"return "), False)
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_ReturnElement(this, range):
            __csu(this, range)
        # end function __m_ReturnElement

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

        __clsT = __x_dcls("ReturnElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_ReturnElement})
        return __clsT
    # end class factory ReturnElement, __c_ReturnElement

    def __c_SpreadElement(__cexT):
        def __g_typeName(this):
            return (u"spread")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, SequenceElement))):
                raise InternalError((u"malformed structure in spread (not in sequence)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __m_simplifyExpressions(this):
            raise InternalError((u"called simplifyExpressions of SpreadElement"))
        # end function __m_simplifyExpressions

        def __m_replaceWithTemp(this, optional = (True)):
            raise InternalError((u"called replaceWithTemp of SpreadElement"))
        # end function __m_replaceWithTemp

        def __m_writePython(this, writer, contchr, parentType = (0)):
            value = this.lastChild
            writer.write((u"*"), (u""))
            value.writePython(writer, False, 11)
        # end function __m_writePython

        def __m_SpreadElement(this, range):
            __csu(this, range)
        # end function __m_SpreadElement

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

        __clsT = __x_dcls("SpreadElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"replaceWithTemp": __m_replaceWithTemp, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_SpreadElement})
        return __clsT
    # end class factory SpreadElement, __c_SpreadElement

    def __c_StaticGroupElement(__cexT):
        def __g_typeName(this):
            return (u"staticinit")
        # end function __g_typeName

        def __g_allowThis(this):
            return False
        # end function __g_allowThis

        def __g_allowSuper(this):
            return False
        # end function __g_allowSuper

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, ClassElement))):
                raise InternalError((u"malformed structure in StaticGroupElement (not in ClassElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body

        def __m_registerFunctionDefinition(this, tag):
            raise InternalError((u"register function definition in class property initializer"))
        # end function __m_registerFunctionDefinition

        def __m_registerLocalVar(this, name, range = (None)):
            raise InternalError((u"register local variable in class property initializer"))
            return None
        # end function __m_registerLocalVar

        def __m_referVar(this, name, range = (None)):
            if __x_cb(__x_eq(this.theClass.tag.name, name)):
                CAS.error(range, (u"cannot access the class name %s in the static property initializer"), name)
            # end if
            return this.theClass.referVar(name, range)
        # end function __m_referVar

        def __m_generatePython(this, gen):
            gen.blank()
            gen.writeln((u"def __csi(this):"))
            gen.tab()
            this.functionDefinitions.generatePython(gen)
            gen.blank()
            gen.comment((u"super"))
            gen.writeln((u"__x_objT.__init__(this)"))
            gen.comment((u"initialize properties"))
            this.body.generatePython(gen)
            gen.TAB()
            gen.comment((u"end static initializer __csi"))
        # end function __m_generatePython

        def __m_dump(this, ctx):
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_StaticGroupElement(this):
            __csu(this, None)
            this.append(FunctionGroupElement())
            this.append(BodyElement(None))
        # end function __m_StaticGroupElement

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

        __clsT = __x_dcls("StaticGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuper": __x_prop(__g_allowSuper, None), "allowSuperCall": __x_prop(__g_allowSuperCall, None), 
"allowThis": __x_prop(__g_allowThis, None), "body": __x_prop(__g_body, None), "checkStruct": __m_checkStruct, 
"dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), "generatePython": __m_generatePython, 
"referVar": __m_referVar, "registerFunctionDefinition": __m_registerFunctionDefinition, "registerLocalVar": __m_registerLocalVar, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_StaticGroupElement})
        return __clsT
    # end class factory StaticGroupElement, __c_StaticGroupElement

    def __c_StaticInitializerElement(__cexT):
        def __g_typeName(this):
            return (u"staticprop")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, True)])
        # end function __g_structList

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.theFunction, StaticGroupElement))):
                raise InternalError((u"malformed structure in StaticInitializerElement (not in StaticGroupElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __g_isInitializer(this):
            this.checkStruct()
            return __x_ne(this.firstChild, None)
        # end function __g_isInitializer

        def __m_declareVariable(this):
            this.checkStruct()
            this.theClass.registerProperty(__cpm[this, "attribute"].name, __cpm[this, "isPublic"], True, __cpm[this
, "attribute"].range)
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable

        def __m_simplifyExpressions(this):
            (super(__clsT, this)).simplifyExpressions()
            if __x_cb(__x_not(this.isInitializer)):
                this.remove()
            # end if
        # end function __m_simplifyExpressions

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            right = this.lastChild
            writer.write((u"this") if __x_cb(__cpm[this, "isPublic"]) else (u"__csp"), False)
            writer.write((u"."), False)
            writer.write(__cpm[this, "attribute"].toPython(), False)
            writer.write((u" = "), (u"\\"))
            right.writePython(writer, False)
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_StaticInitializerElement(this, attribute, isPublic, range):
            __csu(this, range)
            __cpm[this, "isPublic"] = isPublic
            __cpm[this, "attribute"] = attribute
        # end function __m_StaticInitializerElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("StaticInitializerElement", {"__slots__": ("attribute", "isPublic")})
        __clsT = __x_dcls("StaticInitializerElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "declareVariable": __m_declareVariable, "dump": __m_dump, "generatePython": __m_generatePython, 
"isInitializer": __x_prop(__g_isInitializer, None), "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_StaticInitializerElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory StaticInitializerElement, __c_StaticInitializerElement

    def __c_StringLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"string")
        # end function __g_typeName

        def __m_writePython(this, writer, contchr, parentType = (0)):
            def __fMI_(c, k, a):
                cp = StrTool.codePointAt(c)
                br = False
                if __x_cb(__x_eq(cp, 10)):
                    __u_cs.val = __u_cs.val + (u"\\n")
                    __u_cl.val = __u_cl.val + 2
                    if __x_cb(__x_cb(l > 80) and __u_cl.val >= 50):
                        br = True
                    # end if
                elif __x_cb(__x_eq(cp, 9)):
                    __u_cs.val = __u_cs.val + (u"\\t")
                    __u_cl.val = __u_cl.val + 2
                elif __x_cb(__x_eq(cp, 7)):
                    __u_cs.val = __u_cs.val + (u"\\a")
                    __u_cl.val = __u_cl.val + 2
                elif __x_cb(__x_eq(cp, 8)):
                    __u_cs.val = __u_cs.val + (u"\\b")
                    __u_cl.val = __u_cl.val + 2
                elif __x_cb(__x_eq(cp, 13)):
                    __u_cs.val = __u_cs.val + (u"\\r")
                    __u_cl.val = __u_cl.val + 2
                elif __x_cb(__x_eq(c, (u"\""))):
                    __u_cs.val = __u_cs.val + (u"\\\"")
                    __u_cl.val = __u_cl.val + 2
                elif __x_cb(__x_eq(c, (u"\\"))):
                    __u_cs.val = __u_cs.val + (u"\\\\")
                    __u_cl.val = __u_cl.val + 2
                elif __x_cb(__x_cb(cp <= 126) and cp >= 32):
                    __u_cs.val = __u_cs.val + c
                    __u_cl.val = __u_cl.val + 1
                elif __x_cb(cp < 0x10000):
                    __u_cs.val = __u_cs.val + StrTool.toCodePointString(cp)
                    __u_cl.val = __u_cl.val + 6
                else:
                    __u_cs.val = __u_cs.val + StrTool.toCodePointString(cp)
                    __u_cl.val = __u_cl.val + 10
                # end if
                if __x_cb(__x_cb(br) or __u_cl.val >= 100):
                    writer.write(__u_cs.val + (u"\\"), True)
                    __u_cl.val = 0
                    __u_cs.val = (u"")
                # end if
                br = False
            # end function <anonymous> (__fMI_)

            __u_cl = __x_var()
            __u_cs = __x_var()
            v = ArrayList(__cpm[this, "value"])
            l = v.length
            __u_cl.val = 0
            __u_cs.val = (u"")
            writer.write((u"(u\""))
            v.forEach(__fMI_)
            if __x_cb(__u_cl.val > 0):
                writer.write(__u_cs.val, False)
            # end if
            writer.write((u"\")"), contchr)
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"source"), __cpm[this, "value"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_StringLiteralElement(this, value, source, range):
            __csu(this, range)
            __cpm[this, "value"] = value
            __cpm[this, "source"] = source
        # end function __m_StringLiteralElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("StringLiteralElement", {"__slots__": ("source", "value")})
        __clsT = __x_dcls("StringLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_StringLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory StringLiteralElement, __c_StringLiteralElement

    def __c_SuperElement(__cexT):
        def __g_typeName(this):
            return (u"super")
        # end function __g_typeName

        def __g_constantOnly(this):
            return False
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly

        def __m_checkVariables(this):
            this.checkStruct()
            if __x_cb(__x_not(this.allowSuper)):
                CAS.error(this.range, (u"\"super\" keyword unexpected here"))
            # end if
            fn = this.theFunction
            if __x_cb(__x_iof(fn, MethodElement)):
                fn.meetReturnOrThis(this.range)
            # end if
        # end function __m_checkVariables

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(__x_iof(this.parent, CallElement)):
                raise InternalError((u"cannot generate the code for super()"))
            # end if
            writer.write((u"(super(__clsT, this))"), contchr)
        # end function __m_writePython

        def __m_SuperElement(this, range):
            __csu(this, range)
        # end function __m_SuperElement

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

        __clsT = __x_dcls("SuperElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"constantOnly": __x_prop(__g_constantOnly, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_SuperElement})
        return __clsT
    # end class factory SuperElement, __c_SuperElement

    def __c_TernaryOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"ternary")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 3, False)])
        # end function __g_structList

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            cond = this.firstChild
            cc = CallElement.callGlobal((u"__x_tob") if __x_cb(options.enableImplicitBooleanConversion) else (u"__x_cb"), 
cond)
            this.prepend(cc)
            this.checkStruct()
        # end function __m_functionalize

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(__x_not(this.complex)):
                return
            # end if
            cond = this.firstChild
            __v_exec = cond.nextSibling
            altn = __v_exec.nextSibling
            if __x_cb(__x_not(__x_cb(__v_exec.complex) or altn.complex)):
                cond.simplifyExpressions()
                return
            # end if
            atva = this.theFunction.allocTempVar()
            ife = IfBlockElement(None)
            this.theStatement.before(ife)
            iife = IfElement(None)
            ife.append(iife)
            acond = ConditionElement(None)
            iife.append(acond)
            acond.append(cond)
            atrue = BodyElement(None)
            iife.append(atrue)
            atvl = AssignTempElement(atva)
            atrue.append(atvl)
            atvl.append(__v_exec)
            afalse = ElseElement(None)
            ife.append(afalse)
            atvr = AssignTempElement(atva)
            afalse.append(atvr)
            atvr.append(altn)
            this.replaceWith(atvl.getLeftElement())
            ife.simplifyExpressions()
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            cond = this.firstChild
            __v_exec = cond.nextSibling
            altn = __v_exec.nextSibling
            p = parentType >= 1
            if __x_cb(p):
                writer.write((u"("), False)
            # end if
            __v_exec.writePython(writer, (u"") if __x_cb(p) else contchr, 2)
            writer.write((u" if "), (u"") if __x_cb(p) else contchr)
            cond.writePython(writer, (u"") if __x_cb(p) else contchr, 2)
            writer.write((u" else "), (u"") if __x_cb(p) else contchr)
            altn.writePython(writer, (u"") if __x_cb(p) else contchr, 2)
            if __x_cb(p):
                writer.write((u")"), contchr)
            # end if
        # end function __m_writePython

        def __m_TernaryOperatorElement(this, range):
            __csu(this, range)
        # end function __m_TernaryOperatorElement

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

        __clsT = __x_dcls("TernaryOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_TernaryOperatorElement})
        return __clsT
    # end class factory TernaryOperatorElement, __c_TernaryOperatorElement

    def __c_ThisElement(__cexT):
        def __g_typeName(this):
            return (u"this")
        # end function __g_typeName

        def __g_constantOnly(this):
            return True
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return True
        # end function __g_tempVarOnly

        def __m_checkVariables(this):
            this.checkStruct()
            if __x_cb(__x_not(this.allowThis)):
                CAS.error((u"\"this\" expression must be used inside class instance methods"), this.range)
            # end if
            fn = this.theFunction
            if __x_cb(__x_iof(fn, MethodElement)):
                fn.meetReturnOrThis(this.range)
            # end if
        # end function __m_checkVariables

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"this"), contchr)
        # end function __m_writePython

        def __m_ThisElement(this, range):
            __csu(this, range)
        # end function __m_ThisElement

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

        __clsT = __x_dcls("ThisElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"constantOnly": __x_prop(__g_constantOnly, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_ThisElement})
        return __clsT
    # end class factory ThisElement, __c_ThisElement

    def __c_ThrowElement(__cexT):
        def __g_typeName(this):
            return (u"throw")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_generatePython(this, ctx):
            right = this.lastChild
            writer = LineWriter()
            writer.write((u"raise "), False)
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython

        def __m_ThrowElement(this, range):
            __csu(this, range)
        # end function __m_ThrowElement

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

        __clsT = __x_dcls("ThrowElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ThrowElement})
        return __clsT
    # end class factory ThrowElement, __c_ThrowElement

    def __c_TryBlockElement(__cexT):
        def __g_typeName(this):
            return (u"trygroup")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(TryElement, 1, False), ElementPattern(CatchElement, 1, True), ElementPattern(FinallyElement, 
1, True)])
        # end function __g_structList

        def __m_checkStruct(this):
            (super(__clsT, this)).checkStruct()
            if __x_cb(__x_eq(this.firstChild, this.lastChild)):
                raise InternalError((u"malformed structure in TryBlockElement (missing catch or finally)"))
            # end if
        # end function __m_checkStruct

        def __m_generatePython(this, gen):
            this.checkStruct()
            (super(__clsT, this)).generatePython(gen)
            gen.comment((u"end try"))
        # end function __m_generatePython

        def __m_TryBlockElement(this, range):
            __csu(this, range)
        # end function __m_TryBlockElement

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

        __clsT = __x_dcls("TryBlockElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_TryBlockElement})
        return __clsT
    # end class factory TryBlockElement, __c_TryBlockElement

    def __c_TryElement(__cexT):
        def __g_typeName(this):
            return (u"try")
        # end function __g_typeName

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, TryBlockElement))):
                raise InternalError((u"malformed structure in TryElement (not in TryBlockElement)"))
            # end if
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct

        def __m_generatePython(this, ctx):
            ctx.writeln((u"try:"))
            ctx.tab()
            (super(__clsT, this)).generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython

        def __m_TryElement(this, range):
            __csu(this, range)
        # end function __m_TryElement

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

        __clsT = __x_dcls("TryElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "typeName": __x_prop(__g_typeName, None), "__init__": __m_TryElement})
        return __clsT
    # end class factory TryElement, __c_TryElement

    def __c_TupleElement(__cexT):
        def __g_typeName(this):
            return (u"tuple")
        # end function __g_typeName

        def __g_complex(this):
            return __x_cb(this.hasSpread) or (super(__clsT, this)).complex
        # end function __g_complex

        def __m_simplifyExpressions(this):
            if __x_cb(__x_not(this.complex)):
                return
            # end if
            tv = this.makeList()
            cc = CallElement.callGlobal((u"__x_tup"), VarElement.getTempVar(tv))
            this.replaceWith(cc)
        # end function __m_simplifyExpressions

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(this.hasSpread):
                raise InternalError((u"cannot generate python for tuple with spread syntax"))
            # end if
            writer.write((u"__x_tupof("), False)
            (super(__clsT, this)).writePython(writer, (u""))
            if __x_cb(__x_cb(__x_ne(this.firstChild, None)) and __x_eq(this.firstChild, this.lastChild)):
                writer.write((u","), False)
            # end if
            writer.write((u")"), contchr)
        # end function __m_writePython

        def __m_TupleElement(this, range):
            __csu(this, range)
        # end function __m_TupleElement

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

        __clsT = __x_dcls("TupleElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "complex": __x_prop(__g_complex, None), 
"simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_TupleElement})
        return __clsT
    # end class factory TupleElement, __c_TupleElement

    def __c_UniaryOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"uniary")
        # end function __g_typeName

        def __g_constantOnly(this):
            return this.firstChild.constantOnly
        # end function __g_constantOnly

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            op = __cpm[this, "source"]
            n = __x_eq(op, (u"typeof"))
            m = __x_eq(op, (u"!"))
            if __x_cb(__x_not(__x_cb(n) or m)):
                return
            # end if
            exp = this.firstChild
            cc = CallElement.callGlobal((u"__x_typ") if __x_cb(n) else ((u"__x_tnb") if __x_cb(options.enableImplicitBooleanConversion)
 else (u"__x_not")), exp)
            this.replaceWith(cc)
        # end function __m_functionalize

        def __m_writePython(this, writer, contchr, parentType = (0)):
            op = __cpm[this, "source"]
            dst = this.firstChild
            if __x_cb(__x_cb(__x_cb(__x_eq(op, (u"+"))) or __x_eq(op, (u"-"))) or __x_eq(op, (u"~"))):
                p = parentType > 10
                if __x_cb(p):
                    writer.write((u"("), False)
                # end if
                writer.write(op, False)
                dst.writePython(writer, (u"") if __x_cb(p) else contchr, 10)
                if __x_cb(p):
                    writer.write((u")"), contchr)
                # end if
            elif __x_cb(__x_eq(op, (u"?"))):
                p = parentType >= 3
                if __x_cb(p):
                    writer.write((u"("), False)
                # end if
                writer.write((u"None is not "), (u"") if __x_cb(p) else contchr)
                dst.writePython(writer, (u"") if __x_cb(p) else contchr, 4)
                if __x_cb(p):
                    writer.write((u")"), contchr)
                # end if
            else:
                raise InternalError((u"Cannot writePython for uniary ") + op)
            # end if
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_UniaryOperatorElement(this, source, range):
            __csu(this, range)
            if __x_cb(__x_eq(source, (u"delete"))):
                CAS.error(range, (u"delete can only be a standalone statement"))
            # end if
            __cpm[this, "source"] = source
        # end function __m_UniaryOperatorElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("UniaryOperatorElement", {"__slots__": ("source",)})
        __clsT = __x_dcls("UniaryOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "dump": __m_dump, "functionalize": __m_functionalize, 
"structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_UniaryOperatorElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory UniaryOperatorElement, __c_UniaryOperatorElement

    def __c_UpdateElement(__cexT):
        def __g_typeName(this):
            return (u"update")
        # end function __g_typeName

        def __g_complex(this):
            return True
        # end function __g_complex

        def __g_structList(this):
            return ArrayList([ElementPattern(LvalueElement, 1, False)])
        # end function __g_structList

        def __m_checkVariables(this):
            this.checkStruct()
            target = this.firstChild
            target.checkVariables()
            target.checkWrite()
        # end function __m_checkVariables

        def __m_simplifyExpressions(this):
            def append(ase, val, act, op):
                fn = (u"__x_inc") if __x_cb(op) else (u"__x_dec")
                ase.append(CallElement.callGlobal(fn, val) if __x_cb(act) else val)
            # end function append

            this.checkStruct()
            op = __cpm[this, "plus"]
            pre = __cpm[this, "prefix"]
            target = this.firstChild
            rv = target.extractLeftAndDuplicate()
            ate = AssignTempElement(this.theFunction.allocTempVar())
            this.theStatement.before(ate)
            append(ate, rv, pre, op)
            ate.checkStruct()
            asn = AssignElement(None)
            ate.after(asn)
            asn.append(target)
            append(asn, ate.getLeftElement(), __x_not(pre), op)
            asn.checkStruct()
            this.replaceWith(ate.getLeftElement())
        # end function __m_simplifyExpressions

        def __m_dump(this, ctx):
            ctx.attr((u"prefix"), __cpm[this, "prefix"])
            ctx.attr((u"operator"), (u"++") if __x_cb(__cpm[this, "plus"]) else (u"--"))
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_UpdateElement(this, source, prefix, range):
            __csu(this, range)
            if __x_cb(__x_eq(source, (u"++"))):
                __cpm[this, "plus"] = True
            elif __x_cb(__x_eq(source, (u"--"))):
                __cpm[this, "plus"] = False
            else:
                raise InternalError((u"invalid update operator"))
            # end if
            __cpm[this, "prefix"] = prefix
        # end function __m_UpdateElement

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("UpdateElement", {"__slots__": ("plus", "prefix")})
        __clsT = __x_dcls("UpdateElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"complex": __x_prop(__g_complex, None), "dump": __m_dump, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_UpdateElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory UpdateElement, __c_UpdateElement

    def __c_VarElement(__cexT):
        def __g_typeName(this):
            return (u"var")
        # end function __g_typeName

        def __g_complex(this):
            return False
        # end function __g_complex

        def __g_declarator(this):
            return __cpm[this, "_declarator"]
        # end function __g_declarator

        def __g_tempVarOnly(this):
            return __x_cb(__x_cb(__x_iof(__cpm[this, "tag"], TempVar)) or __x_iof(__cpm[this, "tag"], FunctionTag))\
 or (__x_cb(__x_iof(__cpm[this, "tag"], VarReference)) and __cpm[this, "tag"].tempVarOnly)
        # end function __g_tempVarOnly

        def __m_declareVariable(this):
            (super(__clsT, this)).declareVariable()
            if __x_cb(this.declarator):
                __r0 = __cpm[this, "tag"]
                name = __r0.name
                range = __r0.range
                __cpm[this, "tag"] = this.theFunction.registerLocalVar(name, range)
                return
            # end if
            if __x_cb(__x_iof(__cpm[this, "tag"], VarReference)):
                __r1 = __cpm[this, "tag"]
                __r1.at = this.theFunction
                return
            # end if
        # end function __m_declareVariable

        def __m_checkVariables(this):
            v = __cpm[this, "tag"]
            v.read(this.theFunction, this.range)
        # end function __m_checkVariables

        def __m_checkWrite(this):
            v = __cpm[this, "tag"]
            v.write(this.theFunction, this.range)
        # end function __m_checkWrite

        def __m_simplifyExpressions(this):
            pass
        # end function __m_simplifyExpressions

        def __m_extractLeft(this):
            pass
        # end function __m_extractLeft

        def __m_extractLeftAndDuplicate(this):
            if __x_cb(this.declarator):
                raise InternalError((u"declarator used in compound assignment"))
            # end if
            return VarElement(__cpm[this, "tag"], False)
        # end function __m_extractLeftAndDuplicate

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write(__cpm[this, "tag"].toPython(), contchr)
        # end function __m_writePython

        def __m_dump(this, ctx):
            ctx.attr((u"name"), (u"<anonymous>") if __x_cb(__x_eq(__cpm[this, "tag"], None)) else __cpm[this, "tag"]\
.name)
            ctx.attr((u"variable"), __cpm[this, "tag"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump

        def __m_VarElement(this, tag, declarator):
            __csu(this, tag.range)
            __cpm[this, "tag"] = tag
            __cpm[this, "_declarator"] = declarator
        # end function __m_VarElement

        def __n_getGlobalVar(this, name):
            tvs = VarElement(GlobalVar(name), False)
            return tvs
        # end function __n_getGlobalVar

        def __n_getTempVar(this, tv):
            tvs = VarElement(tv, False)
            return tvs
        # end function __n_getTempVar

        def __n_getFunctionExp(this, tag):
            tvs = VarElement(tag, False)
            return tvs
        # end function __n_getFunctionExp

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "tag"] = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu

        __cpiT = __x_dpif("VarElement", {"__slots__": ("_declarator", "tag")})
        __clsT = __x_dcls("VarElement", __cexT, {"__slots__": (), "getFunctionExp": __n_getFunctionExp, "getGlobalVar": __n_getGlobalVar, 
"getTempVar": __n_getTempVar, "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"checkWrite": __m_checkWrite, "complex": __x_prop(__g_complex, None), "declarator": __x_prop(__g_declarator, None), 
"declareVariable": __m_declareVariable, "dump": __m_dump, "extractLeft": __m_extractLeft, "extractLeftAndDuplicate": __m_extractLeftAndDuplicate, 
"simplifyExpressions": __m_simplifyExpressions, "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_VarElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory VarElement, __c_VarElement

    def __c_WhileElement(__cexT):
        def __g_typeName(this):
            return (u"while")
        # end function __g_typeName

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList

        def __m_simplifyExpressions(this):
            this.checkStruct()
            cond = this.firstChild
            cond.checkStruct()
            body = this.lastChild
            if __x_cb(cond.complex):
                conde = cond.firstChild
                conde.replaceWith(BooleanLiteralElement(True, None))
                ife = IfBlockElement(None)
                body.prepend(ife)
                iife = IfElement(None)
                ife.append(iife)
                acond = ConditionElement(None)
                iife.append(acond)
                acondn = NotOperatorElement(None)
                acond.append(acondn)
                acondn.append(conde)
                atrue = BodyElement(None)
                iife.append(atrue)
                abreak = BreakElement(None)
                atrue.append(abreak)
            # end if
            body.simplifyExpressions()
        # end function __m_simplifyExpressions

        def __m_generatePython(this, gen):
            cond = this.firstChild.firstChild
            body = this.lastChild
            writer = LineWriter()
            writer.write((u"while "), False)
            cond.writePython(writer, (u"\\"), 1)
            writer.write((u":"), False)
            writer.finalize(gen)
            gen.tab()
            body.generatePython(gen)
            gen.TAB()
            gen.comment((u"end while"))
        # end function __m_generatePython

        def __m_WhileElement(this, range):
            __csu(this, range)
        # end function __m_WhileElement

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

        __clsT = __x_dcls("WhileElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_WhileElement})
        return __clsT
    # end class factory WhileElement, __c_WhileElement

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StrTool = __r0.StrTool
    printf = __r0.printf
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    __r2 = __x_imp((u".utils"))
    ElementPattern = __r2.ElementPattern
    InternalError = __r2.InternalError
    XMLDumper = __r2.XMLDumper
    __r3 = __x_imp((u".symboltree"))
    SymbolTree = __r3.SymbolTree
    SymbolTreeNode = __r3.SymbolTreeNode
    __r4 = __x_imp((u".attribute"))
    Attribute = __r4.Attribute
    ClassFieldDescriptor = __r4.ClassFieldDescriptor
    isKeyword = __r4.isKeyword
    isSpecial = __r4.isSpecial
    __r5 = __x_imp((u".variable"))
    BuiltinVar = __r5.BuiltinVar
    ClassTag = __r5.ClassTag
    FunctionExpTag = __r5.FunctionExpTag
    FunctionTag = __r5.FunctionTag
    GlobalVar = __r5.GlobalVar
    LocalVar = __r5.LocalVar
    MethodTag = __r5.MethodTag
    TempVar = __r5.TempVar
    VarReference = __r5.VarReference
    encodeRadix32 = __r5.encodeRadix32
    __r6 = __x_imp((u".pygen"))
    LineNumber = __r6.LineNumber
    LineWriter = __r6.LineWriter
    PyGenerator = __r6.PyGenerator
    CAS = __x_imp((u"tools.cas"))
    __r7 = __x_imp((u"tools.options"))
    options = __r7.options
    Element = __c_Element()
    theTree = SymbolTree(Element._getNode, Element._setNode)
    ExpressionElement = __c_ExpressionElement(Element)
    SequenceElement = __c_SequenceElement(ExpressionElement)
    ArgumentElement = __c_ArgumentElement(SequenceElement)
    ArrayElement = __c_ArrayElement(SequenceElement)
    StatementElement = __c_StatementElement(Element)
    AssignElement = __c_AssignElement(StatementElement)
    AssignDestructElement = __c_AssignDestructElement(AssignElement)
    AssignTempElement = __c_AssignTempElement(StatementElement)
    LvalueElement = __c_LvalueElement(ExpressionElement)
    AttributeElement = __c_AttributeElement(LvalueElement)
    BaseFunctionElement = __c_BaseFunctionElement(Element)
    BinaryOperatorElement = __c_BinaryOperatorElement(ExpressionElement)
    BinaryLogicalElement = __c_BinaryLogicalElement(ExpressionElement)
    BlockElement = __c_BlockElement(StatementElement)
    BodyElement = __c_BodyElement(Element)
    FundamentalLiteralElement = __c_FundamentalLiteralElement(ExpressionElement)
    BooleanLiteralElement = __c_BooleanLiteralElement(FundamentalLiteralElement)
    BreakElement = __c_BreakElement(StatementElement)
    CallElement = __c_CallElement(ExpressionElement)
    CatchElement = __c_CatchElement(Element)
    ClassElement = __c_ClassElement(BaseFunctionElement)
    ClassGroupElement = __c_ClassGroupElement(BodyElement)
    ClassInitElement = __c_ClassInitElement(StatementElement)
    ComplexLiteralElement = __c_ComplexLiteralElement(FundamentalLiteralElement)
    CompoundAssignElement = __c_CompoundAssignElement(AssignElement)
    ConditionElement = __c_ConditionElement(Element)
    ContinueElement = __c_ContinueElement(StatementElement)
    DeleteElement = __c_DeleteElement(StatementElement)
    DestructGroupElement = __c_DestructGroupElement(Element)
    DestructObjectElement = __c_DestructObjectElement(DestructGroupElement)
    DestructPropertyElement = __c_DestructPropertyElement(Element)
    DoWhileElement = __c_DoWhileElement(StatementElement)
    ElifElement = __c_ElifElement(Element)
    ElseElement = __c_ElseElement(BodyElement)
    ExpressionStatementElement = __c_ExpressionStatementElement(StatementElement)
    FinallyElement = __c_FinallyElement(BodyElement)
    FunctionElement = __c_FunctionElement(BaseFunctionElement)
    FunctionDefinitionElement = __c_FunctionDefinitionElement(FunctionElement)
    FunctionExpressionElement = __c_FunctionExpressionElement(FunctionElement)
    FunctionExpressionContainerElement = __c_FunctionExpressionContainerElement(ExpressionElement)
    FunctionGroupElement = __c_FunctionGroupElement(BodyElement)
    GlobalElement = __c_GlobalElement(BaseFunctionElement)
    IfBlockElement = __c_IfBlockElement(StatementElement)
    IfElement = __c_IfElement(Element)
    ImportElement = __c_ImportElement(ExpressionElement)
    InstanceGroupElement = __c_InstanceGroupElement(BaseFunctionElement)
    InstanceInitializerElement = __c_InstanceInitializerElement(StatementElement)
    ItemElement = __c_ItemElement(LvalueElement)
    KeyValueElement = __c_KeyValueElement(ExpressionElement)
    MagicCallElement = __c_MagicCallElement(ExpressionElement)
    MethodElement = __c_MethodElement(FunctionElement)
    MethodGroupElement = __c_MethodGroupElement(FunctionGroupElement)
    ParameterGroupElement = __c_ParameterGroupElement(Element)
    MethodParameterGroupElement = __c_MethodParameterGroupElement(ParameterGroupElement)
    NotOperatorElement = __c_NotOperatorElement(ExpressionElement)
    NullLiteralElement = __c_NullLiteralElement(FundamentalLiteralElement)
    NullishCheckElement = __c_NullishCheckElement(ExpressionElement)
    NumberLiteralElement = __c_NumberLiteralElement(FundamentalLiteralElement)
    ObjectLiteralElement = __c_ObjectLiteralElement(ExpressionElement)
    ParameterAssignElement = __c_ParameterAssignElement(Element)
    ParameterElement = __c_ParameterElement(Element)
    RestParameterElement = __c_RestParameterElement(Element)
    ReturnElement = __c_ReturnElement(StatementElement)
    SpreadElement = __c_SpreadElement(ExpressionElement)
    StaticGroupElement = __c_StaticGroupElement(BaseFunctionElement)
    StaticInitializerElement = __c_StaticInitializerElement(StatementElement)
    StringLiteralElement = __c_StringLiteralElement(FundamentalLiteralElement)
    SuperElement = __c_SuperElement(ExpressionElement)
    TernaryOperatorElement = __c_TernaryOperatorElement(ExpressionElement)
    ThisElement = __c_ThisElement(ExpressionElement)
    ThrowElement = __c_ThrowElement(StatementElement)
    TryBlockElement = __c_TryBlockElement(BlockElement)
    TryElement = __c_TryElement(BodyElement)
    TupleElement = __c_TupleElement(SequenceElement)
    UniaryOperatorElement = __c_UniaryOperatorElement(ExpressionElement)
    UpdateElement = __c_UpdateElement(ExpressionElement)
    VarElement = __c_VarElement(LvalueElement)
    WhileElement = __c_WhileElement(StatementElement)
# program end


__()
