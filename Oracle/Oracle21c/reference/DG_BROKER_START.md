---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DG_BROKER_START.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.108 DG\_BROKER\_START

`DG_BROKER_START` enables Oracle to determine whether the Oracle Data Guard broker should be started.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM...SID=’*’` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |

The Oracle Data Guard broker consists of background processes, foreground processes, and the system global area (SGA). The background and foreground processes exist as long as the instance exists, whenever this parameter is set to `true`.

If the database is never going to be configured in an Oracle Data Guard broker configuration, then you can leave this parameter unspecified and accept the default value of `false`. If the database is part of an Oracle Data Guard broker configuration, then you can simplify automatic startup of the broker by setting this parameter to `true` in the initialization parameter file.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DGBKR115) for examples of using this parameter to start the Oracle Data Guard broker