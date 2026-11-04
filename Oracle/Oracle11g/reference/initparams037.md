---
title: CONTROL_FILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams037.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CONTROL_FILES =` `filename` `[,` `filename` `] ...`  Note: The control file name can be an OMF (Oracle Managed Files) name. This occurs when the control file is re-created using the `CREATE CONTROLFILE REUSE` statement. |
| Default value | Operating system-dependent |
| Modifiable | No |
| Range of values | 1 to 8 filenames |
| Basic | Yes |
| Oracle RAC | Multiple instances must have the same value. |

Every database has a control file, which contains entries that describe the structure of the database (such as its name, the timestamp of its creation, and the names and locations of its datafiles and redo files). `CONTROL_FILES` specifies one or more names of control files, separated by commas.

Oracle recommends that you multiplex multiple control files on different devices or mirror the file at the operating system level.