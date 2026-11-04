---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SEC_RETURN_SERVER_RELEASE_BANNER.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.325 SEC\_RETURN\_SERVER\_RELEASE\_BANNER

`SEC_RETURN_SERVER_RELEASE_BANNER` specifies whether the server returns complete database software information to unauthenticated clients.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

Values

- `true`
	Returns complete database version information to the client.
- `false`
	Returns a generic version string to the client.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=LNOCI16581) and [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG162) for more information on controlling the display of the database version banner.