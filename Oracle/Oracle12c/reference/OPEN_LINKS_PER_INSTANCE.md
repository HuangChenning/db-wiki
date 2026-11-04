---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/OPEN_LINKS_PER_INSTANCE.html
tags:
  - oracle
  - 12c
  - reference
---

`OPEN_LINKS_PER_INSTANCE` specifies the maximum number of migratable open connections globally for each database instance.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `4` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 0 to 2 <sup>31</sup> - 1 |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

XA transactions use migratable open connections so that the connections are cached after a transaction is committed. Another transaction can use the connection, provided the user who created the connection is the same as the user who owns the transaction.

`OPEN_LINKS_PER_INSTANCE` is different from `OPEN_LINKS`, which indicates the number of connections from a session. The `OPEN_LINKS` parameter is not applicable to XA applications.