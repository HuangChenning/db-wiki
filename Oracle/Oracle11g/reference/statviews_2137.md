---
title: ALL_XML_SCHEMAS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2137.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_XML_SCHEMAS` describes the registered XML schemas accessible to the current user.

Related Views

- `DBA_XML_SCHEMAS` describes all registered XML schemas in the database.
- `USER_XML_SCHEMAS` describes the registered XML schemas owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the XML schema |
| `SCHEMA_URL` | `VARCHAR2(700)` |  | Schema URL of the XML schema |
| `LOCAL` | `VARCHAR2(3)` |  | Indicates whether the XML schema is local (`YES`) or global (`NO`) |
| `SCHEMA` | `XMLTYPE` |  | XML schema document |
| `INT_OBJNAME` | `VARCHAR2(4000)` |  | Internal database object name for the schema |
| `QUAL_SCHEMA_URL` | `VARCHAR2(767)` |  | Fully qualified schema URL |
| `HIER_TYPE` | `VARCHAR2(11)` |  | Type of hierarchy for which the schema is enabled: |
| `BINARY` | `VARCHAR2(3)` |  | Indicates whether the XML Schema is registered for binary encoding usage (`YES`) or not (`NO`) |
| `SCHEMA_ID` | `RAW(16)` |  | Opaque schema identifier (16 bytes) |
| `HIDDEN` | `VARCHAR2(3)` |  | Indicates whether the XML Schema has been deleted in hidden mode (`YES`) or not (`NO`) |

See Also:

- ["DBA\_XML\_SCHEMAS"](statviews_5101.md)
- ["USER\_XML\_SCHEMAS"](statviews_5513.md)