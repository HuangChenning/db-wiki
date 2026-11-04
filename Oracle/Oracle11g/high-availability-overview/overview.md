---
title: Overview of High Availability
book: Database High Availability Overview
doc_id: E17157-09
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17157/overview.htm
tags:
  - oracle
  - 11g
  - high-availability-overview
---

## 1 Overview of High Availability

This chapter contains the following sections:

## 1.1 What Is High Availability?

Availability is the degree to which an application, service, or function is accessible on demand. Availability is measured by the perception of an application's end user. Users experience frustration when their data is unavailable or the computing system is not performing as expected, and they do not understand or care to differentiate between the complex components of an overall solution. Performance failures due to higher than expected usage create the same disruption as the failure of critical components in the architecture. If a user cannot access the system, it is said to be unavailable. Generally, the term downtime is used to refer to periods when a system is unavailable.

Users who want their systems to be ready to serve them at all times need high availability. A system that is highly available is designed to provide uninterrupted computing services during essential time periods, during most hours of the day, and most days of the week throughout the year; this measurement is often shown as 24x365. However, exceptions can be made for minimal downtime to perform certain operations such as upgrading the system's hardware or software.

Reliability, recoverability, timely error detection, and continuous operations are primary characteristics of a highly available solution:

- Reliability: Reliable hardware is one component of a high availability solution. Reliable software—including the database, Web servers, and applications—is just as critical to implementing a highly available solution. A related characteristic is resilience. For example, low-cost commodity hardware, combined with software such as Oracle Real Application Clusters (Oracle RAC), can be used to implement a very reliable system. The resilience of an Oracle RAC database allows processing to continue even though individual servers may fail.
- Recoverability: There may be many ways to recover from a failure. Therefore, it is important to determine what types of failures may occur in your high availability environment and how to recover from those failures in a timely manner that meets your business requirements. For example, if a critical table is accidentally deleted from the database, what action should you take to recover it? Does your architecture provide the ability to recover in the time specified in a service-level agreement (SLA)?
- Timely error detection: If a component in your architecture fails, then fast detection is essential to recover from the unexpected failure. Although you may be able to recover quickly from an outage, if it takes an additional 90 minutes to discover the problem, then you may not meet your SLA. Monitoring the health of your environment requires reliable software to view it quickly and the ability to notify the database administrator of a problem.
- Continuous operation: Providing continuous access to your data is essential when very little or no downtime is acceptable to perform maintenance activities. Activities, such as moving a table to another location in the database or even adding CPUs to your hardware, should be transparent to the end user in a high availability architecture.

More specifically, a high availability architecture should have the following traits:

- Tolerate failures such that processing continues with minimal or no interruption
- Be transparent to—or tolerant of—system, data, or application changes
- Provide built-in preventive measures
- Provide active monitoring and fast detection of failures
- Provide fast recoverability
- Automate detection and recovery operations
- Protect the data to minimize or prevent data loss
- Implement the operational best practices to manage your environment
- Achieve the goals set in SLAs (for example, recovery time objectives (RTOs) and recovery point objectives (RPOs)) for the lowest possible total cost of ownership

## 1.2 Importance of Availability

The importance of high availability varies among applications. Databases and the Internet have enabled worldwide collaboration and information sharing by extending the reach of database applications throughout organizations and communities. This reach emphasizes the importance of high availability in data management solutions. Both small businesses and global enterprises have users all over the world who require access to data 24 hours a day. Without this data access, operations can stop, and revenue is lost. Users now demand service-level agreements from their information technology (IT) departments and solution providers, reflecting the increasing dependence on these solutions. Increasingly, availability is measured in dollars, euros, and yen, not just in time and convenience.

Enterprises have used their IT infrastructure to provide a competitive advantage, increase productivity, and empower users to make faster and more informed decisions. However, with these benefits has come an increasing dependence on that infrastructure. If a critical application becomes unavailable, then the business can be in jeopardy. The business might lose revenue, incur penalties, and receive bad publicity that has a lasting effect on customers and on the company's stock price.

It is important to examine the factors that determine how your data is protected and maximize availability to your users.

## 1.3 Cost of Downtime

The need to deliver increasing levels of availability continues to accelerate as enterprises reengineer their solutions to gain competitive advantage. Most often, these new solutions rely on immediate access to critical business data. When data is not available, the operation can cease to function. Downtime can lead to lost productivity, lost revenue, damaged customer relationships, bad publicity, and lawsuits.

It is not always easy to place a direct cost on downtime. Angry customers, idle employees, and bad publicity are all costly, but not directly measured in currency. On the other hand, lost revenue and legal penalties incurred because SLA objectives are not met can easily be quantified. The cost of downtime can quickly grow in industries that are dependent on their solutions to provide service.

Other factors to consider in the cost of downtime are:

- The maximum tolerable length of a single unplanned outage
	If the event lasts less than 30 seconds, then it may cause very little impact and may be barely perceptible to end users. As the length of the outage grows, the effect may grow exponentially and negatively affect the business.
- The maximum frequency of allowable incidents
	Frequent outages, even if short in duration, may similarly disrupt business operations.

When designing a solution, it is important to recognize the true cost of downtime to understand how the business can benefit from availability improvements.

Oracle provides a range of high availability solutions to fit every organization regardless of size. Small workgroups and global enterprises alike are able to extend the reach of their critical business applications. With Oracle and the Internet, applications and data are reliably accessible everywhere, at any time.

## 1.4 Causes of Downtime

One of the challenges in designing a high availability solution is examining and addressing all of the possible causes of downtime. It is important to consider causes of both unplanned and planned downtime when designing a fault-tolerant and resilient IT infrastructure. Planned downtime can be just as disruptive to operations as unplanned downtime, especially in global enterprises that support users in multiple time zones.

Table 1-1 describes unplanned outage types and provides examples of each type.

Table 1-1 Causes of Unplanned Downtime

| Type | Description | Examples |
| --- | --- | --- |
| Site failure | A site failure may affect all processing at a data center, or a subset of applications supported by a data center. | - Extended sitewide power failure - Sitewide network failure - Natural disaster makes a data center inoperable - Terrorist or malicious attack on operations or the site |
| Clusterwide failure | The whole cluster hosting an Oracle RAC database is unavailable or fails. This includes:  - Failures of nodes in the cluster - Failure of any other components that result in the cluster being unavailable and the Oracle database and instances on the site being unavailable | - The last surviving node on the Oracle RAC cluster fails and inability to restart the node - Both redundant cluster interconnects fail or clusterware failure - Database corruption so severe that continuity is not possible on the current data server - Disk storage failure |
| Computer failure | A computer failure outage occurs when the system running the database becomes unavailable because it has failed or is no longer accessible. | - Database system hardware failure - Operating system failure - Oracle instance failure - Network interface failure |
| Storage failure | A storage failure outage occurs when the storage holding some or all of the database contents becomes unavailable because it has shut down or is no longer accessible. | - Disk drive failure - Disk controller failure - Storage array failure |
| Data corruption | A corrupt block is a block that has been changed so that it differs from what Oracle Database expects to find. Block corruptions fall under the following categories: physical and logical block corruptions:  - In a [physical corruption](glossary.md), which is also called a media corruption, the database does not recognize the block at all: the checksum is invalid, the block contains all zeros, or the header and footer of the block do not match. - In a [logical corruption](glossary.md), the contents of the block are logically inconsistent. Examples of logical corruption include corruption of a row piece or index entry.  Block corruptions can also be divided into interblock corruption and intrablock corruption:  - In intrablock corruption, the corruption occurs in the block itself and can be either a physical or a logical corruption. - In an interblock corruption, the corruption occurs between blocks and can only be a logical corruption.  A data corruption outage occurs when a hardware, software, or network component causes corrupt data to be read or written. The service-level impact of a data corruption outage may vary, from a small portion of the database (down to a single database block) to a large portion of the database (making it essentially unusable). | - Operating system or storage device driver failure - Faulty host bus adapter - Disk controller failure - Volume manager error causing a bad disk read or write - Software defects |
| Human error | A human error outage occurs when unintentional or other actions are committed that cause data in the database to become incorrect or unusable. The service-level impact of a human error outage can vary significantly, depending on the amount and critical nature of the affected data. | - File deletion (at the file system level) - Dropped database object - Inadvertent data changes - Malicious data changes |
| Lost writes | A lost write is another form of data corruption, but it is much more difficult to detect and repair quickly. A data block stray or lost write occurs when:  - For a lost write, an I/O subsystem acknowledges the completion of the block write even though the write I/O did not occur in the persistent storage. On a subsequent block read on the primary database, the I/O subsystem returns the stale version of the data block, which might be used to update other blocks of the database, thereby corrupting it. - For a stray write, the write I/O completed but it was written somewhere else, and a subsequent read operation returns the stale value. - For an Oracle RAC system, a read I/O from one cluster node returns stale data after a write I/O is completed from another node (lost write). For example, this occurs if a network file system (NFS) is mounted in Oracle RAC without disabling attribute caching (for example, without using the `noac` option). In this case, the write I/O from one node is not immediately visible to another node because it is cached. | - Operating system or storage device driver failure - Faulty host bus adapter - Disk controller failure - Volume manager error - Other application software - Lack of network file systems (NFS) write visibility across a cluster |
| Hang or slowdown | Hang or slowdown occurs when the database or the application is unable to process transactions because of a resource or lock contention. A perceived hang can be caused by lack of system resources. | - Database or application deadlocks - Runaway processes that consume system resources - Log on storms or system faults - Combination of application peaks with lack of system or database resources - Archived redo log destination or fast recovery area destination becomes full |

Table 1-2 describes planned outage types and provides examples of each type.

Table 1-2 Causes of Planned Downtime

| Type | Description | Examples |
| --- | --- | --- |
| System and database changes | Planned system changes occur when performing routine and periodic maintenance operations and new deployments.  Planned system changes include any scheduled changes to the operating environment that occur outside the organizational data structure in the database.  The service-level impact of a planned system change varies significantly depending on the nature and scope of the planned outage, the testing and validation efforts made before implementing the change, and the technologies and features in place to minimize the impact. | - Adding or removing processors to or from an SMP server - Adding or removing nodes to or from a cluster - Adding or removing disks drives or storage arrays - Changing configuration parameters - Upgrading or patching system hardware and software - Upgrading or patching Oracle software - Upgrading or patching application software - System platform migration - Database relocation - Moving from 32 bits to 64 bits - Migrating to cluster architecture - Migrating to new storage |
| Data changes | Planned data changes occur when there are changes to the logical structure or physical organization of Oracle Database objects. The primary objective of these changes is to improve performance or manageability. | - Table definition changes - Adding table partitioning - Creating and rebuilding indexes |
| Application changes | Planned application changes may include data changes and schema and programmatic changes. The primary objective of these changes is to improve performance, manageability, and functionality. | - Application upgrades |

Oracle offers high availability solutions to help avoid both unplanned and planned downtime, and recover from failures. [Chapter 3](unplanned.md) and [Chapter 4](planned.md) discuss each of these high availability solutions in detail.

## 1.5 Roadmap to Implementing the Maximum Availability Architecture (MAA)

Oracle high availability solutions and sound operational practices are key to the successful implementation of IT infrastructure. However, technology alone is not enough.

Choosing and implementing an architecture that best fits your availability requirements can be a daunting task. MAA simplifies the process of choosing and implementing a high availability architecture to fit your business requirements. The MAA architecture:

- Encompasses redundancy across all components
- Provides protection and tolerance from computer failures, storage failures, human errors, data corruption, lost writes, system hangs or slowdowns, and site disasters
- Recovers from outages as quickly and transparently as possible
- Provides solutions to eliminate or reduce planned downtime
- Provides consistent high performance and robust security
- Is straightforward to deploy, can be managed efficiently, and scales easily
- Achieves SLAs at the lowest possible total cost of ownership

To build, implement and maintain such an architecture, you need to:

1. Understand the key effects of the Oracle high availability features on businesses and applications, as described in [Chapter 3](unplanned.md) and [Chapter 4](planned.md).
2. Analyze your specific high availability requirements, including both the technical and operational aspects of your IT systems and business processes, as described in [Chapter 2, "Determining Your High Availability Requirements"](hadesign.md)
3. Choose a high availability architecture, as described in [Chapter 7, "High Availability Architectures and Solutions"](architectures.md)
4. Implement a high availability architecture using the following resources:
	- MAA and high availability best practices white papers and other information
		Oracle offers various best practices white papers, customer MAA papers with proof of concepts, customer case studies, recorded Web casts, demonstrations, and presentations. These resources provide technical details about the MAA various high availability technologies, along with best practice recommendations for configuring and using such technologies.
		You can download these MAA resources from the following Web site
		```
		http://www.oracle.com/goto/maa
		```
		- Oracle Database High Availability Best Practices
		This book provides detailed best practice recommendations and information. It can help you to configure a new high availability environment, or migrate an existing configuration to create a redundant, reliable system without sacrificing simplicity and performance.

An enterprise with a well-articulated set of high availability best practices that encompass high availability analysis frameworks, business drivers, and system capabilities, enjoys an improved operational resilience and enhanced business agility.