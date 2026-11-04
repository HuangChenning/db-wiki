---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SQLSET_REFERENCES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.84 ALL\_SQLSET\_REFERENCES

`ALL_SQLSET_REFERENCES` describes whether or not the SQL tuning sets accessible to the current user are active.

Related Views

- `DBA_SQLSET_REFERENCES` describes whether or not all SQL tuning sets in the database are active. A SQL tuning set cannot be dropped if it is referenced.
- `USER_SQLSET_REFERENCES` describes whether or not the SQL tuning sets owned by the current user are active.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SQLSET_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the SQL tuning set |
| `SQLSET_OWNER` | `VARCHAR2(128)` |  | User name of SQL tuning set owner |
| `SQLSET_ID` | `NUMBER` | `NOT NULL` | Identifier of the SQL tuning set |
| `ID` | `NUMBER` | `NOT NULL` | Reference identifier |
| `OWNER` | `VARCHAR2(128)` |  | User who registered to use the SQL tuning set |
| `DESCRIPTION` | `VARCHAR2(256)` |  | Description of the usage of the SQL tuning set |
| `CREATED` | `DATE` |  | Date the reference was created |

See Also:

- " [DBA\_SQLSET\_REFERENCES](DBA_SQLSET_REFERENCES.md) "
- " [USER\_SQLSET\_REFERENCES](USER_SQLSET_REFERENCES.md) "