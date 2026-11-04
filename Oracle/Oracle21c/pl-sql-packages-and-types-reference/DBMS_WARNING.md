---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_WARNING.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 195 DBMS\_WARNING

The `DBMS_WARNING` package provides a way to manipulate the behavior of PL/SQL warning messages, in particular by reading and changing the setting of the `PLSQL_WARNINGS` initialization parameter to control what kinds of warnings are suppressed, displayed, or treated as errors. This package provides the interface to query, modify and delete current system or session settings.

This chapter contains the following topics:

- Security Model
- Summary of DBMS\_WARNING Subprograms

### 195.1 DBMS\_WARNING Security Model

Note that for all the following interfaces, if value of the scope parameter is `SYSTEM`, then the user must have `ALTER` `SYSTEM` privilege.

### 195.2 Summary of DBMS\_WARNING Subprograms

This table lists the `DBMS_WARNING` subprograms and briefly describes them.

Table 195-1 DBMS\_WARNING Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_WARNING\_SETTING\_CAT Procedure | Modifies the current `session` or `system` warning settings of the `warning_category` previously supplied |
| ADD\_WARNING\_SETTING\_NUM Procedure | Modifies the current `session` or `system` warning settings of the or `warning_number` previously supplied |
| GET\_CATEGORY Function | Returns the category name, given the message number |
| GET\_WARNING\_SETTING\_CAT Function | Returns the specific warning category in the session |
| GET\_WARNING\_SETTING\_NUM Function | Returns the specific warning number in the session |
| GET\_WARNING\_SETTING\_STRING Function | Returns the entire warning string for the current session |
| SET\_WARNING\_SETTING\_STRING Procedure | Replaces previous settings with the new value |

#### 195.2.1 ADD\_WARNING\_SETTING\_CAT Procedure

You can modify the current session's or system's warning settings with the value supplied in this procedure. The value will be added to the existing parameter setting if the value for the `warning_category` or `warning_value` has not been set, or override the existing value.

The effect of calling this function is same as adding the qualifier (`ENABLE` / `DISABLE` / `ERROR`) on the category specified to the end of the current session or system setting.

Syntax

```
DBMS_WARNING.ADD_WARNING_SETTING_CAT (
   warning_category    IN    VARCHAR2,
   warning_value       IN    VARCHAR2,
   scope               IN    VARCHAR2);
```

Parameters

Table 195-2 ADD\_WARNING\_SETTING\_CAT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `warning_category` | Name of the category. Allowed values are `ALL`, `INFORMATIONAL`, `SEVERE` and `PERFORMANCE`. |
| `warning_value` | Value for the category. Allowed values are `ENABLE`, `DISABLE`, and `ERROR`. |
| `scope` | Specifies if the changes are being performed in the session context or the system context. Allowed values are `SESSION` or `SYSTEM`. |

#### 195.2.2 ADD\_WARNING\_SETTING\_NUM Procedure

You can modify the current `session` or `system` warning settings with the value supplied in this procedure. If the value was already set, you will override the existing value.

The effect of calling this function is same as adding the qualifier (`ENABLE` / `DISABLE` / `ERROR`) on the category specified to the end of the current session or system setting.

Syntax

```
DBMS_WARNING.ADD_WARNING_SETTING_NUM (
   warning_number      IN    NUMBER,
   warning_value       IN    VARCHAR2,
   scope               IN    VARCHAR2);
```

Parameters

Table 195-3 ADD\_WARNING\_SETTING\_NUM Procedure Parameters

| Parameter | Description |
| --- | --- |
| `warning_number` | The warning number. Allowed values are all valid warning numbers. |
| `warning_value` | Value for the category. Allowed values are `ENABLE`, `DISABLE`, and `ERROR`. |
| `scope` | Specifies if the changes are being performed in the session context or the system context. Allowed values are `SESSION` or `SYSTEM`. |

Example 195-1 Enabling the Deprecation Warnings

This example shows how to enable the `DEPRECATE` pragma warnings using the DBMS\_WARNING package for the session.
```
BEGIN
  DBMS_WARNING.ADD_WARNING_SETTING_NUM (6019,
                                        'ENABLE',
                                        'SESSION');

  DBMS_WARNING.ADD_WARNING_SETTING_NUM (6020,
                                        'ENABLE',
                                        'SESSION');

  DBMS_WARNING.ADD_WARNING_SETTING_NUM (6021,
                                        'ENABLE',
                                        'SESSION');

  DBMS_WARNING.ADD_WARNING_SETTING_NUM (6022,
                                        'ENABLE',
                                        'SESSION');
END;
```

#### 195.2.3 GET\_CATEGORY Function

This function returns the category name, given the message number.

Syntax

```
DBMS_WARNING.GET_CATEGORY (
   warning_number  IN   pls_integer) 
RETURN VARCHAR2;
```

Parameters

Table 195-4 GET\_CATEGORY Function Parameters

| Parameter | Description |
| --- | --- |
| `warning_number` | The warning message number. |

#### 195.2.4 GET\_WARNING\_SETTING\_CAT Function

This function returns the specific warning category setting for the current session.

Syntax

```
DBMS_WARNING.GET_WARNING_SETTING_CAT (
   warning_category    IN    VARCHAR2)
RETURN warning_value;
```

Parameters

Table 195-5 GET\_WARNING\_SETTING\_CAT Function Parameters

| Parameter | Description |
| --- | --- |
| `warning_category` | Name of the category. Allowed values are all valid category names (`ALL`, `INFORMATIONAL`, `SEVERE` and `PERFORMANCE`). |

#### 195.2.5 GET\_WARNING\_SETTING\_NUM Function

This function returns the specific warning number setting for the current session.

Syntax

```
DBMS_WARNING.GET_WARNING_SETTING_NUM (
   warning_number      IN    NUMBER)
RETURN warning_value;
```

Parameters

Table 195-6 GET\_WARNING\_SETTING\_NUM Function Parameters

| Parameter | Description |
| --- | --- |
| `warning_number` | Warning number. Allowed values are all valid warning numbers. |

#### 195.2.6 GET\_WARNING\_SETTING\_STRING Function

This function returns the entire warning string for the current session.

Syntax

```
DBMS_WARNING.GET_WARNING_SETTING_STRING
 RETURN VARCHAR2;
```

Usage Notes

Use this function when you do not have `SELECT` or `READ` privilege on `v$parameter` or `v$paramater2` fixed tables, or if you want to parse the warning string yourself and then modify and set the new value using `SET_WARNING_SETTING_STRING`.

#### 195.2.7 SET\_WARNING\_SETTING\_STRING Procedure

This procedure replaces previous settings with the new value.

The warning string may contain mix of category and warning numbers using the same syntax as used on the right hand side of '=' when issuing an `ALTER SESSION` or `SYSTEM SET PLSQL_WARNINGS` command. This will have same effect as `ALTER SESSION` or `ALTER SYSTEM` command.

Syntax

```
DBMS_WARNING.SET_WARNING_SETTING_STRING (
   warning_value   IN   VARCHAR2,
   scope           IN   VARCHAR2);
```

Parameters

Table 195-7 SET\_WARNING\_SETTING\_STRING Procedure Parameters

| Parameter | Description |
| --- | --- |
| `warning_value` | The new string that will constitute the new value. |
| `scope` | This will specify if the changes are being done in the session context, or system context. Allowed values are `SESSION` or `SYSTEM`. |