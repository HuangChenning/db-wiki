---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_SQL_MANAGEMENT_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.363 DBA\_SQL\_MANAGEMENT\_CONFIG

`DBA_SQL_MANAGEMENT_CONFIG` displays the configuration parameters of the SQL management base.

You must have the `DBA` role in order to change the configuration parameter values.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the configuration parameter:  - `AUTO_CAPTURE_ACTION` - `AUTO_CAPTURE_MODULE` - `AUTO_CAPTURE_PARSING_SCHEMA_NAME` - `AUTO_CAPTURE_SQL_TEXT` - `PLAN_RETENTION_WEEKS` - `SPACE_BUDGET_PERCENT` |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` |  | Value of the configuration parameter |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Time the parameter value was last updated |
| `MODIFIED_BY` | `VARCHAR2(128)` |  | User who last updated the parameter value |