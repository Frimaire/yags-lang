var {ArrayList} = import('.compat');

function chkKey(s) {
    if(!(s instanceof type(''))) {
        throw new TypeError('key is not a string');
    }
    return s;
}

/**
 * A Map with the key of String
 */
public class StringMap {
    private var o;

    /**
     * initializer
     */
    public function StringMap(source = null) {
        this.o = {};
        (new ArrayList(source)).forEach(function(g, i, a):void {
            var k = chkKey(g[0]);
            var v = g[1];
            if(this.has(k)) {
                throw new AttributeError('key ' + k + ' is existed');
            }
            this.set(k, v);
        });
    }

    /**
     * get the item
     * @param {String} key
     * @param {*} defaultValue, throw if key doesn't exist and defaultValue is not given
     */
    public function get(key, ...defval) {
        var dfv = (new ArrayList(defval));
        if(dfv.length >= 2) {
            throw new TypeError('Only one default value is allowed');
        }
        key = chkKey(key);
        if(dfv.length === 0) {
            return this.o[key];
        }
        return this.o.get(key, dfv.get(0));
    }

    /**
     * set the item
     * @param {String} key
     * @param {*} value
     */
    public function set(key:String, value:*):StringMap {
        key = chkKey(key);
        this.o[key] = value;
        return this;
    }

    /**
     * set the multiple item
     * @param {Array} key
     * @param {*} value
     */
    public function sets(keys:*, value:*):StringMap {
        (new ArrayList(keys)).forEach(function(k, n, a) {
            this.set(k, value);
        });
		return this;
    }

    /**
     * check if the key exists
     * @param {String} key
     */
    public function has(key) {
        key = chkKey(key);
        return this.o.__contains__(key);
    }

    /**
     * delete the item
     * @param {String} key
     */
    public function remove(key) {
        key = chkKey(key);
        if(!this.has(key)) {
            throw new AttributeError('key ' + key + ' doesn\'t exist');
        }
        delete this.o[key];
        return this;
    }
    
    /**
     * iterate the Object
     * @param {Function} callback(item, key, self)
     * callback can return boolean false to stop the iteration
     */
    public function forEach(callback):void {
        var a0 = [...this.o];
        // sort the keys at first
        a0.sort();
        (new ArrayList(a0)).forEach(function(i, k, a) {
			if (callback( this.o[ i ], i, this ) === false) {
				return false;
			}
        });
    }
    
    /**
     * count the items
     */
    public function get length():Number {
        return len(this.o);
    }
}

