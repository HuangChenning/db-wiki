---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/connection-time-estimates-data-guard-switchover-or-failover.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Connection Time Estimates During Data Guard Switchover or Failover

The settings in the connect string allow for the following maximum times to connect during switchover or failover.

- Data Guard Switchover:
	RETRY\_COUNT X RETRY\_DELAY = 100 x 3 sec = 300 sec.
- Data Guard Failover:
	(3 SCANs x TRANSPORT\_CONNECT\_TIMEOUT) + (RETRY\_COUNT x (RETRY\_DELAY + (3 SCANS x TRANSPORT\_CONNECT\_TIMEOUT))) = (3 x 1) + (100 x (3 + (3 x 1)) = 3 + 600 = 603 sec

After Data Guard switchover / Data Guard failover to clu-site2, initial connections to clu-site2 take 3 seconds when clu-site1 is down (use of a connection pool helps mitigate this delay). When clu-site1 is reachable again (when it becomes a standby) connections are nearly instantaneous because the listener on the standby will answer immediately that the service is not there, prompting the client to connect to the other `ADDRESS_LIST`.

- If the switchover or failover completes much earlier than the maximum time, the application will experience less impact.
- Increase RETRY\_COUNT if your system might take longer than 300 sec to complete a switchover or failover. If you need more time to complete a Data Guard switchover, then change RETRY\_COUNT greater than 100.
- If you aren't using Oracle Clusterware, then your HOST address will not reference a SCAN VIP but a single VIP. This means that `TRANSPORT_CONNECT_TIMEOUT` must be set to higher or lower values to account for network latency.