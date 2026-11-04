---
title: DBLINK
book: "SQL 基础实践"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/sql-dev/practice-dblink.html
tags:
  - dameng
  - dm8
  - sql-practice
---

本章节主要介绍在 DM 数据库中数据库链接的使用。

## 一、适用场景

| 软件 | 版本 |
| --- | --- |
| 操作系统 | Redhat 7 及以上版本 |
| DM 数据库 | DM 8.0 及以上版本 |
| CPU 架构 | x86、ARM、龙芯、飞腾等国内外主流 CPU |

## 二、操作方法

### 2.1 数据库链接创建与使用

数据库链接对象 (LINK) 是 DM 中的一种特殊的数据库实体对象，它记录了远程数据库的连接和路径信息，用于建立与远程数据的联系。

- 同构数据库链接—DM 到 DM

创建 DM 到 DM 的数据库链接，并使用数据库链接对远程库做增、删、改、查操作。

> **注意**
> 
> 准备两台数据库服务器 A、B（目前只支持同平台，不支持跨平台建数据库连接），均安装了 DM 数据库，网络必须互通。

两台服务器，其中一个为目的主机 A，另一个为测试机 B；分别在这两台服务器上进入数据库安装目录下的库目录里修改 dm.ini 文件： `MAL_INI=1` ， **实例名 INSTANCE\_NAME 要对应** ，且配置 dmmal.ini（如无此文件，新建此文件）如下所示：

```sql
[mal_inst1]
mal_inst_name  = DMSERVER     --A的实例名
mal_host       = 127.0.0.1   --A的ip
mal_port       = 5282
[mal_inst2]
mal_inst_name  = DMSERVER2            --B的实例名
mal_host       = 127.0.0.1  --B的ip
mal_port       = 5283
```

> **注意**
> 
> A 和 B 的实例名不能一样；–中文注释部分只是方便解释含义，配置 dmmal.ini 时不必写，以免造成格式问题导致 dmserver 服务无法启动。 两台主机的 dmmal.ini 文件相同。配置成功之后分别重启 dmserver DM 数据库服务。

在主机 A 上建表 test，如下所示：

```sql
CREATE TABLE TEST(C1 INT,C2 VARCHAR(20));
```

在 B 上建立到 A 的数据库链接 LINK01，使用链接进行插入、更新和删除操作。如下所示：

```sql
CREATE PUBLIC LINK LINK01 CONNECT WITH SYSDBA IDENTIFIED BY ***** USING '127.0.0.1/5282';

INSERT INTO TEST@LINK01 VALUES(1,'A');
INSERT INTO TEST@LINK01 VALUES(2,'B');
UPDATE TEST@LINK01 SET C2='C' WHERE C1=1;
DELETE FROM TEST@LINK01 WHERE C1=2;

COMMIT;
```

在 B 上查询 A 服务器上表 test 的数据。如下所示：

```sql
select * from TEST@LINK01;
```

输出结果：

- 异构数据库链接 DM 到 Oracle
```sql
--DM 到 Oracle 的数据库连接创建
CREATE LINK LINK1 CONNECT 'ORACLE' WITH USER01 IDENTIFIED BY USER01PASSWD USING '127.0.0.1/orcl';
```

DM 到 Oracle 的数据库连接使用方法同 DM 到 DM 数据库连接。

- 数据库链接删除
```sql
--删除数据库链接 LINK1。
DROP LINK LINK1;
```

> **注意**
> 
> 1、数据库连接目前只支持 DM、Oracle 或 ODBC。  
> 2、DM-DM 的同构数据库链接不支持 MPP 环境，DM 与异构数据库的数据库链接支持 MPP 环境。  
> 3、增删改不支持 INTO 语句。  
> 4、不支持使用游标进行增删改操作。  
> 5、不支持操作远程表的复合类型列。  
> 6、DBLINK 理论上不支持 LOB 类型列的操作，但支持简单的增删改语句中使用常量来对 LOB 类型列进行操作。

## 三、参考文献

更多 SQL 语言使用说明，请参考《DM\_SQL 语言使用手册》，手册位于 **数据库安装路径** `/dmdbms/doc` 文件夹下。如有其他问题，请在 [社区](https://eco.dameng.com/community/question?_blank) 内咨询。