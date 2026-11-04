---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JSON_COLUMNS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.256 ALL\_JSON\_COLUMNS

`ALL_JSON_COLUMNS` provides information on the JavaScript Object Notation (JSON) columns accessible to the current user.

This view displays information on table and view columns that are guaranteed to return JSON data. These include:

- Columns of data type `JSON`
- Columns on which a check constraint containing the `IS` `JSON` condition is defined, where the `IS` `JSON` condition is always enforced. Such check constraints can contain only the `IS` `JSON` condition, or they can contain the `IS` `JSON` condition as part of a logical `AND` condition.
	For example, the following check constraints ensure that the `IS` `JSON` condition is always enforced and will therefore cause `mycol` to appear in the `ALL_JSON_COLUMNS` view:
	```
	mycol IS JSON
	mycol IS JSON AND LENGTH(mycol) > 100
	```
	However, the following check constraint does not ensure that the `IS` `JSON` condition is enforced, because it is part of a logical `OR` condition, and will therefore cause `mycol` to be omitted from the `ALL_JSON_COLUMNS` view:
	```
	mycol IS JSON OR LENGTH(mycol) > 100
	```
- View columns that are defined as the return value of a SQL function that returns JSON data. Such functions include:
	- `TREAT` `(` `expr` `AS` `JSON` `)`
		- `JSON_ARRAY`, `JSON_ARRAYAGG`, `JSON_MERGEPATCH`, `JSON_OBJECT`, `JSON_OBJECTAGG`, `JSON_QUERY`, `JSON_SERIALIZE`, and `JSON_TRANSFORM`
	For example, in the following definition for view `v1`, column `mycol` is defined as the return value of the `JSON_OBJECT` function, which will therefore cause `mycol` to appear in the `ALL_JSON_COLUMNS` view:
	```
	CREATE TABLE t1 (text varchar2(100));
	CREATE VIEW v1 AS SELECT JSON_OBJECT(text) AS mycol FROM t1;
	```

Related Views

- `DBA_JSON_COLUMNS` provides information on all JSON columns.
- `USER_JSON_COLUMNS` provides information on the JSON columns for which the user is the owner. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the table with the JSON column |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the table with the JSON column |
| `OBJECT_TYPE` | `VARCHAR2(5)` |  | Object type:  - `TABLE` - `VIEW` |
| `COLUMN_NAME` | `VARCHAR2(128)` |  | Name of the JSON column |
| `FORMAT` | `VARCHAR2(9)` |  | Format of the JSON data |
| `DATA_TYPE` | `VARCHAR2(13)` |  | Data type of the JSON column |

See Also:

- " [DBA\_JSON\_COLUMNS](DBA_JSON_COLUMNS.md) "
- " [USER\_JSON\_COLUMNS](USER_JSON_COLUMNS.md) "
- [Oracle Database JSON Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADJSN-GUID-A8A58B49-13A5-4F42-8EA0-508951DAE0BB) for more information about using JSON with Oracle Database