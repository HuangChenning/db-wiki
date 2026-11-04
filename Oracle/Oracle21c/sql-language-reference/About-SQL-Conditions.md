---
title: SQL Language Reference
book: SQL Language Reference
doc_id: F31301-19
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqlrf/About-SQL-Conditions.html
tags:
  - oracle
  - 21c
  - sql-language-reference
---

## About SQL Conditions

Conditions can have several forms, as shown in the following syntax.

condition::=

![condition](img/condition.gif)

> ```
> { comparison_condition
> | floating_point_condition
> | logical_condition
> | model_condition
> | multiset_condition
> | pattern_matching_condition
> | range_condition
> | null_condition
> | XML_condition
> | JSON_condition
> | compound_condition
> | exists_condition
> | in_condition
> | is_of_type_condition
> }
> ```
>
> ![Oracle Logo](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/gifs/oracle.gif)[  
> Copyright © 1996, 2025, Oracle and/or its affiliates.](https://docs.oracle.com/en/database/oracle/oracle-database/dcommon/html/cpyr.htm)


If you have installed Oracle Text, then you can create conditions with the built-in operators that are part of that product, including `CONTAINS`, `CATSEARCH`, and `MATCHES`. For more information on these Oracle Text elements, refer to [Oracle Text Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqlrf&id=CCREF0103).

The sections that follow describe the various forms of conditions. You must use appropriate condition syntax whenever `condition` appears in SQL statements.

You can use a condition in the `WHERE` clause of these statements:

- `DELETE`
- `SELECT`
- `UPDATE`

You can use a condition in any of these clauses of the `SELECT` statement:

- `WHERE`
- `START` `WITH`
- `CONNECT` `BY`
- `HAVING`

A condition could be said to be of a logical data type, although Oracle Database does not formally support such a data type.

The following simple condition always evaluates to `TRUE`:

```
1 = 1
```

The following more complex condition adds the `salary` value to the `commission_pct` value (substituting the value 0 for null) and determines whether the sum is greater than the number constant 25000:

```
NVL(salary, 0) + NVL(salary + (salary*commission_pct, 0) > 25000)
```

Logical conditions can combine multiple conditions into a single condition. For example, you can use the `AND` condition to combine two conditions:

```
(1 = 1) AND (5 < 7)
```

Here are some valid conditions:

```
name = 'SMITH' 
employees.department_id = departments.department_id 
hire_date > '01-JAN-08' 
job_id IN ('SA_MAN', 'SA_REP') 
salary BETWEEN 5000 AND 10000
commission_pct IS NULL AND salary = 2100
```

Oracle Database does not accept all conditions in all parts of all SQL statements. Refer to the section devoted to a particular SQL statement in this book for information on restrictions on the conditions in that statement.

### Condition Precedence

Precedence is the order in which Oracle Database evaluates different conditions in the same expression. When evaluating an expression containing multiple conditions, Oracle evaluates conditions with higher precedence before evaluating those with lower precedence. Oracle evaluates conditions with equal precedence from left to right within an expression, with the following exceptions:

- Left to right evaluation is not guaranteed for multiple conditions connected using `AND`
- Left to right evaluation is not guaranteed for multiple conditions connected using `OR`

Table 6-1 lists the levels of precedence among SQL condition from high to low. Conditions listed on the same line have the same precedence. As the table indicates, Oracle evaluates operators before conditions.

Table 6-1 SQL Condition Precedence

| Type of Condition | Purpose |
| --- | --- |
| SQL operators are evaluated before SQL conditions | See [Operator Precedence](About-SQL-Operators.md) |
| `=, !=, <, >, <=, >=, ` | comparison |
| `IS [NOT] NULL, LIKE, [NOT] BETWEEN, [NOT] IN, EXISTS, IS OF ` `type` | comparison |
| `NOT` | exponentiation, logical negation |
| `AND` | conjunction |
| `OR` | disjunction |