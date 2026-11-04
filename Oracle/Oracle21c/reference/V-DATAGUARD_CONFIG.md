---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATAGUARD_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.160 V$DATAGUARD\_CONFIG

`V$DATAGUARD_CONFIG` displays the unique database names defined with the `DB_UNIQUE_NAME` and `LOG_ARCHIVE_CONFIG` initialization parameters, providing a view of the Oracle Data Guard environment from any database in the configuration.

The first row of the view lists the unique database name of the current database that was specified with the `DB_UNIQUE_NAME` initialization parameter. Additional rows reflect the unique database names of the other databases in the configuration that were specified with the `DG_CONFIG` keyword of the `LOG_ARCHIVE_CONFIG` initialization parameter.

| Column | Datatype | Description |
| --- | --- | --- |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | Unique database name |
| `PARENT_DBUN` | `VARCHAR2(30)` | `DB_UNIQUE_NAME` of the parent database, also known as the database that supplies live redo to the destination.  For example, suppose Boston is the `DB_UNIQUE_NAME` of the primary database, Chicago is the `DB_UNIQUE_NAME` of the Far Sync Instance, and Seattle is the `DB_UNIQUE_NAME` of the terminal standby database. Since Boston is the primary database, it has no parent database so the `PARENT_DBUN` for Boston will be `NULL`. Since Boston services Chicago, the `PARENT_DBUN` of Chicago will be Boston. Since Chicago services Seattle, Chicago will be the `PARENT_DBUN` for Seattle. |
| `DEST_ROLE` | `VARCHAR2(17)` | Type of archival destination database:  - `BACKUP` `APPLIANCE` - `FAR` `SYNC` `STANDBY` - `LOGICAL` `STANDBY` - `PHYSICAL` `STANDBY` - `PRIMARY` `DATABASE` - `SNAPSHOT` `STANDBY` |
| `CURRENT_SCN` | `NUMBER` | The SCN up to which the specified database has applied redo |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [DB\_UNIQUE\_NAME](DB_UNIQUE_NAME.md) "
- " [LOG\_ARCHIVE\_CONFIG](LOG_ARCHIVE_CONFIG.md) "