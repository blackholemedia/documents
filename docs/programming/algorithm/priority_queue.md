
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# Priority Queue  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [优先队列和堆](https://www.cnblogs.com/wmyskxz/p/9301021.html)  
2. [漫画：什么是二叉堆？（修正版）](https://mp.weixin.qq.com/s/cq2EhVtOTzTVpNpLDXfeJg)  
3. [漫画：什么是堆排序？](https://mp.weixin.qq.com/s/8Bid1naBLtEjPoP-R4HkBg)

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

### 优先队列  



### 二叉堆  

二叉堆本质上是一种完全二叉树，最大堆/最小堆任何一个父节点的值，都**大于等于/小于等于**它左右孩子节点的值

## 问题背景  

11

## 基本概念、架构与处理过程  

### second-class title  

1111

### 二叉堆的基本操作  

二叉堆虽然是一颗完全二叉树，但它的存储方式并不是链式存储，而是顺序存储。换句话说，二叉堆的所有节点都存储在数组当中。

1. 插入节点  
   - Symbol-prefix class
2. 删除节点  
   - 111
3. 构建二叉堆  

### 堆排序  

当我们删除一个最大堆的堆顶（并不是完全删除，而是替换到最后面），经过自我调节，第二大的元素就会被交换上来，成为最大堆的新堆顶，只要反复删除堆顶，反复调节二叉堆，所得到的集合就成为了一个有序集合。  

1. 把无序数组构建成二叉堆；  
2. 循环删除堆顶元素，移到集合尾部，调节堆产生新的堆顶.  

来来来

