# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("ArgumentElement", "ArrayElement", "AssignDestructElement", "AssignElement", "AssignTempElement", \
"AttributeElement", "BaseFunctionElement", "BinaryLogicalElement", "BinaryOperatorElement", "BlockElement", \
"BodyElement", "BooleanLiteralElement", "BreakElement", "CallElement", "CatchElement", "ClassElement", \
"ClassGroupElement", "ClassInitElement", "ComplexLiteralElement", "CompoundAssignElement", "ConditionElement", \
"ContinueElement", "DeleteElement", "DestructGroupElement", "DestructObjectElement", "DestructPropertyElement", \
"DoWhileElement", "Element", "ElifElement", "ElseElement", "ExpressionElement", "ExpressionStatementElement", \
"FinallyElement", "FunctionDefinitionElement", "FunctionElement", "FunctionExpressionElement", "FunctionGroupElement", \
"FundamentalLiteralElement", "GlobalElement", "IfBlockElement", "IfElement", "ImportElement", "InstanceGroupElement", \
"InstanceInitializerElement", "ItemElement", "KeyValueElement", "LvalueElement", "MagicCallElement", \
"MethodElement", "MethodGroupElement", "MethodParameterGroupElement", "NotOperatorElement", "NullLiteralElement", \
"NullishCheckElement", "NumberLiteralElement", "ObjectLiteralElement", "ParameterAssignElement", "ParameterElement", \
"ParameterGroupElement", "RestParameterElement", "ReturnElement", "SequenceElement", "SpreadElement", \
"StatementElement", "StaticGroupElement", "StaticInitializerElement", "StringLiteralElement", "SuperElement", \
"TernaryOperatorElement", "ThisElement", "ThrowElement", "TryBlockElement", "TryElement", "TupleElement", \
"UniaryOperatorElement", "UpdateElement", "VarDeclaratorElement", "VarElement", "WhileElement")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global ArgumentElement, ArrayElement, AssignDestructElement, AssignElement, AssignTempElement, AttributeElement, \
BaseFunctionElement, BinaryLogicalElement, BinaryOperatorElement, BlockElement, BodyElement, BooleanLiteralElement, \
BreakElement, CallElement, CatchElement, ClassElement, ClassGroupElement, ClassInitElement, ComplexLiteralElement, \
CompoundAssignElement, ConditionElement, ContinueElement, DeleteElement, DestructGroupElement, DestructObjectElement, \
DestructPropertyElement, DoWhileElement, Element, ElifElement, ElseElement, ExpressionElement, ExpressionStatementElement, \
FinallyElement, FunctionDefinitionElement, FunctionElement, FunctionExpressionElement, FunctionGroupElement, \
FundamentalLiteralElement, GlobalElement, IfBlockElement, IfElement, ImportElement, InstanceGroupElement, \
InstanceInitializerElement, ItemElement, KeyValueElement, LvalueElement, MagicCallElement, MethodElement, \
MethodGroupElement, MethodParameterGroupElement, NotOperatorElement, NullLiteralElement, NullishCheckElement, \
NumberLiteralElement, ObjectLiteralElement, ParameterAssignElement, ParameterElement, ParameterGroupElement, \
RestParameterElement, ReturnElement, SequenceElement, SpreadElement, StatementElement, StaticGroupElement, \
StaticInitializerElement, StringLiteralElement, SuperElement, TernaryOperatorElement, ThisElement, ThrowElement, \
TryBlockElement, TryElement, TupleElement, UniaryOperatorElement, UpdateElement, VarDeclaratorElement, \
VarElement, WhileElement

    # function definitions:

    # class definitions:

    def __c_Element():
        def __g_typeName(this):
            return (u"abstract")
        # end function __g_typeName (line 44)

        def __g_complex(this):
            return True
        # end function __g_complex (line 48)

        def __g_constantOnly(this):
            return False
        # end function __g_constantOnly (line 52)

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly (line 56)

        def __g_parent(this):
            return __csg[Element, "st"].parent(this)
        # end function __g_parent (line 60)

        def __g_previousSibling(this):
            return __csg[Element, "st"].previousSibling(this)
        # end function __g_previousSibling (line 64)

        def __g_nextSibling(this):
            return __csg[Element, "st"].nextSibling(this)
        # end function __g_nextSibling (line 68)

        def __g_theStatement(this):
            return None
        # end function __g_theStatement (line 72)

        def __g_theFunction(this):
            return this.parent.theFunction
        # end function __g_theFunction (line 76)

        def __g_theClass(this):
            return this.parent.theClass
        # end function __g_theClass (line 80)

        def __g_theGlobal(this):
            return this.parent.theGlobal
        # end function __g_theGlobal (line 84)

        def __g_allowThis(this):
            return this.parent.allowThis
        # end function __g_allowThis (line 88)

        def __g_allowSuper(this):
            return this.parent.allowSuper
        # end function __g_allowSuper (line 92)

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall (line 96)

        def __m_remove(this):
            __csg[Element, "st"].remove(this)
        # end function __m_remove (line 100)

        def __g_firstChild(this):
            return __csg[Element, "st"].firstChild(this)
        # end function __g_firstChild (line 104)

        def __g_lastChild(this):
            return __csg[Element, "st"].lastChild(this)
        # end function __g_lastChild (line 108)

        def __m_before(this, e):
            e.remove()
            __csg[Element, "st"].insertBefore(this, e)
        # end function __m_before (line 112)

        def __m_after(this, e):
            e.remove()
            __csg[Element, "st"].insertAfter(this, e)
        # end function __m_after (line 117)

        def __m_append(this, e):
            e.remove()
            __csg[Element, "st"].appendChild(this, e)
        # end function __m_append (line 122)

        def __m_prepend(this, e):
            e.remove()
            __csg[Element, "st"].prependChild(this, e)
        # end function __m_prepend (line 127)

        def __m_replaceWith(this, e):
            if __x_cb(__x_eq(this, e)):
                return
            # end if (line 133)
            this.before(e)
            this.remove()
        # end function __m_replaceWith (line 132)

        def __m_forEachChild(this, callback):
            def __fP_(e, k, a):
                return callback(e, k, self)
            # end function <anonymous> (__fP_) (line 141)

            v = ArrayList()
            it = __csg[Element, "st"].childrenIterator(this, False)
            k = 0
            while __x_cb(True):
                nx = it.next()
                if __x_cb(nx.done):
                    break
                # end if (line 150)
                v.push(nx.value)
                __r0 = k
                k = __x_inc(__r0)
            # end while (line 148)
            self = this
            v.forEach(__fP_)
        # end function __m_forEachChild (line 140)

        def __g_structList(this):
            return ArrayList()
        # end function __g_structList (line 161)

        def __m_checkStruct(this):
            def __fS_(e, n, s):
                while __x_cb(True):
                    if __x_cb(__x_eq(__u_k.val, sl.length)):
                        raise InternalError((u"malformed structure in ") + s.typeName + (u", expected the end of element, but ") + e\
.typeName + (u" is met;"))
                    # end if (line 168)
                    p = sl.get(__u_k.val)
                    if __x_cb(p.meet(e, s.typeName)):
                        return
                    # end if (line 173)
                    __r0 = __u_k.val
                    __u_k.val = __x_inc(__r0)
                # end while (line 167)
            # end function <anonymous> (__fS_) (line 166)

            __u_k = __x_var()
            sl = this.structList
            __u_k.val = 0
            this.forEachChild(__fS_)
            if __x_cb(__x_eq(sl.length, 0)):
                return
            # end if (line 185)
            while __x_cb(__u_k.val < sl.length):
                sl.get(__u_k.val).meetEOF(this.typeName)
                __r0 = __u_k.val
                __u_k.val = __x_inc(__r0)
            # end while (line 188)
        # end function __m_checkStruct (line 165)

        def __m_checkAllStructure(this):
            def __fU_(e, k, s):
                e.checkAllStructure()
            # end function <anonymous> (__fU_) (line 196)

            this.checkStruct()
            this.forEachChild(__fU_)
        # end function __m_checkAllStructure (line 195)

        def __m_declareVariable(this):
            def __f10_(e, k, t):
                e.declareVariable()
            # end function <anonymous> (__f10_) (line 205)

            this.forEachChild(__f10_)
        # end function __m_declareVariable (line 204)

        def __m_checkVariables(this):
            def __f12_(e, k, t):
                e.checkVariables()
            # end function <anonymous> (__f12_) (line 213)

            this.forEachChild(__f12_)
        # end function __m_checkVariables (line 212)

        def __m_functionalize(this):
            def __f14_(e, k, t):
                e.functionalize()
            # end function <anonymous> (__f14_) (line 221)

            this.forEachChild(__f14_)
        # end function __m_functionalize (line 220)

        def __m_simplifyExpressions(this):
            def __f16_(e, k, t):
                e.simplifyExpressions()
            # end function <anonymous> (__f16_) (line 229)

            this.forEachChild(__f16_)
        # end function __m_simplifyExpressions (line 228)

        def __m_dump(this, ctx):
            ctx.tag(this.typeName)
            ctx.range(this.range)
            ctx.finalize(this)
        # end function __m_dump (line 236)

        def __m_generatePython(this, ctx):
            raise InternalError((u"function generatePython in ") + this.typeName + (u" element is abstract"))
        # end function __m_generatePython (line 242)

        def __m_Element(this, range):
            __csu(this)
            __csg[Element, "st"].initialize(this)
            this.range = range
        # end function __m_Element (line 246)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
            __csp.st = SymbolTree()
        # end static initializer __csi (line 252)

        def __csu(this, *argv):
            # initialize properties
            this._symbolTreeNode = None
            this.range = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 259)

        __cpsT = __x_dpsf("Element", {"__slots__": ("st",)})
        __csp = __cpsT()
        __clsT = __x_dcls("Element", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("_symbolTreeNode", 
"range"), "after": __m_after, "allowSuper": __x_prop(__g_allowSuper, None), "allowSuperCall": __x_prop(__g_allowSuperCall, None), 
"allowThis": __x_prop(__g_allowThis, None), "append": __m_append, "before": __m_before, "checkAllStructure": __m_checkAllStructure, 
"checkStruct": __m_checkStruct, "checkVariables": __m_checkVariables, "complex": __x_prop(__g_complex, None), 
"constantOnly": __x_prop(__g_constantOnly, None), "declareVariable": __m_declareVariable, "dump": __m_dump, 
"firstChild": __x_prop(__g_firstChild, None), "forEachChild": __m_forEachChild, "functionalize": __m_functionalize, 
"generatePython": __m_generatePython, "lastChild": __x_prop(__g_lastChild, None), "nextSibling": __x_prop(__g_nextSibling, None), 
"parent": __x_prop(__g_parent, None), "prepend": __m_prepend, "previousSibling": __x_prop(__g_previousSibling, None), 
"remove": __m_remove, "replaceWith": __m_replaceWith, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "theClass": __x_prop(__g_theClass, None), 
"theFunction": __x_prop(__g_theFunction, None), "theGlobal": __x_prop(__g_theGlobal, None), "theStatement": __x_prop(__g_theStatement, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_Element})
        __csg = __x_csgT(__clsT, __csp)
        return __clsT
    # end class factory Element, __c_Element (line 43)

    def __c_ExpressionElement(__cexT):
        def __g_typeName(this):
            return (u"exprabstr")
        # end function __g_typeName (line 286)

        def __g_complex(this):
            def __f1F_(e, i, s):
                if __x_cb(e.complex):
                    __u_c.val = True
                    return False
                # end if (line 292)
            # end function <anonymous> (__f1F_) (line 291)

            __u_c = __x_var()
            __u_c.val = False
            this.forEachChild(__f1F_)
            return __u_c.val
        # end function __g_complex (line 290)

        def __g_theStatement(this):
            return this.parent.theStatement
        # end function __g_theStatement (line 304)

        def __m_replaceWithTemp(this, optional = (True)):
            if __x_cb(__x_cb(optional) and this.tempVarOnly):
                return None
            # end if (line 309)
            ate = AssignTempElement(this.theFunction.allocTempVar())
            this.replaceWith(ate.getLeftElement())
            ate.append(this)
            return ate
        # end function __m_replaceWithTemp (line 308)

        def __m_insertTempAssign(this, e):
            if __x_cb(__x_eq(e, None)):
                return
            # end if (line 319)
            this.theStatement.before(e)
            e.simplifyExpressions()
        # end function __m_insertTempAssign (line 318)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            raise InternalError((u"function generatePython in ") + this.typeName + (u" element is abstract"))
        # end function __m_writePython (line 326)

        def __m_ExpressionElement(this, range):
            __csu(this, range)
        # end function __m_ExpressionElement (line 330)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 334)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 340)

        __clsT = __x_dcls("ExpressionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"complex": __x_prop(__g_complex, None), "insertTempAssign": __m_insertTempAssign, "replaceWithTemp": __m_replaceWithTemp, 
"theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ExpressionElement})
        return __clsT
    # end class factory ExpressionElement, __c_ExpressionElement (line 285)

    def __c_SequenceElement(__cexT):
        def __g_typeName(this):
            return (u"sequence-abstract")
        # end function __g_typeName (line 354)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 0, True)])
        # end function __g_structList (line 358)

        def __g_hasSpread(this):
            def __f1R_(e, k, s):
                if __x_cb(__x_iof(e, SpreadElement)):
                    __u_f.val = True
                    return False
                # end if (line 364)
            # end function <anonymous> (__f1R_) (line 363)

            __u_f = __x_var()
            __u_f.val = False
            this.forEachChild(__f1R_)
            return __u_f.val
        # end function __g_hasSpread (line 362)

        def __m_simplifyExpressions(this):
            raise InternalError((u"simplifyExpressions of ") + this.typeName + (u" is abstract"))
        # end function __m_simplifyExpressions (line 376)

        def __m_makeList(this):
            def __f1U_(m, k, s):
                if __x_cb(__x_cb(m.complex) or __x_iof(m, SpreadElement)):
                    __u_lc.val = k
                    return False
                # end if (line 382)
            # end function <anonymous> (__f1U_) (line 381)

            def __f1V_(e, k, s):
                if __x_cb(k < __u_lc.val):
                    init.append(e)
                    return
                # end if (line 389)
                if __x_cb(__x_iof(e, SpreadElement)):
                    fn = (u"extend")
                    ee = e.firstChild
                else:
                    fn = (u"append")
                    ee = e
                # end if (line 393)
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
            # end function <anonymous> (__f1V_) (line 388)

            __u_lc = __x_var()
            this.checkStruct()
            __u_lc.val = -1
            this.forEachChild(__f1U_)
            if __x_cb(__u_lc.val < 0):
                raise InternalError((u"redundant calling to makeList"))
            # end if (line 419)
            tv = this.theFunction.allocTempVar()
            ate = AssignTempElement(tv)
            this.insertTempAssign(ate)
            init = ArrayElement(None)
            ate.append(init)
            this.forEachChild(__f1V_)
            if __x_cb(__x_ne(this.firstChild, None)):
                raise InternalError((u"unfinished SequenceElement::makeList"))
            # end if (line 428)
            return tv
        # end function __m_makeList (line 380)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            def __f21_(m, k, s):
                if __x_cb(k > 0):
                    writer.write((u", "), (u""))
                # end if (line 436)
                m.writePython(writer, False)
            # end function <anonymous> (__f21_) (line 435)

            this.forEachChild(__f21_)
        # end function __m_writePython (line 434)

        def __m_SequenceElement(this, range):
            __csu(this, range)
        # end function __m_SequenceElement (line 445)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 449)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 455)

        __clsT = __x_dcls("SequenceElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"hasSpread": __x_prop(__g_hasSpread, None), "makeList": __m_makeList, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_SequenceElement})
        return __clsT
    # end class factory SequenceElement, __c_SequenceElement (line 353)

    def __c_ArgumentElement(__cexT):
        def __g_typeName(this):
            return (u"argument")
        # end function __g_typeName (line 469)

        def __g_complex(this):
            l = this.firstChild
            r = this.lastChild
            if __x_cb(__x_eq(l, None)):
                return False
            # end if (line 476)
            if __x_cb(__x_eq(l, r)):
                return this.firstChild.complex
            # end if (line 479)
            return __x_cb(this.hasSpread) or (super(__clsT, this)).complex
        # end function __g_complex (line 473)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_cb(__x_iof(this.parent, CallElement)) or __x_iof(this.parent, MagicCallElement))):
                raise InternalError((u"malformed structure in argument (not in call)"))
            # end if (line 486)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 485)

        def __m_simplifyExpressions(this):
            if __x_cb(__x_not(this.complex)):
                return
            # end if (line 493)
            l = this.firstChild
            r = this.lastChild
            if __x_cb(__x_eq(l, r)):
                if __x_cb(__x_iof(l, SpreadElement)):
                    l.firstChild.simplifyExpressions()
                else:
                    l.simplifyExpressions()
                # end if (line 499)
                return
            # end if (line 498)
            tv = this.makeList()
            sr = SpreadElement(None)
            this.append(sr)
            sr.append(VarElement.getTempVar(tv))
        # end function __m_simplifyExpressions (line 492)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"("), False)
            (super(__clsT, this)).writePython(writer, (u""))
            writer.write((u")"), contchr)
        # end function __m_writePython (line 512)

        def __m_ArgumentElement(this, range):
            __csu(this, range)
        # end function __m_ArgumentElement (line 518)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 522)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 528)

        __clsT = __x_dcls("ArgumentElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "complex": __x_prop(__g_complex, None), "simplifyExpressions": __m_simplifyExpressions, 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_ArgumentElement})
        return __clsT
    # end class factory ArgumentElement, __c_ArgumentElement (line 468)

    def __c_ArrayElement(__cexT):
        def __g_typeName(this):
            return (u"array")
        # end function __g_typeName (line 541)

        def __g_complex(this):
            return __x_cb(this.hasSpread) or (super(__clsT, this)).complex
        # end function __g_complex (line 545)

        def __m_simplifyExpressions(this):
            if __x_cb(__x_not(this.complex)):
                return
            # end if (line 550)
            tv = this.makeList()
            this.replaceWith(VarElement.getTempVar(tv))
        # end function __m_simplifyExpressions (line 549)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(this.hasSpread):
                raise InternalError((u"cannot generate python for array with spread syntax"))
            # end if (line 558)
            writer.write((u"["), False)
            (super(__clsT, this)).writePython(writer, (u""))
            writer.write((u"]"), contchr)
        # end function __m_writePython (line 557)

        def __m_ArrayElement(this, range):
            __csu(this, range)
        # end function __m_ArrayElement (line 566)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 570)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 576)

        __clsT = __x_dcls("ArrayElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "complex": __x_prop(__g_complex, None), 
"simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ArrayElement})
        return __clsT
    # end class factory ArrayElement, __c_ArrayElement (line 540)

    def __c_StatementElement(__cexT):
        def __g_typeName(this):
            return (u"statement-abstract")
        # end function __g_typeName (line 589)

        def __g_theStatement(this):
            return this
        # end function __g_theStatement (line 593)

        def __m_StatementElement(this, range):
            __csu(this, range)
        # end function __m_StatementElement (line 597)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 601)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 607)

        __clsT = __x_dcls("StatementElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_StatementElement})
        return __clsT
    # end class factory StatementElement, __c_StatementElement (line 588)

    def __c_AssignElement(__cexT):
        def __g_typeName(this):
            return (u"assign")
        # end function __g_typeName (line 619)

        def __g_structList(this):
            return ArrayList([ElementPattern(LvalueElement, 1, False), ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 623)

        def __m_checkVariables(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            left.checkWrite()
            right.checkVariables()
        # end function __m_checkVariables (line 627)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            left.extractLeft()
            right.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions (line 635)

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            left = this.firstChild
            right = this.lastChild
            left.writePython(writer, False)
            writer.write((u" = "), (u"\\"))
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython (line 644)

        def __m_AssignElement(this, range):
            __csu(this, range)
        # end function __m_AssignElement (line 654)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 658)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 664)

        __clsT = __x_dcls("AssignElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_AssignElement})
        return __clsT
    # end class factory AssignElement, __c_AssignElement (line 618)

    def __c_AssignDestructElement(__cexT):
        def __g_structList(this):
            return ArrayList([ElementPattern(DestructGroupElement, 1, False), ElementPattern(ExpressionElement, 1, 
False)])
        # end function __g_structList (line 677)

        def __m_checkVariables(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            left.checkVariables()
            right.checkVariables()
        # end function __m_checkVariables (line 682)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            left = this.firstChild
            left.checkStruct()
            right = this.lastChild
            left.append(right)
            this.before(left)
            left.simplifyExpressions()
            this.remove()
        # end function __m_simplifyExpressions (line 690)

        def __m_generatePython(this, ctx):
            raise InternalError((u"cannot generate python for AssignDestructElement"))
        # end function __m_generatePython (line 701)

        def __m_AssignDestructElement(this, range):
            __csu(this, range)
        # end function __m_AssignDestructElement (line 705)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 709)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 715)

        __clsT = __x_dcls("AssignDestructElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkVariables": __m_checkVariables, "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "__init__": __m_AssignDestructElement})
        return __clsT
    # end class factory AssignDestructElement, __c_AssignDestructElement (line 676)

    def __c_AssignTempElement(__cexT):
        def __g_typeName(this):
            return (u"assigntemp")
        # end function __g_typeName (line 728)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 732)

        def __m_checkStruct(this):
            if __x_cb(__x_ne(__cpm[this, "aim"].at, this.theFunction)):
                raise InternalError((u"Mismatched scope for AssignTempElement"))
            # end if (line 737)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 736)

        def __m_checkVariables(this):
            raise InternalError((u"Illegal stage 1 for AssignTempElement"))
        # end function __m_checkVariables (line 743)

        def __m_getLeftElement(this):
            return VarElement.getTempVar(__cpm[this, "aim"])
        # end function __m_getLeftElement (line 747)

        def __m_dump(this, ctx):
            ctx.attr((u"target"), __cpm[this, "aim"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 751)

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            left = __cpm[this, "aim"]
            right = this.firstChild
            writer.write(__cpm[this, "aim"].toPython(), False)
            writer.write((u" = "), (u"\\"))
            right.writePython(writer, False)
            writer.finalize(ctx)
        # end function __m_generatePython (line 756)

        def __m_AssignTempElement(this, aim):
            __csu(this, None)
            __cpm[this, "aim"] = aim
        # end function __m_AssignTempElement (line 766)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 771)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "aim"] = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 777)

        __cpiT = __x_dpif("AssignTempElement", {"__slots__": ("aim",)})
        __clsT = __x_dcls("AssignTempElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "checkVariables": __m_checkVariables, "dump": __m_dump, "generatePython": __m_generatePython, 
"getLeftElement": __m_getLeftElement, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_AssignTempElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory AssignTempElement, __c_AssignTempElement (line 727)

    def __c_LvalueElement(__cexT):
        def __g_typeName(this):
            return (u"lvalue-abstract")
        # end function __g_typeName (line 796)

        def __m_checkWrite(this):
            this.checkVariables()
        # end function __m_checkWrite (line 800)

        def __g_declarator(this):
            return False
        # end function __g_declarator (line 804)

        def __m_extractLeft(this):
            raise InternalError((u"extractLeft is abstract in ") + this.typeName)
        # end function __m_extractLeft (line 808)

        def __m_extractLeftAndDuplicate(this):
            raise InternalError((u"extractLeftAndDuplicate is abstract in ") + this.typeName)
        # end function __m_extractLeftAndDuplicate (line 812)

        def __m_dump(this, ctx):
            ctx.attr((u"declare"), this.declarator)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 816)

        def __m_LvalueElement(this, range):
            __csu(this, range)
        # end function __m_LvalueElement (line 821)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 825)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 831)

        __clsT = __x_dcls("LvalueElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkWrite": __m_checkWrite, 
"declarator": __x_prop(__g_declarator, None), "dump": __m_dump, "extractLeft": __m_extractLeft, "extractLeftAndDuplicate": __m_extractLeftAndDuplicate, 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_LvalueElement})
        return __clsT
    # end class factory LvalueElement, __c_LvalueElement (line 795)

    def __c_AttributeElement(__cexT):
        def __g_typeName(this):
            return (u"attribute")
        # end function __g_typeName (line 844)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 848)

        def __m_extractLeft(this):
            this.checkStruct()
            left = this.firstChild
            ate = left.replaceWithTemp()
            this.insertTempAssign(ate)
            this.checkStruct()
        # end function __m_extractLeft (line 852)

        def __m_extractLeftAndDuplicate(this):
            this.checkStruct()
            left = this.firstChild
            ate = left.replaceWithTemp(False)
            this.insertTempAssign(ate)
            v = AttributeElement(__cpm[this, "attribute"], this.range)
            v.append(ate.getLeftElement())
            this.checkStruct()
            return v
        # end function __m_extractLeftAndDuplicate (line 860)

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 871)

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
            # end if (line 881)
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
            # end if (line 888)
        # end function __m_writePython (line 876)

        def __m_AttributeElement(this, attribute, range):
            __csu(this, range)
            __cpm[this, "attribute"] = attribute
        # end function __m_AttributeElement (line 902)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 907)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 913)

        __cpiT = __x_dpif("AttributeElement", {"__slots__": ("attribute",)})
        __clsT = __x_dcls("AttributeElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"dump": __m_dump, "extractLeft": __m_extractLeft, "extractLeftAndDuplicate": __m_extractLeftAndDuplicate, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_AttributeElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory AttributeElement, __c_AttributeElement (line 843)

    def __c_BaseFunctionElement(__cexT):
        def __g_typeName(this):
            return (u"basefunction")
        # end function __g_typeName (line 931)

        def __g_functionToken(this):
            return Identifier.encodeRadix32(__cpm[this, "functionId"])
        # end function __g_functionToken (line 935)

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall (line 939)

        def __g_theFunction(this):
            return this
        # end function __g_theFunction (line 943)

        def __g_parentFunction(this):
            return this.parent.theFunction
        # end function __g_parentFunction (line 947)

        def __g_functionDefinitions(this):
            raise InternalError(this.typeName + (u" have no inner function definition area"))
        # end function __g_functionDefinitions (line 951)

        def __g_body(this):
            raise InternalError(this.typeName + (u" have no function body"))
        # end function __g_body (line 955)

        def __m_getLocal(this, name):
            return __cpm[this, "vars"].get(name, None)
        # end function __m_getLocal (line 959)

        def __m_setLocal(this, name, v):
            if __x_cb(__x_eq(v, None)):
                raise InternalError((u"set a null variable"))
            # end if (line 964)
            __cpm[this, "vars"].set(name, v)
        # end function __m_setLocal (line 963)

        def __m_registerFunctionDefinition(this, tag, range = (None)):
            name = tag.name
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                raise ConflictError((u"Duplicate function definition: %s"), range, v.range, name)
            # end if (line 973)
            this.setLocal(name, tag)
        # end function __m_registerFunctionDefinition (line 970)

        def __m_registerLocalVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                raise ConflictError((u"Identifier '%s' has already been declared"), range, v.range, name)
            # end if (line 981)
            v = LocalVar(name, this, range)
            this.setLocal(name, v)
            return v
        # end function __m_registerLocalVar (line 979)

        def __m_forEachLocalVar(this, callback):
            def __f4P_(e, k, a):
                return callback(e, k, self)
            # end function <anonymous> (__f4P_) (line 990)

            self = this
            __cpm[this, "vars"].forEach(__f4P_)
        # end function __m_forEachLocalVar (line 989)

        def __m_referVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if (line 1000)
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar (line 998)

        def __m_allocTempVar(this):
            __r0 = this
            __r1 = __cpm[__r0, "tempCounter"]
            __cpm[__r0, "tempCounter"] = __x_inc(__r1)
            tid = __r1
            return TempVar(tid, this)
        # end function __m_allocTempVar (line 1006)

        def __m_declareVariable(this):
            __cpm[this, "functionId"] = this.theGlobal.allocFunctionId()
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable (line 1014)

        def __m_dump(this, ctx):
            ctx.attr((u"id"), __cpm[this, "functionId"])
            ctx.attr((u"tempcnt"), __cpm[this, "tempCounter"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 1019)

        def __m_BaseFunctionElement(this, range):
            __csu(this, range)
        # end function __m_BaseFunctionElement (line 1025)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1029)

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
        # end instance initializer and super constructor __csu (line 1035)

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
    # end class factory BaseFunctionElement, __c_BaseFunctionElement (line 930)

    def __c_BinaryOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"binary")
        # end function __g_typeName (line 1061)

        def __g_constantOnly(this):
            return __x_cb(this.firstChild.constantOnly) and this.lastChild.constantOnly
        # end function __g_constantOnly (line 1065)

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly (line 1069)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList (line 1073)

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
            # end if (line 1085)
            cc = CallElement(None)
            this.replaceWith(cc)
            callee = VarElement.getGlobalVar(fn)
            cc.append(callee)
            argv = ArgumentElement(None)
            cc.append(argv)
            argv.append(a)
            argv.append(b)
            cc.checkStruct()
        # end function __m_functionalize (line 1077)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(__x_not(this.complex)):
                return
            # end if (line 1101)
            left = this.firstChild
            right = this.lastChild
            op = __cpm[this, "source"]
            if __x_cb(right.complex):
                ale = left.replaceWithTemp()
                this.insertTempAssign(ale)
                right.simplifyExpressions()
            else:
                left.simplifyExpressions()
            # end if (line 1107)
        # end function __m_simplifyExpressions (line 1099)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            oppMap = StringMap([[(u"+"), 8], [(u"-"), 8], [(u"*"), 9], [(u"/"), 9], [(u"%"), 9], [(u"**"), 9], [(u">>"), 
7], [(u"<<"), 7], [(u"&"), 6], [(u"^"), 5], [(u"|"), 4], [(u"=="), 3], [(u"!="), 3], [(u"<="), 3], [(u"<"), 
3], [(u">="), 3], [(u">"), 3]])
            op = __cpm[this, "source"]
            left = this.firstChild
            right = this.lastChild
            if __x_cb(__x_not(oppMap.has(op))):
                raise InternalError((u"Cannot writePython for binary ") + op)
            # end if (line 1123)
            p = oppMap.get(op)
            lp = p
            rp = p + 1
            if __x_cb(__x_eq(op, (u"**"))):
                lp = 11
                rp = 11
            # end if (line 1129)
            if __x_cb(__x_eq(p, 3)):
                lp = 4
                rp = 4
            # end if (line 1133)
            ap = p < parentType
            lsp = (u"") if __x_cb(ap) else contchr
            if __x_cb(ap):
                writer.write((u"("), False)
            # end if (line 1139)
            left.writePython(writer, lsp, lp)
            writer.write((u" ") + op + (u" "), lsp)
            right.writePython(writer, lsp, rp)
            if __x_cb(ap):
                writer.write((u")"), contchr)
            # end if (line 1145)
        # end function __m_writePython (line 1116)

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 1150)

        def __m_BinaryOperatorElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_BinaryOperatorElement (line 1155)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1160)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1166)

        __cpiT = __x_dpif("BinaryOperatorElement", {"__slots__": ("source",)})
        __clsT = __x_dcls("BinaryOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "dump": __m_dump, "functionalize": __m_functionalize, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_BinaryOperatorElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory BinaryOperatorElement, __c_BinaryOperatorElement (line 1060)

    def __c_BinaryLogicalElement(__cexT):
        def __g_typeName(this):
            return (u"logic")
        # end function __g_typeName (line 1184)

        def __g_complex(this):
            if __x_cb(this.theGlobal.enableImplicitBooleanConversion):
                return True
            # end if (line 1189)
            return __x_cb(__x_eq(__cpm[this, "source"], (u"??"))) or (super(__clsT, this)).complex
        # end function __g_complex (line 1188)

        def __g_constantOnly(this):
            return __x_cb(this.firstChild.constantOnly) and this.lastChild.constantOnly
        # end function __g_constantOnly (line 1195)

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly (line 1199)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList (line 1203)

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            op = __cpm[this, "source"]
            a = this.firstChild
            b = this.lastChild
            if __x_cb(__x_cb(__x_not(this.theGlobal.enableImplicitBooleanConversion)) and (__x_cb(__x_eq(op, (u"&&")))
 or __x_eq(op, (u"||")))):
                chk = CallElement.callGlobal((u"__x_cb"), a)
                this.prepend(chk)
                this.checkStruct()
            # end if (line 1213)
        # end function __m_functionalize (line 1207)

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
            # end if (line 1236)
            atrue = BodyElement(None)
            iife.append(atrue)
            atvr = AssignTempElement(atva)
            atrue.append(atvr)
            atvr.append(right)
            ife.simplifyExpressions()
            this.replaceWith(atvl.getLeftElement())
        # end function __m_simplifyExpressionsImplicitBooleanConversion (line 1221)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(this.theGlobal.enableImplicitBooleanConversion):
                __cpm[this, "simplifyExpressionsImplicitBooleanConversion"]()
                return
            # end if (line 1256)
            if __x_cb(__x_not(this.complex)):
                return
            # end if (line 1260)
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
            # end if (line 1277)
            atrue = BodyElement(None)
            iife.append(atrue)
            atvr = AssignTempElement(atva)
            atrue.append(atvr)
            atvr.append(right)
            ife.simplifyExpressions()
            this.replaceWith(atvl.getLeftElement())
        # end function __m_simplifyExpressions (line 1254)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            op = __cpm[this, "source"]
            left = this.firstChild
            right = this.lastChild
            if __x_cb(__x_cb(__x_eq(op, (u"||"))) or __x_eq(op, (u"&&"))):
                ap = 2 <= parentType
                lsp = (u"") if __x_cb(ap) else contchr
                if __x_cb(ap):
                    writer.write((u"("), False)
                # end if (line 1304)
                left.writePython(writer, lsp, 3)
                writer.write((u" or ") if __x_cb(__x_eq(op, (u"||"))) else (u" and "), lsp)
                right.writePython(writer, lsp, 2)
                if __x_cb(ap):
                    writer.write((u")"), contchr)
                # end if (line 1310)
            else:
                raise InternalError((u"Cannot writePython for logic ") + op)
            # end if (line 1301)
        # end function __m_writePython (line 1297)

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 1318)

        def __m_BinaryLogicalElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_BinaryLogicalElement (line 1323)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1328)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1334)

        __cpiT = __x_dpif("BinaryLogicalElement", {"__slots__": ("source",), "simplifyExpressionsImplicitBooleanConversion": __x_smet(__m_simplifyExpressionsImplicitBooleanConversion)})
        __clsT = __x_dcls("BinaryLogicalElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "complex": __x_prop(__g_complex, None), "constantOnly": __x_prop(__g_constantOnly, None), "dump": __m_dump, 
"functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_BinaryLogicalElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory BinaryLogicalElement, __c_BinaryLogicalElement (line 1183)

    def __c_BlockElement(__cexT):
        def __g_typeName(this):
            return (u"block")
        # end function __g_typeName (line 1353)

        def __g_structList(this):
            return ArrayList([ElementPattern(StatementElement, 0, True)])
        # end function __g_structList (line 1357)

        def __m_generatePython(this, ctx):
            def __f5V_(e, k, t):
                e.generatePython(ctx)
            # end function <anonymous> (__f5V_) (line 1362)

            this.forEachChild(__f5V_)
        # end function __m_generatePython (line 1361)

        def __m_BlockElement(this, range):
            __csu(this, range)
        # end function __m_BlockElement (line 1369)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1373)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1379)

        __clsT = __x_dcls("BlockElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_BlockElement})
        return __clsT
    # end class factory BlockElement, __c_BlockElement (line 1352)

    def __c_BodyElement(__cexT):
        def __g_typeName(this):
            return (u"body")
        # end function __g_typeName (line 1391)

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall (line 1395)

        def __g_structList(this):
            return ArrayList([ElementPattern(StatementElement, 0, True)])
        # end function __g_structList (line 1399)

        def __m_generatePython(this, ctx):
            def __f68_(e, k, t):
                e.generatePython(ctx)
            # end function <anonymous> (__f68_) (line 1404)

            this.forEachChild(__f68_)
        # end function __m_generatePython (line 1403)

        def __m_BodyElement(this, range):
            __csu(this, range)
        # end function __m_BodyElement (line 1411)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1415)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1421)

        __clsT = __x_dcls("BodyElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "allowSuperCall": __x_prop(__g_allowSuperCall, None), 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_BodyElement})
        return __clsT
    # end class factory BodyElement, __c_BodyElement (line 1390)

    def __c_FundamentalLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"literal-abstract")
        # end function __g_typeName (line 1434)

        def __g_complex(this):
            return False
        # end function __g_complex (line 1438)

        def __g_constantOnly(this):
            return True
        # end function __g_constantOnly (line 1442)

        def __g_tempVarOnly(this):
            return True
        # end function __g_tempVarOnly (line 1446)

        def __m_replaceWithTemp(this, optional = (True)):
            if __x_cb(optional):
                return None
            # end if (line 1451)
            return (super(__clsT, this)).replaceWithTemp(False)
        # end function __m_replaceWithTemp (line 1450)

        def __m_FundamentalLiteralElement(this, range):
            __csu(this, range)
        # end function __m_FundamentalLiteralElement (line 1457)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1461)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1467)

        __clsT = __x_dcls("FundamentalLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "complex": __x_prop(__g_complex, None), "constantOnly": __x_prop(__g_constantOnly, None), "replaceWithTemp": __m_replaceWithTemp, 
"tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_FundamentalLiteralElement})
        return __clsT
    # end class factory FundamentalLiteralElement, __c_FundamentalLiteralElement (line 1433)

    def __c_BooleanLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"boolean")
        # end function __g_typeName (line 1480)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"True") if __x_cb(__cpm[this, "value"]) else (u"False"), contchr)
        # end function __m_writePython (line 1484)

        def __m_dump(this, ctx):
            ctx.attr((u"value"), __cpm[this, "value"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 1488)

        def __m_BooleanLiteralElement(this, value, range):
            __csu(this, range)
            __cpm[this, "value"] = value
        # end function __m_BooleanLiteralElement (line 1493)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1498)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1504)

        __cpiT = __x_dpif("BooleanLiteralElement", {"__slots__": ("value",)})
        __clsT = __x_dcls("BooleanLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_BooleanLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory BooleanLiteralElement, __c_BooleanLiteralElement (line 1479)

    def __c_BreakElement(__cexT):
        def __m_generatePython(this, ctx):
            ctx.writeln((u"break"))
        # end function __m_generatePython (line 1520)

        def __m_BreakElement(this, range):
            __csu(this, range)
        # end function __m_BreakElement (line 1524)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1528)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1534)

        __clsT = __x_dcls("BreakElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"__init__": __m_BreakElement})
        return __clsT
    # end class factory BreakElement, __c_BreakElement (line 1519)

    def __c_CallElement(__cexT):
        def __g_typeName(this):
            return (u"call")
        # end function __g_typeName (line 1546)

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall (line 1550)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False), ElementPattern(ArgumentElement, 1, False)])
        # end function __g_structList (line 1554)

        def __m_checkVariables(this):
            callee = this.firstChild
            argv = this.lastChild
            supcall = __x_iof(this.firstChild, SuperElement)
            if __x_cb(__x_not(supcall)):
                callee.checkVariables()
            elif __x_cb(__x_not(this.allowSuperCall)):
                raise CompileError((u"super() statement unexpected here"), this.range)
            # end if (line 1562)
            argv.checkVariables()
            if __x_cb(supcall):
                fn = this.theFunction
                fn.meetSuper(this.range)
            # end if (line 1568)
        # end function __m_checkVariables (line 1558)

        def __m_functionalize(this):
            (super(__clsT, this)).functionalize()
            supcall = __x_iof(this.firstChild, SuperElement)
            if __x_cb(supcall):
                argv = this.lastChild
                argv.prepend(ThisElement(None))
            # end if (line 1577)
        # end function __m_functionalize (line 1574)

        def __m_simplifyExpressions(this):
            callee = this.firstChild
            argv = this.lastChild
            supcall = __x_iof(this.firstChild, SuperElement)
            if __x_cb(argv.complex):
                if __x_cb(__x_not(supcall)):
                    callee2 = callee.replaceWithTemp()
                    this.insertTempAssign(callee2)
                # end if (line 1588)
                argv.simplifyExpressions()
            elif __x_cb(callee.complex):
                callee.simplifyExpressions()
            # end if (line 1587)
        # end function __m_simplifyExpressions (line 1583)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            callee = this.firstChild
            supcall = __x_iof(this.firstChild, SuperElement)
            argv = this.lastChild
            if __x_cb(supcall):
                writer.write((u"__csu"), False)
            else:
                callee.writePython(writer, contchr, 12)
            # end if (line 1602)
            argv.writePython(writer, contchr, 12)
        # end function __m_writePython (line 1598)

        def __m_CallElement(this, range):
            __csu(this, range)
        # end function __m_CallElement (line 1610)

        def __n_callGlobal(this, name, arg):
            cc = CallElement(None)
            callee = VarElement.getGlobalVar(name)
            cc.append(callee)
            argv = ArgumentElement(None)
            cc.append(argv)
            argv.append(arg)
            return cc
        # end function __n_callGlobal (line 1614)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1624)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1630)

        __clsT = __x_dcls("CallElement", __cexT, {"__slots__": (), "callGlobal": __n_callGlobal, "__init__": __csi}, 
{"__slots__": (), "allowSuperCall": __x_prop(__g_allowSuperCall, None), "checkVariables": __m_checkVariables, 
"functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_CallElement})
        return __clsT
    # end class factory CallElement, __c_CallElement (line 1545)

    def __c_CatchElement(__cexT):
        def __g_typeName(this):
            return (u"catch")
        # end function __g_typeName (line 1644)

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 1, True), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 1648)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, TryBlockElement))):
                raise InternalError((u"malformed structure in CatchElement (not in TryBlockElement)"))
            # end if (line 1653)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 1652)

        def __m_generatePython(this, gen):
            writer = LineWriter()
            writer.write((u"except __x_errT as "), False)
            ex = this.firstChild
            body = this.lastChild
            if __x_cb(__x_eq(ex, body)):
                writer.write(this.theFunction.allocTempVar().toRawPython(), False)
            else:
                ex.writePython(writer, (u""))
            # end if (line 1664)
            writer.write((u":"), False)
            writer.finalize(gen)
            gen.tab()
            ex.generateRenameAssignment(gen)
            body.generatePython(gen)
            gen.TAB()
        # end function __m_generatePython (line 1659)

        def __m_CatchElement(this, range):
            __csu(this, range)
        # end function __m_CatchElement (line 1677)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 1681)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 1687)

        __clsT = __x_dcls("CatchElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_CatchElement})
        return __clsT
    # end class factory CatchElement, __c_CatchElement (line 1643)

    def __c_ClassElement(__cexT):
        def __g_typeName(this):
            return (u"class")
        # end function __g_typeName (line 1700)

        def __g_theClass(this):
            return this
        # end function __g_theClass (line 1704)

        def __g_structList(this):
            return ArrayList([ElementPattern(MethodGroupElement, 1, False), ElementPattern(StaticGroupElement, 1, 
False), ElementPattern(InstanceGroupElement, 1, False)])
        # end function __g_structList (line 1708)

        def __g_allowThis(this):
            return True
        # end function __g_allowThis (line 1713)

        def __g_allowSuper(this):
            return True
        # end function __g_allowSuper (line 1717)

        def __g_allowSuperCall(this):
            return __cpm[this, "hasSuper"]
        # end function __g_allowSuperCall (line 1721)

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions (line 1725)

        def __g_staticInit(this):
            this.checkStruct()
            e = this.firstChild.nextSibling
            return e
        # end function __g_staticInit (line 1731)

        def __g_instanceInit(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_instanceInit (line 1737)

        def __g_body(this):
            return None
        # end function __g_body (line 1743)

        def __m_referVar(this, name, range = (None)):
            if __x_cb(__x_eq(this.tag.name, name)):
                return this.tag
            # end if (line 1748)
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar (line 1747)

        def __m_registerFunctionDefinition(this, tag, range = (None)):
            def coerce(tag):
                if __x_cb(__x_not(__x_iof(tag, MethodTag))):
                    raise InternalError((u"only method is allowed in class"))
                # end if (line 1756)
                return tag
            # end function coerce (line 1755)

            tag2 = coerce(tag)
            st = tag2.isStatic
            o = __cpm[this, "staticMembers"] if __x_cb(st) else __cpm[this, "instanceMembers"]
            n = tag2.name
            cfd = o.get(n, None)
            if __x_cb(__x_eq(cfd, None)):
                cfd = ClassFieldDescriptor(n, st)
                o.set(n, cfd)
            # end if (line 1767)
            cfd.meetMethod(tag2)
        # end function __m_registerFunctionDefinition (line 1754)

        def __m_registerLocalVar(this, name, range = (None)):
            raise InternalError((u"only property is allowed in class"))
        # end function __m_registerLocalVar (line 1774)

        def __m_registerProperty(this, name, isPublic, isStatic, range):
            st = isStatic
            n = name
            o = __cpm[this, "staticMembers"] if __x_cb(st) else __cpm[this, "instanceMembers"]
            cfd = o.get(n, None)
            if __x_cb(__x_eq(cfd, None)):
                cfd = ClassFieldDescriptor(n, st)
                o.set(n, cfd)
            # end if (line 1783)
            cfd.meetProperty(isPublic, range)
        # end function __m_registerProperty (line 1778)

        def __m_hasPrivateInstance(this, name):
            o = __cpm[this, "instanceMembers"]
            cfd = o.get(name, None)
            if __x_cb(__x_eq(cfd, None)):
                return False
            # end if (line 1793)
            return cfd.isPrivate
        # end function __m_hasPrivateInstance (line 1790)

        def __m_hasPrivateStatic(this, name):
            o = __cpm[this, "staticMembers"]
            cfd = o.get(name, None)
            if __x_cb(__x_eq(cfd, None)):
                return False
            # end if (line 1802)
            return cfd.isPrivate
        # end function __m_hasPrivateStatic (line 1799)

        def __m_declareVariable(this):
            if __x_cb(__x_not(__x_iof(this.parentFunction, GlobalElement))):
                raise InternalError((u"Public member not in global"))
            # end if (line 1809)
            this.theGlobal.registerClassDefinition(this.tag, this.tag.range)
            if __x_cb(__cpm[this, "isPublic"]):
                this.theGlobal.declarePublic(this.tag.name, this.tag.range)
            # end if (line 1813)
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable (line 1808)

        def __m_createClassInitElement(this):
            return ClassInitElement(__cpm[this, "hasSuper"], this.tag, this.tag.range)
        # end function __m_createClassInitElement (line 1819)

        def __m_generatePython(this, gen):
            def __f8A_(p, k, s):
                if __x_cb(p.isPrivate):
                    __u_haspi.val = True
                    return False
                # end if (line 1825)
            # end function <anonymous> (__f8A_) (line 1824)

            def __f8B_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and p.isPrivate)):
                    return
                # end if (line 1832)
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u"\\"))
                # end if (line 1835)
                writer.write((u"\"") + p.toPython() + (u"\""), (u""))
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8B_) (line 1831)

            def __f8C_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and p.isPrivate)):
                    return
                # end if (line 1844)
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                if __x_cb(p.isMethod):
                    writer.write((u"__x_smet("), False)
                # end if (line 1849)
                writer.write(p.toMethodName(), False)
                if __x_cb(p.isMethod):
                    writer.write((u")"), False)
                # end if (line 1853)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8C_) (line 1843)

            def __f8D_(p, k, s):
                if __x_cb(p.isPrivate):
                    __u_hasps.val = True
                    return False
                # end if (line 1861)
            # end function <anonymous> (__f8D_) (line 1860)

            def __f8E_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and p.isPrivate)):
                    return
                # end if (line 1868)
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u""))
                # end if (line 1871)
                writer.write((u"\"") + p.toPython() + (u"\""), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8E_) (line 1867)

            def __f8F_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and p.isPrivate)):
                    return
                # end if (line 1880)
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                writer.write(p.toMethodName(), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8F_) (line 1879)

            def __f8G_(p, k, s):
                if __x_cb(__x_not(p.isPrivate)):
                    return
                # end if (line 1891)
                p2 = sm.get(k, None)
                if __x_cb(__x_cb(__x_ne(p2, None)) and p2.isPrivate):
                    __u_haspis.val = True
                    return False
                # end if (line 1895)
            # end function <anonymous> (__f8G_) (line 1890)

            def __f8H_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and __x_not(p.isPrivate))):
                    return
                # end if (line 1902)
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u""))
                # end if (line 1905)
                writer.write((u"\"") + p.toPython() + (u"\""), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8H_) (line 1901)

            def __f8I_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and __x_not(p.isPrivate))):
                    return
                # end if (line 1914)
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                writer.write(p.toMethodName(), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8I_) (line 1913)

            def __f8J_(p, k, a):
                if __x_cb(__x_not(__x_cb(p.isProperty) and __x_not(p.isPrivate))):
                    return
                # end if (line 1925)
                if __x_cb(__u_ppl.val > 0):
                    writer.write((u", "), (u""))
                # end if (line 1928)
                writer.write((u"\"") + p.toPython() + (u"\""), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8J_) (line 1924)

            def __f8K_(p, k, a):
                if __x_cb(__x_not(__x_cb(__x_not(p.isProperty)) and __x_not(p.isPrivate))):
                    return
                # end if (line 1937)
                writer.write((u", "), (u""))
                writer.write((u"\"") + p.toPython() + (u"\": "), False)
                writer.write(p.toMethodName(), False)
                __r0 = __u_ppl.val
                __u_ppl.val = __x_inc(__r0)
            # end function <anonymous> (__f8K_) (line 1936)

            def __f8L_(f, k, a):
                if __x_cb(f.isConstructor):
                    __u_ctag.val = f.tag
                    return False
                # end if (line 1948)
            # end function <anonymous> (__f8L_) (line 1947)

            __u_ctag = __x_var()
            __u_haspi = __x_var()
            __u_haspis = __x_var()
            __u_hasps = __x_var()
            __u_ppl = __x_var()
            sm = __cpm[this, "staticMembers"]
            im = __cpm[this, "instanceMembers"]
            gen.blank()
            sline = LineNumber()
            gen.logLineNumber(sline)
            writer = LineWriter()
            writer.write((u"def "), False)
            writer.write(this.tag.toFactoryName(), False)
            writer.write((u"("), (u""))
            if __x_cb(__cpm[this, "hasSuper"]):
                writer.write((u"__cexT"), (u""))
            # end if (line 1968)
            writer.write((u"):"), False)
            writer.finalize(gen)
            gen.tab()
            this.functionDefinitions.generatePython(gen)
            this.staticInit.generatePython(gen)
            this.instanceInit.generatePython(gen)
            gen.blank()
            __u_haspi.val = False
            im.forEach(__f8A_)
            if __x_cb(__u_haspi.val):
                writer = LineWriter()
                writer.write((u"__cpiT = __x_dpif("), False)
                writer.write((u"\"") + this.tag.toPython() + (u"\""), False)
                writer.write((u", "), (u""))
                writer.write((u"{"), (u""))
                writer.write((u"\"__slots__\": ("), (u""))
                __u_ppl.val = 0
                im.forEach(__f8B_)
                if __x_cb(__x_eq(__u_ppl.val, 1)):
                    writer.write((u","), False)
                # end if (line 1989)
                writer.write((u")"), (u""))
                __u_ppl.val = 0
                im.forEach(__f8C_)
                writer.write((u"})"), False)
                writer.finalize(gen)
            # end if (line 1980)
            __u_hasps.val = False
            sm.forEach(__f8D_)
            if __x_cb(__u_hasps.val):
                writer = LineWriter()
                writer.write((u"__cpsT = __x_dpsf("), False)
                writer.write((u"\"") + this.tag.toPython() + (u"\""), False)
                writer.write((u", "), (u""))
                writer.write((u"{"), (u""))
                writer.write((u"\"__slots__\": ("), (u""))
                __u_ppl.val = 0
                sm.forEach(__f8E_)
                if __x_cb(__x_eq(__u_ppl.val, 1)):
                    writer.write((u","), False)
                # end if (line 2009)
                writer.write((u")"), False)
                __u_ppl.val = 0
                sm.forEach(__f8F_)
                writer.write((u"})"), False)
                writer.finalize(gen)
                gen.writeln((u"__csp = __cpsT()"))
            # end if (line 2000)
            __u_haspis.val = False
            im.forEach(__f8G_)
            writer = LineWriter()
            writer.write((u"__clsT = __x_dcls("), False)
            writer.write((u"\"") + this.tag.toPython() + (u"\""), False)
            writer.write((u", "), (u""))
            writer.write((u"__cexT") if __x_cb(__cpm[this, "hasSuper"]) else (u"__x_objT"), False)
            writer.write((u", "), False)
            writer.write((u"{"), (u""))
            writer.write((u"\"__slots__\": ("), (u""))
            __u_ppl.val = 0
            sm.forEach(__f8H_)
            if __x_cb(__x_eq(__u_ppl.val, 1)):
                writer.write((u","), False)
            # end if (line 2031)
            writer.write((u")"), False)
            __u_ppl.val = 0
            sm.forEach(__f8I_)
            writer.write((u", "), (u""))
            writer.write((u"\"__init__\": __csi"), False)
            writer.write((u"}, "), (u""))
            writer.write((u"{"), (u""))
            writer.write((u"\"__slots__\": ("), (u""))
            __u_ppl.val = 0
            im.forEach(__f8J_)
            if __x_cb(__x_eq(__u_ppl.val, 1)):
                writer.write((u","), False)
            # end if (line 2044)
            writer.write((u")"), False)
            __u_ppl.val = 0
            im.forEach(__f8K_)
            __u_ctag.val = None
            this.functionDefinitions.forEachChild(__f8L_)
            writer.write((u", "), (u""))
            if __x_cb(__x_eq(__u_ctag.val, None)):
                writer.write((u"\"__init__\": __csu"), False)
            else:
                writer.write((u"\"__init__\": "), False)
                writer.write(__u_ctag.val.toPython(), False)
            # end if (line 2053)
            writer.write((u"})"), False)
            writer.finalize(gen)
            if __x_cb(__u_haspi.val):
                gen.writeln((u"__cpm = __x_prmT(__clsT, __cpiT)"))
            # end if (line 2061)
            if __x_cb(__u_hasps.val):
                gen.writeln((u"__csg = __x_csgT(__clsT, __csp)"))
            # end if (line 2064)
            if __x_cb(__u_haspis.val):
                gen.writeln((u"__cpg = __x_cpgT(__clsT, __cpm, __csp)"))
            # end if (line 2067)
            gen.writeln((u"return __clsT"))
            gen.TAB()
            gen.comment((u"end class factory %s, %s (line %l)"), this.tag.toPython(), this.tag.toFactoryName(), sline)
        # end function __m_generatePython (line 1823)

        def __m_dump(this, ctx):
            ctx.attr((u"tag"), this.tag)
            ctx.attr((u"public"), __cpm[this, "isPublic"])
            ctx.attr((u"extended"), __cpm[this, "hasSuper"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 2075)

        def __m_ClassElement(this, name, hasSuper, isPublic, tagRange, range):
            __csu(this, range)
            this.tag = ClassTag(name, this, tagRange)
            __cpm[this, "isPublic"] = isPublic
            __cpm[this, "hasSuper"] = hasSuper
            this.append(MethodGroupElement())
            this.append(StaticGroupElement())
            this.append(InstanceGroupElement(__cpm[this, "instanceMembers"]))
        # end function __m_ClassElement (line 2082)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2092)

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
        # end instance initializer and super constructor __csu (line 2098)

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
    # end class factory ClassElement, __c_ClassElement (line 1699)

    def __c_ClassGroupElement(__cexT):
        def __g_typeName(this):
            return (u"classgroup")
        # end function __g_typeName (line 2126)

        def __g_structList(this):
            return ArrayList([ElementPattern(ClassElement, 0, True)])
        # end function __g_structList (line 2130)

        def __m_ClassGroupElement(this):
            __csu(this, None)
        # end function __m_ClassGroupElement (line 2134)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2138)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2144)

        __clsT = __x_dcls("ClassGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ClassGroupElement})
        return __clsT
    # end class factory ClassGroupElement, __c_ClassGroupElement (line 2125)

    def __c_ClassInitElement(__cexT):
        def __g_typeName(this):
            return (u"classinit")
        # end function __g_typeName (line 2156)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, __x_not(__cpm[this, "extended"]))])
        # end function __g_structList (line 2160)

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            writer.write(__cpm[this, "tag"].toPython(), False)
            writer.write((u" = "), (u"\\"))
            writer.write(__cpm[this, "tag"].toFactoryName(), False)
            writer.write((u"("), (u"\\"))
            if __x_cb(__cpm[this, "extended"]):
                sup = this.firstChild
                sup.writePython(writer, False)
            # end if (line 2170)
            writer.write((u")"), (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython (line 2164)

        def __m_dump(this, ctx):
            ctx.attr((u"tag"), __cpm[this, "tag"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 2178)

        def __m_ClassInitElement(this, extended, tag, range):
            __csu(this, range)
            __cpm[this, "extended"] = extended
            __cpm[this, "tag"] = tag
        # end function __m_ClassInitElement (line 2183)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2189)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2195)

        __cpiT = __x_dpif("ClassInitElement", {"__slots__": ("extended", "tag")})
        __clsT = __x_dcls("ClassInitElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"dump": __m_dump, "generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_ClassInitElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ClassInitElement, __c_ClassInitElement (line 2155)

    def __c_ComplexLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"imag")
        # end function __g_typeName (line 2212)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(parentType >= 12):
                writer.write((u"("), False)
            # end if (line 2217)
            s = ArrayList(__cpm[this, "source"])
            s.set(-1, (u"j"))
            writer.write(s.join((u"")), False)
            if __x_cb(parentType >= 12):
                writer.write((u")"), False)
            # end if (line 2223)
        # end function __m_writePython (line 2216)

        def __m_dump(this, ctx):
            ctx.attr((u"source"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 2228)

        def __m_ComplexLiteralElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_ComplexLiteralElement (line 2233)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2238)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2244)

        __cpiT = __x_dpif("ComplexLiteralElement", {"__slots__": ("source",)})
        __clsT = __x_dcls("ComplexLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_ComplexLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ComplexLiteralElement, __c_ComplexLiteralElement (line 2211)

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
        # end function __m_simplifyExpressions (line 2260)

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "operator"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 2277)

        def __m_generatePython(this, ctx):
            raise InternalError((u"cannot generate Python for CompoundAssignElement"))
        # end function __m_generatePython (line 2282)

        def __m_CompoundAssignElement(this, operator, range):
            __csu(this, range)
            m = StringMap([[(u"*="), (u"*")], [(u"**="), (u"**")], [(u"/="), (u"/")], [(u"%="), (u"%")], [(u"+="), 
(u"+")], [(u"-="), (u"-")], [(u"<<="), (u"<<")], [(u">>="), (u">>")], [(u"&="), (u"&")], [(u"^="), (u"^")], 
[(u",="), (u",")]])
            if __x_cb(__x_not(m.has(operator))):
                raise InternalError((u"unknown assignment operator ") + operator)
            # end if (line 2291)
            __cpm[this, "operator"] = m.get(operator)
        # end function __m_CompoundAssignElement (line 2286)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2297)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2303)

        __cpiT = __x_dpif("CompoundAssignElement", {"__slots__": ("operator",)})
        __clsT = __x_dcls("CompoundAssignElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"__init__": __m_CompoundAssignElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory CompoundAssignElement, __c_CompoundAssignElement (line 2259)

    def __c_ConditionElement(__cexT):
        def __g_typeName(this):
            return (u"cond")
        # end function __g_typeName (line 2320)

        def __g_theStatement(this):
            return this.parent.theStatement
        # end function __g_theStatement (line 2324)

        def __g_complex(this):
            this.checkStruct()
            return this.firstChild.complex
        # end function __g_complex (line 2328)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 2333)

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            exp = this.firstChild
            cc = CallElement.callGlobal((u"__x_tob") if __x_cb(this.theGlobal.enableImplicitBooleanConversion) else (u"__x_cb"), 
exp)
            this.append(cc)
            this.checkStruct()
        # end function __m_functionalize (line 2337)

        def __m_simplifyExpressions(this):
            raise InternalError((u"cannot simplifyExpressions of ConditionElement"))
        # end function __m_simplifyExpressions (line 2347)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            exp = this.firstChild
            exp.writePython(writer, contchr, parentType)
        # end function __m_writePython (line 2351)

        def __m_ConditionElement(this, range):
            __csu(this, range)
        # end function __m_ConditionElement (line 2356)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2360)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2366)

        __clsT = __x_dcls("ConditionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"complex": __x_prop(__g_complex, None), "functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_ConditionElement})
        return __clsT
    # end class factory ConditionElement, __c_ConditionElement (line 2319)

    def __c_ContinueElement(__cexT):
        def __m_generatePython(this, ctx):
            ctx.writeln((u"continue"))
        # end function __m_generatePython (line 2380)

        def __m_ContinueElement(this, range):
            __csu(this, range)
        # end function __m_ContinueElement (line 2384)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2388)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2394)

        __clsT = __x_dcls("ContinueElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"generatePython": __m_generatePython, "__init__": __m_ContinueElement})
        return __clsT
    # end class factory ContinueElement, __c_ContinueElement (line 2379)

    def __c_DeleteElement(__cexT):
        def __g_typeName(this):
            return (u"return")
        # end function __g_typeName (line 2406)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 2410)

        def __m_checkVariables(this):
            if __x_cb(__x_not(__x_iof(this.firstChild, LvalueElement))):
                raise CompileError((u"only left value can be deleted"), this.range)
            # end if (line 2415)
            (super(__clsT, this)).checkVariables()
        # end function __m_checkVariables (line 2414)

        def __m_generatePython(this, ctx):
            right = this.lastChild
            writer = LineWriter()
            writer.write((u"del "), False)
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython (line 2421)

        def __m_DeleteElement(this, range):
            __csu(this, range)
        # end function __m_DeleteElement (line 2429)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2433)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2439)

        __clsT = __x_dcls("DeleteElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DeleteElement})
        return __clsT
    # end class factory DeleteElement, __c_DeleteElement (line 2405)

    def __c_DestructGroupElement(__cexT):
        def __g_typeName(this):
            return (u"destrabstract")
        # end function __g_typeName (line 2452)

        def __g_declarator(this):
            return __cpm[this, "_declarator"]
        # end function __g_declarator (line 2456)

        def __m_checkStruct(this):
            def __fAI_(e, k, s):
                if __x_cb(__x_iof(e, DestructPropertyElement)):
                    if __x_cb(__x_ne(e.declarator, s.declarator)):
                        raise InternalError((u"malformed structure in ") + s.typeName + (u" (mismatched declarator property)"))
                    # end if (line 2463)
                else:
                    raise InternalError((u"malformed structure in ") + s.typeName + (u" (unknown child)"))
                # end if (line 2462)
            # end function <anonymous> (__fAI_) (line 2461)

            (super(__clsT, this)).checkStruct()
            this.forEachChild(__fAI_)
        # end function __m_checkStruct (line 2460)

        def __m_simplifyExpressions(this):
            raise InternalError((u"call abstract simplifyExpressions to ") + this.typeName)
        # end function __m_simplifyExpressions (line 2475)

        def __m_dump(this, ctx):
            ctx.attr((u"declare"), this.declarator)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 2479)

        def __m_DestructGroupElement(this, declarator, range):
            __csu(this, range)
            __cpm[this, "_declarator"] = declarator
        # end function __m_DestructGroupElement (line 2484)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2489)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2495)

        __cpiT = __x_dpif("DestructGroupElement", {"__slots__": ("_declarator",)})
        __clsT = __x_dcls("DestructGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "declarator": __x_prop(__g_declarator, None), "dump": __m_dump, "simplifyExpressions": __m_simplifyExpressions, 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_DestructGroupElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory DestructGroupElement, __c_DestructGroupElement (line 2451)

    def __c_DestructObjectElement(__cexT):
        def __g_typeName(this):
            return (u"destrobj")
        # end function __g_typeName (line 2512)

        def __g_structList(this):
            return ArrayList([ElementPattern(DestructPropertyElement, 0, False)])
        # end function __g_structList (line 2516)

        def __m_simplifyExpressions(this):
            def __fAS_(e, k, s):
                e.checkStruct()
                e.append(ate.getLeftElement())
                s.before(e)
                e.simplifyExpressions()
            # end function <anonymous> (__fAS_) (line 2521)

            ate = AssignTempElement(this.theFunction.allocTempVar())
            this.before(ate)
            right = this.lastChild
            ate.append(right)
            ate.simplifyExpressions()
            this.forEachChild(__fAS_)
            this.remove()
        # end function __m_simplifyExpressions (line 2520)

        def __m_DestructObjectElement(this, declarator, range):
            __csu(this, declarator, range)
        # end function __m_DestructObjectElement (line 2537)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2541)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2547)

        __clsT = __x_dcls("DestructObjectElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DestructObjectElement})
        return __clsT
    # end class factory DestructObjectElement, __c_DestructObjectElement (line 2511)

    def __c_DestructPropertyElement(__cexT):
        def __g_declarator(this):
            return __cpm[this, "_declarator"]
        # end function __g_declarator (line 2560)

        def __g_typeName(this):
            return (u"destrprop")
        # end function __g_typeName (line 2564)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, DestructObjectElement))):
                raise InternalError((u"malformed structure in DestructPropertyElement (not in DestructObjectElement)"))
            # end if (line 2569)
            e = this.firstChild
            if __x_cb(__x_cb(__x_ne(e, this.lastChild)) or __x_not(__x_cb(__x_iof(e, LvalueElement)) or __x_iof(e, 
DestructGroupElement))):
                raise InternalError((u"malformed structure in ") + this.typeName + (u" (unknown child)"))
            # end if (line 2573)
            if __x_cb(__x_ne(e.declarator, this.declarator)):
                raise InternalError((u"malformed structure in ") + this.typeName + (u" (disagreed declarator property)"))
            # end if (line 2577)
        # end function __m_checkStruct (line 2568)

        def __m_checkVariables(this):
            this.checkStruct()
            e = this.firstChild
            if __x_cb(__x_iof(e, LvalueElement)):
                e.checkWrite()
            else:
                e.checkVariables()
            # end if (line 2585)
        # end function __m_checkVariables (line 2582)

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
            # end if (line 2597)
            this.remove()
        # end function __m_simplifyExpressions (line 2592)

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            ctx.attr((u"declare"), this.declarator)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 2616)

        def __m_DestructPropertyElement(this, declarator, attribute, range):
            __csu(this, range)
            __cpm[this, "_declarator"] = declarator
            __cpm[this, "attribute"] = attribute
        # end function __m_DestructPropertyElement (line 2622)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2628)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2634)

        __cpiT = __x_dpif("DestructPropertyElement", {"__slots__": ("_declarator", "attribute")})
        __clsT = __x_dcls("DestructPropertyElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "checkVariables": __m_checkVariables, "declarator": __x_prop(__g_declarator, None), 
"dump": __m_dump, "simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DestructPropertyElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory DestructPropertyElement, __c_DestructPropertyElement (line 2559)

    def __c_DoWhileElement(__cexT):
        def __g_typeName(this):
            return (u"dowhile")
        # end function __g_typeName (line 2652)

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 2656)

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
        # end function __m_simplifyExpressions (line 2660)

        def __m_generatePython(this, gen):
            raise InternalError((u"generate python for do-while"))
        # end function __m_generatePython (line 2686)

        def __m_DoWhileElement(this, range):
            __csu(this, range)
        # end function __m_DoWhileElement (line 2690)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2694)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2700)

        __clsT = __x_dcls("DoWhileElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_DoWhileElement})
        return __clsT
    # end class factory DoWhileElement, __c_DoWhileElement (line 2651)

    def __c_ElifElement(__cexT):
        def __g_typeName(this):
            return (u"elif")
        # end function __g_typeName (line 2713)

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 2717)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, IfBlockElement))):
                raise InternalError((u"malformed structure in IfElement (not in IfBlockElement)"))
            # end if (line 2722)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 2721)

        def __g_complex(this):
            return this.firstChild.complex
        # end function __g_complex (line 2728)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(this.complex):
                raise InternalError((u"simplify a elif with complex condition"))
            # end if (line 2734)
            body = this.lastChild
            body.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions (line 2732)

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
        # end function __m_generatePython (line 2742)

        def __m_ElifElement(this, range):
            __csu(this, range)
        # end function __m_ElifElement (line 2755)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2759)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2765)

        __clsT = __x_dcls("ElifElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"complex": __x_prop(__g_complex, None), "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ElifElement})
        return __clsT
    # end class factory ElifElement, __c_ElifElement (line 2712)

    def __c_ElseElement(__cexT):
        def __g_typeName(this):
            return (u"else")
        # end function __g_typeName (line 2778)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, IfBlockElement))):
                raise InternalError((u"malformed structure in IfElement (not in IfBlockElement)"))
            # end if (line 2783)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 2782)

        def __m_generatePython(this, ctx):
            ctx.writeln((u"else:"))
            ctx.tab()
            (super(__clsT, this)).generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython (line 2789)

        def __m_ElseElement(this, range):
            __csu(this, range)
        # end function __m_ElseElement (line 2796)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2800)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2806)

        __clsT = __x_dcls("ElseElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "typeName": __x_prop(__g_typeName, None), "__init__": __m_ElseElement})
        return __clsT
    # end class factory ElseElement, __c_ElseElement (line 2777)

    def __c_ExpressionStatementElement(__cexT):
        def __g_typeName(this):
            return (u"exprstat")
        # end function __g_typeName (line 2818)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 2822)

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall (line 2826)

        def __m_simplifyExpressions(this):
            (super(__clsT, this)).simplifyExpressions()
            if __x_cb(this.lastChild.tempVarOnly):
                this.remove()
            # end if (line 2832)
        # end function __m_simplifyExpressions (line 2830)

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            right = this.lastChild
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython (line 2837)

        def __m_ExpressionStatementElement(this, range):
            __csu(this, range)
        # end function __m_ExpressionStatementElement (line 2844)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2848)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2854)

        __clsT = __x_dcls("ExpressionStatementElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuperCall": __x_prop(__g_allowSuperCall, None), "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ExpressionStatementElement})
        return __clsT
    # end class factory ExpressionStatementElement, __c_ExpressionStatementElement (line 2817)

    def __c_FinallyElement(__cexT):
        def __g_typeName(this):
            return (u"finally")
        # end function __g_typeName (line 2867)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, TryBlockElement))):
                raise InternalError((u"malformed structure in TryElement (not in TryBlockElement)"))
            # end if (line 2872)
            (super(__clsT, this)).checkStruct()
            __cpm[this, "checkJump"](this)
        # end function __m_checkStruct (line 2871)

        def __m_checkJump(this, e):
            def __fCG_(ee, k, a):
                cj(ee)
            # end function <anonymous> (__fCG_) (line 2880)

            if __x_cb(__x_cb(__x_cb(__x_iof(e, ReturnElement)) or __x_iof(e, BreakElement)) or __x_iof(e, ContinueElement)):
                raise CompileError((u"Jump statements occur in finally block"), this.range)
            # end if (line 2884)
            if __x_cb(__x_iof(e, ExpressionElement)):
                return
            # end if (line 2887)
            cj = __cpm[this, "checkJump"]
            e.forEachChild(__fCG_)
        # end function __m_checkJump (line 2879)

        def __m_generatePython(this, ctx):
            ctx.writeln((u"finally:"))
            ctx.tab()
            (super(__clsT, this)).generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython (line 2894)

        def __m_FinallyElement(this, range):
            __csu(this, range)
        # end function __m_FinallyElement (line 2901)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 2905)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 2911)

        __cpiT = __x_dpif("FinallyElement", {"__slots__": (), "checkJump": __x_smet(__m_checkJump)})
        __clsT = __x_dcls("FinallyElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "typeName": __x_prop(__g_typeName, None), "__init__": __m_FinallyElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory FinallyElement, __c_FinallyElement (line 2866)

    def __c_FunctionElement(__cexT):
        def __g_typeName(this):
            return (u"function")
        # end function __g_typeName (line 2927)

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(ParameterGroupElement, 
1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 2931)

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions (line 2936)

        def __g_parameters(this):
            this.checkStruct()
            e = this.firstChild.nextSibling
            return e
        # end function __g_parameters (line 2942)

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body (line 2948)

        def __m_referVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if (line 2956)
            if __x_cb(__x_cb(__x_ne(this.tag.name, None)) and __x_eq(this.tag.name, name)):
                return this.tag
            # end if (line 2959)
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar (line 2954)

        def __m_generatePython(this, gen):
            def __fCT_(v, n, s):
                if __x_cb(__x_not(v.closure)):
                    return
                # end if (line 2967)
                gen.writeln(v.toRawPython() + (u" = __x_var()"))
            # end function <anonymous> (__fCT_) (line 2966)

            def __fCU_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    __u_nwv.val = True
                    return False
                # end if (line 2974)
            # end function <anonymous> (__fCU_) (line 2973)

            def __fCV_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    gen.writeln(v.toRawPython() + (u" = 0"))
                # end if (line 2981)
            # end function <anonymous> (__fCV_) (line 2980)

            __u_nwv = __x_var()
            gen.blank()
            sline = LineNumber()
            gen.logLineNumber(sline)
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
            this.forEachLocalVar(__fCT_)
            this.parameters.generatePython(gen)
            this.body.generatePython(gen)
            __u_nwv.val = False
            this.forEachLocalVar(__fCU_)
            if __x_cb(__u_nwv.val):
                gen.comment((u"Uninitialized variable:"))
                gen.writeln((u"return"))
                this.forEachLocalVar(__fCV_)
            # end if (line 3005)
            gen.TAB()
            gen.comment((u"end function %s (line %l)"), this.tag.toComment(), sline)
        # end function __m_generatePython (line 2965)

        def __m_dump(this, ctx):
            ctx.attr((u"tag"), this.tag)
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 3014)

        def __m_FunctionElement(this, range):
            __csu(this, range)
        # end function __m_FunctionElement (line 3019)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3023)

        def __csu(this, *argv):
            # initialize properties
            this.tag = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3029)

        __clsT = __x_dcls("FunctionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("tag",), 
"body": __x_prop(__g_body, None), "dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), 
"generatePython": __m_generatePython, "parameters": __x_prop(__g_parameters, None), "referVar": __m_referVar, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_FunctionElement})
        return __clsT
    # end class factory FunctionElement, __c_FunctionElement (line 2926)

    def __c_FunctionDefinitionElement(__cexT):
        def __m_declareVariable(this):
            this.parentFunction.registerFunctionDefinition(this.tag, this.tag.range)
            if __x_cb(__cpm[this, "isPublic"]):
                if __x_cb(__x_not(__x_iof(this.parentFunction, GlobalElement))):
                    raise InternalError((u"Public member not in global"))
                # end if (line 3047)
                this.theGlobal.declarePublic(this.tag.name, this.tag.range)
            # end if (line 3046)
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable (line 3044)

        def __m_dump(this, ctx):
            ctx.attr((u"public"), __cpm[this, "isPublic"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 3055)

        def __m_FunctionDefinitionElement(this, name, isPublic, tagRange, range):
            __csu(this, range)
            this.tag = FunctionTag(name, this, tagRange)
            __cpm[this, "isPublic"] = isPublic
            this.append(FunctionGroupElement())
            this.append(ParameterGroupElement())
            this.append(BodyElement(None))
        # end function __m_FunctionDefinitionElement (line 3060)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3069)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "isPublic"] = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3075)

        __cpiT = __x_dpif("FunctionDefinitionElement", {"__slots__": ("isPublic",)})
        __clsT = __x_dcls("FunctionDefinitionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "declareVariable": __m_declareVariable, "dump": __m_dump, "__init__": __m_FunctionDefinitionElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory FunctionDefinitionElement, __c_FunctionDefinitionElement (line 3043)

    def __c_FunctionExpressionElement(__cexT):
        def __m_FunctionExpressionElement(this, name, tagRange, range):
            __csu(this, range)
            this.tag = FunctionExpTag(name, this, tagRange)
            this.append(FunctionGroupElement())
            this.append(ParameterGroupElement())
            this.append(BodyElement(None))
        # end function __m_FunctionExpressionElement (line 3092)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3100)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3106)

        __clsT = __x_dcls("FunctionExpressionElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "__init__": __m_FunctionExpressionElement})
        return __clsT
    # end class factory FunctionExpressionElement, __c_FunctionExpressionElement (line 3091)

    def __c_FunctionGroupElement(__cexT):
        def __g_typeName(this):
            return (u"functiongroup")
        # end function __g_typeName (line 3118)

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionElement, 0, True)])
        # end function __g_structList (line 3122)

        def __m_FunctionGroupElement(this):
            __csu(this, None)
        # end function __m_FunctionGroupElement (line 3126)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3130)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3136)

        __clsT = __x_dcls("FunctionGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_FunctionGroupElement})
        return __clsT
    # end class factory FunctionGroupElement, __c_FunctionGroupElement (line 3117)

    def __c_GlobalElement(__cexT):
        def __g_typeName(this):
            return (u"global")
        # end function __g_typeName (line 3148)

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(ClassGroupElement, 1, 
False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 3152)

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions (line 3157)

        def __g_classDefinitions(this):
            this.checkStruct()
            e = this.firstChild.nextSibling
            return e
        # end function __g_classDefinitions (line 3163)

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body (line 3169)

        def __g_parent(this):
            return None
        # end function __g_parent (line 3175)

        def __g_theGlobal(this):
            return this
        # end function __g_theGlobal (line 3179)

        def __g_theClass(this):
            return None
        # end function __g_theClass (line 3183)

        def __g_parentFunction(this):
            return None
        # end function __g_parentFunction (line 3187)

        def __g_allowThis(this):
            return False
        # end function __g_allowThis (line 3191)

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall (line 3195)

        def __m_allocFunctionId(this):
            __r0 = this
            __r1 = __cpm[__r0, "functionCounter"]
            __cpm[__r0, "functionCounter"] = __x_inc(__r1)
            return __r1
        # end function __m_allocFunctionId (line 3199)

        def __m_registerClassDefinition(this, tag, range = (None)):
            name = tag.name
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                raise ConflictError((u"Duplicate class definition: %s"), range, v.range, name)
            # end if (line 3209)
            this.setLocal(name, tag)
        # end function __m_registerClassDefinition (line 3206)

        def __m_declarePublic(this, name, range):
            ai = Identifier(name, range)
            if __x_cb(ai.isSpecial):
                raise CompileError((u"public name must be a valid Python identifier: %s"), range, name)
            # end if (line 3217)
            an = ArrayList(name)
            if __x_cb(__x_cb(__x_eq(an.get(0), (u"_"))) and an.get(1) == (u"_")):
                raise CompileError((u"public name starts with double underscore is reserved: %s"), range, name)
            # end if (line 3221)
            ov = __cpm[this, "exports"].get(name, False)
            if __x_cb(ov):
                raise ConflictError((u"Duplicate public variable declaration: %s"), range, ov.range, name)
            # end if (line 3225)
            __cpm[this, "exports"].set(name, True)
        # end function __m_declarePublic (line 3215)

        def __m_referVar(this, name, range = (None)):
            if __x_cb(__x_eq(name, (u"eval"))):
                raise CompileError((u"Eval is evil"), range)
            # end if (line 3232)
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if (line 3236)
            v2 = __cpm[this, "builtins"].get(name, None)
            if __x_cb(__x_ne(v2, None)):
                return v2
            # end if (line 3240)
            raise CompileError((u"%s is not defined"), range, name)
        # end function __m_referVar (line 3231)

        def __m_generatePython(this, gen):
            def __fE5_(v, n, a):
                exp.push(n)
            # end function <anonymous> (__fE5_) (line 3247)

            def __fE6_(v, k, a):
                if __x_cb(k > 0):
                    writer.write((u", "), (u"\\"))
                # end if (line 3252)
                writer.write((u"\"") + v + (u"\""), False)
            # end function <anonymous> (__fE6_) (line 3251)

            def __fE7_(v, k, a):
                if __x_cb(k > 0):
                    writer.write((u", "), (u"\\"))
                # end if (line 3259)
                writer.write(v, False)
            # end function <anonymous> (__fE7_) (line 3258)

            def __fE8_(v, n, s):
                if __x_cb(__x_not(v.closure)):
                    return
                # end if (line 3266)
                gen.writeln(v.toRawPython() + (u" = __x_var()"))
            # end function <anonymous> (__fE8_) (line 3265)

            def __fE9_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    __u_nwv.val = True
                    return False
                # end if (line 3273)
            # end function <anonymous> (__fE9_) (line 3272)

            def __fEA_(v, n, o):
                if __x_cb(__x_cb(__x_not(v.closure)) and __x_not(v.assigned)):
                    gen.writeln(v.toRawPython() + (u" = 0"))
                # end if (line 3280)
            # end function <anonymous> (__fEA_) (line 3279)

            __u_nwv = __x_var()
            gen.comment((u"-*- coding: utf-8 -*-"))
            gen.writeln((u"from __future__ import print_function, absolute_import, division, generators"))
            gen.blank()
            exp = ArrayList()
            __cpm[this, "exports"].forEach(__fE5_)
            writer = LineWriter()
            writer.write((u"__all__ = ("), False)
            if __x_cb(exp.length > 0):
                exp.forEach(__fE6_)
                if __x_cb(__x_eq(exp.length, 1)):
                    writer.write((u","), False)
                # end if (line 3295)
            # end if (line 3293)
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
 __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, \
__x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN"))
            gen.writeln((u"__x_imp = __x_imf(__name__)"))
            if __x_cb(exp.length > 0):
                writer = LineWriter()
                writer.write((u"global "), False)
                exp.forEach(__fE7_)
                writer.finalize(gen)
            # end if (line 3312)
            gen.blank()
            gen.comment((u"function definitions:"))
            this.functionDefinitions.generatePython(gen)
            gen.blank()
            gen.comment((u"class definitions:"))
            this.classDefinitions.generatePython(gen)
            this.forEachLocalVar(__fE8_)
            gen.blank()
            this.body.generatePython(gen)
            __u_nwv.val = False
            this.forEachLocalVar(__fE9_)
            if __x_cb(__u_nwv.val):
                gen.comment((u"Uninitialized variable:"))
                gen.writeln((u"return"))
                this.forEachLocalVar(__fEA_)
            # end if (line 3329)
            gen.TAB()
            gen.comment((u"program end"))
            gen.blank()
            gen.blank()
            gen.writeln((u"__()"))
        # end function __m_generatePython (line 3246)

        def __m_dump(this, ctx):
            ctx.attr((u"function-counter"), __cpm[this, "functionCounter"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 3341)

        def __m_setBuiltins(this, s, k, a):
            __cpm[this, "builtins"].set(s, BuiltinVar(s, this))
        # end function __m_setBuiltins (line 3346)

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
            # Uninitialized variable:
            return
            self = 0
        # end function __m_GlobalElement (line 3350)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3386)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "exports"] = StringMap()
            __cpm[this, "builtins"] = StringMap()
            __cpm[this, "functionCounter"] = 0
            this.enableImplicitBooleanConversion = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3392)

        __cpiT = __x_dpif("GlobalElement", {"__slots__": ("builtins", "exports", "functionCounter"), "setBuiltins": __x_smet(__m_setBuiltins)})
        __clsT = __x_dcls("GlobalElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("enableImplicitBooleanConversion",), 
"allocFunctionId": __m_allocFunctionId, "allowSuperCall": __x_prop(__g_allowSuperCall, None), "allowThis": __x_prop(__g_allowThis, None), 
"body": __x_prop(__g_body, None), "classDefinitions": __x_prop(__g_classDefinitions, None), "declarePublic": __m_declarePublic, 
"dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), "generatePython": __m_generatePython, 
"parent": __x_prop(__g_parent, None), "parentFunction": __x_prop(__g_parentFunction, None), "referVar": __m_referVar, 
"registerClassDefinition": __m_registerClassDefinition, "structList": __x_prop(__g_structList, None), 
"theClass": __x_prop(__g_theClass, None), "theGlobal": __x_prop(__g_theGlobal, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_GlobalElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory GlobalElement, __c_GlobalElement (line 3147)

    def __c_IfBlockElement(__cexT):
        def __g_typeName(this):
            return (u"ifgroup")
        # end function __g_typeName (line 3418)

        def __g_structList(this):
            return ArrayList([ElementPattern(IfElement, 1, False), ElementPattern(ElifElement, 0, True), ElementPattern(ElseElement, 
1, True)])
        # end function __g_structList (line 3422)

        def __m_simplifyExpressions(this):
            def __fEK_(e, k, self):
                e.checkStruct()
                if __x_cb(__x_eq(k, 0)):
                    return
                # end if (line 3430)
                if __x_cb(__u_mcei.val):
                    __u_if2.val.append(e)
                    return
                # end if (line 3433)
                if __x_cb(__x_iof(e, ElseElement)):
                    e.simplifyExpressions()
                    return
                # end if (line 3437)
                if __x_cb(__x_not(e.complex)):
                    e.simplifyExpressions()
                    return
                # end if (line 3441)
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
            # end function <anonymous> (__fEK_) (line 3428)

            __u_else2 = __x_var()
            __u_if2 = __x_var()
            __u_mcei = __x_var()
            if __x_cb(__cpm[this, "simplified"]):
                raise InternalError((u"simplify if again"))
            # end if (line 3461)
            __cpm[this, "simplified"] = True
            this.checkStruct()
            this.firstChild.simplifyExpressions()
            __u_mcei.val = False
            __u_if2.val = None
            __u_else2.val = None
            this.forEachChild(__fEK_)
            if __x_cb(__u_mcei.val):
                __u_else2.val.simplifyExpressions()
            # end if (line 3471)
            this.checkStruct()
        # end function __m_simplifyExpressions (line 3427)

        def __m_generatePython(this, gen):
            def __fEM_(e, k, t):
                e.generatePython(gen)
            # end function <anonymous> (__fEM_) (line 3478)

            sline = LineNumber()
            gen.logLineNumber(sline)
            this.forEachChild(__fEM_)
            gen.comment((u"end if (line %l)"), sline)
        # end function __m_generatePython (line 3477)

        def __m_IfBlockElement(this, range):
            __csu(this, range)
        # end function __m_IfBlockElement (line 3488)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3492)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "simplified"] = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3498)

        __cpiT = __x_dpif("IfBlockElement", {"__slots__": ("simplified",)})
        __clsT = __x_dcls("IfBlockElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_IfBlockElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory IfBlockElement, __c_IfBlockElement (line 3417)

    def __c_IfElement(__cexT):
        def __g_typeName(this):
            return (u"if")
        # end function __g_typeName (line 3516)

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 3520)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, IfBlockElement))):
                raise InternalError((u"malformed structure in IfElement (not in IfBlockElement)"))
            # end if (line 3525)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 3524)

        def __g_theStatement(this):
            return this.parent.theStatement
        # end function __g_theStatement (line 3531)

        def __g_complex(this):
            return this.firstChild.complex
        # end function __g_complex (line 3535)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            this.firstChild.checkStruct()
            cond = this.firstChild.firstChild
            body = this.lastChild
            cond.simplifyExpressions()
            body.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions (line 3539)

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
        # end function __m_generatePython (line 3549)

        def __m_IfElement(this, range):
            __csu(this, range)
        # end function __m_IfElement (line 3562)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3566)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3572)

        __clsT = __x_dcls("IfElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"complex": __x_prop(__g_complex, None), "generatePython": __m_generatePython, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "theStatement": __x_prop(__g_theStatement, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_IfElement})
        return __clsT
    # end class factory IfElement, __c_IfElement (line 3515)

    def __c_ImportElement(__cexT):
        def __g_typeName(this):
            return (u"import")
        # end function __g_typeName (line 3586)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, CallElement))):
                raise InternalError((u"malformed structure in ImportElement (not in CallElement)"))
            # end if (line 3591)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 3590)

        def __g_constantOnly(this):
            return False
        # end function __g_constantOnly (line 3597)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"__x_imp"), contchr)
        # end function __m_writePython (line 3601)

        def __m_ImportElement(this, range):
            __csu(this, range)
        # end function __m_ImportElement (line 3605)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3609)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3615)

        __clsT = __x_dcls("ImportElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"constantOnly": __x_prop(__g_constantOnly, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ImportElement})
        return __clsT
    # end class factory ImportElement, __c_ImportElement (line 3585)

    def __c_InstanceGroupElement(__cexT):
        def __g_typeName(this):
            return (u"instanceinit")
        # end function __g_typeName (line 3628)

        def __g_allowThis(this):
            return this.parent.allowThis
        # end function __g_allowThis (line 3632)

        def __g_allowSuper(this):
            return this.parent.allowSuper
        # end function __g_allowSuper (line 3636)

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall (line 3640)

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 3644)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, ClassElement))):
                raise InternalError((u"malformed structure in InstanceGroupElement (not in ClassElement)"))
            # end if (line 3649)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 3648)

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions (line 3655)

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body (line 3661)

        def __m_registerFunctionDefinition(this, tag, range = (None)):
            raise InternalError((u"register function definition in class property initializer"))
        # end function __m_registerFunctionDefinition (line 3667)

        def __m_registerLocalVar(this, name, range = (None)):
            raise InternalError((u"register local variable in class property initializer"))
            return None
        # end function __m_registerLocalVar (line 3671)

        def __m_referVar(this, name, range = (None)):
            return this.theClass.referVar(name, range)
        # end function __m_referVar (line 3676)

        def __m_generatePython(this, gen):
            def __fFQ_(p, k, s):
                if __x_cb(p.isPrivate):
                    __u_haspi.val = True
                    return False
                # end if (line 3682)
            # end function <anonymous> (__fFQ_) (line 3681)

            __u_haspi = __x_var()
            gen.blank()
            sline = LineNumber()
            gen.logLineNumber(sline)
            gen.writeln((u"def __csu(this, *argv):"))
            gen.tab()
            this.functionDefinitions.generatePython(gen)
            gen.blank()
            __u_haspi.val = False
            __cpm[this, "instanceMembers"].forEach(__fFQ_)
            if __x_cb(__u_haspi.val):
                gen.comment((u"create the private field"))
                gen.writeln((u"__cpm.create(this)"))
            # end if (line 3698)
            gen.comment((u"initialize properties"))
            this.body.generatePython(gen)
            gen.comment((u"super"))
            gen.writeln((u"super(__clsT, this).__init__(*argv)"))
            gen.TAB()
            gen.comment((u"end instance initializer and super constructor __csu (line %l)"), sline)
        # end function __m_generatePython (line 3680)

        def __m_dump(this, ctx):
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 3710)

        def __m_InstanceGroupElement(this, instanceMembers):
            __csu(this, None)
            __cpm[this, "instanceMembers"] = instanceMembers
            this.append(FunctionGroupElement())
            this.append(BodyElement(None))
        # end function __m_InstanceGroupElement (line 3714)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3721)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3727)

        __cpiT = __x_dpif("InstanceGroupElement", {"__slots__": ("instanceMembers",)})
        __clsT = __x_dcls("InstanceGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuper": __x_prop(__g_allowSuper, None), "allowSuperCall": __x_prop(__g_allowSuperCall, None), 
"allowThis": __x_prop(__g_allowThis, None), "body": __x_prop(__g_body, None), "checkStruct": __m_checkStruct, 
"dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), "generatePython": __m_generatePython, 
"referVar": __m_referVar, "registerFunctionDefinition": __m_registerFunctionDefinition, "registerLocalVar": __m_registerLocalVar, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_InstanceGroupElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory InstanceGroupElement, __c_InstanceGroupElement (line 3627)

    def __c_InstanceInitializerElement(__cexT):
        def __g_typeName(this):
            return (u"instanceprop")
        # end function __g_typeName (line 3747)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, True)])
        # end function __g_structList (line 3751)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.theFunction, InstanceGroupElement))):
                raise InternalError((u"malformed structure in InstanceInitializerElement (not in InstanceGroupElement)"))
            # end if (line 3756)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 3755)

        def __g_isInitializer(this):
            this.checkStruct()
            return __x_ne(this.firstChild, None)
        # end function __g_isInitializer (line 3762)

        def __m_declareVariable(this):
            this.checkStruct()
            this.theClass.registerProperty(__cpm[this, "attribute"].name, __cpm[this, "isPublic"], False, __cpm[this
, "attribute"].range)
        # end function __m_declareVariable (line 3767)

        def __m_simplifyExpressions(this):
            if __x_cb(this.isInitializer):
                aae = AssignElement(this.range)
                this.replaceWith(aae)
                attr = AttributeElement(__cpm[this, "attribute"], __cpm[this, "attribute"].range)
                aae.append(attr)
                attr.append(ThisElement(None))
                aae.append(this.firstChild)
            # end if (line 3774)
            this.remove()
        # end function __m_simplifyExpressions (line 3773)

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 3785)

        def __m_InstanceInitializerElement(this, attribute, isPublic, range):
            __csu(this, range)
            __cpm[this, "isPublic"] = isPublic
            __cpm[this, "attribute"] = attribute
        # end function __m_InstanceInitializerElement (line 3790)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3796)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3802)

        __cpiT = __x_dpif("InstanceInitializerElement", {"__slots__": ("attribute", "isPublic")})
        __clsT = __x_dcls("InstanceInitializerElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "declareVariable": __m_declareVariable, "dump": __m_dump, "isInitializer": __x_prop(__g_isInitializer, None), 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_InstanceInitializerElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory InstanceInitializerElement, __c_InstanceInitializerElement (line 3746)

    def __c_ItemElement(__cexT):
        def __g_typeName(this):
            return (u"item")
        # end function __g_typeName (line 3820)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList (line 3824)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(__x_not(this.complex)):
                return
            # end if (line 3830)
            left = this.firstChild
            right = this.lastChild
            atel = left.replaceWithTemp()
            this.insertTempAssign(atel)
            right.simplifyExpressions()
            this.checkStruct()
        # end function __m_simplifyExpressions (line 3828)

        def __m_extractLeft(this):
            this.checkStruct()
            left = this.firstChild
            right = this.lastChild
            atel = left.replaceWithTemp()
            this.insertTempAssign(atel)
            ater = right.replaceWithTemp()
            this.insertTempAssign(ater)
            this.checkStruct()
        # end function __m_extractLeft (line 3841)

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
        # end function __m_extractLeftAndDuplicate (line 3852)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            object = this.firstChild
            index = this.lastChild
            object.writePython(writer, (u"\\"), 12)
            writer.write((u"["), False)
            index.writePython(writer, (u"\\"), 0)
            writer.write((u"]"), contchr)
        # end function __m_writePython (line 3868)

        def __m_ItemElement(this, range):
            __csu(this, range)
        # end function __m_ItemElement (line 3877)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3881)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3887)

        __clsT = __x_dcls("ItemElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "extractLeft": __m_extractLeft, 
"extractLeftAndDuplicate": __m_extractLeftAndDuplicate, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ItemElement})
        return __clsT
    # end class factory ItemElement, __c_ItemElement (line 3819)

    def __c_KeyValueElement(__cexT):
        def __g_typeName(this):
            return (u"kvpair")
        # end function __g_typeName (line 3901)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 2, False)])
        # end function __g_structList (line 3905)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, ObjectLiteralElement))):
                raise InternalError((u"malformed structure in KeyValueElement (not in ObjectLiteralElement)"))
            # end if (line 3910)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 3909)

        def __m_simplifyExpressions(this):
            raise InternalError((u"called simplifyExpressions of KeyValueElement"))
        # end function __m_simplifyExpressions (line 3916)

        def __m_replaceWithTemp(this, optional = (True)):
            raise InternalError((u"called replaceWithTemp of KeyValueElement"))
        # end function __m_replaceWithTemp (line 3920)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            key = this.firstChild
            value = this.lastChild
            key.writePython(writer, False, 11)
            writer.write((u": "), (u""))
            value.writePython(writer, False, 11)
        # end function __m_writePython (line 3924)

        def __m_KeyValueElement(this, range):
            __csu(this, range)
        # end function __m_KeyValueElement (line 3932)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3936)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 3942)

        __clsT = __x_dcls("KeyValueElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "replaceWithTemp": __m_replaceWithTemp, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_KeyValueElement})
        return __clsT
    # end class factory KeyValueElement, __c_KeyValueElement (line 3900)

    def __c_MagicCallElement(__cexT):
        def __g_typeName(this):
            return (u"magiccall")
        # end function __g_typeName (line 3956)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False), ElementPattern(ArgumentElement, 1, False)])
        # end function __g_structList (line 3960)

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
        # end function __m_functionalize (line 3964)

        def __m_dump(this, ctx):
            ctx.attr((u"name"), __cpm[this, "name"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 3977)

        def __m_MagicCallElement(this, name, range):
            __csu(this, range)
            allowFns = StringMap()
            allowFns.sets([(u"apply"), (u"bind"), (u"drop"), (u"every"), (u"filter"), (u"find"), (u"findIndex"), 
(u"flatMap"), (u"forEach"), (u"isEmpty"), (u"join"), (u"length"), (u"map"), (u"pop"), (u"push"), (u"reduce"), 
(u"shift"), (u"slice"), (u"some"), (u"splice"), (u"take"), (u"unshift")], True)
            if __x_cb(__x_not(allowFns.has(name))):
                raise CompileError((u"@%s is not a valid magic method"), range, name)
            # end if (line 3988)
            __cpm[this, "name"] = name
        # end function __m_MagicCallElement (line 3982)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 3994)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4000)

        __cpiT = __x_dpif("MagicCallElement", {"__slots__": ("name",)})
        __clsT = __x_dcls("MagicCallElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"dump": __m_dump, "functionalize": __m_functionalize, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_MagicCallElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory MagicCallElement, __c_MagicCallElement (line 3955)

    def __c_MethodElement(__cexT):
        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(MethodParameterGroupElement, 
1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 4017)

        def __g_allowThis(this):
            tag = this.tag
            return __x_cb(this.parent.allowThis) and __x_not(tag.isStatic)
        # end function __g_allowThis (line 4022)

        def __g_allowSuper(this):
            tag = this.tag
            return __x_cb(this.parent.allowSuper) and __x_not(tag.isStatic)
        # end function __g_allowSuper (line 4027)

        def __g_allowSuperCall(this):
            tag = this.tag
            return __x_cb(this.isConstructor) and this.parent.allowSuperCall
        # end function __g_allowSuperCall (line 4032)

        def __g_isConstructor(this):
            tag = this.tag
            return __x_cb(__x_not(tag.isStatic)) and __x_eq(tag.name, this.theClass.tag.name)
        # end function __g_isConstructor (line 4037)

        def __m_declareVariable(this):
            tag = this.tag
            if __x_cb(this.isConstructor):
                if __x_cb(__x_not(tag.isPublic)):
                    raise CompileError((u"Class constructor may not be a private method"))
                # end if (line 4045)
                if __x_cb(tag.isAccessor):
                    raise CompileError((u"Class constructor may not be an accessor"))
                # end if (line 4048)
            else:
                this.parentFunction.registerFunctionDefinition(this.tag, this.tag.range)
            # end if (line 4044)
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable (line 4042)

        def __m_meetSuper(this, range):
            if __x_cb(__x_not(this.allowSuperCall)):
                return
            # end if (line 4058)
            if __x_cb(__cpm[this, "smet"]):
                raise CompileError((u"Super constructor may only be called once"), range)
            # end if (line 4061)
            __cpm[this, "smet"] = True
        # end function __m_meetSuper (line 4057)

        def __m_meetReturnOrThis(this, range):
            if __x_cb(__x_not(this.allowSuperCall)):
                return
            # end if (line 4068)
            if __x_cb(__x_not(__cpm[this, "smet"])):
                raise CompileError((u"Super statement cannot occur after a this, super or return statement"), range)
            # end if (line 4071)
        # end function __m_meetReturnOrThis (line 4067)

        def __m_checkVariables(this):
            (super(__clsT, this)).checkVariables()
            if __x_cb(__x_cb(__x_not(__cpm[this, "smet"])) and this.allowSuperCall):
                raise CompileError((u"Must call super constructor in derived class before returning from derived constructor"), 
this.range)
            # end if (line 4078)
        # end function __m_checkVariables (line 4076)

        def __m_referVar(this, name, range = (None)):
            v = this.getLocal(name)
            if __x_cb(__x_ne(v, None)):
                return v
            # end if (line 4086)
            if __x_cb(__x_cb(__x_ne(this.tag.name, None)) and __x_eq(this.tag.name, name)):
                if __x_cb(__x_not(this.isConstructor)):
                    raise CompileError((u"'this' is required for referring the method itself"), range)
                # end if (line 4090)
            # end if (line 4089)
            return this.parentFunction.referVar(name, range)
        # end function __m_referVar (line 4084)

        def __m_functionalize(this):
            if __x_cb(__x_cb(this.isConstructor) and __x_not(this.allowSuperCall)):
                expr = ExpressionStatementElement(None)
                this.body.prepend(expr)
                ce = CallElement(None)
                expr.append(ce)
                ce.append(SuperElement(None))
                ce.append(ArgumentElement(None))
            # end if (line 4098)
            (super(__clsT, this)).functionalize()
        # end function __m_functionalize (line 4097)

        def __m_MethodElement(this, name, methodType, isStatic, isPublic, tagRange, range):
            __csu(this, range)
            tag = MethodTag(name, methodType, isStatic, isPublic, this, tagRange)
            this.tag = tag
            this.append(FunctionGroupElement())
            this.append(MethodParameterGroupElement(tag))
            this.append(BodyElement(None))
        # end function __m_MethodElement (line 4109)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4118)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "smet"] = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4124)

        __cpiT = __x_dpif("MethodElement", {"__slots__": ("smet",)})
        __clsT = __x_dcls("MethodElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "allowSuper": __x_prop(__g_allowSuper, None), 
"allowSuperCall": __x_prop(__g_allowSuperCall, None), "allowThis": __x_prop(__g_allowThis, None), "checkVariables": __m_checkVariables, 
"declareVariable": __m_declareVariable, "functionalize": __m_functionalize, "isConstructor": __x_prop(__g_isConstructor, None), 
"meetReturnOrThis": __m_meetReturnOrThis, "meetSuper": __m_meetSuper, "referVar": __m_referVar, "structList": __x_prop(__g_structList, None), 
"__init__": __m_MethodElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory MethodElement, __c_MethodElement (line 4016)

    def __c_MethodGroupElement(__cexT):
        def __g_typeName(this):
            return (u"methods")
        # end function __g_typeName (line 4144)

        def __g_allowSuperCall(this):
            return this.parent.allowSuperCall
        # end function __g_allowSuperCall (line 4148)

        def __g_structList(this):
            return ArrayList([ElementPattern(MethodElement, 0, True)])
        # end function __g_structList (line 4152)

        def __m_MethodGroupElement(this):
            __csu(this)
        # end function __m_MethodGroupElement (line 4156)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4160)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4166)

        __clsT = __x_dcls("MethodGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuperCall": __x_prop(__g_allowSuperCall, None), "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_MethodGroupElement})
        return __clsT
    # end class factory MethodGroupElement, __c_MethodGroupElement (line 4143)

    def __c_ParameterGroupElement(__cexT):
        def __g_typeName(this):
            return (u"params")
        # end function __g_typeName (line 4179)

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 0, True), ElementPattern(ParameterAssignElement, 0, 
True), ElementPattern(RestParameterElement, 0, True)])
        # end function __g_structList (line 4183)

        def __m_generatePython(this, ctx):
            def __fI0_(e, k, s):
                e.generateRenameAssignment(ctx)
            # end function <anonymous> (__fI0_) (line 4189)

            this.checkStruct()
            this.forEachChild(__fI0_)
        # end function __m_generatePython (line 4188)

        def __m_toPrameterList(this, writer, contchr, parentType = (0)):
            def __fI2_(e, k, s):
                if __x_cb(__u_o.val):
                    writer.write((u", "), (u""))
                # end if (line 4199)
                e.writePython(writer, (u""))
                __u_o.val = True
            # end function <anonymous> (__fI2_) (line 4198)

            __u_o = __x_var()
            __u_o.val = False
            this.forEachChild(__fI2_)
        # end function __m_toPrameterList (line 4197)

        def __m_ParameterGroupElement(this):
            __csu(this, None)
        # end function __m_ParameterGroupElement (line 4211)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4215)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4221)

        __clsT = __x_dcls("ParameterGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "toPrameterList": __m_toPrameterList, 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_ParameterGroupElement})
        return __clsT
    # end class factory ParameterGroupElement, __c_ParameterGroupElement (line 4178)

    def __c_MethodParameterGroupElement(__cexT):
        def __m_declareVariable(this):
            def __fI8_(p, k, s):
                __r0 = __u_pcnt.val
                __u_pcnt.val = __x_inc(__r0)
            # end function <anonymous> (__fI8_) (line 4235)

            __u_pcnt = __x_var()
            tag = __cpm[this, "tag"]
            __u_pcnt.val = 0
            this.forEachChild(__fI8_)
            if __x_cb(__x_cb(tag.isSetter) and __x_ne(__u_pcnt.val, 1)):
                raise CompileError((u"Setter must have exactly one formal parameter"), this.range)
            # end if (line 4244)
            if __x_cb(__x_cb(__x_cb(tag.isAccessor) and __x_not(tag.isSetter)) and __x_ne(__u_pcnt.val, 0)):
                raise CompileError((u"Getter must not have any formal parameters"), this.range)
            # end if (line 4247)
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable (line 4234)

        def __m_toPrameterList(this, writer, contchr, parentType = (0)):
            def __fIA_(e, k, s):
                writer.write((u", "), (u""))
                e.writePython(writer, (u""))
            # end function <anonymous> (__fIA_) (line 4254)

            writer.write((u"this"), (u""))
            this.forEachChild(__fIA_)
        # end function __m_toPrameterList (line 4253)

        def __m_MethodParameterGroupElement(this, tag):
            __csu(this)
            __cpm[this, "tag"] = tag
        # end function __m_MethodParameterGroupElement (line 4263)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4268)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4274)

        __cpiT = __x_dpif("MethodParameterGroupElement", {"__slots__": ("tag",)})
        __clsT = __x_dcls("MethodParameterGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "declareVariable": __m_declareVariable, "toPrameterList": __m_toPrameterList, "__init__": __m_MethodParameterGroupElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory MethodParameterGroupElement, __c_MethodParameterGroupElement (line 4233)

    def __c_NotOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"not")
        # end function __g_typeName (line 4290)

        def __g_constantOnly(this):
            return this.firstChild.constantOnly
        # end function __g_constantOnly (line 4294)

        def __g_tempVarOnly(this):
            return this.firstChild.tempVarOnly
        # end function __g_tempVarOnly (line 4298)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 4302)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = parentType >= 2
            dst = this.firstChild
            if __x_cb(p):
                writer.write((u"("), False)
            # end if (line 4309)
            writer.write((u"not "), (u"") if __x_cb(p) else contchr)
            dst.writePython(writer, (u"") if __x_cb(p) else contchr, 4)
            if __x_cb(p):
                writer.write((u")"), contchr)
            # end if (line 4314)
        # end function __m_writePython (line 4306)

        def __m_NotOperatorElement(this, range):
            __csu(this, range)
        # end function __m_NotOperatorElement (line 4319)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4323)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4329)

        __clsT = __x_dcls("NotOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NotOperatorElement})
        return __clsT
    # end class factory NotOperatorElement, __c_NotOperatorElement (line 4289)

    def __c_NullLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"null")
        # end function __g_typeName (line 4342)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"None"), contchr)
        # end function __m_writePython (line 4346)

        def __m_NullLiteralElement(this, range):
            __csu(this, range)
        # end function __m_NullLiteralElement (line 4350)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4354)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4360)

        __clsT = __x_dcls("NullLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NullLiteralElement})
        return __clsT
    # end class factory NullLiteralElement, __c_NullLiteralElement (line 4341)

    def __c_NullishCheckElement(__cexT):
        def __g_typeName(this):
            return (u"isnullish")
        # end function __g_typeName (line 4372)

        def __g_constantOnly(this):
            return this.firstChild.constantOnly
        # end function __g_constantOnly (line 4376)

        def __g_tempVarOnly(this):
            return this.firstChild.tempVarOnly
        # end function __g_tempVarOnly (line 4380)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 4384)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = parentType >= 3
            dst = this.firstChild
            if __x_cb(p):
                writer.write((u"("), False)
            # end if (line 4391)
            writer.write((u"None is "), (u"") if __x_cb(p) else contchr)
            dst.writePython(writer, (u"") if __x_cb(p) else contchr, 4)
            if __x_cb(p):
                writer.write((u")"), contchr)
            # end if (line 4396)
        # end function __m_writePython (line 4388)

        def __m_NullishCheckElement(this, range):
            __csu(this, range)
        # end function __m_NullishCheckElement (line 4401)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4405)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4411)

        __clsT = __x_dcls("NullishCheckElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NullishCheckElement})
        return __clsT
    # end class factory NullishCheckElement, __c_NullishCheckElement (line 4371)

    def __c_NumberLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"real")
        # end function __g_typeName (line 4424)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(parentType >= 12):
                writer.write((u"("), False)
            # end if (line 4429)
            writer.write(__cpm[this, "source"], False)
            if __x_cb(parentType >= 12):
                writer.write((u")"), False)
            # end if (line 4433)
        # end function __m_writePython (line 4428)

        def __m_dump(this, ctx):
            ctx.attr((u"source"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 4438)

        def __m_NumberLiteralElement(this, value, source, range):
            __csu(this, range)
            __cpm[this, "value"] = value
            __cpm[this, "source"] = source
        # end function __m_NumberLiteralElement (line 4443)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4449)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4455)

        __cpiT = __x_dpif("NumberLiteralElement", {"__slots__": ("source", "value")})
        __clsT = __x_dcls("NumberLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_NumberLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory NumberLiteralElement, __c_NumberLiteralElement (line 4423)

    def __c_ObjectLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"object")
        # end function __g_typeName (line 4471)

        def __g_structList(this):
            return ArrayList([ElementPattern(KeyValueElement, 0, True)])
        # end function __g_structList (line 4475)

        def __m_simplifyExpressions(this):
            def __fJH_(m, k, s):
                if __x_cb(m.complex):
                    __u_lc.val = k
                # end if (line 4481)
            # end function <anonymous> (__fJH_) (line 4480)

            def __fJI_(m, k, s):
                if __x_cb(k > __u_lc.val):
                    return False
                # end if (line 4487)
                m.checkStruct()
                key = m.firstChild
                value = m.lastChild
                ate = key.replaceWithTemp()
                this.insertTempAssign(ate)
                tas = value.replaceWithTemp()
                this.insertTempAssign(tas)
            # end function <anonymous> (__fJI_) (line 4486)

            __u_lc = __x_var()
            this.checkStruct()
            __u_lc.val = -1
            this.forEachChild(__fJH_)
            this.forEachChild(__fJI_)
            this.checkStruct()
        # end function __m_simplifyExpressions (line 4479)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            def __fJK_(m, k, s):
                if __x_cb(k > 0):
                    writer.write((u", "), (u""))
                # end if (line 4509)
                m.writePython(writer, False)
            # end function <anonymous> (__fJK_) (line 4508)

            writer.write((u"({"), (u""))
            this.forEachChild(__fJK_)
            writer.write((u"})"), contchr)
        # end function __m_writePython (line 4507)

        def __m_ObjectLiteralElement(this, range):
            __csu(this, range)
        # end function __m_ObjectLiteralElement (line 4520)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4524)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4530)

        __clsT = __x_dcls("ObjectLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_ObjectLiteralElement})
        return __clsT
    # end class factory ObjectLiteralElement, __c_ObjectLiteralElement (line 4470)

    def __c_ParameterAssignElement(__cexT):
        def __g_typeName(this):
            return (u"optparam")
        # end function __g_typeName (line 4543)

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 1, False), ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 4547)

        def __m_checkVariables(this):
            p = this.firstChild
            v = this.lastChild
            p.checkVariables()
            v.checkVariables()
            if __x_cb(__x_cb(v.complex) or __x_not(v.constantOnly)):
                raise CompileError((u"Default parameter must be constant"), v.range)
            # end if (line 4556)
        # end function __m_checkVariables (line 4551)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = this.firstChild
            v = this.lastChild
            p.writePython(writer, False)
            writer.write((u" = "), (u""))
            writer.write((u"("), False)
            v.writePython(writer, (u""))
            writer.write((u")"), False)
        # end function __m_writePython (line 4561)

        def __m_generateRenameAssignment(this, ctx):
            p = this.firstChild
            p.generateRenameAssignment(ctx)
        # end function __m_generateRenameAssignment (line 4571)

        def __m_ParameterAssignElement(this, range):
            __csu(this, range)
        # end function __m_ParameterAssignElement (line 4576)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4580)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4586)

        __clsT = __x_dcls("ParameterAssignElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkVariables": __m_checkVariables, "generateRenameAssignment": __m_generateRenameAssignment, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_ParameterAssignElement})
        return __clsT
    # end class factory ParameterAssignElement, __c_ParameterAssignElement (line 4542)

    def __c_ParameterElement(__cexT):
        def __g_typeName(this):
            return (u"param")
        # end function __g_typeName (line 4599)

        def __m_declareVariable(this):
            __cpm[this, "target"] = this.theFunction.registerLocalVar(__cpm[this, "source"], this.range)
        # end function __m_declareVariable (line 4603)

        def __m_checkVariables(this):
            __cpm[this, "target"].write(this.theFunction, this.range)
        # end function __m_checkVariables (line 4607)

        def __m_simplifyExpressions(this):
            pass
        # end function __m_simplifyExpressions (line 4611)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write(__cpm[this, "target"].toOriginPython(), False)
        # end function __m_writePython (line 4615)

        def __m_generateRenameAssignment(this, ctx):
            if __x_cb(__x_not(__cpm[this, "target"].closure)):
                return
            # end if (line 4620)
            writer = LineWriter()
            writer.write(__cpm[this, "target"].toPython(), False)
            writer.write((u" = "), False)
            writer.write(__cpm[this, "target"].toOriginPython(), False)
            writer.finalize(ctx)
        # end function __m_generateRenameAssignment (line 4619)

        def __m_dump(this, ctx):
            ctx.attr((u"name"), __cpm[this, "source"])
            ctx.attr((u"var"), __cpm[this, "target"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 4630)

        def __m_ParameterElement(this, source, range):
            __csu(this, range)
            __cpm[this, "source"] = source
        # end function __m_ParameterElement (line 4636)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4641)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "target"] = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4647)

        __cpiT = __x_dpif("ParameterElement", {"__slots__": ("source", "target")})
        __clsT = __x_dcls("ParameterElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkVariables": __m_checkVariables, "declareVariable": __m_declareVariable, "dump": __m_dump, "generateRenameAssignment": __m_generateRenameAssignment, 
"simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_ParameterElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory ParameterElement, __c_ParameterElement (line 4598)

    def __c_RestParameterElement(__cexT):
        def __g_typeName(this):
            return (u"rest")
        # end function __g_typeName (line 4666)

        def __g_structList(this):
            return ArrayList([ElementPattern(ParameterElement, 1, False)])
        # end function __g_structList (line 4670)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            p = this.firstChild
            writer.write((u"*"), False)
            p.writePython(writer, False)
        # end function __m_writePython (line 4674)

        def __m_generateRenameAssignment(this, ctx):
            this.checkStruct()
            p = this.firstChild
            p.generateRenameAssignment(ctx)
        # end function __m_generateRenameAssignment (line 4680)

        def __m_RestParameterElement(this, range):
            __csu(this, range)
        # end function __m_RestParameterElement (line 4686)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4690)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4696)

        __clsT = __x_dcls("RestParameterElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "generateRenameAssignment": __m_generateRenameAssignment, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_RestParameterElement})
        return __clsT
    # end class factory RestParameterElement, __c_RestParameterElement (line 4665)

    def __c_ReturnElement(__cexT):
        def __g_typeName(this):
            return (u"return")
        # end function __g_typeName (line 4709)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, True)])
        # end function __g_structList (line 4713)

        def __m_checkVariables(this):
            fn = this.theFunction
            if __x_cb(__x_iof(fn, MethodElement)):
                fn.meetReturnOrThis(this.range)
            # end if (line 4719)
            (super(__clsT, this)).checkVariables()
        # end function __m_checkVariables (line 4717)

        def __m_generatePython(this, ctx):
            right = this.lastChild
            if __x_cb(__x_eq(right, None)):
                ctx.writeln((u"return"))
                return
            # end if (line 4727)
            writer = LineWriter()
            writer.write((u"return "), False)
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython (line 4725)

        def __m_ReturnElement(this, range):
            __csu(this, range)
        # end function __m_ReturnElement (line 4737)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4741)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4747)

        __clsT = __x_dcls("ReturnElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_ReturnElement})
        return __clsT
    # end class factory ReturnElement, __c_ReturnElement (line 4708)

    def __c_SpreadElement(__cexT):
        def __g_typeName(this):
            return (u"spread")
        # end function __g_typeName (line 4760)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 4764)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, SequenceElement))):
                raise InternalError((u"malformed structure in spread (not in sequence)"))
            # end if (line 4769)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 4768)

        def __m_simplifyExpressions(this):
            raise InternalError((u"called simplifyExpressions of SpreadElement"))
        # end function __m_simplifyExpressions (line 4775)

        def __m_replaceWithTemp(this, optional = (True)):
            raise InternalError((u"called replaceWithTemp of SpreadElement"))
        # end function __m_replaceWithTemp (line 4779)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            value = this.lastChild
            writer.write((u"*"), (u""))
            value.writePython(writer, False, 11)
        # end function __m_writePython (line 4783)

        def __m_SpreadElement(this, range):
            __csu(this, range)
        # end function __m_SpreadElement (line 4789)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4793)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4799)

        __clsT = __x_dcls("SpreadElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"replaceWithTemp": __m_replaceWithTemp, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_SpreadElement})
        return __clsT
    # end class factory SpreadElement, __c_SpreadElement (line 4759)

    def __c_StaticGroupElement(__cexT):
        def __g_typeName(this):
            return (u"staticinit")
        # end function __g_typeName (line 4812)

        def __g_allowThis(this):
            return False
        # end function __g_allowThis (line 4816)

        def __g_allowSuper(this):
            return False
        # end function __g_allowSuper (line 4820)

        def __g_allowSuperCall(this):
            return False
        # end function __g_allowSuperCall (line 4824)

        def __g_structList(this):
            return ArrayList([ElementPattern(FunctionGroupElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 4828)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, ClassElement))):
                raise InternalError((u"malformed structure in StaticGroupElement (not in ClassElement)"))
            # end if (line 4833)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 4832)

        def __g_functionDefinitions(this):
            this.checkStruct()
            e = this.firstChild
            return e
        # end function __g_functionDefinitions (line 4839)

        def __g_body(this):
            this.checkStruct()
            e = this.lastChild
            return e
        # end function __g_body (line 4845)

        def __m_registerFunctionDefinition(this, tag, range = (None)):
            raise InternalError((u"register function definition in class property initializer"))
        # end function __m_registerFunctionDefinition (line 4851)

        def __m_registerLocalVar(this, name, range = (None)):
            raise InternalError((u"register local variable in class property initializer"))
            return None
        # end function __m_registerLocalVar (line 4855)

        def __m_referVar(this, name, range = (None)):
            if __x_cb(__x_eq(this.theClass.tag.name, name)):
                raise CompileError((u"cannot access the class name %s in the static property initializer"), range, name)
            # end if (line 4861)
            return this.theClass.referVar(name, range)
        # end function __m_referVar (line 4860)

        def __m_generatePython(this, gen):
            gen.blank()
            sline = LineNumber()
            gen.logLineNumber(sline)
            gen.writeln((u"def __csi(this):"))
            gen.tab()
            this.functionDefinitions.generatePython(gen)
            gen.blank()
            gen.comment((u"super"))
            gen.writeln((u"__x_objT.__init__(this)"))
            gen.comment((u"initialize properties"))
            this.body.generatePython(gen)
            gen.TAB()
            gen.comment((u"end static initializer __csi (line %l)"), sline)
        # end function __m_generatePython (line 4867)

        def __m_dump(this, ctx):
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 4883)

        def __m_StaticGroupElement(this):
            __csu(this, None)
            this.append(FunctionGroupElement())
            this.append(BodyElement(None))
        # end function __m_StaticGroupElement (line 4887)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4893)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4899)

        __clsT = __x_dcls("StaticGroupElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "allowSuper": __x_prop(__g_allowSuper, None), "allowSuperCall": __x_prop(__g_allowSuperCall, None), 
"allowThis": __x_prop(__g_allowThis, None), "body": __x_prop(__g_body, None), "checkStruct": __m_checkStruct, 
"dump": __m_dump, "functionDefinitions": __x_prop(__g_functionDefinitions, None), "generatePython": __m_generatePython, 
"referVar": __m_referVar, "registerFunctionDefinition": __m_registerFunctionDefinition, "registerLocalVar": __m_registerLocalVar, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_StaticGroupElement})
        return __clsT
    # end class factory StaticGroupElement, __c_StaticGroupElement (line 4811)

    def __c_StaticInitializerElement(__cexT):
        def __g_typeName(this):
            return (u"staticprop")
        # end function __g_typeName (line 4915)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, True)])
        # end function __g_structList (line 4919)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.theFunction, StaticGroupElement))):
                raise InternalError((u"malformed structure in StaticInitializerElement (not in StaticGroupElement)"))
            # end if (line 4924)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 4923)

        def __g_isInitializer(this):
            this.checkStruct()
            return __x_ne(this.firstChild, None)
        # end function __g_isInitializer (line 4930)

        def __m_declareVariable(this):
            this.checkStruct()
            this.theClass.registerProperty(__cpm[this, "attribute"].name, __cpm[this, "isPublic"], True, __cpm[this
, "attribute"].range)
        # end function __m_declareVariable (line 4935)

        def __m_simplifyExpressions(this):
            (super(__clsT, this)).simplifyExpressions()
            if __x_cb(__x_not(this.isInitializer)):
                this.remove()
            # end if (line 4943)
        # end function __m_simplifyExpressions (line 4941)

        def __m_generatePython(this, ctx):
            writer = LineWriter()
            right = this.lastChild
            writer.write((u"this") if __x_cb(__cpm[this, "isPublic"]) else (u"__csp"), False)
            writer.write((u"."), False)
            writer.write(__cpm[this, "attribute"].toPython(), False)
            writer.write((u" = "), (u"\\"))
            right.writePython(writer, False)
            writer.finalize(ctx)
        # end function __m_generatePython (line 4948)

        def __m_dump(this, ctx):
            ctx.attr((u"attribute"), __cpm[this, "attribute"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 4959)

        def __m_StaticInitializerElement(this, attribute, isPublic, range):
            __csu(this, range)
            __cpm[this, "isPublic"] = isPublic
            __cpm[this, "attribute"] = attribute
        # end function __m_StaticInitializerElement (line 4964)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 4970)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 4976)

        __cpiT = __x_dpif("StaticInitializerElement", {"__slots__": ("attribute", "isPublic")})
        __clsT = __x_dcls("StaticInitializerElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "declareVariable": __m_declareVariable, "dump": __m_dump, "generatePython": __m_generatePython, 
"isInitializer": __x_prop(__g_isInitializer, None), "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_StaticInitializerElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory StaticInitializerElement, __c_StaticInitializerElement (line 4914)

    def __c_StringLiteralElement(__cexT):
        def __g_typeName(this):
            return (u"string")
        # end function __g_typeName (line 4994)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            def __fM6_(c, k, a):
                cp = StrTool.codePointAt(c)
                br = False
                if __x_cb(__x_eq(cp, 10)):
                    __u_cs.val = __u_cs.val + (u"\\n")
                    __u_cl.val = __u_cl.val + 2
                    if __x_cb(__x_cb(l > 80) and __u_cl.val >= 50):
                        br = True
                    # end if (line 5005)
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
                # end if (line 5002)
                if __x_cb(__x_cb(br) or __u_cl.val >= 100):
                    writer.write(__u_cs.val + (u"\\"), True)
                    __u_cl.val = 0
                    __u_cs.val = (u"")
                # end if (line 5036)
                br = False
            # end function <anonymous> (__fM6_) (line 4999)

            __u_cl = __x_var()
            __u_cs = __x_var()
            v = ArrayList(__cpm[this, "value"])
            l = v.length
            __u_cl.val = 0
            __u_cs.val = (u"")
            writer.write((u"(u\""))
            v.forEach(__fM6_)
            if __x_cb(__u_cl.val > 0):
                writer.write(__u_cs.val, False)
            # end if (line 5052)
            writer.write((u"\")"), contchr)
        # end function __m_writePython (line 4998)

        def __m_dump(this, ctx):
            ctx.attr((u"source"), __cpm[this, "value"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 5058)

        def __m_StringLiteralElement(this, value, source, range):
            __csu(this, range)
            __cpm[this, "value"] = value
            __cpm[this, "source"] = source
        # end function __m_StringLiteralElement (line 5063)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5069)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5075)

        __cpiT = __x_dpif("StringLiteralElement", {"__slots__": ("source", "value")})
        __clsT = __x_dcls("StringLiteralElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "dump": __m_dump, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_StringLiteralElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory StringLiteralElement, __c_StringLiteralElement (line 4993)

    def __c_SuperElement(__cexT):
        def __g_typeName(this):
            return (u"super")
        # end function __g_typeName (line 5091)

        def __g_constantOnly(this):
            return False
        # end function __g_constantOnly (line 5095)

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly (line 5099)

        def __m_checkVariables(this):
            this.checkStruct()
            if __x_cb(__x_not(this.allowSuper)):
                raise CompileError((u"'super' keyword unexpected here"), this.range)
            # end if (line 5105)
            fn = this.theFunction
            if __x_cb(__x_iof(fn, MethodElement)):
                fn.meetReturnOrThis(this.range)
            # end if (line 5109)
        # end function __m_checkVariables (line 5103)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(__x_iof(this.parent, CallElement)):
                raise InternalError((u"cannot generate the code for super()"))
            # end if (line 5115)
            writer.write((u"(super(__clsT, this))"), contchr)
        # end function __m_writePython (line 5114)

        def __m_SuperElement(this, range):
            __csu(this, range)
        # end function __m_SuperElement (line 5121)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5125)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5131)

        __clsT = __x_dcls("SuperElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"constantOnly": __x_prop(__g_constantOnly, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_SuperElement})
        return __clsT
    # end class factory SuperElement, __c_SuperElement (line 5090)

    def __c_TernaryOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"ternary")
        # end function __g_typeName (line 5144)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 3, False)])
        # end function __g_structList (line 5148)

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            cond = this.firstChild
            cc = CallElement.callGlobal((u"__x_tob") if __x_cb(this.theGlobal.enableImplicitBooleanConversion) else (u"__x_cb"), 
cond)
            this.prepend(cc)
            this.checkStruct()
        # end function __m_functionalize (line 5152)

        def __m_simplifyExpressions(this):
            this.checkStruct()
            if __x_cb(__x_not(this.complex)):
                return
            # end if (line 5164)
            cond = this.firstChild
            __v_exec = cond.nextSibling
            altn = __v_exec.nextSibling
            if __x_cb(__x_not(__x_cb(__v_exec.complex) or altn.complex)):
                cond.simplifyExpressions()
                return
            # end if (line 5170)
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
        # end function __m_simplifyExpressions (line 5162)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            cond = this.firstChild
            __v_exec = cond.nextSibling
            altn = __v_exec.nextSibling
            p = parentType >= 1
            if __x_cb(p):
                writer.write((u"("), False)
            # end if (line 5201)
            __v_exec.writePython(writer, (u"") if __x_cb(p) else contchr, 2)
            writer.write((u" if "), (u"") if __x_cb(p) else contchr)
            cond.writePython(writer, (u"") if __x_cb(p) else contchr, 2)
            writer.write((u" else "), (u"") if __x_cb(p) else contchr)
            altn.writePython(writer, (u"") if __x_cb(p) else contchr, 2)
            if __x_cb(p):
                writer.write((u")"), contchr)
            # end if (line 5209)
        # end function __m_writePython (line 5196)

        def __m_TernaryOperatorElement(this, range):
            __csu(this, range)
        # end function __m_TernaryOperatorElement (line 5214)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5218)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5224)

        __clsT = __x_dcls("TernaryOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "functionalize": __m_functionalize, "simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, "__init__": __m_TernaryOperatorElement})
        return __clsT
    # end class factory TernaryOperatorElement, __c_TernaryOperatorElement (line 5143)

    def __c_ThisElement(__cexT):
        def __g_typeName(this):
            return (u"this")
        # end function __g_typeName (line 5237)

        def __g_constantOnly(this):
            return True
        # end function __g_constantOnly (line 5241)

        def __g_tempVarOnly(this):
            return True
        # end function __g_tempVarOnly (line 5245)

        def __m_checkVariables(this):
            this.checkStruct()
            if __x_cb(__x_not(this.allowThis)):
                raise CompileError((u"'this' expression must be used inside class instance methods"), this.range)
            # end if (line 5251)
            fn = this.theFunction
            if __x_cb(__x_iof(fn, MethodElement)):
                fn.meetReturnOrThis(this.range)
            # end if (line 5255)
        # end function __m_checkVariables (line 5249)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write((u"this"), contchr)
        # end function __m_writePython (line 5260)

        def __m_ThisElement(this, range):
            __csu(this, range)
        # end function __m_ThisElement (line 5264)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5268)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5274)

        __clsT = __x_dcls("ThisElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"constantOnly": __x_prop(__g_constantOnly, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_ThisElement})
        return __clsT
    # end class factory ThisElement, __c_ThisElement (line 5236)

    def __c_ThrowElement(__cexT):
        def __g_typeName(this):
            return (u"throw")
        # end function __g_typeName (line 5287)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 5291)

        def __m_generatePython(this, ctx):
            right = this.lastChild
            writer = LineWriter()
            writer.write((u"raise "), False)
            right.writePython(writer, (u"\\"))
            writer.finalize(ctx)
        # end function __m_generatePython (line 5295)

        def __m_ThrowElement(this, range):
            __csu(this, range)
        # end function __m_ThrowElement (line 5303)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5307)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5313)

        __clsT = __x_dcls("ThrowElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_ThrowElement})
        return __clsT
    # end class factory ThrowElement, __c_ThrowElement (line 5286)

    def __c_TryBlockElement(__cexT):
        def __g_typeName(this):
            return (u"trygroup")
        # end function __g_typeName (line 5325)

        def __g_structList(this):
            return ArrayList([ElementPattern(TryElement, 1, False), ElementPattern(CatchElement, 1, True), ElementPattern(FinallyElement, 
1, True)])
        # end function __g_structList (line 5329)

        def __m_checkStruct(this):
            (super(__clsT, this)).checkStruct()
            if __x_cb(__x_eq(this.firstChild, this.lastChild)):
                raise InternalError((u"malformed structure in TryBlockElement (missing catch or finally)"))
            # end if (line 5336)
        # end function __m_checkStruct (line 5334)

        def __m_generatePython(this, gen):
            this.checkStruct()
            sline = LineNumber()
            gen.logLineNumber(sline)
            (super(__clsT, this)).generatePython(gen)
            gen.comment((u"end try (line %l)"), sline)
        # end function __m_generatePython (line 5341)

        def __m_TryBlockElement(this, range):
            __csu(this, range)
        # end function __m_TryBlockElement (line 5349)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5353)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5359)

        __clsT = __x_dcls("TryBlockElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), 
"checkStruct": __m_checkStruct, "generatePython": __m_generatePython, "structList": __x_prop(__g_structList, None), 
"typeName": __x_prop(__g_typeName, None), "__init__": __m_TryBlockElement})
        return __clsT
    # end class factory TryBlockElement, __c_TryBlockElement (line 5324)

    def __c_TryElement(__cexT):
        def __g_typeName(this):
            return (u"try")
        # end function __g_typeName (line 5372)

        def __m_checkStruct(this):
            if __x_cb(__x_not(__x_iof(this.parent, TryBlockElement))):
                raise InternalError((u"malformed structure in TryElement (not in TryBlockElement)"))
            # end if (line 5377)
            (super(__clsT, this)).checkStruct()
        # end function __m_checkStruct (line 5376)

        def __m_generatePython(this, ctx):
            ctx.writeln((u"try:"))
            ctx.tab()
            (super(__clsT, this)).generatePython(ctx)
            ctx.TAB()
        # end function __m_generatePython (line 5383)

        def __m_TryElement(this, range):
            __csu(this, range)
        # end function __m_TryElement (line 5390)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5394)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5400)

        __clsT = __x_dcls("TryElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkStruct": __m_checkStruct, 
"generatePython": __m_generatePython, "typeName": __x_prop(__g_typeName, None), "__init__": __m_TryElement})
        return __clsT
    # end class factory TryElement, __c_TryElement (line 5371)

    def __c_TupleElement(__cexT):
        def __g_typeName(this):
            return (u"tuple")
        # end function __g_typeName (line 5412)

        def __g_complex(this):
            return __x_cb(this.hasSpread) or (super(__clsT, this)).complex
        # end function __g_complex (line 5416)

        def __m_simplifyExpressions(this):
            if __x_cb(__x_not(this.complex)):
                return
            # end if (line 5421)
            tv = this.makeList()
            cc = CallElement.callGlobal((u"__x_tup"), VarElement.getTempVar(tv))
            this.replaceWith(cc)
        # end function __m_simplifyExpressions (line 5420)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            if __x_cb(this.hasSpread):
                raise InternalError((u"cannot generate python for tuple with spread syntax"))
            # end if (line 5430)
            writer.write((u"__x_tupof("), False)
            (super(__clsT, this)).writePython(writer, (u""))
            if __x_cb(__x_cb(__x_ne(this.firstChild, None)) and __x_eq(this.firstChild, this.lastChild)):
                writer.write((u","), False)
            # end if (line 5435)
            writer.write((u")"), contchr)
        # end function __m_writePython (line 5429)

        def __m_TupleElement(this, range):
            __csu(this, range)
        # end function __m_TupleElement (line 5441)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5445)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5451)

        __clsT = __x_dcls("TupleElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "complex": __x_prop(__g_complex, None), 
"simplifyExpressions": __m_simplifyExpressions, "typeName": __x_prop(__g_typeName, None), "writePython": __m_writePython, 
"__init__": __m_TupleElement})
        return __clsT
    # end class factory TupleElement, __c_TupleElement (line 5411)

    def __c_UniaryOperatorElement(__cexT):
        def __g_typeName(this):
            return (u"uniary")
        # end function __g_typeName (line 5464)

        def __g_constantOnly(this):
            return this.firstChild.constantOnly
        # end function __g_constantOnly (line 5468)

        def __g_tempVarOnly(this):
            return False
        # end function __g_tempVarOnly (line 5472)

        def __g_structList(this):
            return ArrayList([ElementPattern(ExpressionElement, 1, False)])
        # end function __g_structList (line 5476)

        def __m_functionalize(this):
            this.checkStruct()
            (super(__clsT, this)).functionalize()
            op = __cpm[this, "source"]
            n = __x_eq(op, (u"typeof"))
            m = __x_eq(op, (u"!"))
            if __x_cb(__x_not(__x_cb(n) or m)):
                return
            # end if (line 5486)
            exp = this.firstChild
            cc = CallElement.callGlobal((u"__x_typ") if __x_cb(n) else ((u"__x_tnb") if __x_cb(this.theGlobal.enableImplicitBooleanConversion)
 else (u"__x_not")), exp)
            this.replaceWith(cc)
        # end function __m_functionalize (line 5480)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            op = __cpm[this, "source"]
            dst = this.firstChild
            if __x_cb(__x_cb(__x_cb(__x_eq(op, (u"+"))) or __x_eq(op, (u"-"))) or __x_eq(op, (u"~"))):
                p = parentType > 10
                if __x_cb(p):
                    writer.write((u"("), False)
                # end if (line 5500)
                writer.write(op, False)
                dst.writePython(writer, (u"") if __x_cb(p) else contchr, 10)
                if __x_cb(p):
                    writer.write((u")"), contchr)
                # end if (line 5505)
            elif __x_cb(__x_eq(op, (u"?"))):
                p = parentType >= 3
                if __x_cb(p):
                    writer.write((u"("), False)
                # end if (line 5510)
                writer.write((u"None is not "), (u"") if __x_cb(p) else contchr)
                dst.writePython(writer, (u"") if __x_cb(p) else contchr, 4)
                if __x_cb(p):
                    writer.write((u")"), contchr)
                # end if (line 5515)
            else:
                raise InternalError((u"Cannot writePython for uniary ") + op)
            # end if (line 5498)
        # end function __m_writePython (line 5495)

        def __m_dump(this, ctx):
            ctx.attr((u"operator"), __cpm[this, "source"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 5523)

        def __m_UniaryOperatorElement(this, source, range):
            __csu(this, range)
            if __x_cb(__x_eq(source, (u"delete"))):
                raise CompileError((u"delete can only be a standalone statement"), range)
            # end if (line 5530)
            __cpm[this, "source"] = source
        # end function __m_UniaryOperatorElement (line 5528)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5536)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5542)

        __cpiT = __x_dpif("UniaryOperatorElement", {"__slots__": ("source",)})
        __clsT = __x_dcls("UniaryOperatorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "constantOnly": __x_prop(__g_constantOnly, None), "dump": __m_dump, "functionalize": __m_functionalize, 
"structList": __x_prop(__g_structList, None), "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_UniaryOperatorElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory UniaryOperatorElement, __c_UniaryOperatorElement (line 5463)

    def __c_UpdateElement(__cexT):
        def __g_typeName(this):
            return (u"update")
        # end function __g_typeName (line 5560)

        def __g_complex(this):
            return True
        # end function __g_complex (line 5564)

        def __g_structList(this):
            return ArrayList([ElementPattern(LvalueElement, 1, False)])
        # end function __g_structList (line 5568)

        def __m_checkVariables(this):
            this.checkStruct()
            target = this.firstChild
            target.checkVariables()
            target.checkWrite()
        # end function __m_checkVariables (line 5572)

        def __m_simplifyExpressions(this):
            def append(ase, val, act, op):
                fn = (u"__x_inc") if __x_cb(op) else (u"__x_dec")
                ase.append(CallElement.callGlobal(fn, val) if __x_cb(act) else val)
            # end function append (line 5580)

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
        # end function __m_simplifyExpressions (line 5579)

        def __m_dump(this, ctx):
            ctx.attr((u"prefix"), __cpm[this, "prefix"])
            ctx.attr((u"operator"), (u"++") if __x_cb(__cpm[this, "plus"]) else (u"--"))
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 5602)

        def __m_UpdateElement(this, source, prefix, range):
            __csu(this, range)
            if __x_cb(__x_eq(source, (u"++"))):
                __cpm[this, "plus"] = True
            elif __x_cb(__x_eq(source, (u"--"))):
                __cpm[this, "plus"] = False
            else:
                raise InternalError((u"invalid update operator"))
            # end if (line 5610)
            __cpm[this, "prefix"] = prefix
        # end function __m_UpdateElement (line 5608)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5620)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5626)

        __cpiT = __x_dpif("UpdateElement", {"__slots__": ("plus", "prefix")})
        __clsT = __x_dcls("UpdateElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"complex": __x_prop(__g_complex, None), "dump": __m_dump, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_UpdateElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory UpdateElement, __c_UpdateElement (line 5559)

    def __c_VarDeclaratorElement(__cexT):
        def __g_typeName(this):
            return (u"vardecl")
        # end function __g_typeName (line 5643)

        def __g_structList(this):
            return ArrayList([ElementPattern(VarElement, 1, False)])
        # end function __g_structList (line 5647)

        def __m_checkStruct(this):
            (super(__clsT, this)).checkStruct()
            v = this.firstChild
            if __x_cb(__x_not(v.declarator)):
                raise InternalError((u"malformed structure in VarDeclaratorElement (mismatched declarator)"))
            # end if (line 5654)
        # end function __m_checkStruct (line 5651)

        def __m_declareVariable(this):
            this.checkStruct()
            (super(__clsT, this)).declareVariable()
        # end function __m_declareVariable (line 5659)

        def __m_simplifyExpressions(this):
            this.remove()
        # end function __m_simplifyExpressions (line 5664)

        def __m_VarDeclaratorElement(this, range):
            __csu(this, range)
        # end function __m_VarDeclaratorElement (line 5668)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5672)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5678)

        __clsT = __x_dcls("VarDeclaratorElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
), "checkStruct": __m_checkStruct, "declareVariable": __m_declareVariable, "simplifyExpressions": __m_simplifyExpressions, 
"structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), "__init__": __m_VarDeclaratorElement})
        return __clsT
    # end class factory VarDeclaratorElement, __c_VarDeclaratorElement (line 5642)

    def __c_VarElement(__cexT):
        def __g_typeName(this):
            return (u"var")
        # end function __g_typeName (line 5691)

        def __g_complex(this):
            return False
        # end function __g_complex (line 5695)

        def __g_declarator(this):
            return __cpm[this, "_declarator"]
        # end function __g_declarator (line 5699)

        def __g_tempVarOnly(this):
            return __x_cb(__x_iof(__cpm[this, "target"], TempVar)) or __x_iof(__cpm[this, "target"], FunctionTag)
        # end function __g_tempVarOnly (line 5703)

        def __m_declareVariable(this):
            if __x_cb(__x_not(this.declarator)):
                return
            # end if (line 5708)
            __cpm[this, "target"] = this.theFunction.registerLocalVar(__cpm[this, "source"], this.range)
        # end function __m_declareVariable (line 5707)

        def __m_checkVariables(this):
            v = __cpm[this, "target"]
            if __x_cb(__x_eq(v, None)):
                v = this.theFunction.referVar(__cpm[this, "source"], this.range)
                __cpm[this, "target"] = v
            # end if (line 5716)
            v.read(this.theFunction, this.range)
        # end function __m_checkVariables (line 5714)

        def __m_checkWrite(this):
            v = __cpm[this, "target"]
            if __x_cb(__x_eq(v, None)):
                v = this.theFunction.referVar(__cpm[this, "source"], this.range)
                __cpm[this, "target"] = v
            # end if (line 5725)
            v.write(this.theFunction, this.range)
        # end function __m_checkWrite (line 5723)

        def __m_simplifyExpressions(this):
            pass
        # end function __m_simplifyExpressions (line 5732)

        def __m_extractLeft(this):
            pass
        # end function __m_extractLeft (line 5736)

        def __m_extractLeftAndDuplicate(this):
            if __x_cb(this.declarator):
                raise InternalError((u"declarator used in compound assignment"))
            # end if (line 5741)
            v = VarElement(__cpm[this, "source"], False, this.range)
            __r0 = v
            __cpm[__r0, "target"] = __cpm[this, "target"]
            return v
        # end function __m_extractLeftAndDuplicate (line 5740)

        def __m_writePython(this, writer, contchr, parentType = (0)):
            writer.write(__cpm[this, "target"].toPython(), contchr)
        # end function __m_writePython (line 5750)

        def __m_dump(this, ctx):
            ctx.attr((u"name"), __cpm[this, "source"])
            ctx.attr((u"variable"), __cpm[this, "target"])
            (super(__clsT, this)).dump(ctx)
        # end function __m_dump (line 5754)

        def __m_VarElement(this, source, declarator, range):
            __csu(this, range)
            __cpm[this, "source"] = source
            __cpm[this, "_declarator"] = declarator
        # end function __m_VarElement (line 5760)

        def __n_getGlobalVar(this, name):
            tvs = VarElement(name, False, None)
            __r0 = tvs
            __cpm[__r0, "target"] = GlobalVar(name)
            return tvs
        # end function __n_getGlobalVar (line 5766)

        def __n_getTempVar(this, tv):
            tvs = VarElement((u"__r"), False, None)
            __r0 = tvs
            __cpm[__r0, "target"] = tv
            return tvs
        # end function __n_getTempVar (line 5773)

        def __n_getFunctionExp(this, tag):
            tvs = VarElement((u"__e"), False, None)
            __r0 = tvs
            __cpm[__r0, "target"] = tag
            return tvs
        # end function __n_getFunctionExp (line 5780)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5787)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            __cpm[this, "target"] = None
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5793)

        __cpiT = __x_dpif("VarElement", {"__slots__": ("_declarator", "source", "target")})
        __clsT = __x_dcls("VarElement", __cexT, {"__slots__": (), "getFunctionExp": __n_getFunctionExp, "getGlobalVar": __n_getGlobalVar, 
"getTempVar": __n_getTempVar, "__init__": __csi}, {"__slots__": (), "checkVariables": __m_checkVariables, 
"checkWrite": __m_checkWrite, "complex": __x_prop(__g_complex, None), "declarator": __x_prop(__g_declarator, None), 
"declareVariable": __m_declareVariable, "dump": __m_dump, "extractLeft": __m_extractLeft, "extractLeftAndDuplicate": __m_extractLeftAndDuplicate, 
"simplifyExpressions": __m_simplifyExpressions, "tempVarOnly": __x_prop(__g_tempVarOnly, None), "typeName": __x_prop(__g_typeName, None), 
"writePython": __m_writePython, "__init__": __m_VarElement})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory VarElement, __c_VarElement (line 5690)

    def __c_WhileElement(__cexT):
        def __g_typeName(this):
            return (u"while")
        # end function __g_typeName (line 5814)

        def __g_structList(this):
            return ArrayList([ElementPattern(ConditionElement, 1, False), ElementPattern(BodyElement, 1, False)])
        # end function __g_structList (line 5818)

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
            # end if (line 5827)
            body.simplifyExpressions()
        # end function __m_simplifyExpressions (line 5822)

        def __m_generatePython(this, gen):
            cond = this.firstChild.firstChild
            body = this.lastChild
            writer = LineWriter()
            sline = LineNumber()
            gen.logLineNumber(sline)
            writer.write((u"while "), False)
            cond.writePython(writer, (u"\\"), 1)
            writer.write((u":"), False)
            writer.finalize(gen)
            gen.tab()
            body.generatePython(gen)
            gen.TAB()
            gen.comment((u"end while (line %l)"), sline)
        # end function __m_generatePython (line 5847)

        def __m_WhileElement(this, range):
            __csu(this, range)
        # end function __m_WhileElement (line 5863)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 5867)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 5873)

        __clsT = __x_dcls("WhileElement", __cexT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "generatePython": __m_generatePython, 
"simplifyExpressions": __m_simplifyExpressions, "structList": __x_prop(__g_structList, None), "typeName": __x_prop(__g_typeName, None), 
"__init__": __m_WhileElement})
        return __clsT
    # end class factory WhileElement, __c_WhileElement (line 5813)

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    StrTool = __r0.StrTool
    printf = __r0.printf
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    __r2 = __x_imp((u".utils"))
    CompileError = __r2.CompileError
    ElementPattern = __r2.ElementPattern
    Range = __r2.Range
    ConflictError = __r2.ConflictError
    InternalError = __r2.InternalError
    XMLDumper = __r2.XMLDumper
    __r3 = __x_imp((u".symboltree"))
    SymbolTree = __r3.SymbolTree
    SymbolTreeNode = __r3.SymbolTreeNode
    __r4 = __x_imp((u".identifier"))
    Attribute = __r4.Attribute
    BuiltinVar = __r4.BuiltinVar
    ClassFieldDescriptor = __r4.ClassFieldDescriptor
    ClassTag = __r4.ClassTag
    FunctionExpTag = __r4.FunctionExpTag
    FunctionTag = __r4.FunctionTag
    GlobalVar = __r4.GlobalVar
    Identifier = __r4.Identifier
    LocalVar = __r4.LocalVar
    MethodTag = __r4.MethodTag
    TempVar = __r4.TempVar
    Variable = __r4.Variable
    __r5 = __x_imp((u".pygen"))
    LineNumber = __r5.LineNumber
    LineWriter = __r5.LineWriter
    PyGenerator = __r5.PyGenerator
    Element = __c_Element()
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
    VarDeclaratorElement = __c_VarDeclaratorElement(StatementElement)
    VarElement = __c_VarElement(LvalueElement)
    WhileElement = __c_WhileElement(StatementElement)
# program end


__()
