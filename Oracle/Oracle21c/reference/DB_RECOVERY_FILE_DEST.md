---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_RECOVERY_FILE_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.92 DB\_RECOVERY\_FILE\_DEST

`DB_RECOVERY_FILE_DEST` specifies the default location for the fast recovery area.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_RECOVERY_FILE_DEST = ` `directory` `  \|  ` `disk group` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Modifiable in a PDB | No |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

The fast recovery area contains multiplexed copies of current control files and online redo logs, as well as archived redo logs, flashback logs, and RMAN backups.

Specifying this parameter without also specifying the `DB_RECOVERY_FILE_DEST_SIZE` initialization parameter is not allowed.

See Also:

- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV8183) for information on setting up and configuring the fast recovery area
- " [DB\_RECOVERY\_FILE\_DEST\_SIZE](DB_RECOVERY_FILE_DEST_SIZE.md) "