---
title: "自主访问控制"
book: "DM8 安全管理"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/discretionary-access-control.html
tags:
  - dameng
  - dm8
  - security
---

自主访问控制（Discretionary Access Control，DAC）是这样一种访问控制方式：由数据库对象的拥有者自主决定是否将自己拥有的对象的部分或全部访问权限授予其他用户。也就是说，在自主访问控制下，用户可以按照自己的意愿，有选择地与其他用户共享他拥有的数据库对象。

## 3.1 权限管理

DM 数据库对用户的权限管理有着严密的规定，如果没有权限，用户将无法完成任何操作。

用户权限有两类：数据库权限和对象权限。数据库权限主要是指针对数据库对象的创建、删除、修改的权限，对数据库备份等权限。而对象权限主要是指对数据库对象中的数据的访问权限。数据库权限一般由 SYSDBA、SYSAUDITOR 和 SYSSSO 指定，也可以由具有特权的其他用户授予。对象权限一般由数据库对象的所有者授予用户，也可由 SYSDBA 用户指定，或者由具有该对象权限的其他用户授权。

DM 数据库用户可以通过动态视图 V$AUTHORITIES 来查询当前数据库中的所有权限，该视图字段如下：

| **序号** | **列** | **数据类型** | **说明** |
| --- | --- | --- | --- |
| 1 | ID | INTEGER | 权限 ID |
| 2 | NAME | VARCHAR(256) | 权限名称 |
| 3 | TYPE | INTEGER | 权限类型。1 表示数据库权限；2 表示对象权限；3 表示黑名单权限。黑名单权限表示关闭指定的对象权限 |

### 3.1.1 数据库权限

数据库权限是与数据库安全相关的非常重要的权限，其权限范围比对象权限更加广泛，因而一般被授予数据库管理员或者一些具有管理功能的角色。数据库权限与 DM 预定义角色有着重要的联系，详细介绍请参考 3.2.1.1 DM 预定义角色 。

DM 提供了 100 余种数据库权限，表 3.1 列出了最常用的几种数据库权限。完整的数据库权限及其与 DM 预定义角色的关系列表可参考附录 1 与附录 2。

表3.1 常用的几种数据库权限

| **数据库权限** | **说明** |
| --- | --- |
| CREATE TABLE | 在自己的模式中创建表的权限 |
| CREATE VIEW | 在自己的模式中创建视图的权限 |
| CREATE USER | 创建用户的权限 |
| CREATE TRIGGER | 在自己的模式中创建触发器的权限 |
| ALTER USER | 修改用户的权限 |
| ALTER DATABASE | 修改数据库的权限 |
| CREATE PROCEDURE | 在自己模式中创建存储程序的权限 |
| SELECT ANY DICTIONARY | 查询任意系统表或系统视图的记录的权限 |

不同类型的数据库对象，其相关的数据库权限也不相同。

例如，对于表对象，相关的数据库权限包括：

- CREATE TABLE：在自己的模式中创建表
- CREATE ANY TABLE：在任意模式中创建表
- ALTER TABLE：修改自己模式中的表
- ALTER ANY TABLE：修改任意模式中的表
- DROP TABLE：删除自己的模式中的表
- DROP ANY TABLE：删除任意模式中的表
- INSERT TABLE：向自己的模式中的表插入记录
- INSERT ANY TABLE：向任意模式中的表插入记录
- UPDATE TABLE：更新自己的模式中的表的记录
- UPDATE ANY TABLE：更新任意模式中的表的记录
- DELETE TABLE：删除自己的模式中的表的记录
- DELETE ANY TABLE：删除任意模式中的表的记录
- SELECT TABLE：查询自己模式中的表的记录
- SELECT ANY TABLE：查询任意模式中的表的记录
- REFERENCES TABLE：引用自己的模式中的表
- REFERENCES ANY TABLE：引用任意 m 哦是中的表
- DUMP TABLE：导出自己模式中的表
- DUMP ANY TABLE：导出任意模式中的表
- GRANT TABLE：向其他用户进行自己模式中的表上权限的授权
- GRANT ANY TABLE：向其他用户进行任意模式中的表上权限的授权
- FLASHBACK TABLE：闪回自己模式中的表
- FLASHBACK ANY TABLE：闪回任意模式中的表

而对于存储程序对象，其相关的数据库权限则包括：

- CREATE PROCEDURE：在自己的模式中创建存储程序
- CREATE ANY PROCEDURE：在任意模式中创建存储程序
- DROP PROCEDURE：删除自己的模式中的存储过程
- DROP ANY PROCEDURE：删除任意模式中的存储程序
- EXECUTE PROCEDURE：执行自己模式中的存储程序
- EXECUTE ANY PROCEDURE：执行任意模式中的存储程序
- GRANT PROCEDURE：向其他用户进行自己模式中存储程序上权限的授权
- GRANT ANY PROCEDURE：向其他用户进行任意模式中存储程序上权限的授权

需要说明的是，表、视图、触发器、存储程序等对象为模式对象，在默认情况下对这些对象的操作都是在当前用户自己的模式下进行的。如果要在其他用户的模式下操作这些类型的对象，需要具有相应的 ANY 特权。例如，要能够在其他用户的模式下创建表，当前用户必须具有 CREATE ANY TABLE 数据库权限，如果希望能够在其他用户的模式下删除表，必须具有 DROP ANY TABLE 数据库权限。

> **建议**
> 
> **DM中有一个较特殊的数据库权限“CREATE SESSION”，表示创建会话连接数据库的权限。系统预设的管理员用户都具备此权限，新建用户缺省也具备此权限，管理员可根据实际需要回收指定用户的CREATE SESSION权限以限制该用户连接数据库。**

### 3.1.2 对象权限

对象权限主要是对数据库对象中的数据的访问权限，主要用来授予需要对某个数据库对象的数据进行操纵的数据库普通用户。表 3.2 列出了主要的对象权限。

表3.2 常用的对象权限

| **数据库对象类型对象权限** | **表** | **视图** | **存储程序** | **包** | **类** | **类型** | **序列** | **目录** | **域** /CHARACTER SET /COLLATION |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SELECT | √ | √ |  |  |  |  | √ |  |  |
| INSERT | √ | √ |  |  |  |  |  |  |  |
| DELETE | √ | √ |  |  |  |  |  |  |  |
| UPDATE | √ | √ |  |  |  |  |  |  |  |
| REFERENCES | √ | √ |  |  |  |  |  |  |  |
| SELECT FOR DUMP | √ |  |  |  |  |  |  |  |  |
| EXECUTE |  |  | √ | √ | √ | √ |  | √ |  |
| READ |  |  |  |  |  |  |  | √ |  |
| WRITE |  |  |  |  |  |  |  | √ |  |
| USAGE |  |  |  |  |  |  |  |  | √ |
| FLASHBACK | √ | √ |  |  |  |  |  |  |  |
| INDEX | √ |  |  |  |  |  |  |  |  |
| ALTER | √ |  |  |  |  |  |  |  |  |

SELECT、INSERT、DELETE 和 UPDATE 权限分别是针对数据库对象中的数据的查询、插入、删除和修改的权限。对于表和视图来说，删除操作是整行进行的，而查询、插入和修改却可以在一行的某个列上进行，所以在指定权限时，DELETE 权限只要指定所要访问的表就可以了，而 SELECT、INSERT 和 UPDATE 权限还可以进一步指定是对哪个列的权限。

表对象的 REFERENCES 权限是指可以与一个表建立关联关系的权限，如果具有了这个权限，当前用户就可以通过自己的一个表中的外键，与对方的表建立关联。关联关系是通过主键和外键进行的，所以在授予这个权限时，可以指定表中的列，也可以不指定。

表对象的 SELECT FOR DUMP 权限是指导出表对象的权限，需要与同一表对象的 SELECT 的权限一起授予才能成功将该表对象导出。

视图对象语法上支持授权 REFERENCES 和 FLASHBACK 权限，但实际不起作用。

存储程序等对象的 EXECUTE 权限是指可以执行这些对象的权限。有了这个权限，一个用户就可以执行另一个用户的存储程序、包、类等。

目录对象的 READ 和 WRITE 权限指可以读或写访问某个目录对象的权限。

域对象的 USAGE 权限指可以使用某个域对象的权限。拥有某个域的 USAGE 权限的用户可以在定义或修改表时为表列声明使用这个域。

当一个用户获得另一个用户的某个对象的访问权限后，可以以“模式名.对象名”的形式访问这个数据库对象。一个用户所拥有的对象和可以访问的对象是不同的，这一点在数据字典视图中有所反映。在默认情况下用户可以直接访问自己模式中的数据库对象，但是要访问其他用户所拥有的对象，就必须具有相应的对象权限。

对象权限的授予一般由对象的所有者完成，也可由 SYSDBA 或具有某对象权限且具有转授权限的用户授予，但最好由对象的所有者完成。

## 3.2 角色管理

角色是一组权限的组合，使用角色的目的是使权限管理更加方便。假设有 10 个用户，这些用户为了访问数据库，至少拥有 CREATE TABLE、CREATE VIEW 等权限。如果将这些权限分别授予这些用户，那么需要进行的授权次数是比较多的。但是如果把这些权限事先放在一起，然后作为一个整体授予这些用户，那么每个用户只需一次授权，授权的次数将大大减少，而且用户数越多，需要指定的权限越多，这种授权方式的优越性就越明显。这些事先组合在一起的一组权限就是角色，角色中的权限既可以是数据库权限，也可以是对象权限，还可以是别的角色。

为了使用角色，首先在数据库中创建一个角色，这时角色中没有任何权限。然后向角色中添加权限。最后将这个角色授予用户，这个用户就具有了角色中的所有权限。在使用角色的过程中，可以随时向角色中添加权限，也可以随时从角色中删除权限，用户的权限也随之改变。如果要回收所有权限，只需将角色从用户回收即可。

### 3.2.1 角色的创建与删除

#### 3.2.1.1 DM 预定义角色

在 DM 数据库中有两类角色，一类是 DM 预设定的角色，一类是用户自定义的角色。DM 提供了一系列的预定义角色以帮助用户进行数据库权限的管理。预定义角色在数据库被创建之后即存在，并且已经包含了一些权限，数据库管理员可以将这些角色直接授予用户。

在“三权分立”和“四权分立”机制下，DM 的预定义角色及其所具有的权限是不相同的。表 3.3 和表 3.4 分别列出了“三权分立”和“四权分立”机制下常见的系统角色及其简单介绍，完整的预定义角色权限列表请参见附录 1 和附录 2。

表3.3 “三权分立”常见的数据库预设定的角色

| **角色名称** | **角色简单说明** |
| --- | --- |
| DBA | DM 数据库系统中对象与数据操作的最高权限集合，拥有构建数据库的全部特权，只有 DBA 才可以创建数据库结构 |
| RESOURCE | 可以创建数据库对象，对有权限的数据库对象进行数据操纵，不可以创建数据库结构 |
| PUBLIC | 不可以创建数据库对象，只能对有权限的数据库对象进行数据操纵。常规情况下，不建议回收用户的 PUBLIC 角色，一旦用户的 PUBLIC 角色被回收，将导致很多功能因权限不够无法使用 |
| VTI | 具有系统动态视图的查询权限。VTI 默认授权给 DBA 角色且可转授，不支持从 DBA 中回收 VTI。可以为 SYSDBA 授予和回收 VTI |
| SOI | 具有非审计/安全系统表的查询权限。SOI 默认授权给 SYSDBA 用户且可转授，不支持从 SYSDBA 回收 SOI |
| SVI | 具有基础 V 视图的查询权限。SVI 默认授权给 PUBLIC 且可转授，不支持从 PUBLIC 中回收 SVI。可以为 SYSDBA 授予和回收 SVI |
| DB\_AUDIT\_ADMIN | 数据库审计的最高权限集合，可以对数据库进行各种审计操作，并创建新的审计用户 |
| DB\_AUDIT\_OPER | 可以对数据库进行各种审计操作，但不能创建新的审计用户 |
| DB\_AUDIT\_PUBLIC | 无实际权限 |
| DB\_AUDIT\_VTI | 具有系统动态视图的查询权限，DB\_AUDIT\_VTI 默认授权给 DB\_AUDIT\_ADMIN 且可转授 |
| DB\_AUDIT\_SOI | 具有基础类系统表和与审计操作相关的系统表的查询权限 |
| DB\_AUDIT\_SVI | 具有基础 V 视图和审计 V 视图的查询权限。DB\_AUDIT\_SVI 默认授权给 DB\_AUDIT\_PUBLIC 且可转授 |
| DB\_POLICY\_ADMIN | 数据库强制访问控制的最高权限集合，可以对数据库进行强制访问控制管理，并创建新的安全管理用户 |
| DB\_POLICY\_OPER | 可以对数据库进行强制访问控制管理，但不能创建新的安全管理用户 |
| DB\_POLICY\_PUBLIC | 无实际权限 |
| DB\_POLICY\_VTI | 具有系统动态视图的查询权限，DB\_POLICY\_VTI 默认授权给 DB\_POLICY\_ADMIN 且可转授 |
| DB\_POLICY\_SOI | 具有基础类系统表和与安全操作相关的系统表的查询权限 |
| DB\_POLICY\_SVI | 具有基础 V 视图和安全 V 视图的查询权限 |
| SYS\_ADMIN | 系统预留角色 ，暂未启用 |
| SELECT\_CATALOG\_ROLE | METADATA.GET\_DDL 专用，查询相同类型其他用户的对象、或 SYSDBO 用户（包含创建的用户）下的对象、或 SYS 模式下的对象。此处的相同类型其他用户是指 SYSDBA 或 SYSDBA 创建的用户。SELECT\_CATALOG\_ROLE 默认授权给 DBA 角色且可转授 |
| DB\_AUDIT\_SELECT\_CATALOG\_ROLE | METADATA.GET\_DDL 专用，查询相同类型其他用户或不同类型用户的对象（包含 SYS 模式)。DB\_AUDIT\_SELECT\_CATALOG\_ROLE 默认授权给 DB\_AUDIT\_ADMIN 角色且可转授 |
| DB\_POLICY\_SELECT\_CATALOG\_ROLE | METADATA.GET\_DDL 专用，查询相同类型其他用户或不同类型用户的对象（包含 SYS 模式)。DB\_POLICY\_SELECT\_CATALOG\_ROLE 默认授权给 DB\_POLICY\_ADMIN 角色且可转授 |

表3.4 “四权分立”常见的数据库预设定的角色

| **角色名称** | **角色简单说明** |
| --- | --- |
| DBA | 拥有构建数据库的全部特权，只有 DBA 才可以创建数据库结构 |
| RESOURCE | 可以创建和删除角色 |
| PUBLIC | 只能查询相关的数据字典表 |
| VTI | 具有系统动态视图的查询权限。VTI 默认授权给 DBA 角色且可转授，不支持从 DBA 中回收 VTI。可以为 SYSDBA 授予和回收 VTI |
| SOI | 具有非审计/安全系统表的查询权限。SOI 默认授权给 SYSDBA 用户且可转授，不支持从 SYSDBA 回收 SOI |
| SVI | 具有基础 V 视图的查询权限。SVI 默认授权给 PUBLIC 且可转授，不支持从 PUBLIC 中回收 SVI。可以为 SYSDBA 授予和回收 SVI |
| DB\_AUDIT\_ADMIN | 数据库审计的最高权限集合，可以对数据库进行各种审计操作，并创建新的审计用户 |
| DB\_AUDIT\_OPER | 可以对数据库进行各种审计操作，但不能创建新的审计用户 |
| DB\_AUDIT\_PUBLIC | 无实际权限 |
| DB\_AUDIT\_VTI | 具有系统动态视图的查询权限，DB\_AUDIT\_VTI 默认授权给 DB\_AUDIT\_ADMIN 且可转授 |
| DB\_AUDIT\_SOI | 具有基础类系统表和与审计操作相关的系统表的查询权限 |
| DB\_AUDIT\_SVI | 具有基础 V 视图和审计 V 视图的查询权限。DB\_AUDIT\_SVI 默认授权给 DB\_AUDIT\_PUBLIC 且可转授 |
| DB\_POLICY\_ADMIN | 数据库强制访问控制的最高权限集合，可以对数据库进行强制访问控制管理，并创建新的安全管理用户 |
| DB\_POLICY\_OPER | 可以对数据库进行强制访问控制管理，但不能创建新的安全管理用户 |
| DB\_POLICY\_PUBLIC | 无实际权限 |
| DB\_POLICY\_VTI | 具有系统动态视图的查询权限，DB\_POLICY\_VTI 默认授权给 DB\_POLICY\_ADMIN 且可转授 |
| DB\_POLICY\_SOI | 具有基础类系统表和与安全操作相关的系统表的查询权限 |
| DB\_POLICY\_SVI | 具有基础 V 视图和安全 V 视图的查询权限 |
| DB\_OBJECT\_ADMIN | 可以在自己的模式下创建各种数据库对象并进行数据操纵，也可以创建和删除非模式对象 |
| DB\_OBJECT\_OPER | 可以在自己的模式下创建数据库对象并进行数据操纵 |
| DB\_OBJECT\_PUBLIC | 不可以创建数据库对象，只能对有权限的数据库对象进行数据操纵 |
| DB\_OBJECT\_VTI | 具有系统动态视图的查询权限，DB\_OBJECT\_VTI 默认授权给 DB\_OBJECT\_ADMIN 且可转授 |
| DB\_OBJECT\_SOI | 具有非审计/安全系统表的查询权限 |
| DB\_OBJECT\_SVI | 和 SVI 权限一样 |
| SYS\_ADMIN | 系统内部角色，具有 CREATE ANY TRIGGER 和 DROP ANY TRIGGER 权限。四权分立时，由于没有 CREATE ANY TRIGGER 和 DROP ANY TRIGGER 权限, 系统自动将 SYS\_ADMIN 授权给 SYSDBA，只有具备 SYS\_ADMIN 时 SYSDBA 才可以创建库级的事件触发器。SYS\_ADMIN 既不可转授，也不可从 SYSDBA 回收 |
| SELECT\_CATALOG\_ROLE | METADATA.GET\_DDL 专用，查询相同类型其他用户的对象、或 SYSDBO 用户（包含创建的用户）下的对象、或 SYS 模式下的对象。此处的相同类型其他用户是指 SYSDBA 或 SYSDBA 创建的用户。SELECT\_CATALOG\_ROLE 默认授权给 DBA 角色且可转授 |
| DB\_AUDIT\_SELECT\_CATALOG\_ROLE | METADATA.GET\_DDL 专用，查询相同类型其他用户或不同类型用户的对象（包含 SYS 模式)。DB\_AUDIT\_SELECT\_CATALOG\_ROLE 默认授权给 DB\_AUDIT\_ADMIN 角色且可转授 |
| DB\_POLICY\_SELECT\_CATALOG\_ROLE | METADATA.GET\_DDL 专用，查询相同类型其他用户或不同类型用户的对象（包含 SYS 模式)。DB\_POLICY\_SELECT\_CATALOG\_ROLE 默认授权给 DB\_POLICY\_ADMIN 角色且可转授 |
| DB\_OBJECT\_SELECT\_CATALOG\_ROLE | METADATA.GET\_DDL 专用，查询相同类型其他用户的对象、或 SYSDBA 用户（包含创建的用户）下的对象、或 SYS 模式下的对象。此处的相同类型其他用户是指 SYSDBO 或 SYSDBO 创建的用户。DB\_OBJECT\_SELECT\_CATALOG\_ROLE 默认授权给 DB\_OBJECT \_ADMIN 角色且可转授 |

根据角色拥有的工作权限的不同，可以将预定义角色分为 DBA 类型预定义角色、AUDITOR 类型预定义角色、SSO 类型预定义角色和 DBO 类型预定义角色。下面详细介绍：

- DBA 类型预定义角色拥有部分管理员工作权限，有权利执行一部分管理员工作。DBA 类型预定义角色包括 DBA、RESOURCE、PUBLIC、VTI、SOI、SVI、SYS\_ADMIN、SELECT\_CATALOG\_ROLE；
- AUDITOR 类型预定义角色拥有部分审计员工作权限，有权利执行一部分审计员工作。AUDITOR 类型预定义角色包括 DB\_AUDIT\_ADMIN、DB\_AUDIT\_OPER、DB\_AUDIT\_PUBLIC、DB\_AUDIT\_VTI、DB\_AUDIT\_SOI、DB\_AUDIT\_SVI、DB\_AUDIT\_SELECT\_CATALOG\_ROLE；
- SSO 类型预定义角色拥有部分安全员工作权限，有权利执行一部分安全员工作。SSO 类型预定义角色包括 DB\_POLICY\_ADMIN、DB\_POLICY\_OPER、DB\_POLICY\_PUBLIC、DB\_POLICY\_VTI、DB\_POLICY\_SOI、DB\_POLICY\_SVI、DB\_POLICY\_SELECT\_CATALOG\_ROLE；
- DBO 类型预定义角色拥有部分对象操作员工作权限，有权利执行一部分对象操作员工作。DBO 类型预定义角色包括 DB\_OBJECT\_ADMIN、DB\_OBJECT\_OPER、DB\_OBJECT\_PUBLIC、DB\_OBJECT\_VTI、DB\_OBJECT\_SOI、DB\_OBJECT\_SVI、DB\_OBJECT\_SELECT\_CATALOG\_ROLE。

初始时仅有管理员具有创建用户的权限，每种类型的管理员创建的用户缺省就拥有这种类型的 PUBLIC 和 SOI 预定义角色，如 SYSAUDITOR 新创建的用户缺省就具有 DB\_AUDIT\_PUBLIC 和 DB\_AUDIT\_SOI 角色。之后管理员可根据需要进一步授予新建用户其他预定义角色。

当不使用 SP\_RESTRICT\_DBA（1）限制 DBA 角色的 ANY 特权时，由于 DBA 角色拥有 ADMIN ANY DATABASE PRIVILEGE 特权，因此 DBA 类型用户可以将 CREATE USER 权限转授给其他用户，非 DBA 类型用户的用户不可以。当使用 SP\_RESTRICT\_DBA（1）限制 DBA 的 ANY 特权时，因为限制了 ADMIN ANY DATABASE PRIVILEGE，所以此时所有用户都无法转授 CREATE USER 权限。

拥有 CREATE USER 权限的用户可以创建新的用户，他们创建的新用户缺省也具有与其创建者相同类型的 PUBLIC 预定义角色。

■ **限制 DBA 的 ANY 特权**

从附录 1 和附录 2 的表中我们可以看到，缺省情况下，DBA 角色拥有许多的 ANY 特权，如 DROP ANY TABLE、INSERT ANY TABLE 等等。DM 提供了一种限制 DBA 的 ANY 特权的方法：在非 DM 安全版本中，只有 SYSDBA 用户才能限制 DBA 的 ANY 特权；在 DM 安全版本中，只有具有 DB\_POLICY\_ADMIN 角色的用户才能限制 DBA 的 ANY 特权。通过执行下面的系统过程来实现，系统过程执行完成后需要重启服务器该限制才能生效。

```
VOID
SP_RESTRICT_DBA(
    FLAG INT
);
```

参数 FLAG 置为 1 表示限制 DBA 的 ANY 特权，此过程执行后所有的 DBA 用户将不再具有 ANY 特权；FLAG 置为 0 表示不限制 DBA 的 ANY 特权。

#### 3.2.1.2 创建角色

具有“CREATE ROLE”数据库权限的用户也可以创建新的角色，其语法如下：

```
CREATE ROLE [IF NOT EXISTS] <角色名>;
```

**使用说明：**

1. 创建者必须具有 CREATE ROLE 数据库权限；
2. 角色名的长度不能超过 128 个字符；
3. 角色名不允许和系统已存在的用户名重名；
4. 角色名不允许是 DM 保留字。

例 创建角色 BOOKSHOP\_ROLE1，赋予其 PERSON.ADDRESS 表的 SELECT 权限。

```
CREATE ROLE BOOKSHOP_ROLE1;
GRANT SELECT ON PERSON.ADDRESS TO BOOKSHOP_ROLE1;
```

#### 3.2.1.3 删除角色

具有“DROP ROLE”权限的用户可以删除角色，其语法如下：

```
DROP ROLE [IF EXISTS] <角色名>;
```

即使已将角色授予了其他用户，删除这个角色的操作也将成功。此时，那些之前被授予该角色的用户将不再具有这个角色所拥有的权限，除非用户通过其他途径也获得了这个角色所具有的权限。

指定 IF EXISTS 关键字后，删除不存在的角色时不会报错，否则会报错。

例如，接上一小节的例子。将角色 BOOKSHOP\_ROLE1 授予用户 BOOKSHOP\_USER，则用户 BOOKSHOP\_USER 具有了 SELECT 表 PERSON.ADDRESS 的权限。此时删除角色 BOOKSHOP\_ROLE1，那么用户 BOOKSHOP\_USER 将不再能查询表 PERSON.ADDRESS。但是如果用户 BOOKSHOP\_USER 从别的途径（直接授权或通过别的角色授权）重复获得了 SELECT 表 PERSON.ADDRESS 的权限，那么即使删除了角色 BOOKSHOP\_ROLE1，用户 BOOKSHOP\_USER 仍然具有 SELECT 表 PERSON.ADDRESS 的权限。

### 3.2.2 角色的启用与禁用

某些时候，用户不愿意删除一个角色，但是却希望这个角色失效，此时可以使用 DM 系统过程 SP\_SET\_ROLE 来设置这个角色为不可用，将第二参数置为 0 表示禁用角色。

例 下面的语句将角色 BOOKSHOP\_ROLE1 禁用。

```
SP_SET_ROLE('BOOKSHOP_ROLE1', 0);
```

**使用说明：**

1. 只有拥有 ADMIN\_ANY\_ROLE 权限的用户才能启用和禁用角色，并且设置后立即生效；
2. 凡是包含禁用角色 A 的角色 M，M 中禁用的角色 A 将无效，但是 M 仍有效；
3. 系统预设的角色是不能设置的，如：DBA、PUBLIC、RESOURCE。

当用户希望启用某个角色时，同样可以通过 SP\_SET\_ROLE 来启用角色，只要将第二个参数置为 1 即可。

例 下面的语句将启用角色 BOOKSHOP\_ROLE1。

```
SP_SET_ROLE('BOOKSHOP_ROLE1', 1);
```

### 3.2.3 SVI 角色用法

在启用了 SVI 环境的情况下，拥有 SVI 角色权限的用户可以查询 V 视图。V 视图请参考《DM8 系统管理员手册》。缺省情况下系统未启用 SVI 环境，因此需要使用 V 视图的用户，须先手动启用 SVI 环境，即执行 SP\_INIT\_SVI\_SYS(1)和 SP\_SWITCH\_SVI(1)过程。

下面是使用 SVI 角色的相关系统过程：

1. SP\_INIT\_SVI\_SYS

**定义：**

```
SP_INIT_SVI_SYS(

CREATE_FLAG   int

)
```

**功能说明：**

可以手动创建所有 V 视图，并授权给 SVI、DB\_POLICY\_SVI、DB\_OBJECT\_SVI 和 DB\_AUDIT\_SVI。只有 DBA 和 DB\_OBJECT\_ADMIN 可以执行。

**参数详解**

CREATE\_FLAG：1 创建所有 V 视图；0 删除所有 V 视图

**返回值**

无

**举例说明**

```
SP_INIT_SVI_SYS(1);

SP_INIT_SVI_SYS(0);
```
2. SP\_SWITCH\_SVI

**定义：**

```
SP_SWITCH_SVI(

flag      int

)
```

**功能说明：**

SVI 环境启用或禁用。只有 DBA/DB\_OBJECT\_ADMIN 可以执行。SVI 启用时字典信息来源于 V 视图， 禁用字典信息来源于 SYS.数据字典表。

SP\_INIT\_SVI\_SYS(1)需和 SP\_SWITCH\_SVI(1)一起使用，SP\_INIT\_SVI\_SYS(0)需和 SP\_SWITCH\_SVI(0)一起使用，才有效果。否则报错。

**参数说明：**

flag：1 启用 SVI 环境；0 禁用 SVI 环境

**返回值：**

启用返回 1；禁用返回 0

**举例说明：**

```
SP_SWITCH_SVI(0); 

SP_SWITCH_SVI(1);
```
3. SF\_GET\_SVI

**定义：**

```
SF_GET_SVI ()
```

**功能说明：**

获取当前系统是否启用 SVI 环境 。

**参数说明：**

无

**返回值：**

启用返回 1；禁用返回 0

**举例说明：**

```
SP_SWITCH_SVI(0); 
SELECT SF_GET_SVI;  //结果为0
SP_SWITCH_SVI(1); 
SELECT SF_GET_SVI;  //结果为1
```

## 3.3 权限的分配与回收

可以通过 GRANT 语句将权限（包括数据库权限、对象权限、角色权限和模式权限）分配给用户和角色，之后也可以使用 REVOKE 语句将授出的权限再进行回收。

### 3.3.1 数据库权限的分配与回收

#### 3.3.1.1 数据库权限的分配

可以使用 GRANT 语句授予用户和角色数据库权限。

数据库权限的授权语句语法为：

```
GRANT <特权> TO <用户或角色>{,<用户或角色>} [WITH ADMIN OPTION];
<特权> ::= <数据库权限>{,<数据库权限>};
<用户或角色>::= <用户名> | <角色名>
```

**使用说明：**

1. 授权者必须具有对应的数据库权限以及其转授权。四权分立下四类管理员（DBA、SSO、AUDITOR、DBO）均不能转授 PROFILE 权限（CREATE PROFILE、DROP PROFILE、ALTER PROFILE）和 USER 权限（CREATE USER、ALTER USER、DROP USER）；三权分立下只有管理员 DBA 能转授 PROFILE 权限和 USER 权限，管理员 SSO 和 AUDITOR 不能转授 PROFILE 权限和 USER 权限；
2. 接受者必须与授权者用户类型一致；
3. 数据库权限及其与 DM 预定义角色的关系列表可参考附录 1 与附录 2；
4. WITH ADMIN OPTION 表示可以转授，即被授权者可以把这些权限继续授予给其他用户或角色，缺省不能转授。例如：A 将权限转授给 B，B 又将权限转授给 C。那么 A→B→C 之间就形成了一个链式关系。

例 系统管理员 SYSDBA 把建表的权限授予用户 BOOKSHOP\_USER1，并允许其转授。BOOKSHOP\_USER1 把权限继续转授给 BOOKSHOP\_USER2。

```
//SYSDBA执行。SYSDBA将权限授予BOOKSHOP_USER1
GRANT CREATE TABLE TO BOOKSHOP_USER1 WITH ADMIN OPTION; --使用WITH ADMIN OPTION，BOOKSHOP_USER1才可转授
//BOOKSHOP_USER1执行。BOOKSHOP_USER1将从SYSDBA获取的权限转授给BOOKSHOP_USER2
GRANT CREATE TABLE TO BOOKSHOP_USER2;--BOOKSHOP_USER2被授权成功，但不可继续转授
GRANT CREATE TABLE TO BOOKSHOP_USER2 WITH ADMIN OPTION;--BOOKSHOP_USER2被授权成功，且可继续转授
```

#### 3.3.1.2 数据库权限的回收

可以使用 REVOKE 语句回收授出的指定数据库权限。

回收数据库权限的语句语法为：

```
REVOKE [ADMIN OPTION FOR]<特权> FROM <用户或角色>{,<用户或角色>} ;
<特权> ::= <数据库权限>{,<数据库权限>}
<用户或角色>::= <用户名> | <角色名>
```

**使用说明：**

1. 权限回收者必须是具有回收相应数据库权限以及转授权的用户；
2. ADMIN OPTION FOR 选项的意义是取消用户或角色的转授权限，但是权限不回收。

**例 1** 接 3.3.1.1 中的例子，现在 SYSDBA 把用户 BOOKSHOP\_USER1 的建表权限收回。

```
REVOKE CREATE TABLE FROM BOOKSHOP_USER1;
```

**例 2** 接 3.3.1.1 中的例子，之前 SYSDBA 把建视图的权限授给了用户 BOOKSHOP\_USER1，并且允许转授。现在 SYSDBA 不让用户 BOOKSHOP\_USER1 转授 CREATE VIEW 权限。

```
REVOKE ADMIN OPTION FOR CREATE VIEW FROM BOOKSHOP_USER1;
```

BOOKSHOP\_USER1 仍有 CREATE VIEW 权限，但是不能将 CREATE VIEW 权限转授给其他用户。

#### 3.3.1.3 限制相关数据库权限的授予与回收

通过 INI 参数 ENABLE\_DDL\_ANY\_PRIV 限制 DDL 相关的 ANY 特权的授予与回收，有 2 个取值：

- 1：可以授予和回收 DDL 相关的 ANY 特权；
- 0：不可以授予和回收 DDL 相关的 ANY 特权。缺省为 0。

例 当 ENABLE\_DDL\_ANY\_PRIV=0 时，SYSDBA 无法授予或回收 create any trigger 权限。

```
create user DBSEC  identified by "Dbsec_123";
GRANT create any trigger TO DBSEC;    //报错
revoke create any trigger from DBSEC; //报错
```

### 3.3.2 对象权限的分配与回收

#### 3.3.2.1 对象权限的分配

可以使用 GRANT 语句将对象权限授予用户和角色。

对象权限的授权语句语法为：

```
GRANT <特权> [OFF] ON <对象> TO <用户或角色>{,<用户或角色>} [WITH GRANT OPTION];
<特权>::= ALL [PRIVILEGES] | 
<动作> {, <动作>}
<动作>::= SELECT[(<列清单>)] |
         INSERT[(<列清单>)] | 
         UPDATE[(<列清单>)] | 
         DELETE | 
         REFERENCES[(<列清单>)] |
         EXECUTE |
         READ |
         WRITE |
         USAGE |
         INDEX |
         ALTER |
         SELECT FOR DUMP |
         FLASHBACK
<列清单>::= <列名> {,<列名>}
<对象> ::= SCHEMA <模式名> |
           DIRECTORY <目录名> |
           [<对象类型>] [<模式名>.] <对象名>
<对象类型>::= TABLE | VIEW | PROCEDURE | FUNCTION | PACKAGE | CLASS | TYPE | SEQUENCE |  DOMAIN |  SYNONYM | LIBRARY
<对象名> ::= <表名> | <视图名> | <存储过程/函数名> |<包名> |<类名> |<类型名> |<序列名> | <域名> | <同义词名> | <LIBRARY名>
<用户或角色>::= <用户名> | <角色名>
```

**使用说明：**

1. 授权者必须是具有对应对象权限以及其转授权的用户；
2. 使用 INI 参数 OBJECT\_PRIV\_MODE 可控制授权策略是否兼容 ORACLE；
3. OFF 授予黑名单权限，即关闭（黑名单）用户的模式级对象权限。模式级对象权限是指 < 对象类型 > 为 SCHEMA 的权限；
4. < 对象 > 为 SCHEMA 时，须提前设置 INI 参数 GRANT\_SCHEMA=1 或 2，即开启授予和回收模式权限功能。授权用户需要具有对授权模式的"GRANT ANY OBJECT PRIVILEGE"权限。此时，< 动作 > 为 EXECUTE、READ 、WRITE，虽然可授权成功，但不起作用。设置 INI 参数 GRANT\_SCHEMA=1 时，ALL 或 ALL PRIVILEGES 表示将指定模式的所有对象权限都授予被授予者；
5. 如未指定 < 对象 > 的 < 模式名 >，模式为授权者所在的模式。DIRECTORY 为非模式对象，没有模式；
6. 如设定了对象类型，则该类型必须与对象的实际类型一致，否则会报错；
7. WITH GRANT OPTION 表示可以转授，即被授权者可以把这些权限继续授予其他用户或角色，缺省不能转授；
8. 不带列清单授权时，如果对象上存在同类型的列权限，会全部自动合并；
9. < 特权 > 为 ALL 或 ALL PRIVILEGES 时，表示将指定的数据库对象上所有的对象权限都授予被授权者。不同类型的数据库对象相关的对象权限见\[3.1.2 对象权限 \](#3.1.2 对象权限)的介绍；
10. 对于用户所在的模式的表，用户具有所有权限而不需特别指定；
11. INDEX 动作向其他用户授予指定表的创建和删除索引（包含全文索引）的权限；
12. ALTER 动作仅支持向其他用户授予指定表的修改权限、表（列）注释权限和指定序列的修改权限。

当授权语句中使用了 ALL PRIVILEGES 时，会将指定的数据库对象上所有的对象权限都授予被授权者。不同类型的数据库对象相关的对象权限见 3.1.2 节的介绍。

**例 1** SYSDBA 把 PERSON.ADDRESS 表的全部权限授给用户 BOOKSHOP\_USER1。

```
GRANT ALL PRIVILEGES ON PERSON.ADDRESS TO BOOKSHOP_USER1;
```

\*\*例 2 \*\*假设用户 BOOKSHOP\_USER1 创建了存储过程 BOOKSHOP\_USER1\_PROC1，数据库管理员 SYSDBA 把该存储过程的执行权 EXECUTE 授给已存在用户 BOOKSHOP\_USER2，并使其具有该权限的转授权。

```
GRANT EXECUTE ON PROCEDURE BOOKSHOP_USER1.BOOKSHOP_USER1_PROC1 TO BOOKSHOP_USER2 WITH GRANT OPTION;
```

**例 3** 假设 SYSDBA 是表 BOOKSHOP\_T1 的创建者，用户 BOOKSHOP\_USER1、BOOKSHOP\_USER2、BOOKSHOP\_USER3 存在，且都不是 DBA 权限用户。

```
//以SYSDBA身份登录，并执行语句：
GRANT SELECT ON BOOKSHOP_T1 TO BOOKSHOP_USER1 WITH GRANT OPTION;
//以BOOKSHOP_USER1身份登录，并执行语句：
GRANT SELECT ON SYSDBA.BOOKSHOP_T1 TO BOOKSHOP_USER2;
//以BOOKSHOP_USER2身份登录，并执行语句：
GRANT SELECT ON SYSDBA.BOOKSHOP_T1 TO BOOKSHOP_USER3;
//错误，用户BOOKSHOP_USER2没有SELECT权限的转授权
```

**例 4** 用户 SYSDBA 创建一个名为 VIEW\_PRODUCT 的视图，要求对于该视图，允许 BOOKSHOP\_USER1 能够进行查询、插入、删除和更新操作，用户 BOOKSHOP\_USER2 和 BOOKSHOP\_USER3 也可进行同样的工作，但要求其操作权限由用户 BOOKSHOP\_USER1 控制。

```
//以SYSDBA的身份登录：
CREATE VIEW VIEW_PRODUCT AS 
SELECT * FROM PRODUCTION.PRODUCT
WHERE NOWPRICE>=20 AND ORIGINALPRICE<40 WITH CHECK OPTION;
GRANT SELECT, INSERT, DELETE, UPDATE ON VIEW_PRODUCT
TO BOOKSHOP_USER1 WITH GRANT OPTION; 
//以用户BOOKSHOP_USER1的身份登录：
GRANT SELECT, INSERT, DELETE, UPDATE ON SYSDBA.VIEW_PRODUCT TO BOOKSHOP_USER2, BOOKSHOP_USER3;
```

**例 5** 假定表的创建者 SYSDBA 把所创建的 PRODUCTION.PRODUCT 表的部分列的更新权限授予用户 BOOKSHOP\_USER1，BOOKSHOP\_USER1 再将此更新权限转授给用户 BOOKSHOP\_USER2。

```
//首先，以SYSDBA的身份登录，并执行语句：
GRANT UPDATE (ORIGINALPRICE, NOWPRICE) ON PRODUCTION.PRODUCT TO BOOKSHOP_USER1 WITH GRANT OPTION;
//其次，以BOOKSHOP_USER1的身份登录，并执行语句，把列级更新权限授给用户BOOKSHOP_USER2：
GRANT UPDATE(ORIGINALPRICE, NOWPRICE)ON PRODUCTION.PRODUCT TO BOOKSHOP_USER2;
```

\*\*例 6 \*\*使用 SYSDBA 创建用户 USER01 和 USER02，并把模式 USER02 下所有对象的查询权限授予用户 USER01。须提前开启 INI 参数 GRANT\_SCHEMA=1 或 2。

```
DROP USER USER01 CASCADE;
DROP USER USER02 CASCADE;
//创建用户时，系统自动创建了同名模式USER01，USER02
CREATE USER USER01 IDENTIFIED BY "USER01_psd"; 
CREATE USER USER02 IDENTIFIED BY "USER02_psd";
//授予用户USER02建表，插入的权限
GRANT CREATE TABLE,INSERT TABLE TO USER02;
//将模式USER02下所有对象的查询权限授予用户USER01
GRANT SELECT ON SCHEMA USER02 TO USER01;
//登录用户USER02
CREATE TABLE T1(C1 INT); 
INSERT INTO T1 VALUES(1);
COMMIT;
//登录用户USER01，可以查询成功
SELECT * FROM USER02.T1;
```

**例 7** 为黑名单用户 USER02 授予黑名单权限，即取消 USER02 的对象权限。须提前开启 INI 参数 GRANT\_SCHEMA=1 或 2。

```
//将USER01对象的查询权限授予USER02。此时user02获得user01对象的查询权限
GRANT SELECT ON SCHEMA USER01 TO USER02; 
//为USER02授予黑名单权限。此时USER02失去USER01的T1的查询权限
GRANT SELECT OFF ON USER01.T1 TO USER02;
```

**例 8** 为用户 USER1 授予 ALTER 对象权限，ALTER 权限包括对表（列）的注释权限。

```
//SYSDBA登录，先创建用户和表，然后把ALTER权限授予USER1
CREATE USER USER1 IDENTIFIED BY "USER1_psd";
CREATE TABLE TESTT(C1 INT);
GRANT ALTER ON  TESTT TO USER1;
// USER1登录，对TESTT表进行注释，可注释成功
COMMENT ON TABLE SYSDBA.TESTT IS 'COMMENT IN ALTER';
//SYSDBA登录，进行查询
SELECT * FROM  SYSTABLECOMMENTS WHERE TVNAME='TESTT';
行号       SCHNAME TVNAME TABLE_TYPE COMMENT$
---------- ------- ------ ---------- --------
1          SYSDBA  TESTT TABLE      COMMENT IN ALTER
```

#### 3.3.2.2 对象权限的回收

可以使用 REVOKE 语句回收授出的指定数据库对象的指定权限。

对象权限的回收语句语法为：

```
REVOKE [GRANT OPTION FOR] <特权> [OFF] ON <对象> FROM <用户或角色> {,<用户或角色>} [<回收选项>];
<特权>::= ALL [PRIVILEGES] | 
         <动作> {, <动作>}
<动作>::= SELECT |
         INSERT | 
         UPDATE | 
         DELETE | 
         REFERENCES |
         EXECUTE |
         READ |
         WRITE |
         USAGE |
         INDEX |
         ALTER |
         SELECT FOR DUMP |
         FLASHBACK
<对象> ::= SCHEMA <模式名> |
          DIRECTORY <目录名> |
          [<对象类型>] [<模式名>.] <对象名>
<对象类型>::= TABLE | VIEW | PROCEDURE | FUNCTION | PACKAGE | CLASS | TYPE | SEQUENCE |  DOMAIN | SYNONYM | LIBRARY
<对象名> ::= <表名> | <视图名> | <存储过程/函数名> |<包名> |<类名> |<类型名> | <序列名> | <域名> | <同义词名> |<LIBRARY名>
<用户或角色>::= <用户名> | <角色名>
<回收选项> ::= RESTRICT | CASCADE
```

**使用说明：**

1. 权限回收者必须是具有回收相应对象权限以及转授权的用户；
2. 使用 INI 参数 OBJECT\_PRIV\_MODE 可控制权限回收策略是否兼容 ORACLE；
3. V8.1.4.109 版本之后，拥有特权 GRANT ANY OBJECT PRIVILEGE 的用户，能够回收任意对象权限；降级至 V8.1.4.107 及更早的版本，降级前由拥有特权 GRANT ANY OBJECT PRIVILEGE 或者 GRANT ANY XX（如 GRANT ANY TABLE/VIEW/PROCEDURE 等）或者特例授予的权限，只能由对象所属用户进行回收；
4. < 对象类型 > 为 SCHEMA 时，须提前设置 INI 参数 GRANT\_SCHEMA=1 或 2，即开启授予和回收模式权限功能；
5. 回收时不能带列清单，若对象上存在同类型的列权限，则一并被回收；
6. 使用 GRANT OPTION FOR 选项的目的是收回用户或角色权限转授的权利，而不回收用户或角色的权限；
7. < 回收选项 > 分为 CASCADE 和 RESTRICT。不同的回收选项，其意义不同。具体如下：
- CASCADE 表示级联回收，可回收授予时带或不带 WITH GRANT OPTION 的权限，若带 WITH GRANT OPTION 还会引起级联回收。级联回收指不仅收回该用户或角色直接拥有的权限，还同时回收所有因该用户或角色而间接获得这些权限的其他用户或角色的权限。例如：A 将 SELECT 授权（选择了 WITH GRANT OPTION）给 B，B 转授给 C，则使用 CASCADE 选项收回 A 的 SELECT 权限时，会将 B 和 C 的 SELECT 权限一同收回。利用此选项时不会检查权限是否存在依赖等限制。另外，利用此选项进行级联回收时，若被回收对象上存在另一条路径授予同样权限给该对象时，则仅需回收当前权限。
- RESTRICT 表示限制回收，只能回收授予时不带 WITH GRANT OPTION 的权限。无法回收授予时带 WITH GRANT OPTION 的权限，也无法回收存在依赖等限制的权限（如角色上的某权限被别的用户用于创建视图等）。
- 缺省 < 回收选项 >，表示无法回收授予时带 WITH GRANT OPTION 的权限，但也不会检查要回收的权限是否存在依赖等限制。

> **建议**
> 
> 用户A给用户B授权且允许其转授，B将权限转授给C。当A回收B的权限的时候必须加CASCADE回收选项。

例 1 接 3.3.2.1 节例 1，SYSDBA 从用户 BOOKSHOP\_USER1 处回收其授出的 PERSON.ADDRESS 表的全部权限。

```
REVOKE ALL PRIVILEGES ON PERSON.ADDRESS FROM BOOKSHOP_USER1 CASCADE;
```

例 2 接 3.3.2.1 节例 2，SYSDBA 从用户 BOOKSHOP\_USER2 处回收其授出的存储过程 BOOKSHOP\_USER1\_PROC1 的 EXECUTE 权限。

```
REVOKE EXECUTE ON PROCEDURE BOOKSHOP_USER1.BOOKSHOP_USER1_PROC1
FROM BOOKSHOP_USER2 CASCADE;
```

例 3 假定系统中存在非 SYSDBA 用户 BOOKSHOP\_USER1、BOOKSHOP\_USER2、BOOKSHOP\_USER3 和 BOOKSHOP\_USER4，其中 BOOKSHOP\_USER1 具有 CREATE TABLE 数据库权限，BOOKSHOP\_USER2 具有 CREATE VIEW 数据库权限，且已成功执行了如下的语句：

```
BOOKSHOP_USER1登录执行:
CREATE TABLE T1(ID INT, NAME VARCHAR(100));
GRANT SELECT ON T1 TO PUBLIC;
GRANT INSERT(ID) ON T1 TO BOOKSHOP_USER2 WITH GRANT OPTION;
BOOKSHOP_USER2登录执行:
CREATE VIEW V1 AS SELECT NAME FROM BOOKSHOP_USER1.T1 WHERE ID < 10;
BOOKSHOP_USER3登录执行:
GRANT INSERT(ID) ON BOOKSHOP_USER1.T1 TO BOOKSHOP_USER4 WITH GRANT OPTION;
BOOKSHOP_USER4登录执行:
GRANT INSERT(ID) ON BOOKSHOP_USER1.T1 TO BOOKSHOP_USER2 WITH GRANT OPTION;
```

此时，若 BOOKSHOP\_USER1 执行以下语句会引起之前授予的 INSERT(ID)权限被合并。

```
GRANT INSERT ON T1 TO BOOKSHOP_USER2 WITH GRANT OPTION;
```

若 BOOKSHOP\_USER1 执行以下语句，会成功，因为这种方式不检查权限是否存在限制。

```
REVOKE SELECT ON T1 FROM PUBLIC;
```

若 BOOKSHOP\_USER1 执行以下语句，则会失败，因为这种方式检查权限是否存在限制，即 BOOKSHOP\_USER2 利用此权限创建了视图 V1。

```
REVOKE SELECT ON T1 FROM PUBLIC RESTRICT;
```

若 BOOKSHOP\_USER1 执行以下语句，会进行级联回收 BOOKSHOP\_USER2、BOOKSHOP\_USER3、BOOKSHOP\_USER4 授出的 INSERT(ID)权限。

```
REVOKE INSERT ON T1 FROM BOOKSHOP_USER2 CASCADE;
```

但若 BOOKSHOP\_USER1 连续执行了以下两条语句，则后一条语句仅回收其授予 BOOKSHOP\_USER2 的权限，而不会产生级联回收，因为有另一条路经授予了 BOOKSHOP\_USER3 同样的权限 INSERT(ID)。

```
GRANT INSERT ON T1 TO BOOKSHOP_USER3 WITH GRANT OPTION;
REVOKE INSERT ON T1 FROM BOOKSHOP_USER2 CASCADE;
```

例 4 接 3.3.2.1 节例 7，回收黑名单权限。

```
//回收黑名单权限。此时USER02重新获得USER01的T1的查询权限
REVOKE SELECT OFF ON USER01.T1 FROM USER02;
```

### 3.3.3 角色权限的分配与回收

#### 3.3.3.1 角色权限的分配

通常角色包含权限或其他角色，通过使用 GRANT 语句将一个角色授予用户或另一角色可以使得用户和角色继承该角色所具有的权限。

授予角色权限的语句语法如下：

```
GRANT <角色名>{, <角色名>} TO <用户或角色>{,<用户或角色>} [WITH  ADMIN OPTION];
<用户名或角色名> ::= <用户名> | <角色名>
```

**使用说明：**

1. 角色的授予者必须为拥有相应的角色以及其转授权的用户。但有一点例外：四权分立下，SYSDBA、SYSDBO 虽然没有 ADMIN ANY ROLE 权限，但依然可以对其他用户或角色授予 SVI（由 SYSDBA 授予）、DB\_OBJECT\_SVI（由 SYSDBO 授予）角色权限；
2. 接受者必须与授权者类型一致(譬如不能把审计角色授予标记角色)；
3. WITH ADMIN OPTION 表示可以转授，即被授权者可以把这些权限继续授予给其他用户或角色，缺省不能转授；
4. 不支持角色的循环转授，如将 BOOKSHOP\_ROLE1 授予 BOOKSHOP\_ROLE2，BOOKSHOP\_ROLE2 不能再授予 BOOKSHOP\_ROLE1；
5. 支持对系统角色授权系统权限。但是不支持再为 PUBLIC 系统角色授予在 dminit 初始化时已经被授予的系统权限（INSERT TABLE、UPDATE TABLE、DELETE TABLE、SELECT TABLE、DUMP TABLE、REFERENCE TABLE、GRANT TABLE、INSERT VIEW、UPDATE VIEW、DELETE VIEW、SELECT VIEW、GRANT VIEW、EXECUTE PROCEDURE、GRANT PROCEDURE、SELECT SEQUENCE、GRANT SEQUENCE、EXECUTE PACKAGE、GRANT PACKAGE、SELECT MATERIALIZED VIEW、GRANT DOMAIN、USAGE DOMAIN），也不支持为 PUBLIC 角色授予 SVI 角色。不支持为 DBA 角色授予 VTI 角色。

例 假设存在角色 BOOKSHOP\_ROLE1，角色 BOOKSHOP\_ROLE2，用户 BOOKSHOP\_USER1。

```
//让用户BOOKSHOP_USER1继承角色BOOKSHOP_ROLE1的权限
GRANT BOOKSHOP_ROLE1 TO BOOKSHOP_USER1;

//让角色BOOKSHOP_ROLE2继承角色BOOKSHOP_ROLE1的权限
GRANT BOOKSHOP_ROLE1 TO BOOKSHOP_ROLE2;
```

#### 3.3.3.2 角色权限的回收

可以使用 REVOKE 语句回收用户或其它角色从指定角色继承过来的权限。

回收角色权限的语句语法为：

```
REVOKE [ADMIN OPTION FOR] <角色名>{,<角色名>} FROM <角色名或用户名>;
<角色名或用户名> ::= <用户名> | <角色名>
```

**使用说明：**

1. 权限回收者必须是具有回收相应角色以及转授权的用户。对于角色授权时使用 WITH ADMIN OPTION 先给用户 1 授权，然后又转授用户 2 的情况，回收用户 1 的角色时不会级联回收用户 2 的角色；
2. 使用 ADMIN OPTION FOR 选项的目的是收回用户或角色权限转授的权利，而不回收用户或角色的权限；
3. 支持对系统角色回收系统权限。但是不支持回收 PUBLIC 系统角色中在 dminit 初始化时已经被授予的系统权限，也不支持回收 PUBLIC 角色的 SVI 角色。不支持回收 DBA 角色的 VTI 角色。

例 接 3.3.3.1 节的例子，回收用户 BOOKSHOP\_USER1 和角色 BOOKSHOP\_ROLE2 的 BOOKSHOP\_ROLE1 角色。不支持回收 DBA 角色的 VTI 角色。

```
REVOKE BOOKSHOP_ROLE1 FROM BOOKSHOP_USER1;
REVOKE BOOKSHOP_ROLE1 FROM BOOKSHOP_ROLE2;
```

### 3.3.4 模式权限的分配与回收

模式权限是模式级别的对象权限，又称为模式级别对象的 ANY 特权。

若要使用模式权限的分配与回收功能，须先开启 INI 参数 GRANT\_SCHEMA=1 或 2。

#### 3.3.4.1 模式权限的分配

为用户赋予模式级别的对象 ANY 特权后，该用户拥有对该模式用户下该类对象的 ANY 特权。

模式级别对象的 ANY 特权授予语法如下：

```
GRANT <模式权限> ON SCHEMA <模式> TO <用户或角色>{,<用户或角色>} [WITH ADMIN OPTION];
<模式权限>::=ALL [PRIVILEGES] | <ANY特权>
<ANY特权>::= SELECT ANY TABLE |
INSERT ANY TABLE |
UPDATE ANY TABLE | 
DELETE ANY TABLE | 
REFERENCES ANY TABLE |
DUMP ANY TABLE |
FLASHBACK ANY TABLE
CREATE ANY TABLE |
ALTER ANY TABLE |
DROP ANY TABLE |
SELECT ANY VIEW |  
INSERT ANY VIEW |
UPDATE ANY VIEW | 
DELETE ANY VIEW |
CREATE ANY VIEW |
ALTER ANY VIEW |
DROP ANY VIEW |
SELECT ANY MATERIALIZED VIEW |
CREATE ANY MATERIALIZED VIEW |
ALTER ANY MATERIALIZED VIEW |
DROP ANY MATERIALIZED VIEW |
CREATE ANY INDEX |
ALTER ANY INDEX |
DROP ANY INDEX |
CREATE ANY CONTEXT INDEX |
ALTER ANY CONTEXT INDEX |
DROP ANY CONTEXT INDEX |
SELECT ANY SEQUENCE | 
CREATE ANY SEQUENCE |
ALTER ANY SEQUENCE |
DROP ANY SEQUENCE |
EXECUTE ANY PROCEDURE |
CREATE ANY PROCEDURE |
DROP ANY PROCEDURE |
EXECUTE ANY PACKAGE | 
CREATE ANY PACKAGE |
DROP ANY PACKAGE |
USAGE ANY DOMAIN |
CREATE ANY DOMAIN |
DROP ANY DOMAIN |
CREATE ANY TRIGGER |
ALTER ANY TRIGGER |
DROP ANY TRIGGER |
CREATE ANY SYNONYM |
DROP ANY SYNONYM
<用户名或角色名> ::= <用户名> | <角色名>
```

**使用说明：**

1. 授权者必须是具有对应对象权限以及其转授权的用户；
2. 授权用户需要具有对授权模式的"GRANT ANY OBJECT PRIVILEGE"权限；
3. 设置 INI 参数 GRANT\_SCHEMA=2 时，ALL 或 ALL PRIVILEGES 表示将指定模式的上述所有 ANY 特权都授予被授予者;
4. WITH ADMIN OPTION 表示可以转授，即被授权者可以把这些权限继续授予给其他用户或角色，缺省不能转授。

例 1 通过 SCHEMA 级别授权，将用户 USER227 查询任何表的权限给到新的用户 USER228。

```
--新建用户USER227
CREATE USER USER227 IDENTIFIED BY Dmsys_123;
GRANT "PUBLIC","RESOURCE","SOI","SVI","VTI" TO USER227;
--新建另外一个新的用户USER228
CREATE USER USER228 IDENTIFIED BY Dmsys_456;
GRANT "PUBLIC","RESOURCE","SOI","SVI","VTI" TO USER228;
--通过SCHEMA级别授权，将用户USER227查询任何表的权限给到新的用户USER228。
GRANT SELECT ANY TABLE ON SCHEMA USER227 TO USER228;
--登录USER227用户创建表
CREATE TABLE TEST1(C1 INT);
INSERT INTO TEST1 VALUES(1);
COMMIT;
--登录USER228用户查询到user227上的表
SELECT * FROM USER227.TEST1;
```

#### 3.3.4.2 模式权限的回收

可以使用 REVOKE 语句回收授出的指定模式级别对象的 ANY 特权。

模式级别对象 ANY 特权的回收语句语法为：

```
REVOKE [GRANT ADMIN FOR] <模式权限> ON SCHEMA <模式名> FROM <用户或角色> {,<用户或角色>} [<回收选项>];
<模式权限>::=ALL [PRIVILEGES] | <ANY特权>
<ANY特权>::= SELECT ANY TABLE |
INSERT ANY TABLE |
UPDATE ANY TABLE | 
DELETE ANY TABLE | 
REFERENCES ANY TABLE |
DUMP ANY TABLE |
FLASHBACK ANY TABLE
CREATE ANY TABLE |
ALTER ANY TABLE |
DROP ANY TABLE |
SELECT ANY VIEW |  
INSERT ANY VIEW |
UPDATE ANY VIEW | 
DELETE ANY VIEW |
CREATE ANY VIEW |
ALTER ANY VIEW |
DROP ANY VIEW |
SELECT ANY MATERIALIZED VIEW |
CREATE ANY MATERIALIZED VIEW |
ALTER ANY MATERIALIZED VIEW |
DROP ANY MATERIALIZED VIEW |
CREATE ANY INDEX |
ALTER ANY INDEX |
DROP ANY INDEX |
CREATE ANY CONTEXT INDEX |
ALTER ANY CONTEXT INDEX |
DROP ANY CONTEXT INDEX |
SELECT ANY SEQUENCE | 
CREATE ANY SEQUENCE |
ALTER ANY SEQUENCE |
DROP ANY SEQUENCE |
EXECUTE ANY PROCEDURE |
CREATE ANY PROCEDURE |
DROP ANY PROCEDURE |
EXECUTE ANY PACKAGE | 
CREATE ANY PACKAGE |
DROP ANY PACKAGE |
USAGE ANY DOMAIN |
CREATE ANY DOMAIN |
DROP ANY DOMAIN |
CREATE ANY TRIGGER |
ALTER ANY TRIGGER |
DROP ANY TRIGGER |
CREATE ANY SYNONYM |
DROP ANY SYNONYM
<用户名或角色名> ::= <用户名> | <角色名>
<回收选项> ::= RESTRICT | CASCADE
```

**使用说明：**

1. 权限回收者必须是具有回收相应角色以及转授权的用户；
2. 使用 ADMIN OPTION FOR 选项的目的是收回用户或角色权限转授的权利，而不回收用户或角色的权限；
3. 设置 INI 参数 GRANT\_SCHEMA=2 时，ALL 或 ALL PRIVILEGES 表示将指定模式的上述所有 ANY 特权都授予被授予者;
4. < 回收选项 > 分为 CASCADE 和 RESTRICT。不同的回收选项，其意义不同。具体如下：
- CASCADE 表示级联回收，可回收授予时带或不带 WITH ADMIN OPTION 的权限，若带 WITH ADMIN OPTION 还会引起级联回收。利用此选项时不会检查权限是否存在依赖等限制。另外，利用此选项进行级联回收时，若被回收对象上存在另一条路径授予同样权限给该对象时，则仅需回收当前权限。
- RESTRICT 表示限制回收，只能回收授予时不带 WITH ADMIN OPTION 的权限。无法回收授予时带 WITH ADMIN OPTION 的权限，也无法回收存在依赖等限制的权限（如角色上的某权限被别的用户用于创建视图等）。
- 缺省 < 回收选项 >，表示无法回收授予时带 WITH ADMIN OPTION 的权限，但也不会检查要回收的权限是否存在依赖等限制。

例 1 接 3.3.4.1 节例 1，SYSDBA 从用户 USER228 处回收其授出的 SELECT ANY TABLE 权限。

```
REVOKE SELECT ANY TABLE ON SCHEMA USER227 FROM USER228 CASCADE;
```