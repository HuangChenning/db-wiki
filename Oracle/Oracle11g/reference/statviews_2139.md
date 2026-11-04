---
title: ALL_XML_TABLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2139.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XML_TABLES` describes the XML tables accessible to the current user.

Related Views

- `DBA_XML_TABLES` describes all XML tables in the database.
- `USER_XML_TABLES` describes the XML tables owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the XML table |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Name of the XML table |
| `XMLSCHEMA` | `VARCHAR2(700)` |  | Name of the XML Schema that is used for the table definition |
| `SCHEMA_OWNER` | `VARCHAR2(30)` |  | Owner of the XML Schema that is used for the table definition |
| `ELEMENT_NAME` | `VARCHAR2(2000)` |  | Name of the XML SChema element that is used for the table |
| `STORAGE_TYPE` | `VARCHAR2(17)` |  | Storage option for the XMLtype data: |
| `ANYSCHEMA` | `VARCHAR2(3)` |  | If storage is `BINARY`, indicates whether the column allows `ANYSCHEMA` (`YES`) or not (`NO`), else NULL |
| `NONSCHEMA` | `VARCHAR2(3)` |  | If storage is `BINARY`, indicates whether the column allows `NONSCHEMA` (`YES`) or not (`NO`), else NULL |

See Also:

- ["DBA\_XML\_TABLES"](statviews_5103.md)
- ["USER\_XML\_TABLES"](statviews_5515.md)