---
title: Fast Connection Failover
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/fstconfo.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 27 Fast Connection Failover

Fast Connection Failover offers a driver-independent way for your Java Database Connectivity (JDBC) application to take advantage of the connection failover facilities offered by Oracle Database 11g. This chapter discusses the following concepts:

Note:

- Starting from Oracle Database 11g Release 2 (11.2), this feature has been deprecated, and replaced with Universal Connection Pool (UCP) for JDBC. Oracle recommends that you take advantage of the new architecture, which is more powerful and offers better performance. Refer to the following links for more information
	`http://www.oracle.com/technetwork/database/focus-areas/application-development/index-099369.html`
	`http://download.oracle.com/docs/cd/B28359_01/java.111/e10788.pdf`
- If you are using UCP, then you should not enable implicit connection caching to use Fast Connection Failover feature. Refer to the following link for more information
	`http://www.oracle.com/technetwork/database/enterprise-edition/ucp-transition-guide-129515.pdf`

## Overview of Fast Connection Failover

The Fast Connection Failover mechanism depends on the implicit connection cache feature. For more information about implicit connection cache, refer to [Chapter 21, "Implicit Connection Caching"](concache.md).

The advantages of Fast Connection Failover include the following:

- Driver independence
	Fast Connection Failover supports both the JDBC Thin and JDBC Oracle Call Interface (OCI) drivers.
- Integration with implicit connection cache
	The two features work together synergistically to improve application performance and high availability.
- Integration with Oracle Real Application Clusters (Oracle RAC)
	This provides superior Real Application Clusters/high availability event notification mechanisms.
- Easy integration with application code
	You only need to enable Fast Connection Failover and no further configuration is required.

Fast Connection Failover Features

When enabled, Fast Connection Failover provides the following:

- Rapid detection and cleanup of invalid cached connections, that is, DOWN event processing
- Load balancing of available connections, that is, UP event processing
- Run-time work request distribution to all active Oracle RAC instances

## Using Fast Connection Failover

Applications manage Fast Connection Failover through `DataSource` instances.

This section covers the following topics:

- Fast Connection Failover Prerequisites
- Configuring ONS for Fast Connection Failover
- Enabling Fast Connection Failover
- Querying Fast Connection Failover Status

### Fast Connection Failover Prerequisites

Fast Connection Failover is available under the following circumstances:

- The implicit connection cache is enabled.
	Fast Connection Failover works in conjunction with the JDBC connection caching mechanism. This helps applications manage connections to ensure high availability.
- The application uses service names to connect to the database.
	The application cannot use service identifiers.
- The underlying database has Oracle Database 11g Real Application Clusters (Oracle RAC) capability or Oracle Data Guard configured with either single instance Databases or Oracle RAC.
	If failover events are not propagated, then connection failover cannot occur.
- Oracle Notification Service (ONS) is configured and available on the node where JDBC is running.
	JDBC depends on ONS to propagate database events and notify JDBC of them.
- The Java Virtual Machine (JVM) in which your JDBC instance is running must have `oracle.ons.oraclehome` set to point to your `ORACLE_HOME`.

### Configuring ONS for Fast Connection Failover

In order for Fast Connection Failover to work, you must configure ONS correctly. ONS is shipped as part of Oracle Database 11g. For more information, refer to ["Configuration of ONS"](apxracfan.md).

#### Remote ONS Subscription

The advantages of remote ONS subscription are the following:

- Support for an All Java middle-tier stack
- No ONS daemon needed on the client computer and, therefore, no need to manage this process
- Simple configuration using the `DataSource` property

When using remote ONS subscription for Fast Connection Failover, the application invokes the following method on an `OracleDataSource` instance:

```
setONSConfiguration(String remoteONSConfig)
```

The `remoteONSConfig` parameter is a list of name and value pairs of the form `name` `=` `value` that are separated by a new line character (\\n). `name` can be one of `nodes`, `walletfile`, or `walletpassword`. This parameter should specify at least the `nodes` ONS configuration attribute, which is a list of `host``:``port` pairs, each pair separated by comma (,). The hosts and ports denote the remote ONS daemons available on the Oracle RAC nodes.

See Also:

["Configuration of ONS"](apxracfan.md)

SSL could be used in communicating with the ONS daemons when the `walletfile` attribute is specified as an Oracle wallet file. In such cases, if the `walletpassword` attribute is not specified, single sign-on (SSO) would be assumed.

Following are a few examples, assuming `ods` is an `OracleDataSource` instance:

```
ods.setONSConfiguration("nodes=racnode1.example.com:4200,racnode2.example.com:4200");

ods.setONSConfiguration("nodes=racnode1:4200,racnode2:4200\nwalletfile=/mydir/Wallet\nwalletpassword=mypasswd");

ods.setONSConfiguration("nodes=racnode1:4200,racnode2:4200\nwalletfile=/mydir/conf/Wallet");
```

### Enabling Fast Connection Failover

An application enables Fast Connection Failover by calling `setFastConnectionFailoverEnabled(true)` on a `DataSource` instance, before retrieving any connections from that instance.

You cannot enable Fast Connection Failover when reinitializing a connection cache. You must enable it before using the `OracleDataSource` instance.

Example 27-1 illustrates how to enable Fast Connection Failover.

Note:

After a cache is Fast Connection Failover-enabled, you cannot disable Fast Connection Failover during the lifetime of that cache.

To enable Fast Connection Failover, you must perform the following:

- Configure and start ONS. If ONS is not correctly set up, then implicit connection cache creation fails and an `ONSException` is thrown at the first `getConnection` request.
- Set the `FastConnectionFailoverEnabled` property before making the first `getConnection` request to an `OracleDataSource`. When Fast Connection Failover is enabled, the failover applies to all connections in the connection cache. If your application explicitly creates a connection cache using the Connection Cache Manager, then you must first set `FastConnectionFailoverEnabled` before retrieving any connections.
- Use a service name rather than a service identifier when setting the `OracleDataSource` `url` property.

Example 27-1 Enabling Fast Connection Failover

```
// declare datasource
ods.setUrl(
"jdbc:oracle:oci:@(DESCRIPTION=
  (ADDRESS=(PROTOCOL=TCP)(HOST=cluster_alias)
    (PORT=1521))
    (CONNECT_DATA=(SERVICE_NAME=service_name)))");
ods.setUser("scott");
ods.setConnectionCachingEnabled(true);
ods.setFastConnectionFailoverEnabled(true):
ctx.bind("myDS",ods);
ds=(OracleDataSource) ctx.lookup("MyDS");
try {
 ds.getConnection();  // transparently creates and accesses cache
 catch (SQLException SE {
  }
}
...
```

### Querying Fast Connection Failover Status

An application determines if Fast Connection Failover is enabled by calling `OracleDataSource.getFastConnectionFailoverEnabled`, which returns `true` if failover is enabled, `false` otherwise.

## Understanding Fast Connection Failover

After Fast Connection Failover is enabled, the mechanism is automatic; no application intervention is needed. This section discusses how a connection failover is presented to an application and what steps the application takes to recover.

This section covers the following topics:

- What the Application Sees
- How It Works

### What the Application Sees

By the time an Oracle RAC service failure is propagated to the JDBC application, the database already rolls back the local transaction. The cache manager then cleans up all invalid connections. When an application holding an invalid connection tries to do work through that connection, it is possible to receive `SQLException, ORA-17008, Closed Connection`.

When an application receives a `Closed Connection` error message, it should do the following:

1. Retry the connection request. This is essential, because the old connection is no longer open.
2. Replay the transaction. All work done before the connection was closed has been lost.

Note:

The application should not try to roll back the transaction. The transaction was already rolled back in the database by the time the application received the exception.

### How It Works

Under Fast Connection Failover, each connection in the cache maintains a mapping to a service, instance, database, and host name.

When a database generates an Oracle RAC event, that event is forwarded to the JVM in which JDBC is running. A daemon thread inside the JVM receives the Oracle RAC event and passes it on to the Connection Cache Manager. The Connection Cache Manager then throws SQL exceptions to the applications affected by the Oracle RAC event.

A typical failover scenario may work like the following:

1. A database instance fails, leaving several stale connections in the cache.
2. The Oracle RAC mechanism in the database generates an Oracle RAC event which is sent to the JVM containing JDBC.
3. The daemon thread inside the JVM finds all the connections affected by the Oracle RAC event, notifies them of the closed connection through SQL exceptions, and rolls back any open transactions.
4. Each individual connection receives a SQL exception and must retry.

## Comparison of Fast Connection Failover and TAF

Fast Connection Failover differs from Transparent Application Failover (TAF) in the following ways:

- Application-level connection retries
	Fast Connection Failover supports application-level connection retries. This gives the application control of responding to connection failovers. The application can choose whether to retry the connection or to rethrow the exception. TAF supports connection retries only at the OCI/Net layer.
- Integration with the implicit connection cache
	Fast Connection Failover is well-integrated with the implicit connection cache, which allows the Connection Cache Manager to manage the cache for high availability. For example, failed connections are automatically invalidated in the cache. TAF works at the network level on a per-connection basis, which means that the connection cache cannot be notified of failures.
- Event-based
	Fast Connection Failover is based on the Oracle RAC event mechanism. This means that Fast Connection Failover is efficient and detects failures quickly for both active and inactive connections.
- Load-balancing support
	Fast Connection Failover supports UP event load balancing of connections and run-time work request distribution across active Oracle RAC instances.

Note:

Oracle recommends not to use TAF and Fast Connection Failover in the same application.