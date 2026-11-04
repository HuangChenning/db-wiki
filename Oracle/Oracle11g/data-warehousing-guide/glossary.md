---
title: Glossary
book: Data Warehousing Guide
doc_id: E25554-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25554/glossary.htm
tags:
  - oracle
  - 11g
  - data-warehousing-guide
---

additive

Describes a fact (or measure) that can be summarized through addition. An additive fact is the most common type of fact. Examples include sales, cost, and profit. Contrast with nonadditive and semi-additive.

advisor

See SQL Access Advisor.

aggregate

Summarized data. For example, unit sales of a particular product could be aggregated by day, month, quarter and yearly sales.

aggregation

The process of consolidating data values into a single value. For example, sales data could be collected on a daily basis and then be aggregated to the week level, the week data could be aggregated to the month level, and so on. The data can then be referred to as aggregate data. The term aggregation is synonymous with summarization, and aggregate data is synonymous with summary data.

ancestor

A value at any level higher than a given value in a hierarchy. For example, in a Time dimension, the value 1999 might be the ancestor of the values Q1-99 and Jan-99.

attribute

A descriptive characteristic of one or more levels. For example, the product dimension for a clothing manufacturer might contain a level called item, one of whose attributes is color. Attributes represent logical groupings that enable end users to select data based on like characteristics.

Note that in relational modeling, an attribute is defined as a characteristic of an entity. In Oracle Database 10g, an attribute is a column in a dimension that characterizes each element of a single level.

cardinality

From an OLTP perspective, this refers to the number of rows in a table. From a data warehousing perspective, this typically refers to the number of distinct values in a column. For most data warehouse DBAs, a more important issue is the degree of cardinality.

change set

A set of logically grouped change data that is transactionally consistent. It contains one or more change tables.

change table

A relational table that contains change data for a single source table. To Change Data Capture subscribers, a change table is known as a publication.

child

A value at the level under a given value in a hierarchy. For example, in a Time dimension, the value Jan-99 might be the child of the value Q1-99. A value can be a child for more than one parent if the child value belongs to multiple hierarchies.

cleansing

The process of resolving inconsistencies and fixing the anomalies in source data, typically as part of the ETL process.

Common Warehouse Metadata (CWM)

A repository standard used by Oracle data warehousing, and decision support. The CWM repository schema is a standalone product that other products can share—each product owns only the objects within the CWM repository that it creates.

cross product

A procedure for combining the elements in multiple sets. For example, given two columns, each element of the first column is matched with every element of the second column. A simple example is illustrated as follows:

```
Col1   Col2   Cross Product
----   ----   -------------
a      c      ac
b      d      ad
              bc
              bd
```

Cross products are performed when grouping sets are concatenated, as described in [Chapter 21, "SQL for Aggregation in Data Warehouses"](aggreg.md).

data mart

A data warehouse that is designed for a particular line of business, such as sales, marketing, or finance. In a dependent data mart, the data can be derived from an enterprise-wide data warehouse. In an independent data mart, data can be collected directly from sources.

data source

A database, application, repository, or file that contributes data to a warehouse.

data warehouse

A relational database that is designed for query and analysis rather than transaction processing. A data warehouse usually contains historical data that is derived from transaction data, but it can include data from other sources. It separates analysis workload from transaction workload and enables a business to consolidate data from several sources.

In addition to a relational database, a data warehouse environment often consists of an ETL solution, an analytical SQL engine, client analysis tools, and other applications that manage the process of gathering data and delivering it to business users.

degree of cardinality

The number of unique values of a column divided by the total number of rows in the table. This is particularly important when deciding which indexes to build. You typically want to use bitmap indexes on low degree of cardinality columns and B-tree indexes on high degree of cardinality columns. As a general rule, a cardinality of under 1% makes a good candidate for a bitmap index.

denormalize

The process of allowing redundancy in a table. Contrast with normalize.

derived fact (or measure)

A fact (or measure) that is generated from existing data using a mathematical operation or a data transformation. Examples include averages, totals, percentages, and differences.

detail

See: fact table.

detail table

See: fact table.

dimension

The term dimension is commonly used in two ways:

dimension table

Dimension tables describe the business entities of an enterprise, represented as hierarchical, categorical information such as time, departments, locations, and products. Dimension tables are sometimes called lookup or reference tables.

dimension value

One element in the list that makes up a dimension. For example, a computer company might have dimension values in the product dimension called LAPPC and DESKPC. Values in the geography dimension might include Boston and Paris. Values in the time dimension might include MAY96 and JAN97.

drill

To navigate from one item to a set of related items. Drilling typically involves navigating up and down through a level (or levels) in a hierarchy. When selecting data, you expand a hierarchy when you drill down in it, and you collapse a hierarchy when you drill up in it.

drill down

To expand the view to include child values that are associated with parent values in the hierarchy.

drill up

To collapse the list of descendant values that are associated with a parent value in the hierarchy.

element

An object or process. For example, a dimension is an object, a mapping is a process, and both are elements.

entity

Entity is used in database modeling. In relational databases, it typically maps to a table.

ETL

ETL stands for extraction, transformation, and loading. ETL refers to the methods involved in accessing and manipulating source data and loading it into a data warehouse. The order in which these processes are performed varies.

Note that ETT (extraction, transformation, transportation) and ETM (extraction, transformation, move) are sometimes used instead of ETL.

extraction

The process of taking data out of a source as part of an initial phase of ETL.

fact

Data, usually numeric and additive, that can be examined and analyzed. Examples include sales, cost, and profit. Fact and measure are synonymous; fact is more commonly used with relational environments, measure is more commonly used with multidimensional environments. A derived fact (or measure) is generated from existing data using a mathematical operation or a data transformation.

fact table

A table in a star schema that contains facts. A fact table typically has two types of columns: those that contain facts and those that are dimension table foreign keys. The primary key of a fact table is usually a composite key that is made up of all of its foreign keys.

A fact table might contain either detail level facts or facts that have been aggregated (fact tables that contain aggregated facts are often instead called summary tables). A fact table usually contains facts with the same level of aggregation.

fast refresh

An operation that applies only the data changes to a materialized view, thus eliminating the need to rebuild the materialized view from scratch.

file-to-table mapping

Maps data from flat files to tables in the warehouse.

hierarchy

A logical structure that uses ordered levels as a means of organizing data. A hierarchy can be used to define data aggregation; for example, in a time dimension, a hierarchy might be used to aggregate data from the Month level to the Quarter level to the Year level. Hierarchies can be defined in Oracle as part of the dimension object. A hierarchy can also be used to define a navigational drill path, regardless of whether the levels in the hierarchy represent aggregated totals.

high boundary

The newest row in a subscription window.

level

A position in a hierarchy. For example, a time dimension might have a hierarchy that represents data at the Month, Quarter, and Year levels.

level value table

A database table that stores the values or data for the levels you created as part of your dimensions and hierarchies.

low boundary

The oldest row in a subscription window.

mapping

The definition of the relationship and data flow between source and target objects.

materialized view

A pre-computed table comprising aggregated or joined data from fact and possibly a dimension table. Also known as a summary or aggregate table.

measure

See fact.

metadata

Data that describes data and other structures, such as objects, business rules, and processes. For example, the schema design of a data warehouse is typically stored in a repository as metadata, which is used to generate scripts used to build and populate the data warehouse. A repository contains metadata.

Examples include: for data, the definition of a source to target transformation that is used to generate and populate the data warehouse; for information, definitions of tables, columns and associations that are stored inside a relational modeling tool; for business rules, discount by 10 percent after selling 1,000 items.

model

An object that represents something to be made. A representative style, plan, or design. A model can also be metadata that defines the structure of the data warehouse.

nonadditive

Describes a fact (or measure) that cannot be summarized through addition. An example includes Average. Contrast with additive and semi-additive.

normalize

In a relational database, the process of removing redundancy in data by separating the data into multiple tables. Contrast with denormalize.

The process of removing redundancy in data by separating the data into multiple tables.

OLTP

See: online transaction processing (OLTP).

online transaction processing (OLTP)

Online transaction processing. OLTP systems are optimized for fast and reliable transaction handling. Compared to data warehouse systems, most OLTP interactions will involve a relatively small number of rows, but a larger group of tables.

parallelism

Breaking down a task so that several processes do part of the work. When multiple CPUs each do their portion simultaneously, very large performance gains are possible.

parallel execution

Breaking down a task so that several processes do part of the work. When multiple CPUs each do their portion simultaneously, very large performance gains are possible.

parent

A value at the level above a given value in a hierarchy. For example, in a Time dimension, the value `Q1-99` might be the parent of the child value `Jan-99`.

partition

Very large tables and indexes can be difficult and time-consuming to work with. To improve manageability, you can break your tables and indexes into smaller pieces called partitions.

pivoting

A transformation where each record in an input stream is converted to many records in the appropriate table in the data warehouse. This is particularly important when taking data from nonrelational databases.

publication

A relational table that contains change data for a single source table. A Change Data Capture publisher refers to a publication as a change table.

publication ID

A publication ID is a unique numeric value that Change Data Capture assigns to each change table defined by a publisher.

publisher

Usually a database administrator who is in charge of creating and maintaining schema objects that make up the Change Data Capture system.

query rewrite

A mechanism to use a materialized view (which is precomputed) to quickly answer queries.

refresh

The mechanism whereby a materialized view is changed to reflect new data.

rewrite

See: query rewrite.

schema

A collection of related database objects. Relational schemas are grouped by database user ID and include tables, views, and other objects. The sample schemas `sh` are used throughout this Guide. Two special types of schema are snowflake schema and star schema.

semi-additive

Describes a fact (or measure) that can be summarized through addition along some, but not all, dimensions. Examples include headcount and on hand stock. Contrast with additive and nonadditive.

slice and dice

This is an informal term referring to data retrieval and manipulation. We can picture a data warehouse as a cube of data, where each axis of the cube represents a dimension. To "slice" the data is to retrieve a piece (a slice) of the cube by specifying measures and values for some or all of the dimensions. When we retrieve a data slice, we may also move and reorder its columns and rows as if we had diced the slice into many small pieces. A system with good slicing and dicing makes it easy to navigate through large amounts of data.

snowflake schema

A type of star schema in which each dimension table is partly or fully normalized.

source

A database, application, file, or other storage facility from which the data in a data warehouse is derived.

source system

A database, application, file, or other storage facility from which the data in a data warehouse is derived.

source tables

The tables in a source database.

SQL Access Advisor

The SQL Access Advisor helps you achieve your performance goals by recommending the proper materialized view set, materialized view logs, partitions, and indexes for a given workload. It is a GUI in Oracle Enterprise Manager, and has similar capabilities to the `DBMS_ADVISOR` package.

staging area

A place where data is processed before entering the warehouse.

staging file

A file used when data is processed before entering the warehouse.

star query

A join between a fact table and a number of dimension tables. Each dimension table is joined to the fact table using a primary key to foreign key join, but the dimension tables are not joined to each other.

star schema

A relational schema whose design represents a multidimensional data model. The star schema consists of one or more fact tables and one or more dimension tables that are related through foreign keys.

subject area

A classification system that represents or distinguishes parts of an organization or areas of knowledge. A data mart is often developed to support a subject area such as sales, marketing, or geography.

subscribers

Consumers of the published change data. These are normally applications.

subscription

A mechanism for Change Data Capture subscribers that controls access to the change data from one or more source tables of interest within a single change set. A subscription contains one or more subscriber views.

subscription window

A mechanism that defines the range of rows in a Change Data Capture publication that the subscriber can currently see in subscriber views.

summary

See: materialized view.

Summary Advisor

Replaced by the SQL Access Advisor.

target

Holds the intermediate or final results of any part of the ETL process. The target of the entire ETL process is the data warehouse.

third normal form (3NF)

A classical relational database modeling technique that minimizes data redundancy through normalization.

third normal form schema

A schema that uses the same kind of normalization as typically found in an OLTP system. Third normal form schemas are sometimes chosen for a large data warehouse, especially an environment with significant data loading requirements that is used to feed a data mart and execute long-running queries. Compare with snowflake schema and star schema.

transformation

The process of manipulating data. Any manipulation beyond copying is a transformation. Examples include cleansing, aggregating, and integrating data from multiple source tables.

transportation

The process of moving copied or transformed data from a source to a data warehouse. Compare with transformation.

unique identifier

An identifier whose purpose is to differentiate between the same item when it appears in more than one place.

update window

The length of time available for updating a warehouse. For example, you might have 8 hours at night to update your warehouse.

update frequency

How often a data warehouse is updated with new information. For example, a warehouse might be updated nightly from an OLTP system.

validation

The process of verifying metadata definitions and configuration parameters.

versioning

The ability to create new versions of a data warehouse project for new requirements and changes.