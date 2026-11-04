---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBMS_METADATA_TRANSFORM_PARAMS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBMS_METADATA_TRANSFORM_PARAMS` documents the valid transform parameters for each transform.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Object type name |
| `TRANSFORM` | `VARCHAR2(128)` | `NOT NULL` | Transform name |
| `PARAM` | `VARCHAR2(128)` | `NOT NULL` | Parameter name |
| `DATATYPE` | `VARCHAR2(11)` |  | `BOOLEAN`, `TEXT`, `NUMBER` or `UNSPECIFIED` |
| `DEFAULT_VAL` | `VARCHAR2(2000)` |  | Default value of transform parameter |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the transform parameter |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [DBMS\_METADATA\_PARSE\_ITEMS](DBMS_METADATA_PARSE_ITEMS.md) "
- " [DBMS\_METADATA\_TRANSFORMS](DBMS_METADATA_TRANSFORMS.md) "