---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LGWRIO_OUTLIER.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.34 V$LGWRIO\_OUTLIER

`V$LGWRIO_OUTLIER` contains entries corresponding to Log Writer (LGWR) process I/Os that have taken a long time (more than 500 ms) to complete. Use this view to see if there any occasional delays in serving disk I/O requests by the storage subsystem.

| Column | Datatype | Description |
| --- | --- | --- |
| `FUNCTION_NAME` | `VARCHAR2(18)` | I/O function name of the delayed I/O |
| `IO_SIZE` | `NUMBER` | Size of the I/O in bytes |
| `WAIT_EVENT` | `VARCHAR2(64)` | Wait event name that was used to track the I/O |
| `FILE_NAME` | `VARCHAR2(513)` | Name of the file to which the I/O was targeted |
| `IO_LATENCY` | `NUMBER` | Time taken to complete the I/O (in milliseconds) |
| `DISK1_NAME` | `VARCHAR2(255)` | For Oracle ASM, the name of the first disk to which the I/O was issued |
| `DISK1_LATENCY` | `NUMBER` | Latency seen on the first disk (in milliseconds) |
| `DISK2_NAME` | `VARCHAR2(255)` | For Oracle ASM, the name of the second disk to which the I/O was issued |
| `DISK2_LATENCY` | `NUMBER` | Latency seen on the second disk (in milliseconds) |
| `DISK3_NAME` | `VARCHAR2(255)` | For Oracle ASM, the name of the third disk to which the I/O was issued |
| `DISK3_LATENCY` | `NUMBER` | Latency seen on the third disk (in milliseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$IO\_OUTLIER](V-IO_OUTLIER.md) "
- " [V$KERNEL\_IO\_OUTLIER](V-KERNEL_IO_OUTLIER.md) "