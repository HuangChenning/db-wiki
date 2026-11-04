---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MINING_ALGORITHMS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.272 ALL\_MINING\_ALGORITHMS

`ALL_MINING_ALGORITHMS` describes the settings for a current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ALGORITHM_NAME` | `VARCHAR2(128)` |  | Algorithm used by the model. |
| `MINING_FUNCTION` | `VARCHAR2(30)` |  | Function of the machine learning model. The machine learning function is specified when the model is built:  - `CLASSIFICATION` - `REGRESSION` - `CLUSTERING` - `FEATURE_EXTRACTION` - `ASSOCIATION_RULES` - `ATTRIBUTE_IMPORTANCE` - `ANOMALY DETECTION` |
| `ALGORITHM_TYPE` | `VARCHAR2(20)` |  | Algorithm type of the model |
| `ALGORITHM_METADATA` | `CLOB` |  | Metadata of the algorithm |
| `DESCRIPTION` | `VARCHAR2(4000)` |  | Description of the algorithm |