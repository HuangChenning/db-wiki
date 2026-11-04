---
title: ALL_MINING_MODELS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1142.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MINING_MODELS` describes the mining models accessible to the current user.

Related Views

- `DBA_MINING_MODELS` describes all mining models in the database.
- `USER_MINING_MODELS` describes the mining models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the mining model |
| `MODEL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the mining model |
| `MINING_FUNCTION` | `VARCHAR2(30)` |  | Function of the mining model. The function identifies the class of problems that can be solved by this model. The mining function is specified when the model is built: - `CLASSIFICATION` - `REGRESSION` - `CLUSTERING` - `FEATURE_EXTRACTION` - `ASSOCIATION_RULES` - `ATTRIBUTE_IMPORTANCE` |
| `ALGORITHM` | `VARCHAR2(30)` |  | Algorithm used by the model. Each mining function has a default algorithm. The default can be overridden with a model setting (see `*_MINING_MODEL_SETTINGS`): - `NAIVE_BAYES` - `ADAPTIVE_BAYES_NETWORK` - `DECISION_TREE` - `SUPPORT_VECTOR_MACHINES` - `KMEANS` - `O_CLUSTER` - `NONNEGATIVE_MATRIX_FACTOR` - `GENERALIZED_LINEAR_MODEL` - `APRIORI_ASSOCIATION_RULES` - `MINIMUM_DESCRIPTION_LENGTH` |
| `CREATION_DATE` | `DATE` | `NOT NULL` | Date that the model was created |
| `BUILD_DURATION` | `NUMBER` |  | Time (in seconds) of the model build process |
| `MODEL_SIZE` | `NUMBER` |  | Size of the model (in megabytes) |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comment applied to the model with a SQL `COMMENT` statement |