---
title: "20、HighGo Database中的约束条件"
book: "日常使用类"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/way/HighGo_constraint.html"
tags:
  - highgo
  - highgo-v45
  - way-daily-use
---

## HighGo Database中的约束条件

## 1、简介

约束的作用是让数据库安全的存储或恢复数据。约束让我们能够根据我们的愿望来控制表中的数据。

各种约束介绍  
传统的约束

## 2、非空约束

一个非空约束（NOT NULL）指定一个列中不会有空值。约束的顺序没有关系，因为并不需要决定约束被检查的顺序。

示例：

```
highgo=# CREATE TABLE products (
    product_no integer NOT NULL,
    name text NOT NULL,
    price numeric
);
```

## 3、唯一约束

唯一约束（UINQUE）保证在一列中或者一组列中保存的数据在表中所有行间是唯一的。允许在有唯一约束的列上存在多个空值。

示例：

```
highgo=# CREATE TABLE products (
    product_no integer UNIQUE,
    name text,
    price numeric
);
```

## 4、主键约束

一个主键约束是表中行的唯一标识符的一个列或者一组列。此时对应的列值都是唯一的并且非空。

示例：

```
highgo=# CREATE TABLE products (
    product_no integer PRIMARY KEY,
    name text,
    price numeric
);
```

## 5、外键约束

一个外键约束指定一列（或一组列）中的值必须匹配另一个表中某些行的值。一个表可以有超过一个的外键约束。一个外键所引用的列必须是一个主键或者被唯一约束所限制。

示例：

```
highgo=# CREATE TABLE posts(
     user_id int NOT NULL REFERENCES users(id)
     ...
     ...
);
```

## 6、检查约束

一个检查约束（CHECK）是最普通的约束类型。它允许我们指定一个特定列中的值必须要满足一个布尔表达式。需要注意的是，一个检查约束在其检查表达式值为真或空值时被满足。

示例：

```
highgo=# CREATE TABLE products(
     name text,
     price int CHECK(price > 0)
);
```

## 7、排他约束

排他约束（exclusion）保证如果将任何两行的指定列或表达式使用指定操作符进行比较，至少其中一个操作符比较将会返回否或空值。

## 8、数据类型

数据类型通常不会被认为是约束条件，但是数据类型可以约束输入的数据的类型，这在某种程度上也可以看作是一种约束条件。