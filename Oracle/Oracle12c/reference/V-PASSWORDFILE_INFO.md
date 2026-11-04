---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-PASSWORDFILE_INFO.html
tags:
  - oracle
  - 12c
  - reference
---

`V$PASSWORDFILE_INFO` provides information about the database password file.

This view can be queried from the root or from a pluggable database (PDB) in a multitenant container database (CDB). When queried, this view always returns one row.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_NAME` | `VARCHAR2(513)` | Fully qualified password file name/location. |
| `FORMAT` | `VARCHAR2(6)` | Shows the format of the password file. Possible values include:  - Legacy - 12 - 12.2 |
| `IS_ASM` | `VARCHAR2(5)` | Indicates where the password file is stored. Possible values:  - `TRUE`: The password file is stored in Oracle ASM. - `FALSE`: The password file is stored in the operating system file system. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Because there is only one password file for a CDB that is common for the entire CDB, the only value possible for `CON_ID` is `0` for this view. |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).