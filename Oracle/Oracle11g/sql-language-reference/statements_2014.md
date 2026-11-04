---
title: ALTER SYSTEM
book: SQL Language Reference
doc_id: E41084-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_2014.htm
tags:
  - oracle
  - 11g
  - sql-language-reference
---

Purpose

Use the `ALTER` `SYSTEM` statement to dynamically alter your Oracle Database instance. The settings stay in effect as long as the database is mounted.

Prerequisites

You must have `ALTER` `SYSTEM` system privilege.

Syntax

alter\_system::=

![alter_system](img/alter_system.gif)

> ```
> ALTER SYSTEM
>   { archive_log_clause
>   | checkpoint_clause
>   | check_datafiles_clause
>   | distributed_recov_clauses
>   | FLUSH { SHARED_POOL | GLOBAL CONTEXT | BUFFER_CACHE
>           | REDO TO target_db_name [ [ NO ] CONFIRM APPLY ] }
>   | end_session_clauses
>   | SWITCH LOGFILE
>   | { SUSPEND | RESUME }
>   | quiesce_clauses
>   | rolling_migration_clauses
>   | security_clauses
>   | shutdown_dispatcher_clause
>   | REGISTER
>   | SET alter_system_set_clause
>         [ alter_system_set_clause ]...
>   | RESET alter_system_reset_clause
>           [ alter_system_reset_clause ]...
>   } ;
> ```
  
  

(archive\_log\_clause::=, checkpoint\_clause::=, check\_datafiles\_clause::=, distributed\_recov\_clauses::=, end\_session\_clauses::=, quiesce\_clauses::=, rolling\_migration\_clauses::=, security\_clauses::=, shutdown\_dispatcher\_clause::=, alter\_system\_set\_clause::=, alter\_system\_reset\_clause::=)

archive\_log\_clause::=

![archive_log_clause](img/archive_log_clause.gif)

> ```
> ARCHIVE LOG
>    [  INSTANCE 'instance_name' ]
>    { { SEQUENCE integer
>      | CHANGE integer
>      | CURRENT [ NOSWITCH ]
>      | GROUP integer
>      | LOGFILE 'filename'
>           [ USING BACKUP CONTROLFILE ]
>      | NEXT
>      | ALL
>      }
>      [ TO 'location' ]
>    }
> ```
  
  

checkpoint\_clause::=

![checkpoint_clause](img/checkpoint_clause.gif)

> ```
> CHECKPOINT [ GLOBAL | LOCAL ]
> ```
  
  

check\_datafiles\_clause::=

![check_datafiles_clause](img/check_datafiles_clause.gif)

> ```
> CHECK DATAFILES [ GLOBAL | LOCAL ]
> ```
  
  

distributed\_recov\_clauses::=

![distributed_recov_clauses](img/distributed_recov_clauses.gif)

> ```
> { ENABLE | DISABLE } DISTRIBUTED RECOVERY
> ```
  
  

end\_session\_clauses::=

![end_session_clauses](img/end_session_clauses.gif)

> ```
> { DISCONNECT SESSION 'integer1, integer2'
>      [ POST_TRANSACTION ]
> | KILL SESSION 'integer1, integer2 [, @integer3]'
> }
> [ IMMEDIATE ]
> ```
  
  

quiesce\_clauses::=

![quiesce_clauses](img/quiesce_clauses.gif)

> ```
> QUIESCE RESTRICTED | UNQUIESCE
> ```
  
  

rolling\_migration\_clauses::=

![rolling_migration_clauses](img/rolling_migration_clauses.gif)

> ```
> { START ROLLING MIGRATION TO 'ASM_version'
> | STOP ROLLING MIGRATION
> }
> ```
  
  

security\_clauses::=

![security_clauses](img/security_clauses.gif)

> ```
> { { ENABLE | DISABLE } RESTRICTED SESSION
> | SET ENCRYPTION WALLET OPEN IDENTIFIED BY
>   { "wallet_password" | "HSM_auth_string" }
> | SET ENCRYPTION WALLET CLOSE
>   [ IDENTIFIED BY { "wallet_password" | "HSM_auth_string" } ]
> | "set_encryption_key"
> }
> ```
  
  

set\_encryption\_key::=

![set_encryption_key](img/set_encryption_key.gif)

> ```
> { SET ENCRYPTION KEY
>   {
>     [ "certificate_id" ] IDENTIFIED BY "wallet_password"
>     |
>     IDENTIFIED BY "HSM_auth_string" [ MIGRATE USING "wallet_password" ]
>   }
> }
> ```
  
  

shutdown\_dispatcher\_clause::=

![shutdown_dispatcher_clause](img/shutdown_dispatcher_clause.gif)

> ```
> SHUTDOWN [ IMMEDIATE ] dispatcher_name
> ```
  
  

alter\_system\_set\_clause::=

![alter_system_set_clause](img/alter_system_set_clause.gif)

> ```
> { set_parameter_clause
> | USE_STORED_OUTLINES = (TRUE | FALSE | category_name)
> | GLOBAL_TOPIC_ENABLED = (TRUE | FALSE)
> }
> ```
  
  

set\_parameter\_clause::=

![set_parameter_clause](img/set_parameter_clause.gif)

> ```
> parameter_name =
>    parameter_value [, parameter_value ]...
>    [ COMMENT = string ]
>    [ DEFERRED ]
>    [ { SCOPE = { MEMORY | SPFILE | BOTH }
>      | SID = { 'sid' | '*' }
>      }...
>    ]
> ```
  
  

alter\_system\_reset\_clause::=

![alter_system_reset_clause](img/alter_system_reset_clause.gif)

> ```
> parameter_name
>    [ { SCOPE = SPFILE 
>      | SID = { 'sid' | '*' }
>      }...
>    ]
> ```
  

Semantics

archive\_log\_clause

The `archive_log_clause` manually archives redo log files or enables or disables automatic archiving. To use this clause, your instance must have the database mounted. The database can be either open or closed unless otherwise noted.

INSTANCE Clause

This clause is relevant only if you are using Oracle Real Application Clusters (Oracle RAC). Specify the name of the instance for which you want the redo log file group to be archived. The instance name is a string of up to 80 characters. Oracle Database automatically determines the thread that is mapped to the specified instance and archives the corresponding redo log file group. If no thread is mapped to the specified instance, then Oracle Database returns an error.

SEQUENCE Clause

Specify `SEQUENCE` to manually archive the online redo log file group identified by the log sequence number `integer` in the specified thread. If you omit the `THREAD` parameter, then Oracle Database archives the specified group from the thread assigned to your instance.

CHANGE Clause

Specify `CHANGE` to manually archive the online redo log file group containing the redo log entry with the system change number (SCN) specified by `integer` in the specified thread. If the SCN is in the current redo log file group, then Oracle Database performs a log switch. If you omit the `THREAD` parameter, then Oracle Database archives the groups containing this SCN from all enabled threads.

You can use this clause only when your instance has the database open.

CURRENT Clause

Specify `CURRENT` to manually archive the current redo log file group of the specified thread, forcing a log switch. If you omit the `THREAD` parameter, then Oracle Database archives all redo log file groups from all enabled threads, including logs previous to current logs. You can specify `CURRENT` only when the database is open.

NOSWITCH Specify `NOSWITCH` if you want to manually archive the current redo log file group without forcing a log switch. This setting is used primarily with standby databases to prevent data divergence when the primary database shuts down. Divergence implies the possibility of data loss in case of primary database failure.

You can use the `NOSWITCH` clause only when your instance has the database mounted but not open. If the database is open, then this operation closes the database automatically. You must then manually shut down the database before you can reopen it.

GROUP Clause

Specify `GROUP` to manually archive the online redo log file group with the `GROUP` value specified by `integer`. You can determine the `GROUP` value for a redo log file group by querying the dynamic performance view `V$LOG`. If you specify both the `THREAD` and `GROUP` parameters, then the specified redo log file group must be in the specified thread.

LOGFILE Clause

Specify `LOGFILE` to manually archive the online redo log file group containing the redo log file member identified by ' `filename` '. If you specify both the `THREAD` and `LOGFILE` parameters, then the specified redo log file group must be in the specified thread.

If the database was mounted with a backup control file, then specify `USING` `BACKUP` `CONTROLFILE` to permit archiving of all online logfiles, including the current logfile.

Restriction on the LOGFILE clause You must archive redo log file groups in the order in which they are filled. If you specify a redo log file group for archiving with the `LOGFILE` parameter, and earlier redo log file groups are not yet archived, then Oracle Database returns an error.

NEXT Clause

Specify `NEXT` to manually archive the next online redo log file group from the specified thread that is full but has not yet been archived. If you omit the `THREAD` parameter, then Oracle Database archives the earliest unarchived redo log file group from any enabled thread.

ALL Clause

Specify `ALL` to manually archive all online redo log file groups from the specified thread that are full but have not been archived. If you omit the `THREAD` parameter, then Oracle Database archives all full unarchived redo log file groups from all enabled threads.

TO location Clause

Specify `TO` ' `location` ' to indicate the primary location to which the redo log file groups are archived. The value of this parameter must be a fully specified file location following the conventions of your operating system. If you omit this parameter, then Oracle Database archives the redo log file group to the location specified by the initialization parameters `LOG_ARCHIVE_DEST` or `LOG_ARCHIVE_DEST_` `n`.

checkpoint\_clause

Specify `CHECKPOINT` to explicitly force Oracle Database to perform a checkpoint, ensuring that all changes made by committed transactions are written to data files on disk. You can specify this clause only when your instance has the database open. Oracle Database does not return control to you until the checkpoint is complete.

GLOBAL In an Oracle Real Application Clusters (Oracle RAC) environment, this setting causes Oracle Database to perform a checkpoint for all instances that have opened the database. This is the default.

LOCAL In an Oracle RAC environment, this setting causes Oracle Database to perform a checkpoint only for the thread of redo log file groups for the instance from which you issue the statement.

See Also:

"Forcing a Checkpoint: Example"

check\_datafiles\_clause

In a distributed database system, such as an Oracle RAC environment, this clause updates an instance's SGA from the database control file to reflect information on all online data files.

- Specify `GLOBAL` to perform this synchronization for all instances that have opened the database. This is the default.
- Specify `LOCAL` to perform this synchronization only for the local instance.

Your instance should have the database open.

end\_session\_clauses

The `end_session_clauses` give you several ways to end the current session.

DISCONNECT SESSION Clause

Use the `DISCONNECT` `SESSION` clause to disconnect the current session by destroying the dedicated server process (or virtual circuit if the connection was made by way of a Shared Sever). To use this clause, your instance must have the database open. You must identify the session with both of the following values from the `V$SESSION` view:

- For `integer1`, specify the value of the `SID` column.
- For `integer2`, specify the value of the `SERIAL#` column.

If system parameters are appropriately configured, then application failover will take effect.

- The `POST_TRANSACTION` setting allows ongoing transactions to complete before the session is disconnected. If the session has no ongoing transactions, then this clause has the same effect described for as `KILL` `SESSION`.
- The `IMMEDIATE` setting disconnects the session and recovers the entire session state immediately, without waiting for ongoing transactions to complete.
	- If you also specify `POST_TRANSACTION` and the session has ongoing transactions, then the `IMMEDIATE` keyword is ignored.
		- If you do not specify `POST_TRANSACTION`, or you specify `POST_TRANSACTION` but the session has no ongoing transactions, then this clause has the same effect as described for `KILL` `SESSION` `IMMEDIATE`.
		See Also:
		"Disconnecting a Session: Example"

KILL SESSION Clause

The `KILL` `SESSION` clause lets you mark a session as terminated, roll back ongoing transactions, release all session locks, and partially recover session resources. To use this clause, your instance must have the database open. Your session and the session to be terminated must be on the same instance unless you specify `integer3`.You must identify the session with the following values from the `V$SESSION` view:

- For `integer1`, specify the value of the `SID` column.
- For `integer2`, specify the value of the `SERIAL#` column.
- For the optional `integer3`, specify the ID of the instance where the target session to be killed exists. You can find the instance ID by querying the GV$ tables.

If the session is performing some activity that must be completed, such as waiting for a reply from a remote database or rolling back a transaction, then Oracle Database waits for this activity to complete, marks the session as terminated, and then returns control to you. If the waiting lasts a minute, then Oracle Database marks the session to be terminated and returns control to you with a message that the session is marked to be terminated. The `PMON` background process then marks the session as terminated when the activity is complete.

Whether or not the session has an ongoing transaction, Oracle Database does not recover the entire session state until the session user issues a request to the session and receives a message that the session has been terminated.

See Also:

"Terminating a Session: Example"

IMMEDIATE Specify `IMMEDIATE` to instruct Oracle Database to roll back ongoing transactions, release all session locks, recover the entire session state, and return control to you immediately.

distributed\_recov\_clauses

The `DISTRIBUTED` `RECOVERY` clause lets you enable or disable distributed recovery. To use this clause, your instance must have the database open.

ENABLE Specify `ENABLE` to enable distributed recovery. In a single-process environment, you must use this clause to initiate distributed recovery.

You may need to issue the `ENABLE` `DISTRIBUTED` `RECOVERY` statement more than once to recover an in-doubt transaction if the remote node involved in the transaction is not accessible. In-doubt transactions appear in the data dictionary view `DBA_2PC_PENDING`.

See Also:

"Enabling Distributed Recovery: Example"

DISABLE Specify `DISABLE` to disable distributed recovery.

FLUSH SHARED\_POOL Clause

The `FLUSH` `SHARED_POOL` clause lets you clear data from the shared pool in the system global area (SGA). The shared pool stores:

- Cached data dictionary information and
- Shared SQL and PL/SQL areas for SQL statements, stored procedures, function, packages, and triggers.

This statement does not clear global application context information, nor does it clear shared SQL and PL/SQL areas for items that are currently being executed. You can use this clause regardless of whether your instance has the database dismounted or mounted, open or closed.

See Also:

"Clearing the Shared Pool: Example"

FLUSH GLOBAL CONTEXT Clause

The `FLUSH` `GLOBAL` `CONTEXT` clause lets you flush all global application context information from the shared pool in the system global area (SGA). You can use this clause regardless of whether your instance has the database dismounted or mounted, open or closed.

FLUSH BUFFER\_CACHE Clause

The `FLUSH` `BUFFER_CACHE` clause lets you clear all data from the buffer cache in the system global area (SGA), including the `KEEP`, `RECYCLE`, and `DEFAULT` buffer pools.

Caution:

This clause is intended for use only on a test database. Do not use this clause on a production database, because as a result of this statement, subsequent queries will have no hits, only misses.

This clause is useful if you need to measure the performance of rewritten queries or a suite of queries from identical starting points.

FLUSH REDO Clause

Use the `FLUSH` `REDO` clause to flush redo data from a primary database to a standby database and to optionally wait for the flushed redo data to be applied to a physical or logical standby database.

This clause can allow a failover to be performed on the target standby database without data loss, even if the primary database is not in a zero data loss data protection mode, provided that all redo data that has been generated by the primary database can be flushed to the standby database.

The `FLUSH` `REDO` clause must be issued on a mounted, but not open, primary database.

target\_db\_name

For `target_db_name`, specify the `DB_UNIQUE_NAME` of the standby database that is to receive the redo data flushed from the primary database.

The value of the `LOG_ARCHIVE_DEST_` `n` database initialization parameter that corresponds to the target standby database must contain the `DB_UNIQUE_NAME` attribute, and the value of that attribute must match the `DB_UNIQUE_NAME` of the target standby database.

NO CONFIRM APPLY

If you specify this clause, then the `ALTER` `SYSTEM` statement will not complete until the standby database has received all of the flushed redo data. You must specify this clause if the target standby database is a snapshot standby database.

CONFIRM APPLY

If you specify this clause, then the `ALTER` `SYSTEM` statement will not complete until the target standby database has received and applied all flushed redo data. This is the default behavior unless you specify `NO` `CONFIRM` `APPLY`. You cannot specify this clause if the target standby database is a snapshot standby database.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/sql_stmts.htm#SBYDB01222) for more information about the `FLUSH` `REDO` clause and failovers

SWITCH LOGFILE Clause

The `SWITCH` `LOGFILE` clause lets you explicitly force Oracle Database to begin writing to a new redo log file group, regardless of whether the files in the current redo log file group are full. When you force a log switch, Oracle Database begins to perform a checkpoint but returns control to you immediately rather than when the checkpoint is complete. To use this clause, your instance must have the database open.

See Also:

"Forcing a Log Switch: Example"

SUSPEND | RESUME

The `SUSPEND` clause lets you suspend all I/O (data file, control file, and file header) as well as queries, in all instances, enabling you to make copies of the database without having to handle ongoing transactions.

Restrictions on SUSPEND and RESUME `SUSPEND` and `RESUME` are subject to the following restrictions:

- Do not use this clause unless you have put the database tablespaces in hot backup mode.
- Do not terminate the session that issued the `ALTER` `SYSTEM` `SUSPEND` statement. An attempt to reconnect while the system is suspended may fail because of recursive SQL that is running during the `SYS` login.
- If you start a new instance while the system is suspended, then that new instance will not be suspended.

The `RESUME` clause lets you make the database available once again for queries and I/O.

rolling\_migration\_clauses

Use these clauses in a clustered Oracle Automatic Storage Management (Oracle ASM) environment to migrate one node at a time to a different Oracle ASM version without affecting the overall availability of the Oracle ASM cluster or the database clusters using Oracle ASM for storage.

START ROLLING MIGRATION When starting rolling upgrade, for `ASM_version`, you must specify the following string:

```
'<version_num>, <release_num>, <update_num>,<port_release_num>,<port_update_num>'
```

`ASM_version` must be equal to or greater than 11.1.0.0.0. The surrounding single quotation marks are required. Oracle ASM first verifies that the current release is compatible for migration to the specified release, and then goes into limited functionality mode. Oracle ASM then determines whether any rebalance operations are under way anywhere in the cluster. If there are any such operations, then the statement fails and must be reissued after the rebalance operations are complete.

Rolling upgrade mode is a cluster-wide in-memory persistent state. The cluster continues to be in this state until there is at least one Oracle ASM instance running in the cluster. Any new instance joining the cluster switches to migration mode immediately upon startup. If all the instances in the cluster terminate, then subsequent startup of any Oracle ASM instance will not be in rolling upgrade mode until you reissue this statement to restart rolling upgrade of the Oracle ASM instances.

STOP ROLLING MIGRATION Use this clause to stop rolling upgrade and bring the cluster back into normal operation. Specify this clause only after all instances in the cluster have migrated to the same software version. The statement will fail if the cluster is not in rolling upgrade mode.

When you specify this clause, the Oracle ASM instance validates that all the members of the cluster are at the same software version, takes the instance out of rolling upgrade mode, and returns to full functionality of the Oracle ASM cluster. If any rebalance operations are pending because disks have gone offline, then those operations are restarted if the `ASM_POWER_LIMIT` parameter would not be violated by such a restart.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm#OSTMG02400) for more information about rolling upgrade

quiesce\_clauses

Use the `QUIESCE` `RESTRICTED` and `UNQUIESCE` clauses to put the database in and take it out of the quiesced state. This state enables database administrators to perform administrative operations that cannot be safely performed in the presence of concurrent transactions, queries, or PL/SQL operations.

Note:

The `QUIESCE` `RESTRICTED` clause is valid only if the Database Resource Manager is installed and only if the Resource Manager has been on continuously since database startup in any instances that have opened the database.

If multiple `QUIESCE` `RESTRICTED` or `UNQUIESCE` statements issue at the same time from different sessions or instances, then all but one will receive an error.

QUIESCE RESTRICTED

Specify `QUIESCE` `RESTRICTED` to put the database in the quiesced state. For all instances with the database open, this clause has the following effect:

- Oracle Database instructs the Database Resource Manager in all instances to prevent all inactive sessions (other than `SYS` and `SYSTEM`) from becoming active. No user other than `SYS` and `SYSTEM` can start a new transaction, a new query, a new fetch, or a new PL/SQL operation.
- Oracle Database waits for all existing transactions in all instances that were initiated by a user other than `SYS` or `SYSTEM` to finish (either commit or abort). Oracle Database also waits for all running queries, fetches, and PL/SQL procedures in all instances that were initiated by users other than `SYS` or `SYSTEM` and that are not inside transactions to finish. If a query is carried out by multiple successive OCI fetches, then Oracle Database does not wait for all fetches to finish. It waits for the current fetch to finish and then blocks the next fetch. Oracle Database also waits for all sessions (other than those of `SYS` or `SYSTEM`) that hold any shared resources (such as enqueues) to release those resources. After all these operations finish, Oracle Database places the database into quiesced state and finishes executing the `QUIESCE` `RESTRICTED` statement.
- If an instance is running in shared server mode, then Oracle Database instructs the Database Resource Manager to block logins (other than `SYS` or `SYSTEM`) on that instance. If an instance is running in non-shared-server mode, then Oracle Database does not impose any restrictions on user logins in that instance.

During the quiesced state, you cannot change the Resource Manager plan in any instance.

UNQUIESCE

Specify `UNQUIESCE` to take the database out of quiesced state. Doing so permits transactions, queries, fetches, and PL/SQL procedures that were initiated by users other than `SYS` or `SYSTEM` to be undertaken once again. The `UNQUIESCE` statement does not have to originate in the same session that issued the `QUIESCE` `RESTRICTED` statement.

security\_clauses

The `security_clauses` let you control access to the instance. They also allow you to enable or disable access to the encrypted data in the instance.

RESTRICTED SESSION

The `RESTRICTED` `SESSION` clause lets you restrict logon to Oracle Database. You can use this clause regardless of whether your instance has the database dismounted or mounted, open or closed.

- Specify `ENABLE` to allow only users with `RESTRICTED` `SESSION` system privilege to log on to Oracle Database. Existing sessions are not terminated.
	This clause applies only to the current instance. Therefore, in an Oracle RAC environment, authorized users without the `RESTRICTED` `SESSION` system privilege can still access the database by way of other instances.
- Specify `DISABLE` to reverse the effect of the `ENABLE` `RESTRICTED` `SESSION` clause, allowing all users with `CREATE` `SESSION` system privilege to log on to Oracle Database. This is the default.

See Also:

"Restricting Sessions: Example"

SET ENCRYPTION WALLET Clause

Use this clause to manage database access to the Transparent Data Encryption (TDE) master encryption key. The TDE master encryption key is stored in an external security module, which can be an encryption wallet or Hardware Security Module (HSM).

Although this statement begins with the keyword `ALTER`, an `ALTER` `SYSTEM` `SET` `ENCRYPTION` `WALLET` statement is not a DDL clause. However, you cannot roll back such a statement.

Although this clause begins with the `SET` keyword, do not confuse it with the alter\_system\_set\_clause, which allows you to use the `SET` keyword to set the value of initialization parameters. `ENCRYPTION` `WALLET` is not an initialization parameter.

OPEN

When you specify this clause, the database uses the specified password to open the encryption wallet and load the TDE master key into database memory for the duration of the instance, or establish a connection to the HSM in order to send the encrypted table and tablespace keys to the HSM and receive then back decrypted.

- Specify `wallet_password` to retrieve the master encryption key from the encryption wallet. If the encryption wallet is not available or is already open, then the database returns an error. The double quotation marks around `wallet_password` are required.
- Specify `HSM_auth_string` to make the HSM accessible. `HSM_auth_string` is of the form " `user_id`:`password` " where:
	- `user_id` is the user ID created for the database using the HSM management interface
		- `password` is the password created for the user ID using the HSM management interface
	The double quotation marks around `HSM_auth_string` are required

CLOSE Use this clause to disable encryption and decryption in your database. The `wallet_password` is required to close an encryption wallet. `HSM_auth_string` is required to disable access to the HSM. Refer to OPEN for details on specifying `HSM_auth_string`.

A password is not required to close an auto-open wallet when only an auto-open wallet is present. The password is required to close an auto-open wallet when both an auto-open wallet and an encryption wallet are open. In this case, using `CLOSE` with a password will close the auto-open wallet and the encryption wallet.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/design.htm#RACAD7269) for information on setting encryption wallets in an Oracle Real Application Clusters (Oracle RAC) environment

set\_encryption\_key

Use this clause to generate a new TDE master encryption key, if none exists. If there are existing master keys in the HSM or wallet, then this clause rekeys the existing table and tablespace keys, that is, it decrypts all table and tablespace keys with the old master key and reencrypts them with the new master key.

An `ALTER` `SYSTEM` `SET` `ENCRYPTION` `KEY` statement is a DDL statement and will automatically commit any pending transactions in the schema.

Although this clause begins with the `SET` keyword, do not confuse it with the alter\_system\_set\_clause, which allows you to use the `SET` keyword to set the value of initialization parameters. `ENCRYPTION` `KEY` is not an initialization parameter.

IDENTIFIED BY wallet\_password

This clause loads the TDE master encryption key from the encryption wallet into memory for access to encrypted data.

- The `certificate_id` is required if you are using PKI asymmetric key pairs as master encryption keys. Specify the integer that identifies the certificate. You can find this value by querying the `CERT_ID` column of the `V$WALLET` dynamic performance view. Do not specify `certificate_id` if you are using symmetric keys, which are the default.
- For `wallet_password`, specify the password used to connect to the security module.

If you specify an invalid `certificate_id` or `wallet_password`, then the database returns an error. The double quotation marks around `certificate_id` and `wallet_password` are required.

Restriction on IDENTIFIED BY wallet\_password PKI-based master keys, including unified master encryption keys, can only be used with TDE column encryption and an Oracle Wallet, not with HSM.

IDENTIFIED BY HSM\_auth\_string This clause creates a master encryption key that will be stored inside the HSM. The master encryption key is used to encrypt or decrypt table keys inside the HSM.

`HSM_auth_string` is of the form " `user_id`:`password` " where:

- `user_id` is the user ID created for the database using the HSM management interface
- `password` is the password created for the user ID using the HSM management interface

The double quotation marks around `HSM_auth_string` are required.

If you are already using Transparent Data Encryption with an Oracle Wallet and you would like to migrate to an HSM, then specify the `MIGRATE` `USING` `wallet_password` clause. This decrypts the existing table and tablespace keys, and then reencrypts them with the newly created, HSM-based, master encryption key. Note that the encryption wallet is still in use after you migrate to an HSM, because it may contain master encryption keys that were used for export files, RMAN backups, or encrypted data in temporary or undo tablespaces or redo log files. After migrating, perform one of the following steps:

- Change the wallet password to the `HSM_auth_string` using Oracle Wallet Manager or the `orapki` command-line tool.
- Create a local auto-open wallet from the encryption wallet and either rename the encryption wallet, or move it out of the directory specified in `ENCRYPTION_WALLET_LOCATION` in `sqlnet`.`ora`. Do not delete the encryption wallet and do not forget the wallet password.

See Also:

- [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asotrans.htm#ASOAG600) for more information on using the server wallet and encryption keys and on Transparent Data Encryption
- The description of the `CREATE` `TABLE` ["encryption\_spec "](statements_7002.md) for information on using that feature to encrypt table columns
- "Establishing a Wallet and Encryption Key: Examples"

shutdown\_dispatcher\_clause

The `SHUTDOWN` clause is relevant only if your system is using the shared server architecture of Oracle Database. It shuts down a dispatcher identified by `dispatcher_name`.

Note:

Do not confuse this clause with the SQL\*Plus command `SHUTDOWN`, which is used to shut down the entire database.

The `dispatcher_name` must be a string of the form ' `D` `xxx` ', where `xxx` indicates the number of the dispatcher. For a listing of dispatcher names, query the `NAME` column of the `V$DISPATCHER` dynamic performance view.

- If you specify `IMMEDIATE`, then the dispatcher stops accepting new connections immediately and Oracle Database terminates all existing connections through that dispatcher. After all sessions are cleaned up, the dispatcher process shuts down.
- If you do not specify `IMMEDIATE`, then the dispatcher stops accepting new connections immediately but waits for all its users to disconnect and for all its database links to terminate. Then it shuts down.

REGISTER Clause

Specify `REGISTER` to instruct the `PMON` background process to register the instance with the listeners immediately. If you do not specify this clause, then registration of the instance does not occur until the next time `PMON` executes the discovery routine. As a result, clients may not be able to access the services for as long as 60 seconds after the listener is started.

See Also:

[Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/process.htm#CNCPT1254) and [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/net_arch.htm#NETAG1080) for information on the `PMON` background process and listeners

alter\_system\_set\_clause

You can change the value of many initialization parameters for the current instance, whether you have started the database with a traditional plain-text parameter file (pfile) or with a server parameter file (spfile). [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams_part.htm#REFRN001) indicates these parameters in the "Modifiable" category of each parameter description. If you are using a pfile, then the change will persist only for the duration of the instance. However, if you have started the database with an spfile, then you can change the value of the parameter in the spfile itself, so that the new value will occur in subsequent instances.

Oracle Database Reference documents all initialization parameters in full. The parameters fall into three categories:

- [Basic parameters:](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams002.htm#REFRN00101) Database administrators should be familiar with and consider the setting for all of the basic parameters.
- [Functional categories:](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams004.htm#REFRN00102) Oracle Database Reference also lists the initialization parameters by their functional category.
- Alphabetical listing: The Table of Contents of [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) contains all initialization parameters in alphabetical order.

The ability to change initialization parameter values depends on whether you have started up the database with a traditional plain-text initialization parameter file (pfile) or with a server parameter file (spfile). To determine whether you can change the value of a particular parameter, query the `ISSYS_MODIFIABLE` column of the `V$PARAMETER` dynamic performance view.

set\_parameter\_clause

When setting a parameter value, you can specify additional settings as follows:

The clause lets you associate a comment string with this change in the value of the parameter. The comment string cannot contain control characters or a line break. If you also specify, then this comment will appear in the parameter file to indicate the most recent change made to this parameter.