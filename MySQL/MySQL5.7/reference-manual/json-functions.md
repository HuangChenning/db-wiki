---
title: "12.17 JSON Functions"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/json-functions.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

The functions described in this section perform operations on JSON values. For discussion of the [`JSON`](json.md) data type and additional examples showing how to use these functions, see [Section 11.5, “The JSON Data Type”](json.md).

For functions that take a JSON argument, an error occurs if the argument is not a valid JSON value. Arguments parsed as JSON are indicated by *`json_doc`*; arguments indicated by *`val`* are not parsed.

Functions that return JSON values always perform normalization of these values (see [Normalization, Merging, and Autowrapping of JSON Values](json.md)), and thus orders them. *The precise outcome of the sort is subject to change at any time; do not rely on it to be consistent between releases*.

Unless otherwise indicated, the JSON functions were added in MySQL 5.7.8.

A set of spatial functions for operating on GeoJSON values is also available. See [Section 12.16.11, “Spatial GeoJSON Functions”](spatial-geojson-functions.md).