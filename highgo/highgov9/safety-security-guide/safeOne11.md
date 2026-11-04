---
title: "闪回"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne11.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 闪回

随着数据库应用的日益复杂，数据恢复和错误纠正的需求不断增加。传统备份恢复和PITR（Point-In-Time  
Recovery）等手段在恢复速度和灵活性上存在不足。为了快速恢复因误操作导致的数据丢失或损坏，提高数据库的可用性和可靠性，瀚高数据库提供了闪回查询和闪回表功能。

支持基于时间戳的闪回查询功能，支持用户查询指定历史时刻的数据；实现闪回表功能，允许用户将表恢复到指定时间点的状态。允许用户将表恢复到DROP/TRUNCATE操作前的状态。用户能够在秒级时间内恢复误操作前的数据，提升数据库的容错能力和数据恢复效率。

闪回查询功能是V9.0.5版本新增功能。本模块仅支持在oracle兼容模式下进行闪回查询和闪回恢复操作。

## 闪回的特点

高效恢复：通过闪回查询和闪回表功能，用户可以在秒级时间内恢复误操作前的数据，大大缩短了数据恢复时间。

灵活查询：支持基于时间戳的闪回查询，其中时间戳可以使用常量或表达式。

数据完整性：在恢复过程中，确保数据的完整性和一致性，避免因恢复操作导致的数据损坏。

兼容性：与现有数据库系统无缝集成，不影响现有业务的正常运行，不影响现有数据库系统的性能。

## 闪回的约束

- 闪回查询和闪回表到某时间点的功能需要获取事务与时间的对应关系，因此需要提前开启记录事务提交时间的参数track\_commit\_timestamp。
- 闪回查询和闪回表到某时间点的功能依赖于历史数据的保留，因此需要合理设置vacuum\_defer\_cleanup\_age设置保留旧元组的事务数量的参数，以确保有足够的历史数据可供恢复。
- 闪回表到DROP操作之前仅支持restrict模式的操作，回收对象也仅支持表本身及依赖于它的toast表，索引。
- 闪回表到TRUNCATE操作之前仅支持restrict模式的操作，回收对象也仅支持表本身和依赖于它的toast表。不支持对trigger的处理，不支持重置sequence的情况。

## 闪回查询

在SELECT语句中使用新增的AS  
OF关键字指定特定的时间，可以使查询从表中获取到指定时间状态下的历史数据。该功能需要提前开启记录事务提交时间的参数track\_commit\_timestamp，并设置保留旧元组的事务数量的参数vacuum\_defer\_cleanup\_age到合适值。

语法：

```
SELECT [ * | expression ] [ FROM from_item [AS OF time_expr ] ]
```

参数说明：

- expression
	给定表达式
- from\_item

其中 from\_item 可以是以下之一：

```
[ ONLY ] table_name [ * ] [ [ AS ] alias [ ( column_alias [,
...] ) ] ]

[ TABLESAMPLE sampling_method ( argument [, ...] ) [ REPEATABLE (
seed ) ] ]

[ LATERAL ] ( select ) [ AS ] alias [ ( column_alias [, ...] )
]

with_query_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]

[ LATERAL ] function_name ( [ argument [, ...] ] )

[ WITH ORDINALITY ] [ [ AS ] alias [ ( column_alias [, ...] )
] ]

[ LATERAL ] function_name ( [ argument [, ...] ] ) [ AS ] alias
( column_definition [, ...] )

[ LATERAL ] function_name ( [ argument [, ...] ] ) AS (
column_definition [, ...] )

[ LATERAL ] ROWS FROM( function_name ( [ argument [, ...] ] ) [
AS ( column_definition [, ...] ) ] [, ...] )

[ WITH ORDINALITY ] [ [ AS ] alias [ ( column_alias [, ...] )
] ]

from_item [ NATURAL ] join_type from_item [ ON join_condition |
USING ( join_column [, ...] ) ]
```
- time\_expr
	可以是timestamptz常量字符串，或返回结果为timestamptz类型的表达式。

使用示例：

示例1使用常量，闪回到指定时间点：

```
[highgo@node1 bin]$ ./psql highgo highgo -p 1521

用户 highgo 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=# create table test (id int);

CREATE TABLE

highgo=# insert into test values(11),(22),(33);

INSERT 0 3

highgo=#

highgo=# select now();

now

------------------------------

2025-11-19 18:44:16.30766+08

(1 行记录)

highgo=# insert into test values(100);

INSERT 0 1

闪回到指定时间点

highgo=# select * from test as of '2025-11-19 18:44:16.30766+08';

id

----

11

22

33

(3 行记录)

示例2使用表达式闪回查询：

highgo=# select * from test as of now() - interval '100' second;
```

## 闪回表

闪回查询功能不支持恢复已被删除的表，我们增加新的语法，可以支持将表中的数据恢复到指定时间点的状态；也可以恢复被DROP/TRUNCATE操作后的表。

### 新增系统表

系统表pg\_recyclebin用以存储可回收对象的信息：

---

| 列类型 | 列名称 | 描述 |
| --- | --- | --- |
| Oid | oid | 为回收对象自动生成的唯一oid |
| Oid | rcybaseid | 回收对象所依赖的基表在pg\_recyclebin表中的id，引用pg\_recyclebin.oid |
| Oid | rcyrelid | 对象的relation id |
| NameData | rcyname | 为回收对象生成的唯一名称 |
| NameData | rcyoriginname | 对象原始的名称 |
| char | rcyoperation | 操作类型：’t’ = TRUNCATE, ‘d’ = DROP |
| int16 | rcytype | 对象的类型：0 table, 1 index, 2 toast table, 3 toast index |
| timestamptz | rcyrecycletime | 对象被回收的时间 |
| Oid | rcynamespace | 对象所属的namespace的oid |
| Oid | rcytablespace | 对象所属的tablespace的oid |
| Oid | rcyrelfilenode | 对象被回收的filenode的oid |

---

### 新增参数

新增GUC参数ivorysql.enable\_recycle\_bin用于支持闪回表到DROP|TRUNCATE操作前，参数取值为on或off，参数立即生效。所有用户有权限设置该参数。

```
highgo=# set ivorysql.enable_recycle_bin=on;

SET
```

### 闪回表数据到指定时间点

闪回表数据到指定的时间点（前提是表未被删除），该功能需要提前开启数据库自带参数track\_commit\_timestamp，设置参数vacuum\_defer\_cleanup\_age（设置保留旧元组的事务数量）到合适值：

语法：

```
FLASHBACK TABLE table_name TO TIMESTAMP time_expr;
```

参数说明：

- table\_name
	表名称
- time\_expr
	可以是timestamptz常量字符串，或返回结果为timestamptz类型的表达式

### 闪回表到DROP操作前

闪回表到drop操作之前，该功能需要开启参数ivorysql.enable\_recycle\_bin。语法：

```
FLASHBACK TABLE table_name TO BEFORE DROP [RENAME TO new_tablename];
```

参数说明：

- table\_name
	表名称
- new\_tablename
	闪回表的新名称

### 闪回表到TRUNCATE操作前

闪回表到truncate操作之前，该功能需要开启参数ivorysql.enable\_recycle\_bin。语法：

```
FLASHBACK TABLE table_name TO BEFORE TRUNCATE;
```

参数说明：

- table\_name
	表名称

### 清理表对象的历史数据

清理表对象的历史数据：

语法一：

```
PURGE [RECYCLEBIN | TABLE table_name];
```

参数说明：

- table\_name
	表名称

使用purge table  
语句清除指定表关联的对象，每次执行清理对应表最旧的一个版本的垃圾数据；只有超级用户有权限执行PURGE  
RECYCLEBIN，普通用户只能PURGE有权限的表。

使用purge recyclebin时清空整个回收站。

语法二：

```
DROP TABLE table_name [RESTRICT|CASCADE] [PURGE]
```

为DROP语法增加了可选的PURGE子句，可以使DROP操作不记录回收站。

示例：

```
PURGE TABLE foo;

PURGE RECYCLEBIN;

DROP TABLE foo PURGE;
```

### 闪回恢复使用

首先查参数是否启用，注意登录1521端口：

```
[highgo@node1 bin]$ ./psql highgo highgo -p 1521

用户 highgo 的口令：

psql (14.20)

hgdb-client-V9.0.5

输入 "help" 来获取帮助信息.

highgo=# show track_commit_timestamp ;

track_commit_timestamp

------------------------

on

(1 行记录)

highgo=# show vacuum_defer_cleanup_age ;

vacuum_defer_cleanup_age

--------------------------

100

(1 行记录)

highgo=# show ivorysql.enable_recycle_bin ;

ivorysql.enable_recycle_bin

-----------------------------

on

(1 行记录)
```

2.创建测试表并插入数据：

```
highgo=# create table test (id int,name text);

CREATE TABLE

highgo=# create index test_in on test (id);

CREATE INDEX

highgo=# insert into test values(1,'flashback');

INSERT 0 1

highgo=# select now();

now

-------------------------------

2025-11-20 18:15:20.617875+08

(1 行记录)

highgo=# insert into test values(2,'query');

INSERT 0 1

highgo=#

3.闪回到指定时间点：

highgo=# flashback table test to timestamp '2025-11-20 18:15:20.617875+08';

FLASHBACK

highgo=# select * from test;

id | name

----+-----------

1 | flashback

(1 行记录)

highgo=# flashback table test to timestamp now()- interval '200'
second;

FLASHBACK

highgo=# select * from test;

id | name

----+-----------

1 | flashback

2 | query

(2 行记录)

highgo=# truncate table test;

TRUNCATE TABLE

highgo=# select * from test;

id | name

----+------

(0 行记录)

4.检查回收站：

highgo=# select * from pg_recyclebin ;

5.闪回恢复到truncate操作前：

highgo=# flashback table test to before truncate;

FLASHBACK

highgo=# select * from test;

id | name

----+-----------

1 | flashback

2 | query

(2 行记录)

highgo=# drop table test;

DROP TABLE

highgo=# select * from pg_recyclebin ;

6.闪回恢复到drop操作之前：

highgo=# flashback table test to before drop rename to testnew;

FLASHBACK

highgo=# select * from testnew;

id | name

----+-----------

1 | flashback

2 | query

(2 行记录)
```