var {ArrayList, StrTool, printf} = import('.compat');
var {StringMap} = import('.StringMap');
var {CompileError, ElementPattern, Range, ConflictError, InternalError, XMLDumper} = import('.utils');
var {SymbolTree, SymbolTreeNode} = import('.symboltree');
var {Attribute, BuiltinVar, ClassFieldDescriptor, ClassTag, FunctionExpTag, FunctionTag, GlobalVar, Identifier, LocalVar, MethodTag, TempVar, Variable} = import('.identifier');
var {LineNumber, LineWriter, PyGenerator} = import('.pygen');

// please DO NOT delete the headers like this
// #########= Element

/**
 * Base class of the statement in intermediate representation
 * The term "element" is used to distinguish between it and AST(from parser)'s
 */
public class Element {
    private static var st:SymbolTree = new SymbolTree();

    // for symbol tree library
    public var _symbolTreeNode:SymbolTreeNode = null;

    /**
    * The range of this in the source code
    */
    public var range:Range = null;

    /**
    * the name of this element
    */
    public function get typeName():String {
        return 'abstract';
    }

    /** 
     * check if this is a complex expression
     * for the other elements, return true
     */
    public function get complex():Boolean {
        return true;
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     * for statement, returns false
     */
    public function get constantOnly():Boolean {
        return false;
    }

    /**
     * check if if this is only a temp variable, 
     * or other expressions without any side-effect, such as literals
     * for statement, returns false
     */
    public function get tempVarOnly():Boolean {
        return false;
    }

    /**
     * the parent element of this
     */
    public function get parent():Element {
        return Element.st.parent(this);
    }

    /**
     * the previous sibling element of this
     */
    public function get previousSibling():Element {
        return Element.st.previousSibling(this);
    }

    /**
     * the next sibling element of this
     */
    public function get nextSibling():Element {
        return Element.st.nextSibling(this);
    }

    /**
     * the statement element this is in
     *
     * 该元素所在的完整语句
     * 所谓完整语句是指在语句的前后插入另一条完整语句不会破坏元素的结构
     * 例如, if, 函数定义, 表达式语句都属于完整语句, 而函数体, 部分表达式则不属于完整语句.
     */
    public function get theStatement():Element {
        return null;
    }

    /**
     * the function element this is in
     *
     * 该元素所在的函数
     * 在此"函数"指的是能够形成变量作用域的块, 详见BaseFunctionElement.
     */
    public function get theFunction():BaseFunctionElement {
        return this.parent.theFunction;
    }

    /**
     * the class element this is in
     *
     * 该元素所在的类
     * 如果该语句不在类里面(比如全局函数), 那就上溯到global最终返回null
     */
    public function get theClass():ClassElement {
        return this.parent.theClass;
    }

    /**
     * the global element this is in
     *
     * 该元素所在的全局
     */
    public function get theGlobal():GlobalElement {
        return this.parent.theGlobal;
    }

    /**
     * true if this can be refered here
     *
     * 只有方法才会形成this的作用域, 全局没有this, 即没有globalThis
     * 和js不同, 一般的函数不再形成自身的this作用域
     */
    public function get allowThis():Boolean {
        return this.parent.allowThis;
    }

    /**
     * true if super can be refered here
     */
    public function get allowSuper():Boolean {
        return this.parent.allowSuper;
    }

    /**
     * true if super() can be used here
     *
     * super()只能是独立的语句, 只有有超类的构造函数才能使用super()调用
     * 而且super()不能出现在块中
     */
    public function get allowSuperCall():Boolean {
        return false;
    }

    /**
     * removes the element from the tree
     */
    public function remove():void {
        Element.st.remove(this);
    }

    /**
     * the first child.
     */
    public function get firstChild():Element {
        return Element.st.firstChild(this);
    }

    /**
     * the last child.
     */
    public function get lastChild():Element {
        return Element.st.lastChild(this);
    }

    /**
     * Insert content before this element.
     * the elements will be removed from its original place
     */
    public function before(e:Element):void {
        // insertBefore(referenceObject, newObject)
        // `newObject` is now the previous sibling of `referenceObject`.
        // SymbolTree will not remove the element automatically
        e.remove();
        Element.st.insertBefore(this, e);
    }

    /**
     * Insert content after this element.
     * the elements will be removed from its original place
     */
    public function after(e:Element):void {
        // insertAfter(referenceObject, newObject)
        // `newObject` is now the next sibling of `referenceObject`.
        e.remove();
        Element.st.insertAfter(this, e);
    }

    /**
     * Insert content to the end of the element.
     * the elements will be removed from its original place
     * @param {Element} elements, the result has the same sequence
     */
    public function append(e:Element):void {
        // appendChild(referenceObject, newObject)
        // `newObject` is now the last child of `referenceObject`.
        e.remove();
        Element.st.appendChild(this, e);
    }

    /**
     * Insert content to the beginning of the element.
     * the elements will be removed from its original place
     * @param {Element} elements, the result has the same sequence
     */
    public function prepend(e:Element):void {
        // prependChild(referenceObject, newObject)
        // `newObject` is now the first child of `referenceObject`.
        e.remove();
        Element.st.prependChild(this, e);
    }

    /**
     * replace this with e.
     * @param {Element} elements, the new element
     */
    public function replaceWith(e:Element):void {
        if(this === e) {
            return;
        }
        this.before(e);
        this.remove();
    }

    /**
     * iterate the children
     * @param {Function} callback(item, index, self)
     * callback can return boolean false to stop the iteration
     */
    public function forEachChild(callback):void {
        var v = new ArrayList();
        var it = Element.st.childrenIterator(this, false);
        var k = 0;
        // cache the elements at first
        while(true) {
            var nx = it.next();
            if(nx.done) {
                break;
            }
            v.push(nx.value);
            k++;
        }
        var self = this;
        v.forEach(function(e, k, a) {
            return callback(e, k, self)
        });
    }

    /**
     * the required struture of this
     *
     * 返回该元素的合法子元素列表, 用于结构检查.
     * 列表的成员必须是ElementPattern, 其中每个元素都是贪心匹配的, 也就是尽可能匹配更多的子元素.
     * 如果需要更复杂的结构检查, 可以返回null, 此时须超控checkStruct函数.
     */
    public function get structList():ArrayList {
        // 默认不允许含有子元素
        return new ArrayList();
    }

    /**
     * check the struture of this
     */
    public function checkStruct():void {
        var sl = this.structList;
        var k = 0;
        this.forEachChild(function(e, n, s) {
            while(true) {
                if(k === sl.length) {
                    throw new InternalError('malformed structure in ' + s.typeName + ', expected the end of element, but ' + e.typeName + ' is met;');
                }
                var p = sl.get(k);
                if(p.meet(e, s.typeName)) {
                    return;
                }
                k++;
            }
        });
        if(sl.length === 0) {
            return;
        }
        while(k < sl.length) {
            sl.get(k).meetEOF(this.typeName);
            k++;
        }
    }

    /**
     * check the struture of the elements recursively
     */
    public function checkAllStructure():void {
        this.checkStruct();
        this.forEachChild(function(e, k, s) {
            e.checkAllStructure();
        });
    }

    /**
     * pre-stage1
     * declare this variable
     * 
     * 声明变量, 因为变量声明是提升的, 所以在正式进行变量检查前需要先处理变量声明
     */
    public function declareVariable():void {
        this.forEachChild(function(e, k, t) {
            e.declareVariable();
        });
    }

    /**
     * walk stage 1
     *
     * 扫描全部变量, 检查变量是否正确声明, 有无需要建立闭包
     */
    public function checkVariables():void {
        this.forEachChild(function(e, k, t) {
            e.checkVariables();
        });
    }

    /**
     * pre-stage 2
     *
     * 将部分表达式转换成函数
     * 该项在simplifyExpressions之前运行, 只有少数元素需要进行此操作, 例如, instanceof运算符需要转换成函数
     * 对于表达式, 如果子表达式是简单的, 也必须向下层传递
     */
    public function functionalize():void {
        this.forEachChild(function(e, k, t) {
            e.functionalize();
        });
    }

    /**
     * walk stage 2
     *
     * 简化表达式, 提升复杂表达式, 使之能被py表示
     * 对于表达式, 如果子表达式是简单的, 可以直接返回而不用再触发子表达式的该项操作
     */
    public function simplifyExpressions():void {
        this.forEachChild(function(e, k, t) {
            e.simplifyExpressions();
        });
    }

    /**
     * dump to XML code
     */
    public function dump(ctx:XMLDumper):void {
        ctx.tag(this.typeName);
        ctx.range(this.range);
        ctx.finalize(this);
    }

    /**
    * generate python code
    *
    * 生成Python代码
    */
    public function generatePython(ctx:PyGenerator):void {
        throw new InternalError('function generatePython in ' + this.typeName + " element is abstract");
    }

    /**
    * the constructor
    */
    public function Element(range:Range) {
        Element.st.initialize(this);
        this.range = range;
    }
}

// #########= ExpressionElement

/**
 * base class of the expressions
 *
 * 表达式的基类, 表达式元素一般具有比较严格的结构限制, 且不能作为独立语句出现
 */
public class ExpressionElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'exprabstr';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        var c = false;
        this.forEachChild(function(e, i, s) {
            if(e.complex) {
                c = true;
                return false;
            }
        });
        return c;
    }

    /**
     * the statement element this is in
     */
    override public function get theStatement():Element {
        return this.parent.theStatement;
    }

    /**
     * replace this with a temporary variable
     *
     * 将自身替换为临时变量, 返回临时变量赋值语句
     * 如果自身是无副作用的表达式, 可以不替换并返回null
     * 如果必须替换, 可将可选参数optional设为false
     */
    public function replaceWithTemp(optional = true):AssignTempElement {
        if(optional && this.tempVarOnly) {
            return null;
        }
        var ate = new AssignTempElement(this.theFunction.allocTempVar());
        this.replaceWith(ate.getLeftElement());
        ate.append(this);
        return ate;
    }

    /**
     * insert a AssignTempElement before the statement this is in and simplify it
     *
     * 将临时变量赋值语句插入该表达式所在语句之前, 并将其简化
     * 这个一般是配合replaceWithTemp来完成的
     * e可以是null, 此时该函数将直接返回, 用于表达式本身无副作用, 无须析出的情况
     */
    public function insertTempAssign(e:AssignTempElement):void {
        if(e === null) {
            return;
        }
        this.theStatement.before(e);
        e.simplifyExpressions();
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     *
     * 由于表达式是行内元素, 因此不能一次向输出中写入一行, 而是要写入字符
     * 向writer里写入对应的python代码, contchr是续行符, 如果在括号内可以是空字符串
     * 把contchr设成false可以禁止子元素换行, 除非子元素无视这个
     *
     * 子元素必须保证自己有比父元素更高的优先级, 如果子元素的优先级不够, 就要加上括号
     * parentType表示了父元素的性质, 可以省略, 此时为默认值0
     *   - 0: 总是能够保证子元素优先, 比如表达式顶层, 括号内部, 或以逗号分隔的参数
     *   - 1: 条件运算符(?:)
     *   - 2: 逻辑运算符
     *   - 3: 比较运算符
     *   - 4: 按位或(|)
     *   - 5: 按位异或(^)
     *   - 6: 按位与(&)
     *   - 7: 移位(<<, >>)
     *   - 8: 加减(+, -)
     *   - 9: 乘(*). 注意除以和余数用函数替换了
     *   - 10: 单目运算符(+, -, ~)
     *   - 11: 幂(**)
     *   - 12: 成员的基值(object.attribute), 被调函数(callee())
     */
    public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        throw new InternalError('function generatePython in ' + this.typeName + " element is abstract");
    }

    /**
    * the constructor
    */
    public function ExpressionElement(range:Range) {
        super(range);
    }
}

// #########= SequenceElement

/**
 * base class for expressions containing a series of things
 * including ArrayLiteral, CallExpression and sequence expression
 *
 * 存在线性列表的表达式(比如数组字面量, 函数调用参数)的基类
 * 注意不再允许使用序列表达式(以逗号分隔的表达式)
 */
public class SequenceElement extends ExpressionElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'sequence-abstract';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 0, true)]);
    }

    /**
     * true if there is a spread element inside this
     */
    public function get hasSpread():Boolean {
        var f = false;
        this.forEachChild(function(e, k, s) {
            if(e instanceof SpreadElement) {
                f = true;
                return false;
            }
        });
        return f;
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        throw new InternalError('simplifyExpressions of ' + this.typeName + ' is abstract');
    }

    /**
     * make a list of the children of this element, used for simplifyExpressions of the subclass.
     * DO NOT call this method if this is not complex.
     * The subclass must place the return value of this method to a proper place.
     * This will NOT be removed or replaced.
     * @returns {TempVar} the TempVar of the list
     */
    public function makeList():TempVar {
        // examples:
        // [1, 2, 3, ...a] => temp0
        //   temp0 = [1, 2, 3]
        //   temp0.extend(a)
        // (a(), 1, b++, 2, 3, ...c) => tuple(temp0)
        //   temp0 = [a(), 1]
        //   temp1 = b
        //   b = temp1 + 1
        //   temp0.append(temp1)
        //   temp0.append(2)
        //   temp0.append(3)
        //   temp0.extend(c)
        // a(b(), 2, ...c, 3, ...d) => a(...temp0)
        //   temp0 = [b(), 2]
        //   temp0.extend(c)
        //   temp0.append(3)
        //   temp0.extend(d)
        this.checkStruct();
        var lc = -1;
        this.forEachChild(function(m, k, s) {
            if(m.complex || m instanceof SpreadElement) {
                lc = k;
                return false;
            }
        });
        if(lc < 0) {
            throw new InternalError('redundant calling to makeList');
        }

        var tv = this.theFunction.allocTempVar();
        var ate = new AssignTempElement(tv);
        this.insertTempAssign(ate);
        var init = new ArrayElement(null);
        ate.append(init);

        this.forEachChild(function(e, k, s) {
            if(k < lc) {
                init.append(e);
                return;
            }

            var fn, ee;
            if(e instanceof SpreadElement) {
                fn = 'extend';
                ee = e.firstChild;
            } else {
                fn = 'append';
                ee = e;
            }
            e.remove();
            // tv.append(ee) || tv.extend(ee)
            var cst = new ExpressionStatementElement(null);
            s.theStatement.before(cst);
            var cc = new CallElement(null);
            cst.append(cc);
            var ce = new AttributeElement(new Attribute(fn, null), null);
            cc.append(ce);
            var tve = VarElement.getTempVar(tv);
            ce.append(tve);
            var parg = new ArgumentElement(null);
            cc.append(parg);
            parg.append(ee);
            // ArgumentElement can prevent the infinite recursion
            cst.simplifyExpressions();
        });
        // should be cleared
        if(this.firstChild !== null) {
            throw new InternalError('unfinished SequenceElement::makeList');
        }

        return tv;
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        this.forEachChild(function(m, k, s) {
            if(k > 0) {
                writer.write(', ', '');
            }
            m.writePython(writer, false);
        });
    }

    /**
     * the constructor
     */
    public function SequenceElement(range:Range) {
        super(range);
    }
}

// #########= ArgumentElement

/**
 * argument (tuple) literal
 */
public class ArgumentElement extends SequenceElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'argument';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        var l = this.firstChild, r = this.lastChild;
        if(l === null) {
            return false;
        }
        if(l === r) {
            // only one simple spread fn(...a) is simple
            return this.firstChild.complex;
        }
        return this.hasSpread || super.complex;
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof CallElement || this.parent instanceof MagicCallElement)) {
            throw new InternalError('malformed structure in argument (not in call)');
        }
        super.checkStruct();
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        if(!this.complex) {
            return;
        }
        var l = this.firstChild, r = this.lastChild;
        if(l === r) {
            // single complex
            if(l instanceof SpreadElement) {
                l.firstChild.simplifyExpressions();
            } else {
                l.simplifyExpressions();
            }
            return;
        }
        var tv = this.makeList();
        // f(...temp)
        var sr = new SpreadElement(null);
        this.append(sr);
        sr.append(VarElement.getTempVar(tv));
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        writer.write('(', false);
        super.writePython(writer, '');
        writer.write(')', contchr);
    }

    /**
     * the constructor
     */
    public function ArgumentElement(range:Range) {
        super(range);
    }
}

// #########= ArrayElement

/**
 * array (list) literal
 */
public class ArrayElement extends SequenceElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'array';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        return this.hasSpread || super.complex;
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        if(!this.complex) {
            return;
        }
        var tv = this.makeList();
        // already a list
        this.replaceWith(VarElement.getTempVar(tv));
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        if(this.hasSpread) {
            throw new InternalError('cannot generate python for array with spread syntax');
        }
        writer.write('[', false);
        super.writePython(writer, '');
        writer.write(']', contchr);
    }

    /**
     * the constructor
     */
    public function ArrayElement(range:Range) {
        super(range);
    }
}

// #########= StatementElement

/**
 * base class of the standalone statement
 *
 * 语句的基类
 * 所谓完整语句是指在语句的前后插入另一条完整语句不会破坏元素的结构
 * 例如, if, 函数定义, 赋值都属于完整语句, 而函数体, 表达式则不属于完整语句.
 */
public class StatementElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'statement-abstract';
    }

    /**
     * the statement element this is in
     */
    override public function get theStatement():Element {
        return this;
    }

    /**
     * the constructor
     */
    public function StatementElement(range:Range) {
        super(range);
    }
}

// #########= AssignElement

/**
 * single assignment
 * AssignDestructElement for destructing assignment
 */
public class AssignElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'assign';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(LvalueElement, 1, false), // left value
            new ElementPattern(ExpressionElement, 1, false), // right value
        ]);
    }

    /**
    * walk stage 1
    *
    * 扫描全部变量, 检查变量是否正确声明, 有无需要建立闭包
    */
    override public function checkVariables():void {
        this.checkStruct();
        var left = this.firstChild;
        var right = this.lastChild;
        left.checkWrite();
        right.checkVariables();
    }

    /**
    * walk stage 2
    *
    * 简化表达式
    */
    override public function simplifyExpressions():void {
        this.checkStruct();
        var left = this.firstChild;
        var right = this.lastChild;
        left.extractLeft();
        right.simplifyExpressions();
        this.checkStruct();
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} ctx
     */
    override public function generatePython(ctx:PyGenerator):void {
        var writer = new LineWriter();
        var left = this.firstChild;
        var right = this.lastChild;
        left.writePython(writer, false);
        writer.write(' = ', '\\');
        right.writePython(writer, '\\');
        writer.finalize(ctx);
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function AssignElement(range:Range) {
        super(range);
    }
}

// #########= AssignDestructElement

/**
 * assignment with destructuring pattern as left value
 *
 * 用于解构赋值
 * 该元素的左值必须是解构组(DestructGroupElement), 这是一个基类, 具体的解构赋值又有两种情况.
 * 一种是数组解构(DestructArrayElement), 这实际上是解迭代器.
 * 一种是对象解构(DestructObjectElement), 在YAGS中, 是针对attr(而非index)解构的.
 * 其中数组解构的机制和Python不一样, 而对象解构则在Python中没有, 因此这两种解构都要另外实现.
 * 解构赋值元素会在stage2时进行拆分, 转换为普通的赋值.
 */
public class AssignDestructElement extends AssignElement {
    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(DestructGroupElement, 1, false), // left value
            new ElementPattern(ExpressionElement, 1, false), // right value
        ]);
    }

    /**
    * walk stage 1
    *
    * 扫描全部变量, 检查变量是否正确声明, 有无需要建立闭包
    */
    override public function checkVariables():void {
        this.checkStruct();
        var left = this.firstChild;
        var right = this.lastChild;
        // DestructGroupElement的checkVariables就是写入检查
        left.checkVariables();
        right.checkVariables();
    }

    /**
    * walk stage 2
    *
    * 简化表达式
    */
    override public function simplifyExpressions():void {
        this.checkStruct();
        var left = this.firstChild;
        left.checkStruct();
        var right = this.lastChild;
        // 将自身的右值放入DestructGroupElement中, 再令其展开
        left.append(right);
        this.before(left);
        left.simplifyExpressions();
        // this已经不需要了
        this.remove();
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} ctx
     */
    override public function generatePython(ctx:PyGenerator):void {
        throw new InternalError('cannot generate python for AssignDestructElement');
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function AssignDestructElement(range:Range) {
        super(range);
    }
}

// #########= AssignTempElement

/**
 * assign to a temporary variable
 *
 * 获取一个临时变量, 生成一个将结果赋给临时变量的赋值语句
 * 注意所有临时变量只能赋值一次
 */
public class AssignTempElement extends StatementElement {
    /**
     * the temp var
     */
    private var aim:TempVar = null;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'assigntemp';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, false), // right value
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(this.aim.at !== this.theFunction) {
            throw new InternalError('Mismatched scope for AssignTempElement');
        }
        super.checkStruct();
    }

    /**
     * walk stage 1
     */
    override public function checkVariables():void {
        // AssignTempElement can only be created in stage 2
        throw new InternalError('Illegal stage 1 for AssignTempElement');
    }

    /**
     * get the VarElement of the lvalue
     */
    public function getLeftElement():VarElement {
        return VarElement.getTempVar(this.aim);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('target', this.aim);
        super.dump(ctx);
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} ctx
     */
    override public function generatePython(ctx:PyGenerator):void {
        var writer = new LineWriter();
        var left = this.aim;
        var right = this.firstChild;
        writer.write(this.aim.toPython(), false);
        writer.write(' = ', '\\');
        right.writePython(writer, false);
        writer.finalize(ctx);
    }

    /**
    * the constructor
    */
    public function AssignTempElement(aim:TempVar) {
        super(null);
        this.aim = aim;
    }
}

// #########= LvalueElement

/**
 * base class of the left value
 *
 * 可以作为赋值目标的表达式的基类, 不要直接使用这个类
 */
public class LvalueElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'lvalue-abstract';
    }

    /**
     * check write variable
     *
     * 对于一般LvalueElement来说等同于checkVariables
     * 具体是否能写入只能等到运行时判断
     */
    public function checkWrite():void {
        this.checkVariables();
    }

    /**
     * true if this is a declarator
     *
     * 如果是一个变量声明(比如var), 返回true, 大多左值都是无法声明的
     */
    public function get declarator():Boolean {
        return false;
    }

    /**
     * extract the left's object and index
     * (stage 2)
     *
     * 析出中间值
     * 在es中, 赋值(对于存在副作用的情况下)是从左边开始执行的, 这里遵照该规定.
     * 例如a(b++)[b++] = b++是先执行a(b++), 然后是方括号中的b++, 最后才是等式右边的b++.
     * 注意这和JAVA一致, 但和Python相反.
     * 因此对于有副作用的左值需要先存储其中间值.
     *
     * 这个和simplifyExpression方法形式上是一样的.
     * 作为右值时, 须调用simplifyExpression(或者replaceWithTemp). 作为左值时, 须调用extractLeft(或者extractLeftAndDuplicate).
     */
    public function extractLeft():void {
        throw new InternalError('extractLeft is abstract in ' + this.typeName);
    }

    /**
     * extract the left's object and index and return the duplication of this
     * (stage 2)
     *
     * 析出中间值并返回复制的左值表达式
     * 该函数一般用于复合赋值或者自增(减)运算
     * 在a[b]++和a[b] += c等表达式中, a和b只能在最开始执行一次, 在赋值阶段不会再执行.
     * 因此要先将a和b存入临时变量
     * 和extractLeft的区别在于, 本函数还会返回左值析出后的复制, 以便将其作为右值
     */
    public function extractLeftAndDuplicate():LvalueElement {
        throw new InternalError('extractLeftAndDuplicate is abstract in ' + this.typeName);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('declare', this.declarator);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function LvalueElement(range:Range) {
        super(range);
    }
}

// #########= AttributeElement

/**
 * member expression a.b
 */
public class AttributeElement extends LvalueElement {
    /**
     * an Attribute, the property name
     */
    private var attribute:Attribute;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'attribute';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 1, false)]);
    }

    /**
     * extrace the left's object and index
     * (stage 2)
     */
    override public function extractLeft():void {
        this.checkStruct();
        var left = this.firstChild;
        var ate = left.replaceWithTemp();
        this.insertTempAssign(ate);
        this.checkStruct();
    }

    /**
     * extrace the left's object and index and return the duplication of this
     * (stage 2)
     */
    override public function extractLeftAndDuplicate():LvalueElement {
        this.checkStruct();
        var left = this.firstChild;
        // 因为要使用两次, 所以不能返回空值
        var ate = left.replaceWithTemp(false);
        this.insertTempAssign(ate);

        var v = new AttributeElement(this.attribute, this.range);
        v.append(ate.getLeftElement());
        this.checkStruct();
        return v;
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('attribute', this.attribute);
        super.dump(ctx);
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var cls = this.theClass;
        var pi = cls === null ? false : cls.hasPrivateInstance(this.attribute.name);
        var ps = cls === null ? false : cls.hasPrivateStatic(this.attribute.name);
        var object = this.firstChild;
        var psk;
        if(pi && ps) {
            psk = '__cpg';
        } else if(pi) {
            psk = '__cpm';
        } else if(ps) {
            psk = '__csg';
        }
        if(pi || ps) {
            writer.write(psk, false);
            writer.write('[', false);
            object.writePython(writer, '');
            writer.write(', "', false);
            writer.write(this.attribute.toPython(), false);
            writer.write('"]', contchr);
        } else {
            object.writePython(writer, '\\', 12);
            writer.write('.', false);
            writer.write(this.attribute.toPython(), contchr);
        }
    }

    /**
     * the constructor
     */
    public function AttributeElement(attribute:Attribute, range:Range) {
        super(range);
        this.attribute = attribute;
    }
}

// #########= BaseFunctionElement

/**
 * Base class of the statements with function scope
 *
 * BaseFunctionElement是函数定义的基类, 函数或类似函数的类会继承此类
 * 所谓类似函数是指会形成一个局部的变量作用域的元素, 顶层也是一种.
 */
public class BaseFunctionElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'basefunction';
    }

    /**
     * variables map
     *
     * 局部变量
     */
    private var vars:StringMap = new StringMap();

    /**
     * variables map for the public variable refered in the fnction
     *
     * 公开变量在py中是使用global实现的, 在函数体内如果发生该变量的引用, 需要提前用global声明
     */
    private var assignedPublic:StringMap = new StringMap();

    /**
     * index of this function
     *
     * 当前函数在全局(本文件内)的id
     */
    private var functionId:Number = 0;

    /**
     * token of this function
     *
     * 当前函数的全局id串, 经过编码
     */
    public function get functionToken():String {
        return Identifier.encodeRadix32(this.functionId);
    }

    /**
     * true if super() can be used here
     *
     * 只有构造函数才能使用super()调用, 构造函数里定义的函数则不可以
     */
    override public function get allowSuperCall():Boolean {
        return false;
    }

    /**
     * id of the next temporary variable
     */
    private var tempCounter:Number = 0;

    /**
     * the function element this is in
     *
     * 该语句所在的函数
     */
    override public function get theFunction():BaseFunctionElement {
        return this;
    }

    /**
     * the parent function of this
     */
    public function get parentFunction():BaseFunctionElement {
        // 全局元素需要超控这个函数, 并返回null
        return this.parent.theFunction;
    }

    /**
     * the function defined in this function
     */
    public function get functionDefinitions():FunctionGroupElement {
        throw new InternalError(this.typeName + ' have no inner function definition area');
    }

    /**
     * the body
     */
    public function get body():BodyElement {
        throw new InternalError(this.typeName + ' have no function body');
    }

    /**
     * get variable in this function
     * @param {String} name, the identifier of the variable
     */
    public function getLocal(name:String):Variable {
        return this.vars.get(name, null);
    }

    /**
     * set variable to this scope
     * @param {String} name, the identifier of the variable
     * @param {Variable} v, the variable
     */
    public function setLocal(name:String, v:Variable):void {
        if(v === null) {
            throw new InternalError('set a null variable');
        }
        this.vars.set(name, v);
    }

    /**
     * register local function definition
     * @param {FunctionTag} tag, the tag of function
     * @param {Range} range
     */
    public function registerFunctionDefinition(tag:FunctionTag, range:Range = null):void {
        // check if exists
        var name = tag.name;
        var v = this.getLocal(name);
        if(v !== null) {
            throw new ConflictError("Duplicate function definition: %s", range, v.range, name);
        }
        this.setLocal(name, tag);
    }

    /**
     * register local variable and return it
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     */
    public function registerLocalVar(name:String, range:Range = null):LocalVar {
        // check if exists
        var v = this.getLocal(name);
        if(v !== null) {
            throw new ConflictError("Identifier '%s' has already been declared", range, v.range, name);
        }
        v = new LocalVar(name, this, range);
        this.setLocal(name, v);
        return v;
    }

    /**
     * iterate local variables
     * @param {Function} callback(variable, index, self)
     * callback can return boolean false to stop the iteration
     */
    public function forEachLocalVar(callback):void {
        var self = this;
        this.vars.forEach(function(e, k, a) {
            return callback(e, k, self)
        });
    }

    /**
     * find the variable by name
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     *
     * 查找变量, 一些子类可能需要超控该方法
     */
    public function referVar(name:String, range:Range = null):Variable {
        // check if exists
        var v = this.getLocal(name);
        if(v !== null) {
            return v;
        }
        return this.parentFunction.referVar(name, range);
    }

    /**
     * allocate temporal variable
     * return the TempVar object
     */
    public function allocTempVar():TempVar {
        var tid = this.tempCounter++;
        return new TempVar(tid, this);
    }

    /**
     * declare this variable
     * (pre-stage1)
     *
     * 向全局申请函数id
     */
    override public function declareVariable():void {
        this.functionId = this.theGlobal.allocFunctionId();
        super.declareVariable();
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('id', this.functionId);
        ctx.attr('tempcnt', this.tempCounter);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function BaseFunctionElement(range:Range) {
        super(range);
    }
}

// #########= BinaryOperatorElement

/**
 * class of the binary operators
 */
public class BinaryOperatorElement extends ExpressionElement {
    /**
     * raw (operator) in js, a string
     */
    private var source:String;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'binary';
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return this.firstChild.constantOnly && this.lastChild.constantOnly;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        // may throw exception
        return false;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 2, false)]);
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        this.checkStruct();
        super.functionalize();
        var op = this.source;
        var a = this.firstChild;
        var b = this.lastChild;
        // instanceof, ===, !==要转换为函数
        var opfMap = new StringMap([
            ['instanceof', '__x_iof'], 
            ['===', '__x_eq'], ['!==', '__x_ne']
        ]);
        var fn = opfMap.get(op, null);
        if(fn === null) {
            return;
        }
        var cc = new CallElement(null);
        this.replaceWith(cc);
        var callee = VarElement.getGlobalVar(fn);
        cc.append(callee);
        var argv = new ArgumentElement(null);
        cc.append(argv);
        argv.append(a);
        argv.append(b);
        cc.checkStruct();
    }

    /**
    * walk stage 2
    *
    * 简化表达式, 提升复杂表达式, 使之能被py表示
    */
    override public function simplifyExpressions():void {
        this.checkStruct();
        if(!this.complex) {
            return;
        }
        var left = this.firstChild;
        var right = this.lastChild;
        var op = this.source;

        // 对于其他双目运算符, 左右操作数都会执行
        if(right.complex) {
            // 左操作数总是在右操作数前执行, 因此需要先析出左操作数
            var ale = left.replaceWithTemp();
            this.insertTempAssign(ale);
            right.simplifyExpressions();
        } else {
            left.simplifyExpressions();
        }
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var oppMap = new StringMap([
            ['+', 8], ['-', 8], ['*', 9], ['/', 9], ['%', 9], ['**', 9],
            ['>>', 7], ['<<', 7], ['&', 6], ['^', 5], ['|', 4],
            ['==', 3], ['!=', 3], ['<=', 3], ['<', 3], ['>=', 3], ['>', 3]
        ]);
        var op = this.source;
        var left = this.firstChild;
        var right = this.lastChild;
        if(!oppMap.has(op)) {
            throw new InternalError('Cannot writePython for binary ' + op);
        }
        var p = oppMap.get(op);
        // 双目运算是左结合的, 右边需要提升一个优先级
        var lp = p;
        var rp = p + 1;
        if(op === '**') {
            // 幂(**)是特例, 和单目运算符混合时总是加上括号, 尽管py无此规定
            lp = 11;
            rp = 11;
        }
        // 为了避免变成连续比较, 比较之间总是加括号
        if(p === 3) {
            lp = 4;
            rp = 4;
        }
        var ap = p < parentType;
        var lsp = ap ? '' : contchr; 
        if(ap) {
            writer.write('(', false);
        }
        left.writePython(writer, lsp, lp);
        writer.write(' ' + op + ' ', lsp);
        right.writePython(writer, lsp, rp);
        if(ap) {
            writer.write(')', contchr);
        }
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('operator', this.source);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function BinaryOperatorElement(source:String, range:Range) {
        super(range);
        this.source = source;
    }
}

// #########= BinaryLogicalElement

/**
 * class of the binary logic operators
 */
public class BinaryLogicalElement extends ExpressionElement {
    /**
     * raw (operator) in js, a string
     */
    private var source:String;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'logic';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        if(this.theGlobal.enableImplicitBooleanConversion) {
            // should cache the value
            return true;
        }
        return this.source === '??' || super.complex;
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return this.firstChild.constantOnly && this.lastChild.constantOnly;
    }

    /**
     * check if if this is only a temp variable, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get tempVarOnly():Boolean {
        // may throw exception
        return false;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 2, false)]);
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        this.checkStruct();
        super.functionalize();
        var op = this.source;
        var a = this.firstChild;
        var b = this.lastChild;
        // coerce to the boolean type if implicit boolean conversion is not enabled
        if(!this.theGlobal.enableImplicitBooleanConversion && (op === '&&' || op === '||')) {
            var chk = CallElement.callGlobal('__x_cb', a);
            this.prepend(chk);
            this.checkStruct();
        }
    }

    /**
     * walk stage 2 under enableImplicitBooleanConversion
     */
    private function simplifyExpressionsImplicitBooleanConversion():void {
        // convert to if, use TOBoolean(tob) / ToNotBoolean(tnb) function
        //
        // input:
        // a(b && c)
        // output:
        // __temp0 = b
        // if(__x_tob(__temp0)) {
        //   __temp0 = c;
        // }
        // a(__temp0)
        //
        // input:
        // a(b || c)
        // output:
        // __temp0 = b
        // if(!(__temp0)) {
        //   __temp0 = c;
        // }
        // a(__temp0)
        var left = this.firstChild;
        var right = this.lastChild;
        var op = this.source;
        
        var atva = this.theFunction.allocTempVar();
        var atvl = new AssignTempElement(atva);
        this.theStatement.before(atvl);
        atvl.append(left);
        atvl.simplifyExpressions();

        var ife = new IfBlockElement(null);
        this.theStatement.before(ife);
        var iife = new IfElement(null);
        ife.append(iife);
        var acond = new ConditionElement(null);
        iife.append(acond);
        if(op === '&&') {
            acond.append(CallElement.callGlobal('__x_tob', atvl.getLeftElement()));
        } else if(op === '||') {
            acond.append(CallElement.callGlobal('__x_tnb', atvl.getLeftElement()));
        } else if(op === '??') {
            var acondnc = new NullishCheckElement(null);
            acond.append(acondnc);
            acondnc.append(atvl.getLeftElement());
        }
        var atrue = new BodyElement(null);
        iife.append(atrue);
        var atvr = new AssignTempElement(atva);
        atrue.append(atvr);
        atvr.append(right);
        ife.simplifyExpressions();

        this.replaceWith(atvl.getLeftElement());
    }

    /**
     * walk stage 2
     *
     * 简化表达式, 提升复杂表达式, 使之能被py表示
     */
    override public function simplifyExpressions():void {
        this.checkStruct();
        if(this.theGlobal.enableImplicitBooleanConversion) {
            this.simplifyExpressionsImplicitBooleanConversion();
            return;
        }
        if(!this.complex) {
            return;
        }
        var left = this.firstChild;
        var right = this.lastChild;
        var op = this.source;

        // 由于&&, ||, ??是短路的, 故需要转换为if语句
        //
        // input:
        // a(b && c)
        // output:
        // __temp0 = __x_cb(b)
        // if(__temp0) {
        //   __temp0 = c;
        // }
        // a(__temp0)
        //
        // input:
        // a(b || c)
        // output:
        // __temp0 = b
        // if(!__temp0) {
        //   __temp0 = c;
        // }
        // a(__temp0)
        //
        // input:
        // a(b ?? c)
        // output:
        // __temp0 = b
        // if(__temp0 === null) {
        //   __temp0 = c;
        // }
        // a(__temp0)
        var atva = this.theFunction.allocTempVar();
        var atvl = new AssignTempElement(atva);
        this.theStatement.before(atvl);
        atvl.append(left);
        atvl.simplifyExpressions();

        var ife = new IfBlockElement(null);
        this.theStatement.before(ife);
        var iife = new IfElement(null);
        ife.append(iife);
        var acond = new ConditionElement(null);
        iife.append(acond);
        if(op === '&&') {
            acond.append(atvl.getLeftElement());
        } else if(op === '||') {
            var acondor = new NotOperatorElement(null);
            acond.append(acondor);
            acondor.append(atvl.getLeftElement());
        } else if(op === '??') {
            var acondnc = new NullishCheckElement(null);
            acond.append(acondnc);
            acondnc.append(atvl.getLeftElement());
        }
        var atrue = new BodyElement(null);
        iife.append(atrue);
        var atvr = new AssignTempElement(atva);
        atrue.append(atvr);
        atvr.append(right);
        ife.simplifyExpressions();

        this.replaceWith(atvl.getLeftElement());
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var op = this.source;
        var left = this.firstChild;
        var right = this.lastChild;
        if(op === '||' || op === '&&') {
            // 总是给混合使用的逻辑运算符加括号
            var ap = 2 <= parentType;
            var lsp = ap ? '' : contchr; 
            if(ap) {
                writer.write('(', false);
            }
            // 此处不再需要布尔类型检查了
            left.writePython(writer, lsp, 3);
            writer.write(op === '||' ? ' or ' : ' and ', lsp);
            right.writePython(writer, lsp, 2);
            if(ap) {
                writer.write(')', contchr);
            }
        } else {
            // ?? 全部要变成if语句
            throw new InternalError('Cannot writePython for logic ' + op);
        }
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('operator', this.source);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function BinaryLogicalElement(source:String, range:Range) {
        super(range);
        this.source = source;
    }
}

// #########= BlockElement

/**
 * the unconditional block
 */
public class BlockElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'block';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(StatementElement, 0, true)
        ]);
    }

    /**
    * generate python code
    *
    * 生成Python代码
    */
    override public function generatePython(ctx:PyGenerator):void {
        this.forEachChild(function(e, k, t) {
            e.generatePython(ctx);
        });
    }

    /**
    * the constructor
    * @param {Range} range, the range of the whole block
    */
    public function BlockElement(range:Range) {
        super(range);
    }
}

// #########= BodyElement

/**
 * the conditional body
 */
public class BodyElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'body';
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        // constructor will return true
        return this.parent.allowSuperCall;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(StatementElement, 0, true)
        ]);
    }

    /**
    * generate python code
    *
    * 生成Python代码
    */
    override public function generatePython(ctx:PyGenerator):void {
        this.forEachChild(function(e, k, t) {
            e.generatePython(ctx);
        });
    }

    /**
    * the constructor
    * @param {Range} range, the range of the whole block
    */
    public function BodyElement(range:Range) {
        super(range);
    }
}

// #########= FundamentalLiteralElement

/**
 * base class of the literal expressions
 */
public class FundamentalLiteralElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'literal-abstract';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        return false;
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return true;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        return true;
    }

    /**
     * replace this with a temporary variable
     */
    override public function replaceWithTemp(optional = true):AssignTempElement {
        if(optional) {
            return null;
        }
        return super.replaceWithTemp(false);
    }

    /**
    * the constructor
    */
    public function FundamentalLiteralElement(range:Range) {
        super(range);
    }
}

// #########= BooleanLiteralElement

/**
 * class of the boolean literal expressions (true / false)
 */
public class BooleanLiteralElement extends FundamentalLiteralElement {
    /**
    * the value of this
    */
    private var value:Boolean;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'boolean';
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        writer.write(this.value ? 'True' : 'False', contchr);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('value', this.value);
        super.dump(ctx);
    }

    /**
    * the constructor
    */
    public function BooleanLiteralElement(value:Boolean, range:Range) {
        super(range);
        this.value = value;
    }
}

// #########= BreakElement

/**
 * break statement
 * labeled break is not supported
 */
public class BreakElement extends StatementElement {
    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        ctx.writeln('break');
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function BreakElement(range:Range) {
        super(range);
    }
}

// #########= CallElement

/**
 * class of the binary operators
 */
public class CallElement extends ExpressionElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'call'
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        return this.parent.allowSuperCall;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, false), // callee
            new ElementPattern(ArgumentElement, 1, false), // arguments
        ]);
    }

    /**
     * scan the variables in this expression
     * (stage 1)
     */
    override public function checkVariables():void {
        var callee = this.firstChild;
        var argv = this.lastChild;
        var supcall = this.firstChild instanceof SuperElement;
        if(!supcall) {
            callee.checkVariables();
        } else if(!this.allowSuperCall) {
            throw new CompileError("super() statement unexpected here", this.range);
        }
        argv.checkVariables();
        // check argv at first to reject super(this)
        if(supcall) {
            // must be method
            var fn = this.theFunction;
            fn.meetSuper(this.range);
        }
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        super.functionalize();
        // super(), 即__csu的第一个参数是this
        var supcall = this.firstChild instanceof SuperElement;
        if(supcall) {
            var argv = this.lastChild;
            argv.prepend(new ThisElement(null));
        }
    }

    /**
    * walk stage 2
    *
    * 简化表达式, 提升复杂表达式, 使之能被py表示
    */
    override public function simplifyExpressions():void {
        var callee = this.firstChild;
        var argv = this.lastChild;
        var supcall = this.firstChild instanceof SuperElement;
        if(argv.complex) {
            // 如果参数是复杂的, 那被调函数也得析出
            if(!supcall) {
                var callee2 = callee.replaceWithTemp();
                this.insertTempAssign(callee2);
            }
            argv.simplifyExpressions();
        } else if(callee.complex) {
            callee.simplifyExpressions();
        }
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var callee = this.firstChild;
        var supcall = this.firstChild instanceof SuperElement;
        var argv = this.lastChild;
        if(supcall) {
            writer.write('__csu', false);
        } else {
            callee.writePython(writer, contchr, 12);
        }
        argv.writePython(writer, contchr, 12);
    }

    /**
     * the constructor
     */
    public function CallElement(range:Range) {
        super(range);
    }

    /**
     * create a call gaobal var with a single argument
     */
    public static function callGlobal(name:String, arg:ExpressionElement):CallElement {
        var cc = new CallElement(null);
        var callee = VarElement.getGlobalVar(name);
        cc.append(callee);
        var argv = new ArgumentElement(null);
        cc.append(argv);
        argv.append(arg);
        return cc;
    }
}

// #########= CatchElement

/**
 * if statement
 *
 * 单个catch的语句
 * 不要直接使用这个, 需要放入一个TryBlockElement中
 */
public class CatchElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'catch';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ParameterElement, 1, true),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof TryBlockElement)) {
            throw new InternalError('malformed structure in CatchElement (not in TryBlockElement)');
        }
        super.checkStruct();
    }

    /**
    * put the python code of the contained expression into writer
    *
    * @param {PyGenerator} gen
    */
    override public function generatePython(gen:PyGenerator):void {
        var writer = new LineWriter();
        writer.write('except __x_errT as ', false);
        var ex = this.firstChild;
        var body = this.lastChild;
        if(ex === body) {
            // no error variable catch {}
            writer.write(this.theFunction.allocTempVar().toRawPython(), false)
        } else {
            ex.writePython(writer, '');
        }
        writer.write(':', false);
        writer.finalize(gen);
        gen.tab();
        // rename the exception variable if necessary
        ex.generateRenameAssignment(gen);
        body.generatePython(gen);
        gen.TAB();
    }

    /**
     * the constructor
     */
    public function CatchElement(range:Range) {
        super(range);
    }
}

// #########= ClassElement

/**
 * class
 *
 * ClassElement是类定义的类
 * YAGS提供类似于es4的类定义机制, 类只能在顶层定义且不可以嵌套
 * 只提供了private和public两种成员访问控制符
 *
 * 生成类的代码放在一个函数中, 称为类工厂函数, 该函数在运行时执行一次, 并产生类定义.
 * 注意类的定义不是提升的, 这是因为静态初始化器在类定义时立即执行, 需保证执行顺序.
 * 尽管ClassElement在全局中会放入functionDefinitions区, 但该函数会在原来的位置调用, 并将结果赋值给类标签(使用ClassInitElement).
 * 类工厂函数以__c_作为函数名前缀, 同时类内部所有和类创建有关的辅助变量均以__c为前缀
 *
 * 类的定义区由这三个部分组成:
 * 1. 方法定义: 这个等同于函数的functionDefinitions, 定义该类的内层方法(不管是否是静态的).
 * 2. 静态初始化器(__csi): Class Static Initializer, 该函数用于初始化类的静态属性, 在该函数执行阶段, 类的标签还不能访问. 静态属性的初始化器放入此处.
 * 3. 成员初始化器(__csu): Class SUper, 该函数用于初始化类的实例属性, 并调用超类的构造器, 构造器中的super()实际调用的就是__csu函数. 对于没有定义构造器的类, __csu将作为__init__函数. 实例属性的初始化器放入此处.
 */
public class ClassElement extends BaseFunctionElement {
    /**
     * the tag of this
     */
    public var tag:ClassTag = null;

    /**
     * true if this is a public declaration
     */
    private var isPublic:Boolean = false;

    /**
     * true if this extends a class (otherwise extends object)
     */
    private var hasSuper:Boolean = false;

    /**
     * instance members, a dictionary of ClassFieldDescriptor
     */
    private var instanceMembers:StringMap = new StringMap();

    /**
     * static members, a dictionary of ClassFieldDescriptor
     */
    private var staticMembers:StringMap = new StringMap();

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'class';
    }

    /**
     * the class element this is in
     */
    override public function get theClass():ClassElement {
        return this;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(MethodGroupElement, 1, false),
            new ElementPattern(StaticGroupElement, 1, false),
            new ElementPattern(InstanceGroupElement, 1, false)
        ]);
    }

    /**
     * true if this can be refered here
     */
    override public function get allowThis():Boolean {
        return true;
    }

    /**
     * true if super can be refered here
     */
    override public function get allowSuper():Boolean {
        return true;
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        return this.hasSuper;
    }

    /**
     * the function defined in this function
     */
    override public function get functionDefinitions():FunctionGroupElement {
        this.checkStruct();
        var e = this.firstChild;
        return e;
    }

    /**
     * the static property initializer
     */
    public function get staticInit():StaticGroupElement {
        this.checkStruct();
        var e = this.firstChild.nextSibling;
        return e;
    }

    /**
     * the instance property initializer
     */
    public function get instanceInit():InstanceGroupElement {
        this.checkStruct();
        var e = this.lastChild;
        return e;
    }

    /**
     * the body
     */
    override public function get body():BodyElement {
        return null;
    }

    /**
     * find the variable by name
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     *
     * 注意和JAVA不一样, 如果要访问实例的成员必须加上this, 如果要访问静态成员必须加上类名
     */
    override public function referVar(name:String, range:Range = null):Variable {
        // check if class name
        if(this.tag.name === name) {
            return this.tag;
        }
        return this.parentFunction.referVar(name, range);
    }

    /**
     * register function definition
     * @param {FunctionTag} tag, the tag of method
     * @param {Range} range
     */
    override public function registerFunctionDefinition(tag:FunctionTag, range:Range = null):void {
        // as operator is not supported
        function coerce(tag):MethodTag {
            if(!(tag instanceof MethodTag)) {
                throw new InternalError('only method is allowed in class');
            }
            return tag;
        }
        var tag2 = coerce(tag);
        var st = tag2.isStatic;
        var o = st ? this.staticMembers : this.instanceMembers;
        var n = tag2.name;
        var cfd = o.get(n, null);
        if(cfd === null) {
            cfd = new ClassFieldDescriptor(n, st);
            o.set(n, cfd);
        }
        cfd.meetMethod(tag2);
    }

    /**
     * register local variable and return it
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     */
    override public function registerLocalVar(name:String, range:Range = null):LocalVar {
        throw new InternalError('only property is allowed in class');
    }

    /**
     * register property
     * @param {String} name, the name of property
     * @param {Boolean} isPublic, true if this is a public property
     * @param {Boolean} isStatic, true if this is a static property
     * @param {Range} range
     */
    public function registerProperty(name:String, isPublic:Boolean, isStatic:Boolean, range:Range):void {
        var st = isStatic, n = name;
        var o = st ? this.staticMembers : this.instanceMembers;
        var cfd = o.get(n, null);
        if(cfd === null) {
            cfd = new ClassFieldDescriptor(n, st);
            o.set(n, cfd);
        }
        cfd.meetProperty(isPublic, range);
    }

    /**
     * check if the specified name is a private instance member
     * @param {String} name, the name of attribute
     */
    public function hasPrivateInstance(name:String):Boolean {
        var o = this.instanceMembers;
        var cfd = o.get(name, null);
        if(cfd === null) {
            return false;
        }
        return cfd.isPrivate;
    }

    /**
     * check if the specified name is a private static member
     * @param {String} name, the name of attribute
     */
    public function hasPrivateStatic(name:String):Boolean {
        var o = this.staticMembers;
        var cfd = o.get(name, null);
        if(cfd === null) {
            return false;
        }
        return cfd.isPrivate;
    }

    /**
     * declare this variable
     * (pre-stage1)
     *
     * 声明变量. 
     */
    override public function declareVariable():void {
        if(!(this.parentFunction instanceof GlobalElement)) {
            throw new InternalError('Public member not in global');
        }
        // 注册当前类的tag
        this.theGlobal.registerClassDefinition(this.tag, this.tag.range);
        // 如果是公开的, 就向全局注册公开成员
        if(this.isPublic) {
            this.theGlobal.declarePublic(this.tag.name, this.tag.range);
        }
        super.declareVariable();
    }

    /**
     * create the ClassInitElement for this class
     */
    public function createClassInitElement():ClassInitElement {
        return new ClassInitElement(this.hasSuper, this.tag, this.tag.range);
    }

    /**
     * generate python code of the class factory
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(gen:PyGenerator):void {
        var sm = this.staticMembers;
        var im = this.instanceMembers;

        gen.blank();
        var sline = new LineNumber();
        gen.logLineNumber(sline);

        // 函数声明
        var writer = new LineWriter();
        writer.write('def ', false);
        writer.write(this.tag.toFactoryName(), false);
        writer.write('(', '');
        if(this.hasSuper) {
            writer.write('__cexT', '');
        }
        writer.write('):', false);
        writer.finalize(gen);

        gen.tab();

        // 方法定义
        this.functionDefinitions.generatePython(gen);
        // 静态初始化器(__csi)
        this.staticInit.generatePython(gen);
        // 实例初始化器和超类构造(__csu)
        this.instanceInit.generatePython(gen);

        gen.blank();

        // 如果该类含有私有的实例成员, 就需要构建一个私有成员类(__cpiT)来存放这些私有成员.
        // 在__csu函数执行时将创建一个对应的__cpiT实例. 对该实例的访问则是通过Class Private Map(__cpm)来实现的(参见AttributeElement).
        // 由于访问所有同名的属性(不管是否是本类的实例)均需要进行检查, 从而有一定的开销, 但应该比给所有私有变量带上特殊符号要好.
        // 注意, 访问私有成员不局限于当前实例(即this). 如果将该类的其他实例作为参数传入方法(包括静态的), 同样可以访问对应的私有变量.
        var haspi = false;
        im.forEach(function(p, k, s) {
            if(p.isPrivate) {
                haspi = true;
                return false;
            }
        });
        // __cpiT由__x_dpif函数创建
        // definePrivateInstanceField(className:str, fields:dict)
        if(haspi) {
            writer = new LineWriter();
            writer.write('__cpiT = __x_dpif(', false);
            writer.write('"' + this.tag.toPython() + '"', false);
            writer.write(', ', '');
            writer.write('{', '');
            writer.write('"__slots__": (', '');
            var ppl = 0;
            im.forEach(function(p, k, a) {
                if(!(p.isProperty && p.isPrivate)) {
                    return;
                }
                if(ppl > 0) {
                    writer.write(', ', '\\');
                }
                writer.write('"' + p.toPython() + '"', '');
                ppl++;
            });
            if(ppl === 1) {
                // trailing comma is required for tuple with only one element
                writer.write(',', false);
            }
            writer.write(')', '');
            ppl = 0;
            im.forEach(function(p, k, a) {
                if(!(!p.isProperty && p.isPrivate)) {
                    return;
                }
                writer.write(', ', '');
                writer.write('"' + p.toPython() + '": ', false);
                if(p.isMethod) {
                    // 对于私有方法, 需要使用staticmethod装饰器进行处理
                    // 不然将其this指针绑定到__clsT的实例上时会发生错误
                    writer.write('__x_smet(', false);
                }
                writer.write(p.toMethodName(), false);
                if(p.isMethod) {
                    writer.write(')', false);
                }
                ppl++;
            });
            writer.write('})', false);
            writer.finalize(gen);
        }

        // 如果该类含有静态成员, 则需要一个静态私有成员类(Private Static Field Type, __cpsfT).
        // 和类本身一样, 这个类只有一个实例, 称为Class Static Private(__csp).
        // 对静态私有成员的访问是通过Class Static private Gate(__csg)对象来完成的.
        var hasps = false;
        sm.forEach(function(p, k, s) {
            if(p.isPrivate) {
                hasps = true;
                return false;
            }
        });
        // __cpsfT由__x_dpsf函数创建
        // definePrivateStaticField(className:str, fields:dict)

        if(hasps) {
            writer = new LineWriter();
            writer.write('__cpsT = __x_dpsf(', false);
            writer.write('"' + this.tag.toPython() + '"', false);
            writer.write(', ', '');
            writer.write('{', '');
            writer.write('"__slots__": (', '');
            ppl = 0;
            sm.forEach(function(p, k, a) {
                if(!(p.isProperty && p.isPrivate)) {
                    return;
                }
                if(ppl > 0) {
                    writer.write(', ', '');
                }
                writer.write('"' + p.toPython() + '"', false);
                ppl++;
            });
            if(ppl === 1) {
                // trailing comma is required for tuple with only one element
                writer.write(',', false);
            }
            writer.write(')', false);
            ppl = 0;
            sm.forEach(function(p, k, a) {
                if(!(!p.isProperty && p.isPrivate)) {
                    return;
                }
                writer.write(', ', '');
                writer.write('"' + p.toPython() + '": ', false);
                writer.write(p.toMethodName(), false);
                ppl++;
            });
            writer.write('})', false);
            writer.finalize(gen);
            // 创建__cpsfT实例
            gen.writeln('__csp = __cpsT()');
        }

        // 最复杂的一种情况是, 如果该类具有某个成员同时是实例私有成员和静态私有成员,
        // 则要先后检查这两种可能性, 这是使用Class Private Gate(__cpg)对象来完成的.
        var haspis = false;
        im.forEach(function(p, k, s) {
            if(!p.isPrivate) {
                return;
            }
            var p2 = sm.get(k, null);
            if(p2 !== null && p2.isPrivate) {
                haspis = true;
                return false;
            }
        });

        // 最终的类__clsT由__x_dcls创建
        // defineClass(className:str, superClass:type, staticFields:dict, instanceFields:dict)
        writer = new LineWriter();
        writer.write('__clsT = __x_dcls(', false);
        writer.write('"' + this.tag.toPython() + '"', false);
        writer.write(', ', '');
        // 如果没有超类就是object(__x_objT)
        writer.write(this.hasSuper ? '__cexT' : '__x_objT', false);
        writer.write(', ', false);
        writer.write('{', '');
        writer.write('"__slots__": (', '');
        ppl = 0;
        sm.forEach(function(p, k, a) {
            if(!(p.isProperty && !p.isPrivate)) {
                return;
            }
            if(ppl > 0) {
                writer.write(', ', '');
            }
            writer.write('"' + p.toPython() + '"', false);
            ppl++;
        });
        if(ppl === 1) {
            // trailing comma is required for tuple with only one element
            writer.write(',', false);
        }
        writer.write(')', false);
        ppl = 0;
        sm.forEach(function(p, k, a) {
            if(!(!p.isProperty && !p.isPrivate)) {
                return;
            }
            writer.write(', ', '');
            writer.write('"' + p.toPython() + '": ', false);
            writer.write(p.toMethodName(), false);
            ppl++;
        });
        writer.write(', ', '');
        writer.write('"__init__": __csi', false);
        writer.write('}, ', '');
        writer.write('{', '');
        writer.write('"__slots__": (', '');
        ppl = 0;
        im.forEach(function(p, k, a) {
            if(!(p.isProperty && !p.isPrivate)) {
                return;
            }
            if(ppl > 0) {
                writer.write(', ', '');
            }
            writer.write('"' + p.toPython() + '"', false);
            ppl++;
        });
        if(ppl === 1) {
            // trailing comma is required for tuple with only one element
            writer.write(',', false);
        }
        writer.write(')', false);
        ppl = 0;
        im.forEach(function(p, k, a) {
            if(!(!p.isProperty && !p.isPrivate)) {
                return;
            }
            writer.write(', ', '');
            writer.write('"' + p.toPython() + '": ', false);
            writer.write(p.toMethodName(), false);
            ppl++;
        });

        // 查找构造器
        var ctag = null;
        this.functionDefinitions.forEachChild(function(f, k, a) {
            if(f.isConstructor) {
                ctag = f.tag;
                return false;
            }
        });

        // 如果没有指定构造器那__csu就是构造器
        writer.write(', ', '');
        if(ctag === null) {
            writer.write('"__init__": __csu', false);
        } else {
            writer.write('"__init__": ', false);
            writer.write(ctag.toPython(), false);
        }
        writer.write('})', false);
        writer.finalize(gen);

        // 如果存在私有变量, 创建对应的访问器
        if(haspi) {
            gen.writeln('__cpm = __x_prmT(__clsT, __cpiT)')
        }
        if(hasps) {
            gen.writeln('__csg = __x_csgT(__clsT, __csp)')
        }
        if(haspis) {
            gen.writeln('__cpg = __x_cpgT(__clsT, __cpm, __csp)')
        }

        // 最后返回__clsT作为结果
        gen.writeln('return __clsT')

        gen.TAB();

        gen.comment(
            'end class factory %s, %s (line %l)',
            this.tag.toPython(),
            this.tag.toFactoryName(),
            sline
        );
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('tag', this.tag);
        ctx.attr('public', this.isPublic);
        ctx.attr('extended', this.hasSuper);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function ClassElement(name:String, hasSuper:Boolean, isPublic:Boolean, tagRange:Range, range:Range) {
        super(range);
        this.tag = new ClassTag(name, this, tagRange);
        this.isPublic = isPublic;
        this.hasSuper = hasSuper;
        this.append(new MethodGroupElement());
        this.append(new StaticGroupElement());
        this.append(new InstanceGroupElement(this.instanceMembers));
    }
}

// #########= ClassGroupElement

/**
 * class definitions
 */
public class ClassGroupElement extends BodyElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'classgroup'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ClassElement, 0, true)
        ]);
    }

    /**
     * the constructor
     */
    public function ClassGroupElement() {
        super(null);
    }
}

// #########= ClassInitElement

/**
 * class initializer statement
 */
public class ClassInitElement extends StatementElement {
    /**
     * true if this has a super class
     */
    private var extended:Boolean;

    /**
     * the tag of the class
     */
    private var tag:ClassTag;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'classinit';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            // the super class
            new ElementPattern(ExpressionElement, 1, !this.extended)
        ]);
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} ctx
     */
    override public function generatePython(ctx:PyGenerator):void {
        var writer = new LineWriter();
        writer.write(this.tag.toPython(), false);
        writer.write(' = ', '\\');
        writer.write(this.tag.toFactoryName(), false);
        writer.write('(', '\\');
        if(this.extended) {
            var sup = this.firstChild;
            sup.writePython(writer, false);
        }
        writer.write(')', '\\');
        writer.finalize(ctx);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('tag', this.tag);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function ClassInitElement(extended:Boolean, tag:ClassTag, range:Range) {
        super(range);
        this.extended = extended;
        this.tag = tag;
    }
}

// #########= ComplexLiteralElement

/**
 * class of the complex literal expressions (actually, only the imaginary part)
 */
public class ComplexLiteralElement extends FundamentalLiteralElement {
    /**
    * the source of this
    */
    private var source:String;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'imag';
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        if(parentType >= 12) {
            writer.write('(', false);
        }
        var s = (new ArrayList(this.source));
        // python only allows j-suffix
        s.set(-1, 'j');
        writer.write(s.join(""), false);
        if(parentType >= 12) {
            writer.write(')', false);
        }
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('source', this.source);
        super.dump(ctx);
    }

    /**
    * the constructor
    */
    public function ComplexLiteralElement(source:String, range:Range) {
        super(range);
        this.source = source;
    }
}

// #########= CompoundAssignElement

/**
 * a container of single expression
 *
 * python的复合赋值可能会触发原位计算, 也就是说可能修改目标对象, 这并不合理
 * 因此这里将复合赋值改写成普通赋值的形式
 */
public class CompoundAssignElement extends AssignElement {
    /**
     * operator, a string
     */
    private var operator:String;

    /**
    * walk stage 2
    *
    * 简化表达式
    */
    override public function simplifyExpressions():void {
        // 析出左值后, 将表达式改写成一般赋值形式
        this.checkStruct();
        var left = this.firstChild;
        var right = this.lastChild;

        var ae = new AssignElement(this.range);
        this.replaceWith(ae);

        ae.append(left);
        var rv = left.extractLeftAndDuplicate();

        var re = new BinaryOperatorElement(this.operator, null);
        ae.append(re);
        re.append(rv);
        re.append(right);
        re.simplifyExpressions();
        re.checkStruct();
        ae.checkStruct();
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('operator', this.operator);
        super.dump(ctx);
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} ctx
     */
    override public function generatePython(ctx:PyGenerator):void {
        throw new InternalError('cannot generate Python for CompoundAssignElement');
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function CompoundAssignElement(operator:String, range:Range) {
        super(range);
        var m = new StringMap([['*=', '*'], ['**=', '**'], ['/=', '/'], ['%=', '%'], ['+=', '+'], ['-=', '-'], ['<<=', '<<'], ['>>=', '>>'], ['&=', '&'], ['^=', '^'], ['|=', '|']]);
        if(!m.has(operator)) {
            throw new InternalError('unknown assignment operator ' + operator);
        }
        this.operator = m.get(operator);
    }
}

// #########= ConditionElement

/**
 * the condition
 */
public class ConditionElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'cond';
    }

    /**
     * the statement element this is in
     */
    override public function get theStatement():Element {
        return this.parent.theStatement;
    }

    /** 
     * check if this is a complex expression
     * for statement, returns false
     */
    override public function get complex():Boolean {
        this.checkStruct();
        return this.firstChild.complex;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, false)
        ]);
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        this.checkStruct();
        super.functionalize();
        // 条件式要求严格布尔类型, 也就是只接受true和false
        // 因此要将条件用coerceBoolean(__x_cb)包裹, 进行类型检查以确保严格布尔判断
        var exp = this.firstChild;
        var cc = CallElement.callGlobal(this.theGlobal.enableImplicitBooleanConversion ? '__x_tob' : '__x_cb', exp);
        this.append(cc);
        this.checkStruct();
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        // stage 2 应当由上级元素负责
        throw new InternalError('cannot simplifyExpressions of ConditionElement');
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var exp = this.firstChild;
        exp.writePython(writer, contchr, parentType);
    }

    /**
    * the constructor
    * @param {Range} range, the range of the whole block
    */
    public function ConditionElement(range:Range) {
        super(range);
    }
}

// #########= ContinueElement

/**
 * continue statement
 * labeled continue is not supported
 */
public class ContinueElement extends StatementElement {
    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        ctx.writeln('continue');
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function ContinueElement(range:Range) {
        super(range);
    }
}

// #########= DeleteElement

/**
 * delete statement
 */
public class DeleteElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'return';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, false)
        ]);
    }

    /**
     * walk stage 1
     */
    override public function checkVariables():void {
        if(!(this.firstChild instanceof LvalueElement)) {
            throw new CompileError('only left value can be deleted', this.range);
        }
        super.checkVariables();
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        var right = this.lastChild;
        var writer = new LineWriter();
        writer.write('del ', false);
        right.writePython(writer, '\\');
        writer.finalize(ctx);
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function DeleteElement(range:Range) {
        super(range);
    }
}

// #########= DestructGroupElement

/**
 * base class for destructuring pattern
 */
public class DestructGroupElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'destrabstract'
    }

    /**
     * true if this is a declarator
     */
    private var _declarator:Boolean;

    /**
     * true if this is a declarator
     */
    public function get declarator():Boolean {
        return this._declarator;
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        super.checkStruct();
        // check if the children are declarators
        this.forEachChild(function(e, k, s) {
            if(e instanceof DestructPropertyElement) {
                if(e.declarator !== s.declarator) {
                    throw new InternalError('malformed structure in ' + s.typeName + ' (mismatched declarator property)');
                }
            } else {
                throw new InternalError('malformed structure in ' + s.typeName + ' (unknown child)');
            }
        });
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        throw new InternalError('call abstract simplifyExpressions to ' + this.typeName);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('declare', this.declarator);
        super.dump(ctx);
    }

    /**
    * the constructor
    * @param {Boolean} declarator, true if this is a declarator
    * @param {Range} range, the range of the expresion
    */
    public function DestructGroupElement(declarator:Boolean, range:Range) {
        super(range);
        this._declarator = declarator;
    }
}

// #########= DestructObjectElement

/**
 * destructuring object pattern
 */
public class DestructObjectElement extends DestructGroupElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'destrobj'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(DestructPropertyElement, 0, false),
        ]);
    }

    /**
     * walk stage 2
     *
     * 到了这个阶段, 该元素已经从原来的父级元素(AssignDestructElement)析出
     * 而且, 最后一个元素是由AssignDestructElement放入的右值
     * 如果该元素之前是在另一个解构元素内, 在调用this.simplifyExpressions前就已经先析出成AssignDestructElement了
     */
    override public function simplifyExpressions():void {
        // 先将右值赋给一个临时变量, 再获取对应对象的成员
        var ate = new AssignTempElement(this.theFunction.allocTempVar());
        this.before(ate);
        var right = this.lastChild;
        ate.append(right);
        ate.simplifyExpressions();
        // 分解出自身的子成员
        this.forEachChild(function(e, k, s) {
            e.checkStruct();
            e.append(ate.getLeftElement());
            s.before(e);
            // 如果子成员也是解构的, 则递归处理
            e.simplifyExpressions();
        });
        // this已经不需要了
        this.remove();
    }

    /**
    * the constructor
    * @param {Boolean} declarator, true if this is a declarator
    * @param {Range} range, the range of the expresion
    */
    public function DestructObjectElement(declarator:Boolean, range:Range) {
        super(declarator, range);
    }
}

// #########= DestructPropertyElement

/**
 * member of destructuring object pattern
 * for object literal, use KeyValueElement
 */
public class DestructPropertyElement extends Element {
    /**
     * true if this is a declarator
     */
    private var _declarator:Boolean;

    /**
     * an Attribute, the property name
     */
    private var attribute:Attribute;

    /**
     * true if this is a declarator
     */
    public function get declarator():Boolean {
        return this._declarator;
    }

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'destrprop'
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof DestructObjectElement)) {
            throw new InternalError('malformed structure in DestructPropertyElement (not in DestructObjectElement)');
        }
        var e = this.firstChild;
        if(e !== this.lastChild || !(e instanceof LvalueElement || e instanceof DestructGroupElement)) {
            throw new InternalError('malformed structure in ' + this.typeName + ' (unknown child)');
        }
        if(e.declarator !== this.declarator) {
            throw new InternalError('malformed structure in ' + this.typeName + ' (disagreed declarator property)');
        }
    }

    /**
     * scan the variables in this expression
     * (stage 1)
     */
    override public function checkVariables():void {
        this.checkStruct();
        var e = this.firstChild;
        if(e instanceof LvalueElement) {
            e.checkWrite();
        } else {
            e.checkVariables();
        }
    }

    /**
     * walk stage 2
     *
     * 到了这个阶段, 该元素已经从原来的父级元素(DestructObjectElement)析出
     * 而且, 最后一个元素是右值的对象(存储于临时变量中)
     */
    override public function simplifyExpressions():void {
        // 到了解构的成员, 就和一般赋值是一样的, 先执行左值的表达式, 再执行getter
        // 当然, 如果该项又是一个解构, 那还是按解构的顺序
        var e = this.firstChild;

        var ro = this.lastChild;
        var re = new AttributeElement(this.attribute, null);
        re.append(ro);

        if(e instanceof LvalueElement) {
            // 如果是左值表达式(一般成员), 就转换为一般的赋值
            var dae = new AssignElement(this.range);
            this.before(dae);
            dae.append(e);
            dae.append(re);
            dae.simplifyExpressions();
        } else if(e instanceof DestructGroupElement) {
            // 如果左值表达式是另一个解构, 就先把当前值赋给一个临时变量,
            var ate = new AssignTempElement(this.theFunction.allocTempVar());
            this.before(ate);
            ate.append(re);
            // 再递归地解构这个临时变量
            this.before(e);
            e.append(ate.getLeftElement());
            e.simplifyExpressions();
        } else {
            throw new InternalError('malformed structure in DestructPropertyElement (unknown child)');
        }
        // this已经不需要了
        this.remove();
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('attribute', this.attribute);
        ctx.attr('declare', this.declarator);
        super.dump(ctx);
    }

    /**
    * the constructor
    * @param {Boolean} declarator, true if this is a declarator
    * @param {Range} range, the range of the expresion
    */
    public function DestructPropertyElement(declarator:Boolean, attribute:Attribute, range:Range) {
        super(range);
        this._declarator = declarator;
        this.attribute = attribute;
    }
}

// #########= DoWhileElement

/**
 * while statement
 */
public class DoWhileElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'dowhile'
    }

    /**
     * the required struture of this
     *
     * like while, the condition must be placed first
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ConditionElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * walk stage 2
     */
    public function simplifyExpressions():void {
        this.checkStruct();
        var cond = this.firstChild;
        cond.checkStruct();
        var body = this.lastChild;

        // 将自身替换成while(true), 在内部进行退出判断
        var nwhile = new WhileElement(this.range);
        this.replaceWith(nwhile);

        nwhile.append (cond);
        var conde = cond.firstChild;
        conde.replaceWith(new BooleanLiteralElement(true, null));

        var ife = new IfBlockElement(null);
        body.append(ife);

        var iife = new IfElement(null);
        ife.append(iife);
        var acond = new ConditionElement(null);
        iife.append(acond);
        // break unless cond
        var acondn = new NotOperatorElement(null);
        acond.append(acondn);
        acondn.append(conde);

        var atrue = new BodyElement(null);
        iife.append(atrue);
        var abreak = new BreakElement(null);
        atrue.append(abreak);

        // 此时iife中复杂的条件也会在这一步简化
        super.simplifyExpressions();
    }

    /**
    * put the python code of the contained expression into writer
    *
    * @param {PyGenerator} gen
    */
    override public function generatePython(gen:PyGenerator):void {
        throw new InternalError('generate python for do-while');
    }

    /**
     * the constructor
     */
    public function DoWhileElement(range:Range) {
        super(range);
    }

}

// #########= ElifElement

/**
 * else-if statement
 *
 * 单个else-if的语句
 * 该元素不能单独存在, 而需要放入一个IfBlockElement中
 */
public class ElifElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'elif'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ConditionElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof IfBlockElement)) {
            throw new InternalError('malformed structure in IfElement (not in IfBlockElement)');
        }
        super.checkStruct();
    }

    /**
     * indicates if this a complex expression
     */
    override public function get complex():Boolean {
        return this.firstChild.complex;
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        this.checkStruct();
        if(this.complex) {
            throw new InternalError('simplify a elif with complex condition');
        }
        var body = this.lastChild;
        body.simplifyExpressions();
        this.checkStruct();
    }

    /**
    * put the python code of the contained expression into writer
    *
    * @param {PyGenerator} gen
    */
    override public function generatePython(ctx:PyGenerator):void {
        var cond = this.firstChild.firstChild;
        var body = this.lastChild;
        var writer = new LineWriter();
        writer.write('elif ', false);
        cond.writePython(writer, '\\', 1);
        writer.write(':', false);
        writer.finalize(ctx);
        ctx.tab();
        body.generatePython(ctx);
        ctx.TAB();
    }

    /**
     * the constructor
     */
    public function ElifElement(range:Range) {
        super(range);
    }
}

// #########= ElseElement

/**
 * else statement
 *
 * 单个else的语句
 * 该元素不能单独存在, 而需要放入一个IfBlockElement中
 */
public class ElseElement extends BodyElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'else'
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof IfBlockElement)) {
            throw new InternalError('malformed structure in IfElement (not in IfBlockElement)');
        }
        super.checkStruct();
    }

    /**
     * put the python code of the contained expression into writer
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        ctx.writeln('else:');
        ctx.tab();
        super.generatePython(ctx);
        ctx.TAB();
    }

    /**
     * the constructor
     */
    public function ElseElement(range:Range) {
        super(range);
    }
}

// #########= ExpressionStatementElement

/**
 * a container of single expression
 *
 * 存放简单表达式, 即值不被他用的表达式, 如a()
 */
public class ExpressionStatementElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'exprstat';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, false)
        ]);
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        // super() can only be a stand-alone statement
        // this will be forwarded to constructor's body
        return this.parent.allowSuperCall;
    }

    /**
    * walk stage 2
    *
    * 简化表达式
    */
    override public function simplifyExpressions():void {
        super.simplifyExpressions();
        // 如果简化后该表达式已经没有副作用了, 那么就可以去掉
        // 比如a++会被全部简化出去, 只剩临时变量
        if(this.lastChild.tempVarOnly) {
            this.remove();
        }
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        var writer = new LineWriter();
        var right = this.lastChild;
        right.writePython(writer, '\\');
        writer.finalize(ctx);
    }

    /**
    * the constructor
    * @param {ExpressionElement} origin, the original expression
    * @param {Range} range, the range of the expresion
    */
    public function ExpressionStatementElement(range:Range) {
        super(range);
    }
}

// #########= FinallyElement

/**
 * finally statement
 *
 * 单个finally的语句
 * 不要直接使用这个, 需要放入一个TryBlockElement中
 */
public class FinallyElement extends BodyElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'finally'
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof TryBlockElement)) {
            throw new InternalError('malformed structure in TryElement (not in TryBlockElement)');
        }
        super.checkStruct();
        this.checkJump(this);
    }

    /**
     * check if there are jump statements
     *
     * Although the jump statement in finally block only cause a warning in most compliers,
     * YAGS enforce this rule.
     */
    private function checkJump(e:Element):void {
        if(e instanceof ReturnElement ||
           e instanceof BreakElement ||
           e instanceof ContinueElement) {
            throw new CompileError('Jump statements occur in finally block', this.range);
        }
        if(e instanceof ExpressionElement) {
            return;
        }
        var cj = this.checkJump;
        e.forEachChild(function(ee, k, a) {
            cj(ee);
        });
    }

    /**
    * put the python code of the contained expression into writer
    *
    * @param {PyGenerator} gen
    */
    override public function generatePython(ctx:PyGenerator):void {
        ctx.writeln('finally:');
        ctx.tab();
        super.generatePython(ctx);
        ctx.TAB();
    }

    /**
     * the constructor
     */
    public function FinallyElement(range:Range) {
        super(range);
    }
}

// #########= FunctionElement

/**
 * Base class of the statements with parameter
 *
 * FunctionElement是函数定义的基类, 这包括所有含调用参数的元素
 * 具体的函数分为FunctionDeclarationElement(函数定义), FunctionExpressionElement(函数表达式)和MethodElement(方法)
 * 三者的区别在于会产生不一样的tag, 此外MethodElement的第一个参数是this
 * 
 * 目前默认参数只允许"常量", 这包括数字, 字符串, 布尔值的字面量, null或者是由常量构成的表达式(包括数组)
 * 由于此等限制, 函数只需要一个变量作用域, 而不需要给参数设计独立的作用域
 *
 * 一个一般函数由如下几部分组成
 * 1. 内层函数定义: 所有该函数内的函数(表达式或定义)均放入此区域, 包括函数表达式(函数表达式原来的位置放一个VarElement指向该表达式)
 * 2. 变量定义: 对本级定义的闭包变量进行初始化
 * 3. 参数展开: 对于闭包访问的参数进行重命名(即赋值给变量槽)
 * 4. 函数正文: 即函数体
 * 5. 变量补定义: 对于没有被闭包访问, 又没有在本级写入的局部变量进行定义. 后续考虑对这种情况提出警告或错误.
 * 其中, 内层函数定义(FunctionGroupElement), 参数展开(ParameterGroupElement)和函数正文(FunctionBodyElement)使用专门的元素进行表示, 而其他部分只在代码生成时输出.
 */
public class FunctionElement extends BaseFunctionElement {
    /**
     * the tag of this
     */
    public var tag:FunctionTag = null;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'function';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(FunctionGroupElement, 1, false),
            // for method, use MethodParameterGroupElement
            new ElementPattern(ParameterGroupElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * the function defined in this function
     */
    override public function get functionDefinitions():FunctionGroupElement {
        this.checkStruct();
        var e = this.firstChild;
        return e;
    }

    /**
     * the parameter group
     */
    public function get parameters():ParameterGroupElement {
        this.checkStruct();
        var e = this.firstChild.nextSibling;
        return e;
    }

    /**
     * the body
     */
    override public function get body():BodyElement {
        this.checkStruct();
        var e = this.lastChild;
        return e;
    }

    /**
     * find the variable by name
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     *
     * 查找变量, 一些子类可能需要超控该方法
     */
    override public function referVar(name:String, range:Range = null):Variable {
        // check if exists
        var v = this.getLocal(name);
        if(v !== null) {
            return v;
        }
        // check if function tag
        if(this.tag.name !== null && this.tag.name === name) {
            return this.tag;
        }
        return this.parentFunction.referVar(name, range);
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(gen:PyGenerator):void {
        gen.blank();
        var sline = new LineNumber();
        gen.logLineNumber(sline);

        // 函数声明
        var writer = new LineWriter();
        writer.write('def ', false);
        writer.write(this.tag.toPython(), false);
        writer.write('(', '');
        this.parameters.toPrameterList(writer, '');
        writer.write('):', false);
        writer.finalize(gen);

        gen.tab();

        // 内层函数定义
        this.functionDefinitions.generatePython(gen);

        // 变量定义
        gen.blank();
        // 只有在被内层函数写入的(闭包)变量才需要定义
        this.forEachLocalVar(function(v, n, s) {
            if(!v.closure) {
                return;
            }
            gen.writeln(v.toRawPython() + ' = __x_var()');
        });
        // 参数展开
        this.parameters.generatePython(gen);

        // 函数体
        this.body.generatePython(gen);

        // 变量补定义
        // 如果在本级声明, 又没有赋值的变量, 则进行补定义
        // 这样在读取该变量时会抛出异常
        // 未来可以考虑对于这样的变量提出警告或错误
        var nwv = false;
        this.forEachLocalVar(function(v, n, o) {
            if(!v.closure && !v.assigned) {
                nwv = true;
                return false;
            }
        });
        if(nwv) {
            gen.comment('Uninitialized variable:');
            gen.writeln('return');
            this.forEachLocalVar(function(v, n, o) {
                if(!v.closure && !v.assigned) {
                    gen.writeln(v.toRawPython() + ' = 0');
                }
            });
        }

        gen.TAB();

        gen.comment(
            'end function %s (line %l)',
            this.tag.toComment(),
            sline
        );
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('tag', this.tag);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function FunctionElement(range:Range) {
        super(range);
    }
}

// #########= FunctionDefinitionElement

/**
 * function definition
 * 
 * 函数定义
 * 注意, FunctionDefinitionElement应放入上级函数的定义区(functionDefinitions)内
 * 不管原来的函数定义在什么位置
 */
public class FunctionDefinitionElement extends FunctionElement {
    /**
     * true if this is a public declaration
     */
    private var isPublic:Boolean = false;

    /**
     * declare this variable
     * (pre-stage1)
     *
     * 声明变量. 
     */
    override public function declareVariable():void {
        // 注册当前函数的tag
        this.parentFunction.registerFunctionDefinition(this.tag, this.tag.range);
        // 如果是公开的, 就向全局注册公开成员
        if(this.isPublic) {
            if(!(this.parentFunction instanceof GlobalElement)) {
                throw new InternalError('Public member not in global');
            }
            this.theGlobal.declarePublic(this.tag.name, this.tag.range);
        }
        super.declareVariable();
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('public', this.isPublic);
        super.dump(ctx);
    }

    /**
     * the constructor
     * @param {String} name
     * @param {Boolean} isPublic
     * @param {Range} tagRange
     * @param {Range} range
     */
    public function FunctionDefinitionElement(name:String, isPublic:Boolean, tagRange:Range, range:Range) {
        super(range);
        this.tag = new FunctionTag(name, this, tagRange);
        this.isPublic = isPublic;
        this.append(new FunctionGroupElement());
        this.append(new ParameterGroupElement());
        this.append(new BodyElement(null));
    }
}

// #########= FunctionExpressionElement

/**
 * function expression
 * 
 * 函数表达式
 * 在Python中, 并没有函数表达式, 因此只能使用一个具名函数来表示
 * 注意, FunctionExpressionElement应放入上级函数的定义区(functionDefinitions)内
 * 而在原函数表达式的位置应使用一个VarElement替代
 */
public class FunctionExpressionElement extends FunctionElement {
    /**
     * the constructor
     * @param {String} name, null for anonymous function expression
     * @param {Range} range
     */
    public function FunctionExpressionElement(name:String, tagRange:Range, range:Range) {
        super(range);
        this.tag = new FunctionExpTag(name, this, tagRange);
        this.append(new FunctionGroupElement());
        this.append(new ParameterGroupElement());
        this.append(new BodyElement(null));
    }
}

// #########= FunctionGroupElement

/**
 * function definitions
 *
 * 函数体中内部函数的定义
 */
public class FunctionGroupElement extends BodyElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'functiongroup'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(FunctionElement, 0, true)
        ]);
    }

    /**
     * the constructor
     */
    public function FunctionGroupElement() {
        super(null);
    }
}

// #########= GlobalElement

/*
 * element of the top-level (global)
 *
 * 顶层(全局)的类
 */
public class GlobalElement extends BaseFunctionElement {
    /**
     * map for exported variables
     *
     * these variables should also be set in vars
     */
    private var exports:StringMap = new StringMap();

    /**
     * map for built-in variables
     *
     * these variables should not be set in vars
     */
    private var builtins:StringMap = new StringMap();

    /**
     * id of the next function
     */
    private var functionCounter:Number = 0;

    /**
     * compile option enableImplicitBooleanConversion
     */
    public var enableImplicitBooleanConversion:Boolean = false;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'global';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        // 定义在全局的函数同样是提升的, 
        return new ArrayList([
            new ElementPattern(FunctionGroupElement, 1, false),
            new ElementPattern(ClassGroupElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * the function defined in this function
     */
    override public function get functionDefinitions():FunctionGroupElement {
        this.checkStruct();
        var e = this.firstChild;
        return e;
    }

    /**
     * the function defined in this function
     */
    public function get classDefinitions():ClassGroupElement {
        this.checkStruct();
        var e = this.firstChild.nextSibling;
        return e;
    }

    /**
     * the body
     */
    override public function get body():BodyElement {
        this.checkStruct();
        var e = this.lastChild;
        return e;
    }

    /**
     * the parent element of this
     */
    override public function get parent():Element {
        return null;
    }

    /**
     * the global element this is in
     *
     * 该语句所在的全局, 用于变量检查
     */
    override public function get theGlobal():GlobalElement {
        return this;
    }

    /**
     * the class element this is in
     *
     * 该语句所在的类, 用于变量检查
     * 如果该语句不在类里面(比如全局函数), 那就由global返回null
     */
    override public function get theClass():ClassElement {
        return null;
    }

    /**
     * the parent function of this
     */
    override public function get parentFunction():BaseFunctionElement {
        // 全局元素需要超控这个函数, 并返回null
        return null;
    }

    /**
     * true if this can be refered here
     */
    override public function get allowThis():Boolean {
        return false;
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        return false;
    }

    /**
     * assign an unique id for each function
     */
    public function allocFunctionId():Number {
        return this.functionCounter++;
    }

    /**
     * register class definition
     * @param {ClassTag} tag, the tag of class
     * @param {Range} range
     */
    public function registerClassDefinition(tag:ClassTag, range:Range = null):void {
        // check if exists
        var name = tag.name;
        var v = this.getLocal(name);
        if(v !== null) {
            throw new ConflictError("Duplicate class definition: %s", range, v.range, name);
        }
        this.setLocal(name, tag);
    }

    /**
     * declare the member as public
     */
    public function declarePublic(name:String, range:Range):void {
        var ai = new Identifier(name, range);
        if(ai.isSpecial) {
            throw new CompileError('public name must be a valid Python identifier: %s', range, name);
        }
        var an = new ArrayList(name);
        if(an.get(0) === '_' && an.get(1) == '_') {
            // 以下划线加数字开头的变量名是保留的
            // 局部变量不受影响, 因为会自动重命名
            throw new CompileError('public name starts with double underscore is reserved: %s', range, name);
        }
        var ov = this.exports.get(name, false);
        if(ov) {
            throw new ConflictError('Duplicate public variable declaration: %s', range, ov.range, name);
        }
        this.exports.set(name, true);
    }

    /**
     * find the variable by name
     * @param {String} name, the identifier of the variable
     * @param {Range} range, original range object of the identifier from the parser, used for error reporting
     *
     * 对于未定义的变量, 不再向上一级查找(因为没有上一级), 而是报错
     */
    override public function referVar(name:String, range:Range = null):Variable {
        if(name === 'eval') {
            // 禁止eval
            throw new CompileError('Eval is evil', range);
        }
        // check if exists
        var v = this.getLocal(name);
        if(v !== null) {
            return v;
        }
        // 查找内置(built-in)作用域
        var v2 = this.builtins.get(name, null);
        if(v2 !== null) {
            return v2;
        }
        throw new CompileError('%s is not defined', range, name);
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(gen:PyGenerator):void {
        // 不设置unicode_literals是因为一些内部字符串如标识符名称在Python2中要用二进制串表示
        gen.comment('-*- coding: utf-8 -*-');
        gen.writeln('from __future__ import print_function, absolute_import, division, generators');
        gen.blank();
        // 声明导出的变量
        var exp = new ArrayList();
        this.exports.forEach(function(v, n, a) {
            exp.push(n);
        });
        var writer;
        writer = new LineWriter();
        writer.write('__all__ = (', false);
        if(exp.length > 0) {
            exp.forEach(function(v, k, a) {
                if(k > 0) {
                    writer.write(', ', '\\');
                }
                writer.write('"' + v + '"', false);
            });
            if(exp.length === 1) {
                // trailing comma is required for single element
                writer.write(',', false);
            }
        }
        writer.write(')', false);
        writer.finalize(gen);

        gen.blank();
        gen.blank();
        gen.writeln('def __():');
        gen.tab();

        // 导入超全局变量
        gen.writeln('from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_at_has, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN');
        // 生成import函数(把__package__绑定为import_module的第二参数)
        gen.writeln('__x_imp = __x_imf(__name__)');

        // 声明导出的变量
        if(exp.length > 0) {
            writer = new LineWriter();
            writer.write('global ', false);
            exp.forEach(function(v, k, a) {
                if(k > 0) {
                    writer.write(', ', '\\');
                }
                writer.write(v, false);
            });
            writer.finalize(gen);
        }

        // 内层函数定义
        gen.blank();
        gen.comment('function definitions:');
        this.functionDefinitions.generatePython(gen);

        // 类定义
        gen.blank();
        gen.comment('class definitions:');
        this.classDefinitions.generatePython(gen);

        // 变量定义
        // 只有在被内层函数写入的(闭包)变量才需要定义
        this.forEachLocalVar(function(v, n, s) {
            if(!v.closure) {
                return;
            }
            gen.writeln(v.toRawPython() + ' = __x_var()');
        });

        // 函数体
        gen.blank();
        this.body.generatePython(gen);

        // 变量补定义
        // 如果在本级声明, 又没有赋值的变量, 则进行补定义
        // 这样在读取该变量时会抛出异常
        // 未来可以考虑对于这样的变量提出警告或错误
        var nwv = false;
        this.forEachLocalVar(function(v, n, o) {
            if(!v.closure && !v.assigned) {
                nwv = true;
                return false;
            }
        });
        if(nwv) {
            gen.comment('Uninitialized variable:');
            gen.writeln('return');
            this.forEachLocalVar(function(v, n, o) {
                if(!v.closure && !v.assigned) {
                    gen.writeln(v.toRawPython() + ' = 0');
                }
            });
        }

        gen.TAB();
        gen.comment('program end');
        gen.blank();
        gen.blank();
        gen.writeln('__()');
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('function-counter', this.functionCounter);
        super.dump(ctx);
    }

    private function setBuiltins(s:String, k:Number, a:ArrayList):void {
        this.builtins.set(s, new BuiltinVar(s, this));
    }

    /**
     * the constructor
     */
    public function GlobalElement(range:Range) {
        super(range);
        var bis = this.builtins;
        var self
        (new ArrayList(["ArithmeticError", "AssertionError", "AttributeError", "BaseException", "BufferError", "BytesWarning", "DeprecationWarning", "EOFError", "Ellipsis", "EnvironmentError", "Exception", "False", "FloatingPointError", "FutureWarning", "GeneratorExit", "IOError", "ImportError", "ImportWarning", "IndentationError", "IndexError", "KeyError", "KeyboardInterrupt", "LookupError", "MemoryError", "NameError", "None", "NotImplemented", "NotImplementedError", "OSError", "OverflowError", "PendingDeprecationWarning", "ReferenceError", "RuntimeError", "RuntimeWarning", "StandardError", "StopIteration", "SyntaxError", "SyntaxWarning", "SystemError", "SystemExit", "TabError", "True", "TypeError", "UnboundLocalError", "UnicodeDecodeError", "UnicodeEncodeError", "UnicodeError", "UnicodeTranslateError", "UnicodeWarning", "UserWarning", "ValueError", "Warning", "ZeroDivisionError", "__debug__", "__doc__", "__import__", "__name__", "__package__", "abs", "all", "any", "apply", "basestring", "bin", "bool", "buffer", "bytearray", "bytes", "callable", "chr", "classmethod", "cmp", "coerce", "compile", "complex", "copyright", "credits", "delattr", "dict", "dir", "divmod", "enumerate", "eval", "execfile", "exit", "file", "filter", "float", "format", "frozenset", "getattr", "globals", "hasattr", "hash", "help", "hex", "id", "input", "int", "intern", "isinstance", "issubclass", "iter", "len", "license", "list", "locals", "long", "map", "max", "memoryview", "min", "next", "object", "oct", "open", "ord", "pow", "print", "property", "quit", "range", "raw_input", "reduce", "reload", "repr", "reversed", "round", "set", "setattr", "slice", "sorted", "staticmethod", "str", "sum", "super", "tuple", "type", "unichr", "unicode", "vars", "xrange", "zip", "BlockingIOError", "BrokenPipeError", "ChildProcessError", "ConnectionAbortedError", "ConnectionError", "ConnectionRefusedError", "ConnectionResetError", "FileExistsError", "FileNotFoundError", "InterruptedError", "IsADirectoryError", "NotADirectoryError", "PermissionError", "ProcessLookupError", "RecursionError", "ResourceWarning", "StopAsyncIteration", "TimeoutError", "__build_class__", "__loader__", "__spec__", "ascii", "exec", "NaN", "Infinity"])).forEach(this.setBuiltins);

        this.append(new FunctionGroupElement());
        this.append(new ClassGroupElement());
        this.append(new BodyElement(null));
    }
}

// #########= IfBlockElement

/**
 * if-elseif-else package
 *
 * if的语句包, 存放整个if-else if-else组合
 *
 * es里的if只有if和else, else if实际上是两者结合起来的
 * 但是如果每个else if都这样表示, 在python里可能会造成非常壮观的缩进
 * 因此需要尽量把else if转换成py的elif
 *
 * IfBlockElement - if语句的整体, 由以下三种成员构成
 * IfElement - 代表if, 具有条件(condition)表达式
 * ElifElement - 代表else if, 具有条件表达式
 * ElseElement - 代表else, 只能在最后
 *
 * 最初形成if ir的时候, 需要将所有的else if用ElifElement表示
 * 如果发现ElifElement的条件是复杂表达式, 那就会将这个else if语句重新转换回else和if
 * 以便放置简化条件表达式析出的语句
 */
public class IfBlockElement extends StatementElement {
    private var simplified:Boolean = false;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'ifgroup'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(IfElement, 1, false),
            new ElementPattern(ElifElement, 0, true),
            new ElementPattern(ElseElement, 1, true)
        ]);
    }

    /**
     * walk stage 2
     *
     * 条件表达式可能是复杂的表达式, 需要简化
     * 如果if的条件是复杂的, 可以析出到if语句之前(通过theStatement可以传递到该IfBlockElement)
     * 如果某个else if的条件是复杂的, 就要将本句改成if, 连同之后的所有子句全部放入新的else块中.
     * else不可能是复杂的, 只要在其内简化语句即可.
     */
    override public function simplifyExpressions():void {
        if(this.simplified) {
            throw new InternalError('simplify if again');
        }
        this.simplified = true;
        this.checkStruct();

        // simplify if
        this.firstChild.simplifyExpressions();

        // meeted complex else if
        var mcei = false;
        // put the complex else-if and the rest elements into if2
        // and put if2 into else2
        var if2 = null;
        var else2 = null;

        this.forEachChild(function(e, k, self) {
            e.checkStruct();
            if(k === 0) {
                // if
                return;
            }
            if(mcei) {
                if2.append(e);
                return;
            }
            // else when mcei is false (no complex else-if)
            if(e instanceof ElseElement) {
                e.simplifyExpressions();
                return;
            }
            // else-if
            if(!e.complex) {
                e.simplifyExpressions();
                return;
            }
            mcei = true;
            // else-if with complex condition
            else2 = new ElseElement(null);
            e.replaceWith(else2);
            if2 = new IfBlockElement(null);
            else2.append(if2);
            // convert the else-if into if
            var elif2 = new IfElement(null);
            if2.append(elif2);
            var cond2 = e.firstChild; // the condition
            var body2 = e.lastChild; // the body
            elif2.append(cond2);
            elif2.append(body2);
        });

        // recursive simplify the new else if needed
        if(mcei) {
            else2.simplifyExpressions();
        }
        this.checkStruct();
    }

    /**
    * put the python code of the contained expression into writer
    *
    * @param {PyGenerator} gen
    */
    override public function generatePython(gen:PyGenerator):void {
        var sline = new LineNumber();
        gen.logLineNumber(sline);
        this.forEachChild(function(e, k, t) {
            e.generatePython(gen);
        });
        gen.comment('end if (line %l)', sline);
    }

    /**
     * the constructor
     */
    public function IfBlockElement(range:Range) {
        super(range);
    }
}

// #########= IfElement

/**
 * if statement
 *
 * 单个if的语句
 * 该元素不能单独存在, 而需要放入一个IfBlockElement中
 */
public class IfElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'if'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ConditionElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof IfBlockElement)) {
            throw new InternalError('malformed structure in IfElement (not in IfBlockElement)');
        }
        super.checkStruct();
    }

    /**
     * the statement element this is in
     */
    override public function get theStatement():Element {
        // if can extract the condition before it
        return this.parent.theStatement;
    }

    /**
     * indicates if this a complex expression
     */
    override public function get complex():Boolean {
        return this.firstChild.complex;
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        this.checkStruct();
        this.firstChild.checkStruct();
        // simplify the condition directly
        var cond = this.firstChild.firstChild;
        var body = this.lastChild;
        cond.simplifyExpressions();
        body.simplifyExpressions();
        this.checkStruct();
    }

    /**
     * put the python code of the contained expression into writer
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        var cond = this.firstChild.firstChild;
        var body = this.lastChild;
        var writer = new LineWriter();
        writer.write('if ', false);
        cond.writePython(writer, false, 1);
        writer.write(':', false);
        writer.finalize(ctx);
        ctx.tab();
        body.generatePython(ctx);
        ctx.TAB();
    }

    /**
     * the constructor
     */
    public function IfElement(range:Range) {
        super(range);
    }
}

// #########= ImportElement

/**
 * import callee
 * import()
 */
public class ImportElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'import';
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof CallElement)) {
            throw new InternalError('malformed structure in ImportElement (not in CallElement)');
        }
        super.checkStruct();
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return false;
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        // __x_imp is importlib.import_module with __package__ bound as the second parameter
        writer.write('__x_imp', contchr);
    }

    /**
     * the constructor
     */
    public function ImportElement(range:Range) {
        super(range);
    }
}

// #########= InstanceGroupElement

/**
 * super constructor
 */
public class InstanceGroupElement extends BaseFunctionElement {
    /**
     * same object as this.theClass.instanceMembers
     */
    private var instanceMembers:StringMap;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'instanceinit';
    }

    /**
     * true if this can be refered here
     */
    override public function get allowThis():Boolean {
        return this.parent.allowThis;
    }

    /**
     * true if super can be refered here
     */
    override public function get allowSuper():Boolean {
        return this.parent.allowSuper;
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        return this.parent.allowSuperCall;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(FunctionGroupElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof ClassElement)) {
            throw new InternalError('malformed structure in InstanceGroupElement (not in ClassElement)');
        }
        super.checkStruct();
    }

    /**
     * the function defined in this function
     */
    override public function get functionDefinitions():FunctionGroupElement {
        this.checkStruct();
        var e = this.firstChild;
        return e;
    }

    /**
     * the body
     */
    override public function get body():BodyElement {
        this.checkStruct();
        var e = this.lastChild;
        return e;
    }

    /**
     * register local function definition
     * @param {FunctionTag} tag, the tag of function
     * @param {Range} range
     */
    override public function registerFunctionDefinition(tag:FunctionTag, range:Range = null):void {
        throw new InternalError('register function definition in class property initializer');
    }

    /**
     * register local variable and return it
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     */
    override public function registerLocalVar(name:String, range:Range = null):LocalVar {
        throw new InternalError('register local variable in class property initializer');
        return null;
    }

    /**
     * find the variable by name
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     */
    override public function referVar(name:String, range:Range = null):Variable {
        return this.theClass.referVar(name, range);
    }

    /**
     * generate python code of the class factory
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(gen:PyGenerator):void {
        gen.blank();
        var sline = new LineNumber();
        gen.logLineNumber(sline);

        gen.writeln('def __csu(this, *argv):');

        gen.tab();

        this.functionDefinitions.generatePython(gen);

        gen.blank();

        // check if there are private members
        var haspi = false;
        this.instanceMembers.forEach(function(p, k, s) {
            if(p.isPrivate) {
                haspi = true;
                return false;
            }
        });
        if(haspi) {
            gen.comment('create the private field');
            gen.writeln('__cpm.create(this)');
        }

        gen.comment('initialize properties');
        this.body.generatePython(gen);

        gen.comment('super');
        gen.writeln('super(__clsT, this).__init__(*argv)');

        gen.TAB();

        gen.comment(
            'end instance initializer and super constructor __csu (line %l)',
            sline
        );
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function InstanceGroupElement(instanceMembers:StringMap) {
        super(null);
        this.instanceMembers = instanceMembers;
        this.append(new FunctionGroupElement());
        this.append(new BodyElement(null));
    }
}

// #########= InstanceInitializerElement

/**
 * declaration of instance property
 */
public class InstanceInitializerElement extends StatementElement {
    /**
     * an Attribute, the property name
     */
    private var attribute:Attribute;

    /**
     * true if this is a public propeerty
     */
    private var isPublic:Boolean;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'instanceprop';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, true)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.theFunction instanceof InstanceGroupElement)) {
            throw new InternalError('malformed structure in InstanceInitializerElement (not in InstanceGroupElement)');
        }
        super.checkStruct();
    }

    /**
     * true if this is a initializer
     */
    public function get isInitializer():Boolean {
        this.checkStruct();
        return this.firstChild !== null;
    }

    /**
     * declare this variable
     * (pre-stage1)
     */
    override public function declareVariable():void {
        this.checkStruct();
        this.theClass.registerProperty(this.attribute.name, this.isPublic, false, this.attribute.range);
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        // convert to assignment
        if(this.isInitializer) {
            var aae = new AssignElement(this.range);
            this.replaceWith(aae);
            var attr = new AttributeElement(this.attribute, this.attribute.range);
            aae.append(attr);
            attr.append(new ThisElement(null));
            aae.append(this.firstChild);
        }
        this.remove();
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('attribute', this.attribute);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function InstanceInitializerElement(attribute:Attribute, isPublic:Boolean, range:Range) {
        super(range);
        this.isPublic = isPublic;
        this.attribute = attribute;
    }
}

// #########= ItemElement

/**
 * member expression a[b]
 */
public class ItemElement extends LvalueElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'item';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 2, false)]);
    }

    /**
    * walk stage 2
    *
    * 简化表达式, 提升复杂表达式, 使之能被py表示
    */
    override public function simplifyExpressions():void {
        this.checkStruct();
        if(!this.complex) {
            return
        }
        // 为了保证执行顺序, 须将基值析出
        var left = this.firstChild;
        var right = this.lastChild;
        var atel = left.replaceWithTemp();
        this.insertTempAssign(atel);

        right.simplifyExpressions();
        this.checkStruct();
    }

    /**
     * extrace the left's object and index
     * (stage 2)
     */
    override public function extractLeft():void {
        this.checkStruct();
        var left = this.firstChild;
        var right = this.lastChild;
        var atel = left.replaceWithTemp();
        this.insertTempAssign(atel);
        var ater = right.replaceWithTemp();
        this.insertTempAssign(ater);
        this.checkStruct();
    }

    /**
     * extrace the left's object and index and return the duplication of this
     * (stage 2)
     */
    override public function extractLeftAndDuplicate():LvalueElement {
        this.checkStruct();

        var left = this.firstChild;
        var right = this.lastChild;
        // 因为要使用两次, 所以不能返回空值
        var atel = left.replaceWithTemp(false);
        this.insertTempAssign(atel);
        var ater = right.replaceWithTemp(false);
        this.insertTempAssign(ater);
        this.checkStruct();

        var v = new ItemElement(this.range);
        v.append(atel.getLeftElement());
        v.append(ater.getLeftElement());
        v.checkStruct();
        return v;
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        // 自身是不用加括号的, 因为最多出现在同级元素(调用或成员)的左边

        var object = this.firstChild;
        var index = this.lastChild;
        object.writePython(writer, '\\', 12);
        writer.write('[', false);
        index.writePython(writer, '\\', 0);
        writer.write(']', contchr);
    }

    /**
     * the constructor
     */
    public function ItemElement(range:Range) {
        super(range);
    }
}

// #########= KeyValueElement

/**
 * key-value pair for object (dict) literal
 * for left value (destructuring object), use DestructPropertyElement
 */
public class KeyValueElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'kvpair';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 2, false)]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof ObjectLiteralElement)) {
            throw new InternalError('malformed structure in KeyValueElement (not in ObjectLiteralElement)');
        }
        super.checkStruct();
    }

    /**
     * walk stage 2
     *
     * 简化表达式, 提升复杂表达式, 使之能被py表示
     */
    override public function simplifyExpressions():void {
        // 不可能调用该函数
        // 父元素会把简化的工作完成
        throw new InternalError('called simplifyExpressions of KeyValueElement');
    }

    /**
     * extrace this
     * (stage 2)
     */
    override public function replaceWithTemp(optional = true):AssignTempElement {
        // 不可能调用该函数
        // 父元素会把简化的工作完成
        throw new InternalError('called replaceWithTemp of KeyValueElement');
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var key = this.firstChild;
        var value = this.lastChild;
        // 自身是不用加括号的, 因为最多出现在同级元素(调用或成员)的左边
        key.writePython(writer, false, 11);
        writer.write(': ', '');
        value.writePython(writer, false, 11);
    }

    /**
     * the constructor
     */
    public function KeyValueElement(range:Range) {
        // NOTE: 对于非计算键, 在由AST转换为IR时就要将其转为字符串
        super(range);
    }
}

// #########= MagicCallElement

/**
 * call the dot-at function
 *
 * xxx.@yyy(...)
 * currently, only callee is allowed for dot-at member
 */
public class MagicCallElement extends ExpressionElement {
    /**
     * the name of the method
     */
    private var name;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'magiccall';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, false), // object
            new ElementPattern(ArgumentElement, 1, false), // arguments
        ]);
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        this.checkStruct();
        super.functionalize();
        var cc = new CallElement(this.range);
        this.replaceWith(cc);
        var o = VarElement.getGlobalVar('__x_at_' + this.name);
        cc.append(o);
        var argv = this.lastChild;
        var self = this.firstChild;
        argv.prepend(self);
        cc.append(argv);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('name', this.name);
        super.dump(ctx);
    }

    /**
    * the constructor
    */
    public function MagicCallElement(name:String, range:Range) {
        // fl doesn't allow super after throw
        super(range);
        var allowFns = new StringMap();
        allowFns.sets(['apply', 'bind', 'drop', 'every', 'filter', 'find', 'findIndex', 'flatMap', 'forEach', 'has', 'isEmpty', 'join', 'length', 'map', 'pop', 'push', 'reduce', 'shift', 'slice', 'some', 'splice', 'take', 'unshift'], true);
        if(!allowFns.has(name)) {
            throw new CompileError('@%s is not a valid magic method', range, name);
        }
        this.name = name;
    }
}

// #########= MethodElement

/**
 * method definition
 * 
 * 方法定义
 * 各个方法均放入所在类的定义区(methodDefinitions)内
 * 方法不管是否静态均使用该类, 构造函数需要使用子类ConstructorElement
 */
public class MethodElement extends FunctionElement {
    /**
     * true if super() is met
     */
    private var smet:Boolean = false;

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(FunctionGroupElement, 1, false),
            // for method, use MethodParameterGroupElement
            new ElementPattern(MethodParameterGroupElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * true if this can be refered here
     */
    override public function get allowThis():Boolean {
        var tag = this.tag;
        return this.parent.allowThis && !tag.isStatic;
    }

    /**
     * true if super can be refered here
     */
    override public function get allowSuper():Boolean {
        var tag = this.tag;
        return this.parent.allowSuper && !tag.isStatic;
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        var tag = this.tag;
        return this.isConstructor && this.parent.allowSuperCall;
    }

    /**
     * true if this is a constructor
     */
    public function get isConstructor():Boolean {
        var tag = this.tag;
        return !tag.isStatic && tag.name === this.theClass.tag.name;
    }

    /**
     * declare this variable
     * (pre-stage1)
     */
    override public function declareVariable():void {
        var tag = this.tag;
        // 检查构造器类型
        if(this.isConstructor) {
            if(!tag.isPublic) {
                throw new CompileError('Class constructor may not be a private method');
            }
            if(tag.isAccessor) {
                throw new CompileError('Class constructor may not be an accessor');
            }
        } else {
            // 将当前方法注册到类 (构造器不用注册)
            this.parentFunction.registerFunctionDefinition(this.tag, this.tag.range);
        }
        super.declareVariable();
    }

    /**
     * called when super() is met
     */
    public function meetSuper(range:Range):void {
        if(!this.allowSuperCall) {
            return;
        }
        if(this.smet) {
            throw new CompileError('Super constructor may only be called once', range);
        }
        this.smet = true;
    }

    /**
     * called when return() is met
     */
    public function meetReturnOrThis(range:Range):void {
        if(!this.allowSuperCall) {
            return;
        }
        // 在super()之前抛异常应该是可以的, 尽管ActionScript不允许
        // JAVA在不久前的JEP 447中允许了这一点
        if(!this.smet) {
            throw new CompileError('Super statement cannot occur after a this, super or return statement', range);
        }
    }

    /**
     * walk stage 1
     */
    override public function checkVariables():void {
        super.checkVariables();
        // 如果是构造器检查是否有super
        if(!this.smet && this.allowSuperCall) {
            throw new CompileError('Must call super constructor in derived class before returning from derived constructor', this.range);
        }
    }

    /**
     * find the variable by name
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     */
    override public function referVar(name:String, range:Range = null):Variable {
        // check if exists
        var v = this.getLocal(name);
        if(v !== null) {
            return v;
        }
        // reject function tag
        if(this.tag.name !== null && this.tag.name === name) {
            // for constructor, bubble to the class
            if(!this.isConstructor) {
                throw new CompileError('\'this\' is required for referring the method itself', range);
            }
        }
        return this.parentFunction.referVar(name, range);
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        // for constructor without super class, insert super (__csu) call
        // now it is safe to do that since the allow-super-call check is finished
        if(this.isConstructor && !this.allowSuperCall) {
            var expr = new ExpressionStatementElement(null);
            this.body.prepend(expr);
            var ce = new CallElement(null);
            expr.append(ce);
            ce.append(new SuperElement(null));
            ce.append(new ArgumentElement(null));
        }
        super.functionalize();
    }

    /**
     * the constructor
     * @param {String} name
     * @param {Boolean} isStatic
     * @param {Boolean} isPublic
     * @param {Range} tagRange
     * @param {Range} range
     */
    public function MethodElement(name:String, methodType:String, isStatic:Boolean, isPublic:Boolean, tagRange:Range, range:Range) {
        super(range);
        var tag = new MethodTag(name, methodType, isStatic, isPublic, this, tagRange);
        this.tag = tag;
        this.append(new FunctionGroupElement());
        // 静态方法也是有this指针的, 只不过这个指针指向的是静态类体且对用户代码不可访问
        this.append(new MethodParameterGroupElement(tag));
        this.append(new BodyElement(null));
    }
}

// #########= MethodGroupElement

/**
 * method definitions
 *
 * 方法的定义, 和FunctionGroupElement相比, 该元素中只能是MethodElement
 */
public class MethodGroupElement extends FunctionGroupElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'methods';
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        // forward to the class
        return this.parent.allowSuperCall;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(MethodElement, 0, true)
        ]);
    }

    /**
     * the constructor
     */
    public function MethodGroupElement() {
        super();
    }
}

// #########= ParameterGroupElement

/**
 * class of the parameters
 *
 * 存放参数的类, 每个函数只会有一个
 * 其内元素可以是ParameterElement, ParameterAssignElement(可选参数)和RestParameterElement(剩余参数)
 */
public class ParameterGroupElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'params';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        // 在将AST转IR时应确保必要参数在前, 可选参数在后, 不然报InternalError
        return new ArrayList([
            new ElementPattern(ParameterElement, 0, true),
            new ElementPattern(ParameterAssignElement, 0, true),
            new ElementPattern(RestParameterElement, 0, true)
        ]);
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        // for function signature, call toPrameterList
        // 对于函数签名里的参数列表, 调用toPrameterList输出

        // generatePython用于输出重命名的参数
        // 如果参数被内层函数所修改, 就要变成闭包的变量
        // 此时应将其赋给对应的闭包变量(参数重命名)
        this.checkStruct();
        this.forEachChild(function(e, k, s) {
            e.generateRenameAssignment(ctx);
        });
    }

    /**
     * generate python code for the parameter list
     *
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    public function toPrameterList(writer, contchr, parentType = 0) {
        var o = false;
        this.forEachChild(function(e, k, s) {
            if(o) {
                writer.write(', ', '');
            }
            e.writePython(writer, '');
            o = true;
        });
    }

    /**
     * the constructor
     */
    public function ParameterGroupElement() {
        super(null);
    }
}

// #########= MethodParameterGroupElement

/**
 * class of the parameters of method (this as the first parameter)
 */
public class MethodParameterGroupElement extends ParameterGroupElement {
    private var tag:MethodTag;

    /**
     * declare this variable
     * (pre-stage1)
     */
    override public function declareVariable():void {
        var tag = this.tag;
        // check parameter count if necessary
        var pcnt = 0;
        this.forEachChild(function(p, k, s) {
            pcnt++;
        });
        if(tag.isSetter && pcnt !== 1) {
            throw new CompileError('Setter must have exactly one formal parameter', this.range);
        }
        if(tag.isAccessor && !tag.isSetter && pcnt !== 0) {
            throw new CompileError('Getter must not have any formal parameters', this.range);
        }
        super.declareVariable();
    }

    /**
     * generate python code for the parameter list
     *
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function toPrameterList(writer, contchr, parentType = 0) {
        writer.write('this', '');
        this.forEachChild(function(e, k, s) {
            writer.write(', ', '');
            e.writePython(writer, '');
        });
    }

    /**
     * the constructor
     */
    public function MethodParameterGroupElement(tag:MethodTag) {
        super();
        this.tag = tag;
    }
}

// #########= NotOperatorElement

/**
 * class of the not operator
 * internal use only
 */
public class NotOperatorElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'not';
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return this.firstChild.constantOnly;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        return this.firstChild.tempVarOnly;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 1, false)]);
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var p = parentType >= 2;
        var dst = this.firstChild;
        if(p) {
            writer.write('(', false);
        }
        writer.write('not ', p ? '' : contchr);
        dst.writePython(writer, p ? '' : contchr, 4);
        if(p) {
            writer.write(')', contchr);
        }
    }

    /**
     * the constructor
     */
    public function NotOperatorElement(range:Range) {
        super(range);
    }
}

// #########= NullLiteralElement

/**
 * class of the null literal expressions (null)
 */
public class NullLiteralElement extends FundamentalLiteralElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'null';
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        writer.write('None', contchr);
    }

    /**
    * the constructor
    */
    public function NullLiteralElement(range:Range) {
        super(range);
    }
}

// #########= NullishCheckElement

/**
 * class of the nullish-check operators
 * internal use only
 */
public class NullishCheckElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'isnullish';
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return this.firstChild.constantOnly;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        return this.firstChild.tempVarOnly;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 1, false)]);
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var p = parentType >= 3;
        var dst = this.firstChild;
        if(p) {
            writer.write('(', false);
        }
        writer.write('None is ', p ? '' : contchr);
        dst.writePython(writer, p ? '' : contchr, 4);
        if(p) {
            writer.write(')', contchr);
        }
    }

    /**
     * the constructor
     */
    public function NullishCheckElement(range:Range) {
        super(range);
    }
}

// #########= NumberLiteralElement

/**
 * class of the number (real/int) literal expressions
 */
public class NumberLiteralElement extends FundamentalLiteralElement {
    /**
    * the value of this
    */
    private var value:Number;

    /**
    * the source of this
    */
    private var source:String;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'real';
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        // 直接输出即可
        // 隐含八进制(以0开头的)会被解析器拒绝
        if(parentType >= 12) {
            writer.write('(', false);
        }
        writer.write(this.source, false);
        if(parentType >= 12) {
            writer.write(')', false);
        }
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('source', this.source);
        super.dump(ctx);
    }

    /**
    * the constructor
    */
    public function NumberLiteralElement(value:Number, source:String, range:Range) {
        super(range);
        this.value = value;
        this.source = source;
    }
}

// #########= ObjectLiteralElement

/**
 * Object literal expression
 */
public class ObjectLiteralElement extends ExpressionElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'object';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(KeyValueElement, 0, true)]);
    }

    /**
     * walk stage 2
     *
     * 简化表达式, 提升复杂表达式, 使之能被py表示
     */
    override public function simplifyExpressions():void {
        this.checkStruct();

        var lc = -1;
        this.forEachChild(function(m, k, s) {
            if(m.complex) {
                lc = k;
            }
        });
        // 但凡有一个是复杂的, 其之前的所有成员都要析出, 以保证执行顺序
        this.forEachChild(function(m, k, s) {
            if(k > lc) {
                return false;
            }
            m.checkStruct();
            // 键, 值都要析出
            var key = m.firstChild;
            var value = m.lastChild;
            var ate = key.replaceWithTemp();
            this.insertTempAssign(ate);
            var tas = value.replaceWithTemp();
            this.insertTempAssign(tas);
        });

        this.checkStruct();
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        writer.write('({', '');
        this.forEachChild(function(m, k, s) {
            if(k > 0) {
                writer.write(', ', '');
            }
            m.writePython(writer, false);
        });
        writer.write('})', contchr);
    }

    /**
     * the constructor
     */
    public function ObjectLiteralElement(range:Range) {
        super(range);
    }
}

// #########= ParameterAssignElement

/**
 * class of the parameter with the default value
 */
public class ParameterAssignElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'optparam';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        // 在将AST转IR时应确保必要参数在前, 可选参数在后, 不然报InternalError
        return new ArrayList([
            new ElementPattern(ParameterElement, 1, false),
            new ElementPattern(ExpressionElement, 1, false),
        ]);
    }

    /**
    * scan the variables in this expression
    * (stage 1)
    */
    override public function checkVariables():void {
        var p = this.firstChild;
        var v = this.lastChild;
        p.checkVariables();
        v.checkVariables();
        if(v.complex || !v.constantOnly) {
            throw new CompileError('Default parameter must be constant', v.range);
        }
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        // write the original name
        var p = this.firstChild;
        var v = this.lastChild;
        p.writePython(writer, false);
        writer.write(' = ', '');
        writer.write('(', false);
        v.writePython(writer, '');
        writer.write(')', false);
    }

    /**
     * generate the rename assignment, used if the parameter is closured
     */
    public function generateRenameAssignment(ctx:PyGenerator):void {
        var p = this.firstChild;
        p.generateRenameAssignment(ctx);
    }

    /**
     * the constructor
     */
    public function ParameterAssignElement(range:Range) {
        super(range);
    }
}

// #########= ParameterElement

/**
 * class of the variable in the parameter, used for function or catch
 */
public class ParameterElement extends Element {
    /**
     * name of the variable
     */
    private var source:String;

    /**
     * the Variable
     */
    private var target:LocalVar = null;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'param';
    }

    /**
     * declare this variable
     * (pre-stage1)
     */
    override public function declareVariable():void {
        this.target = this.theFunction.registerLocalVar(this.source, this.range);
    }

    /**
    * scan the variables in this expression
    * (stage 1)
    */
    override public function checkVariables():void {
        this.target.write(this.theFunction, this.range);
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        // nothing to do
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        // write the original name
        writer.write(this.target.toOriginPython(), false);
    }

    /**
     * generate the rename assignment, used if the parameter is closured
     */
    public function generateRenameAssignment(ctx:PyGenerator):void {
        if(!this.target.closure) {
            return;
        }
        var writer = new LineWriter();
        writer.write(this.target.toPython(), false);
        writer.write(' = ', false);
        writer.write(this.target.toOriginPython(), false);
        writer.finalize(ctx);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('name', this.source);
        ctx.attr('var', this.target);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function ParameterElement(source:String, range:Range) {
        super(range);
        this.source = source;
    }
}

// #########= RestParameterElement

/**
 * class of the rest parameter
 * (for right value, refer to SpreadElement)
 */
public class RestParameterElement extends Element {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'rest';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ParameterElement, 1, false)
        ]);
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var p = this.firstChild;
        writer.write('*', false);
        p.writePython(writer, false);
    }

    /**
     * generate the rename assignment, used if the parameter is closured
     */
    public function generateRenameAssignment(ctx:PyGenerator):void {
        this.checkStruct();
        var p = this.firstChild;
        p.generateRenameAssignment(ctx);
    }

    /**
     * the constructor
     */
    public function RestParameterElement(range:Range) {
        super(range);
    }
}

// #########= ReturnElement

/**
 * return statement
 */
public class ReturnElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'return';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, true)
        ]);
    }

    /**
     * walk stage 1
     */
    override public function checkVariables():void {
        // if this statement is in a constructor, notify it
        var fn = this.theFunction;
        if(fn instanceof MethodElement) {
            fn.meetReturnOrThis(this.range);
        }
        super.checkVariables();
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        var right = this.lastChild;
        if(right === null) {
            ctx.writeln('return');
            return;
        }
        var writer = new LineWriter();
        writer.write('return ', false);
        right.writePython(writer, '\\');
        writer.finalize(ctx);
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function ReturnElement(range:Range) {
        super(range);
    }
}

// #########= SpreadElement

/**
 * spread literal
 */
public class SpreadElement extends ExpressionElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'spread';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 1, false)]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof SequenceElement)) {
            throw new InternalError('malformed structure in spread (not in sequence)');
        }
        super.checkStruct();
    }

    /**
     * walk stage 2
     *
     * 简化表达式, 提升复杂表达式, 使之能被py表示
     */
    override public function simplifyExpressions():void {
        // 不可能调用该函数
        // 父元素会把简化的工作完成
        throw new InternalError('called simplifyExpressions of SpreadElement');
    }

    /**
     * extract this
     * (stage 2)
     */
    override public function replaceWithTemp(optional = true):AssignTempElement {
        throw new InternalError('called replaceWithTemp of SpreadElement');
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var value = this.lastChild;
        writer.write('*', '');
        value.writePython(writer, false, 11);
    }

    /**
     * the constructor
     */
    public function SpreadElement(range:Range) {
        super(range);
    }
}

// #########= StaticGroupElement

/**
 * static properties initializer group
 */
public class StaticGroupElement extends BaseFunctionElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'staticinit';
    }

    /**
     * true if this can be refered here
     */
    override public function get allowThis():Boolean {
        return false;
    }

    /**
     * true if super can be refered here
     */
    override public function get allowSuper():Boolean {
        return false;
    }

    /**
     * true if super() can be used here
     */
    override public function get allowSuperCall():Boolean {
        return false;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(FunctionGroupElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof ClassElement)) {
            throw new InternalError('malformed structure in StaticGroupElement (not in ClassElement)');
        }
        super.checkStruct();
    }

    /**
     * the function defined in this function
     */
    override public function get functionDefinitions():FunctionGroupElement {
        this.checkStruct();
        var e = this.firstChild;
        return e;
    }

    /**
     * the body
     */
    override public function get body():BodyElement {
        this.checkStruct();
        var e = this.lastChild;
        return e;
    }

    /**
     * register local function definition
     * @param {FunctionTag} tag, the tag of function
     * @param {Range} range
     */
    override public function registerFunctionDefinition(tag:FunctionTag, range:Range = null):void {
        throw new InternalError('register function definition in class property initializer');
    }

    /**
     * register local variable and return it
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     */
    override public function registerLocalVar(name:String, range:Range = null):LocalVar {
        throw new InternalError('register local variable in class property initializer');
        return null;
    }

    /**
     * find the variable by name
     * @param {String} name, the identifier of the variable
     * @param {Range} range
     */
    override public function referVar(name:String, range:Range = null):Variable {
        // reject class name
        if(this.theClass.tag.name === name) {
            throw new CompileError('cannot access the class name %s in the static property initializer', range, name);
        }
        return this.theClass.referVar(name, range);
    }

    /**
     * generate python code of the class factory
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(gen:PyGenerator):void {
        gen.blank();
        var sline = new LineNumber();
        gen.logLineNumber(sline);

        // private fields(__csp) is a local var in class factory
        gen.writeln('def __csi(this):');

        gen.tab();

        this.functionDefinitions.generatePython(gen);

        gen.blank();

        gen.comment('super');
        gen.writeln('__x_objT.__init__(this)');

        gen.comment('initialize properties');
        this.body.generatePython(gen);

        gen.TAB();

        gen.comment(
            'end static initializer __csi (line %l)',
            sline
        );
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function StaticGroupElement() {
        super(null);
        this.append(new FunctionGroupElement());
        this.append(new BodyElement(null));
    }
}

// #########= StaticInitializerElement

/**
 * declaration of static property
 */
public class StaticInitializerElement extends StatementElement {
    /**
     * an Attribute, the property name
     */
    private var attribute:Attribute;

    /**
     * true if this is a public propeerty
     */
    private var isPublic:Boolean;

    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'staticprop';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, true)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.theFunction instanceof StaticGroupElement)) {
            throw new InternalError('malformed structure in StaticInitializerElement (not in StaticGroupElement)');
        }
        super.checkStruct();
    }

    /**
     * true if this is a initializer
     */
    public function get isInitializer():Boolean {
        this.checkStruct();
        return this.firstChild !== null;
    }

    /**
     * declare this variable
     * (pre-stage1)
     */
    override public function declareVariable():void {
        this.checkStruct();
        this.theClass.registerProperty(this.attribute.name, this.isPublic, true, this.attribute.range);
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        super.simplifyExpressions();
        if(!this.isInitializer) {
            this.remove();
        }
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        var writer = new LineWriter();
        var right = this.lastChild;
        writer.write(this.isPublic ? 'this' : '__csp', false);
        writer.write('.', false);
        writer.write(this.attribute.toPython(), false);
        writer.write(' = ', '\\');
        right.writePython(writer, false);
        writer.finalize(ctx);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('attribute', this.attribute);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function StaticInitializerElement(attribute:Attribute, isPublic:Boolean, range:Range) {
        super(range);
        this.isPublic = isPublic;
        this.attribute = attribute;
    }
}

// #########= StringLiteralElement

/**
 * class of the string literal expressions
 */
public class StringLiteralElement extends FundamentalLiteralElement {
    /**
    * the value of this
    */
    private var value:String;

    /**
    * the source of this
    */
    private var source:String;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'string';
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var v = new ArrayList(this.value);
        var l = v.length;
        var cl = 0;
        var cs = '';
        writer.write('(u"');
        v.forEach(function(c, k, a) {
            // 如果字符数少于80, 就不断行
            // 不然每60-100个字符断行, 意思是如果在这个长度范围内, 遇上换行符就换行
            // 不然就每100个字符断行
            var cp = StrTool.codePointAt(c);
            var br = false;
            if(cp === 10) {
                cs += '\\n';
                cl += 2;
                if(l > 80 && cl >= 50) {
                    br = true;
                }
            } else if(cp === 9) {
                // 转义知名的符号
                cs += '\\t';
                cl += 2;
            } else if(cp === 7) {
                cs += '\\a';
                cl += 2;
            } else if(cp === 8) {
                cs += '\\b';
                cl += 2;
            } else if(cp === 13) {
                cs += '\\r';
                cl += 2;
            } else if(c === '"') {
                // 转义引号
                cs += '\\"';
                cl += 2;
            } else if(c === '\\') {
                // 转义反斜杠
                cs += '\\\\';
                cl += 2;
            } else if(cp <= 126 && cp >= 32) {
                // 可显示的ASCII直接写出
                cs += c;
                cl += 1;
            } else if(cp < 0x10000) {
                cs += StrTool.toCodePointString(cp);
                cl += 6;
            } else {
                cs += StrTool.toCodePointString(cp);
                cl += 10;
            }
            if(br || cl >= 100) {
                writer.write(cs + '\\', true);
                cl = 0;
                cs = '';
            }
            br = false;
        });
        if(cl > 0) {
            writer.write(cs, false);
        }
        writer.write('")', contchr);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('source', this.value);
        super.dump(ctx);
    }

    /**
    * the constructor
    */
    public function StringLiteralElement(value:String, source:String, range:Range) {
        super(range);
        this.value = value;
        this.source = source;
    }
}

// #########= SuperElement

/**
 * class of super pointer
 *
 * for super(), refer to CallSuperElement
 */
public class SuperElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'super';
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return false;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        return false;
    }

    /**
     * scan the variables in this expression
     * (stage 1)
     */
    override public function checkVariables():void {
        this.checkStruct();
        if(!this.allowSuper) {
            throw new CompileError("'super' keyword unexpected here", this.range);
        }
        // if this statement is in a constructor, notify it
        var fn = this.theFunction;
        if(fn instanceof MethodElement) {
            fn.meetReturnOrThis(this.range);
        }
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        // true if super()
        if(this.parent instanceof CallElement) {
            // super() should generated by CallElement
            throw new InternalError('cannot generate the code for super()');
        }
        writer.write('(super(__clsT, this))', contchr);
    }

    /**
    * the constructor
    */
    public function SuperElement(range:Range) {
        super(range);
    }
}

// #########= TernaryOperatorElement

/**
 * class of the ternary (?:) operators
 */
public class TernaryOperatorElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'ternary';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 3, false)]);
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        this.checkStruct();
        super.functionalize();
        var cond = this.firstChild;
        var cc = CallElement.callGlobal(this.theGlobal.enableImplicitBooleanConversion ? '__x_tob' : '__x_cb', cond);
        this.prepend(cc);
        this.checkStruct();
    }

    /**
    * walk stage 2
    *
    * 简化表达式, 提升复杂表达式, 使之能被py表示
    */
    override public function simplifyExpressions():void {
        this.checkStruct();
        if(!this.complex) {
            return;
        }
        var cond = this.firstChild;
        var exec = cond.nextSibling;
        var altn = exec.nextSibling;

        // 如果只是条件是复杂的, 那么只需要简化条件, 其他的部分仍然保留原样
        if(!(exec.complex || altn.complex)) {
            cond.simplifyExpressions();
            return;
        }

        // 如果两个条件执行表达式有一个是复杂的, 那就要改写成if语句
        // input: a(b ? c : d)
        // output:
        // if(__x_cb(b)) {
        //   __temp = c;
        // } else {
        //   __temp = d;
        // }
        // a(__temp)
        var atva = this.theFunction.allocTempVar();

        var ife = new IfBlockElement(null);
        this.theStatement.before(ife);

        var iife = new IfElement(null);
        ife.append(iife);
        var acond = new ConditionElement(null);
        iife.append(acond);
        acond.append(cond);
        var atrue = new BodyElement(null);
        iife.append(atrue);
        var atvl = new AssignTempElement(atva);
        atrue.append(atvl);
        atvl.append(exec);

        var afalse = new ElseElement(null);
        ife.append(afalse);
        var atvr = new AssignTempElement(atva);
        afalse.append(atvr);
        atvr.append(altn);

        this.replaceWith(atvl.getLeftElement());
        ife.simplifyExpressions();
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var cond = this.firstChild;
        var exec = cond.nextSibling;
        var altn = exec.nextSibling;
        // 如果子表达式是自身也加上括号
        var p = parentType >= 1;
        if(p) {
            writer.write('(', false);
        }
        exec.writePython(writer, p ? '' : contchr, 2);
        writer.write(' if ', p ? '' : contchr);
        cond.writePython(writer, p ? '' : contchr, 2);
        writer.write(' else ', p ? '' : contchr);
        altn.writePython(writer, p ? '' : contchr, 2);
        if(p) {
            writer.write(')', contchr);
        }
    }

    /**
     * the constructor
     */
    public function TernaryOperatorElement(range:Range) {
        super(range);
    }
}

// #########= ThisElement

/**
 * class of this pointer
 */
public class ThisElement extends ExpressionElement {
    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'this';
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return true;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        return true;
    }

    /**
     * scan the variables in this expression
     * (stage 1)
     */
    override public function checkVariables():void {
        this.checkStruct();
        if(!this.allowThis) {
            throw new CompileError("'this' expression must be used inside class instance methods", this.range);
        }
        // if this statement is in a constructor, notify it
        var fn = this.theFunction;
        if(fn instanceof MethodElement) {
            fn.meetReturnOrThis(this.range);
        }
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        writer.write('this', contchr);
    }

    /**
    * the constructor
    */
    public function ThisElement(range:Range) {
        super(range);
    }
}

// #########= ThrowElement

/**
 * throw statement
 */
public class ThrowElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'throw';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ExpressionElement, 1, false)
        ]);
    }

    /**
     * generate python code
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        var right = this.lastChild;
        var writer = new LineWriter();
        writer.write('raise ', false);
        right.writePython(writer, '\\');
        writer.finalize(ctx);
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function ThrowElement(range:Range) {
        super(range);
    }
}

// #########= TryBlockElement

/**
 * try..catch..finally package
 */
public class TryBlockElement extends BlockElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'trygroup'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(TryElement, 1, false),
            new ElementPattern(CatchElement, 1, true),
            new ElementPattern(FinallyElement, 1, true)
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        super.checkStruct();
        if(this.firstChild === this.lastChild) {
            throw new InternalError('malformed structure in TryBlockElement (missing catch or finally)');
        }
    }

    /**
     * put the python code of the contained expression into writer
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(gen:PyGenerator):void {
        this.checkStruct();
        var sline = new LineNumber();
        gen.logLineNumber(sline);
        super.generatePython(gen);
        gen.comment('end try (line %l)', sline);
    }

    /**
     * the constructor
     */
    public function TryBlockElement(range:Range) {
        super(range);
    }
}

// #########= TryElement

/**
 * try statement
 *
 * 单个try的语句
 * 不要直接使用这个, 需要放入一个TryBlockElement中
 */
public class TryElement extends BodyElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'try'
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        if(!(this.parent instanceof TryBlockElement)) {
            throw new InternalError('malformed structure in TryElement (not in TryBlockElement)');
        }
        super.checkStruct();
    }

    /**
     * put the python code of the contained expression into writer
     *
     * @param {PyGenerator} gen
     */
    override public function generatePython(ctx:PyGenerator):void {
        ctx.writeln('try:');
        ctx.tab();
        super.generatePython(ctx);
        ctx.TAB();
    }

    /**
     * the constructor
     */
    public function TryElement(range:Range) {
        super(range);
    }
}

// #########= TupleElement

/**
 * tuple literal
 */
public class TupleElement extends SequenceElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'tuple';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        return this.hasSpread || super.complex;
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        if(!this.complex) {
            return;
        }
        var tv = this.makeList();
        // convert list to tuple
        var cc = CallElement.callGlobal('__x_tup', VarElement.getTempVar(tv));
        this.replaceWith(cc);
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        if(this.hasSpread) {
            throw new InternalError('cannot generate python for tuple with spread syntax');
        }
        writer.write('__x_tupof(', false);
        super.writePython(writer, '');
        // trailing comma is required for tuple with single member
        if(this.firstChild !== null && this.firstChild === this.lastChild) {
            writer.write(',', false);
        }
        writer.write(')', contchr);
    }

    /**
     * the constructor
     */
    public function TupleElement(range:Range) {
        super(range);
    }
}

// #########= UniaryOperatorElement

/**
 * class of the uniary operators
 */
public class UniaryOperatorElement extends ExpressionElement {
    /**
     * raw (operator) in js, a string
     */
    private var source:String;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'uniary';
    }

    /**
     * check if if this is a compile-time constant, 
     * or other expressions without any side-effect, such as literals
     */
    override public function get constantOnly():Boolean {
        return this.firstChild.constantOnly;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        // may throw exception
        return false;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(ExpressionElement, 1, false)]);
    }

    /**
     * pre-stage 2
     */
    override public function functionalize():void {
        this.checkStruct();
        super.functionalize();
        var op = this.source;
        // !和typeof要转换为函数
        var n = op === 'typeof';
        var m = op === '!';
        if(!(n || m)) {
            return;
        }
        var exp = this.firstChild;
        var cc = CallElement.callGlobal(n ? '__x_typ' : (this.theGlobal.enableImplicitBooleanConversion ? '__x_tnb' : '__x_not'), exp);
        this.replaceWith(cc);
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        var op = this.source;
        var dst = this.firstChild;
        if(op === '+' || op === '-' || op === '~') {
            var p = parentType > 10;
            if(p) {
                writer.write('(', false);
            }
            writer.write(op, false);
            dst.writePython(writer, p ? '' : contchr, 10);
            if(p) {
                writer.write(')', contchr);
            }
        } else if(op === '?') {
            p = parentType >= 3;
            if(p) {
                writer.write('(', false);
            }
            // is和比较同级
            writer.write('None is not ', p ? '' : contchr);
            dst.writePython(writer, p ? '' : contchr, 4);
            if(p) {
                writer.write(')', contchr);
            }
        } else {
            throw new InternalError('Cannot writePython for uniary ' + op);
        }
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('operator', this.source);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function UniaryOperatorElement(source:String, range:Range) {
        super(range);
        if(source === 'delete') {
            throw new CompileError('delete can only be a standalone statement', range);
        }
        this.source = source;
    }
}

// #########= UpdateElement

/**
 * class of the update operators (++/--)
 */
public class UpdateElement extends ExpressionElement {
    /**
     * true for ++, false for --
     */
    private var plus:Boolean;

    /**
     * true if pre (--a), false if post (a--)
     */
    private var prefix:Boolean;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'update';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        return true;
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([new ElementPattern(LvalueElement, 1, false)]);
    }

    /**
    * scan the variables in this expression
    * (stage 1)
    */
    override public function checkVariables():void {
        this.checkStruct();
        var target = this.firstChild;
        target.checkVariables();
        target.checkWrite();
    }

    /**
    * walk stage 2
    *
    * 简化表达式, 提升复杂表达式, 使之能被py表示
    */
    override public function simplifyExpressions():void {
        this.checkStruct();
        var op = this.plus;
        var pre = this.prefix;
        var target = this.firstChild;
        var rv = target.extractLeftAndDuplicate();

        var ate = new AssignTempElement(this.theFunction.allocTempVar());
        this.theStatement.before(ate);

        // 前/后缀决定了增(减)的时机
        // 如果是前缀操作, 则临时变量就是增/减后的
        append(ate, rv, pre, op);
        ate.checkStruct();

        var asn = new AssignElement(null);
        ate.after(asn);
        // 如果是后缀操作, 则在赋值回原变量时才进行增/减
        asn.append(target);
        append(asn, ate.getLeftElement(), !pre, op);
        asn.checkStruct();

        // 最后将自身替换为临时变量
        this.replaceWith(ate.getLeftElement());

        function append(ase, val, act, op) {
            var fn = op ? '__x_inc' : '__x_dec';
            // inc, dec会对类型进行检查, 只允许整数或浮点数
            ase.append(act ? CallElement.callGlobal(fn, val) : val);
        }
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('prefix', this.prefix);
        ctx.attr('operator', this.plus ? '++' : '--');
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function UpdateElement(source:String, prefix:Boolean, range:Range) {
        super(range);
        if(source === '++') {
            this.plus = true;
        }
        else if(source === '--') {
            this.plus = false;
        }
        else {
            throw new InternalError('invalid update operator');
        }
        this.prefix = prefix;
    }
}

// #########= VarDeclaratorElement

/**
 * var without initializer
 */
public class VarDeclaratorElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'vardecl';
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(VarElement, 1, false), // left value
        ]);
    }

    /**
     * check the struture of this
     */
    override public function checkStruct():void {
        super.checkStruct();
        var v = this.firstChild;
        if(!v.declarator) {
            throw new InternalError('malformed structure in VarDeclaratorElement (mismatched declarator)');
        }
    }

    /**
     * declare this variable
     * (pre-stage1)
     */
    override public function declareVariable():void {
        this.checkStruct();
        super.declareVariable();
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        // now, this is useless
        this.remove();
    }

    /**
    * the constructor
    * @param {Range} range, the range of the expresion
    */
    public function VarDeclaratorElement(range:Range) {
        super(range);
    }
}

// #########= VarElement

/**
 * class of the variable
 */
public class VarElement extends LvalueElement {
    private var _declarator:Boolean;

    /**
     * name of the variable
     */
    private var source:String;

    /**
     * the Variable
     *
     * 该表达式引用的变量, 在checkWrite, checkVariables时会根据this.source查找到实际的变量
     */
    private var target:Variable = null;

    /**
    * the name of this element
    */
    override public function get typeName():String {
        return 'var';
    }

    /** 
     * check if this is a complex expression
     */
    override public function get complex():Boolean {
        return false;
    }

    /**
     * true if this is a declarator
     *
     * 如果是一个变量声明(比如var), 返回true, 大多左值都是无法声明的
     */
    override public function get declarator():Boolean {
        return this._declarator;
    }

    /**
    * check if if this is only a temp variable, 
    * or other expressions without any side-effect, such as literals
    */
    override public function get tempVarOnly():Boolean {
        // 临时变量, this或者单纯的函数名都不会产生副作用
        return this.target instanceof TempVar || this.target instanceof FunctionTag;
    }

    /**
     * declare this variable
     * (pre-stage1)
     *
     * 如果需要就声明变量. 
     */
    override public function declareVariable():void {
        if(!this.declarator) {
            return;
        }
        this.target = this.theFunction.registerLocalVar(this.source, this.range);
    }

    /**
    * scan the variables in this expression
    * (stage 1)
    */
    override public function checkVariables():void {
        var v = this.target;
        if(v === null) {
            v = this.theFunction.referVar(this.source, this.range);
            this.target = v;
        }
        v.read(this.theFunction, this.range);
    }

    /**
     * check write variable
     */
    override public function checkWrite():void {
        var v = this.target;
        if(v === null) {
            v = this.theFunction.referVar(this.source, this.range);
            this.target = v;
        }
        v.write(this.theFunction, this.range);
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        // nothing to do
    }

    /**
     * extrace the left's object and index
     * (stage 2)
     */
    override public function extractLeft():void {
        // nothing to do
    }

    /**
     * extrace the left's object and index and return the duplication of this
     * (stage 2)
     */
    override public function extractLeftAndDuplicate():LvalueElement {
        if(this.declarator) {
            throw new InternalError('declarator used in compound assignment');
        }
        var v = new VarElement(this.source, false, this.range);
        v.target = this.target;
        return v;
    }

    /**
     * to python string
     * @param {LineWriter} writer
     * @param {String} contchr
     * @param {Number} parentType
     */
    override public function writePython(writer:LineWriter, contchr:*, parentType:Number = 0):void {
        writer.write(this.target.toPython(), contchr);
    }

    /**
     * dump to XML code
     */
    override public function dump(ctx:XMLDumper):void {
        ctx.attr('name', this.source);
        ctx.attr('variable', this.target);
        super.dump(ctx);
    }

    /**
     * the constructor
     */
    public function VarElement(source:String, declarator:Boolean, range:Range) {
        super(range);
        this.source = source;
        this._declarator = declarator;
    }

    /**
     * get a global variable
     */
    public static function getGlobalVar(name:String):VarElement {
        var tvs = new VarElement(name, false, null);
        tvs.target = new GlobalVar(name);
        return tvs;
    }

    /**
     * get a global variable
     */
    public static function getTempVar(tv:TempVar):VarElement {
        var tvs = new VarElement('__r', false, null);
        tvs.target = tv;
        return tvs;
    }

    /**
     * get a function expression tag
     */
    public static function getFunctionExp(tag:FunctionExpTag):VarElement {
        var tvs = new VarElement('__e', false, null);
        tvs.target = tag;
        return tvs;
    }
}

// #########= WhileElement

/**
 * while statement
 */
public class WhileElement extends StatementElement {
    /**
     * the name of this element
     */
    override public function get typeName():String {
        return 'while'
    }

    /**
     * the required struture of this
     */
    override public function get structList():ArrayList {
        return new ArrayList([
            new ElementPattern(ConditionElement, 1, false),
            new ElementPattern(BodyElement, 1, false)
        ]);
    }

    /**
     * walk stage 2
     */
    override public function simplifyExpressions():void {
        this.checkStruct();
        var cond = this.firstChild;
        cond.checkStruct();
        var body = this.lastChild;
        // 如果条件是复杂的, 先变成无条件循环while(true)
        // 再在内部进行退出判断
        if(cond.complex) {
            var conde = cond.firstChild;
            conde.replaceWith(new BooleanLiteralElement(true, null));

            var ife = new IfBlockElement(null);
            body.prepend(ife);

            var iife = new IfElement(null);
            ife.append(iife);
            var acond = new ConditionElement(null);
            iife.append(acond);
            // break unless cond
            var acondn = new NotOperatorElement(null);
            acond.append(acondn);
            acondn.append(conde);

            var atrue = new BodyElement(null);
            iife.append(atrue);
            var abreak = new BreakElement(null);
            atrue.append(abreak);
        }
        // 此时iife中复杂的条件也会在这一步简化
        body.simplifyExpressions();
    }

    /**
    * put the python code of the contained expression into writer
    *
    * @param {PyGenerator} gen
    */
    override public function generatePython(gen:PyGenerator):void {
        var cond = this.firstChild.firstChild;
        var body = this.lastChild;
        var writer = new LineWriter();
        var sline = new LineNumber();
        gen.logLineNumber(sline);
        writer.write('while ', false);
        cond.writePython(writer, '\\', 1);
        writer.write(':', false);
        writer.finalize(gen);

        gen.tab();
        body.generatePython(gen);
        gen.TAB();

        gen.comment('end while (line %l)', sline);
    }

    /**
     * the constructor
     */
    public function WhileElement(range:Range) {
        super(range);
    }

}

