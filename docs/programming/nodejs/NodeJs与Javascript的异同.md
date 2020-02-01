
Table of Contents
=================

   * [Template](#template)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [异同](#异同)
         * [JavaScript](#javascript)
         * [NodeJS](#nodejs)

Created by ALTA
# Template  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [前端Javascript与Nodejs的异同](https://segmentfault.com/a/1190000006154835)

## 异同  

`JavaScript`=`ECMAScript`+`DOM`+`BOM`  

前端和后端的`js`相同点就是，他们的语言基础都是`ECMAScript`，只是他们所扩展的东西不同，前端需要操作页面元素，于是扩展了`DOM`，也需要操作浏览器，于是就扩展了`BOM`。而服务端的`js`则也是基于`ECMAScript`扩展出了服务端所需要的一些`API`，稍微了解后台的童鞋肯定知道，后台语音有操作系统的能力，于是扩展`os`，需要有操作文件的能力，于是扩展出`file`文件系统、需要操作网络，于是扩展出`net`网络系统，需要操作数据，于是要扩展出`database`的能力。

基础是相同的，只是环境不同，导致他们扩展出来的东西不同而已

### JavaScript  

1. ECMAScript: 语言基础，如：语法、数据类型结构以及一些内置对象;
2. DOM: 一些操作页面元素的方法;
3. BOM: 一些操作浏览器的方法.

### NodeJS  

1. ECMAScript: 语言基础，如：语法、数据类型结构以及一些内置对象;
2. os: 操作系统;
3. file: 文件系统;
4. network: 网络系统;
5. database: 数据库.