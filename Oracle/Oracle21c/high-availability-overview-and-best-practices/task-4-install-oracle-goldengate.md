---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-4-install-oracle-goldengate.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 4 - Install Oracle GoldenGate

Install the Oracle GoldenGate software locally on all nodes in the Oracle Exadata Database Service configuration that will be part of the Oracle GoldenGate configuration. Make sure the installation directory is identical on all nodes.

Perform the following steps to complete this task:

- Step 4.1 - Unzip the Software and Create the Response File for the Installation
- Step 4.2 - Install Oracle GoldenGate
- Step 4-3 - Patch Oracle GoldenGate

Step 4.1 - Unzip the Software and Create the Response File for the Installation

1. As the `oracle` OS user on the first database node, unzip the software:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ unzip
	 /u02/app_acfs/goldengate/213000_fbo_ggs_Linux_x64_Oracle_services_shiphome.zip
	 -d /u02/app_acfs/goldengate
	```
	The software includes an example response file for Oracle Database release 21c and earlier supported releases. Copy the response file to a shared file system, so the same file can be used to install Oracle GoldenGate on all database nodes, and edit the following parameters:
	- `INSTALL_OPTION=ora21c`
		- `SOFTWARE_LOCATION=/u02/app/oracle/goldengate/gg21c                                 (recommended location)`
2. As the `oracle` OS user on the first database node, copy and edit the response file for the installation.
	```
	[oracle@exadb-node1 ~]$ cp
	 /u02/app_acfs/goldengate/fbo_ggs_Linux_x64_Oracle_services_shiphome/Disk1/response/oggcore.rsp
	 /u02/app_acfs/goldengate
	[oracle@exadb-node1 ~]$ vi /u02/app_acfs/goldengate/oggcore.rsp
	# Before edit
	INSTALL_OPTION=
	SOFTWARE_LOCATION=
	# After edit
	INSTALL_OPTION=ora21c
	SOFTWARE_LOCATION=/u02/app/oracle/goldengate/gg21c
	```

Step 4.2 - Install Oracle GoldenGate

As the `oracle` OS user on all database nodes install Oracle GoldenGate:

```
[oracle@exadb-node1 ~]$ cd
 /u02/app_acfs/goldengate/fbo_ggs_Linux_x64_Oracle_services_shiphome/Disk1/
[oracle@exadb-node1 ~]$ ./runInstaller -silent -nowait
 -responseFile /u02/app_acfs/goldengate/oggcore.rsp

Starting Oracle Universal Installer...

Checking Temp space: must be greater than 120 MB.   Actual 32755 MB    Passed
Checking swap space: must be greater than 150 MB.   Actual 16383 MB    Passed
Preparing to launch Oracle Universal Installer from
 /tmp/OraInstall2022-07-08_02-54-51PM. Please wait ...
You can find the log of this install session at:
 /u01/app/oraInventory/logs/installActions2022-07-08_02-54-51PM.log
Successfully Setup Software.
The installation of Oracle GoldenGate Services was successful.
Please check '/u01/app/oraInventory/logs/silentInstall2022-07-08_02-54-51PM.log'
 for more details.

[oracle@exadb-node1 ~]$ cat
 /u01/app/oraInventory/logs/silentInstall2022-07-08_02-54-51PM.log
The installation of Oracle GoldenGate Services was successful.

[oracle@exadb-node1 ~]$ ssh exadb-node2
[oracle@exadb-node2 ~]$ cd
 /u02/app_acfs/goldengate/fbo_ggs_Linux_x64_Oracle_services_shiphome/Disk1
[oracle@exadb-node2 ~]$ ./runInstaller -silent -nowait
 -responseFile /u02/app_acfs/goldengate/oggcore.rsp

Starting Oracle Universal Installer...

Checking Temp space: must be greater than 120 MB.   Actual 32755 MB    Passed
Checking swap space: must be greater than 150 MB.   Actual 16383 MB    Passed
Preparing to launch Oracle Universal Installer from
 /tmp/OraInstall2022-07-08_03-54-51PM. Please wait ...
You can find the log of this install session at:
 /u01/app/oraInventory/logs/installActions2022-07-08_03-54-51PM.log
Successfully Setup Software.
The installation of Oracle GoldenGate Services was successful.
Please check '/u01/app/oraInventory/logs/silentInstall2022-07-08_03-54-51PM.log'
 for more details.

[oracle@exadb-node1 ~]$ cat
 /u01/app/oraInventory/logs/silentInstall2022-07-08_03-54-51PM.log
The installation of Oracle GoldenGate Services was successful.
```

Step 4.3 - Patch Oracle Goldengate

As the `oracle` OS user on all database nodes, install the latest OPatch:

```
[oracle@exadb-node1 ~]$ unzip -oq -d /u01/app/oracle/goldengate/gg21c
 /u02/app_acfs/goldengate /p6880880_210000_Linux-x86-64.zip
[oracle@exadb-node1 ~]$ cat >> ~/.bashrc <<EOF
export ORACLE_HOME=/u01/app/oracle/goldengate/gg21c
export PATH=$ORACLE_HOME/OPatch:$PATH
EOF
[oracle@exadb-node1 ~]$. ~/.bashrc
[oracle@exadb-node1 ~]$ opatch lsinventory |grep 'Oracle GoldenGate Services'

Oracle GoldenGate Services                                           21.1.0.0.0

[oracle@gghub_prim1 Disk1]$ opatch version

OPatch Version: 12.2.0.1.37
```

As the `oracle` OS user, run OPatch `prereq` to validate any conflict before applying the patch:

```
[oracle@exadb-node1 ~]$ unzip -oq -d /u02/app_acfs/goldengate
 /u02/app_acfs/goldengate /p35214851_219000OGGRU_Linux-x86-64.zip
[oracle@exadb-node1 ~]$ cd /u02/app_acfs/goldengate/35214851/
[oracle@exadb-node1 35214851]$ opatch prereq CheckConflictAgainstOHWithDetail -ph ./

Oracle Interim Patch Installer version 12.2.0.1.26
Copyright (c) 2023, Oracle Corporation.  All rights reserved.

PREREQ session
Oracle Home       : /u01/app/oracle/goldengate/gg21c
Central Inventory : /u01/app/oraInventory
   from           : /u01/app/oracle/goldengate/gg21c/oraInst.loc
OPatch version    : 12.2.0.1.26
OUI version       : 12.2.0.9.0
Log file location : /u01/app/oracle/goldengate/gg21c/cfgtoollogs/opatch/opatch2023-04-21_13-44-16PM_1.log

Invoking prereq "checkconflictagainstohwithdetail"

Prereq "checkConflictAgainstOHWithDetail" passed.
```

As the `oracle` OS user on all database nodes, patch Oracle GoldenGate Microservices Architecture using OPatch:

```
[oracle@exadb-node1 ~]$ cd /u02/app_acfs/goldengate/35214851/
[oracle@exadb-node1 35214851]$ opatch apply         

Oracle Interim Patch Installer version 12.2.0.1.37
Copyright (c) 2023, Oracle Corporation.  All rights reserved.

Oracle Home       : /u01/app/oracle/goldengate/gg21c
Central Inventory : /u01/app/oraInventory
   from           : /u01/app/oracle/goldengate/gg21c/oraInst.loc
OPatch version    : 12.2.0.1.37
OUI version       : 12.2.0.9.0
Log file location : /u01/app/oracle/goldengate/gg21c/cfgtoollogs/opatch/opatch2023-04-21_19-40-41PM_1.log
Verifying environment and performing prerequisite checks...
OPatch continues with these patches:   35214851

Do you want to proceed? [y|n]
y
User Responded with: Y
All checks passed.

Please shutdown Oracle instances running out of this ORACLE_HOME on the local system.
(Oracle Home = '/u01/app/oracle/goldengate/gg21c')

Is the local system ready for patching? [y|n]
y
User Responded with: Y
Backing up files...
Applying interim patch '35214851' to OH '/u01/app/oracle/goldengate/gg21c'

Patching component oracle.oggcore.services.ora21c, 21.1.0.0.0...
Patch 35214851 successfully applied.
Log file location: /u01/app/oracle/goldengate/gg21c/cfgtoollogs/opatch/opatch2023-04-21_19-40-41PM_1.log

OPatch succeeded.

[oracle@exadb-node1 35214851]$ opatch lspatches

35214851;
```