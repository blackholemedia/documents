
Table of Contents
=================

   * [现代编码模型](#现代编码模型)
      * [参考引用](#参考引用)
      * [基本概念](#基本概念)
      * [抽象字符集ACR](#抽象字符集acr)
         * [字符](#字符)
         * [抽象字符](#抽象字符)
      * [编码字符集CCS](#编码字符集ccs)
         * [统一字符集UCS](#统一字符集ucs)
         * [其他字符集](#其他字符集)
      * [字符编码表CEF](#字符编码表cef)
         * [码元](#码元)
      * [字符编码方案CES](#字符编码方案ces)
      * [传输编码语法TES](#传输编码语法tes)
      * [应用](#应用)
         * [Python2中的编码问题](#python2中的编码问题)

Created by ALTA
# 现代编码模型  

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

### 字符  

> character, char  

字符是指字母、数字、标点、表意文字（如汉字）、符号、或者其他文本形式的书写“原子”。例：`a`,`啊`,`あ`,`α`,`Д`等，都是抽象的字符。  

### 抽象字符   

> Abstract Character

抽象字符就是抽象的字符。像`a`这样的字符是有形的，但在计算机中，有许多的字符是空白的，甚至是不可打印的。比如ASCII字符集中的NULL，就是一个抽象字符。注意`\x00`,`\000`,`NULL`,`0`这些写法都只是这个抽象字符的某种表现形式，而不是这个抽象字符本身。

抽象字符集顾名思义，指的是**抽象字符的集合**，已经有了很多标准的字符集定义: [Character Sets](http://www.iana.org/assignments/character-sets/character-sets.xhtml)。比如US-ASCII, UCS(Unicode), GBK这些我们耳熟能详的名字，都是(或者至少是)抽象字符集.  

US-ASCII定义了128个抽象字符的集合。GBK挑选了两万多个中日韩汉字和其他一些字符组成字符集，而UCS则尝试去容纳一切的抽象字符。它们都是抽象字符集。  

- 抽象字符 英文字母`A`同时属于US-ASCII, UCS, GBK这三个字符集。
- 抽象字符 中文文字`蛤`不属于US-ASCII，属于GBK字符集，也属于UCS字符集。
- 抽象文字 Emoji 不属于US-ASCII与GBK字符集，但属于UCS字符集。

集合的一个重要特性，就是无序性，集合中的元素都是无序的，所以抽象字符集中的字符都是**无序的**，抽象字符集对应的是python中的set的概念。 例：我可以自己定义一个字符的集合，叫这个集合为haha字符集  

>haha_acr = { 'a', '吼', 'あ', ' α', 'Д' }

大家觉得**抽象字符集**这个名字太啰嗦，所以有时候直接叫它**字符集**。最后需要注意一点的是，抽象字符集也是有**开放**与**封闭**之分的。 ASCII抽象字符集定义了128个抽象字符，再也不会增加。这是一个封闭字符集。Unicode尝试收纳所有的字符，一直在不断地扩张之中。最近(2016.06)Unicode9.0.0已经收纳了128,237个字符，并且未来仍然会继续增长，这是一个开放的字符集。  

## 编码字符集CCS  

>Coded Character Set. A character set in which each character is assigned a numeric code point. Frequently abbreviated as character set, charset, or code set; the acronym CCS is also used.

**编码字符集**是一个每个所属字符都分配了**码位**的**抽象字符集**。 编码字符集(CCS)也经常简单叫做**字符集(Character Set)**。这样的叫法经常会将抽象字符集ACR与编码字符集CCS搞混。不过大多时候人们也不在乎这种事情。  
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

编码字符集有许许多多，但最出名的应该就是**US-ASCII**和**UCS**了。ASCII因为太有名了，所以就不说了.  

### 统一字符集UCS   

最常见的**编码字符集**就是**统一字符集 UCS**  

> UCS. Acronym for Universal Character Set, which is specified by International Standard ISO/IEC 10646, which is equivalent in repertoire to the Unicode Standard.  

UCS就是统一字符集，就是由 ISO/IEC 10646所定义的编码字符集。通常说的“**Unicode字符集**”指的就是它。不过需要辨明的一点是，**Unicode**这个词本身指的是一系列用于计算机表示所有语言字符的**标准**。基本上所有能在其他字符集中遇到的符号，都可以在UCS中找到，而一些新的不属于任何传统字符集的字符，例如Emoji，也会收录于UCS中。这也是UCS地位超然的原因.  
举个例子，UCS中码位为0x4E00~0x9FFF的**码位**，就用于表示**中日韩统一表意文字**  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/ucs_1.jpg" width="400px"> </div><br>

大家喜闻乐见的Emoji表情则位于更高的码位，例如“哭笑”，在UCS中的码位就是0x1F602。  

关于CCS，这些介绍大抵足够了。不过还有一个细节需要注意。按照目前最新Unicode 9.0.0的标准，UCS理论上收录了128,237个字符,也就是0x1F4ED个。不过如果进行一些尝试会发现，实际能用的最大的码位点在0x1F6D0 ，也就是128,720，竟然超过了收录的字符数，这又是为什么呢？  

**码位**是非负整数没错，但这不代表它一定是连续分配的。出现这种情况只有一个原因，那就是UCS的码位分配不是连续的，中间有一段空洞，即存在一段码位，没有分配对应的字符。  

实际上，UCS实际分配的**码位**是 **0x0000~0x0xD7FF** 与 **0xE000~0x10FFFF** 这两段。中间**0xD800~0xDFFF**这2048个码位留作它用，并不对应实际的字符。如果直接尝试去输出这个码位段的'字符'，结果会告诉你这是个非法字符。例如在python2中尝试打印码位0xDDDD的字符：  

```python
>>> print u'\UDDDD'
File "<stdin>", line 1
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-5: truncated \UXXXXXXXX escape
```

- 0x0000~0xD7FF | 0xE000~0x10FFFF 称为Unicode标量值(Unicode scala value)
- 0xD800~0xDBFF 称为High-surrogate
- 0xDC00~0xDFFF 称为Low-surrogate

**Unicode标量值**就是实际存在对应字符的**码位**. 为什么中间一端的码位会留空，则是为了方便下一个层次的**字符编码表**CEF的UTF-16而处理的.  

### 其他字符集  

除了ASCII与UCS，世界上还有许许多多的字符集。在US-ASCII诞生与Unicode诞生之间，很多英语之外的字符无法在计算机中表示。大家八仙过海各显神通，定义了许许多多其他的字符集。例如GBK字符集，以及其近似实现 Code Page 936。这些字符集中的字符，最后都汇入了Unicode中  

## 字符编码表CEF  

> Unicode Encoding Form. A character encoding form that assigns each Unicode scalar value to a unique code unit sequence. The Unicode Standard defines three Unicode encoding forms: UTF-8, UTF-16, and UTF-32

现在我们拥有一个编码字符集了，Let's say: UCS。这个字符集中的每个字符都有一个非负整数码位与之一一对应。
看上去很好，既然计算机可以存储整数，而现在字符已经能表示为整数，我们是不是可以说，用计算机存储字符的问题已经得到了解决呢？

慢！还有一个问题没有解决。

在讲抽象字符集ACR的时候曾经提起，UCS是一个**开放字符集**，未来可能有更多的符号加入到这个字符集中来。也就是说UCS需要的码位，理论上是无限的。但计算机**整形**能表示的整数范围是有限的。譬如，一个字节的无符号单字节整形(unsigned char, uint8)能够表示的码位只有0~0xFF，共256个；一个无符号短整形(unsigned short, uint16)的可用码位只有0~0xFFFF，共65536个；而一个标准整形(unsigned int, uint32)能表示的码位只有0~0xFFFFFFFF，共4294967296个。

虽然就目前来看，UCS收录的符号总共也就十多万个，用一个uint可以表示几十亿个字符呢。但谁知道哪天制定Unicode标准的同志们不会玩心大发造几十亿个Emoji加入UCS中。所以说到底，一对**有限与无限的矛盾，必须通过一种方式进行调和**。这个解决方案，就是**字符编码表(Character Encoding Form)**。  

> 字符编码表将码位(Code Point)映射为码元序列(Code Unit Sequences)

对于Unicode而言，字符编码表将**Unicode标量值(Unicode scalar value)**一一映射为**码元序列(Code Unit Sequences)**。  

### 码元  

> Code unit: The minimal bit combination that can represent a unit of encoded text for processing or interchange.

码元是能用于处理或交换编码文本的最小比特组合。通常计算机处理字符的码元为一字节，即8bit。同时因为计算机中char其实是一种整形，而整形的计算往往以计算机的字长作为一个基础单元，通常来讲，也就是4字节。  

Unicode定义了三种不同的CEF，分别采用了1字节，2字节，4字节的码元，正好对应了计算机中最常见的三种整形长度：  

> 在Unicode中，指定了三种标准的字符编码表，UTF-8, UTF-16, UTF-32。分别将Unicode标量值映射为比特数为8、16、32的码元的序列

UTF-8的码元为uint8, UTF-16的码元为uint16, UTF-32的码元为uint32。当然有一些非标准的CEF，如UCS-2,UCS-4，在此不多介绍。  

需要注意一点的是，CEF将**码位**映射为**码元序列。**这个映射必须是**一一映射(双射)**。因为当使用CEF进行**编码(Encode)**时，是将码位映射为码元序列。而当使用CEF进行**解码(Decode)**时，是将码元序列还原为码位。为了保证两个过程都不出现歧义，必须保证CEF是一个双射。  

知道了**字符编码表CEF**是什么还不够，我们还需要知道它是怎么做的。即：**如何将一个无限大的整数，一一映射为指定字宽的码元序列**。  

这个问题可以通过变长编码来解决：无论是UTF-8还是UTF-16，本质思想都是**通过预留标记位来指示码元序列的长度，**从而实现变长编码。  

各个CEF的细节我建议参看维基百科: [UTF-8](https://zh.wikipedia.org/wiki/UTF-8), [UTF-16](https://zh.wikipedia.org/wiki/UTF-16), [UTF-32](https://zh.wikipedia.org/wiki/UTF-32), 更深入学习方式就是直接阅读[Unicode9.0.0 Standard](http://www.unicode.org/versions/Unicode9.0.0/)  

例子：  

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/cef_1.jpg" width="400px"> </div><br>

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/cef_2.jpg" width="400px"> </div><br>

## 字符编码方案CES  

> Unicode encoding scheme: A specified byte serialization for a Unicode encoding
> form, including the specification of the handling of a byte order mark (BOM), if
> allowed.

简单说，**字符编码方案 CES** 等于 **字符编码表CEF** 加上**字节序列化**的方案。通过字符编码表CEF我们已经可以将字符转为码元序列。无论是哪种UTF-X的码元，都可以找到计算机中与之对应的整形存放。那么现在我们能说存储处理交换字符这个问题解决了吗？还不行。  

假设一个字符按照UTF16拆成了若干个码元组成的码元序列，因为每个码元都是一个unsigned short，实际上是两个字节。因此将码元序列化为字节序列的时候，就会遇到一些问题。  

- 大小端序问题：每个码元究竟是高位字节在前还是低位字节在前呢？
- 字节序标记问题：另一个程序如何知道当文本是什么端序的呢？

这些都是CEF需要操心的问题。对于网络交换和本地处理，大小端序各有优劣。这个问题不属于本文范畴。
**字节序标记BOM (Byte Order Mark)**，则是放置于编码字节序列开始处的一段特殊字节序列，用于表示文本序列的大小端序。对于这两个问题的不同答案，在3种CEF：UTF-8,UTF-16,UTF-32上。Unicode实际上定义了7种字符编码方案CES:

- UTF-8
- UTF-16LE
- UTF-16BE
- UTF-16
- UTF-32LE
- UTF-32BE
- UTF-32

其中UTF-8因为已经采用字节作为码元了，所以实际上不存在字节序的问题。其他两种CES嘛，都有一个大端版本一个小端版本，还有一个随机应变大小端带BOM的版本. 下面给一个Python编码的小例子，将Emoji：哭笑 转换为各种CES.  

```python
for encoding in ['UTF-8', 'UTF-16LE', 'UTF-16BE', 'UTF-16', 'UTF-32LE', 'UTF-32BE', 'UTF-32']:
    print('%-10s\t%s' % (encoding, repr(us.encode(encoding))))
    
# ---------------------------------- 输出结果
UTF-8           b'\xf0\x9f\x98\x82'
UTF-16LE        b'=\xd8\x02\xde'
UTF-16BE        b'\xd8=\xde\x02'
UTF-16          b'\xff\xfe=\xd8\x02\xde'
UTF-32LE        b'\x02\xf6\x01\x00'
UTF-32BE        b'\x00\x01\xf6\x02'
UTF-32          b'\xff\xfe\x00\x00\x02\xf6\x01\x00'
```

- UTF-8将:joy:编码成了四个字节 0xF0 0x9F 0x98 0x82  
- UTF-16BE是大端编码，将:joy:编码成了0xD8 0x3D 0xDE 0x02  
- UTF-16LE是小端编码，所以每个二字节的码元内大小字节排列次序正好想法，编码成了 0x3D 0xD8 0x02 0xDE  
- UTF-16默认采用小端编码且带BOM，所以编码成了 0xFF 0xFE 0x3D 0xD8 0x02 0xDE，0xFFFE是BOM，代表小端序  
- UTF-32与UTF-16基本同理     

这里也出现一个问题，历史上**字符编码方案(Character Encoding Schema)**曾经就是指**UTF(Unicode Transformation Formats)**。所以UTF-X到底是属于字符编码方案CES还是属于字符编码表CEF是一个模棱两可的问题。UTF-X可以同时指代字符编码表CEF或者字符编码方案CES。
UTF-8问题还好，因为UTF-8的字节序列化方案太朴素了，以至于CES和CEF都没什么区别。但其他两种：UTF-16,UTF-32，就比较棘手了。当我们说UTF-16时，既可以指代UTF-16字符编码表，又可以指代UTF-16字符编码方案。所以当有人说“这个字符串是**UTF-16编码**的”时，鬼知道他到底说的到底是一个**（UTF-16 encoding form的）码元序列**还是**(UTF-16 encoding schema 的)字节流**。  

简单的说，字符编码表CEF和字符编码方案CES区别如下：

> c ∈ CCS ---CEF--> Code Unit Sequence
> c ∈ CCS ---CES--> Byte Sequence

**字符编码表CEF**将**码位**映射为**码元序列**，而**字符编码方案CES**将**码位**序列化为**字节流**。  

<font color=Red>我们通常所说的动词**编码(Encode)**就是指使用CES，将CCS中字符组成的字符串转变为字节序列。
而**解码(Decode)**就是反过来，将 **编码字节序列** 通过CES的一一映射还原为CCS中字符的序列。</font>  

除了Unicode标准定义的七中CES，还有两种CES: UCS-2，UCS-4 。严格来说，UCS-2和UCS-4属于字符编码表CEF的层次，不过鉴于其朴素的序列化方案，也可以理解为CES。这两种CES的特点是采用定长编码，比如UCS-2直接把码位序列化为unsigned short。之前一直很流行，但当UCS中字符越来越多，超过65536个之后，UCS-2就GG了。至于UCS-4，基本和UTF-32差不多。虽说有生之年基本不可能看到UCS大小超出四字节的表示范围，但每个字符统一用4字节来存储这件事本身就很蠢了……。  

当然除了UCS，其他字符集，例如US-ASCII，GBK，也会有自己的字符编码方案，只不过我们很少听说，一个很重要的原因是，这些字符集的编码方案太简单了，以至于CCS，CEF，CES三层直接合一了。
例如US-ASCII的CES，因为ASCII就128个字符，只要直接把其**码位**转换成(char)，就完成了编码。如此简单的编码，直接让CCS，CEF，CES三层合一。很多其他的字符集也与之类似。  

## 传输编码语法TES  

通过CES，我们已经可以将一个字符表示为一个字节序列。但是有时候，字节序列表示还不够。比如在HTTP协议中，在URL里，一些字符是不允许出现的。这时候就需要再次对字节流进行编码。

著名的Base64编码，就是把字节流映射成了一个由64个安全字符组成字符集所表示的字符流。从而使字节流能够安全地在Web中传输。不过这一块的内容已经离我们讨论的主题太远了。

## 应用  

### Python2中的编码问题  

回到正题，出现各种编码问题，无非是哪里的编码设置出错了，常见编码错误的原因有：

- Python解释器的默认编码
- Python源文件文件编码
- Terminal使用的编码
- 操作系统的语言设置


最严重的问题其实是：

- **Python2的默认编码方案的非常不合理。**  

  Python2解释器的**默认编码方案(CES)**是US-ASCII。Java，C#，Javascript等语言内部的默认**编码方案**都是UTF-16，Go语言的内部默认**编码方案**使用UTF-8。与之相比，默认使用US-ASCII的python2简直是骨骼清奇，当然，这也有一部分历史原因在里头。Python3就乖乖地改成UTF-8了

- **Python2的字符串类型与字符串字面值很容易让人混淆**  

  python的默认'字符串类型'`<str>`与其叫**字符串**，不如叫**字节串**，用下标去访问的每一个元素都是一个**字节**。而`<unicode>`类型才是真正意义上的**字符串**，用下标去访问的每一个元素都是一个**字符**(虽然底下可能每个字符长度不同)。  
  
  字符串`<unicode>` 与 字节串`<str>` 的关系为:  
  
  1. 字符串`<unicode>` 通过字符编码方案(CES)编码(Encode) 得到字节串`<str>`  
  2. 字节串`<str>` 通过字符编码方案(CES)解码(Decode)得到字符串`<unicode>`  
  
  字节串就字节串，为啥要起个类型名叫str呢？另外，字面值语法用一对什么前缀都没有的引号表示str，这样的设计非常反直觉。当然，`<str>`与`<unicode>`这样的类型设计以及两者的关系设计本身是无可厚非的。该黑的应该是这两个类型起的**名字**和**字面值表示方法**。至于怎么改进是好的，Python3已经给出答案  

