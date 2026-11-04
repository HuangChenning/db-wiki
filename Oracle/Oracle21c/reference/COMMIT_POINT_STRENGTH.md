---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/COMMIT_POINT_STRENGTH.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.46 COMMIT\_POINT\_STRENGTH

`COMMIT_POINT_STRENGTH` specifies a value that determines the commit point site in a distributed transaction.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | `0` to `255` |
| Basic | No |

Note:

This parameter is relevant only in distributed database systems.

The node in the transaction with the highest value for `COMMIT_POINT_STRENGTH` will be the commit point site.

The commit point site of a database should reflect the amount of critical shared data in the database. For example, a database on a mainframe computer typically shares more data among users than one on a personal computer. Therefore, `COMMIT_POINT_STRENGTH` should be set to a higher value for the mainframe computer.

The commit point site stores information about the status of transactions. Other computers in a distributed transaction require this information during Oracle's two-phase commit, so it is desirable to have machines that are always available as commit point sites. Therefore, set `COMMIT_POINT_STRENGTH` to a higher value on your more available machines.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT041) and [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN12119) for information on two-phase commit
- Your operating system-specific Oracle documentation for the default value of this parameter