---
title: PREDICTION_BOUNDS
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/functions133.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Syntax

![prediction_bounds](img/prediction_bounds.gif)

> ```
> PREDICTION_BOUNDS
> ( [schema.] model
>   [, confidence_level [, class_value]]
>   mining_attribute_clause
> )
> ```
  
  

mining\_attribute\_clause::=

![mining_attribute_clause](img/mining_attribute_clause.gif)

> ```
> USING
> { * 
> | { [ schema . ] table . * 
>   | expr [ AS alias ]
>   }
>     [, { [ schema . ] table . * 
>        | expr [ AS alias ]
>        }
>     ]...
> }
> ```
  
  

Purpose

The `PREDICTION_BOUNDS` function is for use with generalized linear models (GLM) created by the `DBMS_DATA_MINING` package or with Oracle Data Miner. It returns an object with two `NUMBER` fields `LOWER` and `UPPER`. For a regression mining function, the bounds apply to value of the prediction. For a classification mining function, the bounds apply to the probability value. If the GLM was built using ridge regression, or if the covariance matrix is found to be singular during the build, then this function returns `NULL` for both fields.

- For `confidence_level`, specify a number in the range (0,1). If you omit this clause, then the default value is 0.95.
- The `class_value` argument is valid for classification models but not for regression models. By default, the function returns the bounds for the prediction with the highest probability. You can use the `class_value` argument to filter out the bounds value specific to a target value.
	You can specify `class_value` while leaving `confidence_level` at its default by specifying `NULL` for `confidence_level`.
- The `mining_attribute_clause` has the same behavior for `PREDICTION_BOUNDS` that it has for `PREDICTION`. Refer to [mining\_attribute\_clause](functions132.md).

See Also:

- Oracle Data Mining Concepts for detailed information about [Oracle Data Mining](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/toc.htm) and about [generalized linear models](https://docs.oracle.com/cd/E11882_01/datamine.112/e16808/algo_glm.htm#DMCON022)
- [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/models_deploying.htm#DMPRG004) for detailed information about scoring with the Data Mining SQL functions

Example

The following example returns the distribution of customers whose ages are predicted to be between 25 and 45 years with 98% confidence.

This example and the prerequisite data mining operations can be found in the demo file `$ORACLE_HOME/rdbms/demo/dmglcdem.sql`. The example is presented here to illustrate the syntactic use of the function. General information on data mining demo files is available in [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

```
SELECT count(cust_id) cust_count, cust_marital_status
  FROM (SELECT cust_id, cust_marital_status
    FROM mining_data_apply_v
    WHERE PREDICTION_BOUNDS(glmr_sh_regr_sample,0.98 USING *).LOWER > 24 AND
          PREDICTION_BOUNDS(glmr_sh_regr_sample,0.98 USING *).UPPER < 46)
    GROUP BY cust_marital_status;
 
    CUST_COUNT CUST_MARITAL_STATUS
-------------- --------------------
            46 NeverM
             7 Mabsent
             5 Separ.
            35 Divorc.
            72 Married
```