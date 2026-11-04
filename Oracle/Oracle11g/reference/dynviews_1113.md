---
title: "V$DELETED_OBJECT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1113.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DELETED_OBJECT` displays information about deleted archived logs, datafile copies and backup pieces from the control file. The only purpose of this view is to optimize the recovery catalog resync operation. When an archived log, datafile copy, or backup piece is deleted, the corresponding record is marked deleted.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Deleted object record ID |
| `STAMP` | `NUMBER` | Deleted object record stamp |
| `TYPE` | `VARCHAR2(26)` | Identifies the type of deleted object: - `ARCHIVED LOG` - `BACKUP PIECE` - `DATAFILE COPY` - `PROXY COPY` - `BACKUP PIECE AVAILABLE` - `BACKUP PIECE EXPIRED` - `PROXY COPY AVAILABLE` - `PROXY COPY EXPIRED` - `BACKUP PIECE UNAVAILABLE` - `PROXY COPY UNAVAILABLE` - `DATAFILE COPY AVAILABLE` - `DATAFILE COPY EXPIRED` - `DATAFILE COPY UNAVAILABLE` - `ARCHIVED LOG AVAILABLE` - `ARCHIVED LOG EXPIRED` - `ARCHIVED LOG UNAVAILABLE` - `BACKUP SET KEEP OPTIONS` - `BACKUP SET KEEP UNTIL` - `PROXY COPY KEEP OPTIONS` - `PROXY COPY KEEP UNTIL` - `DATAFILE COPY KEEP OPTIONS` - `DATAFILE COPY KEEP UNTIL` - `DATAFILE RENAME ON RESTORE` |
| `OBJECT_RECID` | `NUMBER` | Record ID of the deleted object |
| `OBJECT_STAMP` | `NUMBER` | Record timestamp of the deleted object |
| `OBJECT_DATA` | `NUMBER` | Displays additional internal information related to this deleted object. For internal Oracle use only. |
| `SET_STAMP` | `NUMBER` | Set stamp of the deleted object |
| `SET_COUNT` | `NUMBER` | Set count of the deleted object |