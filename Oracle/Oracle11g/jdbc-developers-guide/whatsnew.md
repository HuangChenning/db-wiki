---
title: "What's New"
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/whatsnew.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

This chapter describes the new features in Oracle Database 11g Release 2 (11.2) JDBC drivers.

## New Features for Release 2 (11.2)

In this release, Oracle JDBC drivers support the following new features:

### SQLXML Support

This release of Oracle JDBC drivers provides a mapping interface to support the SQL/XML database data type. For more information about SQL/XML database data type, refer to ["SQLXML Type"](jdbcvers.md).

### Timestamp and Time Zone improvement

This release of Oracle JDBC drivers provides a newly designed time zone cache to address the issues related to version incompatibility of time zones. For more information refer to ["Overview of Classes oracle.sql.TIMESTAMP, oracle.sql.TIMESTAMPTZ, and oracle.sql.TIMESTAMPLTZ"](oraint.md).

### LOB Prefetching Support

This release of Oracle JDBC drivers improves the performance of LOB operations by reducing the number of round trips to the database. For more information refer to ["Prefetching LOB Data"](oraperf.md).

### Zero-copy I/O for Oracle SecureFiles

This release of JDBC drivers provides faster LOB operations by using zero-copy I/O framework. For more information refer to ["Zero-Copy I/O for Oracle SecureFiles"](oralob.md).

### Setting Session Edition for a Connection

Starting from this release of Oracle JDBC drivers, when you connect to the Database, you can specify the session edition in your code along with user name, password, System privileges, and connection identifier. For more information, refer to [Oracle Database JDBC Java API Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e13995/toc.htm).

See Also:

[Oracle Database Advanced Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e41502/adfns_editions.htm#ADFNS020) for more information about session editions

### Internet Protocol Version 6 Support (IPv6)

This release of Oracle JDBC drivers supports Internet Protocol Version 6 (IPv6) addresses. For more information refer to ["Internet Protocol Version 6 Support"](urls.md).

Note:

All the new System classes that are required for IPv6 support are loaded when Java is enabled during database initialization. So, if your application does not have any IPv6 addressing, then you do not need to change your code to use IPv6 functionality. However, if your application has either IPv6 only or both IPv6 and IPv4 addressing, then you should set the `java.net.preferIPv6Addresses` system property in the command line. This enables the Oracle JVM to load appropriate libraries. These libraries are loaded once and cannot be reloaded without restarting the Java process.

### PreparedStatement.getMetaData() Method

Starting from Oracle Database 11g Release 2 (11.2), JDBC drivers support obtaining the metadata of a SELECT statement without executing the `PreparedStatement`. This feature works even with the earlier database releases. For more information, please refer to ["Interface oracle.jdbc.OraclePreparedStatement"](oraint.md).

### Oracle RAC Fast Application Notification

Oracle Database 11g Release 2 (11.2) introduces a simplified API for accessing Oracle RAC Fast Application Notification (FAN) events. This feature enables you to develop more responsive applications that take full advantage of Oracle Database high-availability features. For more information refer to ["Oracle RAC Fast Application Notification"](apxracfan.md).

### Universal Connection Pool

Oracle Database 11g Release 2 (11.2) includes Oracle Universal Connection Pool (UCP) for JDBC developers. The Oracle Universal Connection Pool (UCP) is a full-featured connection pool for managing database connections. Database-intensive Java applications use the connection pool to improve performance and better utilize system resources.

Note:

Oracle Universal Connection Pool (UCP) for JDBC developers was introduced in Oracle Database 11.1.0.7 release.

See Also:

[Oracle Universal Connection Pool for JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e12265/toc.htm)

### OCI Client Result Cache Enhancement

The Oracle Call Interface (OCI) client result cache feature is enhanced in Oracle Database 11g Release 2 (11.2). The client result cache now supports table annotations and caching on query with views. Also, the restriction causing the client cache to be disabled with database resident pooling is now removed. For more information refer to ["Client Result Cache"](instclnt.md).