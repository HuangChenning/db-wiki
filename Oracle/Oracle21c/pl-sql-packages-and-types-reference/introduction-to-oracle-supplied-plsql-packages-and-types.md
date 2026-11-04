---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/introduction-to-oracle-supplied-plsql-packages-and-types.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 1 Introduction to Oracle Supplied PL/SQL Packages & Types

Oracle supplies many PL/SQL packages with the Oracle server to extend database functionality and provide PL/SQL access to SQL features. You can use the supplied packages when creating your applications or for ideas in creating your own stored procedures.

This manual covers the packages provided with the Oracle database server. Packages supplied with other products, such as Oracle Developer or the Oracle Application Server, are not covered.

Note that not every package or type described in this manual or elsewhere in the Oracle Database Documentation Library is installed by default. In such cases, the documentation states this and explains how to install the object. Run this query as a suitably privileged user:

```
SELECT DISTINCT Owner, Object_Type, Object_Name FROM DBA_Objects_AE
     WHERE Owner IN (
       'SYS', 'OUTLN', 'SYSTEM', 'CTXSYS', 'DBSNMP',
       'LOGSTDBY_ADMINISTRATOR', 'ORDSYS',
       'ORDPLUGINS', 'OEM_MONITOR', 'MDSYS', 'LBACSYS', 
       'DMSYS', 'WMSYS', 'OLAPDBA', 'OLAPSVR', 'OLAP_USER',
       'OLAPSYS', 'EXFSYS', 'SYSMAN', 'MDDATA',
       'SI_INFORMTN_SCHEMA', 'XDB', 'ODM')
     AND Object_Type IN ('PACKAGE', 'TYPE')
     ORDER BY Owner, Object_Type, Object_Name
```

This lists every Oracle-supplied package and type that is currently installed in the database. Note that it lists a number of objects not mentioned in the Oracle Database Documentation Library. This is deliberate. Some of the Oracle-supplied packages and types are intended to be used only by other Oracle-supplied components. Any package or type that is not described in the Oracle Database Documentation Library is not supported for direct customer use.

This chapter contains the following topics:

- Package Overview
- Summary of Oracle Supplied PL/SQL Packages and Types
	See Also:
	[Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS-GUID-C0141D00-57EA-4957-9270-CCA83EE82C95) for information on how to create your own packages

### 1.1 Package Overview

A package is an encapsulated collection of related program objects stored together in the database. Program objects are procedures, functions, variables, constants, cursors, and exceptions.

#### 1.1.1 Package Components

PL/SQL packages have two parts: the specification and the body, although sometimes the body is unnecessary. The specification is the interface to your application; it declares the types, variables, constants, exceptions, cursors, and subprograms available for use. The body fully defines cursors and subprograms, and so implements the specification.

Unlike subprograms, packages cannot be called, parameterized, or nested. However, the formats of a package and a subprogram are similar:

```
CREATE PACKAGE name AS  -- specification (visible part)
   -- public type and item declarations
   -- subprogram specifications
END [name];

CREATE PACKAGE BODY name AS  -- body (hidden part)
   -- private type and item declarations
   -- subprogram bodies
[BEGIN
   -- initialization statements]
END [name];
```

The specification holds public declarations that are visible to your application. The body holds implementation details and private declarations that are hidden from your application. You can debug, enhance, or replace a package body without changing the specification. You can change a package body without recompiling calling programs because the implementation details in the body are hidden from your application.

#### 1.1.2 Using Oracle Supplied Packages

Most Oracle supplied packages are automatically installed when the database is created. Certain packages are not installed automatically. Special installation instructions for these packages are documented in the individual chapters.

To call a PL/SQL function from SQL, you must either own the function or have `EXECUTE` privileges on the function. To select from a view defined with a PL/SQL function, you must have `SELECT` privileges on the view. No separate `EXECUTE` privileges are needed to select from the view. Instructions on special requirements for packages are documented in the individual chapters.

#### 1.1.3 Creating New Packages

To create packages and store them permanently in an Oracle database, use the `CREATE` `PACKAGE` and `CREATE` `PACKAGE` `BODY` statements. You can execute these statements interactively from SQL\*Plus or Enterprise Manager.

To create a new package, do the following:

1. Create the package specification with the `CREATE` `PACKAGE` statement.
	You can declare program objects in the package specification. Such objects are called public objects. Public objects can be referenced outside the package, as well as by other objects in the package.
	Note:
	It is often more convenient to add the `OR` `REPLACE` clause in the `CREATE` `PACKAGE` statement. But note that `CREATE` `PACKAGE` warns you if you are about to overwrite an existing package with the same name while `CREATE` `OR` `REPLACE` `just` overwrites it with no warning.
2. Create the package body with the `CREATE` `PACKAGE` `BODY` statement.
	You can declare and define program objects in the package body.
	- You must define public objects declared in the package specification.
		- You can declare and define additional package objects, called private objects. Private objects are declared in the package body rather than in the package specification, so they can be referenced only by other objects in the package. They cannot be referenced outside the package.
		See Also:
		- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=LNPLS-GUID-C285EC5A-BE50-4192-A88E-48C0778B34E0)
		- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADFNS-GUID-C0141D00-57EA-4957-9270-CCA83EE82C95) for more information on creating new packages
		- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=CNCPT-GUID-6B5D98B7-A25D-4187-B3A9-43629E214635)
		for more information on storing and executing packages

##### 1.1.3.1 Separating the Specification and Body

The specification of a package declares the public types, variables, constants, and subprograms that are visible outside the immediate scope of the package. The body of a package defines the objects declared in the specification, as well as private objects that are not visible to applications outside the package.

Oracle stores the specification and body of a package separately in the database. Other schema objects that call or reference public program objects depend only on the package specification, not on the package body. Using this distinction, you can change the definition of a program object in the package body without causing Oracle to invalidate other schema objects that call or reference the program object. Oracle invalidates dependent schema objects only if you change the declaration of the program object in the package specification.

###### 1.1.3.1.1 Creating a New Package: Example

The following example shows a package specification for a package named `EMPLOYEE_MANAGEMENT`. The package contains one stored function and two stored procedures.

```
CREATE PACKAGE employee_management AS
   FUNCTION hire_emp (name VARCHAR2, job VARCHAR2,
      mgr NUMBER, hiredate DATE, sal NUMBER, comm NUMBER,
      deptno NUMBER) RETURN NUMBER;
   PROCEDURE fire_emp (emp_id NUMBER);
   PROCEDURE sal_raise (emp_id NUMBER, sal_incr NUMBER);
END employee_management;
```

The body for this package defines the function and the procedures:

```
CREATE PACKAGE BODY employee_management AS
   FUNCTION hire_emp (name VARCHAR2, job VARCHAR2,
      mgr NUMBER, hiredate DATE, sal NUMBER, comm NUMBER,
      deptno NUMBER) RETURN NUMBER IS
```

The function accepts all arguments for the fields in the employee table except for the employee number. A value for this field is supplied by a sequence. The function returns the sequence number generated by the call to this function.

```
new_empno    NUMBER(10);

BEGIN
   SELECT emp_sequence.NEXTVAL INTO new_empno FROM dual;
   INSERT INTO emp VALUES (new_empno, name, job, mgr,
      hiredate, sal, comm, deptno);
   RETURN (new_empno);
END hire_emp;

PROCEDURE fire_emp(emp_id IN NUMBER) AS
```

The procedure deletes the employee with an employee number that corresponds to the argument `emp_id`. If no employee is found, then an exception is raised.

```
BEGIN
      DELETE FROM emp WHERE empno = emp_id;
      IF SQL%NOTFOUND THEN
      raise_application_error(-20011, 'Invalid Employee
         Number: ' || TO_CHAR(emp_id));
   END IF;
END fire_emp;

PROCEDURE sal_raise (emp_id IN NUMBER, sal_incr IN NUMBER) AS
```

The procedure accepts two arguments. `Emp_id` is a number that corresponds to an employee number. `Sal_incr` is the amount by which to increase the employee's salary.

```
BEGIN

   -- If employee exists, then update salary with increase.
   
      UPDATE emp
         SET sal = sal + sal_incr
         WHERE empno = emp_id;
      IF SQL%NOTFOUND THEN
         raise_application_error(-20011, 'Invalid Employee
            Number: ' || TO_CHAR(emp_id));
      END IF;
   END sal_raise;
END employee_management;
```

Note:

If you want to try this example, then first create the sequence number `emp_sequence`. You can do this using the following SQL\*Plus statement:

```
SQL> CREATE SEQUENCE emp_sequence
   > START WITH 8000 INCREMENT BY 10;
```

#### 1.1.4 Referencing Package Contents

When you want to reference the types, items, and subprograms declared in a package specification, use the dot notation.

For example:

```
package_name.type_name
package_name.item_name
package_name.subprogram_name
```

### 1.2 Summary of Oracle Supplied PL/SQL Packages and Types

PL/SQL packages are supplied with the Oracle server that extend database functionality and provide PL/SQL access to SQL features.

These packages, listed in the following table, run as the invoking user, rather than the package owner. Unless otherwise noted, the packages are callable through public synonyms of the same name.

Note:

- The procedures and functions provided in these packages and their external interfaces are reserved by Oracle and are subject to change.
- Modifying Oracle supplied packages can cause internal errors and database security violations. Do not modify supplied packages.

Table 1-1 Summary of Oracle Supplied PL/SQL Packages

| Package Name | Description |
| --- | --- |
| `APEX_APPLICATION ` through `APEX_ZIP` | For a complete description of all the packages that ship with Oracle Application Express, see [Oracle Application Express API Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=AEAPI538) |
| `CTX_ADM` | Lets you administer servers and the data dictionary |
| `CTX_ANL` | The `CTX_ANL` package is used with `AUTO_LEXER` and provides procedures for adding and dropping a custom dictionary from the lexer. |
| `CTX_CLS` | Lets you generate `CTXRULE` rules for a set of documents |
| `CTX_DDL` | Lets you create and manage the preferences, section lists and stopgroups required for Text indexes |
| `CTX_DOC` | Lets you request document services |
| `CTX_ENTITY` | The `CTX_ENTITY` package enables you to search for terms that are unknown to you without specifying a particular search text. |
| `CTX_OUTPUT` | Lets you manage the index log |
| `CTX_QUERY` | Lets you generate query feedback, count hits, and create stored query expressions |
| `CTX_REPORT` | Lets you create various index reports |
| `CTX_THES` | Lets you to manage and browse thesauri |
| `CTX_ULEXER` | For use with the user-lexer |
| `DBMS_ADDM` | Facilitates the use of Advisor functionality regarding the Automatic Database Diagnostic Monitor |
| `DBMS_ADVANCED_REWRITE` | Contains interfaces for advanced query rewrite users to create, drop, and maintain functional equivalence declarations for query rewrite |
| `DBMS_ADVISOR` | Part of the SQLAccess Advisor, an expert system that identifies and helps resolve performance problems relating to the execution of SQL statements |
| `DBMS_ALERT` | Provides support for the asynchronous notification of database events |
| `DBMS_APP_CONT` | The `DBMS_APP_CONT` package provides an interface to determine if the in-flight transaction on a now unavailable session committed or not, and if the last call on that session completed or not. |
| `DBMS_APP_CONT_ADMIN` | This package provides a collection dba level admin operations in relation to Application Continuity. |
| `DBMS_APPLICATION_INFO` | Lets you register an application name with the database for auditing or performance tracking purposes |
| `DBMS_APPLY_ADM` | Provides administrative procedures to start, stop, and configure an apply process |
| `DBMS_AQ` | Lets you add a message (of a predefined object type) onto a queue or to dequeue a message |
| `DBMS_AQADM` | Lets you perform administrative functions on a queue or queue table for messages of a predefined object type |
| `DBMS_AQELM` | Provides procedures to manage the configuration of Advanced Queuing asynchronous notification by e-mail and HTTP |
| `DBMS_AQIN` | Plays a part in providing secure access to the Oracle JMS interfaces |
| `DBMS_ASSERT` | Provides an interface to validate properties of the input value |
| `DBMS_AUDIT_UTIL` | The `DBMS_AUDIT_UTIL` package provides functions that enable you to format the output of queries to the `DBA_FGA_AUDIT_TRAIL`, `DBA_AUDIT_TRAIL`, `UNIFIED_AUDIT_TRAIL`, and `V$XML_AUDIT_TRAIL` views. |
| `DBMS_AUDIT_MGMT` | The `DBMS_AUDIT_MGMT` package provides subprograms to manage audit trail records. These subprograms enable audit administrators to manage the audit trail. |
| `DBMS_AUTO_REPORT` | The `DBMS_AUTO_REPORT` package provides an interface to view SQL Monitoring and Real-time Automatic Database Diagnostic Monitor (ADDM) data that has been captured into Automatic Workload Repository (AWR). It also provides subprograms to control the behavior of how these data are captured to AWR. |
| `DBMS_AUTO_SQLTUNE` | The `DBMS_AUTO_SQLTUNE` package is the interface for managing the Automatic SQL Tuning task. |
| `DBMS_AUTO_TASK_ADMIN` | Used by the DBA as well as Enterprise Manager to access the `AUTOTASK` controls |
| `DBMS_AW_STATS` | Contains a subprogram that generates and stores optimizer statistics for cubes and dimensions |
| `DBMS_BLOCKCHAIN_TABLE` | A blockchain table is an append-only table designed for centralized blockchain applications. |
| `DBMS_CAPTURE_ADM` | Describes administrative procedures to start, stop, and configure a capture process; used in Replication |
| `DBMS_COMPARISON` | Provides interfaces to compare and converge database objects at different databases |
| `DBMS_COMPRESSION` | Provides an interface to facilitate choosing the correct compression level for an application |
| `DBMS_CONNECTION_POOL` | Provides an interface to manage the Database Resident Connection Pool |
| `DBMS_CQ_NOTIFICATION` | Is part of a set of features that clients use to receive notifications when result sets of a query have changed. The package contains interfaces that can be used by mid-tier clients to register objects and specify delivery mechanisms. |
| `DBMS_CREDENTIAL` | The `DBMS_CREDENTIAL` package provides an interface for authenticating and impersonating `EXTPROC` callout functions, as well as external jobs, remote jobs and file watchers from the `SCHEDULER`. |
| `DBMS_CRYPTO` | Lets you encrypt and decrypt stored data, can be used in conjunction with PL/SQL programs running network communications, and supports encryption and hashing algorithms |
| `DBMS_CSX_ADMIN` | Provides an interface to customize the setup when transporting a tablespace containing binary XML data |
| `DBMS_CUBE` | Contains subprograms that create OLAP cubes and dimensions, and that load and process the data for querying |
| `DBMS_CUBE_ADVISE` | Contains subprograms for evaluating cube materialized views to support log-based fast refresh and query rewrite |
| `DBMS_CUBE_LOG` | `DBMS_CUBE_LOG` contains subprograms for creating and managing logs for cubes and cube dimensions. |
| `DBMS_DATA_MINING` | Implements the Oracle Data Mining interface for creating, evaluating, and managing mining models |
| `DBMS_DATA_MINING_TRANSFORM` | Provides subroutines that can be used to prepare data for Oracle Data Mining |
| `DBMS_DATAPUMP` | Lets you move all, or part of, a database between databases, including both data and metadata |
| `DBMS_DB_VERSION` | The `DBMS_DB_VERSION` package specifies the Oracle version numbers and other information useful for simple conditional compilation selections based on Oracle versions. |
| `DBMS_DBCOMP` | The `DBMS_DBCOMP` package performs block comparison to detect lost writes or database inconsistencies between a primary database and one or more physical standby databases. |
| `DBMS_DBFS_CONTENT` | Provides an interface comprising a file system-like abstraction backed by one or more Store Providers |
| `DBMS_DBFS_CONTENT_SPI` | Provides the Application Programming Interface (API) specification for `DBMS_DBFS_CONTENT` service providers |
| `DBMS_DBFS_HS` | Provides users the ability to use tape or Amazon S3 Web service as a storage tier when doing Information Lifecycle Management for their database tables |
| `DBMS_DBFS_SFS` | Provides an interface to operate a SecureFile-based store (SFS) for the content interface described in the `DBMS_DBFS_CONTENT` package |
| `DBMS_DDL` | Provides access to some SQL DDL statements from stored procedures, and provides special administration operations not available as DDLs |
| `DBMS_DEBUG` | Implements server-side debuggers and provides a way to debug server-side PL/SQL program units |
| `DBMS_DEBUG_JDWP` | The `DBMS_DEBUG_JDWP` provides the interface to initiate and control the debugging of PL/SQL stored procedures and Java stored procedures over Java Debug Wire Protocol (JDWP). |
| `DBMS_DEBUG_JDWP_CUSTOM` | The `DBMS_DEBUG_JDWP_CUSTOM` package is a PL/SQL package that provides database users a means to perform custom handling of a debug connection request of a database session to a debugger using the Java Debug Wire Protocol (JDWP). |
| `DBMS_DESCRIBE` | Describes the arguments of a stored procedure with full name translation and security checking |
| `DBMS_DG` | Allows applications to notify the primary database in an Oracle Data Guard broker environment to initiate a fast-start failover when the application encounters a condition that warrants a failover |
| `DBMS_DIMENSION` | Enables you to verify dimension relationships and provides an alternative to the Enterprise Manager Dimension Wizard for displaying a dimension definition |
| `DBMS_DISTRIBUTED_TRUST_ADMIN` | Maintains the Trusted Database List, which is used to determine if a privileged database link from a particular server can be accepted |
| `DBMS_DNFS` | The `DBMS_DNFS` package provides an interface to assists in creating a database using files in the backup set. |
| `DBMS_DST` | The `DBMS_DST` package provides an interface to apply the Daylight Saving Time (DST) patch to the Timestamp with Time Zone datatype. |
| `DBMS_EDITIONS_UTILITIES` | The `DBMS_EDITIONS_UTILITIES` package provides helper functions for edition related operations. |
| `DBMS_EPG` | Implements the embedded PL/SQL gateway that enables a Web browser to invoke a PL/SQL stored procedure through an HTTP listener |
| `DBMS_ERRLOG` | Provides a procedure that enables you to create an error logging table so that DML operations can continue after encountering errors rather than abort and roll back |
| `DBMS_FGA` | Provides fine-grained security functions |
| `DBMS_FILE_GROUP` | One of a set of Streams packages, provides administrative interfaces for managing file groups, file group versions, files and file group repositories |
| `DBMS_FILE_TRANSFER` | Lets you copy a binary file within a database or to transfer a binary file between databases |
| `DBMS_FLASHBACK` | Lets you flash back to a version of the database at a specified wall-clock time or a specified system change number (SCN) |
| `DBMS_FLASHBACK_ARCHIVE` | Contains procedures for disassociation and re-association of a Flashback Data Archive (FDA) enabled table from/with its underlying FDA respectively. |
| `DBMS_FREQUENT_ITEMSET` | Enables frequent itemset counting |
| `DBMS_FS` | The `DBMS_FS` package for performing operations on an Oracle file system (make, mount, unmount and destroy operations) in an Oracle database. |
| `DBMS_GOLDENGATE_AUTH` | The `DBMS_GOLDENGATE_AUTH` package provides subprograms for granting privileges to and revoking privileges from GoldenGate administrators. |
| `DBMS_HADOOP` | The `DBMS_HADOOP` package provides a PL/SQL procedure called `CREATE_EXTDDL_FOR_HIVE()`, that creates an Oracle external table for a given hive table. |
| `DBMS_HANG_MANAGER` | The `DBMS_HANG_MANAGER` package provides a method of changing some Hang Manager configuration parameters. |
| `DBMS_HEAT_MAP` | The `DBMS_HEAT_MAP` package provides an interface to externalize heatmaps at various levels of storage including block, extent, segment, object and tablespace. |
| `DBMS_HIERARCHY` | Contains functions and procedures for validating the data in tables used by analytic views and hierarchies and for creating a log table. |
| `DBMS_HM` | Contains constants and procedure declarations for health check management |
| `DBMS_HPROF` | Provides an interface for profiling the execution of PL/SQL applications |
| `DBMS_HS_PARALLEL` | Enables parallel processing for heterogeneous targets access |
| `DBMS_HS_PASSTHROUGH` | Lets you use Heterogeneous Services to send pass-through SQL statements to non-Oracle systems |
| `DBMS_ILM` | The `DBMS_ILM` package provides an interface for implementing Information Lifecycle Management (ILM) strategies using Automatic Data Optimization (ADO) policies. |
| `DBMS_ILM_ADMIN` | The `DBMS_ILM_ADMIN` package provides an interface to customize Automatic Data Optimization (ADO) policy execution. |
| `DBMS_INMEMORY` | The `DBMS_INMEMORY` package provides an interface for In-Memory Column Store (IM column store) functionality. |
| `DBMS_INMEMORY_ADMIN` | The `DBMS_INMEMORY_ADMIN` package provides interfaces for managing an In-Memory FastStart (IM FastStart) area and In-Memory Expressions (IM expressions). |
| `DBMS_IOT` | Creates a table into which references to the chained rows for an Index Organized Table can be placed using the `ANALYZE` command |
| `DBMS_JAVA` | Provides a PL/SQL interface for accessing database functionality from Java |
| `DBMS_JOB` | Schedules and manages jobs in the job queue (Deprecated) |
| `DBMS_JSON` | Provides an interface for data-guide operations |
| `DBMS_LDAP` | Provides functions and procedures to access data from LDAP servers |
| `DBMS_LDAP_UTL` | Provides the Oracle Extension utility functions for LDAP |
| `DBMS_LIBCACHE` | Prepares the library cache on an Oracle instance by extracting SQL and PL/SQL from a remote instance and compiling this SQL locally without execution |
| `DBMS_LOB` | Provides general purpose routines for operations on Oracle Large Object (`LOB` s) datatypes - `BLOB`, `CLOB` (read/write), and `BFILE` s (read-only) |
| `DBMS_LOCK` | Lets you request, convert and release locks through Oracle Lock Management services |
| `DBMS_LOGMNR` | Provides functions to initialize and run the log reader |
| `DBMS_LOGMNR_D` | Queries the dictionary tables of the current database, and creates a text based file containing their contents |
| `DBMS_LOGSTDBY` | Describes procedures for configuring and managing the logical standby database environment |
| `DBMS_LOGSTDBY_CONTEXT` | You can use the procedures provided in the `DBMS_LOGSTDBY_CONTEXT` package to set and retrieve various parameters associated with `LSBY_APPLY_CONTEXT`. |
| `DBMS_METADATA` | Lets callers easily retrieve complete database object definitions (metadata) from the dictionary |
| `DBMS_METADATA_DIFF` | Contains the interfaces for comparing two metadata documents in SXML format. The result of the comparison is an SXML difference document. This document can be converted to other formats using the `DBMS_METADATA` submit interface and the `CONVERT` API. |
| `DBMS_MGD_ID_UTL` | Provides a set of utility subprograms |
| `DBMS_MGWADM` | Describes the Messaging Gateway administrative interface; used in Advanced Queuing |
| `DBMS_MGWMSG` | Describes object types (used by the canonical message types to convert message bodies) and helper methods, constants, and subprograms for working with the Messaging Gateway message types; used in Advanced Queuing. |
| `DBMS_MLE` | The `DBMS_MLE` package allows users to execute JavaScript code inside the Oracle Database and exchange data seamlessly between PL/SQL and JavaScript. |
| `DBMS_MONITOR` | Let you use PL/SQL for controlling additional tracing and statistics gathering |
| `DBMS_MVIEW` | Lets you refresh snapshots that are not part of the same refresh group and purge logs. `DBMS_SNAPSHOT` is a synonym. |
| `DBMS_MVIEW_STATS` | The `DBMS_MVIEW_STATS` package provides an interface to manage the collection and retention of statistics for materialized view refresh operations. |
| `DBMS_NETWORK_ACL_ADMIN` | Provides the interface to administer the network Access Control List (ACL) |
| `DBMS_NETWORK_ACL_UTILITY` | The `DBMS_NETWORK_ACL_UTILITY` package provides the utility functions to facilitate the evaluation of access control list (ACL) assignments governing TCP connections to network hosts. |
| `DBMS_ODCI` | Returns the CPU cost of a user function based on the elapsed time of the function |
| `DBMS_OPTIM_BUNDLE` | This package is used to manage the installed but disabled module bug fixes that cause an execution plan change. |
| `DBMS_OUTLN` | Provides the interface for procedures and functions associated with management of stored outlines Synonymous with `OUTLN_PKG` |
| `DBMS_OUTPUT` | Accumulates information in a buffer so that it can be retrieved later |
| `DBMS_PARALLEL_EXECUTE` | Enables the user to incrementally update table data in parallel |
| `DBMS_PART` | The `DBMS_PART` package provides an interface for maintenance and management operations on partitioned objects. |
| `DBMS_PCLXUTIL` | Provides intra-partition parallelism for creating partition-wise local indexes |
| `DBMS_PDB` | The `DBMS_PDB` package provides an interface to examine and manipulate data about pluggable databases (PDBs) in a multitenant container database (CDB). It also contains an interface specify which database objects are application common objects. |
| `DBMS_PDB_ALTER_SHARING` | In an application container with a pre-installed application, the `DBMS_PDB_ALTER_SHARING` package provides an interface to set database objects as application common objects or to specify that a database object is not an application common object. |
| `DBMS_PERF` | The `DBMS_PERF` package provides and interface to generate active reports for monitoring database performance. |
| `DBMS_PIPE` | Provides a DBMS pipe service which enables messages to be sent between sessions |
| `DBMS_PLSQL_CODE_COVERAGE` | The `DBMS_PLSQL_CODE_COVERAGE` package provides an interface for the collection of code coverage data of PL/SQL applications at the basic block level. |
| `DBMS_PREDICTIVE_ANALYTICS` | Provides subroutines that implement automatic data mining operations for predict, explain, and profile |
| `DBMS_PREPROCESSOR` | Provides an interface to print or retrieve the source text of a PL/SQL unit in its post-processed form |
| `DBMS_PRIVILEGE_CAPTURE` | The `DBMS_PRIVILEGE_CAPTURE` package provides an interface to database privilege analysis. |
| `DBMS_PROCESS` | The `DBMS_PROCESS` package provides an interface to manage the prespawned servers. |
| `DBMS_PROFILER` | Provides a Probe Profiler API to profile existing PL/SQL applications and identify performance bottlenecks |
| `DBMS_PROPAGATION_ADM` | Provides administrative procedures for configuring propagation from a source queue to a destination queue |
| `DBMS_QOPATCH` | The `DBMS_QOPATCH` package provides an interface to view the installed database patches. |
| `DBMS_RANDOM ` | Provides a built-in random number generator |
| `DBMS_REDACT` | The `DBMS_REDACT` package provides an interface to Oracle Data Redaction, which enables you to mask (redact) data that is returned from queries issued by lowprivileged users or an application. |
| `DBMS_REDEFINITION` | Lets you perform an online reorganization of tables |
| `DBMS_REFRESH` | Lets you create groups of snapshots that can be refreshed together to a transactionally consistent point in time Requires the Distributed Option |
| `DBMS_REPAIR` | Provides data corruption repair procedures |
| `DBMS_RESCONFIG` | Provides an interface to operate on the Resource Configuration List, and to retrieve listener information for a resource |
| `DBMS_RESOURCE_MANAGER` | Maintains plans, consumer groups, and plan directives; it also provides semantics so that you may group together changes to the plan schema |
| `DBMS_RESOURCE_MANAGER_PRIVS` | Maintains privileges associated with resource consumer groups |
| `DBMS_RESULT_CACHE` | Provides an interface to operate on the Result Cache |
| `DBMS_RESUMABLE` | Lets you suspend large operations that run out of space or reach space limits after executing for a long time, fix the problem, and make the statement resume execution |
| `DBMS_RLS` | Provides row level security administrative interface |
| `DBMS_ROLLING` | The `DBMS_ROLLING PL/SQL` package is used to implement the Rolling Upgrade Using Active Data Guard feature, which streamlines the process of upgrading Oracle Database software in a Data Guard configuration in a rolling fashion. |
| `DBMS_ROWID` | Provides procedures to create rowids and to interpret their contents |
| `DBMS_RULE` | Describes the subprograms that enable the evaluation of a rule set for a specified event. |
| `DBMS_RULE_ADM` | Provides the subprograms for creating and managing rules, rule sets, and rule evaluation contexts. |
| `DBMS_SCHEDULER` | Provides a collection of scheduling functions that are callable from any PL/SQL program |
| `DBMS_SERVER_ALERT` | Lets you issue alerts when some threshold has been violated |
| `DBMS_SERVICE` | Lets you create, delete, activate and deactivate services for a single instance |
| `DBMS_SESSION` | Provides access to SQL `ALTER` `SESSION ` statements, and other session information, from stored procedures |
| `DBMS_SHARED_POOL` | Lets you keep objects in shared memory, so that they will not be aged out with the normal LRU mechanism |
| `DBMS_SODA` | Implements Simple Oracle Document Access (`SODA`) which allows you to use the Oracle Database as a NoSQL document store. |
| `DBMS_SPACE` | Provides segment space information not available through standard SQL |
| `DBMS_SPACE_ADMIN` | Provides tablespace and segment space administration not available through the standard SQL |
| `DBMS_SPD` | The `DBMS_SPD` package provides subprograms for managing SQL plan directives (SPD). |
| `DBMS_SPM` | Supports the SQL plan management feature by providing an interface for the DBA or other user to perform controlled manipulation of plan history and SQL plan baselines maintained for various SQL statements |
| `DBMS_SQL` | Lets you use dynamic SQL to access the database |
| `DBMS_SQL_MONITOR` | The `DBMS_SQL_MONITOR` package provides information about Real-time SQL Monitoring and Real-time Database Operation Monitoring. |
| `DBMS_SQL_TRANSLATOR` | The `DBMS_SQL_TRANSLATOR` package provides an interface for creating, configuring, and using SQL translation profiles. |
| `DBMS_SQLDIAG` | Provides an interface to the SQL Diagnosability functionality |
| `DBMS_SQLPA` | Provides an interface to implement the SQL Performance Analyzer. |
| `DBMS_SQLTUNE` | Provides the interface to tune SQL statements |
| `DBMS_STAT_FUNCS` | Provides statistical functions |
| `DBMS_STATS` | Provides a mechanism for users to view and modify optimizer statistics gathered for database objects |
| `DBMS_STORAGE_MAP` | Communicates with FMON to invoke mapping operations |
| `DBMS_SYNC_REFRESH` | The `DBMS_SYNC_REFRESH` package provides an interface to perform a synchronous refresh of materialized views. |
| `DBMS_TABLE_DATA` | The `DBMS_TABLE_DATA` package provides procedures that can be used to retrieve the byte value of a single column, or a series of columns, in any table. |
| `DBMS_TDB` | Reports whether a database can be transported between platforms using the RMAN `CONVERT DATABASE` command. It verifies that databases on the current host platform are of the same endian format as the destination platform, and that the state of the current database does not prevent transport of the database. |
| `DBMS_TF` | The `DBMS_TF` package contains utilities for `POLYMORPHIC` `TABLE` functions (PTFs) implementation. You can use DBMS\_TF subprograms to consume and produce data, and get information about its execution environment.. |
| `DBMS_TNS` | The `DBMS_TNS` package provides the RESOLVE\_TNSNAME function to resolve a TNS name and return the corresponding Oracle Net8 connection string. |
| `DBMS_TRACE` | Provides routines to start and stop PL/SQL tracing |
| `DBMS_TRANSACTION` | Provides access to SQL transaction statements from stored procedures and monitors transaction activities |
| `DBMS_TRANSFORM` | Provides an interface to the message format transformation features of Oracle Advanced Queuing |
| `DBMS_TSDP_MANAGE` | The `DBMS_TSDP_MANAGE` package provides an interface to import and manage sensitive columns and sensitive column types in the database. |
| `DBMS_TSDP_PROTECT` | The `DBMS_TSDP_PROTECT` package provides an interface to configure transparent sensitive data protection (TSDP) policies in conjunction with the `DBMS_TSDP_MANAGE` package. The `DBMS_TSDP_PROTECT` package is available with the Enterprise Edition only. |
| `DBMS_TTS` | Checks if the transportable set is self-contained |
| `DBMS_TYPES` | Consists of constants, which represent the built-in and user-defined types |
| `DBMS_UMF` | The `DBMS_UMF` package provides an interface for deploying the Remote Management Framework (RMF) for an Oracle Database. The RMF is used for collecting performance statistics for an Oracle Database. |
| `DBMS_USER_CERTS` | The `DBMS_USER_CERTS` package allows you add and delete certificates. |
| `DBMS_UTILITY` | Provides various utility routines |
| `DBMS_WARNING` | Provides the interface to query, modify and delete current system or session settings |
| `DBMS_WM` | Describes how to use the programming interface to Oracle Database Workspace Manager to work with long transactions |
| `DBMS_WORKLOAD_CAPTURE` | Configures the Workload Capture system and produce the workload capture data. |
| `DBMS_WORKLOAD_REPLAY` | Provides an interface to replay and report on a record of a workload on a production or test system |
| `DBMS_WORKLOAD_REPOSITORY` | Lets you manage the Workload Repository, performing operations such as managing snapshots and baselines |
| `DBMS_XA` | Contains the XA/Open interface for applications to call XA interface in PL/SQL |
| `DBMS_XDB` | Describes Resource Management and Access Control interface for PL/SQL |
| `DBMS_XDB_ADMIN` | Provides an interface to implement `XMLIndex` administration operation |
| `DBMS_XDB_CONFIG` | The `DBMS_XDB_CONFIG` package provides an interface for configuring Oracle XML DB and its repository. |
| `DBMS_XDB_CONSTANTS` | The `DBMS_XDB_CONSTANTS` package provides an interface to commonly used constants. |
| `DBMS_XDB_REPOS` | The `DBMS_XDB_REPOS` package provides an interface to operate on the Oracle XML database Repository. |
| `DBMS_XDBRESOURCE` | Provides an interface to operate on the XDB resource's metadata and contents |
| `DBMS_XDB_VERSION` | Describes the versioning interface |
| `DBMS_XDBZ` | Controls the Oracle XML DB repository security, which is based on Access Control Lists (ACLs) |
| `DBMS_XEVENT` | Provides event-related types and supporting subprograms |
| `DBMS_XMLDOM` | Explains access to XMLType objects |
| `DBMS_XMLGEN` | Converts the results of a SQL query to a canonical XML format |
| `DBMS_XMLINDEX` | Provides an interface to implement asychronous indexing and apply node referencing |
| `DBMS_XMLPARSER` | Explains access to the contents and structure of XML documents |
| `DBMS_XMLSCHEMA` | Explains procedures to register and delete XML schemas |
| `DBMS_XMLSTORE` | Provides the ability to store XML data in relational tables |
| `DBMS_XMLTRANSLATIONS` | Provides an interface to perform translations so that strings can be searched or displayed in various languages |
| `DBMS_XPLAN` | Describes how to format the output of the `EXPLAIN` `PLAN` command |
| `DBMS_XSLPROCESSOR` | Explains access to the contents and structure of XML documents |
| `DEBUG_EXTPROC` | Lets you debug external procedures on platforms with debuggers that attach to a running process |
| `HTF` | Hypertext functions generate HTML tags |
| `HTP` | Hypertext procedures generate HTML tags |
| `OWA_CACHE` | Provides an interface that enables the `PL/SQL Gateway` cache to improve the performance of PL/SQL Web applications |
| `OWA_COOKIE` | Provides an interface for sending and retrieving HTTP cookies from the client's browser |
| `OWA_CUSTOM` | Provides a Global PLSQL Agent Authorization callback function |
| `OWA_IMAGE` | Provides an interface to access the coordinates where a user clicked on an image |
| `OWA_OPT_LOCK` | Contains subprograms that impose optimistic locking strategies so as to prevent lost updates |
| `OWA_PATTERN` | Provides an interface to locate text patterns within strings and replace the matched string with another string |
| `OWA_SEC` | Provides an interface for custom authentication |
| `OWA_TEXT` | Contains subprograms used by `OWA_PATTERN` for manipulating strings. They are externalized so you can use them directly. |
| `OWA_UTIL` | Contains utility subprograms for performing operations such as getting the value of CGI environment variables, printing the data that is returned to the client, and printing the results of a query in an HTML table |
| `SDO_CS` | Provides functions for coordinate system transformation |
| `SDO_CSW_PROCESS` | Contains subprograms for various processing operations related to support for Catalog Services for the Web (CSW) |
| `SDO_GCDR` | Contains the Oracle Spatial geocoding subprograms, which let you geocode unformatted postal addresses |
| `SDO_GEOM` | Provides functions implementing geometric operations on spatial objects |
| `SDO_GEOR` | Contains functions and procedures for the Spatial GeoRaster feature, which lets you store, index, query, analyze, and deliver raster image data and its associated Spatial vector geometry data and metadata |
| `SDO_GEOR_ADMIN` | Contains subprograms for administrative operations related to GeoRaster. |
| `SDO_GEOR_UTL` | Contains utility functions and procedures for the Spatial GeoRaster feature, including those related to using triggers with GeoRaster data |
| `SDO_LRS` | Provides functions for linear referencing system support |
| `SDO_MIGRATE` | Provides functions for migrating spatial data from previous releases |
| `SDO_NET` | Provides functions and procedures for working with data modeled as nodes and links in a network |
| `SDO_NET_MEM` | Contains functions and procedures for performing editing and analysis operations on network data using a network memory object |
| `SDO_OLS` | Contains functions and procedures for performing editing and analysis operations on network data using a network memory object |
| `SDO_PC_PKG` | Contains subprograms to support the use of point clouds in Spatial |
| `SDO_SAM` | Contains functions and procedures for spatial analysis and data mining |
| `SDO_TIN_PKG` | Contains subprograms to support the use of triangulated irregular networks (TINs) in Spatial |
| `SDO_TOPO` | Provides procedures for creating and managing Spatial topologies |
| `SDO_TOPO_MAP` | Contains subprograms for editing Spatial topologies using a cache (TopoMap object) |
| `SDO_TUNE` | Provides functions for selecting parameters that determine the behavior of the spatial indexing scheme used in Oracle Spatial |
| `SDO_UTIL` | Provides utility functions and procedures for Oracle Spatial |
| `SDO_WFS_LOCK` | Contains subprograms for WFS support for registering and unregistering feature tables |
| `SDO_WFS_PROC` | Provides utility functions and procedures for Oracle Spatial |
| `SEM_APIS` | Contains subprograms for working with the Resource Description Framework (RDF) and Web Ontology Language (OWL) in an Oracle database. |
| `SEM_PERF` | Contains subprograms for examining and enhancing the performance of the Resource Description Framework (RDF) and Web Ontology Language (OWL) support in an Oracle database |
| `SEM_RDFCTX` | Contains subprograms for managing extractor policies and semantic indexes created for documents |
| `SEM_RDFSA` | Contains subprograms for providing fine-grained access control to RDF data, using either a virtual private database (VPD) or Oracle Label Security (OLS) |
| `UTL_COLL ` | Enables PL/SQL programs to use collection locators to query and update |
| `UTL_COMPRESS` | Provides a set of data compression utilities |
| `UTL_DBWS` | Provides database Web services |
| `UTL_ENCODE` | Provides functions that encode RAW data into a standard encoded format so that the data can be transported between hosts |
| `UTL_FILE` | Enables your PL/SQL programs to read and write operating system text files and provides a restricted version of standard operating system stream file I/O |
| `UTL_HTTP` | Enables HTTP callouts from PL/SQL and SQL to access data on the Internet or to call Oracle Web Server Cartridges |
| `UTL_I18N` | Provides a set of services (Oracle Globalization Service) that help developers build multilingual applications |
| `UTL_INADDR` | Provides a procedure to support internet addressing |
| `UTL_IDENT` | Specifies which database or client PL/SQL is running |
| `UTL_LMS` | Retrieves and formats error messages in different languages |
| `UTL_MAIL` | A utility for managing email which includes commonly used email features, such as attachments, CC, BCC, and return receipt |
| `UTL_NLA` | Exposes a subset of the BLAS and LAPACK (Version 3.0) operations on vectors and matrices represented as `VARRAY` s |
| `UTL_RAW` | Provides SQL functions for manipulating `RAW` datatypes |
| `UTL_RECOMP` | Recompiles invalid PL/SQL modules, invalid views, Java classes, indextypes and operators in a database, either sequentially or in parallels |
| `UTL_REF` | Enables a PL/SQL program to access an object by providing a reference to the object |
| `UTL_SMTP` | Provides PL/SQL functionality to send emails |
| `UTL_RPADV` | Provides subprograms to collect and analyze statistics for the Oracle Replication components in a distributed database environment |
| `UTL_TCP` | Provides PL/SQL functionality to support simple TCP/IP-based communications between servers and the outside world |
| `UTL_URL` | Provides escape and unescape mechanisms for URL characters |
| `WPG_DOCLOAD` | Provides an interface to download files, both BLOBs and BFILEs |
| `ANYDATA TYPE` | A self-describing data instance type containing an instance of the type plus a description |
| `ANYDATASET TYPE` | Contains a description of a given type plus a set of data instances of that type |
| `ANYTYPE TYPE` | Contains a type description of any persistent SQL type, named or unnamed, including object types and collection types; or, it can be used to construct new transient type descriptions |
| `Oracle Database Advanced Queuing Types` | Describes the types used in Advanced Queuing |
| `DBFS Content Interface Types` | Describes public types defined to support the `DBMS_DBFS_CONTENT` interface. |
| `Database URI Type` | Contains URI Support, UriType Super Type, HttpUriType Subtype, DBUriType Subtype, XDBUriType Subtype, UriFactory Package |
| `Expression Filter Types` | Expression Filter feature is supplied with a set of predefined types and public synonyms for these types. |
| `JMS TYPES` | Describes JMS types so that a PL/SQL application can use JMS queues of JMS types |
| `LOGICAL CHANGE RECORD TYPES` | Describes LCR types, which are message payloads that contain information about changes to a database. |
| `MG_ID Package Types` | Provides an extensible framework that supports current RFID tags with the standard family of EPC bit encodings for the supported encoding types |
| `POLYMORPHIC TABLE FUNCTION (PTF) Package Types` | Describes types defined in the DBMS\_TF package to support PTF |
| `RULES TYPEs` | Describes the types used with rules, rule sets, and evaluation contexts |
| `RULES Manager Types` | Rules Manager is supplied with one predefined type and a public synonym |
| `SODA Types` | Describes the SODA Types. |
| `UTL Streams Types` | Describes abstract streams types used with Oracle XML functionality |
| `XMLType` | Describes the types and functions used for native XML support in the server |