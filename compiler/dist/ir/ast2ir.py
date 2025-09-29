# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("convertASTIR",)


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global convertASTIR

    # function definitions:

    def convertASTIR(ast):
        assrt(ast, Syntax.Program)
        ra = rangeFromAST(ast)
        ir = GlobalElement(ra)
        convTop(ir, ast)
        return ir
    # end function convertASTIR

    def convLiteral(p, o):
        v = o.value
        r = o.raw
        ra = rangeFromAST(o)
        if __x_cb(__x_eq(v, None)):
            el = NullLiteralElement(ra)
        elif __x_cb(__x_eq(__x_typ(v), (u"boolean"))):
            el = BooleanLiteralElement(v, ra)
        elif __x_cb(__x_eq(__x_typ(v), (u"string"))):
            el = StringLiteralElement(v, r, ra)
        elif __x_cb(__x_eq(__x_typ(v), (u"number"))):
            el = NumberLiteralElement(v, r, ra)
        else:
            raise InternalError((u"unknown literal type"), ra, v)
        # end if
        p.append(el)
    # end function convLiteral

    def convImag(p, o):
        r = o.raw
        ra = rangeFromAST(o)
        el = ComplexLiteralElement(r, ra)
        p.append(el)
    # end function convImag

    def assrt(o, type):
        if __x_cb(__x_eq(o, None)):
            raise InternalError((u"expected ") + type + (u" but null is met"))
        # end if
        if __x_cb(__x_ne(o.type, type)):
            raise InternalError((u"expected ") + type + (u" but ") + o.type + (u" is met"))
        # end if
    # end function assrt

    def assrt2(o, type):
        def __f6_(s, k, a):
            if __x_cb(__x_eq(o.type, s)):
                __u_m.val = True
            # end if
        # end function <anonymous> (__f6_)

        __u_m = __x_var()
        if __x_cb(__x_eq(o, None)):
            raise InternalError((u"expected ") + type + (u" but null is met"))
        # end if
        __u_m.val = False
        ArrayList(type).forEach(__f6_)
        if __x_cb(__x_not(__u_m.val)):
            raise InternalError((u"expected ") + ArrayList(type).get(0) + (u"-like but ") + o.type + (u" is met"))
        # end if
    # end function assrt2

    def convThis(p, o):
        assrt(o, Syntax.ThisExpression)
        ra = rangeFromAST(o)
        p.append(ThisElement(ra))
    # end function convThis

    def ident(o):
        assrt(o, Syntax.Identifier)
        return o.name
    # end function ident

    def createTag(o, TagClass, *argv):
        __r0 = TagClass
        __r1 = [ident(o), rangeFromAST(o)]
        __r1.extend(argv)
        return __r0(*__r1)
    # end function createTag

    def convIdentAsStr(p, o):
        assrt(o, Syntax.Identifier)
        n = ident(o)
        ra = rangeFromAST(o)
        se = StringLiteralElement(n, (u"\"") + n + (u"\""), ra)
        p.append(se)
    # end function convIdentAsStr

    def convAttr(o):
        return Attribute(ident(o), rangeFromAST(o))
    # end function convAttr

    def convVar(p, o, decl = (False)):
        assrt(o, Syntax.Identifier)
        ra = rangeFromAST(o)
        p.append(VarElement(VarReference(ident(o), ra), decl))
    # end function convVar

    def convMember(p, o):
        assrt(o, Syntax.MemberExpression)
        ra = rangeFromAST(o)
        oo = o.object
        po = o.property
        cm = o.computed
        if __x_cb(cm):
            ee = ItemElement(ra)
        else:
            ee = AttributeElement(convAttr(po), ra)
        # end if
        p.append(ee)
        convExpr(ee, oo)
        if __x_cb(cm):
            convExprAllowTuple(ee, po)
        # end if
    # end function convMember

    def convSuper(p, o):
        assrt(o, Syntax.Super)
        ra = rangeFromAST(o)
        p.append(SuperElement(ra))
    # end function convSuper

    def convArgs(tus, pra, args):
        def __fG_(ie, k, a):
            if __x_cb(__x_eq(ie, None)):
                CAS.error(pra, (u"Empty slot is not allowed"))
            # end if
            ra = rangeFromAST(ie)
            if __x_cb(__x_eq(ie.type, Syntax.SpreadElement)):
                iee = SpreadElement(ra)
                tus.append(iee)
                convExpr(iee, ie.argument)
            else:
                convExpr(tus, ie)
            # end if
        # end function <anonymous> (__fG_)

        ArrayList(args).forEach(__fG_)
    # end function convArgs

    def convDotAtCall(p, o):
        assrt2(o, [Syntax.CallExpression, Syntax.NewExpression])
        ra = rangeFromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.NewExpression)):
            CAS.error(ra, (u"at-function can only be callee"))
        # end if
        ce = o.callee
        assrt(ce, Syntax.DotAtExpression)
        me = ce.method
        obj = ce.object
        argv = o.arguments
        da = MagicCallElement(ident(me), ra)
        p.append(da)
        convExpr(da, obj)
        arge = ArgumentElement(None)
        da.append(arge)
        convArgs(arge, ra, argv)
    # end function convDotAtCall

    def convImport(p, o):
        assrt(o, Syntax.Import)
        ra = rangeFromAST(o)
        cs = ImportElement(ra)
        p.append(cs)
    # end function convImport

    def convCall(p, o):
        assrt2(o, [Syntax.CallExpression, Syntax.NewExpression])
        ra = rangeFromAST(o)
        argv = o.arguments
        ce = o.callee
        if __x_cb(__x_eq(ce.type, Syntax.DotAtExpression)):
            convDotAtCall(p, o)
        else:
            cs = CallElement(ra)
            p.append(cs)
            convExpr(cs, ce)
            arge = ArgumentElement(None)
            cs.append(arge)
            convArgs(arge, ra, argv)
        # end if
    # end function convCall

    def convArray(p, o):
        assrt(o, Syntax.ArrayExpression)
        ra = rangeFromAST(o)
        ce = o.elements
        cs = ArrayElement(ra)
        p.append(cs)
        convArgs(cs, ra, ce)
    # end function convArray

    def convObject(p, o):
        def __fM_(ie, k, a):
            ke = ie.key
            ve = ie.value
            ki = ie.kind
            rra = rangeFromAST(ie)
            if __x_cb(__x_eq(ve, None)):
                raise InternalError((u"null value dict init"), ie)
            # end if
            if __x_cb(__x_ne(ki, (u"init"))):
                CAS.error(rra, (u"Accessor or method in object expression is not allowed."))
            # end if
            kve = KeyValueElement(rra)
            cs.append(kve)
            if __x_cb(__x_eq(ke.type, Syntax.Identifier)):
                convIdentAsStr(kve, ke)
            else:
                convExpr(kve, ke)
            # end if
            convExpr(kve, ve)
        # end function <anonymous> (__fM_)

        assrt(o, Syntax.ObjectExpression)
        ra = rangeFromAST(o)
        ce = o.properties
        cs = ObjectLiteralElement(ra)
        p.append(cs)
        ArrayList(ce).forEach(__fM_)
    # end function convObject

    def convUnary(p, o):
        assrt(o, Syntax.UnaryExpression)
        ra = rangeFromAST(o)
        op = o.operator
        ar = o.argument
        ee = UniaryOperatorElement(op, ra)
        p.append(ee)
        convExpr(ee, ar)
    # end function convUnary

    def convBinary(p, o):
        assrt(o, Syntax.BinaryExpression)
        ra = rangeFromAST(o)
        op = o.operator
        ee = BinaryOperatorElement(op, ra)
        p.append(ee)
        convExpr(ee, o.left)
        convExpr(ee, o.right)
    # end function convBinary

    def convBinaryLogic(p, o):
        assrt(o, Syntax.LogicalExpression)
        ra = rangeFromAST(o)
        op = o.operator
        ee = BinaryLogicalElement(op, ra)
        p.append(ee)
        convExpr(ee, o.left)
        convExpr(ee, o.right)
    # end function convBinaryLogic

    def convUpdate(p, o):
        assrt(o, Syntax.UpdateExpression)
        ra = rangeFromAST(o)
        op = o.operator
        ar = o.argument
        ee = UpdateElement(op, o.prefix, ra)
        p.append(ee)
        convExpr(ee, ar)
    # end function convUpdate

    def convCond(p, o):
        assrt(o, Syntax.ConditionalExpression)
        ra = rangeFromAST(o)
        ee = TernaryOperatorElement(ra)
        p.append(ee)
        convExpr(ee, o.test)
        convExpr(ee, o.consequent)
        convExpr(ee, o.alternate)
    # end function convCond

    def makeError(msg):
        def __fT_(p, o):
            ra = rangeFromAST(o)
            CAS.error(ra, msg)
        # end function <anonymous> (__fT_)

        return __fT_
    # end function makeError

    def convExpr(p, o):
        emap = StringMap([[Syntax.Literal, convLiteral], [Syntax.ComplexLiteral, convImag], [Syntax.ThisExpression, 
convThis], [Syntax.Identifier, convVar], [Syntax.MemberExpression, convMember], [Syntax.Super, convSuper], 
[Syntax.CallExpression, convCall], [Syntax.NewExpression, convCall], [Syntax.ArrayExpression, convArray], 
[Syntax.ObjectExpression, convObject], [Syntax.UnaryExpression, convUnary], [Syntax.BinaryExpression, 
convBinary], [Syntax.LogicalExpression, convBinaryLogic], [Syntax.UpdateExpression, convUpdate], [Syntax\
.ConditionalExpression, convCond], [Syntax.FunctionExpression, convFuncExpr], [Syntax.Import, convImport], 
[Syntax.SequenceExpression, makeError((u"comma operator is not allowed"))], [Syntax.DotAtExpression, 
makeError((u"at-function can only be callee"))], [Syntax.ArrowFunctionExpression, makeError((u"arrow function is not allowed"))], 
[Syntax.AssignmentExpression, makeError((u"assignment must be standalone statement"))], [Syntax.YieldExpression, 
makeError((u"generator is not implemented yet"))], [Syntax.AwaitExpression, makeError((u"async function is not implemented yet"))], 
[Syntax.TemplateElement, makeError((u"templated string is not implemented yet"))], [Syntax.TemplateLiteral, 
makeError((u"templated string is not implemented yet"))]])
        res = emap.get(o.type, None)
        if __x_cb(__x_eq(res, None)):
            raise InternalError((u"unknown expression ") + o.type, o)
        # end if
        res(p, o)
    # end function convExpr

    def convExprAllowTuple(p, o):
        if __x_cb(__x_cb(o.type != Syntax.SequenceExpression) or __x_not(options.enableTupleSubscription)):
            convExpr(p, o)
            return
        # end if
        ra = rangeFromAST(o)
        ce = o.expressions
        cs = TupleElement(ra)
        p.append(cs)
        convArgs(cs, ra, ce)
    # end function convExprAllowTuple

    def convExprStat(p, o):
        assrt(o, Syntax.ExpressionStatement)
        ie = o.expression
        ra = rangeFromAST(o)
        if __x_cb(__x_cb(__x_eq(ie.type, Syntax.UnaryExpression)) and __x_eq(ie.operator, (u"delete"))):
            convDelete(p, ie)
        elif __x_cb(__x_eq(ie.type, Syntax.AssignmentExpression)):
            convAssign(p, ra, ie.left, ie.right, ie.operator)
        else:
            ee = ExpressionStatementElement(ra)
            p.append(ee)
            convExpr(ee, ie)
        # end if
    # end function convExprStat

    def convDelete(p, o):
        assrt(o, Syntax.UnaryExpression)
        ra = rangeFromAST(o)
        ee = DeleteElement(ra)
        ar = o.argument
        p.append(ee)
        convExpr(ee, ar)
    # end function convDelete

    def convAssign(p, ra, l, r, op):
        if __x_cb(__x_eq(l.type, Syntax.ArrayPattern)):
            CAS.error(ra, (u"Destructing to array pattern is not supported yet."))
        # end if
        if __x_cb(__x_ne(l.type, Syntax.ObjectPattern)):
            ee = CompoundAssignElement(op, ra) if __x_cb(__x_ne(op, (u"="))) else AssignElement(ra)
            p.append(ee)
            convExpr(ee, l)
        else:
            if __x_cb(__x_ne(op, (u"="))):
                raise InternalError((u"compound destructuring assignment"))
            # end if
            ee = AssignDestructElement(ra)
            p.append(ee)
            convPattern(ee, l, False)
        # end if
        convExpr(ee, r)
    # end function convAssign

    def convPattern(p, o, decl):
        ra = rangeFromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.ArrayPattern)):
            CAS.error(ra, (u"Destructuring to array pattern is not supported yet."))
        elif __x_cb(__x_eq(o.type, Syntax.ObjectPattern)):
            convObjPattern(p, o, decl)
        else:
            raise InternalError((u"Unknown pattern type ") + o.type)
        # end if
    # end function convPattern

    def convObjPattern(p, o, decl):
        def __f15_(ie, k, a):
            __u_has.val = True
            ko = ie.key
            vo = ie.value
            ki = ie.kind
            rra = rangeFromAST(ie)
            if __x_cb(__x_eq(vo, None)):
                raise InternalError((u"null value object pattern"), ie)
            # end if
            if __x_cb(__x_ne(ki, (u"init"))):
                raise InternalError((u"method in object pattern"), ie)
            # end if
            kve = DestructPropertyElement(decl, convAttr(ko), rra)
            ee.append(kve)
            if __x_cb(__x_eq(vo.type, Syntax.AssignmentPattern)):
                CAS.error(rra, (u"Default value is not allowed in destructuring object."))
            elif __x_cb(__x_cb(__x_eq(vo.type, Syntax.ArrayPattern)) or __x_eq(vo.type, Syntax.ObjectPattern)):
                convPattern(kve, vo, decl)
            elif __x_cb(decl):
                convVar(kve, vo, True)
            else:
                convExpr(kve, vo)
            # end if
        # end function <anonymous> (__f15_)

        __u_has = __x_var()
        assrt(o, Syntax.ObjectPattern)
        ra = rangeFromAST(o)
        ce = o.properties
        ee = DestructObjectElement(decl, ra)
        p.append(ee)
        __u_has.val = False
        ArrayList(ce).forEach(__f15_)
        if __x_cb(__x_not(__u_has.val)):
            CAS.error(ra, (u"Empty destructuring target is not allowed."))
        # end if
    # end function convObjPattern

    def convVarDecl(p, o):
        def __f17_(oi, k, a):
            assrt(oi, Syntax.VariableDeclarator)
            rra = rangeFromAST(oi)
            l = oi.id
            r = oi.init
            if __x_cb(__x_eq(r, None)):
                ee = ExpressionStatementElement(rra)
                p.append(ee)
                ee.append(VarElement(VarReference(ident(l), rra), True))
            elif __x_cb(__x_eq(l.type, Syntax.Identifier)):
                ee = AssignElement(rra)
                p.append(ee)
                convVar(ee, l, True)
                convExpr(ee, r)
            else:
                ee = AssignDestructElement(ra)
                p.append(ee)
                convPattern(ee, l, True)
                convExpr(ee, r)
            # end if
        # end function <anonymous> (__f17_)

        assrt(o, Syntax.VariableDeclaration)
        ra = rangeFromAST(o)
        ki = o.kind
        if __x_cb(__x_ne(ki, (u"var"))):
            CAS.error(ra, (u"%s declaration is not allowed"), ki)
        # end if
        ArrayList(o.declarations).forEach(__f17_)
    # end function convVarDecl

    def convChildren(p, el):
        def __f19_(ie, k, a):
            convStat(p, ie)
        # end function <anonymous> (__f19_)

        ArrayList(el).forEach(__f19_)
    # end function convChildren

    def convStatOrBlock(p, o, BodyClass):
        if __x_cb(__x_eq(o, None)):
            assrt(o, Syntax.BlockStatement)
        # end if
        ra = rangeFromAST(o)
        be = BodyClass(ra)
        p.append(be)
        if __x_cb(__x_eq(o.type, Syntax.BlockStatement)):
            convChildren(be, o.body)
        else:
            convStat(be, o)
        # end if
    # end function convStatOrBlock

    def convCondExpr(p, o):
        ra = rangeFromAST(o)
        ee = ConditionElement(ra)
        p.append(ee)
        convExpr(ee, o)
    # end function convCondExpr

    def convWhile(p, o):
        assrt(o, Syntax.WhileStatement)
        ra = rangeFromAST(o)
        we = WhileElement(ra)
        p.append(we)
        convCondExpr(we, o.test)
        convStatOrBlock(we, o.body, BodyElement)
    # end function convWhile

    def convElse(p, o):
        if __x_cb(__x_eq(o, None)):
            return
        # end if
        ra = rangeFromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.IfStatement)):
            elife = ElifElement(ra)
            p.append(elife)
            convCondExpr(elife, o.test)
            convStatOrBlock(elife, o.consequent, BodyElement)
            convElse(p, o.alternate)
        else:
            convStatOrBlock(p, o, ElseElement)
        # end if
    # end function convElse

    def convIf(p, o):
        assrt(o, Syntax.IfStatement)
        ra = rangeFromAST(o)
        ee = IfBlockElement(ra)
        p.append(ee)
        ie = IfElement(ra)
        ee.append(ie)
        convCondExpr(ie, o.test)
        convStatOrBlock(ie, o.consequent, BodyElement)
        convElse(ee, o.alternate)
    # end function convIf

    def convReturn(p, o):
        assrt(o, Syntax.ReturnStatement)
        ra = rangeFromAST(o)
        re = ReturnElement(ra)
        p.append(re)
        a = o.argument
        if __x_cb(__x_ne(a, None)):
            convExpr(re, a)
        # end if
    # end function convReturn

    def convThrow(p, o):
        assrt(o, Syntax.ThrowStatement)
        ra = rangeFromAST(o)
        throw_ = ThrowElement(ra)
        p.append(throw_)
        convExpr(throw_, o.argument)
    # end function convThrow

    def convBreak(p, o):
        assrt(o, Syntax.BreakStatement)
        ra = rangeFromAST(o)
        if __x_cb(__x_ne(o.label, None)):
            CAS.error(ra, (u"labeled break is not implemented yet."))
        # end if
        p.append(BreakElement(ra))
    # end function convBreak

    def convCont(p, o):
        assrt(o, Syntax.ContinueStatement)
        ra = rangeFromAST(o)
        if __x_cb(__x_ne(o.label, None)):
            CAS.error(ra, (u"labeled continue is not implemented yet."))
        # end if
        p.append(ContinueElement(ra))
    # end function convCont

    def convParam(p, o):
        ra = rangeFromAST(o)
        if __x_cb(__x_ne(o.type, Syntax.Identifier)):
            CAS.error(ra, (u"Destructuring parameter is not supported yet"))
        # end if
        ee = ParameterElement(ident(o), ra)
        p.append(ee)
    # end function convParam

    def convCatch(tcf, o):
        assrt(o, Syntax.CatchClause)
        ra = rangeFromAST(o)
        een = __x_ne(o.param, None)
        catch_ = CatchElement(ra)
        tcf.append(catch_)
        if __x_cb(een):
            convParam(catch_, o.param)
        # end if
        convStatOrBlock(catch_, o.body, BodyElement)
    # end function convCatch

    def convTry(p, o):
        assrt(o, Syntax.TryStatement)
        ra = rangeFromAST(o)
        tcf = TryBlockElement(ra)
        p.append(tcf)
        convStatOrBlock(tcf, o.block, TryElement)
        if __x_cb(__x_ne(o.handler, None)):
            convCatch(tcf, o.handler)
        # end if
        if __x_cb(__x_ne(o.finalizer, None)):
            convStatOrBlock(tcf, o.finalizer, FinallyElement)
        # end if
    # end function convTry

    def convStat(p, o):
        def __f1N_(*a):
            pass
        # end function <anonymous> (__f1N_)

        emap = StringMap([[Syntax.EmptyStatement, __f1N_], [Syntax.ExpressionStatement, convExprStat], [Syntax\
.VariableDeclaration, convVarDecl], [Syntax.WhileStatement, convWhile], [Syntax.IfStatement, convIf], 
[Syntax.TryStatement, convTry], [Syntax.ThrowStatement, convThrow], [Syntax.ContinueStatement, convCont], 
[Syntax.BreakStatement, convBreak], [Syntax.ReturnStatement, convReturn], [Syntax.FunctionDeclaration, 
makeError((u"nested functions cannot be declared"))]])
        res = emap.get(o.type, None)
        if __x_cb(__x_eq(res, None)):
            raise InternalError((u"unknown statement ") + o.type, o)
        # end if
        res(p, o)
    # end function convStat

    def convFuncDecl(pfn, o, pub):
        assrt(o, Syntax.FunctionDeclaration)
        if __x_cb(o.expression):
            raise InternalError((u"Unexcepted function with single expression"), o)
        # end if
        ra = rangeFromAST(o)
        fn = FunctionDefinitionElement(createTag(o.id, FunctionTag), pub, ra)
        pfn.functionDefinitions.append(fn)
        convFuncInner(fn, o)
    # end function convFuncDecl

    def convFuncExpr(p, o):
        assrt(o, Syntax.FunctionExpression)
        ra = rangeFromAST(o)
        name = o.id
        fnc = FunctionExpressionContainerElement(FunctionExpTag() if __x_cb(__x_eq(name, None)) else createTag(name, 
FunctionExpTag), ra)
        fn = fnc.functionBody
        p.append(fnc)
        convFuncInner(fn, o)
    # end function convFuncExpr

    def convFuncInnerDecl(fn, o):
        if __x_cb(__x_eq(o.type, Syntax.FunctionDeclaration)):
            convFuncDecl(fn, o, False)
        else:
            convStat(fn.body, o)
        # end if
    # end function convFuncInnerDecl

    def convFuncInner(fn, o):
        def __f1S_(p, k, v):
            rra = rangeFromAST(o)
            if __x_cb(__x_cb(__x_cb(__x_eq(p.type, Syntax.Identifier)) or __x_eq(p.type, Syntax.ArrayPattern)) or __x_eq(p\
.type, Syntax.ObjectPattern)):
                if __x_cb(opt):
                    CAS.error(rra, (u"optional parameter may be placed only after required parameter"))
                # end if
                convParam(pe, p)
            elif __x_cb(__x_eq(p.type, Syntax.AssignmentPattern)):
                ie = ParameterAssignElement(rra)
                pe.append(ie)
                convParam(ie, p.left)
                convExpr(ie, p.right)
            elif __x_cb(__x_eq(p.type, Syntax.RestElement)):
                ie = RestParameterElement(rra)
                pe.append(ie)
                convParam(ie, p.argument)
            else:
                raise InternalError((u"unknown parameter ") + p.type, p)
            # end if
        # end function <anonymous> (__f1S_)

        def __f1T_(m, k, a):
            convFuncInnerDecl(fn, m)
        # end function <anonymous> (__f1T_)

        ra = rangeFromAST(o)
        if __x_cb(o.isAsync):
            CAS.error(ra, (u"async function is not supported yet"))
        # end if
        if __x_cb(o.generator):
            CAS.error(ra, (u"generator function is not supported yet"))
        # end if
        pe = fn.parameters
        opt = False
        ArrayList(o.params).forEach(__f1S_)
        defs = fn.functionDefinitions
        body = fn.body
        expr = o.expression
        if __x_cb(expr):
            rra = rangeFromAST(o.body)
            re = ReturnElement(rra)
            body.append(re)
            convExpr(re, o.body)
        else:
            assrt(o.body, Syntax.BlockStatement)
            ArrayList(o.body.body).forEach(__f1T_)
        # end if
    # end function convFuncInner

    def convClassDecl(g, oc, pub):
        def __f1V_(oi, k, a):
            def __f20_(ov, k, a):
                assrt(ov, Syntax.VariableDeclarator)
                rii = rangeFromAST(ov)
                ido = ov.id
                ino = ov.init
                ie = (StaticInitializerElement if __x_cb(s) else InstanceInitializerElement)(convAttr(ido), p, rii)
                (ce.staticInit if __x_cb(s) else ce.instanceInit).body.append(ie)
                if __x_cb(__x_ne(ino, None)):
                    convExpr(ie, ino)
                # end if
            # end function <anonymous> (__f20_)

            ra = rangeFromAST(oi)
            ira = rangeFromAST(oi)
            if __x_cb(__x_eq(oi.accessModifier, (u"public"))):
                p = True
            elif __x_cb(__x_eq(oi.accessModifier, (u"private"))):
                p = False
            else:
                raise InternalError((u"unknown access modifier"))
            # end if
            s = oi.isStatic
            od = oi.declaration
            if __x_cb(__x_cb(__x_eq(oi.type, Syntax.PropertyDeclaration)) and __x_eq(oi.kind, (u"var"))):
                assrt(od, Syntax.VariableDeclaration)
                ArrayList(od.declarations).forEach(__f20_)
            elif __x_cb(__x_eq(oi.type, Syntax.MethodDeclaration)):
                assrt(od, Syntax.FunctionDeclaration)
                me = MethodElement(createTag(od.id, MethodTag, oi.kind, s, p), ra)
                ce.functionDefinitions.append(me)
                convFuncInner(me, od)
            else:
                raise InternalError((u"unknown class member type"))
            # end if
        # end function <anonymous> (__f1V_)

        assrt(oc, Syntax.ClassDeclaration)
        ra = rangeFromAST(oc)
        su = oc.superClass
        ce = ClassElement(createTag(oc.id, ClassTag), __x_ne(su, None), pub, ra)
        g.classDefinitions.append(ce)
        cinit = ce.createClassInitElement()
        g.body.append(cinit)
        if __x_cb(__x_ne(su, None)):
            convExpr(cinit, su)
        # end if
        bo = oc.body
        assrt(bo, Syntax.ClassBody)
        ArrayList(bo.body).forEach(__f1V_)
    # end function convClassDecl

    def convTopDecl(g, o, pub, next):
        ra = rangeFromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.FunctionDeclaration)):
            convFuncDecl(g, o, pub)
        elif __x_cb(__x_eq(o.type, Syntax.ClassDeclaration)):
            convClassDecl(g, o, pub)
        else:
            next(g, o)
        # end if
    # end function convTopDecl

    def convTop(g, o):
        def __f23_(m, k, a):
            def __f24_(g, o):
                raise InternalError((u"Illegal public declaration ") + o.type)
            # end function <anonymous> (__f24_)

            if __x_cb(__x_eq(m.type, Syntax.PublicDeclaration)):
                convTopDecl(g, m.declaration, True, __f24_)
            else:
                convTopDecl(g, m, False, convFuncInnerDecl)
            # end if
        # end function <anonymous> (__f23_)

        assrt(o, Syntax.Program)
        ArrayList(o.body).forEach(__f23_)
    # end function convTop

    def rangeFromAST(o):
        locs = o.loc
        rg = o.range
        return Range(Marker(rg[0], locs.start.line, locs.start.column), Marker(rg[1], locs.end.line, locs.end\
.column))
    # end function rangeFromAST

    # class definitions:

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    __r2 = __x_imp((u".utils"))
    InternalError = __r2.InternalError
    __r3 = __x_imp((u"tools.range"))
    Range = __r3.Range
    Marker = __r3.Marker
    __r4 = __x_imp((u"tools.options"))
    options = __r4.options
    CAS = __x_imp((u"tools.cas"))
    __r5 = __x_imp((u".attribute"))
    Attribute = __r5.Attribute
    __r6 = __x_imp((u".variable"))
    VarReference = __r6.VarReference
    ClassTag = __r6.ClassTag
    FunctionTag = __r6.FunctionTag
    FunctionExpTag = __r6.FunctionExpTag
    MethodTag = __r6.MethodTag
    __r7 = __x_imp((u".syntax"))
    Syntax = __r7.Syntax
    __r8 = __x_imp((u".element"))
    ArgumentElement = __r8.ArgumentElement
    ArrayElement = __r8.ArrayElement
    AssignDestructElement = __r8.AssignDestructElement
    AssignElement = __r8.AssignElement
    AssignTempElement = __r8.AssignTempElement
    AttributeElement = __r8.AttributeElement
    BaseFunctionElement = __r8.BaseFunctionElement
    BinaryOperatorElement = __r8.BinaryOperatorElement
    BinaryLogicalElement = __r8.BinaryLogicalElement
    BlockElement = __r8.BlockElement
    BodyElement = __r8.BodyElement
    BooleanLiteralElement = __r8.BooleanLiteralElement
    BreakElement = __r8.BreakElement
    CallElement = __r8.CallElement
    CatchElement = __r8.CatchElement
    ClassElement = __r8.ClassElement
    ClassGroupElement = __r8.ClassGroupElement
    ClassInitElement = __r8.ClassInitElement
    ComplexLiteralElement = __r8.ComplexLiteralElement
    CompoundAssignElement = __r8.CompoundAssignElement
    ConditionElement = __r8.ConditionElement
    ContinueElement = __r8.ContinueElement
    DeleteElement = __r8.DeleteElement
    DestructGroupElement = __r8.DestructGroupElement
    DestructObjectElement = __r8.DestructObjectElement
    DestructPropertyElement = __r8.DestructPropertyElement
    DoWhileElement = __r8.DoWhileElement
    Element = __r8.Element
    ElifElement = __r8.ElifElement
    ElseElement = __r8.ElseElement
    ExpressionElement = __r8.ExpressionElement
    ExpressionStatementElement = __r8.ExpressionStatementElement
    FinallyElement = __r8.FinallyElement
    FunctionDefinitionElement = __r8.FunctionDefinitionElement
    FunctionElement = __r8.FunctionElement
    FunctionExpressionElement = __r8.FunctionExpressionElement
    FunctionExpressionContainerElement = __r8.FunctionExpressionContainerElement
    FunctionGroupElement = __r8.FunctionGroupElement
    FundamentalLiteralElement = __r8.FundamentalLiteralElement
    GlobalElement = __r8.GlobalElement
    IfBlockElement = __r8.IfBlockElement
    IfElement = __r8.IfElement
    ImportElement = __r8.ImportElement
    InstanceGroupElement = __r8.InstanceGroupElement
    InstanceInitializerElement = __r8.InstanceInitializerElement
    ItemElement = __r8.ItemElement
    KeyValueElement = __r8.KeyValueElement
    LvalueElement = __r8.LvalueElement
    MagicCallElement = __r8.MagicCallElement
    MethodElement = __r8.MethodElement
    MethodGroupElement = __r8.MethodGroupElement
    MethodParameterGroupElement = __r8.MethodParameterGroupElement
    NotOperatorElement = __r8.NotOperatorElement
    NullLiteralElement = __r8.NullLiteralElement
    NullishCheckElement = __r8.NullishCheckElement
    NumberLiteralElement = __r8.NumberLiteralElement
    ObjectLiteralElement = __r8.ObjectLiteralElement
    ParameterAssignElement = __r8.ParameterAssignElement
    ParameterElement = __r8.ParameterElement
    ParameterGroupElement = __r8.ParameterGroupElement
    RestParameterElement = __r8.RestParameterElement
    ReturnElement = __r8.ReturnElement
    SequenceElement = __r8.SequenceElement
    SpreadElement = __r8.SpreadElement
    StatementElement = __r8.StatementElement
    StaticGroupElement = __r8.StaticGroupElement
    StaticInitializerElement = __r8.StaticInitializerElement
    StringLiteralElement = __r8.StringLiteralElement
    SuperElement = __r8.SuperElement
    TernaryOperatorElement = __r8.TernaryOperatorElement
    ThisElement = __r8.ThisElement
    ThrowElement = __r8.ThrowElement
    TryBlockElement = __r8.TryBlockElement
    TryElement = __r8.TryElement
    TupleElement = __r8.TupleElement
    UniaryOperatorElement = __r8.UniaryOperatorElement
    UpdateElement = __r8.UpdateElement
    VarElement = __r8.VarElement
    WhileElement = __r8.WhileElement
# program end


__()
