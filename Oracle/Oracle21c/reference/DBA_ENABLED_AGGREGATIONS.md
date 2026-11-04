---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ENABLED_AGGREGATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.303 DBA\_ENABLED\_AGGREGATIONS

`DBA_ENABLED_AGGREGATIONS` displays information about enabled on-demand statistic aggregation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AGGREGATION_TYPE` | `VARCHAR2(21)` |  | Type of the aggregation:  - `CLIENT_ID` - `SERVICE` - `SERVICE_MODULE` - `SERVICE_MODULE_ACTION` |
| `PRIMARY_ID` | `VARCHAR2(64)` |  | Primary qualifier (specific client identifier or service name) |
| `QUALIFIER_ID1` | `VARCHAR2(48)` |  | Secondary qualifier (specific module name) |
| `QUALIFIER_ID2` | `VARCHAR2(32)` |  | Additional qualifier (specific action name) |