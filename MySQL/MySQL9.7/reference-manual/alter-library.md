---
title: "15.1.7 ALTER LIBRARY Statement"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/alter-library.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 15.1.7 ALTER LIBRARY Statement

```
ALTER LIBRARY library_name 
    COMMENT "comment_text"
```

This statement adds a comment to the named JavaScript library, or replaces the existing comment if there is one. Following execution of this statement, the updated comment can be viewed in the output of [`SHOW CREATE LIBRARY`](show-create-library.md) and in the `ROUTINE_COMMENT` column of the Information Schema [`LIBRARIES`](information-schema-libraries-table.md) table. The comment text must be quoted.

To remove a comment from a library without replacing it, specify an empty comment string (`COMMENT ""` or `COMMENT ''`).