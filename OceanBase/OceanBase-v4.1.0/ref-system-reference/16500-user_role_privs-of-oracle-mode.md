---
title: USER_ROLE_PRIVS
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699125.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# USER_ROLE_PRIVS

USER_ROLE_PRIVS
====================================

功能
-----------

描述授予当前用户的角色。

  <main id="notice" >
    <h4>功能适用性</h4>
    <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
  </main>

字段说明
-------------

|   **字段名称**   |    **类型**    | **是否可以为 NULL** |           **描述**           |
|--------------|--------------|----------------|----------------------------|
| GRANTEE      | VARCHAR2(30) | NO             | 用户的名称，或 PUBLIC             |
| GRANTED_ROLE | VARCHAR2(30) | NO             | 授予用户的角色名称                  |
| ADMIN_OPTION | VARCHAR2(3)  | NO             | 指示授权是否带有 ADMIN 选项          |
| DEFAULT_ROLE | VARCHAR2(3)  | NO             | 指示角色是否被指定为用户的 DEFAULT ROLE |
