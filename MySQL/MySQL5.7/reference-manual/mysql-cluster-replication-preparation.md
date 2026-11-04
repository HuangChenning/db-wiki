---
title: "21.7.5 Preparing the NDB Cluster for Replication"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/mysql-cluster-replication-preparation.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 21.7.5 Preparing the NDB Cluster for Replication

Preparing the NDB Cluster for replication consists of the following steps:

1. Check all MySQL servers for version compatibility (see [Section 21.7.2, “General Requirements for NDB Cluster Replication”](mysql-cluster-replication-general.md)).
2. Create a replication account on the source Cluster with the appropriate privileges, using the following two SQL statements:
	```
	mysqlS> CREATE USER 'replica_user'@'replica_host'
	     -> IDENTIFIED BY 'replica_password';
	mysqlS> GRANT REPLICATION SLAVE ON *.*
	     -> TO 'replica_user'@'replica_host';
	```
	In the previous statement, *`replica_user`* is the replication account user name, *`replica_host`* is the host name or IP address of the replica, and *`replica_password`* is the password to assign to this account.
	For example, to create a replica user account with the name `myreplica`, logging in from the host named `replica-host`, and using the password `53cr37`, use the following [`CREATE USER`](create-user.md) and [`GRANT`](grant.md) statements:
	```
	mysqlS> CREATE USER 'myreplica'@'replica-host'
	     -> IDENTIFIED BY '53cr37';
	mysqlS> GRANT REPLICATION SLAVE ON *.*
	     -> TO 'myreplica'@'replica-host';
	```
	For security reasons, it is preferable to use a unique user account—not employed for any other purpose—for the replication account.
3. Set up the replica to use the source. Using the [**mysql**](mysql.md) client, this can be accomplished with the following [`CHANGE MASTER TO`](change-master-to.md) statement:
	```
	mysqlR> CHANGE MASTER TO
	     -> MASTER_HOST='source_host',
	     -> MASTER_PORT=source_port,
	     -> MASTER_USER='replica_user',
	     -> MASTER_PASSWORD='replica_password';
	```
	In the previous statement, *`source_host`* is the host name or IP address of the replication source, *`source_port`* is the port for the replica to use when connecting to the source, *`replica_user`* is the user name set up for the replica on the source, and *`replica_password`* is the password set for that user account in the previous step.
	For example, to tell the replica to use the MySQL server whose host name is `rep-source` with the replication account created in the previous step, use the following statement:
	```
	mysqlR> CHANGE MASTER TO
	     -> MASTER_HOST='rep-source',
	     -> MASTER_PORT=3306,
	     -> MASTER_USER='myreplica',
	     -> MASTER_PASSWORD='53cr37';
	```
	For a complete list of options that can be used with this statement, see [Section 13.4.2.1, “CHANGE MASTER TO Statement”](change-master-to.md).
	To provide replication backup capability, you also need to add an [`--ndb-connectstring`](mysql-cluster-options-variables.md) option to the replica's `my.cnf` file prior to starting the replication process. See [Section 21.7.9, “NDB Cluster Backups With NDB Cluster Replication”](mysql-cluster-replication-backups.md), for details.
	For additional options that can be set in `my.cnf` for replicas, see [Section 16.1.6, “Replication and Binary Logging Options and Variables”](replication-options.md).
4. If the source cluster is already in use, you can create a backup of the source and load this onto the replica to cut down on the amount of time required for the replica to synchronize itself with the source. If the replica is also running NDB Cluster, this can be accomplished using the backup and restore procedure described in [Section 21.7.9, “NDB Cluster Backups With NDB Cluster Replication”](mysql-cluster-replication-backups.md).
	```
	ndb-connectstring=management_host[:port]
	```
	In the event that you are *not* using NDB Cluster on the replica, you can create a backup with this command on the source:
	```
	shellS> mysqldump --master-data=1
	```
	Then import the resulting data dump onto the replica by copying the dump file over to it. After this, you can use the [**mysql**](mysql.md) client to import the data from the dumpfile into the replica database as shown here, where *`dump_file`* is the name of the file that was generated using [**mysqldump**](mysqldump.md) on the source, and *`db_name`* is the name of the database to be replicated:
	```
	shellR> mysql -u root -p db_name < dump_file
	```
	For a complete list of options to use with [**mysqldump**](mysqldump.md), see [Section 4.5.4, “mysqldump — A Database Backup Program”](mysqldump.md).
	Note
	If you copy the data to the replica in this fashion, you should make sure that the replica is started with the [`--skip-slave-start`](replication-options-replica.md) option on the command line, or else include `skip-slave-start` in the replica's `my.cnf` file to keep it from trying to connect to the source to begin replicating before all the data has been loaded. Once the data loading has completed, follow the additional steps outlined in the next two sections.
5. Ensure that each MySQL server acting as a replication source is assigned a unique server ID, and has binary logging enabled, using the row-based format. (See [Section 16.2.1, “Replication Formats”](replication-formats.md).) In addition, we recommend enabling the [`slave_allow_batching`](mysql-cluster-options-variables.md) system variable; beginning with NDB 7.6.23, a warning is issued if this variable is set to `OFF`. You should also consider increasing the values used with the [`--ndb-batch-size`](mysql-cluster-options-variables.md) and [`--ndb-blob-write-batch-bytes`](mysql-cluster-options-variables.md) options as well. All of these options can be set either in the source server's `my.cnf` file, or on the command line when starting the source [**mysqld**](mysqld.md) process. See [Section 21.7.6, “Starting NDB Cluster Replication (Single Replication Channel)”](mysql-cluster-replication-starting.md), for more information.