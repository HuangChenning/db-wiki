---
title: "MySQL :: MySQL 26.7 Reference Manual :: 7.5.4 Query Attribute Components"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/query-attribute-components.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 7.5.4 Query Attribute Components

A component service provides access to query attributes (see [Section 11.6, “Query Attributes”](query-attributes.md)). The `query_attributes` component uses this service to provide access to query attributes within SQL statements.

- Purpose: Implements the [`mysql_query_attribute_string()`](query-attributes.md) function that takes an attribute name argument and returns the attribute value as a string, or `NULL` if the attribute does not exist.
- URN: `file://component_query_attributes`

Developers who wish to incorporate the same query-attribute component service used by `query_attributes` should consult the `mysql_query_attributes.h` file in a MySQL source distribution.