---
title: DBA_APPLY_INSTANTIATED_OBJECTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3056.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_APPLY_INSTANTIATED_OBJECTS` displays information about objects for which an instantiation SCN has been set.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SOURCE_DATABASE` | `VARCHAR2(128)` | `NOT NULL` | Name of the database where the object originated |
| `SOURCE_OBJECT_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object at the source database |
| `SOURCE_OBJECT_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object at the source database |
| `SOURCE_OBJECT_TYPE` | `VARCHAR2(11)` |  | Type of the object at the source database |
| `INSTANTIATION_SCN` | `NUMBER` |  | Instantiation SCN for the object. Only changes committed after this SCN are applied by an apply process. |
| `IGNORE_SCN` | `NUMBER` |  | SCN below which the instantiation SCN cannot be set. This value corresponds to the SCN value at the source database at the time when the object was prepared for instantiation. |
| `APPLY_DATABASE_LINK` | `VARCHAR2(128)` |  | Database link to which changes are applied. If null, then changes are applied to the local database. |