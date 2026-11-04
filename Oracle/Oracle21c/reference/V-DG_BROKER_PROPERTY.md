---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DG_BROKER_PROPERTY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.173 V$DG\_BROKER\_PROPERTY

`V$DG_BROKER_PROPERTY` displays information about Oracle Data Guard broker properties.

| Column | Datatype | Description |
| --- | --- | --- |
| `MEMBER` | `VARCHAR2(31)` | Broker configuration member to which the property applies  This column displays the `DB_UNIQUE_NAME` initialization parameter for the member. If the member role is `CONFIGURATION`, then the configuration name is displayed. |
| `DATAGUARD_ROLE` | `VARCHAR2(18)` | Member role:  - `CONFIGURATION` - `FAR` `SYNC` `INSTANCE` - `LOGICAL` `STANDBY` - `PHYSICAL` `STANDBY` - `PRIMARY` - `RECOVERY` `APPLIANCE` - `SNAPSHOT` `STANDBY` |
| `PROPERTY` | `VARCHAR2(31)` | Property name |
| `PROPERTY_TYPE` | `VARCHAR2(12)` | Property type:  - `CONFIGURABLE` - `MONITORABLE` |
| `VALUE` | `VARCHAR2(4000)` | Property value  If `PROPERTY_TYPE` = `MONITORABLE`, then this column displays `(monitorable)`. |
| `VALUE_TYPE` | `VARCHAR2(11)` | Property value type:  - `BYTE` `STRING` - `INTEGER` - `STRING` - `UNDEFINED` - `XML` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This view is available starting with Oracle Database 21c.