
Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [RPC](#rpc)
      * [参考引用](#参考引用)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理过程](#基本概念架构与处理过程)
         * [RPC过程](#rpc过程)

Created by ALTA

# RPC  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [如何给老婆解释什么是RPC](<https://www.jianshu.com/p/2accc2840a1b>)  
2. [如何实现一个简单的RPC](<https://www.jianshu.com/p/5b90a4e70783>)  
3. [什么是RPC?](<https://www.jianshu.com/p/7d6853140e13>)  
4. [花了一个星期，我终于把RPC框架整明白了](<https://developer.51cto.com/art/201906/597963.htm>)

## 问题背景  

> RPC: Remote Procedure Call

**分布式**是促使RPC诞生的领域。

假设你有一个计算器接口，Calculator，以及它的实现类CalculatorImpl，那么在系统还是**单体应用**时，你要调用Calculator的add方法来执行一个加运算，直接new一个CalculatorImpl，然后调用add方法就行了，这其实就是非常普通的**本地函数调用**，因为在**同一个地址空间**，或者说在同一块内存，所以通过方法栈和参数栈就可以实现，当改造成分布式应用的时候，将很多可以共享的功能都单独拎出来，比如上面说到的计算器，你单独把它放到一个服务里头，让别的服务去调用它。<u>这下问题来了，服务A里头并没有CalculatorImpl这个类，那它要怎样调用服务B的CalculatorImpl的add方法呢</u>？<font color=limegreen>简单来说就是A服务想要执行B服务的某些方法</font>  

很自然我们想到以下解决方法：  

- 采用类B/S架构，B服务暴露一个Restful接口，代价是：每次调用时，是不是都需要写一串发起http请求的代码呢？比如httpClient.sendRequest...之类  
- 代理模式(<font color=Yellow>文章给的例子还没看懂</font>)

综上，RPC解决以下两个问题：  

- 分布式系统中，服务之间的调用问题  
- 远程调用时，要能够像本地调用一样方便，让调用者感知不到远程调用的逻辑

## 基本概念、架构与处理过程  

### RPC过程  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/rpc_procedure.png" width="400px"> </div><br>

