---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_POLICY_ATTRIBUTES.html
tags:
  - oracle
  - 12c
  - reference
---

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
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the policy attribute is applied and enforced in all application PDBs (`YES`) or only in the local PDB (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the policy attribute is inherited from the root (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_POLICY\_ATTRIBUTES](DBA_POLICY_ATTRIBUTES.md) "
- " [USER\_POLICY\_ATTRIBUTES](USER_POLICY_ATTRIBUTES.md) "