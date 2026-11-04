---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BGPROCESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.107 V$BGPROCESS

`V$BGPROCESS` displays information about the background processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `PADDR` | `RAW(4 \| 8)` | Address of the process state object |
| `PSERIAL#` | `NUMBER` | Process state object serial number |
| `NAME` | `VARCHAR2(5)` | Name of this background process |
| `DESCRIPTION` | `VARCHAR2(64)` | Description of the background process |
| `ERROR` | `NUMBER` | Error encountered |
| `TYPE` | `VARCHAR2(5)` | This column has a value of `SLAVE` for all background worker processes, otherwise it is null. |
| `PRIORITY` | `VARCHAR2(8)` | Lists the current priority with which the process is running. This column has string values based on the operating system. On Linux, the values that can appear in this column are:  - `TS`: Time sharing - `RT`: Real time priority |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |