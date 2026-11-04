---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOCKDOWN_RULES.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.44 V$LOCKDOWN\_RULES

`V$LOCKDOWN_RULES` displays information about lockdown profile rules that are applicable in the pluggable database (PDB) where this view is queried.

| Column | Datatype | Description |
| --- | --- | --- |
| `RULE_TYPE` | `VARCHAR2(128)` | Type of the rule:  - `STATEMENT` - `FEATURE` - `OPTION` |
| `RULE` | `VARCHAR2(128)` | Rule to be enabled or disabled |
| `CLAUSE` | `VARCHAR2(128)` | Clause of the statement |
| `CLAUSE_OPTION` | `VARCHAR2(128)` | Option of the clause |
| `STATUS` | `VARCHAR2(7)` | Status of the lockdown profile:  - `ENABLE` - `DISABLE` - `EMPTY` |
| `USERS` | `VARCHAR2(6)` | Type of users affected by the rule:  - `ALL` - `LOCAL` - `COMMON` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs - `1`: This value is used for rows containing data that pertain to only the root. - n: Where n is the applicable container ID for the rows containing data |

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBSEG-GUID-AB5E62DB-7E2A-4B5A-BA96-A2BD2DF15275) for more information about PDB lockdown profiles