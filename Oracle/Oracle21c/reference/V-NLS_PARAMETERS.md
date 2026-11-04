---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-NLS_PARAMETERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.92 V$NLS\_PARAMETERS

`V$NLS_PARAMETERS` contains current values of NLS parameters.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER` | `VARCHAR2(64)` | Parameter names are as follows: `NLS_CALENDAR`, `NLS_CHARACTERSET`, `NLS_COMP`, `NLS_CURRENCY`, `NLS_DATE_FORMAT`, `NLS_DATE_LANGUAGE`, `NLS_DUAL_CURRENCY`, `NLS_ISO_CURRENCY`, `NLS_LANGUAGE`, `NLS_LENGTH_SEMANTICS`,`                                     NLS_NCHAR_CHARACTERSET`, `NLS_NCHAR_CONV_EXCP`, `NLS_NUMERIC_CHARACTERS`, `NLS_SORT`, `NLS_TERRITORY`, `NLS_TIMESTAMP_FORMAT`, and `NLS_TIMESTAMP_TZ_FORMAT`.  Two additional parameters, `NLS_TIME_FORMAT` and `NLS_TIME_TZ_FORMAT`, are currently used for internal purposes only. |
| `VALUE` | `VARCHAR2(64)` | NLS parameter value |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |