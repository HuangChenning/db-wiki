---
title: "恢复回收站中的租户"
book: obshell
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077847.html"
tags:
  - oceanbase
  - standalone
  - ref-obshell
---

# 恢复回收站中的租户

本文介绍如何通过 API 恢复回收站中的指定租户。

## 调用说明

如果设置了密码，则需要通过认证。详情可参见 [API 混合加密](20-api-hybrid-encryption.md)。

### 请求路径

POST /api/v1/recyclebin/tenant/:name

### 请求参数

| 参数 | 类型 | 必选 | 示例值 | 描述 |
|----|----|----|----|----|
| new_name | string | 否 | t2 | 恢复后的租户的新名称。如果未设置，则恢复的租户名为其原租户名。 |

### 返回结果

[TABLE]

## 示例

### 请求示例

POST 10.10.10.1:2886/api/v1/recyclebin/tenant/t1

``` json
{
    "new_name": "t2"
}
```

### 返回示例

``` json
{
    "successful": true,
    "timestamp": "2024-10-14T16:00:09.813011861+08:00",
    "duration": 130,
    "status": 200,
    "traceId": "fa1fbe181d870bde"
}
```

## 相关文档

除通过命令行调用 API 接口外，还可以通过 SDK 方法调用 API。

- 通过 obshell-sdk-python 请求 API 方法的介绍可参见 [恢复回收站中的租户](200-restore-tenants-in-the-recycle-bin-of-python.md)。

- 通过 obshell-sdk-go 请求 API 方法的介绍可参见 [恢复回收站中的租户](200-restore-tenants-in-the-recycle-bin-of-go.md)。
