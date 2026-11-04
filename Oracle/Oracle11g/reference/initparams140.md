---
title: MAX_ENABLED_ROLES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams140.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `30` |
| Modifiable | No |
| Range of values | 1 to 148 |
| Basic | No |

Note:

The `MAX_ENABLED_ROLES` parameter is deprecated. It is retained for backward compatibility only.

Even if valid values are assigned to this parameter, they are ignored. There is no need to explicitly disable the parameter.

`MAX_ENABLED_ROLES` specifies the maximum number of database roles that users can enable, including roles contained within other roles. The actual number of roles that users can enable is 2 plus the value of `MAX_ENABLED_ROLES`, because each user has two additional roles, `PUBLIC` and the user's own role.

For example, if `MAX_ENABLED_ROLES` is set to `5`, then user `HR` can have seven roles enabled (the five enabled by `MAX_ENABLED_ROLES`, plus `PUBLIC` and `HR`).