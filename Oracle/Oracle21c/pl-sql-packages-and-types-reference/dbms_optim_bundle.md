---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/dbms_optim_bundle.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 124 DBMS\_OPTIM\_BUNDLE

The `DBMS_OPTIM_BUNDLE` package is used to manage the installed but disabled module bug fixes which cause an execution plan change.

This chapter contains the following topics:

### 124.1 DBMS\_OPTIM\_BUNDLE Security Model

The `DBMS_OPTIM_BUNDLE` package runs with the privileges of the user starting the package. DBA role is required to run this package.

### 124.2 Summary of DBMS\_OPTIM\_BUNDLE Subprograms

This table lists the `DBMS_OPTIM_BUNDLE` subprograms and briefly describes them.

Table 124-1 DBMS\_OPTIM\_BUNDLE Package Subprograms

| Subprogram | Description |
| --- | --- |
| ENABLE\_OPTIM\_FIXES Procedure | This procedure enables or disables fixes with plan changes up to the latest installed release update. |
| GETBUGSFORBUNDLE Procedure | This procedure displays execution plan bug fixes applied as part of release updates. |
| LISTBUNDLESWITHFCFIXES Procedure | This procedure lists the release update names and release update IDs of release updates with fix control fixes. |
| SET\_FIX\_CONTROLS Procedure | This procedure enables or disables a list of fixes with `_fix_controls`. |

#### 124.2.1 ENABLE\_OPTIM\_FIXES Procedure

The `DBMS_OPTIM_BUNDLE` subprogram, `ENABLE_OPTIM_FIXES` procedure enables or disables fixes with plan changes up to the latest installed release update.

Syntax

```
DBMS_OPTIM_BUNDLE.ENABLE_OPTIM_FIXES ( 
   action                           IN  VARCHAR2  DEFAULT 'OFF', 
   scope                            IN  VARCHAR2  DEFAULT 'MEMORY',
   current_setting_precedence       IN  VARCHAR2  DEFAULT 'YES');
```

Parameters

Table 124-2 ENABLE\_OPTIM\_FIXES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `action` | Enables or disables all of the installed but disabled execution plan bug fixes up to and including the current release update.  The possible values are: - `ON` -enables the bundle fixes. - `OFF` -disables bundle fixes by setting the `_fix_controls` to the value `0`. It will not remove `_fix_control` entries from `SPFILE`.  The default value is `OFF`. |
| `scope` | The scope of enabling or disabling the installed but disabled execution plan bug fixes.  The possible values are: - `MEMORY` - `SPFILE` - `BOTH` - `INITORA`  `MEMORY` / `SPFILE` / `BOTH`: These three input values enables or disables the fixes in a given scope.  `INITORA`: This input value will just display manual command syntax that the user needs to manually enter into the database's `init.ora` file in order to enable or disable execution plan bug fixes. When using `SCOPE=INITORA` in this way, the `current_setting_precedence` field has no significance. |
| `current_setting_precedence` | Sets the precedence of environment settings or release update settings, where these settings are in conflict.  The possible values are: - `YES` -the current environment settings take precedence in case of conflict - `NO` -release update settings take precedence in case of conflict  The default value is `YES`. |

Examples

To enable all of the installed but disabled execution plan bug fixes up to and including those from the current release update:

```
SQL> execute dbms_optim_bundle.enable_optim_fixes('ON','BOTH', 'YES');
```

This instruction would enable all fixes, in both `MEMORY` and in the persistant `SPFILE`, with a precedence of current setting.

Exceptions

The following exceptions are raised by the `ENABLE_OPTIM_FIXES                Procedure`:
- `ORA-20001`: Bad input value
- `ORA-20002`: Internal or other errors

#### 124.2.2 GETBUGSFORBUNDLE Procedure

The `DBMS_OPTIM_BUNDLE` subprogram, `GETBUGSFORBUNDLE` procedure displays execution plan bug fixes applied as part of release updates.

Syntax

```
DBMS_OPTIM_BUNDLE.GETBUGSFORBUNDLE ( 
   bundleid            IN  NUMBER  DEFAULT NULL);
```

Parameters

Table 124-3 GETBUGSFORBUNDLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `bundleid` | The release update ID.  If `NULL`, the execution plan bug fixes from the latest bundle is displayed. If a bundle ID is specified, then the execution plan bug fixes up to the specified bundle is displayed.  The default value is `NULL`. |

Examples

To view a listing of the installed but disabled execution plan bug fixes from the most recent release update applied:

```
SQL> set serveroutput on;
SQL> execute dbms_optim_bundle.getbugsforbundle;

19.8.0.0.200714DBRU:
   Bug: 29304314, fix_controls: 29304314
   Bug: 29930457, fix_controls: 29930457
```

The above example lists the installed but disabled execution plan bug fixes from the `19.8.0.0.200714DBRU` release.

To view a listing of the installed but disabled execution plan bug fixes from release updates up to and including release update 171017:

```
SQL> execute dbms_optim_bundle.getbugsforbundle(171017);
```

Exceptions

The following exceptions are raised by the `GETBUGSFORBUNDLE                Procedure`:
- `ORA-20001`: Bad input value
- `ORA-20002`: Internal or other errors

#### 124.2.3 LISTBUNDLESWITHFCFIXES Procedure

The `DBMS_OPTIM_BUNDLE` subprogram, `LISTBUNDLESWITHFCFIXES` procedure lists the release update names and release update IDs of release updates with fix control fixes.

Syntax

```
DBMS_OPTIM_BUNDLE.LISTBUNDLESWITHFCFIXES ( );
```

Examples

To view the release update names and release update IDs:

```
SQL> set serveroutput on
SQL> exec dbms_optim_bundle.listBundlesWithFCFixes;
   bundleId: 190719, bundleName: 19.4.0.0.190719DBRU
   bundleId: 191015, bundleName: 19.5.0.0.191015DBRU
   bundleId: 200414, bundleName: 19.7.0.0.200414DBRU
   bundleId: 200714, bundleName: 19.8.0.0.200714DBRU
   bundleId: 201020, bundleName: 19.9.0.0.201020DBRU
   bundleId: 210119, bundleName: 19.10.0.0.210119DBRU
   bundleId: 210420, bundleName: 19.11.0.0.210420DBRU
   bundleId: 210720, bundleName: 19.12.0.0.210720DBRU

   PL/SQL procedure successfully completed.
```

Exceptions

The following exception is raised by the `LISTBUNDLESWITHFCFIXES                Procedure`:

`ORA-20002`: Internal or other errors

#### 124.2.4 SET\_FIX\_CONTROLS Procedure

The `DBMS_OPTIM_BUNDLE` subprogram, `SET_FIX_CONTROLS` procedure enables or disables a list of fixes with `_fix_controls`. The fixes can be present in a base version, in a release update, or in a one-off release. This procedure appends the new fix control settings to the existing ones.

Syntax

```
DBMS_OPTIM_BUNDLE.SET_FIX_CONTROLS ( 
   fix_control_string               IN  VARCHAR2,
   sid                              IN  VARCHAR2  DEFAULT '*', 
   scope                            IN  VARCHAR2  DEFAULT 'MEMORY',
   current_setting_precedence       IN  VARCHAR2  DEFAULT 'YES');
```

Parameters

Table 124-4 SET\_FIX\_CONTROLS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `fix_control_string` | Comma separated list of `fix_control:value` pair. For example: `'13329748:0,20355502:4,                            27060221:1'` |
| `sid` | The name of the instance on which `fix_control` setting need to be made.  Acceptable values are `*` or valid `instance_name` from `sys.gv$instance`. The default value is `*`. |
| `scope` | The scope of enabling or disabling the installed but disabled execution plan bug fixes.  The possible values are: - `MEMORY` - `SPFILE` - `BOTH`  The default value is `MEMORY`. |
| `current_setting_precedence` | Precedence of current setting over user supplied setting.  The possible values are: - `YES` –the current environment settings take precedence in case of conflict - `NO` –input settings take precedence in case of conflict  The default value is `YES`. |

Exceptions

The following exceptions are raised by the `SET_FIX_CONTROLS                Procedure`:
- `ORA-20001`: Bad input value
- `ORA-20002`: Internal or other errors