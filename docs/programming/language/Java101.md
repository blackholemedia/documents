
Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Java101](#java101)
      * [参考引用](#参考引用)
      * [基本概念](#基本概念)
         * [修饰符](#修饰符)
         * [泛型](#泛型)
      * [基本语法](#基本语法)
         * [变量](#变量)
         * [数组](#数组)
         * [方法](#方法)
         * [类](#类)

Created by ALTA

# Java101  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [泛型](<https://segmentfault.com/a/1190000014120746>)
2. [java new对象时直接在后面加两个大括号是什么用法](<https://www.oschina.net/question/2830476_2274044>)

### 

<div align="center"> <img src="https://blackholemedia.github.io/documents/statics/417bc315-4409-48c6-83e0-59e8d405429e.jpg" width="400px"> </div><br>

Content 

数学公式
$$
f'(t)=\lim_{\Delta t \to 0}\frac{f(t + \Delta t)-f(t)}{\Delta t}
$$

1. Number-prefix class  

   Content 

   - Symbol-prefix class 

     Content 

## 基本概念  

### 修饰符  

left blank

### 泛型  

泛型是**提供给javac编译器使用的**，它用于限定集合的输入类型，让编译器在源代码级别上，即挡住向集合中插入非法数据。**把类型明确的工作推迟到创建对象或调用方法的时候才去明确的特殊的类型**，因此泛型适用于对象(变量、类)/方法  

1. 泛型类  

   ```java
   public static void main(String[] args) {
       //创建对象并指定元素类型
       ObjectTool<Integer> objectTool = new ObjectTool<>();
       /**
        * 如果我在这个对象里传入的是String类型的,它在编译时期就通过不了.
        */
       objectTool.setObj(10);
       int i = objectTool.getObj();
       System.out.println(i);
   }
   ```

2. 泛型方法  

   ```java
   //定义泛型方法..
   public <T> void show(T t) {
       System.out.println(t);
   }
   
   public static void main(String[] args) {
       //创建对象
       ObjectTool tool = new ObjectTool();
   
       //调用方法,传入的参数是什么类型,返回值就是什么类型
       tool.show("hello");
       tool.show(12);
       tool.show(12.5);
   }
   ```

   

## 基本语法  

### 变量  

`数据类型 变量名 = 值`，前述语句完成了声明及赋值，其实质相当于 `数据类型 变量名 = new 数据类型 (){}`，后者是前者的细化

<font color=limegreen>值可以是一个量值，也可以是一个实例(对象)，所以我们发现A.创建对象的语法规则;B.定义数组变量;C.泛型定义也遵循上面的等式，一切都是对象。究其原因就是所有的量值、实例、对象都是通过类进行定义的，无论是基本数据类型，还是引用数据类型都是如此，数据类型=类</font>  

```java
Puppy myPuppy = new Puppy( "tommy" );
// 数据类型: Puppy类，类也是数据类型的一种
// 变量名： myPuppy
// new：构建值(实例)
// 数据类型：构建值(实例)，Puppy类
// (): 构建值(实例)，调用构造方法，传入参数tommy
// {}: 构建值(实例)，临时定义类的属性或方法
int[] a = new int[]{1,2,3,4}
// 数据类型: int[]，数组，我们可以看到数组数据类型的定义与泛型定义几乎一致，采用基础数据类型+封闭符号对数据类型进行约束，此处的基础数据类型是int, 封闭符号是[]，约束是：1.这是个集合 2.集合的元素必须为int
// 变量名： a
// new：构建值(实例)
// 数据类型：构建值(实例)，int[]，数组
// (): 构建值(实例)，此处表明被调用的构造方法无需参数，即被调用的构造方法是缺省的/默认的
// {}: 构建值(实例)，临时定义类的属性或方法，此处定义了类包含有1，2，3，4等常量
ObjectTool<Integer> objectTool = new ObjectTool<>();
// 数据类型: ObjectTool<>，带泛型的ObjectTool类，因为类也是数据类型的一种，采用基础数据类型+封闭符号对数据类型进行约束，此处的基础数据类型是ObjectTool, 封闭符号是<>，约束是：1.这是个集合类，且集合类中的元素类型待明确 2.这个集合类必须为ObjectTool
// 变量名： objectTool
// new：构建值(实例)
// 数据类型：构建值(实例)，ObjectTool<>，带泛型的ObjectTool类
// (): 构建值(实例)，此处表明被调用的构造方法无需参数，即被调用的构造方法是缺省的/默认的
// {}: 构建值(实例)，临时定义类的属性或方法，此处没有定义
List<String> list = new ArrayList<String>() {
            {
                add("a");
                add("b");
            }
        };
// 数据类型: List<String>，带泛型的List类，因为类也是数据类型的一种，采用基础数据类型+封闭符号对数据类型进行约束，此处的基础数据类型是List, 封闭符号是<>，约束是：1.这是个集合类，且集合类中的元素类型已明确为String 2.这个集合类必须为List
// 变量名： list
// new：构建值(实例)
// 数据类型：构建值(实例)，ArrayList<String>，带泛型的ArrayList类
// (): 构建值(实例)，此处表明被调用的构造方法无需参数，即被调用的构造方法是缺省的/默认的
// {}: 构建值(实例)，临时定义类的属性或方法，此处动态增加了两个方法

// 由后面两个例子可知，等号前后的数据类型可以不一致，但必然呈现继承/包含/强化等关系，这些关系可使之视作相同的数据类型，如ObjectTool<Integer>是ObjectTool<>的强化，ArrayList<String>是List<String>的继承
```



1. 数据类型  

   基本数据类型：

   - 整数类型（byte，short，int，long）
   - 浮点类型（float，double）
   - 字符型（char）
   - 布尔型（boolean)

   引用数据类型：

   - 类（class）
   - 接口（interface）
   - 数组(特别提醒String为引用类型)

   基本类型存储的是数据的本身，引用类型存储的是保存数据的空间地址

2. 11111



### 数组  

1. 声明: 数组类型[] 数组名称，或者： 数组类型 数组名称[] ，例：int [] a; 

2. 分配空间：数组名称=new 数组类型[数组长度]，例：a=new int[5]; 可以把前两个步骤合并：int a=new int[5];

3. 赋值：a[0]=1；

   可以把上述3个步骤合并： int[] a=new int[]{1,2,3,4}

### 方法  

`修饰符 返回值类型 方法名（参数）{
方法体
}`

```java
public int show(int a,int b){
int sum;
sum=a+b;
return sum;
}
```

### 类  

`修饰符 class 类名{}`  

```java
//创建一个名为computer的类
public class computer {
    //类的属性（也叫成员变量）
    String brand;
    int price;
    String type;

    //类的方法
    public void playGame(){
        System.out.println("使用电脑打游戏");
    }
    public void netPlay(){  
        System.out.println("使用电脑上网!"+"brand:"+brand+" price:"+price+" type:"+type);
    }

}

//实例化类
public class InitailComputer {
    public static void main(String[] args){
        //使用computer类进行创建computer对象，new computer() 就是实例化
         computer computer=new computer();、
         //调用方法
         computer.netPlay();
    }
}
```
