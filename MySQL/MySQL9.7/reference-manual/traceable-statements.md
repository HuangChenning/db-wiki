---
title: "10.15.3 Traceable Statements"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/traceable-statements.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 10.15.3 Traceable Statements

Statements which are traceable are listed here:

Tracing is supported for both `INSERT` and `REPLACE` statements using `VALUES`, `VALUES ROW`, or `SELECT`.

Traces of multi-table `UPDATE` and `DELETE` statements are supported.

Tracing of `SET optimizer_trace` is not supported.

For statements which are prepared and executed in separate steps, preparation and execution are traced separately.