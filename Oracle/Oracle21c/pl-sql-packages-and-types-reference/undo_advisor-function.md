---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/undo_advisor-function.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 192.1.6 UNDO\_ADVISOR Function

This function uses the advisor framework to check if there is any problem with the current instance and provide recommendations.

Syntax

Note:

This function should be used when `undo_management` is set to auto.

Viewing the output using the historical information in memory:

```
DBMS_UNDO_ADV.UNDO_ADVISOR(
    instance_id IN NUMBER)
RETURN VARCHAR2;
```

Viewing the output using start time and end time:

```
DBMS_UNDO_ADV.UNDO_ADVISOR(
    start_time  IN DATE,
    end_time    IN DATE,
    instance_id IN NUMBER)
RETURN VARCHAR2;
```

Viewing the output using begin and end AWR snapshot ID:

```
DBMS_UNDO_ADV.UNDO_ADVISOR(
    begin_snap  IN NUMBER,
    end_snap    IN NUMBER,
    instance_id IN NUMBER)
RETURN VARCHAR2;
```

Parameters

Table 192-7 UNDO\_ADVISOR Function Parameters

| Parameter | Description |
| --- | --- |
| `start_time` | Start time of the given period. |
| `end_time` | End time of the given period. |
| `begin_snap` | Begin snapshot identifier. It is based on historical information in AWR from the `begin_snap` identifier. |
| `end_snap` | End snapshot identifier. It is based on historical information in AWR until the `end_snap` identifier. |
| `instance_id` | Instance ID of the current instance. |