
Table of Contents
=================

   * [Node JS](#node-js)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [关键词](#关键词)
      * [回调函数](#回调函数)
      * [同步/异步，阻塞/非阻塞](#同步异步阻塞非阻塞)
      * [Web应用架构](#web应用架构)
      * [事件创建与触发](#事件创建与触发)
      * [模块](#模块)
      * [基本模块](#基本模块)
         * [fs](#fs)
         * [stream](#stream)
         * [http](#http)

Created by ALTA
# Node JS  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [彻底理解JS中的回调函数](https://blog.csdn.net/rockage/article/details/79513450)

## 关键词  

-  事件驱动  
- 非阻塞IO  
- 事件循环  
- 回调函数([NodeJs中的回调函数](https://blog.csdn.net/mimikuer/article/details/78871187))

## 回调函数  

回调函数，就是放在另外一个函数（如 parent）的参数列表中，作为参数传递给这个 parent，然后在 parent 函数体的某个位置执行。如下代码，首先定义一个f1 函数，它有一个参数 callback，这个 callback 就是回调函数，名字可以任意取。在函数体中，定义了三个变量 a,b,c。然后调用 callback 函数，最后返回一个值。这里我们并不知道callback这个回调函数是干什么的，因为没有定义它的功能，它只是有三个参数。然后调用f1 函数，这时候我们就需要指定 callback 具体要实现什么了，可以看到，它完成了一个 求和的功能。**定义的时候只定义形参，调用的时候定义函数功能**   

```javascript
var f1 = function(callback)
{
    var a = 1,
        b = 2,
        c = 3;
    var s = callback(a,b,c);
    return s;
};
var d = f1(function(x,y,z){
    return (x+y+z);
});
console.log(d);
```

再比如，使用ejs模板，完成一个上传图片与查看相册的功能，我们可能这样做：

首先定义一个函数完成获取相册文件夹的功能：

```javascript
function getAllAlbums(){
    //这里具体实现功能，最后返回一个文件夹数组
    fs.readdir(...)
}
```

然后定义渲染函数，调用刚刚的获取文件夹函数，将结果进行渲染：

```javascript
var albums = function(req,res,next){
    res.render("index",{
        "albums" : getAllAlbums()
    });
}
```

但是，这个做法是错误的，因为这是传统的思维！当你要获取所有的文件夹时，就要涉及到读文件，fs.readdir()，而这肯定是异步的！因此可能你的文件还没读完，页面就已经被渲染了，这时就会报错。所以，正确的做法是，在getAllAlbums中使用callback回调函数，而在调用getAllAlbums时，把读完文件后的 数据 当做回调函数的参数来使用：

```javascript
function getAllAlbums(callback){

    fs.readdir("./uploads",function(err,files){
        var allAlbums = [];
        ...
        callback(allAlbums);
    }

}
var albums = function(req,res,next){

    getAllAlbums(function(err,allAlbums){
        res.render("index",{
            "albums" : allAlbums
        });
    })

}
```



## 同步/异步，阻塞/非阻塞  

- 同步/异步：同步和异步关注的是**消息通信机制** (synchronous communication/ asynchronous communication)
  所谓同步，就是在发出一个*调用*时，在没有得到结果之前，该*调用*就不返回。但是一旦调用返回，就得到返回值了。
  而异步则是相反，*调用*在发出之后，这个调用就直接返回了，所以没有返回结果。换句话说，当一个异步过程调用发出后，调用者不会立刻得到结果。而是在*调用*发出后，*被调用者*通过状态、通知来通知调用者，或通过回调函数处理这个调用。

- 阻塞/非阻塞：阻塞和非阻塞关注的是**程序在等待调用结果（消息，返回值）时的状态.**
  阻塞调用是指调用结果返回之前，当前线程会被挂起。调用线程只有在得到结果之后才会返回。
  非阻塞调用指在不能立刻得到结果之前，该调用不会阻塞当前线程。

## Web服务器  

Web服务器一般指网站服务器，是指驻留于因特网上某种类型计算机的程序，Web服务器的基本功能就是提供Web信息浏览服务。它只需支持HTTP协议、HTML文档格式及URL，与客户端的网络浏览器配合。大多数 web 服务器都支持服务端的脚本语言（php、python、ruby）等，并通过脚本语言从数据库获取数据，将结果返回给客户端浏览器。目前最主流的三个Web服务器是Apache、Nginx、IIS。

## Web应用架构

![Web应用架构](https://blackholemedia.github.io/documents/statics/web_architecture.jpg)  

- **Client** - 客户端，一般指浏览器，浏览器可以通过 HTTP 协议向服务器请求数据  

- **Server** - 服务端，一般指 Web 服务器，可以接收客户端请求，并向客户端发送响应数据(node服务器)  

- **Business** - 业务层， 通过 Web 服务器处理应用程序，如与数据库交互，逻辑运算，调用外部程序等(node.js 脚本)

  Node.js 提供了 http 模块，http 模块主要用于搭建 HTTP 服务端和客户端，使用 HTTP 服务器或客户端功能必须调用 http 模块  

- **Data** - 数据层，一般由数据库组成  

## 事件创建与触发  

创建事件处理程序 ——> on绑定事件处理程序 ——> emit触发事件处理程序

## 模块  

hello.js如下，模块名即为：hello

```javascript
'use strict';

var s = 'Hello';

function greet(name) {
    console.log(s + ', ' + name + '!');
}

function hello() {
    console.log('Hello, world!');
}

module.exports = greet;  //函数暴露，使得导入模块的时候可以直接调用
//或者输出多个对象
module.exports = {
    hello: hello,
    greet: greet
};
```

模块导入以及使用  

```javascript
'use strict';

// 引入hello模块:
var greet = require('./hello');

var s = 'Michael';

greet(s); // Hello, Michael!
```

要在模块中对外输出变量，输出的变量可以是任意对象、函数、数组等 ,用：

```javascript
module.exports = variable;
```

要引入其他模块输出的对象，引入的对象具体是什么，取决于引入模块输出的对象。用：

```javascript
var foo = require('other_module');
```

*直接对`module.exports`赋值，可以应对任何情况*：  

```javascript
module.exports = {
    foo: function () { return 'foo'; }
};
```

## 基本模块  

### fs  

1. 异步读文件

   ```javascript
   'use strict';
   
   var fs = require('fs');
   
   fs.readFile('sample.txt', 'utf-8', function (err, data) {
       if (err) {
           console.log(err);
       } else {
           console.log(data);
       }
   });
   ```

   异步读取时，传入的回调函数接收两个参数，当正常读取时，`err`参数为`null`，`data`参数为读取到的String。当读取发生错误时，`err`参数代表一个错误对象，`data`为`undefined`。这也是Node.js标准的回调函数：第一个参数代表错误信息，第二个参数代表结果。

2. 同步读文件  

   ```javascript
   'use strict';
   
   var fs = require('fs');
   
   var data = fs.readFileSync('sample.txt', 'utf-8');
   console.log(data);
   ```

3. 异步写文件  

   ```javascript
   'use strict';
   
   var fs = require('fs');
   
   var data = 'Hello, Node.js';
   fs.writeFile('output.txt', data, function (err) {
       if (err) {
           console.log(err);
       } else {
           console.log('ok.');
       }
   });
   ```

   回调函数只关心写入成功与否，故只有一个err参数

4. 同步写文件  

   类似同步读文件

### stream  

参考 [stream](<https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/001434501515527e6fce6d5ec4b4fd9b572122cd1ec8ded000>)  

### http  

详细参考： [http](https://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000/0014345015296018cac40c198b543fead5c549865b9bd4a000)  

1. HTTP服务器

   要开发HTTP服务器程序，从头处理TCP连接，解析HTTP是不现实的。这些工作实际上已经由Node.js自带的http模块完成了。应用程序并不直接和HTTP协议打交道，而是操作http模块提供的request和response对象.   

   `request`对象封装了HTTP请求，我们调用`request`对象的属性和方法就可以拿到所有HTTP请求的信息；*疑问：request对象是如何获得HTTP的请求信息的？*  

   response`对象封装了HTTP响应，我们操作`response`对象的方法，就可以把HTTP响应返回给浏览器  

   ```javascript
    'use strict';
     
     // 导入http模块:
     var http = require('http');
     
     // 创建http server，并传入回调函数:
     var server = http.createServer(function (request, response) {
         // 回调函数接收request和response对象,
         // 获得HTTP请求的method和url:
         console.log(request.method + ': ' + request.url);
         // 将HTTP响应200写入response, 同时设置Content-Type: text/html:
         response.writeHead(200, {'Content-Type': 'text/html'});
         // 将HTTP响应的HTML内容写入response:
         response.end('<h1>Hello world!</h1>');
     });
     
     // 让服务器监听8080端口:
     server.listen(8080);
     console.log('Server is running at http://127.0.0.1:8080/');
   ```

   