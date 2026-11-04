---
title: SEC_CASE_SENSITIVE_LOGON
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams225.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `true \| false` |
| Basic | No |

`SEC_CASE_SENSITIVE_LOGON` enables or disables password case sensitivity in the database.

Values:

- `true`
	Database logon passwords are case sensitive.
- `false`
	Database logon passwords are not case sensitive.