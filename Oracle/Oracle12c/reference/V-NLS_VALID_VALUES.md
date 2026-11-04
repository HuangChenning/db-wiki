---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-NLS_VALID_VALUES.html
tags:
  - oracle
  - 12c
  - reference
---

`V$NLS_VALID_VALUES` lists all valid values for NLS parameters.

| Column | Datatype | Description |
| --- | --- | --- |
| `PARAMETER` | `VARCHAR2(64)` | Parameter name (`LANGUAGE` \| `SORT` \| `TERRITORY` \| `CHARACTERSET`) |
| `VALUE` | `VARCHAR2(64)` | NLS parameter value |
| `ISDEPRECATED` | `VARCHAR2(5)` | Indicates whether the parameter has been deprecated (`TRUE`) or not (`FALSE`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |