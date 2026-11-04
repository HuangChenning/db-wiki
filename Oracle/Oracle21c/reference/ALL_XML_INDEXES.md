---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_INDEXES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.143 ALL\_XML\_INDEXES

`ALL_XML_INDEXES` describes the XML indexes accessible to the current user.

Related Views

- `DBA_XML_INDEXES` describes all XML indexes in the database.
- `USER_XML_INDEXES` describes the XML indexes owned by the current user. This view does not display the `INDEX_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the XML index |
| `INDEX_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the XML index |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the indexed object |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the indexed object |
| `TYPE` | `VARCHAR2(10)` |  | Type of the indexed column:  - `REPOSITORY` - `BINARY` - `CLOB in OR` - `CLOB` |
| `INDEX_TYPE` | `VARCHAR2(27)` |  | Type of the index:  - `STRUCTURED` - `STRUCTURED and UNSTRUCTURED` - `UNSTRUCTURED` |
| `PATH_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the path table |
| `PARAMETERS` | `XMLTYPE` |  | Indexed paths and Scheduler job information |
| `ASYNC` | `VARCHAR2(9)` |  | Asynchronous index type:  - `ON-COMMIT` - `MANUAL` - `EVERY` - `ALWAYS` |
| `STALE` | `VARCHAR2(5)` |  | Indicates whether the index type is stale (`TRUE`) or not (`FALSE`) |
| `PEND_TABLE_NAME` | `VARCHAR2(128)` |  | Name of the pending table |
| `EX_OR_INCLUDE` | `VARCHAR2(8)` |  | Path subsetting:  - `INCLUDE` - `EXCLUDE` - `FULLY IX` |

See Also:

- " [DBA\_XML\_INDEXES](DBA_XML_INDEXES.md) "
- " [USER\_XML\_INDEXES](USER_XML_INDEXES.md) "