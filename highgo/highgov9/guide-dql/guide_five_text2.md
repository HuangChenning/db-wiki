---
title: "连接表"
book: "数据查询DQL"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/guide/guide_five_text2.html"
tags:
  - highgo
  - highgo-v9
  - guide-dql
---

## 连接表

连接表是根据特定的连接类型从两个其它表中派生的表。

连接的表也可以是连接表，在 JOIN 子句周围可以使用圆括号来控制连接顺序，否则 JOIN 子句会从左至右嵌套。

### 交叉连接

```
TI CROSS JOIN T2
```

交叉连接的结果由所有 T1 里面的列后面跟着所有 T2 里面的列构成。如果两个表分别有 N 和 M 行，连接表将有 N \* M 行。 `FROM T1 CROSS JOIN T2 ` 等效于 `FROM T1 INNER JOIN T2 ON TRUE` ，也等效于 `FROM T1,T2` 。

现在有如下 t1、t2两张表，对他们进行交叉连接：



```
highgo=# SELECT* FROM t1 CROSS JOIN t2;
 num | name | num | value 
-----+------+-----+-------
   1 | a    |   1 | xxx
   1 | a    |   3 | yyy
   1 | a    |   5 | zzz
   2 | b    |   1 | xxx
   2 | b    |   3 | yyy
   2 | b    |   5 | zzz
   3 | c    |   1 | xxx
   3 | c    |   3 | yyy
   3 | c    |   5 | zzz
(9 行记录)
```

### 条件连接

```
T1 { [ INNER ]|{ LEFT|RIGHT|FULL }[ OUTER ]} JOIN T2 ON bollean_expression

T1 { [ INNER ]|{ LEFT|RIGHT|FULL }[ OUTER ]} JOIN T2 USING ( join column list)

T1 NATURAL { [ INNER ]|{ LEFT|RIGHT|FULL }[ OUTER ]} JOIN T2
```

INNER 是缺省；LEFT、RIGHT 和 FULL 指示一个外连接。连接条件在 ON 或 USING 子句中指定，或者用关键字 NATURAL 隐含地指定。ON 子句接收一个和 WHERE 子句里一样的布尔值表达式。

USING 是一种快捷方法，它允许你利用特殊的情况：连接的两端都具有相同的连接列名。例如用 `USING (a, b)` 连接表 T1 和 T2 会产生连接条件 `ON T1.a = T2.a AND T1.b = T2.b` 。

`JOIN USING` 的输出会废除冗余列。 `JOIN ON` 会先产生来自 T1 的所有列，后面跟上所有来自 T2 的列；而 `JOIN USING` 会先为列出的每一个列对产生一个输出列，然后先跟上来自 T1 的剩余列，最后跟上来自 T2 的剩余列。

NATURAL 是 USING 的快捷形式。如果不存在公共列， `NATURAL JOIN` 的行为将和 `JOIN ... ON TRUE` 一样产生交叉集连接。

#### INNER JOIN

**内连接：** 对于 T1 的每一行 R1，生成的连接表都有一行对应 T2 中的每一个满足和 R1 的连接条件的行，即内连接只返回连接表中两个字段相等的行。

例如对 t1 、t2 做内连接：

```
highgo=# SELECT* FROM t1 INNER JOIN t2 ON t1.num= t2.num;
highgo=# SELECT* FROM t1 INNER JOIN t2 USING(num);
highgo=# SELECT* FROM t1 NATURAL INNER JOIN t2;
```

上面三条语句的执行结果相同，结果如下所示：

```
num | name | value 
-----+------+-------
   1 | a    | xxx
   3 | c    | yyy
(2 行记录)
```

#### LEFT OUTER JOIN

**左外连接：** 首先，执行一次内连接。然后，为 T1 中每一个无法在连接条件上匹配 T2 里任何一行的行返回一个连接行，该连接行中 T2 的列用空值补齐，因此，生成的连接表里为来自 T1 的每一行都至少包含一行。左外连接的连接表包括左表中的所有记录和右表中连接字段相等的记录。

等效于 `LEFT JOIN` 。

对 t1、t2 做左外连接的结果如下：

```
highgo=# SELECT* FROM t1 LEFT JOIN t2 ON t1.num= t2.num;
 num | name | num | value 
-----+------+-----+-------
   1 | a    |   1 | xxx
   3 | c    |   3 | yyy
   2 | b    |     | 
(3 行记录)

highgo=# SELECT* FROM t1 LEFT JOIN t2 USING(num);--废除冗余列
 num | name | value 
-----+------+-------
   1 | a    | xxx
   3 | c    | yyy
   2 | b    | 
(3 行记录)
```

#### RIGHT OUTER JOIN

**右外连接：** 首先，执行一次内连接。然后，为 T2 中每一个无法在连接条件上匹配 T1 里任何一行的行返回一个连接行，该连接行中 T1 的列用空值补齐。右外连接的连接表包括右表中的所有记录和左表中连接字段相等的记录。

等效于 `RIGHT JOIN` 。

例如对 t1、t2 做右外连接：

```
highgo=# SELECT* FROM t1 RIGHT JOIN t2 ON t1.num= t2.num;
 num | name | num | value 
-----+------+-----+-------
   1 | a    |   1 | xxx
   3 | c    |   3 | yyy
     |      |   5 | zzz
(3 行记录)
```

#### FULL OUTER JOIN

**全连接：** 首先，执行一次内连接。然后，为 T1 中每一个无法在连接条件上匹配 T2 里任何一行的行返回一个连接行，该连接行中 T2 的列用空值补齐。同样，为 T2 中每一个无法在连接条件上匹配 T1 里任何一行的行返回一个连接行，该连接行中 T1 的列用空值补齐。全连接即返回连接字段相等的记录及左右表中所有剩余记录。

等效于 `FULL JOIN` 。

例如对 t1、t2 做全连接：

```
highgo=# SELECT* FROM t1 FULL JOIN t2 ON t1.num= t2.num;
 num | name | num | value 
-----+------+-----+-------
   1 | a    |   1 | xxx
   2 | b    |     | 
   3 | c    |   3 | yyy
     |      |   5 | zzz
(4 行记录)
```

用 on 指定的连接条件也可以包含其他与连接不直接相关的条件，例如我们在用 num 连接 t1 和 t2 时，对 t2.value 加一个条件：

```
highgo=# SELECT* FROM t1 LEFT JOIN t2 ON t1.num= t2.num AND t2.value='xxx';
 num | name | num | value 
-----+------+-----+-------
   1 | a    |   1 | xxx
   2 | b    |     | 
   3 | c    |     | 
(3 行记录)
```

如果将 t2 的限制条件放在 `WHERE` 子句中将会产生以下结果：

```
highgo=# SELECT* FROM t1 LEFT JOIN t2 ON t1.num=t2.num WHERE t2.value='xxx';
 num | name | num | value 
-----+------+-----+-------
   1 | a    |   1 | xxx
(1 行记录)
```

这是因为放在 ON 子句中的一个约束在连接之前被处理，而放在 WHERE 子句中的一个约束是在连接之后被处理。这对内连接没有关系，但是对于外连接会带来麻烦。