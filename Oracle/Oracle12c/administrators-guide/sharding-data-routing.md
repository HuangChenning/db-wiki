---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/sharding-data-routing.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

Oracle Sharding supports two types of routing.

The following topics describe routing in an SDB environment.

- Direct Routing to a Shard  
	Oracle clients and connections pools are able to recognize sharding keys specified in the connection string for high performance data dependent routing. A shard routing cache in the connection layer is used to route database requests directly to the shard where the data resides.
- Queries and DMLs via Proxy Routing in an SDB  
	Sharding supports routing for queries that do not specify a sharding key. This allows the flexibility for any database application to execute SQL statements (including `SELECT` and `DML`) in a system where tables are sharded or duplicated without the need to specify the shards where the query should be executed.

**Parent topic:** [Sharded Database Management](shard_part.md)

### 54.1 Direct Routing to a Shard

Oracle clients and connections pools are able to recognize sharding keys specified in the connection string for high performance data dependent routing. A shard routing cache in the connection layer is used to route database requests directly to the shard where the data resides.

The following topics describe direct routing to a shard:

- About Direct Routing to a Shard  
	In direct routing to a shard, a connection is established to a single, relevant shard which contains the data pertinent to the required transaction using a sharding key.
- Sharding APIs  
	Oracle connection pools and drivers support Oracle Sharding.

**Parent topic:** Routing in an SDB Environment

#### 54.1.1 About Direct Routing to a Shard

In direct routing to a shard, a connection is established to a single, relevant shard which contains the data pertinent to the required transaction using a sharding key.

A sharding key is used to route database connection requests at a user session level during connection checkout. The composite sharding method requires both a sharding key and a super sharding key. Direct routing requires the sharding key (or super sharding key) be passed as part of the connection. Based on this information, a connection is established to the relevant shard which contains the data pertinent to the given sharding key or super sharding key.

Once the session is established with a shard, all SQL queries and DMLs are supported and executed in the scope of the given shard. This routing is fast and is used for all OLTP workloads that perform intra-shard transactions. It is recommended that direct routing be employed for all OLTP workloads that require the highest performance and availability.

In support of Oracle Sharding, key enhancements have been made to Oracle connection pools and drivers. Starting in Oracle Database 12c Release 2, JDBC, Universal Connection Pool (UCP), OCI Session Pool (OCI), and Oracle Data Provider for.NET (ODP.NET) provide new APIs to pass sharding keys during the connection creation. Apache Tomcat, IBM Websphere, Oracle WebLogic Server, and JBOSS can leverage JDBC/UCP support and use sharding. PHP, Python, Perl, and Node.js can leverage OCI support.

A shard topology cache is a mapping of the sharding key ranges to the shards. Oracle Integrated Connection Pools maintain this shard topology cache in their memory. Upon the first connection to a given shard (during pool initialization or when the pool connects to newer shards), the sharding key range mapping is collected from the shards to dynamically build the shard topology cache.

Caching the shard topology creates a fast path to the shards and expedites the process of creating a connection to a shard. When a connection request is made with a sharding key, the connection pool looks up the corresponding shard on which this particular sharding key exists (from its topology cache). If a matching connection is available in the pool then the pool returns a connection to the shard by applying its internal connection selection algorithm.

A database connection request for a given sharding key that is in any of the cached topology map, goes directly to the shard (that is, bypassing the shard director). Connection Pool also subscribes to RLB notifications from the SDB and dispenses the best connection based on runtime load balancing advisory. Once the connection is established, the client executes transactions directly on the shard. After all transactions for the given sharding key have been executed, the application must return the connection to the pool and obtain a connection for another key.

If a matching connection is not available in the pool, then a new connection is created by forwarding the connection request with the sharding key to the shard director.

Once the pools are initialized and the shard topology cache is built based on all shards, a shard director outage has no impact on direct routing.

See Also:

Direct Routing to a Shard

**Parent topic:** Direct Routing to a Shard

#### 54.1.2 Sharding APIs

Oracle connection pools and drivers support Oracle Sharding.

JDBC, UCP, OCI, and Oracle Data Provider for.NET (ODP.NET) recognize sharding keys as part of the connection check. Apache Tomcat, Websphere, and WebLogic leverage UCP support for sharding and PHP, Python, Perl, and Node.js leverage OCI support.

Sharding APIs for Oracle UCP

A shard-aware application gets a connection to a given shard by specifying the sharding key using the enhanced sharding API calls `createShardingKeyBuilder` and `createConnectionBuilder`.

At a high-level, the following steps have to be followed in making an application work with a Sharded Database:

1. Update the URL to reflect the Shard Directors and Global Service.
2. Set the pool parameters at the pool level and the shard level:
	- Initial number of connections to be created when UCP is started using `setInitialPoolSize`
		- Minimum number of connections maintained by pool at runtime using `setMinPoolSize`
		- UCP property to set maximum number of connections allowed on connection pool using `setMaxPoolSize`
		- Set max connections per shard with `setMaxConnectionsPerShard`
3. Build a sharding key object with `createShardingKeyBuilder`.
4. Establish a connection using `createConnectionBuilder`.
5. Execute transactions within the scope of the given shard.

Example 54-1 Establishing a Connection Using UCP Sharding API

The following is a code fragment which illustrates how the sharding keys are built and connections established using UCP Sharding API calls.

```
...

PoolDataSource pds =                                
     PoolDataSourceFactory.getPoolDataSource();
  
  // Set Connection Pool properties
pds.setURL(DB_URL);
pds.setUser("hr");  
pds.setPassword("****");
pds.setInitialPoolSize(10);
pds.setMinPoolSize(20);
pds.setMaxPoolSize(30);
                
// build the sharding key object

OracleShardingKey shardingKey = 
    pds.createShardingKeyBuilder() 
      .subkey("mary.smith@example.com", OracleType.VARCHAR2)
      .build(); 

  // Get an UCP connection for a shard
Connection conn = 
    pds.createConnectionBuilder()
     .shardingKey(shardingKey)
     .build();
...
```

Example 54-2 Sample Shard-Aware Application Code Using UCP Connection Pool

In this example the pool settings are defined at the pool level and at the shard level.

```
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import oracle.jdbc.OracleShardingKey;
import oracle.jdbc.OracleType;
import oracle.jdbc.pool.OracleDataSource;
import oracle.ucp.jdbc.PoolDataSource;
import oracle.ucp.jdbc.PoolDataSourceFactory;

public class MaxConnPerShard
{    
  public static void main(String[] args) throws SQLException
  {    
    String url = "jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(HOST=shard-dir1)(PORT=3216)(PROTOCOL=tcp))(CONNECT_DATA=(SERVICE_NAME=shsvc.shpool.oradbcloud)(REGION=east)))";
    String user="testuser1", pwd = "testuser1";  
  
    int maxPerShard = 100, initPoolSize = 20;    

    PoolDataSource pds = PoolDataSourceFactory.getPoolDataSource();
    pds.setConnectionFactoryClassName(OracleDataSource.class.getName());
    pds.setURL(url);
    pds.setUser(user);
    pds.setPassword(pwd);
    pds.setConnectionPoolName("testpool");
    pds.setInitialPoolSize(initPoolSize);    

    // set max connection per shard
    pds.setMaxConnectionsPerShard(maxPerShard);
    System.out.println("Max-connections per shard is: "+pds.getMaxConnectionsPerShard());
                
    // build the sharding key object
    int shardingKeyVal = 123;    
    OracleShardingKey sdkey = pds.createShardingKeyBuilder()
        .subkey(shardingKeyVal, OracleType.NUMBER)
        .build();

    // try to build maxPerShard connections with the sharding key
    Connection[] conns = new Connection[maxPerShard];
    for (int i=0; i<maxPerShard; i++)
    {      
      conns[i] = pds.createConnectionBuilder()
          .shardingKey(sdkey)
          .build();
    
Statement stmt = conns[i].createStatement();
      ResultSet rs = stmt.executeQuery("select sys_context('userenv', 'instance_name'), sys_context('userenv', 'chunk_id') from dual");
      while (rs.next()) {
        System.out.println((i+1)+" - inst:"+rs.getString(1)+", chunk:"+rs.getString(2));
      }
      rs.close();
      stmt.close();
    }      

    System.out.println("Try to build "+(maxPerShard+1)+" connection ...");
    try {
      Connection conn = pds.createConnectionBuilder()
          .shardingKey(sdkey)
          .build();

      Statement stmt = conn.createStatement();
      ResultSet rs = stmt.executeQuery("select sys_context('userenv', 'instance_name'), sys_context('userenv', 'chunk_id') from dual");
      while (rs.next()) {
        System.out.println((maxPerShard+1)+" - inst:"+rs.getString(1)+", chunk:"+rs.getString(2));
      }
      rs.close();
      stmt.close();

      System.out.println("Problem!!! could not build connection as max-connections per shard exceeded");
      conn.close();
    } catch (SQLException e) {
      System.out.println("Max-connections per shard met, could not build connection any more, expected exception: "+e.getMessage());
    }    
    for (int i=0; i<conns.length; i++)
    {
      conns[i].close();
    }        
  }
}
```

ODP.NET Sharding APIs

A shard-aware application gets a connection to a given shard by specifying the sharding key and super sharding key using ODP.NET APIs, such as the `SetShardingKey(OracleShardingKey shardingKey, OracleShardingKey superShardingKey)` instance method on the `OracleConnection` class.

At a high level, the following steps are necessary for a.NET application to work with a Sharded Database:

1. Use ODP.NET, Unmanaged Driver.
	Sharding is supported with or without ODP.NET connection pooling. Each pool can maintain connections to different shards of the sharded database.
2. Use an `OracleShardingKey` class to set the sharding key and another instance for the super sharding key.
3. Invoke the `OracleConnection.SetShardingKey()` method prior to calling `OracleConnection.Open()` so that ODP.NET can return a connection with the specified sharding key and super sharding key.
	These keys must be set while the `OracleConnection` is in a Closed state, otherwise an exception is thrown.

Example 54-3 Sample Shard-Aware Application Code Using ODP.NET

```
using System;
using Oracle.DataAccess.Client;
 
class Sharding
{
  static void Main()
  {
    OracleConnection con = new OracleConnection("user id=hr;password=hr;Data Source=orcl;");
    //Setting a shard key
    OracleShardingKey shardingKey = new OracleShardingKey(OracleDbType.Int32, 123);
    //Setting a second shard key value for a composite key
    shardingKey.SetShardingKey(OracleDbType.Varchar2, "gold");
    //Creating and setting the super shard key
    OracleShardingKey superShardingKey = new OracleShardingKey();
    superShardingKey.SetShardingKey(OracleDbType.Int32, 1000);
    
    //Setting super sharding key and sharding key on the connection
    con.SetShardingKey(shardingKey, superShardingKey);
    con.Open();

    //perform SQL query
  }
}
```

See Also:

[Oracle Database JDBC Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=JJDBC-GUID-1D7795CA-79DC-452B-9FCC-0EF430F87461) for information about JDBC support for Oracle Sharding

[Oracle Universal Connection Pool Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=JJUCP-GUID-12685D3A-F083-433A-90DF-C5533009B841) for information about UCP support for Oracle Sharding

[Oracle Data Provider for.NET Developer's Guide for Microsoft Windows](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=ODPNT8599) for information about ODP.NET support for Oracle Sharding

[Oracle Call Interface Programmer's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/admin&id=LNOCI-GUID-C64136C2-CF65-4507-8811-9A03946CC817) for information about the OCI interface for using shards

**Parent topic:** Direct Routing to a Shard

### 54.2 Queries and DMLs via Proxy Routing in an SDB

Sharding supports routing for queries that do not specify a sharding key. This allows the flexibility for any database application to execute SQL statements (including `SELECT` and `DML`) in a system where tables are sharded or duplicated without the need to specify the shards where the query should be executed.

The following topics describe proxy routing in detail:

- About Proxy Routing in a Sharded Database  
	Proxy routing is an ancillary usage pattern targeted for developer convenience. This requires connection be established to the coordinator.
- Oracle Sharding Coordinator  
	The Oracle Sharding coordinator database contains the metadata of the sharded topology and provides query processing support for sharded databases.
- Querying and DMLs Using Proxy Routing  
	Proxy routing enables aggregation of data and reporting across shards. It also allows the flexibility for any database application to execute SQL statements (including SELECT and DML) in a system where tables are sharded or duplicated without the need to specify the sharding key (during connect) where the query should execute.
- Proxy Routing for Single-Shard Queries  
	Single shard query (SSQ) is the query which needs to scan data only from one shard and need not look at any other shard.
- Proxy Routing for Multi-Shard Queries  
	A multi-shard query must scan data from more than one shard, and the processing on each shard is independent of any other shard.
- Resiliency of Proxy Routing  
	It is highly recommended that the coordinator be protected with Data Guard with fast-start failover and optionally be Oracle RAC-enabled for availability and scalability
- Supported Query Shapes in Proxy Routing  
	In Oracle Database 12c Release 2, multi-shard query support has several restrictions. Some restrictions are based on the type of tables involved in the query and some are based on the SQL constructs used.

**Parent topic:** Routing in an SDB Environment

#### 54.2.1 About Proxy Routing in a Sharded Database

Proxy routing is an ancillary usage pattern targeted for developer convenience. This requires connection be established to the coordinator.

In Oracle Database 12.2, the shard catalog database assumes the role of the coordinator database. The coordinator uses the metadata of the sharded topology and provides query processing support for sharded databases. The SQL compiler identifies the relevant shards automatically and coordinates the query execution across all the participating shards. Once the session is made to the coordinator, SQL queries and DMLs are executed and require no modification.

Proxy routing is suitable for the following scenarios:

- When the application cannot pass the sharding key during connect
- When the application needs to access data from sharded tables residing on multiple shards
- SQL queries typically used in reporting such as - Aggregates on sales data

Routing using the coordinator allows your application to submit SQL statements without a sharding key value passed during connect. The Coordinator’s SQL compiler analyzes and rewrites the query into query fragments that are sent and executed by the participating shards. The queries are rewritten so that most of the query processing is done on the participating shards and then aggregated by the coordinator. In essence, the shards act as compute nodes for the queries executed by coordinator. Because the computation is pushed to the data, there is reduced movement of data between shards and the coordinator. It also enables the effective utilization of the resources of the shards as much as possible to offload processing from the coordinator.

It is recommended that applications separate their workloads for direct routing and proxy routing. Separate connection pools must be created for these workloads.

See Also:

Queries and DMLs via Proxy Routing in an SDB

**Parent topic:** Queries and DMLs via Proxy Routing in an SDB

#### 54.2.2 Oracle Sharding Coordinator

The Oracle Sharding coordinator database contains the metadata of the sharded topology and provides query processing support for sharded databases.

Connecting to the Coordinator

To perform multi-shard queries, connect to the coordinator using the GDS$CATALOG service on the shard catalog database:

```
sqlplus app_schema/app_schema@shardcatvm:1521/GDS\$CATALOG.oradbcloud
```

Coordinator High Availability

The unavailability of the coordinator impacts proxy-routing based workloads. So it is highly recommended that the coordinator be protected with Data Guard in Maximum Availability protection mode (zero data loss failover) with fast-start failover enabled. The coordinator may optionally be Oracle RAC-enabled for additional availability and scalability.

Unavailability of the coordinator has zero impact on workloads utilizing direct routing.

Coordinator Database Sizing

The shard catalog and coordinator host the following key information:

- Metadata of the sharded database topology
- Schema of the sharded application
- Master copies of the duplicated tables

The size of the metadata and the schema is nominal; however, the number of duplicated tables and the space they occupy should be planned for when sizing the coordinator.

In addition to the above, the coordinator should also be sized to handle proxy routing, which can be CPU, I/O, and memory intensive based on the SQL queries and the amount of data being processed.

**Parent topic:** Queries and DMLs via Proxy Routing in an SDB

#### 54.2.3 Querying and DMLs Using Proxy Routing

Proxy routing enables aggregation of data and reporting across shards. It also allows the flexibility for any database application to execute SQL statements (including SELECT and DML) in a system where tables are sharded or duplicated without the need to specify the sharding key (during connect) where the query should execute.

In both use-cases the user accepts a reduced level of performance compared to direct routing.

In a sharded database (SDB), there are two types of tables: sharded tables and duplicated tables.

Sharded tables are equi-partitioned on a sharding key.

```
S=S1 U S2 U … U Sn
```

Duplicated tables are identical on all shards.

```
R = R1 = … = Rn
```

Proxy routing in an SDB provides a transparent mechanism to execute typical SQL queries that access data from sharded and duplicated tables without requiring the application to specify the relevant shards The SQL compiler identifies the relevant shards automatically and coordinates the query execution across all the participating shards. Database links are used for the communication between the coordinator and the shards.

At a high level the coordinator rewrites each incoming query, Q, into a distributive form composed of two queries, CQ and SQ, where SQ (Shard Query) is the portion of Q that executes on each participating shard and CQ (Coordinator Query) is the portion that executes on the coordinator shard.

```
Q  =>  CQ ( Shard_Iterator( SQ ) )
```

The following is an example of an aggregate query Q1 rewritten into Q1’ for an inter shard execution:

```
Q1 : SELECT COUNT(*) FROM customers

Q1’: SELECT SUM(sc) FROM (Shard_Iterator(SELECT COUNT(*) sc FROM s1 (i) ))
```

There are two key elements in this process: (1) identifying the relevant shards (2) rewriting the query into a distributive form, and shard iteration.

During the compilation of a query on the coordinator database, the query compiler analyzes the predicates on the sharding key and extracts the ones that can be used to identify the participating shards, i.e. shards that will contribute rows for the sharded tables referenced in the query. The rest of the shards are referred to as pruned shards.

In the case where only one participating shard was identified, the full query is routed to that shard for full execution. This is termed as a Single Shard Query. If there is more than one participating shard the query is known as multi-shard query and is rewritten. The rewriting process takes into account the expressions computed by the query as well as the query shape.

**Parent topic:** Queries and DMLs via Proxy Routing in an SDB

#### 54.2.4 Proxy Routing for Single-Shard Queries

Single shard query (SSQ) is the query which needs to scan data only from one shard and need not look at any other shard.

The SSQ is similar to a client connecting to a specific shard and issuing a query on that shard. In this scenario, the entire query will be executed on the single participating shard, and the coordinator just passes processed rows back to the client. The plan on coordinator would be similar to the remote mapped cursor.

For example, the following query is fully mapped to shard1 because the data for customer 123 is located on shard1. The unit of execution on the shard is entire query.

```
Q1: SELECT count(*) 
    FROM customers c, orders o 
    WHERE c.custno = o.custno and 
          c.custno = 123;
```

The SSQ contains a condition on the shard key that maps to one and only one shard which is known at query compilation time (literals) or query start time (bind). The query is fully executed on the qualifying shard. SSQs can be SELECT, UPDATE, DELETE and INSERT. MERGE/UPSERT are not supported.

SSQs are supported for:

- Equality and In-list, such as `Area = ‘West’`
- Conditions containing literal, bind, or expression of literals and binds, such as
	```
	Area = :bind
	Area = CASE :bind <10 THEN ‘West’ ELSE ‘East’ END
	```
- `SELECT`, `UPDATE`, `DELETE` and `INSERT`

**Parent topic:** Queries and DMLs via Proxy Routing in an SDB

#### 54.2.5 Proxy Routing for Multi-Shard Queries

A multi-shard query must scan data from more than one shard, and the processing on each shard is independent of any other shard.

A multi-shard query maps to more than one shard and the coordinator may need to do some processing before sending the result to the client. For example, the following query fetches the number of orders placed by each customer.

```
Q2: SELECT count(*), c.custno 
    FROM customers c, orders o 
    WHERE c.custno = o.custno
    GROUP BY c.custno;
```

The query is transformed to the following by the coordinator.

```
Q3: SELECT sum(count_col), custno 
    FROM (SELECT count(*) count_col, c.custno 
          FROM customers c, orders o 
          WHERE c.custno = o.custno
          GROUP BY c.custno)
    GROUP BY custno;
```

The inline query block is mapped to every shard just as a remote mapped query block. The coordinator performs further aggregation and `GROUP BY` on top of the result set from all shards. The unit of execution on every shard is the inline query block.

In Oracle Database 12c Release 2 muti-shard queries are supported for `SELECT` statements only. A query can either access a single shard (in case of equality filter), or ALL shards (in case of no filter predicate on sharding key).

**Parent topic:** Queries and DMLs via Proxy Routing in an SDB

#### 54.2.6 Resiliency of Proxy Routing

It is highly recommended that the coordinator be protected with Data Guard with fast-start failover and optionally be Oracle RAC-enabled for availability and scalability

Failure of the coordinator affects multi- and single-shard queries that are routed through the coordinator. The following are failure scenarios while querying and the expected behavior of proxy routing:

- If a participating shard is down, then the coordinator sends the query to another shard with same data.
- If failure happens during execution of the query on a participating shard, then the user will receive an error.

**Parent topic:** Queries and DMLs via Proxy Routing in an SDB

#### 54.2.7 Supported Query Shapes in Proxy Routing

In Oracle Database 12c Release 2, multi-shard query support has several restrictions. Some restrictions are based on the type of tables involved in the query and some are based on the SQL constructs used.

A query with a join between e.g. two sharded tables must satisfy one of the following two conditions to complete successfully:

- All tables should be joined using equality on sharding key.
- All tables have a filter on sharding key that qualifies the same shard.

A query with a join between a sharded and a duplicated table can be on any column using any comparison operator (= < > <= >=) or even arbitrary join expression.

Query Involves Only Duplicated Tables

For queries involving only duplicated tables there are no restrictions on the query shape. The query is executed on the coordinator.

Query Involves Only Sharded Tables

For single table query, the query may have an equality filter on sharding key that qualifies a shard. For join queries, all tables should be joined using equality on sharding key. Here are various supported and unsupported join patterns.

Supported

- Inner join where equi-join is only on sharding key
	```
	SELECT … FROM s1 INNER JOIN s2 ON s1.sk=s2.sk 
	WHERE any_filter(s1) AND any_filter(s2)
	```
- Left outer join only on sharding key
	```
	SELECT … FROM s1 LEFT OUTER JOIN s2 ON s1.sk=s2.sk
	```
- Right outer join, same as left outer join
	```
	SELECT … FROM s1 RIGHT OUTER JOIN s2 ON s1.sk=s2.sk
	```
- Full outer join only on sharding key, but only if Native is valid which requires equi-join.
	```
	SELECT … FROM s1 FULL OUTER JOIN s2 ON s1.sk=s2.sk
	WHERE any_filter(s1) AND any_filter(s2)
	```

Not Supported

- Semi-join (`EXISTS`) on non sharding key
- Anti-join (`NOT EXISTS`)

Query Involves Sharded and Duplicated Tables

This type of query will be either SSQ or MSQ based on the predicates on the sharding key. The only difference is that the query will contain a non sharded table which is duplicated on each shard.

Joins between a sharded and a duplicated table can be on any column using any comparison operator (= < > <= >=) or even arbitrary join expression. The following are various supported and unsupported join patterns.

Supported

- Inner join
	```
	SELECT … FROM s1 INNER JOIN r1 ON any_join_condition(s1,r1) 
	WHERE any_filter(s1) AND any_filter(r1)
	```
- Left/Right outer join
	Condition: sharded table has to be the null augmented table, that is
	- Sharded table is the first table in `LEFT OUTER JOIN`
		```
		SELECT … FROM s1 LEFT OUTER JOIN r1 ON any_join_condition(s1,r1) 
		WHERE any_filter(s1) AND any_filter(r1)
		SELECT … FROM r1 LEFT OUTER JOIN s1 ON any_join_condition(s1,s2) 
		AND any_filter(r1) AND filter_one_shard(s1)
		```
		- Sharded table is second table in `RIGHT OUTER JOIN`
		```
		SELECT … FROM r1 RIGHT OUTER JOIN s1 ON any_join_condition(s1,r1) 
		WHERE any_filter(s1) AND any_filter(r1)
		SELECT … FROM s1 RIGHT OUTER JOIN r1 ON any_join_condition(s1,s2) 
		AND filter_one_shard(s1) AND any_filter(r1)
		```
- Full outer join
	Condition: Sharded table pruned to single shard via filter predicate on sharding key AND Native Full outer join
	```
	SELECT … FROM s1 FULL OUTER JOIN r1 ON s1.sk=s2.sk
	WHERE any_filter(s1) AND any_filter(s2)
	```
- Semi-join (`EXISTS`)
	Condition: Duplicated table should be in the sub-query OR sharded table in subquery and it prunes to single shard using filter on sharding key
	```
	SELECT … FROM s1 EXISTS 
	(SELECT 1 FROM r1 WHERE r1.anykey=s1.anykey)
	SELECT … FROM r1 EXISTS 
	(SELECT 1 FROM s1 WHERE r1.anykey=s1.anykey and filter_one_shard(s1))
	```
- Anti-join (`NOT EXISTS`)
	Condition: Duplicated table should be in the sub-query
	```
	SELECT … FROM s1 NOT EXISTS 
	(SELECT 1 FROM r1 WHERE r1.anykey=s1.anykey)
	```

Not Supported

- Left/Right outer join
	Duplicated table is first table in `LEFT OUTER JOIN` OR Sharded table is first and it maps to single shard based on filter predicate on sharding key.
	```
	SELECT … FROM r1 LEFT OUTER JOIN s1 ON any_join_condition(s1,s2) 
	AND any_filter(r1) AND any_filter(s1)
	```
	Duplicated table is second table in `RIGHT OUTER JOIN` OR Sharded table is second and it maps to single shard based on filter predicate on sharding key.
	```
	SELECT … FROM s1 RIGHT OUTER JOIN r1 ON any_join_condition(s1,s2) 
	AND any_filter (s1) AND any_filter(r1)
	```
- Full Outer Join
	Sharded table requiring access to multiple shards
	```
	SELECT … FROM s1 FULL OUTER JOIN r1 ON s1.non_sk=s2.non_sk
	WHERE any_filter(s1) AND any_filter(s2)
	```
- Semi-join (`EXISTS`)
	Sharded table in subquery that requires access of multiple shards.
	```
	SELECT … FROM r1 EXISTS 
	(SELECT 1 FROM s1 WHERE r1.anykey=s1.anykey)
	```
- Anti-join (`NOT EXISTS`)
	Sharded table is in the sub-query
	```
	SELECT … FROM r1 NOT EXISTS 
	(SELECT 1 FROM s1 WHERE r1.anykey=s1.anykey
	```

Aggregate Functions

The following aggregations are supported by proxy routing.

- `COUNT`
- `SUM`
- `MIN`
- `MAX`
- `AVG`

Multi-shard Queries and Global CR

A multi-shard query must maintain global read consistency (CR) by issuing the query at the highest common SCN across all the shards.

Transactions

A DML statement that affects only one shard is supported. For example,

```
update S1 set col = … where sk = <constant>;
```

A DML statement that affects more than one shard is not supported. For example,

```
update S1 set col = …;
```

Within a transaction, multiple single shard DMLs can be performed on different shards. For example,

```
insert into S1 values (…);
Update S1 set col = … where sk = constant;
Delete S1 where sk = constant;
Commit;
```

For multi-shard DML, the coordinator uses database link, starts a distributed transaction and performs two phase commit to guarantee the consistency of the distributed transaction. In the case of an in-doubt transaction, the database administrator has to recover it manually.

Execution Plans for Proxy Routing

In Oracle Database 12c Release 2 (12.2.0.1) the plan of the shard query shows the coordinator plan only. You must connect to a shard to see the shard plan for the query. The SQL ID of the query on the shard is different from the SQL ID of the original query on the coordinator, so the shard query text is embedded with the SQL ID of the coordinator and the shard user must look for the SQL with the SQL ID of the original SQL as a comment in the SQL text.

```
SQL> explain plan for select count(*) from employees;

-----------------------------------------------
| Id  | Operation         | Name              |
-----------------------------------------------
|   0 | SELECT STATEMENT  |                   |
|   1 |  SORT AGGREGATE   |                   |
|   2 |   VIEW            | VW_SHARD_B4851255 |
|   3 |    SHARD ITERATOR |                   |
|   4 |     REMOTE        |                   |
-----------------------------------------------
Remote SQL Information (identified by operation id):
----------------------------------------------------
   4 - EXPLAIN PLAN INTO PLAN_TABLE@! FOR
       SELECT COUNT(*) FROM "EMPLOYEES" "A1" /* coord_sql_id=3g18nvrpt0a8p */
```

Passing Hints in Cross Shard Queries

Any hint specified in original query on the coordinator is propagated to the shards.

Tracing and Troubleshooting Slow Running Cross Shard Queries

Set the trace event `shard_sql` on the coordinator to trace the query rewrite and shard pruning. One of the common performance issue observed is when the group by is not pushed to the shards because of certain limitations of the sharding. Check if all of the possible operations are pushed to shards and the coordinator has minimal work to consolidate the results from shards.

**Parent topic:** Queries and DMLs via Proxy Routing in an SDB