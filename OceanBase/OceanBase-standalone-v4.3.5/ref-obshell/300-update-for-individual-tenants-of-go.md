---
title: "更新单个租户备份配置"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003976115.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 更新单个租户备份配置

#### 注意

若需设置 `binding` 与 `piece_switch_interval`，则 `archive_base_uri` 仍需要设置，因为三者绑定，不支持增量设置。

#### 说明

建议先查看 [obshell-sdk-go 快速上手](100-quickstart-of-go.md) 内容，了解如何使用 obshell-sdk-go。
