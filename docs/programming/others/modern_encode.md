
Table of Contents
=================

   * [现代编码模型](#现代编码模型)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [基本概念](#基本概念)
      * [抽象字符集ACR](#抽象字符集acr)
         * [字符(character, char)](#字符character-char)
         * [抽象字符 (Abstract Character)](#抽象字符-abstract-character)
      * [编码字符集CCS(Coded Character Set)](#编码字符集ccscoded-character-set)
         * [统一字符集 UCS (Universal Character Set)](#统一字符集-ucs-universal-character-set)

Created by ALTA
# 现代编码模型  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [Python编码为什么蛋疼](https://www.zhihu.com/question/31833164)

## 基本概念  

现代编码模型自底向上分为五个层次：

- 抽象字符表 ACR (Abstract Character Repertoire)
- 编码字符集 CCS (Coded Character Set)
- 字符编码表 CEF (Character Encoding Form)
- 字符编码方案 CES (Character Encoding Schema)
- 传输编码语法 TES (Transfer Encoding Syntax)

参考如下标准：

- [现代编码模型-Wiki](https://zh.wikipedia.org/wiki/%E5%AD%97%E7%AC%A6%E7%BC%96%E7%A0%81#.E7.8E.B0.E4.BB.A3.E7.BC.96.E7.A0.81.E6.A8.A1.E5.9E.8B)
- [Unicode术语表](http://unicode.org/glossary/)

## 抽象字符集ACR  

抽象字符集是现代编码模型的最底层，它是一个集合，通过枚举指明了所属的所有抽象字符。但是要了解抽象字符集是什么，我们首先需要了解什么是**字符**与**抽象字符**

### 字符(character, char)  

字符是指字母、数字、标点、表意文字（如汉字）、符号、或者其他文本形式的书写“原子”。例：`a`,`啊`,`あ`,`α`,`Д`等，都是抽象的字符。  

### 抽象字符 (Abstract Character)  

抽象字符就是抽象的字符。像`a`这样的字符是有形的，但在计算机中，有许多的字符是空白的，甚至是不可打印的。比如ASCII字符集中的NULL，就是一个抽象字符。注意`\x00`,`\000`,`NULL`,`0`这些写法都只是这个抽象字符的某种表现形式，而不是这个抽象字符本身。

抽象字符集顾名思义，指的是**抽象字符的集合**，已经有了很多标准的字符集定义: [Character Sets](http://www.iana.org/assignments/character-sets/character-sets.xhtml)。比如US-ASCII, UCS(Unicode), GBK这些我们耳熟能详的名字，都是(或者至少是)抽象字符集.  

US-ASCII定义了128个抽象字符的集合。GBK挑选了两万多个中日韩汉字和其他一些字符组成字符集，而UCS则尝试去容纳一切的抽象字符。它们都是抽象字符集。  

- 抽象字符 英文字母`A`同时属于US-ASCII, UCS, GBK这三个字符集。
- 抽象字符 中文文字`蛤`不属于US-ASCII，属于GBK字符集，也属于UCS字符集。
- 抽象文字 Emoji 不属于US-ASCII与GBK字符集，但属于UCS字符集。

集合的一个重要特性，就是无序性，集合中的元素都是无序的，所以抽象字符集中的字符都是**无序的**，抽象字符集对应的是python中的set的概念。 例：我可以自己定义一个字符的集合，叫这个集合为haha字符集  

>haha_acr = { 'a', '吼', 'あ', ' α', 'Д' }

大家觉得**抽象字符集**这个名字太啰嗦，所以有时候直接叫它**字符集**。最后需要注意一点的是，抽象字符集也是有**开放**与**封闭**之分的。 ASCII抽象字符集定义了128个抽象字符，再也不会增加。这是一个封闭字符集。Unicode尝试收纳所有的字符，一直在不断地扩张之中。最近(2016.06)Unicode9.0.0已经收纳了128,237个字符，并且未来仍然会继续增长，这是一个开放的字符集。  

## 编码字符集CCS(Coded Character Set)  

>Coded Character Set. A character set in which each character is assigned a numeric code point. Frequently abbreviated as character set, charset, or code set; the acronym CCS is also used.

**编码字符集**是一个每个所属字符都分配了**码位**的抽象**字符集**。 **编码字符集****(CCS)**也经常简单叫做**字符集****(Character Set)**。这样的叫法经常会将**抽象字符集****ACR**与**编码字符集****CCS**搞混。不过大多时候人们也不在乎这种事情。  
**抽象字符集**是抽象字符的集合，而集合是**无序**的。无序的抽象字符集并没有什么卵用，因为我们只能判断某个字符是否属于某个字符集，却无法方便地引用，指称这个集合中的某个特定元素。以下两个表述指称了同一个字符，但哪一种更方便呢？  

- ASCII(抽象)字符集中的那个代表什么都没有的通常表示为NULL的抽象字符
- ASCII(编码)字符集中的0号字符

为了更好的描述，操作字符，我们可以为抽象字符集中的每个字符关联一个数字编号，这个数字编号称之为**码位(Code Point)**。通常根据习惯，我们为字符分配的**码位**通常都是非负整数，习惯上用十六进制表示。且一个编码字符集中字符与码位的映射是**一一映射**。  

举个例子，为haha抽象字符集进行编码，就可以得到haha编码字符集。  

> haha_ccs = { 'a' : 0x0, '吼':0x1 , 'あ':0x2 , ' α':0x3 , 'Д':0x4  }

字符`吼`与码位`0x1`关联，这时候，在haha编码字符集中，`吼`就不再是一个单纯的抽象字符了，而是一个**编码字符(Coded Chacter)**，且拥有码位 `0x1`。  
如果说抽象字符集是一个Set，那么编码字符集就可以类比为一个Dict.  

```python
CCS = { k:i for i, k in enumerate(ACR)}
```

它的key是字符，而value则是码位。至于码位具体是怎样分配的，这个规律就不好说了。比如为什么我想给haha_ccs的`吼`字符分配码位`0x1`而不是`0x23333`呢？因为这样能续一秒，反映了CCS设计者的主观趣味。  

编码字符集有许许多多，但最出名的应该就是US-ASCII和UCS了。ASCII因为太有名了，所以就不说了.  

### 统一字符集 UCS (Universal Character Set)  

最常见的**编码字符集**就是**统一字符集 UCS**  

> UCS. Acronym for Universal Character Set, which is specified by International Standard ISO/IEC 10646, which is equivalent in repertoire to the Unicode Standard.  

UCS就是统一字符集，就是由 ISO/IEC 10646所定义的编码字符集。通常说的“**Unicode字符集**”指的就是它。不过需要辨明的一点是，**Unicode**这个词本身指的是一系列用于计算机表示所有语言字符的**标准**。基本上所有能在其他字符集中遇到的符号，都可以在UCS中找到，而一些新的不属于任何传统字符集的字符，例如Emoji，也会收录于UCS中。这也是UCS地位超然的原因.  
举个例子，UCS中码位为0x4E00~0x9FFF的**码位**，就用于表示**中日韩统一表意文字**  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/ucs_1.jpg" width="400px"> </div><br>

大家喜闻乐见的Emoji表情则位于更高的码位，例如“哭笑”，在UCS中的码位就是0x1F602。  

关于CCS，这些介绍大抵足够了。不过还有一个细节需要注意。按照目前最新Unicode 9.0.0的标准，UCS理论上收录了128,237个字符,也就是0x1F4ED个。不过如果进行一些尝试会发现，实际能用的最大的码位点在0x1F6D0 ，也就是128,720，竟然超过了收录的字符数，这又是为什么呢？

