---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/BACKGROUND_DUMP_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.32 BACKGROUND\_DUMP\_DEST

`BACKGROUND_DUMP_DEST` specifies the pathname (directory or disc) where debugging trace files for the background processes (LGWR, DBWn, and so on) are written during Oracle operations.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `BACKGROUND_DUMP_DEST = { ` `pathname` `  \|  ` `directory` ` }` |
| Default value | Operating system-dependent |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Any valid local path, directory, or disk |
| Basic | No |

Note:

The `BACKGROUND_DUMP_DEST` parameter is deprecated in Oracle Database 12c Release 1 (12.1.0.1).

An alert log in the directory specified by `BACKGROUND_DUMP_DEST` logs significant database events and messages. Anything that affects the database instance or global database is recorded here. The alert log is a normal text file. Its file name is operating system-dependent. For platforms that support multiple instances, it takes the form `alert_` `sid``.log`, where sid is the system identifier. This file grows slowly, but without limit, so you might want to delete it periodically. You can delete the file even when the database is running.

Note:

This parameter is ignored by the diagnosability infrastructure introduced in Oracle Database 11g Release 1 (11.1), which places trace and core files in a location controlled by the `DIAGNOSTIC_DEST` initialization parameter.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11008) for more information on the DIAGNOSTIC\_DEST initialization parameter
- " [USER\_DUMP\_DEST](USER_DUMP_DEST.md) " for information on setting a destination for server process trace files