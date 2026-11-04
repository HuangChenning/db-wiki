---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_ARCHIVE_FORMAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.188 LOG\_ARCHIVE\_FORMAT

Use `LOG_ARCHIVE_FORMAT` to specify the default filename format when archiving redo log files.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_ARCHIVE_FORMAT = ` `filename` |
| Default value | Operating system-dependent |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Any string that resolves to a valid filename |
| Basic | No |
| Oracle RAC | Multiple instances can have different values, but identical values are recommended. |

`LOG_ARCHIVE_FORMAT` is applicable only if you are using the redo log in `ARCHIVELOG` mode. Use a text string and variables to specify the default filename format when archiving redo log files. The string generated from this format is appended to the string specified in the `LOG_ARCHIVE_DEST` parameter.

The following variables can be used in the format:

`%s` log sequence number

`%S` log sequence number, zero filled

`%t` thread number

`%T` thread number, zero filled

`%a` activation ID

`%d` database ID

`%r` resetlogs ID that ensures unique names are constructed for the archived log files across multiple incarnations of the database

Using uppercase letters for the variables (for example, `%S`) causes the value to be fixed length and padded to the left with zeros. An example of specifying the archive redo log filename format follows:

```
LOG_ARCHIVE_FORMAT = 'log%t_%s_%r.arc'
```

Archive log file names must contain each of the elements `%s` (sequence), `%t` (thread), and `%r` (resetlogs ID) to ensure that all archive log file names are unique. If the `LOG_ARCHIVE_FORMAT` initialization parameter is set in the parameter file, then make sure the parameter value contains the `%s`, `%t`, and `%r` elements. Otherwise, the following error is displayed at the time of instance startup:

```
ORA-19905: log_archive_format must contain %s, %t and %r
```

Neither `LOG_ARCHIVE_DEST` nor `LOG_ARCHIVE_FORMAT` have to be complete file or directory specifiers themselves; they only need to form a valid file path after the variables are substituted into `LOG_ARCHIVE_FORMAT` and the two parameters are concatenated together.

`LOG_ARCHIVE_FORMAT` is ignored in these cases:

- For archived log files that go to the fast recovery area
- When `LOG_ARCHIVE_DEST[_n]` points to the root of an Oracle ASM disk group (for example, `+DATA`). The directory of a disk group (for example, +DATA/logs) must be specified for the parameter to be honored.

In these cases where `LOG_ARCHIVE_FORMAT` is ignored, an Oracle ASM file name is used. See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG94201) for more information on Oracle ASM file names.

See Also:

- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV90025), [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB-GUID-0FD317D6-1A49-4DB3-A141-D00CB3089E84), and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD326) for more information about this parameter
- Your operating system- specific Oracle documentation for the default value and range of values for `LOG_ARCHIVE_FORMAT`