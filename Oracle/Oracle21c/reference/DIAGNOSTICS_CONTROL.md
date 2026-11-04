---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DIAGNOSTICS_CONTROL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.110 DIAGNOSTICS\_CONTROL

`DIAGNOSTICS_CONTROL` enables you to control and monitor the users who perform potentially unsafe database diagnostic operations.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DIAGNOSTICS_CONTROL = { ERROR \| WARNING \| IGNORE }` |
| Default value | `IGNORE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

When diagnosing Oracle database issues, an Oracle Support Service staff member might instruct you to perform diagnostic operations. Some diagnostic operations are harmless. However, others could have adverse effects if not performed properly with the guidance of an Oracle Support Service staff member. In order to control and monitor who performs such diagnostic operations, Oracle Database 21c introduces the following security controls:

- Potentially unsafe diagnostic operations are internally identified in the database. These operations include setting certain debug events and debug actions with the `ALTER` `SESSION` or `ALTER` `SYSTEM` statement. For example:
	```
	ALTER SESSION SET EVENTS '1357 trace name context forever, level 2';
	ALTER SYSTEM SET EVENTS 'trace[vos]';
	```
- A user can be authorized to perform potentially unsafe diagnostic operations, either by being granted the `ENABLE` `DIAGNOSTICS` system privilege, or by being granted the `DBA` role, or by authenticating as `SYSDBA`.
- The `DIAGNOSTICS_CONTROL` initialization parameter enables you to specify how the database responds when an unauthorized user attempts to perform these diagnostic operations. The possible values are:
	- `ERROR`: When an unauthorized user attempts to perform a potentially unsafe diagnostic operation, the attempt fails with error `ORA-01031: insufficient privileges`.
		- `WARNING`: When an unauthorized user attempts to perform a potentially unsafe diagnostic operation, the attempt succeeds, but a warning is written to the alert log.
		- `IGNORE`: When an unauthorized user attempts to perform a potentially unsafe diagnostic operation, the attempt succeeds and no error messages or warnings occur. This is the default.

Note:

When altering the `DIAGNOSTICS_CONTROL` initialization parameter, be aware of the following guidelines:

- To modify this parameter with the `ALTER` `SYSTEM` command, you must be authenticated `AS` `SYSDBA`.
- In Oracle RAC environments, it is currently not possible to modify this parameter on remote instances by specifying the `SID` clause in the `ALTER` `SYSTEM` `SET` statement.

Note:

This parameter is available starting with Oracle Database 21c.