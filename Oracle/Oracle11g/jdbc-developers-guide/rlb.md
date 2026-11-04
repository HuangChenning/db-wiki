---
title: Run-Time Connection Load Balancing
book: "JDBC Developer's Guide"
doc_id: E16548-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/java.112/e16548/rlb.htm
tags:
  - oracle
  - 11g
  - jdbc-developers-guide
---

## 22 Run-Time Connection Load Balancing

Oracle Database 11g provides the run-time connection load balancing feature. This chapter contains the following sections:

- Overview of Run-Time Connection Load Balancing
- Enabling Run-Time Connection Load Balancing

Note:

Starting from Oracle Database 11 Release 2 (11.2), this feature has been deprecated, and replaced with Universal Connection Pool (UCP) for JDBC. Oracle recommends that you take advantage of the new architecture, which is more powerful and offers better performance. Refer to the following link for more information
```
http://www.oracle.com/technology/tech/java/sqlj_jdbc/index.html
```

## Overview of Run-Time Connection Load Balancing

In an Oracle Real Application Clusters environment, a connection could belong to any instance that provides the relevant service. In the best case, all instances perform equally well and randomly retrieving a connection from the cache is appropriate. However, when one instance performs better than others, random selection of a connection is inefficient. The run-time connection load balancing feature enables routing of work requests to an instance that offers the best performance, minimizing the need to relocate work.

Figure 22-1 illustrates run-time connection load balancing. When run-time connection load balancing is enabled on the implicit connection cache, the following steps occur:

1. A client requests a connection from the connection cache by calling the `getConnection` method on the `DataSource` object.
2. The run-time connection load balancing mechanism selects the connection that belongs to the best instance from the connection cache. In Figure 22-1, this could be either Instance1 or Instance2.
3. The client receives the connection that would process the work request with the best response time.

Figure 22-1 Run-Time Connection Load Balancing

![The run-time connection load balancing feature.](https://docs.oracle.com/cd/E11882_01/java.112/e16548/img/rlb.gif "The run-time connection load balancing feature.")  
[Description of "Figure 22-1 Run-Time Connection Load Balancing"](https://docs.oracle.com/cd/E11882_01/java.112/e16548/img_text/rlb.htm)  

Connection retrieval based on the load balancing advisory is automatic. A request for a connection is serviced by selecting a connection based on the service goal as determined by the Load Balancing Advisory. The service goal determines whether the connection provides best service quality, that is, how efficiently a single transaction completes, or best throughput, that is, how efficiently an entire job or long-running query completes. The advisory is used by the connection cache as long as the events are posted by Oracle Real Application Clusters. When the events stop arriving, the connection cache reverts to random retrieval of connections from the cache.

Run-time connection load balancing relies on the Oracle Notification Service (ONS) infrastructure. It uses the same out-of-band ONS event mechanism that is used for Fast Connection Failover processing. As a result, run-time connection load balancing is enabled by default when Fast Connection Failover is enabled. There is no additional setup or configuration of ONS required to benefit from run-time connection load balancing.

See Also:

["Using Fast Connection Failover"](fstconfo.md)

## Enabling Run-Time Connection Load Balancing

To enable and use run-time connection load balancing, you must configure the Oracle Real Application Clusters database in the following manner:

- The service goal must be set to one of the following:
	- `DBMS_SERVICE.SERVICE_TIME`
		- `DBMS_SERVICE.THROUGHPUT`
- The connection balancing goal must be set to `SHORT`.

These goals must be set when calling `dbms_service.create_service` or `dbms_service.modify_service`. The service goal can be set using the `goal` parameter, and the connection balancing goal can be set using the `clb_goal` parameter.

Note:

You can set the connection balancing goal to `LONG`. However, this is mostly useful for closed workloads, that is, when the rate of completing work is equal to the rate of starting new work.