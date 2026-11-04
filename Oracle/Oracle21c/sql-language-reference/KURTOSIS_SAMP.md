---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/KURTOSIS_SAMP.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## KURTOSIS\_SAMP

Syntax

![kurtosis_samp](img/kurtosis_samp.gif)

> ```
> KURTOSIS_SAMP ( [DISTINCT | ALL | UNIQUE] expr )
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


Purpose

The sample kurtosis function `KURTOSIS_SAMP` is primarily used to determine the characteristics of outliers in a given distribution.

NULL values in `expr` are ignored.

Returns NULL if all rows in the group have NULL `expr` values.

Returns 0 if there are one or two rows in `expr`.

For a given set of values, the result of sample kurtosis (`KURTOSIS_SAMP`) and population kurtosis (`KURTOSIS_POP`) are always deterministic. However, the values of `KURTOSIS_SAMP` and `KURTOSIS_POP` differ. As the number of values in the data set increases, the difference between the computed values of `KURTOSIS_SAMP` and `KURTOSIS_POP` decreases.