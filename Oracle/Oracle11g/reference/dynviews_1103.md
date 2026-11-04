---
title: "V$DATAGUARD_CONFIG"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1103.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$DATAGUARD_CONFIG` displays the unique database names defined with the `DB_UNIQUE_NAME` and `LOG_ARCHIVE_CONFIG` initialization parameters, providing a view of the Data Guard environment from any database in the configuration.

The first row of the view lists the unique database name of the current database that was specified with the `DB_UNIQUE_NAME` initialization parameter. Additional rows reflect the unique database names of the other databases in the configuration that were specified with the `DG_CONFIG` keyword of the `LOG_ARCHIVE_CONFIG` initialization parameter.

| Column | Datatype | Description |
| --- | --- | --- |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | Unique database name |