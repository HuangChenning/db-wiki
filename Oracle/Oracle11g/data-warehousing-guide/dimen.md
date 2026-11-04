---
title: Dimensions
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/dimen.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

## 11 Dimensions

This chapter discusses using dimensions in a data warehouse: It contains the following topics:

## What are Dimensions?

A [dimension](glossary.md) is a structure that categorizes data in order to enable users to answer business questions. Commonly used dimensions are customers, products, and time. For example, each sales channel of a clothing retailer might gather and store data regarding sales and reclamations of their Cloth assortment. The retail chain management can build a data warehouse to analyze the sales of its products across all stores over time and help answer questions such as:

- What is the effect of promoting one product on the sale of a related product that is not promoted?
- What are the sales of a product before and after a promotion?
- How does a promotion affect the various distribution channels?

The data in the retailer's data warehouse system has two important components: dimensions and facts. The dimensions are products, customers, promotions, channels, and time. One approach for identifying your dimensions is to review your reference tables, such as a product table that contains everything about a product, or a promotion table containing all information about promotions. The facts are sales (units sold) and profits. A data warehouse contains facts about the sales of each product at on a daily basis.

A typical relational implementation for such a data warehouse is a star schema. The fact information is stored in what is called a fact table, whereas the dimensional information is stored in dimension tables. In our example, each sales transaction record is uniquely defined as for each customer, for each product, for each sales channel, for each promotion, and for each day (time).

See Also:

[Chapter 20, "Schema Modeling Techniques"](schemas.md) for further details

In Oracle Database, the dimensional information itself is stored in a dimension table. In addition, the database object dimension helps to organize and group dimensional information into hierarchies. This represents natural `1:n` relationships between columns or column groups (the levels of a hierarchy) that cannot be represented with constraint conditions. Going up a level in the hierarchy is called rolling up the data and going down a level in the hierarchy is called drilling down the data. In the retailer example:

- Within the `time` dimension, months roll up to quarters, quarters roll up to years, and years roll up to all years.
- Within the `product` dimension, products roll up to subcategories, subcategories roll up to categories, and categories roll up to all products.
- Within the `customer` dimension, customers roll up to `city`. Then cities roll up to `state`. Then states roll up to `country`. Then countries roll up to `subregion`. Finally, subregions roll up to `region`, as shown in Figure 11-1.

Figure 11-1 Sample Rollup for a Customer Dimension

![Description of Figure 11-1 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg072.gif)  
[Description of "Figure 11-1 Sample Rollup for a Customer Dimension"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg072.htm)  

Data analysis typically starts at higher levels in the dimensional hierarchy and gradually drills down if the situation warrants such analysis.

Dimensions do not have to be defined. However, if your application uses dimensional modeling, it is worth spending time creating them as it can yield significant benefits, because they help query rewrite perform more complex types of rewrite. Dimensions are also beneficial to certain types of materialized view refresh operations and with the SQL Access Advisor. They are only mandatory if you use the SQL Access Advisor (a GUI tool for materialized view and index management) without a workload to recommend which materialized views and indexes to create, drop, or retain.

See Also:

- [Chapter 18, "Basic Query Rewrite"](qrbasic.md) for further details regarding query rewrite
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/advisor.htm#PFGRF008) for further details regarding the SQL Access Advisor

In spite of the benefits of dimensions, you must not create dimensions in any schema that does not fully satisfy the dimensional relationships described in this chapter. Incorrect results can be returned from queries otherwise.

## Creating Dimensions

Before you can create a dimension object, the dimension tables must exist in the database possibly containing the dimension data. For example, if you create a customer dimension, one or more tables must exist that contain the city, state, and country information. In a star schema data warehouse, these dimension tables already exist. It is therefore a simple task to identify which ones will be used.

Now you can draw the hierarchies of a dimension as shown in Figure 11-1. For example, `city` is a child of `state` (because you can aggregate city-level data up to state), and `country`. This hierarchical information will be stored in the database object dimension.

In the case of normalized or partially normalized dimension representation (a dimension that is stored in more than one table), identify how these tables are joined. Note whether the joins between the dimension tables can guarantee that each child-side row joins with one and only one parent-side row. In the case of denormalized dimensions, determine whether the child-side columns uniquely determine the parent-side (or attribute) columns. If you use constraints to represent these relationships, they can be enabled with the `NOVALIDATE` and `RELY` clauses if the relationships represented by the constraints are guaranteed by other means.

You may want the capability to skip `NULL` levels in a dimension. An example of this is with Puerto Rico. You may want Puerto Rico to be included within a region of North America, but not include it within the state category. If you want this capability, use the `SKIP` `WHEN` `NULL` clause. See the sample dimension later in this section for more information and [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for syntax and restrictions.

You create a dimension using either the `CREATE` `DIMENSION` statement or the Dimension Wizard in Oracle Enterprise Manager. Within the `CREATE` `DIMENSION` statement, use the `LEVEL` clause to identify the names of the dimension levels.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5006.htm#SQLRF01206) for a complete description of the `CREATE` `DIMENSION` statement

This customer dimension contains a single hierarchy with a geographical rollup, with arrows drawn from the child level to the parent level, as shown in Figure 11-1.

Each arrow in this graph indicates that for any child there is one and only one parent. For example, each city must be contained in exactly one state and each state must be contained in exactly one country. States that belong to more than one country violate hierarchical integrity. Also, you must use the `SKIP` `WHEN` `NULL` clause if you want to include cities that do not belong to a state, such as Washington D.C. Hierarchical integrity is necessary for the correct operation of management functions for materialized views that include aggregates.

For example, you can declare a dimension `products_dim`, which contains levels `product`, `subcategory`, and `category`:

```
CREATE DIMENSION products_dim
       LEVEL product           IS (products.prod_id)
       LEVEL subcategory       IS (products.prod_subcategory)
       LEVEL category          IS (products.prod_category) ...
```

Each level in the dimension must correspond to one or more columns in a table in the database. Thus, level `product` is identified by the column `prod_id` in the products table and level `subcategory` is identified by a column called `prod_subcategory` in the same table.

In this example, the database tables are denormalized and all the columns exist in the same table. However, this is not a prerequisite for creating dimensions. "Using Normalized Dimension Tables" shows how to create a dimension `customers_dim` that has a normalized schema design using the `JOIN` `KEY` clause.

The next step is to declare the relationship between the levels with the `HIERARCHY` statement and give that hierarchy a name. A hierarchical relationship is a functional dependency from one level of a hierarchy to the next level in the hierarchy. Using the level names defined previously, the `CHILD` `OF` relationship denotes that each child's level value is associated with one and only one parent level value. The following statement declares a hierarchy `prod_rollup` and defines the relationship between products, subcategory, and category:

```
HIERARCHY prod_rollup 
 (product         CHILD OF
  subcategory     CHILD OF
  category)
```

In addition to the `1:n` hierarchical relationships, dimensions also include `1:1` attribute relationships between the hierarchy levels and their dependent, determined dimension attributes. For example, the dimension `times_dim`, as defined in [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm), has columns `fiscal_month_desc`, `fiscal_month_name`, and `days_in_fiscal_month`. Their relationship is defined as follows:

```
LEVEL fis_month IS TIMES.FISCAL_MONTH_DESC
...
ATTRIBUTE fis_month DETERMINES
      (fiscal_month_name, days_in_fiscal_month)
```

The `ATTRIBUTE`... `DETERMINES` clause relates `fis_month` to `fiscal_month_name and days_in_fiscal_month`. Note that this is a unidirectional determination. It is only guaranteed, that for a specific `fiscal_month`, for example, `1999-11`, you will find exactly one matching values for `fiscal_month_name`, for example, `November` and `days_in_fiscal_month`, for example, 28. You cannot determine a specific `fiscal_month_desc` based on the `fiscal_month_name`, which is `November` for every fiscal year.

In this example, suppose a query were issued that queried by `fiscal_month_name` instead of `fiscal_month_desc`. Because this `1:1` relationship exists between the attribute and the level, an already aggregated materialized view containing `fiscal_month_desc` can be joined back to the dimension information and used to identify the data.

See Also:

[Chapter 18, "Basic Query Rewrite"](qrbasic.md) for further details of using dimensional information

A sample dimension definition follows:

```
CREATE DIMENSION products_dim
    LEVEL product           IS (products.prod_id)
    LEVEL subcategory       IS (products.prod_subcategory) [SKIP WHEN NULL]
    LEVEL category          IS (products.prod_category)
    HIERARCHY prod_rollup (
         product         CHILD OF
         subcategory     CHILD OF
         category)
    ATTRIBUTE product DETERMINES
     (products.prod_name, products.prod_desc,
      prod_weight_class, prod_unit_of_measure,
      prod_pack_size, prod_status, prod_list_price, prod_min_price)
    ATTRIBUTE subcategory DETERMINES
     (prod_subcategory, prod_subcategory_desc)
    ATTRIBUTE category DETERMINES
     (prod_category, prod_category_desc);
```

Alternatively, the `extended_attribute_clause` could have been used instead of the `attribute_clause`, as shown in the following example:

```
CREATE DIMENSION products_dim
    LEVEL product           IS (products.prod_id)
    LEVEL subcategory       IS (products.prod_subcategory)
    LEVEL category          IS (products.prod_category)
    HIERARCHY prod_rollup (
         product         CHILD OF
         subcategory     CHILD OF
         category
        )
    ATTRIBUTE product_info LEVEL product DETERMINES
     (products.prod_name, products.prod_desc,
      prod_weight_class, prod_unit_of_measure,
      prod_pack_size, prod_status, prod_list_price, prod_min_price)
    ATTRIBUTE subcategory DETERMINES
     (prod_subcategory, prod_subcategory_desc)
    ATTRIBUTE category DETERMINES
     (prod_category, prod_category_desc);
```

The design, creation, and maintenance of dimensions is part of the design, creation, and maintenance of your data warehouse schema. Once the dimension has been created, verify that it meets these requirements:

- There must be a `1:n` relationship between a parent and children. A parent can have one or more children, but a child can have only one parent.
- There must be a `1:1` attribute relationship between hierarchy levels and their dependent dimension attributes. For example, if there is a column `fiscal_month_desc`, then a possible attribute relationship would be `fiscal_month_desc` to `fiscal_month_name`. For skip `NULL` levels, if a row of the relation of a skip level has a `NULL` value for the level column, then that row must have a `NULL` value for the attribute-relationship column, too.
- If the columns of a parent level and child level are in different relations, then the connection between them also requires a `1:n` join relationship. Each row of the child table must join with one and only one row of the parent table unless you use the `SKIP` `WHEN` `NULL` clause. This relationship is stronger than referential integrity alone, because it requires that the child join key must be non-null, that referential integrity must be maintained from the child join key to the parent join key, and that the parent join key must be unique.
- You must ensure (using database constraints if necessary) that the columns of each hierarchy level are non-null unless you use the `SKIP` `WHEN` `NULL` clause and that hierarchical integrity is maintained.
- An optional join key is a join key that connects the immediate non-skip child (if such a level exists), `CHILDLEV`, of a skip level to the nearest non-skip ancestor (again, if such a level exists), `ANCLEV`, of the skip level in the hierarchy. Also, this joinkey is allowed only when `CHILDLEV` and `ANCLEV` are defined over different relations.
- The hierarchies of a dimension can overlap or be disconnected from each other. However, the columns of a hierarchy level cannot be associated with more than one dimension.
- Join relationships that form cycles in the dimension graph are not supported. For example, a hierarchy level cannot be joined to itself either directly or indirectly.
	Note:
	The information stored with a dimension objects is only declarative. The previously discussed relationships are not enforced with the creation of a dimension object. You should validate any dimension definition with the `DBMS_DIMENSION.VALIDATE_DIMENSION` procedure, as discussed in "Validating Dimensions".

### Dropping and Creating Attributes with Columns

You can use the attribute clause in a `CREATE` `DIMENSION` statement to specify one or multiple columns that are uniquely determined by a hierarchy level.

If you use the `extended_attribute_clause` to create multiple columns determined by a hierarchy level, you can drop one attribute column without dropping them all. Alternatively, you can specify an attribute name for each attribute clause `CREATE` or `ALTER` `DIMENSION` statement so that an attribute name is specified for each attribute clause where multiple level-to-column relationships can be individually specified.

The following statement illustrates how you can drop a single column without dropping all columns:

```
CREATE DIMENSION products_dim
LEVEL product         IS (products.prod_id)
LEVEL subcategory     IS (products.prod_subcategory)
LEVEL category        IS (products.prod_category)
HIERARCHY prod_rollup (
          product        CHILD OF
          subcategory    CHILD OF category)
ATTRIBUTE product DETERMINES
         (products.prod_name, products.prod_desc,
          prod_weight_class, prod_unit_of_measure,
          prod_pack_size,prod_status, prod_list_price, prod_min_price)
ATTRIBUTE subcategory_att DETERMINES
         (prod_subcategory, prod_subcategory_desc)
ATTRIBUTE category DETERMINES
         (prod_category, prod_category_desc);

ALTER DIMENSION products_dim
DROP ATTRIBUTE subcategory_att LEVEL subcategory COLUMN prod_subcategory;
```

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_5006.htm#SQLRF01206) for a complete description of the `CREATE` `DIMENSION` statement

### Multiple Hierarchies

A single dimension definition can contain multiple hierarchies. Suppose our retailer wants to track the sales of certain items over time. The first step is to define the time dimension over which sales will be tracked. Figure 11-2 illustrates a dimension `times_dim` with two time hierarchies.

Figure 11-2 times\_dim Dimension with Two Time Hierarchies

![Description of Figure 11-2 follows](https://docs.oracle.com/cd/E11882_01/server.112/e25554/dwhsg075.gif)  
[Description of "Figure 11-2 times\_dim Dimension with Two Time Hierarchies"](https://docs.oracle.com/cd/E11882_01/server.112/e25554/img_text/dwhsg075.htm)  

From the illustration, you can construct the hierarchy of the denormalized `time_dim` dimension's `CREATE` `DIMENSION` statement as follows. The complete `CREATE` `DIMENSION` statement as well as the `CREATE` `TABLE` statement are shown in [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm).

```
CREATE DIMENSION times_dim
   LEVEL day         IS times.time_id
   LEVEL month       IS times.calendar_month_desc
   LEVEL quarter     IS times.calendar_quarter_desc
   LEVEL year        IS times.calendar_year
   LEVEL fis_week    IS times.week_ending_day
   LEVEL fis_month   IS times.fiscal_month_desc
   LEVEL fis_quarter IS times.fiscal_quarter_desc
   LEVEL fis_year    IS times.fiscal_year
   HIERARCHY cal_rollup    (
             day     CHILD OF
             month   CHILD OF
             quarter CHILD OF
             year
   )
   HIERARCHY fis_rollup    (
             day         CHILD OF
             fis_week    CHILD OF
             fis_month   CHILD OF
             fis_quarter CHILD OF
             fis_year
   ) <attribute determination clauses>;
```

### Using Normalized Dimension Tables

The tables used to define a dimension may be normalized or denormalized and the individual hierarchies can be normalized or denormalized. If the levels of a hierarchy come from the same table, it is called a fully denormalized hierarchy. For example, `cal_rollup` in the `times_dim` dimension is a denormalized hierarchy. If levels of a hierarchy come from different tables, such a hierarchy is either a fully or partially normalized hierarchy. This section shows how to define a normalized hierarchy.

Suppose the tracking of a customer's location is done by city, state, and country. This data is stored in the tables customers and countries. The customer dimension `customers_dim` is partially normalized because the data entities `cust_id` and `country_id` are taken from different tables. The clause `JOIN` `KEY` within the dimension definition specifies how to join together the levels in the hierarchy. The dimension statement is partially shown in the following. The complete `CREATE` `DIMENSION` statement as well as the `CREATE` `TABLE` statement are shown in [Oracle Database Sample Schemas](https://docs.oracle.com/cd/E11882_01/server.112/e10831/toc.htm).

```
CREATE DIMENSION customers_dim
   LEVEL customer  IS (customers.cust_id)
   LEVEL city      IS (customers.cust_city)
   LEVEL state     IS (customers.cust_state_province)
   LEVEL country   IS (countries.country_id)
   LEVEL subregion IS (countries.country_subregion)
   LEVEL region IS (countries.country_region)
   HIERARCHY geog_rollup (
      customer        CHILD OF
      city            CHILD OF
      state           CHILD OF
      country         CHILD OF
      subregion       CHILD OF
      region
   JOIN KEY (customers.country_id) REFERENCES country);
```

If you use the `SKIP` `WHEN` `NULL` clause, you can use the `JOIN` `KEY` clause to link levels that have a missing level in their hierarchy. For example, the following statement enables a state level that has been declared as `SKIP` `WHEN` `NULL` to join city and country:

```
JOIN KEY (city.country_id) REFERENCES country;
```

This ensures that the rows at customer and city levels can still be associated with the rows of country, subregion, and region levels.

## Viewing Dimensions

Dimensions can be viewed through one of two methods:

- Using Oracle Enterprise Manager
- Using the DESCRIBE\_DIMENSION Procedure

### Using Oracle Enterprise Manager

All of the dimensions that exist in the data warehouse can be viewed using Oracle Enterprise Manager. Select the Dimension object from within the Schema icon to display all of the dimensions. Select a specific dimension to graphically display its hierarchy, levels, and any attributes that have been defined.

### Using the DESCRIBE\_DIMENSION Procedure

To view the definition of a dimension, use the `DESCRIBE_DIMENSION` procedure in the `DBMS_DIMENSION` package. For example, if a dimension is created in the `sh` sample schema with the following statements:

```
CREATE DIMENSION channels_dim
        LEVEL channel       IS (channels.channel_id)
        LEVEL channel_class IS (channels.channel_class)
        HIERARCHY channel_rollup (
                channel CHILD OF channel_class)
        ATTRIBUTE channel DETERMINES (channel_desc)
        ATTRIBUTE channel_class DETERMINES (channel_class);
```

Execute the `DESCRIBE_DIMENSION` procedure as follows:

```
SET SERVEROUTPUT ON FORMAT WRAPPED;  --to improve the display of info
EXECUTE DBMS_DIMENSION.DESCRIBE_DIMENSION('SH.CHANNELS_DIM');
```

You then see the following output results:

```
EXECUTE DBMS_DIMENSION.DESCRIBE_DIMENSION('SH.CHANNELS_DIM'); 
  DIMENSION SH.CHANNELS_DIM 
    LEVEL CHANNEL IS SH.CHANNELS.CHANNEL_ID 
    LEVEL CHANNEL_CLASS IS SH.CHANNELS.CHANNEL_CLASS 

    HIERARCHY CHANNEL_ROLLUP ( 
             CHANNEL CHILD OF 
             CHANNEL_CLASS) 

    ATTRIBUTE CHANNEL LEVEL CHANNEL DETERMINES
SH.CHANNELS.CHANNEL_DESC 
    ATTRIBUTE CHANNEL_CLASS LEVEL CHANNEL_CLASS DETERMINES
SH.CHANNELS.CHANNEL_CLASS
```

## Using Dimensions with Constraints

Constraints play an important role with dimensions. Full referential integrity is sometimes enabled in data warehouses, but not always. This is because operational databases normally have full referential integrity and you can ensure that the data flowing into your data warehouse never violates the already established integrity rules.

It is recommended that constraints be enabled and, if validation time is a concern, then the `NOVALIDATE` clause should be used as follows:

```
ENABLE NOVALIDATE CONSTRAINT pk_time;
```

Primary and foreign keys should be implemented also. Referential integrity constraints and `NOT` `NULL` constraints on the fact tables provide information that query rewrite can use to extend the usefulness of materialized views.

In addition, you should use the `RELY` clause to inform query rewrite that it can rely upon the constraints being correct as follows:

```
ALTER TABLE time MODIFY CONSTRAINT pk_time RELY;
```

This information is also used for query rewrite. See [Chapter 18, "Basic Query Rewrite"](qrbasic.md) for more information.

If you use the `SKIP` `WHEN` `NULL` clause, at least one of the referenced level columns should not have `NOT` `NULL` constraints.

## Validating Dimensions

The information of a dimension object is declarative only and not enforced by the database. If the relationships described by the dimensions are incorrect, incorrect results could occur. Therefore, you should verify the relationships specified by `CREATE` `DIMENSION` using the `DBMS_DIMENSION.VALIDATE_DIMENSION` procedure periodically.

This procedure is easy to use and has only four parameters:

- `dimension`: the owner and name.
- `incremental`: set to `TRUE` to check only the new rows for tables of this dimension.
- `check_nulls`: set to `TRUE` to verify that all columns that are not in the levels containing a `SKIP` `WHEN` `NULL` clause are not null.
- `statement_id`: a user-supplied unique identifier to identify the result of each run of the procedure.

The following example validates the dimension `TIME_FN` in the `sh` schema:

```
@utldim.sql 
EXECUTE DBMS_DIMENSION.VALIDATE_DIMENSION ('SH.TIME_FN', FALSE, TRUE, 
  'my first example');
```

Before running the `VALIDATE_DIMENSION` procedure, you need to create a local table, `DIMENSION_EXCEPTIONS`, by running the provided script `utldim.sql`. If the `VALIDATE_DIMENSION` procedure encounters any errors, they are placed in this table. Querying this table will identify the exceptions that were found. The following illustrates a sample:

```
SELECT * FROM dimension_exceptions
WHERE statement_id = 'my first example';

STATEMENT_ID       OWNER  TABLE_NAME  DIMENSION_NAME   RELATIONSHIP   BAD_ROWID
------------       -----  ----------  --------------   ------------   ---------
my first example   SH     MONTH       TIME_FN          FOREIGN KEY    AAAAuwAAJAAAARwAAA
```

However, rather than query this table, it may be better to query the rowid of the invalid row to retrieve the actual row that has violated the constraint. In this example, the dimension `TIME_FN` is checking a table called `month`. It has found a row that violates the constraints. Using the rowid, you can see exactly which row in the month table is causing the problem, as in the following:

```
SELECT * FROM month
WHERE rowid IN (SELECT bad_rowid
                FROM dimension_exceptions
                WHERE statement_id = 'my first example');

MONTH    QUARTER   FISCAL_QTR    YEAR    FULL_MONTH_NAME    MONTH_NUMB
------   -------   ----------    ----    ---------------    ----------
199903     19981        19981    1998              March             3
```

## Altering Dimensions

You can modify a dimension using the `ALTER` `DIMENSION` statement. You can add or drop a level, hierarchy, or attribute from the dimension using this command.

Referring to the time dimension in Figure 11-2, you can remove the attribute `fis_year`, drop the hierarchy `fis_rollup`, or remove the level `fiscal_year`. In addition, you can add a new level called `f_year` as in the following:

```
ALTER DIMENSION times_dim DROP ATTRIBUTE fis_year;
ALTER DIMENSION times_dim DROP HIERARCHY fis_rollup;
ALTER DIMENSION times_dim DROP LEVEL fis_year;
ALTER DIMENSION times_dim ADD LEVEL f_year IS times.fiscal_year;
```

If you used the `extended_attribute_clause` when creating the dimension, you can drop one attribute column without dropping all attribute columns. This is illustrated in "Dropping and Creating Attributes with Columns", which shows the following statement:

```
ALTER DIMENSION product_dim 
DROP ATTRIBUTE size LEVEL prod_type COLUMN Prod_TypeSize;
```

If you try to remove anything with further dependencies inside the dimension, Oracle Database rejects the altering of the dimension. A dimension becomes invalid if you change any schema object that the dimension is referencing. For example, if the table on which the dimension is defined is altered, the dimension becomes invalid.

You can modify a dimension by adding a level containing a `SKIP` `WHEN` `NULL` clause, as in the following statement:

```
ALTER DIMENSION times_dim
ADD LEVEL f_year IS times.fiscal_year SKIP WHEN NULL;
```

You cannot, however, modify a level that contains a `SKIP` `WHEN` `NULL` clause. Instead, you need to drop the level and re-create it.

To check the status of a dimension, view the contents of the column `invalid` in the `ALL_DIMENSIONS` data dictionary view. To revalidate the dimension, use the `COMPILE` option as follows:

```
ALTER DIMENSION times_dim COMPILE;
```

Dimensions can also be modified or deleted using Oracle Enterprise Manager.

## Deleting Dimensions

A dimension is removed using the `DROP` `DIMENSION` statement. For example, you could issue the following statement:

```
DROP DIMENSION times_dim;
```