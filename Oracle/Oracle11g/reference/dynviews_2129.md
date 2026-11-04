---
title: "V$RECOVERY_STATUS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2129.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RECOVERY_STATUS` contains statistics of the current recovery process. This view contains useful information only for the Oracle process doing the recovery. When Recovery Manager directs a server process to perform recovery, only Recovery Manager is able to view the relevant information in this view. `V$RECOVERY_STATUS` will be empty to all other Oracle users.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECOVERY_CHECKPOINT` | `DATE` | Point in time to which the recovery has occurred. If no logs have been applied, this is the point in time the recovery starts. |
| `THREAD` | `NUMBER` | Number of the redo thread currently being processed |
| `SEQUENCE_NEEDED` | `NUMBER` | Log sequence number of the log needed by the recovery process. The value is `0` if no log is needed. |
| `SCN_NEEDED` | `VARCHAR2(16)` | Low SCN of the log needed by recovery. The value is `0` if unknown or no log is needed. |
| `TIME_NEEDED` | `DATE` | Time when the log was created. The value is midnight on 1/1/88 if the time is unknown or if no log is needed. |
| `PREVIOUS_LOG_NAME` | `VARCHAR2(513)` | Filename of the log |
| `PREVIOUS_LOG_STATUS` | `VARCHAR2(13)` | Status of the previous log. Contains one of the following values: `RELEASE; WRONG NAME; MISSING NAME; UNNEEDED NAME; NONE` |
| `REASON` | `VARCHAR2(13)` | Reason recovery is returning control to the user (`NEED LOG\|LOG REUSED\|THREAD DISABLED`) |