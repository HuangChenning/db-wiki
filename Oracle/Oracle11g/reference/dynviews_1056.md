---
title: "V$BACKUP_DEVICE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1056.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_DEVICE` displays information about supported backup devices. If a device type does not support named devices, then one row with the device type and a null device name is returned for that device type. If a device type supports named devices then one row is returned for each available device of that type. The special device type DISK is not returned by this view because it is always available.

| Column | Datatype | Description |
| --- | --- | --- |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of the backup device |
| `DEVICE_NAME` | `VARCHAR2(513)` | Name of the backup device |