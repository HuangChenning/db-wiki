---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/XML_DB_EVENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.382 XML\_DB\_EVENTS

`XML_DB_EVENTS` enables or disables XML DB events.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `XML_DB_EVENTS = { enable \| disable }` |
| Default value | `enable` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Changing this parameter through an `ALTER SESSION` statement affects only the current session. Only users with the `XDBADMIN` role are allowed to change this parameter in a session.

Changing this parameter through an `ALTER SYSTEM` statement will make a systemwide change of this parameter; however, the change is only registered by new sessions started after the change. Currently running sessions need to be restarted to pick up the new change. Users must have the `ALTER SYSTEM` privilege to make a systemwide change.

See Also:

[Oracle XML DB Developer’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ADXDB-GUID-C7D110F1-CB15-475B-83E6-7C186DF0E119) for more information about this parameter