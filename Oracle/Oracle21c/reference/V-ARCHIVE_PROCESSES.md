---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ARCHIVE_PROCESSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.40 V$ARCHIVE\_PROCESSES

`V$ARCHIVE_PROCESSES` displays the state of the various ARCH processes for the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `PROCESS` | `NUMBER` | Identifier for the ARCH process for the instance, numbered from 0-9 |
| `STATUS` | `VARCHAR2(10)` | Status of the ARCH process, displayed as a keyword. Possible values are: `STOPPED`, `SCHEDULED`, `STARTING`, `ACTIVE`, `STOPPING`, and `TERMINATED`. |
| `LOG_SEQUENCE` | `NUMBER` | This is the online redo log sequence number currently being archived, if `STATE` =" `BUSY` " |
| `STATE` | `VARCHAR2(4)` | This is the current state of the ARCH process, displayed as a keyword. Possible keywords are `IDLE` or `BUSY`. |
| `ROLES` | `VARCHAR2(36)` | The list of roles assigned to the archive process. The roles include: `HEART_BEAT`, `NO_FAL`, `NO_SRL`, `CLEAR_LOGS` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |