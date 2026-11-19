---
title: oceanbase.DBA_OB_TABLET_TO_LS
book: "系统视图"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005284460.html"
tags:
  - oceanbase
  - distributed
  - ref-system-views
---

# oceanbase.DBA_OB_TABLET_TO_LS

<main id="notice" type='explain'>
<h4>说明</h4>
<p>该视图从 V4.0.0 版本开始引入。</p>
</main>

## 功能描述

展示本租户的所有 Tablet 列表以及 Tablet 所属的日志流信息。

## 字段说明

|   字段名称    |     类型     | 是否可以为 NULL |        描述        |
|-----------|------------|------------|------------------|
| TABLET_ID | bigint(20) | NO         | TABLET ID        |
| LS_ID     | bigint(1)  | NO         | TABLET 所属的日志流 ID |

## 查询示例

系统租户查询本租户的 Tablet 列表信息，展示前 5 条信息。

```shell
obclient [oceanbase]> SELECT * FROM oceanbase.DBA_OB_TABLET_TO_LS LIMIT 5;
```

查询结果如下所示：

```shell
+-----------+-------+
| TABLET_ID | LS_ID |
+-----------+-------+
|         1 |     1 |
|    100001 |     1 |
|    100002 |     1 |
|    100003 |     1 |
|     50003 |     1 |
+-----------+-------+
5 rows in set
```
