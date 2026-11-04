---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/triggers-and-oracle-ai-database-data-transfer-utilities.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Triggers and Oracle Database Data Transfer Utilities

The Oracle database utilities that transfer data to your database, possibly firing triggers, are:

- SQL\*Loader (`sqlldr`)
	SQL\*Loader loads data from external files into tables of an Oracle database.
	During a SQL\*Loader conventional load, `INSERT` triggers fire.
	Before a SQL\*Loader direct load, triggers are disabled.
	See Also:
	[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SUTIL003) for more information about SQL\*Loader
- Data Pump Import (`impdp`)
	Data Pump Import (`impdp`) reads an export dump file set created by Data Pump Export (`expdp`) and writes it to an Oracle database.
	If a table to be imported does not exist on the target database, or if you specify `TABLE_EXISTS_ACTION=REPLACE`, then `impdp` creates and loads the table before creating any triggers, so no triggers fire.
	If a table to be imported exists on the target database, and you specify either `TABLE_EXISTS_ACTION=APPEND` or `TABLE_EXISTS_ACTION=TRUNCATE`, then `impdp` loads rows into the existing table, and `INSERT` triggers created on the table fire.
	See Also:
	[Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SUTIL300) for more information about Data Pump Import
- Original Import (`imp`)
	Original Import (the original Import utility, `imp`) reads object definitions and table data from dump files created by original Export (the original Export utility, `exp`) and writes them to the target database.
	Note:
	To import files that original Export created, you must use original Import. In all other cases, Oracle recommends that you use Data Pump Import instead of original Import.
	If a table to be imported does not exist on the target database, then `imp` creates and loads the table before creating any triggers, so no triggers fire.
	If a table to be imported exists on the target database, then the Import `IGNORE` parameter determines whether triggers fire during import operations. The `IGNORE` parameter specifies whether object creation errors are ignored or not, resulting in the following behavior:
	- If `IGNORE=n` (default), then `imp` does not change the table and no triggers fire.
		- If `IGNORE=y`, then `imp` loads rows into the existing table, and `INSERT` triggers created on the table fire.
	See Also:
	- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SUTIL001) for more information about the original Import utility
	- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SUTIL3634) for more information about the original Export utility
	- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=SUTIL1719) for more information about `IGNORE`