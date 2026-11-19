---
title: "更新单个租户的备份配置"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286779.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 更新单个租户的备份配置

#### 注意

若需设置 `binding` 与 `piece_switch_interval`，则 `archive_base_uri` 仍需要设置，因为三者绑定，不支持增量设置。
