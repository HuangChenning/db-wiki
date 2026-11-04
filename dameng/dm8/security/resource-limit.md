---
title: "资源限制"
book: "DM8 安全管理"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/resource-limit.html
tags:
  - dameng
  - dm8
  - security
---

DM 支持在创建和修改用户时指定对用户进行资源限制，具体语法参考本文 2.2 节的介绍。

资源限制用于限制用户对 DM 数据库系统资源的使用，表 9.1 列出了资源限制所包含的内容。

表9.1 DM资源限制项

| **资源设置项** | **说明** | **最大值** | **最小值** | **缺省值** |
| --- | --- | --- | --- | --- |
| GLOBAL\_SESSION\_PER\_USER | 在所有 DSC 实例中，一个用户可以同时拥有的会话数量 | 32768 | 1 | 系统所能提供的最大值 |
| SESSION\_PER\_USER | 在一个实例中，一个用户可以同时拥有的会话数量 | 32768 | 1 | 安全版本中默认值为 4096；其他版本中默认值为系统所能提供的最大值 |
| CONNECT\_TIME | 一个会话连接、访问和操作数据库服务器的时间上限。   单位由 INI 参数 RESOURCE\_FLAG 决定。RESOURCE\_FLAG 取值 1、0 时，CONNECT\_TIME 单位分别为秒、分钟。   RESOURCE\_FLAG 缺省值为 0 | 当 RESOURCE\_FLAG 取值 1、0 时，缺省值分别为 86400 秒、1440 分钟（1 天） | 1 | 无限制 |
| CONNECT\_IDLE\_TIME | 会话最大空闲时间。单位由 INI 参数 RESOURCE\_FLAG 决定。RESOURCE\_FLAG 取值 1、0 时，CONNECT\_IDLE\_TIME 单位分别为秒、分钟。   RESOURCE\_FLAG 缺省值为 0 | 当 RESOURCE\_FLAG 取值 1、0 时，缺省值分别为 86400 秒、1440 分钟（1 天） | 1 | 无限制 |
| FAILED\_LOGIN\_ATTEMPTS | 将引起一个账户被锁定的连续注册失败的次数 | 100 | 1 | 3，系统预设管理员用户默认无限制 |
| CPU\_PER\_SESSION | 一个会话允许使用的 CPU 时间上限（单位：秒） | 31536000（365 天） | 1 | 无限制 |
| CPU\_PER\_CALL | 用户的一个请求能够使用的 CPU 时间上限（单位：秒） | 86400（1 天） | 1 | 无限制 |
| READ\_PER\_SESSION | 会话能够读取的总数据页数上限 | 2147483646 | 1 | 无限制 |
| READ\_PER\_CALL | 每个请求能够读取的数据页数 | 2147483646 | 1 | 无限制 |
| MEM\_SPACE | 会话占有的私有内存空间上限（单位：MB） | 2147483647 | 1 | 无限制 |
| PASSWORD\_LIFE\_TIME | 口令有效期（单位：天）。过了有效期，会进入过期口令宽限期。过期口令宽限期由 PASSWORD\_GRACE\_TIME 设置 | 365 | 1 | 无限制 |
| PASSWORD\_REUSE\_TIME | 重用同一个口令的时间间隔（单位：天）。一个口令过了宽限期之后，将禁止使用。如果想再次使用该口令，须同时满足 PASSWORD\_REUSE\_TIME 和 PASSWORD\_REUSE\_MAX 的规定 | 365 | 1 | 无限制 |
| PASSWORD\_REUSE\_MAX | 重用同一个口令之前，需要修改口令的次数 | 32768 | 1 | 无限制 |
| PASSWORD\_LOCK\_TIME | 如果超过 FAILED\_LOGIN\_ATTEMPTS 设置值，一个用户将被锁定的分钟数 | 1440（1 天） | 1 | 1，系统预设管理员用户默认无限制 |
| PASSWORD\_GRACE\_TIME | 过期口令宽限期（单位：天）。宽限期仍可正常访问数据库。但在宽限期中，必须对口令进行修改，修改之后使用新口令可以继续登录系统。如果宽限期未修改口令，超过该宽限期后，将禁止执行除修改口令以外的其他操作 | 30 | 1 | 10，系统预设管理员用户默认无限制 |
| INACTIVE\_ACCOUNT\_TIME | 指定用户的非活跃时间，用户超过指定时间未登录将被自动锁定 | 24855 | 15 | 无限制 |

> **注意**
> 
> 当PASSWORD\_GRACE\_TIME为UNLIMITED时不能设置PASSWORD\_LIFE\_TIME。

除上述资源设置项外，DM 还支持用户 IP 地址限制和用户时间段限制。

用户 IP 地址设置项包括 ALLOW\_IP（允许的 IP 地址）和 NOT\_ALLOW\_IP（不允许的 IP 地址），具体的限制规则如下表所示。

表9.2 IP地址限制规则

<table><tbody><tr><td colspan="2"><b>IP地址限制项</b></td><td colspan="4"><b>集合状态</b></td></tr><tr><td rowspan="2">IP集合地址</td><td>不允许的IP地址</td><td>空</td><td>N</td><td>空</td><td>N</td></tr><tr><td>允许的IP地址</td><td>Y</td><td>空</td><td>空</td><td>Y</td></tr><tr><td colspan="2">IP限制结果</td><td>只允许属于集合Y的IP地址</td><td>只允许属于集合N以外的所有IP地址</td><td>允许所有IP，即无任何IP地址限制</td><td>只允许属于Y-N （差集）集合的IP地址</td></tr></tbody></table>

允许 IP 和禁止 IP 用于控制此登录是否可以从某个 IP 访问数据库，其中禁止 IP 优先。在设置 IP 时，设置的允许 IP 和禁止 IP 需要用双引号括起来，中间用逗号隔开，如"192.168.0.29","192.168.0.30"；也可以利用\*或 CIDR 格式来设置网段，如"192.168.0.\*"或"192.168.0.0/16"；需要注意，\*和 CIDR 格式不能在同一 IP 中一起设置。

用户时间段设置项包括 ALLOW\_DATETIME（允许的时间段）和 NOT\_ALLOW\_DATETIME（不允许的时间段），具体的限制规则如下表所示：

表9.3用户时间段限制规则

<table><tbody><tr><td colspan="2"><b>时间段限制项</b></td><td colspan="4"><b>集合状态</b></td></tr><tr><td rowspan="2">时间段集合</td><td>不允许的时间段</td><td>空</td><td>N</td><td>空</td><td>N</td></tr><tr><td>允许的时间段</td><td>Y</td><td>空</td><td>空</td><td>Y</td></tr><tr><td colspan="2">时间段限制结果</td><td>只允许属于集合Y的时间段</td><td>只允许属于集合N以外的所有时间段</td><td>允许所有时间段，即无任何时间段限制</td><td>只允许属于Y-N （差集）集合的时间段</td></tr></tbody></table>

允许时间段和禁止时间段用于控制此登录是否可以在某个时间段访问数据库，其中禁止时间段优先。设置的时间段中的日期和时间要分别用双引号括起来。在设置时间段时，有两种方式：

- 具体时间段，如 2023 年 1 月 1 日 8：30 至 2023 年 2 月 1 日 17：00；
- 规则时间段，如每周一 8：30 至每周五 17：00。

例 1 创建对失败登录次数进行控制的用户，如果用户失败的登录次数达到 3 次，这个用户账号将被锁定。

```
CREATE USER USER1 IDENTIFIED BY "USER1_psd"
LIMIT FAILED_LOGIN_ATTEMPTS 3, PASSWORD_LOCK_TIME 5;
```

例 2 创建对修改口令进行限制的用户，要求用户在 30 天内必须把口令修改过 5 次后，才能使用过去用过的口令。

```
CREATE USER USER2 IDENTIFIED BY "USER2_psd"
LIMIT PASSWORD_REUSE_TIME 30, PASSWORD_REUSE_MAX 5;
```

例 3 创建对允许 IP 和允许时间段进行限制的用户，要求用户在 192.168.0.\*网段进行登录，且访问时间必须为工作时段。

```
CREATE USER USER3 IDENTIFIED BY "USER3_psd"
ALLOW_IP "192.168.0.*" ALLOW_DATETIME MON "8:30:00" TO FRI "17:30:00";
```

例 4 创建对允许 IP 和允许时间段进行限制的用户，要求用户在 192.168.0.29 或 192.168.0.30 IP 进行登录，且访问时间段为 2023 年 1 月 1 日 8：30 至 2023 年 12 月 31 日 17：30。

```
CREATE USER USER4 IDENTIFIED BY "USER4_psd" ALLOW_IP "192.168.0.29", "192.168.0.30" ALLOW_DATETIME "2023-1-1" "8:30:30" to
"2023-12-31" "17:30:00";
```