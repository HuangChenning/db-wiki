---
title: "V$FS_FAILOVER_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1150.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FS_FAILOVER_STATS` displays statistics about Fast-Start Failovers (FSFOs) occurring on the system.

| Column | Datatype | Description |
| --- | --- | --- |
| `LAST_FAILOVER_TIME` | `VARCHAR2(20)` | Timestamp of the last Fast-Start Failover |
| `LAST_FAILOVER_REASON` | `VARCHAR2(255)` | Reason for the last Fast-Start Failover |