---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INMEMORY_ADG_ENABLED.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.149 INMEMORY\_ADG\_ENABLED

`INMEMORY_ADG_ENABLED` indicates whether in-memory for Active Data Guard is enabled in addition to the in-memory cache size.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `true` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | The same value should be used on all instances. If the value for this parameter is changed on one instance, the parameter’s value should be changed to the same value on the other instances. |

For Active Data Guard, media recovery needs to retrieve in-memory objects when applying redo and to invalidate the related objects after the query advance. This parameter controls whether media recovery does the retrieving and invalidating.

This parameter should be set on standby databases. The value of this parameter is meaningless on a primary database.

If the standby is an Oracle RAC instance, then all the different standby instances must have this parameter set to the same value.

This parameter is a dynamic system-modifiable parameter whose value can be changed only when Active Data Guard recovery is not running.

If you start multi-instance redo apply (MIRA) Active Data Guard recovery, all instances involved in MIRA must have the parameter set to the same value, otherwise MIRA will signal an error.

Example

If the standby is an Oracle RAC instance, this parameter should be set to the same value on all the Oracle RAC instances:

```
SQL> alter system set inmemory_adg_enabled=true sid='*';
```

See Also:

- " [INMEMORY\_SIZE](INMEMORY_SIZE.md) "
- [Oracle Database In-Memory Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=INMEM-GUID-F5934C5A-34DE-46BA-ABD2-727E548B8D9F) for more information about deploying an In-Memory Column Store (IM column store) in an Active Data Guard environment