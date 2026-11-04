---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_DEFINITIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.21 DBA\_ADVISOR\_DEFINITIONS

`DBA_ADVISOR_DEFINITIONS` displays the properties of all advisors in the database.

The view contains one row for each task, representing the current state of the task as well as execution-specific data such as progress monitoring and completion status.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the advisor |
| `ADVISOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the advisor |
| `PROPERTY` | `NUMBER` | `NOT NULL` | Properties:  - Bit 0: - Indicates whether the advisor runs in `COMPREHENSIVE` mode (`1`) or not (`0`) - Bit 1: - Indicates whether the advisor runs in `LIMITED` mode (`1`) or not (`0`) - Bit 2: - Indicates whether the advisor is resumable (`1`) or not (`0`) - Bit 3: - Indicates whether the advisor accepts user directives (`1`) or not (`0`) |