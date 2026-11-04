---
title: DG_BROKER_CONFIG_FILEn
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams076.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DG_BROKER_CONFIG_FILE[1 \| 2] =` `filename` |
| Default value | Operating system-dependent |
| Modifiable | `ALTER SYSTEM` |
| Range of values | One filename |
| Basic | No |

`DG_BROKER_CONFIG_FILE` `n` (where `n` = 1, 2) specifies the names for the Data Guard broker configuration files.

Every database that is part of a Data Guard broker configuration has two broker configuration files, which contain entries that describe the state and properties of the configuration (such as the sites and databases that are part of the configuration, the roles and properties of each of the databases, and the state of each of the elements of the configuration). Two files are provided so as to always maintain the last known good state of the configuration.

If `DG_BROKER_CONFIG_FILE` `n` is not explicitly defined, then it is set to an operating system-specific default value at instance startup. The parameter can only be altered when the DMON (Data Guard broker) process is not running.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/toc.htm) for more information about setting this parameter