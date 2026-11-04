---
title: "Chapter 9 Using MySQL Enterprise Backup with Group Replication"
book: "MySQL Enterprise Backup User's Guide (Version 9.7.0)"
version: "9.7"
source: "https://dev.mysql.com/doc/mysql-enterprise-backup/9.7/en/meb-group-replication.html"
tags:
  - mysql
  - mysql-9.7
  - enterprise-backup
---

MySQL Enterprise Backup User's Guide (Version 9.7.0)

For how to use MySQL Enterprise Backup to back up and subsequently restore a [Group Replication](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/group-replication.html) member, see [Using MySQL Enterprise Backup with Group Replication](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/group-replication-enterprise-backup.html).

When working with a [Group Replication](https://docs.oracle.com/cd/E17952_01/mysql-9.7-en/group-replication.html) setup, **mysqlbackup** makes the backup information available to all members of the server group by making sure that the `backup_history`, `backup_sbt_history` (when [using the SBT API](meb-backup-osb.md)), and `backup_progress` tables are updated on a primary node for each **mysqlbackup** operation. For the feature to work on any host in a Group Replication setup, make sure the following requirements are met:

- Host names or host addresses contained in the `member_host` column in the `performance_schema.replication_group_members` table must be resolvable by **mysqlbackup**.
- In addition to the `mysqlbackup@localhost` account created on each host as described in [Section 4.1.2, “Grant MySQL Privileges to Backup Administrator”](mysqlbackup.privileges.md), accounts for the user `mysqlbackup` to access *all* hosts in the group have been created on *every* member of the server group. These are sample statements for creating the accounts:
	```
	CREATE USER 'mysqlbackup'@'host1' IDENTIFIED BY 'password';
	CREATE USER 'mysqlbackup'@'host2' IDENTIFIED BY 'password';
	CREATE USER 'mysqlbackup'@'host3' IDENTIFIED BY 'password';
	...
	```
	Or, if the host names fall into a pattern, use a wildcard for the host names (if allowed by your environment's security policy) to perform the same task with a single statement; for example:
	```
	CREATE USER 'mysqlbackup'@'host_' IDENTIFIED BY 'password';
	```
- The account `mysqlbackup@localhost` *AND* all other accounts for accessing the hosts (i.e., ``mysqlbackup@*`host1`*``, ``mysqlbackup@*`host2`*``,``mysqlbackup@*`host3`*``, etc, or simply `mysqlbackup@host_` in our example) use *the same password* for server access. This is needed because, depending on how host names are resolved, **mysqlbackup** will likely be using two accounts to finish a backup job on a Group Replication set up (one for the actual backup operation, the other for updating the history and progress tables on a primary host), but only one password can be specified in the backup command. Therefore, the accounts must use the same password.
- All the privileges granted to `mysqlbackup@localhost` as described in [Section 4.1.2, “Grant MySQL Privileges to Backup Administrator”](mysqlbackup.privileges.md) are also granted to all other accounts with which **mysqlbackup** connects to the hosts:
	```
	GRANT SELECT ON performance_schema.replication_group_members TO 'mysqlbackup'@'host1'; 
	GRANT SELECT ON performance_schema.replication_group_members TO 'mysqlbackup'@'host2'; 
	GRANT SELECT ON performance_schema.replication_group_members TO 'mysqlbackup'@'host3';
	[More grant statements for other privileges for all hosts ...]
	```
	Or, if the host names fall into a pattern, use a wildcard for the host names (if allowed by your environment's security policy) to perform the same task; for example:
	```
	GRANT SELECT ON performance_schema.replication_group_members TO 'mysqlbackup'@'host_'; 
	[More grant statements for other privileges...]
	```