---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/LOG_ARCHIVE_CONFIG.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.183 LOG\_ARCHIVE\_CONFIG

`LOG_ARCHIVE_CONFIG` enables or disables the sending of redo logs to remote destinations and the receipt of remote redo logs, and specifies the unique database names (`DB_UNIQUE_NAME`) for each database in the Data Guard configuration.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_ARCHIVE_CONFIG =`  ``` { [ SEND \| NOSEND ] [ RECEIVE \| NORECEIVE ] [ DG_CONFIG=(remote_db_unique_name1 [, ... remote_db_unique_name30) \| NODG_CONFIG ] } ``` |
| Default value | `NULL` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

Values

- `SEND`
	Enables the sending of redo logs to remote destinations
- `NOSEND`
	Disables the sending of redo logs to remote destinations
- `RECEIVE`
	Enables the receipt of remotely archived redo logs
- `NORECEIVE`
	Disables the receipt of remotely archived redo logs
- `DG_CONFIG`
	Specifies a list of up to 30 unique database names (defined with the `DB_UNIQUE_NAME` initialization parameter) for all of the databases in the Data Guard configuration.
- `NODG_CONFIG`
	Eliminates the list of service provider names previously specified with the `DG_CONFIG` option.

When this parameter has not been set, its default value is `NULL`. However, the `NULL` value is treated as if the parameter has been set to `‘SEND, RECEIVE, NODG_CONFIG’`.