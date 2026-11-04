---
title: Getting Started
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/getsta.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 2 Getting Started

This chapter discusses the compatibility of Oracle Java Database Connectivity (JDBC) driver versions, database versions, and Java Development Kit (JDK) versions. It also describes the basics of testing a client installation and configuration and running a simple application. This chapter contains the following sections:

## Version Compatibility for Oracle JDBC Drivers

This section discusses the general JDBC version compatibility issues.

Backward Compatibility

The JDBC drivers are certified to work with the currently supported versions of Oracle Database. For example, the JDBC Thin drivers in Oracle Database 11g Release 2 (11.2) are certified to work with the 10.2.x, 10.1.x, 9.2.x, and 9.0.1.x Oracle Database releases. However, they are not certified to work with older, unsupported database releases, such as 8.0.x and 7.x.

Forward Compatibility

Existing and supported JDBC drivers are certified to work with Oracle Database 11g Release 2 (11.2).

Note:

- In Oracle Database 11g Release 2 (11.2), Oracle JDBC drivers no longer support JDK 1.4.x or earlier versions.
- You can find a complete, up-to-date list of supported databases at `http://www.oracle.com/technetwork/database/enterprise-edition/jdbc-faq-090281.html`.

## Verification of a JDBC Client Installation

To verify a JDBC client installation, you must do all of the following:

- Check the Installed Directories and Files
- Check the Environment Variables
- Ensure that the Java Code Can Be Compiled and Run
- Determine the Version of the JDBC Driver
- Test JDBC and the Database Connection

Installation of an Oracle JDBC driver is platform-specific. Follow the installation instructions for the driver you want to install in your platform-specific documentation.

This section describes the steps for verifying an Oracle client installation of the JDBC drivers, assuming that you have already installed the driver of your choice.

If you have installed the JDBC Thin driver, then no further installation on the client computer is necessary.

Note:

The JDBC Thin driver requires a TCP/IP listener to be running on the computer where the database is installed.

If you have installed the JDBC Oracle Call Interface (OCI) driver, then you must also install the Oracle client software. This includes Oracle Net and the OCI libraries.

### Check the Installed Directories and Files

Installing the Oracle Java products creates, among other things, the following directories:

- `ORACLE_HOME` `/jdbc`
- `ORACLE_HOME` `/jlib`

Check whether or not the following directories and files have been created and populated in the `ORACLE_HOME` `/jdbc` directory:

- `demo`
	This directory contains a compressed file, `demo.zip` or `demo.tar`. When you uncompress this compressed file, the `samples` directory and the `Samples-Readme.txt` file are created. The `samples` directory contains sample programs, including examples of how to use JDBC escape syntax and Oracle SQL syntax, PL/SQL blocks, streams, user-defined types, additional Oracle type extensions, and Oracle performance extensions.
- `doc`
	This directory contains the `javadoc.zip` file, which is the Oracle JDBC application programming interface (API) documentation.
- `lib`
	The `lib` directory contains the following required Java classes:
	- `orai18n.jar` and `orai18n-mapping.jar`
		Contain classes for globalization and multibyte character sets support
		- `ojdbc5.jar`, `ojdbc5_g.jar`, `ojdbc6.jar`, and `ojdbc6_g.jar`
		Contain the JDBC driver classes for use with JDK 1.5 and JDK 1.6
		Note:
		- Since Oracle Database 11g Release 1 (11.1), support for a version of JDK earlier than version 1.5 has been removed. Also, the `ojdbc14.jar` and `classes12.jar` files are no longer shipped. Instead, you can use the `ojdbc5.jar` and `ojdbc6.jar` files, which are shipped with Oracle Database 11g.
		- If you are using JSE 6 and later, then there is no need to explicitly load the JDBC driver. This means that the Java run-time loads the driver when needed and you need not include `Class.forName("oracle.jdbc.OracleDriver")` or `new oracle.jdbc.OracleDriver()` in your code. But if you are using J2SE 5.0, then you need to load the JDBC driver explicitly.
- `Readme.txt`
	This file contains late-breaking and release-specific information about the drivers, which may not have been included in other documentation on the product.

Check whether or not the following directories have been created and populated in the `ORACLE_HOME` `/jlib` directory:

- `jta.jar` and `jndi.jar`
	These files contain classes for the Java Transaction API (JTA) and the Java Naming and Directory Interface (JNDI). These are required only if you are using JTA features for distributed transaction management or JNDI features for naming services.
	Note:
	These files can also be obtained from the Sun Microsystems Web site. However, it is recommended that you use the versions supplied by Oracle, which have been tested with the Oracle drivers.
- `ons.jar`
	This JAR file contains classes for Oracle Notification Services. This file is required if you use Fast Application Notification (FAN) to notify other processes about configuration and service level information.

### Check the Environment Variables

This section describes the environment variables that must be set for the JDBC OCI driver and the JDBC Thin driver, focusing on the Sun Solaris, Linux, and Microsoft Windows platforms.

You must set the `CLASSPATH` environment variable for your installed JDBC OCI or Thin driver. Include the following in the `CLASSPATH` environment variable:

```
ORACLE_HOME/jdbc/lib/ojdbc5.jar
ORACLE_HOME/jlib/orai18n.jar
```

Note:

If you use the JTA features and the JNDI features, then you must specify `jta.jar` and `jndi.jar` in your `CLASSPATH` environment variable.

JDBC OCI Driver

If you are installing the JDBC OCI driver, then you must also set the following value for the library path environment variable:

- On Sun Solaris or Linux, set the `LD_LIBRARY_PATH` environment variable as follows:
	```
	ORACLE_HOME/lib
	```
	This directory contains the `libocijdbc11.so` shared object library.
	Note:
	If you are running a 32-bit Java Virtual Machine (JVM) against a 64-bit client or database, then you must also add `ORACLE_HOME` `/lib32` to the `LD_LIBRARY_PATH environment variable`.
- On Microsoft Windows, set the `PATH` environment variable as follows:
	```
	ORACLE_HOME\bin
	```
	This directory contains the `ocijdbc11.dll` dynamic link library.

All of the JDBC OCI demonstration programs can be run in the Instant Client mode by including the JDBC OCI Instant Client data shared library on the library path environment variable.

See Also:

[Chapter 6, "Features Specific to JDBC OCI Driver"](instclnt.md)

JDBC Thin Driver

If you are installing the JDBC Thin driver, then you do not have to set any other environment variables. However, to use the JDBC server-side Thin driver, you need to set permission.

Setting Permission for the Server-Side Thin Driver

The JDBC server-side Thin driver opens a socket for its connection to the database. Because Oracle Database enforces the Java security model, a check is performed for a `SocketPermission` object.

To use the JDBC server-side Thin driver, the connecting user must be granted the appropriate permission. The following is an example of how the permission can be granted for the user `SCOTT`:

```
CREATE ROLE jdbcthin;
CALL dbms_java.grant_permission('JDBCTHIN', 'java.net.SocketPermission', '*', 'connect');
GRANT jdbcthin TO SCOTT;
```

Note that `JDBCTHIN` in the `grant_permission` call must be in uppercase. The asterisk (`*`) is a pattern. You can restrict the user by granting permission to connect to only specific computers or ports.

See Also:

[Oracle Database Java Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e10588/toc.htm)

### Ensure that the Java Code Can Be Compiled and Run

To further ensure that Java is set up properly on your client system, go to the `samples` directory under the `ORACLE_HOME` `/jdbc/demo` directory. Now, type the following commands on the command line, one after the other, to see if the Java compiler and the Java interpreter run without error:

```
javac

java
```

Each of the preceding commands should display a list of options and parameters and then exit. Ideally, verify that you can compile and run a simple test program, such as `jdbc/demo/samples/generic/SelectExample`.

### Determine the Version of the JDBC Driver

You can determine the version of the JDBC driver that you installed, by calling the `getDriverVersion` method of the `OracleDatabaseMetaData` class.

The following sample code shows how to determine the driver version:

```
import java.sql.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.OracleDataSource;

class JDBCVersion
{
  public static void main (String args[]) throws SQLException
  {
    OracleDataSource ods = new OracleDataSource();
    ods.setURL("jdbc:oracle:thin:scott/tiger@<host>:<port>:<service>");
    Connection conn = ods.getConnection();

    // Create Oracle DatabaseMetaData object
    DatabaseMetaData meta = conn.getMetaData();

    // gets driver info:
    System.out.println("JDBC driver version is " + meta.getDriverVersion());
  }
}
```

You can also determine the version of the JDBC driver by executing the following commands:

- `java -jar ojdbc5.jar`
- `java -jar ojdbc6.jar`

### Test JDBC and the Database Connection

The `samples` directory contains sample programs for a particular Oracle JDBC driver. One of the programs, `JdbcCheckup.java`, is designed to test JDBC and the database connection. The program queries for the user name, password, and the name of the database to which you want to connect. The program connects to the database, queries for the string " `Hello World` ", and prints it to the screen.

Go to the `samples` directory, and compile and run the `JdbcCheckup.java` program. If the results of the query print without error, then your Java and JDBC installations are correct.

Although `JdbcCheckup.java` is a simple program, it demonstrates several important functions by performing the following:

- Imports the necessary Java classes, including JDBC classes
- Creates a `DataSource` instance
- Connects to the database
- Runs a simple query
- Prints the query results to your screen

The `JdbcCheckup.java` program, which uses the JDBC OCI driver, is as follows:

```
/*
 * This sample can be used to check the JDBC installation.
 * Just run it and provide the connect information. It will select
 * "Hello World" from the database.
 */

// You need to import the java.sql and JDBC packages to use JDBC
import java.sql.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.OracleDataSource;

// We import java.io to be able to read from the command line
import java.io.*;

class JdbcCheckup
{
  public static void main(String args[]) throws SQLException, IOException
  {

    // Prompt the user for connect information
    System.out.println("Please enter information to test connection to 
                          the database");
    String user;
    String password;
    String database;

    user = readEntry("user: ");
    int slash_index = user.indexOf('/');
    if (slash_index != -1)
    {
      password = user.substring(slash_index + 1);
      user = user.substring(0, slash_index);
    }
    else
      password = readEntry("password: ");
    database = readEntry("database(a TNSNAME entry): ");

    System.out.print("Connecting to the database...");
    System.out.flush();
    System.out.println("Connecting...");
    // Open an OracleDataSource and get a connection
    OracleDataSource ods = new OracleDataSource();
    ods.setURL("jdbc:oracle:oci:@" + database);
    ods.setUser(user);
    ods.setPassword(password);
    Connection conn = ods.getConnection();
    System.out.println("connected.");

    // Create a statement
    Statement stmt = conn.createStatement();

    // Do the SQL "Hello World" thing
    ResultSet rset = stmt.executeQuery("select 'Hello World' from dual");

    while (rset.next())
      System.out.println(rset.getString(1));
    // close the result set, the statement and the connection
    rset.close();
    stmt.close();
    conn.close();
    System.out.println("Your JDBC installation is correct.");
  }

  // Utility function to read a line from standard input
  static String readEntry(String prompt)
  {
    try
    {
      StringBuffer buffer = new StringBuffer();
      System.out.print(prompt);
      System.out.flush();
      int c = System.in.read();
      while (c != '\n' && c != -1)
      {
        buffer.append((char)c);
        c = System.in.read();
      }
      return buffer.toString().trim();
    }
    catch(IOException e)
    {
      return "";
    }
  }
}
```

## Basic Steps in JDBC

After verifying the JDBC client installation, you can start creating your JDBC applications. When using Oracle JDBC drivers, you must include certain driver-specific information in your programs. This section describes, in the form of a tutorial, where and how to add the information. The tutorial guides you through the steps to create code that connects to and queries a database from the client.

You must write code to perform the following tasks:

1. Importing Packages
2. Opening a Connection to a Database
3. Creating a Statement Object
4. Running a Query and Retrieving a Result Set Object
5. Processing the Result Set Object
6. Closing the Result Set and Statement Objects
7. Making Changes to the Database
8. Committing Changes
9. Closing the Connection

Note:

You must supply Oracle driver-specific information for the first three tasks, which allow your program to use the JDBC application programming interface (API) to access a database. For the other tasks, you can use standard JDBC Java code, as you would for any Java application.

### Importing Packages

Regardless of which Oracle JDBC driver you use, include the `import` statements shown in Table 2-1 at the beginning of your program.

Table 2-1 Import Statements for JDBC Driver

| Import statement | Provides |
| --- | --- |
| `import java.sql.*;` | Standard JDBC packages. |
| `import java.math.*;` | The `BigDecimal` and `BigInteger` classes. You can omit this package if you are not going to use these classes in your application. |
| `import oracle.jdbc.*;`  `import oracle.jdbc.pool.*;`  `import oracle.sql.*;` | Oracle extensions to JDBC. This is optional.  `OracleDataSource`.  Oracle type extensions. This is optional. |

The Oracle packages listed as optional provide access to the extended functionality provided by Oracle JDBC drivers, but are not required for the example presented in this section.

Note:

It is better to import only the classes your application needs, rather than using the wildcard asterisk (`*`). This guide uses the asterisk (\*) for simplicity, but this is not the recommended way of importing classes and interfaces.

### Opening a Connection to a Database

First, you must create an `OracleDataSource` instance. Then, open a connection to the database using the `OracleDataSource.getConnection` method. The properties of the retrieved connection are derived from the `OracleDataSource` instance. If you set the URL connection property, then all other properties, including `TNSEntryName`, `DatabaseName`, `ServiceName`, `ServerName`, `PortNumber`, `Network Protocol`, and driver type are ignored.

Specifying a Database URL, User Name, and Password

The following code sets the URL, user name, and password for a data source:

```
OracleDataSource ods = new OracleDataSource();
ods.setURL(url);
ods.setUser(user);
ods.setPassword(password);
```

The following example connects user `scott` with password `tiger` to a database with service `orcl` through port 1521 of the host `myhost`, using the JDBC Thin driver:

```
OracleDataSource ods = new OracleDataSource();
String url = "jdbc:oracle:thin:@//myhost:1521/orcl",
ods.setURL(url);
ods.setUser("scott");
ods.setPassword("tiger");
Connection conn = ods.getConnection();
```

Note:

The user name and password specified in the arguments override any user name and password specified in the URL.

Specifying a Database URL that Includes User Name and Password

The following example connects user `scott` with password `tiger` to a database host whose Transparent Network Substrate (TNS) entry is `myTNSEntry`, using the JDBC Oracle Call Interface (OCI) driver. In this case, the URL includes the user name and password and is the only input parameter.

```
String url = "jdbc:oracle:oci:scott/tiger@myTNSEntry");
ods.setURL(url);
Connection conn = ods.getConnection();
```

If you want to connect using the Thin driver, then you must specify the port number. For example, if you want to connect to the database on the host `myhost` that has a TCP/IP listener on port 1521 and the service identifier is `orcl`, then provide the following code:

```
String URL = "jdbc:oracle:thin:scott/tiger@//myhost:1521/orcl");
ods.setURL(URL);
Connection conn = ods.getConnection();
```

See Also:

[Chapter 8, "Data Sources and URLs"](urls.md)

### Creating a Statement Object

Once you connect to the database and, in the process, create a `Connection` object, the next step is to create a `Statement` object. The `createStatement` method of the JDBC `Connection` object returns an object of the JDBC `Statement` type. To continue the example from the previous section, where the `Connection` object `conn` was created, here is an example of how to create the `Statement` object:

```
Statement stmt = conn.createStatement();
```

### Running a Query and Retrieving a Result Set Object

To query the database, use the `executeQuery` method of the `Statement` object. This method takes a SQL statement as input and returns a JDBC `ResultSet` object.

Note:

- The method used to execute a `Statement` object depends on the type of SQL statement being executed. If the `Statement` object represents a SQL query returning a `ResultSet` object, the `executeQuery` method should be used. If the SQL is known to be a DDL statement or a DML statement returning an update count, the `executeUpdate` method should be used. If the type of the SQL statement is not known, the `execute` method should be used.
- In case of a standard JDBC driver, if the SQL string being executed does not return a `ResultSet` object, then the `executeQuery` method throws a `SQLException` exception. In case of an Oracle JDBC driver, the `executeQuery` method does not throw a `SQLException` exception even if the SQL string being executed does not return a `ResultSet` object.

To continue the example, once you create the `Statement` object `stmt`, the next step is to run a query that returns a `ResultSet` object with the contents of the `ename` column of a table of employees named `EMP`:

```
ResultSet rset = stmt.executeQuery ("SELECT ename FROM emp");
```

### Processing the Result Set Object

Once you run your query, use the `next()` method of the `ResultSet` object to iterate through the results. This method steps through the result set row by row, detecting the end of the result set when it is reached.

To pull data out of the result set as you iterate through it, use the appropriate `get` `XXX` methods of the `ResultSet` object, where `XXX` corresponds to a Java data type.

For example, the following code will iterate through the `ResultSet` object, `rset`, from the previous section and will retrieve and print each employee name:

```
while (rset.next())
   System.out.println (rset.getString(1));
```

The `next()` method returns `false` when it reaches the end of the result set. The employee names are materialized as Java `String` values.

### Closing the Result Set and Statement Objects

You must explicitly close the `ResultSet` and `Statement` objects after you finish using them. This applies to all `ResultSet` and `Statement` objects you create when using Oracle JDBC drivers. The drivers do not have finalizer methods. The cleanup routines are performed by the `close` method of the `ResultSet` and `Statement` classes. If you do not explicitly close the `ResultSet` and `Statement` objects, serious memory leaks could occur. You could also run out of cursors in the database. Closing both the result set and the statement releases the corresponding cursor in the database. If you close only the result set, then the cursor is not released.

For example, if your `ResultSet` object is `rset` and your `Statement` object is `stmt`, then close the result set and statement with the following lines of code:

```
rset.close();
stmt.close();
```

When you close a `Statement` object that a given `Connection` object creates, the connection itself remains open.

Note:

Typically, you should put `close` statements in a `finally` clause.

### Making Changes to the Database

DML Operations

To perform DML (Data Manipulation Language) operations, such as INSERT or UPDATE operations, you can create either a `Statement` object or a `PreparedStatement` object. `PreparedStatement` objects enable you to run a statement with varying sets of input parameters. The `prepareStatement` method of the JDBC `Connection` object lets you define a statement that takes variable bind parameters and returns a JDBC `PreparedStatement` object with your statement definition.

Use the `set` `XXX` methods on the `PreparedStatement` object to bind data to the prepared statement to be sent to the database.

The following example shows how to use a prepared statement to run `INSERT` operations that add two rows to the `EMP` table.

```
// Prepare to insert new names in the EMP table
PreparedStatement pstmt = null;
try{
    pstmt = conn.prepareStatement ("insert into EMP (EMPNO, ENAME) values (?, ?)");

    // Add LESLIE as employee number 1500
    pstmt.setInt (1, 1500);          // The first ? is for EMPNO
    pstmt.setString (2, "LESLIE");   // The second ? is for ENAME
    // Do the insertion
    pstmt.execute ();

    // Add MARSHA as employee number 507
    pstmt.setInt (1, 507);           // The first ? is for EMPNO
    pstmt.setString (2, "MARSHA");   // The second ? is for ENAME
    // Do the insertion
    pstmt.execute ();
}

finally{
                if(pstmt!=null)

    // Close the statement
    pstmt.close();
}
```

DDL Operations

To perform data definition language (DDL) operations, you can create either a `Statement` object or a `PreparedStatement` object. The following example shows how to create a table in the database using a `Statement` object.

```
//create table EMP with columns EMPNO and ENAME
String query;
Statement stmt=null;

try{
    query="create table EMP " +
          "(EMPNO int, " +
          "ENAME varchar(50))";
    stmt = conn.createStatement();
    stmt.executeUpdate(query);
    }
finally{
     //close the Statement object
     stmt.close();
    }
```

If your code involves reexecuting a DDL operation, then, before reexecuting the statement, you must prepare it again. The following example shows how to prepare your DDL statements before any reexecution:

```
//
PreparedStatement pstmt = null;
PreparedStatement tstmt = null;
try{
    pstmt = conn.prepareStatement ("insert into EMP (EMPNO, ENAME) values (?, ?)");
 
    // Add LESLIE as employee number 1500
    pstmt.setInt (1, 1500);          // The first ? is for EMPNO
    pstmt.setString (2, "LESLIE");   // The second ? is for ENAME
    // Do the insertion
    pstmt.execute ();
    
    tstmt = conn.prepareStatement("truncate table EMP"); 
    tstmt.executeUpdate();
 
 
    // Add MARSHA as employee number 507
    pstmt.setInt (1, 507);           // The first ? is for EMPNO
    pstmt.setString (2, "MARSHA");   // The second ? is for ENAME
    // Do the insertion
    pstmt.execute ();
 
    tstmt.close();
    tstmt = conn.prepareStatement("truncate table EMP"); 
    tstmt.executeUpdate();
    }
finally{
if(pstmt!=null)

    // Close the statement
     pstmt.close();
}
```

### Committing Changes

By default, data manipulation language (DML) operations are committed automatically as soon as they are run. This is known as the auto-commit mode. However, you can disable auto-commit mode with the following method call on the `Connection` object:

```
conn.setAutoCommit(false);
```

See Also:

["Disabling Auto-Commit Mode"](apxtips.md).

If you disable the auto-commit mode, then you must manually commit or roll back changes with the appropriate method call on the `Connection` object:

```
conn.commit();
```

or:

```
conn.rollback();
```

A `COMMIT` or `ROLLBACK` operation affects all DML statements run since the last `COMMIT` or `ROLLBACK`.

Note:

- If the auto-commit mode is disabled and you close the connection without explicitly committing or rolling back your last changes, then an implicit `COMMIT` operation is run.
- Any data definition language (DDL) operation always causes an implicit `COMMIT`. If the auto-commit mode is disabled, then this implicit `COMMIT` will commit any pending DML operations that had not yet been explicitly committed or rolled back.

#### Changing Commit Behavior

When a transaction updates the database, it generates a redo entry corresponding to this update. Oracle Database buffers this redo in memory until the completion of the transaction. When you commit the transaction, the Log Writer (LGWR) process writes the redo entry for the commit to disk, along with the accumulated redo entries of all changes in the transaction. By default, Oracle Database writes the redo to disk before the call returns to the client. This behavior introduces latency in the commit because the application must wait for the redo entry to be persisted on disk.

If your application requires very high transaction throughput and you are willing to trade commit durability for lower commit latency, then you can change the behavior of the default `COMMIT` operation, depending on the needs of your application. You can change the behavior of the `COMMIT` operation with the following options:

- `WAIT`
- `NOWAIT`
- `WRITEBATCH`
- `WRITEIMMED`

See Also:

For more information on these options, refer to the Oracle Javadoc at
```
http://download.oracle.com/otn/utilities_drivers/jdbc/111060/doc/javadoc/index.html
```

These options let you control two different aspects of the commit phase:

- Whether the `COMMIT` call should wait for the server to process it or not. This is achieved by using the `WAIT` or `NOWAIT` option.
- Whether the Log Writer should batch the call or not. This is achieved by using the `WRITEIMMED` or `WRITEBATCH` option.

You can also combine different options together. For example, if you want the `COMMIT` call to return without waiting for the server to process it and also the log writer to process the commits in batch, then you can use the `NOWAIT` and `WRITEBATCH` options together. For example:

```
((OracleConnection)conn).commit(
    EnumSet.of(
      OracleConnection.CommitOption.WRITEBATCH,
      OracleConnection.CommitOption.NOWAIT));
```

Note:

you cannot use the `WAIT` and `NOWAIT` options together because they have opposite meanings. If you do so, then the JDBC driver will throw an exception. The same applies to the `WRITEIMMED` and `WRITEBATCH` options.

### Closing the Connection

You must close the connection to the database after you have performed all the required operations and no longer require the connection. You can close the connection by using the `close` method of the `Connection` object, as follows:

```
conn.close();
```

Note:

Typically, you should put `close` statements in a `finally` clause.

## Sample: Connecting, Querying, and Processing the Results

The steps in the preceding sections are illustrated in the following example, which uses the Oracle JDBC Thin driver to create a data source, connects to the database, creates a `Statement` object, runs a query, and processes the result set.

Note that the code for creating the `Statement` object, running the query, returning and processing the `ResultSet` object, and closing the statement and connection uses the standard JDBC API.

```
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;
import oracle.jdbc.pool.OracleDataSource;

class JdbcTest
{
   public static void main (String args []) throws SQLException
   {

OracleDataSource ods = null;
Connection conn = null;
Statement stmt = null;
ResultSet rset = null;

      // Create DataSource and connect to the local database
      ods = new OracleDataSource();
      ods.setURL("jdbc:oracle:thin:@//myhost:1521/orcl");
      ods.setUser("scott");
      ods.setPassword("tiger");
      conn = ods.getConnection();

try
{
      // Query the employee names 
      stmt = conn.createStatement (); 
      rset = stmt.executeQuery ("SELECT ename FROM emp");

      // Print the name out 
      while (rset.next ())
         System.out.println (rset.getString (1));
    }

      //Close the result set, statement, and the connection

finally{
      if(rset!=null) rset.close();
      if(stmt!=null) stmt.close();
      if(conn!=null) conn.close();
}
   } 
}
```

If you want to adapt the code for the OCI driver, then replace the call to the `OracleDataSource.setURL` method with the following:

```
ods.setURL("jdbc:oracle:oci:@MyHostString");
```

where, `MyHostString` is an entry in the `TNSNAMES.ORA` file.

## Stored Procedure Calls in JDBC Programs

This section describes how Oracle JDBC drivers support the following kinds of stored procedures:

- PL/SQL Stored Procedures
- Java Stored Procedures

### PL/SQL Stored Procedures

Oracle JDBC drivers support the processing of PL/SQL stored procedures and anonymous blocks. They support PL/SQL block syntax and most of JDBC escape syntax. The following PL/SQL calls would work with any Oracle JDBC driver:

```
// JDBC escape syntax
CallableStatement cs1 = conn.prepareCall
                       ( "{call proc (?,?)}" ) ; // stored proc
CallableStatement cs2 = conn.prepareCall
                       ( "{? = call func (?,?)}" ) ; // stored func
// PL/SQL block syntax
CallableStatement cs3 = conn.prepareCall
                       ( "begin proc (?,?); end;" ) ; // stored proc
CallableStatement cs4 = conn.prepareCall
                       ( "begin ? := func(?,?); end;" ) ; // stored func
```

As an example of using the Oracle syntax, here is a PL/SQL code snippet that creates a stored function. The PL/SQL function gets a character sequence and concatenates a suffix to it:

```
create or replace function foo (val1 char)
return char as
begin
   return val1 || 'suffix';
end;
```

The function invocation in your JDBC program should look like the following:

```
OracleDataSource ods = new OracleDataSource();
ods.setURL("jdbc:oracle:oci:@<hoststring>");
ods.setUser("scott");
ods.setPassword("tiger");
Connection conn = ods.getConnection();

CallableStatement cs = conn.prepareCall ("begin ? := foo(?); end;");
cs.registerOutParameter(1,Types.CHAR);
cs.setString(2, "aa");
cs.executeUpdate();
String result = cs.getString(1);
```

### Java Stored Procedures

You can use JDBC to call Java stored procedures through the SQL and PL/SQL engines. The syntax for calling Java stored procedures is the same as the syntax for calling PL/SQL stored procedures, presuming they have been properly published. That is, you have written call specifications to publish them to the Oracle data dictionary. Applications can call Java stored procedures using the Native Java Interface for direct invocation of `static` Java methods.

## Processing SQL Exceptions

To handle error conditions, Oracle JDBC drivers throw SQL exceptions, producing instances of the `java.sql.SQLException` class or its subclass. Errors can originate either in the JDBC driver or in the database itself. Resulting messages describe the error and identify the method that threw the error. Additional run-time information can also be appended.

JDBC 3.0 defines only a single exception, `SQLException`. However, there are large categories of errors and it is useful to distinguish them. Therefore, in JDBC 4.0, a set of subclasses of the `SQLException` exception is introduced to identify the different categories of errors. To know more about this feature, see [Support for JDBC 4.0 Standard](jdbcvers.md).

Basic exception handling can include retrieving the error message, retrieving the error code, retrieving the SQL state, and printing the stack trace. The `SQLException` class includes functionality to retrieve all of this information, when available.

See Also:

- [Appendix D, "JDBC Error Messages"](apxermsg.md)
- [Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm)

Retrieving Error Information

You can retrieve basic error information with the following methods of the `SQLException` class:

- `getMessage`
- `getErrorCode`
- `getSQLState`

The following example prints output from a `getMessage` method call:

```
catch(SQLException e)
{
   System.out.println("exception: " + e.getMessage());
}
```

This would print the output, such as the following, for an error originating in the JDBC driver:

```
exception: Invalid column type
```

Note:

Error message text is available in alternative languages and character sets supported by Oracle.

Printing the Stack Trace

The `SQLException` class provides the `printStackTrace()` method for printing a stack trace. This method prints the stack trace of the throwable object to the standard error stream. You can also specify a `java.io.PrintStream` object or `java.io.PrintWriter` object for output.

The following code fragment illustrates how you can catch SQL exceptions and print the stack trace.

```
try { <some code> } 
catch(SQLException e) { e.printStackTrace (); }
```

To illustrate how the JDBC drivers handle errors, assume the following code uses an incorrect column index:

```
// Iterate through the result and print the employee names 
// of the code 
 
try { 
  while (rset.next ()) 
      System.out.println (rset.getString (5));  // incorrect column index
}
catch(SQLException e) { e.printStackTrace (); }
```

Assuming the column index is incorrect, running the program would produce the following error text:

```
java.sql.SQLException: Invalid column index
at oracle.jdbc.driver.OracleResultSetImpl.getDate(OracleResultSetImpl.java:1556)
at Employee.main(Employee.java:41)
```