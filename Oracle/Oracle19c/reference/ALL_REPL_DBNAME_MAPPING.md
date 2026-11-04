---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_REPL_DBNAME_MAPPING.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.29 ALL\_REPL\_DBNAME\_MAPPING

`ALL_REPL_DBNAME_MAPPING` provides details about the database name mapping in replication for the current user.

Related View

`DBA_REPL_DBNAME_MAPPING` provides details about the database name mapping in replication.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_ROOT_NAME` | `VARCHAR2(128)` |  | The fully qualified global name of the root in a multitenant container database (CDB) where the changes originated |
| `SOURCE_DATABASE_NAME` | `VARCHAR2(128)` |  | The fully qualified global name of the pluggable database (PDB) where the changes originated |
| `SOURCE_CONTAINER_NAME` | `VARCHAR2(128)` |  | The container name of the database where the changes originated |

See Also:

" [DBA\_REPL\_DBNAME\_MAPPING](DBA_REPL_DBNAME_MAPPING.md) "