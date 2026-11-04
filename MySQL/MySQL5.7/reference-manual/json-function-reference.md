---
title: "12.17.1 JSON Function Reference"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/json-function-reference.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 12.17.1 JSON Function Reference

**Table 12.22 JSON Functions**

| Name | Description | Deprecated |
| --- | --- | --- |
| [`->`](json-search-functions.md) | Return value from JSON column after evaluating path; equivalent to JSON\_EXTRACT(). |  |
| [`->>`](json-search-functions.md) | Return value from JSON column after evaluating path and unquoting the result; equivalent to JSON\_UNQUOTE(JSON\_EXTRACT()). |  |
| [`JSON_APPEND()`](json-modification-functions.md) | Append data to JSON document | Yes |
| [`JSON_ARRAY()`](json-creation-functions.md) | Create JSON array |  |
| [`JSON_ARRAY_APPEND()`](json-modification-functions.md) | Append data to JSON document |  |
| [`JSON_ARRAY_INSERT()`](json-modification-functions.md) | Insert into JSON array |  |
| [`JSON_CONTAINS()`](json-search-functions.md) | Whether JSON document contains specific object at path |  |
| [`JSON_CONTAINS_PATH()`](json-search-functions.md) | Whether JSON document contains any data at path |  |
| [`JSON_DEPTH()`](json-attribute-functions.md) | Maximum depth of JSON document |  |
| [`JSON_EXTRACT()`](json-search-functions.md) | Return data from JSON document |  |
| [`JSON_INSERT()`](json-modification-functions.md) | Insert data into JSON document |  |
| [`JSON_KEYS()`](json-search-functions.md) | Array of keys from JSON document |  |
| [`JSON_LENGTH()`](json-attribute-functions.md) | Number of elements in JSON document |  |
| [`JSON_MERGE()`](json-modification-functions.md) | Merge JSON documents, preserving duplicate keys. Deprecated synonym for JSON\_MERGE\_PRESERVE() | Yes |
| [`JSON_MERGE_PATCH()`](json-modification-functions.md) | Merge JSON documents, replacing values of duplicate keys |  |
| [`JSON_MERGE_PRESERVE()`](json-modification-functions.md) | Merge JSON documents, preserving duplicate keys |  |
| [`JSON_OBJECT()`](json-creation-functions.md) | Create JSON object |  |
| [`JSON_PRETTY()`](json-utility-functions.md) | Print a JSON document in human-readable format |  |
| [`JSON_QUOTE()`](json-creation-functions.md) | Quote JSON document |  |
| [`JSON_REMOVE()`](json-modification-functions.md) | Remove data from JSON document |  |
| [`JSON_REPLACE()`](json-modification-functions.md) | Replace values in JSON document |  |
| [`JSON_SEARCH()`](json-search-functions.md) | Path to value within JSON document |  |
| [`JSON_SET()`](json-modification-functions.md) | Insert data into JSON document |  |
| [`JSON_STORAGE_SIZE()`](json-utility-functions.md) | Space used for storage of binary representation of a JSON document |  |
| [`JSON_TYPE()`](json-attribute-functions.md) | Type of JSON value |  |
| [`JSON_UNQUOTE()`](json-modification-functions.md) | Unquote JSON value |  |
| [`JSON_VALID()`](json-attribute-functions.md) | Whether JSON value is valid |  |

MySQL 5.7.22 and later supports two aggregate JSON functions [`JSON_ARRAYAGG()`](aggregate-functions.md) and [`JSON_OBJECTAGG()`](aggregate-functions.md). See [Section 12.19, “Aggregate Functions”](aggregate-functions-and-modifiers.md), for descriptions of these.

Also beginning with MySQL 5.7.22:

- “pretty-printing” of JSON values in an easy-to-read format can be obtained using the [`JSON_PRETTY()`](json-utility-functions.md) function.
- You can see how much storage space a given JSON value takes up using [`JSON_STORAGE_SIZE()`](json-utility-functions.md).

For complete descriptions of these two functions, see [Section 12.17.6, “JSON Utility Functions”](json-utility-functions.md).