
Table of Contents
=================

   * [Unittest](#unittest)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [主要概念](#主要概念)
         * [静态类图](#静态类图)
         * [工作过程](#工作过程)

Created by ALTA
# Unittest  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [Python必会的单元测试框架 —— unittest](https://www.cnblogs.com/hackerain/p/3682019.html)
2. [unittest介绍](<https://blog.csdn.net/huilan_same/article/details/52944782>)
3. [Django单元测试类——TestCase与TransactionTestCase](<https://blog.csdn.net/BDuck2014/article/details/86521755>)

## 主要概念  

`test fixture`, `test case`, `test suite`, `test runner`

### 静态类图  

![静态类图](https://blackholemedia.github.io/documents/statics/230040440455234.png)  

1. 一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)。单元测试(unit test)的本质也就在这里，一个测试用例是一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证  
2. 而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite  
3. TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法，就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例  
4. TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法  
5. 测试的结果会保存到TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息

### 工作过程  

1. 写好TestCase

2. 然后由TestLoader加载TestCase到TestSuite

3. 然后由TextTestRunner来运行TestSuite，运行的结果保存在TextTestResult中，

4. 整个过程集成在unittest.main模块中。我们通过命令行或者unittest.main()执行时，main会调用TextTestRunner中的run来执行，或者我们可以直接通过TextTestRunner来执行用例。这里加个说明，在Runner执行时，默认将执行结果输出到控制台，我们可以设置其输出到文件，在文件中查看结果（你可能听说过HTMLTestRunner，是的，通过它可以将结果输出到HTML中，生成漂亮的报告，它跟TextTestRunner是一样的）

5. 关于test fixture: 

   >Test authors should subclass TestCase for their own tests. Construction and deconstruction of the test's environment ('fixture') can be implemented by overriding the 'setUp' and 'tearDown' methods respectively.
   
   可见，对一个测试用例环境的搭建和销毁，是一个fixture，通过覆盖TestCase的setUp()和tearDown()方法来实现。

### 测试用例的区分  

```python
import random
import unittest
 
class TestSequenceFunctions(unittest.TestCase):
 
    def setUp(self):
        self.seq = range(10)
 
    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
 
        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))
 
    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
 
    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
 
if __name__ == '__main__':
    unittest.main()
```

上述一个测试类中包含3个测试方法，根据TestLoader是如何加载测试用例的(后面深入源码分析时补充)可是每个测试方法均为一个测试用例。**每个**测试用例**均会**执行一次setUp和tearDown方法，<u>如果希望所有的用例共用setUp和tearDown方法(即开始前执行1次setUp, 所有用例结束后执行1次tearDown)，使用类方法`setUpClass`、`tearDownClass`</u>  

PS: *unittest中并无_post_tearDown方法，该方法为django test继承unittest后扩展*

