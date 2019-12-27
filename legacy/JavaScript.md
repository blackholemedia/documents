
Table of Contents
=================

   * [JavaScript](#javascript)
      * [关键词](#关键词)
      * [关键叙述](#关键叙述)
         * [定义](#定义)
         * [基本语法](#基本语法)
         * [数据类型](#数据类型)
         * [函数](#函数)
         * [方法](#方法)
         * [高阶函数](#高阶函数)
         * [闭包](#闭包)
         * [箭头函数](#箭头函数)
         * [Generator](#generator)
      * [标准对象](#标准对象)
         * [包装对象](#包装对象)
         * [Date](#date)
         * [RegExp](#regexp)
         * [JSON](#json)
      * [面向对象编程](#面向对象编程)
         * [基本叙述](#基本叙述)
         * [创建对象](#创建对象)
         * [原型继承](#原型继承)
         * [CLASS继承](#class继承)
      * [浏览器](#浏览器)
         * [浏览器对象](#浏览器对象)
         * [操作DOM](#操作dom)
      * [错误处理](#错误处理)
         * [try...catch...finally](#trycatchfinally)
         * [错误类型](#错误类型)
         * [抛出错误](#抛出错误)
         * [异步错误处理](#异步错误处理)

Created by [I am your father]
# JavaScript  
回调函数  
非阻塞I/O  
事件循环  
事件驱动  

## 关键叙述  
### 定义  
JavaScript是一种运行在浏览器中的解释型的编程语言

### 基本语法  

1. 每条语句后加 ;

2. ｛｝用于包含语句块

   ```javascript
   if (2 > 1) {
       x = 1;
       y = 2;
       z = 3;
   }
   ```

3. JavaScript严格区分大小写

### 数据类型  

1. 比较运算符

   - ==，会自动转换数据类型再比较，很多时候，会得到非常诡异的结果
   - ===，不会自动转换数据类型，如果数据类型不一致，返回`false`，如果一致，再比较
   - 比较两个浮点数是否相等，只能计算它们之差的绝对值，看是否小于某个阈值   `Math.abs(1 / 3 - (1 - 2 / 3)) < 0.0000001;`
   - `NaN`这个特殊的Number与所有其他值都不相等，包括自己，只能用isNaN()函数判断
   - `null`表示一个“空”的值，它和`0`以及空字符串`''`不同，`0`是一个数值，`''`表示长度为0的字符串，而`null`表示“空”

2. 对象，python中的字典，key限定为字符串

   - 最后一个键值对不需要在末尾添加","
   - 访问不存在的属性不报错，而是返回`undefined`
   - 一个属性是否是`对象`自身拥有的，而不是继承得到的，可以用`hasOwnProperty()`方法

3. 声明及赋值变量均不需要指定类型，*变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错*

4. 条件判断

   ```javascript
   var age = 3;
   if (age >= 18) {
       alert('adult');
   } else if (age >= 6) {
       alert('teenager');
   } else {
       alert('kid');
   }
   ```

5. 循环

   - for循环(接近C语言)

     ```javascript
     var x = 0;
     var i;
     for (i=1; i<=10000; i++) {
         x = x + i;
     }
     ```

   - for...in循环

     ```javascript
     var o = {
         name: 'Jack',
         age: 20,
         city: 'Beijing'
     };
     for (var key in o) {
         console.log(key); // 'name', 'age', 'city'
     }
     ```

   - for...of循环

     ```javascript
     var o = {
         name: 'Jack',
         age: 20,
         city: 'Beijing'
     };
     for (var key of o) {
         console.log(key); // 'jack', 20, 'Beijing'
     }
     ```

   - while循环

   - do...while循环

6. Map/Set

   - Map对应Python中的字典，只是key可以为任意数值类型，不限定为字符串
   - Set对应python中的tulpe

7. `forEach()`方法, 参考[iterable](<https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143450082788640f82a480be8481a8ce8272951a40970000>) 

### 函数  

1. 定义和调用

   - 函数定义方式1(x为函数参数，多个参数用`,`分隔)：

     ```javascript
     function abs(x) {
         if (x >= 0) {
             return x;
         } else {
             return -x;
         }
     }
     ```

   - 函数定义方式2(匿名函数赋予变量，末尾加`;`)：

     ```javascript
     var abs = function (x) {
         if (x >= 0) {
             return x;
         } else {
             return -x;
         }
     };
     ```

   - 函数参数 arguments, 如bash里面的参数，用法类似数组

     ```javascript
     // foo(a[, b], c)
     // 接收2~3个参数，b是可选参数，如果只传2个参数，b默认为null：
     function foo(a, b, c) {
         if (arguments.length === 2) {
             // 实际拿到的参数是a和b，c为undefined
             c = b; // 把b赋给c
             b = null; // b变为默认值
         }
         // ...
     }
     ```

   - 函数参数 rests, 类似与Python中的`*args`, 参数接收为数组

     ```javascript
     function foo(a, b, ...rest) {
         console.log('a = ' + a);
         console.log('b = ' + b);
         console.log(rest);
     }
     
     foo(1, 2, 3, 4, 5);
     // 结果:
     // a = 1
     // b = 2
     // Array [ 3, 4, 5 ]
     
     foo(1);
     // 结果:
     // a = 1
     // b = undefined
     // Array []
     ```

2. 变量作用域

   - 变量提升  
     先扫描整个函数体的语句，把所有申明的变量“提升”到函数顶部, 只提升声明，赋值不提升，因此需要严格遵守“在函数内部首先申明所有变量”这一规则

     ```javascript
     function foo() {
         var
             x = 1, // x初始化为1
             y = x + 1, // y初始化为2
             z, i; // z和i为undefined
         // 其他语句:
         for (i=0; i<100; i++) {
             ...
         }
     }
     ```

   - 全局作用域  
     JavaScript实际上只有一个全局作用域。任何变量（函数也视为变量）如果没有在当前函数作用域中找到，就会继续往上查找。JavaScript默认有一个全局对象`window`，全局作用域的变量实际上被绑定到`window`的一个属性

   - 块级作用域  
   函数体内声明的变量作用于整个函数体内：

     ```javascript
     'use strict';
     
     function foo() {
         for (var i=0; i<100; i++) {
             //
         }
         i += 100; // 仍然可以引用变量i
     }
     ```

     有时候需要缩小变量的作用域，采用`let`作声明:

     ```javascript
     'use strict';
     
     function foo() {
         var sum = 0;
         for (let i=0; i<100; i++) {
             sum += i;
         }
         // SyntaxError:
         i += 1;
     }
     ```

     

3. 命名空间
  
   全局变量会绑定到`window`上，不同的JavaScript文件如果使用了相同的全局变量会造成命名冲突，解决办法：把自己的所有变量和函数全部绑定到一个全局变量中

4. 解构赋值  

    对一组变量同时进行赋值

### 方法  

1. 概念与Python中方法概念一致, 给对象绑定函数

2. `this`关键字

   作用大体等同于Python方法中的self, 指代当前对象，区别如下：

   - 对象的方法形式调用，比如`xiaoming.age()`，该函数的`this`指向被调用的对象，也就是`xiaoming`；独立调用函数，比如`getAge()`，此时，该函数的`this`指向全局对象`window`或指向`undefined`(strict模式)

     ```javascript
     function getAge() {
         var y = new Date().getFullYear();
         return y - this.birth;
     }
     
     var xiaoming = {
         name: '小明',
         birth: 1990,
         age: getAge
     };
     
     xiaoming.age(); // 25, 正常结果
     getAge(); // NaN
     ```

   - 函数内部定义的函数，this指向undefined而非指向对象，解决方法如下，用一个`that`变量捕获`this`：

     ```javascript
     'use strict';
     
     var xiaoming = {
         name: '小明',
         birth: 1990,
         age: function () {
             var that = this; // 在方法内部一开始就捕获this
             function getAgeFromBirth() {
                 var y = new Date().getFullYear();
                 return y - that.birth; // 用that而不是this
             }
             return getAgeFromBirth();
         }
     };
     
     xiaoming.age(); // 25
     ```

   - 独立调用函数：根据是否是strict模式，`this`指向`undefined`或`window`，**可以用`apply`控制`this`的指向**

     ```javascript
     function getAge() {
         var y = new Date().getFullYear();
         return y - this.birth;
     }
     
     var xiaoming = {
         name: '小明',
         birth: 1990,
         age: getAge
     };
     
     xiaoming.age(); // 25
     getAge.apply(xiaoming, []); // 25, this指向xiaoming, 参数为空
     ```
     apply方法，它接收两个参数，第一个参数就是需要绑定的this变量，第二个参数是Array，表示函数本身的参数，与apply()类似的方法是call()，唯一区别是：apply()把参数打包成Array再传入，call()把参数按顺序传入

     ```javascript
     Math.max.apply(null, [3, 5, 4]); // 5
     Math.max.call(null, 3, 5, 4); // 5
     ```

   - 装饰器  
     待补充

### 高阶函数  
基本与python高阶函数一致，以一个函数作为另一个函数的参数，主要包含map/reduce/filter/sort  
1. map
    map()方法定义在JavaScript的Array中，调用Array的map()方法，传入函数，就得到了一个新的Array，用法同python

  ```javascript
  var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  var results = arr.map(pow); // [1, 4, 9, 16, 25, 36, 49, 64, 81]
  console.log(results);
  ```
2. reduce  
     reduce()方法同样定义在JavaScript的Array中，用法同python

3. filter
     filter()方法同样定义在JavaScript的Array中，用法同python

     ```javascript
     var arr = ['A', 'B', 'C'];
     var r = arr.filter(function (element, index, self) {
         console.log(element); // 依次打印'A', 'B', 'C'
         console.log(index); // 依次打印0, 1, 2
         console.log(self); // self就是变量arr
         return true;
     });
     ```
4. sort  
   - sort()方法会直接对Array进行修改，它返回的结果仍是当前Array  

   - Array的sort()方法默认把所有元素先转换为String再排序，结果'10'排在了'2'的前面，因为字符'1'比字符'2'的ASCII码小

   - 通常用法，采用高阶函数，排序在参数函数中实现

     ```javascript
     var arr = [10, 20, 1, 2];
     arr.sort(function (x, y) {
         if (x < y) {
             return 1;
         }
         if (x > y) {
             return -1;
         }
         return 0;
     }); // [20, 10, 2, 1]
     ```
### 闭包  
大坑待填
### 箭头函数
1. 类似于匿名函数
```javascript
// 两个参数:
(x, y) => x * x + y * y

// 无参数:
() => 3.14

// 可变参数:
(x, y, ...rest) => {
    var i, sum = x + y;
    for (i=0; i<rest.length; i++) {
        sum += rest[i];
    }
    return sum;
}
```
2.返回对象需注意单表达式，如果是单表达式，需要增加括号：

```javascript
// ok:
x => ({ foo: x })
// SyntaxError:
x => { foo: x }
```
3.与匿名函数的区别：箭头函数内部的this是词法作用域，由上下文确定

```javascript
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = function () {
            return new Date().getFullYear() - this.birth; // this指向window或undefined
        };
        return fn();
    }
};
```
```javascript
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = () => new Date().getFullYear() - this.birth; // this指向obj对象
        return fn();
    }
};
obj.getAge(); // 25
```
由于this在箭头函数中已经按照词法作用域绑定了，所以，用call()或者apply()调用箭头函数时，无法对this进行绑定，即传入的第一个参数被忽略

```javascript
var obj = {
    birth: 1990,
    getAge: function (year) {
        var b = this.birth; // 1990
        var fn = (y) => y - this.birth; // this.birth仍是1990
        return fn.call({birth:2000}, year);
    }
};
obj.getAge(2015); // 25
```
### Generator  
与python基本一致，详细参考[Generator](<https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/00143450083887673122b45a4414333ac366c3c935125e7000>).  

## 标准对象  

### 包装对象  

函数前➕new,结果就是包装对象

```javascript
var n = new Number(123)
typeof n; // 'object'

var n = Number('123'); // 123，相当于parseInt()或parseFloat()
typeof n; // 'number'
```

### Date  
参考[date](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499525761186acdd5ac3a44f8a50cc0ed8606139b000)  

### RegExp  
参考 [RegExp](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499503920bb7b42ff6627420da2ceae4babf6c4f2000)  

### JSON  
序列化与反序列化：参考 [JSON](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434499490767fe5a0e31e17e44b69dcd1196f7ec6fc6000)  

## 面向对象编程  

JavaScript不区分类和实例的概念，而是通过原型（prototype）来实现面向对象编程，所有对象都是实例，所谓继承关系不过是把一个对象的原型指向另一个对象而已  

### 基本叙述  

1. 根据原型创建对象的演示,下述代码仅用于演示目的

   ```javascript
   var Student = {
       name: 'Robot',
       height: 1.2,
       run: function () {
           console.log(this.name + ' is running...');
       }
   };
   
   var xiaoming = {
       name: '小明'
   };
   
   xiaoming.__proto__ = Student;
   ```
   2.根据原型创建对象  
   编写JavaScript代码时，不要直接用`obj.__proto__`去改变一个对象的原型，并且低版本的IE也无法使用`__proto__`。Object.create()方法可以传入一个原型对象，并创建一个基于该原型的新对象，但是新对象什么属性都没有，可以编写一个函数来创建`xiaoming`  

   ```javascript
   // 原型对象:
   var Student = {
       name: 'Robot',
       height: 1.2,
       run: function () {
           console.log(this.name + ' is running...');
       }
   };
   
   function createStudent(name) {
       // 基于Student原型创建一个新对象:
       var s = Object.create(Student);
       // 初始化新对象:
       s.name = name;
       return s;
   }
   
   var xiaoming = createStudent('小明');
   xiaoming.run(); // 小明 is running...
   xiaoming.__proto__ === Student; // true
   ```
### 创建对象   

1. 原型链
    创建一个Array对象，其原型链是：

  ```javascript
  arr ----> Array.prototype ----> Object.prototype ----> null
  ```

2. 构造函数  
   用关键字`new`来调用普通函数，并返回一个对象， 普通函数变为构造函数

```javascript
function Student(name) {
    this.name = name;
    this.hello = function () {
        alert('Hello, ' + this.name + '!');
    }
}

var xiaoming = new Student('小明');
xiaoming.name; // '小明'
xiaoming.hello(); // Hello, 小明!
```
新创建对象的原型链为

```javascript
xiaoming ----> Student.prototype ----> Object.prototype ----> null
```
![原型链](./statics/prototypechain.png)
用new Student()创建的对象还从原型上获得了一个constructor属性，它指向函数Student本身,另外函数Student恰好有个属性prototype指向xiaoming、xiaohong的原型对象。一句话：**函数的prototype属性指向原型对象，原型对象的constructor属性指向函数，继承者`xiaoming`继承的是原型对象，所以`xiaoming`有constructor属性而没有prototype属性**，要让创建的对象共享一个`hello`函数，根据对象的属性查找原则，我们只要把`hello`函数移动到`xiaoming`、`xiaohong`这些对象共同的原型上即可

```javascript
function Student(name) {
    this.name = name;
}

Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
};
```

3.常用编程模式  
按照约定，构造函数首字母应当大写，而普通函数首字母应当小写。编写一个createStudent()函数，在内部封装所有的new操作，以免遗漏new关键字

```javascript
function Student(props) {
    this.name = props.name || '匿名'; // 默认值为'匿名'
    this.grade = props.grade || 1; // 默认值为1
}

Student.prototype.hello = function () {
    alert('Hello, ' + this.name + '!');
};

function createStudent(props) {
    return new Student(props || {})
}
```
### 原型继承  
待补充

### CLASS继承  

```javascript
class Student {
    constructor(name) {
        this.name = name;
    }

    hello() {
        alert('Hello, ' + this.name + '!');
    }
}

var xiaoming = new Student('小明'); // 与前面创建对象代码完全一致
xiaoming.hello();
```
1. class继承

   ```javascript
   class PrimaryStudent extends Student {
       constructor(name, grade) {
           super(name); // 记得用super调用父类的构造方法!
           this.grade = grade;
       }
   
       myGrade() {
           alert('I am at grade ' + this.grade);
       }
   }
   ```

## 浏览器  

### 浏览器对象  

1. windows  
window既是充当全局作用域，又表示浏览器窗口  
2. screen  
3. navigator  
4. location  
5. document  
document对象就是整个DOM树的根节点  

### 操作DOM  

由于HTML文档被浏览器解析后就是一棵DOM树，要改变HTML的结构，就需要通过JavaScript来操作DOM。

## 错误处理  

### try...catch...finally  

```javascript
var r1, r2, s = null;
try {
    r1 = s.length; // 此处应产生错误
    r2 = 100; // 该语句不会执行
} catch (e) {
    console.log('出错了：' + e);
} finally {
    console.log('finally');
}
console.log('r1 = ' + r1); // r1应为undefined
console.log('r2 = ' + r2); // r2应为undefined
```
注意，catch和finally可以不必都出现。也就是说，try语句一共有三种形式
### 错误类型  
JavaScript有一个标准的Error对象表示错误，还有从Error派生的TypeError、ReferenceError等错误对象。我们在处理错误时，可以通过catch(e)捕获的变量e访问错误对象

```javascript
try {
    ...
} catch (e) {
    if (e instanceof TypeError) {
        alert('Type error!');
    } else if (e instanceof Error) {
        alert(e.message);
    } else {
        alert('Error: ' + e);
    }
}
```

### 抛出错误  

```javascript
var r, n, s;
try {
    s = prompt('请输入一个数字');
    n = parseInt(s);
    if (isNaN(n)) {
        throw new Error('输入错误');
    }
    // 计算平方:
    r = n * n;
    console.log(n + ' * ' + n + ' = ' + r);
} catch (e) {
    console.log('出错了：' + e);
}
```

### 异步错误处理  

**JavaScript引擎是一个事件驱动的执行引擎，代码总是以单线程执行，而回调函数的执行需要等到下一个满足条件的事件出现后，才会被执行**  

```javascript
function printTime() {
    throw new Error();
}

try {
    setTimeout(printTime, 1000);
    console.log('done');
} catch (e) {
    console.log('error');
}
```

在于调用`setTimeout()`函数时，传入的`printTime`函数并未立刻执行！紧接着，JavaScript引擎会继续执行`console.log('done');`语句，而此时并没有错误发生。直到1秒钟后，执行`printTime`函数时才发生错误，但此时除了在`printTime`函数内部捕获错误外，外层代码并无法捕获