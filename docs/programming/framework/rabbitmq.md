
Table of Contents
=================

   * [RabbitMQ](#rabbitmq)
      * [参考引用](#参考引用)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理流程](#基本概念架构与处理流程)
         * [AMQP协议](#amqp协议)
         * [AMQP基本概念](#amqp基本概念)
         * [AMQP处理过程](#amqp处理过程)
         * [RabbitMQ](#rabbitmq-1)
         * [常用交换器](#常用交换器)
      * [安装部署](#安装部署)
      * [原理细节及详细过程](#原理细节及详细过程)
         * [详细过程](#详细过程)
      * [深入的其他议题](#深入的其他议题)
         * [死信队列(DLX)](#死信队列dlx)
         * [消费端ACK与NACK](#消费端ack与nack)
         * [Return消息机制](#return消息机制)
         * [消费端自定义监听(推模式和拉模式pull/push)](#消费端自定义监听推模式和拉模式pullpush)
         * [如何保证幂等性](#如何保证幂等性)
         * [如何保证可靠性](#如何保证可靠性)
         * [消息如何限流](#消息如何限流)
         * [集群设置](#集群设置)

Created by ALTA
# RabbitMQ  
<font color=limegreen>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [RabbitMQ（一）：RabbitMQ快速入门](https://www.cnblogs.com/sgh1023/p/11217017.html)  
2. [RabbitMQ基础概念详细介绍](https://www.cnblogs.com/williamjie/p/9481774.html)  
3. [RabbitMQ](<https://www.jianshu.com/p/78847c203b76>)

## 问题背景  

以电商场景为例，如果商品服务和订单服务是两个不同的微服务，在下单的过程中订单服务需要调用商品服务进行扣库存操作。按照传统的方式，下单过程要等到调用完毕之后才能返回下单成功，如果网络产生波动等原因使得商品服务扣库存延迟或者失败，会带来较差的用户体验，如果在高并发的场景下，这样的处理显然是不合适的，那怎么进行优化呢？这就需要消息队列登场了。

消息队列提供一个异步通信机制，消息的发送者不必一直等待到消息被成功处理才返回，而是立即返回(<font color=Yellow>立即返回什么，假设库存没了，扣库存失败了怎么办？订单服务的结果依赖与商品服务的结果，这可以用异步去处理？</font>)。消息中间件负责处理网络通信，如果网络连接不可用，消息被暂存于队列当中，当网络畅通的时候在将消息转发给相应的应用程序或者服务，当然前提是这些服务订阅了该队列。如果在商品服务和订单服务之间使用消息中间件，既可以提高并发量，又降低服务之间的耦合度。<font color=limegreen>所以消息队列的一个典型应用场景就是异步处理，把消息放入消息中间件中，等到需要的时候再去处理</font>.

除上述场景外，以下场景也适用：

- 流量削峰。例如秒杀活动，在短时间内访问量急剧增加，使用消息队列，当消息队列满了就拒绝响应，跳转到错误页面，这样就可以使得系统不会因为超负载而崩溃  
- 日志处理(<font color=Yellow>找找例子</font>)  
- 应用解耦。假设某个服务A需要给许多个服务（B、C、D）发送消息，当某个服务（例如B）不需要发送消息了，服务A需要改代码再次部署；当新加入一个服务（服务E）需要服务A的消息的时候，也需要改代码重新部署；另外服务A也要考虑其他服务挂掉，没有收到消息怎么办？要不要重新发送呢？是不是很麻烦，使用MQ发布订阅模式，服务A只生产消息发送到MQ，B、C、D从MQ中读取消息，需要A的消息就订阅，不需要了就取消订阅，服务A不再操心其他的事情，使用这种方式可以降低服务或者系统之间的耦合  

## 基本概念、架构与处理流程  

### AMQP协议  

高级消息队列协议 Advanced Message Queue Protocol，是应用层协议的一个开放标准，为面向消息的[中间件](http://www.diggerplus.org/archives/tag/中间件)设计。消息中间件主要用于组件之间的解耦，消息的发送者无需知道消息使用者的存在，反之亦然。<font color=red>RabbitMQ是一个开源的AMQP实现，服务器端用Erlang语言编写，支持多种客户端</font>  

### AMQP基本概念  

- Server(broker)：接收客户端的连接，实现AMQP实体服务。
- Connection：连接，应用程序与Server的网络连接，TCP连接。
- Channel：信道，消息读写等操作在信道中进行。客户端可以建立多个信道，每个信道代表一个会话任务。
- Message：消息，应用程序和服务器之间传送的数据，消息可以非常简单，也可以很复杂。有Properties和Body组成。Properties为外包装，可以对消息进行修饰，比如消息的优先级、延迟等高级特性；Body就是消息体内容。
- Virtual Host：虚拟主机，用于逻辑隔离，类似于权限控制组，权限控制的最小粒度。一个虚拟主机里面可以有若干个Exchange和Queue，同一个虚拟主机里面不能有相同名称的Exchange或Queue。(为什么需要多个虚拟主机呢？很简单，RabbitMQ当中，用户只能在虚拟主机的粒度进行权限控制。因此，如果需要禁止A组访问B组的交换机/队列/绑定，必须为A和B分别创 建一个虚拟主机。每一个RabbitMQ服务器都有一个默认的虚拟主机`/`。)
- Exchange：交换器，接收消息，按照路由规则将消息路由到一个或者多个队列。如果路由不到，或者返回给生产者，或者直接丢弃。RabbitMQ常用的交换器常用类型有direct、topic、fanout、headers四种，后面详细介绍。
- Binding：绑定，交换器和消息队列之间的虚拟连接，绑定中可以包含一个或者多个BindingKey(<font color=Yellow>为什么要有Binding，有RoutingKey不就足够了吗？</font><font color=limegreen>个人理解是：Binding相当于修路， BindingKey相当于修好的路名，消费者将消息发送给Exchange时，一般会指定一个routing key；当binding key与routing key相匹配时(消息要去的路和修好的路名一致)，消息将会被路由到对应的Queue中; 通常Exchange Type与binding key固定（在正常使用时一般这些内容都是固定配置好的），正如平常路名通常不怎么频繁变更</font>)。
- BindingKey: 在绑定多个Queue到同一个Exchange的时候，这些Binding允许使用相同的binding key(<font color=limegreen>意思是同一个消息分发到不同的队列</font>)。
- RoutingKey：路由键，生产者将消息发送给交换器的时候，会发送一个RoutingKey，用来指定路由规则，这样交换器就知道把消息发送到哪个队列。路由键通常为一个“.”分割的字符串，例如“com.rabbitmq”。
- Queue：消息队列，用来保存消息，供消费者消费。

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/amqp.png" width="400px"> </div><br>

*我们完全可以直接使用 Connection 就能完成信道的工作，为什么还要引入信道呢?试想这样一个场景， 一个应用程序中有很多个线程需要从 RabbitMQ 中消费消息，或者生产消息，那么必然需要建立很多个 Connection，也就是许多个 TCP 连接。然而对于操作系统而言，建立和销毁 TCP 连接是非常昂贵的开销，而且TCP的连接数也有限制，这也限制了系统处理高并发的能力。但是，在TCP连接中建立Channel是没有上述代价的。 RabbitMQ 采用 TCP 连接复用的方式，不仅可以减少性能开销，同时也便于管理*

### AMQP处理过程  

生产者是投递消息的一方，首先连接到Server，建立一个连接，开启一个信道；然后生产者声明交换器和队列，设置相关属性，并通过路由键将交换器和队列进行绑定。同理，消费者也需要进行建立连接，开启信道等操作，便于接收消息。

接着生产者就可以发送消息，发送到服务端中的虚拟主机，虚拟主机中的交换器根据路由键选择路由规则，然后发送到不同的消息队列中，这样订阅了消息队列的消费者就可以获取到消息，进行消费。

最后还要关闭信道和连接。详细过程参考[原理及详细过程](#原理及详细过程)

### RabbitMQ  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/rabbitmq.jpg" width="400px"> </div><br>

### 常用交换器  

RabbitMQ主要包含四种交换器类型(direct、topic、fanout、headers)， 这么多类型是为了灵活地分发消息到队列(比如topic可以用于模糊匹配，Exchange将RoutingKey和某Topic进行模糊匹配，其中`*`用来匹配一个词，`#`用于匹配一个或者多个词。例如`com.#`能匹配到`com.rabbitmq.oa`和`com.rabbitmq`)，更多细节参考引用。

## 安装部署  

参考搜索引擎  

## 原理细节及详细过程  

### 详细过程  

1. 声明MessageQueue  

   在Rabbit MQ中，无论是生产者发送消息还是消费者接受消息，都首先需要声明一个MessageQueue(<font color=Yellow>也就是生产者需要知道往哪儿发消息，消费者需要知道从哪儿收消息</font>)。这就存在一个问题，是生产者声明还是消费者声明呢？要解决这个问题，首先需要明确:

   - 消费者是无法订阅或者获取不存在的MessageQueue中信息。  
   - 消息被Exchange接受以后，如果没有匹配的Queue，则会被丢弃  

   在明白了上述两点以后，就容易理解如果是消费者去声明Queue，就有可能会出现在声明Queue之前，生产者已发送的消息被丢弃的隐患。如果应用能够通过消息重发的机制允许消息丢失，则使用此方案没有任何问题。但是如果不能接受该方案，这就需要无论是生产者还是消费者，在发送或者接受消息前，都需要去尝试建立消息队列。这里有一点需要明确，如果客户端尝试建立一个已经存在的消息队列，Rabbit MQ不会做任何事情，并返回客户端建立成功的  

   <font color=limegreen>也就是分情况： A. 如果应用有消息重发机制，可以是消费者去声明Queue; B. 生产者和消费者都去声明，看谁先建立声明成功(因为成功建立之后后者的请求不会再建立，只返回建立成功)</font>

2. 生产者发送消息  

   ExchangeType和Binding(<font color=limegreen>BildingKey</font>)决定了消息的路由规则。所以生产者想要发送消息，首先必须要声明一个Exchange和该Exchange对应的Binding。可以通过 ExchangeDeclare和BindingDeclare完成。  

   在Rabbit MQ中，声明一个Exchange需要三个参数：ExchangeName，ExchangeType和Durable。  

   - ExchangeName是该Exchange的名字，该属性在创建Binding和生产者通过publish推送消息时需要指定。  
   - ExchangeType，指Exchange的类型，在RabbitMQ中，有四种类型的Exchange：direct ，fanout和，topic， headers，不同的Exchange会表现出不同路由行为。
   - Durable是该Exchange的持久化属性，参考第4点持久化。

   声明一个Binding需要提供一个QueueName，ExchangeName和BindingKey

3. 消费者接受消息  

   在RabbitMQ中消费者有2种方式获取队列中的消息:

   - 订阅，通过basic.consume命令，订阅某一个队列中的消息,channel会自动在处理完上一条消息之后，接收下一条消息。（同一个channel消息处理是串行的）。除非关闭channel或者取消订阅，否则客户端将会一直接收队列的消息。  
   - 单条获取，通过basic.get命令主动获取队列中的消息，但是<font color=Red>绝对不可以通过循环调用basic.get来代替basic.consume</font>，这是因为basic.get RabbitMQ在实际执行的时候，是首先consume某一个队列，然后检索第一条消息，然后再取消订阅。如果是高吞吐率的消费者，最好还是建议使用basic.consume

   如果有多个消费者同时订阅同一个队列的话，RabbitMQ是采用循环的方式分发消息的，每一条消息只能被一个订阅者接收。例如，有队列Queue，其中ClientA和ClientB都Consume了该队列，MessageA到达队列后，被分派到ClientA，<font color=red>ClientA回复服务器收到响应，服务器删除MessageA</font>；再有一条消息MessageB抵达队列，服务器根据“循环推送”原则，将消息会发给ClientB，然后收到ClientB的确认后，删除MessageB；等到再下一条消息时，服务器会再将消息发送给ClientA.  

   消费者在接到消息以后，都需要给服务器发送一条确认命令，这个即可以在handleDelivery里显式的调用basic.ack实现，也可以在Consume某个队列的时候，设置autoACK属性为true实现。<u>这个ACK仅仅是通知服务器可以安全的删除该消息，而不是通知生产者，与RPC不同。 如果消费者在接到消息以后还没来得及返回ACK就断开了连接，消息服务器会重传该消息给下一个订阅者，如果没有订阅者就会存储该消息</u>  

   既然RabbitMQ提供了ACK某一个消息的命令，当然也提供了Reject某一个消息的命令。当客户端发生错误，调用basic.reject命令拒绝某一个消息时，可以设置一个requeue的属性，如果为true，则消息服务器会重传该消息给下一个订阅者；如果为false，则会直接删除该消息。当然，也可以通过ack，让消息服务器直接删除该消息并且不会重传(<font color=limegreen>A; 被动拒绝，如上文的没来得及返回ACK——重传消息给下一订阅者；B. 主动拒绝，主动告诉消息服务器是重传给下一订阅者还是直接删除消息</font>)  

4. 持久化  

   Rabbit MQ默认是不持久队列、Exchange、Binding以及队列中的消息的，这意味着一旦消息服务器重启，所有已声明的队列，Exchange，Binding以及队列中的消息都会丢失。通过设置Exchange和MessageQueue的durable属性为true，可以使得<font color=red>队列和Exchange持久化，但是这还不能使得队列中的消息持久化</font>，这需要生产者在发送消息的时候，将delivery mode设置为2，只有这3个全部设置完成后，才能保证服务器重启不会对现有的队列造成影响。这里需要注意的是，只有durable为true的Exchange和durable为ture的Queues才能绑定，否则在绑定时，RabbitMQ都会抛错的。持久化会对RabbitMQ的性能造成比较大的影响，可能会下降10倍不止

5. 事务  

    对事务的支持是AMQP协议的一个重要特性。假设当生产者将一个持久化消息发送给服务器时，因为consume命令本身没有任何Response返回，所以即使服务器崩溃，没有持久化该消息，生产者也无法获知该消息已经丢失。如果此时使用事务，即通过txSelect()开启一个事务，然后发送消息给服务器，然后通过txCommit()提交该事务，即可以保证，如果txCommit()提交了，则该消息一定会持久化，如果txCommit()还未提交即服务器崩溃，则该消息不会服务器就收。当然Rabbit MQ也提供了txRollback()命令用于回滚某一个事务(<font color=limegreen>也就是当持久化的时候，生产者无法知道持久化是否成功，因为</font><font color=Yellow>消息发送到服务器，服务器不返回确认结果，而消费者consume也不返回确认结果，如果返回了其实就知道了消息发到了服务器上，不知道是不是这样理解</font>)

6. confirm机制(<font color=Yellow>这部分原样copy没看没整理</font>)  

   使用事务固然可以保证只有提交的事务，才会被服务器执行。但是这样同时也将客户端与消息服务器同步起来，这背离了消息队列解耦的本质。Rabbit MQ提供了一个更加轻量级的机制来保证生产者可以感知服务器消息是否已被路由到正确的队列中——Confirm。如果设置channel为confirm状态，则通过该channel发送的消息都会被分配一个唯一的ID，然后一旦该消息被正确的路由到匹配的队列中后，服务器会返回给生产者一个Confirm，该Confirm包含该消息的ID，这样生产者就会知道该消息已被正确分发。对于持久化消息，只有该消息被持久化后，才会返回Confirm。Confirm机制的最大优点在于异步，生产者在发送消息以后，即可继续执行其他任务。而服务器返回Confirm后，会触发生产者的回调函数，生产者在回调函数中处理Confirm信息。如果消息服务器发生异常，导致该消息丢失，会返回给生产者一个nack，表示消息已经丢失，这样生产者就可以通过重发消息，保证消息不丢失。Confirm机制在性能上要比事务优越很多。但是Confirm机制，无法进行回滚，就是一旦服务器崩溃，生产者无法得到Confirm信息，生产者其实本身也不知道该消息吃否已经被持久化，只有继续重发来保证消息不丢失，但是如果原先已经持久化的消息，并不会被回滚，这样队列中就会存在两条相同的消息，系统需要支持去重

7. 消息队列使用过程概括如下：

   - 客户端连接到消息队列服务器，打开一个channel  
   - 客户端声明一个exchange，并设置相关属性  
   - 客户端声明一个queue，并设置相关属性  
   - 客户端使用routing key，在exchange和queue之间建立好绑定关系  
   - 客户端投递消息到exchange  
   - 客户端消费消息

## 深入的其他议题  

### 死信队列(DLX)  

left blank  

### 消费端ACK与NACK

left blank  

### Return消息机制  

left blank  

### 消费端自定义监听(推模式和拉模式pull/push)

left blank  

### 如何保证幂等性  

left blank  

### 如何保证可靠性  

left blank  

### 消息如何限流  

left blank  

### 集群设置  

left blank