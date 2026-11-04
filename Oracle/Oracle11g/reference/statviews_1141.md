---
title: ALL_MINING_MODEL_SETTINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1141.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MINING_MODEL_SETTINGS` describes the settings of the mining models accessible to the current user.

Model settings can be specified in a settings table that is used as input to the model build process. The settings associated with a model are algorithm-dependent. Setting values can be provided as input to the model build process. If no values are provided, then default values are used.

Related Views

- `DBA_MINING_MODEL_SETTINGS` describes the settings of all mining models in the database.
- `USER_MINING_MODEL_SETTINGS` describes the settings of the mining models owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the mining model |
| `MODEL_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the mining model |
| `SETTING_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the setting |
| `SETTING_VALUE` | `VARCHAR2(4000)` |  | Value of the setting |
| `SETTING_TYPE` | `VARCHAR2(7)` |  | Indicates whether the default value (`DEFAULT`) or a user-specified value (`INPUT`) is used by the model |