---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_APP_PATCHES.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.107 DBA\_APP\_PATCHES

`DBA_APP_PATCHES` describes all the application patches in the application container.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `APP_NAME` | `VARCHAR2(128)` |  | Name of the application |
| `PATCH_NUMBER` | `NUMBER` |  | Patch number |
| `PATCH_MIN_VERSION` | `VARCHAR2(30)` |  | Minimum application version for the patch |
| `PATCH_STATUS` | `VARCHAR2(10)` |  | Status of the patch |
| `PATCH_COMMENT` | `VARCHAR2(4000)` |  | Comment associated with the patch |
| `PATCH_CHECKSUM` | `NUMBER` |  | Checksum for the patch |