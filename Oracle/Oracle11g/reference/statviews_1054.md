---
title: ALL_CUBE_DIM_MODELS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1054.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_DIM_MODELS` describes the models for the OLAP dimensions accessible to the current user.

Related Views

- `DBA_CUBE_DIM_MODELS` describes the models for all OLAP dimensions in the database.
- `USER_CUBE_DIM_MODELS` describes the models for the OLAP dimensions owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the cube dimension |
| `DIMENSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a cube dimension |
| `MODEL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of a model for the cube dimension |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the model in the session language |

See Also:

- ["DBA\_CUBE\_DIM\_MODELS"](statviews_3130.md)
- ["USER\_CUBE\_DIM\_MODELS"](statviews_5266.md)