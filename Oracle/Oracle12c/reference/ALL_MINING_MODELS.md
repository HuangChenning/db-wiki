---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_MINING_MODELS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_MINING_MODELS` describes the mining models accessible to the current user.

Mining models are schema objects created by Oracle Data Mining.

Related Views

- `DBA_MINING_MODELS` describes all mining models in the database.
- `USER_MINING_MODELS` describes the mining models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the mining model |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the mining model |
| `MINING_FUNCTION` | `VARCHAR2(30)` |  | Function of the mining model. The function identifies the class of problems that can be solved by this model. The mining function is specified when the model is built:  - `CLASSIFICATION` - `REGRESSION` - `CLUSTERING` - `FEATURE_EXTRACTION` - `ASSOCIATION_RULES` - `ATTRIBUTE_IMPORTANCE` |
| `ALGORITHM` | `VARCHAR2(30)` |  | Algorithm used by the model. Each mining function has a default algorithm. The default can be overridden with a model setting (see `*_MINING_MODEL_SETTINGS`):  - `NAIVE_BAYES` - `DECISION_TREE` - `EXPLICIT_SEMANTIC_ANALYS` - `SUPPORT_VECTOR_MACHINES` - `KMEANS` - `O_CLUSTER` - `NONNEGATIVE_MATRIX_FACTOR` - `GENERALIZED_LINEAR_MODEL` - `APRIORI_ASSOCIATION_RULES` - `MINIMUM_DESCRIPTION_LENGTH` - `EXPECTATION_MAXIMIZATION` - `SINGULAR_VALUE_DECOMP` - `R_EXTENSIBLE` |
| `CREATION_DATE` | `DATE` | `NOT NULL` | Date that the model was created |
| `BUILD_DURATION` | `NUMBER` |  | Time (in seconds) of the model build process |
| `MODEL_SIZE` | `NUMBER` |  | Size of the model (in megabytes) |
| `PARTITIONED` | `VARCHAR2(3)` |  | Indicates whether the model is partitioned or not. Possible values:  - `YES`: The model is partitioned. - `NO`: The model is not partitioned |