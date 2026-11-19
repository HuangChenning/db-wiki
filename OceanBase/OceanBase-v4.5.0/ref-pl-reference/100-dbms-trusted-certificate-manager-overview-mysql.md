---
title: "DBMS_TRUSTED_CERTIFICATE_MANAGER 概述"
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479869.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# DBMS_TRUSTED_CERTIFICATE_MANAGER 概述

`DBMS_TRUSTED_CERTIFICATE_MANAGER` 系统包用于添加、删除、修改受 OBserver 集群信任的 CA 根证书，用于 RPC 安全认证。

<main id="notice" >
  <h4>功能适用性</h4>
  <p>该内容仅适用于 OceanBase 数据库企业版。OceanBase 数据库社区版仅提供 MySQL 模式。</p>
</main>

## 权限说明

调用者必须为 sys 租户，才可调用系统包。

## DBMS_TRUSTED_CERTIFICATE_MANAGER 子程序概览

下表列出了 OceanBase 数据库当前版本所支持的 `DBMS_TRUSTED_CERTIFICATE_MANAGER` 子程序和简要描述。

| 子程序     | 描述                                      |
| --------- | ----------------------------------------- |
| [ADD_TRUSTED_CERTIFICATE](200.add-trusted-certificate-mysql.md) | 添加一个 CA 根证书，以便使用该证书签发的数字证书的 OBserver 集群或 OMS 等组件能够安全地通过 RPC 认证并连接到集群。 |
| [DELETE_TRUSTED_CERTIFICATE](300.delete-trusted-certificat-mysql.md) | 移除一个 CA 根证书，使得使用该证书签发的数字证书的 OBserver 集群或 OMS 等组件无法继续连接到集群。 |
| [UPDATE_TRUSTED_CERTIFICATE](400.update-trusted-certificat-mysql.md)	| 更新 OBserver 集群所信任的 CA 根证书信息。           |
