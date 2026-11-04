---
title: "14.1 Built-In Function and Operator Reference"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/built-in-function-reference.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

The following table lists each built-in (native) function and operator and provides a short description of each one. For a table listing functions that are loadable at runtime, see [Section 14.2, “Loadable Function Reference”](loadable-function-reference.md).

**Table 14.1 Built-In Functions and Operators**

| Name | Description | Deprecated |
| --- | --- | --- |
| [`&`](bit-functions.md) | Bitwise AND |  |
| [`>`](comparison-operators.md) | Greater than operator |  |
| [`>>`](bit-functions.md) | Right shift |  |
| [`>=`](comparison-operators.md) | Greater than or equal operator |  |
| [`<`](comparison-operators.md) | Less than operator |  |
| [`<>`, `!=`](comparison-operators.md) | Not equal operator |  |
| [`<<`](bit-functions.md) | Left shift |  |
| [`<=`](comparison-operators.md) | Less than or equal operator |  |
| [`<=>`](comparison-operators.md) | NULL-safe equal to operator |  |
| [`%`, `MOD`](arithmetic-functions.md) | Modulo operator |  |
| [`*`](arithmetic-functions.md) | Multiplication operator |  |
| [`+`](arithmetic-functions.md) | Addition operator |  |
| [`-`](arithmetic-functions.md) | Minus operator |  |
| [`-`](arithmetic-functions.md) | Change the sign of the argument |  |
| [`->`](json-search-functions.md) | Return value from JSON column after evaluating path; equivalent to JSON\_EXTRACT(). |  |
| [`->>`](json-search-functions.md) | Return value from JSON column after evaluating path and unquoting the result; equivalent to JSON\_UNQUOTE(JSON\_EXTRACT()). |  |
| [`/`](arithmetic-functions.md) | Division operator |  |
| [`:=`](assignment-operators.md) | Assign a value |  |
| [`=`](assignment-operators.md) | Assign a value (as part of a [`SET`](set-variable.md) statement, or as part of the `SET` clause in an [`UPDATE`](update.md) statement) |  |
| [`=`](comparison-operators.md) | Equal operator |  |
| [`^`](bit-functions.md) | Bitwise XOR |  |
| [`ABS()`](mathematical-functions.md) | Return the absolute value |  |
| [`ACOS()`](mathematical-functions.md) | Return the arc cosine |  |
| [`ADDDATE()`](date-and-time-functions.md) | Add time values (intervals) to a date value |  |
| [`ADDTIME()`](date-and-time-functions.md) | Add time |  |
| [`AES_DECRYPT()`](encryption-functions.md) | Decrypt using AES |  |
| [`AES_ENCRYPT()`](encryption-functions.md) | Encrypt using AES |  |
| [`AND`, `&&`](logical-operators.md) | Logical AND |  |
| [`ANY_VALUE()`](miscellaneous-functions.md) | Suppress ONLY\_FULL\_GROUP\_BY value rejection |  |
| [`ASCII()`](string-functions.md) | Return numeric value of left-most character |  |
| [`ASIN()`](mathematical-functions.md) | Return the arc sine |  |
| [`asynchronous_connection_failover_add_managed()`](replication-functions-async-failover.md) | Add group member source server configuration information to a replication channel source list |  |
| [`asynchronous_connection_failover_add_source()`](replication-functions-async-failover.md) | Add source server configuration information server to a replication channel source list |  |
| [`asynchronous_connection_failover_delete_managed()`](replication-functions-async-failover.md) | Remove a managed group from a replication channel source list |  |
| [`asynchronous_connection_failover_delete_source()`](replication-functions-async-failover.md) | Remove a source server from a replication channel source list |  |
| [`asynchronous_connection_failover_reset()`](replication-functions-async-failover.md) | Remove all settings relating to group replication asynchronous failover |  |
| [`ATAN()`](mathematical-functions.md) | Return the arc tangent |  |
| [`ATAN2()`, `ATAN()`](mathematical-functions.md) | Return the arc tangent of the two arguments |  |
| [`AVG()`](aggregate-functions.md) | Return the average value of the argument |  |
| [`BENCHMARK()`](information-functions.md) | Repeatedly execute an expression |  |
| [`BETWEEN ... AND ...`](comparison-operators.md) | Whether a value is within a range of values |  |
| [`BIN()`](string-functions.md) | Return a string containing binary representation of a number |  |
| [`BIN_TO_UUID()`](miscellaneous-functions.md) | Convert binary UUID to string |  |
| [`BINARY`](cast-functions.md) | Cast a string to a binary string | Yes |
| [`BIT_AND()`](aggregate-functions.md) | Return bitwise AND |  |
| [`BIT_COUNT()`](bit-functions.md) | Return the number of bits that are set |  |
| [`BIT_LENGTH()`](string-functions.md) | Return length of argument in bits |  |
| [`BIT_OR()`](aggregate-functions.md) | Return bitwise OR |  |
| [`BIT_XOR()`](aggregate-functions.md) | Return bitwise XOR |  |
| [`CAN_ACCESS_COLUMN()`](internal-functions.md) | Internal use only |  |
| [`CAN_ACCESS_DATABASE()`](internal-functions.md) | Internal use only |  |
| [`CAN_ACCESS_TABLE()`](internal-functions.md) | Internal use only |  |
| [`CAN_ACCESS_USER()`](internal-functions.md) | Internal use only |  |
| [`CAN_ACCESS_VIEW()`](internal-functions.md) | Internal use only |  |
| [`CASE`](flow-control-functions.md) | Case operator |  |
| [`CAST()`](cast-functions.md) | Cast a value as a certain type |  |
| [`CEIL()`](mathematical-functions.md) | Return the smallest integer value not less than the argument |  |
| [`CEILING()`](mathematical-functions.md) | Return the smallest integer value not less than the argument |  |
| [`CHAR()`](string-functions.md) | Return the character for each integer passed |  |
| [`CHAR_LENGTH()`](string-functions.md) | Return number of characters in argument |  |
| [`CHARACTER_LENGTH()`](string-functions.md) | Synonym for CHAR\_LENGTH() |  |
| [`CHARSET()`](information-functions.md) | Return the character set of the argument |  |
| [`COALESCE()`](comparison-operators.md) | Return the first non-NULL argument |  |
| [`COERCIBILITY()`](information-functions.md) | Return the collation coercibility value of the string argument |  |
| [`COLLATION()`](information-functions.md) | Return the collation of the string argument |  |
| [`COMPRESS()`](encryption-functions.md) | Return result as a binary string |  |
| [`CONCAT()`](string-functions.md) | Return concatenated string |  |
| [`CONCAT_WS()`](string-functions.md) | Return concatenate with separator |  |
| [`CONNECTION_ID()`](information-functions.md) | Return the connection ID (thread ID) for the connection |  |
| [`CONV()`](mathematical-functions.md) | Convert numbers between different number bases |  |
| [`CONVERT()`](cast-functions.md) | Cast a value as a certain type |  |
| [`CONVERT_TZ()`](date-and-time-functions.md) | Convert from one time zone to another |  |
| [`COS()`](mathematical-functions.md) | Return the cosine |  |
| [`COT()`](mathematical-functions.md) | Return the cotangent |  |
| [`COUNT()`](aggregate-functions.md) | Return a count of the number of rows returned |  |
| [`COUNT(DISTINCT)`](aggregate-functions.md) | Return the count of a number of different values |  |
| [`CRC32()`](mathematical-functions.md) | Compute a cyclic redundancy check value |  |
| [`CUME_DIST()`](window-function-descriptions.md) | Cumulative distribution value |  |
| [`CURDATE()`](date-and-time-functions.md) | Return the current date |  |
| [`CURRENT_DATE()`, `CURRENT_DATE`](date-and-time-functions.md) | Synonyms for CURDATE() |  |
| [`CURRENT_ROLE()`](information-functions.md) | Return the current active roles |  |
| [`CURRENT_TIME()`, `CURRENT_TIME`](date-and-time-functions.md) | Synonyms for CURTIME() |  |
| [`CURRENT_TIMESTAMP()`, `CURRENT_TIMESTAMP`](date-and-time-functions.md) | Synonyms for NOW() |  |
| [`CURRENT_USER()`, `CURRENT_USER`](information-functions.md) | The authenticated user name and host name |  |
| [`CURTIME()`](date-and-time-functions.md) | Return the current time |  |
| [`DATABASE()`](information-functions.md) | Return the default (current) database name |  |
| [`DATE()`](date-and-time-functions.md) | Extract the date part of a date or datetime expression |  |
| [`DATE_ADD()`](date-and-time-functions.md) | Add time values (intervals) to a date value |  |
| [`DATE_FORMAT()`](date-and-time-functions.md) | Format date as specified |  |
| [`DATE_SUB()`](date-and-time-functions.md) | Subtract a time value (interval) from a date |  |
| [`DATEDIFF()`](date-and-time-functions.md) | Subtract two dates |  |
| [`DAY()`](date-and-time-functions.md) | Synonym for DAYOFMONTH() |  |
| [`DAYNAME()`](date-and-time-functions.md) | Return the name of the weekday |  |
| [`DAYOFMONTH()`](date-and-time-functions.md) | Return the day of the month (0-31) |  |
| [`DAYOFWEEK()`](date-and-time-functions.md) | Return the weekday index of the argument |  |
| [`DAYOFYEAR()`](date-and-time-functions.md) | Return the day of the year (1-366) |  |
| [`DEFAULT()`](miscellaneous-functions.md) | Return the default value for a table column |  |
| [`DEGREES()`](mathematical-functions.md) | Convert radians to degrees |  |
| [`DENSE_RANK()`](window-function-descriptions.md) | Rank of current row within its partition, without gaps |  |
| [`DIV`](arithmetic-functions.md) | Integer division |  |
| [`ELT()`](string-functions.md) | Return string at index number |  |
| [`EXISTS()`](comparison-operators.md) | Whether the result of a query contains any rows |  |
| [`EXP()`](mathematical-functions.md) | Raise to the power of |  |
| [`EXPORT_SET()`](string-functions.md) | Return a string such that for every bit set in the value bits, you get an on string and for every unset bit, you get an off string |  |
| [`EXTRACT()`](date-and-time-functions.md) | Extract part of a date |  |
| [`ExtractValue()`](xml-functions.md) | Extract a value from an XML string using XPath notation |  |
| [`FIELD()`](string-functions.md) | Index (position) of first argument in subsequent arguments |  |
| [`FIND_IN_SET()`](string-functions.md) | Index (position) of first argument within second argument |  |
| [`FIRST_VALUE()`](window-function-descriptions.md) | Value of argument from first row of window frame |  |
| [`FLOOR()`](mathematical-functions.md) | Return the largest integer value not greater than the argument |  |
| [`FORMAT()`](string-functions.md) | Return a number formatted to specified number of decimal places |  |
| [`FORMAT_BYTES()`](performance-schema-functions.md) | Convert byte count to value with units |  |
| [`FORMAT_PICO_TIME()`](performance-schema-functions.md) | Convert time in picoseconds to value with units |  |
| [`FOUND_ROWS()`](information-functions.md) | For a SELECT with a LIMIT clause, the number of rows that would be returned were there no LIMIT clause |  |
| [`FROM_BASE64()`](string-functions.md) | Decode base64 encoded string and return result |  |
| [`FROM_DAYS()`](date-and-time-functions.md) | Convert a day number to a date |  |
| [`FROM_UNIXTIME()`](date-and-time-functions.md) | Format Unix timestamp as a date |  |
| [`GeomCollection()`](gis-mysql-specific-functions.md) | Construct geometry collection from geometries |  |
| [`GeometryCollection()`](gis-mysql-specific-functions.md) | Construct geometry collection from geometries |  |
| [`GET_DD_COLUMN_PRIVILEGES()`](internal-functions.md) | Internal use only |  |
| [`GET_DD_CREATE_OPTIONS()`](internal-functions.md) | Internal use only |  |
| [`GET_DD_INDEX_SUB_PART_LENGTH()`](internal-functions.md) | Internal use only |  |
| [`GET_FORMAT()`](date-and-time-functions.md) | Return a date format string |  |
| [`GET_LOCK()`](locking-functions.md) | Get a named lock |  |
| [`GREATEST()`](comparison-operators.md) | Return the largest argument |  |
| [`GROUP_CONCAT()`](aggregate-functions.md) | Return a concatenated string |  |
| [`group_replication_disable_member_action()`](group-replication-functions-for-member-actions.md) | Disable member action for event specified |  |
| [`group_replication_enable_member_action()`](group-replication-functions-for-member-actions.md) | Enable member action for event specified |  |
| [`group_replication_get_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Get version of group replication communication protocol currently in use |  |
| [`group_replication_get_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Get maximum number of consensus instances currently set for group |  |
| [`group_replication_reset_member_actions()`](group-replication-functions-for-member-actions.md) | Reset all member actions to defaults and configuration version number to 1 |  |
| [`group_replication_set_as_primary()`](group-replication-functions-for-new-primary.md) | Make a specific group member the primary |  |
| [`group_replication_set_communication_protocol()`](group-replication-functions-for-communication-protocol.md) | Set version for group replication communication protocol to use |  |
| [`group_replication_set_write_concurrency()`](group-replication-functions-for-maximum-consensus.md) | Set maximum number of consensus instances that can be executed in parallel |  |
| [`group_replication_switch_to_multi_primary_mode()`](group-replication-functions-for-mode.md) | Changes the mode of a group running in single-primary mode to multi-primary mode |  |
| [`group_replication_switch_to_single_primary_mode()`](group-replication-functions-for-mode.md) | Changes the mode of a group running in multi-primary mode to single-primary mode |  |
| [`GROUPING()`](miscellaneous-functions.md) | Distinguish super-aggregate ROLLUP rows from regular rows |  |
| [`GTID_SUBSET()`](gtid-functions.md) | Return true if all GTIDs in subset are also in set; otherwise false. |  |
| [`GTID_SUBTRACT()`](gtid-functions.md) | Return all GTIDs in set that are not in subset. |  |
| [`HEX()`](string-functions.md) | Hexadecimal representation of decimal or string value |  |
| [`HOUR()`](date-and-time-functions.md) | Extract the hour |  |
| [`ICU_VERSION()`](information-functions.md) | ICU library version |  |
| [`IF()`](flow-control-functions.md) | If/else construct |  |
| [`IFNULL()`](flow-control-functions.md) | Null if/else construct |  |
| [`IN()`](comparison-operators.md) | Whether a value is within a set of values |  |
| [`INET_ATON()`](miscellaneous-functions.md) | Return the numeric value of an IP address |  |
| [`INET_NTOA()`](miscellaneous-functions.md) | Return the IP address from a numeric value |  |
| [`INET6_ATON()`](miscellaneous-functions.md) | Return the numeric value of an IPv6 address |  |
| [`INET6_NTOA()`](miscellaneous-functions.md) | Return the IPv6 address from a numeric value |  |
| [`INSERT()`](string-functions.md) | Insert substring at specified position up to specified number of characters |  |
| [`INSTR()`](string-functions.md) | Return the index of the first occurrence of substring |  |
| [`INTERNAL_AUTO_INCREMENT()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_AVG_ROW_LENGTH()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_CHECK_TIME()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_CHECKSUM()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_DATA_FREE()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_DATA_LENGTH()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_DD_CHAR_LENGTH()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_GET_COMMENT_OR_ERROR()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_GET_ENABLED_ROLE_JSON()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_GET_HOSTNAME()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_GET_USERNAME()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_GET_VIEW_WARNING_OR_ERROR()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_INDEX_COLUMN_CARDINALITY()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_INDEX_LENGTH()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_IS_ENABLED_ROLE()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_IS_MANDATORY_ROLE()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_KEYS_DISABLED()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_MAX_DATA_LENGTH()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_TABLE_ROWS()`](internal-functions.md) | Internal use only |  |
| [`INTERNAL_UPDATE_TIME()`](internal-functions.md) | Internal use only |  |
| [`INTERVAL()`](comparison-operators.md) | Return the index of the argument that is less than the first argument |  |
| [`IS`](comparison-operators.md) | Test a value against a boolean |  |
| [`IS_FREE_LOCK()`](locking-functions.md) | Whether the named lock is free |  |
| [`IS_IPV4()`](miscellaneous-functions.md) | Whether argument is an IPv4 address |  |
| [`IS_IPV4_COMPAT()`](miscellaneous-functions.md) | Whether argument is an IPv4-compatible address |  |
| [`IS_IPV4_MAPPED()`](miscellaneous-functions.md) | Whether argument is an IPv4-mapped address |  |
| [`IS_IPV6()`](miscellaneous-functions.md) | Whether argument is an IPv6 address |  |
| [`IS NOT`](comparison-operators.md) | Test a value against a boolean |  |
| [`IS NOT NULL`](comparison-operators.md) | NOT NULL value test |  |
| [`IS NULL`](comparison-operators.md) | NULL value test |  |
| [`IS_USED_LOCK()`](locking-functions.md) | Whether the named lock is in use; return connection identifier if true |  |
| [`IS_UUID()`](miscellaneous-functions.md) | Whether argument is a valid UUID |  |
| [`ISNULL()`](comparison-operators.md) | Test whether the argument is NULL |  |
| [`JSON_ARRAY()`](json-creation-functions.md) | Create JSON array |  |
| [`JSON_ARRAY_APPEND()`](json-modification-functions.md) | Append data to JSON document |  |
| [`JSON_ARRAY_INSERT()`](json-modification-functions.md) | Insert into JSON array |  |
| [`JSON_ARRAYAGG()`](aggregate-functions.md) | Return result set as a single JSON array |  |
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
| [`JSON_OBJECTAGG()`](aggregate-functions.md) | Return result set as a single JSON object |  |
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
| [`LAG()`](window-function-descriptions.md) | Value of argument from row lagging current row within partition |  |
| [`LAST_DAY`](date-and-time-functions.md) | Return the last day of the month for the argument |  |
| [`LAST_INSERT_ID()`](information-functions.md) | Value of the AUTOINCREMENT column for the last INSERT |  |
| [`LAST_VALUE()`](window-function-descriptions.md) | Value of argument from last row of window frame |  |
| [`LCASE()`](string-functions.md) | Synonym for LOWER() |  |
| [`LEAD()`](window-function-descriptions.md) | Value of argument from row leading current row within partition |  |
| [`LEAST()`](comparison-operators.md) | Return the smallest argument |  |
| [`LEFT()`](string-functions.md) | Return the leftmost number of characters as specified |  |
| [`LENGTH()`](string-functions.md) | Return the length of a string in bytes |  |
| [`LIKE`](string-comparison-functions.md) | Simple pattern matching |  |
| [`LineString()`](gis-mysql-specific-functions.md) | Construct LineString from Point values |  |
| [`LN()`](mathematical-functions.md) | Return the natural logarithm of the argument |  |
| [`LOAD_FILE()`](string-functions.md) | Load the named file |  |
| [`LOCALTIME()`, `LOCALTIME`](date-and-time-functions.md) | Synonym for NOW() |  |
| [`LOCALTIMESTAMP`, `LOCALTIMESTAMP()`](date-and-time-functions.md) | Synonym for NOW() |  |
| [`LOCATE()`](string-functions.md) | Return the position of the first occurrence of substring |  |
| [`LOG()`](mathematical-functions.md) | Return the natural logarithm of the first argument |  |
| [`LOG10()`](mathematical-functions.md) | Return the base-10 logarithm of the argument |  |
| [`LOG2()`](mathematical-functions.md) | Return the base-2 logarithm of the argument |  |
| [`LOWER()`](string-functions.md) | Return the argument in lowercase |  |
| [`LPAD()`](string-functions.md) | Return the string argument, left-padded with the specified string |  |
| [`LTRIM()`](string-functions.md) | Remove leading spaces |  |
| [`MAKE_SET()`](string-functions.md) | Return a set of comma-separated strings that have the corresponding bit in bits set |  |
| [`MAKEDATE()`](date-and-time-functions.md) | Create a date from the year and day of year |  |
| [`MAKETIME()`](date-and-time-functions.md) | Create time from hour, minute, second |  |
| [`MASTER_POS_WAIT()`](replication-functions-synchronization.md) | Block until the replica has read and applied all updates up to the specified position | Yes |
| [`MATCH()`](fulltext-search.md) | Perform full-text search |  |
| [`MAX()`](aggregate-functions.md) | Return the maximum value |  |
| [`MBRContains()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry contains MBR of another |  |
| [`MBRCoveredBy()`](spatial-relation-functions-mbr.md) | Whether one MBR is covered by another |  |
| [`MBRCovers()`](spatial-relation-functions-mbr.md) | Whether one MBR covers another |  |
| [`MBRDisjoint()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are disjoint |  |
| [`MBREquals()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries are equal |  |
| [`MBRIntersects()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries intersect |  |
| [`MBROverlaps()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries overlap |  |
| [`MBRTouches()`](spatial-relation-functions-mbr.md) | Whether MBRs of two geometries touch |  |
| [`MBRWithin()`](spatial-relation-functions-mbr.md) | Whether MBR of one geometry is within MBR of another |  |
| [`MD5()`](encryption-functions.md) | Calculate MD5 checksum |  |
| [`MEMBER OF()`](json-search-functions.md) | Returns true (1) if first operand matches any element of JSON array passed as second operand, otherwise returns false (0) |  |
| [`MICROSECOND()`](date-and-time-functions.md) | Return the microseconds from argument |  |
| [`MID()`](string-functions.md) | Return a substring starting from the specified position |  |
| [`MIN()`](aggregate-functions.md) | Return the minimum value |  |
| [`MINUTE()`](date-and-time-functions.md) | Return the minute from the argument |  |
| [`MOD()`](mathematical-functions.md) | Return the remainder |  |
| [`MONTH()`](date-and-time-functions.md) | Return the month from the date passed |  |
| [`MONTHNAME()`](date-and-time-functions.md) | Return the name of the month |  |
| [`MultiLineString()`](gis-mysql-specific-functions.md) | Contruct MultiLineString from LineString values |  |
| [`MultiPoint()`](gis-mysql-specific-functions.md) | Construct MultiPoint from Point values |  |
| [`MultiPolygon()`](gis-mysql-specific-functions.md) | Construct MultiPolygon from Polygon values |  |
| [`NAME_CONST()`](miscellaneous-functions.md) | Cause the column to have the given name |  |
| [`NOT`, `!`](logical-operators.md) | Negates value |  |
| [`NOT BETWEEN ... AND ...`](comparison-operators.md) | Whether a value is not within a range of values |  |
| [`NOT EXISTS()`](comparison-operators.md) | Whether the result of a query contains no rows |  |
| [`NOT IN()`](comparison-operators.md) | Whether a value is not within a set of values |  |
| [`NOT LIKE`](string-comparison-functions.md) | Negation of simple pattern matching |  |
| [`NOT REGEXP`](regexp.md) | Negation of REGEXP |  |
| [`NOW()`](date-and-time-functions.md) | Return the current date and time |  |
| [`NTH_VALUE()`](window-function-descriptions.md) | Value of argument from N-th row of window frame |  |
| [`NTILE()`](window-function-descriptions.md) | Bucket number of current row within its partition. |  |
| [`NULLIF()`](flow-control-functions.md) | Return NULL if expr1 = expr2 |  |
| [`OCT()`](string-functions.md) | Return a string containing octal representation of a number |  |
| [`OCTET_LENGTH()`](string-functions.md) | Synonym for LENGTH() |  |
| [`OR`, `\|\|`](logical-operators.md) | Logical OR |  |
| [`ORD()`](string-functions.md) | Return character code for leftmost character of the argument |  |
| [`PERCENT_RANK()`](window-function-descriptions.md) | Percentage rank value |  |
| [`PERIOD_ADD()`](date-and-time-functions.md) | Add a period to a year-month |  |
| [`PERIOD_DIFF()`](date-and-time-functions.md) | Return the number of months between periods |  |
| [`PI()`](mathematical-functions.md) | Return the value of pi |  |
| [`Point()`](gis-mysql-specific-functions.md) | Construct Point from coordinates |  |
| [`Polygon()`](gis-mysql-specific-functions.md) | Construct Polygon from LineString arguments |  |
| [`POSITION()`](string-functions.md) | Synonym for LOCATE() |  |
| [`POW()`](mathematical-functions.md) | Return the argument raised to the specified power |  |
| [`POWER()`](mathematical-functions.md) | Return the argument raised to the specified power |  |
| [`PS_CURRENT_THREAD_ID()`](performance-schema-functions.md) | Performance Schema thread ID for current thread |  |
| [`PS_THREAD_ID()`](performance-schema-functions.md) | Performance Schema thread ID for given thread |  |
| [`QUARTER()`](date-and-time-functions.md) | Return the quarter from a date argument |  |
| [`QUOTE()`](string-functions.md) | Escape the argument for use in an SQL statement |  |
| [`RADIANS()`](mathematical-functions.md) | Return argument converted to radians |  |
| [`RAND()`](mathematical-functions.md) | Return a random floating-point value |  |
| [`RANDOM_BYTES()`](encryption-functions.md) | Return a random byte vector |  |
| [`RANK()`](window-function-descriptions.md) | Rank of current row within its partition, with gaps |  |
| [`REGEXP`](regexp.md) | Whether string matches regular expression |  |
| [`REGEXP_INSTR()`](regexp.md) | Starting index of substring matching regular expression |  |
| [`REGEXP_LIKE()`](regexp.md) | Whether string matches regular expression |  |
| [`REGEXP_REPLACE()`](regexp.md) | Replace substrings matching regular expression |  |
| [`REGEXP_SUBSTR()`](regexp.md) | Return substring matching regular expression |  |
| [`RELEASE_ALL_LOCKS()`](locking-functions.md) | Release all current named locks |  |
| [`RELEASE_LOCK()`](locking-functions.md) | Release the named lock |  |
| [`REPEAT()`](string-functions.md) | Repeat a string the specified number of times |  |
| [`REPLACE()`](string-functions.md) | Replace occurrences of a specified string |  |
| [`REVERSE()`](string-functions.md) | Reverse the characters in a string |  |
| [`RIGHT()`](string-functions.md) | Return the specified rightmost number of characters |  |
| [`RLIKE`](regexp.md) | Whether string matches regular expression |  |
| [`ROLES_GRAPHML()`](information-functions.md) | Return a GraphML document representing memory role subgraphs |  |
| [`ROUND()`](mathematical-functions.md) | Round the argument |  |
| [`ROW_COUNT()`](information-functions.md) | The number of rows updated |  |
| [`ROW_NUMBER()`](window-function-descriptions.md) | Number of current row within its partition |  |
| [`RPAD()`](string-functions.md) | Append string the specified number of times |  |
| [`RTRIM()`](string-functions.md) | Remove trailing spaces |  |
| [`SCHEMA()`](information-functions.md) | Synonym for DATABASE() |  |
| [`SEC_TO_TIME()`](date-and-time-functions.md) | Converts seconds to 'hh:mm:ss' format |  |
| [`SECOND()`](date-and-time-functions.md) | Return the second (0-59) |  |
| [`SESSION_USER()`](information-functions.md) | Synonym for USER() |  |
| [`SHA1()`, `SHA()`](encryption-functions.md) | Calculate an SHA-1 160-bit checksum |  |
| [`SHA2()`](encryption-functions.md) | Calculate an SHA-2 checksum |  |
| [`SIGN()`](mathematical-functions.md) | Return the sign of the argument |  |
| [`SIN()`](mathematical-functions.md) | Return the sine of the argument |  |
| [`SLEEP()`](miscellaneous-functions.md) | Sleep for a number of seconds |  |
| [`SOUNDEX()`](string-functions.md) | Return a soundex string |  |
| [`SOUNDS LIKE`](string-functions.md) | Compare sounds |  |
| [`SOURCE_POS_WAIT()`](replication-functions-synchronization.md) | Block until the replica has read and applied all updates up to the specified position |  |
| [`SPACE()`](string-functions.md) | Return a string of the specified number of spaces |  |
| [`SQRT()`](mathematical-functions.md) | Return the square root of the argument |  |
| [`ST_Area()`](gis-polygon-property-functions.md) | Return Polygon or MultiPolygon area |  |
| [`ST_AsBinary()`, `ST_AsWKB()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKB |  |
| [`ST_AsGeoJSON()`](spatial-geojson-functions.md) | Generate GeoJSON object from geometry |  |
| [`ST_AsText()`, `ST_AsWKT()`](gis-format-conversion-functions.md) | Convert from internal geometry format to WKT |  |
| [`ST_Buffer()`](spatial-operator-functions.md) | Return geometry of points within given distance from geometry |  |
| [`ST_Buffer_Strategy()`](spatial-operator-functions.md) | Produce strategy option for ST\_Buffer() |  |
| [`ST_Centroid()`](gis-polygon-property-functions.md) | Return centroid as a point |  |
| [`ST_Collect()`](spatial-aggregate-functions.md) | Aggregate spatial values into collection |  |
| [`ST_Contains()`](spatial-relation-functions-object-shapes.md) | Whether one geometry contains another |  |
| [`ST_ConvexHull()`](spatial-operator-functions.md) | Return convex hull of geometry |  |
| [`ST_Crosses()`](spatial-relation-functions-object-shapes.md) | Whether one geometry crosses another |  |
| [`ST_Difference()`](spatial-operator-functions.md) | Return point set difference of two geometries |  |
| [`ST_Dimension()`](gis-general-property-functions.md) | Dimension of geometry |  |
| [`ST_Disjoint()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is disjoint from another |  |
| [`ST_Distance()`](spatial-relation-functions-object-shapes.md) | The distance of one geometry from another |  |
| [`ST_Distance_Sphere()`](spatial-convenience-functions.md) | Minimum distance on earth between two geometries |  |
| [`ST_EndPoint()`](gis-linestring-property-functions.md) | End Point of LineString |  |
| [`ST_Envelope()`](gis-general-property-functions.md) | Return MBR of geometry |  |
| [`ST_Equals()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is equal to another |  |
| [`ST_ExteriorRing()`](gis-polygon-property-functions.md) | Return exterior ring of Polygon |  |
| [`ST_FrechetDistance()`](spatial-relation-functions-object-shapes.md) | The discrete Fréchet distance of one geometry from another |  |
| [`ST_GeoHash()`](spatial-geohash-functions.md) | Produce a geohash value |  |
| [`ST_GeomCollFromText()`, `ST_GeometryCollectionFromText()`, `ST_GeomCollFromTxt()`](gis-wkt-functions.md) | Return geometry collection from WKT |  |
| [`ST_GeomCollFromWKB()`, `ST_GeometryCollectionFromWKB()`](gis-wkb-functions.md) | Return geometry collection from WKB |  |
| [`ST_GeometryN()`](gis-geometrycollection-property-functions.md) | Return N-th geometry from geometry collection |  |
| [`ST_GeometryType()`](gis-general-property-functions.md) | Return name of geometry type |  |
| [`ST_GeomFromGeoJSON()`](spatial-geojson-functions.md) | Generate geometry from GeoJSON object |  |
| [`ST_GeomFromText()`, `ST_GeometryFromText()`](gis-wkt-functions.md) | Return geometry from WKT |  |
| [`ST_GeomFromWKB()`, `ST_GeometryFromWKB()`](gis-wkb-functions.md) | Return geometry from WKB |  |
| [`ST_HausdorffDistance()`](spatial-relation-functions-object-shapes.md) | The discrete Hausdorff distance of one geometry from another |  |
| [`ST_InteriorRingN()`](gis-polygon-property-functions.md) | Return N-th interior ring of Polygon |  |
| [`ST_Intersection()`](spatial-operator-functions.md) | Return point set intersection of two geometries |  |
| [`ST_Intersects()`](spatial-relation-functions-object-shapes.md) | Whether one geometry intersects another |  |
| [`ST_IsClosed()`](gis-linestring-property-functions.md) | Whether a geometry is closed and simple |  |
| [`ST_IsEmpty()`](gis-general-property-functions.md) | Whether a geometry is empty |  |
| [`ST_IsSimple()`](gis-general-property-functions.md) | Whether a geometry is simple |  |
| [`ST_IsValid()`](spatial-convenience-functions.md) | Whether a geometry is valid |  |
| [`ST_LatFromGeoHash()`](spatial-geohash-functions.md) | Return latitude from geohash value |  |
| [`ST_Latitude()`](gis-point-property-functions.md) | Return latitude of Point |  |
| [`ST_Length()`](gis-linestring-property-functions.md) | Return length of LineString |  |
| [`ST_LineFromText()`, `ST_LineStringFromText()`](gis-wkt-functions.md) | Construct LineString from WKT |  |
| [`ST_LineFromWKB()`, `ST_LineStringFromWKB()`](gis-wkb-functions.md) | Construct LineString from WKB |  |
| [`ST_LineInterpolatePoint()`](spatial-operator-functions.md) | The point a given percentage along a LineString |  |
| [`ST_LineInterpolatePoints()`](spatial-operator-functions.md) | The points a given percentage along a LineString |  |
| [`ST_LongFromGeoHash()`](spatial-geohash-functions.md) | Return longitude from geohash value |  |
| [`ST_Longitude()`](gis-point-property-functions.md) | Return longitude of Point |  |
| [`ST_MakeEnvelope()`](spatial-convenience-functions.md) | Rectangle around two points |  |
| [`ST_MLineFromText()`, `ST_MultiLineStringFromText()`](gis-wkt-functions.md) | Construct MultiLineString from WKT |  |
| [`ST_MLineFromWKB()`, `ST_MultiLineStringFromWKB()`](gis-wkb-functions.md) | Construct MultiLineString from WKB |  |
| [`ST_MPointFromText()`, `ST_MultiPointFromText()`](gis-wkt-functions.md) | Construct MultiPoint from WKT |  |
| [`ST_MPointFromWKB()`, `ST_MultiPointFromWKB()`](gis-wkb-functions.md) | Construct MultiPoint from WKB |  |
| [`ST_MPolyFromText()`, `ST_MultiPolygonFromText()`](gis-wkt-functions.md) | Construct MultiPolygon from WKT |  |
| [`ST_MPolyFromWKB()`, `ST_MultiPolygonFromWKB()`](gis-wkb-functions.md) | Construct MultiPolygon from WKB |  |
| [`ST_NumGeometries()`](gis-geometrycollection-property-functions.md) | Return number of geometries in geometry collection |  |
| [`ST_NumInteriorRing()`, `ST_NumInteriorRings()`](gis-polygon-property-functions.md) | Return number of interior rings in Polygon |  |
| [`ST_NumPoints()`](gis-linestring-property-functions.md) | Return number of points in LineString |  |
| [`ST_Overlaps()`](spatial-relation-functions-object-shapes.md) | Whether one geometry overlaps another |  |
| [`ST_PointAtDistance()`](spatial-operator-functions.md) | The point a given distance along a LineString |  |
| [`ST_PointFromGeoHash()`](spatial-geohash-functions.md) | Convert geohash value to POINT value |  |
| [`ST_PointFromText()`](gis-wkt-functions.md) | Construct Point from WKT |  |
| [`ST_PointFromWKB()`](gis-wkb-functions.md) | Construct Point from WKB |  |
| [`ST_PointN()`](gis-linestring-property-functions.md) | Return N-th point from LineString |  |
| [`ST_PolyFromText()`, `ST_PolygonFromText()`](gis-wkt-functions.md) | Construct Polygon from WKT |  |
| [`ST_PolyFromWKB()`, `ST_PolygonFromWKB()`](gis-wkb-functions.md) | Construct Polygon from WKB |  |
| [`ST_Simplify()`](spatial-convenience-functions.md) | Return simplified geometry |  |
| [`ST_SRID()`](gis-general-property-functions.md) | Return spatial reference system ID for geometry |  |
| [`ST_StartPoint()`](gis-linestring-property-functions.md) | Start Point of LineString |  |
| [`ST_SwapXY()`](gis-format-conversion-functions.md) | Return argument with X/Y coordinates swapped |  |
| [`ST_SymDifference()`](spatial-operator-functions.md) | Return point set symmetric difference of two geometries |  |
| [`ST_Touches()`](spatial-relation-functions-object-shapes.md) | Whether one geometry touches another |  |
| [`ST_Transform()`](spatial-operator-functions.md) | Transform coordinates of geometry |  |
| [`ST_Union()`](spatial-operator-functions.md) | Return point set union of two geometries |  |
| [`ST_Validate()`](spatial-convenience-functions.md) | Return validated geometry |  |
| [`ST_Within()`](spatial-relation-functions-object-shapes.md) | Whether one geometry is within another |  |
| [`ST_X()`](gis-point-property-functions.md) | Return X coordinate of Point |  |
| [`ST_Y()`](gis-point-property-functions.md) | Return Y coordinate of Point |  |
| [`STATEMENT_DIGEST()`](encryption-functions.md) | Compute statement digest hash value |  |
| [`STATEMENT_DIGEST_TEXT()`](encryption-functions.md) | Compute normalized statement digest |  |
| [`STD()`](aggregate-functions.md) | Return the population standard deviation |  |
| [`STDDEV()`](aggregate-functions.md) | Return the population standard deviation |  |
| [`STDDEV_POP()`](aggregate-functions.md) | Return the population standard deviation |  |
| [`STDDEV_SAMP()`](aggregate-functions.md) | Return the sample standard deviation |  |
| [`STR_TO_DATE()`](date-and-time-functions.md) | Convert a string to a date |  |
| [`STRCMP()`](string-comparison-functions.md) | Compare two strings |  |
| [`SUBDATE()`](date-and-time-functions.md) | Synonym for DATE\_SUB() when invoked with three arguments |  |
| [`SUBSTR()`](string-functions.md) | Return the substring as specified |  |
| [`SUBSTRING()`](string-functions.md) | Return the substring as specified |  |
| [`SUBSTRING_INDEX()`](string-functions.md) | Return a substring from a string before the specified number of occurrences of the delimiter |  |
| [`SUBTIME()`](date-and-time-functions.md) | Subtract times |  |
| [`SUM()`](aggregate-functions.md) | Return the sum |  |
| [`SYSDATE()`](date-and-time-functions.md) | Return the time at which the function executes |  |
| [`SYSTEM_USER()`](information-functions.md) | Synonym for USER() |  |
| [`TAN()`](mathematical-functions.md) | Return the tangent of the argument |  |
| [`TIME()`](date-and-time-functions.md) | Extract the time portion of the expression passed |  |
| [`TIME_FORMAT()`](date-and-time-functions.md) | Format as time |  |
| [`TIME_TO_SEC()`](date-and-time-functions.md) | Return the argument converted to seconds |  |
| [`TIMEDIFF()`](date-and-time-functions.md) | Subtract time |  |
| [`TIMESTAMP()`](date-and-time-functions.md) | With a single argument, this function returns the date or datetime expression; with two arguments, the sum of the arguments |  |
| [`TIMESTAMPADD()`](date-and-time-functions.md) | Add an interval to a datetime expression |  |
| [`TIMESTAMPDIFF()`](date-and-time-functions.md) | Return the difference of two datetime expressions, using the units specified |  |
| [`TO_BASE64()`](string-functions.md) | Return the argument converted to a base-64 string |  |
| [`TO_DAYS()`](date-and-time-functions.md) | Return the date argument converted to days |  |
| [`TO_SECONDS()`](date-and-time-functions.md) | Return the date or datetime argument converted to seconds since Year 0 |  |
| [`TRIM()`](string-functions.md) | Remove leading and trailing spaces |  |
| [`TRUNCATE()`](mathematical-functions.md) | Truncate to specified number of decimal places |  |
| [`UCASE()`](string-functions.md) | Synonym for UPPER() |  |
| [`UNCOMPRESS()`](encryption-functions.md) | Uncompress a string compressed |  |
| [`UNCOMPRESSED_LENGTH()`](encryption-functions.md) | Return the length of a string before compression |  |
| [`UNHEX()`](string-functions.md) | Return a string containing hex representation of a number |  |
| [`UNIX_TIMESTAMP()`](date-and-time-functions.md) | Return a Unix timestamp |  |
| [`UpdateXML()`](xml-functions.md) | Return replaced XML fragment |  |
| [`UPPER()`](string-functions.md) | Convert to uppercase |  |
| [`USER()`](information-functions.md) | The user name and host name provided by the client |  |
| [`UTC_DATE()`](date-and-time-functions.md) | Return the current UTC date |  |
| [`UTC_TIME()`](date-and-time-functions.md) | Return the current UTC time |  |
| [`UTC_TIMESTAMP()`](date-and-time-functions.md) | Return the current UTC date and time |  |
| [`UUID()`](miscellaneous-functions.md) | Return a Universal Unique Identifier (UUID) |  |
| [`UUID_SHORT()`](miscellaneous-functions.md) | Return an integer-valued universal identifier |  |
| [`UUID_TO_BIN()`](miscellaneous-functions.md) | Convert string UUID to binary |  |
| [`VALIDATE_PASSWORD_STRENGTH()`](encryption-functions.md) | Determine strength of password |  |
| [`VALUES()`](miscellaneous-functions.md) | Define the values to be used during an INSERT |  |
| [`VAR_POP()`](aggregate-functions.md) | Return the population standard variance |  |
| [`VAR_SAMP()`](aggregate-functions.md) | Return the sample variance |  |
| [`VARIANCE()`](aggregate-functions.md) | Return the population standard variance |  |
| [`VERSION()`](information-functions.md) | Return a string that indicates the MySQL server version |  |
| [`WAIT_FOR_EXECUTED_GTID_SET()`](gtid-functions.md) | Wait until the given GTIDs have executed on the replica. |  |
| [`WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS()`](gtid-functions.md) | Use `WAIT_FOR_EXECUTED_GTID_SET()`. | Yes |
| [`WEEK()`](date-and-time-functions.md) | Return the week number |  |
| [`WEEKDAY()`](date-and-time-functions.md) | Return the weekday index |  |
| [`WEEKOFYEAR()`](date-and-time-functions.md) | Return the calendar week of the date (1-53) |  |
| [`WEIGHT_STRING()`](string-functions.md) | Return the weight string for a string |  |
| [`XOR`](logical-operators.md) | Logical XOR |  |
| [`YEAR()`](date-and-time-functions.md) | Return the year |  |
| [`YEARWEEK()`](date-and-time-functions.md) | Return the year and week |  |
| [`\|`](bit-functions.md) | Bitwise OR |  |
| [`~`](bit-functions.md) | Bitwise inversion |  |