---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CONTROL_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.55 CONTROL\_FILES

`CONTROL_FILES` specifies one or more names of control files, separated by commas.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CONTROL_FILES = ` `filename` `  [,  ``filename` ` ] ...`  Note: The control file name can be an OMF (Oracle Managed Files) name. This occurs when the control file is re-created using the `CREATE CONTROLFILE REUSE` statement. |
| Default value | Operating system-dependent |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 1 to 8 filenames |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

Every database has a control file, which contains entries that describe the structure of the database (such as its name, the timestamp of its creation, and the names and locations of its data files and redo files).

Oracle recommends that you multiplex multiple control files on different devices or mirror the file at the operating system level.

See Also:

[Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN11494) for information about specifying control files at database creation