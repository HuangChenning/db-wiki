---
title: "集中式数据库推荐配置"
book: "部署集中式版"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701714.html"
tags:
  - oceanbase
  - standalone
  - deploy
---

# 集中式数据库推荐配置

为确保在不同业务场景下用户都能基于 OceanBase 集中式数据库获得较好性能，此篇文档给出一些推荐配置。

| 参数类型 | 配置项名称/系统变量名称 | 推荐值 | 说明 |
|----|----|----|----|
| 集群级配置项 | [syslog_level](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502173) | WARN | 仅保留需要 DBA 关注的或者干预的非预期场景的日志 |
| 集群级配置项 | [enable_syslog_recycle](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502197) | 1 | 开启系统日志回收 |
| 集群级配置项 | [max_syslog_file_count](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502275) | 80 | 保留 80 个日志文件，总共占用 20G 日志空间。需要按照您的空间情况进行配置。 |
| 集群级配置项 | [enable_record_trace_log](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502133) | false | 用于设置是否记录追踪日志 |
| 集群级配置项 | [ignore_replay_checksum_error](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502260) | true | 关闭回放 checksum 校验，防止异常场景下集群启动失败。 |
| 集群级配置项 | \_lcl_op_interval | '0ms' | 关闭死锁检测 |
| 集群级配置项 | \_enable_defensive_check | false | 禁用 4377 校验 |

配置项操作如下：

在 sys 租户中执行以下语句，配置集群级配置项。

```
ALTER SYSTEM SET syslog_level = 'WARN';
ALTER SYSTEM SET enable_syslog_recycle = 1;
ALTER SYSTEM SET max_syslog_file_count = 80;
ALTER SYSTEM SET enable_record_trace_log = false;
ALTER SYSTEM SET ignore_replay_checksum_error = true;
ALTER SYSTEM SET _lcl_op_interval = '0ms';
ALTER SYSTEM SET _enable_defensive_check = false;
```
