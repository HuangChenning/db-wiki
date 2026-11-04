---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_DIM_MODELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.148 ALL\_CUBE\_DIM\_MODELS

`ALL_CUBE_DIM_MODELS` describes the models for the OLAP dimensions accessible to the current user.

Related Views

- `DBA_CUBE_DIM_MODELS` describes the models for all OLAP dimensions in the database.
- `USER_CUBE_DIM_MODELS` describes the models for the OLAP dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a cube dimension |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of a model for the cube dimension |
| `MODEL_ID` | `NUMBER` | `NOT NULL` | ID of the model |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the model in the session language |

See Also:

- " [DBA\_CUBE\_DIM\_MODELS](DBA_CUBE_DIM_MODELS.md) "
- " [USER\_CUBE\_DIM\_MODELS](USER_CUBE_DIM_MODELS.md) "