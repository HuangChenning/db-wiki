---
title: CREATE DIMENSION
book: SQL Language Reference
doc_id: E96310-37
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-DIMENSION.html
tags:
  - oracle
  - 19c
  - sql-language-reference
---

## Purpose

Use the `CREATE` `DIMENSION` statement to create a **dimension**. A dimension defines a parent-child relationship between pairs of column sets, where all the columns of a column set must come from the same table. However, columns in one column set (called a **level**) can come from a different table than columns in another set. The optimizer uses these relationships with materialized views to perform **query rewrite**. The SQL Access Advisor uses these relationships to recommend creation of specific materialized views.

**Note:** Oracle Database does not automatically validate the relationships you declare when creating a dimension. To validate the relationships specified in the *hierarchy\_clause* and the *dimension\_join\_clause* of `CREATE` `DIMENSION`, you must run the `DBMS_OLAP`.`VALIDATE_DIMENSION` procedure.

**See Also:**

- [CREATE MATERIALIZED VIEW](CREATE-MATERIALIZED-VIEW.md) for more information on materialized views
- [*Oracle Database SQL Tuning Guide*](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/sqlrf&id=TGSQL591) for more information on query rewrite, the optimizer and the SQL Access Advisor

## Prerequisites

To create a dimension in your own schema, you must have the `CREATE` `DIMENSION` system privilege. To create a dimension in another user’s schema, you must have the `CREATE` `ANY` `DIMENSION` system privilege. In either case, you must have the `READ` or `SELECT` object privilege on any objects referenced in the dimension.

## Syntax

## create\_dimension::=

[Description of the illustration create\_dimension.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/create_dimension.html)

## level\_clause::=

[Description of the illustration level\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/level_clause.html)

## hierarchy\_clause::=

[Description of the illustration hierarchy\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/hierarchy_clause.html)

## dimension\_join\_clause::=

[Description of the illustration dimension\_join\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/dimension_join_clause.html)

## attribute\_clause::=

[Description of the illustration attribute\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/attribute_clause.html)

## extended\_attribute\_clause::=

[Description of the illustration extended\_attribute\_clause.eps](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/img_text/extended_attribute_clause.html)

## Semantics

## schema

Specify the schema in which the dimension will be created. If you do not specify *schema*, then Oracle Database creates the dimension in your own schema.

## dimension

Specify the name of the dimension. The name must satisfy the requirements listed in “ [Database Object Naming Rules](Database-Object-Names-and-Qualifiers.md) ”.

## level\_clause

The *level\_clause* defines a level in the dimension. A level defines dimension hierarchies and attributes.

***level***

Specify the name of the level.

***level\_table. level\_column***

Specify the columns in the level. You can specify up to 32 columns. The tables you specify in this clause must already exist.

**SKIP WHEN NULL**

Specify this clause to indicate that if the specified level is `NULL`, then the level is to be skipped. This clause lets you preserve the hierarchical chain of parent-child relationship by an alternative path that skips over the specified level. See *hierarchy\_clause*.

**Restrictions on Dimension Level Columns**

Dimension level columns are subject to the following restrictions:

- All of the columns in a level must come from the same table.
- If columns in different levels come from different tables, then you must specify the *dimension\_join\_clause*.
- The set of columns you specify must be unique to this level.
- The columns you specify cannot be specified in any other dimension.
- Each `level_column` must be non-null unless the level is specified with `SKIP` `WHEN` `NULL`. The non-null columns need not have `NOT` `NULL` constraints. The column for which you specify `SKIP` `WHEN` `NULL` cannot have a `NOT` `NULL` constraint).

##

## hierarchy\_clause

The *hierarchy\_clause* defines a linear hierarchy of levels in the dimension. Each hierarchy forms a chain of parent-child relationships among the levels in the dimension. Hierarchies in a dimension are independent of each other. They may, but need not, have columns in common.

Each level in the dimension should be specified at most once in this clause, and each level must already have been named in the *level\_clause.*

***hierarchy***

Specify the name of the hierarchy. This name must be unique in the dimension.

***child\_level***

Specify the name of a level that has an n:1 relationship with a parent level. The *level\_columns* of *child\_level* cannot be null, and each *child\_level* value uniquely determines the value of the next named *parent\_level*.

If the child *level\_table* is different from the parent *level\_table*, then you must specify a join relationship between them in the *dimension\_join\_clause*.

***parent\_level***

Specify the name of a level.

## dimension\_join\_clause

The *dimension\_join\_clause* lets you specify an inner equijoin relationship for a dimension whose columns are contained in multiple tables. This clause is required and permitted only when the columns specified in the hierarchy are not all in the same table.

***child\_key\_column***

Specify one or more columns that are join-compatible with columns in the parent level.

If you do not specify the schema and table of each *child\_column*, then the schema and table are inferred from the `CHILD` `OF` relationship in the *hierarchy\_clause*. If you do specify the schema and column of a *child\_key\_column*, then the schema and table must match the schema and table of columns in the child of *parent\_level* in the *hierarchy\_clause*.

***parent\_level***

Specify the name of a level.

**Restrictions on Join Dimensions**

Join dimensions are subject to the following restrictions:

- You can specify only one *dimension\_join\_clause* for a given pair of levels in the same hierarchy.
- The *child\_key\_columns* must be non-null, and the parent key must be unique and non-null. You need not define constraints to enforce these conditions, but queries may return incorrect results if these conditions are not true.
- Each child key must join with a key in the *parent\_level* table.
- Self-joins are not permitted. The *child\_key\_columns* cannot be in the same table as *parent\_level*.
- All of the child key columns must come from the same table.
- The number of child key columns must match the number of columns in *parent\_level*, and the columns must be joinable.
- You cannot specify multiple child key columns unless the parent level consists of multiple columns.

## attribute\_clause

The *attribute\_clause* lets you specify the columns that are uniquely determined by a hierarchy level. The columns in *level* must all come from the same table as the *dependent\_columns*. The *dependent\_columns* need not have been specified in the *level\_clause*.

For example, if the hierarchy levels are `city`, `state`, and `country`, then `city` might determine `mayor`, `state` might determine `governor`, and `country` might determine `president`.

## extended\_attribute\_clause

This clause lets you specify an attribute name for one or more level-to-column relations. The type of attribute you create with this clause is not different from the type of attribute created using the *attribute\_clause*. The only difference is that this clause lets you assign a name to the attribute that is different from the level name.

## Examples

**Creating a Dimension: Examples**

This statement was used to create the `customers_dim` dimension in the sample schema `sh`:

```md
CREATE DIMENSION customers_dim
   LEVEL customer   IS (customers.cust_id)
   LEVEL city       IS (customers.cust_city)
   LEVEL state      IS (customers.cust_state_province)
   LEVEL country    IS (countries.country_id)
   LEVEL subregion  IS (countries.country_subregion)
   LEVEL region     IS (countries.country_region)
   HIERARCHY geog_rollup (
      customer      CHILD OF
      city          CHILD OF
      state         CHILD OF
      country       CHILD OF
      subregion     CHILD OF
      region
   JOIN KEY (customers.country_id) REFERENCES country
   )
   ATTRIBUTE customer DETERMINES
   (cust_first_name, cust_last_name, cust_gender,
    cust_marital_status, cust_year_of_birth,
    cust_income_level, cust_credit_limit)
   ATTRIBUTE country DETERMINES (countries.country_name)
;
```

**Creating a Dimension with Extended Attributes: Example**

Alternatively, the *extended\_attribute\_clause* could have been used instead of the *attribute\_clause*, as shown in the following example:

```md
CREATE DIMENSION customers_dim
   LEVEL customer   IS (customers.cust_id)
   LEVEL city       IS (customers.cust_city)
   LEVEL state      IS (customers.cust_state_province)
   LEVEL country    IS (countries.country_id)
   LEVEL subregion  IS (countries.country_subregion)
   LEVEL region     IS (countries.country_region)
   HIERARCHY geog_rollup (
      customer      CHILD OF
      city          CHILD OF
      state         CHILD OF
      country       CHILD OF
      subregion     CHILD OF
      region
   JOIN KEY (customers.country_id) REFERENCES country
   )
   ATTRIBUTE customer_info LEVEL customer DETERMINES
   (cust_first_name, cust_last_name, cust_gender,
    cust_marital_status, cust_year_of_birth,
    cust_income_level, cust_credit_limit)
   ATTRIBUTE country DETERMINES (countries.country_name);
```

**Creating a Dimension with NULL Column Values: Example**

The following example shows how to create the dimension if one of the level columns is null and you want to preserve the hierarchical chain. The example uses the `cust_marital_status` column for simplicity because it is not a `NOT` `NULL` column. If it had such a constraint, then you would have to disable the constraint before using the `SKIP` `WHEN` `NULL` clause.

```md
CREATE DIMENSION customers_dim
   LEVEL customer IS (customers.cust_id)
   LEVEL status IS (customers.cust_marital_status) SKIP WHEN NULL
   LEVEL city IS (customers.cust_city)
   LEVEL state IS (customers.cust_state_province)
   LEVEL country IS (countries.country_id)
   LEVEL subregion IS (countries.country_subregion) SKIP WHEN NULL
   LEVEL region IS (countries.country_region)
   HIERARCHY geog_rollup (
      customer CHILD OF
      city CHILD OF
      state CHILD OF
      country CHILD OF
      subregion CHILD OF
      region
   JOIN KEY (customers.country_id) REFERENCES country
   )
   ATTRIBUTE customer DETERMINES
   (cust_first_name, cust_last_name, cust_gender,
    cust_marital_status, cust_year_of_birth,
    cust_income_level, cust_credit_limit)
   ATTRIBUTE country DETERMINES (countries.country_name)
;
```