---
title: "更新 UPDATE"
book: "数据操纵DML"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_four_text3.html"
tags:
  - highgo
  - highgo-v9
  - guide-dml
---

## 更新 UPDATE

修改已经存储在数据库中的数据的行为叫做更新，可以更新单个行、部分行、所有行，也可以独立地更新一列信息而其他的列不受影响。要更新现有的行，使用 `UPDATE` 命令，这需要提供三部分信息：

1. 表的名字和要更新的列名
2. 列的新值
3. 要更新的是哪（些）行
```
UPDATE table_name SET colname1 = value1, colname2 = value2, ..., colnameN = valueN 
WHERE [condition]
```

condition为更新的筛选条件

例如对 person 表进行如下更新操作：

1）筛选 person 表中 age 为21的行，将其 address 列的值修改为 ‘济南’；

2）将表中 id 列的信息都更新为 1。

```
1 UPDATE person SET address='street_4' WHERE age=21;
2 UPDATE person SET id=1;
```

此时查询该表将得到以下内容：

```
highgo=# SELECT* FROM person;
 id | name  | age | address  
----+-------+-----+----------
  1 | Amy   |  20 | street_1
  1 | Bob   |  19 | street_2
  1 | Bob   |     | 
  1 | Cindy |     | 
  1 | Candy |  19 | street_1
  1 | Daisy |  21 | street_4
  1 | Emma  |  21 | street_4
(7 行记录)
```