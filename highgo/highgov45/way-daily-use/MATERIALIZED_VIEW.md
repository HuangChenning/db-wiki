---
title: "21、管理物化视图（MATERIALIZED VIEW）"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/MATERIALIZED_VIEW.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## 管理物化视图（MATERIALIZED VIEW）

## 一、创建物化视图

### 1、CREATE MATERIALIZED VIEW 定义一个新的物化视图

```
Synopsis
CREATE MATERIALIZED VIEW [ IF NOT EXISTS ] table_name
[ (column_name [, ...] ) ]
[ WITH ( storage_parameter [= value] [, ... ] ) ]
[ TABLESPACE tablespace_name ]
AS query
[ WITH [ NO ] DATA ]
```

## 2、描述

CREATE MATERIALIZED VIEW定义一个查询的物化视图。 在该命令被发出时，查询会被执行并且被用来填充该视图（除非使用了 WITH NO DATA），并且后来可能会用 REFRESH MATERIALIZED VIEW进行刷新。

## 3、参数

IF NOT EXISTS

如果已经存在一个同名的物化视图时不要抛出错误。这种情况下会发出一个 提示。注意这不保证现有的物化视图与即将创建的物化视图相似。

table\_name

要创建的物化视图的名称（可以被模式限定）。

column\_name

新物化视图中的一个列名。如果没有提供列名，会从查询的输出列名来得到。

WITH ( storage\_parameter \[= value\] \[, … \] )

这个子句为新的物化视图指定可选的存储参数。WITH子句能够为表或与一个UNIQUE、PRIMARY KEY或者EXCLUDE约束相关的索引指定存储参数。

TABLESPACE tablespace\_name

tablespace\_name是 要把新物化视图创建在其中的表空间的名称。

query

一个SELECT、TABLE 或者VALUES命令。这个查询将在一个安全受限的操作中运行。 特别说明，对本身会创建临时表的函数的调用将会失败。

WITH \[ NO \] DATA

这个子句指定物化视图是否在创建时被填充。如果不是，该物化视图将被标记为不可扫描并且在REFRESH MATERIALIZED VIEW被使用前不能被查询。

## 4、示例

创建物化视图：

```
highgo=# CREATE MATERIALIZED VIEW IF NOT EXISTS tbl_view TABLESPACE pg_default as  select * from tbl WITH no data;
CREATE MATERIALIZED VIEW
highgo=# select * from tbl_view;
ERROR:  55000: materialized view "tbl_view" has not been populated
提示:  Use the REFRESH MATERIALIZED VIEW command.
highgo=# REFRESH MATERIALIZED VIEW tbl_view;
REFRESH MATERIALIZED VIEW
highgo=# select * from tbl_view;
  id
------
    1
    2
    3
```

## 二、修改物化视图

### 1、ALTER MATERIALIZED VIEW 更改一个物化视图的定义

```
Synopsis
ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    action [, ... ]
ALTER MATERIALIZED VIEW name
    DEPENDS ON EXTENSION extension_name
ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    RENAME [ COLUMN ] column_name TO new_column_name
ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    RENAME TO new_name
ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    SET SCHEMA new_schema
ALTER MATERIALIZED VIEW ALL IN TABLESPACE name [ OWNED BY role_name [, ... ] ]
    SET TABLESPACE new_tablespace [ NOWAIT ]
```

其中 action是下列之一：

```
ALTER [ COLUMN ] column_name SET STATISTICS integer
ALTER [ COLUMN ] column_name SET ( attribute_option = value [, ... ] )
ALTER [ COLUMN ] column_name RESET ( attribute_option [, ... ] )
ALTER [ COLUMN ] column_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN }
CLUSTER ON index_name
SET WITHOUT CLUSTER
SET ( storage_parameter = value [, ... ] )
RESET ( storage_parameter [, ... ] )
OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
```

### 2、描述

ALTER MATERIALIZED VIEW更改一个现有物化视图的多个辅助属性。

要使用ALTER MATERIALIZED VIEW，你必须拥有该物化视图。要更改一个物化视图的模式，你还必须拥有新模式上的CREATE特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须拥有该物化视图所在模式上的CREATE特权（这些限制强制修改拥有者不能做一些通过删除和重建该物化视图做不到的事情。不过，一个超级用户怎么都能更改任何视图的所有权。）。

DEPENDS ON EXTENSION形式把该物化视图标记为依赖于一个扩展，这样该扩展被删除时会自动地删除掉这个物化视图。

可用于ALTER MATERIALIZED VIEW的语句形式和动作是 ALTER TABLE的一个子集，并且在用于物化视图时具有相同的含义。

### 3、参数

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

### 4、示例

把物化视图tbl\_view 重命名为 tbl\_view\_backup：

```
highgo=# ALTER MATERIALIZED VIEW tbl_view RENAME to tbl_view_backup;
ALTER MATERIALIZED VIEW
```

## 三、移除物化视图

### 1、DROP MATERIALIZED VIEW 移除一个物化视图

```
Synopsis
DROP MATERIALIZED VIEW [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

### 2、描述

DROP MATERIALIZED VIEW删除一个现有的物化视图。要执行这个命令你必须是该物化视图的拥有者。

### 3、参数

IF EXISTS

如果该物化视图不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的物化视图的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该物化视图的对象（例如其他物化视图或常规视图），然后删除所有依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该物化视图，则拒绝删除它。这是默认值。

### 4、示例

这个命令将移除名为tbl\_view的物化视图：

```
highgo=# DROP MATERIALIZED VIEW tbl_view ;
DROP MATERIALIZED VIEW
```

## 四、更新物化视图

### 1、REFRESH MATERIALIZED VIEW 更新一个物化视图的内容

```
Synopsis
REFRESH MATERIALIZED VIEW [ CONCURRENTLY ] name
[ WITH [ NO ] DATA ]
```

### 2、描述

REFRESH MATERIALIZED VIEW完全刷新一个物化视图的内容。你必须是该物化视图的属主才能执行这个命令.旧的内容会被抛弃。如果指定了 WITH DATA（或者作为默认值），支持查询将被执行以提供新的数据，并且会让物化视图将处于可扫描的状态。如果指定了 WITH NO DATA，则不会生成新数据并且会让物化视图处于一种不可扫描的状态。

CONCURRENTLY和WITH NO DATA 不能被一起指定。

### 3、参数

CONCURRENTLY

对物化视图的刷新不阻塞在该物化视图上的并发选择。如果没有这个选项，一次影响很多行的刷新将使用更少的资源并且更快结束，但是可能会阻塞其他尝试从物化视图中读取的连接。这个选项在只有少量行被影响的情况下可能会更快。

只有当物化视图上有至少一个UNIQUE索引（只用列名 并且包括所有行）时，才允许这个选项。也就是说，该索引不能建立在任何表达式上或者包括WHERE子句。

当物化视图还未被填充时，这个选项不能被使用。

即使带有这个选项，对于任意一个物化视图一次也只能运行一个 REFRESH。

name

要刷新的物化视图的名称（可以被模式限定）。

注解

虽然用于未来的CLUSTER操作的默认索引会被保持， REFRESH MATERIALIZED VIEW不会基于这个属性排序产生的行。如果希望数据在产生时排序，必须在支持查询中使用 ORDER BY子句。

### 4、示例

这个命令将使用物化视图tbl\_view\_backup定义中的查询来替换该物化视图的内容，并且让它处于一种可扫描的状态：

```
highgo=# REFRESH MATERIALIZED VIEW tbl_view_backup;
REFRESH MATERIALIZED VIEW
```

这个命令将释放与物化视图tbl\_view\_backup相关的存储并且让它变成一种不可扫描的状态：

```
highgo=# REFRESH MATERIALIZED VIEW tbl_view_backup WITH NO DATA;
REFRESH MATERIALIZED VIEW
highgo=# select * from tbl_view_backup;
ERROR:  55000: materialized view "tbl_view_backup" has not been populated
提示:  Use the REFRESH MATERIALIZED VIEW command.
```