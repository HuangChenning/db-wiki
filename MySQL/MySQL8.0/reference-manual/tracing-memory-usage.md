---
title: "10.15.5 Tracing Memory Usage"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/tracing-memory-usage.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 10.15.5 Tracing Memory Usage

Each stored trace is a string, which is extended (using `realloc()`) as optimization progresses by appending more data to it. The [`optimizer_trace_max_mem_size`](server-system-variables.md) server system variable sets a limit on the total amount of memory used by all traces currently being stored. If this limit is reached, the current trace is not extended, which means the trace is incomplete; in this case the `MISSING_BYTES_BEYOND_MAX_MEM_SIZE` column shows the number of bytes missing from the trace.