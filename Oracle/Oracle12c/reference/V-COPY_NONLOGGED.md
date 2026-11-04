---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-COPY_NONLOGGED.html
tags:
  - oracle
  - 12c
  - reference
---

`V$COPY_NONLOGGED` displays information about nonlogged block ranges in data file copy blocks recorded in the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | Instance ID |
| `RECID` | `NUMBER` | Nonlogged copy record ID |
| `STAMP` | `NUMBER` | Nonlogged copy record stamp |
| `COPY_RECID` | `NUMBER` | Data file copy record ID |
| `COPY_STAMP` | `NUMBER` | Data file copy record stamp |
| `FILE#` | `NUMBER` | Absolute file number of the data file that contains this range of nonlogged blocks |
| `BLOCK#` | `NUMBER` | Block number of the first nonlogged block in the range of nologged blocks |
| `BLOCKS` | `NUMBER` | Number of nonlogged blocks found starting with `BLOCK#` |
| `NONLOGGED_CHANGE#` | `NUMBER` | The smallest SCN on which any block in this block range became nonlogged. NULL if unknown. |
| `NONLOGGED_TIME` | `VARCHAR2` | The time that corresponds to `NONLOGGED_CHANGE#`. NULL if unknown. |
| `RESETLOGS_CHANGE#` | `VARCHAR2` | The resetlogs SCN of the incarnation on which this block range was first marked as nonlogged. NULL if unknown. |
| `RESETLOGS_TIME` | `VARCHAR2` | The resetlogs time of the incarnation on which this block range was first marked as nologged. NULL if unknown. |
| `OBJECT#` | `VARCHAR2` | The object ID this range belongs to. If this field is NULL, the object number is unknown. |
| `REASON` | `CHAR(7)` | The reason why this block range appears in this list. For Oracle Database 12c, it is always `UNKNOWN`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |