---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/MIN_AUTH_SERVERS.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.217 MIN\_AUTH\_SERVERS

`MIN_AUTH_SERVERS` specifies the minimum number of authentication servers in the authentication pool. This pool authenticates user connections when client applications connect to Database Resident Connection Pooling (DRCP).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Minimum: `0`  Maximum: `MAX_AUTH_SERVERS` or `PROCESSES`, whichever is the lesser value |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

The value of this parameter must be less than or equal to the values of both the `MAX_AUTH_SERVERS` initialization parameter and the `PROCESSES` initialization parameter. `MAX_AUTH_SERVERS` specifies the maximum number of authentication servers in the authentication pool. `PROCESSES` specifies the maximum number of operating system user processes that can simultaneously connect to Oracle.

Note:

This parameter is available starting with Oracle Database 19c, Release Update 19.10.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ADMIN-GUID-82FF6896-F57E-41CF-89F7-755F3BC9C924) for more information about setting this parameter
- " [MAX\_AUTH\_SERVERS](MAX_AUTH_SERVERS.md) "
- " [PROCESSES](PROCESSES.md) "