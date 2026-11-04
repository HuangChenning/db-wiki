---
title: "V$HM_RUN"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1178.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HM_RUN` displays information about all Health Monitor checks and their status.

| Column | Datatype | Description |
| --- | --- | --- |
| `RUN_ID` | `NUMBER` | Unique ID to represent the run |
| `NAME` | `VARCHAR2(32)` | Unique name used to identify the run |
| `CHECK_NAME` | `VARCHAR2(32)` | Name of the check |
| `RUN_MODE` | `VARCHAR2(8)` | Mode of the run: |
| `TIMEOUT` | `NUMBER` | Number of seconds allowed for this run to complete before it is aborted |
| `START_TIME` | `TIMESTAMP(6)` | Start time of the run |
| `LAST_RESUME_TIME` | `TIMESTAMP(6)` | Last resumed time for the run |
| `END_TIME` | `TIMESTAMP(6)` | End time of the run |
| `MODIFIED_TIME` | `TIMESTAMP(6)` | Last modified time of the run record |
| `STATUS` | `VARCHAR2(11)` | Status of the run: |
| `SRC_INCIDENT` | `NUMBER` | Source incident ID that activated this run |
| `NUM_INCIDENT` | `NUMBER` | Number of incidents created by this run |
| `ERROR_NUMBER` | `NUMBER` | Error number if the run failed to complete because of an error |
| `PROBLEM_ID` | `NUMBER` | Problem ID of the source incident ID that may have activated this Run |