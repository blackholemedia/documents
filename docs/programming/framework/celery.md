
Table of Contents
=================

   * [Celery](#celery)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [定义](#定义)
         * [任务队列](#任务队列)
         * [原理](#原理)
      * [架构](#架构)
         * [任务模块 Task](#任务模块-task)
         * [broker](#broker)
         * [worker](#worker)
         * [backend](#backend)
      * [使用](#使用)

Created by ALTA
# Celery  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [Python 并行分布式框架 Celery 详解](https://blog.csdn.net/cuomer/article/details/81214438)  
2. [异步任务神器 Celery 快速入门教程](https://blog.csdn.net/chenqiuge1984/article/details/80127446)
3. [celery 原理理解](https://www.cnblogs.com/Tommy-Yu/p/5955294.html)  
4. [Celery基本原理探讨](https://blog.csdn.net/yang00322/article/details/77840637)

## 定义  

> Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.
>
> The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, [Eventlet](http://eventlet.net/), or [gevent](http://gevent.org/). Tasks can execute asynchronously (in the background) or synchronously (wait until ready).

Celery 是一个简单、灵活且可靠的，处理大量消息的**分布式系统**(<font color=Yellow>什么是分布式系统？master-slave?</font>)，并且提供维护这样一个系统的必需工具。

它是一个专注于实时处理的**任务队列**，同时也支持任务调度(<font color=green>分布式系统＋任务队列</font>)

### 任务队列  

>Task queues are used as a mechanism to distribute work across threads or machines.
>
>A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform.
>
>Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker 
>
>— offical document

<font color=Yellow>broker delivers message to worker这一步是如何完成的？broker推送还是worker轮询？</font>  

### 原理  

参考[celery 原理理解](<https://www.cnblogs.com/Tommy-Yu/p/5955294.html>)<font color=Yellow>有时间自己实现一下</font>  

## 架构  

Celery的架构***任务模块***，***消息中间件***（message broker），**任务执行单元**（worker）和***任务执行结果存储***（task result store）组成。  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/celery.png" width="400px"> </div><br>

### 任务模块 Task  

包含异步任务和定时任务。其中，**异步任务通常在业务逻辑中被触发并发往任务队列，而定时任务由 Celery Beat 进程周期性地将任务发往任务队列**

### broker  

*Celery本身不提供消息服务*，但是可以方便的和第三方提供的消息中间件集成。包括，RabbitMQ, [Redis](http://lib.csdn.net/base/redis), [MongoDB](http://lib.csdn.net/base/mongodb) (experimental), Amazon SQS (experimental),CouchDB (experimental), SQLAlchemy (experimental),Django ORM (experimental), IronMQ  

### worker  

Worker是Celery提供的任务执行的单元，worker并发的运行在分布式的系统节点中。**它实时监控消息队列，获取队列中调度的任务，并执行它**<font color=Yellow>(所以是由woker轮询？)</font>  

### backend  

通常程序发送的消息，发完就完了，可能都不知道对方时候接受了。为此，celery实现了一个backend，用于存储这些消息以及celery执行的一些消息和结果。Backend是在Celery的配置中的一个配置项 CELERY_RESULT_BACKEND ，作用是保存结果和状态，如果你需要跟踪任务的状态，那么需要设置这一项，可以是Database backend，也可以是Cache backend(<font color=Yellow>memcached</font>)，具体可以参考这里： [CELERY_RESULT_BACKEND](http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend) 。

## 使用  

