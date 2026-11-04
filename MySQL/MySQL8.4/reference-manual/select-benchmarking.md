---
title: "10.13.1 Measuring the Speed of Expressions and Functions"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/select-benchmarking.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 10.13.1 Measuring the Speed of Expressions and Functions

To measure the speed of a specific MySQL expression or function, invoke the [`BENCHMARK()`](information-functions.md) function using the [**mysql**](mysql.md) client program. Its syntax is [``BENCHMARK(*`loop_count`*,*`expr`*)``](information-functions.md). The return value is always zero, but [**mysql**](mysql.md) prints a line displaying approximately how long the statement took to execute. For example:

```
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