---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-STATS_ADVISOR_RULES.html
tags:
  - oracle
  - 12c
  - reference
---

`V$STATS_ADVISOR_RULES` displays the rule definition information for each Optimizer Statistics Advisor rule.

| Column | Datatype | Description |
| --- | --- | --- |
| `RULE_ID` | `NUMBER` | ID of the rule |
| `NAME` | `VARCHAR2(64)` | Name of the rule |
| `RULE_TYPE` | `VARCHAR2(9)` | Type of the rule:  - `OBJECT` - `OPERATION` - `SYSTEM` |
| `DESCRIPTION` | `VARCHAR2(64)` | Description of the rule |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL-GUID-054F4B76-DD57-46EE-98EA-0FF04F49D1B3) for more information about Optimizer Statistics Advisor.