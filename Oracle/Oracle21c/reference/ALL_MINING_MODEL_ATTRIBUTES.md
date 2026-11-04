---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MINING_MODEL_ATTRIBUTES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.273 ALL\_MINING\_MODEL\_ATTRIBUTES

`ALL_MINING_MODEL_ATTRIBUTES` describes the attributes of the machine learning models accessible to the current user.

Only the attributes in the model signature are included in this view. The attributes in the model signature correspond to the columns in the training data that were used to build the model.

Machine learning models are schema objects created by Oracle Machine Learning for SQL.

Related Views

- `DBA_MINING_MODEL_ATTRIBUTES` describes the attributes of all machine learning models in the database.
- `USER_MINING_MODEL_ATTRIBUTES` describes the attributes of the machine learning models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the machine learning model |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the machine learning model |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the attribute |
| `ATTRIBUTE_TYPE` | `VARCHAR2(11)` | – | Logical type of the attribute. The type is identified during the model build or apply process:  - `NUMERICAL`: Numeric data - `CATEGORICAL`: Character data - `TEXT`: Unstructured text data - `PARTITION`: The input signature column is used for the partitioning key - `MIXED`: The input signature column takes on more than one attribute type. 	This is due to user-defined embedded transformations that allow an input column to be transformed into multiple independent mining attributes, including mining attributes of different types. |
| `DATA_TYPE` | `VARCHAR2(106)` | – | Data type of the attribute |
| `DATA_LENGTH` | `NUMBER` | – | Length of the data type |
| `DATA_PRECISION` | `NUMBER` | – | Precision of a fixed point number. Precision, which is the total number of significant decimal digits, is represented as p in the data type `NUMBER(p,s)`. |
| `DATA_SCALE` | `NUMBER` | – | Scale of a fixed point number. Scale, which is the number of digits from the decimal to the least significant digit, is represented as s in the data type `NUMBER(p,s)`. |
| `USAGE_TYPE` | `VARCHAR2(8)` | – | Indicates whether the attribute was used to construct the model (`ACTIVE`) or not (`INACTIVE`). Some attributes may be eliminated by transformations or algorithmic processing. The `*_MINING_MODEL_ATTRIBUTES` view only lists the attributes used by the model, therefore the value of this column is always `ACTIVE`. |
| `TARGET` | `VARCHAR2(3)` | – | Indicates whether the attribute is the target of a predictive model (`YES`) or not (`NO`). The target describes the result that is produced when the model is applied. |
| `ATTRIBUTE_SPEC` | `VARCHAR2(4000)` | – | One or more keywords that identify special treatment for the attribute during model build. Values are:  - `FORCE_IN`: (GLM only) When feature selection is enabled, forces the inclusion of the attribute in the model build. Feature selection is disabled by default. If the model is not using GLM with feature selection enabled, this value is ignored. - `NOPREP`: When ADP is on, prevents automatic transformation of the attribute. If ADP is `OFF`, this value is ignored. - `TEXT`: Causes the attribute to be treated as unstructured text data. The `TEXT` value supports three subsettings: `POLICY_NAME`, `MAX_FEATURES`, `TOKEN_TYPE`, and `MIN_DOCUMENTS`. Subsettings are specified as name:value pairs within parentheses. For example: `(POLICY_NAME:mypolicy)` `(MAX_FEATURES:2000)(TOKEN_TYPE:THEME)`. See [Oracle Machine Learning for SQL API Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DMAPI-GUID-DC9371F7-B16A-43C7-A563-5C2016064E72) for details. - `NULL`: The `ATTRIBUTE_SPEC` for this attribute is `NULL`. 	`ATTRIBUTE_SPEC` is a parameter to the PL/SQL procedure `DBMS_DATA_MINING_TRANSFORM.SET_TRANSFORM`. See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73054) for details. |

See Also:

[Oracle Machine Learning for SQL API Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DMAPI-GUID-7AAB55D5-6711-4BE5-A0CE-B2A6B68ED689) for more information about the attributes of machine learning models