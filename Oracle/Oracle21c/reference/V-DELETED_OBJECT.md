---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DELETED_OBJECT.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.171 V$DELETED\_OBJECT

`V$DELETED_OBJECT` displays information about deleted archived logs, data file copies and backup pieces from the control file.

The only purpose of this view is to optimize the recovery catalog resync operation. When an archived log, data file copy, or backup piece is deleted, the corresponding record is marked deleted.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Deleted object record ID |
| `STAMP` | `NUMBER` | Deleted object record stamp |
| `TYPE` | `VARCHAR2(26)` | Identifies the type of deleted object:  - `ARCHIVED LOG` - `BACKUP PIECE` - `DATAFILE COPY` - `PROXY COPY` - `BACKUP PIECE AVAILABLE` - `BACKUP PIECE EXPIRED` - `PROXY COPY AVAILABLE` - `PROXY COPY EXPIRED` - `BACKUP PIECE UNAVAILABLE` - `PROXY COPY UNAVAILABLE` - `DATAFILE COPY AVAILABLE` - `DATAFILE COPY EXPIRED` - `DATAFILE COPY UNAVAILABLE` - `ARCHIVED LOG AVAILABLE` - `ARCHIVED LOG EXPIRED` - `ARCHIVED LOG UNAVAILABLE` - `BACKUP SET KEEP OPTIONS` - `BACKUP SET KEEP UNTIL` - `PROXY COPY KEEP OPTIONS` - `PROXY COPY KEEP UNTIL` - `DATAFILE COPY KEEP OPTIONS` - `DATAFILE COPY KEEP UNTIL` - `DATAFILE RENAME ON RESTORE` |
| `OBJECT_RECID` | `NUMBER` | Record ID of the deleted object |
| `OBJECT_STAMP` | `NUMBER` | Record timestamp of the deleted object |
| `OBJECT_DATA` | `NUMBER` | Displays additional internal information related to this deleted object. For internal Oracle use only. |
| `SET_STAMP` | `NUMBER` | Set stamp of the deleted object |
| `SET_COUNT` | `NUMBER` | Set count of the deleted object |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |