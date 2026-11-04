---
title: ALL_DEPENDENCIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1069.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_DEPENDENCIES` describes dependencies between procedures, packages, functions, package bodies, and triggers accessible to the current user, including dependencies on views created without any database links. This view does not display the `SCHEMAID` column.

Related Views

- `DBA_DEPENDENCIES` describes all dependencies between objects in the database. This view does not display the `SCHEMAID` column.
- `USER_DEPENDENCIES` describes dependencies between objects in the current user's schema. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(17)` |  | Type of the object |
| `REFERENCED_OWNER` | `VARCHAR2(30)` |  | Owner of the referenced object (remote owner if remote object) |
| `REFERENCED_NAME` | `VARCHAR2(64)` |  | Name of the referenced object |
| `REFERENCED_TYPE` | `VARCHAR2(17)` |  | Type of the referenced object |
| `REFERENCED_LINK_NAME` | `VARCHAR2(128)` |  | Name of the link to the parent object (if remote) |
| `SCHEMAID` | `NUMBER` |  | ID of the current schema |
| `DEPENDENCY_TYPE` | `VARCHAR2(4)` |  | Indicates whether the dependency is a `REF` dependency (`REF`) or not (`HARD`) |