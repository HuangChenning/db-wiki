---
title: "V$LOGFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2033.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGFILE` contains information about redo log files.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP#` | `NUMBER` | Redo log group identifier number |
| `STATUS` | `VARCHAR2(7)` | Status of the log member: |
| `TYPE` | `VARCHAR2(7)` | Type of the logfile: |
| `MEMBER` | `VARCHAR2(513)` | Redo log member name |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |