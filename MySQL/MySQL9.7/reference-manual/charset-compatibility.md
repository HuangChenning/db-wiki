---
title: "12.3.10 Compatibility with Other DBMSs"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/charset-compatibility.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 12.3.10 Compatibility with Other DBMSs

For MaxDB compatibility these two statements are the same:

```
CREATE TABLE t1 (f1 CHAR(N) UNICODE);
CREATE TABLE t1 (f1 CHAR(N) CHARACTER SET ucs2);
```

Both the `UNICODE` attribute and the `ucs2` character set are deprecated; you should expect them to be removed in a future version of MySQL.