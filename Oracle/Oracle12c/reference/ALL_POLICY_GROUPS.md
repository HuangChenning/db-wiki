---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_POLICY_GROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_POLICY_GROUPS` describes the policy groups defined for the synonyms, tables, and views accessible to the current user.

Related Views

- `DBA_POLICY_GROUPS` describes all policy groups in the database.
- `USER_POLICY_GROUPS` describes the policy groups defined for the synonyms, tables, and views owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the synonym, table, or view |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the synonym, table, or view |
| `POLICY_GROUP` | `VARCHAR2(128)` |  | Name of the policy group |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the policy group is applied and enforced in all application PDBs (`YES`) or only in the local PDB (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the policy group is inherited from the root (`YES`) or not (`NO`)  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |

See Also:

- " [DBA\_POLICY\_GROUPS](DBA_POLICY_GROUPS.md) "
- " [USER\_POLICY\_GROUPS](USER_POLICY_GROUPS.md) "