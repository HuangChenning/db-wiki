---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INSTANCE_NUMBER.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.165 INSTANCE\_NUMBER

`INSTANCE_NUMBER` specifies a unique number that maps the instance to one free list group for each database object created with storage parameter `FREELIST GROUPS`.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` (zero) |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 1 to maximum number of instances specified when the database was created |
| Basic | Yes |
| Oracle RAC | You must set this parameter for every instance, and all instances must have different values. |

`INSTANCE_NUMBER` is an Oracle RAC parameter that can be specified in parallel mode or exclusive mode.

The `INSTANCE` parameter of the `ALTER TABLE ... ALLOCATE EXTENT` statement assigns an extent to a particular free list group. If you set `INSTANCE_NUMBER` to the value specified for the `INSTANCE` parameter, the instance uses that extent for inserts and for updates that expand rows.

The practical maximum value of this parameter is the maximum number of instances specified in the `CREATE DATABASE` statement. The absolute maximum is operating system-dependent.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD817) for more information