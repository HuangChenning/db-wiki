---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_SQL_MANAGEMENT_CONFIG.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_SQL_MANAGEMENT_CONFIG` displays the configuration parameters of the SQL management base.

You must have the `DBA` role in order to change the configuration parameter values.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the configuration parameter:  - `SPACE_BUDGET_PERCENT` - `PLAN_RETENTION_WEEKS` - `AUTO_CAPTURE_SQL_TEXT` - `AUTO_CAPTURE_PARSING_SCHEMA_NAME` - `AUTO_CAPTURE_MODULE` - `AUTO_CAPTURE_ACTION` |
| `PARAMETER_VALUE` | `VARCHAR2(4000)` | `NOT NULL` | Value of the configuration parameter |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Time the parameter value was last updated |
| `MODIFIED_BY` | `VARCHAR2(128)` |  | User who last updated the parameter value |