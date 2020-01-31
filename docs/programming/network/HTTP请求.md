
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# HTTP请求  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [一次完整的HTTP请求](https://www.cnblogs.com/engeng/articles/5959335.html)

### 

Content 

1. Number-prefix class  

   Content 

   - Symbol-prefix class 

     Content 

## HTTP请求过程

域名解析 --> 发起TCP的3次握手 --> 建立TCP连接后发起http请求 --> 服务器响应http请求，浏览器得到html代码 --> 浏览器解析html代码，并请求html代码中的资源（如js、css、图片等） --> 浏览器对页面进行渲染呈现给用户  

### 域名解析  

域名解析顺序：浏览器首先搜索浏览器自身的DNS缓存 --> 搜索操作系统自身的DNS缓存 --> 尝试读取hosts文件 --> 浏览器发起一个DNS的系统调用，就会向本地配置的首选DNS服务器(通常为运营商DNS服务器)发起域名解析请求 --> 获得IP地址

### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 