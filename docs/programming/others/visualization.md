
Table of Contents
=================

   * [Visualization](#visualization)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [定义](#定义)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理过程](#基本概念架构与处理过程)
         * [matplotlib图形结构](#matplotlib图形结构)

Created by ALTA
# Visualization  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [Python可视化笔记43篇合集](https://zhuanlan.zhihu.com/p/313462427)  

## 定义  

Left blank

## 问题背景  

left blank

## 基本概念、架构与处理过程  

### matplotlib图形结构  

- figure层  

  指整张图，可设置整张图的分辨率（dpi），长宽（size）、标题（title）等特征；可包含多个axes，可简单理解为多个子图（下图为两个axes）；figure置于canvas系统层之上，用户不可见；  

  <div align="center"> <img src="https://blackholemedia.github.io/documents/statics/matplotlib.webp" width="400px"> </div><br>

- axes层  

  每个子图，可以绘制各种图形，例如柱状图（bar），饼图（pie函数），箱图（boxplot）等；

