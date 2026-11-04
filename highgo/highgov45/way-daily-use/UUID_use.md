---
title: "7、UUID函数的使用"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/UUID_use.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## UUID函数的使用

## 1、问题现象

本文档解决了如何在函数数据库中调用UUID函数已经如何消除“-”显示的方法

## 2、问题原因

1. UUID函数的调用需要通过拓展（extension）来实现。
2. 直接调用UUID函数显示的字符串会通过“-”来连接。

## 3、解决方案

### 3.1 创建并调用

测试环境

```
HighGo Database V4.7 Enterprise Edition Release 4.7.6 - 64-bit Production
```

创建uuid-ossp扩展：

```
highgo=# create extension "uuid-ossp";

日志: 00000: 语句: create extension "uuid-ossp";

CREATE EXTENSION
```

查询uuid-ossp是否创建成功：

```
highgo=# \dx uuid-ossp

List of installed extensions

Name | Version | Schema | Description

-----------+---------+--------+-------------------------------------------------

uuid-ossp | 1.0 | public | generate universally unique identifiers (UUIDs)

(1 row)
```

调用测试：

```
highgo=# select uuid_generate_v4();

uuid_generate_v4

--------------------------------------

36ecc872-5f97-4471-a0e1-31d5e33716ce

(1 row)
```

### 3.2 不同模式下的调用

#### (1)查看所有模式

```
product=# \dn

List of schemas

Name | Owner

----------------+--------

hgdb_catalog | highgo

icp_business | test

oracle_catalog | highgo

public | highgo

test | highgo

(5 rows)
```

#### (2)修改默认模式

```
product=# set search_path = icp_business,public,"$user";

SET

product=# show search_path ;

search_path

-------------------------------

icp_business, public, "$user"

(1 row)
```

#### (3)创建“UUID”

```
product=# create extension "uuid-ossp";

CREATE EXTENSION

product=# \dx uuid-ossp;

List of installed extensions

Name | Version | Schema | Description

-----------+---------+--------------+-------------------------------------------------

uuid-ossp | 1.0 | icp_business | generate universally unique identifiers (UUIDs)

(1 row)
```

#### (4)取消当前模式搜寻路径

```
product=# set search_path = public,"$user";

SET

product=# \dx uuid-ossp;

List of installed extensions

Name | Version | Schema | Description

-----------+---------+--------------+-------------------------------------------------

uuid-ossp | 1.0 | icp_business | generate universally unique identifiers (UUIDs)

(1 row)
```

#### (5)模拟相同问题

```
product=# select uuid_generate_v4();

错误: 42883: 函数 uuid_generate_v4() 不存在

LINE 1: select uuid_generate_v4();

^
HINT: 没有匹配指定名称和参数类型的函数. 您也许需要增加明确的类型转换.
```

#### (6)重新设置模式路径

如果是要永久修改请使用：alter system set search\_path = icp\_business,public,”$user”;

```
product=# set search_path = icp_business,public,"$user";

SET
```

#### (7)重新调用

```
product=# select uuid_generate_v4();

uuid_generate_v4

--------------------------------------

a2b4890a-2d41-4f12-8e5a-b2f68768d3da

(1 row)
```

### 3.3 关于-的显示替换

```
product=# select replace(uuid_generate_v4()::varchar,'-'::varchar,''::varchar);

             replace              

----------------------------------

c520aba1909f4b9097983b00e22a4734

(1 row)

product=# select sys_guid();

             sys_guid             

----------------------------------

446d30950a2551d1a9aed4a03f446ef7

(1 row)
```