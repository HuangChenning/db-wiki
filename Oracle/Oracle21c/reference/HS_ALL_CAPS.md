---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/HS_ALL_CAPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.192 HS\_ALL\_CAPS

`HS_ALL_CAPS` contains information about all of the capabilities (that is, features) associated with non-Oracle (FDS) data stores.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAP_NUMBER` | `NUMBER` |  | Capability number |
| `CONTEXT` | `NUMBER` |  | Context in which this capability is applicable |
| `TRANSLATION` | `VARCHAR2(255)` |  | Valid for functions; contains translation to FDS dialect |
| `ADDITIONAL_INFO` | `NUMBER` |  | Flag for internal use |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` |  | Name of the FDS Class |
| `FDS_INST_NAME` | `VARCHAR2(30)` |  | Name of the FDS instance |