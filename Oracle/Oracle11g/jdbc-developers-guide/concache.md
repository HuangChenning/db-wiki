---
title: Implicit Connection Caching
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/concache.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 21 Implicit Connection Caching

Connection caching, generally implemented in the middle tier, is a means of keeping and using the cache of physical database connections.

Note:

Starting from Oracle Database 11 Release 2 (11.2), this feature has been deprecated, and replaced with Universal Connection Pool (UCP) for JDBC. Oracle recommends that you take advantage of the new architecture, which is more powerful and offers better performance. Refer to the following link for more information
```
http://www.oracle.com/technology/tech/java/sqlj_jdbc/index.html
```

The implicit connection cache is an improved Java Database Connectivity (JDBC) 3.0-compliant connection cache implementation for `DataSource`. Java and Java2 Platform, Enterprise Edition (J2EE) applications benefit from transparent access to the cache, support for multiple users, and the ability to request connections based on user-defined profiles.

An application turns the implicit connection cache on by calling `setConnectionCachingEnabled(true)` on an `OracleDataSource`. After implicit caching is turned on, the first connection request to the `OracleDataSource` transparently creates a connection cache. There is no need for application developers to write their own cache implementations.

This chapter is divided into the following sections:

## The Implicit Connection Cache

The connection caching architecture has been redesigned so that caching is transparently integrated into the data source architecture.

The connection cache uses the concept of physical connections and logical connections. Physical connections are the actual connections returned by the database and logical connections are containers used by the cache to manipulate physical connections. You can think of logical connections as handles. The caches always return logical connections, which implement the same interfaces as physical connections.

The implicit connection cache offers the following:

- Driver independence
	Both the JDBC Thin and JDBC Oracle Call Interface (OCI) drivers support the implicit connection cache.
- Transparent access to the JDBC connection cache
	After an application turns implicit caching on, it uses the standard `OracleDataSource` application programming interfaces (APIs) to get connections. With caching enabled, all connection requests are serviced from the connection cache.
	When an application calls the `OracleConnection.close` method to close the logical connection, the physical connection is returned to the cache.
- Single cache per `OracleDataSource` instance
	When connection caching is turned on, each cache-enabled `OracleDataSource` has exactly one cache associated with it. All connections obtained through that data source, no matter what user name and password are used, are returned to the cache. When an application requests a connection from the data source, the cache either returns an existing connection or creates a new connection with matching authentication information.
	Note:
	Caches cannot be shared between `DataSource` instances. There is a one-to-one mapping between cache-enabled `DataSource` instances and caches.
- Heterogeneous user names and passwords per cache
	Unlike the previous cache implementation, all connections obtained through the same data source are stored in a common cache, no matter what user name and password the connection requests.
- Support for JDBC 3.0 connection caching, including support for multiple users and the required cache properties
- Property-based configuration
	Cache properties define the behavior of the cache. The supported properties set timeouts, the number of connections to be held in the cache, and so on. Using these properties, applications can reclaim and reuse abandoned connections. The implicit connection cache supports all the JDBC 3.0 connection cache properties.
- OracleConnectionCacheManager
	The new `OracleConnectionCacheManager` class provides a rich set of administrative APIs that applications can use to manage the connection cache. Each virtual machine has one distinguished instance of `OracleConnectionCacheManager`. Applications manage a cache through the single `OracleConnectionCacheManager` instance.
- User-defined connection attributes
	The implicit connection cache supports user-defined connection attributes that can be used to determine which connections are retrieved from the cache. Connection attributes can be thought of as labels whose semantics are defined by the application, not by the caching mechanism.
- Callback mechanism
	The implicit connection cache provides a mechanism for users to define cache behavior when a connection is returned to the cache, when handling abandoned connections, and when a connection is requested but none is available in the cache.
- Connect-time load balancing
	Implicit connection caching provides connect-time load balancing when a connection is first created by the application. The database listener distributes connection creation across Oracle Real Application Clusters instances that would perform the best at the time of connection creation.
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/hafeats.htm#RACAD7122)
- Run-time connection load balancing
	Run-time connection load balancing of work requests uses Service Metrics to route work requests to an Oracle Real Application Clusters instance that offers the best performance. Selecting a connection from the cache based on service, to execute a work request, greatly increases the throughput and scalability.

## Using the Connection Cache

This section discusses how applications use the implicit connection cache. It covers the following topics:

- Turning Caching On
- Opening a Connection
- Setting Connection Cache Name
- Setting Connection Cache Properties
- Closing a Connection
- Implicit Connection Cache Example

### Turning Caching On

An application turns the implicit connection cache on by calling `OracleDataSource.setConnectionCachingEnabled(true)`. After implicit caching is turned on, the first connection request to the `OracleDataSource` class transparently creates a connection cache.

Example 21-1 provides a sample code that uses the implicit connection cache.

Example 21-1 Using the Implicit Connection Cache

```
// Example to show binding of OracleDataSource to JNDI,
// then using implicit connection cache 
 
import oracle.jdbc.pool.*; // import the pool package
 
Context ctx = new InitialContext(ht);
OracleDataSource ods = new OracleDataSource();
 
// Set DataSource properties
ods.setUser("Scott");
ods.setConnectionCachingEnabled(true);    // Turns on caching
ctx.bind("MyDS", ods);
// ...
// Retrieve DataSource from the InitialContext
ods =(OracleDataSource) ctx. lookup("MyDS");  
 
// Transparently create cache and retrieve connection 
conn = ods.getConnection();
// ...
conn.close();  // return connection to the cache
// ...
ods.close() // close datasource and clean up the cache
```

### Opening a Connection

After you have turned connection caching on, whenever you retrieve a connection through the `OracleDataSource.getConnection` method, the JDBC drivers check to see if a connection is available in the cache.

The `getConnection` method checks if there are any free physical connections in the cache that match the specified criteria. If a match is found, then a logical connection is returned, wrapping the physical connection. If no physical connection match is found, then a new physical connection is created, wrapped in a logical connection, and returned.

There are four variations on `getConnection`, two that make no reference to the connection cache and two that specify which sort of connections the cache may return. The non-cache-specific `getConnection` methods behave in the standard manner.

Note:

When implicit connection cache is enabled, the connection returned by `OracleDataSource.getConnection` may not have the state reset. You must, therefore, reset all the connection states, such as auto-commit, batch size, prefetch size, transaction status, and transaction isolation, before putting the connection back into the cache.

### Setting Connection Cache Name

The `ConnectionCacheName` property of `OracleDataSource` is an optional property used by the Connection Cache Manager to manage a connection cache. You can set this property by calling the following method:

```
public void synchronized setConnectionCacheName(String cacheName) throws SQLException
```

When this property is set, the name is used to uniquely identify the cache accessed by the cache-enabled `OracleDataSource`. If the property is not set, then a default cache name is created using the convention `DataSourceName#HexRepresentationOfNumberOfCaches`.

Note:

The `getConnectionCacheName()` method will return the name of the connection cache only if the `setConnectionCacheName` method is called after the `setConnectionCachingEnabled` method is called.

### Setting Connection Cache Properties

You can fine-tune the behavior of the implicit connection cache using the `setConnectionCacheProperties` method to set various connection properties.

See Also:

"Connection Cache Properties"

Note:

- Before setting the cache-specific properties, you must enable caching on the data source; otherwise the `setConnectionCacheProperties` method will have no effect.
- Although these properties govern the behavior of the connection cache, they are set on the data source, and not on the connection or on the cache itself.

### Closing a Connection

An application returns a connection to the cache by calling the `close` method. There are two variants of the `close` method: one with no arguments and one that takes a `Connection` object as argument.

Note:

- Applications must close connections to ensure that the connections are returned to the cache.
- When implicit connection cache is enabled, you must reset all the connection states, such as auto-commit, batch size, prefetch size, transaction status, and transaction isolation, before putting the connection back into the cache. This ensures that any subsequent connection retrieved from the cache will have its state reset.

### Implicit Connection Cache Example

Example 21-2 demonstrates creating a data source, setting its caching and data source properties, retrieving a connection, and closing that connection in order to return it to the cache.

Example 21-2 Connection Cache Example

```
import java.sql.*;
import javax.sql.*;
import java.util.*;
import javax.naming.*;
import javax.naming.spi.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.*;
 
...
  
    // create a DataSource    
    OracleDataSource ods = new OracleDataSource();
    
    // set cache properties 
    java.util.Properties prop = new java.util.Properties();
    prop.setProperty("MinLimit", "2");    
    prop.setProperty("MaxLimit", "10");    
 
    // set DataSource properties    
    String url = "jdbc:oracle:oci8:@";    
    ods.setURL(url);    
    ods.setUser("hr");    
    ods.setPassword("hr");    
    ods.setConnectionCachingEnabled(true); // be sure set to true    
    ods.setConnectionCacheProperties (prop);    
    ods.setConnectionCacheName("ImplicitCache01"); // this cache's name    
 
    // We need to create a connection to create the cache 
    Connection conn = ds.getConnection(user, pass);
    Statement  stmt  = conn.createStatement();
    ResultSet  rset  = stmt.executeQuery("select user from dual");
    conn.close(); 
     
    ods.close();
```

## Connection Attributes

Each connection obtained from a data source can have user-defined attributes. Attributes are specified by the application developer and are `java.lang.Properties` name and value pairs.

An application can use connection attributes to supply additional semantics to identify connections. For instance, an application may create an attribute named `connection_type` and then assign it the value `payroll` or `inventory`.

Note:

The semantics of connection attributes are entirely application-defined. The connection cache itself enforces no restrictions on the key or value of connection attributes.

The methods that get and set connection attributes are found on the `OracleConnection` interface. This section covers the following topics:

- Getting Connections
- Setting Connection Attributes
- Checking Attributes of a Returned Connection
- Connection Attribute Example

### Getting Connections

The first connection you retrieve has no attributes. You must set them. After you have set attributes on a connection, you can request the connection by specifying its attribute, using the specialized forms of the `getConnection` method:

- `getConnection(java.util.Properties cachedConnectionAttributes`
	Requests a database connection that matches the specified `cachedConnectionAttributes`.
	See Also:
	For a discussion on connection attributes, see "Other Properties".
- `getConnection(java.lang.String user, java.lang.String password, java.util.Properties cachedConnectionAttributes)`
	Requests a database connection from the implicit connection cache that matches the specified `user`, `password` and `cachedConnectionAttributes`. If null values are passed for `user` and `password`, the `DataSource` defaults are used.

Attribute Matching Rules

The rules for matching `connectionAttributes` come in two variations:

- Basic
	In this variation, the cache is searched to retrieve the connection that matches the attributes. The connection search mechanism as follows:
	1. If an exact match is found, the connection is returned to the caller.
		2. If an exact match is not found and the `ClosestConnectionMatch` data source property is set, then the connection with the closest match is returned. The closest matched connection is one that has the highest number of the original attributes matched. Note that the closest matched connection may match a subset of the original attributes, but does not have any attributes that are not part of the original list. For example, if the original list of attributes is A, B and C, then a closest match may have A and B set, but never a D.
		3. If none of the existing connections matches, a new connection is returned. The new connection is created using the user name and password set on the `DataSource`. If `getConnection(String, String, java.util.Properties)` is called, then the user name and password passed as arguments are used to open the new connection.
- Advanced
	In this variation, the attributes may be associated with weights. The connection search mechanism is similar to the basic `connectionAttributes` based search, except that the connections are searched not only based on the `connectionAttributes`, but also using a set of weights that are associated with the keys on the `connectionAttributes`. These weights are assigned to the keys as a one-time operation and is supported as a connection cache property, `AttributeWeights`.

### Setting Connection Attributes

An application sets connection attributes using the following:

```
applyConnectionAttributes(java.util.Properties connAttr)
```

No validation is done on `connAttr`. Applying connection attributes is cumulative. Each time you call `applyConnectionAttributes`, the `connAttr` attribute you supply is added to those previously in force.

### Checking Attributes of a Returned Connection

When an application requests a connection with specified attributes, it is possible that no match will be found in the connection cache. When this happens, the connection cache creates a connection with no attributes and returns it. The connection cache cannot create a connection with the requested attributes, because the Connection Cache manager is ignorant of the semantics of the attributes.

Note:

If the `closestConnectionMatch` property has been set, then the cache manager looks for close attribute matches rather than exact matches.

For this reason, applications should always check the attributes of a returned connection. To do this, use the `getUnMatchedConnectionAttributes` method, which returns a list of any attributes that were not matched in retrieving the connection. If the return value of this method is `null`, you know that you must set all the connection attributes.

### Connection Attribute Example

Example 21-3 illustrates using connection attributes.

Example 21-3 Using Connection Attributes

```
java.util.Properties connAttr = new java.util.Properties();
 connAttr.setProperty("connection_type", "payroll");

 // retrieve connection that matches attributes
 Connection conn = ds.getConnection(connAttr); 
 // Check to see which attributes weren't matched
unmatchedProp = ((OracleConnection)conn).getUnMatchedConnectionAttributes();
if ( unmatchedProp != null )
 {
 // apply attributes to the connection
 ((OracleConnection)conn).applyConnectionAttributes(connAttr);  
 }
 // verify whether conn contains property after apply attributes
 connProp = ((OracleConnection)conn).getConnectionAttributes(); 
 listProperties (connProp);
```

## Connection Cache Properties

The connection cache properties govern the characteristics of a connection cache. This section lists the supported connection cache properties. It covers the following topics:

- Limit Properties
- TIMEOUT Properties
- Other Properties
- Connection Property Example

Applications set cache properties in one of the following ways:

- Using the `OracleDataSource` method `setConnectionCacheProperties`
- When creating a cache using `OracleConnectionCacheManager`
- When reinitializing a cache using `OracleConnectionCacheManager`

### Limit Properties

These properties control the size of the cache.

InitialLimit

Sets how many connections are created in the cache when it is created or reinitialized. When this property is set to an integer value greater than 0, creating or reinitializing the cache automatically creates the specified number of connections, filling the cache in advance of need.

Default: 0

MaxLimit

Sets the maximum number of connection instances the cache can hold. The default value is `Integer.MAX_VALUE`, meaning that there is no limit enforced by the connection cache, so that the number of connections is limited only by the number of database sessions configured for the database.

Default: `Integer.MAX_VALUE` (no limit)

Note:

If the number of concurrent connections exceeds the maximum number of sessions configured at the database server, then you will get `ORA-00018` error. To avoid this error, you must set a value for the `MaxLimit` property. This value should be less than the value of the `SESSIONS` parameter configured for the database server.

MaxStatementsLimit

Sets the maximum number of statements that a connection keeps open. When a cache has this property set, reinitializing the cache or closing the data source automatically closes all cursors beyond the specified `MaxStatementsLimit`.

Default: 0

MinLimit

Sets the minimum number of connections the cache maintains.

Default: 0

Note:

- Setting the `MinLimit` property does not initialize the cache to contain the minimum number of connections. To do this, use the `InitialLimit` property.
- When `InitialLimit` is greater than `MinLimit`, it is possible to have any number of connections specified by `InitialLimit` up to a value specified by `MaxLimit`. Therefore, `InitialLimit` does not depend on `MinLimit`.
- Connections can fall below the minimum limit set on the connection pool when JDBC Fast Connection Failover DOWN events are processed. The processing removes affected connections from the pool. `MinLimit` will be honored as requests to the connection pool increase and the number of connections get past the `MinLimit` value.

### TIMEOUT Properties

These properties control the lifetime of an element in the cache.

InactivityTimeout

Sets the maximum time a physical connection can remain idle in a connection cache. An idle connection is one that is not active and does not have a logical handle associated with it. When `InactivityTimeout` expires, the underlying physical connection is closed. However, the size of the cache is not allowed to shrink below `minLimit`, if it has been set.

Default: 0 (no timeout in effect)

TimeToLiveTimeout

Sets the maximum time in seconds that a logical connection can remain open. When `TimeToLiveTimeout` expires, the logical connection is unconditionally closed, the relevant statement handles are canceled, and the underlying physical connection is returned to the cache for reuse.

Default: 0 (no timeout in effect)

See Also:

"Use Cases for TimeToLiveTimeout and AbandonedConnectionTimeout"

AbandonedConnectionTimeout

Sets the maximum time that a connection can remain unused before the connection is closed and returned to the cache. A connection is considered unused if it has not had SQL database activity.

When `AbandonedConnectionTimeout` is set, JDBC monitors SQL database activity on each logical connection. For example, when `stmt.execute` is called on the connection, a heartbeat is registered to convey that this connection is active. The heartbeats are set at each database execution. If a connection has been inactive for the specified amount of time, the underlying connection is reclaimed and returned to the cache for reuse.

Default: 0 (no timeout in effect)

See Also:

"Use Cases for TimeToLiveTimeout and AbandonedConnectionTimeout"

PropertyCheckInterval

Sets the time interval at which the Connection Cache Manager inspects and enforces all specified cache properties. `PropertyCheckInterval` is set in seconds.

Default: 900 seconds

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/performance.htm#NETAG0144)

### Other Properties

These properties control miscellaneous cache behavior.

AttributeWeights

`AttributeWeights` sets the weight for each attribute set on the connection.

See Also:

"AttributeWeights"

ClosestConnectionMatch

`ClosestConnectionMatch` causes the connection cache to retrieve the connection with the closest approximation to the specified connection attributes.

See Also:

"ClosestConnectionMatch"

ConnectionWaitTimeout

Specifies cache behavior when a connection is requested and there are already MaxLimit connections active. If `ConnectionWaitTimeout` is equal to zero, then each connection request waits for zero seconds, that is, `null` connection is returned immediately. If `ConnectionWaitTimeout` is greater than zero, then each connection request waits for the specified number of seconds or until a connection is returned to the cache. If no connection is returned to the cache before the timeout elapses, then the connection request returns `null`.

Default: zero

LowerThresholdLimit

Sets the lower threshold limit on the cache. The default is 20 percent of the `MaxLimit` on the connection cache. This property is used whenever a `releaseConnection(`) cache callback method is registered.

ValidateConnection

Setting `ValidateConnection` to `true` causes the connection cache to test every connection it retrieves against the underlying database. If a valid connection cannot be retrieved, then an exception is thrown.

Default: `false`

Note:

In Oracle Database 11g Release 1 (11.1) and later versions, there is a change in connection cache behavior. If both the `ValidateConnection` property and the Database `CONNECT_TIME` resource limit are enabled, then the connection cache may return a connection that exceeds the value set for the `CONNECT_TIME` limit, without throwing an exception. An exception is instead thrown at the next statement execution on this connection.

Oracle recommends not setting the `CONNECT_TIME` limit while enabling the `ValidateConnection` property.

### Connection Property Example

Example 21-4 demonstrates how an application uses connection properties.

Example 21-4 Using Connection Properties

```
import java.sql.*;
import javax.sql.*;
import java.util.*;
import javax.naming.*;
import javax.naming.spi.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.*;
...
  OracleDataSource ds =  (OracleDataSource) ctx.lookup("...");
  java.util.Properties prop = new java.util.Properties ();
  prop.setProperty("MinLimit", "5");     // the cache size is 5 at least 
  prop.setProperty("MaxLimit", "25");
  prop.setProperty("InitialLimit", "3"); // create 3 connections at startup
  prop.setProperty("InactivityTimeout", "1800");    //  seconds
  prop.setProperty("AbandonedConnectionTimeout", "900");  //  seconds
  prop.setProperty("MaxStatementsLimit", "10");
  prop.setProperty("PropertyCheckInterval", "60"); // seconds

  ds.setConnectionCacheProperties (prop);  // set properties
  Connection conn = ds.getConnection();
  conn.dosomework();
  java.util.Properties propList=ds.getConnectionCacheProperties();  // retrieve
```

## Connection Cache Manager API

`OracleConnectionCacheManager` provides administrative APIs that the middle tier can use to manage available connection caches. This section provides an example of using the Connection Cache Manager.

Example of ConnectionCacheManager Use

Example 21-5 demonstrates the `OracleConnectionCacheManager` interface.

Example 21-5 Connection Cache Manager Example

```
import java.sql.*;
import javax.sql.*;
import java.util.*;
import javax.naming.*;
import javax.naming.spi.*;
import oracle.jdbc.*;
import oracle.jdbc.pool.*;
...
// Get singleton ConnectionCacheManager instance
  OracleConnectionCacheManager occm =
  OracleConnectionCacheManager.getConnectionCacheManagerInstance();
  String cacheName = "foo";  // Look for a specific cache
  // Use Cache Manager to check # of available connections 
  // and active connections
  System.out.println(occm.getNumberOfAvailableConnections(cacheName)
      " connections are available in cache " + cacheName);
 
  System.out.println(occm.getNumberOfActiveConnections(cacheName)
      + " connections are active");
  // Refresh all connections in cache 
  occm.refreshCache(cacheName,
    OracleConnectionCacheManager.REFRESH_ALL_CONNECTIONS);
  // Reinitialize cache, closing all connections
  java.util.Properties newProp = new java.util.Properties();
  newProp.setProperty("MaxLimit", "50");
  occm.reinitializeCache(cacheName, newProp);
```

## Advanced Topics

This section discusses cache functionality that is useful for advanced users, but is not essential to understanding or using the implicit connection cache. This section covers the following topics:

- Attribute Weights and Connection Matching
- Connection Cache Callbacks

### Attribute Weights and Connection Matching

There are two connection cache properties that enable the developer to specify which connections in the connection cache are accepted in response to a `getConnection` request. When you set the `ClosestConnectionMatch` property to `true`, you are telling the Connection Cache Manager to return connections that match only some of the attributes you have specified.

If you do not specify `attributeWeights`, then the Connection Cache Manager returns the connection that matches the highest number of attributes. If you specify `attributeWeights`, then you can control the priority the manager uses in matching attributes.

ClosestConnectionMatch

Setting `ClosestConnectionMatch` to `true` causes the connection cache to retrieve the connection with the closest approximation to the specified connection attributes. This can be used in combination with `AttributeWeights` to specify what is considered a closest match.

Default: `false`

AttributeWeights

Sets the weights for each `connectionAttribute`. This property is used when `ClosestConnectionMatch` is set to `true` to determine which attributes are given highest priority when searching for matches. An attribute with a high weight is given more importance in determining a match than an attribute with a low weight.

`AttributeWeights` contains a set of `String` s representing key-value pairs. Each key/value pair sets the weights for each `connectionAttribute` for which the user intends to request a connection. Each `String` is in the format written by the `java.util.Properties.Store(OutputStream, String)` method, and thus can be read by the `java.util.Properties.load(InputStream)` method. The `Key` is a `connectionAttribute` and the `Value` is the weight. A weight must be an integer value greater than 0. The default weight is 1.

For example, `TRANSACTION_ISOLATION` could be assigned a weight of 10 and `ROLE` a weight of 5. If `ClosestConnectionMatch` is set to `true`, when a `connectionAttribute` based connection request is made on the cache, connections with a matching `TRANSACTION_ISOLATION` will be favored over connections with a matching `ROLE`.

Default: No `AttributeWeights`

### Connection Cache Callbacks

The implicit connection cache offers a way for the application to specify callbacks to be called by the connection cache. Callback methods are supported with the `OracleConnectionCacheCallback` interface. This callback mechanism is useful to take advantage of the special knowledge of the application about particular connections, supplementing the default behavior when handling abandoned connections or when the cache is empty.

`OracleConnectionCacheCallback` is an interface that must be implemented by the user and registered with `OracleConnection`. The registration API is as follows:

```
public void
registerConnectionCacheCallback(
OracleConnectionCacheCallback cbk, Object usrObj,  int cbkflag);
```

In this interface, `cbk` is the user implementation of the `OracleConnectionCacheCallback` interface. The `usrObj` parameter contains any parameters that the user wants supplied. This user object is passed back, unmodified, when the callback method is called. The `cbkflag` parameter specifies which callback method should be called. It must be one of the following values:

- `OracleConnection.ABANDONED_CONNECTION_CALLBACK`
- `OracleConnection.RELEASE_CONNECTION_CALLBACK`
- `OracleConnection.ALL_CALLBACKS`

When `ALL_CALLBACKS` is set, all the connection cache callback methods are called. For example,

```
// register callback, to invoke all callback methods
((OracleConnection)conn).registerConnectionCacheCallback( new UserConnectionCacheCallback(), 
  new SomeUserObject(), 
OracleConnection.ALL_CALLBACKS);
```

An application can register a `ConnectionCacheCallback` on an `OracleConnection`. When a callback is registered, the connection cache calls the `handleAbandonedConnection` method of the callback before reclaiming the connection. If the callback returns `true`, then the connection is reclaimed. If the callback returns `false`, then the connection remains active.

The `UserConnectionCacheCallback` interface supports two callback methods to be implemented by the user, `releaseConnection` and `handleAbandonedConnection`.

### Use Cases for TimeToLiveTimeout and AbandonedConnectionTimeout

The following are the use cases for the `TimeToLiveTimeout` and `AbandonedConnectionTimeout` timeout mechanisms when used with implicit connection cache. Note that these timeout mechanisms are applicable to the logical connection when it is retrieved from the connection cache.

- The application considers the connections completely stateless.
	When the connections are stateless, either of the timeout mechanisms can be used. The connections for which the timeout expires are put back into the connection cache for reuse. These connections are valid for reuse because there is no session state associated with them.
- The application maintains state on each connection, but has a cleanup routine that can render the connections stateless when they are returned to the connection cache.
	In this case, `TimeToLiveTimeout` cannot be used. There is no way for the connection cache to ensure that a connection returned to the cache is in a reusable condition.However, `AbandonedConnectionTimeout` can be used in this scenario, only if `OracleConnectionCacheCallback` is registered on the connection. The `handleAbandonedConnection` callback method is implemented by the application and ensures that the necessary cleanup is done. The connection is closed when the timeout processing invokes this callback method. The closing of this connection by the callback method causes the connection to be put back into the connection cache in a state where it is reusable.
	Note:
	Do not to close the connection after calling handleAbandonedConnection method because the connection could be in an invalid state. JDBC internally knows how to reclaim a connection even when it is in an invalid state.
	See Also:
	"Connection Cache Callbacks"
- The application maintains state on each connection, but has no control over the connection and, therefore, cannot ensure cleaning up of state for reuse of connections by other applications or users.
	The use of either of the timeout mechanisms is not recommended.