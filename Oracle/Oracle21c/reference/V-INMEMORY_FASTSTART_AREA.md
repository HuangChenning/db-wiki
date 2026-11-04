---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-INMEMORY_FASTSTART_AREA.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.7 V$INMEMORY\_FASTSTART\_AREA

`V$INMEMORY_FASTSTART_AREA` provides information about the In-Memory FastStart (IM FastStart) area.

| Column | Datatype | Description |
| --- | --- | --- |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `TABLESPACE_NAME` | `VARCHAR2(128)` | IM FastStart tablespace name. When IM FastStart is not enabled, the value of `TABLESPACE_NAME` is `INVALID_TABLESPACE` and the value of `STATUS` is `DISABLE`. |
| `STATUS` | `VARCHAR2(10)` | IM FastStart status. Possible values include:  - `ENABLE`: An IM FastStart tablespace has been specified and the content of the IM column is being periodically checkpointed to disk. - `ENABLING`: An IM FastStart tablespace has been specified and the database is creating the IM FastStart area. - `DISABLE`: An IM FastStart tablespace has not been specified. This is the default. - `MIGRATING`: A user has requested the IM FastStart area be migrated from one tablespace to another. - `DISABLING`: A user has requested IM FastStart to be disabled. |
| `ALLOCATED_SIZE` | `NUMBER` | The allocated size of an IM FastStart tablespace in bytes |
| `USED_SIZE` | `NUMBER` | The currently used size of an IM FastStart area (in bytes) within the tablespace. |
| `LAST_CHECKPOINT_TIME` | `TIMESTAMP(6)` | The time when the last IMCU was checkpointed to the IM FastStart area |
| `LAST_POPULATE_TIME` | `TIMESTAMP(6)` | The time of the last population from the IM FastStart area |
| `NUM_DEFERRED_WRITES` | `NUMBER` | The number of pending deferred writes to the IM FastStart area |