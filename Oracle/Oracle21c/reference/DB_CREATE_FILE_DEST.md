---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_CREATE_FILE_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.78 DB\_CREATE\_FILE\_DEST

`DB_CREATE_FILE_DEST` specifies the default location for Oracle-managed datafiles.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_CREATE_FILE_DEST = ` `directory` `  \|  ` `disk group` |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | Yes |

This location is also used as the default location for Oracle-managed control files and online redo logs if none of the `DB_CREATE_ONLINE_LOG_DEST_` `n` initialization parameters are specified.

If a file system directory is specified as the default location, then the directory must already exist; Oracle does not create it. The directory must have appropriate permissions that allow Oracle to create files in it. Oracle generates unique names for the files, and a file thus created is an Oracle Managed File.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN003) for more information on setting this parameter and on Oracle Managed Files