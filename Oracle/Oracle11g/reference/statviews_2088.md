---
title: ALL_STREAMS_UNSUPPORTED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2088.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_STREAMS_UNSUPPORTED` displays information about the tables accessible to the current user that are not supported by Streams in this release of the Oracle Database.

Related View

`DBA_STREAMS_UNSUPPORTED` displays information about all tables in the database that are not supported by Streams in this release of the Oracle Database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the table |
| `REASON` | `VARCHAR2(39)` |  | Reason why the table is not supported: - `IOT` - `column with user-defined type` - `unsupported column exists` - `object table` - `AQ queue table` - `temporary table` - `sub object` - `external table` - `materialized view` - `FILE column exists` - `materialized view log` - `materialized view container table` - `streams unsupported object` - `domain index` - `IOT with overflow` - `IOT with LOB` - `IOT with physical Rowid mapping` - `mapping table for physical rowid of IOT` - `IOT with LOB` - `IOT with row movement` - `summary container table` |
| `AUTO_FILTERED` | `VARCHAR2(3)` |  | Indicates whether Streams automatically filters out the object (`YES`) or not (`NO`) |

See Also:

["DBA\_STREAMS\_UNSUPPORTED"](statviews_5028.md)