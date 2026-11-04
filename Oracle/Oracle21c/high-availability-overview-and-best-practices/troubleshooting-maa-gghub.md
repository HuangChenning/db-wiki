---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/troubleshooting-maa-gghub.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Troubleshooting MAA GoldenGate Hub

### Oracle GoldenGate Extract Failure or Error Conditions Considerations

For Oracle GoldenGate Extract processes using Oracle Data Guard configurations that are using redo transport Maximum Performance or Maximum Availability modes, the following parameter must be added to the Extract process parameter file on the primary database system to avoid losing transactions and resulting in logical data inconsistencies:

```
TRANLOGOPTIONS HANDLEDLFAILOVER
```

This parameter prevents Extract from extracting transaction data from redo that has not yet been applied to the Data Guard standby database. This is crucial to preventing Oracle GoldenGate from replicating data to a target database that does not exist in the source standby database.

If this parameter is not specified, after a data loss failover of the source database it is possible to have data in the target database that is not present in the source database, leading to logical data inconsistencies.

By default, after 60 seconds, a warning message is written to the Extract report file when the Extract is stalled because it can't query the standby database applied SCN information. For example:

`WARNING OGG-02721 Extract has been waiting for the standby database for 60                 seconds.`

The amount of time before the warning message is written to the Extract report file can be adjusted using the Extract parameter `TRANLOGOPTIONS HANDLEDLFAILOVER                 STANDBY_WARNING`.

If the Extract is still unable to query the standby database applied SCN information after 30 minutes (default), the Extract process abend, logging the following message in the Extract report file:

`ERROR OGG-02722 Extract abended waiting for 1,800 seconds for the standby                 database to be accessible or caught up with the primary database.`

If the standby database becomes available before the default 30 timeout expires, Extract continues mining data from the source database and reports the following message to the report file:

`INFO OGG-02723 Extract resumed from stalled state and started processing                 LCRs.`

The timeout value of 30 minutes can be adjusted using the Extract parameter `TRANLOGOPTIONS HANDLEDLFAILOVER STANDBY_ABEND <value>`, where value is the number of seconds the standby is unavailable before abending.

If the standby database will be unavailable for a prolonged duration, such as during a planned maintenance outage, and you wish Extract to continue extracting data from the primary database, remove the `TRANLOGOPTIONS HANDLEDLFAILOVER` parameter from the Extract parameter file and restart Extract. Remember to set the parameter after the standby becomes available.

Note:

If extracting from a primary database continues while the standby is unavailable, a data loss failover could result after the standby becomes available, and not all the primary redo was applied before a failover. The GoldenGate target database will contain data that does not exist in the source database.

If the Extract process has been assigned an auto restart profile, as documented in [Cloud: Oracle GoldenGate Microservices Architecture on Oracle Exadata Database Service Configuration Best Practices](ogg-microservices-cloud1.md), after a Data Guard role transition, the Extract process automatically restarts. Extract continues to mine redo data from the new primary database, ignoring the current state of the new standby database, until a default 5 minute timeout period expires. After this time, if the standby is not available Extract will abend with the following errors:

`INFO    OGG-25053  Timeout waiting for 300 seconds for standby database                 reinstatement. Now enforcing HANDLEDLFAILOVER.`

`ERROR   OGG-06219  Unable to extract data from the Logmining server                 OGG$CAP_XXXXX.`

`ERROR   OGG-02078  Extract encountered a fatal error in a processing thread and                 is abending.`

Extract continues attempting to automatically restart, based on the Oracle GoldenGate Microservices auto restart profile, and fails because it reaches the `HANDLEDLFAILOVER` timeout, until the number of retries is reached or the new standby database becomes available.

During the timeout period following a database role transition, the `HANDLEDLFAILOVER` parameter is automatically suspended, so data is replicated to the Oracle GoldenGate replica database without consideration of the source standby database not being kept up to date. The timeout period for the standby database to start up before Extract abends can be adjusted using the Extract parameter `TRANLOGOPTIONS DLFAILOVER_TIMEOUT`.

It is recommended that you leave `DLFAILOVER_TIMEOUT` at the default of 5 minutes to allow the old primary to convert to a standby. If the new standby database will be unavailable for an extended period of time or completely gone, then to ensure that Extract starts and remains running, you must remove the `HANDLEDLFAILOVER` parameter from the Extract parameter file. After removing the parameter, Extract no longer waits until redo has been applied to the standby database before extracting the data.

During the time it takes for the standby database to come back online and apply all of the redo from the primary database, there is data divergence between it and the Oracle GoldenGate replica database. This divergence is resolved when the standby database is up to date. At this point you can add the `HANDLEDLFAILOVER` parameter back into the integrated Extract process parameter file, and then stop and restart the Extract.

When Oracle Data Guard Fast Start Failover is disabled, such that the broker can automatically fail over to a standby database in the event of loss of the primary database, you must specify an additional integrated Extract parameter:

```
TRANLOGOPTIONS FAILOVERTARGETDESTID n
```

This parameter identifies which standby database the Oracle GoldenGate Extract process must remain behind, with regards to not extracting redo data that has not yet been applied to the standby database.

If Oracle Data Guard Fast Start Failover is disabled, and you don’t specify the additional integrated Extract parameter `FAILOVERTARGETDESTID`, the extract will abend with the following errors:

`ERROR OGG-06219 Unable to extract data from the Logmining server                 OGG$CAP_XXXXX.`

`ERROR OGG-02078 Extract encountered a fatal error in a processing thread and is                 abending.`

### Troubleshooting ACFS Replication

The health of ACFS replication is determined by the `acfsutil repl util                 verifyprimary/verifystandby` commands. These commands are called by the example CRS action scripts acfs\_primary.scr and acfs\_standby.scr, but they are also implicitly called during a file system role transition.

Both commands will return a value of ‘0’ if there are no problems detected. If a non-zero value is returned, run the same command with verbose flag to see comprehensive output of the verification tests.

As the grid user on the standby GGHub system, verify the ACFS replication with the primary GGHub:

```
[grid@gghub_stby1]$ acfsutil repl util verifyprimary /mnt/acfs_gg -v

- Attempting to ping clust1-vip1
- ping successful
- Attempting to ssh
  '/usr/bin/ssh -o BatchMode=true -o Ciphers=aes128-ctr -o ConnectTimeout=3   -x oracle@clust1-vip1 true 2>&1'
- ssh output: Host key verification failed.
- ssh output: Host key verification failed.
- ssh attempt failed, ret=255
verifyprimary return code: 255
```

The errors reported by the verify command, `Host key verification failed`, clearly showing why it failed. In this example, there is a problem with the ssh configuration between the standby and the primary file system GGHubs. Once the problem has been resolved, rerun the verify commands to ensure there are no further problems.

After a failover has completed, it is recommended to check the acfsutil trace files for the reason behind the failover. The acfsutil trace files are located in the CRS trace file directory, which defaults to ``/u01/app/grid/diag/crs/`hostname`/crs/trace/crsd_scriptagent_grid.trc``.

Below are some common failures that can occur with incorrect ACFS replication configuration.

SSH daemon is shutdown or not configured to run on the VIP

When using an application VIP on the ACFS primary and standby GGHubs, the ssh daemon must be configured to listen for incoming connections on the VIP address. If this configuration is not done, or the ssh daemon is not running on either of the current primary/standby hosts the verifyprimary or verifystandby commands will fail with the following error.

As the grid user on the primary GGHub system, verify the ACFS recplication with the standby GGHub:

```
[grid@gghub_prim1]$ acfsutil repl util verifystandby /mnt/acfs_gg -v

- Attempting to ping gghubstby.goldengate.com
- ping successful
- Attempting to ssh
  '/usr/bin/ssh -o BatchMode=true   -o Ciphers=aes128-ctr -o ConnectTimeout=3   -x oracle@gghub_stby-avip true 2>&1'

- ssh output: ssh: connect to host gghub_stby1 port 22: Connection refused
- ssh output: ssh: connect to host gghub_stby2 port 22: Connection refused

- ssh attempt failed, ret=255
verifystandby return code: 255
```

As the grid user on the standby GGHub system, check that the resource application VIP and sshd\_restart are running and restart them if not:

```
[grid@gghub_stby1 ~]$ crsctl stat res -w "TYPE co app.appviptypex2"

NAME=gghubstby
TYPE=app.appviptypex2.type
TARGET=OFFLINE
STATE=OFFLINE

[grid@gghub_stby1 ~]$ crsctl start res gghubstby

CRS-2672: Attempting to start 'gghubstby' on 'gghub_stby1'
CRS-2676: Start of 'gghubstby' on 'gghub_stby1' succeeded
CRS-2672: Attempting to start 'sshd_restart' on 'gghub_stby1'
CRS-2676: Start of 'sshd_restart' on 'gghub_stby1' succeeded
```

Check that `acfsutil repl verifystandby/verifyprimary` returns a result of ‘0’ from both the primary and standby host.

Primary ACFS background resources are not running

1. The primary or standby ACFS servers are not accessible
2. ACFS Replication ssh user problem
3. SSH Host key verification failed

### Troubleshooting Oracle GoldenGate

There may be occasions when GoldenGate processes are not successfully started on an Oracle RAC node. There are number of files generated by GoldenGate, XAG, and CRS that should be reviewed to determine the cause of the problem.

Below is a list of important log and trace files, along with their example locations and some example output.

XAG log file

Location: \<XAG installation directory>/log/\<hostname>

Example location: /u01/app/grid/xag/log/\`hostname\`

File name: agctl\_goldengate\_grid.trc

Contains all commands executed with agctl along with the output from the commands, including those that CRS executes.

```
2022-04-18 11:52:21: stop resource success
2022-04-18 11:52:38: agctl start goldengate <instance_name>
2022-04-18 11:52:38: executing cmd: /u01/app/19.0.0.0/grid/bin/crsctl status res xag.<INSTANCE_NAME>.goldengate
2022-04-18 11:52:38: executing cmd: /u01/app/19.0.0.0/grid/bin/crsctl status res xag.<INSTANCE_NAME>.goldengate -f
2022-04-18 11:52:38: executing cmd: /u01/app/19.0.0.0/grid/bin/crsctl start resource xag.<INSTANCE_NAME>.goldengate -f
2022-04-18 11:52:45: Command output:
>  CRS-2672: Attempting to start 'xag.<INSTANCE_NAME>.goldengate' on 'exadb-node1'
>  CRS-2676: Start of 'xag.<INSTANCE_NAME>.goldengate' on 'exadb-node1' succeeded
>End Command output
2022-04-18 11:52:45: start resource success
```

XAG GoldenGate instance trace file

Location: \<XAG installation directory>/log/\<hostname>

Example location: /u01/app/grid/xag/log/\`hostname\`

File name: <GoldenGate\_instance\_name>\_agent\_goldengate.trc

It contains the output from the commands executed by agctl, the environment variables used, and any debug output enabled for the underlying commands.

```
2022-04-18 12:14:46: Exported ORACLE_SID ggdg1
2022-04-18 12:14:46: Exported GGS_HOME /u01/oracle/goldengate/gg21c_MS
2022-04-18 12:14:46: Exported OGG_CONF_HOME /mnt/dbfs/goldengate/deployments/ggsm01/etc/conf
2022-04-18 12:14:46: Exported LD_LIBRARY_PATH 
/u01/oracle/goldengate/gg21c_MS:/u01/app/19.0.0.0/grid/lib:/etc/ORCLcluster/lib
2022-04-18 12:14:46: Exported LD_LIBRARY_PATH_64 /u01/oracle/goldengate/gg21c_MS
2022-04-18 12:14:46: Exported LIBPATH /u01/oracle/goldengate/gg21c_MS
2022-04-18 12:14:46: ogg input = {"oggHome":"/u01/oracle/goldengate/gg21c_MS","serviceManager":{"oggConfHome":"/mnt/dbfs/goldengate/deployments/ggsm01/etc/conf","portNumber":9100},"username":"<username>","credential":"*****"}
2022-04-18 12:14:46: About to exec /u01/oracle/goldengate/gg21c_MS/bin/XAGTask HealthCheck
2022-04-18 12:14:47: XAGTask retcode = 0
```

CRS trace file

Location: /u01/app/grid/diag/crs/\<hostname>/crs/trace

Example location: /u01/app/grid/diag/crs/\`hostname\`/crs/trace

File name: crsd\_scriptagent\_oracle.trc

Contains the output created by any CRS resource action scripts, like XAG or dbfs\_mount. This trace file is crucial to determining why DBFS or GoldenGate did not start on a RAC node.

```
2022-04-18 11:52:38.634 :    AGFW:549631744: {1:30281:59063} Agent received the message: RESOURCE_START[xag.<INSTANCE_NAME>.goldengate 1 1] ID 4098:4125749
2022-04-18 11:52:38.634 :    AGFW:549631744: {1:30281:59063} Preparing START command for: xag.<INSTANCE_NAME>.goldengate 1 1
2022-04-18 11:52:38.634 :    AGFW:549631744: {1:30281:59063} xag.<INSTANCE_NAME>.goldengate 1 1 state changed from: OFFLINE to: STARTING
2022-04-18 11:52:38.634 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] Executing action script: /u01/oracle/XAG_MA/bin/aggoldengatescaas[start]
2022-04-18 11:52:38.786 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] GG agent running command 'start' on xag.<INSTANCE_NAME>.goldengate
2022-04-18 11:52:42.140 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] ServiceManager fork pid = 265747
2022-04-18 11:52:42.140 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] Waiting for /mnt/dbfs/goldengate/deployments/ggsm01/var/run/ServiceManager.pid
2022-04-18 11:52:42.140 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] Waiting for SM to start
2022-04-18 11:52:42.140 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] ServiceManager PID = 265749
2022-04-18 11:52:43.643 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] XAGTask retcode = 0
2022-04-18 11:52:43.643 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [start] XAG HealthCheck after start returned 0
2022-04-18 11:52:43.643 :    AGFW:558036736: {1:30281:59063} Command: start for resource: xag.<INSTANCE_NAME>.goldengate 1 1 completed with status: SUCCESS
2022-04-18 11:52:43.643 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [check] Executing action script: /u01/oracle/XAG_MA/bin/aggoldengatescaas[check]
2022-04-18 11:52:43.644 :    AGFW:549631744: {1:30281:59063} Agent sending reply for: RESOURCE_START[xag.<INSTANCE_NAME>.goldengate 1 1] ID 4098:4125749
2022-04-18 11:52:43.795 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [check] GG agent running command 'check' on xag.<INSTANCE_NAME>.goldengate
2022-04-18 11:52:45.548 :CLSDYNAM:558036736: [xag.<INSTANCE_NAME>.goldengate]{1:30281:59063} [check] XAGTask retcode = 0
2022-04-18 11:52:45.548 :    AGFW:549631744: {1:30281:59063} xag.<INSTANCE_NAME>.goldengate 1 1 state changed from: STARTING to: ONLINE
```

GoldenGate deployment log files

Location: <Goldengate\_deployment\_directory>/<instance\_name>/var/log

Example location: /mnt/dbfs/goldengate/deployments/<instance\_name>/var/log

File names: adminsrvr.log, recvsrvr.log, pmsrvr.log, distsrvr.log

Contains the output of start, stop, and status checks of the Oracle GoldenGate deployment processes (Administration Server, Distribution Server, Receiver Server, and Performance Metrics Server).

```
2022-04-18T11:52:42.645-0400 INFO | Setting deploymentName to '<instance_name>'. (main)
2022-04-18T11:52:42.665-0400 INFO | Read SharedContext from store for length 19 of file '/mnt/dbfs/goldengate/deployments/<instance_name>/var/lib/conf/adminsrvr-resources.dat'. (main)
2022-04-18T11:52:42.723-0400 INFO | XAG Integration enabled (main)
2022-04-18T11:52:42.723-0400 INFO | Configuring security. (main)
2022-04-18T11:52:42.723-0400 INFO | Configuring user authorization secure store path as '/mnt/dbfs/goldengate/deployments/<instance_name>/var/lib/credential/secureStore/'. (main)
2022-04-18T11:52:42.731-0400 INFO | Configuring user authorization as ENABLED. (main)
2022-04-18T11:52:42.749-0400 INFO | Set network configuration. (main)
2022-04-18T11:52:42.749-0400 INFO | Asynchronous operations are enabled with default synchronous wait time of 30 seconds (main)
2022-04-18T11:52:42.749-0400 INFO | HttpServer configuration complete. (main)
2022-04-18T11:52:42.805-0400 INFO | SIGHUP handler installed. (main)
2022-04-18T11:52:42.813-0400 INFO | SIGINT handler installed. (main)
2022-04-18T11:52:42.815-0400 INFO | SIGTERM handler installed. (main)
2022-04-18T11:52:42.817-0400 WARN | Security is configured as 'disabled'. (main)
2022-04-18T11:52:42.818-0400 INFO | Starting service listener... (main)
2022-04-18T11:52:42.819-0400 INFO | Mapped 'ALL' interface to address 'ANY:9101' with default IPV4/IPV6 options identified by 'exadb-node1.domain'. (main)
2022-04-18T11:52:42.821-0400 INFO | Captured 1 interface host names: 'exadb-node1.domain' (main)
2022-04-18T11:52:42.824-0400 INFO | The Network ipACL specification is empty. Accepting ANY address on ALL interfaces. (main)
2022-04-18T11:52:42.826-0400 INFO | Server started at 2022-04-18T11:52:42.827-05:00 (2022-04-18T15:52:42.827Z GMT) (main)
```

GoldenGate report files

Location: <Goldengate\_deployment\_directory>/<instance\_name>/var/lib/report

Example location: /mnt/dbfs/goldengate/deployments/<instance\_name>/var/lib/report

The GoldenGate report files contain important information, warning messages, and errors for all GoldenGate processes, including the Manager processes. If any of the GoldenGate processes fail to start or abend when running, the process report file will contain important information that can be used to determine the cause of the failure.

```
2022-04-23 13:01:50  ERROR   OGG-00446  Unable to lock file " /mnt/acfs_gg/deployments/<instance_name>/var/lib/checkpt/EXT_1A.cpe" (error 95, Operation not supported).
2022-04-23 13:01:50  ERROR   OGG-01668  PROCESS ABENDING.
```

### Troubleshooting GGHub Deployment Using Ansible

Check the Primary and Standby GGHub Clusterware Resources Status

Ansible automation creates the GGHub clusterware resources with names that include the GGHub deployment name, primary GGHub group name, and standby GGHub group name provided in the inventory file.

In this example, the GGHub deployment name is `maahub`, the primary GGHub group name is `maahuba,` and the standby GGHub group name is `maahubb`.

The following table explains the GGHub clusterware resources using example names.

| Example GGHub clusterware resource name | Purpose |
| --- | --- |
| `acfs_primary` | ACFS clusterware resource that exists on both primary and standby GGHub clusters, but state is ONLINE only on the primary GGHub cluster with primary ACFS file system.  The `acfs_primary` clusterware resource is used to automatically determine if Oracle GoldenGate can start processes on the primary GGHub. |
| `acfs_standby` | ACFS clusterware resource that exists on both primary and standby GGHub clusters.  The `acfs_standby` clusterware resource checks that the local file system is a standby file system and verifies the remote primary file system status. |
| `maahuba-app-vip1` | APP VIP resource for the primary GGHub cluster using the primary GGHub group name. |
| `maahubb-app-vip1` | APP VIP resource for the standby GGHub cluster using the standby GGHub group name. |
| `nginx` | NGINX clusterware resource.  Resource exists on both primary and standby GGHub clusters. |
| `ora.data.maahub.acfs` | ACFS clusterware resource that exists on both primary and standby GGHub clusters, and is named using the format `ora.diskgroup_name.volume_name.acfs`.  The `ora.data.maahub.acfs` clusterware resource ensures that the ACFS file system is available before starting GoldenGate Microservices. |
| `ora.repl.dupd.data.maahub.acfs` | ACFS replication clusterware resource using the GGHub deployment name.  Resource starts on the primary GGHub cluster which is the source of ACFS replication. After role reversal this resource starts on the new primary GGHub cluster. |
| `xag.maahub.goldengate` | XAG clusterware resource.  Resource exists on both primary and standby GGHub clusters, but state is ONLINE only on the primary GGHub cluster. |

Primary GGHub Clusterware resources status

Validate the primary GGHub clusterware resources on the first node of the primary GGHub cluster using the `crsctl` utility as the clusterware software owner OS user `grid`.

The deployment name used in this example is `maahub` and the primary group name is `maahuba`.

```
$ crsctl status res acfs_primary acfs_standby nginx
 <primary_group>-app-vip1 xag.<gg_deployment_name>.goldengate
 ora.data.<gg_deployment_name>.acfs ora.repl.dupd.data.<gg_deployment_name>.acfs -t
OR
$ crsctl status res acfs_primary acfs_standby nginx maahuba-app-vip1 xag.maahub.goldengate
 ora.data.maahub.acfs ora.repl.dupd.data.maahub.acfs -t
```

Example output

```
--------------------------------------------------------------------------------
Name           Target  State        Server                   State details
--------------------------------------------------------------------------------
Cluster Resources
--------------------------------------------------------------------------------
acfs_primary
      1        ONLINE  ONLINE       maahuba1                 STABLE
acfs_standby
      1        ONLINE  ONLINE       maahuba1                 STABLE
maahuba-app-vip1
      1        ONLINE  ONLINE       maahuba1                 STABLE
nginx
      1        ONLINE  ONLINE       maahuba1                 STABLE
ora.data.maahub.acfs
      1        ONLINE  ONLINE       maahuba1                 mounted on /opt/oracle/gghub/maahub,STABLE
ora.repl.dupd.data.maahub.acfs
      1        ONLINE  ONLINE       maahuba1                 STABLE
xag.maahub.goldengate
      1        ONLINE  ONLINE       maahuba1                 STABLE
```

Standby GGHub Clusterware resources status

Validate the standby GGHub clusterware resources status on the first node of the standby GGHub cluster.

The standby group name in this example is `maahubb`.

Notice that the `acfs_primary` resource state is OFFLINE on the standby cluster as expected.

```
$ crsctl status res acfs_primary acfs_standby ora.data.maahub.acfs
 maahubb-app-vip1 maahubb-app-vip1 xag.maahub.goldengate nginx -t
```

Example output

expected.

```
--------------------------------------------------------------------------------
Name           Target  State        Server                   State details
--------------------------------------------------------------------------------
Cluster Resources
--------------------------------------------------------------------------------
acfs_primary
      1        OFFLINE OFFLINE                               STABLE
acfs_standby
      1        ONLINE  ONLINE       maahubb1                 STABLE
maahubb-app-vip1
      1        ONLINE  ONLINE       maahubb1                 STABLE
nginx
      1        OFFLINE  OFFLINE     maahubb1                 STABLE
ora.data.maahub.acfs
      1        ONLINE  ONLINE       maahubb1                 mounted on /opt/oracle/gghub/maahub,STABLE
xag.maahub.goldengate
      1        ONLINE  OFFLINE                               STABLE
```

Check the GGHub ACFS Mount Replication Status

Check the ACFS replication initialization status

As the `grid` OS user on the primary and standby GGHub nodes, monitor the initialization progress. When the status changes to “Send Completed” it means the initial primary file system copy has finished, and the primary file system is now being replicated to the standby host, as shown here.

```
# On the Primary GGHub

[grid@gghub_prim1 ~]$ /sbin/acfsutil repl info -c -v /opt/oracle/gghub/maahub | grep Status

Status:                              Send Completed

# On the Standby GGHub

[grid@gghub_prim1 ~]$ /sbin/acfsutil repl info -c -v /opt/oracle/gghub/maahub | grep Status

Status:                              Receive Completed OR Receiving incremental differences
```

Verify the ACFS replicated file system

As the `grid` OS user on the primary and standby GGHub nodes, verify and monitor the ACFS replicated file system.

```
# On the Primary GGHub

[grid@gghub_prim1 ~]$ acfsutil repl util verifystandby /opt/oracle/gghub/maahub

verifystandby returned: 0

# On the Standby GGHub

[grid@gghubtest31 ~]$ acfsutil repl util verifyprimary /opt/oracle/gghub/maahub

verifyprimary returned: 0
```

Note:

Both commands return a value of 0 (zero) if there are no problems detected. If a non-zero value is returned, refer to Troubleshooting ACFS Replication for information about monitoring, diagnosing, and resolving common issues with ACFS Replication before continuing.

Check the ACFS replication status

For a healthy ACFS replication the primary GGHub ACFS replication status should be `Running` and retries made number should be 0 on the primary GGHub cluster.

Use the following command to check the ACFS replication information on the primary GGHub cluster.

```
$ /usr/sbin/acfsutil repl info -v -c /opt/oracle/gghub/maahub
```

Example output

```
Site:                                Primary
Primary hostname:                    maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com
Primary path:                        /opt/oracle/gghub/maahub
Primary status:                      Running
Background Resources:                Active

Standby connect string:              grid@maahubb-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com
Standby path:                        /opt/oracle/gghub/maahub
Replication interval:                0 days, 0 hours, 0 minutes, 0 seconds
Sending primary as of:               Fri Jul 18 21:10:39 2025
Status:                              Sending incremental differences
Lag Time:                            00:00:37 (Constant mode)
Retries made:                        0
Standby Backup Snapshot:             Up to Date
Last send started at:                Fri Jul 18 21:10:39 2025
Last send completed at:              In progress
Next send starts at:                 On send completion
Replicated tags:
Data transfer compression:           Off
ssh strict host key checking:        On
Debug log level:                     3
Replication ID:                      0xa1012b70
```
Standby GGHub ACFS replication status

Use the following command to check the ACFS replication information on the standby GGHub cluster.

The status should not have any errors and elapsed time for last receive should not be higher than few seconds.

```
$ /usr/sbin/acfsutil repl info -v -c /opt/oracle/gghub/maahub
```

Example output

```
Site:                                Standby
Primary hostname:                    maahuba-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com
Primary path:                        /opt/oracle/gghub/maahub

Standby connect string:              grid@maahubb-app-vip1.clientsubnet.vcnfraans1.oraclevcn.com
Standby path:                        /opt/oracle/gghub/maahub
Replication interval:                0 days, 0 hours, 0 minutes, 0 seconds
Last sync time with primary:         Fri Jul 18 21:11:44 2025
Receiving primary as of:             Fri Jul 18 21:11:44 2025
Status:                              Receive Completed
Standby Backup Snapshot:             Up to Date
Last receive started at:             Fri Jul 18 21:11:44 2025
Last receive completed at:           Fri Jul 18 21:11:50 2025
Elapsed time for last receive:       0 days, 0 hours, 0 minutes, 6 seconds
Data transfer compression:           Off
ssh strict host key checking:        On
Debug log level:                     3
Replication ID:                      0xa1012b70
```

Removal of GGHub Clusterware Resources and GoldenGate Replication Processes

To remove the GGHub configuration from both the primary and standby GGHub clusters including the ACFS mount point and GoldenGate Extract and Replicat processes execute the Ansible playbook oracle.gghub.remove.

Playbook `oracle.gghub.remove` asks for confirmation before proceeding with the removal steps.

Note:

Use the `oracle.gghub.remove` playbook with caution, because it removes all of the GoldenGate Extract and Replicat processes managed by GGHub, along with GGHub clusterware resources and ACFS mounts from both primary and standby GGHub clusters.

Playbook `oracle.gghub.remove` prompts for the Ansible vault password. Use the GoldenGate admin password from the vault for removal.

Execute the `oracle.gghub.remove` playbook as follows to remove the GGHub deployment and GoldenGate replication processes.

```
(gghub) [~]$ ansible-playbook oracle.gghub.remove
 -i /u01/maagghub/inventory/maahub.yml -e @/u01/maagghub/inventory/maahub.key
 --ask-vault-pass
```

GGHub ACFS Replication Resync Using Ansible

GGHub ACFS replication resync can be performed using MAA Ansible collection playbook `oracle.gghub.maa_ha` with tag `acfs_resync`.

ACFS replication resync initializes the replication between the primary and standby GGHub clusters.

A resync may be required if ACFS replication is in error status and cannot be recovered.

```
(gghub) [~]$ ansible-playbook oracle.gghub.maa_ha
 -i /u01/maagghub/inventory/maahub.yml  --tags acfs_resync
```

After resync is complete, validate the ACFS replication status on the primary and standby GGHub clusters using the commands provided in "Check the ACFS replication status" above.