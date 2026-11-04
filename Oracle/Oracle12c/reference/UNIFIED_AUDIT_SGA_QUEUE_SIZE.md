---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/UNIFIED_AUDIT_SGA_QUEUE_SIZE.html
tags:
  - oracle
  - 12c
  - reference
---

`UNIFIED_AUDIT_SGA_QUEUE_SIZE` specifies the size of SGA queue for unified auditing.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` MB |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 1 MB to 30 MB |
| Basic | No |
| Oracle RAC | Multiple instances can have different values |

`UNIFIED_AUDIT_SGA_QUEUE_SIZE` can be useful when queued-write mode is used for unified auditing. In queued-write mode, audit records are first written to the SGA queue. When the SGA queue reaches a particular threshold, the audit records are flushed to the `AUDSYS` schema table. The SGA queue size should be tuned according to the audit data generation. If large numbers of audit records are generated very frequently, you can increase the size of SGA queue, so that frequent flushes of queue data can be prevented. Similarly, if fewer audit records are generated, a smaller size can be used for the SGA queue.

Note:

The `UNIFIED_AUDIT_SGA_QUEUE_SIZE` initialization parameter is deprecated in Oracle Database 12c Release 2 (12.2.0.1), and may be desupported in a future release.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=DBSEG631) for more information about writing unified audit trail records to the `AUDSYS` schema.