---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IOFUNCMETRIC.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.14 V$IOFUNCMETRIC

`V$IOFUNCMETRIC` displays I/O statistics information by database function for the most recent time interval period.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time of the interval |
| `END_TIME` | `DATE` | End time of the interval |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `FUNCTION_ID` | `NUMBER` | Function ID |
| `FUNCTION_NAME` | `VARCHAR2(18)` | Function name |
| `SMALL_READ_MBPS` | `NUMBER` | Single block megabytes read per second |
| `SMALL_WRITE_MBPS` | `NUMBER` | Single block megabytes written per second |
| `LARGE_READ_MBPS` | `NUMBER` | Multiblock megabytes read per second |
| `LARGE_WRITE_MBPS` | `NUMBER` | Multiblock megabytes written per second |
| `SMALL_READ_IOPS` | `NUMBER` | Single block read requests per second |
| `SMALL_WRITE_IOPS` | `NUMBER` | Single block write requests per second |
| `LARGE_READ_IOPS` | `NUMBER` | Multiblock read requests per second |
| `LARGE_WRITE_IOPS` | `NUMBER` | Multiblock write requests per second |
| `AVG_WAIT_TIME` | `NUMBER` | Average wait time (in milliseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |