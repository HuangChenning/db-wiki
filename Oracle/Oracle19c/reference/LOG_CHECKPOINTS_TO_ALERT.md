---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/LOG_CHECKPOINTS_TO_ALERT.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.192 LOG\_CHECKPOINTS\_TO\_ALERT

`LOG_CHECKPOINTS_TO_ALERT` lets you log your checkpoints to the alert log. Doing so is useful for determining whether checkpoints are occurring at the desired frequency.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `true \| false` |
| Basic | No |