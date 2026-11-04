---
title: DBFS_CONTENT_PROPERTIES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5114.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBFS_CONTENT_PROPERTIES` displays all the property/value pairs for all path items in all content stores in the system.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STORE` | `VARCHAR2(256)` |  | Name of store |
| `MOUNT` | `VARCHAR2(256)` |  | Location at which instance of store is mounted |
| `PATHNAME` | `VARCHAR2(1024)` |  | Name of path to item |
| `PROPERTY_NAME` | `VARCHAR2(32)` |  | Name of the property |
| `PROPERTY_VALUE` | `VARCHAR2(1024)` |  | Value of the property |
| `PROPERTY_TYPE` | `NUMBER` |  | PL/SQL typecode for the property value |