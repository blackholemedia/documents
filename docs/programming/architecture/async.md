
Table of Contents
=================

   * [Async和Await的理解](#async和await的理解)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [定义](#定义)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理过程](#基本概念架构与处理过程)
         * [asyncwait的使用](#asyncawait的使用)

Created by ALTA
# Async和Await的理解  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [对python async与await的理解](https://www.cnblogs.com/xinghun85/p/9937741.html)  

## 定义  

Left blank

## 问题背景  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/async_in_real_world.png" width="400px"> </div><br>  

## 基本概念、架构与处理过程  

### async\await的使用  

正常的函数在执行时是不会中断的，所以你要写一个能够中断的函数，就需要添加async关键字  

async 用来声明一个函数为异步函数，异步函数的特点是能在函数执行过程中挂起，去执行其他异步函数，等到挂起条件（假设挂起条件是sleep(5)）消失后，也就是5秒到了再回来执行  

await 用来用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，就将此挂起，去执行其他的异步程序。await 后面只能跟异步程序或有__await__属性的对象，因为异步程序与一般程序不同。假设有两个异步函数async a，async b，a中的某一步有await，当程序碰到关键字await b()后，异步程序挂起后去执行另一个异步b程序，就是从函数内部跳出去执行其他函数，**当挂起条件消失后，不管b是否执行完，要马上从b程序中跳出来**，回到原程序执行原来的操作。如果await后面跟的b函数不是异步函数，那么操作就只能等b执行完再返回，无法在b执行的过程中返回。如果要在b执行完才返回，也就不需要用await关键字了，直接调用b函数就行。所以这就需要await后面跟的是异步函数了。在一个异步函数中，可以不止一次挂起，也就是可以用多个await  

```python
 1 async def test2(i):
 2     r = await other_test(i)
 3     print(i,r)
 4 
 5 async def other_test(i):
 6     r = requests.get(i)
 7     print(i)
 8     await asyncio.sleep(4)
 9     print(time.time()-start)
10     return r
11 
12 url = ["https://segmentfault.com/p/1210000013564725",
13        "https://www.jianshu.com/p/83badc8028bd",
14        "https://www.baidu.com/"]
15 
16 loop = asyncio.get_event_loop()
17 task = [asyncio.ensure_future(test2(i)) for i in url]
18 start = time.time()
19 loop.run_until_complete(asyncio.wait(task))
20 endtime = time.time()-start
21 print(endtime)
22 loop.close()
# ---------------------------------- 输出结果
https://segmentfault.com/p/1210000013564725
https://www.jianshu.com/p/83badc8028bd
https://www.baidu.com/
4.425147771835327
https://segmentfault.com/p/1210000013564725 <Response [200]>
4.5975635051727295
https://www.jianshu.com/p/83badc8028bd <Response [403]>
4.722797632217407
https://www.baidu.com/ <Response [200]>
4.722797632217407
```

  对于16~19行可用下图来粗略形容一下：

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/async_code_detail.png" width="400px"> </div><br>

