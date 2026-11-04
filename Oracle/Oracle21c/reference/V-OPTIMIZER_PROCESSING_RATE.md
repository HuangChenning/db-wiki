---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OPTIMIZER_PROCESSING_RATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.104 V$OPTIMIZER\_PROCESSING\_RATE

`V$OPTIMIZER_PROCESSING_RATE` displays the processing rates used by the optimizer to compute degree of parallelism.

Note:

You can manipulate these rates using these procedures for the `DBMS_STATS` package:

- `SET_PROCESSING_RATE`
- `DELETE_PROCESSING_RATE`
- `GATHER_PROCESSING_RATE`

See [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS059) for more information about the `DBMS_STATS` package.

| Column | Datatype | Description |
| --- | --- | --- |
| `ADDRESS` | `RAW(4\| 8)` | Address of the handle to the parent for this cursor |
| `OPERATION_NAME` | `VARCHAR2(64)` | Name of the operation. The possible values are `AGGR`, `ALL`, `CPU`, `CPU_ACCESS`, `CPU_AGGR`, `CPU_BYTES_PER_SEC`, `CPU_FILTER`, `CPU_GBY`, `CPU_HASH_JOIN`, `CPU_JOIN`, `CPU_NL_JOIN`, `CPU_RANDOM_ACCESS`, `CPU_ROWS_PER_SEC`, `CPU_SEQUENTIAL_ACCESS`, `CPU_SM_JOIN`, `CPU_SORT`, `HASH`, `IO`, `IO_ACCESS`, `IO_BYTES_PER_SEC`, `IO_RANDOM_ACCESS`, `IO_ROWS_PER_SEC`, `IO_SEQUENTIAL_ACCESS`, `MEMCMP`, `MEMCPY` |
| `MANUAL_VALUE` | `VARCHAR2(10)` | Value of the operation set manually by the user |
| `CALIBRATION_VALUE` | `VARCHAR2(10)` | Value of the operation obtained from calibration (by running the `GATHER_PROCESSING_RATE` procedure) |
| `DEFAULT_VALUE` | `VARCHAR2(10)` | Default value of the operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |