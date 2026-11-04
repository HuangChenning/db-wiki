---
title: "10.15.14 Preventing the Use of Optimizer Trace"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/preventing-use-of-optimizer-trace.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 10.15.14 Preventing the Use of Optimizer Trace

If, for some reason, you wish to prevent users from seeing traces of their queries, start the server with the options shown here:

```
--maximum-optimizer-trace-max-mem-size=0 --optimizer-trace-max-mem-size=0
```

This sets the maximum size to 0 and prevents users from changing this limit, thus truncating all traces to 0 bytes.