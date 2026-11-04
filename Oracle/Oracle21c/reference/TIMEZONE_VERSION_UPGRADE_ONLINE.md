---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TIMEZONE_VERSION_UPGRADE_ONLINE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.366 TIMEZONE\_VERSION\_UPGRADE\_ONLINE

`TIMEZONE_VERSION_UPGRADE_ONLINE` enables you to keep the database running in normal mode while upgrading time zone data using the `DBMS_DST` package.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

In releases prior to Oracle Database 21c, you were required to put the database in `UPGRADE` mode in order to initiate a time zone data upgrade using the `DBMS_DST` package. Starting with Oracle Database 21c, you can perform such an upgrade while the database is in normal mode by setting the value of `TIMEZONE_VERSION_UPGRADE_ONLINE` to `true`.

Note:

Setting the value of this parameter is only one step in a series of steps for upgrading your time zone data. Refer to [Oracle Database Globalization Support Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=NLSPG-GUID-42DDBBFA-FF58-41B6-81A1-515FD7968A38) for the complete set of steps before you set this parameter value.