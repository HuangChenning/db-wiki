---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_ANNOTATION_VALUES.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.51 ALL\_ANNOTATION\_VALUES

`ALL_ANNOTATION_VALUES` displays the values for schema annotations accessible to the current user.

Related Views

- `DBA_ANNOTATION_VALUES` displays the values for all schema annotations in the database.
- `USER_ANNOTATION_VALUES` displays the values for schema annotations owned by the current user. This view does not display the `ANNOTATION_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ANNOTATION_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Annotation owner |
| `ANNOTATION_NAME` | `VARCHAR2(1024)` | `NOT NULL` | Annotation name |
| `ANNOTATION_VALUE` | `VARCHAR2(4000)` |  | Annotation value |

Note:

This view is available starting with Oracle Database 19c, Release Update 19.28.

See Also:

- " [DBA\_ANNOTATION\_VALUES](DBA_ANNOTATION_VALUES.md) "
- " [USER\_ANNOTATION\_VALUES](USER_ANNOTATION_VALUES.md) "