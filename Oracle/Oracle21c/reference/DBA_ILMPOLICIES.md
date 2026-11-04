---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ILMPOLICIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.101 DBA\_ILMPOLICIES

`DBA_ILMPOLICIES` displays details about Automatic Data Optimization policies in the database.

The view contains common details relevant to all types of Automatic Data Optimization policies, not just details relevant to the data movement-related Automatic Data Optimization policies.

Related View

`USER_ILMPOLICIES` displays details about Automatic Data Optimization policies owned by the user.

Note:

Automatic Data Optimization is supported in Oracle Database 12c Release 2 multitenant environments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `POLICY_NAME` | `VARCHAR2(128)` |  | The name of the Automatic Data Optimization policy is auto-generated |
| `POLICY_TYPE` | `VARCHAR2(13)` |  | Type of the policy. Valid values include `DATAMOVEMENT`. |
| `TABLESPACE` | `VARCHAR2(30)` |  | Tablespace name, in the case of a tablespace-level policy |
| `ENABLED` | `VARCHAR2(6)` |  | Indicates whether the policy is enabled or not |
| `DELETED` | `VARCHAR2(7)` |  | Possible values:  - `YES` - Indicates that the policy associated has been deleted (but shall remain active for this object) - `NO` - Indicates that the policy is active |

Note:

Automatic Data Optimization policies cannot be set on tables with object types or materialized views.

See Also:

" [USER\_ILMPOLICIES](USER_ILMPOLICIES.md) "