---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBMS_METADATA_PARSE_ITEMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.177 DBMS\_METADATA\_PARSE\_ITEMS

`DBMS_METADATA_PARSE_ITEMS` documents the valid parse items.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Object type name |
| `PARSE_ITEM` | `VARCHAR2(124)` |  | Parse item name |
| `ALTER_XML` | `VARCHAR2(1)` |  | `Y`: Can be used when generating `ALTER_XML` document |
| `FETCH_XML_CLOB` | `VARCHAR2(1)` |  | `Y`: Can be returned by `FETCH_XML_CLOB` |
| `CONVERT` | `VARCHAR2(1)` |  | `Y`: Can be returned by `CONVERT` or `FETCH_DDL` |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the parse item |

See Also:

- " [DBMS\_METADATA\_TRANSFORM\_PARAMS](DBMS_METADATA_TRANSFORM_PARAMS.md) "
- " [DBMS\_METADATA\_TRANSFORMS](DBMS_METADATA_TRANSFORMS.md) "