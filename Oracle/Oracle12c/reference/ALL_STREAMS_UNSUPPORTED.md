---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_STREAMS_UNSUPPORTED.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_STREAMS_UNSUPPORTED` displays information about the tables accessible to the current user that are not supported by Streams in this release of the Oracle Database.

Related View

`DBA_STREAMS_UNSUPPORTED` displays information about all tables in the database that are not supported by Streams in this release of the Oracle Database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table |
| `REASON` | `VARCHAR2(39)` |  | Reason why the table is not supported:  - `IOT` - `column with user-defined type` - `unsupported column exists` - `object table` - `AQ queue table` - `temporary table` - `sub object` - `external table` - `materialized view` - `FILE column exists` - `materialized view log` - `materialized view container table` - `streams unsupported object` - `domain index` - `IOT with overflow` - `IOT with LOB` - `IOT with physical Rowid mapping` - `mapping table for physical rowid of IOT` - `IOT with LOB` - `IOT with row movement` - `summary container table` |
| `AUTO_FILTERED` | `VARCHAR2(3)` |  | Indicates whether Streams automatically filters out the object (`YES`) or not (`NO`) |

See Also:

" [DBA\_STREAMS\_UNSUPPORTED](DBA_STREAMS_UNSUPPORTED.md) "