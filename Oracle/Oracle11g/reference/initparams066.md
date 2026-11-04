---
title: DB_RECOVERY_FILE_DEST_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams066.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_RECOVERY_FILE_DEST_SIZE =` `integer` `[K \| M \| G]` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

`DB_RECOVERY_FILE_DEST_SIZE` specifies (in bytes) the hard limit on the total space to be used by target database recovery files created in the fast recovery area.

Note that neither block 0 nor the OS block header of each Oracle file is included in this size. Allow an extra 10% for this data when computing the actual disk usage required for the fast recovery area.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmconfb.htm#BRADV8183) for information on setting up and configuring the fast recovery area
- ["DB\_RECOVERY\_FILE\_DEST"](initparams065.md)