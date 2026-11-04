---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/SESSIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`SESSIONS` specifies the maximum number of sessions that can be created in the system.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived: (1.5 \* `PROCESSES`) + 22 |
| Modifiable | `ALTER SYSTEM` can be used in a PDB only to change the value of the `SESSIONS` parameter for that PDB.  `ALTER SYSTEM` cannot be used to change the value of the `SESSIONS` parameter in a non-CDB or in a CDB$ROOT. |
| Modifiable in a PDB | Yes |
| Range of values | 1 to 2 <sup>16</sup> (which is 1 to 65536) |
| Basic | Yes |

Because every login requires a session, this parameter effectively determines the maximum number of concurrent users in the system. You should always set this parameter explicitly to a value equivalent to your estimate of the maximum number of concurrent users, plus the number of background processes, plus approximately 10% for recursive sessions.

Oracle uses the default value of this parameter as its minimum. Values between 1 and the default do not trigger errors, but Oracle ignores them and uses the default instead.

The default values of the `ENQUEUE_RESOURCES` and `TRANSACTIONS` parameters are derived from `SESSIONS`. Therefore, if you increase the value of `SESSIONS`, you should consider whether to adjust the values of `ENQUEUE_RESOURCES` and `TRANSACTIONS` as well. (Note that `ENQUEUE_RESOURCES` is obsolete as of Oracle Database 10g release 2 (10.2).)

In a shared server environment, the value of `PROCESSES` can be quite small. Therefore, Oracle recommends that you adjust the value of `SESSIONS` to approximately 1.1 \* total number of connections.

For a CDB, the root container's `SESSIONS` parameter specifies the total number of sessions for the database.

The `SESSIONS` parameter for a PDB specifies the total number of sessions that can be used by that PDB. Its value defaults to the root container's `SESSIONS` value. If the PDB tries to use more sessions than configured by its `SESSIONS` parameter, an `ORA-00018` error message is generated. For PDBs, the SESSIONS parameter does not count recursive sessions and hence does not require the 10% adjustment.

The `SESSIONS` parameter for a PDB can only be modified by the PDB. It cannot be set higher than the CDB's `SESSIONS` value.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT7776) for more information on memory structures
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT008) for more information on processes
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=CNCPT89235) for more information about CDBs and PDBs