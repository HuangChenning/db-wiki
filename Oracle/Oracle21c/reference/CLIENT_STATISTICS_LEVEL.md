---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/CLIENT_STATISTICS_LEVEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.40 CLIENT\_STATISTICS\_LEVEL

`CLIENT_STATISTICS_LEVEL` controls whether database clients report network statistics to the database.

This parameter applies only to clients that use Oracle Call Interface (OCI) to connect to the database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `CLIENT_STATISTICS_LEVEL = { TYPICAL \| OFF }` |
| Default value | `TYPICAL` |
| Modifiable | `ALTER SYSTEM ... DEFERRED` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Database clients sometimes have performance issues when interacting with the database over a network (LAN or WAN). You can use this parameter to enable clients to collect network statistics and periodically send them to the database, where the statistics are displayed in `AWR` and `V$` views. These statistics include TCP and SQL\*Net statistics. They complement existing database statistics and can be used to analyze, troubleshoot, and tune potential network performance or configuration issues.

Possible values:

- `TYPICAL`
	This setting enables clients to collect network statistics and periodically send them to the database.
- `OFF`
	This setting disables this feature. Clients will not send network statistics to the database.

When you modify this parameter, the new setting applies only to subsequent new connections to database clients.

Note:

To view a complete listing of the statistics that are collected and reported when this feature is enabled, issue the following SQL statement:

```
SELECT name FROM V$STATNAME
  WHERE name LIKE 'Client%' ORDER BY name;

NAME
-----------------------------------------------------
Client Advertised Receive Window
Client Advertised Send Window
Client Data Segments In
Client Data Segments Out
Client Lost Packets
Client Path Maximum Transmission Unit(MTU)
Client Send Congestion Window
Client Time (usec) Busy Sending Data
Client Time (usec) Busy Sending Data under Congestion
Client Time (usec) Last Ack Received
Client Time (usec) Last Ack Sent
Client Time (usec) Last Data Received
Client Time (usec) Last Data Sent
Client Time (usec) Limited by Receive Window
Client Time (usec) Limited by Send Buffer
Client Time (usec) Round Trip Time
Client Time (usec) Round Trip Time Variance
Client Total Bytes Acked
Client Total Bytes Received
Client Total Number of Retransmitted Packets
```