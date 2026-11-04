---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TSDP_POLICY_CONDITION.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.61 DBA\_TSDP\_POLICY\_CONDITION

`DBA_TSDP_POLICY_CONDITION` describes the Transparent Sensitive Data Protection policy and condition mapping. It also lists the property-value pairs for the condition.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | The name of the Transparent Sensitive Data Protection policy |
| `SUB_POLICY` | `NUMBER` | `NOT NULL` | The sub policy of the Transparent Sensitive Data Protection policy |
| `PROPERTY` | `VARCHAR2(11)` |  | The condition property. Possible values:  - `DATATYPE` - `LENGTH` - `SCHEMA_NAME` - `TABLE_NAME` |
| `VALUE` | `VARCHAR2(128)` |  | The value of the condition property |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG855) for more information about using Transparent Sensitive Data Protection