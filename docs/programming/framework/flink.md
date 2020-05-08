
Table of Contents
=================

   * [Flink](#flink)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [问题背景](#问题背景)
      * [如何使用Flink](#如何使用flink)
         * [Flink基本架构](#flink基本架构)
         * [核心原理](#核心原理)

Created by ALTA
# Flink  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [为什么选择Flink](<https://www.jianshu.com/p/442521ddc28f>)

## 问题背景  

- 数据是无穷的  
- 数据是连续不断的，因此我们不可能等到所有数据都到了才开始处理  
- 连续不断的数据流处理，如果时间线中间某些数据处理出错怎么办？  
- 先产生的数据不一定先到，后产生的数据也不一定后到，也就是数据不一定是有序的，这样的数据该如何处理

Flink用于解决包括但不限于上述的问题

## 如何使用Flink  

### Flink基本架构  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/flink_structure.png" width="400px"> </div><br>

 用于工作的叫做 TaskManager（又叫：Worker）。TaskManager 里面以后运行着Task（又叫：subTask）。TaskSlot 中就会运行着真正计算的任务 Task。  

TaskManager 相当于用来给 Task 提供执行环境。JobManager相当于是主节点，TaskManager相当于是从节点。JobManager用来负责管理，TaskManager用来负责执行具体的Task，他们之间也要通过网络进行RPC通信。RPC通信，底层使用的是Akka。 我们还会用到一个客户端。这个客户端用来提交任务(左图中的Client)。  

客户端提交任务，首先会与 JobManager 进行通信。我们在本地写程序。程序中会构建成一个类似于 Spark 的 DAG(Flink 中叫做Dataflow graph)，将 Dataflow graph 提交到 JobManager。JobManager 会把这个Dataflow graph 切分成多个 Task。将 Task 调度到TaskManager中进行执行。(和Spark很相似)

### 核心原理  

Flink依赖以下4个机制解决背景中的问题：Window，Time，Checkpoint，State

1. Window  

   观察窗，将无限流切分成有限流，是处理有限流的核心组件，可以是时间驱动的（Time Window），也可以是数据驱动的（Count Window）<font color=yellow>参考流体的表述</font>

2. Time  

   Event-Time ：事件时间是每个事件在其生产设备上发生的时间。此时间通常在进入Flink之前嵌入记录中，并且 可以从每个记录中提取该事件时间戳

   Ingestion-Time ：摄取时间是事件进入Flink的时间。在源算子处，每个记录将源的当前时间作为时间戳，并且基于时间的 算子操作（如时间窗口）引用该时间戳  

   Processing-Time ： 处理时间是指执行相应算子操作的机器的系统时间  

   