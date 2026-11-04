---
title: "V$HM_CHECK"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1173.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HM_CHECK` displays information about all the checks registered with Health Monitor. Each check is uniquely identified by a name or an ID.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Health check ID |
| `NAME` | `VARCHAR2(64)` | Health check name |
| `NAME_NLS` | `VARCHAR2(1024)` | Internationalized names of the health checks |
| `CLSID` | `NUMBER` | Class ID to which this check belongs |
| `CLS_NAME` | `VARCHAR2(15)` | Class name of the check: |
| `FLAGS` | `NUMBER` | Reserved for internal use |
| `INTERNAL_CHECK` | `VARCHAR2(1)` | Internal check |
| `OFFLINE_CAPABLE` | `VARCHAR2(1)` | Ability to run when database is not open yet (Y or N) |
| `DESCRIPTION` | `VARCHAR2(64)` | Description of what the check does |