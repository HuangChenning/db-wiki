---
title: "V$RMAN_COMPRESSION_ALGORITHM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2145.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RMAN_COMPRESSION_ALGORITHM` provides descriptions of supported compression algorithms. It is used by the RMAN client.

| Column | Datatype | Description |
| --- | --- | --- |
| `ALGORITHM_ID` <sup>Foot 1</sup> | `NUMBER` | Algorithm ID |
| `ALGORITHM_NAME` | `VARCHAR2(64)` | Name of the algorithm (for example, `LOW`, `MEDIUM`, `DEFAULT`, or `HIGH`) |
| `INITIAL_RELEASE` | `VARCHAR2(18)` | First Oracle Database release when this compression algorithm was available |
| `TERMINAL_RELEASE` | `VARCHAR2(18)` | Last Oracle Database release that supported using this compression algorithm to create new backups. Existing backups can always be restored, even if they use a deprecated compression algorithm. |
| `ALGORITHM_DESCRIPTION` | `VARCHAR2(64)` | Description of the algorithm |
| `ALGORITHM_COMPATIBILITY` | `VARCHAR2(18)` | Required database compatibility level for the algorithm (for example, 11.2.0 for `DEFAULT`) |
| `IS_VALID` | `VARCHAR2(3)` | Indicates whether the algorithm is valid with regard to the compatibility setting (`YES`) or not (`NO`). The value is `YES` if `ALGORITHM_COMPATIBILITY` <= `DATABASE_COMPATIBILITY`. |
| `REQUIRES_ACO` | `VARCHAR2(3)` | Indicates whether the algorithm requires the Advanced Compression Option (`YES`) or not (`NO`) |
| `IS_DEFAULT` <sup>Footref 1</sup> | `VARCHAR2(3)` | Indicates whether the algorithm is the default compression algorithm that RMAN uses to create compressed backup sets (`YES`) or not (`NO`) |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).