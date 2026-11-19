---
title: "获取所有资源规格信息"
book: obshell
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000004286751.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取所有资源规格信息

本文介绍如何通过 API 获取所有的资源规格信息。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/units/config

### 返回结果

[TABLE]

DbaObUnitConfig 的数据结构：

| 参数           | 类型      | 说明                 |
|----------------|-----------|----------------------|
| unit_config_id | int       | 资源规格 ID。        |
| name           | string    | 资源规格的名称。     |
| max_cpu        | float64   | CPU 规格的上限。     |
| min_cpu        | float64   | CPU 规格的下限。     |
| memory_size    | int       | 内存规格。           |
| log_disk_size  | int       | 日志盘空间的大小。   |
| max_iops       | uint      | IOPS 的上限。        |
| min_iops       | uint      | IOPS 的下限。        |
| create_time    | time.Time | 资源规格的创建时间。 |
| modify_time    | time.Time | 资源规格的修改时间。 |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/units/config

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T15:40:53.446393206+08:00",
    "duration": 5,
    "status": 200,
    "traceId": "f8a505228bd6194a",
    "data": {
        "contents": [
            {
                "unit_config_id": 1,
                "name": "sys_unit_config",
                "max_cpu": 3,
                "min_cpu": 3,
                "memory_size": 1073741824,
                "log_disk_size": 2147483648,
                "max_iops": 9223372036854775807,
                "min_iops": 9223372036854775807,
                "create_time": "2024-10-14T10:24:57.968738+08:00",
                "modify_time": "2024-10-14T10:24:57.968738+08:00"
            },
            {
                "unit_config_id": 1001,
                "name": "s1",
                "max_cpu": 2,
                "min_cpu": 2,
                "memory_size": 2147483648,
                "log_disk_size": 6442450944,
                "max_iops": 9223372036854775807,
                "min_iops": 9223372036854775807,
                "create_time": "2024-10-14T10:26:41.286401+08:00",
                "modify_time": "2024-10-14T10:26:41.286401+08:00"
            }
        ]
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [获取所有资源规格信息](200-get-all-resource-specifications-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [获取所有资源规格信息](200-get-all-resource-specifications-of-go.md)。
