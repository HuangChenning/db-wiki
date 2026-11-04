---
title: "11、如何创建大写的表名"
book: "运维指导类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/big_tablename.html"
tags:
  - highgo
  - highgo-v45
  - way-operations-guide
---

## 如何创建大写的表名

## 1、表名为aaa

```
create table AAA(a int);
```

## 2、使用英文双引号，表名为AAA

```
create table "AAA"(a int);
```

## 3、使用中文双引号，表名为“aaa”

```
create table “AAA”(a int);
```

## 4、结果如下：

```
highgo=# \d
           关联列表
 架构模式   |  名称   |   类型  |  拥有者
----------------+---------+--------+--------
 oracle_catalog | dual      | 视图    | highgo
 public      | AAA       | 数据表  | highgo
 public      | aaa       | 数据表  | highgo
 public      | people    | 数据表  | highgo
 public      | “aaa”     | 数据表  | highgo
(5 行记录)
```