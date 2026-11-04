---
title: DBMS_DATA_MINING
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_datmin.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 44 DBMS\_DATA\_MINING

Oracle Data Mining is an analytical technology that derives actionable information from data in an Oracle Database. You can use Oracle Data Mining to evaluate the probability of future events and discover unsuspected associations and groupings within your data.

The `DBMS_DATA_MINING` package is the programmatic interface for creating and managing data mining models (mining model schema objects). Oracle Data Mining also supports a family of SQL functions for deploying data mining models.

Oracle Data Miner, a graphical interface to Oracle Data Mining, is available for download from the Oracle Technology Network at: `http://www.oracle.com/technetwork/database/options/odm/`

See Also:

- [Chapter 45, "DBMS\_DATA\_MINING\_TRANSFORM"](d_dmtran.md). This package supports data pre-processing for data mining models.
- [Chapter 104, "DBMS\_PREDICTIVE\_ANALYTICS"](d_predan.md). This package supports several routines that perform automated data mining.
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions002.htm#SQLRF20030) for information about the SQL Data Mining scoring functions.
- [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/intro_concepts.htm#DMCON001) for an introduction to Oracle Data Mining.
- [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/whatsnew.htm#DMCON000) for new features in Oracle Data Mining.

This chapter contains the following topics:

- Using DBMS\_DATA\_MINING
	- Overview
		- Mining Model Objects
		- Security Model
		- Deprecated Subprograms
		- Mining Functions
		- Model Settings
		- Data Types
- Summary of DBMS\_DATA\_MINING Subprograms

---

## Using DBMS\_DATA\_MINING

This section contains topics that relate to using the `DBMS_DATA_MINING` package.

---

### Overview

Oracle Data Mining supports both supervised and unsupervised data mining. Supervised data mining predicts a target value based on historical data. Unsupervised data mining discovers natural groupings and does not use a target.

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/intro_concepts.htm#DMCON030) for more information

A data mining function refers to the methods for solving a given class of data mining problems. The mining function must be specified when a model is created. See "Mining Functions".

Note on Terminology:

In data mining terminology, a function is a general type of problem to be solved by a given approach to data mining. In SQL language terminology, a function is an operator that returns a value.

In Oracle Data Mining documentation, the term function, or mining function refers to a data mining function; the term SQL function or SQL Data Mining function refers to a SQL function for scoring (deploying) data mining models. The SQL Data Mining functions are documented in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions002.htm#SQLRF20030).

Supervised data mining functions include:

- Classification
- Regression
- Attribute Importance

Unsupervised data mining functions include:

- Clustering
- Association
- Feature Extraction
- Anomaly Detection (one-class classification)

The steps you use to build and apply a mining model depend on the data mining function and the algorithm being used. The algorithms supported by Oracle Data Mining are listed in Table 44-1.

Table 44-1 Oracle Data Mining Algorithms

| Algorithm | Abbreviation | Function |
| --- | --- | --- |
| Adaptive Bayes Network (deprecated) | ABN | Classification |
| Apriori | AP | Association |
| Decision Tree | DT | Classification |
| Generalized Linear Model | GLM | Classification and Regression |
| k-Means (default clustering algorithm) | KM | Clustering |
| Minimal Descriptor Length | MDL | Attribute Importance |
| Naive Bayes (default classification algorithm) | NB | Classification |
| Non-Negative Matrix Factorization | NMF | Feature Extraction |
| Orthogonal Partitioning Clustering | O-Cluster | Clustering |
| Support Vector Machine (default regression algorithm) | SVM | Classification and regression (and anomaly detection through one-class classification) |

---

### Mining Model Objects

Mining models are Oracle Database schema objects. They support the standard security features of Oracle Database. Mining models are also supported by SQL `COMMENT` and SQL `AUDIT`.

See Also:

- [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/schemaobjs.htm#DMADM003) for information about mining model objects, SQL `COMMENT`, and SQL `AUDIT`
- [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/security.htm#DMADM004) for information about mining model security
- [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009) for information about the sample Data Mining programs

#### ALL\_MINING\_MODELS

You can query the data dictionary view `ALL_MINING_MODELS` to obtain a list of accessible mining models.

Example 44-1 ALL\_MINING\_MODELS

```
SQL> describe all_mining_models
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 OWNER                                     NOT NULL VARCHAR2(30)
 MODEL_NAME                                NOT NULL VARCHAR2(30)
 MINING_FUNCTION                                    VARCHAR2(30)
 ALGORITHM                                          VARCHAR2(30)
 CREATION_DATE                             NOT NULL DATE
 BUILD_DURATION                                     NUMBER
 MODEL_SIZE                                         NUMBER
 COMMENTS                                           VARCHAR2(4000)
```

#### Mining Model Naming Restrictions

The naming rules for models are more restrictive than the naming rules for most database schema objects. A model name must satisfy the following additional requirements:

- It must be 25 or fewer characters long.
- It must be a nonquoted identifier. Oracle requires that nonquoted identifiers contain only alphanumeric characters, the underscore (\_), dollar sign ($), and pound sign (#); the initial character must be alphabetic. Oracle strongly discourages the use of the dollar sign and pound sign in nonquoted literals.

Naming requirements for schema objects are fully documented in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements008.htm#SQLRF00223).

#### ALL\_MINING\_MODEL\_ATTRIBUTES

You can query the data dictionary view `ALL_MINING_MODEL_ATTRIBUTES` to obtain a list of the data attributes for each accessible mining model. Data attributes are the columns of data used by an algorithm to build a model. Some or all of these columns must be present in the data to which the model is applied.

Data attributes are referred to as the model signature. The `ALL_MINING_MODEL_ATTRIBUTES` view lists the data attributes in the model signature, including the target if the model is supervised.

An algorithm builds an internal representation of the data attributes and uses them as either categoricals (data that classifies or categorizes) or as numericals (continuous data). These internal model attributes can be viewed using the `GET_MODEL_DETAILS` functions.

Example 44-2 ALL\_MINING\_MODEL\_ATTRIBUTES

```
SQL> describe all_mining_model_attributes
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 OWNER                                     NOT NULL VARCHAR2(30)
 MODEL_NAME                                NOT NULL VARCHAR2(30)
 ATTRIBUTE_NAME                            NOT NULL VARCHAR2(30)
 ATTRIBUTE_TYPE                                     VARCHAR2(11)
 DATA_TYPE                                          VARCHAR2(12)
 DATA_LENGTH                                        NUMBER
 DATA_PRECISION                                     NUMBER
 DATA_SCALE                                         NUMBER
 USAGE_TYPE                                         VARCHAR2(8)
 TARGET                                             VARCHAR2(3)
```

See Also:

[Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/xform_casetbl.htm#DMPRG010) for more information about attributes and `ALL_MINING_MODEL_ATTRIBUTES`

#### ALL\_MINING\_MODEL\_SETTINGS

The view `ALL_MINING_MODEL_SETTINGS` returns the settings for each accessible mining model. Settings control various characteristics of mining models.

All settings have default values. The values of some settings are generated by the algorithm by default. You can override the default value of a setting by specifying its value in a settings table for the model. All settings, both default and user-specified, are listed in `ALL_MINING_MODEL_SETTINGS`.

Example 44-3 ALL\_MINING\_MODEL\_SETTINGS

```
SQL> describe all_mining_model_settings
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 OWNER                                     NOT NULL VARCHAR2(30)
 MODEL_NAME                                NOT NULL VARCHAR2(30)
 SETTING_NAME                              NOT NULL VARCHAR2(30)
 SETTING_VALUE                                      VARCHAR2(4000)
 SETTING_TYPE                                       VARCHAR2(7)
```

See Also:

- Model Settings
- [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for more information about `ALL_MINING_MODEL_SETTINGS`

---

### Security Model

The `DBMS_DATA_MINING` package is owned by user `SYS` and is installed as part of database installation. Execution privilege on the package is granted to public. The routines in the package are run with invokers' rights (run with the privileges of the current user).

The `DBMS_DATA_MINING` package exposes APIs that are leveraged by the Oracle Data Mining option. Users who wish to create mining models in their own schema require the `CREATE MINING MODEL` system privilege (as well as the `CREATE TABLE` and `CREATE VIEW` system privilege). Users who wish to create mining models in other schemas require the `CREATE ANY MINING MODEL` system privilege (as well as the corresponding table and view creation privileges).

Users have full control over managing models that exist within their own schema. Additional system privileges necessary for managing data mining models in other schemas include `ALTER ANY MINING MODEL`, `DROP ANY MINING MODEL`, `SELECT ANY MINING MODEL`, `COMMENT ANY MINING MODEL`, and `AUDIT ANY`.

Individual object privileges on mining models, `ALTER MINING MODEL` and `SELET MINING MODEL`, can be used to selectively grant privileges on a model to a different user.

See Also:

[Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/security.htm#DMADM004) for more information about the security features of Oracle Data Mining

---

### Deprecated Subprograms

The following subprograms were deprecated in Oracle Data Mining 11g Release 1 (11.1).

- `GET_DEFAULT_SETTINGS`
	Replaced with data dictionary views: `USER` / `ALL` / `DBA_MINING_MODEL_SETTINGS`
- `GET_MODEL_SETTINGS`
	Replaced with data dictionary views: `USER` / `ALL` / `DBA_MINING_MODEL_SETTINGS`
- `GET_MODEL_SIGNATURE`
	Replaced with data dictionary views: `USER` / `ALL` / `DBA_MINING_MODEL_ATTRIBUTES`

The following view was deprecated in Oracle Data Mining 11g Release 1 (11.1).

- `DM_USER_MODELS`
	Replaced with data dictionary views: `USER` / `ALL` / `DBA_MINING_MODELS`

The Adaptive Bayes Network algorithm was deprecated in Oracle Data Mining 11g Release 1 (11.1).

Note:

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

Since 11g Release 1 (11.1), the `DMSYS` schema is no longer present in the database. Oracle Data Mining metadata now resides in `SYS`.

---

### Mining Functions

The constants that specify the mining function of a model are listed in Table 44-2. The concept of a "mining function" is introduced in "Overview".

All models are created with a mining function. The mining function is a required argument to the CREATE\_MODEL Procedure.

Table 44-2 Mining Functions

| Value | Description |
| --- | --- |
| `ASSOCIATION` | Association is a descriptive mining function. An association model identifies relationships and the probability of their occurrence within a data set.  Association models use the Apriori algorithm. |
| `ATTRIBUTE_IMPORTANCE` | Attribute Importance is a predictive mining function. An attribute importance model identifies the relative importance of an attribute in predicting a given outcome.  Attribute Importance models use the Minimal Descriptor Length algorithm. |
| `CLASSIFICATION` | Classification is a predictive mining function. A classification model uses historical data to predict a categorical target.  Classification models can use: Naive Bayes, Adaptive Bayes Network (deprecated), Decision Tree, Logistic Regression, or Support Vector Machine algorithms. The default is Naive Bayes.  The classification function can also be used for anomaly detection. In this case, the SVM algorithm with a null target is used (One-Class SVM). |
| `CLUSTERING` | Clustering is a descriptive mining function. A clustering model identifies natural groupings within a data set.  Clustering models can use: k-Means or O-Cluster algorithms. The default is k-Means. |
| `FEATURE_EXTRACTION` | Feature Extraction is a descriptive mining function. A feature extraction model creates an optimized data set on which to base a model.  Feature extraction models use the Non-Negative Matrix Factorization algorithm. |
| `REGRESSION` | Regression is a predictive mining function. A regression model uses historical data to predict a numerical target.  Regression models can use Support Vector Machine or Linear Regression. The default is Support Vector Machine. |

---

### Model Settings

Oracle Data Mining uses settings to specify the algorithm and other characteristics of a model. Some settings are general, some are specific to a mining function, and some are specific to an algorithm.

All settings have default values. If you want to override one or more of the settings for a model, you must create a settings table. The settings table must have the column names and data types shown in Table 44-3.

Table 44-3 Required Columns in the Model Settings Table

| Column Name | Data Type |
| --- | --- |
| `SETTING_NAME` | `VARCHAR2(30)` |
| `SETTING_VALUE` | `VARCHAR2(4000)` |

The information you provide in the settings table is used by the model at build time. The name of the settings table is an optional argument to the CREATE\_MODEL Procedure.

You can find the settings used by a model by querying the data dictionary view `ALL_MINING_MODEL_SETTINGS`. This view lists the model settings used by the mining models to which you have access. All the setting values are included in the view, whether default or user-specified. See "ALL\_MINING\_MODEL\_SETTINGS".

#### Algorithm Names

The `ALGO_NAME` setting specifies the model algorithm. The values for the `ALGO_NAME` setting are listed in Table 44-4.

Table 44-4 Algorithm Names

| ALGO\_NAME Value | Description | Mining Function |
| --- | --- | --- |
| `ALGO_ADAPTIVE_BAYES_NETWORK` | Adaptive Bayes Network (deprecated) | Classification |
| `ALGO_DECISION_TREE` | Decision Tree | Classification |
| `ALGO_NAIVE_BAYES` | Naive Bayes | Classification |
| `ALGO_GENERALIZED_LINEAR_MODEL` | Generalized Linear Model | Classification and Regression |
| `ALGO_SUPPORT_VECTOR_MACHINES` | Support Vector Machine | Classification and Regression |
| `ALGO_KMEANS` | Enhanced k\_Means | Clustering |
| `ALGO_O_CLUSTER` | O-Cluster | Clustering |
| `ALGO_AI_MDL` | Minimum Description Length | Attribute Importance |
| `ALGO_APRIORI_ASSOCIATION_RULES` | Apriori | Association Rules |
| `ALGO_NONNEGATIVE_MATRIX_FACTOR` | Non-Negative Matrix Factorization | Feature Extraction |

Oracle Data Mining supports more than one algorithm for the classification, regression, and clustering mining functions. Each of these mining functions has a default algorithm, as shown in Table 44-5.

Table 44-5 Default Algorithms

| Mining Function | Default Algorithm |
| --- | --- |
| Classification | Naive Bayes |
| Regression | Support Vector Machine |
| Clustering | k-Means |

#### Automatic Data Preparation

The `PREP_AUTO` setting indicates whether or not the model will use Automatic Data Preparation (ADP). By default ADP is disabled.

When you enable ADP, the model uses heuristics to transform the build data according to the requirements of the algorithm. The transformation instructions are stored with the model and reused whenever the model is applied. You can view the transformation instructions in the model details.

You can choose to supplement automatic data preparations by specifying additional transformations in the `xform_list` parameter when you build the model. (See "CREATE\_MODEL Procedure".)

If you do not use ADP (default) and do not specify transformations in the `xform_list` parameter to `CREATE_MODEL` (also the default), you will continue to operate in 10.2 mode. This means that you must implement your own transformations separately in the build, test, and scoring data; you must take special care to implement the exact same transformations in each data set.

If you do not use ADP, but you do specify transformations in the `xform_list` parameter to `CREATE_MODEL`, Oracle Data Mining embeds the transformation definitions in the model and prepares the test and scoring data to match the build data. Because of automatic and embedded data preparation, mining models are known as supermodels.

The values for the `PREP_AUTO` setting are described in Table 44-6.

Table 44-6 PREP\_AUTO Setting

| PREP\_AUTO Value | Description |
| --- | --- |
| `PREP_AUTO_OFF` | Disable Automatic Data Preparation (default). |
| `PREP_AUTO_ON` | Enable Automatic Data Preparation. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/xform_data.htm#DMCON003) for information about data preparation

#### Mining Function Settings

The settings described in Table 44-7 apply to a mining function.

Table 44-7 Mining Function Settings

| Mining Function | Setting Name | Setting Value | Description |
| --- | --- | --- | --- |
| Association | `ASSO_MAX_RULE_LENGTH` | `TO_CHAR( 2<=` `numeric_expr` `<=20)` | Maximum rule length for association rules.  Default is 4. |
| Association | `ASSO_MIN_CONFIDENCE` | `TO_CHAR( 0<=` `numeric_expr` `<=1)` | Minimum confidence for association rules.  Default is 0.1. |
| Association | `ASSO_MIN_SUPPORT` | `TO_CHAR( 0<=` `numeric_expr` `<=1)` | Minimum support for association rules.  Default is 0.1. |
| Classification | `CLAS_COST_TABLE_NAME` | table\_name | (Decision Tree only) Name of a table that stores a cost matrix to be used by the algorithm in building the model. The cost matrix specifies the costs associated with misclassifications.  Only Decision Tree models can use a cost matrix at build time. All classification algorithms can use a cost matrix at apply time.  The cost matrix table is user-created. See "ADD\_COST\_MATRIX Procedure" for the column requirements.  See [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON050) for information about costs. |
| Classification | `CLAS_PRIORS_TABLE_NAME` | table\_name | (Naive Bayes) Name of a table that stores prior probabilities to offset differences in distribution between the build data and the scoring data.  The priors table is user-created. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG020) for the column requirements. See [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON033) for additional information about priors. |
| Classification | `CLAS_WEIGHTS_TABLE_NAME` | table\_name | (GLM and SVM only) Name of a table that stores weighting information for individual target values in SVM classification and GLM logistic regression models. The weights are used by the algorithm to bias the model in favor of higher weighted classes.  The class weights table is user-created. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG021) for the column requirements. See [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_glm.htm#DMCON020) for additional information about class weights. |
| Clustering | `CLUS_NUM_CLUSTERS` | `TO_CHAR( numeric_expr` `>=1)` | Maximum number of leaf clusters generated by a clustering algorithm. (Oracle Data Mining clustering algorithms are hierarchical, as described in [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/clustering.htm#DMCON247).)  Enhanced k-Means usually produces the exact number of clusters specified by `CLUS_NUM_CLUSTERS`, unless there are fewer distinct data points.  O-Cluster may produce fewer clusters than the number specified by `CLUS_NUM_CLUSTERS`, depending on the data.  Default is 10. |
| Feature Extraction | `FEAT_NUM_FEATURES` | `TO_CHAR(``numeric_expr` `>=1)` | Number of features to be extracted by a feature extraction model.  The default is estimated from the data by the algorithm. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/part2.htm#DMCON042) for information about mining functions

#### Global Settings

The settings in Table 44-8 are applicable to any type of model, but are currently only implemented for specific algorithms.

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-8 Global Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `ODMS_ITEM_ID_COLUMN_NAME` | column\_name | (Association Rules only) Name of a column that contains the items in a transaction. When this setting is specified, the algorithm expects the data to be presented in native transactional format, consisting of two columns:  - Case ID, either categorical or numerical - Item ID, either categorical or numerical, specified by `ODMS_ITEM_ID_COLUMN_NAME`  A typical example of transactional data is market basket data, wherein a case represents a basket that may contain many items. Each item is stored in a separate row, and many rows may be needed to represent a case. The case ID values do not uniquely identify each row. Transactional data is also called multi-record case data.  Association Rules is normally used with transactional data, but it can also be applied to single-record case data (similar to other algorithms).  For more information about single-record and multi-record case data, see [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/xform_casetbl.htm#DMPRG006). |
| `ODMS_ITEM_VALUE_COLUMN_NAME` | column\_name | (Association Rules only) Name of a column that contains a value associated with each item in a transaction. This setting is only used when a value has been specified for `ODMS_ITEM_ID_COLUMN_NAME` indicating that the data is presented in native transactional format.  When `ODMS_ITEM_VALUE_COLUMN_NAME` is specified, the algorithm expects the build data to consist of three columns:  - Case ID, either categorical or numerical - Item ID, either categorical or numerical, specified by `ODMS_ITEM_ID_COLUMN_NAME` - Item value, either categorical or numerical, specified by `ODMS_ITEM_VALUE_COLUMN_NAME`  The item value column may specify information such as the number of items (for example, three apples) or the type of the item (for example, macintosh apples). |
| `ODMS_MISSING_VALUE_TREATMENT` | `ODMS_MISSING_VALUE_MEAN_MODE`  `ODMS_MISSING_VALUE_DELETE_ROW` | (GLM only) How to treat missing values in the training data. This setting does not affect the scoring data.  Oracle Data Mining replaces missing values with the mean (numeric attributes) or the mode (categorical attributes) both at build time and apply time. You can set `ODMS_MISSING_VALUE_TREATMENT` to `ODMS_MISSING_VALUE_DELETE_ROW` to override this behavior in the training data. When `ODMS_MISSING_VALUE_TREATMENT` is set to `ODMS_MISSING_VALUE_DELETE_ROW`, the rows in the training data that contain missing values are deleted. However, if you want to replicate this missing value treatment in the scoring data, you must perform the transformation explicitly. For instructions, see [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_glm.htm#DMCON062).  The value `ODMS_MISSING_VALUE_DELETE_ROW` is only valid for tables without nested columns. If this value is used with nested data, an exception is raised. |
| `ODMS_ROW_WEIGHT_COLUMN_NAME` | column\_name | (GLM only) Name of a column in the training data that contains a weighting factor for the rows.  Row weights can be used as a compact representation of repeated rows, as in the design of experiments where a specific configuration is repeated several times. Row weights can also be used to emphasize certain rows during model construction. For example, to bias the model towards rows that are more recent and away from potentially obsolete data. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_glm.htm#DMCON022) for information about GLM

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/market_basket.htm#DMCON009) for information about Association Rules

#### Algorithm Settings: Adaptive Bayes Network (deprecated)

These settings affect the behavior of the Adaptive Bayes Network algorithm.

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-9 ABN Settings

| Setting | Value | Description |
| --- | --- | --- |
| `ABNS_MAX_BUILD_MINUTES` | `TO_CHAR(` `numeric_expr` `>=0)` | Maximum time to complete an ABN model build.  Default is 0, which implies no time limit. |
| `ABNS_MAX_NB_PREDICTORS` | `TO_CHAR(` `numeric_expr` `>0)` | Maximum number of predictors, measured by their MDL ranking, to be considered for building an ABN model of type `abns_naive_bayes`.  Default is 10. |
| `ABNS_MAX_PREDICTORS` | `TO_CHAR(``numeric_expr` `>0)` | Maximum number of predictors, measured by their MDL ranking, to be considered for building an ABN model of type `abns_single_feature` or `abns_multi_feature`.  Default is 25. |
| `ABNS_MODEL_TYPE` | `ABNS_MULTI_FEATURE`  `ABNS_NAIVE_BAYES`  `ABNS_SINGLE_FEATURE` | Type of ABN model.  The default is `multi_feature`. |

#### Algorithm Settings: Decision Tree

These settings affect the behavior of the Decision Tree algorithm.

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-10 Decision Tree Settings

| Setting | Value | Description |
| --- | --- | --- |
| `TREE_IMPURITY_METRIC` | `TREE_IMPURITY_ENTROPY`  `TREE_IMPURITY_GINI` | Tree impurity metric for Decision Tree.  Tree algorithms seek the best test question for splitting data at each node. The best splitter and split value are those that result in the largest increase in target value homogeneity (purity) for the entities in the node. Purity is measured in accordance with a metric. Decision trees can use either gini (`TREE_IMPURITY_GINI`) or entropy (`TREE_IMPURITY_ENTROPY`) as the purity metric. By default, the algorithm uses gini. |
| `TREE_TERM_MAX_DEPTH` | `TO_CHAR( 2<=` `numeric_expr` `<=20)` | Criteria for splits: maximum tree depth (the maximum number of nodes between the root and any leaf node, including the leaf node).  Default is 7. |
| `TREE_TERM_MINPCT_MODE` | `TO_CHAR( 0<=` `numeric_expr` `<=10)` | No child shall have fewer records than this number, which is expressed as a percentage of the training rows.  Default is 0.05, indicating 0.05%. |
| `TREE_TERM_MINPCT_SPLIT` | `TO_CHAR( 0 <=` `numeric_expr` `<=20)` | Criteria for splits: minimum number of records in a parent node expressed as a percent of the total number of records used to train the model. No split is attempted if number of records is below this value.  Default is 0.1, indicating 0.1%. |
| `TREE_TERM_MINREC_NODE` | `TO_CHAR(``numeric_expr` `>=0)` | No child shall have fewer records than this number.  Default is 10. |
| `TREE_TERM_MINREC_SPLIT` | `TO_CHAR( numeric_expr` `>=0)` | Criteria for splits: minimum number of records in a parent node expressed as a value. No split is attempted if number of records is below this value.  Default is 20. |

#### Algorithm Settings: Generalized Linear Models

These settings affect the behavior of GLM models. GLM can be used for classification (logistic regression) or regression (linear regression).

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-11 GLM Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `GLMS_CONF_LEVEL` | `TO_CHAR(0<` `numeric_expr` `<1)` | The confidence level for coefficient confidence intervals.  The default confidence level is 0.95. |
| `GLMS_DIAGNOSTICS_TABLE_NAME` | table\_name | The name of a table to contain row-level diagnostic information for a GLM model. The table is created during model build.  If you want to create a diagnostics table, you must specify a case ID when you build the model. (See the CREATE\_MODEL Procedure.) If you specify a diagnostics table but do not provide a case ID, an exception is raised.  For information on GLM diagnostics, see Oracle Data Mining Concepts. |
| `GLMS_REFERENCE_CLASS_NAME` | target\_value | The target value to be used as the reference value in a logistic regression model. Probabilities will be produced for the other (non-reference) class.  By default, the algorithm chooses the value with the highest prevalence (the most cases) for the reference class. |
| `GLMS_RIDGE_REGRESSION` | `GLMS_RIDGE_REG_ENABLE`  `GLMS_RIDGE_REG_DISABLE` | Whether or not ridge regression will be enabled.  By default, the algorithm determines whether or not to use ridge. You can explicitly enable ridge by setting `GLMS_RIDGE_REGRESSION` to `GLMS_RIDGE_REG_ENABLE`.  Ridge applies to both regression and classification mining functions.  When ridge is enabled, no prediction bounds are produced by the `PREDICTION_BOUNDS` SQL operator. |
| `GLMS_RIDGE_VALUE` | `TO_CHAR(0<` `numeric_expr)` | The value for the ridge parameter used by the algorithm. This setting is only used when you explicitly enable ridge regression by setting `GLMS_RIDGE_REGRESSION` to `GLMS_RIDGE_REG_ENABLE`.  If ridge regression is enabled internally by the algorithm, the ridge parameter is determined by the algorithm. |
| `GLMS_VIF_FOR_RIDGE` | `GLMS_VIF_RIDGE_ENABLE`  `GLMS_VIF_RIDGE_DISABLE` | (Linear regression only) Whether or not to produce Variance Inflation Factor (VIF) statistics when ridge is being used.  By default, VIF is not produced when ridge is enabled.  When you explicitly enable ridge regression by setting `GLMS_RIDGE_REGRESSION` to `GLMS_RIDGE_REG_ENABLE`, you can request VIF statistics by setting `GLMS_VIF_FOR_RIDGE` to `GLMS_VIF_RIDGE_ENABLE`; the algorithm will produce VIF if enough system resources are available. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_glm.htm#DMCON022) for information about GLM

#### Algorithm Settings: k-Means

These settings affect the behavior of the k-Means algorithm.

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-12 k-Means Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `KMNS_BLOCK_GROWTH` | `TO_CHAR(1<` `numeric_expr` `<=5)` | Growth factor for memory allocated to hold cluster data  Default value is 2 |
| `KMNS_CONV_TOLERANCE` | `TO_CHAR(0<` `numeric_expr` `<=0.5)` | Convergence tolerance for k-Means algorithm  Default is 0.01 |
| `KMNS_DISTANCE` | `KMNS_COSINE`  `KMNS_EUCLIDEAN`  `KMNS_FAST_COSINE` | Distance Function for k-Means Clustering. The default is euclidean. |
| `KMNS_ITERATIONS` | `TO_CHAR(0<` `numeric_expr` `<=20)` | Number of iterations for k-Means algorithm  Default is 3 |
| `KMNS_MIN_PCT_ATTR_SUPPORT` | `TO_CHAR(0<=` `numeric_expr` `<=1)` | The fraction of attribute values that must be non-null in order for the attribute to be included in the rule description for the cluster.  Setting the parameter value too high in data with missing values can result in very short or even empty rules.  Default is 0.1. |
| `KMNS_NUM_BINS` | `TO_CHAR(``numeric_expr` `>0)` | Number of histogram bins. Specifies the number of bins in the attribute histogram produced by k-Means. The bin boundaries for each attribute are computed globally on the entire training data set. The binning method is equi-width. All attributes have the same number of bins with the exception of attributes with a single value that have only one bin.  Default is 10. |
| `KMNS_SPLIT_CRITERION` | `KMNS_SIZE`  `KMNS_VARIANCE` | Split criterion for k-Means Clustering. The default criterion is the variance. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_kmeans.htm#DMCON057) for information about k-Means.

#### Algorithm Settings: Naive Bayes

These settings affect the behavior of the Naive Bayes Algorithm.

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-13 Naive Bayes Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `NABS_PAIRWISE_THRESHOLD` | `TO_CHAR(0<=` `numeric_expr` `<=1)` | Value of pairwise threshold for NB algorithm  Default is 0.01. |
| `NABS_SINGLETON_THRESHOLD` | `TO_CHAR(0<=` `numeric_expr` `<=1)` | Value of singleton threshold for NB algorithm  Default value is 0.01 |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_nb.htm#DMCON018) for information about Naive Bayes

#### Algorithm Settings: Non-Negative Matrix Factorization

These settings affect the behavior of the Non-Negative Matrix Factorization algorithm.

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-14 NMF Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `NMFS_CONV_TOLERANCE` | `TO_CHAR(0<` `numeric_expr` `<=0.5)` | Convergence tolerance for NMF algorithm  Default is 0.05 |
| `NMFS_NONNEGATIVE_SCORING` | `NMFS_NONNEG_SCORING_ENABLE`  `NMFS_NONNEG_SCORING_DISABLE` | Whether negative numbers should be allowed in scoring results. When set to `NMFS_NONNEG_SCORING_ENABLE`, negative feature values will be replaced with zeros. When set to `NMFS_NONNEG_SCORING_DISABLE`, negative feature values will be allowed.  Default is `NMFS_NONNEG_SCORING_ENABLE` |
| `NMFS_NUM_ITERATIONS` | `TO_CHAR(1 <=` `numeric_expr` `<=500)` | Number of iterations for NMF algorithm  Default is 50 |
| `NMFS_RANDOM_SEED` | `TO_CHAR(``numeric_expr)` | Random seed for NMF algorithm.  Default is –1. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_nmf.htm#DMCON058) for information about NMF

#### Algorithm Settings: O-Cluster

These settings affect the behavior of the O-Cluster algorithm.

You can query the data dictionary view `*_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_ALL_MINING_MODEL_SETTINGS`.

Table 44-15 O-CLuster Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `OCLT_MAX_BUFFER` | `TO_CHAR(``numeric_expr` `>0)` | Buffer size for O-Cluster.  Default is 50,000. |
| `OCLT_SENSITIVITY` | `TO_CHAR(0 <=` `numeric_expr` `<=1)` | A fraction that specifies the peak density required for separating a new cluster. The fraction is related to the global uniform density.  Default is 0.5. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_oc.htm#DMCON059) for information about O-Cluster

#### Algorithm Settings: Support Vector Machine

These settings affect the behavior of the Support Vector Machine algorithm. SVM can be used for classification or regression, or for anomaly detection (classification with a null target).

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016) for information about \* `_MINING_MODEL_SETTINGS`.

Table 44-16 SVM Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `SVMS_ACTIVE_LEARNING` | `SVMS_AL_DISABLE`  `SVMS_AL_ENABLE` | Whether active learning is enabled or disabled. By default, active learning is enabled.  When active learning is enabled, the SVM algorithm uses active learning to build a reduced size model. When active learning is disabled, the SVM algorithm builds a standard model. |
| `SVMS_COMPLEXITY_FACTOR` | `TO_CHAR(``numeric_expr` `>0``)` | Value of complexity factor for SVM algorithm (both classification and regression).  Default value estimated from the data by the algorithm. |
| `SVMS_CONV_TOLERANCE` | `TO_CHAR(``numeric_expr` `>0)` | Convergence tolerance for SVM algorithm.  Default is 0.001. |
| `SVMS_EPSILON` | `TO_CHAR(``numeric_expr` `>0)` | Value of epsilon factor for SVM regression.  Default value estimated from the data by the algorithm. |
| `SVMS_KERNEL_CACHE_SIZE` | `TO_CHAR(``numeric_expr` `>0)` | Value of kernel cache size for SVM algorithm. Applies to Gaussian kernel only.  Default is 50000000 bytes. |
| `SVMS_KERNEL_FUNCTION` | `svm_gaussian`  `svms_linear` | Kernel for Support Vector Machine. The default is determined by the algorithm based on the number of attributes in the training data. When there are many attributes, the algorithm uses a linear kernel, otherwise it uses a nonlinear (Gaussian) kernel.  The number of attributes does not correspond to the number of columns in the training data. The algorithm explodes categorical attributes to binary, numeric attributes. In addition, Oracle Data Mining handles each row in a nested column as a separate attribute. SVM takes these factors into account when choosing the kernel function. |
| `SVMS_OUTLIER_RATE` | `TO_CHAR(``0< numeric_expr` `<1)` | The desired rate of outliers in the training data. Valid for One-Class SVM models only (anomaly detection).  Default is.1. |
| `SVMS_STD_DEV` | `TO_CHAR(``numeric_expr` `>0)` | Value of standard deviation for SVM algorithm.  This is applicable only for Gaussian kernel.  Default value estimated from the data by the algorithm. |

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_svm.htm#DMCON025) for information about SVM

---

### Data Types

The `DBMS_DATA_MINING` package uses object data types to store information about model attributes. Most of these types are returned by the table functions `GET` \_ `n`, where `n` identifies the type of information to return. These functions take a model name as input and return the requested information as a collection of rows.

For a list of the `GET` functions, see "Summary of DBMS\_DATA\_MINING Subprograms".

Oracle Data Mining also uses object data types for handling transactional data. These types, `DM_NESTED_NUMERICALS` and `DM_NESTED_CATEGORICALS` specify nested tables that can be used for storing a set of mining attributes in a single column. For more information on nested tables, see the [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/xform_casetbl.htm#DMPRG006).

All the table functions use pipelining, which causes each row of output to be materialized as it is read from model storage, without waiting for the generation of the complete table object. For more information on pipelined, parallel table functions, consult the [Oracle Database PL/SQL Language Reference.](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/tuning.htm#LNPLS01210)

The Data Mining object data types are described in Table 44-17.

Table 44-17 DBMS\_DATA\_MINING Summary of Data Types

| Data Type | Description |
| --- | --- |
| `DM_ABN_DETAIL` | Information about an attribute in an Adaptive Bayes Network model. |
| `DM_ABN_DETAILS` | A collection of `DM_ABN_DETAIL`. Returned by GET\_MODEL\_DETAILS\_ABN Function. |
| `DM_CENTROID` | The centroid of a cluster. |
| `DM_CENTROIDS` | A collection of `DM_CENTROID`. A member of `DM_CLUSTER`. |
| `DM_CHILD` | A child node of a cluster. |
| `DM_CHILDREN` | A collection of `DM_CHILD`. A member of `DM_CLUSTER`. |
| `DM_CLUSTER` | A cluster. A cluster includes `DM_PREDICATES`, `DM_CHILDREN`, `DM_CENTROIDS`, and `DM_HISTOGRAMS`. It also includes a `DM_RULE`. |
| `DM_CLUSTERS` | A collection of `DM_CLUSTER`. Returned by GET\_MODEL\_DETAILS\_KM Function and GET\_MODEL\_DETAILS\_OC Function. |
| `DM_CONDITIONAL` | The conditional probability of an attribute in a Naive Bayes model. |
| `DM_CONDITIONALS` | A collection of `DM_CONDITIONAL`. Returned by GET\_MODEL\_DETAILS\_NB Function. |
| `DM_COST_ELEMENT` | The actual and predicted values in a cost matrix. |
| `DM_COST_MATRIX` | A collection of `DM_COST_ELEMENT`. Returned by GET\_MODEL\_COST\_MATRIX Function. |
| `DM_GLM_COEFF` | The coefficient and associated statistics of an attribute in a Generalized Linear Model. |
| `DM_GLM_COEFF_SET` | A collection of `DM_GLM_COEFF`. Returned by GET\_MODEL\_DETAILS\_GLM Function. |
| `DM_HISTOGRAM_BIN` | A histogram associated with a cluster. |
| `DM_HISTOGRAMS` | A collection of `DM_HISTOGRAM_BIN`. A member of `DM_CLUSTER`. |
| `DM_ITEM` | An item in an association rule. |
| `DM_ITEMS` | A collection of `DM_ITEM`. |
| `DM_ITEMSET` | A collection of `DM_ITEMS`. |
| `DM_ITEMSETS` | A collection of `DM_ITEMSET`. Returned by GET\_FREQUENT\_ITEMSETS Function. |
| `DM_MODEL_GLOBAL_DETAIL` | High-level statistics about a model. |
| `DM_MODEL_GLOBAL_DETAILS` | A collection of `DM_MODEL_GLOBAL_DETAIL`. Returned by GET\_MODEL\_DETAILS\_GLOBAL Function. |
| `DM_MODEL_SETTING` | A model setting. |
| `DM_MODEL_SETTINGS` | A collection of `DM_MODEL_SETTING`. Returned by GET\_MODEL\_SETTINGS Function and GET\_DEFAULT\_SETTINGS Function. |
| `DM_MODEL_SIGNATURE_ATTRIBUTE` | An attribute in the model signature. |
| `DM_MODEL_SIGNATURE` | A collection of `DM_MODEL_SIGNATURE`. Returned by GET\_MODEL\_SIGNATURE Function. |
| `DM_NB_DETAIL` | Information about an attribute in a Naive Bayes model. |
| `DM_NB_DETAILS` | A collection of `DM_DB_DETAIL`. Returned by GET\_MODEL\_DETAILS\_NB Function. |
| `DM_NESTED_CATEGORICAL` | The name and value of a categorical attribute. |
| `DM_NESTED_CATEGORICALS` | A collection of `DM_NESTED_CATEGORICAL`. A collection of attributes defined as a single model attribute. Transactional data must be defined as nested attributes for Data Mining. |
| `DM_NESTED_NUMERICAL` | The name and value of a numerical attribute. |
| `DM_NESTED_NUMERICALS` | A collection of `DM_NESTED_NUMERICAL`. A collection of attributes defined as a single model attribute. Transactional data must be defined as nested attributes for Data Mining. |
| `DM_NMF_ATTRIBUTE` | An attribute in a feature of a Non-Negative Matrix Factorization model. |
| `DM_NMF_ATTRIBUTE_SET` | A collection of `DM_NMF_ATTRIBUTE`. A member of `DM_NMF_FEATURE`. |
| `DM_NMF_FEATURE` | A feature in a Non-Negative Matrix Factorization model. |
| `DM_NMF_FEATURE_SET` | A collection of `DM_NMF_FEATURE`. Returned by GET\_MODEL\_DETAILS\_NMF Function. |
| `DM_PREDICATE` | Antecedent and consequent attributes. |
| `DM_PREDICATES` | A collection of `DM_PREDICATE`. A member of `DM_RULE`, `DM_CLUSTER`, and `DM_ABN_DETAIL`. |
| `DM_RANKED_ATTRIBUTE` | An attribute ranked by its importance in an Attribute Importance model. |
| `DM_RANKED_ATTRIBUTES` | A collection of `DM_RANKED_ATTRIBUTE`. Returned by GET\_MODEL\_DETAILS\_AI Function. |
| `DM_RULE` | A rule that defines a conditional relationship.  The rule can be one of the association rules returned by GET\_ASSOCIATION\_RULES Function, or it can be a rule associated with a cluster in the collection of clusters returned by GET\_MODEL\_DETAILS\_KM Function and GET\_MODEL\_DETAILS\_OC Function. |
| `DM_RULES` | A collection of `DM_RULE`. Returned by GET\_ASSOCIATION\_RULES Function. |
| `DM_SVM_ATTRIBUTE` | The name, value, and coefficient of an attribute in a Support Vector Machine model. |
| `DM_SVM_ATTRIBUTE_SET` | A collection of `DM_SVM_ATTRIBUTE`. Returned by GET\_MODEL\_DETAILS\_SVM Function. Also a member of `DM_SVM_LINEAR_COEFF`. |
| `DM_SVM_LINEAR_COEFF` | The linear coefficient of each attribute in a Support Vector Machine model. |
| `DM_SVM_LINEAR_COEFF_SET` | A collection of `DM_SVM_LINEAR_COEFF`. Returned by GET\_MODEL\_DETAILS\_SVM Function for an SVM model built using the linear kernel. |
| `DM_TRANSFORM` | The transformation and reverse transformation expressions for an attribute. |
| `DM_TRANSFORMS` | A collection of `DM_TRANSFORM`. Returned by GET\_MODEL\_TRANSFORMATIONS Function. |
| `TRANSFORM_LIST` | A list of user-specified transformations for a model. Accepted as a parameter by the CREATE\_MODEL Procedure.  This collection type is defined in the [DBMS\_DATA\_MINING\_TRANSFORM](d_dmtran.md) package. |

---

## Summary of DBMS\_DATA\_MINING Subprograms

Table 44-18 summarizes the subprograms included in the `DBMS_DATA_MINING` package.

Table 44-18 DBMS\_DATA\_MINING Package Subprograms

| Data Type | Purpose |
| --- | --- |
| ADD\_COST\_MATRIX Procedure | Adds a cost matrix to a classification model |
| ALTER\_REVERSE\_EXPRESSION Procedure | Changes the reverse transformation expression to an expression that you specify |
| APPLY Procedure | Applies a model to a data set (scores the data) |
| COMPUTE\_CONFUSION\_MATRIX Procedure | Computes the confusion matrix from the `APPLY` results on test data for a classification model; also provides the accuracy of the model |
| COMPUTE\_LIFT Procedure | Computes lift for a given positive target value from the `APPLY` results on test data for a classification model |
| COMPUTE\_ROC Procedure | Computes Receiver Operating Characteristic (ROC) for a classification model |
| CREATE\_MODEL Procedure | Creates (builds) a model |
| DROP\_MODEL Procedure | Drops a model |
| EXPORT\_MODEL Procedure | Exports a model to a dump file |
| GET\_ASSOCIATION\_RULES Function | Returns the rules from an association model |
| GET\_DEFAULT\_SETTINGS Function | Returns all the default settings for all mining functions and algorithms |
| GET\_FREQUENT\_ITEMSETS Function | Returns the frequent itemsets for an association model |
| GET\_MODEL\_COST\_MATRIX Function | Returns the cost matrix for a model |
| GET\_MODEL\_DETAILS\_ABN Function | Returns the details of an Adaptive Bayes Network model |
| GET\_MODEL\_DETAILS\_AI Function | Returns the details of an Attribute Importance model |
| GET\_MODEL\_DETAILS\_GLM Function | Returns the details of a Generalized Linear Model |
| GET\_MODEL\_DETAILS\_GLOBAL Function | Returns high-level statistics about a model |
| GET\_MODEL\_DETAILS\_KM Function | Returns the details of a k-Means model |
| GET\_MODEL\_DETAILS\_NB Function | Returns the details of a Naive Bayes model |
| GET\_MODEL\_DETAILS\_NMF Function | Returns the details of an NMF model |
| GET\_MODEL\_DETAILS\_OC Function | Returns the details of an O-Cluster model |
| GET\_MODEL\_DETAILS\_SVM Function | Returns the details of an SVM model with a linear kernel |
| GET\_MODEL\_DETAILS\_XML Function | Returns the details of a Decision Tree model |
| GET\_MODEL\_SETTINGS Function | Returns the settings used to build a model |
| GET\_MODEL\_SIGNATURE Function | Returns the signature of a model |
| GET\_MODEL\_TRANSFORMATIONS Function | Returns the user-specified transformation definitions embedded in the model, as well as many of the ADP transformations |
| GET\_TRANSFORM\_LIST Procedure | Converts between two different transformation specification formats |
| IMPORT\_MODEL Procedure | Imports a model into a user schema |
| RANK\_APPLY Procedure | Ranks the predictions from the `APPLY` results for a classification model |
| REMOVE\_COST\_MATRIX Procedure | Removes a cost matrix from a model |
| RENAME\_MODEL Procedure | Renames a model |

---

### ADD\_COST\_MATRIX Procedure

This procedure associates a cost matrix table with a classification model. The cost matrix biases the model by assigning costs or benefits to specific model outcomes.

The cost matrix is stored with the model and taken into account when the model is scored. The stored cost matrix is the default scoring matrix for the model.

You can also specify a cost matrix inline when you invoke a Data Mining SQL function for scoring. When an inline cost matrix is specified, it is used instead of the default, stored cost matrix (if one exists).

To obtain the default scoring matrix for a model, use the `GET_MODEL_COST_MATRIX` function. To remove the default scoring matrix from a model, use the `REMOVE_COST_MATRIX` procedure. See "GET\_MODEL\_COST\_MATRIX Function" and "REMOVE\_COST\_MATRIX Procedure".

See Also:

- "Biasing a Classification Model" in [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON050) for more information about costs
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions134.htm#SQLRF06210) for syntax of inline cost matrix

Syntax

```
DBMS_DATA_MINING.ADD_COST_MATRIX (
       model_name                IN VARCHAR2,
       cost_matrix_table_name    IN VARCHAR2,
       cost_matrix_schema_name   IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 44-19 ADD\_COST\_MATRIX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is assumed. |
| `cost_matrix_table_name` | Name of the cost matrix table (described in Table 44-20). |
| `cost_matrix_schema_name` | Schema of the cost matrix table. If no schema is specified, the current schema is used. |

Usage Notes

1. If the model is not in your schema, then `ADD_COST_MATRIX` requires the `ALTER ANY MINING MODEL` system privilege or the `ALTER` object privilege for the mining model.
2. The cost matrix table must have the columns shown in Table 44-20. Note that the actual and predicted target values must have the same data type.
	Table 44-20 Required Columns in a Cost Matrix Table
	| Column Name | Data Type |
	| --- | --- |
	| `ACTUAL_TARGET_VALUE` | `VARCHAR2(4000)` for categorical targets  `NUMBER` for numeric targets |
	| `PREDICTED_TARGET_VALUE` | `VARCHAR2(4000)` for categorical targets  `NUMBER` for numeric targets |
	| `COST` | `NUMBER` |
3. Since a benefit can be viewed as a negative cost, you can specify a benefit for a given outcome by providing a negative number in the `costs` column of the cost matrix table.
4. All classification algorithms can use a cost matrix for scoring. The Decision Tree algorithm can also use a cost matrix at build time.If you want to build a Decision Tree model with a cost matrix, specify the cost matrix table name in the `CLAS_COST_TABLE_NAME` setting in the settings table for the model. See Table 44-7, "Mining Function Settings".
	The cost matrix used to create a Decision Tree model becomes the default scoring matrix for the model. If you want to specify different costs for scoring, use the `REMOVE_COST_MATRIX` procedure to remove the cost matrix and the `ADD_COST_MATRIX` procedure to add a new one.

Example

This example creates a cost matrix table called `COSTS_NB` and adds it to a Naive Bayes model called `NB_SH_CLAS_SAMPLE`. The model has a binary target: 1 means that the customer responds to a promotion; 0 means that the customer does not respond. The cost matrix assigns a cost of.25 to misclassifications of customers who do not respond and a cost of.75 to misclassifications of customers who do respond. This means that it is three times more costly to misclassify responders than it is to misclassify non-responders.

```
CREATE TABLE costs_nb (
  actual_target_value           NUMBER,
  predicted_target_value        NUMBER,
  cost                          NUMBER);
INSERT INTO costs_nb values (0, 0, 0);
INSERT INTO costs_nb values (0, 1, .25);
INSERT INTO costs_nb values (1, 0, .75);
INSERT INTO costs_nb values (1, 1, 0);
COMMIT;
 
EXEC dbms_data_mining.add_cost_matrix('nb_sh_clas_sample', 'costs_nb');
 
SELECT cust_gender, COUNT(*) AS cnt, ROUND(AVG(age)) AS avg_age
   FROM mining_data_apply_v
   WHERE PREDICTION(nb_sh_clas_sample COST MODEL
      USING cust_marital_status, education, household_size) = 1
   GROUP BY cust_gender
   ORDER BY cust_gender;
   
C        CNT    AVG_AGE
- ---------- ----------
F         72         39
M        555         44
```

---

### ALTER\_REVERSE\_EXPRESSION Procedure

This procedure replaces a reverse transformation expression with an expression that you specify. If the attribute does not have a reverse expression, the procedure creates one from the specified expression.

You can also use this procedure to customize the output of clustering, feature extraction, and anomaly detection models.

Syntax

```
DBMS_DATA_MINING. ALTER_REVERSE_EXPRESSION (
         model_name             VARCHAR2,
         expression             CLOB,
         attribute_name         VARCHAR2 DEFAULT NULL,
         attribute_subname      VARCHAR2 DEFAULT NULL);
```

Parameters

Table 44-21 ALTER\_REVERSE\_EXPRESSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `expression` | A SQL expression |
| `attribute_name` | Name of the attribute. Specify `NULL` if you wish to apply `expression` to a cluster, feature, or One-Class SVM prediction. |
| `attribute_subname` | Name of the nested attribute if `attribute_name` is a nested column, otherwise `NULL`. |

Usage Notes

1. For purposes of model transparency, Oracle Data Mining provides reverse transformations for transformations that are embedded in a model. Reverse transformations are used in model details and in the results of scoring.
	See Also:
	[About Transformation Lists](d_dmtran.md) in [Chapter 45](d_dmtran.md)
	Note:
	Use caution when altering the reverse expression for the target of a model that has a cost matrix. If you specify a reverse expression that is inconsistent with the target values in the cost matrix table, you will not be able to score the model.
	See "ADD\_COST\_MATRIX Procedure" and [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON050) for information about cost matrixes.
2. To prevent reverse transformation of an attribute, you can specify `NULL` for `expression`.
3. You can use `ALTER_REVERSE_EXPRESSION` to label clusters produced by clustering models and features produced by feature extraction.
	You can use `ALTER_REVERSE_EXPRESSION` to replace the zeros and ones returned by anomaly-detection models. By default, anomaly-detection models label anomalous records with 0 and all other records with 1.
	See Also:
	[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/anomalies.htm#DMCON006) for information about anomaly detection

Examples

1. In this example, the target (`affinity_card`) of the model `CLASS_MODEL` is manipulated internally as `yes` or `no` instead of `1` or `0` but returned as `1` s and `0` s when scored. The `ALTER_REVERSE_EXPRESSION` procedure causes the target values to be returned as `TRUE` or `FALSE`.
	The data sets `MINING_DATA_BUILD` and `MINING_DATA_TEST` are included with the Oracle Data Mining sample programs. See [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009) for information about the sample programs.
	```
	DECLARE
	        v_xlst dbms_data_mining_transform.TRANSFORM_LIST;
	  BEGIN
	    dbms_data_mining_transform.SET_TRANSFORM(v_xlst,
	          'affinity_card', NULL,
	          'decode(affinity_card, 1, ''yes'', ''no'')',
	          'decode(affinity_card, ''yes'', 1, 0)');
	    dbms_data_mining.CREATE_MODEL(
	      model_name             => 'CLASS_MODEL',
	      mining_function        => dbms_data_mining.classification,
	      data_table_name        => 'mining_data_build',
	      case_id_column_name    => 'cust_id',
	      target_column_name     => 'affinity_card',
	      settings_table_name    => NULL,
	      data_schema_name       => 'dmuser',
	      settings_schema_name   => NULL,
	      xform_list             => v_xlst );
	  END;
	/
	SELECT cust_income_level, occupation,
	           PREDICTION(CLASS_MODEL USING *) predict_response
	      FROM mining_data_test WHERE age = 60 AND cust_gender IN 'M'
	      ORDER BY cust_income_level;
	 
	CUST_INCOME_LEVEL              OCCUPATION                PREDICT_RESPONSE
	------------------------------ --------------------- --------------------
	A: Below 30,000                Transp.                                  1
	E: 90,000 - 109,999            Transp.                                  1
	E: 90,000 - 109,999            Sales                                    1
	G: 130,000 - 149,999           Handler                                  0
	G: 130,000 - 149,999           Crafts                                   0
	H: 150,000 - 169,999           Prof.                                    1
	J: 190,000 - 249,999           Prof.                                    1
	J: 190,000 - 249,999           Sales                                    1
	 
	BEGIN
	  dbms_data_mining.ALTER_REVERSE_EXPRESSION (
	     model_name      => 'CLASS_MODEL',
	     expression      => 'decode(affinity_card, ''yes'', ''TRUE'', ''FALSE'')',
	     attribute_name  => 'affinity_card');
	END;
	/
	column predict_response on
	column predict_response format a20
	SELECT cust_income_level, occupation,
	             PREDICTION(CLASS_MODEL USING *) predict_response
	      FROM mining_data_test WHERE age = 60 AND cust_gender IN 'M'
	      ORDER BY cust_income_level;
	 
	CUST_INCOME_LEVEL              OCCUPATION            PREDICT_RESPONSE
	------------------------------ --------------------- --------------------
	A: Below 30,000                Transp.               TRUE
	E: 90,000 - 109,999            Transp.               TRUE
	E: 90,000 - 109,999            Sales                 TRUE
	G: 130,000 - 149,999           Handler               FALSE
	G: 130,000 - 149,999           Crafts                FALSE
	H: 150,000 - 169,999           Prof.                 TRUE
	J: 190,000 - 249,999           Prof.                 TRUE
	J: 190,000 - 249,999           Sales                 TRUE
	```
2. This example specifies labels for the clusters that result from the `sh_clus` model. The labels consist of the word "Cluster" and the internal numeric identifier for the cluster.
	```
	BEGIN
	  dbms_data_mining.ALTER_REVERSE_EXPRESSION( 'sh_clus', '''Cluster ''||value');
	END;
	/
	 
	SELECT cust_id, cluster_id(sh_clus using *) cluster_id
	   FROM sh_aprep_num
	       WHERE cust_id < 100011
	       ORDER by cust_id;
	 
	CUST_ID CLUSTER_ID
	------- ------------------------------------------------
	 100001 Cluster 18
	 100002 Cluster 14
	 100003 Cluster 14
	 100004 Cluster 18
	 100005 Cluster 19
	 100006 Cluster 7
	 100007 Cluster 18
	 100008 Cluster 14
	 100009 Cluster 8
	 100010 Cluster 8
	```

---

### APPLY Procedure

This procedure applies a mining model to the data of interest, and generates the results in a table. The apply process is also referred to as scoring.

For predictive mining functions, the apply process generates predictions in a target column. For descriptive mining functions such as clustering, the apply process assigns each case to a cluster with a probability.

In Oracle Data Mining, the apply operation is not applicable to association models and attribute importance models.

Note:

Scoring can also be performed directly in SQL using the Data Mining functions. See
- "Data Mining Functions" in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions002.htm#SQLRF20030)
- "Scoring and Deployment" in [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_deploying.htm#DMPRG004) and

Syntax

```
DBMS_DATA_MINING.APPLY (
      model_name           IN VARCHAR2,
      data_table_name      IN VARCHAR2,
      case_id_column_name  IN VARCHAR2,
      result_table_name    IN VARCHAR2,
      data_schema_name     IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 44-22 APPLY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `data_table_name` | Name of table or view representing data to be scored |
| `case_id_column_name` | Name of the case identifier column |
| `result_table_name` | Name of the table to store apply results |
| `data_schema_name` | Name of the schema containing the data to be scored |

Usage Notes

1. The data provided for `APPLY` must undergo the same preprocessing as the data used to create and test the model. When you use Automatic Data Preparation, the preprocessing required by the algorithm is handled for you by the model — both at build time and apply time. (See "Automatic Data Preparation".)
2. `APPLY` creates a table in the user's schema to hold the results. The columns are algorithm-specific.
	The columns in the results table are listed in Table 44-23 through Table 44-27. The case ID column name in the results table will match the case ID column name provided by you. The type of the incoming case ID column is also preserved in `APPLY` output.
	Note:
	Make sure that the case ID column does not have the same name as one of the columns that will be created by `APPLY`. For example, when applying a classification model, the case ID in the scoring data must not be ' `PREDICTION` ' or ' `PROBABILITY` ' (See Table 44-23).
3. The data type for the ' `PREDICTION` ', ' `CLUSTER_ID` ', and ' `FEATURE_ID` ' output columns is influenced by any reverse expression that is embedded in the model by the user. If the user does not provide a reverse expression that alters the scored value type, then the types will conform to the descriptions in the following tables. See "ALTER\_REVERSE\_EXPRESSION Procedure".

#### Classification

The results table for classification has the columns described in Table 44-23. If the target of the model is categorical, the `PREDICTION` column will have a `VARCHAR2` data type. If the target is numerical, the `PREDICTION` column will have a `NUMBER` data type.

Table 44-23 APPLY Results Table for Classification

| Column Name | Data Type |
| --- | --- |
| `Case ID column name` | `VARCHAR2` or `NUMBER` |
| `PREDICTION` | `VARCHAR2` or `NUMBER` |
| `PROBABILITY` | `NUMBER` |

#### One-Class SVM (Anomaly Detection)

The results table for anomaly detection has the columns described in Table 44-24.

Table 44-24 APPLY Results Table for Anomaly Detection

| Column Name | Data Type |
| --- | --- |
| `Case ID column name` | `VARCHAR2` or `NUMBER` |
| `PREDICTION` | `NUMBER` |
| `PROBABILITY` | `NUMBER` |

Values in the `PREDICTION` column can be either 0 or 1. When the prediction is 1, the case is a typical example. When the prediction is 0, the case is an outlier.

#### Regression using SVM or GLM

The results table for regression has the columns described in Table 44-25.

Table 44-25 APPLY Results Table for Regression

| Column Name | Data Type |
| --- | --- |
| `Case ID column name` | `VARCHAR2` or `NUMBER` |
| `PREDICTION` | `NUMBER` |

#### Clustering using k-Means or O-Cluster

Clustering is an unsupervised mining function, and hence there are no targets. The results of an `APPLY` operation will contain simply the cluster identifier corresponding to a case, and the associated probability. The results table has the columns described in Table 44-26.

Table 44-26 APPLY Results Table for Clustering

| Column Name | Data Type |
| --- | --- |
| `Case ID column name` | `VARCHAR2` or `NUMBER` |
| `CLUSTER_ID` | `NUMBER` |
| `PROBABILITY` | `NUMBER` |

#### Feature Extraction using NMF

Feature extraction is also an unsupervised mining function, and hence there are no targets. The results of an `APPLY` operation will contain simply the feature identifier corresponding to a case, and the associated match quality. The results table has the columns described in Table 44-27.

Table 44-27 APPLY Results Table for Feature Extraction

| Column Name | Data Type |
| --- | --- |
| `Case ID column name` | `VARCHAR2` or `NUMBER` |
| `FEATURE_ID` | `NUMBER` |
| `MATCH_QUALITY` | `NUMBER` |

Examples

This example applies the GLM regression model `GLMR_SH_REGR_SAMPLE` to the data in the `MINING_DATA_APPLY_V` view. The apply results are output to the table `REGRESSION_APPLY_RESULT`.

```
SQL> BEGIN
       DBMS_DATA_MINING.APPLY (
       model_name     => 'glmr_sh_regr_sample',
       data_table_name     => 'mining_data_apply_v',
       case_id_column_name => 'cust_id',
       result_table_name   => 'regression_apply_result');
    END;
    /
 
SQL> SELECT * FROM regression_apply_result WHERE cust_id >  101485;
 
   CUST_ID PREDICTION
---------- ----------
    101486 22.8048824
    101487 25.0261101
    101488 48.6146619
    101489   51.82595
    101490 22.6220714
    101491 61.3856816
    101492 24.1400748
    101493  58.034631
    101494 45.7253149
    101495 26.9763318
    101496 48.1433425
    101497 32.0573434
    101498 49.8965531
    101499  56.270656
    101500 21.1153047
```

---

### COMPUTE\_CONFUSION\_MATRIX Procedure

This procedure computes a confusion matrix, stores it in a table in the user's schema, and returns the model accuracy.

A confusion matrix is a test metric for classification models. It compares the predictions generated by the model with the actual target values in a set of test data. The matrix is n-by-n, where n is the number of classes. The confusion matrix lists the number of times each class was correctly predicted and the number of times it was predicted to be one of the other classes.

`COMPUTE_CONFUSION_MATRIX` accepts three input streams:

- The predictions generated on the test data. The information is passed in three columns:
	- Case ID column
		- Prediction column
		- Scoring criterion column containing either probabilities or costs
- The known target values in the test data. The information is passed in two columns:
	- Case ID column
		- Target column containing the known target values
- (Optional) A cost matrix table with predefined columns. See the Usage Notes for the column requirements.

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON034) for more details about confusion matrixes and other test metrics for classification

"COMPUTE\_LIFT Procedure"

"COMPUTE\_ROC Procedure"

Syntax

```
DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX (
      accuracy                     OUT NUMBER,
      apply_result_table_name      IN  VARCHAR2,
      target_table_name            IN  VARCHAR2,
      case_id_column_name          IN  VARCHAR2,
      target_column_name           IN  VARCHAR2,
      confusion_matrix_table_name  IN  VARCHAR2,
      score_column_name            IN  VARCHAR2 DEFAULT 'PREDICTION',
      score_criterion_column_name  IN  VARCHAR2 DEFAULT 'PROBABILITY',
      cost_matrix_table_name       IN  VARCHAR2 DEFAULT NULL,
      apply_result_schema_name     IN  VARCHAR2 DEFAULT NULL,
      target_schema_name           IN  VARCHAR2 DEFAULT NULL,
      cost_matrix_schema_name      IN  VARCHAR2 DEFAULT NULL,
      score_criterion_type         IN  VARCHAR2 DEFAULT 'PROBABILITY');
```

Parameters

Table 44-28 COMPUTE\_CONFUSION\_MATRIX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `accuracy` | Output parameter containing the overall percentage accuracy of the predictions. |
| `apply_result_table_name` | Table containing the predictions. |
| `target_table_name` | Table containing the known target values from the test data. |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data. |
| `confusion_matrix_table_name` | Table containing the confusion matrix. The table will be created by the procedure in the user's schema.  The columns in the confusion matrix table are described in the Usage Notes. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is `PREDICTION`, which is the default name created by the `APPLY` procedure (See "APPLY Procedure"). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains either the probabilities or the costs that determine the predictions.  By default, scoring is based on probability; the class with the highest probability is predicted for each case. If scoring is based on cost, the class with the lowest cost is predicted.  The `score_criterion_type` parameter indicates whether probabilities or costs will be used for scoring.  The default column name is ' `PROBABILITY'`, which is the default name created by the `APPLY` procedure (See "APPLY Procedure").  See the Usage Notes for additional information. |
| `cost_matrix_table_name` | (Optional) Table that defines the costs associated with misclassifications. If a cost matrix table is provided and the `score_criterion_type` parameter is set to `'COSTS'`, the costs in this table will be used as the scoring criteria.  The columns in a cost matrix table are described in the Usage Notes. |
| `apply_result_schema_name` | Schema of the apply results table.  If null, the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, the user's schema is assumed. |
| `cost_matrix_schema_name` | Schema of the cost matrix table, if one is provided.  If null, the user's schema is assumed. |
| `score_criterion_type` | Whether to use probabilities or costs as the scoring criterion. Probabilities or costs are passed in the column identified in the `score_criterion_column_name` parameter.  The default value of `score_criterion_type` is `'PROBABILITY'`. To use costs as the scoring criterion, specify `'COST'`.  If `score_criterion_type` is set to ' `COST` ' but no cost matrix is provided and if there is a scoring cost matrix associated with the model, then the associated costs are used for scoring.  See the Usage Notes and the Examples. |

Usage Notes

- The predictive information you pass to `COMPUTE_CONFUSION_MATRIX` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the confusion matrix.
- Instead of passing a cost matrix to `COMPUTE_CONFUSION_MATRIX`, you can use a scoring cost matrix associated with the model. A scoring cost matrix can be embedded in the model or it can be defined dynamically when the model is applied. To use a scoring cost matrix, invoke the SQL `PREDICTION_COST` function to populate the score criterion column.
- The predictions that you pass to `COMPUTE_CONFUSION_MATRIX` are in a table or view specified in `apply_result_table_name`.
	```
	CREATE TABLE apply_result_table_name
	 AS (
	            case_id_column_name
	            VARCHAR2, 
	            score_column_name              VARCHAR2,
	            score_criterion_column_name
	    VARCHAR2);
	```
- A cost matrix must have the columns described in Table 44-29.
	Table 44-29 Columns in a Cost Matrix
	| Column Name | Data Type |
	| --- | --- |
	| `actual_target_value` | `NUMBER` or `VARCHAR2` |
	| `predicted_target_value` | `NUMBER` or `VARCHAR2` |
	| `cost` | `NUMBER` |
	See Also:
	[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON032) for more information about cost matrixes
- The confusion matrix created by `COMPUTE_CONFUSION_MATRIX` has the columns described in Table 44-30.
	Table 44-30 Columns in a Confusion Matrix
	| Column Name | Data Type |
	| --- | --- |
	| `actual_target_value` | `NUMBER` or `VARCHAR2` |
	| `predicted_target_value` | `NUMBER` or `VARCHAR2` |
	| `value` | `NUMBER` |
	See Also:
	[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON034) for more information about confusion matrixes

Examples

These examples use the Naive Bayes model `nb_sh_clas_sample`, which is created by one of the Oracle Data Mining sample programs.

Compute a Confusion Matrix Based on Probabilities

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```
CREATE TABLE nb_apply_results AS
       SELECT cust_id,
              PREDICTION(nb_sh_clas_sample USING *) prediction,
              PREDICTION_PROBABILITY(nb_sh_clas_sample USING *) probability
       FROM mining_data_test_v;
```

Using probabilities as the scoring criterion, you can compute the confusion matrix as follows.

```
DECLARE
   v_accuracy    NUMBER;
      BEGIN
        DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX (
                   accuracy                     => v_accuracy,
                   apply_result_table_name      => 'nb_apply_results',
                   target_table_name            => 'mining_data_test_v',
                   case_id_column_name          => 'cust_id',
                   target_column_name           => 'affinity_card',
                   confusion_matrix_table_name  => 'nb_confusion_matrix',
                   score_column_name            => 'PREDICTION',
                   score_criterion_column_name  => 'PROBABILITY'
                   cost_matrix_table_name       =>  null,
                   apply_result_schema_name     =>  null,
                   target_schema_name           =>  null,
                   cost_matrix_schema_name      =>  null,
                   score_criterion_type         => 'PROBABILITY');
        DBMS_OUTPUT.PUT_LINE('**** MODEL ACCURACY ****: ' || ROUND(v_accuracy,4));
      END;
      /
```

The confusion matrix and model accuracy are shown as follows.

```
**** MODEL ACCURACY ****: .7847

SQL>SELECT * from nb_confusion_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         60
                  0                      0        891
                  1                      1        286
                  0                      1        263
```

Compute a Confusion Matrix Based on a Cost Matrix Table

The confusion matrix in the previous example shows a high rate of false positives. For 263 cases, the model predicted 1 when the actual value was 0. You could use a cost matrix to minimize this type of error.

The cost matrix table `nb_cost_matrix` specifies that a false positive is 3 times more costly than a false negative.

```
SQL> SELECT * from nb_cost_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE       COST
------------------- ---------------------- ----------
                  0                      0          0
                  0                      1        .75
                  1                      0        .25
                  1                      1          0
```

This statement shows how to generate the predictions using `APPLY`.

```
BEGIN
    DBMS_DATA_MINING.APPLY(
          model_name          => 'nb_sh_clas_sample',
          data_table_name     => 'mining_data_test_v',
          case_id_column_name => 'cust_id',
          result_table_name   => 'nb_apply_results');
 END;
/
```

This statement computes the confusion matrix using the cost matrix table. The score criterion column is named ' `PROBABILITY` ', which is the name generated by `APPLY`.

```
DECLARE
  v_accuracy    NUMBER;
     BEGIN
       DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX (
                accuracy                     => v_accuracy,
                apply_result_table_name      => 'nb_apply_results',
                target_table_name            => 'mining_data_test_v',
                case_id_column_name          => 'cust_id',
                target_column_name           => 'affinity_card',
                confusion_matrix_table_name  => 'nb_confusion_matrix',
                score_column_name            => 'PREDICTION',
                score_criterion_column_name  => 'PROBABILITY',
                cost_matrix_table_name       => 'nb_cost_matrix',
                apply_result_schema_name     => null,
                target_schema_name           => null,
                cost_matrix_schema_name      => null,
                score_criterion_type         => 'COST');
       DBMS_OUTPUT.PUT_LINE('**** MODEL ACCURACY ****: ' || ROUND(v_accuracy,4));
    END;
    /
```

The resulting confusion matrix shows a decrease in false positives (212 instead of 263).

```
**** MODEL ACCURACY ****: .798

SQL> SELECT * FROM nb_confusion_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         91
                  0                      0        942
                  1                      1        255
                  0                      1        212
```

Compute a Confusion Matrix Based on Embedded Costs

You can use the `ADD_COST_MATRIX` procedure to embed a cost matrix in a model. The embedded costs can be used instead of probabilities for scoring. This statement adds the previously-defined cost matrix to the model.

```
BEGIN    DBMS_DATA_MINING.ADD_COST_MATRIX ('nb_sh_clas_sample', 'nb_cost_matrix');END;/
```

The following statement applies the model to the test data using the embedded costs and stores the results in a table.

```
CREATE TABLE nb_apply_results AS
         SELECT cust_id,
              PREDICTION(nb_sh_clas_sample COST MODEL USING *) prediction,
              PREDICTION_COST(nb_sh_clas_sample COST MODEL USING *) cost
          FROM mining_data_test_v;
```

You can compute the confusion matrix using the embedded costs.

```
DECLARE
   v_accuracy         NUMBER;
   BEGIN
       DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX (
            accuracy                     => v_accuracy,
            apply_result_table_name      => 'nb_apply_results',
            target_table_name            => 'mining_data_test_v',
            case_id_column_name          => 'cust_id',
            target_column_name           => 'affinity_card',
            confusion_matrix_table_name  => 'nb_confusion_matrix',
            score_column_name            => 'PREDICTION',
            score_criterion_column_name  => 'COST',
            cost_matrix_table_name       => null,
            apply_result_schema_name     => null,
            target_schema_name           => null,
            cost_matrix_schema_name      => null,
            score_criterion_type         => 'COST');
   END;
   /
```

The results are:

```
**** MODEL ACCURACY ****: .798

SQL> SELECT * FROM nb_confusion_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         91
                  0                      0        942
                  1                      1        255
                  0                      1        212
```

---

### COMPUTE\_LIFT Procedure

This procedure computes lift and stores the results in a table in the user's schema.

Lift is a test metric for binary classification models. To compute lift, one of the target values must be designated as the positive class. `COMPUTE_LIFT` compares the predictions generated by the model with the actual target values in a set of test data. Lift measures the degree to which the model's predictions of the positive class are an improvement over random chance.

Lift is computed on scoring results that have been ranked by probability (or cost) and divided into quantiles. Each quantile includes the scores for the same number of cases.

`COMPUTE_LIFT` calculates quantile-based and cumulative statistics. The number of quantiles and the positive class are user-specified. Additionally, `COMPUTE_LIFT` accepts three input streams:

- The predictions generated on the test data. The information is passed in three columns:
	- Case ID column
		- Prediction column
		- Scoring criterion column containing either probabilities or costs associated with the predictions
- The known target values in the test data. The information is passed in two columns:
	- Case ID column
		- Target column containing the known target values
- (Optional) A cost matrix table with predefined columns. See the Usage Notes for the column requirements.

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON053) for more details about lift and test metrics for classification

"COMPUTE\_CONFUSION\_MATRIX Procedure"

"COMPUTE\_ROC Procedure"

Syntax

```
DBMS_DATA_MINING.COMPUTE_LIFT (
      apply_result_table_name      IN VARCHAR2,
      target_table_name            IN VARCHAR2,
      case_id_column_name          IN VARCHAR2,
      target_column_name           IN VARCHAR2,
      lift_table_name              IN VARCHAR2,
      positive_target_value        IN VARCHAR2,
      score_column_name            IN VARCHAR2 DEFAULT 'PREDICTION',
      score_criterion_column_name  IN VARCHAR2 DEFAULT 'PROBABILITY',
      num_quantiles                IN NUMBER DEFAULT 10,
      cost_matrix_table_name       IN VARCHAR2 DEFAULT NULL,
      apply_result_schema_name     IN VARCHAR2 DEFAULT NULL,
      target_schema_name           IN VARCHAR2 DEFAULT NULL,
      cost_matrix_schema_name      IN VARCHAR2 DEFAULT NULL
      score_criterion_type         IN VARCHAR2 DEFAULT 'PROBABILITY');
```

Parameters

Table 44-31 COMPUTE\_LIFT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `apply_result_table_name` | Table containing the predictions. |
| `target_table_name` | Table containing the known target values from the test data. |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data. |
| `lift_table_name` | Table containing the lift statistics. The table will be created by the procedure in the user's schema.  The columns in the lift table are described in the Usage Notes. |
| `positive_target_value` | The positive class. This should be the class of interest, for which you want to calculate lift.  If the target column is a `NUMBER`, you can use the `TO_CHAR()` operator to provide the value as a string. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is ' `PREDICTION` ', which is the default name created by the `APPLY` procedure (See "APPLY Procedure"). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains either the probabilities or the costs that determine the predictions.  By default, scoring is based on probability; the class with the highest probability is predicted for each case. If scoring is based on cost, the class with the lowest cost is predicted.  The `score_criterion_type` parameter indicates whether probabilities or costs will be used for scoring.  The default column name is ' `PROBABILITY` ', which is the default name created by the `APPLY` procedure (See "APPLY Procedure").  See the Usage Notes for additional information. |
| `num_quantiles` | Number of quantiles to be used in calculating lift. The default is 10. |
| `cost_matrix_table_name` | (Optional) Table that defines the costs associated with misclassifications. If a cost matrix table is provided and the `score_criterion_type` parameter is set to ' `COST` ', the costs will be used as the scoring criteria.  The columns in a cost matrix table are described in the Usage Notes. |
| `apply_result_schema_name` | Schema of the apply results table.  If null, the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, the user's schema is assumed. |
| `cost_matrix_schema_name` | Schema of the cost matrix table, if one is provided.  If null, the user's schema is assumed. |
| `score_criterion_type` | Whether to use probabilities or costs as the scoring criterion. Probabilities or costs are passed in the column identified in the `score_criterion_column_name` parameter.  The default value of `score_criterion_type` is ' `PROBABILITY` '. To use costs as the scoring criterion, specify ' `COST` '.  If `score_criterion_type` is set to ' `COST` ' but no cost matrix is provided and if there is a scoring cost matrix associated with the model, then the associated costs are used for scoring.  See the Usage Notes and the Examples. |

Usage Notes

- The predictive information you pass to `COMPUTE_LIFT` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the lift.
- Instead of passing a cost matrix to `COMPUTE_LIFT`, you can use a scoring cost matrix associated with the model. A scoring cost matrix can be embedded in the model or it can be defined dynamically when the model is applied. To use a scoring cost matrix, invoke the SQL `PREDICTION_COST` function to populate the score criterion column.
- The predictions that you pass to `COMPUTE_LIFT` are in a table or view specified in `apply_results_table_name`.
	```
	CREATE TABLE apply_result_table_name
	 AS (
	            case_id_column_name
	            VARCHAR2, 
	            score_column_name              VARCHAR2,
	            score_criterion_column_name
	    VARCHAR2);
	```
- A cost matrix must have the columns described in Table 44-32.
	Table 44-32 Columns in a Cost Matrix
	| Column Name | Data Type |
	| --- | --- |
	| `actual_target_value` | `NUMBER` or `VARCHAR2` |
	| `predicted_target_value` | `NUMBER` or `VARCHAR2` |
	| `cost` | `NUMBER` |
	See Also:
	[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON032) for more information about cost matrixes
- The table created by `COMPUTE_LIFT` has the columns described in Table 44-33
	Table 44-33 Columns in a Lift Table
	| Column Name | Data Type |
	| --- | --- |
	| `quantile_number` | `NUMBER` |
	| `probability_threshold` | `NUMBER` |
	| `gain_cumulative` | `NUMBER` |
	| `quantile_total_count` | `NUMBER` |
	| `quantile_target_count` | `NUMBER` |
	| `percent_records_cumulative` | `NUMBER` |
	| `lift_cumulative` | `NUMBER` |
	| `target_density_cumulative` | `NUMBER` |
	| `targets_cumulative` | `NUMBER` |
	| `non_targets_cumulative` | `NUMBER` |
	| `lift_quantile` | `NUMBER` |
	| `target_density` | `NUMBER` |
	See Also:
	[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON035) for details about the information in the lift table
- When a cost matrix is passed to `COMPUTE_LIFT`, the cost threshold is returned in the `probability_threshold` column of the lift table.

Examples

This example uses the Naive Bayes model `nb_sh_clas_sample`, which is created by one of the Oracle Data Mining sample programs.

The example illustrates lift based on probabilities. For examples that show computation based on costs, see "COMPUTE\_CONFUSION\_MATRIX Procedure".

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```
CREATE TABLE nb_apply_results AS
    SELECT cust_id, t.prediction, t.probability
    FROM mining_data_test_v, TABLE(PREDICTION_SET(nb_sh_clas_sample USING *)) t;
```

Using probabilities as the scoring criterion, you can compute lift as follows.

```
BEGIN
           DBMS_DATA_MINING.COMPUTE_LIFT (
              apply_result_table_name              => 'nb_apply_results',
              target_table_name                => 'mining_data_test_v',
              case_id_column_name              => 'cust_id',
              target_column_name               => 'affinity_card',
              lift_table_name                             => 'nb_lift',
              positive_target_value                 =>  to_char(1),
              score_column_name                => 'PREDICTION',
              score_criterion_column_name    => 'PROBABILITY',
              num_quantiles                                =>  10,
              cost_matrix_table_name                =>  null,
              apply_result_schema_name            =>  null,
              target_schema_name               =>  null,
              cost_matrix_schema_name              =>  null,
              score_criterion_type                   =>  'PROBABILITY');
        END;
        /
```

This query displays some of the statistics from the resulting lift table.

```
SQL>SELECT quantile_number, probability_threshold, gain_cumulative,
           quantile_total_count
           FROM nb_lift;

QUANTILE_NUMBER PROBABILITY_THRESHOLD GAIN_CUMULATIVE QUANTILE_TOTAL_COUNT 
--------------- --------------------- --------------- --------------------  
              1            .989335775       .15034965                   55 
              2            .980534911       .26048951                   55  
              3            .968506098      .374125874                   55  
              4            .958975196      .493006993                   55 
              5            .946705997      .587412587                   55  
              6            .927454174       .66958042                   55  
              7            .904403627      .748251748                   55  
              8            .836482525      .839160839                   55  
             10            .500184953               1                   54
```

---

### COMPUTE\_ROC Procedure

This procedure computes receiver operating characteristic (ROC), stores the results in a table in the user's schema, and returns a measure of the model accuracy.

ROC is a test metric for binary classification models. To compute ROC, one of the target values must be designated as the positive class. `COMPUTE_ROC` compares the predictions generated by the model with the actual target values in a set of test data.

ROC measures the impact of changes in the probability threshold. The probability threshold is the decision point used by the model for predictions. In binary classification, the default probability threshold is 0.5. The value predicted for each case is the one with a probability greater than 50%.

ROC can be plotted as a curve on an X-Y axis. The false positive rate is placed on the X axis. The true positive rate is placed on the Y axis. A false positive is a positive prediction for a case that is negative in the test data. A true positive is a positive prediction for a case that is positive in the test data.

`COMPUTE_ROC` accepts two input streams:

- The predictions generated on the test data. The information is passed in three columns:
	- Case ID column
		- Prediction column
		- Scoring criterion column containing probabilities
- The known target values in the test data. The information is passed in two columns:
	- Case ID column
		- Target column containing the known target values

See Also:

[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON054) for more details about ROC and test metrics for classification

"COMPUTE\_CONFUSION\_MATRIX Procedure"

"COMPUTE\_LIFT Procedure"

Syntax

```
DBMS_DATA_MINING.COMPUTE_ROC (
      roc_area_under_curve         OUT NUMBER,
      apply_result_table_name      IN  VARCHAR2,
      target_table_name            IN  VARCHAR2,
      case_id_column_name          IN  VARCHAR2,
      target_column_name           IN  VARCHAR2,
      roc_table_name               IN  VARCHAR2,
      positive_target_value        IN  VARCHAR2,
      score_column_name            IN  VARCHAR2 DEFAULT 'PREDICTION',
      score_criterion_column_name  IN  VARCHAR2 DEFAULT 'PROBABILITY',
      apply_result_schema_name     IN  VARCHAR2 DEFAULT NULL,
      target_schema_name           IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 44-34 COMPUTE\_ROC Procedure Parameters

| Parameter | Description |
| --- | --- |
| `roc_area_under_the_curve` | Output parameter containing the area under the ROC curve (AUC). The AUC measures the likelihood that an actual positive will be predicted as positive.  The greater the AUC, the greater the flexibility of the model in accommodating trade-offs between positive and negative class predictions. AUC can be especially important when one target class is rarer or more important to identify than another. |
| `apply_result_table_name` | Table containing the predictions. |
| `target_table_name` | Table containing the known target values from the test data. |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data. |
| `roc_table_name` | Table containing the ROC output. The table will be created by the procedure in the user's schema.  The columns in the ROC table are described in the Usage Notes. |
| `positive_target_value` | The positive class. This should be the class of interest, for which you want to calculate ROC.  If the target column is a `NUMBER`, you can use the `TO_CHAR()` operator to provide the value as a string. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is ' `PREDICTION` ', which is the default name created by the `APPLY` procedure (See "APPLY Procedure"). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains the probabilities that determine the predictions.  The default column name is ' `PROBABILITY` ', which is the default name created by the `APPLY` procedure (See "APPLY Procedure"). |
| `apply_result_schema_name` | Schema of the apply results table.  If null, the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, the user's schema is assumed. |

Usage Notes

- The predictive information you pass to `COMPUTE_ROC` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the receiver operating characteristic.
- The predictions that you pass to `COMPUTE_ROC` are in a table or view specified in `apply_results_table_name`.
	```
	CREATE TABLE apply_result_table_name
	 AS (
	            case_id_column_name
	            VARCHAR2, 
	            score_column_name              VARCHAR2,
	            score_criterion_column_name
	    VARCHAR2);
	```
- The table created by `COMPUTE_ROC` has the columns shown in Table 44-35.
	Table 44-35 COMPUTE\_ROC Output
	| Column | Data Type |
	| --- | --- |
	| `probability` | `NUMBER` |
	| `true_positives` | `NUMBER` |
	| `false_negatives` | `NUMBER` |
	| `false_positives` | `NUMBER` |
	| `true_negatives` | `NUMBER` |
	| `true_positive_fraction` | `NUMBER` |
	| `false_positive_fraction` | `NUMBER` |
	See Also:
	[Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/classify.htm#DMCON054) for details about the output of `COMPUTE_ROC`
- ROC is typically used to determine the most desirable probability threshold. This can be done by examining the true positive fraction and the false positive fraction. The true positive fraction is the percentage of all positive cases in the test data that were correctly predicted as positive. The false positive fraction is the percentage of all negative cases in the test data that were incorrectly predicted as positive.
	Given a probability threshold, the following statement returns the positive predictions in an apply result table ordered by probability.
	```
	SELECT case_id_column_name 
	       FROM apply_result_table_name 
	       WHERE probability
	 > probability_threshold
	 
	       ORDER BY probability
	 DESC;
	```
- There are two approaches to identifying the most desirable probability threshold. Which approach you use depends on whether or not you know the relative cost of positive versus negative class prediction errors.
	If the costs are known, you can apply the relative costs to the ROC table to compute the minimum cost probability threshold. Suppose the relative cost ratio is: Positive Class Error Cost / Negative Class Error Cost = 20. Then execute a query like this.
	```
	WITH cost
	 AS (
	  SELECT probability_threshold
	, 20 * false_negatives
	 + false_positives
	 cost
	 
	    FROM ROC_table
	 
	  GROUP BY probability_threshold
	), 
	    minCost
	 AS (
	      SELECT min(cost
	) minCost
	 
	        FROM cost
	)
	      SELECT max(probability_threshold
	)probability_threshold 
	        FROM cost
	, minCost
	 
	    WHERE cost
	 = minCost
	;
	```
	If relative costs are not well known, you can simply scan the values in the ROC table (in sorted order) and make a determination about which of the displayed trade-offs (misclassified positives versus misclassified negatives) is most desirable.
	```
	SELECT * FROM ROC_table
	 
	         ORDER BY probability_threshold
	;
	```

Examples

This example uses the Naive Bayes model `nb_sh_clas_sample`, which is created by one of the Oracle Data Mining sample programs.

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```
CREATE TABLE nb_apply_results AS
    SELECT cust_id, t.prediction, t.probability
    FROM mining_data_test_v, TABLE(PREDICTION_SET(nb_sh_clas_sample USING *)) t;
```

Using the predictions and the target values from the test data, you can compute ROC as follows.

```
DECLARE
     v_area_under_curve NUMBER;
  BEGIN
         DBMS_DATA_MINING.COMPUTE_ROC (
               roc_area_under_curve                  => v_area_under_curve,
               apply_result_table_name       => 'nb_apply_results',
               target_table_name               => 'mining_data_test_v',
               case_id_column_name            => 'cust_id',
               target_column_name             => 'affinity_card',
               roc_table_name                     => 'nb_roc',
               positive_target_value         => '1',
               score_column_name               => 'PREDICTION',
               score_criterion_column_name   => 'PROBABILITY');
           DBMS_OUTPUT.PUT_LINE('**** AREA UNDER ROC CURVE ****: ' ||
           ROUND(v_area_under_curve,4));
  END;
 /
```

The resulting AUC and a selection of columns from the ROC table are shown as follows.

```
**** AREA UNDER ROC CURVE ****: .8212

SQL> SELECT probability, true_positive_fraction, false_positive_fraction 
            FROM nb_roc;
 
PROBABILITY  TRUE_POSITIVE_FRACTION  FALSE_POSITIVE_FRACTION
-----------  ----------------------  -----------------------
     .00000                       1                        1
     .50018              .826589595               .227902946
     .53851              .823699422               .221837088
     .54991              .820809249               .217504333
     .55628              .815028902               .215771231
     .55628              .817919075               .215771231
     .57563              .800578035               .214904679
     .57563              .812138728               .214904679
      .                   .                        .
      .                   .                        .
      .                   .                        .
```

---

### CREATE\_MODEL Procedure

This procedure creates a mining model with a given mining function.

By passing an `xform_list` to `CREATE_MODEL`, you can specify a list of transformations to be performed on the input data. If the `PREP_AUTO` setting is on, the transformations are used in addition to the automatic transformations. If the `PREP_AUTO` setting is off, the specified transformations are the only ones implemented by the model. In both cases, the transformation definitions are embedded in the model and executed automatically whenever the model is applied. See "Automatic Data Preparation".

Syntax

```
DBMS_DATA_MINING.CREATE_MODEL (
      model_name            IN VARCHAR2,
      mining_function       IN VARCHAR2,
      data_table_name       IN VARCHAR2,
      case_id_column_name   IN VARCHAR2,
      target_column_name    IN VARCHAR2 DEFAULT NULL,
      settings_table_name   IN VARCHAR2 DEFAULT NULL,
      data_schema_name      IN VARCHAR2 DEFAULT NULL,
      settings_schema_name  IN VARCHAR2 DEFAULT NULL,
      xform_list            IN TRANSFORM_LIST DEFAULT NULL);
```

Parameters

Table 44-36 CREATE\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. See also "Mining Model Naming Restrictions". |
| `mining_function` | The mining function. Values are listed in Table 44-2, "Mining Functions". |
| `data_table_name` | Table or view containing the build data. |
| `case_id_column_name` | Case identifier column in the build data. |
| `target_column_name` | For supervised models, the target column in the build data. `NULL` for unsupervised models. |
| `settings_table_name` | Table containing build settings for the model. `NULL` if there is no settings table (only default settings are used). |
| `data_schema_name` | Schema hosting the build data. If `NULL`, the user's schema is assumed. |
| `settings_schema_name` | Schema hosting the settings table. If `NULL`, the user's schema is assumed. |
| `xform_list` | A list of transformations to be used in addition to or instead of automatic transformations, depending on the value of the `PREP_AUTO` setting. (See "Automatic Data Preparation".)  The data type is `TRANSFORM_LIST`, which consists of records of type `TRANSFORM_REC`.  ``` TYPE   TRANFORM_REC     IS RECORD (      attribute_name       VARCHAR2(4000),      attribute_subname    VARCHAR2(4000),      expression           EXPRESSION_REC,      reverse_expression   EXPRESSION_REC,      attribute_spec       VARCHAR2(4000)); ```  Each `TRANSFORM_REC` describes the transformation and reverse transformation for an attribute. `EXPRESSION_REC` stores a SQL expression.  The SQL expression stored in `EXPRESSION_REC` can be manipulated using routines in the `DBMS_DATA_MINING_TRANSFORM` package. Examples are: `SET_EXPRESSION`, `GET_EXPRESSION`, and `SET_TRANSFORM`.  You can use `ATTRIBUTE_SPEC` to disable Automatic Data Preparation (ADP) for an individual attribute. Specify ' `NOPREP` ' to prevent automatic preparation of this attribute when ADP is on. When ADP is off, the ' `NOPREP` ' value is ignored.  The ' `NOPREP` ' value cannot be used for an individual subname of a nested attribute. If ' `NOPREP` ' is specified for an individual subname when ADP is on, an error is generated. |

Usage Notes

You can obtain information about a model by querying these data dictionary views.

  
`ALL_MINING_MODELS`  
`ALL_MINING_MODEL_ATTRIBUTES`  
`ALL_MINING_MODEL_SETTINGS`  

Specify the `USER` prefix instead of `ALL` to obtain information about models in your own schema only.

See Also:

[Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/api_tour.htm#DMPRG012) for information on the data dictionary views

Examples

The first example builds a classification model using the Support Vector Machine algorithm.

```
-- Create the settings table 
CREATE TABLE svm_model_settings (
  setting_name  VARCHAR2(30),
  setting_value VARCHAR2(30));

-- Populate the settings table
-- Specify SVM. By default, Naive Bayes is used for classification.
-- Specify ADP. By default, ADP is not used.
BEGIN 
  INSERT INTO svm_model_settings (setting_name, setting_value) VALUES
     (dbms_data_mining.algo_name, dbms_data_mining.algo_support_vector_machines);
  INSERT INTO svm_model_settings (setting_name, setting_value) VALUES
     (dbms_data_mining.prep_auto,dbms_data_mining.prep_auto_on);
  COMMIT;
END;
/
-- Create the model using the specified settings 
BEGIN
  DBMS_DATA_MINING.CREATE_MODEL(
    model_name          => 'svm_model',
    mining_function     => dbms_data_mining.classification,
    data_table_name     => 'mining_data_build_v',
    case_id_column_name => 'cust_id',
    target_column_name  => 'affinity_card',
    settings_table_name => 'svm_model_settings');
END;
/
```

You can display the model settings with the following query.

```
SELECT * FROM user_mining_model_settings 
       WHERE model_name IN 'SVM_MODEL';

MODEL_NAME     SETTING_NAME            SETTING_VALUE                  SETTING
-------------  ----------------------  -----------------------------  -------
SVM_MODEL      ALGO_NAME               ALGO_SUPPORT_VECTOR_MACHINES  INPUT
SVM_MODEL      SVMS_KERNEL_CACHE_SIZE  50000000                      DEFAULT
SVM_MODEL      SVMS_ACTIVE_LEARNING    SVMS_AL_ENABLE                DEFAULT
SVM_MODEL      SVMS_STD_DEV            3.004524                      DEFAULT
SVM_MODEL      PREP_AUTO               ON                            INPUT
SVM_MODEL      SVMS_COMPLEXITY_FACTOR  1.887389                      DEFAULT
SVM_MODEL      SVMS_KERNEL_FUNCTION    SVMS_GAUSSIAN                 DEFAULT
SVM_MODEL      SVMS_CONV_TOLERANCE     .001                          DEFAULT
```

The second example creates an anomaly detection model. Anomaly detection uses SVM classification without a target. This example uses the same settings table created for the SVM classification model in the first example.

```
BEGIN
  DBMS_DATA_MINING.CREATE_MODEL(
    model_name          => 'anomaly_detect_model',
    mining_function     => dbms_data_mining.classification,
    data_table_name     => 'mining_data_build_v',
    case_id_column_name => 'cust_id',
    target_column_name  => null,
    settings_table_name => 'svm_model_settings');
END;
/
```

This query shows that the models created in these examples are the only ones in your schema.

```
SELECT model_name, mining_function, algorithm FROM user_mining_models;
 
MODEL_NAME              MINING_FUNCTION      ALGORITHM
----------------------  -------------------- ------------------------------
SVM_MODEL               CLASSIFICATION       SUPPORT_VECTOR_MACHINES
ANOMALY_DETECT_MODEL    CLASSIFICATION       SUPPORT_VECTOR_MACHINES
```

This query shows that only the SVM classification model has a target.

```
SELECT model_name, attribute_name, attribute_type, target 
       FROM user_mining_model_attributes 
       WHERE target = 'YES';
 
MODEL_NAME          ATTRIBUTE_NAME   ATTRIBUTE_TYPE     TARGET
------------------  ---------------  -----------------  ------
SVM_MODEL           AFFINITY_CARD    CATEGORICAL         YES
```

---

### DROP\_MODEL Procedure

This procedure deletes the specified mining model.

Syntax

```
DBMS_DATA_MINING.DROP_MODEL (model_name IN VARCHAR2,
                             force      IN BOOLEAN DEFAULT FALSE);
```

Parameters

Table 44-37 DROP\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the mining model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `force` | Forces the mining model to be dropped even if it is invalid. A mining model may be invalid if a serious system error interrupted the model build process. |

Usage Note

To drop a mining model, you must be the owner or you must have the `DROP ANY MINING MODEL` privilege. See [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/security.htm#DMADM004) for information about privileges for data mining.

Example

You can use the following command to delete a valid mining model named `nb_sh_clas_sample` that exists in your schema.

```
BEGIN
  DBMS_DATA_MINING.DROP_MODEL(model_name => 'nb_sh_clas_sample');
END;
/
```

---

### EXPORT\_MODEL Procedure

This procedure exports the specified data mining models to a dump file set. To import the models from the dump file set, use the IMPORT\_MODEL Procedure. `EXPORT_MODEL` and `IMPORT_MODEL` use Oracle Data Pump technology.

When Oracle Data Pump is used to export/import an entire schema or database, the mining models in the schema or database are included. However, `EXPORT_MODEL` and `IMPORT_MODEL` are the only utilities that support the export/import of individual models.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/part_dp.htm#SUTIL2877) for information about Oracle Data Pump

[Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/schemaobjs.htm#DMADM010) for more information about exporting and importing mining models

Syntax

```
DBMS_DATA_MINING.EXPORT_MODEL (
      filename          IN VARCHAR2,
      directory         IN VARCHAR2,
      model_filter      IN VARCHAR2 DEFAULT NULL,
      filesize          IN VARCHAR2 DEFAULT NULL,
      operation         IN VARCHAR2 DEFAULT NULL,
      remote_link       IN VARCHAR2 DEFAULT NULL,
      jobname           IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 44-38 EXPORT\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `filename` | Name of the dump file set to which the models should be exported. The name must be unique within the schema.  The dump file set can contain one or more files. The number of files in a dump file set is determined by the size of the models being exported (both metadata and data) and a specified or estimated maximum file size. You can specify the file size in the `filesize` parameter, or you can use the `operation` parameter to cause Oracle Data Pump to estimate the file size. If the size of the models to export is greater than the maximum file size, one or more additional files are created.  When the export operation completes successfully, the name of the dump file set is automatically expanded to `filename01.dmp`, even if there is only one file in the dump set. If there are additional files, they are named sequentially as `filename02.dmp`, `filename03.dmp`, and so forth. |
| `directory` | Name of a pre-defined directory object that specifies where the dump file set should be created.  The exporting user must have read/write privileges on the directory object and on the file system directory that it identifies.  See [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5007.htm#SQLRF01207) for information about directory objects. |
| `model_filter` | Optional parameter that specifies which model or models to export. If you do not specify a value for `model_filter`, all models in the schema are exported. You can also specify `NULL` (the default) or `'ALL'` to export all models.  You can export individual models by name and groups of models based on mining function or algorithm. For instance, you could export all regression models or all Naive Bayes models. Examples are provided in Table 44-39. |
| `filesize` | Optional parameter that specifies the maximum size of a file in the dump file set. The size may be specified in bytes, kilobytes (K), megabytes (M), or gigabytes (G). The default size is 50 MB.  If the size of the models to export is larger than `filesize`, one or more additional files are created within the dump set. See the description of the `filename` parameter for more information. |
| `operation` | Optional parameter that specifies whether or not to estimate the size of the files in the dump set. By default the size is not estimated and the value of the `filesize` parameter determines the size of the files.  You can specify either of the following values for `operation`:  - `'EXPORT'` — Export all or the specified models. (Default) - `'ESTIMATE'` — Estimate the size of the exporting models. |
| `remote_link` | Optional parameter not used in this release. Set to `NULL`. |
| `jobname` | Optional parameter that specifies the name of the export job. By default, the name has the form `username` `_exp_` `nnnn`, where `nnnn` is a number. For example, a job name in the `SCOTT` schema might be `SCOTT_exp_134`.  If you specify a job name, it must be unique within the schema. The maximum length of the job name is 30 characters.  A log file for the export job, named `jobname.log`, is created in the same directory as the dump file set. |

Usage Notes

The `model_filter` parameter specifies which models to export. You can list the models by name, or you can specify all models that have the same mining function or algorithm. You can query the `USER_MINING_MODELS` view to list the models in your schema.

```
SQL> describe user_mining_models
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 MODEL_NAME                                NOT NULL VARCHAR2(30)
 MINING_FUNCTION                                    VARCHAR2(30)
 ALGORITHM                                          VARCHAR2(30)
 CREATION_DATE                             NOT NULL DATE
 BUILD_DURATION                                     NUMBER
 MODEL_SIZE                                         NUMBER
 COMMENTS                                           VARCHAR2(4000)
```

For more information on data dictionary views of mining models, see "Mining Model Objects".

Examples of model filters are provided in Table 44-39.

Table 44-39 Sample Values for the Model Filter Parameter

| Sample Value | Meaning |
| --- | --- |
| `'mymodel'` | Export the model named `mymodel` |
| `'name= ''mymodel'''` | Export the model named `mymodel` |
| `'name IN (''mymodel2'',''mymodel3'')'` | Export the models named `mymodel2` and `mymodel3` |
| `'ALGORITHM_NAME = ''NAIVE_BAYES'''` | Export all Naive Bayes models. See Table 44-4 for a list of algorithm names. |
| `'FUNCTION_NAME =''CLASSIFICATION'''` | Export all classification models. See Table 44-2 for a list of mining functions. |

Examples

The following statement exports all the models in the `DMUSER3` schema to a dump file set called `models_out` in the directory `$ORACLE_HOME/rdbms/log`. This directory is mapped to a directory object called `DATA_PUMP_DIR`. The `DMUSER3` user has read/write access to the directory and to the directory object.

```
SQL>execute dbms_data_mining.export_model ('models_out', 'DATA_PUMP_DIR');
```

You can exit SQL\*Plus and list the resulting dump file and log file.

```
SQL>exit
>cd $ORACLE_HOME/rdbms/log
>ls
>DMUSER3_exp_1027.log  models_out01.dmp
```

The following example uses the same directory object and is executed by the same user. It exports the models called `NMF_SH_SAMPLE` and `SVMR_SH_REGR_SAMPLE` to a different dump file set in the same directory.

```
SQL>execute dbms_data_mining.export_model ( 'models2_out', 'DATA_PUMP_DIR',
            'name in (''NMF_SH_SAMPLE'', ''SVMR_SH_REGR_SAMPLE'')');
SQL>exit
>cd $ORACLE_HOME/rdbms/log
>ls
>DMUSER3_exp_1027.log  models_out01.dmp
 DMUSER3_exp_924.log  models2_out01.dmp
```

---

### GET\_ASSOCIATION\_RULES Function

This table function returns the rules from an association model.

You can specify filtering criteria to cause `GET_ASSOCIATION_RULES` to return a subset of the rules. Filtering criteria can improve the performance of the table function. If the number of rules is large, the greatest performance improvement will result from specifying the `topn` parameter.

Syntax

```
DBMS_DATA_MINING.GET_ASSOCIATION_RULES (
   model_name            IN VARCHAR2,
   topn                  IN NUMBER DEFAULT NULL,
   rule_id               IN INTEGER DEFAULT NULL,
   min_confidence        IN NUMBER DEFAULT NULL,
   min_support           IN NUMBER DEFAULT NULL,
   max_rule_length       IN INTEGER DEFAULT NULL,
   min_rule_length       IN INTEGER DEFAULT NULL,
   sort_order            IN ORA_MINING_VARCHAR2_NT DEFAULT NULL,
   antecedent_items      IN DM_ITEMS DEFAULT NULL,
   consequent_items      IN DM_ITEMS DEFAULT NULL,
   min_lift              IN NUMBER DEFAULT NULL)
 RETURN DM_RULES PIPELINED;
```

Parameters

Table 44-40 GET\_ASSOCIATION\_RULES Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used.  This is the only required parameter of `GET_ASSOCIATION_RULES`. All other parameters specify optional filters on the rules to return. |
| `topn` | Return the n top rules ordered by confidence and then support, both descending. If you specify a sort order, the top n rules are derived after the sort is performed.  If `topn` is specified and no maximum or minimum rule length is specified, then the only columns allowed in the sort order are `RULE_CONFIDENCE` and `RULE_SUPPORT`. If topn is specified and a maximum or minimum rule length is specified, then `RULE_CONFIDENCE`, `RULE_SUPPORT`, and `NUMBER_OF_ITEMS` are allowed in the sort order. |
| `rule_id` | Identifier of the rule to return. If you specify a value for `rule_id`, do not specify values for the other filtering parameters. |
| `min_confidence` | Return the rules with confidence greater than or equal to this number |
| `min_support` | Return the rules with support greater than or equal to this number |
| `max_rule_length` | Return the rules with a length less than or equal to this number.  Rule length refers to the number of items in the rule (See `NUMBER_OF_ITEMS` in Table 44-41). For example, in the rule A=>B (if A, then B), the number of items is 2.  If `max_rule_length` is specified, then the `NUMBER_OF_ITEMS` column is permitted in the sort order. |
| `min_rule_length` | Return the rules with a length greater than or equal to this number. See `max_rule_length` for a description of rule length.  If `min_rule_length` is specified, then the `NUMBER_OF_ITEMS` column is permitted in the sort order. |
| `sort_order` | Sort the rules by the values in one or more of the returned columns. Specify one or more column names, each followed by `ASC` for ascending order or `DESC` for descending order.  For example, to sort the result set in descending order first by the `NUMBER_OF_ITEMS` column, then by the `RULE_CONFIDENCE` column, you would specify:  `ORA_MINING_VARCHAR2_NT('NUMBER_OF_ITEMS DESC', 'RULE_CONFIDENCE DESC')`  If you specify `topn`, the results will vary depending on the sort order.  By default, the results are sorted by confidence in descending order, then by support in descending order.  See the examples. |
| `antecedent_items` | Return the rules with these items in the antecedent. See the examples. |
| `consequent_items` | Return the rules with this item in the consequent. See the examples. |
| `min_lift` | Return the rules with lift greater than or equal to this number. |

Return Values

Table 44-41 GET\_ASSOCIATION RULES Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_RULES` | Represents a set of rows of type `DM_RULE`. The rows have the following columns:  ``` (rule_id              INTEGER,  antecedent           DM_PREDICATES,  consequent           DM_PREDICATES,  rule_support         NUMBER,  rule_confidence      NUMBER,  rule_lift            NUMBER,  antecedent_support   NUMBER,  consequent_support   NUMBER,  number_of_items      INTEGER ) ``` |
|  | The `antecedent` and `consequent` columns each return nested tables of type `DM_PREDICATES`.The rows, of type `DM_PREDICATE`, have the following columns:  ``` (attribute_name            VARCHAR2(4000),  attribute_subname         VARCHAR2(4000),  conditional_operator      CHAR(2)/*=,<>,<,>,<=,>=*/,  attribute_num_value       NUMBER,  attribute_str_value       VARCHAR2(4000),  attribute_support         NUMBER,  attribute_confidence      NUMBER) ``` |

Usage Notes

This table function pipes out rows of type `DM_RULES`. For information on Data Mining data types and piped output from table functions, see "Data Types".

The `ORA_MINING_VARCHAR2_NT` type is defined as a table of `VARCHAR2(4000)`.

Examples

The following example demonstrates an Association model build followed by several invocations of the `GET_ASSOCIATION_RULES` table function.

```
-- prepare a settings table to override default settings
CREATE TABLE market_settings AS
SELECT *
  FROM TABLE(DBMS_DATA_MINING.GET_DEFAULT_SETTINGS)
 WHERE setting_name LIKE 'ASSO_%';
BEGIN
-- update the value of the minimum confidence
UPDATE census_settings
   SET setting_value = TO_CHAR(0.081)
 WHERE setting_name = DBMS_DATA_MINING.asso_min_confidence;

-- build an AR model 
DBMS_DATA_MINING.CREATE_MODEL(
  model_name => 'market_model',
  function => DBMS_DATA_MINING.ASSOCIATION,
  data_table_name => 'market_build',
  case_id_column_name => 'item_id',
  target_column_name => NULL,
  settings_table_name => 'census_settings');
END;
/
-- View the (unformatted) rules 
SELECT rule_id, antecedent, consequent, rule_support,
       rule_confidence
  FROM TABLE(DBMS_DATA_MINING.GET_ASSOCIATION_RULES('market_model'));
```

In the previous example, you view all rules. To view just the top 20 rules, use the following statement.

```
-- View the top 20 (unformatted) rules
SELECT rule_id, antecedent, consequent, rule_support,
       rule_confidence
  FROM TABLE(DBMS_DATA_MINING.GET_ASSOCIATION_RULES('market_model', 20));
```

The following query uses the association model `AR_SH_SAMPLE`, which is created from one of the Oracle Data Mining sample programs. (See [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009) for information about the sample programs.)

```
SELECT * FROM TABLE (
   DBMS_DATA_MINING.GET_ASSOCIATION_RULES (
      'AR_SH_SAMPLE', 10, NULL, 0.5, 0.01, 2, 1,
         ORA_MINING_VARCHAR2_NT (
         'NUMBER_OF_ITEMS DESC', 'RULE_CONFIDENCE DESC', 'RULE_SUPPORT DESC'),
         DM_ITEMS(DM_ITEM('CUSTPRODS', 'Mouse Pad', 1, NULL), 
                  DM_ITEM('CUSTPRODS', 'Standard Mouse', 1, NULL)),
         DM_ITEMS(DM_ITEM('CUSTPRODS', 'Extension Cable', 1, NULL))));
```

The query returns three rules, shown as follows.

```
13  DM_PREDICATES(
       DM_PREDICATE('CUSTPRODS', 'Mouse Pad', '= ', 1, NULL, NULL, NULL), 
       DM_PREDICATE('CUSTPRODS', 'Standard Mouse', '= ', 1, NULL, NULL, NULL))
    DM_PREDICATES(
       DM_PREDICATE('CUSTPRODS', 'Extension Cable', '= ', 1, NULL, NULL, NULL))
    .15532      .84393   2.7075     .18404     .3117   2
 
11  DM_PREDICATES(
       DM_PREDICATE('CUSTPRODS', 'Standard Mouse', '= ', 1, NULL, NULL, NULL))
    DM_PREDICATES(
       DM_PREDICATE('CUSTPRODS', 'Extension Cable', '= ', 1, NULL, NULL, NULL))
    .18085      .56291   1.8059     .32128     .3117   1
 
9   DM_PREDICATES(
       DM_PREDICATE('CUSTPRODS', 'Mouse Pad', '= ', 1, NULL, NULL, NULL))
    DM_PREDICATES(
       DM_PREDICATE('CUSTPRODS', 'Extension Cable', '= ', 1, NULL, NULL, NULL))
      .17766    .55116   1.7682     .32234     .3117   1
```

---

### GET\_DEFAULT\_SETTINGS Function

The `GET_DEFAULT_SETTINGS` function was deprecated in Oracle Data Mining 11g Release 1 (11.1). It was replaced with the data dictionary view \* `_MINING_MODEL_SETTINGS`. `USER_`, `ALL_`, and `DBA_` versions of the view are available. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG016).

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

Note:

See "Deprecated Subprograms"

This table function returns the default settings for all mining functions and algorithms supported in the `DBMS_DATA_MINING` package.

Syntax

```
DBMS_DATA_MINING.GET_DEFAULT_SETTINGS
  RETURN DM_MODEL_SETTINGS PIPELINED;
```

Return Values

Table 44-42 GET\_DEFAULT\_SETTINGS Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_MODEL_SETTINGS` | Represents a set of rows of type `DM_MODEL_SETTING`. The rows have the following columns:  ``` (setting_name    VARCHAR2(30),  setting_value   VARCHAR2(128)) ``` |

Usage Notes

This table function pipes out rows of type `DM_MODEL_SETTING`. For information on Data Mining data types and piped output from table functions, see "Data Types".

This function is particularly useful if you do not know what settings are associated with a particular function or algorithm, and you want to override some or all of them.

Examples

For example, if you want to override some or all of k-Means clustering settings, you can create a settings table as shown, and update individual settings as required.

```
BEGIN
  CREATE TABLE mysettings AS
  SELECT * 
  FROM TABLE(DBMS_DATA_MINING.GET_DEFAULT_SETTINGS)
   WHERE setting_name LIKE 'KMNS%';
  -- now update individual settings as required
  UPDATE mysettings
     SET setting_value = 0.02
   WHERE setting_name = DBMS_DATA_MINING.KMNS_MIN_PCT_ATTR_SUPPORT;
END;
/
```

---

### GET\_FREQUENT\_ITEMSETS Function

This table function returns a set of rows that represent the frequent itemsets from an Association model. For a detailed description of frequent itemsets, consult [Oracle Data Mining Concepts](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/toc.htm).

Syntax

```
DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS (
    model_name          IN VARCHAR2,
    topn                IN NUMBER DEFAULT NULL,
    max_itemset_length  IN NUMBER DEFAULT NULL)
  RETURN DM_ITEMSETS PIPELINED;
```

Parameters

Table 44-43 GET\_FREQUENT\_ITEMSETS Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `topn` | When not `NULL`, return the top n rows ordered by support in descending order |
| `max_itemset_length` | Maximum length of an item set. |

Return Values

Table 44-44 GET\_FREQUENT\_ITEMSETS Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_ITEMSETS` | Represents a set of rows of type `DM_ITEMSET`. The rows have the following columns:  ``` (itemsets_id      NUMBER, items             DM_ITEMS, support           NUMBER, number_of_items   NUMBER) ```  The `items` column returns a nested table of type `DM_ITEMS`. The rows have type `DM_ITEM`:  ``` (attribute_name      VARCHAR2(4000), attribute_subname    VARCHAR2(4000), attribute_num_value  NUMBER, attribute_str_value  VARCHAR2(4000)) ``` |

Usage Notes

This table function pipes out rows of type `DM_ITEMSETS`. For information on Data Mining data types and piped output from table functions, see "Data Types".

Examples

The following example demonstrates an Association model build followed by an invocation of `GET_FREQUENT_ITEMSETS` table function from Oracle SQL.

```
-- prepare a settings table to override default settings
CREATE TABLE market_settings AS
```
```
SELECT *
```
```
FROM TABLE(DBMS_DATA_MINING.GET_DEFAULT_SETTINGS)
 WHERE setting_name LIKE 'ASSO_%';
BEGIN
-- update the value of the minimum confidence
UPDATE market_settings
   SET setting_value = TO_CHAR(0.081)
 WHERE setting_name = DBMS_DATA_MINING.asso_min_confidence;

/* build a AR model */
DBMS_DATA_MINING.CREATE_MODEL(
  model_name           => 'market_model',
  function             => DBMS_DATA_MINING.ASSOCIATION,
  data_table_name      => 'market_build',
  case_id_column_name  => 'item_id',
  target_column_name   => NULL,
  settings_table_name  => 'census_settings');
END;
/

-- View the (unformatted) Itemsets from SQL*Plus
SELECT itemset_id, items, support, number_of_items
  FROM TABLE(DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS('market_model'));
```

In the example above, you view all itemsets. To view just the top 20 itemsets, use the following statement:

```
-- View the top 20 (unformatted) Itemsets from SQL*Plus
SELECT itemset_id, items, support, number_of_items
  FROM TABLE(DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS('market_model', 20));
```

---

### GET\_MODEL\_COST\_MATRIX Function

This function returns the rows of the default scoring matrix associated with the specified model.

By default, this function returns the scoring matrix that was added to the model with the `ADD_COST_MATRIX` procedure. If you wish to obtain the cost matrix used to create a model, specify `cost_matrix_type_create` as the `matrix_type`. See Table 44-45.

See also ADD\_COST\_MATRIX Procedure.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_COST_MATRIX (
      model_name        IN VARCHAR2,
      matrix_type       IN VARCHAR2 DEFAULT cost_matrix_type_score)
RETURN DM_COST_MATRIX PIPELINED;
```

Parameters

Table 44-45 GET\_MODEL\_COST\_MATRIX Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `matrix_type` | The type of cost matrix.  `COST_MATRIX_TYPE_SCORE` — cost matrix used for scoring. (Default.)  `COST_MATRIX_TYPE_CREATE` — cost matrix used to create the model (Decision Tree only). |

Return Values

Table 44-46 GET\_MODEL\_COST\_MATRIX Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_COST_MATRIX` | Represents a set of rows of type `DM_COST_ELEMENT`. The rows have the following columns:  ``` actual          VARCHAR2(4000), predicted       VARCHAR2(4000), cost            NUMBER) ``` |

Usage Notes

Only Decision Tree models can be built with a cost matrix. If you want to build a Decision Tree model with a cost matrix, specify the cost matrix table name in the `CLAS_COST_TABLE_NAME` setting in the settings table for the model. See Table 44-7, "Mining Function Settings".

The cost matrix used to create a Decision Tree model becomes the default scoring matrix for the model. If you want to specify different costs for scoring, you can modify the values in the cost matrix table or you can use the `REMOVE_COST_MATRIX` procedure to remove the cost matrix and the `ADD_COST_MATRIX` procedure to add a new one

Example

This example returns the scoring cost matrix associated with the Naive Bayes model `NB_SH_CLAS_SAMPLE`.

```
column actual format a10
column predicted format a10
SELECT *
    FROM TABLE(dbms_data_mining.get_model_cost_matrix('nb_sh_clas_sample'))
    ORDER BY predicted, actual;
 
ACTUAL     PREDICTED   COST
---------- ---------- -----
0          0            .00
1          0            .75
0          1            .25
1          1            .00
```

---

### GET\_MODEL\_DETAILS\_ABN Function

The Adaptive Bayes Network algorithm `ABN` algorithm was deprecated in Oracle Data Mining 11g Release 1 (11.1).

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

Note:

See "Deprecated Subprograms"

This table function returns a set of rows that provide the details of an Adaptive Bayes Network model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_ABN (
    model_name         IN VARCHAR2)
  RETURN DM_ABN_DETAILS PIPELINED;
```

Parameters

Table 44-47 GET\_MODEL\_DETAILS\_ABN Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-48 GET\_MODEL\_DETAILS\_ABN Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_ABN_DETAILS` | Represents a set of rows of type `DM_ABN_DETAIL`. The rows have the following columns:  ``` (rule_id           INTEGER,  antecedent        DM_PREDICATES,  consequent        DM_PREDICATES,  rule_support      NUMBER) ``` |
|  | The `antecedent` and `consequent` columns of `DM_ABN_DETAIL` each return nested tables of type `DM_PREDICATES`. The rows, of type `DM_PREDICATE`, have the following columns:  ``` (attribute_name          VARCHAR2(4000),  attribute_subname       VARCHAR2(4000),  conditional_operator    CHAR(2), /*=,<>,<,>,<=,>=*/  attribute_num_value     NUMBER,  attribute_str_value     VARCHAR2(4000),  attribute_support       NUMBER,  attribute_confidence    NUMBER) ``` |

Usage Notes

This table function pipes out rows of type `DM_ABN_DETAIL`. For information on Data Mining data types and piped output from table functions, see "Data Types".

This function returns details only for a single feature ABN model.

Examples

The following example demonstrates an ABN model build followed by an invocation of `GET_MODEL_DETAILS_ABN` table function from Oracle SQL.

```
BEGIN
  -- prepare a settings table to override default algorithm and model type
  CREATE TABLE abn_settings (setting_name VARCHAR2(30),
  setting_value 
VARCHAR2(128));
  INSERT INTO abn_settings VALUES (DBMS_DATA_MINING.ALGO_NAME,
    DBMS_DATA_MINING.ALGO_ADAPTIVE_BAYES_NETWORK);
  INSERT INTO abn_settings VALUES    (DBMS_DATA_MINING.ABNS_MODEL_TYPE,     DBMS_DATA_MINING.ABNS_SINGLE_FEATURE);
   COMMIT;
  -- create a model
  DBMS_DATA_MINING.CREATE_MODEL (
    model_name           => 'abn_model',
    function             => DBMS_DATA_MINING.CLASSIFICATION,
    data_table_name      => 'abn_build',
    case_id_column_name  => 'id',
    target_column_name   => NULL,
    settings_table_name  => 'abn_settings');
END;
/
-- View the (unformatted) results from SQL*Plus
SELECT *
    FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_ABN('abn_model'));
```

---

### GET\_MODEL\_DETAILS\_AI Function

This table function returns a set of rows that provide the details of an Attribute Importance model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_AI (
  model_name         IN VARCHAR2)
 RETURN DM_RANKED_ATTRIBUTES PIPELINED;
```

Parameters

Table 44-49 GET\_MODEL\_DETAILS\_AI Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-50 GET\_MODEL\_DETAILS\_AI Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_RANKED_ATTRIBUTES` | Represents a set of rows of type `DM_RANKED_ATTRIBUTE`. The rows have the following columns:  ``` (attribute_name          VARCHAR2(4000,  attribute_subname       VARCHAR2(4000),  importance_value        NUMBER,  rank                    NUMBER(38)) ``` |

Examples

The following example returns model details for the attribute importance model `AI_SH_sample`, which was created by the sample program `dmaidemo.sql`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

```
SELECT attribute_name, importance_value, rank
    FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_AI('AI_SH_sample'))
    ORDER BY RANK;
 
ATTRIBUTE_NAME                           IMPORTANCE_VALUE       RANK
---------------------------------------- ---------------- ----------
HOUSEHOLD_SIZE                                 .151685183          1
CUST_MARITAL_STATUS                            .145294546          2
YRS_RESIDENCE                                   .07838928          3
AGE                                            .075027496          4
Y_BOX_GAMES                                    .063039952          5
EDUCATION                                      .059605314          6
HOME_THEATER_PACKAGE                           .056458722          7
OCCUPATION                                     .054652937          8
CUST_GENDER                                    .035264741          9
BOOKKEEPING_APPLICATION                        .019204751         10
PRINTER_SUPPLIES                                        0         11
OS_DOC_SET_KANJI                               -.00050013         12
FLAT_PANEL_MONITOR                             -.00509564         13
BULK_PACK_DISKETTES                            -.00540822         14
COUNTRY_NAME                                   -.01201116         15
CUST_INCOME_LEVEL                              -.03951311         16
```

---

### GET\_MODEL\_DETAILS\_GLM Function

This table function returns the coefficient statistics for a Generalized Linear Model.

The same set of statistics is returned for both linear and logistic regression, but statistics that do not apply to the mining function are returned as `NULL`. For more details, see the Usage Notes.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_GLM (
             model_name             VARCHAR2)
RETURN DM_GLM_COEFF_SET PIPELINED;
```

Parameters

Table 44-51 GET\_MODEL\_DETAILS\_GLM Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-52 GET\_MODEL\_DETAILS\_GLM Return Values

| Return Value | Description |
| --- | --- |
| `DM_GLM_COEFF_SET` | Represents a set of rows of type `DM_GLM_COEFF`. The rows have the following columns:  ``` (class                   VARCHAR2(4000),  attribute_name          VARCHAR2(4000),  attribute_subname       VARCHAR2(4000),  attribute_value         VARCHAR2(4000),  coefficient             NUMBER,  std_error               NUMBER,  test_statistic          NUMBER,  p_value                 NUMBER,  VIF                     NUMBER,  std_coefficient         NUMBER,  lower_coeff_limit       NUMBER,  upper_coeff_limit       NUMBER,  exp_coefficient         BINARY_DOUBLE,  exp_lower_coeff_limit   BINARY_DOUBLE,  exp_upper_coeff_limit   BINARY_DOUBLE) ``` |

`GET_MODEL_DETAILS_GLM` returns a row of statistics for each attribute and one extra row for the intercept, which is identified by a null value in the attribute name. Each row has the `DM_GLM_COEFF` data type. The statistics are described in Table 44-53.

Table 44-53 DM\_GLM\_COEFF Data Type Description

| Column | Description |
| --- | --- |
| `class` | The non-reference target class for logistic regression. The model is built to predict the probability of this class.  The other class (the reference class) is specified in the model setting `GLMS_REFERENCE_CLASS_NAME`. See Table 44-11, "GLM Settings".  For linear regression, `class` is null. |
| `attribute_name` | The attribute name when there is no subname, or first part of the attribute name when there is a subname. The value of `attribute_name` is also the name of the column in the case table that is the source for this attribute.  For the intercept, `attribute_name` is null. Intercepts are equivalent to the bias term in SVM models. |
| `attribute_subname` | The name of an attribute in a nested table. The full name of a nested attribute has the form:  `attribute_name.attribute_subname`  where `attribute_name` is the name of the nested column in the case table that is the source for this attribute.  If the attribute is not nested, `attribute_subname` is null. If the attribute is an intercept, both the `attribute_name` and the `attribute_subname` are null. |
| `attribute_value` | The value of the attribute (categorical attribute only).  For numerical attributes, `attribute_value` is null. |
| `coefficient` | The linear coefficient estimate. |
| `std_error` | Standard error of the coefficient estimate. |
| `test_statistic` | For linear regression, the t-value of the coefficient estimate.  For logistic regression, the Wald chi-square value of the coefficient estimate. |
| `p-value` | Probability of the `test_statistic`. Used to analyze the significance of specific attributes in the model. |
| `VIF` | Variance Inflation Factor. The value is zero for the intercept. For logistic regression, `VIF` is null. |
| `std_coefficient` | Standardized estimate of the coefficient. |
| `lower_coeff_limit` | Lower confidence bound of the coefficient. |
| `upper_coeff_limit` | Upper confidence bound of the coefficient. |
| `exp_coefficient` | Exponentiated coefficient for logistic regression. For linear regression, `exp_coefficient` is null. |
| `exp_lower_coeff_limit` | Exponentiated coefficient for lower confidence bound of the coefficient for logistic regression. For linear regression, `exp_lower_coeff_limit` is null. |
| `exp_upper_coeff_limit` | Exponentiated coefficient for upper confidence bound of the coefficient for logistic regression. For linear regression, `exp_lower_coeff_limit` is null. |

Usage Notes

Not all statistics are necessarily returned for each coefficient. Statistics will be null if:

- They do not apply to the mining function. For example, `exp_coefficient` does not apply to linear regression.
- They cannot be computed from a theoretical standpoint. For example, when ridge regression is enabled, the coefficient values are returned with no statistics except VIF if it is enabled. (For information on ridge regression, see Table 44-11, "GLM Settings".)
- They cannot be computed because of limitations in system resources.
- Their values would be infinity.

Examples

The following example returns some of the model details for the GLM regression model `GLMR_SH_Regr_sample`, which was created by the sample program `dmglrdem.sql`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

```
SQL> SELECT *
   FROM (SELECT class, attribute_name, attribute_value, coefficient, std_error
              FROM TABLE(dbms_data_mining.get_model_details_glm(
                           'GLMR_SH_Regr_sample'))
            ORDER BY class, attribute_name, attribute_value)
     WHERE ROWNUM < 11;

CLASS     ATTRIBUTE_NAME      ATTRIBUTE_VALUE  COEFFICIENT  STD_ERROR
--------- ------------------  ---------------- -----------  ----------
          AFFINITY_CARD                         -.60686139   .531250033
          BULK_PACK_DISKETTES                   -1.9729645   .924531227
          COUNTRY_NAME        Argentina         -1.3340963  1.1942193
          COUNTRY_NAME        Australia           -.340504  5.13688361
          COUNTRY_NAME        Brazil             5.3855269  1.93197882
          COUNTRY_NAME        Canada            4.13393291  2.41283125
          COUNTRY_NAME        China              .74409259  3.59923638
          COUNTRY_NAME        Denmark           -2.5287879  3.18569293
          COUNTRY_NAME        France            -1.0908689  7.18471003
          COUNTRY_NAME        Germany           -1.7472166  2.53689456
```

---

### GET\_MODEL\_DETAILS\_GLOBAL Function

This table function returns statistics about the model as a whole. Global details are available for GLM and for association rules.

Separate global details are returned for linear and logistic regression. When ridge regression is enabled, fewer global details are returned. For information about ridge, see Table 44-11, "GLM Settings".

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_GLOBAL (
      model_name     IN  VARCHAR2)
RETURN DM_MODEL_GLOBAL_DETAILS PIPELINED;
```

Parameters

Table 44-54 GET\_MODEL\_DETAILS\_GLOBAL Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-55 GET\_MODEL\_DETAILS\_GLOBAL Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_MODEL_GLOBAL_DETAILS` | A collection of rows of type `DM_MODEL_GLOBAL_DETAIL`. The rows have the following columns:  ``` (global_detail_name   VARCHAR2(30),  global_detail_value   NUMBER) ``` |

Global Details for GLM: Linear Regression

Table 44-56 Global Details for Linear Regression

| GLOBAL\_DETAIL\_NAME | Description |
| --- | --- |
| `MODEL_DF` | Model degrees of freedom |
| `MODEL_SUM_SQUARES` | Model sum of squares |
| `MODEL_MEAN_SQUARE` | Model mean square |
| `F_VALUE` | Model F value statistic |
| `MODEL_F_P_VALUE` | Model F value probability |
| `ERROR_DF` | Error degrees of freedom |
| `ERROR_SUM_SQUARES` | Error sum of squares |
| `ERROR_MEAN_SQUARE` | Error mean square |
| `CORRECTED_TOTAL_DF` | Corrected total degrees of freedom |
| `CORRECTED_TOT_SS` | Corrected total sum of squares |
| `ROOT_MEAN_SQ` | Root mean square error |
| `DEPENDENT_MEAN` | Dependent mean |
| `COEFF_VAR` | Coefficient of variation |
| `R_SQ` | R-Square |
| `ADJUSTED_R_SQUARE` | Adjusted R-Square |
| `AIC` | Akaike's information criterion |
| `SBIC` | Schwarz's Bayesian information criterion |
| `GMSEP` | Estimated mean square error of the prediction, assuming multivariate normality |
| `HOCKING_SP` | Hocking Sp statistic |
| `J_P` | JP statistic (the final prediction error) |
| `NUM_PARAMS` | Number of parameters (the number of coefficients, including the intercept) |
| `NUM_ROWS` | Number of rows |
| `MODEL_CONVERGED` | Whether or not the model converged. Value is `1` if it converged, or `0` if it did not converge |
| `VALID_COVARIANCE_MATRIX` | Valid covariance matrix. Value is `1` if the covariance matrix was computed, or `0` if it was not computed |

Global Details for GLM: Logistic Regression

Table 44-57 Global Details for Logistic Regression

| GLOBAL\_DETAIL\_NAME | Description |
| --- | --- |
| `AIC_INTERCEPT` | Akaike's criterion for the fit of the intercept only model |
| `AIC_MODEL` | Akaike's criterion for the fit of the intercept and the covariates (predictors) mode |
| `SC_INTERCEPT` | Schwarz's Criterion for the fit of the intercept only model |
| `SC_MODEL` | Schwarz's Criterion for the fit of the intercept and the covariates (predictors) model |
| `NEG2_LL_INTERCEPT` | \-2 log likelihood of the intercept only model |
| `NEG2_LL_MODEL` | \-2 log likelihood of the model |
| `LR_DF` | Likelihood ratio degrees of freedom |
| `LR_CHI_SQ` | Likelihood ratio chi-square value |
| `LR_CHI_SQ_P_VALUE` | Likelihood ratio chi-square probability value |
| `PSEUDO_R_SQ_CS` | Pseudo R-square Cox and Snell |
| `PSEUDO_R_SQ_N` | Pseudo R-square Nagelkerke |
| `DEPENDENT_MEAN` | Dependent mean |
| `PCT_CORRECT` | Percent of correct predictions |
| `PCT_INCORRECT` | Percent of incorrectly predicted rows |
| `PCT_TIED` | Percent of cases where probability for both cases is the same |
| `NUM_PARAMS` | Number of parameters (the number of coefficients, including the intercept) |
| `NUM_ROWS` | Number of rows |
| `MODEL_CONVERGED` | Whether or not the model converged. Value is `1` if it converged, or `0` if it did not converge. |
| `VALID_COVARIANCE_MATRIX` | Valid covariance matrix. Value is `1` if the covariance matrix was computed, or `0` if the covariance matrix not computed |

Global Detail for Association Rules

A single global detail is produced by an Association model.

Table 44-58 Global Detail for Association Rules

| GLOBAL\_DETAIL\_NAME | Description |
| --- | --- |
| `RULE_COUNT` | The number of association rules in the model. |

Examples

The following example returns the global model details for the GLM regression model `GLMR_SH_Regr_sample`, which was created by the sample program `dmglrdem.sql`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

```
SELECT *
  FROM TABLE(dbms_data_mining.get_model_details_global(
              'GLMR_SH_Regr_sample'))
ORDER BY global_detail_name;
GLOBAL_DETAIL_NAME             GLOBAL_DETAIL_VALUE
------------------------------ -------------------
ADJUSTED_R_SQUARE                       .731412557
AIC                                       5931.814
COEFF_VAR                               18.1711243
CORRECTED_TOTAL_DF                            1499
CORRECTED_TOT_SS                        278740.504
DEPENDENT_MEAN                              38.892
ERROR_DF                                      1433
ERROR_MEAN_SQUARE                       49.9440956
ERROR_SUM_SQUARES                       71569.8891
F_VALUE                                 62.8492452
GMSEP                                    52.280819
HOCKING_SP                              .034877162
J_P                                     52.1749319
MODEL_CONVERGED                                  1
MODEL_DF                                        66
MODEL_F_P_VALUE                                  0
MODEL_MEAN_SQUARE                       3138.94871
MODEL_SUM_SQUARES                       207170.615
NUM_PARAMS                                      67
NUM_ROWS                                      1500
ROOT_MEAN_SQ                            7.06711367
R_SQ                                    .743238288
SBIC                                    6287.79977
VALID_COVARIANCE_MATRIX                          1
```

---

### GET\_MODEL\_DETAILS\_KM Function

This table function returns a set of rows that provide the details of a k-Means clustering model.

You can provide input to `GET_MODEL_DETAILS_KM` to request specific information about the model, thus improving the performance of the query. If you do not specify filtering parameters, `GET_MODEL_DETAILS_KM` returns all the information about the model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_KM (
          model_name          VARCHAR2,
          cluster_id          NUMBER    DEFAULT NULL,
          attribute           VARCHAR2  DEFAULT NULL,
          centroid            NUMBER    DEFAULT 1, 
          histogram           NUMBER    DEFAULT 1, 
          rules               NUMBER    DEFAULT 2,
          attribute_subname   VARCHAR2  DEFAULT NULL)
RETURN DM_CLUSTERS PIPELINED;
```

Parameters

Table 44-59 GET\_MODEL\_DETAILS\_KM Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `cluster_id` | The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise the details for all clusters are returned. |
| `attribute` | The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise the details for all attributes are returned |
| `centroid` | This parameter accepts the following values:  - 1 — Details about centroids are returned (default) - 0 — Details about centroids are not returned |
| `histogram` | This parameter accepts the following values:  - 1 — Details about histograms are returned (default) - 0 — Details about histograms are not returned |
| `rules` | This parameter accepts the following values:  - 2 — Details about rules are returned (default) - 1 — Rule summaries are returned - 0 — No information about rules is returned |

Return Values

Table 44-60 GET\_MODEL\_DETAILS\_KM Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_CLUSTERS` | Represents a set of rows of type `DM_CLUSTER`. The rows have the following columns:  ``` (id                   NUMBER,  cluster_id           VARCHAR2(4000),  record_count         NUMBER,  parent               NUMBER,  tree_level           NUMBER,  dispersion           NUMBER,  split_predicate      DM_PREDICATES,  child                DM_CHILDREN,  centroid             DM_CENTROIDS,  histogram            DM_HISTOGRAMS,  rule                 DM_RULE) ``` |
|  | The `split_predicate` column of `DM_CLUSTER` returns a nested table of type `DM_PREDICATES`. Each row, of type `DM_PREDICATE`, has the following columns:  ``` (attribute_name           VARCHAR2(4000),  attribute_subname        VARCHAR2(4000),  conditional_operator     CHAR(2) /*=,<>,<,>,<=,>=*/,  attribute_num_value      NUMBER,  attribute_str_value      VARCHAR2(4000),  attribute_support        NUMBER,  attribute_confidence     NUMBER) ``` |
|  | The `child` column of `DM_CLUSTER` returns a nested table of type `DM_CHILDREN`. The rows, of type `DM_CHILD`, have a single column of type `NUMBER`, which contains the identifiers of each child. |
|  | The `centroid` column of `DM_CLUSTER` returns a nested table of type `DM_CENTROIDS`. The rows, of type `DM_CENTROID`, have the following columns:  ``` (attribute_name    VARCHAR2(4000),  attribute_subname  VARCHAR2(4000),  mean               NUMBER,  mode_value         VARCHAR2(4000),  variance           NUMBER) ``` |
|  | The `histogram` column of `DM_CLUSTER` returns a nested table of type `DM_HISTOGRAMS`. The rows, of type `DM_HISTOGRAM_BIN`, have the following columns:  ``` (attribute_name    VARCHAR2(4000),  attribute_subname  VARCHAR2(4000),  bin_id             NUMBER,  lower_bound        NUMBER,  upper_bound        NUMBER,  label              VARCHAR2(4000),  count              NUMBER) ``` |
|  | The `rule` column of `DM_CLUSTER` returns a single row of type `DM_RULE`. The columns are:  ``` (rule_id            INTEGER,  antecedent         DM_PREDICATES,  consequent         DM_PREDICATES,  rule_support       NUMBER,  rule_confidence    NUMBER,  rule_lift          NUMBER,  antecedent_support NUMBER,  consequent_support NUMBER,  number_of_items    INTEGER) ``` |
|  | The `antecedent` and `consequent` columns of `DM_RULE` each return nested tables of type `DM_PREDICATES`. The rows, of type `DM_PREDICATE`, have the following columns:  ``` (attribute_name           VARCHAR2(4000),  attribute_subname  VARCHAR2(4000),  conditional_operator     CHAR(2)/*=,<>,<,>,<=,>=*/,  attribute_num_value      NUMBER,  attribute_str_value      VARCHAR2(4000),  attribute_support        NUMBER,  attribute_confidence     NUMBER) ``` |

Usage Notes

The table function pipes out rows of type `DM_CLUSTERS`. For information on Data Mining data types and piped output from table functions, see "Data Types".

Examples

The following example returns model details for the k-Means clustering model `KM_SH_Clus_sample`, which was created by the sample program `dmkmdemo.sql`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

```
SELECT T.id           clu_id,
       T.record_count rec_cnt,
       T.parent       parent,
       T.tree_level   tree_level,
       T.dispersion   dispersion
  FROM (SELECT *
          FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_KM(
                     'KM_SH_Clus_sample'))
        ORDER BY id) T
 WHERE ROWNUM < 6;  
 
    CLU_ID    REC_CNT     PARENT TREE_LEVEL DISPERSION
---------- ---------- ---------- ---------- ----------
         1       1500                     1  5.9152211
         2        638          1          2 3.98458982
         3        862          1          2 5.83732097
         4        376          3          3 5.05192137
         5        486          3          3 5.42901522
```

---

### GET\_MODEL\_DETAILS\_NB Function

This table function returns a set of rows that provide the details of a Naive Bayes model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_NB (
   model_name      IN       VARCHAR2)
 RETURN DM_NB_DETAILS PIPELINED;
```

Parameters

Table 44-61 GET\_MODEL\_DETAILS\_NB Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-62 GET\_MODEL\_DETAILS\_NB Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_NB_DETAILS` | Represents a set of rows of type `DM_NB_DETAIL`. The rows have the following columns:  ``` (target_attribute_name          VARCHAR2(30),  target_attribute_str_value     VARCHAR2(4000),  target_attribute_num_value     NUMBER,  prior_probability              NUMBER,  conditionals                   DM_CONDITIONALS) ``` |
|  | The `conditionals` column of `DM_NB_DETAIL` returns a nested table of type `DM_CONDITIONALS`. The rows, of type `DM_CONDITIONAL`, have the following columns:  ``` (attribute_name             VARCHAR2(4000),  attribute_subname          VARCHAR2(4000),  attribute_str_value        VARCHAR2(4000),  attribute_num_value        NUMBER,  conditional_probability    NUMBER) ``` |

Usage Notes

The table function pipes out rows of type `DM_NB_DETAILS`. For information on Data Mining data types and piped output from table functions, see "Data Types".

Examples

The following query is from the sample program `dmnbdemo.sql`. It returns model details about the model `NB_SH_Clas_sample`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

The query creates labels from the bin boundary tables that were used to bin the training data. It replaces the attribute values with the labels. For numeric bins, the labels are `(``lower_boundary`,`upper_boundary``]`; for categorical bins, the label matches the value it represents. (This method of categorical label representation will only work for cases where one value corresponds to one bin.) The target was not binned.

```
WITH
    bin_label_view AS (
    SELECT col, bin, (DECODE(bin,'1','[','(') || lv || ',' || val || ']') label
      FROM (SELECT col,
                   bin,
                   LAST_VALUE(val) OVER (
                   PARTITION BY col ORDER BY val
                   ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) lv,
                   val
             FROM nb_sh_sample_num)
   UNION ALL
   SELECT col, bin, val label
     FROM nb_sh_sample_cat
   ),
   model_details AS (
   SELECT T.target_attribute_name                                        tname,
          TO_CHAR(
          NVL(T.target_attribute_num_value,T.target_attribute_str_value)) tval,
          C.attribute_name                                               pname,
          NVL(L.label, NVL(C.attribute_str_value, C.attribute_num_value)) pval,
          T.prior_probability                                           priorp,
          C.conditional_probability                                      condp
     FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_NB('NB_SH_Clas_sample')) T,
          TABLE(T.conditionals) C,
          bin_label_view L
    WHERE C.attribute_name = L.col (+) AND
          (NVL(C.attribute_str_value,C.attribute_num_value) = L.bin(+))
   ORDER BY 1,2,3,4,5,6
   )
   SELECT tname, tval, pname, pval, priorp, condp
     FROM model_details
    WHERE ROWNUM < 11;

TNAME          TVAL PNAME                     PVAL           PRIORP   CONDP
-------------- ---- ------------------------- ------------- ------- -------
AFFINITY_CARD  0    AGE                       (24,30]         .6500   .1714
AFFINITY_CARD  0    AGE                       (30,35]         .6500   .1509
AFFINITY_CARD  0    AGE                       (35,40]         .6500   .1125
AFFINITY_CARD  0    AGE                       (40,46]         .6500   .1134
AFFINITY_CARD  0    AGE                       (46,53]         .6500   .1071
AFFINITY_CARD  0    AGE                       (53,90]         .6500   .1312
AFFINITY_CARD  0    AGE                       [17,24]         .6500   .2134
AFFINITY_CARD  0    BOOKKEEPING_APPLICATION   0               .6500   .1500
AFFINITY_CARD  0    BOOKKEEPING_APPLICATION   1               .6500   .8500
AFFINITY_CARD  0    BULK_PACK_DISKETTES       0               .6500   .3670
```

---

### GET\_MODEL\_DETAILS\_NMF Function

This table function returns a set of rows that provide the details of a Non-Negative Matrix Factorization model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_NMF (
   model_name        IN        VARCHAR2)
 RETURN DM_NMF_FEATURE_SET PIPELINED;
```

Parameters

Table 44-63 GET\_MODEL\_DETAILS\_NMF Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-64 GET\_MODEL\_DETAILS\_NMF Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_NMF_FEATURE_SET` | Represents a set of rows of `DM_NMF_FEATURE`. The rows have the following columns:  ``` (feature_id          NUMBER,  mapped_feature_id   VARCHAR2(4000),  attribute_set       DM_NMF_ATTRIBUTE_SET) ``` |
|  | The `attribute_set` column of `DM_NMF_FEATURE` returns a nested table of type `DM_NMF_ATTRIBUTE_SET`. The rows, of type `DM_NMF_ATTRIBUTE`, have the following columns:  ``` (attribute_name    VARCHAR2(4000),  attribute_subname  VARCHAR2(4000),  attribute_value    VARCHAR2(4000),  coefficient        NUMBER) ``` |

Usage Notes

The table function pipes out rows of type `DM_NMF_FEATURE_SET`. For information on Data Mining data types and piped output from table functions, see "Data Types".

Examples

The following example returns model details for the feature extraction model `NMF_SH_Sample`, which was created by the sample program `dmnmdemo.sql`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

```
SELECT * FROM (
SELECT F.feature_id,
       A.attribute_name,
       A.attribute_value,
       A.coefficient
  FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_NMF('NMF_SH_Sample')) F,
       TABLE(F.attribute_set) A
ORDER BY feature_id,attribute_name,attribute_value
) WHERE ROWNUM < 11; 
 
FEATURE_ID ATTRIBUTE_NAME          ATTRIBUTE_VALUE          COEFFICIENT
--------- -----------------------  ---------------- -------------------
        1 AFFINITY_CARD                                 .051208078859308
        1 AGE                                          .0390513260041573
        1 BOOKKEEPING_APPLICATION                      .0512734004239326
        1 BULK_PACK_DISKETTES                           .232471260895683
        1 COUNTRY_NAME             Argentina          .00766817464479959
        1 COUNTRY_NAME             Australia         .000157637881096675
        1 COUNTRY_NAME             Brazil              .0031409632415604
        1 COUNTRY_NAME             Canada             .00144213099311427
        1 COUNTRY_NAME             China             .000102279310968754
        1 COUNTRY_NAME             Denmark           .000242424084307513
```

---

### GET\_MODEL\_DETAILS\_OC Function

This table function returns a set of rows that provide the details of an O-Cluster clustering model. The rows are an enumeration of the clustering patterns generated during the creation of the model.

You can provide input to `GET_MODEL_DETAILS_OC` to request specific information about the model, thus improving the performance of the query. If you do not specify filtering parameters, `GET_MODEL_DETAILS_OC` returns all the information about the model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_OC (
          model_name         VARCHAR2,
          cluster_id         NUMBER    DEFAULT NULL,
          attribute          VARCHAR2  DEFAULT NULL,
          centroid           NUMBER    DEFAULT 1, 
          histogram          NUMBER    DEFAULT 1, 
          rules              NUMBER    DEFAULT 2)
RETURN DM_CLUSTERS PIPELINED;
```

Parameters

Table 44-65 GET\_MODEL\_DETAILS\_OC Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `cluster_id` | The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise the details for all clusters are returned. |
| `attribute` | The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise the details for all attributes are returned |
| `centroid` | This parameter accepts the following values:  - 1 — Details about centroids are returned (default) - 0 — Details about centroids are not returned |
| `histogram` | This parameter accepts the following values:  - 1 — Details about histograms are returned (default) - 0 — Details about histograms are not returned |
| `rules` | This parameter accepts the following values:  - 2 — Details about rules are returned (default) - 1 — Rule summaries are returned - 0 — No information about rules is returned |

Return Values

Table 44-66 GET\_MODEL\_DETAILS\_OC Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_CLUSTERS` | Represents a set of rows of type `DM_CLUSTER`. The rows have the following columns:  ``` (id               NUMBER,  cluster_id       VARCHAR2(4000),  record_count     NUMBER,  parent           NUMBER,  tree_level       NUMBER,  dispersion       NUMBER,  split_predicate  DM_PREDICATES,  child            DM_CHILDREN,  centroid         DM_CENTROIDS,  histogram        DM_HISTOGRAMS,  rule             DM_RULE) ``` |
|  | The `split_predicate` column of `DM_CLUSTER` returns a nested table of type `DM_PREDICATES`. Each row, of type `DM_PREDICATE`, has the following columns:  ``` (attribute_name           VARCHAR2(4000),  attribute_subname        VARCHAR2(4000),  conditional_operator     CHAR(2) /*=,<>,<,>,<=,>=*/,  attribute_num_value      NUMBER,  attribute_str_value      VARCHAR2(4000),  attribute_support        NUMBER,  attribute_confidence     NUMBER) ``` |
|  | The `child` column of `DM_CLUSTER` returns a nested table of type `DM_CHILDREN`. The rows, of type `DM_CHILD`, have a single column of type `NUMBER`, which contains the identifiers of each child. |
|  | The `centroid` column of `DM_CLUSTER` returns a nested table of type `DM_CENTROIDS`. The rows, of type `DM_CENTROID`, have the following columns:  ``` (attribute_name    VARCHAR2(4000),  attribute_subname  VARCHAR2(4000),  mean               NUMBER,  mode_value         VARCHAR2(4000),  variance           NUMBER) ``` |
|  | The `histogram` column of `DM_CLUSTER` returns a nested table of type `DM_HISTOGRAMS`. The rows, of type `DM_HISTOGRAM_BIN`, have the following columns:  ``` (attribute_name    VARCHAR2(4000),  attribute_subname  VARCHAR2(4000),  bin_id             NUMBER,  lower_bound        NUMBER,  upper_bound        NUMBER,  label              VARCHAR2(4000),  count              NUMBER) ``` |
|  | The `rule` column of `DM_CLUSTER` returns a single row of type `DM_RULE`. The columns are:  ``` (rule_id            INTEGER,  antecedent         DM_PREDICATES,  consequent         DM_PREDICATES,  rule_support       NUMBER,  rule_confidence    NUMBER,  rule_lift          NUMBER,  antecedent_support NUMBER,  consequent_support NUMBER,  number_of_items    INTEGER) ``` |
|  | The `antecedent` and `consequent` columns each return nested tables of type `DM_PREDICATES`.The rows, of type `DM_PREDICATE`, have the following columns:  ``` (attribute_name           VARCHAR2(4000),  attribute_subname        VARCHAR2(4000),  conditional_operator     CHAR(2)/*=,<>,<,>,<=,>=*/,  attribute_num_value      NUMBER,  attribute_str_value      VARCHAR2(4000),  attribute_support        NUMBER,  attribute_confidence     NUMBER) ``` |

Usage Notes

The table function pipes out rows of type `DM_CLUSTER`. For information about Data Mining data types and piped output from table functions, see "Data Types".

Examples

The following example returns model details for the clustering model `OC_SH_Clus_sample`, which was created by the sample program `dmocdemo.sql`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

For each cluster in this example, the split predicate indicates the attribute and the condition used to assign records to the cluster's children during model build. It provides an important piece of information on how the population within a cluster can be divided up into two smaller clusters.

```
SELECT clu_id, attribute_name, op, s_value
     FROM (SELECT a.id clu_id, sp.attribute_name, sp.conditional_operator op,
                  sp.attribute_str_value s_value
             FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_OC(
                    'OC_SH_Clus_sample')) a,
                  TABLE(a.split_predicate) sp
           ORDER BY a.id, op, s_value)
     WHERE ROWNUM < 11;
 
     CLU_ID ATTRIBUTE_NAME       OP S_VALUE
----------- -------------------- ---------------------------------
          1 OCCUPATION           IN ?
          1 OCCUPATION           IN Armed-F
          1 OCCUPATION           IN Cleric.
          1 OCCUPATION           IN Crafts
          2 OCCUPATION           IN ?
          2 OCCUPATION           IN Armed-F
          2 OCCUPATION           IN Cleric.
          3 OCCUPATION           IN Exec.
          3 OCCUPATION           IN Farming
          3 OCCUPATION           IN Handler
```

---

### GET\_MODEL\_DETAILS\_SVM Function

This table function returns a set of rows that provide the details of a linear Support Vector Machine (SVM) model. If invoked for nonlinear SVM, it returns `ORA-40215`.

In linear SVM models, only nonzero coefficients are stored. This reduces storage and speeds up model loading. As a result, if an attribute is missing in the coefficient list returned by `GET_MODEL_DETAILS_SVM`, then the coefficient of this attribute should be interpreted as zero.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_SVM (
        model_name        VARCHAR2,
        reverse_coef      NUMBER DEFAULT 0)
 RETURN DM_SVM_LINEAR_COEFF_SET PIPELINED;
```

Parameters

Table 44-67 GET\_MODEL\_DETAILS\_SVM Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `reverse_coef` | Whether or not `GET_MODEL_DETAILS_SVM` should transform the attribute coefficients using the original attribute transformations.  When `reverse_coef` is set to 0 (default), `GET_MODEL_DETAILS_SVM` returns the coefficients directly from the model without applying transformations.  When `reverse_coef` is set to 1, `GET_MODEL_DETAILS_SVM` transforms the coefficients and bias by applying the normalization shifts and scales that were generated using automatic data preparation.  See Usage Note 4. |

Return Values

Table 44-68 GET\_MODEL\_DETAILS\_SVM Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_SVM_LINEAR_COEFF_SET` | Represents a set of rows of type `DM_SVM_LINEAR_COEFF`. The rows have the following columns:  ``` (class            VARCHAR2(4000),  attribute_set    DM_SVM_ATTRIBUTE_SET) ``` |
|  | The `attribute_set` column returns a nested table of type `DM_SVM_ATTRIBUTE_SET`. The rows, of type `DM_SVM_ATTRIBUTE`, have the following columns:  ``` (attribute_name      VARCHAR2(4000),  attribute_subname   VARCHAR2(4000),  attribute_value     VARCHAR2(4000),  coefficient         NUMBER) ```  See Usage Notes. |

Usage Notes

1. This table function pipes out rows of type `DM_SVM_LINEAR_COEFF`. For information on Data Mining data types and piped output from table functions, see "Data Types".
2. The `class` column of `DM_SVM_LINEAR_COEFF` contains classification target values. For SVM regression models, `class` is null. For each classification target value, a set of coefficients is returned. For binary classification, one-class classification, and regression models, only a single set of coefficients is returned.
3. The `attribute_value` column in `DM_SVM_ATTRIBUTE_SET` is used for categorical attributes.
4. `GET_MODEL_DETAILS` functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model.
	The coefficients are related to the transformed, not the original, attributes. When returned directly with the model details, the coefficients may not provide meaningful information. If you want `GET_MODEL_DETAILS_SVM` to transform the coefficients such that they relate to the original attributes, set the `reverse_coef` parameter to 1.

Examples

The following example returns model details for the SVM classification model `SVMC_SH_Clas_sample`, which was created by the sample program `dmsvcdem.sql`. For information about the sample programs, see [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

```
WITH
  mod_dtls AS (
  SELECT *
    FROM TABLE(DBMS_DATA_MINING.GET_MODEL_DETAILS_SVM('SVMC_SH_Clas_sample'))
  ),
  model_details AS (
  SELECT D.class, A.attribute_name, A.attribute_value, A.coefficient
    FROM mod_dtls D,
            TABLE(D.attribute_set) A
    ORDER BY D.class, ABS(A.coefficient) DESC
  )
  SELECT class, attribute_name aname, attribute_value aval, coefficient coeff
    FROM model_details
    WHERE ROWNUM < 11;
 
CLASS      ANAME                     AVAL                      COEFF
---------- ------------------------- ------------------------- -----
1                                                              -2.85
1          BOOKKEEPING_APPLICATION                              1.11
1          OCCUPATION                Other                      -.94
1          HOUSEHOLD_SIZE            4-5                         .88
1          CUST_MARITAL_STATUS       Married                     .82
1          YRS_RESIDENCE                                         .76
1          HOUSEHOLD_SIZE            6-8                        -.74
1          OCCUPATION                Exec.                       .71
1          EDUCATION                 11th                       -.71
1          EDUCATION                 Masters                     .63
```

---

### GET\_MODEL\_DETAILS\_XML Function

This function returns an XML object that provides the details of a Decision Tree model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_DETAILS_XML (
         model_name      IN       VARCHAR2)
   RETURN XMLTYPE;
```

Parameters

Table 44-69 GET\_MODEL\_DETAILS\_XML Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-70 GET\_MODEL\_DETAILS\_XML Function Return Value

| Return Value | Description |
| --- | --- |
| `XMLTYPE` | The XML definition for the decision tree model. See [Chapter 260, "XMLTYPE"](t_xml.md) for details.  The XML conforms to the Data Mining Group Predictive Model Markup Language (PMML) version 2.1 specification. The specification is available at `http://www.dmg.org`. |

Usage Notes

Special characters that cannot be displayed by Oracle XML are converted to '#'.

Examples

The following statements in SQL\*Plus return the details of the decision tree model `dt_sh_clas_sample`. This model is created by the program `dmdtdemo.sql`, one of the sample data mining programs provided with Oracle Database Examples.

Note: The "&quot" characters you will see in the XML output are a result of SQL\*Plus behavior. To display the XML in proper format, cut and past it into a file and open the file in a browser.

```
column dt_details format a320
SELECT 
 dbms_data_mining.get_model_details_xml('dt_sh_clas_sample') 
 AS DT_DETAILS
FROM dual;

DT_DETAILS
--------------------------------------------------------------------------------
<PMML version="2.1">
  <Header copyright="Copyright (c) 2004, Oracle Corporation. All rights
      reserved."/>
  <DataDictionary numberOfFields="9">
    <DataField name="AFFINITY_CARD" optype="categorical"/> 
    <DataField name="AGE" optype="continuous"/> 
    <DataField name="BOOKKEEPING_APPLICATION" optype="continuous"/>
    <DataField name="CUST_MARITAL_STATUS" optype="categorical"/>
    <DataField name="EDUCATION" optype="categorical"/> 
    <DataField name="HOUSEHOLD_SIZE" optype="categorical"/>
    <DataField name="OCCUPATION" optype="categorical"/>
    <DataField name="YRS_RESIDENCE" optype="continuous"/>
    <DataField name="Y_BOX_GAMES" optype="continuous"/>
  </DataDictionary>
  <TreeModel modelName="DT_SH_CLAS_SAMPLE" functionName="classification"
      splitCharacteristic="binarySplit">
    <Extension name="buildSettings">
      <Setting name="TREE_IMPURITY_METRIC" value="TREE_IMPURITY_GINI"/>
      <Setting name="TREE_TERM_MAX_DEPTH" value="7"/>
      <Setting name="TREE_TERM_MINPCT_NODE" value=".05"/>
      <Setting name="TREE_TERM_MINPCT_SPLIT" value=".1"/> 
      <Setting name="TREE_TERM_MINREC_NODE" value="10"/>
      <Setting name="TREE_TERM_MINREC_SPLIT" value="20"/>
      <costMatrix>
        <costElement>
          <actualValue>0</actualValue>
          <predictedValue>0</predictedValue>
          <cost>0</cost>
        </costElement>
        <costElement>
          <actualValue>0</actualValue>
          <predictedValue>1</predictedValue>
          <cost>1</cost>
        </costElement>
        <costElement>
          <actualValue>1</actualValue>
          <predictedValue>0</predictedValue>
          <cost>8</cost> 
        </costElement>
        <costElement> 
          <actualValue>1</actualValue>
          <predictedValue>1</predictedValue> 
          <cost>0</cost> 
        </costElement>
      </costMatrix>
    </Extension>
    <MiningSchema>
      .
      .
      .
      .
      .
      . 
      </Node>
    </Node>
  </TreeModel>
</PMML>
```

---

### GET\_MODEL\_SETTINGS Function

The `GET_MODEL_SETTINGS` function was deprecated in Oracle Data Mining 11g Release 1 (11.1). It was replaced with the data dictionary view \* `_MINING_MODEL_SETTINGS`. `USER_`, `ALL_`, and `DBA_` versions of the view are available. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_building.htm#DMPRG210).

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

Note:

See "Deprecated Subprograms"

This table function returns the list of settings that were used to build the model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_SETTINGS(
   model_name           IN VARCHAR2)
 RETURN DM_MODEL_SETTINGS PIPELINED;
```

Parameters

Table 44-71 GET\_MODEL\_SETTINGS Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-72 GET\_MODEL\_SETTINGS Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_MODEL_SETTINGS` | Represents a set of rows of type `DM_MODEL_SETTING`. The rows have the following columns:  ``` (setting_name    VARCHAR2(30), setting_value    VARCHAR2(128)) ``` |

Usage Notes

The table function pipes out rows of type DM\_MODEL\_SETTING. For information about Data Mining data types and piped output from table functions, see "Data Types".

You can use this table function to determine the settings that were used to build the model. This is purely for informational purposes only — you cannot alter the model to adopt new settings.

Examples

Assume that you have built a classification model `census_model` using the Naive Bayes algorithm. You can retrieve the model settings using Oracle SQL as follows:

```
SELECT setting_name, setting_value
  FROM TABLE(DBMS_DATA_MINING.GET_MODEL_SETTINGS('census_model'));
```

---

### GET\_MODEL\_SIGNATURE Function

The `GET_MODEL_SIGNATURE` function was deprecated in Oracle Data Mining 11g Release 1 (11.1). It was replaced with the data dictionary view \* `_MINING_MODEL_ATTRIBUTES`. `USER_`, `ALL_`, and `DBA_` versions of the view are available. See [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/xform_casetbl.htm#DMPRG018).

Oracle recommends that you do not use deprecated procedures in new applications. Support for deprecated features is for backward compatibility only.

Note:

See "Deprecated Subprograms"

This table function returns the model signature, which lists the column attributes used to build the model and which should be present in the scoring data.

The case identifier is not considered a mining attribute. For classification and regression models, the target attribute is also not considered part of the model signature.

See Also:

Instead of using the `GET_MODEL_SIGNATURE` function, you can query the data dictionary view, `ALL_MINING_MODEL_ATTRIBUTES`. See the [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/xform_casetbl.htm#DMPRG018).

Syntax

```
DBMS_DATA_MINING.GET_MODEL_SIGNATURE(
  model_name           IN VARCHAR2)
RETURN DM_MODEL_SIGNATURE PIPELINED;
```

Parameters

Table 44-73 GET\_MODEL\_SIGNATURE Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-74 GET\_MODEL\_SIGNATURE Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_MODEL_SIGNATURE` | Represents a set of rows of type `DM_MODEL_SIGNATURE_ATTRIBUTE`. The rows have the following columns:  ``` (attribute_name      VARCHAR2(30),  attribute_type      VARCHAR2(106)) ``` |

Usage Notes

This table function pipes out rows of type `DM_MODEL_SIGNATURE`. For information on Data Mining data types and piped output from table functions, see "Data Types".

Examples

Assume that you have built a classification model `census_model` using the Naive Bayes algorithm. You can retrieve the model details using Oracle SQL as follows:

```
SELECT attribute_name, attribute_type
  FROM TABLE(DBMS_DATA_MINING.GET_MODEL_SIGNATURE('census_model');
```

---

### GET\_MODEL\_TRANSFORMATIONS Function

This function returns the transformation expressions embedded in the specified model.

Syntax

```
DBMS_DATA_MINING.GET_MODEL_TRANSFORMATIONS (
      model_name     IN VARCHAR2)
RETURN DM_TRANSFORMS PIPELINED;
```

Parameters

Table 44-75 GET\_MODEL\_TRANSFORMATIONS Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Return Values

Table 44-76 GET\_MODEL\_TRANSFORMATIONS Function Return Value

| Return Value | Description |
| --- | --- |
| `DM_TRANSFORMS` | The transformation expressions embedded in `model_name`.  The `DM_TRANSFORMS` type is a table of `DM_TRANSFORM` objects. Each `DM_TRANSFORM` has these fields:  ``` attribute_name       VARCHAR2(4000) attribute_subname    VARCHAR2(4000) expression           CLOB reverse_expression   CLOB ``` |

Usage Notes

When Automatic Data Preparation (ADP) is enabled, both automatic and user-defined transformations may be associated with an attribute. In this case, the user-defined transformations are evaluated before the automatic transformations.

Examples

In this example, several columns in the `SH.CUSTOMERS` table are used to create a Naive Bayes model. A transformation expression is specified for one of the columns. The model does not use ADP.

```
CREATE OR REPLACE VIEW mining_data AS
   SELECT cust_id, cust_year_of_birth, cust_income_level,cust_credit_limit
   FROM sh.customers;

describe mining_data
 Name                                   Null?    Type
 -------------------------------------- -------- --------------------------
 CUST_ID                                NOT NULL NUMBER
 CUST_YEAR_OF_BIRTH                     NOT NULL NUMBER(4)
 CUST_INCOME_LEVEL                               VARCHAR2(30)
 CUST_CREDIT_LIMIT                               NUMBER
 
CREATE TABLE settings_nb(
      setting_name  VARCHAR2(30),
      setting_value VARCHAR2(30));
BEGIN
     INSERT INTO settings_nb (setting_name, setting_value) VALUES
           (dbms_data_mining.algo_name, dbms_data_mining.algo_naive_bayes);
     INSERT INTO settings_nb (setting_name, setting_value) VALUES
           (dbms_data_mining.prep_auto, dbms_data_mining.prep_auto_off);
     COMMIT;
END;
/
DECLARE
    mining_data_xforms   dbms_data_mining_transform.TRANSFORM_LIST;
  BEGIN
    dbms_data_mining_transform.SET_TRANSFORM (
         xform_list           =>  mining_data_xforms,
         attribute_name       => 'cust_year_of_birth',
         attribute_subname    =>  null,
         expression           => 'cust_year_of_birth + 10',
         reverse_expression   => 'cust_year_of_birth - 10');
    dbms_data_mining.CREATE_MODEL (
        model_name           =>  'new_model',
        mining_function      =>   dbms_data_mining.classification,
        data_table_name      =>  'mining_data',
        case_id_column_name  =>  'cust_id',
        target_column_name   =>  'cust_income_level',
        settings_table_name  =>  'settings_nb',
        data_schema_name     =>   nulL,
        settings_schema_name =>   null,
        xform_list           =>   mining_data_xforms );
  END;
 /
SELECT attribute_name, TO_CHAR(expression), TO_CHAR(reverse_expression)
      FROM TABLE (dbms_data_mining.GET_MODEL_TRANSFORMATIONS('new_model'));

ATTRIBUTE_NAME      TO_CHAR(EXPRESSION)       TO_CHAR(REVERSE_EXPRESSION)
------------------  ------------------------  ----------------------------- 
CUST_YEAR_OF_BIRTH  cust_year_of_birth + 10   cust_year_of_birth - 10
```

---

### GET\_TRANSFORM\_LIST Procedure

This procedure converts transformation expressions specified as `DM_TRANSFORMS` to a transformation list (`TRANSFORM_LIST`) that can be used in creating a model. `DM_TRANSFORMS` is returned by the `GET_MODEL_TRANSFORMATIONS` function.

You can also use routines in the `DBMS_DATA_MINING_TRANSFORM` package to construct a transformation list.

Syntax

```
DBMS_DATA_MINING.GET_TRANSFORM_LIST (
      xform_list           OUT NOCOPY TRANSFORM_LIST,
      model_xforms         IN  DM_TRANSFORMS);
```

Parameters

Table 44-77 GET\_TRANSFORM\_LIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xform_list` | A list of transformation specifications that can be embedded in a model. Accepted as a parameter to the CREATE\_MODEL Procedure.  The `TRANSFORM_LIST` type is a table of `TRANSFORM_REC` objects. Each `TRANSFORM_REC` has these fields:  ``` attribute_name      VARCHAR2(30) attribute_subname   VARCHAR2(4000) expression          EXPRESSION_REC reverse_expression  EXPRESSION_REC attribute_spec      VARCHAR2(4000) ```  For details about the `TRANSFORM_LIST` collection type, see [Table 45-1, "Data Types in DBMS\_DATA\_MINING\_TRANSFORM"](d_dmtran.md). |
| `model_xforms` | A list of embedded transformation expressions returned by the GET\_MODEL\_TRANSFORMATIONS Function for a specific model.  The `DM_TRANSFORMS` type is a table of `DM_TRANSFORM` objects. Each `DM_TRANSFORM` has these fields:  ``` attribute_name       VARCHAR2(4000) attribute_subname    VARCHAR2(4000) expression           CLOB reverse_expression   CLOB ``` |

Examples

In this example, a model `mod1` is trained using several columns in the `SH.CUSTOMERS` table. The model uses ADP, which automatically bins one of the columns.

A second model `mod2` is trained on the same data without ADP, but it uses a transformation list that was obtained from `mod1`. As a result, both `mod1` and `mod2` have the same embedded transformation expression.

```
CREATE OR REPLACE VIEW mining_data AS
     SELECT cust_id, cust_year_of_birth, cust_income_level, cust_credit_limit
     FROM sh.customers;
 
describe mining_data
 Name                                      Null?    Type
 ----------------------------------------- -------- ----------------------------
 CUST_ID                                   NOT NULL NUMBER
 CUST_YEAR_OF_BIRTH                        NOT NULL NUMBER(4)
 CUST_INCOME_LEVEL                                  VARCHAR2(30)
 CUST_CREDIT_LIMIT                                  NUMBER

CREATE TABLE setmod1(setting_name  VARCHAR2(30),setting_value VARCHAR2(30));
BEGIN
   INSERT INTO setmod1 VALUES (dbms_data_mining.algo_name, dbms_data_mining.algo_naive_bayes);
   INSERT INTO setmod1 VALUES (dbms_data_mining.prep_auto,dbms_data_mining.prep_auto_on);
   dbms_data_mining.CREATE_MODEL (
               model_name            => 'mod1',
               mining_function       => dbms_data_mining.classification,
               data_table_name       => 'mining_data',
               case_id_column_name   => 'cust_id',
               target_column_name    => 'cust_income_level',
               settings_table_name   => 'setmod1');
    COMMIT;
END;
/
CREATE TABLE setmod2(setting_name  VARCHAR2(30),setting_value VARCHAR2(30));
BEGIN
  INSERT INTO setmod2
      VALUES (dbms_data_mining.algo_name, dbms_data_mining.algo_naive_bayes);
  COMMIT;
END;
/
DECLARE
  v_xform_list       dbms_data_mining_transform.TRANSFORM_LIST;
  dmxf               DM_TRANSFORMS;
BEGIN
   EXECUTE IMMEDIATE
    'SELECT dm_transform(attribute_name, attribute_subname,expression, reverse_expression)
     FROM TABLE(dbms_data_mining.GET_MODEL_TRANSFORMATIONS (''mod1''))'
     BULK COLLECT INTO dmxf;
   dbms_data_mining.GET_TRANSFORM_LIST (
        xform_list             =>  v_xform_list,
        model_xforms           =>  dmxf);
   dbms_data_mining.CREATE_MODEL(
         model_name            => 'mod2',
         mining_function       =>  dbms_data_mining.classification,
         data_table_name       => 'mining_data',
         case_id_column_name   => 'cust_id',
         target_column_name    => 'cust_income_level',
         settings_table_name   => 'setmod2',
         xform_list            =>  v_xform_list);
END;
/

-- Transformation expression embedded in mod1
SELECT TO_CHAR(expression) FROM TABLE (dbms_data_mining.GET_MODEL_TRANSFORMATIONS('mod1'));

TO_CHAR(EXPRESSION)
--------------------------------------------------------------------------------
CASE WHEN "CUST_YEAR_OF_BIRTH"<1915 THEN 0 WHEN "CUST_YEAR_OF_BIRTH"<=1915 THEN 0
WHEN "CUST_YEAR_OF_BIRTH"<=1920.5 THEN 1 WHEN "CUST_YEAR_OF_BIRTH"<=1924.5 THEN 2
.
.
.
.5 THEN 29 WHEN "CUST_YEAR_OF_BIRTH" IS NOT NULL THEN 30 END

-- Transformation expression embedded in mod2
SELECT TO_CHAR(expression) FROM TABLE (dbms_data_mining.GET_MODEL_TRANSFORMATIONS('mod2'));

TO_CHAR(EXPRESSION)
--------------------------------------------------------------------------------
CASE WHEN "CUST_YEAR_OF_BIRTH"<1915 THEN 0 WHEN "CUST_YEAR_OF_BIRTH"<=1915 THEN 0
WHEN "CUST_YEAR_OF_BIRTH"<=1920.5 THEN 1 WHEN "CUST_YEAR_OF_BIRTH"<=1924.5 THEN 2
.
.
.
.5 THEN 29 WHEN "CUST_YEAR_OF_BIRTH" IS NOT NULL THEN 30 END

-- Reverse transformation expression embedded in mod1
SELECT TO_CHAR(reverse_expression)FROM TABLE (dbms_data_mining.GET_MODEL_TRANSFORMATIONS('mod1'));

TO_CHAR(REVERSE_EXPRESSION)
--------------------------------------------------------------------------------
DECODE("CUST_YEAR_OF_BIRTH",0,'( ; 1915), [1915; 1915]',1,'(1915; 1920.5]',2,'(1
920.5; 1924.5]',3,'(1924.5; 1928.5]',4,'(1928.5; 1932.5]',5,'(1932.5; 1936.5]',6
.
.
.
8,'(1987.5; 1988.5]',29,'(1988.5; 1989.5]',30,'(1989.5;  )',NULL,'NULL')
 
-- Reverse transformation expression embedded in mod2
SELECT TO_CHAR(reverse_expression) FROM TABLE (dbms_data_mining.GET_MODEL_TRANSFORMATIONS('mod2'));
      
TO_CHAR(REVERSE_EXPRESSION)
--------------------------------------------------------------------------------
DECODE("CUST_YEAR_OF_BIRTH",0,'( ; 1915), [1915; 1915]',1,'(1915; 1920.5]',2,'(1
920.5; 1924.5]',3,'(1924.5; 1928.5]',4,'(1928.5; 1932.5]',5,'(1932.5; 1936.5]',6
.
.
.
8,'(1987.5; 1988.5]',29,'(1988.5; 1989.5]',30,'(1989.5;  )',NULL,'NULL')
```

---

### IMPORT\_MODEL Procedure

This procedure imports one or more data mining models. The procedure is overloaded. You can call it to import mining models from a dump file set, or you can call it to import a single mining model from a PMML document.

Import from a dump file set

You can import mining models from a dump file set that was created by the EXPORT\_MODEL Procedure. `IMPORT_MODEL` and `EXPORT_MODEL` use Oracle Data Pump technology to export to and import from a dump file set.

When Oracle Data Pump is used directly to export/import an entire schema or database, the mining models in the schema or database are included. `EXPORT_MODEL` and `IMPORT_MODEL` export/import mining models only.

Import from PMML

This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2) Data Mining.

You can import a mining model represented in Predictive Model Markup Language (PMML). The model must be of type `RegressionModel`, either linear regression or binary logistic regression.

PMML is an XML-based standard specified by the Data Mining Group (`http://www.dmg.org`). Applications that are PMML-compliant can deploy PMML-compliant models that were created by any vendor. Oracle Data Mining supports the core features of PMML 3.1 for regression models.

See Also:

[Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/schemaobjs.htm#DMADM010) for more information about exporting and importing mining models

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/part_dp.htm#SUTIL2877) for information about Oracle Data Pump

`http://www.dmg.org/faq.html` for more information about PMML

Syntax

Imports a mining model from a dump file set:

```
DBMS_DATA_MINING.IMPORT_MODEL (
      filename        IN  VARCHAR2,
      directory       IN  VARCHAR2,
      model_filter    IN  VARCHAR2 DEFAULT NULL,
      operation       IN  VARCHAR2 DEFAULT NULL,
      remote_link     IN  VARCHAR2 DEFAULT NULL,
      jobname         IN  VARCHAR2 DEFAULT NULL,
      schema_remap    IN  VARCHAR2 DEFAULT NULL);
```

Imports a mining model from a PMML document:

```
DBMS_DATA_MINING.IMPORT_MODEL (
      model_name      IN  VARCHAR2,
      pmmldoc         IN XMLTYPE);
```

Parameters

Table 44-78 IMPORT\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `filename` | Name of the dump file set from which the models should be imported. The dump file set must have been created by the `EXPORT_MODEL` procedure or the `expdp` export utility of Oracle Data Pump.  The dump file set can contain one or more files. (Refer to "EXPORT\_MODEL Procedure" for details.) If the dump file set contains multiple files, you can specify `'` `filename` `%U'` instead of listing them. For example, if your dump file set contains 3 files, `archive01.dmp`, `archive02.dmp`, and `archive03.dmp`, you can import them by specifying `'archive%U'`. |
| `directory` | Name of a pre-defined directory object that specifies where the dump file set is located. Both the exporting and the importing user must have read/write access to the directory object and to the file system directory that it identifies.  Note: The target database must have also have read/write access to the file system directory. |
| `model_filter` | Optional parameter that specifies one or more models to import. If you do not specify a value for `model_filter`, all models in the dump file set are imported. You can also specify `NULL` (the default) or 'ALL' to import all models.  The value of `model_filter` can be one or more model names. The following are valid filters.  ``` 'mymodel1' 'name IN (''mymodel2'',''mymodel3'')' ```  The first causes `IMPORT_MODEL` to import a single model named `mymodel1`. The second causes `IMPORT_MODEL` to import two models, `mymodel2` and `mymodel3`. |
| `operation` | Optional parameter that specifies whether to import the models or the SQL statements that create the models. By default, the models are imported.  You can specify either of the following values for `operation`:  - `'IMPORT'` — Import the models (Default) - `'SQL_FILE'` — Write the SQL DDL for creating the models to a text file. The text file is named `job_name``.sql` and is located in the dump set directory. |
| `remote_link` | Optional parameter not used in this release. Set to `NULL` |
| `jobname` | Optional parameter that specifies the name of the import job. By default, the name has the form `username` `_imp_` `nnnn`, where `nnnn` is a number. For example, a job name in the `SCOTT` schema might be `SCOTT_imp_134`.  If you specify a job name, it must be unique within the schema. The maximum length of the job name is 30 characters.  A log file for the import job, named `jobname``.log,` is created in the same directory as the dump file set. |
| `schema_remap` | Optional parameter for importing into a different schema. By default, models are exported and imported within the same schema.  If the dump file set belongs to a different schema, you must specify a schema mapping in the form `export_user`:`import_user`. For example, you would specify `'SCOTT:MARY'` to import a model exported by `SCOTT` into the `MARY` schema.  Note: In some cases, you may need to have the `IMP_FULL_DATABASE` privilege or the `SYS` role to import a model from a different schema. |
| `model_name` | Name for the new model that will be created in the database as a result of an import from PMML The name must be unique within the user's schema. |
| `pmmldoc` | The PMML document representing the model to be imported. The PMML document has an `XMLTYPE` object type. See [Chapter 260, "XMLTYPE"](t_xml.md) for details. |

Usage Notes

The following notes pertain to mining model import based on Oracle Data Pump.

Mining models are stored in the default tablespace of the mining model owner, or in a tablespace to which the owner has access. The tablespace must also exist in the target database, and the target user must have access to it. If the tablespace does not exist in the target database, you must create it before importing the models.

For example, if the models were created in schema `DMUSER` and the default tablespace for `DMUSER` is `USERS`, then the `USERS` tablespace must exist in the target database. You can create the `USERS` tablespace and grant access to a target user with appropriate tablespace quota as follows.

```
connect / as sysdba;
create tablespace USERS datafile 'data_file_name' size 200M autoextend on;
alter user target_user quota unlimited on USERS;
```

Examples

1. This example shows a model being exported and imported within the schema `dmuser2`. Then the same model is imported into the `dmuser3` schema. The `dmuser3` user has the `IMP_FULL_DATABASE` privilege.
	```
	SQL> connect dmuser2
	Enter password: dmuser2_password
	Connected.
	SQL> select model_name from user_mining_models;
	 
	MODEL_NAME
	------------------------------
	NMF_SH_SAMPLE
	SVMO_SH_CLAS_SAMPLE
	SVMR_SH_REGR_SAMPLE
	-- export the model called NMF_SH_SAMPLE to a dump file in same schema
	SQL>EXECUTE DBMS_DATA_MINING.EXPORT_MODEL ('NMF_SH_SAMPLE_out', 'DATA_PUMP_DIR',
	                            'name = ''NMF_SH_SAMPLE''');
	-- import the model back into the same schema
	SQL>EXECUTE DBMS_DATA_MINING.IMPORT_MODEL ('NMF_SH_SAMPLE_out01.dmp', 
	                            'DATA_PUMP_DIR', 'name = ''NMF_SH_SAMPLE''');
	-- connect as different user
	-- import same model into that schema
	SQL> connect dmuser3
	Enter password: dmuser3_password
	Connected.
	SQL>EXECUTE DBMS_DATA_MINING.IMPORT_MODEL ('NMF_SH_SAMPLE_out01.dmp', 
	                            'DATA_PUMP_DIR', 'name = ''NMF_SH_SAMPLE''',
	                            'IMPORT', NULL, 'nmf_imp_job', 'dmuser2:dmuser3');
	```
	The following example shows user `MARY` importing all models from a dump file, `model_exp_001.dmp`, which was created by user `SCOTT`. The dump file is located in the file system directory mapped to a directory object called `DM_DUMP`. If user `MARY` does not have `IMP_FULL_DATABASE` privileges, `IMPORT_MODEL` will raise an error.
	```
	-- import all models
	DECLARE
	  file_name       VARCHAR2(40);
	BEGIN
	  file_name := 'model_exp_001.dmp';
	  DBMS_DATA_MINING.IMPORT_MODEL(
	                filename=>file_name,
	               directory=>'DM_DUMP',                 schema_remap=>'SCOTT:MARY');
	  DBMS_OUTPUT.PUT_LINE(
	'DBMS_DATA_MINING.IMPORT_MODEL of all models from SCOTT done!');
	END;
	/
	```
2. This example shows how a PMML document called `SamplePMML1.xml` could be imported from a location referenced by directory object `PMMLDIR` into the schema of the current user. The imported model will be called `PMMLMODEL1`.
	```
	BEGIN    
	    dbms_data_mining.import_model ('PMMLMODEL1',
	        XMLType (bfilename ('PMMLDIR', 'SamplePMML1.xml'),
	          nls_charset_id ('AL32UTF8')
	        ));
	END;
	```

---

### RANK\_APPLY Procedure

This procedure ranks the results of an `APPLY` operation based on a top-N specification for predictive and descriptive model results. For classification models, you can provide a cost matrix as input, and obtain the ranked results with costs applied to the predictions.

Syntax

```
DBMS_DATA_MINING.RANK_APPLY (
      apply_result_table_name        IN VARCHAR2,
      case_id_column_name            IN VARCHAR2,
      score_column_name              IN VARCHAR2,
      score_criterion_column_name    IN VARCHAR2,
      ranked_apply_table_name        IN VARCHAR2,
      top_N                          IN INTEGER DEFAULT 1,
      cost_matrix_table_name         IN VARCHAR2 DEFAULT NULL,
      apply_result_schema_name       IN VARCHAR2 DEFAULT NULL,
      cost_matrix_schema_name        IN VARCHAR2 DEFAULT NULL);
```

Parameters

Table 44-79 RANK\_APPLY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `apply_result_table_name` | Name of the table or view containing the results of an `APPLY` operation on the test dataset (see Usage Notes) |
| `case_id_column_name` | Name of the case identifier column. This must be the same as the one used for generating `APPLY` results. |
| `score_column_name` | Name of the prediction column in the apply results table |
| `score_criterion_column_name` | Name of the probability column in the apply results table |
| `ranked_apply_result_tab_name` | Name of the table containing the ranked apply results |
| `top_N` | Top N predictions to be considered from the `APPLY` results for precision recall computation |
| `cost_matrix_table_name` | Name of the cost matrix table |
| `apply_result_schema_name` | Name of the schema hosting the `APPLY` results table |
| `cost_matrix_schema_name` | Name of the schema hosting the cost matrix table |

Usage Notes

You can use `RANK_APPLY` to generate ranked apply results, based on a top-N filter and also with application of cost for predictions, if the model was built with costs.

The behavior of `RANK_APPLY` is similar to that of `APPLY` with respect to other DDL-like operations such as `CREATE_MODEL`, `DROP_MODEL`, and `RENAME_MODEL`. The procedure does not depend on the model; the only input of relevance is the apply results generated in a fixed schema table from `APPLY`.

The main intended use of `RANK_APPLY` is for the generation of the final `APPLY` results against the scoring data in a production setting. You can apply the model against test data using `APPLY`, compute various test metrics against various cost matrix tables, and use the candidate cost matrix for `RANK_APPLY`.

The schema for the apply results from each of the supported algorithms is listed in subsequent sections. The `case_id` column will be the same case identifier column as that of the apply results.

#### Classification Models — NB, ABN, SVM

For numerical targets, the ranked results table will have the definition as shown:

```
(case_id       VARCHAR2/NUMBER,
prediction     NUMBER,
probability    NUMBER,
cost           NUMBER,
rank           INTEGER)
```

For categorical targets, the ranked results table will have the following definition:

```
(case_id       VARCHAR2/NUMBER,
prediction     VARCHAR2,
probability    NUMBER,
cost           NUMBER,
rank           INTEGER)
```

#### Clustering using k-Means or O-Cluster

Clustering is an unsupervised mining function, and hence there are no targets. The results of an `APPLY` operation contains simply the cluster identifier corresponding to a case, and the associated probability. Cost matrix is not considered here. The ranked results table will have the definition as shown, and contains the cluster ids ranked by `top-N`.

```
(case_id       VARCHAR2/NUMBER,
cluster_id     NUMBER,
probability    NUMBER,
rank           INTEGER)
```

#### Feature Extraction using NMF

Feature extraction is also an unsupervised mining function, and hence there are no targets. The results of an `APPLY` operation contains simply the feature identifier corresponding to a case, and the associated match quality. Cost matrix is not considered here. The ranked results table will have the definition as shown, and contains the feature ids ranked by `top-N`.

```
(case_id        VARCHAR2/NUMBER,
feature_id      NUMBER,
match_quality   NUMBER,
rank            INTEGER)
```

Examples

```
BEGIN
/* build a model with name census_model.
 * (See example under CREATE_MODEL)
 */ 

/* if training data was pre-processed in any manner,
 * perform the same pre-processing steps on apply
 * data also.
 * (See examples in the section on DBMS_DATA_MINING_TRANSFORM)
 */

/* apply the model to data to be scored */
DBMS_DATA_MINING.RANK_APPLY(
  apply_result_table_name       => 'census_apply_result',
  case_id_column_name           => 'person_id',
  score_column_name             => 'prediction',
  score_criterion_column_name   => 'probability
  ranked_apply_result_tab_name  => 'census_ranked_apply_result',
  top_N                         => 3,
  cost_matrix_table_name        => 'census_cost_matrix');
END;
/

-- View Ranked Apply Results
SELECT *
  FROM census_ranked_apply_result;
```

---

### REMOVE\_COST\_MATRIX Procedure

Removes the default scoring matrix from a classification model.

See Also:

- "ADD\_COST\_MATRIX Procedure"
- "REMOVE\_COST\_MATRIX Procedure"

Syntax

```
DBMS_DATA_MINING.REMOVE_COST_MATRIX (
      model_name   IN  VARCHAR2);
```

Parameters

Table 44-80 Remove\_Cost\_Matrix Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

Usage Notes

If the model is not in your schema, then `REMOVE_COST_MATRIX` requires the `ALTER ANY MINING MODEL` system privilege or the `ALTER` object privilege for the mining model.

Example

The Naive Bayes model `NB_SH_CLAS_SAMPLE` has an associated cost matrix that can be used for scoring the model.

```
SQL>SELECT *
      FROM TABLE(dbms_data_mining.get_model_cost_matrix('nb_sh_clas_sample'))
      ORDER BY predicted, actual;
 
ACTUAL     PREDICTED        COST
---------- ---------- ----------
0          0                   0
1          0                 .75
0          1                 .25
1          1                   0
```

You can remove the cost matrix with `REMOVE_COST_MATRIX`.

```
SQL>EXECUTE dbms_data_mining.remove_cost_matrix('nb_sh_clas_sample');

SQL>SELECT *
      FROM TABLE(dbms_data_mining.get_model_cost_matrix('nb_sh_clas_sample'))
      ORDER BY predicted, actual;

no rows selected
```

---

### RENAME\_MODEL Procedure

This procedure renames a mining model to a new name that you specify.

The model name is in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. For mining model naming restrictions, see "Mining Model Naming Restrictions".

Syntax

```
DBMS_DATA_MINING.RENAME_MODEL (
     model_name            IN VARCHAR2,
     new_model_name        IN VARCHAR2);
```

Parameters

Table 44-81 RENAME\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Old name of the model |
| `new_model_name` | New name of the model. |

Usage Notes

If an `APPLY` operation is using a model, and you attempt to rename the model during that time, the `RENAME` will succeed and `APPLY` will return indeterminate results.

Examples

Assume the existence of a model `census_model`. The following example shows how to rename this model.

```
BEGIN
  DBMS_DATA_MINING.RENAME_MODEL(
    model_name      => 'census_model',
    new_model_name  => 'census_new_model');
END;
/
```