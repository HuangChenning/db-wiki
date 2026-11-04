---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_FILE_NAME_CONVERT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.196 LOG\_FILE\_NAME\_CONVERT

`LOG_FILE_NAME_CONVERT` converts the filename of a new log file on the primary database to the filename of a log file on the standby database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_FILE_NAME_CONVERT = '` `string1` `' , '` `string2` `' , '` `string3` `' , '` `string4` `' , ...`  Where:  - `string1` is the pattern of the primary database filename - `string2` is the pattern of the standby database filename - `string3` is the pattern of the primary database filename - `string4` is the pattern of the standby database filename  You can enclose each string in single or double quotation marks.  You can specify as many pairs of primary and standby replacement strings as required.  Example:  `LOG_FILE_NAME_CONVERT = '/dbs/t1/','/dbs/t1/s','dbs/t2/','dbs/t2/s'` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

If you add a log file to the primary database, you must add a corresponding file to the standby database.

Set the value of this parameter to one or more pairs of strings. The first string is the pattern found in the log file names on the primary database. The second string is the pattern found in the log file names on the standby database.

When the standby database is updated, this parameter converts the log file name on the primary database to the log file name on the standby database. The file must exist on the standby database and must be writable or the recovery process will halt with an error.

If you specify an odd number of strings (the last string has no corresponding replacement string), an error is signalled during startup. If the filename being converted matches more than one pattern in the pattern/replace string list, the first matched pattern takes effect. There is no limit on the number of pairs that you can specify in this parameter (other than the hard limit of the maximum length of multivalue parameters).

You should also use `LOG_FILE_NAME_CONVERT` to rename the logfiles in the clone control file when setting up the clone database during tablespace point-in-time recovery.

Note:

The `LOG_FILE_NAME_CONVERT` parameter applies only to online logs (not to archived logs).

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB4985)