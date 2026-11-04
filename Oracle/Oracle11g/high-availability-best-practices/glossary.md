---
title: Glossary
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/glossary.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

Oracle Active Data Guard option

A physical standby database can be open for read-only access while Redo Apply is active if a license for the Oracle Active Data Guard option has been purchased. This capability, known as real-time query, also provides the ability to have block-change tracking on the standby database, thus allowing incremental backups to be performed on the standby.

clusterwide failure

The whole cluster hosting the Oracle RAC database is unavailable or fails. This includes failures of nodes in the cluster, and any other components that result in the cluster being unavailable and the Oracle database and instances on the site being unavailable.

computer failure

An outage that occurs when the system running the database becomes unavailable because it has crashed or is no longer accessible.

data corruption

A corrupt block is a block that has been changed so that it differs from what Oracle Database expects to find. Block corruptions fall under two categories: physical and logical block corruptions.

hang or slow down

Hang or slow down occurs when the database or the application cannot process transactions because of a resource or lock contention. Perceived hang can be caused by lack of system resources.

human error

An outage that occurs when unintentional or malicious actions are committed that cause data in the database to become logically corrupt or unusable. The service level impact of a human error outage can vary significantly depending on the amount and critical nature of the affected data.

logical unit numbers (LUNs)

Three-bit identifiers used on a SCSI bus to distinguish between up to eight devices (logical units) with the same SCSI ID.

lost write

A lost write is another form of data corruption that can occur when an I/O subsystem acknowledges the completion of the block write, while in fact the write did not occur in the persistent storage. No error is reported by the I/O subsystem back to Oracle.

MAA environment

The Maximum Availability architecture provides the most comprehensive set of solutions for both unplanned and because it inherits the capabilities and advantages of both Oracle Database 11g with Oracle RAC and Oracle Database 11g with Data Guard.

MAA involves high availability best practices for all Oracle products across the entire technology stack—Oracle Database, Oracle WebLogic Server, Oracle Applications, Oracle Collaboration Suite, and Enterprise Manager.

network server processes

The Data Guard network server processes, also referred to as LNSn processes, on the primary database perform a network send to the RFS process on the standby database. There is one network server process for each destination.

real-time query

If a license for the Oracle Active Data Guard option has been purchased, you can open a physical standby database while Redo Apply continues to apply redo data received from the primary database.

recovery point objective (RPO)

The maximum amount of data an IT-based business process may lose before causing harm to the organization. RPO indicates the data-loss tolerance of a business process or an organization in general. This data loss is often measured in terms of time, for example, five hours or two days worth of data loss.

recovery time objective (RTO)

The maximum amount of time that an IT-based business process can be down before the organization suffers significant material losses. RTO indicates the downtime tolerance of a business process or an organization in general.

site failure

An outage that occurs when an event causes all or a significant portion of an application to stop processing or slow to an unusable service level. A site failure may affect all processing at a data center, or a subset of applications supported by a data center.

snapshot standby database

An updatable standby database that you create from a physical standby database. A snapshot standby database receives and archives redo data received from the primary database, but the snapshot standby database does not apply redo data from the primary database while the standby database is open for read/write I/O. Thus, the snapshot standby typically diverges from the primary database over time. Moreover, local updates to the snapshot standby database cause additional divergence. However, a snapshot standby protects the primary database because the snapshot standby can be converted back into a physical standby database.

storage failure

An outage that occurs when the storage holding some or all of the database contents becomes unavailable because it has shut down or is no longer accessible.

transient logical standby database

A transient logical standby database is a physical standby database that has been temporarily converted into a logical standby database to perform a rolling database upgrade.