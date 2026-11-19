---
title: "删除 Catalog"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004840209.html"
tags:
  - oceanbase
  - distributed
  - ref-database-object-management
---

# 删除 Catalog

当一个 Catalog 不再使用时，可以使用 `DROP CATALOG [IF EXISTS] external_catalog_name;` 语句将其删除。

在删除 Catalog 时，如果指定了 `IF EXISTS`，即使要删除的 Catalog 不存在也不会报错；如果不指定 `IF EXISTS`，则会报错。

**示例如下：**

```shell
obclient> DROP CATALOG IF EXISTS test_odps_catalog;
```

## 相关文档

* [Catalog 概述](100.catalog-overview-of-mysql-mode.md)
* [创建 External Catalog](200.create-catalog-of-mysql-mode.md)
* [查看 Catalog](300.view-catalog-of-mysql-mode.md)
* [DROP CATALOG](../../../500.sql-reference/100.sql-syntax/200.common-tenant-of-mysql-mode/600.sql-statement-of-mysql-mode/3350.drop-catalog-of-mysql-mode.md)
