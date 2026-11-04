---
title: HS_CLASS_CAPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5133.htm
tags:
  - oracle
  - 11g
  - reference
---

`HS_CLASS_CAPS` contains information about the class-specific (driver) capabilities belonging to the non-Oracle (FDS) data store.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAP_NUMBER` | `NUMBER` | `NOT NULL` | Capability number |
| `CAP_DESCRIPTION` | `VARCHAR2(255)` |  | Capability description |
| `CONTEXT` | `NUMBER` |  | Flag indicating the context in which the capability is enabled |
| `TRANSLATION` | `VARCHAR2(255)` |  | Valid for functions; contains translation to FDS dialect |
| `ADDITIONAL_INFO` | `NUMBER` |  | Additional flags for internal use |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the FDS Class |
| `FDS_CLASS_ID` | `NUMBER` | `NOT NULL` | Sequence: a counter that is incremented for every row inserted (used internally) |