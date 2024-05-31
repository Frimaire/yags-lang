# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division, generators

__all__ = ("SymbolTree", "SymbolTreeNode")


def __():
    from libyags0 import __x_tup, __x_tupof, __x_lst, __x_errT, __x_eq, __x_ne, __x_typ, __x_cb, __x_not, __x_iof, __x_inc, __x_dec, __x_var, __x_imf, __x_at_take, __x_at_drop, __x_at_forEach, __x_at_map, __x_at_filter, __x_at_flatMap, __x_at_some, __x_at_every, __x_at_find, __x_at_findIndex, __x_at_reduce, __x_at_join, __x_at_bind, __x_at_apply, __x_at_length, __x_at_isEmpty, __x_at_push, __x_at_pop, __x_at_shift, __x_at_unshift, __x_at_slice, __x_at_splice, __x_dcls, __x_dpif, __x_dpsf, __x_prmT, __x_csgT, __x_cpgT, __x_objT, __x_smet, __x_prop, __x_tob, __x_tnb, Infinity, NaN
    __x_imp = __x_imf(__name__)
    global SymbolTree, SymbolTreeNode

    # function definitions:

    # class definitions:

    def __c_SymbolTreeNode():
        def __g_isAttached(this):
            return __x_cb(__x_cb(__x_ne(this.parent, None)) or __x_ne(this.previousSibling, None)) or __x_ne(this\
.nextSibling, None)
        # end function __g_isAttached (line 17)

        def __g_hasChildren(this):
            return __x_ne(this.firstChild, None)
        # end function __g_hasChildren (line 22)

        def __m_childrenChanged(this):
            if __x_cb(__x_ne(this.childrenVersion, this.childrenVersion)):
                this.childrenVersion = 0
            else:
                this.childrenVersion = this.childrenVersion + 1 & 0xFFFFFFFF
            # end if (line 27)
            this.childIndexCachedUpTo = None
        # end function __m_childrenChanged (line 26)

        def __m_getCachedIndex(this, parentNode):
            if __x_cb(__x_ne(this.cachedIndexVersion, parentNode.childrenVersion)):
                this.cachedIndexVersion = NaN
                return -1
            # end if (line 36)
            return this.cachedIndex
        # end function __m_getCachedIndex (line 35)

        def __m_setCachedIndex(this, parentNode, index):
            this.cachedIndexVersion = parentNode.childrenVersion
            this.cachedIndex = index
        # end function __m_setCachedIndex (line 43)

        def __m_SymbolTreeNode(this):
            __csu(this)
        # end function __m_SymbolTreeNode (line 48)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 52)

        def __csu(this, *argv):
            # initialize properties
            this.parent = None
            this.previousSibling = None
            this.nextSibling = None
            this.firstChild = None
            this.lastChild = None
            this.childrenVersion = 0
            this.childIndexCachedUpTo = None
            this.cachedIndex = -1
            this.cachedIndexVersion = NaN
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 58)

        __clsT = __x_dcls("SymbolTreeNode", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": ("cachedIndex", 
"cachedIndexVersion", "childIndexCachedUpTo", "childrenVersion", "firstChild", "lastChild", "nextSibling", 
"parent", "previousSibling"), "childrenChanged": __m_childrenChanged, "getCachedIndex": __m_getCachedIndex, 
"hasChildren": __x_prop(__g_hasChildren, None), "isAttached": __x_prop(__g_isAttached, None), "setCachedIndex": __m_setCachedIndex, 
"__init__": __m_SymbolTreeNode})
        return __clsT
    # end class factory SymbolTreeNode, __c_SymbolTreeNode (line 16)

    def __c_TreeIterator():
        def __m_next(this):
            tree = __cpm[this, "status_TREE"]
            iterateFunc = __cpm[this, "status_ITERATE_FUNC"]
            root = __cpm[this, "status_ROOT"]
            if __x_cb(__x_eq(__cpm[this, "status_NEXT"], None)):
                return TreeIteratorResult(True, root)
            # end if (line 86)
            value = __cpm[this, "status_NEXT"]
            if __x_cb(__x_eq(iterateFunc, 1)):
                __cpm[this, "status_NEXT"] = tree._node(value).previousSibling
            elif __x_cb(__x_eq(iterateFunc, 2)):
                __cpm[this, "status_NEXT"] = tree._node(value).nextSibling
            elif __x_cb(__x_eq(iterateFunc, 3)):
                __cpm[this, "status_NEXT"] = tree._node(value).parent
            elif __x_cb(__x_eq(iterateFunc, 4)):
                __cpm[this, "status_NEXT"] = tree.preceding(value, ({(u"root"): root}))
            else:
                __cpm[this, "status_NEXT"] = tree.following(value, ({(u"root"): root}))
            # end if (line 90)
            return TreeIteratorResult(False, value)
        # end function __m_next (line 82)

        def __m_TreeIterator(this, tree, root, firstResult, iterateFunction):
            __csu(this)
            __cpm[this, "status_TREE"] = tree
            __cpm[this, "status_ROOT"] = root
            __cpm[this, "status_NEXT"] = firstResult
            __cpm[this, "status_ITERATE_FUNC"] = iterateFunction
        # end function __m_TreeIterator (line 104)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
            this.PREV = 1
            this.NEXT = 2
            this.PARENT = 3
            this.PRECEDING = 4
            this.FOLLOWING = 5
        # end static initializer __csi (line 112)

        def __csu(this, *argv):
            # create the private field
            __cpm.create(this)
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 123)

        __cpiT = __x_dpif("TreeIterator", {"__slots__": ("status_ITERATE_FUNC", "status_NEXT", "status_ROOT", \
"status_TREE")})
        __clsT = __x_dcls("TreeIterator", __x_objT, {"__slots__": ("FOLLOWING", "NEXT", "PARENT", "PRECEDING", 
"PREV"), "__init__": __csi}, {"__slots__": (), "next": __m_next, "__init__": __m_TreeIterator})
        __cpm = __x_prmT(__clsT, __cpiT)
        return __clsT
    # end class factory TreeIterator, __c_TreeIterator (line 81)

    def __c_TreeIteratorResult():
        def __m_TreeIteratorResult(this, done, value):
            __csu(this)
            this.done = done
            this.value = value
        # end function __m_TreeIteratorResult (line 140)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 146)

        def __csu(this, *argv):
            # initialize properties
            this.done = False
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 152)

        __clsT = __x_dcls("TreeIteratorResult", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": (
"done", "value"), "__init__": __m_TreeIteratorResult})
        return __clsT
    # end class factory TreeIteratorResult, __c_TreeIteratorResult (line 139)

    def __c_TreePosition():
        def __h_DISCONNECTED(this):
            return 1
        # end function __h_DISCONNECTED (line 165)

        def __h_PRECEDING(this):
            return 2
        # end function __h_PRECEDING (line 169)

        def __h_FOLLOWING(this):
            return 4
        # end function __h_FOLLOWING (line 173)

        def __h_CONTAINS(this):
            return 8
        # end function __h_CONTAINS (line 177)

        def __h_CONTAINED__BY(this):
            return 16
        # end function __h_CONTAINED__BY (line 181)

        def __m_TreePosition(this):
            __csu(this)
            raise TypeError((u"TreePosition is not a constructor"))
        # end function __m_TreePosition (line 185)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 190)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 196)

        __clsT = __x_dcls("TreePosition", __x_objT, {"__slots__": (), "CONTAINED_BY": __x_prop(__h_CONTAINED__BY, None), 
"CONTAINS": __x_prop(__h_CONTAINS, None), "DISCONNECTED": __x_prop(__h_DISCONNECTED, None), "FOLLOWING": __x_prop(__h_FOLLOWING, None), 
"PRECEDING": __x_prop(__h_PRECEDING, None), "__init__": __csi}, {"__slots__": (), "__init__": __m_TreePosition})
        return __clsT
    # end class factory TreePosition, __c_TreePosition (line 164)

    def __c_SymbolTree():
        def __m_SymbolTree(this):
            __csu(this)
        # end function __m_SymbolTree (line 209)

        def __m_initialize(this, object):
            this._node(object)
            return object
        # end function __m_initialize (line 213)

        def __m___node(this, object):
            if __x_cb(__x_eq(object, None)):
                return None
            # end if (line 219)
            node = object._symbolTreeNode
            if __x_cb(__x_ne(node, None)):
                return node
            # end if (line 223)
            node = SymbolTreeNode()
            __r0 = object
            __r0._symbolTreeNode = node
            return node
        # end function _node(__m___node) (line 218)

        def __m_hasChildren(this, object):
            return this._node(object).hasChildren
        # end function __m_hasChildren (line 232)

        def __m_firstChild(this, object):
            return this._node(object).firstChild
        # end function __m_firstChild (line 236)

        def __m_lastChild(this, object):
            return this._node(object).lastChild
        # end function __m_lastChild (line 240)

        def __m_previousSibling(this, object):
            return this._node(object).previousSibling
        # end function __m_previousSibling (line 244)

        def __m_nextSibling(this, object):
            return this._node(object).nextSibling
        # end function __m_nextSibling (line 248)

        def __m_parent(this, object):
            return this._node(object).parent
        # end function __m_parent (line 252)

        def __m_childrenIterator(this, parent, reverse = (False)):
            parentNode = this._node(parent)
            return TreeIterator(this, parent, parentNode.lastChild if __x_cb(reverse) else parentNode.firstChild, 
TreeIterator.PREV if __x_cb(reverse) else TreeIterator.NEXT)
        # end function __m_childrenIterator (line 256)

        def __m_previousSiblingsIterator(this, object):
            return TreeIterator(this, object, this._node(object).previousSibling, TreeIterator.PREV)
        # end function __m_previousSiblingsIterator (line 262)

        def __m_nextSiblingsIterator(this, object):
            return TreeIterator(this, object, this._node(object).nextSibling, TreeIterator.NEXT)
        # end function __m_nextSiblingsIterator (line 266)

        def __m_ancestorsIterator(this, object):
            return TreeIterator(this, object, object, TreeIterator.PARENT)
        # end function __m_ancestorsIterator (line 270)

        def __m_remove(this, removeObject):
            removeNode = this._node(removeObject)
            parentNode = this._node(removeNode.parent)
            prevNode = this._node(removeNode.previousSibling)
            nextNode = this._node(removeNode.nextSibling)
            if __x_cb(__x_ne(parentNode, None)):
                if __x_cb(__x_eq(parentNode.firstChild, removeObject)):
                    __r0 = parentNode
                    __r0.firstChild = removeNode.nextSibling
                # end if (line 280)
                if __x_cb(__x_eq(parentNode.lastChild, removeObject)):
                    __r1 = parentNode
                    __r1.lastChild = removeNode.previousSibling
                # end if (line 284)
            # end if (line 279)
            if __x_cb(__x_ne(prevNode, None)):
                __r2 = prevNode
                __r2.nextSibling = removeNode.nextSibling
            # end if (line 289)
            if __x_cb(__x_ne(nextNode, None)):
                __r3 = nextNode
                __r3.previousSibling = removeNode.previousSibling
            # end if (line 293)
            __r4 = removeNode
            __r4.parent = None
            __r5 = removeNode
            __r5.previousSibling = None
            __r6 = removeNode
            __r6.nextSibling = None
            __r7 = removeNode
            __r7.cachedIndex = -1
            __r8 = removeNode
            __r8.cachedIndexVersion = NaN
            if __x_cb(__x_ne(parentNode, None)):
                parentNode.childrenChanged()
            # end if (line 307)
            return removeObject
        # end function __m_remove (line 274)

        def __m_insertBefore(this, referenceObject, newObject):
            referenceNode = this._node(referenceObject)
            prevNode = this._node(referenceNode.previousSibling)
            newNode = this._node(newObject)
            parentNode = this._node(referenceNode.parent)
            if __x_cb(newNode.isAttached):
                raise Error((u"Given object is already present in this SymbolTree, remove it first"))
            # end if (line 318)
            __r0 = newNode
            __r0.parent = referenceNode.parent
            __r1 = newNode
            __r1.previousSibling = referenceNode.previousSibling
            __r2 = newNode
            __r2.nextSibling = referenceObject
            __r3 = referenceNode
            __r3.previousSibling = newObject
            if __x_cb(__x_ne(prevNode, None)):
                __r4 = prevNode
                __r4.nextSibling = newObject
            # end if (line 329)
            if __x_cb(__x_cb(__x_ne(parentNode, None)) and __x_eq(parentNode.firstChild, referenceObject)):
                __r5 = parentNode
                __r5.firstChild = newObject
            # end if (line 333)
            if __x_cb(__x_ne(parentNode, None)):
                parentNode.childrenChanged()
            # end if (line 337)
            return newObject
        # end function __m_insertBefore (line 313)

        def __m_insertAfter(this, referenceObject, newObject):
            referenceNode = this._node(referenceObject)
            nextNode = this._node(referenceNode.nextSibling)
            newNode = this._node(newObject)
            parentNode = this._node(referenceNode.parent)
            if __x_cb(newNode.isAttached):
                raise Error((u"Given object is already present in this SymbolTree, remove it first"))
            # end if (line 348)
            __r0 = newNode
            __r0.parent = referenceNode.parent
            __r1 = newNode
            __r1.previousSibling = referenceObject
            __r2 = newNode
            __r2.nextSibling = referenceNode.nextSibling
            __r3 = referenceNode
            __r3.nextSibling = newObject
            if __x_cb(__x_ne(nextNode, None)):
                __r4 = nextNode
                __r4.previousSibling = newObject
            # end if (line 359)
            if __x_cb(__x_cb(__x_ne(parentNode, None)) and __x_eq(parentNode.lastChild, referenceObject)):
                __r5 = parentNode
                __r5.lastChild = newObject
            # end if (line 363)
            if __x_cb(__x_ne(parentNode, None)):
                parentNode.childrenChanged()
            # end if (line 367)
            return newObject
        # end function __m_insertAfter (line 343)

        def __m_prependChild(this, referenceObject, newObject):
            referenceNode = this._node(referenceObject)
            newNode = this._node(newObject)
            if __x_cb(newNode.isAttached):
                raise Error((u"Given object is already present in this SymbolTree, remove it first"))
            # end if (line 376)
            if __x_cb(referenceNode.hasChildren):
                this.insertBefore(referenceNode.firstChild, newObject)
            else:
                __r0 = newNode
                __r0.parent = referenceObject
                __r1 = referenceNode
                __r1.firstChild = newObject
                __r2 = referenceNode
                __r2.lastChild = newObject
                referenceNode.childrenChanged()
            # end if (line 379)
            return newObject
        # end function __m_prependChild (line 373)

        def __m_appendChild(this, referenceObject, newObject):
            referenceNode = this._node(referenceObject)
            newNode = this._node(newObject)
            if __x_cb(newNode.isAttached):
                raise Error((u"Given object is already present in this SymbolTree, remove it first"))
            # end if (line 396)
            if __x_cb(referenceNode.hasChildren):
                this.insertAfter(referenceNode.lastChild, newObject)
            else:
                __r0 = newNode
                __r0.parent = referenceObject
                __r1 = referenceNode
                __r1.firstChild = newObject
                __r2 = referenceNode
                __r2.lastChild = newObject
                referenceNode.childrenChanged()
            # end if (line 399)
            return newObject
        # end function __m_appendChild (line 393)

        def __csi(this):
            # super
            __x_objT.__init__(this)
            # initialize properties
        # end static initializer __csi (line 413)

        def __csu(this, *argv):
            # initialize properties
            # super
            super(__clsT, this).__init__(*argv)
        # end instance initializer and super constructor __csu (line 419)

        __clsT = __x_dcls("SymbolTree", __x_objT, {"__slots__": (), "__init__": __csi}, {"__slots__": (), "_node": __m___node, 
"ancestorsIterator": __m_ancestorsIterator, "appendChild": __m_appendChild, "childrenIterator": __m_childrenIterator, 
"firstChild": __m_firstChild, "hasChildren": __m_hasChildren, "initialize": __m_initialize, "insertAfter": __m_insertAfter, 
"insertBefore": __m_insertBefore, "lastChild": __m_lastChild, "nextSibling": __m_nextSibling, "nextSiblingsIterator": __m_nextSiblingsIterator, 
"parent": __m_parent, "prependChild": __m_prependChild, "previousSibling": __m_previousSibling, "previousSiblingsIterator": __m_previousSiblingsIterator, 
"remove": __m_remove, "__init__": __m_SymbolTree})
        return __clsT
    # end class factory SymbolTree, __c_SymbolTree (line 208)

    Error = Exception
    SymbolTreeNode = __c_SymbolTreeNode()
    TreeIterator = __c_TreeIterator()
    TreeIteratorResult = __c_TreeIteratorResult()
    TreePosition = __c_TreePosition()
    SymbolTree = __c_SymbolTree()
# program end


__()
