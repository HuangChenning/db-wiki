---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MINING_MODEL_XFORMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.277 ALL\_MINING\_MODEL\_XFORMS

`ALL_MINING_MODEL_XFORMS` describes the user-specified transformations embedded in all models accessible to the user.

Related Views

- `DBA_MINING_MODEL_XFORMS` describes the user-specified transformations embedded in all models accessible in the system.
- `USER_MINING_MODEL_XFORMS` describes the user-specified transformations embedded with the user's own models. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Name of the model owner |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the model |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` |  | Name of the attribute used in the transformation |
| `ATTRIBUTE_SUBNAME` | `VARCHAR2(4000)` |  | Subname of the attribute used in the transformation |
| `ATTRIBUTE_SPEC` | `VARCHAR2(4000)` |  | Attribute specification provided to model training |
| `EXPRESSION` | `CLOB` |  | Transformation expression provided to model training |
| `REVERSE` | `VARCHAR2(3)` |  | Indicates whether the specified transformation is a reverse transformation (`YES`) or a forward expression (`NO`) |