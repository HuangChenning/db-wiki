---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SEC_RELEVANT_COLS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.70 ALL\_SEC\_RELEVANT\_COLS

`ALL_SEC_RELEVANT_COLS` describes the security relevant columns of the security policies for the tables and views accessible to the current user.

Related Views

- `DBA_SEC_RELEVANT_COLS` describes the security relevant columns of all security policies in the database.
- `USER_SEC_RELEVANT_COLS` describes the security relevant columns of the security policies for the tables and views owned by the current user. This view does not display the `OBJECT_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_OWNER` | `VARCHAR2(128)` |  | Owner of the table or view |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the table or view |
| `POLICY_GROUP` | `VARCHAR2(128)` |  | Name of the policy group |
| `POLICY_NAME` | `VARCHAR2(128)` |  | Name of the policy |
| `SEC_REL_COLUMN` | `VARCHAR2(128)` |  | Name of the security relevant column |
| `COLUMN_OPTION` | `VARCHAR2(8)` |  | Option of the security relevant column:  - `NONE` - `ALL_ROWS` |
| `COMMON` | `VARCHAR2(3)` |  | Indicates whether the policy security relevant column is applied and enforced in all application PDBs (`YES`) or only in the local PDB (`NO`) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the policy security relevant column is inherited from the root (`YES`) or not (`NO`) |

See Also:

- " [DBA\_SEC\_RELEVANT\_COLS](DBA_SEC_RELEVANT_COLS.md) "
- " [USER\_SEC\_RELEVANT\_COLS](USER_SEC_RELEVANT_COLS.md) "