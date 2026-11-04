---
title: "V$ASM_OPERATION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1031.htm
tags:
  - oracle
  - 11g
  - reference
---

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_OPERATION` displays one row for every active Oracle ASM long running operation executing in the Oracle ASM instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Disk group number (primary key). This is the foreign key to the `V$ASM_DISKGROUP` view. |
| `OPERATION` | `CHAR(5)` | Type of the operation: - `REBAL` - Rebalance pending for this group. The disk group needs rebalance to complete. - `ONLIN` - Online disks operation in progress for the disk group |
| `STATE` | `VARCHAR2(4)` | State of the operation: - `WAIT` - No operations running for the group - `RUN` - Operation running for the group - `REAP` - Operation is being run down - `HALT` - Operation halted by admin - `ERRS` - Operation halted by errors |
| `POWER` | `NUMBER` | Power requested for the operation as specified by the `ASM_POWER_LIMIT` initialization parameter or command syntax |
| `ACTUAL` | `NUMBER` | Power allocated to the operation |
| `SOFAR` | `NUMBER` | Number of Allocation Units that have been moved so far by the operation |
| `EST_WORK` | `NUMBER` | Estimated number of Allocation Units that have to be moved by the operation |
| `EST_RATE` | `NUMBER` | Estimated number of Allocation Units that are being moved per minute by the operation |
| `EST_MINUTES` | `NUMBER` | Estimated amount of time (in minutes) that the remainder of the operation is expected to take |
| `ERROR_CODE` | `VARCHAR2(44)` | Oracle external error code; NULL if no error |