---
title: "系统表"
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle3.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## 系统表

本节记录对PostgreSQL系统表进行修订部分内容，以及新增数据库兼容特性相关系统表内容。

其中PG\_OBJECT、PG\_PACKAGE、PG\_PACKAGE\_BODY、DUAL、PG\_RECYCLEBIN为新增系统表。

| **表名称** | **说明** |
| --- | --- |
| PG\_ATTRIBUTE | 存储有关表列的信息 |
| PG\_CLASS | 存储表、索引、序列、视图等对象的信息 |
| PG\_FOREIGN\_SERVER | 存储外部服务相关信息 |
| PG\_OBJECT | 存储对象相关信息 |
| PG\_PACKAGE | 定义了PLISQL的包 |
| PG\_PACKAGE\_BODY | 定义了PLISQL的包体 |
| PG\_SEQUENCE | 存储有关序列的信息 |
| DUAL | 伪表 |
| PG\_RECYCLEBIN | 存储可回收对象的信息 |

## PG\_ATTRIBUTE

表pg\_attribute存储有关表列的信息。数据库中的每一个表的每一个列都恰好在pg\_attribute中有一行。（这其中也会有索引的属性项，并且事实上所有具有pg\_class项的对象在这里都有属性项），术语属性等同于列，这里使用是尊重PG官方手册。

| **列名** | **数据类型** | **引用** | **描述** |
| --- | --- | --- | --- |
| ATTRELID | OID | pg\_class.oid | 列所属的表 |
| ATTNAME | NAME |  | 列名 |
| ATTTYPID | OID | pg\_type.oid | 列的数据类型 |
| ATTSTATTARGET | INT4 |  | attstattarget控制由ANALYZE对此列收集的统计信息的细节层次。0值表示不会收集任何统计信息。一个负值则说明直接使用系统默认的目标。正值的确切含义取决于数据类型。对于标量数据类型，attstattarget既是要收集的“最常见值”的目标号，也是要创建的柱状图容器的目标号。 |
| ATTLEN | INT2 |  | 本列类型的pg\_type.typelen的一个拷贝 |
| ATTNUM | INT2 |  | 列的编号。一般列从1开始向上编号。系统列（如ctid）则拥有（任意）负值编号 |
| ATTNDIMS | INT4 |  | 如果该列是一个数组类型，这里就是其维度数；否则为0。（在目前一个数组的维度数并不被强制，因此任何非零值都能有效地表明“这是一个数组”。） |
| ATTCACHEOFF | INT4 |  | 在存储中总是为-1，但是当被载入到一个内存中的行描述符后，这里可能会更新为属性在行内的偏移 |
| ATTTYPMOD | INT4 |  | atttypmod记录了在表创建时提供的类型相关数据（例如一个varchar列的最大长度）。它会被传递给类型相关的输入函数和长度强制函数。对于那些不需要atttypmod的类型，这个值通常总是为-1. |
| ATTBYVAL | BOOL |  | 该列类型的pg\_type.typbyval的一个拷贝 |
| ATTSTORAGE | CHAR |  | 通常是该列类型的pg\_type.typstorage的一个拷贝。对于可TOAST的数据类型，这可以在创建后被修改以控制存储策略。 |
| ATTALIGN | CHAR |  | 该列类型的pg\_type.typalign的一个拷贝 |
| ATTCOMPRESSION | CHAR |  | 该列当前的压缩方法。通常为’\\0’以指定使用当前默认设置。否则，’p’选择pglz压缩，而’l’选择LZ4压缩。但是，当attstorage不允许压缩时，该字段将被忽略。 |
| ATTNOTNULL | BOOL |  | 这表示一个非空约束 |
| ATTHASDEF | BOOL |  | 该列有一个默认表达式或生成的表达式，在此情况下在pg\_attrdef表中会有一个对应项来真正定义该表达式。（检查attgenerated以确定是默认还是生成的表达式。） |
| ATTHASMISSING | BOOL |  | 该列在行中完全缺失时会用到这个列的值，如果在行创建之后增加一个有非易失DEFAULT值的列，就会发生这种情况。实际使用的值被存放在attmissngval列中。 |
| **ATTIDENTITY** | **CHAR** |  | 在PG兼容模式中，如果是一个零字节（’’），则不是一个标识列。否则，a=总是生成，d=默认生成。      在Oracle兼容模式中，i代表自增列不能插入只能生成，o代表可以指定插入，但不能指定插入NULL，n代表可以指定插入，包括NULL |
| ATTGENERATED | CHAR |  | 如果为零字节（’’）,则不是生成的列。否则，s=stored。（将来可能会添加其他值。） |
| ATTISDROPPED | BOOL |  | 该列被删除且不再有效。一个删除的列仍然物理存在于表中，但是会被分析器忽略并因此无法通过SQL访问。 |
| ATTISLOCAL | BOOL |  | 该列是由关系本地定义的。注意一个列可以同时时本地定义和继承的。 |
| ATTINHCOUNT | INT4 |  | 该列的直接祖先的编号。一个具有非零编号祖先的列不可能被删除或者重命名。 |
| ATTCOLLATION | OID | pg\_collation.oid | 该列被定义的排序规则，如果该列不是一个可排序数据类型则为0。 |
| ATTACL | ACLITEM\[\] |  | 列级访问权限 |
| ATTOPTIONS | TEXT\[\] |  | 属性级选项，以“keyword=value”形式的字符串 |
| ATTFDWOPTIONS | TEXT\[\] |  | 属性级的外部数据包装器选项，以“keyword=value”形式的字符串 |
| ATTMISSINGVAL | ANYARRAY |  | 这个列中是一个含有一个元素的数组，其中的值被用于该列在行中完全缺失时，如果在行创建之后增加一个有非易失DEFAULT值的列，就会发生这种情况。只有当atthasmissing为真时才使用这个值。如果没有值则该列为空。 |
| ATTISVISIBLE | BOOL |  | 列是否可见，默认可见 |

## PG\_CLASS

表pg\_class记录表和几乎所有具有列或者像表的对象。这包括索引、序列、视图、物化视图、组合类型和TOAST表

| **列名** | **数据类型** | **引用** | **描述** |
| --- | --- | --- | --- |
| OID | OID |  | 行标识符 |
| RELNAME | NAME |  | 表、索引、视图等的名字 |
| RELNAMESPACE | OID | pg\_namespace.oid | 包含该关系的名字空间的OID |
| RELTYPE | OID | pg\_type.oid | 可能存在的表行类型所对应数据类型的OID；对索引为0，序列，和toast表，索引没有pg\_type项 |
| RELOFTYPE | OID | pg\_type.od | 对于有类型的表，为底层组合类型的OID，对于其他所有关系为0 |
| RELOWNER | OID | pg\_authid.oid | 关系的拥有者 |
| RELAM | OID | pg\_am.oid | 如果这是一个表或者索引，表示索引使用的访问方法（堆、B树、哈希等）；否则为0（0出现在序列，以及没有存储的关系，例如视图） |
| RELFILENODE | OID |  | 该关系的磁盘文件的名字，0表示这是一个“映射”关系，其磁盘文件名取决于低层状态 |
| RELTABLESPACE | OID | pg\_tablespace.oid | 该关系所存储的表空间。如果为0，使用数据库的默认表空间。（如果关系无磁盘文件时无意义） |
| RELPAGES | INT4 |  | 该表磁盘表面的尺寸，以页面计（页面尺寸为BLCKSZ）。这只是一个由规划器使用的估计值。 |
| RELTUPLES | FLOAT4 |  | 表中的存活行数。这只是一个由规划器使用的估计值。如果该表从未被清理或分析，包含-1的reltuples表示行数是未知的。 |
| RELALLVISIBLE | INT4 |  | 在表的可见性映射表中被标记为全可见的页数。这只是一个由规划器使用的估计值。 |
| RELTOASTRELID | OID | pg\_class.oid | 与该表相关联的TOAST表的OID，如果没有则为零。TOAST表将大属性“线外”存储在一个二级表中。 |
| RELHASINDEX | BOOL |  | 如果这是一个表并且其上建有（或最近建有）索引则为真 |
| RELISSHARED | BOOL |  | 如果该表在集簇中的所有数据库间共享则为真。只有某些系统目录（如pg\_database）是共享的。 |
| RELPERSISTENCE | CHAR |  | p = 永久表，u = 无日志表， t = 临时表，g=全局临时表 |
| RELKIND | CHAR |  | r = 普通表， i = 索引， S = 序列， t = TOAST表， v = 视图， m = 物化视图， c = 组合类型， f = 外部表， p = 分区表， I = 分区索引 |
| RELNATTS | INT2 |  | 关系中用户列的数目（系统列不计算在内）。在pg\_attribute中必须有这么多对应的项。 |
| RELCHECKS | INT2 |  | 表上CHECK约束的数目 |
| RELHASRULES | BOOL |  | 如果表有（或曾有）规则则为真 |
| RELHASTRIGGERS | BOOL |  | 如果表有（或曾有）触发器则为真 |
| RELHASSUBCLASS | BOOL |  | 如果表或索引具有（或曾经具有）任何继承子项，则为真(True) |
| RELROWSECURITY | BOOL |  | 如果表上启用了行级安全性则为真 |
| RELFORCEROWSECURITY | BOOL |  | 如果行级安全性（启用时）也适用于表拥有者则为真 |
| RELISPOPULATED | BOOL |  | 如果表已被填充则为真（对于所有关系该列都为真，但对于某些物化视图却不是） |
| RELREPLIDENT | CHAR |  | 用来为行形成“replica identity”的列： d = 默认 (主键，如果存在), n = 无, f = 所有列 i = 索引的indisreplident被设置或者为默认 |
| RELISPARTITION | BOOL |  | 如果表或索引是一个分区，则为真 |
| RELREWRITE | OID | pg\_class.oid | 对于在要求表重写的DDL操作期间被写入的新关系，这个域包含原始关系的OID，否则为零。 那种状态仅在内部可见，对于一个用户可见的关系这个域应该从不包含不是零的值 |
| RELFROZENXID | XID |  | 在此之前的所有事务ID在表中已经被替换为一个永久的（“冻结的”) 事务ID。 这用于跟踪表是否需要被清理，以便阻止事务ID回卷或者允许pg\_xact被收缩。 如果该关系不是一个表则为0（InvalidTransactionId） |
| RELMINMXID | XID |  | 在此之前的多事务ID在表中已经被替换为一个事务ID。这被用于跟踪表是否需要被清理，以阻止 多事务ID回卷或者允许pg\_multixact被收缩。如果关系不是一个表则 为0（InvalidMultiXactId） |
| RELACL | ACLITEM\[\] |  | 访问权限 |
| RELOPTIONS | TEXT\[\] |  | 访问方法相关的选项，以“keyword=value”字符串形式 |
| RELPARTBOUND | PG\_NODE\_TREE |  | 如果表示一个分区（见relispartition），分区边界的内部表达 |
| RELHASROWID | BOOL |  | 表是否拥有ROWID，默认否 |

## PG\_FOREIGN\_SERVER

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| OID | oid | 行标识符 |
| srvname | name | 外部服务器的名字 |
| srvowner | oid | 外部服务器的拥有者 |
| srvfdw | oid | 此外部服务器的外部数据包装器的OID |
| olnkispublic | boolean | 标识创建的dblink是否是public的 |
| olnkisshared | boolean | 标识创建的dblink是否是共享的 |
| olnksharedauth | boolean | 标识创建的共享的dblink是否通过认证，验证只在第一次调用时，如果通过验证，将更新这个值，后续在同一个dblink上的访问将不再发起认证 |
| olnkconntype | bigint | 标识创建的dblink的类型，有三种枚举类型ORA\_DBLINK\_CONNECTED\_USER、ORA\_DBLINK\_FIXED\_USER、ORA\_DBLINK\_CURRENT\_USER对用，其值为1、2、3 |
| srvtype | text | 服务器的类型（可选） |
| srvversion | text | 服务器的版本（可选） |
| srvacl | aclitem\[\] | 访问权限 |
| srvoptions | text\[\] | 外部服务器特定选项，以“keyword=value”字符串形式 |
| olnkusingstring | text | 保存了创建dblink时的连接字符串信息 |
| olnksviname | text | dblink的服务名称 |

## PG\_OBJECT

| **列名** | **类型** | **说明** |
| --- | --- | --- |
| obj\_oid | oid | 对象的oid |
| objsubid | integer | 列属性（针对表的列的序号） |
| objname | name | 对象的名字 |
| refclassid | oid | 存储该对象的系统表oid |
| schemaoid | oid | 对象schema |
| objkind | char | 对象类型：      ‘r’：普通表      ‘v’：视图      ‘m’：物化视图      ‘P’：分区表      ‘F’：外部表      ‘p’：存储过程      ‘w’：窗口函数      ‘f’：普通函数      ‘a’：聚集函数      ‘s’：模式      ‘d’：数据库      ‘t’：触发器      ‘c’：列名称 |
| compatible\_mode | char | 对象是在那个兼容模式下创建的。      ‘o’：ORACLE兼容模式下创建的对象      ‘m’：MYSQL兼容模式下创建的对象      ‘p’：PG模式下创建的对象 |
| created | timestamp | 创建时间 |
| modified | timestamp | 最新的修改时间 |
| option | jsonb | 对象属性 |

## PG\_PACKAGE

| **列名** | **数据类型** | **引用** | **描述** |
| --- | --- | --- | --- |
| OID | OID |  | 行标识符 |
| PKGNAME | NAME |  | 包名称 |
| PKGNAMESPACE | OID |  | 包命名空间 |
| PKGOWNER | OID |  | 包所属用户 |
| DEFINE\_INVOK | BOOL |  | 指定包中函数、存储过程以及包规范中声明的显示游标的AUTHID |
| EDITABLE | BOOL |  | 对象是否是可编辑的 |
| USE\_COLLATION | BOOL |  | 使用字符串排序集 |
| PKGACL | ACLITEM\[\] |  | 包访问权限列表 |
| ACCESSSOURCE | PG\_NODE\_TREE |  | 指定可以调用该包的每个访问器 |
| PKGSRC | TEXT |  | 包定义内容 |

## PG\_PACKAGE\_BODY

| **列名** | **数据类型** | **引用** | **描述** |
| --- | --- | --- | --- |
| OID | OID |  | 行标识符 |
| PKGOID | OID |  | 包OID |
| BODYSRC | TEXT |  | 包体内容 |

## PG\_SEQUENCE

目录pg\_sequence包含有关序列的信息。 一些序列的信息（例如名称和方案）放在pg\_class中。

| **列名** | **数据类型** | **引用** | **描述** |
| --- | --- | --- | --- |
| SEQRELID | OID | pg\_class.oid | 这个序列的pg\_class项的OID |
| SEQTYPID | OID | pg\_type.oid | 序列的数据类型 |
| SEQSTART | INT8 |  | 序列的起始值 |
| SEQINCREMENT | INT8 |  | 序列的增量值 |
| SEQMAX | INT8 |  | 序列的最大值 |
| SEQMIN | INT8 |  | 序列的最小值 |
| SEQCACHE | INT8 |  | 序列的缓冲尺寸 |
| SEQCYCLE | BOOL |  | 序列是否循环 |
| FLAGS | INT2 |  | 标志支持scale、extend、session选项。 |

## DUAL

DUAL表属于SYS模式下的一个虚拟表，包含一列为DUMMY, 默认类型为VARCHAR2 (1)。从DUAL表中进行选择对于使用SELECT语句计算常量表达式很有用。表中仅有一行数据。

## PG\_RECYCLEBIN

表pg\_recyclebin存储可回收对象的信息。该表在V9.0.5及以后的版本中支持。

| **列名** | **数据类型** | **引用** | **描述** |
| --- | --- | --- | --- |
| OID | OID |  | 为回收对象自动生成的唯一oid |
| RCYBASEID | OID | pg\_recyclebin.oid | 回收对象所依赖的基表在pg\_recyclebin表中的id |
| RCYRELID | OID |  | 对象的relation id |
| RCYNAME | NAME |  | 为回收对象生成的唯一名称 |
| RCYORIGINNAME | NAME |  | 对象原始的名称 |
| RCYOPERATION | CHAR |  | 操作类型：’t’ = TRUNCATE, ‘d’ = DROP |
| RCYTYPE | SMALLINT |  | 对象的类型：0 table, 1 index, 2 toast table, 3 toast index |
| RCYRECYCLETIME | TIMESTAMP WITH TIME ZONE |  | 对象被回收的时间 |
| RCYNAMESPACE | OID |  | 对象所属的namespace的oid |
| RCYTABLESPACE | OID |  | 对象所属的tablespace的oid |
| RCYRELFILENODE | OID |  | 对象被回收的filenode的oid |