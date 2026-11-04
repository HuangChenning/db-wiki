---
title: ALL_FILE_GROUP_TABLESPACES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1096.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_FILE_GROUP_TABLESPACES` shows information about the transportable tablespaces present (partially or completely) in the file groups accessible to the current user (when the file groups contain dump files).

Related Views

- `DBA_FILE_GROUP_TABLESPACES` shows information about the transportable tablespaces present (partially or completely) in all file groups in the database (when the file groups contain dump files).
- `USER_FILE_GROUP_TABLESPACES` shows information about the transportable tablespaces present (partially or completely) in the file groups owned by the current user (when the file groups contain dump files). This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Version of the file group that contains the tablespace |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |