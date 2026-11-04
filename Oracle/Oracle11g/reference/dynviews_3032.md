---
title: "V$SGA_DYNAMIC_FREE_MEMORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3032.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SGA_DYNAMIC_FREE_MEMORY` displays information about the amount of SGA memory available for future dynamic SGA resize operations.

| Column | Datatype | Description |
| --- | --- | --- |
| `CURRENT_SIZE` | `NUMBER` | Amount of available memory (in bytes) |