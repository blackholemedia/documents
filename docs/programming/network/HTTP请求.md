
Table of Contents
=================

   * [HTTP请求](#http请求)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [HTTP请求过程](#http请求过程)
         * [域名解析](#域名解析)
         * [TCP 3次握手](#tcp-3次握手)
         * [建立TCP连接后发起http请求](#建立tcp连接后发起http请求)
         * [服务器端响应http请求，浏览器得到html代码](#服务器端响应http请求浏览器得到html代码)
         * [浏览器解析html代码，并请求html代码中的资源](#浏览器解析html代码并请求html代码中的资源)
         * [浏览器对页面进行渲染呈现给用户](#浏览器对页面进行渲染呈现给用户)

Created by ALTA
# HTTP请求  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [一次完整的HTTP请求](https://www.cnblogs.com/engeng/articles/5959335.html)



## HTTP请求过程

<u>域名解析 --> 发起TCP的3次握手 --> 建立TCP连接后发起http请求 --> 服务器响应http请求，浏览器得到html代码 --> 浏览器解析html代码，并请求html代码中的资源（如js、css、图片等） --> 浏览器对页面进行渲染呈现给用户</u>  

### 域名解析  

域名解析顺序：浏览器首先搜索浏览器自身的DNS缓存 --> 搜索操作系统自身的DNS缓存 --> 尝试读取hosts文件 --> 浏览器发起一个DNS的系统调用，就会向本地配置的首选DNS服务器(通常为运营商DNS服务器)发起域名解析请求 --> 获得IP地址

### TCP 3次握手  

拿到域名对应的IP地址之后，User-Agent（一般是指浏览器）会以一个随机端口（1024 < 端口 < 65535）向服务器的WEB程序（常用的有httpd,nginx等）80端口发起TCP的连接请求。这个连接请求（原始的http请求经过TCP/IP4层模型的层层封包）到达服务器端后（这中间通过各种路由设备，局域网内除外），进入到网卡，然后是进入到内核的TCP/IP协议栈（用于识别该连接请求，解封包，一层一层的剥开），还有可能要经过Netfilter防火墙（属于内核的模块）的过滤，最终到达WEB程序（本文就以Nginx为例），最终建立了TCP/IP的连接。过程如下图：

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/tcp3handshake.jpg" width="400px"> </div><br>

1. Client首先发送一个连接试探，ACK=0 表示确认号无效，SYN = 1 表示这是一个连接请求或连接接受报文，同时表示这个数据报不能携带数据，seq = x 表示Client自己的初始序号（seq = 0 就代表这是第0号包），这时候Client进入syn_sent状态，表示客户端等待服务器的回复  
2. Server监听到连接请求报文后，如同意建立连接，则向Client发送确认。TCP报文首部中的SYN 和 ACK都置1 ，ack = x + 1表示期望收到对方下一个报文段的第一个数据字节序号是x+1，同时表明x为止的所有数据都已正确收到（ack=1其实是ack=0+1,也就是期望客户端的第1个包），seq = y 表示Server 自己的初始序号（seq=0就代表这是服务器这边发出的第0号包）。这时服务器进入syn_rcvd，表示服务器已经收到Client的连接请求，等待client的确认  
3. Client收到确认后还需再次发送确认，同时携带要发送给Server的数据。ACK 置1 表示确认号ack= y + 1 有效（代表期望收到服务器的第1个包），Client自己的序号seq= x + 1（表示这就是我的第1个包，相对于第0个包来说的），一旦收到Client的确认之后，这个TCP连接就进入Established状态，就可以发起http请求了  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/tcp3handshake-1.jpg" width="400px"> </div><br>

### 建立TCP连接后发起http请求  

进过TCP3次握手之后，浏览器发起了http的请求，请求参考[HTTP报文](https://blackholemedia.github.io/documents/#/programming/network/HTTP%E6%8A%A5%E6%96%87)  

### 服务器端响应http请求，浏览器得到html代码  

服务器端WEB程序接收到http请求以后，就开始处理该请求，处理之后就返回给浏览器html文件，响应报文参考：[HTTP报文](https://blackholemedia.github.io/documents/#/programming/network/HTTP%E6%8A%A5%E6%96%87)  

**那到底服务器端接收到http请求后是怎么样生成html文件？**  

1. nginx读取配置文件

   Nginx在收到 浏览器 GET / 请求时，会读取http请求里面的头部信息，根据Host来匹配自己的所有的虚拟主机的配置文件的server_name,有匹配那么就读取该虚拟主机的配置，发现如下配置:

   ```nginx
   root /web/echo
   ```

   这个目录就是/，当我们`http://www.linux178.com/`时就是访问这个目录下面的文件。
   
   ```nginx
   index index.html index.htm index.php
   ```
   
   通过这个就能得知网站的首页文件是那个文件，也就是我们进入`http://www.linux178.com/` ，nginx就会自动帮我们把index.html(假设首页是index.php，没找到则报404)加到后面，那么添加之后的URL是`/index.php`，然后根据后面的配置进行处理：
   
   ```nginx
   location ~ .*\.php(\/.*)*$ {
      root /web/echo;
      fastcgi_pass   127.0.0.1:9000;
      fastcgi_index  index.php;
      astcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
      include        fastcgi_params;
   }
   ```
   
   这一段配置指明凡是请求的URL中匹配（这里是启用了正则表达式进行匹配） `*.php`后缀的（后面跟的参数）都交给后端的fastcgi进程进行处理。
   
2. 把php文件交给fastcgi进程去处理  

   nginx把/index.php这个URL交给了后端的fastcgi进程处理，等待fastcgi处理完成后（结合数据库查询出数据，填充模板生成html文件）返回给nginx一个index.html文档，Nginx再把这个index.html返回给浏览器，于是乎浏览器就拿到了首页的html代码，同时nginx写一条访问日志到日志文件中去。


### 浏览器解析html代码，并请求html代码中的资源  

浏览器拿到index.html文件后，就开始解析其中的html代码，遇到js/css/p_w_picpath等静态资源时，就向服务器端去请求下载（会使用多线程下载，每个浏览器的线程数不一样），这个时候就用上keep-alive特性了，建立一次HTTP连接，可以请求多个资源，下载资源的顺序就是按照代码里的顺序，但是由于每个资源大小不一样，而浏览器又多线程请求请求资源，所以从下图看出，这里显示的顺序并不一定是代码里面的顺序。  

浏览器在请求静态资源时（在未过期的情况下），向服务器端发起一个http请求（询问自从上一次修改时间到现在有没有对资源进行修改），如果服务器端返回304状态码（告诉浏览器服务器端没有修改），那么浏览器会直接读取本地的该资源的缓存文件。

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/get_statics_resource.jpg" width="400px"> </div><br>

详细浏览器工作原理参考：[前端必读：浏览器内部工作原理](https://kb.cnblogs.com/page/129756/)

### 浏览器对页面进行渲染呈现给用户  

最后，浏览器利用自己内部的工作机制，把请求到的静态资源和html代码进行渲染，渲染之后呈现给用户。