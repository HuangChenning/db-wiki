---
title: "V$LOGSTDBY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2044.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$LOGSTDBY` is deprecated.

| Column | Datatype | Description |
| --- | --- | --- |
| `SERIAL#` | `NUMBER` | SQL Session serial number. This data is used when joining this view with the `V$SESSION` and `V$PX_SESSION` views. |
| `LOGSTDBY_ID` | `NUMBER` | Parallel query slave ID |
| `PID` | `VARCHAR2(12)` | Process ID of the SQL apply process |
| `TYPE` | `VARCHAR2(30)` | Indicates the task being performed by the process (`COORDINATOR`, `APPLIER`, `ANALYZER`, `READER`, `PREPARER`, or `BUILDER`) |
| `STATUS_CODE` | `NUMBER` | Status number (or Oracle error code) belonging to the STATUS message |
| `STATUS` | `VARCHAR2(256)` | Description of the current activity of the process |
| `HIGH_SCN` | `NUMBER` | Highest system change number (SCN) seen by the process. This column is used to confirm the progress of the individual process. |