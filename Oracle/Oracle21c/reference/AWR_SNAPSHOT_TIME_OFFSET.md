---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/AWR_SNAPSHOT_TIME_OFFSET.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.30 AWR\_SNAPSHOT\_TIME\_OFFSET

`AWR_SNAPSHOT_TIME_OFFSET` specifies an offset for the Automatic Workload Repository (AWR) snapshot start time.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | There is no offset by default. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | 0 - 3599, or the special value 1000000 |
| Basic | No |
| Oracle RAC | Multiple instances should use the same value |

AWR snapshots normally start at the top of the hour (12:00, 1:00, 2:00, and so on). This parameter allows DBAs to specify an offset for the AWR snapshot start time.

This is a useful parameter to avoid CPU spikes from multiple instances all starting their AWR snapshots at the same time. If you have a large system with many instances on it (like many Exadata installations), and you are experiencing such CPU spikes, this parameter can be very useful.

The parameter is specified in seconds. Normally, you set it to a value less than 3600. If you set the special value 1000000 (1,000,000), you get an automatic mode, in which the offset is based on the database name.

The automatic mode is an effective way of getting a reasonable distribution of offset times when you have a very large number of instances running on the same node.