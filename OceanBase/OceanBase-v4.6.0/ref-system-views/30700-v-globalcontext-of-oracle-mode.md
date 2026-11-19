---
title: "V$GLOBALCONTEXT"
book: "系统视图"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005683532.html"
tags:
  - oceanbase
  - distributed
  - ref-system-views
---

# V$GLOBALCONTEXT

<main id="notice" type='explain'>
<h4>说明</h4>
<p>该视图从 V3.2.4 版本开始引入。</p>
</main>

## 功能描述

展示当前会话可访问的全局上下文属性的 `CLIENT_IDENTIFIER` 值。

## 字段说明

|       字段名称        |       类型       | **是否可以为 NULL** |        描述        |
|-------------------|----------------|----------------|------------------|
| NAMESPACE         | VARCHAR2(128)  | NO             | 全局可访问上下文的命名空间    |
| ATTRIBUTE         | VARCHAR2(128)  | NO             | 全局可访问上下文的属性      |
| VALUE             | VARCHAR2(4000) | NO             | 全局可访问上下文的属性值     |
| USERNAME          | VARCHAR2(128)  | NO             | 适用于全局可访问上下文值的用户名 |
| CLIENT_IDENTIFIER | VARCHAR2(65)   | NO             | 全局可访问上下文的客户端标识符  |
| CON_ID            | NUMBER(38)     | NO             | 租户 ID            |
