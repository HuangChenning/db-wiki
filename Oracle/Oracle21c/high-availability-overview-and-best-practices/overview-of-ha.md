---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-of-ha.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 1 Overview of High Availability

See the following topics to learn what high availability and why it is important. Then follow the roadmap to implementing a Maximum Availability Architecture.

### What Is High Availability?

Availability is the degree to which an application and database service is available.

Availability is measured by the perception of an application's user. Users experience frustration when their data is unavailable or the computing system is not performing as expected, and they do not understand or care to differentiate between the complex components of an overall solution. Performance failures due to higher than expected usage create the same disruption as the failure of critical components in the architecture. If a user cannot access the application or database service, it is said to be unavailable. Generally, the term downtime is used to refer to periods when a system is unavailable.

Users who want their systems to be always ready to serve them need high availability. A system that is highly available is designed to provide uninterrupted computing services during essential time periods, during most hours of the day, and most days of the week throughout the year; this measurement is often shown as 24x365. Such systems may also need a high availability solution for planned maintenance operations such as upgrading a system's hardware or software.

Reliability, recoverability, timely error detection, and continuous operations are primary characteristics of a highly available solution:

- Reliability: Reliable hardware is one component of a high availability solution. Reliable software—including the database, web servers, and applications—is just as critical to implementing a highly available solution. A related characteristic is resilience. For example, low-cost commodity hardware, combined with software such as Oracle Real Application Clusters (Oracle RAC), can be used to implement a very reliable system. The resilience of an Oracle RAC database allows processing to continue even though individual servers may fail. For example, the Oracle RAC database allows processing to continue even though individual servers may fail.
- Recoverability: Even though there may be many ways to recover from a failure, it is important to determine what types of failures may occur in your high availability environment and how to recover from those failures quickly in order to meet your business requirements. For example, if a critical table is accidentally deleted from the database, what action should you take to recover it? Does your architecture provide the ability to recover in the time specified in a service-level agreement (SLA)?
- Timely error detection: If a component in your architecture fails, then fast detection is essential to recover from the unexpected failure. Although you may be able to recover quickly from an outage, if it takes an additional 90 minutes to discover the problem, then you may not meet your SLA. Monitoring the health of your environment requires reliable software to view it quickly and the ability to notify the database administrator of a problem.
- Continuous operation: Providing continuous access to your data is essential when very little or no downtime is acceptable to perform maintenance activities. Activities, such as moving a table to another location in the database or even adding CPUs to your hardware, should be transparent to the user in a high availability architecture.

More specifically, a high availability architecture should have the following traits:

- Tolerate failures such that processing continues with minimal or no interruption
- Be transparent to—or tolerant of—system, data, or application changes
- Provide built-in preventive measures
- Provide active monitoring and fast detection of failures
- Provide fast recoverability
- Automate detection and recovery operations
- Protect the data to minimize or prevent data loss and corruptions
- Implement the operational best practices to manage your environment
- Achieve the goals set in SLAs (for example, recovery time objectives (RTOs) and recovery point objectives (RPOs)) for the lowest possible total cost of ownership

### Importance of Availability

The importance of high availability varies among applications. Databases and the internet have enabled worldwide collaboration and information sharing by extending the reach of database applications throughout organizations and communities.

This reach emphasizes the importance of high availability in data management solutions. Both small businesses and global enterprises have users all over the world who require access to data 24 hours a day. Without this data access, operations can stop, and revenue is lost. Users now demand service-level agreements from their information technology (IT) departments and solution providers, reflecting the increasing dependence on these solutions. Increasingly, availability is measured in dollars, euros, and yen, not just in time and convenience.

Enterprises have used their IT infrastructure to provide a competitive advantage, increase productivity, and empower users to make faster and more informed decisions. However, with these benefits has come an increasing dependence on that infrastructure. If a critical application becomes unavailable, then the business can be in jeopardy. The business might lose revenue, incur penalties, and receive bad publicity that has a lasting effect on customers and on the company's stock price.

It is important to examine the factors that determine how your data is protected and maximize availability to your users.

### Cost of Downtime

The need to deliver increasing levels of availability continues to accelerate as enterprises reengineer their solutions to gain competitive advantage. Most often, these new solutions rely on immediate access to critical business data.

When data is not available, the operation can cease to function. Downtime can lead to lost productivity, lost revenue, damaged customer relationships, bad publicity, and lawsuits.

It is not always easy to place a direct cost on downtime. Angry customers, idle employees, and bad publicity are all costly, but not directly measured in currency. On the other hand, lost revenue and legal penalties incurred because SLA objectives are not met can easily be quantified. The cost of downtime can quickly grow in industries that are dependent on their solutions to provide service.

Other factors to consider in the cost of downtime are:

- The maximum tolerable length of a single unplanned outage
	If the event lasts less than 30 seconds, then it may cause very little impact and may be barely perceptible to users. As the length of the outage grows, the effect may grow exponentially and negatively affect the business.
- The maximum frequency of allowable incidents
	Frequent outages, even if short in duration, may similarly disrupt business operations.

When designing a solution, it is important to recognize the true cost of downtime to understand how the business can benefit from availability improvements.

Oracle provides a range of high availability solutions to fit every organization regardless of size. Small workgroups and global enterprises alike are able to extend the reach of their critical business applications. With Oracle and the Internet, applications and data are reliably accessible everywhere, at any time.

### Causes of Downtime

One of the challenges in designing a high availability solution is examining and addressing all of the possible causes of downtime.

It is important to consider causes of both unplanned and planned downtime when designing a fault-tolerant and resilient IT infrastructure. Planned downtime can be just as disruptive to operations as unplanned downtime, especially in global enterprises that support users in multiple time zones.

The following table describes unplanned outage types and provides examples of each type.

Table 1-1 Causes of Unplanned Downtime

| Type | Description | Examples |
| --- | --- | --- |
| Site failure | A site failure may affect all processing at a data center, or a subset of applications supported by a data center.  The definition of site varies given the contexts of on-premises and cloud.  - Site failure - entire regional failure - Data center - entire data center location - Availability domain - isolated data center within a region with possibly many other availability domains - Fault domain - isolated set of system resources within an Availability Domain or data center  Typically, each site, data center, availability domain, and fault domain has its own set of isolated hardware, DB compute, network, storage, and power. | - Extended site-wide power failure - Site-wide network failure - Natural disaster makes a data center inoperable - Terrorist or malicious attack on operations or the site |
| Cluster-wide failure | The whole cluster hosting an Oracle RAC database is unavailable or fails. This includes:  - Failures of nodes in the cluster - Failure of any other components that result in the cluster being unavailable and the Oracle database and instances on the site being unavailable | - The last surviving node on the Oracle RAC cluster fails and the node or database cannot be restarted - Both redundant cluster interconnections fail or Clusterware failure - Database corruption so severe that continuity is not possible on the current database server - Clusterware and hardware-software defects preventing availability or stability. |
| Computer failure | A computer failure outage occurs when the system running the database becomes unavailable because it has failed or is no longer available. When the database uses Oracle RAC then a computer failure represents a subset of the system (while retaining full access to the data). | - Database system hardware failure - Operating system failure - Oracle instance failure |
| Network failure | A network failure outage occurs when a network device stops or reduces network traffic and communication from your application to database, database to storage, or any system to system that is critical to your application service processing. | - Network switch failure - Network interface failure - Network cable failures |
| Storage failure | A storage failure outage occurs when the storage holding some or all of the database contents becomes unavailable because it has shut down or is no longer available. | - Disk or flash drive failure - Disk controller failure - Storage array failure |
| Data corruption | A corrupt block is a block that was changed so that it differs from what Oracle Database expects to find. Block corruptions can be categorized as physical or logical:  - In a physical block corruption, which is also called a media corruption, the database does not recognize the block at all; the checksum is invalid or the block contains all zeros. An example of a more sophisticated block corruption is when the block header and footer do not match. - In a logical block corruption, the contents of the block are physically sound and pass the physical block checks; however, the block can be logically inconsistent. Examples of logical block corruption include incorrect block type, incorrect data or redo block sequence number, corruption of a row piece or index entry, or data dictionary corruptions.  Block corruptions can also be divided into interblock corruption and intrablock corruption:  - In an intrablock corruption, the corruption occurs in the block itself and can be either a physical or a logical block corruption. - In an interblock corruption, the corruption occurs between blocks and can only be a logical block corruption.  A data corruption outage occurs when a hardware, software, or network component causes corrupt data to be read or written. The service-level impact of a data corruption outage may vary, from a small portion of the application or database (down to a single database block) to a large portion of the application or database (making it essentially unusable). | - Operating system or storage device driver failure - Faulty host bus adapter - Disk controller failure - Volume manager error causing a bad disk read or write - Software or hardware defects |
| Human error | A human error outage occurs when unintentional or other actions are committed that cause data in the database to become incorrect or unusable. The service-level impact of a human error outage can vary significantly, depending on the amount and critical nature of the affected data. | - File deletion (at the file system level) - Dropped database object - Inadvertent data changes - Malicious data changes |
| Lost or stray writes | A lost or stray write is another form of data corruption, but it is much more difficult to detect and repair quickly. A data block stray or lost write occurs when:  - For a lost write, an I/O subsystem acknowledges the completion of the block write even though the write I/O did not occur in the persistent storage. On a subsequent block read on the primary database, the I/O subsystem returns the stale version of the data block, which might be used to update other blocks of the database, thereby corrupting it. - For a stray write, the write I/O completed but it was written somewhere else, and a subsequent read operation returns the stale value. - For an Oracle RAC system, a read I/O from one cluster node returns stale data after a write I/O is completed from another node (lost write). For example, this occurs if a network file system (NFS) is mounted in Oracle RAC without disabling attribute caching (for example, without using the `noac` option). In this case, the write I/O from one node is not immediately visible to another node because it is cached.  Block corruptions caused by stray writes or lost writes can cause havoc to your database availability. The data block may be physically or logically correct but subsequent disk reads will show blocks that are stale or with an incorrect Oracle Database block address. | - Operating system or storage device driver failure - Faulty host bus adapter - Disk controller failure - Volume manager error - Other application software - Lack of network file systems (NFS) write visibility across a cluster - Software or hardware defects |
| Delay, slowdown, or hangs | A delay or slowdown occurs when the database or the application cannot process transactions because of a resource or lock contention. A perceived delay can be caused by lack of system resources. | - Database or application deadlocks - Runaway processes that consume system resources - Logon storms or system faults - Combination of application peaks with lack of system or database resources. This can occur with one application or many applications in a consolidated database environment without proper resource management. - Archived redo log destination or fast recovery area destination becomes full - Oversubscribed or heavily consolidated database system |

The following table describes planned outage types and provides examples of each type.

Table 1-2 Causes of Planned Downtime

| Type | Description | Examples |
| --- | --- | --- |
| Software changes | - Planned periodic software changes to apply minor fixes for stability and security - Planned annual or bi-annual major upgrades to adopt new features and capabilities | - Software updates, including security updates to operating system, clusterware. or database - Major upgrade of operating system, clusterware, or database - Updating or upgrading application software |
| System and database changes | - Planned system changes to replace defected hardware - Planned system changes to expand or reduce system resources - Planned database changes to adopt parameter changes - Planned change to migrate to new hardware or architecture | - Adding or removing processors or memory to a server - Adding or removing nodes to or from a cluster - Adding or removing disks drives or storage arrays - Replacing any Field Replaceable Unit (FRU) - Changing configuration parameters - System platform migration - Migrating to cluster architecture - Migrating to new storage |
| Data changes | Planned data changes to the logical structure or physical organization of Oracle Database objects. The primary objective of these changes is to improve performance or manageability. | - Table definition changes - Adding table partitioning - Creating and rebuilding indexes |
| Application changes | Planned application changes can include data changes and schema and programmatic changes. The primary objective of these changes is to improve performance, manageability, and functionality. | Application upgrades |

Oracle offers high availability solutions to help avoid both unplanned and planned downtime, and recover from failures. [Oracle Database High Availability Solutions for Unplanned Downtime](ha-unplanned-downtime.md) and [Oracle Database High Availability Solutions for Planned Downtime](ha-planned-downtime.md) discuss each of these high availability solutions in detail.

### Chaos Engineering

Maximum Availability Architecture leverages Chaos Engineering throughout its testing and development life cycles to ensure that end-to-end application and database availability is preserved or at its optimal levels for any fault or maintenance event.

Chaos Engineering is the discipline of experimenting on a system in order to build confidence in the system’s capability to withstand turbulent conditions in production. Specifically, MAA injects various faults and planned maintenance events to evaluate application and database impact throughout our development, stress, and testing cycles. With that experimentation, best practices, defects, and lessons learned are derived, and that knowledge is put back in practice to evolve and improve our MAA solutions.

### Roadmap to Implementing the Maximum Availability Architecture

Oracle high availability solutions and sound operational practices are the key to successful implementation of an IT infrastructure. However, technology alone is not enough.

Choosing and implementing an architecture that best fits your availability requirements can be a daunting task. Oracle Maximum Availability Architecture (MAA) simplifies the process of choosing and implementing a high availability architecture to fit your business requirements with the following considerations:

- Encompasses redundancy across all components
- Provides protection and tolerance from computer failures, storage failures, human errors, data corruption, lost writes, system delays or slowdowns, and site disasters
- Recovers from outages as quickly and transparently as possible
- Provides solutions to eliminate or reduce planned downtime
- Provides consistent high performance and robust security
- Provides Oracle Engineered System and cloud options to simplify deployment and management and achieve the highest scalability, performance, and availability
- Achieves SLAs at the lowest possible total cost of ownership
- Applies to On-Premise, Oracle Public Cloud, and hybrid architectures consisting of parts on-premise and part in the cloud
- Provides special consideration to Container or Oracle Multitenant, Oracle Database In-Memory, and Oracle Sharding architectures

To build, implement, and maintain this type of architecture, you need to:

1. Analyze your specific high availability requirements, including both the technical and operational aspects of your IT systems and business processes, as described in [High Availability and Data Protection – Getting From Requirements to Architecture](https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/ha-requirements-architecture.html#GUID-7EB6D827-A30E-4E76-BAF8-0AF4DDCAD2C2 "Any effort to design and implement a high availability strategy for Oracle Database begins by performing a thorough business impact analysis to identify the consequences to the enterprise of downtime and data loss, whether caused by unplanned or planned outages.The business impact analysis categorizes the business processes based on the severity of the impact of IT-related outages.A complete business impact analysis provides the insight needed to quantify the cost of unplanned and planned downtime.The business impact analysis determines your tolerance to downtime, also known as the recovery time objective (RTO).The business impact analysis also determines your tolerance to data loss, also known as a recovery point objective (RPO).A manageability goal is more subjective than either the RPO or the RTO. You must make an objective evaluation of the skill sets, management resources, and tools available in an organization, and the degree to which the organization can successfully manage all elements of a high availability architecture.Understanding the total cost of ownership (TCO) and objectives for return on investment (ROI) are essential to selecting a high availability architecture that also achieves the business goals of your organization.The business impact analysis will help you document what is already known. The outcome of the business impact analysis provides the insight you need to group databases having similar RTO and RPO objectives together.Oracle MAA best practices define high availability reference architectures that address the complete range of availability and data protection required by enterprises of all sizes and lines of business.The Bronze tier is appropriate for databases where simple restart of a failed component (e.g. listener, database instance, or database) or restore from backup is \"HA and DR enough.\"The Silver tier provides an additional level of high availability for databases that require minimal or zero downtime in the event of database instance or server failure, as well as most common planned maintenance events, such as hardware and software updates.The Gold tier raises the stakes substantially for business-critical applications that cannot tolerate high RTO and RPO for any disasters such as database, cluster, corruptions, or site failures. Additionally, major database upgrades or site migrations can be done in seconds.The Platinum tier introduces two architecture patterns: Oracle GoldenGate replication with Oracle Database 19c Oracle Active Data Guard and Oracle AI Database 26ai and later releases.The Diamond tier introduces builds on MAA Platinum with Oracle GoldenGate, and is ideal for extremely mission critical systems.Each MAA reference architecture delivers known and tested levels of downtime and data protection.").
2. Evaluate the various high availability architectures and their benefits and options, as described in [Oracle MAA Reference Architectures](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/26&id=HAIAD).
3. Understand the availability impact for each MAA reference architecture, or various high availability features, on businesses and applications, as described in [Oracle Database High Availability Solutions for Unplanned Downtime](ha-unplanned-downtime.md), and [Oracle Database High Availability Solutions for Planned Downtime](ha-planned-downtime.md).
4. Familiarize yourself with Oracle high availability features, as described in [Features for Maximizing Availability](ha-features.md).
5. Use operational best practices to provide a successful MAA implementation, as described in [Operational Prerequisites to Maximizing Availability](operational-prerequisites-maximizing-availability1.md).
6. Implement a high availability architecture using Oracle MAA resources, which provide technical details about the various Oracle MAA high availability technologies, along with best practice recommendations for configuring and using such technologies, such as Oracle MAA best practices technical briefs, customer papers with proof of concepts, customer case studies, recorded web casts, demonstrations, and presentations.
	Additional Oracle MAA resources are available at [http://www.oracle.com/goto/maa](http://www.oracle.com/goto/maa).