---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Overview of Oracle GoldenGate Microservices Architecture Configuration on Oracle Exadata Database Service

The target Oracle Exadata Database Service that hosts Oracle GoldenGate Microservices Architecture can act as the source database, the target database, or in some cases, as both source and target databases for Oracle GoldenGate. These best practices are applicable for configuring Oracle GoldenGate Microservices Architecture with Oracle Exadata Database Service on Dedicated Infrastructure or Cloud@Customer.

Follow this roadmap to configure Oracle GoldenGate on Oracle Exadata Database Service on Dedicated Infrastructure (ExaDB-D) or Oracle Exadata Database Service on Cloud@Customer.

- [Task 1 - Before You Begin](task-1-you-begin.md): To configure Oracle GoldenGate on Oracle Exadata Cloud Infrastructure or Cloud@Customer, you need an ExaDB-D or ExaDB-C@C system, CA certificates, and configure some extra software.
- [Task 2 - Configure the Oracle Database for GoldenGate](task-2-configure-database-goldengate.md): Use best practices to configure the source and target databases in an Oracle GoldenGate replicated environment.
- [Task 3 - Create a Shared File System to Store the Oracle GoldenGate Deployment](task-3-create-shared-file-system-store-goldengate-deployment.md): Set up either Oracle DBFS or Oracle ACFS for configuring HA on Oracle Cloud Infrastructure with Oracle GoldenGate. If your architecture has a GoldenGate replica database protected by a cloud physical standby database (Oracle Data Guard), use Oracle DBFS; otherwise use ACFS.
- [Task 4 - Install Oracle GoldenGate](task-4-install-oracle-goldengate.md): Use best practices to install and configure Oracle GoldenGate components on Oracle Cloud Infrastructure.
- [Task 5 - Create the Oracle GoldenGate Deployment](task-5-create-oracle-goldengate-deployment.md): Create a response file to create the GoldenGate deployment using the Oracle GoldenGate Configuration Assistant.
- [Task 6 - Configure the Network](task-6-configure-network.md): Configure virtual cloud network (VCN) components such as private DNS zones, VIP, bastion, security lists and firewalls for Oracle GoldenGate to function properly.
- [Task 7 - Configure Oracle Grid Infrastructure Agent](task-7-configure-oracle-grid-infrastructure-agent-xag.md): Configure Oracle GoldenGate for HA on Oracle Cloud Infrastructure.
- [Task 8 - Configure NGINX Reverse Proxy](task-8-configure-nginx-reverse-proxy1.md): Configure reverse proxy and HA by using Nginx.
- [Task 9 - Create Oracle Net TNS Alias for Oracle GoldenGate Database Connections](task-9-create-oracle-net-tns-alias-oracle-goldengate-database-connections1.md): Create a TNS alias to simplify database connectivity for the Oracle GoldenGate processes when switching between Oracle RAC nodes.
- [Task 10 - Create a New Profile](task-10-create-new-profile.md): Create a new profile to automatically start the Extract and Replicat processes when the Oracle GoldenGate Administration Server is started.
- [Task 11 - Configure Oracle GoldenGate Processes](task-11-configure-oracle-goldengate-processes.md): Create and configure Oracle GoldenGate Extract, Replicat, and Path processes need for data replication