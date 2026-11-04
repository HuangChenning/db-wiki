---
title: "SQL*Loader and PL/SQL Demonstrations"
book: "Administrator's Reference for Linux and UNIX-Based Operating Systems"
doc_id: E10839-25
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e10839/ldr_demo.htm
tags:
  - oracle
  - 11g
  - administrators-reference-for-linux-and-unix-based-operating-systems
---

## 7 SQL\*Loader and PL/SQL Demonstrations

This chapter describes how to build and run the SQL\*Loader and PL/SQL demonstration programs available with Oracle Database. It contains the following sections:

Note:

To use the demonstrations described in this chapter, you must install Oracle Database Examples included on the Oracle Database 11g Examples media. You must unlock JONES account and set the password before creating the demonstrations.

## 7.1 SQL\*Loader Demonstrations

Run the `ulcase.sh` file to run the SQL\*Loader demonstrations. To run an individual demonstration, read the information contained in the file to determine how to run it.

## 7.2 PL/SQL Demonstrations

PL/SQL includes many demonstration programs. You must build database objects and load sample data before using these programs. To build the objects and load the sample data:

1. Change directory to the PL/SQL demonstrations directory:
	```
	$ cd $ORACLE_HOME/plsql/demo
	```
2. Start SQL\*Plus, and enter the following command:
	```
	$ sqlplus 
	SQL> CONNECT JONES
	Enter password: password
	```
3. Run the following commands to build the objects and load the sample data:
	```
	SQL> @exampbld.sql
	SQL> @examplod.sql
	```
	Note:
	Build the demonstrations as any Oracle user with sufficient privileges. Run the demonstrations as the same Oracle user.

PL/SQL Kernel Demonstrations

The following PL/SQL kernel demonstrations are available with the software:

- `examp1.sql` to `examp8.sql`
- `examp11.sql` to `examp14.sql`
- `sample1.sql` to `sample4.sql`
- `extproc.sql`

To compile and run the `examp` `n``.sql` or `sample` `n``.sql` PL/SQL kernel demonstrations:

1. Start SQL\*Plus, and enter the following command:
	```
	$ cd $ORACLE_HOME/plsql/demo
	$ sqlplus 
	SQL> CONNECT JONES
	Enter password: password
	```
2. Run a command similar to the following to run a demonstration, where `demo_name` is the name of the demonstration:
	```
	SQL> @demo_name
	```

To run the `extproc.sql` demonstration:

1. If required, add an entry for external procedures to the `tnsnames.ora` file, similar to the following:
	```
	EXTPROC_CONNECTION_DATA =
	   (DESCRIPTION =
	       (ADDRESS_LIST = 
	          (ADDRESS=(PROTOCOL = IPC)( KEY = EXTPROC))
	       )
	       (CONNECT_DATA = 
	          (SID = PLSExtProc)
	       )
	    )
	```
2. If required, add an entry for external procedures to the `listener.ora` file, similar to the following:
	Note:
	The value that you specify for SID\_NAME in the `listener.ora` file must match the value that you specify for SID in the `tnsnames.ora` file.
	- On HP-UX, Linux, and Solaris:
		```
		SID_LIST_LISTENER = 
		  (SID_LIST = 
		     (SID_DESC=
		        (SID_NAME=PLSExtProc)
		        (ORACLE_HOME=oracle_home_path)
		        (ENVS=EXTPROC_DLLS=oracle_home_path/plsql/demo/extproc.so,
		           LD_LIBRARY_PATH=oracle_home_path/plsql/demo)
		        (PROGRAM=extproc)
		      )
		    )
		```
		- On AIX:
		```
		SID_LIST_LISTENER = 
		  (SID_LIST = 
		     (SID_DESC=
		        (SID_NAME=PLSExtProc)
		        (ORACLE_HOME=oracle_home_path)
		        (ENVS=EXTPROC_DLLS=oracle_home_path/plsql/demo/extproc.so,
		           LIBPATH=oracle_home_path/plsql/demo)
		        (PROGRAM=extproc)
		      )
		    )
		```
3. Change directory to `$ORACLE_HOME/plsql/demo`.
4. Run the following command to create the `extproc.so` shared library, build the required database objects, and load the sample data:
	```
	$ make -f demo_plsql.mk extproc.so exampbld examplod
	```
	Alternatively, if you have already built the database objects and loaded the sample data, then run the following command:
	```
	$ make -f demo_plsql.mk extproc.so
	```
5. From SQL\*Plus, run the following commands:
	```
	SQL> CONNECT SYSTEM
	Enter password: system_password
	SQL> GRANT CREATE LIBRARY TO JONES;
	SQL> CONNECT JONES
	Enter password: password
	SQL> CREATE OR REPLACE LIBRARY demolib IS
	  2  'oracle_home_path/plsql/demo/extproc.so';
	  3  /
	```
	Note:
	`CREATE LIBRARY` is a very high privilege. This privilege must be granted only to trusted users.
6. To start the demonstration, run the following command:
	```
	SQL> @extproc
	```

PL/SQL Precompiler Demonstrations

Note:

The `make` commands shown in this section build the required database objects and load the sample data in the JONES schema.

The following precompiler demonstrations are available:

- `examp9.pc`
- `examp10.pc`
- `sample5.pc`
- `sample6.pc`

To build the PL/SQL precompiler demonstrations, set the library path environment variable to include the `$ORACLE_HOME/lib` directory, and run the following commands:

```
$ cd $ORACLE_HOME/plsql/demo
$ make -f demo_plsql.mk demos
```

To build a single demonstration, run its name as the argument in the `make` command. For example, to build the `examp9` demonstration, run the following command:

```
$ make -f demo_plsql.mk examp9
```

To start the `examp9` demonstration, run the following command:

```
$ ./examp9
```

## 7.3 Calling 32-Bit External Procedures from 64-Bit Oracle Database PL/SQL

Note:

This section applies to any 64-Bit Oracle Database.

Starting with Oracle Database 11g release 2 (11.2), `extproc32` is no longer available from 64-bit Oracle database install. Therefore, if you have a requirement to run 32-bit external procedures from 64-bit Oracle database, you must obtain 32-bit `extproc` by installing the corresponding 32-bit client software for your platform. Specifically, you must choose custom install within 32-bit client installation, and then select both Oracle Database Utilities and Oracle listener.

In other words, you need a separate Oracle home (32-bit) to run the 32-bit `extproc`. Note that the executable name is not `extproc32` anymore, but simply `extproc`.

To enable 32-bit external procedures on 64-bit Oracle database environment, you must configure 32-bit listener for `extproc` and specify Oracle home (from the 32-bit client install) for the `extproc` `listener.ora` entry.