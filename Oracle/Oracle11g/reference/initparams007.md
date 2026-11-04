---
title: ACTIVE_INSTANCE_COUNT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams007.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | There is no default value. |
| Modifiable | No |
| Range of values | 1 or >= the number of instances in the cluster. (Values other than 1 have no effect on the active or standby status of any instances.) |
| Basic | No |
| Oracle RAC | You must set this parameter for every instance, and multiple instances must have the same value. |

Note:

The `ACTIVE_INSTANCE_COUNT` parameter is deprecated. It is retained for backward compatibility only.

`ACTIVE_INSTANCE_COUNT` enables you to designate one instance in a two-instance cluster as the primary instance and the other instance as the secondary instance. This parameter has no functionality in a cluster with more than two instances.

When you set this parameter to 1, the first instance you start up becomes the primary instance and accepts client connections. The second instance starts up as a secondary instance and can accept client connections only if the first instance fails. In such an event, the secondary instance becomes the primary instance.

When the failed instance can once again be started up, it starts up as the secondary instance, and will not accept client connections unless the current primary instance fails.

Note:

This parameter functions only in a cluster with only two instances.