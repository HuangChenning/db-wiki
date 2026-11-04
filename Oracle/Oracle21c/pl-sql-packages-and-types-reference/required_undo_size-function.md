---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/required_undo_size-function.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 192.1.5 REQUIRED\_UNDO\_SIZE Function

This function returns the required undo tablespace size (in MB) to satisfy certain undo retention value based on undo statistics available for a given period.

Syntax

Note:

Zero will be returned if the information about the given period is not available.

Viewing the output using the historical information in memory:

```
DBMS_UNDO_ADV.REQUIRED_UNDO_SIZE(
    retention IN NUMBER)
RETURN NUMBER;
```

Viewing the output using start time and end time:

```
DBMS_UNDO_ADV.REQUIRED_UNDO_SIZE(
    retention  IN NUMBER,
    start_time IN DATE,
    end_time   IN DATE)
RETURN NUMBER;
```

Viewing the output using begin and end AWR snapshot ID:

```
DBMS_UNDO_ADV.REQUIRED_UNDO_SIZE(
    retention  IN NUMBER,
    begin_snap IN NUMBER,
    end_snap   IN NUMBER)
RETURN NUMBER;
```

Parameters

Table 192-6 REQUIRED\_UNDO\_SIZE Function Parameters

| Parameter | Description |
| --- | --- |
| `retention` | Retention value you want to set for the `undo_retention` `init.ora` parameter. |
| `start_time` | Start time of the given period. |
| `end_time` | End time of the given period. |
| `begin_snap` | Begin snapshot identifier. It is based on historical information in AWR from the `begin_snap` identifier. |
| `end_snap` | End snapshot identifier. It is based on historical information in AWR until the `end_snap` identifier. |