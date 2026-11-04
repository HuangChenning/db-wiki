---
title: "14.23 Internal Functions"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/internal-functions.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

**Table 14.33 Internal Functions**

| Name | Description |
| --- | --- |
| `CAN_ACCESS_COLUMN()` | Internal use only |
| `CAN_ACCESS_DATABASE()` | Internal use only |
| `CAN_ACCESS_TABLE()` | Internal use only |
| `CAN_ACCESS_USER()` | Internal use only |
| `CAN_ACCESS_VIEW()` | Internal use only |
| `GET_DD_COLUMN_PRIVILEGES()` | Internal use only |
| `GET_DD_CREATE_OPTIONS()` | Internal use only |
| `GET_DD_INDEX_SUB_PART_LENGTH()` | Internal use only |
| `INTERNAL_AUTO_INCREMENT()` | Internal use only |
| `INTERNAL_AVG_ROW_LENGTH()` | Internal use only |
| `INTERNAL_CHECK_TIME()` | Internal use only |
| `INTERNAL_CHECKSUM()` | Internal use only |
| `INTERNAL_DATA_FREE()` | Internal use only |
| `INTERNAL_DATA_LENGTH()` | Internal use only |
| `INTERNAL_DD_CHAR_LENGTH()` | Internal use only |
| `INTERNAL_GET_COMMENT_OR_ERROR()` | Internal use only |
| `INTERNAL_GET_ENABLED_ROLE_JSON()` | Internal use only |
| `INTERNAL_GET_HOSTNAME()` | Internal use only |
| `INTERNAL_GET_USERNAME()` | Internal use only |
| `INTERNAL_GET_VIEW_WARNING_OR_ERROR()` | Internal use only |
| `INTERNAL_INDEX_COLUMN_CARDINALITY()` | Internal use only |
| `INTERNAL_INDEX_LENGTH()` | Internal use only |
| `INTERNAL_IS_ENABLED_ROLE()` | Internal use only |
| `INTERNAL_IS_MANDATORY_ROLE()` | Internal use only |
| `INTERNAL_KEYS_DISABLED()` | Internal use only |
| `INTERNAL_MAX_DATA_LENGTH()` | Internal use only |
| `INTERNAL_TABLE_ROWS()` | Internal use only |
| `INTERNAL_UPDATE_TIME()` | Internal use only |

The functions listed in this section are intended only for internal use by the server. Attempts by users to invoke them result in an error.