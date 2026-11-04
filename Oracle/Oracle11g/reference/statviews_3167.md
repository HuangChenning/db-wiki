---
title: DBA_ENABLED_TRACES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3167.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ENABLED_TRACES` displays information about enabled SQL traces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TRACE_TYPE` | `VARCHAR2(21)` |  | Type of the trace: |
| `PRIMARY_ID` | `VARCHAR2(64)` |  | Primary qualifier (specific client identifier or service name) |
| `QUALIFIER_ID1` | `VARCHAR2(48)` |  | Secondary qualifier (specific module name) |
| `QUALIFIER_ID2` | `VARCHAR2(32)` |  | Additional qualifier (specific action name) |
| `WAITS` | `VARCHAR2(5)` |  | Indicates whether waits are traced (`TRUE`) or not (`FALSE`) |
| `BINDS` | `VARCHAR2(5)` |  | Indicates whether binds are traced (`TRUE`) or not (`FALSE`) |
| `INSTANCE_NAME` | `VARCHAR2(16)` |  | Instance name for tracing restricted to named instances |

See Also:

The following support note at `https://support.oracle.com` for more information about using the `DBMS_MONITOR` PL/SQL package and the `DBA_ENABLED_TRACES` view:

Note 293661.1 "Tracing Enhancements In 10g and 11g Using DBMS\_MONITOR"