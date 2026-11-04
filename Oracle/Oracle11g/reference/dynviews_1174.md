---
title: "V$HM_CHECK_PARAM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1174.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$HM_CHECK_PARAM` displays information about the input parameters of all Health Monitor checks.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Parameter ID |
| `NAME` | `VARCHAR2(64)` | Parameter name |
| `CHECK_ID` | `NUMBER` | ID of the check to which this parameter belongs |
| `TYPE` | `VARCHAR2(20)` | Data type of the input parameter: |
| `DEFAULT_VALUE` | `VARCHAR2(64)` | Default value for this parameter |
| `FLAGS` | `NUMBER` | Reserved for internal use |
| `DESCRIPTION` | `VARCHAR2(64)` | Description of the parameter |