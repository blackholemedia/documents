
Table of Contents
=================

   * [Loopback](#loopback)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [标准项目结构](#标准项目结构)
         * [server目录](#server目录)
         * [client目录](#client目录)

Created by ALTA


## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1.   

   

## 标准项目结构  
### server目录  
1. /boot目录  

   应用初始化脚本  

   - root.js指定根目录url的路由信息
   - 此目录也可以添加脚本以实现url + view函数

2. /model 

   仅与server相关的model  

3. config.json  

   应用配置文件，类似于django的settings  

4. datasource.json  

   数据源配置文件，包含数据库账号端口等信息，django是包含在settings里面

5. model-config.json  

   模型配置文件，将模型字段定义与上述定义的数据库相连接, 作用类似django中model的class __META__  ,但仅指定模型使用哪个数据库，具体到哪个表仍需要在model的json文件里面定义

6. middleware.json  

   中间件配置信息，可用于指定静态文件位置, django 是包含在settings里面  

7. server.json  

   应用主程序，类似于django下的manage

8. component-config.json  

   指定需要装载的loopback component  

### client目录  

1. README

2. HTML静态文件  

3. /common目录

   主要存放server和client共享的文件

4. models目录 

   通常为自定义的models,类似于django里面的models，每个模型都包含json和js文件，json为字段定义(类似于django的model，外键和访问控制也在此处定义)，js为类似于django的url + view函数

