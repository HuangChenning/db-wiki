---
title: Glossary
book: Database High Availability Overview
doc_id: E17157-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17157/glossary.htm
tags:
  - oracle
  - 11g
  - high-availability-overview
---

business impact analysis

An impact analysis that categorizes the business processes based on the severity of the impact of IT-related outages.

clusterwide failure

The whole cluster hosting the Oracle RAC database is unavailable or fails. This includes failures of nodes in the cluster, and any other components that result in the cluster being unavailable and the Oracle database and instances on the site being unavailable.

computer failure

An outage that occurs when the system running the database becomes unavailable because it has crashed or is no longer accessible.

cost of downtime

A complete business impact analysis provides the insight needed to quantify the cost of unplanned and planned downtime. Understanding this cost is essential because it helps prioritize your high availability investment and directly influences the high availability technologies that you choose to minimize the downtime risk.

data corruption

A corrupt block is a block that has been changed so that it differs from what Oracle Database expects to find. Block corruptions fall under two categories: physical and logical block corruptions.

See also physical corruption and logical corruption.

hang or slow down

Hang or slow down occurs when the database or the application is unable to process transactions because of a resource or lock contention. Perceived hang can be caused by lack of system resources.

human error

An outage that occurs when unintentional or malicious actions are committed that cause data in the database to become logically corrupt or unusable. The service level impact of a human error outage can vary significantly depending on the amount and critical nature of the affected data.

logical corruption

The contents of the block are logically inconsistent. Examples of logical corruption include corruption of a row piece or index entry.

logical unit numbers (LUNs)

Three-bit identifiers used on a SCSI bus to distinguish between up to eight devices (logical units) with the same SCSI ID.

lost write

A lost write is another form of data corruption that can occur when an I/O subsystem acknowledges the completion of the block write, while in fact the write I/O did not occur in the persistent storage. No error is reported by the I/O subsystem back to Oracle Database.

MAA environment

An architecture that provides the most comprehensive set of solutions for both unplanned and because it inherits the capabilities and advantages of both Oracle Database 11g with Oracle RAC and Oracle Database 11g with Data Guard.

The MAA environment consists of a site containing an Oracle RAC primary database and a second site containing a cluster that hosts both logical and physical standby databases, or at least one physical or logical standby database.

manageability goal

More subjective than either the RPO or the RTO, the manageability goal results from an objective evaluation of the skill sets and management resources available in an organization, and the degree to which the organization can successfully manage all elements of a high availability architecture. Understanding manageability goals helps organizations differentiate between what is possible and what is practical to implement.

network server processes

The Data Guard network server processes, also referred to as LNSn processes, on the primary database perform a network send to the RFS process on the standby database. There is one network server process for each destination.

Oracle Active Data Guard option

A physical standby database can be open for read-only access while Redo Apply is active if a license for the Oracle Active Data Guard option has been purchased. This capability, known as Active Data Guard, also provides the ability to have block-change tracking on the standby database, thus allowing incremental backups to be performed on the standby.

Note: The Active Data Guard option may also be referred to as "real-time query" in other documentation.

physical corruption

The database does not recognize the block at all: the checksum is invalid, the block contains all zeros, or the header and footer of the block do not match. A physical corruption is also called a media corruption.

recovery point objective (RPO)

The maximum amount of data an IT-based business process may lose before causing harm to the organization. RPO indicates the data-loss tolerance of a business process or an organization in general. This data loss is often measured in terms of time, for example, five hours or two days worth of data loss.

recovery time objective (RTO)

The maximum amount of time that an IT-based business process can be down before the organization suffers significant material losses. RTO indicates the downtime tolerance of a business process or an organization in general.

return on investment (ROI)

Return on Investment (or Rate of return) is used to evaluate the efficiency of an investment in finance and economics.

site failure

An outage that occurs when an event causes all or a significant portion of an application to stop processing or slow to an unusable service level. A site failure may affect all processing at a data center, or a subset of applications supported by a data center.

storage failure

An outage that occurs when the storage holding some or all of the database contents becomes unavailable because it has shut down or is no longer accessible.

total cost of ownership (TCO)

A financial estimate designed to help consumers and enterprise managers assess direct and indirect costs. It is used in many industries and is a form of full cost accounting.

transient logical standby database

A transient logical standby database allows you to reuse your current physical standby database by temporarily converting it into a logical standby on which to perform a rolling database upgrade, incurring minimal downtime.