---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/SEC_MAX_FAILED_LOGIN_ATTEMPTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.322 SEC\_MAX\_FAILED\_LOGIN\_ATTEMPTS

`SEC_MAX_FAILED_LOGIN_ATTEMPTS` specifies the number of authentication attempts that can be made by a client on a connection to the server process.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `3` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | An integer greater than or equal to `1`. |
| Basic | No |

These login attempts can be for multiple user accounts in the same connection. After the specified number of failure attempts, the connection will be automatically dropped by the server process, and the server process is terminated.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DBSEG-GUID-994A09FB-7D7A-44BC-9757-EAA6232CC3BA) for more information about this parameter