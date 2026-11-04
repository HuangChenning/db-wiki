---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_ACFSREPLTAG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.45 V$ASM\_ACFSREPLTAG

`V$ASM_ACFSREPLTAG` displays replicated tag information for Oracle ACFS file systems that are initialized for replication.

| Column | Datatype | Description |
| --- | --- | --- |
| `FSNAME` | `VARCHAR2(1024)` | File system mount point (foreign key to `V$ASM_FILESYSTEM`) |
| `VOLDEV` | `VARCHAR2(256)` | Name of the Oracle ADVM device |
| `TAG` | `VARCHAR2(32)` | Tag name that is being replicated |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

Note:

This view only contains records for Oracle ASM releases prior to Oracle Database 12c Release 2 (12.2.0.1). To display Oracle ACFS replication information for Oracle Database 12c Release 2 (12.2.0.1) or higher, use the `acfsutil repl info` command.

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG30000) for more information about Oracle Advanced Cluster File System (Oracle ACFS)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG95490) for additional information about using views to display Oracle Advanced Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30).