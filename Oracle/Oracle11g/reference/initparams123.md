---
title: LOG_ARCHIVE_CONFIG
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams123.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `LOG_ARCHIVE_CONFIG =` ``` { [ SEND \| NOSEND ] [ RECEIVE \| NORECEIVE ] [ DG_CONFIG=(remote_db_unique_name1 [, ... remote_db_unique_name30) \| NODG_CONFIG ] } ``` |
| Default value | `'SEND, RECEIVE, NODG_CONFIG'` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`LOG_ARCHIVE_CONFIG` enables or disables the sending of redo logs to remote destinations and the receipt of remote redo logs, and specifies the unique database names (`DB_UNIQUE_NAME`) for each database in the Data Guard configuration.

Values:

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