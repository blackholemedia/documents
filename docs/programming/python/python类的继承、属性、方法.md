
Table of Contents
=================

   * [python类的继承、属性及方法](#python类的继承属性及方法)
      * [阅读说明](#阅读说明)
      * [类的继承](#类的继承)
         * [使用继承](#使用继承)
         * [多重继承](#多重继承)
      * [类的属性-总结](#类的属性-总结)
      * [类的方法-总结](#类的方法-总结)

Created by ALTA
# python类的继承、属性及方法  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```



## 类的继承  

继承关系：继承是相对两个类而言的父子关系，子类继承了父类的所有__公有属性和方法__，继承实现了代码重用。

### 使用继承  

```python
class Myclass(ParentClass)
```

如果父类定义了init方法，子类必须显式调用父类的init方法： 

```python
ParentClass.init(self,[args…])
```

如果子类需要扩展父类的行为，可以添加init方法的参数

### 多重继承  
1. 语法： 

```python
class class_name(Parent_c1,Parent_c2,….)
```

2. 注意： 

当父类中出现多个自定义的init方法时，多重继承只执行第一个类的init方法，其它不执行。

```python
class People(object):
    color = 'yellow'
    # def __init__(self, c):#参数大于等于2个，子类必须显式调用；只有一个参数的话，可以直接调用。单一继承
    def __init__(self):#多重继承
        print "Init..."      
        self.dwell = 'Earth'
        self.color = 'yellow'
        
    def think(self):
        print "I am a %s" %self.color
        print "My home is %s" %self.dwell
        print "I am a thinker"

class Martian(object):

    color = 'red'
    
    def __init__(self):
        self.dwell = 'Martian'

class Chinese(Martian, People): #多重调用跟位置关系有关；可通过显式调用改变

    def __init__(self):
        # People.__init__(self, 'red')
        People.__init__(self)
        # super(Chinese, self).__init__( 'red') #通过super函数继承父类

    # pass
    # def talk(self):
    #     print("I like talking")
    # def think(self): #这里通过子类对父类的重写
    #     print("I like talking")

cn = Chinese()

# print cn.color #继承父类的color

cn.think()

# cn.talk()
```

## 类的属性-总结

- 类的属性，也有公有属性
- 类的私有属性
- 对象的公有属性
- 对象的私有属性
- 内置属性
- 函数的局部变量

```python

class MyClass(object):

    var1 = '类属性，类的公有属性 var1'
    __var2 = '类的私有属性 __var2'

    def func1(self):
        self.var3 = '对象的公有属性 var3'  #对象属性，只能对象访问
        self.__var4 = '对象的私有属性 __var4'  #无法通过对象访问，类的外面
        var5 = '函数的局部变量 var5'  #只能在函数的内部访问
        print self.__var4
        print var5

    def func2(self):
        print self.var1
        print self.__var2
        print self.var3
        print self.__var4

mc = MyClass()
mc.func1()
print('******' * 10)
mc.func2()
print('******' * 10)
print mc.__dict__
print MyClass.__dict__

# # print mc.var1  #公有属性
# # print mc._MyClass__var2 #私有属性
# # print mc.var3
```

## 类的方法-总结  

- 公有方法

- 私有方法

- 实例方法

  1.只能由实例对象调用; 2.第一个参数必须是实例对象(一般约定为self)，通过它来传递实例的属性和方法（也可以传类的属性和方法）。

- 类方法

  1.实例对象和类对象都可以调用; 2.第一个参数必须是当前类对象(一般约定为cls)，通过它来传递类的属性和方法（不能传实例的属性和方法）。

  原则上，类方法是将类本身作为对象进行操作的方法。假设有个方法，且这个方法在逻辑上采用类本身作为对象来调用更合理，那么这个方法就可以定义为类方法

- 静态方法

  1.实例对象和类对象都可以调用；2.参数随意，方法体中不能使用类或实例的任何属性和方法

  静态方法是类中的函数，不需要实例。静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个**独立的、单纯的**函数，它仅仅托管于某个类的名称空间中，便于使用和维护。

```python
class MyClass(object):

    name = 'Test'

    def __init__(self): #只需进行类的实例化，即可被调用。其它可不用
        self.func1()
        self.__func2()
        self.classFun()
        self.staticFun()

    def func1(self):
        print self.name,
        print "我是公有方法"
        
    # self.__func2() #私有方法需通过内部调用，的方式间接调用
    def __func2(self):
        print self.name,
        print "我是私有方法"

    @classmethod
    def classFun(self):
        print self.name,
        print "我是类方法"

    @staticmethod
    def staticFun():
        print MyClass.name
        print "我是静态方法"

mc = MyClass()

# mc.func1()
# MyClass.classFun()
# MyClass.staticFun()
```