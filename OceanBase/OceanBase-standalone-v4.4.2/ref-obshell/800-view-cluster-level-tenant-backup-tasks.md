---
title: "查看集群级备份任务"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077908.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 查看集群级备份任务

本文介绍如何通过 API 查看集群级备份任务。

## 调用说明

### 接口约束

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/obcluster/backup/overview

### 返回结果

[TABLE]

CdbObBackupTask 的数据结构：

[TABLE]

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/obcluster/overview

### 返回示例

``` json
{
  "successful": true,
  "timestamp": "2024-10-12T18:12:51.179120149+08:00",
  "duration": 52,
  "status": 200,
  "traceId": "1868835c2071a85a",
  "data": {
    "statuses": [
      {
        "tenant_id": 1002,
        "task_id": 1,
        "job_id": 1,
        "incarnation": 1,
        "backup_set_id": 1,
        "start_timestamp": "2024-10-12T18:08:08.723714+08:00",
        "end_timestamp": "2024-10-12T18:10:43.487426+08:00",
        "status": "COMPLETED",
        "start_scn": 1728727696264250400,
        "end_scn": 1728727843446713000,
        "user_ls_start_scn": 1728727710694531300,
        "encryption_mode": "NONE",
        "input_bytes": 128825794,
        "output_bytes": 22320897,
        "output_rate_bytes": 144225.6503,
        "extra_meta_bytes": 0,
        "tablet_count": 596,
        "finish_tablet_count": 596,
        "macro_block_count": 61,
        "finish_macro_block_count": 61,
        "file_count": 0,
        "meta_turn_id": 1,
        "data_turn_id": 0,
        "result": 0,
        "comment": "",
        "path": "oss://oss-328067-1012-obshell/backup/archive/test/1/1002/data?host=oss-cn-hangzhou.aliyuncs.com"
      },
      {
        "tenant_id": 1004,
        "task_id": 1,
        "job_id": 1,
        "incarnation": 1,
        "backup_set_id": 1,
        "start_timestamp": "2024-10-12T18:08:08.760053+08:00",
        "end_timestamp": "2024-10-12T18:10:46.209384+08:00",
        "status": "COMPLETED",
        "start_scn": 1728727701874235100,
        "end_scn": 1728727846169762600,
        "user_ls_start_scn": 1728727714351766000,
        "encryption_mode": "NONE",
        "input_bytes": 101560294,
        "output_bytes": 23082192,
        "output_rate_bytes": 146600.7626,
        "extra_meta_bytes": 0,
        "tablet_count": 596,
        "finish_tablet_count": 596,
        "macro_block_count": 48,
        "finish_macro_block_count": 48,
        "file_count": 0,
        "meta_turn_id": 1,
        "data_turn_id": 0,
        "result": 0,
        "comment": "",
        "path": "oss://oss-328067-1012-obshell/backup/archive/test/1/1004/data?host=oss-cn-hangzhou.aliyuncs.com"
      }
    ]
  }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [查看集群级备份任务](800-view-cluster-level-tenant-backup-tasks-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [查看集群级备份任务](800-view-cluster-level-tenant-backup-tasks-of-go.md)。
