
Table of Contents
=================

   * [Python Notes](#python-notes)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [杂乱的知识点](#杂乱的知识点)
         * [方法定义中(def)的冒号限制类型(或 -&gt;)](#方法定义中def的冒号限制类型或--)
         * [切片操作](#切片操作)
         * [查询模块帮助文档](#查询模块帮助文档)
         * [字符串中的引号](#字符串中的引号)
         * [函数的参数](#函数的参数)
         * [创建generator的两种方式](#创建generator的两种方式)
         * [__str__和__repr__方法](#__str__和__repr__方法)

Created by ALTA
# Python Notes  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. 11  

   

## 杂乱的知识点  

### 方法定义中(def)的冒号限制类型(或 ->)  

仅仅相当于注释，不强制检查

### 切片操作  

 [start_index:  stop_index:  step]：start_index是切片的起始位置，stop_index是切片的结束位置（不包括），step可以不提供，默认值是1，步长值不能为0

```python
L=list(range(10))
L1=L[0:3]  #从索引0开始取，直到索引3为止，但不包括索引3
#运行结果：[0, 1, 2]
L2=L[:3]   #如果第一个索引是0，还可以省略
#运行结果：[0, 1, 2]
L3=L[:-1]  #Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片,倒数第一个元素的索引是-1
#运行结果：[0, 1, 2, 3, 4, 5, 6, 7, 8]
L4=L[1:8:2] #前8个数，每两个取一个
#运行结果：[1, 3, 5, 7]
L5=L[::-1]  #倒序取每一个数
#运行结果：[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
L6=L[:]     #只写[:]就可以原样复制一个list
#运行结果：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 查询模块帮助文档  

1. 先导入模块，再查询普通模块的使用方法， `help(module_name)`
2. 先导入sys，再查询系统内置模块的使用方法，`sys.bultin_modulenames`
3. 查看模块下所有函数，`dir(module_name)`
4. 查看模块下特定函数，`help(module_name.function_name)`
5. 查看函数信息的另一种方法，`print(func_name.__doc__)`

### 字符串中的引号  

单引号`' '`定义字符串的时候，它就会认为你字符串里面的双引号`" "`是普通字符，从而不需要转义。反之当你用双引号定义字符串的时候，就会认为你字符串里面的单引号是普通字符无需转义

```python
Str1 = "We all know that 'A' and 'B' are two capital letters."
Str2 = 'The teacher said: "Practice makes perfect" is a very famous proverb.'
```

### 函数的参数  

1. 必选参数：即位置参数

2. 默认参数：如`def power(x, n=2)`，x即为位置参数，n为默认参数，必选参数在前，默认参数在后

3. 可变参数：传入的参数个数是可变的，不必自行将所有参数组装成一个list或tuple，如`def 	calc(*args)`。定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个`*`号。在函数内部，参数args接收到的是一个tuple

   ```python
   def calc(*numbers):
   	sum = 0
   	for n in numbers:
   		sum = sum + n * n
   	return sum
   ```

4. 关键字参数：可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict：

   ```python
   def person(name, age, **kwargs):
   	print('name:', name, 'age:', age, 'other:', kw)
   >>> person('Bob', 35, city='Beijing')
   >>> name: Bob age: 35 other: {'city': 'Beijing'}
   ```


### 创建generator的两种方式  

1. `g = (x * x for x in range(10))`，列表生成式的[]更改为()

2. 如果一个函数定义中包含yield关键字，那么函数就不再是一个普通函数，而是一个generator，函数是顺序执行，遇到return语句或者最后一行函数语句返回。而generator在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行  

   ```python
   def fib(max):
       n, a, b = 0, 0, 1
       while n < max:
           yield b
           a, b = b, a + b
           n = n + 1
       return 'done'
   ```


### `__str__`和`__repr__`方法  

两个方法均用于返回对象供人阅读，`__str__()`用于显示给用户，而`__repr__()`用于显示给开发人员。print调用的是`__str__`方法，直接输出实例调用的是`__repr__`方法

```python
>>> class Student(object):
		def __init__(self, name):
		self.name = name

>>> print(Student('Michael'))
<__main__.Student object at 0x109afb190>
>>> s = Student('Michael')
>>> s
<__main__.Student object at 0x109afb310>
```

