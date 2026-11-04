---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_RECOVERY_FILE_DEST_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.93 DB\_RECOVERY\_FILE\_DEST\_SIZE

`DB_RECOVERY_FILE_DEST_SIZE` specifies (in bytes) the hard limit on the total space to be used by target database recovery files created in the fast recovery area.

| Property | Description |
| --- | --- |
| Parameter type | Big integer |
| Syntax | `DB_RECOVERY_FILE_DEST_SIZE = ` `integer` ` [K \| M \| G]` |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM ... SID='*'` |
| Modifiable in a PDB | No |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

Note that neither block 0 nor the OS block header of each Oracle file is included in this size. Allow an extra 10% for this data when computing the actual disk usage required for the fast recovery area.

See Also:

- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV8183) for information on setting up and configuring the fast recovery area
- " [DB\_RECOVERY\_FILE\_DEST](DB_RECOVERY_FILE_DEST.md) "