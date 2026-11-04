---
title: DBA_FEATURE_USAGE_STATISTICS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3181.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_FEATURE_USAGE_STATISTICS` displays information about database feature usage statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database identifier of the database being tracked |
| `NAME` | `VARCHAR2(64)` | `NOT NULL` | Name of the feature |
| `VERSION` | `VARCHAR2(17)` | `NOT NULL` | Database version in which the feature was tracked |
| `DETECTED_USAGES` | `NUMBER` | `NOT NULL` | Number of times the system has detected usage for the feature |
| `TOTAL_SAMPLES` | `NUMBER` | `NOT NULL` | Number of times the system has woken up and checked for feature usage |
| `CURRENTLY_USED` | `VARCHAR2(5)` |  | Indicates whether usage was detected the last time the system checked (`TRUE`) or not (`FALSE`) |
| `FIRST_USAGE_DATE` | `DATE` |  | First sample time the system detected usage of the feature |
| `LAST_USAGE_DATE` | `DATE` |  | Last sample time the system detected usage of the feature |
| `AUX_COUNT` | `NUMBER` |  | This column stores feature-specific usage data in number format. |
| `FEATURE_INFO` | `CLOB` |  | This column stores feature-specific usage data in character format. |
| `LAST_SAMPLE_DATE` | `DATE` |  | Amount of time (in seconds) between the last two usage sample times |
| `LAST_SAMPLE_PERIOD` | `NUMBER` |  | Amount of time (in hours) between the last two usage sample times |
| `SAMPLE_INTERVAL` | `NUMBER` |  | Sample interval |
| `DESCRIPTION` | `VARCHAR2(128)` |  | Description of the feature and usage detection logic |

Note:

Use the following SQL query to list the database features and their descriptions in alphabetical order:
```
SELECT name, description FROM dba_feature_usage_statistics
ORDER BY name;
```