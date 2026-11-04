---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/USE_DEDICATED_BROKER.html
tags:
  - oracle
  - 12c
  - reference
---

`USE_DEDICATED_BROKER` determines how dedicated servers are spawned.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `False` unless multithreaded Oracle is enabled <sup>Foot 1</sup> |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | If specified, all instances must use the same value |

<sup>Footnote 1</sup>

Multithreaded Oracle is enabled by setting the `THREADED_EXECUTION` initialization parameter to `true`.

When this parameter is set to `false`, the listener spawns a dedicated server directly.

When this parameter is set to `true`, the listener hands the connection to a dedicated connection broker that spawns the dedicated server. Unlike the listener, the dedicated connection broker is a database process, and hence it can implement policies leveraging database information before the spawn.

To enable the dedicated connection broker using the `USE_DEDICATED_BROKER` initialization parameter, you must:

1. Set the `USE_DEDICATED_BROKER` initialization parameter to `true`.
2. Set the `DEDICATED_THROUGH_BROKER_` listener-name parameter to `on` in the listener.ora file.

Performing these two steps configures the Connection Broker Process (Nnnn).

Note:

When multithreaded Oracle is enabled, the dedicated connection broker process is also enabled and used.

Configuration of the brokers is controlled by the `CONNECTION_BROKERS` initialization parameter.

See Also:

- " [CONNECTION\_BROKERS](CONNECTION_BROKERS.md) " for more information about configuring brokers
- [Table F-1](background-processes.md) for more information about the Connection Broker Process (Nnnn)
- " [THREADED\_EXECUTION](THREADED_EXECUTION.md) " for more information about enabling multithreaded Oracle
- [Oracle Database Net Services Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=NETRF2101) for more information about the `DEDICATED_THROUGH_BROKER_` listener-name parameter in the listener.ora file