---
title: "插入 INSERT"
book: "数据操纵"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/INSERT.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-manipulation
---

## 插入INSERT

向表中插入一条数据，数据的值是按照这些列在表中出现的顺序列出的。插入的值通常是常量，但也允许使用标量表达式。向表中插入数据的语法的缺点是你必须知道表中列的顺序，要避免这个问题，可以显式地列出列。

插入语句如下所示：

```sql
INSERT INTO table_name VALUES (value1,value2,...,valueN);
```

显式列出列进行数据插入的语句如下所示：

```sql
INSERT INTO table_name(colname1,colname2,...,colnameN) VALUES (value1,value2,...,valueN);
```

显式列出的插入方式可以只插入部分列的数据，未插入的列在查询时将被填充为它们的缺省值。

例如在 person 表中插入部分数据：

```sql
INSERT INTO person (id,name,age,address) VALUES (1,'Amy',20,'street_1');
INSERT INTO person VALUES (2,'Bob',19,'street_2');
INSERT INTO person (id,name) VALUES (2,'Bob');
INSERT INTO person VALUES (1, 'Cindy');
```

第四种形式是HGDB的一个扩展，它使用给出的值从左开始填充列，有多少个给出的列值就填充多少个列，其他列的将使用缺省值。

在数据插入时，HGDB 也支持多行插入，插入的多行数据格式应相同，数据之间用逗号分隔。

例如在 person 表中插入多条数据：

```sql
highgo=# INSERT INTO person VALUES
(3,'Candy',19,'street_1'), 
(4,'Daisy',21,'street_2'),
(5,'Emma',21,'street_3');
INSERT 0 3
```

除了插入常量和标量，也可以插入查询的结果（可能没有行、一行或多行）。

例如向 person 表中插入如下查询结果：

```sql
INSERT INTO person (id, name, age) 
SELECT id, name, age FROM new_person 
WHERE address = 'street_1';
```