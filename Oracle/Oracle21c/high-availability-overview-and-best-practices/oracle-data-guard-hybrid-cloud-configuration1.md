---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/oracle-data-guard-hybrid-cloud-configuration1.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 37 Oracle Data Guard Hybrid Cloud Configuration

A hybrid Oracle Data Guard configuration consists of a primary database and one or more standby databases residing partially on-premises and partially in the Oracle OCI cloud or Oracle multicloud (for example, Oracle Database@Azure, Oracle Database@Google, or Oracle Database@AWS).

Note that the term **Oracle Cloud** refers to both Oracle OCI and Oracle multicloud going forward.

The process detailed in this topic uses the Oracle Database as a Service (DBaaS) tools to create a cloud standby database from an existing on-premises primary database. Oracle DBaaS tools streamline and simplify the process of creating the standby database in Oracle Cloud while incorporating MAA best practices.

After establishing the cloud standby database as described here, you can perform a role transition so that the primary database runs in the cloud instead of on-premises, and Oracle Data Guard life-cycle operations (switchover, failover, and reinstate) are available using the `dbcactl/dbaascli` commands.

Note:

Additional manual steps may be required during configuration if there are standby databases residing on-premises.

### Benefits Of Hybrid Data Guard in the Oracle Cloud

The following are the primary benefits to using a hybrid Data Guard configuration in the Oracle Cloud.

- Flexibility to use Oracle Cloud Infrastructure data centers to supplement an on-premises data center footprint for disaster recovery or other purposes
- Oracle manages the cloud data center and infrastructure
- Ability to switch over (planned events) or fail over (unplanned events) production to the standby database in the cloud during scheduled maintenance or unplanned outages.
	Once a failed on-premises database is repaired, it can be synchronized with the current production database in the cloud. Then, production can be switched back to the on-premises database if required.
- Use the same Oracle MAA best practices as the on-premises deployment. Additional Oracle MAA best practices specific to hybrid Data Guard deployments are specified in the topics that follow. When configured with MAA best practices, a hybrid Data Guard configuration provides:
	- Recovery Time Objective (RTO) of seconds when configured with Data Guard fast-start failover and its automatic failover benefits
		- Recovery Point Objective (RPO) less than a second for Data Guard with ASYNC transport
		- RPO zero for Data Guard in a Maximum Availability protection mode that leverages a SYNC or FAR SYNC configuration

### MAA Recommendations for Using Exadata Cloud for Disaster Recovery

When deploying Exadata Cloud for Disaster Recovery, Oracle MAA recommends:

- Create a cloud database system target that is symmetric or similar to the on-premises primary database to ensure performance SLAs can be met after a role transition. For example, create an Oracle RAC target for an Oracle RAC source, Exadata for Exadata, and so on.
- Ensure that network bandwidth can handle peak redo rates in addition to existing network traffic.
	My Oracle Support document [Assessing and Tuning Network Performance for Data Guard and RMAN (Doc ID 2064368.1)](https://support.oracle.com/rs?type=doc&id=2064368.1) provides additional network bandwidth troubleshooting guidance for assessing and tuning network performance for Data Guard and RMAN.
- Ensure network reliability and security between on-premises and the Cloud environment.
- Use Oracle Active Data Guard for additional automatic block repair, data protection, and offloading benefits.
- Use Oracle Transparent Data Encryption (TDE) for both primary and standby databases.
	My Oracle Support document [Oracle Database Tablespace Encryption Behavior in Oracle Cloud (Doc ID 2359020.1)](https://support.oracle.com/rs?type=doc&id=2359020.1) has additional details on TDE behavior in cloud configurations.
- Configure backups to Autonomous Recovery Service or Object Storage for the Oracle databases, in primary or standby role. See [Manage Database Backup and Recovery on Oracle Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-managing-db-backup-and-recovery.html#ECSCM-GUID-07D1B1D6-4A06-4859-B7DF-4C3A681A6B40) and [Database Autonomous Recovery Service](https://docs.public.oneportal.content.oci.oraclecloud.com/iaas/recovery-service/doc/overview-recovery-service.html).

### Security Requirements and Considerations

Oracle MAA best practices recommend using Oracle Transparent Data Encryption (TDE) to encrypt the primary and standby databases to ensure that data is encrypted at-rest.

Using TDE to protect data is an essential part of improving the security of the system. Note the following variables that need to be considered when evaluating TDE.

- CPU overhead - Encryption requires additional CPU cycles to calculate encrypted and decrypted values. TDE, however, is optimized to minimize the overhead by taking advantage of database caching capabilities and leveraging hardware acceleration within Exadata. Most TDE users see little performance impact on their production systems after enabling TDE.
- Lower data compression - Encrypted data compresses less efficiently than non-encrypted data, so any compression applied to data encrypted with TDE results in lower compression ratios. When TDE encryption is used, redo transport compression is not recommended or typically required since data in the redo is already encrypted; however, when TDE is used in conjunction with Oracle Database compression technologies such as Advanced Compression or Hybrid Columnar Compression, compression is performed before the encryption occurs, and the benefits of compression and encryption are both achieved.
- Key management - Encryption is only as strong as the encryption key used and the loss of the encryption key is tantamount to losing all data protected by that key.
	If encryption is enabled on a few databases, keeping track of the key and its life cycle is relatively easy. As the number of encrypted databases grows, managing keys becomes an increasingly difficult problem. If you are managing a large number of encrypted databases, it is recommended that Oracle Key Vault be used on-premises to store and manage TDE master keys.

Data can be converted during the migration process, but it is recommended that TDE be enabled before beginning the migration to provide the most secure Oracle Data Guard environment. A VPN connection or Oracle Net encryption is also required for inflight encryption for any other database payload that is not encrypted by TDE, such as data file or redo headers for example. See My Oracle Support document [Oracle Database Tablespace Encryption Behavior in Oracle Cloud (Doc ID 2359020.1)](https://support.oracle.com/rs?type=doc&id=2359020.1) for more information.

If the on-premises database is not already enabled with TDE, see My Oracle Support document [Primary Note For Transparent Data Encryption ( TDE ) (Doc ID 1228046.1)](https://support.oracle.com/rs?type=doc&id=1228046.1) to enable TDE and create wallet files.

If TDE cannot be enabled for the on-premises database, see [Encryption of Tablespaces in an Oracle Data Guard Environment](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=ASOAG-GUID-6B769BE8-5312-406F-BD28-51C3C0CCC33D) in Oracle Database Advanced Security Guide for information about decrypting redo operations in hybrid cloud disaster recovery configurations where the Cloud database is encrypted with TDE and the on-premises database is not.

### Platform, Database, and Network Prerequisites

The following requirements must be met to ensure a successful migration to a Cloud standby database.

| Requirement Type | On-Premises Requirements | Oracle Cloud Requirements |
| --- | --- | --- |
| Operating System | Linux, Windows or Solaris X86 (My Oracle Support Note 413484.1 for Data Guard cross-platform compatibility) | Oracle Enterprise Linux (64-bit) |
| Oracle Database Version\* | Extreme performance / BYOL\*  See [Supported Database Editions and Versions](https://docs.oracle.com/en-us/iaas/dbcs/doc/bare-metal-and-virtual-machine-db-systems.html#DBSCB-GUID-AFDF235F-FED1-4FF4-A10D-D067ACD80C9D) for information about database service options in Oracle Cloud. | Extreme performance / BYOL\*  See [Supported Database Editions and Versions](https://docs.oracle.com/en-us/iaas/dbcs/doc/bare-metal-and-virtual-machine-db-systems.html#DBSCB-GUID-AFDF235F-FED1-4FF4-A10D-D067ACD80C9D) for information about database service options in Oracle Cloud. |
| Oracle Database Architecture | Oracle RAC or single-instance | Oracle RAC or single-instance |
| Oracle Multitenant | For Oracle 12.1 and above, the primary database must be a multitenant container database (CDB) | Multitenant container database (CDB) or non-CDB |
| Physical or Virtual Host | Physical or Virtual | Exadata Virtual |
| Database Size | Any size | Any size.  For shape limits please consult Exadata Cloud documentation |
| TDE Encryption | Recommended | Mandatory for Cloud databases |

\* The Oracle Database release on the primary and standby databases should be the same database major release and database release update (RU) during initial standby instantiation. For database software updates that are standby-first compatible, the primary and standby database Oracle Home software can be different (for example, 19RU vs 19 RU+1). For the standby instantiation in the Oracle cloud, the standby database Oracle Home software must be the same or a later RU. See [Oracle Patch Assurance - Data Guard Standby-First Patch Apply (Doc ID 1265700.1)](https://support.oracle.com/rs?type=doc&id=1265700.1).

#### Cloud Network Prerequisites

Data transfers from on-premises to Oracle Cloud use the public network, VPN, and/or the high bandwidth option provided by Oracle FastConnect.

In an Oracle Data Guard configuration, the primary and standby databases must be able to communicate bi-directionally. This requires additional network configuration to allow access to ports between the systems.

Note:

Network connectivity configuration is not required for Oracle Exadata Database Service on Cloud@Customer because it is deployed on the on-premises network. Skip to On-Premises Prerequisites if you are using ExaDB-C@C.

Secure Connectivity

For Oracle Exadata Database Service (not required for ExaDB-C@C) there are two options to privately connect the virtual cloud network to the on-premises network: FastConnect and IPSec VPN. Both methods require a Dynamic Routing Gateway (DRG) to connect to the private Virtual Cloud Network (VCN).

See [Access to Your On-Premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/connectivityonprem.htm) for details about creating a DRG.

- OCI FastConnect - Provides an easy way to create a dedicated, private connection between the data center and OCI. FastConnect provides higher bandwidth options and a more reliable and consistent networking experience compared to internet-based connections. See [FastConnect Overview](https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm). (link https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm) for details.
- IPSec VPN - Internet Protocol Security or IP Security (IPSec ) is a protocol suite that encrypts the entire IP traffic before the packets are transferred from the source to the destination. See [Site-to-Site VPN Overview](https://docs.oracle.com/iaas/Content/Network/Tasks/overviewIPsec.htm) for an overview of IPSec in OCI.

Public Internet Connectivity

Connectivity between OCI and on-premises can also be achieved using the public internet.

This method is not secure by default; additional steps must be taken to secure transmissions. The steps for hybrid Data Guard configuration assume public internet connectivity.

By default, cloud security for port 1521 is disabled. Also, this default pre-configured port in the cloud for either a Virtual Machine (VM) or Bare Metal (BM) has open access from the public internet.

1. If a Virtual Cloud Network (VCN) for the standby database doesn't have an Internet Gateway, one must be added.
	To create an internet gateway see [Internet Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/managingIGs.htm).
2. Ingress and egress rules must be configured in the VCN security list to connect from and to the on-premises database.
	See [Security Lists](https://docs.oracle.com/iaas/Content/Network/Concepts/securitylists.htm) for additional information.

#### On-Premises Prerequisites

The following prerequisites must be met before instantiating the standby database.

##### Evaluate Network Using oratcptest

In an Oracle Data Guard configuration, the primary and standby databases transmit information in both directions. This requires basic configuration, network tuning, and opening of ports at both the primary and standby databases.

It is vital that the bandwidth exists to support the redo generation rate of the primary database.

Follow instructions in [Assessing and Tuning Network Performance for Data Guard and RMAN (Doc ID 2064368.1)](https://support.oracle.com/rs?type=doc&id=2064368.1) to assess and tune the network link between the on-premises and cloud environments.

##### Configuration

- Name resolution
	- For ExaDB-C@C, because the clusters reside on the on-premises network, the on-premises DNS should resolve each cluster, and no further configuration should be necessary.
		- For Oracle Exadata Database Service, name resolution between the clusters must be configured.
		This can be done either using a static file like /etc/hosts, or by configuring the on-premises DNS to properly resolve the public IP address of the OCI instance. In addition, the on-premises firewall must have Access Control Lists configured to allow SSH and Oracle Net to be accessed from the on-premises system to OCI.
- Oracle Data Guard in a DR configuration requires access from the Cloud instance to the on-premises database; the primary database listener port must be opened with restricted access from the Cloud IP addresses using features like `iptables`.
	Because every corporation has different network security policies, the network administrator must perform operations like the cloud-side network configuration shown in Cloud Network Prerequisites.
- Prompt-less SSH from Oracle Cloud to the on-premises machine. This is configured both for on-premises to Cloud during the provisioning process and from the Cloud to on-premises.
- The configuration of the on-premises firewall to allow inbound SSH connectivity from the Cloud to the on-premises machine.
- It is strongly recommended that you complete the network assessment described above in Evaluate Network Using oratcptest. Setting the appropriate TCP socket buffers setting is especially important for ASYNC redo transport.
- It is recommended that the RDBMS software be the same on the primary and standby database for instantiation. If the current on-premises Oracle Database release is not available in Oracle Exadata Database Service, then the primary database must be on the same major database release and the same or lower Release Update (RU).

##### Implement MAA Best Practice Parameter Settings on the Primary Database

Most MAA best practices for Data Guard are part of the process described here; however, the Standby Redo Log should be created on the primary database before starting this process.

See [Oracle Data Guard Configuration Best Practices](configure-and-deploy-oracle-data-guard.md) for information.

##### Validating Connectivity between On-Premises and Exadata Cloud Hosts

After the networking steps are implemented successfully, run the command below to validate that the connection is successful between all sources and all targets in both directions.

1. As the `oracle` OS user on all nodes of the on-premises environment, use `curl` to test connectivity between all on-premises and all cloud nodes.
	```
	[oracle@on-prem1]$ curl -v telnet://<FQDN-CLOUD-HOST1>:22 (or other available port)
	* Rebuilt URL to: telnet://<FQDN-CLOUD-HOST1>:22/
	*   Trying <CLOUD-HOST1-IP>...
	* TCP_NODELAY set
	* Connected to <FQDN-CLOUD-HOST1> (<CLOUD-HOST1-IP>) port 22 (#0)
	SSH-2.0-OpenSSH_8.0
	^C
	[oracle@on-prem1]$
	```
2. As the `oracle` OS user on all nodes of the cloud environment, use `curl` to test connectivity between all cloud and all on-premises nodes.
	```
	[oracle@cloud-exadata1]$ curl -v telnet://<FQDN-ON-PREM-HOST1>:22 (or other available port)
	* Rebuilt URL to: telnet://<FQDN-CLOUD-HOST1>:22/
	*   Trying <ON-PREM-HOST1-IP>...
	* TCP_NODELAY set
	* Connected to <FQDN-ON-PREM-HOST1> (<ON-PREM-HOST1-IP>) port 22 (#0)
	SSH-2.0-OpenSSH_8.0
	^C
	[oracle@cloud-exadata1]$
	```

If `curl` connection is successful, proceed to the next step.

Note:

Successful connections will get the message "Connected to \<FQDN-HOST1> (\<HOST-IP>) port 22", while unsuccessful connections will get the message "Failed to connect to \<FQDN-HOST1> port 22: Connection refused"

#### Prepare the Primary Database Environment

The Hybrid Data Guard configuration process uses the Oracle Cloud DBaaS tools and automation to ensure the process used to create the standby database is the same process as is used in the Oracle Cloud.

This will ensure that the cloud database is visible in the cloud user interface.

Because the on-premises database is not a cloud created database, some steps are required to ensure successful completion.

##### Create an ACFS Mount Point

Hybrid Data Guard configurations require an ACFS mount point for sharing files between instances, for example tnsnames.ora and TDE wallets.

This mount point exists in cloud platforms in `/var/opt/oracle/dbaas_acfs`. If there is no existing ACFS mount point for the primary cluster create one using the steps in [Creating an Oracle ACFS File System](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=OSTMG-GUID-4C98CF06-8CCC-45F1-9316-C40FB3EFF268). (An existing ACFS mount point can be used)

##### Configure Transparent Data Encryption on the Source Database

Transparent Data Encryption (TDE) is required on Oracle Cloud databases, including any standby database which is part of a hybrid Data Guard configuration.

While it is strongly recommended that the on-premises database also be encrypted, leaving the primary database unencrypted as part of a hybrid Data Guard configuration can be configured and is better supported by new parameters in Oracle Database 19c (19.16) and later releases.

For all TDE configurations with Oracle Data Guard, the encryption wallet must be created on the primary database and the master key must be set whether or not the primary database will be encrypted with TDE.

The parameters required for TDE configuration differ depending with Oracle Database releases. The values may be different for each database in the Data Guard configuration.

- In Oracle Database release 19c (19.16) and later, the parameters `TABLESPACE_ENCRYPTION`, `WALLET_ROOT`, and `TDE_CONFIGURATION` are required to properly configure TDE.
- For Oracle Database 19c releases before 19.16, set parameters `WALLET_ROOT`, `TDE_CONFIGURATION`, and `ENCRYPT_NEW_TABLESPACES`.
- For releases earlier than Oracle Database19c, set parameters `ENCRYPTION_WALLET_LOCATION` and `ENCRYPT_NEW_TABLESPACES`.

Note:

Unless otherwise specified by the `TABLESPACE_ENCRYPTION=DECRYPT_ONLY` parameter, a new tablespace's encryption on the standby database will be the same as that of the primary.

In the following table use the links to find references for setting the primary and standby database parameters.

| Parameter | Definition | All Oracle Database releases before 19c | Oracle Database release 19.15 and earlier | Oracle Database release 19.16 and later |
| --- | --- | --- | --- | --- |
| [ENCRYPTION\_WALLET\_LOCATION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=ASOAG-GUID-DF9504EF-BA08-4585-895D-2E5F4BA30E50) | Defines the location of the wallet | RECOMMENDED | DEPRECATED | DEPRECATED |
| [WALLET\_ROOT](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=REFRN-GUID-37347728-3D24-444A-A9ED-5B981C4EA2D3) and [TDE\_CONFIGURATION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=REFRN-GUID-285A9BCE-22AE-4DE4-A76E-1319B7BB91BC) | `WALLET_ROOT` sets the location of the root of the directory for wallet storage for each PDB in a CDB.  `TDE_CONFIGURATION` defines the type of keystore. For example, `FILE` for a wallet keystore. The keystore type must be set to the same value on the primary and standby database. | N/A | RECOMMENDED | RECOMMENDED |
| [ENCRYPT\_NEW\_TABLESPACES](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=REFRN-GUID-44EF2AAC-1313-4437-B0F3-A427F45016F2) | Indicates whether a new tablespace on the primary database should be encrypted  The `ENCRYPT_NEW_TABLESPACES` parameter can be set as follows:  - `CLOUD_ONLY` - Default setting. Any new tablespaces created are transparently encrypted with the AES128 algorithm, unless a different algorithm is specified in the `ENCRYPTION` clause in the `CREATE TABLESPACE` statement. For on-premises databases, tablespaces are only encrypted if the `CREATE TABLESPACE...ENCRYPTION` clause is specified. - `ALWAYS` - Any new tablespace created in a primary database, on-premises or in the cloud, will be transparently encrypted with the AES128 algorithm, unless a different encryption algorithm is specified in the `CREATE TABLESPACE ENCRYPTION` clause. - `DDL` - Allows you to create tablespaces with or without encryption following the `CREATE                                             TABLESPACE` command, and also lets you change the encryption algorithm. Note: This value is not applicable for cloud primary databases with releases from Oracle Database 19c (19.16) and later because tablespace encryption is enforced. | RECOMMENDED | RECOMMENDED | NOT RECOMMENDED  Override with recommended setting for `TABLESPACE_ENCRYPTION` |
| [TABLESPACE\_ENCRYPTION](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=REFRN-GUID-42408BFB-1A3F-4BAA-B0E9-1AA0CD48FA5A) (see note above) | Oracle Database 19c (19.16) and later releases - indicates whether a new tablespace should be encrypted. Available options are `AUTO_ENABLE`, `MANUAL_ENABLE`, and `DECRYPT_ONLY`.  Starting with Oracle Database 19c (19.16), Oracle Cloud forces encryption for all tablespaces in the cloud database. This cannot be overridden.  To prevent encrypted tablespaces on an on-premises database (primary or standby) set the `TABLESPACE_ENCRYPTION` parameter to `DECRYPT_ONLY`.  `DECRYPT_ONLY` is only valid in an on-premises database. | N/A | N/A | RECOMMENDED |

To configure Transparent Data Encryption using a TDE wallet follow the steps in [Configuring Transparent Data Encryption](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=ASOAG-GUID-C5D20EAE-3369-411F-9A7E-13AB14139F1D).

##### Check the TDE Master Key Before Instantiation

Even in cases where the primary database remains unencrypted, TDE must be configured on the primary database. This configuration includes creating the encryption wallet and setting the master key.

During the process the wallet is copied to the standby database. The master key stored in the wallet will be used by the standby database for encryption.

In the event of a switchover where the cloud standby database becomes the primary database, the key is used by the unencrypted on-premises database to decrypt the encrypted redo from the cloud database.

Failure to set the master key will result in failure of Data Guard managed recovery.

To confirm the master key is set properly:

- Verify that the `MASTERKEYID` column in V$ `DATABASE_KEY_INFO` matches a key existing in `V$ENCRYPTION_KEYS` on the source database.
	In a multitenant container database (CDB) environment, check `CDB$ROOT` and all the PDBs except `PDB$SEED`.

##### Configure Online Redo Logs

Redo log switches can have a significant impact on redo transport and apply performance.

Follow these best practices for sizing the online redo logs on the primary database before instantiation.

- All online redo log groups should have identically sized logs (to the byte).
- Online redo logs should reside on high performing disks (DATA disk groups) and on high redundancy disk groups if possible.
- Create a minimum of three online redo log groups per thread of redo on Oracle RAC instances.
- Create online redo log groups on shared disks in an Oracle RAC environment.
- Do not multiplex online redo logs (multiple members per log group) unless they are not placed on high redundancy disk groups.
- Size online redo logs to switch no more than 12 times per hour (every ~5 minutes) during peak workloads.

##### Size Redo Logs

Size redo logs based on the peak redo generation rate of the primary database.

You can determine the peak rate by running the query below for a time period that includes the peak workload.

The peak rate could be seen at month-end, quarter-end, or annually. Using the guidance above, size the redo logs to handle the highest rate +10% in order for redo apply to perform consistently during these workloads.

```
SQL> SELECT thread#,sequence#,blocks*block_size/1024/1024 MB,
(next_time-first_time)*86400 sec,
 blocks*block_size/1024/1024)/((next_time-first_time)*86400) "MB/s"
 FROM v$archived_log
 WHERE ((next_time-first_time)*86400<>0)
 and first_time between to_date('2015/01/15 08:00:00','YYYY/MM/DD HH24:MI:SS')
 and to_date('2015/01/15 11:00:00','YYYY/MM/DD HH24:MI:SS')
 and dest_id=1 order by first_time;

   THREAD#  SEQUENCE#         MB        SEC       MB/s 
---------- ---------- ---------- ---------- ---------- 
         2       2291 29366.1963        831  35.338383 
         1       2565 29365.6553        781 37.6000708 
         2       2292 29359.3403        537  54.672887 
         1       2566 29407.8296        813 36.1719921 
         2       2293 29389.7012        678 43.3476418 
         2       2294 29325.2217       1236 23.7259075 
         1       2567 11407.3379       2658 4.29169973 
         2       2295 29452.4648        477 61.7452093 
         2       2296 29359.4458        954 30.7751004 
         2       2297 29311.3638        586 50.0193921 
         1       2568 3867.44092       5510 .701894903
```

Choose the redo log size based on the peak generation rate with the following chart.

| Peak Redo Rate | Recommended Redo Log Size |
| --- | --- |
| <= 1 MB/s | 500 MB |
| <= 5 MB/s | 1 GB |
| <= 25 MB/s | 8 GB |
| <= 50 MB/s | 16 GB |
| \> 50 MB/s | 32 GB |

##### Enable Flashback Database

Flashback Database allows reinstatement of the old primary database as a standby database after a failover.

Without Flashback Database enabled, the old primary database would have to be recreated as a standby after a failover. If flashback database has not already been enabled, enable it now.

To enable flashback database, make sure you have sufficient space and I/O throughput in your Fast Recovery Area or RECO disk group, and evaluate any performance impact.

As the `oracle` OS user on the first node of the on-premises environment, run the command below to enable flashback database on the primary if it is not already enabled.

```
[oracle@on-prem1]$ echo "alter database flashback on;" | sqlplus -SILENT "/ as sysdba"

Database altered.
```

##### Configure Redo Transport - Oracle Net Encryption

To protect against plain text or unencrypted tablespace redo from being visible on the WAN, place the following entries in the `sqlnet.ora` file on all on-premises database nodes.

These values should already be set by the deployment tool in cloud configurations.

```
#SQLNET.ORA ON ON-PREMISES HOST(S)
SQLNET.CRYPTO_CHECKSUM_CLIENT=ACCEPTED
SQLNET.CRYPTO_CHECKSUM_SERVER=ACCEPTED
SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT=(SHA256,SHA384,SHA512,SHA1)
SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER=(SHA256,SHA384,SHA512)
SQLNET.ENCRYPTION_CLIENT=REQUESTED
SQLNET.ENCRYPTION_SERVER=REQUESTED
SQLNET.ENCRYPTION_TYPES_CLIENT=(AES256,AES192,AES128)
SQLNET.ENCRYPTION_TYPES_SERVER=(AES256,AES192,AES128)
SQLNET.IGNORE_ANO_ENCRYPTION_FOR_TCPS=TRUE
SSL_CIPHER_SUITES=(SSL_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,SSL_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384,SSL_ECDHE_RSA_WITH_AES_128_GCM_SHA256,SSL_ECDHE_RSA_WITH_AES_256_GCM_SHA384)
SSL_CLIENT_AUTHENTICATION=FALSE
SSL_VERSION=1.2
```

##### Investigate Log for Errors (TFA)

As the `root` OS user on the first node of the on-premises environment, use Oracle Trace File Analyzer to analyze all of your logs across your cluster to identify recent database errors.

The Event Summary gives you a real-time report the database status.

```
[root@on-prem1]# tfactl events -component RDBMS -database [DBname] -last 7d

Output from host : on-prem1
------------------------------

Event Summary:
INFO    :0
ERROR   :0
WARNING :0

Event Timeline:
No Events Found

Output from host : on-prem2
------------------------------

Event Summary:
INFO    :0
ERROR   :0
WARNING :0

Event Timeline:
No Events Found
```

Note:

Review the result and investigate and any failures before moving forward. Refer to [Collecting and Analyzing Oracle Database Diagnostic Data](https://docs.oracle.com/en/engineered-systems/health-diagnostics/trace-file-analyzer/tfaug/quick-start-guide.html#GUID-A1DBE3D4-6501-47D3-854E-E9978F19F7BA) for more information.

### Instantiate the Standby Using Oracle DBaaS Tools

Prepare the on-premises environment and instantiate the standby database using the DBaaS Tools `prepareForStandby` and `configureStandby` work flows.

#### Task 1: Install dbcactl in the On-Premises Environment

Database Configuration Assistant Utility (`dbcactl`) is a standalone software package which is part of Oracle Database product suite. It is designed to assist in the database creation, configuration and lifecycle management of Oracle Database.

Follow instructions in My Oracle Support document [Database Configuration Assistant Utility (dbcactl) - Standalone Software Package (Doc ID 3099785.1)](https://support.oracle.com/rs?type=doc&id=3099785.1) to download the utility used during this process.

#### Task 2: Prepare the Cloud Environment for Instantiation of the Standby Database

The target `ORACLE_HOME` for the standby database must already exist on the standby system. Use the following steps to create the home if one does not already exist.

It is recommended that the home for the standby database be the same version, RU and include one-off patches. If the same RU is not available, a more recent RU of the same major version can be used.

Install an Oracle Home for the Standby Database

1. As the `oracle` OS user on the first node of the on-premises environment, use `opatch` to list the database release.
	```
	[oracle@on-prem1]$ $ORACLE_HOME/OPatch/opatch lspatches | grep 'Database Release Update'
	36912597;Database Release Update : 19.25.0.0.241015 (36912597)
	```
2. As the `root` OS user on the first node of the cloud environment, use `dbaascli` to list the available images matching the on-premises release.
	```
	[root@cloud-exadata1 ~]# dbaascli cswLib showImages | grep -A 1 '19.25'
	2.IMAGE_TAG=19.25.0.0.0
	  VERSION=19.25.0.0.0
	  DESCRIPTION=19c OCT 2024 DB Image
	```
3. As the `root` OS user on the first node of the cloud environment, use `dbaascli` to download the available image matching the on-premises release.
	```
	[root@cloud-exadata1 ~]# dbaascli cswlib download --version 19.25.0.0.0
	...
	dbaascli execution completed
	```
4. As the `root` OS user on the first node of the cloud environment, use `dbaascli` to create the target `ORACLE_HOME` matching the on-premises release.
	```
	[root@cloud-exadata ~]# dbaascli dbHome create --version 19.25.0.0.0
	-----------------
	Running Plugin_initialization job
	...
	---------- START OF PLUGIN RESULT ----------
	{"ORACLE_HOME_NAME":"OraHome4","ORACLE_HOME":"/u02/app/oracle/product/19.0.0.0/dbhome_3"}
	---------- END OF PLUGIN RESULT ----------
	dbaascli execution completed
	```

Note:

Take note of the `ORACLE_HOME_NAME`, you will need it for the migration.

The Oracle Home on the cloud system can also be created using the OCI User Interface.

If Necessary, Modify Instantiation Parallelism

The default settings for instantiation will use four (4) RMAN channels on each standby database instance for instantiation (for example, a 2-node standby cluster = 8 total channels). This default balances impact on the systems involved with speed of data file copy.

However, for very large databases where the system resource impact is not a concern, more channels can be configured to help the file copy complete faster.

This control is in a configuration file on the standby system which can be updated with `dbaascli`.

On the first standby node as root:

1. Confirm the current setting.
	```
	[root@cloud-exadata ~]# dbaascli dataguard showDGConfigAttributes |
	 grep restore_channels_count "restore_channels_count" : "4",
	```
2. Update to the desired PER NODE parallelism using dbaascli.
	```
	[root@cloud-exadata ~]# dbaascli dataguard updateDGConfigAttributes
	 --attributes restore_channels_count=6
	<...>
	The following Data Guard configuration attributes were updated successfully: 
	{
	  "dgConfigurationAttributes" : {
	    "restore_channels_count" : "6"
	  }
	}
	```
3. Verify the new setting.
	```
	[root@cloud-exadata ~]# dbaascli dataguard showDGConfigAttributes |
	 grep restore_channels_count "restore_channels_count" : "6",
	```

Note:

This change impacts all future instantiations, whether for Hybrid Data Guard or OCI standby database creation. It is recommended that you reset the value to the default after this instantiation completes.

#### Task 3: Instantiate the Standby Database

After the preparations are complete you can run the Oracle DBaaS Tools `prepareForStandby` and `configureStandby` work flows to instantiate the cloud standby database.

You will actually run two jobs using the Oracle DBaaS Tools:

- Run `dbcactl` operation `prepareForStandby` in the on-premises environment.
- Run `dbaascli` operation `configureStandby` in the cloud environment.

##### Configure ACFS

As the `root` OS user on the first node of the on-premises environment, create the ACFS mount point required to execute `prepareForStandby`.

```
[root@on-prem1]# $(grep ^crs_home /etc/oracle/olr.loc | cut -d=
 -f2)/bin/crsctl stat res -w "TYPE == ora.acfs.type" |grep NAME
NAME=ora.datac1.acfsvol01.acfs

[root@on-prem1]# $(grep ^crs_home /etc/oracle/olr.loc | cut -d= -f2)/bin/crsctl
 stat res ora.datac1.acfsvol01.acfs -f |grep ^MOUNTPOINT_PATH
MOUNTPOINT_PATH=/acfs01

Create a directory for the dbname (oradb1 for this example):

[root@on-prem1]# mkdir /acfs01/oradb1
[root@on-prem1]# chown oracle:oinstall /acfs01/oradb1
```

##### Run dbcactl Operation prepareForStandby in the On-Premises Environment

Now you are prepared to start the process. First, you will prepare the primary database to become part of a Data Guard configuration. Gather the following information which will be passed to the workflow.

1. As the `root` OS user on the first node of the cloud environment, collect the `standbyScanName` and `standbyScanPort` required to execute `dbcactl`.
	```
	[root@cloud-exadata1 ~]# $(grep ^crs_home /etc/oracle/olr.loc | cut
	 -d= -f2)/bin/srvctl config scan |grep 'SCAN name:' | awk '{print $3}'
	cloud-exadata-scan.clientnet.default.oraclevcn.com,
	[root@cloud-exadata1 ~]# dbaascli grid getDetails | grep scanListenerTCPPorts | cut
	 -d "[" -f2 | cut -d "]" -f1
	 1521
	```
	Make note of these pieces of information to be passed to the workflow.
2. As the `oracle` OS user on the first node of the on-premises environment, collect the primary database unique name required to execute `dbcactl`.
	```
	[oracle@on-prem1]$ echo "select DB_UNIQUE_NAME from v\$database;" |
	 sqlplus -SILENT "/ as sysdba"
	DB_UNIQUE_NAME
	------------------------------
	oradb1_onprem
	```
3. As the `oracle` OS user on the first node of the on-premises environment, set the environment variable `ORACLE_HOME` pointing to the on-premises database Oracle Home.
	```
	[oracle@on-prem1]$ srvctl config database -home
	oradb1     /u01/app/oracle/product/19.0.0.0/dbhome_1       19.0.0.0.0
	[oracle@on-prem1]$ export ORACLE_HOME=/u01/app/oracle/product/19.0.0.0/dbhome_1
	```
4. With that information gathered, run the `prepareForStandby` work flow with the appropriate replacements.
	As the `oracle` OS user on the first node of the on-premises environment, run `dbcsctl` operation `prepareForStandby` with corresponding arguments.
	```
	[oracle@on-prem1]$ 
	<dbcactl_folder>/dbcactl \ 
	-silent \
	-oui_internal \
	-configureDatabase \
	-prepareForStandby \
	-dgTNSNamesoraFilePath /acfs01/oradb1 \
	-sourceDB oradb1_onprem \
	-standbyDBUniqueName oradb1_cloud \
	-standbyScanName cloud-exadata-scan.clientnet.default.oraclevcn.com \
	-standbyScanPort 1521 \
	-standbyDBDomain clientnet.default.oraclevcn.com \
	-blobFileLocation /tmp 
	Loading DBCA...
	SYS_PASSWORD_PROMPT
	<ENTER_SYS_PASSWORD>
	Session ID of the current execution is: 53
	-----------------
	Running Create_dg_services job
	Completed Create_dg_services job
	25% complete
	-----------------
	Running Update_tnsnames_ora_file job
	Completed Update_tnsnames_ora_file job
	50% complete
	-----------------
	Running Update_ifile_entry job
	Completed Update_ifile_entry job
	75% complete
	-----------------
	Running Prepare_blob_file job
	Completed Prepare_blob_file job
	100% complete
	---------- PLUGIN NOTES ----------
	Successfully created blob file: /tmp/oradb1_2024-11-21_10-59-53AM_137640.tar
	---------- END OF PLUGIN NOTES ----------
	Look at the log file
	 "/u01/app/oracle/cfgtoollogs/dbca/oradb1_onprem/oradb1_onprem.log"
	 for further details.
	```
	The workflow creates a zip file with required files to instantiate the standby database. For example, `tnsnames.ora`, TDE wallet, and so on. This TAR file is listed in the output of the command and must be copied from the to a location on the standby system.
5. As the `oracle` OS user on the first node of the on-premises environment, copy the generated blob file to the first node of the cloud environment.
	```
	[oracle@on-prem1]$ scp /tmp/oradb1_2024-11-21_10-59-53AM_137640.tar
	 opc@cloud-exadata1:/tmp
	```

##### Run dbaascli Operation configureStandby in the Cloud Environment

1. First, gather some information that has to be passed to the `configureStandby` work flow.
	As the `oracle` OS user on the first node of the on-premises environment, collect the `primaryScanIPAddresses`, `primaryScanPort`, and `primaryServiceName` required to execute `dbaascli`.
	```
	[oracle@on-prem1]$ $(grep ^crs_home /etc/oracle/olr.loc |
	 cut -d= -f2)/bin/srvctl config scan |grep 'SCAN name:' | awk '{print $3}'
	maafra2vm01-oe6ab-scan.clientnet.maafradefault.oraclevcn.com
	[oracle@on-prem1]$ srvctl config scan_listener -scannumber 1 |grep Endpoints
	Endpoints: TCP:1521/TCPS:2484
	[oracle@on-prem1]$ lsnrctl status | grep oradb1_onprem | cut -d'"' -f 2
	oradb1_onprem.companyxyz.region.com
	```
2. As the `root` OS user on the first node of the cloud environment, run `dbaascli` operation `configureStandby` with corresponding arguments.
	```
	[root@cloud-exadata1]# 
	dbaascli dataguard configureStandby \
	--dbname oradb1 \
	--oracleHome /u02/app/oracle/product/19.0.0.0/dbhome_3 \
	--standbyDBUniqueName oradb1_cloud \
	--primaryScanIPAddresses companyxyz.region.com \
	--primaryScanPort 1521 \
	--primaryServiceName oradb1_onprem.companyxyz.region.com \
	--protectionMode MAX_PERFORMANCE \
	--transportType ASYNC \
	--activeDG true \
	--standbyScanIPAddresses cloud-exadata-scan.clientnet.default.oraclevcn.com \
	--standbyScanPort 1521 \
	--standbyBlobFromPrimary /tmp/oradb1_2024-11-21_10-59-53AM_137640.tar
	Enter PRIMARY_DB_SYS_PASSWORD:
	<ENTER_PRIMARY_DB_SYS_PASSWORD>
	Enter PRIMARY_DB_TDE_PASSWORD:
	<ENTER_PRIMARY_DB_SYS_PASSWORD>
	Enter AWR_ADMIN_PASSWORD:
	<ENTER_AWR_ADMIN_PASSWORD>
	Enter AWR_ADMIN_PASSWORD (reconfirmation):
	<ENTER_AWR_ADMIN_PASSWORD>
	Loading PILOT...
	Session ID of the current execution is: 10015
	Log file location:
	 /var/opt/oracle/log/oradb1/dataguard/configureStandby/pilot_2024-11-21_11-28-21-AM_270773
	-----------------
	Running Plugin_initialization job
	Enter PRIMARY_DB_SYS_PASSWORD
	*******************
	Enter PRIMARY_DB_TDE_PASSWORD
	******************
	Enter AWR_ADMIN_PASSWORD
	********************
	Completed Plugin_initialization job
	-----------------
	Running Validate_plugin_inputs job
	Completed Validate_plugin_inputs job
	-----------------
	Running Default_database_values_initialization job
	Completed Default_database_values_initialization job
	-----------------
	...
	-----------------
	Running Generate_dgconfig_details job
	Acquiring native write lock: global_dgsystem_details_generation
	Releasing native lock: global_dgsystem_details_generation
	Completed Generate_dgconfig_details job
	Releasing lock: oradb1
	Releasing lock: _u02_app_oracle_product_19.0.0.0_dbhome_3
	-----------------
	Running Cleanup job
	Completed Cleanup job
	dbaascli execution completed
	```
	Note:
	The Oracle MAA best practice is for the standby to be open read-only to enable Automatic Block Media Recovery; Use the flag `--activeDG                             true`
3. As the `root` OS user on the first node of the cloud environment, run the following commands to monitor the progress of the `dbaascli` operation `configureStandby`.
	```
	[root@cloud-exadata1]# export dbName=oradb1
	[root@cloud-exadata1]# export dbUniqueName=oradb1_cloud
	[root@cloud-exadata1]# tail -20f \`ls -t
	 /var/opt/oracle/log/$dbName/dataguard/configureStandby/pilot_* | head -1\`
	FINE: [2024-11-21 11:43:38.908 UTC][pool-334-thread-1][DBCAExecutor$DBCAExecutionProcessHandler.logOutput:96]
	 -----------------
	FINE: [2024-11-21 11:43:38.910 UTC][pool-334-thread-1][DBCAExecutor$DBCAExecutionProcessHandler.logOutput:96]
	 Running Open_pdbs job
	FINE: [2024-11-21 11:43:42.661 UTC][pool-334-thread-1][DBCAExecutor$DBCAExecutionProcessHandler.logOutput:96]
	 Completed Open_pdbs job
	FINE: [2024-11-21 11:43:42.668 UTC][pool-334-thread-1][DBCAExecutor$DBCAExecutionProcessHandler.logOutput:96]
	 90% complete
	FINE: [2024-11-21 11:43:42.692 UTC][pool-334-thread-1][DBCAExecutor$DBCAExecutionProcessHandler.logOutput:96]
	 -----------------
	FINE: [2024-11-21 11:43:42.697 UTC][pool-334-thread-1][DBCAExecutor$DBCAExecutionProcessHandler.logOutput:96]
	 Running Create_services job
	[root@cloud-exadata1]# tail -20f \`ls -t
	 /var/opt/oracle/log/$dbName/dataguard/configureStandby/$dbUniqueName/trace* | head -1\`
	[pool-3-thread-4] [ 2024-11-21 12:03:55.015 UTC ] [CRSCache.getAttributesFromCRS:155]
	  CRS: name: ora.oradb1_cloud.oradb1_oradb1p3.paas.oracle.com.svc, type 1, node: null
	[pool-3-thread-4] [ 2024-11-21 12:03:55.015 UTC ] [CRSCache.getAttributesFromCRS:156]
	  attrs: [GLOBAL]
	[pool-3-thread-4] [ 2024-11-21 12:03:55.016 UTC ] [CRSCache.getAttributesFromCRS:163]
	  CRS: [<GLOBAL:false>]
	[pool-3-thread-4] [ 2024-11-21 12:03:55.016 UTC ] [CRSNative.genericStartEntity:668]
	  [MAJOR EVENT] About to start resource:
	 Name: ora.oradb1_cloud.oradb1_oradb1p3.paas.oracle.com.svc, force:false node: null,
	 options: 0, filter null
	[pool-3-thread-4] [ 2024-11-21 12:03:55.016 UTC ] [CRSNative.genericStartEntity:678]
	  filter = null
	[pool-3-thread-4] [ 2024-11-21 12:03:55.016 UTC ] [CRSNative.genericStartEntity:679]
	  node name = null
	[root@cloud-exadata1]# tail -20f /u01/app/grid/diag/crs/\`hostname\`/crs/trace/alert.log 
	2024-11-21 12:13:59.362 [CRSD(398369)]
	 CRS-2772: Server 'maafra3vm02-qbi0z1' has been assigned to pool
	 'ora.oradb1_oradb1_oradb1p3_ro.paas.oracle.com'.
	2024-11-21 12:13:59.363 [CRSD(398369)]
	 CRS-2772: Server 'maafra3vm02-qbi0z2' has been assigned to pool
	 'ora.oradb1_oradb1_oradb1p3_ro.paas.oracle.com'.
	2024-11-21 12:14:00.420 [CRSD(398369)]
	 CRS-2772: Server 'maafra3vm02-qbi0z1' has been assigned to pool
	 'ora.oradb1_oradb1_oradb1p4.paas.oracle.com'.
	2024-11-21 12:14:00.421 [CRSD(398369)]
	 CRS-2772: Server 'maafra3vm02-qbi0z2' has been assigned to pool
	 'ora.oradb1_oradb1_oradb1p4.paas.oracle.com'.
	```

#### Task 4: Validate the Standby Database

1. As the `root` OS user on the first node of the cloud environment, check the Oracle database configuration.
	```
	[root@cloud-exadata1]# dbaascli database getDetails --dbname oradb1 |
	 egrep 'dbName|dbRole|dbType|patchVersion'
	  "dbName" : "oradb1",
	  "dbRole" : "PHYSICAL_STANDBY",
	  "dbType" : "RAC",
	  "patchVersion" : "19.25.0.0.0",
	      "pdbName" : "ORADB1P1",
	      "pdbName" : "ORADB1P2",
	      "pdbName" : "ORADB1P3",
	      "pdbName" : "ORADB1P4",
	      "pdbName" : "ORADB1P5",
	```
2. As the `root` OS user on the first node of the cloud environment, check the Oracle Data Guard Broker configuration.
	```
	[root@cloud-exadata1]# dbaascli dataguard getDetails --dbName oradb1 |
	 egrep 'protectionMode|"status"|dbUniqueName|dgRole|standbyType|transportType|"switchoverReadiness"|"failoverReadiness"|redoTransportState|databaseStatus'
	  "protectionMode" : "MAX_PERFORMANCE",
	  "status" : "SUCCESS",
	      "dbUniqueName" : "oradb1_onprem",
	      "dgRole" : "PRIMARY",
	      "standbyType" : null,
	      "transportType" : "ASYNC",
	      "switchoverReadiness" : "HEALTHY",
	      "failoverReadiness" : "HEALTHY",
	      "redoTransportState" : "ON",
	      "databaseStatus" : "SUCCESS",
	      "dbUniqueName" : "oradb1_cloud",
	      "dgRole" : "STANDBY",
	      "standbyType" : "PHYSICAL_STANDBY",
	      "transportType" : "ASYNC",
	      "switchoverReadiness" : "HEALTHY",
	      "failoverReadiness" : "HEALTHY",
	      "redoTransportState" : null,
	      "databaseStatus" : "SUCCESS",
	```
	'status' should be SUCCESS. If any other status is shown, re-run the command after waiting 2 minutes to give the Broker time to update. If issues persist, see the Oracle Data Guard Broker documentation to diagnose and correct any issues.
3. As the `oracle` OS user on the first node of the cloud environment, validate the standby database.
	```
	[oracle@cloud-exadata1]$ dgmgrl / 'validate database oradb1_cloud'
	DGMGRL for Linux: Release 19.0.0.0.0 - Production on Thu Nov 21 15:26:55 2024
	Version 19.25.0.0.0
	Copyright (c) 1982, 2019, Oracle and/or its affiliates.  All rights reserved.
	Welcome to DGMGRL, type "help" for information.
	Connected to "oradb1_cloud"
	Connected as SYSDG.
	  Database Role:     Physical standby database
	  Primary Database:  oradb1_onprem
	  Ready for Switchover:  Yes
	  Ready for Failover:    Yes (Primary Running)
	  Managed by Clusterware:
	    oradb1_onprem  :  YES            
	    oradb1_cloud:  YES
	```

#### Task 5: Offline Encrypt the Cloud Standby Database

If the primary database was encrypted with TDE before instantiation, skip this task.

If the primary database was not encrypted with TDE prior to instantiation, the standby in Oracle Cloud must be encrypted using fast offline encryption.

See [KB127996 Implementing Transparent Data Encryption (TDE) Using Standby-First Offline Encryption](https://support.oracle.com/support/?documentId=KB127996) to complete the encryption for the standby database only. That is, do not perform a switchover and encrypt the on-premises database. The on-premises database will remain unencrypted.

For complete details about mixed encryption Data Guard configurations see [KB18578 Oracle Database Tablespace Encryption Behavior in Oracle Cloud](https://support.oracle.com/support/?documentId=KB18578).

#### Task 6: Implement Recommended MAA Best Practices

After standby instantiation, evaluate implementing the following Oracle MAA best practices to achieve better data protection and availability.

While many of the recommended best practices are implemented as part of the workflows, some additional recommendations are not implemented as they may have a performance impact.

The additional key best practices are listed below. Also see [Oracle Data Guard Configuration Best Practices](configure-and-deploy-oracle-data-guard.md) for details about Oracle MAA recommended best practices for Oracle Data Guard.

Set Data Protection Parameters

MAA best practice recommendations include the following settings on the primary and standby databases.

`db_block_checksum=TYPICAL`

`db_lost_write_protect=TYPICAL`

`db_block_checking=MEDIUM`

```
SQL> show parameter db_block_checksum

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_block_checksum                    string      TYPICAL

SQL> alter system set db_block_checksum=TYPICAL scope=both sid='*';

SQL> show parameter db_lost_write_protect

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_lost_write_protect                string      typical

SQL> alter system set db_lost_write_protect=TYPICAL scope=both sid='*';

SQL> show parameter db_block_checking

NAME                                 TYPE        VALUE
------------------------------------ ----------- ------------------------------
db_block_checking                    string      OFF

SQL> alter system set db_block_checking=MEDIUM scope=both sid='*';
```

Note that the `db_block_checking` setting has an impact on primary database performance and should be thoroughly tested with a production workload in a lower, production-like environment.

If the performance impact is determined to be unacceptable on the primary database, the standby database should set `db_block_checking=MEDIUM` with the primary set to `NONE` and set the `cloudautomation` Data Guard Broker property to '1' for both databases so that the value will be automatically changed accordingly after a role transition swapping values of the primary and standby databases.

```
DGMGRL> edit database primary-unique-name set property cloudautomation=1;
Property "cloudautomation" updated

DGMGRL> edit database standby-unique-name set property cloudautomation=1;
Property "cloudautomation" updated
```

Note that the `cloudautomation` property must be set on both databases to work properly.

Configure Backups

Optionally, configure automatic backups for the Oracle cloud database, for primary or standby role, using Autonomous Recovery Service or object storage.

Autonomous Recovery Service allows you to offload backup processing and storage in addition to the following benefits:

- Significantly reduce dependencies on backup infrastructure
- Develop a centralized backup management strategy for all the supported OCI database services
- Retain backups with Recovery Service for a maximum period of 95 days
- Leverage real-time data protection capabilities to eliminate data loss
- Significantly reduce backup processing overhead for your production databases
- Implement a dedicated network for Recovery Service operations in each virtual cloud network (VCN)
- Automate backup validation to ensure recoverability
- Implement a policy-driven backup life-cycle management

See [Manage Database Backup and Recovery on Oracle Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/iaas/exadatacloud/exacs/ecs-managing-db-backup-and-recovery.html#ECSCM-GUID-07D1B1D6-4A06-4859-B7DF-4C3A681A6B40) and [Database Autonomous Recovery Service](https://docs.public.oneportal.content.oci.oraclecloud.com/iaas/recovery-service/doc/overview-recovery-service.html) for more information.

### Data Guard Life Cycle Operations

When the configuration is complete, Data Guard life-cycle operations, failover, switchover, and reinstate can be performed by `dbaascli` commands. See the [OCI Documentation](https://docs.oracle.com/en/cloud/paas/database-dbaas-cloud/csdbi/dbaascli.html) for details.

### Health Check and Monitoring

After instantiating the standby database, a health check should be performed to ensure that the Oracle Data Guard databases (primary and standby) are compliant with Oracle MAA best practices.

It is also recommended that you perform the health check monthly, and before and after database maintenance. Oracle Autonomous Health Framework and automated tools including an Oracle MAA Scorecard using OraChk or ExaChk are recommended for checking the health of a Data Guard configuration. See [Oracle Autonomous Health Framework User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/engineered-systems/health-diagnostics/autonomous-health-framework&id=AHFUG-GUID-A1DBE3D4-6501-47D3-854E-E9978F19F7BA) and [Oracle ORAchk and Oracle EXAchk documentation](https://docs.oracle.com/en/engineered-systems/health-diagnostics/exachk/index.html).

Regular monitoring of the Oracle Data Guard configuration is not provided in a hybrid Data Guard configuration and must be done manually. See [Monitor an Oracle Data Guard Configuration](monitor-oracle-data-guard-configuration.md) for more information.