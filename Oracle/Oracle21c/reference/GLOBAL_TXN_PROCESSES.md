---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/GLOBAL_TXN_PROCESSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.141 GLOBAL\_TXN\_PROCESSES

`GLOBAL_TXN_PROCESSES` specifies the initial number of GTXn background processes (GTX0,... GTX9 and GTXa,... GTXj) per instance to support global (XA) transactions in an Oracle RAC environment.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to `20` |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

If you want to disable the GTXn background processes, then you must set `GLOBAL_TXN_PROCESSES` to `0` in your parameter file. Setting this parameter to `0` will disable the XA support on an Oracle RAC database. Error `ORA-55712` will be returned if you try to run XA transactions on an Oracle RAC database with this parameter set to `0`. You can change the setting to a nonzero value at run time to turn on the support for XA.

`GLOBAL_TXN_PROCESSES` is useful for systems that process global (XA) transactions heavily. You do not need to specify a value for this parameter since Oracle Database automatically determines the number of processes and autotunes them, as necessary. GTXn background processes are only seen in an Oracle RAC environment.

See Also:

[Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADFNS813) for more information about this parameter