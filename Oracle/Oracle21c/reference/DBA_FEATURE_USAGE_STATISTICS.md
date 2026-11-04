---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_FEATURE_USAGE_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.321 DBA\_FEATURE\_USAGE\_STATISTICS

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
| `LAST_SAMPLE_DATE` | `DATE` |  | The last time the system checked for usage |
| `LAST_SAMPLE_PERIOD` | `NUMBER` |  | Amount of time (in seconds) between the last two usage sample times |
| `SAMPLE_INTERVAL` | `NUMBER` |  | Sample interval |
| `DESCRIPTION` | `VARCHAR2(128)` |  | Description of the feature and usage detection logic |
| `LAST_FEAT_SAMPLE_DATE` <sup>Foot 1</sup> | `DATE` |  | The last time the system checked for usage of the feature |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 21c.

Note:

Use the following SQL query to list the database features and their descriptions in alphabetical order:

```
SELECT name, description FROM dba_feature_usage_statistics
ORDER BY name;
```