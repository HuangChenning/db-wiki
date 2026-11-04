---
title: "MySQL :: MySQL 26.10 Reference Manual :: 10.15.14 Preventing the Use of Optimizer Trace"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/preventing-use-of-optimizer-trace.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 10.15.14 Preventing the Use of Optimizer Trace

If, for some reason, you wish to prevent users from seeing traces of their queries, start the server with the options shown here:

```svg
--maximum-optimizer-trace-max-mem-size=0 --optimizer-trace-max-mem-size=0
```

This sets the maximum size to 0 and prevents users from changing this limit, thus truncating all traces to 0 bytes.