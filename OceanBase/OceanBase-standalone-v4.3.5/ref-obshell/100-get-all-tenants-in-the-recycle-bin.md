---
title: "获取回收站中的所有租户信息"
book: obshell
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003975988.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 获取回收站中的所有租户信息

本文介绍如何通过 API 获取回收站中的所有租户信息。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

GET /api/v1/recyclebin/tenants

### 返回结果

[TABLE]

DbaRecyclebin 的数据结构：

| 参数                 | 类型   | 说明                            |
|----------------------|--------|---------------------------------|
| object_name          | string | 租户在回收站中的名称。          |
| original_tenant_name | string | 租户的原名称。                  |
| can_undrop           | string | 租户是否能被 undrop（YES/NO）。 |
| can_purge            | string | 租户是否能被清理（YES/NO）。    |

## 示例

### 请求示例

GET 10.10.10.1:2886/api/v1/recyclebin/tenants

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T16:12:44.394940604+08:00",
    "duration": 40,
    "status": 200,
    "traceId": "5b7f4130ec2be90f",
    "data": {
        "contents": [
            {
                "object_name": "__recycle_$_123456_1728893438913560",
                "original_tenant_name": "t1",
                "can_undrop": "YES",
                "can_purge": "YES"
            }
        ]
    }
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [获取回收站中的所有租户信息](100-get-all-tenants-in-the-recycle-bin-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [获取回收站中的所有租户信息](100-get-all-tenants-in-the-recycle-bin-of-go.md)。
