---
title: ALL_FILE_GROUP_EXPORT_INFO
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1093.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_FILE_GROUP_EXPORT_INFO` shows export-related information for each version accessible to the current user. There will only be information in this view for versions that have a valid Data Pump dump file.

Related Views

- `DBA_FILE_GROUP_EXPORT_INFO` shows export-related information for each version in the database that has a valid Data Pump dump file.
- `USER_FILE_GROUP_EXPORT_INFO` shows export-related information for all file groups owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | User-specified name for the version |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number |
| `EXPORT_VERSION` | `VARCHAR2(30)` | `NOT NULL` | Version of exported objects |
| `PLATFORM_NAME` | `VARCHAR2(101)` | `NOT NULL` | Platform on which the export was performed |
| `EXPORT_TIME` | `DATE` | `NOT NULL` | Time at which the export job was performed |
| `EXPORT_SCN` | `NUMBER` |  | SCN of the export job |
| `SOURCE_GLOBAL_NAME` | `VARCHAR2(128)` |  | Global name of the exporting database |