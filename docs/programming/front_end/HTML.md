
Table of Contents
=================

  * [阅读说明](#阅读说明)
  * [参考引用](#参考引用)
  * [基本概念](#基本概念)
     * [什么是HTML](#什么是html)
     * [HTML标签](#html标签)
     * [HTML元素](#html元素)
     * [HTML元素-其他分类标准](#html元素-其他分类标准)
     * [HTML属性](#html属性)
     * [HTML样式](#html样式)
     * [HTML类](#html类)
     * [HTML脚本](#html脚本)
     * [HTML文档类型](#html文档类型)
     * [HTML实体](#html实体)

Created by ALTA

## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站：

1. [HTML教程](<https://www.w3school.com.cn/html/index.asp>)

## 基本概念  

### 什么是HTML  

HTML 是用来描述网页的一种语言。  

* HTML 不是一种编程语言，而是一种*标记语言* (markup language)
* 标记语言是一套*标记标签* (markup tag)
* HTML 使用*标记标签*来描述网页

### HTML标签  

HTML 标签是 1.由*尖括号*包围的关键词；2.成对出现；3.开始标签(开放标签)、结束标签(闭合标签)

标准标签请参考： [标签参考手册](<https://www.w3school.com.cn/tags/index.asp>)， [标签参考手册-功能分类](<https://www.w3school.com.cn/tags/html_ref_byfunc.asp>)

### HTML元素  

**HTML 文档是由 HTML 元素定义的。**

<font color=Red>HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。</font><font color=green>换言之元素的种类与标签的种类一一对应</font>

常见元素如下：

1. 标题元素

   对应标签`<h1>` to `<h6>`

   ```html
   <h1>This is a heading</h1>
   ```

2. 水平线元素  

   对应标签`<hr> `

   ```html
   <p>This is a paragraph</p>
   <hr />
   <p>This is a paragraph</p>
   ```

3. 注释元素  

   对应标签`<!-->`

   ```html
   <!-- This is a comment -->
   ```

4. 段落元素  

   对应标签`<p>`

   ```html
   <p>This is my first paragraph.</p>
   ```

5. 主体元素

   对应标签`<body>`,定义HTML文档的主体

   ```html
   <body>
   <p>This is my first paragraph.</p>
   </body>
   ```

6. 文档元素

   对应标签`<html>`， 定义整个 HTML 文档

   ```html
   <html>
   
   <body>
   <p>This is my first paragraph.</p>
   </body>
   
   </html>
   ```

7. 头部元素

   对应标签`<head>`, `<head>`元素是所有头部元素的容器。`<head>`内的元素可包含脚本，指示浏览器在何处可以找到样式表，提供元信息，等等。以下标签都可以添加到 head 部分：`<title>`、`<base>`、`<link>`、`<meta>`以及`<style>`

### HTML元素-其他分类标准  

1. HTML块元素(block level element)

   大多数 HTML 元素被定义为块级元素或内联元素。块级元素在浏览器显示时，通常会以新行来开始（和结束），如：`<h1>, <p>, <ul>, <table>`

   `<div>`元素属于典型的块元素，该元素没有特定的含义，它是可用于组合其他 HTML 元素的容器.如果与 CSS 一同使用，`<div>` 元素可用于对大的内容块设置样式属性.`<div>` 元素的另一个常见的用途是文档布局。

2. HTML内联元素(inline element)

   内联元素在显示时通常不会以新行开始， 如：`<b>, <td>, <a>, <img>`

   `<span>`元素属于典型的内联元素，该元素没有特定的含义，它是可用于文本的容器.如果与 CSS 一同使用，`<span>` 元素可用于对部分文本设置样式属性.

### HTML属性  

HTML <font color=Red>标签</font>可以拥有*属性*(<font color=green>因此属性是在尖括号内</font>)。属性提供了<u>有关 HTML 元素</u>的*更多的信息*。常见属性如下：

1. class  

   规定元素的类名

2. id  

   规定元素的唯一id

3. style

   规定元素的行内样式(inline style)

4. title

   规定元素的额外信息

详细标准属性信息参考： [标准属性参考手册](<https://www.w3school.com.cn/tags/html_ref_standardattributes.asp>)

### HTML样式  

style属性的作用是：<font color=Red>提供了一种改变所有HTML元素的样式的通用方法</font>，样式是 HTML 4 引入的，它是一种新的首选的改变 HTML 元素样式的方式。通过 HTML 样式，能够通过使用 style 属性直接将样式添加到 HTML 元素，或者间接地在独立的样式表中（CSS 文件）进行定义。三种方法使用样式表：

1. 外部样式表  

   当样式需要被应用到<u>很多页面</u>的时候，外部样式表将是理想的选择。使用外部样式表，你就可以通过更改一个文件来改变整个站点的外观

   ```html
   <head>
   <link rel="stylesheet" type="text/css" href="mystyle.css">
   </head>
   ```

2. 内部样式表  

   <u>单个文件</u>需要特别样式时，就可以使用内部样式表。你可以在` head `部分通过 `<style>` 标签定义内部样式表

   ```html
   <head>
   
   <style type="text/css">
   body {background-color: red}
   p {margin-left: 20px}
   </style>
   </head>
   ```

3. 内联样式  

   当特殊的样式需要应用到<u>个别元素</u>时，就可以使用内联样式。 使用内联样式的方法是在<u>相关的标签中使用样式属性</u>。样式属性可以包含任何 CSS 属性。以下实例显示出如何改变段落的颜色和左外边距：

   ```html
   <p style="color: red; margin-left: 20px">
   This is a paragraph
   </p>
   ```

### HTML类  

对 HTML 进行分类（设置类），使我们能够为元素的类定义 CSS 样式。为相同的类设置相同的样式，或者为不同的类设置不同的样式。

1. 分类块级元素

   设置` <div>` 元素的类，使我们能够为相同的`<div>`元素设置相同的类  

   ```html
   <!DOCTYPE html>
   <html>
   <head>
   <style>
   .cities {
       background-color:black;
       color:white;
       margin:20px;
       padding:20px;
   } 
   </style>
   </head>
   
   <body>
   
   <div class="cities">
   <h2>London</h2>
   <p>London is the capital city of England. 
   It is the most populous city in the United Kingdom, 
   with a metropolitan area of over 13 million inhabitants.</p>
   </div>
   
   <div class="cities">
   <h2>Paris</h2>
   <p>Paris is the capital and most populous city of France.</p>
   </div>
   
   <div class="cities">
   <h2>Tokyo</h2>
   <p>Tokyo is the capital of Japan, the center of the Greater Tokyo Area,
   and the most populous metropolitan area in the world.</p>
   </div>
   
   </body>
   </html>
   ```

2. 分类行内元素  

   设置`<span> `元素的类，能够为相同的`<span>`元素设置相同的样式

   ```html
   <!DOCTYPE html>
   <html>
   <head>
   <style>
     span.red {color:red;}
   </style>
   </head>
   <body>
   
   <h1>My <span class="red">Important</span> Heading</h1>
   
   </body>
   </html>
   ```


### HTML脚本  

`<script>`标签用于定义客户端脚本，比如 JavaScript。 script 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。必需的 type 属性规定脚本的 MIME 类型。JavaScript 最常用于图片操作、表单验证以及内容动态更新。

```html
<script type="text/javascript">
document.write("Hello World!")
</script>
```

### HTML文档类型  

1. `<!DOCTYPE>`声明

   Web 世界中存在许多不同的文档。只有了解文档的类型，浏览器才能正确地显示文档。HTML 也有多个不同的版本，只有完全明白页面中使用的确切 HTML 版本，浏览器才能完全正确地显示出 HTML 页面。这就是`<!DOCTYPE>`的用处。

   `<!DOCTYPE>`不是 HTML 标签。它为浏览器提供一项信息（声明），即 HTML 是用什么版本编写的。

### HTML实体  

在 HTML 中，某些字符是预留的。例如在 HTML 中不能使用小于号（<）和大于号（>），这是因为浏览器会误认为它们是标签。如果希望正确地显示预留字符，我们必须在 HTML 源代码中使用字符实体（character entities）。字符实体书写如下：

```html
&entity_name;
<!-- 或者 -->
&#entity_number;
<!-- 例如小于号 -->
&lt;
&#69;
```

所有实体符号参考： [实体符号参考手册](<https://www.w3school.com.cn/tags/html_ref_entities.html>)