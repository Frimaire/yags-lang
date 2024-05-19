// modified from js library symbol-tree
// see https://github.com/jsdom/js-symbol-tree

// The original license of this library is The MIT License (MIT)
/*
  Copyright (c) 2015 Joris van der Wel

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
*/

var Error = Exception;

public class SymbolTreeNode {
    public var parent = null;
    public var previousSibling = null;
    public var nextSibling = null;

    public var firstChild = null;
    public var lastChild = null;

    /** This value is incremented anytime a children is added or removed */
    public var childrenVersion = 0;
    /** The last child object which has a cached index */
    public var childIndexCachedUpTo = null;

    /** This value represents the cached node index, as long as
     * cachedIndexVersion matches with the childrenVersion of the parent */
    public var cachedIndex = -1;
    public var cachedIndexVersion = NaN; // NaN is never equal to anything

    public function get isAttached():Boolean {
        return this.parent !== null ||
            this.previousSibling !== null ||
            this.nextSibling !== null;
    }

    public function get hasChildren():Boolean {
        return this.firstChild !== null;
    }

    public function childrenChanged():void {
        /* jshint -W016 */
        // integer wrap around
        if(this.childrenVersion !== this.childrenVersion) {
            this.childrenVersion = 0;
        } else {
            this.childrenVersion = (this.childrenVersion + 1) & 0xFFFFFFFF;
        }
        this.childIndexCachedUpTo = null;
    }

    public function getCachedIndex(parentNode):Number {
        // (assumes parentNode is actually the parent)
        if (this.cachedIndexVersion !== parentNode.childrenVersion) {
            this.cachedIndexVersion = NaN;
            // cachedIndex is no longer valid
            return -1;
        }

        return this.cachedIndex; // -1 if not cached
    }

    public function setCachedIndex(parentNode, index:Number):void {
        // (assumes parentNode is actually the parent)
        this.cachedIndexVersion = parentNode.childrenVersion;
        this.cachedIndex = index;
    }
    
    public function SymbolTreeNode() {
    }
}

class TreeIterator {
    public static var PREV = 1;
    public static var NEXT = 2;
    public static var PARENT = 3;
    public static var PRECEDING = 4;
    public static var FOLLOWING = 5;

    private var status_TREE;
    private var status_ROOT;
    private var status_NEXT;
    private var status_ITERATE_FUNC;

    public function next() {
        var tree = this.status_TREE;
        var iterateFunc = this.status_ITERATE_FUNC;
        var root = this.status_ROOT;

        if (this.status_NEXT === null) {
            return new TreeIteratorResult(
                true,
                root
            );
        }

        var value = this.status_NEXT;

        if (iterateFunc === 1) {
            this.status_NEXT = tree._node(value).previousSibling;
        }
        else if (iterateFunc === 2) {
            this.status_NEXT = tree._node(value).nextSibling;
        }
        else if (iterateFunc === 3) {
            this.status_NEXT = tree._node(value).parent;
        }
        else if (iterateFunc === 4) {
            this.status_NEXT = tree.preceding(value, {root: root});
        }
        else /* if (iterateFunc === 5)*/ {
            this.status_NEXT = tree.following(value, {root: root});
        }

        return new TreeIteratorResult(
            false,
            value
        );
    }
    
    public function TreeIterator(tree, root, firstResult, iterateFunction) {
        this.status_TREE = tree;
        this.status_ROOT = root;
        this.status_NEXT = firstResult;
        this.status_ITERATE_FUNC = iterateFunction;
    }
}


class TreeIteratorResult {
    public var done:Boolean = false;
    public var value;

    public function TreeIteratorResult(done:Boolean, value:*) {
        this.done = done;
        this.value = value;
    }
}

class TreePosition {
    // same as DOM DOCUMENT_POSITION_
    public static function get DISCONNECTED() {
        return 1;
    }

    public static function get PRECEDING() {
        return 2;
    }

    public static function get FOLLOWING() {
        return 4;
    }

    public static function get CONTAINS() {
        return 8;
    }

    public static function get CONTAINED_BY() {
        return 16;
    }

    /**
     * the constructor
     */
    public function TreePosition() {
        throw new TypeError('TreePosition is not a constructor');
    }
}


// The AS version here requires a property named _symbolTreeNode in the target instead of using the Symbol.
// These functions are ported:
// constructor
// initialize
// _node
// hasChildren
// firstChild
// lastChild
// previousSibling
// nextSibling
// parent
// childrenIterator
// previousSiblingsIterator
// nextSiblingsIterator
// ancestorsIterator
// remove
// insertBefore
// insertAfter
// prependChild
// appendChild

public class SymbolTree {

    /**
     * @constructor
     * @alias module:symbol-tree
     * @param {string} [description='SymbolTree data'] Description used for the Symbol
     */
    public function SymbolTree() {
    }

    /**
     * You can use this function to (optionally) initialize an object right after its creation,
     * to take advantage of V8's fast properties. Also useful if you would like to
     * freeze your object.
     *
     * * `O(1)`
     *
     * @method
     * @alias module:symbol-tree#initialize
     * @param {Object} object
     * @return {Object} object
     */
    public function initialize(object) {
        this._node(object);

        return object;
    }

    public function _node(object):SymbolTreeNode {
        if (object === null) {
            return null;
        }

        var node = object._symbolTreeNode;

        if (node !== null) {
            return node;
        }

        node = new SymbolTreeNode();
        object._symbolTreeNode = node;
        return node;
    }

    /**
     * Returns `true` if the object has any children. Otherwise it returns `false`.
     *
     * * `O(1)`
     *
     * @method hasChildren
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Boolean}
     */
    public function hasChildren(object):Boolean {
        return this._node(object).hasChildren;
    }

    /**
     * Returns the first child of the given object.
     *
     * * `O(1)`
     *
     * @method firstChild
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object}
     */
    public function firstChild(object) {
        return this._node(object).firstChild;
    }

    /**
     * Returns the last child of the given object.
     *
     * * `O(1)`
     *
     * @method lastChild
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object}
     */
    public function lastChild(object) {
        return this._node(object).lastChild;
    }

    /**
     * Returns the previous sibling of the given object.
     *
     * * `O(1)`
     *
     * @method previousSibling
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object}
     */
    public function previousSibling(object) {
        return this._node(object).previousSibling;
    }

    /**
     * Returns the next sibling of the given object.
     *
     * * `O(1)`
     *
     * @method nextSibling
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object}
     */
    public function nextSibling(object) {
        return this._node(object).nextSibling;
    }

    /**
     * Return the parent of the given object.
     *
     * * `O(1)`
     *
     * @method parent
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object}
     */
    public function parent(object) {
        return this._node(object).parent;
    }

    /**
     * Iterate over all children of the given object
     *
     * * `O(1)` for a single iteration
     *
     * @method childrenIterator
     * @memberOf module:symbol-tree#
     * @param {Object} parent
     * @param {Object} [options]
     * @param {Boolean} [options.reverse=false]
     * @return {Object} An iterable iterator (ES6)
     */
    public function childrenIterator(parent, reverse:Boolean = false):TreeIterator {
        var parentNode = this._node(parent);

        return new TreeIterator(
            this,
            parent,
            reverse ? parentNode.lastChild : parentNode.firstChild,
            reverse ? TreeIterator.PREV : TreeIterator.NEXT
        );
    }

    /**
     * Iterate over all the previous siblings of the given object. (in reverse tree order)
     *
     * * `O(1)` for a single iteration
     *
     * @method previousSiblingsIterator
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object} An iterable iterator (ES6)
     */
    public function previousSiblingsIterator(object):TreeIterator {
        return new TreeIterator(
            this,
            object,
            this._node(object).previousSibling,
            TreeIterator.PREV
        );
    }

    /**
     * Iterate over all the next siblings of the given object. (in tree order)
     *
     * * `O(1)` for a single iteration
     *
     * @method nextSiblingsIterator
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object} An iterable iterator (ES6)
     */
    public function nextSiblingsIterator(object):TreeIterator {
        return new TreeIterator(
            this,
            object,
            this._node(object).nextSibling,
            TreeIterator.NEXT
        );
    }

    /**
     * Iterate over all inclusive ancestors of the given object
     *
     * * `O(1)` for a single iteration
     *
     * @method ancestorsIterator
     * @memberOf module:symbol-tree#
     * @param {Object} object
     * @return {Object} An iterable iterator (ES6)
     */
    public function ancestorsIterator(object):TreeIterator {
        return new TreeIterator(
            this,
            object,
            object,
            TreeIterator.PARENT
        );
    }

    /**
     * Remove the object from this tree.
     * Has no effect if already removed.
     *
     * * `O(1)`
     *
     * @method remove
     * @memberOf module:symbol-tree#
     * @param {Object} removeObject
     * @return {Object} removeObject
     */
    public function remove(removeObject) {
        var removeNode = this._node(removeObject);
        var parentNode = this._node(removeNode.parent);
        var prevNode = this._node(removeNode.previousSibling);
        var nextNode = this._node(removeNode.nextSibling);

        if (parentNode !== null) {
            if (parentNode.firstChild === removeObject) {
                parentNode.firstChild = removeNode.nextSibling;
            }

            if (parentNode.lastChild === removeObject) {
                parentNode.lastChild = removeNode.previousSibling;
            }
        }

        if (prevNode !== null) {
            prevNode.nextSibling = removeNode.nextSibling;
        }

        if (nextNode !== null) {
            nextNode.previousSibling = removeNode.previousSibling;
        }

        removeNode.parent = null;
        removeNode.previousSibling = null;
        removeNode.nextSibling = null;
        removeNode.cachedIndex = -1;
        removeNode.cachedIndexVersion = NaN;

        if (parentNode !== null) {
            parentNode.childrenChanged();
        }

        return removeObject;
    }

    /**
     * Insert the given object before the reference object.
     * `newObject` is now the previous sibling of `referenceObject`.
     *
     * * `O(1)`
     *
     * @method insertBefore
     * @memberOf module:symbol-tree#
     * @param {Object} referenceObject
     * @param {Object} newObject
     * @throws {Error} If the newObject is already present in this SymbolTree
     * @return {Object} newObject
     */
    public function insertBefore(referenceObject, newObject) {
        var referenceNode = this._node(referenceObject);
        var prevNode = this._node(referenceNode.previousSibling);
        var newNode = this._node(newObject);
        var parentNode = this._node(referenceNode.parent);

        if (newNode.isAttached) {
            throw Error('Given object is already present in this SymbolTree, remove it first');
        }

        newNode.parent = referenceNode.parent;
        newNode.previousSibling = referenceNode.previousSibling;
        newNode.nextSibling = referenceObject;
        referenceNode.previousSibling = newObject;

        if (prevNode !== null) {
            prevNode.nextSibling = newObject;
        }

        if (parentNode !== null && parentNode.firstChild === referenceObject) {
            parentNode.firstChild = newObject;
        }

        if (parentNode !== null) {
            parentNode.childrenChanged();
        }

        return newObject;
    }

    /**
     * Insert the given object after the reference object.
     * `newObject` is now the next sibling of `referenceObject`.
     *
     * * `O(1)`
     *
     * @method insertAfter
     * @memberOf module:symbol-tree#
     * @param {Object} referenceObject
     * @param {Object} newObject
     * @throws {Error} If the newObject is already present in this SymbolTree
     * @return {Object} newObject
     */
    public function insertAfter(referenceObject, newObject) {
        var referenceNode = this._node(referenceObject);
        var nextNode = this._node(referenceNode.nextSibling);
        var newNode = this._node(newObject);
        var parentNode = this._node(referenceNode.parent);

        if (newNode.isAttached) {
            throw Error('Given object is already present in this SymbolTree, remove it first');
        }

        newNode.parent = referenceNode.parent;
        newNode.previousSibling = referenceObject;
        newNode.nextSibling = referenceNode.nextSibling;
        referenceNode.nextSibling = newObject;

        if (nextNode !== null) {
            nextNode.previousSibling = newObject;
        }

        if (parentNode !== null && parentNode.lastChild === referenceObject) {
            parentNode.lastChild = newObject;
        }

        if (parentNode !== null) {
            parentNode.childrenChanged();
        }

        return newObject;
    }

    /**
     * Insert the given object as the first child of the given reference object.
     * `newObject` is now the first child of `referenceObject`.
     *
     * * `O(1)`
     *
     * @method prependChild
     * @memberOf module:symbol-tree#
     * @param {Object} referenceObject
     * @param {Object} newObject
     * @throws {Error} If the newObject is already present in this SymbolTree
     * @return {Object} newObject
     */
    public function prependChild(referenceObject, newObject) {
        var referenceNode = this._node(referenceObject);
        var newNode = this._node(newObject);

        if (newNode.isAttached) {
            throw Error('Given object is already present in this SymbolTree, remove it first');
        }

        if (referenceNode.hasChildren) {
            this.insertBefore(referenceNode.firstChild, newObject);
        }
        else {
            newNode.parent = referenceObject;
            referenceNode.firstChild = newObject;
            referenceNode.lastChild = newObject;
            referenceNode.childrenChanged();
        }

        return newObject;
    }

    /**
     * Insert the given object as the last child of the given reference object.
     * `newObject` is now the last child of `referenceObject`.
     *
     * * `O(1)`
     *
     * @method appendChild
     * @memberOf module:symbol-tree#
     * @param {Object} referenceObject
     * @param {Object} newObject
     * @throws {Error} If the newObject is already present in this SymbolTree
     * @return {Object} newObject
     */
    public function appendChild(referenceObject, newObject) {
        var referenceNode = this._node(referenceObject);
        var newNode = this._node(newObject);

        if (newNode.isAttached) {
            throw Error('Given object is already present in this SymbolTree, remove it first');
        }

        if (referenceNode.hasChildren) {
            this.insertAfter(referenceNode.lastChild, newObject);
        }
        else {
            newNode.parent = referenceObject;
            referenceNode.firstChild = newObject;
            referenceNode.lastChild = newObject;
            referenceNode.childrenChanged();
        }

        return newObject;
    }
}

