
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# GIL  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [深入理解Python中的GIL（全局解释器锁）。 - 蜗牛学院的文章 ](https://zhuanlan.zhihu.com/p/75780308)  
2. [Python GIL全局解释器锁详解（深度剖析）](<http://c.biancheng.net/view/5537.html>)  

## 定义  

> In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe. (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)  

GIL 是最流行的 CPython 解释器（平常称为 Python）中的一个技术术语，中文译为全局解释器锁，其本质上类似操作系统的 Mutex。GIL 的功能是：在 CPython 解释器中执行的每一个 Python 线程，都会先锁住自己，以阻止别的线程执行

## 问题背景  

GIL的问题其实是由于近十几年来应用程序和操作系统逐步从多任务单核心演进到多任务多核心导致的 , 在一个古老的单核CPU上调度多个线程任务，大家相互共享一个全局锁，谁在CPU执行，谁就占有这把锁，直到这个线程因为IO操作或者Timer Tick到期让出CPU，没有在执行的线程就安静的等待着这把锁  

很明显，在一个现代多核心的处理器上，上面的模型就有很大优化空间了，原来只能等待的线程任务，现在可以在其它空闲的核心上调度并发执行。由于古老GIL机制，如果线程2需要在CPU 2 上执行，它需要先等待在CPU 1 上执行的线程1释放GIL（记住：GIL是全局的）。如果线程1是因为 I/O 阻塞让出的GIL，那么线程2必定拿到GIL。但如果线程1是因为timer ticks计数满100让出GIL，那么这个时候线程1和线程2公平竞争。但要命的是，在Python 2.x, 线程1不会动态的调整自身的优先级，所以很大概率下次被选中执行的还是线程1，在很多个这样的选举周期内，线程2只能安静的看着线程1拿着GIL在CPU 1上欢快的执行  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/gil.jpg" width="400px"> </div><br>



## 基本概念、架构与处理过程  

### GIL底层原理  



### 线程安全  

线程释放GIL的条件：

- 进入IO操作而主动释放了GIL  

  由于线程A的IO操作等待时间不确定，<u>那么等待的线程B一定会得到GIL锁</u>，这种比较“礼貌的”情况我们一般称为“协同式多任务处理”，相当于大家按照协商好的规则来，线程是安全的，不需要额外加锁。

- 解释器不间断执行了1000字节码的指令或不间断运行了15毫秒而放弃了GIL  

  线程A和线程B将同时竞争GIL锁。在同时竞争的情况下，实际上谁会竞争成功是不确定的一个结果，所以一般被称为“抢占式多任务处理”，python3上由于对GIL做了优化，并且会动态调整线程的优先级，所以线程B的优先级会比较高，但仍然无法肯定线程B就一定会拿到GIL。那么在这种情况下，线程可能就会出现不安全的状态。  

