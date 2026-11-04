---
title: "V$LATCH_MISSES"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2017.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LATCH_MISSES` displays statistics about missed attempts to acquire a latch.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARENT_NAME` | `VARCHAR2(64)` | Latch name of a parent latch |
| `WHERE` | `VARCHAR2(80)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `LOCATION`. |
| `NWFAIL_COUNT` | `NUMBER` | Number of times that no-wait acquisition of the latch failed |
| `SLEEP_COUNT` | `NUMBER` | Number of times that acquisition attempts caused sleeps |
| `WTR_SLP_COUNT` | `NUMBER` | Number of times a waiter slept |
| `LONGHOLD_COUNT` | `NUMBER` | Number of times someone held a latch for the entire duration of someone else's sleep |
| `LOCATION` | `VARCHAR2(80)` | Location that attempted to acquire the latch |