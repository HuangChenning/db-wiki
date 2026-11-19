---
title: "发起租户恢复"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286786.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 发起租户恢复

本文介绍如何通过 API 发起租户恢复。

## 调用说明

### 接口约束

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

POST /api/v1/tenant/restore

### 请求参数

| 参数 | 类型 | 必选 | 示例值 | 描述 |
|----|----|----|----|----|
| data_backup_uri | string | 必选项 | "file:///data/backup/data" | 源数据备份文件路径。 |
| archive_log_uri | string | 可选项 | "file:///data/backup/clog" | 源日志归档目的端。不设置则和 `data_backup_uri` 相同。 |
| restore_tenant_name | string | 必选项 | "new_tenant" | 恢复的租户名。 |
| time_stamp | time.time | 可选项 | "2006-01-02T15:04:05.000+08:00" | 指定恢复时间戳，格式为 `2006-01-02T15:04:05.000Z08:00`。设置后表示恢复到该时间点为止，且包括该 timestamp 位点。 |
| scn | int | 可选项 | 1728727696264250400 | 指定恢复的 SCN，设置后表示恢复到该 SCN 位点为止，且包括该 SCN 位点。 |
| ha_high_thread_score | int | 可选项 | 10 | 用于设置高可用高优先级线程的当前工作线程数。取值范围为 \[0, 100\]，未设置的情况下，默认为 10。 |
| zone_list | \[\]ZoneParam | 必选项 | 详情参见下文 **ZoneParam 的数据结构** | 租户所使用的资源规格以及副本的分布情况。 |
| concurrency | int | 可选项 | 2 | 数据恢复的并发度。如果不指定，则默认等于该租户被分配的 MAX_CPU 数。 |
| decryption | \[\]string | 可选项 | {"pwd1"} | 备份集设置的密码。需写出全部的密码。 |
| kms_encrypt_info | string | 可选项 | 无 | 设置密钥管理信息。如果未加密或恢复时可以访问原来的密钥管理服务，则可以不设置。 |

ZoneParam 的数据结构：

| 参数             | 类型   | 必选 | 示例值 | 描述                                 |
|------------------|--------|------|--------|--------------------------------------|
| name             | string | 是   | zone1  | Zone 的名称                          |
| unit_config_name | string | 是   | s1     | 租户资源池在 Zone 上使用的资源规格。 |

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

POST 10.10.10.1:2886/api/v1/tenant/restore

``` json
{
    "data_backup_uri": "oss://oss-328067-1014-obshell/backup/archive/test/1/1002/data?host=oss-cn-hangzhou.aliyuncs.com", 
    "restore_tenant_name": "rt2", 
    "zone_list": 
      [
        {
          "name": "zone1", 
          "unit_config_name": "unit1"
        }
      ], 
    "archive_log_uri": "oss://oss-328067-1014-obshell/backup/archive/test/1/1002/clog?host=oss-cn-hangzhou.aliyuncs.com"
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
    "name": "Restore backup_rt2",
    "stage": 1,
    "max_stage": 5,
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

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [发起单个租户恢复](100-initiate-tenant-recovery-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [发起单个租户恢复](100-initiate-tenant-recovery-of-go.md)。
