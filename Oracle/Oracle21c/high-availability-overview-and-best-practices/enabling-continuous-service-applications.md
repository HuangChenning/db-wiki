---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/enabling-continuous-service-applications.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 6 Enabling Continuous Service for Applications

Applications achieve continuous service easily when the underlying network, systems, and databases are always available.

To achieve continuous service in the face of unplanned outages and planned maintenance activities can be challenging. An MAA database architecture and its configuration and operational best practices is built upon redundancy and its ability to tolerate, prevent, and at times auto-repair failures.

However, applications can incur downtime whenever a failure hits a database instance, a database node, or the entire cluster or data center. Similarly, some planned maintenance activities may require restarting a database instance, a database node, or an entire database server to be restarted.

In all cases, following a simple checklist, your applications can incur zero or very little downtime whenever the database service that the application is connected to can be moved to another Oracle RAC instance or to another database.

See [Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md) for various levels and options to achieve continuous service for your application.

Drain Timeouts for Planned Maintenance Events

For planned maintenance events, some applications require time to complete their in-flight transactions.

The amount of time (`DRAIN_TIMEOUT`) for any workload to gracefully complete its in-flight transactions and move its sessions vary based on the workload characteristics. For short OLTP transactions, a `DRAIN_TIMEOUT` of 1 minute may be sufficient, while batch jobs might require 30 minutes. In some cases it might be best to suspend these long transactions to times outside the planned maintenance window.

The trade-off for configuring a longer `DRAIN_TIMEOUT` is that the planned maintenance window would be extended.

The following table outlines planned maintenance events that will incur Oracle RAC instance rolling restart and the relevant service drain timeout variables that may impact your application.

Table 6-1 Drain Timeout Variables for Planned Maintenance Events

| Planned Maintenance Event | Application Drain Timeout Variables |
| --- | --- |
| Exadata Database Host (Dom0) software changes | Exadata Host handles operating system (OS) shutdown with maximum timeout of 10 minutes.  OS shutdown calls an `rhphelper`, which has the following drain timeout settings:  - `DRAIN_TIMEOUT`: value used for services that do not have a `drain_timeout` defined. Default 180 - `MAX_DRAIN_TIMEOUT`: overrides any higher `drain_timeout` value defined for a given service. Default 300  Each Clusterware-managed service is also controlled by a `drain_timeout` attribute that can be lower than the above values.  See also: [Using RHPhelper to Minimize Downtime During Planned Maintenance on Exadata (Doc ID 2385790.1)](https://support.oracle.com/rs?type=doc&id=2385790.1) |
| Exadata Database Guest (DomU) software changes | Exadata `patchmgr` and `dbnodeupdate` software programs call `rhphelper`, which has the following drain timeout settings:  `DRAIN_TIMEOUT`: value used for services that do not have a `drain_timeout` defined. Default 180  `MAX_DRAIN_TIMEOUT`: overrides any higher `drain_timeout` value defined for a given service. Default 300  Each Clusterware-managed service is also controlled by a `drain_timeout` attribute that can be lower than the above values.  See also: [Using RHPhelper to Minimize Downtime During Planned Maintenance on Exadata (Doc ID 2385790.1)](https://support.oracle.com/rs?type=doc&id=2385790.1) |
| Oracle Grid Infrastructure (GI) software changes or upgrade | The recommend steps are described in [Graceful Application Switchover in RAC with No Application Interruption (Doc ID 1593712.1)](https://support.oracle.com/rs?type=doc&id=1593712.1).  Example:  `srvctl stop instance -o immediate                                         -drain_timeout 600 -failover -force`  Each Clusterware-managed service is also controlled by a `drain_timeout` attribute that can be lower than the above values. |
| Oracle Database Software changes | The recommend steps are described in [Graceful Application Switchover in RAC with No Application Interruption (Doc ID 1593712.1)](https://support.oracle.com/rs?type=doc&id=1593712.1).  Example:  `srvctl stop instance -o immediate                                         -drain_timeout 600 -failover -force`  Each Clusterware-managed service is also controlled by a `drain_timeout` attribute that can be lower than the above values. |

See also:

[Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md)