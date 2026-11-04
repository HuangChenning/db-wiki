---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SESSION_WAIT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.25 V$SESSION\_WAIT

`V$SESSION_WAIT` displays the current or last wait for each session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | Session identifier; maps to `V$SESSION.SID` |
| `SEQ#` | `NUMBER` | A number that uniquely identifies the current or last wait (incremented for each wait) |
| `EVENT` | `VARCHAR2(64)` | If the session is currently waiting, then the resource or event for which the session is waiting. If the session is not in a wait, then the resource or event for which the session most recently waited.  See Also: " [Oracle Wait Events](oracle-wait-events.md) " |
| `P1TEXT` | `VARCHAR2(64)` | Description of the first wait event parameter |
| `P1` | `NUMBER` | First wait event parameter (in decimal) |
| `P1RAW` | `RAW(8)` | First wait event parameter (in hexadecimal) <sup>Foot 1</sup> |
| `P2TEXT` | `VARCHAR2(64)` | Description of the second wait event parameter |
| `P2` | `NUMBER` | Second wait event parameter (in decimal) |
| `P2RAW` | `RAW(8)` | Second wait event parameter (in hexadecimal) <sup>Foot 1</sup> |
| `P3TEXT` | `VARCHAR2(64)` | Description of the third wait event parameter |
| `P3` | `NUMBER` | Third wait event parameter (in decimal) |
| `P3RAW` | `RAW(8)` | Third wait event parameter (in hexadecimal) <sup>Foot 1</sup> |
| `WAIT_CLASS_ID` | `NUMBER` | Identifier of the class of the wait event |
| `WAIT_CLASS#` | `NUMBER` | Number of the class of the wait event |
| `WAIT_CLASS` | `VARCHAR2(64)` | Name of the class of the wait event |
| `WAIT_TIME` | `NUMBER` | If the session is currently waiting, then the value is `0`. If the session is not in a wait, then the value is as follows:  - \> `0` - Value is the duration of the last wait in hundredths of a second - `-1` - Duration of the last wait was less than a hundredth of a second - `-2` - Parameter `TIMED_STATISTICS` was set to `false`  This column has been deprecated in favor of the columns `WAIT_TIME_MICRO` and `STATE`. |
| `SECONDS_IN_WAIT` | `NUMBER` | If the session is currently waiting, then the value is the amount of time waited for the current wait. If the session is not in a wait, then the value is the amount of time since the start of the last wait.  This column has been deprecated in favor of the columns `WAIT_TIME_MICRO` and `TIME_SINCE_LAST_WAIT_MICRO`. |
| `STATE` | `VARCHAR2(19)` | Wait state:  - `WAITING` - Session is currently waiting - `WAITED UNKNOWN TIME` - Duration of the last wait is unknown; this is the value when the parameter `TIMED_STATISTICS` is set to `false` - `WAITED SHORT TIME` - Last wait was less than a hundredth of a second - `WAITED KNOWN TIME` - Duration of the last wait is specified in the `WAIT_TIME` column |
| `WAIT_TIME_MICRO` | `NUMBER` | Amount of time waited (in microseconds). If the session is currently waiting, then the value is the time spent in the current wait. If the session is currently not in a wait, then the value is the amount of time waited in the last wait. |
| `TIME_REMAINING_MICRO` | `NUMBER` | Value is interpreted as follows:  - \> `0` - Amount of time remaining for the current wait (in microseconds) - `0` - Current wait has timed out - `-1` - Session can indefinitely wait in the current wait - NULL - Session is not currently waiting |
| `TOTAL_TIME_WAITED_MICRO` <sup>Foot 2</sup> | `NUMBER` | Total time for the current wait (in microseconds)  A wait includes code within its beginning and end that can encounter other waits as part of its implementation. For example, a wait might need to acquire a latch to check state to determine when the wait is satisfied, and the latch itself might enter a wait. In this case, when the latch wait ends and returns to the outer wait, the latch time is included in the value of this column, while the value of `WAIT_TIME_MICRO` is reset to start after the latch wait. |
| `HEUR_TIME_WAITED_MICRO` <sup>Foot 2</sup> | `NUMBER` | Heuristic wait time (in microseconds)  This value is calculated by attempting to group sequential waits that appear to be the same. |
| `TIME_SINCE_LAST_WAIT_MICRO` | `NUMBER` | Time elapsed since the end of the last wait (in microseconds). If the session is currently in a wait, then the value is `0`. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

<sup>Footnote 1</sup>

The `P1RAW`, `P2RAW`, and `P3RAW` columns display the same values as the `P1`, `P2`, and `P3` columns, except that the numbers are displayed in hexadecimal.

<sup>Footnote 2</sup> This column is available starting with Oracle Database 21c.

See Also:

" [TIMED\_STATISTICS](TIMED_STATISTICS.md) " and " [Oracle Wait Events](oracle-wait-events.md) "