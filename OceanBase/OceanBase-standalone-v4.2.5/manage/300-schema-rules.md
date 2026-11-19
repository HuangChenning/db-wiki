---
title: "Schema 规范"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702055.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# Schema 规范

#### 注意

OceanBase 数据库 MySQL Mode 当前表名最大长度限制为 64，具体版本可能有不同限制。

#### 注意

- OceanBase 数据库 Oracle Mode 规范除字母大小写要求之外，其余与 OceanBase 数据库 MySQL Mode规范相同。
- OceanBase 数据库 Oracle Mode 当前表名最大长度限制为 64，具体版本可能有不同限制。

#### 注意

歧义指资源命名虽然符合规范，但有多种解释空间，如以 `tmp_` 开头的表作为普通表，该表又可被视为临时表，应当避免此类情况。

#### 注意

当前 MySQL、OceanBase 数据库 MySQL Mode 主流版本索引长度限制为 64 个字符，不同版本可能存在差异。

#### 注意

- 当前 OceanBase 数据库 Oracle Mode 主流版本索引长度限制为 64 个字符，不同版本可能存在差异。
- 分库分表的同一个逻辑表内的不同物理分表的索引命名相同，仅能在分库分表数相同场景实现，如 10 库 10 表，100 库 100 表，在 10 库 100 内会造成冲突。
- 分库分表的同一个逻辑表内的不同物理分表的索引命名以分表位区分，指索引中包含 00-09 或 000-099 此类分表位，用于避免同一 SCHEMA 内索引命名冲突限制。
- 分库分表的同一个逻辑表内的不同物理分表的索引命名以表名区分，指索引中包含物理分表信息，因物理分表中包含了分表位信息，从而避免了同一 SCHEMA 内索引命名冲突。
- 如一个分库分表的同一个逻辑表内不同物理分表的索引命名不同，可能在使用 hint 上有所限制。hint 中的指定索引信息不能进行分表位解析处理，所以如业务需求必须在 hint 中使用索引，应当使用分库分表数量相同的逻辑库。
