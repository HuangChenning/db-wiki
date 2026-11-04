---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-1-you-begin-oggma-cloud-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 1 - Before You Begin

To get started, complete the following prerequisites:

- Procure Oracle Exadata Database Service on Dedicated Infrastructure or Cloud@Customer for the Oracle GoldenGate deployment.
	You can deploy Oracle GoldenGate with an existing ExaDB-D or ExaDB-C@C system or launch a new system, according to your business needs. For instructions on launching and managing an ExaDB-D system, see [Oracle Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en-us/iaas/exadatacloud/index.html) or for ExaDB-C@C see [Oracle Exadata Database Service on Cloud@Customer](https://docs.oracle.com/en-us/iaas/exadata/index.html).
- Have Oracle GoldenGate configured as detailed in [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md).
	DBFS is required for critical Oracle GoldenGate files when integrating with Data Guard.
- The Oracle Data Guard standby database should also be configured and operational before continuing.
	For more information about Oracle Data Guard see [Getting Started with Oracle Data Guard](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=SBYDB-GUID-31EBC212-59E1-4536-A884-EFA9FE3DFD84).
- A secure deployment involves making RESTful API calls and conveying trail data between the Distribution Server and Receiver Server, over SSL/TLS. You can use your own existing business certificate from your Certificate Authority (CA) or you might create your own certificates.
	Contact your systems administrator to follow your corporate standards to create or obtain the server certificate before proceeding. A separate certificate is required for each VIP and Service Manager pair.