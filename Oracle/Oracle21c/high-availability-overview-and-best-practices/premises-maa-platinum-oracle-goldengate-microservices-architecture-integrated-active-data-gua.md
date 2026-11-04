---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/premises-maa-platinum-oracle-goldengate-microservices-architecture-integrated-active-data-gua.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 28 On-Premises MAA Platinum: Oracle GoldenGate Microservices Architecture Integrated with Active Data Guard

The combination and integration of Oracle GoldenGate Microservices and Oracle Data Guard enables you to achieve an MAA Platinum service-level configuration that achieves zero or near zero downtime for all planned and unplanned outages.

Follow these configuration best practices to enable Oracle GoldenGate Microservices replication using a database that is protected by a Data Guard standby, to transparently and seamlessly work following an Oracle Data Guard role transition, no matter which Data Guard protection mode is configured (Maximum Performance, Maximum Availability, or Maximum Protection).

Topics:

- [Prerequisites](prem-maa-platinum-prereqs.md)
- [Task 1: Configure the Standby Database for Oracle GoldenGate](task-1-configure-standby-database-oracle-goldengate.md)
- [Task 2: Modify the Primary Database Service](task-2-modify-primary-database-service.md)
- [Task 3: Create the Standby Database Service](task-3-create-standby-database-service.md)
- [Task 4: Configure DBFS on the Standby Cluster Nodes](task-4-configure-dbfs-standby-cluster-nodes.md)
- [Task 5: Install Oracle GoldenGate Software](task-5-install-oracle-goldengate-software.md)
- [Task 6: Create Oracle GoldenGate Deployment Directories](task-6-create-oracle-goldengate-deployment-directories.md)
- [Task 7: Configure the Standby NGINX Reverse Proxy](task-7-configure-standby-nginx-reverse-proxy.md)
- [Task 8: Configure Oracle Clusterware](task-8-configure-oracle-clusterware.md)
- [Task 9: Create Oracle Net TNS Aliases for Oracle GoldenGate Database Connections](task-9-create-oracle-net-tns-aliases-oracle-goldengate-database-connections.md)
- [Task 10: Configure Oracle GoldenGate Processes](task-10-configure-oracle-goldengate-processes1.md)
- [Example Distribution Path Target Change Script](prem-example-distribution-path-target-change-script.md)