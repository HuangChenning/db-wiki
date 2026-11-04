---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_CLU_COLUMNS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_CLU_COLUMNS` maps all table columns to related cluster columns.

Related View

`USER_CLU_COLUMNS` maps all table columns owned by the current user to related cluster columns. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER ` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cluster |
| `CLUSTER_NAME ` | `VARCHAR2(128)` | `NOT NULL` | Name of the cluster |
| `CLU_COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Key column in the cluster |
| `TABLE_NAME ` | `VARCHAR2(128)` | `NOT NULL` | Clustered table name |
| `TAB_COLUMN_NAME` | `VARCHAR2(4000)` |  | Key column or attribute of the object type column |

See Also:

" [USER\_CLU\_COLUMNS](USER_CLU_COLUMNS.md) "