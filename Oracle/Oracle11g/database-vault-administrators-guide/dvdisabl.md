---
title: "Disabling and Enabling Oracle Database Vault"
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvdisabl.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## B Disabling and Enabling Oracle Database Vault

This appendix contains:

## When You Must Disable Oracle Database Vault

You may need to disable Oracle Database Vault to perform upgrade tasks or correct erroneous configurations. You can reenable Oracle Database Vault after you complete the corrective tasks.

Note:

Be aware that if you disable Oracle Database Vault, the privileges that were revoked from existing users and roles during installation remain in effect. See ["Privileges That Are Revoked from Existing Users and Roles"](dv_impact.md) for a listing of the revoked privileges.

The following situations require you to disable Oracle Database Vault:

- The Oracle Database Vault user accounts have been inadvertently locked or their passwords forgotten. (See the tip under ["Oracle Database Vault Accounts"](db_objects.md) for a guideline for avoiding this problem in the future.)
- A rule set associated with the `CONNECT` role has been configured incorrectly. This is resulting in failed database logins for all accounts, including those with the `DV_OWNER` or `DV_ADMIN` role, who could correct this problem.
- You must perform maintenance tasks on Oracle Database Vault.
- You must install any of the Oracle Database optional products or features, such as Oracle Spatial, or Oracle Multimedia, by using Database Configuration Assistant (DBCA).
- You are about to install a third-party product, install an Oracle product, or perform an Oracle patch update whose installation may be prevented if Oracle Database Vault is running.
- You must archive the Oracle Database Vault audit trail.

## Checking if Oracle Database Vault Is Enabled or Disabled

You can check if Oracle Database Vault is enabled or disabled by querying the `V$OPTION` data dictionary view. Any user can query this view. If Oracle Database Vault is enabled, the query returns `TRUE`. Otherwise, it returns `FALSE`.

Remember that the `PARAMETER` column value is case sensitive. For example:

```
SELECT * FROM V$OPTION WHERE PARAMETER = 'Oracle Database Vault';
```

If Oracle Database Vault is enabled, the following output appears:

```
PARAMETER                     VALUE
----------------------------- -----------------------
Oracle Database Vault         TRUE
```

## Step 1: Disable Oracle Database Vault

To disable Oracle Database Vault:

1. Stop the database, Database Control console process, and listener.
	- UNIX: Ensure that the environment variables, `ORACLE_HOME`, `ORACLE_SID`, and `PATH` are correctly set. Log in to SQL\*Plus as user `SYS` with the `SYSOPER` privilege and shut down the database. Then from the command line, stop the Database Control console process and listener.
		For example:
		```
		sqlplus sys as sysoper
		Enter password: password
		SQL> SHUTDOWN IMMEDIATE
		SQL> EXIT
		$ emctl stop dbconsole
		$ lsnrctl stop [listener_name]
		```
		For Oracle RAC installations, shut down each database instance as follows:
		```
		$ srvctl stop database -d db_name
		```
		- Windows: Stop the database, Database Control console process, and listener from the Services tool in the Control Panel. The names of Oracle Database services begin with `Oracle`.
2. Disable Oracle Database Vault as follows:
	- UNIX: Run the following commands:
		```
		$ cd $ORACLE_HOME/rdbms/lib
		$ make -f ins_rdbms.mk dv_off ioracle
		```
		If your database is using the IPC protocol for Oracle Exadata storage, then use the following commands to disable Database Vault.
		```
		$ cd $ORACLE_HOME/rdbms/lib
		$ make –f ins_rdbms.mk dv_off ipc_rds ioracle
		```
		- Windows: In the `ORACLE_HOME` `\bin` directory, rename the `oradvll.dll` file to another name, such as `oradvll.dll.dbl`.
3. Restart the database, Database Control console process, and listener.
	- UNIX: Log in to SQL\*Plus as user `SYS` with the `SYSOPER` privilege and restart the database. Then from the command line, restart the Database Control process and listener.
		For example:
		```
		sqlplus sys as sysoper
		Enter password: password
		SQL> STARTUP
		SQL> EXIT
		$ emctl start dbconsole
		$ lsnrctl start [listener_name]
		```
		For Oracle RAC installations, restart each database instance as follows:
		```
		$ srvctl start database -d db_name
		```
		- Windows: Restart the database, Database Control console process, and listener from the Services tool in the Control Panel. The names of Oracle Database services begin with `Oracle`.
4. For Oracle RAC installations, repeat these steps for each node on which the database is installed.

## Step 2: Perform the Required Tasks

At this stage, Oracle Database Vault is disabled. You can perform the following types of activities:

- Use the Oracle Database Vault PL/SQL packages and functions. For example, to correct a login or `CONNECT` rule set error, use the `DBMS_MACADM` PL/SQL package or the Oracle Database Vault Administrator interface.
- Use the SYSTEM or SYS accounts to perform tasks such as creating or changing passwords, or locking and unlocking accounts. In addition to modifying regular database and administrative user accounts, you can modify passwords and the lock status of any of the Oracle Database Vault-specific accounts, such as users who have been granted the `DV_ADMIN` or `DV_ACCTMGR` roles. (See the tip under ["Oracle Database Vault Accounts"](db_objects.md) for a guideline for avoiding this problem in the future.)
- Perform the installation, upgrade, or other tasks that require security protections to be disabled.

## Step 3: Enable Oracle Database Vault

To enable Oracle Database Vault:

1. Stop the database, Database Control console process, and listener.
	- UNIX: Ensure that the environment variables, `ORACLE_HOME`, `ORACLE_SID`, and `PATH` are correctly set. Log in to SQL\*Plus as user `SYS` with the `SYSOPER` privilege and shut down the database. Then from the command line, stop the Database Control console process and listener.
		For example:
		```
		sqlplus sys as sysoper
		Enter password: password
		SQL> SHUTDOWN IMMEDIATE
		SQL> EXIT
		$ emctl stop dbconsole
		$ lsnrctl stop [listener_name]
		```
		For Oracle RAC installations, shut down each database instance as follows:
		```
		$ srvctl stop database -d db_name
		```
		- Windows: Stop the database, Database Control console process, and listener from the Services tool in the Control Panel. The names of Oracle Database services begin with `Oracle`.
2. Enable Oracle Database Vault as follows:
	- UNIX: Run the following commands. The `make` command enables both Oracle Database Vault (`dv_on`) and Oracle Label Security (`lbac_on`). You must enable Oracle Label Security before you can use Database Vault.
		```
		$ cd $ORACLE_HOME/rdbms/lib
		$ make -f ins_rdbms.mk dv_on lbac_on ioracle
		```
		If you want to use the IPC protocol for Oracle Exadata storage, then use the following commands to enable Database Vault and Label Security.
		```
		$ cd $ORACLE_HOME/rdbms/lib
		$ make –f ins_rdbms.mk dv_on lbac_on ipc_rds ioracle
		```
		- Windows: In the `ORACLE_HOME` `\bin` directory, rename the backed up copy of the `oradvll.dll` file (for example, `oradv11.dll.dbl`) to `oradvll.dll`. Ensure that the name of the Oracle Label Security executable is `oralbacll.dll` (and not `oralbacll.dll.dbl` or some other backup name). You must enable Oracle Label Security before you can use Database Vault.
3. Restart the database, Database Control console process, and listener.
	- UNIX: Log in to SQL\*Plus as user `SYS` with the `SYSOPER` privilege and restart the database. Then from the command line, restart the Database Control console process and listener.
		For example:
		```
		sqlplus sys as sysoper
		Enter password: password
		SQL> STARTUP
		SQL> EXIT
		$ emctl start dbconsole
		$ lsnrctl start [listener_name]
		```
		For Oracle RAC installations, restart each database instance as follows:
		```
		$ srvctl start database -d db_name
		```
		- Windows: Restart the database, Database Control console process, and listener from the Services tool in the Control Panel. The names of Oracle Database services begin with `Oracle`.
4. For Oracle RAC installations, repeat these steps for each node on which the database is installed.