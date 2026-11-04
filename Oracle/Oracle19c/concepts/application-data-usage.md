---
title: Database Concepts
book: Database Concepts
doc_id: E96138-11
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/application-data-usage.html
tags:
  - oracle
  - 19c
  - concepts
---

## 6 Application Data Usage

- Schema Annotations  
	For many applications, it is important to maintain additional property metadata for database objects such as tables, views, table columns, indexes, and domains.

**Parent topic:** [Oracle Relational Data Structures](oracle-relational-structures.md)

### Schema Annotations

For many applications, it is important to maintain additional property metadata for database objects such as tables, views, table columns, indexes, and domains.

While domains include built-in usage properties such as check constraints, collations, custom sort order, and others, for extensibility the Oracle database also provide the ability to add custom properties via the `ANNOTATIONS` mechanism for database metadata - including table columns, tables, indexes, and more. Applications often need to maintain additional property metadata especially for rendering user interfaces or customizing application logic.

Some examples of column level usage properties can include:
- Display Label: This may be different from the column name (for example, display the title "Salary" from a column named Employee\_Salary)
- Column Group: In many cases, a column "group" is interesting for a user interface (for example, to group Street Number, Street Name, City, and Zip columns into an Address group)
- Format Mask: For example, a display mask of `$99,999.99` can be used by a user interface tool to render 56434 as `$56,434.00`
- Hide: Whether to show the column in the user interface to an end user (for example, don’t show columns with sensitive information or system-added columns to a certain class of end users)
- Highlight: Whether the column should be displayed with a special highlight
- Allowed Operations: Allows the interface to determine whether to allow a column to support sorting, grouping, displaying a list of values, and others.

Table level usage properties can similarly be used to help applications record whether a table contains sensitive information, what its display name should be, which modules in the application it is owned or managed by, and more.

Most applications create their own repositories for this type of usage metadata, resulting in developer complexity and the possibility of divergence across applications, modules, and microservices.

Oracle Database schema annotations are a lightweight declarative facility for developers to centrally register usage properties for database schema objects. Annotations are stored directly inside the database in dictionary tables alongside the data model definition and the data itself, and available to any applications in order to standardize behavior across common data, but are not interpreted by the database in any way. They should be thought of as lightweight standardized markup for database metadata, for use by applications to register and process extended and custom usage properties.