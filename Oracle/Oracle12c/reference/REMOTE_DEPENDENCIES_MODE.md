---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/REMOTE_DEPENDENCIES_MODE.html
tags:
  - oracle
  - 12c
  - reference
---

`REMOTE_DEPENDENCIES_MODE` specifies how Oracle should handle dependencies upon remote PL/SQL stored procedures.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REMOTE_DEPENDENCIES_MODE = { TIMESTAMP \| SIGNATURE }` |
| Default value | `TIMESTAMP` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `TIMESTAMP`
	The client running the procedure compares the timestamp recorded on the server-side procedure with the current timestamp of the local procedure and executes the procedure only if the timestamps match.
- `SIGNATURE`
	Oracle allows the procedure to execute as long as the signatures are considered safe. This setting allows client PL/SQL applications to be run without recompilation.