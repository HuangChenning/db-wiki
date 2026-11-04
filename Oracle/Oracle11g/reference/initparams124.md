---
title: LOG_ARCHIVE_DEST
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams124.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_ARCHIVE_DEST =` `filespec` |
| Default value | Null |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Any valid path or device name, except raw partitions |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

For Enterprise Edition users, this parameter has been deprecated in favor of the `LOG_ARCHIVE_DEST_` `n` parameters. If Oracle Enterprise Edition is not installed or it is installed, but you have not specified any `LOG_ARCHIVE_DEST_` `n` parameters, this parameter is valid.

`LOG_ARCHIVE_DEST` is applicable only if you are running the database in `ARCHIVELOG` mode or are recovering a database from archived redo logs. `LOG_ARCHIVE_DEST` is incompatible with the `LOG_ARCHIVE_DEST_` `n` parameters, and must be defined as the null string ("") or (' ') when any `LOG_ARCHIVE_DEST_` `n` parameter has a value other than a null string. Use a text string to specify the default location and root of the disk file or tape device when archiving redo log files. (Archiving to tape is not supported on all operating systems.) The value cannot be a raw partition.

If `LOG_ARCHIVE_DEST` is not explicitly defined and all the `LOG_ARCHIVE_DEST_` `n` parameters have null string values, `LOG_ARCHIVE_DEST` is set to an operating system-specific default value on instance startup.

To override the destination that this parameter specifies, either specify a different destination for manual archiving or use the SQL\*Plus statement `ARCHIVE LOG START` `filespec` for automatic archiving, where `filespec` is the new archive destination. To permanently change the destination, use the statement `ALTER SYSTEM SET LOG_ARCHIVE_DEST =` `filespec`, where `filespec` is the new archive destination.

Neither `LOG_ARCHIVE_DEST` nor `LOG_ARCHIVE_FORMAT` have to be complete file or directory specifiers themselves; they only need to form a valid file path after the variables are substituted into `LOG_ARCHIVE_FORMAT` and the two parameters are concatenated together.

See Also:

- [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm)
- ["LOG\_ARCHIVE\_DUPLEX\_DEST"](initparams127.md), ["LOG\_ARCHIVE\_MIN\_SUCCEED\_DEST"](initparams131.md), and ["V$ARCHIVE\_DEST"](dynviews_1012.md) for more information on setting this parameter
- Your Oracle operating system-specific documentation for the default value and for an example of how to specify the destination path or filename using `LOG_ARCHIVE_DEST`