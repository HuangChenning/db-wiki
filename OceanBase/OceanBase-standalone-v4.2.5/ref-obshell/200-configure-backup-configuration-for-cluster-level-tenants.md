---
title: "设置集群级备份配置"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286778.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 设置集群级备份配置

本文介绍如何通过 API 设置集群级备份配置。

## 调用说明

### 接口约束

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

POST /api/v1/obcluster/backup/config

### 请求参数

[TABLE]

### 返回结果

[TABLE]

DagDetailDTO 信息的数据结构如下：

| 参数 | 类型 | 说明 |
|----|----|----|
| id | string | DAG 通用 ID。 |
| dag_id | int | DAG id，是记录在 OceanBase 数据库中的主键。 |
| name | string | DAG 名称。 |
| stage | int | DAG 的当前执行阶段。 |
| max_stage | int | DAG 执行过程中的总阶段数。 |
| state | string | DAG 执行状态。 |
| operator | string | DAG 执行操作类型。 |
| start_time | time.Time | DAG 执行起始时间。 |
| end_time | time.Time | DAG 执行结束时间。 |
| additional_data | map\[string\]any | DAG 其他数据。 |
| nodes | \[\]NodeDetailDTO | DAG 内的所有 Node 信息，详见 [获取 Node 的详细信息](2100-get-node-detail.md)。 |

## 示例

### 请求示例

POST 10.10.10.1:2886/api/v1/obcluster/backup/config

``` json
{
  "backup_base_uri":"file://data/backup",
  "log_archive_concurrency":100,
  "binding":"Mandatory",
  "ha_low_thread_score":35,
  "piece_switch_interval":"6d",
  "archive_lag_target":"2h",
  "delete_policy":
  {
    "policy":"",
    "recovery_window":"5d"
  }
}
```

### 返回示例

``` json
{
  "successful": true,
  "timestamp": "2024-01-09T17:11:43.385889278+08:00",
  "duration": 1,
  "status": 200,
  "traceId": "877fe32b83634153",
  "data": {
    "id": "22130706433028869",
    "dag_id": 4,
    "name": "Set obcluster backup config",
    "stage": 1,
    "max_stage": 2,
    "state": "READY",
    "operator": "RUN",
    "start_time": "2024-01-09T17:11:43.384630643+08:00",
    "end_time": "2024-01-09T17:11:43.384630643+08:00",
    "additional_data": null,
    "nodes": null
  }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [设置集群级备份配置](200-backup-configuration-for-cluster-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [设置集群级备份配置](200-backup-configuration-for-cluster-of-go.md)。
