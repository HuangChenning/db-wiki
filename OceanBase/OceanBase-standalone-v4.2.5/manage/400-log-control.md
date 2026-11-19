---
title: "日志控制方式"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701762.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志控制方式

日志控制方式包括集群配置项、租户系统变量、SQL Hint 和信号量等，这些方式可用于管理和控制系统日志的相关行为。

## 通过配置项控制

系统日志相关的集群配置项：

| 配置项名 | 默认值 | 功能描述 |
|----|----|----|
| [enable_syslog_recycle](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502197) | False | 用于设置是否打开记录启动前的旧日志的开关。 |
| [enable_syslog_wf](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502302) | True | 用于设置是否把 WARN 以上级别的系统日志打印到一个单独的日志文件（日志文件的后缀为 `wf`）中。 |
| [enable_async_syslog](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502111) | True | 用于设置是否为 `observer.log`、`election.log` 和 `rootservice.log` 启用系统日志异步写。 |
| [max_syslog_file_count](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502275) | 0 | 用于设置在回收日志文件之前可以容纳的最大日志文件数量。 |
| [syslog_io_bandwidth_limit](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502143) | 30MB | 用于设置系统日志所能占用的磁盘 IO 带宽上限，超过带宽上限容量的系统日志将被丢弃。取值为 0 表示关闭系统日志。 |
| [syslog_level](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502173) | WDIAG | 用于设置系统日志级别。 |
| [syslog_disk_size](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502278) | 0M | 用于设置系统日志的磁盘空间上限。当系统日志的总大小将要达到该上限时，最旧的日志文件将会被删除，包括已压缩的日志文件。 |
| [syslog_compress_func](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502233) | none | 用于设置系统日志的压缩算法。 |
| [syslog_file_uncompressed_count](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502255) | 0 | 用于设置系统日志不压缩的文件数量。只有在 `syslog_compress_func` 取值不为 `none` 时才生效，且每一种系统日志文件单独计算数量。 |
| [alert_log_level](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502174) | INFO | 用于设置告警日志的级别。 |

## 通过系统变量控制

租户系统变量 `ob_log_level` 控制 Session 级日志级别。有关 `ob_log_level` 的详细信息请参见 [ob_log_level](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502608)。
