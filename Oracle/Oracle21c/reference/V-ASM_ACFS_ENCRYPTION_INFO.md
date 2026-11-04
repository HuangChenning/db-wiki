---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_ACFS_ENCRYPTION_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.42 V$ASM\_ACFS\_ENCRYPTION\_INFO

`V$ASM_ACFS_ENCRYPTION_INFO` displays encryption information for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOL_DEVICE` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `SET_STATUS` | `VARCHAR2(7)` | Indicates whether encryption parameters have been set on the file system (`YES`) or not (`NO`); otherwise `UNKNOWN`. |
| `ENABLED_STATUS` | `VARCHAR2(8)` | Indicates whether file system level encryption is enabled (`ENABLED`) or not (`DISABLED`); otherwise `UNKNOWN`. |
| `ALGORITHM` | `VARCHAR2(7)` | Encryption algorithm used. AES is the only supported algorithm. |
| `KEY_LENGTH` | `VARCHAR2(7)` | Key length used for the encryption key |
| `LAST_REKEY_TIME` | `DATE` | Time that the volume was last rekeyed |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG30000) for more information about Oracle Advanced Cluster File System (Oracle ACFS)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG95490) for additional information about using views to display Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30).