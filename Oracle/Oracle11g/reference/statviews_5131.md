---
title: HS_BASE_CAPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5131.htm
tags:
  - oracle
  - 11g
  - reference
---

`HS_BASE_CAPS` contains information about base capability (that is, base features) of the non-Oracle (FDS) data store.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CAP_NUMBER` | `NUMBER` | `NOT NULL` | Capability number |
| `CAP_DESCRIPTION` | `VARCHAR2(255)` |  | Description of the capability |