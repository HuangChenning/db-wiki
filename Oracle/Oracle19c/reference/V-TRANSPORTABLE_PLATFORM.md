---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-TRANSPORTABLE_PLATFORM.html
tags:
  - oracle
  - 19c
  - reference
---

## 9.123 V$TRANSPORTABLE\_PLATFORM

Specifically, it lists all platforms supported by the RMAN `CONVERT TABLESPACE` command, along with the endianness of each platform.

| Column | Datatype | Description |
| --- | --- | --- |
| `PLATFORM_ID` | `NUMBER` | Platform identification number |
| `PLATFORM_NAME` | `VARCHAR2(101)` | Platform name |
| `ENDIAN_FORMAT` | `VARCHAR2(14)` | Platform endian format:  - `Big` - `Little` - `UNKNOWN FORMAT` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |