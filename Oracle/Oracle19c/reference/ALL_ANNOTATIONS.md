---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_ANNOTATIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.52 ALL\_ANNOTATIONS

`ALL_ANNOTATIONS` displays schema annotations accessible to the current user.

Related Views

- `DBA_ANNOTATIONS` displays all schema annotations in the database.
- `USER_ANNOTATIONS` displays schema annotations owned by the current user. This view does not display the `ANNOTATION_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ANNOTATION_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Annotation owner |
| `ANNOTATION_NAME` | `VARCHAR2(1024)` | `NOT NULL` | Annotation name |

Note:

This view is available starting with Oracle Database 19c, Release Update 19.28.

See Also:

- " [DBA\_ANNOTATIONS](DBA_ANNOTATIONS.md) "
- " [USER\_ANNOTATIONS](USER_ANNOTATIONS.md) "