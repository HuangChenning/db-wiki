---
title: "8.15.16 Optimizer Trace Implementation"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/optimizer-trace-implementation.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.15.16 Optimizer Trace Implementation

See the files `sql/opt_trace*`, starting with `sql/opt_trace.h`. A trace is started by creating an instance of `Opt_trace_start`; information is added to this trace by creating instances of `Opt_trace_object` and `Opt_trace_array`, and by using the `add()` methods of these classes.