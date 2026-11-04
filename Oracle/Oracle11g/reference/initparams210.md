---
title: REMOTE_DEPENDENCIES_MODE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams210.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `REMOTE_DEPENDENCIES_MODE = { TIMESTAMP \| SIGNATURE }` |
| Default value | `TIMESTAMP` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |

`REMOTE_DEPENDENCIES_MODE` specifies how Oracle should handle dependencies upon remote PL/SQL stored procedures.

Values:

- `TIMESTAMP`
	The client running the procedure compares the timestamp recorded on the server-side procedure with the current timestamp of the local procedure and executes the procedure only if the timestamps match.
- `SIGNATURE`
	Oracle allows the procedure to execute as long as the signatures are considered safe. This setting allows client PL/SQL applications to be run without recompilation.

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm) for information about the consequences of the settings of this parameter