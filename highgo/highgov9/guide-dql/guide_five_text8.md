---
title: "表和列名"
book: "数据查询DQL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_five_text8.html"
tags:
  - highgo
  - highgo-v9
  - guide-dql
---

## 表和列别名

你可以给一个表或复杂的表引用指定一个临时的名字，用于剩下的查询中引用那些派生的表，这叫做表别名。

创建表别名的语句如下（AS可以省略）：

```
FROM table_references AS alias
```

例如在对表 produts 和表 orders 做内连接时，为方便表示连接条件，可以在 FROM 子句里对两个表指定别名 p 和 o：

```
SELECT* FROM products p JOIN orders o on p.product_no = o.product_no;
```

表别名主要用于简化符号，但是当把一个表连接到它自身时必须使用别名，例如查找 people 表中的孙辈和祖辈关系：

```
SELECT * FROM people AS mother JOIN people AS child ON mother.id = child.mother_id;
```

如果一个表引用是一个子查询，则必须要使用一个别名。

另外一种给表指定别名的形式是给表的列赋予临时名字，如果指定的列别名比表里实际的列少，那么剩下的列就没有被重命名。

给表的列指定别名的语句如下：

```
FROM table_reference [AS] alias ( column1 [, column2 [, ...]] )
```

例如为表 products 和表 orders 创建列别名：

```
highgo=# SELECT* FROM products a (a,b,c);
 a | b | c 
---+---+---
 1 | a | 1
(1 行记录)

highgo=# SELECT* FROM orders A(d);
 d | product_no | quantity 
---+------------+----------
 1 |          1 |        1
(1 行记录)
```