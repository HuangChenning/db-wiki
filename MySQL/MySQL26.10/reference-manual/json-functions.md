---
title: "MySQL :: MySQL 26.10 Reference Manual :: 14.17 JSON Functions"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/json-functions.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## 14.17 JSON Functions

The functions described in this section perform operations on JSON values. For discussion of the [`JSON`](json.md) data type and additional examples showing how to use these functions, see [Section 13.5, “The JSON Data Type”](json.md).

For functions that take a JSON argument, an error occurs if the argument is not a valid JSON value. Arguments parsed as JSON are indicated by *`json_doc`*; arguments indicated by *`val`* are not parsed.

Functions that return JSON values always perform normalization of these values (see [Normalization, Merging, and Autowrapping of JSON Values](json.md)), and thus orders them. *The precise outcome of the sort is subject to change at any time; do not rely on it to be consistent between releases*.

A set of spatial functions for operating on GeoJSON values is also available. See [Section 14.16.11, “Spatial GeoJSON Functions”](spatial-geojson-functions.md).