---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-KERNEL_IO_OUTLIER.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.25 V$KERNEL\_IO\_OUTLIER

`V$KERNEL_IO_OUTLIER` contains entries corresponding to I/Os that have taken a long time (more than 500 ms) to complete.

Use this view to see the individual kernel components of I/Os for which there are any occasional delays in serving disk I/O requests by the storage subsystem.

Note:

Although this view exists on all platforms in Oracle Database 12c, it is only populated on the Solaris platform.

| Column | Datatype | Description |
| --- | --- | --- |
| `TIMESTAMP` | `NUMBER` | Number of seconds elapsed since 00:00 UTC, January 1, 1970 |
| `IO_SIZE` | `NUMBER` | Size of the I/O, in KB. |
| `IO_OFFSET` | `NUMBER` | Offset into the device of the I/O |
| `DEVICE_NAME` | `VARCHAR2(513)` | Name of the device to which the I/O was targeted |
| `PROCESS_NAME` | `VARCHAR2(64)` | Name of the process that issued the I/O |
| `TOTAL_LATENCY` | `NUMBER` | Total time the I/O spent in the kernel (in milliseconds) |
| `SETUP_LATENCY` | `NUMBER` | Time spent during initial I/O setup before sending to SCSI target device driver (in milliseconds) |
| `QUEUE_TO_HBA_LATENCY` | `NUMBER` | Time spent in the SCSI target device driver before being sent to the Host Bus Adaptor (in milliseconds) |
| `TRANSFER_LATENCY` | `NUMBER` | Time spent in the Host Bus Adaptor and physically transferring the I/O to the storage device (in milliseconds) |
| `CLEANUP_LATENCY` | `NUMBER` | Time spent freeing resources used by the completed I/O (in milliseconds) |
| `PID` | `NUMBER` | Process ID that issued the I/O |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$IO\_OUTLIER](V-IO_OUTLIER.md) "
- " [V$LGWRIO\_OUTLIER](V-LGWRIO_OUTLIER.md) "