---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_FILE_GROUP_EXPORT_INFO.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.191 ALL\_FILE\_GROUP\_EXPORT\_INFO

There will only be information in this view for versions that have a valid Data Pump dump file.

Related Views

- `DBA_FILE_GROUP_EXPORT_INFO` shows export-related information for each version in the database that has a valid Data Pump dump file.
- `USER_FILE_GROUP_EXPORT_INFO` shows export-related information for all file groups owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | User-specified name for the version |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number |
| `EXPORT_VERSION` | `VARCHAR2(128)` | `NOT NULL` | Version of exported objects |
| `PLATFORM_NAME` | `VARCHAR2(101)` | `NOT NULL` | Platform on which the export was performed |
| `EXPORT_TIME` | `DATE` | `NOT NULL` | Time at which the export job was performed |
| `EXPORT_SCN` | `NUMBER` |  | SCN of the export job |
| `SOURCE_GLOBAL_NAME` | `VARCHAR2(128)` |  | Global name of the exporting database |

See Also:

- " [DBA\_FILE\_GROUP\_EXPORT\_INFO](DBA_FILE_GROUP_EXPORT_INFO.md) "
- " [USER\_FILE\_GROUP\_EXPORT\_INFO](USER_FILE_GROUP_EXPORT_INFO.md) "