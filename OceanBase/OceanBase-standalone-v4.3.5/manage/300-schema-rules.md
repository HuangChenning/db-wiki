---
title: "Schema 规范"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577852.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# Schema 规范

#### 注意

OceanBase 数据库 MySQL 模式当前表名最大长度限制为 64，具体版本可能有不同限制。

#### 注意

- OceanBase 数据库 Oracle 模式规范除字母大小写要求之外，其余与 OceanBase 数据库 MySQL Mode规范相同。
- OceanBase 数据库 Oracle 模式当前表名最大长度限制为 64，具体版本可能有不同限制。

#### 注意

歧义指资源命名虽然符合规范，但有多种解释空间，如以 `tmp_` 开头的表作为普通表，该表又可被视为临时表，应当避免此类情况。

#### 注意

当前 MySQL、OceanBase 数据库 MySQL 模式主流版本索引长度限制为 64 个字符，不同版本可能存在差异。

#### 注意

当前 OceanBase 数据库 Oracle 模式主流版本索引长度限制为 64 个字符，不同版本可能存在差异。
