---
title: "V$LOGHIST"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2034.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGHIST` contains log history information from the control file. This view is retained for historical compatibility. Oracle recommends that you use `V$LOG_HISTORY` instead.

See Also:

["V$LOG\_HISTORY"](dynviews_2032.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `THREAD#` | `NUMBER` | Log thread number |
| `SEQUENCE#` | `NUMBER` | Log sequence number |
| `FIRST_CHANGE#` | `NUMBER` | Lowest SCN in the log |
| `FIRST_TIME` | `DATE` | Time of first SCN in the log |
| `SWITCH_CHANGE#` | `NUMBER` | SCN at which the log switch occurred; one more than highest SCN in the log |