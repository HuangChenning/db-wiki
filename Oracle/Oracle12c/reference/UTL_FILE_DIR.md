---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/UTL_FILE_DIR.html
tags:
  - oracle
  - 12c
  - reference
---

`UTL_FILE_DIR` lets you specify one or more directories that Oracle should use for PL/SQL file I/O.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `UTL_FILE_DIR = ` `pathname` |
| Default value | There is no default value. |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | Any valid directory path |
| Basic | No |

If you are specifying multiple directories, you must repeat the `UTL_FILE_DIR` parameter for each directory on separate lines of the initialization parameter file.

All users can read or write to all files specified by this parameter. Therefore all PL/SQL users must be trusted with the information in the directories specified by this parameter.

Note:

If you list multiple values, all entries of this parameter must be on contiguous lines of the parameter file. If you separate them with other parameters, Oracle will read only the last (contiguous) lines.

Note:

The `UTL_FILE_DIR` initialization parameter is deprecated in Oracle Database 12c Release 2 (12.2.0.1), and may be desupported in a future release.

In the past, accessible directories for PL/SQL file I/O were specified in the initialization file using the `UTL_FILE_DIR` parameter. However, `UTL_FILE_DIR` access is no longer recommended. Oracle recommends that you instead use the directory object feature, which replaces `UTL_FILE_DIR`. Directory objects offer more flexibility and granular control to the UTL\_FILE application administrator, can be maintained dynamically (that is, without shutting down the database), and are consistent with other Oracle tools.