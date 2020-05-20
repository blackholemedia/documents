
Table of Contents
=================

   * [Kafka](#kafka)
      * [参考引用](#参考引用)
      * [定义](#定义)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理过程](#基本概念架构与处理过程)
         * [基本概念](#基本概念)
         * [架构](#架构)
         * [处理过程](#处理过程)
      * [安装部署](#安装部署)
      * [原理及详细过程](#原理及详细过程)
      * [其他细节及问题](#其他细节及问题)

Created by ALTA


<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [为什么使用Kafka](<https://blog.csdn.net/SJF0115/article/details/78480433>)  
2. [Kafka简明教程](<https://zhuanlan.zhihu.com/p/37405836>)  
3. [Kafka学习笔记（一） ：为什么需要Kafka？](<https://segmentfault.com/a/1190000013834998>)

## 定义  

> Apache Kafka® is a *distributed streaming platform*  
>
> A streaming platform has three key capabilities:  
>
> - Publish and subscribe to streams of records, similar to a message queue or enterprise messaging system  
> - Store streams of records in a fault-tolerant durable way  
> - Process streams of records as they occur

## 问题背景  

<font color=limegreen>由定义可知Kafka并不是简单地被定义为消息队列，官方定义Kafka为分布式流平台(*distributed streaming platform*)，消息队列(消息中间件)是其实现的功能之一而不是其全部功能.下述的问题以Kafka作为消息中间件的角色作为背景，既然是消息中间件，那么Kafka就可以处理同类消息中间件处理的问题(参考[RabbitMQ](<https://blackholemedia.github.io/documents/#/programming/framework/rabbitmq>))</font>  

Left blank

除上述问题适用外，Kafka也适用于处理以下问题：

- 日志收集：一个公司可以用Kafka可以收集各种服务的log，通过kafka以统一接口服务的方式开放给各种consumer，例如Hadoop、Hbase、Solr等  
- 解耦： 在项目启动之初来预测将来项目会碰到什么需求，是极其困难的。消息系统在处理过程中间插入了一个隐含的、基于数据的接口层，两边的处理过程都要实现这一接口。这允许你独立的扩展或修改两边的处理过程，只要确保它们遵守同样的接口约束(参考RabbitMQ)  
- 冗余：有些情况下，处理数据的过程会失败。除非数据被持久化，否则将造成丢失。消息队列把数据进行持久化直到它们已经被完全处理，通过这一方式规避了数据丢失风险。许多消息队列所采用的"插入-获取-删除"范式中，在把一个消息从队列中删除之前，需要你的处理系统明确的指出该消息已经被处理完毕，从而确保你的数据被安全的保存直到你使用完毕
- 用户活动跟踪：Kafka经常被用来记录web用户或者app用户的各种活动，如浏览网页、搜索、点击等活动，这些活动信息被各个服务器发布到kafka的topic中，然后订阅者通过订阅这些topic来做实时的监控分析，或者装载到Hadoop、数据仓库中做离线分析和挖掘  
- 运营指标：Kafka也经常用来记录运营监控数据。包括收集各种分布式应用的数据，生产各种操作的集中反馈，比如报警和报告  
- 流式处理：比如spark streaming和storm  
- 限流削峰：在访问量剧增的情况下，应用仍然需要继续发挥作用，但是这样的突发流量并不常见；如果为以能处理这类峰值访问为标准来投入资源随时待命无疑是巨大的浪费。使用消息队列能够使关键组件顶住突发的访问压力，而不会因为突发的超负荷的请求而完全崩溃  
- 异步处理  
- 顺序保证：在大多使用场景下，数据处理的顺序都很重要。大部分消息队列本来就是排序的，并且能保证数据会按照特定的顺序来处理。Kafka保证一个Partition内的消息的有序性  
- 缓冲：在任何重要的系统中，都会有需要不同的处理时间的元素。例如，加载一张图片比应用过滤器花费更少的时间。消息队列通过一个缓冲层来帮助任务最高效率的执行———写入队列的处理会尽可能的快速。该缓冲有助于控制和优化数据流经过系统的速度

## 基本概念、架构与处理过程  

### 基本概念  

- `Broker` ： Kafka消息服务器，消息中心。一个Broker可以容纳多个Topic  
- `Producer` ：消息生产者，就是向Kafka broker发消息的客户端。  
-  `Consumer` ：消息消费者，向Kafka broker取消息的客户端。  
-  `Zookeeper` ：管理Producer，Broker，Consumer的动态加入与离开。  
-  `Topic` ：可以为各种消息划分为多个不同的主题，Topic就是主题名称。Producer可以针对某个主题进行生产，Consumer可以针对某个主题进行订阅。  
-  `Consumer Group`： Kafka采用广播的方式进行消息分发，而Consumer集群在消费某Topic时， Zookeeper会为该集群建立Offset消费偏移量，最新Consumer加入并消费该主题时，可以从最新的Offset点开始消费。  
-  `Partition`：Kafka采用对数据文件切片（Partition）的方式可以将一个Topic可以分布存储到多个Broker上，一个Topic可以分为多个Partition。在多个Consumer并发访问一个partition会有同步锁控制  

### 架构  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/kafka_structure.png" width="400px"> </div><br>

### 处理过程  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/kafka_process.png" width="400px"> </div><br>

## 安装部署  

参考搜索引擎  

## 原理及详细过程  

left blank 

## 其他细节及问题  

Left blank