---
title: DBA_SQL_MANAGEMENT_CONFIG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4275.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_SQL_MANAGEMENT_CONFIG` displays the configuration parameters of the SQL management base. You must have the `DBA` role in order to change the configuration parameter values.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PARAMETER_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the configuration parameter: |
| `PARAMETER_VALUE` | `NUMBER` | `NOT NULL` | Value of the configuration parameter |
| `LAST_MODIFIED` | `TIMESTAMP(6)` |  | Time the parameter value was last updated |
| `MODIFIED_BY` | `VARCHAR2(30)` |  | User who last updated the parameter value |