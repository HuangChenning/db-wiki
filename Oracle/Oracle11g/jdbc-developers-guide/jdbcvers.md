---
title: JDBC Standards Support
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/jdbcvers.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 3 JDBC Standards Support

The Oracle Java Database Connectivity (JDBC) drivers support different versions of the JDBC standard features. In Oracle Database 11g Release 2 (11.2), Oracle JDBC drivers have been enhanced to provide support for the JDBC 4.0 standards. These features are provided through the `oracle.jdbc` and `oracle.sql` packages. These packages support Java Development Kit (JDK) releases 1.5 and 1.6. This chapter discusses the JDBC standards support in Oracle JDBC drivers. It contains the following sections:

## Support for JDBC 2.0 Standard

Standard JDBC 2.0 features are supported by JDK 1.2 and later versions. There are three areas to consider:

- Support for data types, such as objects, arrays, and large objects (LOBs). This is handled through the standard `java.sql` package.
- Support for standard features, such as result set enhancements and update batching. This is handled through standard objects, such as `Connection`, `ResultSet`, and `PreparedStatement`, under JDK 1.2.x and later.
- Support for extended features, such as features of the JDBC 2.0 optional package, also known as the standard extension application programming interface (API), including data sources, connection pooling, and distributed transactions.

This section covers the following topics:

- Data Type Support
- Standard Feature Support
- Extended Feature Support
- Standard versus Oracle Performance Enhancement APIs

Note:

Versions of JDK earlier than 1.5 are no longer supported. The package `oracle.jdbc2` has been removed.

### Data Type Support

Oracle JDBC fully supports JDK 1.5 and JDK 1.6, which includes standard JDBC 2.0 functionality through implementation of interfaces in the standard `java.sql` package. These interfaces are implemented as appropriate by classes in the `oracle.sql` and `oracle.jdbc` packages.

### Standard Feature Support

In a JDK 1.5 environment, using the JDBC classes in `ojdbc5.jar`, JDBC 2.0 features, such as scrollable result sets, updatable result sets, and update batching, are supported through methods specified by standard JDBC 2.0 interfaces.

### Extended Feature Support

Features of the JDBC 2.0 optional package, including data sources, connection pooling, and distributed transactions, are supported in a JDK 1.2.x or later environment.

The standard `javax.sql` package and classes that implement its interfaces are included in the Java Archive (JAR) files packaged with Oracle Database.

### Standard versus Oracle Performance Enhancement APIs

The following performance enhancements are available under JDBC 2.0, which had previously been available only as Oracle extensions:

- Update batching
- Fetch size or row prefetching

In each case, you have the option of using the standard model or the Oracle model. Oracle recommends that you use the JDBC standard model whenever possible. Do not, however, try to mix usage of the standard model and Oracle model within a single application for either of these features.

See Also:

- ["Update Batching"](oraperf.md)
- ["Fetch Size"](resltset.md)

## Support for JDBC 3.0 Standard

Standard JDBC 3.0 features are supported by JDK 1.4 and later versions. Table 3-1 lists the JDBC 3.0 features supported by Oracle Database 11g Release 2 (11.2) and gives references to a detailed discussion of each feature.

Table 3-1 Key Areas of JDBC 3.0 Functionality

| Feature | Comments and References |
| --- | --- |
| Transaction savepoints | See "Transaction Savepoints" for information. |
| Statement caching | Reuse of prepared statements by connection pools. See [Chapter 20, "Statement and Result Set Caching"](stmtcach.md). |
| Switching between local and global transactions | See ["Switching Between Global and Local Transactions"](xadistra.md). |
| LOB modification | See "JDBC 3.0 LOB Interface Methods". |
| Named SQL parameters | See ["Interface oracle.jdbc.OracleCallableStatement"](oraint.md) and ["Interface oracle.jdbc.OraclePreparedStatement"](oraint.md). |
| RowSets | See [Chapter 18, "JDBC RowSets"](jcrowset.md) |
| Retrieving auto-generated keys | See "Retrieval of Auto-Generated Keys" |
| Result set holdability | See "Result Set Holdability" |

The following JDBC 3.0 features supported by Oracle JDBC drivers are covered in this section:

- Transaction Savepoints
- Retrieval of Auto-Generated Keys
- JDBC 3.0 LOB Interface Methods
- Result Set Holdability

### Transaction Savepoints

The JDBC 3.0 specification supports savepoints, which offer finer demarcation within transactions. Applications can set a savepoint within a transaction and then roll back all work done after the savepoint. Savepoints relax the atomicity property of transactions. A transaction with a savepoint is atomic in the sense that it appears to be a single unit outside the context of the transaction, but code operating within the transaction can preserve partial states.

Note:

Savepoints are supported for local transactions only. Specifying a savepoint within a global transaction causes a `SQLException` exception to be thrown.

#### Creating a Savepoint

You create a savepoint using the `Connection.setSavepoint` method, which returns a `java.sql.Savepoint` instance.

A savepoint is either named or unnamed. You specify the name of a savepoint by supplying a string to the `setSavepoint` method. If you do not specify a name, then the savepoint is assigned an integer ID. You retrieve a name using the `getSavepointName` method. You retrieve an ID using the `getSavepointId` method.

Note:

Attempting to retrieve a name from an unnamed savepoint or attempting to retrieve an ID from a named savepoint throws a `SQLException` exception.

#### Rolling Back to a Savepoint

You roll back to a savepoint using the `Connection.rollback(Savepoint svpt)` method. If you try to roll back to a savepoint that has been released, then a `SQLException` exception is thrown.

#### Releasing a Savepoint

You remove a savepoint using the `Connection.releaseSavepoint(Savepoint svpt)` method.

#### Checking Savepoint Support

You query if savepoints are supported by your database by calling the `oracle.jdbc.OracleDatabaseMetaData.supportsSavepoints` method, which returns `true` if savepoints are available, `false` otherwise.

#### Savepoint Notes

When using savepoints, you must consider the following:

- After a savepoint has been released, attempting to reference it in a rollback operation will cause a `SQLException` exception to be thrown.
- When a transaction is committed or rolled back, all savepoints created in that transaction are automatically released and become invalid.
- Rolling a transaction back to a savepoint automatically releases and makes invalid any savepoints created after the savepoint in question.

### Retrieval of Auto-Generated Keys

Many database systems automatically generate a unique key field when a row is inserted. Oracle Database provides the same functionality with the help of sequences and triggers. JDBC 3.0 introduces the retrieval of auto-generated keys feature that enables you to retrieve such generated values. In JDBC 3.0, the following interfaces are enhanced to support the retrieval of auto-generated keys feature:

- `java.sql.DatabaseMetaData`
- `java.sql.Connection`
- `java.sql.Statement`

These interfaces provide methods that support retrieval of auto-generated keys. However, this feature is supported only when `INSERT` statements are processed. Other data manipulation language (DML) statements are processed, but without retrieving auto-generated keys.

Note:

The Oracle server-side internal driver does not support the retrieval of auto-generated keys feature.

#### java.sql.Statement

If key columns are not explicitly indicated, then Oracle JDBC drivers cannot identify which columns need to be retrieved. When a column name or column index array is used, Oracle JDBC drivers can identify which columns contain auto-generated keys that you want to retrieve. However, when the `Statement.RETURN_GENERATED_KEYS` integer flag is used, Oracle JDBC drivers cannot identify these columns. When the integer flag is used to indicate that auto-generated keys are to be returned, the `ROWID` pseudo column is returned as key. The `ROWID` can be then fetched from the `ResultSet` object and can be used to retrieve other columns.

#### Sample Code

The following code illustrates retrieval of auto-generated keys:

```
/** SQL statements for creating an ORDERS table and a sequence for generating the
  * ORDER_ID.
  *
  * CREATE TABLE ORDERS (ORDER_ID NUMBER, CUSTOMER_ID NUMBER, ISBN NUMBER,
  * DESCRIPTION NCHAR(5))
  *
  * CREATE SEQUENCE SEQ01 INCREMENT BY 1 START WITH 1000
  */

...
String cols[] = {"ORDER_ID", "DESCRIPTION"};

// Create a PreparedStatement for inserting a row into the ORDERS table.
OraclePreparedStatement pstmt = (OraclePreparedStatement)
conn.prepareStatement("INSERT INTO ORDERS (ORDER_ID, CUSTOMER_ID, ISBN,  DESCRIPTION) VALUES (SEQ01.NEXTVAL, 101,
 966431502, ?)", cols);
char c[] = {'a', '\u5185', 'b'};
String s = new String(c);
pstmt.setNString(1, s);
pstmt.executeUpdate();
ResultSet rset = pstmt.getGeneratedKeys();
...
```

In the preceding example, a sequence, `SEQ01`, is created to generate values for the `ORDER_ID` column starting from `1000` and incrementing by `1` each time the sequence is processed to generate the next value. An `OraclePreparedStatement` object is created to insert a row in to the `ORDERS` table.

#### Limitations

Auto-generated keys are implemented using the DML returning clause. So, they are subjected to the following limitations:

- You cannot combine auto-generated keys with batch update.
- You need to access the `ResultSet` object returned from `getGeneratedKeys` method by position only and no bind variable names should be used as columns in the `ResultSet` object.

### JDBC 3.0 LOB Interface Methods

Table 3-2 and Table 3-3 show the conversions between Oracle proprietary methods and JDBC 3.0 standard methods.

Table 3-2 BLOB Method Equivalents

| Oracle Proprietary Method | JDBC 3.0 Standard Method |
| --- | --- |
| `putBytes(long pos, byte [] bytes)` | `setBytes(long pos, byte[] bytes)` |
| `putBytes(long pos, byte [] bytes, int length)` | `setBytes(long pos, byte[] bytes, int offset, int len)` |
| `getBinaryOutputStream(long pos)` | `setBinaryStream(long pos)` |
| `trim (long len)` | `truncate(long len)` |

Table 3-3 CLOB Method Equivalents

| Oracle Proprietary Method | JDBC 3.0 Standard Method |
| --- | --- |
| `putString(long pos, String str)` | `setString(long pos, String str)` |
| not applicable | `setString(long pos, String str, int offset, int len)` |
| `getAsciiOutputStream(long pos)` | `setAsciiStream(long pos)` |
| `getCharacterOutputStream(long pos)` | `setCharacterStream(long pos)` |
| `trim (long len)` | `truncate(long len)` |

### Result Set Holdability

Result set holdability was introduced since JDBC 3.0. This feature enables applications to decide whether the `ResultSet` objects should be open or closed, when a commit operation is performed. The commit operation could be either implicit or explicit.

Oracle Database supports only `HOLD_CURSORS_OVER_COMMIT`. Therefore, it is the default value for Oracle JDBC drivers. Any attempt to change holdability will throw a `SQLException` exception.

## Support for JDBC 4.0 Standard

The JDBC 4.0 standard support is provided by JDK 1.6 and later versions. Oracle Database 11g Release 2 (11.2) JDBC drivers provide support for the JDBC 4.0 standard.

Note:

- You need to have the `ojdbc6.jar` in your `classpath` environment variable in order to have JDBC 4.0 standard support.
- The JDBC 4.0 specification defines the `getClientInfo` and `setClientInfo` methods to get and set client information. The 11.2 Oracle JDBC drivers do not define any client information, so any call to these methods throws a `SQLClientInfoException` exception.
- The JDBC 4.0 specification defines the `java.sql.Connection.createArrayOf` factory method to create `java.sql.Array` objects. The `createArrayOf` method accepts the name of the array element type as one of the arguments, where the array type is anonymous. Oracle database supports only named array types, not anonymous array types. So, the 11.2 Oracle JDBC drivers do not and cannot support the `createArrayOf` method. You must use the Oracle specific `createARRAY` method to create an array type. For more information about the `createArrayOf` method, refer to ["Creating ARRAY Objects"](oraarr.md).
- This document provides only an overview of these new features. For detailed information about these features, see "Java 2 Platform, Standard Edition (JSE) 6.0 specification" at
	```
	http://download.oracle.com/javase/6/docs/
	```

Some of the features available in Oracle Database 11g Release 2 (11.2) JDBC drivers are the following:

- Wrapper Pattern Support
- SQLXML Type
- Enhanced Exception Hierarchy and SQLException
- The RowId Data Type
- LOB Creation
- National Language Character Set Support

### Wrapper Pattern Support

Wrapper pattern is a common coding pattern used in Java applications to provide extensions beyond the traditional JDBC API that are specific to a data source. You may need to use these extensions to access the resources that are wrapped as proxy class instances representing the actual resources. JDBC 4.0 introduces the `Wrapper` interface that describes a standard mechanism to access these wrapped resources represented by their proxy, to permit direct access to the resource delegates.

The `Wrapper` interface provides the following two methods:

- `public boolean isWrapperFor(Class<?> iface) throws SQLException;`
- `public <T> T unwrap(Class<T> iface) throws SQLException;`

The other JDBC 4.0 interfaces, except those that represent SQL data, all implement this interface. These include `Connection`, `Statement` and its subtypes, `ResultSet`, and the metadata interfaces.

See Also:

`http://download.oracle.com/javase/6/docs/api/java/sql/Wrapper.html`

### SQLXML Type

One of the most important updates in JDBC 4.0 standard is the support for the XML data type, defined by the SQL 2003 standard. Now JDBC offers a mapping interface to support the SQL/XML database data type, that is, `java.sql.SQLXML`. This new JDBC interface defines Java native bindings for XML, thus making handling of any database XML data easier and more efficient.

Note:

- You also need to include the `xdb.jar` and `xmlparserv2.jar` files in the `classpath` environment variable to use `SQLXML` type data, if they are not already present in the `classpath`.
- SQLXML is not supported in `CachedRowset` objects.

You can create an instance of XML by calling the `createSQLXML` method in `java.sql.Connection` interface. This method returns an empty XML object.

The `PreparedStatement`, `CallableStatement`, and `ResultSet` interfaces have been extended with the appropriate getter and setter methods in the following way:

- `PreparedStatement`: The method `setSQLXML` have been added
- `CallableStatement`: The methods `getSQLXML` and `setSQLXML` have been added
- `ResultSet`: The method `getSQLXML` have been added

The oracle.jdbc.getObjectReturnsXMLType Property

In Oracle Database 10g and earlier versions of Oracle Database 11g, Oracle JDBC drivers supported the Oracle SQL XML type (XMLType) through an Oracle proprietary extension. XML values were represented by instances of the `oracle.xdb.XMLType` class and the SQL XMLType values were read and set through the JDBC standard `getObject`, `setObject`, and `updateObject` methods.

The JDBC standard requires the `getObject` method to return an instance of `java.sql.SQLXML` type when called on a SQL XML type column. But, the earlier versions of Oracle JDBC drivers return an instance of `oracle.xdb.XMLType`. This does not conform to the JDBC standard.

The current release of Oracle JDBC drivers conform to the JDBC standard with the introduction of a new connection property, `oracle.jdbc.getObjectReturnsXMLType`. If you set this property to `false`, then the `getObject` method returns an instance of `java.sql.SQLXML` type. You can achieve this by using the following command line option while compiling your program with `javac`:

```
-Doracle.jdbc.getObjectReturnsXMLType="false"
```

If you depend on the existing Oracle proprietary support for SQL XMLType using `oracle.xdb.XMLType`, then you can change the value of this property back to `true` by using the following command line option:

```
-Doracle.jdbc.getObjectReturnsXMLType="true"
```

The value of the `oracle.jdbc.getObjectReturnsXMLType` property is a `String` representing a boolean value of either `true` or `false`. If the value of this property is `true`, then the `getObject` method returns `oracle.xdb.XMLType` instances, when called for a SQL XMLType column. This is the deafault value of the `oracle.jdbc.getObjectReturnsXMLType` property. If the value of this property is `false`, then the `getObject` method returns `java.sql.SQLXML` instances. This is the standard JDBC-compliant mode.

Note:

The `oracle.jdbc.getObjectReturnsXMLType` property affects only the result of the `getObject` method. All other methods conform to the JDBC 4.0 standard regardless of the value of the property.

Example

Example 3-1 Accessing SQLXML Data

The following example shows how to create an instance of XML from a `String`, write the XML data into the Database, and then retrieve the XML data from the Database.

```
import java.sql.*;
import java.util.Properties;
import oracle.jdbc.pool.OracleDataSource;
 
public class SQLXMLTest
 {
 
  public static void main(String[] args) 
  {
  
  Connection conn = null;
  Statement stmt = null;
  ResultSet rs = null;
  PreparedStatement ps = null;
  
  String xml = "<?xml version=\"1.0\"?>\n" +
    "<oldjoke>\n" +
    "<burns>Say <quote>goodnight</quote>, Gracie.</burns>\n" +
    "<allen><quote>Goodnight, Gracie.</quote></allen>\n" +
    "<applause/>\n" +
    "</oldjoke>";
 
  try
  {
 
     OracleDataSource ods = new OracleDataSource();
     ods.setURL("jdbc:oracle:thin:@//localhost:1521/orcl");
     ods.setUser("scott");
     ods.setPassword("tiger");
     conn = ods.getConnection();
 
     ps = conn.prepareStatement("insert into x values (?, ?)");
     ps.setString(1, "string to string");
     SQLXML x = conn.createSQLXML();
     x.setString(xml);
     ps.setSQLXML(2, x);
     ps.execute();
     x.free();
     stmt = conn.createStatement();
     rs = stmt.executeQuery("select * from x");
     while (rs.next()) 
     {
 
       System.out.println(rs.getString(1) + "\n" + rs.getSQLXML(2).getString());
     }
 
     rs.close();
     ps.close();    
  }
 
  catch (SQLException e){e.printStackTrace ();}
 
  }
}
```

Note:

Calling a setter method with an empty XML throws `SQLException`. The getter methods never return an empty XML.

See Also:

JSR 173: Streaming API for XML at:

`http://www.jcp.org/aboutJava/communityprocess/first/jsr173/`

### Enhanced Exception Hierarchy and SQLException

JDBC 3.0 defines only a single exception, `SQLException`. However, there are large categories of errors and it is useful to distinguish them. This feature provides subclasses of the `SQLException` class to identify the different categories of errors. The primary distinction is between permanent errors and transient errors. Permanent errors are a result of the correct operation of the system and will always occur. Transient errors are the result of failures, including timeouts, of some part of the system and may not reoccur.

JDBC 4.0 adds additional exceptions to represent transient and permanent errors and the different categories of these errors.

Also, the `SQLException` class and its subclasses are enhanced to provide support for the J2SE chained exception functionality.

### The RowId Data Type

JDBC 4.0 provides the `java.sql.RowId` data type to represent SQL `ROWID` values. You can retrieve a `RowId` value using the getter methods defined in the `ResultSet` and `CallableStatement` interfaces. You can also use a `RowId` value in a parameterized `PreparedStatement` to set a parameter with a `RowId` object or in an updatable result set to update a column with a specific `RowId` value.

A `RowId` object is valid until the identified row is not deleted. A `RowId` object may also be valid for the following:

- The duration of the transaction in which it is created
- The duration of the session in which it is created
- An undefined duration where by it is valid forever

The lifetime of the RowId object can be determined by calling the `DatabaseMetaData.getRowIdLifetime` method.

### LOB Creation

In JDBC 4.0, the `Connection` interface has been enhanced to provide support for the creation of `BLOB`, `CLOB`, and `NCLOB` objects. The interface provides the `createBlob`, `createClob`, and `createNClob` methods that enable you to create `Blob`, `Clob`, and `NClob` objects.

The created large objects (LOBs) do not contain any data. You can add or retrieve data to or from these objects by calling the APIs available in the `java.sql.Blob`, `java.sql.Clob`, and `java.sql.NClob` interfaces. You can either retrieve the entire content or a part of the content from these objects. The following code snippet illustrates how to retrieve 100 bytes of data from a `BLOB` object starting at offset 200:

```
...
Connection con = DriverManager.getConnection(url, props);
Blob aBlob = con.createBlob();
// Add data to the BLOB object.
aBlob.setBytes(...);
...
// Retrieve part of the data from the BLOB object.
InputStream is = aBlob.getBinaryStream(200, 100);
...
```

You can also pass LOBs as input parameters to a `PreparedStatement` object by using the `setBlob`, `setClob`, and `setNClob` methods. You can use the `updateBlob`, `updateClob`, and `updateNClob` methods to update a column value in an updatable result set.

These LOBs are temporary LOBs and can be used for any purpose for which temporary LOBs should be used. To make the storage permanent in the database, these LOBs must be written to a table.

See Also:

["Working With Temporary LOBs"](oralob.md)

Temporary LOBs remain valid for at least the duration of the transaction in which they are created. This may result in unwarranted use of memory during a long running transaction. You can release LOBs by calling their `free` method, as follows:

```
...
Clob aClob = con.createClob();
int numWritten = aClob.setString(1, val);
aClob.free();
...
```

### National Language Character Set Support

JDBC 4.0 introduces the `NCHAR`, `NVARCHAR`, `LONGNVARCHAR`, and `NCLOB` JDBC types to access the national character set types. These types are similar to the `CHAR`, `VARCHAR`, `LONGVARCHAR`, and `CLOB` types, except that the values are encoded using the national character set.