---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-IM_COLUMN_LEVEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.1 V$IM\_COLUMN\_LEVEL

`V$IM_COLUMN_LEVEL` presents the selective column compression levels that are defined using the `inmemory_memcompress` clause of the `inmemory_column_clause` of the `CREATE TABLE` statement.

This view returns no rows for a table which has no associated selective column compression levels.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | Instance ID |
| `OWNER` | `VARCHAR2(31)` | Username of the table owner |
| `OBJ_NUM` | `NUMBER` | Table object number |
| `TABLE_NAME` | `VARCHAR2(31)` | Table name |
| `SEGMENT_COLUMN_ID` | `NUMBER` | Segment column number |
| `COLUMN_NAME` | `VARCHAR2(31)` | Column name |
| `INMEMORY_COMPRESSION` | `VARCHAR2(26)` | Column compression level. Possible values:  - `DEFAULT`: This value appears for physical columns of a table that do not have a selective column clause. It also appears when a virtual column has been explicitly enabled for in-memory storage using `ALTER TABLE ` table-name `INMEMORY(VC)`. - `UNSPECIFIED`: This value appears for virtual columns of a table that do not have a selective column clause.  If the `INMEMORY_VIRTUAL_COLUMNS` initialization parameter is set to `MANUAL`, a virtual column with a `DEFAULT INMEMORY_COMPRESSION` clause will be materialized while a virtual column with an `UNSPECIFIED` value will not be. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire multitenant container database (CDB). This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

The SYS\_IME hidden virtual columns automatically added by the In-Memory Expression (IME) infrastructure will not be shown in this view.

See Also:

- " [INMEMORY\_CLAUSE\_DEFAULT](INMEMORY_CLAUSE_DEFAULT.md) "
- " [V$IM\_SEGMENTS](V-IM_SEGMENTS.md) "
- " [V$IM\_USER\_SEGMENTS](V-IM_USER_SEGMENTS.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-BFA53515-7643-41E5-A296-654AB4A9F9E7) for an introduction to the IM column store
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF56769) for more information about the `inmemory_column_clause` of the SQL `CREATE TABLE` statement