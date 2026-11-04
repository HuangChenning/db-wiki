---
title: ALL_POLICIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2010.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_POLICIES` describes all Oracle Virtual Private Database (VPD) security policies for objects accessible to the current user. A security policy is a list of security requirements and rules that regulate access to those database objects.

Related Views

- `DBA_POLICIES` describes all Oracle Virtual Private Database (VPD) security policies in the database.
- `USER_POLICIES` describes all Oracle Virtual Private Database (VPD) security policies associated with objects owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the synonym, table, or view |
| `OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the synonym, table, or view |
| `POLICY_GROUP` | `VARCHAR2(30)` | `NOT NULL` | Name of the policy group |
| `POLICY_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the policy |
| `PF_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the policy function |
| `PACKAGE` | `VARCHAR2(30)` |  | Name of the package containing the policy function |
| `FUNCTION` | `VARCHAR2(30)` | `NOT NULL` | Name of the policy function |
| `SEL` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to queries on the object (`YES`) or not (`NO`) |
| `INS` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to `INSERT` statements on the object (`YES`) or not (`NO`) |
| `UPD` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to `UPDATE` statements on the object (`YES`) or not (`NO`) |
| `DEL` | `VARCHAR2(3)` |  | Indicates whether the policy is applied to `DELETE` statements on the object (`YES`) or not (`NO`) |
| `IDX` | `VARCHAR2(3)` |  | Indicates whether the policy is enforced for index maintenance on the object (`YES`) or not (`NO`) |
| `CHK_OPTION` | `VARCHAR2(3)` |  | Indicates whether the check option is enforced for the policy (`YES`) or not (`NO`) |
| `ENABLE` | `VARCHAR2(3)` |  | Indicates whether the policy is enabled (`YES`) or disabled (`NO`) |
| `STATIC_POLICY` | `VARCHAR2(3)` |  | Indicates whether the policy is static (`YES`) or not (`NO`) |
| `POLICY_TYPE` | `VARCHAR2(24)` |  | Policy type: - `STATIC` - `SHARED_STATIC` - `CONTEXT_SENSITIVE` - `SHARED_CONTEXT_SENSITIVE` - `DYNAMIC` |
| `LONG_PREDICATE` | `VARCHAR2(3)` |  | Indicates whether the policy function can return a maximum of 32 KB of predicate (`YES`) or not (`NO`). If `NO`, the default maximum predicate size is `4000` bytes. |

See Also:

- ["DBA\_POLICIES"](statviews_4182.md)
- ["USER\_POLICIES"](statviews_5397.md)
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) for an overview of security policies and fine-grained access control
- [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/toc.htm) for information about implementing security policies
- The `DBMS_RLS` package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information on administering security policies