---
title: HS_ALL_CAPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5128.htm
tags:
  - oracle
  - 11g
  - reference
---

`HS_ALL_CAPS` contains information about all of the capabilities (that is, features) associated with non-Oracle (FDS) data stores.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAP_NUMBER` | `NUMBER` |  | Capability number |
| `CONTEXT` | `NUMBER` |  | Context in which this capability is applicable |
| `TRANSLATION` | `VARCHAR2(255)` |  | Valid for functions; contains translation to FDS dialect |
| `ADDITIONAL_INFO` | `NUMBER` |  | Flag for internal use |
| `FDS_CLASS_NAME` | `VARCHAR2(30)` |  | Name of the FDS Class |
| `FDS_INST_NAME` | `VARCHAR2(30)` |  | Name of the FDS instance |