---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SPPARAMETER.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.45 V$SPPARAMETER

If a server parameter file was not used to start the instance, then each row of the view will contain `FALSE` in the `ISSPECIFIED` column.

| Column | Datatype | Description |
| --- | --- | --- |
| `FAMILY` | VARCHAR2(80) | For internal use only |
| `SID` | `VARCHAR2(80)` | SID for which the parameter is defined. |
| `NAME` | `VARCHAR2(80)` | Name of the parameter |
| `TYPE` | `VARCHAR2(11)` | Parameter type |
| `VALUE` | `VARCHAR2(255)` | Parameter value (null if a server parameter file was not used to start the instance) |
| `DISPLAY_VALUE` | `VARCHAR2(255)` | Parameter value in a user-friendly format. For example, if the `VALUE` column shows the value `262144` for a big integer parameter, then the `DISPLAY_VALUE` column will show the value `256K`. |
| `ISSPECIFIED` | `VARCHAR2(6)` | Indicates whether the parameter was specified in the server parameter file (`TRUE`) or not (`FALSE`) |
| `ORDINAL` | `NUMBER` | Position (ordinal number) of the parameter value (`0` if a server parameter file was not used to start the instance). Useful only for parameters whose values are lists of strings. |
| `UPDATE_COMMENT` | `VARCHAR2(255)` | Comments associated with the most recent update (null if a server parameter file was not used to start the instance) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |