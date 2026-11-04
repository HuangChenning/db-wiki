---
title: "10.15.8 The optimizer_trace System Variable"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/optimizer-trace-system-variable.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 10.15.8 The optimizer\_trace System Variable

The optimizer\_trace system variable has these on/off switches:

- `enabled`: Enables (`ON`) or disables (`OFF`) tracing
- `one_line`: If set to `ON`, the trace contains no whitespace, thus conserving space. This renders the trace difficult to read for humans, still usable by JSON parsers, since they ignore whitespace.