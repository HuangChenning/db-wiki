---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IOSTAT_NETWORK.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.21 V$IOSTAT\_NETWORK

`V$IOSTAT_NETWORK` displays information about network I/O statistics that were caused by accessing files on a remote database instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `CLIENT` | `VARCHAR2(32)` | Database client name initiating the network I/O (for example, RMAN or PL/SQL) |
| `READS#` | `NUMBER` | Number of read operations issued |
| `WRITES#` | `NUMBER` | Number of write operations issued |
| `KBYTES_READ` | `NUMBER` | Total number of kilobytes read |
| `KBYTES_WRITTEN` | `NUMBER` | Total number of kilobytes written |
| `READ_LATENCY` | `NUMBER` | Total read wait time (in milliseconds) |
| `WRITE_LATENCY` | `NUMBER` | Total write wait time (in milliseconds) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |