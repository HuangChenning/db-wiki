---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_LOB_TEMPLATES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.262 ALL\_LOB\_TEMPLATES

`ALL_LOB_TEMPLATES` describes the LOB subpartition templates accessible to the current user.

Related Views

- `DBA_LOB_TEMPLATES` describes all LOB subpartition templates in the database.
- `USER_LOB_TEMPLATES` describes the LOB subpartition templates owned by the current user. This view does not display the `USER_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `LOB_COL_NAME` | `VARCHAR2(4000)` |  | Name of the LOB column |
| `SUBPARTITION_NAME` | `VARCHAR2(132)` | `NOT NULL` | Name of the subpartition |
| `LOB_SEGMENT_NAME` | `VARCHAR2(132)` | `NOT NULL` | Name of the LOB segment |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name of the subpartition |

See Also:

- " [DBA\_LOB\_TEMPLATES](DBA_LOB_TEMPLATES.md) "
- " [USER\_LOB\_TEMPLATES](USER_LOB_TEMPLATES.md) "