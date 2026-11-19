---
title: ALL_POLICY_CONTEXTS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700791.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ALL_POLICY_CONTEXTS

## 功能

展示访问视图时会根据上下文的取值选择对应的策略组生效。

## 字段说明

| 字段 | 类型 | 是否可以为 NULL | 描述 |
| --- | --- | --- | --- |
| OBJECT_OWNER | VARCHAR2(128) | YES | 受策略控制的对象的拥有者 |
| OBJECT_NAME | VARCHAR2(128) | YES | 受策略控制的对象的名字 |
| NAMESPACE | VARCHAR2(128) | NO | 关联的 Context 名称 |
| ATTRIBUTE | VARCHAR2(128) | NO | 关联的 Context 中的属性名 |
| COMMON | VARCHAR2(3) | NO | 仅用于兼容，目前值固定为 NO。 |
| INHERITED | VARCHAR2(3) | NO | 仅用于兼容，目前值固定为 NO。 |
