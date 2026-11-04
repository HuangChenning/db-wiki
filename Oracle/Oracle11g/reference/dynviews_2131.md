---
title: "V$REPLPROP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2131.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$REPLPROP` displays information about the parallel propagation currently in progress at the replication site. Use this view to determine which transactions are currently being propagated, the number of calls propagated in each transaction, and the current activity of the parallel propagation slave processes or parallel propagation coordinator process.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier |
| `SERIAL#` | `NUMBER` | Session serial number. Used to identify uniquely a session's objects. Guarantees that session-level commands are applied to the correct session objects if the session ends with, and another session begins with, the same session ID. |
| `NAME` | `VARCHAR2(71)` | Name of the propagation session: - `Replication Parallel Prop Slave` `n` - Slave process `n` is active, either waiting, pushing deferred transactions, purging metadata, or creating an error transaction - `Replication Parallel Prop Coordinator` - Coordinator process is active, and either waiting, sleeping, or scheduling slaves to perform operations  The coordinator process reads transactions from the deferred transaction queue and assigns them to the slave processes. Then, the slaves propagate the transactions to the destination site. When the slaves push transactions in a push session, the slaves remain active until the push session completes, even if there are no more transactions to push. |
| `DBLINK` | `VARCHAR2(128)` | Database link on which this replication session is propagating |
| `STATE` | `VARCHAR2(12)` | State of the propagation session: - `WAIT` - Slave processes or the coordinator process is waiting for an event (that is, a message) - `SLEEP` - Coordinator process is sleeping for the duration of the `delay_seconds` setting. 	Note: `delay_seconds` is set with the `DBMS_DEFER_SYS.SCHEDULE_PUSH` procedure. - `PUSH` - Slave processes are pushing transactions from the deferred transaction queue to the remote site - `PURGE` - Slave processes are purging metadata related to successfully applied transactions from the remote site - `CREATE ERROR` - Slave processes are creating an error transaction. In this case, an error or a conflict occurred while the slaves were pushing deferred transactions to the remote site. - `SCHEDULE TXN` - Coordinator process is determining the order that transactions are applied and assigning slave processes to execute the transactions |
| `XID` | `VARCHAR2(22)` | If the session is a slave session, then indicates the transaction id of the transaction that the slave is currently propagating. |
| `SEQUENCE` | `NUMBER` | If the process is a slave process, then indicates the sequence number of the calls propagated in the current operation, if relevant. Each transaction must process one or more calls, and the value of `SEQUENCE` starts at zero and increases as each call is processed. The `SEQUENCE` value shows the call that is currently being processed in each transaction. This value increases until the slave has processed all of the calls in a transaction. |

Note:

This view only contains data when deferred transactions are being pushed using parallel propagation at the current site. The `parallelism` parameter must be set to `1` or higher in the `DBMS_DEFER_SYS.PUSH` function for a push to use parallel propagation. Otherwise, the push uses serial propagation, and no data appears in this view during the push.