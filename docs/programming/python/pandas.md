
Table of Contents
=================

   * [Pandas](#pandas)
      * [阅读说明](#阅读说明)
      * [参考引用](#参考引用)
      * [定义](#定义)
      * [问题背景](#问题背景)
      * [基本概念、架构与处理过程](#基本概念架构与处理过程)
         * [second-class title](#second-class-title)
      * [常用工具及函数](#常用工具及函数)
         * [Sample Data](#sample-data)
         * [Let's go](#lets-go)

Created by ALTA
# Pandas  

<font color=#008000>绿色字体</font>代表个人的思考理解，<font color=Yellow>黄色字体</font>代表阅读理解过程中的疑问，<font color=Red>红色字体</font>代表关键重要信息，<u>下划线</u>代表次关键重要信息，`阴影`或 *一般斜体* 均表示引用或强调 

```python
# ---------------------------------- 输出结果
```

## 参考引用  

本文引用及参考自下列文章/网站， 版权归属原作者所有：

1. 111111

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

left blank

## 基本概念、架构与处理过程  

### second-class title  

1. Number-prefix class  
   - Symbol-prefix class



## 常用工具及函数  

### Sample Data  

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'a': np.random.randn(1000),
                    'b': np.random.randn(1000),
                    'N': np.random.randint(100,1000,(1000)),
                    'x':'x'})
```

### Let's go  

1. 读取MySQL   

   ```python
   df = pd.read_sql(query_sql, db_conn, index_col=['report_date', 'uid'], parse_dates=['report_date'])
   ```

2. 创建连续日期序列  

   ```python
   date_range = pd.date_range('20201001', '20201003', freq='D', normalize=True)
   # start_date/end_date: string/date/datetime
   ```

3. 创建多层次索引  

   ```python
   idx = pd.MultiIndex.from_tuples([(day, pid, txn_type)
                                            for day in date_range
                                            for pid in [12, 13, 32, 33]
                                            for txn_type in ['sell', 'buy']
                                            ], names=['report_date', 'pid', 'type'])
   col = ['value', 'timestamp']
   df = pd.DataFrame(0.0, idx, col)
   ```

   output:

   ```python
                         value  timestamp
   report_date pid type                  
   2020-10-01  12  sell    0.0        0.0
                   buy     0.0        0.0
               13  sell    0.0        0.0
                   buy     0.0        0.0
               32  sell    0.0        0.0
                   buy     0.0        0.0
               33  sell    0.0        0.0
                   buy     0.0        0.0
   2020-10-02  12  sell    0.0        0.0
                   buy     0.0        0.0
               13  sell    0.0        0.0
                   buy     0.0        0.0
               32  sell    0.0        0.0
                   buy     0.0        0.0
               33  sell    0.0        0.0
                   buy     0.0        0.0
   2020-10-03  12  sell    0.0        0.0
                   buy     0.0        0.0
               13  sell    0.0        0.0
                   buy     0.0        0.0
               32  sell    0.0        0.0
                   buy     0.0        0.0
               33  sell    0.0        0.0
                   buy     0.0        0.0
   ```

4. 多层次索引和多层次列名相互转换  

   ```python
   df.unstack(level=[1, 2])
   ```

   output:

   ```python
               value                                    timestamp                 
   pid            12        13        32        33             12        13        
   type         sell  buy sell  buy sell  buy sell  buy      sell  buy sell  buy   
   report_date                                                                     
   2020-10-01    0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0       0.0  0.0  0.0  0.0   
   2020-10-02    0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0       0.0  0.0  0.0  0.0   
   2020-10-03    0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0       0.0  0.0  0.0  0.0   
                                    
   pid           32        33       
   type        sell  buy sell  buy  
   report_date                      
   2020-10-01   0.0  0.0  0.0  0.0  
   2020-10-02   0.0  0.0  0.0  0.0  
   2020-10-03   0.0  0.0  0.0  0.0  
   ```
   
恢复原样：
   
```python
   df.stack(level=[1, 2])
   ```
   
5. 以另一个data frame的索引筛选某个data frame， 多层次索引同样适用  

   ```python
   df.loc[df.index.isin(df2.index)]
   ```

6. 分组，并且统计  

   ```python
   df = df.groupby(['report_date', 'pid']).count()
   ```

   output:  

   ```python
                    value  timestamp
   report_date pid                  
   2020-10-01  12       2          2
               13       2          2
               32       2          2
               33       2          2
   2020-10-02  12       2          2
               13       2          2
               32       2          2
               33       2          2
   2020-10-03  12       2          2
               13       2          2
               32       2          2
               33       2          2
   ```

   ```python
   df.groupby(['report_date', 'pid']).apply(sum)
   ```

   output:  

   ```python
                    value  timestamp
   report_date pid                  
   2020-10-01  12     0.0        0.0
               13     0.0        0.0
               32     0.0        0.0
               33     0.0        0.0
   2020-10-02  12     0.0        0.0
               13     0.0        0.0
               32     0.0        0.0
               33     0.0        0.0
   2020-10-03  12     0.0        0.0
               13     0.0        0.0
               32     0.0        0.0
               33     0.0        0.0
   ```

     

7. hhhhhh