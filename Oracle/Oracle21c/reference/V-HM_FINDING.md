---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HM_FINDING.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.279 V$HM\_FINDING

`V$HM_FINDING` displays information about all the findings of various Health Monitor runs.

| Column | Datatype | Description |
| --- | --- | --- |
| `FINDING_ID` | `NUMBER` | Unique ID to represent the finding |
| `RUN_ID` | `NUMBER` | ID of the run that created this finding |
| `NAME` | `VARCHAR2(32)` | Name of the finding |
| `PARENT_ID` | `NUMBER` | Parent finding ID for this finding |
| `CHILD_COUNT` | `NUMBER` | Number of active (open) child findings, if this finding is a parent finding type |
| `CLASS_NAME` | `VARCHAR2(32)` | Name of the class to which this finding belongs |
| `TIME_DETECTED` | `TIMESTAMP(6)` | Time this finding was detected |
| `MODIFIED` | `TIMESTAMP(6)` | Time that this finding was last modified |
| `PRIORITY` | `VARCHAR2(8)` | Priority of the finding:  - `LOW,` - `HIGH` - `CRITICAL` |
| `STATUS` | `VARCHAR2(12)` | Status of the finding:  - `OPEN` - `CLOSED` |
| `TYPE` | `VARCHAR2(13)` | Type of the finding:  - `INFORMATIONAL` - `FAILURE` |
| `DESCRIPTION` | `VARCHAR2(1024)` | Description of the finding |
| `DAMAGE_DESCRIPTION` | `VARCHAR2(1024)` | Possible damage description of the finding |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |