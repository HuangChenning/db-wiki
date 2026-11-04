---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WI_TEMPLATES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.115 DBA\_WI\_TEMPLATES

Each row in `DBA_WI_TEMPLATES` describes a template that has been found in the workload that is related to the Workload Intelligence job whose identifier is equal to `JOB_ID`.

A template can represent either a simple query, or an entire transaction. Two queries in the given workload belong to the same template, if they exhibit trivial differences, for example, if they contain different literal values, different bind variable names, different comments, or different white spaces.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `JOB_ID` | `NUMBER` | `NOT NULL` | The identifier of the job in the workload of which the given template has been found |
| `TEMPLATE_ID` | `NUMBER` | `NOT NULL` | The identifier of a template in a given job |
| `IS_TRANSACTION` | `CHAR(1)` | `NOT NULL` | Flag that indicates whether the given template represents a transaction:  - `Y` - indicates that the given template represents a transaction - `N` - indicates that the given template does not represent a transaction |