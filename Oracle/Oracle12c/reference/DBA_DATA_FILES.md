---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_DATA_FILES.html
tags:
  - oracle
  - 12c
  - reference
---

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
| `LOST_WRITE_PROTECT` | `VARCHAR2(7)` |  | For internal use only. |

See Also:

- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ASOAG-GUID-A9C23E31-CF57-477A-9E85-856DD411718D) for information on opening a software keystore
- [Oracle Database Advanced Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ASOAG-GUID-81E6D2BA-EE27-4D35-96FB-2FFC0BCD396B) for information on opening a hardware keystore
- " [DBA\_TABLESPACES](DBA_TABLESPACES.md) "