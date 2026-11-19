---
title: "物理恢复失败"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701875.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 物理恢复失败

#### 注意

- OceanBase 数据库当前仅支持将低版本的备份数据恢复到同版本或高版本中，但不支持将 V3.x 或 V2.x 版本的备份数据恢复到 V4.x 版本中。
- 对于 OceanBase 数据库 V4.1.0 版本，不支持恢复 OceanBase 数据库 V4.1.0 之前版本的数据。例如，OceanBase 数据库 V4.0.x 版本的备份数据不能恢复到 OceanBase 数据库 V4.1.0 版本中。

#### 注意

如果在 `rootservice.log` 中 `grep` 不到相关日志，可能是因为 `rootservice.log` 切了文件，可以执行 `grep "ob_restore_util" rootservice.log.* | grep "ret=\-4016"`。

#### 注意

由于从 V4.1.0 版本开始，OceanBase 数据库遵循所有恢复日志齐步走的策略，如果有日志流卡在 `6` 或者 `8`之前的状态，则可能会导致其他日志流的状态都卡在 `6` 不动。

#### 说明

日志从归档目录中恢复到租户的整个过程可能会耗费较长时间，该过程持续的时间长短主要取决于待恢复的日志量、归档介质的读取性能以及 OceanBase 数据库的压力等因素。

#### 注意

如果在 `observer.log` 中 `grep` 不到相关日志，可能是因为 `observer.log` 切了文件，可以执行 `grep "YFA00BA2D905-0005E5DEE6A2294E-0-0" observer.log.*`。

#### 注意

如果在 `observer.log` 中 `grep` 不到相关日志，可能是因为 `observer.log` 切了文件，可以 `grep "trace_id" observer.log.* | grep "WARN\|ERROR"`。

#### 注意

如果在 `rootservice.log` 中 `grep` 不到相关日志，可能是因为 `rootservice.log` 切了文件，可以 `grep "ob_restore_scheduler" rootservice.log.* | grep "WARN\|ERROR"`。
