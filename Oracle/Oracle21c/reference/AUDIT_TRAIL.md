---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDIT_TRAIL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.26 AUDIT\_TRAIL

Note:

This parameter is effective when using traditional auditing. Traditional auditing is deprecated in Oracle Database 21c. Oracle recommends that you instead use unified auditing, which enables selective and more effective auditing inside Oracle Database.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `AUDIT_TRAIL = { none \| os \| db [, extended] \| xml [, extended] }` |
| Default value | `none` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |

Values

- `none`
	Disables standard auditing. This value is the default if the `AUDIT_TRAIL` parameter was not set in the initialization parameter file or if you created the database using a method other than Database Configuration Assistant. If you created the database using Database Configuration Assistant, then the default is `db`.
- `os`
	Directs all audit records to an operating system file. Oracle recommends that you use the `os` setting, particularly if you are using an ultra-secure database configuration.
- `db`
	Directs audit records to the database audit trail (the `SYS.AUD$` table), except for records that are always written to the operating system audit trail. Use this setting for a general database for manageability.
	If the database was started in read-only mode with `AUDIT_TRAIL` set to `db`, then Oracle Database internally sets `AUDIT_TRAIL` to `os`. Check the alert log for details.
- `db, extended`
	Performs all actions of `AUDIT_TRAIL` = `db`, and also populates the SQL bind and SQL text CLOB-type columns of the `SYS.AUD$` table, when available. These two columns are populated only when this parameter is specified. When standard auditing is used with `DB, EXTENDED`, then virtual private database (VPD) predicates and policy names are also populated in the `SYS.AUD$` table.
	If the database was started in read-only mode with `AUDIT_TRAIL` set to `db, extended`, then Oracle Database internally sets `AUDIT_TRAIL` to `os`. Check the alert log for details.
- `xml`
	Writes to the operating system audit record file in XML format. Records all elements of the `AuditRecord` node except `Sql_Text` and `Sql_Bind` to the operating system XML audit file.
- `xml, extended`
	Performs all actions of `AUDIT_TRAIL` = `xml`, and includes SQL text and SQL bind information in the audit trail.

You can use the SQL `AUDIT` statement to set auditing options regardless of the setting of this parameter.

In a CDB, the scope of the settings for this initialization parameter is the CDB. Although the audit trail is provided per PDB in a CDB, this initialization parameter cannot be configured for individual PDBs.

Examples

The following statement sets the `db, extended` value for the `AUDIT_TRAIL` parameter. The new value takes effect after the database is restarted.

```
SQL> alter system set AUDIT_TRAIL=db, extended scope=spfile;

System altered.

SQL>
```

The following statement sets the `xml, extended` value for the `AUDIT_TRAIL` parameter. The new value takes effect after the database is restarted.

```
SQL> alter system set AUDIT_TRAIL=xml, extended scope=spfile;

System altered.

SQL>
```

The following statement sets the `db` value for the `AUDIT_TRAIL` parameter. The new value takes effect after the database is restarted.

```
SQL> alter system set AUDIT_TRAIL=db scope=spfile;

System altered.

SQL>
```

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG1025) for information about configuring unified audit policies
- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52813) to learn more about traditional non-unified auditing