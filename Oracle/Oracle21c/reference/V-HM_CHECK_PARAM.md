---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HM_CHECK_PARAM.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.278 V$HM\_CHECK\_PARAM

`V$HM_CHECK_PARAM` displays information about the input parameters of all Health Monitor checks.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Parameter ID |
| `NAME` | `VARCHAR2(64)` | Parameter name |
| `CHECK_ID` | `NUMBER` | ID of the check to which this parameter belongs |
| `TYPE` | `VARCHAR2(20)` | Data type of the input parameter:  - `DBKH_PARAM_UB4` - `DBKH_PARAM_UB8` - `DBKH_PARAM_TEXT` - `DBKH_PARAM_DATE` - `DBKH_PARAM_UB4_LIST` - `DBKH_PARAM_UB8_LIST` - `DBKH_PARAM_TEXT_LIST` - `DBKH_PARAM_DATE_LIST` |
| `DEFAULT_VALUE` | `VARCHAR2(64)` | Default value for this parameter |
| `FLAGS` | `NUMBER` | Reserved for internal use |
| `DESCRIPTION` | `VARCHAR2(1024)` | Description of the parameter |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |