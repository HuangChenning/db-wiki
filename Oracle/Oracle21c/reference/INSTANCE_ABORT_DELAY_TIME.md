---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/INSTANCE_ABORT_DELAY_TIME.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.161 INSTANCE\_ABORT\_DELAY\_TIME

`INSTANCE_ABORT_DELAY_TIME` specifies how much time to delay an internal initiated instance termination (in seconds), such as when an irrecoverable process dies or an irrecoverable instance error occurs.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `0` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` and higher |
| Basic | No |
| Oracle RAC | Different instances should use the same value. |

This parameter does not apply to a `SHUTDOWN` `ABORT` operation or any instance termination necessary to implement a user command.

Setting this parameter to a value greater than 0 enables a DBA to take some actions before a termination occurs due to an irrecoverable error. Note that since the instance is in an irrecoverable state, the DBA should not be too ambitious with the actions taken because some processes and/ or resources may be corrupted or unavailable, making complex actions impossible. Oracle does not guarantee what it is possible when an instance is in this state. A message is written to the alert log when the delayed termination is initiated. The value will not apply in the case of PMON death.

The larger the specified value, the longer the instance stays up, and the potential increases for other problems to occur. If you set this parameter, Oracle recommends setting it to a value between 0 and 60.