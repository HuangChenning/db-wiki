---
title: Introduction to High Availability Best Practices
book: High Availability Best Practices
doc_id: E10803-06
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10803/intro.htm
tags:
  - oracle
  - 11g
  - high-availability-best-practices
---

## 1 Introduction to High Availability Best Practices

By implementing and using Oracle Maximum Availability Architecture (MAA) best practices, you can provide high availability for the Oracle database and related technology.

This chapter contains the following topics:

## 1.1 Oracle Database High Availability Architecture

Designing and implementing a high availability architecture can be a daunting task given the broad range of Oracle technologies and hardware, software, and deployment options. A successful effort begins with clearly defined and thoroughly understood business requirements. Thorough analysis of the business requirements enables you to make intelligent design decisions and develop an architecture that addresses your business needs in the most cost effective manner. The architecture you choose must achieve the required levels of availability, performance, scalability, and security. Moreover, the architecture you choose should have a clearly defined plan for deployment and ongoing management that minimizes complexity and business risk.

Once your business requirements are understood, you should begin designing your high availability architecture by reading the [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/toc.htm) to get a high-level view of the various Oracle solutions that comprise the Oracle Maximum Availability Architecture (MAA). This should result in a design for an architecture that can be fully examined and validated using the best practices documented in this book.

## 1.2 Oracle Database High Availability Best Practices

Oracle High Availability (HA) best practices help you deploy a highly available architecture throughout your enterprise. Having a set of configuration and operational best practices helps you achieve high availability and reduces the cost associated with the implementation and ongoing maintenance of your enterprise. Also, employing best practices can optimize usage of system resources.

By implementing the HA best practices you can:

- Reduce the cost of creating an Oracle Database high availability system by following detailed guidelines on configuring your database, storage, application failover, backup and recovery. See [Chapter 3, "Overview of Configuration Best Practices"](config_intro.md) for more information.
- Use operational best practices to maintain your system. See [Chapter 2, "Operational Prerequisites to Maximizing Availability"](operational_bps.md) for more information.
- Detect and quickly recover from unscheduled outages caused by computer failure, storage failure, human error, or data corruption. For more information, see [Section 5.1.6, "Protect Against Data Corruption"](config_db.md) and [Chapter 13, "Recovering from Unscheduled Outages"](outage.md).
- Eliminate or reduce downtime due to scheduled maintenance such as database patches or application upgrades as described in [Chapter 14, "Reducing Downtime for Planned Maintenance"](schedule_outage.md).

## 1.3 Oracle Maximum Availability Architecture

Oracle Maximum Availability Architecture (MAA) is Oracle's best practices blueprint based on Oracle High Availability (HA) technologies, extensive validation performed by the Oracle MAA development team, and the accumulated production experience of customers who have successfully deployed business critical applications on Oracle.

MAA covers Oracle products within the following technologies:

- Oracle Database as described in this book
- Oracle Exadata Database Machine and Oracle Exalogic Elastic Cloud
- Oracle Fusion Middleware and Oracle WebLogic Server
- Oracle Applications (Siebel, Peoplesoft, E-Business Suite)
- Oracle Collaboration Suite
- Oracle Enterprise Manager

This book, Oracle Database High Availability Best Practices primarily focuses on high availability best practices for the Oracle Database. There are also other components for which you might want to consider Oracle Maximum Availability Architecture (MAA) best practices. For more information go to:

`http://www.oracle.com/goto/MAA`

See:

- [Oracle Fusion Middleware Disaster Recovery Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ASDRG) for information about Oracle Fusion Middleware high availability
- [Oracle Fusion Middleware Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=ASADM349) for information about backup and recovery for Oracle Fusion Middleware

The goal of MAA is to achieve the optimal HA architecture at the lowest cost and complexity. MAA provides:

- Best practices that span the Exadata Database Machine, Oracle Database, Oracle Fusion Middleware, Oracle Applications, Oracle Enterprise Manager, and solutions provided by Oracle Partners.
- Accommodates a range of business requirements to make these best practices as widely applicable as possible.
- Leverages lower-cost servers and storage.
- Uses hardware and operating system independent features and evolves with new Oracle versions and features. The only exception is Exadata MAA which has specific and customized configuration and operating practices for Exadata Database Machine.
- Makes high availability best practices as widely applicable as possible considering the various business service level agreements (SLA).
- Uses the Oracle Grid Infrastructure with Database Server Grid and Database Storage Grid to provide highly resilient, scalable, and lower cost infrastructures.
- Provides the ability to control the length of time to recover from an outage and the amount of acceptable data loss from any outage.

For more information about MAA and documentation about best practices for all MAA components, visit the MAA website at

`http://www.oracle.com/goto/maa`