---
title: DG_BROKER_START
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams077.htm
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

`DG_BROKER_START` enables Oracle to determine whether or not the Data Guard broker (DMON) process should be started. DMON is a non-fatal Oracle background process and exists as long as the instance exists, whenever this parameter is set to `true`.

If the site is never going to be configured in a Data Guard broker configuration, then you can leave the parameter unspecified and accept the default value of `false`. If the site is part of a Data Guard broker configuration, then automatic startup of the DMON process is simplified by setting `DG_BROKER_START` to `true` in the initialization parameter file.