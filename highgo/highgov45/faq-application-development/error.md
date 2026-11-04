---
title: "2、调用序列插入数据时报权限不足-报错:对于序列“seq_xxl_job_xxx”权限不足"
book: "开发应用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/question/error.html"
tags:
  - highgo
  - highgo-v45
  - faq-application-development
---

## 调用序列插入数据时报权限不足

## 1、问题现象

自增主键调用序列，在插入数据时报错：对于序列“seq\_xxl\_job\_xxx”权限不足。

## 2、解决方案

查看序列所有者：

```
highgo=# ds seq_a
         List of relations
 Schema | Name  |   Type   | Owner  
--------+-------+----------+-------
 public | seq_a | sequence | sysdba
(1 row)
```

所有者登录，进行赋权：

```
grant usage on SEQUENCE seq_name to PUBLIC;
```