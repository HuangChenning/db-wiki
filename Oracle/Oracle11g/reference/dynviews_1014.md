---
title: "V$ARCHIVE_GAP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1014.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ARCHIVE_GAP` displays information about archive gaps on a standby database. This view can be used to find out the current archive gap that is blocking recovery for the current recovery incarnation.

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Thread number of the missing archived redo log files. The number is 1 for a single instance. For Real Application Clusters, this column will contain different numbers. |
| `LOW_SEQUENCE#` | `NUMBER` | Lowest sequence number of the log files received on the standby system |
| `HIGH_SEQUENCE#` | `NUMBER` | Highest sequence number of the log files received on the standby system |