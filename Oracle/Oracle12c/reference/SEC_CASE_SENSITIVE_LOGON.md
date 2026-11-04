---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SEC_CASE_SENSITIVE_LOGON.html
tags:
  - oracle
  - 12c
  - reference
---

`SEC_CASE_SENSITIVE_LOGON` enables or disables password case sensitivity in the database.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

Note:

The `SEC_CASE_SENSITIVE_LOGON` parameter is deprecated. It is retained for backward compatibility only. For more information about the deprecation of this parameter, see [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG3225).

Values

- `true`
	Database logon passwords are case sensitive.
- `false`
	Database logon passwords are not case sensitive.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG3225) for more details about the SEC\_CASE\_SENSITIVE\_LOGON parameter