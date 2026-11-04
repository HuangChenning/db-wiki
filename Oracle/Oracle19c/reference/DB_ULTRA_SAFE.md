---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_ULTRA_SAFE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.97 DB\_ULTRA\_SAFE

`DB_ULTRA_SAFE` sets the default values for other parameters that control protection levels.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_ULTRA_SAFE = { OFF \| DATA_ONLY \| DATA_AND_INDEX }` |
| Default value | `OFF` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Basic | No |

Values

- `OFF`
	When any of `DB_BLOCK_CHECKING`, `DB_BLOCK_CHECKSUM`, or `DB_LOST_WRITE_PROTECT` are explicitly set, no changes are made.
- `DATA_ONLY`
	- `DB_BLOCK_CHECKING` will be set to `MEDIUM`.
		- `DB_LOST_WRITE_PROTECT` will be set to `TYPICAL`.
		- `DB_BLOCK_CHECKSUM` will be set to `FULL`.
- `DATA_AND_INDEX`
	- `DB_BLOCK_CHECKING` will be set to `FULL`.
		- `DB_LOST_WRITE_PROTECT` will be set to `TYPICAL`.
		- `DB_BLOCK_CHECKSUM` will be set to `FULL`.