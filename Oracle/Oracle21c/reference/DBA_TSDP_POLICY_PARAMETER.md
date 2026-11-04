---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TSDP_POLICY_PARAMETER.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.63 DBA\_TSDP\_POLICY\_PARAMETER

`DBA_TSDP_POLICY_PARAMETER` shows the parameter-value pairs for the condition of the Transparent Sensitive Data Protection policy.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | The name of the Transparent Sensitive Data Protection policy |
| `SUB_POLICY` | `NUMBER` | `NOT NULL` | The sub policy of the Transparent Sensitive Data Protection policy |
| `PARAMETER` | `VARCHAR2(128)` |  | The parameter for the Transparent Sensitive Data Protection sub policy |
| `VALUE` | `VARCHAR2(4000)` |  | The value of the parameter |
| `DEFAULT_OPTION` | `VARCHAR2(5)` |  | Indicates whether this is the default option for the policy:  - `TRUE`: This is the default option for the policy - `FALSE`: This is not the default option for the policy |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG855) for more information about using Transparent Sensitive Data Protection