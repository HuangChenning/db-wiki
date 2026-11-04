---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RMAN_COMPRESSION_ALGORITHM.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.178 V$RMAN\_COMPRESSION\_ALGORITHM

`V$RMAN_COMPRESSION_ALGORITHM` provides descriptions of supported compression algorithms. It is used by the RMAN client.

| Column | Datatype | Description |
| --- | --- | --- |
| `ALGORITHM_ID` | `NUMBER` | Algorithm ID |
| `ALGORITHM_NAME` | `VARCHAR2(64)` | Name of the algorithm (for example, `LOW`, `MEDIUM`, `DEFAULT`, or `HIGH`) |
| `INITIAL_RELEASE` | `VARCHAR2(18)` | First Oracle Database release when this compression algorithm was available |
| `TERMINAL_RELEASE` | `VARCHAR2(18)` | Last Oracle Database release that supported using this compression algorithm to create new backups. Existing backups can always be restored, even if they use a deprecated compression algorithm. |
| `ALGORITHM_DESCRIPTION` | `VARCHAR2(64)` | Description of the algorithm |
| `ALGORITHM_COMPATIBILITY` | `VARCHAR2(18)` | Required database compatibility level for the algorithm (for example, 11.2.0 for `DEFAULT`) |
| `IS_VALID` | `VARCHAR2(3)` | Indicates whether the algorithm is valid with regard to the compatibility setting (`YES`) or not (`NO`). The value is `YES` if `ALGORITHM_COMPATIBILITY` <= `DATABASE_COMPATIBILITY`. |
| `REQUIRES_ACO` | `VARCHAR2(3)` | Indicates whether the algorithm requires the Advanced Compression Option (`YES`) or not (`NO`) |
| `IS_DEFAULT` | `VARCHAR2(3)` | Indicates whether the algorithm is the default compression algorithm that RMAN uses to create compressed backup sets (`YES`) or not (`NO`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |