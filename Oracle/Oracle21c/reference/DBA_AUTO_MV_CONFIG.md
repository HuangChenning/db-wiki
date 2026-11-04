---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_MV_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.184 DBA\_AUTO\_MV\_CONFIG

`DBA_AUTO_MV_CONFIG` displays configuration parameters associated with automatic materialized views and automatic zone maps.

The configuration parameters displayed in this view can be updated with `CONFIGURE` procedure of the `DBMS_AUTO_MV` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the configuration parameter |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Value of the configuration parameter |
| `LAST_UPDATED` | `TIMESTAMP(6)` |  | Date and time of the last parameter value update |
| `UPDATED_BY` | `VARCHAR2(128)` |  | User who last updated the parameter value |
| `DESCRIPTION` | `VARCHAR2(72)` |  | Description of the configuration parameter |

Note:

This view is available starting with Oracle Database 21c.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS72964) for more information about the `DBMS_AUTO_MV.CONFIGURE` procedure