---
title: ALL_XML_INDEXES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2136.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XML_INDEXES` describes the XML indexes accessible to the current user.

Related Views

- `DBA_XML_INDEXES` describes all XML indexes in the database.
- `USER_XML_INDEXES` describes the XML indexes owned by the current user. This view does not display the `INDEX_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the XML index |
| `INDEX_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the XML index |
| `TABLE_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the indexed object |
| `TABLE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the indexed object |
| `TYPE` | `VARCHAR2(10)` |  | Type of the indexed column: - `REPOSITORY` - `BINARY` - `CLOB in OR` - `CLOB` |
| `INDEX_TYPE` | `VARCHAR2(27)` |  | Type of the index: - `STRUCTURED` - `STRUCTURED and UNSTRUCTURED` - `UNSTRUCTURED` |
| `PATH_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the path table |
| `PARAMETERS` | `XMLTYPE` |  | Indexed paths and Scheduler job information |
| `ASYNC` | `VARCHAR2(9)` |  | Asynchronous index type: |
| `STALE` | `VARCHAR2(5)` |  | Indicates whether the index type is stale (`TRUE`) or not (`FALSE`) |
| `PEND_TABLE_NAME` | `VARCHAR2(30)` |  | Name of the pending table |
| `EX_OR_INCLUDE` | `VARCHAR2(8)` |  | Path subsetting: |

See Also:

- ["DBA\_XML\_INDEXES"](statviews_5100.md)
- ["USER\_XML\_INDEXES"](statviews_5512.md)