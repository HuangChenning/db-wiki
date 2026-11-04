---
title: "to_date函数自动容错问题"
book: "应用开发类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionThree7.html"
tags:
  - highgo
  - highgo-v9
  - faq-application-development
---

#### 问题描述

HighgoV9\_O 中执行：

```java
highgo=# select to_date('202601','yyyymmdd') from dual;
       to_date       
---------------------
 2026-01-01 00:00:00
(1 行记录)
```

Oracle中执行：

```java
SQL> select to_date('202601','yyyymmdd') from dual;
select to_date('202601','yyyymmdd') from dual
               *
第 1 行出现错误:
ORA-01840: 输入值对于日期格式不够长
```

#### 环境信息

操作系统：Linux

数据库版本：HighgoV9\_O

#### 原因分析

在Oracle兼容模式下，to\_date(‘202601’, ‘yyyymmdd’) 这类转换语法存在自动容错机制：当输入的字符串与指定的日期格式不匹配时，系统不会报错，而是自动赋予一个默认值。这种隐式容错容易掩盖编码或格式上的失误，导致不符合预期的错误数据被悄然写入数据库，给数据质量带来潜在风险。

#### 解决方案

HighgoV9版本的数据库提供GUC参数 ivorysql.enable\_standard\_datetime\_parsing\_mode 控制开关，该参数表明是否启用标准日期时间解析。

参数说明：

| **属性** | **描述** |
| --- | --- |
| 参数类型 | STRING |
| 语法 | set ivorysql.enable\_standard\_datetime\_parsing\_mode = on |
| 默认值 | off |
| 可修改 | ALTER SESSION, ALTER SYSTEM |
| 说明 | 是否启用标准日期时间解析 |

```java
alter system set ivorysql.enable_standard_datetime_parsing_mode = 'on';
select pg_reload_conf();

highgo=# select to_date('202601','yyyymmdd') from dual;
错误:  input string is too short for datetime format
```