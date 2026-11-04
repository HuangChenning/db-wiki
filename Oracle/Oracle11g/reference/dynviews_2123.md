---
title: "V$RECOVER_FILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2123.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RECOVER_FILE` displays the status of files needing media recovery.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File identifier number |
| `ONLINE` | `VARCHAR2(7)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `ONLINE_STATUS`. |
| `ONLINE_STATUS` | `VARCHAR2(7)` | Online status (`ONLINE`, `OFFLINE`) |
| `ERROR` | `VARCHAR2(18)` | Why the file needs to be recovered: NULL if reason unknown, or `OFFLINE NORMAL` if recovery not needed |
| `CHANGE#` | `NUMBER` | SCN where recovery must start |
| `TIME` | `DATE` | Time of SCN when recovery must start |