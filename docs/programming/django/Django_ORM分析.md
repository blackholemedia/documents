
Table of Contents
=================

   * [Django ORM分析](#django-orm分析)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [model中各类继承关系](#model中各类继承关系)
      * [manager](#manager)
         * [manager继承QuerySet所有方法](#manager继承queryset所有方法)
         * [每一个model的manager](#每一个model的manager)

Created by ALTA
# Django ORM分析  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [参考资料](<https://www.jianshu.com/p/ac87788b55f3>)  

## model中各类继承关系  

1. type —> ModelBase(元类) —>Model(基类)

## manager  

### manager继承QuerySet所有方法  
modle.objects中的objects是modle的manager，manager是Manager类，俗称管理器，他是继承BaseManager并且通过BaseManager.get_queryset(QuerySet),将QuerySet类的所有方法都添加到了manager中，所以modle.objects.using(db).all()其实就是modle.objects.queryset.using(db).all()，modle.objects.get(pk=xx)就等于modle.objects.queryset.get()；  

### 每一个model的manager  


