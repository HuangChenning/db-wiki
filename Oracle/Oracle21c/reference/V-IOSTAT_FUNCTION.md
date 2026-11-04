---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IOSTAT_FUNCTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.19 V$IOSTAT\_FUNCTION

`V$IOSTAT_FUNCTION` displays disk I/O statistics for database functions (such as the LGWR and DBWR).

| Column | Datatype | Description |
| --- | --- | --- |
| `FUNCTION_ID` | `NUMBER` | Function ID |
| `FUNCTION_NAME` | `VARCHAR2(18)` | Function name:  - `RMAN` - `DBWR` - `LGWR` - `ARCH` - `XDB` - `Streams` `AQ` - `Data` `Pump` - `Recovery` - `Buffer` `Cache` `Reads` - `Direct` `Reads` - `Direct` `Writes` - `Smart` `Scan` - `Archive` `Manager` - `Others` |
| `SMALL_READ_MEGABYTES` | `NUMBER` | Number of megabytes read via single block read requests |
| `SMALL_WRITE_MEGABYTES` | `NUMBER` | Number of megabytes written via single block write requests |
| `LARGE_READ_MEGABYTES` | `NUMBER` | Number of megabytes read via multiblock read requests |
| `LARGE_WRITE_MEGABYTES` | `NUMBER` | Number of megabytes written via multiblock write requests |
| `SMALL_READ_REQS` | `NUMBER` | Number of single block read requests |
| `SMALL_WRITE_REQS` | `NUMBER` | Number of single block write requests |
| `LARGE_READ_REQS` | `NUMBER` | Number of multiblock read requests |
| `LARGE_WRITE_REQS` | `NUMBER` | Number of multiblock write requests |
| `NUMBER_OF_WAITS` | `NUMBER` | Number of synchronous I/O waits by functionality |
| `WAIT_TIME` | `NUMBER` | Total synchronous I/O wait time (in milliseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |