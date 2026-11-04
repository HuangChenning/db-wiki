---
title: RESOURCE_MANAGER_PLAN
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams218.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `RESOURCE_MANAGER_PLAN =` `plan_name` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Any valid character string |

`RESOURCE_MANAGER_PLAN` specifies the top-level resource plan to use for an instance. The resource manager will load this top-level plan along with all its descendants (subplans, directives, and consumer groups). If you do not specify this parameter, the resource manager is off by default.

You can change the setting of this parameter using the `ALTER SYSTEM` statement to turn on the resource manager (if it was previously off) or to turn off the resource manager or change the current plan (if it was previously on). If you specify a plan that does not exist in the data dictionary, Oracle returns an error message.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on resource plans
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information on the `DBMS_RESOURCE_MANAGER` and `DBMS_RESOURCE_MANAGER_PRIVS` packages
- ["DBA\_RSRC\_PLANS"](statviews_4230.md), ["DBA\_RSRC\_PLAN\_DIRECTIVES"](statviews_4229.md), and the various `V$RSRC_*` dynamic performance views in [Part I](dynviews_part.md) for information on existing resource plans