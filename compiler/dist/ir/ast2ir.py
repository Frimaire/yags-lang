# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("convertASTIR",)


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global convertASTIR

    # function definitions:

    def convertASTIR(ast, options):
        assrt(ast, Syntax.Program)
        ra = Range.fromAST(ast)
        ir = GlobalElement(ra)
        if __x_cb(__x_eq(options, None)):
            options = StringMap()
        # end if (line 18)
        __r0 = ir
        __r0.enableImplicitBooleanConversion = options.get((u"enableImplicitBooleanConversion"), False)
        __r1 = ir
        __r1.enableTupleSubscription = options.get((u"enableTupleSubscription"), False)
        convTop(ir, ast)
        return ir
    # end function convertASTIR (line 14)

    def convLiteral(p, o):
        v = o.value
        r = o.raw
        ra = Range.fromAST(o)
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
        # end if (line 33)
        p.append(el)
    # end function convLiteral (line 29)

    def convImag(p, o):
        r = o.raw
        ra = Range.fromAST(o)
        el = ComplexLiteralElement(r, ra)
        p.append(el)
    # end function convImag (line 47)

    def assrt(o, type):
        if __x_cb(__x_eq(o, None)):
            raise InternalError((u"expected ") + type + (u" but null is met"))
        # end if (line 55)
        if __x_cb(__x_ne(o.type, type)):
            raise InternalError((u"expected ") + type + (u" but ") + o.type + (u" is met"))
        # end if (line 58)
    # end function assrt (line 54)

    def assrt2(o, type):
        def __f6_(s, k, a):
            if __x_cb(__x_eq(o.type, s)):
                __u_m.val = True
            # end if (line 65)
        # end function <anonymous> (__f6_) (line 64)

        __u_m = __x_var()
        if __x_cb(__x_eq(o, None)):
            raise InternalError((u"expected ") + type + (u" but null is met"))
        # end if (line 71)
        __u_m.val = False
        ArrayList(type).forEach(__f6_)
        if __x_cb(__x_not(__u_m.val)):
            raise InternalError((u"expected ") + ArrayList(type).get(0) + (u"-like but ") + o.type + (u" is met"))
        # end if (line 76)
    # end function assrt2 (line 63)

    def convThis(p, o):
        assrt(o, Syntax.ThisExpression)
        ra = Range.fromAST(o)
        p.append(ThisElement(ra))
    # end function convThis (line 81)

    def ident(o):
        assrt(o, Syntax.Identifier)
        return o.name
    # end function ident (line 87)

    def convIdentAsStr(p, o):
        assrt(o, Syntax.Identifier)
        n = ident(o)
        ra = Range.fromAST(o)
        se = StringLiteralElement(n, (u"\"") + n + (u"\""), ra)
        p.append(se)
    # end function convIdentAsStr (line 92)

    def convAttr(o):
        return Attribute(ident(o), Range.fromAST(o))
    # end function convAttr (line 100)

    def convVar(p, o, decl = (False)):
        assrt(o, Syntax.Identifier)
        ra = Range.fromAST(o)
        p.append(VarElement(ident(o), decl, ra))
    # end function convVar (line 104)

    def convMember(p, o):
        assrt(o, Syntax.MemberExpression)
        ra = Range.fromAST(o)
        oo = o.object
        po = o.property
        cm = o.computed
        if __x_cb(cm):
            ee = ItemElement(ra)
        else:
            ee = AttributeElement(convAttr(po), ra)
        # end if (line 116)
        p.append(ee)
        convExpr(ee, oo)
        if __x_cb(cm):
            convExprAllowTuple(ee, po)
        # end if (line 123)
    # end function convMember (line 110)

    def convSuper(p, o):
        assrt(o, Syntax.Super)
        ra = Range.fromAST(o)
        p.append(SuperElement(ra))
    # end function convSuper (line 128)

    def convArgs(tus, pra, args):
        def __fF_(ie, k, a):
            if __x_cb(__x_eq(ie, None)):
                raise CompileError((u"Empty slot is not allowed"), pra)
            # end if (line 136)
            ra = Range.fromAST(ie)
            if __x_cb(__x_eq(ie.type, Syntax.SpreadElement)):
                iee = SpreadElement(ra)
                tus.append(iee)
                convExpr(iee, ie.argument)
            else:
                convExpr(tus, ie)
            # end if (line 140)
        # end function <anonymous> (__fF_) (line 135)

        ArrayList(args).forEach(__fF_)
    # end function convArgs (line 134)

    def convDotAtCall(p, o):
        assrt2(o, [Syntax.CallExpression, Syntax.NewExpression])
        ra = Range.fromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.NewExpression)):
            raise CompileError((u"at-function can only be callee"), ra)
        # end if (line 155)
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
    # end function convDotAtCall (line 152)

    def convImport(p, o):
        assrt(o, Syntax.Import)
        ra = Range.fromAST(o)
        cs = ImportElement(ra)
        p.append(cs)
    # end function convImport (line 171)

    def convCall(p, o):
        assrt2(o, [Syntax.CallExpression, Syntax.NewExpression])
        ra = Range.fromAST(o)
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
        # end if (line 183)
    # end function convCall (line 178)

    def convArray(p, o):
        assrt(o, Syntax.ArrayExpression)
        ra = Range.fromAST(o)
        ce = o.elements
        cs = ArrayElement(ra)
        p.append(cs)
        convArgs(cs, ra, ce)
    # end function convArray (line 195)

    def convObject(p, o):
        def __fL_(ie, k, a):
            ke = ie.key
            ve = ie.value
            ki = ie.kind
            rra = Range.fromAST(ie)
            if __x_cb(__x_eq(ve, None)):
                raise InternalError((u"null value dict init"), ie)
            # end if (line 210)
            if __x_cb(__x_ne(ki, (u"init"))):
                raise CompileError((u"accessor or method in object expression is not allowed"), rra)
            # end if (line 213)
            kve = KeyValueElement(rra)
            cs.append(kve)
            if __x_cb(__x_eq(ke.type, Syntax.Identifier)):
                convIdentAsStr(kve, ke)
            else:
                convExpr(kve, ke)
            # end if (line 218)
            convExpr(kve, ve)
        # end function <anonymous> (__fL_) (line 205)

        assrt(o, Syntax.ObjectExpression)
        ra = Range.fromAST(o)
        ce = o.properties
        cs = ObjectLiteralElement(ra)
        p.append(cs)
        ArrayList(ce).forEach(__fL_)
    # end function convObject (line 204)

    def convUnary(p, o):
        assrt(o, Syntax.UnaryExpression)
        ra = Range.fromAST(o)
        op = o.operator
        ar = o.argument
        ee = UniaryOperatorElement(op, ra)
        p.append(ee)
        convExpr(ee, ar)
    # end function convUnary (line 234)

    def convBinary(p, o):
        assrt(o, Syntax.BinaryExpression)
        ra = Range.fromAST(o)
        op = o.operator
        ee = BinaryOperatorElement(op, ra)
        p.append(ee)
        convExpr(ee, o.left)
        convExpr(ee, o.right)
    # end function convBinary (line 244)

    def convBinaryLogic(p, o):
        assrt(o, Syntax.LogicalExpression)
        ra = Range.fromAST(o)
        op = o.operator
        ee = BinaryLogicalElement(op, ra)
        p.append(ee)
        convExpr(ee, o.left)
        convExpr(ee, o.right)
    # end function convBinaryLogic (line 254)

    def convUpdate(p, o):
        assrt(o, Syntax.UpdateExpression)
        ra = Range.fromAST(o)
        op = o.operator
        ar = o.argument
        ee = UpdateElement(op, o.prefix, ra)
        p.append(ee)
        convExpr(ee, ar)
    # end function convUpdate (line 264)

    def convCond(p, o):
        assrt(o, Syntax.ConditionalExpression)
        ra = Range.fromAST(o)
        ee = TernaryOperatorElement(ra)
        p.append(ee)
        convExpr(ee, o.test)
        convExpr(ee, o.consequent)
        convExpr(ee, o.alternate)
    # end function convCond (line 274)

    def makeError(msg):
        def __fS_(p, o):
            ra = Range.fromAST(o)
            raise CompileError(msg, ra)
        # end function <anonymous> (__fS_) (line 285)

        return __fS_
    # end function makeError (line 284)

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
        # end if (line 307)
        res(p, o)
    # end function convExpr (line 293)

    def convExprAllowTuple(p, o):
        if __x_cb(__x_cb(o.type != Syntax.SequenceExpression) or __x_not(p.theGlobal.enableTupleSubscription)):
            convExpr(p, o)
            return
        # end if (line 314)
        ra = Range.fromAST(o)
        ce = o.expressions
        cs = TupleElement(ra)
        p.append(cs)
        convArgs(cs, ra, ce)
    # end function convExprAllowTuple (line 313)

    def convExprStat(p, o):
        assrt(o, Syntax.ExpressionStatement)
        ie = o.expression
        ra = Range.fromAST(o)
        if __x_cb(__x_cb(__x_eq(ie.type, Syntax.UnaryExpression)) and __x_eq(ie.operator, (u"delete"))):
            convDelete(p, ie)
        elif __x_cb(__x_eq(ie.type, Syntax.AssignmentExpression)):
            convAssign(p, ra, ie.left, ie.right, ie.operator)
        else:
            ee = ExpressionStatementElement(ra)
            p.append(ee)
            convExpr(ee, ie)
        # end if (line 329)
    # end function convExprStat (line 325)

    def convDelete(p, o):
        assrt(o, Syntax.UnaryExpression)
        ra = Range.fromAST(o)
        ee = DeleteElement(ra)
        ar = o.argument
        p.append(ee)
        convExpr(ee, ar)
    # end function convDelete (line 340)

    def convAssign(p, ra, l, r, op):
        if __x_cb(__x_eq(l.type, Syntax.ArrayPattern)):
            raise CompileError((u"destructing to array pattern is not supported yet"), ra)
        # end if (line 350)
        if __x_cb(__x_ne(l.type, Syntax.ObjectPattern)):
            ee = CompoundAssignElement(op, ra) if __x_cb(__x_ne(op, (u"="))) else AssignElement(ra)
            p.append(ee)
            convExpr(ee, l)
        else:
            if __x_cb(__x_ne(op, (u"="))):
                raise InternalError((u"compound destructuring assignment"))
            # end if (line 358)
            ee = AssignDestructElement(ra)
            p.append(ee)
            convPattern(ee, l, False)
        # end if (line 353)
        convExpr(ee, r)
    # end function convAssign (line 349)

    def convPattern(p, o, decl):
        ra = Range.fromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.ArrayPattern)):
            raise CompileError((u"destructuring to array pattern is not supported yet"), ra)
        elif __x_cb(__x_eq(o.type, Syntax.ObjectPattern)):
            convObjPattern(p, o, decl)
        else:
            raise InternalError((u"Unknown pattern type ") + o.type)
        # end if (line 370)
    # end function convPattern (line 368)

    def convObjPattern(p, o, decl):
        def __f14_(ie, k, a):
            __u_has.val = True
            ko = ie.key
            vo = ie.value
            ki = ie.kind
            rra = Range.fromAST(ie)
            if __x_cb(__x_eq(vo, None)):
                raise InternalError((u"null value object pattern"), ie)
            # end if (line 386)
            if __x_cb(__x_ne(ki, (u"init"))):
                raise InternalError((u"method in object pattern"), ie)
            # end if (line 389)
            kve = DestructPropertyElement(decl, convAttr(ko), rra)
            ee.append(kve)
            if __x_cb(__x_eq(vo.type, Syntax.AssignmentPattern)):
                raise CompileError((u"default value is not allowed in destructuring object"), rra)
            elif __x_cb(__x_cb(__x_eq(vo.type, Syntax.ArrayPattern)) or __x_eq(vo.type, Syntax.ObjectPattern)):
                convPattern(kve, vo, decl)
            elif __x_cb(decl):
                convVar(kve, vo, True)
            else:
                convExpr(kve, vo)
            # end if (line 394)
        # end function <anonymous> (__f14_) (line 380)

        __u_has = __x_var()
        assrt(o, Syntax.ObjectPattern)
        ra = Range.fromAST(o)
        ce = o.properties
        ee = DestructObjectElement(decl, ra)
        p.append(ee)
        __u_has.val = False
        ArrayList(ce).forEach(__f14_)
        if __x_cb(__x_not(__u_has.val)):
            raise CompileError((u"empty destructuring target is not allowed"), ra)
        # end if (line 413)
    # end function convObjPattern (line 379)

    def convVarDecl(p, o):
        def __f16_(oi, k, a):
            assrt(oi, Syntax.VariableDeclarator)
            rra = Range.fromAST(oi)
            l = oi.id
            r = oi.init
            if __x_cb(__x_eq(r, None)):
                ee = VarDeclaratorElement(rra)
                p.append(ee)
                ee.append(VarElement(ident(l), True, rra))
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
            # end if (line 424)
        # end function <anonymous> (__f16_) (line 419)

        assrt(o, Syntax.VariableDeclaration)
        ra = Range.fromAST(o)
        ki = o.kind
        if __x_cb(__x_ne(ki, (u"var"))):
            raise CompileError(ki + (u" declaration is not allowed"), ra)
        # end if (line 444)
        ArrayList(o.declarations).forEach(__f16_)
    # end function convVarDecl (line 418)

    def convChildren(p, el):
        def __f18_(ie, k, a):
            convStat(p, ie)
        # end function <anonymous> (__f18_) (line 451)

        ArrayList(el).forEach(__f18_)
    # end function convChildren (line 450)

    def convStatOrBlock(p, o, BodyClass):
        if __x_cb(__x_eq(o, None)):
            assrt(o, Syntax.BlockStatement)
        # end if (line 459)
        ra = Range.fromAST(o)
        be = BodyClass(ra)
        p.append(be)
        if __x_cb(__x_eq(o.type, Syntax.BlockStatement)):
            convChildren(be, o.body)
        else:
            convStat(be, o)
        # end if (line 465)
    # end function convStatOrBlock (line 458)

    def convCondExpr(p, o):
        ra = Range.fromAST(o)
        ee = ConditionElement(ra)
        p.append(ee)
        convExpr(ee, o)
    # end function convCondExpr (line 472)

    def convWhile(p, o):
        assrt(o, Syntax.WhileStatement)
        ra = Range.fromAST(o)
        we = WhileElement(ra)
        p.append(we)
        convCondExpr(we, o.test)
        convStatOrBlock(we, o.body, BodyElement)
    # end function convWhile (line 479)

    def convElse(p, o):
        if __x_cb(__x_eq(o, None)):
            return
        # end if (line 489)
        ra = Range.fromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.IfStatement)):
            elife = ElifElement(ra)
            p.append(elife)
            convCondExpr(elife, o.test)
            convStatOrBlock(elife, o.consequent, BodyElement)
            convElse(p, o.alternate)
        else:
            convStatOrBlock(p, o, ElseElement)
        # end if (line 493)
    # end function convElse (line 488)

    def convIf(p, o):
        assrt(o, Syntax.IfStatement)
        ra = Range.fromAST(o)
        ee = IfBlockElement(ra)
        p.append(ee)
        ie = IfElement(ra)
        ee.append(ie)
        convCondExpr(ie, o.test)
        convStatOrBlock(ie, o.consequent, BodyElement)
        convElse(ee, o.alternate)
    # end function convIf (line 504)

    def convReturn(p, o):
        assrt(o, Syntax.ReturnStatement)
        ra = Range.fromAST(o)
        re = ReturnElement(ra)
        p.append(re)
        a = o.argument
        if __x_cb(__x_ne(a, None)):
            convExpr(re, a)
        # end if (line 522)
    # end function convReturn (line 516)

    def convThrow(p, o):
        assrt(o, Syntax.ThrowStatement)
        ra = Range.fromAST(o)
        throw_ = ThrowElement(ra)
        p.append(throw_)
        convExpr(throw_, o.argument)
    # end function convThrow (line 527)

    def convBreak(p, o):
        assrt(o, Syntax.BreakStatement)
        ra = Range.fromAST(o)
        if __x_cb(__x_ne(o.label, None)):
            raise CompileError((u"labeled break is not implemented yet"), ra)
        # end if (line 538)
        p.append(BreakElement(ra))
    # end function convBreak (line 535)

    def convCont(p, o):
        assrt(o, Syntax.ContinueStatement)
        ra = Range.fromAST(o)
        if __x_cb(__x_ne(o.label, None)):
            raise CompileError((u"labeled continue is not implemented yet"), ra)
        # end if (line 547)
        p.append(ContinueElement(ra))
    # end function convCont (line 544)

    def convParam(p, o):
        ra = Range.fromAST(o)
        if __x_cb(__x_ne(o.type, Syntax.Identifier)):
            raise CompileError((u"destructuring parameter is not supported yet"), ra)
        # end if (line 555)
        ee = ParameterElement(ident(o), ra)
        p.append(ee)
    # end function convParam (line 553)

    def convCatch(tcf, o):
        assrt(o, Syntax.CatchClause)
        ra = Range.fromAST(o)
        een = __x_ne(o.param, None)
        catch_ = CatchElement(ra)
        tcf.append(catch_)
        if __x_cb(een):
            convParam(catch_, o.param)
        # end if (line 568)
        convStatOrBlock(catch_, o.body, BodyElement)
    # end function convCatch (line 562)

    def convTry(p, o):
        assrt(o, Syntax.TryStatement)
        ra = Range.fromAST(o)
        tcf = TryBlockElement(ra)
        p.append(tcf)
        convStatOrBlock(tcf, o.block, TryElement)
        if __x_cb(__x_ne(o.handler, None)):
            convCatch(tcf, o.handler)
        # end if (line 580)
        if __x_cb(__x_ne(o.finalizer, None)):
            convStatOrBlock(tcf, o.finalizer, FinallyElement)
        # end if (line 583)
    # end function convTry (line 574)

    def convStat(p, o):
        def __f1M_(*a):
            pass
        # end function <anonymous> (__f1M_) (line 589)

        emap = StringMap([[Syntax.EmptyStatement, __f1M_], [Syntax.ExpressionStatement, convExprStat], [Syntax\
.VariableDeclaration, convVarDecl], [Syntax.WhileStatement, convWhile], [Syntax.IfStatement, convIf], 
[Syntax.TryStatement, convTry], [Syntax.ThrowStatement, convThrow], [Syntax.ContinueStatement, convCont], 
[Syntax.BreakStatement, convBreak], [Syntax.ReturnStatement, convReturn], [Syntax.FunctionDeclaration, 
makeError((u"nested functions cannot be declared"))]])
        res = emap.get(o.type, None)
        if __x_cb(__x_eq(res, None)):
            raise InternalError((u"unknown statement ") + o.type, o)
        # end if (line 599)
        res(p, o)
    # end function convStat (line 588)

    def convFuncDecl(pfn, o, pub):
        assrt(o, Syntax.FunctionDeclaration)
        if __x_cb(o.expression):
            raise InternalError((u"Unexcepted function with single expression"), o)
        # end if (line 607)
        ra = Range.fromAST(o)
        ria = Range.fromAST(o.id)
        fn = FunctionDefinitionElement(ident(o.id), pub, ria, ra)
        pfn.functionDefinitions.append(fn)
        convFuncInner(fn, o)
    # end function convFuncDecl (line 605)

    def convFuncExpr(p, o):
        assrt(o, Syntax.FunctionExpression)
        ra = Range.fromAST(o)
        name = o.id
        fn = FunctionExpressionElement(None if __x_cb(__x_eq(name, None)) else ident(name), None if __x_cb(__x_eq(name, 
None)) else Range.fromAST(name), ra)
        p.theFunction.functionDefinitions.append(fn)
        convFuncInner(fn, o)
        p.append(VarElement.getFunctionExp(fn.tag))
    # end function convFuncExpr (line 617)

    def convFuncInnerDecl(fn, o):
        if __x_cb(__x_eq(o.type, Syntax.FunctionDeclaration)):
            convFuncDecl(fn, o, False)
        else:
            convStat(fn.body, o)
        # end if (line 629)
    # end function convFuncInnerDecl (line 628)

    def convFuncInner(fn, o):
        def __f1R_(p, k, v):
            rra = Range.fromAST(o)
            if __x_cb(__x_cb(__x_cb(__x_eq(p.type, Syntax.Identifier)) or __x_eq(p.type, Syntax.ArrayPattern)) or __x_eq(p\
.type, Syntax.ObjectPattern)):
                if __x_cb(opt):
                    raise CompileError((u"optional parameter may be placed only after required parameter"), rra)
                # end if (line 641)
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
            # end if (line 639)
        # end function <anonymous> (__f1R_) (line 637)

        def __f1S_(m, k, a):
            convFuncInnerDecl(fn, m)
        # end function <anonymous> (__f1S_) (line 659)

        ra = Range.fromAST(o)
        if __x_cb(o.isAsync):
            raise CompileError((u"async function is not supported yet"), ra)
        # end if (line 664)
        if __x_cb(o.generator):
            raise CompileError((u"generator function is not supported yet"), ra)
        # end if (line 667)
        pe = fn.parameters
        opt = False
        ArrayList(o.params).forEach(__f1R_)
        defs = fn.functionDefinitions
        body = fn.body
        expr = o.expression
        if __x_cb(expr):
            rra = Range.fromAST(o.body)
            re = ReturnElement(rra)
            body.append(re)
            convExpr(re, o.body)
        else:
            assrt(o.body, Syntax.BlockStatement)
            ArrayList(o.body.body).forEach(__f1S_)
        # end if (line 676)
    # end function convFuncInner (line 636)

    def convClassDecl(g, oc, pub):
        def __f1U_(oi, k, a):
            def __f1V_(ov, k, a):
                assrt(ov, Syntax.VariableDeclarator)
                rii = Range.fromAST(ov)
                ido = ov.id
                ino = ov.init
                ie = (StaticInitializerElement if __x_cb(s) else InstanceInitializerElement)(convAttr(ido), p, rii)
                (ce.staticInit if __x_cb(s) else ce.instanceInit).body.append(ie)
                if __x_cb(__x_ne(ino, None)):
                    convExpr(ie, ino)
                # end if (line 696)
            # end function <anonymous> (__f1V_) (line 689)

            ra = Range.fromAST(oi)
            ira = Range.fromAST(oi)
            if __x_cb(__x_eq(oi.accessModifier, (u"public"))):
                p = True
            elif __x_cb(__x_eq(oi.accessModifier, (u"private"))):
                p = False
            else:
                raise InternalError((u"unknown access modifier"))
            # end if (line 703)
            s = oi.isStatic
            od = oi.declaration
            if __x_cb(__x_cb(__x_eq(oi.type, Syntax.PropertyDeclaration)) and __x_eq(oi.kind, (u"var"))):
                assrt(od, Syntax.VariableDeclaration)
                ArrayList(od.declarations).forEach(__f1V_)
            elif __x_cb(__x_eq(oi.type, Syntax.MethodDeclaration)):
                assrt(od, Syntax.FunctionDeclaration)
                ria = Range.fromAST(od.id)
                me = MethodElement(ident(od.id), oi.kind, s, p, ria, ra)
                ce.functionDefinitions.append(me)
                convFuncInner(me, od)
            else:
                raise InternalError((u"unknown class member type"))
            # end if (line 712)
        # end function <anonymous> (__f1U_) (line 688)

        assrt(oc, Syntax.ClassDeclaration)
        ra = Range.fromAST(oc)
        ria = Range.fromAST(oc.id)
        su = oc.superClass
        ce = ClassElement(ident(oc.id), __x_ne(su, None), pub, ria, ra)
        g.classDefinitions.append(ce)
        cinit = ce.createClassInitElement()
        g.body.append(cinit)
        if __x_cb(__x_ne(su, None)):
            convExpr(cinit, su)
        # end if (line 734)
        bo = oc.body
        assrt(bo, Syntax.ClassBody)
        ArrayList(bo.body).forEach(__f1U_)
    # end function convClassDecl (line 687)

    def convTopDecl(g, o, pub, next):
        ra = Range.fromAST(o)
        if __x_cb(__x_eq(o.type, Syntax.FunctionDeclaration)):
            convFuncDecl(g, o, pub)
        elif __x_cb(__x_eq(o.type, Syntax.ClassDeclaration)):
            convClassDecl(g, o, pub)
        else:
            next(g, o)
        # end if (line 744)
    # end function convTopDecl (line 742)

    def convTop(g, o):
        def __f22_(m, k, a):
            def __f23_(g, o):
                raise InternalError((u"Illegal public declaration ") + o.type)
            # end function <anonymous> (__f23_) (line 755)

            if __x_cb(__x_eq(m.type, Syntax.PublicDeclaration)):
                convTopDecl(g, m.declaration, True, __f23_)
            else:
                convTopDecl(g, m, False, convFuncInnerDecl)
            # end if (line 759)
        # end function <anonymous> (__f22_) (line 754)

        assrt(o, Syntax.Program)
        ArrayList(o.body).forEach(__f22_)
    # end function convTop (line 753)

    # class definitions:

    __r0 = __x_imp((u".compat"))
    ArrayList = __r0.ArrayList
    __r1 = __x_imp((u".StringMap"))
    StringMap = __r1.StringMap
    __r2 = __x_imp((u".utils"))
    Range = __r2.Range
    InternalError = __r2.InternalError
    CompileError = __r2.CompileError
    __r3 = __x_imp((u".identifier"))
    Attribute = __r3.Attribute
    __r4 = __x_imp((u".syntax"))
    Syntax = __r4.Syntax
    __r5 = __x_imp((u".element"))
    ArgumentElement = __r5.ArgumentElement
    ArrayElement = __r5.ArrayElement
    AssignDestructElement = __r5.AssignDestructElement
    AssignElement = __r5.AssignElement
    AssignTempElement = __r5.AssignTempElement
    AttributeElement = __r5.AttributeElement
    BaseFunctionElement = __r5.BaseFunctionElement
    BinaryOperatorElement = __r5.BinaryOperatorElement
    BinaryLogicalElement = __r5.BinaryLogicalElement
    BlockElement = __r5.BlockElement
    BodyElement = __r5.BodyElement
    BooleanLiteralElement = __r5.BooleanLiteralElement
    BreakElement = __r5.BreakElement
    CallElement = __r5.CallElement
    CatchElement = __r5.CatchElement
    ClassElement = __r5.ClassElement
    ClassGroupElement = __r5.ClassGroupElement
    ClassInitElement = __r5.ClassInitElement
    ComplexLiteralElement = __r5.ComplexLiteralElement
    CompoundAssignElement = __r5.CompoundAssignElement
    ConditionElement = __r5.ConditionElement
    ContinueElement = __r5.ContinueElement
    DeleteElement = __r5.DeleteElement
    DestructGroupElement = __r5.DestructGroupElement
    DestructObjectElement = __r5.DestructObjectElement
    DestructPropertyElement = __r5.DestructPropertyElement
    DoWhileElement = __r5.DoWhileElement
    Element = __r5.Element
    ElifElement = __r5.ElifElement
    ElseElement = __r5.ElseElement
    ExpressionElement = __r5.ExpressionElement
    ExpressionStatementElement = __r5.ExpressionStatementElement
    FinallyElement = __r5.FinallyElement
    FunctionDefinitionElement = __r5.FunctionDefinitionElement
    FunctionElement = __r5.FunctionElement
    FunctionExpressionElement = __r5.FunctionExpressionElement
    FunctionGroupElement = __r5.FunctionGroupElement
    FundamentalLiteralElement = __r5.FundamentalLiteralElement
    GlobalElement = __r5.GlobalElement
    IfBlockElement = __r5.IfBlockElement
    IfElement = __r5.IfElement
    ImportElement = __r5.ImportElement
    InstanceGroupElement = __r5.InstanceGroupElement
    InstanceInitializerElement = __r5.InstanceInitializerElement
    ItemElement = __r5.ItemElement
    KeyValueElement = __r5.KeyValueElement
    LvalueElement = __r5.LvalueElement
    MagicCallElement = __r5.MagicCallElement
    MethodElement = __r5.MethodElement
    MethodGroupElement = __r5.MethodGroupElement
    MethodParameterGroupElement = __r5.MethodParameterGroupElement
    NotOperatorElement = __r5.NotOperatorElement
    NullLiteralElement = __r5.NullLiteralElement
    NullishCheckElement = __r5.NullishCheckElement
    NumberLiteralElement = __r5.NumberLiteralElement
    ObjectLiteralElement = __r5.ObjectLiteralElement
    ParameterAssignElement = __r5.ParameterAssignElement
    ParameterElement = __r5.ParameterElement
    ParameterGroupElement = __r5.ParameterGroupElement
    RestParameterElement = __r5.RestParameterElement
    ReturnElement = __r5.ReturnElement
    SequenceElement = __r5.SequenceElement
    SpreadElement = __r5.SpreadElement
    StatementElement = __r5.StatementElement
    StaticGroupElement = __r5.StaticGroupElement
    StaticInitializerElement = __r5.StaticInitializerElement
    StringLiteralElement = __r5.StringLiteralElement
    SuperElement = __r5.SuperElement
    TernaryOperatorElement = __r5.TernaryOperatorElement
    ThisElement = __r5.ThisElement
    ThrowElement = __r5.ThrowElement
    TryBlockElement = __r5.TryBlockElement
    TryElement = __r5.TryElement
    TupleElement = __r5.TupleElement
    UniaryOperatorElement = __r5.UniaryOperatorElement
    UpdateElement = __r5.UpdateElement
    VarDeclaratorElement = __r5.VarDeclaratorElement
    VarElement = __r5.VarElement
    WhileElement = __r5.WhileElement
# program end


__()
