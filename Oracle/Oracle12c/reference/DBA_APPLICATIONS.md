---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_APPLICATIONS.html
tags:
  - oracle
  - 12c
  - reference
---

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

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).