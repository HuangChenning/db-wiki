---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SYS_OPTIMIZER_ENV.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.92 V$SYS\_OPTIMIZER\_ENV

`V$SYS_OPTIMIZER_ENV` displays the contents of the optimizer environment for the instance. The optimizer environment stores the value of the main parameters used by the Oracle optimizer when building the execution plan of a SQL statement. Hence, modifying the value of one or more of these parameters (for example, by issuing an `ALTER SYSTEM` statement) could lead to plan changes.

The parameters displayed by this view are either regular initialization parameters (such as `OPTIMIZER_FEATURES_ENABLE`) or pseudo parameters (such as `ACTIVE_INSTANCE_COUNT`).

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Unique identifier of the parameter in the optimizer environment |
| `NAME` | `VARCHAR2(40)` | Name of the parameter |
| `SQL_FEATURE` | `VARCHAR2(64)` | Associated feature control ID |
| `ISDEFAULT` | `VARCHAR2(3)` | Indicates whether the parameter is set to the default value (`YES`) or not (`NO`) |
| `VALUE` | `VARCHAR2(25)` | Value of the parameter |
| `DEFAULT_VALUE` | `VARCHAR2(25)` | Default value of the parameter |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [OPTIMIZER\_FEATURES\_ENABLE](OPTIMIZER_FEATURES_ENABLE.md) "
- " [ACTIVE\_INSTANCE\_COUNT](ACTIVE_INSTANCE_COUNT.md) "