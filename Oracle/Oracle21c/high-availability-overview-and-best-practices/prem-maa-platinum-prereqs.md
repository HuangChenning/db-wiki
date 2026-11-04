---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/prem-maa-platinum-prereqs.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Prerequisites

Be sure to complete the following prerequisites before performing any tasks for on-premises MAA Platinum architecture configuration.

- As a prerequisite for MAA Platinum on-premises, have Oracle GoldenGate configured as detailed in [On-Premises: Oracle GoldenGate Microservices Architecture with Oracle Real Application Clusters Configuration Best Practices](ogg-microservices-premises1.md).
- The Database File System (DBFS) is required for critical Oracle GoldenGate files when integrating with Data Guard.
- The Oracle Data Guard standby database should also be configured and operational before continuing.

The following are software requirements that the MAA Platinum configuration is based on:

- Oracle Grid Infrastructure 19c or later
	Oracle Grid Infrastructure provides the necessary components needed to manage high availability for any business-critical applications. Using Oracle Clusterware (a component of Oracle Grid Infrastructure) network, database, and Oracle GoldenGate resources can be managed to provide availability in the event of a failure.
- Oracle Grid Infrastructure Agent version 10.2 or later
	The Oracle Grid Infrastructure Agent leverages the Oracle Grid Infrastructure components to provide integration between Oracle GoldenGate and its dependent resources, such as the database, network, and file system. The agent also integrates Oracle GoldenGate with Oracle Data Guard so that Oracle GoldenGate is restarted on the new primary database following a role transition.
- Oracle Database 19c or later
	See [My Oracle Support Document 2193391.1](https://support.oracle.com/rs?type=doc&id=2193391.1) for a full list of recommended Oracle Database patches when using Oracle GoldenGate.
- Oracle GoldenGate Microservices version 21c or later
	Oracle GoldenGate 21c introduces unified build support so a single software installation supports capturing and applying replicated data to multiple major Oracle Database versions (11g Release 2 to 21c). This is possible because an Oracle GoldenGate installation includes the required Oracle Database client libraries without requiring a separate database `ORACLE_HOME` installation.
- Oracle DBFS to protect and replicate critical Oracle GoldenGate files
	The Oracle Database File System (DBFS) is the only MAA-validated and recommended file system for an Oracle Data Guard and Oracle GoldenGate configuration, because it allows the storage of the required Oracle GoldenGate files, such as the checkpoint and trail files, to be located inside the same database that is protected with Oracle Data Guard, ensuring consistency between the Oracle GoldenGate files and the database in a seamless fashion.

When the prerequisites are met, follow the configuration best practices in the Tasks that follow. These tasks should be performed to ensure the seamless integration of Oracle GoldenGate Microservices with Oracle Data Guard, which in turn ensures that GoldenGate continues running after any Data Guard role transition.