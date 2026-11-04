---
title: "V$FS_OBSERVER_HISTOGRAM"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1151.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$FS_OBSERVER_HISTOGRAM` displays statistics that are based on the frequency of successful pings between the observer and primary database for different time intervals. These statistics can be used to select an appropriate value for the `FastStartFailoverThreshold` configuration property for your environment.

| Column | Datatype | Description |
| --- | --- | --- |
| `WAIT_TIME` | `NUMBER` | The time interval between a pair of successful observer pings (ping-pairs) to this instance. Note that the values in this column are the upper bound of the inter-ping interval samples represented by a given histogram bucket. If `WAIT_TIME` = number, then this column represents inter-ping intervals <= number that are not included in any smaller bucket. |
| `WAIT_COUNT` | `NUMBER` | The number of ping-pairs with an inter-ping interval that corresponds with this histogram bucket. |
| `LAST_UPDATE_TIME` | `VARCHAR2(20)` | The last time this row was updated |

Note:

This view is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbpropref.htm#DGBKR863) for more information about the `FastStartFailoverThreshold` configuration property