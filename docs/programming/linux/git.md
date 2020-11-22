
Table of Contents
=================

   * [Git](#git)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [定义](#定义)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理过程](#基本概念架构与处理过程)
         * [second-class title](#second-class-title)
      * [常用操作](#常用操作)

Created by ALTA
# Git  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [git pull 命令](https://www.yiibai.com/git/git_pull.html)  
2. [github平台如何回退代码到历史指定版本](https://blog.csdn.net/ccorg/article/details/80115408)  
3. [git撤销](https://blog.csdn.net/YoungStunner/article/details/78696763)  
4. [Git](https://github.com/magnumwm/aqumon_doc/blob/master/tech_session/git/git.md)  

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

## 定义  

Left blank

## 问题背景  

Left blank

## 基本概念、架构与处理过程  

### second-class title  

1. Number-prefix class  
   - Symbol-prefix class

## 常用操作  

- 如何避免每次提交输密码  
- 1. git clone 采用`ssh`；
  2. 保存` .git-credentials`文件，然后`git config --global credential.helper store`  
- git stash  
- 1. 添加stash: ` git stash push -m 'hhhhh'`，恢复指定stash; `git stash apply stash@{0}`, 删除指定stash: `git stash drop stash@{1} `，显示stash内容： `git stash show  stash@{$num}  -p`  
- 撤销推送至github的commit  
- 1. git log查询版本的ID ，用于回退使用  
  2. 恢复历史版本： `git reset --hard fae6966548e3ae`  
  3. 修改推到远程服务器: `git push -f -u origin master`  
  4. 重新更新: `git pull`  
- git合并冲突，想恢复至远程分支  
- 1. `git fetch --all`，git fetch 只是下载远程的库的内容，不做任何的合并  
  2. `git reset --hard origin/master`， master为想恢复的分支  
- 