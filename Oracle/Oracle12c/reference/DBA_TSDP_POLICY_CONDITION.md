---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_TSDP_POLICY_CONDITION.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_TSDP_POLICY_CONDITION` describes the Transparent Sensitive Data Protection policy and condition mapping. It also lists the property-value pairs for the condition.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | The name of the Transparent Sensitive Data Protection policy |
| `SUB_POLICY` | `NUMBER` | `NOT NULL` | The sub policy of the Transparent Sensitive Data Protection policy |
| `PROPERTY` | `VARCHAR2(11)` |  | The condition property. Possible values:  - `DATATYPE` - `LENGTH` - `SCHEMA_NAME` - `TABLE_NAME` |
| `VALUE` | `VARCHAR2(128)` |  | The value of the condition property |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG855) for more information about using Transparent Sensitive Data Protection