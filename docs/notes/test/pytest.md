
Table of Contents
=================

   * [Pytest基础](#pytest基础)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [pytest的测试文件的发现顺序](#pytest的测试文件的发现顺序)
      * [建议的项目布局](#建议的项目布局)
         * [测试代码与应用代码(application code)分离](#测试代码与应用代码application-code分离)

Created by ALTA
# Pytest基础  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. [Good Integration Practices](<https://docs.pytest.org/en/latest/goodpractices.html>)



## pytest的测试文件的发现顺序  

1. 如果指定命令行参数，从命令行参数路径查询
2. 无命令行参数则从 [`testpaths`](https://docs.pytest.org/en/latest/reference.html#confval-testpaths) (if configured，可从ini中配置)或当前路径查询
3. 上述路径中递归查询`test_*.py`和`*_test.py`文件，通过他们的[test package name](https://docs.pytest.org/en/latest/goodpractices.html#test-package-name)导入
4. 从第3步导入的文件中查找前缀为test的函数/方法，或前缀为Test的类(类内不包含`__init__`方法)

## 建议的项目布局  

### 测试代码与应用代码(application code)分离  

```markdown
setup.py
mypkg/
    __init__.py
    app.py
    view.py
tests/
    test_app.py
    test_view.py
    ...
```


