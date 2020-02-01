
Table of Contents
=================

   * [标准项目结构](#标准项目结构)
      * [server目录](#server目录)
         * [/boot目录](#boot目录)
         * [/model](#model)
         * [config.json](#configjson)
         * [datasource.json](#datasourcejson)
         * [model-config.json](#model-configjson)
         * [middleware.json](#middlewarejson)
         * [server.json](#serverjson)
         * [component-config.json](#component-configjson)
      * [/client目录](#client目录)
         * [README](#readme)
         * [HTML静态文件](#html静态文件)
      * [/common目录](#common目录)
         * [models目录](#models目录)

Created by [I am your father]
# 标准项目结构  
## server目录  

### /boot目录  

应用初始化脚本  

1. root.js指定根目录url的路由信息
2. 此目录也可以添加脚本以实现url + view函数

### /model 

仅与server相关的model  

### config.json  

应用配置文件，类似于django的settings  

### datasource.json  

数据源配置文件，包含数据库账号端口等信息，django是包含在settings里面

### model-config.json  

模型配置文件，将模型字段定义与上述定义的数据库相连接, 作用类似django中model的class __META__  ,但仅指定模型使用哪个数据库，具体到哪个表仍需要在model的json文件里面定义

### middleware.json  

中间件配置信息，可用于指定静态文件位置, django 是包含在settings里面  

### server.json  

应用主程序，类似于django下的manage

### component-config.json  

指定需要装载的loopback component  

## /client目录  

### README  

### HTML静态文件  

## /common目录  

主要存放server和client共享的文件

### models目录 

通常为自定义的models,类似于django里面的models，每个模型都包含json和js文件，json为字段定义(类似于django的model，外键和访问控制也在此处定义)，js为类似于django的url + view函数

