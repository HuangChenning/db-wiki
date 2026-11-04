---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JAVA_THROWS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.253 ALL\_JAVA\_THROWS

`ALL_JAVA_THROWS` displays information about exceptions thrown from methods of the Java classes accessible to the current user.

Related Views

- `DBA_JAVA_THROWS` displays information about exceptions thrown from methods of all Java classes in the database.
- `USER_JAVA_THROWS` displays information about exceptions thrown from methods of the Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `METHOD_INDEX` | `NUMBER` |  | Index of the throwing method of the exception |
| `METHOD_NAME` | `VARCHAR2(4000)` |  | Name of the throwing method of the exception |
| `EXCEPTION_INDEX` | `NUMBER` |  | Index of the exception |
| `EXCEPTION_CLASS` | `VARCHAR2(4000)` |  | Class of the exception |