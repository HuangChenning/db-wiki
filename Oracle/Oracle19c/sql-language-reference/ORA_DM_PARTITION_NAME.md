---
title: ORA_DM_PARTITION_NAME
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ORA_DM_PARTITION_NAME.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Syntax

[Description of the illustration ora\_dm\_partition\_name.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/ora_dm_partition_name.html)

## mining\_attribute\_clause::=

[Description of the illustration mining\_attribute\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/mining_attribute_clause.html)

## Purpose

`ORA_DM_PARTITION_NAME` is a single row function that works along with other existing functions. This function returns the name of the partition associated with the input row. When `ORA_DM_PARTITION_NAME` is used on a non-partitioned model, the result is `NULL`.

The syntax of the `ORA_DM_PARTITION_NAME` function can use an optional `GROUPING` hint when scoring a partitioned model. See [GROUPING Hint](Comments.md).

## mining\_attribute\_clause

The *mining\_attribute\_clause* identifies the column attributes to use as predictors for scoring. When the function is invoked with the analytic syntax, these predictors are also used for building the transient models. The *mining\_attribute\_clause* behaves as described for the `PREDICTION` function. See *[mining\_attribute\_clause](PREDICTION.md)*.

```md
<div class="infoboxnote" markdown="1">

**See Also:**

- [*Oracle Data Mining User's Guide*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=DMPRG004) for information about scoring

- [*Oracle Data Mining Concepts*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=DMCON008) for information about clustering

</div>  **Note:**   The following examples are excerpted from the Data Mining sample programs. For more information about the sample programs, see in [*Oracle Data Mining User's Guide*](/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=DMPRG714).
```

## Example

```md
SELECT prediction(mymodel using *) pred, ora_dm_partition_name(mymodel USING *) pname FROM customers;
```