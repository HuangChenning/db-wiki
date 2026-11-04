---
title: "枚举类型"
book: "数据类型"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/enum.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-types
---

## 枚举类型

枚举（enum）类型是由一个静态、值的有序集合构成的数据类型。枚举类型的一个例子可以是一周中的日期，或者一个数据的状态值集合。枚举类型可以使用 `CREATE TYPE` 命令创建。

例如创建并应用一个枚举类型：

```sql
highgo=# CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
CREATE TYPE

highgo=# CREATE TABLE person ( 
name text, 
current_mood mood 
);
CREATE TABLE

highgo=# INSERT INTO person VALUES ('Moe', 'happy');
INSERT 0 1
highgo=# SELECT* FROM person WHERE current_mood='happy';
 name | current_mood 
------+--------------
 Moe  | happy
(1 行记录)
```

在排序的时候，一个枚举类型的值的排序是该类型被创建时所列出的值的顺序，比如上面创建的 mood 类型的排序为 sad、ok、happy。

尽管枚举类型的主要目的是用于值的静态集合，但也有方法在现有枚举类型中增加新值和重命名值。不可以从枚举类型中去除现有的值，也不能更改这些值的排序顺序，如果要那样做可以删除并且重建枚举类型。

例如创建并应用新的枚举类型 happiness：

```sql
highgo=# CREATE TYPE happiness AS ENUM ('happy', 'very happy', 'ecstatic');
CREATE TYPE

highgo=# CREATE TABLE holidays ( 
highgo(# num_weeks integer, 
highgo(# happiness happiness 
highgo(# );
CREATE TABLE
    
highgo=# INSERT INTO holidays VALUES (4,'happy'),(6,'very happy'),(8,'ecstatic');
INSERT 0 3
    
highgo=# INSERT INTO holidays VALUES (2,'sad');
错误:  对于枚举happiness的输入值无效: "sad"

highgo=# SELECT person.name,holidays.num_weeks FROM person,holidays WHERE person.current_mood = holidays.happiness;
错误:  操作符不存在: mood = happiness
```

每一种枚举数据类型都是独立的并且不能和其他枚举类型相比较。不同的枚举类型中即便存在相同的类型，它们之间也不能进行比较。如果你确实需要做这样的事情，可以写一个自定义的操作符或者在查询中加上显式造型：

```sql
highgo=# SELECT person.name,holidays.num_weeks,person.current_mood,holidays.happiness FROM person,holidays WHERE person.current_mood::text = holidays.happiness::text;
 name | num_weeks | current_mood | happiness 
------+-----------+--------------+-----------
 Moe  |         4 | happy        | happy
(1 行记录)
```