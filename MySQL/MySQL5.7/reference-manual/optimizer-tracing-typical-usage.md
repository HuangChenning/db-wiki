---
title: "8.15.1 Typical Usage"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/optimizer-tracing-typical-usage.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 8.15.1 Typical Usage

To perform optimizer tracing entails the following steps:

1. Enable tracing by executing [`SET`](set-variable.md) [`optimizer_trace="enabled=ON"`](server-system-variables.md).
2. Execute the statement to be traced. See [Section 8.15.3, “Traceable Statements”](traceable-statements.md), for a listing of statements which can be traced.
3. Examine the contents of the [`INFORMATION_SCHEMA.OPTIMIZER_TRACE`](information-schema-optimizer-trace-table.md) table.
4. To examine traces for multiple queries, repeat the previous two steps as needed.
5. To disable tracing after you have finished, execute `SET optimizer_trace="enabled=OFF"`.

You can trace only statements which are executed within the current session; you cannot see traces from other sessions.