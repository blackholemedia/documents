
Table of Contents
=================

   * [Linux学习笔记](#linux学习笔记)
      * [参考引用](#参考引用)
      * [帮助命令](#帮助命令)
         * [帮助文档基本说明](#帮助文档基本说明)
         * [whatis](#whatis)
         * [内部命令（builtin）与外部命令](#内部命令builtin与外部命令)
         * [查看内部命令使用方法](#查看内部命令使用方法)
         * [查看外部命令使用方法](#查看外部命令使用方法)
         * [man中的字段说明](#man中的字段说明)
         * [man手册查看命令](#man手册查看命令)
         * [man手册章节](#man手册章节)
      * [查找命令](#查找命令)
         * [find](#find)
         * [locate](#locate)
         * [which](#which)
         * [whereis](#whereis)
         * [type](#type)
      * [其他常用命令](#其他常用命令)
      * [常见LINUX根目录结构](#常见linux根目录结构)

Created by ALTA
# Linux学习笔记  

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站：

1. 11  

   

## 帮助命令  

### 帮助文档基本说明  

1. [] 可选内容  
2. <> 必选内容
3. a | b 二选一
4. { } 分组
5. ... 同一内容可出现多次

Some options will have a limited list of choices. A list of choices will be comma seperated and put between braces.

```shell
{choice1,choice2}
{yes,no}
```

### whatis  

输入“whatis echo”，会显示如下信息。每行包含三部分，第一部分是命令名称；第二部分是命令在man手册出现的位置，第三部分是简述命令或函数的作用

```shell
>>>whatis echo
>>>echo (1) - display a line of text
```

如果想详细了解命令信息，可以输入如下命令：

```shell
>>>man 1 echo 或者 man echo(仅当数字为1时候可省略，其他数字不可省略)
```

### 内部命令（builtin）与外部命令  

man bash：   NAME字段后面的命令都是内部命令

### 查看内部命令使用方法  

1. help COMMAND  显示COMMAND这个命令的用法
2. man help 显示所有内部命令列表及使用方法

### 查看外部命令使用方法  

1. COMMAND  --help

```shell
>>>bash –-help  //部分命令，也可以简写为COMMAND -h
```

2. man COMMAND  原始格式为：man [章节] COMMAND，默认第1章省略  
3. info COMMAND

### man中的字段说明  

1. NAME 名称及简要说明

2. SYNOPSIS 用法格式说明

   - 可选内容

   - 必选内容

   - a|b 二选一

   - { } 分组

   - ... 同一内容可出现多次

3. DESCRIPTION 详细说明

4. OPTIONS 选项说明

5. EXAMPLES 示例

6. FILES 相关文件

7. AUTHOR 作者

8. COPYRIGHT 版本信息

9. REPORTING BUGS bug信息

10. SEE ALSO 其它帮助参考

### man手册查看命令  

- q Q ZZ 退出
- g  1g               光标跳至文档首部
- G         光标跳至文档尾部
- e j       文档前进N行
- y k      文档后退N行
- f space 文档前进N页
- b ^B    文档后退N页
-  /pattern n/N 向后查询
-  ?pattern        向前查询
- &pattern     只显示匹配到的行

### man手册章节  

   - User Commands // 用户命令
   - System Calls // 系统调用
   - C Library Functions // C函数库调用
   - Devices and Special Files // 设备文件和特殊文件
   - File Formats and Conventions // 配置文件及格式
   - Games et. Al. // 游戏
   - Miscellanea // 杂项
   - System Administration tools and Deamons // 管理类命令

## 查找命令  

### find  

 find <指定目录> <指定条件> <指定动作>

- <指定目录>： 所要搜索的目录及其所有子目录。默认为当前目录。

- <指定条件>： 所要搜索的文件的特征。

- <指定动作>： 对搜索结果进行特定的处理。

```shell
find . -name ‘my*’ -ls
```

### locate  

locate命令其实是`find -name`的另一种写法，它不搜索具体目录，而是搜索一个数据库（/var/lib/locatedb），这个数据库中含有本地所有文件信息。Linux系统自动创建这个数据库，每天自动更新一次，所以使用locate命令查不到最新变动过的文件。为了避免这种情况，可以先使用updatedb命令手动更新数据库再使用locate  

### which  

which命令的作用是，在PATH变量指定的路径中，搜索某个系统命令的位置，并且返回第一个搜索结果.也就是说，使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令.  

### whereis  

whereis命令只能用于程序名的搜索，而且只搜索二进制文件（参数-b）、man说明文件（参数-m）和源代码文件（参数-s）.如果省略参数，则返回所有信息.  

### type  

type命令其实不能算查找命令，它是用来区分某个命令到底是由shell自带的，还是由shell外部的独立二进制文件提供的。如果一个命令是外部命令，那么使用-p参数，会显示该命令的路径，相当于which命令.

## 其他常用命令  



## 常见LINUX根目录结构  

| 名称       | 作用     | 描述                             |
| --------- | ---------------------------- | ------------------------------------------------------------ |
| bin       | 存放普通用户可执行的指令                             | 即使在单用户模式下也能够执行处理                                                             |
| boot      | 开机引导目录                 | 包括Linux内核文件与开机所需要的文件                          |
| dev       | 设备目录                     | 所有的硬件设备及周边均放置在这个设备目录中                   |
| etc       | 各种配置文件目录             | 大部分配置属性均存放在这里                                   |
| lib/lib64 | 开机时常用的动态链接库       | bin及sbin指令也会调用对应的lib库                             |
| media     | 可移除设备挂载目录           | 类似软盘 U盘 光盘等临时挂放目录      |
| mnt       | 用户临时挂载其他的文件系统   | 额外的设备可挂载在这里,相对临时而言                          |
| opt       | 第三方软件安装目录           | 现在习惯性的放置在/usr/local中                               |
| proc      | 虚拟文件系统                 | 通常是内存中的映射,特别注意在误删除数据文件后，比如DB，只要系统不重启,还是有很大几率能将数据找回来 |
| root      | 系统管理员主目录             | 除root之外,其他用户均放置在/home目录下                       |
| run       | 系统运行是所需文件           | 以前防止在/var/run中,后来拆分成独立的/run目录。重启后重新生成对应的目录数据 |
| sbin      | 只有root才能运行的管理指令   | 跟bin类似,但只属于root管理员                                 |
| snap      | ubunut全新软件包管理方式     | snap软件包一般在/snap这个目录下                              |
| srv       | 服务启动后需要访问的数据目录 |                                                              |
| sys       | 跟proc一样虚拟文件系统       | 记录核心系统硬件信息                                         |
| tmp       | 存放临时文件目录             | 所有用户对该目录均可读写                                     |
| usr       | 应用程序放置目录             |                                                              |







