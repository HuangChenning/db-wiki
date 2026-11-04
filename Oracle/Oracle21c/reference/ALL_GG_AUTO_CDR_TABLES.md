---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_GG_AUTO_CDR_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.199 ALL\_GG\_AUTO\_CDR\_TABLES

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
| `ROW_RESOLUTION_METHOD` <sup>Foot 1</sup> | `VARCHAR2(18)` |  | Indicates which row-level conflict resolution method to use when the old value of the logical change record (LCR) timestamp column is different from the timestamp column value in the table. Possible values:  - `EARLIEST` `TIMESTAMP`: The conflict will be resolved in favor of the LCR when the new value of the LCR timestamp column is less than the timestamp column value in the table - `LATEST` `TIMESTAMP`: The conflict will be resolved in favor of the LCR when the new value of the LCR timestamp column is greater than the timestamp column value in the table |
| `DELETE_ALWAYS_WINS` <sup>Foot 1</sup> | `VARCHAR2(3)` |  | When a conflict occurs between a delete operation and another operation, a `YES` value indicates that the delete operation succeeds and the other operation is discarded, and a `NO` value indicates that there is no special preference for the delete operation |
| `IGNORE_SITE_PRIORITY` <sup>Foot 1</sup> | `VARCHAR2(3)` |  | When a conflict occurs between a target table change and a source table change, and `SITE` `PRIORITY` has been specified, this value indicates whether `SITE` `PRIORITY` should be ignored (`YES`) or not (`NO`) |
| `TOMBSTONE_TABLE` | `VARCHAR2(128)` |  | Tombstone table name (if table has delete tombstoning enabled) |
| `ROW_RESOLUTION_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Name of row-level timestamp column |
| `KEY_VERSION_COLUMN` <sup>Foot 1</sup> | `VARCHAR2(8)` |  | Indicates whether the table contains a hidden column named `KEYVER$$`, which contains a version timestamp  Possible values:  - `KEYVER$$` - The table contains a `KEYVER$$` column - `NONE` - The table does not contain a `KEYVER$$` column |
| `EXISTING_DATA_TIMESTAMP` | `TIMESTAMP(6)` |  | Timestamp to give existing rows when a new timestamp column is added |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

See Also:

" [DBA\_GG\_AUTO\_CDR\_TABLES](DBA_GG_AUTO_CDR_TABLES.md) "