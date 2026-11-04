---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MINING_MODEL_SETTINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.275 ALL\_MINING\_MODEL\_SETTINGS

`ALL_MINING_MODEL_SETTINGS` describes the settings of the machine learning models accessible to the current user.

Machine learning models are schema objects created by Oracle Machine Learning for SQL.

Related Views

- `DBA_MINING_MODEL_SETTINGS` describes the settings of all machine learning models in the database.
- `USER_MINING_MODEL_SETTINGS` describes the settings of the machine learning models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the machine learning model |
| `MODEL_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the machine learning model |
| `SETTING_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the setting |
| `SETTING_VALUE` | `VARCHAR2(4000)` | – | Value of the setting |
| `SETTING_TYPE` | `VARCHAR2(7)` | – | Indicates whether the default value (`DEFAULT`) or a user-specified value (`INPUT`) is used by the model |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS608) for descriptions of model settings