---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBMS_METADATA_TRANSFORM_PARAMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.178 DBMS\_METADATA\_TRANSFORM\_PARAMS

`DBMS_METADATA_TRANSFORM_PARAMS` documents the valid transform parameters for each transform.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OBJECT_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Object type name |
| `TRANSFORM` | `VARCHAR2(128)` | `NOT NULL` | Transform name |
| `PARAM` | `VARCHAR2(128)` | `NOT NULL` | Parameter name |
| `DATATYPE` | `VARCHAR2(11)` |  | `BOOLEAN`, `TEXT`, `NUMBER` or `UNSPECIFIED` |
| `DEFAULT_VAL` | `VARCHAR2(2000)` |  | Default value of the transform parameter |
| `CLIENT` | `VARCHAR2(1)` |  | Indicates whether the transform parameter is available to the Data Pump client (`Y`) or not (`N`) |
| `API` | `VARCHAR2(1)` |  | Indicates whether the transform parameter is available to the Data Pump API (`Y`) or not (`N`) |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the transform parameter |

See Also:

- " [DBMS\_METADATA\_PARSE\_ITEMS](DBMS_METADATA_PARSE_ITEMS.md) "
- " [DBMS\_METADATA\_TRANSFORMS](DBMS_METADATA_TRANSFORMS.md) "