
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# Cryptography  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [RSA算法原理](http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html)  
2. [RSA算法原理二](http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html)  
3. [RSA的公钥和私钥到底哪个才是用来加密和哪个用来解密？ - 王希的回答 - 知乎](https://www.zhihu.com/question/25912483/answer/252031361)  
4. [RSA的公钥和私钥到底哪个才是用来加密和哪个用来解密？ - 刘巍然-学酥的回答 - 知乎](https://www.zhihu.com/question/25912483/answer/31653639)  
5. [数字签名](<http://www.youdzone.com/signature.html>)  


## 定义  

Left blank

## 问题背景  

left blank

## 基本概念、架构与处理过程  

### 对称加密  

> （1）甲方选择某一种加密规则，对信息进行加密；
> （2）乙方使用同一种规则，对信息进行解密。

加密和解密使用同样**规则（简称"密钥"）**, 这种加密模式有一个最大弱点：甲方必须把加密规则告诉乙方，否则无法解密。保存和传递密钥，就成了最头疼的问题  

### 非对称加密  

人们认识到，加密和解密可以使用不同的规则，只要这两种规则之间存在某种对应关系即可(<font color=Yellow>这种对应关系不就相当于密钥了吗.....迷</font>)，这样就避免了直接传递密钥   

> （1）乙方生成两把密钥（公钥和私钥）。公钥是公开的，任何人都可以获得，私钥则是保密的。
> （2）甲方获取乙方的公钥，然后用它对信息加密。
> （3）乙方得到加密后的信息，用私钥解密。

<font color=Red>由上述过程可知，对应关系没有被传递，一直在乙的手里，从而克服密钥传递问题</font>  

### 非对称加密的典型算法-RSA

#### 欧拉函数与欧拉定理  

> 任意给定正整数n，请问在小于等于n的正整数之中，有多少个与n构成互质关系？（比如，在1到8之中，有多少个数与8构成互质关系？）

计算这个值的方法就叫做[欧拉函数](http://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0)，以φ(n)表示，在1到8之中，与8形成互质关系的是1、3、5、7，所以 φ(n) = 4，欧拉函数计算参考引用1.  

欧拉函数的用处，在于[欧拉定理](http://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%AE%9A%E7%90%86_(%E6%95%B0%E8%AE%BA))。"欧拉定理"指的是:

> 如果两个正整数a和n互质，则n的欧拉函数 φ(n) 可以让下面的等式成立：

$$
a^{\phi(n)}\equiv1(mod\quad n)
$$

也就是说，a的φ(n)次方被n除的余数为1。或者说，a的φ(n)次方减去1，可以被n整除  

#### 模反元素  

> 如果两个正整数a和n互质，那么一定可以找到整数b，使得 ab-1 被n整除，或者说ab被n除的余数是1,这时，b就叫做a的["模反元素"](http://zh.wikipedia.org/wiki/%E6%A8%A1%E5%8F%8D%E5%85%83%E7%B4%A0)。

$$
ab\equiv1(mod\quad n)
$$

#### RSA加密体制  

RSA公钥加密体制包含如下3个算法：KeyGen（密钥生成算法），Encrypt（加密算法）以及Decrypt（解密算法）

##### 密钥生成  

1. 选取两不等质数p, q, 求积n=p×q
2. 计算n的欧拉函数φ(n) = (p-1)(q-1)（如果n可以分解成两个互质的整数之积，积的欧拉函数等于各个因子的欧拉函数之积，儿质数的欧拉函数为n-1）
3. 随机选择一个整数e，条件是1< e < φ(n)，且e与φ(n) 互质
4. 计算e对于φ(n)的模反元素d
5. 公钥为PK=(n, e)，私钥为SK=(n, d）

### 数字签名  

既然是加密，那肯定是不希望别人知道我的消息，所以只有我才能解密，所以可得出**公钥负责加密，私钥负责解密**；同理，既然是签名，那肯定是不希望有人冒充我发消息，只有我才能发布这个签名，所以可得出**私钥负责签名，公钥负责验证**  



