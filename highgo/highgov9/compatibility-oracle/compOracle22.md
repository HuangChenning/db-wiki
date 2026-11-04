---
title: DBLINK
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle22.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## DBLINK

## 说明

瀚高数据库管理系统V9.0支持创建私有、公共、共享数据库链接:

1、私有数据库链接

在本地数据库中的特定schema中创建链接。只有schema中私有数据库链接或PL/SQL子程序的所有者才能使用此链接访问相应远程数据库中的数据对象。

此链接比公共或全局链接更安全，因为只有专用链接的所有者或同一schema中的子程序才能使用该链接访问远程数据库。

2、公共数据库链接

创建数据库范围内的链接。数据库中的所有用户和PL/SQL子程序都可以使用该链接访问相应远程数据库中的数据库对象。当许多用户需要远程Oracle数据库的访问路径时，可以为数据库中的所有用户创建单个公共的数据库链接。

3、共享数据库链接

要创建共享数据库链接，需要在CREATE DATABASE LINK 语句中使用关键字 SHARED。

4、管理数据库链接

管理数据库连接，包括关闭和删除数据库链接，如果你在会话中访问数据库链接，则该链接将保持打开状态，直到您关闭会话为止。要手动关闭数据库链接，请使用ALTER SESSION CLOSE DATABASE LINK语句。

链接打开是指通过该链接访问的每个远程数据库上都有一个进程处于活动状态。关闭会话后，会话中处于活动状态的链接将自动关闭。可以手动关闭链接。

要关闭链接，请发出以下语句，其中 linkname 指链接的名称：

ALTER SESSION CLOSE DATABASE LINK linkname;

删除数据库链接

你可以删除数据库链接，就像删除表或视图一样。 如果链接是私有的，那么它必须位于schema中。

语法如下，其中dblink是链接的名称：

DROP \[PUBLIC\] DATABASE LINK dblink;

注：不支持loongarch、mips和申威处理器架构平台下运行该功能。

## 示例

\--假设在oracle服务器上存在表t2，t3

\--执行远程查询数据操作

create public database link oratest connect to oratestuser

identified by “123456”

using ‘(DESCRIPTION =

(ADDRESS = (PROTOCOL = TCP)(HOST = 192.168.21.137)(PORT = 1521))

(CONNECT\_DATA =

(SERVER = DEDICATED)

(SERVICE\_NAME = XE)

))’ with ‘oracle\_fdw’;

\-- access remote table t2, t3

select \* from t2@ofuplnk1;

select \* from t3@ofuplnk1;

\--修改dblink用户密码

alter public database link oratest connect to oratestuser identified by ‘hello@123’;

\--删除dblink

drop public database link oratest;