---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ENABLED_TRACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.304 DBA\_ENABLED\_TRACES

`DBA_ENABLED_TRACES` displays information about enabled SQL traces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRACE_TYPE` | `VARCHAR2(21)` |  | Type of the trace:  - `CLIENT_ID` - `SERVICE` - `SERVICE_MODULE` - `SERVICE_MODULE_ACTION` - `DATABASE` |
| `PRIMARY_ID` | `VARCHAR2(64)` |  | Primary qualifier (specific client identifier or service name) |
| `QUALIFIER_ID1` | `VARCHAR2(64)` |  | Secondary qualifier (specific module name) |
| `QUALIFIER_ID2` | `VARCHAR2(64)` |  | Additional qualifier (specific action name) |
| `WAITS` | `VARCHAR2(5)` |  | Indicates whether waits are traced (`TRUE`) or not (`FALSE`) |
| `BINDS` | `VARCHAR2(5)` |  | Indicates whether binds are traced (`TRUE`) or not (`FALSE`) |
| `PLAN_STATS` | `VARCHAR2(10)` |  | Indicates whether cursor execution statistics are traced. Possible values include:  - `ALL_EXEC`: Execution statistics are dumped at each cursor execution - `NEVER`: Execution statistics are never dumped - `FIRST_EXEC`: Execution statistics are dumped during the first execution of the cursor. This is the default behavior. |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Instance name for tracing restricted to named instances |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS091) for more information about the `DBMS_MONITOR` package