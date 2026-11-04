---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_OPERATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.67 V$ASM\_OPERATION

In an Oracle Automatic Storage Management (Oracle ASM) instance, `V$ASM_OPERATION` displays one row for every active Oracle ASM long running operation executing in the Oracle ASM instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Disk group number (primary key). This is the foreign key to the `V$ASM_DISKGROUP` view. |
| `OPERATION` | `CHAR(5)` | Type of the operation:  - `REBAL` - Rebalance pending for this group. The disk group is rebalancing. - `REMIRROR` - Remirror is pending for this group. - `SCRUB` - Scrubbing is pending for this group.  Starting with Oracle Database 12c, new queries should use the `PASS` column instead of this column. |
| `PASS` | `VARCHAR2(9)` | Type of the operation:  - `COMPACT` - Oracle ASM is moving user data closer together, which improves performance by reducing seek distance - `PREPARE` - Completing work corresponding to the prepare SQL operation. This phase is enabled only for `FLEX` or `EXTENDED` redundancy disk groups and `COMPATIBLE.ASM` must be set to `12.2` or higher. - `REBALANCE` - Rebalance pending for this group. The disk group is rebalancing. - `REBUILD` - Restoring the redundancy of forcing disks. Forcing disks are those disks that have been dropped with the `FORCE` option. - `RESILVER` - This value appears in Oracle Exadata environments when WriteBack FlashCache is enabled - `RESYNC` - Resync operation in progress to bring one or more Oracle ASM disks online - `SCRUBBING` - The disk group is scrubbing.  Starting with Oracle Database 12c, new queries should use this column instead of the `OPERATION` column. |
| `STATE` | `VARCHAR2(4)` | State of the operation:  - `WAIT` - No operations running for the group - `EST` - An estimate is computed on the amount of work to be done for the rebalance - `RUN` - Operation running for the group - `REAP` - Operation is being run down - `DONE` - Displayed for a pass that is complete - `ERRS` - Operation halted by errors  Estimates are computed in parallel in the background while the work is being executed. Thus, the transition from the `EST` to the `RUN` state may be extremely fast. |
| `POWER` | `NUMBER` | Power requested for the operation as specified by the ASM\_POWER\_LIMIT initialization parameter or command syntax. Or, power requested for the operation as specified by the power option of the scrubbing SQL syntax. |
| `ACTUAL` | `NUMBER` | Power allocated to the operation |
| `SOFAR` | `NUMBER` | Number of Allocation Units that are being moved per minute by the operation. Or, the number of Allocation Units that have been scrubbed so far. |
| `EST_WORK` | `NUMBER` | Estimated number of Allocation Units that have to be moved by the operation. Or, the estimated number of Allocation Units that have to be scrubbed by the scrubbing operation. |
| `EST_RATE` | `NUMBER` | Estimated number of Allocation Units that are being moved per minute by the operation |
| `EST_MINUTES` | `NUMBER` | Estimated amount of time (in minutes) that the remainder of the operation is expected to take |
| `ERROR_CODE` | `VARCHAR2(44)` | Oracle external error code; NULL if no error |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information