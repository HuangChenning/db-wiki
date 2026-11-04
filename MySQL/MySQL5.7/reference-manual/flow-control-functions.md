---
title: "12.5 Flow Control Functions"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/flow-control-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

**Table 12.7 Flow Control Operators**

| Name | Description |
| --- | --- |
| `CASE` | Case operator |
| `IF()` | If/else construct |
| `IFNULL()` | Null if/else construct |
| `NULLIF()` | Return NULL if expr1 = expr2 |

- [``CASE           *`value`* WHEN           *`compare_value`* THEN           *`result`* [WHEN           *`compare_value`* THEN           *`result`* ...] [ELSE           *`result`*] END``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/flow-control-functions.html#operator_case)
	[``CASE WHEN           *`condition`* THEN           *`result`* [WHEN           *`condition`* THEN           *`result`* ...] [ELSE           *`result`*] END``](https://docs.oracle.com/cd/E17952_01/mysql-5.7-en/flow-control-functions.html#operator_case)
	The first `CASE` syntax returns the *`result`* for the first ``*`value`*=*`compare_value`*`` comparison that is true. The second syntax returns the result for the first condition that is true. If no comparison or condition is true, the result after `ELSE` is returned, or `NULL` if there is no `ELSE` part.
	Note
	The syntax of the `CASE` *operator* described here differs slightly from that of the SQL [`CASE`](case.md) *statement* described in [Section 13.6.5.1, “CASE Statement”](case.md), for use inside stored programs. The [`CASE`](case.md) statement cannot have an `ELSE NULL` clause, and it is terminated with `END CASE` instead of `END`.
	The return type of a `CASE` expression result is the aggregated type of all result values.
	```
	mysql> SELECT CASE 1 WHEN 1 THEN 'one'
	    ->     WHEN 2 THEN 'two' ELSE 'more' END;
	        -> 'one'
	mysql> SELECT CASE WHEN 1>0 THEN 'true' ELSE 'false' END;
	        -> 'true'
	mysql> SELECT CASE BINARY 'B'
	    ->     WHEN 'a' THEN 1 WHEN 'b' THEN 2 END;
	        -> NULL
	```
- ``IF(*`expr1`*,*`expr2`*,*`expr3`*)``
	If *`expr1`* is `TRUE` (``*`expr1`* <>           0`` and ``*`expr1`* IS           NOT NULL``), `IF()` returns *`expr2`*. Otherwise, it returns *`expr3`*.
	Note
	There is also an [`IF`](if.md) *statement*, which differs from the `IF()` *function* described here. See [Section 13.6.5.2, “IF Statement”](if.md).
	If only one of *`expr2`* or *`expr3`* is explicitly `NULL`, the result type of the `IF()` function is the type of the non- `NULL` expression.
	The default return type of `IF()` (which may matter when it is stored into a temporary table) is calculated as follows:
	- If *`expr2`* or *`expr3`* produce a string, the result is a string.
		If *`expr2`* and *`expr3`* are both strings, the result is case-sensitive if either string is case-sensitive.
	- If *`expr2`* or *`expr3`* produce a floating-point value, the result is a floating-point value.
	- If *`expr2`* or *`expr3`* produce an integer, the result is an integer.
	```
	mysql> SELECT IF(1>2,2,3);
	        -> 3
	mysql> SELECT IF(1<2,'yes','no');
	        -> 'yes'
	mysql> SELECT IF(STRCMP('test','test1'),'no','yes');
	        -> 'no'
	```
- ``IFNULL(*`expr1`*,*`expr2`*)``
	If *`expr1`* is not `NULL`, `IFNULL()` returns *`expr1`*; otherwise it returns *`expr2`*.
	```
	mysql> SELECT IFNULL(1,0);
	        -> 1
	mysql> SELECT IFNULL(NULL,10);
	        -> 10
	mysql> SELECT IFNULL(1/0,10);
	        -> 10
	mysql> SELECT IFNULL(1/0,'yes');
	        -> 'yes'
	```
	The default return type of ``IFNULL(*`expr1`*,*`expr2`*)`` is the more “general” of the two expressions, in the order `STRING`, `REAL`, or `INTEGER`. Consider the case of a table based on expressions or where MySQL must internally store a value returned by `IFNULL()` in a temporary table:
	```
	mysql> CREATE TABLE tmp SELECT IFNULL(1,'test') AS test;
	mysql> DESCRIBE tmp;
	+-------+--------------+------+-----+---------+-------+
	| Field | Type         | Null | Key | Default | Extra |
	+-------+--------------+------+-----+---------+-------+
	| test  | varbinary(4) | NO   |     |         |       |
	+-------+--------------+------+-----+---------+-------+
	```
	In this example, the type of the `test` column is [`VARBINARY(4)`](binary-varbinary.md) (a string type).
- ``NULLIF(*`expr1`*,*`expr2`*)``
	Returns `NULL` if ``*`expr1`* =           *`expr2`*`` is true, otherwise returns *`expr1`*. This is the same as ``CASE WHEN           *`expr1`* =           *`expr2`* THEN NULL ELSE           *`expr1`* END``.
	The return value has the same type as the first argument.
	```
	mysql> SELECT NULLIF(1,1);
	        -> NULL
	mysql> SELECT NULLIF(1,2);
	        -> 1
	```
	Note
	MySQL evaluates *`expr1`* twice if the arguments are not equal.