
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# 长连接和心跳保活机制  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [谈谈长连接和心跳保活机制](https://www.jianshu.com/p/46196c96dc0b)
2. [手把手教你实现 自适应的心跳保活机制](<https://blog.csdn.net/carson_ho/article/details/79522975>)

### 

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/417bc315-4409-48c6-83e0-59e8d405429e.jpg" width="400px"> </div><br>

Content 

数学公式
$$
f'(t)=\lim_{\Delta t \to 0}\frac{f(t + \Delta t)-f(t)}{\Delta t}
$$

1. Number-prefix class  

   Content 

   - Symbol-prefix class 

     Content 

## 简介  

通信双方进行TCP链接后进行通信，结束后不主动关闭链接
优点：通信速度快，免去了DNS解析时间，以及三次握手四次分手的时间，避免短时间内重复连接所造成的信道资源 & 网络资源的浪费

### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 