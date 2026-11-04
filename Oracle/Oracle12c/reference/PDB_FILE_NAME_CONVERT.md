---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PDB_FILE_NAME_CONVERT.html
tags:
  - oracle
  - 12c
  - reference
---

`PDB_FILE_NAME_CONVERT` maps names of existing files to new file names when processing a `CREATE` `PLUGGABLE` `DATABASE` statement, as well as when processing the `ENABLE` `PLUGGABLE` `DATABASE` clause of the `CREATE` `DATABASE` statement, if the `file_name_convert_clause` is not specified and Oracle Managed Files is not enabled.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PDB_FILE_NAME_CONVERT = '` `string1` `' , '` `string2` `' , '` `string3` `' , '` `string4` `' , ...`  Where:  - `string1` is the pattern of the existing filename - `string2` is the pattern of the new filename - `string3` is the pattern of the existing filename - `string4` is the pattern of the new filename  You can enclose each string in single or double quotation marks.  You can specify as many pairs of existing and new replacement strings as required.  Example:  `PDB_FILE_NAME_CONVERT = '/dbs/t1/','/dbs/t1/s','dbs/t2/','dbs/t2/s'` |
| Default value | There is no default value |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

File name patterns specified in this initialization parameter cannot match files or directories managed by Oracle Managed Files.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN13528) for more information about this parameter