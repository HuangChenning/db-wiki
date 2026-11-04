---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/MIN_AUTH_SERVERS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.214 MIN\_AUTH\_SERVERS

`MIN_AUTH_SERVERS` specifies the minimum number of authentication servers in the authentication pool. This pool authenticates user connections when client applications connect to Database Resident Connection Pooling (DRCP).

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | If the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `true`, then the default value for `MIN_AUTH_SERVERS` is `0` in each PDB.  If the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `false`, then the default value for `MIN_AUTH_SERVERS` is `1` in the CDB root. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes, according to the following guidelines:  - When the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `true`, `MIN_AUTH_SERVERS` can be modified only at the PDB level; it cannot be modified for the CDB root. - When the `ENABLE_PER_PDB_DRCP` initialization parameter is set to `false`, `MIN_AUTH_SERVERS` can be modified only for the CDB root; it cannot be modified at the PDB level. |
| Range of values | Minimum: `0`  Maximum: `MAX_AUTH_SERVERS` or `PROCESSES`, whichever is the lesser value |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

The value of this parameter must be less than or equal to the values of both the `MAX_AUTH_SERVERS` initialization parameter and the `PROCESSES` initialization parameter. The `MAX_AUTH_SERVERS` parameter specifies the maximum number of authentication servers in the authentication pool. The `PROCESSES` parameter specifies the maximum number of operating system user processes that can simultaneously connect to Oracle.

Note:

This parameter is available starting with Oracle Database release 19c, version 19.10.