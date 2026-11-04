---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STANDBY_PDB_SOURCE_FILE_DIRECTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.353 STANDBY\_PDB\_SOURCE\_FILE\_DIRECTORY

`STANDBY_PDB_SOURCE_FILE_DIRECTORY` specifies a directory location on the standby where source datafiles for instantiating the standby PDB may be found.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_PDB_SOURCE_FILE_DIRECTORY = datafiles-directory` |
| Default value | NULL |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Different values can be set on different instances. |

In Oracle Database releases prior to Oracle Database 18c, if a PDB was plugged into a CDB, on a standby, the datafiles were expected to be in PDB's Oracle Managed Files (OMF) directory location. If they were not found there, the user had to copy the datafiles to the OMF location and then restart redo apply on the standby.

To address that deficiency, the `STANDBY_PDB_SOURCE_FILE_DIRECTORY` specifies a directory location on the standby where source datafiles for instantiating the PDB may be found. If the datafiles are not found there, an attempt will be made to locate them in the OMF location on the standby.

This parameter can also be used to try to copy files in cases where the source PDB's files are not present on the standby. For example, the source PDB could have been created with standbys=NONE. In this case, the `STANDBY_PDB_SOURCE_FILE_DIRECTORY` parameter can enable the standby to copy files from a location if they are made available.

See Also:

" [STANDBY\_PDB\_SOURCE\_FILE\_DBLINK](STANDBY_PDB_SOURCE_FILE_DBLINK.md) "