---
title: "获取所有资源池信息"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077922.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取所有资源池信息

本文介绍如何通过 API 获取集群中所有的资源池信息。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/resource-pools

### 返回结果

[TABLE]

DbaObResourcePool 的数据结构：

| 参数           | 类型      | 说明                          |
|----------------|-----------|-------------------------------|
| id             | int       | 资源池的 ID。                 |
| name           | string    | 资源池的名称。                |
| zone_list      | string    | 资源池所位于的 Zone 列表。    |
| unit_num       | int       | 资源池的 unit 个数。          |
| unit_config_id | int       | 资源池所使用的资源规格的 ID。 |
| tenant_id      | int       | 资源池所属的租户 ID。         |
| replica_type   | string    | 资源池上的副本类型。          |
| create_time    | time.Time | 资源池的创建时间。            |
| modify_time    | time.Time | 资源池的修改时间。            |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/resource-pools

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T15:49:07.354211125+08:00",
    "duration": 4,
    "status": 200,
    "traceId": "b1cebf73debb0d68",
    "data": {
        "contents": [
            {
                "id": 1,
                "name": "sys_pool",
                "zone_list": "zone1",
                "unit_num": 1,
                "UnitCount": 0,
                "unit_config_id": 1,
                "tenant_id": 1,
                "replica_type": "FULL",
                "CreateTime": "2024-10-14T10:24:57.972281+08:00",
                "ModifyTime": "2024-10-14T10:24:57.982035+08:00"
            },
            {
                "id": 1002,
                "name": "t1",
                "zone_list": "zone1",
                "unit_num": 1,
                "UnitCount": 0,
                "unit_config_id": 1001,
                "tenant_id": 1002,
                "replica_type": "FULL",
                "CreateTime": "2024-10-14T10:26:55.045879+08:00",
                "ModifyTime": "2024-10-14T10:26:55.562399+08:00"
            },
            {
                "id": 1003,
                "name": "t2",
                "zone_list": "zone1",
                "unit_num": 1,
                "UnitCount": 0,
                "unit_config_id": 1001,
                "tenant_id": 1002,
                "replica_type": "FULL",
                "CreateTime": "2024-10-14T10:26:55.057419+08:00",
                "ModifyTime": "2024-10-14T10:26:55.562399+08:00"
            }
        ]
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [获取所有资源池信息](100-get-all-rp-specifications-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [获取所有资源池信息](100-get-all-rp-specifications-of-go.md)。
