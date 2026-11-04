---
title: "18、hgdb数据编辑"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HGDB_edit.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## hgdb数据编辑

## 1、介绍

数据编辑（Data Redaction）功能是一种动态数据脱敏机制，针对数据查询时的敏感数据进行动态的安全保护，通过设置策略对表的字段进行动态查询时动态修订。

一个完整的数据编辑策略由三部分组成：数据编辑函数、数据编辑策略应用 SQL命令、相应的权限配置。

使用内置的数据编辑函数；

通过绑定策略语句将函数与目标数据关联；

数据编辑函数及策略仅可通过 SYSSSO 用户创建、修改、删除、禁用、启用、授权操作，普通用户和数据库管理员仅可查看管理视图

在启用数据编辑之前，需打开参数开关：redaction\_policy。可通过命令行或直接修改 conf 文件进行修改。命令行格式如下：

```
alter system set redaction_policy to on;
select pg_reload_conf();
```

## 2、创建编辑策略

语法：

```
CREATE REDACTION POLICY <name> ON <table_name>
[ ADD [ COLUMN ] <column_name>[,…] USING <funcname_clause> ]
[, ...]
[ FOR ( <expression> ) ]
DISABLE/ENABLE；
```

解析：

name：当前策略的名称，

table\_name：当前数据编辑策略作用为哪张表

column\_name：策略应用于哪个列

funcname\_clause：数据编辑函数名称，目前支持的脱敏函数见下文函数列表

expression：表达式，即对哪些用户执行数据编辑策略。比如 user=’u1’，就是对 u1

## 3、示例

```
1）确认参数开启
highgo=> show redaction_policy;
redaction_policy
------------------ on
(1 row)
2）创建测试用户
create user u1 password 'Hello@123';
create user u2 password 'Hello@123';
create user u3 password 'Hello@123';
3）在用户 u3 下创建测试表，并赋予 u1 和 u2 用户 select 权限
\c highgo u3
create table test(id int, col1 varchar,info text);
insert into test values(1,'abc','test');
insert into test values(2,'abcabcabc','testtesttest');
grant select on test to u1,u2;
4）使用 syssso 用户创建数据编辑策略
\c highgo syssso
create redaction policy p1 on test add column col1 using redact_all for (user = ‘u1’);
//该策略仅对 u1 用户生效
5）查看数据
\c highgo u1
select * from test; ----期望查看到 col1 列为脱敏后数据
结果如下：
id | col1 | info
----+-----------+-------------- 1 | xxx | test
2 | xxxxxxxxx | testtesttest
(2 rows)
\c highgo u2
select * from test; -----期望查看到明文
结果如下：
id | col1 | info
----+-----------+-------------- 1 | abc | test
2 | abcabcabc | testtesttest
(2 rows)
6）同时指定多列
由于同一个表只能创建一个数据编辑策略，所以先删掉 p1，再创建：
\c highgo syssso
drop redaction policy p1;
create redaction policy p2 on test add column id using redact_bankcard,add
column info using redact_shuffle for (user = ‘u1’);
即：对列 id 使用 redact_bankcard 函数，列 info 使用 redact_shuffle 函数。
查看数据：
\c highgo u1
select * from test;
结果如下：
id | col1 | info
----+-----------+-------------- 0 | abc | tset
0 | abcabcabc | etststttetse
(2 rows)
//redact_bankcard 函数不支持对 int 类型进行脱敏，所以自动使用 redact_all 对
int 类型进行脱敏，结果为 0。
7）创建数据编辑策略，但是不启用
\c highgo syssso
drop redaction policy p2;
create redaction policy p3 on test add column id using redact_bankcard,add
column info using redact_shuffle for (user = ‘u1’) disable;
查看数据：
\c highgo u1
select * from test;
结果为明文：
id | col1 | info
----+-----------+-------------- 1 | abc | test
2 | abcabcabc | testtesttest
(2 rows)
```

## 4、修改数据编辑策略

```
目前修改策略可使用以下几种方式：
（1）ALTER REDACTION POLICY policyname MODIFY COLUMN colname USING func_name;
修改当前策略中，列 colname 使用的数据编辑函数
（2）ALTER REDACTION POLICY policyname RENAME TO policyname2;
修改当前策略的名字
（3）ALTER REDACTION POLICY policyname DISABLE/ENABLE;
修改当前策略是否启用
（4）ALTER REDACTION POLICY policyname DROP COLUMN colname;
修改当前策略，删除掉其中的某一行数据编辑列
（5）ALTER REDACTION POLICY policyname for (user = ‘username’);
修改当前策略，增加数据编辑表达式
（6）ALTER REDACTION POLICY policyname ADD COLUMN colname USING func_name
修改当前策略，增加数据编辑列
```

## 5、删除数据编辑策略

```
DROP REDACTION POLICY policynamelist
例：
DROP REDACTION POLICY p1;
删除数据编辑策略 p1
DROP REDACTION POLICY p1,p2;
删除数据编辑策略 p1,p2
```

## 6、限制

1、创建策略只能使用 syssso 进行设定，其他用户无权限。

2、一张表中只能创建一个策略

3、一个列只能指定一个数据编辑函数

目前，数据编辑不支持瀚高的特有数据类型，例如： money、bytea、enum、几何

类型、网络地址类型、bit、文本搜索类型、uuid、xml、json、数组类型、组合类型、范

围类型、域类型、oid、pg\_lsn、伪类型和用户自定义类型等。