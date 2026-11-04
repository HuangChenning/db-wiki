---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBMS_METADATA_TRANSFORMS.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Object type name |
| `TRANSFORM` | `VARCHAR2(128)` | `NOT NULL` | Transform name |
| `INPUT_TYPE` | `VARCHAR2(24)` |  | Type of input document |
| `OUTPUT_TYPE` | `VARCHAR2(24)` |  | Type of output document |
| `DESCRIPTION` | `VARCHAR2(71)` |  | Description of the transform |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBMS\_METADATA\_PARSE\_ITEMS](DBMS_METADATA_PARSE_ITEMS.md) "
- " [DBMS\_METADATA\_TRANSFORM\_PARAMS](DBMS_METADATA_TRANSFORM_PARAMS.md) "