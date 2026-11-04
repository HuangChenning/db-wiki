---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.1.7 ALTER LIBRARY Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/alter-library.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.1.7 ALTER LIBRARY Statement

```sql
ALTER LIBRARY library_name
    COMMENT "comment_text"
```

This statement adds a comment to the named JavaScript library, or replaces the existing comment if there is one. Following execution of this statement, the updated comment can be viewed in the output of [`SHOW CREATE LIBRARY`](show-create-library.md) and in the `ROUTINE_COMMENT` column of the Information Schema [`LIBRARIES`](information-schema-libraries-table.md) table. The comment text must be quoted.

To remove a comment from a library without replacing it, specify an empty comment string (`COMMENT ""` or `COMMENT ''`).