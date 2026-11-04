---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_POLICY_CONTEXTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.15 ALL\_POLICY\_CONTEXTS

`ALL_POLICY_CONTEXTS` describes the driving contexts defined for the synonyms, tables, and views accessible to the current user.

Related Views

- `DBA_POLICY_CONTEXTS` describes all driving contexts in the database.
- `USER_POLICY_CONTEXTS` describes the driving contexts defined for the synonyms, tables, and views owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the synonym, table, or view |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the synonym, table, or view |
| `NAMESPACE` | `VARCHAR2(128)` | `NOT NULL` | Namespace of the driving context |
| `ATTRIBUTE` | `VARCHAR2(128)` | `NOT NULL` | Attribute of the driving context |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the policy context is applied and enforced in all application PDBs (`YES`) or only in the local PDB (`NO`) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the policy context is inherited from the root (`YES`) or not (`NO`) |

See Also:

- " [DBA\_POLICY\_CONTEXTS](DBA_POLICY_CONTEXTS.md) "
- " [USER\_POLICY\_CONTEXTS](USER_POLICY_CONTEXTS.md) "