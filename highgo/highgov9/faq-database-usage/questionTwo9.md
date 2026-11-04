---
title: "时间类型不正确"
book: "数据库使用类"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/question/questionTwo9.html"
tags:
  - highgo
  - highgo-v9
  - faq-database-usage
---

#### 1、问题描述

应用与数据的日期值存在差异  
**具体表现**

#### 2、问题排查

###### 1）数据库日志

![questionTwo9-3](img/questionTwo9-3.png)

###### 2）排查程序

查询历史显示均存在时差  
查询源库数据正常  
查询迁移后数据存在时间差异  
排查数据库参数

```sql
alter system set nls_date_format to 'YYYY-MM-DD HH24:MM:SS';
```

#### 3 解决方案

修改参数

```sql
alter system set nls_date_format to 'YYYY-MM-DD HH24:MI:SS';
```