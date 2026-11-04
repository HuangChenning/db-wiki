---
title: LOG_FILE_NAME_CONVERT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams137.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_FILE_NAME_CONVERT = '` `string1` `' , '` `string2` `' , '` `string3` `' , '` `string4` `' , ...`  Where:  - `string1` is the pattern of the primary database filename - `string2` is the pattern of the standby database filename - `string3` is the pattern of the primary database filename - `string4` is the pattern of the standby database filename  You can use as many pairs of primary and standby replacement strings as required. You can use single or double quotation marks.  The following are example settings that are acceptable:  `LOG_FILE_NAME_CONVERT = '/dbs/t1/','/dbs/t1/s','dbs/t2/ ','dbs/t2/s_'` |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION` |
| Basic | No |

`LOG_FILE_NAME_CONVERT` converts the filename of a new log file on the primary database to the filename of a log file on the standby database. If you add a log file to the primary database, you must add a corresponding file to the standby database.

If you specify an odd number of strings (the last string has no corresponding replacement string), an error is signalled during startup. If the filename being converted matches more than one pattern in the pattern/replace string list, the first matched pattern takes effect. There is no limit on the number of pairs that you can specify in this parameter (other than the hard limit of the maximum length of multivalue parameters).

When the standby database is updated, this parameter converts the log file name on the primary database to the log file name on the standby database. The file must exist on the standby database and must be writable or the recovery process will halt with an error.

The first string is the pattern found in the log file names on the primary database. The second string is the pattern found in the log file names on the standby database.

You should also use `LOG_FILE_NAME_CONVERT` to rename the logfiles in the clone control file when setting up the clone database during tablespace point-in-time recovery.

Note:

The `LOG_FILE_NAME_CONVERT` parameter applies only to online logs (not to archived logs).