---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SQLSET.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.81 ALL\_SQLSET

`ALL_SQLSET` displays information about all SQL tuning sets accessible to the current user.

Related Views

- `DBA_SQLSET` displays information about all SQL tuning sets in the database.
- `USER_SQLSET` displays information about the SQL tuning sets owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the SQL tuning set |
| `ID` | `NUMBER` | `NOT NULL` | SQL tuning set identifier |
| `CON_DBID` | `NUMBER` | `NOT NULL` | The database ID of the PDB |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the SQL tuning set |
| `DESCRIPTION` | `VARCHAR2(256)` |  | Description of the SQL tuning set |
| `CREATED` | `DATE` |  | Date the SQL tuning set was created |
| `LAST_MODIFIED` | `DATE` |  | Date the SQL tuning set was last modified |
| `STATEMENT_COUNT` | `NUMBER` |  | Number of statements in the SQL tuning set |

See Also:

- " [DBA\_SQLSET](DBA_SQLSET.md) "
- " [USER\_SQLSET](USER_SQLSET.md) "