---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AUDITABLE_SYSTEM_ACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.178 AUDITABLE\_SYSTEM\_ACTIONS

`AUDITABLE_SYSTEM_ACTIONS` maps the auditable system action numbers to the action names. These actions are configurable for audit when unified auditing is enabled.

The actions include:

- All standard RDBMS actions (from the `V$SQLCOMMAND` view) except the following, which are not configurable for auditing:
	- ALTER EDITION
		- ALTER REWRITE EQUIVALENCE
		- ALTER SUMMARY
		- ALTER TRACING
		- CREATE BITMAPFILE
		- CREATE CONTROL FILE
		- CREATE DATABASE
		- CREATE SUMMARY
		- DECLARE REWRITE EQUIVALENCE
		- DROP BITMAPFILE
		- DROP DATABASE
		- DROP REWRITE EQUIVALENCE
		- DROP SUMMARY
		- FLASHBACK DATABASE
		- MERGE
		- SAVEPOINT
		- SET CONSTRAINTS
		- UNDROP OBJECT
		- UPDATE INDEXES
		- UPDATE JOIN INDEX
		- VALIDATE INDEX
- Other actions:
	- ALL
		- LOGON
		- LOGOFF

Note:

This view is populated only in an Oracle Database where unified auditing is enabled.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TYPE` | `NUMBER` |  | Numeric component type for system wide actions |
| `COMPONENT` | `VARCHAR2(64)` |  | Name of component for system wide actions |
| `ACTION` | `NUMBER` |  | Numeric auditable action code for system wide actions |
| `NAME` | `VARCHAR2(64)` |  | Name of auditable action |

Some auditable actions in `AUDITABLE_SYSTEM_ACTIONS` have different names than their equivalent commands in `V$SQLCOMMAND`, as shown in the following table:

| AUDITABLE\_SYSTEM\_ACTIONS Action Name | V$SQLCOMMAND Command Name |
| --- | --- |
| GRANT | GRANT OBJECT |
| REVOKE | REVOKE OBJECT |
| AUDIT | AUDIT OBJECT |
| NOAUDIT | NOAUDIT OBJECT |
| EXECUTE | PL/SQL EXECUTE |
| EXPLAIN PLAN | EXPLAIN |
| CALL | CALL METHOD |
| PURGE DBA\_RECYCLEBIN | PURGE DBA RECYCLEBIN |

See Also:

" [V$SQLCOMMAND](V-SQLCOMMAND.md) "