---
title: "安全认证最佳实践"
book: "运维管理"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489653.html"
tags:
  - oceanbase
  - best-practices
  - management
---

# 安全认证最佳实践

在全球范围内高度重视数据安全治理的背景下，数据库作为存储组织关键数据资产的基础软件，如何保障数据库安全已经成为数据库厂商和广大用户需要共同解决的一个重要课题。OceanBase 作为一家数据库厂商，多年来高度重视产品安全性，积极贯彻监管要求，建立安全管理体系，致力于打造稳定、可靠、安全、开放的数据基础设施。OceanBase 希望通过技术创新，帮助用户保障数据的机密性、完整性和可用性，成为客户值得信赖的基础软件供应商。当然保障数据库安全不仅需要厂商的投入，更需要厂商和用户的通力协作。

数据库系统的重要指标之一是要确保系统安全，通过数据库管理系统防止非授权使用数据库，保护数据库的文件和数据。

本文主要讲解安全认证的最佳实践操作。

## MySQL 模式租户

### 禁用空密码账户

空密码账户的存在降低了攻击成本，攻击者只要正确猜解出用户名，无需密码即可登陆，因此需要禁用数据库的空密码账户，避免未授权的恶意用户访问数据库。

- 自检操作

  使用下述语句查询是否存在空密码账户。

  ```
  obclient> SELECT user, password FROM mysql.user WHERE LENGTH(password)=0;
  ```

- 加固操作

  数据库管理员可以使用如下语句为空密码账户配置密码。

  ```
  obclient> SET PASSWORD FOR u0 = PASSWORD('auth_string');
  obclient> ALTER USER u0 IDENTIFIED by '******';
  ```

### 禁用 GRANT 语句创建账户

使用 GRANT 语句时，如果目标用户不存在，会尝试创建用户。这容易导致在 GRANT 语句编写出错时，非预期的创建空密码用户，引入账户管理风险。设置配置项 sql_mode 的值包含 NO_AUTO_CREATE_USER 可以禁止 GRANT 语句创建用户。

- 自检操作

  执行如下 SQL 语句评估配置是否正确。

  ```
  obclient> SELECT @@global.sql_mode;
  obclient> SELECT @@session.sql_mode;
  ```

  确保所有的返回结果中都包含 NO_AUTO_CREATE_USER 值。

- 加固操作

  使用具备 SUPER 权限的管理员账户，执行如下 SQL。

  ```
  obclient> SET @@global.sql_mode=CONCAT(@@global.sql_mode, ',NO_AUTO_CREATE_USER');
  ```

### 启用密码复杂度校验

MySQL 租户支持通过租户级系统变量配置密码复杂度策略，启用密码复杂度策略可以预防弱口令问题，提升密码破解的门槛。

[TABLE]

- 自检操作

  使用如下语句查看当前租户的密码复杂度配置。

  ```
  obclient> SHOW VARIABLES LIKE "validate_password%";
  ```

  返回结果如下：

  ```
  +--------------------------------------+-------+
  | Variable_name                        | Value |
  +--------------------------------------+-------+
  | validate_password_check_user_name    | on    |
  | validate_password_length             | 0     |
  | validate_password_mixed_case_count   | 0     |
  | validate_password_number_count       | 0     |
  | validate_password_policy             | low   |
  | validate_password_special_char_count | 0     |
  +--------------------------------------+-------+
  6 rows in set
  ```

- 加固操作

  建议的配置如下。

  - `validate_password_length`：设置用户密码最小长度，建议密码长度不小于 14。
  - `validate_password_check_user_name`：设置用户密码是否可以和用户名相同，建议设置为 ON。
  - `validate_password_policy`：设置密码检查策略，建议设置为 medium。
  - `validate_password_mixed_case_count`：设置用户密码至少包含的大写字母个数以及至少包含的小写字母个数，建议不小于 1。
  - `validate_password_number_count`：设置用户密码至少包含的数字个数，建议不小于 1。
  - `validate_password_special_char_count`：设置用户密码至少包含的特殊字符个数，建议不小于 1。

### 连续认证失败锁定账户

MySQL 租户支持通过租户级配置项 `connection_control_failed_connections_threshold` 来指定用户错误登录尝试的阈值，登陆失败次数超出阈值的账户将被锁定，锁定时长可通过配置项 `connection_control_min_connection_delay` 和 `connection_control_max_connection_delay` 进行设置，从而防止对账户密码的爆破攻击，提高数据库的安全性。

- 自检操作

  使用如下命令查看 `connection_control_failed_connections_threshold` 配置项。

  ```
  obclient [oceanbase]> SHOW PARAMETERS LIKE 'connection_control_failed_connections_threshold';
  ```

  如果该配置项的值为 0，说明未开启登陆失败锁定。

- 加固操作

  使用如下命令配置登陆失败 5 次后锁定。

  ```
  obclient> ALTER SYSTEM SET connection_control_failed_connections_threshold = 5;
  ```

### 配置密码超时时间

系统变量 `default_password_lifetime` 可用于配置 MySQL 租户全局的密码过期时间，密码过期后需要重置密码才能执行其它操作。配置密码过期时间能提升运维安全水位和系统的合规性，降低密码泄漏带来的风险。

- 自检操作

  使用如下命令查看当前配置的密码超时时间。

  ```
  obclient> SELECT @@default_password_lifetime;
  ```

  返回结果如下：

  ```
  +-----------------------------+
  | @@default_password_lifetime |
  +-----------------------------+
  |                           0 |
  +-----------------------------+
  1 row in set
  ```

- 加固操作

  租户管理员可以使用如下命令设置密码超时时间为 90 天。

  ```
  obclient> SET GLOBAL default_password_lifetime=90;
  ```

## Oracle 模式租户

### 连续认证失败锁定账户

Oracle 租户支持通过 USER PROFILE 配置认证策略，支持配置登陆失败次数，并锁定登陆失败超限的账户，从而防止对账户密码的爆破攻击，提高数据库的安全性。

- 自检操作

  使用如下语句查看当前用户的 USER PROFILE 配置。

  ```
  obclient> SELECT * FROM DBA_PROFILES;
  ```

  结果中的 FAILED_LOGIN_ATTEMPTS 和 PASSWORD_LOCK_TIME 字段分别是登陆失败次数和账户锁定时长。

- 加固操作

  以管理员身份登录 Oracle 租户，使用如下命令创建一个 USER PROFILE，设置密码连续错误 5 次将锁定账户一天，并在 test 账户启用。

  ```
  obclient> CREATE PROFILE "test_auth_policy" LIMIT FAILED_LOGIN_ATTEMPTS 5  PASSWORD_LOCK_TIME 1;
  obclient> SELECT * FROM DBA_PROFILES;
  obclient> ALTER USER test PROFILE "test_auth_policy";
  ```

### 指定密码有效期和宽限期

Oracle 租户支持配置密码有效期和宽限期。配置密码有效期能提升运维安全水位和系统的合规性，降低密码泄漏带来的风险。

- 自检操作

  使用如下语句查看当前用户的 USER PROFILE 配置。

  ```
  obclient> SELECT * FROM DBA_PROFILES;
  ```

  结果中的 PASSWORD_LIFE_TIME 跟 PASSWORD_GRACE_TIME 分别是密码有效期跟宽限期。

- 加固操作

  请确保 PASSWORD_LIFE_TIME 小于等于 90，并且宽限期 PASSWORD_GRACE_TIME 小于等于 5。

  ```
  obclient> ALTER PROFILE "test_auth_policy" LIMIT PASSWORD_LIFE_TIME 90 PASSWORD_GRACE_TIME 5;
  ```

### 设置密码复杂度并启用密码复杂度验证

Oracle 租户支持配置密码复杂度策略，启用密码复杂度策略可以预防弱口令问题，提升密码破解的门槛。

- 自检操作

  使用如下语句查看当前用户的 USER PROFILE 配置。

  ```
  obclient> SELECT LIMIT FROM DBA_PROFILES WHERE RESOURCE_NAME='PASSWORD_VERIFY_FUNCTION' AND PROFILE='DEFAULT';
  ```

  返回结果如下：

  ```
  +-----------------+
  | LIMIT           |
  +-----------------+
  | VERIFY_FUNCTION |
  +-----------------+
  ```

  返回值为 NULL 则表示密码复杂度验证未开启，值为指定的函数则表示密码复杂度验证已开启。

- 加固操作

  此处可参考官网文档 [密码复杂度](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000218721)。
