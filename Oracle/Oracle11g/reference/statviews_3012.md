---
title: DBA_ADVISOR_DEFINITIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3012.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_DEFINITIONS` displays the properties of all advisors in the database. The view contains one row for each task, representing the current state of the task as well as execution-specific data such as progress monitoring and completion status.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the advisor |
| `ADVISOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the advisor |
| `PROPERTY` | `NUMBER` | `NOT NULL` | Properties: - Bit 0: - Indicates whether the advisor runs in `COMPREHENSIVE` mode (`1`) or not (`0`) - Bit 1: - Indicates whether the advisor runs in `LIMITED` mode (`1`) or not (`0`) - Bit 2: - Indicates whether the advisor is resumable (`1`) or not (`0`) - Bit 3: - Indicates whether the advisor accepts user directives (`1`) or not (`0`) |