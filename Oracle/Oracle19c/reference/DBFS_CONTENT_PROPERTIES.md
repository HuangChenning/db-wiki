---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBFS_CONTENT_PROPERTIES.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.171 DBFS\_CONTENT\_PROPERTIES

`DBFS_CONTENT_PROPERTIES` displays all the property/value pairs for all path items in all content stores in the system.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STORE` | `VARCHAR2(256)` |  | Name of store |
| `MOUNT` | `VARCHAR2(256)` |  | Location at which instance of store is mounted |
| `PATHNAME` | `VARCHAR2(1024)` |  | Name of path to item |
| `PROPERTY_NAME` | `VARCHAR2(32)` |  | Name of the property |
| `PROPERTY_VALUE` | `VARCHAR2(1024)` |  | Value of the property |
| `PROPERTY_TYPE` | `NUMBER` |  | PL/SQL typecode for the property value |