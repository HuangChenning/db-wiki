---
title: "7.5.4 Query Attribute Components"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/query-attribute-components.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 7.5.4 Query Attribute Components

A component service provides access to query attributes (see [Section 11.6, “Query Attributes”](query-attributes.md)). The `query_attributes` component uses this service to provide access to query attributes within SQL statements.

- Purpose: Implements the [`mysql_query_attribute_string()`](query-attributes.md) function that takes an attribute name argument and returns the attribute value as a string, or `NULL` if the attribute does not exist.
- URN: `file://component_query_attributes`

Developers who wish to incorporate the same query-attribute component service used by `query_attributes` should consult the `mysql_query_attributes.h` file in a MySQL source distribution.