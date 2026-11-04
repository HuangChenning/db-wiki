---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_SUPPLEMENTAL_LOGGING.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_SUPPLEMENTAL_LOGGING` provides information about supplemental logging for a pluggable database (PDB) in a multitenant container database (CDB).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `MINIMAL` | `VARCHAR2(3)` |  | Identifies whether minimal supplemental logging is on (`YES` or `NO`) |
| `PRIMARY_KEY` | `VARCHAR2(3)` |  | Identifies whether primary key supplemental logging is on (`YES` or `NO`) |
| `UNIQUE_INDEX` | `VARCHAR2(3)` |  | Identifies whether unique column supplemental logging is on (`YES` or `NO`) |
| `FOREIGN_KEY` | `VARCHAR2(3)` |  | Identifies whether foreign key supplemental logging is on (`YES` or `NO`) |
| `ALL_COLUMN` | `VARCHAR2(3)` |  | Identifies whether all column supplemental logging is on (`YES` or `NO`) |
| `PROCEDURAL` | `VARCHAR2(3)` |  | Identifies whether supplemental logging for procedural replication is on (`YES` or `NO`) |

See Also:

- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SUTIL1582) for more information about supplemental logging
- " [V$DATABASE](V-DATABASE.md) " for information about supplemental logging in a CDB