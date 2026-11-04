---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SEC_PROTOCOL_ERROR_TRACE_ACTION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.324 SEC\_PROTOCOL\_ERROR\_TRACE\_ACTION

`SEC_PROTOCOL_ERROR_TRACE_ACTION` specifies the kind of logging the database server does when bad packets are received from a possibly malicious client, apart from the client receiving the error.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SEC_PROTOCOL_ERROR_TRACE_ACTION = { NONE \| TRACE \| LOG \| ALERT }` |
| Default value | `TRACE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

Values

- `NONE`
	The database server does not record it in any of the trace files.
- `TRACE`
	A short entry is made in the alert log file and a detailed incident file is generated. The server trace file also will have an entry about the protocol error and incident file.
- `LOG`
	The server trace file will have an entry about the protocol violation.
- `ALERT`
	A short entry is made in the alert log file and in the server trace file about the protocol violation.