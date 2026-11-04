---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/STANDBY_DB_PRESERVE_STATES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.350 STANDBY\_DB\_PRESERVE\_STATES

`STANDBY_DB_PRESERVE_STATES` controls whether user sessions, buffers, and other internal states of the instance are retained when a readable physical standby database is converted to a primary database. This parameter is meaningful on a physical standby database that is open in real-time query mode.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `STANDBY_DB_PRESERVE_STATES = { NONE \| SESSION \| BUFFER \| ALL }` |
| Default value | `NONE` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Values

- `NONE`
	Nothing is retained. All sessions are disconnected and all buffers are flushed. This is the default value.
- `SESSION`
	The role transition waits 10 seconds for active sessions to finish the current statement or top-level PL/SQL call. The sessions that are still active after 10 seconds are terminated. The sessions that complete their work in this lap of time are retained, along with inactive sessions. If the database is reopened as the primary within 300 seconds, the retained sessions resume their operations as if nothing had happened. If the database (or individual PDB) is not opened in the primary role within 300 seconds, the sessions will be terminated.
- `BUFFER`
	All current buffers are retained. Media recovery buffers are converted to current buffers and retained, if possible. When the database is reopened as the primary, the retained buffers are available for use, which may enable queries to run faster during the first few minutes of operation. If the database (or an individual PDB) is not opened in the primary role, the buffers will be flushed.
- `ALL`
	This value is equivalent to setting both the `SESSION` and `BUFFER` values.

Note:

Sessions that have long running queries or are using database links will not be retained regardless of the setting of this parameter.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB-GUID-07CB190C-C248-4FF5-AB64-EAA9C6D42677) for more information about real-time query mode
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB-GUID-857F6F45-DC1C-4345-BD39-F3BE7D79F1CD) for more information about preserving user sessions and buffers when a standby database is converted to a primary database