---
title: "MySQL :: MySQL 26.10 Reference Manual :: 27.3 JavaScript Stored Programs"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/stored-routines-js.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 27.3 JavaScript Stored Programs

MySQL 26.10 supports stored routines written in JavaScript, as in the simple example shown here:

```sql
mysql> CREATE FUNCTION add_nos(arg1 INT, arg2 INT) 
    ->   RETURNS INT LANGUAGE JAVASCRIPT AS 
    ->   $$
    $>     return arg1 + arg2
    $>   $$
    ->   ;
Query OK, 0 rows affected (0.01 sec)

mysql> SELECT add_nos(12,52);
+----------------+
| add_nos(12,52) |
+----------------+
|             64 |
+----------------+
1 row in set (0.00 sec)
```

Note

Support for JavaScript stored routines requires installation of the Multilingual Engine (MLE) component. For information about installing and configuring the MLE component, see [Section 7.5.7, “Multilingual Engine Component (MLE)”](mle-component.md).

JavaScript stored programs can be used together with other user-created and MySQL-native stored programs (subject to limitations described elsewhere in this section), as well as with MySQL system and user variables. We can see some of this here, using the `add_nos()` function created in the previous example:

```sql
mysql> SET @x = 2;
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT @x;
+------+
| @x   |
+------+
|    2 |
+------+
1 row in set (0.00 sec)

mysql> SELECT @@server_id;
+-------------+
| @@server_id |
+-------------+
|           1 |
+-------------+
1 row in set (0.00 sec)

mysql> SELECT add_nos(POW(2,@x), 1);
+-----------------------+
| add_nos(POW(2,@x), 1) |
+-----------------------+
|                     5 |
+-----------------------+
1 row in set (0.01 sec)

mysql> SELECT POW(add_nos(@x, @@server_id), add_nos(@x, 1));
+-----------------------------------------------+
| POW(add_nos(@x, @@server_id), add_nos(@x, 1)) |
+-----------------------------------------------+
|                                            27 |
+-----------------------------------------------+
1 row in set (0.01 sec)
```

JavaScript stored procedures can be invoked using [`CALL`](call.md), as with SQL stored procedures.

JavaScript stored programs can also take column values as arguments. JavaScript stored functions can be invoked anywhere in an SQL expression that it is legal to use any other function, such as in `WHERE`, `HAVING`, `ORDER     BY`, and `JOIN` clauses. They can also be invoked within the body of a trigger or event definition, although the definitions themselves must be written in SQL. Examples of some of these features can be found later in this section (see [Section 27.3.12, “JavaScript Stored Program Examples”](srjs-examples.md)).