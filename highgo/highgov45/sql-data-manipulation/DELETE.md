---
title: "删除 DELETE"
book: "数据操纵"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/DELETE.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-manipulation
---

## 删除DELETE

和前面插入数据一样，对表的删除操作只能实现整行删除，而不能删除行的部分数据。

数据的删除语句如下所示：

```sql
DELETE FROM table_name WHERE [condition];
```

例如删除表 person 中 address 值为 ‘street\_1’ 的行的数据：

```sql
highgo=# DELETE FROM person WHERE address='street_1';
DELETE 2
```

如果没有指定 `WHERE` 子句，那么表中所有记录都将被删除，但是只删除了表的数据，表格还在的。

```sql
highgo=# DELETE FROM person;
DELETE 5
highgo=# SELECT* FROM person;
 id | name | age | address 
----+------+-----+---------
(0 行记录)
```