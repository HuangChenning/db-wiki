---
title: "Implementing Data Cartridges in C, C++, and Java"
book: "Data Cartridge Developer's Guide"
doc_id: E10765-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/c_cpp_java.htm
tags:
  - oracle
  - 11g
  - data-cartridge-developers-guide
---

## 5 Implementing Data Cartridges in C, C++, and Java

This chapter describes how to use C, C++, and Java to implement the methods of a data cartridge. Methods are procedures and functions that define the operations permitted on data defined using the data cartridge. The focus is on issues related to developing and debugging external procedures.

This chapter contains these topics:

## Using External Procedures

PL/SQL is a powerful language for database programming, but some methods are too complex to code optimally in PL/SQL. For example, a routine to perform numeric integration probably runs faster if it is implemented in C rather than PL/SQL.

To support such special-purpose processing, PL/SQL provides an interface for calling routines written in other languages. This makes the strengths and capabilities of 3GLs, like C, available through calls from a database server. Such a 3GL routine is called an external procedure; it is stored in a shared library, registered with PL/SQL, and called from PL/SQL at run time.

External procedures are an important tool for data cartridge developers. They can be used not only to write fast, efficient, computation-intensive routines for cartridge types, but also to integrate existing code with the database as data cartridges. Existing shared libraries from other languages, such as a Windows NT DLL with C routines to perform format conversions for audio files, can be called directly from a method in a type implemented by an audio cartridge. Similarly, you can use external procedures to process signals, drive devices, analyze data streams, render graphics, or process numeric data.

See Also:

[PL/SQL User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm) for details on external procedures and their use

## Using Shared Libraries

A shared library is an operating system file, such as a Windows DLL or a Solaris shared object, that stores the coded implementation of external procedures. You can access to the shared library from Oracle by using an alias library, which is a schema object that represents the library within PL/SQL. For security reasons, you need DBA privileges to create an alias library.

To create the alias library, you must decide on the operating system location for the library, log in as a DBA or as a user with the `CREATE` `LIBRARY` privilege, and then enter the statement in Example 5-1. This creates the alias library schema object in the database. After the alias library is created, you can refer to the shared library by the name `DS_Lib` from PL/SQL.

Example 5-1 Creating an Alias Library

```
CREATE OR REPLACE LIBRARY DS_Lib AS  
     '/data_cartridge_dir/libdatastream.so';
```

Example 5-1 specifies an absolute path for the library. If you have copies of the library on multiple systems, to support distributed execution of external procedures by designated or dedicated agents, use an environment variable to specify the location of the libraries more generally, as in Example 5-2. This statement uses the environment variable `${DS_LIB_HOME}` to specify a common point of reference or root directory from which the library can be found on all systems. The string following the `AGENT` keyword specifies the agent (actually, a database link) that is used to run any external procedure declared to be in library `DS_Lib`.

Example 5-2 Specifying the Location of the Library Using an Environment Variable

```
CREATE OR REPLACE LIBRARY DS_Lib AS 
  '${DS_LIB_HOME}/libdatastream.so' AGENT 'agent_link';
```

See Also:

[Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm) for more information on using dedicated external procedure agents

## Registering an External Procedure

To call an external procedure, you must not only instruct PL/SQL regarding the alias library where the external procedure is defined, but also how to call this procedure and what arguments to pass to it.

The `DataStream` type was defined in [Example 3-1](obj_types.md), and [Example 3-2](obj_types.md) defined methods o f `DataStream` by calling functions from the `DS_Package` package, which is specified in [Example 4-9](pl_sql.md). Example 5-3 defines the body of this package.

Example 5-3 Defining the Body of a Package

```
CREATE OR REPLACE PACKAGE BODY DS_Package AS 
     FUNCTION DS_Findmin(data  CLOB) RETURN PLS_INTEGER IS EXTERNAL 
     NAME "c_findmin" LIBRARY DS_Lib LANGUAGE C WITH CONTEXT; 
     FUNCTION DS_Findmax(data CLOB) RETURN PLS_INTEGER IS EXTERNAL 
     NAME "c_findmax" LIBRARY DS_Lib LANGUAGE C WITH CONTEXT; 
   END;
```

Note that in the `PACKAGE` `BODY` declaration clause, the package functions are tied to external procedures in a shared library. The `EXTERNAL` clause in the function declaration registers information about the external procedure, such as its name (found after the `NAME` keyword), its location (which must be an alias library, following the `LIBRARY` keyword), the language in which the external procedure is written (following the `LANGUAGE` keyword), and so on.

The final part of the `EXTERNAL` clause in the example is the `WITH` `CONTEXT` specification. Here, a context pointer is passed to the external procedure. The context pointer is opaque to the external procedure, but is available so that the external procedure can call back to the Oracle server, to potentially access more data in the same transaction context.

Although the example describes external procedure calls from object type methods, a data cartridge can use external procedures from a variety of other places in PL/SQL. External procedure calls can appear in:

- Anonymous blocks
- Standalone and packaged subprograms
- Methods of an object type
- Database triggers
- SQL statements (calls to packaged functions only)

See Also:

- [PL/SQL User's Guide and Reference.](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm) for a description of the parameters that can accompany an `EXTERNAL` clause
- [Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/toc.htm), the chapter on external procedures, for information on formatting the call specification when passing an object type to a C routine
- The `WITH` `CONTEXT` clause is discussed in "Using the WITH CONTEXT Clause".

## How PL/SQL Calls an External Procedure

To call an external procedure, PL/SQL must know the DLL or shared library in which the procedure resides. PL/SQL looks up the alias library in the `EXTERNAL` clause of the subprogram that registered the external procedure. The data dictionary is used to determine the actual path to the operating system shared library or DLL.

PL/SQL alerts a Listener process, which in turn starts a session-specific agent. Unless some other particular agent has been designated either in the `CREATE LIBRARY` statement for the procedure's specified library or in the agent argument of the `CREATE PROCEDURE` statement, the default agent `extproc` is launched. The Listener hands over the connection to the agent. PL/SQL passes the agent the name of the DLL, the name of the external procedure, and any parameters passed in by the caller. The rest of this account assumes that the agent launched is the default agent `extproc`.

After receiving the name of the DLL and the external procedure, `extproc` loads the DLL and runs the external procedure. Also, `extproc` handles service calls, such as raising an exception, and callbacks to the Oracle server. Finally, `extproc` passes to PL/SQL any values returned by the external procedure. Figure 5-1 shows the flow of control.

Figure 5-1 Calling an External Procedure

![Description of Figure 5-1 follows](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img/addci012.gif "Description of Figure 5-1 follows")  
[Description of "Figure 5-1 Calling an External Procedure"](https://docs.oracle.com/cd/E11882_01/appdev.112/e10765/img_text/addci012.htm)  

After the external procedure completes, `extproc` remains active throughout your Oracle session. Thus, you incur the cost of spawning `extproc` only one time, no matter how many calls you make. Still, you should call an external procedure only when the computational benefits outweigh the cost. When you log off, `extproc` is killed.

Note that the Listener must start `extproc` on the system that runs the Oracle server. Starting `extproc` on a different system is not supported.

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm) for more information on using dedicated external procedure agents to run an external procedure
- [Oracle Database Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about administering `extproc` and external procedure call

## Configuration Files for External Procedures

The configuration files `listener.ora` and `tnsnames.ora` must have appropriate entries, so that the Listener can dispatch the external procedures.

The Listener configuration file `listener.ora` must have a `SID_DESC` entry for the external procedure, as demonstrated in Example 5-4.

Example 5-4 Setting the SID\_DESC Entry in the Listener Configuration FIle

```
# Listener configuration file  
# This file is generated by stkconf.tsc  
 
CONNECT_TIMEOUT_LISTENER = 0  
 
LISTENER = (ADDRESS_LIST=  
  (ADDRESS=(PROTOCOL=ipc)(KEY=o10))  
  (ADDRESS=(PROTOCOL=tcp)(HOST=unix123)(PORT=1521))  
)

SID_LIST_LISTENER = (SID_LIST=   
  SID_DESC=(SID_NAME=o10)(ORACLE_HOME=/rdbms/u01/app/oracle/product/11.2.0.1.0) 
  SID_DESC=(SID_NAME=extproc)
           (ORACLE_HOME=/rdbms/u01/app/oracle/product/11.2.0.1.0)
  (PROGRAM=extproc))
```

Example 5-4 assumes the following:

- The Oracle instance is called `o10`.
- The system or node on which the Oracle server runs is named `unix123`.
- The installation directory for the Oracle server is `/rdbms/u01`.
- The port number for Oracle TCP/IP communication is the default Listener port `1521`.

The `tnsnames.ora` file is the network substrate configuration file, and it must also be updated to refer to the external procedure, as demonstrated in Example 5-5:

Example 5-5 Updating the Network Substrate Configuration to Refer to External Procedures

```
o10 = (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=unix123)(PORT=1521))
  (CONNECT_DATA=(SID=o10)))
extproc_connection_data = (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=o10))
  CONNECT_DATA=(SID=extproc)))
```

Example 5-5 assumes that IPC mechanisms are used to communicate with the external procedure. You can also use, for example, TCP/IP for communication, in which case the `PROTOCOL` parameter must be set to `tcp`.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about configuring the `listener.ora` and `tnsnames.ora` files

### Passing Parameters to an External Procedure

Passing parameters to an external procedure is complicated by several circumstances:

- The set of PL/SQL data types does not correspond one-to-one with the set of C data types.
- PL/SQL parameters can be `null`, whereas C parameters cannot. Unlike C, PL/SQL includes the RDBMS concept of nullity.
- The external procedure might need the current length or maximum length of `CHAR`, `LONG` `RAW`, `RAW`, and `VARCHAR2` parameters.
- The external procedure might need character set information about `CHAR`, `VARCHAR2`, and `CLOB` parameters.
- PL/SQL might need the current length, maximum length, or null status of values returned by the external procedure.

In the following sections, you learn how to specify a parameter list that deals with these circumstances. An example of parameter passing is shown in Example 5-6, where the package function `DS_Findmin(data CLOB)` calls the C routine `c_findmin` and the `CLOB` argument is passed to the C routine as an `OCILobLocator()`.

### Specifying Data Types

You do not pass parameters to an external procedure directly. Instead, you pass them to the PL/SQL subprogram that registered the external procedure. So, you must specify PL/SQL data types for the parameters. Table 5-1 maps each PL/SQL data type to a default external data type. The external data types map to C data type.

Table 5-1 Parameter Data Type Mappings

| PL/SQL Type | Supported External Types | Default External Type |
| --- | --- | --- |
| ``` BINARY_INTEGER, BOOLEAN, PLS_INTEGER ``` | ``` CHAR, UNSIGNED CHAR, SHORT, UNSIGNED  SHORT, INT, UNSIGNED INT, LONG,  UNSIGNED LONG, SB1, UB1, SB2, UB2,   SB4, UB4, SIZE_T ``` | ``` INT ``` |
| ``` NATURAL, NATURALN,  POSITIVE, POSITIVEN,  SIGNTYPE ``` | ``` CHAR, UNSIGNED CHAR, SHORT, UNSIGNED  SHORT, INT, UNSIGNED INT, LONG,  UNSIGNED LONG, SB1, UB1, SB2 ,UB2,  SB4, UB4, SIZE_T ``` | ``` UNSIGNED INT ``` |
| ``` FLOAT, REAL ``` | ``` FLOAT ``` | ``` FLOAT ``` |
| ``` DOUBLE PRECISION ``` | ``` DOUBLE ``` | ``` DOUBLE ``` |
| ``` CHAR, CHARACTER, LONG, ROWID, VARCHAR, VARCHAR2 ``` | ``` STRING ``` | ``` STRING ``` |
| ``` LONG RAW, RAW ``` | ``` RAW ``` | ``` RAW ``` |
| ``` BFILE, BLOB, CLOB ``` | ``` OCILOBLOCATOR ``` | ``` OCILOBLOCATOR ``` |

In some cases, you can use the `PARAMETERS` clause to override the default data type mappings. For example, you can re-map the PL/SQL data type `BOOLEAN` from external data type `INT` to external data type `CHAR`.

To avoid errors when declaring C prototype parameters, refer to Table 5-2, which shows the C data type to specify for a given external data type and PL/SQL parameter mode. For example, if the external data type of an `OUT` parameter is `CHAR`, specify the data type `char*` in your C prototype.

Table 5-2 External Data Type Mappings

| External Data Type | IN, RETURN | IN by Reference, RETURN by Reference | IN OUT, OUT |
| --- | --- | --- | --- |
| ``` CHAR ``` | ``` char ``` | ``` char * ``` | ``` char * ``` |
| ``` UNSIGNED CHAR ``` | ``` unsigned char ``` | ``` unsigned char * ``` | ``` unsigned char * ``` |
| ``` SHORT ``` | ``` short ``` | ``` short * ``` | ``` short * ``` |
| ``` UNSIGNED SHORT ``` | ``` unsigned short ``` | ``` unsigned short * ``` | ``` unsigned short * ``` |
| ``` INT ``` | ``` int ``` | ``` int * ``` | ``` int * ``` |
| ``` UNSIGNED INT ``` | ``` unsigned int ``` | ``` unsigned int * ``` | ``` unsigned int * ``` |
| ``` LONG ``` | ``` long ``` | ``` long * ``` | ``` long * ``` |
| ``` UNSIGNED LONG ``` | ``` unsigned long ``` | ``` unsigned long * ``` | ``` unsigned long * ``` |
| ``` SIZE_T ``` | ``` size_t ``` | ``` size_t * ``` | ``` size_t * ``` |
| ``` SB1 ``` | ``` sb1 ``` | ``` sb1 * ``` | ``` sb1 * ``` |
| ``` UB1 ``` | ``` ub1 ``` | ``` ub1 * ``` | ``` ub1 * ``` |
| ``` SB2 ``` | ``` sb2 ``` | ``` sb2 * ``` | ``` sb2 * ``` |
| ``` UB2 ``` | ``` ub2 ``` | ``` ub2 * ``` | ``` ub2 * ``` |
| ``` SB4 ``` | ``` sb4 ``` | ``` sb4 * ``` | ``` sb4 * ``` |
| ``` UB4 ``` | ``` ub4 ``` | ``` ub4 * ``` | ``` ub4 * ``` |
| ``` FLOAT ``` | ``` float ``` | ``` float * ``` | ``` float * ``` |
| ``` DOUBLE ``` | ``` double ``` | ``` double * ``` | ``` double * ``` |
| ``` STRING ``` | ``` char * ``` | ``` char * ``` | ``` char * ``` |
| ``` RAW ``` | ``` unsigned char * ``` | ``` unsigned char * ``` | ``` unsigned char * ``` |
| ``` OCILOBLOCATOR ``` | ``` OCILobLocator * ``` | ``` OCILobLocator * ``` | ``` OCILobLocator ** ``` |

### Using the Parameters Clause

You can optionally use the `PARAMETERS` clause to pass additional information about PL/SQL formal parameters and function return values to an external procedure. You can also use this clause to reposition parameters.

See Also:

[Oracle Database PL/SQL Language Reference.](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/toc.htm)

### Using the WITH CONTEXT Clause

When launched, an external procedure must access the database. For example, `DS_Findmin` does not copy the entire `CLOB` data over to `c_findmin`, because doing so would vastly increase the amount of stack that the C routine needs. Instead, the PL/SQL function just passes a `LOB` locator to the C routine, with the intent that the database is accessed again from C to read the actual `LOB` data.

When the C routine reads the data, it can use the OCI buffering and streaming interfaces associated with LOBs, so that only incremental amounts of stack are needed. Such re-access of the database from an external procedure is known as a callback.

To be able to call back to a database, you must use the `WITH` `CONTEXT` clause to give the external procedure access to the database environment, service, and error handles. When an external procedure is called using `WITH` `CONTEXT`, the corresponding C routine automatically gets an argument of type `OCIExtProcContext` \* as its first parameter. The order of the parameters can be changed using the `PARAMETERS` clause. You can use this context pointer to fetch the handles using the `OCIExtProcGetEnv` call, and then call back to the database. This procedure is shown in Example 5-6.

See Also:

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for details about OCI callbacks

## Doing Callbacks

An external procedure that runs on the Oracle server can call the access function `OCIExtProcGetEnv()` to obtain the OCI environment and service handles. With the OCI, you can use callbacks to execute SQL statements and PL/SQL subprograms, fetch data, and manipulate LOBs. Moreover, callbacks and external procedures operate in the same user session and transaction context, so they have the same user privileges.

Example 5-6 is a version of `c_findmin` that is simplified to illustrate callbacks.

Example 5-6 Using Callbacks

```
Static  OCIEnv   *envhp;
Static  OCISvcCtx  *svchp;
Static OCIError   *errhp;
Int   c_findmin (OCIExtProcContext *ctx, OCILobLocator  *lobl) {
sword  retval;
retval = OCIExtProcGetEnv (ctx, &envhp, &svchp, &errhp);
if ((retval != OCI_SUCCESS) && (retval !=  OCI_SUCCESS_WITH_INFO))
   exit(-1);
   /* Use lobl to read the CLOB, compute the minimum, and store the value
       in retval. */
return retval;
}
```

### Restrictions on Callbacks

With callbacks, the following SQL statements and OCI routines are not supported:

- Transaction control statements such as `COMMIT`
- Data definition statements such as `CREATE`
- Object-oriented OCI routines such as `OCIRefClear`
- Polling-mode OCI routines such as `OCIGetPieceInfo`
- The following OCI routines:
	- `OCIEnvInit()`
		- `OCIInitialize()`
		- `OCIPasswordChange()`
		- `OCIServerAttach()`
		- `OCIServerDetach()`
		- `OCISessionBegin ()`
		- `OCISessionEnd ()`
		- `OCISvcCtxToLda()`
		- `OCITransCommit()`
		- `OCITransDetach()`
		- `OCITransRollback()`
		- `OCITransStart()`
- Also, with OCI routine `OCIHandleAlloc()`, the following handle types are not supported:
	- `OCI_HTYPE_SERVER`
		- `OCI_HTYPE_SESSION`
		- `OCI_HTYPE_SVCCTX`
		- `OCI_HTYPE_TRANS`

## Common Potential Errors

This section presents several kinds of errors you might encounter when running external procedures.

### Calls to External Functions

```
Can't Find DLL
ORA-06520: PL/SQL: Error loading external library
ORA-06522: Unable to load DLL
ORA-06512: at "<name>", line <number>
ORA-06512: at "<name>", line <number>
ORA-06512: at line <number>
```

You may have specified the wrong path or wrong name for the DLL file, or you may have tried to use a DLL on a network mounted drive (a remote drive).

### RPC Time Out

```
ORA-28576: lost RPC connection to external procedure agent
ORA-06512: at "<name>", line <number>
ORA-06512: at "<name>", line <number>
ORA-06512: at line <number>
```

This error might occur after you exit a debugger while debugging a shared library or DLL. Simply disconnect your client and reconnect to the database.

## Debugging External Procedures

Usually, when an external procedure fails, its C prototype is faulty. That is, the prototype does not match the one generated internally by PL/SQL. This can happen if you specify an incompatible C data type. For example, to pass an `OUT` parameter of type `REAL`, you must specify `float *`. Specifying `float`, `double *`, or any other C data type, results in a mismatch.

In such cases, you might get a lost RPC connection to external procedure agent error, which means that agent `extproc` terminated abnormally because the external procedure caused a core dump. To avoid errors when declaring C prototype parameters, refer to Table 5-2.

### Using Package DEBUG\_EXTPROC

To help you debug external procedures, PL/SQL provides the utility package `DEBUG_EXTPROC`. To install the package, run the script `dbgextp`.`sql`, which you can find in the PL/SQL demo directory.

To use the package, follow the instructions in `dbgextp.sql`. Your Oracle account must have `EXECUTE` privileges on the package and `CREATE` `LIBRARY` privileges.

Note that `DEBUG_EXTPROC` works only on platforms with debuggers that can attach to a running process.

### Debugging C Code in DLLs on Windows NT Systems

If you are developing on a Windows NT system, you may perform the following additional actions to debug external procedures:

1. Invoke the Windows NT Task Manager; press Ctrl+Alt+Del and select Task Manager.
2. In the Processes display, select ExtProc.exe.
3. Right click, and select Debug.
4. Select OK in the message box.
	At this point, if you have built your DLL in a debug fashion with Microsoft Visual C++, Visual C++ is activated.
5. In the Visual C++ window, select Edit > Breakpoints.
6. Use the breakpoint identified in `dbgextp.sql` in the PL/SQL demo directory.

## Guidelines for Using External Procedures with Data Cartridges

Make sure to write thread-safe external procedures. In particular, avoid using static variables, which can be shared by routines running in separate threads.

For help in creating a dynamic link library, look in the RDBMS subdirectory `/public`, where a template `makefile` can be found.

When calling external procedures, never write to `IN` parameters or overflow the capacity of `OUT` parameters. PL/SQL does no run-time checks for these error conditions. Likewise, never read an `OUT` parameter or a function result. Also, always assign a value to `IN` `OUT` and `OUT` parameters and to function results. Otherwise, your external procedure does not return successfully.

If you include the `WITH` `CONTEXT` and `PARAMETERS` clauses, you must specify the parameter `CONTEXT`, which shows the position of the context pointer in the parameter list. If you omit the `PARAMETERS` clause, the context pointer is the first parameter passed to the external procedure.

If you include the `PARAMETERS` clause and the external procedure is a function, you must specify the parameter `RETURN` (not `RETURN property`) in the last position.

For every formal parameter, there must be a corresponding parameter in the `PARAMETERS` clause. Also, ensure that the data types of parameters in the `PARAMETERS` clause are compatible with those in the C prototype, because no implicit conversions are done.

A parameter for which you specify `INDICATOR` or `LENGTH` has the same parameter mode as the corresponding formal parameter. However, a parameter for which you specify `MAXLEN`, `CHARSETID`, or `CHARSETFORM` is always treated like an `IN` parameter, even if you also specify `BY REFERENCE`.

With a parameter of type `CHAR`, `LONG` `RAW`, `RAW`, or `VARCHAR2`, you must use the property `LENGTH`. Also, if that parameter is `IN` `OUT` or `OUT` and null, you must set the length of the corresponding C parameter to zero.

See Also:

For more information about multithreading, see the [Oracle Database Heterogeneous Connectivity Administrator's Guide.](https://docs.oracle.com/cd/E11882_01/server.112/e11050/toc.htm)

## Java Methods

To use Java Data Cartridges, it is important that you know how to load Java class definitions, about how to call stored procedures, and about context management. Information on ODCI classes can also be found in [Chapter 18, "Cartridge Services Using C, C++ and Java"](serv_c_java_ref.md) of this manual.