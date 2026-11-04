---
title: "10.15.16 Optimizer Trace Implementation"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/optimizer-trace-implementation.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 10.15.16 Optimizer Trace Implementation

See the files `sql/opt_trace*`, starting with `sql/opt_trace.h`. A trace is started by creating an instance of `Opt_trace_start`; information is added to this trace by creating instances of `Opt_trace_object` and `Opt_trace_array`, and by using the `add()` methods of these classes.