---
title: LOG_CHECKPOINTS_TO_ALERT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams136.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SYSTEM` |
| Range of values | `true \| false` |
| Basic | No |

`LOG_CHECKPOINTS_TO_ALERT` lets you log your checkpoints to the alert file. Doing so is useful for determining whether checkpoints are occurring at the desired frequency.