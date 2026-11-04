---
title: "MySQL :: MySQL 26.7 Reference Manual :: 10.15.3 Traceable Statements"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/traceable-statements.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 10.15.3 Traceable Statements

Statements which are traceable are listed here:

Tracing is supported for both `INSERT` and `REPLACE` statements using `VALUES`, `VALUES ROW`, or `SELECT`.

Traces of multi-table `UPDATE` and `DELETE` statements are supported.

Tracing of `SET optimizer_trace` is not supported.

For statements which are prepared and executed in separate steps, preparation and execution are traced separately.