---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MINING_MODELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.278 ALL\_MINING\_MODELS

`ALL_MINING_MODELS` describes the machine learning models accessible to the current user.

Mining models are schema objects created by Oracle Machine Learning for SQL.

Related Views

- `DBA_MINING_MODELS` describes all machine learning models in the database.
- `USER_MINING_MODELS` describes the machine learning models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the machine learning model |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the machine learning model |
| `MINING_FUNCTION` | `VARCHAR2(30)` | `NOT NULL` | Function of the mining model. The function identifies the class of problems that can be solved by this model. The machine learning function is specified when the model is built:  - `CLASSIFICATION` - `REGRESSION` - `CLUSTERING` - `FEATURE_EXTRACTION` - `ASSOCIATION_RULES` - `ATTRIBUTE_IMPORTANCE` - `TIME_SERIES` |
| `ALGORITHM` | `VARCHAR2(30)` | `NOT NULL` | Algorithm used by the model. Each machine learning function has a default algorithm. The default can be overridden with a model setting (see `*_MINING_MODEL_SETTINGS`):  - `APRIORI_ASSOCIATION_RULES` - `CUR_DECOMPOSITION` - `DECISION_TREE` - `EXPECTATION_MAXIMIZATION` - `EXPLICIT_SEMANTIC_ANALYS` - `EXPONENTIAL_SMOOTHING` - `EXTENSIBLE_LANG` - `GENERALIZED_LINEAR_MODEL` - `KMEANS` - `MINIMUM_DESCRIPTION_LENGTH` - `MSET_SPRT` - `NAIVE_BAYES` - `NEURAL_NETWORK` - `NONNEGATIVE_MATRIX_FACTOR` - `O_CLUSTER` - `RANDOM_FOREST` - `SUPPORT_VECTOR_MACHINE` - `SINGULAR_VALUE_DECOMP` - `XGBOOST` |
| `ALGORITHM_TYPE` | `VARCHAR2(10)` | `NOT NULL` | Algorithm type of the model |
| `CREATION_DATE` | `DATE` | `NOT NULL` | Date that the model was created |
| `BUILD_DURATION` | `NUMBER` | `NOT NULL` | Time (in seconds) of the model build process |
| `MODEL_SIZE` | `NUMBER` | `NOT NULL` | Size of the model (in megabytes) |
| `PARTITIONED` | `VARCHAR2(3)` | `NOT NULL` | Indicates whether the model is partitioned or not. Possible values:  - `YES`: The model is partitioned. - `NO`: The model is not partitioned |