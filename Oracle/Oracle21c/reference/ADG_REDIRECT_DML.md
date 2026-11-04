---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ADG_REDIRECT_DML.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.9 ADG\_REDIRECT\_DML

Use `ADG_REDIRECT_DML` to enable or disable automatic redirection of DML operations from a standby to the primary in Oracle Active Data Guard environments.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM`  Can be modified at the session level with a special `ALTER` `SESSION` command. See details below. |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

Automatic redirection of DML operations to the primary can be configured at the system level or the session level. The session level setting overrides the system level setting.

- To enable automatic redirection of DML operations to the primary at the system level, set `ADG_REDIRECT_DML` to `true`.
- To disable automatic redirection of DML operations to the primary at the system level, set `ADG_REDIRECT_DML` to `false`.
- To enable automatic redirection of DML operations from a standby to the primary for the current session, issue the following SQL statement:
	```
	ALTER SESSION ENABLE ADG_REDIRECT_DML;
	```
- To disable automatic redirection of DML operations from a standby to the primary for the current session, issue the following SQL statement:
	```
	ALTER SESSION DISABLE ADG_REDIRECT_DML;
	```

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB-GUID-8AAD002C-ED06-4349-8BB5-EC8DB30B2628) for more information about automatic redirection of DML operations