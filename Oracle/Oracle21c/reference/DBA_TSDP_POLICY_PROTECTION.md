---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TSDP_POLICY_PROTECTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.64 DBA\_TSDP\_POLICY\_PROTECTION

`DBA_TSDP_POLICY_PROTECTION` shows the list of columns that have been protected through Transparent Sensitive Data Protection.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEMA_NAME` | `VARCHAR2(128)` | `NOT NULL` | The schema containing the sensitive data |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | The table containing the sensitive column |
| `COLUMN_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the sensitive column |
| `TSDP_POLICY` | `VARCHAR2(128)` |  | The TSDP policy name based on which the column protection was enabled |
| `SECURITY_FEATURE` | `VARCHAR2(12)` |  | The security feature enabled on the sensitive column |
| `SECURITY_FEATURE_POLICY` | `VARCHAR2(128)` | `NOT NULL` | Name of the underlying Oracle security feature policy |
| `SUBPOLICY#` | `NUMBER` | `NOT NULL` | The subpolicy of the Transparent Sensitive Data Protection policy based on which protection has been enabled |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG855) for more information about using Transparent Sensitive Data Protection