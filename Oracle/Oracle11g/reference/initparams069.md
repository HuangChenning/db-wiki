---
title: DB_ULTRA_SAFE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams069.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_ULTRA_SAFE = { OFF \| DATA_ONLY \| DATA_AND_INDEX }` |
| Default value | `OFF` |
| Modifiable | No |
| Basic | No |

`DB_ULTRA_SAFE` sets the default values for other parameters that control protection levels.

Values:

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