---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-ASM_ACFS_SEC_RULE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$ASM_ACFS_SEC_RULE` contains information about all Oracle ACFS security rules for each Oracle ACFS file system. This view also supports GV$ global views.

| Column | Datatype | Description |
| --- | --- | --- |
| `RULE_NAME` | `VARCHAR2(256)` | Name of the rule |
| `RULE_TYPE` | `VARCHAR2(32)` | Type of the rule:  - `time` - `username` - `groupname` - `hostname` - `application` |
| `RULE_VALUE` | `VARCHAR2(512)` | Value of the rule, which could include values such as 23:10:00 for `time`, Bob for `username`, dba for `groupname`, host147 for `hostname`, /sbin/cat for `application`. |
| `RULE_VALUE2` | `VARCHAR2(512)` | The value will be populated only if the rule type is `time`. When the rule type is `time`, the start time is entered in `RULE_VALUE` and the end time is entered in `RULE_VALUE2`. |
| `RULE_OPTION` | `VARCHAR2(7)` | Possible values are `ALLOW` or `DENY` |
| `FS_NAME` | `VARCHAR2(1024)` | Mount path name to identify the file system |
| `VOL_DEVICE` | `VARCHAR2(256)` | ADVM volume name |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG30000) for more information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS)
- [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG95490) for additional information about using views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance. For information about Oracle Flex ASM, refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=OSTMG-GUID-DE759521-9CF3-45D9-9123-7159C9ED4D30).