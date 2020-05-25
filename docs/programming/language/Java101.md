
Table of Contents
=================

   * [template](#template)
      * [first-class title](#first-class-title)
         * [second-class title](#second-class-title)
      * [first-class title](#first-class-title-1)
         * [second-class title](#second-class-title-1)

Created by ALTA
# Template  
## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [泛型](<https://segmentfault.com/a/1190000014120746>)

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

### 数组  

1. 声明: 数组类型[] 数组名称，或者： 数组类型 数组名称[] ，例：int [] a; 

2. 分配空间：数组名称=new 数组类型[数组长度]，例：a=new int[5]; 可以把前两个步骤合并：int a=new int[5];

3. 赋值：a[0]=1；

   可以把上述3个步骤合并： int[] a=new int[]{1,2,3,4}

### 方法  

修饰符 返回值类型 方法名（参数）{
方法体
}

```java
public int show(int a,int b){
int sum;
sum=a+b;
return sum;
}
```

### 类  

修饰符 class 类名{}  

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



### second-class title  

1. Number-prefix class  
   - Symbol-prefix class
   - 