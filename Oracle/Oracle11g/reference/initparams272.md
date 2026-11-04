---
title: XML_DB_EVENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams272.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `XML_DB_EVENTS = { enable \| disable }` |
| Default value | `enable` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`XML_DB_EVENTS` enables or disables XML DB Events.

Changing this parameter through an `ALTER SESSION` statement affects only the current session. Only users with the `XDBADMIN` role are allowed to change this parameter in a session.

Changing this parameter through an `ALTER SYSTEM` statement will make a system-wide change of this parameter; however, the change is only registered by new sessions started after the change. Currently running sessions need to be restarted to pick up the new change. Users must have the `ALTER SYSTEM` privilege to make a system-wide change.