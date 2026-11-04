---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_FILEMETRIC_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.404 DBA\_HIST\_FILEMETRIC\_HISTORY

`DBA_HIST_FILEMETRIC_HISTORY` displays the history of file metrics collected in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `FILEID` | `NUMBER` | `NOT NULL` | File number |
| `CREATIONTIME` | `NUMBER` | `NOT NULL` | File creation time |
| `BEGIN_TIME` | `DATE` | `NOT NULL` | Begin time of the interval |
| `END_TIME` | `DATE` | `NOT NULL` | End time of the interval |
| `INTSIZE` | `NUMBER` | `NOT NULL` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | `NOT NULL` | ID of the group to which the file belongs |
| `AVGREADTIME` | `NUMBER` | `NOT NULL` | Average file read time |
| `AVGWRITETIME` | `NUMBER` | `NOT NULL` | Average file write time |
| `PHYSICALREAD` | `NUMBER` | `NOT NULL` | Number of physical reads |
| `PHYSICALWRITE` | `NUMBER` | `NOT NULL` | Number of physical writes |
| `PHYBLKREAD` | `NUMBER` | `NOT NULL` | Number of physical block reads |
| `PHYBLKWRITE` | `NUMBER` | `NOT NULL` | Number of physical block writes |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |