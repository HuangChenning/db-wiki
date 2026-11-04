---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ASM_IO_PROCESSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.20 ASM\_IO\_PROCESSES

`ASM_IO_PROCESSES` specifies the number of I/O worker processes to be started in an Oracle IOServer instance.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `20` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `1` – `32` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

This parameter is applicable only in an Oracle IOServer instance, which runs out of an Oracle Grid Infrastructure home.

The default value should work in most cases. However, under heavy I/O load, there may be some delays associated with posting processes out of I/O waits. In this case, a slightly higher value than the default may be appropriate.