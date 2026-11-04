---
title: "V$MEMORY_TARGET_ADVICE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2062.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$MEMORY_TARGET_ADVICE` provides information about how the `MEMORY_TARGET` parameter should be sized based on current sizing and satisfaction metrics.

| Column | Datatype | Description |
| --- | --- | --- |
| `MEMORY_SIZE` | `NUMBER` | If the `MEMORY_SIZE_FACTOR` column has a value of 1, then this column shows the current size of memory, as set by the `MEMORY_TARGET` initialization parameter.  If the value of the `MEMORY_SIZE_FACTOR` column is less than or greater than 1, then this column shows a proposed memory size. |
| `MEMORY_SIZE_FACTOR` | `NUMBER` | A multiplier for the current memory size. Possible values are 0.25, 0.5, 0.75, 1, 1.5, 1.75, and 2. This multiplier times the current memory size equals the value of the `MEMORY_SIZE` column. |
| `ESTD_DB_TIME` | `NUMBER` | For current memory size (`MEMORY_SIZE_FACTOR = 1`), the amount of database time required to complete the current workload. For a proposed memory size, the estimated amount of database time that would be required if the `MEMORY_TARGET` parameter were changed to the proposed size. |
| `ESTD_DB_TIME_FACTOR` | `NUMBER` | For a proposed memory size, ratio of estimated database time to current database time |
| `VERSION` | `NUMBER` | Version number of this recommendation (this snapshot of the `V$MEMORY_TARGET_ADVICE` view) |

Table 8-2 shows how the information provided in `V$MEMORY_TARGET_ADVICE` could be used to improve performance. The data indicates that if current memory size is 380M, and you were to increase it to 760M (2x), the current workload would take 80525 units of DBtime as opposed to 115475 units of DBtime, which is a significant improvement in performance.

Table 8-2 Example of Using V$MEMORY\_TARGET\_ADVICE

| MEMORY\_SIZE | MEMORY\_SIZE\_FACTOR | ESTD\_DB\_TIME | ESTD\_DB\_TIME\_FACTOR | VERSION |
| --- | --- | --- | --- | --- |
| 380 | 1 | 115475 | 1 | 3 |
| 95 | .25 | 200500 | 1.7 | 3 |
| 190 | .5 | 125600 | 1.1 | 3 |
| 760 | 2 | 80525 | 0.7 | 3 |