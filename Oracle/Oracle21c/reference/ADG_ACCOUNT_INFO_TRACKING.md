---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ADG_ACCOUNT_INFO_TRACKING.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.8 ADG\_ACCOUNT\_INFO\_TRACKING

`ADG_ACCOUNT_INFO_TRACKING` controls login attempts of users on Oracle Active Data Guard standby databases. It extends the control of user account security information.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ADG_ACCOUNT_INFO_TRACKING = { LOCAL \| GLOBAL }` |
| Default value | `LOCAL` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | The same value must be used on all instances. |

Setting `ADG_ACCOUNT_INFO_TRACKING` to `LOCAL` (the default value) continues to enforce the default behavior, by maintaining a local copy of users account information in the standby's in-memory view. Login failures are only tracked locally on a per database basis, and login is denied when the failure maximum is reached.

Setting the parameter to `GLOBAL` triggers a more secure behavior, by maintaining a single global copy of users account information across all Data Guard databases (primary and standby). Login failures across all databases in the Data Guard configuration count towards the maximum count and logins anywhere will be denied when the count is reached. This setting improves security against login attacks across a production database and all Active Data Guard standby databases.