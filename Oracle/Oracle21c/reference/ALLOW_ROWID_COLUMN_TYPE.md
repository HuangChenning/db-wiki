---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALLOW_ROWID_COLUMN_TYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.12 ALLOW\_ROWID\_COLUMN\_TYPE

`ALLOW_ROWID_COLUMN_TYPE` determines whether table columns of data type `ROWID` are allowed to be created.

Note:

This parameter is valid only for Oracle Autonomous Database on dedicated Exadata infrastructure. On other types of Oracle databases, the value of this parameter is ignored and `ROWID` columns are always allowed to be created.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Multiple instances should use the same value |

Values:

- `false`
	Columns of data type `ROWID` are not allowed.
	You cannot specify `ROWID` columns when creating tables, nor can you add `ROWID` columns to existing tables. If the value of this parameter is changed from `true` to `false` at a time when `ROWID` columns exist in the database, then those columns are allowed to remain. However, Oracle recommends that you leave this parameter set to its default value of `false` and avoid introducing `ROWID` columns into Oracle Autonomous Database on dedicated Exadata infrastructure.
- `true`
	Columns of data type `ROWID` are allowed.
	If you choose this setting, be aware that `ROWID` columns are incompatible with rolling upgrade operations and other internal operations that physically move table rows. At a minimum, database activities involving `ROWID` columns should be suspended during upgrades. Applications using `ROWID` columns should introduce correctness validation to mitigate against logical errors in the application if a row relocates.