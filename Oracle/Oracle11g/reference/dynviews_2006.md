---
title: "V$IOFUNCMETRIC"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2006.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$IOFUNCMETRIC` displays I/O statistics information by database function for the most recent time interval period.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin time for the metric value |
| `END_TIME` | `DATE` | End time for the metric value |
| `INTSIZE_CSEC` | `NUMBER` | Size of the time period |
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