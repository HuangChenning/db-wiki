---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/summary-recommendations-when-deploying-oracle-goldengate-oracle-rac.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Summary of Recommendations when Deploying Oracle GoldenGate on Oracle RAC

When configuring Oracle GoldenGate in an Oracle RAC environment, follow these recommendations.

- Install the latest version of Oracle GoldenGate software locally on each Oracle RAC node, making sure that the software location is the same on all Oracle RAC nodes.
- Use the Oracle Database File System (DBFS) or Oracle Advanced Cluster File System (ACFS) for the file system where the Oracle GoldenGate files are stored (trail, checkpoint, temporary, report, and parameter files).
- Use the same DBFS or ACFS mount point on all of the Oracle RAC nodes that may run Oracle GoldenGate.
- When creating the GoldenGate deployment, specify either DBFS or ACFS for the deployment location.
- Install Grid Infrastructure agent (XAG) version 10 or later on all Oracle RAC nodes that will run Oracle GoldenGate.
- Configure the GoldenGate processes to automatically start and restart when the deployment is started.