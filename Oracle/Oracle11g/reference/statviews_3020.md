---
title: DBA_ADVISOR_FINDING_NAMES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3020.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_FINDING_NAMES` provides a list of all finding names registered with the Advisor Framework.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` |  | ID of the finding name |
| `ADVISOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Advisor name |
| `FINDING_NAME` | `VARCHAR2(4000)` |  | Finding name |