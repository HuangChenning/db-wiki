---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_MINING_MODEL_VIEWS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.268 ALL\_MINING\_MODEL\_VIEWS

`ALL_MINING_MODEL_VIEWS` provides a description of all the model views accessible to the user.

Related Views

- `DBA_MINING_MODEL_VIEWS` provides a description of all the model views in the database.
- `USER_MINING_MODEL_VIEWS` provides a description of the user's own model views. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the model view |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the model to which model views belongs |
| `VIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the model view |
| `VIEW_TYPE` | `VARCHAR2(128)` | – | Type of the model view |

See Also:

" [ALL\_MINING\_MODEL\_VIEWS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=DMPRG-GUID-69D3A987-CCD8-435A-B624-B3FD0583F02B) " in Oracle Data Mining User’s Guide