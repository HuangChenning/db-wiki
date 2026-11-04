---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/PRODUCT_COMPONENT_VERSION.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.217 PRODUCT\_COMPONENT\_VERSION

`PRODUCT_COMPONENT_VERSION` contains version and status information for component products.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PRODUCT` | `VARCHAR2(80)` |  | Product name |
| `VERSION` | `VARCHAR2(80)` |  | Version number |
| `VERSION_FULL` | `VARCHAR2(160)` |  | The version number with the new Oracle Database version scheme introduced in Oracle Database 18c. The version number is displayed only for the database component. All other components return a null value for this column. |
| `STATUS` | `VARCHAR2(80)` |  | Status of release |