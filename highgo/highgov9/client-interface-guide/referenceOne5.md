---
title: "信息模式"
book: "客户端接口指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceOne5.html"
tags:
  - highgo
  - highgo-v9
  - client-interface-guide
---

## 信息模式

信息模式由一组视图构成，它们包含定义在当前数据库中对象的信息。信息模式以 SQL 标准定义，因此能够被移植并且保持稳定 — 系统目录则不同，它们是与瀚高数据库相关的并且是为了实现的考虑而建模的。不过，信息模式视图不包含与瀚高数据库相关特性有关的信息。要咨询那些信息你需要查询系统目录或其他瀚高数据库-相关视图。

| **注意：** |
| --- |
| 当在数据库中查询约束信息时，一个期望返回一行的标准兼容的查询可能返回多行。这是因为 SQL 标准要求约束名在一个模式中唯一，但是瀚高数据库并不强制这种限制。瀚高数据库自动产生的约束名避免在相同的模式中重复，但是用户能够指定这种重复的名称。这个问题可能在查询信息模式视图时出现，例如check\_constraint\_routine\_usage、check\_constraints、domain\_constraints和 referential\_constraints。一些其他视图也有相似的问题，但是它们包含了表名来帮助区分重复行，例如constraint\_column\_usage、 constraint\_table\_usage、table\_constraints。 |

## 模式

信息模式本身是一个名为information\_schema的模式。这个模式自动存在于所有数据库中。这个模式的拥有者是集簇中的初始数据库用户，并且该用户自然地拥有这个模式上的所有特权，包括删除它的能力（但是这样节省的空间是很小的）。

默认情况下，信息模式不在模式搜索路径中，因此你需要使用限定名访问其中的所有对象。因为信息模式中的某些对象的名称是可能出现在用户应用中的一般名称，如果你想把该信息模式放在路径中，你应该小心。

## 数据类型

信息模式视图的列使用定义在信息模式中的特殊数据类型。它们被定义为普通内建类型之上的简单域。你不应在信息模式之外使用这些类型进行工作，但是如果你的应用从信息模式中进行选择，那你的应用就必须准备好面对它们。

这些类型是：

cardinal\_number

一种非负整数。

character\_data

一种字符串（没有指定最大长度）。

sql\_identifier

一种字符串。这种类型被用于 SQL 标识符，类型character\_data被用于任何其他类型的文本数据。

time\_stamp

在类型timestamp with time zone之上的一个域。

yes\_or\_no

一种字符串域，它包含YES或NO。这被用来在信息模式中表示布尔（真/假）（信息模式是在类型boolean被加到 SQL 标准之前被发明的，因此这个惯例是用来使信息模式向后兼容）。

信息模式中的每一列都是这五种类型之一。

## information\_schema\_catalog\_name

information\_schema\_catalog\_name是一个表，它总是包含一行和一列，其中包含了当前数据库（SQL 术语中的当前目录）的名字。

| **名称** | **数据类型** | 描述 |
| --- | --- | --- |
| catalog\_name | sql\_identifier | 包含这个信息模式的数据库名 |

: 表 5.1 information\_schema\_catalog\_name列

## administrable\_role\_authorizations

视图administrable\_role\_authorizations标识当前用户对其有管理选项的所有角色。

| **名称** | 数据类型 | **描述** |
| --- | --- | --- |
| grantee | sql\_identifier | 被授予这个角色的成员关系的角色名（可以是当前用户，或者在嵌套角色成员关系情况下的一个不同角色） |
| role\_name | sql\_identifier | 角色名 |
| is\_grantable | yes\_or\_no | 总是 YES |

: 表 5.2 administrable\_role\_authorizations列

## applicable\_roles

视图applicable\_roles当前用户可以使用其特权的所有角色。这意味着有某种角色授权链从当前用户到讨论中的角色。当前用户本身也是一个可应用的角色。可应用的角色的集合通常被用于权限检查。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantee | sql\_identifier | 被授予这个角色的成员关系的角色名（可以是当前用户，或者在嵌套角色成员关系情况下的一个不同角色） |
| role\_name | sql\_identifier | 一个角色的名字 |
| is\_grantable | yes\_or\_no | YES表示被授予者在该角色上有管理选项，NO表示没有管理选项 |

: 表 5.3 applicable\_roles列

## attributes

视图attributes包含数据库中定义的组合数据类型的属性的有关信息（注意该视图并不给出有关表列的信息，表列有时候在 Highgo上下文环境中也被称为属性）。只有当前用户能够访问（由于是拥有者获得的权限或是在类型上有某些特权）的那些属性会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| udt\_catalog | sql\_identifier | 包含该数据类型的数据库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 包含该数据类型的模式名 |
| udt\_name | sql\_identifier | 数据类型名 |
| attribute\_name | sql\_identifier | 属性名 |
| ordinal\_position | cardinal\_number | 属性在该数据类型内部的顺序位置（从 1 开始计算） |
| attribute\_default | character\_data | 该属性的默认表达式 |
| is\_nullable | yes\_or\_no | 如果该属性是可能为空的，值为YES，否则为NO |
| data\_type | character\_data | 如果该属性是一个内建类 型，此列值为该属性的数据类型；如果该属性是某种数组，此列值为ARRAY（在这种情况下，见视图element\_types）；其他情况，此列值为USERDEFINED（在这种情况下，该类型在attribute\_udt\_name和相关列中标识）。 |
| character\_maximum\_length | cardinal\_number | 如果data\_type标识一个字符或位串类型，这里是声明的最大长度；如果没有声明最大长度，则对于所有其他数据类型为空。 |
| character\_octet\_length | cardinal\_number | 如果data\_type标识一个字符类型，这里是一个数据的最大可能长度（以字节计）；对其他所有数据类型为空。最大字节长度取决于声明的字符最大长度（见上文）和服务器编码。 |
| character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_catalog | sql\_identifier | 包含此属性排序规则的数据库名（总是当前数据库），如果默认或者该属性的数据类型不可排序则为空 |
| collation\_schema | sql\_identifier | 包含此属性排序规则的模式名，如果默认或者该属性的数据类型不可排序则为空 |
| collation\_name | sql\_identifier | 该属性排序规则的名称，如果默认或者该属性的数据类型不可排序则为空 |
| numeric\_precision | cardinal\_number | 如果data\_type标识一种数字类型，这列包含这个属性类型的（声明的或隐式的）精度。精度指示了有效位数。它可以按照列numeric\_precision\_radix中指定的被表示为十进制（基于 10）或二进制（基于 2）。对于所有其他数据类型，这一列为空。 |
| numeric\_precision\_radix | cardinal\_number | 如果data\_type标识一种数字类型，这一列指示numeric\_precision和numeric\_scale列中的值是基于什么来表示。该值为 2 或 10。对于所有其他数据类型，这一列为空。 |
| numeric\_scale | cardinal\_number | 如果data\_type标识一种准确数字类型，这列包含这个属性类型的（声明的或隐式的）比例。比例指示了有效位数。它可以按照列numeric\_precision\_radix中指定的被表示为十进制（基于 10）或二进制（基于 2）。对于所有其他数据类型，这一列为空。 |
| datetime\_precision | cardinal\_number | 如果data\_type标识一种日期、时间、时间戳或时间间隔类型，这一列包含这个属性类型的（声明的或隐式的）分数秒的精度，也就是秒值的小数点后的十进制位数。对于所有其他数据类型，这一列为空。 |
| interval\_type | character\_data | 如果data\_type标识一种时间间隔类型，这一列包含时间间隔为这个属性包括哪些域的声明，例如YEAR TO MONTH、DAY TO SECOND等等。如果没有指定域限制（也就是该时间间隔接受所有域），并且对于所有其他数据类型，这个域为空。 |
| interval\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性（关于时间间隔类型属性的分数秒精度可见datetime\_precision） |
| attribute\_udt\_catalog | sql\_identifier | 属性数据类型被定义的数据名（总是当前数据库） |
| attribute\_udt\_schema | sql\_identifier | 属性数据类型被定义的模式名 |
| attribute\_udt\_name | sql\_identifier | 属性数据类型的名称 |
| scope\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| maximum\_cardinality | cardinal\_number | 总是空，因为数组在瀚高数据库中总是有无限制的最大势 |
| dtd\_identifier | sql\_identifier | 该列的数据类型描述符的一个标识符，在从属于该表的数据类型标识符之中唯一。这主要用于与这类标识符的其他实例进行连接（该标识符的指定格式没有被定义并且不保证在未来的版本中保持相同）。 |
| is\_derived\_reference\_attribute | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |

: 表 5.4 attributes列

关于某些列的详情，参见第 5.17 节之下的一个相似结构的视图。

## character\_sets

视图character\_sets标识当前数据库中可用的字符集。因为瀚高数据库不支持在同一个数据库中有多个字符集，这个视图只显示一个字符集，它就是数据库编码。

注意下列术语在 SQL 标准中是怎样使用的：

字元集（character repertoire）

字符的一个抽象集合，例如UNICODE、UCS或LATIN1。它不作为一个 SQL 对象显示，但是在这个视图中可见。

字符编码形式（character encoding form）

某种字元集的一种编码。大部分较老的字元集只使用一种编码形式，并且因此它们没有独立的名字（例如LATIN1就是一种适用于LATIN1字元集的编码形式）。但是 Unicode 就有几种编码形式如UTF8、UTF16等等（并非全部被瀚高数据库支持）。编码形式不作为一个 SQL 对象显示，但是在这个视图中可见。

字符集（character set）

一个标识一种字元集、一种字符编码以及一种默认排序规则的命名 SQL 对象。一个预定义的字符集通常具有和一种编码形式相同的名字，但是用户可以定义其他名字。例如，字符集UTF8通常标识字元集UCS、编码形式UTF8以及某种默认排序规则。

你可以把瀚高数据库中的一种”编码”想成一个字符集或是一种字符编码形式。它们将具有相同的名字，并且在一个数据库中只能用其中一个。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| character\_set\_catalog | sql\_identifier | 当前字符集并未被实现为模式对象，因此这一列为空。 |
| character\_set\_schema | sql\_identifier | 当前字符集并未被实现为模式对象，因此这一列为空。 |
| character\_set\_name | sql\_identifier | 该字符集的名字，当前实现为显示该数据库编码的名字 |
| character\_repertoire | sql\_identifier | 字元集，如果编码为UTF8则显示UCS，否则只显示编码名称 |
| form\_of\_use | sql\_identifier | 字符编码形式，与数据库编码相同 |
| default\_collate\_catalog | sql\_identifier | 包含该默认排序规则的数据库名（如果任意排序规则被标识，总是当前数据库） |
| default\_collate\_schema | sql\_identifier | 包含该默认排序规则的模式名 |
| default\_collate\_name | sql\_identifier | 默认排序规则的名字。该默认排序规则被标识为匹配当前数据库的COLLATE和CTYPE设置的排序规则。如果没有那种排序规则，那么这一列和相关模式以及目录列为空。 |

: 表 5.5 character\_sets列

## check\_constraint\_routine\_usage

视图check\_constraint\_routine\_usage标识被检查约束琐事使用的例程（函数和过程）。只有被一个当前启用的角色所拥有的例程才被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该约束的模式名 |
| constraint\_name | sql\_identifier | 约束名 |
| specific\_catalog | sql\_identifier | 包含该函数的数据库名（总当前数据库） |
| specific\_schema | sql\_identifier | 包含该函数的模式名 |
| specific\_name | sql\_identifier | 该函数的“指定名称”。 |

: 表 5.6 check\_constraint\_routine\_usage列

## check\_constraints

视图check\_constraints包含所有检查约束，不管是定义在一个表上的还是定义在一个域上的，它们被一个当前启用的角色所拥有（表或域的拥有者就是约束的拥有者）。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该约束的模式名 |
| constraint\_name | sql\_identifier | 约束名 |
| specific\_catalog | sql\_identifier | 包含该函数的数据库名（总当前数据库） |
| specific\_schema | sql\_identifier | 包含该函数的模式名 |
| specific\_name | sql\_identifier | 该函数的“指定名称”。 |

: 表 5.7 check\_constraints列

## collations

视图collations包含在当前数据库中可用的排序规则。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该排序规则的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该排序规则的模式名 |
| constraint\_name | sql\_identifier | 默认排序规则的名称 |
| pad\_attribute | character\_data | 总是NO PAD（另一种选择PAD SPACE没有被瀚高数据库支持） |

: 表 5.8 collations列

## collation\_character\_set\_applicability

视图collation\_character\_set\_applicability标识可用的排序规则适用于哪些字符集。在瀚高数据库中，每个数据库中只有一种字符集（解释见第 5.7 节），因此这个视图没有提供很有用的信息。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该排序规则的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该排序规则的模式名 |
| constraint\_name | sql\_identifier | 默认排序规则的名称 |
| character\_set\_catalog | sql\_identifier | 当前字符集还未被实现为模式对象，所以这一列为空 |
| character\_set\_schema | sql\_identifier | 当前字符集还未被实现为模式对象，所以这一列为空 |
| character\_set\_name | sql\_identifier | 字符集名称 |

: 表 5.9 collation\_character\_set\_applicability列

## column\_column\_usage

视图column\_column\_usage标识依赖于同一表中的另一个基本列生成的所有列。只包含当前启用的角色所拥有的表。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含表的数据库的名称(总是当前数据库) |
| table\_schema | sql\_identifier | 包含表的模式的名称 |
| table\_name | sql\_identifier | 表的名称 |
| column\_name | sql\_identifier | 生成列所依赖的基本列的名称 |
| dependent\_column | sql\_identifier | 生成的列的名称 |

: 表 5.10 column\_column\_usage Columns

## column\_domain\_usage

视图column\_domain\_usage标识所有使用定义在当前数据库中并且被一个当前启用的角色拥有的域的列（表列或视图列）。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| domain\_catalog | sql\_identifier | 包含该域的数据库名（总是当前数据库） |
| domain\_schema | sql\_identifier | 包含该域的模式名 |
| domain\_name | sql\_identifier | 域名称 |
| table\_catalog | sql\_identifier | 包含该表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该表的模式名 |
| table\_name | sql\_identifier | 表名称 |
| column\_name | sql\_identifier | 列名称 |

: 表 5.11 column\_domain\_usage列

## column\_options

视图column\_options包含为当前数据库中外部表列定义的所有选项。只有当前用户能够访问（作为拥有者或具有某些特权）的那些外部表列才被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含该外部表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该外部表的模式名 |
| table\_name | sql\_identifier | 外部表名 |
| column\_name | sql\_identifier | 列名称 |
| option\_name | sql\_identifier | 一个选项名 |
| option\_value | sql\_identifier | 该选项的值 |

: 表 5.12 column\_options列

## column\_privileges

视图column\_privileges标识所有授予给一个当前启用的角色或者被一个当前启用的角色授予的特权。对每一个列、授予者、被授予者的组合只有一行。

如果一个特权被授予在一整个表上，它在这个视图中被显示为在每一列上授予，但是只有可用于列粒度的特权类型才会这样： SELECT、INSERT、 UPDATE、REFERENCES。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee | sql\_identifier | 被授予该特权的角色名 |
| table\_catalog | sql\_identifier | 包含该列的表所在的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该列的表所在的模式名 |
| table\_name | sql\_identifier | 包含该列的表名 |
| column\_name | sql\_identifier | 列名称 |
| privilege\_type | character\_data | 特权类型：SELECT、NSERT、UPDATE或 REFERENCES |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.13 column\_privileges列

## column\_udt\_usage

视图column\_udt\_usage标识所有使用被一个当前启用的角色拥有的数据类型的列。注意在瀚高数据库中，内建数据类型的行为和用户定义的类型相似，因此它们也被包括在这里。详见第 5.17 节。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| udt\_catalog | sql\_identifier | 该列数据类型（如果适用，底层的域类型）被定义的数据库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 该列数据类型（如果适用，底层的域类型）被定义的模式名 |
| udt\_name | sql\_identifier | 该列数据类型（如果适用，底层的域类型）的名称 |
| table\_catalog | sql\_identifier | 该列数据类型（如果适用，底层的域类型）的名称 |
| table\_catalog | sql\_identifier | 包含该表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该表的模式名 |
| table\_name | sql\_identifier | 表名称 |
| column\_name | sql\_identifier | 列名称 |

: 表 5.14 column\_udt\_usage列

## columns

视图columns包含数据库中有关所有表列（或视图列）的信息。系统列（ctid等）不被包括在内。只有那些当前用户能够访问（作为拥有者或具有某些特权）的列才被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含该表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该表的模式名 |
| table\_name | sql\_identifier | 表名称 |
| column\_name | sql\_identifier | 列名称 |
| ordinal\_position | cardinal\_number | 该列在表内的顺序位置（从 1开始计） |
| column\_default | character\_data | 该列的默认表达式 |
| is\_nullable | yes\_or\_no | 如果该列可以为空，则为YES，否则为NO。一个非空约束是让一列成为不能为空的方法，但还有其他方法。 |
| data\_type | character\_data | 如果该列的数据类型是一种内建类型，则为该列的数据类型；如果是某种数组（此种情况见视图element\_types），则为ARRAY；否则为USERDEFINED（此种情况下该类型被标识在udt\_name和相关列中）。如果该列基于一个域，这一列引用该域底层的类型（该列被标识在domain\_name和相关列中）。 |
| character\_maximum\_length | cardinal\_number | 如果data\_type标识一种字符或位串类型，这里是声明的最大长度；如果没有声明最大长度或者所有其他数据类型，这里为空。 |
| character\_octet\_length | cardinal\_number | 如果data\_type标识一个字符类型，这里是一个数据的最大可能长度（以字节计）；对其他所有数据类型为空。最大字节长度取决于声明的字符最大长度（见上文）和服务器编码。 |
| numeric\_precision | cardinal\_number | 如果data\_type标识一种数字类型，这列包含这个属性类型的（声明的或隐式的）精度。精度指示了有效位数。它可以按照 列numeric\_precision\_radix中指定的被表示为十进制（基于 10）或二进制（基 于 2）。对于所有其他数据类型，这一列为空。 |
| numeric\_precision\_radix | cardinal\_number | 如果data\_type标识一种数字类型，这一列指示numeric\_precision和numeric\_scale列中的值是基于什么来表示。该值为 2 或 10。对于所有其他数据类型，这一列为空。 |
| numeric\_scale | cardinal\_number | 如果data\_type标识一种准确数字类型，这列包含这个属性类型的（声明的或隐式）比例。比例指示了有效位数。它可以按照列numeric\_ precision\_radix中指定的被表示为十进制（基于 10）或二进制（基于2）。对于所有其他数据类型，这一列为空。 |
| datetime\_precision | cardinal\_number | 如果data\_type标识一种日期、时间、时间戳或时间间类型，这一列包含这个属性类型的（声明的或隐式的）分数秒的精度，也就是秒值的小数点后的十进制位数。对于所有其他数据类型，这一列为空。 |
| interval\_type | character\_data | 如果data\_type标识一种时间间隔类型，这一列包含时间间隔为这个属性包括哪些域的声明，例如YEAR TO MONTH、DAY TO SECOND等等。如果没有指定域限制（也就是该时间间隔接受所有域），并且对于所有其他数据类型，这个域为空。 |
| character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_catalog | sql\_identifier | 包含此属性排序规则的数据库名（总是当前数据库）， 如果默认或者该属性的数据类型不可排序则为空 |
| collation\_schema | sql\_identifier | 包含此属性排序规则的模式名，如果默认或者该属性的 数据类型不可排序则为空 |
| collation\_name | sql\_identifier | 该属性排序规则的名称，如默认或者该属性的数据类型不可排序则为空 |
| domain\_catalog | sql\_identifier | 如果该列有一个域类型，这里是该域所在的数据库名（总是当前数据库），否则为空 |
| domain\_schema | sql\_identifier | 如果该列有一个域类型，这是该域所在的模式名，否为空。 |
| domain\_name | sql\_identifier | 如果该列有一个域类型，这里是该域的名称，否则为空 |
| udt\_catalog | sql\_identifier | 该列数据类型（如果适用，底层的域类型）被定义的数库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 该列数据类型（如果适用，底层的域类型）被定义的模式名 |
| udt\_name | sql\_identifier | 该列数据类型（如果适用，底层的域类型）的名称 |
| scope\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| dtd\_identifier | sql\_identifier | 该列的数据类型描述符的一个标识符，在从属于该表的数据类型标识符之中唯一。这主要用于与这类标识符的其他实例进行连接（该标识符的指定格式没有被定义并且不保证在未来的版本中保持相同）。 |
| is\_self\_referencing | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| is\_identity | yes\_or\_no | 如果该列是一个标识列，则YES，否则为NO。 |
| identity\_generation | character\_data | 如果该列是一个标识列，则为ALWAYS或者BY DEFAULT，它反映该列的定义。 |
| identity\_start | character\_data | 如果该列是一个标识列，则内部序列的起始值，否则为空。 |
| identity\_increment | character\_data | 如果该列是一个标识列，则是内部序列的增量，否则为空。 |
| identity\_maximum | character\_data | 如果该列是一个标识列，则是内部序列的最大值，否则为空。 |
| identity\_minimum | character\_data | 如果该列是一个标识列，则是内部序列的最小值，否则为空。 |
| identity\_cycle | yes\_or\_no | 如果该列是一个标识列，则YES和NO分别表示内部序列可循环和不可循环，否则为空。 |
| is\_generated | character\_data | 如果列是生成的列，则ALWAYS，否则 NEVER。 |
| generation\_expression | character\_data | 如果列是生成的列，则生成表达式，否则为空。 |
| is\_updatable | yes\_or\_no | 如果该列是可更新的，则为YES，否则为NO（基表中的列总是可更新的，视图中的列则不一定） |

: 表 5.15 columns列

因为在 SQL 中有多种方式定义数据类型，而瀚高数据库还包含额外的方式来定义数据类型，它们在信息模式中的表示可能有点困难。列data\_type应该标识列的底层内建类型。在瀚高数据库中，这表示定义在系统目录模式pg\_catalog中的类型。如果应用能够特别地（例如以不同方式格式化数字类型或使用精度列中的数据）处理总所周知的内建类型，这列可能会有用。列udt\_name、udt\_schema和udt\_catalog总是标识列的底层数据类型，即使该列是基于一个域的（因为瀚高数据库对待内建类型和用户定义类型的方式是一样的，内建类型也出现在这里。这是 SQL 标准的一种扩展）。如果一个应用想要根据该类型以不同的方式处理数据，就应该使用这些列，因为在那种情况下即使该列真地基于一个域也没有关系。如果该列是基于一个域，该域的标识被存储在列domain\_name、domain\_schema和domain\_catalog。

如果你想要把列和它们相关的数据类型配对并且把域视作单独的类型，你可以写coalesce(domain\_name, udt\_name)等等。

## constraint\_column\_usage

视图constraint\_column\_usage标识在当前数据库中被某个约束使用的所有列。只有包含在被一个当前启用的角色拥有的表中的那些列才被显示。对于一个检查约束，这个视图标识被用在该检查约束中的列。对于一个外键约束，这个视图标识外键引用的列。对于一个唯一或主键约束，这个视图标识被约束的列。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含被某个约束使用的列的表所在的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含被某个约束使用的列的表所在的模式名 |
| table\_name | sql\_identifier | 包含被某个约束使用的列的表名 |
| column\_name | sql\_identifier | 包含被某个约束使用的列名 |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该约束的模式名 |
| constraint\_name | sql\_identifier | 约束名 |

: 表 5.16 constraint\_column\_usage列

## constraint\_table\_usage

视图constraint\_table\_usage标识在当前数据库中被某个约束使用的所有表（这与视图table\_constraints不同，它标识哪些表约束定义在哪些表上）。对于一个外键约束，这个视图标识该外键引用的表。对于一个唯一或主键约束，这个视图仅标识该约束属于的表。

检查约束和非空约束不被包括在这个视图中。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含被某个约束使用的表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含被某个约束使用的表的模式名 |
| table\_name | sql\_identifier | 包含被某个约束使用的表名 |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该约束的模式名 |
| constraint\_name | sql\_identifier | 约束名 |

: 表 5.17 constraint\_table\_usage列

## data\_type\_privileges

视图data\_type\_privileges标识当前用户能够访问（作为被描述对象的拥有者或者具有其上的某种特权）的所有数据类型描述符。只要一个数据类型被用在一个表列、一个域或一个函数（作为参数或返回类型）就会生成一个数据类型描述符并且在那个实例中存储一些有关该数据类型如何被使用的信息（例如，声明的最大长度，如果适用）。每一个数据类型描述符被赋予一个任意的标识符，它在被赋予给一个对象（表、域、函数）的数据类型描述符中唯一。这个视图对于应用可能没什么用，但是它被用于定义信息模式中的一些其他视图。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| object\_catalog | sql\_identifier | 包含该被描述对象的数据库名（总是当前数据库） |
| object\_schema | sql\_identifier | 包含该被描述对象的模式名 |
| object\_name | sql\_identifier | 该描述对象的名字 |
| object\_type | character\_data | 被描述对象的类型：TABLE（从属于表的一列的数据类型描述符）、DOMAIN （从属于域的数据类型描述符）、ROUTINE（从属于函数的一个参数或返回数据类型的数据类型描述符）。 |
| dtd\_identifier | sql\_identifier | 数据类型描述符的标识符，它在同一对象的数据类型描述符之间唯一。 |

: 表 5.18 data\_type\_privileges列

## domain\_constraints

视图domain\_constraints包含所有属于当前数据库中定义的域的约束。只有当前用户能访问的那些域才被显示（作为拥有者或具有某些特权）。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该约束的模式名 |
| constraint\_name | sql\_identifier | 约束名 |
| domain\_catalog | sql\_identifier | 包含该域的数据库名（总是当前数据库） |
| domain\_schema | sql\_identifier | 包含该域的模式名 |
| domain\_name | sql\_identifier | 该域的名称 |
| is\_deferrable | yes\_or\_no | 如果该约束是可延迟的，则为YES，否则为NO |
| initially\_deferred | yes\_or\_no | 如果该约束是可延迟的且初始就被延迟，则为YES，否则 为NO |

: 表 5.19 domain\_constraints列

## domain\_udt\_usage

视图domain\_udt\_usage标识所有基于被一个当前启用的角色拥有的数据类型的域。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| udt\_catalog | sql\_identifier | 该域数据类型被定义的数据库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 该域数据类型被定义的模式名 |
| udt\_name | sql\_identifier | 该域数据类型的名称 |
| domain\_catalog | sql\_identifier | 包含该域的数据库名（总是当前数据库） |
| domain\_schema | sql\_identifier | 包含该域的模式名 |
| domain\_name | sql\_identifier | 该域的名称 |

: 表 5.20 domain\_udt\_usage列

## domains

视图domains包含定义在当前数据库中的所有域。只有当前用户能够访问（作为拥有者或具有某些特权）的域才被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| domain\_catalog | sql\_identifier | 包含该域的数据库名（总是当前数据库） |
| domain\_schema | sql\_identifier | 包含该域的模式名 |
| domain\_name | sql\_identifier | 该域的名称 |
| data\_type | character\_data | 该域的数据类型如果是一种内建类型，这里是该域的数类型；如果是某种数组 （此种情况见视图element\_types），则为ARRAY；否则为USERDEFINED（此种情况中，该类 型被标识在udt\_name和相关列中）。 |
| character\_maximum\_length | cardinal\_number | 如果该域有一个字符或位串类型，这里是声明的最大长度；如果没有声明最大长度，则对于所有其他数据类型为空。 |
| character\_octet\_length | cardinal\_number | 如果该域有一个字符类型，这里是一个数据的最大可能长度（以字节计）；对其他所有数据类型为空。最大字节长度取决于声明的字符最大长度（见上文）和服务器编码。 |
| character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_catalog | sql\_identifier | 包含此域排序规则的数据库（总是当前数据库），如果默认或者该域的数据类型不可排序则为空 |
| collation\_schema | sql\_identifier | 包含此域排序规则的模式名，如果默认或者该域的数据类型不可排序则为空 |
| collation\_name | sql\_identifier | 该域排序规则的名称，如果默认或者该域的数据类型不可排序则为空 |
| numeric\_precision | cardinal\_number | 如果该域有一种数字类型，这列包含这个域类型的（声明的或隐式的）精度。精度指示了有效位数。它可以按照列numeric\_precision\_radix中指定的被表示为十进制（基于 10）或二进制（基于 2）。对于所有其他数据类，这一列为空。 |
| numeric\_precision\_radix | cardinal\_number | 如果该域有一种数字类型，这一列指示numeric\_precision和numeric\_scale列中的值是基于什么来表示。该值为 2 或 10。对于所有其他数据类型，这一列为空。 |
| numeric\_scale | cardinal\_number | 如果该域有一种准确数字类型，这列包含这个域类型的声明的或隐式的）比例。比例指示了有效位数。它可以按照列numeric\_precision\_radix中定的被表示为十进制（基于 10）或二进制（基于 2）。对于所有其他数据类型，这一列为空。 |
| datetime\_precision | cardinal\_number | 如果data\_type标识一种日期、时间、时间戳或时间间隔类型，这一列包含这个域型的（声明的或隐式的）分数秒的精度，也就是秒值的小数点后的十进制位数。于所有其他数据类型，这 一列为空。 |
| interval\_type | character\_data | 如果data\_type标识一种时间间隔类型，这一列包含时间间隔为这个域包括哪些域的声明，例如YEAR TO MONTH、DAY TO SECOND等等。如果没有指定域限制（也就是该时间间隔接受所有域），并且对于所有其他数据类型，这个域为空。 |
| interval\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性（关于时间间隔类型域的分数秒精度可见datetime\_precision） |
| domain\_default | character\_data | 该域的默认表达式 |
| udt\_catalog | sql\_identifier | 该域数据类型被定义的数据库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 该域数据类型被定义的模式名 |
| udt\_name | sql\_identifier | 该域数据类型的名称 |
| scope\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| maximum\_cardinality | cardinal\_number | 总是空，因为数组在瀚高数据库中总是有无限制的最大势 |
| dtd\_identifier | sql\_identifier | 该域的数据类型描述符的一标识符，在从属于该域的数据类型标识符之中唯一这不重要，因为一个域只含一个数据类型描述符）。这主要用于与这类标 识符的其他实例进行连接（该标识符的指定格式没有被定义并且不保证在未来的版本中保持相同）。 |

: 表 5.21 domains列

## element\_types

视图element\_types包含数组元素的数据类型描述符。当一个表列、组合类型属性、域、函数参数或函数返回值被定义为一种数组类型，相应的信息模式视图只在列data\_type中包含ARRAY。要获得该数组元素类型的信息，你可以连接该相应的视图和这个视图。例如，要显示一个表的列及其数据类型和数组元素类型，你可以：

SELECT c.column\_name, c.data\_type, e.data\_type AS element\_type

FROM information\_schema.columnsCLEFT JOIN information\_schema.element\_types e

ON ((c.table\_catalog, c.table\_schema, c.table\_name, 'TABLE',

c.dtd\_identifier)

\= (e.object\_catalog, e.object\_schema, e.object\_name, e.object\_type,

e.collection\_type\_identifier))

WHERE c.table\_schema = '...' AND c.table\_name = '...'

ORDER BY c.ordinal\_position;

这个视图只包括当前用户能够访问（作为拥有者或具有某些特权）的对象。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| object\_catalog | sql\_identifier | 包含使用被描述的数组的对象的数据库名（总是当前数据库） |
| object\_schema | sql\_identifier | 包含使用被描述的数组的对的模式名 |
| object\_name | sql\_identifier | 使用被描述的模式的对象名 |
| object\_type | character\_data | 使用被描述的数组的对象的类型：TABLE（被一个表列使用的数组）、USER-DEFINEDTYPE（被组合类型的一个属性使用的数组）、DOMAIN（被域使用的数组）、ROUTINE（被函数的一个参数或返回数据类型使用的数组）。 |
| collection\_type\_identifie | sql\_identifier | 被描述的数组的数据类型描述符的标识符。使用这个去与其他信息模式视图的dtd\_identifier列连接。 |
| data\_type | character\_data | 如果数组元素的数据类型是内建类型，这里是数组元素的数据类型，否则为USERDEFINED（在那种情况下，该类型被标识在udt\_name和相列中）。 |
| character\_maximum\_length | cardinal\_number | 总是为空，因为这种信息不用于瀚高数据库中的数组元素数据类型 |
| character\_octet\_length | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的数组元素数据类型 |
| character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_catalog | sql\_identifier | 包含元素类型排序规则的数据库名（总是当前数据库）,如果默认或该元素的数据类型是不可排序的则为空 |
| collation\_schema | sql\_identifier | 包含元素类型排序规则的模式名, 如果默认或该元素的数据类型是不可排序的则为空 |
| collation\_name | sql\_identifier | 元素类型的排序规则名, 如果默认或该元素的数据类型是不可排序的则为空 |
| numeric\_precision | cardinal\_number | 总是为空，因为这种信息不用于瀚高数据库中的数组元素数据类型 |
| numeric\_precision\_radix | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的数组元素数据类型 |
| numeric\_scale | cardinal\_number | 总是为空，因为这种信息不用于瀚高数据库中的数组元素数据类型 |
| datetime\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的数组元素数据类型 |
| interval\_type | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的数组元素数据类型 |
| interval\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的数组元素数据类型 |
| domain\_default | character\_data | 还未被实现 |
| udt\_catalog | sql\_identifier | 元素的数据类型所在的数据库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 元素的数据类型所在的模式名 |
| udt\_name | sql\_identifier | 模式的数据类型名 |
| scope\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| maximum\_cardinality | sql\_identifier | 总是空，因为数组在瀚高数据库中总是有无限制的最大势 |
| dtd\_identifier | sql\_identifier | 该元素的数据类型描述符的标识符。当前无用。 |

: 表 5.22 element\_types列

## enabled\_roles

视图enabled\_roles标识当前”已被启用的角色”。已被启用的角色被递归地定义为：当前用户以及被授予给具有自动继承的已被启用角色的所有角色。换句话说，就是当前用户是其直接或间接成员的所有角色。

为了权限检查，”可应用角色”的集合被应用，它会比已被启用角色的集合包含的角色范围更宽。因此通常使用视图applicable\_roles要更好，applicable\_roles视图的详情请见第 5.5 节。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| role\_name | sql\_identifier | 角色名称 |

: 表 5.23 enabled\_roles列

## foreign\_data\_wrapper\_options

视图foreign\_data\_wrapper\_options包含为当前数据库中外部数据包装器定义的所有选项。只有那些当前用户能够访问（作为拥有者或具有某些特权）的外部数据包装器被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| foreign\_data\_wrapper\_catalog | sql\_identifier | 该外部数据包装器所在的数据库名（总是当前数据库） |
| foreign\_data\_wrapper\_name | sql\_identifier | 该外部数据包装器的名字 |
| option\_name | sql\_identifier | 一个选项名 |
| option\_value | character\_data | 该选项的值 |

: 表 5.24 foreign\_data\_wrapper\_options列

## foreign\_data\_wrappers

视图foreign\_data\_wrappers包含定义在当前数据库中的所有外部数据包装器。只有那些当前用户能够访问（作为拥有者或具有某些特权）的外部数据包装器才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| foreign\_data\_wrapper\_catalog | sql\_identifier | 包含该外部数据包装器的数据库名（总是当前数据库） |
| foreign\_data\_wrapper\_name | sql\_identifier | 外部数据包装器的名字 |
| authorization\_identifier | sql\_identifier | 外部服务器拥有者的名字 |
| library\_name | character\_data | 实现这个外部数据包装器的库文件名 |
| foreign\_data\_wrapper\_language | character\_data | 用于实现这个外部数据包装器的语言 |

: 表 5.25 foreign\_data\_wrappers列

## foreign\_server\_options

视图foreign\_server\_options包含为当前数据库中外部服务器定义的所有选项。只有那些当前用户能够访问（作为拥有者或具有某些特权）的外部服务器才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| foreign\_server\_catalog | sql\_identifier | 该外部服务器所在的数据库（总是当前数据库） |
| foreign\_server\_name | sql\_identifier | 该外部服务器的名字 |
| option\_name | sql\_identifier | 一个选项名 |
| option\_value | character\_data | 该选项的值 |

: 表 5.26 foreign\_server\_options列

## foreign\_servers

视图foreign\_servers包含当前数据库中定义的所有外部服务器。只有那些当前用户能够访问（作为拥有者或具有某些特权）的外部服务器才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| foreign\_server\_catalog | sql\_identifier | 该外部服务器所在的数据库名（总是当前数据库） |
| foreign\_server\_name | sql\_identifier | 该外部服务器的名字 |
| foreign\_data\_wrapper\_catalog | sql\_identifier | 包含被该外部服务器使用的外部数据包装器的数据库名（总是当前数据库） |
| foreign\_data\_wrapper\_name | sql\_identifier | 被该外部服务器所使用的外部数据包装器的名字 |
| foreign\_server\_type | character\_data | 外部服务器类型信息（如果在创建时指定过） |
| foreign\_server\_version | character\_data | 外部服务器版本信息（如果在创建时指定过） |
| authorization\_identifier | sql\_identifier | 该外部服务器的拥有者名字 |

: 表 5.27 foreign\_servers列

## foreign\_table\_options

视图foreign\_table\_options包含为当前数据库中外部表定义的所有选项。只有那些当前用户能够访问（作为拥有者或具有某些特权）的外部表才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| foreign\_table\_catalog | sql\_identifier | 包含该外部表的数据库名（总是当前数据库） |
| foreign\_table\_schema | sql\_identifier | 包含该外部表的模式名 |
| foreign\_table\_name | sql\_identifier | 外部表的名字 |
| option\_name | sql\_identifier | 一个选项名 |
| option\_value | character\_data | 该选项的值 |

: 表 5.28 foreign\_table\_options列

## foreign\_tables

视图foreign\_tables包含定义在当前数据库中的所有外部表。只有那些当前用户能够访问（作为拥有者或具有某些特权）的外部表才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| foreign\_table\_catalog | sql\_identifier | 该外部表所在的数据库名（总是当前数据库） |
| foreign\_table\_schema | sql\_identifier | 包含该外部表的模式名 |
| foreign\_table\_name | sql\_identifier | 该外部表的名字 |
| foreign\_server\_catalog | sql\_identifier | 该外部服务器所在的数据库名（总是当前数据库） |
| foreign\_server\_name | sql\_identifier | 该外部服务器的名字 |

: 表 5.29 foreign\_tables列

## key\_column\_usage

视图key\_column\_usage标识当前数据库中所有被某种唯一、主键或外键约束限制的列。检查约束不被包括在这个视图中。只有那些当前用户能够访问的列才会被显示（作为拥有者或具有某些特权）。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该约束的模式名 |
| constraint\_name | sql\_identifier | 包含该约束的模式名 |
| table\_catalog | sql\_identifier | 约束名 |
| table\_catalog | sql\_identifier | 包含被这个约束限制的列的表所在的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含被这个约束限制的列的表所在的模式名 |
| table\_name | sql\_identifier | 包含被这个约束限制的列的表的名字 |
| column\_name | sql\_identifier | 被这个约束限制的列名 |
| ordinal\_position | cardinal\_number | 该列在约束键中的顺序位置（从 1 开始计数） |
| position\_in\_unique\_constraintcaint | cardinal\_number | 对于一个外键约束，被引用行在其唯一约束中的顺序位置（从 1 开始计数）；对于其他约束为空 |

: 表 5.30 key\_column\_usage列

## parameters

视图parameters包含当前数据库中所有函数的参数的有关信息。只有那些当前用户能够访问（作为拥有者或具有某些特权）的函数才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| specific\_catalog | sql\_identifier | 包含该函数的数据库名（总是当前数据库） |
| specific\_schema | sql\_identifier | 包含该函数的模式名 |
| specific\_name | sql\_identifier | 该函数的“专用名”。详见第 5.41 节 |
| ordinal\_position | cardinal\_number | 该参数在函数参数列表中的顺序位置（从 1 开始计数） |
| parameter\_mode | character\_data | IN表示输入参数， OUT表示输出参数， INOUT表示输入输出参数。 |
| is\_result | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| as\_locator | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| parameter\_name | sql\_identifier | 参数名，如果参数没有名称则为空 |
| data\_type | character\_data | 该参数的数据类型如果是一种内建类型，这里是该参数的数据类型；如果是某种数组（此种情况见视图element\_types），则为ARRAY；否则为USER DEFINED（此种情况中，该类型被标识在udt\_name和相关列中）。 |
| character\_maximum\_length | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| character\_octet\_length | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_catalog | sql\_identifier | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| collation\_schema | sql\_identifier | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| collation\_name | sql\_identifier | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| numeric\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| numeric\_precision\_radix | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| numeric\_scale | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| datetime\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| interval\_type | character\_data | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| interval\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| udt\_catalog | sql\_identifier | 该参数的数据类型所在的数据库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 该参数的数据类型所在的模式名 |
| udt\_name | sql\_identifier | 该参数的数据类型的名字 |
| scope\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| maximum\_cardinality | cardinal\_number | 总是空，因为数组在瀚高数据库中总是有无限制的最大势 |
| dtd\_identifier | sql\_identifier | 该参数的数据类型描述符的一个标识符，在从属于该函数的数据类型标识符之中唯一（这不重要，因为一个域只包含一个数据类型描述符）。这主要用于与这类标识符的其他实例进行连接（该标识符的指定格式没有被定义并且不保证在未来的版本中保持相同）。 |
| parameter\_default | character\_data | 该参数的默认表达式，如果没有或者该函数不被一个当前启用的角色拥有则为空值。 |

: 表 5.31 parameters列

## referential\_constraints

视图referential\_constraints包含当前数据库中的所有引用（外键）约束。只有那些当前用户具有其引用表上写权限（作为拥有者或具有某些除SELECT之外的特权）的约束才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema | sql\_identifier | 包含该约束的模式名 |
| constraint\_name | sql\_identifier | 约束名 |
| unique\_constraint\_catalog | sql\_identifier | 包含该外键约束所引用的唯一或主键约束的数据库名（总是当前数据库） |
| unique\_constraint\_schema | sql\_identifier | 包含该外键约束所引用的唯一或主键约束的模式名 |
| unique\_constraint\_name | sql\_identifier | 包含该外键约束所引用的唯一或主键约束的名字 |
| match\_option | character\_data | 外键约束的匹配选项：FULL、PARTIAL或NONE。 |
| update\_rule | character\_data | 外键约束的更新规则：CASCADE、SET NULL、SET DEFAULT、RESTRICT或NO ACTION。 |
| delete\_rule | character\_data | 外键约束的删除规则：CASCADE、SET NULL、SET DEFAULT、RESTRICT或NO ACTION。 |

: 表 5.32 referential\_constraints列

## role\_column\_grants

视图role\_column\_grants标识所有在列上授予的特权，这些特权的授予者或者被授予者是一个当前已被启用的角色。更多信息可以在column\_privileges中找到。这个视图和column\_privileges之间的唯一实质性区别是：这个视图忽略那些以授予给PUBLIC的方式使当前用户获得其访问权限的列。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee | sql\_identifier | 被授予该特权的角色名 |
| table\_catalog | sql\_identifier | 包含该列的表所在的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该列的表所在的模式名 |
| table\_name | sql\_identifier | 包含该列的表名 |
| column\_name | sql\_identifier | 列名称 |
| privilege\_type | character\_data | 特权类型：SELECT、INSERT、UPDATE或REFERENCES |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.33 role\_column\_grants列

## role\_routine\_grants

视图role\_routine\_grants标识所有在函数上授予的特权，这些特权的授予者或者被授予者是一个当前已被启用的角色。更多信息可以在routine\_privileges中找到。这个视图和routine\_privileges之间的唯一实质性区别是：这个视图忽略那些以授予给PUBLIC的方式使当前用户获得其访问权限的函数。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee |  | 被授予该特权的角色名 |
| specific\_catalog |  | 包含该函数的数据库名（总是当前数据库） |
| specific\_schema |  | 包含该函数的模式名 |
| specific\_name |  | 该函数的“专用名”。 |
| routine\_catalog |  | 包含该函数的数据库名（总是当前数据库） |
| routine\_schema |  | 包含该函数的模式名 |
| routine\_name |  | 该函数的名字（在重载的情况下可能会重复） |
| privilege\_type | character\_data | 总是为EXECUTE（函数唯一的特权类型） |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.34 role\_routine\_grants列

## role\_table\_grants

视图role\_table\_grants标识所有在表或视图上授予的特权，这些特权的授予者或者被授予者是一个当前已被启用的角色。更多信息可以在table\_privileges中找到。这个视图和table\_privileges之间的唯一实质性区别是：这个视图忽略那些以授予给PUBLIC的方式使当前用户获得其访问权限的表。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee |  | 被授予该特权的角色名 |
| table\_catalog |  | 包含该表的数据库名（总是当前数据库） |
| table\_schema |  | 包含该表的模式名 |
| table\_name |  | 表名称 |
| privilege\_type | character\_data | 该特权的类型：SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES或TRIGGER |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |
| with\_hierarchy | yes\_or\_no | 在 SQL 标准中，WITHIERARCHY OPTION是一个独立的（子）特权，它允许在表继承层级上的特定操作。在 瀚高数据库中，这被包括在SELECT特权中，因此这一列在特权为SELECT时显示YES，其他时候显示NO。 |

: 表 5.35 role\_table\_grants列

## role\_udt\_grants

视图role\_udt\_grants标识所有在用户定义类型上授予的USAGE特权，这些特权的授予者或者被授予者是一个当前已被启用的角色。更多信息可以在udt\_privileges中找到。这个视图和udt\_privileges之间的唯一实质性区别是：这个视图忽略那些以授予给PUBLIC的方式使当前用户获得其访问权限的对象。因为数据类型在瀚高数据库中并没有真正的特权，而是只有一个给PUBLIC的隐式授予，这个视图为空。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee |  | 被授予该特权的角色名 |
| object\_catalog |  | 包含该对象的数据库名（总是当前数据库） |
| object\_schema |  | 如果适用，则为包含该对象的模式名，否则为一个空字符串 |
| object\_name |  | 对象的名字 |
| object\_type | character\_data | COLLATION或DOMAIN或FOREIGN DATA WRAPPER或FOREIGN SERVER或SEQUENCE |
| privilege\_type | character\_data | 总是USAGE |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.36 role\_udt\_grants列

## role\_usage\_grants

视图role\_usage\_grants标识所有在多种对象上授予的USAGE特权，这些特权的授予者或者被授予者是一个当前已被启用的角色。更多信息可以在usage\_privileges中找到。这个视图和usage\_privileges之间的唯一实质性区别是：这个视图忽略那些以授予给PUBLIC的方式使当前用户获得其访问权限的对象。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee |  | 被授予该特权的角色名 |
| object\_catalog |  | 包含该对象的数据库名（总是当前数据库） |
| object\_schema |  | 如果适用，则为包含该对象的模式名，否则为一个空字符串 |
| object\_name |  | 对象的名字 |
| object\_type | character\_data | COLLATION或DOMAIN或FOREIGN DATA WRAPPER或FOREIGN SERVER或SEQUENCE |
| privilege\_type | character\_data | 总是USAGE |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.37 role\_usage\_grants列

## routine\_privileges

视图routine\_privileges标识所有在函数上授予的特权，其授予者或被授予者是一个当前已被启用的角色。对于每一种函数、授予者和被授予者的组合，这里都有一行。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee | sql\_identifier | 被授予该特权的角色名 |
| specific\_catalog | sql\_identifier | 包含该函数的数据库名（总是当前数据库） |
| specific\_schema | sql\_identifier | 包含该函数的模式名 |
| specific\_name | sql\_identifier | 该函数的“专用名”。详 见第 5.41 节。 |
| routine\_catalog | sql\_identifier | 包含该函数的数据库名（总是当前数据库） |
| routine\_schema | sql\_identifier | 包含该函数的模式名 |
| routine\_name | sql\_identifier | 该函数的名字（在重载的情况下可能重复） |
| privilege\_type | character\_data | 总是EXECUTE（函数唯一的特权类型） |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.38 routine\_privileges列

## routines

视图routines包含当前数据库中所有的函数和过程。只有那些当前用户能够访问（作为拥有者或具有某些特权）的函数和过程才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| specific\_catalog | sql\_identifier | 包含该函数的数据库名（总是当前数据库） |
| specific\_schema | sql\_identifier | 包含该函数的模式名 |
| specific\_name | sql\_identifier | 该函数的“专用名”。这是一个在模式中唯一标识该函数的名称，即使该函数真正的名称已经被重载。专用名的格式尚未被定义，它应当仅被用来与指定例程名称的其他实例进行比较。 |
| routine\_catalog | sql\_identifier | 包含该函数的数据库名（总是当前数据库） |
| routine\_schema | sql\_identifier | 包含该函数的模式名 |
| routine\_name | sql\_identifier | 该函数的名字（在重载的情况下可能重复） |
| routine\_type | sql\_identifier | FUNCTION表示是一个函 数，PROCEDURE表示是一个过程 |
| module\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| module\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| module\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| udt\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| udt\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| udt\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| data\_type | character\_data | 该函数的返回数据类型如果是一种内建类型，这里是该数据类型；如果是某种数组（此种情况见视图element\_types），则为ARRAY；否则为USER DEFINED（此种情况中，该类型被标识在type\_udt\_name和相关列中）。如果是过程则此项为空。 |
| character\_maximum\_length | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| character\_octet\_length | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_catalog | sql\_identifier | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| collation\_schema | sql\_identifier | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| collation\_name | sql\_identifier | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| numeric\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| numeric\_precision\_radix | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| numeric\_scale | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| datetime\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| interval\_type | character\_data | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| interval\_precision | cardinal\_number | 总是为空，因为这种信息不适用于瀚高数据库中的返回数据类型 |
| type\_udt\_catalog | sql\_identifier | 该函数的返回数据类型所在的数据库名（总是当前数据库）。如果是过程则此项为空。 |
| type\_udt\_schema | sql\_identifier | 该函数的返回数据类型所在的模式名。如果是过程则此项为空。 |
| type\_udt\_name | sql\_identifier | 该函数的返回数据类型的名字。如果是过程则此项为空。 |
| scope\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| scope\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| maximum\_cardinality | cardinal\_number | 总是空，因为数组在瀚高数据库中总是有无限制的最大势 |
| dtd\_identifier | sql\_identifier | 该函数返回数据类型的数据类型描述符的一个标识符，在从属于该函数的数据类型标识符之中唯一。这主要用于与这类标识符的其他实例进行连接（该标识符的指定格式没有被定义并且不保证在未来的版本中保持相同）。 |
| routine\_body | character\_data | 如果该函数是一个 SQL 函数，则为SQL，否则为EXTERNAL |
| routine\_definition | character\_data | 该函数的源文本（如果该函数不属于一个当前已被启用的角色，则为空）。（根据 SQL 标准，只有routine\_body为SQL时这一列才适用。但是在瀚高数据库中，它将会包含该函数被创建时所指定的任何源文本。） |
| external\_name | character\_data | 如果这个函数是一个C函数，则为该函数的外部名称（链接符号），否则为空（这会产生和显示在routine\_definition中相同的值）。 |
| external\_language | character\_data | 该函数所用的语言 |
| parameter\_style | character\_data | 总是GENERAL（SQL 标准定义了其他参数风格，但在瀚高数据库中不可用） |
| is\_deterministic | yes\_or\_no | 如果该函数被声明为不变（在 SQL 标准中被称为确定性的），则为YES，否则为NO（你不能通过该信息模式查询在瀚高数据库中可用的其他易变级别）。 |
| sql\_data\_access | character\_data | 总是MODIFIES，表示该函数 可能修改 SQL 数据。这种信息对瀚高数据库没有用处。 |
| is\_null\_call | yes\_or\_no | 如果该函数在任一参数为空时自动返回空值，则为YES，否则为NO。如果是过程则此项为空。 |
| sql\_path | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| schema\_level\_routine | yes\_or\_no | 总是YES（反例是一个用户定义类型的方法，这是在 瀚高数据库不可用的一种特性）。 |
| max\_dynamic\_result\_sets | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| is\_user\_defined\_cast | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| is\_implicitly\_invocable | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| security\_type | character\_data | 如果该函数以当前用户的特权运行，则为INVOKER；如果该函数以定义它的用户的特权运行，则为DEFINER。 |
| to\_sql\_specific\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| to\_sql\_specific\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| to\_sql\_specific\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| as\_locator | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| created | time\_stamp | 应用于一个瀚高数据库中不可用的特性 |
| last\_altered | time\_stamp | 应用于一个瀚高数据库中不可用的特性 |
| new\_savepoint\_level | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| is\_udt\_dependent | yes\_or\_no | 当前总是NO。另一个选项YES应用于一个瀚高数据库中不可用的特性。 |
| result\_cast\_from\_data\_type | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_as\_locator | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_char\_max\_length | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_char\_octet\_length | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_char\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_char\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_char\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_collation\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_collation\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_collation\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_numeric\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_numeric\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_numeric\_scale | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_datetime\_precision | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_interval\_type | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_interval\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_type\_udt\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_type\_udt\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_type\_udt\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_scope\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_scope\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_scope\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_maximum\_cardinality | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| result\_cast\_dtd\_identifier | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |

: 表 5.39 routines列

## schemata

视图schemata包含当前数据库中被当前用户（作为属主或具有某些特权）可访问的所有模式。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| catalog\_name | sql\_identifier | 该模式所在的数据库名（总是当前数据库） |
| schema\_name | sql\_identifier | 该模式的名称 |
| schema\_owner | sql\_identifier | 该模式拥有者的名称 |
| default\_character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| default\_character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| default\_character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| sql\_path | character\_data | 应用于一个瀚高数据库中不可用的特性 |

: 表 5.40 schemata列

## sql\_features

表sql\_features包含的信息指示了哪些 SQL 标准中定义的正式特性被瀚高数据库所支持。这和附录 D中的信息一样。这里你也能找到一些额外的背景信息。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| feature\_id | character\_data | 该特性的标识符字符串 |
| feature\_name | character\_data | 该特性的描述性名称 |
| sub\_feature\_id | character\_data | 该子特性的标识符字符串，或者如果不是一个子特性则为一个长度为零的字符串 |
| sub\_feature\_name | character\_data | 该子特性的描述性名称，或者如果不是一个子特性则为一个长度为零的字符串 |
| is\_supported | yes\_or\_no | 如果该特性被当前版本的瀚高数据库完全支持，则为YES，否则为NO |
| is\_verified\_by | character\_data | 总是为空，因为瀚高数据库开发组没有对特性的一致性执行正式的测试 |
| comments | character\_data | 可能会是关于该特性被支持状态的一段注释 |

: 表 5.41 sql\_features列

## sql\_implementation\_info

表sql\_implementation\_info包含的信息指示剩下的由 SQL 标准实现定义的多个方面。这类信息主要用来在 ODBC 接口的情境中使用；其它接口的用户可能将发现这类信息用处不大。

由于这个原因，个体实现信息项没有在这里描述，你将会在 ODBC 接口的描述中找到它们。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| implementation\_info\_id | character\_data | 该实现信息项的标识符字符串 |
| implementation\_info\_name | character\_data | 该实现信息项的描述性名称 |
| integer\_value | cardinal\_number | 该实现信息项的值，如果该值被包含在character\_value列中则为空 |
| character\_value | character\_data | 该实现信息项的值，如果该值被包含在integer\_value列中则为空 |
| comments | character\_data | 可能是从属于该实现信息项的一段注释 |

: 表 5.42 sql\_implementation\_info列

## sql\_languages

表sql\_languages为每一种被瀚高数据库支持的 SQL 语言绑定包含一行。瀚高数据库支持在C中的直接 SQL 和嵌入式 SQL，这是你从这张表中知道的所有东西。

这个表在 SQL:2008 中已被从 SQL 标准中移除，因此这里没有项引用 SQL:2003 之后的标准。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| sql\_language\_source | character\_data | 该语言定义的源名称，总是ISO 9075，即 SQL 标准 |
| sql\_language\_year | character\_data | sql\_language\_source中引用的标准被通过的年份。 |
| sql\_language\_conformance | character\_data | 该语言绑定的标准一致性级别。对于 ISO 9075:2003 总是CORE。 |
| sql\_language\_integrity | character\_data | 总是为空（这个值与一个早期版本的 SQL 标准相关）。 |
| sql\_language\_implementation | character\_data | 总是为空 |
| sql\_language\_binding\_style | character\_data | 语言绑定风格，为DIRECT或EMBEDDED |
| sql\_language\_programming\_language | character\_data | 如果绑定风格为EMBEDDED，则为编程语言，否则为空。瀚高数据库仅支持C语言。 |

: 表 5.43 sql\_languages列

## sql\_packages

表sql\_packages包含的信息指示哪些定义在 SQL 标准中的特性包被瀚高数据库支持。特性包上的背景信息可参考附录 D。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| feature\_id | character\_data | 该包的标识符字符串 |
| feature\_name | character\_data | 该包的描述性名称 |
| is\_supported | yes\_or\_no | 如果该包被当前版本的瀚高数据库支持，则为YES，否则为NO |
| is\_verified\_by | character\_data | 总是为空，因为瀚高数据库开发组没有对特性的一致性执行正式的测试 |
| comments | character\_data | 可能会是关于该包被支持状态的一段注释 |

: 表 5.44 sql\_packages列

## sql\_parts

表sql\_parts包含的信息指示哪些定义在 SQL 标准中的部分被瀚高数据库支持。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| feature\_id | character\_data | 包含该部分编号的一个标识符字符串 |
| feature\_name | character\_data | 该部分的描述性名称 |
| is\_supported | yes\_or\_no | 如果当前版本的瀚高数据库完全支持该部分，则为YES，否则为NO |
| is\_verified\_by | character\_data | 总是为空，因为瀚高数据库开发组没有对特性的一致性执行正式的测试 |
| comments | character\_data | 可能会是关于该部分被支持状态的一段注释 |

: 表 5.45 sql\_parts列

## sql\_sizing

表sql\_sizing包含有关瀚高数据库中多种尺寸限制和最大值的信息。这类信息主要用来在 ODBC 接口的情境中使用；其它接口的用户可能将发现这类信息用处不大。由于这个原因，个体实现信息项没有在这里描述，你将会在 ODBC 接口的描述中找到它们。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| sizing\_id | cardinal\_number | 该尺寸项的标识符 |
| sizing\_name | character\_data | 该尺寸项的描述性名称 |
| supported\_value | cardinal\_number | 尺寸项的值，如果尺寸是不受限制或不能确定的则为 0， 如果尺寸项适用的特性不受支持则为空 |
| comments | character\_data | 可能是从属于尺寸项的一段注释 |

: 表 5.46 sql\_sizing列

## sequences

视图sequences包含所有定义在当前数据库中的序列。只有那些当前用户能够访问（作为拥有者或具有某些特权）的序列才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| sequence\_catalog | sql\_identifier | 包含该序列的数据库名（总是当前数据库） |
| sequence\_schema | sql\_identifier | 包含该序列的模式名 |
| sequence\_name | sql\_identifier | 该序列的名字 |
| data\_type | character\_data | 该序列的数据类型。 |
| numeric\_precision | cardinal\_number | 这列包含这个序列数据类型（见上文）的（声明的或隐式的）精度。精度指示了有效位数。它可以按照列numeric\_precision\_radix中指定的被表示为十进制（基于 10）或二进制（基于2）。 |
| numeric\_precision\_radix | cardinal\_number | 这一列指示numeric\_precision和numeric\_scale列中的值是基于什么来表示。该值为 2 或 10。 |
| numeric\_scale | cardinal\_number | 这列包含这个序列数据类型（见上文）的（声明的或隐式的）比例。比例指示了有效位数。它可以按照列numeric\_precision\_radix中指定的被表示为十进制（基于 10）或二进制（基于 2）。 |
| start\_value | character\_data | 该序列的开始值 |
| minimum\_value | character\_data | 该序列的最小值 |
| maximum\_value | character\_data | 该序列的最大值 |
| increment | character\_data | 该序列的增量 |
| cycle\_option | yes\_or\_no | 如果该序列会循环，则为YES，否则为NO |

: 表 5.47 sequences列

注意依照 SQL 标准，开始值、最小值、最大值和增量值被作为字符串返回。

## sql\_sizing\_profiles

表sql\_sizing\_profiles包含有关 SQL 标准的多种 profile 所需的sql\_sizing值的信息。瀚高数据库不追踪任何 SQL profile，因此这个表为空。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| sizing\_id | cardinal\_number | 该尺寸项的标识符 |
| sizing\_name | character\_data | 该尺寸项的描述性名称 |
| profile\_id | character\_data | 一个 profile 的标识符字符串 |
| required\_value | cardinal\_number | 该 SQL profile 对尺寸项要求的值，如果该 profile对尺寸项没有限制则为 0，如果该 profile 不要求该尺寸项所适用的任何特性则为空 |
| comments | character\_data | 可能是从属于该 profile 中尺寸项的一段注释 |

: 表 5.48 sql\_sizing\_profiles列

## table\_constraints

视图table\_constraints包含属于特定表的所有约束，这些表要满足的条件是：当前用户拥有表或者是当前用户在表上具有某种除SELECT之外的特权。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| constraint\_catalog | sql\_identifier | 包含该约束的数据库名（总是当前数据库） |
| constraint\_schema |  | 包含该约束的模式名 |
| constraint\_name |  | 约束名 |
| table\_catalog |  | 包含该表的数据库名（总是当前数据库） |
| table\_schema |  | 包含该表的模式名 |
| table\_name |  | 表名称 |
| constraint\_type | character\_data | 该约束的类型：CHECK、FOREIGN KEY、PRIMARY KEY或UNIQUE |
| is\_deferrable | yes\_or\_no | 如果该约束是可延迟的，则为YES，否则为NO |
| initially\_deferred | yes\_or\_no | 如果该约束是可延迟的并且是初始已被延迟，则为YES，否则为NO |
| enforced | yes\_or\_no | 适用于一种瀚高数据库中不可用的特性（当前总是YES） |

: 表 5.49 table\_constraints列

## table\_privileges

视图table\_privileges标识在表或视图上所有被授予的特权，这些特权必须是被一个当前已被启用角色授出或者被授予给一个当前已被启用角色。对每一个表、授予者和被授予者的组合都有一行。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee | sql\_identifier | 被授予该特权的角色名 |
| table\_catalog | sql\_identifier | 包含该表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该表的模式名 |
| table\_name | sql\_identifier | 表名称 |
| privilege\_type | character\_data | 特权类型：SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES或TRIGGER |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |
| with\_hierarchy | yes\_or\_no | 在 SQL 标准中，WITH IERARCHY OPTION是一个独立的（子）特权，它允许在表继承层级上的特定操作。在 瀚高数据库中，这被包括在SELECT特权中，因此这一列在特权为SELECT时显示YES，其他时候显示NO。 |

: 表 5.50 table\_privileges列

## tables

视图tables包含定义在当前数据库中的所有表和视图。只有那些当前用户能够访问（作为拥有者或具有某些特权）的表和视图才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含该表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该表的模式名 |
| table\_name | sql\_identifier | 表名称 |
| table\_type | character\_data | 该表的类型：BASE TABLE表示一个持久的基本表（常见表类型），VIEW表示一个视图，FOREIGN表示一个外部表，LOCAL TEMPORARY表示一个临时表 |
| self\_referencing\_column\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| reference\_generation | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| user\_defined\_type\_catalog | sql\_identifier | 如果该表是一个有类型的表，则是包含其底层数据类型的数据库名（总是当前数据库），否则为空。 |
| user\_defined\_type\_schema | sql\_identifier | 如果该表是一个有类型的表，则是包含其底层数据类型的模式名，否则为空。 |
| user\_defined\_type\_name | sql\_identifier | 如果该表是一个有类型的表，则是其底层数据类型的名称，否则为空。 |
| is\_insertable\_into | yes\_or\_no | 如果该表能够被插入，则为YES，否则为NO（基本表总是能被插入，而视图则不一定）。 |
| is\_typed | yes\_or\_no | 如果该表是一个有类型的表，则为YES，否则为NO |
| commit\_action | character\_data | 还未被实现 |

: 表 5.51 tables列

## transforms

视图transforms包含定义在当前数据库中的转换的信息。更准确 来说， 包含在转换中的每一个函数（”FROM SQL”或者 “TO SQL”函数）在其中都有一行。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| udt\_catalog | sql\_identifier | 包含该转换所适用类型的数据库的名称（总是当前数据库） |
| udt\_schema |  | 包含该转换所适用类型的模式的名称 |
| udt\_name |  | 该转换所适用类型的名称 |
| specific\_catalog |  | 包含该函数的数据库的名称（总是当前数据库） |
| specific\_schema |  | 包含该函数的模式的名称 |
| specific\_name |  | 该函数的“专用名”。更多信息请见第 5.41 节。 |
| group\_name |  | SQL 标准允许在“组”中定义转换，并且在运行时选择一个 组。瀚高数据库不支持这种做法，转换是与一种语言相关的。作为一种折衷， 这个域包含该转换所适用的语言。 |
| transform\_type | character\_data | FROM SQL或者TO SQL |

: 表 5.52 transforms 列

## triggered\_update\_columns

对于当前数据库中指定一个列列表（如UPDATE OF column1, column2）的触发器，视图triggered\_update\_columns标识这些列。没有指定一个列列表的触发器不被包括在这个视图中。只有那些当前用户拥有或具有某种除SELECT之外特权的列才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| trigger\_catalog | sql\_identifier | 包含该触发器的数据库名 是当前数据库） |
| trigger\_schema | sql\_identifier | 包含该触发器的模式名 |
| trigger\_name | sql\_identifier | 该触发器的名称 |
| event\_object\_catalog | sql\_identifier | 包含触发器所在的表的数据库名（总是当前数据库） |
| event\_object\_schema | sql\_identifier | 包含触发器所在的表的模式名 |
| event\_object\_table | sql\_identifier | 触发器所在的表的名称 |
| event\_object\_column | sql\_identifier | 触发器所在的列的名称 |

: 表 5.53 triggered\_update\_columns列

## triggers

视图triggers包含所有定义在当前数据库中表和视图上的触发器，并且只显示当前用户拥有的触发器或者是当前用户在其上具有某种除SELECT之外特权的触发器。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| trigger\_catalog | sql\_identifier | 包含该触发器的数据库名总是当前数据库） |
| trigger\_schema | sql\_identifier | 包含该触发器的模式名 |
| trigger\_name | sql\_identifier | 该触发器的名称 |
| event\_manipulation | sql\_identifier | 触发该触发器的事件 （INSERT、 UPDATE或DELETE） |
| event\_object\_catalog | sql\_identifier | 包含触发器所在的表的数据库名（总是当前数据库） |
| event\_object\_schema | sql\_identifier | 包含该触发器所在的表的模式名 |
| event\_object\_table | sql\_identifier | 该触发器所在的表的名称 |
| action\_order | cardinal\_number | 同一个表上具有相同event\_manipulation、action\_timing和active触发器之间的触发顺序。在 瀚高数据库中，触发器按照名称顺序被触发，因此这一列会反映这种规则。 |
| action\_condition | character\_data | 触发器的WHEN条件，如果没有则为空（如果该表不被一个当前已启用角色拥有也是为空） |
| action\_statement | character\_data | 触发器的WHEN条件，如果没有则为空（如果该表不被一个当前已启用角色拥有也是为空） |
| action\_orientation | character\_data | 标识触发器是对每个被处理的行触发一次还是为每个语句触发一次（ROW或STATEMENT） |
| action\_timing | character\_data | 触发器在什么时候触发 （BEFORE、 AFTER或INSTEAD OF） |
| action\_reference\_old\_table | sql\_identifier | “旧”传递表的名称，如果没有则为空 |
| action\_reference\_new\_table | sql\_identifier | “新”传递表的名称，如果没有则为空 |
| action\_reference\_old\_row | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| action\_reference\_new\_row | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| created | time\_stamp | 应用于一个瀚高数据库中不可用的特性 |

: 表 5.54 triggers列

瀚高数据库中的触发器有两点与 SQL 标准不兼容，这会影响在该信息模式中的表示。第一，在数据库中触发器的名字是局限于每个表的，而不是独立于模式对象。因此可能在一个模式中会有重复的触发器名称，只要它们属于不同的表（trigger\_catalog和trigger\_schema才真正标识了触发器被定义在哪个表上）。第二，在数据库中触发器可以被定义为在多个事件上触发（例如ON INSERT OR UPDATE），而在SQL 标准中只允许一个。如果一个触发器被定义为在多个事件上触发，它在信息模式中被表示为多行，每一行对应于一类事件。作为这两个问题的结果，视图triggers的主键实际上是(trigger\_catalog, trigger\_schema, event\_object\_table, trigger\_name, event\_manipulation)，而不是(trigger\_catalog, trigger\_schema, trigger\_name)（这是 SQL 标准指定的）。尽管如此，如果你以符合 SQL 标准（在模式中触发器名称唯一并且每个触发器只能有一种事件类型）的方式定义你的触发器，这将不会影响你。

## dt\_privileges

视图udt\_privileges标识所有在用户定义类型上授予的

USAGE特权，这些特权的授予者或者被授予者是一个当前已被启用的角色。 对每一个类型、授予者和被授予者的组合都有一行。这个视图只显示组合类型（原因见下面的 第 5.59 节）。 域特权见第 5.58 节。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee | sql\_identifier | 被授予该特权的角色名 |
| udt\_catalog | sql\_identifier | 包含该类型的数据库名（总是当前数据库） |
| udt\_schema | sql\_identifier | 包含该类型的模式名 |
| udt\_name | sql\_identifier | 该类型的名字 |
| privilege\_type | character\_data | 总是TYPE USAGE |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.55 udt\_privileges列

## usage\_privileges

视图usage\_privileges标识所有在多种对象上授予的USAGE特权，这些特权的授予者或者被授予者是一个当前已被启用的角色。在数据库中，这当前适用于排序规则、域、外部数据包装器、外部服务器和序列。对每一个对象、授予者和被授予者都有一行。

由于在瀚高数据库中排序规则并没有真正的特权，这个视图对所有排序规则显示由拥有者授予给PUBLIC的隐式非可授予的USAGE特权。但是对其他对象类型则显示真实的特权。

在数据库中，序列也支持除USAGE之外的SELECT和UPDATE特权。这些是非标准的并且因此在该信息模式中不可见。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| grantor | sql\_identifier | 授予该特权的角色名 |
| grantee | sql\_identifier | 被授予该特权的角色名 |
| object\_catalog | sql\_identifier | 包含该对象的数据库名（总是当前数据库） |
| object\_schema | sql\_identifier | 如果适用，则是包含该对象的模式名，否则为一个空字符串 |
| object\_name | sql\_identifier | 该对象的名称 |
| object\_type | character\_data | COLLATION或DOMAIN或FOREIGN DATA WRAPPER或FOREIGN SERVER或SEQUENCE |
| privilege\_type | character\_data | 总是USAGE |
| is\_grantable | yes\_or\_no | 如果该特权是可授予的，则为YES，否则为NO |

: 表 5.56 usage\_privileges列

## user\_defined\_types

视图user\_defined\_types目前包含定义在当前数据库中的所有组合类型。只有那些当前用户能够访问（作为拥有者或具有某些特权）的类型才会被显示。

SQL 知道两种用户定义类型：结构类型（在瀚高数据库中也被称为组合类型）以及独特类型（在瀚高数据库中没有实现）。要经得起未来的考验，请使用列user\_defined\_type\_category来区分它们。其他用户定义类型如基类型和枚举（都是数据库的扩展）不会被显示在这里。对于域，请见第 5.23 节。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| user\_defined\_type\_catalog | sql\_identifier | 包含该类型的数据库名（总是当前数据库） |
| user\_defined\_type\_schema | sql\_identifier | 包含该类型的模式名 |
| user\_defined\_type\_name | sql\_identifier | 该类型的名字 |
| user\_defined\_type\_category | character\_data | 当前总是STRUCTURED |
| is\_instantiable | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| is\_final | yes\_or\_no | 应用于一个瀚高数据库中不可用的特性 |
| ordering\_form | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| ordering\_category | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| ordering\_routine\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| ordering\_routine\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| ordering\_routine\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| reference\_type | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| data\_type | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| character\_maximum\_length | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| character\_octet\_length | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| character\_set\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_catalog | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_schema | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| collation\_name | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| numeric\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| numeric\_precision\_radix | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| numeric\_scale | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| datetime\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| interval\_type | character\_data | 应用于一个瀚高数据库中不可用的特性 |
| interval\_precision | cardinal\_number | 应用于一个瀚高数据库中不可用的特性 |
| source\_dtd\_identifier | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |
| ref\_dtd\_identifier | sql\_identifier | 应用于一个瀚高数据库中不可用的特性 |

: 表 5.57 user\_defined\_types列

## user\_mapping\_options

视图user\_mapping\_options包含在当前数据库中为用户映射定义的所有选项。只有那些当前用户能够访问其相应外部服务器（作为拥有者或具有某些特权）的用户映射才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| authorization\_identifier | sql\_identifier | 被映射的用户名，如果映射是公共的则为PUBLIC |
| foreign\_server\_catalog | sql\_identifier | 这个映射所使用的外部服务器所在的数据库名（总是当前数据库） |
| foreign\_server\_name | sql\_identifier | 这个映射所使用的外部服务器的名称 |
| option\_name | sql\_identifier | 一个选项名 |
| option\_value | character\_data | 选项的值。除非当前用户是被映射的用户或者映射是PUBLIC的并且当前用户是服务器拥有者或者超级用户，这一列将显示为空。这样做的目的是保护作为用户映射选项存储的口令信息。 |

: 表 5.58 user\_mapping\_options列

## user\_mappings

视图user\_mappings包含定义在当前数据库中的所有用户映射。只有当前用户能够访问其对应外部服务器（作为拥有者或具有某些特权）的用户映射才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| authorization\_identifier | sql\_identifier | 被映射的用户名，如果映射是公共的则为PUBLIC |
| foreign\_server\_catalog | sql\_identifier | 这个映射所使用的外部服务器所在的数据库名（总是当前数据库） |
| foreign\_server\_name | sql\_identifier | 这个映射所使用的外部服务器的名称 |

: 表 5.59 user\_mappings列

## view\_column\_usage

视图view\_column\_usage标识被使用在一个视图的查询表达式（定义该视图的SELECT语句）中的所有列。只有当包含一列的表被一个当前已被启用角色拥有时，该列才会被包括在这个视图中。

| 注意： |
| --- |
| 系统表列不被包括。在某个时候这应该会被修复。 |

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| view\_catalog | sql\_identifier | 包含该视图的数据库名（总是当前数据库） |
| view\_schema | sql\_identifier | 包含该视图的模式名 |
| view\_name | sql\_identifier | 该视图的名称 |
| table\_catalog | sql\_identifier | 被视图所使用的列所属表的数据库名（总是当前数据库） |
| tableschema | sql\_identifier | 被视图所使用的列所属表的模式名 |
| table\_name | sql\_identifier | 被视图所使用的列所属表的名称 |
| column\_name | sql\_identifier | 被该视图所使用的列名 |

: 表 5.60 view\_column\_usage列

## view\_routine\_usage

视图view\_routine\_usage标识被使用在一个视图的查询表达式（定义该视图的SELECT语句）中的所有例程（函数和过程）。只有被一个当前已被启用角色拥有的例程才会被包括在这个视图中。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含该视图的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该视图的模式名 |
| table\_name | sql\_identifier | 该视图的名称 |
| specific\_catalog | sql\_identifier | 包含该函数的数据库名（总是当前数据库） |
| specific\_schema | sql\_identifier | 包含该函数的模式名 |
| specific\_name | sql\_identifier | 该函数的“专用名”。详 见第5.41 节。 |

: 表 5.61 view\_routine\_usage列

## view\_table\_usage

视图view\_table\_usage标识被使用在一个视图的查询表达式（定义该视图的SELECT语句）中的所有表。只有被一个当前已被启用角色拥有的表才会被包括在这个视图中。

| 注意： |
| --- |
| 系统表没有被包括。这应当会在某个时候被修复。 |

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| view\_catalog | sql\_identifier | 包含该视图的数据库名（总是当前数据库） |
| view\_schema | sql\_identifier | 包含该视图的模式名 |
| view\_name | sql\_identifier | 该视图的名称 |
| table\_catalog | sql\_identifier | 包含被该视图所使用的表的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含被该视图所使用的表的模式名 |
| table\_name | sql\_identifier | 包含被该视图所使用的表的名称 |

: 表 5.62 view\_table\_usage列

## views

视图views包含定义在当前数据库中的所有视图。只有当前用户能够访问（作为拥有者或具有某些特权）的视图才会被显示。

| **名称** | **数据类型** | **描述** |
| --- | --- | --- |
| table\_catalog | sql\_identifier | 包含该视图的数据库名（总是当前数据库） |
| table\_schema | sql\_identifier | 包含该视图的模式名 |
| table\_name | sql\_identifier | 该视图的名称 |
| view\_definition | character\_data | 定义视图的查询表达式（如果该视图不被一个当前已被启用角色拥有则为空） |
| check\_option | character\_data | CASCADED 或 LOCAL 如果视图上有CHECK OPTION 定义,如果没有则为NONE。 |
| is\_updatable | yes\_or\_no | 如果该视图是可更新的（允许UPDATE和DELETE），则为YES，否则为NO |
| is\_insertable\_into | yes\_or\_no | 如果该视图是可插入的（允许INSERT），则为YES，否则为NO |
| is\_trigger\_updatable | yes\_or\_no | 如果该视图上有一个INSTEAD OF UPDATE触发器，则为YES，否则为NO |
| is\_trigger\_deletable | yes\_or\_no | 如果该视图上有一个INSTEAD OF DELETE触发器，则为YES，否则为NO |
| is\_trigger\_insertable\_into | yes\_or\_no | 如果该视图上有一个INSTEAD OF INSERT触发器，则为YES，否则为NO |

表 5.63 views列