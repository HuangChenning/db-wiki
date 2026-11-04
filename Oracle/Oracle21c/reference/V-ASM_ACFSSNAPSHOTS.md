---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_ACFSSNAPSHOTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.46 V$ASM\_ACFSSNAPSHOTS

`V$ASM_ACFSSNAPSHOTS` displays snapshot information for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `FS_NAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOL_DEVICE` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `SNAP_NAME` | `VARCHAR2(1024)` | Name of the snapshot |
| `CREATE_TIME` | `DATE` | Time when the snapshot was created |
| `TYPE` | `VARCHAR2(2)` | Snapshot type. Possible types are read-only (RO) or read/write (RW). |
| `PARENT` | `VARCHAR2(1024)` | Parent name used to create the snapshot. If the snapshot was created using the mount point as a base, parent name will be NULL. If the snapshot was created using an existing snapshot as the base, the parent name will be the name of the snapshot passed to the `acfsutil snap create -p` operation. |
| `LINK` | `VARCHAR2(1024)` | If link has been set, the path of the link. If unset, NULL. |
| `ADDITIONAL_STORAGE` | `NUMBER` | Equivalent to "storage added to snapshot" output |
| `QUOTA` | `NUMBER` | Value of quota. If unset, NULL. |
| `REPL` | `VARCHAR2(5)` | Indicates whether the snapshot is being used for replication (`TRUE`) or not (`FALSE`) |
| `STATE` | `VARCHAR2(14)` | The state of the snapshot: - `AVAILABLE` - Default - `DELETE_WAITING` - Maps to "delete waiting for last close" - `DELETE_IN_PROGRESS` - Maps to "delete in progress" |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG30000) for more information about Oracle Advanced Cluster File System (Oracle ACFS)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG95490) for additional information about using views to display Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30).