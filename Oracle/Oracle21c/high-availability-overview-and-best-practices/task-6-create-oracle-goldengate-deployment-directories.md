---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-6-create-oracle-goldengate-deployment-directories.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 6: Create Oracle GoldenGate Deployment Directories

The Oracle GoldenGate Service Manager and deployment are already created on the primary cluster, as required by the prerequisites, but certain directories and symbolic links need to be configured on the standby cluster nodes.

These directories and symbolic links were created on the primary cluster, in the tasks you performed as part of [On-Premises: Oracle GoldenGate Microservices Architecture with Oracle Real Application Clusters Configuration Best Practices](ogg-microservices-premises1.md).

Now you create the following directories and symbolic links on the all Oracle RAC nodes on the standby cluster as follows.

1. If there are multiple GoldenGate Service Managers configured on the primary cluster, each with their own deployment, and individually registered with XAG, they must belong to separate `OGG_HOME` software installation directories.
	The same directories and symbolic links for the `OGG_HOME` directories that were configured on primary cluster, must match on the standby cluster.
2. If the GoldenGate deployment was created with the Performance Metric Server enabled, the metric datastore home directory must be created on the standby Oracle RAC nodes.
	For example, determine the datastore directory on the primary cluster nodes:
	```
	$ grep RepoDatastorePath <deployment directory>/var/log/pmsrvr.log|uniq
	"RepoDatastorePath": "",
	 "RepoDatastorePath": "/u01/oracle/goldengate/datastores/ggnorth",
	```
	Then create the directory on all standby cluster nodes:
	```
	$ mkdir -p /u01/oracle/goldengate/datastores/ggnorth
	```
3. If the database release is earlier than Oracle Database 21c (21.3), create the Oracle GoldenGate deployment temp directory local storage to match the symbolic link created on the primary cluster.
	For example, on the primary cluster if you have:
	```
	$ ls –lrt DBFS_GoldenGate_deployment_home_directory/var/temp
	lrwxrwxrwx  1 oracle oinstall 32 Aug 31 12:27 temp
	 -> /u01/oracle/goldengate/deployments/ggnorth/temp
	```
	Then create the same directory on the standby cluster nodes:
	```
	$ mkdir –p /u01/oracle/goldengate/deployments/ggnorth/temp
	```