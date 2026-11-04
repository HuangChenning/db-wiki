---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_APPLICATIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.99 DBA\_APPLICATIONS

`DBA_APPLICATIONS` provides information about the applications in the current application container.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application |
| `APP_ID` | `NUMBER` |  | ID of the application |
| `APP_VERSION` | `VARCHAR2(30)` |  | Version of the application |
| `APP_STATUS` | `VARCHAR2(12)` |  | Status of the application |
| `APP_IMPLICIT` | `VARCHAR2(1)` |  | Indicates whether the application is implicit (`Y`) or not (`N`) |
| `APP_CAPTURE_SERVICE` | `VARCHAR2(64)` |  | Service name used for the capture |
| `APP_CAPTURE_MODULE` | `VARCHAR2(64)` |  | Module name used for the capture |