---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_STREAMS_NEWLY_SUPPORTED.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.91 ALL\_STREAMS\_NEWLY\_SUPPORTED

`ALL_STREAMS_NEWLY_SUPPORTED` displays information about the tables accessible to the current user that are newly supported by capture processes.

Related View

`DBA_STREAMS_NEWLY_SUPPORTED` displays information about all tables in the database that are newly supported by capture processes.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `REASON` | `VARCHAR2(39)` |  | Reason why the table was not supported in a previous release:  - `IOT` - `column with user-defined type` - `unsupported column exists` - `object table` - `AQ queue table` - `temporary table` - `sub object` - `external table` - `materialized view` - `FILE column exists` - `materialized view log` - `materialized view container table` - `streams unsupported object` - `domain index` |
| `COMPATIBLE` | `CHAR(4)` |  | Minimum database compatibility for capture processes to support the database object |

See Also:

" [DBA\_STREAMS\_NEWLY\_SUPPORTED](DBA_STREAMS_NEWLY_SUPPORTED.md) "