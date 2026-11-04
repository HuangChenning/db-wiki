---
title: DB_RECOVERY_FILE_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams065.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_RECOVERY_FILE_DEST =` `directory` `\|` `disk group` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

`DB_RECOVERY_FILE_DEST` specifies the default location for the fast recovery area. The fast recovery area contains multiplexed copies of current control files and online redo logs, as well as archived redo logs, flashback logs, and RMAN backups.

Specifying this parameter without also specifying the `DB_RECOVERY_FILE_DEST_SIZE` initialization parameter is not allowed.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV8183) for information on setting up and configuring the fast recovery area
- ["DB\_RECOVERY\_FILE\_DEST\_SIZE"](initparams066.md)