---
title: ALL_XML_VIEW_COLS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2140.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XML_VIEW_COLS` describes the columns of the XML views accessible to the current user.

Related Views

- `DBA_XML_VIEW_COLS` describes the columns of all XML views in the database.
- `USER_XML_VIEW_COLS` describes the columns of the XML views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the XML view |
| `VIEW_NAME` | `VARCHAR2(30)` |  | Name of the XML view |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Name of the XML view column |
| `XMLSCHEMA` | `VARCHAR2(700)` |  | Name of the XML Schema that is used for the view definition |
| `SCHEMA_OWNER` | `VARCHAR2(30)` |  | Owner of the XML Schema that is used for the view definition |
| `ELEMENT_NAME` | `VARCHAR2(2000)` |  | Name of the XML SChema element that is used for the view |

See Also:

- ["DBA\_XML\_VIEW\_COLS"](statviews_5104.md)
- ["USER\_XML\_VIEW\_COLS"](statviews_5516.md)