---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-1-you-begin.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 1 - Before You Begin

Perform the following steps to complete this task:

- Step 1.1 - Set Up the Oracle Cloud Infrastructure DB System
- Step 1.2 - Download the Required Software
- Step 1.3 - Configure Your System to Install Software from Oracle Linux Yum Server
- Step 1.4 - Secure Deployments Requirements (Certificates)

Step 1.1 - Set Up the Oracle Cloud Infrastructure DB System

To get started, you need an Oracle Exadata Database Service on Dedicated Infrastructure or Cloud@Customer for Oracle GoldenGate deployment.

You can deploy Oracle GoldenGate with an existing ExaDB-D/ExaDB-C@C system or launch a new system, according to your business needs.

For instructions on launching and managing an ExaDB-D system, see [Oracle Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en-us/iaas/exadatacloud/index.html) or for ExaDB-C@C see [Oracle Exadata Database Service on Cloud@Customer](https://docs.oracle.com/en-us/iaas/exadata/index.html).

Step 1.2 - Download the Required Software

1. Create the staging directory to download all the required software.
	```
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]# mkdir /u02/app_acfs/goldengate
	[root@exadb-node1 ~]# chown oracle:oinstall /u02/app_acfs/goldengate
	[root@exadb-node1 ~]# chmod g+w /u02/app_acfs/goldengate
	```
2. Download subsequent patches to the base release, go to the Patches and Updates tab of [My Oracle Support](https://support.oracle.com/epmos/faces/PatchHome).
	- See [Installing Patches for Oracle GoldenGate](https://docs.oracle.com/en/middleware/goldengate/core/21.3/coredoc/install-installing-patches-ma.html#GUID-BE9C5FCD-9DC0-4452-B232-123BA82979D0) Microservices Architecture for more information.
		- The minimum required version is Patch 35214851: Oracle GoldenGate 21.9.0.0.2 Microservices for Oracle
3. Download the latest OPatch release, Patch 6880880, for Oracle Database 21c (21.0.0.0.0) from My Oracle Support Document [2542082.1](https://support.oracle.com/rs?type=doc&id=2542082.1).
4. Download the Oracle GoldenGate 21c Microservices software, or higher, from [Oracle GoldenGate Downloads](http://www.oracle.com/technetwork/middleware/goldengate/downloads/index.html).
5. Download the Oracle Grid Infrastructure Standalone Agents for Oracle Clusterware 19c, version 10.2 or higher, from [Oracle Grid Infrastructure Standalone Agents for Oracle Clusterware](http://www.oracle.com/technetwork/database/database-technologies/clusterware/downloads/xag-agents-downloads-3636484.html).
6. Download the `mount-dbfs-version.zip` file with `mount-dbfs.sh` and `mount-dbfs.conf` from My Oracle Support [Document 1054431.1](https://support.oracle.com/rs?type=doc&id=1054431.1).
7. Download the python script (`secureServices.py`) from My Oracle Support [Document 2826001.1](https://support.oracle.com/rs?type=doc&id=2826001.1).

Step 1.3 - Configure Your System to Install Software from Oracle Linux Yum Server

Oracle Linux yum server hosts software for Oracle Linux and compatible distributions. These instructions help you get started configuring your Linux system for Oracle Linux yum server and installing software via yum.

1. As the `root` OS user, create the file `/etc/yum.repos.d/oracle-public-yum-ol7.repo` with the following contents:
	```
	[opc@exadb-node1 ~]$ sudo su -
	[root@exadb-node1 ~]#
	cat > /etc/yum.repos.d/oracle-public-yum-ol7.repo <<EOF
	[ol7_latest]
	name=Oracle Linux $releasever Latest ($basearch)
	baseurl=http://yum$ociregion.oracle.com/repo/OracleLinux/OL7/latest/\$basearch/
	gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
	gpgcheck=1
	enabled=1
	EOF
	```
2. As the `root` OS user, follow [Doc ID 2397264.1](https://support.oracle.com/rs?type=doc&id=2397264.1) to modify the configuration file `/etc/yum.conf` and validate the software repositories are enabled:
	```
	[root@exadb-node1 ~]# yum repolist
	repo id             repo name                                     status
	!public_ol7_latest  Oracle Linux 7.9-6.0.1.el7_9 Latest (x86_64)  19,712+4,957
	repolist: 19,992
	```

Step 1.4 - Secure Deployments Requirements (Certificates)

A secure deployment involves making RESTful API calls and conveying trail data between the Distribution Server and Receiver Server, over SSL or TLS.

You can use your own existing business certificate from your Certificate Authority (CA) or you might create your own certificates.

Contact your systems administrator to follow your corporate standards to create or obtain the server certificate before proceeding. A separate certificate is required for each VIP and Service Manager pair.