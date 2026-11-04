---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_DIR_DEFINITIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.22 DBA\_ADVISOR\_DIR\_DEFINITIONS

`DBA_ADVISOR_DIR_DEFINITIONS` provides a definition of the base directive.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` | `NOT NULL` | Unique id for directive. The directive management engine automatically generates ID numbers. The identifier is unique among all directives regardless of the domain name and directive name. |
| `ADVISOR_ID` | `NUMBER` | `NOT NULL` | Identifier number of the owner advisor. |
| `ADVISOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of the advisor to which this directive belongs. |
| `DIRECTIVE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| `DOMAIN_NAME` | `VARCHAR2(128)` | `NOT NULL` | Domain or namespace name. |
| `DESCRIPTION` | `VARCHAR2(256)` | `NOT NULL` | An optional description that documents the purpose of the directive. |
| `TYPE` | `NUMBER` | `NOT NULL` | Further describes the use of the directive. Possible values are:  1. Filter - An Xpath filter 2. Single Value - Evaluation returns a single string value 3. Multiple Values - Evaluation returns one to many string values 4. Conditional - Evaluation returns a single value based on an input key, similar to a `CASE` or `SWITCH` statement |
| `TYPE_NAME` | `VARCHAR2(15)` |  | A decoded version of the `TYPE` column. |
| `TASK_STATUS` | `VARCHAR2(9)` |  | The status of the directive instances when a task is not in its initial state. Possible values are:  - `IMMUTABLE` - `MUTABLE` |
| `INSTANCES` | `VARCHAR2(8)` |  | Indicates whether a directive will permit multiple instances. Possible values are:  - `SINGLE` - `MULTIPLE` |
| `METADATA` | `CLOB` | `NOT NULL` | A DTD that is used to process the directive. |