---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/AUDITABLE_SYSTEM_ACTIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`AUDITABLE_SYSTEM_ACTIONS` maps the auditable system action numbers to the action names. These actions are configurable for audit when unified auditing is enabled.

The actions include:

- All standard RDBMS actions (from the `V$SQLCOMMAND` view) except the following, which are not configurable for auditing:
	- ALTER EDITION
		- ALTER REWRITE EQUIVALENCE
		- CREATE BITMAPFILE
		- CREATE CONTROL FILE
		- CREATE DATABASE
		- DECLARE REWRITE EQUIVALENCE
		- DROP BITMAPFILE
		- DROP DATABASE
		- DROP REWRITE EQUIVALENCE
		- FLASHBACK DATABASE
- Other actions:
	- ALL
		- LOGON
		- LOGOFF

Note:

This view is populated only in an Oracle Database where unified auditing is enabled.

- See [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG006) for more information about unified auditing.
- See [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=UPGRD52810) for more information about migrating to unified auditing.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TYPE` | `NUMBER` |  | Numeric component type for system wide actions |
| `COMPONENT` | `VARCHAR2(64)` |  | Name of component for system wide actions |
| `ACTION` | `NUMBER` |  | Numeric auditable action code for system wide actions |
| `NAME` | `VARCHAR2(64)` |  | Name of auditable action |

See Also:

" [V$SQLCOMMAND](V-SQLCOMMAND.md) "