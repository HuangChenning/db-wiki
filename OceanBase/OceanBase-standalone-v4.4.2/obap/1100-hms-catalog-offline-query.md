---
title: "OceanBase 通过 HMS Catalog 离线查询加速"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077060.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# OceanBase 通过 HMS Catalog 离线查询加速

#### 说明

若 HMS 启用 Kerberos 认证，需额外提供 `KERBEROS_PRINCIPAL` 和 `KEYTAB` 参数。

#### 注意

Hive 表的 event_date 是 string 类型，需用 STR_TO_DATE() 转为 DATE 以保证类型一致。
