---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_XML_VIEWS.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.155 ALL\_XML\_VIEWS

`ALL_XML_VIEWS` describes the XML views accessible to the current user.

Related Views

- `DBA_XML_VIEWS` describes all XML views the database.
- `USER_XML_VIEWS` describes the XML views owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the XML view |
| `VIEW_NAME` | `VARCHAR2(128)` |  | Name of the XML view |
| `XMLSCHEMA` | `VARCHAR2(700)` |  | Name of the XML Schema that is used for the view definition |
| `SCHEMA_OWNER` | `VARCHAR2(128)` |  | Owner of the XML Schema that is used for the view definition |
| `ELEMENT_NAME` | `VARCHAR2(2000)` |  | Name of the XML SChema element that is used for the view |

See Also:

- " [DBA\_XML\_VIEWS](DBA_XML_VIEWS.md) "
- " [USER\_XML\_VIEWS](USER_XML_VIEWS.md) "