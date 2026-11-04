---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_WI_STATEMENTS.html
tags:
  - oracle
  - 12c
  - reference
---

Each row in `DBA_WI_STATEMENTS` describes a statement (SQL or PL/SQL) that is part of the template with identifier `TEMPLATE_ID`, which has been found in the workload that is related to the Workload Intelligence job whose identifier is equal to `JOB_ID`.

A template may consist of multiple statements, for example, if it represents a transaction. In this case, there is one row in this view for every one of these statements. These statements are ordered, based on the order defined by the corresponding transaction. Column `SEQUENCE_NUMBER` is used to describe this order.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The identifier of the job in the workload of which the given statement has been found |
| `TEMPLATE_ID` | `NUMBER` | `NOT NULL` | The identifier of the template in the given job to which the current statement belongs |
| `SEQUENCE_NUMBER` | `NUMBER` | `NOT NULL` | A number that indicates the order of the current statement in the given template |
| `SQL_TEXT` | `CLOB` | `NOT NULL` | The SQL text associated with the current statement. Note that although multiple SQL statements can be classified to the same template, only one row is stored that represents them all. This row corresponds to the first instance of the given template that is found during parsing of the workload. |