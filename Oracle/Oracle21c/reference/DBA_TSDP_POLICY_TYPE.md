---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TSDP_POLICY_TYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.65 DBA\_TSDP\_POLICY\_TYPE

`DBA_TSDP_POLICY_TYPE` shows the Transparent Sensitive Data Protection policy to sensitive column type mapping.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | The Transparent Sensitive Data Protection policy name |
| `SENSITIVE_TYPE` | `VARCHAR2(128)` |  | The sensitive column type name |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG855) for more information about using Transparent Sensitive Data Protection