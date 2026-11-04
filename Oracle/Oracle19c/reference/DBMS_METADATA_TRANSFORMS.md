---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBMS_METADATA_TRANSFORMS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.176 DBMS\_METADATA\_TRANSFORMS

`DBMS_METADATA_TRANSFORMS` documents the valid Oracle-supplied transforms.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Object type name |
| `TRANSFORM` | `VARCHAR2(128)` | `NOT NULL` | Transform name |
| `INPUT_TYPE` | `VARCHAR2(24)` |  | Type of input document |
| `OUTPUT_TYPE` | `VARCHAR2(24)` |  | Type of output document |
| `DESCRIPTION` | `VARCHAR2(71)` |  | Description of the transform |

See Also:

- " [DBMS\_METADATA\_PARSE\_ITEMS](DBMS_METADATA_PARSE_ITEMS.md) "
- " [DBMS\_METADATA\_TRANSFORM\_PARAMS](DBMS_METADATA_TRANSFORM_PARAMS.md) "