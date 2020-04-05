
Table of Contents
=================

   * [数据结构](#数据结构)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [数据结构的存储方式](#数据结构的存储方式)
      * [数据结构的基本操作](#数据结构的基本操作)

Created by ALTA
# 数据结构  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [数据结构和算法学习指南](https://mp.weixin.qq.com/s/7rxMytD1EBjqtnmMalrDcw?)

## 数据结构的存储方式  

**数据结构的存储方式只有两种：数组（顺序存储）和链表（链式存储）**  

数组和链表是结构基础。其他多样化的数据结构，究其源头，都是在链表或者数组上的特殊操作，以树为例：用数组实现就是「堆」，因为「堆」是一个完全二叉树，用数组存储不需要节点指针，操作也比较简单；用链表实现就是很常见的那种「树」，因为不一定是完全二叉树，所以不适合用数组存储。为此，在这种链表「树」结构之上，又衍生出各种巧妙的设计，比如二叉搜索树、AVL 树、红黑树、区间树、B 树等  

数组和链表区别如下：

- **数组**由于是紧凑连续存储,可以随机访问，通过索引快速找到对应元素，而且相对节约存储空间。但正因为连续存储，内存空间必须一次性分配够，所以说数组如果要扩容，需要重新分配一块更大的空间，再把数据全部复制过去，时间复杂度 O(N)；而且你如果想在数组中间进行插入和删除，每次必须搬移后面的所有数据以保持连续，时间复杂度 O(N)
- **链表**因为元素不连续，而是靠指针指向下一个元素的位置，所以不存在数组的扩容问题；如果知道某一元素的前驱和后驱，操作指针即可删除该元素或者插入新元素，时间复杂度 O(1)。但是正因为存储空间不连续，你无法根据一个索引算出对应元素的地址，所以不能随机访问；而且由于每个元素必须存储指向前后元素位置的指针，会消耗相对更多的储存空间  

## 数据结构的基本操作  

遍历 + 访问，再具体一点就是：增删查改

**设计不同数据结构的原因是为了在不同的应用场景，尽可能高效地增删查改**