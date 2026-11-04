---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_POLICY_ATTRIBUTES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.14 ALL\_POLICY\_ATTRIBUTES

`ALL_POLICY_ATTRIBUTES` lists the attribute associations {Namespaces, Attributes} of context-sensitive and shared context-sensitive Oracle Virtual Private Database (VPD) policies for objects accessible to the current user.

Related Views

- `DBA_POLICY_ATTRIBUTES` lists the attribute associations {Namespaces, Attributes} of all context-sensitive and shared context-sensitive Oracle Virtual Private Database (VPD) policies in the database.
- `USER_POLICY_ATTRIBUTES` lists the attribute associations {Namespaces, Attributes} of all context-sensitive and shared-context sensitive Oracle Virtual Private Database (VPD) policies for synonyms, tables, or views owned by the user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the synonym, table, or view |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the synonym, table, or view |
| `POLICY_GROUP` | `VARCHAR2(128)` |  | Name of the policy group |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the policy |
| `NAMESPACE` | `VARCHAR2(128)` |  | Name of the local application context |
| `ATTRIBUTE` | `VARCHAR2(128)` |  | Name of the attribute |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the policy attribute is applied and enforced in all application PDBs (`YES`) or only in the local PDB (`NO`) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the policy attribute is inherited from the root (`YES`) or not (`NO`) |

See Also:

- " [DBA\_POLICY\_ATTRIBUTES](DBA_POLICY_ATTRIBUTES.md) "
- " [USER\_POLICY\_ATTRIBUTES](USER_POLICY_ATTRIBUTES.md) "