---
title: "8、常用的表空间维护语句"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/maintenance.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 常用的表空间维护语句

## 1、文档用途

本文档列出了常用的表空间维护语句，包括创建、修改、删除操作。

## 2、详细信息

create tablespace注册一个新的集簇范围的表空间，表空间的名称必须与数据库集簇中现有的任何表空间名称不同。表空间允许超级用户在文件系统上定义一个存放位置，可以把数据库对象（例如表和索引等）的数据文件放在该位置。

### （1）创建表空间

创建表空间之前，首先确保HighGo DB服务器必须启动并运行。创建表空间的用户必须具备create tablespace权限或超级用户权限。

```
--在指定位置创建一个表空间tabspace_test，执行语句前，需要先创建目录/data/tabspace_test

CREATE TABLESPACE tabspace_test OWNER username LOCATION '/data/tabspace_test';
```

### （2）更改表空间定义

alter tablespace可以用于更改表空间的定义。要更改表空间，必须是表空间的属主。要更改表空间的属主，必须先创建该用户。

```
--修改表空间的名称

alter tablespace tablespace_name rename to new_tablespace_name;

--修改表空间的属主，新用户必须是已存在用户

alter tablespace tablespace_name owner to new_owner;
```

### （3）删除表空间

一个表空间只能被其拥有者或超级用户删除。在表空间被删除前，必须保证数据库中没有对象在使用该表空间。如果有活动会话使用该表空间作为临时表空间，也会drop失败。

```
--删除表空间

drop tablespace tablespace_name;

--删除不存在的表空间时不报错

drop tablespace if exists tablespace_name;
```