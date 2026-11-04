---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/STANDBY_DB_PRESERVE_STATES.html
tags:
  - oracle
  - 12c
  - reference
---

`STANDBY_DB_PRESERVE_STATES` controls whether user sessions and other internal states of the instance are retained when a readable physical standby database is converted to a primary database. This parameter is meaningful on a physical standby database that is open in real-time query mode.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_DB_PRESERVE_STATES = { NONE \| SESSION \| ALL }` |
| Default value | `NONE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

The possible values for the parameter are `NONE`, `SESSION`, and `ALL`. The default is `NONE`, meaning nothing is retained and all sessions are disconnected. When this parameter is set to `SESSION` or `ALL`, user sessions are retained when a readable physical standby database is converted to primary. When the database is reopened as the primary, the suspended sessions resume their operations as if nothing had happened. If the database (or an individual PDB) is not opened in the primary role, the sessions will be terminated.

Note:

Sessions that have long running queries or are using database links will not be retained regardless of the setting of this parameter.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB-GUID-07CB190C-C248-4FF5-AB64-EAA9C6D42677) for more information about real-time query mode
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SBYDB-GUID-857F6F45-DC1C-4345-BD39-F3BE7D79F1CD) for more information about preserving user sessions when a standby is converted to primary