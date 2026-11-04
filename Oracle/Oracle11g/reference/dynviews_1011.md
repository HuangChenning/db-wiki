---
title: "V$ARCHIVE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1011.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$ARCHIVE` displays information about redo log files in need of archiving. Each row displays information for one thread. This information is also available in `V$LOG`. Oracle recommends that you use `V$LOG`.

See Also:

["V$LOG"](dynviews_2031.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP#` | `NUMBER` | Log file group number |
| `THREAD#` | `NUMBER` | Log file thread number |
| `SEQUENCE#` | `NUMBER` | Log file sequence number |
| `ISCURRENT` | `VARCHAR2(3)` | This is the current online redo log |
| `CURRENT` | `VARCHAR2(3)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `ISCURRENT`. |
| `FIRST_CHANGE#` | `NUMBER` | First SCN stored in the current log |