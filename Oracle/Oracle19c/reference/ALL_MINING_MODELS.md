---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_MINING_MODELS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.270 ALL\_MINING\_MODELS

`ALL_MINING_MODELS` describes the mining models accessible to the current user.

Mining models are schema objects created by Oracle Data Mining.

Related Views

- `DBA_MINING_MODELS` describes all mining models in the database.
- `USER_MINING_MODELS` describes the mining models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the mining model |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the mining model |
| `MINING_FUNCTION` | `VARCHAR2(30)` | `NOT NULL` | Function of the mining model. The function identifies the class of problems that can be solved by this model. The mining function is specified when the model is built:  - `CLASSIFICATION` - `REGRESSION` - `CLUSTERING` - `FEATURE_EXTRACTION` - `ASSOCIATION_RULES` - `ATTRIBUTE_IMPORTANCE` |
| `ALGORITHM` | `VARCHAR2(30)` | `NOT NULL` | Algorithm used by the model. Each mining function has a default algorithm. The default can be overridden with a model setting (see `*_MINING_MODEL_SETTINGS`):  - `CUR_DECOMPOSITION` - `NAIVE_BAYES` - `DECISION_TREE` - `EXPLICIT_SEMANTIC_ANALYS` - `EXPONENTIAL_ SMOOTHING` - `SUPPORT_VECTOR_MACHINES` - `KMEANS` - `O_CLUSTER` - `NONNEGATIVE_MATRIX_FACTOR` - `NEURAL_NETWORK` - `GENERALIZED_LINEAR_MODEL` - `APRIORI_ASSOCIATION_RULES` - `MINIMUM_DESCRIPTION_LENGTH` - `EXPECTATION_MAXIMIZATION` - `RANDOM_FOREST` - `SINGULAR_VALUE_DECOMP` - `R_EXTENSIBLE` |
| `ALGORITHM_TYPE` | `VARCHAR2(10)` | `NOT NULL` | Algorithm type of the model |
| `CREATION_DATE` | `DATE` | `NOT NULL` | Date that the model was created |
| `BUILD_DURATION` | `NUMBER` | `NOT NULL` | Time (in seconds) of the model build process |
| `MODEL_SIZE` | `NUMBER` | `NOT NULL` | Size of the model (in megabytes) |
| `PARTITIONED` | `VARCHAR2(3)` | `NOT NULL` | Indicates whether the model is partitioned or not. Possible values:  - `YES`: The model is partitioned. - `NO`: The model is not partitioned |