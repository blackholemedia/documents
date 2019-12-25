
Table of Contents
=================

   * [Python Notes](#python-notes)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [杂乱的知识点](#杂乱的知识点)
         * [查询模块帮助文档](#查询模块帮助文档)

Created by ALTA
# Python Notes  


## 阅读说明  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用

## 杂乱的知识点  


###方法定义中(def)的冒号限制类型(或 ->)  

仅仅相当于注释，不强制检查

### 查询模块帮助文档  

1. 先导入模块，再查询普通模块的使用方法， `help(module_name)`
2. 先导入sys，再查询系统内置模块的使用方法，`sys.bultin_modulenames`
3. 查看模块下所有函数，`dir(module_name)`
4. 查看模块下特定函数，`help(module_name.function_name)`
5. 查看函数信息的另一种方法，`print(func_name.__doc__)`


