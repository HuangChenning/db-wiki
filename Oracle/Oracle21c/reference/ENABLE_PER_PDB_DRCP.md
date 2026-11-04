---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ENABLE_PER_PDB_DRCP.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.124 ENABLE\_PER\_PDB\_DRCP

`ENABLE_PER_PDB_DRCP` controls whether Database Resident Connection Pooling (DRCP) configures one connection pool for the entire CDB or one isolated connection pool for each PDB.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

Possible values:

- `true`
	DRCP creates one isolated connection pool for each PDB. You can connect to a particular PDB and configure, manage, and monitor its connection pool according to the specific requirements for that PDB. For example, you can set values for the `MIN_AUTH_SERVERS`, `MAX_AUTH_SERVERS`, and `DRCP_DEDICATED_OPT` initialization parameters for a PDB, and you can use the `DBMS_CONNECTION_POOL` package to manage the connection pool for a PDB.
	When `ENABLE_PER_PDB_DRCP` is set to `true`, there is no connection pool for the entire CDB. The values of the `MIN_AUTH_SERVERS`, `MAX_AUTH_SERVERS`, and `DRCP_DEDICATED_OPT` initialization parameters have no meaning in the CDB root and you cannot alter them, nor can you use the `DBMS_CONNECTION_POOL` package while connected to the CDB root.
- `false`
	DRCP creates one connection pool for the entire CDB. This connection pool is shared by all PDBs. You can set the `MIN_AUTH_SERVERS`, `MAX_AUTH_SERVERS`, and `DRCP_DEDICATED_OPT` initialization parameters only in the CDB root, and you can use the `DBMS_CONNECTION_POOL` only while connected to the CDB root.

Note:

This parameter is available starting with Oracle Database 21c.