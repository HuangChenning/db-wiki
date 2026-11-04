---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PARAMETER2.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.110 V$PARAMETER2

`V$PARAMETER2` displays information about the initialization parameters that are currently in effect for the session, with each list parameter value appearing as a row in the view. A new session inherits parameter values from the instance-wide values displayed in the `V$SYSTEM_PARAMETER2` view.

Presenting the list parameter values in this format enables you to quickly determine the values for a list parameter. For example, if a parameter value is `a, b`, then the `V$PARAMETER` view does not tell you if the parameter has two values (both `a` and `b`) or one value (`a, b`). `V$PARAMETER2` makes the distinction between the list parameter values clear.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM` | `NUMBER` | Parameter number |
| `NAME` | `VARCHAR2(80)` | Name of the parameter |
| `TYPE` | `NUMBER` | Parameter type:  - `1` - Boolean - `2` - String - `3` - Integer - `4` - Parameter file - `5` - Reserved - `6` - Big integer |
| `VALUE` | `VARCHAR2(4000)` | Parameter value for the session (if modified within the session); otherwise, the instance-wide parameter value |
| `DISPLAY_VALUE` | `VARCHAR2(4000)` | Parameter value in a user-friendly format. For example, if the `VALUE` column shows the value `262144` for a big integer parameter, then the `DISPLAY_VALUE` column will show the value `256K`. |
| `ISDEFAULT` | `VARCHAR2(6)` | Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`) |
| `ISSES_MODIFIABLE` | `VARCHAR2(5)` | Indicates whether the parameter can be changed with `ALTER SESSION` (`TRUE`) or not (`FALSE`) |
| `ISSYS_MODIFIABLE` | `VARCHAR2(9)` | Indicates whether the parameter can be changed with `ALTER SYSTEM` and when the change takes effect:  - `IMMEDIATE` - Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect immediately. - `DEFERRED` - Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect in subsequent sessions. - `FALSE` - Parameter cannot be changed with `ALTER SYSTEM` unless a server parameter file was used to start the instance. The change takes effect in subsequent instances. |
| `ISPDB_MODIFIABLE` | `VARCHAR2(5)` | Indicates whether the parameter can be modified inside a PDB (`TRUE`) or not (`FALSE`).  In a non-CDB, the value of this column is `NULL`. |
| `ISINSTANCE_MODIFIABLE` | `VARCHAR2(5)` | For parameters that can be changed with `ALTER SYSTEM`, indicates whether the value of the parameter can be different for every instance (`TRUE`) or whether the parameter must have the same value for all Real Application Clusters instances (`FALSE`). If the `ISSYS_MODIFIABLE` column is `FALSE`, then this column is always `FALSE`. |
| `ISMODIFIED` | `VARCHAR2(10)` | Indicates whether the parameter has been modified after instance startup:  - `MODIFIED` - Parameter has been modified with `ALTER SESSION` - `SYSTEM_MOD` - Parameter has been modified with `ALTER SYSTEM` (which causes all the currently logged in sessions' values to be modified) - `FALSE` - Parameter has not been modified after instance startup |
| `ISADJUSTED` | `VARCHAR2(5)` | Indicates whether Oracle adjusted the input value to a more suitable value (for example, the parameter value should be prime, but the user input a non-prime number, so Oracle adjusted the value to the next prime number) |
| `ISDEPRECATED` | `VARCHAR2(5)` | Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`) |
| `ISBASIC` | `VARCHAR2(5)` | Indicates whether the parameter is a basic parameter (`TRUE`) or not (`FALSE`) |
| `DESCRIPTION` | `VARCHAR2(255)` | Description of the parameter |
| `ORDINAL` | `NUMBER` | Position (ordinal number) of the parameter value. Useful only for parameters whose values are lists of strings. |
| `UPDATE_COMMENT` | `VARCHAR2(255)` | Comments associated with the most recent update |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$SYSTEM\_PARAMETER](V-SYSTEM_PARAMETER.md) "
- " [V$PARAMETER](V-PARAMETER.md) "