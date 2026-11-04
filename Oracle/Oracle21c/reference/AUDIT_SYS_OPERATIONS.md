---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDIT_SYS_OPERATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.24 AUDIT\_SYS\_OPERATIONS

`AUDIT_SYS_OPERATIONS` enables or disables the auditing of directly issued user SQL statements with `SYS` authorization. These include SQL statements directly issued by users when connected with the `SYSASM`, `SYSBACKUP`, `SYSDBA`, `SYSDG`, `SYSKM`, or `SYSOPER` privileges, as well as SQL statements that have been executed with `SYS` authorization using the PL/SQL package `DBMS_SYS_SQL`.

Note:

This parameter is effective when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `TRUE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `TRUE \| FALSE` |
| Basic | No |

The audit records are written to the operating system's audit trail. The audit records will be written in XML format if the `AUDIT_TRAIL` initialization parameter is set to `xml` or `xml, extended`

On UNIX platforms, if the `AUDIT_SYSLOG_LEVEL` parameter has also been set, then it overrides the `AUDIT_TRAIL` parameter and SYS audit records are written to the system audit log using the `SYSLOG` utility.

In a CDB, the scope of the settings for this initialization parameter is the CDB. Although the audit trail is provided per PDB in a CDB, this initialization parameter cannot be configured for individual PDBs.