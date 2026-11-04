---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_XML_TAB_COLS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.154 ALL\_XML\_TAB\_COLS

`ALL_XML_TAB_COLS` describes the columns of the XML tables accessible to the current user.

Related Views

- `DBA_XML_TAB_COLS` describes the columns of all XML tables in the database.
- `USER_XML_TAB_COLS` describes the columns of the XML tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the XML table |
| `TABLE_NAME` | `VARCHAR2(128)` |  | Name of the XML table |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the XML table column |
| `XMLSCHEMA` | `VARCHAR2(700)` |  | Name of the XML Schema that is used for the table definition |
| `SCHEMA_OWNER` | `VARCHAR2(128)` |  | Owner of the XML Schema that is used for the table definition |
| `ELEMENT_NAME` | `VARCHAR2(2000)` |  | Name of the XML SChema element that is used for the table |
| `STORAGE_TYPE` | `VARCHAR2(17)` |  | Storage option for the XMLType data:  - `OBJECT-RELATIONAL` - `BINARY` - `CLOB`  Note: The `CLOB` storage option for XMLType data is deprecated in Oracle Database 12c Release 1 (12.1). Oracle recommends using the `BINARY` storage option, instead. |
| `ANYSCHEMA` | `VARCHAR2(3)` |  | If storage is `BINARY`, indicates whether the column allows `ANYSCHEMA` (`YES`) or not (`NO`), else NULL |
| `NONSCHEMA` | `VARCHAR2(3)` |  | If storage is `BINARY`, indicates whether the column allows `NONSCHEMA` (`YES`) or not (`NO`), else NULL |
| `TOKENSETS` | `VARCHAR2(4000)` |  | This column is for internal use only. |

See Also:

- " [DBA\_XML\_TAB\_COLS](DBA_XML_TAB_COLS.md) "
- " [USER\_XML\_TAB\_COLS](USER_XML_TAB_COLS.md) "