---
title: ACTIVATE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000001915143.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# ACTIVATE

该语句用于激活恢复的租户。

## 语法

```sql
ALTER SYSTEM ACTIVATE STANDBY TENANT tenant_name;
```

## 语法说明

| 参数 | 描述 |
| --- | --- |
| tenant_name | 恢复成功的备租户名。当前每条命令仅支持切换一个租户。 |

## 示例

```shell
obclient> ALTER SYSTEM ACTIVATE STANDBY TENANT test_tenant;
```
