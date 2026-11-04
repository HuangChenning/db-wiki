---
title: DBA_ENABLED_AGGREGATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3166.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ENABLED_AGGREGATIONS` displays information about enabled on-demand statistic aggregation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `AGGREGATION_TYPE` | `VARCHAR2(21)` |  | Type of the aggregation: - `CLIENT_ID` - `SERVICE` - `SERVICE_MODULE` - `SERVICE_MODULE_ACTION` |
| `PRIMARY_ID` | `VARCHAR2(64)` |  | Primary qualifier (specific client identifier or service name) |
| `QUALIFIER_ID1` | `VARCHAR2(48)` |  | Secondary qualifier (specific module name) |
| `QUALIFIER_ID2` | `VARCHAR2(32)` |  | Additional qualifier (specific action name) |