---
title: "访问控制最佳实践"
book: "运维管理"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489655.html"
tags:
  - oceanbase
  - best-practices
  - management
---

# 访问控制最佳实践

在全球范围内高度重视数据安全治理的背景下，数据库作为存储组织关键数据资产的基础软件，如何保障数据库安全已经成为数据库厂商和广大用户需要共同解决的一个重要课题。OceanBase 作为一家数据库厂商，多年来高度重视产品安全性，积极贯彻监管要求，建立安全管理体系，致力于打造稳定、可靠、安全、开放的数据基础设施。OceanBase 希望通过技术创新，帮助用户保障数据的机密性、完整性和可用性，成为客户值得信赖的基础软件供应商。当然保障数据库安全不仅需要厂商的投入，更需要厂商和用户的通力协作。

数据库系统的重要指标之一是要确保系统安全，通过数据库管理系统防止非授权使用数据库，保护数据库的文件和数据。

本文主要讲解访问控制的最佳实践操作。

## MySQL 模式租户

### 仅管理员账户配置 CREATE USER 权限

MySQL 租户的 `CREATE USER` 权限可以用于修改任意用户密码或删除用户，因此应确保仅管理员具备该权限。

#### 相关操作

- 自检操作

  使用如下命令查看具备 `CREATE USER` 权限的非 root 用户。

  ``` sql
  SELECT * FROM information_schema.user_privileges WHERE GRANTEE NOT LIKE ("'root'%") AND PRIVILEGE_TYPE = "CREATE USER"\G
  ```

- 加固操作

  使用 REVOKE 命令撤销普通用户的 `CREATE USER` 权限。

  ``` sql
  REVOKE CREATE USER ON *.* FROM '<user>';
  ```

### 仅管理员账户配置数据库级元数据访问权限

MySQL 租户的元数据信息存储在 MySQL 数据库和 oceanbase 数据库的内部表/内部视图中。这些元数据包含了密码哈希、账户权限等敏感信息，因此应当限制普通用户的访问，按需配置访问权限，仅允许管理员账户对元数据具备全局访问权限。

#### 相关操作

- 自检操作

  使用如下命令查询具备 oceanbase / mysql 数据库访问权限的非 root 用户。

  ``` sql
  SELECT u.* FROM DBA_OB_USERS AS u INNER JOIN DBA_OB_DATABASE_PRIVILEGE as db WHERE (database_name = "oceanbase" OR database_name = "mysql") AND u.USER_NAME= db.USERNAME AND u.user_name != "root"\G
  ```

- 加固操作

  使用 REVOKE 命令撤销普通用户的数据库级元数据访问权限，并改用表级权限按需配置。

  ``` sql
  REVOKE ALL ON database_name.* FROM username;
  GRANT SELECT, INSERT, UPDATE ON database_name.table_name TO username;
  GRANT DELETE ON database_name.another_table TO username
  ```

## Oracle 模式租户

### 移除 PUBLIC 的系统包 EXECUTE 权限

撤销 PUBLIC 角色的执行权限可以限制所有用户对系统包的访问和执行能力。这可以提高系统的安全性，确保只有经过授权的用户才能使用一些高风险的系统包。

#### 相关操作

- 自检操作

  使用如下命令查看是否给 PUBLIC 角色授权了高危系统包的执行权限。

  ``` sql
  SELECT grantee, privilege FROM dba_tab_privs WHERE grantee = 'PUBLIC' AND privilege = 'EXECUTE';
  ```

- 加固操作

  使用如下命令，移除 PUBLIC 角色对高危系统包的执行权限。

  ``` sql
  REVOKE EXECUTE ON DBMS_LOB FROM PUBLIC;
  REVOKE EXECUTE ON UTL_FILE FROM PUBLIC;
  REVOKE EXECUTE ON DBMS_SCHEDULER FROM PUBLIC;
  REVOKE EXECUTE ON DBMS_SQL FROM PUBLIC;
  REVOKE EXECUTE ON DBMS_XMLGEN FROM PUBLIC;
  ```

### 确保 '% ANY %' 类型权限非管理员 GRANTEE 上被移除

Oracle 模式 ANY 关键字使用户能够更改数据库目录中的任何数据库对象，容易引起用户间的越权访问。因此非管理员 grantee 不应分配该权限。

#### 相关操作

- 自检操作

  使用如下命令查询具备访问敏感信息的用户。

  ``` sql
  SELECT GRANTEE, PRIVILEGE FROM DBA_SYS_PRIVS WHERE PRIVILEGE LIKE '% ANY %' AND GRANTEE NOT IN ('SYS', 'DBA','ORAAUDITOR');
  ```

- 加固操作

  使用 REVOKE 命令将形如 '% ANY %' 类型的权限从非管理员 grantee 上移除，下面是一个移除 EXECUTE ANY PROCEDURE 权限的例子。

  ``` sql
  REVOKE EXECUTE ANY PROCEDURE FROM <grantee>;
  ```
