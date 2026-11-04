---
title: DBMS_DATA_MINING
book: PL/SQL Packages and Types Reference
doc_id: E96430-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATA_MINING.html
tags:
  - oracle
  - 19c
  - pl-sql-packages-and-types-reference
---

The `DBMS_DATA_MINING` package is the application programming interface for creating, evaluating, and querying data mining models.

This chapter contains the following topics:

### DBMS\_DATA\_MINING Overview

Oracle Data Mining supports both supervised and unsupervised data mining. Supervised data mining predicts a target value based on historical data. Unsupervised data mining discovers natural groupings and does not use a target. You can use Oracle Data Mining to mine structured data and unstructured text.

Supervised data mining functions include:

- Classification
- Regression
- Feature Selection (Attribute Importance)

Unsupervised data mining functions include:

- Clustering
- Association
- Feature Extraction
- Anomaly Detection

The steps you use to build and apply a mining model depend on the data mining function and the algorithm being used. The algorithms supported by Oracle Data Mining are listed in Table 53-1.

Table 1 Oracle Data Mining Algorithms

| Algorithm | Abbreviation | Function |
| --- | --- | --- |
| Apriori | AR | Association |
| CUR Matrix Decomposition | CUR | Attribute Importance |
| Decision Tree | DT | Classification |
| Expectation Maximization | EM | Clustering |
| Explicit Semantic Analysis | ESA | Feature Extraction, Classification |
| Exponential Smoothing | ESM | Time Series |
| Generalized Linear Model | GLM | Classification, Regression |
| k-Means | KM | Clustering |
| Minimum Descriptor Length | MDL | Attribute Importance |
| Naive Bayes | NB | Classification |
| Neural Networks | NN | Classification, Regression |
| Non-Negative Matrix Factorization | NMF | Feature Extraction |
| Orthogonal Partitioning Clustering | O-Cluster | Clustering |
| Random Forest | RF | Classification |
| Singular Value Decomposition and Principal Component Analysis | SVD and PCA | Feature Extraction |
| Support Vector Machine | SVM | Classification, Regression, Anomaly Detection |

Oracle Data Mining supports more than one algorithm for the classification, regression, clustering, and feature extraction mining functions. Each of these mining functions has a default algorithm, as shown in Table 53-2.

Table 2 Oracle Data Mining Default Algorithms

| Mining Function | Default Algorithm |
| --- | --- |
| Classification | Naive Bayes |
| Clustering | k-Means |
| Feature Extraction | Non-Negative Matrix Factorization |
| Feature Selection | Minimum Descriptor Length |
| Regression | Support Vector Machine |

### DBMS\_DATA\_MINING Security Model

The `DBMS_DATA_MINING` package is owned by user `SYS` and is installed as part of database installation. Execution privilege on the package is granted to public. The routines in the package are run with invokers’ rights (run with the privileges of the current user).

The `DBMS_DATA_MINING` package exposes APIs that are leveraged by the Oracle Data Mining component of the Advanced Analytics Option. Users who wish to create mining models in their own schema require the `CREATE MINING MODEL` system privilege. Users who wish to create mining models in other schemas require the `CREATE ANY MINING MODEL` system privilege.

Users have full control over managing models that exist within their own schema. Additional system privileges necessary for managing data mining models in other schemas include `ALTER ANY MINING MODEL`, `DROP ANY MINING MODEL`, `SELECT ANY MINING MODEL`, `COMMENT ANY MINING MODEL`, and `AUDIT ANY`.

Individual object privileges on mining models,`ALTER MINING MODEL` and `SELECT MINING MODEL`, can be used to selectively grant privileges on a model to a different user.

**See Also:** [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG795) for more information about the security features of Oracle Data Mining

### DBMS\_DATA\_MINING - Mining Functions

A data mining **function** refers to the methods for solving a given class of data mining problems.

The mining function must be specified when a model is created. (See CREATE\_MODEL Procedure.)

Table 3 Mining Functions

| Value | Description |
| --- | --- |
| `ASSOCIATION` | Association is a descriptive mining function. An association model identifies relationships and the probability of their occurrence within a data set.  Association models use the Apriori algorithm. |
| `ATTRIBUTE_IMPORTANCE` | Attribute importance is a predictive mining function, also known as feature selection. An attribute importance model identifies the relative importance of an attribute in predicting a given outcome.  Attribute importance models can use Minimum Description Length, or CUR Matrix Decomposition. Minimum Description Length is the default. |
| `CLASSIFICATION` | Classification is a predictive mining function. A classification model uses historical data to predict a categorical target.  Classification models can use: Naive Bayes, Decision Tree, Logistic Regression, or Support Vector Machine. The default is Naive Bayes.  The classification function can also be used for anomaly detection. In this case, the SVM algorithm with a null target is used (One-Class SVM). |
| `CLUSTERING` | Clustering is a descriptive mining function. A clustering model identifies natural groupings within a data set.  Clustering models can use k-Means, O-Cluster, or Expectation Maximization. The default is k-Means. |
| `FEATURE_EXTRACTION` | Feature Extraction is a descriptive mining function. A feature extraction model creates an optimized data set on which to base a model.  Feature extraction models can use Explicit Semantic Analysis, Non-Negative Matrix Factorization, Singular Value Decomposition, or Principal Component Analysis. Non-Negative Matrix Factorization is the default. |
| `REGRESSION` | Regression is a predictive mining function. A regression model uses historical data to predict a numerical target.  Regression models can use Support Vector Machine or Linear Regression. The default is Support Vector Machine. |
| `TIME_SERIES` | Time series is a predictive mining function. A time series model forecasts the future values of a time-ordered series of historical numeric data over a user-specified time window. Time series models use the Exponential Smoothing algorithm. |

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON042) for more information about mining functions

### DBMS\_DATA\_MINING - Model Settings

Oracle Data Mining uses settings to specify the algorithm and other characteristics of a model. Some settings are general, some are specific to a mining function, and some are specific to an algorithm.

All settings have default values. If you want to override one or more of the settings for a model, you must create a settings table. The settings table must have the column names and datatypes shown in the following table.

Table 4 Required Columns in the Model Settings Table

| Column Name | Datatype |
| --- | --- |
| `SETTING_NAME` | `VARCHAR2(30)` |
| `SETTING_VALUE` | `VARCHAR2(4000)` |

The information you provide in the settings table is used by the model at build time. The name of the settings table is an optional argument to the CREATE\_MODEL Procedure.

You can find the settings used by a model by querying the data dictionary view `ALL_MINING_MODEL_SETTINGS`. This view lists the model settings used by the mining models to which you have access. All the setting values are included in the view, whether default or user-specified.

**See Also:**

- `ALL_MINING_MODEL_SETTINGS` in [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN20557)
- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG767) for information about specifying model settings

### DBMS\_DATA\_MINING - Algorithm Names

The `ALGO_NAME` setting specifies the model algorithm.

The values for the `ALGO_NAME` setting are listed in the following table.

Table 5 Algorithm Names

| ALGO\_NAME Value | Description | Mining Function |
| --- | --- | --- |
| `ALGO_AI_MDL` | Minimum Description Length | Attribute Importance |
| `ALGO_APRIORI_ASSOCIATION_RULES` | Apriori | Association Rules |
| `ALGO_CUR_DECOMPOSITION` | CUR Decomposition | Attribute Importance |
| `ALGO_DECISION_TREE` | Decision Tree | Classification |
| `ALGO_EXPECTATION_MAXIMIZATION` | Expectation Maximization | Clustering |
| `ALGO_EXPLICIT_SEMANTIC_ANALYS` | Explicit Semantic Analysis | Feature Extraction  Classification |
| `ALGO_EXPONENTIAL_SMOOTHING` | Exponential Smoothing | Time Series |
| `ALGO_EXTENSIBLE_LANG` | Language used for extensible algorithm | All mining functions supported |
| `ALGO_GENERALIZED_LINEAR_MODEL` | Generalized Linear Model | Classification, Regression; also Feature Selection and Generation |
| `ALGO_KMEANS` | Enhanced *k* \_Means | Clustering |
| `ALGO_NAIVE_BAYES` | Naive Bayes | Classification |
| `ALGO_NEURAL_NETWORK` | Neural Network | Classification |
| `ALGO_NONNEGATIVE_MATRIX_FACTOR` | Non-Negative Matrix Factorization | Feature Extraction |
| `ALGO_O_CLUSTER` | O-Cluster | Clustering |
| `ALGO_RANDOM_FOREST` | Random Forest | Classification |
| `ALGO_SINGULAR_VALUE_DECOMP` | Singular Value Decomposition | Feature Extraction |
| `ALGO_SUPPORT_VECTOR_MACHINES` | Support Vector Machine | Classification and Regression |

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON043) for information about algorithms

### DBMS\_DATA\_MINING - Automatic Data Preparation

Oracle Data Mining for SQL supports fully Automatic Data Preparation (ADP), user-directed general data preparation, and user-specified embedded data preparation. The `PREP_*` settings enable the user to request fully automated or user-directed general data preparation. By default, fully Automatic Data Preparation (`PREP_AUTO_ON`) is enabled.

When you enable ADP, the model uses heuristics to transform the build data according to the requirements of the algorithm. Instead of fully ADP, the user can request that the data be shifted and/or scaled with the `PREP_SCALE*` and `PREP_SHIFT*` settings. The transformation instructions are stored with the model and reused whenever the model is applied. The model settings can be viewed in `USER_MINING_MODEL_SETTINGS`.

You can choose to supplement Automatic Data Preparations by specifying additional transformations in the `xform_list` parameter when you build the model. See “ CREATE\_MODEL Procedure ” and “ CREATE\_MODEL2 Procedure ”.

If you do not use ADP *and* do not specify transformations in the `xform_list` parameter to `CREATE_MODEL`, you must implement your own transformations separately in the build, test, and scoring data. You must take special care to implement the exact same transformations in each data set.

If you do not use ADP, but you *do* specify transformations in the `xform_list` parameter to `CREATE_MODEL`, OML4SQL embeds the transformation definitions in the model and prepares the test and scoring data to match the build data.

The values for the `PREP_*` setting are described in the following table.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.PREP_AUTO_ON`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'ON'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 6 PREP\_\* Setting

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e3369" rowspan="2" width="20%"><p><code>PREP_AUTO</code></p></td><td headers="d299446e3385 d299446e3374" width="20%"><p><code>PREP_AUTO_ON</code></p></td><td headers="d299446e3385 d299446e3376" width="20%"><p><code>ON</code></p></td><td headers="d299446e3385 d299446e3378" width="40%">This setting enables fully automated data preparation.<p>The default is <code>PREP_AUTO_ON</code>.</p></td></tr><tr><td headers="d299446e3385 d299446e3374" width="20%"><p><code>PREP_AUTO_OFF</code></p></td><td headers="d299446e3385 d299446e3376" width="20%"><p><code>OFF</code></p></td><td headers="d299446e3385 d299446e3378" width="40%"><p>Disables fully automated data preparation.</p></td></tr><tr><td headers="d299446e3369" rowspan="2" width="20%"><p><code>PREP_SCALE_2DNUM</code></p></td><td headers="d299446e3433 d299446e3374" width="20%"><p><code>PREP_SCALE_STDDEV</code></p></td><td headers="d299446e3433 d299446e3376" width="20%"><p><code>PREP_SCALE_STDDEV</code></p></td><td headers="d299446e3433 d299446e3378" width="40%"><p>This setting enables scaling data preparation for two-dimensional numeric columns. <code>PREP_AUTO</code> must be <code>OFF</code> for this setting to take effect.</p><p><code>PREP_SCALE_STDDEV</code>: A request to divide the column values by the standard deviation of the column and is often provided together with <code>PREP_SHIFT_MEAN</code> to yield z-score normalization.</p></td></tr><tr><td headers="d299446e3433 d299446e3374" width="20%"><p><code> PREP_SCALE_RANGE</code></p></td><td headers="d299446e3433 d299446e3376" width="20%"><p><code> PREP_SCALE_RANGE</code></p></td><td headers="d299446e3433 d299446e3378" width="40%"><p>A request to divide the column values by the range of values and is often provided together with <code>PREP_SHIFT_MIN</code> to yield a range of [0,1].</p></td></tr><tr><td headers="d299446e3369" width="20%"><p><code>PREP_SCALE_NNUM </code></p></td><td headers="d299446e3497 d299446e3374" width="20%"><p><code>PREP_SCALE_MAXABS</code></p></td><td headers="d299446e3497 d299446e3376" width="20%"><p><code>PREP_SCALE_MAXABS</code></p></td><td headers="d299446e3497 d299446e3378" width="40%"><p>This setting enables scaling data preparation for nested numeric columns. <code>PREP_AUTO</code> must be <code>OFF</code> for this setting to take effect. If specified, then the valid value for this setting is <code>PREP_SCALE_MAXABS</code>, which yields data in the range of [-1,1].</p></td></tr><tr><td headers="d299446e3369" rowspan="2" width="20%"><p><code>PREP_SHIFT_2DNUM</code></p></td><td headers="d299446e3530 d299446e3374" width="20%"><p><code>PREP_SHIFT_MEAN</code></p></td><td headers="d299446e3530 d299446e3376" width="20%"><p><code>PREP_SHIFT_MEAN</code></p></td><td headers="d299446e3530 d299446e3378" width="40%"><p>This setting enables centering data preparation for two-dimensional numeric columns. <code>PREP_AUTO</code> must be <code>OFF</code> for this setting to take effect.</p><p><code>PREP_SHIFT_MEAN</code>: Results in subtracting the average of the column from each value.</p></td></tr><tr><td headers="d299446e3530 d299446e3374" width="20%"><p><code>PREP_SHIFT_MIN</code></p></td><td headers="d299446e3530 d299446e3376" width="20%"><p><code>PREP_SHIFT_MIN</code></p></td><td headers="d299446e3530 d299446e3378" width="40%"><p>Results in subtracting the minimum of the column from each value.</p></td></tr></tbody></table>

**See Also:** [*Oracle® Machine Learning for SQL*](https://docs.oracle.com/en/database/oracle/machine-learning/oml4sql/21/dmprg/about-transformations.html#GUID-233283C0-337B-4CF5-8F08-759B9B526957) for information about data transformations

### DBMS\_DATA\_MINING - Mining Function Settings

The settings described in this table apply to a mining function.

Table 7 Mining Function Settings

| Mining Function | Setting Name | Setting Value | Description |
| --- | --- | --- | --- |
| Association | `ASSO_MAX_RULE_LENGTH` | `TO_CHAR( 2<=` *numeric\_expr* `<=20)` | Maximum rule length for Association Rules.  Default is `4`. |
| Association | `ASSO_MIN_CONFIDENCE` | `TO_CHAR( 0<=` *numeric\_expr* `<=1)` | Minimum confidence for Association Rules.  Default is `0.1`. |
| Association | `ASSO_MIN_SUPPORT` | `TO_CHAR( 0<=` *numeric\_expr* `<=1)` | Minimum support for Association Rules  Default is `0.1`. |
| Association | `ASSO_MIN_SUPPORT_INT` | a positive integer | Minimum absolute support that each rule must satisfy. The value must be an integer.  Default is `1`. |
| Association | `ASSO_MIN_REV_CONFIDENCE` | `TO_CHAR( 0<=` *numeric\_expr* `<=1)` | Sets the Minimum Reverse Confidence that each rule should satisfy.  The Reverse Confidence of a rule is defined as the number of transactions in which the rule occurs divided by the number of transactions in which the consequent occurs.  The value is real number between 0 and 1.  The default is `0`. |
| Association | `ASSO_IN_RULES` | `NULL` | Sets Including Rules applied for each association rule: it specifies the list of items that at least one of them must appear in each reported association rule, either as antecedent or as consequent. It is a comma separated string containing the list of including items.  If not set, the default behavior is, the filtering is not applied.  For example,  ```md INSERT INTO sett_tab (setting_name, setting_value) VALUES  (dbms_data_mining.asso_in_rules, '''a'',''b'''); ``` |
| Association | `ASSO_EX_RULES` | `NULL` | Sets Excluding Rules applied for each association rule: it specifies the list of items that none of them can appear in each reported Association Rules. It is a comma separated string containing the list of excluding items. No rule can contain any item in the list.  The default is `NULL`.  For example,  ```md INSERT INTO sett_tab (setting_name, setting_value) VALUES  (dbms_data_mining.asso_ex_rules, '''a'',''b'''); ``` |
| Association | `ASSO_ANT_IN_RULES` | `NULL` | Sets Including Rules for the antecedent: it specifies the list of items that at least one of them must appear in the antecedent part of each reported association rule. It is a comma separated string containing the list of including items. The antecedent part of each rule must contain at least one item in the list.  The default is `NULL`.  For example,  ```md INSERT INTO sett_tab (setting_name, setting_value) VALUES  (dbms_data_mining.asso_ant_in_rules, '''a'',''b'''); ``` |
| Association | `ASSO_ANT_EX_RULES` | `NULL` | Sets Excluding Rules for the antecedent: it specifies the list of items that none of them can appear in the antecedent part of each reported association rule. It is a comma separated string containing the list of excluding items. No rule can contain any item in the list in its antecedent part.  The default is `NULL`.  For example,  ```md INSERT INTO sett_tab (setting_name, setting_value) VALUES  (dbms_data_mining.asso_ant_ex_rules, '''a'',''b'''); ``` |
| Association | `ASSO_CONS_IN_RULES` | `NULL` | Sets Including Rules for the consequent: it specifies the list of items that at least one of them must appear in the consequent part of each reported association rule. It is a comma separated string containing the list of including items. The consequent of each rule must be an item in the list.  The default is `NULL`.  For example,  ```md INSERT INTO sett_tab (setting_name, setting_value) VALUES  (dbms_data_mining.asso_cons_in_rules, '''a'',''b'''); ``` |
| Association | `ASSO_CONS_EX_RULES` | `NULL` | Sets Excluding Rules for the consequent: it specifies the list of items that none of them can appear in the consequent part of each reported association rule. It is a comma separated string containing the list of excluding items. No rule can have any item in the list as its consequent.  The excluding rule can be used to reduce the data that must be stored, but the user may be required to build extra model for executing different including or Excluding Rules.  The default is `NULL`.  For example,  ```md INSERT INTO sett_tab (setting_name, setting_value) VALUES  (dbms_data_mining.asso_cons_ex_rules, '''a'',''b'''); ``` |
| Association | `ASSO_AGGREGATES` | `NULL` | Specifies the columns to be aggregated. It is a comma separated string containing the names of the columns for aggregation. Number of columns in the list must be <= 10.< p>  You can set `ASSO_AGGREGATES` if `ODMS_ITEM_ID_COLUMN_NAME` is set indicating transactional input data. See DBMS\_DATA\_MINING - Global Settings. The data table must have valid column names such as `ITEM_ID` and `CASE_ID` which are derived from `ODMS_ITEM_ID_COLUMN_NAME` and `case_id_column_name` respectively.  `ITEM_VALUE` is not a mandatory value.  The default is `NULL`.  For each item, the user may supply several columns to aggregate. It requires more memory to buffer the extra data. Also, the performance impact can be seen because of the larger input data set and more operation. |
| \<p>Association\</p> | `ASSO_ABS_ERROR` | `0` < `ASSO_ABS_ERROR` ≤ `MAX(ASSO_MIN_SUPPORT, ASSO_MIN_CONFIDENCE). ` | Specifies the absolute error for the Association Rules sampling.  A smaller value of `ASSO_ABS_ERROR` obtains a larger sample size which gives accurate results but takes longer computational time. "Set a reasonable value for `ASSO_ABS_ERROR`, such as its default value, to avoid large sample size. The default value is `0.5` \* `MAX(ASSO_MIN_SUPPORT, ASSO_MIN_CONFIDENCE)`. |
| \<p>Association\</p> | `ASSO_CONF_LEVEL` | `0` ≤ `ASSO_CONF_LEVEL` ≤ `1` | Specifies the confidence level for an Association Rules sample.  A larger value of `ASSO_CONF_LEVEL` obtains a larger sample size. Any value between `0.9` and `1` is suitable. The default value is `0.95`. |
| Classification | `CLAS_COST_TABLE_NAME` | *table\_name* | (Decision Tree only) Name of a table that stores a cost matrix to be used by the algorithm in building the model. The cost matrix specifies the costs associated with misclassifications.  Only Decision Tree models can use a cost matrix at build time. All classification algorithms can use a cost matrix at apply time.  The cost matrix table is user-created. See " ADD\_COST\_MATRIX Procedure " for the column requirements.  See [Oracle Data Mining Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON050) for information about costs. |
| Classification | `CLAS_PRIORS_TABLE_NAME` | *table\_name* | (Naive Bayes) Name of a table that stores prior probabilities to offset differences in distribution between the build data and the scoring data.  The priors table is user-created. See [Oracle Data Mining User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG858) for the column requirements. See [Oracle Data Mining Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON033) for additional information about priors. |
| Classification | `CLAS_WEIGHTS_TABLE_NAME` | *table\_name* | (GLM and SVM only) Name of a table that stores weighting information for individual target values in SVM classification and GLM logistic regression models. The weights are used by the algorithm to bias the model in favor of higher weighted classes.  The class weights table is user-created. See [Oracle Data Mining User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG860) for the column requirements. See [Oracle Data Mining Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON033) for additional information about class weights. |
| Classification | `CLAS_WEIGHTS_BALANCED` | `ON`  `OFF` | This setting indicates that the algorithm must create a model that balances the target distribution. This setting is most relevant in the presence of rare targets, as balancing the distribution may enable better average accuracy (average of per-class accuracy) instead of overall accuracy (which favors the dominant class). The default value is `OFF`. |
| Classification | `CLAS_MAX_SUP_BINS` | For Decision Tree:  ``` 2 <= < code>`a number`` <=2147483647< code>` ```  For Random Forest:  ``` 2 <= < code>`a number`` <=254< code>` ``` | This parameter specifies the maximum number of bins for each attribute.  Default value is `32`.  See, DBMS\_DATA\_MINING - Automatic Data Preparation |
| Clustering | `CLUS_NUM_CLUSTERS` | *TO\_CHAR( numeric\_expr* `>=1)` | Maximum number of leaf clusters generated by a clustering algorithm. The algorithm may return fewer clusters, depending on the data.  Enhanced k-Means usually produces the exact number of clusters specified by `CLUS_NUM_CLUSTERS`, unless there are fewer distinct data points.  Expectation Maximization (EM) may return fewer clusters than the number specified by `CLUS_NUM_CLUSTERS` depending on the data. The number of clusters returned by EM cannot be greater than the number of components, which is governed by algorithm-specific settings. (See Expectation Maximization Settings for Learning table) Depending on these settings, there may be fewer clusters than components. If component clustering is disabled, the number of clusters equals the number of components.  For EM, the default value of `CLUS_NUM_CLUSTERS` is system-determined. For k-Means and O-Cluster, the default is `10`. |
| Feature Extraction | `FEAT_NUM_FEATURES` | `TO_CHAR(`*numeric\_expr* `>=1)` | Number of features to be extracted by a feature extraction model.  The default is estimated from the data by the algorithm. If the matrix rank is smaller than this number, fewer features will be returned.  For CUR Matrix Decomposition, the `FEAT_NUM_FEATURES` value is same as the `CURS_SVD_RANK` value. |

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON042) for information about mining functions

### DBMS\_DATA\_MINING - Global Settings

The configuration settings in this table are applicable to any type of model, but are currently only implemented for specific algorithms.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.ODMS_MISSING_VALUE_MEAN_MODE`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'ODMS_MISSING_VALUE_MEAN_MODE'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 8 Global Settings

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Setting Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_ITEM_ID_COLUMN_NAME</code></p></td><td headers="d299446e5120 d299446e5103" width="20%"><p>column_name</p></td><td headers="d299446e5120 d299446e5108" width="20%"><p>column_name</p></td><td headers="d299446e5120 d299446e5113" width="40%"><p>(Association rules only) Name of a column that contains the items in a transaction. When this setting is specified, the algorithm expects the data to be presented in a native transactional format, consisting of two columns:</p><ul><li><p>Case ID, either categorical or numeric</p></li><li><p>Item ID, either categorical or numeric</p></li></ul><p>A typical example of transactional data is market basket data, wherein a case represents a basket that may contain many items. Each item is stored in a separate row, and many rows may be needed to represent a case. The case ID values do not uniquely identify each row. Transactional data is also called multi-record case data.</p><p>Association rules function is normally used with transactional data, but it can also be applied to single-record case data (similar to other algorithms).</p><p>For more information about single-record and multi-record case data, see <a href="https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG006"><cite>Oracle SQL Developer Data Modeler User's Guide</cite></a>.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_ITEM_VALUE_COLUMN_NAME</code></p></td><td headers="d299446e5171 d299446e5103" width="20%"><p>column_name</p></td><td headers="d299446e5171 d299446e5108" width="20%"><p>column_name</p></td><td headers="d299446e5171 d299446e5113" width="40%"><p>(Association rules only) Name of a column that contains a value associated with each item in a transaction. This setting is only used when a value has been specified for <code>ODMS_ITEM_ID_COLUMN_NAME</code> indicating that the data is presented in native transactional format.</p><p>If <code>ASSO_AGGREGATES</code> is used, then the build data must include the following three columns and the columns specified in the AGGREGATES setting.</p><ul><li><p>Case ID, either categorical or numeric</p></li><li><p>Item ID, either categorical or numeric, specified by <code>ODMS_ITEM_ID_COLUMN_NAME</code></p></li><li><p>Item value, either categorical or numeric, specified by <code>ODMS_ITEM_VALUE_COLUMN_NAME</code></p></li></ul>If <code>ASSO_AGGREGATES</code>, Case ID, and Item ID column are present, then the Item Value column may or may not appear.<p>The Item Value column may specify information such as the number of items (for example, three apples) or the type of the item (for example, macintosh apples).</p>For details on <code>ASSO_AGGREGATES</code>, see <a href="https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATA_MINING.html#GUID-CE514371-EC80-41EA-AB07-7F6501687D12">DBMS_DATA_MINING - Mining Function Settings</a>.</td></tr><tr><td headers="d299446e5098" rowspan="3" width="20%"><p><code>ODMS_MISSING_VALUE_TREATMENT</code></p></td><td headers="d299446e5247 d299446e5103" width="20%"><p><code>ODMS_MISSING_VALUE_MEAN_MODE</code></p></td><td headers="d299446e5247 d299446e5108" width="20%"><p><code>ODMS_MISSING_VALUE_MEAN_MODE</code></p></td><td headers="d299446e5247 d299446e5113" width="40%"><p>Indicates how to treat missing values in the training data. This setting does not affect the scoring data. The default value is <code>ODMS_MISSING_VALUE_AUTO</code>.</p><p><code>ODMS_MISSING_VALUE_MEAN_MODE</code> replaces missing values with the mean (numeric attributes) or the mode (categorical attributes) both at build time and apply time where appropriate.</p><p>When <code>ODMS_MISSING_VALUE_TREATMENT</code> is set to <code>ODMS_MISSING_VALUE_DELETE_ROW</code>, the rows in the training data that contain missing values are deleted. However, if you want to replicate this missing value treatment in the scoring data, then you must perform the transformation explicitly.</p></td></tr><tr><td headers="d299446e5247 d299446e5103" width="20%"><p><code>ODMS_MISSING_VALUE_DELETE_ROW</code></p></td><td headers="d299446e5247 d299446e5103" width="20%"><p><code>ODMS_MISSING_VALUE_DELETE_ROW</code></p></td><td headers="d299446e5247 d299446e5108" width="20%"><p>The value <code>ODMS_MISSING_VALUE_DELETE_ROW</code> applies to all algorithms.</p></td></tr><tr><td headers="d299446e5247 d299446e5103" width="20%"><p><code>ODMS_MISSING_VALUE_AUTO</code></p></td><td headers="d299446e5247 d299446e5103" width="20%"><p><code>ODMS_MISSING_VALUE_AUTO</code></p></td><td headers="d299446e5247 d299446e5108" width="20%"><code>ODMS_MISSING_VALUE_AUTO</code> performs different strategies for different algorithms.</td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_ROW_WEIGHT_COLUMN_NAME</code></p></td><td headers="d299446e5327 d299446e5103" width="20%"><p>column_name</p></td><td headers="d299446e5327 d299446e5108" width="20%"><p>column_name</p></td><td headers="d299446e5327 d299446e5113" width="40%"><p>(GLM only) Name of a column in the training data that contains a weighting factor for the rows. The column data type must be NUMBER.</p><p>Row weights can be used as a compact representation of repeated rows, as in the design of experiments where a specific configuration is repeated several times. Row weights can also be used to emphasize certain rows during model construction. For example, to bias the model towards rows that are more recent and away from potentially obsolete data.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_TEXT_POLICY_NAME</code></p></td><td headers="d299446e5354 d299446e5103" width="20%"><p>The name of an Oracle Text POLICY created using <code>CTX_DDL.CREATE_POLICY</code>.</p></td><td headers="d299446e5354 d299446e5108" width="20%"><p>The name of an Oracle Text POLICY created using <code>CTX_DDL.CREATE_POLICY</code>.</p></td><td headers="d299446e5354 d299446e5113" width="40%"><p>Affects how individual tokens are extracted from unstructured text.</p><p>For details about <code>CTX_DDL.CREATE_POLICY</code>, see <a href="https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=CCREF2105">Oracle Text Reference</a>.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_TEXT_MAX_FEATURES</code></p></td><td headers="d299446e5393 d299446e5103" width="20%"><p>1 <= value</p></td><td headers="d299446e5393 d299446e5108" width="20%"><p>1 <= value</p></td><td headers="d299446e5393 d299446e5113" width="40%"><p>The maximum number of distinct features, across all text attributes, to use from a document set passed to <code>CREATE_MODEL</code>. The default is <code>3000</code>. ESA has the default value of <code>300000</code>.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_TEXT_MIN_DOCUMENTS</code></p></td><td headers="d299446e5428 d299446e5103" width="20%"><p>Non-negative value</p></td><td headers="d299446e5428 d299446e5108" width="20%"><p>Non-negative value</p></td><td headers="d299446e5428 d299446e5113" width="40%"><p>This is a text processing setting the controls how in how many documents a token needs to appear to be used as a feature.</p><p>The default is <code>1</code>. ESA has a default of <code>3</code>.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_PARTITION_COLUMNS</code></p></td><td headers="d299446e5459 d299446e5103" width="20%"><p>Comma separated list of data mining attributes</p></td><td headers="d299446e5459 d299446e5108" width="20%"><p>Comma separated list of data mining attributes</p></td><td headers="d299446e5459 d299446e5113" width="40%"><p>This setting indicates a request to build a partitioned model. The setting value is a comma-separated list of the data mining attributes to be used to determine the in-list partition key values. These data mining attributes are taken from the input columns unless an <code>XFORM_LIST</code> parameter is passed to <code>CREATE_MODEL</code>. If the <code>XFORM_LIST</code> parameter is passed to <code>CREATE_MODEL</code>, then the data mining attributes are taken from the attributes produced by these transformations.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_MAX_PARTITIONS</code></p></td><td headers="d299446e5512 d299446e5103" width="20%"><p><code>1< value <= 1000000</code></p></td><td headers="d299446e5512 d299446e5108" width="20%"><p><code>1< value <= 1000000</code></p></td><td headers="d299446e5512 d299446e5113" width="40%"><p>This setting indicates the maximum number of partitions allowed for the model. The default is <code>1000</code>.</p></td></tr><tr><td headers="d299446e5098" rowspan="2" width="20%"><p><code>ODMS_SAMPLING</code></p></td><td headers="d299446e5544 d299446e5103" width="20%"><p><code>ODMS_SAMPLING_ENABLE</code></p></td><td headers="d299446e5544 d299446e5108" width="20%"><p><code>ODMS_SAMPLING_ENABLE</code></p></td><td headers="d299446e5544 d299446e5113" width="40%"><p>This setting allows the user to request a sampling of the build data. The default is <code>ODMS_SAMPLING_DISABLE</code>.</p></td></tr><tr><td headers="d299446e5544 d299446e5103" width="20%"><p><code>ODMS_SAMPLING_DISABLE</code></p></td><td headers="d299446e5544 d299446e5108" width="20%"><p><code>ODMS_SAMPLING_DISABLE</code></p></td><td headers="d299446e5544 d299446e5113" width="40%">Disables sampling of the build data.</td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_SAMPLE_SIZE</code></p></td><td headers="d299446e5592 d299446e5103" width="20%"><p><code>0 < Value</code></p></td><td headers="d299446e5592 d299446e5108" width="20%"><p><code>0 < Value</code></p></td><td headers="d299446e5592 d299446e5113" width="40%"><p>This setting determines how many rows will be sampled (approximately). It can be set only if <code>ODMS_SAMPLING</code> is enabled. The default value is the system determined.</p></td></tr><tr><td headers="d299446e5098" rowspan="3" width="20%"><p><code>ODMS_PARTITION_BUILD_TYPE</code></p></td><td headers="d299446e5621 d299446e5103" width="20%"><p><code>ODMS_PARTITION_BUILD_INTRA</code></p></td><td headers="d299446e5621 d299446e5108" width="20%"><p><code>ODMS_PARTITION_BUILD_INTRA</code></p></td><td headers="d299446e5621 d299446e5113" width="40%"><p>This setting controls the parallel build of partitioned models.</p><p><code>ODMS_PARTITION_BUILD_INTRA</code> - Each partition is built in parallel using all slaves.</p><p>The default mode is <code>ODMS_PARTITION_BUILD_HYBRID</code></p></td></tr><tr><td headers="d299446e5621 d299446e5103" width="20%"><p><code>ODMS_PARTITION_BUILD_INTER</code></p></td><td headers="d299446e5621 d299446e5108" width="20%"><p><code>ODMS_PARTITION_BUILD_INTER</code></p></td><td headers="d299446e5621 d299446e5113" width="40%"><p>Each partition is built entirely in a single slave, but multiple partitions may be built at the same time since multiple slaves are active.</p></td></tr><tr><td headers="d299446e5621 d299446e5103" width="20%"><p><code>ODMS_PARTITION_BUILD_HYBRID</code></p></td><td headers="d299446e5621 d299446e5108" width="20%"><p><code>ODMS_PARTITION_BUILD_HYBRID</code></p></td><td headers="d299446e5621 d299446e5113" width="40%"><p>It is a combination of the other two types and is recommended for most situations to adapt to dynamic environments.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_TABLESPACE_NAME</code></p></td><td headers="d299446e5695 d299446e5103" width="20%"><p><i>tablespace_name</i></p></td><td headers="d299446e5695 d299446e5108" width="20%"><p><i>tablespace_name</i></p></td><td headers="d299446e5695 d299446e5113" width="40%"><p>This setting controls the storage specifications.</p><p>If you explicitly sets this to the name of a tablespace (for which you have sufficient quota), then the specified tablespace storage creates the resulting model content. If you do not provide this setting, then the default tablespace of the user creates the resulting model content.</p></td></tr><tr><td headers="d299446e5098" width="20%"><p><code>ODMS_RANDOM_SEED</code></p></td><td headers="d299446e5725 d299446e5103" width="20%"><p>Non-negative integer</p></td><td headers="d299446e5725 d299446e5108" width="20%"><p>Non-negative integer</p></td><td headers="d299446e5725 d299446e5113" width="40%"><p>The hash function with a random number seed generates a random number with uniform distribution. Users can control the random number seed by this setting. The default is <code>0</code>.</p><p>This setting is used by Random Forest, Neural Network, and CUR Matrix Decomposition.</p></td></tr><tr><td headers="d299446e5098" rowspan="2" width="20%"><p><code>ODMS_DETAILS</code></p></td><td headers="d299446e5755 d299446e5103" width="20%"><p><code>ODMS_ENABLE</code></p></td><td headers="d299446e5755 d299446e5108" width="20%"><p><code>ODMS_ENABLE</code></p></td><td headers="d299446e5755 d299446e5113" width="40%"><p>This setting reduces the space that is used while creating a model, especially a partitioned model. The default value is <code>ODMS_ENABLE</code>.</p><p>When the setting is <code>ODMS_ENABLE</code>, it creates model tables and views when the model is created. You can query the model with SQL.</p><p>The reduction in space depends on the model. Reduction on the order of 10x can be achieved.</p></td></tr><tr><td headers="d299446e5755 d299446e5103" width="20%"><p><code>ODMS_DISABLE</code></p></td><td headers="d299446e5755 d299446e5108" width="20%"><p><code>ODMS_DISABLE</code></p></td><td headers="d299446e5755 d299446e5113" width="40%"><p>When the setting is <code>ODMS_DISABLE</code>, model views are not created and tables relevant to model details are not created either.</p></td></tr></tbody></table>

**See Also:**

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON022) for information about GLM

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON009) for information about Association Rules

[*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG602) for information about mining unstructured text

### DBMS\_DATA\_MINING - Algorithm Settings: ALGO\_EXTENSIBLE\_LANG

The settings listed in the following table configure the behavior of the mining model with an Extensible algorithm. The mining model is built in R language.

The `RALG_*_FUNCTION` specifies the R script that is used to build, score, and view an R model and must be registered in the Oracle R Enterprise script repository. The R scripts are registered through Oracle R Enterprise with special privileges. When `ALGO_EXTENSIBLE_LANG` is set to R in the `MINING_MODEL_SETTING` table, the mining model is built in the R language. After the R model is built, the names of the R scripts are recorded in `MINING_MODEL_SETTING` table in the `SYS` schema. The scripts must exist in the script repository for the R model to function. The amount of R memory used to build, score, and view the R model through these R scripts can be controlled by Oracle R Enterprise.

All algorithm-independent `DBMS_DATA_MINING` subprograms can operate on an R model for mining functions such as Association, Attribute Importance, Classification, Clustering, Feature Extraction, and Regression.

The supported `DBMS_DATA_MINING` subprograms include, but are not limited, to the following:

- ADD\_COST\_MATRIX Procedure
- COMPUTE\_CONFUSION\_MATRIX Procedure
- COMPUTE\_LIFT Procedure
- COMPUTE\_ROC Procedure
- CREATE\_MODEL Procedure
- DROP\_MODEL Procedure
- EXPORT\_MODEL Procedure
- GET\_MODEL\_COST\_MATRIX Function
- IMPORT\_MODEL Procedure
- REMOVE\_COST\_MATRIX Procedure
- RENAME\_MODEL Procedure

Table 9 ALGO\_EXTENSIBLE\_LANG Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `RALG_BUILD_FUNCTION` | `R_BUILD_FUNCTION_SCRIPT_NAME` | Specifies the name of an existing registered R script for R algorithm mining model build function. The R script defines an R function for the first input argument for training data and returns an R model object. For Clustering and Feature Extraction mining function model build, the R attributes dm$nclus and dm$nfeat must be set on the R model to indicate the number of clusters and features respectively. The `RALG_BUILD_FUNCTION` must be set along with `ALGO_EXTENSIBLE_LANG` in the `model_setting_table`. |
| `RALG_BUILD_PARAMETER` | `SELECT` *value* param\_name, … `FROM DUAL` | Specifies a list of numeric and string scalar for optional input parameters of the model build function. |
| `RALG_SCORE_FUNCTION` | `R_SCORE_FUNCTION_SCRIPT_NAME` | Specifies the name of an existing registered R script to score data. The script returns a `data.frame` containing the corresponding prediction results. The setting is used to score data for mining functions such as Regression, Classification, Clustering, and Feature Extraction. This setting does not apply to Association and Attribute Importance functions |
| `RALG_WEIGHT_FUNCTION` | `R_WEIGHT_FUNCTION_SCRIPT_NAME` | Specifies the name of an existing registered R script for R algorithm that computes the weight (contribution) for each attribute in scoring. The script returns a `data.frame` containing the contributing weight for each attribute in a row. This function setting is needed for `PREDICTION_DETAILS` SQL function. |
| `RALG_DETAILS_FUNCTION` | `R_DETAILS_FUNCTION_SCRIPT_NAME` | Specifies the name of an existing registered R script for R algorithm that produces the model information. This setting is required to generate a model view. |
| `RALG_DETAILS_FORMAT` | `SELECT` *type\_value* *column\_name*, … `FROM DUAL` | Specifies the `SELECT` query for the list of numeric and string scalars for the output column type and the column name of the generated model view. This setting is required to generate a model view. |

**See Also:** [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-DCD47B08-1703-4789-B87D-96760A7726F9)

### DBMS\_DATA\_MINING - Algorithm Settings: CUR Matrix Decomposition

The following settings configure the behavior of the CUR Matrix Decomposition algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.CURS_ROW_IMP_DISABLE`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'CURS_ROW_IMP_DISABLE'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 10 CUR Matrix Decomposition

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e6851" width="20%"><p><code>CURS_APPROX_ATTR_NUM</code></p></td><td headers="d299446e6873 d299446e6856" width="20%"><p>The value must be a positive integer</p></td><td headers="d299446e6873 d299446e6861" width="20%"><p>The value must be a positive integer</p></td><td headers="d299446e6873 d299446e6866" width="40%"><p>Defines the approximate number of attributes to be selected.</p><p>The default value is the number of attributes.</p></td></tr><tr><td headers="d299446e6851" rowspan="2" width="20%"><p><code>CURS_ROW_IMPORTANCE</code></p></td><td headers="d299446e6898 d299446e6856" width="20%"><p><code>CURS_ROW_IMP_ENABLE</code></p></td><td headers="d299446e6898 d299446e6861" width="20%"><p><code>CURS_ROW_IMP_ENABLE</code></p></td><td headers="d299446e6898 d299446e6866" width="40%"><p>Defines the flag indicating whether or not to perform row selection.</p><p>Enables row selection.</p><p>The default value is <code>CURS_ROW_IMP_DISABLE</code>.</p></td></tr><tr><td headers="d299446e6898 d299446e6856" width="20%"><p><code>CURS_ROW_IMP_DISABLE</code></p></td><td headers="d299446e6898 d299446e6856" width="20%"><p><code>CURS_ROW_IMP_DISABLE</code></p></td><td headers="d299446e6898 d299446e6861" width="20%"><p>Disables row selection.</p></td><td headers="d299446e6898 d299446e6866" width="40%"></td></tr><tr><td headers="d299446e6851" width="20%"><p><code>CURS_APPROX_ROW_NUM </code></p></td><td headers="d299446e6950 d299446e6856" width="20%"><p>The value must be a positive integer</p></td><td headers="d299446e6950 d299446e6861" width="20%"><p>The value must be a positive integer</p></td><td headers="d299446e6950 d299446e6866" width="40%"><p>Defines the approximate number of rows to be selected. This parameter is only used when users decide to perform row selection (<code>CURS_ROW_IMP_ENABLE</code>).</p><p>The default value is the total number of rows.</p></td></tr><tr><td headers="d299446e6851" width="20%"><p><code>CURS_SVD_RANK</code></p></td><td headers="d299446e6978 d299446e6856" width="20%"><p>The value must be a positive integer</p></td><td headers="d299446e6978 d299446e6861" width="20%"><p>The value must be a positive integer</p></td><td headers="d299446e6978 d299446e6866" width="40%"><p>Defines the rank parameter used in the column/row leverage score calculation.</p><p>If users do not provide an input value, the value is determined by the system.</p></td></tr></tbody></table>

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-EABE920F-1196-49C0-89CD-F25E062E16EF)

### DBMS\_DATA\_MINING - Algorithm Settings: Decision Tree

These settings configure the behavior of the Decision Tree algorithm. Note that the Decision Tree settings are also used to configure the behavior of Random Forest as it constructs each individual Decision Tree.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.TREE_IMPURITY_ENTROPY`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'TREE_IMPURITY_ENTROPY'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 11 Decision Tree Settings

<table width="100%"><thead><tr><th width="25%">Setting Name</th><th width="26%">Constant Value</th><th>String Value Equivalent</th><th width="49%">Description</th></tr></thead><tbody><tr><td headers="d299446e7450" rowspan="2" width="25%"><p><code>TREE_IMPURITY_METRIC</code></p></td><td headers="d299446e7472 d299446e7455" width="26%"><p><code>TREE_IMPURITY_ENTROPY</code></p></td><td headers="d299446e7472 d299446e7460"><p><code>TREE_IMPURITY_ENTROPY</code></p></td><td headers="d299446e7472 d299446e7465" width="49%"><p>Tree impurity metric for Decision Tree.</p><p>Tree algorithms seek the best test question for splitting data at each node. The best splitter and split values are those that result in the largest increase in target value homogeneity (purity) for the entities in the node. Purity is by a metric. By default, the algorithm uses <code>TREE_IMPURITY_GINI</code>.</p></td></tr><tr><td headers="d299446e7472 d299446e7455" width="26%"><p><code>TREE_IMPURITY_GINI</code></p></td><td headers="d299446e7472 d299446e7455" width="26%"><p><code>TREE_IMPURITY_GINI</code></p></td><td headers="d299446e7472 d299446e7460"><p>Decision trees can use either Gini (<code>TREE_IMPURITY_GINI</code>) or entropy (<code>TREE_IMPURITY_ENTROPY</code>) as the purity metric.</p></td></tr><tr><td headers="d299446e7450" width="25%"><p><code>TREE_TERM_MAX_DEPTH</code></p></td><td headers="d299446e7526 d299446e7455" width="26%"><p>For Decision Tree:</p><p><code>2<=</code> <code> a
                                    number</code> <code> <=20</code></p><p>For Random Forest:</p><p><code>2<=</code> <code> a
                                    number</code> <code> <=100</code></p></td><td headers="d299446e7526 d299446e7460"><p>For Decision Tree:</p><p><code>2<=</code> <code> a
                                    number</code> <code> <=20</code></p><p>For Random Forest:</p><p><code>2<=</code> <code> a
                                    number</code> <code> <=100</code></p></td><td headers="d299446e7526 d299446e7465" width="49%"><p>Criteria for splits: maximum tree depth (the maximum number of nodes between the root and any leaf node, including the leaf node).</p><p>For Decision Tree, the default is <code>7</code>.</p><p>For Random Forest, the default is <code>16</code>.</p></td></tr><tr><td headers="d299446e7450" width="25%"><p><code>TREE_TERM_MINPCT_NODE</code></p></td><td headers="d299446e7603 d299446e7455" width="26%"><p><code>0<=</code> <code> a
                                    number</code> <code><=10</code></p></td><td headers="d299446e7603 d299446e7460"><p><code>0<=</code> <code> a
                                    number</code> <code><=10</code></p></td><td headers="d299446e7603 d299446e7465" width="49%"><p>The minimum number of training rows in a node expressed as a percentage of the rows in the training data.</p><p>Default is <code>
0.05</code>, indicating 0.05%.</p></td></tr><tr><td headers="d299446e7450" width="25%"><p><code>TREE_TERM_MINPCT_SPLIT</code></p></td><td headers="d299446e7643 d299446e7455" width="26%"><p><code>0 < </code> <code>a
                                    number</code> <code> <=20</code></p></td><td headers="d299446e7643 d299446e7460"><p><code>0 < </code> <code>a
                                    number</code> <code> <=20</code></p></td><td headers="d299446e7643 d299446e7465" width="49%"><p>The minimum number of rows required to consider splitting a node expressed as a percentage of the training rows.</p><p>Default is <code>0.1</code>, indicating 0.1%.</p></td></tr><tr><td headers="d299446e7450" width="25%"><p><code>TREE_TERM_MINREC_NODE</code></p></td><td headers="d299446e7683 d299446e7455" width="26%"><p><code> a
                                    number</code> <code>>=0</code></p></td><td headers="d299446e7683 d299446e7460"><p><code> a
                                    number</code> <code>>=0</code></p></td><td headers="d299446e7683 d299446e7465" width="49%"><p>The minimum number of rows in a node.</p><p>Default is <code>10</code>.</p></td></tr><tr><td headers="d299446e7450" width="25%"><p><code>TREE_TERM_MINREC_SPLIT</code></p></td><td headers="d299446e7721 d299446e7455" width="26%"><p><code>a number</code> <code> > 1</code></p></td><td headers="d299446e7721 d299446e7460"><p><code>a number</code> <code> > 1</code></p></td><td headers="d299446e7721 d299446e7465" width="49%"><p>Criteria for splits: minimum number of records in a parent node expressed as a value. No split is attempted if the number of records is below this value.</p><p>Default is <code>20</code>.</p></td></tr></tbody></table>

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON019) for information about Decision Tree

### DBMS\_DATA\_MINING - Algorithm Settings: Expectation Maximization

These algorithm settings configure the behavior of the Expectation Maximization algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.EMCS_ATTR_FILTER_ENABLE`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'EMCS_ATTR_FILTER_ENABLE'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON590) for information about Expectation Maximization

Table 12 Expectation Maximization Settings for Data

<table width="100%"><thead><tr><th width="27%">Setting Name</th><th width="25%">Constant Value</th><th>String Value Equivalent</th><th width="49%">Description</th></tr></thead><tbody><tr><td headers="d299446e8211" rowspan="2" width="27%"><p><code>EMCS_ATTRIBUTE_FILTER</code></p></td><td headers="d299446e8233 d299446e8216" width="25%"><p><code>EMCS_ATTR_FILTER_ENABLE</code></p></td><td headers="d299446e8233 d299446e8221"><p><code>EMCS_ATTR_FILTER_ENABLE</code></p></td><td headers="d299446e8233 d299446e8226" width="49%"><p>Whether or not to include uncorrelated attributes in the model. When <code>EMCS_ATTRIBUTE_FILTER</code> is enabled, uncorrelated attributes are not included.</p><p>Note:</p><p>This setting applies only to attributes that are not nested.</p><p>Default is system-determined.</p></td></tr><tr><td headers="d299446e8233 d299446e8216" width="25%"><p><code>EMCS_ATTR_FILTER_DISABLE</code></p></td><td headers="d299446e8233 d299446e8216" width="25%"><p><code>EMCS_ATTR_FILTER_DISABLE</code></p></td><td headers="d299446e8233 d299446e8221"><p>Includes uncorrelated attributes in the model.</p></td></tr><tr><td headers="d299446e8211" width="27%"><p><code>EMCS_MAX_NUM_ATTR_2D</code></p></td><td headers="d299446e8290 d299446e8216" width="25%"><p><code>TO_CHAR</code> (<code>
                                                  numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e8290 d299446e8221"><p><code>TO_CHAR</code> (<code>
                                                  numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e8290 d299446e8226" width="49%"><p>Maximum number of correlated attributes to include in the model.</p><p>Note: This setting applies only to attributes that are not nested (2D).</p><p>Default is <code>50</code>.</p></td></tr><tr><td headers="d299446e8211" rowspan="3" width="27%"><p><code>EMCS_NUM_DISTRIBUTION</code></p></td><td headers="d299446e8337 d299446e8216" width="25%"><p><code>EMCS_NUM_DISTR_BERNOULLI</code></p></td><td headers="d299446e8337 d299446e8221"><p><code>EMCS_NUM_DISTR_BERNOULLI</code></p></td><td headers="d299446e8337 d299446e8226" width="49%"><p>The distribution for modeling numeric attributes. Applies to the input table or view as a whole and does not allow per-attribute specifications.</p><p>The options include Bernoulli, Gaussian, or system-determined distribution. When Bernoulli or Gaussian distribution is chosen, all numeric attributes are modeled using the same type of distribution.</p><p>Default is <code>EMCS_NUM_DISTR_SYSTEM</code>.</p></td></tr><tr><td headers="d299446e8337 d299446e8216" width="25%"><p><code>EMCS_NUM_DISTR_GAUSSIAN</code></p></td><td headers="d299446e8337 d299446e8216" width="25%"><p><code>EMCS_NUM_DISTR_GAUSSIAN</code></p></td><td headers="d299446e8337 d299446e8221"><p>Models all numeric attributes using Gaussian distribution.</p></td></tr><tr><td headers="d299446e8337 d299446e8216" width="25%"><p><code>EMCS_NUM_DISTR_SYSTEM</code></p></td><td headers="d299446e8337 d299446e8216" width="25%"><p><code>EMCS_NUM_DISTR_SYSTEM</code></p></td><td headers="d299446e8337 d299446e8221"><p>When the distribution is system-determined, individual attributes may use different distributions (either Bernoulli or Gaussian), depending on the data.</p></td></tr><tr><td headers="d299446e8211" width="27%"><p><code>EMCS_NUM_EQUIWIDTH_BINS</code></p></td><td headers="d299446e8409 d299446e8216" width="25%"><p><code>TO_CHAR</code> ( 1 < <code>numeric_expr</code> <code><=255)</code></p></td><td headers="d299446e8409 d299446e8221"><p><code>TO_CHAR</code> ( 1 < <code>numeric_expr</code> <code><=255)</code></p></td><td headers="d299446e8409 d299446e8226" width="49%"><p>Number of equi-width bins that will be used for gathering cluster statistics for numeric columns.</p><p>Default is <code>11</code>.</p></td></tr><tr><td headers="d299446e8211" width="27%"><p><code>EMCS_NUM_PROJECTIONS</code></p></td><td headers="d299446e8453 d299446e8216" width="25%"><p><code>TO_CHAR</code> ( <code>numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e8453 d299446e8221"><p><code>TO_CHAR</code> ( <code>numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e8453 d299446e8226" width="49%"><p>Specifies the number of projections that will be used for each nested column. If a column has fewer distinct attributes than the specified number of projections, the data will not be projected. The setting applies to all nested columns.</p><p>Default is <code>50</code>.</p></td></tr><tr><td headers="d299446e8211" width="27%"><p><code>EMCS_NUM_QUANTILE_BINS</code></p></td><td headers="d299446e8497 d299446e8216" width="25%"><p><code>TO_CHAR</code> ( 1 < <code>numeric_expr</code> <code><=255)</code></p></td><td headers="d299446e8497 d299446e8221"><p><code>TO_CHAR</code> ( 1 < <code>numeric_expr</code> <code><=255)</code></p></td><td headers="d299446e8497 d299446e8226" width="49%"><p>Specifies the number of quantile bins that will be used for modeling numeric columns with multivalued Bernoulli distributions.</p><p>Default is system-determined.</p></td></tr><tr><td headers="d299446e8211" width="27%"><p><code>EMCS_NUM_TOPN_BINS</code></p></td><td headers="d299446e8538 d299446e8216" width="25%"><p><code>TO_CHAR</code> ( 1 < <code>numeric_expr</code> <code><=255)</code></p></td><td headers="d299446e8538 d299446e8221"><p><code>TO_CHAR</code> ( 1 < <code>numeric_expr</code> <code><=255)</code></p></td><td headers="d299446e8538 d299446e8226" width="49%"><p>Specifies the number of top-N bins that will be used for modeling categorical columns with multivalued Bernoulli distributions.</p><p>Default is system-determined.</p></td></tr></tbody></table>

Table 13 Expectation Maximization Settings for

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e8590" rowspan="2" width="20%"><p><code>EMCS_CONVERGENCE_CRITERION</code></p></td><td headers="d299446e8612 d299446e8595" width="20%"><p><code>EMCS_CONV_CRIT_HELDASIDE</code></p></td><td headers="d299446e8612 d299446e8600" width="20%"><p><code>EMCS_CONV_CRIT_HELDASIDE</code></p></td><td headers="d299446e8612 d299446e8605" width="40%"><p>The convergence criterion for EM. The convergence criterion may be based on a held-aside data set, or it may be Bayesian Information Criterion.</p><p><code>EMCS_CONV_CRIT_HELDASIDE</code>: Uses a held-aside data set for convergence criterion.</p><p>Default is system determined.</p></td></tr><tr><td headers="d299446e8612 d299446e8595" width="20%"><p><code>EMCS_CONV_CRIT_BIC</code></p></td><td headers="d299446e8612 d299446e8595" width="20%"><p><code>EMCS_CONV_CRIT_BIC</code></p></td><td headers="d299446e8612 d299446e8600" width="20%"><p>Uses the Bayesian Information Criterion (BIC) for convergence.</p></td></tr><tr><td headers="d299446e8590" width="20%"><p><code>EMCS_LOGLIKE_IMPROVEMENT</code></p></td><td headers="d299446e8667 d299446e8595" width="20%"><p><code>TO_CHAR( 0 <
                                                  </code> <code>numeric_expr</code> <code>
                                                  < 1)</code></p></td><td headers="d299446e8667 d299446e8600" width="20%"><p><code>TO_CHAR( 0 <
                                                  </code> <code>numeric_expr</code> <code>
                                                  < 1)</code></p></td><td headers="d299446e8667 d299446e8605" width="40%"><p>When the convergence criterion is based on a held-aside data set (<code>EMCS_CONVERGENCE_CRITERION</code> = <code>EMCS_CONV_CRIT_HELDASIDE</code>), this setting specifies the percentage improvement in the value of the log likelihood function that is required for adding a new component to the model.</p><p>Default value is <code>
0.001</code>.</p></td></tr><tr><td headers="d299446e8590" width="20%"><p><code>EMCS_NUM_COMPONENTS</code></p></td><td headers="d299446e8713 d299446e8595" width="20%"><p><code>TO_CHAR</code> ( <code>numeric_expr</code> <code>>=1</code>)</p></td><td headers="d299446e8713 d299446e8600" width="20%"><p><code>TO_CHAR</code> ( <code>numeric_expr</code> <code>>=1</code>)</p></td><td headers="d299446e8713 d299446e8605" width="40%"><p>Maximum number of components in the model. If model search is enabled, the algorithm automatically determines the number of components based on improvements in the likelihood function or based on regularization, up to the specified maximum.</p><p>The number of components must be greater than or equal to the number of clusters.</p><p>Default is 20.</p></td></tr><tr><td headers="d299446e8590" width="20%"><p><code>EMCS_NUM_ITERATIONS</code></p></td><td headers="d299446e8760 d299446e8595" width="20%"><p><code>TO_CHAR</code> ( <code>numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e8760 d299446e8600" width="20%"><p><code>TO_CHAR</code> ( <code>numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e8760 d299446e8605" width="40%"><p>Specifies the maximum number of iterations in the EM algorithm.</p><p>Default is <code>100</code>.</p></td></tr><tr><td headers="d299446e8590" rowspan="2" width="20%"><p><code>EMCS_MODEL_SEARCH</code></p></td><td headers="d299446e8804 d299446e8595" width="20%"><p><code>EMCS_MODEL_SEARCH_ENABLE</code></p></td><td headers="d299446e8804 d299446e8600" width="20%"><p><code>EMCS_MODEL_SEARCH_ENABLE</code></p></td><td headers="d299446e8804 d299446e8605" width="40%"><p>This setting enables model search in EM where different model sizes are explored and a best size is selected.</p><p>The default is <code>EMCS_MODEL_SEARCH_DISABLE</code>.</p></td></tr><tr><td headers="d299446e8804 d299446e8595" width="20%"><p><code>EMCS_MODEL_SEARCH_DISABLE</code> (default).</p></td><td headers="d299446e8804 d299446e8600" width="20%"><p><code>EMCS_MODEL_SEARCH_DISABLE</code> (default).</p></td><td headers="d299446e8804 d299446e8605" width="40%"><p>Deactivates model search.</p></td></tr><tr><td headers="d299446e8590" rowspan="2" width="20%"><p><code>EMCS_REMOVE_COMPONENTS</code></p></td><td headers="d299446e8856 d299446e8595" width="20%"><p><code>EMCS_REMOVE_COMPS_ENABLE</code> (default)</p></td><td headers="d299446e8856 d299446e8600" width="20%"><p><code>EMCS_REMOVE_COMPS_ENABLE</code> (default)</p></td><td headers="d299446e8856 d299446e8605" width="40%"><p>This setting allows the EM algorithm to remove a small component from the solution.</p><p>The default is <code>EMCS_REMOVE_COMPS_ENABLE</code>.</p></td></tr><tr><td headers="d299446e8856 d299446e8595" width="20%"><p><code>EMCS_REMOVE_COMPS_DISABLE</code></p></td><td headers="d299446e8856 d299446e8600" width="20%"><p><code>EMCS_REMOVE_COMPS_DISABLE</code></p></td><td headers="d299446e8856 d299446e8605" width="40%"><p>Prevents the EM algorithm from removing small components.</p></td></tr><tr><td headers="d299446e8590" width="20%"><p><code>EMCS_RANDOM_SEED</code></p></td><td headers="d299446e8908 d299446e8595" width="20%"><p>Non-negative integer</p></td><td headers="d299446e8908 d299446e8600" width="20%"><p>Non-negative integer</p></td><td headers="d299446e8908 d299446e8605" width="40%"><p>This setting controls the seed of the random generator used in EM. The default is <code>0</code>.</p></td></tr></tbody></table>

Table 14 Expectation Maximization Settings for Component

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e8945" rowspan="2" width="20%"><p><code>EMCS_CLUSTER_COMPONENTS</code></p></td><td headers="d299446e8967 d299446e8950" width="20%"><p><code>EMCS_CLUSTER_COMP_ENABLE</code></p></td><td headers="d299446e8967 d299446e8955" width="20%"><p><code>EMCS_CLUSTER_COMP_ENABLE</code></p></td><td headers="d299446e8967 d299446e8960" width="40%"><p>Enables or disables the grouping of EM components into high-level clusters. When disabled, the components themselves are treated as clusters.</p><p>When component clustering is enabled, model scoring through the SQL <code>CLUSTER</code> function will produce assignments to the higher level clusters.</p><p>Default is <code>EMCS_CLUSTER_COMP_ENABLE</code>.</p></td></tr><tr><td headers="d299446e8967 d299446e8950" width="20%"><p><code>EMCS_CLUSTER_COMP_DISABLE</code></p></td><td headers="d299446e8967 d299446e8950" width="20%"><p><code>EMCS_CLUSTER_COMP_DISABLE</code></p></td><td headers="d299446e8967 d299446e8955" width="20%"><p>When clustering is disabled, the <code>CLUSTER</code> function will produce assignments to the original components.</p></td></tr><tr><td headers="d299446e8945" width="20%"><p><code>EMCS_CLUSTER_THRESH</code></p></td><td headers="d299446e9024 d299446e8950" width="20%"><p><code>TO_CHAR</code> (<code>
                                                  numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e9024 d299446e8955" width="20%"><p><code>TO_CHAR</code> (<code>
                                                  numeric_expr</code> <code>>=1)</code></p></td><td headers="d299446e9024 d299446e8960" width="40%"><p>Dissimilarity threshold that controls the clustering of EM components. When the dissimilarity measure is less than the threshold, the components are combined into a single cluster.</p><p>A lower threshold may produce more clusters that are more compact. A higher threshold may produce fewer clusters that are more spread out.</p><p>Default is <code>2</code>.</p></td></tr><tr><td headers="d299446e8945" rowspan="3" width="20%"><p><code>EMCS_LINKAGE_FUNCTION</code></p></td><td headers="d299446e9071 d299446e8950" width="20%"><p><code>EMCS_LINKAGE_SINGLE</code></p></td><td headers="d299446e9071 d299446e8955" width="20%"><p><code>EMCS_LINKAGE_SINGLE</code></p></td><td headers="d299446e9071 d299446e8960" width="40%"><p>Allows the specification of a linkage function for the agglomerative clustering step.</p><p><code>EMCS_LINKAGE_SINGLE</code> uses the nearest distance within the branch. The clusters tend to be larger and have arbitrary shapes.</p><p>Default is <code>EMCS_LINKAGE_SINGLE</code>.</p></td></tr><tr><td headers="d299446e9071 d299446e8950" width="20%"><p><code>EMCS_LINKAGE_AVERAGE</code></p></td><td headers="d299446e9071 d299446e8950" width="20%"><p><code>EMCS_LINKAGE_AVERAGE</code></p></td><td headers="d299446e9071 d299446e8955" width="20%"><p><code>EMCS_LINKAGE_AVERAGE</code> uses the average distance within the branch. There is less chaining effect and the clusters are more compact.</p></td></tr><tr><td headers="d299446e9071 d299446e8950" width="20%"><p><code>EMCS_LINKAGE_COMPLETE</code></p></td><td headers="d299446e9071 d299446e8950" width="20%"><p><code>EMCS_LINKAGE_COMPLETE</code></p></td><td headers="d299446e9071 d299446e8955" width="20%"><p><code>EMCS_LINKAGE_COMPLETE</code> uses the maximum distance within the branch. The clusters are smaller and require strong component overlap.</p></td></tr></tbody></table>

Table 15 Expectation Maximization Settings for Cluster

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalents</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e9157" rowspan="2" width="20%"><p><code>EMCS_CLUSTER_STATISTICS</code></p></td><td headers="d299446e9179 d299446e9162" width="20%"><p><code>EMCS_CLUS_STATS_ENABLE</code></p></td><td headers="d299446e9179 d299446e9167" width="20%"><p><code>EMCS_CLUS_STATS_ENABLE</code></p></td><td headers="d299446e9179 d299446e9172" width="40%"><p>Enables or disables the gathering of descriptive statistics for clusters (centroids, histograms, and rules).</p><p>Default is <code>EMCS_CLUS_STATS_ENABLE</code>.</p></td></tr><tr><td headers="d299446e9179 d299446e9162" width="20%"><p><code>EMCS_CLUS_STATS_DISABLE</code></p></td><td headers="d299446e9179 d299446e9162" width="20%"><p><code>EMCS_CLUS_STATS_DISABLE</code></p></td><td headers="d299446e9179 d299446e9167" width="20%"><p>When statistics are disabled, model size is reduced, and <code>GET_MODEL_DETAILS_EM</code> only returns taxonomy (hierarchy) and cluster counts.</p></td></tr><tr><td headers="d299446e9157" width="20%"><p><code>EMCS_MIN_PCT_ATTR_SUPPORT</code></p></td><td headers="d299446e9230 d299446e9162" width="20%"><p><code>TO_CHAR( 0 <
                                                  </code> <code>numeric_expr</code> <code>
                                                  < 1)</code></p></td><td headers="d299446e9230 d299446e9167" width="20%"><p><code>TO_CHAR( 0 <
                                                  </code> <code>numeric_expr</code> <code>
                                                  < 1)</code></p></td><td headers="d299446e9230 d299446e9172" width="40%"><p>Minimum support required for including an attribute in the cluster rule. The support is the percentage of the data rows assigned to a cluster that must have non-null values for the attribute.</p><p>Default is <code>0.1</code>.</p></td></tr></tbody></table>

### DBMS\_DATA\_MINING - Algorithm Settings: Explicit Semantic Analysis

Explicit Semantic Analysis (ESA) is a useful technique for extracting meaningful and interpretable features.

The settings listed in the following table configure the ESA values.

Table 16 Explicit Semantic Analysis

| Setting Name | Constant Value | String Value Equivalent | Description |
| --- | --- | --- | --- |
| `ESAS_VALUE_THRESHOLD` | Non-negative number | Non-negative number | This setting thresholds a small value for attribute weights in the transformed build data. The default is `1e-8`. |
| `ESAS_MIN_ITEMS` | Text input `100`  Non-text input is `0` | Text input `100`  Non-text input is `0` | This setting determines the minimum number of non-zero entries that need to be present in an input row. The default is 100 for text input and 0 for non-text input. |
| `ESAS_TOPN_FEATURES` | A positive integer | A positive integer | This setting controls the maximum number of features per attribute. The default is `1000`.   Oracle Data Mining validates the `ESAS_TOPN_FEATURES` setting before allocating internal buffers during model creation. Oversized values are rejected during validation. |

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-7DC30272-E234-4C7C-B7D2-29D0E5448BA6) for information about ESA.

### DBMS\_DATA\_MINING - Algorithm Settings: Exponential Smoothing

These settings configure the behavior of the Exponential Smoothing (ESM) algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.EXSM_SIMPLE`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'EXSM_SIMPLE'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

The settings listed in the following table configure Exponential Smoothing values.

Table 17 Exponential Smoothing

<table><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e10194" rowspan="14" width="20%"><code>EXSM_MODEL</code></td><td headers="d299446e10204 d299446e10196" width="20%"><p><code>EXSM_SIMPLE</code></p></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_SIMPLE</code></td><td headers="d299446e10204 d299446e10200" width="40%"><p>This setting specifies the model.</p><p><code>EXSM_SIMPLE</code>: Forecasts data as a weighted moving average, with the influence of past observations declining exponentially with the length of time since the observation occurred. Errors in estimation are assumed to be normally distributed, with constant mean and variance. It is appropriate for data with no clear trend or seasonal pattern.</p><p>The default value is <code>EXSM_SIMPLE</code>.</p></td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_SIMPLE_MULT</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_SIMPLE_MULT_ERR</code></td><td headers="d299446e10204 d299446e10200" width="40%">Forecasts data as a weighted moving average, with the influence of past observations declining exponentially with the length of time since the observation occurred. Errors in estimation are assumed to be proportional to the level of the prior estimate.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_HOLT</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_HOLT</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies Holt's linear exponential smoothing method, designed to forecast data with an underlying linear trend.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_HOLT_DMP</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_HOLT_DAMPED</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies Holt's linear exponential smoothing with a damping factor to progressively reduce the strength of the trend over time.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_MUL_TRND</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_MULT_TREND</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies an exponential smoothing framework with a multiplicative trend component, effectively capturing data where trends are not linear but grow or decay over time.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_MULTRD_DMP</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_MULT_TREND_DAMPED</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies an exponential smoothing algorithm with a multiplicative trend that diminishes over time, providing a conservative approach to trend estimation.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_SEAS_ADD</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_SEASON_ADD</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies an exponential smoothing with an additive seasonal component, isolating and accounting for seasonal variations without incorporating a trend.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_SEAS_MUL</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_SEASON_MUL</code></td><td headers="d299446e10204 d299446e10200" width="40%">Executes exponential smoothing with a multiplicative seasonal component, capturing seasonal effects that increase or decrease in proportion to the level of the series.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_HW</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_WINTERS</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies the Holt-Winters method with additive trends and multiplicative seasonality, offering a robust model for data with both linear trend and proportional seasonal variation.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_HW_DMP</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_WINTERS_DAMPED</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies the Holt-Winters method with a damped trend and multiplicative seasonality, moderating the linear trend over time while still capturing proportional seasonal changes.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_HW_ADDSEA</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_ADDWINTERS</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies the Holt-Winters additive model to simultaneously smooth data with linear trends and additive seasonal effects.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_DHW_ADDSEA</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_ADDWINTERS_DAMPED</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies the Holt-Winters additive approach with a damping mechanism, reducing the impact of the trend and seasonal components over time.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_HWMT</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_WINTERS_MULT_TREND</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies the Holt-Winters model with both trend and seasonality components being multiplicative, suited for series where the seasonal variations and trends are both increasing or decreasing proportional to level.</td></tr><tr><td headers="d299446e10204 d299446e10196" width="20%"><code>EXSM_HWMT_DMP</code></td><td headers="d299446e10204 d299446e10198" width="20%"><code>EXSM_WINTERS_MUL_TREND_DMP</code></td><td headers="d299446e10204 d299446e10200" width="40%">Applies the Holt-Winters model with a damped multiplicative trend, effectively moderating the exponential increase or decrease of both trend and seasonal components over time.</td></tr><tr><td headers="d299446e10194" width="20%"><code>EXSM_SEASONALITY</code></td><td headers="d299446e10351 d299446e10196" width="20%"><code>positive integer > 1</code></td><td headers="d299446e10351 d299446e10198" width="20%"><code>positive integer > 1</code></td><td headers="d299446e10351 d299446e10200" width="40%"><p>This setting specifies a positive integer value as the length of seasonal cycle.</p><p>The value it takes must be larger than <code>1</code>. For example, setting value <code>4</code> means that every group of four observations forms a seasonal cycle.</p><p>This setting is only applicable and must be provided for models with seasonality, otherwise the model throws an error.</p><p>When <code>EXSM_INTERVAL</code> is not set, this setting applies to the original input time series. When <code>EXSM_INTERVAL</code> is set, this setting applies to the accumulated time series.</p></td></tr><tr><td headers="d299446e10194" rowspan="8" width="20%"><code>EXSM_INTERVAL</code></td><td headers="d299446e10387 d299446e10196" width="20%"><p><code>EXSM_INTERVAL_YEAR</code></p></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_YEAR</code></td><td headers="d299446e10387 d299446e10200" width="40%"><p>This setting only applies and must be provided when the time column (<code>case_id</code> column) has datetime type. It specifies the spacing interval of the accumulated equally spaced time series.</p><p>The model throws an error if the time column of input table is of datetime type and setting <code>EXSM_INTERVAL</code> is not provided.</p><p><code>EXSM_INTERVAL_YEAR</code>: This option sets the spacing interval of the accumulated time series to one year. When selected, the data is aggregated or summarized on a yearly basis.</p></td></tr><tr><td headers="d299446e10387 d299446e10196" width="20%"><code>EXSM_INTERVAL_QTR</code></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_QTR</code></td><td headers="d299446e10387 d299446e10200" width="40%">This option sets the spacing interval to a quarter, aggregating the data for every three months.</td></tr><tr><td headers="d299446e10387 d299446e10196" width="20%"><code>EXSM_INTERVAL_MONTH</code></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_MONTH</code></td><td headers="d299446e10387 d299446e10200" width="40%">This option adjusts the spacing interval to one month. The accumulated time series represent aggregated or summarized data for each month.</td></tr><tr><td headers="d299446e10387 d299446e10196" width="20%"><code>EXSM_INTERVAL_WEEK</code></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_WEEK</code></td><td headers="d299446e10387 d299446e10200" width="40%">With this option data is aggregated or summarized on a weekly basis, setting the spacing interval to one week.</td></tr><tr><td headers="d299446e10387 d299446e10196" width="20%"><code>EXSM_INTERVAL_DAY</code></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_DAY</code></td><td headers="d299446e10387 d299446e10200" width="40%">This option adjusts the spacing interval to one day. It's suitable for scenarios where daily aggregated insights are required.</td></tr><tr><td headers="d299446e10387 d299446e10196" width="20%"><code>EXSM_INTERVAL_HOUR</code></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_HOUR</code></td><td headers="d299446e10387 d299446e10200" width="40%">For more granular insights, this option sets the spacing interval to one hour. It's especially useful when analyzing data that changes significantly within a day.</td></tr><tr><td headers="d299446e10387 d299446e10196" width="20%"><code>EXSM_INTERVAL_MIN</code></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_MINUTE</code></td><td headers="d299446e10387 d299446e10200" width="40%">With this option the spacing is set to one minute. This provides a very detailed view of data, suitable for applications like high-frequency trading or real-time monitoring systems.</td></tr><tr><td headers="d299446e10387 d299446e10196" width="20%"><code>EXSM_INTERVAL_SEC</code></td><td headers="d299446e10387 d299446e10198" width="20%"><code>EXSM_INTERVAL_SECOND</code></td><td headers="d299446e10387 d299446e10200" width="40%">For most granular details, this options sets the spacing interval to one second. It's tailored for scenarios requiring real-time or near-real-time analysis.</td></tr><tr><td headers="d299446e10194" rowspan="2" width="20%"><code>EXSM_INITVL_OPTIMIZE</code></td><td headers="d299446e10487 d299446e10196" width="20%"><p><code>EXSM_INITVL_OPTIMIZE_ENABLE</code></p></td><td headers="d299446e10487 d299446e10198" width="20%"><p><code>EXSM_INITVL_OPTIMIZE_ENABLE</code></p></td><td headers="d299446e10487 d299446e10200" width="40%"><p>The setting <code>EXSM_INITVL_OPTIMIZE</code> determines whether initial values are optimized during model build.</p><p>The default value is <code>EXSM_INITVL_OPTIMIZE_ENABLE</code>.</p></td></tr><tr><td headers="d299446e10487 d299446e10196" width="20%"><p><code>EXSM_INITVL_OPTIMIZE_DISABLE</code></p></td><td headers="d299446e10487 d299446e10198" width="20%"><p><code>EXSM_INITVL_OPTIMIZE_DISABLE</code></p></td><td headers="d299446e10487 d299446e10200" width="40%"><p>Note:</p><code>EXSM_INITVL_OPTIMIZE</code> can only be set to <code>EXSM_INITVL_OPTIMIZE_DISABLE</code> if the user has set <code>EXSM_MODEL</code> to <code>EXSM_HW</code> or <code>EXSM_HW_ADDSEA</code>. If <code>EXSM_MODEL</code> is set to another model type or is not specified, you get an error 40213 (conflicting settings) and the model is not built.</td></tr><tr><td headers="d299446e10194" rowspan="7" width="20%"><code>EXSM_ACCUMULATE</code></td><td headers="d299446e10552 d299446e10196" width="20%"><p><code>EXSM_ACCU_TOTAL</code></p></td><td headers="d299446e10552 d299446e10198" width="20%"><p><code>EXSM_ACCU_TOTAL</code></p></td><td headers="d299446e10552 d299446e10200" width="40%"><p>This setting only applies and must be provided when the time column has datetime type. It specifies how to generate the value of the accumulated time series from the input time series.</p><p><code>EXSM_ACCU_TOTAL</code>: This option calculates the total sum of the time series values within a specified interval. When selected, it will aggregate the data by summing up all the individual values in the datetime range.</p><p>The default value is <code>EXSM_ACCU_TOTAL</code>.</p></td></tr><tr><td headers="d299446e10552 d299446e10196" width="20%"><p><code>EXSM_ACCU_STD</code></p></td><td headers="d299446e10552 d299446e10198" width="20%"><p><code>EXSM_ACCU_STD</code></p></td><td headers="d299446e10552 d299446e10200" width="40%"><p>This option computes the standard deviation of the time series values within a specified interval. It helps you understand the amount of variation or dispersion in your data.</p></td></tr><tr><td headers="d299446e10552 d299446e10196" width="20%"><p><code>EXSM_ACCU_MAX</code></p></td><td headers="d299446e10552 d299446e10198" width="20%"><p><code>EXSM_ACCU_MAX</code></p></td><td headers="d299446e10552 d299446e10200" width="40%"><p>By selecting this option, the maximum value of the time series within a specified interval will be determined. It helps in identifying the peak value in the given range.</p></td></tr><tr><td headers="d299446e10552 d299446e10196" width="20%"><p><code>EXSM_ACCU_MIN</code></p></td><td headers="d299446e10552 d299446e10198" width="20%"><p><code>EXSM_ACCU_MIN</code></p></td><td headers="d299446e10552 d299446e10200" width="40%"><p>This option focuses on determining the minimum value of the time series within a specified interval. It is useful for identifying the lowest value in the time series for the given datetime range.</p></td></tr><tr><td headers="d299446e10552 d299446e10196" width="20%"><p><code>EXSM_ACCU_AVG</code></p></td><td headers="d299446e10552 d299446e10198" width="20%"><p><code>EXSM_ACCU_AVG</code></p></td><td headers="d299446e10552 d299446e10200" width="40%"><p>This specifies the average value of your time series within a specified interval. It calculates the mean value of all data points in the specified range.</p></td></tr><tr><td headers="d299446e10552 d299446e10196" width="20%"><p><code>EXSM_ACCU_MEDIAN</code></p></td><td headers="d299446e10552 d299446e10198" width="20%"><p><code>EXSM_ACCU_MEDIAN</code></p></td><td headers="d299446e10552 d299446e10200" width="40%"><p>This option provides the median of the time series values within the given interval. The median gives a central value, which can be especially useful if your data contains outliers.</p></td></tr><tr><td headers="d299446e10552 d299446e10196" width="20%"><p><code>EXSM_ACCU_COUNT</code></p></td><td headers="d299446e10552 d299446e10198" width="20%"><p><code>EXSM_ACCU_COUNT</code></p></td><td headers="d299446e10552 d299446e10200" width="40%"><p>This option counts the number of time series values within the specified interval. It is helpful if you want to know how many data points are present in a certain datetime range.</p></td></tr><tr><td headers="d299446e10194" rowspan="9" width="20%"><code>EXSM_SETMISSING</code></td><td headers="d299446e10692 d299446e10196" width="20%"><p>Specify an option:</p><p><code>EXSM_MISS_MIN</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_MIN</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>This setting specifies how to handle missing values, which may come from input data and/or the accumulation process of time series. You can specify either a number or an option. If a number is specified, all the missing values are set to that number.</p><p><code>EXSM_MISS_MIN</code>: Replaces missing value with minimum of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_MAX</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_MAX</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>Replaces missing value with maximum of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_AVG</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_AVG</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>Replaces missing value with average of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_MEDIAN</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_MEDIAN</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>Replaces missing value with median of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_LAST</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_LAST</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>Replaces missing value with last non-missing value of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_FIRST</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_FIRST</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>Replaces missing value with first non-missing value of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_PREV</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_PREV</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>Replaces missing value with the previous non-missing value of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_NEXT</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_NEXT</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>Replaces missing value with the next non-missing value of the accumulated time series.</p></td></tr><tr><td headers="d299446e10692 d299446e10196" width="20%"><p><code>EXSM_MISS_AUTO</code></p></td><td headers="d299446e10692 d299446e10198" width="20%"><p><code>EXSM_MISS_AUTO</code></p></td><td headers="d299446e10692 d299446e10200" width="40%"><p>EXSM model treats the input data as an irregular (non-uniformly spaced) time series.</p><p>If this setting is not provided, <code>EXSM_MISS_AUTO</code> is the default value. In such a case, the model treats the input time series as irregular time series, viewing missing values as gaps.</p></td></tr><tr><td headers="d299446e10194" width="20%"><code>EXSM_PREDICTION_STEP</code></td><td headers="d299446e10872 d299446e10196" width="20%">It must be set to a number between 1- 30.</td><td headers="d299446e10872 d299446e10198" width="20%">It must be set to a number between 1-30.</td><td headers="d299446e10872 d299446e10200" width="40%"><p>This setting specifies how many steps ahead the predictions are to be made.</p><p>If it is not set, the default value is <code>1</code>: the model gives one-step-ahead prediction. A value greater than <code>30</code> results in an error.</p></td></tr><tr><td headers="d299446e10194" width="20%"><code>EXSM_CONFIDENCE_LEVEL</code></td><td headers="d299446e10894 d299446e10196" width="20%">It must be a number between 0 and 1, exclusive.</td><td headers="d299446e10894 d299446e10198" width="20%">It must be a number between 0 and 1, exclusive.</td><td headers="d299446e10894 d299446e10200" width="40%"><p>This setting specifies the desired confidence level for prediction.</p><p>The lower and upper bounds of the specified confidence interval is reported. If this setting is not specified, the default confidence level is <code>95%</code>.</p></td></tr><tr><td headers="d299446e10194" rowspan="5" width="20%"><code>
                                EXSM_OPT_CRITERION</code></td><td headers="d299446e10913 d299446e10196" width="20%"><p><code>EXSM_OPT_CRIT_LIK</code></p></td><td headers="d299446e10913 d299446e10198" width="20%"><p><code>EXSM_OPT_CRIT_LIK</code></p></td><td headers="d299446e10913 d299446e10200" width="40%"><p>This setting specifies the desired optimization criterion. The optimization criterion is useful as a diagnostic for comparing models' fit to the same data.</p><p><code>EXSM_OPT_CRIT_LIK</code>: This represents the negative double of the logarithm of the likelihood associated with a given model.</p><p>The default value is <code>EXSM_OPT_CRIT_LIK</code>.</p></td></tr><tr><td headers="d299446e10913 d299446e10196" width="20%"><p><code>EXSM_OPT_CRIT_MSE</code></p></td><td headers="d299446e10913 d299446e10198" width="20%"><p><code>EXSM_OPT_CRIT_MSE</code></p></td><td headers="d299446e10913 d299446e10200" width="40%"><p>This provides the mean squared error pertaining to the model.</p></td></tr><tr><td headers="d299446e10913 d299446e10196" width="20%"><p><code>EXSM_OPT_CRIT_AMSE</code></p></td><td headers="d299446e10913 d299446e10198" width="20%"><p><code>EXSM_OPT_CRIT_AMSE</code></p></td><td headers="d299446e10913 d299446e10200" width="40%"><p>This denotes the average of the mean squared error over a time window as specified by the user.</p></td></tr><tr><td headers="d299446e10913 d299446e10196" width="20%"><p><code>EXSM_OPT_CRIT_SIG</code></p></td><td headers="d299446e10913 d299446e10198" width="20%"><p><code>EXSM_OPT_CRIT_SIG</code></p></td><td headers="d299446e10913 d299446e10200" width="40%"><p>This metric captures the standard deviation of the residuals of the model.</p></td></tr><tr><td headers="d299446e10913 d299446e10196" width="20%"><p><code>EXSM_OPT_CRIT_MAE</code></p></td><td headers="d299446e10913 d299446e10198" width="20%"><p><code>EXSM_OPT_CRIT_MAE</code></p></td><td headers="d299446e10913 d299446e10200" width="40%"><p>This metric conveys the average absolute error associated with the model. It measures the size of the error.</p></td></tr><tr><td headers="d299446e10194" width="20%"><code>EXSM_NMSE</code></td><td headers="d299446e11018 d299446e10196" width="20%">positive integer</td><td headers="d299446e11018 d299446e10198" width="20%">positive integer</td><td headers="d299446e11018 d299446e10200" width="40%">This setting specifies the length of the window used in computing the error metric Average Mean Square Error (AMSE).</td></tr></tbody></table>

**See Also:**

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-65C7E533-E403-4F71-A5FE-EC034745904F) for information about ESM.

[https://github.com/oracle-samples/oracle-db-examples/tree/main/machine-learning/sql](https://github.com/oracle-samples/oracle-db-examples/tree/main/machine-learning/sql) browse to the release folder and click the `oml4sql-time-series-exponential-smoothing.sql` example.

### DBMS\_DATA\_MINING - Algorithm Settings: Generalized Linear Model

The settings listed in the following table configure the behavior of the Generalized Linear Model algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.GLMS_FTR_GEN_QUADRATIC`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'GLMS_FTR_GEN_QUADRATIC'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 18 DBMS\_DATA\_MINING GLM

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e11483" width="20%"><p><code>GLMS_CONF_LEVEL</code></p></td><td headers="d299446e11502 d299446e11488" width="20%"><p><code>TO_CHAR(0<
                                        </code> <code>numeric_expr</code> <code>
                                    <1)</code></p></td><td headers="d299446e11502 d299446e11493" width="20%"><p><code>TO_CHAR(0<
                                        </code> <code>numeric_expr</code> <code>
                                    <1)</code></p></td><td headers="d299446e11502 d299446e11495" width="40%"><p>The confidence level for coefficient confidence intervals.</p><p>The default confidence level is <code>
0.95</code>.</p></td></tr><tr><td headers="d299446e11483" rowspan="2" width="20%"><p><code>GLMS_FTR_GEN_METHOD</code></p></td><td headers="d299446e11542 d299446e11488" width="20%"><p><code>GLMS_FTR_GEN_QUADRATIC</code></p></td><td headers="d299446e11542 d299446e11493" width="20%"><p><code>GLMS_FTR_GEN_QUADRATIC</code></p></td><td headers="d299446e11542 d299446e11495" width="40%"><p>Whether feature generation is quadratic or cubic. When feature generation is enabled, the algorithm automatically chooses the most appropriate feature generation method based on the data.</p><p><code>GLMS_FTR_GEN_QUADRATIC</code>: Generates features using a quadratic method.</p></td></tr><tr><td headers="d299446e11542 d299446e11488" width="20%"><p><code>GLMS_FTR_GEN_CUBIC</code></p></td><td headers="d299446e11542 d299446e11488" width="20%"><p><code>GLMS_FTR_GEN_CUBIC</code></p></td><td headers="d299446e11542 d299446e11493" width="20%"><p>Generates features using a cubic method.</p></td></tr><tr><td headers="d299446e11483" rowspan="2" width="20%"><p><code>GLMS_FTR_GENERATION</code></p></td><td headers="d299446e11593 d299446e11488" width="20%"><p><code>GLMS_FTR_GENERATION_ENABLE</code></p></td><td headers="d299446e11593 d299446e11493" width="20%"><p><code>GLMS_FTR_GENERATION_ENABLE</code></p></td><td headers="d299446e11593 d299446e11495" width="40%"><p>Whether or not feature generation is enabled for GLM. By default, feature generation is not enabled.</p><p>Note: Feature generation can only be enabled when feature selection is also enabled.</p></td></tr><tr><td headers="d299446e11593 d299446e11488" width="20%"><p><code>GLMS_FTR_GENERATION_DISABLE</code></p></td><td headers="d299446e11593 d299446e11488" width="20%"><p><code>GLMS_FTR_GENERATION_DISABLE</code></p></td><td headers="d299446e11593 d299446e11493" width="20%"><p>Disables feature generation for GLM (default).</p></td></tr><tr><td headers="d299446e11483" rowspan="4" width="20%"><p><code>GLMS_FTR_SEL_CRIT</code></p></td><td headers="d299446e11642 d299446e11488" width="20%"><p><code>GLMS_FTR_SEL_AIC</code></p></td><td headers="d299446e11642 d299446e11493" width="20%"><p><code>GLMS_FTR_SEL_AIC</code></p></td><td headers="d299446e11642 d299446e11495" width="40%"><p>Feature selection penalty criterion for adding a feature to the model.</p><p>When feature selection is enabled, the algorithm automatically chooses the penalty criterion based on the data.</p><p><code>GLMS_FTR_SEL_AIC</code>: Uses Akaike Information Criterion for feature selection.</p></td></tr><tr><td headers="d299446e11642 d299446e11488" width="20%"><p><code>GLMS_FTR_SEL_SBIC</code></p></td><td headers="d299446e11642 d299446e11488" width="20%"><p><code>GLMS_FTR_SEL_SBIC</code></p></td><td headers="d299446e11642 d299446e11493" width="20%"><p>Uses Schwarz Bayesian Information Criterion for feature selection.</p></td></tr><tr><td headers="d299446e11642 d299446e11488" width="20%"><p><code>GLMS_FTR_SEL_RIC</code></p></td><td headers="d299446e11642 d299446e11488" width="20%"><p><code>GLMS_FTR_SEL_RIC</code></p></td><td headers="d299446e11642 d299446e11493" width="20%">Uses Risk Inflation Criterion for feature selection.</td></tr><tr><td headers="d299446e11642 d299446e11488" width="20%"><p><code>GLMS_FTR_SEL_ALPHA_INV</code></p></td><td headers="d299446e11642 d299446e11488" width="20%"><p><code>GLMS_FTR_SEL_ALPHA_INV</code></p></td><td headers="d299446e11642 d299446e11493" width="20%">Uses Alpha Inverse Criterion for feature selection.</td></tr><tr><td headers="d299446e11483" rowspan="2" width="20%"><p><code>GLMS_FTR_SELECTION</code></p></td><td headers="d299446e11730 d299446e11488" width="20%"><p><code>GLMS_FTR_SELECTION_ENABLE</code></p></td><td headers="d299446e11730 d299446e11493" width="20%"><p><code>GLMS_FTR_SELECTION_ENABLE</code></p></td><td headers="d299446e11730 d299446e11495" width="40%"><p>Whether or not feature selection is enabled for GLM.</p><p>By default, feature selection is not enabled.</p></td></tr><tr><td headers="d299446e11730 d299446e11488" width="20%"><p><code>GLMS_FTR_SELECTION_DISABLE</code></p></td><td headers="d299446e11730 d299446e11488" width="20%"><p><code>GLMS_FTR_SELECTION_DISABLE</code></p></td><td headers="d299446e11730 d299446e11493" width="20%"><p>Disables feature selection.</p></td></tr><tr><td headers="d299446e11483" width="20%"><p><code>GLMS_MAX_FEATURES</code></p></td><td headers="d299446e11781 d299446e11488" width="20%"><p><code>TO_CHAR(0 <
                                        </code> <code>numeric_expr</code> <code> <=
                                    2000)</code></p></td><td headers="d299446e11781 d299446e11493" width="20%"><p><code>TO_CHAR(0 <
                                        </code> <code>numeric_expr</code> <code> <=
                                    2000)</code></p></td><td headers="d299446e11781 d299446e11495" width="40%"><p>When feature selection is enabled, this setting specifies the maximum number of features that can be selected for the final model.</p><p>By default, the algorithm limits the number of features to ensure sufficient memory.</p></td></tr><tr><td headers="d299446e11483" rowspan="2" width="20%"><p><code>GLMS_PRUNE_MODEL</code></p></td><td headers="d299446e11818 d299446e11488" width="20%"><p><code>GLMS_PRUNE_MODEL_ENABLE</code></p></td><td headers="d299446e11818 d299446e11493" width="20%"><p><code>GLMS_PRUNE_MODEL_ENABLE</code></p></td><td headers="d299446e11818 d299446e11495" width="40%"><p>Enables or disables pruning of features in the final model. Pruning is based on T-Test statistics for linear regression, or Wald Test statistics for logistic regression. Features are pruned in a loop until all features are statistically significant with respect to the full data.</p><p>When feature selection is enabled, the algorithm automatically prunes as per the description..</p><p>When feature selection is disabled, you cannot specify pruning.</p></td></tr><tr><td headers="d299446e11818 d299446e11488" width="20%"><p><code>GLMS_PRUNE_MODEL_DISABLE</code></p></td><td headers="d299446e11818 d299446e11488" width="20%"><p><code>GLMS_PRUNE_MODEL_DISABLE</code></p></td><td headers="d299446e11818 d299446e11493" width="20%"><p>Disables pruning of features.</p></td></tr><tr><td headers="d299446e11483" width="20%"><p><code>GLMS_REFERENCE_CLASS_NAME</code></p></td><td headers="d299446e11872 d299446e11488" width="20%"><p>target_value</p></td><td headers="d299446e11872 d299446e11493" width="20%"><p>target_value</p></td><td headers="d299446e11872 d299446e11495" width="40%"><p>The target value used as the reference class in a binary logistic regression model. Probabilities are produced for the other class.</p><p>By default, the algorithm chooses the value with the highest prevalence (the most cases) for the reference class.</p></td></tr><tr><td headers="d299446e11483" rowspan="2" width="20%"><p><code>GLMS_RIDGE_REGRESSION</code></p></td><td headers="d299446e11899 d299446e11488" width="20%"><p><code>GLMS_RIDGE_REG_ENABLE</code></p></td><td headers="d299446e11899 d299446e11493" width="20%"><p><code>GLMS_RIDGE_REG_ENABLE</code></p></td><td headers="d299446e11899 d299446e11495" width="40%"><p>Enable or disable ridge regression. Ridge applies to both regression and classification data mining techniques.</p><p>When ridge is enabled, prediction bounds are not produced by the <code>PREDICTION_BOUNDS</code> SQL function.</p><p>Note: Ridge may only be enabled when feature selection is not specified, or has been explicitly disabled. If ridge regression is enabled, you cannot enable feature selection and an exception is raised.</p></td></tr><tr><td headers="d299446e11899 d299446e11488" width="20%"><p><code>GLMS_RIDGE_REG_DISABLE</code></p></td><td headers="d299446e11899 d299446e11488" width="20%"><p><code>GLMS_RIDGE_REG_DISABLE</code></p></td><td headers="d299446e11899 d299446e11493" width="20%"><p>Disables ridge regression.</p></td></tr><tr><td headers="d299446e11483" width="20%"><p><code>GLMS_RIDGE_VALUE</code></p></td><td headers="d299446e11963 d299446e11488" width="20%"><p><code>TO_CHAR (numeric_expr >
                                0)</code></p></td><td headers="d299446e11963 d299446e11493" width="20%"><p><code>TO_CHAR (numeric_expr >
                                0)</code></p></td><td headers="d299446e11963 d299446e11495" width="40%"><p>The value of the ridge parameter. This setting is only used when the algorithm is configured to use ridge regression.</p><p>If ridge regression is enabled internally by the algorithm, then the ridge parameter is determined by the algorithm.</p></td></tr><tr><td headers="d299446e11483" rowspan="2" width="20%"><code>GLMS_ROW_DIAGNOSTICS</code></td><td headers="d299446e11996 d299446e11488" width="20%"><p><code>GLMS_ROW_DIAG_ENABLE</code></p></td><td headers="d299446e11996 d299446e11493" width="20%"><p><code>GLMS_ROW_DIAG_ENABLE</code></p></td><td headers="d299446e11996 d299446e11495" width="40%"><p>Enables or disables row diagnostics.</p><p><code>GLMS_ROW_DIAG_ENABLE</code>: Enables row diagnostics.</p></td></tr><tr><td headers="d299446e11996 d299446e11488" width="20%"><p><code>GLMS_ROW_DIAG_DISABLE (default).</code></p></td><td headers="d299446e11996 d299446e11493" width="20%"><p><code>GLMS_ROW_DIAG_DISABLE (default).</code></p></td><td headers="d299446e11996 d299446e11495" width="40%"><p>Disables row diagnostics (default).</p></td></tr><tr><td headers="d299446e11483" width="20%"><p><code>GLMS_CONV_TOLERANCE</code></p></td><td headers="d299446e12046 d299446e11488" width="20%"><p>The range is (<code>0, 1</code>) non-inclusive.</p></td><td headers="d299446e12046 d299446e11493" width="20%"><p>The range is (<code>0, 1</code>) non-inclusive.</p></td><td headers="d299446e12046 d299446e11495" width="40%"><p>Convergence Tolerance setting of the GLM algorithm</p><p>The default value is system-determined.</p></td></tr><tr><td headers="d299446e11483" width="20%"><p><code>GLMS_NUM_ITERATIONS</code></p></td><td headers="d299446e12079 d299446e11488" width="20%"><p>Positive integer</p></td><td headers="d299446e12079 d299446e11493" width="20%"><p>Positive integer</p></td><td headers="d299446e12079 d299446e11495" width="40%"><p>Maximum number of iterations for the GLM algorithm. The default value is system-determined.</p></td></tr><tr><td headers="d299446e11483" width="20%"><p><code>GLMS_BATCH_ROWS</code></p></td><td headers="d299446e12104 d299446e11488" width="20%"><p><code>0</code> or Positive integer</p></td><td headers="d299446e12104 d299446e11493" width="20%"><p><code>0</code> or Positive integer</p></td><td headers="d299446e12104 d299446e11495" width="40%"><p>Number of rows in a batch used by the SGD solver. The value of this parameter sets the size of the batch for the SGD solver. An input of 0 triggers a data driven batch size estimate.</p><p>The default is <code>2000</code></p></td></tr><tr><td headers="d299446e11483" rowspan="4" width="20%"><p><code>GLMS_SOLVER</code></p></td><td headers="d299446e12140 d299446e11488" width="20%"><p><code>GLMS_SOLVER_SGD (StochasticGradient
                                    Descent)</code></p></td><td headers="d299446e12140 d299446e11493" width="20%"><p><code>GLMS_SOLVER_SGD (StochasticGradient
                                    Descent)</code></p></td><td headers="d299446e12140 d299446e11495" width="40%"><p>This setting allows the user to choose the GLM solver. The solver cannot be selected if <code>GLMS_FTR_SELECTION</code> setting is enabled.</p><p><code>GLMS_SOLVER_SGD</code>: Optimizes generalized linear models by iteratively updating parameters using a subset of the data to minimize errors.</p><p>The default value is system determined.</p><div><p>See Also:</p><a href="https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-F36DDDDB-3A87-4C97-8000-EBF009E794C2">GLM Solvers</a></div></td></tr><tr><td headers="d299446e12140 d299446e11488" width="20%"><p><code>GLMS_SOLVER_CHOL (Cholesky)</code></p></td><td headers="d299446e12140 d299446e11493" width="20%"><p><code>GLMS_SOLVER_CHOL (Cholesky)</code></p></td><td headers="d299446e12140 d299446e11495" width="40%"><p>Solves generalized linear models using the Cholesky decomposition method, which provides a stable and efficient solution by transforming the right-hand of the equation into a lower triangular matrix and its conjugate transpose.</p></td></tr><tr><td headers="d299446e12140 d299446e11488" width="20%"><p><code>GLMS_SOLVER_QR</code></p></td><td headers="d299446e12140 d299446e11493" width="20%"><p><code>GLMS_SOLVER_QR</code></p></td><td headers="d299446e12140 d299446e11495" width="40%"><p>Utilizes the QR decomposition technique to solve generalized linear models, ensuring numerical stability and accuracy by decomposing the problem into an orthonormal matrix Q and upper triangular matrix R.</p></td></tr><tr><td headers="d299446e12140 d299446e11488" width="20%"><p><code>GLMS_SOLVER_LBFGS_ADMM</code></p></td><td headers="d299446e12140 d299446e11493" width="20%"><p><code>GLMS_SOLVER_LBFGS_ADMM</code></p></td><td headers="d299446e12140 d299446e11495" width="40%"><p>Combines L-BFGS, an approximation of the Broyden-Fletcher-Goldfarb-Shanno optimization algorithm, with ADMM for solving large-scale generalized linear model problems efficiently.</p></td></tr><tr><td headers="d299446e11483" rowspan="2" width="20%"><p><code>GLMS_SPARSE_SOLVER</code></p></td><td headers="d299446e12241 d299446e11488" width="20%"><p><code>GLMS_SPARSE_SOLVER_ENABLE</code></p></td><td headers="d299446e12241 d299446e11493" width="20%"><p><code>GLMS_SPARSE_SOLVER_ENABLE</code></p></td><td headers="d299446e12241 d299446e11495" width="40%"><p>This setting allows the user to use sparse solver if it is available. The default value is <code>GLMS_SPARSE_SOLVER_DISABLE</code>.</p></td></tr><tr><td headers="d299446e12241 d299446e11488" width="20%"><p><code>GLMS_SPARSE_SOLVER_DISABLE</code> (default).</p></td><td headers="d299446e12241 d299446e11493" width="20%"><p><code>GLMS_SPARSE_SOLVER_DISABLE</code> (default).</p></td><td headers="d299446e12241 d299446e11495" width="40%"><p>Disables sparse solver.</p></td></tr></tbody></table>

**Related Topics**

- DBMS\_DATA\_MINING — Algorithm Settings: Neural Network
- DBMS\_DATA\_MINING — Solver Settings: LBFGS
- DBMS\_DATA\_MINING — Solver Settings: ADMM
- [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-F36DDDDB-3A87-4C97-8000-EBF009E794C2)

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON022) for information about GLM.

### DBMS\_DATA\_MINING - Algorithm Settings: k -Means

The settings listed in the following table configure the behavior of the *k* -Means algorithm.

/

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.KMNS_COSINE`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'KMNS_COSINE'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 19 k-Means Settings

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e12771" width="20%"><p><code>KMNS_CONV_TOLERANCE</code></p></td><td headers="d299446e12790 d299446e12776" width="20%"><p><code>TO_CHAR(0<</code> <code>numeric_expr</code> <code><1)</code></p></td><td headers="d299446e12790 d299446e12781" width="20%"><p><code>TO_CHAR(0<</code> <code>numeric_expr</code> <code><1)</code></p></td><td headers="d299446e12790 d299446e12783" width="40%"><p>Minimum Convergence Tolerance for k-Means. The algorithm iterates until the minimum Convergence Tolerance is satisfied or until the maximum number of iterations, specified in <code>KMNS_ITERATIONS</code>, is reached.</p><p>Decreasing the Convergence Tolerance produces a more accurate solution but may result in longer run times.</p><p>The default Convergence Tolerance is <code>
0.001</code>.</p></td></tr><tr><td headers="d299446e12771" rowspan="2" width="20%"><p><code>KMNS_DISTANCE</code></p></td><td headers="d299446e12839 d299446e12776" width="20%"><p><code>KMNS_COSINE</code></p></td><td headers="d299446e12839 d299446e12781" width="20%"><p><code>KMNS_COSINE</code></p></td><td headers="d299446e12839 d299446e12783" width="40%"><p>Distance function for k-Means.</p><p><code>KMNS_COSINE</code>: Uses cosine distance for k-Means.</p><p>The default distance function is <code>KMNS_EUCLIDEAN</code>.</p></td></tr><tr><td headers="d299446e12839 d299446e12776" width="20%"><p><code>KMNS_EUCLIDEAN</code></p></td><td headers="d299446e12839 d299446e12776" width="20%"><p><code>KMNS_EUCLIDEAN</code></p></td><td headers="d299446e12839 d299446e12781" width="20%"><p>Uses Euclidean distance for k-Means.</p></td></tr><tr><td headers="d299446e12771" width="20%"><p><code>KMNS_ITERATIONS</code></p></td><td headers="d299446e12906 d299446e12776" width="20%"><p><code>TO_CHAR(</code><code>positive_numeric_expr</code>)</p></td><td headers="d299446e12906 d299446e12781" width="20%"><p><code>TO_CHAR(</code><code>positive_numeric_expr</code>)</p></td><td headers="d299446e12906 d299446e12783" width="40%"><p>Maximum number of iterations for k-Means. The algorithm iterates until either the maximum number of iterations is reached or the minimum Convergence Tolerance, specified in <code>KMNS_CONV_TOLERANCE</code>, is satisfied.</p><p>The default number of iterations is <code>20</code>.</p></td></tr><tr><td headers="d299446e12771" width="20%"><p><code>KMNS_MIN_PCT_ATTR_SUPPORT</code></p></td><td headers="d299446e12950 d299446e12776" width="20%"><p><code>TO_CHAR(0<=</code> <code>numeric_expr</code> <code><=1)</code></p></td><td headers="d299446e12950 d299446e12781" width="20%"><p><code>TO_CHAR(0<=</code> <code>numeric_expr</code> <code><=1)</code></p></td><td headers="d299446e12950 d299446e12783" width="40%"><p>Minimum percentage of attribute values that must be non-null in order for the attribute to be included in the rule description for the cluster.</p><p>If the data is sparse or includes many missing values, a minimum support that is too high can cause very short rules or even empty rules.</p><p>The default minimum support is <code>0.1</code>.</p></td></tr><tr><td headers="d299446e12771" width="20%"><p><code>KMNS_NUM_BINS</code></p></td><td headers="d299446e12993 d299446e12776" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>>0)</code></p></td><td headers="d299446e12993 d299446e12781" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>>0)</code></p></td><td headers="d299446e12993 d299446e12783" width="40%"><p>Number of bins in the attribute histogram produced by k-means. The bin boundaries for each attribute are computed globally on the entire training data set. The binning method is equi-width. All attributes have the same number of bins with the exception of attributes with a single value that have only one bin.</p><p>The default number of histogram bins is <code>11</code>.</p></td></tr><tr><td headers="d299446e12771" rowspan="2" width="20%"><p><code>KMNS_SPLIT_CRITERION</code></p></td><td headers="d299446e13038 d299446e12776" width="20%"><p><code>KMNS_SIZE</code></p></td><td headers="d299446e13038 d299446e12781" width="20%"><p><code>KMNS_SIZE</code></p></td><td headers="d299446e13038 d299446e12783" width="40%"><p>Split criterion for k-means. The split criterion controls the initialization of new k-Means clusters. The algorithm builds a binary tree and adds one new cluster at a time.</p><p>When the split criterion is based on size, the new cluster is placed in the area where the largest current cluster is located.</p><p>The default split criterion is the <code>KMNS_VARIANCE</code>.</p></td></tr><tr><td headers="d299446e13038 d299446e12776" width="20%"><p><code>KMNS_VARIANCE</code></p></td><td headers="d299446e13038 d299446e12776" width="20%"><p><code>KMNS_VARIANCE</code></p></td><td headers="d299446e13038 d299446e12781" width="20%"><p>When the split criterion is based on the variance, the new cluster is placed in the area of the most spread-out cluster.</p></td></tr><tr><td headers="d299446e12771" width="20%"><code>KMNS_RANDOM_SEED </code></td><td headers="d299446e13097 d299446e12776" width="20%"><p>Non-negative integer</p></td><td headers="d299446e13097 d299446e12781" width="20%"><p>Non-negative integer</p></td><td headers="d299446e13097 d299446e12783" width="40%"><p>This setting controls the seed of the random generator used during the k-Means initialization. It must be a non-negative integer value.</p><p>The default is <code>0</code>.</p></td></tr><tr><td headers="d299446e12771" rowspan="3" width="20%"><p><code>KMNS_DETAILS</code></p></td><td headers="d299446e13129 d299446e12776" width="20%"><p><code>KMNS_DETAILS_NONE</code></p></td><td headers="d299446e13129 d299446e12781" width="20%"><p><code>KMNS_DETAILS_NONE</code></p></td><td headers="d299446e13129 d299446e12783" width="40%"><p>This setting determines the level of cluster detail that are computed during the build.</p><p><code>KMNS_DETAILS_NONE</code>: No cluster details are computed. Only the scoring information is persisted.</p></td></tr><tr><td headers="d299446e13129 d299446e12776" width="20%"><p><code>KMNS_DETAILS_HIERARCHY</code></p></td><td headers="d299446e13129 d299446e12781" width="20%"><p><code>KMNS_DETAILS_HIERARCHY</code></p></td><td headers="d299446e13129 d299446e12783" width="40%"><p>Cluster hierarchy and cluster record counts are computed. This is the default value.</p></td></tr><tr><td headers="d299446e13129 d299446e12776" width="20%"><p><code>KMNS_DETAILS_ALL</code></p></td><td headers="d299446e13129 d299446e12781" width="20%"><p><code>KMNS_DETAILS_ALL</code></p></td><td headers="d299446e13129 d299446e12783" width="40%"><p>Cluster hierarchy, record counts, descriptive statistics (means, variances, modes, histograms, and rules) are computed.</p></td></tr></tbody></table>

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON057) for information about *k* -Means

### DBMS\_DATA\_MINING - Algorithm Settings: Naive Bayes

The settings listed in the following table configure the behavior of the Naive Bayes algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.NABS_PAIRWISE_THRESHOLD`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'NABS_PAIRWISE_THRESHOLD'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 20 Naive Bayes Settings

| Setting Name | Setting Value | String Value Equivalent | Description |
| --- | --- | --- | --- |
| `NABS_PAIRWISE_THRESHOLD` | `TO_CHAR(0<=` *numeric\_expr* `<=1)` | `TO_CHAR(0<=` *numeric\_expr* `<=1)` | Value of pairwise threshold for NB algorithm  Default is `0`. |
| `NABS_SINGLETON_THRESHOLD` | `TO_CHAR(0<=` *numeric\_expr* `<=1)` | `TO_CHAR(0<=` *numeric\_expr* `<=1)` | Value of singleton threshold for NB algorithm  Default value is `0`. |

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON018) for information about Naive Bayes

### DBMS\_DATA\_MINING - Algorithm Settings: Neural Network

The settings listed in the following table configure the behavior of Neural Network.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.NNET_REGULARIZER_NONE`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'NNET_REGULARIZER_NONE'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 21 DBMS\_DATA\_MINING Neural Network

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e14195" width="20%"><p><code>NNET_HIDDEN_LAYERS</code></p></td><td headers="d299446e14217 d299446e14200" width="20%"><p>Non-negative integer</p></td><td headers="d299446e14217 d299446e14205" width="20%"><p>Non-negative integer</p></td><td headers="d299446e14217 d299446e14210" width="40%"><p>Defines the topology by number of hidden layers.</p><p>The default value is <code>1</code>.</p><p>The maximum supported value is 2100. This limit prevents unsafe memory use and out-of-bounds buffer handling during Neural Network model creation. Existing model configurations with <code>NNET_HIDDEN_LAYERS</code> values of <code>2100</code> or less do not require changes.</p></td></tr><tr><td headers="d299446e14195" width="20%"><p><code>NNET_NODES_PER_LAYER</code></p></td><td headers="d299446e14245 d299446e14200" width="20%"><p>A list of positive integers</p></td><td headers="d299446e14245 d299446e14205" width="20%"><p>A list of positive integers</p></td><td headers="d299446e14245 d299446e14210" width="40%"><p>Defines the topology by number of nodes per layer. Different layers can have different number of nodes.</p><p>The value should be non-negative integers and comma separated. For example, '10, 20, 5'. The setting values must be consistent with <code>NNET_HIDDEN_LAYERS</code>. The default number of nodes per layer is the number of attributes or <code>50</code> (if the number of attributes > <code>50</code>).</p></td></tr><tr><td headers="d299446e14195" rowspan="5" width="20%"><p><code>NNET_ACTIVATIONS</code></p></td><td headers="d299446e14282 d299446e14200" width="20%"><p>One or more of the following strings:</p><code>NNET_ACTIVATIONS_LOG_SIG</code></td><td headers="d299446e14282 d299446e14205" width="20%"><code>NNET_ACTIVATIONS_LOG_SIG</code></td><td headers="d299446e14282 d299446e14210" width="40%"><p>Specifies the activation functions for the hidden layers. You can specify a single activation function, which is then applied to each hidden layer, or you can specify an activation function for each layer individually. Different layers can have different activation functions.</p><p>To apply a different activation function to one or more of the layers, you must specify an activation function for each layer. The number of activation functions you specify must be consistent with the <code>NNET_HIDDEN_LAYERS</code> and <code>NNET_NODES_PER_LAYER</code> values.</p><p>Different layers can have different activation functions.</p><p><code>NNET_ACTIVATIONS_LOG_SIG</code>: Uses the logistic sigmoid activation function.</p><p>The default value is '' <code>NNET_ACTIVATIONS_LOG_SIG</code> ''.</p><p>For example, if you have three hidden layers, you could specify the use of the same activation function for all three layers with the following settings value:</p><pre><code>('NNET_ACTIVATIONS', 'NNET_ACTIVATIONS_TANH')</code></pre><p>The following settings value specifies a different activation function for each layer:</p><pre><code>('NNET_ACTIVATIONS', '''NNET_ACTIVATIONS_TANH'', ''NNET_ACTIVATIONS_LOG_SIG'', ''NNET_ACTIVATIONS_ARCTAN''')</code></pre><p>Note:</p>You specify the different activation functions as strings within a single string. All quotes are single and two single quotes are used to escape a single quote in SQL statements and PL/SQL blocks.</td></tr><tr><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_LINEAR</code></td><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_LINEAR</code></td><td headers="d299446e14282 d299446e14205" width="20%"><p>Uses the linear activation function.</p></td></tr><tr><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_TANH</code></td><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_TANH</code></td><td headers="d299446e14282 d299446e14205" width="20%"><p>Uses the hyperbolic tangent activation function.</p></td></tr><tr><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_ARCTAN</code></td><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_ARCTAN</code></td><td headers="d299446e14282 d299446e14205" width="20%"><p>Uses the arctangent activation function.</p></td></tr><tr><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_BIPOLAR_SIG</code></td><td headers="d299446e14282 d299446e14200" width="20%"><code>NNET_ACTIVATIONS_BIPOLAR_SIG</code></td><td headers="d299446e14282 d299446e14205" width="20%"><p>Uses the bipolar sigmoid activation function.</p></td></tr><tr><td headers="d299446e14195" width="20%"><p><code>NNET_WEIGHT_LOWER_BOUND</code></p></td><td headers="d299446e14405 d299446e14200" width="20%"><p>A real number</p></td><td headers="d299446e14405 d299446e14205" width="20%"><p>A real number</p></td><td headers="d299446e14405 d299446e14210" width="40%"><div>The setting specifies the lower bound of the region where weights are randomly initialized. <code>NNET_WEIGHT_LOWER_BOUND</code> and <code>NNET_WEIGHT_UPPER_BOUND</code> must be set together. Setting one and not setting the other raises an error. <code>NNET_WEIGHT_LOWER_BOUND</code> must not be greater than <code>NNET_WEIGHT_UPPER_BOUND</code>. The default value is <code>-sqrt(6/(l_nodes+r_nodes))</code>. The value of <code>l_nodes</code> for:<ul><li><p>input layer dense attributes is (<code>1+number of dense attributes</code>)</p></li><li><p>input layer sparse attributes is <code>number of sparse attributes</code></p></li><li><p>each hidden layer is (<code>1+number of
                                                nodes in that hidden layer</code>)</p></li></ul></div><p>The value of <code>r_nodes</code> is the number of nodes in the layer that the weight is connecting to.</p></td></tr><tr><td headers="d299446e14195" width="20%"><p><code>NNET_WEIGHT_UPPER_BOUND</code></p></td><td headers="d299446e14476 d299446e14200" width="20%"><p>A real number</p></td><td headers="d299446e14476 d299446e14205" width="20%"><p>A real number</p></td><td headers="d299446e14476 d299446e14210" width="40%"><p>This setting specifies the upper bound of the region where weights are initialized. It should be set in pairs with <code>NNET_WEIGHT_LOWER_BOUND</code> and its value must not be smaller than the value of <code>NNET_WEIGHT_LOWER_BOUND</code>. If not specified, the values of <code>NNET_WEIGHT_LOWER_BOUND</code> and <code>NNET_WEIGHT_UPPER_BOUND</code> are system determined.</p><p>The default value is <code>sqrt(6/(l_nodes+r_nodes))</code>. See <code>NNET_WEIGHT_LOWER_BOUND</code>.</p></td></tr><tr><td headers="d299446e14195" width="20%"><p><code>NNET_ITERATIONS</code></p></td><td headers="d299446e14519 d299446e14200" width="20%"><p>Positive integer</p></td><td headers="d299446e14519 d299446e14205" width="20%"><p>Positive integer</p></td><td headers="d299446e14519 d299446e14210" width="40%"><p>This setting specifies the maximum number of iterations in the Neural Network algorithm.</p><p>The default value is <code>200</code>.</p></td></tr><tr><td headers="d299446e14195" width="20%"><p><code>NNET_TOLERANCE</code></p></td><td headers="d299446e14547 d299446e14200" width="20%"><p><code>TO_CHAR(0<
                                        </code> <code>numeric_expr</code> <code>
                                    <1)</code></p></td><td headers="d299446e14547 d299446e14205" width="20%"><p><code>TO_CHAR(0<
                                        </code> <code>numeric_expr</code> <code>
                                    <1)</code></p></td><td headers="d299446e14547 d299446e14210" width="40%"><p>Defines the convergence tolerance setting of the Neural Network algorithm.</p><p>The default value is <code>
0.000001</code>.</p></td></tr><tr><td headers="d299446e14195" rowspan="3" width="20%"><p><code>NNET_REGULARIZER</code></p></td><td headers="d299446e14588 d299446e14200" width="20%"><p><code>NNET_REGULARIZER_NONE</code></p></td><td headers="d299446e14588 d299446e14205" width="20%"><p><code>NNET_REGULARIZER_NONE</code></p></td><td headers="d299446e14588 d299446e14210" width="40%"><p>Regularization setting for Neural Network algorithm.</p><p><code>NNET_REGULARIZER_NONE</code>: Disables regularization. If the total number of training rows is less than or equal to 50000, the default is <code>NNET_REGULARIZER_NONE</code>.</p></td></tr><tr><td headers="d299446e14588 d299446e14200" width="20%"><p><code>NNET_REGULARIZER_L2</code></p></td><td headers="d299446e14588 d299446e14200" width="20%"><p><code>NNET_REGULARIZER_L2</code></p></td><td headers="d299446e14588 d299446e14205" width="20%"><p>Applies L2 regularization, which penalizes the sum of squared weights.</p></td></tr><tr><td headers="d299446e14588 d299446e14200" width="20%"><p><code>NNET_REGULARIZER_HELDASIDE</code></p></td><td headers="d299446e14588 d299446e14200" width="20%"><p><code>NNET_REGULARIZER_HELDASIDE</code></p></td><td headers="d299446e14588 d299446e14205" width="20%">Uses a held-aside method for regularization. If the total number of training rows is greater than 50000, the default is <code>NNET_REGULARIZER_HELDASIDE</code>.</td></tr><tr><td headers="d299446e14195" width="20%"><p><code>NNET_HELDASIDE_RATIO</code></p></td><td headers="d299446e14662 d299446e14200" width="20%"><p><code>0 <= numeric_expr <=1</code></p></td><td headers="d299446e14662 d299446e14205" width="20%"><p><code>0 <= numeric_expr <=1</code></p></td><td headers="d299446e14662 d299446e14210" width="40%"><p>Define the held ratio for the held-aside method.</p><p>The default value is <code>0.25</code>.</p></td></tr><tr><td headers="d299446e14195" width="20%"><code>NNET_HELDASIDE_MAX_FAIL</code></td><td headers="d299446e14698 d299446e14200" width="20%"><p>A positive integer.</p></td><td headers="d299446e14698 d299446e14205" width="20%"><p>A positive integer.</p></td><td headers="d299446e14698 d299446e14210" width="40%"><p>With <code>NNET_REGULARIZER_HELDASIDE</code>, the training process is stopped early if the network performance on the validation data fails to improve or remains the same for <code>NNET_HELDASIDE_MAX_FAIL</code> epochs in a row.</p><p>The default value is <code>6</code>.</p></td></tr><tr><td headers="d299446e14195" width="20%"><p><code>NNET_REG_LAMBDA</code></p></td><td headers="d299446e14730 d299446e14200" width="20%"><p><code>TO_CHAR(numeric_expr >=0)</code></p></td><td headers="d299446e14730 d299446e14205" width="20%"><p><code>TO_CHAR(numeric_expr >=0)</code></p></td><td headers="d299446e14730 d299446e14210" width="40%"><p>Defines the L2 regularization parameter lambda. This can not be set together with <code>NNET_REGULARIZER_HELDASIDE</code>.</p><p>The default value is <code>1</code>.</p></td></tr></tbody></table>

**Related Topics**

- DBMS\_DATA\_MINING — Solver Settings: LBFGS

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-C45971D9-A874-4546-A0EC-1FF25B229E2B) for information about Neural Network.

### DBMS\_DATA\_MINING - Algorithm Settings: Non-Negative Matrix Factorization

The settings listed in the following table configure the behavior of the Non-negative Matrix Factorization algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.NMFS_NONNEG_SCORING_ENABLE`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'NMFS_NONNEG_SCORING_ENABLE'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

You can query the data dictionary view \* `_MINING_MODEL_SETTINGS` (using the `ALL`, `USER`, or `DBA` prefix) to find the setting values for a model. See [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN20557) for information about \* `_MINING_MODEL_SETTINGS`.

Table 22 NMF Settings

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e15246" width="20%"><p><code>NMFS_CONV_TOLERANCE</code></p></td><td headers="d299446e15265 d299446e15251" width="20%"><p><code>TO_CHAR(0<
                                        </code> <code>numeric_expr</code> <code>
                                    <=
0.5)</code></p></td><td headers="d299446e15265 d299446e15256" width="20%"><p><code>TO_CHAR(0<
                                        </code> <code>numeric_expr</code> <code>
                                    <=0.5)</code></p></td><td headers="d299446e15265 d299446e15258" width="40%"><p>Convergence tolerance for NMF algorithm</p><p>Default is <code>0.05</code></p></td></tr><tr><td headers="d299446e15246" rowspan="2" width="20%"><p><code>NMFS_NONNEGATIVE_SCORING</code></p></td><td headers="d299446e15304 d299446e15251" width="20%"><p><code>NMFS_NONNEG_SCORING_ENABLE</code></p></td><td headers="d299446e15304 d299446e15256" width="20%"><p><code>NMFS_NONNEG_SCORING_ENABLE</code></p></td><td headers="d299446e15304 d299446e15258" width="40%"><p>Whether negative numbers should be allowed in scoring results.</p><p>When set to <code>NMFS_NONNEG_SCORING_ENABLE</code>, negative feature values will be replaced with zeros.</p><p>Default is <code>NMFS_NONNEG_SCORING_ENABLE</code></p></td></tr><tr><td headers="d299446e15304 d299446e15251" width="20%"><p><code>NMFS_NONNEG_SCORING_DISABLE</code></p></td><td headers="d299446e15304 d299446e15251" width="20%"><p><code>NMFS_NONNEG_SCORING_DISABLE</code></p></td><td headers="d299446e15304 d299446e15256" width="20%"><p>When set to <code>NMFS_NONNEG_SCORING_DISABLE</code>, negative feature values will be allowed.</p></td></tr><tr><td headers="d299446e15246" width="20%"><p><code>NMFS_NUM_ITERATIONS</code></p></td><td headers="d299446e15360 d299446e15251" width="20%"><p><code>TO_CHAR(1 <=</code> <code>numeric_expr</code> <code> <=500)</code></p></td><td headers="d299446e15360 d299446e15256" width="20%"><p><code>TO_CHAR(1 <=</code> <code>numeric_expr</code> <code> <=500)</code></p></td><td headers="d299446e15360 d299446e15258" width="40%"><p>Number of iterations for NMF algorithm</p><p>Default is <code>50</code></p></td></tr><tr><td headers="d299446e15246" width="20%"><p><code>NMFS_RANDOM_SEED</code></p></td><td headers="d299446e15401 d299446e15251" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr)</code></p></td><td headers="d299446e15401 d299446e15256" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr)</code></p></td><td headers="d299446e15401 d299446e15258" width="40%"><p>Random seed for NMF algorithm.</p><p>Default is <code>-1</code>.</p></td></tr></tbody></table>

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON058) for information about NMF

### DBMS\_DATA\_MINING - Algorithm Settings: O-Cluster

The settings in the table configure the behavior of the O-Cluster algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.OCLT_SENSITIVITY`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'OCLT_SENSITIVITY'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 23 O-CLuster Settings

| Setting Name | Constant Value | String Value Equivalent | Description |
| --- | --- | --- | --- |
| `OCLT_SENSITIVITY` | `TO_CHAR(0 <=` *numeric\_expr* `<=1)` | `TO_CHAR(0 <=` *numeric\_expr* `<=1)` | A fraction that specifies the peak density required for separating a new cluster. The fraction is related to the global uniform density.  Default is `0.5`. |

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON059) for information about O-Cluster

### DBMS\_DATA\_MINING - Algorithm Settings: Random Forest

These settings configure the behavior of the Random Forest algorithm. Random Forest makes use of the Decision Tree settings to configure the construction of individual trees.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.RFOR_MTRY`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'RFOR_MTRY'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 24 Random Forest Settings

| Setting Name | Constant Value | String Value Equivalent | Description |
| --- | --- | --- | --- |
| `RFOR_MTRY` | `a number >= 0` | `a number >= 0` | Size of the random subset of columns to be considered when choosing a split at a node. For each node, the size of the pool remains the same, but the specific candidate columns change. The default is half of the columns in the model signature. The special value `0` indicates that the candidate pool includes all columns. |
| `RFOR_NUM_TREES` | `1<=` *a number* `<=65535` | `1<=` *a number* `<=65535` | Number of trees in the forest  Default is `20`. |
| `RFOR_SAMPLING_RATIO` | `0<` *a fraction* `<=1` | `0<` *a fraction* `<=1` | Fraction of the training data to be randomly sampled for use in the construction of an individual tree. The default is half of the number of rows in the training data. |

**Related Topics**

- DBMS\_DATA\_MINING — Algorithm Settings: Decision Tree

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-B6506C33-8555-4181-993F-CD7D48B4DA3C) for information about Random Forest

### DBMS\_DATA\_MINING - Algorithm Constants and Settings: Singular Value Decomposition

The following constant affects the behavior of the Singular Value Decomposition algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.SVDS_MAX_NUM_FEATURES`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'SVDS_MAX_NUM_FEATURES'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 25 Singular Value Decomposition

| Constant Name | Constant Value | Description |
| --- | --- | --- |
| `SVDS_MAX_NUM_FEATURES` | 2500 | The maximum number of features supported by SVD. |

The following settings configure the behavior of the Singular Value Decomposition algorithm.

Table 26 Singular Value Decomposition

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e16999" rowspan="2" width="20%"><p><code>SVDS_U_MATRIX_OUTPUT</code></p></td><td headers="d299446e17018 d299446e17004" width="20%"><p><code>SVDS_U_MATRIX_ENABLE</code></p></td><td headers="d299446e17018 d299446e17009" width="20%"><p><code>SVDS_U_MATRIX_ENABLE</code></p></td><td headers="d299446e17018 d299446e17011" width="40%"><p>Specifies whether to persist the U Matrix produced by SVD.</p><p><code>SVDS_U_MATRIX_ENABLE</code>: The U matrix in SVD has as many rows as the number of rows in the build data. To avoid creating a large model, the U matrix is persisted only when <code>SVDS_U_MATRIX_OUTPUT</code> is enabled.</p><p>When <code>SVDS_U_MATRIX_OUTPUT</code> is enabled, the build data must include a case ID. An exception is raised if no case ID is present.</p><p>Default is <code>SVDS_U_MATRIX_DISABLE</code>.</p></td></tr><tr><td headers="d299446e17018 d299446e17004" width="20%"><p><code>SVDS_U_MATRIX_DISABLE</code></p></td><td headers="d299446e17018 d299446e17004" width="20%"><p><code>SVDS_U_MATRIX_DISABLE</code></p></td><td headers="d299446e17018 d299446e17009" width="20%"><p>Does not persist the U Matrix.</p></td></tr><tr><td headers="d299446e16999" rowspan="2" width="20%"><p><code>SVDS_SCORING_MODE</code></p></td><td headers="d299446e17086 d299446e17004" width="20%"><p><code>SVDS_SCORING_SVD</code></p></td><td headers="d299446e17086 d299446e17009" width="20%"><p><code>SVDS_SCORING_SVD</code></p></td><td headers="d299446e17086 d299446e17011" width="40%"><p>Whether to use SVD or PCA scoring for the model.</p><p>When the build data is scored with SVD, the projections will be the same as the U matrix.</p><p>Default is <code>SVDS_SCORING_SVD</code>.</p></td></tr><tr><td headers="d299446e17086 d299446e17004" width="20%"><p><code>SVDS_SCORING_PCA</code></p></td><td headers="d299446e17086 d299446e17004" width="20%"><p><code>SVDS_SCORING_PCA</code></p></td><td headers="d299446e17086 d299446e17009" width="20%"><p>When the build data is scored with PCA, the projections will be the product of the U and S matrices.</p></td></tr><tr><td headers="d299446e16999" rowspan="4" width="20%"><p><code>SVDS_SOLVER </code></p></td><td headers="d299446e17137 d299446e17004" width="20%"><p><code>SVDS_SOLVER_TSSVD</code></p></td><td headers="d299446e17137 d299446e17009" width="20%"><p><code>SVDS_SOLVER_TSSVD</code></p></td><td headers="d299446e17137 d299446e17011" width="40%"><p>This setting indicates the solver to be used for computing SVD of the data. In the case of PCA, the solver setting indicates the type of SVD solver used to compute the PCA for the data. When this setting is not specified the solver type selection is data driven. If the number of attributes is greater than 3240, then the default wide solver is used. Otherwise, the default narrow solver is selected.</p><p>The following are the group of solvers:</p><ul><li><p>Narrow data solvers: for matrices with up to 11500 attributes (<code>TSEIGEN</code>) or up to 8100 attributes (<code>TSSVD</code>).</p></li><li><p>Wide data solvers: for matrices up to 1 million attributes.</p></li></ul><p>For narrow data solvers:</p><ul><li><p>Tall-Skinny SVD uses QR computation TSVD (<code>SVDS_SOLVER_TSSVD</code>)</p></li><li><p>Tall-Skinny SVD uses eigenvalue computation, TSEIGEN (<code>SVDS_SOLVER_TSEIGEN</code>), is the default solver for narrow data.</p></li></ul><p>For wide data solvers:</p><ul><li><p>Stochastic SVD uses QR computation SSVD (<code>SVDS_SOLVER_SSVD</code>), is the default solver for wide data solvers.</p></li><li><p>Stochastic SVD uses eigenvalue computations, STEIGEN (<code>SVDS_SOLVER_STEIGEN</code>).</p></li></ul></td></tr><tr><td headers="d299446e17137 d299446e17004" width="20%"><p><code>SVDS_SOLVER_TSEIGEN</code></p></td><td headers="d299446e17137 d299446e17009" width="20%"><p><code>SVDS_SOLVER_TSEIGEN</code></p></td><td headers="d299446e17137 d299446e17011" width="40%"><p>Tall-Skinny SVD using eigenvalue computation for matrices with up to 11500 attributes. This is the default solver for narrow data.</p></td></tr><tr><td headers="d299446e17137 d299446e17004" width="20%"><p><code>SVDS_SOLVER_SSVD</code></p></td><td headers="d299446e17137 d299446e17009" width="20%"><p><code>SVDS_SOLVER_SSVD</code></p></td><td headers="d299446e17137 d299446e17011" width="40%"><p>Stochastic SVD using QR computation for matrices with up to 1 million attributes. This is the default solver for wide data.</p></td></tr><tr><td headers="d299446e17137 d299446e17004" width="20%"><p><code>SVDS_SOLVER_STEIGEN</code></p></td><td headers="d299446e17137 d299446e17009" width="20%"><p><code>SVDS_SOLVER_STEIGEN</code></p></td><td headers="d299446e17137 d299446e17011" width="40%">Stochastic SVD using eigenvalue computations for matrices with up to 1 million attributes.</td></tr><tr><td headers="d299446e16999" width="20%"><p><code>SVDS_TOLERANCE</code></p></td><td headers="d299446e17287 d299446e17004" width="20%"><p>Range [<code>0, 1</code>]</p></td><td headers="d299446e17287 d299446e17009" width="20%"><p>Range [<code>0, 1</code>]</p></td><td headers="d299446e17287 d299446e17011" width="40%"><p>This setting is used to prune features. Define the minimum value the eigenvalue of a feature as a share of the first eigenvalue to not to prune. Default value is data driven.</p></td></tr><tr><td headers="d299446e16999" width="20%"><p><code>SVDS_RANDOM_SEED</code></p></td><td headers="d299446e17318 d299446e17004" width="20%"><p>Range [<code>0 - 4,294,967,296</code>]</p></td><td headers="d299446e17318 d299446e17009" width="20%"><p>Range [<code>0 - 4,294,967,296</code>]</p></td><td headers="d299446e17318 d299446e17011" width="40%"><p>The random seed value is used for initializing the sampling matrix used by the Stochastic SVD solver. The default is <code>0</code>. The SVD Solver must be set to <code>SSVD</code> or <code>STEIGEN</code>.</p></td></tr><tr><td headers="d299446e16999" width="20%"><p><code>SVDS_OVER_SAMPLING</code></p></td><td headers="d299446e17358 d299446e17004" width="20%"><p>Range [<code>1, 5000</code>].</p></td><td headers="d299446e17358 d299446e17009" width="20%"><p>Range [<code>1, 5000</code>].</p></td><td headers="d299446e17358 d299446e17011" width="40%"><p>This setting is configures the number of columns in the sampling matrix used by the Stochastic SVD solver. The number of columns in this matrix is equal to the requested number of features plus the oversampling setting. The SVD Solver must be set to <code>SSVD</code> or <code>STEIGEN</code>.</p></td></tr><tr><td headers="d299446e16999" width="20%"><p><code>SVDS_POWER_ITERATIONS</code></p></td><td headers="d299446e17396 d299446e17004" width="20%"><p>Range [<code>0, 20</code>].</p></td><td headers="d299446e17396 d299446e17009" width="20%"><p>Range [<code>0, 20</code>].</p></td><td headers="d299446e17396 d299446e17011" width="40%"><p>The power iteration setting improves the accuracy of the SSVD solver. The default is <code>2</code>. The SVD Solver must be set to <code>SSVD</code> or <code>STEIGEN</code>.</p></td></tr></tbody></table>

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON591)

### DBMS\_DATA\_MINING - Algorithm Settings: Support Vector Machine

The settings listed in the following table configure the behavior of the Support Vector Machine algorithm.

The **Constant Value** column specifies constants using the prefix `DBMS_DATA_MINING`. For example,`DBMS_DATA_MINING.SVMS_GAUSSIAN`. Alternatively, you can specify the corresponding string value from the **String Value Equivalent** column without the `DBMS_DATA_MINING` prefix, in single quotes. For example, `'SVMS_GAUSSIAN'`.

**Note:** The distinction between **Constant Value** and **String Value Equivalent** for this algorithm is applicable to Oracle Database 19 *c* and Oracle Database 21 *c*.

Table 27 SVM Settings

<table width="100%"><thead><tr><th width="20%">Setting Name</th><th width="20%">Constant Value</th><th width="20%">String Value Equivalent</th><th width="40%">Description</th></tr></thead><tbody><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_COMPLEXITY_FACTOR</code></p></td><td headers="d299446e17898 d299446e17881" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0</code><code>)</code></p></td><td headers="d299446e17898 d299446e17886" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0</code><code>)</code></p></td><td headers="d299446e17898 d299446e17891" width="40%"><p>Regularization setting that balances the complexity of the model against model robustness to achieve good generalization on new data. SVM uses a data-driven approach to finding the complexity factor.</p><p>Value of complexity factor for SVM algorithm (both classification and regression).</p><p>Default value estimated from the data by the algorithm.</p></td></tr><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_CONV_TOLERANCE</code></p></td><td headers="d299446e17948 d299446e17881" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0)</code></p></td><td headers="d299446e17948 d299446e17886" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0)</code></p></td><td headers="d299446e17948 d299446e17891" width="40%"><p>Convergence tolerance for SVM algorithm.</p><p>Default is <code>
0.0001</code>.</p></td></tr><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_EPSILON</code></p></td><td headers="d299446e17988 d299446e17881" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0)</code></p></td><td headers="d299446e17988 d299446e17886" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0)</code></p></td><td headers="d299446e17988 d299446e17891" width="40%"><p>Regularization setting for regression, similar to complexity factor. Epsilon specifies the allowable residuals, or noise, in the data.</p><p>Value of epsilon factor for SVM regression.</p><p>Default is <code>0.1</code>.</p></td></tr><tr><td headers="d299446e17876" rowspan="2" width="20%"><p><code>SVMS_KERNEL_FUNCTION</code></p></td><td headers="d299446e18037 d299446e17881" width="20%"><p><code>SVMS_GAUSSIAN</code></p></td><td headers="d299446e18037 d299446e17886" width="20%"><p><code>SVMS_GAUSSIAN</code></p></td><td headers="d299446e18037 d299446e17891" width="40%"><p>Kernel for Support Vector Machine. Linear or Gaussian.</p><p><code>SVMS_GAUSSIAN</code>: Uses the Gaussian kernel for SVM.</p>The default value is <code>SVMS_LINEAR</code>.</td></tr><tr><td headers="d299446e18037 d299446e17881" width="20%"><p><code>SVMS_LINEAR</code></p></td><td headers="d299446e18037 d299446e17881" width="20%"><p><code>SVMS_LINEAR</code></p></td><td headers="d299446e18037 d299446e17886" width="20%"><p>Uses the Linear kernel for SVM. This is the default option.</p></td></tr><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_OUTLIER_RATE</code></p></td><td headers="d299446e18091 d299446e17881" width="20%"><p><code>TO_CHAR(</code><code>0<
                                        numeric_expr</code> <code> <1)</code></p></td><td headers="d299446e18091 d299446e17886" width="20%"><p><code>TO_CHAR(</code><code>0<
                                        numeric_expr</code> <code> <1)</code></p></td><td headers="d299446e18091 d299446e17891" width="40%"><p>The desired rate of outliers in the training data. Valid for One-Class SVM models only (anomaly detection).</p><p>Default is <code>0.01</code>.</p></td></tr><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_STD_DEV</code></p></td><td headers="d299446e18135 d299446e17881" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0)</code></p></td><td headers="d299446e18135 d299446e17886" width="20%"><p><code>TO_CHAR(</code><code>numeric_expr</code> <code>
                                    >0)</code></p></td><td headers="d299446e18135 d299446e17891" width="40%"><p>Controls the spread of the Gaussian kernel function. SVM uses a data-driven approach to find a standard deviation value that is on the same scale as distances between typical cases.</p><p>Value of standard deviation for SVM algorithm.</p><p>This is applicable only for Gaussian kernel.</p><p>Default value estimated from the data by the algorithm.</p></td></tr><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_NUM_ITERATIONS</code></p></td><td headers="d299446e18178 d299446e17881" width="20%"><p>Positive integer</p></td><td headers="d299446e18178 d299446e17886" width="20%"><p>Positive integer</p></td><td headers="d299446e18178 d299446e17891" width="40%"><p>This setting sets an upper limit on the number of SVM iterations. The default is system determined because it depends on the SVM solver.</p></td></tr><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_NUM_PIVOTS</code></p></td><td headers="d299446e18201 d299446e17881" width="20%"><p>Range [<code>1; 10000</code>]</p></td><td headers="d299446e18201 d299446e17886" width="20%"><p>Range [<code>1; 10000</code>]</p></td><td headers="d299446e18201 d299446e17891" width="40%"><p>This setting sets an upper limit on the number of pivots used in the Incomplete Cholesky decomposition. It can be set only for non-linear kernels. The default value is <code>200</code>.</p></td></tr><tr><td headers="d299446e17876" width="20%"><p><code>SVMS_BATCH_ROWS</code></p></td><td headers="d299446e18232 d299446e17881" width="20%"><p>Positive integer</p></td><td headers="d299446e18232 d299446e17886" width="20%"><p>Positive integer</p></td><td headers="d299446e18232 d299446e17891" width="40%"><p>This setting applies to SVM models with linear kernel. This setting sets the size of the batch for the SGD solver. An input of 0 triggers a data driven batch size estimate. The default is <code>20000</code>.</p></td></tr><tr><td headers="d299446e17876" rowspan="2" width="20%"><p><code>SVMS_REGULARIZER</code></p></td><td headers="d299446e18258 d299446e17881" width="20%"><p><code>SVMS_REGULARIZER_L1</code></p></td><td headers="d299446e18258 d299446e17886" width="20%"><p><code>SVMS_REGULARIZER_L1</code></p></td><td headers="d299446e18258 d299446e17891" width="40%"><p>This setting controls the type of regularization that the SGD SVM solver uses. The setting can be used only for linear SVM models. The default is system determined because it depends on the potential model size.</p><p><code>SVMS_REGULARIZER_L1</code>: Uses L1 regularization.</p></td></tr><tr><td headers="d299446e18258 d299446e17881" width="20%"><p><code>SVMS_REGULARIZER_L2</code></p></td><td headers="d299446e18258 d299446e17886" width="20%"><p><code>SVMS_REGULARIZER_L2</code></p></td><td headers="d299446e18258 d299446e17891" width="40%"><p>Uses L2 regularization.</p></td></tr><tr><td headers="d299446e17876" rowspan="2" width="20%"><p><code>SVMS_SOLVER</code></p></td><td headers="d299446e18311 d299446e17881" width="20%"><p><code>SVMS_SOLVER_SGD</code> (Sub-Gradient Descend)</p></td><td headers="d299446e18311 d299446e17886" width="20%"><p><code>SVMS_SOLVER_SGD</code> (Sub-Gradient Descend)</p></td><td headers="d299446e18311 d299446e17891" width="40%"><p>Enables to choose the SVM solver. The SGD solver cannot be selected if the kernel is non-linear. The default value is system determined.</p><p><code>SVMS_SOLVER_SGD</code>: Uses Sub-Gradient Descent solver.</p></td></tr><tr><td headers="d299446e18311 d299446e17881" width="20%"><p><code>SVMS_SOLVER_IPM</code> (Interior Point Method)</p></td><td headers="d299446e18311 d299446e17886" width="20%"><p><code>SVMS_SOLVER_IPM</code> (Interior Point Method)</p></td><td headers="d299446e18311 d299446e17891" width="40%"><p>Uses Interior Point Method solver.</p></td></tr></tbody></table>

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON025) for information about SVM

### DBMS\_DATA\_MINING - Solver Settings

Oracle Data Mining algorithms can use different solvers. Solver settings can be provided at build time in the setting table.

**Related Topics**

- DBMS\_DATA\_MINING — Solver Settings: ADMM
- DBMS\_DATA\_MINING — Solver Settings: LBFGS

### DBMS\_DATA\_MINING - Solver Settings: ADMM

The settings listed in the following table configure the behavior of Alternating Direction Method of Multipliers (ADMM). Generalized Linear Models (GLM) use these settings.

Table 28 DBMS\_DATA\_MINING ADMM Settings

| Settings Name | Setting Value | Description |
| --- | --- | --- |
| `ADMM_CONSENSUS` | A positive integer | It is a ADMM’s consensus parameter. The value must be a positive number. The default value is `0.1`. |
| `ADMM_ITERATIONS` | A positive integer | The number of `ADMM` iterations. The value must be a positive integer. The default value is `50`. |
| `ADMM_TOLERANCE` | A positive integer | It is a tolerance parameter. The value must be a positive number. The default value is `0.0001` |

**Related Topics**

- [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-F36DDDDB-3A87-4C97-8000-EBF009E794C2)

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-C45971D9-A874-4546-A0EC-1FF25B229E2B) for information about Neural Network

### DBMS\_DATA\_MINING - Solver Settings: LBFGS

The settings listed in the following table configure the behavior of L-BFGS. Neural Network and Generalized Linear Models (GLM) use these settings.

Table 29 DBMS\_DATA\_MINING L-BFGS Settings

| Setting Name | Setting Value | Description |
| --- | --- | --- |
| `LBFGS_GRADIENT_TOLERANCE` | `TO_CHAR (numeric_expr >0)` | Defines gradient infinity norm tolerance for L-BFGS. Default value is `1E-9`. |
| `LBFGS_HISTORY_DEPTH` | The value must be a positive integer. | Defines the number of historical copies kept in L-BFGS solver.  The default value is `20`. |
| `LBFGS_SCALE_HESSIAN` | `LBFGS_SCALE_HESSIAN_ENABLE`  `LBFGS_SCALE_HESSIAN_DISABLE` | Defines whether to scale Hessian in L-BFGS or not.  Default value is `LBFGS_SCALE_HESSIAN_ENABLE`. |

**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON-GUID-C45971D9-A874-4546-A0EC-1FF25B229E2B) for information about Neural Network

### DBMS\_DATA\_MINING Datatypes

The `DBMS_DATA_MINING` package defines object datatypes for mining transactional data. The package also defines a type for user-specified transformations. These types are called `DM_NESTED_` *n*, where *n* identifies the Oracle datatype of the nested attributes.

The Data Mining object datatypes are described in the following table:

Table 30 DBMS\_DATA\_MINING Summary of Datatypes

| Datatype | Description |
| --- | --- |
| `DM_NESTED_BINARY_DOUBLE` | The name and value of a numerical attribute of type `BINARY_DOUBLE`. |
| `DM_NESTED_BINARY_DOUBLES` | A collection of `DM_NESTED_BINARY_DOUBLE`. |
| `DM_NESTED_BINARY_FLOAT` | The name and value of a numerical attribute of type `BINARY_FLOAT`. |
| `DM_NESTED_BINARY_FLOATS` | A collection of `DM_NESTED_BINARY_FLOAT`. |
| `DM_NESTED_CATEGORICAL` | The name and value of a categorical attribute of type `CHAR`, `VARCHAR`, or `VARCHAR2`. |
| `DM_NESTED_CATEGORICALS` | A collection of `DM_NESTED_CATEGORICAL`. |
| `DM_NESTED_NUMERICAL` | The name and value of a numerical attribute of type `NUMBER` or `FLOAT`. |
| `DM_NESTED_NUMERICALS` | A collection of `DM_NESTED_NUMERICAL`. |
| `ORA_MINING_VARCHAR2_NT` | A table of `VARCHAR2(4000)`. |
| `TRANSFORM_LIST` | A list of user-specified transformations for a model. Accepted as a parameter by the CREATE\_MODEL Procedure.  This collection type is defined in the [DBMS\_DATA\_MINING\_TRANSFORM](DBMS_DATA_MINING_TRANSFORM.md) package. |

For more information about mining nested data, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG006).

**Note:** Starting from Oracle Database 12 *c* Release 2, `*GET_MODEL_DETAILS` are deprecated and are replaced with *Model Detail Views*. See [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-AF7C531D-5327-4456-854C-9D6424C5F9EC).

### Deprecated Types

This topic contains tables listing deprecated types.

The `DBMS_DATA_MINING` package defines object datatypes for storing information about model attributes. Most of these types are returned by the table functions `GET` \_ *n*, where *n* identifies the type of information to return. These functions take a model name as input and return the requested information as a collection of rows.

For a list of the `GET` functions, see “ Summary of DBMS\_DATA\_MINING Subprograms ”.

All the table functions use pipelining, which causes each row of output to be materialized as it is read from model storage, without waiting for the generation of the complete table object. For more information on pipelined, parallel table functions, consult the [*Oracle Database PL/SQL Language Reference.*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=LNPLS01210)

Table 31 DBMS\_DATA\_MINING Summary of Deprecated Datatypes

| Datatype | Description |
| --- | --- |
| `DM_CENTROID` | The centroid of a cluster. |
| `DM_CENTROIDS` | A collection of `DM_CENTROID`. A member of `DM_CLUSTER`. |
| `DM_CHILD` | A child node of a cluster. |
| `DM_CHILDREN` | A collection of `DM_CHILD`. A member of `DM_CLUSTER`. |
| `DM_CLUSTER` | A cluster. A cluster includes `DM_PREDICATES`, `DM_CHILDREN`, `DM_CENTROIDS`, and `DM_HISTOGRAMS`. It also includes a `DM_RULE`.  See also, Table 53-33. |
| `DM_CLUSTERS` | A collection of `DM_CLUSTER`. Returned by GET\_MODEL\_DETAILS\_KM Function, GET\_MODEL\_DETAILS\_OC Function, and GET\_MODEL\_DETAILS\_EM Function.  See also, Table 53-33. |
| `DM_CONDITIONAL` | The conditional probability of an attribute in a Naive Bayes model. |
| `DM_CONDITIONALS` | A collection of `DM_CONDITIONAL`. Returned by GET\_MODEL\_DETAILS\_NB Function. |
| `DM_COST_ELEMENT` | The actual and predicted values in a cost matrix. |
| `DM_COST_MATRIX` | A collection of `DM_COST_ELEMENT`. Returned by GET\_MODEL\_COST\_MATRIX Function. |
| `DM_EM_COMPONENT` | A component of an Expectation Maximization model. |
| `DM_EM_COMPONENT_SET` | A collection of `DM_EM_COMPONENT`. Returned by GET\_MODEL\_DETAILS\_EM\_COMP Function. |
| `DM_EM_PROJECTION` | A projection of an Expectation Maximization model. |
| `DM_EM_PROJECTION_SET` | A collection of `DM_EM_PROJECTION`. Returned by GET\_MODEL\_DETAILS\_EM\_PROJ Function. |
| `DM_GLM_COEFF` | The coefficient and associated statistics of an attribute in a Generalized Linear Model. |
| `DM_GLM_COEFF_SET` | A collection of `DM_GLM_COEFF`. Returned by GET\_MODEL\_DETAILS\_GLM Function. |
| `DM_HISTOGRAM_BIN` | A histogram associated with a cluster. |
| `DM_HISTOGRAMS` | A collection of `DM_HISTOGRAM_BIN`. A member of `DM_CLUSTER`.  See also, Table 53-33. |
| `DM_ITEM` | An item in an association rule. |
| `DM_ITEMS` | A collection of `DM_ITEM`. |
| `DM_ITEMSET` | A collection of `DM_ITEMS`. |
| `DM_ITEMSETS` | A collection of `DM_ITEMSET`. Returned by GET\_FREQUENT\_ITEMSETS Function. |
| `DM_MODEL_GLOBAL_DETAIL` | High-level statistics about a model. |
| `DM_MODEL_GLOBAL_DETAILS` | A collection of `DM_MODEL_GLOBAL_DETAIL`. Returned by GET\_MODEL\_DETAILS\_GLOBAL Function. |
| `DM_NB_DETAIL` | Information about an attribute in a Naive Bayes model. |
| `DM_NB_DETAILS` | A collection of `DM_DB_DETAIL`. Returned by GET\_MODEL\_DETAILS\_NB Function. |
| `DM_NMF_ATTRIBUTE` | An attribute in a feature of a Non-Negative Matrix Factorization model. |
| `DM_NMF_ATTRIBUTE_SET` | A collection of `DM_NMF_ATTRIBUTE`. A member of `DM_NMF_FEATURE`. |
| `DM_NMF_FEATURE` | A feature in a Non-Negative Matrix Factorization model. |
| `DM_NMF_FEATURE_SET` | A collection of `DM_NMF_FEATURE`. Returned by GET\_MODEL\_DETAILS\_NMF Function. |
| `DM_PREDICATE` | Antecedent and consequent in a rule. |
| `DM_PREDICATES` | A collection of `DM_PREDICATE`. A member of `DM_RULE` and `DM_CLUSTER`. Predicates are returned by GET\_ASSOCIATION\_RULES Function, GET\_MODEL\_DETAILS\_EM Function, GET\_MODEL\_DETAILS\_KM Function, and GET\_MODEL\_DETAILS\_OC Function.  See also, Table 53-33. |
| `DM_RANKED_ATTRIBUTE` | An attribute ranked by its importance in an Attribute Importance model. |
| `DM_RANKED_ATTRIBUTES` | A collection of `DM_RANKED_ATTRIBUTE`. Returned by GET\_MODEL\_DETAILS\_AI Function. |
| `DM_RULE` | A rule that defines a conditional relationship.  The rule can be one of the association rules returned by GET\_ASSOCIATION\_RULES Function, or it can be a rule associated with a cluster in the collection of clusters returned by GET\_MODEL\_DETAILS\_KM Function and GET\_MODEL\_DETAILS\_OC Function.  See also, Table 53-33. |
| `DM_RULES` | A collection of `DM_RULE`. Returned by GET\_ASSOCIATION\_RULES Function.  See also, Table 53-33. |
| `DM_SVD_MATRIX` | A factorized matrix S, V, or U returned by a Singular Value Decomposition model. |
| `DM_SVD_MATRIX_SET` | A collection of `DM_SVD_MATRIX`. Returned by GET\_MODEL\_DETAILS\_SVD Function. |
| `DM_SVM_ATTRIBUTE` | The name, value, and coefficient of an attribute in a Support Vector Machine model. |
| `DM_SVM_ATTRIBUTE_SET` | A collection of `DM_SVM_ATTRIBUTE`. Returned by GET\_MODEL\_DETAILS\_SVM Function. Also a member of `DM_SVM_LINEAR_COEFF`. |
| `DM_SVM_LINEAR_COEFF` | The linear coefficient of each attribute in a Support Vector Machine model. |
| `DM_SVM_LINEAR_COEFF_SET` | A collection of `DM_SVM_LINEAR_COEFF`. Returned by GET\_MODEL\_DETAILS\_SVM Function for an SVM model built using the linear kernel. |
| `DM_TRANSFORM` | The transformation and reverse transformation expressions for an attribute. |
| `DM_TRANSFORMS` | A collection of `DM_TRANSFORM`. Returned by GET\_MODEL\_TRANSFORMATIONS Function. |

**Return Values for Clustering Algorithms**

The table contains description of `DM_CLUSTER` return value columns, nested table columns, and rows.

Table 32 DM\_CLUSTER Return Values for Clustering Algorithms

| Return Value | Description |
| --- | --- |
| `DM_CLUSTERS` | A set of rows of type `DM_CLUSTER`. The rows have the following columns:  ```md (id NUMBER, cluster_id VARCHAR2(4000), record_count NUMBER, parent NUMBER, tree_level NUMBER, dispersion NUMBER, split_predicate DM_PREDICATES, child DM_CHILDREN, centroid DM_CENTROIDS, histogram DM_HISTOGRAMS, rule DM_RULE) ``` |
| `DM_PREDICATE` | The `antecedent` and `consequent` columns each return nested tables of type `DM_PREDICATES`. The rows, of type `DM_PREDICATE`, have the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), conditional_operator CHAR(2)/*=,<>,<,>,<=,>=*/, attribute_num_value NUMBER, attribute_str_value VARCHAR2(4000), attribute_support NUMBER, attribute_confidence NUMBER) ``` |

**DM\_CLUSTER Fields**

The following table describes `DM_CLUSTER` fields.

Table 33 DM\_CLUSTER Fields

| Column Name | Description |
| --- | --- |
| `id` | Cluster identifier |
| `cluster_id` | The ID of a cluster in the model |
| `record_count` | Specifies the number of records |
| `parent` | Parent ID |
| `tree_level` | Specifies the number of splits from the root |
| `dispersion` | A measure used to quantify whether a set of observed occurrences are dispersed compared to a standard statistical model. |
| `split_predicate` | The `split_predicate` column of `DM_CLUSTER` returns a nested table of type `DM_PREDICATES`. Each row, of type `DM_PREDICATE`, has the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), conditional_operator CHAR(2) /*=,<>,<,>,<=,>=*/, attribute_num_value NUMBER, attribute_str_value VARCHAR2(4000), attribute_support NUMBER, attribute_confidence NUMBER) ```  Note: The Expectation Maximization algorithm uses all the fields except `dispersion` and `split_predicate`. |
| `child` | The `child` column of `DM_CLUSTER` returns a nested table of type `DM_CHILDREN`. The rows, of type `DM_CHILD`, have a single column of type `NUMBER`, which contains the identifiers of each child. |
| `centroid` | The `centroid` column of `DM_CLUSTER` returns a nested table of type `DM_CENTROIDS`. The rows, of type `DM_CENTROID`, have the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), mean NUMBER, mode_value VARCHAR2(4000), variance NUMBER) ``` |
| `histogram` | The `histogram` column of `DM_CLUSTER` returns a nested table of type `DM_HISTOGRAMS`. The rows, of type `DM_HISTOGRAM_BIN`, have the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), bin_id NUMBER, lower_bound NUMBER, upper_bound NUMBER, label VARCHAR2(4000), count NUMBER) ``` |
| `rule` | The `rule` column of `DM_CLUSTER` returns a single row of type `DM_RULE`. The columns are:  ```md (rule_id INTEGER, antecedent DM_PREDICATES, consequent DM_PREDICATES, rule_support NUMBER, rule_confidence NUMBER, rule_lift NUMBER, antecedent_support NUMBER, consequent_support NUMBER, number_of_items INTEGER) ``` |

**Usage Notes**

- The table function pipes out rows of type `DM_CLUSTER`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.
- For descriptions of predicates (`DM_PREDICATE`) and rules (`DM_RULE`), see [GET\_ASSOCIATION\_RULES Function](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DATA_MINING.html#GUID-4669DF41-ED9B-4A61-A9A2-3B553FF23998 "The GET_ASSOCIATION_RULES function returns the rules produced by an Association model. Starting from Oracle Database 12c Release 2, this function is deprecated. See \"Model Detail Views\" in Oracle Data Mining User's Guide").

### Summary of DBMS\_DATA\_MINING Subprograms

This table summarizes the subprograms included in the `DBMS_DATA_MINING` package.

The `GET_*` interfaces are replaced by model views. Oracle recommends that users leverage model detail views instead. For more information, refer to “Model Detail Views” in *Oracle Data Mining User’s Guide* and “Static Data Dictionary Views: `ALL_ALL_TABLES` to `ALL_OUTLINES` ” in *Oracle Database Reference*.

Table 34 DBMS\_DATA\_MINING Package Subprograms

| Subprogram | Purpose |
| --- | --- |
| ADD\_COST\_MATRIX Procedure | Adds a cost matrix to a classification model |
| ADD\_PARTITION Procedure | Adds single or multiple partitions in an existing partition model |
| ALTER\_REVERSE\_EXPRESSION Procedure | Changes the reverse transformation expression to an expression that you specify |
| APPLY Procedure | Applies a model to a data set (scores the data) |
| COMPUTE\_CONFUSION\_MATRIX Procedure | Computes the confusion matrix for a classification model |
| COMPUTE\_CONFUSION\_MATRIX\_PART Procedure | Computes the evaluation matrix for partitioned models |
| COMPUTE\_LIFT Procedure | Computes lift for a classification model |
| COMPUTE\_LIFT\_PART Procedure | Computers lift for partitioned models |
| COMPUTE\_ROC Procedure | Computes Receiver Operating Characteristic (ROC) for a classification model |
| COMPUTE\_ROC\_PART Procedure | Computes Receiver Operating Characteristic (ROC) for a partitioned model |
| CREATE\_MODEL Procedure | Creates a model |
| CREATE\_MODEL2 Procedure | Creates a model without extra persistent stages |
| Create Model Using Registration Information | Fetches setting information from JSON object |
| DROP\_ALGORITHM Procedure | Drops the registered algorithm information. |
| DROP\_PARTITION Procedure | Drops a single partition |
| DROP\_MODEL Procedure | Drops a model |
| EXPORT\_MODEL Procedure | Exports a model to a dump file |
| EXPORT\_SERMODEL Procedure | Exports a model in a serialized format |
| FETCH\_JSON\_SCHEMA Procedure | Fetches and reads JSON schema from `all_mining_algorithms` view |
| GET\_MODEL\_COST\_MATRIX Function | Returns the cost matrix for a model |
| IMPORT\_MODEL Procedure | Imports a model into a user schema |
| IMPORT\_SERMODEL Procedure | Imports a serialized model back into the database |
| JSON Schema for R Extensible Algorithm | Displays flexibility in creating JSON schema for R Extensible |
| REGISTER\_ALGORITHM Procedure | Registers a new algorithm |
| RANK\_APPLY Procedure | Ranks the predictions from the `APPLY` results for a classification model |
| REMOVE\_COST\_MATRIX Procedure | Removes a cost matrix from a model |
| RENAME\_MODEL Procedure | Renames a model |

**Deprecated GET\_MODEL\_DETAILS**

Starting from Oracle Database 12 *c* Release 2, the following `GET_MODEL_DETAILS` are deprecated:

Table 35 Deprecated GET\_MODEL\_DETAILS Functions

| Subprogram | Purpose |
| --- | --- |
| GET\_ASSOCIATION\_RULES Function | Returns the rules from an association model |
| GET\_FREQUENT\_ITEMSETS Function | Returns the frequent itemsets for an association model |
| GET\_MODEL\_DETAILS\_AI Function | Returns details about an Attribute Importance model |
| GET\_MODEL\_DETAILS\_EM Function | Returns details about an Expectation Maximization model |
| GET\_MODEL\_DETAILS\_EM\_COMP Function | Returns details about the parameters of an Expectation Maximization model |
| GET\_MODEL\_DETAILS\_EM\_PROJ Function | Returns details about the projects of an Expectation Maximization model |
| GET\_MODEL\_DETAILS\_GLM Function | Returns details about a Generalized Linear Model |
| GET\_MODEL\_DETAILS\_GLOBAL Function | Returns high-level statistics about a model |
| GET\_MODEL\_DETAILS\_KM Function | Returns details about a *k* -Means model |
| GET\_MODEL\_DETAILS\_NB Function | Returns details about a Naive Bayes model |
| GET\_MODEL\_DETAILS\_NMF Function | Returns details about a Non-Negative Matrix Factorization model |
| GET\_MODEL\_DETAILS\_OC Function | Returns details about an O-Cluster model |
| GET\_MODEL\_SETTINGS Function | Returns the settings used to build the given model  This function is replaced with `USER/ALL/DBA_MINING_MODEL_SETTINGS` |
| GET\_MODEL\_SIGNATURE Function | Returns the list of columns from the build input table  This function is replaced with `USER/ALL/DBA_MINING_MODEL_ATTRIBUTES` |
| GET\_MODEL\_DETAILS\_SVD Function | Returns details about a Singular Value Decomposition model |
| GET\_MODEL\_DETAILS\_SVM Function | Returns details about a Support Vector Machine model with a linear kernel |
| GET\_MODEL\_TRANSFORMATIONS Function | Returns the transformations embedded in a model  This function is replaced with `USER/ALL/DBA_MINING_MODEL_XFORMS` |
| GET\_MODEL\_DETAILS\_XML Function | Returns details about a Decision Tree model |
| GET\_TRANSFORM\_LIST Procedure | Converts between two different transformation specification formats |

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-AF7C531D-5327-4456-854C-9D6424C5F9EC)
- [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN-GUID-41B62782-83FA-4066-8C56-0D0B66CC0EC7)

### ADD\_COST\_MATRIX Procedure

The `ADD_COST_MATRIX` procedure associates a cost matrix table with a Classification model. The cost matrix biases the model by assigning costs or benefits to specific model outcomes.

The cost matrix is stored with the model and taken into account when the model is scored.

You can also specify a cost matrix inline when you invoke a Data Mining SQL function for scoring. To view the scoring matrix for a model, query the `DM$VC` prefixed model view. Refer to [Model Detail View for Classification Algorithm](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-38E4FB18-14B2-4A82-B5CE-D2B0EF26DD13).

To obtain the default scoring matrix for a model, query the `DM$VC` prefixed model view. To remove the default scoring matrix from a model, use the `REMOVE_COST_MATRIX` procedure. See “ GET\_MODEL\_COST\_MATRIX Function ” and “ REMOVE\_COST\_MATRIX Procedure ”.

**See Also:**

- “Biasing a Classification Model” in [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON050) for more information about costs
- [*Oracle Database SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SQLRF06210) for syntax of inline cost matrix
- *Oracle Data Mining User’s Guide*

**Syntax**

```md
DBMS_DATA_MINING.ADD_COST_MATRIX (
       model_name                IN VARCHAR2,
       cost_matrix_table_name    IN VARCHAR2,
       cost_matrix_schema_name   IN VARCHAR2 DEFAULT NULL);
       partition_name            IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 36 ADD\_COST\_MATRIX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is assumed. |
| `cost_matrix_table_name` | Name of the cost matrix table (described in Table 53-37). |
| `cost_matrix_schema_name` | Schema of the cost matrix table. If no schema is specified, then the current schema is used. |
| `partition_name` | Name of the partition in a partitioned model |

**Usage Notes**

1. If the model is not in your schema, then `ADD_COST_MATRIX` requires the `ALTER ANY MINING MODEL` system privilege or the `ALTER` object privilege for the mining model.
2. The cost matrix table must have the columns shown in Table 53-37.
	Table 37 Required Columns in a Cost Matrix Table
	| Column Name | Datatype |
	| --- | --- |
	| `ACTUAL_TARGET_VALUE` | Valid target data type |
	| `PREDICTED_TARGET_VALUE` | Valid target data type |
	| `COST` | `NUMBER,``FLOAT`, `BINARY_DOUBLE`, or `BINARY_FLOAT` |
	**See Also:** [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG593) for valid target datatypes
3. The types of the actual and predicted target values must be the same as the type of the model target. For example, if the target of the model is `BINARY_DOUBLE`, then the actual and predicted values must be `BINARY_DOUBLE`. If the actual and predicted values are `CHAR` or `VARCHAR`, then `ADD_COST_MATRIX` treats them as `VARCHAR2` internally.
	If the types do not match, or if the actual or predicted value is not a valid target value, then the `ADD_COST_MATRIX` procedure raises an error.
	**Note:**
	If a reverse transformation is associated with the target, then the actual and predicted values must be consistent with the target after the reverse transformation has been applied.
	See “Reverse Transformations and Model Transparency” under the “About Transformation Lists” section in [DBMS\_DATA\_MINING\_TRANSFORM Operational Notes](DBMS_DATA_MINING_TRANSFORM.md) for more information.
4. Since a benefit can be viewed as a negative cost, you can specify a benefit for a given outcome by providing a negative number in the `costs` column of the cost matrix table.
5. All Classification algorithms can use a cost matrix for scoring. The Decision Tree algorithm can also use a cost matrix at build time. If you want to build a Decision Tree model with a cost matrix, specify the cost matrix table name in the `CLAS_COST_TABLE_NAME` setting in the settings table for the model. See Table 53-7.
	The cost matrix used to create a Decision Tree model becomes the default scoring matrix for the model. If you want to specify different costs for scoring, use the `REMOVE_COST_MATRIX` procedure to remove the cost matrix and the `ADD_COST_MATRIX` procedure to add a new one.
6. Scoring on a partitioned model is partition-specific. Scoring cost matrices can be added to or removed from an individual partition in a partitioned model. If `PARTITION_NAME` is NOT NULL, then the model must be a partitioned model. The `COST_MATRIX` is added to that partition of the partitioned model.
	If the `PARTITION_NAME` is NULL, but the model is a partitioned model, then the `COST_MATRIX` table is added to every partition in the model.

**Example**

This example creates a cost matrix table called `COSTS_NB` and adds it to a Naive Bayes model called `NB_SH_CLAS_SAMPLE`. The model has a binary target: 1 means that the customer responds to a promotion; 0 means that the customer does not respond. The cost matrix assigns a cost of.25 to misclassifications of customers who do not respond and a cost of.75 to misclassifications of customers who do respond. This means that it is three times more costly to misclassify responders than it is to misclassify non-responders.

```md
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

### ADD\_PARTITION Procedure

`ADD_PARTITION` procedure supports a single or multiple partition addition to an existing partitioned model.

The `ADD_PARTITION` procedure derives build settings and user-defined expressions from the existing model. The target column must exist in the input data query when adding partitions to a supervised model.

**Syntax**

```md
DBMS_DATA_MINING.ADD_PARTITION (
      model_name                IN VARCHAR2,
      data_query                IN CLOB,
      add_options               IN VARCHAR2 DEFAULT ERROR);
```

**Parameters**

Table 38 ADD\_PARTITION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `data_query` | An arbitrary SQL statement that provides data to the model build. The user must have privilege to evaluate this query. |
| `add_options` | Allows users to control the conditional behavior of ADD for cases where rows in the input dataset conflict with existing partitions in the model. The following are the possible values:  - `REPLACE`: Replaces the existing partition for which the conflicting keys are found. - `ERROR`: Terminates the ADD operation without adding any partitions. - `IGNORE`: Eliminates the rows having the conflicting keys.  Note:  For better performance, Oracle recommends using `DROP_PARTITION` followed by the `ADD_PARTITION` instead of using the `REPLACE` option. |

### ALTER\_REVERSE\_EXPRESSION Procedure

This procedure replaces a reverse transformation expression with an expression that you specify. If the attribute does not have a reverse expression, the procedure creates one from the specified expression.

You can also use this procedure to customize the output of clustering, feature extraction, and anomaly detection models.

**Syntax**

```md
DBMS_DATA_MINING.ALTER_REVERSE_EXPRESSION (
         model_name             VARCHAR2,
         expression             CLOB,
         attribute_name         VARCHAR2 DEFAULT NULL,
         attribute_subname      VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 39 ALTER\_REVERSE\_EXPRESSION Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `expression` | An expression to replace the reverse transformation associated with the attribute. |
| `attribute_name` | Name of the attribute. Specify `NULL` if you wish to apply `expression` to a cluster, feature, or One-Class SVM prediction. |
| `attribute_subname` | Name of the nested attribute if `attribute_name` is a nested column, otherwise `NULL`. |

**Usage Notes**

1. For purposes of model transparency, Oracle Data Mining provides reverse transformations for transformations that are embedded in a model. Reverse transformations are applied to the attributes returned in model details (`GET_MODEL_DETAILS_` \* functions) and to the scored target of predictive models.
	**See Also:** “About Transformation Lists” under [DBMS\_DATA\_MINING\_TRANSFORM Operational Notes](DBMS_DATA_MINING_TRANSFORM.md)
2. If you alter the reverse transformation for the target of a model that has a cost matrix, you must specify a transformation expression that has the same type as the actual and predicted values in the cost matrix. Also, the reverse transformation that you specify must result in values that are present in the cost matrix.
	**See Also:** “ ADD\_COST\_MATRIX Procedure ” and [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON050) for information about cost matrixes.
3. To prevent reverse transformation of an attribute, you can specify `NULL` for *expression*.
4. The reverse transformation expression can contain a reference to a PL/SQL function that returns a valid Oracle datatype. For example, you could define a function like the following for a categorical attribute named `blood_pressure` that has values ‘Low’, ‘Medium’ and ‘High’.
	```md
	CREATE OR REPLACE FUNCTION numx(c char) RETURN NUMBER IS
	  BEGIN
	    CASE c WHEN ''Low'' THEN RETURN 1;
	           WHEN ''Medium'' THEN RETURN 2;
	           WHEN ''High'' THEN RETURN 3;
	           ELSE RETURN null;
	    END CASE;
	  END numx;
	```
	Then you could invoke `ALTER_REVERSE_EXPRESION` for `blood_pressure` as follows.
	```md
	EXEC dbms_data_mining.alter_reverse_expression(
	             '<model_name>', 'NUMX(blood_pressure)', 'blood_pressure');
	```
5. You can use `ALTER_REVERSE_EXPRESSION` to label clusters produced by clustering models and features produced by feature extraction.
	You can use `ALTER_REVERSE_EXPRESSION` to replace the zeros and ones returned by anomaly-detection models. By default, anomaly-detection models label anomalous records with 0 and all other records with 1.
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON006) for information about anomaly detection

**Examples**

1. In this example, the target (`affinity_card`) of the model `CLASS_MODEL` is manipulated internally as `yes` or `no` instead of `1` or `0` but returned as `1` s and `0` s when scored. The `ALTER_REVERSE_EXPRESSION` procedure causes the target values to be returned as `TRUE` or `FALSE`.
	The data sets `MINING_DATA_BUILD` and `MINING_DATA_TEST` are included with the Oracle Data Mining sample programs. See [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714) for information about the sample programs.
```md
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
1. This example specifies labels for the clusters that result from the `sh_clus` model. The labels consist of the word “Cluster” and the internal numeric identifier for the cluster.
```md
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

### APPLY Procedure

The `APPLY` procedure applies a mining model to the data of interest, and generates the results in a table. The `APPLY` procedure is also referred to as **scoring**.

For predictive mining functions, the `APPLY` procedure generates predictions in a target column. For descriptive mining functions such as Clustering, the `APPLY` process assigns each case to a cluster with a probability.

In Oracle Data Mining, the `APPLY` procedure is not applicable to Association models and Attribute Importance models.

```md
<div class="infoboxnote" markdown="1">

**Note:**

Scoring can also be performed directly in SQL using the Data Mining functions. See

- "Data Mining Functions" in [*Oracle Database SQL Language Reference*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SQLRF20030)

- "Scoring and Deployment" in [*Oracle Data Mining User's Guide*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG004)

</div>
```

**Syntax**

```md
DBMS_DATA_MINING.APPLY (
      model_name           IN VARCHAR2,
      data_table_name      IN VARCHAR2,
      case_id_column_name  IN VARCHAR2,
      result_table_name    IN VARCHAR2,
      data_schema_name     IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 40 *APPLY Procedure Parameters*

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `data_table_name` | Name of table or view containing the data to be scored |
| `case_id_column_name` | Name of the case identifier column |
| `result_table_name` | Name of the table in which to store apply results |
| `data_schema_name` | Name of the schema containing the data to be scored |

**Usage Notes**

1. The data provided for `APPLY` must undergo the same preprocessing as the data used to create and test the model. When you use Automatic Data Preparation, the preprocessing required by the algorithm is handled for you by the model: both at build time and apply time. (See “ Automatic Data Preparation ”.)
2. `APPLY` creates a table in the user’s schema to hold the results. The columns are algorithm-specific.
	The columns in the results table are listed in Table 53-41 through Table 53-45. The case ID column name in the results table will match the case ID column name provided by you. The type of the incoming case ID column is also preserved in `APPLY` output.

**Note:** Make sure that the case ID column does not have the same name as one of the columns that will be created by `APPLY`. For example, when applying a Classification model, the case ID in the scoring data must not be `PREDICTION` or `PROBABILITY` (See Table 53-41).

1. The datatype for the `PREDICTION`, `CLUSTER_ID`, and `FEATURE_ID` output columns is influenced by any reverse expression that is embedded in the model by the user. If the user does not provide a reverse expression that alters the scored value type, then the types will conform to the descriptions in the following tables. See “ ALTER\_REVERSE\_EXPRESSION Procedure ”.
2. If the model is partitioned, the `result_table_name` can contain results from different partitions depending on the data from the input data table. An additional column called `PARTITION_NAME` is added to the result table indicating the partition name that is associated with each row.
	For a non-partitioned model, the behavior does not change.

**Classification**

The results table for Classification has the columns described in Table 53-41. If the target of the model is categorical, the `PREDICTION` column will have a `VARCHAR2` datatype. If the target has a binary type, the `PREDICTION` column will have the binary type of the target.

Table 41 APPLY Results Table for Classification

| Column Name | Datatype |
| --- | --- |
| `Case ID column name` | Type of the case ID |
| `PREDICTION` | Type of the target |
| `PROBABILITY` | `BINARY_DOUBLE` |

**Anomaly Detection**

The results table for Anomaly Detection has the columns described in Table 53-42.

Table 42 APPLY Results Table for Anomaly Detection

| Column Name | Datatype |
| --- | --- |
| `Case ID column name` | Type of the case ID |
| `PREDICTION` | `NUMBER` |
| `PROBABILITY` | `BINARY_DOUBLE` |

**Regression**

The results table for Regression has the columns described in APPLY Procedure.

Table 43 APPLY Results Table for Regression

| Column Name | Datatype |
| --- | --- |
| `Case ID column name` | Type of the case ID |
| `PREDICTION` | Type of the target |

**Clustering**

Clustering is an unsupervised mining function, and hence there are no targets. The results of an `APPLY` procedure will contain simply the cluster identifier corresponding to a case, and the associated probability. The results table has the columns described in Table 53-44.

Table 44 APPLY Results Table for Clustering

| Column Name | Datatype |
| --- | --- |
| `Case ID column name` | Type of the case ID |
| `CLUSTER_ID` | `NUMBER` |
| `PROBABILITY` | `BINARY_DOUBLE` |

**Feature Extraction**

Feature Extraction is also an unsupervised mining function, and hence there are no targets. The results of an `APPLY` procedure will contain simply the feature identifier corresponding to a case, and the associated match quality. The results table has the columns described in Table 53-45.

Table 45 APPLY Results Table for Feature Extraction

| Column Name | Datatype |
| --- | --- |
| `Case ID column name` | Type of the case ID |
| `FEATURE_ID` | `NUMBER` |
| `MATCH_QUALITY` | `BINARY_DOUBLE` |

**Examples**

This example applies the GLM Regression model `GLMR_SH_REGR_SAMPLE` to the data in the `MINING_DATA_APPLY_V` view. The `APPLY` results are output of the table `REGRESSION_APPLY_RESULT`.

```md
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

### COMPUTE\_CONFUSION\_MATRIX Procedure

This procedure computes a confusion matrix, stores it in a table in the user’s schema, and returns the model accuracy.

A confusion matrix is a test metric for classification models. It compares the predictions generated by the model with the actual target values in a set of test data. The confusion matrix lists the number of times each class was correctly predicted and the number of times it was predicted to be one of the other classes.

`COMPUTE_CONFUSION_MATRIX` accepts three input streams:

- The predictions generated on the test data. The information is passed in three columns:
	- Case ID column
		- Prediction column
		- Scoring criterion column containing either probabilities or costs
- The known target values in the test data. The information is passed in two columns:
	- Case ID column
		- Target column containing the known target values
- (Optional) A cost matrix table with predefined columns. See the Usage Notes for the column requirements. \<div class="infoboxnote" markdown="1">
	```md
	**See Also:**
	[*Oracle Data Mining Concepts*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON034) for more details about confusion matrixes and other test metrics for classification
	"[COMPUTE_LIFT Procedure](DBMS_DATA_MINING.html#GUID-FCB84437-585F-4C25-973D-126A2B79075B)"
	"[COMPUTE_ROC Procedure](DBMS_DATA_MINING.html#GUID-AD4A702E-80F1-4C66-8DC2-EED5DBE8DF20)"
	</div>
	```

**Syntax**

```md
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

**Parameters**

Table 46 COMPUTE\_CONFUSION\_MATRIX Procedure Parameters

| Parameter | Description |
| --- | --- |
| `accuracy` | Output parameter containing the overall percentage accuracy of the predictions. |
| `apply_result_table_name` | Table containing the predictions. |
| `target_table_name` | Table containing the known target values from the test data. |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data. |
| `confusion_matrix_table_name` | Table containing the confusion matrix. The table will be created by the procedure in the user's schema.  The columns in the confusion matrix table are described in the Usage Notes. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is `PREDICTION`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains either the probabilities or the costs that determine the predictions.  By default, scoring is based on probability; the class with the highest probability is predicted for each case. If scoring is based on cost, the class with the lowest cost is predicted.  The `score_criterion_type` parameter indicates whether probabilities or costs will be used for scoring.  The default column name is ' `PROBABILITY'`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure ").  See the Usage Notes for additional information. |
| `cost_matrix_table_name` | (Optional) Table that defines the costs associated with misclassifications. If a cost matrix table is provided and the `score_criterion_type` parameter is set to `'COSTS'`, the costs in this table will be used as the scoring criteria.  The columns in a cost matrix table are described in the Usage Notes. |
| `apply_result_schema_name` | Schema of the apply results table.  If null, the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, the user's schema is assumed. |
| `cost_matrix_schema_name` | Schema of the cost matrix table, if one is provided.  If null, the user's schema is assumed. |
| `score_criterion_type` | Whether to use probabilities or costs as the scoring criterion. Probabilities or costs are passed in the column identified in the `score_criterion_column_name` parameter.  The default value of `score_criterion_type` is `'PROBABILITY'`. To use costs as the scoring criterion, specify `'COST'`.  If `score_criterion_type` is set to ' `COST` ' but no cost matrix is provided and if there is a scoring cost matrix associated with the model, then the associated costs are used for scoring.  See the Usage Notes and the Examples. |

**Usage Notes**

- The predictive information you pass to `COMPUTE_CONFUSION_MATRIX` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the confusion matrix.
- Instead of passing a cost matrix to `COMPUTE_CONFUSION_MATRIX`, you can use a scoring cost matrix associated with the model. A scoring cost matrix can be embedded in the model or it can be defined dynamically when the model is applied. To use a scoring cost matrix, invoke the SQL `PREDICTION_COST` function to populate the score criterion column.
- The predictions that you pass to `COMPUTE_CONFUSION_MATRIX` are in a table or view specified in `apply_result_table_name`.
```md
case_id_column_name
```
- A cost matrix must have the columns described in Table 53-47.
	Table 47 Columns in a Cost Matrix
	| Column Name | Datatype |
	| --- | --- |
	| `actual_target_value` | Type of the target column in the build data |
	| `predicted_target_value` | Type of the predicted target in the test data. The type of the predicted target must be the same as the type of the actual target unless the predicted target has an associated reverse transformation. |
	| `cost` | `BINARY_DOUBLE` |
	**See Also:**
	[*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG152) for valid target datatypes
	[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON032) for more information about cost matrixes
- The confusion matrix created by `COMPUTE_CONFUSION_MATRIX` has the columns described in Table 53-48.
	Table 48 Columns in a Confusion Matrix
	| Column Name | Datatype |
	| --- | --- |
	| `actual_target_value` | Type of the target column in the build data |
	| `predicted_target_value` | Type of the predicted target in the test data. The type of the predicted target is the same as the type of the actual target unless the predicted target has an associated reverse transformation. |
	| `value` | `BINARY_DOUBLE` |
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON034) for more information about confusion matrixes

**Examples**

These examples use the Naive Bayes model `nb_sh_clas_sample`, which is created by one of the Oracle Data Mining sample programs.

**Compute a Confusion Matrix Based on Probabilities**

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```md
CREATE TABLE nb_apply_results AS
       SELECT cust_id,
              PREDICTION(nb_sh_clas_sample USING *) prediction,
              PREDICTION_PROBABILITY(nb_sh_clas_sample USING *) probability
       FROM mining_data_test_v;
```

Using probabilities as the scoring criterion, you can compute the confusion matrix as follows.

```md
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

```md
**** MODEL ACCURACY ****: .7847

SQL>SELECT * from nb_confusion_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         60
                  0                      0        891
                  1                      1        286
                  0                      1        263
```

**Compute a Confusion Matrix Based on a Cost Matrix Table**

The confusion matrix in the previous example shows a high rate of false positives. For 263 cases, the model predicted 1 when the actual value was 0. You could use a cost matrix to minimize this type of error.

The cost matrix table `nb_cost_matrix` specifies that a false positive is 3 times more costly than a false negative.

```md
SQL> SELECT * from nb_cost_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE       COST
------------------- ---------------------- ----------
                  0                      0          0
                  0                      1        .75
                  1                      0        .25
                  1                      1          0
```

This statement shows how to generate the predictions using `APPLY`.

```md
BEGIN
    DBMS_DATA_MINING.APPLY(
          model_name          => 'nb_sh_clas_sample',
          data_table_name     => 'mining_data_test_v',
          case_id_column_name => 'cust_id',
          result_table_name   => 'nb_apply_results');
 END;
/
```

This statement computes the confusion matrix using the cost matrix table. The score criterion column is named ‘ `PROBABILITY` ’, which is the name generated by `APPLY`.

```md
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

```md
**** MODEL ACCURACY ****: .798

SQL> SELECT * FROM nb_confusion_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         91
                  0                      0        942
                  1                      1        255
                  0                      1        212
```

**Compute a Confusion Matrix Based on Embedded Costs**

You can use the `ADD_COST_MATRIX` procedure to embed a cost matrix in a model. The embedded costs can be used instead of probabilities for scoring. This statement adds the previously-defined cost matrix to the model.

```md
BEGIN    DBMS_DATA_MINING.ADD_COST_MATRIX ('nb_sh_clas_sample', 'nb_cost_matrix');END;/
```

The following statement applies the model to the test data using the embedded costs and stores the results in a table.

```md
CREATE TABLE nb_apply_results AS
         SELECT cust_id,
              PREDICTION(nb_sh_clas_sample COST MODEL USING *) prediction,
              PREDICTION_COST(nb_sh_clas_sample COST MODEL USING *) cost
          FROM mining_data_test_v;
```

You can compute the confusion matrix using the embedded costs.

```md
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

```md
**** MODEL ACCURACY ****: .798

SQL> SELECT * FROM nb_confusion_matrix;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         91
                  0                      0        942
                  1                      1        255
                  0                      1        212
```

### COMPUTE\_CONFUSION\_MATRIX\_PART Procedure

The `COMPUTE_CONFUSION_MATRIX_PART` procedure computes a confusion matrix, stores it in a table in the user’s schema, and returns the model accuracy.

`COMPUTE_CONFUSION_MATRIX_PART` provides support to computation of evaluation metrics per-partition for partitioned models. For non-partitioned models, refer to COMPUTE\_CONFUSION\_MATRIX Procedure.

A confusion matrix is a test metric for Classification models. It compares the predictions generated by the model with the actual target values in a set of test data. The confusion matrix lists the number of times each class was correctly predicted and the number of times it was predicted to be one of the other classes.

`COMPUTE_CONFUSION_MATRIX_PART` accepts three input streams:

- The predictions generated on the test data. The information is passed in three columns:
	- Case ID column
		- Prediction column
		- Scoring criterion column containing either probabilities or costs
- The known target values in the test data. The information is passed in two columns:
	- Case ID column
		- Target column containing the known target values
- (Optional) A cost matrix table with predefined columns. See the Usage Notes for the column requirements.

**See Also:**

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON034) for more details about confusion matrixes and other test metrics for classification

“ COMPUTE\_LIFT\_PART Procedure ”

“ COMPUTE\_ROC\_PART Procedure ”

**Syntax**

```md
DBMS_DATA_MINING.compute_confusion_matrix_part(
      accuracy                    OUT DM_NESTED_NUMERICALS,
      apply_result_table_name     IN  VARCHAR2,
      target_table_name           IN  VARCHAR2,
      case_id_column_name         IN  VARCHAR2,
      target_column_name          IN  VARCHAR2,
      confusion_matrix_table_name IN  VARCHAR2,
      score_column_name           IN  VARCHAR2 DEFAULT 'PREDICTION',
      score_criterion_column_name IN  VARCHAR2 DEFAULT 'PROBABILITY',
      score_partition_column_name IN  VARCHAR2 DEFAULT 'PARTITION_NAME',
      cost_matrix_table_name      IN  VARCHAR2 DEFAULT NULL,
      apply_result_schema_name    IN  VARCHAR2 DEFAULT NULL,
      target_schema_name          IN  VARCHAR2 DEFAULT NULL,
      cost_matrix_schema_name     IN  VARCHAR2 DEFAULT NULL,
      score_criterion_type        IN  VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 49 COMPUTE\_CONFUSION\_MATRIX\_PART Procedure Parameters

| Parameter | Description |
| --- | --- |
| `accuracy` | Output parameter containing the overall percentage accuracy of the predictions  The output argument is changed from `NUMBER` to `DM_NESTED_NUMERICALS` |
| `apply_result_table_name` | Table containing the predictions |
| `target_table_name` | Table containing the known target values from the test data |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data. |
| `confusion_matrix_table_name` | Table containing the confusion matrix. The table will be created by the procedure in the user's schema.  The columns in the confusion matrix table are described in the Usage Notes. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is `PREDICTION`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains either the probabilities or the costs that determine the predictions.  By default, scoring is based on probability; the class with the highest probability is predicted for each case. If scoring is based on cost, then the class with the lowest cost is predicted.  The `score_criterion_type` parameter indicates whether probabilities or costs will be used for scoring.  The default column name is `PROBABILITY`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure ").  See the Usage Notes for additional information. |
| `score_partition_column_name` | (Optional) Parameter indicating the column which contains the name of the partition. This column slices the input test results such that each partition has independent evaluation matrices computed. |
| `cost_matrix_table_name` | (Optional) Table that defines the costs associated with misclassifications. If a cost matrix table is provided and the `score_criterion_type` parameter is set to `COSTS`, the costs in this table will be used as the scoring criteria.  The columns in a cost matrix table are described in the Usage Notes. |
| `apply_result_schema_name` | Schema of the apply results table.  If null, then the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, then the user's schema is assumed. |
| `cost_matrix_schema_name` | Schema of the cost matrix table, if one is provided.  If null, then the user's schema is assumed. |
| `score_criterion_type` | Whether to use probabilities or costs as the scoring criterion. Probabilities or costs are passed in the column identified in the `score_criterion_column_name` parameter.  The default value of `score_criterion_type` is `PROBABILITY`. To use costs as the scoring criterion, specify `COST`.  If `score_criterion_type` is set to `COST` but no cost matrix is provided and if there is a scoring cost matrix associated with the model, then the associated costs are used for scoring.  See the Usage Notes and the Examples. |

**Usage Notes**

- The predictive information you pass to `COMPUTE_CONFUSION_MATRIX_PART` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the confusion matrix.
- Instead of passing a cost matrix to `COMPUTE_CONFUSION_MATRIX_PART`, you can use a scoring cost matrix associated with the model. A scoring cost matrix can be embedded in the model or it can be defined dynamically when the model is applied. To use a scoring cost matrix, invoke the SQL `PREDICTION_COST` function to populate the score criterion column.
- The predictions that you pass to `COMPUTE_CONFUSION_MATRIX_PART` are in a table or view specified in `apply_result_table_name`.
```md
case_id_column_name
```
- A cost matrix must have the columns described in Table 53-47.
	Table 50 Columns in a Cost Matrix
	| Column Name | Datatype |
	| --- | --- |
	| `actual_target_value` | Type of the target column in the test data |
	| `predicted_target_value` | Type of the predicted target in the test data. The type of the predicted target must be the same as the type of the actual target unless the predicted target has an associated reverse transformation. |
	| `cost` | `BINARY_DOUBLE` |
	**See Also:**
	[*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG152) for valid target datatypes
	[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON032) for more information about cost matrixes
- The confusion matrix created by `COMPUTE_CONFUSION_MATRIX_PART` has the columns described in Table 53-48.
	Table 51 Columns in a Confusion Matrix Part
	| Column Name | Datatype |
	| --- | --- |
	| `actual_target_value` | Type of the target column in the test data |
	| `predicted_target_value` | Type of the predicted target in the test data. The type of the predicted target is the same as the type of the actual target unless the predicted target has an associated reverse transformation. |
	| `value` | `BINARY_DOUBLE` |
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON034) for more information about confusion matrixes

**Examples**

These examples use the Naive Bayes model `nb_sh_clas_sample`, which is created by one of the Oracle Data Mining sample programs.

**Compute a Confusion Matrix Based on Probabilities**

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```md
CREATE TABLE nb_apply_results AS
       SELECT cust_id,
              PREDICTION(nb_sh_clas_sample USING *) prediction,
              PREDICTION_PROBABILITY(nb_sh_clas_sample USING *) probability
       FROM mining_data_test_v;
```

Using probabilities as the scoring criterion, you can compute the confusion matrix as follows.

```md
DECLARE
   v_accuracy    NUMBER;
      BEGIN
        DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX_PART (
                   accuracy                     => v_accuracy,
                   apply_result_table_name      => 'nb_apply_results',
                   target_table_name            => 'mining_data_test_v',
                   case_id_column_name          => 'cust_id',
                   target_column_name           => 'affinity_card',
                   confusion_matrix_table_name  => 'nb_confusion_matrix',
                   score_column_name            => 'PREDICTION',
                   score_criterion_column_name  => 'PROBABILITY'
                   score_partition_column_name  => 'PARTITION_NAME'
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

```md
**** MODEL ACCURACY ****: .7847

SELECT * FROM NB_CONFUSION_MATRIX;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         60
                  0                      0        891
                  1                      1        286
                  0                      1        263
```

**Compute a Confusion Matrix Based on a Cost Matrix Table**

The confusion matrix in the previous example shows a high rate of false positives. For 263 cases, the model predicted 1 when the actual value was 0. You could use a cost matrix to minimize this type of error.

The cost matrix table `nb_cost_matrix` specifies that a false positive is 3 times more costly than a false negative.

```md
SELECT * from NB_COST_MATRIX;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE       COST
------------------- ---------------------- ----------
                  0                      0          0
                  0                      1        .75
                  1                      0        .25
                  1                      1          0
```

This statement shows how to generate the predictions using `APPLY`.

```md
BEGIN
    DBMS_DATA_MINING.APPLY(
          model_name          => 'nb_sh_clas_sample',
          data_table_name     => 'mining_data_test_v',
          case_id_column_name => 'cust_id',
          result_table_name   => 'nb_apply_results');
 END;
/
```

This statement computes the confusion matrix using the cost matrix table. The score criterion column is named ‘ `PROBABILITY` ’, which is the name generated by `APPLY`.

```md
DECLARE
  v_accuracy    NUMBER;
     BEGIN
       DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX_PART (
                accuracy                     => v_accuracy,
                apply_result_table_name      => 'nb_apply_results',
                target_table_name            => 'mining_data_test_v',
                case_id_column_name          => 'cust_id',
                target_column_name           => 'affinity_card',
                confusion_matrix_table_name  => 'nb_confusion_matrix',
                score_column_name            => 'PREDICTION',
                score_criterion_column_name  => 'PROBABILITY',
                score_partition_column_name  => 'PARTITION_NAME'
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

```md
**** MODEL ACCURACY ****: .798

 SELECT * FROM NB_CONFUSION_MATRIX;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         91
                  0                      0        942
                  1                      1        255
                  0                      1        212
```

**Compute a Confusion Matrix Based on Embedded Costs**

You can use the `ADD_COST_MATRIX` procedure to embed a cost matrix in a model. The embedded costs can be used instead of probabilities for scoring. This statement adds the previously-defined cost matrix to the model.

```md
BEGIN
DBMS_DATA_MINING.ADD_COST_MATRIX ('nb_sh_clas_sample', 'nb_cost_matrix');
END;/
```

The following statement applies the model to the test data using the embedded costs and stores the results in a table.

```md
CREATE TABLE nb_apply_results AS
         SELECT cust_id,
              PREDICTION(nb_sh_clas_sample COST MODEL USING *) prediction,
              PREDICTION_COST(nb_sh_clas_sample COST MODEL USING *) cost
          FROM mining_data_test_v;
```

You can compute the confusion matrix using the embedded costs.

```md
DECLARE
   v_accuracy         NUMBER;
   BEGIN
       DBMS_DATA_MINING.COMPUTE_CONFUSION_MATRIX_PART (
            accuracy                     => v_accuracy,
            apply_result_table_name      => 'nb_apply_results',
            target_table_name            => 'mining_data_test_v',
            case_id_column_name          => 'cust_id',
            target_column_name           => 'affinity_card',
            confusion_matrix_table_name  => 'nb_confusion_matrix',
            score_column_name            => 'PREDICTION',
            score_criterion_column_name  => 'COST',
            score_partition_column_name  => 'PARTITION_NAME'
            cost_matrix_table_name       => null,
            apply_result_schema_name     => null,
            target_schema_name           => null,
            cost_matrix_schema_name      => null,
            score_criterion_type         => 'COST');
   END;
   /
```

The results are:

```md
**** MODEL ACCURACY ****: .798

 SELECT * FROM NB_CONFUSION_MATRIX;
ACTUAL_TARGET_VALUE PREDICTED_TARGET_VALUE      VALUE
------------------- ---------------------- ----------
                  1                      0         91
                  0                      0        942
                  1                      1        255
                  0                      1        212
```

### COMPUTE\_LIFT Procedure

This procedure computes lift and stores the results in a table in the user’s schema.

Lift is a test metric for binary classification models. To compute lift, one of the target values must be designated as the positive class. `COMPUTE_LIFT` compares the predictions generated by the model with the actual target values in a set of test data. Lift measures the degree to which the model’s predictions of the positive class are an improvement over random chance.

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

**See Also:**

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON053) for more details about lift and test metrics for classification

“ COMPUTE\_CONFUSION\_MATRIX Procedure ”

“ COMPUTE\_ROC Procedure ”

**Syntax**

```md
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

**Parameters**

Table 52 COMPUTE\_LIFT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `apply_result_table_name` | Table containing the predictions. |
| `target_table_name` | Table containing the known target values from the test data. |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data. |
| `lift_table_name` | Table containing the lift statistics. The table will be created by the procedure in the user's schema.  The columns in the lift table are described in the Usage Notes. |
| `positive_target_value` | The positive class. This should be the class of interest, for which you want to calculate lift.  If the target column is a `NUMBER`, you can use the `TO_CHAR()` operator to provide the value as a string. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is ' `PREDICTION` ', which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains either the probabilities or the costs that determine the predictions.  By default, scoring is based on probability; the class with the highest probability is predicted for each case. If scoring is based on cost, the class with the lowest cost is predicted.  The `score_criterion_type` parameter indicates whether probabilities or costs will be used for scoring.  The default column name is ' `PROBABILITY` ', which is the default name created by the `APPLY` procedure (See " APPLY Procedure ").  See the Usage Notes for additional information. |
| `num_quantiles` | Number of quantiles to be used in calculating lift. The default is 10. |
| `cost_matrix_table_name` | (Optional) Table that defines the costs associated with misclassifications. If a cost matrix table is provided and the `score_criterion_type` parameter is set to ' `COST` ', the costs will be used as the scoring criteria.  The columns in a cost matrix table are described in the Usage Notes. |
| `apply_result_schema_name` | Schema of the apply results table.  If null, the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, the user's schema is assumed. |
| `cost_matrix_schema_name` | Schema of the cost matrix table, if one is provided.  If null, the user's schema is assumed. |
| `score_criterion_type` | Whether to use probabilities or costs as the scoring criterion. Probabilities or costs are passed in the column identified in the `score_criterion_column_name` parameter.  The default value of `score_criterion_type` is ' `PROBABILITY` '. To use costs as the scoring criterion, specify ' `COST` '.  If `score_criterion_type` is set to ' `COST` ' but no cost matrix is provided and if there is a scoring cost matrix associated with the model, then the associated costs are used for scoring.  See the Usage Notes and the Examples. |

**Usage Notes**

- The predictive information you pass to `COMPUTE_LIFT` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the lift.
- Instead of passing a cost matrix to `COMPUTE_LIFT`, you can use a scoring cost matrix associated with the model. A scoring cost matrix can be embedded in the model or it can be defined dynamically when the model is applied. To use a scoring cost matrix, invoke the SQL `PREDICTION_COST` function to populate the score criterion column.
- The predictions that you pass to `COMPUTE_LIFT` are in a table or view specified in `apply_results_table_name`.
```md
case_id_column_name
```
- A cost matrix must have the columns described in Table 53-53.
	Table 53 Columns in a Cost Matrix
	| Column Name | Datatype |
	| --- | --- |
	| `actual_target_value` | Type of the target column in the build data |
	| `predicted_target_value` | Type of the predicted target in the test data. The type of the predicted target must be the same as the type of the actual target unless the predicted target has an associated reverse transformation. |
	| `cost` | `NUMBER` |
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON032) for more information about cost matrixes
- The table created by `COMPUTE_LIFT` has the columns described in Table 53-54
	Table 54 Columns in a Lift Table
	| Column Name | Datatype |
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
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON035) for details about the information in the lift table
- When a cost matrix is passed to `COMPUTE_LIFT`, the cost threshold is returned in the `probability_threshold` column of the lift table.

**Examples**

This example uses the Naive Bayes model `nb_sh_clas_sample`, which is created by one of the Oracle Data Mining sample programs.

The example illustrates lift based on probabilities. For examples that show computation based on costs, see “ COMPUTE\_CONFUSION\_MATRIX Procedure ”.

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```md
CREATE TABLE nb_apply_results AS
    SELECT cust_id, t.prediction, t.probability
    FROM mining_data_test_v, TABLE(PREDICTION_SET(nb_sh_clas_sample USING *)) t;
```

Using probabilities as the scoring criterion, you can compute lift as follows.

```md
BEGIN
       DBMS_DATA_MINING.COMPUTE_LIFT (
            apply_result_table_name            => 'nb_apply_results',
            target_table_name                  => 'mining_data_test_v',
            case_id_column_name                => 'cust_id',
            target_column_name                 => 'affinity_card',
            lift_table_name                        => 'nb_lift',
            positive_target_value              =>  to_char(1),
            score_column_name                  => 'PREDICTION',
            score_criterion_column_name    => 'PROBABILITY',
            num_quantiles                          =>  10,
            cost_matrix_table_name             =>  null,
            apply_result_schema_name           =>  null,
            target_schema_name                 =>  null,
            cost_matrix_schema_name            =>  null,
            score_criterion_type               =>  'PROBABILITY');
      END;
      /
```

This query displays some of the statistics from the resulting lift table.

```md
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

### COMPUTE\_LIFT\_PART Procedure

The `COMPUTE_LIFT_PART` procedure computes Lift and stores the results in a table in the user’s schema. This procedure provides support to the computation of evaluation metrics per-partition for partitioned models.

Lift is a test metric for binary Classification models. To compute Lift, one of the target values must be designated as the positive class. `COMPUTE_LIFT_PART` compares the predictions generated by the model with the actual target values in a set of test data. Lift measures the degree to which the model’s predictions of the positive class are an improvement over random chance.

Lift is computed on scoring results that have been ranked by probability (or cost) and divided into quantiles. Each quantile includes the scores for the same number of cases.

`COMPUTE_LIFT_PART` calculates quantile-based and cumulative statistics. The number of quantiles and the positive class are user-specified. Additionally, `COMPUTE_LIFT_PART` accepts three input streams:

- The predictions generated on the test data. The information is passed in three columns:
	- Case ID column
		- Prediction column
		- Scoring criterion column containing either probabilities or costs associated with the predictions
- The known target values in the test data. The information is passed in two columns:
	- Case ID column
		- Target column containing the known target values
- (Optional) A cost matrix table with predefined columns. See the Usage Notes for the column requirements.

**See Also:**

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON053) for more details about Lift and test metrics for classification

“ COMPUTE\_LIFT Procedure ”

“ COMPUTE\_CONFUSION\_MATRIX Procedure ”

“ COMPUTE\_CONFUSION\_MATRIX\_PART Procedure ”

“ COMPUTE\_ROC Procedure ”

“ COMPUTE\_ROC\_PART Procedure ”

**Syntax**

```md
DBMS_DATA_MINING.COMPUTE_LIFT_PART (
      apply_result_table_name     IN VARCHAR2,
      target_table_name           IN VARCHAR2,
      case_id_column_name         IN VARCHAR2,
      target_column_name          IN VARCHAR2,
      lift_table_name             IN VARCHAR2,
      positive_target_value       IN VARCHAR2,
      score_column_name           IN VARCHAR2 DEFAULT 'PREDICTION',
      score_criterion_column_name IN VARCHAR2 DEFAULT 'PROBABILITY',
      score_partition_column_name IN VARCHAR2 DEFAULT 'PARTITION_NAME',
      num_quantiles               IN NUMBER   DEFAULT 10,
      cost_matrix_table_name      IN VARCHAR2 DEFAULT NULL,
      apply_result_schema_name    IN VARCHAR2 DEFAULT NULL,
      target_schema_name          IN VARCHAR2 DEFAULT NULL,
      cost_matrix_schema_name     IN VARCHAR2 DEFAULT NULL,
      score_criterion_type        IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 55 COMPUTE\_LIFT\_PART Procedure Parameters

| Parameter | Description |
| --- | --- |
| `apply_result_table_name` | Table containing the predictions |
| `target_table_name` | Table containing the known target values from the test data |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data. |
| `lift_table_name` | Table containing the Lift statistics. The table will be created by the procedure in the user's schema.  The columns in the Lift table are described in the Usage Notes. |
| `positive_target_value` | The positive class. This should be the class of interest, for which you want to calculate Lift.  If the target column is a `NUMBER`, then you can use the `TO_CHAR()` operator to provide the value as a string. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is `PREDICTION`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains either the probabilities or the costs that determine the predictions.  By default, scoring is based on probability; the class with the highest probability is predicted for each case. If scoring is based on cost, then the class with the lowest cost is predicted.  The `score_criterion_type` parameter indicates whether probabilities or costs will be used for scoring.  The default column name is `PROBABILITY`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure ").  See the Usage Notes for additional information. |
| `score_partition_column_name` | Optional parameter indicating the column containing the name of the partition. This column slices the input test results such that each partition has independent evaluation matrices computed. |
| `num_quantiles` | Number of quantiles to be used in calculating Lift. The default is 10. |
| `cost_matrix_table_name` | (Optional) Table that defines the costs associated with misclassifications. If a cost matrix table is provided and the `score_criterion_type` parameter is set to `COST`, then the costs will be used as the scoring criteria.  The columns in a cost matrix table are described in the Usage Notes. |
| `apply_result_schema_name` | Schema of the apply results table  If null, then the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets  If null, then the user's schema is assumed. |
| `cost_matrix_schema_name` | Schema of the cost matrix table, if one is provided  If null, then the user's schema is assumed. |
| `score_criterion_type` | Whether to use probabilities or costs as the scoring criterion. Probabilities or costs are passed in the column identified in the `score_criterion_column_name` parameter.  The default value of `score_criterion_type` is `PROBABILITY`. To use costs as the scoring criterion, specify `COST`.  If `score_criterion_type` is set to `COST` but no cost matrix is provided and if there is a scoring cost matrix associated with the model, then the associated costs are used for scoring.  See the Usage Notes and the Examples. |

**Usage Notes**

- The predictive information you pass to `COMPUTE_LIFT_PART` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the Lift.
- Instead of passing a cost matrix to `COMPUTE_LIFT_PART`, you can use a scoring cost matrix associated with the model. A scoring cost matrix can be embedded in the model or it can be defined dynamically when the model is applied. To use a scoring cost matrix, invoke the SQL `PREDICTION_COST` function to populate the score criterion column.
- The predictions that you pass to `COMPUTE_LIFT_PART` are in a table or view specified in `apply_results_table_name`.
```md
apply_result_table_name
```
- A cost matrix must have the columns described in Table 53-53.
	Table 56 Columns in a Cost Matrix
	| Column Name | Datatype |
	| --- | --- |
	| `actual_target_value` | Type of the target column in the test data |
	| `predicted_target_value` | Type of the predicted target in the test data. The type of the predicted target must be the same as the type of the actual target unless the predicted target has an associated reverse transformation. |
	| `cost` | `NUMBER` |
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON032) for more information about cost matrixes
- The table created by `COMPUTE_LIFT_PART` has the columns described in Table 53-54
	Table 57 Columns in a COMPUTE\_LIFT\_PART Table
	| Column Name | Datatype |
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
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON035) for details about the information in the Lift table
- When a cost matrix is passed to `COMPUTE_LIFT_PART`, the cost threshold is returned in the `probability_threshold` column of the Lift table.

**Examples**

This example uses the Naive Bayes model `nb_sh_clas_sample`, which is created by one of the Oracle Data Mining sample programs.

The example illustrates Lift based on probabilities. For examples that show computation based on costs, see “ COMPUTE\_CONFUSION\_MATRIX Procedure ”.

For a partitioned model example, see “ COMPUTE\_CONFUSION\_MATRIX\_PART Procedure ”.

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```md
CREATE TABLE nb_apply_results AS
    SELECT cust_id, t.prediction, t.probability
    FROM mining_data_test_v, TABLE(PREDICTION_SET(nb_sh_clas_sample USING *)) t;
```

Using probabilities as the scoring criterion, you can compute Lift as follows.

```md
BEGIN
      DBMS_DATA_MINING.COMPUTE_LIFT_PART (
             apply_result_table_name     => 'nb_apply_results',
             target_table_name           => 'mining_data_test_v',
             case_id_column_name         => 'cust_id',
             target_column_name          => 'affinity_card',
             lift_table_name             => 'nb_lift',
             positive_target_value       =>  to_char(1),
             score_column_name           => 'PREDICTION',
             score_criterion_column_name => 'PROBABILITY',
             score_partition_column_name => 'PARTITITON_NAME',
             num_quantiles               =>  10,
             cost_matrix_table_name      =>  null,
             apply_result_schema_name    =>  null,
             target_schema_name          =>  null,
             cost_matrix_schema_name     =>  null,
             score_criterion_type        =>  'PROBABILITY');
END;
/
```

This query displays some of the statistics from the resulting Lift table.

```md
SELECT quantile_number, probability_threshold, gain_cumulative,
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

### COMPUTE\_ROC Procedure

This procedure computes the receiver operating characteristic (ROC), stores the results in a table in the user’s schema, and returns a measure of the model accuracy.

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

**See Also:**

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON054) for more details about ROC and test metrics for classification

“ COMPUTE\_CONFUSION\_MATRIX Procedure ”

“ COMPUTE\_LIFT Procedure ”

**Syntax**

```md
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

**Parameters**

Table 58 COMPUTE\_ROC Procedure

| Parameter | Description |
| --- | --- |
| `roc_area_under_the_curve` | Output parameter containing the area under the ROC curve (AUC). The AUC measures the likelihood that an actual positive will be predicted as positive.  The greater the AUC, the greater the flexibility of the model in accommodating trade-offs between positive and negative class predictions. AUC can be especially important when one target class is rarer or more important to identify than another. |
| `apply_result_table_name` | Table containing the predictions. |
| `target_table_name` | Table containing the known target values from the test data. |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | \<p>Target column in the targets table. Contains the known target values from the test data.\</p> \<div class="infoboxnote" id="GUID-AD4A702E-80F1-4C66-8DC2-EED5DBE8DF20\_\_GUID-A74DF730-F4FA-4F90-AB82-A388A21A3382"> \<p class="notep1">Note:\</p>The target column does not support `BINARY_DOUBLE` data type. \</div> |
| `roc_table_name` | Table containing the ROC output. The table will be created by the procedure in the user's schema.  The columns in the ROC table are described in the Usage Notes. |
| `positive_target_value` | The positive class. This should be the class of interest, for which you want to calculate ROC.  If the target column is a `NUMBER`, you can use the `TO_CHAR()` operator to provide the value as a string. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is ' `PREDICTION` ', which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains the probabilities that determine the predictions.  The default column name is ' `PROBABILITY` ', which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `apply_result_schema_name` | Schema of the apply results table.  If null, the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, the user's schema is assumed. |

**Usage Notes**

- The predictive information you pass to `COMPUTE_ROC` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the receiver operating characteristic.
- The predictions that you pass to `COMPUTE_ROC` are in a table or view specified in `apply_results_table_name`.
```md
apply_result_table_name
```
- The table created by `COMPUTE_ROC` has the columns shown in Table 53-59.
	Table 59 COMPUTE\_ROC Output
	| Column | Datatype |
	| --- | --- |
	| `probability` | `BINARY_DOUBLE` |
	| `true_positives` | `NUMBER` |
	| `false_negatives` | `NUMBER` |
	| `false_positives` | `NUMBER` |
	| `true_negatives` | `NUMBER` |
	| `true_positive_fraction` | `NUMBER` |
	| `false_positive_fraction` | `NUMBER` |
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON054) for details about the output of `COMPUTE_ROC`
- ROC is typically used to determine the most desirable probability threshold. This can be done by examining the true positive fraction and the false positive fraction. The true positive fraction is the percentage of all positive cases in the test data that were correctly predicted as positive. The false positive fraction is the percentage of all negative cases in the test data that were incorrectly predicted as positive.
	Given a probability threshold, the following statement returns the positive predictions in an apply result table ordered by probability.
```md
probability
```
- There are two approaches to identifying the most desirable probability threshold. Which approach you use depends on whether or not you know the relative cost of positive versus negative class prediction errors.
	If the costs are known, you can apply the relative costs to the ROC table to compute the minimum cost probability threshold. Suppose the relative cost ratio is: Positive Class Error Cost / Negative Class Error Cost = 20. Then execute a query like this.
```md
cost
```

If relative costs are not well known, you can simply scan the values in the ROC table (in sorted order) and make a determination about which of the displayed trade-offs (misclassified positives versus misclassified negatives) is most desirable.

```md
ROC_table
```

**Examples**

This example uses the Naive Bayes model `nb_sh_clas_sample`.

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```md
CREATE TABLE nb_apply_results AS
    SELECT cust_id, t.prediction, t.probability
    FROM mining_data_test_v, TABLE(PREDICTION_SET(nb_sh_clas_sample USING *)) t;
```

Using the predictions and the target values from the test data, you can compute ROC as follows.

```md
DECLARE
     v_area_under_curve NUMBER;
BEGIN
     DBMS_DATA_MINING.COMPUTE_ROC (
         roc_area_under_curve        => v_area_under_curve,
         apply_result_table_name     => 'nb_apply_results',
         target_table_name           => 'mining_data_test_v',
         case_id_column_name         => 'cust_id',
         target_column_name          => 'mining_data_test_v',
         roc_table_name              => 'nb_roc',
         positive_target_value       => '1',
         score_column_name           => 'PREDICTION',
         score_criterion_column_name => 'PROBABILITY');
     DBMS_OUTPUT.PUT_LINE('**** AREA UNDER ROC CURVE ****: ' ||
     ROUND(v_area_under_curve,4));
END;
/
```

The resulting AUC and a selection of columns from the ROC table are shown as follows.

```md
**** AREA UNDER ROC CURVE ****: .8212

 SELECT PROBABILITY, TRUE_POSITIVE_FRACTION, FALSE_POSITIVE_FRACTION
            FROM NB_ROC;

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

### COMPUTE\_ROC\_PART Procedure

The `COMPUTE_ROC_PART` procedure computes Receiver Operating Characteristic (ROC), stores the results in a table in the user’s schema, and returns a measure of the model accuracy. This procedure provides support to computation of evaluation metrics per-partition for partitioned models.

ROC is a test metric for binary classification models. To compute ROC, one of the target values must be designated as the positive class. `COMPUTE_ROC_PART` compares the predictions generated by the model with the actual target values in a set of test data.

ROC measures the impact of changes in the probability threshold. The probability threshold is the decision point used by the model for predictions. In binary classification, the default probability threshold is `0.5`. The value predicted for each case is the one with a probability greater than 50%.

ROC can be plotted as a curve on an x-y axis. The false positive rate is placed on the x-axis. The true positive rate is placed on the y-axis. A false positive is a positive prediction for a case that is negative in the test data. A true positive is a positive prediction for a case that is positive in the test data.

`COMPUTE_ROC_PART` accepts two input streams:

- The predictions generated on the test data. The information is passed in three columns:
	- Case ID column
		- Prediction column
		- Scoring criterion column containing probabilities
- The known target values in the test data. The information is passed in two columns:
	- Case ID column
		- Target column containing the known target values

**See Also:**

[*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON054) for more details about ROC and test metrics for Classification

“ COMPUTE\_ROC Procedure ”

“ COMPUTE\_CONFUSION\_MATRIX Procedure ”

“ COMPUTE\_LIFT\_PART Procedure ”

“ COMPUTE\_LIFT Procedure ”

**Syntax**

```md
DBMS_DATA_MINING.compute_roc_part(
      roc_area_under_curve        OUT DM_NESTED_NUMERICALS,
      apply_result_table_name     IN  VARCHAR2,
      target_table_name           IN  VARCHAR2,
      case_id_column_name         IN  VARCHAR2,
      target_column_name          IN  VARCHAR2,
      roc_table_name              IN  VARCHAR2,
      positive_target_value       IN  VARCHAR2,
      score_column_name           IN  VARCHAR2 DEFAULT 'PREDICTION',
      score_criterion_column_name IN  VARCHAR2 DEFAULT 'PROBABILITY',
      score_partition_column_name IN  VARCHAR2 DEFAULT 'PARTITION_NAME',
      apply_result_schema_name    IN  VARCHAR2 DEFAULT NULL,
      target_schema_name          IN  VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 60 COMPUTE\_ROC\_PART Procedure

| Parameter | Description |
| --- | --- |
| `roc_area_under_the_curve` | Output parameter containing the area under the ROC curve (AUC). The AUC measures the likelihood that an actual positive will be predicted as positive.  The greater the AUC, the greater the flexibility of the model in accommodating trade-offs between positive and negative class predictions. AUC can be especially important when one target class is rarer or more important to identify than another.  The output argument is changed from `NUMBER` to `DM_NESTED_NUMERICALS`. |
| `apply_result_table_name` | Table containing the predictions. |
| `target_table_name` | Table containing the known target values from the test data. |
| `case_id_column_name` | Case ID column in the apply results table. Must match the case identifier in the targets table. |
| `target_column_name` | Target column in the targets table. Contains the known target values from the test data.  Note:  The target column does not support `BINARY_DOUBLE` data type. |
| `roc_table_name` | Table containing the ROC output. The table will be created by the procedure in the user's schema.  The columns in the ROC table are described in the Usage Notes. |
| `positive_target_value` | The positive class. This should be the class of interest, for which you want to calculate ROC.  If the target column is a `NUMBER`, then you can use the `TO_CHAR()` operator to provide the value as a string. |
| `score_column_name` | Column containing the predictions in the apply results table.  The default column name is `PREDICTION`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `score_criterion_column_name` | Column containing the scoring criterion in the apply results table. Contains the probabilities that determine the predictions.  The default column name is `PROBABILITY`, which is the default name created by the `APPLY` procedure (See " APPLY Procedure "). |
| `score_partition_column_name` | Optional parameter indicating the column which contains the name of the partition. This column slices the input test results such that each partition has independent evaluation matrices computed. |
| `apply_result_schema_name` | Schema of the apply results table.  If null, then the user's schema is assumed. |
| `target_schema_name` | Schema of the table containing the known targets.  If null, then the user's schema is assumed. |

**Usage Notes**

- The predictive information you pass to `COMPUTE_ROC_PART` may be generated using SQL `PREDICTION` functions, the `DBMS_DATA_MINING.APPLY` procedure, or some other mechanism. As long as you pass the appropriate data, the procedure can compute the receiver operating characteristic.
- The predictions that you pass to `COMPUTE_ROC_PART` are in a table or view specified in `apply_results_table_name`.
```md
apply_result_table_name
```
- The `COMPUTE_ROC_PART` table has the following columns:
	Table 61 COMPUTE\_ROC\_PART Output
	| Column | Data Type |
	| --- | --- |
	| `probability` | `BINARY_DOUBLE` |
	| `true_positives` | `NUMBER` |
	| `false_negatives` | `NUMBER` |
	| `false_positives` | `NUMBER` |
	| `true_negatives` | `NUMBER` |
	| `true_positive_fraction` | `NUMBER` |
	| `false_positive_fraction` | `NUMBER` |
	**See Also:** [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON054) for details about the output of `COMPUTE_ROC_PART`
- ROC is typically used to determine the most desirable probability threshold. This can be done by examining the true positive fraction and the false positive fraction. The true positive fraction is the percentage of all positive cases in the test data that were correctly predicted as positive. The false positive fraction is the percentage of all negative cases in the test data that were incorrectly predicted as positive.
	Given a probability threshold, the following statement returns the positive predictions in an apply result table ordered by probability.
```md
probability
```
- There are two approaches to identify the most desirable probability threshold. The approach you use depends on whether you know the relative cost of positive versus negative class prediction errors.
	If the costs are known, then you can apply the relative costs to the ROC table to compute the minimum cost probability threshold. Suppose the relative cost ratio is: Positive Class Error Cost / Negative Class Error Cost = 20. Then execute a query as follows:
```md
cost
```

If relative costs are not well known, then you can simply scan the values in the ROC table (in sorted order) and make a determination about which of the displayed trade-offs (misclassified positives versus misclassified negatives) is most desirable.

```md
ROC_table
```

**Examples**

This example uses the Naive Bayes model `nb_sh_clas_sample`.

The following statement applies the model to the test data and stores the predictions and probabilities in a table.

```md
CREATE TABLE nb_apply_results AS
    SELECT cust_id, t.prediction, t.probability
    FROM mining_data_test_v, TABLE(PREDICTION_SET(nb_sh_clas_sample USING *)) t;
```

Using the predictions and the target values from the test data, you can compute ROC as follows.

```md
DECLARE
     v_area_under_curve NUMBER;
BEGIN
     DBMS_DATA_MINING.COMPUTE_ROC_PART (
         roc_area_under_curve        => v_area_under_curve,
         apply_result_table_name     => 'nb_apply_results',
         target_table_name           => 'mining_data_test_v',
         case_id_column_name         => 'cust_id',
         target_column_name          => 'affinity_card',
         roc_table_name              => 'nb_roc',
         positive_target_value       => '1',
         score_column_name           => 'PREDICTION',
         score_criterion_column_name => 'PROBABILITY');
         score_partition_column_name => 'PARTITION_NAME'
     DBMS_OUTPUT.PUT_LINE('**** AREA UNDER ROC CURVE ****: ' ||
     ROUND(v_area_under_curve,4));
END;
/
```

The resulting AUC and a selection of columns from the ROC table are shown as follows.

```md
**** AREA UNDER ROC CURVE ****: .8212

 SELECT PROBABILITY, TRUE_POSITIVE_FRACTION, FALSE_POSITIVE_FRACTION
            FROM NB_ROC;

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

### CREATE\_MODEL Procedure

This procedure creates a mining model with a given mining function.

**Syntax**

```md
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

**Parameters**

Table 62 CREATE\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used.  See the Usage Notes for model naming restrictions. |
| `mining_function` | The mining function. Values are listed in Table 53-3. |
| `data_table_name` | Table or view containing the build data |
| `case_id_column_name` | Case identifier column in the build data. |
| `target_column_name` | For supervised models, the target column in the build data. `NULL` for unsupervised models. |
| `settings_table_name` | Table containing build settings for the model. `NULL` if there is no settings table (only default settings are used). |
| `data_schema_name` | Schema hosting the build data. If `NULL`, then the user’s schema is assumed. |
| `settings_schema_name` | Schema hosting the settings table. If `NULL` then the user’s schema is assumed. |
| `xform_list` | A list of transformations to be used in addition to or instead of automatic transformations, depending on the value of the `PREP_AUTO` setting. (See " Automatic Data Preparation ".)  The datatype of `xform_list` is `TRANSFORM_LIST`, which consists of records of type `TRANSFORM_REC`. Each `TRANSFORM_REC` specifies the transformation information for a single attribute.  ```md TYPE TRANFORM_REC IS RECORD ( attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), expression EXPRESSION_REC, reverse_expression EXPRESSION_REC, attribute_spec VARCHAR2(4000)); ```  The `expression` field stores a SQL expression for transforming the attribute. The `reverse_expression` field stores a SQL expression for reversing the transformation in model details and, if the attribute is a target, in the results of scoring. The SQL expressions are manipulated by routines in the `DBMS_DATA_MINING_TRANSFORM` package:  - [SET\_EXPRESSION Procedure](DBMS_DATA_MINING_TRANSFORM.md) - [GET\_EXPRESSION Function](DBMS_DATA_MINING_TRANSFORM.md) - [SET\_TRANSFORM Procedure](DBMS_DATA_MINING_TRANSFORM.md)  The `attribute_spec` field identifies individualized treatment for the attribute. See the Usage Notes for details.  See [Table 54-1](DBMS_DATA_MINING_TRANSFORM.md) for details about the `TRANSFORM_REC` type. |

**Usage Notes**

1. You can use the `attribute_spec` field of the `xform_list` argument to identify an attribute as unstructured text or to disable Automatic Data Preparation for the attribute. The `attribute_spec` can have the following values:
	- `TEXT`: Indicates that the attribute contains unstructured text. The `TEXT` value may optionally be followed by `POLICY_NAME`, `TOKEN_TYPE`, `MAX_FEATURES`, and `MIN_DOCUMENTS` parameters.
		`TOKEN_TYPE` has the following possible values: `NORMAL`, `STEM`, `THEME`, `SYNONYM`, `BIGRAM`, `STEM_BIGRAM`. `SYNONYM` may be optionally followed by a thesaurus name in square brackets.
		`MAX_FEATURES` specifies the maximum number of tokens extracted from the text.
		`MIN_DOCUMENTS` specifies the minimal number of documents in which every selected token shall occur. (For information about creating a text policy, see `CTX_DDL.CREATE_POLICY` in [*Oracle Text Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=CCREF2105)).
		Oracle Data Mining can process columns of `VARCHAR2` / `CHAR`, `CLOB`, `BLOB`, and `BFILE` as text. If the column is `VARCHAR2` or `CHAR` and you do not specify `TEXT`, Oracle Data Mining will process the column as categorical data. If the column is `CLOB`, then Oracle Data Mining will process it as text by default (You do not need to specify it as `TEXT`. However, you do need to provide an Oracle Text Policy in the settings). If the column is `BLOB` or `BFILE`, you must specify it as `TEXT`, otherwise `CREATE_MODEL` will return an error.
		If you specify `TEXT` for a nested column or for an attribute in a nested column, `CREATE_MODEL` will return an error.
		- `NOPREP`: Disables ADP for the attribute. When ADP is `OFF`, the `NOPREP` value is ignored.
		You can specify `NOPREP` for a nested column, but not for an attribute in a nested column. If you specify `NOPREP` for an attribute in a nested column when ADP is on, `CREATE_MODEL` will return an error.
2. You can obtain information about a model by querying the Data Dictionary views.
	```md
	ALL/USER/DBA_MINING_MODELS
	ALL/USER/DBA_MINING_MODEL_ATTRIBUTES
	ALL/USER/DBA_MINING_MODEL_SETTINGS
	ALL/USER/DBA_MINING_MODEL_VIEWS
	ALL/USER/DBA_MINING_MODEL_PARTITIONS
	ALL/USER/DBA_MINING_MODEL_XFORMS
	```
	You can obtain information about model attributes by querying the model details through model views. Refer to *Oracle Data Mining User’s Guide*.
3. The naming rules for models are more restrictive than the naming rules for most database schema objects. A model name must satisfy the following additional requirements:
	- It must be 123 or fewer characters long.
		- It must be a nonquoted identifier. Oracle requires that nonquoted identifiers contain only alphanumeric characters, the underscore (\_), dollar sign ($), and pound sign (#); the initial character must be alphabetic. Oracle strongly discourages the use of the dollar sign and pound sign in nonquoted literals.
	Naming requirements for schema objects are fully documented in [*Oracle Database SQL Language Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SQLRF00223).
4. To build a partitioned model, you must provide additional settings.
	The setting for partitioning columns are as follows:
	```md
	INSERT INTO settings_table VALUES ('ODMS_PARTITION_COLUMNS', 'GENDER, AGE');
	```
	To set user-defined partition number for a model, the setting is as follows:
	```md
	INSERT INTO settings_table VALUES ('ODMS_MAX_PARTITIONS', '10');
	```
	The default value for maximum number of partitions is `1000`.
5. By passing an `xform_list` to `CREATE_MODEL`, you can specify a list of transformations to be performed on the input data. If the `PREP_AUTO` setting is `ON`, the transformations are used in addition to the automatic transformations. If the `PREP_AUTO` setting is `OFF`, the specified transformations are the only ones implemented by the model. In both cases, transformation definitions are embedded in the model and executed automatically whenever the model is applied. See “ Automatic Data Preparation ”. Other transforms that can be specified with `xform_list` include `FORCE_IN`. Refer to *Oracle Data Mining User’s Guide*.

**Examples**

The first example builds a Classification model using the Support Vector Machine algorithm.

```md
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

You can display the model settings with the following query:

```md
SELECT * FROM user_mining_model_settings
       WHERE model_name IN 'SVM_MODEL';

MODEL_NAME     SETTING_NAME            SETTING_VALUE                  SETTING
-------------  ----------------------  -----------------------------  -------
SVM_MODEL      ALGO_NAME               ALGO_SUPPORT_VECTOR_MACHINES  INPUT

SVM_MODEL      SVMS_STD_DEV            3.004524                      DEFAULT
SVM_MODEL      PREP_AUTO               ON                            INPUT
SVM_MODEL      SVMS_COMPLEXITY_FACTOR  1.887389                      DEFAULT
SVM_MODEL      SVMS_KERNEL_FUNCTION    SVMS_LINEAR                      DEFAULT
SVM_MODEL      SVMS_CONV_TOLERANCE     .001                          DEFAULT
```

The following is an example of querying a model view instead of the older `GEL_MODEL_DETAILS_SVM` routine.

```md
SELECT target_value, attribute_name, attribute_value, coefficient   FROM DM$VLSVM_MODEL;
```

The second example creates an Anomaly Detection model. Anomaly Detection uses SVM Classification without a target. This example uses the same settings table created for the SVM Classification model in the first example.

```md
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

```md
SELECT model_name, mining_function, algorithm FROM user_mining_models;

MODEL_NAME              MINING_FUNCTION      ALGORITHM
----------------------  -------------------- ------------------------------
SVM_MODEL               CLASSIFICATION       SUPPORT_VECTOR_MACHINES
ANOMALY_DETECT_MODEL    CLASSIFICATION       SUPPORT_VECTOR_MACHINES
```

This query shows that only the SVM Classification model has a target.

```md
SELECT model_name, attribute_name, attribute_type, target
       FROM user_mining_model_attributes
       WHERE target = 'YES';

MODEL_NAME          ATTRIBUTE_NAME   ATTRIBUTE_TYPE     TARGET
------------------  ---------------  -----------------  ------
SVM_MODEL           AFFINITY_CARD    CATEGORICAL         YES
```

### CREATE\_MODEL2 Procedure

The `CREATE_MODEL2` procedure is an alternate procedure to the `CREATE_MODEL` procedure, which enables creating a model without extra persistence stages. In the `CREATE_MODEL` procedure, the input is a table or a view and if such an object is not already present, the user must create it. By using the `CREATE_MODEL2` procedure, the user does not need to create such transient database objects.

**Syntax**

```md
DBMS_DATA_MINING.CREATE_MODEL2 (
     model_name            IN VARCHAR2,
     mining_function       IN VARCHAR2,
     data_query            IN CLOB,
     set_list              IN SETTING_LIST,
     case_id_column_name   IN VARCHAR2 DEFAULT NULL,
     target_column_name    IN VARCHAR2 DEFAULT NULL,
     xform_list            IN TRANSFORM_LIST DEFAULT NULL);
```

**Parameters**

Table 63 CREATE\_MODEL2 Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[`schema_name`.\] `model_name`. If you do not specify a schema, then the current schema is used.  See the Usage Notes, CREATE\_MODEL Procedure for model naming restrictions. |
| `mining_function` | The mining function. Values are listed in DBMS\_DATA\_MINING - Mining Function Settings. |
| `data_query` | A query which provides training data for building the model. |
| `set_list` | Specifies the `SETTING_LIST`   `SETTING_LIST` is a table of CLOB index by `VARCHAR2(30)`; Where the index is the setting name and the CLOB is the setting value for that name.\</br> |
| `case_id_column_name` | Case identifier column in the build data. |
| `target_column_name` | For supervised models, the target column in the build data. `NULL` for unsupervised models. |
| `xform_list` | Refer to CREATE\_MODEL Procedure. |

**Usage Notes**

Refer to CREATE\_MODEL Procedure for Usage Notes.

**Examples**

The following example uses the Support Vector Machine algorithm.

```md
declare
 v_setlst DBMS_DATA_MINING.SETTING_LIST;

BEGIN
  v_setlst(dbms_data_mining.algo_name) := dbms_data_mining.algo_support_vector_machines;
  v_setlst(dbms_data_mining.prep_auto) := dbms_data_mining.prep_auto_on;

DBMS_DATA_MINING.CREATE_MODEL2(
    model_name         => 'svm_model',
    mining_function    => dbms_data_mining.classification,
    data_query         => 'select * from mining_data_build_v',
    data_table_name    => 'mining_data_build_v',
    case_id_column_name=> 'cust_id',
    target_column_name => 'affinity_card',
    set_list           => v_setlst,
    case_id_column_name=> 'cust_id',
    target_column_name => 'affinity_card');
END;
/
```

### Create Model Using Registration Information

![Only in Oracle on-premises](img/only-or-onprem.png) This topic applies only to Oracle on-premises.

Users can create models using a registered algorithm name. The `DBMS_DATA_MINING.CREATE_MODEL` function fetches the setting information from the JSON object.

**Usage Notes**

If an algorithm is registered, user can create model using the registered algorithm name. Since all R scripts and default setting values are already registered, providing the value through the setting table is not necessary. This makes the use of this algorithm easier.

**Examples**

The first example builds a Classification model using the GLM algorithm.

```md
CREATE TABLE GLM_RDEMO_SETTINGS_CL (

   setting_name  VARCHAR2(30),
   setting_value VARCHAR2(4000));
   BEGIN
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
         ('ALGO_EXTENSIBLE_LANG', 'R');
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
         (dbms_data_mining.ralg_registration_algo_name, 't1');
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
        (dbms_data_mining.odms_formula,
        'AGE + EDUCATION + HOUSEHOLD_SIZE + OCCUPATION');
        INSERT INTO GLM_RDEMO_SETTINGS_CL VALUES
         ('RALG_PARAMETER_FAMILY',   'binomial(logit)' );
   END;
   /
     BEGIN
          DBMS_DATA_MINING.CREATE_MODEL(
          model_name                    =>    'GLM_RDEMO_CLASSIFICATION',
          mining_function               =>     dbms_data_mining.classification,
          data_table_name               =>    'mining_data_build_v',
          case_id_column_name           =>    'CUST_ID',
          target_column_name            =>    'AFFINITY_CARD',
          settings_table_name           =>    'GLM_RDEMO_SETTINGS_CL');
      END;
      /
```

### DROP\_ALGORITHM Procedure

This function is used to drop the registered algorithm information.

**Syntax**

```md
DBMS_DATA_MINING.DROP_ALGORITHM (algorithm_name  IN  VARCHAR2(30),
                                 cascade         IN  BOOLEAN default FALSE)
```

**Parameters**

Table 64 DROP\_ALGORITHM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `algorithm_name` | Name of the algorithm. |
| `cascade` | If the cascade option is `TRUE`, all the models with this algorithms are forced to drop. There after, the algorithm is dropped. The default value is `FALSE`. |

**Usage Note**

- To drop a mining model, you must be the owner or you must have the `RQADMIN` privilege. See [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG795) for information about privileges for data mining.
- Make sure a model is not built on the algorithm, then drop the algorithm from the system table.
- If you try to drop an algorithm with a model built on it, then an error is displayed.

### DROP\_PARTITION Procedure

The `DROP_PARTITION` procedure drops a single partition that is specified in the parameter `partition_name`.

**Syntax**

```md
DBMS_DATA_MINING.DROP_PARTITION (
      model_name                IN VARCHAR2,
      partition_name            IN VARCHAR2);
```

**Parameters**

Table 65 DROP\_PARTITION Procedure Parameters

| Parameters | Description |
| --- | --- |
| `model_name` | Name of the mining model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Name of the partition that must be dropped. |

### DROP\_MODEL Procedure

This procedure deletes the specified mining model.

**Syntax**

```md
DBMS_DATA_MINING.DROP_MODEL (model_name IN VARCHAR2,
                             force      IN BOOLEAN DEFAULT FALSE);
```

**Parameters**

Table 66 DROP\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the mining model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `force` | Forces the mining model to be dropped even if it is invalid. A mining model may be invalid if a serious system error interrupted the model build process. |

**Usage Note**

To drop a mining model, you must be the owner or you must have the `DROP ANY MINING MODEL` privilege. See [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG795) for information about privileges for data mining.

**Example**

You can use the following command to delete a valid mining model named `nb_sh_clas_sample` that exists in your schema.

```md
BEGIN
  DBMS_DATA_MINING.DROP_MODEL(model_name => 'nb_sh_clas_sample');
END;
/
```

### EXPORT\_MODEL Procedure

This procedure exports the specified data mining models to a dump file set.

To import the models from the dump file set, use the IMPORT\_MODEL Procedure. `EXPORT_MODEL` and `IMPORT_MODEL` use Oracle Data Pump technology.

When Oracle Data Pump is used to export/import an entire schema or database, the mining models in the schema or database are included. However, `EXPORT_MODEL` and `IMPORT_MODEL` are the only utilities that support the export/import of individual models.

**See Also:**

[*Oracle Database Utilities*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SUTIL2877) for information about Oracle Data Pump

[*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG689) for more information about exporting and importing mining models

**Syntax**

```md
DBMS_DATA_MINING.EXPORT_MODEL (
      filename          IN VARCHAR2,
      directory         IN VARCHAR2,
      model_filter      IN VARCHAR2 DEFAULT NULL,
      filesize          IN VARCHAR2 DEFAULT NULL,
      operation         IN VARCHAR2 DEFAULT NULL,
      remote_link       IN VARCHAR2 DEFAULT NULL,
      jobname           IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 67 EXPORT\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `filename` | Name of the dump file set to which the models should be exported. The name must be unique within the schema.  The dump file set can contain one or more files. The number of files in a dump file set is determined by the size of the models being exported (both metadata and data) and a specified or estimated maximum file size. You can specify the file size in the `filesize` parameter, or you can use the `operation` parameter to cause Oracle Data Pump to estimate the file size. If the size of the models to export is greater than the maximum file size, one or more additional files are created.  When the export operation completes successfully, the name of the dump file set is automatically expanded to `filename01.dmp`, even if there is only one file in the dump set. If there are additional files, they are named sequentially as `filename02.dmp`, `filename03.dmp`, and so forth. |
| `directory` | Name of a pre-defined directory object that specifies where the dump file set should be created.  The exporting user must have read/write privileges on the directory object and on the file system directory that it identifies.  See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SQLRF01207) for information about directory objects. |
| `model_filter` | Optional parameter that specifies which model or models to export. If you do not specify a value for `model_filter`, all models in the schema are exported. You can also specify `NULL` (the default) or `'ALL'` to export all models.  You can export individual models by name and groups of models based on mining function or algorithm. For instance, you could export all regression models or all Naive Bayes models. Examples are provided in Table 53-68. |
| `filesize` | Optional parameter that specifies the maximum size of a file in the dump file set. The size may be specified in bytes, kilobytes (K), megabytes (M), or gigabytes (G). The default size is 50 MB.  If the size of the models to export is larger than `filesize`, one or more additional files are created within the dump set. See the description of the `filename` parameter for more information. |
| `operation` | Optional parameter that specifies whether or not to estimate the size of the files in the dump set. By default the size is not estimated and the value of the `filesize` parameter determines the size of the files.  You can specify either of the following values for `operation`:  - `'EXPORT'` - Export all or the specified models. (Default) - `'ESTIMATE'` - Estimate the size of the exporting models. |
| `remote_link` | Optional parameter that specifies the name of a database link to a remote system. The default value is `NULL`. A database link is a schema object in a local database that enables access to objects in a remote database. When you specify a value for `remote_link`, you can export the models in the remote database. The `EXP_FULL_DATABASE` role is required for exporting the remote models. The `EXP_FULL_DATABASE` privilege, the `CREATE DATABASE LINK` privilege, and other privileges may also be required. |
| `jobname` | Optional parameter that specifies the name of the export job. By default, the name has the form `username` `_exp_` `nnnn`, where `nnnn` is a number. For example, a job name in the `SCOTT` schema might be `SCOTT_exp_134`.  If you specify a job name, it must be unique within the schema. The maximum length of the job name is 30 characters.  A log file for the export job, named `jobname.log`, is created in the same directory as the dump file set. |

**Usage Notes**

The `model_filter` parameter specifies which models to export. You can list the models by name, or you can specify all models that have the same mining function or algorithm. You can query the `USER_MINING_MODELS` view to list the models in your schema.

```md
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

Examples of model filters are provided in Table 53-68.

Table 68 Sample Values for the Model Filter Parameter

| Sample Value | Meaning |
| --- | --- |
| `'mymodel'` | Export the model named `mymodel` |
| `'name= ''mymodel'''` | Export the model named `mymodel` |
| `'name IN (''mymodel2'',''mymodel3'')'` | Export the models named `mymodel2` and `mymodel3` |
| `'ALGORITHM_NAME = ''NAIVE_BAYES'''` | Export all Naive Bayes models. See Table 53-5 for a list of algorithm names. |
| `'FUNCTION_NAME =''CLASSIFICATION'''` | Export all classification models. See Table 53-3 for a list of mining functions. |

**Examples**

1. The following statement exports all the models in the `DMUSER3` schema to a dump file set called `models_out` in the directory `$ORACLE_HOME/rdbms/log`. This directory is mapped to a directory object called `DATA_PUMP_DIR`. The `DMUSER3` user has read/write access to the directory and to the directory object.
	```md
	SQL>execute dbms_data_mining.export_model ('models_out', 'DATA_PUMP_DIR');
	```
	You can exit SQL\*Plus and list the resulting dump file and log file.
	```md
	SQL>EXIT
	>cd $ORACLE_HOME/rdbms/log
	>ls
	>DMUSER3_exp_1027.log  models_out01.dmp
	```
2. The following example uses the same directory object and is executed by the same user.This example exports the models called `NMF_SH_SAMPLE` and `SVMR_SH_REGR_SAMPLE` to a different dump file set in the same directory.
	```md
	SQL>EXECUTE DBMS_DATA_MINING.EXPORT_MODEL ( 'models2_out', 'DATA_PUMP_DIR',
	            'name in (''NMF_SH_SAMPLE'', ''SVMR_SH_REGR_SAMPLE'')');
	SQL>EXIT
	>cd $ORACLE_HOME/rdbms/log
	>ls
	>DMUSER3_exp_1027.log  models_out01.dmp
	 DMUSER3_exp_924.log  models2_out01.dmp
	```
3. The following examples show how to export models with specific algorithm and mining function names.
	```md
	SQL>EXECUTE DBMS_DATA_MINING.EXPORT_MODEL('algo.dmp','DM_DUMP',
	        'ALGORITHM_NAME IN (''O_CLUSTER'',''GENERALIZED_LINEAR_MODEL'',
	        ''SUPPORT_VECTOR_MACHINES'',''NAIVE_BAYES'')');
	SQL>EXECUTE DBMS_DATA_MINING.EXPORT_MODEL('func.dmp', 'DM_DUMP',
	        'FUNCTION_NAME IN (CLASSIFICATION,CLUSTERING,FEATURE_EXTRACTION)');
	```

### EXPORT\_SERMODEL Procedure

This procedure exports the model in a serialized format so that they can be moved to another platform for scoring.

When exporting a model in serialized format, the user must pass in an empty `BLOB` locator and specify the model name to be exported. If the model is partitioned, the user can optionally select an individual partition to export, otherwise all partitions are exported. The returned `BLOB` contains the content that can be deployed.

**Syntax**

```md
DBMS_DATA_MINING.EXPORT_SERMODEL (
      model_data     IN OUT NOCOPY BLOB,
      model_name     IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 69 EXPORT\_SERMODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_data` | Provides serialized model data. |
| `model_name` | Name of the mining model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Name of the partition that must be exported. |

**Examples**

The following statement exports all the models in a serialized format.

```md
DECLARE
 v_blob blob;
BEGIN
 dbms_lob.createtemporary(v_blob, FALSE);
 dbms_data_mining.export_sermodel(v_blob, 'MY_MODEL');
-- save v_blob somewhere (e.g., bfile, etc.)
 dbms_lob.freetemporary(v_blob);
END;
/
```

**See Also:** [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG689) for more information about exporting and importing mining models

### FETCH\_JSON\_SCHEMA Procedure

![Only in Oracle on-premises](img/only-or-onprem.png) This topic applies only to Oracle on-premises.

User can fetch and read JSON schema from the `ALL_MINING_ALGORITHMS` view. This function returns the pre-registered JSON schema for R extensible algorithms.

**Syntax**

```md
DBMS_DATA_MINING.FETCH_JSON_SCHEMA RETURN CLOB;
```

**Parameters**

Table 70 FETCH\_JSON\_SCHEMA Procedure

| Parameter | Description |
| --- | --- |
| `RETURN` | This function returns the pre-registered JSON schema for R extensibility.  The default value is `CLOB`. |

**Usage Note**

If a user wants to register a new algorithm using the algorithm registration function, they must fetch and follow the pre-registered JSON schema using this function, when they create the required JSON object metadata, and then pass it to the registration function.

### GET\_ASSOCIATION\_RULES Function

The `GET_ASSOCIATION_RULES` function returns the rules produced by an Association model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*

You can specify filtering criteria to `GET_ASSOCIATION_RULES` to return a subset of the rules. Filtering criteria can improve the performance of the table function. If the number of rules is large, then the greatest performance improvement will result from specifying the `topn` parameter.

**Syntax**

```md
DBMS_DATA_MINING.get_association_rules(
      model_name       IN VARCHAR2,
      topn             IN NUMBER DEFAULT NULL,
      rule_id          IN INTEGER DEFAULT NULL,
      min_confidence   IN NUMBER DEFAULT NULL,
      min_support      IN NUMBER DEFAULT NULL,
      max_rule_length  IN INTEGER DEFAULT NULL,
      min_rule_length  IN INTEGER DEFAULT NULL,
      sort_order       IN ORA_MINING_VARCHAR2_NT DEFAULT NULL,
      antecedent_items IN DM_ITEMS DEFAULT NULL,
      consequent_items IN DM_ITEMS DEFAULT NULL,
      min_lift         IN NUMBER DEFAULT NULL,
      partition_name   IN VARCHAR2 DEFAULT NULL)
  RETURN DM_Rules PIPELINED;
```

**Parameters**

Table 71 GET\_ASSOCIATION\_RULES Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used.  This is the only required parameter of `GET_ASSOCIATION_RULES`. All other parameters specify optional filters on the rules to return. |
| `topn` | Returns the n top rules ordered by confidence and then support, both descending. If you specify a sort order, then the top n rules are derived after the sort is performed.  If `topn` is specified and no maximum or minimum rule length is specified, then the only columns allowed in the sort order are `RULE_CONFIDENCE` and `RULE_SUPPORT`. If `topn` is specified and a maximum or minimum rule length is specified, then `RULE_CONFIDENCE`, `RULE_SUPPORT`, and `NUMBER_OF_ITEMS` are allowed in the sort order. |
| `rule_id` | Identifier of the rule to return. If you specify a value for `rule_id`, do not specify values for the other filtering parameters. |
| `min_confidence` | Returns the rules with confidence greater than or equal to this number. |
| `min_support` | Returns the rules with support greater than or equal to this number. |
| `max_rule_length` | Returns the rules with a length less than or equal to this number.  Rule length refers to the number of items in the rule (See `NUMBER_OF_ITEMS` in Table 53-72). For example, in the rule A=>B (if A, then B), the number of items is 2.  If `max_rule_length` is specified, then the `NUMBER_OF_ITEMS` column is permitted in the sort order. |
| `min_rule_length` | Returns the rules with a length greater than or equal to this number. See `max_rule_length` for a description of rule length.  If `min_rule_length` is specified, then the `NUMBER_OF_ITEMS` column is permitted in the sort order. |
| `sort_order` | Sorts the rules by the values in one or more of the returned columns. Specify one or more column names, each followed by `ASC` for ascending order or `DESC` for descending order. (See Table 53-72 for the column names.)  For example, to sort the result set in descending order first by the `NUMBER_OF_ITEMS` column, then by the `RULE_CONFIDENCE` column, you must specify:  `ORA_MINING_VARCHAR2_NT('NUMBER_OF_ITEMS DESC', 'RULE_CONFIDENCE DESC')`  If you specify `topn`, the results will vary depending on the sort order.  By default, the results are sorted by Confidence in descending order, then by Support in descending order. |
| `antecedent_items` | Returns the rules with these items in the antecedent. |
| `consequent_items` | Returns the rules with this item in the consequent. |
| `min_lift` | Returns the rules with lift greater than or equal to this number. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Return Values**

The object type returned by `GET_ASSOCIATION_RULES` is described in Table 53-72. For descriptions of each field, see the Usage Notes.

Table 72 GET\_ASSOCIATION RULES Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_RULES` | A set of rows of type `DM_RULE`. The rows have the following columns:  ```md (rule_id INTEGER, antecedent DM_PREDICATES, consequent DM_PREDICATES, rule_support NUMBER, rule_confidence NUMBER, rule_lift NUMBER, antecedent_support NUMBER, consequent_support NUMBER, number_of_items INTEGER ) ``` |
| `DM_PREDICATES` | The `antecedent` and `consequent` columns each return nested tables of type `DM_PREDICATES`. The rows, of type `DM_PREDICATE`, have the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), conditional_operator CHAR(2)/*=,<>,<,>,<=,>=*/, attribute_num_value NUMBER, attribute_str_value VARCHAR2(4000), attribute_support NUMBER, attribute_confidence NUMBER) ``` |

**Usage Notes**

1. This table function pipes out rows of type `DM_RULES`. For information on Data Mining data types and piped output from table functions, see “ Datatypes ”.
2. The columns returned by `GET_ASSOCIATION_RULES` are described as follows:
	| Column in DM\_RULES | Description |
	| --- | --- |
	| `rule_id` | Unique identifier of the rule |
	| `antecedent` | The independent condition in the rule. When this condition exists, the dependent condition in the consequent also exists.  The condition is a combination of attribute values called a predicate (`DM_PREDICATE`). The predicate specifies a condition for each attribute. The condition may specify equality (=), inequality (<>), greater than (>), less than (<), greater than or equal to (>=), or less than or equal to (<=) a given value.< p>  `Support` and `Confidence` for each attribute condition in the antecedent is returned in the predicate. Support is the number of transactions that satisfy the antecedent. Confidence is the likelihood that a transaction will satisfy the antecedent.  Note: The occurence of the attribute as a `DM_PREDICATE` indicates the presence of the item in the transaction. The actual value for `attribute_num_value` or `attribute_str_value` is meaningless. For example, the following predicate indicates that 'Mouse Pad' is present in the transaction even though the attribute value is `NULL`.  ```md DM_PREDICATE('PROD_NAME',  'Mouse Pad', '= ', NULL, NULL, NULL, NULL)) ``` |
	| `consequent` | The dependent condition in the rule. This condition exists when the antecedent exists.  The consequent, like the antecedent, is a predicate (`DM_PREDICATE`).  Support and confidence for each attribute condition in the consequent is returned in the predicate. Support is the number of transactions that satisfy the consequent. Confidence is the likelihood that a transaction will satisfy the consequent. |
	| `rule_support` | The number of transactions that satisfy the rule. |
	| `rule_confidence` | The likelihood of a transaction satisfying the rule. |
	| `rule_lift` | The degree of improvement in the prediction over random chance when the rule is satisfied. |
	| `antecedent_support` | The ratio of the number of transactions that satisfy the antecedent to the total number of transactions. |
	| `consequent_support` | The ratio of the number of transactions that satisfy the consequent to the total number of transactions. |
	| `number_of_items` | The total number of attributes referenced in the antecedent and consequent of the rule. |

**Examples**

The following example demonstrates an Association model build followed by several invocations of the `GET_ASSOCIATION_RULES` table function:

```md
-- prepare a settings table to override default settings
CREATE TABLE market_settings AS
SELECT *
  FROM TABLE(DBMS_DATA_MINING.GET_DEFAULT_SETTINGS)
 WHERE setting_name LIKE 'ASSO_%';
BEGIN
-- update the value of the minimum confidence
UPDATE market_settings
   SET setting_value = TO_CHAR(0.081)
 WHERE setting_name = DBMS_DATA_MINING.asso_min_confidence;

-- build an AR model
DBMS_DATA_MINING.CREATE_MODEL(
  model_name => 'market_model',
  function => DBMS_DATA_MINING.ASSOCIATION,
  data_table_name => 'market_build',
  case_id_column_name => 'item_id',
  target_column_name => NULL,
  settings_table_name => 'market_settings');
END;
/
-- View the (unformatted) rules
SELECT rule_id, antecedent, consequent, rule_support,
       rule_confidence
  FROM TABLE(DBMS_DATA_MINING.GET_ASSOCIATION_RULES('market_model'));
```

In the previous example, you view all rules. To view just the top 20 rules, use the following statement.

```md
-- View the top 20 (unformatted) rules
SELECT rule_id, antecedent, consequent, rule_support,
       rule_confidence
  FROM TABLE(DBMS_DATA_MINING.GET_ASSOCIATION_RULES('market_model', 20));
```

The following query uses the Association model `AR_SH_SAMPLE`, which is created from one of the Oracle Data Mining sample programs:

```md
SELECT * FROM TABLE (
   DBMS_DATA_MINING.GET_ASSOCIATION_RULES (
      'AR_SH_SAMPLE', 10, NULL, 0.5, 0.01, 2, 1,
         ORA_MINING_VARCHAR2_NT (
         'NUMBER_OF_ITEMS DESC', 'RULE_CONFIDENCE DESC', 'RULE_SUPPORT DESC'),
         DM_ITEMS(DM_ITEM('CUSTPRODS', 'Mouse Pad', 1, NULL),
                  DM_ITEM('CUSTPRODS', 'Standard Mouse', 1, NULL)),
         DM_ITEMS(DM_ITEM('CUSTPRODS', 'Extension Cable', 1, NULL))));
```

The query returns three rules, shown as follows:

```md
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

**See Also:**

Table 53-72 for the `DM_RULE` column data types.

[*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714) for information about the sample programs.

[*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-AF7C531D-5327-4456-854C-9D6424C5F9EC) for Model Detail Views.

### GET\_FREQUENT\_ITEMSETS Function

The `GET_FREQUENT_ITEMSETS` function returns a set of rows that represent the frequent itemsets from an Association model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

For a detailed description of frequent itemsets, consult [*Oracle Data Mining Concepts*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMCON061).

**Syntax**

```md
DBMS_DATA_MINING.get_frequent_itemsets(
      model_name IN VARCHAR2,
      topn IN NUMBER DEFAULT NULL,
      max_itemset_length IN NUMBER DEFAULT NULL,
      partition_name     IN VARCHAR2 DEFAULT NULL)
  RETURN DM_ItemSets PIPELINED;
```

**Parameters**

Table 73 GET\_FREQUENT\_ITEMSETS Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `topn` | When not `NULL`, return the top *n* rows ordered by support in descending order |
| `max_itemset_length` | Maximum length of an item set. |
| `partition_name` | Specifies a partition in a partitioned model.  Note:  The `partition_name` columns applies only when the model is partitioned. |

**Return Values**

Table 74 GET\_FREQUENT\_ITEMSETS Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_ITEMSETS` | A set of rows of type `DM_ITEMSET`. The rows have the following columns:  ```md (partition_name VARCHAR2(128) itemsets_id NUMBER, items DM_ITEMS, support NUMBER, number_of_items NUMBER) ```  Note:  The `partition_name` columns applies only when the model is partitioned.  The `items` column returns a nested table of type `DM_ITEMS`. The rows have type `DM_ITEM`:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_num_value NUMBER, attribute_str_value VARCHAR2(4000)) ``` |

**Usage Notes**

This table function pipes out rows of type `DM_ITEMSETS`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.

**Examples**

The following example demonstrates an Association model build followed by an invocation of `GET_FREQUENT_ITEMSETS` table function from Oracle SQL.

```md
-- prepare a settings table to override default settings
CREATE TABLE market_settings AS

SELECT * FROM TABLE(DBMS_DATA_MINING.GET_DEFAULT_SETTINGS)
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
  settings_table_name  => 'market_settings');
END;
/

-- View the (unformatted) Itemsets from SQL*Plus
SELECT itemset_id, items, support, number_of_items
  FROM TABLE(DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS('market_model'));
```

In the example above, you view all itemsets. To view just the top 20 itemsets, use the following statement:

```md
-- View the top 20 (unformatted) Itemsets from SQL*Plus
SELECT itemset_id, items, support, number_of_items
  FROM TABLE(DBMS_DATA_MINING.GET_FREQUENT_ITEMSETS('market_model', 20));
```

**See Also:** [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-AF7C531D-5327-4456-854C-9D6424C5F9EC)

### GET\_MODEL\_COST\_MATRIX Function

The `GET_*` interfaces are replaced by model views, and Oracle recommends that users leverage the views instead. The GET\_MODEL\_COST\_MATRIX function is replaced by the `DM$VC` prefixed view, Scoring Cost Matrix. The cost matrix used when building a Decision Tree is made available by the `DM$VM` prefixed view, Decision Tree Build Cost Matrix.

Refer to [Model Detail View for Classification Algorithm](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-38E4FB18-14B2-4A82-B5CE-D2B0EF26DD13).

The `GET_MODEL_COST_MATRIX` function returns the rows of a cost matrix associated with the specified model.

By default, this function returns the scoring cost matrix that was added to the model with the `ADD_COST_MATRIX` procedure. If you wish to obtain the cost matrix used to create a model, specify `cost_matrix_type_create` as the `matrix_type`. See Table 53-75.

See also ADD\_COST\_MATRIX Procedure.

**Syntax**

```md
DBMS_DATA_MINING.GET_MODEL_COST_MATRIX (
      model_name                IN VARCHAR2,
      matrix_type               IN VARCHAR2 DEFAULT cost_matrix_type_score)
      partition_name            IN VARCHAR2 DEFAULT NULL);
RETURN DM_COST_MATRIX PIPELINED;
```

**Parameters**

Table 75 GET\_MODEL\_COST\_MATRIX Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `matrix_type` | The type of cost matrix.  `COST_MATRIX_TYPE_SCORE` - cost matrix used for scoring. (Default.)  `COST_MATRIX_TYPE_CREATE` - cost matrix used to create the model (Decision Tree only). |
| `partition_name` | Name of the partition in a partitioned model |

**Return Values**

Table 76 GET\_MODEL\_COST\_MATRIX Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_COST_MATRIX` | A set of rows of type `DM_COST_ELEMENT`. The rows have the following columns:  ```md actual VARCHAR2(4000), NUMBER, predicted VARCHAR2(4000), cost NUMBER) ``` |

**Usage Notes**

Only Decision Tree models can be built with a cost matrix. If you want to build a Decision Tree model with a cost matrix, specify the cost matrix table name in the `CLAS_COST_TABLE_NAME` setting in the settings table for the model. See Table 53-7.

The cost matrix used to create a Decision Tree model becomes the default scoring matrix for the model. If you want to specify different costs for scoring, you can use the `REMOVE_COST_MATRIX` procedure to remove the cost matrix and the `ADD_COST_MATRIX` procedure to add a new one.

The `GET_MODEL_COST_MATRIX` may return either the build or scoring cost matrix defined for a model or model partition.

If you do not specify a partitioned model name, then an error is displayed.

**Example**

This example returns the scoring cost matrix associated with the Naive Bayes model `NB_SH_CLAS_SAMPLE`.

```md
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

### GET\_MODEL\_DETAILS\_AI Function

The `GET_MODEL_DETAILS_AI` function returns a set of rows that provide the details of an Attribute Importance model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_ai(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN dm_ranked_attributes pipelined;
```

**Parameters**

Table 77 GET\_MODEL\_DETAILS\_AI Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Return Values**

Table 78 GET\_MODEL\_DETAILS\_AI Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_RANKED_ATTRIBUTES` | A set of rows of type `DM_RANKED_ATTRIBUTE`. The rows have the following columns:  ```md (attribute_name VARCHAR2(4000, attribute_subname VARCHAR2(4000), importance_value NUMBER, rank NUMBER(38)) ``` |

**Examples**

The following example returns model details for the Attribute Importance model `AI_SH_sample`, which was created by the sample program `dmaidemo.sql`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

```md
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

### GET\_MODEL\_DETAILS\_EM Function

The `GET_MODEL_DETAILS_EM` function returns a set of rows that provide statistics about the clusters produced by an Expectation Maximization model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

By default, the EM algorithm groups components into high-level clusters, and `GET_MODEL_DETAILS_EM` returns only the high-level clusters with their hierarchies. Alternatively, you can configure EM model to disable the grouping of components into high-level clusters. In this case, `GET_MODEL_DETAILS_EM` returns the components themselves as clusters with their hierarchies. See Table 53-12.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_em(
      model_name VARCHAR2,
      cluster_id NUMBER   DEFAULT NULL,
      attribute  VARCHAR2 DEFAULT NULL,
      centroid   NUMBER   DEFAULT 1,
      histogram  NUMBER   DEFAULT 1,
      rules      NUMBER   DEFAULT 2,
      attribute_subname  VARCHAR2 DEFAULT NULL,
      topn_attributes NUMBER DEFAULT NULL,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN dm_clusters PIPELINED;
```

**Parameters**

Table 79 GET\_MODEL\_DETAILS\_EM Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `cluster_id` | The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise, the details for all clusters are returned. |
| `attribute` | The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned |
| `centroid` | This parameter accepts the following values:  - 1: Details about centroids are returned (default) - 0: Details about centroids are not returned |
| `histogram` | This parameter accepts the following values:  - 1: Details about histograms are returned (default) - 0: Details about histograms are not returned |
| `rules` | This parameter accepts the following values:  - 2: Details about rules are returned (default) - 1: Rule summaries are returned - 0: No information about rules is returned |
| `attribute_subname` | The name of a nested attribute. The full name of a nested attribute has the form:  `attribute_name.attribute_subname`  where `attribute_name` is the name of the column and `attribute_subname` is the name of the nested attribute in that column. If the attribute is not nested, then `attribute_subname` is null. |
| `topn_attributes` | Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the `n` attributes with the highest confidence values in the rules are returned.  If the number of attributes included in the rules is less than `topn`, then, up to `n` additional attributes in alphabetical order are returned.  If both the `attribute` and `topn_attributes` parameters are specified, then `topn_attributes` is ignored. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Usage Notes**

1. For information on Data Mining datatypes and Return Values for Clustering Algorithms piped output from table functions, see “ Datatypes ”.
2. `GET_MODEL_DETAILS` functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model.
3. When cluster statistics are disabled (`EMCS_CLUSTER_STATISTICS` is set to `EMCS_CLUS_STATS_DISABLE`), `GET_MODEL_DETAILS_EM` does not return centroids, histograms, or rules. Only taxonomy (hierarchy) and cluster counts are returned.
4. When the `partition_name` is `NULL` for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-CFBE2171-E775-4C5B-AE61-8242BCDEFE23)

### GET\_MODEL\_DETAILS\_EM\_COMP Function

The `GET_MODEL_DETAILS_EM_COMP` table function returns a set of rows that provide details about the parameters of an Expectation Maximization model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See [Model Detail Views](https://docs.oracle.com/en/database/oracle/oracle-database/19/dmprg/model-detail-views.html) in *Oracle Data Mining User’s Guide*.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_em_comp(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_EM_COMPONENT_SET PIPELINED;
```

**Parameters**

Table 80 GET\_MODEL\_DETAILS\_EM\_COMP Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model to retrieve details for. |

**Return Values**

Table 81 GET\_MODEL\_DETAILS\_EM\_COMP Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_EM_COMPONENT_SET` | A set of rows of type `DM_EM_COMPONENT`. The rows have the following columns:  ```md (info_type VARCHAR2(30), component_id NUMBER, cluster_id NUMBER, attribute_name VARCHAR2(4000), covariate_name VARCHAR2(4000), attribute_value VARCHAR2(4000), value NUMBER ) ``` |

**Usage Notes**

1. This table function pipes out rows of type `DM_EM_COMPONENT`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.
	The columns in each row returned by `GET_MODEL_DETAILS_EM_COMP` are described as follows:
	| Column in DM\_EM\_COMPONENT | Description |
	| --- | --- |
	| `info_type` | The type of information in the row. The following information types are supported:  - `cluster` - `prior` - `mean` - `covariance` - `frequency` |
	| `component_id` | Unique identifier of a component |
	| `cluster_id` | Unique identifier of the high-level leaf cluster for each component |
	| `attribute_name` | Name of an original attribute or a derived feature ID. The derived feature ID is used in models built on data with nested columns. The derived feature definitions can be obtained from the GET\_MODEL\_DETAILS\_EM\_PROJ Function. |
	| `covariate_name` | Name of an original attribute or a derived feature ID used in variance/covariance definition |
	| `attribute_value` | Categorical value or bin interval for binned numerical attributes |
	| `value` | Encodes different information depending on the value of `info_type`, as follows:  - `cluster` - The value field is `NULL` - `prior` - The value field returns the component prior - `mean` - The value field returns the mean of the attribute specified in `attribute_name` - `covariance` - The value field returns the covariance of the attributes specified in `attribute_name` and `covariate_name`. Using the same attribute in `attribute_name` and `covariate_name`, returns the variance. - `frequency` - The value field returns the multivalued Bernoulli frequency parameter for the attribute/value combination specified by `attribute_name` and `attribute_value`  See Usage Note 2 for details. |
2. The following table shows which fields are used for each \`info\_type\`. The blank cells represent \`NULL\`s. | info\_type | component\_id | cluster\_id | attribute\_name | covariate\_name | attribute\_value | value | | --- | --- | --- | --- | --- | --- | --- | | cluster | X | X | | | | | | prior | X | X | | | | X | | mean | X | X | X | | | X | | covariance | X | X | X | X | | X | | frequency | X | X | X | | X | X | {: summary="This table shows which fields of each row are used for each info\_type." }
3. `GET_MODEL_DETAILS` functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model.
4. When the value is `NULL` for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-CFBE2171-E775-4C5B-AE61-8242BCDEFE23)

### GET\_MODEL\_DETAILS\_EM\_PROJ Function

The `GET_MODEL_DETAILS_EM_PROJ` function returns a set of rows that provide statistics about the projections produced by an Expectation Maximization model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_em_proj(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_EM_PROJECTION_SET PIPELINED;
```

**Parameters**

Table 82 GET\_MODEL\_DETAILS\_EM\_PROJ Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model |

**Return Values**

Table 83 GET\_MODEL\_DETAILS\_EM\_PROJ Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_EM_PROJECTION_SET` | A set of rows of type `DM_EM_PROJECTION`. The rows have the following columns:  ```md (feature_name VARCHAR2(4000), attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), coefficient NUMBER ) ```  See Usage Notes for details. |

**Usage Notes**

1. This table function pipes out rows of type `DM_EM_PROJECTION`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.
	The columns in each row returned by `GET_MODEL_DETAILS_EM_PROJ` are described as follows:
	| Column in DM\_EM\_PROJECTION | Description |
	| --- | --- |
	| `feature_name` | Name of a derived feature. The feature maps to the attribute\_name returned by the GET\_MODEL\_DETAILS\_EM Function. |
	| `attribute_name` | Name of a column in the build data |
	| `attribute_subname` | Subname in a nested column |
	| `attribute_value` | Categorical value |
	| `coefficient` | Projection coefficient. The representation is sparse; only the non-zero coefficients are returned. |
2. `GET_MODEL_DETAILS` functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model.
	The coefficients are related to the transformed, not the original, attributes. When returned directly with the model details, the coefficients may not provide meaningful information.
3. When the value is `NULL` for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-CFBE2171-E775-4C5B-AE61-8242BCDEFE23)

### GET\_MODEL\_DETAILS\_GLM Function

The `GET_MODEL_DETAILS_GLM` function returns the coefficient statistics for a Generalized Linear Model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

The same set of statistics is returned for both linear and Logistic Regression, but statistics that do not apply to the mining function are returned as `NULL`. For more details, see the Usage Notes.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_glm(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_GLM_Coeff_Set PIPELINED;
```

**Parameters**

Table 84 GET\_MODEL\_DETAILS\_GLM Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model |

**Return Values**

Table 85 GET\_MODEL\_DETAILS\_GLM Return Values

| Return Value | Description |
| --- | --- |
| `DM_GLM_COEFF_SET` | A set of rows of type `DM_GLM_COEFF`. The rows have the following columns:  ```md (class VARCHAR2(4000), attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), feature_expression VARCHAR2(4000),  coefficient NUMBER, std_error NUMBER, test_statistic NUMBER, p_value NUMBER, VIF NUMBER, std_coefficient NUMBER, lower_coeff_limit NUMBER, upper_coeff_limit NUMBER, exp_coefficient BINARY_DOUBLE, exp_lower_coeff_limit BINARY_DOUBLE, exp_upper_coeff_limit BINARY_DOUBLE) ``` |

`GET_MODEL_DETAILS_GLM` returns a row of statistics for each attribute and one extra row for the intercept, which is identified by a null value in the attribute name. Each row has the `DM_GLM_COEFF` datatype. The statistics are described in Table 53-86.

Table 86 DM\_GLM\_COEFF Datatype Description

| Column | Description |
| --- | --- |
| `class` | The non-reference target class for Logistic Regression. The model is built to predict the probability of this class.  The other class (the reference class) is specified in the model setting `GLMS_REFERENCE_CLASS_NAME`. See Table 53-18.  For Linear Regression, `class` is null. |
| `attribute_name` | The attribute name when there is no subname, or first part of the attribute name when there is a subname. The value of `attribute_name` is also the name of the column in the case table that is the source for this attribute.  For the intercept, `attribute_name` is null. Intercepts are equivalent to the bias term in SVM models. |
| `attribute_subname` | The name of an attribute in a nested table. The full name of a nested attribute has the form:  `attribute_name.attribute_subname`  where `attribute_name` is the name of the nested column in the case table that is the source for this attribute.  If the attribute is not nested, then `attribute_subname` is null. If the attribute is an intercept, then both the `attribute_name` and the `attribute_subname` are null. |
| `attribute_value` | The value of the attribute (categorical attribute only).  For numeric attributes, `attribute_value` is null. |
| `feature_expression` | The feature name constructed by the algorithm when feature generation is enabled and higher-order features are found. If feature selection is not enabled, then the feature name is simply the fully-qualified attribute name (`attribute_name.attribute_subname` if the attribute is in a nested column).  For categorical attributes, the algorithm constructs a feature name that has the following form:  `fully-qualified_attribute_name.attribute_value`  For numeric attributes, the algorithm constructs a name for the higher-order feature by taking the product of the resulting values:  (`attrib1`)\*(`attrib2`))\*......  where `attrib1` and `attrib2` are fully-qualified attribute names. |
| `coefficient` | The linear coefficient estimate. |
| `std_error` | Standard error of the coefficient estimate. |
| `test_statistic` | For Linear Regression, the t-value of the coefficient estimate.  For Logistic Regression, the Wald chi-square value of the coefficient estimate. |
| `p-value` | Probability of the `test_statistic`. Used to analyze the significance of specific attributes in the model. |
| `VIF` | Variance Inflation Factor. The value is zero for the intercept. For Logistic Regression, `VIF` is null. VIF is not computed if the solver is Cholesky. |
| `std_coefficient` | Standardized estimate of the coefficient. |
| `lower_coeff_limit` | Lower confidence bound of the coefficient. |
| `upper_coeff_limit` | Upper confidence bound of the coefficient. |
| `exp_coefficient` | Exponentiated coefficient for Logistic Regression. For Linear Regression, `exp_coefficient` is null. |
| `exp_lower_coeff_limit` | Exponentiated coefficient for lower confidence bound of the coefficient for Logistic Regression. For Linear Regression, `exp_lower_coeff_limit` is null. |
| `exp_upper_coeff_limit` | Exponentiated coefficient for upper confidence bound of the coefficient for Logistic Regression. For Linear Regression, `exp_lower_coeff_limit` is null. |

**Usage Notes**

Not all statistics are necessarily returned for each coefficient. Statistics will be null if:

- They do not apply to the mining function. For example, `exp_coefficient` does not apply to Linear Regression.
- They cannot be computed from a theoretical standpoint. For information on ridge regression, see Table 53-18.
- They cannot be computed because of limitations in system resources.
- Their values would be infinity.
- When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Examples**

The following example returns some of the model details for the GLM Regression model `GLMR_SH_Regr_sample`, which was created by the sample program `dmglrdem.sql`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

```md
SET line 120
SET pages 99
column attribute_name format a30
column attribute_subname format a20
column attribute_value format a20
col coefficient format 990.9999
col std_error format 990.9999
SQL> SELECT * FROM
(SELECT attribute_name, attribute_value, coefficient, std_error
  FROM DM$VDGLMR_SH_REGR_SAMPLE order by 1,2)
WHERE rownum < 11;

ATTRIBUTE_NAME                 ATTRIBUTE_VALUE     COEFFICIENT     STD_ERROR
------------------------------ -------------------- ----------- ---------
AFFINITY_CARD                                         -0.5797         0.5283
BOOKKEEPING_APPLICATION                             -0.4689         3.8872
BULK_PACK_DISKETTES                                 -0.9819         2.5430
COUNTRY_NAME                     Argentina             -1.2020         1.1876
COUNTRY_NAME                     Australia             -0.0071         5.1146
COUNTRY_NAME                     Brazil                 5.2931         1.9233
COUNTRY_NAME                     Canada                  4.0191         2.4108
COUNTRY_NAME                     China                  0.8706         3.5889
COUNTRY_NAME                     Denmark             -2.9822          3.1803
COUNTRY_NAME                     France                 -1.1044         7.1811
```

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-5451C38E-CDEF-4DA3-9741-3C811D3D66EA)

### GET\_MODEL\_DETAILS\_GLOBAL Function

The `GET_MODEL_DETAILS_GLOBAL` function returns statistics about the model as a whole. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

Global details are available for Generalized Linear Models, Association Rules, Singular Value Decomposition, and Expectation Maximization. There are new Global model views which show global information for all algorithms. Oracle recommends that users leverage the views instead. Refer to [Model Details View Global](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-67DD361B-69F7-4D73-9590-844D441590E1).

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_global(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_model_global_details PIPELINED;
```

**Parameters**

Table 87 GET\_MODEL\_DETAILS\_GLOBAL Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Return Values**

Table 88 GET\_MODEL\_DETAILS\_GLOBAL Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_MODEL_GLOBAL_DETAILS` | A collection of rows of type `DM_MODEL_GLOBAL_DETAIL`. The rows have the following columns:  ```md (global_detail_name VARCHAR2(30), global_detail_value NUMBER) ``` |

**Examples**

The following example returns the global model details for the GLM Regression model `GLMR_SH_Regr_sample`, which was created by the sample program `dmglrdem.sql`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

```md
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

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-67DD361B-69F7-4D73-9590-844D441590E1)

### GET\_MODEL\_DETAILS\_KM Function

The `GET_MODEL_DETAILS_KM` function returns a set of rows that provide the details of a *k* -Means clustering model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

You can provide input to `GET_MODEL_DETAILS_KM` to request specific information about the model, thus improving the performance of the query. If you do not specify filtering parameters, then `GET_MODEL_DETAILS_KM` returns all the information about the model.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_km(
      model_name VARCHAR2,
      cluster_id NUMBER   DEFAULT NULL,
      attribute  VARCHAR2 DEFAULT NULL,
      centroid   NUMBER   DEFAULT 1,
      histogram  NUMBER   DEFAULT 1,
      rules      NUMBER   DEFAULT 2,
      attribute_subname  VARCHAR2 DEFAULT NULL,
      topn_attributes NUMBER DEFAULT NULL,
      partition_name VARCHAR2 DEFAULT NULL)
  RETURN dm_clusters PIPELINED;
```

**Parameters**

Table 89 GET\_MODEL\_DETAILS\_KM Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `cluster_id` | The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise the details for all clusters are returned. |
| `attribute` | The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned |
| `centroid` | This parameter accepts the following values:  - 1: Details about centroids are returned (default) - 0: Details about centroids are not returned |
| `histogram` | This parameter accepts the following values:  - 1: Details about histograms are returned (default) - 0: Details about histograms are not returned |
| `rules` | This parameter accepts the following values:  - 2: Details about rules are returned (default) - 1: Rule summaries are returned - 0: No information about rules is returned |
| `attribute_subname` | The name of a nested attribute. The full name of a nested attribute has the form:  `attribute_name.attribute_subname`  where `attribute_name` is the name of the column and `attribute_subname` is the name of the nested attribute in that column.  If the attribute is not nested, `attribute_subname` is null. |
| `topn_attributes` | Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the `n` attributes with the highest confidence values in the rules are returned.  If the number of attributes included in the rules is less than `topn`, then up to `n` additional attributes in alphabetical order are returned.  If both the `attribute` and `topn_attributes` parameters are specified, then `topn_attributes` is ignored. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Usage Notes**

1. The table function pipes out rows of type `DM_CLUSTERS`. For information on Data Mining datatypes and Return Value for Clustering Algorithms piped output from table functions, see “ Datatypes ”.
2. When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Examples**

The following example returns model details for the *k* -Means clustering model `KM_SH_Clus_sample`, which was created by the sample program `dmkmdemo.sql`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

```md
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

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-98B328E3-3FEB-4E84-B8A9-D4E578C2EFAB)

### GET\_MODEL\_DETAILS\_NB Function

The `GET_MODEL_DETAILS_NB` function returns a set of rows that provide the details of a Naive Bayes model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_nb(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_NB_Details PIPELINED;
```

**Parameters**

Table 90 GET\_MODEL\_DETAILS\_NB Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model |

**Return Values**

Table 91 GET\_MODEL\_DETAILS\_NB Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_NB_DETAILS` | A set of rows of type `DM_NB_DETAIL`. The rows have the following columns:  ```md (target_attribute_name VARCHAR2(30), target_attribute_str_value VARCHAR2(4000), target_attribute_num_value NUMBER, prior_probability NUMBER, conditionals DM_CONDITIONALS) ```  The `conditionals` column of `DM_NB_DETAIL` returns a nested table of type `DM_CONDITIONALS`. The rows, of type `DM_CONDITIONAL`, have the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_str_value VARCHAR2(4000), attribute_num_value NUMBER, conditional_probability NUMBER) ``` |

**Usage Notes**

- The table function pipes out rows of type `DM_NB_DETAILS`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.
- When the value is `NULL` for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Examples**

The following query is from the sample program `dmnbdemo.sql`. It returns model details about the model `NB_SH_Clas_sample`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

The query creates labels from the bin boundary tables that were used to bin the training data. It replaces the attribute values with the labels. For numeric bins, the labels are `(`*lower\_boundary*,*upper\_boundary*`]`; for categorical bins, the label matches the value it represents. (This method of categorical label representation will only work for cases where one value corresponds to one bin.) The target was not binned.

```md
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
          NVL(TO_CHAR(T.target_attribute_num_value,T.target_attribute_str_value)) tval,
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

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-12B0E813-9FB6-4057-8736-61DB3A5D4F42)

### GET\_MODEL\_DETAILS\_NMF Function

The `GET_MODEL_DETAILS_NMF` function returns a set of rows that provide the details of a Non-Negative Matrix Factorization model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_nmf(
      model_name IN VARCHAR2,
      partition_name VARCHAR2 DEFAULT NULL)
   RETURN DM_NMF_Feature_Set PIPELINED;
```

**Parameters**

Table 92 GET\_MODEL\_DETAILS\_NMF Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model |

**Return Values**

Table 93 GET\_MODEL\_DETAILS\_NMF Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_NMF_FEATURE_SET` | A set of rows of `DM_NMF_FEATURE`. The rows have the following columns:  ```md (feature_id NUMBER, mapped_feature_id VARCHAR2(4000), attribute_set DM_NMF_ATTRIBUTE_SET) ```  The `attribute_set` column of `DM_NMF_FEATURE` returns a nested table of type `DM_NMF_ATTRIBUTE_SET`. The rows, of type `DM_NMF_ATTRIBUTE`, have the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), coefficient NUMBER) ``` |

**Usage Notes**

- The table function pipes out rows of type `DM_NMF_FEATURE_SET`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.
- When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Examples**

The following example returns model details for the feature extraction model `NMF_SH_Sample`, which was created by the sample program `dmnmdemo.sql`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

```md
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

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-0F8C4CCF-BD8C-4220-877D-C4E729EF210B)

### GET\_MODEL\_DETAILS\_OC Function

The `GET_MODEL_DETAILS_OC` function returns a set of rows that provide the details of an O-Cluster clustering model. The rows are an enumeration of the Clustering patterns generated during the creation of the model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

You can provide input to `GET_MODEL_DETAILS_OC` to request specific information about the model, thus improving the performance of the query. If you do not specify filtering parameters, then `GET_MODEL_DETAILS_OC` returns all the information about the model.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_oc(
      model_name VARCHAR2,
      cluster_id NUMBER   DEFAULT NULL,
      attribute  VARCHAR2 DEFAULT NULL,
      centroid   NUMBER   DEFAULT 1,
      histogram  NUMBER   DEFAULT 1,
      rules      NUMBER   DEFAULT 2,
      topn_attributes NUMBER DEFAULT NULL,
      partition_name VARCHAR2 DEFAULT NULL)
  RETURN dm_clusters PIPELINED;
```

**Parameters**

Table 94 GET\_MODEL\_DETAILS\_OC Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `cluster_id` | The ID of a cluster in the model. When a valid cluster ID is specified, only the details of this cluster are returned. Otherwise the details for all clusters are returned. |
| `attribute` | The name of an attribute. When a valid attribute name is specified, only the details of this attribute are returned. Otherwise, the details for all attributes are returned |
| `centroid` | This parameter accepts the following values:  - 1: Details about centroids are returned (default) - 0: Details about centroids are not returned |
| `histogram` | This parameter accepts the following values:  - 1: Details about histograms are returned (default) - 0: Details about histograms are not returned |
| `rules` | This parameter accepts the following values:  - 2: Details about rules are returned (default) - 1: Rule summaries are returned - 0: No information about rules is returned |
| `topn_attributes` | Restricts the number of attributes returned in the centroid, histogram, and rules objects. Only the `n` attributes with the highest confidence values in the rules are returned.  If the number of attributes included in the rules is less than `topn`, then up to `n` additional attributes in alphabetical order are returned.  If both the `attribute` and `topn_attributes` parameters are specified, then `topn_attributes` is ignored. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Usage Notes**

1. For information about Data Mining datatypes and Return Values for Clustering Algorithms piped output from table functions, see “ Datatypes ”.
2. When the value is NULL for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Examples**

The following example returns model details for the clustering model `OC_SH_Clus_sample`, which was created by the sample program `dmocdemo.sql`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

For each cluster in this example, the split predicate indicates the attribute and the condition used to assign records to the cluster’s children during model build. It provides an important piece of information on how the population within a cluster can be divided up into two smaller clusters.

```md
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

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-8863AF99-07EC-4083-982A-2E5E0CA03887)

### GET\_MODEL\_SETTINGS Function

The `GET_MODEL_SETTINGS` function returns the settings used to build the given model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Static Data Dictionary Views: `ALL_ALL_TABLES` to `ALL_OUTLINES` ” in *Oracle Database Reference*.

**Syntax**

```md
FUNCTION get_model_settings(model_name IN VARCHAR2)
  RETURN DM_Model_Settings PIPELINED;
```

**Parameters**

Table 95 GET\_MODEL\_SETTINGS Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |

**Return Values**

Table 96 GET\_MODEL\_SETTINGS Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_MODEL_SETTINGS` | A set of rows of type `DM_MODEL_SETTINGS`. The rows have the following columns:  ```md DM_MODEL_SETTINGS TABLE OF SYS.DM_MODEL_SETTING Name Type ---------------------- -------------------- SETTING_NAME VARCHAR2(30) SETTING_VALUE VARCHAR2(4000) ``` |

**Usage Notes**

1. This table function pipes out rows of type `DM_MODEL_SETTINGS`. For information on Data Mining datatypes and piped output from table functions, see “ DBMS\_DATA\_MINING Datatypes ”.
2. The setting names/values include both those specified by the user and any defaults assigned by the build process.

**Examples**

The following example returns model model settings for an example Naive Bayes model.

```md
SETTING_NAME                   SETTING_VALUE
------------------------------ ------------------------------
ALGO_NAME                       ALGO_NAIVE_BAYES
PREP_AUTO                       ON
ODMS_MAX_PARTITIONS             1000
NABS_SINGLETON_THRESHOLD       0
CLAS_WEIGHTS_BALANCED          OFF
NABS_PAIRWISE_THRESHOLD        0
ODMS_PARTITION_COLUMNS         GENDER,Y_BOX_GAMES
ODMS_MISSING_VALUE_TREATMENT   ODMS_MISSING_VALUE_AUTO
ODMS_SAMPLING                  ODMS_SAMPLING_DISABLE

9 rows selected.
```

**Related Topics**

- [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN-GUID-41B62782-83FA-4066-8C56-0D0B66CC0EC7)

### GET\_MODEL\_SIGNATURE Function

The `GET_MODEL_SIGNATURE` function returns the list of columns from the build input table that were used by the build process to train the model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Static Data Dictionary Views: `ALL_ALL_TABLES` to `ALL_OUTLINES` ” in *Oracle Database Reference*.

**Syntax**

```md
FUNCTION get_model_signature (model_name IN VARCHAR2)
RETURN DM_Model_Signature PIPELINED;
```

**Parameters**

Table 97 GET\_MODEL\_SIGNATURE Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |

**Return Values**

Table 98 GET\_MODEL\_SIGNATURE Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_MODEL_SIGNATURE` | A set of rows of type `DM_MODEL_SIGNATURE`. The rows have the following columns:  ```md DM_MODEL_SIGNATURE TABLE OF SYS.DM_MODEL_SIGNATURE_ATTRIBUTE Name Type ------------------ ------------------- ATTRIBUTE_NAME VARCHAR2(130) ATTRIBUTE_TYPE VARCHAR2(106) ``` |

**Usage Notes**

1. This table function pipes out rows of type `DM_MODEL_SIGNATURE`. For information on Data Mining datatypes and piped output from table functions, see “ DBMS\_DATA\_MINING Datatypes ”.
2. The signature names or types include only those attributes used by the build process.

**Examples**

The following example returns model settings for an example Naive Bayes model.

```md
ATTRIBUTE_NAME                 ATTRIBUTE_TYPE
------------------------------ ------------------
AGE                            NUMBER
ANNUAL_INCOME                  NUMBER
AVERAGE___ITEMS_PURCHASED      NUMBER
BOOKKEEPING_APPLICATION        NUMBER
BULK_PACK_DISKETTES            NUMBER
BULK_PURCH_AVE_AMT             NUMBER
DISABLE_COOKIES                NUMBER
EDUCATION                      VARCHAR2
FLAT_PANEL_MONITOR             NUMBER
GENDER                         VARCHAR2
HOME_THEATER_PACKAGE           NUMBER
HOUSEHOLD_SIZE                 VARCHAR2
MAILING_LIST                   NUMBER
MARITAL_STATUS                 VARCHAR2
NO_DIFFERENT_KIND_ITEMS        NUMBER
OCCUPATION                     VARCHAR2
OS_DOC_SET_KANJI               NUMBER
PETS                           NUMBER
PRINTER_SUPPLIES               NUMBER
PROMO_RESPOND                  NUMBER
SHIPPING_ADDRESS_COUNTRY       VARCHAR2
SR_CITIZEN                     NUMBER
TOP_REASON_FOR_SHOPPING        VARCHAR2
WKS_SINCE_LAST_PURCH           NUMBER
WORKCLASS                      VARCHAR2
YRS_RESIDENCE                  NUMBER
Y_BOX_GAMES                    NUMBER

27 rows selected.
```

**Related Topics**

- [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN-GUID-41B62782-83FA-4066-8C56-0D0B66CC0EC7)

### GET\_MODEL\_DETAILS\_SVD Function

The `GET_MODEL_DETAILS_SVD` function returns a set of rows that provide the details of a Singular Value Decomposition model. Oracle recommends to use model details view settings. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

Refer to [Model Details View for Singular Value Decomposition](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-3B0E13CF-E479-43E6-B4B6-EE3E6A2D8B06).

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_svd(
      model_name IN VARCHAR2,
      matrix_type IN VARCHAR2 DEFAULT NULL,
      partition_name VARCHAR2 DEFAULT NULL)
   RETURN DM_SVD_MATRIX_Set PIPELINED;
```

**Parameters**

Table 99 GET\_MODEL\_DETAILS\_SVD Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `matrix_type` | Specifies which of the three SVD matrix types to return. Values are: `U`, `S`, `V`, and `NULL`. When `matrix_type` is null (default), all matrices are returned.  The U matrix is only computed when the `SVDS_U_MATRIX_OUTPUT` setting is enabled. It is not computed by default. If the model does not contain U matrices and you set `matrix_type` to `U`, an empty set of rows is returned. See Table 53-26. |
| `partition_name` | A partition in a partitioned model. |

**Return Values**

Table 100 GET\_MODEL\_DETAILS\_SVD Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_SVD_MATRIX_SET` | A set of rows of type `DM_SVD_MATRIX`. The rows have the following columns:  ```md (matrix_type CHAR(1), feature_id NUMBER, mapped_feature_id VARCHAR2(4000), attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), case_id VARCHAR2(4000), value NUMBER, variance NUMBER, pct_cum_variance NUMBER) ```  See Usage Notes for details. |

**Usage Notes**

1. This table function pipes out rows of type `DM_SVD_MATRIX`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.
	The columns in each row returned by `GET_MODEL_DETAILS_SVD` are described as follows:
	| Column in DM\_SVD\_MATRIX\_SET | Description |
	| --- | --- |
	| `matrix_type` | The type of matrix. Possible values are **S**, **V**, and **U**. This field is never null. |
	| `feature_id` | The feature that the matrix entry refers to. |
	| `mapped_feature_id` | A descriptive name for the feature. |
	| `attribute_name` | Column name in the **V** matrix component bases. This field is null for the **S** and **U** matrices. |
	| `attribute_subname` | Subname in the **V** matrix component bases. This is relevant only in the case of a nested column. This field is null for the **S** and **U** matrices. |
	| `case_id` | Unique identifier of the row in the build data described by the **U** matrix projection. This field is null for the **S** and **V** matrices. |
	| `value` | The matrix entry value. |
	| `variance` | The variance explained by a component. It is non-null only for **S** matrix entries. This column is non-null only for **S** matrix entries and for SVD models with setting `dbms_data_mining.svds_scoring_mode` set to `dbms_data_mining.svds_scoring_pca` and the build data is centered, either manually or because the setting `dbms_data_mining.prep_auto` is set to `dbms_data_mining.prep_auto_on`. |
	| `pct_cum_variance` | The percent cumulative variance explained by the components thus far. The components are ranked by the explained variance in descending order.  This column is non-null only for S matrix entries and for SVD models with setting `dbms_data_mining.svds_scoring_mode` set to `dbms_data_mining.svds_scoring_pca` and the build data is centered, either manually or because the setting `dbms_data_mining.prep_auto` is set to `dbms_data_mining.prep_auto_on`. |
2. The output of `GET_MODEL_DETAILS` is in sparse format. Zero values are not returned. Only the diagonal elements of the **S** matrix, the non-zero coefficients in the **V** matrix bases, and the non-zero **U** matrix projections are returned.
	There is one exception: If the data row does not produce non-zero **U** Matrix projections, the case ID for that row is returned with `NULL` for the `feature_id` and `value`. This is done to avoid losing any records from the original data.
3. `GET_MODEL_DETAILS` functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model.
4. When the value is `NULL` for a partitioned model, an exception is thrown. When the value is not null, it must contain the preferred partition name.

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-3B0E13CF-E479-43E6-B4B6-EE3E6A2D8B06)

### GET\_MODEL\_DETAILS\_SVM Function

The `GET_MODEL_DETAILS_SVM` function returns a set of rows that provide the details of a linear Support Vector Machine (SVM) model. If invoked for nonlinear SVM, it returns `ORA-40215`. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Model Detail Views” in *Oracle Data Mining User’s Guide*.

In linear SVM models, only nonzero coefficients are stored. This reduces storage and speeds up model loading. As a result, if an attribute is missing in the coefficient list returned by `GET_MODEL_DETAILS_SVM`, then the coefficient of this attribute should be interpreted as zero.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_svm(
      model_name   VARCHAR2,
      reverse_coef NUMBER DEFAULT 0,
      partition_name VARCHAR2 DEFAULT NULL)
  RETURN DM_SVM_Linear_Coeff_Set PIPELINED;
```

**Parameters**

Table 101 GET\_MODEL\_DETAILS\_SVM Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, then your own schema is used. |
| `reverse_coef` | Whether or not `GET_MODEL_DETAILS_SVM` should transform the attribute coefficients using the original attribute transformations.  When `reverse_coef` is set to 0 (default), `GET_MODEL_DETAILS_SVM` returns the coefficients directly from the model without applying transformations.  When `reverse_coef` is set to 1, `GET_MODEL_DETAILS_SVM` transforms the coefficients and bias by applying the normalization shifts and scales that were generated using automatic data preparation.  See Usage Note 4. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Return Values**

Table 102 GET\_MODEL\_DETAILS\_SVM Function Return Values

| Return Value | Description |
| --- | --- |
| `DM_SVM_LINEAR_COEFF_SET` | A set of rows of type `DM_SVM_LINEAR_COEFF`. The rows have the following columns:  ```md (class VARCHAR2(4000), attribute_set DM_SVM_ATTRIBUTE_SET) ```  The `attribute_set` column returns a nested table of type `DM_SVM_ATTRIBUTE_SET`. The rows, of type `DM_SVM_ATTRIBUTE`, have the following columns:  ```md (attribute_name VARCHAR2(4000), attribute_subname VARCHAR2(4000), attribute_value VARCHAR2(4000), coefficient NUMBER) ```  See Usage Notes. |

**Usage Notes**

1. This table function pipes out rows of type `DM_SVM_LINEAR_COEFF`. For information on Data Mining datatypes and piped output from table functions, see “ Datatypes ”.
2. The `class` column of `DM_SVM_LINEAR_COEFF` contains Classification target values. For SVM Regression models, `class` is null. For each Classification target value, a set of coefficients is returned. For Binary Classification, one-class Classification, and Regression models, only a single set of coefficients is returned.
3. The `attribute_value` column in `DM_SVM_ATTRIBUTE_SET` is used for categorical attributes.
4. \`GET\_MODEL\_DETAILS\` functions preserve model transparency by automatically reversing the transformations applied during the build process. Thus the attributes returned in the model details are the original attributes (or a close approximation of the original attributes) used to build the model. The coefficients are related to the transformed, not the original, attributes. When returned directly with the model details, the coefficients may not provide meaningful information. If you want \`GET\_MODEL\_DETAILS\_SVM\` to transform the coefficients such that they relate to the original attributes, set the \`reverse\_coef\` parameter to 1.
5. When the value is `NULL` for a partitioned model, an exception is thrown. When the value is not null, it must contain the desired partition name.

**Examples**

The following example returns model details for the SVM Classification model `SVMC_SH_Clas_sample`, which was created by the sample program `dmsvcdem.sql`. For information about the sample programs, see [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG714).

```md
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

**Related Topics**

- [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-E40F3A3A-0158-45B4-8FD9-ADF6CA3FB9A6)

### GET\_MODEL\_DETAILS\_XML Function

This function returns an XML object that provides the details of a Decision Tree model.

**Syntax**

```md
DBMS_DATA_MINING.get_model_details_xml(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN XMLType;
```

**Parameters**

Table 103 GET\_MODEL\_DETAILS\_XML Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model. |

**Return Values**

Table 104 GET\_MODEL\_DETAILS\_XML Function Return Value

| Return Value | Description |
| --- | --- |
| `XMLTYPE` | The XML definition for the Decision Tree model. See "XMLTYPE" for details.  The XML definition conforms to the Data Mining Group Predictive Model Markup Language (PMML) version 2.1 specification. The specification is available at [https://dmg.org](https://dmg.org/).  If a nested attribute is used as a splitter, the attribute will appear in the XML document as field="' '.", as opposed to the non-nested attributes which appear in the document as field=" ".  Note:  The column names are surrounded by single quotes and a period separates the column\_name from the subname.  The rest of the document style remains unchanged. |

**Usage Notes**

Special characters that cannot be displayed by Oracle XML are converted to ‘#’.

**Examples**

The following statements in SQL\*Plus return the details of the Decision Tree model `dt_sh_clas_sample`. This model is created by the program `dmdtdemo.sql`, one of the sample data mining programs provided with Oracle Database Examples.

Note: The “”” characters you will see in the XML output are a result of SQL\*Plus behavior. To display the XML in proper format, cut and past it into a file and open the file in a browser.

```md
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

### GET\_MODEL\_TRANSFORMATIONS Function

This function returns the transformation expressions embedded in the specified model. Starting from Oracle Database 12 *c* Release 2, this function is deprecated. See “Static Data Dictionary Views: `ALL_ALL_TABLES` to `ALL_OUTLINES` ” in *Oracle Database Reference*.

All `GET_*` interfaces are replaced by model views, and Oracle recommends that users reference the model views to retrieve the relevant information. The `GET_MODEL_TRANSFORMATIONS` function is replaced by the following:

- USER(/DBA/ALL)\_MINING\_MODEL\_XFORMS: provides the user-embedded transformations
- DM$VX prefixed model view: provides text feature extraction information
- D$VN prefixed mode view: provides normalization and missing value information
- DM$VB: provides binning information

**See Also:**

- “About Transformation Lists” in [DBMS\_DATA\_MINING\_TRANSFORM Operational Notes](DBMS_DATA_MINING_TRANSFORM.md)
- “ GET\_TRANSFORM\_LIST Procedure ”
- “ CREATE\_MODEL Procedure ”
- “ [ALL\_MINING\_MODEL\_XFORMS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN-GUID-7A2ED301-F002-40B4-B9AD-8B5F4E14C716) ” in *Oracle Database Reference*
- “ [DBA\_MINING\_MODEL\_XFORMS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN-GUID-491A0A4F-3D6A-4A4A-8CE5-1580F9EB334A) ” in *Oracle Database Reference*
- “ [USER\_MINING\_MODEL\_XFORMS](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN-GUID-67DD8422-421C-468A-934F-1BC527B9F2D4) ” in *Oracle Database Reference*
- [Model Details View for Binning](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-7DAABEDD-675A-4689-BB1C-A67C2CC46B02)
- [Normalization and Missing Value Handling](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-6411E882-982D-4EC3-9E25-758787876D53)
- [Data Preparation for Text Features](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG-GUID-92F248DB-F500-442A-88F0-FC87ACFCF540)

**Syntax**

```md
DBMS_DATA_MINING.get_model_transformations(
      model_name IN VARCHAR2,
      partition_name IN VARCHAR2 DEFAULT NULL)
  RETURN DM_Transforms PIPELINED;
```

**Parameters**

Table 105 GET\_MODEL\_TRANSFORMATIONS Function Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Indicates the name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |
| `partition_name` | Specifies a partition in a partitioned model |

**Return Values**

Table 106 GET\_MODEL\_TRANSFORMATIONS Function Return Value

| Return Value | Description |
| --- | --- |
| `DM_TRANSFORMS` | The transformation expressions embedded in `model_name`.  The `DM_TRANSFORMS` type is a table of `DM_TRANSFORM` objects. Each `DM_TRANSFORM` has these fields:  ```md attribute_name VARCHAR2(4000) attribute_subname VARCHAR2(4000) expression CLOB reverse_expression CLOB ``` |

**Usage Notes**

When Automatic Data Preparation (ADP) is enabled, both automatic and user-defined transformations may be associated with an attribute. In this case, the user-defined transformations are evaluated before the automatic transformations.

When invoked for a partitioned model, the `partition_name` parameter must be specified.

**Examples**

In this example, several columns in the `SH.CUSTOMERS` table are used to create a Naive Bayes model. A transformation expression is specified for one of the columns. The model does not use ADP.

```md
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

**Related Topics**

- [*Oracle Database Reference*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=REFRN-GUID-41B62782-83FA-4066-8C56-0D0B66CC0EC7)

### GET\_TRANSFORM\_LIST Procedure

This procedure converts transformation expressions specified as `DM_TRANSFORMS` to a transformation list (`TRANSFORM_LIST`) that can be used in creating a model. `DM_TRANSFORMS` is returned by the `GET_MODEL_TRANSFORMATIONS` function.

You can also use routines in the `DBMS_DATA_MINING_TRANSFORM` package to construct a transformation list.

**See Also:**

“About Transformation Lists” in [DBMS\_DATA\_MINING\_TRANSFORM](DBMS_DATA_MINING_TRANSFORM.md)

“ GET\_MODEL\_TRANSFORMATIONS Function ”

“ CREATE\_MODEL Procedure ”

**Syntax**

```md
DBMS_DATA_MINING.GET_TRANSFORM_LIST (
      xform_list           OUT NOCOPY TRANSFORM_LIST,
      model_xforms         IN  DM_TRANSFORMS);
```

**Parameters**

Table 107 GET\_TRANSFORM\_LIST Procedure Parameters

| Parameter | Description |
| --- | --- |
| `xform_list` | A list of transformation specifications that can be embedded in a model. Accepted as a parameter to the CREATE\_MODEL Procedure.  The `TRANSFORM_LIST` type is a table of `TRANSFORM_REC` objects. Each `TRANSFORM_REC` has these fields:  ```md attribute_name VARCHAR2(30) attribute_subname VARCHAR2(4000) expression EXPRESSION_REC reverse_expression EXPRESSION_REC attribute_spec VARCHAR2(4000) ```  For details about the `TRANSFORM_LIST` collection type, see [Table 54-1](DBMS_DATA_MINING_TRANSFORM.md). |
| `model_xforms` | A list of embedded transformation expressions returned by the GET\_MODEL\_TRANSFORMATIONS Function for a specific model.  The `DM_TRANSFORMS` type is a table of `DM_TRANSFORM` objects. Each `DM_TRANSFORM` has these fields:  ```md attribute_name VARCHAR2(4000) attribute_subname VARCHAR2(4000) expression CLOB reverse_expression CLOB ``` |

**Examples**

In this example, a model `mod1` is trained using several columns in the `SH.CUSTOMERS` table. The model uses ADP, which automatically bins one of the columns.

A second model `mod2` is trained on the same data without ADP, but it uses a transformation list that was obtained from `mod1`. As a result, both `mod1` and `mod2` have the same embedded transformation expression.

```md
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

### IMPORT\_MODEL Procedure

This procedure imports one or more data mining models. The procedure is overloaded. You can call it to import mining models from a dump file set, or you can call it to import a single mining model from a PMML document.

**Import from a dump file set**

You can import mining models from a dump file set that was created by the EXPORT\_MODEL Procedure. `IMPORT_MODEL` and `EXPORT_MODEL` use Oracle Data Pump technology to export to and import from a dump file set.

When Oracle Data Pump is used directly to export/import an entire schema or database, the mining models in the schema or database are included. `EXPORT_MODEL` and `IMPORT_MODEL` export/import mining models only.

**Import from PMML**

You can import a mining model represented in Predictive Model Markup Language (PMML). The model must be of type `RegressionModel`, either linear regression or binary logistic regression.

PMML is an XML-based standard specified by the Data Mining Group ([`https://dmg.org`](https://dmg.org/)). Applications that are PMML-compliant can deploy PMML-compliant models that were created by any vendor. Oracle Data Mining supports the core features of PMML 3.1 for regression models.

```md
<div class="infoboxnote" markdown="1">

**See Also:**

[*Oracle Data Mining User's Guide*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG689) for more information about exporting and importing mining models

[*Oracle Database Utilities*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=SUTIL2877) for information about Oracle Data Pump

[\`https://dmg.org/dmg-faq.html\`](https://dmg.org/dmg-faq.html) for more information about PMML

</div>
```

**Syntax**

Imports a mining model from a dump file set:

```md
DBMS_DATA_MINING.IMPORT_MODEL (
      filename          IN  VARCHAR2,
      directory         IN  VARCHAR2,
      model_filter      IN  VARCHAR2 DEFAULT NULL,
      operation         IN  VARCHAR2 DEFAULT NULL,
      remote_link       IN  VARCHAR2 DEFAULT NULL,
      jobname           IN  VARCHAR2 DEFAULT NULL,
      schema_remap      IN  VARCHAR2 DEFAULT NULL,
      tablespace_remap  IN  VARCHAR2 DEFAULT NULL);
```

Imports a mining model from a PMML document:

```md
DBMS_DATA_MINING.IMPORT_MODEL (
      model_name        IN  VARCHAR2,
      pmmldoc           IN  XMLTYPE
      strict_check      IN  BOOLEAN DEFAULT FALSE);
```

**Parameters**

Table 108 IMPORT\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `filename` | Name of the dump file set from which the models should be imported. The dump file set must have been created by the `EXPORT_MODEL` procedure or the `expdp` export utility of Oracle Data Pump.  The dump file set can contain one or more files. (Refer to " EXPORT\_MODEL Procedure " for details.) If the dump file set contains multiple files, you can specify `'` `filename` `%U'` instead of listing them. For example, if your dump file set contains 3 files, `archive01.dmp`, `archive02.dmp`, and `archive03.dmp`, you can import them by specifying `'archive%U'`. |
| `directory` | Name of a pre-defined directory object that specifies where the dump file set is located. Both the exporting and the importing user must have read/write access to the directory object and to the file system directory that it identifies.  Note: The target database must have also have read/write access to the file system directory. |
| `model_filter` | Optional parameter that specifies one or more models to import. If you do not specify a value for `model_filter`, all models in the dump file set are imported. You can also specify `NULL` (the default) or 'ALL' to import all models.  The value of `model_filter` can be one or more model names. The following are valid filters.  ```md 'mymodel1' 'name IN (''mymodel2'',''mymodel3'')' ```  The first causes `IMPORT_MODEL` to import a single model named `mymodel1`. The second causes `IMPORT_MODEL` to import two models, `mymodel2` and `mymodel3`. |
| `operation` | Optional parameter that specifies whether to import the models or the SQL statements that create the models. By default, the models are imported.  You can specify either of the following values for `operation`:  - `'IMPORT'` - Import the models (Default) - `'SQL_FILE'` - Write the SQL DDL for creating the models to a text file. The text file is named `job_name``.sql` and is located in the dump set directory. |
| `remote_link` | Optional parameter that specifies the name of a database link to a remote system. The default value is `NULL`. A database link is a schema object in a local database that enables access to objects in a remote database. When you specify a value for `remote_link`, you can import models into the local database from the remote database. The import is fileless; no dump file is involved. The `IMP_FULL_DATABASE` role is required for importing the remote models. The `EXP_FULL_DATABASE` privilege, the `CREATE DATABASE LINK` privilege, and other privileges may also be required. |
| `jobname` | Optional parameter that specifies the name of the import job. By default, the name has the form `username` `_imp_` `nnnn`, where `nnnn` is a number. For example, a job name in the `SCOTT` schema might be `SCOTT_imp_134`.  If you specify a job name, it must be unique within the schema. The maximum length of the job name is 30 characters.  A log file for the import job, named `jobname``.log,` is created in the same directory as the dump file set. |
| `schema_remap` | Optional parameter for importing into a different schema. By default, models are exported and imported within the same schema.  If the dump file set belongs to a different schema, you must specify a schema mapping in the form `export_user`:`import_user`. For example, you would specify `'SCOTT:MARY'` to import a model exported by `SCOTT` into the `MARY` schema.  Note: In some cases, you may need to have the `IMP_FULL_DATABASE` privilege or the `SYS` role to import a model from a different schema. |
| `tablespace_remap` | Optional parameter for importing into a different tablespace. By default, models are exported and imported within the same tablespace.  If the dump file set belongs to a different tablespace, you must specify a tablespace mapping in the form `export_tablespace`:`import_tablespace`. For example, you would specify `'TBLSPC01:TBLSPC02'` to import a model that was exported from tablespace `TBLSPC01` into tablespace `TBLSPC02`.  Note: In some cases, you may need to have the `IMP_FULL_DATABASE` privilege or the `SYS` role to import a model from a different tablespace. |
| `model_name` | Name for the new model that will be created in the database as a result of an import from PMML The name must be unique within the user’s schema. |
| `pmmldoc` | The PMML document representing the model to be imported. The PMML document has an `XMLTYPE` object type. See “XMLTYPE” for details. |
| `strict_check` | Whether or not an error occurs when the PMML document contains sections that are not part of core PMML (for example, Output or Targets). Oracle Data Mining supports only core PMML; any non-core features may affect the scoring representation.  If the PMML does not strictly conform to core PMML and `strict_check` is set to `TRUE`, then `IMPORT_MODEL` returns an error. If strict\_check is `FALSE` (the default), then the error is suppressed. The model may be imported and scored. |

**Examples**

This example shows a model being exported and imported within the schema `dmuser2`. Then the same model is imported into the `dmuser3` schema. The `dmuser3` user has the `IMP_FULL_DATABASE` privilege. The `dmuser2` user has been assigned the `USER2` tablespace; `dmuser3` has been assigned the `USER3` tablespace.

```md
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
SQL>EXECUTE DBMS_DATA_MINING.EXPORT_MODEL (
            filename =>'NMF_SH_SAMPLE_out',
            directory =>'DATA_PUMP_DIR',
            model_filter => 'name = ''NMF_SH_SAMPLE''');

-- import the model back into the same schema
SQL>EXECUTE DBMS_DATA_MINING.IMPORT_MODEL (
            filename => 'NMF_SH_SAMPLE_out01.dmp',
            directory => 'DATA_PUMP_DIR',
            model_filter => 'name = ''NMF_SH_SAMPLE''');

-- connect as different user
-- import same model into that schema
SQL> connect dmuser3
Enter password: dmuser3_password
Connected.
SQL>EXECUTE DBMS_DATA_MINING.IMPORT_MODEL (
            filename => 'NMF_SH_SAMPLE_out01.dmp',
            directory => 'DATA_PUMP_DIR',
            model_filter => 'name = ''NMF_SH_SAMPLE''',
            operation =>'IMPORT',
            remote_link => NULL,
            jobname => 'nmf_imp_job',
            schema_remap => 'dmuser2:dmuser3',
            tablespace_remap => 'USER2:USER3');
```

The following example shows user `MARY` importing all models from a dump file, `model_exp_001.dmp`, which was created by user `SCOTT`. User `MARY` has been assigned a tablespace named `USER2`; user `SCOTT` was assigned the tablespace `USERS` when the models were exported into the dump file `model_exp_001.dmp`.The dump file is located in the file system directory mapped to a directory object called `DM_DUMP`. If user `MARY` does not have `IMP_FULL_DATABASE` privileges, `IMPORT_MODEL` will raise an error.

```md
-- import all models
DECLARE
  file_name  VARCHAR2(40);
BEGIN
  file_name := 'model_exp_001.dmp';
  DBMS_DATA_MINING.IMPORT_MODEL(
            filename=> 'file_name',
            directory=>'DM_DUMP',
            schema_remap=>'SCOTT:MARY',
            tablespace_remap=>'USERS:USER2');
  DBMS_OUTPUT.PUT_LINE(
           'DBMS_DATA_MINING.IMPORT_MODEL of all models from SCOTT done!');
END;
/
```

This example shows how the user `xuser` could import the model `dmuser.r1mod` from a remote database. The SQL\*Net connection alias for the remote database is `R1DB`. The user `xuser` is assigned the `SYSAUX` tablespace; the user `dmuser` is assigned the `TBS_1` tablespace.

```md
CONNECT / AS SYSDBA;
GRANT CREATE DATABASE LINK TO xuser;
GRANT imp_full_database TO xuser;
CONNECT xuser/xuserpassword
CREATE DATABASE LINK dmuser_link
         CONNECT TO dmuser IDENTIFIED BY dmuserpassword USING 'R1DB';
EXEC dbms_data_mining.import_model (
    NULL,
   'DMUSER_DIR',
   'R1MOD',
    remote_link => 'DMUSER_LINK', schema_remap => 'DMUSER:XUSER',
                    tablespace_remap => 'TBS_1:SYSAUX' );
SELECT name FROM dm_user_models;

NAME

-----------------------------------------------------------------------------
R1MOD
```

This example shows how a PMML document called `SamplePMML1.xml` could be imported from a location referenced by directory object `PMMLDIR` into the schema of the current user. The imported model will be called `PMMLMODEL1`.

```md
BEGIN
    dbms_data_mining.import_model ('PMMLMODEL1',
        XMLType (bfilename ('PMMLDIR', 'SamplePMML1.xml'),
          nls_charset_id ('AL32UTF8')
        ));
END;
```

### IMPORT\_SERMODEL Procedure

This procedure imports the serialized format of the model back into a database.

The import routine takes the serialized content in the `BLOB` and the name of the model to be created with the content. This import does not create model views or tables that are needed for querying model details. The import procedure only provides the ability to score the model.

**Syntax**

```md
DBMS_DATA_MINING.IMPORT_SERMODEL (
      model_data     IN BLOB,
      model_name     IN VARCHAR2,);
```

**Parameters**

Table 109 IMPORT\_SERMODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_data` | Provides model data in `BLOB` format. |
| `model_name` | Name of the mining model in the form \[schema\_name.\]model\_name. If you do not specify a schema, then your own schema is used. |

**Examples**

The following statement imports the serialized format of the models.

```md
declare
 v_blob blob;
BEGIN
 dbms_lob.createtemporary(v_blob, FALSE);
-- fill in v_blob from somewhere (e.g., bfile, etc.)
 dbms_data_mining.import_sermodel(v_blob, 'MY_MODEL');
 dbms_lob.freetemporary(v_blob);
END;
/
```

**Related Topics**

- EXPORT\_SERMODEL Procedure

**See Also:** [*Oracle Data Mining User’s Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/arpls&id=DMPRG689) for more information about exporting and importing mining models

### JSON Schema for R Extensible Algorithm

![Only in Oracle on-premises](img/only-or-onprem.png) This topic applies only to Oracle on-premises.

This procedure helps you create JSON objects following the JSON schema offering flexibility for R Extensibility.

**Usage Note**

Some flexibility when creating a new JSON object is as follows:

- Partial registration is allowed. For example, the detail function can be missing.
- Different orders are allowed. For example, the detail function can be written before the build function or after it.

**Example 53-1 JSON Schema**

JSON schema 1.1 for R extensible algorithm:

```md
{
    "type": "object",
    "properties": {
        "algo_name_display": { "type" : "object",
                                               "properties" : {
                                               "language" : { "type" : "string",
                                                                       "enum" : ["English", "Spanish", "French"],
                                                                       "default" : "English"},
                                               "name" : { "type" : "string"}}
                                             },

        "function_language": {"type": "string" },
        "mining_function": {
                 "type" : "array",
                 "items" : [
                     { "type" : "object",
                        "properties" : {
                           "mining_function_name"  : { "type" : "string"},
                           "build_function": {
                                   "type": "object",
                                   "properties": {
                                        "function_body": { "type": "CLOB" }
                                                        }
                                    },

        "detail_function": {
                 "type" : "array",
                  "items" : [
                      {"type": "object",
                        "properties": {
                             "function_body": { "type": "CLOB" },
                             "view_columns": { "type" : "array",
                                                                   "items" : {
                                                                           "type" : "object",
                                                                           "properties" : {
                                                                               "name" : { "type" : "string"},
                                                                               "type" : { "type" : "string",
                                                                                               "enum" : ["VARCHAR2",
                                                                                                                "NUMBER",
                                                                                                                "DATE",
                                                                                                                "BOOLEAN"]
                                                                                             }
                                                                            }
                                                          }
                                            }
                                 }
                     ]
        },

       "score_function": {
                 "type": "object",
                 "properties": {
                       "function_body": { "type": "CLOB" }
                        }
                 },
        "weight_function": {
                        "type": "object",
                        "properties": {
                            "function_body": { "type": "CLOB" },
                        }
                 }
                               }
           }]
        },

       "algo_setting": {
                "type" : "array",
                "items" : [
                    { "type" : "object",
                       "properties" : {
                          "name"              : { "type" : "string"},
                          "name_display": { "type" : "object",
                                                         "properties" : {
                                                         "language" : { "type" : "string",
                                                                                 "enum" : ["English", "Spanish", "French"],
                                                                                 "default" : "English"},
                                                         "name" : { "type" : "string"}}
                                                      },
                          "type" : { "type" : "string",
                                          "enum" : ["string", "integer", "number", "boolean"]},

                          "optional": {"type" : "BOOLEAN",
                                               "default" : "FALSE"},

                          "value" : { "type" :  "string"},

                          "min_value" : { "type": "object",
                                                      "properties": {
                                                            "min_value": {"type": "number"},
                                                             "inclusive": { "type": "boolean",
                                                                                   "default" : TRUE},
                                                       }
                                                  },
                           "max_value" : {"type": "object",
                                                     "properties": {
                                                          "max_value": {"type": "number"},
                                                          "inclusive": { "type": "boolean",
                                                                                 "default" : TRUE},
                                                            }
                                                    },

                          "categorical choices" : { "type": "array",
                                                                  "items": {
                                                                      "type": "string"
                                                                   }
                                                               },

                          "description_display": { "type" : "object",
                                                                  "properties" : {
                                                                  "language" : { "type" : "string",
                                                                                          "enum" : ["English", "Spanish", "French"],
                                                                                          "default" : "English"},
                                                                  "name" : { "type" : "string"}}
                                                               }
                        }
                    }
                 ]
          }
    }
}
```

**Example 53-2 JSON object example**

The following is an JSON object example that must be passed to the registration procedure:

```md
{  "algo_name_display"   :     {"English", "t1"},
                         "function_language"    :      "R",
                         "mining_function" : {
  "mining_function_name" : "CLASSIFICATION",
                         "build_function" : {"function_body": "function(dat, formula, family) {                                                                                                                                      set.seed(1234);
                                          mod <- glm(formula = formula, data=dat,
                                                      family= eval(parse(text=family))); mod}"},
           "score_function" :  { "function_body": "function(mod, dat) {
                                             res <- predict(mod, newdata = dat, type=''response                                                                                                        '');
                                             res2=data.frame(1-res, res); res2}"}}
                          },
                          "algo_setting" :   [{"name"                : "dbms_data_mining.odms_m                                                                                                                                                                                                                                                                    issing_value_treatment",
                            "name_display"   : {"English", "dbms_data_mining.odms_missing_value                                    _treatment"},
                            "type"                  : "string",
                            "optional"            :  "TRUE",
                            "value"                : "dbms_data_mining.odms_missing_value_mean_mode",
                            "categorical choices"   : [    "dbms_data_mining.odms_missing_value_mean_mode",
                                                                         "dbms_data_mining.odms_missing_value_auto",
                                                                         "dbms_data_mining.odms_missing_value_delete_row"],
                            "description"                : {"English",
                                                                     "how to treat missing values"}
                         },
                                                       {"name"                : "RALG_PARAMETER_FAMILY",
                            "name_display"   : {"English", "RALG_PARAMETER_FAMILY"},
                            "type"                  : "string",
                            "optional"            :  "TRUE",
                            "value"                :  "",
                            "description"       : {"English", "R family parameter in build function"}
                         }
],
                        }
```

### REGISTER\_ALGORITHM Procedure

![Only in Oracle on-premises](img/only-or-onprem.png) This topic applies only to Oracle on-premises.

Use this function to register a new algorithm by providing the algorithm name, data mining function, and other algorithm metadata.

**Syntax**

```md
DBMS_DATA_MINING.REGISTER_ALGORITHM (
                    algorithm_name           IN VARCHAR2,
                    algorithm_metadata       IN CLOB,
                    algorithm_description    IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 110 REGISTER\_ALGORITHM Procedure

| Parameter | Description |
| --- | --- |
| `algorithm_name` | Name of the algorithm. |
| `algorithm_metadata` | Metadata of the algorithm. |
| `algorithm_description` | Description of the algorithm. |

**Usage Notes**

The registration procedure performs the following:

- Checks whether `algorithm_metadata` has correct JSON syntax.
- Checks whether the input JSON object follows the predefined JSON schema.
- Checks whether current user has `RQADMIN` privilege.
- Checks duplicate algorithms so that the same algorithm is not registered twice.
- Checks for missing entries. For example, algorithm name, algorithm type, metadata, and build function.

**Register Algorithms After the JSON Object Is Created**

SQL users can register new algorithms by creating a JSON object following the JSON schema and passing it to the `REGISTER_ALGORITHM` procedure.

```md
BEGIN
  DBMS_DATA_MINING.register_algorithm(
    algorithm_name                 =>   't1',
    algorithm_metadata            =>
    '{"function_language" : "R",
      "mining_function" :
        { "mining_function_name" : "CLASSIFICATION",
           "build_function" : {"function_body": "function(dat, formula, family) { set.seed(1234);
                                          mod <- glm(formula = formula, data=dat,
                                                              family=eval(parse(text=family))); mod}"},
           "score_function" :  {"function_body": "function(mod, dat) {
                                             res <- predict(mod, newdata = dat, type=''response'');
                                             res2=data.frame(1-res, res); res2}"}}
    }',
    algorithm_description  => 't1');
END;
/
```

### RANK\_APPLY Procedure

This procedure ranks the results of an `APPLY` operation based on a top-N specification for predictive and descriptive model results.

For classification models, you can provide a cost matrix as input, and obtain the ranked results with costs applied to the predictions.

**Syntax**

```md
DBMS_DATA_MINING.RANK_APPLY (
      apply_result_table_name        IN VARCHAR2,
      case_id_column_name            IN VARCHAR2,
      score_column_name              IN VARCHAR2,
      score_criterion_column_name    IN VARCHAR2,
      ranked_apply_table_name        IN VARCHAR2,
      top_N                          IN NUMBER (38) DEFAULT 1,
      cost_matrix_table_name         IN VARCHAR2    DEFAULT NULL,
      apply_result_schema_name       IN VARCHAR2    DEFAULT NULL,
      cost_matrix_schema_name        IN VARCHAR2    DEFAULT NULL);
```

**Parameters**

Table 111 RANK\_APPLY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `apply_result_table_name` | Name of the table or view containing the results of an `APPLY` operation on the test data set (see Usage Notes) |
| `case_id_column_name` | Name of the case identifier column. This must be the same as the one used for generating `APPLY` results. |
| `score_column_name` | Name of the prediction column in the apply results table |
| `score_criterion_column_name` | Name of the probability column in the apply results table |
| `ranked_apply_result_tab_name` | Name of the table containing the ranked apply results |
| `top_N` | Top N predictions to be considered from the `APPLY` results for precision recall computation |
| `cost_matrix_table_name` | Name of the cost matrix table |
| `apply_result_schema_name` | Name of the schema hosting the `APPLY` results table |
| `cost_matrix_schema_name` | Name of the schema hosting the cost matrix table |

**Usage Notes**

You can use `RANK_APPLY` to generate ranked apply results, based on a top-N filter and also with application of cost for predictions, if the model was built with costs.

The behavior of `RANK_APPLY` is similar to that of `APPLY` with respect to other DDL-like operations such as `CREATE_MODEL`, `DROP_MODEL`, and `RENAME_MODEL`. The procedure does not depend on the model; the only input of relevance is the apply results generated in a fixed schema table from `APPLY`.

The main intended use of `RANK_APPLY` is for the generation of the final `APPLY` results against the scoring data in a production setting. You can apply the model against test data using `APPLY`, compute various test metrics against various cost matrix tables, and use the candidate cost matrix for `RANK_APPLY`.

The schema for the apply results from each of the supported algorithms is listed in subsequent sections. The `case_id` column will be the same case identifier column as that of the apply results.

**Classification Models - NB and SVM**

For numerical targets, the ranked results table will have the definition as shown:

```md
(case_id       VARCHAR2/NUMBER,
prediction     NUMBER,
probability    NUMBER,
cost           NUMBER,
rank           INTEGER)
```

For categorical targets, the ranked results table will have the following definition:

```md
(case_id       VARCHAR2/NUMBER,
prediction     VARCHAR2,
probability    NUMBER,
cost           NUMBER,
rank           INTEGER)
```

**Clustering Using *k* -Means or O-Cluster**

Clustering is an unsupervised mining function, and hence there are no targets. The results of an `APPLY` operation contains simply the cluster identifier corresponding to a case, and the associated probability. Cost matrix is not considered here. The ranked results table will have the definition as shown, and contains the cluster ids ranked by `top-N`.

```md
(case_id       VARCHAR2/NUMBER,
cluster_id     NUMBER,
probability    NUMBER,
rank           INTEGER)
```

**Feature Extraction using NMF**

Feature extraction is also an unsupervised mining function, and hence there are no targets. The results of an `APPLY` operation contains simply the feature identifier corresponding to a case, and the associated match quality. Cost matrix is not considered here. The ranked results table will have the definition as shown, and contains the feature ids ranked by `top-N`.

```md
(case_id        VARCHAR2/NUMBER,
feature_id      NUMBER,
match_quality   NUMBER,
rank            INTEGER)
```

**Examples**

```md
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

### REMOVE\_COST\_MATRIX Procedure

The `REMOVE_COST_MATRIX` procedure removes the default scoring matrix from a classification model.

**See Also:**

- “ ADD\_COST\_MATRIX Procedure ”
- “ REMOVE\_COST\_MATRIX Procedure ”

**Syntax**

```md
DBMS_DATA_MINING.REMOVE_COST_MATRIX (
      model_name   IN  VARCHAR2);
```

**Parameters**

Table 112 Remove\_Cost\_Matrix Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Name of the model in the form \[schema\_name.\]model\_name. If you do not specify a schema, your own schema is used. |

**Usage Notes**

If the model is not in your schema, then `REMOVE_COST_MATRIX` requires the `ALTER ANY MINING MODEL` system privilege or the `ALTER` object privilege for the mining model.

**Example**

The Naive Bayes model `NB_SH_CLAS_SAMPLE` has an associated cost matrix that can be used for scoring the model.

```md
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

```md
SQL>EXECUTE dbms_data_mining.remove_cost_matrix('nb_sh_clas_sample');

SQL>SELECT *
      FROM TABLE(dbms_data_mining.get_model_cost_matrix('nb_sh_clas_sample'))
      ORDER BY predicted, actual;

no rows selected
```

### RENAME\_MODEL Procedure

This procedure changes the name of the mining model indicated by *model\_name* to the name that you specify as *new\_model\_name*.

If a model with *new\_model\_name* already exists, then the procedure optionally renames *new\_model\_name* to *versioned\_model\_name* before renaming *model\_name* to *new\_model\_name*.

The model name is in the form \[*schema\_name*.\] *model\_name*. If you do not specify a schema, your own schema is used. For mining model naming restrictions, see the Usage Notes for “ CREATE\_MODEL Procedure ”.

**Syntax**

```md
DBMS_DATA_MINING.RENAME_MODEL (
     model_name            IN VARCHAR2,
     new_model_name        IN VARCHAR2,
     versioned_model_name  IN VARCHAR2 DEFAULT NULL);
```

**Parameters**

Table 113 RENAME\_MODEL Procedure Parameters

| Parameter | Description |
| --- | --- |
| `model_name` | Model to be renamed. |
| `new_model_name` | New name for the model `model_name`. |
| `versioned_model_name` | New name for the model `new_model_name` if it already exists. |

**Usage Notes**

If you attempt to rename a model while it is being applied, then the model will be renamed but the apply operation will return indeterminate results.

**Examples**

1. This example changes the name of model `census_model` to `census_model_2012`.
	```md
	BEGIN
	  DBMS_DATA_MINING.RENAME_MODEL(
	    model_name      => 'census_model',
	    new_model_name  => 'census_model_2012');
	END;
	/
	```
2. In this example, there are two classification models in the user’s schema: `clas_mod`, the working model, and `clas_mod_tst`, a test model. The `RENAME_MODEL` procedure preserves `clas_mod` as `clas_mod_old` and makes the test model the new working model.
```md
SELECT model_name FROM user_mining_models;
MODEL_NAME

-------------------------------------------------------------------
CLAS_MOD
CLAS_MOD_TST

BEGIN
  DBMS_DATA_MINING.RENAME_MODEL(
    model_name            => 'clas_mod_tst',
    new_model_name        => 'clas_mod',
    versioned_model_name  => 'clas_mod_old');
END;
/

SELECT model_name FROM user_mining_models;
MODEL_NAME

-------------------------------------------------------------------
CLAS_MOD
CLAS_MOD_OLD
```