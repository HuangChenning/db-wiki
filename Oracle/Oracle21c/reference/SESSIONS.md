---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/SESSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.330 SESSIONS

`SESSIONS` specifies the maximum number of sessions that can be created in the system.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | Derived: (1.5 \* `PROCESSES`) + 22 |
| Modifiable | `ALTER SYSTEM` can be used in a PDB only to change the value of the `SESSIONS` parameter for that PDB.  `ALTER SYSTEM` cannot be used to change the value of the `SESSIONS` parameter in a non-CDB or in `CDB$ROOT`. |
| Modifiable in a PDB | Yes |
| Range of values | If you explicitly set a value for this parameter, then the range of values that you can specify is 1 to (2 <sup>16</sup> - 1), which is 1 to 65535.  If you do not explicitly set a value for this parameter, then it is set to the default value. If `COMPATIBLE` >= `19.0.0`, then the default value will not exceed a maximum of (2 <sup>18</sup> - 1), which is 262143. If `COMPATIBLE` < `19.0.0`, then the default value will not exceed a maximum of (2 <sup>16</sup> - 1), which is 65535. |
| Basic | Yes |

Because every login requires a session, this parameter effectively determines the maximum number of concurrent users in the system. You should always set this parameter explicitly to a value equivalent to your estimate of the maximum number of concurrent users, plus the number of background processes, plus approximately 10% for recursive sessions.

Oracle uses the default value of this parameter as its minimum. Values between 1 and the default do not trigger errors, but Oracle ignores them and uses the default instead.

The default values of the `ENQUEUE_RESOURCES` and `TRANSACTIONS` parameters are derived from `SESSIONS`. Therefore, if you increase the value of `SESSIONS`, you should consider whether to adjust the values of `ENQUEUE_RESOURCES` and `TRANSACTIONS` as well. (Note that `ENQUEUE_RESOURCES` is obsolete as of Oracle Database 10g release 2 (10.2).)

In a shared server environment, the value of `PROCESSES` can be quite small. Therefore, Oracle recommends that you adjust the value of `SESSIONS` to approximately 1.1 \* total number of connections.

For a CDB, the root container's `SESSIONS` parameter specifies the total number of sessions for the database.

The `SESSIONS` parameter for a PDB specifies the total number of sessions that can be used by that PDB. Its value defaults to the root container's `SESSIONS` value. If the PDB tries to use more sessions than configured by its `SESSIONS` parameter, an `ORA-00018` error message is generated. For PDBs, the SESSIONS parameter does not count recursive sessions and hence does not require the 10% adjustment.

The `SESSIONS` parameter for a PDB can only be modified by the PDB. It cannot be set higher than the CDB's `SESSIONS` value.

See Also:

- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT7776) for more information on memory structures
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT008) for more information on processes
- [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=MULTI-GUID-AB84D6C9-4BBE-4D36-992F-2BB85739329F) for more information about CDBs and PDBs