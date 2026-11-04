---
title: DB_CREATE_ONLINE_LOG_DEST_n
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams054.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_CREATE_ONLINE_LOG_DEST_[1 \| 2 \| 3 \| 4 \| 5] =` `directory` `\|` `disk group` |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | Yes |

`DB_CREATE_ONLINE_LOG_DEST_` `n` (where `n` = 1, 2, 3,... 5) specifies the default location for Oracle-managed control files and online redo logs. If more than one `DB_CREATE_ONLINE_LOG_DEST_` `n` parameter is specified, then the control file or online redo log is multiplexed across the locations of the other `DB_CREATE_ONLINE_LOG_DEST_` `n` parameters. One member of each online redo log is created in each location, and one control file is created in each location.

Specifying at least two parameters provides greater fault tolerance for the control files and online redo logs if one of the locations should fail.

If a file system directory is specified as the default location, then the directory must already exist; Oracle does not create it. The directory must have appropriate permissions that allow Oracle to create files in it. Oracle generates unique names for the files, and a file thus created is an Oracle Managed File.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/omf.htm#ADMIN003) for more information on setting this parameter and on Oracle Managed Files