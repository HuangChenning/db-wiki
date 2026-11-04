---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBMS_METADATA_PARSE_ITEMS.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Object type name |
| `PARSE_ITEM` | `VARCHAR2(124)` |  | Parse item name |
| `ALTER_XML` | `VARCHAR2(1)` |  | `Y`: Can be used when generating `ALTER_XML` document |
| `FETCH_XML_CLOB` | `VARCHAR2(1)` |  | `Y`: Can be returned by `FETCH_XML_CLOB` |
| `CONVERT` | `VARCHAR2(1)` |  | `Y`: Can be returned by `CONVERT` or `FETCH_DDL` |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the parse item |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBMS\_METADATA\_TRANSFORM\_PARAMS](DBMS_METADATA_TRANSFORM_PARAMS.md) "
- " [DBMS\_METADATA\_TRANSFORMS](DBMS_METADATA_TRANSFORMS.md) "