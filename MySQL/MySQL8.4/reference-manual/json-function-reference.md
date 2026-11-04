---
title: "14.17.1 JSON Function Reference"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/json-function-reference.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 14.17.1 JSON Function Reference

**Table 14.22 JSON Functions**

| Name | Description | Deprecated |
| --- | --- | --- |
| [`->`](json-search-functions.md) | Return value from JSON column after evaluating path; equivalent to JSON\_EXTRACT(). |  |
| [`->>`](json-search-functions.md) | Return value from JSON column after evaluating path and unquoting the result; equivalent to JSON\_UNQUOTE(JSON\_EXTRACT()). |  |
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
| [`JSON_OVERLAPS()`](json-search-functions.md) | Compares two JSON documents, returns TRUE (1) if these have any key-value pairs or array elements in common, otherwise FALSE (0) |  |
| [`JSON_PRETTY()`](json-utility-functions.md) | Print a JSON document in human-readable format |  |
| [`JSON_QUOTE()`](json-creation-functions.md) | Quote JSON document |  |
| [`JSON_REMOVE()`](json-modification-functions.md) | Remove data from JSON document |  |
| [`JSON_REPLACE()`](json-modification-functions.md) | Replace values in JSON document |  |
| [`JSON_SCHEMA_VALID()`](json-validation-functions.md) | Validate JSON document against JSON schema; returns TRUE/1 if document validates against schema, or FALSE/0 if it does not |  |
| [`JSON_SCHEMA_VALIDATION_REPORT()`](json-validation-functions.md) | Validate JSON document against JSON schema; returns report in JSON format on outcome on validation including success or failure and reasons for failure |  |
| [`JSON_SEARCH()`](json-search-functions.md) | Path to value within JSON document |  |
| [`JSON_SET()`](json-modification-functions.md) | Insert data into JSON document |  |
| [`JSON_STORAGE_FREE()`](json-utility-functions.md) | Freed space within binary representation of JSON column value following partial update |  |
| [`JSON_STORAGE_SIZE()`](json-utility-functions.md) | Space used for storage of binary representation of a JSON document |  |
| [`JSON_TABLE()`](json-table-functions.md) | Return data from a JSON expression as a relational table |  |
| [`JSON_TYPE()`](json-attribute-functions.md) | Type of JSON value |  |
| [`JSON_UNQUOTE()`](json-modification-functions.md) | Unquote JSON value |  |
| [`JSON_VALID()`](json-attribute-functions.md) | Whether JSON value is valid |  |
| [`JSON_VALUE()`](json-search-functions.md) | Extract value from JSON document at location pointed to by path provided; return this value as VARCHAR(512) or specified type |  |
| [`MEMBER OF()`](json-search-functions.md) | Returns true (1) if first operand matches any element of JSON array passed as second operand, otherwise returns false (0) |  |

MySQL supports two aggregate JSON functions [`JSON_ARRAYAGG()`](aggregate-functions.md) and [`JSON_OBJECTAGG()`](aggregate-functions.md). See [Section 14.19, “Aggregate Functions”](aggregate-functions-and-modifiers.md), for descriptions of these.

MySQL also supports “pretty-printing” of JSON values in an easy-to-read format, using the [`JSON_PRETTY()`](json-utility-functions.md) function. You can see how much storage space a given JSON value takes up, and how much space remains for additional storage, using [`JSON_STORAGE_SIZE()`](json-utility-functions.md) and [`JSON_STORAGE_FREE()`](json-utility-functions.md), respectively. For complete descriptions of these functions, see [Section 14.17.8, “JSON Utility Functions”](json-utility-functions.md).