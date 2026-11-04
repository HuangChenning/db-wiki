---
title: "表达式"
book: "数据查询"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/sql/expression.html"
tags:
  - highgo
  - highgo-v45
  - sql-data-query
---

## 表达式

这里对表表达式进行介绍，与值表达式不同，值表达式也称为标量表达式，是一个标量，表表达式计算一个表，是一个结果。表表达式包含一个 `FROM` 子句，子句中可以根据需要选用 `WHERE` 、 `GROUP BY` 和 `HAVING` 关键字添加相应条件。这些条件对 `FROM` 子句引用的表指定了一系列转换操作，所有这些转换最后生成一个虚拟表，虚拟表提供行传递给选择列表计算查询的输出结果。

### SELECT 命令

从数据库中检索数据的过程或命令叫做查询。

`SELECT` 的查询语句如下所示：

```sql
SELECT select_list FROM table_expression [sort_specification]
```

例如查询 person 表中的 name 和 age 两列信息：

```sql
SELECT name,age FROM person;
```

如果想要查询该表的全部内容，select\_list 用 `*` 来代替即可。

一个选择列表也可以选择可用列的一个子集或者在使用它们之前对列进行计算，例如进行下面的查询：

```sql
SELECT a,b+c FROM table1;
```

`FROM table1` 是一种非常简单的表表达式，它只读取了一个表，通常，表表达式可以是基本表、连接和子查询组成的复杂结构，但也可以省略整个表表达式而把 `SELECT` 命令当做一个计算器：

```sql
SELECT 3*4+(5-2)*6;
```

如果选择列表里的表达式返回变化的结果，可以用 `SELECT` 来调用函数：

例如用 `SELECT` 调用随机函数：

```sql
SELECT random();
```

### FROM 子句

FROM 子句从一个用逗号分隔的表引用列表中的一个或多个其它表中生成一个表。

```sql
FROM table_reference [, table_reference [, ...]]
```

表引用可以是一个表名字或者是一个生成的临时表，该表可以进行由 `WHERE` 、 `GROUP BY` 和 `HAVING` 子句指定的转换，并最后生成全局的表表达式结果。如果在 `FROM` 子句中引用了多于一个表， 那么它们被交叉连接（即构造它们的行的笛卡尔积）。

### WHERE 子句

```sql
WHERE search_condition
```

注意 search\_condition 返回一个 boolean 类型值。

例如将 orders 订单表中 order\_id 为1的商品的 quantity 属性修改为5：

```sql
UPDATE orders SET quantity=5 WHERE order_id =1;
```

这里 `WHERE order_id = 1` 就是一个 boolean 类型，如果等式成立，结果为 1，如果等式不成立，结果为 0。

WHERE 子句里面也可以用 AND、OR 进行条件的组合，例如查询 person 表中年龄大于19、住址不为 stress\_1的结果：

```sql
SELECT* FROM person WHERE age>19 AND address != 'stress_1';
```

### HAVING 子句

理解 `WHERE` 以及 `HAVING` 子句之间的关系对我们非常重要。 `WHERE` 和 `HAVING` 的基本区别如下： `WHERE` 在分组和聚集计算之前选取输入行（因此，它控制哪些行进入聚集计算）， 而 `HAVING` 在分组和聚集之后选取分组行。因此， `WHERE` 子句不能包含聚集函数，因为试图用聚集函数判断哪些行应输入给聚集运算是没有意义的。相反， `HAVING` 子句总是包含聚集函数（严格说来，你可以写不使用聚集的 `HAVING` 子句）。

例如在 weather 表中筛选城市最高低温低于40度的城市：

```sql
SELECT city,max(temp_lo)
FROM weather
GROUP BY city
HAVING max(temp_lo)<40;
```

### LIKE

LIKE 操作符进行模式匹配，下划线 （\_）匹配单个字符，百分号（%）匹配任何零或更多个字符的序列。

例如可以将上面 HAVING 的例子修改为查询 H 开头的城市中最高低温低于40的城市。

```sql
SELECT city,max(temp_lo)
FROM weather
WHERE city LIKE'H%'
GROUP BY city
HAVING max(temp_lo)<40;
```

如果将 WHERE 条件中的 `LIKE 'H%'` 用 `LIKE 'H_'` 替换，查询结果将为0。

查询 person 表中年龄以2开头的信息：

```sql
SELECT* FROM person WHERE age::text LIKE '2_';
```

查询结果如下：

```sql
id | name  | age | address  
----+-------+-----+----------
  1 | Daisy |  21 | street_4
  1 | Emma  |  21 | street_4
(2 行记录)
```