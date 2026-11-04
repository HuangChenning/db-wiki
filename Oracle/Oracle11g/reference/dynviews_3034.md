---
title: "V$SGA_TARGET_ADVICE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3034.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SGA_TARGET_ADVICE` displays information about the `SGA_TARGET` initialization parameter.

| Column | Datatype | Description |
| --- | --- | --- |
| `SGA_SIZE` | `NUMBER` | Size of the SGA |
| `SGA_SIZE_FACTOR` | `NUMBER` | Ratio between the SGA\_SIZE and the current size of the SGA |
| `ESTD_DB_TIME` | `NUMBER` | Estimated DB\_TIME for this SGA\_SIZE |
| `ESTD_DB_TIME_FACTOR` | `NUMBER` | Ratio between ESTD\_DB\_TIME and DB\_TIME for the current size of the SGA |
| `ESTD_PHYSICAL_READS` | `NUMBER` | Estimated number of physical reads |