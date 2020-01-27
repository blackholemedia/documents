
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# 自然常数  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [自然常数e](<https://zhuanlan.zhihu.com/p/40317763>)

### 

Content 

1. Number-prefix class  

   Content 

   - Symbol-prefix class 

     Content 

## 基本概念  

我们一般把一种自然现象的状态用一个函数表示，而状态的变化用变化率来描述。  

首先明确一下几个概念，这样更有利于后面的分析。<u>状态量是指描述事物当前状态的量</u>，比如某根竹子长5m，某个人体重50Kg。<u>状态量的变化率对应的是导数的概念</u>，是指无穷小时间内状态增量和时间增量的比值。

状态量的变化率：  
$$
f'(t)=\lim_{\Delta t \to 0}\frac{f(t + \Delta t)-f(t)}{\Delta t}
$$
单位状态量的变化率：  
$$
f'(t)=\lim_{\Delta t \to 0}\frac{f(t + \Delta t)-f(t)}{\Delta t}\frac{1}{f(t)}=\frac{f'(t)}{f(t)}
$$
状态量变化率对应的是宏观观念，描述的是整体的变化情况；单位状态变化率对应的是微观观念，描述的的局部变化情况。实际事物的局部变化往往是某种物理规律决定的，与当前系统总的状态是无关的。比如竹子的成长变化，每一处竹子的成长规律都是一样的，和当前竹子总长度是无关的，再比如每一个细胞如何分裂的规律是固定的，和当前有多少细胞也没关系  

## 实例  

下面我们来看一个简单的物理现象：假设一根竹苗是1m，它是连续的生长的，单位增长率为100%/year/m（注意是单位状态量的变化率哦）,请问一年后竹子会长多高?  
$$
{(1+\frac{100\%}{1})}^1=2m
$$
上述解法忽略了竹子是一直在增长的，新长出来的部分也会继续生长，这是一个动态的过程。欧拉给出的解法如下：
$$
f'(t)=\lim_{n \to \infty}{(1+\frac{100\%}{n})}^n
$$


### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 