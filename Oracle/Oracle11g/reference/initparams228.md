---
title: SEC_PROTOCOL_ERROR_TRACE_ACTION
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams228.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `SEC_PROTOCOL_ERROR_TRACE_ACTION = { NONE \| TRACE \| LOG \| ALERT }` |
| Default value | `TRACE` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`SEC_PROTOCOL_ERROR_TRACE_ACTION` specifies the action that the database should take when bad packets are received from a possibly malicious client.

Values:

- `NONE`
	The database server ignores the bad packets and does not generate any trace files or log messages.
- `TRACE`
	A detailed trace file is generated when bad packets are received, which can be used to debug any problems in client/server communication.
- `LOG`
	A minimal log message is printed in the alert logfile and in the server trace file. A minimal amount of disk space is used.
- `ALERT`
	An alert message is sent to a DBA or monitoring console.