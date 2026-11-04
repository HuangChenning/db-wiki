---
title: "15.1.32 DROP LIBRARY Statement"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/drop-library.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 15.1.32 DROP LIBRARY Statement

```
DROP LIBRARY [IF EXISTS] [database.]library
```

Drops the named JavaScript library. An optional database name may be specified; otherwise, the current database is assumed.

To execute this statement, the user must have the [`ALTER ROUTINE`](privileges-provided.md) privilege. A library created by a user with the [`SYSTEM_USER`](privileges-provided.md) privilege can be dropped only by a user having the same privilege.

See [Section 27.3.8, “Using JavaScript Libraries”](srjs-libraries.md), for more information and examples.