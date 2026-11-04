---
title: ALL_LOB_TEMPLATES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1132.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_LOB_TEMPLATES` describes the LOB subpartition templates accessible to the current user.

Related Views

- `DBA_LOB_TEMPLATES` describes all LOB subpartition templates in the database.
- `USER_LOB_TEMPLATES` describes the LOB subpartition templates owned by the current user. This view does not display the `USER_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the table |
| `LOB_COL_NAME` | `VARCHAR2(4000)` |  | Name of the LOB column |
| `SUBPARTITION_NAME` | `VARCHAR2(34)` | `NOT NULL` | Name of the subpartition |
| `LOB_SEGMENT_NAME` | `VARCHAR2(34)` | `NOT NULL` | Name of the LOB segment |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name of the subpartition |

See Also:

- ["DBA\_LOB\_TEMPLATES"](statviews_4110.md)
- ["USER\_LOB\_TEMPLATES"](statviews_5347.md)