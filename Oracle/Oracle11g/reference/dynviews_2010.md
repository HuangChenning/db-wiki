---
title: "V$IOSTAT_FUNCTION"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2010.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$IOSTAT_FUNCTION` displays disk I/O statistics for database functions (such as the LGWR and DBWR).

| Column | Datatype | Description |
| --- | --- | --- |
| `FUNCTION_ID` | `NUMBER` | Function ID |
| `FUNCTION_NAME` | `VARCHAR2(18)` | Function name: - `RMAN` - `DBWR` - `LGWR` - `ARCH` - `XDB` - `Streams` `AQ` - `Data` `Pump` - `Recovery` - `Buffer` `Cache` `Reads` - `Direct` `Reads` - `Direct` `Writes` - `Smart` `Scan` - `Archive` `Manager` - `Others` |
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