---
title: "V$SYSTEM_WAIT_CLASS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3099.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYSTEM_WAIT_CLASS` displays the instance-wide time totals for each registered wait class.

| Column | Datatype | Description |
| --- | --- | --- |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the wait class |
| `WAIT_CLASS#` | `NUMBER` | Number of the wait class |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the wait class |
| `TOTAL_WAITS` | `NUMBER` | Number of times waits of the class occurred |
| `TIME_WAITED` | `NUMBER` | Amount of time (in hundredths of a second) spent in the wait by all sessions in the instance |
| `TOTAL_WAITS_FG` | `NUMBER` | Number of times waits from this wait class occurred in foreground sessions |
| `TIME_WAITED_FG` | `NUMBER` | Amount of time (in hundredths of a second) spent in waits from this wait class in foreground sessions |