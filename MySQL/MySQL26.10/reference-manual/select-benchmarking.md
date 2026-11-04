---
title: "MySQL :: MySQL 26.10 Reference Manual :: 10.13.1 Measuring the Speed of Expressions and Functions"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/select-benchmarking.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 10.13.1 Measuring the Speed of Expressions and Functions

To measure the speed of a specific MySQL expression or function, invoke the [`BENCHMARK()`](information-functions.md) function using the [**mysql**](mysql.md) client program. Its syntax is [``BENCHMARK(*`loop_count`*,*`expr`*)``](information-functions.md). The return value is always zero, but [**mysql**](mysql.md) prints a line displaying approximately how long the statement took to execute. For example:

```sql
mysql> SELECT BENCHMARK(1000000,1+1);
+------------------------+
| BENCHMARK(1000000,1+1) |
+------------------------+
|                      0 |
+------------------------+
1 row in set (0.32 sec)
```

This result was obtained on a Pentium II 400MHz system. It shows that MySQL can execute 1,000,000 simple addition expressions in 0.32 seconds on that system.

The built-in MySQL functions are typically highly optimized, but there may be some exceptions. [`BENCHMARK()`](information-functions.md) is an excellent tool for finding out if some function is a problem for your queries.