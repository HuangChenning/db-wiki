---
title: "MySQL :: MySQL 26.7 Reference Manual :: 12.3.10 Compatibility with Other DBMSs"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/charset-compatibility.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 12.3.10 Compatibility with Other DBMSs

For MaxDB compatibility these two statements are the same:

```sql
CREATE TABLE t1 (f1 CHAR(N) UNICODE);
CREATE TABLE t1 (f1 CHAR(N) CHARACTER SET ucs2);
```

Both the `UNICODE` attribute and the `ucs2` character set are deprecated; you should expect them to be removed in a future version of MySQL.