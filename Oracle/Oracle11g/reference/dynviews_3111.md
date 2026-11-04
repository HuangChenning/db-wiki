---
title: "V$TIMER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3111.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$TIMER` displays the elapsed time in hundredths of a second. Time is measured since the beginning of the epoch, which is operating system specific, and wraps around to 0 again whenever the value overflows four bytes (roughly 497 days).

| Column | Datatype | Description |
| --- | --- | --- |
| `HSECS` | `NUMBER` | Elapsed time (in hundredths of a second) |