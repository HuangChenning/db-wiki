---
title: "3.数据访问控制"
book: "HGDB 安全管理手册"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/data_access.html"
tags:
  - highgo
  - highgo-v45
  - develop-security-management
---

## 3\. 数据访问控制

在数据库系统中，对数据的访问控制分为自主访问控制和强制访问控制。自主访问控制的权限往往由数据库对象的所有者进行授权，用户获得某项权限即可执行相应的操作。强制访问控制则主要由安全标记和安全规则限制用户对数据库对象进行某项操作，用户的一切操作必须符合安全规则，否则即便用户是该数据所有者也无法进行操作。

## 3.1. 自主访问控制

一个对象被创建，就会被分配一个所有者。所有者通常是执行创建语句的角色。对于大多数对象，默认只有其所有者才能够对其执行任何操作。其他角色要操作它，必须分配相应的权限。

### 3.1.1. 权限介绍

数据库中可分配的有效权限有：SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES、TRIGGER、CREATE、CONNECT、TEMPORARY、EXECUTE、USAGE、ALL，详细信息请如下。

- **SELECT：** 查询权限。允许 SELECT 命令查询列、表、视图、物化视图、或其他类似表格的对象，允许使用 COPY TO 命令，UPDATE 或 DELETE操作现有的列也需要这个权限。这个权限还允许序列使用currval 函数，允许大对象读取对象。
- **INSERT：** 插入权限。允许INSERT 命令向表、视图等对象中插入数据。可以在特定列上授予，在这种情况下INSERT命令可以在特定的列插入数据（其他列将采用默认值）。此权限还允许使用COPY FROM。
- **UPDATE：** 更新权限。允许 UPDATE 命令更新列、表、视图等。 (需要SELECT权限引用表列，来确定要更新的行，或计算列的新值。) 允许使用序列使用 nextval 和 setval 函数，允许大对象写入或截断。SELECT … FOR UPDATE和SELECT … FOR SHARE命令除了需要SELECT权限外，还需要至少一列上有这个权限。
- **DELETE：** 删除权限。允许 DELETE 命令从表、视图等对象中删除行。(需要SELECT权限引用表列来确定要删除的行。)
- **TRUNCATE：** 截断/清空权限。允许 TRUNCATE 命令清空在表、视图等。
- **REFERENCES：** 引用外部对象权限。允许创建引用表或表的特定列的外键约束。
- **TRIGGE：** 触发器权限。允许在表、视图等对象上创建触发器。
- **CREATE：** 创建对象权限。允许在数据库、模式、表空间中创建对象。
	- 对于数据库，允许在数据库中创建新的模式和发布，并允许在数据库中安装受信任的扩展。
		- 对于模式，允许在模式中创建新对象。要重命名现有对象，你必须拥有对象 and所包含模式的此权限。
		- 对于表空间，允许在表空间中创建表、索引和临时文件，并允许创建将表空间作为默认表空间的数据库。（注意，撤销此特权不会更改已有对象的位置。）
- **CONNECT：** 连接权限。允许访问者连接到数据库。此权限在连接启动时进行检查(同时受pg\_hba.conf 配置文件中的参数限制).
- **TEMPORARY：** 临时表权限。允许在使用数据库时创建临时表。
- **EXECUTE：** 函数、过程权限。允许调用函数或过程，包括使用在函数之上实现的任何运算符。这是适用于函数和过程的唯一权限类型。
- **USAGE：** 模式连接权限。允许连接到模式中，对模式下所有对象的操作，均需要此权限。
	- 对于程序语言，允许使用语言来创建该语言的函数。 这是适用于过程语言的唯一权限类型。
		- 对于模式，允许访问模式中包含的对象（假设对象自己的权限要求也已得到满足）。 从本质上讲，这允许受让者“look up”模式中的对象。如果没有此权限，仍可以看到对象名称，例如通过查询系统目录。 此外，在撤消此权限后，现有会话可能还具有以前执行过此查找的语句，因此这不是阻止对象访问的彻底安全的方法。
		- 对于序列, 允许使用currval 和 nextval 函数.
		- 对于类型和域，允许在创建表、函数和其他模式对象时使用类型或域。 （注意，此权限不控制类型的全部 “usage” ，例如查询中出现的类型的值。 它仅防止创建依赖于类型的对象。 此权限的主要目的是控制哪些用户可以对类型创建依赖项，这可能会防止所有者以后更改类型。 ）
		- 对于外部数据包装器，允许使用外部数据包装器创建新服务器。
		- 对于外部服务器，允许使用服务器创建外部表。受让者还可以创建、更改或删除与该服务器关联的自己的用户映射。
- **ALL:** 所有权限。允许对象的类型可用的所有操作。

其他命令所需的权限罗列在相应命令的参考页上。

下表显示了ACL（访问控制列表）值中用于这些权限类型的单字母缩写。你将在下面列出的 psql 命令的输出中，或者在查看系统目录的 ACL 列时看到这些字母。

表 3.1 ACL权限及字母缩写列表

| **权限** | **缩写** | **适用对象类型** |
| --- | --- | --- |
| SELECT | r(“读”) | LARGE OBJECT,SEQUENCE,TABLE(and table-like objects), table column |
| INSERT | a(“增补”) | TABLE, table column |
| UPDATE | w(“写”) | LARGE OBJECT,SEQUENCE,TABLE, table column |
| DELETE | d | TABLE |
| TRUNCATE | D | TABLE |
| REFERENCES | x | TABLE, table column |
| TRIGGER | t | TABLE |
| CREATE | C | DATABASE,SCHEMA,TABLESPACE |
| CONNECT | c | DATABASE |
| TEMPORARY | T | DATABASE |
| EXECUTE | X | FUNCTION,PROCEDURE |
| USAGE | U | DOMAIN,FOREIGN DATA WRAPPER,FOREIGN SERVER,LANGUAGE,SCHEMA,SEQUENCE,TYPE |

下表使用上面所示的缩写总结了每种类型 SQL 对象可用的权限.它还显示可用于检查每种对象类型的特权设置的psql命令。

表 3.2 对象权限列表

| **对象类型** | **所有权限** | **默认PUBLIC权限** | **psql命令** |
| --- | --- | --- | --- |
| DATABASE | CTc | Tc | \\l |
| DOMAIN | U | U | \\dD+ |
| FUNCTION or PROCEDURE | X | X | \\df+ |
| FOREIGN DATA WRAPPER | U | none | \\dew+ |
| FOREIGN SERVER | U | none | \\des+ |
| LANGUAGE | U | U | \\dL+ |
| LARGE OBJECT | rw | none |  |
| SCHEMA | UC | none | \\dn+ |
| SEQUENCE | rwU | none | \\dp |
| TABLE(and table-like objects) | arwdDxt | none | \\dp |
| Table column | arwx | none | \\dp |
| TABLESPACE | C | none | \\db+ |
| TYPE | U | U | \\dT+ |

已授予特定对象的权限显示为aclitem项的列表，其中每个aclitem项描述了特定授予者授予给一个被授与者的权限。例如，calvin=r\*w/hobbes 指明角色calvin具有SELECT（r）权限和授予选项（\*）以及不可授予权限UPDATE（w），均由角色hobbes授予。如果calvin对由其他授予人授予的同一对象也具有一些权限，那将显示为单独的aclitem条目。aclitem 中的空受赠方字段代表PUBLIC。

例如，假设用户miriam创建了表mytable并且:

```sql
GRANT SELECT ON mytable TO PUBLIC;
GRANT SELECT, UPDATE, INSERT ON mytable TO admin;
GRANT SELECT (col1), UPDATE (col1) ON mytable TO miriam_rw;
```

则 psql的 \\dp 命令将显示:

```sql
=> \dp mytable
                            Access privileges
 Schema |  Name   | Type  |   Access privileges   |   Column privileges   | Policies
-−-−-−-−+-−-−-−-−-+-−-−-−-+-−-−-−-−-−-−-−-−-−-−-−-+-−-−-−-−-−-−-−-−-−-−-−-+-−-−-−-−-−
 public | mytable | table | miriam=arwdDxt/miriam+| col1:                +|
        |         |       | =r/miriam            +|   miriam_rw=rw/miriam |
        |         |       | admin=arw/miriam      |                       |
row
```

如果“Access privileges”列对于给定对象为空，则表示该对象具有默认权限（也就是说，它在相关系统目录中的权限条目为空）。默认权限始终包含所有者的所有权限，并且可以包括 PUBLIC 的一些权限，具体取决于对象类型，如上所述。对象上的第一个GRANT或REVOKE将实例化默认权限（例如，生成miriam\_arwdDxt/miriam），然后根据指定的请求修改它们。类似的，只有具有非默认特权的列的条目才显示在“Column privileges”中。（注意：为此目的，“default privileges”始终表示对象类型的内置缺省权限。其权限受ALTER DEFAULT PRIVILEGES 命令影响的对象将始终显示一个显式权限条目，其中包含 ALTER。）

注意：所有者的隐式授予选项没有在访问权限显示中标记。仅当授予选项被显式授予给某人时才会出现。

### 3.1.2. 访问控制

安全版关闭三权功能（由hg\_sepofpowers参数控制）后其自主访问控制机制与非安全版数据库相同。开启三权功能后，数据库会拥有更加严格的权限控制。下表详细列出了当三权功能开启后，每类用户对不同对象拥有的具体权限。

三权分立版本为v45（hg\_sepv4=v45）的情况下，三个管理员用户和普通用户对数据库对象的权限。

表 3.3 V45三权权限控制

| **操作对象** | **操作名称** | **SYSDBA** | **SYSSSO** | **SYSSAO** | **普通用户** |
| --- | --- | --- | --- | --- | --- |
| **表空间** | 创建表空间 | 只能创建属主为自己的表空间，带owner 属性创建时除owner sysdba外均创建失败，报错为：permission denied（表空间的属主只能是sysdba） | 无权限 | 无权限 | 无权限 |
|  | 修改表空间属性 | 不能修改表空间属主为其他用户，若修改属主为sysdba外的用户，则修改失败，报错为：The owner of the tablespace can only be sysdba（表空间的属主只能是sysdba） | 无权限 | 无权限 | 无权限 |
|  | 表空间权限赋权及回收 | 不能赋权给其他管理员用户，可以赋权给自己及普通用户；   不能将with grant option属性给任何用户 | 无权限 | 无权限 | 无权限 |
|  | 删除表空间 | 对所有表空间有删除权限 | 无权限 | 无权限 | 无权限 |
| **数据库** | 创建数据库 | 只能创建属主为自己的数据库，带owner 属性创建时除owner sysdba外均创建失败，报错为：The owner of the database can only be sysdba（数据库的属主只能是sysdba） | 无权限 | 无权限 | 无权限 |
|  | 修改数据库属性 | 不能修改数据库属主为其他用户，若修改属主为sysdba外的用户，则修改失败，报错为：The owner of the database can only be sysdba（数据库的属主只能是sysdba） | 无权限 | 无权限 | 无权限 |
|  | 数据库权限赋权及回收 | 不能将create/temporary/temp权限赋权给syssso和syssao用户；   不能将with grant option属性给任何用户 | 无权限 | 无权限 | 无权限 |
|  | 删除数据库 | 对所有数据库有删除权限 | 无权限 | 无权限 | 无权限 |
| **模式** | 创建模式 | 只可创建属主为自己或属主为普通用户的模式 | 无权限 | 无权限 | 赋权数据库权限后只可创建属主为自己的模式 |
|  | 修改模式属性 | 只可修改属主为自己的模式的属性（如：rename to /owner to），可以将属主修改为自己及普通用户，但是不可以修改为其他管理员用户 | 无权限 | 无权限 | 赋权数据库权限后只可修改属主为自己的模式的属性，且只可修改属主为自己的用户组成员，不可以将属主修改为管理员用户或其他普通用户 |
|  | 模式权限赋权及回收 | 不能将属主为自己的模式的权限赋权给sysdba外的任何用户，对于属主非自己的模式无权限 | 可以将普通用户模式的权限赋权给自己及其他普通用户 | 无权限 | 只可将属主为自己的模式的权限授予自己及其他普通用户，不能授予管理员用户，对于属主非自己的模式无权限 |
|  | 使用模式 | 只可使用属主为自己的模式及public模式 | 只可使用属主为自己的模式及有限访问public模式 | 只可使用属主为自己的模式及有限访问public模式 | 只可使用属主为自己的和已授权的模式及public模式 |
|  | 删除模式 | 只可删除属主为自己的模式（public模式不可删除） | 无权限 | 无权限 | 只可删除属主为自己的模式，有其他用户创建的对象时可使用级联删除 |
| **用户或角色** | 创建用户或角色 | 1.不带属性（除password属性）创建用户时可创建成功，创建角色时不带password属性可创建成功   2.创建用户或角色时，若带有superuser、createdb、createrole属性，则创建失败，报错为：can’t create with superuser/createdb/createrole   3.创建用户时，若带有replication属性，可创建成功   4.三个管理员用户的权限不可以通过继承属性赋予其他用户，也不可继承其他用户的权限 | 无权限 | 无权限 | 无权限 |
|  | 修改用户或角色属性 | 1.修改用户属性时，若带有superuser、createdb、createrole属性，则修改失败，报错为permission denied   2.可对其他用户进行重命名，不可对sysdba、syssso、syssao三个管理员用户进行重命名   3.不可修改其他用户的密码及有效期，也不可修改自己的密码有效期 | 除安全版特殊要求（syssso可以修改用户的密码、有效期）外，均无权限 | 无权限 | 无权限 |
|  | 删除用户或角色 | 1.可删除普通用户   2.不能通过drop命令删除sysdba、syssso、syssao三个管理员用户 | 无权限 | 无权限 | 无权限 |
| **表** | 创建表 | 只可在自建模式和public模式下创建表 | 无权限 | 无权限 | 只可在自建模式、已授权的模式和public模式下创建表 |
|  | 查询及使用表 | 只可查询、使用属主为自己的表以及安全功能中特殊要求的表 | 可以查询、使用属主为自己的表以及安全功能中特殊要求的表 | 可以查询、使用属主为自己的表以及安全功能中特殊要求的表 | 可以查询、使用自己创建的及已授权的表以及安全功能中特殊要求的表 |
|  | 修改表属性 | 只可修改自己创建的表的属性，不可将自己的表的属主修改为自己外的其他用户 | 无权限 | 无权限 | 只可修改自己创建的表的属性，不可将自己的表的属主修改为自己外的其他用户 |
|  | 表权限赋权及回收 | 自己的表不能赋权给自己外的其他用户，其他用户的表也不能赋权给sysdba | 赋权模式的权限后可以将普通用户自建模式下的表赋权给其他普通用户 | 无权限 | 只可将属主为自己的表赋权给自己及其他普通用户，但不可以赋权给管理员用户 |
|  | 删除表 | 只可删除属主为自己的表 | 无权限 | 无权限 | 只可删除属主为自己的表 |
| **索引** | 创建索引 | 只可在自建表上创建索引 | 无权限 | 无权限 | 只可在自建表上创建索引 |
|  | 修改索引 | 只可修改自己创建的索引 | 无权限 | 无权限 | 只可修改自己创建的索引 |
|  | 删除索引 | 只可删除自己创建的索引 | 无权限 | 无权限 | 只可删除自己创建的索引 |
| **函数** | 创建函数 | 只可在自建模式和public模式下创建函数 | 无权限 | 无权限 | 只可在自建模式、已授权的模式及public模式下创建函数 |
|  | 修改函数属性 | 只可修改属主为自己的函数的属性（如：rename to/set schema/depends on extension），owner to属性只可修改为sysdba，若修改owner to属性为sysdba以外的用户，则提示permission denied | 无权限 | 无权限 | 只可修改属主为自己的函数的属性，但owner to属性不可修改，若修改owner to属性为除本用户之外的用户，则提示You can‘t change the owner（不能改变属主） |
|  | 函数权限赋权及回收 | 不可以将属主为自己的函数的权限赋予自己外的其他用户，也不可将其他用户创建的函数权限赋权给sysdba | 赋权模式的权限后可以将普通用户自建模式下的函数赋权给其他普通用户 | 无权限 | 只可将属主为自己的函数的权限赋予自己及其他普通用户，不能赋权给管理员用户 |
|  | 调用函数 | 只可调用属主为自己的函数 | 只可调用public模式下sysdba的函数和属主为自己的函数 | 只可调用public模式下sysdba的函数和属主为自己的函数 | 只可调用属主为自己的函数和已授权的函数及public模式下sysdba的函数 |
|  | 删除函数 | 只可删除属主为自己的函数 | 无权限 | 无权限 | 只可删除属主为自己的函数 |
| **存储过程** | 创建存储过程 | 只可在自建模式和public模式下创建存储过程 | 无权限 | 无权限 | 只可在自建模式和public模式下创建存储过程 |
|  | 修改存储过程属性 | 只可修改属主为自己的存储过程的属性（如：rename to/set schema/depends on extension），owner to属性只可修改为sysdba，若修改owner to属性为sysdba以外的用户，则提示permission denied | 无权限 | 无权限 | 只可修改属主为自己的函数的属性，但owner to属性不可修改，若修改owner to属性为除本用户之外的用户，则提示You can‘t change the owner（不能改变属主） |
|  | 存储过程权限赋权及回收 | 不可以将属主为自己的存储过程的权限赋予任何其他用户，也不可将其他用户创建的存储过程权限赋权给sysdba | 赋权模式的权限后可以将普通用户自建模式下的存储过程赋权给其他普通用户 | 无权限 | 只可将自己创建的存储过程的权限赋权给其他普通用户，不能赋权给管理员用户 |
|  | 调用存储过程 | 只可调用属主为自己的存储过程 | 只可调用public模式下sysdba的存储过程和属主为自己的存储过程 | 只可调用public模式下sysdba的存储过程和属主为自己的存储过程 | 只可调用属主为自己的存储过程和已授权的存储过程及public模式下sysdba的存储过程 |
|  | 删除存储过程 | 只可删除属主为自己的存储过程 | 无权限 | 无权限 | 只可删除属主为自己的存储过程 |
| **序列** | 创建序列 | 只可在自建模式和public模式下创建序列 | 无权限 | 无权限 | 只可在自建模式、已授权的模式及public模式下创建序列 |
|  | 修改序列属性 | 只可修改属主为自己的序列的属性（如：rename to/owner to/set schema/），属主不能修改为自己外的其他用户 | 无权限 | 无权限 | 只可修改属主为自己的序列的属性（如：rename to/owner to/set schema/），属主不能修改为自己外的其他用户 |
|  | 序列权限赋权及回收 | 不可以将自己创建的序列的权限赋予自己外的其他用户，也不可将其他用户创建的序列权限赋权给sysdba | 赋权模式的权限后可以将普通用户自建模式下的序列赋权给其他普通用户 | 无权限 | 只可将自己创建的序列的权限赋权给自己及其他普通用户，不能赋权给管理员用户 |
|  | 使用及查询序列 | 只可使用及查询属主为自己的序列 | 无权限 | 无权限 | 只能使用及查询属主为自己及已授权的序列 |
|  | 删除序列 | 只可删除属主为自己的序列 | 无权限 | 无权限 | 只可删除属主为自己的序列 |
| **视图** | 创建视图 | 只可在自建表上创建视图 | 无权限 | 无权限 | 只可在有增删改查权限的表上创建视图 |
|  | 修改视图属性 | 只可修改属主为自己的视图的属性，属主可以修改为自己，不能修改为其他管理员及普通用户 | 无权限 | 无权限 | 只可修改属主为自己的用户组成员，不可以将属主修改为管理员用户或其他普通用户 |
|  | 删除视图 | 只可删除属主为自己的视图 | 无权限 | 无权限 | 只可删除属主为自己的视图 |
| **导入导出** | copy | 只可导入数据到本用户对象，只可导出本用户数据 | 无权限 | 无权限 | 无权限 |
|  | \\copy | 只可导入数据到本用户对象，只可导出本用户数据 | 无权限 | 无权限 | 只可导入数据到本用户对象，只可导出本用户数据及已授权的数据 |
| **安全策略** | 安全策略配置 | 无权限 | 可进行安全策略参数设置 | 无权限 | 无权限 |
|  | 安全策略查询 | 无权限 | 可查询安全策略参数值 | 无权限 | 无权限 |
| **安全标记** | 安全标记设置 | 无权限 | 只可对普通用户的安全标记值进行设置及修改 | 无权限 | 无权限 |
|  | 安全标记查询 | 可查询自己创建的表的安全标记值及行安全标记值 | 可查询所有用户、表、行的安全标记值 | 无权限 | 可查询可支配的（根据强访规则确定）行安全标记值 |
| **审计** | 审计策略配置 | 无权限 | 无权限 | 可进行审计策略参数设置 | 无权限 |
|  | 审计策略查询 | 无权限 | 无权限 | 可查询审计策略参数值 | 无权限 |
|  | 审计操作 | 无权限 | 无权限 | 可审计数据库及用户的操作 | 无权限 |
| **备份恢复** | 包括pg\_dumpall/   pg\_dump/pg\_restore/   （pg\_basebackup   /hg\_rman后续版本考虑） | 可以备份恢复所有数据（备份前需进行数据加密，确保对于其他用户的数据无权查看） | 可以备份恢复属主为自己的对象 | 可以备份恢复属主为自己的对象 | 具有备份恢复用户本身数据的权限 |

三权分立是v4（hg\_sepv4=v4）的情况下，三个管理员用户和普通用户对数据库对象的权限。

表 3.4 V4三权权限控制

| **操作对象** | **操作名称** | **SYSDBA** | **SYSSSO** | **SYSSAO** | **普通用户** |
| --- | --- | --- | --- | --- | --- |
| **用户或角色** | 创建用户或角色 | 1.不带属性（除password属性）创建用户时可创建成功，创建角色时不带password属性可创建成功   2.创建用户或角色时，若带有superuser、createdb、createrole属性，则创建失败。   3.创建用户时，若带有replication属性，可创建成功 | 无权限 | 无权限 | 无权限 |
|  | 修改用户或角色属性 | 1.修改用户属性时，若带有superuser、createdb、createrole属性，则修改失败，报错为permission denied   2.可对其他用户进行重命名，不可对sysdba、syssso、syssao三个管理员用户进行重命名   3.不可修改其他用户的密码及有效期，也不可修改自己的密码有效期 | syssso可以修改用户的密码、有效期 | 无权限 | 无权限 |
|  | 删除用户或角色 | 1.可删除普通用户   2.不能通过drop命令删除sysdba、syssso、syssao三个管理员用户 | 无权限 | 无权限 | 无权限 |
| **表** | 创建表 | 可在有权限的schema下创建表 | 无权限 | 无权限 | 只可在自建模式、已授权的模式和public模式下创建表 |
|  | 查询及使用表 | 只可查询、使用属主为自己的表以及安全功能中特殊要求的表 | 可以查询、使用属主为自己的表以及安全功能中特殊要求的表 | 可以查询、使用属主为自己的表以及安全功能中特殊要求的表 | 可以查询、使用自己创建的及已授权的表以及安全功能中特殊要求的表 |
|  | 表权限赋权及回收 | 自己的表不能赋权给自己外的其他用户，其他用户的表也不能赋权给sysdba | 可以将普通用户的表赋权给其他普通用户 | 无权限 | 只可将属主为自己的表赋权给自己及其他普通用户，但不可以赋权给管理员用户 |
| **安全策略** | 安全策略配置 | 无权限 | 可进行安全策略参数设置 | 无权限 | 无权限 |
|  | 安全策略查询 | 无权限 | 可查询安全策略参数值 | 无权限 | 无权限 |
| **安全标记** | 安全标记设置 | 无权限 | 只可对普通用户的安全标记值进行设置及修改 | 无权限 | 无权限 |
|  | 安全标记查询 | 可查询自己创建的表的安全标记值及行安全标记值 | 可查询所有用户、表、行的安全标记值 | 无权限 | 可查询可支配的（根据强访规则确定）行安全标记值 |
| **审计** | 审计策略配置 | 无权限 | 无权限 | 可进行审计策略参数设置 | 无权限 |
|  | 审计策略查询 | 无权限 | 无权限 | 可查询审计策略参数值 | 无权限 |
|  | 审计操作 | 无权限 | 无权限 | 可审计数据库及用户的操作 | 无权限 |
| **备份恢复** | 包括pg\_dumpall/   pg\_dump/pg\_restore/   （pg\_basebackup   /hg\_rman后续版本考虑） | 可以备份恢复所有数据（备份前需进行数据加密，确保对于其他用户的数据无权查看） | 无权限 | 无权限 | 具有备份恢复用户本身数据的权限 |

### 3.1.3. 权限管理

要分配权限，可以使用GRANT命令。例如，如果joe是一个已有角色，而accounts是一个已有表，更新该表的权限可以按如下方式授权：

> GRANT UPDATE ON accounts TO joe;

用ALL取代特定权限会把与对象类型相关的所有权限全部授权。

> GRANT ALL ON accounts TO joe;

一个特殊的名为PUBLIC的“角色”可以用来向系统中的每一个角色授予一个权限。同时，在数据库中有很多用户时可以设置“组”角色来帮助管理权限。

为了撤销一个权限，使用REVOKE 命令：

> REVOKE ALL ON accounts FROM PUBLIC;

对象拥有者的特殊权限（即执行DROP、GRANT、REVOKE等的权力）总是隐式地属于拥有者，并且不能被授予或撤销。但是对象拥有者可以选择撤销他们自己的普通权限，例如把一个表变得对他们自己和其他人只读。

> REVOKE ALL ON accounts from joe;
> 
> GRANT SELECT ON accounts TO joe;

可以在授予权限时使用“with grant option”来允许接收人将权限转授给其他人。如果后来授予选项被撤销，则所有从接收人那里获得的权限（直接或者通过授权链获得）都将被撤销。

> GRANT SELECT ON accounts TO joe with grant option;

在创建对象时，系统默认将某些类型对象的权限授予PUBLIC。 默认情况下，在表、表列、序列、外部数据包装器、外部服务器、大型对象、模式或表空间上，不向PUBLIC授予权限。 对于其他类型的对象，授予 PUBLIC的默认权限如下所示： 针对数据库的CONNECT和TEMPORARY（创建临时表）权限; 针对函数和程序的EXECUTE权限;以及针对语言和数据类型（包括域）的USAGE权限。当然，对象所有者可以REVOKE默认权限和特别授予的权限。 （为了最大程度的安全性，在创建对象的同一事务中发出REVOKE;那么就没有其他用户能够使用该对象的窗口。） 此外，可以使用ALTER DEFAULT PRIVILEGES命令取代这些默认权限设置。

## 3.2. 行级安全控制

除可以通过GRANT使用 SQL 标准的特权系统之外，表还可以具有行安全性策略，它针对每一个用户限制哪些行可以被普通的查询返回或者可以被数据修改命令插入、更新或删除。

这种特性也被称为行级安全性。默认情况下，表不具有任何策略，这样用户根据 SQL 特权系统具有对表的访问特权，对于查询或更新来说其中所有的行都是平等的。

当在一个表上启用行安全性时（使用ALTER TABLE … ENABLE ROW LEVEL SECURITY），所有对该表选择行或者修改行的普通访问都必须被一条行安全性策略所允许（不过，表的拥有者通常不服从行安全性策略）。如果表上不存在策略，将使用一条默认的否定策略，即所有的行都不可见或者不能被修改。应用在整个表上的操作不服从行安全性，例如TRUNCATE和 REFERENCES。

行安全性策略可以针对特定的命令、角色或者两者。一条策略可以被指定为适用于ALL命令，或者SELECT、 INSERT、UPDATE、或者DELETE。可以为一条给定策略分配多个角色，并且通常的角色成员关系和继承规则也适用。

要指定哪些行根据一条策略是可见的或者是可修改的，需要一个返回布尔结果的表达式。

对于每一行，在计算任何来自用户查询的条件或函数之前，先会计算这个表达式（这条规则的唯一例外是leakproof函数， 它们被保证不会泄露信息，优化器可能会选择在行安全性检查之前应用这类函数）。使该表达式不返回true的行将不会被处理。可以指定独立的表达式来单独控制哪些行可见以及哪些行被允许修改。策略表达式会作为查询的一部分运行并且带有运行该查询的用户的特权，但是安全性定义者函数 可以被用来访问对调用用户不可用的数据。

具有BYPASSRLS属性的超级用户和角色在访问一个表时总是可以绕过行安全性系统。表拥有者通常也能绕过行安全性，不过表拥有者可以选择用ALTER TABLE … FORCE ROW LEVEL SECURITY来服从行安全性。

启用和禁用行安全性以及向表增加策略是只有表所有者拥有该特权。

策略的创建可以使用CREATE POLICY命令，策略的修改可以使用ALTER POLICY命令，而策略的删除可以使用 DROP POLICY命令。要为一个给定表启用或者禁用行安全性，可以使用ALTER TABLE命令。

每一条策略都有名称并且可以为一个表定义多条策略。由于策略是表相关的，一个表的每一条策略都必须有一个唯一的名称。不同的表可以拥有相同名称的策略。

当多条策略适用于一个给定的查询时，会把它们用OR（对宽容性策略，默认的策略类型）或者AND（对限制性策略）组合在一起。这和给定角色拥有它作为成员的所有角色的特权的规则类似。宽容性策略和限制性策略在下文将会进一步讨论。

作为一个简单的例子，如何在account关系上创建一条策略以允许只有managers角色的成员能访问行，并且只能访问它们账户的行：

> CREATE TABLE accounts (manager text, company text, contact\_email  
> text);
> 
> ALTER TABLE accounts ENABLE ROW LEVEL SECURITY;
> 
> CREATE POLICY account\_managers ON accounts TO managers
> 
> USING (manager = current\_user);

上面的策略隐含地提供了一个与其该约束适用于被一个命令选择的行（这样一个经理不能SELECT、UPDATE或者DELETE属于其他经理的已有行）以及被一个命令修改的行（这样属于其他经理的行不能通过INSERT或者UPDATE创建）。

如果没有指定角色或者使用了特殊的用户名PUBLIC， 则该策略适用于系统上所有的用户。

要允许所有用户访问users 表中属于他们自己的行，可以使用一条简单的策略：

> CREATE POLICY user\_policy ON users
> 
> USING (user\_name = current\_user);

这个例子的效果和前一个类似。

为了对增加到表中的行使用与可见行不同的策略，可以组合多条策略。这一对策略将允许所有用户查看users表中的所有行，但只能修改他们自己的行：

> CREATE POLICY user\_sel\_policy ON users
> 
> FOR SELECT
> 
> USING (true);
> 
> CREATE POLICY user\_mod\_policy ON users
> 
> USING (user\_name = current\_user);

在一个SELECT命令中，这两条规则被用OR组合在一起，最终的效应就是所有的行都能被选择。在其他命令类型中，只有第二条策略适用，这样其效果就和以前相同。

也可以用ALTER TABLE命令禁用行安全性。禁用行安全性不会移除定义在表上的任何策略，它们只是被简单地忽略。然后该表中的所有行都是可见的并且可修改，服从于标准的 SQL特权系统。

下面是一个较大的例子，它展示了这种特性如何被用于生产环境。表 passwd模拟了一个Unix 口令文件：

> \-# 简单的口令文件例子
> 
> CREATE TABLE passwd (
> 
> user\_name text UNIQUE NOT NULL,
> 
> pwhash text,
> 
> uid int PRIMARY KEY,
> 
> gid int NOT NULL,
> 
> real\_name text NOT NULL,
> 
> home\_phone text,
> 
> extra\_info text,
> 
> home\_dir text NOT NULL,
> 
> shell text NOT NULL
> 
> );
> 
> CREATE ROLE admin; -# 管理员
> 
> CREATE ROLE bob; -# 普通用户
> 
> CREATE ROLE alice; -# 普通用户
> 
> \-# 填充表
> 
> INSERT INTO passwd VALUES
> 
> (‘admin’,’xxx’,0,0,’Admin’,’111-222-3333’,null,’/root’,’/bin/dash’);
> 
> INSERT INTO passwd VALUES
> 
> (‘bob’,’xxx’,1,1,’Bob’,’123-456-6890’,null,’/home/bob’,’/bin/zsh’);
> 
> INSERT INTO passwd VALUES
> 
> (‘alice’,’xxx’,2,1,’Alice’,’098-665-4321’,null,’/home/alice’,’/bin/zsh’);
> 
> \-# 确保在表上启用行级安全性
> 
> ALTER TABLE passwd ENABLE ROW LEVEL SECURITY;
> 
> \-# 创建策略
> 
> \-# 管理员能看见所有行并且增加任意行
> 
> CREATE POLICY admin\_all ON passwd TO admin USING (true) WITH CHECK  
> (true);
> 
> \-# 普通用户可以看见所有行
> 
> CREATE POLICY all\_view ON passwd FOR SELECT USING (true);
> 
> \-# 普通用户可以更新它们自己的记录，但是限制普通用户可用的 shell
> 
> CREATE POLICY user\_mod ON passwd FOR UPDATE
> 
> USING (current\_user = user\_name)
> 
> WITH CHECK (
> 
> current\_user = user\_name AND
> 
> shell IN (‘/bin/bash’,’/bin/sh’,’/bin/dash’,’/bin/zsh’,’/bin/tcsh’)
> 
> );
> 
> \-# 允许管理员有所有普通权限
> 
> GRANT SELECT, INSERT, UPDATE, DELETE ON passwd TO admin;
> 
> \-# 用户只在公共列上得到选择访问
> 
> GRANT SELECT
> 
> (user\_name, uid, gid, real\_name, home\_phone, extra\_info,  
> home\_dir, shell)
> 
> ON passwd TO public;
> 
> \-# 允许用户更新特定行
> 
> GRANT UPDATE
> 
> (pwhash, real\_name, home\_phone, extra\_info, shell)
> 
> ON passwd TO public;

对于任意安全性设置来说，重要的是测试并确保系统的行为符合预期。使用上述的例子，下面展示了权限系统工作正确：

> \-# admin 可以看到所有的行和域
> 
> highgo=> set role admin;
> 
> SET
> 
> highgo=> table passwd;
> 
> user\_name | pwhash | uid | gid | real\_name | home\_phone |  
> extra\_info |
> 
> home\_dir | shell
> 
> \-#-#-#-#-#-+-#-#-#-#+-#-#-+-#-#-+-#-#-#-#-#-+-#-#-#-#-#-#-#+-#-#-#-#-#-#+-#-#-#-
> 
> #-#-#-+-#-#-#-#-#-
> 
> admin | xxx | 0 | 0 | Admin | 111-222-3333 | | /root
> 
> | /bin/dash
> 
> bob | xxx | 1 | 1 | Bob | 123-456-6890 | | /home/
> 
> bob | /bin/zsh
> 
> alice | xxx | 2 | 1 | Alice | 098-665-4321 | | /home/
> 
> alice | /bin/zsh
> 
> (3 rows)
> 
> \-# 测试 Alice 能做什么
> 
> highgo=> set role alice;
> 
> SET
> 
> highgo=> table passwd;
> 
> ERROR: permission denied for relation passwd
> 
> highgo=> select  
> user\_name,real\_name,home\_phone,extra\_info,home\_dir,shell from
> 
> passwd;
> 
> user\_name | real\_name | home\_phone | extra\_info | home\_dir |  
> shell
> 
> \-#-#-#-#-#-+-#-#-#-#-#-+-#-#-#-#-#-#-#+-#-#-#-#-#-#+-#-#-#-#-#-#-+-#-#-#-#-#-
> 
> admin | Admin | 111-222-3333 | | /root | /bin/dash
> 
> bob | Bob | 123-456-6890 | | /home/bob | /bin/zsh
> 
> alice | Alice | 098-665-4321 | | /home/alice | /bin/zsh
> 
> (3 rows)
> 
> highgo=> update passwd set user\_name = ‘joe’;
> 
> ERROR: permission denied for relation passwd
> 
> \-# Alice 被允许更改她自己的 real\_name，但不能改其他的
> 
> highgo=> update passwd set real\_name = ‘Alice Doe’;
> 
> UPDATE 1
> 
> highgo=> update passwd set real\_name = ‘John Doe’ where user\_name =  
> ‘admin’;
> 
> UPDATE 0
> 
> highgo=> update passwd set shell = ‘/bin/xx’;
> 
> ERROR: new row violates WITH CHECK OPTION for “passwd”
> 
> highgo=> delete from passwd;
> 
> ERROR: permission denied for relation passwd
> 
> highgo=> insert into passwd (user\_name) values (‘xxx’);
> 
> ERROR: permission denied for relation passwd
> 
> \-# Alice 可以更改她自己的口令；行级安全性会悄悄地阻止更新其他行
> 
> highgo=> update passwd set pwhash = ‘abc’;
> 
> UPDATE 1

目前为止所有构建的策略都是宽容性策略，也就是当多条策略都适用时会被 “OR”组合在一起。而宽容性策略可以被用来仅允许在预计情况中对行的访问，这比将宽容性策略与限制性策略（记录必须通过这类策略并且它们会被“AND”组合起来）组合在一起更简单。在上面的例子之上，我们增加一条限制性策略要求通过一个本地Unix套接字连接过来的管理员访问passwd表的记录：

> CREATE POLICY admin\_local\_only ON passwd AS RESTRICTIVE TO admin
> 
> USING (pg\_catalog.inet\_client\_addr() IS NULL);

然后，由于这条限制性规则的存在，我们可以看到从网络连接进来的管理员将无法看到任何记录：

> \=> SELECT current\_user;
> 
> current\_user
> 
> \-#-#-#-#-#-#-#
> 
> admin
> 
> (1 row)
> 
> \=> select inet\_client\_addr();
> 
> inet\_client\_addr
> 
> \-#-#-#-#-#-#-#-#-#
> 
> 126.0.0.1
> 
> (1 row)
> 
> \=> SELECT current\_user;
> 
> current\_user
> 
> \-#-#-#-#-#-#-#
> 
> admin
> 
> (1 row)
> 
> \=> TABLE passwd;
> 
> user\_name | pwhash | uid | gid | real\_name | home\_phone | extra\_info | home\_dir | shell
> 
> \-#-#-#-#-#-+-#-#-#-#+-#-#-+-#-#-+-#-#-#-#-#-+-#-#-#-#-#-#+-#-#-#-#-#-#+-#-#-#-#-#+-#-#-#-
> 
> (0 rows)
> 
> \=> UPDATE passwd set pwhash = NULL;
> 
> UPDATE 0

参照完整性检查（例如唯一或逐渐约束和外键引用）时会绕过行级安全性以保证数据完整性得到维护。

在某些环境中需要确保行安全性被关闭。例如，在做备份时，由于行安全性配置可能导致某些行被从备份中忽略掉，这会是灾难性的。在这类情况下，你可以设置row\_security配置参数为 off。这本身不会绕过行安全性，它所做的是如果任何结果会 被一条策略过滤掉，就会抛出一个错误。然后错误的原因就可以被找到并且修复。

在上面的例子中，策略表达式只考虑了要被访问的行中的当前值。这是最简单并且表现最好的情况。如果需要参考其他行或者其他表来做出策略的决定，可以在策略表达式中通过使用子句SELECT或者包含SELECT的函数来实现。不过要注意这类访问可能会导致争用，在错误的情况下这可能会导致信息泄露。例如，考虑下面的表设计：

> \-# 特权组的定义
> 
> CREATE TABLE groups (group\_id int PRIMARY KEY,
> 
> group\_name text NOT NULL);
> 
> INSERT INTO groups VALUES
> 
> (1, ‘low’),
> 
> (2, ‘medium’),
> 
> (5, ‘high’);
> 
> GRANT ALL ON groups TO alice; -# alice 是管理员
> 
> GRANT SELECT ON groups TO public;
> 
> \-# 用户的特权级别的定义
> 
> CREATE TABLE users (user\_name text PRIMARY KEY,
> 
> group\_id int NOT NULL REFERENCES groups);
> 
> INSERT INTO users VALUES
> 
> (‘alice’, 5),
> 
> (‘bob’, 2),
> 
> (‘mallory’, 2);
> 
> GRANT ALL ON users TO alice;
> 
> GRANT SELECT ON users TO public;
> 
> \-# 保存要被保护的信息的表
> 
> CREATE TABLE information (info text,
> 
> group\_id int NOT NULL REFERENCES groups);
> 
> INSERT INTO information VALUES
> 
> (‘barely secret’, 1),
> 
> (‘slightly secret’, 2),
> 
> (‘very secret’, 5);
> 
> ALTER TABLE information ENABLE ROW LEVEL SECURITY;
> 
> \-# 对于安全性 group\_id 大于等于一行的 group\_id 的用户，
> 
> \-# 这一行应该是可见的/可更新的
> 
> CREATE POLICY fp\_s ON information FOR SELECT
> 
> USING (group\_id <= (SELECT group\_id FROM users WHERE user\_name =
> 
> current\_user));
> 
> CREATE POLICY fp\_u ON information FOR UPDATE
> 
> USING (group\_id <= (SELECT group\_id FROM users WHERE user\_name =
> 
> current\_user));
> 
> \-# 我们只依赖于行级安全性来保护信息表
> 
> GRANT ALL ON information TO public;

现在假设alice希望更改“有一点点秘密” 的信息，但是觉得mallory不应该看到该行中的新内容，因此她这样做：

> BEGIN;
> 
> UPDATE users SET group\_id = 1 WHERE user\_name = ‘mallory’;
> 
> UPDATE information SET info = ‘secret from mallory’ WHERE group\_id = 2;
> 
> COMMIT;

这看起来是安全的，没有窗口可供mallory看到 “对 mallory 保密”的字符串。不过，这里有一种竞争条件。如果mallory正在并行地做：

> SELECT \* FROM information WHERE group\_id = 2 FOR UPDATE;

并且她的事务处于READ COMMITTED模式，她就可能看到“s对 mallory 保密”的东西。如果她的事务在alice 做完之后就到达信息行，就会阻塞等待 alice的事务提交，并取得更新后的行内容。不过，对于来自users的隐式 SELECT，它不会取得一个已更新的行，因为子句SELECT没有FOR UPDATE，相反会使用查询开始时取得的快照读取users行。因此，策略表达式会测试mallory的特权级别的旧值并且允许她看到被更新的行。

有多种方法能解决这个问题。一种简单的答案是在行安全性策略中的子句SELECT里使用SELECT … FOR SHARE。 不过，这要求在被引用表（这里是users）上授予 UPDATE特权给受影响的用户。还有，在被引用的表上过多并发地使用行共享锁可能会导致性能问题，特别是表更新比较频繁时。另一种解决方案（如果被引用表上的更新不频繁就可行）是在更新被引用表时对它取一个排他锁，这样就没有并发事务能够检查旧的行值了。或者我们可以在提交对被引用表的更新之后、在做依赖于新安全性情况的更改之前等待所有并发事务结束。

更多细节请见CREATE POLICY 和ALTER TABLE。

## 3.3. 强制访问控制

仅安全版提供该功能。

强制访问控制是在自主访问控制的基础上对用户权限的进一步控制，通过调整用户的安全标记来控制用户行为。数据库系统在创建新的用户、表和记录时系统会默认的为其设置一个安全标记，用户的安全标记为默认值（s0:c0.c1023），表和记录的安全标记为其创建者的安全标记。强制访问控制策略对临时表暂不管控。

数据库强访问控制开关及策略设置均由syssso用户进行管理，具体操作如下：

```sql
select set_secure_param('hg_macontrol','on');
select set_secure_param('hg_macontrol','min');
select set_secure_param('hg_rowsecure','on');
select set_secure_param('hg_rowsecure','off');
```
- **hg\_macontrol：** 强制访问控制功能开关，默认 on，开启强制访问控制；参数值为 min，表示强访功能最小化，即只有自主访问控制功能。参数值重启生效。此参数受hg\_sepofpowers 三权分立开关限制，若三权功能关闭，此参数设置不生效。
- **hg\_rowsecure：** 行级强制访问功能开关。该参数只在 hg\_macontrol 为 on 时生效。参数值为 on|off，on 为开启行级访问控制，off 为关闭行级访问控制，开启表级访问控制。默认为 off。参数值重启生效。

### 3.3.1. 安全标记

**安全标记格式：**

安全标记为特定格式的字符串，如 “s0:c0.c1023”，由安全级别（敏感度）和安全类别（类别）组成。敏感度范围为s0~s15，共16个级别，类别范围为c0~c1023，共1024个类别。其中敏感度s0~s15的安全级别为递进关系，而类别之间并没有级别高低之分。一个安全标记可拥有多个类别并使用逗号分隔，如果多个安全类别是连续的则只显示第一个和最后一个中间用英文句号分隔，例如：

- **s0:c0.c1023：** 表示安全级别为 s0，安全类别为包含 c0到 c1023 全部类别的集合。
- **s5:c0.c100,c200,c300：** 表示安全级别为 s5，安全类别为包含 c0~ c100和c200~c300 类别的集合。

上述敏感度和类别的多种组合，可以自由划分，来满足不同环境下的保密等级要求，例如常见的绝密范围、机密范围、秘密范围、内部范围、公开范围、自定义范围（用户自定义），这六种范围的保密等级就可由实现。可自行从s0~s15中挑选部分与之对应，类别则可以进一步对权限进行细化。

**安全标记的支配关系：**

在比较安全标记时，若标记L1敏感度大于等于标记L2敏感度且L1类别包含L2类别，则称L1支配L2。例如安全标记“s1:c0,c1,c2”支配标记“s0:c0,c1”。若安全级别和安全类别全部相等则称这两个安全标记相等。其余情况算作不可比较。

**安全标记的设置和修改：**

在开启强制访问控制的情况下，用户被创建时，数据库会自动为其创建默认安全标记“s0:c0.c1023”。数据库对象被创建时，默认安全标记为其创建者的安全标记。用户的安全标记值存储在系统表hg\_user\_seclabel中，该表只有useroid（用户OID）和 label（安全标记）两个字段，数据库对象的安全标记存储在系统表pg\_seclabel中，改表字段说明详见下表，这两个系统表只有syssso有权访问。

pg\_seclabel的列

| 名称 | 类型 | 引用 | 描述 |
| --- | --- | --- | --- |
| objoid | oid | 任意OID 字段 | 该安全标签依附的对象的OID |
| classoid | oid | pg\_class.oid | 该对象所出现的系统目录的OID |
| objsubid | int4 |  | 对于一个在表列上的安全标签，这将是列号（objoid和classoid指表本身）。对于所有其他对象类型，本列为0。 |
| provider | text |  | 与该标签相关的标签提供者。 |
| label | text |  | 应用于该对象的安全标签。 |

目前强制访问控制模块支持的数据库对象有表，视图，序列。以上对象的安全标记可以由syssso通过函数进行修改。

表 3.5 安全标记相关函数列表

| **函数名** | **功能** |
| --- | --- |
| set\_user\_seclabel(Oid oid, char seclabel) | 将指定的用户的安全标记设置为指定值。 |
| get\_user\_seclabel(Oid oid) | 返回指定用户的安全标记。 |
| set\_table\_seclabel(Oid oid, char seclabel) | 将指定的数据库对象的安全标记设置为指定值。 |
| get\_table\_seclabel(Oid oid) | 返回指定数据库对象的安全标记。 |

三个系统用户的默认安全标记为“s0:c0.c1023”且无法被修改。系统表没有安全标记，数据库初始化时创建的记录没有行级安全标记，查询没有安全标记的行记录的seclabel系统列返回值为“unlabeled”。

```sql
highgo=# select rolname,seclabel from pg_authid;
          rolname          |  seclabel
---------------------------+-------------
 pg_monitor                | unlabeled
 pg_read_all_settings      | unlabeled
 pg_read_all_stats         | unlabeled
 pg_stat_scan_tables       | unlabeled
 pg_read_server_files      | unlabeled
 pg_write_server_files     | unlabeled
 pg_execute_server_program | unlabeled
 pg_signal_backend         | unlabeled
 sysdba                    | unlabeled
 syssao                    | unlabeled
 syssso                    | unlabeled
 test                      | s0:c0.c1023
 u1                        | s0:c0.c1023
 u2                        | s0:c0.c1023
```

### 3.3.2. 访问控制

访问控制可以分为表级访问控制和行级访问控制，默认为行级访问控制规则。目前支持对表，视图，序列的访问控制。表级访问控制时，需syssso 用户关闭行级访问控制，行级访问控制时需开启，并重启数据库生效更改。

```sql
select set_secure_param('hg_rowsecure','off');
select set_secure_param('hg_rowsecure','on);
```

**当访问对象为表时：**

在表级访问控制下（行级访问控制开关需关闭），当通过执行select 语句从表中查询数据时需要用户安全标记支配表的安全标记，否则提示错误，例如用户标记“s1:c0.c1023”,表的安全标记为“s0:c0.c1023”则可以执行查询。

```sql
--用户test 安全标记为s0:c0.c1023，级别比表 t1 安全标记 s1:c0.c1023 级别低，用户安全标记不可支配表安全标记，此时查询表报错。
test=> select a.usename,b.* from pg_user a,hg_user_seclabel b where a.usesysid=b.useroid and a.usename = 'test';
 usename | useroid |    label
---------+---------+-------------
 test     |   16384 | s0:c0.c1023
row

test=> select a.relname,b.* from pg_class a,pg_seclabel b where a.oid=b.objoid;
 relname | objoid | classoid | objsubid | provider |    label
---------+--------+----------+----------+----------+-------------
 t1      |  16395 |        0 |        0 | HG_MAC   | s1:c0.c1023
row

You are now connected to database "test" as user "test".
test=# select *,seclabel from t1;
2022-05-16 13:46:09.782 CST [42845] ERROR:  Violate MAC select rules: permission denied for t1
2022-05-16 13:46:09.782 CST [42845] STATEMENT:  select * from t1;
ERROR:  Violate MAC select rules: permission denied for t1

--用户test 安全标记为s1:c0.c1023，级别比表 t1 安全标记 s0:c0.c1023 级别高，用户安全标记可支配表安全标记，此时查询表正常。
test=> select a.usename,b.* from pg_user a,hg_user_seclabel b where a.usesysid=b.useroid and a.usename = 'test';
 usename | useroid |    label
---------+---------+-------------
 test     |   16384 | s1:c0.c1023
row

test=> select a.relname,b.* from pg_class a,pg_seclabel b where a.oid=b.objoid;
 relname | objoid | classoid | objsubid | provider |    label
---------+--------+----------+----------+----------+-------------
 t1      |  16395 |        0 |        0 | HG_MAC   | s0:c0.c1023
row

test=> \c - test
You are now connected to database "test" as user "test".
test=# select * from t1;
 id
----
  1
  2
rows
```

在表级访问控制下通过执行UPDATE 或DELETE对表中的数据行进行更新或删除操作时需要用户的安全标记和表的安全标记相等，否则提示错误。

```sql
test=> select a.usename,b.* from pg_user a,hg_user_seclabel b where a.usesysid=b.useroid and a.usename = 'test';
 usename | useroid |    label
---------+---------+-------------
 test     |   16384 | s1:c0.c1023
row

test=> select a.relname,b.* from pg_class a,pg_seclabel b where a.oid=b.objoid;
 relname | objoid | classoid | objsubid | provider |    label
---------+--------+----------+----------+----------+-------------
 t1      |  16395 |        0 |        0 | HG_MAC   | s0:c0.c1023
row

test=> \c - test
You are now connected to database "test" as user "test".
test=# update t1 set id = 5 where id = 1;
2022-05-16 14:04:26.550 CST [43043] ERROR:  Violate MAC update rules: permission denied for t1
2022-05-16 14:04:26.550 CST [43043] STATEMENT:  update t1 set id = 5 where id = 1;
ERROR:  Violate MAC update rules: permission denied for t1
test=# delete from t1 where id=1;
2022-05-16 14:15:18.546 CST [43043] ERROR:  Violate MAC delete rules: permission denied for t1
2022-05-16 14:15:18.546 CST [43043] STATEMENT:  delete from t1 where id=1;
ERROR:  Violate MAC delete rules: permission denied for t1
```

在表级安全下当通过INSERT向表中插入数据时，需要表的安全标记支配用户的安全标记，以保证数据只能由低级别流向高级别。

```sql
--用户test 安全标记为s1:c0.c1023，级别比表 t1 安全标记 s0:c0.c1023 级别高，表安全标记不可支配用户安全标记，此时插入数据报错。
test=> select a.usename,b.* from pg_user a,hg_user_seclabel b where a.usesysid=b.useroid and a.usename = 'test';
 usename | useroid |    label
---------+---------+-------------
 test     |   16384 | s1:c0.c1023
row

test=> select a.relname,b.* from pg_class a,pg_seclabel b where a.oid=b.objoid;
 relname | objoid | classoid | objsubid | provider |    label
---------+--------+----------+----------+----------+-------------
 t1      |  16395 |        0 |        0 | HG_MAC   | s0:c0.c1023
row

test=> \c - test
You are now connected to database "test" as user "test".
test=# insert into t1 values(3);
2022-05-16 14:07:37.913 CST [43043] ERROR:  Violate MAC insert rules: permission denied for t1
2022-05-16 14:07:37.913 CST [43043] STATEMENT:  insert into t1 values(3);
ERROR:  Violate MAC insert rules: permission denied for t1
```

在行级访问控制下，执行SELECT将不再判断表的安全标记，将根据表中每一行的安全标记进行判断，若用户安全标记可以支配该行的安全标记，那么返回结果否则不返回。例如用户安全标记标记为“s1:c0.c1023”，那么该用户可以通过执行SELECT查询表中任何行安全标记被“s1:c0.c1023”支配的记录。行级安全标记存储在每一行记录的系统列“seclabel”中，其默认值同样为其创建者的安全标记，行级安全标记无法被主动修改，只有当该记录被更新时该安全标记才会被更新。

```sql
test=# select a.usename,b.* from pg_user a,hg_user_seclabel b where a.usesysid=b.useroid and a.usename = 'test';
 usename | useroid |    label
---------+---------+-------------
 test     |   16384 | s1:c0.c1023
row
test=> select a.usename,b.* from pg_user a,hg_user_seclabel b where a.usesysid=b.useroid and a.usename = 'u1';
 usename | useroid |    label
---------+---------+-------------
 u1      |   16389 | s0:c0.c1023
test=# select a.relname,b.* from pg_class a,pg_seclabel b where a.oid=b.objoid;
 relname | objoid | classoid | objsubid | provider |    label
---------+--------+----------+----------+----------+-------------
 t1      |  16395 |        0 |        0 | HG_MAC   | s1:c0.c1023
row
test=# \c - test
test=# select *,seclabel from t1;
 id |  seclabel
----+-------------
|
|
rows
test=# update t1 set id=5 where id=1;
UPDATE 1

--用户test 安全标记为s1:c0.c1023，支配表 t1 中两行数据的安全标记 s0:c0.c1023、s1:c0.c1023，可正常查询表中所有数据。
test=# select *,seclabel from t1;
 id |  seclabel
----+-------------
|
|
rows
--用户test 安全标记为s0:c0.c1023，仅支配表 t1 中一行数据的安全标记 s0:c0.c1023，查询结果中也仅返回一条数据。
test=# \c - u1
test=# select *,seclabel from t1;
 id |  seclabel
----+-------------
|
```

在行级安全下，UPDATE和DELETE语句的执行除了需要满足用户安全标记与表级安全标记相等。还需要满足用户安全标记支配目标行记录的安全标记。例如安全标记为“s2:c0.c3”的用户可以更改和删除安全标记为“s2:c0.c3”的表中安全标记为“s1:c0.c2”的记录的数据。

在行级安全下对insert的访问控制与表级访问控制规则一致。因为未插入的记录还没有行安全标记。

**当访问对象为视图时：**

规则与上述对象为表时的访问规则相同，只是视图在满足上述规则时，还需其基表也满足对应的规则。

在表级访问控制规则下，当通过SELECT 去查询视图时需要用户的安全标记支配视图的安全标记，此外，还需要用户安全标记支配视图定义中使用的每一个表或视图的安全标记。

在瀚高数据库系统中，表级访问控制下，对视图进行UPDATE或DELETE操作时，若该视图是可更新视图，那么还需要满足类似于对表的访问控制规则。即需要满足用户安全标记等于视图的安全标记。例如若用户希望对视图v1进行UPDATE或DELETE 操作那么需要用户安全标记和视图v1安全标记相等，且用户安全标记和视图v1定义中使用的表的安全标记相等。

执行INSERT操作也需要满足用户安全标记被视图安全标记支配，且用户安全标记被视图v1定义中使用的表的安全标记支配。关于可更新视图详见关于视图的部分。

在行级访问控制下，对视图执行SELECT操作将不再判断表和视图的安全标记，若用户安全标记可以支配视图定义中使用的表中的行记录的安全记录，那么这些行将被作为结果返回。

在行级访问控制下，当一个视图为可更新视图时，对该视图执行UPDATE, DELETE或INSERT操作需要符合类似于访问对象为表时的访问控制规则。同样还需要满足施加在视图定义中使用的表上的访问控制规则。例如视图v1的定义中使用了表t1那么如若对视图v1执行UPDATE或DELETE操作需要满足，用户安全标记等于视图v1安全标记，且等于表t1安全标记，并且目标行记录的安全标记需要被用户安全标记支配。

**当访问控制对象为序列时：**

由于序列在数据库中是一个只有一行的表所以行级访问访问控制是没有意义的，对序列的访问控制在行级和表级访问控制下规则是一样的。

首先在数据库系统中用户对序列只有SELECT和UPDATE权限。实际上能对序列执行的sql语句只有SELECT，其余操作需要由序列操作函数进行。

函数nextval()和setval()需要UPDATE权限，以此类比于UPDATE语句，当用户通过该函数修改序列当前值时需要用户安全标记等于序列安全标记。

函数currval()和lastval()则需要SELECT权限，那么以此类比于SELECT语句，当用户调用以上函数时则需要用户安全标记支配序列安全标记。关于序列操作函数的详细信息请看关于序列的章节。

| **注意：** |
| --- |
| 当表中的某列数据类型为serial时，向其中插入默认值时会调用nextval函数，若此时序列的安全标记与用户安全标记不相等，则会因无法访问序列而导致插入数据失败。 |