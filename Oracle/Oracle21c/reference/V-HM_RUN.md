---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HM_RUN.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.282 V$HM\_RUN

`V$HM_RUN` displays information about all Health Monitor checks and their status.

| Column | Datatype | Description |
| --- | --- | --- |
| `RUN_ID` | `NUMBER` | Unique ID to represent the run |
| `NAME` | `VARCHAR2(32)` | Unique name used to identify the run |
| `CHECK_NAME` | `VARCHAR2(32)` | Name of the check |
| `RUN_MODE` | `VARCHAR2(8)` | Mode of the run:  - `MANUAL` - `REACTIVE` - `AUTO` |
| `TIMEOUT` | `NUMBER` | Number of seconds allowed for this run to complete before it is terminated |
| `START_TIME` | `TIMESTAMP(6)` | Start time of the run |
| `LAST_RESUME_TIME` | `TIMESTAMP(6)` | Last resumed time for the run |
| `END_TIME` | `TIMESTAMP(6)` | End time of the run |
| `MODIFIED_TIME` | `TIMESTAMP(6)` | Last modified time of the run record |
| `STATUS` | `VARCHAR2(11)` | Status of the run:  - `INITIAL` - `EXECUTING` - `INTERRUPTED` - `TIMEDOUT` - `CANCELLED` - `COMPLETED` - `ERROR` |
| `SRC_INCIDENT` | `NUMBER` | Source incident ID that activated this run |
| `NUM_INCIDENT` | `NUMBER` | Number of incidents created by this run |
| `ERROR_NUMBER` | `NUMBER` | Error number if the run failed to complete because of an error |
| `PROBLEM_ID` | `NUMBER` | Problem ID of the source incident ID that may have activated this Run |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |