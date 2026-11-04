---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_GG_AUTO_CDR_TABLES.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_GG_AUTO_CDR_TABLES` provides details about tables configured for Oracle GoldenGate automatic conflict detection and resolution (CDR) that are owned by the current user.

Related View

`DBA_GG_AUTO_CDR_TABLES` provides details about all the tables configured for Oracle GoldenGate automatic conflict detection and resolution (CDR).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Table name |
| `RESOLUTION_GRANULARITY` | `VARCHAR2(6)` |  | Resolution granularity:  - `ROW` - `COLUMN` |
| `FETCHCOLS` | `VARCHAR2(3)` |  | Extract fetchcols configuration:  - `Yes`: Extract will fetch non-scalar data - `No`: Extract will not fetch non-scalar data |
| `RECORD_CONFLICTS` | `VARCHAR2(3)` |  | Monitoring of conflicts: - `Yes`: Conflict info is recorded - `No`: Conflict info is not recorded |
| `USE_CUSTOM_HANDLERS` | `VARCHAR2(4)` |  | Use of customized or automatic conflict handlers:  - `All`: If using custom handlers - `None`: If using automatic handlers |
| `TOMBSTONE_TABLE` | `VARCHAR2(128)` |  | Tombstone table name (if table has delete tombstoning enabled) |
| `ROW_RESOLUTION_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Name of row-level timestamp column |
| `EXISTING_DATA_TIMESTAMP` | `TIMESTAMP(6)` |  | Timestamp to give existing rows when a new timestamp column is added |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_GG\_AUTO\_CDR\_TABLES](DBA_GG_AUTO_CDR_TABLES.md) "