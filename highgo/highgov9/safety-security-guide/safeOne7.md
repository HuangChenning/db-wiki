---
title: "自主访问控制"
book: "安全指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/safety/safeOne7.html"
tags:
  - highgo
  - highgo-v9
  - safety-security-guide
---

## 自主访问控制

自主访问控制的权限往往由数据库对象的所有者进行授权，用户获得某项权限即可执行相应的操作。

一个对象被创建，就会被分配一个所有者。所有者通常是执行创建语句的角色。对于大多数对象，默认只有其所有者才能够对其执行任何操作。其他角色要操作它，必须分配相应的权限。

## 权限介绍

数据库中可分配的有效权限有：SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES、TRIGGER、CREATE、CONNECT、TEMPORARY、EXECUTE、USAGE、ALL，详细信息请如下。

SELECT：查询权限。允许 SELECT  
命令查询列、表、视图、物化视图、或其他类似表格的对象，允许使用 COPY TO 命令，UPDATE 或 DELETE操作现有的列也需要这个权限。这个权限还允许序列使用currval 函数，允许大对象读取对象。

INSERT：插入权限。允许INSERT 命令向表、视图等对象中插入数据。可以在特定列上授予，在这种情况下INSERT命令可以在特定的列插入数据（其他列将采用默认值）。此权限还允许使用COPY FROM。

UPDATE：更新权限。允许 UPDATE 命令更新列、表、视图等。(需要SELECT权限引用表列，来确定要更新的行，或计算列的新值。)

允许使用序列使用 nextval 和 setval 函数，允许大对象写入或截断。SELECT … FOR UPDATE和SELECT … FOR  
SHARE命令除了需要SELECT权限外，还需要至少一列上有这个权限。

DELETE：删除权限。允许 DELETE  
命令从表、视图等对象中删除行。(需要SELECT权限引用表列来确定要删除的行。)

TRUNCATE：截断/清空权限。允许 TRUNCATE 命令清空在表、视图等。

REFERENCES：引用外部对象权限。允许创建引用表或表的特定列的外键约束。

TRIGGE：触发器权限。允许在表、视图等对象上创建触发器。

CREATE：创建对象权限。允许在数据库、模式、表空间中创建对象。

对于数据库，允许在数据库中创建新的模式和发布，并允许在数据库中安装受信任的扩展。

对于模式，允许在模式中创建新对象。要重命名现有对象，你必须拥有对象and所包含模式的此权限。

对于表空间，允许在表空间中创建表、索引和临时文件，并允许创建将表空间作为默认表空间的数据库。（注意，撤销此特权不会更改已有对象的位置。）

CONNECT：连接权限。允许访问者连接到数据库。此权限在连接启动时进行检查(同时受pg\_hba.conf  
配置文件中的参数限制).

TEMPORARY：临时表权限。允许在使用数据库时创建临时表。

EXECUTE：函数、过程权限。允许调用函数或过程，包括使用在函数之上实现的任何运算符。这是适用于函数和过程的唯一权限类型。

USAGE：模式连接权限。允许连接到模式中，对模式下所有对象的操作，均需要此权限。

对于程序语言，允许使用语言来创建该语言的函数。  
这是适用于过程语言的唯一权限类型。

对于模式，允许访问模式中包含的对象（假设对象自己的权限要求也已得到满足）。从本质上讲，这允许受让者”lookup”模式中的对象。如果没有此权限，仍可以看到对象名称，例如通过查询系统目录。  
此外，在撤消此权限后，现有会话可能还具有以前执行过此查找的语句，因此这不是阻止对象访问的彻底安全的方法。

对于序列, 允许使用currval 和 nextval 函数.

对于类型和域，允许在创建表、函数和其他模式对象时使用类型或域。  
（注意，此权限不控制类型的全部 “usage” ，例如查询中出现的类型的值。它仅防止创建依赖于类型的对象。  
此权限的主要目的是控制哪些用户可以对类型创建依赖项，这可能会防止所有者以后更改类型。）

对于外部数据包装器，允许使用外部数据包装器创建新服务器。

对于外部服务器，允许使用服务器创建外部表。受让者还可以创建、更改或删除与该服务器关联的自己的用户映射。

ALL: 所有权限。允许对象的类型可用的所有操作。

其他命令所需的权限罗列在相应命令的参考页上。

下表显示了ACL（访问控制列表）值中用于这些权限类型的单字母缩写。你将在下面列出的  
psql 命令的输出中，或者在查看系统目录的 ACL 列时看到这些字母。

ACL权限及字母缩写列表：

| 权限 | 缩写 | 适用对象类型 |
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

---

下表使用上面所示的缩写总结了每种类型 SQL对象可用的权限.它还显示可用于检查每种对象类型的特权设置的psql命令。

对象权限列表：

---

| 对象类型 | 所有权 | 默认PUBLIC权限 | psql命令 |
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

---

已授予特定对象的权限显示为aclitem项的列表，其中每个aclitem项描述了特定授予者授予给一个被授与者的权限。例如，

```
calvin=rw/hobbes
```

指明角色calvin具有SELECT（r）权限和授予选项（\*）以及不可授予权限UPDATE（w），均由角色hobbes授予。如果calvin对由其他授予人授予的同一对象也具有一些权限，那将显示为单独的aclitem条目。aclitem  
中的空受赠方字段代表PUBLIC。

例如，假设用户miriam创建了表mytable并且:

```
highgo=> grant select on mytable to public;

highgo=> grant select,update,insert on mytable to admin;

highgo=> grant select (col1), update (col1) on mytable to miriam_rw;
```

则 psql的 \\dp 命令将显示:

```
highgo=> \dp mytable

Access privileges

Schema | Name | Type | Access privileges | Column privileges |
Policies

-−-−-−-−+-−-−-−-−-+-−-−-−-+-−-−-−-−-−-−-−-−-−-−-−-+-−-−-−-−-−-−-−-−-−-−-−-+-−-−-−-−-−

public | mytable | table | miriam=arwdDxt/miriam+| col1: +|

| | | =r/miriam +| miriam_rw=rw/miriam |

| | | admin=arw/miriam | |

(1 row)
```

如果”Access  
privileges”列对于给定对象为空，则表示该对象具有默认权限（也就是说，它在相关系统目录中的权限条目为空）。默认权限始终包含所有者的所有权限，并且可以包括 PUBLIC 的一些权限，具体取决于对象类型，如上所述。对象上的第一个GRANT或REVOKE将实例化默认权限（例如，生成miriam\_arwdDxt/miriam），然后根据指定的请求修改它们。类似的，只有具有非默认特权的列的条目才显示在”Column privileges”中。（注意：为此目的，”default privileges”始终表示对象类型的内置缺省权限。其权限受ALTER DEFAULT PRIVILEGES 命令影响的对象将始终显示一个显式权限条目，其中包含 ALTER。）

## 权限管理

要分配权限，可以使用GRANT命令。例如，如果joe是一个已有角色，而accounts是一个已有表，更新该表的权限可以按如下方式授权：

```
GRANT UPDATE ON accounts TO joe;
```

用ALL取代特定权限会把与对象类型相关的所有权限全部授权。

```
GRANT ALL ON accounts TO joe;
```

一个特殊的名为PUBLIC的”角色”可以用来向系统中的每一个角色授予一个权限。同时，在数据库中有很多用户时可以设置”组”角色来帮助管理权限。

为了撤销一个权限，使用REVOKE命令：

```
REVOKE ALL ON accounts FROM PUBLIC;
```

对象拥有者的特殊权限（即执行DROP、GRANT、REVOKE等的权力）总是隐式地属于拥有者，并且不能被授予或撤销。但是对象拥有者可以选择撤销他们自己的普通权限，例如把一个表变得对他们自己和其他人只读。

```
REVOKE ALL ON accounts from joe;
GRANT SELECT ON accounts TO joe;
```

可以在授予权限时使用”withgrantoption”来允许接收人将权限转授给其他人。如果后来授予选项被撤销，则所有从接收人那里获得的权限（直接或者通过授权链获得）都将被撤销。

```
GRANT SELECT ON accounts TO joe with grant option;
```

在创建对象时，系统默认将某些类型对象的权限授予PUBLIC。默认情况下，在表、表列、序列、外部数据包装器、外部服务器、大型对象、模式或表空间上，不向PUBLIC授予权限。对于其他类型的对象，授予PUBLIC的默认权限如下所示：针对数据库的CONNECT和TEMPORARY（创建临时表）权限;针对函数和程序的EXECUTE权限;以及针对语言和数据类型（包括域）的USAGE权限。当然，对象所有者可以REVOKE默认权限和特别授予的权限。（为了最大程度的安全性，在创建对象的同一事务中发出REVOKE;那么就没有其他用户能够使用该对象的窗口。）此外，可以使用ALTER DEFAULT PRIVILEGES命令取代这些默认权限设置。