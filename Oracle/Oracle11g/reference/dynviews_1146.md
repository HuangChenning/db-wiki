---
title: "V$FLASHBACK_DATABASE_STAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1146.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FLASHBACK_DATABASE_STAT` displays statistics for monitoring the I/O overhead of logging flashback data. This view also displays the estimated flashback space needed based on previous workloads.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Beginning of the time interval |
| `END_TIME` | `DATE` | End of the time interval |
| `FLASHBACK_DATA` | `NUMBER` | Number of bytes of flashback data written during the interval |
| `DB_DATA` | `NUMBER` | Number of bytes of database data read and written during the interval |
| `REDO_DATA` | `NUMBER` | Number of bytes of redo data written during the interval |
| `ESTIMATED_FLASHBACK_SIZE` | `NUMBER` | Value of `ESTIMATED_FLASHBACK_SIZE` in `V$FLASHBACK_DATABASE_LOG` at the end of the time interval |