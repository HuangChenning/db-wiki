---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-6-create-oracle-goldengate-deployment.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 6: Create the Oracle GoldenGate Deployment

Once the Oracle GoldenGate software has been installed, the next step is to create a deployment using the Oracle GoldenGate Configuration Assistant (`oggca`).

There are two limitations that currently exist with Oracle GoldenGate and XAG:

1. A Service Manager that is registered with XAG can only manage a single deployment. If multiple deployments are required, each deployment must use their own Service Manager. Oracle GoldenGate release 21c simplifies this requirement because it uses a single deployment to support Extract and Replicat processes connecting to different versions of the Oracle Database.
2. Each Service Manager registered with XAG must belong to separate `OGG_HOME` software installation directories. Instead of installing Oracle GoldenGate multiple times, the recommended approach is to install Oracle GoldenGate one time, and then create a symbolic link for each Service Manager `OGG_HOME`.

For example:

```
$ echo $OGG_HOME
/u01/oracle/goldengate/gg21c_MS

$ ln –s /u01/oracle/goldengate/gg21c_MS /u01/oracle/goldengate/gg21c_MS_ggnorth

$ export OGG_HOME=/u01/oracle/goldengate/gg21c_MS_ggnorth
$ $OGG_HOME/bin/oggca.sh
```

The symbolic link and `OGG_HOME` environment variable must be configured before running the Oracle GoldenGate Configuration Assistant on all Oracle RAC nodes.

Recommendations for creating the GoldenGate deployment in the Oracle GoldenGate Configuration Assistant are as follows.

1. In Service Manager Options, specify the following for the creation of a new Service Manager.
	1. In the Service Manager Details pane, select Create New Service Manager.
		2. Enter the Service Manager Deployment Home location on the shared DBFS or ACFS file system.
		3. Select to Integrate with XAG.
		4. In the Service Manager Connection Details pane, specify `localhost` in the Listening hostname/address field.
		Using `localhost` allows the deployment to be started on all of the Oracle RAC nodes without the need for a Virtual IP address (VIP).
		5. Enter the port number in Listening port.
2. In Deployment Directories, specify the Deployment home directory on the shared DBFS or ACFS file system.
3. In Environment Variables, specify a correct TNS\_ADMIN directory.
	Starting with Oracle GoldenGate release 21.3, a database `ORACLE_HOME` is no longer required because the required database libraries are installed as part of the Oracle GoldenGate installation. It is recommended that you use `TNS_ADMIN` directory outside of any existing `ORACLE_HOME` directories.
4. In Security Options, do not select SSL/TLS Security.
	External access to the Oracle GoldenGate Microservices server is achieved by using NGINX Reverse Proxy SSL-termination. Secure access and communication to the GoldenGate deployments will be exclusively through the SSL port 443. Internal connectivity within the same local host between NGINX and GoldenGate does not require SSL.
5. In Port Settings, if the Management Pack for Oracle GoldenGate has been licensed, select Enable Monitoring to use the performance metric server using either Berkeley Database (BDB) or Lightening Memory Database (LMDB).
	For both BDB and LMDB Metrics Service DataStore types, set the Metrics Service DataStore home directory to a local directory that exists on all Oracle RAC nodes. For example: `/u01/oracle/goldengate/datastores/deployment                                 name`
6. Continue through the Oracle GoldenGate Configuration Assistant until the deployment is created.
7. After the deployment has been created, if you are using DBFS for the shared file system and the database version is a release earlier than Oracle Database Release 21c (21.3), run the following commands to move the Oracle GoldenGate deployment temp directory from DBFS to local storage.
	On the first node:
	```
	$ cd <DBFS GoldenGate deployment home directory/var
	$ mkdir -p local_storage_directory/deployment_name
	$ mv temp local_storage_directory/deployment_name
	$ ln -s local_storage_directory/deployment_name/temp temp
	```
	On all other nodes:
	```
	$ mkdir local_storage_directory/deployment_name/temp
	```
	First node example:
	```
	$ cd /mnt/dbfs/goldengate/deployments/ggnorth/var
	$ mkdir –p /u01/oracle/goldengate/deployments/ggnorth
	$ mv temp /u01/oracle/goldengate/deployments/ggnorth
	$ ln -s /u01/oracle/goldengate/deployments/ggnorth/temp temp
	```
	On all other nodes:
	```
	$ mkdir /u01/oracle/goldengate/deployments/ggnorth/temp
	```