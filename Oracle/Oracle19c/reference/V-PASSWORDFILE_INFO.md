---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-PASSWORDFILE_INFO.html
tags:
  - oracle
  - 19c
  - reference
---

## 8.111 V$PASSWORDFILE\_INFO

`V$PASSWORDFILE_INFO` provides information about the database password file.

This view can be queried from the root or from a pluggable database (PDB) in a multitenant container database (CDB). When queried, this view always returns one row.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE_NAME` | `VARCHAR2(513)` | Fully qualified password file name/location. |
| `FORMAT` | `VARCHAR2(6)` | Shows the format of the password file:  - `LEGACY` - `12` - `12.2` |
| `IS_ASM` | `VARCHAR2(5)` | Indicates where the password file is stored. Possible values:  - `TRUE`: The password file is stored in Oracle ASM. - `FALSE`: The password file is stored in the operating system file system. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Because there is only one password file for a CDB that is common for the entire CDB, the only value possible for `CON_ID` is `0` for this view. |

Note:

If the database password file name or location was recently changed, and you do not see the change reflected in this view, you can run the following SQL statement:

```
SQL> ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE;
```

This statement flushes the metadata cache and updates the database to use the new password file. It also updates this view with the current password file information.