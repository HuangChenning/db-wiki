---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_NONLOGGED.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.96 V$BACKUP\_NONLOGGED

`V$BACKUP_NONLOGGED` displays information about nonlogged block ranges in data file backups, recorded in the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Nologged backup record ID |
| `STAMP` | `NUMBER` | Nonlogged backup record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp |
| `SET_COUNT` | `NUMBER` | Backup set count |
| `PIECE#` | `NUMBER` | Backup piece that contains the range of nonlogged blocks |
| `FILE#` | `NUMBER` | Absolute file number of the data file that contains this range of nonlogged blocks |
| `BLOCK#` | `NUMBER` | Block number of the first nonlogged block in the range of nologged blocks |
| `BLOCKS` | `NUMBER` | Number of nonlogged blocks found starting with `BLOCK#` |
| `NONLOGGED_CHANGE#` | `NUMBER` | The smallest SCN on which any block in this block range became nonlogged. NULL if unknown. |
| `NONLOGGED_TIME` | `VARCHAR2` | The time that corresponds to `NONLOGGED_CHANGE#`. NULL if unknown. |
| `RESETLOGS_CHANGE#` | `VARCHAR2` | The resetlogs SCN of the incarnation on which this block range was first marked as nonlogged. NULL if unknown. |
| `RESETLOGS_TIME` | `VARCHAR2` | The resetlogs time of the incarnation on which this block range was first marked as nologged. NULL if unknown. |
| `OBJECT#` | `VARCHAR2` | The object ID this range belongs to. If this field is NULL, the object number is unknown. |
| `REASON` | `CHAR(7)` | The reason why this block range appears in this list, for example, primary file offline, could not talk to primary, non-standby recovery, and so on. For Oracle Database 12c and later releases, it is always `UNKNOWN`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |