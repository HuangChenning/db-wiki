---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FS_OBSERVER_HISTOGRAM.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.243 V$FS\_OBSERVER\_HISTOGRAM

`V$FS_OBSERVER_HISTOGRAM` displays statistics that are based on the frequency of successful pings between the observer and primary database for different time intervals. The wait event in this histogram is the observer's wait until pings to the primary succeed.

The histogram displays only when there were ping failures between the observer and the primary database.

No rows are shown in this view for unregistered observers.

These statistics can be used to select an appropriate value for the `FastStartFailoverThreshold` configuration property for your environment.

| Column | Datatype | Description |
| --- | --- | --- |
| `OBSERVER_NAME` | `VARCHAR2(513)` | The Fast-Start Failover observer name |
| `OBSERVER_HOST` | `VARCHAR2(513)` | The name of the host where this observer is running |
| `WAIT_TIME` | `NUMBER` | The time interval between a pair of successful observer pings (ping-pairs) to this instance. Note that the values in this column are the upper bound of the inter-ping interval samples represented by a given histogram bucket. If `WAIT_TIME` = number, then this column represents inter-ping intervals <= number that are not included in any smaller bucket.  The value in this column is the time (in seconds) that a ping failure lasted. |
| `WAIT_COUNT` | `NUMBER` | The number of ping-pairs with an inter-ping interval that corresponds with this histogram bucket.  If all pings have been successful so far, this column has a value of 0. |
| `LAST_UPDATE_TIME` | `VARCHAR2(20)` | The last time this row was updated |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DGBKR863) for more information about the `FastStartFailoverThreshold` configuration property

Example

Assume that the following shows the status of observer’s pings to the primary:

```
Ping time   Ping result
---------  -----------
1:00:00    SUCCESS
1:00:03    FAIL
1:00:06    FAIL
1:00:09    SUCCESS   => Wait time of 6 seconds
1:00:12    SUCCESS   
1:00:15    FAIL
1:00:18    FAIL
1:00:21    SUCCESS   => Wait time of 6 seconds
1:00:24    SUCCESS
1:00:27    FAIL
1:00:30    SUCCESS   => Wait time of 3 seconds
```

These ping results will result in the histogram view below:

```
WAIT_TIME   WAIT_COUNT   LAST_UPDATE_TIME
  3         1            1:00:30

  6         2            1:00:21

  9         0

 12         0

...
```

In this case, the `FastStartFailoverThreshold` value should be set to larger than 6 because communication between the observer and the primary sometimes fails for 6 seconds.