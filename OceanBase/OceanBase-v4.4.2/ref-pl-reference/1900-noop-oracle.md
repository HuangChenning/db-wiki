---
title: NOOP
book: "PL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286911.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# NOOP

用于验证服务器是否仍处于连接状态并正确监听。

<main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库 Oracle 模式。</p>
  </main>

## 语法

```sql
UTL_SMTP.NOOP (
   c  IN OUT NOCOPY connection)
RETURN reply;

UTL_SMTP.NOOP (
   c  IN OUT NOCOPY connection);
```

## 参数解释

| **参数** |         **解释**         |
|--------|------------------------|
|c|SMTP 连接。|

## 返回值

| **返回值** |          **描述**          |
|---------|--------------------------|
|reply|command 的回复。如果有多个回复，则返回最后一个回复。|

## 使用说明

* 用于从服务器引发成功的回复，在 `open_connect` 后，可通过 `noop` 验证服务器是否仍处于连接状态并正确监听。
* 预期返回是 `250` 开头的回复信息，表示服务器已经处于连接状态并正确监听。
