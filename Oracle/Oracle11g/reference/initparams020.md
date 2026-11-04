---
title: BACKGROUND_DUMP_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams020.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `BACKGROUND_DUMP_DEST = {` `pathname` `\|` `directory` `}` |
| Default value | Operating system-dependent |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Any valid local path, directory, or disk |
| Basic | No |

`BACKGROUND_DUMP_DEST` specifies the pathname (directory or disc) where debugging trace files for the background processes (LGWR, DBWn, and so on) are written during Oracle operations.

An alert file in the directory specified by `BACKGROUND_DUMP_DEST` logs significant database events and messages. Anything that affects the database instance or global database is recorded here. The alert file is a normal text file. Its filename is operating system-dependent. For platforms that support multiple instances, it takes the form `alert_` `sid``.log`, where sid is the system identifier. This file grows slowly, but without limit, so you might want to delete it periodically. You can delete the file even when the database is running.

Note:

This parameter is ignored by the new diagnosability infrastructure introduced in Oracle Database 11g Release 1 (11.1), which places trace and core files in a location controlled by the `DIAGNOSTIC_DEST` initialization parameter.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on setting this parameter and on alert files
- Your operating system-specific Oracle documentation for the default value of this parameter
- ["USER\_DUMP\_DEST"](initparams269.md) for information on setting a destination for server process trace files