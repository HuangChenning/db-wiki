---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CAPTURE_EXTRA_ATTRIBUTES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_CAPTURE_EXTRA_ATTRIBUTES` displays information about the extra attributes for the capture processes accessible to the current user.

Related View

`DBA_CAPTURE_EXTRA_ATTRIBUTES` displays information about the extra attributes for all capture processes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAPTURE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the capture process |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the extra attribute |
| `INCLUDE` | `VARCHAR2(3)` |  | Indicates whether the extra attribute is included (`YES`) or not (`NO`) |
| `ROW_ATTRIBUTE` | `VARCHAR2(3)` |  | Indicates whether the extra attribute is a row LCR attribute (`YES`) or not (`NO`) |
| `DDL_ATTRIBUTE` | `VARCHAR2(3)` |  | Indicates whether the extra attribute is a DDL LCR attribute (`YES`) or not (`NO`) |

See Also:

" [DBA\_CAPTURE\_EXTRA\_ATTRIBUTES](DBA_CAPTURE_EXTRA_ATTRIBUTES.md) "