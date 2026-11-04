---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-INSTANCE_PING.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.10 V$INSTANCE\_PING

`V$INSTANCE_PING` provides information about measured latency of the interconnect for all instances in an Oracle Real Application Clusters (Oracle RAC) environment.

In an Oracle RAC environment, every few seconds the PING process of each instance checks the response of the interconnect to all instances of the same database.

It sends two messages. One message is 500 bytes in size (referred to in the column descriptions as 500B), and the other is 8 kilobytes in size (referred to in column descriptions as 8K).

For each message sent to each instance, the amount of time it took to get a response back is measured (in microseconds). The view records the latest measurements as well as cumulative data since instance startup.

| Column | Datatype | Description |
| --- | --- | --- |
| `INSTANCE` | `NUMBER` | The instance communicated with. In the V$ view for each instance, there is one row for that instance, and in the GV$ view for each instance, there is also one row for that instance, so there are n <sup>2</sup> rows for n instances. |
| `CURRENT_500B` | `NUMBER` | The latest response time for the 500B message (in microseconds) |
| `AVERAGE_500B` | `NUMBER` | The average response time for the 500B messages since instance startup (in microseconds). Note that `AVERAGE_500B` should be the same as `WAIT_TIME_500B/COUNT_500B`. |
| `MAX_500B` | `NUMBER` | The maximal response time for the 500B messages since instance startup (in microseconds) |
| `COUNT_500B` | `NUMBER` | The number of measurements for the 500B messages since instance startup |
| `WAIT_TIME_500B` | `NUMBER` | The sum of all response times for the 500B messages since instance startup (in microseconds) |
| `WAIT_TIME_SQUARED_500B` | `NUMBER` | The sum of the response time squared for 500B messages since instance startup. The unit is in microseconds squared and divided by 1000. |
| `CURRENT_8K` | `NUMBER` | The latest response time for the 8K message (in microseconds) |
| `AVERAGE_8K` | `NUMBER` | The average response time for the 8K messages since instance startup (in microseconds). Note that `AVERAGE_8K` should be the same as `WAIT_TIME_8K/COUNT_8K`. |
| `MAX_8K` | `NUMBER` | The maximal response time for the 8K messages since instance startup (in microseconds) |
| `COUNT_8K` | `NUMBER` | The number of measurements for the 8K messages since instance startup |
| `WAIT_TIME_8K` | `NUMBER` | The sum of all response times for the 8K messages since instance startup (in microseconds) |
| `WAIT_TIME_SQUARED_8K` | `NUMBER` | The sum of the response time squared for 8K messages since instance startup. The unit is in microseconds squared and divided by 16. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. For this view, the possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. |