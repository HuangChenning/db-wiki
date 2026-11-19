---
title: "设置参数"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077401.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 设置参数

#### 说明

`SHOW PARAMETERS` 语句通过指定 `TENANT` 关键字来查看指定租户的配置项信息。

#### 说明

系统租户下，可以通过指定 `TENANT` 关键字来修改全部或指定租户的租户级配置项。

#### 说明

- 同时修改多个配置项时，以逗号（,）分隔。
- 集群级配置项不能通过普通租户设置，也不可以通过系统租户（即 `sys` 租户） 指定为普通租户设置，仅支持在系统租户下配置。例如，执行 `ALTER SYSTEM SET memory_limit='100G' TENANT='test_tenant'` 语句将导致报错，因为 `memory_limit` 是集群级配置项。
- 租户级配置项可以直接在本租户下修改，也可以在系统租户下通过指定 `TENANT` 关键字来修改。
- `ALTER SYSTEM` 语句不能同时指定 Zone 和 OBServer。并且在指定 Zone 时，仅支持指定一个 Zone；指定 OBServer 时，仅支持指定一个 OBServer。如果修改时，不指定 Zone 也不指定 OBServer，则集群级配置项会在整个集群所有 OBServer 上生效；租户级配置项会在当前租户在集群内所在的 OBServer 上生效。
- 确认一个配置项为集群级别还是租户级别，可根据 `SHOW PARAMETERS` 语句执行结果中的 `scope` 列对应的值来判断：
  - `scope` 值为 `CLUSTER` 则表示为集群级配置项。
  - `scope` 值为 `TENANT` 则表示为租户级配置项。

#### 说明

执行成功以后，所有被指定租户的配置项均会被修改。

#### 说明

- 同时修改多个配置项时，以逗号（,）分隔。
- Oracle 模式下，只能配置租户级配置项。
- 租户级配置项可以直接在本租户下修改，也可以在系统租户下通过指定 `TENANT` 关键字来修改。

#### 说明

- 同时重置多个配置项时，以逗号（,）分隔。
- 集群级配置项不能通过普通租户重置，也不可以通过系统租户（即 `sys` 租户） 指定为普通租户重置，仅支持在系统租户下重置。例如，执行 `ALTER SYSTEM RESET memory_limit TENANT='test_tenant'` 语句将导致报错，因为 `memory_limit` 是集群级配置项。
- 租户级配置项可以直接在本租户下修改，也可以在系统租户下通过指定 `TENANT` 关键字来修改。
- `ALTER SYSTEM RESET` 语句不支持指定 Zone 或 OBServer。
- 确认一个配置项为集群级别还是租户级别，可根据 `SHOW PARAMETERS` 语句执行结果中的 `scope` 列对应的值来判断：
  - `scope` 值为 `CLUSTER` 则表示为集群级配置项。
  - `scope` 值为 `TENANT` 则表示为租户级配置项。

#### 说明

执行成功以后，所有被指定租户的配置项均会被修改。

#### 说明

- 同时重置多个配置项时，以逗号（,）分隔。
- Oracle 模式下，只能重置租户级配置项。
- 租户级配置项可以直接在本租户下重置，也可以在系统租户下通过指定 `TENANT` 关键字来重置。

#### 说明

- 系统租户下，可以查看本租户的租户级配置项和集群级配置项信息。同时，可以通过指定 `TENANT` 关键字来查看指定租户的配置项信息。
- 普通租户下，可以查看本租户的租户级配置项以及系统租户的集群级配置项信息。
- `WHERE expr` 中可以指定的列属性与 `SHOW PARAMETERS` 返回结果中的列属性一致。
