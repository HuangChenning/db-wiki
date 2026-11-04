---
title: Troubleshooting Oracle Database Vault
book: "Database Vault Administrator's Guide"
doc_id: E23090-13
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23090/troubleshooting.htm
tags:
  - oracle
  - 11g
  - database-vault-administrators-guide
---

## E Troubleshooting Oracle Database Vault

This appendix contains:

## Using Trace Files to Diagnose Events in the Database

This section contains:

- About Using Trace Files to Diagnose Oracle Database Vault Events
- Types of Oracle Database Vault Trace Events That You Can and Cannot Track
- Levels of Oracle Database Vault Trace Events
- Performance Effect of Enabling Oracle Database Vault Trace Files
- Enabling Oracle Database Vault Trace Events
- Finding Oracle Database Vault Trace File Data
- Examples Oracle Database Vault Trace Files
- Disabling Oracle Database Vault Trace Events

### About Using Trace Files to Diagnose Oracle Database Vault Events

You can monitor the Oracle Database Vault database instance for server and background process events by enabling and checking the database instance trace files. Trace files reveal the Oracle Database Vault policy authorization success and failures. They are useful for providing information to help resolve bug and other issues that may occur.

To set tracing for Oracle Database Vault, you must have the `DV_ADMIN` role. To perform the configuration, you use either of the `ALTER SESSION SET EVENTS` or `ALTER SYSTEM SET EVENTS` SQL statements.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/monitoring.htm#ADMIN11243) for more information about how to manage trace files

### Types of Oracle Database Vault Trace Events That You Can and Cannot Track

Table E-1 describes the types of activities that you can track with trace files.

Table E-1 Contents of Oracle Database Vault Trace Files

| Database Vault Feature | Description |
| --- | --- |
| Realm authorizations | The trace file tracks cases of realm authorization with a rule set and realm authorization to a role. See "Examples Oracle Database Vault Trace Files" for examples of this type of trace file. |
| Rule set evaluations | The trace file includes information about a rule set evaluation from a realm authorization, for a command rule, the CONNECT command rule, and from a factor. |
| Oracle Data Pump authorization | The trace file includes Database Vault Data Pump authorization results and other user, object, and SQL text information. |
| Oracle Scheduler job authorization | The trace file includes the Database Vault Oracle Scheduler job authorization results, job name, job owner, current statement, and so on. |
| Object privilege bypass | The trace file tracks both direct grants and grants through a role. This type of trace is useful for cases where mandatory realms are not enabled, which enables users who have an object privilege to access realm protected objects. |
| Factor loading | The trace file tracks the expression and value for each factor loaded. |
| Others | Object owner bypassed realm protection and other Database Vault failed and succeeded operations |

### Levels of Oracle Database Vault Trace Events

You can use the following levels for Oracle Database Vault trace events:

- Low prints the information for all failed Oracle Database Vault authorizations to a trace file. This type of trace file includes failed realm authorizations, failed factor loading, failed rule set evaluating, and so on. It has a low impact on Oracle Database performance.
- High prints trace records that include both successful and failed authorizations. Because this type of tracing tracks all the authorizations, the overhead is larger than that of the low level tracing. In addition, the trace files are usually larger.
- Highest prints the PL/SQL stack and function call stack to a trace file, as well as what is traced at level high (as described in Table E-1). It has the highest impact on Oracle Database performance.

### Performance Effect of Enabling Oracle Database Vault Trace Files

Be careful about enabling trace files. Doing so can increase the overhead of the database instance operation, which could decrease performance.

### Enabling Oracle Database Vault Trace Events

This section contains:

- Enabling Trace Events for the Current Database Session
- Enabling Trace Events for All Database Sessions

#### Enabling Trace Events for the Current Database Session

1. Log into the database instance as a user who has been granted the `DV_ADMIN` role and the `ALTER SESSION` system privilege.
	For example:
	```
	sqlplus lbrown_dvowner
	Enter password: password
	Connected.
	```
2. Enter the `ALTER SESSION SET EVENTS` SQL statement to set the tracing to low, high, or highest, as described in "Levels of Oracle Database Vault Trace Events".
	- To turn on tracing for failed operations that have a low impact, enter one of the following statements:
		```
		ALTER SESSION SET EVENTS 'TRACE[DV] DISK=LOW';
		ALTER SESSION SET EVENTS '47998 TRACE NAME CONTEXT FOREVER, LEVEL 1';
		```
		- To turn on tracing for both failed and successful operations that have a high impact, enter one of the following statements:
		```
		ALTER SESSION SET EVENTS 'TRACE[DV] DISK=HIGH';
		ALTER SESSION SET EVENTS '47998 TRACE NAME CONTEXT FOREVER, LEVEL 3';
		```
		- To turn on tracing for both failed and successful operations with a function and PL/SQL call stack that has the highest impact, enter one of the following statements:
		```
		ALTER SESSION SET EVENTS 'TRACE[DV] DISK=HIGHEST';
		ALTER SESSION SET EVENTS '47998 TRACE NAME CONTEXT FOREVER, LEVEL 4';
		```

#### Enabling Trace Events for All Database Sessions

1. Log into the database instance as a user who has been granted the `DV_ADMIN` role and the `ALTER SYSTEM` system privilege.
	For example:
	```
	sqlplus lbrown_dvowner
	Enter password: password
	Connected.
	```
2. Enter the `ALTER SYSTEM SET EVENTS` SQL statement, using the syntax that is shown in Step [^1] in "Enabling Trace Events for the Current Database Session".
	For example:
	```
	ALTER SYSTEM SET EVENTS 'TRACE[DV] DISK=LOW';
	```
3. Restart the database.
	For example:
	```
	SHUTDOWN IMMEDIATE
	STARTUP
	```

Another way that you can enable trace events for all database sessions is to add the following line to the `init.ora` file, and then restart the database:

```
event="47998 trace name context forever, level [trace_level]"
```

Replace `trace_level` with one of the following values:

- `1` for the lowest level of tracing
- `3` for the high level
- `4` for the highest level

For example:

```
event="47998 trace name context forever, level [1]"
```

### Finding Oracle Database Vault Trace File Data

This section contains:

- Finding the Database Vault Trace File Directory Location
- Using the Linux grep Command to Search Trace Files for Strings
- Using the ADR Command Interpreter (ADRCI) Utility to QueryTrace Files

#### Finding the Database Vault Trace File Directory Location

You can find the full directory location of trace files by querying the `V$DIAG_INFO` dynamic view.

For example:

```
SELECT VALUE FROM V$DIAG_INFO WHERE NAME = 'Default Trace File';

VALUE
--------------------------------------------------------------------------------
/u01/app/oracle/product/11.2.0.4/log/diag/rdbms/orcl/orcl/trace/orcl_ora_7174.trc
```

#### Using the Linux grep Command to Search Trace Files for Strings

To query or process the trace files, you can use the Linux `grep` command to search for strings. For example, to find the trace files that show realm authorization failures, enter the following command:

```
grep 'Result=Realm Authorization Failed'  *.trc
```

#### Using the ADR Command Interpreter (ADRCI) Utility to QueryTrace Files

Another way to query trace files is to use the ADR Command Interpreter (`ADRCI`) command-line utility. For example, to use `ADRCI` to find the trace files, enter the `SHOW TRACEFILE` command:

```
adrci --To start ACRCI from the command line
adrci> show tracefile

diag/rdbms/orcl/orcl/trace/orcl_m002_14551.trc
diag/rdbms/orcl/orcl/trace/orcl_tmon_13450.trc
diag/rdbms/orcl/orcl/trace/orcl_vktm_963.trc
diag/rdbms/orcl/orcl/trace/alert_orcl.log
...
```

To find the number of all trace incidents:

```
adrci> show incident

ADR Home = /u01/app/oracle/product/11.2.0.4/log/diag/rdbms/orcl/orcl:
*************************************************************************
234 rows fetched
```

The following `ADRCI` command returns a list of all trace files whose name contains the word `ora`:

```
adrci> show tracefile %ora%

/u01/app/oracle/product/11.2.0.4/log/diag/rdbms/orcl/orcl/trace/orcl_ora_18841.trc
/u01/app/oracle/product/11.2.0.4/log/diag/rdbms/orcl/orcl/trace/orcl_ora_12017.trc
/u01/app/oracle/product/11.2.0.4/log/diag/rdbms/orcl/orcl/trace/orcl_ora_19372.trc
/u01/app/oracle/product/11.2.0.4/log/diag/rdbms/orcl/orcl/trace/orcl_ora_12221.trc
/u01/app/oracle/product/11.2.0.4/log/diag/rdbms/orcl/orcl/trace/orcl_ora_1600.trc
...
```

The following `ADRCI` command searches for trace files that contain the phrase `Realm Authorization Failed`:

```
adrci> show trace %trc -xp "[payload like '%Realm Authorization Failed%']"
```

See Also:

- [Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/adrci.htm#SUTIL700) for detailed information about the `ADRCI` utility
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/diag.htm#ADMIN11277) for information about viewing reports with the `ADRCI` utility

### Examples Oracle Database Vault Trace Files

This section provides examples of trace files for all three levels: low, high, and highest.

Example E-1 shows trace file data for low level realm violations.

Example E-1 Low Level Oracle Database Vault Realm Violations in a Trace File

```
*** 2010-02-05 18:35:31.438
*** SESSION ID:(34.559) 2010-02-05 18:35:31.438
*** CLIENT ID:() 2010-02-05 18:35:31.438
*** SERVICE NAME:(SYS$USERS) 2010-02-05 18:35:31.438
*** MODULE NAME:(SQL*Plus) 2010-02-05 18:35:31.438
*** ACTION NAME:() 2010-02-05 18:35:31.438
 
Result=Realm Authorization Failed
        Realm_Name=realm 3      Required_Auth_Level=0
        Current_User=116
        Object_Owner=U1 Object_Name=T1  Object_Type=TABLE
        SQL_Text=INSERT INTO U1.T1 VALUES(30)
 
Result=Realm Authorization Failed
        Realm_Name=realm 3      Required_Auth_Level=0
        Current_User=116
        Object_Owner=U1 Object_Name=T1  Object_Type=TABLE
        SQL_Text=DELETE FROM U1.T1
 
Result=Realm Authorization Failed
        Realm_Name=realm 3      Required_Auth_Level=0
        Current_User=116
        Object_Owner=U1 Object_Name=T3  Object_Type=TABLE
        SQL_Text=CREATE TABLE U1.T3(C INT)
 
*** 2010-02-05 18:35:34.465
 
Result=Realm Authorization Failed
        Realm_Name=realm 3      Required_Auth_Level=0
        Current_User=116
        Object_Owner=U1 Object_Name=T1  Object_Type=TABLE
        SQL_Text=INSERT INTO U1.T1 VALUES(30)
 
Result=Realm Authorization Failed
        Realm_Name=realm 3      Required_Auth_Level=0
        Current_User=116
        Object_Owner=U1 Object_Name=T1  Object_Type=TABLE
        SQL_Text=DELETE FROM U1.T1
```

Example E-2 shows how Database Vault authorization can appear in a trace file with high level trace enabled.

Example E-2 High Level Trace Enabled for Oracle Database Vault Authorization

```
Result= Realm Authorization Passed
        Reason=Current user is the object owner
        Current_User=70 Command=SELECT
        Object_Owner=LBACSYS    Object_Name=LBAC$AUDIT  Object_Type=TABLE
 
Result= Realm Authorization Passed
        Reason=Current user is the object owner
        Current_User=70 Command=SELECT
        Object_Owner=LBACSYS    Object_Name=LBAC$AUDIT  Object_Type=TABLE
 
Result= Realm Authorization Passed
        Reason=Current user is the object owner
        Current_User=70 Command=SELECT
        Object_Owner=LBACSYS    Object_Name=LBAC$POL    Object_Type=TABLE
 
Result= Realm Authorization Passed
        Reason=Current user is the object owner
        Current_User=70 Command=SELECT
        Object_Owner=LBACSYS    Object_Name=LBAC$USER_LOGON     Object_Type=VIEW
 
……
 
Result= Realm Authorization Passed
        Reason=Current user is the object owner
        Current_User=70 Command=SELECT
        Object_Owner=LBACSYS    Object_Name=LBAC$POL    Object_Type=TABLE
 
Result=Set Factor Value
        Factor_Name=Sensitive_Treatments        Factor_Expression=/SURGERY/PSYCHOLOGICAL
 
Result=Set Factor Value
        Factor_Name=Database_Instance   Factor_Expression=UPPER(SYS_CONTEXT('USERENV','INSTANCE'))      Factor_Value=1
 
Result=Set Factor Value
        Factor_Name=Client_IP   Factor_Expression=UPPER(SYS_CONTEXT('USERENV','IP_ADDRESS'))    Factor_Value=
 
Result=Set Factor Value
        Factor_Name=Authentication_Method       Factor_Expression=UPPER(SYS_CONTEXT('USERENV','AUTHENTICATION_METHOD')) Factor_Value=PASSWORD
……
 
*** ACTION NAME:() 2010-02-05 18:47:19.540
 
Result=Rule Set Evaluation Failed
        Command=SELECT  RuleSet_ID=2    RuleSet_Name=Disabled
        Current_User=SYSTEM 
        Object_Owner=U1 Object_Name=T1  Object_Type=TABLE
        SQL_Text=SELECT * FROM U1.T1
 
Result=Rule Set Evaluation Succeeded
        Command=SELECT  RuleSet_ID=1    RuleSet_Name=Enabled
        Current_User=SYSTEM 
        Object_Owner=U1 Object_Name=T1  Object_Type=TABLE
        SQL_Text=SELECT * FROM U1.T1
```

Example E-3 shows how highest level violations that involve Oracle Scheduler jobs authorization can appear in a trace file when trace is enabled at the highest level.

Example E-3 Highest Level Traces on Violations on Realm-Protected Objects

```
------ Call Stack Trace ------
kzvdvechk<-kzvdveqau<-kksfbc<-opiexe<-kpoal8<-opiodr<-ttcpip<-opitsk<-opiino<-opiodr<-opidrv<-sou2o<-opimai_real<-ssthrdmain<-main<-__libc_start_main<-_start
 
Result=Object Privilege check passed
        Current_User=INVOKER2   Used_Role=1
        Object_Owner=SYSTEM     Object_Name=PRODUCT_PRIVS       Object_Type=VIEW
        SQL_Text=SELECT CHAR_VALUE FROM SYSTEM.PRODUCT_PRIVS WHERE (UPPER('SQL*PLUS') LIKE UPPER(PRODUCT)) AND ((USER LIKE USERID) OR (USERID = 'PUBLIC')) AND (UPPER(ATTRIBUTE) = 'ROLES')
*** MODULE NAME:(SQL*Plus) 2010-02-05 18:57:53.973
*** ACTION NAME:() 2010-02-05 18:57:53.973
 
----- Current SQL Statement for this session (sql_id=2sr63rjm45yfh) -----
UPDATE INVOKER1.T1 SET A = 20
----- PL/SQL Stack -----
----- PL/SQL Call Stack -----
  object      line  object
  handle    number  name
0x26a00e34         1  anonymous block
0x2495b000       185  package body SYS.DBMS_ISCHED
0x24958fb8       486  package body SYS.DBMS_SCHEDULER
0x247bbb34         1  anonymous block
 
------ Call Stack Trace ------
kzvdvechk<-kzvdveqau<-kksfbc<-opiexe<-opipls<-opiodr<-__PGOSF151_rpidrus<-skgmstack<-rpidru<-rpiswu2<-rpidrv<-psddr0<-psdnal<-pevm_EXECC<-pfrinstr_EXECC<-pfrrun_no_tool<-pfrrun<-plsql_run<-peicnt<-kkxexe<-opiexe<-kpoal8<-opiodr<-kpoodr<-upirtrc<-kpurcsc<-kpuexec
<-OCIStmtExecute<-jslvec_execcb<-jslvswu<-jslve_execute0<-jskaJobRun<-jsiRunJob<-jsaRunJob<-spefcmpa<-spefmccallstd<-pextproc<-__PGOSF495_peftrusted<-__PGOSF522_psdexsp<-rpiswu2<-psdextp<-pefccal<-pefcal<-pevm_FCAL<-pfrinstr_FCAL<-pfrrun_no_tool<-pfrrun<-plsql_run
<-peicnt<-kkxexe<-opiexe<-kpoal8<-opiodr<-ttcpip<-opitsk<-opiino<-opiodr<-opidrv<-sou2o<-opimai_real<-ssthrdmain<-main<-__libc_start_main<-_start
 
Result=Realm Authorization Succeeded
        Realm_Name=jobowner realm       Used_Auth_Level=0
        Current_User=119
        Object_Owner=INVOKER1   Object_Name=T1  Object_Type=TABLE
        SQL_Text=UPDATE INVOKER1.T1 SET A = 20
 
Result=Scheduler Job Authorization Succeeded
        Current_User=JOBOWNER   Logon_User=INVOKER2
        Job_Owner=JOBOWNER      Job_Name=DMLJOB1
        Object_Owner=INVOKER1   Object_Name=T1  Object_Type=TABLE
        SQL_Text=UPDATE INVOKER1.T1 SET A = 20
```

### Disabling Oracle Database Vault Trace Events

This section contains:

- Disabling Trace Events for the Current Database Session
- Disabling Trace Events for All Database Sessions

#### Disabling Trace Events for the Current Database Session

1. Log into the database instance as a user who has been granted the `DV_ADMIN` role and the `ALTER SESSION` system privilege.
	For example:
	```
	sqlplus lbrown_dvowner
	Enter password: password
	Connected.
	```
2. Enter both of the following SQL statements to disable tracing:
	```
	ALTER SESSION SET EVENTS 'TRACE[DV] OFF'; 
	ALTER SESSION SET EVENTS '47998 trace name context off';
	```
	Alternatively, you can use the `ALTER SYSTEM` statement as well:
	```
	ALTER SYSTEM SET EVENTS 'TRACE[DV] OFF'; 
	ALTER SYSTEM SET EVENTS '47998 trace name context off';
	```

#### Disabling Trace Events for All Database Sessions

1. Log into the database instance as a user who has been granted the `DV_ADMIN` role and the `ALTER SYSTEM` system privilege.
	For example:
	```
	sqlplus lbrown_dvowner
	Enter password: password
	Connected.
	```
2. Enter the `ALTER SYSTEM SET EVENTS` SQL statement, using the syntax that is shown in Step [^2] in "Disabling Trace Events for the Current Database Session".
	For example:
	```
	ALTER SYSTEM SET EVENTS 'TRACE[DV] OFF';
	```
3. Restart the database.
	For example:
	```
	SHUTDOWN IMMEDIATE
	STARTUP
	```

Another way that you can disable trace events for all database sessions is to add the following line to the `init.ora` file, and then restart the database:

```
event="47998 trace name context off"
```

Ensure that the `init.ora` file does not have any conflicting `47998` lines, such as `event="47998 trace name context forever, level [1]"`.

## General Diagnostic Tips

Follow these general tips for diagnosing problems in realms, factors, and rule sets:

- For realm protections, verify that a user has the underlying system or object privileges (granted directly or through a role) that might affect the command.
- If a realm authorization is not working, verify that the account roles are set correctly.
- For PL/SQL expressions used in factors and rule sets, grant the `EXECUTE` privilege on the PL/SQL package functions used in these expressions directly to the account and determine if the results appear to be correct.
- Use the auditing reports to diagnose problems in general. See ["Oracle Database Vault Auditing Reports"](reports.md) for more information.

## Configuration Problems with Oracle Database Vault Components

If you suspect problems with the configuration of realms, command rules, factors, rule sets, or secure application roles, you can run the appropriate configuration report. See the following sections for more information:

- ["Command Rule Configuration Issues Report"](reports.md)
- ["Factor Configuration Issues Report"](reports.md)
- ["Factor Without Identities Report"](reports.md)
- ["Identity Configuration Issues Report"](reports.md)
- ["Realm Authorization Configuration Issues Report"](reports.md)
- ["Rule Set Configuration Issues Report"](reports.md)
- ["Secure Application Configuration Issues Report"](reports.md)

To run these reports, see ["How to Run Oracle Database Vault Reports"](reports.md).

[^1]: Enter the `ALTER SESSION SET EVENTS` SQL statement to set the tracing to low, high, or highest, as described in "Levels of Oracle Database Vault Trace Events".

- To turn on tracing for failed operations that have a low impact, enter one of the following statements:
	```
	ALTER SESSION SET EVENTS 'TRACE[DV] DISK=LOW';
	ALTER SESSION SET EVENTS '47998 TRACE NAME CONTEXT FOREVER, LEVEL 1';
	```
- To turn on tracing for both failed and successful operations that have a high impact, enter one of the following statements:
	```
	ALTER SESSION SET EVENTS 'TRACE[DV] DISK=HIGH';
	ALTER SESSION SET EVENTS '47998 TRACE NAME CONTEXT FOREVER, LEVEL 3';
	```
- To turn on tracing for both failed and successful operations with a function and PL/SQL call stack that has the highest impact, enter one of the following statements:
	```
	ALTER SESSION SET EVENTS 'TRACE[DV] DISK=HIGHEST';
	ALTER SESSION SET EVENTS '47998 TRACE NAME CONTEXT FOREVER, LEVEL 4';
	```

[^2]: Enter both of the following SQL statements to disable tracing:

```
ALTER SESSION SET EVENTS 'TRACE[DV] OFF'; 
ALTER SESSION SET EVENTS '47998 trace name context off';
```

Alternatively, you can use the `ALTER SYSTEM` statement as well:

```
ALTER SYSTEM SET EVENTS 'TRACE[DV] OFF'; 
ALTER SYSTEM SET EVENTS '47998 trace name context off';
```