---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_DATA_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.272 DBA\_DATA\_FILES

Note:

When you query the `DBA_DATA_FILES` data dictionary view, Oracle must have access to all tablespaces and their data files if the requested information is not already available in the dictionary. If the tablespaces are encrypted, then you must open the Oracle wallet (keystore) before you can query `DBA_DATA_FILES`. You can use the `ADMINISTER` `KEY` `MANAGEMENT` `SET` `KEYSTORE` `OPEN` statement to open the keystore.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_NAME` | `VARCHAR2(513)` |  | Name of the database file |
| `FILE_ID ` | `NUMBER` |  | Absolute file number of the database file |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Name of the tablespace to which the file belongs |
| `BYTES ` | `NUMBER` |  | Size of the file in bytes |
| `BLOCKS` | `NUMBER` |  | Size of the file in Oracle blocks |
| `STATUS ` | `VARCHAR2(9)` |  | File status: `AVAILABLE` or `INVALID` (`INVALID` means that the file number is not in use, for example, a file in a tablespace that was dropped) |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number |
| `AUTOEXTENSIBLE` | `VARCHAR2(3)` |  | Autoextensible indicator |
| `MAXBYTES` | `NUMBER` |  | Maximum file size in bytes |
| `MAXBLOCKS` | `NUMBER` |  | Maximum file size in blocks |
| `INCREMENT_BY` | `NUMBER` |  | Number of Oracle blocks used as autoextension increment |
| `USER_BYTES` | `NUMBER` |  | The size of the file available for user data. The actual size of the file minus the `USER_BYTES` value is used to store file related metadata. |
| `USER_BLOCKS` | `NUMBER` |  | Number of blocks which can be used by the data |
| `ONLINE_STATUS ` | `VARCHAR2(7)` |  | Online status of the file:  - `SYSOFF` - `SYSTEM` - `OFFLINE` - `ONLINE` - `RECOVER` |
| `LOST_WRITE_PROTECT` | `VARCHAR2(7)` |  | Lost write protection status of the file. Possible values:  - `ENABLED`: Indicates that lost write data is being collected - `OFF`: Indicates that lost write data is not being collected - `SUSPEND`: Indicates that lost write data is not currently being collected, but it can be enabled at a later date. The lost write data collected when the file was `ENABLED` remains in the lost write database, but it is not being checked or updated.  If lost write protection is enabled for a single data file, it does not have to be enabled for another data file in the same tablespace.  If lost write protection is enabled for a tablespace, it is enabled for all data files for that tablespace, including data files added later.  You can check the lost write protection status for a tablespace by querying the `LOST_WRITE_PROTECT` column in the `DBA_TABLESPACES` view. |

See Also:

- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-F3652F6F-B1B8-485A-BCBE-32C0875E93E5) for information on opening a software keystore
- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ASOAG-GUID-CEDB143A-BC7E-43EF-AD41-59BD0ED36421) for information on opening a hardware keystore
- " [DBA\_TABLESPACES](DBA_TABLESPACES.md) "