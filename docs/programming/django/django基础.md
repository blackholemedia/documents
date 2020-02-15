
Table of Contents
=================

   * [Django基础](#django基础)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [基本概念](#基本概念)
         * [Web应用框架](#web应用框架)
         * [MVC与MTV](#mvc与mtv)
         * [DJANGO的MTV组织](#django的mtv组织)

Created by ALTA
# Django基础  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. 111111

## 基本概念  

### Web应用框架  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/django_web_framework.jpg" width="400px"> </div><br>

### MVC与MTV  

MVC：全名Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。通俗解释：<font color=Red>一种文件的组织和管理形式！</font>其实就是把不同类型的文件放到不同的目录下的一种方法，然后取了个高大上的名字。当然，它带来的好处有很多，比如前后端分离，松耦合等等  

- 模型(model)：定义数据库相关的内容，一般放在models.py文件中。
- 视图(view)：定义HTML等静态网页文件相关，也就是那些html、css、js等前端的东西。
- 控制器(controller)：定义业务逻辑相关，就是你的主要代码

MTV：view不再是HTML相关，而是主业务逻辑了，相当于控制器。html被放在Templates中，称作模板，于是MVC就变成了MTV。和MVC本质上是一样的，换汤不换药

### DJANGO的MTV组织  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/django_mtv.jpg" width="400px"> </div><br>



