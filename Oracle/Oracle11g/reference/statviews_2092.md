---
title: ALL_SUBPARTITION_TEMPLATES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2092.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SUBPARTITION_TEMPLATES` describes the subpartition templates accessible to the current user.

Related Views

- `DBA_SUBPARTITION_TEMPLATES` describes all subpartition templates in the database.
- `USER_SUBPARTITION_TEMPLATES` describes the subpartition templates owned by the current user. This view does not display the `USER_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `SUBPARTITION_NAME` | `VARCHAR2(34)` | `NOT NULL` | Name of the subpartition |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of the subpartition |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name of the subpartition |
| `HIGH_BOUND` | `LONG` |  | Literal list values of the subpartition |

See Also:

- ["DBA\_SUBPARTITION\_TEMPLATES"](statviews_5032.md)
- ["USER\_SUBPARTITION\_TEMPLATES"](statviews_5467.md)