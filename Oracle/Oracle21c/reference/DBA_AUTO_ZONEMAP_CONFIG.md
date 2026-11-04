---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTO_ZONEMAP_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.192 DBA\_AUTO\_ZONEMAP\_CONFIG

`DBA_AUTO_ZONEMAP_CONFIG` describes the current settings for automatic zone map configuration parameters.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Parameter name |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Parameter value |
| `LAST_UPDATED` | `TIMESTAMP(6)` |  | Time at which the parameter value was last updated |
| `UPDATED_BY` | `VARCHAR2(128)` |  | User who last updated the parameter value |
| `DESCRIPTION` | `VARCHAR2(71)` |  | Brief description of the parameter |

Note:

This view is available starting with Oracle Database 21c.