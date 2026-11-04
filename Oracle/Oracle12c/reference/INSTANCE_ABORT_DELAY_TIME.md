---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/INSTANCE_ABORT_DELAY_TIME.html
tags:
  - oracle
  - 12c
  - reference
---

`INSTANCE_ABORT_DELAY_TIME` specifies how much time to delay an internal initiated instance abort (in seconds), such as when a fatal process dies or an unrecoverable instance error occurs.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` and higher |
| Basic | No |
| Oracle RAC | Different instances should use the same value. |

This parameter does not apply to a shutdown abort operation or any abort necessary to implement a user command.

Setting this parameter to a value greater than 0 enables a DBA to take some actions before an abort occurs due to a fatal error. Note that since the instance is in a fatal state, the DBA should not be too ambitious with the actions taken because some processes and/ or resources may be corrupted or unavailable, making complex actions impossible. Oracle does not guarantee what it is possible when an instance is in this state. A message is written to the alert log when the delayed abort is initiated. The value will not apply in the case of PMON death.

The larger the specified value, the longer the instance stays up, and the potential increases for other problems to occur. If you set this parameter, Oracle recommends setting it to a value between 0 and 60.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).