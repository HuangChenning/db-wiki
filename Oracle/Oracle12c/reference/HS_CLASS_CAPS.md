---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/HS_CLASS_CAPS.html
tags:
  - oracle
  - 12c
  - reference
---

`HS_CLASS_CAPS` contains information about the class-specific (driver) capabilities belonging to the non-Oracle (FDS) data store.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAP_NUMBER` | `NUMBER ` | `NOT NULL` | Capability number |
| `CAP_DESCRIPTION` | `VARCHAR2(255)` |  | Capability description |
| `CONTEXT` | `NUMBER` |  | Flag indicating the context in which the capability is enabled |
| `TRANSLATION` | `VARCHAR2(255)` |  | Valid for functions; contains translation to FDS dialect |
| `ADDITIONAL_INFO` | `NUMBER` |  | Additional flags for internal use |
| `FDS_CLASS_NAME` | `VARCHAR2(30) ` | `NOT NULL` | Name of the FDS Class |
| `FDS_CLASS_ID` | `NUMBER ` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |