
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# 魔术方法  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. 111111

### 

Content 

1. Number-prefix class  

   Content 

   - Symbol-prefix class 

     Content 

## 魔术方法  

### `__slot__`  

用于限制实例的属性，比如，只允许对Student实例添加`name`和`age`属性。`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的  

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

### `__iter__`  

用于返回一个迭代对象(<font color=Red>该对象需包含`__next__`方法</font>)，然后，Python的for循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环

### `__next__`  

用于  

### `__call__`  



### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 