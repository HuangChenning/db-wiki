---
title: DBA_HIST_FILEMETRIC_HISTORY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3224.htm
tags:
  - oracle
  - 11g
  - reference
---

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