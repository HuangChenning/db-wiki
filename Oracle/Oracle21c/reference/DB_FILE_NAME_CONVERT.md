---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_FILE_NAME_CONVERT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.82 DB\_FILE\_NAME\_CONVERT

`DB_FILE_NAME_CONVERT` is useful for creating a duplicate database for recovery purposes. It converts the filename of a new datafile on the primary database to a filename on the standby database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_FILE_NAME_CONVERT = '` `string1` `' , '` `string2` `' , '` `string3` `' , '` `string4` `' , ...`  Where:  - `string1` is the pattern of the primary database filename - `string2` is the pattern of the standby database filename - `string3` is the pattern of the primary database filename - `string4` is the pattern of the standby database filename  You can enclose each string in single or double quotation marks.  You can specify as many pairs of primary and standby replacement strings as required. However, starting with Oracle Database 12c Release 2 (12.2), Oracle recommends that you limit the number of pairs to 99.  Example:  `DB_FILE_NAME_CONVERT = '/dbs/t1/','/dbs/t1/s','dbs/t2/','dbs/t2/s'` |
| Default value | There is no default value. |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

If you add a datafile to the primary database, you must add a corresponding file to the standby database. When the standby database is updated, this parameter converts the datafile name on the primary database to the datafile name on the standby database. The file on the standby database must exist and be writable, or the recovery process will halt with an error.

Set the value of this parameter to one or more pairs of strings. The first string in a pair is the pattern found in the datafile names on the primary database. The second string in a pair is the pattern found in the datafile names on the standby database.

If you specify an odd number of strings (the last string has no corresponding replacement string), an error is returned during startup. If the filename being converted matches more than one pattern in the pattern/replace string list, the first matched pattern takes effect. There is no limit on the number of pairs that you can specify in this parameter (other than the hard limit of the maximum length of multivalue parameters). However, starting with Oracle Database 12c Release 2 (12.2), Oracle recommends that you limit the number of pairs to 99.

You can also use `DB_FILE_NAME_CONVERT` to rename the datafiles in the clone control file when setting up a clone database during tablespace point-in-time recovery.

See Also:

- [Oracle Database Backup and Recovery User’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=BRADV8001) for more information about database backup and recovery
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB00010) for more information about Oracle Data Guard