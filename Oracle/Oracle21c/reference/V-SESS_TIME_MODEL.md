---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESS_TIME_MODEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.16 V$SESS\_TIME\_MODEL

`V$SESS_TIME_MODEL` displays the session-accumulated time for various operations. The time reported is the total elapsed or CPU time (in microseconds). Any timed operation will buffer at most 5 seconds of time data. Specifically, this means that if a timed operation (such as SQL execution) takes a long period of time to perform, the data published to this view is at most missing 5 seconds of the time accumulated for the operation.

The time values are 8-byte integers and can therefore hold approximately 580,000 years of time before wrapping. Background process time is not included in a statistic value unless the statistic is specifically for background processes.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session ID (same as in `V$SESSION`) |
| `STAT_ID` | `NUMBER` | Statistic identifier for the time statistic |
| `STAT_NAME` | `VARCHAR2(64)` | Name of the statistic (see Table 10-1) |
| `VALUE` | `NUMBER` | Amount of time (in microseconds) that the session has spent in this operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Table 10-1 V$SESS\_TIME\_MODEL and V$SYS\_TIME\_MODEL Statistics

| Statistic Name | Description |
| --- | --- |
| DB time | Amount of elapsed time (in microseconds) spent performing Database user-level calls. This does not include the elapsed time spent on instance background processes such as PMON. |
| DB CPU | Amount of CPU time (in microseconds) spent on database user-level calls. This does not include the CPU time spent on instance background processes such as PMON. |
| background elapsed time | Amount of elapsed time (in microseconds) consumed by database background processes. |
| background CPU time | Amount of CPU time (in microseconds) consumed by database background processes. |
| sequence load elapsed time | Amount of elapsed time spent getting the next sequence number from the data dictionary. If a sequence is cached, then this is the amount of time spent replenishing the cache when it runs out. No time is charged when a sequence number is found in the cache. For non-cached sequences, some time will be charged for every nextval call. |
| parse time elapsed | Amount of elapsed time spent parsing SQL statements. It includes both soft and hard parse time. |
| hard parse elapsed time | Amount of elapsed time spent hard parsing SQL statements. |
| SQL execute elapsed time | Amount of elapsed time SQL statements are executing. Note that for select statements this also includes the amount of time spent performing fetches of query results. |
| connection management call elapsed time | Amount of elapsed time spent performing session connect and disconnect calls. |
| failed parse elapsed time | Amount of time spent performing SQL parses which ultimately fail with some parse error. |
| failed parse (out of shared memory) elapsed time | Amount of time spent performing SQL parses which ultimately fail with error `ORA-04031`. |
| hard parse (sharing criteria) elapsed time | Amount of elapsed time spent performing SQL hard parses when the hard parse resulted from not being able to share an existing cursor in the SQL cache. |
| hard parse (bind mismatch) elapsed time | Amount of elapsed time spent performing SQL hard parses when the hard parse resulted from bind type or bind size mismatch with an existing cursor in the SQL cache. |
| PL/SQL execution elapsed time | Amount of elapsed time spent running the PL/SQL interpreter. This does not include time spent recursively executing/parsing SQL statements or time spent recursively executing the Java VM. |
| PL/SQL compilation elapsed time | Amount of elapsed time spent running the PL/SQL compiler. |
| inbound PL/SQL rpc elapsed time | Time inbound PL/SQL remote procedure calls have spent executing. It includes all time spent recursively executing SQL and JAVA, and therefore is not easily related to "PL/SQL execution elapsed time". |
| Java execution elapsed time | Amount of elapsed time spent running the Java VM. This does not include time spent recursively executing/parsing SQL statements or time spent recursively executing PL/SQL. |
| RMAN cpu time (backup/restore) | Amount of CPU time (in microseconds) spent in RMAN backup and restore operations. |
| repeated bind elapsed time | Amount of elapsed time spent giving new values to bind variables (rebinding). |
| OLAP engine elapsed time | Amount of time spent performing OLAP session transactions. This includes time spent on database user-level calls, SQL statement execution, and PL/SQL execution within the OLAP transaction. |
| OLAP engine CPU time | Amount of CPU time spent on OLAP session transactions. This includes time spent on database user-level calls, SQL statement execution, and PL/SQL execution within the OLAP transaction. |

The relationships between the statistics listed in Table 10-1 form two trees in which all the time reported by a child in the tree is contained within the parent in the tree. The following are the relationship trees; the number is the level in the given tree.

```
1) background elapsed time
    2) background cpu time
          3) RMAN cpu time (backup/restore)
1) DB time
    2) DB CPU
    2) connection management call elapsed time
    2) sequence load elapsed time
    2) sql execute elapsed time
    2) parse time elapsed
          3) hard parse elapsed time
                4) hard parse (sharing criteria) elapsed time
                    5) hard parse (bind mismatch) elapsed time
          3) failed parse elapsed time
                4) failed parse (out of shared memory) elapsed time
    2) PL/SQL execution elapsed time
    2) inbound PL/SQL rpc elapsed time
    2) PL/SQL compilation elapsed time
    2) Java execution elapsed time
    2) repeated bind elapsed time
```

The relationship between a parent and a child in the tree indicates containment only. Keep the following in mind regarding the tree:

- Children do not necessarily add up to the parent.
- Children are not necessarily exclusive (that is, they may overlap).
- The union of children does not necessarily cover the whole of the parent.

See Also:

" [V$SYS\_TIME\_MODEL](V-SYS_TIME_MODEL.md) "