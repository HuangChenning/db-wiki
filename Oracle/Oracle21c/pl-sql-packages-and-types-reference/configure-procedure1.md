---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/configure-procedure1.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## CONFIGURE Procedure

This procedure sets configuration options for auto zone map; specifically to enable or disable feature and to control foreground or background mode of the feature.

Syntax

```
DBMS_AUTO_ZONEMAP.CONFIGURE (
   parameter_name       IN    VARCHAR2,
   parameter_value      IN    VARCHAR2);
```

Parameters

Table 36-3 CONFIGURE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `parameter_name` | `AUTO_ZONEMAP_MODE` is the only configure parameter name that is currently allowed. If you specify any other name, an invalid argument error message is displayed. |
| `parameter_value` | The four values are allowed for this parameter: - `ON`: Turns on auto zone map feature completely. Both for foreground and background zone map creation and maintenance. - `OFF`: Turns off auto zone map feature completely. Both for foreground and background zone map creation and maintenance. - `FOREGROUND`: Turns on only for foreground zone map creation and maintenance. - `BACKGROUND`: Turns on only for background zone map creation and maintenance. |