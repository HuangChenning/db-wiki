---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_AUTOMATIC_LEVEL.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.150 INMEMORY\_AUTOMATIC\_LEVEL

`INMEMORY_AUTOMATIC_LEVEL` is used to enable the Automatic In-Memory feature, which automates the management of the In-Memory Column Store (IM column store) to help ensure that the working data set is in the IM column store at all times.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `INMEMORY_AUTOMATIC_LEVEL = { LOW \| MEDIUM \| HIGH \| OFF }` |
| Default value | `OFF` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | All instances should use the same value. |

Typically, among all the IM enabled segments, only a subset is actively queried at any time. This subset is known as the working data set. The working data set is expected to change over time for many applications.

`INMEMORY_AUTOMATIC_LEVEL` attempts to keep the working data set in the IM column store at all times by moving segments in and out of the IM column store based on access patterns.

Oracle recommends that you provision enough memory for the working data set to fit in the IM column store.

The following values can be set:

- `LOW`: The database evicts cold segments from the IM column store when it is under memory pressure.
- `MEDIUM`: The database evicts cold segments from the IM column store when it is under memory pressure. This level includes an additional optimization that ensures that any hot segment that was not populated because of memory pressure is populated first.
- `HIGH`: All segments in the database are enabled for the IM column store, except segments belonging to Oracle-maintained users and segments from external tables. Automatic In-Memory manages all segments enabled for the IM column store, keeping hot segments in the IM column store and evicting cold segments. This level includes an additional optimization that ensures that any hot segment that was not populated because of memory pressure is populated first.
- `OFF`: Automatic In-Memory is disabled. This value returns the IM column store to the behavior that existed prior to Oracle Database 18c, when the Automatic In-Memory features was introduced. If you do not expect a stable working data set, set the parameter to `OFF`. This is the default value.

See Also:

- [Oracle Database Licensing Information User Manual](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DBLIC-GUID-0F9EB85D-4610-4EDF-89C2-4916A0E7AC87) to learn which database offerings support the Automatic In-Memory feature
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-B2473D1F-AEAF-4802-9E28-85B3D823093C) for more information about configuring the Automatic In-Memory feature