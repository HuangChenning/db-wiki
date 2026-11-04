---
title: AUDIT_TRAIL
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams017.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `AUDIT_TRAIL = { none \| os \| db [, extended] \| xml [, extended] }` |
| Default value | `none` |
| Modifiable | No |
| Basic | No |

`AUDIT_TRAIL` enables or disables database auditing.

Values:

- `none`
	Disables standard auditing. This value is the default if the `AUDIT_TRAIL` parameter was not set in the initialization parameter file or if you created the database using a method other than Database Configuration Assistant. If you created the database using Database Configuration Assistant, then the default is `db`.
- `os`
	Directs all audit records to an operating system file. Oracle recommends that you use the `os` setting, particularly if you are using an ultra-secure database configuration.
- `db`
	Directs audit records to the database audit trail (the `SYS.AUD$` table), except for records that are always written to the operating system audit trail. Use this setting for a general database for manageability.
	If the database was started in read-only mode with `AUDIT_TRAIL` set to `db`, then Oracle Database internally sets `AUDIT_TRAIL` to `os`. Check the alert log for details.
- `db, extended`
	Performs all actions of `AUDIT_TRAIL` = `db`, and also populates the SQL bind and SQL text CLOB-type columns of the `SYS.AUD$` table, when available. These two columns are populated only when this parameter is specified.
	If the database was started in read-only mode with `AUDIT_TRAIL` set to `db, extended`, then Oracle Database internally sets `AUDIT_TRAIL` to `os`. Check the alert log for details.
- `xml`
	Writes to the operating system audit record file in XML format. Records all elements of the `AuditRecord` node except `Sql_Text` and `Sql_Bind` to the operating system XML audit file.
- `xml, extended`
	Performs all actions of `AUDIT_TRAIL` = `xml`, and includes SQL text and SQL bind information in the audit trail.

You can use the SQL `AUDIT` statement to set auditing options regardless of the setting of this parameter.

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

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG90002) describes the types of auditing that can be performed and provides more information about using the different auditing options, including configuration examples.