---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_ACFS_SEC_REALM_FILTER.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ASM_ACFS_SEC_REALM_FILTER` contains an entry for every filter in the Oracle ACFS security realm for each Oracle ACFS file system. A filter is a defined as a command rule/rule set pair in a realm. This view also supports GV$ global views.

| Column | Datatype | Description |
| --- | --- | --- |
| `REALM_NAME` | `VARCHAR2(255)` | Realm name |
| `CMD_RULE_NAME` | `VARCHAR2(32)` | Command rule name |
| `RULESET_NAME` | `VARCHAR2(256)` | Ruleset name |
| `FS_NAME` | `VARCHAR2(1024)` | Mount path name to identify the file system |
| `VOL_DEVICE` | `VARCHAR2(256)` | ADVM volume name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG30000) for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG95490) for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30).