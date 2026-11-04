---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBMS_METADATA_TRANSFORMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.179 DBMS\_METADATA\_TRANSFORMS

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