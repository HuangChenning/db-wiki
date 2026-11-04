---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SUBPARTITION_TEMPLATES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.98 ALL\_SUBPARTITION\_TEMPLATES

`ALL_SUBPARTITION_TEMPLATES` describes the subpartition templates accessible to the current user.

Related Views

- `DBA_SUBPARTITION_TEMPLATES` describes all subpartition templates in the database.
- `USER_SUBPARTITION_TEMPLATES` describes the subpartition templates owned by the current user. This view does not display the `USER_NAME` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `USER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table |
| `SUBPARTITION_NAME` | `VARCHAR2(132)` | `NOT NULL` | Name of the subpartition |
| `SUBPARTITION_POSITION` | `NUMBER` |  | Position of the subpartition |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace name of the subpartition |
| `HIGH_BOUND` | `LONG` |  | Literal list values of the subpartition |
| `COMPRESSION` | `VARCHAR2(4)` |  | Compression values of `COMPRESSION` or `NOCOMPRESSION` can be specified in a subpartition template.  The value in this column indicates whether the subpartition template specifies that for each new added composite partition, its subpartition data will be stored in compressed format (`YES`) or not (`NO`).  If compression is not specified in the subpartition template, then the default is that data stored in newly-added subpartitions will not be stored in compressed format (`NO`). |
| `INDEXING` | `VARCHAR2(4)` |  | Indexing values of `INDEXING ON` or `INDEXING OFF` can be specified in a subpartition template.  The value in this column indicates whether the subpartition template specifies that for each new added composite partition, its subpartition data will be considered for a partial index (`ON`) or not (`OFF`).  If indexing is not specified in the subpartition template, then the default is that data stored in newly-added subpartitions will considered for a partial index (`ON`). |
| `READ_ONLY` | `VARCHAR2(4)` |  | Values of `READ ONLY` or `READ WRITE` can be specified in a subpartition template.  The value in this column indicates whether the subpartition template specifies that for each new added composite partition, its subpartition data will be read only (`YES`) or not (`NO`).  If the read clause is not specified in the subpartition template, then the default is that data stored in newly-added subpartitions will be read/write (`NO`). |

See Also:

- " [DBA\_SUBPARTITION\_TEMPLATES](DBA_SUBPARTITION_TEMPLATES.md) "
- " [USER\_SUBPARTITION\_TEMPLATES](USER_SUBPARTITION_TEMPLATES.md) "