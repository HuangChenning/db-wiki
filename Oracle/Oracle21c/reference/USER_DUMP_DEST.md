---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_DUMP_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.379 USER\_DUMP\_DEST

`USER_DUMP_DEST` specifies the pathname for a directory where the server will write debugging trace files on behalf of a user process.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `USER_DUMP_DEST = { ` `pathname` `  \|  ` `directory` ` }` |
| Default value | Operating system-dependent |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Any valid local path, directory, or disk |
| Basic | No |

Note:

The `USER_DUMP_DEST` initialization parameter is deprecated.

For example, this directory might be set as follows:

- On MS-DOS: `C:\ORACLE\UTRC`
- On UNIX: `/oracle/utrc`
- On VMS: `DISK$UR3:[ORACLE.UTRC]`

Note:

This parameter is ignored by the diagnosability infrastructure introduced in Oracle Database 11g Release 1 (11.1), which places trace and core files in a location controlled by the `DIAGNOSTIC_DEST` initialization parameter.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL809) for more information about the use of trace files
- Your operating system-specific Oracle documentation for the range of values