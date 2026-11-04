---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DM_USER_MODELS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.185 DM\_USER\_MODELS

`DM_USER_MODELS` displays information about the models in the user's schema.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the model |
| `FUNCTION_NAME` | `VARCHAR2(30)` |  | Model function:  - `association` - Association is a descriptive mining function. An association model identifies relationships and the probability of their occurrence within a data set. - `attribute_importance` - Attribute Importance is a predictive mining function. An attribute importance model identifies the relative importance of an attribute in predicting a given outcome. - `classification` - Classification is a predictive mining function. A classification model uses historical data to predict new discrete or categorical data. 	The `classification` function can also be used for anomaly detection. In this case, the SVM algorithm with a null target is used (One-Class SVM). - `clustering` - Clustering is a descriptive mining function. A clustering model identifies natural groupings within a data set. - `feature_extraction` - Feature Extraction is a descriptive mining function. A feature extraction model creates an optimized data set on which to base a model. - `regression` - Regression is a predictive mining function. A regression model uses historical data to predict new continuous, numeric data. |
| `ALGORITHM_NAME` | `VARCHAR2(30)` |  | Algorithm used by the model:  - `algo_name` - Setting that specifies the algorithm used by the model. - `asso_max_rule_length` - Setting that specifies the maximum length of a rule used by an association model. - `asso_min_confidence` - Setting that specifies the minimum confidence for an association model. - `asso_min_support` - Setting that specifies the minimum support for an association model. - `clas_cost_table_name` - Setting that specifies the name of the cost matrix table for a classification model. - `clas_priors_table_name` - Setting that specifies the name of the prior probability table for NB and ABN models. Decision Tree is the only classification algorithm that does not use priors. 	For SVM classification models, this setting specifies the name of a table of weights. - `clus_num_clusters` - Setting that specifies the number of clusters for a clustering model. - `feat_num_features` - Setting that specifies the number of features for a feature selection model. |
| `CREATION_DATE` | `DATE` | `NOT NULL` | Date on which the model was created |
| `BUILD_DURATION` | `NUMBER` |  | Duration of the model build process |
| `TARGET_ATTRIBUTE` | `VARCHAR2(128)` |  | Attribute designated as the target of a classification model |
| `MODEL_SIZE` | `NUMBER` |  | Size of the model (in megabytes) |