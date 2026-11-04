---
title: "删除 DROP"
book: "数据定义"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/DROP.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-definition
---

## 删除 DROP

数据库、用户、表、视图、模式、索引等对象的删除均通过 `DELETE` 关键字来实现。

### 删除数据库

数据库用命令 `DROP DATABASE` 命令删除：

```sql
DROP DATABASE name;
```

只有数据库的拥有者或者超级用户才可以删除数据库，删除数据库会移除其中包括的所有对象，即使那些对象有不同的拥有者。数据库的删除操作不能被撤销。

不能对当前登录的数据库执行 `DROP DATABASE` 命令，因此可以连接到 template1 模板数据库进行删除，template1 是删除一个给定数据库集簇中最后一个用户数据库的唯一选项。

### 删除用户

要删除一个角色，可以使用 `DROP ROLE` 命令：

```sql
DROP ROLE name;
```

### 删除表

要删除一张表，可以使用 `DROP TABLE` 命令：

```sql
DROP TABLE table_name;
```

### 删除视图

要删除创建的视图，可以使用 `DROP VIEW` 命令：

```sql
DROP VIEW view_name;
```

### 删除模式

删除一个空的模式（模式的所有对象已经被删除）：

```sql
DROP SCHEMA myschema;
```

删除一个模式以及其中包含的所有对象：

```sql
DROP SCHEMA myschema CASCADE;
```

### 删除索引

```sql
DROP INDEX index_name;
```

删除 person 表、p\_o\_view 视图、city\_index\_capital 索引的语句如下：

```sql
DROP TABLE person;
DROP VIEW p_o_view;
DROP INDEX city_index_capital;
```