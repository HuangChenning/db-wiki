---
title: "V$IOSTAT_NETWORK"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2012.htm
tags:
  - oracle
  - 11g
  - reference
---

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