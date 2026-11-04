---
title: Merge
book: "Oracle兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compOracle13.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-oracle
---

## Merge

## 说明

### INTO 子句

使用INTO子句指定要更新或插入得target表或视图，为了将数据merge到一个视图中，这个视图必须是可更新的。

### 目标视图的限制

不能指定在其上定义了INSTEAD OF触发器的目标视图

### USING 子句

使用USING子句指定要更新或插入的源

### ON 子句

使用 ON 子句指定 MERGE 操作更新或插入的条件，对于目标表中搜索条件为真的每一行，数据库使用来自源的相应数据更新该行。 如果任何行的条件都不为真，则数据库根据相应的源行插入到目标表中。

### MERGE\_UPDATE\_CLAUSE

merge\_update\_clause 指定目标表或视图的新列值。如果 ON 子句的条件为真，将执行此更新。如果执行了更新子句，则激活目标表上定义的所有更新触发器。

如果数据库仅在指定条件为真时执行更新操作，请指定 where\_clause。条件可以引用数据源或目标表。如果条件不成立，则数据库在将行合并到表时跳过更新操作。

指定 DELETE where\_clause 以在填充或更新表时清理表中的数据。 受此子句影响的唯一行是目标表中由合并操作更新的那些行。 DELETE WHERE 条件评估更新后的值，而不是由 UPDATE SET … WHERE 条件评估的原始值。 如果目标表的一行满足 DELETE 条件但不包含在 ON 子句定义的连接中，则不删除。目标表上定义的任何删除触发器都将为每次删除行激活。

可以单独指定此子句，或与 merge\_insert\_clause 一起。如果同时指定两者，则它们可以按任意顺序排列。

**merge\_update\_clause 的限制**

merge\_update\_clause 子句受以下限制：

- 不能更新在ON条件子句中引用的列
- 更新视图时不能指定DEFAULT

### MERGE\_INSERT\_CLAUSE

如果 ON 子句的条件为假，merge\_insert\_clause 指定要插入到目标表列中的值。 如果执行插入子句，则激活目标表上定义的所有插入触发器。 如果在 INSERT 关键字之后省略列列表，则目标表中的列数必须与 VALUES 子句中的值数匹配。

要将所有源行插入表中，可以在 ON 子句条件中使用常量过滤谓词。 一个常量过滤谓词的例子是 ON (0=1)。 数据库识别这样的谓词并将所有源行无条件插入到表中。这种方法与省略 merge\_update\_clause 不同。在这种情况下，数据库仍然必须执行连接。使用常量过滤谓词，不执行连接。

如果希望数据库仅在指定条件为真时执行插入操作，请指定where\_clause。条件只能引用数据源列。数据库跳过条件不成立的所有行的插入操作。

可以单独指定merge\_insert\_clause或使用merge\_update\_clause。如果同时指定两者，则它们可以按任意顺序排列。

**merge\_insert\_clause的限制**

插入视图时不能指定DEFAULT

### SIMPLE\_EXPRESSION

指定要用作语句标记的值，以便可以在错误记录表中识别来自该语句的错误。表达式可以是文本文字、数字文字或通用SQL表达式，例如绑定变量。如果将函数表达式转换为文本文字，也可以使用函数表达式——例如，TO\_CHAR(SYSDATE)。

### REJECT LIMIT

此子句允许指定一个整数作为在语句终止和回滚语句所做的任何更改之前要记录的错误数的上限。默认拒绝限制为零，对于并行DML操作，拒绝限制适用于每个并行服务器。

### DML错误记录的限制

1. 以下情况会导致语句失败并在不调用错误日志记录功能的情况下回滚：
2. 违反延迟约束
3. 任何引发唯一约束或索引违规的直接路径的INSERT或MERGE操作
4. 任何引发唯一约束或索引违规的UPDATE或MERGE操作
5. 无法在错误记录表中跟踪LONG、LOB或对象类型列的错误。但是，作为DML操作目标的表可以包含这些类型的列。
6. 如果创建或修改相应的错误记录表以使其包含不受支持类型的列，并且如果该列的名称对应于目标DML表中不受支持的列，则DML语句在解析时失败
7. 如果错误记录表不包含任何不受支持的列类型，则将记录所有DML错误，直到达到错误的拒绝限制。对于发生错误的行，错误记录表中对应列的列值与控制信息一起记录

## 示例

创建所需要的测试表：

CREATE TABLE people\_source (

person\_id INTEGER NOT NULL PRIMARY KEY,

first\_name VARCHAR(20) NOT NULL,

last\_name VARCHAR(20) NOT NULL,

title VARCHAR(10) NOT NULL

);

CREATE TABLE people\_target (

person\_id INTEGER NOT NULL PRIMARY KEY,

first\_name VARCHAR(20) NOT NULL,

last\_name VARCHAR(20) NOT NULL,

title VARCHAR(10) NOT NULL

);

INSERT INTO people\_target VALUES (1, ‘John’, ‘Smith’, ‘Mr’);

INSERT INTO people\_target VALUES (2, ‘alice’, ‘jones’, ‘Mrs’);

INSERT INTO people\_target VALUES (3, ‘tony’, ‘james’, ‘Mr’);

INSERT INTO people\_source VALUES (2, ‘Alice’, ‘Jones’, ‘Mrs.’);

INSERT INTO people\_source VALUES (3, ‘Jane’, ‘Doe’, ‘Miss’);

INSERT INTO people\_source VALUES (4, ‘Dave’, ‘Brown’, ‘Mr’);

1. **MATCHED THEN UPDATE**

以下语句使用 person\_id 列比较 people\_target 和 people\_source 的内容，当 people\_source 表中存在匹配项时，people\_target 表中的值会更新。

MERGE INTO people\_target pt

USING people\_source ps

ON (pt.person\_id = ps.person\_id)

WHEN MATCHED THEN UPDATE

SET pt.first\_name = ps.first\_name,

pt.last\_name = ps.last\_name,

pt.title = ps.title;

1. **MATCHEND THEN UPDATE 带上WHERE过滤条件**

示例2同示例1类似，但在UPDATE语句中带上了WHERE 过滤条件。

MERGE INTO people\_target pt

USING people\_source ps

ON (pt.person\_id = ps.person\_id)

WHEN MATCHED THEN UPDATE

SET pt.first\_name = ps.first\_name,

pt.last\_name = ps.last\_name,

pt.title = ps.title

where pt.title = ‘Mrs’;

1. **MATCHED THEN UPDATE 附加 DELETE语句**

MERGE INTO people\_target pt

USING people\_source ps

ON (pt.person\_id = ps.person\_id)

WHEN MATCHED THEN UPDATE

SET pt.first\_name = ps.first\_name,

pt.last\_name = ps.last\_name,

pt.title = ps.title

DELETE where pt.title = ‘Mrs.’;

1. **NOT MATCHED THEN INSERT**

此语句使用 person\_id 列比较 people\_target 和 people\_source 表的内容，people\_target表中的值仅在 people\_source 表中没有匹配项时更新：

MERGE INTO people\_target pt

USING people\_source ps

ON (pt.person\_id = ps.person\_id)

WHEN NOT MATCHED THEN INSERT

(pt.person\_id, pt.first\_name, pt.last\_name, pt.title)

VALUES (ps.person\_id, ps.first\_name, ps.last\_name, ps.title);

注：需要提前设置环境变量，set ivorysql.insert\_enable\_alias to on;

1. **MATCHED UPDATE和NOT MATCHED INSERT组合**

以下语句使用 person\_id 列比较 people\_target 和 people\_source 表的内容，并有条件地插入和更新 people\_target 表中的数据。对于people\_source 表中的每个匹配行，将使用 people\_source 表中的值更新 people\_target 表中的值。people\_source 表中任何不匹配的行都将添加到 people\_target 表中：

MERGE INTO people\_target pt

USING people\_source ps

ON (pt.person\_id = ps.person\_id)

WHEN MATCHED THEN UPDATE

SET pt.first\_name = ps.first\_name,

pt.last\_name = ps.last\_name,

pt.title = ps.title

WHEN NOT MATCHED THEN INSERT

(pt.person\_id, pt.first\_name, pt.last\_name, pt.title)

VALUES (ps.person\_id, ps.first\_name, ps.last\_name, ps.title);

注：需要提前设置环境变量，set ivorysql.insert\_enable\_alias to on;