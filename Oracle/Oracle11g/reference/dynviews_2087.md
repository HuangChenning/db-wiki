---
title: "V$PARAMETER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2087.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PARAMETER` displays information about the initialization parameters that are currently in effect for the session. A new session inherits parameter values from the instance-wide values displayed by the `V$SYSTEM_PARAMETER` view.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM` | `NUMBER` | Parameter number |
| `NAME` | `VARCHAR2(80)` | Name of the parameter |
| `TYPE` | `NUMBER` | Parameter type: |
| `VALUE` | `VARCHAR2(4000)` | Parameter value for the session (if modified within the session); otherwise, the instance-wide parameter value |
| `DISPLAY_VALUE` | `VARCHAR2(4000)` | Parameter value in a user-friendly format. For example, if the `VALUE` column shows the value `262144` for a big integer parameter, then the `DISPLAY_VALUE` column will show the value `256K`. |
| `ISDEFAULT` | `VARCHAR2(9)` | Indicates whether the parameter is set to the default value (`TRUE`) or the parameter value was specified in the parameter file (`FALSE`) |
| `ISSES_MODIFIABLE` | `VARCHAR2(5)` | Indicates whether the parameter can be changed with `ALTER SESSION` (`TRUE`) or not (`FALSE`) |
| `ISSYS_MODIFIABLE` | `VARCHAR2(9)` | Indicates whether the parameter can be changed with `ALTER SYSTEM` and when the change takes effect: - `IMMEDIATE` - Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect immediately. - `DEFERRED` - Parameter can be changed with `ALTER SYSTEM` regardless of the type of parameter file used to start the instance. The change takes effect in subsequent sessions. - `FALSE` - Parameter cannot be changed with `ALTER SYSTEM` unless a server parameter file was used to start the instance. The change takes effect in subsequent instances. |
| `ISINSTANCE_MODIFIABLE` | `VARCHAR2(5)` | For parameters that can be changed with `ALTER SYSTEM`, indicates whether the value of the parameter can be different for every instance (`TRUE`) or whether the parameter must have the same value for all Real Application Clusters instances (`FALSE`). If the `ISSYS_MODIFIABLE` column is `FALSE`, then this column is always `FALSE`. |
| `ISMODIFIED` | `VARCHAR2(10)` | Indicates whether the parameter has been modified after instance startup: - `MODIFIED` - Parameter has been modified with `ALTER SESSION` - `SYSTEM_MOD` - Parameter has been modified with `ALTER SYSTEM` (which causes all the currently logged in sessions' values to be modified) - `FALSE` - Parameter has not been modified after instance startup |
| `ISADJUSTED` | `VARCHAR2(5)` | Indicates whether Oracle adjusted the input value to a more suitable value (for example, the parameter value should be prime, but the user input a non-prime number, so Oracle adjusted the value to the next prime number) |
| `ISDEPRECATED` | `VARCHAR2(5)` | Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`) |
| `ISBASIC` | `VARCHAR2(5)` | Indicates whether the parameter is a basic parameter (`TRUE`) or not (`FALSE`) |
| `DESCRIPTION` | `VARCHAR2(255)` | Description of the parameter |
| `UPDATE_COMMENT` | `VARCHAR2(255)` | Comments associated with the most recent update |
| `HASH` | `NUMBER` | Hash value for the parameter name |