---
title: ALL_MINING_MODEL_ATTRIBUTES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1140.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MINING_MODEL_ATTRIBUTES` describes the attributes of the mining models accessible to the current user.

Attributes correspond to the columns of data used to build a model. Columns with the same names and data types should be available in any data set to which the model is applied.

Related Views

- `DBA_MINING_MODEL_ATTRIBUTES` describes the attributes of all mining models in the database.
- `USER_MINING_MODEL_ATTRIBUTES` describes the attributes of the mining models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the mining model |
| `MODEL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the mining model |
| `ATTRIBUTE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the attribute |
| `ATTRIBUTE_TYPE` | `VARCHAR2(11)` |  | Logical type of the attribute. The type is identified during the model build or apply process: - `NUMERICAL` - Numeric data - `CATEGORICAL` - Character data |
| `DATA_TYPE` | `VARCHAR2(12)` |  | Data type of the attribute: - `VARCHAR2` - `NUMBER` - `FLOAT` - `CHAR` - `NESTED TABLE` |
| `DATA_LENGTH` | `NUMBER` |  | Length of the data type |
| `DATA_PRECISION` | `NUMBER` |  | Precision of a fixed point number. Precision, which is the total number of significant decimal digits, is represented as p in the data type `NUMBER(p,s)`. |
| `DATA_SCALE` | `NUMBER` |  | Scale of a fixed point number. Scale, which is the number of digits from the decimal to the least significant digit, is represented as s in the data type `NUMBER(p,s)`. |
| `USAGE_TYPE` | `VARCHAR2(8)` |  | Indicates whether the attribute was used to construct the model (`ACTIVE`) or not (`INACTIVE`). Some attributes may be eliminated by transformations or algorithmic processing. The `*_MINING_MODEL_ATTRIBUTES` view only lists the attributes used by the model, therefore the value of this column is always `ACTIVE`. |
| `TARGET` | `VARCHAR2(3)` |  | Indicates whether the attribute is the target of a predictive model (`YES`) or not (`NO`). The target describes the result that is produced when the model is applied. |

See Also:

- ["DBA\_MINING\_MODEL\_ATTRIBUTES"](statviews_4134.md)
- ["USER\_MINING\_MODEL\_ATTRIBUTES"](statviews_5355.md)
- [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/toc.htm) for information about model attributes