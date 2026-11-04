---
title: SHUTDOWN
book: "SQL*Plus User's Guide and Reference"
doc_id: E16604-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e16604/ch_twelve042.htm
tags:
  - oracle
  - 11g
  - sqlplus-users-guide-and-reference
---

---

Syntax

SHUTDOWN \[ABORT | IMMEDIATE | NORMAL | TRANSACTIONAL \[LOCAL\]\]

Shuts down a currently running Oracle Database instance, optionally closing and dismounting a database.

Shutdown commands that wait for current calls to complete or users to disconnect such as SHUTDOWN NORMAL and SHUTDOWN TRANSACTIONAL have a time limit of one hour that the SHUTDOWN command will wait. If all events blocking the shutdown have not occurred within one hour, the shutdown command cancels with the following message:

```
ORA-01013: user requested cancel of current operation
```

Terms

ABORT

Proceeds with the fastest possible shutdown of the database without waiting for calls to complete or users to disconnect.

Uncommitted transactions are not rolled back. Client SQL statements currently being processed are terminated. All users currently connected to the database are implicitly disconnected and the next database startup will require instance recovery.

You must use this option if a background process terminates abnormally.

IMMEDIATE

Does not wait for current calls to complete or users to disconnect from the database.

Further connects are prohibited. The database is closed and dismounted. The instance is shutdown and no instance recovery is required on the next database startup.

NORMAL

NORMAL is the default option which waits for users to disconnect from the database.

Further connects are prohibited. The database is closed and dismounted. The instance is shutdown and no instance recovery is required on the next database startup.

TRANSACTIONAL \[LOCAL\]

Performs a planned shutdown of an instance while allowing active transactions to complete first. It prevents clients from losing work without requiring all users to log off.

No client can start a new transaction on this instance. Attempting to start a new transaction results in disconnection. After completion of all transactions, any client still connected to the instance is disconnected. Now the instance shuts down just as it would if a SHUTDOWN IMMEDIATE statement was submitted. The next startup of the database will not require any instance recovery procedures.

The LOCAL mode specifies a transactional shutdown on the local instance only, so that it only waits on local transactions to complete, not all transactions. This is useful, for example, for scheduled outage maintenance.

Usage

SHUTDOWN with no arguments is equivalent to SHUTDOWN NORMAL.

You must be connected to a database as SYSOPER, or SYSDBA. You cannot connect through a multi-threaded server. See [CONNECT](ch_twelve015.md) for more information about connecting to a database.

Examples

To shutdown the database in normal mode, enter

```
SHUTDOWN
```

```
Database closed. 
Database dismounted. 
Oracle instance shut down.
```