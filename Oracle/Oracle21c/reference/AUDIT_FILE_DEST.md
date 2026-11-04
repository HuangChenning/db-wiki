---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDIT_FILE_DEST.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.23 AUDIT\_FILE\_DEST

`AUDIT_FILE_DEST` specifies the operating system directory into which the audit trail is written when the `AUDIT_TRAIL` initialization parameter is set to os, xml, or xml,extended.

Note:

This parameter is effective when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `AUDIT_FILE_DEST = '` `directory` `'` |
| Default value | The first default value is:  `ORACLE_BASE` `/admin/` `ORACLE_SID` `/adump`  The second default value, which is used if the first default value does not exist or is unusable, is:  `ORACLE_HOME` `/rdbms/audit`  Both of these default values are for UNIX systems. Other platforms may have different defaults.  In a multitenant container database (CDB), both of these default values will be appended with the GUID of the pluggable database (PDB) to store audit records that belong to the PDB. For example, if the PDB's GUID is `03E1F908EE04252CE053B280E80AAAA3`, the first default directory will be:  `ORACLE_BASE` `/admin/` `ORACLE_SID` `/adump/03E1F908EE04252CE053B280E80AAAA3`  You can use the `V$CONTAINERS` view to query a PDB's GUID. |
| Modifiable | `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | No |
| Basic | No |

If you do not explicitly set a value for this parameter in the initialization file, then at least one of the two default operating system directories mentioned in the preceding table must exist and be writeable. Otherwise, the instance will fail to start.

If you explicitly set a value for this parameter in the initialization file, then the directory you specify must exist and be writeable. Otherwise, the instance will fail to start.

The audit records will be written in XML format if the `AUDIT_TRAIL` initialization parameter is set to xml or xml, extended. It is also the location to which mandatory auditing information is written and, if so specified by the `AUDIT_SYS_OPERATIONS` initialization parameter, audit records for user `SYS`.

In a multitenant container database (CDB), the scope of the settings for this initialization parameter is the CDB. Although the audit trail is provided per pluggable database (PDB) in a CDB, this initialization parameter cannot be configured for individual PDBs.