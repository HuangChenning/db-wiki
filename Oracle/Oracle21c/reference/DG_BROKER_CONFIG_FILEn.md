---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DG_BROKER_CONFIG_FILEn.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.107 DG\_BROKER\_CONFIG\_FILEn

`DG_BROKER_CONFIG_FILE` `n` (where `n` = 1, 2) specifies the names for the Data Guard broker configuration files.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DG_BROKER_CONFIG_FILE[1 \| 2] = ` `filename` |
| Default value | Operating system-dependent |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | One filename |
| Basic | No |

Every database that is part of a Data Guard broker configuration has two broker configuration files, which contain entries that describe the state and properties of the configuration (such as the sites and databases that are part of the configuration, the roles and properties of each of the databases, and the state of each of the elements of the configuration). Two files are provided to always maintain the last known good state of the configuration.

If `DG_BROKER_CONFIG_FILE` `n` is not explicitly defined, then it is set to an operating system-specific default value at instance startup. This parameter can be altered only when the Data Guard broker is not running. See " [DG\_BROKER\_START](DG_BROKER_START.md) " for information on how to stop and start the broker.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DGBKR3393) for more information about setting this parameter