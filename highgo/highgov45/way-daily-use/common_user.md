---
title: "22、限制普通用户访问其他数据库权限修改"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/common_user.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 限制普通用户访问其他数据库权限修改

## 1、问题描述

```
highgo=# create user a with password 'xxxxxxxx'; --创建a用户
CREATE ROLE
highgo=# create database db_a with owner a;   --创建数据库db_a，owner为用户a
CREATE DATABASE
highgo=# create user b with password 'xxxxxxxx'; --创建b用户
CREATE ROLE
highgo=# create database db_b with owner b;   --创建数据库db_b，owner为用户b
CREATE DATABASE
highgo=# \q

[highgo@localhost etc]$ psql -U a -d db_b    --用户a连接数据库db_b
Password for user a: 
psql (6.0.1)
PSQL: Release 6.0.1
Type "help" for help.
db_b=> create table by_a (id int);       --执行创建表操作成功。insert、update、drop经测试也可正常执行。
CREATE TABLE
```

非超级用户a为什么可以连接任何数据库db\_b，不仅可以连接还可以在public模式下面创建自己的object并对其执行增删改查等操作。

## 2、问题分析

这其实是由瀚高数据库的逻辑结构决定的，在瀚高数据库中逻辑结构有4层：实例（集簇）→数据库→schema→数据库对象。一个数据库集簇下面可以有多个数据库，每个数据库可以有多个schema，每个schema又可以有多个数据库对象，包括table、view、function等。他与oracle不同的是用户并属于逻辑结构中的任何一层，是独立之外的object，他不属于某个数据库或者schema，在瀚高数据库中库与用户没有直接的关联关系，所以会出现上面的权限疑问。

## 3、问题解决

当然我们仍然可以通过权限操作来实现我们想要的效果，使数据库只有超级用户、属主用户可以连接，排除安全隐患。

```
revoke all on database db_b from public; --此处public代表所有普通用户。
```

如果后期又想赋予该权限，可以执行以下逆命令。

```
grant all on database db_b to public;
```