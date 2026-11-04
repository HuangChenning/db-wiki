---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/overview-ogg-ma-cloud-rac-and-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Overview

With these configuration and operational best practices, Oracle GoldenGate can be configured to work seamlessly with Oracle Data Guard after any zero data loss or data loss role transition.

By using Database File System (DBFS) as the file system for the Oracle GoldenGate Microservices deployment files, Oracle GoldenGate Extract, Distribution Paths, and Replicat processes continue to stay synchronized with the database after a role transition.

Implement these best practices for configuring Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service on Dedicated Infrastructure (ExaDB-D), or Oracle Exadata Database Service on Cloud@Customer (ExaDB-C@C), to work seamlessly with Oracle Data Guard, using Oracle Real Application Clusters (Oracle RAC), Oracle Clusterware, and Oracle Database File System (DBFS).

These best practices enable Oracle GoldenGate Microservices replication using a database that is protected by a Data Guard standby, to work following an Oracle Data Guard role transition transparently and seamlessly, no matter which Data Guard protection mode is configured (Maximum Performance, Maximum Availability, or Maximum Protection).

There are several key software requirements:

- Oracle Grid Infrastructure 19c or later
	Oracle Grid Infrastructure provides the necessary components needed to manage high availability for any business-critical applications. Using Oracle Clusterware (a component of Oracle Grid Infrastructure) network, database, and Oracle GoldenGate resources can be managed to provide availability in the event of a failure.
- Oracle Grid Infrastructure Agent version 10.2 or later
	The Oracle Grid Infrastructure Agent leverages the Oracle Grid Infrastructure components to provide integration between Oracle GoldenGate and its dependent resources, such as the database, network, and file system. The agent also integrates Oracle GoldenGate with Oracle Data Guard so that Oracle GoldenGate is restarted on the new primary database following a role transition.
- Oracle Database 19c or later
	Refer to [My Oracle Support note 2193391.1](https://support.oracle.com/rs?type=doc&id=2193391.1) for a full list of recommended Oracle Database patches when using Oracle GoldenGate.
- Oracle GoldenGate Microservices version 21c or later
	Oracle GoldenGate 21c introduces unified build support so a single software installation supports capturing and applying replicated data to multiple major Oracle Database versions (11g Release 2 to 21c). This is possible because an Oracle GoldenGate installation includes the required Oracle Database client libraries without requiring a separate database `ORACLE_HOME` installation.
- Oracle DBFS to protect and replicate critical Oracle GoldenGate files
	The Oracle Database File System (DBFS) is the only MAA-validated and recommended file system for an Oracle Data Guard and Oracle GoldenGate configuration, because it allows the storage of the required Oracle GoldenGate files, such as the checkpoint and trail files, to be located inside the same database that is protected with Oracle Data Guard, ensuring consistency between the Oracle GoldenGate files and the database in a seamless fashion.