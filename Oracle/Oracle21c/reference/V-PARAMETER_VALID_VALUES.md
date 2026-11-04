---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PARAMETER_VALID_VALUES.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.109 V$PARAMETER\_VALID\_VALUES

`V$PARAMETER_VALID_VALUES` displays a list of valid values for list parameters.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM` | `NUMBER` | Parameter number |
| `NAME` | `VARCHAR2(64)` | Parameter name |
| `ORDINAL` | `NUMBER` | Ordinal number in the list (1-based) |
| `VALUE` | `VARCHAR2(255)` | Parameter value at ordinal |
| `ISDEFAULT` | `VARCHAR2(64)` | Indicates whether the given ordinal value is the default value for the parameter |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |