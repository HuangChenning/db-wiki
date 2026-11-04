---
title: "User's Guide and Reference"
book: "SQL*Plus User's Guide and Reference"
doc_id: F31846-03
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sqpug/CONNECT.html
tags:
  - oracle
  - 21c
  - sqlplus-users-guide-and-reference
---

Syntax

```
CONN[ECT] [{logon | / | proxy}  [AS {SYSASM |SYSBACKUP |SYSDBA |SYSDG |SYSOPER | SYSRAC | SYSKM}]  [edition=value]]
```

where logon has the syntax:

```
username[/password] [@connect_identifier]
```

where proxy has the syntax:

```
proxyuser[username] [/password] [@connect_identifier]
```

Note:

The brackets around username in proxy are required syntax, not an indication of an optional term. For example, to connect to `scott` through proxy user `hr` with password `welcome1`.

```
CONNECT hr[scott]/welcome1
```

Connects a given username to the Oracle Database. When you run a CONNECT command, the site profile, glogin.sql, and the user profile, login.sql, are executed.

CONNECT does not reprompt for username or password if the initial connection does not succeed.

WARNING:

Including your password in plain text is a security risk. You can avoid this risk by omitting the password, and entering it only when the system prompts for it.

To connect to a database using an enterprise user proxy, you must first configure the proxy. For information about configuring an enterprise user proxy, see the [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=DBIMI).

Terms

```
username[/password]
```

The username and password you use to connect to Oracle Database. If you omit username and password, SQL\*Plus prompts you for them. If you enter a slash (/) or enter Return or click Execute when prompted for username, SQL\*Plus logs you in using a default logon. See [/ (slash)](slash.md) for more information.

If you omit only password, SQL\*Plus prompts you for password. When prompting, SQL\*Plus does not display password on your terminal screen.

See the [PASSWORD](PASSWORD.md) command for information about changing your password in SQL\*Plus.

```
connect_identifier
```

An Oracle Net connect identifier. The exact syntax depends on the Oracle Net configuration. For more information, refer to the Oracle Net manual or contact your DBA. SQL\*Plus does not prompt for a service name, but uses your default database if you do not include a connect identifier.

A connect\_identifier is also used to connect to a pluggable database (PDB). See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN13506)

```
edition=value
```

The value for the Oracle Session Edition. An edition enables two or more versions of an object in a database. It provides a staging area where changed objects can be loaded into the database, compiled, and executed during uptime. This is particularly useful to reduce downtime associated with patching an application. edition=value overrides any edition value specified in the ORA\_EDITION environment variable. For more detailed information, see [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN).

```
/ (slash)
```

Represents a default logon using operating system authentication. You cannot enter a connect\_identifier if you use a default logon. In a default logon, SQL\*Plus typically attempts to log you in using the username OPS$name, where name is your operating system username. See the [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN) for information about operating system authentication.

In SQL\*Plus command line, where applications use password credentials to connect to databases, it is possible to store the credentials in a client-side Oracle wallet. When you configure a client to use the Oracle wallet, applications can use the following syntax to connect to databases that use password authentication:

```
CONNECT /@database_alias
```

For information about configuring your client to use secure external password store and for information about managing credentials in it, see the [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=DBSEG).

```
AS {SYSASM |SYSBACKUP |SYSDBA |SYSDG |SYSOPER |SYSRAC |SYSKM}
```

The AS clause enables privileged connections by users who have been granted that system privileges. You can use any one of these privileged connections with the default logon, /.

For information about system privileges, see the [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN).

Usage

CONNECT commits the current transaction to the database, disconnects the current username from Oracle Database, and reconnects with the specified username.

If you log on or connect as a user whose account has expired, SQL\*Plus prompts you to change your password before you can connect.

If an account is locked, a message is displayed and connection into that account (as that user) is not permitted until the account is unlocked by your DBA.

For more information about user account management, refer to the CREATE USER, ALTER USER and the CREATE PROFILE commands in the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=SQLRF).

Examples

To connect across Oracle Net with username HR, to the database known by the Oracle Net alias as FLEETDB, enter

```
CONNECT HR@FLEETDB
```

For more information about setting up your password file, refer to the [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sqpug&id=ADMIN).

To connect to an instance on the current node as a privileged user named HR, enter

```
CONNECT HR AS SYSDBA
```

To connect to an instance on the current node as a privileged default user, enter

```
CONNECT / AS SYSDBA
```

You can use the CONNECT command to connect to a CDB using easy connect or a net service name.

This statement connects to the hr user using the hrapp service. The hrapp service has a PDB property for the hrpdb PDB. This example assumes that the client is configured to have a Net Service Name for the hrapp service.

```
CONNECT hr@hrapp
```