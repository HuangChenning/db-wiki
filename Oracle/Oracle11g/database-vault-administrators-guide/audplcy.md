---
title: Auditing Oracle Database Vault
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/audplcy.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## A Auditing Oracle Database Vault

This appendix contains:

## Oracle Database Vault Specific Audit Events

This section contains:

- Oracle Database Vault Audit Events
- Format of the Oracle Database Vault Audit Trail

### Oracle Database Vault Audit Events

Oracle Database Vault uses audit events to track the following activities:

- Realm Audit. You can audit both successful and failed actions, based on the auditing option that you set when you created the realm. The exception to this is actions performed by the schema owner.
- Rule Set Audit. Audits the rule set processing results. You can audit both successful and failed processing. Realm authorizations can be managed using rule sets. You can audit the rule set processing results. Factor assignments and secure application roles audits can be managed using a rule set.
- Factor Audit. You can audit both successful and failed factor processing. For failed factor processing, you can audit on all or any of the following events: Retrieval Error, Retrieval Null, Validation Error, Validation False, Trust Level Null, or Trust Level Less Than Zero.
- Oracle Label Security Session Initialization Failed. Audits instances where the Oracle Label Security session fails to initialize.
- Oracle Label Security Attempt to Upgrade Session Label Failed. Audits instances where the Oracle Label Security component prevents a session from setting a label that exceeds the maximum session label.

### Format of the Oracle Database Vault Audit Trail

The Oracle Database Vault audit event records are stored in the `AUDIT_TRAIL$` table, which is part of the `DVSYS` schema. These audit records are not part of the Oracle Database audit trail, and how auditing is enabled in the database has no effect how Oracle Database Vault collects its audit data in the `DVSYS.AUDIT_TRAIL$` table. In fact, even if auditing has been disabled in Oracle Database, then the Oracle Database Vault audit functionality continues to write to the `DVSYS.AUDIT_TRAIL$` table. Users who have been granted the `DV_OWNER`, `DV_ADMIN`, or `DV_SECANALYST` role can directly query the `DVYS.AUDIT_TRAIL$` table.

Users who have been granted the `DV_OWNER`, `DV_ADMIN`, `DV_SECANALYST` or `DV_MONITOR` role can directly query the `DVYS.AUDIT_TRAIL$` table.

Note:

Oracle Audit Vault and Database Firewall can collect the audit data for Oracle Database Vault. See [Oracle Audit Vault and Database Firewall Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=SIGAD) for more information.

Table A-1 describes the format of the audit trail, which you must understand if you plan to create custom reports that use the `DVSYS.AUDIT_TRAIL$` table.

Table A-1 Oracle Database Vault Audit Trail Format

| Column | Datatype | Null | Description |
| --- | --- | --- | --- |
| `ID#` | `NUMBER` | `NOT NULL` | Numeric identifier for the audit record |
| `OS_USERNAME` | `VARCHAR2(255)` |  | Operating system login user name of the user whose actions were audited |
| `USERNAME` | `VARCHAR2(30)` |  | Name of the database user whose actions were audited |
| `USERHOST` | `VARCHAR2(128)` |  | Client computer name |
| `TERMINAL` | `VARCHAR2(255)` |  | Identifier for the user's terminal |
| `TIMESTAMP` | `DATE` |  | Date and time of creation of the audit trail entry (in the local database session time zone) |
| `OWNER` | `VARCHAR2(30)` |  | Creator of the object affected by the action, always `DVSYS` (because `DVSYS` is where objects are created) |
| `OBJ_NAME` | `VARCHAR2(128)` |  | Name of the object affected by the action. Expected values are:  - `ROLE$` - `REALM$` - `CODE$` - `FACTOR$` |
| `ACTION` | `NUMBER` | `NOT NULL` | Numeric action type code. The corresponding name of the action type is in the `ACTION_NAME` column. Expected `ACTION` and `ACTION_NAME` values are:  - `10000`: Factor Evaluation Audit - `10001`: Factor Assignment Audit - `10002`: Factor Expression Audit - `10003`: Realm Violation Audit - `10004`: Realm Authorization Audit - `10005`: Command Authorization Audit - `10006`: Secure Role Audit - `10007`: Access Control Session Initialization Audit - `10008`: Access Control Command Authorization Audit - `10009`: Oracle Label Security Session Initialization Audit - `10010`: Oracle Label Security Attempt to Upgrade Label Audit |
| `ACTION_NAME` | `VARCHAR2(128)` |  | Name of the action type corresponding to the numeric code in the `ACTION` column |
| `ACTION_OBJECT_ID` | `NUMBER` |  | The unique identifier of the record in the table specified under `OBJ_NAME` |
| `ACTION_OBJECT_NAME` | `VARCHAR2(128)` |  | The unique name or natural key of the record in the table specified under `OBJ_NAME` |
| `ACTION_COMMAND` | `VARCHAR2(4000)` |  | The SQL text of the command procedure that was executed that resulted in the audit event being triggered |
| `AUDIT_OPTION` | `VARCHAR2(4000)` |  | The labels for all audit options specified in the record that resulted in the audit event being triggered. For example, a factor set operation that is supposed to audit on get failure and get `NULL` would indicate these two options. |
| `RULE_SET_ID` | `NUMBER` |  | The unique identifier of the rule set that was executing and caused the audit event to trigger |
| `RULE_SET_NAME` | `VARCHAR2(30)` |  | The unique name of the rule set that was executing and caused the audit event to trigger |
| `RULE_ID` | `NUMBER` |  | Not used |
| `RULE_NAME` | `VARCHAR2(30)` |  | Not used |
| `FACTOR_CONTEXT` | `VARCHAR2(4000)` |  | An XML document that contains all of the factor identifiers for the current session at the point when the audit event was triggered |
| `COMMENT_TEXT` | `VARCHAR2(4000)` |  | Text comment on the audit trail entry, providing more information about the statement audited |
| `SESSIONID` | `NUMBER` | `NOT NULL` | Numeric identifier for each Oracle session |
| `ENTRYID` | `NUMBER` | `NOT NULL` | Same as the value in the `ID#` column |
| `STATEMENTID` | `NUMBER` | `NOT NULL` | Numeric identifier for the statement invoked that caused the audit event to be generated. This is empty for most Oracle Database Vault events. |
| `RETURNCODE` | `NUMBER` | `NOT NULL` | Oracle error code generated by the action. The error code for a statement or procedure invoked that caused the audit event to be generated. This is empty for most Oracle Database Vault events. |
| `EXTENDED_TIMESTAMP` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time stamp of creation of the audit trail entry (time stamp of user login for entries) in UTC (Coordinated Universal Time) time zone |
| `PROXY_SESSIONID` | `NUMBER` |  | Proxy session serial number, if an enterprise user has logged in through the proxy mechanism |
| `GLOBAL_UID` | `VARCHAR2(32)` |  | Global user identifier for the user, if the user has logged in as an enterprise user |
| `INSTANCE_NUMBER` | `NUMBER` |  | Instance number as specified by the `INSTANCE_NUMBER` initialization parameter |
| `OS_PROCESS` | `VARCHAR2(16)` |  | Operating system process identifier of the Oracle process |
| `CREATED_BY` | `VARCHAR2(30)` |  | Database login user name of the user whose actions were audited |
| `CREATE_DATE` | `DATE` |  | Date on which the action occurred, based on the `SYSDATE` date |
| `UPDATED_BY` | `VARCHAR2(30)` |  | Same as `CREATED_BY` column value |
| `UPDATE_DATE` | `DATE` |  | Same as `UPDATED_BY` column value |

## Archiving and Purging the Oracle Database Vault Audit Trail

You can create an archive of the Oracle Database Vault audit trail by exporting the `DVSYS.AUDIT_TRAIL$` system table, which is owned by `DVSYS`, to a dump file. You should periodically archive and then purge the audit trail to prevent it from growing too large.

To archive and purge the Oracle Database Vault audit trail:

1. Ensure that you or the user performing the export operation has been granted the appropriate authorization.
	See ["Using Oracle Data Pump in an Oracle Database Vault Environment"](dba.md) for more information.
2. Disable Oracle Database Vault.
	See ["Step 1: Disable Oracle Database Vault"](dvdisabl.md).
3. At the operating system command prompt, create a directory for the Oracle Database Vault audit trail (for example, in `$ORACLE_BASE/admin/$DB_UNIQUE_NAME/dvaudit`).
	You may want to keep this directory in the same location as the operating system audit trail directories for Oracle Database, which by default is in the `$ORACLE_BASE/admin/$DB_UNIQUE_NAME/adump` directory. In SQL\*Plus, you can check the location of the audit trail directory as follows:
	```
	SHOW PARAMETER AUDIT_FILE_DEST
	```
	Output similar to the following appears:
	```
	NAME                 TYPE     VALUE
	-------------------  -------  ---------------------------------------
	audit_file_dest      string   /opt/oracle/app/oracle/admin/orcl/adump
	```
4. In SQL\*Plus, create a directory object in which to generate the Oracle Database Vault audit trail. To do so, connect as `SYS` or as any user who has the `CREATE ANY DIRECTORY` privilege.
	For example:
	```
	CREATE DIRECTORY dv_audit_dir AS '/opt/oracle/app/oracle/admin/orcl/dvaudit';
	```
	Enclose the directory path in single quotation marks, not double quotation marks.
5. In SQL\*Plus, grant read and write privileges on the directory object to user `DVSYS`.
	For example:
	```
	GRANT READ, WRITE ON DIRECTORY dvaudit TO dvsys;
	```
6. At the operating system command prompt, enter a command similar to the following to export the `DVSYS.AUDIT_TRAIL$` audit table into a new dump file.
	```
	EXPDP DVSYS
	Enter password: password
	DIRECTORY=dvaudit \
	TABLES=DVSYS.AUDIT_TRAIL$ \
	QUERY=DVSYS.AUDIT_TRAIL$:"WHERE timestamp < 2009-08-03:19:34:59" 
	DUMPFILE=dv_audit_031607.dmp
	```
	In this specification:
	- `DIRECTORY`: Enter the directory object that you created in Step 5. Ensure that the user who is running `EXPDP` (`DVSYS` in this example) has read and write permissions on this directory object. If you created the directory object, then you automatically have read and write permissions on it.
		- `TABLES`: Enter `DVSYS.AUDIT_TRAIL$`, the name of the audit trail table.
		- `QUERY`: Optional. This setting writes a subset of the audit table contents to the dump file, in this case, audit records that are less than the `timestamp` column value of `2009-08-03:19:34:59.`
		- `DUMPFILE`: Enter the name of the dump file that you want to create. The default extension is `.dmp`, but you can use any extension. Ensure that the file name you specify is unique.
7. In SQL\*Plus, purge the Oracle Database Vault audit trail table, now that you have archived it.
	For example, if you archived all audit trail records that are less than the `timestamp` column value of `2009-08-03:19:34:59`, enter the following statement:
	```
	DELETE FROM DVSYS.AUDIT_TRAIL$ WHERE TIMESTAMP < 2009-08-03:19:34:59;
	```
	To completely purge the audit trail and remove the extents allocated to the audit trail table, enter the following statement:
	```
	TRUNCATE TABLE DVSYS.AUDIT_TRAIL$;
	```
8. Exit SQL\*Plus.
9. Re-enable Oracle Database Vault.
	See ["Step 3: Enable Oracle Database Vault"](dvdisabl.md).

## Oracle Database Audit Settings Created for Oracle Database Vault

When you install Oracle Database Vault, it creates several `AUDIT` settings in the database. However, in order for these audit settings to take place, auditing must be enabled in this database. You can check if auditing is enabled by using the `SHOW PARAMETER` command to find the value of the `AUDIT_TRAIL` initialization parameter. By default, auditing is disabled in Oracle Database.

If the `AUDIT_TRAIL` parameter is set to `NONE`, then auditing is not enabled, so you must set `AUDIT_TRAIL`. For detailed information about the `AUDIT_TRAIL` parameter settings, see [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/auditing.htm#DBSEG66232) and [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams017.htm#REFRN10006).

Table A-2 lists the `AUDIT` settings that Oracle Database Vault adds to the database.

Table A-2 Audit Policy Settings Oracle Database Vault Adds to Oracle Database

| Audit Setting Type | Audited Statements (BY ACCESS and on Success or Failure Unless Otherwise Noted) |
| --- | --- |
| System Audit Settings/System Privilege Usage | `ALTER ANY`  `CREATE ANY`  `DELETE ANY`  `DROP ANY`  `EXECUTE ANY` (`WHENEVER NOT SUCCESSFUL`)  `FORCE ANY`  `GRANT ANY`  `INSERT ANY`  `UPDATE ANY` |
| System Audit Settings/Object Management | `ALTER DATABASE, PROFILE, ROLLBACK SEGMENT, SESSION, SYSTEM, TABLE, TABLESPACE, USER`  `CREATE CLUSTER, DATABASE LINK, INDEXTYPE, LIBRARY, OPERATOR, PUBLIC SYNONYM, PROCEDURE, PROFILE, ROLE, ROLLBACK SEGMENT, SEQUENCE, SESSION, SNAPSHOT, SYNONYM, TABLE, TABLESPACE, TRIGGER, TYPE, USER, VIEW`  `TRUNCATE` |
| System Audit Settings/Intrusive Commands | `ALTER SESSION`  `BECOME USER`  `CREATE SESSION`  `DEBUG CONNECT SESSION`  `RESTRICTED SESSION` |
| System Audit Settings/Administration Commands | `ADMINISTER DATABASE TRIGGER`  `BACKUP ANY TABLE`  `EXEMPT ACCESS POLICY`  `MANAGE TABLESPACE` |
| System Audit Settings/Audit Commands | `AUDIT ANY`  `AUDIT SYSTEM` |
| System Audit Settings/Access Control | `GRANT ANY PRIVILEGE/ANY OBJECT PRIVILEGE/ROLE`  `GRANT DIRECTORY`  `GRANT SEQUENCE`  `GRANT TABLE`  `GRANT TYPE` |
| User Audit Settings for `DVSYS` / `DVF`  User Audit Settings for `LBACSYS`  See [Table 11-2, "Database Accounts Used by Oracle Database Vault"](db_objects.md) for more information about these accounts.  See also these sections for detailed information on the `DVSYS` and `DVF` schemas:  - ["DVSYS Schema"](db_objects.md) - ["DVF Schema"](db_objects.md) | `ADMINISTER DATABASE TRIGGER`  `ALTER` `object`  `AUDIT SYSTEM`  `BECOME USER`  `CLUSTER` |