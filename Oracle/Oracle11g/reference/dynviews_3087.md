---
title: "V$SYS_OPTIMIZER_ENV"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3087.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SYS_OPTIMIZER_ENV` displays the contents of the optimizer environment for the instance. The optimizer environment stores the value of the main parameters used by the Oracle optimizer when building the execution plan of a SQL statement. Hence, modifying the value of one or more of these parameters (for example, by issuing an `ALTER SYSTEM` statement) could lead to plan changes.

The parameters displayed by this view are either regular initialization parameters (such as `OPTIMIZER_FEATURES_ENABLE`) or pseudo parameters (such as `ACTIVE_INSTANCE_COUNT`).

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Unique identifier of the parameter in the optimizer environment |
| `NAME` | `VARCHAR2(40)` | Name of the parameter |
| `SQL_FEATURE` | `VARCHAR2(64)` | Associated feature control ID |
| `ISDEFAULT` | `VARCHAR2(3)` | Indicates whether the parameter is set to the default value (`YES`) or not (`NO`) |
| `VALUE` | `VARCHAR2(25)` | Value of the parameter |
| `DEFAULT_VALUE` | `VARCHAR2(25)` | Default value of the parameter |