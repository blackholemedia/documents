
Table of Contents
=================

   * [Graph](#graph)
      * [参考引用](#参考引用)
      * [定义](#定义)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理过程](#基本概念架构与处理过程)
      * [搜索与遍历](#搜索与遍历)
         * [深度优先](#深度优先)
         * [广度优先](#广度优先)
         * [拓扑排序](#拓扑排序)

Created by ALTA
# Graph  
<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [图论算法](https://blog.csdn.net/u011815404/article/details/80313879)  
2. [图论基础知识、常用算法与LeetCode题解](https://www.paincker.com/graph-theory)  
3. [图论：拓扑排序详解](https://www.cnblogs.com/fusiwei/p/11331916.html) 
4. [有向无环图的拓扑排序](https://www.cnblogs.com/en-heng/p/5085690.html)

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

Left blank

## 问题背景  

11

## 基本概念、架构与处理过程  



## 搜索与遍历  

深度优先和广度优先是图论算法的基础

### 深度优先  

类似树的后序遍历，深度优先遍历的基本过程为：

1. 从图中某个顶点 v0 出发，首先访问 v0
2. 访问结点 v0 的第一个邻接点，以这个邻接点 vt 作为一个新节点，访问 vt 所有邻接点，直到以 vt 出发的所有节点都被访问(<font color=#008000>递归访问：访问vt第一个邻接点，再访问该邻接点的邻接点，不停套娃下去</font>)
3. 回溯到 v0 的下一个未被访问过的邻接点，以这个邻结点为新节点，重复步骤 2，直到图中所有与 v0 相通的所有节点都被访问
4. 若此时图中仍有未被访问的结点，则另选图中的一个未被访问的顶点作为起始点，重复步骤 1，直到图中的所有节点均被访问

### 广度优先  

类似树的先序遍历，广度优先遍历的基本过程为：

1. 从图中某个顶点 v0 出发，首先访问 v0，将 v0 加入队列
2. 将队首元素的未被访问过的邻接点加入队列，访问队首元素并将队首元素出队，直到队列为空
3. 若此时图中仍有未被访问的结点，则另选图中的一个未被访问的顶点作为起始点，重复步骤 1，直到图中的所有节点均被访问过。



### 拓扑排序  

拓扑排序只能用在有向无环图(Directed Acyclic Graph, DAG)，拓扑序不唯一。拓扑排序可以理解为：对某点v而言，只有当v的所有源点均出现了，v才能出现  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/right_dag.png" width="400px"> </div><br>

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/wrong_dag.png" width="400px"> </div><br>

1. 实现算法  
   - 入度表

