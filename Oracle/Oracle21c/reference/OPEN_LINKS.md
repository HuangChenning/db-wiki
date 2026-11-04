---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPEN_LINKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.238 OPEN\_LINKS

`OPEN_LINKS` specifies the maximum number of concurrent open connections to remote databases in one session. These connections include database links, as well as external procedures and cartridges, each of which uses a separate process.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | 0 to 32768 |
| Basic | No |

Oracle counts one open link for the following:

- For each user that references a public or private database link
- For each external procedure or cartridge connection when it is executed for the first time

Both types of connections close when the session ends. You can also close a database link connection explicitly by issuing an `ALTER SESSION CLOSE DATABASE LINK` statement.

You should set this parameter to allow for the external procedure and cartridge connections expected during the session plus the number of databases referred to in typical distributed transactions (that is, a single SQL statement that references multiple databases), so that all the databases can be open to execute the statement. For example, if queries alternately access databases A, B, and C, and `OPEN_LINKS` is set to `2`, time will be lost waiting while one connection is broken and another made. Increase the value if many different databases are accessed over time.

This parameter refers only to connections used for distributed transactions. Direct connections to a remote database specified as an application connects are not counted.

If you set `OPEN_LINKS` to `0`, then no distributed transactions are allowed.

In a multitenant container database (CDB), the `OPEN_LINKS` parameter can be set at both the root and at the PDB level using either an initialization parameter file (PFILE) or server parameter file (SPFILE). You need to restart the instance or reopen the PDB for a new `OPEN_LINKS` value to become effective.