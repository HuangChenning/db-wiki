---
title: "删除 Catalog"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006123848.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 删除 Catalog

当一个 Catalog 不再使用时，可以使用 `DROP CATALOG [IF EXISTS] external_catalog_name;` 语句将其删除。

在删除 Catalog 时，如果指定了 `IF EXISTS`，即使要删除的 Catalog 不存在也不会报错；如果不指定 `IF EXISTS`，则会报错。

**示例如下：**

```
obclient> DROP CATALOG IF EXISTS test_odps_catalog;
```

## 相关文档

- [Catalog 概述](100-catalog-overview-of-mysql-mode.md)
- [创建 External Catalog](200-create-catalog-of-mysql-mode.md)
- [查看 Catalog](300-view-catalog-of-mysql-mode.md)
- [DROP CATALOG](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002977503)
