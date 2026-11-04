---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_INDEX_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.178 DBA\_AUTO\_INDEX\_CONFIG

`DBA_AUTO_INDEX_CONFIG` displays the current configuration parameter settings for automatic indexing.

You can set automatic indexing configuration parameters by using the `DBMS_AUTO_INDEX.CONFIGURE` procedure.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the configuration parameter |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Value of the configuration parameter |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Time at which the parameter value was last modified |
| `MODIFIED_BY` | `VARCHAR2(128)` |  | User who last modified the parameter value |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-93A19936-453A-4C62-8DFB-FB52AC70C838) for more information about the `DBMS_AUTO_INDEX.CONFIGURE` procedure