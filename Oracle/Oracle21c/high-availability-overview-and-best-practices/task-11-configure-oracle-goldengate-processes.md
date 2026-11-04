---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/task-11-configure-oracle-goldengate-processes.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Task 11 - Configure Oracle GoldenGate Processes

When creating Extract, Distribution Paths, and Replicat processes with Oracle GoldenGate Microservices Architecture, all files that need to be shared between Oracle RAC nodes are already shared with the deployment files stored on a shared file system (DBFS or ACFS).

Listed below are the essential configuration details recommended for running Oracle GoldenGate Microservices on Oracle RAC for Extract, Distribution Paths, and Replicat processes.

Perform the following steps to complete this task:

- Step 11.1 - Extract Configuration
- Step 11.2 - (DBFS only) Place the Temporary Cache Files on the Shared Storage
- Step 11.3 - Distribution Path Configuration
- Step 11.4 - Replicat Configuration

Step 11.1 - Extract Configuration

When creating an Extract using the Oracle GoldenGate Administration Service GUI interface, leave the `Trail SubDirectory` parameter blank so that the trail files are automatically created in the deployment directories stored on the shared file system. The default location for trail files is the `/<deployment directory>/var/lib/data` directory.

Note:

To capture from a multitenant database, you must use an Extract configured at the root level using a `c##` account. To apply data into a multitenant database, a separate Replicat is needed for each PDB because a Replicat connects at the PDB level and doesn't have access to objects outside of that PDB

Create the database credentials:

1. Log in to the Oracle GoldenGate Administration Server in the Source Oracle GoldenGate.
2. Click in Overview under Administration Service.
3. Click the plus button to Add Extract.
4. Select Integrated Extract.
5. Add the required information.
6. Click Next.
7. If using CDB Root Capture from PDB, add the `SOURCATALOG` parameter with the PDB Name.
8. Click Create.

Step 11.2 - (DBFS only) Place the Temporary Cache Files on the Shared Storage

If you are using DBFS for shared storage, and the deployment `var/temp` directory was moved to local storage as described in [Task 5 - Create the Oracle GoldenGate Deployment](task-5-create-oracle-goldengate-deployment.md), it is recommended that you use the Extract `CACHEMGR` parameter to place the temporary cache files on the shared storage.

1. As the `oracle` OS user, create a new directory under the DBFS deployment mount point.:
	```
	[opc@exadb-node1 ~]$ sudo su - oracle
	[oracle@exadb-node1 ~]$ mkdir
	 /mnt/dbfs/goldengate/deployments/<instance_name>/temp_cache
	```
2. Set the Extract parameter to the new directory:
	```
	CACHEMGR CACHEDIRECTORY
	 /mnt/dbfs/goldengate/deployments/<instance_name>/temp_cache
	```

More instructions about creating an Extract process are available in [Using Oracle GoldenGate Classic Architecture with Oracle Database](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/index.html).

Step 11.3 - Distribution Path Configuration

When using Oracle GoldenGate Distribution paths with the NGINX Reverse Proxy, additional steps must be carried out to ensure the path client and server certificates are configured.

More instructions about creating distribution paths are available in [Oracle GoldenGate Microservices Documentation](https://docs.oracle.com/en/middleware/goldengate/core/21.3/coredoc). A step-by-step example is in the following video, “ [Connect an on-premises Oracle GoldenGate to OCI GoldenGate using NGINX,”](https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:31380) to correctly configure the certificates.

Perform the following sub-steps to complete this step:

- Step 11.3.1 - Download the Target Server’s Root Certificate, and then upload it to the source Oracle GoldenGate
- Step 11.3.2 - Create a user in the Target Deployment for the Source Oracle GoldenGate to use
- Step 11.3.3 - Create a Credential in the Source Oracle GoldenGate
- Step 11.3.4 - Create a Distribution Path on the Source Oracle GoldenGate to the Target Deployment
- Step 11.3.5 - Verify the Connection in the Target Deployment Console Receiver Service

Step 11.3.1 - Download the Target Server’s Root Certificate, and then upload it to the source Oracle GoldenGate

Download the target deployment server’s root certificate and add the CA certificate to the source deployment Service Manager.

1. Log in to the Administration Service on the Target GoldenGate.
2. Follow “Step 2 - Download the target server’s root certificate” in the video “ [Connect an on-premises Oracle GoldenGate to OCI GoldenGate using NGINX](https://apexapps.oracle.com/pls/apex/f?p=44785:112:0::::P112_CONTENT_ID:31380).”

Step 11.3.2 - Create a user in the Target Deployment for the Source Oracle GoldenGate to use

Create a user in the target deployment for the distribution path to connect to:

1. Log in to the Administration Service on the Target GoldenGate.
2. Click Administrator under Administration Service.
3. Click the plus (+) sign next to Users.
4. Enter the details.

Step 11.3.3 - Create a Credential in the Source Oracle GoldenGate

Create a credential in the source deployment connecting the target deployment with the user created in the previous step. For example, a domain of OP2C and an alias of WSSNET.

1. Log in to the Administration Service on the Source Oracle GoldenGate.
2. Click Configuration under Administration Service.
3. Click the plus (+) sign next to Credentials on the Database home page. The Add Credentials page is displayed.
4. Enter the details.

Step 11.3.4 - Create a Distribution Path on the Source Oracle GoldenGate to the Target Deployment

A path is created to send trail files from the Distribution Server to the Receiver Server. You can create a path from the Distribution Service.

To add a path for the source deployment:

1. Log in to the Distribution Service on the Source Oracle Goldengate.
2. Click the plus (+) sign next to Path on the Distribution Service home page. The Add Path page is displayed.
3. Enter the details as follows:
	| Option | Description |
	| --- | --- |
	| Path Name | Select a name for the path. |
	| Source: Trail Name | Select the Extract name from the drop-down list, which populates the trail name automatically. If it doesn’t, enter the trail name you provided while adding the Extract. |
	| Generated Source URI | Specify localhost for the server’s name; this allows the distribution path to be started on any of the Oracle RAC nodes. |
	| Target Authentication Method | Use `UserID Alias` |
	| Target | Set the Target transfer protocol to wss (secure web socket). Set the Target Host to the target hostname/VIP that will be used for connecting to the target system along with the Port Number that NGINX was configured with (default is 443). |
	| Domain | Set the Domain to the credential domain created above in Step 11.3.3, for example, OP2C. |
	| Alias | The Alias is set to the credential alias wssnet, also created in Step 11.3.3. |
	| Auto Restart Options | Set the distribution path to restart when the Distribution Server starts automatically. This is required, so that manual intervention is not required after an Oracle RAC node relocation of the Distribution Server. It is recommended to set the number of Retries to 10. Set the Delay, which is the time in minutes to pause between restart attempts, to 1. |
4. Click Create Path.
5. From the Action Menu, click Start.
6. Verify that the Distribution Service is running.

Step 11.3.5 - Verify the Connection in the Target Deployment Console Receiver Service

1. Log in to the Administration Service on the Target Deployment Console.
2. Click on Receiver Service.

Step 11.4 - Replicat Configuration

The Replicat process receives the trail data and applies it to the database.

Perform the following sub-steps to complete this step:

- Step 11.4.1 - Create the Checkpoint Table
- Step 11.4.2 - Add a Replicat

Step 11.4.1 - Create the Checkpoint Table

The checkpoint table is a required component for Oracle GoldenGate Replicat processes. After connecting to the database from the Credentials page of the Administration Service, you can create the checkpoint table.

Create the checkpoint table in the target deployment:

1. Log in to the Administration Service on the Target GoldenGate.
2. Click Configuration under Administration Service.
3. Click Database and Connect to the target database or PDB.
4. Click the plus (+) sign next to Checkpoint. The Add Checkpoint page is displayed.
5. Enter the details.

See [About Checkpoint Table](https://docs.oracle.com/en/middleware/goldengate/core/21.3/oracle-db/configuring-oracle-goldengate-apply.html#GUID-3DFBE2BE-20C5-48AA-B96A-7697126D77FE) for more information about the checkpoint table.

Step 11.4.2 - Add a Replicat

After you set up your database connections and verified them, you can add a Replicat for the deployment by following these steps:

1. Log in to the Administration Service on the Target GoldenGate.
2. Click the plus (+) sign next to Replicats on the Administration Service home page. The Add Replicat page is displayed.
3. Select a Replicat type and click Next.
4. Enter the details as follows:
	| Option | Description |
	| --- | --- |
	| Process Name | The name of the Replicat process |
	| Credential Domain | Credential domain created in Step 9.2. In our example is `GoldenGate` |
	| Credential Alias | Credential alias created in Step 9.2. Our example is `Target_PDB` |
	| Source | Select the source to use Trail. |
	| Trail Name | A two-character trail name. |
	| Checkpoint Table | Set the use of an existing checkpoint table. |
5. Click Create Path.
6. From the Action Menu, click Start.
7. Verify that the Replicat is running.