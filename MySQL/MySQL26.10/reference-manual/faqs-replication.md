---
title: "MySQL :: MySQL 26.10 Reference Manual :: A.14 MySQL 26.10 FAQ: Replication"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/faqs-replication.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

## A.14 MySQL 26.10 FAQ: Replication

In the following section, we provide answers to questions that are most frequently asked about MySQL Replication.

A.14.1. Must the replica be connected to the source all the time?

A.14.2. Must I enable networking on my source and replica to enable replication?

A.14.3. How do I know how late a replica is compared to the source? In other words, how do I know the date of the last statement replicated by the replica?

A.14.4. How do I force the source to block updates until the replica catches up?

A.14.5. What issues should I be aware of when setting up two-way replication?

A.14.6. How can I use replication to improve performance of my system?

A.14.7. What should I do to prepare client code in my own applications to use performance-enhancing replication?

A.14.8. When and how much can MySQL replication improve the performance of my system?

A.14.9. How can I use replication to provide redundancy or high availability?

A.14.10. How do I tell whether a replication source server is using statement-based or row-based binary logging format?

A.14.11. How do I tell a replica to use row-based replication?

A.14.12. How do I prevent GRANT and REVOKE statements from replicating to replica machines?

A.14.13. Does replication work on mixed operating systems (for example, the source runs on Linux while replicas run on macOS and Windows)?

A.14.14. Does replication work on mixed hardware architectures (for example, the source runs on a 64-bit machine while replicas run on 32-bit machines)?

| **A.14.1.** | Must the replica be connected to the source all the time? |
| --- | --- |
|  | No, it does not. The replica can go down or stay disconnected for hours or even days, and then reconnect and catch up on updates. For example, you can set up a source/replica relationship over a dial-up link where the link is up only sporadically and for short periods of time. The implication of this is that, at any given time, the replica is not guaranteed to be in synchrony with the source unless you take some special measures.  To ensure that catchup can occur for a replica that has been disconnected, you must not remove binary log files from the source that contain information that has not yet been replicated to the replicas. Asynchronous replication can work only if the replica is able to continue reading the binary log from the point where it last read events. |
| **A.14.2.** | Must I enable networking on my source and replica to enable replication? |
|  | Yes, networking must be enabled on the source and replica. If networking is not enabled, the replica cannot connect to the source and transfer the binary log. Verify that the [`skip_networking`](server-system-variables.md) system variable has not been enabled in the configuration file for either server. |
| **A.14.3.** | How do I know how late a replica is compared to the source? In other words, how do I know the date of the last statement replicated by the replica? |
|  | Check the `Seconds_Behind_Master` column in the output from [`SHOW         REPLICA \| SLAVE STATUS`](show-replica-status.md). See [Section 19.1.7.1, “Checking Replication Status”](replication-administration-status.md).  When the replication SQL thread executes an event read from the source, it modifies its own time to the event timestamp. (This is why [`TIMESTAMP`](datetime.md) is well replicated.) In the `Time` column in the output of [`SHOW PROCESSLIST`](show-processlist.md), the number of seconds displayed for the replication SQL thread is the number of seconds between the timestamp of the last replicated event and the real time of the replica machine. You can use this to determine the date of the last replicated event. Note that if your replica has been disconnected from the source for one hour, and then reconnects, you may immediately see large `Time` values such as 3600 for the replication SQL thread in [`SHOW PROCESSLIST`](show-processlist.md). This is because the replica is executing statements that are one hour old. See [Section 19.2.3, “Replication Threads”](replication-threads.md). |
| **A.14.4.** | How do I force the source to block updates until the replica catches up? |
|  | Use the following procedure:  1. On the source, execute these statements: 	```sql 	mysql> FLUSH TABLES WITH READ LOCK; 	mysql> SHOW MASTER STATUS; 	``` 	Record the replication coordinates (the current binary log file name and position) from the output of the [`SHOW`](show.md) statement. 2. On the replica, issue the following statement, where the arguments to the [`SOURCE_POS_WAIT()`](replication-functions-synchronization.md) or [`MASTER_POS_WAIT()`](replication-functions-synchronization.md) function are the replication coordinate values obtained in the previous step: 	```sql 	mysql> SELECT MASTER_POS_WAIT('log_name', log_pos); 	Or from MySQL 8.0.26: 	mysql> SELECT SOURCE_POS_WAIT('log_name', log_pos); 	``` 	The [`SELECT`](select.md) statement blocks until the replica reaches the specified log file and position. At that point, the replica is in synchrony with the source and the statement returns. 3. On the source, issue the following statement to enable the source to begin processing updates again: 	```sql 	mysql> UNLOCK TABLES; 	``` |
| **A.14.5.** | What issues should I be aware of when setting up two-way replication? |
|  | MySQL replication currently does not support any locking protocol between source and replica to guarantee the atomicity of a distributed (cross-server) update. In other words, it is possible for client A to make an update to co-source 1, and in the meantime, before it propagates to co-source 2, client B could make an update to co-source 2 that makes the update of client A work differently than it did on co-source 1. Thus, when the update of client A makes it to co-source 2, it produces tables that are different from what you have on co-source 1, even after all the updates from co-source 2 have also propagated. This means that you should not chain two servers together in a two-way replication relationship unless you are sure that your updates can safely happen in any order, or unless you take care of mis-ordered updates somehow in the client code.  You should also realize that two-way replication actually does not improve performance very much (if at all) as far as updates are concerned. Each server must do the same number of updates, just as you would have a single server do. The only difference is that there is a little less lock contention because the updates originating on another server are serialized in one replication thread. Even this benefit might be offset by network delays. |
| **A.14.6.** | How can I use replication to improve performance of my system? |
|  | Set up one server as the source and direct all writes to it. Then configure as many replicas as you have the budget and rackspace for, and distribute the reads among the source and the replicas. |
| **A.14.7.** | What should I do to prepare client code in my own applications to use performance-enhancing replication? |
|  | See the guide to using replication as a scale-out solution, [Section 19.4.5, “Using Replication for Scale-Out”](replication-solutions-scaleout.md). |
| **A.14.8.** | When and how much can MySQL replication improve the performance of my system? |
|  | MySQL replication is most beneficial for a system that processes frequent reads and infrequent writes. In theory, by using a single-source/multiple-replica setup, you can scale the system by adding more replicas until you either run out of network bandwidth, or your update load grows to the point that the source cannot handle it.  To determine how many replicas you can use before the added benefits begin to level out, and how much you can improve performance of your site, you must know your query patterns, and determine empirically by benchmarking the relationship between the throughput for reads and writes on a typical source and a typical replica. The example here shows a rather simplified calculation of what you can get with replication for a hypothetical system. Let `reads` and `writes` denote the number of reads and writes per second, respectively.  Let's say that system load consists of 10% writes and 90% reads, and we have determined by benchmarking that `reads` is 1200 - 2 \* `writes`. In other words, the system can do 1,200 reads per second with no writes, the average write is twice as slow as the average read, and the relationship is linear. Suppose that the source and each replica have the same capacity, and that we have one source and *`N`* replicas. Then we have for each server (source or replica):  `reads` = 1200 - 2 \* `writes`  `reads` = 9 \* `writes` / (*`N`* + 1) (reads are split, but writes replicated to all replicas)  9 \* `writes` / (*`N`* + 1) + 2 \* `writes` = 1200  `writes` = 1200 / (2 + 9/(*`N`* + 1))  The last equation indicates the maximum number of writes for *`N`* replicas, given a maximum possible read rate of 1,200 per second and a ratio of nine reads per write.  This analysis yields the following conclusions:  - If *`N`* = 0 (which means we have no replication), our system can handle about 1200/11 = 109 writes per second. - If *`N`* = 1, we get up to 184 writes per second. - If *`N`* = 8, we get up to 400 writes per second. - If *`N`* = 17, we get up to 480 writes per second. - Eventually, as *`N`* approaches infinity (and our budget negative infinity), we can get very close to 600 writes per second, increasing system throughput about 5.5 times. However, with only eight servers, we increase it nearly four times.  These computations assume infinite network bandwidth and neglect several other factors that could be significant on your system. In many cases, you may not be able to perform a computation similar to the one just shown that accurately predicts what happens on your system if you add *`N`* replicas. However, answering the following questions should help you decide whether and by how much replication may improve the performance of your system:  - What is the read/write ratio on your system? - How much more write load can one server handle if you reduce the reads? - For how many replicas do you have bandwidth available on your network? |
| **A.14.9.** | How can I use replication to provide redundancy or high availability? |
|  | How you implement redundancy is entirely dependent on your application and circumstances. High-availability solutions (with automatic failover) require active monitoring and either custom scripts or third party tools to provide the failover support from the original MySQL server to the replica.  To handle the process manually, you should be able to switch from a failed source to a pre-configured replica by altering your application to talk to the new server or by adjusting the DNS for the MySQL server from the failed server to the new server.  For more information and some example solutions, see [Section 19.4.8, “Switching Sources During Failover”](replication-solutions-switch.md). |
| **A.14.10.** | How do I tell whether a replication source server is using statement-based or row-based binary logging format? |
|  | Check the value of the [`binlog_format`](replication-options-binary-log.md) system variable:  ```sql mysql> SHOW VARIABLES LIKE 'binlog_format'; ```  The value shown is always one of `STATEMENT`, `ROW`, or `MIXED`. For `MIXED` mode, statement-based logging is used by default but replication switches automatically to row-based logging under certain conditions, such as unsafe statements. For information about when this may occur, see [Section 7.4.4.3, “Mixed Binary Logging Format”](binary-log-mixed.md). |
| **A.14.11.** | How do I tell a replica to use row-based replication? |
|  | Replicas automatically know which format to use. |
| **A.14.12.** | How do I prevent [`GRANT`](grant.md) and [`REVOKE`](revoke.md) statements from replicating to replica machines? |
|  | Start the server with the [`--replicate-wild-ignore-table=mysql.%`](replication-options-replica.md) option to ignore replication for tables in the `mysql` database. |
| **A.14.13.** | Does replication work on mixed operating systems (for example, the source runs on Linux while replicas run on macOS and Windows)? |
|  | Yes. |
| **A.14.14.** | Does replication work on mixed hardware architectures (for example, the source runs on a 64-bit machine while replicas run on 32-bit machines)? |
|  | Yes. |