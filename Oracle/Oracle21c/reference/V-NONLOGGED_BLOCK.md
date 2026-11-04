---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-NONLOGGED_BLOCK.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.94 V$NONLOGGED\_BLOCK

`V$NONLOGGED_BLOCK` displays ranges of nonlogged datafile blocks recorded in the control file.

Prior to Oracle Database 12c, the presence of any nonlogged blocks in a data file was recorded in the file header via the `FIRST_NONLOGGED_SCN` column of the `V$DATAFILE` view. Now with 12c, in addition to the file header data, the ranges themselves are recorded in the control file. A control file range is a superset of the actual nonlogged blocks, meaning that small ranges can be merged to form larger ranges, even when there are some valid blocks between the smaller ranges.

The information in the view is maintained by `RMAN VALIDATE`, `RMAN RESTORE`, `RMAN RECOVER`, and Flashback Database and Media Recovery. A non RMAN-based restore will cause the data to become invalid, and it will be purged the next time any of those tasks are invoked and involve the file. As a result of space reuse, it is possible for ranges to no longer contain any nonlogged blocks. An RMAN VALIDATE command can be used to synchronize the ranges with the actual nonlogged blocks found from a scan of the data file.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Absolute file number of the data file that contains the nonlogged blocks |
| `BLOCK#` | `NUMBER` | Block number of the first nonlogged block in the range of nologged blocks |
| `BLOCKS` | `NUMBER` | Number of nonlogged blocks found starting with `BLOCK#` |
| `NONLOGGED_START_CHANGE#` | `NUMBER` | The smallest SCN on which any block in this block range became nonlogged. NULL if unknown. |
| `NONLOGGED_START_TIME` | `DATE` | The time that corresponds to `NONLOGGED_START_CHANGE#`. NULL if unknown. |
| `NONLOGGED_END_CHANGE#` | `NUMBER` | The largest SCN on which any block in this block range became nonlogged. NULL if unknown. |
| `NONLOGGED_END_TIME` | `DATE` | The time that corresponds to `NONLOGGED_END_CHANGE#`. NULL if unknown. |
| `RESETLOGS_CHANGE#` | `NUMBER` | The resetlogs SCN of the incarnation on which this block range was first marked as nonlogged. NULL if unknown. |
| `RESETLOGS_TIME` | `DATE` | The resetlogs time of the incarnation on which this block range was first marked as nologged. NULL if unknown. |
| `OBJECT#` | `VARCHAR2(40)` | The object ID this range belongs to. If this field is NULL, the object number is unknown. |
| `REASON` | `VARCHAR2(9)` | The reason why this block range appears in this list, for example, primary file offline, could not talk to primary, non-standby recovery, and so on. For Oracle Database 12c and later releases, it is always `UNKNOWN`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |