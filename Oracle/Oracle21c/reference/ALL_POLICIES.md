---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_POLICIES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.13 ALL\_POLICIES

`ALL_POLICIES` describes all Oracle Virtual Private Database (VPD) security policies for objects accessible to the current user. A security policy is a list of security requirements and rules that regulate row level access to those database objects.

Related Views

- `DBA_POLICIES` describes all Oracle Virtual Private Database (VPD) security policies in the database.
- `USER_POLICIES` describes all Oracle Virtual Private Database (VPD) security policies associated with objects owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the synonym, table, or view |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the synonym, table, or view |
| `POLICY_GROUP` | `VARCHAR2(128)` |  | Name of the policy group |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the policy |
| `PF_OWNER` | `VARCHAR2(128)` |  | Owner of the policy function |
| `PACKAGE` | `VARCHAR2(128)` |  | Name of the package containing the policy function |
| `FUNCTION` | `VARCHAR2(128)` |  | Name of the policy function |
| `SEL` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to queries on the object (`YES`) or not (`NO`) |
| `INS` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to `INSERT` statements on the object (`YES`) or not (`NO`) |
| `UPD` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to `UPDATE` statements on the object (`YES`) or not (`NO`) |
| `DEL` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to `DELETE` statements on the object (`YES`) or not (`NO`) |
| `IDX` | `VARCHAR2(3)` |  | Indicates whether the policy is enforced for index maintenance on the object (`YES`) or not (`NO`) |
| `CHK_OPTION` | `VARCHAR2(3)` |  | Indicates whether the check option is enforced for the policy (`YES`) or not (`NO`) |
| `ENABLE` | `VARCHAR2(3)` |  | Indicates whether the policy is enabled (`YES`) or disabled (`NO`) |
| `STATIC_POLICY` | `VARCHAR2(3)` |  | Indicates whether the policy is static (`YES`) or not (`NO`). This column is obsolete because information about static policies is shown in the `POLICY_TYPE` column. |
| `POLICY_TYPE` | `VARCHAR2(24)` |  | Policy type:  - `STATIC` - `SHARED_STATIC` - `CONTEXT_SENSITIVE` - `SHARED_CONTEXT_SENSITIVE` - `DYNAMIC` |
| `LONG_PREDICATE` | `VARCHAR2(3)` |  | Indicates whether the policy function can return a maximum of 32 KB of predicate (`YES`) or not (`NO`). If `NO`, the default maximum predicate size is `4000` bytes. |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the policy is applied and enforced in all application PDBs (`YES`) or only in the local PDB (`NO`) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the policy is inherited from the root (`YES`) or not (`NO`) |

See Also:

- " [DBA\_POLICIES](DBA_POLICIES.md) "
- " [USER\_POLICIES](USER_POLICIES.md) "
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG001) for more information about security policies
- The `DBMS_RLS` package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS052) for information on administering security policies