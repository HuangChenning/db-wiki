---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_ACFSTAG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.47 V$ASM\_ACFSTAG

`V$ASM_ACFSTAG` displays every file or directory that has a tag and its tag name for every mounted Oracle ACFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `TAG_NAME` | `VARCHAR2(32)` | Tag name on file or directory |
| `FS_NAME` | `VARCHAR2(1024)` | File system mount point |
| `PATH_NAME` | `VARCHAR2(4096)` | Complete file path name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG30000) for more information about Oracle Advanced Cluster File System (Oracle ACFS)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG95490) for additional information about using views to display Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30).