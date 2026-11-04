---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-4-install-oracle-goldengate-oggma-clod-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 4 - Install Oracle GoldenGate

Install the Oracle GoldenGate software locally on all nodes in the Oracle Exadata Database Service configuration that will be part of the GoldenGate configuration.

Note:

Make sure the installation directory is the identical on all nodes to match the primary system installation directory.

1. As the `opc` OS user on the standby system, copy the `oggcore.rsp` response file from the primary system to the standby system:
	```
	[opc@standby_node_1 ~]$ scp
	 primary_node_1:/u02/app_acfs/goldengate/oggcore.rsp
	 /u02/app_acfs/goldengate
	```
2. On the standby system, follow “Step 4.2 - Install Oracle GoldenGate” as detailed in [Task 4 - Install Oracle GoldenGate](task-4-install-oracle-goldengate.md).