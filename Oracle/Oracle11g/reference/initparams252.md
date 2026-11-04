---
title: STANDBY_FILE_MANAGEMENT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams252.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_FILE_MANAGEMENT = { MANUAL \| AUTO }` |
| Default value | `MANUAL` |
| Modifiable | `ALTER SYSTEM` |

`STANDBY_FILE_MANAGEMENT` enables or disables automatic standby file management. When automatic standby file management is enabled, operating system file additions and deletions on the primary database are replicated on the standby database. `STANDBY_FILE_MANAGEMENT` is only applicable to physical standby databases.

Values:

- `MANUAL`
	disables automatic standby file management
- `AUTO`
	enables automatic standby file management

Setting `STANDBY_FILE_MANAGEMENT` to `AUTO` causes Oracle to automatically create files on the standby database and, in some cases, overwrite existing files. Care must be taken when setting `STANDBY_FILE_MANAGEMENT` and `DB_FILE_NAME_CONVERT` so that existing standby files will not be accidentally overwritten.

If the standby database is on the same system as the primary database, then ensure that the primary and standby systems do not point to the same files.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for more information about setting this parameter