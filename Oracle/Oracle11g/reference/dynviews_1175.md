---
title: "V$HM_FINDING"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1175.htm
tags:
  - oracle
  - 11g
  - reference
---

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
| `PRIORITY` | `VARCHAR2(8)` | Priority of the finding: |
| `STATUS` | `VARCHAR2(12)` | Status of the finding: |
| `TYPE` | `VARCHAR2(13)` | Type of the finding: |
| `DESCRIPTION` | `VARCHAR2(1024)` | Description of the finding |
| `DAMAGE_DESCRIPTION` | `VARCHAR2(1024)` | Possible damage description of the finding |