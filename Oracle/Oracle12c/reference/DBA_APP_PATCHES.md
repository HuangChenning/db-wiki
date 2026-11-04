---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_APP_PATCHES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_APP_PATCHES` describes all the application patches in the Application Container.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application |
| `PATCH_NUMBER` | `NUMBER` |  | Patch number |
| `PATCH_MIN_VERSION` | `VARCHAR2(30)` |  | Minimum application version for the patch |
| `PATCH_STATUS` | `VARCHAR2(10)` |  | Status of the patch |
| `PATCH_COMMENT` | `VARCHAR2(4000)` |  | Comment associated with the patch |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).