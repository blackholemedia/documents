
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# Celery  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. 111111

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

## 定义  

> Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.
>
> The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, [Eventlet](http://eventlet.net/), or [gevent](http://gevent.org/). Tasks can execute asynchronously (in the background) or synchronously (wait until ready).

Celery 是一个简单、灵活且可靠的，处理大量消息的**分布式系统**(<font color=Yellow>什么是分布式系统？master-slave?</font>)，并且提供维护这样一个系统的必需工具。

它是一个专注于实时处理的**任务队列**，同时也支持任务调度(<font color=green>分布式系统＋任务队列</font>)

## 架构  

Celery的架构由三部分组成，***消息中间件***（message broker），**任务执行单元**（worker）和***任务执行结果存储***（task result store）组成。  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/celery.png" width="400px"> </div><br>

### broker  

*Celery本身不提供消息服务*，但是可以方便的和第三方提供的消息中间件集成。包括，RabbitMQ, [Redis](http://lib.csdn.net/base/redis), [MongoDB](http://lib.csdn.net/base/mongodb) (experimental), Amazon SQS (experimental),CouchDB (experimental), SQLAlchemy (experimental),Django ORM (experimental), IronMQ  

### worker  

Worker是Celery提供的任务执行的单元，worker并发的运行在分布式的系统节点中  

### backend  

通常程序发送的消息，发完就完了，可能都不知道对方时候接受了。为此，celery实现了一个backend，用于存储这些消息以及celery执行的一些消息和结果。Backend是在Celery的配置中的一个配置项 CELERY_RESULT_BACKEND ，作用是保存结果和状态，如果你需要跟踪任务的状态，那么需要设置这一项，可以是Database backend，也可以是Cache backend，具体可以参考这里： [CELERY_RESULT_BACKEND](http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend) 。

## 使用  



### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 