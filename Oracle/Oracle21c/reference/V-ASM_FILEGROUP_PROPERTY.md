---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_FILEGROUP_PROPERTY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.65 V$ASM\_FILEGROUP\_PROPERTY

`V$ASM_FILEGROUP_PROPERTY` describes all the properties of every Oracle Automatic Storage Management (Oracle ASM) File Group.

In both Oracle ASM and Oracle Database instances, `V$ASM_FILEGROUP_PROPERTY` will display one row for every property of every file type of every File Group contained in every Disk Group mounted by the instance.

File Group properties are only displayed for File Groups on Disk Groups where `COMPATIBLE.ASM` is set to `12.2` or higher.

Note:

There will not be an entry for the default File Group.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Number of the Disk Group in which this File Group exists (composite primary key) |
| `FILEGROUP_NUMBER` | `NUMBER` | Number associated to the File Group within its Disk Group (composite primary key) |
| `COMPOUND_INDEX` | `NUMBER` | A 32-bit number consisting of a Disk Group number in the high-order 8 bits and a Property Number in the low-order 24 bits (for efficient access to the view) |
| `PROPERTY_INDEX` | `NUMBER` | Number of this property in the Disk Group for the File Group (composite primary key) |
| `INCARNATION` | `NUMBER` | Incarnation number for this property (composite primary key) |
| `FILE_TYPE` | `VARCHAR2(30)` | Type of file the property will be applied to:  - `ARCHIVELOG` - `ASMPARAMETERFILE` - `ASMVDRL` - `ASMVOL` - `AUDIT_SPILLFILES` - `AUTOBACKUP` - `BACKUPSET` - `CHANGETRACKING` - `CONTAINER` - `CONTROLFILE` - `DATAFILE` - `DATAGUARDCONFIG` - `DUMPSET` - `FLASHBACK` - `FLASHFILE` - `KEY_STORE` - `OCRBACKUP` - `OCRFILE` - `ONLINELOG` - `PARAMETERFILE` - `TEMPFILE` - `VOTINGFILE` - `XTRANSPORT`  The value can be `NULL` for properties with a File Group granularity. |
| `NAME` | `VARCHAR2(64)` | Full name of the property. Possible values:  - `COMPATIBLE.CLIENT` - `DBCLONE_STATUS` - `OWNER` - `PARENT_FILEGROUP_NUMBER` - `POWER_LIMIT` - `PRIORITY` - `REDUNDANCY` - `STRIPING` - `USER_GROUP` |
| `VALUE` | `VARCHAR2(256)` | Value of the property  See [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-BE9083C8-A5DF-48CD-BB32-C8A6FCDA3E7B) for information about file group property values. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$ASM\_FILEGROUP](V-ASM_FILEGROUP.md) "