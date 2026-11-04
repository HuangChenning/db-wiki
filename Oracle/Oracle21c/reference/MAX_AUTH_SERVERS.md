---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MAX_AUTH_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.199 MAX\_AUTH\_SERVERS

`MAX_AUTH_SERVERS` specifies the maximum number of authentication servers in the authentication pool. This pool authenticates user connections when client applications connect to Database Resident Connection Pooling (DRCP).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `25` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes, according to the following guidelines:  - When the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `true`, `MAX_AUTH_SERVERS` can be modified only at the PDB level; it cannot be modified for the CDB root. - When the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `false`, `MAX_AUTH_SERVERS` can be modified only for the CDB root; it cannot be modified at the PDB level. |
| Range of values | Minimum: `MIN_AUTH_SERVERS` or `1`, whichever is the greater value  Maximum: operating system-dependent |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

The value of this parameter must be greater than or equal to the value of the `MIN_AUTH_SERVERS` initialization parameter, which specifies the minimum number of authentication servers in the authentication pool. The exception is when `MIN_AUTH_SERVERS = 0`. In this case, the value of `MAX_AUTH_SERVERS` must be greater than or equal to `1`.

Note:

This parameter is available starting with Oracle Database release 19c, version 19.10.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-82FF6896-F57E-41CF-89F7-755F3BC9C924) for more information about setting this parameter
- " [ENABLE\_PER\_PDB\_DRCP](ENABLE_PER_PDB_DRCP.md) "
- " [MIN\_AUTH\_SERVERS](MIN_AUTH_SERVERS.md) "