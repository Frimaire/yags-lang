# Yet Another Glue Script
Yet Another Glue Script (YAGS) - Not only python with braces!

YAGS is an js-like language compiled to Python.

Highlights
----------

-   Braces are used instead of indentation. Of course, indentation still helps improve the readability of the code and is recommended.
-   A syntax close to JavaScript or ECMAScript. Developers who are familiar with js can get started quickly, while users of other C-family languages will not have too many difficulties in understanding it.
-   Runs in Python environment and has good interoperability. Existing modules in Python such as NumPy also work.

Trending
--------

Please follow the [related discussion](https://github.com/Frimaire/yags-lang/issues/1 "wikilink") about destructuring assignment and function parameters and help me introduce these features.

A Glance
--------

### Hello World

``` javascript
print('Hello World!');
```

### Complex Literal

``` javascript
print((1 - 1j) ** 2 + 2i);
```

### Spread Syntax

Expected output: 0 1 2 3 4 5 6 7 8 9 10 100 1000 10000

``` javascript
print(0, ...[1, ...range(2, 10), 10, ...[100, 1000]], 10000);
```

### Ternary Conditional Operator

Count the steps to reach 1 in 3n+1 problem. (OEIS [A006577](https://oeis.org/A006577)).

``` javascript
function collatz(n) {
    return n == 1 ? 0 : collatz(n % 2 == 1 ? 3 * n + 1 : n / 2) + 1;
}
print(collatz(27)); // 111
```

### Closure

Expected output: 1 5 14 30 55 91 140 204 285 385

``` javascript
function gen(s) {
    var n = 1;
    return function() {
        s += n ** 2;
        n++;
        return s;
    };
}

var f = gen(0);
var k = 0;
while(k++ < 10) {
    print(f());
}
```

### Import

Calculate integration using the [scipy library](https://docs.scipy.org/doc/scipy/tutorial/integrate.html).

``` javascript
var {pi: PI, sin, cos} = import('math');
var {quad} = import('scipy.integrate');

var f = 100;

print(quad(function(t) {
    return cos(2 * PI * f * t) ** 2;
}, 0, 1)[0]); // exact value is 1/2

print(quad(function(t) {
    return cos(2 * PI * f * t) * sin(2 * PI * f * t);
}, 0, 1)[0]); // exact value is 0
```

### Class

ES4-style classes definition can be used. `public` and `private` can be used as access modifiers.

``` actionscript
class Rectangle {
    private var h;
    private var w;

    public function get area() {
        return this.w * this.h;
    }

    public function Rectangle(width, height) {
        this.w = width;
        this.h = height;
    }
}

print((new Rectangle(5, 6)).area); // 30
```

Goals
-----

1.  Provide language features similar to ECMAScript.
2.  Has stricter features than standard ECMAScript to reduce common errors and avoid confusion for unskilled ES users.
3.  Provide an easy-to-use mechanism to use Python modules in YAGS code or make modules written in YAGS available to Python code.
4.  Suitable for writing small scripts or tools, but it can also be used to write a huge project.

At the same time, these are not the design goals of YAGS:

1.  YAGS will not completely implement an ECMAScript standard. In other words, this is not a tool for running unmodified js code.
2.  YAGS is not designed for "write less". It does not have many syntactic sugars or other language features that are difficult for beginners to understand.

The implementation of YAGS is divided into three levels. Currently, only Level 0 (that is, the compiler) has been implemented and Level 1 is in progress.

1.  Level 0: This level only provides syntax-level features without changing the corresponding behavior, and uses Python's native built-in objects. (`[]` produces `list`, and `{}` produces `dict`)
2.  Level 1: This level has complete language features, including a set of built-in objects.
3.  Level 2: Based on Level 1, this level provides variable type checking.
