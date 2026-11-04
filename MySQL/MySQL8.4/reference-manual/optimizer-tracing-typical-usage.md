---
title: "10.15.1 Typical Usage"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/optimizer-tracing-typical-usage.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 10.15.1 Typical Usage

To perform optimizer tracing entails the following steps:

1. Enable tracing by executing [`SET`](set-variable.md) [`optimizer_trace="enabled=ON"`](server-system-variables.md).
2. Execute the statement to be traced. See [Section 10.15.3, “Traceable Statements”](traceable-statements.md), for a listing of statements which can be traced.
3. Examine the contents of the [`INFORMATION_SCHEMA.OPTIMIZER_TRACE`](information-schema-optimizer-trace-table.md) table.
4. To examine traces for multiple queries, repeat the previous two steps as needed.
5. To disable tracing after you have finished, execute `SET optimizer_trace="enabled=OFF"`.

You can trace only statements which are executed within the current session; you cannot see traces from other sessions.