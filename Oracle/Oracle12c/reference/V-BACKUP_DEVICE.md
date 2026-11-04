---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-BACKUP_DEVICE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$BACKUP_DEVICE` displays information about supported backup devices.

If a device type does not support named devices, then one row with the device type and a null device name is returned for that device type. If a device type supports named devices then one row is returned for each available device of that type. The special device type DISK is not returned by this view because it is always available.

| Column | Datatype | Description |
| --- | --- | --- |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of the backup device |
| `DEVICE_NAME` | `VARCHAR2(513)` | Name of the backup device |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |