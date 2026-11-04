---
title: DBA_STREAMS_TRANSFORMATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5027.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_STREAMS_TRANSFORMATIONS` displays information about all transformations available on a system, in order of execution.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RULE_OWNER` | `VARCHAR2(30)` |  | Owner of the rule |
| `RULE_NAME` | `VARCHAR2(30)` |  | Name of the rule |
| `TRANSFORM_TYPE` | `VARCHAR2(26)` |  | Type of the transformation: |
| `FROM_SCHEMA_NAME` | `VARCHAR2(30)` |  | Schema to be renamed |
| `TO_SCHEMA_NAME` | `VARCHAR2(30)` |  | New schema name |
| `FROM_TABLE_NAME` | `VARCHAR2(30)` |  | Table to be renamed |
| `TO_TABLE_NAME` | `VARCHAR2(30)` |  | New table name |
| `SCHEMA_NAME` | `VARCHAR2(30)` |  | Schema of the column to be modified |
| `TABLE_NAME` | `VARCHAR2(30)` |  | Table of the column to be modified |
| `FROM_COLUMN_NAME` | `VARCHAR2(4000)` |  | Column to be renamed |
| `TO_COLUMN_NAME` | `VARCHAR2(4000)` |  | New column name |
| `COLUMN_NAME` | `VARCHAR2(4000)` |  | Column to add or delete |
| `COLUMN_VALUE` | `ANYDATA` |  | Value of the column to add |
| `COLUMN_TYPE` | `VARCHAR2(4000)` |  | Type of the new column |
| `COLUMN_FUNCTION` | `VARCHAR2(30)` |  | Name of the default function used to add a column |
| `VALUE_TYPE` | `VARCHAR2(3)` |  | Indicates whether to modify the old (`OLD`), new (`NEW`), or both (`*`) values of the LCR |
| `USER_FUNCTION_NAME` | `VARCHAR2(4000)` |  | Name of the user-defined transformation function to run |
| `SUBSETTING_OPERATION` | `VARCHAR2(6)` |  | DML operation for row subsetting: |
| `DML_CONDITION` | `VARCHAR2(4000)` |  | Row subsetting condition |
| `DECLARATIVE_TYPE` | `VARCHAR2(13)` |  | Type of declarative transform: |
| `PRECEDENCE` | `NUMBER` |  | Execution order relative to other declarative transformations on the same `STEP_NUMBER` |
| `STEP_NUMBER` | `NUMBER` |  | Order in which this transformation should be executed |