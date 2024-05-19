var {ArrayList} = import('.compat');
var {StringMap} = import('.StringMap');
var {Range, InternalError, CompileError} = import('.utils');
var {Attribute} = import('.identifier');
var {Syntax} = import('.syntax');
var {ArgumentElement, ArrayElement, AssignDestructElement, AssignElement, AssignTempElement, AttributeElement, BaseFunctionElement, BinaryOperatorElement, BlockElement, BodyElement, BooleanLiteralElement, BreakElement, CallElement, CatchElement, ClassElement, ClassGroupElement, ClassInitElement, ComplexLiteralElement, CompoundAssignElement, ConditionElement, ContinueElement, DeleteElement, DestructGroupElement, DestructObjectElement, DestructPropertyElement, DoWhileElement, Element, ElifElement, ElseElement, ExpressionElement, ExpressionStatementElement, FinallyElement, FunctionDefinitionElement, FunctionElement, FunctionExpressionElement, FunctionGroupElement, FundamentalLiteralElement, GlobalElement, IfBlockElement, IfElement, ImportElement, InstanceGroupElement, InstanceInitializerElement, ItemElement, KeyValueElement, LvalueElement, MagicCallElement, MethodElement, MethodGroupElement, MethodParameterGroupElement, NotOperatorElement, NullLiteralElement, NullishCheckElement, NumberLiteralElement, ObjectLiteralElement, ParameterAssignElement, ParameterElement, ParameterGroupElement, RestParameterElement, ReturnElement, SequenceElement, SpreadElement, StatementElement, StaticGroupElement, StaticInitializerElement, StringLiteralElement, SuperElement, TernaryOperatorElement, ThisElement, ThrowElement, TryBlockElement, TryElement, TupleElement, UniaryOperatorElement, UpdateElement, VarDeclaratorElement, VarElement, WhileElement} = import('.element');

public function convertASTIR(ast:Object):GlobalElement {
    assrt(ast, Syntax.Program);
    var ra = Range.fromAST(ast);
    var ir = new GlobalElement(ra);
    convTop(ir, ast);
    return ir;
}

function convLiteral(p:Element, o:Object):void {
    var v = o.value;
    var r = o.raw;
    var ra = Range.fromAST(o);
    var el;
    if(v === null) {
        el = new NullLiteralElement(ra);
    } else if(typeof v === 'boolean') {
        el = new BooleanLiteralElement(v, ra);
    } else if(typeof v === 'string') {
        el = new StringLiteralElement(v, r, ra);
    } else if(typeof v === 'number') {
        el = new NumberLiteralElement(v, r, ra);
    } else {
        throw new InternalError('unknown literal type', ra, v);
    }
    p.append(el);
}

function convImag(p:Element, o:Object):void {
    var r = o.raw;
    var ra = Range.fromAST(o);
    var el = new ComplexLiteralElement(r, ra);
    p.append(el);
}

function assrt(o:Object, type:String):void {
    if(o === null) {
        throw new InternalError('expected ' + type + ' but null is met');
    }
    if(o.type !== type) {
        throw new InternalError('expected ' + type + ' but ' + o.type + ' is met');
    }
}

function assrt2(o:Object, type:*):void {
    if(o === null) {
        throw new InternalError('expected ' + type + ' but null is met');
    }
    var m = false;
    (new ArrayList(type)).forEach(function(s, k, a) {
        if(o.type === s) {
            m = true;
        }
    });
    if(!m) {
        throw new InternalError('expected ' + (new ArrayList(type)).get(0) + '-like but ' + o.type + ' is met');
    }
}

function convThis(p:Element, o:Object):void {
    assrt(o, Syntax.ThisExpression);
    var ra = Range.fromAST(o);
    p.append(new ThisElement(ra));
}

function ident(o):String {
    assrt(o, Syntax.Identifier);
    return o.name;
}

function convIdentAsStr(p:Element, o:Object):void {
    assrt(o, Syntax.Identifier);
    var n = ident(o);
    var ra = Range.fromAST(o);
    var se = new StringLiteralElement(n, '"' + n + '"', ra);
    p.append(se);
}

function convAttr(o:Object):Attribute {
    return new Attribute(ident(o), Range.fromAST(o));
}

function convVar(p:Element, o:Object, decl:Boolean = false):void {
    assrt(o, Syntax.Identifier);
    var ra = Range.fromAST(o);
    p.append(new VarElement(ident(o), decl, ra));
}

function convMember(p:Element, o:Object):void {
    assrt(o, Syntax.MemberExpression);
    var ra = Range.fromAST(o);
    var oo = o.object;
    var po = o.property;
    var cm = o.computed;
    var ee;
    if(cm) {
        ee = new ItemElement(ra);
    } else {
        ee = new AttributeElement(convAttr(po), ra);
    }
    p.append(ee);
    convExpr(ee, oo);
    if(cm) {
        convExpr(ee, po);
    }
}

function convSuper(p:Element, o:Object):void {
    assrt(o, Syntax.Super);
    var ra = Range.fromAST(o);
    p.append(new SuperElement(ra));
}

function convArgs(tus:SequenceElement, pra:Range, args):void {
    (new ArrayList(args)).forEach(function(ie, k, a) {
        if(ie === null) {
            throw new CompileError('Empty slot is not allowed', pra);
        }
        var ra = Range.fromAST(ie);
        if(ie.type === Syntax.SpreadElement) {
            var iee = new SpreadElement(ra);
            tus.append(iee);
            convExpr(iee, ie.argument);
        } else {
            convExpr(tus, ie);
        }
    });
}

function convDotAtCall(p:Element, o:Object):void {
    assrt2(o, [Syntax.CallExpression, Syntax.NewExpression]);
    var ra = Range.fromAST(o);
    if(o.type === Syntax.NewExpression) {
        throw new CompileError('at-function can only be callee', ra);
    }
    var ce = o.callee;
    assrt(ce, Syntax.DotAtExpression);
    var me = ce.method;
    var obj = ce.object;
    var argv = o.arguments;
    var da = new MagicCallElement(ident(me), ra);
    p.append(da);

    convExpr(da, obj);

    var arge = new ArgumentElement(null);
    da.append(arge);
    convArgs(arge, ra, argv);
}

function convImport(p:Element, o:Object):void {
    assrt(o, Syntax.Import);
    var ra = Range.fromAST(o);
    var cs = new ImportElement(ra);
    p.append(cs);
}

function convCall(p:Element, o:Object):void {
    assrt2(o, [Syntax.CallExpression, Syntax.NewExpression]);
    var ra = Range.fromAST(o);
    var argv = o.arguments;
    var ce = o.callee;
    if(ce.type === Syntax.DotAtExpression) {
        convDotAtCall(p, o);
    } else {
        var cs = new CallElement(ra);
        p.append(cs);

        convExpr(cs, ce);

        var arge = new ArgumentElement(null);
        cs.append(arge);
        convArgs(arge, ra, argv);
    }
}

function convArray(p:Element, o:Object):void {
    assrt(o, Syntax.ArrayExpression);
    var ra = Range.fromAST(o);
    var ce = o.elements;
    var cs = new ArrayElement(ra);
    p.append(cs);
    convArgs(cs, ra, ce);
}

function convObject(p:Element, o:Object):void {
    assrt(o, Syntax.ObjectExpression);
    var ra = Range.fromAST(o);
    var ce = o.properties;
    var cs = new ObjectLiteralElement(ra);
    p.append(cs);

    (new ArrayList(ce)).forEach(function(ie, k, a) {
        var ke = ie.key;
        var ve = ie.value;
        var ki = ie.kind;
        var rra = Range.fromAST(ie);
        if(ve === null) {
            throw new InternalError('null value dict init', ie);
        }
        if(ki !== 'init') {
            throw new CompileError('accessor or method in object expression is not allowed', rra);
        }
        var kve = new KeyValueElement(rra);
        cs.append(kve);

        // key
        if(ke.type === Syntax.Identifier) {
            convIdentAsStr(kve, ke);
        } else {
            convExpr(kve, ke);
        }
        // value
        convExpr(kve, ve);
    });
}

function convUnary(p:Element, o:Object):void {
    assrt(o, Syntax.UnaryExpression);
    var ra = Range.fromAST(o);
    var op = o.operator;
    var ar = o.argument;
    var ee = new UniaryOperatorElement(op, ra);
    p.append(ee);
    convExpr(ee, ar);
}

function convBinary(p:Element, o:Object):void {
    assrt2(o, [Syntax.BinaryExpression, Syntax.LogicalExpression]);
    var ra = Range.fromAST(o);
    var op = o.operator;
    var ee = new BinaryOperatorElement(op, ra);
    p.append(ee);
    convExpr(ee, o.left);
    convExpr(ee, o.right);
}

function convUpdate(p:Element, o:Object):void {
    assrt(o, Syntax.UpdateExpression);
    var ra = Range.fromAST(o);
    var op = o.operator;
    var ar = o.argument;
    var ee = new UpdateElement(op, o.prefix, ra);
    p.append(ee);
    convExpr(ee, ar);
}

function convCond(p:Element, o:Object):void {
    assrt(o, Syntax.ConditionalExpression);
    var ra = Range.fromAST(o);
    var ee = new TernaryOperatorElement(ra);
    p.append(ee);
    convExpr(ee, o.test);
    convExpr(ee, o.consequent);
    convExpr(ee, o.alternate);
}

function makeError(msg:String) {
    return function (p:Element, o:Object):void {
        var ra = Range.fromAST(o);
        throw new CompileError(msg, ra);
    }
}

function convExpr(p:Element, o:Object):void {
    var emap = new StringMap(
        [
            [Syntax.Literal, convLiteral],
            [Syntax.ComplexLiteral, convImag],
            [Syntax.ThisExpression, convThis],
            [Syntax.Identifier, convVar],
            [Syntax.MemberExpression, convMember],
            [Syntax.Super, convSuper],
            [Syntax.CallExpression, convCall],
            [Syntax.NewExpression, convCall],
            [Syntax.ArrayExpression, convArray],
            [Syntax.ObjectExpression, convObject],
            [Syntax.UnaryExpression, convUnary],
            [Syntax.BinaryExpression, convBinary],
            [Syntax.LogicalExpression, convBinary],
            [Syntax.UpdateExpression, convUpdate],
            [Syntax.ConditionalExpression, convCond],
            [Syntax.FunctionExpression, convFuncExpr],
            [Syntax.Import, convImport],

            [Syntax.SequenceExpression, makeError('comma operator is not allowed')],
            [Syntax.DotAtExpression, makeError('at-function can only be callee')],
            [Syntax.ArrowFunctionExpression, makeError('arrow function is not allowed')],
            [Syntax.AssignmentExpression, makeError('assignment must be standalone statement')],
            [Syntax.YieldExpression, makeError('generator is not implemented yet')],
            [Syntax.AwaitExpression, makeError('async function is not implemented yet')],
            [Syntax.TemplateElement, makeError('templated string is not implemented yet')],
            [Syntax.TemplateLiteral, makeError('templated string is not implemented yet')],
        ]
    );
    var res = emap.get(o.type, null);
    if(res === null) {
        throw new InternalError('unknown expression ' + o.type, o);
    }
    res(p, o);
}

function convExprStat(p:Element, o:Object):void {
    assrt(o, Syntax.ExpressionStatement);
    var ie = o.expression;
    var ra = Range.fromAST(o);
    if(ie.type === Syntax.UnaryExpression && ie.operator === 'delete') {
        convDelete(p, ie);
    } else if(ie.type === Syntax.AssignmentExpression) {
        convAssign(p, ra, ie.left, ie.right, ie.operator);
    } else {
        var ee = new ExpressionStatementElement(ra);
        p.append(ee);
        convExpr(ee, ie);
    }
}

function convDelete(p:Element, o:Object):void {
    assrt(o, Syntax.UnaryExpression);
    var ra = Range.fromAST(o);
    var ee = new DeleteElement(ra);
    var ar = o.argument;
    p.append(ee);
    convExpr(ee, ar);
}

function convAssign(p:Element, ra:Range, l:Object, r:Object, op:String):void {
    if(l.type === Syntax.ArrayPattern) {
        throw new CompileError('destructing to array pattern is not supported yet', ra);
    }
    var ee;
    if(l.type !== Syntax.ObjectPattern) {
        // normal assign
        ee = op !== '=' ? new CompoundAssignElement(op, ra) : new AssignElement(ra);
        p.append(ee);
        convExpr(ee, l);
    } else {
        if(op !== '=') {
            throw new InternalError('compound destructuring assignment');
        }
        ee = new AssignDestructElement(ra);
        p.append(ee);
        convPattern(ee, l, false);
    }
    convExpr(ee, r);
}

function convPattern(p:Element, o:Object, decl:Boolean):void {
    var ra = Range.fromAST(o);
    if(o.type === Syntax.ArrayPattern) {
        throw new CompileError('destructuring to array pattern is not supported yet', ra);
    } else if(o.type === Syntax.ObjectPattern) {
        convObjPattern(p, o, decl);
    } else {
        throw new InternalError('Unknown pattern type ' + o.type);
    }
}

function convObjPattern(p:Element, o:Object, decl:Boolean):void {
    assrt(o, Syntax.ObjectPattern);
    var ra = Range.fromAST(o);
    var ce = o.properties;
    var ee = new DestructObjectElement(decl, ra);
    p.append(ee);
    var has = false;
    (new ArrayList(ce)).forEach(function(ie, k, a) {
        has = true;
        var ko = ie.key;
        var vo = ie.value;
        var ki = ie.kind;
        var rra = Range.fromAST(ie);
        if(vo === null) {
            throw new InternalError('null value object pattern', ie);
        }
        if(ki !== 'init') {
            throw new InternalError('method in object pattern', ie);
        }

        var kve = new DestructPropertyElement(decl, convAttr(ko), rra);
        ee.append(kve);

        if(vo.type === Syntax.AssignmentPattern) {
            throw new CompileError('default value is not allowed in destructuring object', rra);
        } else if(vo.type === Syntax.ArrayPattern || vo.type === Syntax.ObjectPattern) {
            convPattern(kve, vo, decl);
        } else if(decl) {
            convVar(kve, vo, true);
        } else {
            convExpr(kve, vo);
        }
    });

    if(!has) {
        throw new CompileError('empty destructuring target is not allowed', ra);
    }
}

function convVarDecl(p:Element, o:Object):void {
    assrt(o, Syntax.VariableDeclaration);
    var ra = Range.fromAST(o);
    var ki = o.kind;
    if(ki !== 'var') {
        throw new CompileError(ki + ' declaration is not allowed', ra);
    }
    (new ArrayList(o.declarations)).forEach(function(oi, k, a) {
        assrt(oi, Syntax.VariableDeclarator);
        var rra = Range.fromAST(oi);
        var l = oi.id;
        var r = oi.init;
        var ee;
        if(r === null) {
            ee = new VarDeclaratorElement(rra);
            p.append(ee);
            ee.append(new VarElement(ident(l), true, rra));
        } else if (l.type === Syntax.Identifier) {
            ee = new AssignElement(rra);
            p.append(ee);
            convVar(ee, l, true);
            convExpr(ee, r);
        } else {
            ee = new AssignDestructElement(ra);
            p.append(ee);
            convPattern(ee, l, true);
            convExpr(ee, r);
        }
    });
}

function convChildren(p:Element, el) {
    (new ArrayList(el)).forEach(function(ie, k, a) {
        convStat(p, ie);
    });
}

function convStatOrBlock(p:Element, o:Object, BodyClass:Class):void {
    if(o === null) {
        assrt(o, Syntax.BlockStatement);
    }
    var ra = Range.fromAST(o);
    var be = new BodyClass(ra);
    p.append(be);
    if(o.type === Syntax.BlockStatement) {
        convChildren(be, o.body);
    } else {
        convStat(be, o);
    }
}

function convCondExpr(p:Element, o:Object):void {
    var ra = Range.fromAST(o);
    var ee = new ConditionElement(ra);
    p.append(ee);
    convExpr(ee, o);
}

function convWhile(p:Element, o:Object):void {
    assrt(o, Syntax.WhileStatement);
    var ra = Range.fromAST(o);
    var we = new WhileElement(ra);
    p.append(we);
    convCondExpr(we, o.test);
    convStatOrBlock(we, o.body, BodyElement);
}

function convElse(p:Element, o:Object):void {
    if(o === null) {
        return
    }
    var ra = Range.fromAST(o);
    if(o.type === Syntax.IfStatement) {
        var elife = new ElifElement(ra);
        p.append(elife);
        convCondExpr(elife, o.test);
        convStatOrBlock(elife, o.consequent, BodyElement);
        convElse(p, o.alternate);
    } else {
        convStatOrBlock(p, o, ElseElement);
    }
}

function convIf(p:Element, o:Object):void {
    assrt(o, Syntax.IfStatement);
    var ra = Range.fromAST(o);
    var ee = new IfBlockElement(ra);
    p.append(ee);
    var ie = new IfElement(ra);
    ee.append(ie);
    convCondExpr(ie, o.test);
    convStatOrBlock(ie, o.consequent, BodyElement);
    convElse(ee, o.alternate);
}

function convReturn(p:Element, o:Object):void {
    assrt(o, Syntax.ReturnStatement);
    var ra = Range.fromAST(o);
    var re = new ReturnElement(ra);
    p.append(re);
    var a = o.argument;
    if(a !== null) {
        convExpr(re, a);
    }
}

function convThrow(p:Element, o:Object):void {
    assrt(o, Syntax.ThrowStatement);
    var ra = Range.fromAST(o);
    var throw_ = new ThrowElement(ra);
    p.append(throw_);
    convExpr(throw_, o.argument);
}

function convBreak(p:Element, o:Object):void {
    assrt(o, Syntax.BreakStatement);
    var ra = Range.fromAST(o);
    if(o.label !== null) {
        throw new CompileError('labeled break is not implemented yet', ra);
    }
    p.append(new BreakElement(ra));
}

function convCont(p:Element, o:Object):void {
    assrt(o, Syntax.ContinueStatement);
    var ra = Range.fromAST(o);
    if(o.label !== null) {
        throw new CompileError('labeled continue is not implemented yet', ra);
    }
    p.append(new ContinueElement(ra));
}

function convParam(p:Element, o:Object):void {
    var ra = Range.fromAST(o);
    if(o.type !== Syntax.Identifier) {
        throw new CompileError('destructuring parameter is not supported yet', ra);
    }
    var ee = new ParameterElement(ident(o), ra);
    p.append(ee);
}

function convCatch(tcf:Element, o:Object):void {
    assrt(o, Syntax.CatchClause);
    var ra = Range.fromAST(o);
    var een = o.param !== null;
    var catch_ = new CatchElement(ra);
    tcf.append(catch_);
    if(een) {
        convParam(catch_, o.param);
    }
    convStatOrBlock(catch_, o.body, BodyElement);
}

function convTry(p:Element, o:Object):void {
    assrt(o, Syntax.TryStatement);
    var ra = Range.fromAST(o);
    var tcf = new TryBlockElement(ra);
    p.append(tcf);
    convStatOrBlock(tcf, o.block, TryElement);
    if(o.handler !== null) {
        convCatch(tcf, o.handler);
    }
    if(o.finalizer !== null) {
        convStatOrBlock(tcf, o.finalizer, FinallyElement);
    }
}

function convStat(p:Element, o:Object):void {
    var emap = new StringMap(
        [
            [Syntax.EmptyStatement, function(...a) {}],
            [Syntax.ExpressionStatement, convExprStat],
            [Syntax.VariableDeclaration, convVarDecl],
            [Syntax.WhileStatement, convWhile],
            [Syntax.IfStatement, convIf],
            [Syntax.TryStatement, convTry],
            [Syntax.ThrowStatement, convThrow],
            [Syntax.ContinueStatement, convCont],
            [Syntax.BreakStatement, convBreak],
            [Syntax.ReturnStatement, convReturn],
            [Syntax.FunctionDeclaration, makeError('nested functions cannot be declared')],
        ]
    );
    var res = emap.get(o.type, null);
    if(res === null) {
        throw new InternalError('unknown statement ' + o.type, o);
    }
    res(p, o);
}

function convFuncDecl(pfn:BaseFunctionElement, o:Object, pub:Boolean):void {
    assrt(o, Syntax.FunctionDeclaration);
    if(o.expression) {
        throw new InternalError('Unexcepted function with single expression', o);
    }
    var ra = Range.fromAST(o);
    var ria = Range.fromAST(o.id);
    var fn = new FunctionDefinitionElement(ident(o.id), pub, ria, ra);
    pfn.functionDefinitions.append(fn);
    convFuncInner(fn, o);
}

function convFuncExpr(p:Element, o:Object):void {
    assrt(o, Syntax.FunctionExpression);
    var ra = Range.fromAST(o);
    var name = o.id;
    // put the actual function into declaration area
    var fn = new FunctionExpressionElement(
        name === null ? null : ident(name),
        name === null ? null : Range.fromAST(name),
        ra
    );
    p.theFunction.functionDefinitions.append(fn);
    convFuncInner(fn, o);
    // put the function tag here
    p.append(VarElement.getFunctionExp(fn.tag));
}

function convFuncInnerDecl(fn:BaseFunctionElement, o:Object):void {
    if(o.type === Syntax.FunctionDeclaration) {
        convFuncDecl(fn, o, false);
    } else {
        convStat(fn.body, o);
    }
}

function convFuncInner(fn:FunctionElement, o:Object):void {
    var ra = Range.fromAST(o);
    if(o.isAsync) {
        throw new CompileError('async function is not supported yet', ra);
    }
    if(o.generator) {
        throw new CompileError('generator function is not supported yet', ra);
    }

    var pe = fn.parameters;
    var opt = false;
    (new ArrayList(o.params)).forEach(function(p, k, v) {
        var rra = Range.fromAST(o);
        var ie;
        if(p.type === Syntax.Identifier || p.type === Syntax.ArrayPattern || p.type === Syntax.ObjectPattern) {
            if(opt) {
                throw new CompileError('optional parameter may be placed only after required parameter', rra);
            }
            convParam(pe, p);
        } else if(p.type === Syntax.AssignmentPattern) {
            ie = new ParameterAssignElement(rra);
            pe.append(ie);

            convParam(ie, p.left);
            convExpr(ie, p.right);
        } else if(p.type === Syntax.RestElement) {
            ie = new RestParameterElement(rra);
            pe.append(ie);
            convParam(ie, p.argument);
        } else {
            throw new InternalError('unknown parameter ' + p.type, p);
        }
    });;

    var defs = fn.functionDefinitions;
    var body = fn.body;
    var expr = o.expression;
    if(expr) {
        var rra = Range.fromAST(o.body);
        var re = new ReturnElement(rra);
        body.append(re);
        convExpr(re, o.body);
    } else {
        assrt(o.body, Syntax.BlockStatement);
        (new ArrayList(o.body.body)).forEach(function(m, k, a) {
            convFuncInnerDecl(fn, m);
        });
    }
}

function convClassDecl(g:GlobalElement, oc:Object, pub:Boolean):void {
    assrt(oc, Syntax.ClassDeclaration);
    var ra = Range.fromAST(oc);
    var ria = Range.fromAST(oc.id);
    var su = oc.superClass;
    var ce:ClassElement = new ClassElement(ident(oc.id), su !== null, pub, ria, ra);
    g.classDefinitions.append(ce);
    var cinit = ce.createClassInitElement();
    g.body.append(cinit);
    if(su !== null) {
        convExpr(cinit, su);
    }
    var bo = oc.body;
    assrt(bo, Syntax.ClassBody);
    (new ArrayList(bo.body)).forEach(function(oi, k, a) {
        var ra = Range.fromAST(oi);
        var p, s, ira = Range.fromAST(oi);
        if(oi.accessModifier === 'public') {
            p = true;
        } else if(oi.accessModifier === 'private') {
            p = false;
        } else {
            throw new InternalError('unknown access modifier');
        }
        s = oi.isStatic;
        var od = oi.declaration;
        if(oi.type === Syntax.PropertyDeclaration && oi.kind === 'var') {
            assrt(od, Syntax.VariableDeclaration);
            (new ArrayList(od.declarations)).forEach(function(ov, k, a) {
                assrt(ov, Syntax.VariableDeclarator);
                var rii = Range.fromAST(ov);
                var ido = ov.id;
                var ino = ov.init;
                var ie = new (s ? StaticInitializerElement : InstanceInitializerElement)(convAttr(ido), p, rii);
                (s ? ce.staticInit : ce.instanceInit).body.append(ie);
                if(ino !== null) {
                    // optional initializer
                    convExpr(ie, ino);
                }
            });
        } else if(oi.type === Syntax.MethodDeclaration) {
            assrt(od, Syntax.FunctionDeclaration);
            var ria = Range.fromAST(od.id);
            var me = new MethodElement(ident(od.id), oi.kind, s, p, ria, ra);
            ce.functionDefinitions.append(me);
            convFuncInner(me, od);
        } else {
            throw new InternalError('unknown class member type');
        }
    });
}

function convTopDecl(g:GlobalElement, o:Object, pub:Boolean, next:Function) {
    var ra = Range.fromAST(o);
    if(o.type === Syntax.FunctionDeclaration) {
        convFuncDecl(g, o, pub);
    } else if(o.type === Syntax.ClassDeclaration) {
        convClassDecl(g, o, pub);
    } else {
        next(g, o);
    }
}

function convTop(g:GlobalElement, o:Object):void {
    assrt(o, Syntax.Program);
    (new ArrayList(o.body)).forEach(function(m, k, a) {
        if(m.type === Syntax.PublicDeclaration) {
            convTopDecl(g, m.declaration, true, function(g, o) {
                throw new InternalError('Illegal public declaration ' + o.type);
            });
        } else {
            convTopDecl(g, m, false, convFuncInnerDecl);
        }
    });
}

