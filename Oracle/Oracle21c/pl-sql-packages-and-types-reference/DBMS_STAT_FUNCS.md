---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_STAT_FUNCS.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 176 DBMS\_STAT\_FUNCS

This chapter contains the following topic:

- Summary of DBMS\_STAT\_FUNCS Subprograms

### 176.1 Summary of DBMS\_STAT\_FUNCS Subprograms

This table lists and briefly describes the DBMS\_STAT\_FUNCS subprograms.

Table 176-1 DBMS\_STAT\_FUNCS Package Subprograms

| Subprogram | Description |
| --- | --- |
| EXPONENTIAL\_DIST\_FIT Procedure | Tests how well a sample of values fits an exponential distribution |
| NORMAL\_DIST\_FIT Procedure | Tests how well a sample of values fits a normal distribution |
| POISSON\_DIST\_FIT Procedure | Tests how well a sample of values fits a Poisson distribution |
| SUMMARY Procedure | Summarizes a numerical column of a table |
| UNIFORM\_DIST\_FIT Procedure | Tests how well a sample of values fits a uniform distribution |
| WEIBULL\_DIST\_FIT Procedure | Tests how well a sample of values fits a Weibull distribution |

#### 176.1.1 EXPONENTIAL\_DIST\_FIT Procedure

This procedure tests how well a sample of values fits an exponential distribution.

Syntax

```
DBMS_STAT_FUNCS.EXPONENTIAL_DIST_FIT (
   ownername    IN    VARCHAR2,
   tablename    IN    VARCHAR2,
   columnname   IN    VARCHAR2,
   test_type    IN    VARCHAR2 DEFAULT 'KOLMOGOROV_SMIRNOV',
   lambda       IN    NUMBER,
   mu           IN    NUMBER,
   sig          OUT   NUMBER);
```

Parameters

Table 176-2 EXPONENTIAL\_DIST\_FIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | The schema where the table resides. |
| `tablename` | The table where the column resides. |
| `columnname` | The column of the table against which to run the test. |
| `test_type` | The type of test to use: ' `CHI_SQUARED'`, ' `KOLMOGOROV_SMIRNOV'` or ' `ANDERSON_DARLING'`. |
| `lambda` | The scale parameter. |
| `mu` | The location parameter. |
| `sig` | The goodness of fit value, based on test type. A small value indicates a significant difference between the sample and the exponential distribution. A number close to 1 indicates a close match. |

#### 176.1.2 NORMAL\_DIST\_FIT Procedure

This procedure tests how well a sample of values fits a normal distribution.

Syntax

```
DBMS_STAT_FUNCS.NORMAL_DIST_FIT (
   ownername    IN    VARCHAR2,
   tablename    IN    VARCHAR2,
   columnname   IN    VARCHAR2,
   test_type    IN    VARCHAR2 DEFAULT 'SHAPIRO_WILKS',
   mean         IN    NUMBER,
   stdev        IN    NUMBER,
   sig          OUT   NUMBER);
```

Parameters

Table 176-3 NORMAL\_DIST\_FIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | The schema where the table resides. |
| `tablename` | The table where the column resides. |
| `columnname` | The column of the table against which to run the test. |
| `test_type` | The type of test to use: ' `CHI_SQUARED'`, ' `KOLMOGOROV_SMIRNOV'`, ' `ANDERSON_DARLING'` or ' `SHAPIRO_WILKS` '. |
| `mean` | The mean of the distribution against which to compare. |
| `stdev` | The standard deviation of the distribution against which to compare. |
| `sig` | The goodness of fit value, based on test type. A small value indicates a significant difference between the sample and the normal distribution. A number close to 1 indicates a close match. |

#### 176.1.3 POISSON\_DIST\_FIT Procedure

This procedure tests how well a sample of values fits a Poisson distribution.

Syntax

```
DBMS_STAT_FUNCS.POISSON_DIST_FIT (
   ownername    IN    VARCHAR2,
   tablename    IN    VARCHAR2,
   columnname   IN    VARCHAR2,
   test_type    IN    VARCHAR2 DEFAULT 'KOLMOGOROV_SMIRNOV',
   lambda       IN    NUMBER,
   sig          OUT   NUMBER);
```

Parameters

Table 176-4 POISSON\_DIST\_FIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | The schema where the table resides. |
| `tablename` | The table where the column resides. |
| `columnname` | The column of the table against which to run the test. |
| `test_type` | The type of test to use: ' `KOLMOGOROV_SMIRNOV'` or ' `ANDERSON_DARLING'`. |
| `lambda` | The lambda parameter is the shape parameter. |
| `sig` | The goodness of fit value, based on test type. A small value indicates a significant difference between the sample and the Poisson distribution. A number close to 1 indicates a close match. |

#### 176.1.4 SUMMARY Procedure

This procedure summarizes the numerical column specified in the `columnname` of `tablename`.

The summary is returned as a Summary Type. Note that most of the output of `SUMMARY` can be obtained with currently available SQL.

Syntax

```
DBMS_STAT_FUNCS.SUMMARY (
   ownername    IN    VARCHAR2,
   tablename    IN    VARCHAR2,
   columnname   IN    VARCHAR2,
   sigma_value  IN    NUMBER DEFAULT 3,
   s           OUT    SummaryType);
```

Parameters

Table 176-5 SUMMARY Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | The schema where the table resides. |
| `tablename` | The table where the column resides. |
| `columnname` | The column of the table to be summarized. |
| `sigma_value` | The number of sigmas for the set of extreme values, defaults to 3. |
| `s` | The Record containing summary information about given column. |

Definition of SummaryType

```
TYPE n_arr IS VARRAY(5) of NUMBER;
TYPE num_table IS TABLE of NUMBER;
TYPE summaryType IS RECORD (
   count             NUMBER,
   min               NUMBER,
   max               NUMBER,
   range             NUMBER,
   mean              NUMBER,
   cmode             num_table,
   variance          NUMBER,
   stddev            NUMBER,
   quantile_5        NUMBER,
   quantile_25       NUMBER,
   median            NUMBER,
   quantile_75       NUMBER,
   quantile_95       NUMBER,
   plus_x_sigma      NUMBER,
   minus_x_sigma     NUMBER,
   extreme_values    num_table,
   top_5_values      n_arr,
   bottom_5_values   n_arr);
```

#### 176.1.5 UNIFORM\_DIST\_FIT Procedure

This procedure tests well a sample of values fits a uniform distribution.

Syntax

```
DBMS_STAT_FUNCS.UNIFORM_DIST_FIT (
   ownername    IN    VARCHAR2,
   tablename    IN    VARCHAR2,
   columnname   IN    VARCHAR2,
   var_type     IN    VARCHAR2 DEFAULT 'CONTINUOUS',
   test_type    IN    VARCHAR2 DEFAULT 'KOLMOGOROV_SMIRNOV',
   paramA       IN    NUMBER,
   paramB       IN    NUMBER,
   sig          OUT   NUMBER);
```

Parameters

Table 176-6 UNIFORM\_DIST\_FIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | The schema where the table resides. |
| `tablename` | The table where the column resides. |
| `columnname` | The column of the table against which to run the test. |
| `var_type` | The type of distribution: ' `CONTINUOUS'` (the default) or ' `DISCRETE` ' |
| `test_type` | The type of test to use: ' `CHI_SQUARED'`, ' `KOLMOGOROV_SMIRNOV'` or ' `ANDERSON_DARLING'`. |
| `paramA` | Parameter A estimated from the sample (the location parameter). |
| `paramB` | Parameter B estimated from the sample (the scale parameter). |
| `sig` | The goodness of fit value, based on test type. A small value indicates a significant difference between the sample and the uniform distribution. A number close to 1 indicates a close match. |

#### 176.1.6 WEIBULL\_DIST\_FIT Procedure

This procedure tests how well a sample of values fits a Weibull distribution.

Syntax

```
DBMS_STAT_FUNCS.WEIBULL_DIST_FIT (
   ownername    IN    VARCHAR2,
   tablename    IN    VARCHAR2,
   columnname   IN    VARCHAR2,
   test_type    IN    VARCHAR2 DEFAULT 'KOLMOGOROV_SMIRNOV',
   alpha        IN    NUMBER,
   mu           IN    NUMBER,
   beta         IN    NUMBER,
   sig          OUT   NUMBER);
```

Parameters

Table 176-7 WEIBULL\_DIST\_FIT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `ownername` | The schema where the table resides. |
| `tablename` | The table where the column resides. |
| `columnname` | The column of the table against which to run the test. |
| `test_type` | The type of test to use: ' `CHI_SQUARED'`, ' `KOLMOGOROV_SMIRNOV'` or ' `ANDERSON_DARLING'`. |
| `alpha` | The scale parameter. |
| `mu` | The location parameter. |
| `beta` | The slope/shape parameter. |
| `sig` | The goodness of fit value, based on test type. A small value indicates a significant difference between the sample and the Weibull distribution. A number close to 1 indicates a close match. |