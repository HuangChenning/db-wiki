---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/oracle-net-tns-string-parameters.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Oracle Net TNS String Parameters

The parameters used in the connect string are explained here.

CONNECT\_TIMEOUT

Applies when a connection to a listener address is attempted.

This setting represents the maximum time in which a connection using a specific `ADDRESS` endpoint has to complete. It includes the transport connection time and any other actions that must happen (redirection from SCAN VIP to listener VIP and finally to the foreground spawned process).

`CONNECT_TIMEMOUT` should be larger than `TRANSPORT_CONNECT_TIMEOUT`, otherwise `TRANSPORT_CONNECT_TIMEOUT` is effectively capped by `CONNECT_TIMEOUT`. When `TRANSPORT_CONNECT_TIMEOUT` is not specified, then `CONNECT_TIMEOUT` acts as the timeout for the entire connection attempt to an `ADDRESS` endpoint, both transport and final connection to the database foreground.

Oracle recommends the value for `CONNECT_TIMEOUT` be large enough to account for the value of `TRANSPORT_CONNECT_TIMEOUT`, in addition to potential delays that may occur when connecting to busy listeners and hosts. The value of 90 seconds in the example connect string is very generous and might need to be shortened in some cases. But, if it is too short, then the setting could be counter-productive because it causes additional attempts that can also fail, and can introduce more unproductive workload on the servers to handle connection requests that might be prematurely abandoned.

RETRY\_COUNT

If a connection attempt fails across all `ADDRESS_LISTS`, then additional attempts to connect beginning with the first `ADDRESS_LIST` will be made `RETRY_COUNT` times.

This is useful when a switchover or failover to a standby is in progress and the connection needs to keep trying until the operation is complete.

RETRY\_DELAY

Seconds in between retry attempts.

A short amount of time is given to allow the new primary database time to open. This parameter is used with `RETRY_COUNT` to wait a reasonable amount of time to connect to a newly opened database.

It is better to have short retry delays with many retry counts so the connection can complete close to the time the primary database opened.

TRANSPORT\_CONNECT\_TIMEOUT=1000ms

Allow up to 1000 milliseconds to connect to the listener using TCP hosts in the `ADDRESS`. If no connection is made, then try the next `ADDRESS`.

When an Oracle RAC SCAN host name is used, each IP in the SCAN address is expanded internally into a separate `ADDRESS` string. Each `ADDRESS` is then attempted if a connection attempt fails.

Adjust this parameter for your environment to minimize the time spent waiting for the listener endpoint connection to succeed. If the time is too short, you might give up on a connection attempt too soon, causing more delays and potentially a failure to connect. If the time is too long, then if the listener endpoint is unreachable, you might spend too much time waiting before giving up and trying another endpoint.

The host names specify SCAN VIPs. They are always available when using a cluster. This means that if a node or network is down, the VIP sends an instant reply, so that when connecting, the next address is used immediately if the service is not offered at the VIP address.

LOAD\_BALANCE=ON within ADDRESS\_LIST

When a `HOST` inside an `ADDRESS` resolves to multiple addresses for Oracle RAC SCAN, then all of the addresses are tried in a random order.

If you set `LOAD_BALANCE=OFF`, then the order is the same every time, which might overburden one of the SCAN listeners, so its recommended to set it to `ON`.

EXPIRE\_TIME

With Oracle Client 19c, `EXPIRE_TIME` can be used in tnsnames.ora connect descriptors to prevent firewalls from terminating idle connections and to adjust keepalive timeouts.

The general recommendation for `EXPIRE_TIME` is to use a value that is slightly less than half of the termination period. In older versions of Oracle Client, a tnsnames.ora connect descriptor option `ENABLE=BROKEN` can be used instead of `EXPIRE_TIME`. These settings can also aid detection of a terminated remote database server.