---
title: ALL_XML_VIEWS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2141.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XML_VIEWS` describes the XML views accessible to the current user.

Related Views

- `DBA_XML_VIEWS` describes all XML views the database.
- `USER_XML_VIEWS` describes the XML views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the XML view |
| `VIEW_NAME` | `VARCHAR2(30)` |  | Name of the XML view |
| `XMLSCHEMA` | `VARCHAR2(700)` |  | Name of the XML Schema that is used for the view definition |
| `SCHEMA_OWNER` | `VARCHAR2(30)` |  | Owner of the XML Schema that is used for the view definition |
| `ELEMENT_NAME` | `VARCHAR2(2000)` |  | Name of the XML SChema element that is used for the view |

See Also:

- ["DBA\_XML\_VIEWS"](statviews_5105.md)
- ["USER\_XML\_VIEWS"](statviews_5517.md)