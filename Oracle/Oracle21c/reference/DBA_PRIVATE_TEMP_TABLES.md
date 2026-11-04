---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PRIVATE_TEMP_TABLES.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.253 DBA\_PRIVATE\_TEMP\_TABLES

`DBA_PRIVATE_TEMP_TABLES` describes all of the private temporary tables in the database.

Related View

`USER_PRIVATE_TEMP_TABLES` describes the private temporary tables in the current session. This view does not display the `INST_ID` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SID` | `NUMBER` |  | Session ID of the session that created the private temporary table |
| `SERIAL#` | `NUMBER` |  | Session serial number of the session that created the private temporary table |
| `INST_ID` | `NUMBER` |  | Instance ID of the session that created the private temporary table |
| `OWNER` | `VARCHAR2(128)` |  | Owner name of the private temporary table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Private temporary table name |
| `TABLESPACE_NAME` | `VARCHAR2(128)` |  | Private temporary table's tablespace name |
| `DURATION` | `VARCHAR2(128)` |  | Private temporary table's duration (for example, `SESSION` or `TRANSACTION`) |
| `NUM_ROWS` | `NUMBER` |  | Number of rows in the private temporary table when analyzed |
| `BLOCKS` | `NUMBER` |  | Number of blocks used by private temporary table |
| `AVG_ROW_LEN` | `NUMBER` |  | Average row length |
| `LAST_ANALYZED` | `DATE` |  | Timestamp of last analyze |
| `TXN_ID` | `RAW(8)` |  | Transaction ID of the transaction duration private temporary table |
| `SAVE_POINT_NUM` | `NUMBER` |  | Save point number of the transaction duration private temporary table |

See Also:

- " [USER\_PRIVATE\_TEMP\_TABLES](USER_PRIVATE_TEMP_TABLES.md) "
- " [PRIVATE\_TEMP\_TABLE\_PREFIX](PRIVATE_TEMP_TABLE_PREFIX.md) "
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADMIN-GUID-6EB347F0-64BA-4B15-8182-41BA7D5A876F) for an introduction to private temporary tables