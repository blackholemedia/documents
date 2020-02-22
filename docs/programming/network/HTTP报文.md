
Table of Contents
=================

   * [HTTP报文](#http报文)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [报文组成格式](#报文组成格式)
         * [起始行](#起始行)
         * [头部字段](#头部字段)
         * [非 HTTP 1.1 首部字段](#非-http-11-首部字段)

Created by ALTA
# HTTP报文  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站：

1. [一文带你了解 HTTP 黑科技](<https://juejin.im/post/5e339754e51d451ca967775b>)  
2. [看完这篇HTTP，跟面试官扯皮就没问题了](<https://juejin.im/post/5e1870736fb9a02fef3a5dcb#heading-30>)


## 报文组成格式  

- 起始行（start line）  

  描述请求或响应的基本信息  

- 头部字段（header）  

  使用 key-value 形式更详细地说明报文  

- 消息正文（entity）  

  实际传输的数据，它不一定是纯文本，可以是图片、视频等二进制数据。

其中**起始行和头部字段并成为 `请求头` 或者 `响应头`，统称为 `Header`**；消息正文也叫做实体，称为 `body`。HTTP 协议规定每次发送的报文必须要有 Header，但是可以没有 body，而且在 header 和 body 之间必须要有一个空行（CRLF）  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/header_format.jpg" width="400px"> </div><br>

### 起始行  

每个报文的起始行都是由三个字段组成：**方法、URL 字段和 HTTP 版本字段**。

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/start_line.jpg" width="400px"> </div><br>

1. 请求方法  

   下面是 HTTP1.0 和 HTTP1.1 支持的方法清单

   <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/http_method.jpg" width="400px"> </div><br>

2. 请求URL  

   URL和URI区别参见： URL和URI  

   URL的组成： `协议`+`域名(主机)`+`端口`+`路径`+`查询参数`+`锚点`，以`http://www.example.com:80/path/to/myfile.html?key1=value1&key2=value2#SomewhereInTheDocument`为例：

   - 协议  

     <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/protocol.jpg" width="400px"> </div><br>

   - 主机  

     `www.example.com` 既是一个域名，也代表管理该域名的机构。它指示了需要向网络上的哪一台主机发起请求。当然，也可以直接向主机的IP地址发起请求。

     <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/domain_name.jpg" width="400px"> </div><br>

   - 端口  

   - 路径  

     <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/path.jpg" width="400px"> </div><br>

   - 查询参数  

     <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/parameters.jpg" width="400px"> </div><br>

   - 锚点  

     `#SomewhereInTheDocument` 是资源本身的某一部分的一个锚点。锚点代表资源内的一种“书签”，它给予浏览器显示位于该“加书签”点的内容的指示。 值得注意的是 # 号后面的部分，也称为片段标识符，永远不会与请求一起发送到服务器。

     <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/anchor.jpg" width="400px"> </div><br>

3. HTTP版本  

### 头部字段  

HTTP 的请求标头一般分为四种： `通用标头`、`请求标头`、`响应标头` 和 `实体标头`，还有一类为`内容协商`没有归类  

1. 通用标头  

   可以出现在请求和响应中，主要有三个，分别是 `Date`、`Cache-Control` 和 `Connection`，详细参见引用2

   需要注意的是Cache-Control 的种类比较多，虽然说这是一个通用标头，但是又一些特性是请求标头具有的，有一些是响应标头才有的。其他通用表头参考如下：

   <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/general-header.jpg" width="400px"> </div><br>

2. 请求标头

   <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/request_header.jpg" width="400px"> </div><br>

3. 响应标头  

   以下仅介绍常用的响应标头

   - 响应状态码  

     以 `2xx` 为开头的都表示请求成功响应：

     | **状态码** | **含义**                                                     |
     | ---------- | ------------------------------------------------------------ |
     | 200        | 成功响应                                                     |
     | 204        | 请求处理成功，但是没有资源可以返回                           |
     | 206        | 对资源某一部分进行响应，由Content-Range 指定范围的实体内容。 |

     以 `3xx` 为开头的都表示需要进行附加操作以完成请求  

     | **状态码** | **含义**                                                     |
     | ---------- | ------------------------------------------------------------ |
     | 301        | 永久性重定向，该状态码表示请求的资源已经重新分配 URI，以后应该使用资源现有的 URI |
     | 302        | 临时性重定向。该状态码表示请求的资源已被分配了新的 URI，希望用户（本次）能使用新的 URI 访问。 |
     | 303        | 该状态码表示由于请求对应的资源存在着另一个 URI，应使用 GET 方法定向获取请求的资源。 |
     | 304        | 该状态码表示客户端发送附带条件的请求时，服务器端允许请求访问资源，但未满足条件的情况。 |
     | 307        | 临时重定向。该状态码与 302 Found 有着相同的含义。            |

     以 `4xx` 的响应结果表明客户端是发生错误的原因所在  

     | **状态码** | **含义**                                                     |
     | ---------- | ------------------------------------------------------------ |
     | 400        | 该状态码表示请求报文中存在语法错误。当错误发生时，需修改请求的内容后再次发送请求。 |
     | 401        | 该状态码表示发送的请求需要有通过 HTTP 认证（BASIC 认证、DIGEST 认证）的认证信息。 |
     | 403        | 该状态码表明对请求资源的访问被服务器拒绝了。                 |
     | 404        | 该状态码表明服务器上无法找到请求的资源。                     |

     以 `5xx` 为开头的响应标头都表示服务器本身发生错误  

     | **状态码** | **含义**                                                     |
     | ---------- | ------------------------------------------------------------ |
     | 500        | 该状态码表明服务器端在执行请求时发生了错误。                 |
     | 503        | 该状态码表明服务器暂时处于超负载或正在进行停机维护，现在无法处理请求 |

   - Access-Control-Allow-Origin

     一个返回的 HTTP 标头可能会具有 Access-Control-Allow-Origin ，`Access-Control-Allow-Origin` 指定一个来源，它告诉浏览器允许该来源进行资源访问。 否则-对于没有凭据的请求 `*`通配符，告诉浏览器允许任何源访问资源。例如，要允许源 `https://mozilla.org` 的代码访问资源，可以指定

     ```html
     Access-Control-Allow-Origin: https://mozilla.org
     Vary: Origin
     ```

   - Set-Cookie  

     Cookie 又是另外一个领域的内容了，我们后面文章会说道 Cookie，这里需要记住 Cookie、Set-Cookie 和 Content-Disposition 等在其他 RFC 中定义的首部字段，它们不是属于 HTTP 1.1 的首部字段，但是使用率仍然很高

   其他参考如下：

   <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/response_header.jpg" width="400px"> </div><br>

4. 实体标头  

   实体标头是描述消息正文内容的 HTTP 标头。实体标头用于 HTTP 请求和响应中。头部`Content-Length`、 `Content-Language`、 `Content-Encoding` 是实体头，常见实体标头参考下图：

   <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/body_header.jpg" width="400px"> </div><br>  

5. 内容协商 

   <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/negotiation.jpg" width="400px"> </div><br>

   内容协商机制是指客户端和服务器端就响应的资源内容进行交涉，然后提供给客户端最为适合的资源。内容协商会以响应资源的语言、字符集、编码方式等作为判断的标准。常见内容协商标头如下：

   <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/negotiation_header.jpg" width="400px"> </div><br>

### 非 HTTP 1.1 首部字段  

在 HTTP 协议通信交互中使用到的首部字段，不限于 RFC2616 中定义的 47 种首部字段。还有 Cookie、Set-Cookie 和 Content-Disposition 等在其他 RFC 中定义的首部字段，它们的使用频率也很高。 这些非正式的首部字段统一归纳在 RFC4229 HTTP Header Field Registrations 中
