---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/undo_health-function.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 192.1.8 UNDO\_HEALTH Function

Checks whether there is any problem with the current setting of undo retention and undo tablespace size based on the historical information of a given period and provides recommendations to fix the problem.

Syntax

If the return value is 0, no problem is found. Otherwise, parameter `prob` and `reco` are the problem and recommendation on fixing the problem.

Viewing the output using the historical information in memory:

```
DBMS_UNDO_ADV.UNDO_HEALTH(
    prob OUT VARCHAR2,
    reco OUT VARCHAR2,
    rtn1 OUT VARCHAR2,
    retn OUT NUMBER,
    utbs OUT NUMBER);
```

Viewing the output using start time and end time:

```
DBMS_UNDO_ADV.UNDO_HEALTH(
    prob OUT VARCHAR2,
    reco OUT VARCHAR2,
    rtn1 OUT VARCHAR2,
    retn OUT NUMBER,
    utbs OUT NUMBER)
RETURN NUMBER;
```

Viewing the output using begin and end AWR snapshot ID:

```
DBMS_UNDO_ADV.UNDO_HEALTH(
    begin_snap IN  NUMBER,
    end_snap   IN  NUMBER,
    prob       OUT VARCHAR2,
    reco       OUT VARCHAR2,
    rtn1       OUT VARCHAR2,
    retn       OUT NUMBER,
    utbs       OUT NUMBER)
RETURN NUMBER;
```

Parameters

Table 192-9 UNDO\_HEALTH Function Parameters

| Parameter | Description |
| --- | --- |
| `start_time` | Start time of the given period. |
| `end_time` | End time of the given period. |
| `begin_snap` | Begin snapshot identifier. It is based on historical information in AWR from the `begin_snap` identifier. |
| `end_snap` | End snapshot identifier. It is based on historical information in AWR until the `end_snap` identifier. |
| `prob` | Problem that is being diagnosed.  For example, long running query may fail or undo tablespace cannot satisfy `undo_retention`. |
| `reco` | Recommendation for fixing the problem. |
| `rtn1` | Rationale for the recommendation. |
| `retn` | The numerical value of retention if the recommendation is to change retention. |
| `utbs` | The numerical value of undo tablespace size (in MB) if the recommendation is to change undo tablespace size. |