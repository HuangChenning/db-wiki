---
title: Oracle Database Zero Data Loss Cloud Protect for Autonomous Recovery Service
book: Backup and Recovery User Guide
doc_id: E96241-26
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/cloud-protect-fleet-agent.html
tags:
  - oracle
  - 19c
  - backup-and-recovery-users-guide
---

Protect your on-premises databases on cloud using Oracle Database Autonomous Recovery Service.

Oracle Database Autonomous Recovery Service is a fully managed, standalone, and centralized cloud backup solution for Oracle Databases. Recovery Service is based on the on-premises Oracle Zero Data Loss Recovery Appliance (ZDLRA) technology which offers modern cyber security protection for Oracle Databases of any size. See [Overview of Autonomous Recovery Service](https://docs.oracle.com/en-us/iaas/recovery-service/doc/overview-recovery-service.html) to learn more.

The Cloud Protect Fleet Agent is a SQLcl based tool that enables you to add on-premises Oracle Databases to Recovery Service for data protection.

To use the Cloud Protect Fleet Agent, your database must be deployed on an Linux x86-64 platform. Oracle Database 19.18 and later and Oracle AI Database 26ai are the supported releases.

The Cloud Protect Fleet Agent leverages the Oracle SQLcl (SQL Developer Command Line) interface for on-premises database interactions with Recovery Service. You can invoke the Cloud Protect Fleet Agent commands in SQLcl using `rcv`.

Refer the [Autonomous Recovery Service](https://docs.oracle.com/en-us/iaas/recovery-service/doc/protecting-premises-databases-using-recovery-service.html) documentation for detailed information about using Oracle Database Zero Data Loss Cloud Protect.