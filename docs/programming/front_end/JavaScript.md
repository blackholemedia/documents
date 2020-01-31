
Table of Contents
=================

   * [JavaScript](#javascript)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [基本用法](#基本用法)
         * [位置](#位置)
         * [输出](#输出)
         * [语句](#语句)
         * [语法](#语法)

Created by ALTA


# JavaScript  

## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [JavaScript 教程](<https://www.w3school.com.cn/js/index.asp>)

## 基本用法  

### 位置

在 HTML 中，JavaScript 代码必须位于 `<script>` 与`</script>` 标签之间。

1. JavaScript脚本可被放置与 HTML 页面的`<body>` 或 `<head>` 部分中，或兼而有之

2. JavaScript脚本也可以放置于外部文件中， 通过`<script>` 标签的 src (source) 属性中进行引用

   ```html
   <script src="myScript.js"></script>
   ```

### 输出  

<u>JavaScript 不提供任何内建的打印或显示函数</u>，故JavaScript通常采用以下方式进行显示：

1. 使用 window.alert() 写入警告框

2. 使用 document.write() 写入 HTML 输出

   出于测试目的，使用 document.write() 比较方便：

   ```html
   <!DOCTYPE html>
   <html>
   <body>
   
   <h1>我的第一张网页</h1>
   
   <p>我的第一个段落</p>
   
   <script>
   document.write(5 + 6);
   </script>
   
   </body>
   </html> 
   ```

3. 使用 innerHTML 写入 HTML 元素

   先访问 HTML 元素，然后修改(定义)元素内容。更改 HTML 元素的 innerHTML 属性是在 HTML 中显示数据的常用方法。

   ```html
   <!DOCTYPE html>
   <html>
   <body>
   
   <h1>我的第一张网页</h1>
   
   <p>我的第一个段落</p>
   
   <p id="demo"></p>
   
   <script>
    document.getElementById("demo").innerHTML = 5 + 6;
   </script>
   
   </body>
   </html> 
   ```

4. 使用 console.log() 写入浏览器控制台

   ```html
   <!DOCTYPE html>
   <html>
   <body>
   
   <h1>我的第一张网页</h1>
   
   <p>我的第一个段落</p>
   
   <script>
   console.log(5 + 6);
   </script>
   
   </body>
   </html>
   ```

### 语句  

1. 分号

   分号分隔 JavaScript 语句。分号是非必须但推荐

   ```javascript
   a = 5; b = 6; c = a + b;
   ```

2. 空白字符  

   JavaScript 会忽略多个空格。下述代码等价：

   ```javascript
   var person = "Bill";
   var person="Bill"; 
   ```

3. 代码块

   JavaScript 语句可以用花括号（{...}）组合在代码块中。

   ```javascript
   function myFunction() {
       document.getElementById("demo").innerHTML = "Hello Kitty.";
       document.getElementById("myDIV").innerHTML = "How are you?";
   }
   ```

### 语法  

1. 注释

   双斜杠 // 或 /* 与 **/* 之间的代码被视为注释 

2. 标识符

   标识符是名称，在 JavaScript 中，标识符用于命名变量（以及关键词、函数和标签）。<u>大小写敏感</u>

3. 驼峰式大小写

   JavaScript 程序员倾向于使用以小写字母开头的驼峰大小写：

   ```javascript
   firstName, lastName, masterCard, interCity
   ```

4. 变量

   声明变量时可向它赋值：

   ```javascript
   var carName = "porsche";
   
   var person = "Bill Gates", carName = "porsche", price = 15000;
   
   var person = "Bill Gates",
   carName = "porsche",
   price = 15000;
   ```

   提示：如果把要给数值放入引号中，其余数值会被视作字符串并被级联。

   ```javascript
   var x = 3 + 5 + "8";
   ```

5. 运算符

   详细参考： [JavaScript运算符](<https://www.w3school.com.cn/js/js_operators.asp>)

6. 数据类型

   JavaScript 拥有动态类型。这意味着相同变量可用作不同类型：

   ```javascript
   var x;               // 现在 x 是 undefined
   var x = 7;           // 现在 x 是数值
   var x = "Bill";      // 现在 x 是字符串值
   ```

   