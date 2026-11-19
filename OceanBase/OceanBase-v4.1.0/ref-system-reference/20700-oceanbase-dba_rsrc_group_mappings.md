---
title: oceanbase.DBA_RSRC_GROUP_MAPPINGS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702072.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# oceanbase.DBA_RSRC_GROUP_MAPPINGS

## 功能

展示用户和资源组之间的绑定关系。

## 相关视图

`oceanbase.DBA_RSRC_CONSUMER_GROUPS`

## 字段说明

|      字段类型      |       类型       | 是否可以为 NULL |                描述                 |
|----------------|----------------|------------|-----------------------------------|
| ATTRIBUTE      | varchar(128)  | NO         | 类别，当前版本仅支持 `ORACLE_USER`。         |
| VALUE          | varbinary(128) | NO         | 值，当类别为 `ORACLE_USER` 时，记录的是登录用户名。 |
| CONSUMER_GROUP | varchar(128)  | YES        | 用户绑定到的资源组的名称。                     |
| STATUS         | varchar(128)  | NO         | 资源组的状态，仅用于兼容，目前值固定为 `NULL`。       |
