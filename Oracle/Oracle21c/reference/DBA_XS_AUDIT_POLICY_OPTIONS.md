---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_XS_AUDIT_POLICY_OPTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.148 DBA\_XS\_AUDIT\_POLICY\_OPTIONS

`DBA_XS_AUDIT_POLICY_OPTIONS` describes auditing options defined under all audit policies specific to Oracle Database Real Application Security.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the audit policy |
| `AUDIT_CONDITION` | `VARCHAR2(4000)` |  | Condition associated with the audit policy |
| `AUDIT_OPTION` | `VARCHAR2(128)` |  | Auditing option defined in the audit policy |
| `CONDITION_EVAL_OPT` | `VARCHAR2(9)` |  | Evaluation option associated with the audit policy's condition. The possible values are `STATEMENT`, `SESSION`, `INSTANCE`, `NONE`. |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the audit policy is a common audit policy (`YES`) or local (`NO`). The value is `NULL` in non-CDBs. |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about auditing