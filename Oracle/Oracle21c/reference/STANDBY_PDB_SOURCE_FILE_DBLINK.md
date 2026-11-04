---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STANDBY_PDB_SOURCE_FILE_DBLINK.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.352 STANDBY\_PDB\_SOURCE\_FILE\_DBLINK

`STANDBY_PDB_SOURCE_FILE_DBLINK` specifies the name of a database link that will be used to try to copy the datafiles from a source PDB to which the database link points.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_PDB_SOURCE_FILE_DBLINK = database-link` |
| Default value | NULL |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | Different values can be set on different instances. |

In Oracle Database releases prior to Oracle Database 18c, if a PDB was created by cloning a PDB from the same CDB (a local clone), on a standby the datafiles were automatically copied from the source PDB. However, when the PDB was created as a remote clone, the user was responsible for copying datafiles to the Oracle Managed Files (OMF) location on the standby.

To address that deficiency, the `STANDBY_PDB_SOURCE_FILE_DBLINK` parameter specifies the name of a database link that will be used to try to copy the datafiles from a source PDB to which the database link points. The file copy is done only if the database link points to the source PDB and the source PDB is open in read only mode. Otherwise, the user is still responsible for copying datafiles to the OMF location on the standby.

This parameter can also be used to try to copy files in cases where the source PDB's files are not present on the standby. For example, the source PDB could have been created with standbys=NONE. In this case, the `STANDBY_PDB_SOURCE_FILE_DBLINK` parameter can enable the standby to copy files from the primary if there is a database link set up to the primary.

See Also:

" [STANDBY\_PDB\_SOURCE\_FILE\_DIRECTORY](STANDBY_PDB_SOURCE_FILE_DIRECTORY.md) "