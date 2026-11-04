---
title: "概述"
book: "HGDB SQL命令速查手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/command.html"
tags:
  - highgo
  - highgo-v45
  - develop-sql-command-quick-reference
---

## 1\. 概述

### 1.1. 简介

本文档主要提供瀚高数据库SQL命令的详细使用方法。

### 1.2. SQL命令列表

瀚高数据库支持以下SQL命令。兼容模块相关的命令请查看兼容功能章节的内容。

**SQL命令列表**

| **SQL命令** | **简介** |
| --- | --- |
| ABORT | 中止当前事务 |
| ALTER AGGREGATE | 更改一个聚集函数的定义 |
| ALTER COLLATION | 更改一个排序规则的定义 |
| ALTER CONVERSION | 改变一个转换的定义 |
| ALTER DATABASE | 更改一个数据库 |
| ALTER DEFAULT PRIVILEGES | 定义默认访问特权 |
| ALTER DOMAIN | 更改一个域的定义 |
| ALTER EVENT TRIGGER | 更改一个事件触发器的定义 |
| ALTER EXTENSION | 更改一个扩展的定义 |
| ALTER FOREIGN DATA WRAPPER | 更改一个外部数据包装器的定义 |
| ALTER FOREIGN TABLE | 更改一个外部表的定义 |
| ALTER FUNCTION | 更改一个函数的定义 |
| ALTER GROUP | 更改角色名称或者成员关系 |
| ALTER INDEX | 更改一个索引的定义 |
| ALTER LANGUAGE | 更改一种过程语言的定义 |
| ALTER LARGE OBJECT | 更改一个大对象的定义 |
| ALTER MATERIALIZED VIEW | 更改一个物化视图的定义 |
| ALTER OPERATOR | 更改一个操作符的定义 |
| ALTER OPERATOR CLASS | 更改一个操作符类的定义 |
| ALTER OPERATOR FAMILY | 更改一个操作符族的定义 |
| ALTER POLICY | 更改一条行级安全性策略的定义 |
| ALTER PROCEDURE | 更改一个过程的定义 |
| ALTER PUBLICATION | 修改发布的定义 |
| ALTER ROLE | 更改一个数据库角色 |
| ALTER ROUTINE | 更改一个例程的定义 |
| ALTER RULE | 更改一个规则定义 |
| ALTER SCHEMA | 更改一个模式的定义 |
| ALTER SEQUENCE | 更改一个序列发生器的定义 |
| ALTER SERVER | 更改一个外部服务器的定义 |
| ALTER STATISTICS | 更改扩展统计对象的定义 |
| ALTER SUBSCRIPTION | 修改订阅的定义 |
| ALTER SYSTEM | 更改一个服务器配置参数 |
| ALTER TABLE | 更改一个表的定义 |
| ALTER TABLESPACE | 更改一个表空间的定义 |
| ALTER TEXT SEARCH CONFIGURATION | 更改一个文本搜索配置的定义 |
| ALTER TEXT SEARCH DICTIONARY | 更改一个文本搜索字典的定义 |
| ALTER TEXT SEARCH PARSER | 更改一个文本搜索解析器的定义 |
| ALTER TEXT SEARCH TEMPLATE | 更改一个文本搜索模板的定义 |
| ALTER TRIGGER | 更改一个触发器的定义 |
| ALTER TYPE | 更改一个类型的定义 |
| ALTER USER | 更改一个数据库角色 |
| ALTER USER MAPPING | 更改一个用户映射的定义 |
| ALTER VIEW | 更改一个视图的定义 |
| ANALYZE | 收集有关一个数据库的统计信息 |
| BEGIN | 开始一个事务块 |
| CALL | 调用一个过程 |
| CHECKPOINT | 强制一个事务日志检查点 |
| CLOSE | 关闭一个游标 |
| CLUSTER | 根据一个索引聚簇一个表 |
| COMMENT | 定义或者更改一个对象的注释 |
| COMMIT | 提交当前事务 |
| COMMIT PREPARED | 提交一个早前为两阶段提交预备的事务 |
| COPY | 在一个文件和一个表之间复制数据 |
| CREATE ACCESS METHOD | 定义一种新的访问方法 |
| CREATE AGGREGATE | 定义一个新的聚集函数 |
| CREATE CAST | 定义一种新的造型 |
| CREATE COLLATION | 定义一种新排序规则 |
| CREATE CONVERSION | 定义一种新的编码转换 |
| CREATE DATABASE | 创建一个新数据库 |
| CREATE DOMAIN | 定义一个新的域 |
| CREATE EVENT TRIGGER | 定义一个新的事件触发器 |
| CREATE EXTENSION | 安装一个扩展 |
| CREATE FOREIGN DATA WRAPPER | 定义一个新的外部数据包装器 |
| CREATE FOREIGN TABLE | 定义一个新的外部表 |
| CREATE FUNCTION | 定义一个新函数 |
| CREATE GROUP | 定义一个新的数据库角色 |
| CREATE INDEX | 定义一个新索引 |
| CREATE LANGUAGE | 定义一种新的过程语言 |
| CREATE MATERIALIZED VIEW | 定义一个新的物化视图 |
| CREATE OPERATOR | 定义一个新的操作符 |
| CREATE OPERATOR CLASS | 定义一个新的操作符类 |
| CREATE OPERATOR FAMILY | 定义一个新的操作符族 |
| CREATE POLICY | 为一个表定义一条新的行级安全性策略 |
| CREATE PROCEDURE | 定义一个新的过程 |
| CREATE PUBLICATION | 定义一个新的发布 |
| CREATE ROLE | 定义一个新的数据库角色 |
| CREATE RULE | 定义一条新的重写规则 |
| CREATE SCHEMA | 定义一个新模式 |
| CREATE SEQUENCE | 定义一个新的序列发生器 |
| CREATE SERVER | 定义一个新的外部服务器 |
| CREATE STATISTICS | 定义扩展统计 |
| CREATE SUBSCRIPTION | 定义一个新的订阅 |
| CREATE TABLE | 定义一个新表 |
| CREATE TABLE AS | 从一个查询的结果创建一个新表 |
| CREATE TABLESPACE | 定义一个新的表空间 |
| CREATE TEXT SEARCH CONFIGURATION | 定义一个新的文本搜索配置 |
| CREATE TEXT SEARCH DICTIONARY | 定义一个新的文本搜索字典 |
| CREATE TEXT SEARCH PARSER | 定义一个新的文本搜索解析器 |
| CREATE TEXT SEARCH TEMPLATE | 定义一种新的文本搜索模板 |
| CREATE TRANSFORM | 定义一个新的转换 |
| CREATE TRIGGER | 定义一个新触发器 |
| CREATE TYPE | 定义一种新的数据类型 |
| CREATE USER | 定义一个新的数据库角色 |
| CREATE USER MAPPING | 定义一个用户到一个外部服务器的新映射 |
| CREATE VIEW | 定义一个新视图 |
| DEALLOCATE | 释放一个预备语句 |
| DECLARE | 定义一个游标 |
| DELETE | 删除一个表的行 |
| DISCARD | 抛弃会话状态 |
| DO | 执行一个匿名代码块 |
| DROP ACCESS METHOD | 移除一种访问方法 |
| DROP AGGREGATE | 移除一个聚集函数 |
| DROP CAST | 移除一个造型 |
| DROP COLLATION | 移除一个排序规则 |
| DROP CONVERSION | 移除一个转换 |
| DROP DATABASE | 移除一个数据库 |
| DROP DOMAIN | 移除一个域 |
| DROP EVENT TRIGGER | 移除一个事件触发器 |
| DROP EXTENSION | 移除一个扩展 |
| DROP FOREIGN DATA WRAPPER | 移除一个外部数据包装器 |
| DROP FOREIGN TABLE | 移除一个外部表 |
| DROP FUNCTION | 移除一个函数 |
| DROP GROUP | 移除一个数据库角色 |
| DROP INDEX | 移除一个索引 |
| DROP LANGUAGE | 移除一个过程语言 |
| DROP MATERIALIZED VIEW | 移除一个物化视图 |
| DROP OPERATOR | 移除一个操作符 |
| DROP OPERATOR CLASS | 移除一个操作符类 |
| DROP OPERATOR FAMILY | 移除一个操作符族 |
| DROP OWNED | 移除一个数据库角色拥有的数据库对象 |
| DROP POLICY | 从一个表移除一条行级安全性策略 |
| DROP PROCEDURE | 移除一个过程 |
| DROP PUBLICATION | 删除一个发布 |
| DROP ROLE | 移除一个数据库角色 |
| DROP ROUTINE | 删除一个例程 |
| DROP RULE | 移除一个重写规则 |
| DROP SCHEMA | 移除一个模式 |
| DROP SEQUENCE | 移除一个序列 |
| DROP SERVER | 移除一个外部服务器描述符 |
| DROP STATISTICS | 删除扩展统计 |
| DROP SUBSCRIPTION | 删除一个订阅 |
| DROP TABLE | 移除一个表 |
| DROP TABLESPACE | 移除一个表空间 |
| DROP TEXT SEARCH CONFIGURATION | 移除一个文本搜索配置 |
| DROP TEXT SEARCH DICTIONARY | 移除一个文本搜索字典 |
| DROP TEXT SEARCH PARSER | 移除一个文本搜索解析器 |
| DROP TEXT SEARCH TEMPLATE | 移除一个文本搜索模板 |
| DROP TRANSFORM | 移除转换 |
| DROP TRIGGER | 移除一个触发器 |
| DROP TYPE | 移除一个数据类型 |
| DROP USER | 移除一个数据库角色 |
| DROP USER MAPPING | 移除一个用于外部服务器的用户映射 |
| DROP VIEW | 移除一个视图 |
| END | 提交当前事务 |
| EXECUTE | 执行一个预备语句 |
| EXPLAIN | 显示一个语句的执行计划 |
| FETCH | 使用游标从查询中检索行 |
| GRANT | 定义访问特权 |
| IMPORT FOREIGN SCHEMA | 从一个外部服务器导入表定义 |
| INSERT | 在一个表中创建新行 |
| LISTEN | 监听一个通知 |
| LOAD | 载入一个共享库文件 |
| LOCK | 锁定一个表 |
| MOVE | 定位一个游标 |
| NOTIFY | 生成一个通知 |
| PREPARE | 为执行准备一个语句 |
| PREPARE TRANSACTION | 为两阶段提交准备当前事务 |
| REASSIGN OWNED | 更改一个数据库角色拥有的数据库对象的拥有关系 |
| REFRESH MATERIALIZED VIEW | 替换一个物化视图的内容 |
| REINDEX | 重建索引 |
| RELEASE SAVEPOINT | 销毁一个之前定义的保存点 |
| RESET | 把一个运行时参数的值恢复到默认值 |
| REVOKE | 移除访问特权 |
| ROLLBACK | 中止当前事务 |
| ROLLBACK PREPARED | 取消一个之前为两阶段提交准备好的事务 |
| ROLLBACK TO SAVEPOINT | 回滚到一个保存点 |
| SAVEPOINT | 在当前事务中定义一个新的保存点 |
| SECURITY LABEL | 定义或更改应用到一个对象的安全标签 |
| SELECT | 从一个表或视图检索行 |
| SELECT INTO | 从一个查询的结果定义一个新表 |
| SET | 更改一个运行时参数 |
| SET CONSTRAINTS | 为当前事务设置约束检查时机 |
| SET ROLE | 设置当前会话的当前用户标识符 |
| SET SESSION AUTHORIZATION | 设置当前会话的会话用户标识符和当前用户标识符 |
| SET TRANSACTION | 设置当前事务的特性 |
| SHOW | 显示一个运行时参数的值 |
| START TRANSACTION | 开始一个事务块 |
| TRUNCATE | 清空一个表或者一组表 |
| UNLISTEN | 停止监听一个通知 |
| UPDATE | 更新一个表的行 |
| VACUUM | 垃圾收集并根据需要分析一个数据库 |
| VALUES | 计算一个行集合 |

## 2\. SQL命令

### 2.1. ABORT

ABORT — 中止当前事务

**大纲**

ABORT \[ WORK | TRANSACTION \] \[ AND \[ NO \] CHAIN \]

**描述**

ABORT回滚当前事务并且导致由该事务所作的所有更新被丢弃。这个命令的行为与标准SQL命令ROLLBACK的行为一样。

**参数**

WORK

TRANSACTION

可选关键词。它们没有效果。

AND CHAIN

如果规定了AND CHAIN ，新事务立即启动，具有与刚刚完成的事务相同的事务特征(参见 SET TRANSACTION)。否则，不会启动新事务。

**注解**

使用COMMIT成功地终止一个事务。

在一个事务块之外发出ABORT会发出一个警告消息并且不会产生效果。

**示例**

中止所有更改：

ABORT;

**兼容性**

这个命令是瀚高数据库扩展。ROLLBACK是等效的标准 SQL 命令。

**另见**

BEGIN, COMMIT, ROLLBACK

### 2.2. ALTER AGGREGATE

ALTER AGGREGATE — 更改一个聚集函数的定义

**大纲**

ALTER AGGREGATE name ( aggregate\_signature ) RENAME TO new\_name

ALTER AGGREGATE name ( aggregate\_signature )

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER AGGREGATE name ( aggregate\_signature ) SET SCHEMA new\_schema

其中 aggregate\_signature 是：

\* |

\[ argmode \] \[ argname \] argtype \[, … \] |

\[ \[ argmode \] \[ argname \] argtype \[, … \] \] ORDER BY \[ argmode \] \[ argname \] argtype \[, … \]

**描述**

ALTER AGGREGATE更改一个聚集函数的定义。

要使用ALTER AGGREGATE，你必须拥有该聚集函数。要更改一个聚集函数的模式，你还必须具有新模式上的CREATE特权。要修改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且那个角色必须在聚集函数的模式上拥有CREATE特权（这些限制强制要求拥有者不能通过丢弃并重建该聚集函数来做任何你不能做的事情。不过，一个超级用户可以更改任何聚集函数的所有权）。

**参数**

name

一个现有聚集函数的名称（可以是模式限定的）。

argmode

一个参数的模式：IN或VARIADIC。如果省略，默认为IN。

argname

一个参数的名称。注意ALTER AGGREGATE并不真正关心参数名称，因为决定聚集函数的身份时只需要参数的数据类型。

argtype

聚集函数要在其上操作的输入数据类型。要引用一个零参数聚集函数，在参数说明列表的位置写上\*。要引用一个有序集聚集函数，在直接参数说明和聚集参数说明之间写上ORDER BY。

new\_name

聚集函数的新名称。

new\_owner

聚集函数的新拥有者。

new\_schema

聚集函数的新模式。

**注解**

引用有序集聚集的推荐语法是在直接参数说明和聚集参数说明之间写上ORDER BY，这和CREATE AGGREGATE中的风格相同。不过，省略ORDER BY并且只把直接和聚集参数说明放到一个单一列表中也是可以的。在这种简写形式中，如果在直接和聚集参数列表中都使用了VARIADIC “any”，只用 写一次VARIADIC “any”。

**示例**

要把用于类型integer的聚集函数 myavg重命名为my\_average：

ALTER AGGREGATE myavg(integer) RENAME TO my\_average;

要把用于类型integer的聚集函数 myavg的拥有者改为joe：

ALTER AGGREGATE myavg(integer) OWNER TO joe;

把带有float8类型直接参数和integer 类型聚集参数的有序集聚集mypercentile 移动到 模式myschema中：

ALTER AGGREGATE mypercentile(float8 ORDER BY integer) SET SCHEMA myschema;

这也能行：

ALTER AGGREGATE mypercentile(float8, integer) SET SCHEMA myschema;

**兼容性**

在 SQL 标准中没有ALTER AGGREGATE语句。

**另见**

CREATE AGGREGATE, DROP AGGREGATE

### 2.3. ALTER COLLATION

ALTER COLLATION — 更改一个排序规则的定义

**大纲**

ALTER COLLATION name REFRESH VERSION

ALTER COLLATION name RENAME TO new\_name

ALTER COLLATION name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER COLLATION name SET SCHEMA new\_schema

**描述**

ALTER COLLATION更改一个排序规则的定义。

你必须拥有要对其使用ALTER COLLATION的排序规则。要更改拥有者，你必须是新的拥有角色的直接或者间接成员，并且该角色必须在排序规则的模式上具有CREATE特权（这些限制强制要求拥有者不能通过丢弃并重建该排序规则来做任何你不能做的事情。不过，一个超级用户可以更改任何排序规则的所有权）。

**参数**

name

一个现有排序规则的名称（可以是模式限定的）。

new\_name

排序规则的新名称。

new\_owner

排序规则的新拥有者。

new\_schema

排序规则的新模式。

REFRESH VERSION

更新排序规则的版本。 参阅下面的注意。

**注意**

使用ICU库提供的排序规则时，创建排序规则对象时，系统目录中会记录排序规则的特定ICU版本。 使用排序规则时，将根据记录的版本检查当前版本，并在发生不匹配时发出警告，例如：

WARNING: collation “xx-x-icu” has version mismatch

排序规则定义的更改会导致索引损坏和其他问题，因为数据库系统依赖于具有特定排序顺序的存储对象。通常，应该避免这种情况，但它可以在合法的情况下发生，例如使用pg\_upgrade升级到与更新版本的ICU链接的服务器二进制文件。发生这种情况时，应该重建所有依赖于该排序规则的对象，例如，使用REINDEX。完成后，使用命令ALTER COLLATION … REFRESH VERSION可以刷新排序规则版本。这将更新系统目录以记录当前的排序规则版本，并会使警告消失。请注意，这实际上并不检查是否所有受影响的对象都已正确重建。

以下查询可用于识别当前数据库中需要刷新的所有排序规则以及依赖它们的对象：

```sql
SELECT pg_describe_object(refclassid, refobjid, refobjsubid) AS "Collation",
       pg_describe_object(classid, objid, objsubid) AS "Object"
  FROM pg_depend d JOIN pg_collation c
       ON refclassid = 'pg_collation'::regclass AND refobjid = c.oid
  WHERE c.collversion <> pg_collation_actual_version(c.oid)
  ORDER BY 1, 2;
```

**示例**

要把排序规则de\_DE重命名为german：

ALTER COLLATION “de\_DE” RENAME TO german;

要把排序规则en\_US的拥有者改成joe：

ALTER COLLATION “en\_US” OWNER TO joe;

**兼容性**

在 SQL 标准中没有ALTER COLLATION语句。

**另见**

CREATE COLLATION, DROP COLLATION

### 2.4. ALTER CONVERSION

ALTER CONVERSION — 改变一个转换的定义

**大纲**

ALTER CONVERSION name RENAME TO new\_name

ALTER CONVERSION name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER CONVERSION name SET SCHEMA new\_schema

**描述**

ALTER CONVERSION改变一个转换的定义。

你必须拥有要对其使用ALTER CONVERSION的转换。要更改拥有者，你必须是新的拥有角色的直接或者间接成员，并且该角色必须在转换的模式上具有CREATE特权（这些限制强制要求拥有者不能通过丢弃并重建该转换来做任何你不能做的事情。不过，一个超级用户可以更改任何转换的所有权）。

**参数**

name

一个现有转换的名称（可以是模式限定的）。

new\_name

转换的新名称。

new\_owner

转换的新拥有者。

new\_schema

转换的新模式。

**示例**

要把转换iso\_8859\_1\_to\_utf8重命名为latin1\_to\_unicode：

ALTER CONVERSION iso\_8859\_1\_to\_utf8 RENAME TO latin1\_to\_unicode;

要把转换iso\_8859\_1\_to\_utf8的拥有者改成joe：

ALTER CONVERSION iso\_8859\_1\_to\_utf8 OWNER TO joe;

**兼容性**

在 SQL 标准中没有ALTER CONVERSION语句。

**另见**

CREATE CONVERSION, DROP CONVERSION

### 2.5. ALTER DATABASE

ALTER DATABASE — 更改一个数据库

**大纲**

ALTER DATABASE name \[ \[ WITH \] option \[ … \] \]

这里 option 可以是：

ALLOW\_CONNECTIONS allowconn

CONNECTION LIMIT connlimit

IS\_TEMPLATE istemplate

ALTER DATABASE name RENAME TO new\_name

ALTER DATABASE name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER DATABASE name SET TABLESPACE new\_tablespace

ALTER DATABASE name SET configuration\_parameter { TO | = } { value | DEFAULT }

ALTER DATABASE name SET configuration\_parameter FROM CURRENT

ALTER DATABASE name RESET configuration\_parameter

ALTER DATABASE name RESET ALL

**描述**

ALTER DATABASE更改一个数据库的属性。

第一种形式更改某些针对每个数据库的设置（详见下文）。只有数据库拥有者或者超级用户可以更改这些设置。

第二种形式更改数据库的名称。只有数据库拥有者或者超级用户可以重命名一个数据库，非超级用户拥有者还必须拥有CREATEDB特权。当前数据库不能被重命名（如果你需要这样做请连接到一个不同的数据库）。

第三种形式更改数据库的拥有者。要修改拥有者，你必须拥有该数据库并且也是新拥有角色的一个直接或间接成员，并且你必须具有CREATEDB特权（注意超级用户自动拥有所有这些特权）。

第四种形式更改数据库的默认表空间。只有数据库拥有者或超级用户能够这样做，你还必须对新表空间具有创建特权。这个命令会在物理上移动位于该数据库旧的默认表空间中的任何表或索引到新的表空间中。新的默认表空间对于这个数据库必须是空的，并且不能有人可以连接到该数据库。在非默认表空间中的表和索引不受影响。

剩下的形式更改用于一个瀚高数据库的运行时配置变量的会话默认值。接下来只要一个新的会话在该数据库中开始，指定的值就会成为该会话的默认值。数据库相关的默认值会覆盖出现在postgresql.conf中或者从postgres命令行接收到的设置。只有数据库拥有者或超级用户可以更改一个数据库的会话默认值。一些变量不能用这种方式设置或者只能由超级用户更改。

**参数**

name

要被修改属性的数据库名称。

allowconn

如果为假，则没有人能连接到这个数据库。

connlimit

与这个数据库可以建立多少个并发连接。-1表示没有限制。

istemplate

如果为真，则任何具有CREATEDB特权的用户都可以从这个数据库进行克隆。如果为假，则只有超级用户或者这个数据库的拥有者可以克隆它。

new\_name

数据库的新名称。

new\_owner

数据库的新拥有者。

new\_tablespace

数据库的新默认表空间。

这种形式的命令不能在事务块内执行。

configuration\_parameter

value

将这个数据库的指定配置参数的会话默认值设置为给定值。如果value是DEFAULT，或者等效地使用了RESET，数据库相关的设置会被移除，因此系统范围的默认设置将会在新会话中继承。使用RESET ALL可清除所有数据库相关的设置。SET FROM CURRENT会保存该会话的当前参数值作为数据库相关的值。

**注解**

也可以把一个会话的默认值绑定到一个特定角色而不是一个数据库，见 ALTER ROLE 。如果有冲突，角色相关的设置会覆盖数据库相关的值。

**示例**

要在数据库test中默认禁用索引扫描：

ALTER DATABASE test SET enable\_indexscan TO off;

**兼容性**

ALTER DATABASE语句是一个瀚高数据库扩展。

**另见**

CREATE DATABASE, DROP DATABASE, SET,CREATE TABLESPACE

### 2.6. ALTER DEFAULT PRIVILEGES

ALTER DEFAULT PRIVILEGES — 定义默认访问特权

**大纲**

ALTER DEFAULT PRIVILEGES

\[ FOR { ROLE | USER } target\_role \[, …\] \]

\[ IN SCHEMA schema\_name \[, …\] \]

abbreviated\_grant\_or\_revoke

其中abbreviated\_grant\_or\_revoke是下列之一：

GRANT { { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }

\[, …\] | ALL \[ PRIVILEGES \] }

ON TABLES

TO { \[ GROUP \] role\_name | PUBLIC } \[, …\] \[ WITH GRANT OPTION \]

GRANT { { USAGE | SELECT | UPDATE }

\[, …\] | ALL \[ PRIVILEGES \] }

ON SEQUENCES

TO { \[ GROUP \] role\_name | PUBLIC } \[, …\] \[ WITH GRANT OPTION \]

GRANT { EXECUTE | ALL \[ PRIVILEGES \] }

ON { FUNCTIONS | ROUTINES }

TO { \[ GROUP \] role\_name | PUBLIC } \[, …\] \[ WITH GRANT OPTION \]

GRANT { USAGE | ALL \[ PRIVILEGES \] }

ON TYPES

TO { \[ GROUP \] role\_name | PUBLIC } \[, …\] \[ WITH GRANT OPTION \]

GRANT { USAGE | CREATE | ALL \[ PRIVILEGES \] }

ON SCHEMAS

TO { \[ GROUP \] role\_name | PUBLIC } \[, …\] \[ WITH GRANT OPTION \]

REVOKE \[ GRANT OPTION FOR \]

{ { SELECT | INSERT | UPDATE | DELETE | TRUNCATE | REFERENCES | TRIGGER }

\[, …\] | ALL \[ PRIVILEGES \] }

ON TABLES

FROM { \[ GROUP \] role\_name | PUBLIC } \[, …\]

\[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ { USAGE | SELECT | UPDATE }

\[, …\] | ALL \[ PRIVILEGES \] }

ON SEQUENCES

FROM { \[ GROUP \] role\_name | PUBLIC } \[, …\]

\[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ EXECUTE | ALL \[ PRIVILEGES \] }

ON { FUNCTIONS | ROUTINES }

FROM { \[ GROUP \] role\_name | PUBLIC } \[, …\]

\[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ USAGE | ALL \[ PRIVILEGES \] }

ON TYPES

FROM { \[ GROUP \] role\_name | PUBLIC } \[, …\]

\[ CASCADE | RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ USAGE | CREATE | ALL \[ PRIVILEGES \] }

ON SCHEMAS

FROM { \[ GROUP \] role\_name | PUBLIC } \[, …\]

\[ CASCADE | RESTRICT \]

**描述**

ALTER DEFAULT PRIVILEGES允许你设置将被应用于未来要创建的对象的特权（它不会影响分配给已经存在的对象的特权）。当前，只能修改用于模式、表（包括视图和外部表）、序列、函数和类型（包括域）的特权。其中，可设置权限的函数包括聚集函数和过程函数。当这个命令应用于函数时，单词FUNCTIONS和ROUTINES是等效的。（推荐使用ROUTINES，因为它是用来囊括函数和过程的一个标准术语。）

你只能改变你自己或者你属于其中的角色所创建的对象的默认特权。这些特权可以对全局范围设置（即对当前数据库中创建的所有对象），或者只对在指定模式中创建的对象设置。

用于任何对象类型的默认特权通常会把所有可授予的权限授予给对象拥有者，并且也可能授予一些特权给PUBLIC。不过，这种行为可以通过使用ALTER DEFAULT PRIVILEGES修改全局默认特权来改变。

每个模式规定的默认权限将添加到特定对象类型的全局默认特权的内容中。这意味着你不能撤销每个模式的特权，如果它们已经被全局授予（默认情况下，或者根据以前未规定模式的ALTER DEFAULT PRIVILEGES命令）。 每个模式的REVOKE仅用于反转以前每个模式GRANT的影响。

**参数**

target\_role

一个现有角色的名称，当前角色是它的一个成员。如果FOR ROLE被忽略，将假定为当前角色。

schema\_name

一个现有模式的名称。如果被指定，以后在那个模式中创建的对象的默认特权会被修改。如果IN SCHEMA被忽略，全局默认特权会被修改。当设置特权给模式时不能使用IN SCHEMA，因为模式不能嵌套。

role\_name

要为其授予或者收回特权的一个现有角色的名称。这个参数以及所有abbreviated\_grant\_or\_revoke中的其他参数会按照GRANT或者REVOKE中描述的方式运作，不过这里是为一整类的对象而不是特别指定的对象设置权限。

**注解**

使用psql的\\ddp命令可以获得关于默认特权的现有分配信息。

如果你希望删除一个默认特权被修改的角色，有必要撤销其默认特权上的改变或者使用DROP OWNED BY来为该角色去除默认特权项。

**示例**

为你后续在模式myschema中创建的所有表（和视图）授予SELECT特权，并且也允许角色webuser向它们之中INSERT数据：

ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO PUBLIC;

ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT INSERT ON TABLES TO webuser;

撤销上面的动作，因此后续创建的表不会有任何非常规权限：

ALTER DEFAULT PRIVILEGES IN SCHEMA myschema REVOKE SELECT ON TABLES FROM PUBLIC;

ALTER DEFAULT PRIVILEGES IN SCHEMA myschema REVOKE INSERT ON TABLES FROM webuser;

为后续由角色admin创建的所有函数移除通常在函数上会授予的公共 EXECUTE 权限：

ALTER DEFAULT PRIVILEGES FOR ROLE admin REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;

但是注意你不能使用限制为单个模式的命令来实现该效果。此命令不起作用，除非它撤消匹配的GRANT：

ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE EXECUTE ON FUNCTIONS FROM PUBLIC;

这是因为每个模式的默认特权只能向全局设置添加特权，而不能移除它授予的特权。

**兼容性**

在 SQL 标准中没有ALTER DEFAULT PRIVILEGES语句。

**另见**

GRANT, REVOKE

### 2.7. ALTER DOMAIN

ALTER DOMAIN — 更改一个域的定义

**大纲**

ALTER DOMAIN name

{ SET DEFAULT expression | DROP DEFAULT }

ALTER DOMAIN name

{ SET | DROP } NOT NULL

ALTER DOMAIN name

ADD domain\_constraint \[ NOT VALID \]

ALTER DOMAIN name

DROP CONSTRAINT \[ IF EXISTS \] constraint\_name \[ RESTRICT | CASCADE \]

ALTER DOMAIN name

RENAME CONSTRAINT constraint\_name TO new\_constraint\_name

ALTER DOMAIN name

VALIDATE CONSTRAINT constraint\_name

ALTER DOMAIN name

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER DOMAIN name

RENAME TO new\_name

ALTER DOMAIN name

SET SCHEMA new\_schema

**描述**

ALTER DOMAIN更改一个现有域的定义。有几种形式：

SET/DROP DEFAULT

这些形式设置或者移除一个域的默认值。注意默认值只会应用到后续的INSERT命令，它们不影响使用该域的已经存在于表中的行。

SET/DROP NOT NULL

这些形式更改一个域是被标记为允许NULL值还是拒绝NULL值。只有当使用该域的列不包含空值时才能SET NOT NULL。

ADD domain\_constraint \[ NOT VALID \]

这种形式使用和CREATE DOMAIN相同的语法为一个域增加一个新的约束。当一个新的约束被增加到一个域时，所有使用该域的列都会被根据新加的约束进行检查。可以通过增加使用NOT VALID选项的新约束来抑制这类检查，而该约束则可以在以后使用ALTER DOMAIN … VALIDATE CONSTRAINT 变为可用。新插入和更新的行总是会被根据所有约束进行检查（包括被标记为 NOT VALID的约束）。只有CHECK约束接受 NOT VALID。

DROP CONSTRAINT \[ IF EXISTS \]

这种形式删除一个域上的约束。如果指定了IF EXISTS并且约束不存在，不会抛出错误。在这种情况下会转而发出一个提示。

RENAME CONSTRAINT

这种形式更改一个域上的一个约束的名称。

VALIDATE CONSTRAINT

这种形式验证一个之前作为NOT VALID增加的约束，也就是说它验证该域类型的表列中所有值满足指定的约束。

OWNER

这种形式更改域的拥有者为指定用户。

RENAME

这种形式更改域的名称。

SET SCHEMA

这种形式更改域的模式。任何与该域关联的约束也被会移动到新的模式中。

要使用ALTER DOMAIN，你必须拥有该域。要更改一个域的模式，你还必须具有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该域的模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建域做不到的事情。不过，一个超级用户怎么都能更改任何域的所有权。）。

**参数**

name

要修改的一个现有域的名称（可能是模式限定的）。

domain\_constraint

用于该域的新域约束。

constraint\_name

要删除或重命名的一个现有约束的名称。

NOT VALID

不为约束的合法性验证现有的存储数据。

CASCADE

自动删除依赖于该约束的对象，并且接着删除依赖于那些对象的所有对象。

RESTRICT

如果有任何依赖对象则拒绝删除该约束。这是默认行为。

new\_name

域的新名称。

new\_constraint\_name

约束的新名称。

new\_owner

域的新拥有者的用户名。

new\_schema

域的新模式。

**注解**

尽管ALTER DOMAIN ADD CONSTRAINT尝试验证现有存储的数据是否满足新约束，但此检查不是万无一失的，因为命令无法看到新插入或更新但尚未提交的表行。如果存在并发操作可能插入坏数据的危险，则处理方法是使用NOT VALID选项添加约束，提交该命令，等到所有事务在提交完成之前启动，然后发出ALTER DOMAIN VALIDATE CONSTRAINT以搜索违反约束的数据。此方法是可靠的，因为一旦提交约束，所有新事务都保证针对域类型的新值强制执行约束。

当前，如果域或者任何衍生域被数据库中的任意表的一个容器类型列（组合、数组、范围类型的列）使用，ALTER DOMAIN ADD CONSTRAINT、ALTER DOMAIN VALIDATE CONSTRAINT和 ALTER DOMAIN SET NOT NULL将会失败。这些命令最终将会被改进成能够对这类嵌套值进行约束验证。

**示例**

要把一个NOT NULL约束加到一个域：

ALTER DOMAIN zipcode SET NOT NULL;

要从一个域中移除一个NOT NULL约束：

ALTER DOMAIN zipcode DROP NOT NULL;

要把一个检查约束增加到一个域：

ALTER DOMAIN zipcode ADD CONSTRAINT zipchk CHECK (char\_length(VALUE) = 5);

要从一个域移除一个检查约束：

ALTER DOMAIN zipcode DROP CONSTRAINT zipchk;

要重命名一个域上的一个检查约束：

ALTER DOMAIN zipcode RENAME CONSTRAINT zipchk TO zip\_check;

要把域移动到一个不同的模式：

ALTER DOMAIN zipcode SET SCHEMA customers;

**兼容性**

除OWNER、RENAME、SET SCHEMA 以及VALIDATE CONSTRAINT形式之外（它们是瀚高数据库的扩展），ALTER DOMAIN符合SQL标准。ADD CONSTRAINT变体的NOT VALID子句也是一个瀚高数据库扩展。

**另见**

CREATE DOMAIN, DROP DOMAIN

### 2.8. ALTER EVENT TRIGGER

ALTER EVENT TRIGGER — 更改一个事件触发器的定义

**大纲**

ALTER EVENT TRIGGER name DISABLE

ALTER EVENT TRIGGER name ENABLE \[ REPLICA | ALWAYS \]

ALTER EVENT TRIGGER name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER EVENT TRIGGER name RENAME TO new\_name

**描述**

ALTER EVENT TRIGGER更改一个现有事件触发器的属性。

必须作为一个超级用户才能修改一个时间触发器。

**参数**

name

要修改的现有触发器的名称。

new\_owner

该事件触发器的新拥有者的用户名。

new\_name

该事件触发器的新名称。

DISABLE/ENABLE \[ REPLICA | ALWAYS \] TRIGGER

这些形式配置事件触发器的触发。一个被禁用的触发器对系统来说仍然是可知的， 但是当期触发事件发生时却不会执行它。

**兼容性**

在 SQL 标准中没有ALTER EVENT TRIGGER语句。

**另见**

CREATE EVENT TRIGGER, DROP EVENT TRIGGER

### 2.9. ALTER EXTENSION

ALTER EXTENSION 更改一个扩展的定义

**大纲**

ALTER EXTENSION name UPDATE \[ TO new\_version \]

ALTER EXTENSION name SET SCHEMA new\_schema

ALTER EXTENSION name ADD member\_object

ALTER EXTENSION name DROP member\_object

其中 member\_object 是：

ACCESS METHOD object\_name |

AGGREGATE aggregate\_name ( aggregate\_signature ) |

CAST (source\_type AS target\_type) |

COLLATION object\_name |

CONVERSION object\_name |

DOMAIN object\_name |

EVENT TRIGGER object\_name |

FOREIGN DATA WRAPPER object\_name |

FOREIGN TABLE object\_name |

FUNCTION function\_name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \] |

MATERIALIZED VIEW object\_name |

OPERATOR operator\_name (left\_type, right\_type) |

OPERATOR CLASS object\_name USING index\_method |

OPERATOR FAMILY object\_name USING index\_method |

\[ PROCEDURAL \] LANGUAGE object\_name |

PROCEDURE procedure\_name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \] |

ROUTINE routine\_name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \] |

SCHEMA object\_name |

SEQUENCE object\_name |

SERVER object\_name |

TABLE object\_name |

TEXT SEARCH CONFIGURATION object\_name |

TEXT SEARCH DICTIONARY object\_name |

TEXT SEARCH PARSER object\_name |

TEXT SEARCH TEMPLATE object\_name |

TRANSFORM FOR type\_name LANGUAGE lang\_name |

TYPE object\_name |

VIEW object\_name

并且 aggregate\_signature 是：

\* |

\[ argmode \] \[ argname \] argtype \[, … \] |

\[ \[ argmode \] \[ argname \] argtype \[, … \] \] ORDER BY \[ argmode \] \[ argname \] argtype \[, … \]

**描述**

ALTER EXTENSION更改一个已安装扩展的定义。有几种子形式：

UPDATE

这种形式把该扩展更新到一个新版本。该扩展必须提供一个适当的更新脚本（或者一系列脚本）来把当前已安装的版本修改成所要求的版本。

SET SCHEMA

这种形式把该扩展的对象移动到另一个模式中。要使这个命令成功，该扩展必须是可重定位的。

ADD member\_object

这种形式把一个现有的对象加入到该扩展中。这主要对扩展更新脚本有用。该对象后续将被当作该扩展的一个成员。尤其是该对象只有通过删除扩展才能删除。

DROP member\_object

这种形式从该扩展移除一个成员对象。这主要对扩展更新脚本有用。只有撤销该对象与其扩展之间的关联后才能删除该对象。

要使用ALTER EXTENSION，你必须拥有该扩展。ADD/DROP形式还要求被增加/删除对象的所有权。

**参数**

name

一个已安装扩展的名称。

new\_version

想要得到的该扩展的新版本。这可以写成一个标识符或者一个字符串。如果没有指定，ALTER EXTENSION UPDATE会尝试更新到该扩展的控制文件中的默认版本。

new\_schema

该扩展的新模式。

object\_name

aggregate\_name

function\_name

operator\_name

procedure\_name

routine\_name

要从该扩展增加或者移除的对象的名称。表、聚集、域、外部表、函数、操作符、操作符类、操作符族、过程、例程、序列、文本搜索对象、类型和视图的名称可以被模式限定。

source\_type

该转换的源数据类型的名称。

target\_type

该转换的目标数据类型的名称。

argmode

一个函数、过程或者聚集参数的模式：IN、OUT、INOUT或者VARIADIC。如果被忽略，默认值是IN。注意，ALTER EXTENSION并不真正关心OUT参数，因为决定该函数的身份时只需要输入参数。因此列出IN、INOUT和VARIADIC参数足矣。

argname

一个函数、过程或者聚集参数的名称。注意，ALTER EXTENSION并不真正关心参数名称，因为决定该函数的身份时只需要参数的数据类型。

argtype

一个函数、过程或者或聚集参数的数据类型。

left\_type

right\_type

该操作符参数的数据类型（可以用模式限定）。对一个前缀或后缀操作符的缺失的参数可以写NONE。

PROCEDURAL

这是一个噪声词。

type\_name

该转换的数据类型的名称。

lang\_name

该转换的语言的名称。

**示例**

把hstore扩展更新到版本2.0：

ALTER EXTENSION hstore UPDATE TO ‘2.0’;

把hstore扩展的模式更改到utils：

ALTER EXTENSION hstore SET SCHEMA utils;

要向hstore扩展增加一个现有函数：

ALTER EXTENSION hstore ADD FUNCTION populate\_record(anyelement, hstore);

**兼容性**

ALTER EXTENSION是一个瀚高数据库扩展。

**另见**

CREATE EXTENSION, DROP EXTENSION

### 2.10. ALTER FOREIGN DATA WRAPPER

ALTER FOREIGN DATA WRAPPER — 更改一个外部数据包装器的定义

**大纲**

ALTER FOREIGN DATA WRAPPER name

\[ HANDLER handler\_function | NO HANDLER \]

\[ VALIDATOR validator\_function | NO VALIDATOR \]

\[ OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \]) \]

ALTER FOREIGN DATA WRAPPER name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER FOREIGN DATA WRAPPER name RENAME TO new\_name

**描述**

ALTER FOREIGN DATA WRAPPER更改一个外部数据包装器的定义。该命令的第一种形式用于更改外部数据包装器的支持函数或者一般选项（至少要求一个子句）。第二种形式更改外部数据包装器的拥有者。

只有超级用户能修改外部数据包装器。此外，只有超级用户能够拥有外部数据包装器。

**参数**

name

一个已有的外部数据包装器的名称。

HANDLER handler\_function

为外部数据包装器指定一个新的处理器函数。

NO HANDLER

用于指定该外部数据包装器不再具有一个处理器函数。

注意使用没有处理器的外部数据包装器的外部表不能被访问。

VALIDATOR validator\_function

为外部数据包装器指定一个新的验证器函数。

注意，新的验证器可能会认为该外部数据包装器或者依赖于它的独立服务器的已有选项、用户映射、外部表无效。瀚高数据库不会做这种检查。在使用修改过的外部数据包装器之前确认这些选项正确是用户的责任。不过，在这个ALTER FOREIGN DATA WRAPPER命令中指定的选项将会被使用新的验证器检查。

NO VALIDATOR

用于指定该外部数据包装器不再拥有一个验证器函数。

OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \] )

为该外部数据包装器更改选项。ADD、SET以及DROP指定要被执行的动作。如果没有显式地指定操作，将假定为ADD。选项名称必须唯一，选项名称和值（如果有）也会使用该外部数据包装器的验证器函数来验证。

new\_owner

该外部数据包装器的新拥有者的用户名。

new\_name

该外部数据包装器的新名称。

**示例**

更改一个外部数据包装器dbi，增加选项foo并删除bar：

ALTER FOREIGN DATA WRAPPER dbi OPTIONS (ADD foo ‘1’, DROP ‘bar’);

把外部数据包装器dbi的验证器改为 bob.myvalidator：

ALTER FOREIGN DATA WRAPPER dbi VALIDATOR bob.myvalidator;

**兼容性**

ALTER FOREIGN DATA WRAPPER符合 ISO/IEC 9075-9 (SQL/MED)。不过HANDLER、 VALIDATOR、OWNER TO 以及RENAME子句是扩展。

**另见**

CREATE FOREIGN DATA WRAPPER, DROP FOREIGN DATA WRAPPER

### 2.11. ALTER FOREIGN TABLE

ALTER FOREIGN TABLE — 更改一个外部表的定义

**大纲**

ALTER FOREIGN TABLE \[ IF EXISTS \] \[ ONLY \] name \[ \* \]

action \[, … \]

ALTER FOREIGN TABLE \[ IF EXISTS \] \[ ONLY \] name \[ \* \]

RENAME \[ COLUMN \] column\_name TO new\_column\_name

ALTER FOREIGN TABLE \[ IF EXISTS \] name

RENAME TO new\_name

ALTER FOREIGN TABLE \[ IF EXISTS \] name

SET SCHEMA new\_schema

其中 action 是以下之一：

ADD \[ COLUMN \] column\_name data\_type \[ COLLATE collation \]

\[ column\_constraint \[ … \] \]

DROP \[ COLUMN \] \[ IF EXISTS \] column\_name \[ RESTRICT | CASCADE \]

ALTER \[ COLUMN \] column\_name \[ SET DATA \] TYPE data\_type \[ COLLATE collation

\]

ALTER \[ COLUMN \] column\_name SET DEFAULT expression

ALTER \[ COLUMN \] column\_name DROP DEFAULT

ALTER \[ COLUMN \] column\_name { SET | DROP } NOT NULL

ALTER \[ COLUMN \] column\_name SET STATISTICS integer

ALTER \[ COLUMN \] column\_name SET ( attribute\_option = value \[, … \] )

ALTER \[ COLUMN \] column\_name RESET ( attribute\_option \[, … \] )

ALTER \[ COLUMN \] column\_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED |

MAIN }

ALTER \[ COLUMN \] column\_name OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\]

\[, … \])

ADD table\_constraint \[ NOT VALID \]

VALIDATE CONSTRAINT constraint\_name

DROP CONSTRAINT \[ IF EXISTS \] constraint\_name \[ RESTRICT | CASCADE \]

DISABLE TRIGGER \[ trigger\_name | ALL | USER \]

ENABLE TRIGGER \[ trigger\_name | ALL | USER \]

ENABLE REPLICA TRIGGER trigger\_name

ENABLE ALWAYS TRIGGER trigger\_name

SET WITHOUT OIDS

INHERIT parent\_table

NO INHERIT parent\_table

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \])

**描述**

ALTER FOREIGN TABLE更改一个现有外部表的定义。 有几种子形式：

ADD COLUMN

这种形式使用与CREATE FOREIGN TABLE相同的语法把一个新的列增加到该外部表。和为常规表增加一列不同，这种形式并不影响底层的存储：这个动作只是简单地声明通过该外部表可以访问某个新的列而已。

DROP COLUMN \[ IF EXISTS \]

这种形式从一个外部表删掉一列。如果在该表外部有任何东西依赖于该列，你将需要写上CASCADE，典型的例子就是视图。如果指定了IF EXISTS并且该列不存在，将不会抛出错误。在这种情况下会转而发出一个提示。

SET DATA TYPE

这种形式更改一个外部表的一列的类型。同样，这种形式并不影响底层的存储：这个动作只是简单地更改瀚高数据库相信该列所具有的类型。

SET/DROP DEFAULT

这些形式设置或者移除一列的默认值。默认值只会应用于后续的INSERT或UPDATE命令，它们不会导致已经在表中的行被更改。

SET/DROP NOT NULL

把一列标记为允许或者不允许空值。

SET STATISTICS

这种形式为后续的ANALYZE操作设置针对每列的统计收集目标。详见 ALTER ROLE 的类似形式。

SET ( attribute\_option = value \[, … \] )

RESET ( attribute\_option \[, … \] )

这种形式设置或重置针对每个属性的选项。详见 ALTER ROLE 的类似形式。

SET STORAGE

这种形式设置一个列的存储模式。详见 ALTER ROLE 中类似的模式。注意存储模式不会产生效果，除非该表的外部数据包装器选择处理它。

ADD table\_constraint \[ NOT VALID \]

这种形式为外部表增加一个新的约束，使用的语法和 CREATE FOREIGN TABLE中相同。当前只支持CHECK约束。

和向常规表增加约束的情况不同，为外部表增加约束时不会做任何事情来验证该约束是否正确。这个动作只是简单地声明了该外部表中所有的行都应该满足的某种新的条件（见 CREATE FOREIGN TABLE 中的讨论）。如果该约束被标记为NOT VALID，那么它不被假设为有效，而只是被记录下来以备未来使用。

VALIDATE CONSTRAINT

这种形式把一个之前被标记为NOT VALID的约束标记为有效。不会做任何动作来验证该约束，但是未来的查询将会假定该约束是保持的。

DROP CONSTRAINT \[ IF EXISTS \]

这种形式删掉在一个外部表上的指定约束。如果指定了 IF EXISTS但约束并不存在，则不会抛出错误。在这种情况下会发出一个提示。

DISABLE/ENABLE \[ REPLICA | ALWAYS \] TRIGGER

这些形式配置属于该外部表的触发器的触发情况。详见 ALTER ROLE 的类似形式。

SET WITHOUT OIDS

向后兼容性语法，表示移除oid系统列。由于不能再为外部表添加oid系统列，此语句不再产生效用。

INHERIT parent\_table

这种形式把目标外部表作为指定的父表的新后代。详见 ALTER ROLE 的类似的形式。

NO INHERIT parent\_table

这种形式把目标外部表从指定的父表的子列表中移除。

OWNER

这种形式把该外部表的拥有者改成指定的用户。

OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \] )

更改该外部表或者其中一个列的选项。ADD、SET以及DROP指定要执行的动作。如果没有显式地指定操作，将假定为ADD。不允许重复的名称（不过一个表选项和一个列选项可以重名）。选项名称和值也会用外部数据包装器库来验证。

RENAME

RENAME形式更改外部表的名称或者外部表中一个列的名称。

SET SCHEMA

这种形式把外部表移动到另一个模式中。

所有除了RENAME和SET SCHEMA的动作都能被整合到一个多修改列表以便能被并行应用。例如，可以在一个命令中增加几个列并且/或者修改几个列的类型。

如果该命令被写作ALTER FOREIGN TABLE IF EXISTS …并且该外部表不存在，则不会抛出错误。这种情况下会发出一个提示。

你必须拥有该表以使用ALTER FOREIGN TABLE。要更改一个外部表的模式，你必须还拥有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有在该表的模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建该表做不到的事情。不过，一个超级用户怎么都能更改任何表的所有权）。要增加一列或者修改一个列的类型，你还必须具有该数据类型上的USAGE特权。

**参数**

name

一个要修改的现有外部表的名称（可以被模式限定）。如果在表名前指定了ONLY，则只有该表被修改。如果没有指定ONLY，该表和它所有的后代表（如果有）都会被修改。可选地，在表名后面指定\*可以显式地表示将后代表包括在内。

column\_name

一个新的或者现有列的名称。

new\_column\_name

一个现有列的新名称。

new\_name

该表的新名称。

data\_type

新列的数据类型或者一个现有列的新数据类型。

table\_constraint

外部表的新表约束。

constraint\_name

要删除的现有约束的名称。.

CASCADE

自动删除依赖于被删除列或约束的对象（例如，引用该列的视图），并且接着删除依赖于那些对象的所有对象。

RESTRICT

如果有任何依赖对象就拒绝删除该列或约束。这是默认行为。

trigger\_name

要禁用或启用的一个触发器的名称。

ALL

禁用或者启用所有属于该外部表的触发器（如果任何触发器是内部生成的触发器，这都要求超级用户特权。核心系统不会向外部表增加这类触发器，但是附加代码会这样做。）。

USER

禁用或者启用属于该外部表的除了内部生成的触发器之外的所有触发器。

parent\_table

要与这个外部表关联或者解除关联的父表。

new\_owner

该表的新拥有者的用户名。

new\_schema

该表要被移动到其中的模式的名称。

**注解**

关键词COLUMN是噪声词并且可以被忽略。

当使用ADD COLUMN或DROP COLUMN增加或移除一列、增加一个NOT NULL 或者CHECK 约束或者用SET DATA TYPE更改一个列类型时，不会检查与外部服务器的一 致性。确保该表定义匹配远端是用户的责任。

关于有效参数的进一步描述可参考 CREATE FOREIGN TABLE 。

**示例**

要把一列标记为非空：

ALTER FOREIGN TABLE distributors ALTER COLUMN street SET NOT NULL;

要更改一个外部表的选项：

ALTER FOREIGN TABLE myschema.distributors OPTIONS (ADD opt1 ‘value’, SET opt2

‘value2’, DROP opt3 ‘value3’);

**兼容性**

形式ADD、DROP以及SET DATA TYPE符合SQL标准。其他形式是SQL标准的瀚高数据库扩展。在一个ALTER FOREIGN TABLE命令中指定多于一个操作也是一种扩展。

ALTER FOREIGN TABLE DROP COLUMN可以被用来删除一个外部表的唯一一列，从而留下一个没有列的表。这是一种SQL的扩展，它允许没有列的外部表。

**另见**

CREATE FOREIGN TABLE, DROP FOREIGN TABLE

### 2.12. ALTER FUNCTION

ALTER FUNCTION — 更改一个函数的定义

**大纲**

ALTER FUNCTION name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

action \[ … \] \[ RESTRICT \]

ALTER FUNCTION name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

RENAME TO new\_name

ALTER FUNCTION name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER FUNCTION name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

SET SCHEMA new\_schema

ALTER FUNCTION name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

DEPENDS ON EXTENSION extension\_name

其中 action 是以下之一：

CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT

IMMUTABLE | STABLE | VOLATILE | \[ NOT \] LEAKPROOF

\[ EXTERNAL \] SECURITY INVOKER | \[ EXTERNAL \] SECURITY DEFINER

PARALLEL { UNSAFE | RESTRICTED | SAFE }

COST execution\_cost

ROWS result\_rows

SUPPORT support\_function

SET configuration\_parameter { TO | = } { value | DEFAULT }

SET configuration\_parameter FROM CURRENT

RESET configuration\_parameter

RESET ALL

**描述**

ALTER FUNCTION更改一个函数的定义。

你必须拥有该函数以使用ALTER FUNCTION。要更改一个函数的模式，你还必须具有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有在该函数的模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建该函数做不到的事情。不过，一个超级用户怎么都能更改任何函数的所有权）。

**参数**

name

一个现有函数的名称（可以被模式限定）。如果没有指定参数列表，则该名称必须在它的模式中唯一。

argmode

一个参数的模式：IN、OUT、INOUT或者VARIADIC。如果被忽略，默认为IN。注意ALTER FUNCTION并不真正关心OUT参数，因为在决定函数的身份时只需要输入参数。因此列出IN、INOUT以及VARIADIC参数即可。

argname

一个参数的名称。注意ALTER FUNCTION并不真正参数名称，因为在确定函数的身份时只需要参数的数据类型即可。

argtype

该函数的参数（如果有）的数据类型（可以被模式限定）。

new\_name

该函数的新名称。

new\_owner

该函数的新拥有者。注意如果该函数被标记为SECURITY DEFINER，它的后续执行将会使用新拥有者。

new\_schema

该函数的新模式。

extension\_name

该函数所以来的扩展名。

CALLED ON NULL INPUT

RETURNS NULL ON NULL INPUT

STRICT

CALLED ON NULL INPUT将该函数改为在某些或者全部参数为空值时可以被调用。RETURNS NULL ON NULL INPUT或者STRICT将该函数改为只要任一参数为空值就不被调用而是自动假定一个空值结果。详见 CREATE FOREIGN TABLE 。

IMMUTABLE

STABLE

VOLATILE

把该函数的稳定性更改为指定的设置。详见 CREATE FOREIGN TABLE 。

\[ EXTERNAL \] SECURITY INVOKER

\[ EXTERNAL \] SECURITY DEFINER

更改该函数是否为一个安全性定义者。关键词EXTERNAL 是为了符合 SQL，它会被忽略。关于这项能力的详情请见 CREATE FOREIGN TABLE 。

PARALLEL

决定该函数对于并行是否安全。详见 CREATE FOREIGN TABLE 。

LEAKPROOF

更改该函数是否被认为是防泄漏的。关于这项能力的详情请见 CREATE FOREIGN TABLE 。

COST execution\_cost

更改该函数的估计执行代价。详见 CREATE FOREIGN TABLE 。

ROWS result\_rows

更改一个集合返回函数的估计行数。详见 CREATE FOREIGN TABLE 。

SUPPORT support\_function

设置或更改计划器支持函数以使用这个函数。此选项不能用于完全删除支持功能，因为它必须命名新的支持函数。如果需要这样做，可以使用CREATE OR REPLACE FUNCTION。

configuration\_parameter

value

当该函数被调用时，要对一个配置参数做出增加或者更改的赋值。如果value是DEFAULT或者使用等价的RESET，该函数本地的设置将会被移除，这样该函数会使用其环境中存在的值执行。使用RESET ALL可以清除所有函数本地的设置。SET FROM CURRENT把ALTER FUNCTION执行时该参数的当前值保存为进入该函数时要应用的值。

RESTRICT

为了符合SQL标准存在，被忽略。

**示例**

要把用于类型integer的函数sqrt重命名为square\_root：

ALTER FUNCTION sqrt(integer) RENAME TO square\_root;

要把用于类型integer的函数sqrt 的拥有者改为joe：

ALTER FUNCTION sqrt(integer) OWNER TO joe;

要把用于类型integer的函数sqrt 的模式改为maths：

ALTER FUNCTION sqrt(integer) SET SCHEMA maths;

要把类型integer的函数sqrt 标记为依赖于扩展mathlib：

ALTER FUNCTION sqrt(integer) DEPENDS ON EXTENSION mathlib;

要调整一个函数的自动搜索路径：

ALTER FUNCTION check\_password(text) SET search\_path = admin, pg\_temp;

要禁止一个函数的search\_path的自动设置：

ALTER FUNCTION check\_password(text) RESET search\_path;

这个函数将用其调用者使用的搜索路径来执行。

**兼容性**

这个语句部分兼容SQL标准中的ALTER FUNCTION语句。该标准允许修改一个函数的更多属性，但是不提供重命名一个函数、标记一个函数为安全性定义者、为一个函数附加配置参数值或者更改一个函数的拥有者、模式或者稳定性等功能。该标准还要求RESTRICT关键字，它在瀚高数据库中是可选的。

**另见**

CREATE FOREIGN TABLE, DROP FUNCTION,ALTER PROCEDURE, ALTER ROUTINE

### 2.13. ALTER GROUP

ALTER GROUP — 更改角色名称或者成员关系

**大纲**

ALTER GROUP role\_specification ADD USER user\_name \[, … \]

ALTER GROUP role\_specification DROP USER user\_name \[, … \]

其中 role\_specification 可以是：

role\_name

| CURRENT\_USER

| SESSION\_USER

ALTER GROUP group\_name RENAME TO new\_name

**描述**

ALTER GROUP更改一个用户组的属性。这是一个被废弃的命令，不过为了向后兼容还是会被接受，因为组（以及用户）已经被更一般的角色概念替代了。

前两个变体向一个组增加用户或者从一个组中移除用户（为了这个目的，任何角色都可以扮演“用户”或者“组”）。这些变体实际上等效于在被称为“组”的角色中授予或者回收成员关系，因此最好的方法是使用GRANT或者REVOKE。

第三种变体会更改该组的名称。这恰好等效于用ALTER ROLE重命名该角色。

**参数**

group\_name

要修改的组（角色）的名称。

user\_name

要被加入到该组或者从该组移除的用户（角色）。这些用户必须已经存在，ALTER GROUP不会创建或者删除用户。

new\_name

该组的新名称。

**示例**

向一个组增加用户：

ALTER GROUP staff ADD USER karl, john;

从一个组移除一个用户：

ALTER GROUP workers DROP USER beth;

**兼容性**

在 SQL 标准中没有ALTER GROUP语句。

**另见**

GRANT, REVOKE,ALTER ROLE

### 2.14. ALTER INDEX

ALTER INDEX — 更改一个索引的定义

**大纲**

ALTER INDEX \[ IF EXISTS \] name RENAME TO new\_name

ALTER INDEX \[ IF EXISTS \] name SET TABLESPACE tablespace\_name

ALTER INDEX name ATTACH PARTITION index\_name

ALTER INDEX name DEPENDS ON EXTENSION extension\_name

ALTER INDEX \[ IF EXISTS \] name SET ( storage\_parameter = value \[, … \] )

ALTER INDEX \[ IF EXISTS \] name RESET ( storage\_parameter \[, … \] )

ALTER INDEX \[ IF EXISTS \] name ALTER \[ COLUMN \] column\_number

SET STATISTICS integer

ALTER INDEX ALL IN TABLESPACE name \[ OWNED BY role\_name \[, … \] \]

SET TABLESPACE new\_tablespace \[ NOWAIT \]

**描述**

ALTER INDEX更改一个现有索引的定义。下面描述了几种子窗体。 注意每个子窗体所需的锁级别可能不同。除非显式说明，ACCESS EXCLUSIVE锁被持有。列出多个子命令时，锁的持有将是任何子命令所需的最严格的子命令。

RENAME

RENAME形式更改该索引的名称。如果索引与一个表约束（UNIQUE、PRIMARY KEY或者EXCLUDE）关联，该约束也会被重命名。这对已存储的数据没有影响。

重命名索引取得一个SHARE UPDATE EXCLUSIVE锁。

SET TABLESPACE

这种形式更改该索引的表空间为指定的表空间，并且把与该索引相关联的数据文件移动到新的表空间中。要更改一个索引的表空间，你必须拥有该索引并且具有新表空间上的CREATE特权。可以使用ALL IN TABLESPACE形式把当前数据库中在一个表空间内的所有索引全部移动到另一个表空间中，这将会锁定所有要被移动的索引然后挨个移动它们。这种形式也支持OWNED BY，即只移动属于指定角色的索引。如果指定了NOWAIT选项，那么当该命令无法立刻获得所有锁时将会失败。注意这个命令不会移动系统目录，如果想要移动系统目录，应使用ALTER DATABASE或者显式的ALTER INDEX调用。另见 CREATE TABLESPACE 。

ATTACH PARTITION

导致提到的索引变成附着于被修改的索引。提及的索引必须在包含被修改索引的表的一个分区上，并且具有一种等效的定义。一个附着索引不能被单独删除，它会在其父索引被删除时自动连带删除。

DEPENDS ON EXTENSION

这种形式把该索引标记为依赖于扩展，这样如果该扩展被删除，该索引也将被自动删除。

SET ( storage\_parameter = value \[, … \] )

这种形式为该索引更改一个或者多个索引方法相关的存储参数。可用的参数详见 CREATE INDEX 。注意这个命令不会立刻修改索引内容，根据参数你可能需要用REINDEX重建索引来得到想要的效果。

RESET ( storage\_parameter \[, … \] )

这种形式把一个或者多个索引方法相关的存储参数重置为其默认值。正如 SET一样，可能需要一次REINDEX来完全更新该索引。

ALTER \[ COLUMN \] column\_number SET STATISTICS integer

这种形式为后续的ANALYZE操作设置针对每个列的统计信息收集目标，不过只能用在被定义为表达式的索引列上。由于表达式缺少唯一的名称，我们通过该索引列的顺序号来引用它们。收集目标可以被设置为范围0到10000之间的值。另外，把它设置为-1会恢复到使用系统的默认统计信息目标（default\_statistics\_target）。

**参数**

IF EXISTS

如果该索引不存在不要抛出错误。这种情况下将发出一个提示。

column\_number

引用该索引列的顺序（从左往右）位置的顺序号。

name

要更改的一个现有索引的名称（可能被模式限定）。

new\_name

该索引的新名称。

tablespace\_name

该索引将被移动到的表空间。

extension\_name

该索引所依赖的扩展的名称。

storage\_parameter

一个索引方法相关的存储参数的名称。

value

一个索引方法相关的存储参数的新值。根据该参数，这可能是一个数字或者一个词。

**注解**

也可以用ALTER TABLE来做这些操作。实际上，ALTER INDEX只是ALTER TABLE应用在索引上的形式的别名而已。

以前有一种ALTER INDEX OWNER变体，但现在已被忽略（会出现一个警告）。一个索引的拥有者不能与其基表的拥有者不同。更改基表的拥有者会自动地更改索引的拥有者。

不允许更改系统目录索引的任何部分。

**示例**

要重命名一个现有索引：

ALTER INDEX distributors RENAME TO suppliers;

把一个索引移动到一个不同的表空间：

ALTER INDEX distributors SET TABLESPACE fasttablespace;

更改一个索引的填充因子（假设该索引方法支持填充因子）：

ALTER INDEX distributors SET (fillfactor = 75);

REINDEX INDEX distributors;

为一个表达式索引设置统计信息收集目标：

CREATE INDEX coord\_idx ON measured (x, y, (z + t));

ALTER INDEX coord\_idx ALTER COLUMN 3 SET STATISTICS 1000;

**兼容性**

ALTER INDEX是一种瀚高数据库扩展。

**另见**

CREATE INDEX, REINDEX

### 2.15. ALTER LANGUAGE

ALTER LANGUAGE — 更改一种过程语言的定义

**大纲**

ALTER \[ PROCEDURAL \] LANGUAGE name RENAME TO new\_name

ALTER \[ PROCEDURAL \] LANGUAGE name OWNER TO { new\_owner | CURRENT\_USER |

SESSION\_USER }

**描述**

ALTER LANGUAGE更改一种过程语言的定义。唯一的功能是重命名该语言或者为它赋予一个新的拥有者。要使用ALTER LANGUAGE，你必须是一个超级用户或者该语言的拥有者。

**参数**

name

语言的名称

new\_name

该语言的新名称

new\_owner

该语言的新拥有者

**兼容性**

在 SQL 标准中没有ALTER LANGUAGE语句。

**另见**

CREATE LANGUAGE, DROP LANGUAGE

### 2.16. ALTER LARGE OBJECT

ALTER LARGE OBJECT — 更改一个大对象的定义

**大纲**

ALTER LARGE OBJECT large\_object\_oid OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

**描述**

ALTER LARGE OBJECT更改一个大对象的定义。

您必须拥有大对象才能使用ALTER LARGE OBJECT。要更改所有者，您还必须是新所有者的直接或间接成员。（不过，超级用户仍然可以更改任何大对象。)当前，唯一的功能是分配新所有者，因此两者的约束都始终适用。

**参数**

large\_object\_oid

要被修改的大对象的 OID

new\_owner

该大对象的新拥有者

**兼容性**

在 SQL 标准中没有ALTER LARGE OBJECT 语句。

### 2.17. ALTER MATERIALIZED VIEW

ALTER MATERIALIZED VIEW — 更改一个物化视图的定义

**大纲**

ALTER MATERIALIZED VIEW \[ IF EXISTS \] name

action \[, … \]

ALTER MATERIALIZED VIEW name

DEPENDS ON EXTENSION extension\_name

ALTER MATERIALIZED VIEW \[ IF EXISTS \] name

RENAME \[ COLUMN \] column\_name TO new\_column\_name

ALTER MATERIALIZED VIEW \[ IF EXISTS \] name

RENAME TO new\_name

ALTER MATERIALIZED VIEW \[ IF EXISTS \] name

SET SCHEMA new\_schema

ALTER MATERIALIZED VIEW ALL IN TABLESPACE name \[ OWNED BY role\_name \[, … \] \]

SET TABLESPACE new\_tablespace \[ NOWAIT \]

其中 action是下列之一：

ALTER \[ COLUMN \] column\_name SET STATISTICS integer

ALTER \[ COLUMN \] column\_name SET ( attribute\_option = value \[, … \] )

ALTER \[ COLUMN \] column\_name RESET ( attribute\_option \[, … \] )

ALTER \[ COLUMN \] column\_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED |

MAIN }

CLUSTER ON index\_name

SET WITHOUT CLUSTER

SET ( storage\_parameter = value \[, … \] )

RESET ( storage\_parameter \[, … \] )

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

**描述**

ALTER MATERIALIZED VIEW更改一个现有物化视图的多个辅助属性。

要使用ALTER MATERIALIZED VIEW，你必须拥有该物化视图。要更改一个物化视图的模式，你还必须拥有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须拥有该物化视图所在模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建该物化视图做不到的事情。不过，一个超级用户怎么都能更改任何视图的所有权。）。

DEPENDS ON EXTENSION形式把该物化视图标记为依赖于一个扩展，这样该扩展被删除时会自动地删除掉这个物化视图。

可用于ALTER MATERIALIZED VIEW的语句形式和动作是ALTER TABLE的一个子集，并且在用于物化视图时具有相同的含义。详见 ALTER ROLE 的描述。

**参数**

name

一个现有物化视图的名称（可以是模式限定的）。

column\_name

一个新的或者现有的列的名称。

extension\_name

该物化视图所依赖的扩展的名称。

new\_column\_name

一个现有列的新名称。

new\_owner

该物化视图的新拥有者的用户名。

new\_name

该物化视图的新名称。

new\_schema

该物化视图的新模式。

**示例**

把物化视图foo重命名为 bar：

ALTER MATERIALIZED VIEW foo RENAME TO bar;

**兼容性**

ALTER MATERIALIZED VIEW是一种瀚高数据库扩展。

**另见**

CREATE MATERIALIZED VIEW, DROP MATERIALIZED VIEW, REFRESH MATERIALIZED VIEW

### 2.18. ALTER OPERATOR

ALTER OPERATOR — 更改一个操作符的定义

**大纲**

ALTER OPERATOR name ( { left\_type | NONE }, { right\_type | NONE } )

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER OPERATOR name ( { left\_type | NONE }, { right\_type | NONE } )

SET SCHEMA new\_schema

ALTER OPERATOR name ( { left\_type | NONE }, { right\_type | NONE } )

SET ( { RESTRICT = { res\_proc | NONE }

| JOIN = { join\_proc | NONE }

} \[, … \] )

**描述**

ALTER OPERATOR更改一个操作符的定义。

要使用ALTER OPERATOR，你必须拥有该操作符。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该操作符所在模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建操作符做不到的事情。不过，一个超级用户怎么都能更改任何操作符的所有权。）。

**参数**

name

一个现有操作符的名称（可以是模式限定的）。

left\_type

该操作符左操作数的数据类型，如果该操作符没有左操作数可以写成 NONE。

right\_type

该操作符右操作数的数据类型，如果该操作符没有右操作数可以写成 NONE。

new\_owner

该操作符的新拥有者。

new\_schema

该操作符的新模式。

res\_proc

这个操作符的约束选择度估算器函数，写成 NONE 可以移除现有的选择度估算器。

join\_proc

这个操作符的连接选择度估算器函数，写成 NONE 可以移除现有的选择度估算器。

**示例**

更改类型text的一个自定义操作符a @@ b 的拥有者：

ALTER OPERATOR @@ (text, text) OWNER TO joe;

更改类型int\[\]的自定义操作符a && b的约束和连接选择度估算器函数：

ALTER OPERATOR && (\_int4, \_int4) SET (RESTRICT = \_int\_contsel, JOIN = \_int\_contjoinsel);

**兼容性**

在 SQL 标准中没有ALTER OPERATOR语句。

**另见**

CREATE OPERATOR, DROP OPERATOR

### 2.19. ALTER OPERATOR CLASS

ALTER OPERATOR CLASS — 更改一个操作符类的定义

**大纲**

ALTER OPERATOR CLASS name USING index\_method

RENAME TO new\_name

ALTER OPERATOR CLASS name USING index\_method

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER OPERATOR CLASS name USING index\_method

SET SCHEMA new\_schema

**描述**

ALTER OPERATOR CLASS更改一个操作符类的定义。

要使用ALTER OPERATOR CLASS，你必须拥有该操作符类。要修改拥有者，你还必须是新拥有角色的一个直接或间接成员，并且该角色必须具有该操作符类所在模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建操作符类做不到的事情。不过，一个超级用户怎么都能更改任何操作符类的所有权。）。

**参数**

name

一个现有操作符类的名称（可以是模式限定的）。

index\_method

这个操作符类所服务的索引方法的名称。

new\_name

该操作符类的新名称。

new\_owner

该操作符类的新拥有者。

new\_schema

该操作符类的新模式。

**兼容性**

在 SQL 标准中没有ALTER OPERATOR CLASS语句。

**另见**

CREATE OPERATOR CLASS, DROP OPERATOR CLASS, ALTER OPERATOR FAMILY

### 2.20. ALTER OPERATOR FAMILY

ALTER OPERATOR FAMILY — 更改一个操作符族的定义

**大纲**

ALTER OPERATOR FAMILY name USING index\_method ADD

{ OPERATOR strategy\_number operator\_name ( op\_type, op\_type )

\[ FOR SEARCH | FOR ORDER BY sort\_family\_name \]

| FUNCTION support\_number \[ ( op\_type \[, op\_type \] ) \]

function\_name \[ ( argument\_type \[, …\] ) \]

} \[, … \]

ALTER OPERATOR FAMILY name USING index\_method DROP

{ OPERATOR strategy\_number ( op\_type \[, op\_type \] )

| FUNCTION support\_number ( op\_type \[, op\_type \] )

} \[, … \]

ALTER OPERATOR FAMILY name USING index\_method

RENAME TO new\_name

ALTER OPERATOR FAMILY name USING index\_method

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER OPERATOR FAMILY name USING index\_method

SET SCHEMA new\_schema

**描述**

ALTER OPERATOR FAMILY更改一个操作符族的定义。你能增加操作符以及支持函数到该家族、从该族中移除它们或者更改该族的名称或者拥有者。

在用ALTER OPERATOR FAMILY增加操作符和支持函数到一个族中时，它们不是族内任何特定操作符类的组成部分，而只是“松散”地存在于该族中。这表示这些操作符和函数与该族的语义兼容，但是没有被任何特定索引的正确功能所要求（所要求的操作符和函数应该被作为一个操作符类的一部分声明，见CREATE OPERATOR CLASS）。 瀚高数据库将允许一个族的松散成员在任何时候被从该族中删除，但是在删除一个操作符类的成员之前，必须已经删除整个类以及依赖于该成员的索引。具有代表性的是，单一数据类型操作符和函数是操作符类的一部分，因为在特定数据类型上的索引需要它们的支持。而多数据类型操作符和函数则被作为该族的松散成员。

要使用ALTER OPERATOR FAMILY，你必须是超级用户（做这样的限制是因为一个错误的操作符族定义可能会迷惑服务器甚至让它崩溃）。

ALTER OPERATOR FAMILY目前不检测操作符族定义是否包括该索引方法所要求的所有操作符和函数，也不检查操作符和函数是否形成了一个有理的集合。定义一个合法的操作符族是用户的责任。

**参数**

name

一个现有操作符族的名称（可以是模式限定的）。

index\_method

这个操作符族所应用的索引方法的名称。

strategy\_number

与该操作符族相关的一个操作符的索引方法策略号。

operator\_name

与该操作符族相关的一个操作符的名称（可以是模式限定的）。

op\_type

在一个OPERATOR子句中指定该操作符的操作数数据类型，或者用NONE来表示一个左一元或者右一元操作符。不同于CREATE OPERATOR CLASS中类似的语法，操作数数据类型总是必须被指定。

在一个ADD FUNCTION子句中指定该函数意图支持的操作数数据类型（如果不同于该函数的输入数据类型）。对于B-树比较函数和哈希函数，有必要指定op\_type，因为该函数的输入数据类型总是正确的。对于B-树排序支持函数和GiST、SP-GiST和GIN操作符类中的所有函数，有必要指定该函数要使用的操作数数据类型。

在一个DROP FUNCTION子句中，必须指定该函数要支持的操作数数据类型。

sort\_family\_name

一个现有btree操作符族的名称（可能是模式限定的）， 它描述与一个排序操作符相关的排序顺序。

如果既没有指定FOR SEARCH也没有指定FOR ORDER BY， 默认值是FOR SEARCH。

support\_number

一个与该操作符族相关的函数的索引方法支持过程编号。

function\_name

作为该操作符族的一种索引方法支持函数的函数名称（可以是模式限定的）。 如果没有指定参数列表，则该名称必须在其模式中唯一。

argument\_type

该函数的参数数据类型。

new\_name

该操作符族的新名称。

new\_owner

该操作符族的新拥有者。

new\_schema

该操作符族的新模式。

OPERATOR和FUNCTION子句可以以任何顺序出现。

**注解**

注意DROP语法只通过策略或者支持号以及输入数据类型指定该操作符族中的“slot”。占用这个槽的操作符或函数的名称不会被提及。还有，对于DROP FUNCTION，要指定的类型是该函数意图支持的输入数据类型。对于GiST、SP-GiST以及GIN索引，可能无需对该函数的实际输入参数类型做任何事情。

因为索引机制在使用函数之前不会检查其上的访问权限，包括一个操作符族中的函数或操作符都等同于授予了其上的公共执行权限。这对于操作符族中很有用的这类函数来说，这通常不成问题。

操作符应该由SQL函数定义。一个SQL函数很可能被内联到调用查询中，这将阻止优化器识别出该查询匹配一个索引。

**示例**

下列示例命令为一个操作符族增加跨数据类型的操作符和支持函数，该操作符族已经包含用于数据类型int4以及int2的B-树操作符类。

ALTER OPERATOR FAMILY integer\_ops USING btree ADD

– int4 vs int2

OPERATOR 1 < (int4, int2),

OPERATOR 2 <= (int4, int2),

OPERATOR 3 = (int4, int2),

OPERATOR 4 >= (int4, int2),

OPERATOR 5 > (int4, int2),

FUNCTION 1 btint42cmp(int4, int2),

– int2 vs int4

OPERATOR 1 < (int2, int4),

OPERATOR 2 <= (int2, int4),

OPERATOR 3 = (int2, int4),

OPERATOR 4 >= (int2, int4),

OPERATOR 5 > (int2, int4),

FUNCTION 1 btint24cmp(int2, int4);

再次移除这些项：

ALTER OPERATOR FAMILY integer\_ops USING btree DROP

– int4 vs int2

OPERATOR 1 (int4, int2),

OPERATOR 2 (int4, int2),

OPERATOR 3 (int4, int2),

OPERATOR 4 (int4, int2),

OPERATOR 5 (int4, int2),

FUNCTION 1 (int4, int2),

– int2 vs int4

OPERATOR 1 (int2, int4),

OPERATOR 2 (int2, int4),

OPERATOR 3 (int2, int4),

OPERATOR 4 (int2, int4),

OPERATOR 5 (int2, int4),

FUNCTION 1 (int2, int4);

**兼容性**

在 SQL 标准中没有 ALTER OPERATOR FAMILY语句。

**另见**

CREATE OPERATOR FAMILY, DROP OPERATOR FAMILY, CREATE OPERATOR CLASS, ALTER OPERATOR

CLASS, DROP OPERATOR CLASS

### 2.21. ALTER POLICY

ALTER POLICY — 更改一条行级安全性策略的定义

**大纲**

ALTER POLICY name ON table\_name RENAME TO new\_name

ALTER POLICY name ON table\_name

\[ TO { role\_name | PUBLIC | CURRENT\_USER | SESSION\_USER } \[, …\] \]

\[ USING ( using\_expression ) \]

\[ WITH CHECK ( check\_expression ) \]

**描述**

ALTER POLICY更改一条现有行级安全性策略的定义。请注意，ALTER POLICY只允许修改策略所应用的角色集合，和要修改的USING和WITH CHECK表达式。要更改策略的其他属性，例如其应用的命令，或者是允许还是限制，则必须删除并重新创建策略。

要使用ALTER POLICY，你必须拥有该策略所适用的表。

在ALTER POLICY的第二种形式中，如果指定了角色列表、using\_expression以及check\_expression，它们会被独立地替换。当这些子句之一被省略时，策略的对应部分不会被更改。

**参数**

name

要更改的现有策略的名称。

table\_name

该策略所在的表的名称（可以被模式限定）。

new\_name

该策略的新名称。

role\_name

该策略适用的角色。可以一次指定多个角色。要把该策略应用于所有角色，可使用PUBLIC。

using\_expression

该策略的USING表达式。详见 CREATE POLICY 。

check\_expression

该策略的WITH CHECK表达式。详见 CREATE POLICY 。

**兼容性**

ALTER POLICY是一种瀚高数据库扩展。

**另见**

CREATE POLICY, DROP POLICY

### 2.22. ALTER PROCEDURE

ALTER PROCEDURE — 更改一个过程的定义

**大纲**

ALTER PROCEDURE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

action \[ … \] \[ RESTRICT \]

ALTER PROCEDURE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

RENAME TO new\_name

ALTER PROCEDURE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER PROCEDURE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

SET SCHEMA new\_schema

ALTER PROCEDURE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

DEPENDS ON EXTENSION extension\_name

其中action是下列之一：

\[ EXTERNAL \] SECURITY INVOKER | \[ EXTERNAL \] SECURITY DEFINER

SET configuration\_parameter { TO | = } { value | DEFAULT }

SET configuration\_parameter FROM CURRENT

RESET configuration\_parameter

RESET ALL

**简介**

ALTER PROCEDURE更改一个过程的定义。

要使用ALTER PROCEDURE，你必须拥有该过程。要更改一个过程的方案，你还必须有新方案上的CREATE特权。要更改拥有者，你还必须是新拥有角色的直接或间接成员，并且那个角色在该过程的方案上拥有CREATE特权（这些限制强制更新拥有者无法做到通过删除和重建该过程无法做到的事情。不过，超级用户总是能够更改任何过程的拥有关系）。

**参数**

name

一个现有的过程的名字（可以被方案限定）。如果没有指定参数列表，这个名字必须在其方案中唯一。

argmode

参数的模式：IN或VARIADIC。如果被省略，默认是IN。

argname

参数的名字。注意ALTER PROCEDURE实际上并不关心参数名，因为只需要参数的数据类型来确定过程的身份。

argtype

如果该过程有参数，这是参数的数据类型（可以被方案限定）。

new\_name

该过程的新名字。

new\_owner

该过程的新拥有者。注意，如果这个过程被标记为SECURITY DEFINER，接下来它将被作为新拥有者执行。

new\_schema

该过程的新方案。

extension\_name

该过程所依赖的扩展的名称。

\[ EXTERNAL \] SECURITY INVOKER

\[ EXTERNAL \] SECURITY DEFINER

更改该过程是否为一个安全性定义器。关键词EXTERNAL由于SQL符合性的原因被忽略。更多有关这个能力的信息请见 CREATE PROCEDURE 。

configuration\_parameter

value

增加或者更改在调用该过程时，要对一个配置参数做的赋值。如果value是DEFAULT或者等效的值，则会使用RESET，过程本地的设置会被移除，这样该过程的执行就会使用其所处环境中的值。使用RESET ALL可以清除所有的过程本地设置。SET FROM CURRENT会把ALTER PROCEDURE执行时该参数的当前值保存为进入该过程时要被应用的值。

RESTRICT

为了符合SQL标准会被忽略。

**示例**

要重命名具有两个integer类型参数的过程insert\_data为insert\_record：

ALTER PROCEDURE insert\_data(integer, integer) RENAME TO insert\_record;

要把具有两个integer类型参数的过程insert\_data的拥有者改为joe：

ALTER PROCEDURE insert\_data(integer, integer) OWNER TO joe;

要重把具有两个integer类型参数的过程insert\_data的方案改为accounting：

ALTER PROCEDURE insert\_data(integer, integer) SET SCHEMA accounting;

把过程insert\_data(integer, integer)标记为依赖于扩展myext：

ALTER PROCEDURE insert\_data(integer, integer) DEPENDS ON EXTENSION myext;

要调整一个过程自动设置的搜索路径：

ALTER PROCEDURE check\_password(text) SET search\_path = admin, pg\_temp;

要为一个过程禁用search\_path的自动设置：

ALTER PROCEDURE check\_password(text) RESET search\_path;

现在这个过程将用其调用者所使用的任何搜索路径执行。

**兼容性**

这个语句与SQL标准中的ALTER PROCEDURE语句部分兼容。标注你允许修改一个过程的更多性质，但是不提供重命名过程、让过程成为安全性定义器、为过程附加配置参数值或者更改过程的拥有者、方案或者可变性的能力。标准还要求RESTRICT关键字，而它在瀚高数据库中是可选的。

**另见**

CREATE PROCEDURE, DROP PROCEDURE,ALTER FUNCTION, ALTER ROUTINE

### 2.23. ALTER PUBLICATION

ALTER PUBLICATION — 修改发布的定义

**大纲**

ALTER PUBLICATION name ADD TABLE \[ ONLY \] table\_name \[ \* \] \[, …\]

ALTER PUBLICATION name SET TABLE \[ ONLY \] table\_name \[ \* \] \[, …\]

ALTER PUBLICATION name DROP TABLE \[ ONLY \] table\_name \[ \* \] \[, …\]

ALTER PUBLICATION name SET ( publication\_parameter \[= value\] \[, … \] )

ALTER PUBLICATION name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER PUBLICATION name RENAME TO new\_name

**描述**

命令ALTER PUBLICATION可以更改发布的属性。

前三个语句更改哪些表是该发布的一部分。SET TABLE子句用指定的表替换发布中的表的列表。ADD TABLE和 DROP TABLE子句将从发布中添加和删除一个或多个表。请注意，将表添加到已订阅的发布中将需要在订阅端执行ALTER SUBSCRIPTION … REFRESH PUBLICATION操作才能生效。

第四条语句可以改变在CREATE PUBLICATION中指定的所有发布属性。该命令中未提及的属性保留其先前的设置。

其余语句更改所有者和发布的名称。

你必须拥有该发布才能使用ALTER PUBLICATION。要改变所有者，你也必须是新所有者角色的直接或间接成员。新的所有者必须在数据库上拥有CREATE权限。此外，FOR ALL TABLES发布的新所有者必须是超级用户。但是，超级用户可以在避开这些限制的情况下更改发布的所有权。

**参数**

name

要修改定义的现有发布的名称。

table\_name

现有表的名称。如果在表名之前指定了ONLY，则只有该表受到影响。如果没有指定ONLY，则该表及其所有后代表（如果有的话）都会受到影响。可选地，可以在表名之后指定\*以明确指示包含后代表。

SET ( publication\_parameter \[= value\] \[, … \] )

该子句修改最初由CREATE PUBLICATION设置的发布参数。

new\_owner

发布的新所有者的用户名。

new\_name

发布的新名称。

**示例**

将发布修改为只发布删除和更新：

ALTER PUBLICATION noinsert SET (publish = ‘update, delete’);

给发布添加一些表：

ALTER PUBLICATION mypublication ADD TABLE users, departments;

**兼容性**

ALTER PUBLICATION是瀚高数据库的一个扩展。

**另见**

CREATE PUBLICATION, DROP PUBLICATION,CREATE SUBSCRIPTION, ALTER SUBSCRIPTION

### 2.24. ALTER ROLE

ALTER ROLE — 更改一个数据库角色

**大纲**

ALTER ROLE role\_specification \[ WITH \] option \[ … \]

其中option可以是：

SUPERUSER | NOSUPERUSER

| CREATEDB | NOCREATEDB

| CREATEROLE | NOCREATEROLE

| INHERIT | NOINHERIT

| LOGIN | NOLOGIN

| REPLICATION | NOREPLICATION

| BYPASSRLS | NOBYPASSRLS

| CONNECTION LIMIT connlimit

| \[ ENCRYPTED \] PASSWORD ‘password’

| VALID UNTIL ‘timestamp’

ALTER ROLE name RENAME TO new\_name

ALTER ROLE { role\_specification | ALL } \[ IN DATABASE database\_name \]

SET configuration\_parameter { TO | = } { value | DEFAULT }

ALTER ROLE { role\_specification | ALL } \[ IN DATABASE database\_name \]

SET configuration\_parameter FROM CURRENT

ALTER ROLE { role\_specification | ALL } \[ IN DATABASE database\_name \]

RESET configuration\_parameter

ALTER ROLE { role\_specification | ALL } \[ IN DATABASE database\_name \] RESET ALL其中role\_specification可以是：

role\_name

| CURRENT\_USER

| SESSION\_USER

**描述**

ALTER ROLE更改一个瀚高数据库角色的属性。

前面列出的这个命令的第一种变体能够更改CREATE ROLE中指定的很多角色属性（覆盖了所有可能的属性，不过没有增加和移除成员关系的选项，如果要增加和移除成员关系可使用GRANT和REVOKE）。该命令中没有提到的属性保持它们之前的设置。数据库超级用户能够更改任何角色的任何这些设置。具有CREATEROLE特权的角色能够更改任何这些设置，但是只能为非超级用户和非复制角色修改。普通角色只能更改它们自己的口令。

第二种变体更改该角色的名称。数据库超级用户能重命名任何角色。具有CREATEROLE特权的角色能够重命名任何非超级用户角色。当前的会话用户不能被重命名（如果需要这样做，请以一个不同的用户连接）。

其余的变体用于更改一个角色的配置变量的会话默认值，可以为所有数据库设置，或者只为IN DATABASE中指定的数据库设置。如果指定的是ALL而不是一个角色名，将会为所有角色更改该设置。把ALL和IN DATABASE一起使用实际上和使用命令ALTER DATABASE … SET …相同。

只要改角色后续开始一个新会话，指定的值将会成为该会话的默认值，并且会覆盖postgresql.conf中存在的值或者从postgres命令行收到的值。这只在登录时发生，执行SET ROLE或者 SET SESSION AUTHORIZATION不会导致新的配置值被设置。对于所有数据库设置的值会被附加到一个角色的数据库相关的设置所覆盖。特定数据库或角色的设置会覆盖为所有角色所作的设置。

超级用户能够更改任何人的会话默认值。具有CREATEROLE特权的角色能够更改非超级用户的默认值。普通角色只能为它们自己设置默认值。某些配置变量不能以这种方式设置，或者只能由一个超级用户发出的命令设置。只有超级用户能够更改所有角色在所有数据库中的设置。

**参数**

name

要对其属性进行修改的角色的名称。

CURRENT\_USER

修改当前用户而不是一个显式标识的角色。

SESSION\_USER

修改当前会话用户而不是一个显式标识的角色。

SUPERUSER

NOSUPERUSER

CREATEDB

NOCREATEDB

CREATEROLE

NOCREATEROLE

INHERIT

NOINHERIT

LOGIN

NOLOGIN

REPLICATION

NOREPLICATION

BYPASSRLS

NOBYPASSRLS

CONNECTION LIMIT connlimit

\[ ENCRYPTED \] PASSWORD ‘password’

VALID UNTIL ‘timestamp’

这些子句修改原来有CREATE ROLE 设置的属性。更多信息请见 CREATE ROLE 参考页。

new\_name

该角色的新名称。

database\_name

要在其中设置该配置变量的数据库名称。

configuration\_parameter

value

把这个角色的指定配置参数的会话默认值设置为给定值。如果value为DEFAULT或者等效地使用了RESET，角色相关的变量设置会被移除，这样该角色将会在新会话中继承系统范围的默认设置。使用RESET ALL可清除所有角色相关的设置。SET FROM CURRENT可以把会话中该参数的当前值保存为角色相关的值。如果指定了 IN DATABASE，只会为给定的角色和数据库设置或者移除该配置参数。

角色相关的变量设置只在登录时生效，SET ROLE以及SET SESSION AUTHORIZATION不会处理角色相关的变量设置。

**注解**

使用CREATE ROLE增加新角色，使用DROP ROLE移除一个角色。

ALTER ROLE无法更改一个角色成员关系。可以使用GRANT和REVOKE来实现。

在使用这个命令指定一个未加密口令时要多加小心。该口令将会以明文传送到服务器，并且它还可能会被记录在客户端的命令历史或者服务器日志中。psql包含了一个命令\\password，它可以被用来更改一个角色的口令而不暴露明文口令。

也可以把一个会话默认值绑定到一个指定的数据库而不是一个角色，详见 ALTER DATABASE 。

如果出现冲突，数据库角色相关的设置会覆盖角色相关的设置，角色相关的又会覆盖数据库相关的设置。

**示例**

更改一个角色的口令：

ALTER ROLE davide WITH PASSWORD ‘hu8jmn3’;

更改一个口令的失效日期，指定该口令应该在 2015 年 5 月 4 日中午 （在一个比UTC快 1小时的时区）过期：

ALTER ROLE chris VALID UNTIL ‘May 4 12:00:00 2015 +1’;

让一个口令永远有效：

ALTER ROLE fred VALID UNTIL ‘infinity’;

让一个角色能够创建其他角色和新的数据库：

ALTER ROLE miriam CREATEROLE CREATEDB;

为一个角色指定 maintenance\_work\_mem参数的非默认设置：

ALTER ROLE worker\_bee SET maintenance\_work\_mem = 100000;

为一个角色指定 client\_min\_messages参数的数据库相关的非默认设置：

ALTER ROLE fred IN DATABASE devel SET client\_min\_messages = DEBUG;

**兼容性**

ALTER ROLE语句是一个瀚高数据库扩展。

**另见**

CREATE ROLE, DROP ROLE,ALTER DATABASE, SET

### 2.25. ALTER ROUTINE

ALTER ROUTINE — 更改一个例程的定义

**大纲**

ALTER ROUTINE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

action \[ … \] \[ RESTRICT \]

ALTER ROUTINE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

RENAME TO new\_name

ALTER ROUTINE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER ROUTINE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

SET SCHEMA new\_schema

ALTER ROUTINE name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, …\] \] ) \]

DEPENDS ON EXTENSION extension\_name

其中action是下列之一：

IMMUTABLE | STABLE | VOLATILE | \[ NOT \] LEAKPROOF

\[ EXTERNAL \] SECURITY INVOKER | \[ EXTERNAL \] SECURITY DEFINER

PARALLEL { UNSAFE | RESTRICTED | SAFE }

COST execution\_cost

ROWS result\_rows

SET configuration\_parameter { TO | = } { value | DEFAULT }

SET configuration\_parameter FROM CURRENT

RESET configuration\_parameter

RESET ALL

**描述**

ALTER ROUTINE更改一个例程的定义，它可以是聚集函数、普通函数或者过程。参数的描述、更多的例子以及进一步的细节请参考 ALTER AGGREGATE 、 ALTER FUNCTION 以及 ALTER PROCEDURE 。

**示例**

将类型integer的例程foo重命名为foobar：

ALTER ROUTINE foo(integer) RENAME TO foobar;

不管foo是聚集、函数还是过程，这个命令都能使用。

**兼容性**

这个语句与SQL标准中的ALTER ROUTINE语句部分兼容。更多细节请参考 ALTER FUNCTION 和 ALTER PROCEDURE 。允许例程名称引用聚集函数是一种瀚高数据库的扩展。

**另见**

ALTER AGGREGATE,ALTER FUNCTION,ALTER PROCEDURE, DROP ROUTINE

注意没有CREATE ROUTINE命令。

### 2.26. ALTER RULE

ALTER RULE — 更改一个规则定义

**大纲**

ALTER RULE name ON table\_name RENAME TO new\_name

**描述**

ALTER RULE更改一条现有规则的定义。当前，唯一可用的动作是更改规则的名称。

要使用ALTER RULE，你必须拥有该规则适用的表或者视图。

**参数**

name

要修改的一条现有规则的名称。

table\_name

该规则适用的表或视图的名称（可以是模式限定的）。

new\_name

该规则的新名称。

**示例**

要重命名一条现有的规则：

ALTER RULE notify\_all ON emp RENAME TO notify\_me;

**兼容性**

ALTER RULE是一种瀚高数据库的语言扩展。

**另见**

CREATE RULE, DROP RULE

### 2.27. ALTER SCHEMA

ALTER SCHEMA — 更改一个模式的定义

**大纲**

ALTER SCHEMA name RENAME TO new\_name

ALTER SCHEMA name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

**描述**

ALTER SCHEMA更改一个模式的定义。

要使用ALTER SCHEMA，你必须拥有该模式。要重命名一个模式，你还必须拥有该数据库的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该数据库上的CREATE特权（注意超级用户自动拥有所有这些特权）。

**参数**

name

一个现有模式的名称。

new\_name

该模式的新名称。新名称不能以pg\_开始，因为这些名称被 保留用于系统模式。

new\_owner

该模式的新拥有者。

**兼容性**

在 SQL 标准中没有ALTER SCHEMA语句。

**另见**

CREATE SCHEMA, DROP SCHEMA

### 2.28. ALTER SEQUENCE

ALTER SEQUENCE — 更改一个序列发生器的定义

**大纲**

ALTER SEQUENCE \[ IF EXISTS \] name

\[ AS data\_type \]

\[ INCREMENT \[ BY \] increment \]

\[ MINVALUE minvalue | NO MINVALUE \] \[ MAXVALUE maxvalue | NO MAXVALUE \]

\[ START \[ WITH \] start \]

\[ RESTART \[ \[ WITH \] restart \] \]

\[ CACHE cache \] \[ \[ NO \] CYCLE \]

\[ OWNED BY { table\_name.column\_name | NONE } \]

ALTER SEQUENCE \[ IF EXISTS \] name OWNER TO { new\_owner | CURRENT\_USER |

SESSION\_USER }

ALTER SEQUENCE \[ IF EXISTS \] name RENAME TO new\_name

ALTER SEQUENCE \[ IF EXISTS \] name SET SCHEMA new\_schema

**描述**

ALTER SEQUENCE更改一个现有序列发生器的参数。任何没有在ALTER SEQUENCE命令中明确设置的参数保持它们之前的设置。

要使用ALTER SEQUENCE，你必须拥有该序列。要更改一个序列的模式，你还必须拥有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该域的模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建该序列做不到的事情。不过，一个超级用户怎么都能更改任何序列的所有权。）。

**参数**

name

要修改的序列的名称（可以是模式限定的）。

IF EXISTS

在序列不存在时不要抛出一个错误。这种情况下会发出一个提示。

data\_type

可选子句AS data\_type 改变序列的数据类型。有效类型是smallint、integer和bigint。

当且仅当先前的最小值和最大值是旧数据类型的最小值或最大值时（换句话说，如果序列是使用NO MINVALUE或NO MAXVALUE，隐式或显式创建的），则更改数据类型会自动更改序列的最小值和最大值。否则，将保留最小值和最大值，除非将新值作为同一命令的一部分给出。如果最小值和最大值不符合新的数据类型，则会生成错误。

increment

子句INCREMENT BY increment是可选的。一个正值将产生一个上升序列，一个负值会产生一个下降序列。如果没有指定，旧的增量值将被保持。

minvalue

NO MINVALUE

可选的子句MINVALUEminvalue决定一个序列能产生的最小值。如果指定了NO MINVALUE，上升序列和下降序列的默认值分别是1和数据类型的最小值。如果这些选项都没有被指定，将保持当前的最小值。

maxvalue

NO MAXVALUE

可选的子句MAXVALUE maxvalue决定一个序列能产生的最大值。如果指定了NO MAXVALUE，上升序列和下降序列的默认值分别是数据类型的最大值和-1。如果这些选项都没有被指定，将保持当前的最大值。

start

可选的子句START WITH start更改该序列被记录的开始值。这对于当前序列值没有影响，它会简单地设置未来ALTER SEQUENCE RESTART命令将会使用的值。

restart

可选的子句RESTART \[ WITH restart \]更改该序列的当前值。这类似于用is\_called = false调用setval函数：被指定的值将会被下一次nextval调用返回。写上没有restart值的RESTART等效于提供被CREATE SEQUENCE记录的或者上一次被ALTER SEQUENCE START WITH设置的开始值。

与setval调用相比，序列上的RESTART操作是事务性的并阻止并发事务从同一序列中获取数字。如果这不是所需的操作模式，则应使用setval。

cache

子句CACHE cache使得序列数字被预先分配并且保存在内存中以便更快的访问。最小值是1（每次只产生一个值，即无缓存）。如果没有指定，旧的缓冲值将被保持。

CYCLE

可选的CYCLE关键词可以被用来允许该序列在达到maxvalue（上升序列）或minvalue（下降序列）时回卷。如果到达该限制，下一个被产生的数字将分别是minvalue或者maxvalue。

NO CYCLE

如果指定了可选的NO CYCLE关键词，任何在该序列到达其最大值后的nextval调用将会返回一个错误。如果既没有指定CYCLE也没有指定NO CYCLE，旧的循环行为将被保持。

OWNED BY table\_name.column\_name

OWNED BY NONE

OWNED BY选项导致该序列与一个特定的表列相关联，这样如果该列（或者整个表）被删除，该序列也会被自动删除。如果指定，这种关联会替代之前为该序列指定的任何关联。被指定的表必须具有相同的拥有者并且与该序列在同一个模式中。指定OWNED BY NONE可以移除任何现有的关联。

new\_owner

该序列的新拥有者的用户名。

new\_name

该序列的新名称。

new\_schema

该序列的新模式。

**注解**

ALTER SEQUENCE将不会立即影响除当前后端外其他后端中的nextval结果，因为它们有预分配（缓存）的序列值。在注意到序列生成参数被更改之前它们将用尽所有缓存的值。当前后端将被立刻影响。

ALTER SEQUENCE不会影响该序列的currval状态。

ALTER SEQUENCE阻塞并发nextval、currval、lastval和setval调用。

由于历史原因，ALTER TABLE也可以被用于序列，但是只有等效于上述形式的ALTER TABLE变体才被允许用于序列。

**示例**

在105重启一个被称为serial的序列：

ALTER SEQUENCE serial RESTART WITH 105;

**兼容性**

ALTER SEQUENCE符合SQL 标准，不过AS、START WITH、 OWNED BY、OWNER TO、RENAME TO 以及SET SCHEMA子句是瀚高数据库扩展。

**另见**

CREATE SEQUENCE, DROP SEQUENCE

### 2.29. ALTER SERVER

ALTER SERVER — 更改一个外部服务器的定义

**大纲**

ALTER SERVER name \[ VERSION ‘new\_version’ \]

\[ OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \] ) \]

ALTER SERVER name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER SERVER name RENAME TO new\_name

**描述**

ALTER SERVER更改一个外部服务器的定义。第一种形式更改该服务器的版本字符串或者该服务器的一般选项（至少要求一个子句）。第二种形式更改该服务器的拥有者。

要修改该服务器，你必须是它的拥有者。此外为了修改拥有者，你必须拥有该服务器并且是新拥有角色的一个直接或者间接成员，并且你必须具有该服务器的外部数据包装器上的USAGE特权（注意超级用户自动满足所有这些政策）。

**参数**

name

一个现有服务器的名称。

new\_version

新的服务器版本。

OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \] )

更改该服务器的选项。ADD、SET和DROP指定要执行的动作。如果没有显式地指定操作，将会假定为ADD。选项名称必须唯一，名称和值也会使用该服务器的外部数据包装器库进行验证。

new\_owner

该外部服务器的新拥有者的用户名。

new\_name

该外部服务器的新名称。

**示例**

修改服务器foo，增加连接选项：

ALTER SERVER foo OPTIONS (host ‘foo’, dbname ‘foodb’);

修改服务器foo，更改版本、更改host选项：

ALTER SERVER foo VERSION ‘10.2’ OPTIONS (SET host ‘baz’);

**兼容性**

ALTER SERVER符合 ISO/IEC 9075-9 (SQL/MED)。 OWNER TO和RENAME形式是 瀚高数据库扩展。

**另见**

CREATE SERVER, DROP SERVER

### 2.30. ALTER STATISTICS

ALTER STATISTICS — 更改扩展统计对象的定义

**大纲**

ALTER STATISTICS name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER STATISTICS name RENAME TO new\_name

ALTER STATISTICS name SET SCHEMA new\_schema

**描述**

ALTER STATISTICS更改现有扩展统计对象的参数。任何在ALTER STATISTICS命令中没有明确设定的参数保持它们之前的设置。

您必须拥有统计对象才能使用ALTER STATISTICS。要更改统计对象的模式，还必须在新模式上具有CREATE权限。要更改所有者，还必须是新所有者角色的直接或间接成员，且该角色在统计对象的模式上必须具有CREATE权限。（这些限制强制了通过删除和重新创建统计对象来改变所有者不会做任何你不能做的事情，但是超级用户可以改变任何统计对象的所有权。）

**参数**

name

要修改的统计对象的名称（可能有模式修饰）。

new\_owner

统计对象的新所有者的用户名。

new\_name

统计对象的新名称。

new\_schema

统计对象的新模式。

**兼容性**

SQL标准中没有ALTER STATISTICS命令。

**另见**

CREATE STATISTICS, DROP STATISTICS

### 2.31. ALTER SUBSCRIPTION

ALTER SUBSCRIPTION — 修改订阅的定义

**大纲**

ALTER SUBSCRIPTION name CONNECTION ‘conninfo’

ALTER SUBSCRIPTION name SET PUBLICATION publication\_name \[, …\] \[ WITH

( set\_publication\_option \[= value\] \[, … \] ) \]

ALTER SUBSCRIPTION name REFRESH PUBLICATION \[ WITH ( refresh\_option \[= value\]

\[, … \] ) \]

ALTER SUBSCRIPTION name ENABLE

ALTER SUBSCRIPTION name DISABLE

ALTER SUBSCRIPTION name SET ( subscription\_parameter \[= value\] \[, … \] )

ALTER SUBSCRIPTION name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER SUBSCRIPTION name RENAME TO new\_name

**描述**

ALTER SUBSCRIPTION可以修改大部分可以在CREATE SUBSCRIPTION中指定的订阅属性。

要使用ALTER SUBSCRIPTION，你必须拥有该订阅。要改变所有者，你也必须是新所有者的直接或间接成员。新所有者必须是超级用户。（目前，所有的订阅所有者必须是超级用户，所以所有者的检查将在实践中被绕过，但这可能在未来发生变化。）

**参数**

name

要修改属性的订阅的名称。

CONNECTION ‘conninfo’

该子句修改最初由CREATE SUBSCRIPTION设置的连接属性。

SET PUBLICATION publication\_name

更改订阅发布的列表。参阅 CREATE SUBSCRIPTION 获取更多信息。默认情况下，此命令也将像REFRESH PUBLICATION一样工作。

set\_publication\_option指定了这个操作的附加选项。支持的选项是：

*refresh (boolean)*

如果为false，则该命令将不会尝试刷新表信息。然后应单独执行REFRESH PUBLICATION。默认值是true。

此外，可以指定REFRESH PUBLICATION下描述的刷新选项。

REFRESH PUBLICATION

从发布者获取缺少的表信息。这将开始复制自上次调用REFRESH PUBLICATION 或从CREATE SUBSCRIPTION以来添加到订阅发布中的表。

refresh\_option指定了刷新操作的附加选项。支持的选项有：

*copy\_data (boolean)*

指定在复制启动后是否应复制正在订阅的发布中的现有数据。 默认值是true。（以前订阅的表不会被复制。）

ENABLE

启用先前禁用的订阅，在事务结束时启动逻辑复制工作。

DISABLE

禁用正在运行的订阅，在事务结束时停止逻辑复制工作。

SET ( subscription\_parameter \[= value\] \[, … \] )

该子句修改原先由CREATE SUBSCRIPTION设置的参数。允许的选项是slot\_name和synchronous\_commit。

new\_owner

订阅的新所有者的用户名。

new\_name

订阅的新名称。

**示例**

将订阅的发布更改为insert\_only：

ALTER SUBSCRIPTION mysub SET PUBLICATION insert\_only;

禁用（停止）订阅：

ALTER SUBSCRIPTION mysub DISABLE;

**兼容性**

ALTER SUBSCRIPTION是瀚高数据库的一个扩展。

**另见**

CREATE SUBSCRIPTION, DROP SUBSCRIPTION, CREATE PUBLICATION, ALTER PUBLICATION

### 2.32. ALTER SYSTEM

ALTER SYSTEM — 更改一个服务器配置参数

**大纲**

ALTER SYSTEM SET configuration\_parameter { TO | = } { value | ‘value’ |

DEFAULT }

ALTER SYSTEM RESET configuration\_parameter

ALTER SYSTEM RESET ALL

**描述**

ALTER SYSTEM被用来在整个数据库集簇范围内更改服务器配置参数。它比传统的手动编辑postgresql.conf文件的方法更方便。ALTER SYSTEM会把给出的参数设置写入到postgreql.auto.conf文件中，该文件会随着 postgresql.conf一起被读入。把一个参数设置为DEFAULT或者使用RESET变体可以把该配置项从postgresql.auto.conf文件中移除。

使用RESET ALL可以移除所有这类配置项。

用ALTER SYSTEM设置的值将在下一次重载服务器配置后生效，那些只能在服务器启动时更改的参数则会在下一次服务器重启后生效。重载服务器配置可以通过以下做法实现：调用SQL函数pg\_reload\_conf()， 运行pg\_ctl reload或者向主服务器进程发送一个SIGHUP信号。

只有超级用户能够使用ALTER SYSTEM。还有，由于这个命令直接作用于文件系统并且不能被回滚，不允许在一个事务块或者函数中使用它。

**参数**

configuration\_parameter

一个可设置配置参数的名称。

value

该参数的新值。值可以被指定为字符串常量、标识符、数字或者以上这些构成的逗号分隔的列表，值的具体形式取决于特定的参数。写上DEFAULT可以用来把该参数及其值从postgresql.auto.conf中移除。

**注解**

不能用这个命令来设置data\_directory以及postgresql.conf中不被允许的参数（例如preset options）。

**示例**

设置wal\_level：

ALTER SYSTEM SET wal\_level = replica;

撤销以上的设置，恢复postgresql.conf中有效的设置：

ALTER SYSTEM RESET wal\_level;

**兼容性**

ALTER SYSTEM语句是一种瀚高数据库扩展。

**另见**

SET, SHOW

### 2.33. ALTER TABLE

ALTER TABLE — 更改一个表的定义

**大纲**

ALTER TABLE \[ IF EXISTS \] \[ ONLY \] name \[ \* \]

action \[, … \]

ALTER TABLE \[ IF EXISTS \] \[ ONLY \] name \[ \* \]

RENAME \[ COLUMN \] column\_name TO new\_column\_name

ALTER TABLE \[ IF EXISTS \] \[ ONLY \] name \[ \* \]

RENAME CONSTRAINT constraint\_name TO new\_constraint\_name

ALTER TABLE \[ IF EXISTS \] name

RENAME TO new\_name

ALTER TABLE \[ IF EXISTS \] name

SET SCHEMA new\_schema

ALTER TABLE ALL IN TABLESPACE name \[ OWNED BY role\_name \[, … \] \]

SET TABLESPACE new\_tablespace \[ NOWAIT \]

ALTER TABLE \[ IF EXISTS \] name

ATTACH PARTITION partition\_name { FOR VALUES partition\_bound\_spec |

DEFAULT }

ALTER TABLE \[ IF EXISTS \] name

DETACH PARTITION partition\_name

其中action 是以下之一：

ADD \[ COLUMN \] \[ IF NOT EXISTS \] column\_name data\_type \[ COLLATE collation \]

\[ column\_constraint \[ … \] \]

DROP \[ COLUMN \] \[ IF EXISTS \] column\_name \[ RESTRICT | CASCADE \]

ALTER \[ COLUMN \] column\_name \[ SET DATA \] TYPE data\_type \[ COLLATE collation

\] \[ USING expression \]

ALTER \[ COLUMN \] column\_name SET DEFAULT expression

ALTER \[ COLUMN \] column\_name DROP DEFAULT

ALTER \[ COLUMN \] column\_name { SET | DROP } NOT NULL

ALTER \[ COLUMN \] column\_name ADD GENERATED { ALWAYS | BY DEFAULT } AS

IDENTITY \[ ( sequence\_options ) \]

ALTER \[ COLUMN \] column\_name { SET GENERATED { ALWAYS | BY DEFAULT } |

SET sequence\_option | RESTART \[ \[ WITH \] restart \] } \[…\]

ALTER \[ COLUMN \] column\_name DROP IDENTITY \[ IF EXISTS \]

ALTER \[ COLUMN \] column\_name SET STATISTICS integer

ALTER \[ COLUMN \] column\_name SET ( attribute\_option = value \[, … \] )

ALTER \[ COLUMN \] column\_name RESET ( attribute\_option \[, … \] )

ALTER \[ COLUMN \] column\_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED |

MAIN }

ADD table\_constraint \[ NOT VALID \]

ADD table\_constraint\_using\_index

ALTER CONSTRAINT constraint\_name \[ DEFERRABLE | NOT DEFERRABLE \] \[ INITIALLY

DEFERRED | INITIALLY IMMEDIATE \]

VALIDATE CONSTRAINT constraint\_name

DROP CONSTRAINT \[ IF EXISTS \] constraint\_name \[ RESTRICT | CASCADE \]

DISABLE TRIGGER \[ trigger\_name | ALL | USER \]

ENABLE TRIGGER \[ trigger\_name | ALL | USER \]

ENABLE REPLICA TRIGGER trigger\_name

ENABLE ALWAYS TRIGGER trigger\_name

DISABLE RULE rewrite\_rule\_name

ENABLE RULE rewrite\_rule\_name

ENABLE REPLICA RULE rewrite\_rule\_name

ENABLE ALWAYS RULE rewrite\_rule\_name

DISABLE ROW LEVEL SECURITY

ENABLE ROW LEVEL SECURITY

FORCE ROW LEVEL SECURITY

NO FORCE ROW LEVEL SECURITY

CLUSTER ON index\_name

SET WITHOUT CLUSTER

SET WITHOUT OIDS

SET TABLESPACE new\_tablespace

SET { LOGGED | UNLOGGED }

SET ( storage\_parameter = value \[, … \] )

RESET ( storage\_parameter \[, … \] )

INHERIT parent\_table

NO INHERIT parent\_table

OF type\_name

NOT OF

OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

REPLICA IDENTITY { DEFAULT | USING INDEX index\_name | FULL | NOTHING }

and partition\_bound\_spec is:

IN ( partition\_bound\_expr \[, …\] ) |

FROM ( { partition\_bound\_expr | MINVALUE | MAXVALUE } \[, …\] )

TO ( { partition\_bound\_expr | MINVALUE | MAXVALUE } \[, …\] ) |

WITH ( MODULUS numeric\_literal, REMAINDER numeric\_literal )

and column\_constraint is:

\[ CONSTRAINT constraint\_name \]

{ NOT NULL |

NULL |

CHECK ( expression ) \[ NO INHERIT \] |

DEFAULT default\_expr |

GENERATED ALWAYS AS ( generation\_expr ) STORED |

GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY \[ ( sequence\_options ) \] |

UNIQUE index\_parameters |

PRIMARY KEY index\_parameters |

REFERENCES reftable \[ ( refcolumn ) \] \[ MATCH FULL | MATCH PARTIAL | MATCH

SIMPLE \]

\[ ON DELETE referential\_action \] \[ ON UPDATE referential\_action \] }

\[ DEFERRABLE | NOT DEFERRABLE \] \[ INITIALLY DEFERRED | INITIALLY IMMEDIATE \]而table\_constraint是：

\[ CONSTRAINT constraint\_name \]

{ CHECK ( expression ) \[ NO INHERIT \] |

UNIQUE ( column\_name \[, … \] ) index\_parameters |

PRIMARY KEY ( column\_name \[, … \] ) index\_parameters |

EXCLUDE \[ USING index\_method \] ( exclude\_element WITH operator

\[, … \] ) index\_parameters \[ WHERE ( predicate ) \] |

FOREIGN KEY ( column\_name \[, … \] ) REFERENCES reftable \[ ( refcolumn

\[, … \] ) \]

\[ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE \] \[ ON DELETE action \] \[ ON

UPDATE action \] }

\[ DEFERRABLE | NOT DEFERRABLE \] \[ INITIALLY DEFERRED | INITIALLY IMMEDIATE \]

并且 table\_constraint\_using\_index 是：

\[ CONSTRAINT constraint\_name \]

{ UNIQUE | PRIMARY KEY } USING INDEX index\_name

\[ DEFERRABLE | NOT DEFERRABLE \] \[ INITIALLY DEFERRED | INITIALLY IMMEDIATE \]

UNIQUE、PRIMARY KEY以及EXCLUDE约束中的index\_parameters是：

\[ INCLUDE ( column\_name \[, … \] ) \]

\[ WITH ( storage\_parameter \[= value\] \[, … \] ) \]

\[ USING INDEX TABLESPACE tablespace\_name \]

exclude\_element in an EXCLUDE constraint is:

{ column\_name | ( expression ) } \[ opclass \] \[ ASC | DESC \] \[ NULLS { FIRST |

LAST } \]

**描述**

ALTER TABLE更改一个现有表的定义。下文描述了 几种形式。注意每一种形式所要求的锁级别可能不同。如果没有明确说明，将会 持有一个ACCESS EXCLUSIVE所。当列出多个子命令时，所持有的锁将是子命令所要求的最严格的那一个。

ADD COLUMN \[ IF NOT EXISTS \]

这种形式向该表增加一个新列，使用与 CREATE TABLE相同的语法。如果指定了 IF NOT EXISTS并且使用这个名字的列已经存在，则 不会抛出错误。

DROP COLUMN \[ IF EXISTS \]

这种形式从表删除一列。涉及到该列的索引和表约束也将会被自动 删除。如果该列的移除会导致引用它的多元统计信息仅包含单一列的数据，则该多元统计信息也将被移除。

如果在该表之外有任何东西（例如外键引用或者视图）依赖 于该列，你将需要用到CASCADE。如果指定了 IF EXISTS但该列不存在，则不会抛出错误。 这种情况中会发出一个提示。

SET DATA TYPE

这种形式更改表中一列的类型。涉及到该列的索引和简单表约束将通过重新解析最初提供的表达式被自动转换为使用新的列类型。可选的COLLATE子句为新列指定一种排序规则，如果被省略，排序规则会是新列类型的默认排序规则。可选的USING子句指定如何从旧的列值计算新列值，如果被省略，默认的转换和从旧类型到新类型的赋值造型一样。如果没有从旧类型到新类型的隐式或者赋值造型，则必须提供一个USING子句。

SET/DROP DEFAULT

这些形式为一列设置或者移除默认值。默认值只在后续的INSERT或UPDATE命令中生效，它们不会导致已经在表中的行改变。

SET/DROP NOT NULL

这些形式更改一列是否被标记为允许空值或者拒绝空值。

SET NOT NULL 只能应用于列，前提是表中没有任何记录包含该列的NULL值。通常，这一点在ALTER TABLE全表扫描时来检查；但是，如果找到有效的CHECK约束证明不存在NULL，则跳过表扫描。

如果这个表是一个分区，对于在父表中被标记为NOT NULL的列，不能在其上执行DROP NOT NULL。要从所有的分区中删除NOT NULL约束，可以在父表上执行DROP NOT NULL。即使在父表上没有NOT NULL约束，这样的约束还是能被增加到分区上。也就是说，即便父表允许空值，子表也可以不允许空值，但反过来不行。

ADD GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY

SET GENERATED { ALWAYS | BY DEFAULT }

DROP IDENTITY \[ IF EXISTS \]

这些形式更改一列是否是一个标识列，或者是更改一个已有的标识列的产生属性。

如果DROP IDENTITY IF EXISTS被指定并且该列不是一个标识列，则不会有错误被抛出。在这种情况下会发出一个提示。

SET sequence\_option

RESTART

这些形式修改位于一个现有标识列之下的序列。sequence\_option是一个ALTER SEQUENCE所支持的选项，例如INCREMENT BY。

SET STATISTICS

这种形式为后续的ANALYZE操作设置针对每列的统计收集目标。目标可以被设置在范围0到10000之间，还可以把它设置为-1来恢复到使用系统默认的统计目标（default\_statistics\_target）。

SET STATISTICS要求一个SHARE UPDATE EXCLUSIVE锁。

SET ( attribute\_option = value \[, … \] )

RESET ( attribute\_option \[, … \] )

这种形式设置或者重置每个属性的选项。当前，已定义的针对每个属性的选项只有n\_distinct和n\_distinct\_inherited，它们会覆盖后续ANALYZE操作所得到的可区分值数量估计。n\_distinct影响该表本身的统计信息，而n\_distinct\_inherited影响为该表外加其继承子表收集的统计信息。当被设置为一个正值时，ANALYZE将假定该列刚好包含指定数量的可区分非空值。当被设置为一个负值（必须大于等于-1）时，ANALYZE将假定可区分非空值的数量与表的尺寸成线性比例，确切的计数由估计的表尺寸乘以给定数字的绝对值计算得到。例如，值-1表示该列中所有的值都是可区分的，而值-0.5则表示每一个值平均出现两次。当表的尺寸随时间变化时，这会有所帮助，因为这种计算只有在查询规划时才会被执行。指定值为0将回到正常的估计可区分值数量的做法。

更改针对每个属性的选项要求一个SHARE UPDATE EXCLUSIVE锁。

SET STORAGE

这种形式为一列设置存储模式。这会控制这列是会被保持在线内还是放在一个二级TOAST表中，以及数据是否应被压缩。对于integer之类的定长、线内、未压缩值必须使用PLAIN。MAIN用于线内、可压缩的数据。EXTERNAL用于外部的、未压缩数据。而EXTENDED用于外部的、压缩数据。对于大部分支持非-PLAIN存储的数据类型，EXTENDED是默认值。使用EXTERNAL将会让很大的text和bytea之上的子串操作运行得更快，但是代价是存储空间会增加。注意SET STORAGE本身并不改变表中的任何东西，它只是设置在未来的表更新时要追求的策略。

ADD table\_constraint \[ NOT VALID \]

这种形式使用和CREATE TABLE相同的语法外加NOT VALID选项为一个表增加一个新的约束，该选项当前只被允许用于外键和CHECK约束。

通常，此窗体将导致对表进行扫描，以验证表中的所有现有行是否满足新约束。但是如果使用了NOT VALID选项，则跳过此可能很漫长的扫描。该约束仍将被强制到后续的插入和删除上（也就是说，在外键的情况下如果在被引用表中没有一个匹配的行，操作会失败；或者如果新行不匹配指定的检查条件，操作也会失败）。但是数据库不会假定约束对该表中的所有行都成立，直到通过使用VALIDATE CONSTRAINT选项对它进行验证。参见下述内容以了解关于使用NOT VALID选项的更多信息。

除了接收约束的表上的锁外，外键约束的增加要求在被引用表上的一个SHARE ROW EXCLUSIVE锁。

当唯一或者主键约束被添加到分区表时，会有额外的限制，请参考CREATE TABLE。 此外，当前分区表上的外键约束不能被声明为NOT VALID。

ADD table\_constraint\_using\_index

这种形式基于一个已有的唯一索引为一个表增加新的PRIMARY KEY或UNIQUE约束。该索引中的所有列将被包括在约束中。

该索引不能有表达式列或者是一个部分索引。还有，它必须是一个带有默认排序顺序的B-树索引。这些限制确保该索引等效于使用常规ADD PRIMARY KEY或者ADD UNIQUE命令时创建的索引。

如果PRIMARY KEY被指定，并且该索引的列没有被标记NOT NULL，那么这个命令将尝试对每一个这样的列做ALTER COLUMN SET NOT NULL。这需要一次全表扫描来验证这些列不包含空值。在所有其他情况中，这都是一种很快的操作。

如果提供了一个约束名，那么该索引将被重命名以匹配该约束名。否则该约束将被命名成索引的名称。

这个命令被执行后，该索引被增加的约束“拥有”，这和用常规ADD PRIMARY KEY或ADD UNIQUE命令创建的索引一样。特别地，删掉该约束将会导致该索引也消失。

当前在分区表上不支持这种形式。

| **注意：** |
| --- |
| 如果需要增加一个新的约束但是不希望长时间阻塞表更新，那么使用现有索引增加约束会有所帮助。要这样做，用CREATE INDEX CONCURRENTLY创建该索引，并且接着使用这种语法把它安装为一个正式的约束。例子见下文。 |

ALTER CONSTRAINT

这种形式修改之前创建的一个约束的属性。当前只能修改外键约束。

VALIDATE CONSTRAINT

这种形式验证之前创建为NOT VALID的外键或检查约束，它会扫描表来确保对于该约束没有行不满足约束。如果约束已经被标记为合法，则什么也不会发生。(参见下述内容以了解此命令用途的说明。)

DROP CONSTRAINT \[ IF EXISTS \]

这种形式在一个表上删除指定的约束，还有位于该约束之下的任何索引。如果IF EXISTS被指定并且该约束不存在，不会抛出错误。在这种情况下会发出一个提示。

DISABLE/ENABLE \[ REPLICA | ALWAYS \] TRIGGER

这些形式配置属于该表的触发器的触发设置。系统仍然知道被禁用触发器的存在，但是即使它的触发事件发生也不会执行它。对于一个延迟触发器，会在事件发生时而不是触发器函数真正被执行时检查其启用状态。可以禁用或者启用用名称指定的单个触发器、表上的所有触发器、用户拥有的触发器（这个选项会排除内部生成的约束触发器，例如用来实现外键约束或可延迟唯一和排除约束）。禁用或者启用内部生成的约束触发器要求超级用户特权，这样做要小心因为如果这类触发器不被执行，约束的完整性当然无法保证。

触发器引发机制也受到配置变量session\_replication\_role的影响。当复制角色是“origin”（默认）或者“local”时，被简单启用的触发器将被触发。被配置为ENABLE REPLICA的触发器只有在会话处于“replica”模式时才将被触发。被配置为ENABLE ALWAYS的触发器的触发不会考虑当前复制角色。

这种机制的效果就是，在默认配置中，触发器不会在复制体上引发。这种效果很有用，因为如果一个触发器在源头上被用来在表之间传播数据，那么复制系统也将复制被传播的数据，并且触发器不应该在复制体上引发第二次，因为那会导致重复。不过，如果一个触发器被用于另一种目的（例如创建外部告警），那么将它设置为ENABLE ALWAYS可能更加合适，这样它在复制体上也会被引发。

这个命令要求一个SHARE ROW EXCLUSIVE锁。

DISABLE/ENABLE \[ REPLICA | ALWAYS \] RULE

这些形式配置属于表的重写规则的触发设置。系统仍然知道一个被禁用规则的存在，但在查询重写时不会应用它。其语义与禁用的/启用的触发器的一样。对于ONSELECT规则会忽略这个配置，即使当前会话处于一种非默认的复制角色，这类规则总是会被应用以保持视图工作正常。

规则引发机制也受到配置变量session\_replication\_role的影响，这和上述的触发器类似。

DISABLE/ENABLE ROW LEVEL SECURITY

这些形式控制属于该表的行安全性策略的应用。如果被启用并且该表上不存在策略，则将应用一个默认否定的策略。注意即使行级安全性被禁用，在表上还是可以存在策略。在这种情况下，这些策略将不会被应用并且会被忽略。另见 CREATE POLICY 。

NO FORCE/FORCE ROW LEVEL SECURITY

这些形式控制当用户是表拥有者时表上的行安全性策略的应用。如果被启用，当用户是表拥有者时，行级安全性策略将被应用。如果被禁用（默认），则当用户是表拥有者时，行级安全性将不会被应用。另见 CREATE POLICY 。

CLUSTER ON

这种形式为未来的CLUSTER操作选择默认的索引。 它不会真正地对表进行聚簇。

改变聚簇选项要求一个SHARE UPDATE EXCLUSIVE锁。

SET WITHOUT CLUSTER

这种形式从表中移除最近使用的 CLUSTER索引说明。这会影响未来的不指定索引 的聚簇操作。

改变聚簇选项要求一个SHARE UPDATE EXCLUSIVE锁。

SET WITHOUT OIDS

向后兼容的语法，用于删除oid系统列。由于oid系统列无法再添加，所以不会有实际效果。

SET TABLESPACE

这种形式把该表的表空间更改为指定的表空间并且把该表相关联的数据文件移动到新的表空间中。表上的索引（如果有）不会被移动，但是它们可以用额外的SET TABLESPACE命令单独移动。当应用于分区表时，不会移动，但之后用CREATE TABLE PARTITION OF创建的任何分区将使用该表空间，除非TABLESPACE子句用于重写它。

当前数据库在一个表空间中的所有表可以用ALL IN TABLESPACE形式移动，这将会首先锁住所有将被移动的表然后逐个移动。这种形式也支持OWNED BY，它将只移动指定角色所拥有的表。如果指定了NOWAIT选项，则命令将在无法立刻获得所有所需要的锁时失败。注意这个命令不移动系统目录；如果想要移动系统目录，应该用ALTER DATABASE或者显式的ALTER TABLE调用。对于这种形式来说，information\_schema关系不被认为是系统目录的一部分，因此它们将会被移动。另见 CREATE TABLESPACE 。

SET { LOGGED | UNLOGGED }

这种形式将表从UNLOGGED变为LOGGED或者从LOGGED更改为UNLOGGED。该参数不能应用于临时表。

SET ( storage\_parameter = value \[, … \] )

这种形式为该表更改一个或者更多存储参数。注意这个命令将不会立刻修改表内容，这取决于重写表以得到想要的结果可能需要的参数。可以用VACUUM FULL、CLUSTER或者ALTER TABLE的一种形式来强制一次表重写。对于规划器相关的参数，更改将从该表下一次被锁定开始生效，因此当前执行的查询不会受到影响。

对fillfactor、toast以及autovacuum存储参数，将会拿取SHARE UPDATE EXCLUSIVE锁，就像计划器参数parallel\_workers。

RESET ( storage\_parameter \[, … \] )

这种形式把一个或者更多存储参数重置到它们的默认值。和 SET一样，可能需要一次表重写来更新整个表。

INHERIT parent\_table

这种形式把目标表增加为指定父表的一个新子表。随后，针对父表的查询将包括目标表中的记录。要被增加为一个子表，目标表必须已经包含和父表完全相同的列（也可以有额外的列）。这些列必须具有匹配的数据类型，并且如果它们在父表中具有NOT NULL约束，它们在子表中也必须有NOT NULL约束。

也必须把子表约束与所有父表的CHECK约束进行匹配，不过父表中那些被标记为非可继承（也就是用ALTER TABLE … ADD CONSTRAINT … NO INHERIT 创建的）除外，它们会被忽略。所有匹配得上的子表约束不能被标记为不可继承。当前，UNIQUE、PRIMARY KEY 以及FOREIGN KEY约束没有被考虑，但是这种情况可能会在未来发生变化。

NO INHERIT parent\_table

这种形式把目标表从指定父表的子表列表中移除。针对父表的查询将不再包括来自目标表的记录。

OF type\_name

这种形式把该表链接到一种组合类型，就好像CREATE TABLE OF所做的那样。该表的列名和类型列表必须精确地匹配该组合类型。该表必须不从任何其他表继承。这些限制确保CREATE TABLE OF能允许一个等价的表定义。

NOT OF

这种形式解除一个有类型的表和其类型之间的关联。

OWNER TO

这种形式把表、序列、视图、物化视图或外部表的拥有者改为指定用户。

REPLICA IDENTITY

这种形式更改被写入到预写式日志来标识被更新或删除行的信息。除非使用逻辑复制，这个选项将不会产生效果。DEFAULT（非系统表的默认值）记录主键列（如果有）的旧值。USING INDEX记录被所提到的索引所覆盖的列的旧值，该索引必须是唯一索引、不是部分索引、不是可延迟索引并且只包括被标记成NOT NULL的列。FULL记录行中所有列的旧值。NOTHING不记录有关旧行的任何信息（这是系统表的默认值）。在所有情况下，除非至少有一个要被记录的列在新旧行版本之间发生变化，将不记录旧值。

RENAME

RENAME形式更改一个表（或者一个索引、序列、视图、物化视图或者外部表）的名称、表中一个列的名称或者表的一个约束的名称。在重命名一个具有底层索引的约束时，该索引也会被重命名。它对已存储的数据没有影响。

SET SCHEMA

这种形式把该表移动到另一个模式中。相关的该表列拥有的索引、约束和序列也会被移动。

ATTACH PARTITION partition\_name { FOR VALUES partition\_bound\_spec | DEFAULT }

这种形式把一个已有表（自身也可能被分区）作为一个分区挂接到目标表。该表可以为特定的值使用FOR VALUES挂接为分区，或者用DEFAULT挂接为一个默认分区。对于目标表中的每一个索引，在被挂接的表上都将创建一个响应的索引，如果已经存在等效的索引，该索引将被挂接到目标表的索引，就像执行了ALTER INDEX ATTACH PARTITION一样。请注意，如果现有表是外表，如果目标表上有UNIQUE索引，则当前不允许将表作为目标表的分区附加。(参见 CREATE FOREIGN TABLE.)

一个使用FOR VALUES的分区使用与CREATE TABLE中partition\_bound\_spec相同的语法。分区边界说明必须对应于目标表的分区策略以及分区键。要被挂接的表必须具有和目标表完全相同的所有列，并且不能有多出来的列，而且列的类型也必须匹配。此外，它必须有目标表上所有的NOT NULL以及CHECK约束。当前不考虑FOREIGN KEY约束。来自于父表的UNIQUE和PRIMARY KEY约束将被创建在分区上（如果它们还不存在）。如果被挂接的表上的任何CHECK约束被标记为NO INHERIT，则命令将失败，这类约束必须被重建且重建时不能有NO INHERIT子句。

如果新分区是一个常规表，会执行一次全表扫描来检查表中现有行没有违背分区约束。可以通过对表增加一个有效的CHECK约束来避免这种扫描，该约束可以在运行这个命令之前仅允许满足所需分区约束的行。CHECK约束可以解决让表无需被扫描就能验证分区约束。但是，如果任一分区键是一个表达式并且该分区不接受NULL值，这种方式就无效了。如果挂接一个不接受NULL值的列表分区，还应该为分区键列增加NOT NULL约束，除非它是一个表达式。

如果新分区是一个外部表，则不需要验证该外部表中的所有行遵守分区约束（有关外部表上的约束请参考 CREATE FOREIGN TABLE 中的讨论）。

当一个表有默认分区时，定义新分区会更改默认分区的分区约束。默认分区不能包含任何需要被移动到新分区中的行，并且将被扫描以验证不存在那样的行。如果一个合适的CHECK约束存在，这种扫描（和新分区的扫描一样）可以被避免。还是和新分区的扫描一样，当默认分区是外部表时这种扫描总是会被跳过。

在父表上附加一个分区获得一个SHARE UPDATE EXCLUSIVE锁，除了要附加的表和默认分区上的ACCESS EXCLUSIVE 锁（如果有）。

DETACH PARTITION partition\_name

这种形式会分离目标表的指定分区。被分离的分区继续作为独立的表存在，但是与它之前挂接的表不再有任何联系。任何被挂接到目标表索引的索引也会被分离。

除了RENAME、SET SCHEMA、ATTACH PARTITION和DETACH PARTITION之外，所有形式的ALTER TABLE都作用在单个表上，前面这些形式可以被组合成一个多修改的列表被一起应用。例如，可以在一个命令中增加多个列并且/或者修改多个列的类型。对于大型表来说这会特别有用，因为只需要对表做一趟操作。

要使用ALTER TABLE，你必须拥有该表。要更改一个表的模式或者表空间，你还必须拥有新模式或表空间上的CREATE特权。要把一个表作为一个父表的新子表加入，你必须也拥有该父表。此外，要把一个表挂接为另一个表的新分区，你必须拥有被挂接的表。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该表的模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建表做不到的事情。不过，一个超级用户怎么都能更改任何表的所有权。）。要增加一个列、修改一列的类型或者使用OF子句，你还必须具有该数据类型上的USAGE特权。

**参数**

IF EXISTS

如果表不存在则不要抛出一个错误。这种情况下会发出一个提示。

name

要修改的一个现有表的名称（可以是模式限定的）。如果在表名前指定了ONLY，则只会修改该表。如果没有指定ONLY，该表及其所有后代表（如果有）都会被修改。可选地，在表名后面可以指定\*用来显式地指示包括后代表。

column\_name

一个新列或者现有列的名称。

new\_column\_name

一个现有列的新名称。

new\_name

该表的新名称。

data\_type

一个新列的数据类型或者一个现有列的新数据类型。

table\_constraint

该表的新的表约束。

constraint\_name

一个新约束或者现有约束的名称。

CASCADE

自动删除依赖于被删除列或约束的对象（例如引用该列的视图），并且接着删除依赖于那些对象的所有对象。

RESTRICT

如果有任何依赖对象时拒绝删除列或者约束。这是默认行为。

trigger\_name

一个要禁用或启用的触发器的名称。

ALL

禁用或者启用属于该表的所有触发器（如果有任何触发器是内部产生的约束触发器则需要超级用户特权，例如那些被用来实现外键约束或者可延迟一致性和排他约束的触发器）。

USER

禁用或者启用属于该表的所有触发器，内部产生的约束触发器（例如那些被用来实现外键约束或者可延迟一致性和排他约束的触发器）除外。

index\_name

一个现有索引的名称。

storage\_parameter

一个表存储参数的名称。

value

一个表存储参数的新值。根据该参数，该值可能是一个数字或者一个词。

parent\_table

要与这个表关联或者解除关联的父表。

new\_owner

该表的新拥有者的用户名。

new\_tablespace

要把该表移入其中的表空间的名称。

new\_schema

要把该表移入其中的模式的名称。

partition\_name

要被作为新分区附着到这个表或者从这个表上分离的表的名称。

partition\_bound\_spec

新分区的分区边界说明。更多细节请参考CREATE TABLE中相同的语法。

**注解**

关键词COLUMN是噪声，可以被省略。

在使用ADD COLUMN增加一列并且指定了一个非易失性DEFAULT时，默认值会在该语句执行时计算并且结果会被保存在表的元数据中。这个值将被用于所有现有行的该列。如果没有指定DEFAULT，则使用NULL。在两种情况下都不需要重写表。

增加一个带有非易失性DEFAULT子句的列或者更改一个现有列的类型将要求重写整个表及其索引。在更改一个现有列的类型时有一种例外：如果USING子句不更改列的内容并且旧类型在二进制上与新类型可强制转换或者是新类型上的一个未约束域，则不需要重写表。但是受影响列上的任何索引仍必须被重建。对于一个大型表，表和/或索引重建可能会消耗相当多的时间，并且会临时要求差不多两倍的磁盘空间。

增加一个CHECK或者NOT NULL约束要求扫描表以验证现有行符合该约束，但是不要求一次表重写。

类似地，在挂接一个新分区时，它需要被扫描以验证现有行满足该分区约束。

提供在一个ALTER TABLE中指定多个更改的选项的主要原因就是多次表扫描或者重写可以因此被整合成一次。

扫描大型表以验证新的外键或检查约束可能需要很长时间，并且对表的其他更新将锁定，直到ALTER TABLE ADD CONSTRAINT命令被提交。 NOT VALID约束选项的主要目的是减少对并发更新添加约束的影响。使用 NOT VALID，ADD CONSTRAINT命令不扫描表，可以立即提交。在之后，VALIDATE CONSTRAINT命令会被发出以验证现有行是否满足约束。验证步骤不需要锁定并发更新，因为它知道其他事务将强制执行它们插入或更新的行的约束;只有预先存在的行需要检查。因此，验证在被更改的表上仅获得一个SHARE UPDATE EXCLUSIVE锁。（如果约束是外键，则ROW SHARE锁也需要约束的表引用。）除了改进并发性外，在已知该表包含预先存在的违规行为的情况下使用NOT VALID 和VALIDATE CONSTRAINT也能有作用。一旦约束就位，就不能再插入新的违规数据，并且现有问题可以在空闲时纠正，直到VALIDATE CONSTRAINT最终完成。

DROP COLUMN形式不会在物理上移除列，而只是简单地让它对SQL操作不可见。后续该表中的插入和更新操作将为该列存储一个空值。因此，删除一个列很快，但是它不会立刻减少表所占的磁盘空间，因为被删除列所占用的空间还没有被回收。随着现有列被更新，空间将被逐渐回收。

要强制立即回收被已删除列占据的空间，你可以执行一种能导致全表重写的ALTER TABLE形式。这种形式会导致重新构造每一个把被删除列替换为空值的行。

ALTER TABLE的重写形式对于MVCC是不安全的。在一次表重写之后，如果并发事务使用的是一个在重写发生前取得的快照，该表将对这些并发事务呈现出空表的形态。

SET DATA TYPE的USING选项能实际指定涉及该列旧值的任何表达式。也就是说，它可以不但可以引用要被转换的列，还可以引用其他列。这允许使用SET DATA TYPE语法完成十分普遍的转换。由于这种灵活性，USING表达式不适合于列的默认值（如果有），结果可能不是一个默认值所需的常量表达式。这意味着在没有从旧类型到新类型的隐式或者赋值造型时，即便提供了一个USING子句，SET DATA TYPE还是可能无法转换默认值。在这种情况下，用DROP DEFAULT删除该默认值，执行ALTER TYPE并且接着使用SET DEFAULT增加一个合适的新默认值。类似的考虑也适用于涉及该列的索引和约束。

如果一个表有任何后代表，在不对后代表做相同操作的情况下，不允许在父表中增加列、重命名列或者更改列的类型。这确保了后代总是具有和父表匹配的列。类似地，如果不对所有后代上的CHECK约束进行重命名，就不能在父表中重命名该CHECK约束，这样CHECK约束也能在父表及其后代之间保持匹配（不过，这个限制不适用于基于索引的约束）。此外，因为从父表中选择也会从其后代中选择，父表上的约束不能被标记为有效，除非它在那些后代上也被标记为有效。在所有这些情况下，ALTER TABLE ONLY都将被拒绝。

只有当一个后代表的列不是从任何其他父表继承而来并且没有该列的独立定义时，一次递归的DROP COLUMN操作才会移除该列。一次非递归的DROP COLUMN（即 ALTER TABLE ONLY … DROP COLUMN）不会移除任何后代列，而是会把它们标记成独立定义的列。对于一个分区表，一个非递归的DROP COLUMN命令将会失败，因为一个表的所有分区都必须有和分区根节点相同的列。

标识列的动作（ADD GENERATED、SET等、DROP IDENTITY）以及动作TRIGGER、CLUSTER、OWNER和TABLESPACE不会递归到后代表上，也就是说它们执行时总是好像指定了ONLY一样。增加约束的动作仅对没有标记为NO INHERIT的CHECK约束递归。

不允许更改一个系统目录表的任何部分。

**示例**

要向一个表增加一个类型为varchar的列：

ALTER TABLE distributors ADD COLUMN address varchar(30);

要从表中删除一列：

ALTER TABLE distributors DROP COLUMN address RESTRICT;

要在一个操作中更改两个现有列的类型：

ALTER TABLE distributors

ALTER COLUMN address TYPE varchar(80),

ALTER COLUMN name TYPE varchar(100);

通过一个USING子句更改一个包含 Unix 时间戳的整数列为 timestamp with time zone：

ALTER TABLE foo

ALTER COLUMN foo\_timestamp SET DATA TYPE timestamp with time zone

USING

timestamp with time zone ‘epoch’ + foo\_timestamp \* interval ‘1 second’;

同样的，当该列具有一个不能自动造型成新数据类型的默认值表达式时：

ALTER TABLE foo

ALTER COLUMN foo\_timestamp DROP DEFAULT,

ALTER COLUMN foo\_timestamp TYPE timestamp with time zone

USING

timestamp with time zone ‘epoch’ + foo\_timestamp \* interval ‘1 second’,

ALTER COLUMN foo\_timestamp SET DEFAULT now();

To rename an existing column:

ALTER TABLE distributors RENAME COLUMN address TO city;

重命名一个现有的表：

ALTER TABLE distributors RENAME TO suppliers;

重命名一个现有的约束：

ALTER TABLE distributors RENAME CONSTRAINT zipchk TO zip\_check;

为一列增加一个非空约束：

ALTER TABLE distributors ALTER COLUMN street SET NOT NULL;

从一列移除一个非空约束：

ALTER TABLE distributors ALTER COLUMN street DROP NOT NULL;

向一个表及其所有子表增加一个检查约束：

ALTER TABLE distributors ADD CONSTRAINT zipchk CHECK (char\_length(zipcode) = 5);

只向一个表增加一个检查约束（不为其子表增加）：

ALTER TABLE distributors ADD CONSTRAINT zipchk CHECK (char\_length(zipcode) = 5)

NO INHERIT;

（该检查约束也不会被未来的子表继承）。

从一个表及其子表移除一个检查约束：

ALTER TABLE distributors DROP CONSTRAINT zipchk;

只从一个表移除一个检查约束：

ALTER TABLE ONLY distributors DROP CONSTRAINT zipchk;

（该检查约束仍为子表保留在某个地方）。

为一个表增加一个外键约束：

ALTER TABLE distributors ADD CONSTRAINT distfk FOREIGN KEY (address) REFERENCES

addresses (address);

为一个表增加一个外键约束，并且尽量不要影响其他工作：

ALTER TABLE distributors ADD CONSTRAINT distfk FOREIGN KEY (address) REFERENCES

addresses (address) NOT VALID;

ALTER TABLE distributors VALIDATE CONSTRAINT distfk;

为一个表增加一个（多列）唯一约束：

ALTER TABLE distributors ADD CONSTRAINT dist\_id\_zipcode\_key UNIQUE (dist\_id,

zipcode);

为一个表增加一个自动命名的主键约束，注意一个表只能拥有一个主键：

ALTER TABLE distributors ADD PRIMARY KEY (dist\_id);

把一个表移动到一个不同的表空间：

ALTER TABLE distributors SET TABLESPACE fasttablespace;

把一个表移动到一个不同的模式：

ALTER TABLE myschema.distributors SET SCHEMA yourschema;

重建一个主键约束，并且在重建索引期间不阻塞更新：

CREATE UNIQUE INDEX CONCURRENTLY dist\_id\_temp\_idx ON distributors (dist\_id);

ALTER TABLE distributors DROP CONSTRAINT distributors\_pkey,

ADD CONSTRAINT distributors\_pkey PRIMARY KEY USING INDEX dist\_id\_temp\_idx;

要把一个分区挂接到一个范围分区表上：

ALTER TABLE measurement

ATTACH PARTITION measurement\_y2016m07 FOR VALUES FROM (‘2016-07-01’) TO

(‘2016-08-01’);

要把一个分区挂接到一个列表分区表上：

ALTER TABLE cities

ATTACH PARTITION cities\_ab FOR VALUES IN (‘a’, ‘b’);

要把一个分区挂接到一个哈希分区表上：

ALTER TABLE orders

ATTACH PARTITION orders\_p4 FOR VALUES WITH (MODULUS 4, REMAINDER 3);

要把一个默认分区挂接到一个分区表上：

ALTER TABLE cities

ATTACH PARTITION cities\_partdef DEFAULT;

从一个分区表分离一个分区：

ALTER TABLE measurement

DETACH PARTITION measurement\_y2015m12;

**兼容性**

形式ADD（没有USING INDEX）、 DROP \[COLUMN\]、DROP IDENTITY、RESTART、 SET DEFAULT、SET DATA TYPE（没有USING)、 SET GENERATED以及SET sequence\_option服从SQL标准。其他形式都是瀚高数据库对SQL标准的扩展。此外，在单个ALTER TABLE命令中指定多个操作的能力是一种扩展。

ALTER TABLE DROP COLUMN可以被用来删除一个表的唯一的列，从而留下一个零列的表。这是一种SQL的扩展，SQL中不允许零列的表。

**另见**

CREATE TABLE

### 2.34. ALTER TABLESPACE

ALTER TABLESPACE — 更改一个表空间的定义

**大纲**

ALTER TABLESPACE name RENAME TO new\_name

ALTER TABLESPACE name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER TABLESPACE name SET ( tablespace\_option = value \[, … \] )

ALTER TABLESPACE name RESET ( tablespace\_option \[, … \] )

**描述**

ALTER TABLESPACE可以被用于更改一个表空间的定义。

要更改一个表空间的定义，你必须拥有它。要修改拥有者，你还必须是新拥有角色的一个直接或间接成员（注意超级用户自动拥有这些特权）。

**参数**

name

一个现有表空间的名称。

new\_name

该表空间的新名称。新名称不能以pg\_开始，因为这类名称被保留用于系统表空间。

new\_owner

该表空间的新拥有者。

tablespace\_option

要设置或者重置的一个表空间参数。当前，唯一可用的参数是seq\_page\_cost、random\_page\_cost和effective\_io\_concurrency。为一个特定表空间设定这两个参数值将覆盖规划器对从该表空间中的表读取页面代价的估计值，这些估计值由具有相同名称配置参数建立（见seq\_page\_cost、random\_page\_cost、effective\_io\_concurrency）。如果一个表空间位于一个比其余I/O 子系统更快或者更慢的磁盘上时，这些参数就能派上用场。

**示例**

将表空间index\_space重命名为fast\_raid：

ALTER TABLESPACE index\_space RENAME TO fast\_raid;

更改表空间index\_space的拥有者：

ALTER TABLESPACE index\_space OWNER TO mary;

**兼容性**

在 SQL 标准中没有 ALTER TABLESPACE语句。

**另见**

CREATE TABLESPACE, DROP TABLESPACE

### 2.35. ALTER TEXT SEARCH CONFIGURATION

ALTER TEXT SEARCH CONFIGURATION — 更改一个文本搜索配置的定义

**大纲**

ALTER TEXT SEARCH CONFIGURATION name

ADD MAPPING FOR token\_type \[, … \] WITH dictionary\_name \[, … \]

ALTER TEXT SEARCH CONFIGURATION name

ALTER MAPPING FOR token\_type \[, … \] WITH dictionary\_name \[, … \]

ALTER TEXT SEARCH CONFIGURATION name

ALTER MAPPING REPLACE old\_dictionary WITH new\_dictionary

ALTER TEXT SEARCH CONFIGURATION name

ALTER MAPPING FOR token\_type \[, … \] REPLACE old\_dictionary

WITH new\_dictionary

ALTER TEXT SEARCH CONFIGURATION name

DROP MAPPING \[ IF EXISTS \] FOR token\_type \[, … \]

ALTER TEXT SEARCH CONFIGURATION name RENAME TO new\_name

ALTER TEXT SEARCH CONFIGURATION name OWNER TO { new\_owner | CURRENT\_USER |

SESSION\_USER }

ALTER TEXT SEARCH CONFIGURATION name SET SCHEMA new\_schema

**描述**

ALTER TEXT SEARCH CONFIGURATION更改一个文本搜索配置的定义。你可以修改其从记号类型到词典的映射或者更改该配置的名称或者拥有者。

要使用ALTER TEXT SEARCH CONFIGURATION，你必须是该配置的拥有者。

**参数**

name

一个现有文本搜索配置的名称（可以是模式限定的）。

token\_type

由该配置的解析器发出的记号类型的名称。

dictionary\_name

在其中查阅指定记号类型的文本搜索字典的名称。如果列出了多个字典，会按照指定的顺序查阅它们。

old\_dictionary

在映射中要替换的文本搜索字典的名称。

new\_dictionary

被用来替代old\_dictionary的文本搜索字典的名称。

new\_name

该文本搜索配置的新名称。

new\_owner

该文本搜索配置的新拥有者。

new\_schema

该文本搜索配置的新模式。

ADD MAPPING FOR形式会安装一些词典（用列表列出）用于在其中查阅指定的记号类型。

如果对任一记号类型已经有一个映射，则会发生错误。ALTER MAPPING FOR形式做同样的事情，但是首先会移除这些记号类型的任何现有映射。ALTER MAPPING REPLACE形式用new\_dictionary来替换任何位置上的old\_dictionary。当出现FOR时，只会为指定的记号类型做这样的事情。如果不出现FOR，则会为该配置中所有的映射都这样做。DROP MAPPING形式会移除指定记号类型的所有字典，导致该文本搜索配置忽略这些类型。除非出现IF EXISTS，在那些记号类型没有任何映射时会发生错误。

**示例**

下面的例子把my\_config中任何位置上的english字典替换为swedish字典。

ALTER TEXT SEARCH CONFIGURATION my\_config

ALTER MAPPING REPLACE english WITH swedish;

**兼容性**

在 SQL 标准中没有 ALTER TEXT SEARCH CONFIGURATION 语句。

**另见**

CREATE TEXT SEARCH CONFIGURATION, DROP TEXT SEARCH CONFIGURATION

### 2.36. ALTER TEXT SEARCH DICTIONARY

ALTER TEXT SEARCH DICTIONARY — 更改一个文本搜索字典的定义

**大纲**

ALTER TEXT SEARCH DICTIONARY name (

option \[ = value \] \[, … \]

)

ALTER TEXT SEARCH DICTIONARY name RENAME TO new\_name

ALTER TEXT SEARCH DICTIONARY name OWNER TO { new\_owner | CURRENT\_USER |

SESSION\_USER }

ALTER TEXT SEARCH DICTIONARY name SET SCHEMA new\_schema

**描述**

ALTER TEXT SEARCH DICTIONARY更改一个文本搜索字典的定义。你可以更改该字典的与模板相关的选项，或者更改该字典的名称或者拥有者。

要使用ALTER TEXT SEARCH DICTIONARY，你必须是超级用户。

**参数**

name

一个现有的文本搜索字典的名称（可以是模式限定的）。

option

要为这个字典设置的与模板相关的选项的名称。

value

用于一个模板相关选项的新值。如果等号和值被忽略，则会从该字典中移除该选项之前的设置而允许使用默认值。

new\_name

该文本搜索字典的新名称。

new\_owner

该文本搜索字典的新拥有者。

new\_schema

该文本搜索字典的新模式。

模板相关的选项可以以任何顺序出现。

**示例**

下面的命令更改一个基于Snowball的字典的停用词列表。其他参数保持不变。

ALTER TEXT SEARCH DICTIONARY my\_dict ( StopWords = newrussian );

下面的命令更改语言选项为dutch，并且完全移除停用词选项。

ALTER TEXT SEARCH DICTIONARY my\_dict ( language = dutch, StopWords );

下面的命令“更新”该字典的定义，但是实际没有做任何更改。

ALTER TEXT SEARCH DICTIONARY my\_dict ( dummy );

这种技巧在为该字典更改配置文件时有用：ALTER将强制现有的数据库会话重读配置文件，否则如果会话之前已经读取过就不会再次读取。

**兼容性**

在 SQL 标准中没有 ALTER TEXT SEARCH DICTIONARY语句。

**另见**

CREATE TEXT SEARCH DICTIONARY, DROP TEXT SEARCH DICTIONARY

### 2.37. ALTER TEXT SEARCH PARSER

ALTER TEXT SEARCH PARSER — 更改一个文本搜索解析器的定义

**大纲**

ALTER TEXT SEARCH PARSER name RENAME TO new\_name

ALTER TEXT SEARCH PARSER name SET SCHEMA new\_schema

**描述**

ALTER TEXT SEARCH PARSER更改一个文本搜索解析器的定义。当前，唯一支持的功能是更改该解析器的名称。

要使用ALTER TEXT SEARCH PARSER，你必须是超级用户。

**参数**

name

一个现有文本搜索解析器的名称（可以是模式限定的）。

new\_name

该文本搜索解析器的新名称。

new\_schema

该文本搜索解析器的新模式。

**兼容性**

在SQL标准中没有ALTER TEXT SEARCH PARSER语句。

**另见**

CREATE TEXT SEARCH PARSER, DROP TEXT SEARCH PARSER

### 2.38. ALTER TEXT SEARCH TEMPLATE

ALTER TEXT SEARCH TEMPLATE — 更改一个文本搜索模板的定义

**大纲**

ALTER TEXT SEARCH TEMPLATE name RENAME TO new\_name

ALTER TEXT SEARCH TEMPLATE name SET SCHEMA new\_schema

**描述**

ALTER TEXT SEARCH TEMPLATE更改一个文本搜索模板的定义。当前唯一支持的功能是更改该模板的名称。

要使用ALTER TEXT SEARCH TEMPLATE，你必须是超级用户。

**参数**

name

一个现有文本搜索模板的名称（可以是模式限定的）。

new\_name

该文本搜索模板的新名称。

new\_schema

该文本搜索模板的新模式。

**兼容性**

在 SQL 标准中没有 ALTER TEXT SEARCH TEMPLATE语句。

**另见**

CREATE TEXT SEARCH TEMPLATE, DROP TEXT SEARCH TEMPLATE

### 2.39. ALTER TRIGGER

ALTER TRIGGER — 更改一个触发器的定义

**大纲**

ALTER TRIGGER name ON table\_name RENAME TO new\_name

ALTER TRIGGER name ON table\_name DEPENDS ON EXTENSION extension\_name

**描述**

ALTER TRIGGER更改一个现有触发器的属性。RENAME子句更改给定触发器的名称而不更改其定义。DEPENDS ON EXTENSION子句把该触发器标记为依赖于一个扩展，这样如果扩展被删除，该触发器也会被自动删除。

要更改一个触发器的属性，你必须拥有该触发器所作用的表。

**参数**

name

要修改的一个现有触发器的名称。

table\_name

这个触发器所作用的表的名称。

new\_name

该触发器的新名称。

extension\_name

该触发器所依赖的扩展的名称。

**注解**

临时启用或者禁用一个触发器的功能由ALTER TABLE而不是 ALTER TRIGGER提供，因为ALTER TRIGGER无法表示一次性启用或者禁用一个表上所有触发器的选项。

**示例**

要重命名一个现有的触发器：

ALTER TRIGGER emp\_stamp ON emp RENAME TO emp\_track\_chgs;

要把一个触发器标记为依赖于一个扩展：

ALTER TRIGGER emp\_stamp ON emp DEPENDS ON EXTENSION emplib;

**兼容性**

ALTER TRIGGER是一种瀚高数据库的SQL标准扩展。

**另见**

ALTER ROLE

### 2.40. ALTER TYPE

ALTER TYPE — 更改一个类型的定义

**大纲**

ALTER TYPE name action \[, … \]

ALTER TYPE name OWNER TO { new\_owner | CURRENT\_USER | SESSION\_USER }

ALTER TYPE name RENAME ATTRIBUTE attribute\_name TO new\_attribute\_name \[ CASCADE

| RESTRICT \]

ALTER TYPE name RENAME TO new\_name

ALTER TYPE name SET SCHEMA new\_schema

ALTER TYPE name ADD VALUE \[ IF NOT EXISTS \] new\_enum\_value \[ { BEFORE |

AFTER } neighbor\_enum\_value \]

ALTER TYPE name RENAME VALUE existing\_enum\_value TO new\_enum\_value

这里action 是以下之一：

ADD ATTRIBUTE attribute\_name data\_type \[ COLLATE collation \] \[ CASCADE |

RESTRICT \]

DROP ATTRIBUTE \[ IF EXISTS \] attribute\_name \[ CASCADE | RESTRICT \]

ALTER ATTRIBUTE attribute\_name \[ SET DATA \] TYPE data\_type

\[ COLLATE collation \] \[ CASCADE | RESTRICT \]

**描述**

ALTER TYPE更改一种现有类型的定义。它有几种形式：

ADD ATTRIBUTE

这种形式为一种组合类型增加一个新属性，使用的语法和CREATE TYPE相同。

DROP ATTRIBUTE \[ IF EXISTS \]

这种形式从一种组合类型删除一个属性。如果指定了IF EXISTS并且该属性不存在，则不会抛出错误。这种情况下会发出一个提示。

SET DATA TYPE

这种形式更改一种组合类型的一个属性类型。

OWNER

这种形式更改该类型的拥有者。

RENAME

这种形式更改该类型的名称或者一种组合类型的一个属性的名称。

SET SCHEMA

这种形式把该类型移动到另一个模式中。

ADD VALUE \[ IF NOT EXISTS \] \[ BEFORE | AFTER \]

这种形式为一种枚举类型增加一个新值。可以用BEFORE或者AFTER一个现有值来指定新值在枚举顺序中的位置。否则，新项会被增加在值列表的最后。

如果指定了IF NOT EXISTS，该类型已经包含新值时不会发生错误：会发出一个提示但是不采取其他行动。否则，如果新值已经存在会发生错误。

RENAME VALUE

该形式重命名枚举类型的值。该值在枚举排序中的位置不受影响。如果指定的值不存在或新名称已存在，则会发生错误。

ADD ATTRIBUTE、DROP ATTRIBUTE和ALTER ATTRIBUTE动作可以被整合到一个多个修改组成的列表中，以便被平行应用。例如，可以在一个命令中增加多个属性并且/或者修改多个属性的类型。

要使用ALTER TYPE，你必须拥有该类型。要更改一个类型的模式，你还必须拥有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该类型的模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建该类型做不到的事情。不过，一个超级用户怎么都能更改任何类型的所有权。）。

要增加一个属性或者修改一个属性类型，你还必须具有该数据类型上的USAGE特权。

**参数**

name

要修改的一个现有类型的名称（可能被模式限定）。

new\_name

该类型的新名称。

new\_owner

该类型新拥有者的用户名。

new\_schema

该类型的新模式。

attribute\_name

要增加、修改或者删除的属性名称。

new\_attribute\_name

要被重命名的属性的新名称。

data\_type

要增加的属性的数据类型，或者是要修改的属性的新类型。

new\_enum\_value

要被增加到一个枚举类型的值列表的新值，或将赋予现有值的新名称。和所有枚举文本一样，它需要被引号引用。

neighbor\_enum\_value

一个现有枚举值，新值应该被增加在紧接着该枚举值之前或者之后的位置上。和所有枚举文本一样，它需要被引号引用。

existing\_enum\_value

现有的应该重命名的枚举值。和所有的枚举文本一样，它需要被引号引用。

CASCADE

自动将操作传播到被更改类型的类型表及其后代。

RESTRICT

如果被更改的类型是类型表的类型，则拒绝该操作。这是默认设置。

**注解**

如果ALTER TYPE … ADD VALUE（增加一个新值到枚举类型的形式）不能在一个事务块中执行，新值不能被使用直到事务被提交之后。

涉及到一个新增加枚举值的比较有时会被只涉及原始枚举值的比较更慢。这通常只会在利用BEFORE或者AFTER来把新值的排序位置设置为非列表结尾的地方时发生。不过，有时候即使把新值增加到最后时也会发生这种情况（如果创建了该枚举类型之后出现过OID计数器“回卷”，就会发生这种情况）。这种减速通常不明显，但是如果它确实带来了麻烦，通过删除并且重建该枚举类型或者转储并且重载整个数据库可以重新得到最优性能。

**示例**

要重命名一个数据类型：

ALTER TYPE electronic\_mail RENAME TO email;

把类型email的拥有者改为 joe：

ALTER TYPE email OWNER TO joe;

把类型email的模式改为 customers：

ALTER TYPE email SET SCHEMA customers;

增加一个新属性到一个类型：

ALTER TYPE compfoo ADD ATTRIBUTE f3 int;

在一个特定的排序位置上为一个枚举类型增加一个新值：

ALTER TYPE colors ADD VALUE ‘orange’ AFTER ‘red’;

重命名一个枚举值：

ALTER TYPE colors RENAME VALUE ‘purple’ TO ‘mauve’;

**兼容性**

增加和删除属性的变体是SQL标准的一部分，而其他变体是瀚高数据库扩展。

**另见**

CREATE TYPE, DROP TYPE

### 2.41. ALTER USER

ALTER USER — 更改一个数据库角色

**大纲**

ALTER USER role\_specification \[ WITH \] option \[ … \]

其中 option 可以是：

SUPERUSER | NOSUPERUSER

| CREATEDB | NOCREATEDB

| CREATEROLE | NOCREATEROLE

| INHERIT | NOINHERIT

| LOGIN | NOLOGIN

| REPLICATION | NOREPLICATION

| BYPASSRLS | NOBYPASSRLS

| CONNECTION LIMIT connlimit

| \[ ENCRYPTED \] PASSWORD ‘password’ | PASSWORD NULL

| VALID UNTIL ‘timestamp’

ALTER USER name RENAME TO new\_name

ALTER USER { role\_specification | ALL } \[ IN DATABASE database\_name \]

SET configuration\_parameter { TO | = } { value | DEFAULT }

ALTER USER { role\_specification | ALL } \[ IN DATABASE database\_name \]

SET configuration\_parameter FROM CURRENT

ALTER USER { role\_specification | ALL } \[ IN DATABASE database\_name \]

RESET configuration\_parameter

ALTER USER { role\_specification | ALL } \[ IN DATABASE database\_name \] RESET ALL

其中 role\_specification 可以是：

role\_name

| CURRENT\_USER

| SESSION\_USER

**描述**

ALTER USER现在是ALTER ROLE的一种别名。

**兼容性**

ALTER USER语句是一种瀚高数据库扩展。SQL标准把用户的定义留给实现来处理。

**另见**

ALTER ROLE

### 2.42. ALTER USER MAPPING

ALTER USER MAPPING — 更改一个用户映射的定义

**大纲**

ALTER USER MAPPING FOR { user\_name | USER | CURRENT\_USER | SESSION\_USER |

PUBLIC }

SERVER server\_name

OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \] )

**描述**

ALTER USER MAPPING更改一个用户映射的定义。

一个外部服务器的拥有者可以为任何用户修改用于该服务器的用户映射。还有，如果一个用户被授予了外部服务器上的USAGE特权，它就能为它们自己的用户名修改一个用户映射。

**参数**

user\_name

该映射的用户名。CURRENT\_USER和USER匹配当前用户的名称。PUBLIC被用来匹配系统中所有当前以及未来的用户名。

server\_name

该用户映射的服务器名。

OPTIONS ( \[ ADD | SET | DROP \] option \[‘value’\] \[, … \] )

为该用户映射更改选项。新选项会覆盖任何之前指定的选项。ADD、SET和DROP指定要被执行的动作。如果没有显式地指定操作，将假定为ADD。选项名称必须为唯一，该服务器的外部数据包装器也会验证选项。

**示例**

为服务器foo的用户映射bob更改口令：

ALTER USER MAPPING FOR bob SERVER foo OPTIONS (SET password ‘public’);

**兼容性**

ALTER USER MAPPING符合ISO/IEC 9075-9 (SQL/MED)。有一点细微的语法问题：该标准会忽略FOR关键字。由于CREATE USER MAPPING以及 DROP USER MAPPING都在类似的位置上使用FOR，并且IBM DB2 （作为其他主要的 SQL/MED 实现）也在 ALTER USER MAPPING中要求该关键字，因此为了一致性和互操作性，瀚高数据库在这里的实现与标准不同。

**另见**

CREATE USER MAPPING, DROP USER MAPPING

### 2.43. ALTER VIEW

ALTER VIEW — 更改一个视图的定义

**大纲**

ALTER VIEW \[ IF EXISTS \] name ALTER \[ COLUMN \] column\_name SET

DEFAULT expression

ALTER VIEW \[ IF EXISTS \] name ALTER \[ COLUMN \] column\_name DROP DEFAULT

ALTER VIEW \[ IF EXISTS \] name OWNER TO { new\_owner | CURRENT\_USER |

SESSION\_USER }

ALTER VIEW \[ IF EXISTS \] name RENAME TO new\_name

ALTER VIEW \[ IF EXISTS \] name SET SCHEMA new\_schema

ALTER VIEW \[ IF EXISTS \] name SET ( view\_option\_name \[= view\_option\_value\]

\[, … \] )

ALTER VIEW \[ IF EXISTS \] name RESET ( view\_option\_name \[, … \] )

**描述**

ALTER VIEW更改一个视图的多种辅助属性（如果想要修改视图的查询定义，应使用CREATE OR REPLACE VIEW）。

要使用ALTER VIEW，你必须拥有该视图。要更改一个视图的模式，你还必须具有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该视图的模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建视图做不到的事情。不过，一个超级用户怎么都能更改任何视图的所有权。）。

**参数**

name

一个现有视图的名称（可以是模式限定的）。

IF EXISTS

该视图不存在时不要抛出一个错误。这种情况下会发出一个提示。

SET/DROP DEFAULT

这些形式为一个列设置或者移除默认值。对于任何在该视图上的INSERT或者UPDATE命令，一个视图列的默认值会在引用该视图的任何规则或触发器之前被替换进来。因此，该视图的默认值将会优先于来自底层关系的任何默认值。

new\_owner

该视图的新拥有者的用户名。

new\_name

该视图的新名称。

new\_schema

该视图的新模式。

SET ( view\_option\_name \[= view\_option\_value\] \[, … \] )

RESET ( view\_option\_name \[, … \] )

设置或者重置一个视图选项。当前支持的选项有：

check\_option (string)

更改该视图的检查选项。值必须是local 或者cascaded。

security\_barrier (boolean)

更改该视图的安全屏障属性。值必须是一个布尔值，如true或者false。

**注解**

由于历史原因，ALTER TABLE也可以用于视图，但是只允许等效于以上形式的ALTER TABLE变体用于视图。

**示例**

把视图foo重命名为bar：

ALTER VIEW foo RENAME TO bar;

要为一个可更新视图附加一个默认列值：

CREATE TABLE base\_table (id int, ts timestamptz);

CREATE VIEW a\_view AS SELECT \* FROM base\_table;

ALTER VIEW a\_view ALTER COLUMN ts SET DEFAULT now();

INSERT INTO base\_table(id) VALUES(1); – ts will receive a NULL

INSERT INTO a\_view(id) VALUES(2); – ts will receive the current time

**兼容性**

ALTER VIEW是一种瀚高数据库的SQL标准扩展。

**另见**

CREATE VIEW, DROP VIEW

### 2.44. ANALYZE

ANALYZE — 收集有关一个数据库的统计信息

**大纲**

ANALYZE \[ ( option \[, …\] ) \] \[ table\_and\_columns \[, …\] \]

ANALYZE \[ VERBOSE \] \[ table\_and\_columns \[, …\] \]

其中option可以是：

VERBOSE \[ boolean \]

SKIP\_LOCKED \[ boolean \]

table\_and\_columns是：

table\_name \[ ( column\_name \[, …\] ) \]

**描述**

ANALYZE收集一个数据库中的表的内容的统计信息，并且将结果存储在pg\_statistic系统目录中。接下来，查询规划器会使用这些统计信息来帮助确定查询最有效的执行计划。

如果没有table\_and\_columns列表，则ANALYZE处理当前用户有权分析的当前数据库中的每个表和物化视图。使用列表，ANALYZE仅处理那些表。还可以给出表的列名列表，在这种情况下，仅收集这些列的统计信息。

当选项列表用括号括起来时，选项可以按任何顺序来写。

**参数**

VERBOSE

允许显示进度消息。

SKIP\_LOCKED

规定ANALYZE在开始处理一个关系时不应等待任何冲突的锁被释放:如果关系不能无需等待立即锁定，则跳过该关系。请注意即使采用此选项，ANALYZE在打开关系的索引或从分区、表继承子级和某些类型的外表获取样本行时仍可能阻塞。此外，当ANALYZE通常处理指定分区表的所有分区时，如果分区表上有一个冲突的锁，这个选项将导致ANALYZE跳过所有分区表。

boolean

规定所选的选项打开或关闭。您可以写TRUE、ON或1以启用该选项，或者是FALSE、OFF或0来禁用它。boolean值可以被省略，在假定为TRUE的情况下。

table\_name

要分析的一个指定表的名称（可以是模式限定的）。如果省略，则分析当前数据库中的所有常规表、分区表和物化视图（但不包含外部表）。如果指定的表是分区表，则整个分区表的继承统计信息和各个分区的统计信息都将更新。

column\_name

要分析的一个指定列的名称。默认是所有列。

**输出**

当指定了VERBOSE时，ANALYZE会发出进度消息来指示当前正在处理哪个表。还会打印有关那些表的多种统计信息。

**注解**

要分析表，通常必须是该表的所有者或超级用户。不过，数据库所有者可以分析数据库中的所有表，共享目录除外。（对共享目录的限制意味着真正的数据库范围的ANALYZE只能由超级用户执行。）ANALYZE将跳过调用用户没有分析权限的任何表。

只有被显式选中时才会分析外部表。并非所有外部数据包装器都支持ANALYZE。如果表的包装器不支持ANALYZE，该命令会打印一个警告并且什么也不做。

在默认的瀚高数据库配置中，自动清理守护进程会在表第一次载入数据或者用常规操作改变时负责表的自动分析。当启用自动清理时，定期运行ANALYZE是个好主意，或者可以在表内容做了大的修改后运行ANALYZE。准确的统计信息将帮助规划器选择最合适的查询计划，从而提升查询处理的速度。主读数据库的一般策略是在一天中使用量最低时运行一次VACUUM和ANALYZE（如果有大量的更新动作则是不够的）。

ANALYZE只要求目标表上的一个读锁，因此它可以和表上的其他动作并行。

ANALYZE收集的统计信息通畅包括每列中最常见值的列表以及展示每列中近似数据分布的一个直方图。如果ANALYZE认为这些东西无趣（例如在一个唯一键列中，没有共同值）或者该列的数据类型不支持合适的操作符，以上工作都会被省略。

对于大型的表，ANALYZE会对表内容做随机采样而不是检查每一行。这允许在很少的时间内完成对大型表的分析。不过要注意，这些统计信息只是近似值，并且即使实际表内容没有改变，每次运行ANALYZE时统计信息都会有微小地改变。这可能会导致EXPLAIN显示的规划器估算代价有小的改变。在很少的情况下，这会非决定性地导致规划器的查询计划选择在ANALYZE运行后改变。为了避免这种情况，可以按照下文所述提高ANALYZE所收集的统计信息量。

通过调整default\_statistics\_target配置变量可以控制分析量，对每个列可以用ALTER TABLE … ALTER COLUMN … SET STATISTICS设置每列的统计信息目标（见 ALTER ROLE ）。目标值会设置最常用值列表中的最大项数以及直方图中的最大容器数。默认目标值是 100，可以把它调大或者调小在规划器估计值精度和ANALYZE花费的时间以及pg\_statistic所占空间之间做出平衡。特别地，将统计信息目标设置为零会禁用该列的统计信息收集。在查询的WHERE、GROUP BY或者ORDER BY子句中从不出现的列上这样做会有所帮助，因为规划器用不上这些列上的统计信息。

被分析的列中最大的统计信息目标决定了为准备统计信息要采样的表行数。增加该目标会导致做ANALYZE所需的时间和空间成比例增加。

ANALYZE所估算的值之一是出现在每个列中的可区分值。因为只会检查行的一个子集，即便使用最大的统计信息目标，这种估计有时也可能很不精确。如果这种不精确导致不好的查询计划，可以手工确定一个更精确的值并且用ALTER TABLE … ALTER COLUMN … SET (n\_distinct = …)设置该值（见ALTER TABLE）。

如果被分析的表有一个或者更多子表，ANALYZE将会收集两次统计信息：一次只对父表的行收集，第二次则在父表及其所有子表的行上收集。在规划需要遍历整个继承树的查询时需要第二个统计信息集。不过，在决定是否触发表上的自动分析时，自动清理后台进程将只考虑父表本身上的插入和更新。如果该表很少被插入或者更新，只有手工运行ANALYZE时才会把继承统计信息更新到最新。

如果任何子表是外部表并且其外部数据包装器不支持ANALYZE，在收集继承统计信息时会忽略那些子表。

如果被分析的表不完全为空，ANALYZE将不会为该表记录新统计信息。任何现有统计信息将会被保留。

**兼容性**

SQL 标准中没有ANALYZE语句。

**另见**

VACUUM, vacuumdb

### 2.45. AUDIT

AUDIT — 配置审计(仅安全版)

**大纲**

AUDIT statement\_opts \[, …\]|ALL

BY username \[,…\]|ALL

\[WHENEVER \[NOT\] SUCCESSFUL\]

AUDIT object\_opts\_on \[schema.\]objname\[.colname\]

BY username\[,…\]|ALL

\[WHENEVER \[NOT\] SUCCESSFUL\]

其中 statement\_opts是以下之一：

CREATE ROLE

CREATE DOMAIN

CREATE PROCEDURE

CREATE INDEX

CREATE SCHEMA

CREATE SEQUENCE

CREATE TABLE

CREATE TABLE AS

CREATE TRIGGER

CREATE USER

CREATE VIEW

CREATE EXTENSION

CREATE DATABASE

ALTER ROLE

ALTER DOMAIN

ALTER PROCEDURE

ALTER INDEX

ALTER SYSTEM

ALTER SCHEMA

ALTER SEQUENCE

ALTER TABLE

ALTER TRIGGER

ALTER USER

ALTER VIEW

ALTER EXTENSION

ALTER DATABASE

DROP DOMAIN

DROP PROCEDURE

DROP ROLE

DROP INDEX

DROP SCHEMA

DROP SEQUENCE

DROP TABLE

DROP TRIGGER

DROP USER

DROP VIEW

DROP DATABASE

DROP EXTENSION

SELECT

SELECT INTO

INSERT

UPDATE

DELETE

GRANT

REVOKE

VALUES (1, '{{" "," "," "},{" "," "," "},{" "," "," "}}'); VALUES (2, '{{X," "," "},{" ",O," "},{" ",X," "}}');