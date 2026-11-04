---
title: Working with LOBs and BFILEs
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/oralob.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 14 Working with LOBs and BFILEs

This chapter describes how to use Java Database Connectivity (JDBC) to access and manipulate large objects (LOB) using either the data interface or the locator interface.

In previous releases, Oracle JDBC drivers required Oracle extensions to standard JDBC types to perform many operations in the Oracle Database. JDBC 3.0 reduced the requirement of using Oracle extensions and JDBC 4.0 nearly eliminated this limitation. Refer to the Javasoft Javadoc for the `java.sql` and `javax.sql` packages, and to the Oracle JDBC Javadoc for details on Oracle extensions.

This chapter contains the following sections:

## The LOB Data Types

Prior to Oracle Database 10g, the maximum size of a LOB was 2^32 bytes. This restriction has been removed since Oracle Database 10g, and the maximum size is limited to the size of available physical storage.

See Also:

Oracle Database SecureFiles and Large Objects Developer's Guide

The Oracle database supports the following four LOB data types:

- Binary large object (BLOB)
	This data type is used for unstructured binary data.
- Character large object (CLOB)
	This data type is used for character data.
- National character large object (NCLOB)
	This data type is used for national character data.
- BFILE
	This data type is used for large binary data objects stored in operating system files, outside of database tablespaces.

BLOBs, CLOBs, and NCLOBs are stored persistently in a database tablespace and all operations performed on these data types are under transaction control.

BFILE is an Oracle proprietary data type that provides read-only access to data located outside the database tablespaces on tertiary storage devices, such as hard disks, network mounted files systems, CD-ROMs, PhotoCDs, and DVDs. BFILE data is not under transaction control and is not stored by database backups.

The PL/SQL language supports the LOB data types and the JDBC interface allows passing IN parameters to PL/SQL procedures or functions, and retrieval of OUT parameters or returns. PL/SQL uses value semantics for all data types including LOBs, but reference semantics only for BFILE.

## Oracle SecureFiles

Oracle Database 11g Release 1 (11.1) introduced Oracle SecureFiles, a completely new storage for LOBs.

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm)

Following Features of Oracle SecureFiles are transparently available to JDBC programs through the existing APIs:

- SecureFile compression enables users to compress data to save disk space.
- SecureFile encryption introduces a new encryption facility that allows for random reads and writes of the encrypted data.
- Deduplication enables Oracle database to automatically detect duplicate LOB data and conserve space by storing only one copy of data.
- LOB data path optimization includes logical cache above storage layer and new caching modes.
- High performance space management.

The `setLobOptions` and `getLobOptions` APIs are described in the PL/SQL Packages and Types Reference, and may be accessed from JDBC through callable statements.

Following Features of Oracle SecureFiles are implemented in the database through updation to the existing APIs:

- isSecureFile Method
- Zero-Copy I/O for Oracle SecureFiles

isSecureFile Method

Starting from Oracle Database 11g Release 2 (11.2), you can check whether or not your `BLOB` or `CLOB` data uses Oracle SecureFile storage. To achieve this, use the following method from `oracle.sql.BLOB` or `oracle.sql.CLOB` class:

```
public boolean isSecureFile() throws SQLException
```

If this method returns `true`, then your data uses SecureFile storage.

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm)

Zero-Copy I/O for Oracle SecureFiles

With the release of Oracle Database 11g Release 2 (11.2) JDBC Drivers, the performance of Oracle SecureFiles operations is greatly improved because Oracle Net Services now uses zero-copy I/O framework for better buffer management.

Oracle Database 11g Release 2 (11.2) introduces a new connection property `oracle.net.useZeroCopyIO`. This property can be used to enable or disable the zero-copy I/O protocol. This connection property is defined as the following constant: `OracleConnection.CONNECTION_PROPERTY_THIN_NET_USE_ZERO_COPY_IO`. If you want to disable the zero-copy I/O framework, then set the value of this connection property to `false`. By default, the value of this connection property is `true`.

## Data Interface for LOBs

This section describes the following topics:

- Streamlined Mechanism
- Input
- Output
- CallableSatement and IN OUT Parameter
- Size Limitations

### Streamlined Mechanism

The Oracle 11.2 drivers provide a streamlined mechanism for writing and reading the entire LOB contents. This is referred to as the data interface. The data interface uses standard JDBC methods such as `getString` and `setBytes` to read and write LOB data. It is simpler to code and faster in many cases. Unlike the standard `java.sql.Blob`, `java.sql.Clob` and `java.sql.NClob` interfaces, it does not provide random access capability and cannot access data beyond 2147483648 elements.

### Input

In Oracle Database 11g release 2 (11.2), the `setBytes`, `setBinaryStream`, `setString`, `setCharacterStream`, and `setAsciiStream` methods of `PreparedStatement` are extended to enhance the ability to work with `BLOB`, `CLOB`, and `NCLOB` target columns.

Note:

This enhancement does not affect the `BFILE` data because it is read-only.

For the JDBC Oracle Call Interface (OCI) and Thin drivers, there is no limitation on the size of the `byte` array or `String`, and no limitation on the length specified for the stream functions, except the limits imposed by the Java language.

Note:

In Java, the array size is limited to positive Java `int` or 2147483648 elements.

For the server-side internal driver there is currently a limitation of 4000 bytes for operations on SQL statements, such as an `INSERT` statement. This limitation does not apply for PL/SQL statements. There is a simple workaround for an `INSERT` statement, where it is wrapped in a PL/SQL block in the following way:

```
BEGIN
 INSERT id, c INTO clob_tab VALUES(?,?);
END;
```

You must bear in mind the following automatic switching of the input mode for large data:

- There are three input modes as follows:
	- Direct binding
		This binding is limited in size but most efficient. It places the data for all input columns inline in the block of data sent to the server. All data, including multiple executions of a batch, is sent in a single network operation.
		- Stream binding
		This binding places data at the end. It limits batch size to one and may require multiple round trips to complete.
		- LOB binding
		This binding creates a temporary LOB, copies data to the LOB, and binds the LOB locator. The temporary LOB is automatically freed after execution. The operation to create the temporary LOB and then to writing to the LOB requires multiple round trips. The input of the locators may be batched.
- For SQL statements:
	- The `setBytes` and `setBinaryStream` methods use direct binding for data less than 4001 bytes.
		- The `setBytes` and `setBinaryStream` methods use stream binding for data larger than 4000 bytes.
		- In JDBC 4.0 has introduced new forms of the `setAsciiStream`, `setBinaryStream`, and `setCharacterStream` methods. The form, where the methods take a long argument as length, uses LOB binding for length larger than 2147483648. The form, where the length is not specified, always uses LOB binding.
		- The `setString`, `setCharacterStream`, and `setAsciiStream` methods use direct binding for data smaller than 32767 characters.
		- The `setString`, `setCharacterStream`, and `setAsciiStream` methods use stream binding for data larger than 32766 characters.
		- The new form of `setCharacterStream` method, which takes a `long` argument for length, uses LOB binding for length larger than 2147483647, in JDBC 4.0. The form, where the length is not specified, always uses LOB binding.
- PL/SQL statements
	- The `setBytes` and `setBinary` stream methods use direct binding for data less than 32767 bytes.
		Note:
		If the underlying Database is Oracle Database release 10.x, then this data size limit is 32512 bytes, though you are working with 11g release 2 (11.2) JDBC drivers.
		- The `setBytes` and `setBinaryStream` methods use LOB binding for data larger than 32766 bytes.
		- The `setString`, `setCharacterStream`, and `setAsciiStream` methods use direct binding for data smaller than 32767 bytes in the database character set.
		Note:
		If the underlying Database is Oracle Database release 10.x, then this data size limit is 32512 bytes, though you are working with 11g release 2 (11.2) JDBC drivers.
		- The `setString`, `setCharacterStream`, and `setAsciiStream` methods use LOB binding for data larger than 32766 bytes in the database character set.

The automatic switching of the input mode for large data has impact on certain programs. Previously, you used to get `ORA-17157` errors for attempts to use `setString` method for `String` values larger than 32766 characters. Now, depending on the type of the target parameter, an error may occur while the statement is executed or the operation may succeed.

Another impact is that the automatic switching may result in additional server-side parsing to adapt to the change in the parameter type. This would result in a performance effect, if the data sizes vary above and below the limit for repeated executions of the statement. Switching to the stream modes will effect batching as well.

Forcing conversion to LOB

The `setBytesForBlob` and `setStringForClob` methods, present in the `oracle.jdbc.OraclePreparedStatement` interface, use LOB binding for any data size.

The `SetBigStringTryClob` connection property of Oracle Database 10g Release 1 (10.1) is no longer used or needed.

### Output

The `getBytes`, `getBinaryStream`, `getString`, `getCharacterStream`, and `getAsciiStream` methods of `ResultSet` and `CallableStatement` are extended to work with `BLOB`, `CLOB`, and `BFILE` columns or `OUT` parameters. These methods work for any `LOB` of length less than 2147483648.

Note:

The `getString` and `getNString` methods cannot be used for retrieving BLOB column values. For more information about `getNString` method, refer to [New Methods for National Character Set Type Data in JDK 1.6](global.md).

The data interface operates by accessing the `LOB` locators within the driver and is transparent to application programming. It works with any supported version of the database, that is, Oracle Database 9.2 and later. For database version 11.1 or later, LOB prefetching may be used to reduce or eliminate any additional database round trips required. For more information, refer to LOB prefetching.

`BLOB` or `CLOB` data can be read and written using the same streaming mechanism as for `LONG` `RAW` and `LONG` data. `BFILE` data can be read using the same streaming mechanism. To read, use `defineColumnType(nn,` `Types.LONGVARBINARY)` or `defineColumnType(nn,Types.LONGVARCHAR)` method on the column. This produces a direct stream on the data as if it were a `LONG RAW` or `LONG` column. This technique is limited to Oracle Database 10g release 1 (10.1) and later.

### CallableSatement and IN OUT Parameter

It is a PL/SQL requirement that the Java types used as input and output for an IN OUT parameter must be the same. The automatic switching of types done by the extensions described in this chapter may cause problems with this.

Consider that you have an `IN` `OUT` `CLOB` parameter of a stored procedure and you wish to use `setString` method for setting the value for this parameter. For any `IN` and `OUT` parameter, the binds must be of the same type. The automatic switching of the input mode will cause problems unless you are sure of the data sizes. For example, if it is known that neither the input nor output data will ever be larger than 32766 bytes, then you could use `setString` method for the input parameter and register the `OUT` parameter as `Types.VARCHAR` and use `getString` method for the output parameter.

A better solution is to change the stored procedure to have separate `IN` and `OUT` parameters. That is, if you have:

```
CREATE PROCEDURE clob_proc( c IN OUT CLOB );
```

then, change it to:

```
CREATE PROCEDURE clob_proc( c_in IN CLOB, c_out OUT CLOB );
```

Another workaround is to use a container block to make the call. The `clob_proc` procedure can be wrapped with a Java String to use for the `prepareCall` statement, as follows:

```
"DECLARE c_temp; BEGIN c_temp := ?; clob_proc( c_temp); ? := c_temp; END;"
```

In either case, you may use the `setString` method on the first parameter and the `registerOutParameter` method with `Types.CLOB` on the second.

### Size Limitations

Be aware of the effect on the performance of the Java memory management system due to creation of very large `byte` array or `String`. Read the information provided by your Java virtual machine (JVM) vendor about the impact of very large data elements on memory management, and consider using the stream interfaces instead.

## LOB Locator Interface

Locators are small data structures, which contain information that may be used to access the actual data of the LOB. In a database table, the locator is stored directly in the table, while the data may be in the table or in separate storage. It is common to use separate tablespaces for large LOBs.

In JDBC 4.0, LOBs should be read or written using the interfaces `java.sql.Blob`, `java.sql.Clob`, and `java.sql.NClob`. These provide random access to the data in the LOB.

The Oracle implementation classes `oracle.sql.BLOB`, `oracle.sql.CLOB`, and `oracle.sql.NCLOB` store the locator and access the data with it. The `oracle.sql.BLOB` and `oracle.sql.CLOB` classes implement the `java.sql.Blob` and `java.sql.Clob` interfaces respectively. In `ojdbc6.jar`, `oracle.sql.NCLOB` implements `java.sql.NClob`, but in `ojdbc5.jar`, it implements the `java.sql.Clob` interface.

In Oracle Database 11g, the Oracle JDBC drivers support the JDBC 4.0 `java.sql.NClob` interface in `ojdbc6.jar`, which is compiled with JDK 1.6 and must be used with JRE 6 or greater. The drivers support the JDBC 3.0 standard in `ojdbc5.jar`, which must be used with JRE 5 or greater.

In contrast, `oracle.sql.BFILE` is an Oracle extension, without a corresponding `java.sql` interface.

Certain Oracle extensions, such as some of the read and write methods present in the `oracle.sql.CLOB` and `oracle.sql.BLOB` interfaces, in earlier Oracle Database releases are no longer necessary and are deprecated. You should port your application to the standard JDBC 3.0 interface or to JDBC 4.0 interface, if you are using JDK 1.6 or above, and `ojdbc6.jar`.

See Also:

The Javadoc for more details

LOB prefetching

For Oracle Database 11g Release 2 (11.2) JDBC drivers, the number of round trips is reduced by prefetching the metadata such as the LOB length and the chunk size as well as the beginning of the LOB data along with the locator during regular fetch operations. If you select LOB columns into a result set, a new capability in the server and JDBC drivers allow some or all of the data to be prefetched to the client, when the locator is fetched. Subsequent read API calls will get the data from the prefetch buffers without any need to make database round trips.

The prefetch size is specified in bytes for BLOBs and in characters for CLOBs. It can be specified by setting the connection property `oracle.jdbc.defaultLobPrefetchSize`. The value of this property can be overridden in the following two ways:

- At the statement level: by using the `oracle.jdbc.OracleStatement.setLobPrefetchSize(int)` method
- At the column level: by using the form of `defineColumnType` method that takes length as argument

The default prefetch size is 4000.

Note:

Be aware of the possible memory consumption while setting large LOB prefetch sizes in combination with a large row prefetch size and a large number of LOB columns.

See Also:

The Javadoc for more details

New LOB APIs in JDBC 4.0

Starting from Oracle Database 11g Release 1 (11.1), there is a new interface `java.sql.NClob`. The Oracle drivers implement the `oracle.sql.NCLOB` interface in both `ojdbc5.jar` and `ojdbc6.jar`. In `ojdbc6.jar`, it is declared to implement `java.sql.NClob`, whereas in `ojdbc5.jar`, it only extends the `oracle.sql.CLOB` interface.

The Oracle drivers implement the new factory methods, `createBlob`, `createClob`, and `createNClob` in the `java.sql.Connection` interface to create temporary LOBs.

Starting from JDK 1.6, the `java.sql.Blob`, `java.sql.Clob`, and `java.sql.NClob` interfaces have a new method `free` to free an LOB and release the associated resources. The Oracle drivers use this method to free an LOB, if it is a temporary LOB.

## Working With Temporary LOBs

You can use temporary LOBs to store transient data. The data is stored in temporary table space rather than regular table space. You should free temporary LOBs after you no longer need them. If you do not, then the space the LOB consumes in temporary table space will not be reclaimed.

You can insert temporary LOBs into a table. When you do this, a permanent copy of the LOB is created and stored.

Note:

Inserting a temporary LOB may be preferable in some situations. For example, when the LOB data is relatively small and the overhead of copying the data is less than the cost of a database round trip to retrieve the empty locator. Remember that the data is initially stored in the temporary table space on the server and then moved into permanent storage.

You create a temporary LOB with the `static` method `createTemporary`, defined in both the `oracle.sql.BLOB` and `oracle.sql.CLOB` classes. You free a temporary LOB with the `freeTemporary` method.

You can also create a temporary LOB by using the connection factory methods available in JDBC 4.0. For more information, refer to ["LOB Creation"](jdbcvers.md).

You can test whether a LOB is temporary or not by calling the `isTemporary` method. If the LOB was created by calling the `createTemporary` method, then the `isTemporary` method returns `true`, else it returns `false`.

You can free a temporary LOB by calling the `freeTemporary` method. Free any temporary LOBs before ending the session or call.

Notes:

- If you do not free a temporary LOB, then it will make the storage used by that LOB in the database unavailable. Frequent failure to free temporary LOBs will result in filling up temporary table space with unavailable LOB storage.
- When fetching data from a `ReultSet` with columns that are temporary LOBs, use `getClob` or `getBlob` methods instead of `getString` or `getBytes`.
- The JDBC 4.0 method `free`, present in `java.sql.Blob`, `java.sql.Clob`, and `java.sql.NClob` interfaces, supercedes the `freeTemporary` method.

Creating Temporary NCLOBs in JDK 1.5

You create temporary national character large objects (NCLOBs) using a variant of the `createTemporary` method.

Creating Temporary NCLOBs in JDK 1.6

JDBC 4.0 supports NCLOBs directly. You can use the standard factory method of `java.sql.Connection` interface to create an NCLOB.

## Opening Persistent LOBs with the Open and Close Methods

This section discusses how to open and close your LOBs. The JDBC implementation of this functionality is provided using the following methods of `oracle.sql.BLOB` and `oracle.sql.CLOB` interfaces:

Note:

You do not have to necessarily open and close your LOBs. You may choose to open and close them for performance reasons.

See Also:

Oracle Database SecureFiles and Large Objects Developer's Guide
- `void open (int mode)`
- `void close()`
- `boolean isOpen()`

If you do not wrap LOB operations inside an `Open/Close` call operation, then each modification to the LOB will implicitly open and close the LOB, thereby firing any triggers on a domain index. Note that in this case, any domain indexes on the LOB will become updated as soon as LOB modifications are made. Therefore, domain LOB indexes are always valid and may be used at any time within the same transaction.

If you wrap your LOB operations inside the `Open/Close` call operation, then triggers will not be fired for each LOB modification. Instead, the trigger on domain indexes will be fired at the `Close` call. For example, you might design your application so that domain indexes are not be updated until you call the `close` method. However, this means that any domain indexes on the LOB will not be valid in-between the `Open/Close` calls.

You open a LOB by calling the `open` or `open(int)` method. You may then read and write the LOB without any triggers associated with that LOB firing. When you finish accessing the LOB, close the LOB by calling the `close` method. When you close the LOB, any triggers associated with the LOB will fire.

You can check if a LOB is open or closed by calling the `isOpen` method. If you open the LOB by calling the `open(int)` method, then the value of the argument must be either `MODE_READONLY` or `MODE_READWRITE`, as defined in the `oracle.sql.BLOB` and `oracle.sql.CLOB` classes. If you open the LOB with `MODE_READONLY`, then any attempt to write to the LOB will result in a SQL exception.

Note:

- An error occurs if you commit the transaction before closing all LOBs that were opened by the transaction. The openness of the open LOBs is discarded, but the transaction is successfully committed. Hence, all the changes made to the LOB and non-LOB data in the transaction are committed, but the triggers for domain indexing are not fixed.
- The `open` and `close` methods apply only to persistent LOBs. The `close` method is not similar to the `free` or `freeTemporary` methods used for temporary LOBs. The `free` and `freeTemporary` methods release storage and make a LOB unusable. On the other hand, the `close` method indicates to the database that a modification on a LOB is complete, and triggers should be fired and indexes should be updated. A LOB is still usable after a call to the `close` method.

## Working with BFILEs

This section describes how to read data from BFILEs, using file locators. This section covers the following topics:

- Retrieving BFILE Locators
- Writing to BFILES

Retrieving BFILE Locators

The BFILE data type and `oracle.sql.BFILE` classes are Oracle proprietary. So, there is no standard interface for them. You must use Oracle extensions for this type of data.

If you have a standard JDBC result set or callable statement object that includes BFILE locators, then you can access the locators by using the standard result set `getObject` method. This method returns an `oracle.sql.BFILE` object.

You can also access the locators by casting your result set to `OracleResultSet` or your callable statement to `OracleCallableStatement` and using the `getOracleObject` or `getBFILE` method.

Note:

If you are using `getObject` or `getOracleObject` methods, then remember to cast the output, as necessary.

Once you have a locator, you can access the BFILE data via the API in `oracle.sql.BFILE`. These APIs are similar to the read methods of the `java.sql.BLOB` interface.

Writing to BFILES

You cannot write data to the contents of the BFILE, but you can use an instance of `oracle.sql.BFILE` as input to a SQL statement or to a PL/SQL procedure. You can achieve this by performing one of the following:

- Use the standard `setObject` method.
- Cast the statement to `OraclePreparedStatement` or `OracleCallableStatement`, and use the `setOracleObject` or `setBFILE` method. These methods take the parameter index and an `oracle.sql.BFILE` object as input.
	Note:
	- There is no standard `java.sql` interface for BFILEs.
	- Use the `getBFILE` methods in the `OracleResultSet` and `OracleCallableStatement` classes to retrieve an `oracle.sql.BFILE` object. The `setBFILE` methods in `OraclePreparedStatement` and `OracleCallableStatement` interfaces accept `oracle.sql.BFILE` object as an argument. Use these methods to write to a BFILE.
	- Oracle recommends that you use the `getBFILE`, `setBFILE`, and `updateBFILE` methods instead of the `getBfile`, `setBfile`, and `updateBfile` methods. For example, use the `setBFILE` method instead of the `setBfile` method.

BFILEs are read-only. The body of the data resides in the operating system (OS) file system and can be written to using only OS tools and commands. You can create a BFILE for an existing external file by executing the appropriate SQL statement either from JDBC or by using any other way to execute SQL. However, you cannot create an OS file that a BFILE would refer to by SQL or JDBC. Those are created only externally by a process that has access to server file systems.

Note:

- The code examples present in this chapter, in the earlier versions of this guide, have been removed in favor of references to the sample code available for download on OTN.
- You can download the `demo.zip` file from the following link for complete working programs:
	```
	http://www.oracle.com/technology/tech/java/sqlj_jdbc/index.html
	```