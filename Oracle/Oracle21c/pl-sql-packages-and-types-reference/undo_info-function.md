---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/undo_info-function.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 192.1.9 UNDO\_INFO Function

This function retrieves information about the undo tablespace of the current instance.

Syntax

This function returns the undo tablespace name, maximum possible size for the undo tablespace, current undo retention value, and boolean values to verify if it is auto-extensible or if the undo tablespace has guaranteed undo retention.

```
DBMS_UNDO_ADV.UNDO_INFO(
    tbs_name       OUT VARCHAR2,
    tbs_size       OUT NUMBER,
    tbs_autoextend OUT BOOLEAN,
    tbs_retention  OUT NUMBER,
    tbs_guarantee  OUT BOOLEAN)
RETURN BOOLEAN;
```

Parameters

Table 192-10 UNDO\_INFO Function Parameters

| Parameter | Description |
| --- | --- |
| `tbs_name` | Name of the current undo tablespace the instance is using. |
| `tbs_size` | The size of the undo tablespace in MB, if the undo tablespace is `fixed-sized`. If the tablespace is `auto_extensible`, it is the maximum possible size of the undo tablespace in MB. |
| `tbs_autoextend` | `TRUE` if the undo tablespace is extensible, `FALSE` otherwise. |
| `tbs_retention` | The value of the `undo_retention` `init.ora` parameter. |
| `tbs_guarantee` | `TRUE` if the undo tablespace has guaranteed retention, `FALSE` otherwise. |