---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STANDBY_FILE_MANAGEMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.351 STANDBY\_FILE\_MANAGEMENT

`STANDBY_FILE_MANAGEMENT` enables or disables automatic standby file management.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_FILE_MANAGEMENT = { MANUAL \| AUTO }` |
| Default value | `MANUAL` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

When automatic standby file management is enabled, operating system file additions and deletions on the primary database are replicated on the standby database. `STANDBY_FILE_MANAGEMENT` is only applicable to physical standby databases.

Values

- `MANUAL`
	Disables automatic standby file management
- `AUTO`
	Enables automatic standby file management

Setting `STANDBY_FILE_MANAGEMENT` to `AUTO` causes Oracle to automatically create files on the standby database and, in some cases, overwrite existing files. Care must be taken when setting `STANDBY_FILE_MANAGEMENT` and `DB_FILE_NAME_CONVERT` so that existing standby files will not be accidentally overwritten.

If the standby database is on the same system as the primary database, then ensure that the primary and standby systems do not point to the same files.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB4785) for more information about setting this parameter