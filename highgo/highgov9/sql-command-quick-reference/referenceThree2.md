---
title: "SQL命令"
book: "SQL命令速查手册"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceThree2.html"
tags:
  - highgo
  - highgo-v9
  - sql-command-quick-reference
---

## SQL 命令

## ALTER FOREIGN DATA WRAPPER

— 更改一个外部数据包装器的定义

**大纲**

```sql
ALTER FOREIGN DATA WRAPPER name
    [ HANDLER handler_function | NO HANDLER ]
    [ VALIDATOR validator_function | NO VALIDATOR ]
    [ OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] ) ]

ALTER FOREIGN DATA WRAPPER name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER FOREIGN DATA WRAPPER name RENAME TO new_name
```

**描述**

`ALTER FOREIGN DATA WRAPPER` 更改一个外部数据包装器的定义。该命令的第一种形式用于更改外部数据包装器的支持函数或者一般选项（至少要求一个子句）。第二种形式更改外部数据包装器的拥有者。

只有超级用户能修改外部数据包装器。此外，只有超级用户能够拥有外部数据包装器。

**参数**

- **`name`**
	一个已有的外部数据包装器的名称。
- **`HANDLER handler_function`**
	为外部数据包装器指定一个新的处理器函数。
- **`NO HANDLER`**
	用于指定该外部数据包装器不再具有一个处理器函数。
	> **注意：**
	> 
	> 使用没有处理器的外部数据包装器的外部表不能被访问。
- **`VALIDATOR validator_function`**
	为外部数据包装器指定一个新的验证器函数。
	> **注意：**
	> 
	> 新的验证器可能会认为该外部数据包装器或者依赖于它的独立服务器的已有选项、用户映射、外部表无效。瀚高数据库不会做这种检查。在使用修改过的外部数据包装器之前确认这些选项正确是用户的责任。不过，在这个 `ALTER FOREIGN DATA WRAPPER` 命令中指定的选项将会被使用新的验证器检查。
- **`NO VALIDATOR`**
	用于指定该外部数据包装器不再拥有一个验证器函数。
- **`OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )`**
	为该外部数据包装器更改选项。 `ADD` 、 `SET` 以及 `DROP` 指定要被执行的动作。如果没有显式地指定操作，将假定为 `ADD` 。选项名称必须唯一，选项名称和值（如果有）也会使用该外部数据包装器的验证器函数来验证。
- **`new_owner`**
	该外部数据包装器的新拥有者的用户名。
- **`new_name`**
	该外部数据包装器的新名称。

**示例**

更改一个外部数据包装器 `dbi` ，增加选项 `foo` 并删除 `bar` ：

```sql
ALTER FOREIGN DATA WRAPPER dbi OPTIONS (ADD foo '1', DROP 'bar');
```

把外部数据包装器 `dbi` 的验证器改为 `bob.myvalidator` ：

```sql
ALTER FOREIGN DATA WRAPPER dbi VALIDATOR bob.myvalidator;
```

**兼容性**

`ALTER FOREIGN DATA WRAPPER` 符合 ISO/IEC 9075-9 (SQL/MED)。 `HANDLER` 、 `VALIDATOR` 、 `OWNER TO` 以及 `RENAME` 子句是扩展。

**另见**

```
CREATE FOREIGN DATA WRAPPER\`, \`DROP FOREIGN DATA WRAPPER
```

## ALTER FOREIGN TABLE

— 更改一个外部表的定义

**大纲**

```sql
ALTER FOREIGN TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    action [, ... ]

ALTER FOREIGN TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    RENAME [ COLUMN ] column_name TO new_column_name

ALTER FOREIGN TABLE [ IF EXISTS ] name
    RENAME TO new_name

ALTER FOREIGN TABLE [ IF EXISTS ] name
    SET SCHEMA new_schema
```

其中 **action** 是以下之一：

```sql
ADD [ COLUMN ] column_name data_type [ COLLATE collation ]
    [ column_constraint [ ... ] ]

DROP [ COLUMN ] [ IF EXISTS ] column_name [ RESTRICT | CASCADE ]

ALTER [ COLUMN ] column_name [ SET DATA ] TYPE data_type [ COLLATE collation ]

ALTER [ COLUMN ] column_name SET DEFAULT expression

ALTER [ COLUMN ] column_name DROP DEFAULT

ALTER [ COLUMN ] column_name { SET | DROP } NOT NULL

ALTER [ COLUMN ] column_name SET STATISTICS integer

ALTER [ COLUMN ] column_name SET ( attribute_option = value [, ... ] )

ALTER [ COLUMN ] column_name RESET ( attribute_option [, ... ] )

ALTER [ COLUMN ] column_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN }

ALTER [ COLUMN ] column_name OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ])

ADD table_constraint [ NOT VALID ]

VALIDATE CONSTRAINT constraint_name

DROP CONSTRAINT [ IF EXISTS ] constraint_name [ RESTRICT | CASCADE ]

DISABLE TRIGGER [ trigger_name | ALL | USER ]

ENABLE TRIGGER [ trigger_name | ALL | USER ]

ENABLE REPLICA TRIGGER trigger_name

ENABLE ALWAYS TRIGGER trigger_name

SET WITHOUT OIDS

INHERIT parent_table

NO INHERIT parent_table

OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ])
```

**描述**

`ALTER FOREIGN TABLE` 更改一个现有外部表的定义。有几种子形式：

- **`ADD COLUMN`**
	这种形式使用与 `CREATE FOREIGN TABLE` 相同的语法把一个新的列增加到该外部表。和为常规表增加一列不同，这种形式并不影响底层的存储：这个动作只是简单地声明通过该外部表可以访问某个新的列而已。
- **`DROP COLUMN [ IF EXISTS ]`**
	这种形式从一个外部表删掉一列。如果在该表外部有任何东西依赖于该列，你将需要写上 `CASCADE` ，典型的例子就是视图。如果指定了 `IF EXISTS` 并且该列不存在，将不会抛出错误。在这种情况下会转而发出一个提示。
- **`SET DATA TYPE`**
	这种形式更改一个外部表的一列的类型。同样，这种形式并不影响底层的存储：这个动作只是简单地更改瀚高数据库相信该列所具有的类型。
- **`SET/DROP DEFAULT`**
	这些形式设置或者移除一列的默认值。默认值只会应用于后续的 `INSERT` 或 `UPDATE` 命令，它们不会导致已经在表中的行被更改。
- **`SET/DROP NOT NULL`**
	把一列标记为允许或者不允许空值。
- **`SET STATISTICS`**
	这种形式为后续的 `ANALYZE` 操作设置针对每列的统计收集目标。详见 `ALTER TABLE` 的类似形式。
- **`SET ( attribute_option = value [, ... ] )`**
- **`RESET ( attribute_option [, ... ] )`**
	这种形式设置或重置针对每个属性的选项。详见 `ALTER TABLE` 的类似形式。
- **`SET STORAGE`**
	这种形式设置一个列的存储模式。详见 `ALTER TABLE` 中类似的模式。注意存储模式不会产生效果，除非该表的外部数据包装器选择处理它。
- **`ADD table_constraint [ NOT VALID ]`**
	这种形式为外部表增加一个新的约束，使用的语法和 `CREATE FOREIGN TABLE` 中相同。当前只支持 `CHECK` 约束。
	和向常规表增加约束的情况不同，为外部表增加约束时不会做任何事情来验证该约束是否正确。这个动作只是简单地声明了该外部表中所有的行都应该满足的某种新的条件（见 `CREATE FOREIGN TABLE` 中的讨论）。如果该约束被标记为 `NOT VALID` ，那么它不被假设为有效，而只是被记录下来以备未来使用。
- **`VALIDATE CONSTRAINT`**
	这种形式把一个之前被标记为 `NOT VALID` 的约束标记为有效。不会做任何动作来验证该约束，但是未来的查询将会假定该约束是保持的。
- **`DROP CONSTRAINT [ IF EXISTS ]`**
	这种形式删掉在一个外部表上的指定约束。如果指定了 `IF EXISTS` 但约束并不存在，则不会抛出错误。在这种情况下会发出一个提示。
- **`DISABLE/ENABLE [ REPLICA | ALWAYS ] TRIGGER`**
	这些形式配置属于该外部表的触发器的触发情况。详见 `ALTER TABLE` 的类似形式。
- **`SET WITHOUT OIDS`**
	向后兼容性语法，表示移除 `oid` 系统列。由于不能再为外部表添加 `oid` 系统列，此语句不再产生效用。
- **`INHERIT parent_table`**
	这种形式把目标外部表作为指定的父表的新后代。详见 `ALTER TABLE` 的类似的形式。
- **`NO INHERIT parent_table`**
	这种形式把目标外部表从指定的父表的子女列表中移除。
- **`OWNER`**
	这种形式把该外部表的拥有者改成指定的用户。
- **`OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )`**
	更改该外部表或者其中一个列的选项。 `ADD` 、 `SET` 以及 `DROP` 指定要执行的动作。如果没有显式地指定操作，将假定为 `ADD` 。不允许重复的名称（不过一个表选项和一个列选项可以重名）。选项名称和值也会用外部数据包装器库来验证。
- **`RENAME`**
	`RENAME` 形式更改外部表的名称或者外部表中一个列的名称。
- **`SET SCHEMA`**
	这种形式把外部表移动到另一个模式中。

所有除了 `RENAME` 和 `SET SCHEMA` 的动作都能被整合到一个多修改列表以便能被并行应用。例如，可以在一个命令中增加几个列并且/或者修改几个列的类型。

如果该命令被写作 `ALTER FOREIGN TABLE IF EXISTS ...` 并且该外部表不存在，则不会抛出错误。这种情况下会发出一个提示。

你必须拥有该表以使用 `ALTER FOREIGN TABLE` 。要更改一个外部表的模式，你必须还拥有新模式上的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有在该表的模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建该表做不到的事情。不过，一个超级用户怎么都能更改任何表的所有权）。要增加一列或者修改一个列的类型，你还必须具有该数据类型上的 `USAGE` 特权。

**参数**

- **`name`**
	一个要修改的现有外部表的名称（可以被模式限定）。如果在表名前指定了 `ONLY` ，则只有该表被修改。如果没有指定 `ONLY` ，该表和它所有的后代表（如果有）都会被修改。可选地，在表名后面指定 `*` 可以显式地表示将后代表包括在内。
- **`column_name`**
	一个新的或者现有列的名称。
- **`new_column_name`**
	一个现有列的新名称。
- **`new_name`**
	该表的新名称。
- **`data_type`**
	新列的数据类型或者一个现有列的新数据类型。
- **`table_constraint`**
	外部表的新表约束。
- **`constraint_name`**
	要删除的现有约束的名称。
- **`CASCADE`**
	自动删除依赖于被删除列或约束的对象（例如，引用该列的视图），并且接着删除依赖于那些对象的所有对象。
- **`RESTRICT`**
	如果有任何依赖对象就拒绝删除该列或约束。这是默认行为。
- **`trigger_name`**
	要禁用或启用的一个触发器的名称。
- **`ALL`**
	禁用或者启用所有属于该外部表的触发器（如果任何触发器是内部生成的触发器，这都要求超级用户特权。核心系统不会向外部表增加这类触发器，但是附加代码会这样做。）。
- **`USER`**
	禁用或者启用属于该外部表的除了内部生成的触发器之外的所有触发器。
- **`parent_table`**
	要与这个外部表关联或者解除关联的父表。
- **`new_owner`**
	该表的新拥有者的用户名。
- **`new_schema`**
	该表要被移动到其中的模式的名称。

**注解**

关键词 `COLUMN` 是噪声词并且可以被忽略。

当使用 `ADD COLUMN` 或 `DROP COLUMN` 增加或移除一列、增加一个 `NOT NULL` 或者 `CHECK` 约束或者用 `SET DATA TYPE` 更改一个列类型时，不会检查与外部服务器的一致性。确保该表定义匹配远端是用户的责任。

关于有效参数的进一步描述可参考 `CREATE FOREIGN TABLE` 。

**示例**

要把一列标记为非空：

```sql
ALTER FOREIGN TABLE distributors ALTER COLUMN street SET NOT NULL;
```

要更改一个外部表的选项：

```sql
ALTER FOREIGN TABLE myschema.distributors OPTIONS (ADD opt1 'value', SET opt2 'value2', DROP opt3 'value3');
```

**兼容性**

形式 `ADD` 、 `DROP` 以及 `SET DATA TYPE` 符合 SQL 标准。其他形式是 SQL 标准的瀚高数据库扩展。在一个 `ALTER FOREIGN TABLE` 命令中指定多于一个操作也是一种扩展。

`ALTER FOREIGN TABLE DROP COLUMN` 可以被用来删除一个外部表的唯一一列，从而留下一个没有列的表。这是一种 SQL 的扩展，它允许没有列的外部表。

**另见**

```
CREATE FOREIGN TABLE\`, \`DROP FOREIGN TABLE
```

## ALTER FUNCTION

— 更改一个函数的定义

**大纲**

```sql
ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    action [ ... ] [ RESTRICT ]

ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    RENAME TO new_name

ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    SET SCHEMA new_schema

ALTER FUNCTION name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    DEPENDS ON EXTENSION extension_name
```

其中 **action** 是以下之一：

```sql
CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
IMMUTABLE | STABLE | VOLATILE | [ NOT ] LEAKPROOF
[ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
PARALLEL { UNSAFE | RESTRICTED | SAFE }
COST execution_cost
ROWS result_rows
SUPPORT support_function
SET configuration_parameter { TO | = } { value | DEFAULT }
SET configuration_parameter FROM CURRENT
RESET configuration_parameter
RESET ALL
```

**描述**

`ALTER FUNCTION` 更改一个函数的定义。

你必须拥有该函数以使用 `ALTER FUNCTION` 。要更改一个函数的模式，你还必须具有新模式上的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有在该函数的模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建该函数做不到的事情。不过，一个超级用户怎么都能更改任何函数的所有权）。

**参数**

- **`name`**
	一个现有函数的名称（可以被模式限定）。如果没有指定参数列表，则该名称必须在它的模式中唯一。
- **`argmode`**
	一个参数的模式： `IN` 、 `OUT` 、 `INOUT` 或者 `VARIADIC` 。如果被忽略，默认为 `IN` 。注意 `ALTER FUNCTION` 并不真正关心 `OUT` 参数，因为在决定函数的身份时只需要输入参数。因此列出 `IN` 、 `INOUT` 以及 `VARIADIC` 参数即可。
- **`argname`**
	一个参数的名称。注意 `ALTER FUNCTION` 并不真正参数名称，因为在确定函数的身份时只需要参数的数据类型即可。
- **`argtype`**
	该函数的参数（如果有）的数据类型（可以被模式限定）。
- **`new_name`**
	该函数的新名称。
- **`new_owner`**
	该函数的新拥有者。注意如果该函数被标记为 `SECURITY DEFINER` ，它的后续执行将会使用新拥有者。
- **`new_schema`**
	该函数的新模式。
- **`extension_name`**
	该函数所以来的扩展名。
- **`CALLED ON NULL INPUT`**
- **`RETURNS NULL ON NULL INPUT`**
- **`STRICT`**
	`CALLED ON NULL INPUT` 将该函数改为在某些或者全部参数为空值时可以被调用。 `RETURNS NULL ON NULL INPUT` 或者 `STRICT` 将该函数改为只要任一参数为空值就不被调用而是自动假定一个空值结果。详见 `CREATE FUNCTION` 。
- **`IMMUTABLE`**
- **`STABLE`**
- **`VOLATILE`**
	把该函数的稳定性更改为指定的设置。详见 `CREATE FUNCTION` 。
- **`[ EXTERNAL ] SECURITY INVOKER`**
- **`[ EXTERNAL ] SECURITY DEFINER`**
	更改该函数是否为一个安全性定义者。关键词 `EXTERNAL` 是为了符合 SQL，它会被忽略。关于这项能力的详情请见 `CREATE FUNCTION` 。
- **`PARALLEL`**
	决定该函数对于并行是否安全。详见 `CREATE FUNCTION` 。
- **`LEAKPROOF`**
	更改该函数是否被认为是防泄漏的。关于这项能力的详情请见 `CREATE FUNCTION` 。
- **`COST execution_cost`**
	更改该函数的估计执行代价。详见 `CREATE FUNCTION` 。
- **`ROWS result_rows`**
	更改一个集合返回函数的估计行数。详见 `CREATE FUNCTION` 。
- **`SUPPORT support_function`**
	设置或更改计划器支持函数以使用这个函数。此选项不能用于完全删除支持功能，因为它必须命名新的支持函数。如果需要这样做，可以使用 `CREATE OR REPLACE FUNCTION` 。
- **`configuration_parameter`**
- **`value`**
	当该函数被调用时，要对一个配置参数做出增加或者更改的赋值。如果 `value` 是 `DEFAULT` 或者使用等价的 `RESET` ，该函数本地的设置将会被移除，这样该函数会使用其环境中存在的值执行。使用 `RESET ALL` 可以清除所有函数本地的设置。 `SET FROM CURRENT` 把 `ALTER FUNCTION` 执行时该参数的当前值保存为进入该函数时要应用的值。
- **`RESTRICT`**
	为了符合 SQL 标准存在，被忽略。

**示例**

要把用于类型 `integer` 的函数 `sqrt` 重命名为 `square_root` ：

```sql
ALTER FUNCTION sqrt(integer) RENAME TO square_root;
```

要把用于类型 `integer` 的函数 `sqrt` 的拥有者改为 `joe` ：

```sql
ALTER FUNCTION sqrt(integer) OWNER TO joe;
```

要把用于类型 `integer` 的函数 `sqrt` 的模式改为 `maths` ：

```sql
ALTER FUNCTION sqrt(integer) SET SCHEMA maths;
```

要把类型 `integer` 的函数 `sqrt` 标记为依赖于扩展 `mathlib` ：

```sql
ALTER FUNCTION sqrt(integer) DEPENDS ON EXTENSION mathlib;
```

要调整一个函数的自动搜索路径：

```sql
ALTER FUNCTION check_password(text) SET search_path = admin, pg_temp;
```

要禁止一个函数的 `search_path` 的自动设置：

```sql
ALTER FUNCTION check_password(text) RESET search_path;
```

这个函数将用其调用者使用的搜索路径来执行。

**兼容性**

这个语句部分兼容 SQL 标准中的 `ALTER FUNCTION` 语句。该标准允许修改一个函数的更多属性，但是不提供重命名一个函数、标记一个函数为安全性定义者、为一个函数附加配置参数值或者更改一个函数的拥有者、模式或者稳定性等功能。该标准还要求 `RESTRICT` 关键字，它在瀚高数据库中是可选的。

**另见**

```sql
CREATE FUNCTION\`, \`DROP FUNCTION\`, \`ALTER PROCEDURE\`, \`ALTER ROUTINE
```

## ALTER GROUP

— 更改角色名称或者成员关系

**大纲**

```sql
ALTER GROUP role_specification ADD USER user_name [, ... ]

ALTER GROUP role_specification DROP USER user_name [, ... ]
```

其中 **role\_specification** 可以是：

```
role_name
  | CURRENT_USER
  | SESSION_USER

ALTER GROUP group_name RENAME TO new_name
```

**描述**

`ALTER GROUP` 更改一个用户组的属性。这是一个被废弃的命令，不过为了向后兼容还是会被接受，因为组（以及用户）已经被更一般的角色概念替代了。

前两个变体向一个组增加用户或者从一个组中移除用户（为了这个目的，任何角色都可以扮演”用户”或者”组”）。这些变体实际上等效于在被称为”组”的角色中授予或者回收成员关系，因此最好的方法是使用 `GRANT` 或者 `REVOKE` 。

第三种变体会更改该组的名称。这恰好等效于用 `ALTER ROLE` 重命名该角色。

**参数**

- **`group_name`**
	要修改的组（角色）的名称。
- **`user_name`**
	要被加入到该组或者从该组移除的用户（角色）。这些用户必须已经存在， `ALTER GROUP` 不会创建或者删除用户。
- **`new_name`**
	该组的新名称。

**示例**

向一个组增加用户：

```sql
ALTER GROUP staff ADD USER karl, john;
```

从一个组移除一个用户：

```sql
ALTER GROUP workers DROP USER beth;
```

**兼容性**

在 SQL 标准中没有 `ALTER GROUP` 语句。

**另见**

```sql
GRANT\`, \`REVOKE\`, \`ALTER ROLE
```

## ALTER INDEX

— 更改一个索引的定义

**大纲**

```sql
ALTER INDEX [ IF EXISTS ] name RENAME TO new_name

ALTER INDEX [ IF EXISTS ] name SET TABLESPACE tablespace_name

ALTER INDEX name ATTACH PARTITION index_name

ALTER INDEX name DEPENDS ON EXTENSION extension_name

ALTER INDEX [ IF EXISTS ] name SET ( storage_parameter = value [, ... ] )

ALTER INDEX [ IF EXISTS ] name RESET ( storage_parameter [, ... ] )

ALTER INDEX [ IF EXISTS ] name ALTER [ COLUMN ] column_number
    SET STATISTICS integer

ALTER INDEX ALL IN TABLESPACE name [ OWNED BY role_name [, ... ] ]
    SET TABLESPACE new_tablespace [ NOWAIT ]
```

**描述**

`ALTER INDEX` 更改一个现有索引的定义。下面描述了几种子窗体。注意每个子窗体所需的锁级别可能不同。除非显式说明， `ACCESS EXCLUSIVE` 锁被持有。列出多个子命令时，锁的持有将是任何子命令所需的最严格的子命令。

- **`RENAME`**
	`RENAME` 形式更改该索引的名称。如果索引与一个表约束（ `UNIQUE` 、 `PRIMARY KEY` 或者 `EXCLUDE` ）关联，该约束也会被重命名。这对已存储的数据没有影响。
	重命名索引取得一个 `SHARE UPDATE EXCLUSIVE` 锁。
- **`SET TABLESPACE`**
	这种形式更改该索引的表空间为指定的表空间，并且把与该索引相关联的数据文件移动到新的表空间中。要更改一个索引的表空间，你必须拥有该索引并且具有新表空间上的 `CREATE` 特权。可以使用 `ALL IN TABLESPACE` 形式把当前数据库中在一个表空间内的所有索引全部移动到另一个表空间中，这将会锁定所有要被移动的索引然后挨个移动它们。这种形式也支持 `OWNED BY` ，即只移动属于指定角色的索引。如果指定了 `NOWAIT` 选项，那么当该命令无法立刻获得所有锁时将会失败。注意这个命令不会移动系统目录，如果想要移动系统目录，应使用 `ALTER DATABASE` 或者显式的 `ALTER INDEX` 调用。另见 `CREATE TABLESPACE` 。
- **`ATTACH PARTITION`**
	导致提到的索引变成附着于被修改的索引。提及的索引必须在包含被修改索引的表的一个分区上，并且具有一种等效的定义。一个附着索引不能被单独删除，它会在其父索引被删除时自动连带删除。
- **`DEPENDS ON EXTENSION`**
	这种形式把该索引标记为依赖于扩展，这样如果该扩展被删除，该索引也将被自动删除。
- **`SET ( storage_parameter = value [, ... ] )`**
	这种形式为该索引更改一个或者多个索引方法相关的存储参数。可用的参数详见 `CREATE INDEX` 。注意这个命令不会立刻修改索引内容，根据参数你可能需要用 `REINDEX` 重建索引来得到想要的效果。
- **`RESET ( storage_parameter [, ... ] )`**
	这种形式把一个或者多个索引方法相关的存储参数重置为其默认值。正如 `SET` 一样，可能需要一次 `REINDEX` 来完全更新该索引。
- **`ALTER [ COLUMN ] column_number SET STATISTICS integer`**
	这种形式为后续的 `ANALYZE` 操作设置针对每个列的统计信息收集目标，不过只能用在被定义为表达式的索引列上。由于表达式缺少唯一的名称，我们通过该索引列的顺序号来引用它们。收集目标可以被设置为范围 0 到 10000 之间的值。另外，把它设置为 -1 会恢复到使用系统的默认统计信息目标（ `default_statistics_target` ）。

**参数**

- **`IF EXISTS`**
	如果该索引不存在不要抛出错误。这种情况下将发出一个提示。
- **`column_number`**
	引用该索引列的顺序（从左往右）位置的顺序号。
- **`name`**
	要更改的一个现有索引的名称（可能被模式限定）。
- **`new_name`**
	该索引的新名称。
- **`tablespace_name`**
	该索引将被移动到的表空间。
- **`extension_name`**
	该索引所依赖的扩展的名称。
- **`storage_parameter`**
	一个索引方法相关的存储参数的名称。
- **`value`**
	一个索引方法相关的存储参数的新值。根据该参数，这可能是一个数字或者一个词。

**注解**

也可以用 `ALTER TABLE` 来做这些操作。实际上， `ALTER INDEX` 只是 `ALTER TABLE` 应用在索引上的形式的别名而已。

以前有一种 `ALTER INDEX OWNER` 变体，但现在已被忽略（会出现一个警告）。一个索引的拥有者不能与其基表的拥有者不同。更改基表的拥有者会自动地更改索引的拥有者。

不允许更改系统目录索引的任何部分。

**示例**

要重命名一个现有索引：

```sql
ALTER INDEX distributors RENAME TO suppliers;
```

把一个索引移动到一个不同的表空间：

```sql
ALTER INDEX distributors SET TABLESPACE fasttablespace;
```

更改一个索引的填充因子（假设该索引方法支持填充因子）：

```sql
ALTER INDEX distributors SET (fillfactor = 75);
REINDEX INDEX distributors;
```

为一个表达式索引设置统计信息收集目标：

```sql
CREATE INDEX coord_idx ON measured (x, y, (z + t));
ALTER INDEX coord_idx ALTER COLUMN 3 SET STATISTICS 1000;
```

**兼容性**

`ALTER INDEX` 是一种瀚高数据库扩展。

**另见**

```sql
CREATE INDEX\`, \`REINDEX
```

## ALTER LANGUAGE

— 更改一种过程语言的定义

**大纲**

```sql
ALTER [ PROCEDURAL ] LANGUAGE name RENAME TO new_name

ALTER [ PROCEDURAL ] LANGUAGE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
```

**描述**

`ALTER LANGUAGE` 更改一种过程语言的定义。唯一的功能是重命名该语言或者为它赋予一个新的拥有者。要使用 `ALTER LANGUAGE` ，你必须是一个超级用户或者该语言的拥有者。

**参数**

- **`name`**  
	语言的名称
- **`new_name`**  
	该语言的新名称
- **`new_owner`**  
	该语言的新拥有者

**兼容性**

在 SQL 标准中没有 `ALTER LANGUAGE` 语句。

**另见**

```sql
CREATE LANGUAGE\`, \`DROP LANGUAGE
```

## ALTER LARGE OBJECT

— 更改一个大对象的定义

**大纲**

```sql
ALTER LARGE OBJECT large_object_oid OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
```

**描述**

`ALTER LARGE OBJECT` 更改一个大对象的定义。

您必须拥有大对象才能使用 `ALTER LARGE OBJECT` 。要更改所有者，您还必须是新所有者的直接或间接成员。（不过，超级用户仍然可以更改任何大对象。)当前，唯一的功能是分配新所有者，因此两者的约束都始终适用。

**参数**

- **`large_object_oid`**  
	要被修改的大对象的 OID
- **`new_owner`**  
	该大对象的新拥有者

**兼容性**

在 SQL 标准中没有 `ALTER LARGE OBJECT` 语句。

## ALTER MATERIALIZED VIEW

— 更改一个物化视图的定义

**大纲**

```sql
ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    action [, ... ]

ALTER MATERIALIZED VIEW name
    DEPENDS ON EXTENSION extension_name

ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    RENAME [ COLUMN ] column_name TO new_column_name

ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    RENAME TO new_name

ALTER MATERIALIZED VIEW [ IF EXISTS ] name
    SET SCHEMA new_schema

ALTER MATERIALIZED VIEW ALL IN TABLESPACE name [ OWNED BY role_name [, ... ] ]
    SET TABLESPACE new_tablespace [ NOWAIT ]
```

其中 **action** 是下列之一：

```sql
ALTER [ COLUMN ] column_name SET STATISTICS integer
ALTER [ COLUMN ] column_name SET ( attribute_option = value [, ... ] )
ALTER [ COLUMN ] column_name RESET ( attribute_option [, ... ] )
ALTER [ COLUMN ] column_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN }
CLUSTER ON index_name
SET WITHOUT CLUSTER
SET ( storage_parameter = value [, ... ] )
RESET ( storage_parameter [, ... ] )
OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
```

**描述**

`ALTER MATERIALIZED VIEW` 更改一个现有物化视图的多个辅助属性。

要使用 `ALTER MATERIALIZED VIEW` ，你必须拥有该物化视图。要更改一个物化视图的模式，你还必须拥有新模式上的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须拥有该物化视图所在模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建该物化视图做不到的事情。不过，一个超级用户怎么都能更改任何视图的所有权。）。

`DEPENDS ON EXTENSION` 形式把该物化视图标记为依赖于一个扩展，这样该扩展被删除时会自动地删除掉这个物化视图。

可用于 `ALTER MATERIALIZED VIEW` 的语句形式和动作是 `ALTER TABLE` 的一个子集，并且在用于物化视图时具有相同的含义。详见 `ALTER TABLE` 的描述。

**参数**

- **`name`**  
	一个现有物化视图的名称（可以是模式限定的）。
- **`column_name`**  
	一个新的或者现有的列的名称。
- **`extension_name`**  
	该物化视图所依赖的扩展的名称。
- **`new_column_name`**  
	一个现有列的新名称。
- **`new_owner`**  
	该物化视图的新拥有者的用户名。
- **`new_name`**  
	该物化视图的新名称。
- **`new_schema`**  
	该物化视图的新模式。

**示例**

把物化视图 `foo` 重命名为 `bar` ：

```sql
ALTER MATERIALIZED VIEW foo RENAME TO bar;
```

**兼容性**

`ALTER MATERIALIZED VIEW` 是一种瀚高数据库扩展。

**另见**

```sql
CREATE MATERIALIZED VIEW\`, \`DROP MATERIALIZED VIEW\`, \`REFRESH MATERIALIZED VIEW
```

## ALTER OPERATOR

— 更改一个操作符的定义

**大纲**

```sql
ALTER OPERATOR name ( { left_type | NONE } , { right_type | NONE } )
    OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER OPERATOR name ( { left_type | NONE } , { right_type | NONE } )
    SET SCHEMA new_schema

ALTER OPERATOR name ( { left_type | NONE } , { right_type | NONE } )
    SET ( { RESTRICT = { res_proc | NONE }
           | JOIN = { join_proc | NONE }
         } [, ... ] )
```

**描述**

`ALTER OPERATOR` 更改一个操作符的定义。

要使用 `ALTER OPERATOR` ，你必须拥有该操作符。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该操作符所在模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建操作符做不到的事情。不过，一个超级用户怎么都能更改任何操作符的所有权。）。

**参数**

- **`name`**  
	一个现有操作符的名称（可以是模式限定的）。
- **`left_type`**  
	该操作符左操作数的数据类型，如果该操作符没有左操作数可以写成 `NONE` 。
- **`right_type`**  
	该操作符右操作数的数据类型，如果该操作符没有右操作数可以写成 `NONE` 。
- **`new_owner`**  
	该操作符的新拥有者。
- **`new_schema`**  
	该操作符的新模式。
- **`res_proc`**  
	这个操作符的约束选择度估算器函数，写成 `NONE` 可以移除现有的选择度估算器。
- **`join_proc`**  
	这个操作符的连接选择度估算器函数，写成 `NONE` 可以移除现有的选择度估算器。

**示例**

更改类型 `text` 的一个自定义操作符 `a @@ b` 的拥有者：

```sql
ALTER OPERATOR @@ (text, text) OWNER TO joe;
```

更改类型 `int[]` 的自定义操作符 `a && b` 的约束和连接选择度估算器函数：

```sql
ALTER OPERATOR && (_int4, _int4) SET (RESTRICT = _int_contsel, JOIN = _int_contjoinsel);
```

**兼容性**

在 SQL 标准中没有 `ALTER OPERATOR` 语句。

**另见**

```sql
CREATE OPERATOR\`, \`DROP OPERATOR
```

## ALTER OPERATOR CLASS

— 更改一个操作符类的定义

**大纲**

```sql
ALTER OPERATOR CLASS name USING index_method RENAME TO new_name

ALTER OPERATOR CLASS name USING index_method OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER OPERATOR CLASS name USING index_method SET SCHEMA new_schema
```

**描述**

`ALTER OPERATOR CLASS` 更改一个操作符类的定义。

要使用 `ALTER OPERATOR CLASS` ，你必须拥有该操作符类。要修改拥有者，你还必须是新拥有角色的一个直接或间接成员，并且该角色必须具有该操作符类所在模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建操作符类做不到的事情。不过，一个超级用户怎么都能更改任何操作符类的所有权。）。

**参数**

- **`name`**  
	一个现有操作符类的名称（可以是模式限定的）。
- **`index_method`**  
	这个操作符类所服务的索引方法的名称。
- **`new_name`**  
	该操作符类的新名称。
- **`new_owner`**  
	该操作符类的新拥有者。
- **`new_schema`**  
	该操作符类的新模式。

**兼容性**

在 SQL 标准中没有 `ALTER OPERATOR CLASS` 语句。

**另见**

```sql
CREATE OPERATOR CLASS\`, \`DROP OPERATOR CLASS\`, \`ALTER OPERATOR FAMILY
```

## ALTER OPERATOR FAMILY

— 更改一个操作符族的定义

**大纲**

```sql
ALTER OPERATOR FAMILY name USING index_method ADD
    { OPERATOR strategy_number operator_name ( op_type, op_type )
      [ FOR SEARCH | FOR ORDER BY sort_family_name ]
    | FUNCTION support_number [ ( op_type [ , op_type ] ) ]
      function_name [ ( argument_type [, ...] ) ]
    } [, ... ]

ALTER OPERATOR FAMILY name USING index_method DROP
    { OPERATOR strategy_number ( op_type [ , op_type ] )
    | FUNCTION support_number ( op_type [ , op_type ] )
    } [, ... ]

ALTER OPERATOR FAMILY name USING index_method RENAME TO new_name

ALTER OPERATOR FAMILY name USING index_method OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER OPERATOR FAMILY name USING index_method SET SCHEMA new_schema
```

**描述**

`ALTER OPERATOR FAMILY` 更改一个操作符族的定义。你能增加操作符以及支持函数到该家族、从该族中移除它们或者更改该族的名称或者拥有者。

在用 `ALTER OPERATOR FAMILY` 增加操作符和支持函数到一个族中时，它们不是族内任何特定操作符类的组成部分，而只是 “松散”地存在于该族中。这表示这些操作符和函数与该族的语义兼容，但是没有被任何特定索引的正确功能所要求（所要求的操作符和函数应该被作为一个操作符类的一部分声明，见 `CREATE OPERATOR CLASS` ）。瀚高数据库将允许一个族的松散成员在任何时候被从该族中删除，但是在删除一个操作符类的成员之前，必须已经删除整个类以及依赖于该成员的索引。具有代表性的是，单一数据类型操作符和函数是操作符类的一部分，因为在特定数据类型上的索引需要它们的支持。而多数据类型操作符和函数则被作为该族的松散成员。

要使用 `ALTER OPERATOR FAMILY` ，你必须是超级用户（做这样的限制是因为一个错误的操作符族定义可能会迷惑服务器甚至让它崩溃）。

`ALTER OPERATOR FAMILY` 目前不检测操作符族定义是否包括该索引方法所要求的所有操作符和函数，也不检查操作符和函数是否形成了一个有理的集合。定义一个合法的操作符族是用户的责任。

**参数**

- **`name`**  
	一个现有操作符族的名称（可以是模式限定的）。
- **`index_method`**  
	这个操作符族所应用的索引方法的名称。
- **`strategy_number`**  
	与该操作符族相关的一个操作符的索引方法策略号。
- **`operator_name`**  
	与该操作符族相关的一个操作符的名称（可以是模式限定的）。
- **`op_type`**  
	在一个 `OPERATOR` 子句中指定该操作符的操作数数据类型，或者用 `NONE` 来表示一个左一元或者右一元操作符。不同于 `CREATE OPERATOR CLASS` 中类似的语法，操作数数据类型总是必须被指定。
	在一个 `ADD FUNCTION` 子句中指定该函数意图支持的操作数据类型（如果不同于该函数的输入数据类型）。对于 B-树比较函数和哈希函数，有必要指定 `op_type` ，因为该函数的输入数据类型总是正确的。对于 B-树排序支持函数和 GiST、SP-GiST 和 GIN 操作符类中的所有函数，有必要指定该函数要使用的操作数数据类型。
	在一个 `DROP FUNCTION` 子句中，必须指定该函数要支持的操作数数据类型。
- **`sort_family_name`**  
	一个现有 btree 操作符族的名称（可能是模式限定的），它描述与一个排序操作符相关的排序顺序。
	如果既没有指定 `FOR SEARCH` 也没有指定 `FOR ORDER BY` ，默认值是 `FOR SEARCH` 。
- **`support_number`**  
	一个与该操作符族相关的函数的索引方法支持过程编号。
- **`function_name`**  
	作为该操作符族的一种索引方法支持函数的函数名称（可以是模式限定的）。如果没有指定参数列表，则该名称必须在其模式中唯一。
- **`argument_type`**  
	该函数的参数数据类型。
- **`new_name`**  
	该操作符族的新名称。
- **`new_owner`**  
	该操作符族的新拥有者。
- **`new_schema`**  
	该操作符族的新模式。

`OPERATOR` 和 `FUNCTION` 子句可以以任何顺序出现。

**注解**

注意 `DROP` 语法只通过策略或者支持号以及输入数据类型指定该操作符族中的 “slot”。占用这个槽的操作符或函数的名称不会被提及。还有，对于 `DROP FUNCTION` ，要指定的类型是该函数意图支持的输入数据类型。对于 GiST、SP-GiST 以及 GIN 索引，可能无需对该函数的实际输入参数类型做任何事情。

因为索引机制在使用函数之前不会检查其上的访问权限，包括一个操作符族中的函数或操作符都等同于授予了其上的公共执行权限。这对于操作符族中很有用的这类函数来说，这通常不成问题。

操作符应该由 SQL 函数定义。一个 SQL 函数很可能被内联到调用查询中，这将阻止优化器识别出该查询匹配一个索引。

**示例**

下列示例命令为一个操作符族增加跨数据类型的操作符和支持函数，该操作符族已经包含用于数据类型 `int4` 以及 `int2` 的 B-树操作符类。

```sql
ALTER OPERATOR FAMILY integer_ops USING btree ADD
  -- int4 vs int2
<
<=
=
>=
>
  FUNCTION 1 btint42cmp(int4, int2) ,
  -- int2 vs int4
<
<=
=
>=
>
  FUNCTION 1 btint24cmp(int2, int4) ;
```

再次移除这些项：

```sql
ALTER OPERATOR FAMILY integer_ops USING btree DROP
  -- int4 vs int2
  OPERATOR 1 (int4, int2) ,
  OPERATOR 2 (int4, int2) ,
  OPERATOR 3 (int4, int2) ,
  OPERATOR 4 (int4, int2) ,
  OPERATOR 5 (int4, int2) ,
  FUNCTION 1 (int4, int2) ,
  -- int2 vs int4
  OPERATOR 1 (int2, int4) ,
  OPERATOR 2 (int2, int4) ,
  OPERATOR 3 (int2, int4) ,
  OPERATOR 4 (int2, int4) ,
  OPERATOR 5 (int2, int4) ,
  FUNCTION 1 (int2, int4) ;
```

**兼容性**

在 SQL 标准中没有 `ALTER OPERATOR FAMILY` 语句。

**另见**

```sql
CREATE OPERATOR FAMILY\`, \`DROP OPERATOR FAMILY\`, \`CREATE OPERATOR CLASS\`, \`ALTER OPERATOR CLASS\`, \`DROP OPERATOR CLASS
```

## ALTER POLICY

— 更改一条行级安全性策略的定义

**大纲**

```sql
ALTER POLICY name ON table_name RENAME TO new_name

ALTER POLICY name ON table_name
    [ TO { role_name | PUBLIC | CURRENT_USER | SESSION_USER } [, ...] ]
    [ USING ( using_expression ) ]
    [ WITH CHECK ( check_expression ) ]
```

**描述**

`ALTER POLICY` 更改一条现有行级安全性策略的定义。请注意， `ALTER POLICY` 只允许修改策略所应用的角色集合，和要修改的 `USING` 和 `WITH CHECK` 表达式。要更改策略的其他属性，例如其应用的命令，或者是允许还是限制，则必须删除并重新创建策略。

要使用 `ALTER POLICY` ，你必须拥有该策略所适用的表。

在 `ALTER POLICY` 的第二种形式中，如果指定了角色列表、 `using_expression` 以及 `check_expression` ，它们会被独立地替换。当这些子句之一被省略时，策略的对应部分不会被更改。

**参数**

- **`name`**  
	要更改的现有策略的名称。
- **`table_name`**  
	该策略所在的表的名称（可以被模式限定）。
- **`new_name`**  
	该策略的新名称。
- **`role_name`**  
	该策略适用的角色。可以一次指定多个角色。要把该策略应用于所有角色，可使用 `PUBLIC` 。
- **`using_expression`**  
	该策略的 `USING` 表达式。详见 `CREATE POLICY` 。
- **`check_expression`**  
	该策略的 `WITH CHECK` 表达式。详见 `CREATE POLICY` 。

**兼容性**

`ALTER POLICY` 是一种瀚高数据库扩展。

**另见**

```sql
CREATE POLICY\`, \`DROP POLICY
```

## ALTER PROCEDURE

— 更改一个存储过程的定义

**大纲**

```sql
ALTER PROCEDURE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    action [ ... ] [ RESTRICT ]

ALTER PROCEDURE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    RENAME TO new_name

ALTER PROCEDURE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER PROCEDURE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    SET SCHEMA new_schema

ALTER PROCEDURE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    DEPENDS ON EXTENSION extension_name
```

其中 **action** 是下列之一：

```sql
[ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
SET configuration_parameter { TO | = } { value | DEFAULT }
SET configuration_parameter FROM CURRENT
RESET configuration_parameter
RESET ALL
```

**简介**

`ALTER PROCEDURE` 更改一个过程的定义。

要使用 `ALTER PROCEDURE` ，你必须拥有该过程。要更改一个过程的方案，你还必须有新方案上的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的直接或间接成员，并且那个角色在该过程的方案上拥有 `CREATE` 特权（这些限制强制更新拥有者无法做到通过删除和重建该过程无法做到的事情。不过，超级用户总是能够更改任何过程的拥有关系）。

**参数**

- **`name`**  
	一个现有的过程的名字（可以被方案限定）。如果没有指定参数列表，这个名字必须在其方案中唯一。
- **`argmode`**  
	参数的模式： `IN` 或 `VARIADIC` 。如果被省略，默认是 `IN` 。
- **`argname`**  
	参数的名字。注意 `ALTER PROCEDURE` 实际上并不关心参数名，因为只需要参数的数据类型来确定过程的身份。
- **`argtype`**  
	如果该过程有参数，这是参数的数据类型（可以被方案限定）。
- **`new_name`**  
	该过程的新名字。
- **`new_owner`**  
	该过程的新拥有者。注意，如果这个过程被标记为 `SECURITY DEFINER` ，接下来它将被作为新拥有者执行。
- **`new_schema`**  
	该过程的新方案。
- **`extension_name`**  
	该过程所依赖的扩展的名称。
- **`[ EXTERNAL ] SECURITY INVOKER`**  
	**`[ EXTERNAL ] SECURITY DEFINER`**  
	更改该过程是否为一个安全性定义器。关键词 `EXTERNAL` 由于 SQL 符合性的原因被忽略。更多有关这个能力的信息请见 `CREATE PROCEDURE` 。
- **`configuration_parameter`**
- **`value`**  
	增加或者更改在调用该过程时，要对一个配置参数做的赋值。如果 `value` 是 `DEFAULT` 或者等效的值，则会使用 `RESET` ，过程本地的设置会被移除，这样该过程的执行就会使用其所处环境中的值。使用 `RESET ALL` 可以清除所有的过程本地设置。 `SET FROM CURRENT` 会把 `ALTER PROCEDURE` 执行时该参数的当前值保存为进入该过程时要被应用的值。
	关于允许的参数名和参数值的更多信息请见 `SET` 和第 19 章。
- **`RESTRICT`**  
	为了符合 SQL 标准会被忽略。

**示例**

要重命名具有两个 `integer` 类型参数的过程 `insert_data` 为 `insert_record` ：

```sql
ALTER PROCEDURE insert_data(integer, integer) RENAME TO insert_record;
```

要把具有两个 `integer` 类型参数的过程 `insert_data` 的拥有者改为 `joe` ：

```sql
ALTER PROCEDURE insert_data(integer, integer) OWNER TO joe;
```

要重把具有两个 `integer` 类型参数的过程 `insert_data` 的方案改为 `accounting` ：

```sql
ALTER PROCEDURE insert_data(integer, integer) SET SCHEMA accounting;
```

把过程 `insert_data(integer, integer)` 标记为依赖于扩展 `myext` ：

```sql
ALTER PROCEDURE insert_data(integer, integer) DEPENDS ON EXTENSION myext;
```

要调整一个过程自动设置的搜索路径：

```sql
ALTER PROCEDURE check_password(text) SET search_path = admin, pg_temp;
```

要为一个过程禁用 `search_path` 的自动设置：

```sql
ALTER PROCEDURE check_password(text) RESET search_path;
```

现在这个过程将用其调用者所使用的任何搜索路径执行。

**兼容性**

这个语句与 SQL 标准中的 `ALTER PROCEDURE` 语句部分兼容。标注你允许修改一个过程的更多性质，但是不提供重命名过程、让过程成为安全性定义器、为过程附加配置参数值或者更改过程的拥有者、方案或者可变性的能力。标准还要求 `RESTRICT` 关键字，而它在瀚高数据库中是可选的。

**另见**

```sql
CREATE PROCEDURE\`, \`DROP PROCEDURE\`, \`ALTER FUNCTION\`, \`ALTER ROUTINE
```

## ALTER PUBLICATION

— 修改发布的定义

**大纲**

```sql
ALTER PUBLICATION name ADD TABLE [ ONLY ] table_name [ * ] [, ...]

ALTER PUBLICATION name SET TABLE [ ONLY ] table_name [ * ] [, ...]

ALTER PUBLICATION name DROP TABLE [ ONLY ] table_name [ * ] [, ...]

ALTER PUBLICATION name SET ( publication_parameter [= value] [, ... ] )

ALTER PUBLICATION name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER PUBLICATION name RENAME TO new_name
```

**描述**

命令 `ALTER PUBLICATION` 可以更改发布的属性。

前三个语句更改哪些表是该发布的一部分。 `SET TABLE` 子句用指定的表替换发布中的表的列表。 `ADD TABLE` 和 `DROP TABLE` 子句将从发布中添加和删除一个或多个表。请注意，将表添加到已订阅的发布中将需要在订阅端执行 `ALTER SUBSCRIPTION ... REFRESH PUBLICATION` 操作才能生效。

第四条语句可以改变在 `CREATE PUBLICATION` 中指定的所有发布属性。该命令中未提及的属性保留其先前的设置。

其余语句更改所有者和发布的名称。

你必须拥有该发布才能使用 `ALTER PUBLICATION` 。要改变所有者，你也必须是新所有者角色的直接或间接成员。新的所有者必须在数据库上拥有 `CREATE` 权限。此外， `FOR ALL TABLES` 发布的新所有者必须是超级用户。但是，超级用户可以在避开这些限制的情况下更改发布的所有权。

**参数**

- **`name`**  
	要修改定义的现有发布的名称。
- **`table_name`**  
	现有表的名称。如果在表名之前指定了 `ONLY` ，则只有该表受到影响。如果没有指定 `ONLY` ，则该表及其所有后代表（如果有的话）都会受到影响。可选地，可以在表名之后指定 `*` 以明确指示包含后代表。
- **`SET ( publication_parameter [= value] [, ... ] )`**  
	该子句修改最初由 `CREATE PUBLICATION` 设置的发布参数。
- **`new_owner`**  
	发布的新所有者的用户名。
- **`new_name`**  
	发布的新名称。

**示例**

将发布修改为只发布删除和更新：

```sql
ALTER PUBLICATION noinsert SET (publish = 'update, delete');
```

给发布添加一些表：

```sql
ALTER PUBLICATION mypublication ADD TABLE users, departments;
```

**兼容性**

`ALTER PUBLICATION` 是瀚高数据库的一个扩展。

**参见**

```sql
CREATE PUBLICATION\`, \`DROP PUBLICATION\`, \`CREATE SUBSCRIPTION\`, \`ALTER SUBSCRIPTION
```

## ALTER ROLE

— 更改一个数据库角色

**大纲**

```sql
ALTER ROLE role_specification [ WITH ] option [ ... ]
```

其中 **option** 可以是：

```sql
SUPERUSER | NOSUPERUSER
| CREATEDB | NOCREATEDB
| CREATEROLE | NOCREATEROLE
| INHERIT | NOINHERIT
| LOGIN | NOLOGIN
| REPLICATION | NOREPLICATION
| BYPASSRLS | NOBYPASSRLS
| CONNECTION LIMIT connlimit
| [ ENCRYPTED ] PASSWORD 'password' | PASSWORD NULL
| VALID UNTIL 'timestamp'

ALTER ROLE name RENAME TO new_name

ALTER ROLE { role_specification | ALL } [ IN DATABASE database_name ]
    SET configuration_parameter { TO | = } { value | DEFAULT }

ALTER ROLE { role_specification | ALL } [ IN DATABASE database_name ]
    SET configuration_parameter FROM CURRENT

ALTER ROLE { role_specification | ALL } [ IN DATABASE database_name ]
    RESET configuration_parameter

ALTER ROLE { role_specification | ALL } [ IN DATABASE database_name ] RESET ALL
```

其中 **role\_specification** 可以是：

```sql
role_name
| CURRENT_USER
| SESSION_USER
```

**描述**

`ALTER ROLE` 更改一个瀚高数据库角色的属性。

前面列出的这个命令的第一种变体能够更改 `CREATE ROLE` 中指定的很多角色属性（覆盖了所有可能的属性，不过没有增加和移除成员关系的选项，如果要增加和移除成员关系可使用 `GRANT` 和 `REVOKE` ）。该命令中没有提到的属性保持它们之前的设置。数据库超级用户能够更改任何角色的任何这些设置。具有 `CREATEROLE` 特权的角色能够更改任何这些设置，但是只能为非超级用户和非复制角色修改。普通角色只能更改它们自己的口令。

第二种变体更改该角色的名称。数据库超级用户能重命名任何角色。具有 `CREATEROLE` 特权的角色能够重命名任何非超级用户角色。当前的会话用户不能被重命名（如果需要这样做，请以一个不同的用户连接）。由于 MD5 加密的口令使用角色名作为 salt，因此如果一个角色的口令是 MD5 加密的，重命名该角色会清空其口令。

其余的变体用于更改一个角色的配置变量的会话默认值，可以为所有数据库设置，或者只为 `IN DATABASE` 中指定的数据库设置。如果指定的是 `ALL` 而不是一个角色名，将会为所有角色更改该设置。把 `ALL` 和 `IN DATABASE` 一起使用实际上和使用命令 `ALTER DATABASE ... SET ...` 相同。

只要改角色后续开始一个新会话，指定的值将会成为该会话的默认值，并且会覆盖 `postgresql.conf` 中存在的值或者从 `postgres` 命令行收到的值。这只在登录时发生，执行 `SET ROLE` 或者 `SET SESSION AUTHORIZATION` 不会导致新的配置值被设置。对于所有数据库设置的值会被附加到一个角色的数据库相关的设置所覆盖。特定数据库或角色的设置会覆盖为所有角色所作的设置。

超级用户能够更改任何人的会话默认值。具有 `CREATEROLE` 特权的角色能够更改非超级用户的默认值。普通角色只能为它们自己设置默认值。某些配置变量不能以这种方式设置，或者只能由一个超级用户发出的命令设置。只有超级用户能够更改所有角色在所有数据库中的设置。

**参数**

- **`name`**  
	要对其属性进行修改的角色的名称。
- **`CURRENT_USER`**  
	修改当前用户而不是一个显式标识的角色。
- **`SESSION_USER`**  
	修改当前会话用户而不是一个显式标识的角色。
- **`SUPERUSER`**
- **`NOSUPERUSER`**
- **`CREATEDB`**
- **`NOCREATEDB`**
- **`CREATEROLE`**
- **`NOCREATEROLE`**
- **`INHERIT`**
- **`NOINHERIT`**
- **`LOGIN`**
- **`NOLOGIN`**
- **`REPLICATION`**
- **`NOREPLICATION`**
- **`BYPASSRLS`**
- **`NOBYPASSRLS`**
- **`CONNECTION LIMIT connlimit`**
- **`[ ENCRYPTED ] PASSWORD 'password'`**
- **`PASSWORD NULL`**
- **`VALID UNTIL 'timestamp'`**  
	这些子句修改原来有 `CREATE ROLE` 设置的属性。更多信息请见 `CREATE ROLE` 参考页。
- **`new_name`**  
	该角色的新名称。
- **`database_name`**  
	要在其中设置该配置变量的数据库名称。
- **`configuration_parameter`**
- **`value`**  
	把这个角色的指定配置参数的会话默认值设置为给定值。如果 `value` 为 `DEFAULT` 或者等效地使用了 `RESET` ，角色相关的变量设置会被移除，这样该角色将会在新会话中继承系统范围的默认设置。使用 `RESET ALL` 可清除所有角色相关的设置。 `SET FROM CURRENT` 可以把会话中该参数的当前值保存为角色相关的值。如果指定了 `IN DATABASE` ，只会为给定的角色和数据库设置或者移除该配置参数。
	角色相关的变量设置只在登录时生效， `SET ROLE` 以及 `SET SESSION AUTHORIZATION` 不会处理角色相关的变量设置。

**注解**

使用 `CREATE ROLE` 增加新角色，使用 `DROP ROLE` 移除一个角色。

`ALTER ROLE` 无法更改一个角色成员关系。可以使用 `GRANT` 和 `REVOKE` 来实现。

在使用这个命令指定一个未加密口令时要多加小心。该口令将会以明文传送到服务器，并且它还可能会被记录在客户端的命令历史或者服务器日志中。 `psql` 包含了一个命令 `\password` ，它可以被用来更改一个角色的口令而不暴露明文口令。

也可以把一个会话默认值绑定到一个指定的数据库而不是一个角色，详见 `ALTER DATABASE` 。

如果出现冲突，数据库角色相关的设置会覆盖角色相关的设置，角色相关的又会覆盖数据库相关的设置。

**示例**

更改一个角色的口令：

```sql
ALTER ROLE davide WITH PASSWORD 'hu8jmn3';
```

移除一个角色的口令：

```sql
ALTER ROLE davide WITH PASSWORD NULL;
```

更改一个口令的失效日期，指定该口令应该在 2015 年 5 月 4 日中午（在一个比 UTC 快 1 小时的时区）过期：

```sql
ALTER ROLE chris VALID UNTIL 'May 4 12:00:00 2015 +1';
```

让一个口令永远有效：

```sql
ALTER ROLE fred VALID UNTIL 'infinity';
```

让一个角色能够创建其他角色和新的数据库：

```sql
ALTER ROLE miriam CREATEROLE CREATEDB;
```

为一个角色指定 `maintenance_work_mem` 参数的非默认设置：

```sql
ALTER ROLE worker_bee SET maintenance_work_mem = 100000;
```

为一个角色指定 `client_min_messages` 参数的数据库相关的非默认设置：

```sql
ALTER ROLE fred IN DATABASE devel SET client_min_messages = DEBUG;
```

**兼容性**

`ALTER ROLE` 语句是一个瀚高数据库扩展。

**另见**

```sql
CREATE ROLE\`, \`DROP ROLE\`, \`ALTER DATABASE\`, \`SET
```

## ALTER ROUTINE

— 更改一个例程的定义

**大纲**

```sql
ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    action [ ... ] [ RESTRICT ]

ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    RENAME TO new_name

ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    SET SCHEMA new_schema

ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    DEPENDS ON EXTENSION extension_name
```

其中 **action** 是下列之一：

```sql
IMMUTABLE | STABLE | VOLATILE | [ NOT ] LEAKPROOF
[ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
PARALLEL { UNSAFE | RESTRICTED | SAFE }
COST execution_cost
ROWS result_rows
SET configuration_parameter { TO | = } { value | DEFAULT }
SET configuration_parameter FROM CURRENT
RESET configuration_parameter
RESET ALL
```

**描述**

`ALTER ROUTINE` 更改一个例程的定义，它可以是聚集函数、普通函数或者过程。参数的描述、更多的例子以及进一步的细节请参考 `ALTER AGGREGATE` 、 `ALTER FUNCTION` 以及 `ALTER PROCEDURE` 。

**示例**

将类型 `integer` 的例程 `foo` 重命名为 `foobar` ：

```sql
ALTER ROUTINE foo(integer) RENAME TO foobar;
```

不管 `foo` 是聚集、函数还是过程，这个命令都能使用。

**兼容性**

这个语句与 SQL 标准中的 `ALTER ROUTINE` 语句部分兼容。更多细节请参考 `ALTER FUNCTION` 和 `ALTER PROCEDURE` 。允许例程名称引用聚集函数是一种瀚高数据库的扩展。

**另见**

```
ALTER AGGREGATE\`, \`ALTER FUNCTION\`, \`ALTER PROCEDURE\`, \`DROP ROUTINE
```

**注意** 没有 `CREATE ROUTINE` 命令。

## ALTER RULE

— 更改一个规则定义

**大纲**

```sql
ALTER RULE name ON table_name RENAME TO new_name
```

**描述**

`ALTER RULE` 更改一条现有规则的定义。当前，唯一可用的动作是更改规则的名称。

要使用 `ALTER RULE` ，你必须拥有该规则适用的表或者视图。

**参数**

- **`name`**  
	要修改的一条现有规则的名称。
- **`table_name`**  
	该规则适用的表或视图的名称（可以是模式限定的）。
- **`new_name`**  
	该规则的新名称。

**示例**

要重命名一条现有的规则：

```sql
ALTER RULE notify_all ON emp RENAME TO notify_me;
```

**兼容性**

`ALTER RULE` 是一种瀚高数据库的语言扩展，整个查询重写系统也是。

**另见**

```sql
CREATE RULE\`, \`DROP RULE
```

## ALTER SCHEMA

— 更改一个模式的定义

**大纲**

```sql
ALTER SCHEMA name RENAME TO new_name

ALTER SCHEMA name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }
```

**描述**

`ALTER SCHEMA` 更改一个模式的定义。

要使用 `ALTER SCHEMA` ，你必须拥有该模式。要重命名一个模式，你还必须拥有该数据库的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该数据库上的 `CREATE` 特权（注意超级用户自动拥有所有这些特权）。

**参数**

- **`name`**  
	一个现有模式的名称。
- **`new_name`**  
	该模式的新名称。新名称不能以 `pg_` 开始，因为这些名称被保留用于系统模式。
- **`new_owner`**  
	该模式的新拥有者。

**兼容性**

在 SQL 标准中没有 `ALTER SCHEMA` 语句。

**另见**

```sql
CREATE SCHEMA\`, \`DROP SCHEMA
```

## ALTER SEQUENCE

— 更改一个序列发生器的定义

**大纲**

```sql
ALTER SEQUENCE [ IF EXISTS ] name
    [ AS data_type ]
    [ INCREMENT [ BY ] increment ]
    [ MINVALUE minvalue | NO MINVALUE ] [ MAXVALUE maxvalue | NO MAXVALUE ]
    [ START [ WITH ] start ]
    [ RESTART [ [ WITH ] restart ] ]
    [ CACHE cache ] [ [ NO ] CYCLE ]
    [ OWNED BY { table_name.column_name | NONE } ]

ALTER SEQUENCE [ IF EXISTS ] name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER SEQUENCE [ IF EXISTS ] name RENAME TO new_name

ALTER SEQUENCE [ IF EXISTS ] name SET SCHEMA new_schema
```

**描述**

`ALTER SEQUENCE` 更改一个现有序列发生器的参数。任何没有在 `ALTER SEQUENCE` 命令中明确设置的参数保持它们之前的设置。

要使用 `ALTER SEQUENCE` ，你必须拥有该序列。要更改一个序列的模式，你还必须拥有新模式上的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该域的模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建该序列做不到的事情。不过，一个超级用户怎么都能更改任何序列的所有权。）。

**参数**

- **`name`**  
	要修改的序列的名称（可以是模式限定的）。
- **`IF EXISTS`**  
	在序列不存在时不要抛出一个错误。这种情况下会发出一个提示。
- **`data_type`**  
	可选子句 `AS data_type` 改变序列的数据类型。有效类型是 `smallint` 、 `integer` 和 `bigint` 。
	当且仅当先前的最小值和最大值是旧数据类型的最小值或最大值时（换句话说，如果序列是使用 `NO MINVALUE` 或 `NO MAXVALUE` ，隐式或显式创建的），则更改数据类型会自动更改序列的最小值和最大值。否则，将保留最小值和最大值，除非将新值作为同一命令的一部分给出。如果最小值和最大值不符合新的数据类型，则会生成错误。
- **`increment`**  
	子句 `INCREMENT BY increment` 是可选的。一个正值将产生一个上升序列，一个负值会产生一个下降序列。如果没有指定，旧的增量值将被保持。
- **`minvalue`**
- **`NO MINVALUE`**  
	可选的子句 `MINVALUE minvalue` 决定一个序列能产生的最小值。如果指定了 `NO MINVALUE` ，上升序列和下降序列的默认值分别是 1 和数据类型的最小值。如果这些选项都没有被指定，将保持当前的最小值。
- **`maxvalue`**
- **`NO MAXVALUE`**  
	可选的子句 `MAXVALUE maxvalue` 决定一个序列能产生的最大值。如果指定了 `NO MAXVALUE` ，上升序列和下降序列的默认值分别是数据类型的最大值和 -1。如果这些选项都没有被指定，将保持当前的最大值。
- **`start`**  
	可选的子句 `START WITH start` 更改该序列被记录的开始值。这对于当前序列值没有影响，它会简单地设置未来 `ALTER SEQUENCE RESTART` 命令将会使用的值。
- **`restart`**  
	可选的子句 `RESTART [ WITH restart ]` 更改该序列的当前值。这类似于用 `is_called = false` 调用 `setval` 函数：被指定的值将会被下一次 `nextval` 调用返回。写上没有 `restart` 值的 `RESTART` 等效于提供被 `CREATE SEQUENCE` 记录的或者上一次被 `ALTER SEQUENCE START WITH` 设置的开始值。
	与 `setval` 调用相比，序列上的 `RESTART` 操作是事务性的并阻止并发事务从同一序列中获取数字。如果这不是所需的操作模式，则应使用 `setval` 。
- **`cache`**  
	子句 `CACHE cache` 使得序列数字被预先分配并且保存在内存中以便更快的访问。最小值是 1（每次只产生一个值，即无缓存）。如果没有指定，旧的缓冲值将被保持。
- **`CYCLE`**  
	可选的 `CYCLE` 关键词可以被用来允许该序列在达到 `maxvalue` （上升序列）或 `minvalue` （下降序列）时回卷。如果到达该限制，下一个被产生的数字将分别是 `minvalue` 或者 `maxvalue` 。
- **`NO CYCLE`**  
	如果指定了可选的 `NO CYCLE` 关键词，任何在该序列到达其最大值后的 `nextval` 调用将会返回一个错误。如果既没有指定 `CYCLE` 也没有指定 `NO CYCLE` ，旧的循环行为将被保持。
- **`OWNED BY table_name.column_name`**
- **`OWNED BY NONE`**  
	`OWNED BY` 选项导致该序列与一个特定的表列相关联，这样如果该列（或者整个表）被删除，该序列也会被自动删除。如果指定，这种关联会替代之前为该序列指定的任何关联。被指定的表必须具有相同的拥有者并且与该序列在同一个模式中。指定 `OWNED BY NONE` 可以移除任何现有的关联，让该序列 “自立”。
- **`new_owner`**  
	该序列的新拥有者的用户名。
- **`new_name`**  
	该序列的新名称。
- **`new_schema`**  
	该序列的新模式。

**注解**

`ALTER SEQUENCE` 将不会立即影响除当前后端外其他后端中的 `nextval` 结果，因为它们有预分配（缓存）的序列值。在注意到序列生成参数被更改之前它们将用尽所有缓存的值。当前后端将被立刻影响。

`ALTER SEQUENCE` 不会影响该序列的 `currval` 状态。

`ALTER SEQUENCE` 阻塞并发 `nextval` 、 `currval` 、 `lastval` 和 `setval` 调用。

由于历史原因， `ALTER TABLE` 也可以被用于序列，但是只有等效于上述形式的 `ALTER TABLE` 变体才被允许用于序列。

**示例**

在 105 重启一个被称为 `serial` 的序列：

```sql
ALTER SEQUENCE serial RESTART WITH 105;
```

**兼容性**

`ALTER SEQUENCE` 符合 SQL 标准，不过 `AS` 、 `START WITH` 、 `OWNED BY` 、 `OWNER TO` 、 `RENAME TO` 以及 `SET SCHEMA` 子句是瀚高数据库扩展。

**另见**

```sql
CREATE SEQUENCE\`, \`DROP SEQUENCE
```

## ALTER SERVER

— 更改一个外部服务器的定义

**大纲**

```sql
ALTER SERVER name [ VERSION 'new_version' ]
    [ OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] ) ]

ALTER SERVER name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER SERVER name RENAME TO new_name
```

**描述**

`ALTER SERVER` 更改一个外部服务器的定义。第一种形式更改该服务器的版本字符串或者该服务器的一般选项（至少要求一个子句）。第二种形式更改该服务器的拥有者。

要修改该服务器，你必须是它的拥有者。此外为了修改拥有者，你必须拥有该服务器并且是新拥有角色的一个直接或者间接成员，并且你必须具有该服务器的外部数据包装器上的 `USAGE` 特权（注意超级用户自动满足所有这些政策）。

**参数**

- **`name`**  
	一个现有服务器的名称。
- **`new_version`**  
	新的服务器版本。
- **`OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )`**  
	更改该服务器的选项。 `ADD` 、 `SET` 和 `DROP` 指定要执行的动作。如果没有显式地指定操作，将会假定为 `ADD` 。选项名称必须唯一，名称和值也会使用该服务器的外部数据包装器库进行验证。
- **`new_owner`**  
	该外部服务器的新拥有者的用户名。
- **`new_name`**  
	该外部服务器的新名称。

**示例**

修改服务器 `foo` ，增加连接选项：

```sql
ALTER SERVER foo OPTIONS (host 'foo', dbname 'foodb');
```

修改服务器 `foo` ，更改版本、更改 `host` 选项：

```sql
ALTER SERVER foo VERSION '8.4' OPTIONS (SET host 'baz');
```

**兼容性**

`ALTER SERVER` 符合 ISO/IEC 9075-9 (SQL/MED)。 `OWNER TO` 和 `RENAME` 形式是瀚高数据库扩展。

**另见**

```sql
CREATE SERVER\`, \`DROP SERVER
```

## ALTER STATISTICS

— 更改扩展统计对象的定义

**大纲**

```sql
ALTER STATISTICS name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER STATISTICS name RENAME TO new_name

ALTER STATISTICS name SET SCHEMA new_schema
```

**描述**

`ALTER STATISTICS` 更改现有扩展统计对象的参数。任何在 `ALTER STATISTICS` 命令中没有明确设定的参数保持它们之前的设置。

您必须拥有统计对象才能使用 `ALTER STATISTICS` 。要更改统计对象的模式，还必须在新模式上具有 `CREATE` 权限。要更改所有者，还必须是新所有者角色的直接或间接成员，且该角色在统计对象的模式上必须具有 `CREATE` 权限。（这些限制强制了通过删除和重新创建统计对象来改变所有者不会做任何你不能做的事情，但是超级用户可以改变任何统计对象的所有权。）

**参数**

- **`name`**  
	要修改的统计对象的名称（可能有模式修饰）。
- **`new_owner`**  
	统计对象的新所有者的用户名。
- **`new_name`**  
	统计对象的新名称。
- **`new_schema`**  
	统计对象的新模式。

**兼容性**

SQL 标准中没有 `ALTER STATISTICS` 命令。

**参见**

```sql
CREATE STATISTICS\`, \`DROP STATISTICS
```

## ALTER SUBSCRIPTION

— 修改订阅的定义

**大纲**

```sql
ALTER SUBSCRIPTION name CONNECTION 'conninfo'

ALTER SUBSCRIPTION name SET PUBLICATION publication_name [, ...] 
    [ WITH ( set_publication_option [= value] [, ... ] ) ]

ALTER SUBSCRIPTION name REFRESH PUBLICATION 
    [ WITH ( refresh_option [= value] [, ... ] ) ]

ALTER SUBSCRIPTION name ENABLE

ALTER SUBSCRIPTION name DISABLE

ALTER SUBSCRIPTION name SET ( subscription_parameter [= value] [, ... ] )

ALTER SUBSCRIPTION name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER SUBSCRIPTION name RENAME TO new_name
```

**描述**

`ALTER SUBSCRIPTION` 可以修改大部分可以在 `CREATE SUBSCRIPTION` 中指定的订阅属性。

要使用 `ALTER SUBSCRIPTION` ，你必须拥有该订阅。要改变所有者，你也必须是新所有者的直接或间接成员。新所有者必须是超级用户。（目前，所有的订阅所有者必须是超级用户，所以所有者的检查将在实践中被绕过，但这可能在未来发生变化。）

**参数**

- **`name`**  
	要修改属性的订阅的名称。
- **`CONNECTION 'conninfo'`**  
	该子句修改最初由 `CREATE SUBSCRIPTION` 设置的连接属性。
- **`SET PUBLICATION publication_name`**  
	更改订阅发布的列表。参阅 `CREATE SUBSCRIPTION` 获取更多信息。默认情况下，此命令也将像 `REFRESH PUBLICATION` 一样工作。
	**`set_publication_option`** 指定了这个操作的附加选项。支持的选项是：
	- **`refresh`** (boolean)  
		如果为 `false` ，则该命令将不会尝试刷新表信息。然后应单独执行 `REFRESH PUBLICATION` 。默认值是 `true` 。
	此外，可以指定 `REFRESH PUBLICATION` 下描述的刷新选项。
- **`REFRESH PUBLICATION`**  
	从发布者获取缺少的表信息。这将开始复制自上次调用 `REFRESH PUBLICATION` 或从 `CREATE SUBSCRIPTION` 以来添加到订阅发布中的表。
	**`refresh_option`** 指定了刷新操作的附加选项。支持的选项有：
	- **`copy_data`** (boolean)  
		指定在复制启动后是否应复制正在订阅的发布中的现有数据。默认值是 `true` 。（以前订阅的表不会被复制。）
- **`ENABLE`**  
	启用先前禁用的订阅，在事务结束时启动逻辑复制工作。
- **`DISABLE`**  
	禁用正在运行的订阅，在事务结束时停止逻辑复制工作。
- **`SET ( subscription_parameter [= value] [, ... ] )`**  
	该子句修改原先由 `CREATE SUBSCRIPTION` 设置的参数。允许的选项是 `slot_name` 和 `synchronous_commit` 。
- **`new_owner`**  
	订阅的新所有者的用户名。
- **`new_name`**  
	订阅的新名称。

**示例**

将订阅的发布更改为 `insert_only` ：

```sql
ALTER SUBSCRIPTION mysub SET PUBLICATION insert_only;
```

禁用（停止）订阅：

```sql
ALTER SUBSCRIPTION mysub DISABLE;
```

**兼容性**

`ALTER SUBSCRIPTION` 是瀚高数据库的一个扩展。

**参见**

```sql
CREATE SUBSCRIPTION\`, \`DROP SUBSCRIPTION\`, \`CREATE PUBLICATION\`, \`ALTER PUBLICATION
```

## ALTER SYSTEM

— 更改一个服务器配置参数

**大纲**

```sql
ALTER SYSTEM SET configuration_parameter { TO | = } { value | 'value' | DEFAULT }

ALTER SYSTEM RESET configuration_parameter

ALTER SYSTEM RESET ALL
```

**描述**

`ALTER SYSTEM` 被用来在整个数据库集簇范围内更改服务器配置参数。它比传统的手动编辑 `postgresql.conf` 文件的方法更方便。 `ALTER SYSTEM` 会把给出的参数设置写入到 `postgresql.auto.conf` 文件中，该文件会随着 `postgresql.conf` 一起被读入。把一个参数设置为 `DEFAULT` 或者使用 `RESET` 变体可以把该配置项从 `postgresql.auto.conf` 文件中移除。

使用 `RESET ALL` 可以移除所有这类配置项。

用 `ALTER SYSTEM` 设置的值将在下一次重载服务器配置后生效，那些只能在服务器启动时更改的参数则会在下一次服务器重启后生效。重载服务器配置可以通过以下做法实现：调用 SQL 函数 `pg_reload_conf()` ，运行 `pg_ctl reload` 或者向主服务器进程发送一个 `SIGHUP` 信号。

只有超级用户能够使用 `ALTER SYSTEM` 。还有，由于这个命令直接作用于文件系统并且不能被回滚，不允许在一个事务块或者函数中使用它。

**参数**

- **`configuration_parameter`**  
	一个可设置配置参数的名称。可用的参数可见第 19 章。
- **`value`**  
	该参数的新值。值可以被指定为字符串常量、标识符、数字或者以上这些构成的逗号分隔的列表，值的具体形式取决于特定的参数。写上 `DEFAULT` 可以用来把该参数及其值从 `postgresql.auto.conf` 中移除。

**注解**

不能用这个命令来设置 `data_directory` 以及 `postgresql.conf` 中不被允许的参数（例如 preset options）。

**示例**

设置 `wal_level` ：

```sql
ALTER SYSTEM SET wal_level = replica;
```

撤销以上的设置，恢复 `postgresql.conf` 中有效的设置：

```sql
ALTER SYSTEM RESET wal_level;
```

**兼容性**

`ALTER SYSTEM` 语句是一种瀚高数据库扩展。

**另见**

```sql
SET\`, \`SHOW
```

## ALTER TABLE

— 更改一个表的定义

**大纲**

```sql
ALTER TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    action [, ... ]

ALTER TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    RENAME [ COLUMN ] column_name TO new_column_name

ALTER TABLE [ IF EXISTS ] [ ONLY ] name [ * ]
    RENAME CONSTRAINT constraint_name TO new_constraint_name

ALTER TABLE [ IF EXISTS ] name
    RENAME TO new_name

ALTER TABLE [ IF EXISTS ] name
    SET SCHEMA new_schema

ALTER TABLE ALL IN TABLESPACE name [ OWNED BY role_name [, ... ] ]
    SET TABLESPACE new_tablespace [ NOWAIT ]

ALTER TABLE [ IF EXISTS ] name
    ATTACH PARTITION partition_name { FOR VALUES partition_bound_spec | DEFAULT }

ALTER TABLE [ IF EXISTS ] name
    DETACH PARTITION partition_name
```

其中 **action** 是以下之一：

```sql
ADD [ COLUMN ] [ IF NOT EXISTS ] column_name data_type [ COLLATE collation ]
    [ column_constraint [ ... ] ]

DROP [ COLUMN ] [ IF EXISTS ] column_name [ RESTRICT | CASCADE ]

ALTER [ COLUMN ] column_name [ SET DATA ] TYPE data_type [ COLLATE collation ]
    [ USING expression ]

ALTER [ COLUMN ] column_name SET DEFAULT expression

ALTER [ COLUMN ] column_name DROP DEFAULT

ALTER [ COLUMN ] column_name { SET | DROP } NOT NULL

ALTER [ COLUMN ] column_name ADD GENERATED { ALWAYS | BY DEFAULT } AS
    IDENTITY [ ( sequence_options ) ]

ALTER [ COLUMN ] column_name { SET GENERATED { ALWAYS | BY DEFAULT } |
    SET sequence_option | RESTART [ [ WITH ] restart ] } [...]

ALTER [ COLUMN ] column_name DROP IDENTITY [ IF EXISTS ]

ALTER [ COLUMN ] column_name SET STATISTICS integer

ALTER [ COLUMN ] column_name SET ( attribute_option = value [, ... ] )

ALTER [ COLUMN ] column_name RESET ( attribute_option [, ... ] )

ALTER [ COLUMN ] column_name SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN }

ADD table_constraint [ NOT VALID ]

ADD table_constraint_using_index

ALTER CONSTRAINT constraint_name [ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY
    DEFERRED | INITIALLY IMMEDIATE ]

VALIDATE CONSTRAINT constraint_name

DROP CONSTRAINT [ IF EXISTS ] constraint_name [ RESTRICT | CASCADE ]

DISABLE TRIGGER [ trigger_name | ALL | USER ]

ENABLE TRIGGER [ trigger_name | ALL | USER ]

ENABLE REPLICA TRIGGER trigger_name

ENABLE ALWAYS TRIGGER trigger_name

DISABLE RULE rewrite_rule_name

ENABLE RULE rewrite_rule_name

ENABLE REPLICA RULE rewrite_rule_name

ENABLE ALWAYS RULE rewrite_rule_name

DISABLE ROW LEVEL SECURITY

ENABLE ROW LEVEL SECURITY

FORCE ROW LEVEL SECURITY

NO FORCE ROW LEVEL SECURITY

CLUSTER ON index_name

SET WITHOUT CLUSTER

SET WITHOUT OIDS

SET TABLESPACE new_tablespace

SET { LOGGED | UNLOGGED }

SET ( storage_parameter = value [, ... ] )

RESET ( storage_parameter [, ... ] )

INHERIT parent_table

NO INHERIT parent_table

OF type_name

NOT OF

OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

REPLICA IDENTITY { DEFAULT | USING INDEX index_name | FULL | NOTHING }
```

**partition\_bound\_spec** 是:

```sql
IN ( partition_bound_expr [, ...] ) |
FROM ( { partition_bound_expr | MINVALUE | MAXVALUE } [, ...] )
  TO ( { partition_bound_expr | MINVALUE | MAXVALUE } [, ...] ) |
WITH ( MODULUS numeric_literal, REMAINDER numeric_literal )
```

**column\_constraint** 是:

```sql
[ CONSTRAINT constraint_name ]
{ NOT NULL |
  NULL |
  CHECK ( expression ) [ NO INHERIT ] |
  DEFAULT default_expr |
  GENERATED ALWAYS AS ( generation_expr ) STORED |
  GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY [ ( sequence_options ) ] |
  UNIQUE index_parameters |
  PRIMARY KEY index_parameters |
  REFERENCES reftable [ ( refcolumn ) ] [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ]
    [ ON DELETE referential_action ] [ ON UPDATE referential_action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
```

而 **table\_constraint** 是：

```sql
[ CONSTRAINT constraint_name ]
{ CHECK ( expression ) [ NO INHERIT ] |
  UNIQUE ( column_name [, ... ] ) index_parameters |
  PRIMARY KEY ( column_name [, ... ] ) index_parameters |
  EXCLUDE [ USING index_method ] ( exclude_element WITH operator
    [, ... ] ) index_parameters [ WHERE ( predicate ) ] |
  FOREIGN KEY ( column_name [, ... ] ) REFERENCES reftable [ ( refcolumn
    [, ... ] ) ]
    [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ] [ ON DELETE action ] [ ON
    UPDATE action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
```

并且 **table\_constraint\_using\_index** 是：

```sql
[ CONSTRAINT constraint_name ]
{ UNIQUE | PRIMARY KEY } USING INDEX index_name
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
```

**UNIQUE** 、 **PRIMARY KEY** 以及 **EXCLUDE** 约束中的 **index\_parameters** 是：

```sql
[ INCLUDE ( column_name [, ... ] ) ]
[ WITH ( storage_parameter [= value] [, ... ] ) ]
[ USING INDEX TABLESPACE tablespace_name ]
```

**exclude\_element** in an **EXCLUDE** constraint is:

```sql
{ column_name | ( expression ) } [ opclass ] [ ASC | DESC ] [ NULLS { FIRST | LAST } ]
```

**描述**

`ALTER TABLE` 更改一个现有表的定义。下文描述了几种形式。注意每一种形式所要求的锁级别可能不同。如果没有明确说明，将会持有一个 `ACCESS EXCLUSIVE` 锁。当列出多个子命令时，所持有的锁将是子命令所要求的最严格的那一个。

**ADD COLUMN \[ IF NOT EXISTS \]**

这种形式向该表增加一个新列，使用与 `CREATE TABLE` 相同的语法。如果指定了 `IF NOT EXISTS` 并且使用这个名字的列已经存在，则不会抛出错误。

**DROP COLUMN \[ IF EXISTS \]**

这种形式从表删除一列。涉及到该列的索引和表约束也将会被自动删除。如果该列的移除会导致引用它的多元统计信息仅包含单一列的数据，则该多元统计信息也将被移除。

如果在该表之外有任何东西（例如外键引用或者视图）依赖于该列，你将需要用到 `CASCADE` 。如果指定了 `IF EXISTS` 但该列不存在，则不会抛出错误。这种情况中会发出一个提示。

**SET DATA TYPE**

这种形式更改表中一列的类型。涉及到该列的索引和简单表约束将通过重新解析最初提供的表达式被自动转换为使用新的列类型。可选的 `COLLATE` 子句为新列指定一种排序规则，如果被省略，排序规则会是新列类型的默认排序规则。可选的 `USING` 子句指定如何从旧的列值计算新列值，如果被省略，默认的转换和从旧类型到新类型的赋值造型一样。如果没有从旧类型到新类型的隐式或者赋值造型，则必须提供一个 `USING` 子句。

**SET/DROP DEFAULT**

这些形式为一列设置或者移除默认值。默认值只在后续的 `INSERT` 或 `UPDATE` 命令中生效，它们不会导致已经在表中的行改变。

**SET/DROP NOT NULL**

这些形式更改一列是否被标记为允许空值或者拒绝空值。

`SET NOT NULL` 只能应用于列，前提是表中没有任何记录包含该列的 `NULL` 值。通常，这一点在 `ALTER TABLE` 全表扫描时来检查；但是，如果找到有效的 `CHECK` 约束证明不存在 `NULL` ，则跳过表扫描。

如果这个表是一个分区，对于在父表中被标记为 `NOT NULL` 的列，不能在其上执行 `DROP NOT NULL` 。要从所有的分区中删除 `NOT NULL` 约束，可以在父表上执行 `DROP NOT NULL` 。即使在父表上没有 `NOT NULL` 约束，这样的约束还是能被增加到分区上。也就是说，即便父表允许空值，子表也可以不允许空值，但反过来不行。

**ADD GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY**

**SET GENERATED { ALWAYS | BY DEFAULT }**

**DROP IDENTITY \[ IF EXISTS \]**

这些形式更改一列是否是一个标识列，或者是更改一个已有的标识列的产生属性。

如果 `DROP IDENTITY IF EXISTS` 被指定并且该列不是一个标识列，则不会有错误被抛出。在这种情况下会发出一个提示。

**SET sequence\_option**

**RESTART**

这些形式修改位于一个现有标识列之下的序列。 `sequence_option` 是一个 `ALTER SEQUENCE` 所支持的选项，例如 `INCREMENT BY` 。

**SET STATISTICS**

这种形式为后续的 `ANALYZE` 操作设置针对每列的统计收集目标。目标可以被设置在范围 0 到 10000 之间，还可以把它设置为 -1 来恢复到使用系统默认的统计目标（ `default_statistics_target` ）。

`SET STATISTICS` 要求一个 `SHARE UPDATE EXCLUSIVE` 锁。

**SET ( attribute\_option = value \[, … \] )**

**RESET ( attribute\_option \[, … \] )**

这种形式设置或者重置每个属性的选项。当前，已定义的针对每个属性的选项只有 `n_distinct` 和 `n_distinct_inherited` ，它们会覆盖后续 `ANALYZE` 操作所得到的可区分值数量估计。 `n_distinct` 影响该表本身的统计信息，而 `n_distinct_inherited` 影响为该表外加其继承子女收集的统计信息。当被设置为一个正值时， `ANALYZE` 将假定该列刚好包含指定数量的可区分非空值。当被设置为一个负值（必须大于等于 -1）时， `ANALYZE` 将假定可区分非空值的数量与表的尺寸成线性比例，确切的计数由估计的表尺寸乘以给定数字的绝对值计算得到。例如，值 -1 表示该列中所有的值都是可区分的，而值 -0.5 则表示每一个值平均出现两次。当表的尺寸随时间变化时，这会有所帮助，因为这种计算只有在查询规划时才会被执行。指定值为 0 将回到正常的估计可区分值数量的做法。

更改针对每个属性的选项要求一个 `SHARE UPDATE EXCLUSIVE` 锁。

**SET STORAGE**

这种形式为一列设置存储模式。这会控制这列是会被保持在线内还是放在一个二级 `TOAST` 表中，以及数据是否应被压缩。对于 `integer` 之类的定长、线内、未压缩值必须使用 `PLAIN` 。 `MAIN` 用于线内、可压缩的数据。 `EXTERNAL` 用于外部的、未压缩数据。而 `EXTENDED` 用于外部的、压缩数据。对于大部分支持非- `PLAIN` 存储的数据类型， `EXTENDED` 是默认值。使用 `EXTERNAL` 将会让很大的 `text` 和 `bytea` 之上的子串操作运行得更快，但是代价是存储空间会增加。注意 `SET STORAGE` 本身并不改变表中的任何东西，它只是设置在未来的表更新时要追求的策略。

**ADD table\_constraint \[ NOT VALID \]**

这种形式使用和 `CREATE TABLE` 相同的语法外加 `NOT VALID` 选项为一个表增加一个新的约束，该选项当前只被允许用于外键和 `CHECK` 约束。

通常，此窗体将导致对表进行扫描，以验证表中的所有现有行是否满足新约束。但是如果使用了 `NOT VALID` 选项，则跳过此可能很漫长的扫描。该约束仍将被强制到后续的插入和删除上（也就是说，在外键的情况下如果在被引用表中没有一个匹配的行，操作会失败；或者如果新行不匹配指定的检查条件，操作也会失败）。但是数据库不会假定约束对该表中的所有行都成立，直到通过使用 `VALIDATE CONSTRAINT` 选项对它进行验证。参见下述 Notes 以了解关于使用 `NOT VALID` 选项的更多信息。

除了接收约束的表上的锁外，外键约束的增加要求在被引用表上的一个 `SHARE ROW EXCLUSIVE` 锁。

当唯一或者主键约束被添加到分区表时，会有额外的限制，请参考 `CREATE TABLE` 。此外，当前分区表上的外键约束不能被声明为 `NOT VALID` 。

**ADD table\_constraint\_using\_index**

这种形式基于一个已有的唯一索引为一个表增加新的 `PRIMARY KEY` 或 `UNIQUE` 约束。该索引中的所有列将被包括在约束中。

该索引不能有表达式列或者是一个部分索引。还有，它必须是一个带有默认排序顺序的 B-树索引。这些限制确保该索引等效于使用常规 `ADD PRIMARY KEY` 或者 `ADD UNIQUE` 命令时创建的索引。

如果 `PRIMARY KEY` 被指定，并且该索引的列没有被标记 `NOT NULL` ，那么这个命令将尝试对每一个这样的列做 `ALTER COLUMN SET NOT NULL` 。这需要一次全表扫描来验证这些列不包含空值。在所有其他情况中，这都是一种很快的操作。

如果提供了一个约束名，那么该索引将被重命名以匹配该约束名。否则该约束将被命名成索引的名称。

这个命令被执行后，该索引被增加的约束”拥有”，这和用常规 `ADD PRIMARY KEY` 或 `ADD UNIQUE` 命令创建的索引一样。特别地，删掉该约束将会导致该索引也消失。

当前在分区表上不支持这种形式。

> **注意：**  
> 如果需要增加一个新的约束但是不希望长时间阻塞表更新，那么使用现有索引增加约束会有所帮助。要这样做，用 `CREATE INDEX CONCURRENTLY` 创建该索引，并且接着使用这种语法把它安装为一个正式的约束。例子见下文。

**ALTER CONSTRAINT**

这种形式修改之前创建的一个约束的属性。当前只能修改外键约束。

**VALIDATE CONSTRAINT**

这种形式验证之前创建为 `NOT VALID` 的外键或检查约束，它会扫描表来确保对于该约束没有行不满足约束。如果约束已经被标记为合法，则什么也不会发生。（参见下述 Notes 以了解此命令用途的说明。）

**DROP CONSTRAINT \[ IF EXISTS \]**

这种形式在一个表上删除指定的约束，还有位于该约束之下的任何索引。如果 `IF EXISTS` 被指定并且该约束不存在，不会抛出错误。在这种情况下会发出一个提示。

**DISABLE/ENABLE \[ REPLICA | ALWAYS \] TRIGGER**

这些形式配置属于该表的触发器的触发设置。系统仍然知道被禁用触发器的存在，但是即使它的触发事件发生也不会执行它。对于一个延迟触发器，会在事件发生时而不是触发器函数真正被执行时检查其启用状态。可以禁用或者启用用名称指定的单个触发器、表上的所有触发器、用户拥有的触发器（这个选项会排除内部生成的约束触发器，例如用来实现外键约束或可延迟唯一和排除约束）。禁用或者启用内部生成的约束触发器要求超级用户特权，这样做要小心因为如果这类触发器不被执行，约束的完整性当然无法保证。

触发器引发机制也受到配置变量 `session_replication_role` 的影响。当复制角色是 “origin”（默认）或者 “local” 时，被简单启用的触发器将被触发。被配置为 `ENABLE REPLICA` 的触发器只有在会话处于 “replica” 模式时才将被触发。被配置为 `ENABLE ALWAYS` 的触发器的触发不会考虑当前复制角色。

这种机制的效果就是，在默认配置中，触发器不会在复制体上引发。这种效果很有用，因为如果一个触发器在源头上被用来在表之间传播数据，那么复制系统也将复制被传播的数据，并且触发器不应该在复制体上引发第二次，因为那会导致重复。不过，如果一个触发器被用于另一种目的（例如创建外部告警），那么将它设置为 `ENABLE ALWAYS` 可能更加合适，这样它在复制体上也会被引发。

这个命令要求一个 `SHARE ROW EXCLUSIVE` 锁。

**DISABLE/ENABLE \[ REPLICA | ALWAYS \] RULE**

这些形式配置属于表的重写规则的触发设置。系统仍然知道一个被禁用规则的存在，但在查询重写时不会应用它。其语义与禁用的/启用的触发器的一样。对于 `ON SELECT` 规则会忽略这个配置，即使当前会话处于一种非默认的复制角色，这类规则总是会被应用以保持视图工作正常。

规则引发机制也受到配置变量 `session_replication_role` 的影响，这和上述的触发器类似。

**DISABLE/ENABLE ROW LEVEL SECURITY**

这些形式控制属于该表的行安全性策略的应用。如果被启用并且该表上不存在策略，则将应用一个默认否定的策略。注意即使行级安全性被禁用，在表上还是可以存在策略。在这种情况下，这些策略将不会被应用并且会被忽略。另见 `CREATE POLICY` 。

**NO FORCE/FORCE ROW LEVEL SECURITY**

这些形式控制当用户是表拥有者时表上的行安全性策略的应用。如果被启用，当用户是表拥有者时，行级安全性策略将被应用。如果被禁用（默认），则当用户是表拥有者时，行级安全性将不会被应用。另见 `CREATE POLICY` 。

**CLUSTER ON**

这种形式为未来的 `CLUSTER` 操作选择默认的索引。它不会真正地对表进行聚簇。

改变聚簇选项要求一个 `SHARE UPDATE EXCLUSIVE` 锁。

**SET WITHOUT CLUSTER**

这种形式从表中移除最近使用的 `CLUSTER` 索引说明。这会影响未来的不指定索引的聚簇操作。

改变聚簇选项要求一个 `SHARE UPDATE EXCLUSIVE` 锁。

**SET WITHOUT OIDS**

向后兼容的语法，用于删除 `oid` 系统列。由于 `oid` 系统列无法再添加，所以不会有实际效果。

**SET TABLESPACE**

这种形式把该表的表空间更改为指定的表空间并且把该表相关联的数据文件移动到新的表空间中。表上的索引（如果有）不会被移动，但是它们可以用额外的 `SET TABLESPACE` 命令单独移动。当应用于分区表时，不会移动，但之后用 `CREATE TABLE PARTITION OF` 创建的任何分区将使用该表空间，除非 `TABLESPACE` 子句用于重写它。

当前数据库在一个表空间中的所有表可以用 `ALL IN TABLESPACE` 形式移动，这将会首先锁住所有将被移动的表然后逐个移动。这种形式也支持 `OWNED BY` ，它将只移动指定角色所拥有的表。如果指定了 `NOWAIT` 选项，则命令将在无法立刻获得所有所需要的锁时失败。注意这个命令不移动系统目录；如果想要移动系统目录，应该用 `ALTER DATABASE` 或者显式的 `ALTER TABLE` 调用。对于这种形式来说， `information_schema` 关系不被认为是系统目录的一部分，因此它们将会被移动。另见 `CREATE TABLESPACE` 。

**SET { LOGGED | UNLOGGED }**

这种形式将表从 `UNLOGGED` 变为 `LOGGED` 或者从 `LOGGED` 更改为 `UNLOGGED` 。该参数不能应用于临时表。

**SET ( storage\_parameter = value \[, … \] )**

这种形式为该表更改一个或者更多存储参数。可用的参数请见存储参数。注意这个命令将不会立刻修改表内容，这取决于重写表以得到想要的结果可能需要的参数。可以用 `VACUUM FULL` 、 `CLUSTER` 或者 `ALTER TABLE` 的一种形式来强制一次表重写。对于规划器相关的参数，更改将从该表下一次被锁定开始生效，因此当前执行的查询不会受到影响。

对 `fillfactor` 、 `toast` 以及 `autovacuum` 存储参数，将会拿取 `SHARE UPDATE EXCLUSIVE` 锁，就像计划器参数 `parallel_workers` 。

**RESET ( storage\_parameter \[, … \] )**

这种形式把一个或者更多存储参数重置到它们的默认值。和 `SET` 一样，可能需要一次表重写来更新整个表。

**INHERIT parent\_table**

这种形式把目标表增加为指定父表的一个新子女。随后，针对父亲的查询将包括目标表中的记录。要被增加为一个子女，目标表必须已经包含和父表完全相同的列（也可以有额外的列）。这些列必须具有匹配的数据类型，并且如果它们在父表中具有 `NOT NULL` 约束，它们在子表中也必须有 `NOT NULL` 约束。

也必须把子表约束与所有父表的 `CHECK` 约束进行匹配，不过父表中那些被标记为非可继承（也就是用 `ALTER TABLE ... ADD CONSTRAINT ... NO INHERIT` 创建的）除外，它们会被忽略。所有匹配得上的子表约束不能被标记为不可继承。当前， `UNIQUE` 、 `PRIMARY KEY` 以及 `FOREIGN KEY` 约束没有被考虑，但是这种情况可能会在未来发生变化。

**NO INHERIT parent\_table**

这种形式把目标表从指定父表的子女列表中移除。针对父表的查询将不再包括来自目标表的记录。

**OF type\_name**

这种形式把该表链接到一种组合类型，就好像 `CREATE TABLE OF` 所做的那样。该表的列名和类型列表必须精确地匹配该组合类型。该表必须不从任何其他表继承。这些限制确保 `CREATE TABLE OF` 能允许一个等价的表定义。

**NOT OF**

这种形式解除一个有类型的表和其类型之间的关联。

**OWNER TO**

这种形式把表、序列、视图、物化视图或外部表的拥有者改为指定用户。

**REPLICA IDENTITY**

这种形式更改被写入到预写式日志来标识被更新或删除行的信息。除非使用逻辑复制，这个选项将不会产生效果。 `DEFAULT` （非系统表的默认值）记录主键列（如果有）的旧值。 `USING INDEX` 记录被所提到的索引所覆盖的列的旧值，该索引必须是唯一索引、不是部分索引、不是可延迟索引并且只包括被标记成 `NOT NULL` 的列。 `FULL` 记录行中所有列的旧值。 `NOTHING` 不记录有关旧行的任何信息（这是系统表的默认值）。在所有情况下，除非至少有一个要被记录的列在新旧行版本之间发生变化，将不记录旧值。

**RENAME**

`RENAME` 形式更改一个表（或者一个索引、序列、视图、物化视图或者外部表）的名称、表中一个列的名称或者表的一个约束的名称。在重命名一个具有底层索引的约束时，该索引也会被重命名。它对已存储的数据没有影响。

**SET SCHEMA**

这种形式把该表移动到另一个模式中。相关的该表列拥有的索引、约束和序列也会被移动。

**ATTACH PARTITION partition\_name { FOR VALUES partition\_bound\_spec | DEFAULT }**

这种形式把一个已有表（自身也可能被分区）作为一个分区挂接到目标表。该表可以为特定的值使用 `FOR VALUES` 挂接为分区，或者用 `DEFAULT` 挂接为一个默认分区。对于目标表中的每一个索引，在被挂接的表上都将创建一个响应的索引，如果已经存在等效的索引，该索引将被挂接到目标表的索引，就像执行了 `ALTER INDEX ATTACH PARTITION` 一样。请注意，如果现有表是外表，如果目标表上有 `UNIQUE` 索引，则当前不允许将表作为目标表的分区附加。（参见 `CREATE FOREIGN TABLE` 。）

一个使用 `FOR VALUES` 的分区使用与 `CREATE TABLE` 中 `partition_bound_spec` 相同的语法。分区边界说明必须对应于目标表的分区策略以及分区键。要被挂接的表必须具有和目标表完全相同的所有列，并且不能有多出来的列，而且列的类型也必须匹配。此外，它必须有目标表上所有的 `NOT NULL` 以及 `CHECK` 约束。当前不考虑 `FOREIGN KEY` 约束。来自于父表的 `UNIQUE` 和 `PRIMARY KEY` 约束将被创建在分区上（如果它们还不存在）。如果被挂接的表上的任何 `CHECK` 约束被标记为 `NO INHERIT` ，则命令将失败，这类约束必须被重建且重建时不能有 `NO INHERIT` 子句。

如果新分区是一个常规表，会执行一次全表扫描来检查表中现有行没有违背分区约束。可以通过对表增加一个有效的 `CHECK` 约束来避免这种扫描，该约束可以在运行这个命令之前仅允许满足所需分区约束的行。 `CHECK` 约束可以解决让表无需被扫描就能验证分区约束。但是，如果任一分区键是一个表达式并且该分区不接受 `NULL` 值，这种方式就无效了。如果挂接一个不接受 `NULL` 值的列表分区，还应该为分区键列增加 `NOT NULL` 约束，除非它是一个表达式。

如果新分区是一个外部表，则不需要验证该外部表中的所有行遵守分区约束（有关外部表上的约束请参考 `CREATE FOREIGN TABLE` 中的讨论）。

当一个表有默认分区时，定义新分区会更改默认分区的分区约束。默认分区不能包含任何需要被移动到新分区中的行，并且将被扫描以验证不存在那样的行。如果一个合适的 `CHECK` 约束存在，这种扫描（和新分区的扫描一样）可以被避免。还是和新分区的扫描一样，当默认分区是外部表时这种扫描总是会被跳过。

在父表上附加一个分区获得一个 `SHARE UPDATE EXCLUSIVE` 锁，除了要附加的表和默认分区上的 `ACCESS EXCLUSIVE` 锁（如果有）。

**DETACH PARTITION partition\_name**

这种形式会分离目标表的指定分区。被分离的分区继续作为独立的表存在，但是与它之前挂接的表不再有任何联系。任何被挂接到目标表索引的索引也会被分离。

除了 `RENAME` 、 `SET SCHEMA` 、 `ATTACH PARTITION` 和 `DETACH PARTITION` 之外，所有形式的 `ALTER TABLE` 都作用在单个表上，前面这些形式可以被组合成一个多修改的列表被一起应用。例如，可以在一个命令中增加多个列并且/或者修改多个列的类型。对于大型表来说这会特别有用，因为只需要对表做一趟操作。

要使用 `ALTER TABLE` ，你必须拥有该表。要更改一个表的模式或者表空间，你还必须拥有新模式或表空间上的 `CREATE` 特权。要把一个表作为一个父表的新子表加入，你必须也拥有该父表。此外，要把一个表挂接为另一个表的新分区，你必须拥有被挂接的表。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该表的模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建表做不到的事情。不过，一个超级用户怎么都能更改任何表的所有权。）要增加一个列、修改一列的类型或者使用 `OF` 子句，你还必须具有该数据类型上的 `USAGE` 特权。

**参数**

- **`IF EXISTS`**  
	如果表不存在则不要抛出一个错误。这种情况下会发出一个提示。
- **`name`**  
	要修改的一个现有表的名称（可以是模式限定的）。如果在表名前指定了 `ONLY` ，则只会修改该表。如果没有指定 `ONLY` ，该表及其所有后代表（如果有）都会被修改。可选地，在表名后面可以指定 `*` 用来显式地指示包括后代表。
- **`column_name`**  
	一个新列或者现有列的名称。
- **`new_column_name`**  
	一个现有列的新名称。
- **`new_name`**  
	该表的新名称。
- **`data_type`**  
	一个新列的数据类型或者一个现有列的新数据类型。
- **`table_constraint`**  
	该表的新的表约束。
- **`constraint_name`**  
	一个新约束或者现有约束的名称。
- **`CASCADE`**  
	自动删除依赖于被删除列或约束的对象（例如引用该列的视图），并且接着删除依赖于那些对象的所有对象。
- **`RESTRICT`**  
	如果有任何依赖对象时拒绝删除列或者约束。这是默认行为。
- **`trigger_name`**  
	一个要禁用或启用的触发器的名称。
- **`ALL`**  
	禁用或者启用属于该表的所有触发器（如果有任何触发器是内部产生的约束触发器则需要超级用户特权，例如那些被用来实现外键约束或者可延迟一致性和排他约束的触发器）。
- **`USER`**  
	禁用或者启用属于该表的所有触发器，内部产生的约束触发器（例如那些被用来实现外键约束或者可延迟一致性和排他约束的触发器）除外。
- **`index_name`**  
	一个现有索引的名称。
- **`storage_parameter`**  
	一个表存储参数的名称。
- **`value`**  
	一个表存储参数的新值。根据该参数，该值可能是一个数字或者一个词。
- **`parent_table`**  
	要与这个表关联或者解除关联的父表。
- **`new_owner`**  
	该表的新拥有者的用户名。
- **`new_tablespace`**  
	要把该表移入其中的表空间的名称。
- **`new_schema`**  
	要把该表移入其中的模式的名称。
- **`partition_name`**  
	要被作为新分区附着到这个表或者从这个表上分离的表的名称。
- **`partition_bound_spec`**  
	新分区的分区边界说明。更多细节请参考 `CREATE TABLE` 中相同的语法。

**注解**

关键词 `COLUMN` 是噪声，可以被省略。

在使用 `ADD COLUMN` 增加一列并且指定了一个非易失性 `DEFAULT` 时，默认值会在该语句执行时计算并且结果会被保存在表的元数据中。这个值将被用于所有现有行的该列。如果没有指定 `DEFAULT` ，则使用 `NULL` 。在两种情况下都不需要重写表。

增加一个带有非易失性 `DEFAULT` 子句的列或者更改一个现有列的类型将要求重写整个表及其索引。在更改一个现有列的类型时有一种例外：如果 `USING` 子句不更改列的内容并且旧类型在二进制上与新类型可强制转换或者是新类型上的一个未约束域，则不需要重写表。但是受影响列上的任何索引仍必须被重建。对于一个大型表，表和/或索引重建可能会消耗相当多的时间，并且会临时要求差不多两倍的磁盘空间。

增加一个 `CHECK` 或者 `NOT NULL` 约束要求扫描表以验证现有行符合该约束，但是不要求一次表重写。

类似地，在挂接一个新分区时，它需要被扫描以验证现有行满足该分区约束。

提供在一个 `ALTER TABLE` 中指定多个更改的选项的主要原因就是多次表扫描或者重写可以因此被整合成一次。

扫描大型表以验证新的外键或检查约束可能需要很长时间，并且对表的其他更新将锁定，直到 `ALTER TABLE ADD CONSTRAINT` 命令被提交。 `NOT VALID` 约束选项的主要目的是减少对并发更新添加约束的影响。使用 `NOT VALID` ， `ADD CONSTRAINT` 命令不扫描表，可以立即提交。在之后， `VALIDATE CONSTRAINT` 命令会被发出以验证现有行是否满足约束。验证步骤不需要锁定并发更新，因为它知道其他事务将强制执行它们插入或更新的行的约束；只有预先存在的行需要检查。因此，验证在被更改的表上仅获得一个 `SHARE UPDATE EXCLUSIVE` 锁。（如果约束是外键，则 `ROW SHARE` 锁也需要约束的表引用。）除了改进并发性外，在已知该表包含预先存在的违规行为的情况下使用 `NOT VALID` 和 `VALIDATE CONSTRAINT` 也能有作用。一旦约束就位，就不能再插入新的违规，并且现有问题可以在空闲时纠正，直到 `VALIDATE CONSTRAINT` 最终完成。

`DROP COLUMN` 形式不会在物理上移除列，而只是简单地让它对 SQL 操作不可见。后续该表中的插入和更新操作将为该列存储一个空值。因此，删除一个列很快，但是它不会立刻减少表所占的磁盘空间，因为被删除列所占用的空间还没有被回收。随着现有列被更新，空间将被逐渐回收。

要强制立即回收被已删除列占据的空间，你可以执行一种能导致全表重写的 `ALTER TABLE` 形式。这种形式会导致重新构造每一个把被删除列替换为空值的行。

`ALTER TABLE` 的重写形式对于 MVCC 是不安全的。在一次表重写之后，如果并发事务使用的是一个在重写发生前取得的快照，该表将对这些并发事务呈现出空表的形态。

`SET DATA TYPE` 的 `USING` 选项能实际指定涉及该列旧值的任何表达式。也就是说，它可以不但可以引用要被转换的列，还可以引用其他列。这允许使用 `SET DATA TYPE` 语法完成十分普遍的转换。由于这种灵活性， `USING` 表达式不适合于列的默认值（如果有），结果可能不是一个默认值所需的常量表达式。这意味着在没有从旧类型到新类型的隐式或者赋值造型时，即便提供了一个 `USING` 子句， `SET DATA TYPE` 还是可能无法转换默认值。在这种情况下，用 `DROP DEFAULT` 删除该默认值，执行 `ALTER TYPE` 并且接着使用 `SET DEFAULT` 增加一个合适的新默认值。类似的考虑也适用于涉及该列的索引和约束。

如果一个表有任何后代表，在不对后代表做相同操作的情况下，不允许在父表中增加列、重命名列或者更改列的类型。这确保了后代总是具有和父表匹配的列。类似地，如果不对所有后代上的 `CHECK` 约束进行重命名，就不能在父表中重命名该 `CHECK` 约束，这样 `CHECK` 约束也能在父表及其后代之间保持匹配（不过，这个限制不适用于基于索引的约束）。此外，因为从父表中选择也会从其后代中选择，父表上的约束不能被标记为有效，除非它在那些后代上也被标记为有效。在所有这些情况下， `ALTER TABLE ONLY` 都将被拒绝。

只有当一个后代表的列不是从任何其他父表继承而来并且没有该列的独立定义时，一次递归的 `DROP COLUMN` 操作才会移除该列。一次非递归的 `DROP COLUMN` （即 `ALTER TABLE ONLY ... DROP COLUMN` ）不会移除任何后代列，而是会把它们标记成独立定义的列。对于一个分区表，一个非递归的 `DROP COLUMN` 命令将会失败，因为一个表的所有分区都必须有和分区根节点相同的列。

标识列的动作（ `ADD GENERATED` 、 `SET` 等、 `DROP IDENTITY` ）以及动作 `TRIGGER` 、 `CLUSTER` 、 `OWNER` 和 `TABLESPACE` 不会递归到后代表上，也就是说它们执行时总是好像指定了 `ONLY` 一样。增加约束的动作仅对没有标记为 `NO INHERIT` 的 `CHECK` 约束递归。

不允许更改一个系统目录表的任何部分。

**示例**

要向一个表增加一个类型为 `varchar` 的列：

```sql
ALTER TABLE distributors ADD COLUMN address varchar(30);
```

要从表中删除一列：

```sql
ALTER TABLE distributors DROP COLUMN address RESTRICT;
```

要在一个操作中更改两个现有列的类型：

```sql
ALTER TABLE distributors 
    ALTER COLUMN address TYPE varchar(80), 
    ALTER COLUMN name TYPE varchar(100);
```

通过一个 `USING` 子句更改一个包含 Unix 时间戳的整数列为 `timestamp with time zone` ：

```sql
ALTER TABLE foo ALTER COLUMN foo_timestamp SET DATA TYPE timestamp with time zone 
    USING timestamp with time zone 'epoch' + foo_timestamp * interval '1 second';
```

同样的，当该列具有一个不能自动造型成新数据类型的默认值表达式时：

```sql
ALTER TABLE foo
    ALTER COLUMN foo_timestamp DROP DEFAULT,
    ALTER COLUMN foo_timestamp TYPE timestamp with time zone
        USING timestamp with time zone 'epoch' + foo_timestamp * interval '1 second',
    ALTER COLUMN foo_timestamp SET DEFAULT now();
```

重命名一个现有的列：

```sql
ALTER TABLE distributors RENAME COLUMN address TO city;
```

重命名一个现有的表：

```sql
ALTER TABLE distributors RENAME TO suppliers;
```

重命名一个现有的约束：

```sql
ALTER TABLE distributors RENAME CONSTRAINT zipchk TO zip_check;
```

为一列增加一个非空约束：

```sql
ALTER TABLE distributors ALTER COLUMN street SET NOT NULL;
```

从一列移除一个非空约束：

```sql
ALTER TABLE distributors ALTER COLUMN street DROP NOT NULL;
```

向一个表及其所有子女增加一个检查约束：

```sql
ALTER TABLE distributors ADD CONSTRAINT zipchk CHECK (char_length(zipcode) = 5);
```

只向一个表增加一个检查约束（不为其子女增加）：

```sql
ALTER TABLE distributors ADD CONSTRAINT zipchk CHECK (char_length(zipcode) = 5) NO INHERIT;
```

（该检查约束也不会被未来的子女继承）。

从一个表及其子女移除一个检查约束：

```sql
ALTER TABLE distributors DROP CONSTRAINT zipchk;
```

只从一个表移除一个检查约束：

```sql
ALTER TABLE ONLY distributors DROP CONSTRAINT zipchk;
```

（该检查约束仍为子女表保留在某个地方）。

为一个表增加一个外键约束：

```sql
ALTER TABLE distributors ADD CONSTRAINT distfk FOREIGN KEY (address) REFERENCES addresses (address);
```

为一个表增加一个外键约束，并且尽量不要影响其他工作：

```sql
ALTER TABLE distributors ADD CONSTRAINT distfk FOREIGN KEY (address) REFERENCES addresses (address) NOT VALID;
ALTER TABLE distributors VALIDATE CONSTRAINT distfk;
```

为一个表增加一个（多列）唯一约束：

```sql
ALTER TABLE distributors ADD CONSTRAINT dist_id_zipcode_key UNIQUE (dist_id, zipcode);
```

为一个表增加一个自动命名的主键约束，注意一个表只能拥有一个主键：

```sql
ALTER TABLE distributors ADD PRIMARY KEY (dist_id);
```

把一个表移动到一个不同的表空间：

```sql
ALTER TABLE distributors SET TABLESPACE fasttablespace;
```

把一个表移动到一个不同的模式：

```sql
ALTER TABLE myschema.distributors SET SCHEMA yourschema;
```

重建一个主键约束，并且在重建索引期间不阻塞更新：

```sql
CREATE UNIQUE INDEX CONCURRENTLY dist_id_temp_idx ON distributors (dist_id);
ALTER TABLE distributors 
    DROP CONSTRAINT distributors_pkey,
    ADD CONSTRAINT distributors_pkey PRIMARY KEY USING INDEX dist_id_temp_idx;
```

要把一个分区挂接到一个范围分区表上：

```sql
ALTER TABLE measurement ATTACH PARTITION measurement_y2016m07 
    FOR VALUES FROM ('2016-07-01') TO ('2016-08-01');
```

要把一个分区挂接到一个列表分区表上：

```sql
ALTER TABLE cities ATTACH PARTITION cities_ab FOR VALUES IN ('a', 'b');
```

要把一个分区挂接到一个哈希分区表上：

```sql
ALTER TABLE orders
    ATTACH PARTITION orders_p4 FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

要把一个默认分区挂接到一个分区表上：

```sql
ALTER TABLE cities ATTACH PARTITION cities_partdef DEFAULT;
```

从一个分区表分离一个分区：

```sql
ALTER TABLE measurement DETACH PARTITION measurement_y2015m12;
```

**兼容性**

形式 `ADD` （没有 `USING INDEX` ）、 `DROP [COLUMN]` 、 `DROP IDENTITY` 、 `RESTART` 、 `SET DEFAULT` 、 `SET DATA TYPE` （没有 `USING` ）、 `SET GENERATED` 以及 `SET sequence_option` 服从 SQL 标准。其他形式都是瀚高数据库对 SQL 标准的扩展。此外，在单个 `ALTER TABLE` 命令中指定多个操作的能力是一种扩展。

`ALTER TABLE DROP COLUMN` 可以被用来删除一个表的唯一的列，从而留下一个零列的表。这是一种 SQL 的扩展，SQL 中不允许零列的表。

**另见**

```sql
CREATE TABLE
```

## ALTER TABLESPACE

— 更改一个表空间的定义

**大纲**

```sql
ALTER TABLESPACE name RENAME TO new_name

ALTER TABLESPACE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER TABLESPACE name SET ( tablespace_option = value [, ... ] )

ALTER TABLESPACE name RESET ( tablespace_option [, ... ] )
```

**描述**

`ALTER TABLESPACE` 可以被用于更改一个表空间的定义。

要更改一个表空间的定义，你必须拥有它。要修改拥有者，你还必须是新拥有角色的一个直接或间接成员（注意超级用户自动拥有这些特权）。

**参数**

- **`name`**  
	一个现有表空间的名称。
- **`new_name`**  
	该表空间的新名称。新名称不能以 `pg_` 开始，因为这类名称被保留用于系统表空间。
- **`new_owner`**  
	该表空间的新拥有者。
- **`tablespace_option`**  
	要设置或者重置的一个表空间参数。当前，唯一可用的参数是 `seq_page_cost` 、 `random_page_cost` 和 `effective_io_concurrency` 。为一个特定表空间设定这两个参数值将覆盖规划器对从该表空间中的表读取页面代价的估计值，这些估计值由具有相同名称配置参数建立（见 `seq_page_cost` 、 `random_page_cost` 、 `effective_io_concurrency` ）。如果一个表空间位于一个比其余 I/O 子系统更快或者更慢的磁盘上时，这些参数就能派上用场。

**示例**

将表空间 `index_space` 重命名为 `fast_raid` ：

```sql
ALTER TABLESPACE index_space RENAME TO fast_raid;
```

更改表空间 `index_space` 的拥有者：

```sql
ALTER TABLESPACE index_space OWNER TO mary;
```

**兼容性**

在 SQL 标准中没有 `ALTER TABLESPACE` 语句。

**另见**

```sql
CREATE TABLESPACE\`, \`DROP TABLESPACE
```

## ALTER TEXT SEARCH CONFIGURATION

— 更改一个文本搜索配置的定义

**大纲**

```sql
ALTER TEXT SEARCH CONFIGURATION name
    ADD MAPPING FOR token_type [, ... ] WITH dictionary_name [, ... ]

ALTER TEXT SEARCH CONFIGURATION name
    ALTER MAPPING FOR token_type [, ... ] WITH dictionary_name [, ... ]

ALTER TEXT SEARCH CONFIGURATION name
    ALTER MAPPING REPLACE old_dictionary WITH new_dictionary

ALTER TEXT SEARCH CONFIGURATION name
    ALTER MAPPING FOR token_type [, ... ] REPLACE old_dictionary
    WITH new_dictionary

ALTER TEXT SEARCH CONFIGURATION name
    DROP MAPPING [ IF EXISTS ] FOR token_type [, ... ]

ALTER TEXT SEARCH CONFIGURATION name RENAME TO new_name

ALTER TEXT SEARCH CONFIGURATION name OWNER TO { new_owner | CURRENT_USER |
    SESSION_USER }

ALTER TEXT SEARCH CONFIGURATION name SET SCHEMA new_schema
```

**描述**

`ALTER TEXT SEARCH CONFIGURATION` 更改一个文本搜索配置的定义。你可以修改其从记号类型到词典的映射或者更改该配置的名称或者拥有者。

要使用 `ALTER TEXT SEARCH CONFIGURATION` ，你必须是该配置的拥有者。

**参数**

- **`name`**  
	一个现有文本搜索配置的名称（可以是模式限定的）。
- **`token_type`**  
	由该配置的解析器发出的记号类型的名称。
- **`dictionary_name`**  
	在其中查阅指定记号类型的文本搜索字典的名称。如果列出了多个字典，会按照指定的顺序查阅它们。
- **`old_dictionary`**  
	在映射中要替换的文本搜索字典的名称。
- **`new_dictionary`**  
	被用来替代 `old_dictionary` 的文本搜索字典的名称。
- **`new_name`**  
	该文本搜索配置的新名称。
- **`new_owner`**  
	该文本搜索配置的新拥有者。
- **`new_schema`**  
	该文本搜索配置的新模式。

**ADD MAPPING FOR** 形式会安装一些词典（用列表列出）用于在其中查阅指定的记号类型。

如果对任一记号类型已经有一个映射，则会发生错误。 **ALTER MAPPING FOR** 形式做同样的事情，但是首先会移除这些记号类型的任何现有映射。 **ALTER MAPPING REPLACE** 形式用 `new_dictionary` 来替换任何位置上的 `old_dictionary` 。当出现 `FOR` 时，只会为指定的记号类型做这样的事情。如果不出现 `FOR` ，则会为该配置中所有的映射都这样做。 **DROP MAPPING** 形式会移除指定记号类型的所有字典，导致该文本搜索配置忽略这些类型。除非出现 `IF EXISTS` ，在那些记号类型没有任何映射时会发生错误。

**示例**

下面的例子把 `my_config` 中任何位置上的 `english` 字典替换为 `swedish` 字典。

```sql
ALTER TEXT SEARCH CONFIGURATION my_config
    ALTER MAPPING REPLACE english WITH swedish;
```

**兼容性**

在 SQL 标准中没有 `ALTER TEXT SEARCH CONFIGURATION` 语句。

**另见**

```
CREATE TEXT SEARCH CONFIGURATION\`, \`DROP TEXT SEARCH CONFIGURATION
```

## ALTER TEXT SEARCH DICTIONARY

— 更改一个文本搜索字典的定义

**大纲**

```sql
ALTER TEXT SEARCH DICTIONARY name (
    option [ = value ] [, ... ]
)

ALTER TEXT SEARCH DICTIONARY name RENAME TO new_name

ALTER TEXT SEARCH DICTIONARY name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER TEXT SEARCH DICTIONARY name SET SCHEMA new_schema
```

**描述**

`ALTER TEXT SEARCH DICTIONARY` 更改一个文本搜索字典的定义。你可以更改该字典的与模板相关的选项，或者更改该字典的名称或者拥有者。

要使用 `ALTER TEXT SEARCH DICTIONARY` ，你必须是超级用户。

**参数**

- **`name`**  
	一个现有的文本搜索字典的名称（可以是模式限定的）。
- **`option`**  
	要为这个字典设置的与模板相关的选项的名称。
- **`value`**  
	用于一个模板相关选项的新值。如果等号和值被忽略，则会从该字典中移除该选项之前的设置而允许使用默认值。
- **`new_name`**  
	该文本搜索字典的新名称。
- **`new_owner`**  
	该文本搜索字典的新拥有者。
- **`new_schema`**  
	该文本搜索字典的新模式。

模板相关的选项可以以任何顺序出现。

**示例**

下面的命令更改一个基于 Snowball 的字典的停用词列表。其他参数保持不变。

```sql
ALTER TEXT SEARCH DICTIONARY my_dict ( StopWords = newrussian );
```

下面的命令更改语言选项为 `dutch` ，并且完全移除停用词选项。

```sql
ALTER TEXT SEARCH DICTIONARY my_dict ( language = dutch, StopWords );
```

下面的命令”更新”该字典的定义，但是实际没有做任何更改。

```sql
ALTER TEXT SEARCH DICTIONARY my_dict ( dummy );
```

（之所以能这样做是因为选项移除代码在选项不存在时也不会抱怨）。这种技巧在为该字典更改配置文件时有用： `ALTER` 将强制现有的数据库会话重读配置文件，否则如果会话之前已经读取过就不会再次读取。

**兼容性**

在 SQL 标准中没有 `ALTER TEXT SEARCH DICTIONARY` 语句。

**另见**

```sql
CREATE TEXT SEARCH DICTIONARY\`, \`DROP TEXT SEARCH DICTIONARY
```

## ALTER TEXT SEARCH PARSER

— 更改一个文本搜索解析器的定义

**大纲**

```sql
ALTER TEXT SEARCH PARSER name RENAME TO new_name

ALTER TEXT SEARCH PARSER name SET SCHEMA new_schema
```

**描述**

`ALTER TEXT SEARCH PARSER` 更改一个文本搜索解析器的定义。当前，唯一支持的功能是更改该解析器的名称。

要使用 `ALTER TEXT SEARCH PARSER` ，你必须是超级用户。

**参数**

- **`name`**  
	一个现有文本搜索解析器的名称（可以是模式限定的）。
- **`new_name`**  
	该文本搜索解析器的新名称。
- **`new_schema`**  
	该文本搜索解析器的新模式。

**兼容性**

在 SQL 标准中没有 `ALTER TEXT SEARCH PARSER` 语句。

**另见**

```sql
CREATE TEXT SEARCH PARSER\`, \`DROP TEXT SEARCH PARSER
```

## ALTER TEXT SEARCH TEMPLATE

— 更改一个文本搜索模板的定义

**大纲**

```sql
ALTER TEXT SEARCH TEMPLATE name RENAME TO new_name

ALTER TEXT SEARCH TEMPLATE name SET SCHEMA new_schema
```

**描述**

`ALTER TEXT SEARCH TEMPLATE` 更改一个文本搜索模板的定义。当前唯一支持的功能是更改该模板的名称。

要使用 `ALTER TEXT SEARCH TEMPLATE` ，你必须是超级用户。

**参数**

- **`name`**  
	一个现有文本搜索模板的名称（可以是模式限定的）。
- **`new_name`**  
	该文本搜索模板的新名称。
- **`new_schema`**  
	该文本搜索模板的新模式。

**兼容性**

在 SQL 标准中没有 `ALTER TEXT SEARCH TEMPLATE` 语句。

**另见**

```sql
CREATE TEXT SEARCH TEMPLATE\`, \`DROP TEXT SEARCH TEMPLATE
```

## ALTER TRIGGER

— 更改一个触发器的定义

**大纲**

```sql
ALTER TRIGGER name ON table_name RENAME TO new_name

ALTER TRIGGER name ON table_name DEPENDS ON EXTENSION extension_name
```

**描述**

`ALTER TRIGGER` 更改一个现有触发器的属性。 `RENAME` 子句更改给定触发器的名称而不更改其定义。 `DEPENDS ON EXTENSION` 子句把该触发器标记为依赖于一个扩展，这样如果扩展被删除，该触发器也会被自动删除。

要更改一个触发器的属性，你必须拥有该触发器所作用的表。

**参数**

- **`name`**  
	要修改的一个现有触发器的名称。
- **`table_name`**  
	这个触发器所作用的表的名称。
- **`new_name`**  
	该触发器的新名称。
- **`extension_name`**  
	该触发器所依赖的扩展的名称。

**注解**

临时启用或者禁用一个触发器的功能由 `ALTER TABLE` 而不是 `ALTER TRIGGER` 提供，因为 `ALTER TRIGGER` 无法表示一次性启用或者禁用一个表上所有触发器的选项。

**示例**

要重命名一个现有的触发器：

```sql
ALTER TRIGGER emp_stamp ON emp RENAME TO emp_track_chgs;
```

要把一个触发器标记为依赖于一个扩展：

```sql
ALTER TRIGGER emp_stamp ON emp DEPENDS ON EXTENSION emplib;
```

**兼容性**

`ALTER TRIGGER` 是一种瀚高数据库的 SQL 标准扩展。

**另见**

```sql
ALTER TABLE
```

## ALTER TYPE

— 更改一个类型的定义

**大纲**

```sql
ALTER TYPE name action [, ... ]

ALTER TYPE name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER TYPE name RENAME ATTRIBUTE attribute_name TO new_attribute_name [ CASCADE | RESTRICT ]

ALTER TYPE name RENAME TO new_name

ALTER TYPE name SET SCHEMA new_schema

ALTER TYPE name ADD VALUE [ IF NOT EXISTS ] new_enum_value [ { BEFORE | AFTER } neighbor_enum_value ]

ALTER TYPE name RENAME VALUE existing_enum_value TO new_enum_value
```

这里 **action** 是以下之一：

```sql
ADD ATTRIBUTE attribute_name data_type [ COLLATE collation ] [ CASCADE | RESTRICT ]

DROP ATTRIBUTE [ IF EXISTS ] attribute_name [ CASCADE | RESTRICT ]

ALTER ATTRIBUTE attribute_name [ SET DATA ] TYPE data_type [ COLLATE collation ] [ CASCADE | RESTRICT ]
```

**描述**

`ALTER TYPE` 更改一种现有类型的定义。它有几种形式：

**ADD ATTRIBUTE**  
这种形式为一种组合类型增加一个新属性，使用的语法和 `CREATE TYPE` 相同。

**DROP ATTRIBUTE \[ IF EXISTS \]**  
这种形式从一种组合类型删除一个属性。如果指定了 `IF EXISTS` 并且该属性不存在，则不会抛出错误。这种情况下会发出一个提示。

**SET DATA TYPE**  
这种形式更改一种组合类型的一个属性类型。

**OWNER**  
这种形式更改该类型的拥有者。

**RENAME**  
这种形式更改该类型的名称或者一种组合类型的一个属性的名称。

**SET SCHEMA**  
这种形式把该类型移动到另一个模式中。

**ADD VALUE \[ IF NOT EXISTS \] \[ BEFORE | AFTER \]**  
这种形式为一种枚举类型增加一个新值。可以用 `BEFORE` 或者 `AFTER` 一个现有值来指定新值在枚举顺序中的位置。否则，新项会被增加在值列表的最后。

如果指定了 `IF NOT EXISTS` ，该类型已经包含新值时不会发生错误：会发出一个提示但是不采取其他行动。否则，如果新值已经存在会发生错误。

**RENAME VALUE**  
该形式重命名枚举类型的值。该值在枚举排序中的位置不受影响。如果指定的值不存在或新名称已存在，则会发生错误。

`ADD ATTRIBUTE` 、 `DROP ATTRIBUTE` 和 `ALTER ATTRIBUTE` 动作可以被整合到一个多个修改组成的列表中，以便被平行应用。例如，可以在一个命令中增加多个属性并且/或者修改多个属性的类型。

要使用 `ALTER TYPE` ，你必须拥有该类型。要更改一个类型的模式，你还必须拥有新模式上的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该类型的模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建该类型做不到的事情。不过，一个超级用户怎么都能更改任何类型的所有权。）。

要增加一个属性或者修改一个属性类型，你还必须具有该数据类型上的 `USAGE` 特权。

**参数**

- **`name`**  
	要修改的一个现有类型的名称（可能被模式限定）。
- **`new_name`**  
	该类型的新名称。
- **`new_owner`**  
	该类型新拥有者的用户名。
- **`new_schema`**  
	该类型的新模式。
- **`attribute_name`**  
	要增加、修改或者删除的属性名称。
- **`new_attribute_name`**  
	要被重命名的属性的新名称。
- **`data_type`**  
	要增加的属性的数据类型，或者是要修改的属性的新类型。
- **`new_enum_value`**  
	要被增加到一个枚举类型的值列表的新值，或将赋予现有值的新名称。和所有枚举文本一样，它需要被引号引用。
- **`neighbor_enum_value`**  
	一个现有枚举值，新值应该被增加在紧接着该枚举值之前或者之后的位置上。和所有枚举文本一样，它需要被引号引用。
- **`existing_enum_value`**  
	现有的应该重命名的枚举值。和所有的枚举文本一样，它需要被引号引用。
- **`CASCADE`**  
	自动将操作传播到被更改类型的类型表及其后代。
- **`RESTRICT`**  
	如果被更改的类型是类型表的类型，则拒绝该操作。这是默认设置。

**注解**

如果 `ALTER TYPE ... ADD VALUE` （增加一个新值到枚举类型的形式）不能在一个事务块中执行，新值不能被使用直到事务被提交之后。

涉及到一个新增加枚举值的比较有时会被只涉及原始枚举值的比较更慢。这通常只会在利用 `BEFORE` 或者 `AFTER` 来把新值的排序位置设置为非列表结尾的地方时发生。不过，有时候即使把新值增加到最后时也会发生这种情况（如果创建了该枚举类型之后出现过 OID 计数器 “回卷”，就会发生这种情况）。这种减速通常不明显，但是如果它确实带来了麻烦，通过删除并且重建该枚举类型或者转储并且重载整个数据库可以重新得到最优性能。

**示例**

要重命名一个数据类型：

```sql
ALTER TYPE electronic_mail RENAME TO email;
```

把类型 `email` 的拥有者改为 `joe` ：

```sql
ALTER TYPE email OWNER TO joe;
```

把类型 `email` 的模式改为 `customers` ：

```sql
ALTER TYPE email SET SCHEMA customers;
```

增加一个新属性到一个类型：

```sql
ALTER TYPE compfoo ADD ATTRIBUTE f3 int;
```

在一个特定的排序位置上为一个枚举类型增加一个新值：

```sql
ALTER TYPE colors ADD VALUE 'orange' AFTER 'red';
```

重命名一个枚举值：

```sql
ALTER TYPE colors RENAME VALUE 'purple' TO 'mauve';
```

**兼容性**

增加和删除属性的变体是 SQL 标准的一部分，而其他变体是瀚高数据库扩展。

**另见**

```sql
CREATE TYPE\`, \`DROP TYPE
```

## ALTER USER

— 更改一个数据库角色

**大纲**

```sql
ALTER USER role_specification [ WITH ] option [ ... ]

ALTER USER name RENAME TO new_name

ALTER USER { role_specification | ALL } [ IN DATABASE database_name ]
    SET configuration_parameter { TO | = } { value | DEFAULT }

ALTER USER { role_specification | ALL } [ IN DATABASE database_name ]
    SET configuration_parameter FROM CURRENT

ALTER USER { role_specification | ALL } [ IN DATABASE database_name ]
    RESET configuration_parameter

ALTER USER { role_specification | ALL } [ IN DATABASE database_name ] RESET ALL
```

其中 **option** 可以是：

```sql
SUPERUSER | NOSUPERUSER
| CREATEDB | NOCREATEDB
| CREATEROLE | NOCREATEROLE
| INHERIT | NOINHERIT
| LOGIN | NOLOGIN
| REPLICATION | NOREPLICATION
| BYPASSRLS | NOBYPASSRLS
| CONNECTION LIMIT connlimit
| [ ENCRYPTED ] PASSWORD 'password' | PASSWORD NULL
| VALID UNTIL 'timestamp'
```

其中 **role\_specification** 可以是：

```sql
role_name
| CURRENT_USER
| SESSION_USER
```

**描述**

`ALTER USER` 现在是 `ALTER ROLE` 的一种别名。

**兼容性**

`ALTER USER` 语句是一种瀚高数据库扩展。SQL 标准把用户的定义留给实现来处理。

**另见**

```sql
ALTER ROLE
```

## ALTER USER MAPPING

— 更改一个用户映射的定义

**大纲**

```sql
ALTER USER MAPPING FOR { user_name | USER | CURRENT_USER | SESSION_USER | PUBLIC }
    SERVER server_name
    OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )
```

**描述**

`ALTER USER MAPPING` 更改一个用户映射的定义。

一个外部服务器的拥有者可以为任何用户修改用于该服务器的用户映射。还有，如果一个用户被授予了外部服务器上的 `USAGE` 特权，它就能为它们自己的用户名修改一个用户映射。

**参数**

- **`user_name`**  
	该映射的用户名。 `CURRENT_USER` 和 `USER` 匹配当前用户的名称。 `PUBLIC` 被用来匹配系统中所有当前以及未来的用户名。
- **`server_name`**  
	该用户映射的服务器名。
- **`OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )`**  
	为该用户映射更改选项。新选项会覆盖任何之前指定的选项。 `ADD` 、 `SET` 和 `DROP` 指定要被执行的动作。如果没有显式地指定操作，将假定为 `ADD` 。选项名称必须为唯一，该服务器的外部数据包装器也会验证选项。

**示例**

为服务器 `foo` 的用户映射 `bob` 更改口令：

```sql
ALTER USER MAPPING FOR bob SERVER foo OPTIONS (SET password 'public');
```

**兼容性**

`ALTER USER MAPPING` 符合 ISO/IEC 9075-9 (SQL/MED)。有一点细微的语法问题：该标准会忽略 `FOR` 关键字。由于 `CREATE USER MAPPING` 以及 `DROP USER MAPPING` 都在类似的位置上使用 `FOR` ，并且 IBM DB2（作为其他主要的 SQL/MED 实现）也在 `ALTER USER MAPPING` 中要求该关键字，因此为了一致性和互操作性，瀚高数据库在这里的实现与标准不同。

**另见**

```sql
CREATE USER MAPPING\`, \`DROP USER MAPPING
```

## ALTER VIEW

— 更改一个视图的定义

**大纲**

```sql
ALTER VIEW [ IF EXISTS ] name ALTER [ COLUMN ] column_name SET DEFAULT expression

ALTER VIEW [ IF EXISTS ] name ALTER [ COLUMN ] column_name DROP DEFAULT

ALTER VIEW [ IF EXISTS ] name OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

ALTER VIEW [ IF EXISTS ] name RENAME TO new_name

ALTER VIEW [ IF EXISTS ] name SET SCHEMA new_schema

ALTER VIEW [ IF EXISTS ] name SET ( view_option_name [= view_option_value] [, ... ] )

ALTER VIEW [ IF EXISTS ] name RESET ( view_option_name [, ... ] )
```

**描述**

`ALTER VIEW` 更改一个视图的多种辅助属性（如果想要修改视图的查询定义，应使用 `CREATE OR REPLACE VIEW` ）。

要使用 `ALTER VIEW` ，你必须拥有该视图。要更改一个视图的模式，你还必须具有新模式上的 `CREATE` 特权。要更改拥有者，你还必须是新拥有角色的一个直接或者间接成员，并且该角色必须具有该视图的模式上的 `CREATE` 特权（这些限制强制修改拥有者不能做一些通过删除和重建视图做不到的事情。不过，一个超级用户怎么都能更改任何视图的所有权。）。

**参数**

- **`name`**  
	一个现有视图的名称（可以是模式限定的）。
- **`IF EXISTS`**  
	该视图不存在时不要抛出一个错误。这种情况下会发出一个提示。
- **`SET/DROP DEFAULT`**  
	这些形式为一个列设置或者移除默认值。对于任何在该视图上的 `INSERT` 或者 `UPDATE` 命令，一个视图列的默认值会在引用该视图的任何规则或触发器之前被替换进来。因此，该视图的默认值将会优先于来自底层关系的任何默认值。
- **`new_owner`**  
	该视图的新拥有者的用户名。
- **`new_name`**  
	该视图的新名称。
- **`new_schema`**  
	该视图的新模式。
- **`SET ( view_option_name [= view_option_value] [, ... ] )`**
- **`RESET ( view_option_name [, ... ] )`**  
	设置或者重置一个视图选项。当前支持的选项有：
	- **`check_option`** (string)  
		更改该视图的检查选项。值必须是 `local` 或者 `cascaded` 。
		- **`security_barrier`** (boolean)  
		更改该视图的安全屏障属性。值必须是一个布尔值，如 `true` 或者 `false` 。

**注解**

由于历史原因， `ALTER TABLE` 也可以用于视图，但是只允许等效于以上形式的 `ALTER TABLE` 变体用于视图。

**示例**

把视图 `foo` 重命名为 `bar` ：

```sql
ALTER VIEW foo RENAME TO bar;
```

要为一个可更新视图附加一个默认列值：

```sql
CREATE TABLE base_table (id int, ts timestamptz);
CREATE VIEW a_view AS SELECT * FROM base_table;
ALTER VIEW a_view ALTER COLUMN ts SET DEFAULT now();
INSERT INTO base_table(id) VALUES(1);  -- ts will receive a NULL
INSERT INTO a_view(id) VALUES(2);      -- ts will receive the current time
```

**兼容性**

`ALTER VIEW` 是一种瀚高数据库的 SQL 标准扩展。

**另见**

```sql
CREATE VIEW\`, \`DROP VIEW
```

## ANALYZE

— 收集有关一个数据库的统计信息

**大纲**

```sql
ANALYZE [ ( option [, ...] ) ] [ table_and_columns [, ...] ]

ANALYZE [ VERBOSE ] [ table_and_columns [, ...] ]
```

其中 **option** 可以是：

```sql
VERBOSE [ boolean ]
SKIP_LOCKED [ boolean
```

**table\_and\_columns** 是：

```sql
table_name [ ( column_name [, ...] ) ]
```

**描述**

`ANALYZE` 收集一个数据库中的表的内容的统计信息，并且将结果存储在 `pg_statistic` 系统目录中。接下来，查询规划器会使用这些统计信息来帮助确定查询最有效的执行计划。

如果没有 `table_and_columns` 列表，则 `ANALYZE` 处理当前用户有权分析的当前数据库中的每个表和物化视图。使用列表， `ANALYZE` 仅处理那些表。还可以给出表的列名列表，在这种情况下，仅收集这些列的统计信息。

当选项列表用括号括起来时，选项可以按任何顺序来写。带括号的语法是在瀚高数据库之前的版本中添加的；不带括号的语法已弃用。

**参数**

- **`VERBOSE`**  
	允许显示进度消息。
- **`SKIP_LOCKED`**  
	规定 `ANALYZE` 在开始处理一个关系时不应等待任何冲突的锁被释放：如果关系不能无需等待立即锁定，则跳过该关系。请注意即使采用此选项， `ANALYZE` 在打开关系的索引或从分区、表继承子级和某些类型的外表获取样本行时仍可能阻塞。此外，当 `ANALYZE` 通常处理指定分区表的所有分区时，如果分区表上有一个冲突的锁，这个选项将导致 `ANALYZE` 跳过所有分区表。
- **`boolean`**  
	规定所选的选项打开或关闭。您可以写 `TRUE` 、 `ON` 或 `1` 以启用该选项，或者是 `FALSE` 、 `OFF` 或 `0` 来禁用它。 `boolean` 值可以被省略，在假定为 `TRUE` 的情况下。
- **`table_name`**  
	要分析的一个指定表的名称（可以是模式限定的）。如果省略，则分析当前数据库中的所有常规表、分区表和物化视图（但不包含外部表）。如果指定的表是分区表，则整个分区表的继承统计信息和各个分区的统计信息都将更新。
- **`column_name`**  
	要分析的一个指定列的名称。默认是所有列。

**输出**

当指定了 `VERBOSE` 时， `ANALYZE` 会发出进度消息来指示当前正在处理哪个表。还会打印有关那些表的多种统计信息。

**注解**

要分析表，通常必须是该表的所有者或超级用户。不过，数据库所有者可以分析数据库中的所有表，共享目录除外。（对共享目录的限制意味着真正的数据库范围的 `ANALYZE` 只能由超级用户执行。） `ANALYZE` 将跳过调用用户没有分析权限的任何表。

只有被显式选中时才会分析外部表。并非所有外部数据包装器都支持 `ANALYZE` 。如果表的包装器不支持 `ANALYZE` ，该命令会打印一个警告并且什么也不做。

在默认的瀚高数据库配置中，自动清理守护进程会在表第一次载入数据或者用常规操作改变时负责表的自动分析。当启用自动清理时，定期运行 `ANALYZE` 是个好主意，或者可以在表内容做了大的修改后运行 `ANALYZE` 。准确的统计信息将帮助规划器选择最合适的查询计划，从而提升查询处理的速度。主读数据库的一般策略是在一天中使用量最低时运行一次 `VACUUM` 和 `ANALYZE` （如果有大量的更新动作则是不够的）。

`ANALYZE` 只要求目标表上的一个读锁，因此它可以和表上的其他动作并行。

`ANALYZE` 收集的统计信息通畅包括每列中最常见值的列表以及展示每列中近似数据分布的一个直方图。如果 `ANALYZE` 认为这些东西无趣（例如在一个唯一键列中，没有共同值）或者该列的数据类型不支持合适的操作符，以上工作都会被省略。

对于大型的表， `ANALYZE` 会对表内容做随机采样而不是检查每一行。这允许在很少的时间内完成对大型表的分析。不过要注意，这些统计信息只是近似值，并且即使实际表内容没有改变，每次运行 `ANALYZE` 时统计信息都会有微小地改变。这可能会导致 `EXPLAIN` 显示的规划器估算代价有小的改变。在很少的情况下，这会非决定性地导致规划器的查询计划选择在 `ANALYZE` 运行后改变。为了避免这种情况，可以按照下文所述提高 `ANALYZE` 所收集的统计信息量。

通过调整 `default_statistics_target` 配置变量可以控制分析量，对每个列可以用 `ALTER TABLE ... ALTER COLUMN ... SET STATISTICS` 设置每列的统计信息目标（见 `ALTER TABLE` ）。目标值会设置最常用值列表中的最大项数以及直方图中的最大容器数。默认目标值是 100，可以把它调大或者调小在规划器估计值精度和 `ANALYZE` 花费的时间以及 `pg_statistic` 所占空间之间做出平衡。特别地，将统计信息目标设置为零会禁用该列的统计信息收集。在查询的 `WHERE` 、 `GROUP BY` 或者 `ORDER BY` 子句中从不出现的列上这样做会有所帮助，因为规划器用不上这些列上的统计信息。

被分析的列中最大的统计信息目标决定了为准备统计信息要采样的表行数。增加该目标会导致做 `ANALYZE` 所需的时间和空间成比例增加。

`ANALYZE` 所估算的值之一是出现在每个列中的可区分值。因为只会检查行的一个子集，即便使用最大的统计信息目标，这种估计有时也可能很不精确。如果这种不精确导致不好的查询计划，可以手工确定一个更精确的值并且用 `ALTER TABLE ... ALTER COLUMN ... SET (n_distinct = ...)` 设置该值（见 `ALTER TABLE` ）。

如果被分析的表有一个或者更多子女， `ANALYZE` 将会收集两次统计信息：一次只对父表的行收集，第二次则在父表及其所有子女表的行上收集。在规划需要遍历整个继承树的查询时需要第二个统计信息集。不过，在决定是否触发表上的自动分析时，自动清理后台进程将只考虑父表本身上的插入和更新。如果该表很少被插入或者更新，只有手工运行 `ANALYZE` 时才会把继承统计信息更新到最新。

如果任何子表是外部表并且其外部数据包装器不支持 `ANALYZE` ，在收集继承统计信息时会忽略那些子表。

如果被分析的表不完全为空， `ANALYZE` 将不会为该表记录新统计信息。任何现有统计信息将会被保留。

**兼容性**

SQL 标准中没有 `ANALYZE` 语句。

**另见**

```sql
VACUUM, vacuumdb
```

## BEGIN

— 开始一个事务块

**大纲**

```sql
BEGIN [ WORK | TRANSACTION ] [ transaction_mode [, ...] ]
```

其中 **transaction\_mode** 是以下之一：

```sql
ISOLATION LEVEL { SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED }
READ WRITE | READ ONLY
[ NOT ] DEFERRABLE
```

**描述**

`BEGIN` 开始一个事务块，也就是说所有 `BEGIN` 命令之后的所有语句将被在一个事务中执行，直到给出一个显式的 `COMMIT` 或者 `ROLLBACK` 。默认情况下（没有 `BEGIN` ），瀚高数据库在”自动提交”模式中执行事务，也就是说每个语句都在自己的事务中执行并且在语句结束时隐式地执行一次提交（如果执行成功，否则会完成一次回滚）。

在一个事务块内的语句会执行得更快，因为事务的开始/提交也要求可观的 CPU 和磁盘活动。在进行多个相关更改时，在一个事务内执行多个语句也有助于保证一致性：在所有相关更新还没有完成之前，其他会话将不能看到中间状态。

如果指定了隔离级别、读/写模式或者延迟模式，新事务也会有那些特性，就像执行了 `SET TRANSACTION` 一样。

**参数**

- **`WORK`**
- **`TRANSACTION`**  
	可选的关键词。它们没有效果。

这个语句其他参数的含义请参考 `SET TRANSACTION` 。

**注解**

`START TRANSACTION` 具有和 `BEGIN` 相同的功能。

使用 `COMMIT` 或者 `ROLLBACK` 来终止一个事务块。

在已经在一个事务块中时发出 `BEGIN` 将惹出一个警告消息。事务状态不会被影响。要在一个事务块中嵌套事务，可以使用保存点（见 `SAVEPOINT` ）。

由于向后兼容的原因，连续的 `transaction_modes` 之间的逗号可以被省略。

**示例**

开始一个事务块：

```sql
BEGIN;
```

**兼容性**

`BEGIN` 是一种瀚高数据库语言扩展。它等效于 SQL 标准的命令 `START TRANSACTION` ，它的参考页包含额外的兼容性信息。

`DEFERRABLE` `transaction_mode` 是一种瀚高数据库语言扩展。

附带地， `BEGIN` 关键词被用于嵌入式 SQL 中的一种不同目的。在移植数据库应用时，我们建议小心对待事务语义。

**另见**

```sql
COMMIT, ROLLBACK, START TRANSACTION, SAVEPOINT
```

## CALL

— 调用一个过程

**大纲**

```sql
CALL name ( [ argument ] [, ...] )
```

**简介**

`CALL` 执行一个过程。

如果过程有任何输出参数，则会返回一个结果行，返回这些参数的值。

**参数**

- **`name`**  
	过程的名称（可以被方案限定）。
- **`argument`**  
	过程调用的一个输入参数。

**注解**

用户必须有过程上的 `EXECUTE` 特权才能调用它。

要调用一个函数（不是过程），应使用 `SELECT` 。

如果在事务块中执行 `CALL` ，那么被调用的过程不能执行事务控制语句。只有当 `CALL` 在其自身的事务中执行时，才允许过程执行事务控制语句。

PL/pgSQL 以不同的方式处理 `CALL` 中的输出参数。

**示例**

```sql
CALL do_db_maintenance();
```

**兼容性**

`CALL` 符合 SQL 标准。

**另见**

```sql
CREATE PROCEDURE
```

## CHECKPOINT

— 强制一个事务日志检查点

**大纲**

```sql
CHECKPOINT
```

**描述**

一个检查点是事务日志序列中的一个点，在该点上所有数据文件都已经被更新为反映日志中的信息。所有数据文件将被刷写到磁盘。

`CHECKPOINT` 命令在发出时强制一个立即的检查点，而不用等待由系统规划的常规检查点。 `CHECKPOINT` 不是用来在普通操作中使用的命令。

如果在恢复期间执行， `CHECKPOINT` 命令将强制一个重启点而不是写一个新检查点。

只有超级用户能够调用 `CHECKPOINT` 。

**兼容性**

`CHECKPOINT` 命令是一种瀚高数据库语言扩展。

## CLOSE

— 关闭一个游标

**大纲**

```sql
CLOSE { name | ALL }
```

**描述**

`CLOSE` 释放与一个已打开游标相关的资源。在游标被关闭后，不允许在其上做后续的操作。

当不再需要使用一个游标时应该关闭它。

当一个事务被 `COMMIT` 或者 `ROLLBACK` 终止时，每一个非可保持的已打开游标会被隐式地关闭。当创建一个可保持游标的事务通过 `ROLLBACK` 中止时，该可保持游标会被隐式地关闭。

如果该创建事务成功地提交，可保持游标会保持打开，直至执行一个显式的 `CLOSE` 或者客户端连接断开。

**参数**

- **`name`**  
	要关闭的已打开游标的名称。
- **`ALL`**  
	关闭所有已打开的游标。

**注解**

瀚高数据库没有一个显式的 `OPEN` 游标语句，一个游标在被声明时就被认为是打开的。使用 `DECLARE` 语句可以声明游标。

通过查询 `pg_cursors` 系统视图可以看到所有可用的游标。

如果一个游标在一个保存点之后关闭，并且后来回滚到了这个保存点，那么 `CLOSE` 不会被回滚，也就是说回滚后游标仍然保持关闭。

**示例**

关闭游标 `liahona` ：

```sql
CLOSE liahona;
```

**兼容性**

`CLOSE` 完全服从 SQL 标准。 `CLOSE ALL` 是一种瀚高数据库扩展。

**另见**

`DECLARE`,`FETCH`,`MOVE`

## CLUSTER

— 根据一个索引聚簇一个表

**大纲**

```sql
CLUSTER [VERBOSE] table_name [ USING index_name ]

CLUSTER [VERBOSE]
```

**描述**

`CLUSTER` 指示瀚高数据库基于 `index_name` 所指定的索引来聚簇 `table_name` 所指定的表。该索引必须已经定义在 `table_name` 上。

当一个表被聚簇时，会基于索引信息对它进行物理上的排序。聚簇是一种一次性的操作：

当表后续被更新时，更改没有被聚簇。也就是说，不会尝试根据新行或者被更新行的索引顺序来存储它们（如果想这样做，可以周期性地通过发出该命令重新聚簇。还有，把表的 `fillfactor` 存储参数设置为小于 100% 有助于在更新期间保持聚簇顺序，因为如果空间足够会把被更新行保留在同一个页面中）。

当一个表被更新时，瀚高数据库会记住它是按照哪个索引聚簇的。形式

```sql
CLUSTER table_name
```

会使用前面所用的同一个索引对表重新聚簇。你也可以使用 `CLUSTER` 或者 `ALTER TABLE` 的 `SET WITHOUT CLUSTER` 形式把索引设置为可用于未来的聚簇操作，或者清除任何之前的设置。

不带任何参数的 `CLUSTER` 会重新聚簇调用用户所拥有的当前数据库中已经被聚簇过的表（如果是超级用户调用，则是所有已被聚簇过的表）。这种形式的 `CLUSTER` 不能在一个事务块内执行。

当一个表被聚簇时，会在其上要求一个 `ACCESS EXCLUSIVE` 锁。这会阻止任何其他数据库操作（包括读和写）在 `CLUSTER` 结束前在该表上操作。

**参数**

- **`table_name`**  
	一个表的名称（可能是模式限定的）。
- **`index_name`**  
	一个索引的名称。
- **`VERBOSE`**  
	在每一个表被聚簇时打印一个进度报告。

**注解**

在随机访问一个表中的行时，表中数据的实际顺序是无关紧要的。不过，如果你想要更多地访问其中一些数据，并且有一个索引把它们分组在一起，使用 `CLUSTER` 就会带来好处。

如果你从一个表中要求一个范围的被索引值或者多行都匹配的一个单一值， `CLUSTER` 就会有所帮助，因为一旦该索引标识出了第一个匹配行所在的表页，所有其他匹配行很可能就在同一个表页中，并且因此节省了磁盘访问并且提高了查询速度。

`CLUSTER` 可以使用指定索引上的一次索引扫描或者遵循排序的一次顺序扫描（如果索引是 B 树）对表重新排序。它将会基于规划器代价参数以及可用的统计信息来选择较快的方法。在使用索引扫描时，会创建该表的一份临时拷贝，其中包含按索引顺序排列的表数据。该表上每一个索引的临时拷贝也会被创建。因此，在磁盘上需要至少等于表尺寸加上索引尺寸的综合的空闲空间。

在使用顺序扫描以及排序时，也会创建一个临时排序文件，因此临时空间需求的峰值也就是表尺寸的两倍外加索引尺寸。这种方法通常比索引扫描方法更快，但是如果磁盘空间需求是不能接受的，你可以通过临时地把 `enable_sort` 设置为 `off` 来禁用这种选择。

建议在聚簇前把 `maintenance_work_mem` 设置为一个合理地比较大的值（但是不能超过你可以用于 `CLUSTER` 操作的 RAM 容量）。

因为规划器会记录有关表顺序的统计信息，建议在新近被聚簇的表上运行 `ANALYZE` 。否则，规划器可能会产生很差的查询计划。

因为 `CLUSTER` 会记住哪些索引被聚簇，我们可以第一次手动聚簇想要聚簇的表，然后设置一个定期运行的维护脚本，其中执行不带任何参数的 `CLUSTER` ，这样那些表就会被周期性地重新聚簇。

**示例**

基于索引 `employees_ind` 聚簇表 `employees` ：

```sql
CLUSTER employees USING employees_ind;
```

使用之前用过的同一个索引聚簇 `employees` 表：

```sql
CLUSTER employees;
```

对数据库中以前被聚簇过的所有表进行聚簇：

```sql
CLUSTER;
```

**兼容性**

在 SQL 标准中没有 `CLUSTER` 语句。

为了兼容旧版本瀚高数据库，

```sql
CLUSTER index_name ON table_name
```

语法也被支持。

**另见**

`clusterdb`

— 定义或者更改一个对象的注释

**大纲**

```sql
COMMENT ON
{
  ACCESS METHOD object_name |
  AGGREGATE aggregate_name ( aggregate_signature ) |
  CAST (source_type AS target_type) |
  COLLATION object_name |
  COLUMN relation_name.column_name |
  CONSTRAINT constraint_name ON table_name |
  CONSTRAINT constraint_name ON DOMAIN domain_name |
  CONVERSION object_name |
  DATABASE object_name |
  DOMAIN object_name |
  EXTENSION object_name |
  EVENT TRIGGER object_name |
  FOREIGN DATA WRAPPER object_name |
  FOREIGN TABLE object_name |
  FUNCTION function_name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ] |
  INDEX object_name |
  LARGE OBJECT large_object_oid |
  MATERIALIZED VIEW object_name |
  OPERATOR operator_name (left_type, right_type) |
  OPERATOR CLASS object_name USING index_method |
  OPERATOR FAMILY object_name USING index_method |
  POLICY policy_name ON table_name |
  [ PROCEDURAL ] LANGUAGE object_name |
  PROCEDURE procedure_name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ] |
  PUBLICATION object_name |
  ROLE object_name |
  ROUTINE routine_name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ] |
  RULE rule_name ON table_name |
  SCHEMA object_name |
  SEQUENCE object_name |
  SERVER object_name |
  STATISTICS object_name |
  SUBSCRIPTION object_name |
  TABLE object_name |
  TABLESPACE object_name |
  TEXT SEARCH CONFIGURATION object_name |
  TEXT SEARCH DICTIONARY object_name |
  TEXT SEARCH PARSER object_name |
  TEXT SEARCH TEMPLATE object_name |
  TRANSFORM FOR type_name LANGUAGE lang_name |
  TRIGGER trigger_name ON table_name |
  TYPE object_name |
  VIEW object_name
} IS 'text'
```

其中 `aggregate_signature` 是：

```
* |
[ argmode ] [ argname ] argtype [ , ... ] |
[ [ argmode ] [ argname ] argtype [ , ... ] ] ORDER BY [ argmode ] [ argname ] argtype [ , ... ]
```

**描述**

`COMMENT` 存储关于一个数据库对象的注释。

对每一个对象只保存一个注释字符串，因此为了修改一段注释，对同一个对象发出一个新的 `COMMENT` 命令。要移除一段注释，可在文本字符串的位置上写上 `NULL` 。当对象被删除时，其注释也会被自动删除。

对大部分类型的对象，只有对象的拥有者可以设置注释。角色没有拥有者，因此 `COMMENT ON ROLE` 的规则是你必须作为一个超级用户来对一个超级用户角色设置注释，或者具有 `CREATEROLE` 特权来对非超级用户角色设置注释。同样的，访问方法也没有拥有者，你必须作为一个超级用户来对一个访问方法设置注释。当然，一个超级用户可以对任何东西设置注释。

使用 `psql` 的 `\d` 命令家族可以查看注释。其他检索注释的用户接口可以构建在 `psql` 使用的内建函数之上，即 `obj_description` 、 `col_description` 以及 `shobj_description` 。

**参数**

`object_name`  
`relation_name.column_name`  
`aggregate_name`  
`constraint_name`  
`function_name`  
`operator_name`  
`policy_name`  
`procedure_name`  
`routine_name`  
`rule_name`  
`trigger_name`  
要被注释的对象的名称。表、聚集、排序方式、转换、域、外部表、函数、索引、操作符、操作符类、操作符族、存储过程、例程、序列、统计信息、文本搜索对象、类型和视图的名称可以被模式限定。在注释一列时， `relation_name` 必须引用一个表、视图、组合类型或者外部表。

`table_name`  
`domain_name`  
当在一个约束、触发器、规则或者策略上创建一段注释时，这些参数指定在其上定义该对象的表或域的名称。

`source_type`  
造型的源数据类型的名称。

`target_type`  
造型的目标数据类型的名称。

`argmode`  
一个函数，存储过程或者聚集函数的参数的模式： `IN` 、 `OUT` 、 `INOUT` 或者 `VARIADIC` 。如果被省略，默认值是 `IN` 。注意 `COMMENT` 并不真正关心 `OUT` 参数，因为决定函数的身份只需要输入参数。因此列出 `IN` 、 `INOUT` 和 `VARIADIC` 参数就足够了。

`argname`  
一个函数，存储过程或者聚集函数参数的名称。注意 `COMMENT` 并不真正关心参数名称，因为决定函数的身份只需要参数数据类型。

`argtype`  
一个函数，存储过程或者聚集函数参数的数据类型。

`large_object_oid`  
大对象的 OID。

`left_type`  
`right_type`  
操作符的参数的数据类型（可以是模式限定的）。对一个前缀后后缀操作符的缺失参数可以写 `NONE` 。

`PROCEDURAL`  
这是一个噪声词。

`type_name`  
该转换的数据类型的名称。

`lang_name`  
该转换的语言的名称。

`text`  
写成一个字符串的新注释。如果要删除注释，写成 `NULL` 。

**注解**

当前对查看注释没有安全机制：任何连接到一个数据库的用户能够看到该数据库中所有对象的注释。对于数据库、角色、表空间这类共享对象，注释被全局存储，因此连接到集簇中任何数据库的任何用户可以看到共享对象的所有注释。因此，不要在注释中放置有安全性风险的信息。

**示例**

为表 `mytable` 附加一段注释：

```sql
COMMENT ON TABLE mytable IS 'This is my table.';
```

移除它：

```sql
COMMENT ON TABLE mytable IS NULL;
```

更多的一些例子：

```sql
COMMENT ON ACCESS METHOD rtree IS 'R-Tree access method';

COMMENT ON AGGREGATE my_aggregate (double precision) IS 'Computes sample variance';

COMMENT ON CAST (text AS int4) IS 'Allow casts from text to int4';

COMMENT ON COLLATION "fr_CA" IS 'Canadian French';

COMMENT ON COLUMN my_table.my_column IS 'Employee ID number';

COMMENT ON CONVERSION my_conv IS 'Conversion to UTF8';

COMMENT ON CONSTRAINT bar_col_cons ON bar IS 'Constrains column col';

COMMENT ON CONSTRAINT dom_col_constr ON DOMAIN dom IS 'Constrains col of domain';

COMMENT ON DATABASE my_database IS 'Development Database';

COMMENT ON DOMAIN my_domain IS 'Email Address Domain';

COMMENT ON EXTENSION hstore IS 'implements the hstore data type';

COMMENT ON FOREIGN DATA WRAPPER mywrapper IS 'my foreign data wrapper';

COMMENT ON FOREIGN TABLE my_foreign_table IS 'Employee Information in other database';

COMMENT ON FUNCTION my_function (timestamp) IS 'Returns Roman Numeral';

COMMENT ON INDEX my_index IS 'Enforces uniqueness on employee ID';

COMMENT ON LANGUAGE plpython IS 'Python support for stored procedures';

COMMENT ON LARGE OBJECT 346344 IS 'Planning document';

COMMENT ON MATERIALIZED VIEW my_matview IS 'Summary of order history';

COMMENT ON OPERATOR ^ (text, text) IS 'Performs intersection of two texts';

COMMENT ON OPERATOR - (NONE, integer) IS 'Unary minus';

COMMENT ON OPERATOR CLASS int4ops USING btree IS '4 byte integer operators for btrees';

COMMENT ON OPERATOR FAMILY integer_ops USING btree IS 'all integer operators for btrees';

COMMENT ON POLICY my_policy ON mytable IS 'Filter rows by users';

COMMENT ON PROCEDURE my_proc (integer, integer) IS 'Runs a report';

COMMENT ON ROLE my_role IS 'Administration group for finance tables';

COMMENT ON RULE my_rule ON my_table IS 'Logs updates of employee records';

COMMENT ON SCHEMA my_schema IS 'Departmental data';

COMMENT ON SEQUENCE my_sequence IS 'Used to generate primary keys';

COMMENT ON SERVER myserver IS 'my foreign server';

COMMENT ON STATISTICS my_statistics IS 'Improves planner row estimations';

COMMENT ON TABLE my_schema.my_table IS 'Employee Information';

COMMENT ON TABLESPACE my_tablespace IS 'Tablespace for indexes';

COMMENT ON TEXT SEARCH CONFIGURATION my_config IS 'Special word filtering';

COMMENT ON TEXT SEARCH DICTIONARY swedish IS 'Snowball stemmer for Swedish language';

COMMENT ON TEXT SEARCH PARSER my_parser IS 'Splits text into words';

COMMENT ON TEXT SEARCH TEMPLATE snowball IS 'Snowball stemmer';

COMMENT ON TRANSFORM FOR hstore LANGUAGE plpythonu IS 'Transform between hstore and Python dict';

COMMENT ON TRIGGER my_trigger ON my_table IS 'Used for RI';

COMMENT ON TYPE complex IS 'Complex number data type';

COMMENT ON VIEW my_view IS 'View of departmental costs';
```

**兼容性**

SQL 标准中没有 `COMMENT` 命令。

## COMMIT

— 提交当前事务

**大纲**

```sql
COMMIT [ WORK | TRANSACTION ] [ AND [ NO ] CHAIN ]
```

**描述**

`COMMIT` 提交当前事务。所有由该事务所作的更改会变得对他人可见并且被保证在崩溃发生时仍能持久。

**参数**

`WORK`  
`TRANSACTION`  
可选的关键词。它们没有效果。

`AND CHAIN`  
如果指定了 `AND CHAIN` ，则立即启动与刚刚完成的事务具有相同事务特征（参见 `SET TRANSACTION` ）的新事务。否则，没有新事务被启动。

**注解**

使用 `ROLLBACK` 中止一个事务。

当不在一个事务内时发出 `COMMIT` 不会产生危害，但是它会产生一个警告消息。当 `COMMIT AND CHAIN` 不在事务内时是一个错误。

**示例**

要提交当前事务并且让所有更改持久化：

```sql
COMMIT;
```

**兼容性**

命令 `COMMIT` 符合 SQL 标准。表单 `COMMIT TRANSACTION` 为瀚高数据库扩展。

**另见**

`BEGIN`,`ROLLBACK`

## COMMIT PREPARED

— 提交一个早前为两阶段提交预备的事务

**大纲**

```sql
COMMIT PREPARED transaction_id
```

**描述**

`COMMIT PREPARED` 提交一个处于预备状态的事务。

**参数**

`transaction_id`  
要被提交的事务的事务标识符。

**注解**

要提交一个预备的事务，你必须是原先执行该事务的同一用户或者超级用户。但是不需要处于执行该事务的同一会话中。

这个命令不能在一个事务块中执行。该预备事务将被立刻提交。

`pg_prepared_xacts` 系统视图中列出了所有当前可用的预备事务。

**示例**

提交由事务标识符 `foobar` 标识的事务：

```sql
COMMIT PREPARED 'foobar';
```

**兼容性**

`COMMIT PREPARED` 是一种瀚高数据库扩展。其意图是用于外部事务管理系统，其中有些已经被标准涵盖（例如 X/Open XA），但是那些系统的 SQL 方面未被标准化。

**另见**

`PREPARE TRANSACTION`,`ROLLBACK PREPARED`

## COPY

— 在一个文件和一个表之间复制数据

**大纲**

```sql
COPY table_name [ ( column_name [, ...] ) ]
FROM { 'filename' | PROGRAM 'command' | STDIN }
[ [ WITH ] ( option [, ...] ) ]
[ WHERE condition ]

COPY { table_name [ ( column_name [, ...] ) ] | ( query ) }
TO { 'filename' | PROGRAM 'command' | STDOUT }
[ [ WITH ] ( option [, ...] ) ]
```

其中 `option` 可以是下列之一：

```sql
FORMAT format_name
FREEZE [ boolean ]
DELIMITER 'delimiter_character'
NULL 'null_string'
HEADER [ boolean ]
QUOTE 'quote_character'
ESCAPE 'escape_character'
FORCE_QUOTE { ( column_name [, ...] ) | * }
FORCE_NOT_NULL ( column_name [, ...] )
FORCE_NULL ( column_name [, ...] )
ENCODING 'encoding_name'
```

**描述**

`COPY` 在瀚高数据库表和标准文件系统文件之间移动数据。 `COPY TO` 把一个表的内容复制到一个文件，而 `COPY FROM` 则从一个文件复制数据到一个表（把数据追加到表中原有数据）。 `COPY TO` 也能复制一个 `SELECT` 查询的结果。

如果指定了一个列列表， `COPY TO` 将只把指定列的数据复制到文件。对于 `COPY FROM` ，文件中的每个字段将按顺序插入到指定列中。 `COPY FROM` 命令的列列表中没有指定的表列则会采纳其默认值。

带一个文件名的 `COPY` 指示瀚高数据库服务器直接从一个文件读取或者写入到一个文件。该文件必须是瀚高数据库用户（运行服务器的用户 ID）可访问的并且应该以服务器的视角来指定其名称。当指定了 `PROGRAM` 时，服务器执行给定的命令并且从该程序的标准输出读取或者写入到该程序的标准输入。该程序必须以服务器的视角指定，并且必须是瀚高数据库用户可执行的。在指定 `STDIN` 或者 `STDOUT` 时，数据会通过客户端和服务器之间的连接传输。

**参数**

`table_name`  
一个现有表的名称（可以是模式限定的）。

`column_name`  
可选的要被复制的列列表。如果没有指定列列表，则该表的所有列除了生成的列都会被复制。

`query`  
其结果要被复制的 `SELECT` 、 `VALUES` 、 `INSERT` 、 `UPDATE` 或者 `DELETE` 命令。注意查询周围的圆括号是必要的。

对于 `INSERT` 、 `UPDATE` 以及 `DELETE` 查询，必须提供一个 `RETURNING` 子句并且目标关系不能具有会扩展成多条语句的条件规则、 `ALSO` 规则或者 `INSTEAD` 规则。

`filename`  
输入或者输出文件的路径名。一个输入文件的名称可以是一个绝对或相对路径，但一个输出文件的名称必须是绝对路径。Windows 用户可能需要使用一个 `E''` 字符串并且双写路径名称中使用的任何反斜线。

`PROGRAM`  
一个要执行的命令。在 `COPY FROM` 中，输入将从该命令的标准输出读取，而在 `COPY TO` 中，输出会写入到该命令的标准输入。

注意该命令是由 shell 调用，因此如果你需要传递任何来自不可信来源的参数给 shell 命令，你必须小心地剥离那些可能对 shell 有特殊意义的特殊字符。出于安全原因，最好使用一个固定的命令字符串，或者至少避免传递任何用户输入到其中。

`STDIN`  
指定输入来自客户端应用。

`STDOUT`  
指定输出会去到客户端应用。

`boolean`  
指定选中的选项是应该被关闭还是打开。可以写 `TRUE` 、 `ON` 或 `1` 来启用选项，写 `FALSE` 、 `OFF` 或 `0` 禁用它。 `boolean` 值也可以被省略，那样会假定为 `TRUE` 。

`FORMAT`  
选择要读取或者写入的数据格式： `text` 、 `csv` （逗号分隔值）或者 `binary` 。默认是 `text` 。

`FREEZE`  
请求复制已经完成了行冻结的数据，就好像在运行 `VACUUM FREEZE` 命令之后复制。这是为了初始数据载入的性能而设计的。只有被载入表已经在当前子事务中被创建或截断、该事务中没有游标打开并且该事务没有持有更旧的快照时，行才会被冻结。目前无法在分区表上执行 `COPY FREEZE` 。

注意一旦成功地载入，所有其他会话将能立即看到该数据。这违背了普通的 MVCC 可见性规则，指定该选项的用户应该注意这可能会导致潜在问题。

`DELIMITER`  
指定分隔文件每行中各列的字符。文本格式中默认是一个制表符，而 `CSV` 格式中默认是一个逗号。这必须是一个单一的单字节字符。使用 `binary` 格式时不允许这个选项。

`NULL`  
指定表示一个空值的字符串。文本格式中默认是 `\N` （反斜线-N）， `CSV` 格式中默认是一个未加引用的空串。在你不想区分空值和空串的情况下，即使在文本格式中你也可能更喜欢空串。使用 `binary` 格式时不允许这个选项。

> **注意：**
> 
> 在使用 `COPY FROM` 时，任何匹配这个串的数据项将被存储为空值，因此你应该确定你使用的是和 `COPY TO` 时相同的串。

`HEADER`  
指定文件包含标题行，其中有每一列的名称。在输出时，第一行包含来自表的列名。在输入时，第一行会被忽略。只有使用 `CSV` 格式时才允许这个选项。

`QUOTE`  
指定一个数据值被引用时使用的引用字符。默认是双引号。这必须是一个单一的单字节字符。只有使用 `CSV` 格式时才允许这个选项。

`ESCAPE`  
指定应该出现在一个匹配 `QUOTE` 值的数据字符之前的字符。默认和 `QUOTE` 值一样（这样如果引用字符出现在数据中，它会被双写）。这必须是一个单一的单字节字符。只有使用 `CSV` 格式时才允许这个选项。

`FORCE_QUOTE`  
强制必须对每个指定列中的所有非 `NULL` 值使用引用。 `NULL` 输出不会被引用。如果指定了 `*` ，所有列的非 `NULL` 值都将被引用。只有在 `COPY TO` 中使用 `CSV` 格式时才允许这个选项。

`FORCE_NOT_NULL`  
不要把指定列的值与空值串匹配。在空值串就是空串的默认情况下，这意味着空串将被读作长度为零的字符串而不是空值（即使它们没有被引用）。只有在 `COPY FROM` 中使用 `CSV` 格式时才允许这个选项。

`FORCE_NULL`  
将指定列的值与空值串匹配（即使它已经被加上引号），并且在找到匹配时将该值设置为 `NULL` 。在空值串就是空串的默认情况下，这会把一个被引用的空串转换为 `NULL` 。只有在 `COPY FROM` 中使用 `CSV` 格式时才允许这个选项。

`ENCODING`  
指定文件被以 `encoding_name` 编码。如果省略这个选项，将使用当前的客户端编码。详见下文的注解。

`WHERE`  
`WHERE` 子句是可选的，其一般形式是：

```sql
WHERE condition
```

其中 `condition` 是计算结果为 `boolean` 类型的任意表达式。任何不满足此条件的行都不会插入到表中。在用实际的行值替换任何变量引用时，如果该行返回 `true` ，则该行满足条件。

目前，在 `WHERE` 表达式中不允许使用子查询，并且值的计算不会看到 `COPY` 本身所做的任何更改（当表达式包含对 `VOLATILE` 函数的调用时，这一点很重要）。

**输出**

在成功完成时，一个 `COPY` 命令会返回一个形为 `COPY count` 的命令标签。 `count` 是被复制的行数。

> **注意：**
> 
> 如果命令不是 `COPY ... TO STDOUT` 或者等效的 `psql` 元命令 `\copy ... to stdout` ， `psql` 将只打印这个命令标签。这是为了防止弄混命令标签和刚刚打印的数据。

**注解**

`COPY TO` 只能被用于纯粹的表，不能用于视图。不过你可以写 `COPY (SELECT * FROM viewname) TO ...` 来拷贝一个视图的当前内容。

`COPY FROM` 可以被用于普通表、外部表、分区表或者具有 `INSTEAD OF INSERT` 触发器的视图。

`COPY` 只处理提到的表，它不会从子表复制数据或者复制数据到子表中。例如 `COPY table TO` 会显示与 `SELECT * FROM ONLY table` 相同的数据。而 `COPY (SELECT * FROM table) TO ...` 可以被用来转储一个继承层次中的所有数据。

你必须拥有被 `COPY TO` 读取的表上的选择特权，以及被 `COPY FROM` 插入的表上的插入特权。

拥有在命令中列出的列上的特权就足够了。

如果对表启用了行级安全性，相关的 `SELECT` 策略将应用于 `COPY table TO` 语句。当前，有行级安全性的表不支持 `COPY FROM` 。不过可以使用等效的 `INSERT` 语句。

`COPY` 命令中提到的文件会被服务器（而不是客户端应用）直接读取或写入。因此它们必须位于数据库服务器（不是客户端）的机器上或者是数据库服务器可以访问的。它们必须是瀚高数据库用户（运行服务器的用户 ID）可访问的并且是可读或者可写的。类似地，用 `PROGRAM` 指定的命令也会由服务器（不是客户端应用）直接执行，它也必须是瀚高数据库用户可以执行的。只允许数据库超级用户或者授予了默认角色 `pg_read_server_files` 、 `pg_write_server_files` 及 `pg_execute_server_program` 之一的用户 `COPY` 一个文件或者命令，因为它允许读取或者写入服务器有特权访问的任何文件或者运行服务器有特权访问的程序。

不要把 `COPY` 和 `psql` 指令 `\copy` 弄混。 `\copy` 会调用 `COPY FROM STDIN` 或者 `COPY TO STDOUT` ，然后读取/存储一个 `psql` 客户端可访问的文件中的数据。因此，在使用 `\copy` 时，文件的可访问性和访问权利取决于客户端而不是服务器。

我们推荐在 `COPY` 中使用的文件名总是指定为一个绝对路径。在 `COPY TO` 的情况下服务器会强制这一点，但是对于 `COPY FROM` 你可以选择从一个用相对路径指定的文件中读取。该路径将根据服务器进程（而不是客户端）的工作目录（通常是集簇的数据目录）解释。

用 `PROGRAM` 执行一个命令可能会受到操作系统的访问控制机制（如 SELinux）的限制。

`COPY FROM` 将调用目标表上的任何触发器和检查约束。但是它不会调用规则。

对于标识列， `COPY FROM` 命令将总是写上输入数据中提供的列值，这和 `INSERT` 的选项 `OVERRIDING SYSTEM VALUE` 的行为一样。

`COPY` 输入和输出受到 `DateStyle` 的影响。为了确保到其他可能使用非默认 `DateStyle` 设置的瀚高数据库安装的可移植性，在使用 `COPY TO` 前应该把 `DateStyle` 设置为 `ISO` 。避免转储把 `IntervalStyle` 设置为 `sql_standard` 的数据也是一个好主意，因为负的区间值可能会被具有不同 `IntervalStyle` 设置的服务器解释错误。

即使数据会被服务器直接从一个文件读取或者写入一个文件而不通过客户端，输入数据也会被根据 `ENCODING` 选项或者当前客户端编码解释，并且输出数据会被根据 `ENCODING` 或者当前客户端编码进行编码。

`COPY` 会在第一个错误处停止操作。这在 `COPY TO` 的情况下不会导致问题，但是在 `COPY FROM` 中目标表将已经收到了一些行。这些行将不会变得可见或者可访问，但是它们仍然占据磁盘空间。如果在一次大型的复制操作中出现错误，这可能浪费相当可观的磁盘空间。

你可能希望调用 `VACUUM` 来恢复被浪费的空间。

`FORCE_NULL` 和 `FORCE_NOT_NULL` 可以被同时用在同一列上。这会导致把已被引用的空值串转换为空值并且把未引用的空值串转换为空串。

**文件格式**

- **文本格式**

在使用 `text` 格式时，读取或写入的是一个文本文件，其中每一行就是表中的一行。一行中的列被定界字符分隔。列值本身是由输出函数产生的或者是可被输入函数接受的属于每个属性数据类型的字符串。在为空值的列的位置使用指定的空值串。如果输入文件的任何行包含比预期更多或者更少的列， `COPY FROM` 将会抛出一个错误。

数据的结束可以表示为一个只包含反斜线-点号（ `\.`）的单一行。从一个文件读取时，数据结束标记并不是必要的，因为文件结束符就已经足够用了。只有使用 3.0 客户端协议之前的客户端应用复制数据时才需要它。

反斜线字符（ `\` ）可以被用在 `COPY` 数据中来引用被用作行或者列定界符的字符。特别地，如果下列字符作为一个列值的一部分出现，它们必须被前置一个反斜线：反斜线本身、新行、回车以及当前的定界符字符。

`COPY TO` 会不加任何反斜线返回指定的空值串。相反， `COPY FROM` 会在移除反斜线之前把输入与空值串相匹配。因此，一个空值串（例如 `\N` ）不会与实际的数据值 `\N` （它会被表示为 `\\N` ）搞混。

`COPY FROM` 识别下列特殊的反斜线序列：

| **序列** | **表示** |
| --- | --- |
| `\b` | 退格 (ASCII 8) |
| `\f` | 换页 (ASCII 12) |
| `\n` | 新行 (ASCII 10) |
| `\r` | 回车 (ASCII 13) |
| `\t` | 制表 (ASCII 9) |
| `\v` | 纵向制表 (ASCII 11) |
| `\digits` | 反斜线后跟一到三个十进制位表示该数字代码对应的字符 |
| `\xdigits` | 反斜线加 x 后跟一到三个十六进制位表示该数字代码对应的字符 |

当前， `COPY TO` 不会发出一个十进制或十六进制位反斜线序列，但是它确实把上面列出的其他序列用于那些控制字符。

任何上述表格中没有提到的其他反斜线字符将被当作表示其本身。不过，要注意增加不必要的反斜线，因为那可能意外地产生一个匹配数据结束标记（ `\.`）或者空值串（默认是 `\N` ）的字符串。这些字符串将在完成任何其他反斜线处理之前被识别。

强烈建议产生 `COPY` 数据的应用把数据新行和回车分别转换为 `\n` 和 `\r` 序列。当前可以把一个数据回车表示为一个反斜线和回车，把一个数据新行表示为一个反斜线和新行。不过，未来的发行可能不会接受这些表示。如果在不同的机器之间（例如从 Unix 到 Windows）传输 `COPY` 文件，它们也很容易受到破坏。

`COPY TO` 将用一个 Unix 风格的新行（ `"\n"` ）终止每一行。运行在 Microsoft Windows 上的服务器则会输出回车/新行（ `"\r\n"` ），不过只对 `COPY` 到一个服务器文件这样做。为了做到跨平台一致， `COPY TO STDOUT` 总是发送 `"\n"` 而不管服务器平台是什么。 `COPY FROM` 能够处理以新行、回车或者回车/新行结尾的行。为了减少由作为数据的未加反斜线的新行或者回车带来的风险，如果输出中的行结束并不完全相似， `COPY FROM` 将会抱怨。

- **CSV 格式**

这种格式选项被用于导入和导出很多其他程序（例如电子表格）使用的逗号分隔值（CSV）文件格式。不同于瀚高数据库标准文本格式使用的转义规则，它产生并且识别一般的 CSV 转义机制。

每个记录中的值用 `DELIMITER` 字符分隔。如果值包含定界符字符、 `QUOTE` 字符、 `NULL` 字符串、一个回车或者换行字符，那么整个值会被加上 `QUOTE` 字符作为前缀或者后缀，并且在该值内 `QUOTE` 字符或者 `ESCAPE` 字符的任何一次出现之前放上转义字符。在输出指定列中非 `NULL` 值时，还可以使用 `FORCE_QUOTE` 来强制加上引用。

CSV 格式没有标准方式来区分 `NULL` 值和空字符串。瀚高数据库的 `COPY` 用引用来处理这种区分工作。 `NULL` 被按照 `NULL` 参数字符串输出并且不会被引用，而匹配 `NULL` 参数字符串的非 `NULL` 值会被加上引用。例如，使用默认设置时， `NULL` 被写作一个未被引用的空字符串，而一个空字符串数据值会被写成带双引号（ `""` ）。值的读取遵循类似的规则。你可以用 `FORCE_NOT_NULL` 来防止对指定列的 `NULL` 输入比较。你还可以使用 `FORCE_NULL` 把带引用的空值字符串数据值转换成 `NULL` 。

因为反斜线在 CSV 格式中不是一种特殊字符，数据结束标记 `\.` 也可以作为一个数据值出现。

为了避免任何解释误会，在一行上作为孤项出现的 `\.` 数据值输出时会自动被引用，并且输入时如果被引用，则不会被解释为数据结束标记。如果正在载入一个由另一个应用创建的文件并且其中具有一个未被引用的列且可能具有 `\.` 值，你可能需要在输入文件中引用该值。

> **注意：**
> 
> CSV 格式中，所有字符都是有意义的。一个被空白或者其他非 `DELIMITER` 字符围绕的引用值将包括那些字符。在导入来自用空白填充 CSV 行到固定长度的系统的数据时，这可能会导致错误。如果出现这种情况，在导入数据到瀚高数据库之前，你可能需要预处理该 CSV 文件以移除拖尾的空白。

> **注意：**
> 
> CSV 格式将识别并且产生带有包含嵌入的回车和换行的引用值的 CSV 文件。因此文件并不限于文本格式文件的每个表行一行的形式。

> **注意：**
> 
> 很多程序会产生奇怪的甚至偶尔是不合常理的 CSV 文件，因此该文件格式更像是一种习惯而不是标准。因此你可能会碰到一些无法使用这种机制导入的文件，并且 `COPY` 也可能产生其他程序无法处理的文件。

- **二进制格式**

`binary` 格式选项导致所有数据被以二进制格式而不是文本格式存储/读取。它比文本和 CSV 格式要快一些，但是二进制格式文件在不同的机器架构和瀚高数据库版本之间的可移植性要差些。还有，二进制格式与数据格式非常相关。例如不能从一个 `smallint` 列中输出二进制数据并且把它读入到一个 `integer` 列中，虽然这样做在文本格式中是可行的。

二进制文件格式由一个文件头、零个或者更多个包含行数据的元组以及一个文件尾构成。

头部和数据都以网络字节序表示。

**文件头**

文件头由 15 字节的固定域构成，后面跟着一个变长的头部扩展区。固定域有：

**签名**  
11-字节的序列 `PGCOPY\n\377\r\n\0` — 注意零字节是签名的一个必要的部分（该签名是为了能容易地发现文件被无法正确处理 8 位字符编码的传输所破坏。这个签名将被行尾翻译过滤器、删除零字节、删除高位或者奇偶修改等改变）。

**标志域**  
32-位整数位掩码，用以表示该文件格式的重要方面。位被编号为从 0 （LSB）到 31（MSB）。注意这个域以网络字节序存放（最高有效位在前），所有该文件格式中使用的整数域都是这样。16-31 位被保留用来表示严重的文件格式问题，读取者如果在这个范围内发现预期之外的被设置位，它应该中止。0-15 位被保留用来表示向后兼容的格式问题，读取者应该简单地略过这个范围内任何预期之外的被设置位。当前只定义了一个标志位，其他位必须为零：

位 16：如果为 1，表示数据中包含 OID；如果为 0，则不包含。瀚高数据库不再支持 Oid 系统列，但是格式仍然包含该指示符。

**头部扩展区长度**  
32-为整数，表示头部剩余部分的以字节计的长度，不包括其本身。当前，这个长度为零，并且其后就紧跟着第一个元组。未来对该格式的更改可能会允许在头部中表示额外的数据。如果读取者不知道要对头部扩展区数据做什么，可以安静地跳过它。

头部扩展区域被预期包含一个能自我解释的块的序列。该标志域并不想告诉读取者扩展数据是什么。详细的头部扩展内容的设计留给后来的发行去做。

这种设计允许向后兼容的头部增加（增加头部扩展块或者设置低位标志位）以及非向后兼容的更改（设置高位标志位来表示这类更改并且在需要时向扩展区域中增加支持数据）。

**元组**

每一个元组由一个表示元组中域数量的 16 位整数计数开始（当前，一个表中的所有元组都应该具有相同的计数，但是这可能不会总是为真）。然后是元组中的每一个域，它是一个 32 位的长度字，后面则跟随着这么多个字节的域数据（长度字不包括其本身，并且可以是零）。作为一种特殊情况，-1 表示一个 `NULL` 域值。在 `NULL` 情况下，后面不会跟随值字节。

在域之间没有对齐填充或者任何其他额外的数据。

当前，一个二进制格式文件中的所有数据值都被假设为二进制格式（格式代码一）。可以预见未来的扩展可能会增加一个允许独立指定各列的格式代码的头部域。

如果文件中包含 OID，OID 域会紧跟在域计数字之后。它是一个普通域，不过它没有被包含在域计数中。注意瀚高数据库当前版本不支持 oid 系统列。

**文件尾**

文件位由一个包含 -1 的 16 位整数字组成。这很容易与一个元组的域计数字区分开。

如果一个域计数字不是 -1 也不是期望的列数，读取者应该报告错误。这提供了一种针对某种数据不同步的额外检查。

**示例**

下面的例子使用竖线（ `|` ）作为域定界符把一个表复制到客户端：

```sql
COPY country TO STDOUT (DELIMITER '|');
```

从一个文件中复制数据到 `country` 表中：

```sql
COPY country FROM '/usr1/proj/bray/sql/country_data';
```

只把名称以 ‘A’ 开头的国家复制到一个文件中：

```sql
COPY (SELECT * FROM country WHERE country_name LIKE 'A%') TO '/usr1/proj/bray/sql/a_list_countries.copy';
```

要复制到一个压缩文件中，你可以用管道把输出导到一个外部压缩程序：

```sql
COPY country TO PROGRAM 'gzip > /usr1/proj/bray/sql/country_data.gz';
```

这里是一个适合于从 `STDIN` 复制到表中的数据：

```
AF      AFGHANISTAN
AL      ALBANIA
DZ      ALGERIA
ZM      ZAMBIA
ZW      ZIMBABWE
```

注意每一行上的空白实际是一个制表符。

下面是用二进制格式输出的相同数据。该数据是用 Unix 工具 `od -c` 过滤后显示的。该表具有三列，第一列类型是 `char(2)` ，第二列类型是 `text` ，第三列类型是 `integer` 。所有行在第三列都是空值。

```
0000000   P   G   C   O   P   Y  \n 377  \r  \n  \0  \0  \0  \0  \0  \0
0000020  \0  \0  \0  \0 003  \0  \0  \0 002   A   F  \0  \0  \0 013   A
0000040   F   G   H   A   N   I   S   T   A   N 377 377 377 377  \0 003
0000060  \0  \0  \0 002   A   L  \0  \0  \0 007   A   L   B   A   N   I
0000100   A 377 377 377 377  \0 003  \0  \0  \0 002   D   Z  \0  \0  \0
0000120 007   A   L   G   E   R   I   A 377 377 377 377  \0 003  \0  \0
0000140  \0 002   Z   M  \0  \0  \0 006   Z   A   M   B   I   A 377 377
0000160 377 377  \0 003  \0  \0  \0 002   Z   W  \0  \0  \0  \b   Z   I
0000200   M   B   A   B   W   E 377 377 377 377 377 377
```

**兼容性**

SQL 标准中没有 `COPY` 语句。

下列语法用于旧版本的瀚高数据库，并且仍然被支持：

```sql
COPY table_name [ ( column_name [, ...] ) ]
FROM { 'filename' | STDIN }
[ [ WITH ]
  [ BINARY ]
  [ DELIMITER [ AS ] 'delimiter_character' ]
  [ NULL [ AS ] 'null_string' ]
  [ CSV [ HEADER ]
        [ QUOTE [ AS ] 'quote_character' ]
        [ ESCAPE [ AS ] 'escape_character' ]
        [ FORCE NOT NULL column_name [, ...] ] ] ]

COPY { table_name [ ( column_name [, ...] ) ] | ( query ) }
TO { 'filename' | STDOUT }
[ [ WITH ]
  [ BINARY ]
  [ DELIMITER [ AS ] 'delimiter_character' ]
  [ NULL [ AS ] 'null_string' ]
  [ CSV [ HEADER ]
        [ QUOTE [ AS ] 'quote_character' ]
        [ ESCAPE [ AS ] 'escape_character' ]
        [ FORCE QUOTE { column_name [, ...] | * } ] ] ]
```

注意在这种语法中， `BINARY` 和 `CSV` 被视作独立的关键词，而不是 `FORMAT` 选项的参数。

下列语法用于旧版本的瀚高数据库，并且仍然被支持：

```sql
COPY [ BINARY ] table_name
FROM { 'filename' | STDIN }
[ [USING] DELIMITERS 'delimiter_character' ]
[ WITH NULL AS 'null_string' ]

COPY [ BINARY ] table_name
TO { 'filename' | STDOUT }
[ [USING] DELIMITERS 'delimiter_character' ]
[ WITH NULL AS 'null_string' ]
```

## CREATE ACCESS METHOD

— 定义一种新的访问方法

**大纲**

```sql
CREATE ACCESS METHOD name
    TYPE access_method_type
    HANDLER handler_function
```

**描述**

`CREATE ACCESS METHOD` 创建一种新的访问方法。

访问方法名称在数据库中必须唯一。

只有超级用户可以定义新的访问方法。

**参数**

`name`  
要创建的访问方法的名称。

`access_method_type`  
这个子句指定要定义的访问方法的类型。当前只支持 `TABLE` 和 `INDEX` 。

`handler_function`  
`handler_function` 是一个之前已注册的函数的名称（可能被模式限定），该函数表示要创建的访问方法。处理器函数必须被声明为接收一个单一的 `internal` 类型的参数，并且它的返回类型取决于访问方法的类型；对于 `TABLE` 访问方法，它必须是 `table_am_handler` ，而对于 `INDEX` 访问方法，它必须是 `index_am_handler` 。处理器函数必须实现的 C 级别 API 取决于访问方法的类型。

**示例**

用处理器函数 `heptree_handler` 创建一种索引访问方法 `heptree` ：

```sql
CREATE ACCESS METHOD heptree TYPE INDEX HANDLER heptree_handler;
```

**兼容性**

`CREATE ACCESS METHOD` 是一种瀚高数据库扩展。

**另见**

`DROP ACCESS METHOD`,`CREATE OPERATOR CLASS`,`CREATE OPERATOR FAMILY`

## CREATE AGGREGATE

— 定义一个新的聚集函数

**大纲**

```sql
CREATE [ OR REPLACE ] AGGREGATE name ( [ argmode ] [ argname ] arg_data_type
    [ , ... ] ) (
    SFUNC = sfunc,
    STYPE = state_data_type
    [ , SSPACE = state_data_size ]
    [ , FINALFUNC = ffunc ]
    [ , FINALFUNC_EXTRA ]
    [ , FINALFUNC_MODIFY = { READ_ONLY | SHAREABLE | READ_WRITE } ]
    [ , COMBINEFUNC = combinefunc ]
    [ , SERIALFUNC = serialfunc ]
    [ , DESERIALFUNC = deserialfunc ]
    [ , INITCOND = initial_condition ]
    [ , MSFUNC = msfunc ]
    [ , MINVFUNC = minvfunc ]
    [ , MSTYPE = mstate_data_type ]
    [ , MSSPACE = mstate_data_size ]
    [ , MFINALFUNC = mffunc ]
    [ , MFINALFUNC_EXTRA ]
    [ , MFINALFUNC_MODIFY = { READ_ONLY | SHAREABLE | READ_WRITE } ]
    [ , MINITCOND = minitial_condition ]
    [ , SORTOP = sort_operator ]
    [ , PARALLEL = { SAFE | RESTRICTED | UNSAFE } ]
)

CREATE [ OR REPLACE ] AGGREGATE name ( [ [ argmode ] [ argname ] arg_data_type
    [ , ... ] ]
    ORDER BY [ argmode ] [ argname ] arg_data_type
    [ , ... ] ) (
    SFUNC = sfunc,
    STYPE = state_data_type
    [ , SSPACE = state_data_size ]
    [ , FINALFUNC = ffunc ]
    [ , FINALFUNC_EXTRA ]
    [ , FINALFUNC_MODIFY = { READ_ONLY | SHAREABLE | READ_WRITE } ]
    [ , INITCOND = initial_condition ]
    [ , HYPOTHETICAL ]
    [ , PARALLEL = { SAFE | RESTRICTED | UNSAFE } ]
)
```

或者旧的语法：

```sql
CREATE [ OR REPLACE ] AGGREGATE name (
    BASETYPE = base_type,
    SFUNC = sfunc,
    STYPE = state_data_type
    [ , SSPACE = state_data_size ]
    [ , FINALFUNC = ffunc ]
    [ , FINALFUNC_EXTRA ]
    [ , FINALFUNC_MODIFY = { READ_ONLY | SHAREABLE | READ_WRITE } ]
    [ , COMBINEFUNC = combinefunc ]
    [ , SERIALFUNC = serialfunc ]
    [ , DESERIALFUNC = deserialfunc ]
    [ , INITCOND = initial_condition ]
    [ , MSFUNC = msfunc ]
    [ , MINVFUNC = minvfunc ]
    [ , MSTYPE = mstate_data_type ]
    [ , MSSPACE = mstate_data_size ]
    [ , MFINALFUNC = mffunc ]
    [ , MFINALFUNC_EXTRA ]
    [ , MFINALFUNC_MODIFY = { READ_ONLY | SHAREABLE | READ_WRITE } ]
    [ , MINITCOND = minitial_condition ]
    [ , SORTOP = sort_operator ]
)
```

**描述**

`CREATE AGGREGATE` 定义一个新的聚集函数。 `CREATE OR REPLACE AGGREGATE` 将定义新的聚合函数或替换现有定义。在发布中已经包括了一些基本的和常用的聚集函数。如果要定义一个新类型或者需要一个还没有被提供的聚集函数，那么 `CREATE AGGREGATE` 就可以被用来提供想要的特性。

在替换现有定义时，参数类型、结果类型和直接参数的数量可能不会更改。此外，新定义的类型（普通聚合、有序集聚合或假设集聚合）必须与旧定义相同。

如果给定了一个模式名（例如 `CREATE AGGREGATE myschema.myagg ...`），那么该聚集会被创建在指定的模式中。否则它会被创建在当前模式中。

一个聚集函数需要用它的名称和输入数据类型标识。同一个模式中的两个聚集可以具有相同的名称，只要它们在不同的输入类型上操作即可。一个聚集的名称和输入数据类型必须与同一模式中的每一个普通函数区分开。这种行为与普通函数名的重载完全一样（见 `CREATE FUNCTION` ）。

一个简单的聚集函数由一个或者多个普通函数组成：一个状态转移函数 `sfunc` 和一个可选的最终计算函数 `ffunc` 。它们被这样使用：

```
sfunc( internal-state, next-data-values ) ---> next-internal-state
ffunc( internal-state ) ---> aggregate-value
```

瀚高数据库创建一个数据类型 `stype` 的临时变量来保持聚集的当前内部状态。对每一个输入行，聚集参数值会被计算并且状态转移函数会被调用，它用当前状态值和新参数值计算一个新的内部状态值。等所有行都被处理完后，最终函数会被调用一次来计算该聚集的返回值。如果没有最终函数，则最终的状态值会被返回。

一个聚集函数可以提供一个初始条件，即一个用于内部状态值的初始值。它被作为一个类型 `text` 的值指定并且存储在数据库中，但是它必须是状态值数据类型的一个常量的合法外部表示。如果没有提供，则状态值从空值开始。

如果状态转移函数被声明为 “strict”，那么不能用空值输入来调用它。如果有这种转移函数，聚集将按照下面的行为执行。带有任何空值的行会被忽略（函数不被调用并且之前的状态值被保持）。如果初始状态值就是空值，那么碰到第一个没有空值的行时，状态值会被替换成第一个参数值，并且对于每一个后续的没有空值的行都会调用该转移函数。这对实现 `max` 这样的聚集很方便。注意只有当 `state_data_type` 和第一个 `arg_data_type` 相同时，这种行为才可用。当这些类型不同时，你必须提供一个非空初始条件或者使用一个非严格转移函数。

如果状态转移函数不是严格的，那么在碰到每个输入行时都将会调用它，并且它必须自行处理空值输入和空状态值。这允许聚集的作者完全控制该聚集如何处理空值。

如果最终函数被声明为 “strict”，那么当最终状态值为空时将不会调用它，而是自动地返回一个空结果（当然，这只是严格函数的普通行为）。在任何情况下最终函数都可以返回一个空值。例如， `avg` 的最终函数会在看到零个输入行时返回空。

有时候把最终函数声明成不仅采用状态值还采用对应于聚集输入值的额外参数是有用的。

这样做的主要原因是，如果最终函数是多态的，那么状态值的数据类型将不适合于用来确定结果类型。这些额外的参数总是以 NULL 形式传递（因此使用 `FINALFUNC_EXTRA` 选项时，最终函数不能是严格的），但尽管如此它们都是合法参数。例如，最终函数可以利用 `get_fn_expr_argtype` 来标识当前调用中的实际参数类型。

一个聚集可以选择支持 moving-aggregate mode。这要求指定 `MSFUNC` 、 `MINVFUNC` 以及 `MSTYPE` 参数，并且参数 `MSSPACE` 、 `MFINALFUNC` 、 `MFINALFUNC_EXTRA` 和 `MINITCOND` 是可选的。除了 `MINVFUNC` ，这些参数的工作都和对应的不带 `M` 的简单聚集参数相似，它们定义了包括一个逆向转移函数的聚集的一种独立实现。

在参数列表中带有 `ORDER BY` 的语法会创建一种被称为有序集聚集的特殊聚集类型。如果指定了 `HYPOTHETICAL` ，则会创建一个假想集聚集。这些聚集以依赖排序的方法在排好序的值上操作，因此指定一个输入排序顺序是调用过程的重要一环。还有，它们可以有直接参数，这类参数只对每次聚集计算一次，而不是对每一个输入行计算一次。假想集聚集是有序集聚集的一个子类，其中一些直接参数要求在数量和类型上都匹配被聚集的参数列。这允许这些直接参数的值被当做一个附加的”假想”行被加入到聚集输入行的集合中。

一个聚集可以支持部分聚集。这要求指定 `COMBINEFUNC` 参数。如果 `state_data_type` 为 `internal` ，通常也可以提供 `SERIALFUNC` 和 `DESERIALFUNC` 参数，这样可以让并行聚集成为可能。注意，该聚集还必须被标记为 `PARALLEL SAFE` 以启用并行聚集。

行为与 `MIN` 或 `MAX` 相似的聚集有时可以通过直接查看一个索引而不是扫描每一个输入行来优化。如果这个聚集可以被这样优化，请通过指定一个排序操作符来指出。基本要求是，该聚集必须得出由该操作符产生的排序顺序中的第一个元素，换句话说：

```sql
SELECT agg(col) FROM tab;
```

必须等价于：

```sql
SELECT col FROM tab ORDER BY col USING sortop LIMIT 1;
```

进一步的假定是该聚集忽略空输入，并且当且仅当没有非空输入时它才会返回一个空结果。通常，一种数据类型的 `<` 操作符是 `MIN` 的合适的排序操作符，而 `>` 是 `MAX` 的合适的排序操作符。注意，除非指定的操作符是一个 B-树索引操作符类的”小于”或者”大于”策略成员，优化将永远不会产生实际效果。

要能够创建一个聚集函数，你必须具有参数类型、状态类型和返回类型上的 `USAGE` 特权，还有在支持函数上的 `EXECUTE` 特权。

**参数**

`name`  
要创建的聚集函数的名称（可以是模式限定的）。

`argmode`  
一个参数的模式： `IN` 或者 `VARIADIC` （聚集函数不支持 `OUT` 参数）。如果忽略，默认值是 `IN` 。只有最后一个参数能被标记为 `VARIADIC` 。

`argname`  
一个参数的名称。当前这只用于文档的目的。如果被忽略，该参数就没有名称。

`arg_data_type`  
这个聚集函数操作的一个输入数据类型。要创建一个零参数的聚集函数，可以写一个 `*` 来替代参数说明的列表（这类聚集的一个例子是 `count(*)` ）。

`base_type`  
在 `CREATE AGGREGATE` 的旧语法中，输入数据类型是由一个 `basetype` 参数指定而不是写在聚集名之后。注意这种语法只允许一个输入参数。要用这种语法定义一个零参数的聚集函数，把 `basetype` 指定为 `"ANY"` （不是 `*` ）。有序集聚集不能用旧语法定义。

`sfunc`  
要为每一个输入行调用的状态转移函数名。对于一个正常的 N-参数的聚集函数， `sfunc` 必须接收 N+1 个参数，第一个参数的类型是 `state_data_type` 而其余的参数匹配该聚集被声明的输入数据类型。该函数必须返回一个类型为 `state_data_type` 的值。这个函数会采用当前的状态值以及当前的输入数据值，并且返回下一个状态值。

对于有序集（包括假想集）聚集，状态转移函数只接收当前的状态值和聚集参数，但无需直接参数。否则它就和其他转移函数一样了。

`state_data_type`  
聚集的状态值的数据类型。

`state_data_size`  
聚集的状态值的近似平均尺寸（以字节计）。如果这个参数被忽略或者为零，将使用一个基于 `state_data_type` 的默认估计值。规划器使用这个值来估计一个分组聚集查询所需的内存。只有估计哈希表能够放在 `work_mem` 大小的内存中时，规划器才会对这类查询使用哈希聚集。因此，对这个参数设置大的值会阻止使用哈希聚集。

`ffunc`  
最终函数的名称，该函数在所有输入行都被遍历之后被调用来计算聚集的结果。对于一个常规聚集，这个函数必须只接受一个类型为 `state_data_type` 的单一参数。该聚集的返回数据类型被定义为这个函数的返回类型。如果没有指定 `ffunc` ，则结束状态值被用作聚集的结果，并且返回类型为 `state_data_type` 。

对于有序集（包括假想集）聚集，最终函数不仅接收最终状态值，还会接收所有直接参数的值。

如果指定了 `FINALFUNC_EXTRA` ，则除了最终状态值和任何直接参数之外，最终函数还接收额外的对应于该聚集的常规（聚集）参数的 NULL 值。这主要用于在定义了一个多态聚集时允许正确地决定聚集的结果类型。

`FINALFUNC_MODIFY = { READ_ONLY | SHAREABLE | READ_WRITE }`  
此选项指定最终函数是否为不会修改参数的纯函数。 `READ_ONLY` 表示它不会修改；其他两个值表示它可能会更改迁移状态值。请参见注解以获取更多详细信息。除了有序集合的聚合使用默认值 `READ_WRITE` ，其他默认值均为 `READ_ONLY` 。

`combinefunc`  
`combinefunc` 函数可以被有选择地指定以允许聚集函数支持部分聚集。如果提供这个函数， `combinefunc` 必须组合两个 `state_data_type` 值，每一个都包含在输入值某个子集上的聚集结果，它会产生一个新的 `state_data_type` 来表示在两个输入集上的聚集结果。这个函数可以被看做是一个 `sfunc` ，和后者在一个个体输入行上操作并且把它加到运行聚集状态上不同，这个函数是把另一个聚集状态加到运行状态上。

`combinefunc` 必须被声明为有两个 `state_data_type` 参数并且返回一个 `state_data_type` 值。这个函数可以有选择性地被标记为 “strict”。在被标记的情况下，当任何一个输入状态为空时，将不会调用该函数，而是把另一个状态当作正确的结果。

对于 `state_data_type` 为 `internal` 的聚集函数， `combinefunc` 不能为 strict。这种情况下， `combinefunc` 必须确保正确地处理空状态并且被返回的状态能被恰当地存储在聚集内存上下文中。

`serialfunc`  
`state_data_type` 为 `internal` 的一个聚集函数可以参与到并行聚集中，当且仅当它具有一个 `serialfunc` 函数，该函数必须把聚集状态序列化成一个 `bytea` 值以传送给另一个进程。这个函数必须有一个单一的 `internal` 类型参数并且返回类型 `bytea` 。相应地也需要一个 `deserialfunc` 。

`deserialfunc`  
把一个之前序列化后的聚集状态反序列化为 `state_data_type` 。这个函数必须有两个类型分别为 `bytea` 和 `internal` 的参数，并且产生一个类型 `internal` 的结果（注意：第二个类型为 `internal` 的参数是无用的，但是为了类型安全的原因还是要求有该参数）。

`initial_condition`  
状态值的初始设置。这必须是以数据类型 `state_data_type` 能够接受的形式出现的一个字符串常量。如果没有指定，状态值会从空值开始。

`msfunc`  
前向状态转移函数的名称，在移动聚集模式中会为每个输入行调用这个函数。它非常像常规的转移函数，不过它的第一个参数和结果类型是 `mstate_data_type` ，这可能与 `state_data_type` 不同。

`minvfunc`  
在移动聚集模式中用到的逆向状态转移函数的名称。这个函数与 `msfunc` 具有相同的参数和结果类型，但是它被用于从当前聚集状态中移除一个值，而不是向其中增加一个值。

逆向转移函数必须具有和前向状态转移函数相同的严格性属性。

`mstate_data_type`  
使用移动聚集模式时，用于聚集状态值的数据类型。

`mstate_data_size`  
使用移动聚集模式时，聚集状态值的近似平均尺寸（以字节计）。它的作用和 `state_data_size` 相同。

`mffunc`  
使用移动聚集模式时用到的最终函数名称，当所有输入行都被遍历后会调用它来计算聚集的结果。它的工作和 `ffunc` 一样，但是它的第一个参数类型是 `mstate_data_type` 并且额外的空参数要通过书写 `MFINALFUNC_EXTRA` 来指定。 `mffunc` 或者 `mstate_data_type` 决定的聚集结果类型必须匹配由聚集的常规实现所确定的类型。

`MFINALFUNC_MODIFY = { READ_ONLY | SHAREABLE | READ_WRITE }`  
此选项类似于 `FINALFUNC_MODIFY` ，只是它描述了移动聚集最终函数的行为。

`minitial_condition`  
使用移动聚集模式时，状态值的初始设置。它的作用和 `initial_condition` 一样。

`sort_operator`  
一个 `MIN` - 类或者 `MAX` -类聚集的相关排序操作符。这只是一个操作符名称（可能被模式限定）。这个操作符被假定为具有和该聚集（必须是一个单一参数的常规聚集）相同的输入数据类型。

`PARALLEL = { SAFE | RESTRICTED | UNSAFE }`  
`PARALLEL SAFE` 、 `PARALLEL RESTRICTED` 和 `PARALLEL UNSAFE` 的含义和 `CREATE FUNCTION` 中的相同。如果一个聚集被标记为 `PARALLEL UNSAFE` （默认）或者 `PARALLEL RESTRICTED` ，将不会考虑将它并行化。注意规划器不会参考聚集的支持函数的并行安全性标记，它只会考虑聚集本身的这类标记。

`HYPOTHETICAL`  
只用于有序集聚集，这个标志指定聚集参数会被根据假想集聚集的要求进行处理：即后面的直接参数必须匹配聚集（ `WITHIN GROUP` ）参数的数据类型。 `HYPOTHETICAL` 标志在运行时没有任何效果，它只在命令解析期间对确定数据类型和聚集参数的排序规则有用。

`CREATE AGGREGATE` 的参数可以用任意顺序书写，而无需遵照以上说明的顺序。

**注解**

在指定支持函数名的参数中，如果需要你可以写一个模式名，例如 `SFUNC = public.sum` 。在这里不能写参数类型 — 支持函数的参数类型是根据其他参数决定的。

通常，瀚高数据库函数是不要修改输入值的真函数。然而，一个聚合迁移函数在聚合上下文中使用时被允许诈欺并修改已在迁移状态的参数。因为与每次创建一个迁移状态的新的拷贝相比，这样可以提供实质的性能提升。

同样，虽然人们一般不期望聚合最终函数修改它的输入值，但有时回避修改迁移态参数是不切实际的。这种行为必须使用 `FINALFUNC_MODIFY` 参数声明。 `READ_WRITE` 值表示最终函数以某种未指定的方式修改了迁移状态值。这个值防止将聚合用作窗口函数，并且还可以防止因共用相同的输入值和迁移函数的聚合调用而合并迁移状态。 `SHAREABLE` 值表示过渡函数不能在最终功能之后使用用，但多重最终函数调用可以对最终的迁移状态值执行调用。这个值阻止将聚合用作窗口函数，但允许合并过渡状态。（也就是说，此处所关注的优化不是重复地使用相同的最终函数，而是把不同的最终函数应用到相同的最终迁移状态值。只要所有最终功能都没有标记为 `READ_WRITE` 就被允许。）

如果一个聚集支持移动聚集模式，当该聚集被用于一个具有移动帧起点（即帧起点模式不是 `UNBOUNDED PRECEDING` ）的窗口函数时，它将提升计算效率。在概念上，当从底部进入窗口帧时前向转移函数会把输入值加到聚集的状态上，而逆向转移函数会在从顶部离开帧时再次移除输入值。因此，当值被移除时，它们总是按照被加入的相同顺序被移除。无论何时调用逆向转移函数，它都将因此接收最近增加但是还未被移除的参数值。逆向转移函数可以假定在它移除最旧的行之后至少有一行保留在当前状态中（当情况不是这样时，窗口函数机制会简单地开始一次新的聚集，而不是使用逆向转移函数）。

用于移动聚集模式的前向转移函数不允许返回 NULL 作为新的状态值。如果逆向转移函数返回 NULL，这表明逆向函数无法为这个特定的输入逆转状态计算，并且该聚集计算因此必须从当前帧的开始位置”从零开始”重新被计算。在一些少见的情况中，逆转正在计算中的状态值是不切实际的，这种习惯可以允许在此类情形中使用移动聚集模式。

如果没有提供移动聚集实现，聚集仍然可以被用于移动帧，但是只要帧起点移动，瀚高数据库都将会重新计算整个聚集。注意不管聚集有没有支持移动聚集模式，瀚高数据库都能处理一个移动帧结束而无需重新计算，这可以通过增加新值到聚集状态完成。这就是为什么使用聚合作为窗口函数需要最终函数只读的原因。人们认为最终函数不能破坏聚集的状态值，这样即使已经为一组帧边界得到了一个聚集结果值，该聚集也能继续下去。

有序集聚集的语法允许为最后一个直接参数以及最后一个聚集（ `WITHIN GROUP` ）参数指定 `VARIADIC` 。但是，当前的实现限制只能以两种方式使用 `VARIADIC` 。第一种，有续集聚集只能使用 `VARIADIC "any"` ，不能使用其他可变数组类型。第二种，如果最后一个直接参数是 `VARIADIC "any"` ，那么只能有一个聚集参数并且它也必须是 `VARIADIC "any"` （在系统目录中使用的表示中，这两个参数会被合并为一个单一的 `VARIADIC "any"` 项，因为 `pg_proc` 无法表示具有超过一个 `VARIADIC` 参数的函数）。如果该聚集是一个假想集聚集，匹配 `VARIADIC "any"` 参数的直接参数就是假想参数。任何在前面的参数表示额外的直接参数，它们不被约束为需要匹配聚集参数。

当前，有序集聚集无须支持移动聚集模式，因为它们不能被用作窗口函数。

部分（包括并行）聚集当前不被有续集聚集支持。还有，包括 `DISTINCT` 或者 `ORDER BY` 子句的聚集调用将不会使用部分聚集，因为在部分聚集时无法支持那些语义。

**兼容性**

`CREATE AGGREGATE` 是一种瀚高数据库的语言扩展。SQL 标准没有提供用户定义的聚集函数。

**另见**

`ALTER AGGREGATE`,`DROP AGGREGATE`

## CREATE CAST

— 定义一种新的造型

**大纲**

```sql
CREATE CAST (source_type AS target_type)
    WITH FUNCTION function_name [ (argument_type [, ...]) ]
    [ AS ASSIGNMENT | AS IMPLICIT ]

CREATE CAST (source_type AS target_type)
    WITHOUT FUNCTION
    [ AS ASSIGNMENT | AS IMPLICIT ]

CREATE CAST (source_type AS target_type)
    WITH INOUT
    [ AS ASSIGNMENT | AS IMPLICIT ]
```

**描述**

`CREATE CAST` 定义一种新的造型。一种造型指定如何在两种数据类型之间执行转换。例如：

```sql
SELECT CAST(42 AS float8);
```

通过调用一个之前指定的函数（这种情况中是 `float8(int4)` ）把整型常量 `42` 转换成类型 `float8` （如果没有定义合适的造型，该转换会失败）。

两种类型可以是 **二进制可强制** ，这表示该转换可以被”免费”执行而不用调用任何函数。这要求相应的值使用同样的内部表示。例如，类型 `text` 和 `varchar` 在双向都是二进制可强制的。二进制可强制性并不必是一种对称关系。例如，在当前实现中从 `xml` 到 `text` 的造型可以被免费执行，但是反向则需要一个函数来执行至少一次语法检查（两种在双向都二进制值兼容的类型也被称作 **二进制兼容** ）。

通过使用 `WITH INOUT` 语法，你可以把一种造型定义成 **I/O 转换造型** 。一种 I/O 转换造型执行时，会调用源数据类型的输出函数，并且把结果字符串传递给目标数据类型的输入函数。在很多常见情况中，这种特性避免了为转换单独定义一个造型函数。一种 I/O 转换造型表现得和一个常规的基于函数的造型相同，只是实现不同而已。

默认情况下，只有一次显式造型请求才会调用造型，形式是 `CAST(x AS typename)` 或 `x::typename` 。

如果造型被标记为 `AS ASSIGNMENT` ，那么在为一个目标数据类型的列赋值时会隐式地调用它。例如，假设 `foo.f1` 是一个类型 `text` 的列，那么如果从类型 `integer` 到类型 `text` 的造型被标记为 `AS ASSIGNMENT` ，则：

```sql
INSERT INTO foo (f1) VALUES (42);
```

将被允许，否则不会允许（我们通常使用 **赋值造型** 来描述此类造型）。

如果造型被标记为 `AS IMPLICIT` ，那么可以在任何上下文中隐式地调用它，无论是赋值还是在一个表达式内部（我们通常用术语 **隐式造型** 来描述这类造型）。例如，考虑这个查询：

```sql
SELECT 2 + 4.0;
```

解析器初始会把常量分别标记为类型 `integer` 和 `numeric` 。在系统目录中没有 `integer + numeric` 操作符，但是有一个 `numeric + numeric` 操作符。因此，如果有一种可用的从 `integer` 到 `numeric` 的造型且被标记为 `AS IMPLICIT` — 实际上确实有 — 该查询将会成功。解析器将应用该隐式造型并且解决该查询，就好像它被写成：

```sql
SELECT CAST ( 2 AS numeric ) + 4.0;
```

现在，系统目录也提供一种从 `numeric` 到 `integer` 的造型。如果这种造型被标记为 `AS IMPLICIT` — 实际上并没有 — 那么解析器将面临选择：是用前面介绍的过程，还是把 `numeric` 常量造型成 `integer` 并且应用 `integer + integer` 操作符。由于缺少哪种选择更好的知识，解析器会放弃并且说明查询有歧义。我们能告诉解析器把一个混合了 `numeric` 和 `integer` 的表达式解析成 `numeric` 更好的方法就是只让这两种造型中的一个是隐式的，没有有关于此的内建知识。

对标记造型为隐式持保守态度是明智的。过多的隐式造型路径可能导致瀚高数据库以令人吃惊的方式解释命令，或者由于有多种可能解释而根本无法解析命令。一种好的经验是让一种造型只对于同一种一般类型分类中的类型间的信息保持转换隐式可调用。例如，从 `int2` 到 `int4` 的造型可以被合理地标记为隐式，但是从 `float8` 到 `int4` 的造型可能应该只能在赋值时使用。跨类型分类的造型（如 `text` 到 `int4` ）最好只被用于显式使用。

> **注意：**
> 
> 有时为了可用性或者标准兼容的原因，有必要提供在一个类型集合之间的多种隐式造型，这会导致上述不可避免的歧义。解析器还有一招基于类型分类和优先类型的后手，它能帮助提供这类情况下预期的行为。详见 `CREATE TYPE` 。

要创建一种造型，你必须拥有源数据类型和目标数据类型并且具有在其他类型上的 `USAGE` 特权。要创建一种二进制可强制造型，你必须是一个超级用户（这种限制是因为错误的二进制可强制造型转换很容易让服务器崩溃）。

**参数**

**`source_type`**

该造型的源数据类型的名称。

**`target_type`**

该造型的目标数据类型的名称。

**`function_name[(argument_type [, ...])]`**

被用于执行该造型的函数。函数名称可以用模式限定。如果没有被限定，将在模式搜索路径中查找该函数。函数的结果数据类型必须是该造型的目标数据类型。它的参数讨论如下。如果没有指定参数列表，则该函数名称在其模式中必须是唯一的。

**`WITHOUT FUNCTION`**

指示源类型可以二进制强制到目标类型，因此执行该造型不需要函数。

**`WITH INOUT`**

指示该造型是一种 I/O 转换造型，执行需要调用源数据类型的输出函数，并且把结果字符串传递给目标数据类型的输入函数。

**`AS ASSIGNMENT`**

指示该造型可以在赋值的情况下被隐式调用。

**`AS IMPLICIT`**

指示该造型可以在任何上下文中被隐式调用。

**造型实现函数**

造型实现函数可以具有 1 到 3 个参数。第一个参数类型必须等于源类型或者能从源类型二进制强制得到。第二个参数（如果存在）必须是类型 `integer` ，它接收与目标类型相关联的类型修饰符，如果没有类型修饰符，它会收到 `-1` 。第三个参数（如果存在）必须是类型 `boolean` ，如果该造型是一种显式造型，它会收到 `true` ，否则会收到 `false` （奇怪地是，SQL标准在某些情况中对显式和隐式造型要求不同的行为。这个参数被提供给必须实现这类造型的函数。不推荐在设计自己的数据类型时用它）。

一个造型函数的返回类型必须等于目标类型或者能二进制强制到目标类型。

通常，强制转换必须具有不同的源和目标数据类型。但是，如果它有一个带有多个参数的强制转换实现函数，则可以声明具有相同源类型和目标类型的造型。它用于表示系统目录中特定类型的长度强制函数。命名函数用于将类型的值强制转为其第二个参数提供的类型修饰符的值。

当强制转换具有不同的源类型和目标类型，并且一个函数使用多个参数时，它支持从一种类型转换为另一种类型，并在单个步骤中应用长度强制。如果没有这样的条目，强制转换为使用类型修饰符的类型将涉及两个强制转换步骤，一个是在数据类型之间进行转换，另一个是应用修饰符。

向域类型强制转换或从域类型强制转换当前无效。向域或从域强制转换使用与其基础类型关联的造型。

**注解**

使用 `DROP CAST` 移除用户定义的造型。

记住如果你想要能够双向转换类型，你需要在两个方向上都显式声明造型。

通常没有必要创建用户定义类型和标准字符串类型（ `text` 、 `varchar` 和 `char(n)` ，以及被定义在字符串分类中的用户定义类型）之间的造型。瀚高数据库会为它们提供自动的 I/O 转换造型。到字符串类型的自动造型被当做赋值造型，而字符串类型作为源的自动造型只能是显式的。通过声明你自己的造型来替换自动造型可以覆盖这种行为，但是这样做的唯一原因是你想让该转换比标准的设置更容易被调用。另一种可能的原因是你想让该转换的行为与该类型的 I/O 函数不同，但这种原因足够令人感到意外，你应该考虑再三它是不是个好主意（确实有少量内建类型对转换具有不同的行为，绝大部分是因为 SQL 标准的要求）。

虽然不必要，推荐你继续遵循这种在目标数据类型后面命名造型实现函数的习惯。很多用户习惯于能够使用一种函数风格的记法来造型数据类型，即 `typename(x)` 。这种记法正好是对造型实现函数的调用，这里它没有被作为造型特殊对待。如果你的转换函数没有被指定支持这种习惯，那么你的用户会觉得意外。由于瀚高数据库允许用不同的参数类型重载同一个函数名，因此存在多个从不同类型到同一目标类型的同名转换函数并不困难。

> **注意：**
> 
> 实际上前一段过于简化了：有两种情况中一个函数调用结构在没有被匹配到一个实际函数时将被当作一次造型请求。如果函数调用 `name(x)` 没有正好匹配任何现有函数，但 `name` 是一种数据类型的名称并且 `pg_cast` 提供了一种从 `x` 的类型到这种类型的二进制可强制造型，那么该调用将被翻译为一次二进制可强制造型。通过这种例外，二进制可强制造型能够以函数语法调用，即便没有该函数。同样的，如果没有 `pg_cast` 项，但是该造型是要造型到一种字符串类型或者是要从一种字符串类型造型，调用将被翻译成一次 I/O 转换造型。这种例外允许以函数语法调用 I/O 转换造型。

> **注意：**
> 
> 还有一种例外中的例外：从组合类型到字符串类型的 I/O 转换造型不能使用函数语法调用，而必须被写成显式造型语法（ `CAST` 或者 `::` 记号）。增加这种例外是因为在引入了自动提供的 I/O 转换造型之后，在想要引用一个函数或者列时太容易意外地调用这种造型。

**示例**

要使用函数 `int4(bigint)` 创建一种从类型 `bigint` 到类型 `int4` 的赋值造型：

```sql
CREATE CAST (bigint AS int4) WITH FUNCTION int4(bigint) AS ASSIGNMENT;
```

（在系统中这种造型已经被预定义）。

**兼容性**

`CREATE CAST` 命令符合 SQL 标准，不过 SQL 没有为二进制可强制类型或者实现函数的额外参数做好准备。 `AS IMPLICIT` 也是一种瀚高数据库扩展。

**另见**

`CREATE FUNCTION`,`CREATE TYPE`,`DROP CAST`

## CREATE COLLATION

— 定义一种新排序规则

**大纲**

```sql
CREATE COLLATION [ IF NOT EXISTS ] name (
    [ LOCALE = locale, ]
    [ LC_COLLATE = lc_collate, ]
    [ LC_CTYPE = lc_ctype, ]
    [ PROVIDER = provider, ]
    [ DETERMINISTIC = boolean, ]
    [ VERSION = version ]
)

CREATE COLLATION [ IF NOT EXISTS ] name FROM existing_collation
```

**描述**

`CREATE COLLATION` 使用指定的操作系统区域设置或者复制一个现有的排序规则来定义新的排序规则。

要创建一种排序规则，你必须拥有目标模式上的 `CREATE` 特权。

**参数**

**`IF NOT EXISTS`**

如果已经存在了同名的排序规则，则不要抛出错误。在这种情况下发出一个通知。请注意，不保证已经存在的排序规则与要创建的这个类似。

**`name`**

排序规则的名字，可以被模式限定。如果没有用模式限定，该排序规则会被定义在当前模式中。排序规则名称在其所处的模式中必须唯一（系统目录可以为其他编码包含具有相同名称的排序规则，但数据库编码不匹配时它们会被忽略）。

**`locale`**

这是一种一次设置 `LC_COLLATE` 和 `LC_CTYPE` 的快捷方式。如果你指定它，你就不能指定那两个参数。

**`lc_collate`**

为 `LC_COLLATE` 区域分类使用指定的操作系统区域。

**`lc_ctype`**

为 `LC_CTYPE` 区域分类使用指定的操作系统区域。

**`provider`**

指定用于与此排序规则相关的区域服务的提供程序。可能的值是： `icu` 、 `libc` 。默认是 `libc` 。可用的选择取决于操作系统和构建选项。

**`DETERMINISTIC`**

规定排序是否应使用确定性比较。默认值为 `true` 。确定性比较认为那些在字节上不相等的字符串是不相等的，即使它们在逻辑上被比较认为相等。瀚高数据库使用字节比较来断开连接。不确定的比较可能会使排序规则大小写不敏感或音调不敏感。因此，您需要选择一个适当的 `LC_COLLATE` 设置并且在此处将排序规则设置为不确定。

非确定性排序规则仅被 ICU 提供者支持。

**`version`**

指定使用该排序规则存储的版本字符串。通常忽略该选项，这会导致版本从操作系统提供的排序规则实际版本中计算出来。此选项旨在供 `pg_upgrade` 用于复制现有安装中的版本。

**`existing_collation`**

要复制的一种现有的排序规则的名称。新的排序规则将和现有的具有同样的属性，但是它是一个独立的对象。

**注解**

`CREATE COLLATION` 采用 `SHARE ROW EXCLUSIVE` 锁，在 `pg_collation` 系统分类上，这是自我冲突的，所以一次只能运行一条 `CREATE COLLATION` 命令。

使用 `DROP COLLATION` 可移除用户定义的排序规则。

使用 `libc` 排序规则提供程序时，语言环境必须适用于当前的数据库编码。有关精确的规则，请参见 `CREATE DATABASE` 。

**示例**

从操作系统区域 `fr_FR.utf8` 创建一种排序规则（假定当前数据库编码是 UTF8）：

```sql
CREATE COLLATION french (locale = 'fr_FR.utf8');
```

使用 German phone book 排序顺序使用 ICU 提供程序创建排序规则：

```sql
CREATE COLLATION german_phonebook (provider = icu, locale = 'de-u-co-phonebk');
```

从一个现有的排序规则创建一个新的排序规则：

```sql
CREATE COLLATION german FROM "de_DE";
```

能在应用中使用与操作系统无关的排序规则名称就很方便了。

**兼容性**

在 SQL 标准中有一个 `CREATE COLLATION` 语句，但是它被限制为只能复制一个现有的排序规则。创建新排序规则的语法是一种瀚高数据库扩展。

**另见**

`ALTER COLLATION`,`DROP COLLATION`

## CREATE CONVERSION

— 定义一种新的编码转换

**大纲**

```sql
CREATE [ DEFAULT ] CONVERSION name
    FOR source_encoding TO dest_encoding FROM function_name
```

**描述**

`CREATE CONVERSION` 定义一种字符集编码间新的转换。还有，被标记为 `DEFAULT` 的转换将被自动地用于客户端和服务器之间的编码转换。为了这个目的，必须定义两个转换（从编码 A 到 B 以及从编码 B 到 A）。

要创建一个转换，你必须拥有该函数上的 `EXECUTE` 特权以及目标模式上的 `CREATE` 特权。

**参数**

**`DEFAULT`**

`DEFAULT` 子句表示这个转换是从源编码到目标编码的默认转换。在一个模式中对于每一个编码对，只应该有一个默认转换。

**`name`**

转换的名称，可以被模式限定。如果没有被模式限定，该转换被定义在当前模式中。在一个模式中，转换名称必须唯一。

**`source_encoding`**

源编码名称。

**`dest_encoding`**

目标编码名称。

**`function_name`**

被用来执行转换的函数。函数名可以被模式限定。如果没有，将在路径中查找该函数。

该函数必须具有一下的特征：

```sql
conv_proc(
    integer,   -- 源编码 ID
    integer,   -- 目标编码 ID
    cstring,   -- 源字符串（空值终止的 C 字符串）
    internal,  -- 目标（用一个空值终止的 C 字符串填充）
    integer    -- 源字符串长度
) RETURNS void;
```

**注解**

使用 `DROP CONVERSION` 可以移除用户定义的转换。

创建转换所要求的特权可能在未来的发行中被更改。

**示例**

使用 `myfunc` 创建一个从编码 `UTF8` 到 `LATIN1` 的转换：

```sql
CREATE CONVERSION myconv FOR 'UTF8' TO 'LATIN1' FROM myfunc;
```

**兼容性**

`CREATE CONVERSION` 是一种瀚高数据库扩展。在 SQL 标准中没有 `CREATE CONVERSION` 语句，但是有一个目的和语法都类似的 `CREATE TRANSLATION` 语句。

**另见**

`ALTER CONVERSION`,`CREATE FUNCTION`,`DROP CONVERSION`

## CREATE DATABASE

— 创建一个新数据库

**大纲**

```sql
CREATE DATABASE name
    [ [ WITH ] [ OWNER [=] user_name ]
           [ TEMPLATE [=] template ]
           [ ENCODING [=] encoding ]
           [ LC_COLLATE [=] lc_collate ]
           [ LC_CTYPE [=] lc_ctype ]
           [ TABLESPACE [=] tablespace_name ]
           [ ALLOW_CONNECTIONS [=] allowconn ]
           [ CONNECTION LIMIT [=] connlimit ]
           [ IS_TEMPLATE [=] istemplate ] ]
```

**描述**

`CREATE DATABASE` 创建一个新的瀚高数据库数据库。

要创建一个数据库，你必须是一个超级用户或者具有特殊的 `CREATEDB` 特权。见 `CREATE ROLE` 。

默认情况下，新数据库将通过克隆标准系统数据库 `template1` 被创建。可以通过写 `TEMPLATE name` 指定一个不同的模板。特别地，通过写 `TEMPLATE template0` 你可以创建一个干净的数据库，它将只包含你的瀚高数据库版本所预定义的标准对象。如果你希望避免拷贝任何可能被加入到 `template1` 中的本地安装对象，这将有所帮助。

**参数**

**`name`**

要创建的数据库名。

**`user_name`**

将拥有新数据库的用户的角色名，或者用 `DEFAULT` 来使用默认值（即，执行该命令的用户）。要创建一个被另一个角色拥有的数据库，你必须是该角色的一个直接或间接成员，或者是一个超级用户。

**`template`**

要从其创建新数据库的模板名称，或者用 `DEFAULT` 来使用默认模板（ `template1` ）。

**`encoding`**

要在新数据库中使用的字符集编码。指定一个字符串常量（例如 `'SQL_ASCII'` ），或者一个整数编码编号，或者 `DEFAULT` 来使用默认的编码（即，模板数据库的编码）。

**`lc_collate`**

要在新数据库中使用的排序规则顺序（ `LC_COLLATE` ）。这会影响应用到字符串的排序顺序，例如在带 `ORDER BY` 的查询中，以及文本列上索引所使用的顺序。默认是使用模板数据库的排序规则顺序。附加限制见下文。

**`lc_ctype`**

要在新数据库中使用的字符分类（ `LC_CTYPE` ）。这会影响字符的类别，如小写、大写和数字。默认是使用模板数据库的字符分类。附加限制见下文。

**`tablespace_name`**

将与新数据库相关联的表空间名称，或者 `DEFAULT` 来使用模板数据库的表空间。这个表空间将是在这个数据库中创建的对象的表空间。详见 `CREATE TABLESPACE` 。

**`allowconn`**

如果为假，则没有人能连接到这个数据库。默认为真，表示允许连接（除了被其他机制约束以外，例如 `GRANT/REVOKE CONNECT` ）。

**`connlimit`**

这个数据库允许多少并发连接。 `-1` （默认值）表示没有限制。

**`istemplate`**

如果为真，则任何具有 `CREATEDB` 特权的用户都可以从这个数据库克隆。如果为假（默认），则只有超级用户或者该数据库的拥有者可以克隆它。

可选的参数可以被写成任何顺序，不用按照上面说明的顺序。

**注解**

`CREATE DATABASE` 不能在一个事务块内被执行。

带有一行”不能初始化数据库目录”的错误大部分与在数据目录上权限不足、磁盘满或其他文件系统问题有关。

使用 `DROP DATABASE` 移除一个数据库。

程序 `createdb` 是这个命令的一个包装器程序，为了使用方便而提供。

不会从模板数据库中复制数据库层面的配置参数（通过 `ALTER DATABASE` 设置）。

尽管可以通过指定一个数据库作为模板来从其中而不是 `template1` 复制，这（还）不是”COPY DATABASE”功能的一般目的。主要的限制是在模板数据库被拷贝期间其他会话不能连接到它。如果 `CREATE DATABASE` 启动时还存在任何其他连接，它将失败。否则，到模板数据库的新连接将被挡在外面直到 `CREATE DATABASE` 完成。

为新数据库指定的字符集编码必须与选定的区域设置（ `LC_COLLATE` 和 `LC_CTYPE` ）相兼容。如果区域是 `C` （或者等效的 `POSIX` ），那么所有编码都被允许，但是对于其他区域设置只有一种编码能正确工作（不过，在 Windows 上 UTF-8 编码能够与任何区域一起使用）。 `CREATE DATABASE` 将允许超级用户指定 `SQL_ASCII` 编码而不管区域设置，但是这种选择已被废弃并且可能在数据与数据库中存储的区域不是编码兼容时让字符串函数行为失当。

编码和区域设置必须匹配模板数据的编码和区域，除非 `template0` 被用作模板。这是因为其他数据库可能包含不匹配指定编码的数据，或者可能包含排序顺序受 `LC_COLLATE` 和 `LC_CTYPE` 影响的索引。拷贝这种数据将导致一个由于该新设置损坏的数据库。不过， `template0` 是不会含有任何可能被影响的数据或索引的。

`CONNECTION LIMIT` 选项大概是唯一会被强制的，如果两个新会话在大约同一时间开始并且那时该数据库只剩有一个连接”槽”，可能两者都会失败。还有，该限制对超级用户或后台工作进程无效。

**示例**

要创建一个新数据库：

```sql
CREATE DATABASE lusiadas;
```

要在一个默认表空间 `salesspace` 中创建一个被用户 `salesapp` 拥有的新数据库 `sales` ：

```sql
CREATE DATABASE sales OWNER salesapp TABLESPACE salesspace;
```

要用不同的语言环境创建数据库 `music` ：

```sql
CREATE DATABASE music
    LC_COLLATE 'sv_SE.utf8' LC_CTYPE 'sv_SE.utf8'
    TEMPLATE template0;
```

在这个例子中，如果指定的语言环境与 `template1` 中的语言环境不同，则需要 `TEMPLATE template0` 子句。（如果不是，则明确指定区域设置是多余的。）

要用不同的语言环境和不同的字符集编码创建数据库 `music2` ：

```sql
CREATE DATABASE music2
    LC_COLLATE 'sv_SE.iso885915' LC_CTYPE 'sv_SE.iso885915'
    ENCODING LATIN9
    TEMPLATE template0;
```

指定的区域设置和编码设置必须匹配，否则会报告错误。

请注意，区域名称是特定于操作系统的，因此上述命令可能无法在任何地方以相同的方式工作。

**兼容性**

在 SQL 标准中没有 `CREATE DATABASE` 语句。数据库等效于目录，而目录的创建由实现定义。

**参见**

`ALTER DATABASE`,`DROP DATABASE`

## CREATE DOMAIN

— 定义一个新的域

**大纲**

```sql
CREATE DOMAIN name [ AS ] data_type
    [ COLLATE collation ]
    [ DEFAULT expression ]
    [ constraint [ ... ] ]

其中 constraint 是：

[ CONSTRAINT constraint_name ]
{ NOT NULL | NULL | CHECK (expression) }
```

**描述**

`CREATE DOMAIN` 创建一个新的域。域本质上是一种带有可选约束（在允许的值集合上的限制）的数据类型。定义一个域的用户将成为它的拥有者。

如果给定一个模式名（例如 `CREATE DOMAIN myschema.mydomain ...`），那么域将被创建在该指定的模式中。否则它会被创建在当前模式中。域的名称在其模式中的类型和域之间必须保持唯一。

域主要被用于把字段上的常用约束抽象到一个单一的位置以便维护。例如，几个表可能都包含电子邮件地址列，而且都要求相同的 `CHECK` 约束来验证地址的语法。可以为此定义一个域，而不是在每个表上都单独设置一个约束。

要创建一个域，你必须在其底层类型上拥有 `USAGE` 特权。

**参数**

**`name`**

要被创建的域的名称（可以被模式限定）。

**`data_type`**

域的底层数据类型。可以包括数组指示符。

**`collation`**

用于该域的可选的排序规则。如果没有指定排序规则，将使用底层数据类型的默认排序规则。如果指定了 `COLLATE` ，底层类型必须是可排序的。

**`DEFAULT expression`**

`DEFAULT` 子句为该域数据类型的列指定一个默认值。该值是任何没有变量的表达式（但不允许子查询）。默认值表达式的数据类型必须匹配域的数据类型。如果没有指定默认值，那么默认值就是空值。

默认值表达式将被用在任何没有指定列值的插入操作中。如果为一个特定列定义了默认值，它会覆盖与域相关的默认值。继而，域默认值会覆盖任何与底层数据类型相关的默认值。

**`CONSTRAINT constraint_name`**

一个约束的名称（可选）。如果没有指定，系统会生成一个名称。

**`NOT NULL`**

这个域的值通常不能为空值（但是看看下面的注释）。

**`NULL`**

这个域的值允许为空值。这是默认值。

这个子句只是为了与非标准 SQL 数据库相兼容而设计。在新的应用中不鼓励使用它。

**`CHECK (expression)`**

`CHECK` 子句指定该域的值必须满足的完整性约束或者测试。每一个约束必须是一个产生布尔结果的表达式。它应该使用关键词 `VALUE` 来引用要被测试的值。计算为 `TRUE` 或者 `UNKNOWN` 的表达式成功。如果该表达式产生一个 `FALSE` 结果，会报告一个错误并且该值不允许被转换成该域类型。

当前， `CHECK` 表达式不能包含子查询，也不能引用除 `VALUE` 之外的其他变量。

当一个域有多个 `CHECK` 约束，将按照其名字的字母顺序测试它们（版本 9.5 之前的瀚高数据库不遵循任何用于 `CHECK` 约束的特定触发顺序）。

**注解**

在把一个值转换成域类型时会检查域约束（特别是 `NOT NULL` ）。即使有一个这样的约束，有可能一个名义上属于该域类型的列也会被读成空值。例如，如果在一次外连接查询中，属于该域的列出现在外连接的空值端。下面是一个更精细的例子：

```sql
INSERT INTO tab (domcol) VALUES ((SELECT domcol FROM tab WHERE false));
```

空的标量子-SELECT 将产生一个空值，它被认为是该域类型的值，因此不会在其上应用任何进一步的约束检查，并且插入将会成功。

要避免这类问题很难，因为 SQL 的一般假设是空值也是每一种数据类型的合法值。因此，最好的方法是设计一个允许空值的域约束，然后根据需要在该域类型的列上应用列的 `NOT NULL` 约束。

瀚高数据库假定 `CHECK` 约束的条件是不可变的，也就是说，对于相同的输入值它们总会给出相同的结果。仅在首次将值转换为域类型时，此假设检查 `CHECK` 约束的正确性，而不是在其他时候。

打破此假设的常见方法的一个示例是在 `CHECK` 表达式中引用一个用户定义的函数，然后更改该函数的行为。瀚高数据库不会禁止这样做，但是此间如果有域类型的存储值违反 `CHECK` 约束，它也不会注意到。这将导致后续数据库转储和重新加载失败。处理此类更改的建议方法是删除约束（使用 `ALTER DOMAIN` ），调整函数定义，重新添加约束，然后根据存储的数据重新检查约束。

**示例**

这个例子创建 `us_postal_code` 数据类型并且把它用在一个表定义中。一个正则表达式测试被用来验证值是否看起来像一个合法的 US 邮政编码：

```sql
CREATE DOMAIN us_postal_code AS TEXT
CHECK(
   VALUE ~ '^\d{5}$'
OR VALUE ~ '^\d{5}-\d{4}$'
);

CREATE TABLE us_snail_addy (
  address_id SERIAL PRIMARY KEY,
  street1 TEXT NOT NULL,
  street2 TEXT,
  street3 TEXT,
  city TEXT NOT NULL,
  postal us_postal_code NOT NULL
);
```

**兼容性**

命令 `CREATE DOMAIN` 符合 SQL 标准。

**另见**

`ALTER DOMAIN` ， `DROP DOMAIN`

## CREATE EVENT TRIGGER

— 定义一个新的事件触发器

**大纲**

```sql
CREATE EVENT TRIGGER name
    ON event
    [ WHEN filter_variable IN (filter_value [, ... ]) [ AND ... ] ]
    EXECUTE { FUNCTION | PROCEDURE } function_name()
```

**描述**

`CREATE EVENT TRIGGER` 创建一个新的事件触发器。只要指定的事件发生并且与该触发器相关的 `WHEN` 条件（如果有）被满足，该触发器的函数将被执行。

**参数**

**`name`**

给新触发器的名称。在该数据库中这个名称必须唯一。

**`event`**

会触发对给定函数调用的事件名称。

**`filter_variable`**

用来过滤事件的变量名称。这可以用来限制触发器只为它支持的那一部分情况引发。当前唯一支持的 `filter_variable` 是 `TAG` 。

**`filter_value`**

与该触发器要为其引发的 `filter_variable` 相关联的一个值列表。对于 `TAG` ，这表示一个命令标签列表（例如 `'DROP FUNCTION'` ）。

**`function_name`**

一个用户提供的函数，它被声明为没有参数并且返回类型 `event_trigger` 。

在 `CREATE EVENT TRIGGER` 的语法中，关键字 `FUNCTION` 和 `PROCEDURE` 是等效的，但是被引用的函数在任何情况下都必须是函数，而不是过程。此处关键字 `PROCEDURE` 的使用是历史性的，已弃用。

**注解**

只有超级用户能创建事件触发器。

在单用户模式（见 `postgres` ）中事件触发器被禁用。如果一个错误的事件触发器禁用了数据库让你甚至无法删除它，可以重启到单用户模式，这样你就能删除它。

**示例**

禁止执行任何 DDL 命令：

```sql
CREATE OR REPLACE FUNCTION abort_any_command()
  RETURNS event_trigger
  LANGUAGE plpgsql
AS $$
BEGIN
  RAISE EXCEPTION 'command % is disabled', tg_tag;
END;
$$;

CREATE EVENT TRIGGER abort_ddl ON ddl_command_start
  EXECUTE FUNCTION abort_any_command();
```

**兼容性**

在 SQL 标准中没有 `CREATE EVENT TRIGGER` 语句。

**另见**

`ALTER EVENT TRIGGER` ， `DROP EVENT TRIGGER` ， `CREATE FUNCTION`

## CREATE EXTENSION

— 安装一个扩展

**大纲**

```sql
CREATE EXTENSION [ IF NOT EXISTS ] extension_name
    [ WITH ] [ SCHEMA schema_name ]
             [ VERSION version ]
             [ FROM old_version ]
             [ CASCADE ]
```

**描述**

`CREATE EXTENSION` 把一个新的扩展载入到当前数据库中。不能有同名扩展已经被载入。

载入一个扩展本质上是运行该扩展的脚本文件。该脚本通常将创建新的 SQL 对象，例如函数、数据类型、操作符以及索引支持方法。 `CREATE EXTENSION` 会额外地记录所有被创建对象的标识，这样发出 `DROP EXTENSION` 时可以删除它们。

载入一个扩展要求创建其组件对象所要求的特权。对于大部分扩展这意味这需要超级用户或者数据库拥有者的特权。为了以后特权检察的目的，运行 `CREATE EXTENSION` 的用户会成为该扩展的拥有者以及由该扩展的脚本创建的任何对象的拥有者。

**参数**

**`IF NOT EXISTS`**

已有同名扩展存在时不要抛出错误。这种情况下会发出一个提示。注意，不保证现有的扩展与将要从当前可用的脚本文件创建的脚本有任何相似。

**`extension_name`**

要安装的扩展的名称。瀚高数据库将使用文件 `SHAREDIR/extension/extension_name.control` 中的指令来创建该扩展。

**`schema_name`**

假定该扩展允许其内容被重定位，这是要在其中安装该扩展的对象的模式名称。被提到的模式必须已经存在。如果没有指定并且该扩展的控制文件也没有指定一个模式，将使用当前的默认对象创建模式。

如果该扩展在其控制文件中指定了一个 `schema` 参数，那么不能用 `SCHEMA` 子句覆盖该模式。通常，如果给出了一个 `SCHEMA` 子句并且它与扩展的 `schema` 参数冲突，则会发生错误。不过，如果也给出了 `CASCADE` 子句，则 `schema` 冲突时会忽略 `schema_name` 。给定的 `schema_name` 将被用来安装任何需要的并且没有在其控制文件中指定 `schema` 的扩展。

记住扩展本身被认为不在任何模式中：扩展具有无限定的名称，并且要在整个数据库范围内唯一。但是属于扩展的对象可以在模式中。

**`version`**

要安装的扩展的版本。这可以写成一个标识符或者一个字符串。默认版本在该扩展的控制文件中指定。

**`old_version`**

当且仅当尝试要安装一个扩展来替代一个”老式”的模块（它只是一组没有被打包成扩展的对象的集合）时，才必须指定 `FROM old_version` 。这个选项导致 `CREATE EXTENSION` 运行另一个安装脚本把现有的对象吸收到该扩展中，而不是创建新对象。当心 `SCHEMA` 指定的是包含已经存在对象的模式。

用于 `old_version` 的值由扩展的作者决定，且如果有多于一种版本的老式模块可以被升级到扩展，该值还可能变化。

**`CASCADE`**

自动安装这个扩展所依赖的任何还未安装的扩展。它们的依赖也会同样被自动安装。如果给出 `SCHEMA` 子句，它会应用于这种方式下安装的所有扩展。这个语句的其他选项不会被应用于自动安装的扩展。特别地，这些自动安装的扩展的默认版本将被选中。

**注解**

在使用 `CREATE EXTENSION` 载入扩展到数据库中之前，必须先安装好该扩展的支持文件。关于安装瀚高数据库提供的扩展的信息可以在额外提供的模块中找到。

当前可以用于载入的扩展可以在系统视图 `pg_available_extensions` 或者 `pg_available_extension_versions` 中看到。

**示例**

安装 `hstore` 扩展到当前数据库中：

```sql
CREATE EXTENSION hstore;
```

要小心地指定安装现有 `hstore` 对象的模式。

**兼容性**

`CREATE EXTENSION` 是一种瀚高数据库扩展。

**另见**

`ALTER EXTENSION` ， `DROP EXTENSION`

## CREATE FOREIGN DATA WRAPPER

— 定义一个新的外部数据包装器

**大纲**

```sql
CREATE FOREIGN DATA WRAPPER name
    [ HANDLER handler_function | NO HANDLER ]
    [ VALIDATOR validator_function | NO VALIDATOR ]
    [ OPTIONS ( option 'value' [, ... ] ) ]
```

**描述**

`CREATE FOREIGN DATA WRAPPER` 创建一个新的外部数据包装器。定义外部数据包装器的用户将成为它的拥有者。

在数据库内外部数据包装器名称必须唯一。

只有超级用户能够创建外部数据包装器。

**参数**

**`name`**

要创建的外部数据包装器的名称。

**`HANDLER handler_function`**

`handler_function` 是一个以前注册好的函数的名称，它将被调用来为外部表检索执行函数。处理器函数必须不能有参数，并且它的返回类型必须是 `fdw_handler` 。

可以创建一个没有处理器函数的外部数据包装器，但是使用这个包装器的外部表只能被声明，但不能被访问。

**`VALIDATOR validator_function`**

`validator_function` 是一个之前已注册的函数的名称，它将被调用来检查给予该外部数据包装器的选项，还有用于外部服务器、用户映射以及使用该外部数据包装器的外部表的选项。如果没有验证器函数或者指定了 `NO VALIDATOR` ，那么在创建时不会检查选项（外部数据包装器可能会在运行时忽略或者拒绝无效的选项说明，这取决于实现）。

验证器函数必须接受两个参数：一个类型是 `text[]` ，它将包含存储在系统目录中的选项数组，另一个是类型 `oid` ，它将是包含该选项的系统目录的 OID。返回类型会被忽略，该函数应该使用 `ereport(ERROR)` 函数报告无效选项。

**`OPTIONS ( option 'value' [, ... ] )`**

这个子句为新的外部数据包装器指定选项。允许的选项名称和值与每一个外部数据包装器有关，并且它们会被该外部数据包装器的验证器函数验证。选项名称必须唯一。

**注解**

瀚高数据库的外部数据功能仍在积极的开发中。查询的优化还很原始（也是剩下工作最多的部分）。因此，未来还有很可观的性能提升空间。

**示例**

创建一个无用的外部数据包装器 `dummy` ：

```sql
CREATE FOREIGN DATA WRAPPER dummy;
```

用处理器函数 `file_fdw_handler` 创建一个外部数据包装器 `file` ：

```sql
CREATE FOREIGN DATA WRAPPER file HANDLER file_fdw_handler;
```

用一些选项创建一个外部数据包装器 `mywrapper` ：

```sql
CREATE FOREIGN DATA WRAPPER mywrapper OPTIONS (debug 'true');
```

**兼容性**

`CREATE FOREIGN DATA WRAPPER` 符合 ISO/IEC 9075-9 (SQL/MED)，不过 `HANDLER` 和 `VALIDATOR` 子句是扩展，并且标准子句 `LIBRARY` 和 `LANGUAGE` 还没有在瀚高数据库中被实现。

不过要注意，整体上来说 SQL/MED 功能还没有符合。

**另见**

`ALTER FOREIGN DATA WRAPPER` ， `DROP FOREIGN DATA WRAPPER` ， `CREATE SERVER` ， `CREATE USER MAPPING` ， `CREATE FOREIGN TABLE`

## CREATE FOREIGN TABLE

— 定义一个新的外部表

**大纲**

```sql
CREATE FOREIGN TABLE [ IF NOT EXISTS ] table_name ( [
  { 
    column_name data_type [ OPTIONS ( option 'value' [, ... ] ) ]
    [ COLLATE collation ] [ column_constraint [ ... ] ]
    | table_constraint 
  }
  [, ... ]
] )
[ INHERITS ( parent_table [, ... ] ) ]
SERVER server_name
[ OPTIONS ( option 'value' [, ... ] ) ]

CREATE FOREIGN TABLE [ IF NOT EXISTS ] table_name
  PARTITION OF parent_table [ (
  {
    column_name [ WITH OPTIONS ] [ column_constraint [ ... ] ]
    | table_constraint
  }
  [, ... ]
) ] partition_bound_spec
SERVER server_name
[ OPTIONS ( option 'value' [, ... ] ) ]
```

其中 column\_constraint 是：

```
[ CONSTRAINT constraint_name ]
{ 
  NOT NULL |
  NULL |
  CHECK ( expression ) [ NO INHERIT ] |
  DEFAULT default_expr |
  GENERATED ALWAYS AS ( generation_expr ) STORED 
}
```

而 table\_constraint 是：

```
[ CONSTRAINT constraint_name ]
CHECK ( expression ) [ NO INHERIT ]
```

**描述**

`CREATE FOREIGN TABLE` 在当前数据库中创建一个新的外部表。该表将由发出这个命令的用户所拥有。

如果给定了一个模式名称（例如 `CREATE FOREIGN TABLE myschema.mytable ...`），那么该表会被创建在指定的模式中。否则它会被创建在当前模式中。该外部表的名称必须与同一个模式中的任何其他外部表、表、序列、索引、视图或者物化视图区分开来。

`CREATE FOREIGN TABLE` 还将自动创建一个数据类型来表示该外部表行相应的组合类型。因此，外部表不能和同一个模式中任何现有的数据类型同名。

如果指定了 `PARTITION OF` 子句，则该表被创建为具有指定边界的 `parent_table` 的分区。

要创建一个外部表，你必须具有该外部服务器上的 `USAGE` 特权，以及该表中用到的所有列类型上的 `USAGE` 特权。

**参数**

**`IF NOT EXISTS`**

已经存在同名关系时不要抛出错误。这种情况下会发出一个提示。注意，并不保证已经存在的关系与将要创建的那一个相似。

**`table_name`**

要创建的表的名称（可以被模式限定）。

**`column_name`**

要在新表中创建的列名。

**`data_type`**

该列的数据类型。可以包括数组指示符。

**`COLLATE collation`**

`COLLATE` 子句为该列（必须是一个可排序的数据类型）赋予一个排序规则。如果没有指定，则会使用该列的数据类型的默认排序规则。

**`INHERITS ( parent_table [, ... ] )`**

可选的 `INHERITS` 子句指定了一个表的列表，新的外部表会自动从中继承所有列。父表可以是普通表或者外部表。详见 `CREATE TABLE` 的类似形式。

**`PARTITION OF parent_table FOR VALUES partition_bound_spec`**

此语句可以用来将外部表创建为父表的一个指定区间的分区表。详见 `CREATE TABLE` 的类似形式。注意如果父表存在 `UNIQUE` 类型的索引时，当前是不允许将外部表创建为该父表的分区表。（另见 `ALTER TABLE ATTACH PARTITION` 。）

**`CONSTRAINT constraint_name`**

一个可选的用于列或者表约束的名字。如果该约束被违背，这个约束名字会出现在错误消息中，这样 `col must be positive` 这种约束名就可以被用来与客户端应用交流有用的约束信息（指定包含空格的约束名需要使用双引号）。如果没有指定约束名，系统会自动生成一个。

**`NOT NULL`**

该列不允许包含空值。

**`NULL`**

该列可以包含空值，这是默认值。

提供这个子句只是为了兼容非标准的 SQL 数据库。在新的应用中不鼓励使用它。

**`CHECK ( expression ) [ NO INHERIT ]`**

`CHECK` 子句指定一个产生布尔结果的表达式，该外部表中的每一行都应该满足该表达式。也就是说，对于该外部表中所有的行，这个表达式应该产生 `TRUE` 或者 `UNKNOWN` 而不能产生 `FALSE` 。被作为列约束指定的检查约束应该只引用该列的值，而出现在表约束中的表达式可以引用多列。

当前， `CHECK` 表达式不能包含子查询，也不能引用除当前行的列之外的其他变量。可以引用系统列 `tableoid` ，但是不能引用其他系统列。

被标记为 `NO INHERIT` 的约束将不会传播到子表上。

**`DEFAULT default_expr`**

`DEFAULT` 子句为包含它的列定义赋予一个默认数据值。该值是任意不包含变量的表达式（不允许子查询和对当前表中其他列的交叉引用）。默认值表达式的数据类型必须匹配列的数据类型。

默认值表达式将被用在任何没有指定列值的插入操作中。如果一列没有默认值，则默认值为空值。

**`GENERATED ALWAYS AS ( generation_expr ) STORED`**

该子句创建一个生成列。此列不能写入，只能在读取时返回所指定的表达式的值。

关键字 `STORED` 是必须的，用来表明该列将在写入时计算。（计算出的值将会传递给外部数据封装器负责保存，并在读取时返回。）

生成表达式可以引用表中的其他列，但不能引用其他的生成列。所使用的函数和操作符必须是不可变。不能引用其他表。

**`server_name`**

要用于该外部表的一个现有外部服务器的名称。有关定义一个服务器的细节可以参考 `CREATE SERVER` 。

**`OPTIONS ( option 'value' [, ...] )`**

要与新外部表或者它的一个列相关联的选项。被允许的选项名称和值是与每一个外部数据包装器相关的，并且它们会被该外部数据包装器的验证器函数验证。不允许重复的选项名称（不过一个表选项和一个列选项重名是可以的）。

**注解**

瀚高数据库核心系统不会强制外部表上的约束（例如 `CHECK` 或 `NOT NULL` 子句），大部分外部数据包装器也不会尝试强制它们。也就是说，这类约束会被简单地认为保持为真。这种强制其实没什么意义，因为它只适用于通过该外部表插入或者更新的行，而对通过其他方式修改的行（例如直接在远程服务器上修改）没有作用。附着在外部表上的约束应该表示由外部服务器强制的一个约束。

有些特殊目的的外部数据包装器可能是它们所访问的数据的唯一一种访问机制，在那种情况下让外部数据包装器自己来执行约束强制可能是合适的。但是不应该假设包装器会这样做，除非它的文档说它会。

尽管瀚高数据库不会尝试强制外部表上的约束，但它确实假定它们对于查询优化的目的是正确的。如果在外部表中有不满足约束的行可见，在该表上的查询可能会产生不正确的回答。确保约束定义符合实际是用户的责任。

类似的要点也适用于生成列。生成列在本地瀚高数据库服务器发生插入或更新时进行计算，并将计算结果传递给外部数据封装器，由外部数据封装器负责把结果写到外部数据存储中，但是并不强制要求查询外部表时返回的生成列的值一定是与生成表达式一致。总而言之，此行为可能导致查询到不正确的结果。

虽然列可以从本地分区移到外部表分区（使用的外部数据封装器支持元组路由），但是不能将列从外部表分区移动到本地分区。

**示例**

创建外部表 `films` ，通过服务器 `film_server` 访问它：

```sql
CREATE FOREIGN TABLE films (
    code        char(5) NOT NULL,
    title       varchar(40) NOT NULL,
    did         integer NOT NULL,
    date_prod   date,
    kind        varchar(10),
    len         interval hour to minute
)
SERVER film_server;
```

创建外部表 `measurement_y2016m07` ，通过服务器 `server_07` 访问它，作为范围分区表 `measurement` 的分区：

```sql
CREATE FOREIGN TABLE measurement_y2016m07
    PARTITION OF measurement FOR VALUES FROM ('2016-07-01') TO ('2016-08-01')
    SERVER server_07;
```

**兼容性**

`CREATE FOREIGN TABLE` 命令大部分符合 SQL 标准。不过，与 `CREATE TABLE` 很相似，它允许 `NULL` 约束以及零列外部表。能够指定列默认值也是一种瀚高数据库扩展。瀚高数据库定义的表继承形式是非标准的。

**另见**

`ALTER FOREIGN TABLE` ， `DROP FOREIGN TABLE` ， `CREATE TABLE` ， `CREATE SERVER` ， `IMPORT FOREIGN SCHEMA`

## CREATE FUNCTION

— 定义一个新函数

**大纲**

```sql
CREATE [ OR REPLACE ] FUNCTION
    name ( [ [ argmode ] [ argname ] argtype [ { DEFAULT | = } default_expr ] [, ...] ] )
    [ RETURNS rettype
      | RETURNS TABLE ( column_name column_type [, ...] ) ]
    { LANGUAGE lang_name
      | TRANSFORM { FOR TYPE type_name } [, ... ]
      | WINDOW
      | IMMUTABLE | STABLE | VOLATILE | [ NOT ] LEAKPROOF
      | CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT
      | [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
      | PARALLEL { UNSAFE | RESTRICTED | SAFE }
      | COST execution_cost
      | ROWS result_rows
      | SUPPORT support_function
      | SET configuration_parameter { TO value | = value | FROM CURRENT }
      | AS 'definition'
      | AS 'obj_file', 'link_symbol'
    } ...
```

**描述**

`CREATE FUNCTION` 定义一个新函数。 `CREATE OR REPLACE FUNCTION` 将创建一个新函数或者替换一个现有的函数。要定义一个函数，用户必须具有该语言上的 `USAGE` 特权。

如果包括了一个模式名，那么该函数会被创建在指定的模式中。否则，它会被创建在当前模式中。新函数的名称不能匹配同一个模式中具有相同输入参数类型的任何现有函数或过程。

不过，不同参数类型的函数和过程能够共享一个名字（这被称作 **重载** ）。

要替换一个现有函数的当前定义，可以使用 `CREATE OR REPLACE FUNCTION` 。但不能用这种方式更改函数的名称或者参数类型（如果尝试这样做，实际上就会创建一个新的不同的函数）。还有， `CREATE OR REPLACE FUNCTION` 将不会让你更改一个现有函数的返回类型。要这样做，你必须先删除再重建该函数（在使用 `OUT` 参数时，这意味着除了删除函数之外无法更改任何 `OUT` 参数的类型）。

当 `CREATE OR REPLACE FUNCTION` 被用来替换一个现有的函数，该函数的拥有权和权限不会改变。所有其他的函数属性会按照该命令中所指定的或者隐含的来赋值。必须拥有（包括成为拥有角色的成员）该函数才能替换它。

如果你删除并且重建一个函数，新函数将和旧的不一样，你将必须删掉引用旧函数的现有规则、视图、触发器等。使用 `CREATE OR REPLACE FUNCTION` 更改一个函数定义不会破坏引用该函数的对象。还有， `ALTER FUNCTION` 可以被用来更改一个现有函数的大部分辅助属性。

创建该函数的用户将成为该函数的拥有者。

要创建一个函数，你必须拥有参数类型和返回类型上的 `USAGE` 特权。

**参数**

**`name`**

要创建的函数的名称（可以被模式限定）。

**`argmode`**

一个参数的模式： `IN` 、 `OUT` 、 `INOUT` 或者 `VARIADIC` 。如果省略，默认为 `IN` 。只有 `OUT` 参数能跟在一个 `VARIADIC` 参数后面。还有， `OUT` 和 `INOUT` 参数不能和 `RETURNS TABLE` 符号一起使用。

**`argname`**

一个参数的名称。一些语言（包括 SQL 和 PL/pgSQL）让你在函数体中使用该名称。对于其他语言，一个输入参数的名字只是额外的文字（就该函数本身所关心的来说）。但是你可以在调用一个函数时使用输入参数名来提高可读性。在任何情况下，输出参数的名称是有意义的，因为它定义了结果行类型中的列名（如果忽略一个输出参数的名称，系统将选择一个默认的列名）。

**`argtype`**

该函数参数（如果有）的数据类型（可以是模式限定的）。参数类型可以是基本类型、组合类型或者域类型，或者可以引用一个表列的类型。

根据实现语言，也可以允许指定 `cstring` 之类的”伪类型”。伪类型表示实际参数类型没有被完整指定或者不属于普通 SQL 数据类型集合。

可以写 `table_name.column_name%TYPE` 来引用一列的类型。使用这种特性有时可以帮助创建一个不受表定义更改影响的函数。

**`default_expr`**

如果参数没有被指定值时要用作默认值的表达式。该表达式必须能被强制为该参数的参数类型。只有输入（包括 `INOUT` ）参数可以具有默认值。所有跟随在一个具有默认值的参数之后的输入参数也必须有默认值。

**`rettype`**

返回数据类型（可能被模式限定）。返回类型可以是一种基本类型、组合类型或者域类型，也可以引用一个表列的类型。根据实现语言，也可以允许指定 `cstring` 之类的”伪类型”。如果该函数不会返回一个值，可以指定返回类型为 `void` 。

当有 `OUT` 或者 `INOUT` 参数时，可以省略 `RETURNS` 子句。如果存在，该子句必须和输出参数所表示的结果类型一致：如果有多个输出参数，则为 `RECORD` ，否则与单个输出参数的类型相同。

`SETOF` 修饰符表示该函数将返回一个项的集合而不是一个单一项。

可以写 `table_name.column_name%TYPE` 来引用一列的类型。

**`column_name`**

`RETURNS TABLE` 语法中一个输出列的名称。这实际上是另一种声明 `OUT` 参数的方法，不过 `RETURNS TABLE` 也隐含了 `RETURNS SETOF` 。

**`column_type`**

`RETURNS TABLE` 语法中的输出列的数据类型。

**`lang_name`**

用以实现该函数的语言的名称。可以是 `sql` 、 `c` 、 `internal` 或者一个用户定义的过程语言的名称，例如 `plpgsql` 。不推荐用单引号包围该名称，并且要求区分大小写。

**`TRANSFORM { FOR TYPE type_name } [, ... ]`**

一个由转换构成的列表，对该函数的调用适用于它们。转换在 SQL 类型和语言相关的数据类型之间进行变换，详见 `CREATE TRANSFORM` 。过程语言实现通常把有关内建类型的知识硬编码在代码中，因此那些不需要列举在这里。如果一种过程语言实现不知道如何处理一种类型并且没有转换被提供，它将回退到一种默认的行为来转换数据类型，但是这取决于具体实现。

**`WINDOW`**

`WINDOW` 表示该函数是一个窗口函数而不是一个普通函数。当前只用于用 C 编写的函数。

在替换一个现有函数定义时，不能更改 `WINDOW` 属性。

**`IMMUTABLE`**

**`STABLE`**

**`VOLATILE`**

这些属性告知查询优化器该函数的行为。最多只能指定其中一个。如果这些都不出现，则会默认为 `VOLATILE` 。

- `IMMUTABLE` 表示该函数不能修改数据库并且对于给定的参数值总是会返回相同的值。也就是说，它不会做数据库查找或者使用没有在其参数列表中直接出现的信息。如果给定合格选项，任何用全常量参数对该函数的额调用可以立刻用该函数值替换。
- `STABLE` 表示该函数不能修改数据库，并且对于相同的参数值，它在一次表扫描中将返回相同的结果。但是这种结果在不同的 SQL 语句执行期间可能会变化。对于那些结果依赖于数据库查找、参数变量（例如当前时区）等的函数来说，这是合适的（对希望查询被当前命令修改的行的 `AFTER` 触发器不适合）。还要注意 `current_timestamp` 函数族适合被标记为稳定，因为它们的值在一个事务内不会改变。
- `VOLATILE` 表示该函数的值在一次表扫描中都有可能改变，因此不能做优化。在这种意义上，相对较少的数据库函数是不稳定的，一些例子是 `random()` 、 `currval()` 、 `timeofday()` 。但是注意任何有副作用的函数都必须被分类为不稳定的，即便其结果是可以预测的，这是为了调用被优化掉。一个例子是 `setval()` 。

**`LEAKPROOF`**

`LEAKPROOF` 表示该函数没有副作用。它不会泄露有关其参数的信息（除了通过返回值）。

例如，一个只对某些参数值抛出错误消息而对另外一些却不抛出错误的函数不是防泄漏的，一个把参数值包括在任何错误消息中的函数也不是防泄漏的。这会影响系统如何执行在使用 `security_barrier` 选项创建的视图或者开启了行级安全性的表上执行查询。对于包含有非防泄漏函数的查询，系统将在任何来自查询本身的用户提供条件之前强制来自安全策略或者安全屏障的条件，防止无意中的数据暴露。被标记为防泄漏的函数和操作符被假定是可信的，并且可以在安全性策略和安全性屏障视图的条件之前被执行。此外，没有参数的函数或者不从安全屏障视图或表传递任何参数的函数不一定要被标记为防泄漏的。

**`CALLED ON NULL INPUT`**

**`RETURNS NULL ON NULL INPUT`**

**`STRICT`**

- `CALLED ON NULL INPUT` （默认）表示在某些参数为空值时应正常调用该函数。如果有必要，函数的作者应该负责检查空值并且做出适当的相应。
- `RETURNS NULL ON NULL INPUT` 或 `STRICT` 表示只要其任意参数为空值，该函数就会返回空值。如果指定了这个参数，当有空值参数时该函数不会被执行，而是自动返回一个空值结果。

**`[EXTERNAL] SECURITY INVOKER`**

**`[EXTERNAL] SECURITY DEFINER`**

- `SECURITY INVOKER` 表示要用调用该函数的用户的特权来执行它。这是默认值。
- `SECURITY DEFINER` 指定要用拥有该函数的用户的特权来执行该函数。

为了符合 SQL，允许使用关键词 `EXTERNAL` 。但是它是可选的，因为与 SQL 中不同，这个特性适用于所有函数而不仅是那些外部函数。

**`PARALLEL`**

- `PARALLEL UNSAFE` 表示该函数不能在并行模式中运行并且 SQL 语句中存在一个这样的函数会强制使用顺序执行计划。这是默认选项。
- `PARALLEL RESTRICTED` 表示该函数能在并行模式中运行，但是其执行被限制在并行组的领导者中。
- `PARALLEL SAFE` 表示该函数对于在并行模式中运行是安全的并且不受限制。

如果函数修改任何数据库状态、会使用子事务之类的方式改变事务、访问序列或者对设置（如 `setval` ）做出持久性的更改，它们就应该被标记为并行不安全。如果它们访问临时表、客户端连接状态、游标、预备语句或者系统无法在并行模式中同步的本地后端状态（例如 `setseed` 只能在组领导者中执行，因为另一个进程所作的更改不会在领导者中被反映出来），它们应该被标为并行受限。通常，如果一个函数是受限的或者不安全的却被标成了安全，或者它本来是不安全的却被标成了受限，在并行查询中执行时它可能会抛出错误或者产生错误的答案。如果被错误的标记， C 语言函数理论上可能展现出完全无法定义的行为，因为系统没有办法保护自己不受任意的 C 代码影响，但是在大部分情况下其结果也不会比任何其他函数差到哪里去。如果有疑问，函数应该被标为 `UNSAFE` ，这也是默认值。

**`COST execution_cost`**

一个给出该函数的估计执行代价的正数，单位是 `cpu_operator_cost` 。如果该函数返回一个集合，这就是每个被返回行的代价。如果没有指定代价，对 C 语言和内部函数会指定为 1 个单位，对其他语言的函数则会指定为 100 单位。更大的值会导致规划器尝试避免对该函数的不必要的过多计算。

**`ROWS result_rows`**

一个正数，它给出规划器期望该函数返回的行数估计。只有当该函数被声明为返回一个集合时才允许这个参数。默认假设为 1000 行。

**`SUPPORT support_function`**

用于此函数的 planner support function 的名称（可选的模式限定）。你必须是超级用户才能使用此选项。

**`configuration_parameter`**

**`value`**

`SET` 子句导致进入该函数时指定配置参数将被设置为指定值。并且在该函数退出时恢复到该参数之前的值。 `SET FROM CURRENT` 会把 `CREATE FUNCTION` 被执行时该参数的当前值保存为进入该函数时将被应用的值。

如果一个 `SET` 子句被附加到一个函数，那么在该函数内为同一个变量执行的 `SET LOCAL` 命令会被限制于该函数：在函数退出时该配置参数之前的值仍会被恢复。不过，一个普通的 `SET` 命令（没有 `LOCAL` ）会覆盖 `SET` 子句，更像一个之前的 `SET LOCAL` 命令所做的那样：这种命令的效果在函数退出后将会持续，除非当前事务被回滚。

**`definition`**

一个定义该函数的字符串常量，其含义取决于语言。它可以是一个内部函数名、一个对象文件的路径、一个 SQL 命令或者用一种过程语言编写的文本。

美元引用通常对书写函数定义字符串有所帮助，而普通单引号语法则不会有用。如果没有美元引用，函数定义中的任何单引号或者反斜线必须用双写来转义。

**`obj_file, link_symbol`**

当 C 语言源代码中该函数的名称与 SQL 函数的名称不同时，这种形式的 `AS` 子句被用于动态可载入 C 语言函数。字符串 `obj_file` 是包含编译好的 C 函数的动态库文件的名称，它会由 `LOAD` 命令解析。字符串 `link_symbol` 是该函数的链接符号，也就是该函数在 C 语言源代码中的名称。如果省略链接符号，它将被假定为要定义的 SQL 函数的名称。所有函数的 C 名称都必须不同，因此必须为重载的 C 函数给出不同的 C 名称（例如把参数类型作为 C 名称的一部分）。

在重复调用引用同一对象文件的 `CREATE FUNCTION` 时，对每个会话该文件只会被载入一次。要卸载并且重新装载该文件（可能是在开发期间），需要开始一个新会话。

**重载**

瀚高数据库允许函数重载，也就是说同一个名称可以被用于多个不同的函数，只要它们具有可区分的输入参数类型。不管是否使用它，在有些用户不信任另一些用户的数据库中调用函数时，这种兼容性需要安全性的预防措施。

如果两个函数具有相同的名称和输入参数类型，它们被认为相同（不考虑任何 `OUT` 参数）。

因此这些声明会冲突：

```sql
CREATE FUNCTION foo(int) ...
CREATE FUNCTION foo(int, out text) ...
```

具有不同参数类型列表的函数在创建时将不会被认为是冲突的，但是如果默认值被提供，在使用时它们有可能会冲突。例如，考虑

```sql
CREATE FUNCTION foo(int) ...
CREATE FUNCTION foo(int, int default 42) ...
```

调用 `foo(10)` 将会失败，因为在要决定应该调用哪个函数时会有歧义。

**注解**

允许把完整的 SQL 类型语法用于声明一个函数的参数和返回值。不过， `CREATE FUNCTION` 会抛弃带圆括号的类型修饰符（例如类型 `numeric` 的精度域）。例如 `CREATE FUNCTION foo (varchar(10)) ...` 和 `CREATE FUNCTION foo (varchar) ...` 完全一样。

在用 `CREATE OR REPLACE FUNCTION` 替换一个现有函数时，对于更改参数名是有限制的。不能更改已经分配给任何输入参数的名称（不过可以给之前没有名称的参数增加名称）。如果有多于一个输出参数，不能更改输出参数的名称，因为可能会改变描述函数结果的匿名组合类型的列名。这些限制是为了确保函数被替换时，已有的对该函数的调用不会停止工作。

如果一个被声明为 `STRICT` 的函数带有一个 `VARIADIC` 参数，会严格检查该可变数组作为一个整体是否为非空。如果该数组有空值元素，该函数仍将被调用。

**示例**

这里是一些小例子，它们可以帮你了解函数创建。

一个简单的加法函数：

```sql
CREATE FUNCTION add(integer, integer) RETURNS integer
    AS 'select $1 + $2;'
    LANGUAGE SQL
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;
```

在 PL/pgSQL 中，使用一个参数名称增加一个整数：

```sql
CREATE OR REPLACE FUNCTION increment(i integer) RETURNS integer AS $$
BEGIN
    RETURN i + 1;
END;
$$ LANGUAGE plpgsql;
```

返回一个包含多个输出参数的记录：

```sql
CREATE FUNCTION dup(in int, out f1 int, out f2 text)
    AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
    LANGUAGE SQL;

SELECT * FROM dup(42);
```

你可以用更复杂的方式（用一个显式命名的组合类型）来做同样的事情：

```sql
CREATE TYPE dup_result AS (f1 int, f2 text);

CREATE FUNCTION dup(int) RETURNS dup_result
    AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
    LANGUAGE SQL;

SELECT * FROM dup(42);
```

另一种返回多列的方法是使用一个 `TABLE` 函数：

```sql
CREATE FUNCTION dup(int) RETURNS TABLE(f1 int, f2 text)
    AS $$ SELECT $1, CAST($1 AS text) || ' is text' $$
    LANGUAGE SQL;

SELECT * FROM dup(42);
```

不过， `TABLE` 函数与之前的例子不同，因为它实际返回了一个记录集合而不只是一个记录。

**安全地编写 SECURITY DEFINER 函数**

因为一个 `SECURITY DEFINER` 函数会被以创建它的用户的特权来执行，需要小心地确保该函数不会被误用。为了安全， `search_path` 应该被设置为排除任何不可信用户可写的模式。这可以阻止恶意用户创建对象（例如表、函数以及操作符）来掩饰该函数所要用到的对象。在这方面特别重要的是临时表模式，默认情况下它会第一个被搜索并且通常对任何用户都是可写的。可以通过强制最后搜索临时模式来得到一种安全的布局。要这样做，把 `pg_temp` 写成 `search_path` 中的最后一项。这个函数展示了安全的用法：

```sql
CREATE FUNCTION check_password(uname TEXT, pass TEXT)
    RETURNS BOOLEAN AS $$
DECLARE passed BOOLEAN;
BEGIN
    SELECT (pwd = $2) INTO passed
    FROM pwds
    WHERE username = $1;
    RETURN passed;
END;
$$ LANGUAGE plpgsql
SECURITY DEFINER
-- 设置一个安全的 search_path：受信的模式，然后是 'pg_temp'。
SET search_path = admin, pg_temp;
```

这个函数的目的是为了访问表 `admin.pwds` 。但是如果没有 `SET` 子句或者带有 `SET` 子句却只提到 `admin` ，该函数会变成创建一个名为 `pwds` 的临时表。

另一点要记住的是默认情况下，会为新创建的函数给 `PUBLIC` 授予执行特权。你常常会希望把安全定义器函数的使用限制在某些用户中。要这样做，你必须收回默认的 `PUBLIC` 特权，然后选择性地授予执行特权。为了避免出现新函数能被所有人访问的时间窗口，应在一个事务中创建它并且设置特权。例如：

```sql
BEGIN;
CREATE FUNCTION check_password(uname TEXT, pass TEXT) ... SECURITY DEFINER;
REVOKE ALL ON FUNCTION check_password(uname TEXT, pass TEXT) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION check_password(uname TEXT, pass TEXT) TO admins;
COMMIT;
```

**兼容性**

SQL 标准中定义了 `CREATE FUNCTION` 命令。瀚高数据库的版本与之类似但不完全兼容。属性是不可移植的，不同的可用语言也是不能移植的。

对于和一些其他数据库系统的兼容性， `argmode` 可以被写在 `argname` 之前或者之后。但只有第一种方式是兼容标准的。

对于参数默认值，SQL 标准只指定带有 `DEFAULT` 关键词的语法。带有 `=` 的语法被用在 T-SQL 和 Firebird 中。

**另见**

`ALTER FUNCTION` ， `DROP FUNCTION` ， `GRANT` ， `LOAD` ， `REVOKE`

## CREATE GROUP

— 定义一个新的数据库角色

**大纲**

```sql
CREATE GROUP name [ [ WITH ] option [ ... ] ]
```

其中 option 可以是：

```
SUPERUSER | NOSUPERUSER
| CREATEDB | NOCREATEDB
| CREATEROLE | NOCREATEROLE
| INHERIT | NOINHERIT
| LOGIN | NOLOGIN
| [ ENCRYPTED ] PASSWORD 'password'
| VALID UNTIL 'timestamp'
| IN ROLE role_name [, ...]
| IN GROUP role_name [, ...]
| ROLE role_name [, ...]
| ADMIN role_name [, ...]
| USER role_name [, ...]
| SYSID uid
```

**描述**

`CREATE GROUP` 现在是 `CREATE ROLE` 的一种别名。

**兼容性**

在 SQL 标准中没有 `CREATE GROUP` 语句。

**另见**

```
CREATE ROLE
```

## CREATE INDEX

— 定义一个新索引

**大纲**

```sql
CREATE [ UNIQUE ] INDEX [ CONCURRENTLY ] [ [ IF NOT EXISTS ] name ] ON
    [ ONLY ] table_name [ USING method ]
    ( { column_name | ( expression ) } [ COLLATE collation ] [ opclass ] [ ASC |
 DESC ] [ NULLS { FIRST | LAST } ] [, ...] )
    [ INCLUDE ( column_name [, ...] ) ]
    [ WITH ( storage_parameter = value [, ... ] ) ]
    [ TABLESPACE tablespace_name ]
    [ WHERE predicate ]
```

**描述**

`CREATE INDEX` 在指定关系的指定列上构建一个索引，该关系可以是一个表或者一个物化视图。索引主要被用来提升数据库性能（不过不当的使用会导致性能变差）。

索引的键域被指定为列名或者写在圆括号中的表达式。如果索引方法支持多列索引，可以指定多个域。

一个索引域可以是一个从表行的一列或者更多列值进行计算的表达式。这种特性可以被用来获得对基于基本数据某种变换的数据的快速访问。例如，一个在 `upper(col)` 上计算的索引可以允许子句 `WHERE upper(col) = 'JIM'` 使用索引。

瀚高数据库提供了索引方法 B-树、哈希、GiST、SP-GiST、GIN 以及 BRIN。用户也可以定义自己的索引方法，但是相对较复杂。

当 `WHERE` 子句存在时，会创建一个 **部分索引** 。部分索引只包含表中一部分行的项，通常索引这一部分会比表的其他部分更有用。例如，如果有一个表包含了已付和未付订单，其中未付订单占了整个表的一小部分并且是经常被使用的部分，可以通过只在这一部分上创建一个索引来改进性能。另一种可能的应用是使用带有 `UNIQUE` 的 `WHERE` 在表的一个子集上强制唯一性。

`WHERE` 子句中使用的表达式只能引用底层表的列，但它可以引用所有列而不仅仅是被索引的列。当前， `WHERE` 中也禁止使用子查询和聚集表达式。同样的限制也适用于表达式索引中的表达式域。

所有在索引定义中使用的函数和操作符必须是”不可变的”，就是说它们的结果必须仅依赖于它们的参数而不受外在因素（例如另一个表的内容和当前的时间）的影响。这种限制确保了索引的行为是良定的。要在一个索引表达式或者 `WHERE` 子句中使用用户定义的函数，记住在创建函数时把它标记为不可变。

**参数**

**`UNIQUE`**

导致系统在索引被创建时（如果数据已经存在）或者加入数据时检查重复值。会导致重复项的数据插入或者更新尝试将会产生一个错误。

当唯一索引被应用在分区边上时会有额外的限制，请参考 `CREATE TABLE` 。

**`CONCURRENTLY`**

当使用了这个选项时，瀚高数据库在构建索引时不会取得任何会阻止该表上并发插入、更新或者删除的锁。而标准的索引构建将会把表锁住以阻止对表的写（但不阻塞读），这种锁定会持续到索引创建完毕。在使用这个选项时有多个需要注意的地方 — 请见 **并发构建索引** 。

对于临时表， `CREATE INDEX` 始终是非并发的，因为没有其他会话可以访问它们，并且创建非并发索引的成本更低。

**`IF NOT EXISTS`**

如果一个同名关系已经存在则不要抛出错误。这种情况下会发出一个提示。注意着并不保证现有的索引与将要创建的索引有任何相似。当 `IF NOT EXISTS` 被指定时，需要指定索引名。

**`INCLUDE`**

可选的 `INCLUDE` 子句指定一个列的列表，其中的列将被包括在索引中作为非键列。非键列不能作为索引扫描的条件，并且该索引所强制的任何唯一性或者排除约束都不会考虑它们。不过，只用索引的扫描可以返回非键列的内容而无需访问该索引的基表，因为在索引项中就能直接拿到它们。因此，非键列的增加允许查询使用只用索引的扫描，否则就无法使用。

保守地向索引中增加非键列是明智的，特别是很宽的列。如果一个索引元组超过索引类型允许的最大尺寸，数据插入将会失败。在任何情况下，非键列都会重复来自索引基表的数据并且让索引的尺寸膨胀，因此可能会拖慢搜索。

`INCLUDE` 子句中列出的列不需要合适的操作符类，甚至数据类型没有为给定的访问方法定义操作符类的列都可以包括在这个子句中。

不支持把表达式作为被包括列，因为它们不能被用在只用索引的扫描中。

当前，有 B-树和 GiST 索引访问方法支持这一特性。在 B-树和 GiST 索引中， `INCLUDE` 子句中列出的列的值被包括在对应于堆元组的叶子元组中，但是不包括在用于树导航的上层索引项中。

**`name`**

要创建的索引名称。这里不能包括模式名，因为索引总是被创建在其基表所在的模式中。如果索引名称被省略，瀚高数据库将基于基表名称和被索引列名称选择一个合适的名称。

**`ONLY`**

如果该表是分区表，指示不要在分区上递归创建索引。默认会递归创建索引。

**`table_name`**

要被索引的表的名称（可以被模式限定）。

**`method`**

要使用的索引方法的名称。可以选择 `btree` 、 `hash` 、 `gist` 、 `spgist` 、 `gin` 以及 `brin` 。默认方法是 `btree` 。

**`column_name`**

一个表列的名称。

**`expression`**

一个基于一个或者更多个表列的表达式。如语法中所示，表达式通常必须被写在圆括号中。不过，如果该表达式是一个函数调用的形式，圆括号可以被省略。

**`collation`**

要用于该索引的排序规则的名称。默认情况下，该索引使用被索引列的排序规则或者被索引表达式的结果排序规则。当查询涉及到使用非默认排序规则的表达式时，使用非默认排序规则的索引就能排上用场。

**`opclass`**

一个操作符类的名称。详见下文。

**`ASC`**

指定上升排序（默认）。

**`DESC`**

指定下降排序。

**`NULLS FIRST`**

指定把空值排序在非空值前面。在指定 `DESC` 时，这是默认行为。

**`NULLS LAST`**

指定把空值排序在非空值后面。在没有指定 `DESC` 时，这是默认行为。

**`storage_parameter`**

索引方法相关的存储参数的名称。详见 **索引存储参数** 。

**`tablespace_name`**

在其中创建索引的表空间。如果没有指定，将会使用 `default_tablespace` 。或者对临时表上的索引使用 `temp_tablespaces` 。

**`predicate`**

部分索引的约束表达式。

**索引存储参数**

可选的 `WITH` 子句为索引指定存储参数。每一种索引方法都有自己的存储参数集合。B-树、哈希、GiST 以及 SP-GiST 索引方法都接受这个参数：

**`fillfactor`**

索引的填充因子是一个百分数，它决定索引方法将尝试填充索引页面的充满程度。对于 B-树，在初始的索引构建过程中，叶子页面会被填充至该百分数，当在索引右端扩展索引（增加新的最大键值）时也会这样处理。如果页面后来被完全填满，它们就会被分裂，导致索引的效率逐渐退化。B-树使用了默认的填充因子 90，但是也可以选择为 10 到 100 的任何整数值。如果表是静态的，那么填充因子 100 是最好的，因为它可以让索引的物理尺寸最小化。但是对于更新负荷很重的表，较小的填充因子有利于最小化对页面分裂的需求。其他索引方法以不同但是大致类似的方式使用填充因子，不同方法的默认填充因子也不相同。

B-树索引还额外接受这个参数：

**`vacuum_cleanup_index_scale_factor`**

`vacuum_cleanup_index_scale_factor` 针对每个索引的值。

GiST 还额外接受这个参数：

**`buffering`**

决定是否用缓冲构建技术来构建索引。 `OFF` 会禁用它， `ON` 则启用该特性，如果设置为 `AUTO` 则初始会禁用它，但是一旦索引尺寸到达 `effective_cache_size` 就会随时打开。默认值是 `AUTO` 。

GIN 索引接受不同的参数：

**`fastupdate`**

这个设置控制快速更新技术的使用。它是一个布尔参数： `ON` 启用快速更新， `OFF` 禁用之。默认是 `ON` 。

> **注意：**
> 
> 通过 `ALTER INDEX` 关闭 `fastupdate` 会阻止未来的更新进入到待处理索引项列表中，但它不会自己处理之前的待处理项。可以使用 `VACUUM` 或者调用 `gin_clean_pending_list` 确保处理完待处理列表的项。

**`gin_pending_list_limit`**

自定义 `gin_pending_list_limit` 参数。这个值要以千字节来指定。

BRIN 索引接受不同的参数：

**`pages_per_range`**

定义用于每一个 BRIN 索引项的块范围由多少个表块组成。默认是 128。

**`autosummarize`**

定义是否只要在下一个页面上检测到插入就为前面的页面范围运行概要操作。

**并发构建索引**

创建索引可能会干扰数据库的常规操作。通常瀚高数据库会锁住要被索引的表，让它不能被写入，并且用该表上的一次扫描来执行整个索引的构建。其他事务仍然可以读取表，但是如果它们尝试在该表上进行插入、更新或者删除，它们会被阻塞直到索引构建完成。如果系统是一个生产数据库，这可能会导致严重的后果。索引非常大的表可能会需要很多个小时，而且即使是较小的表，在构建索引过程中阻塞写入者一段时间在生产系统中也是不能接受的。

瀚高数据库支持构建索引时不阻塞写入。这种方法通过指定 `CREATE INDEX` 的 `CONCURRENTLY` 选项实现。当使用这个选项时，瀚高数据库必须执行该表的两次扫描，此外它必须等待所有现有可能会修改或者使用该索引的事务终止。因此这种方法比起标准索引构建过程来说要做更多工作并且需要更多时间。不过，由于它允许在构建索引时继续普通操作，这种方式对于在生产环境中增加新索引很有用。当然，由索引创建带来的额外 CPU 和 I/O 开销可能会拖慢其他操作。

在并发索引构建中，索引实际上在一个事务中被录入到系统目录，然后在两个事务中发生两次表扫描。在每一次表扫描之前，索引构建必须等待已经修改了表的现有事务终止。在第二次扫描之后，索引构建必须等待任何持有早于第二次扫描的快照（见第 13 章）的事务终止。然后该索引最终能被标记为准备好使用，并且 `CREATE INDEX` 命令终止。不过即便那样，该索引也不是立刻可以用于查询：在最坏的情况下，只要早于索引构建开始时存在的事务存在，该索引就无法使用。

如果在扫描表示出现问题，例如死锁或者唯一索引中的唯一性被违背， `CREATE INDEX` 将会失败，但留下一个”不可用”的索引。这个索引会被查询所忽略，因为它可能不完整。不过它仍将消耗更新开销。 `psql` 的 `\d` 命令将把这类索引报告为 `INVALID` ：

```sql
highgo=# \d tab
       Table "public.tab"
 Column |  Type   | Collation | Nullable | Default 
--------+---------+-----------+----------+---------
 col    | integer |           |          | 
Indexes:
    "idx" btree (col) INVALID
```

这种情况下推荐的恢复方法是删除该索引并且尝试再次执行 `CREATE INDEX CONCURRENTLY` 。（另一种可能性是用 `REINDEX INDEX CONCURRENTLY` 重建该索引）。

并发构建一个唯一索引时需要注意的另一点是，当第二次表扫描开始时，唯一约束已经被强制在其他事务上。这意味着在该索引变得可用之前，其他查询中可能就会报告该约束被违背，或者甚至在索引构建最终失败的情况中也是这样。还有，如果在第二次扫描时发生失败，”无效的”索引也会继续强制它的唯一性约束。

表达式索引和部分索引的并发构建也被支持。在这些表达式计算过程中发生的错误可能导致和上述唯一约束违背类似的行为。

常规索引构建允许在同一个表上同时构建其他常规索引，但是在一个表上同时只能有一个并发索引构建发生。在两种情况下，在索引被构建时不允许表的模式修改。另一个不同是，一个常规 `CREATE INDEX` 命令可以在一个事务块中执行，但是 `CREATE INDEX CONCURRENTLY` 不行。

当前不支持在分区表上并发生成索引。然而，你可以在每个分区上单独的并发构建索引，然后最终以非并发的方式创建分区索引，以减少对分区表的写入被锁定的时间。在这种情况下，生成分区索引仅是元数据操作。

**注解**

关于索引何时能被使用、何时不被使用以及什么情况下它们有用的信息请见第 11 章。

当前，只有 B-树、GiST、GIN 和 BRIN 索引方法支持多列索引。默认最多可以索引 32 个域（可以在构建瀚高数据库修改这种限制）。当前只有 B-树支持唯一索引。

为索引的每一列可以指定一个操作符类。该操作符类标识要被该索引用于该列的操作符。

例如，一个四字节整数上的 B-树索引会使用 `int4_ops` 类。这个操作符类包括了用于四字节整数的比较函数。实际上，通常列数据类型的默认操作符类就足够了。对某些数据类型指定操作符类的主要原因是，可能会有多于一种有意义的顺序。例如，我们可能想用绝对值或者实数部分对复数类型排序。我们可以通过为该数据类型定义两个操作符类来做到，并且在创建索引时选择其中合适的类。

当在一个分区表上调用 `CREATE INDEX` 时，默认的行为是递归到所有的分区上以确保它们都具有匹配的索引。每一个分区首先会被检查是否有一个等效的索引存在，如果有则该索引将被挂接为被创建索引的一个分区索引，而被创建的索引将成为其父索引。如果不存在匹配的索引，则会创建一个新的索引并且自动进行挂接。如果命令中没有指定索引名称，每个分区中的新索引的名称将被自动决定。如果指定了 `ONLY` 选项，则不会进行递归，并且该索引会被标记为无效（一旦所有的分区都得到该索引， `ALTER INDEX ... ATTACH PARTITION` 可以把该索引标记为有效）。不过，要注意不管是否指定这一选项，未来使用 `CREATE TABLE ... PARTITION OF` 创建的任何分区将自动有一个匹配的索引，不管有没有指定 `ONLY` 。

对于支持有序扫描的索引方法（当前只有 B-树），可以指定可选子句 `ASC` 、 `DESC` 、 `NULLS FIRST` 以及 `NULLS LAST` 来修改索引的排序顺序。由于一个有序索引能前向或者反向扫描，通常创建一个单列 `DESC` 索引没什么用处 — 一个常规索引已经提供了排序顺序。这些选项的价值是可以创建多列索引，让它的排序顺序匹配有混合排序要求的查询，例如 `SELECT ... ORDER BY x ASC, y DESC` 。如果你想要在依靠索引避免排序步骤的查询中支持”空值排序低”这种行为， `NULLS` 选项就能派上用场，默认的行为是”空值排序高”。

对于大多数索引方法，索引的创建速度取决于 `maintenance_work_mem` 的设置。较大的值将会减少索引创建所需的时间，当然不要把它设置得超过实际可用的内存量（那会迫使机器进行交换）。

瀚高数据库可以在构建索引时利用多个 CPU 以更快地处理表行。这种特性被称为 **并行索引构建** 。对于支持并行构建索引的索引方法（当前只有 B-树）， `maintenance_work_mem` 指定每次索引构建操作整体可用的最大内存量，而不管启动了多少工作者进程。一般来说，一个代价模型（如果有）自动判断应该请求多少工作者进程。

增加 `maintenance_work_mem` 可以让并行索引构建受益，而等效的串行索引构建将无法受益或者得到很小的益处。注意 `maintenance_work_mem` 可能会影响请求的工作者进程的数量，因为并行工作者必须在总的 `maintenance_work_mem` 预算中占有至少 32MB 的份额。还必须有 32MB 的份额留给领袖进程。增加 `max_parallel_maintenance_workers` 可以允许使用更多的工作者，这将降低索引创建所需的时间，只要索引构建不是 I/O 密集型的。当然，还需要有足够的 CPU 计算能力，否则工作者们会闲置。

通过 `ALTER TABLE` 为 `parallel_workers` 设置一个值直接控制着 `CREATE INDEX` 会对表请求多少并行工作者进程。这会完全绕过代价模型，并且防止 `maintenance_work_mem` 对请求多少并行工作者产生影响。通过 `ALTER TABLE` 将 `parallel_workers` 设置为 0 将禁用所有情况下的并行索引构建。

> **提示：**
> 
> 在把 `parallel_workers` 用于调优一次索引构建之后，你可能想要重置 `parallel_workers` 。这可以避免对查询计划的无意更改，因为 `parallel_workers` 影响所有的并行表扫描。

虽然带有 `CONCURRENTLY` 选项的 `CREATE INDEX` 支持并行构建并且没有特殊的限制，但只有第一次表扫描会实际以并行方式执行。

使用 `DROP INDEX` 可以移除一个索引。

以前的瀚高数据库发行也有一种 R-树索引方法。这种方法已经被移除，因为它比起 GiST 方法来说没有什么明显的优势。如果指定了 `USING rtree` ， `CREATE INDEX` 将会把它解释为 `USING gist` ，以便把旧的数据库转换成 GiST。

**示例**

在表 `films` 中的列 `title` 上创建一个 B-树索引：

```sql
CREATE UNIQUE INDEX title_idx ON films (title);
```

要在表 `films` 的列 `title` 上创建一个唯一的 B-树索引并且包括列 `director` 和 `rating` ：

```sql
CREATE UNIQUE INDEX title_idx ON films (title) INCLUDE (director, rating);
```

在表达式 `lower(title)` 上创建一个索引来允许高效的大小写无关搜索：

```sql
CREATE INDEX ON films ((lower(title)));
```

（在这个例子中我们选择省略索引名称，这样系统会选择一个名字，通常是 `films_lower_idx` ）。

创建一个具有非默认排序规则的索引：

```sql
CREATE INDEX title_idx_german ON films (title COLLATE "de_DE");
```

创建一个具有非默认空值排序顺序的索引：

```sql
CREATE INDEX title_idx_nulls_low ON films (title NULLS FIRST);
```

创建一个具有非默认填充因子的索引：

```sql
CREATE UNIQUE INDEX title_idx ON films (title) WITH (fillfactor = 70);
```

创建一个禁用快速更新的 GIN 索引：

```sql
CREATE INDEX gin_idx ON documents_table USING GIN (locations) WITH (fastupdate = off);
```

在表 `films` 中的列 `code` 上创建一个而索引并且把索引放在表空间 `indexspace` 中：

```sql
CREATE INDEX code_idx ON films (code) TABLESPACE indexspace;
```

在一个点属性上创建一个 GiST 索引，这样我们可以在转换函数的结果上有效地使用 box 操作符：

```sql
CREATE INDEX pointloc
    ON points USING gist (box(location,location));
SELECT * FROM points
    WHERE box(location,location) && '(0,0),(1,1)'::box;
```

创建一个表而不排斥对表的写操作：

```sql
CREATE INDEX CONCURRENTLY sales_quantity_index ON sales_table (quantity);
```

**兼容性**

`CREATE INDEX` 是一种瀚高数据库的语言扩展。在 SQL 标准中没有对于索引的规定。

**另见**

`ALTER INDEX` ， `DROP INDEX` ， `REINDEX`

## CREATE LANGUAGE

— 定义一种新的过程语言

**大纲**

```sql
CREATE [ OR REPLACE ] [ PROCEDURAL ] LANGUAGE name

CREATE [ OR REPLACE ] [ TRUSTED ] [ PROCEDURAL ] LANGUAGE name
    HANDLER call_handler [ INLINE inline_handler ] [ VALIDATOR valfunction ]
```

**描述**

`CREATE LANGUAGE` 为一个瀚高数据库数据库注册一种新的过程语言。接着，可以用这种新语言定义函数和存储过程。

> **注意：**
> 
> 大多数过程语言已经被做成了”扩展”，并且应该用 `CREATE EXTENSION` 而不是 `CREATE LANGUAGE` 来安装。 `CREATE LANGUAGE` 的直接使用现在应该被限制在扩展安装脚本中。如果在数据库中有一种”裸”语言（可能是一次升级的结果），可以用 `CREATE EXTENSION langname FROM unpackaged` 把它转换成一个扩展。

`CREATE LANGUAGE` 实际上把该语言名称与负责执行用该语言编写的函数的处理器函数关联在一起。

有两种形式的 `CREATE LANGUAGE` 命令。在第一种形式中，用户只提供想要的语言的名称。瀚高数据库服务器会查询 `pg_pltemplate` 系统目录来决定正确的参数。在第二种形式中，用户要提供语言参数和语言名称。第二种形式可以被用来创建一种没有定义在 `pg_pltemplate` 中的语言，但是这种方法被认为即将废弃。

当服务器在 `pg_pltemplate` 目录中为给定的语言名称找到一个项时，即使命令中已经包括了语言参数，它也将使用目录中的数据。这种行为简化了旧转储文件的载入，旧转储文件很可能包含过时的信息。

通常，用户必须拥有瀚高数据库超级用户特权来注册一种新的语言。不过，如果该语言被列举在 `pg_pltemplate` 目录中并且被标记为允许由数据库拥有者创建（ `tmpldbacreate` 为真），则数据库的拥有者可以把新语言注册在数据库中。默认是可信的语言能够由数据库拥有者创建，但是超级用户可以通过修改 `pg_pltemplate` 的内容来调整这种行为。语言的创建者会成为它的拥有者，并且以后可以删除它、对它重命名或者把它赋予给一个新的拥有者。

`CREATE OR REPLACE LANGUAGE` 将创建或者替换一种现有的定义。如果该语言已经存在，其参数会被根据指定的值或者来自 `pg_pltemplate` 的值更新。但该语言的拥有关系和权限设置不会更改，并且任何已有的用该语言编写的函数仍然被假定有效。除了创建一种语言的普通特权需求，用户还必须是超级用户或者已有语言的拥有者。 `REPLACE` 情况主要被用来确保该语言存在。如果该语言有一个 `pg_pltemplate` 项，那么 `REPLACE` 将不会实际更改现有定义的任何东西，除非从该语言被创建以来 `pg_pltemplate` 已经被修改过（很少见的情况）。

**参数**

**`TRUSTED`**

`TRUSTED` 指定该语言不会授予用户不该具有的数据访问。如果在注册语言时这个关键词被省略，只有具有瀚高数据库超级用户特权的用户才能使用该语言创建新函数。

**`PROCEDURAL`**

这是一个噪声词。

**`name`**

新过程语言的名称。该名称必须在该数据库的语言中唯一。

为了向后兼容，名称可以用单引号围绕。

**`HANDLER call_handler`**

`call_handler` 是一个之前注册的函数的名称，它将被调用来执行该过程语言的函数。

一种过程语言的调用处理器必须以一种编译型语言（如 C）编写并且具有版本 1 的调用约定，它必须在瀚高数据库内注册为一个没有参数并且返回 `language_handler` 类型的函数。 `language_handler` 是一种占位符类型，它被用来标识该函数为一个调用处理器。

**`INLINE inline_handler`**

`inline_handler` 是一个之前注册的函数的名称，它将被调用来执行一个该语言的匿名代码块（ `DO` 命令）。如果没有指定 `inline_handler` 函数，则该语言不支持匿名代码块。

该处理器函数必须接受一个 `internal` 类型的参数，该参数将是 `DO` 命令的内部表示，而且它通常将返回 `void` 。该处理器的返回值会被忽略。

**`VALIDATOR valfunction`**

`valfunction` 是一个之前注册的函数的名称，当一个该语言的新函数被创建时会调用该函数来验证新函数。如果没有指定验证器函数，那么一个新函数被创建时不会被检查。验证器函数必须接受一个 `oid` 类型的参数，它将是要被创建的函数的 OID，而且它通常将返回 `void` 。

一个验证器函数通常会检查函数体中的语法正确性，但是它也能查看函数的其他属性，例如该语言能否处理特定的参数类型。为了发出一个错误，验证器函数应该使用 `ereport()` 函数。验证器函数的返回值会被忽略。

如果指定的语言名称在 `pg_pltemplate` 中有一项，服务器会忽略 `TRUSTED` 选项和支持函数的名称。

**注解**

使用 `DROP LANGUAGE` 删除过程语言。

系统目录 `pg_language` 记录着有关当前已安装的语言的信息。还有， `psql` 命令 `\dL` 列出已安装的语言。

要以一种过程语言创建函数，用户必须具有对于该语言的 `USAGE` 特权。默认情况下，对于可信语言， `USAGE` 被授予给 `PUBLIC` （即所有人）。如果需要可以将它收回。

过程语言对于单个数据库来说是本地的。但是，一种语言可以被安装在 `template1` 数据库中，这会导致它在所有后续创建的数据库中自动变得可用。

如果对语言在服务器的 `pg_pltemplate` 中没有一项，调用处理器函数、内联处理器函数（如果有）以及验证器函数（如果有）必须已经存在。但是当有一个那样的项时，这些函数不必已经存在。如果它们在数据库中不存在，将自动定义它们（如果安装中实现该语言的共享库不可用可能会导致 `CREATE LANGUAGE` 失败）。

在旧版本的瀚高数据库，需要将处理器函数声明为返回占位符类型 `opaque` 而不是 `language_handler` 。为了支持载入旧的转储文件， `CREATE LANGUAGE` 将接受被声明为返回 `opaque` 的函数，但是它将发出一个提示并且把该函数的声明返回类型改为 `language_handler` 。

**示例**

创建任何标准过程语言的最好的方式是：

```sql
CREATE LANGUAGE plperl;
```

对于 `pg_pltemplate` 目录不知道的一种语言，需要这样的命令序列：

```sql
CREATE FUNCTION plsample_call_handler() RETURNS language_handler
    AS '$libdir/plsample'
    LANGUAGE C;

CREATE LANGUAGE plsample
    HANDLER plsample_call_handler;
```

**兼容性**

`CREATE LANGUAGE` 是一种瀚高数据库扩展。

**另见**

```
ALTER LANGUAGE\`, \`CREATE FUNCTION\`, \`DROP LANGUAGE\`, \`GRANT\`, \`REVOKE
```

## CREATE MATERIALIZED VIEW

— 定义一个新的物化视图

**大纲**

```sql
CREATE MATERIALIZED VIEW [ IF NOT EXISTS ] table_name
    [ (column_name [, ...] ) ]
    [ USING method ]
    [ WITH ( storage_parameter [= value] [, ... ] ) ]
    [ TABLESPACE tablespace_name ]
    AS query
    [ WITH [ NO ] DATA ]
```

**描述**

`CREATE MATERIALIZED VIEW` 定义一个查询的物化视图。在该命令被发出时，查询会被执行并且被用来填充该视图（除非使用了 `WITH NO DATA` ），并且后来可能会用 `REFRESH MATERIALIZED VIEW` 进行刷新。

`CREATE MATERIALIZED VIEW` 类似于 `CREATE TABLE AS` ，不过它还会记住被用来初始化该视图的查询，这样它可以在后来被命令刷新。一个物化视图有很多和表相同的属性，但是不支持临时物化视图。

**参数**

**`IF NOT EXISTS`**

如果已经存在一个同名的物化视图时不要抛出错误。这种情况下会发出一个提示。注意这不保证现有的物化视图与即将创建的物化视图相似。

**`table_name`**

要创建的物化视图的名称（可以被模式限定）。

**`column_name`**

新物化视图中的一个列名。如果没有提供列名，会从查询的输出列名来得到。

**`USING method`**

此可选子句指定用于存储新具体化视图内容的表访问方法；该方法需要是 `TABLE` 类型的访问方法。如果未指定此选项，则为新具体化视图选择默认表访问方法。详细信息请参考 `default_table_access_method` 。

**`WITH ( storage_parameter [= value] [, ... ] )`**

这个子句为新的物化视图指定可选的存储参数，详见 **存储参数** 。所有 `CREATE TABLE` 支持的参数 `CREATE MATERIALIZED VIEW` 也支持。详见 `CREATE TABLE` 。

**`TABLESPACE tablespace_name`**

`tablespace_name` 是要把新物化视图创建在其中的表空间的名称。如果没有指定，将查阅 `default_tablespace` 。

**`query`**

一个 `SELECT` 、 `TABLE` 或者 `VALUES` 命令。这个查询将在一个安全受限的操作中运行。特别地，对本身会创建临时表的函数的调用将会失败。

**`WITH [ NO ] DATA`**

这个子句指定物化视图是否在创建时被填充。如果不是，该物化视图将被标记为不可扫描并且在 `REFRESH MATERIALIZED VIEW` 被使用前不能被查询。

**兼容性**

`CREATE MATERIALIZED VIEW` 是一种瀚高数据库扩展。

**另见**

`ALTER MATERIALIZED VIEW` ， `CREATE TABLE AS` ， `CREATE VIEW` ， `DROP MATERIALIZED VIEW` ， `REFRESH MATERIALIZED VIEW`

## CREATE OPERATOR

— 定义一个新的操作符

**大纲**

```sql
CREATE OPERATOR name (
    {FUNCTION|PROCEDURE} = function_name
    [, LEFTARG = left_type ] [, RIGHTARG = right_type ]
    [, COMMUTATOR = com_op ] [, NEGATOR = neg_op ]
    [, RESTRICT = res_proc ] [, JOIN = join_proc ]
    [, HASHES ] [, MERGES ]
)
```

**描述**

`CREATE OPERATOR` 定义一个新的操作符 `name` 。定义操作符的用户会成为该操作符的拥有者。如果给出一个模式名，该操作符将被创建在指定的模式中。否则它会被创建在当前模式中。

操作符名称是最多 `NAMEDATALEN-1` （默认为 63）个字符的序列，这些字符可以是：

```
+ - * / < > = ~ ! @ # % ^ & | \` ?
```

对名称的选择有一些限制：

- `--` 和 `/*` 不能出现在操作符名称中，因为它们会被当做一段注释的开始。
- 多字符操作符名称不能以 `+` 或者 `-` 结束，除非该名称也包含至少一个下列字符：
	text
	```
	~ ! @ # % ^ & | \` ?
	```
	例如， `@-` 是一个被允许的操作符名称，而 `*-` 不是。这种限制允许瀚高数据库解析 SQL 兼容的命令而无需记号之间的空格。
- 将 `=>` 用作一个操作符名称已经不被推荐。在未来的发行中可能会被禁用。

在输入时 `!=` 会被映射为 `<>` ，因此这两个名字总是等效的。

必须至少定义 `LEFTARG` 和 `RIGHTARG` 中的一个。对于二元操作符，两者都必须被定义。对于右一元操作符，只应该定义 `LEFTARG` ，而对于左一元操作符只应该定义 `RIGHTARG` 。

`function_name` 函数必须在之前已经用 `CREATE FUNCTION` 定义好，并且必须被定义为接受正确数量的指定类型的参数。

在 `CREATE OPERATOR` 的语法中，关键词 `FUNCTION` 和 `PROCEDURE` 是等效的，但不管哪种情况下被引用的函数都必须是一个函数而不是过程。这里对关键词 `PROCEDURE` 的是用是有历史原因的，现在已经被废弃。

其他子句指定可选的操作符优化子句。要创建一个操作符，必须具有参数类型和返回类型上的 `USAGE` 特权，以及底层函数上的 `EXECUTE` 特权。如果指定了一个交换子或者求反器操作符，必须拥有这些操作符。

**参数**

**`name`**

要定义的操作符的名称。允许使用的字符请见上文。名称可以被模式限定，例如 `CREATE OPERATOR myschema.+ (...)` 。如果没有被模式限定，该操作符将被创建在当前模式中。

如果两个同一模式中的操作符在不同的数据类型上操作，它们可以具有相同的名称。这被称为 **重载** 。

**`function_name`**

用来实现这个操作符的函数。

**`left_type`**

这个操作符的左操作数（如果有）的数据类型。忽略这个选项可以表示一个左一元操作符。

**`right_type`**

这个操作符的右操作数（如果有）的数据类型。忽略这个选项可以表示一个右一元操作符。

**`com_op`**

这个操作符的交换子。

**`neg_op`**

这个操作符的求反器。

**`res_proc`**

用于这个操作符的限制选择度估计函数。

**`join_proc`**

用于这个操作符的连接选择度估算函数。

**`HASHES`**

表示这个操作符可以支持哈希连接。

**`MERGES`**

表示这个操作符可以支持归并连接。

要在 `com_op` 或者其他可选参数中给出一个模式限定的操作符名称，请使用 `OPERATOR()` 语法，例如：

```sql
COMMUTATOR = OPERATOR(myschema.===) ,
```

**注解**

无法在 `CREATE OPERATOR` 中指定一个操作符的词法优先级，因为解析器的优先级行为是硬写在代码中的。

废弃的选项 `SORT1` 、 `SORT2` 、 `LTCMP` 以及 `GTCMP` 以前被用来指定与支持归并连接的操作符相关的排序操作符的名称。因为相关操作符的信息可以在 B-树的操作符族中找到。如果给出了这些选项之一，它会被忽略（除非是为了隐式设置 `MERGES` 为真）。

使用 `DROP OPERATOR` 从数据库中删除用户定义的操作符。使用 `ALTER OPERATOR` 修改数据库中的操作符。

**示例**

下面的命令为数据类型 `box` 定义了一种新的操作符 `===` （面积相等）：

```sql
CREATE OPERATOR === (
    LEFTARG = box,
    RIGHTARG = box,
    FUNCTION = area_equal_function,
    COMMUTATOR = ===,
    NEGATOR = !==,
    RESTRICT = area_restriction_function,
    JOIN = area_join_function,
    HASHES, MERGES
);
```

**兼容性**

`CREATE OPERATOR` 是一种瀚高数据库扩展。在 SQL 标准中没有用户定义操作符的规定。

**另见**

`ALTER OPERATOR` ， `CREATE OPERATOR CLASS` ， `DROP OPERATOR`

## CREATE OPERATOR CLASS

— 定义一个新的操作符类

**大纲**

```sql
CREATE OPERATOR CLASS name [ DEFAULT ] FOR TYPE data_type
  USING index_method [ FAMILY family_name ] AS
  { OPERATOR strategy_number operator_name [ ( op_type, op_type ) ] [ FOR SEARCH | FOR ORDER BY sort_family_name ]
  | FUNCTION support_number [ ( op_type [ , op_type ] ) ] function_name ( argument_type [, ...] )
  | STORAGE storage_type
  } [, ... ]
```

**描述**

`CREATE OPERATOR CLASS` 创建新的操作符类。一个操作符类定义一种特殊的数据类型如何被用于一个索引。操作符类指定为该数据类型和索引方法扮演特殊角色或者”策略”的操作符。操作符类还指定当该操作符类被选择用于一个索引列时，索引方法要使用的支持函数。操作符类所使用的所有操作符和函数必须在操作符类被创建之前被定义好。

如果给出了一个模式名称，那么该操作符类会被创建在指定模式中。否则，它会被创建在当前模式中。同一模式中的两个操作符类只有在被用于不同的索引方法时才可以具有相同的名称。

定义操作符类的用户将成为其拥有者。当前，创建用户必须是超级用户（做出这种限制是因为错误的操作符类定义会让服务器混淆甚至崩溃）。

`CREATE OPERATOR CLASS` 当前不会检查操作符类定义是否包括该索引方法所要求的所有操作符和函数，也不会检查这些操作符和函数是否构成一个一致的集合。定义一个合法的操作符类是用户的责任。

相关的操作符类可以被组成操作符族。要把一个新的操作符类加入到一个现有的族中，可以在 `CREATE OPERATOR CLASS` 中指定 `FAMILY` 选项。如果没有这个选项，新的类会被放到一个同名的族中（如果族不存在会创建之）。

**参数**

**`name`**

要创建的操作符类的名称。该名称可以被模式限定。

**`DEFAULT`**

如果存在，该操作符类将成为其数据类型的默认操作符类。对一种特定的数据类型和索引方法至多有一个默认操作符类。

**`data_type`**

这个操作符类所用于的列数据类型。

**`index_method`**

这个操作符类所用于的索引方法的名称。

**`family_name`**

要把这个操作符类加入其中的已有操作符族的名称。如果没有指定，将使用一个同名操作符族（如果还不存在则创建之）。

**`strategy_number`**

用于一个与该操作符类相关联的操作符的索引方法策略号。

**`operator_name`**

一个与该操作符类相关联的操作符的名称（可以被模式限定）。

**`op_type`**

在一个 `OPERATOR` 子句中，这表示该操作符的操作数数据类型，或者用 `NONE` 来表示一个左一元或者右一元操作符。在操作数数据类型与该操作符的数据类型相同的一般情况下，操作数的数据类型可以被省略。

在一个 `FUNCTION` 子句中，这表示该函数要支持的操作数数据类型，如果它与该函数的输入数据类型（对于 B-树比较函数和哈希函数）或者操作符类的数据类型（对于 B-树排序支持函数和所有 GiST、SP-GiST、GIN 和 BRIN 操作符类中的函数）不同。这些默认值是正确的，并且 `op_type` 因此不必在 `FUNCTION` 子句中被指定，对于 B-树排序支持函数的情况来说，这表示跨数据类型比较。

**`sort_family_name`**

一个现有 btree 操作符族的名称（可以是模式限定的），它描述与一种排序操作符相关联的排序顺序。

如果 `FOR SEARCH` 和 `FOR ORDER BY` 都没有被指定，那么 `FOR SEARCH` 是默认值。

**`support_number`**

用于一个与该操作符类相关联的函数的索引方法支持函数编号。

**`function_name`**

一个用于该操作符类的索引方法支持函数的函数名称（可以是模式限定的）。

**`argument_type`**

该函数的参数数据类型。

**`storage_type`**

实际存储在索引中的数据类型。通常这和列数据类型相同，但是有些索引方法（当前有 GiST、GIN 和 BRIN）允许它们不同。除非索引方法允许使用不同的类型， `STORAGE` 子句必须被省略。如果 `data_type` 列被指定为 `anyarray` ，那么 `storage_type` 可以被声明为 `anyelement` 以指示索引条目是属于为每个特定索引创建的实际数组类型的元素类型的成员。

`OPERATOR` 、 `FUNCTION` 和 `STORAGE` 子句可以以任何顺序出现。

**注解**

因为索引机制在使用函数之前不检查它们的权限，将一个函数或者操作符包括在一个操作符类中相当于在其上授予公共执行权限。这对操作符类中很有用的函数来说通常不成问题。

操作符不应该用 SQL 函数定义。SQL 函数很有可能会被内联到调用查询中，这会妨碍优化器识别该查询匹配一个索引。

**示例**

下面的例子为数据类型 `_int4` （int4 数组）定义了一个 GiST 索引操作符。完整的例子请见 `intarray` 模块。

```sql
CREATE OPERATOR CLASS gist__int_ops
    DEFAULT FOR TYPE _int4 USING gist AS
&&
=
>
<
        OPERATOR 20 @@ (_int4, query_int),
        FUNCTION 1 g_int_consistent (internal, _int4, smallint, oid, internal),
        FUNCTION 2 g_int_union (internal, internal),
        FUNCTION 3 g_int_compress (internal),
        FUNCTION 4 g_int_decompress (internal),
        FUNCTION 5 g_int_penalty (internal, internal, internal),
        FUNCTION 6 g_int_picksplit (internal, internal),
        FUNCTION 7 g_int_same (_int4, _int4, internal);
```

**兼容性**

`CREATE OPERATOR CLASS` 是一种瀚高数据库扩展。在 SQL 标准中没有 `CREATE OPERATOR CLASS` 语句。

**另见**

`ALTER OPERATOR CLASS`, `DROP OPERATOR CLASS`, `CREATE OPERATOR FAMILY`, `ALTER OPERATOR FAMILY`

## CREATE OPERATOR FAMILY

— 定义一个新的操作符族

**大纲**

```sql
CREATE OPERATOR FAMILY name USING index_method
```

**描述**

`CREATE OPERATOR FAMILY` 创建一个新的操作符族。一个操作符族定义一个相关操作符类组成的集合，并且可能还包含一些额外的、与这些操作符类兼容但对于任何个体索引的功能不是至关重要的操作符和支持函数（对索引至关重要的操作符和函数应该被分组在相关的操作符类中，而不是”松散地”在操作符中。通常，单一数据类型操作符被限制在操作符类中，而跨数据类型操作符可以松散地存在于一个包含用于两种数据类型的操作符类的操作符族中）。

新的操作符族初始时为空。应该通过发出后续的 `CREATE OPERATOR CLASS` 命令来增加包含在其中的操作符类，还可以用可选的 `ALTER OPERATOR FAMILY` 命令来增加”松散的”操作符和它们对应的支持函数。

如果给出一个模式名称，该操作符族会被创建在指定的模式中。否则，它会被创建在当前模式中。只有当同一个模式中的两个操作符族是用于不同的索引方法时，它们才能拥有相同的名字。

定义一个操作符族的用户将成为它的拥有者。当前，创建用户必须是超级用户（做出这样的限制是因为错误的操作符族会让服务器混淆甚至崩溃）。

**参数**

**`name`**

要创建的操作符族的名称。该名称可以被模式限定。

**`index_method`**

这个操作符族要用于的索引方法的名称。

**兼容性**

`CREATE OPERATOR FAMILY` 是一种瀚高数据库扩展。在 SQL 标准中没有 `CREATE OPERATOR FAMILY` 语句。

**另见**

`ALTER OPERATOR FAMILY`, `DROP OPERATOR FAMILY`, `CREATE OPERATOR CLASS`, `ALTER OPERATOR CLASS`, `DROP OPERATOR CLASS`

## CREATE POLICY

— 为一个表定义一条新的行级安全性策略

**大纲**

```sql
CREATE POLICY name ON table_name
    [ AS { PERMISSIVE | RESTRICTIVE } ]
    [ FOR { ALL | SELECT | INSERT | UPDATE | DELETE } ]
    [ TO { role_name | PUBLIC | CURRENT_USER | SESSION_USER } [, ...] ]
    [ USING ( using_expression ) ]
    [ WITH CHECK ( check_expression ) ]
```

**描述**

`CREATE POLICY` 为一个表定义一条行级安全性策略。注意为了应用已被创建的策略，在表上必须启用行级安全性（使用 `ALTER TABLE ... ENABLE ROW LEVEL SECURITY` ）。

一条策略授予权限以选择、插入、更新或者删除匹配相关策略表达式的行。现有的表行会按照 `USING` 中指定的表达式进行检查，而将要通过 `INSERT` 或 `UPDATE` 创建的新行会按照 `WITH CHECK` 中指定的表达式进行检查。当 `USING` 表达式对于一个给定行返回真时，该行对用户可见，而返回假或空时该行不可见。当一个 `WITH CHECK` 表达式对一行返回真时，该行会被插入或更新，而如果返回假或空时会发生一个错误。

对于 `INSERT` 和 `UPDATE` 语句，在 `BEFORE` 触发器被引发后并且在任何数据修改真正发生之前， `WITH CHECK` 表达式会被强制。因此，一个 `BEFORE ROW` 触发器可以修改要被插入的数据，从而影响安全性策略检查的结果。 `WITH CHECK` 表达式在任何其他约束之前被强制。

策略名称是针对每个表的。因此，一个策略名称可以被用于很多个不同的表并且对于不同的表呈现适合于该表的定义。

策略可以被应用于特定的命令或者特定的角色。除非特别指定，新创建的策略的默认行为是适用于所有命令和角色。多个策略可以应用于单个命令，更多细节请见下文。

对同时具有 `USING` 和 `WITH CHECK` 表达式（ `ALL` 和 `UPDATE` ）的策略，如果没有定义 `WITH CHECK` 表达式，那么 `USING` 表达式将被用于决定哪些行可见（普通 `USING` 情况）以及允许哪些新行被增加（ `WITH CHECK` 情况）。

如果为一个表启用了行级安全性但是没有适用的策略存在，将假定为一种”默认否定”策略，这样任何行都不可见也不可更新。

**参数**

**`name`**

要创建的策略的名称。这必须和该表上已有的任何其他策略名称相区分。

**`table_name`**

该策略适用的表的名称（可以被模式限定）。

**`PERMISSIVE`**

指定策略被创建为宽容性策略。适用于一个给定查询的所有宽容性策略将被使用布尔”OR”操作符组合在一起。通过创建宽容性策略，管理员可以在能被访问的记录集合中进行增加。策略默认是宽容性的。

**`RESTRICTIVE`**

指定策略被创建为限制性策略。适用于一个给定查询的所有限制性策略将被使用布尔”AND”操作符组合在一起。通过创建限制性策略，管理员可以减少能被访问的记录集合，因为每一条记录都必须通过所有的限制性策略。

注意在限制性策略真正能发挥作用减少访问之前，需要至少一条宽容性策略来授予对记录的访问。如果只有限制性策略存在，则没有记录能被访问。当宽容性和限制性策略混合存在时，只有当一个记录能通过至少一条宽容性策略以及所有的限制性策略时，该记录才是可访问的。

**`command`**

该策略适用的命令。合法的选项是 `ALL` 、 `SELECT` 、 `INSERT` 、 `UPDATE` 以及 `DELETE` 。 `ALL` 为默认。有关这些策略如何被应用的细节见下文。

**`role_name`**

该策略适用的角色。默认是 `PUBLIC` ，它将把策略应用到所有的角色。

**`using_expression`**

任意的 SQL 条件表达式（返回 boolean）。该条件表达式不能包含任何聚集或者窗口函数。如果行级安全性被启用，这个表达式将被增加到引用该表的查询。让这个表达式返回真的行将可见。让这个表达式返回假或者空的任何行将对用户不可见（在 `SELECT` 中）并且将对修改不可用（在 `UPDATE` 或 `DELETE` 中）。这类行会被悄悄地禁止而不会报告错误。

**`check_expression`**

任意的 SQL 条件表达式（返回 boolean）。该条件表达式不能包含任何聚集或者窗口函数。如果行级安全性被启用，这个表达式将被用在该表上的 `INSERT` 以及 `UPDATE` 查询中。只有让该表达式计算为真的行才被允许。如果任何被插入的记录或者更新后的记录导致该表达式计算为假或者空，则会抛出一个错误。注意 `check_expression` 是根据行的新内容而不是原始内容计算的。

**针对每种命令的策略**

**`ALL`**

为一条策略使用 `ALL` 表示它将适用于所有命令，不管命令的类型如何。如果存在一条 `ALL` 策略以及更多特定的策略，则 `ALL` 策略和那些策略会被应用。此外， `ALL` 策略将同时适用于一个查询的选择端和修改端，如果只定义了一个 `USING` 表达式则将该 `USING` 表达式用于两种情况。

例如，如果发出一个 `UPDATE` ，那么 `ALL` 策略将同时影响 `UPDATE` 能更新哪些行（应用 `USING` 表达式）以及更新后的行是否被允许加入到表中（如果定义了 `WITH CHECK` 表达式，则应用之；否则使用 `USING` 表达式）。如果一条 `INSERT` 或者 `UPDATE` 命令尝试增加行到表中，但行没有通过 `ALL` 策略的 `WITH CHECK` 表达式，则整个语句将会中断。

**`SELECT`**

对一条策略使用 `SELECT` 表示它将适用于 `SELECT` 查询，并且无论何时都要求该约束所在的关系上的 `SELECT` 权限。其结果是在一次 `SELECT` 查询期间，只有该关系中那些通过了 `SELECT` 策略的记录才将被返回，并且查询要求 `SELECT` 权限，例如 `UPDATE` 也将只能看到那些 `SELECT` 策略允许的行。一条 `SELECT` 策略不能具有 `WITH CHECK` 表达式，因为它只适用于正在从关系中检索记录的情况。

**`INSERT`**

为一条策略使用 `INSERT` 表示它适用于 `INSERT` 命令。没有通过这种策略的正在被插入的行会导致策略违背错误，并且整个 `INSERT` 命令将会中止。一条 `INSERT` 策略不能具有 `USING` 表达式，因为它只适用于正在向关系增加记录的情况。

注意在带有 `ON CONFLICT DO UPDATE` 的 `INSERT` 中，只有对通过 `INSERT` 路径追加到关系的行才会检查 `INSERT` 策略的 `WITH CHECK` 表达式。

**`UPDATE`**

对策略使用 `UPDATE` 意味着它将应用于 `UPDATE` 、 `SELECT FOR UPDATE` 和 `SELECT FOR SHARE` 命令，还有 `INSERT` 命令的辅助性的 `ON CONFLICT DO UPDATE` 子句。由于 `UPDATE` 需要提取现有的记录并且用新修改的记录代替，故 `UPDATE` 策略接受 `USING` 表达式和 `WITH CHECK` 表达式。 `USING` 表达式决定 `UPDATE` 命令将能看到哪些要对其操作的记录，而 `WITH CHECK` 表达式定义哪些被修改的行允许存回到关系中。

任何更新后的值无法通过 `WITH CHECK` 表达式的行将会导致错误，并且整个命令将被中止。如果只指定了一个 `USING` 子句，那么该子句将被用于 `USING` 和 `WITH CHECK` 两种情况。

典型地， `UPDATE` 命令也需要从待更新关系中的列读数据（例如在 `WHERE` 子句、 `RETURNING` 子句或在 `SET` 子句右侧的表达式中）。这种情况下，正被更新的关系上也需要 `SELECT` 权限，并且除了 `UPDATE` 策略外，也要应用适当的 `SELECT` 或者 `ALL` 策略。这样，除由 `UPDATE` 或 `ALL` 策略授权更新行之外，通过 `SELECT` 或 `ALL` 策略用也必须能访问正被更新的行。

当 `INSERT` 命令附加了 `ON CONFLICT DO UPDATE` 子句时，如果采用 `UPDATE` 路径，先以任何 `UPDATE` 策略的 `USING` 表达式检查待更新的行，然后以 `WITH CHECK` 表达式检查新修改的行。但要注意的是，不同于单独的 `UPDATE` 命令，如果现有的行不能通过 `USING` 表达式检查，则抛出错误（ `UPDATE` 路径永不会静默地避免）。

**`DELETE`**

为一条策略使用 `DELETE` 表示它适用于 `DELETE` 命令。只有通过这条策略的行才将能被 `DELETE` 命令所看到。如果有的行不能通过该 `DELETE` 策略的 `USING` 表达式，则它们可以通过 `SELECT` 看到但不能被删除。

大多数情况下， `DELETE` 命令也需要从其所删除的关系中的列读取数据（例如在 `WHERE` 子句或 `RETURNING` 子句中）。这种情况下，在该关系上也需要 `SELECT` 权限，并且除了 `DELETE` 策略，也要应用适当的 `SELECT` 或 `ALL` 策略。这样，除由 `DELETE` 或 `ALL` 策略授权删除行之外，通过 `SELECT` 或 `ALL` 策略，用户也必须能访问正被删除的行。

`DELETE` 策略不能具有 `WITH CHECK` 表达式，因为它只适用于正在从关系中删除记录的情况，所以没有新行需要检查。

**表 19.1 按命令类型应用的策略**

| 命令 | SELECT/ALL 策略 USING 表达式 | INSERT/ALL 策略 WITH CHECK 表达式 | UPDATE/ALL 策略 USING 表达式 | UPDATE/ALL 策略 WITH CHECK 表达式 | DELETE/ALL 策略 USING 表达式 |
| --- | --- | --- | --- | --- | --- |
| `SELECT` | 现有行 | — | — | — | — |
| `SELECT FOR UPDATE/SHARE` | 现有行 | — | 现有行 | — | — |
| `INSERT` | — | 新行 | — | — | — |
| `INSERT ... RETURNING` | 新行 <sup>a</sup> | 新行 | — | — | — |
| `UPDATE` | 现有 & 新行 <sup>a</sup> | — | 现有行 | 新行 | — |
| `DELETE` | 现有行 <sup>a</sup> | — | — | — | 现有行 |
| `ON CONFLICT DO UPDATE` | 现有 & 新行 | — | 现有行 | 新行 | — |

<sup>a</sup> 对于现有行或新行，如果需要读访问的话（例如涉及到关系内列的 `WHERE` 或 `RETURNING` 子句）。

**多重策略的应用**

当多种不同命令类型的策略应用于相同命令（例如 `SELECT` 和 `UPDATE` 策略应用于 `UPDATE` 命令）时，用户就必须同时具有这两种类型的权限（例如从关系中选取行和更新的权限）。这样一种策略类型的表达式就与另一种策略类型的表达式通过使用 `AND` 操作符组合在一起。

当相同命令类型的多种策略应用于同一命令时，则必须至少有一个 `PERMISSIVE` 策略授权对该关系的访问，所有的 `RESTRICTIVE` 策略必须通过。这样，所有的 `PERMISSIVE` 策略表达式都用 `OR` 来组合，所有的 `RESTRICTIVE` 策略表达式都用 `AND` 来组合，而结果用 `AND` 来组合。如果没有 `PERMISSIVE` 策略，则拒绝访问。

要注意的是，出于组合多种策略的目的，将 `ALL` 策略视为与所应用的任何其他类型的策略具有相同的类型。

例如，在 `UPDATE` 命令中， `SELECT` 和 `UPDATE` 两种权限都需要，如果每种类型都有多个适用的策略，则将之以下面的方式组合：

```
expression from RESTRICTIVE SELECT/ALL policy 1
AND
expression from RESTRICTIVE SELECT/ALL policy 2
AND
...
AND
(
    expression from PERMISSIVE SELECT/ALL policy 1
    OR
    expression from PERMISSIVE SELECT/ALL policy 2
    OR
    ...
)
AND
expression from RESTRICTIVE UPDATE/ALL policy 1
AND
expression from RESTRICTIVE UPDATE/ALL policy 2
AND
...
AND
(
    expression from PERMISSIVE UPDATE/ALL policy 1
    OR
    expression from PERMISSIVE UPDATE/ALL policy 2
    OR
    ...
)
```

**注解**

要为一个表创建或者修改策略，你必须是该表的拥有者。

虽然策略将被应用于针对数据库中表的显式查询上，但当系统正在执行内部引用完整性检查或者验证约束时不会应用它们。这意味着有间接的方法来决定一个给定的值是否存在。

一个例子是向一个作为主键或者拥有唯一约束的列中尝试插入重复值。如果插入失败则用户可以推导出该值已经存在（这个例子假设用户被策略允许插入他们看不到的记录）。另一个例子是一个用户被允许向一个引用了其他表的表中插入，然而另一个表是隐藏表。通过用户向引用表中插入值可以判断存在性，成功表示该值存在于被引用表中。为了解决这些问题，应该仔细地制作策略以完全阻止用户插入、删除或者更新那些可能指示他们不能看到的值的记录，或者使用生成的值（例如代理键）来代替具有外部含义的键。

通常，系统将在应用用户查询中出现的条件之前先强制由安全性策略施加的过滤条件，这是为了防止无意中把受保护的数据暴露给可能不可信的用户定义函数。不过，被系统（或者系统管理员）标记为 `LEAKPROOF` 的函数和操作符可以在策略表达式之前被计算，因为它们已经被假定为可信。

因为策略表达式会被直接加到用户查询上，它们将使用运行整个查询的用户的权限运行。

因此，使用一条给定策略的用户必须能够访问表达式中引用的任何表或函数，否则在尝试查询启用了行级安全性的表时，他们将简单地收到一条没有权限的错误。不过，这不会改变视图的工作方式。就普通查询和视图来说，权限检查和视图所引用的表的策略将使用视图拥有者的权限以及任何适用于视图拥有者的策略。

**兼容性**

`CREATE POLICY` 是一种瀚高数据库扩展。

**另见**

`ALTER POLICY`, `DROP POLICY`, `ALTER TABLE`

## CREATE PROCEDURE

— 定义一个新的过程

**大纲**

```sql
CREATE [ OR REPLACE ] PROCEDURE
    name ( [ [ argmode ] [ argname ] argtype [ { DEFAULT | = } default_expr ] [, ...] ] )
    {
        LANGUAGE lang_name
      | TRANSFORM { FOR TYPE type_name } [, ... ]
      | [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
      | SET configuration_parameter { TO value | = value | FROM CURRENT }
      | AS 'definition'
      | AS 'obj_file', 'link_symbol'
    } [...]
```

**简介**

`CREATE PROCEDURE` 定义一个新的过程。 `CREATE OR REPLACE PROCEDURE` 将会创建一个新过程或者替换一个已有的定义。为了能够定义过程，用户必须具有所使用的语言上的 `USAGE` 特权。

如果这个命令中包括了一个方案名称，则该过程将被创建在该方案中。否则过程将被创建在当前的方案中。新过程的名称不能匹配同一方案中具有相同输入参数类型的任何现有过程或函数。不过，具有不同参数类型的过程和函数可以共享同一个名称（这被称为重载）。

要替换一个已有过程的当前定义，请使用 `CREATE OR REPLACE PROCEDURE` 。不能用这种方式更改过程的名称或者参数类型（如果尝试这样做，实际上会创建一个新的、不同的过程）。

当 `CREATE OR REPLACE PROCEDURE` 被用来替换一个现有的过程时，该过程的拥有关系和权限保持不变。所有其他的过程属性会被赋予这个命令中指定的或者暗示的值。必须拥有（包括成为拥有角色的成员）该过程才能替换它。

创建过程的用户将成为该过程的拥有者。

为了能够创建一个过程，用户必须具有参数类型上的 `USAGE` 特权。

**参数**

**`name`**

要创建的过程的名称（可以是被方案限定的）。

**`argmode`**

参数的模式可以是： `IN` 、 `INOUT` 或者 `VARIADIC` 。如果省略，则默认为 `IN` （当前对过程不支持 `OUT` 参数，可使用 `INOUT` ）。

**`argname`**

参数的名称。

**`argtype`**

过程的参数（如果有）的数据类型（可以是被方案限定的）。参数类型可以是基础类型、组合类型或者域类型，或者可以引用一个表列的类型。

根据具体的实现语言，还可能可以指定”伪类型”，例如 `cstring` 。伪类型表示实际的参数类型没有完全确定，或者是位于普通 SQL 数据类型的集合之外。

写上 `table_name.column_name%TYPE` 可以引用某个列的类型。使用这种特性有时可以让过程不受表定义改变的影响。

**`default_expr`**

没有指定参数时要被用作默认值的表达式。这个表达式必须符合该参数的参数类型。跟在有默认值的参数后面的输入参数也都必须有默认值。

**`lang_name`**

用于实现该过程的语言名称。它可以是 `sql` 、 `c` 、 `internal` 或者一种用户定义的过程语言的名称，例如 `plpgsql` 。将名称包裹在单引号内的方式已经被废弃，并且要求大小写匹配。

**`TRANSFORM { FOR TYPE type_name } [, ... ]`**

列出对过程的调用应该应用哪些 Transform。Transform 负责在 SQL 类型和语言相关的数据类型之间进行转换，请参考 `CREATE TRANSFORM` 。过程语言实现通常采用硬编码的方式保存内建类型的知识，因此它们无需在这里列出。但如果一种过程语言实现不知道如何处理一种类型并且没有提供 Transform，它将回退到默认的行为来转换数据类型，但是这依赖于其实现。

**`[EXTERNAL] SECURITY INVOKER`**  
**`[EXTERNAL] SECURITY DEFINER`**

`SECURITY INVOKER` 指示过程以调用它的用户的特权来执行。这是默认方式。 `SECURITY DEFINER` 指定过程以拥有它的用户的特权来执行。

为了符合 SQL 标注，允许使用 `EXTERNAL` 关键词，但它是可选的，因为和 SQL 中不同，这个特性适用于所有的过程而不仅仅是外部过程。

`SECURITY DEFINER` 过程不能执行事务控制语句（例如 `COMMIT` 和 `ROLLBACK` ，具体取决于实现的语言）。

**`configuration_parameter`**  
**`value`**

`SET` 子句导致在进入该过程时指定的配置参数被设置为指定的值，并且在过程退出时恢复到之前的值。 `SET FROM CURRENT` 把 `CREATE PROCEDURE` 执行时该参数的当前值保存为在进入该过程时要应用的值。

如果对过程附加一个 `SET` 子句，那么在该过程中为同一个变量执行的 `SET LOCAL` 命令的效果就被限制于该过程：在过程退出时还是会恢复到该配置参数的以前的值。不过，一个普通的 `SET` 命令（没有 `LOCAL` ）会重载这个 `SET` 子句，很像它对一个之前的 `SET LOCAL` 命令所做的事情：这样一个命令的效果将持续到过程退出之后，除非当前事务被回滚。

如果对过程附加一个 `SET` 子句，则该过程不能执行事务控制语句（例如 `COMMIT` 和 `ROLLBACK` ，具体取决于实现的语言）。

**`definition`**

一个定义该过程的字符串常量，其含义取决于语言。它可以是一个内部的过程名、一个对象文件的路径、一个 SQL 命令或者以一种过程语言编写的文本。

在编写过程的定义字符串时，使用美元引用而不是普通的单引号语法常常会很有帮助。如果没有美元引用，过程定义中的任何单引号或者反斜线必须以双写的方式进行转义。

**`obj_file, link_symbol`**

当 C 语言源码中的过程名与 SQL 过程的名称不同时，这种形式的 `AS` 子句被用于动态可装载的 C 语言过程。字符串 `obj_file` 是包含已编译好的 C 过程的共享库文件名，并且被按照 `LOAD` 命令的方式解析。字符串 `link_symbol` 是该过程的链接符号，也就是该过程在 C 语言源代码中的名称。如果链接符号被省略，则会被假定为与正在被定义的 SQL 过程的名称相同。

当重复的 `CREATE PROCEDURE` 调用引用同一个对象文件时，只会对每一个会话装载该文件一次。要卸载或者重新载入该文件（可能是在开发期间），应该开始一个新的会话。

**注解**

函数创建也适用于过程，更多细节请参考 `CREATE FUNCTION` 。

使用 `CALL` 来执行过程。

**示例**

```sql
CREATE PROCEDURE insert_data(a integer, b integer)
LANGUAGE SQL
AS $$
    INSERT INTO tbl VALUES (a);
    INSERT INTO tbl VALUES (b);
$$;

CALL insert_data(1, 2);
```

**兼容性**

SQL 标准中定义有一个 `CREATE PROCEDURE` 命令。瀚高数据库的版本类似但是并不完全兼容。

详情请见 `CREATE FUNCTION` 。

**另见**

`ALTER PROCEDURE`, `DROP PROCEDURE`, CALL, `CREATE FUNCTION`

## CREATE PUBLICATION

— 定义一个新的发布

**大纲**

```sql
CREATE PUBLICATION name
    [ FOR TABLE [ ONLY ] table_name [ * ] [, ...]
    | FOR ALL TABLES ]
    [ WITH ( publication_parameter [= value] [, ... ] ) ]
```

**描述**

`CREATE PUBLICATION` 向当前数据库添加一个新的发布。发布的名称必须与当前数据库中任何现有发布的名称不同。

发布本质上是一组表，其数据更改旨在通过逻辑复制进行复制。

**参数**

**`name`**

新发布的名称。

**`FOR TABLE`**

指定要添加到发布的表的列表。如果在表名之前指定了 `ONLY` ，那么只有该表被添加到发布中。如果没有指定 `ONLY` ，则添加表及其所有后代表（如果有的话）。可选地，可以在表名之后指定 `*` 以明确指示包含后代表。

只有持久基表才能成为出版物的一部分。临时表、非日志表、外表、物化视图、常规视图和分区表不能成为发布的一部分。要复制分区表，请将各个分区添加到发布中。

**`FOR ALL TABLES`**

将发布标记为复制数据库中所有表的更改，包括在将来创建的表。

**`WITH ( publication_parameter [= value] [, ... ] )`**

该子句指定发布的可选参数。支持下列参数：

**`publish`** (`string`)

这个参数决定了哪些 DML 操作将由新的发布发布给订阅者。该值是用逗号分隔的操作列表。允许的操作是 `insert` 、 `update` 、 `delete` 和 `truncate` 。默认是发布所有的动作，所以这个选项的默认值是 `'insert, update, delete, truncate'` 。

**注解**

如果既没有指定 `FOR TABLE` ，也没有指定 `FOR ALL TABLES` ，那么这个发布就是以一组空表开始的。这在稍后添加表格的情况下是有用的。

创建发布不会开始复制。它只为未来的订阅者定义一个分组和过滤逻辑。

要创建一个发布，调用者必须拥有当前数据库的 `CREATE` 权限。（当然，超级用户不需要这个检查。）

要将表添加到发布中，调用者必须拥有该表的所有权。 `FOR ALL TABLES` 子句要求调用者是超级用户。

添加到发布 `UPDATE` 和/或 `DELETE` 操作的发布的表必须已经定义了 `REPLICA IDENTITY` 。否则将在这些表上禁止这些操作。

对于 `INSERT ... ON CONFLICT` 命令，发布将公布从命令实际产生的操作。因此，根据结果，它可以作为 `INSERT` 或 `UPDATE` 发布，也可以根本不发布。

`COPY ... FROM` 命令是作为 `INSERT` 操作发布的。

不发布 DDL 操作。

**示例**

创建一个发布，发布两个表中所有更改：

```sql
CREATE PUBLICATION mypublication FOR TABLE users, departments;
```

创建一个发布，发布所有表中的所有更改：

```sql
CREATE PUBLICATION alltables FOR ALL TABLES;
```

创建一个发布，只发布一个表中的 `INSERT` 操作：

```sql
CREATE PUBLICATION insert_only FOR TABLE mydata
    WITH (publish = 'insert');
```

**兼容性**

`CREATE PUBLICATION` 是一个瀚高数据库扩展。

**又见**

`ALTER PUBLICATION`, `DROP PUBLICATION`

## CREATE ROLE

— 定义一个新的数据库角色

**大纲**

```sql
CREATE ROLE name [ [ WITH ] option [ ... ] ]
```

其中 `option` 可以是：

```
SUPERUSER | NOSUPERUSER
| CREATEDB | NOCREATEDB
| CREATEROLE | NOCREATEROLE
| INHERIT | NOINHERIT
| LOGIN | NOLOGIN
| REPLICATION | NOREPLICATION
| BYPASSRLS | NOBYPASSRLS
| CONNECTION LIMIT connlimit
| [ ENCRYPTED ] PASSWORD 'password' | PASSWORD NULL
| VALID UNTIL 'timestamp'
| IN ROLE role_name [, ...]
| IN GROUP role_name [, ...]
| ROLE role_name [, ...]
| ADMIN role_name [, ...]
| USER role_name [, ...]
| SYSID uid
```

**描述**

`CREATE ROLE` 向瀚高数据库数据库集簇增加一个新的角色。一个角色是一个实体，它可以拥有数据库对象并且拥有数据库特权。根据一个角色如何被使用，它可以被考虑成一个”用户”、一个”组”或者两者。要使用这个命令，你必须具有 `CREATEROLE` 特权或者成为一个数据库超级用户。

注意角色是定义在数据库集簇层面上的，并且因此在集簇中的所有数据库中都可用。

**参数**

**`name`**

新角色的名称。

**`SUPERUSER`**  
**`NOSUPERUSER`**

这些子句决定新角色是否是一个”超级用户”，它可以越过数据库内的所有访问限制。

超级用户状态很危险并且只应该在确实需要时才用。要创建一个新超级用户，你必须自己是一个超级用户。如果没有指定，默认值是 `NOSUPERUSER` 。

**`CREATEDB`**  
**`NOCREATEDB`**

这些子句定义一个角色创建数据库的能力。如果指定了 `CREATEDB` ，被定义的角色将被允许创建新的数据库。指定 `NOCREATEDB` 将否定一个角色创建数据库的能力。如果没有指定，默认值是 `NOCREATEDB` 。

**`CREATEROLE`**  
**`NOCREATEROLE`**

这些子句决定一个角色是否被允许创建新的角色（也就是执行 `CREATE ROLE` ）。一个带有 `CREATEROLE` 特权的角色也能修改和删除其他角色。如果没有指定，默认值是 `NOCREATEROLE` 。

**`INHERIT`**  
**`NOINHERIT`**

如果新的角色是其他角色的成员，这些子句决定新角色是否从那些角色中”继承”特权，把新角色作为成员的角色称为新角色的父角色。一个带有 `INHERIT` 属性的角色能够自动使用已经被授予给其直接或间接父角色的任何数据库特权。如果没有 `INHERIT` ，在另一个角色中的成员关系只会把 `SET ROLE` 的能力授予给那个其他角色，只有在这样做后那个其他角色的特权才可用。如果没有指定，默认值是 `INHERIT` 。

**`LOGIN`**  
**`NOLOGIN`**

这些子句决定一个角色是否被允许登录，也就是在客户端连接期间该角色是否能被给定为初始会话认证名称。一个具有 `LOGIN` 属性的角色可以被考虑为一个用户。没有这个属性的角色对于管理数据库特权很有用，但是却不是用户这个词的通常意义。如果没有指定，默认值是 `NOLOGIN` ，不过当 `CREATE ROLE` 被通过 `CREATE USER` 调用时默认值会是 `LOGIN` 。

**`REPLICATION`**  
**`NOREPLICATION`**

这些子句决定一个角色是否为复制角色。角色必须具有这个属性（或者成为一个超级用户）才能以复制模式（物理复制或者逻辑复制）连接到服务器以及创建或者删除复制槽。一个具有 `REPLICATION` 属性的角色是一个具有非常高特权的角色，并且只应被用于确实需要复制的角色上。如果没有指定，默认值是 `NOREPLICATION` 。

**`BYPASSRLS`**  
**`NOBYPASSRLS`**

这些子句决定是否一个角色可以绕过每一条行级安全性（RLS）策略。默认是 `NOBYPASSRLS` 。注意 `pg_dump` 将默认把 `row_security` 设置为 `OFF` ，以确保一个表的所有内容被转储出来。如果运行 `pg_dump` 的用户不具有适当的权限，将会返回一个错误。超级用户和被转储表的拥有者总是可以绕过 RLS。

**`CONNECTION LIMIT connlimit`**

如果角色能登录，这指定该角色能建立多少并发连接。 `-1` （默认值）表示无限制。注意这个限制仅针对于普通连接。预备事务和后台工作者连接都不受这一限制管辖。

**`[ ENCRYPTED ] PASSWORD 'password'`**  
**`PASSWORD NULL`**

设置角色的口令（口令只对具有 `LOGIN` 属性的角色有用，但是不管怎样你还是可以为没有该属性的角色定义一个口令）。如果你没有计划使用口令认证，你可以忽略这个选项。

如果没有指定口令，口令将被设置为空并且该用户的口令认证总是会失败。也可以用 `PASSWORD NULL` 显式地写出一个空口令。

口令总是以加密的方式存放在系统目录中。 `ENCRYPTED` 关键词没有实际效果，它只是为了向后兼容性而存在。加密的方法由配置参数 `password_encryption` 决定。如果当前的口令字符串已经是 MD5 加密或者 SCRAM 加密的格式，那么不管 `password_encryption` 的值是什么，口令字符串还是原样存储（因为系统无法解密以不同格式加密的口令字符串）。这种方式允许在转储/恢复时重载加密的口令。

**`VALID UNTIL 'timestamp'`**

`VALID UNTIL` 机制设置一个日期和时间，在该时间点之后角色的口令将会失效。如果这个子句被忽略，那么口令将总是有效。

**`IN ROLE role_name`**

`IN ROLE` 子句列出一个或多个现有的角色，新角色将被立即作为新成员加入到这些角色中（注意没有选项可以把新角色作为一个管理员加入，需要用一个单独的 `GRANT` 命令来完成）。

**`IN GROUP role_name`**

`IN GROUP` 是 `IN ROLE` 的一种已废弃的拼写方式。

**`ROLE role_name`**

`ROLE` 子句列出一个或者多个现有角色，它们会被自动作为成员加入到新角色中（这实际上新角色变成了一个”组”）。

**`ADMIN role_name`**

`ADMIN` 子句与 `ROLE` 相似，但是被提及的角色被使用 `WITH ADMIN OPTION` 加入到新角色中，让它们能够把这个角色中的成员关系授予给其他人。

**`USER role_name`**

`USER` 子句是 `ROLE` 子句的一个已废弃的拼写方式。

**`SYSID uid`**

`SYSID` 子句会被忽略，但是会为了向后兼容，还是会接受它。

**注解**

使用 `ALTER ROLE` 来更改一个角色的属性，以及使用 `DROP ROLE` 来移除一个角色。所有用 `CREATE ROLE` 指定的属性可以被后来的 `ALTER ROLE` 命令所修改。

增加和移除组角色成员的最佳方式是使用 `GRANT` 和 `REVOKE` 。

`VALID UNTIL` 子句只为一个口令而不是为一个角色本身定义了一个过期时间。特别地，当使用一个非基于口令认证的方法登录时，过期时间是不会被强制的。

`INHERIT` 属性管理可授予特权（也就是对数据库对象和角色成员关系的访问特权）的继承性。它并不适用于由 `CREATE ROLE` 和 `ALTER ROLE` 设置的特殊角色属性。例如，作为具有 `CREATEDB` 特权的角色的一个成员，并不会立刻授予创建数据库的角色，即便 `INHERIT` 被设置也是如此，在创建一个数据库之前必须通过 `SET ROLE` 成为该角色。

`INHERIT` 属性是用于向后兼容原因的默认值：在早前的瀚高数据库发布中，用户总是能够访问其所属组的所有特权。不过， `NOINHERIT` 更加接近于 SQL 标准中指定的语义。

要小心 `CREATEROLE` 特权。对于一个 `CREATEROLE` 角色的特权没有继承的概念。那意味着即使一个角色没有特定的特权但被允许创建其他角色，它可以轻易地创建与自身特权不同的另一个角色（除了创建具有超级用户特权的角色）。例如，如果角色 “user” 具有 `CREATEROLE` 特权但是没有 `CREATEDB` 特权，但是它能够创建一个带有 `CREATEDB` 特权的新角色。因此，可以把具有 `CREATEROLE` 特权的角色看成是准超级用户角色。

瀚高数据库包括一个程序 `createuser` ，它具有和 `CREATE ROLE` 相同的功能（事实上，它会调用这个命令），但是它可以从命令 shell 中运行。

`CONNECTION LIMIT` 只被近似地强制，如果两个新会话在几乎相同时间被开始，而此时该角色只剩下刚好一个连接”槽”，两者可能都将失败。还有，该限制从不对超级用户强制。

用这个命令指定一个非加密口令时必须加以注意。该命令将被以明文的形式传输到服务器，并且它也可能被记录在客户端命令历史或者服务器日志中。不过，命令 `createuser` 会传输加密的口令。还有， `psql` 包含一个命令 `\password` ，它可以被用来安全地改变该口令。

**示例**

创建一个能登录但是没有口令的角色：

```sql
CREATE ROLE jonathan LOGIN;
```

创建一个有口令的角色：

```sql
CREATE USER davide WITH PASSWORD 'jw8s0F4';
```

（ `CREATE USER` 和 `CREATE ROLE` 完全相同，除了它带有 `LOGIN` ）。

创建一个角色，它的口令有效期截止到 2004 年底。在进入 2005 年第一秒时，该口令会失效。

```sql
CREATE ROLE miriam WITH LOGIN PASSWORD 'jw8s0F4' VALID UNTIL '2005-01-01';
```

创建一个能够创建数据库并且管理角色的角色：

```sql
CREATE ROLE admin WITH CREATEDB CREATEROLE;
```

**兼容性**

SQL 标准中有 `CREATE ROLE` 语句，但是标准只要求语法：

```sql
CREATE ROLE name [ WITH ADMIN role_name ]
```

多个初始管理员以及 `CREATE ROLE` 的所有其他选项都是瀚高数据库扩展。

SQL 标准定义了用户和角色的概念，但是它把它们看成是可区分的概念并且将定义用户的所有命令留给每一种数据库实现来指定。在瀚高数据库中，我们已经选择把用户和角色统一成一种单一实体类型。因此角色比起标准中拥有更多可选的属性。

SQL 标准指定的行为可以通过给用户 `NOINHERIT` 属性来得到最大的金丝，而角色会被给予 `INHERIT` 属性。

**参见**

`SET ROLE`, `ALTER ROLE`, `DROP ROLE`, `GRANT, REVOKE`, `createuser`

## CREATE RULE

— 定义一条新的重写规则

**大纲**

```sql
CREATE [ OR REPLACE ] RULE name AS ON event
    TO table_name [ WHERE condition ]
    DO [ ALSO | INSTEAD ] { NOTHING | command | ( command ; command ... ) }
```

其中 `event` 可以是以下之一：

```
SELECT | INSERT | UPDATE | DELETE
```

**描述**

`CREATE RULE` 定义一条应用于指定表或视图的新规则。 `CREATE OR REPLACE RULE` 将创建一条新规则或者替换同一个表上具有同一名称的现有规则。

瀚高数据库规则系统允许我们定义针对数据库表中插入、更新或者删除动作上的替代动作。大约来说，当在一个给定表上执行给定命令时，一条规则会导致执行额外的命令。或者 `INSTEAD` 规则可以用另一个命令替换给定的命令，或者导致一个命令根本不被执行。规则也被用来实现 SQL 视图。规则实际上是一种命令转换机制或者命令宏。这种转换会在命令的执行开始之前进行。如果你实际上想要为每一个物理行独立地触发一个操作，你可能更需要一个触发器而不是规则。

当前， `ON SELECT` 规则必须是无条件 `INSTEAD` 规则并且其动作必须由一个单一 `SELECT` 命令构成。因此，一条 `ON SELECT` 规则实际上把表变成了一个视图，它的可见内容是由该规则的 `SELECT` 命令返回，而不是直接存在该表中的内容（如果有）。不过，使用 `CREATE VIEW` 命令还是要比创建一个真实表并且在其上定义一条 `ON SELECT` 规则更好。

可以通过定义 `ON INSERT` 、 `ON UPDATE` 以及 `ON DELETE` 规则（或者这些规则的任意子集）来创建可更新的视图，这些规则可以把视图上的更新动作替换为其他表上适当的更新动作。如果想要支持 `INSERT RETURNING` 等等，那么一定要在每一个这类规则中放上一个合适的 `RETURNING` 子句。

如果你尝试为复杂视图更新使用有条件的规则，有一点是很重要的：对于你希望在该视图上允许的每一个动作，必须有一条 `INSTEAD` 规则。如果该规则是有条件的，或者不是 `INSTEAD` ，那么系统仍将拒绝尝试执行该更新动作，因为它会认为在某些情况下它应该停止尝试在该视图的傀儡表上执行动作。如果你想处理有条件规则中的所有有用的情况，可以增加一条无条件的 `DO INSTEAD NOTHING` 规则来确保系统理解它将永远不会被调用来更新傀儡表。然后让有条件规则变成非- `INSTEAD` 。在它们适用的情况下，它们会加到默认的 `INSTEAD NOTHING` 动作（不过，当前这种方法不支持 `RETURNING` 查询）。

> **注意：**
> 
> 足够简单的视图自动就是可更新的（见 `CREATE VIEW` ），它们不需要依靠用户创建的规则来变成可更新的。不过还是可以创建一条显式规则，自动更新转换通常比显式规则效率高。
> 
> 另一种值得考虑的办法是使用 `INSTEAD OF` 触发器（见 `CREATE TRIGGER` ）代替规则。

**参数**

**`name`**

要创建的规则的名称。它必须与同一个表上任何其他规则的名称相区分。同一个表上同一种事件类型的多条规则会按照其名称的字符顺序被应用。

**`event`**

事件是 `SELECT` 、 `INSERT` 、 `UPDATE` 或者 `DELETE` 之一。注意包含 `ON CONFLICT` 子句的 `INSERT` 不能被用在具有 `INSERT` 或者 `UPDATE` 规则的表上。那种情况下请考虑使用可更新的视图。

**`table_name`**

规则适用的表或者视图的名称（可以是模式限定的）。

**`condition`**

任意的 SQL 条件表达式（返回 boolean）。该条件表达式不能引用除 `NEW` 以及 `OLD` 之外的任何表，并且不能包含聚集函数。

**`INSTEAD`**

`INSTEAD` 指示该命令应该取代原始命令被执行。

**`ALSO`**

`ALSO` 指示应该在原始命令之外执行这些命令。

如果 `ALSO` 和 `INSTEAD` 都没有被指定，默认是 `ALSO` 。

**`command`**

组成规则动作的命令。可用的命令有 `SELECT` 、 `INSERT` 、 `UPDATE` 、 `DELETE` 或者 `NOTIFY` 。

在 `condition` 和 `command` 中，名为 `NEW` 和 `OLD` 的表可以被用来引用被引用表中的值。在 `ON INSERT` 和 `ON UPDATE` 规则中， `NEW` 被用来引用被插入或者更新的新行。在 `ON UPDATE` 和 `ON DELETE` 规则中， `OLD` 被用来引用被更新或者删除的现有行。

**注解**

要在表上创建或者修改规则，必须是表的拥有者。

在一条用于视图上 `INSERT` 、 `UPDATE` 或者 `DELETE` 的规则中，可以增加一个 `RETURNING` 子句来发出视图的列。如果该规则被一个 `INSERT RETURNING` 、 `UPDATE RETURNING` 或者 `DELETE RETURNING` 命令触发，这个子句将被用来计算输出。当规则被一个没有 `RETURNING` 的命令触发时，该规则的 `RETURNING` 子句将被忽略。当前的实现只允许无条件 `INSTEAD` 规则包含 `RETURNING` 。此外，用于同一事件的所有规则中至多只能有一个 `RETURNING` 子句（这确保了只有一个候选 `RETURNING` 子句被用来计算结果）。如果在任何可用规则中都没有 `RETURNING` 子句，视图上的 `RETURNING` 查询将被拒绝。

避免循环规则非常重要。例如，尽管下面的两条规则定义都被瀚高数据库所接受， `SELECT` 命令将导致瀚高数据库报告一个错误，因为会产生一条规则的递归扩展：

```sql
CREATE RULE "_RETURN" AS
    ON SELECT TO t1
    DO INSTEAD
        SELECT * FROM t2;

CREATE RULE "_RETURN" AS
    ON SELECT TO t2
    DO INSTEAD
        SELECT * FROM t1;

SELECT * FROM t1;
```

当前，如果一个规则动作包含一个 `NOTIFY` 命令，该 `NOTIFY` 命令将被无条件执行，也就是说，即使该规则不被应用到任何行上，也会发出 `NOTIFY` 。例如，在

```sql
CREATE RULE notify_me AS ON UPDATE TO mytable DO ALSO NOTIFY mytable;

UPDATE mytable SET name = 'foo' WHERE id = 42;
```

中， `UPDATE` 期间将发出一个 `NOTIFY` 事件，不管是否有行匹配条件 `id = 42` 。这是一种实现限制，它可能会在未来的发行中被修复。

**兼容性**

`CREATE RULE` 是一种瀚高数据库语言扩展，整个查询重写系统也是这样。

**另见**

`ALTER RULE`, `DROP RULE`

## CREATE SCHEMA

— 定义一个新模式

**大纲**

```sql
CREATE SCHEMA schema_name [ AUTHORIZATION role_specification ] [ schema_element [...] ]

CREATE SCHEMA AUTHORIZATION role_specification [ schema_element [...] ]

CREATE SCHEMA IF NOT EXISTS schema_name [ AUTHORIZATION role_specification ]

CREATE SCHEMA IF NOT EXISTS AUTHORIZATION role_specification
```

其中 `role_specification` 可以是：

```
user_name
| CURRENT_USER
| SESSION_USER
```

**描述**

`CREATE SCHEMA` 输入一个新模式到当前数据库中。该模式名必须与当前数据库中任何现有模式的名称不同。

一个模式本质上是一个名字空间：它包含命令对象（表、数据类型、函数以及操作符），对象可以与在其他模式中存在的对象重名。可以通过用模式名作为一个前缀”限定”命名对象的名称来访问它们，或者通过把要求的模式包括在搜索路径中来访问命名对象。

一个指定非限定对象名的 `CREATE` 命令在当前模式（搜索路径中的第一个模式，由函数 `current_schema` 决定）中创建对象。

`CREATE SCHEMA` 中可以选择包括子命令用以在新模式中创建对象。这些子命令实际被当做独立的在创建该模式后被发出的命令一样，除非使用 `AUTHORIZATION` 子句，所有被创建的对象都会由该用户拥有。

**参数**

**`schema_name`**

要创建的一个模式名。如果省略， `user_name` 将被用作模式名。该名称不能以 `pg_` 开始，因为这样的名称是用作系统模式的。

**`user_name`**

将拥有新模式的用户的角色名。如果省略，默认为执行该命令的用户。要创建由另一个角色拥有的角色，你必须是那个角色的一个直接或者间接成员，或者是一个超级用户。

**`schema_element`**

要在该模式中创建的对象的定义 SQL 语句。当前，只有 `CREATE TABLE` 、 `CREATE VIEW` 、 `CREATE INDEX` 、 `CREATE SEQUENCE` 、 `CREATE TRIGGER` 以及 `GRANT` 被接受为 `CREATE SCHEMA` 中的子句。其他类型的对象可以在模式被创建之后用单独的命令创建。

**`IF NOT EXISTS`**

如果一个具有同名的模式已经存在，则什么也不做（不过发出一个提示）。使用这个选项时不能包括 `schema_element` 子命令。

**注解**

要创建一个模式，调用用户必须拥有当前数据库的 `CREATE` 特权（当然，超级用户可以绕过这种检查）。

**示例**

创建一个模式：

```sql
CREATE SCHEMA myschema;
```

为用户 `joe` 创建一个模式，该模式也将被命名为 `joe` ：

```sql
CREATE SCHEMA AUTHORIZATION joe;
```

创建一个被用户 `joe` 拥有的名为 `test` 的模式，除非已经有一个名为 `test` 的模式（不管 `joe` 是否拥有该已经存在的模式）。

```sql
CREATE SCHEMA IF NOT EXISTS test AUTHORIZATION joe;
```

创建一个模式并且在其中创建一个表和视图：

```sql
CREATE SCHEMA hollywood
    CREATE TABLE films (title text, release date, awards text[])
    CREATE VIEW winners AS
        SELECT title, release FROM films WHERE awards IS NOT NULL;
```

注意子命令不以分号结束。

下面是达到相同结果的等效的方法：

```sql
CREATE SCHEMA hollywood;
CREATE TABLE hollywood.films (title text, release date, awards text[]);
CREATE VIEW hollywood.winners AS
    SELECT title, release FROM hollywood.films WHERE awards IS NOT NULL;
```

**兼容性**

SQL 标准允许在 `CREATE SCHEMA` 中有一个 `DEFAULT CHARACTER SET` 子句，以及当前瀚高数据库接受的更多子命令类型。

SQL 标准制定 `CREATE SCHEMA` 中的子命令可以以任何顺序出现。当前的瀚高数据库实现不能处理子命令中所有情况的向前引用。有时候可能有必要对子命令进行重排序以避免向前引用。

根据 SQL 标准，模式的拥有者总是拥有其中的所有对象。瀚高数据库允许模式包含非模式拥有者所拥有的对象。只有模式拥有者把其模式上的 `CREATE` 特权授予给了其他人或者一个超级用户选择在该模式中创建对象时才会发生这种事情。

`IF NOT EXISTS` 选项是一种瀚高数据库扩展。

**另见**

`ALTER SCHEMA`, `DROP SCHEMA`

## CREATE SEQUENCE

— 定义一个新的序列发生器

**大纲**

```sql
CREATE [ TEMPORARY | TEMP ] SEQUENCE [ IF NOT EXISTS ] name 
    [ INCREMENT [ BY ] increment ]
    [ MINVALUE minvalue | NO MINVALUE ] 
    [ MAXVALUE maxvalue | NO MAXVALUE ]
    [ START [ WITH ] start ] 
    [ CACHE cache ] 
    [ [ NO ] CYCLE ]
    [ OWNED BY { table_name.column_name | NONE } ]
```

**描述**

`CREATE SEQUENCE` 创建一个新的序列数发生器。这涉及到用名称 `name` 创建并且初始化一个新的特殊的单行表。该发生器将由发出该命令的用户所拥有。

如果给出一个模式名称，则该序列将将被创建在指定的模式中。否则它会被创建在当前模式中。临时序列存在于一个特殊的模式中，因此在创建临时序列时不能给出模式名。序列名称必须与同一模式中任何其他序列、表、索引、视图或者外部表的名称不同。

在序列被创建后，可以使用函数 `nextval` 、 `currval` 以及 `setval` 来操作该序列。尽管无法直接更新一个序列，可以使用这样的查询：

```sql
SELECT * FROM name;
```

来检查一个序列的参数以及当前状态。特别地，序列的 `last_value` 域显示被任意会话最后一次取得的值（当然，在被打印时该值可能已经过时了，因为可能有其他会话正在执行 `nextval` 调用）。

**参数**

**`TEMPORARY`** 或 **`TEMP`**

如果被指定，只会为这个会话创建序列对象，并且在会话退出时自动删除它。当临时序列存在时，已有的同名永久序列（在这个会话中）会变得不可见，不过可以用模式限定的名称来引用同名永久序列。

**`IF NOT EXISTS`**

如果已经存在一个同名的关系时不要抛出错误。这种情况下会发出一个提示。注意这不保证现有的关系与即将创建的序列相似——它甚至可能都不是一个序列。

**`name`**

要创建的序列的名称（可以是模式限定的）。

**`data_type`**

可选的子句 `AS data_type` 制定序列的数据类型。有效类型是 `smallint` 、 `integer` 和 `bigint` 。默认是 `bigint` 。数据类型决定了序列的默认最小和最大值。

**`increment`**

可选的子句 `INCREMENT BY increment` 指定为了创建新值会把哪个值加到当前序列值上。

一个正值将会创造一个上升序列，负值会创造一个下降序列。默认值是 1。

**`minvalue`**  
**`NO MINVALUE`**

可选的子句 `MINVALUE minvalue` 决定一个序列能产生的最小值。如果没有提供这个子句或者指定了 `NO MINVALUE` ，那么会使用默认值。升序序列的默认值为 1。降序序列的默认值为数据类型的最小值。

**`maxvalue`**  
**`NO MAXVALUE`**

可选的子句 `MAXVALUE maxvalue` 决定该序列的最大值。如果没有提供这个子句或者指定了 `NO MAXVALUE` ，那么将会使用默认值。升序序列的默认值是数据类型的最大值。降序序列的默认值是 -1。

**`start`**

可选的子句 `START WITH start` 允许序列从任何地方开始。对于上升序列和下降序列来说，默认的开始值分别是 `minvalue` 和 `maxvalue` 。

**`cache`**

可选的子句 `CACHE cache` 指定要预分配多少个序列数并且把它们放在内存中以便快速访问。最小值为 1（一次只生成一个值，即没有缓存），默认值也是 1。

**`CYCLE`**  
**`NO CYCLE`**

对于上升序列和下降序列， `CYCLE` 选项允许序列在分别达到 `maxvalue` 和 `minvalue` 时回卷。如果达到该限制，下一个产生的数字将分别是 `minvalue` 和 `maxvalue` 。

如果指定了 `NO CYCLE` ，当序列到达其最大值后任何 `nextval` 调用将返回一个错误。如果 `CYCLE` 和 `NO CYCLE` 都没有被指定，则默认为 `NO CYCLE` 。

**`OWNED BY table_name.column_name`**  
**`OWNED BY NONE`**

`OWNED BY` 选项导致序列被与一个特定的表列关联在一起，这样如果该列（或者整个表）被删除，该序列也将被自动删除。指定的表必须和序列具有相同的拥有者并且在同一个模式中。默认选项 `OWNED BY NONE` 指定该序列不与某个列关联。

**注解**

使用 `DROP SEQUENCE` 移除一个序列。

序列是基于 `bigint` 算法的，因此范围是不能超过一个八字节整数的范围（-9223372036854775808 到 9223372036854775807）。

由于 `nextval` 和 `setval` 调用绝不会回滚，如果需要序数的”无间隙”分配，则不能使用序列对象。可以通过在一个只包含一个计数器的表上使用排他锁来构建无间隙的分配，但是这种方案比序列对象开销更大，特别是当有很多事务并发请求序数时。

如果对一个将由多个会话并发使用的序列对象使用了大于 1 的 `cache` 设置，可能会得到意想不到的结果。每个会话会在访问该序列对象时分配并且缓存后续的序列值，并且相应地增加该序列对象的 `last_value` 。然后，在该会话中下一次 `nextval` 会做 `cache-1` ，并且简单地返回预分配的值而不修改序列对象。因此，任何已分配但没有在会话中使用的数字将会在该会话结束时丢失，导致该序列中的”空洞”。

进一步，尽管多个会话能分配到不同的序列值，这些值可能会在所有会话都被考虑时生成出来。例如， `cache` 的设置为 10，会话 A 可能储存值 1..10 并且返回 `nextval=1` ，然后会话 B 可能储存值 11..20 并且在 A 生成 `nextval=2` 之前返回 `nextval=11` 。因此，如果 `cache` 设置为 1，可以安全地假设 `nextval` 值被顺序地生成。如果 `cache` 设置大于 1，就只能假定 `nextval` 值都是可区分的，但不能保证它们被完全地顺序生成。还有， `last_value` 将反映服务于任意会话的最后一个值，不管它是否已经被 `nextval` 返回过。

另一个考虑是，在这样一个序列上执行的 `setval` 将不会通知其他会话，直到它们用尽了任何已缓存的预分配值。

**示例**

创建一个称作 `serial` 的上升序列，从 101 开始：

```sql
CREATE SEQUENCE serial START 101;
```

从这个序列中选取下一个数字：

```sql
SELECT nextval('serial');
 nextval
---------
     101
```

再从这个序列中选取下一个数字：

```sql
SELECT nextval('serial');
 nextval
---------
     102
```

在一个 `INSERT` 命令中使用这个序列：

```sql
INSERT INTO distributors VALUES (nextval('serial'), 'nothing');
```

在一次 `COPY FROM` 后更新新列值：

```sql
BEGIN;
COPY distributors FROM 'input_file';
SELECT setval('serial', max(id)) FROM distributors;
END;
```

**兼容性**

`CREATE SEQUENCE` 符合 SQL 标准，不过下列除外：

- 使用 `nextval()` 而不是标准的 `NEXT VALUE FOR` 表达式获取下一个值。
- `OWNED BY` 子句是一种瀚高数据库扩展。

**另见**

`ALTER SEQUENCE,` `DROP SEQUENCE`

## CREATE SERVER

— 定义一个新的外部服务器

**大纲**

```sql
CREATE SERVER [ IF NOT EXISTS ] server_name [ TYPE 'server_type' ] [ VERSION 'server_version' ]
FOREIGN DATA WRAPPER fdw_name
[ OPTIONS ( option 'value' [, ... ] ) ]
```

**描述**

CREATE SERVER定义一个新的外部服务器。定义该服务器的用户会成为拥有者。

外部服务器通常包装了外部数据包装器用来访问一个外部数据源所需的连接信息。额外的用户相关的连接信息可以通过用户映射的方式来指定。

服务器名称在数据库中必须唯一。

创建服务器要求所使用的外部数据包装器上的USAGE特权。

**参数**

**IF NOT EXISTS**

如果已经存在同名的服务器，不要抛出错误。在这种情况下发出一个通知。 请注意，不能保证现有服务器与要创建的服务器类似。

**server\_name**

要创建的外部服务器的名称。

**server\_type**

可选的服务器类型，可能对外部数据包装器有用。

**server\_version**

可选的服务器版本，可能对外部数据包装器有用。

**fdw\_name**

管理该服务器的外部数据包装器的名称。

**OPTIONS ( option ‘value’ \[, … \] )**

这个子句为服务器指定选项。这些选项通常定义该服务器的连接细节， 但是实际的名称和值取决于该服务器的外部数据包装器。

**注解**

在使用dblink模块时，一个外部服务器的名称可以被 用作 `dblink_connect` 函数的一个参数来指示 连接参数。以这种方式使用外部服务器，需要在其上具有 USAGE特权。

**示例**

创建使用外部数据包装器 `postgres_fdw` 的服务器 `myserver` ：

```sql
CREATE SERVER myserver FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host 'foo', dbname 'foodb', port '5432');
```

详见 `postgres_fdw` 。

**兼容性**

CREATE SERVER符合 ISO/IEC 9075-9 (SQL/MED)。

**另见**

ALTER SERVER, DROP SERVER, CREATE FOREIGN DATA WRAPPER, CREATE FOREIGN TABLE, CREATE USER MAPPING

## CREATE STATISTICS

— 定义扩展统计

**大纲**

```sql
CREATE STATISTICS [ IF NOT EXISTS ] statistics_name
[ ( statistics_kind [, ... ] ) ]
ON column_name, column_name [, ...]
FROM table_name
```

**描述**

CREATE STATISTICS将创建一个新的扩展统计对象， 追踪指定表、外部表或物化视图的数据。该统计对象将在当前数据库中创建， 被发出该命令的用户所有。

如果给定了模式名（比如， `CREATE STATISTICS myschema.mystat ...`）， 那么在给定的模式中创建统计对象。否则在当前模式中创建。 统计对象的名称必须与相同模式中的任何其他统计对象不同。

**参数**

**IF NOT EXISTS**

如果具有相同名称的统计对象已经存在，不会抛出一个错误，只会发出一个提示。 请注意，这里只考虑统计对象的名称，不考虑其定义细节。

**statistics\_name**

要创建的统计对象的名称（可以有模式限定）。

**statistics\_kind**

在此统计对象中计算的统计种类。目前支持的种类是启用n-distinct统计的 `ndistinct` ，启用功能依赖性统计的 `dependencies` ，以及启用最常见的值列表的 `mcv` 。 如果省略该子句，则统计对象中将包含所有支持的统计类型。

**column\_name**

被计算的统计信息包含的表格列的名称。至少必须给出两个列名，列名的顺序可以忽略。

**table\_name**

包含计算统计信息的列的表的名称（可以是模式限定的）。

**注解**

你必须是表的所有者才能创建读取它的统计对象。不过，一旦创建， 统计对象的所有权与基础表无关。

**示例**

用两个功能相关的列创建表 `t1` ， 即第一列中的值的信息足以确定另一列中的值。然后， 在这些列上构建函数依赖关系统计信息：

```sql
CREATE TABLE t1 (
    a int,
    b int
);

INSERT INTO t1 SELECT i/100, i/500
FROM generate_series(1,1000000) s(i);

ANALYZE t1;

-- 匹配行的数量将被大大低估：
EXPLAIN ANALYZE SELECT * FROM t1 WHERE (a = 1) AND (b = 0);

CREATE STATISTICS s1 (dependencies) ON a, b FROM t1;

ANALYZE t1;

-- 现在行计数估计会更准确：
EXPLAIN ANALYZE SELECT * FROM t1 WHERE (a = 1) AND (b = 0);
```

如果没有函数依赖性统计，规划器会认为两个WHERE条件是独立的，并且会将它们的选择性乘以一起，以致得到太小的行数估计。 通过这样的统计，规划器认识到WHERE条件是多余的，并且不会低估行数。

创建表 `t2` 与两个完全相关的列(包含相同的数据)，并且在这些列上创建一个MCV列表:

```sql
CREATE TABLE t2 (
    a int,
    b int
);

INSERT INTO t2 SELECT mod(i,100), mod(i,100)
FROM generate_series(1,1000000) s(i);

CREATE STATISTICS s2 (mcv) ON a, b FROM t2;

ANALYZE t2;

-- valid combination (found in MCV)
EXPLAIN ANALYZE SELECT * FROM t2 WHERE (a = 1) AND (b = 1);

-- invalid combination (not found in MCV)
EXPLAIN ANALYZE SELECT * FROM t2 WHERE (a = 1) AND (b = 2);
```

MCV列表为计划器提供了关于表中普遍出现的特定值的更详细的信息，以及表中未显示的值组合的选择性上限，允许它在这两种情况下产生更好的估计值。

**兼容性**

SQL标准中没有CREATE STATISTICS命令。

**又见**

ALTER STATISTICS, DROP STATISTICS

## CREATE SUBSCRIPTION

— 定义一个新的订阅

**大纲**

```sql
CREATE SUBSCRIPTION subscription_name
CONNECTION 'conninfo'
PUBLICATION publication_name [, ...]
[ WITH ( subscription_parameter [= value] [, ... ] ) ]
```

**描述**

CREATE SUBSCRIPTION为当前数据库添加一个新的订阅。 订阅名称必须与数据库中任何现有的订阅不同。

订阅表示到发布者的复制连接。因此，此命令不仅在本地目录中添加定义， 还会在发布者上创建复制插槽。

在运行此命令的事务提交时，将启动逻辑复制工作器以复制新订阅的数据。

**参数**

**subscription\_name**

新订阅的名称。

**CONNECTION ‘conninfo’**

连接字符串，详细信息请参考第 33.1.1 节。

**PUBLICATION publication\_name**

要订阅的发布者上的发布名称。

**WITH ( subscription\_parameter \[= value\] \[, … \] )**

该子句指定订阅的可选参数。支持的参数有：

**copy\_data (boolean)**

指定在复制启动后是否应复制正在订阅的发布中的现有数据。默认值是 `true` 。

**create\_slot (boolean)**

指定该命令是否要在发布者上创建复制槽。默认值是 `true` 。

**enabled (boolean)**

指定订阅是否应该主动复制，或者是否应该只是设置，但尚未启动。默认值是 `true` 。

**slot\_name (string)**

要使用的复制插槽的名称。默认行为是使用订阅名称作为插槽的名称。

当 `slot_name` 设置为 `NONE` 时， 将不会有复制槽与订阅关联。这在需要稍后手动设置复制槽的情况下会使用。 这样的订阅必须同时 `enabled` 并且 `create_slot` 设置为 `false` 。

**synchronous\_commit (enum)**

该参数的值会覆盖 `synchronous_commit` 设置。 默认值是 `off` 。

对于逻辑复制使用 `off` 是安全的： 如果订阅者由于缺少同步而丢失事务，数据将从发布者重新发送。

进行同步逻辑复制时，不同的设置可能是合适的。 逻辑复制工作者向发布者报告写入和刷新的位置，当使用同步复制时， 发布者将等待实际刷新。这意味着，当订阅用于同步复制时，将订阅者的 `synchronous_commit` 设置为 `off` 可能会增加发布服务器上 `COMMIT` 的延迟。 在这种情况下，将 `synchronous_commit` 设置为 `local` 或更高是有利的。

**connect (boolean)**

指定 `CREATE SUBSCRIPTION` 是否应该连接到发布者。 将其设置为 `false` 将会改变默认值 `enabled` 、 `create_slot` 和 `copy_data` 为 `false` 。

不允许将 `connect` 设置为 `false` 的同时将 `enabled` 、 `create_slot` 或 `copy_data` 设置为 `true` 。

因为该选项设置为 `false` 时不会建立连接， 因此表没有被订阅，所以当启用订阅后，不会复制任何内容。 需要运行 `ALTER SUBSCRIPTION ... REFRESH PUBLICATION` 才能订阅表。

**注解**

创建复制槽时(默认行为), `CREATE SUBSCRIPTION` 不能在事务块内部执行。

如果复制插槽不是作为同一命令的一部分创建的，则创建连接到相同数据库集群的订阅（例如，在同一集群中的数据库之间进行复制或在同一个数据库中进行复制）只能成功否则， `CREATE SUBSCRIPTION` 调用将挂起。要做到这一点， 单独创建复制插槽（使用函数 `pg_create_logical_replication_slot` 和插件名称 `pgoutput` ），并使用参数 `create_slot = false` 创建订阅。这是一个实施限制，可能会在未来的版本中解除。

**示例**

创建一个到远程服务器的订阅，复制发布 `mypublication` 和 `insert_only` 中的表，并在提交时立即开始复制：

```sql
CREATE SUBSCRIPTION mysub
CONNECTION 'host=192.168.1.50 port=5432 user=foo dbname=foodb'
PUBLICATION mypublication, insert_only;
```

创建一个到远程服务器的订阅，复制 `insert_only` 发布中的表， 并且不开始复制直到稍后启用复制。

```sql
CREATE SUBSCRIPTION mysub
CONNECTION 'host=192.168.1.50 port=5432 user=foo dbname=foodb'
PUBLICATION insert_only
WITH (enabled = false);
```

**兼容性**

CREATE SUBSCRIPTION是一个瀚高数据库扩展。

**又见**

ALTER SUBSCRIPTION, DROP SUBSCRIPTION, CREATE PUBLICATION, ALTER PUBLICATION

## CREATE TABLE

— 定义一个新表

**大纲**

```sql
CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ] table_name ( [
    { column_name data_type [ COLLATE collation ] [ column_constraint [ ... ] ]
    | table_constraint
    | LIKE source_table [ like_option ... ] }
    [, ... ]
] )
[ INHERITS ( parent_table [, ... ] ) ]
[ PARTITION BY { RANGE | LIST | HASH } ( { column_name | ( expression ) } [ COLLATE collation ] [ opclass ] [, ... ] ) ]
[ USING method ]
[ WITH ( storage_parameter [= value] [, ... ] ) | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]

CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ] table_name
OF type_name [ (
    { column_name [ WITH OPTIONS ] [ column_constraint [ ... ] ]
    | table_constraint }
    [, ... ]
) ]
[ PARTITION BY { RANGE | LIST | HASH } ( { column_name | ( expression ) } [ COLLATE collation ] [ opclass ] [, ... ] ) ]
[ USING method ]
[ WITH ( storage_parameter [= value] [, ... ] ) | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]

CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ] table_name
PARTITION OF parent_table [ (
    { column_name [ WITH OPTIONS ] [ column_constraint [ ... ] ]
    | table_constraint }
    [, ... ]
) ] { FOR VALUES partition_bound_spec | DEFAULT }
[ PARTITION BY { RANGE | LIST | HASH } ( { column_name | ( expression ) } [ COLLATE collation ] [ opclass ] [, ... ] ) ]
[ USING method ]
[ WITH ( storage_parameter [= value] [, ... ] ) | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]
```

其中 **column\_constraint** 是：

```sql
[ CONSTRAINT constraint_name ]
{ NOT NULL |
  NULL |
  CHECK ( expression ) [ NO INHERIT ] |
  DEFAULT default_expr |
  GENERATED ALWAYS AS ( generation_expr ) STORED |
  GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY [ ( sequence_options ) ] |
  UNIQUE index_parameters |
  PRIMARY KEY index_parameters |
  REFERENCES reftable [ ( refcolumn ) ] [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ]
    [ ON DELETE referential_action ] [ ON UPDATE referential_action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
```

**table\_constraint** 是：

```sql
[ CONSTRAINT constraint_name ]
{ CHECK ( expression ) [ NO INHERIT ] |
  UNIQUE ( column_name [, ... ] ) index_parameters |
  PRIMARY KEY ( column_name [, ... ] ) index_parameters |
  EXCLUDE [ USING index_method ] ( exclude_element WITH operator [, ... ] ) index_parameters [ WHERE ( predicate ) ] |
  FOREIGN KEY ( column_name [, ... ] ) REFERENCES reftable [ ( refcolumn [, ... ] ) ]
    [ MATCH FULL | MATCH PARTIAL | MATCH SIMPLE ] [ ON DELETE referential_action ] [ ON UPDATE referential_action ] }
[ DEFERRABLE | NOT DEFERRABLE ] [ INITIALLY DEFERRED | INITIALLY IMMEDIATE ]
```

**like\_option** 是：

```sql
{ INCLUDING | EXCLUDING } { COMMENTS | CONSTRAINTS | DEFAULTS | GENERATED | IDENTITY | INDEXES | STATISTICS | STORAGE | ALL }
```

**partition\_bound\_spec** 是：

```sql
IN ( partition_bound_expr [, ...] ) |
FROM ( { partition_bound_expr | MINVALUE | MAXVALUE } [, ...] ) 
  TO ( { partition_bound_expr | MINVALUE | MAXVALUE } [, ...] ) |
WITH ( MODULUS numeric_literal, REMAINDER numeric_literal )
```

**UNIQUE** 、 **PRIMARY KEY** 以及 **EXCLUDE** 约束中的 **index\_parameters** 是：

```sql
[ INCLUDE ( column_name [, ... ] ) ]
[ WITH ( storage_parameter [= value] [, ... ] ) ]
[ USING INDEX TABLESPACE tablespace_name ]
```

一个 **EXCLUDE** 约束中的 **exclude\_element** 是：

```sql
{ column_name | ( expression ) } [ opclass ] [ ASC | DESC ] [ NULLS { FIRST | LAST } ]
```

**描述**

CREATE TABLE将在当前数据库中创建一个新的、初始为空的表。该表将由发出该命令的用户所拥有。

如果给定了一个模式名（例如 `CREATE TABLE myschema.mytable ...`），那么该表被创建在指定的模式中。否则它被创建在当前模式中。临时表存在于一个特殊的模式中，因此在创建一个临时表时不能给定一个模式名。该表的名称必须与同一个模式中的任何其他表、序列、索引、视图或外部表的名称区分开。

CREATE TABLE也会自动地创建一个数据类型来表示对应于该表一行的组合类型。因此，表不能用同一个模式中任何已有数据类型的名称。

可选的约束子句指定一个插入或更新操作要成功，新的或更新过的行必须满足的约束（测试）。一个约束是一个SQL对象，它帮助以多种方式定义表中的合法值集合。

有两种方式来定义约束：表约束和列约束。一个列约束会作为列定义的一部分定义。一个表约束定义不与一个特定列绑定，并且它可以包含多于一个列。每一个列约束也可以被写作一个表约束，列约束只是一种当约束只影响一列时方便书写的记号习惯。

要能创建一个表，你必须分别具有所有列类型或OF子句中类型的USAGE特权。

**参数**

**TEMPORARY or TEMP**

如果指定，该表被创建为一个临时表。临时表会在会话结束时自动被删除，或者也可以选择在当前事务结束时删除（见下文的 `ON COMMIT` ）。当临时表存在时，已有的同名持久表将对于当前会话不可见，不过可以使用模式限定的名称进行引用。在一个临时表上创建的任何索引也自动地变为临时的。

自动清理守护进程不能访问并且因此也不能清理或分析临时表。由于这个原因，应该通过会话的 SQL 命令执行合适的清理和分析操作。例如，如果一个临时表将要被用于复杂的查询，最好在把它填充完毕后在其上运行 `ANALYZE` 。

可以选择将 `GLOBAL` 或 `LOCAL` 写在 `TEMPORARY` 或 `TEMP` 的前面。这当前在瀚高数据库中没有区别并且已被废弃，见Compatibility。

**UNLOGGED**

如果指定，该表被创建为一个不受日志记录的表。被写入到不做日志的表中的数据不会被写到预写式日志中，这让它们比普通表快非常多。不过，它们在崩溃时是不安全的：一个不做日志的表在一次崩溃或非干净关闭之后会被自动地截断。一个不做日志的表中的内容也不会被复制到后备服务器中。在一个不做日志的表上创建的任何索引也会自动地不被日志记录。

**IF NOT EXISTS**

如果一个同名关系已经存在，不要抛出一个错误。在这种情况下会发出一个提示。注意这不保证现有的关系是和将要被创建的表相似的东西。

**table\_name**

要被创建的表名（可以选择用模式限定）。

**OF type\_name**

创建一个类型化的表，它的结构取自于指定的组合类型（名字可以选择用模式限定）。

一个类型化的表和它的类型绑定在一起，例如如果类型被删除，该表也将被删除（用 `DROP TYPE ... CASCADE` ）。

当一个类型化的表被创建时，列的数据类型由底层的组合类型决定而没有在 `CREATE TABLE` 命令中直接指定。但是 `CREATE TABLE` 命令可以对表增加默认值和约束，并且可以指定存储参数。

**column\_name**

列的名称会在新表中被建立。

**data\_type**

列的数据类型。这可以包括数组规格。

**COLLATE collation**

`COLLATE` 子句为该列（必须是一种可排序数据类型）赋予一个排序规则。如果没有指定，将使用该列数据类型的默认排序规则。

**INHERITS ( parent\_table \[, … \] )**

可选的 `INHERITS` 子句指定一个表的列表，新表将从其中自动地继承所有列。父表可以是普通表或者外部表。

`INHERITS` 的使用在新的子表和它的父表之间创建一种持久的关系。对于父表的模式修改通常也会传播到子表，并且默认情况下子表的数据会被包括在对父表的扫描中。

如果在多个父表中存在同名的列，除非父表中每一个这种列的数据类型都能匹配，否则会报告一个错误。如果没有冲突，那么重复列会被融合来形成新表中的一个单一列。如果新表中的列名列表包含一个也是继承而来的列名，该数据类型必须也匹配继承的列，并且列定义会被融合成一个。如果新表显式地为列指定了任何默认值，这个默认值将覆盖来自该列继承声明中的默认值。否则，任何父表都必须为该列指定相同的默认值，或者会报告一个错误。

`CHECK` 约束本质上也采用和列相同的方式被融合：如果多个父表或者新表定义中包含相同的命名 `CHECK` 约束，这些约束必须全部具有相同的检查表达式，否则将报告一个错误。具有相同名称和表达式的约束将被融合成一份拷贝。一个父表中的被标记为 `NO INHERIT` 的约束将不会被考虑。注意新表中一个未命名的 `CHECK` 约束将永远不会被融合，因为那样总是会为它选择一个唯一的名字。

列的 `STORAGE` 设置也会从父表复制过来。

如果父表中的列是标识列，那么该属性不会被继承。如果需要，可以将子表中的列声明为标识列。

**PARTITION BY { RANGE | LIST | HASH } ( { column\_name | ( expression ) } \[ opclass \] \[, …\] )**

可选的 `PARTITION BY` 子句指定了对表进行分区的策略。这样创建的表称为分区表。带括号的列或表达式的列表构成表的分区键。使用范围或哈希分区时，分区键可以包含多个列或表达式（最多32个，但在构建瀚高数据库时可以更改此限制），但对于列表分区，分区键必须由单个列或表达式组成。

范围和列表分区需要btree运算符类，而哈希分区需要哈希运算符类。如果没有运算符类被显式指定，将使用相应类型的默认运算符类; 如果不存在默认运算符类，则将引发错误。使用哈希分区时，所使用的运算符类必须实现支持功能 2。

分区表被分成多个子表（称为分区），它们是使用单独的 `CREATE TABLE` 命令创建的。分区表本身是空的。插入到表中的数据行将根据分区键中的列或表达式的值路由到分区。如果没有现有的分区与新行中的值匹配，则会报告错误。

分区表不支持 `EXCLUDE` 约束；但是，你可以在各个分区上定义这些约束。

**PARTITION OF parent\_table { FOR VALUES partition\_bound\_spec | DEFAULT }**

将表创建为指定父表的分区。该表建立时，可以使用 `FOR VALUES` 创建为特定值的分区，也可以使用 `DEFAULT` 创建默认分区。

`partition_bound_spec` 必须对应于父表的分区方法和分区键，并且必须不能与该父表的任何现有分区重叠。具有 `IN` 的形式用于列表分区，具有 `FROM` 和 `TO` 的形式用于范围分区，具有 `WITH` 的形式用于哈希分区。

`partition_bound_expr` 是任何无变量表达式（不允许子查询、窗口函数、聚合函数和集返回函数）。它的数据类型必须与相应分区键列的数据类型相匹配。表达式在表创建时只计算一次，因此它甚至可以包含易失性表达式，如 `CURRENT_TIMESTAMP` 。

在创建列表分区时，可以指定 `NULL` 来表示分区允许分区键列为空。但是，给定父表不能有多于一个这样的列表分区。无法为范围分区指定 NULL。

创建范围分区时，由 `FROM` 指定的下限是一个包含范围，而用 `TO` 指定的上限是排除范围。

也就是说，在 `FROM` 列表中指定的值是该分区的相应分区键列的有效值，而 `TO` 列表中的值不是。请注意，必须根据按行比较的规则来理解此语句。例如，给定 `PARTITION BY RANGE (x,y)` ，分区范围 `FROM (1, 2) TO (3, 4)` 允许 `x=1` 与任何 `y>=2` ， `x=2` 与任何非空 `y` ，和 `x=3` 与任何 `y<4` 。

在创建范围分区以指示列值没有下限或上限时，可以使用特殊值 `MINVALUE` 和 `MAXVALUE` 。

例如，使用 `FROM (MINVALUE) TO (10)` 定义的分区允许任何小于10的值，并且使用 `FROM (10) TO (MAXVALUE)` 定义的分区允许任何大于或等于10的值。

创建涉及多个列的范围分区时，将 `MAXVALUE` 作为下限的一部分并将 `MINVALUE` 作为上限的一部分也是有意义的。例如，使用 `FROM (0, MAXVALUE) TO (10, MAXVALUE)` 定义的分区允许第一个分区键列大于0且小于或等于10的任何行。类似地，使用 `FROM ('a', MINVALUE) TO ('b', MINVALUE)` 定义的分区允许第一个分区键列以”a”开头的任何行。

请注意，如果 `MINVALUE` 或 `MAXVALUE` 用于分区边界的一列，则必须为所有后续列使用相同的值。例如， `(10, MINVALUE, 0)` 不是有效的边界；你应该写 `(10, MINVALUE, MINVALUE)` 。

还要注意，某些元素类型，如 `timestamp` ，具有”无穷”的概念，这只是另一个可以存储的值。这与 `MINVALUE` 和 `MAXVALUE` 不同，它们不是可以存储的实际值，而是它们表示值无界的方式。 `MAXVALUE` 可以被认为比任何其他值（包括”无穷”）都大的值， `MINVALUE` 可以被认为是比任何其他值（包括”负无穷”）都小的值。因此，范围 `FROM ('infinity') TO (MAXVALUE)` 不是空的范围；它只允许存储一个值——“infinity”。

如果指定了 `DEFAULT` ，则表将创建为父表的默认分区。此选项不适用于哈希分区表。不适合给定父级表的任何其他分区的分区键值将路由到默认分区。

当一个表已有 `DEFAULT` 分区并且要对它添加新分区时，必须扫描默认分区以验证它不包含可能属于新分区的任何行。如果默认分区包含大量行，则速度可能会很慢。如果默认分区是外表或者它具有可证明的不可能包含能放置在新分区中的行的约束，则将略过扫描当创建哈希分区时，必须指定模数和余数。模数必须是正整数，余数必须是小于模数的非负整数。通常情况下，当初始设置哈希分区表时，应选择一个与分区数相等的模数，并为每个表分配相同的模数和不同的余数（请参阅下方示例）。不过，并不要求每个分区都具有相同的模数，只要求哈希分区表里面的分区中出现的每个模数都是下一个较大模数的因数。这允许以增量的方式增加分区数量而不需要一次移动所有数据。例如，假设你有一个包含 8 个分区的哈希分区表，每个分区有模数8，但发现有必要将分区数增加到 16 个。您可以拆分其中一个模数-8分区，然后创建两个新的模数-16分区来覆盖键空间的相同部分（一个的余数等于被拆分的分区的余数，另一个的余数等于该值加8），而后用数据重新填充他们。然后，你可以对每一个余数-8分区重复此操作过程，直到没有剩余。虽然这其中的每个步骤都可能会导致大量的数据移动操作，它仍然要好于建一个全新的表并一次移动全部数据。

分区必须与其所属的分区表的字段名和类型相同。对分区表字段名或类型的修改，将自动传播到所有分区。 `CHECK` 约束将自动被每一个分区继承，但是单独的分区可以指定额外的 `CHECK` 约束；与父表相同名称和条件的额外约束将被父表约束合并。可以为每个分区分别指定默认值。但是请注意，在通过分区表插入元组时不会应用分区的默认值。

插入分区表中的行将自动路由到正确的分区。如果不存在合适的分区，则会发生错误。

像 `TRUNCATE` 这样的操作通常会影响一个表及其所有继承子级，这些操作将级联到所有分区，但也可能在单个分区上执行。请注意，使用 `DROP TABLE` 删除分区需要在父表上采用 `ACCESS EXCLUSIVE` 锁。

**LIKE source\_table \[ like\_option … \]**

`LIKE` 指定新表将从哪一个表自动地复制所有的列名、数据类型以及它们的非空约束。

和 `INHERITS` 不同，新表和原始表在创建完成之后是完全分离的。对原始表的更改将不会被应用到新表，并且不可能在原始表的扫描中包括新表的数据。

同样与 `INHERITS` 不同，用 `LIKE` 拷贝的列和约束不会和相似的命名列及约束融合。如果显式指定了相同的名称或者在另一个 `LIKE` 子句中指定了相同的名称，将会发出一个错误。

可选的 `like_option` 子句指定要复制的原始表的附加属性。指定 `INCLUDING` 复制该属性,指定 `EXCLUDING` 忽略该属性。 `EXCLUDING` 为默认值。如果对同一类型的对象指定了多个规范，则使用最后一个规范。可用的选项包括：

**INCLUDING COMMENTS**

复制的列、约束和索引的注释将被复制。默认行为是去除注释，从而导致新表中复制的列和约束没有注释。

**INCLUDING CONSTRAINTS**

`CHECK` 约束将被复制。列约束和表约束之间没有区别。非空约束始终复制到新表。

**INCLUDING DEFAULTS**

复制列定义的默认表达式将被复制。否则，不会复制默认表达式，从而导致新表中复制的列具有空默认值。注意，复制调用数据库修改函数的默认值，例如 `nextval` ，可能在原始表和新表之间创建功能联系。

**INCLUDING GENERATED**

列定义的任何生成表达式将被复制。默认情况下，新列将是常规基本列。

**INCLUDING IDENTITY**

已复制列定义的任何标识规范都将被复制。为新表的每个标识列创建一个新序列，与与旧表关联的序列分开。

**INCLUDING INDEXES**

原始表上的索引、 `PRIMARY KEY` 、 `UNIQUE` 和 `EXCLUDE` 约束将被建立在新表上。根据默认规则选择新索引和约束的名称，而不考虑原始的命名。（此行为可避免新索引可能出现重复名称失败。）

**INCLUDING STATISTICS**

扩展统计信息将复制到新表。

**INCLUDING STORAGE**

已复制列定义的 `STORAGE` 设置将被复制。默认行为是排除 `STORAGE` 设置，从而导致新表中已复制列具有类型规定的默认设置。

**INCLUDING ALL**

`INCLUDING ALL` 是选择所有可用的单独选项的缩写形式。（它能被用于在 `INCLUDING ALL` 之后写单独的 `EXCLUDING` 子句，以选择部分指定选项之外的所有选项。）

`LIKE` 子句也能被用来从视图、外部表或组合类型拷贝列定义。不适合的选项（例如来自视图的 `INCLUDING INDEXES` ）会被忽略。

**CONSTRAINT constraint\_name**

一个列约束或表约束的可选名称。如果该约束被违背，约束名将会出现在错误消息中，这样类似列必须为正的约束名可以用来与客户端应用沟通有用的约束信息（指定包含空格的约束名时需要用到双引号）。如果没有指定约束名，系统将生成一个。

**NOT NULL**

该列不允许包含空值。

**NULL**

该列允许包含空值。这是默认情况。

这个子句只是提供与非标准 SQL 数据库的兼容。在新的应用中不推荐使用。

**CHECK ( expression ) \[ NO INHERIT \]**

`CHECK` 指定一个产生布尔结果的表达式，一个插入或更新操作要想成功，其中新的或被更新的行必须满足该表达式。计算出 `TRUE` 或 `UNKNOWN` 的表达式就会成功。只要任何一个插入或更新操作的行产生了 `FALSE` 结果，将报告一个错误异常并且插入或更新不会修改数据库。一个被作为列约束指定的检查约束只应该引用该列的值，而一个出现在表约束中的表达式可以引用多列。

当前， `CHECK` 表达式不能包含子查询，也不能引用当前行的列之外的变量。可以引用系统列 `tableoid` ，但不能引用其他系统列。

一个被标记为 `NO INHERIT` 的约束将不会传播到子表。

当一个表有多个 `CHECK` 约束时，检查完 `NOT NULL` 约束后，对于每一行会以它们名称的字母表顺序来进行检查（版本 9.5 之前的瀚高数据库对于 `CHECK` 约束不遵从任何特定的引发顺序）。

**DEFAULT default\_expr**

`DEFAULT` 子句为出现在其定义中的列赋予一个默认数据。该值是可以使用变量的表达式（特别是，不允许用对其他列的交叉引用）。子查询也是不允许的。默认值表达式的数据类型必须匹配列的数据类型。

默认值表达式将被用在任何没有为该列指定值的插入操作中。如果一列没有默认值，那么默认值为空值。

**GENERATED ALWAYS AS ( generation\_expr ) STORED**

此子句将列创建为generated column。列无法被写入，读取时将返回指定表达式的结果。

关键字 `STORED` 表示将在写入时计算列并将存储在磁盘上。

生成表达式可以引用表中的其他列，但不能引用其他生成的列。使用的任何函数和运算符都必须是不可改变的。不允许引用其他表。

**GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY \[ ( sequence\_options ) \]**

该子句将列创建为标识列。它将拥有一个隐式序列附加到它，并且新行中的列将自动从分配给它的序列中获取值。

子句 `ALWAYS` 和 `BY DEFAULT` 确定在 `INSERT` 语句中，序列值如何优先于用户指定的值。如果指定了 `ALWAYS` ，则只有在 `INSERT` 语句指定 `OVERRIDING SYSTEM VALUE` 时才接受用户指定的值。如果指定了 `BY DEFAULT` ，则用户指定的值优先。有关详细信息，请参见 `INSERT` 。（在 `COPY` 命令中，无论此设置如何，都始终使用用户指定的值。）

可选的 `sequence_options` 子句可用于覆盖序列的选项。有关详细信息，请参见 `CREATE SEQUENCE` 。

**UNIQUE** （列约束）

\*\*UNIQUE ( column\_name \[, … \] ) \[ INCLUDE ( column\_name \[, …\]) \]\*\*（表约束）

`UNIQUE` 约束指定一个表中的一列或多列组成的组包含唯一的值。唯一表约束的行为与列约束的行为相同，只是表约束能够跨越多列。

对于一个唯一约束的目的来说，空值不被认为是相等的。

每一个唯一表约束必须命名一个列的集合，并且它与该表上任何其他唯一或主键约束所命名的列集合都不相同（否则它将是一个被列举了两次的约束）。

在为多级分区层次结构建立唯一约束时，目标分区表的分区键中的所有列，以及那些由它派生的所有分区表，必须被包含在约束定义中。

添加唯一约束将自动在使用于约束的列或列组上创建唯一的 btree索引。可选子句 `INCLUDE` 在不强制唯一性的情况下向该索引添加一个或多个列。请注意虽然约束在包含的列上是非强制的，但是它仍然依赖于它们。因此，这些列上的某些操作（例如 `DROP COLUMN` ）可能会导致级联约束和索引删除。

**PRIMARY KEY** （列约束）

\*\*PRIMARY KEY ( column\_name \[, … \] ) \[ INCLUDE ( column\_name \[, …\]) \]\*\*（表约束）

`PRIMARY KEY` 约束指定表的一个或者多个列只能包含唯一（不重复）、非空的值。一个表上只能指定一个主键，可以作为列约束或表约束。

主键约束所涉及的列集合应该不同于同一个表上定义的任何唯一约束的列集合（否则，该唯一约束是多余的并且会被丢弃）。

`PRIMARY KEY` 强制的数据约束可以看成是 `UNIQUE` 和 `NOT NULL` 的组合，不过把一组列标识为主键也为模式设计提供了元数据，因为主键标识其他表可以依赖这一个列集合作为行的唯一标识符。

`PRIMARY KEY` 约束共享 `UNIQUE` 约束放到分区表上时限制。

添加 `PRIMARY KEY` 约束将自动在用于约束的列或列组上创建唯一的 btree 索引。可选的 `INCLUDE` 子句允许指定将被包含在索引的非-键部分中的列的列表。虽然包含的列的唯一性是非强制的，但约束仍依赖于它们。因此，这些包含的列上的某些操作（例如 `DROP COLUMN` ）可能会导致级联约束和索引删除。

**EXCLUDE \[ USING index\_method \] ( exclude\_element WITH operator \[, … \] ) index\_parameters \[ WHERE ( predicate ) \]**

`EXCLUDE` 子句定一个排除约束，它保证如果任意两行在指定列或表达式上使用指定操作符进行比较，不是所有的比较都将会返回 `TRUE` 。如果所有指定的操作符都测试相等，这就等价于一个 `UNIQUE` 约束，尽管一个普通的唯一约束将更快。不过，排除约束能够指定比简单相等更通用的约束。例如，你可以使用 `&&` 操作符指定一个约束，要求表中没有两行包含相互覆盖的圆。

排除约束使用一个索引实现，这样每一个指定的操作符必须与用于索引访问方法 `index_method` 的一个适当的操作符类相关联。操作符被要求是交换的。每一个 `exclude_element` 可以选择性地指定一个操作符类或者顺序选项，这些在 `CREATE INDEX` 中有完整描述。

访问方法必须支持 `amgettuple` （见第 61 章），目前这意味着GIN无法使用。尽管允许，但是在一个排除约束中使用 B-树或哈希索引没有意义，因为它无法做得比一个普通唯一索引更出色。因此在实践中访问方法将总是GiST或SP-GiST。

`predicate` 允许你在该表的一个子集上指定一个排除约束。在内部这会创建一个部分索引。注意在为此周围的圆括号是必须的。

**REFERENCES reftable \[ ( refcolumn ) \] \[ MATCH matchtype \] \[ ON DELETE referential\_action \] \[ ON UPDATE referential\_action \]** (column constraint)

**FOREIGN KEY ( column\_name \[, … \] ) REFERENCES reftable \[ ( refcolumn \[, … \] ) \] \[ MATCH matchtype \] \[ ON DELETE referential\_action \] \[ ON UPDATE referential\_action \]** (表约束)

这些子句指定一个外键约束，它要求新表的一列或一个列的组必须只包含能匹配被引用表的某个行在被引用列上的值。如果 `refcolumn` 列表被忽略，将使用 `reftable` 的主键。被引用列必须是被引用表中一个非可延迟唯一约束或主键约束的列。用户必须在被引用的表（或整个表,或特定的引用列）上拥有 `REFERENCES` 权限。增加的外键约束需要 `SHARE ROW EXCLUSIVE` 锁定引用的表。注意外键约束不能在临时表和永久表之间定义。

被插入到引用列的一个值会使用给定的匹配类型与被引用表的值进行匹配。有三种匹配类型： `MATCH FULL` 、 `MATCH PARTIAL` 以及 `MATCH SIMPLE` （这是默认值）。 `MATCH FULL` 将不允许一个多列外键中的一列为空，除非所有外键列都是空；如果它们都是空，则不要求该行在被引用表中有一个匹配。 `MATCH SIMPLE` 允许任意外键列为空，如果任一为空，则不要求该行在被引用表中有一个匹配。 `MATCH PARTIAL` 现在还没有被实现（当然， `NOT NULL` 约束能被应用在引用列上来阻止这些情况发生）。

另外，当被引用列中的数据被改变时，在这个表的列中的数据上可以执行特定的动作。 `ON DELETE` 指定当被引用表中一个被引用行被删除时要执行的动作。同样， `ON UPDATE` 指定当被引用表中一个被引用列被更新为新值时要执行的动作。如果该行被更新，但是被引用列并没有被实际改变，不会做任何动作。除了 `NO ACTION` 检查之外的引用动作不能被延迟，即便该约束被声明为可延迟的。对每一个子句可能有以下动作：

**NO ACTION**

产生一个错误指示删除或更新将会导致一个外键约束违背。如果该约束被延迟，并且仍存在引用行，这个错误将在约束检查时被产生。这是默认动作。

**RESTRICT**

产生一个错误指示删除或更新将会导致一个外键约束违背。这个动作与 `NO ACTION` 相同，不过该检查不是可延迟的。

**CASCADE**

删除任何引用被删除行的行，或者把引用列的值更新为被引用列的新值。

**SET NULL**

将引用列设置为空。

**SET DEFAULT**

设置引用列为它们的默认值（如果该默认值非空，在被引用表中必须有一行匹配该默认值，否则该操作将会失败）。

如果被引用列被频繁地更改，最好在引用列上加上一个索引，这样与外键约束相关的引用动作能够更高效地被执行。

**DEFERRABLE**  
**NOT DEFERRABLE**

这个子句控制该约束是否能被延迟。一个不可延迟的约束将在每一次命令后立刻被检查。可延迟约束的检查将被推迟到事务结束时进行（使用 `SET CONSTRAINTS` 命令）。 `NOT DEFERRABLE` 是默认值。当前，只有 `UNIQUE` 、 `PRIMARY KEY` 、 `EXCLUDE` 以及 `REFERENCES` （外键）约束接受这个子句。 `NOT NULL` 以及 `CHECK` 约束是不可延迟的。注意在包括 `ON CONFLICT DO UPDATE` 子句的 `INSERT` 语句中，可延迟约束不能被用作冲突裁判者。

**INITIALLY IMMEDIATE**  
**INITIALLY DEFERRED**

如果一个约束是可延迟的，这个子句指定检查该约束的默认时间。如果该约束是 `INITIALLY IMMEDIATE` ，它会在每一个语句之后被检查。这是默认值。如果该约束是 `INITIALLY DEFERRED` ，它只会在事务结束时被检查。约束检查时间可以用 `SET CONSTRAINTS` 命令修改。

**USING method**

此可选子句指定用于存储新表内容的表访问方法；该方法需要的是类型 `TABLE` 的访问方法。如果未指定此选项，则为新表选择默认表访问方法。详见 `default_table_access_method` 。

**WITH ( storage\_parameter \[= value\] \[, … \] )**

这个子句为一个表或索引指定可选的存储参数，详见 **存储参数** 。为了向后兼容性，表的 `WITH` 子句还可以包括 `OIDS=FALSE` 以便指定新表的行不应包含 OIDs （对象标识符）， `OIDS=TRUE` 不再受支持。

**WITHOUT OIDS**

这是向后兼容的语法，用于声明表 `WITHOUT OIDS` ，不再支持创建表 `WITH OIDS` 。

**ON COMMIT**

临时表在一个事务块结束时的行为由 `ON COMMIT` 控制。三种选项是：

**PRESERVE ROWS**

在事务结束时不采取特殊的动作。这是默认行为。

**DELETE ROWS**

在每一个事务块结束时将删除临时表中的所有行。实质上，在每一次提交时会完成一次自动的 `TRUNCATE` 。当应用于分区表上时，这不会级联到它的分区。

**DROP**

在当前事务块结束时将删除临时表。当在分区表上使用时，这个操作会删除他的分区，而在具有继承子级的表上使用时，它将删除依赖的子级。

**TABLESPACE tablespace\_name**

`tablespace_name` 是新表要创建于其中的表空间名称。如果没有指定，将参考 `default_tablespace` ，或者如果表是临时的则参考 `temp_tablespaces` 。对于分区表，由于表本身不需要存储，指定表空间将 `default_tablespace` 作为默认表空间覆盖，在未显式指定其他表空间时用于任何新创建的分区。

**USING INDEX TABLESPACE tablespace\_name**

这个子句允许选择与一个 `UNIQUE` 、 `PRIMARY KEY` 或者 `EXCLUDE` 约束相关的索引将被创建在哪个表空间中。如果没有指定，将参考 `default_tablespace` ，或者如果表是临时的则参考 `temp_tablespaces` 。

**存储参数**

`WITH` 子句能够为表或与一个 `UNIQUE` 、 `PRIMARY KEY` 或者 `EXCLUDE` 约束相关的索引指定存储参数。用于索引的存储参数已经在 `CREATE INDEX` 中介绍过。当前可用于表的存储参数在下文中列出。如下文所示，对于很多这类参数，都有一个名字带有 `toast.`前缀的附加参数，它能被用来控制该表的二级TOAST表（如果存在）的行为。如果一个表的参数值被设置但是相应的 `toast.`参数没有被设置，那么 TOAST 表将使用该表的参数值。不支持为分区表指定这些参数，但可以为单个叶子分区指定它们。

**fillfactor (integer)**

一个表的填充因子是一个 10 到 100 之间的百分数。100（完全填满）是默认值。当一个较小的填充因子被指定时， `INSERT` 操作会把表页面只填满到指定的百分比，每个页面上剩余的空间被保留给该页上行的更新。这就让 `UPDATE` 有机会把一行的已更新版本放在与其原始版本相同的页面上，这比把它放在一个不同的页面上效率更高。对于一个项从来不会被更新的表来说，完全填满是最好的选择，但是在更新繁重的表上则较小的填充因子更合适。这个参数不能对 TOAST 表设置。

**toast\_tuple\_target (integer)**

在我们尝试将长列值移动到TOAST表中之前， `toast_tuple_target` 指定需要的最小元组长度，也是在toasting开始时尝试减少长度的目标长度。这仅影响标记为”外部”或”扩展”的列，并且仅适用于新元组 - 对现有行没有影响。默认情况下此参数设置为允许每个块至少 4 个元组，默认块大小为 2040 字节。有效值介于 128 字节和(块大小-标头)之间，默认大小为 8160 字节。更改此值对于非常短或非常长的行可能没有用处。请注意默认设置通常接近最佳状态，在某些情况下设置此参数可能会产生负面影响。不能对TOAST表设置此参数。

**parallel\_workers (integer)**

这个参数设置用于辅助并行扫描这个表的工作者数量。如果没有设置这个参数，系统将基于关系的尺寸来决定一个值。规划者或使用并行扫描的实用程序选择的工作者数量可能会比较少，例如 `max_worker_processes` 的设置较小就是一种可能的原因。

**autovacuum\_enabled, toast.autovacuum\_enabled (boolean)**

为一个特定的表启用或者禁用自动清理守护进程。如果为真，自动清理守护进程将遵照规则在这个表上执行自动的 `VACUUM` 或者 `ANALYZE` 操作。如果为假，这个表不会被自动清理，不过为了阻止事务 ID 回卷时还是会对它进行自动的清理。如果 `autovacuum` 参数为假，自动清理守护进程根本就不会运行（除非为了阻止事务 ID 回卷），设置独立的表存储参数也不会覆盖这个设置。因此显式地将这个存储参数设置为 `true` 很少有大的意义，只有设置为 `false` 才更有用。

**vacuum\_index\_cleanup, toast.vacuum\_index\_cleanup (boolean)**

当 `VACUUM` 在此表上运行时启用或禁用索引清理。默认值为 `true` 。禁用索引清理可以显著加快 `VACUUM` ，但如果表修改很频繁，也可能导致索引严重膨胀。

`VACUUM` 的 `INDEX_CLEANUP` 参数，如果指定，将覆盖此选项的值。

**vacuum\_truncate, toast.vacuum\_truncate (boolean)**

启用或禁用vacuum以尝试截断此表末尾的任何空页。默认值为 `true` 。如果 `true` ， `VACUUM` 和autovacuum将执行截断，截断页的磁盘空间将返回到操作系统。请注意，截断需要 `ACCESS EXCLUSIVE` 在表上锁定。 `VACUUM` 的 `TRUNCATE` 参数，如果指定，覆盖此选项的值。

**autovacuum\_vacuum\_threshold, toast.autovacuum\_vacuum\_threshold (integer)**

`autovacuum_vacuum_threshold` 参数对于每个表的值。

**autovacuum\_vacuum\_scale\_factor, toast.autovacuum\_vacuum\_scale\_factor (float4)**

`autovacuum_vacuum_scale_factor` 参数对于每个表的值。

**autovacuum\_analyze\_threshold (integer)**

`autovacuum_analyze_threshold` 参数对于每个表的值。

**autovacuum\_analyze\_scale\_factor (float4)**

`autovacuum_analyze_scale_factor` 参数对于每个表的值。

**autovacuum\_vacuum\_cost\_delay, toast.autovacuum\_vacuum\_cost\_delay (floating point)**

`autovacuum_vacuum_cost_delay` 参数对于每个表的值。

**autovacuum\_vacuum\_cost\_limit, toast.autovacuum\_vacuum\_cost\_limit (integer)**

`autovacuum_vacuum_cost_limit` 参数对于每个表的值。

**autovacuum\_freeze\_min\_age, toast.autovacuum\_freeze\_min\_age (integer)**

`vacuum_freeze_min_age` 参数对于每个表的值。注意自动清理将忽略超过系统范围 `autovacuum_freeze_max_age` 参数一半的针对每个表的 `autovacuum_freeze_min_age` 参数。

**autovacuum\_freeze\_max\_age, toast.autovacuum\_freeze\_max\_age (integer)**

`autovacuum_freeze_max_age` 参数对于每个表的值。注意自动清理将忽略超过系统范围参数（只能被设置得较小）一半的针对每个表的 `autovacuum_freeze_max_age` 参数。

**autovacuum\_freeze\_table\_age, toast.autovacuum\_freeze\_table\_age (integer)**

`vacuum_freeze_table_age` 参数对于每个表的值。

**autovacuum\_multixact\_freeze\_min\_age, toast.autovacuum\_multixact\_freeze\_min\_age (integer)**

`vacuum_multixact_freeze_min_age` 参数对于每个表的值。注意自动清理将忽略超过系统范围 `autovacuum_multixact_freeze_max_age` 参数一半的针对每个表的 `autovacuum_multixact_freeze_min_age` 参数。

**autovacuum\_multixact\_freeze\_max\_age, toast.autovacuum\_multixact\_freeze\_max\_age (integer)**

`autovacuum_multixact_freeze_max_age` 参数对于每个表的值。注意自动清理将忽略超过系统范围参数（只能被设置得较小）一半的针对每个表的 `autovacuum_multixact_freeze_max_age` 参数。

**autovacuum\_multixact\_freeze\_table\_age, toast.autovacuum\_multixact\_freeze\_table\_age (integer)**

`vacuum_multixact_freeze_table_age` 参数对于每个表的值。

**log\_autovacuum\_min\_duration, toast.log\_autovacuum\_min\_duration (integer)**

`log_autovacuum_min_duration` 参数对于每个表的值。

**user\_catalog\_table (boolean)**

声明该表是一个用于逻辑复制目的的额外的目录表。不能对TOAST表设置这个参数。

**注解**

瀚高数据库为每一个唯一约束和主键约束创建一个索引来强制唯一性。因此，没有必要显式地为主键列创建一个索引（详见 `CREATE INDEX` ）。

在当前的实现中，唯一约束和主键不会被继承。这使得继承和唯一约束的组合相当不正常。

一个表不能有超过 1600 列（实际上，由于元组长度限制，有效的限制通常更低）。

**示例**

创建表films和表distributors：

```sql
CREATE TABLE films (

code char(5) CONSTRAINT firstkey PRIMARY KEY,

title varchar(40) NOT NULL,

did integer NOT NULL,

date_prod date,

kind varchar(10),

len interval hour to minute

);

CREATE TABLE distributors (

did integer PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,

name varchar(40) NOT NULL CHECK (name \<\> \'\')

);
```

创建有一个二维数组的表：

```sql
CREATE TABLE array_int (

vector int\[\]\[\]

);
```

为表films定义一个唯一表约束。唯一表约束能够被定义在表的一列或多列上：

```sql
CREATE TABLE films (

code char(5),

title varchar(40),

did integer,

date_prod date,

kind varchar(10),

len interval hour to minute,

CONSTRAINT production UNIQUE(date_prod)

);
```

定义一个列检查约束：

```sql
CREATE TABLE distributors (

did integer CHECK (did \> 100),

name varchar(40)

);
```

定义一个表检查约束：

```sql
CREATE TABLE distributors (

did integer,

name varchar(40),

CONSTRAINT con1 CHECK (did \> 100 AND name \<\> \'\')

);
```

为表films定义一个主键表约束：

```sql
CREATE TABLE films (

code char(5),

title varchar(40),

did integer,

date_prod date,

kind varchar(10),

len interval hour to minute,

CONSTRAINT code_title PRIMARY KEY(code,title)

);
```

为表distributors定义一个主键约束。下面的两个例子是等价的，第一个使用表约束语法，第二个使用列约束语法：

```sql
CREATE TABLE distributors (

did integer,

name varchar(40),

PRIMARY KEY(did)

);

CREATE TABLE distributors (

did integer PRIMARY KEY,

name varchar(40)

);
```

为列name赋予一个文字常量默认值，安排列did的默认值是从一个序列对象中选择下一个值产生，并且让modtime的默认值是该行被插入的时间：

```sql
CREATE TABLE distributors (

name varchar(40) DEFAULT \'Luso Films\',

did integer DEFAULT nextval(\'distributors_serial\'),

modtime timestamp DEFAULT current_timestamp

);
```

在表distributors上定义两个NOT NULL列约束，其中之一被显式给定了一个名称：

```sql
CREATE TABLE distributors (

did integer CONSTRAINT no_null NOT NULL,

name varchar(40) NOT NULL

);
```

为name列定义一个唯一约束：

```sql
CREATE TABLE distributors (

did integer,

name varchar(40) UNIQUE

);
```

同样的唯一约束用表约束指定：

```sql
CREATE TABLE distributors (

did integer,

name varchar(40),

UNIQUE(name)

);
```

创建相同的表，指定表和它的唯一索引指定 70% 的填充因子：

```sql
CREATE TABLE distributors (

did integer,

name varchar(40),

UNIQUE(name) WITH (fillfactor=70)

)

WITH (fillfactor=70);
```

创建表circles，带有一个排除约束阻止任意两个圆重叠：

```sql
CREATE TABLE circles (

c circle,

EXCLUDE USING gist (c WITH &&)

);
```

在表空间diskvol1中创建表cinemas：

```sql
CREATE TABLE cinemas (

id serial,

name text,

location text

) TABLESPACE diskvol1;
```

创建一个组合类型以及一个类型化的表：

```sql
CREATE TYPE employee_type AS (name text, salary numeric);

CREATE TABLE employees OF employee_type (

PRIMARY KEY (name),

salary WITH OPTIONS DEFAULT 1000

);
```

创建一个范围分区表：

```sql
CREATE TABLE measurement (

logdate date not null,

peaktemp int,

unitsales int

) PARTITION BY RANGE (logdate);
```

创建在分区键中具有多个列的范围分区表：

```sql
CREATE TABLE measurement_year_month (

logdate date not null,

peaktemp int,

unitsales int

) PARTITION BY RANGE (EXTRACT(YEAR FROM logdate), EXTRACT(MONTH FROM logdate));
```

创建列表分区表：

```sql
CREATE TABLE cities (

city_id bigserial not null,

name text not null,

population bigint

) PARTITION BY LIST (left(lower(name), 1));
```

建立哈希分区表:

```sql
CREATE TABLE orders (

order_id bigint not null,

cust_id bigint not null,

status text

) PARTITION BY HASH (order_id);
```

创建范围分区表的分区：

```sql
CREATE TABLE measurement_y2016m07

PARTITION OF measurement (

unitsales DEFAULT 0

) FOR VALUES FROM (\'2016-07-01\') TO (\'2016-08-01\');
```

使用分区键中的多个列创建范围分区表的几个分区：

```sql
CREATE TABLE measurement_ym_older

PARTITION OF measurement_year_month

FOR VALUES FROM (MINVALUE, MINVALUE) TO (2016, 11);

CREATE TABLE measurement_ym_y2016m11

PARTITION OF measurement_year_month

FOR VALUES FROM (2016, 11) TO (2016, 12);

CREATE TABLE measurement_ym_y2016m12

PARTITION OF measurement_year_month

FOR VALUES FROM (2016, 12) TO (2017, 01);

CREATE TABLE measurement_ym_y2017m01

PARTITION OF measurement_year_month

FOR VALUES FROM (2017, 01) TO (2017, 02);
```

创建列表分区表的分区：

```sql
CREATE TABLE cities_ab

PARTITION OF cities (

CONSTRAINT city_id_nonzero CHECK (city_id != 0)

) FOR VALUES IN (\'a\', \'b\');
```

创建本身是分区的列表分区表的分区，然后向其添加分区：

```sql
CREATE TABLE cities_ab

PARTITION OF cities (

CONSTRAINT city_id_nonzero CHECK (city_id != 0)

) FOR VALUES IN (\'a\', \'b\') PARTITION BY RANGE (population);

CREATE TABLE cities_ab_10000_to_100000

PARTITION OF cities_ab FOR VALUES FROM (10000) TO (100000);
```

建立哈希分区表的分区：

```sql
CREATE TABLE orders_p1 PARTITION OF orders

FOR VALUES WITH (MODULUS 4, REMAINDER 0);

CREATE TABLE orders_p2 PARTITION OF orders

FOR VALUES WITH (MODULUS 4, REMAINDER 1);

CREATE TABLE orders_p3 PARTITION OF orders

FOR VALUES WITH (MODULUS 4, REMAINDER 2);

CREATE TABLE orders_p4 PARTITION OF orders

FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

建立默认分区：

```sql
CREATE TABLE cities_partdef

PARTITION OF cities DEFAULT;
```

兼容性

CREATE TABLE命令遵从SQL标准，除了以下例外。

- 临时表

尽管CREATE TEMPORARY TABLE的语法很像 SQL 标准的语法，但事实是并不相同。在标准中，临时表只需要被定义一次并且会自动地存在（从空内容开始）于需要它们的每一个会话中。瀚高数据库则要求每一个会话为每一个要用的临时表发出它自己的CREATE TEMPORARY TABLE命令。这允许不同的会话为不同的目的使用相同的临时表名，而标准的方法约束一个给定临时表名的所有实例都必须具有相同的表结构。

标准中对于临时表行为的定义被广泛地忽略了。瀚高数据库在这一点上的行为和多种其他SQL 数据库是相似的。

SQL 标准也区分全局和局部临时表，其中一个局部临时表为每一个会话中的每一个 SQL 模块具有一个独立的内容集合，但是它的定义仍然是多个会话共享的。因为瀚高数据库不支持 SQL 模块，这种区别与瀚高数据库无关。

为了兼容性目的，瀚高数据库将在临时表声明中接受GLOBAL和LOCAL关键词，但是它们当前没有效果。我们不鼓励使用这些关键词，因为未来版本的瀚高数据库可能采用一种更兼容标准的（对它们含义的）解释。

临时表的ON COMMIT子句也和 SQL 标准相似，但是有一些不同。如果忽略ON COMMIT子句，SQL 指定默认行为是ON COMMIT DELETE ROWS。但是，瀚高数据库中的默认行为是ON COMMIT PRESERVE ROWS。SQL 中不存在ON COMMIT DROP选项。

- 非延迟唯一性约束

但一个UNIQUE或PRIMARY KEY约束是非可延迟的，只要一个行被插入或修改，瀚高数据库就会立即检查唯一性。SQL 标准指出只有在语句结束时才应该强制唯一性。当一个单一命令更新多个键值时，这两者是不同的。要得到兼容标准的行为，将该约束声明为DEFERRABLE但是不延迟（即INITIALLY IMMEDIATE）。注意这可能要显著地慢于立即唯一性检查。

- 列检查约束

SQL 标准指出CHECK列约束只能引用它们应用到的列，只有CHECK表约束能够引用多列。瀚高数据库并没有强制这个限制，它同样处理列检查约束和表检查约束。

- EXCLUDE 约束

EXCLUDE约束类型是一种瀚高数据库扩展。

- NULL “约束”

NULL “约束”（实际上是一个非约束）是一个瀚高数据库对 SQL 标准的扩展，它也被包括（以及对称的NOT NULL约束）在一些其他的数据库系统中以实现兼容性。因为它是任意列的默认值，它的存在就像噪声一样。

- 约束名称

SQL标准规定在包含表或域的模式范围内表和域的约束必须具有唯一的名称。 瀚高数据库是比较宽松的：它只需要约束名称在附加到特定表或域的约束之间是唯一的。 但是，对于基于索引的约束(UNIQUE,PRIMARY KEY, and EXCLUDEconstraints)， 这个特别的自由度并不存在， 因为关联的索引被命名为与约束相同的名称，并且索引名称在相同模式的所有关系中必须是唯一的。

当前，瀚高数据库没有记录NOT NULL约束的名称， 因此它们不受唯一性限制的影响。这在将来的版本中可能会改变。

- 继承

通过INHERITS子句的多继承是一种瀚高数据库的语言扩展。SQL:1999 以及之后的标准使用一种不同的语法和不同的语义定义了单继承。SQL:1999-风格的继承还没有被瀚高数据库。

- 零列表

瀚高数据库允许创建一个没有列的表（例如CREATE TABLE foo();）。这是一个对于 SQL 标准的扩展，它不允许零列表。零列表本身并不是很有用，但是不允许它们会为ALTER TABLE DROP COLUMN带来奇怪的特殊情况，因此忽略这种规则限制看起来更加整洁。

- 多个标识列

瀚高数据库允许一个表拥有多个标识列。 该标准指定一个表最多只能有一个标识列。这主要是为了给模式更改或迁移提供更大的灵活性。 请注意，INSERT命令仅支持一个适用于整个语句的覆盖子句，因此不支持具有不同行为的多个标识列。

Generated Columns

STORED选项不是标准，但也用于其他SQL实现。SQL标准不规定生成列的存储。

- LIKE 子句

虽然 SQL 标准中有一个LIKE子句，但是瀚高数据库接受的很多LIKE子句选项却不在标准中，并且有些标准中的选项也没有被瀚高数据库实现。

- WITH子句

WITH子句是一个瀚高数据库扩展，存储参数不在标准中。

- 表空间

瀚高数据库的表空间概念不是标准的一部分。因此，子句TABLESPACE和USING INDEX TABLESPACE是扩展。

- 类型化的表

类型化的表实现了 SQL 标准的一个子集。根据标准，一个类型化的表具有与底层组合类型相对应的列，以及其他的”自引用列”。瀚高数据库不显式支持自引用列。

- PARTITION BY 子句

PARTITION BY子句是瀚高数据库的一个扩展。

- PARTITION OF 子句

PARTITION OF子句瀚高数据库的一个扩展。

参见

ALTER TABLE, DROP TABLE, CREATE TABLE AS, CREATE TABLESPACE, CREATE TYPE

## CREATE TABLE AS

— 从一个查询的结果创建一个新表

**大纲**

```sql
CREATE [ [ GLOBAL | LOCAL ] { TEMPORARY | TEMP } | UNLOGGED ] TABLE [ IF NOT EXISTS ] table_name
[ (column_name [, ...] ) ]
[ USING method ]
[ WITH ( storage_parameter [= value] [, ... ] ) | WITHOUT OIDS ]
[ ON COMMIT { PRESERVE ROWS | DELETE ROWS | DROP } ]
[ TABLESPACE tablespace_name ]
AS query
[ WITH [ NO ] DATA ]
```

**描述**

CREATE TABLE AS创建一个表，并且用由一个 `SELECT` 命令计算出来的数据填充该表。该表的列具有和 `SELECT` 的输出列相关的名称和数据类型（不过可以通过给出一个显式的新列名列表来覆盖这些列名）。

CREATE TABLE AS和创建一个视图有些相似，但是实际上非常不同：它会创建一个新表并且只计算该查询一次用来初始填充新表。这个新表将不会跟踪该查询源表的后续变化。相反，一个视图只要被查询，它的定义 `SELECT` 语句就会被重新计算。

**参数**

**GLOBAL或者LOCAL**

为兼容性而忽略。不推荐使用这些关键词，详见 `CREATE TABLE` 。

**TEMPORARY或者TEMP**

如果被指定，该表会被创建为一个临时表。详见 `CREATE TABLE` 。

**UNLOGGED**

如果被指定，该表会被创建为一个不做日志的表。详见 `CREATE TABLE` 。

**IF NOT EXISTS**

如果已经存在一个同名的关系时不要抛出错误。这种情况下会发出一个提示。详见 `CREATE TABLE` 。

**table\_name**

要创建的表的名称（可以被模式限定）。

**column\_name**

新表中一列的名称。如果没有提供列名，会从查询的输出列名中得到。

**USING method**

这个可选的子句指定了用于存储新表内容的表访问方法；该方法需要是一个类型 `TABLE` 的访问方法。如果没有指定这个选项，则选择新表的默认表访问方法。详见 `default_table_access_method` 。

**WITH ( storage\_parameter \[= value\] \[, … \] )**

这个子句为新表指定可选的存储参数，详见 **存储参数** 。为了向后兼容，表的 `WITH` 子句也能包含 `OIDS=FALSE` 来指定新表的行将不包含OID（对象标识符）。 `OIDS=TRUE` 不再支持。

**WITHOUT OIDS**

这是向后兼容的语法，用于声明表 `WITHOUT OIDS` ，创建表 `WITH OIDS` 不再被支持。

**ON COMMIT**

临时表在事务块结束时的行为可以用 `ON COMMIT` 控制。三个选项是：

**PRESERVE ROWS**

在事务结束时不采取特殊的动作。这是默认行为。

**DELETE ROWS**

在每一个事务块结束时临时表中的所有行都将被删除。本质上，在每次提交时会完成一次自动的 `TRUNCATE` 。

**DROP**

在当前事务块结束时将删掉临时表。

**TABLESPACE tablespace\_name**

`tablespace_name` 是要在其中创建新表的表空间名称。如果没有指定，将会查询 `default_tablespace` ，临时表会查询 `temp_tablespaces` 。

**query**

一个 `SELECT` 、 `TABLE` 或者 `VALUES` 命令，或者是一个运行准备好的 `SELECT` 、 `TABLE` 或者 `VALUES` 查询的 `EXECUTE` 命令。

**WITH \[ NO \] DATA**

这个子句指定查询产生的数据是否应该被复制到新表中。如果不是，只有表结构会被复制。默认是复制数据。

**注解**

这个命令在功能上类似于 `SELECT INTO` ，但是它更好，因为不太可能被 `SELECT INTO` 语法的其他使用混淆。更进一步， `CREATE TABLE AS` 提供了 `SELECT INTO` 的功能的一个超集。

**示例**

创建一个新表 `films_recent` ，它只由表 `films` 中最近的项组成：

```sql
CREATE TABLE films_recent AS
SELECT * FROM films WHERE date_prod >= '2002-01-01';
```

要完全地复制一个表，也可以使用 `TABLE` 命令的简短形式：

```sql
CREATE TABLE films2 AS
TABLE films;
```

用一个预备语句创建一个新的临时表 `films_recent` ，它仅由表 `films` 中最近的项组成，使用准备好的声明。新表将在提交时被丢弃：

```sql
PREPARE recentfilms(date) AS
SELECT * FROM films WHERE date_prod > $1;

CREATE TEMP TABLE films_recent ON COMMIT DROP AS
EXECUTE recentfilms('2002-01-01');
```

**兼容性**

CREATE TABLE AS符合 SQL标准。下面的是非标准扩展：

- 标准要求在子查询子句周围有圆括号，在瀚高数据库中这些圆括号是可选的。
- 在标准中， `WITH [ NO ] DATA` 子句是必要的，而瀚高数据库中是可选的。
- 瀚高数据库处理临时表的方式和标准不同。详见 `CREATE TABLE` 。
- `WITH` 子句是一种瀚高数据库扩展，标准中没有存储参数。
- 瀚高数据库的表空间概念是标准的一部分。因此，子句 `TABLESPACE` 是一种扩展。

**另见**

CREATE MATERIALIZED VIEW, CREATE TABLE, EXECUTE, SELECT, SELECT INTO, VALUES

## CREATE TABLESPACE

— 定义一个新的表空间

**大纲**

```sql
CREATE TABLESPACE tablespace_name
[ OWNER { new_owner | CURRENT_USER | SESSION_USER } ]
LOCATION 'directory'
[ WITH ( tablespace_option = value [, ... ] ) ]
```

**描述**

CREATE TABLESPACE注册一个新的集簇范围的表空间。表空间的名称必须与数据库集簇中现有的任何表空间不同。

表空间允许超级用户在文件系统上定义另一个位置，可以把包含数据库对象（例如表和索引）的数据文件放在那里。

一个具有适当特权的用户可以把 `tablespace_name` 传递给 `CREATE DATABASE` 、 `CREATE TABLE` 、 `CREATE INDEX` 或者 `ADD CONSTRAINT` 来让这些对象的数据文件存储在指定的表空间中。

> **警告：**
> 
> 表空间不能独立于定义它的集簇使用。

**参数**

**tablespace\_name**

要创建的表空间的名称。名称不能以 `pg_` 开头，因为这样的名称是为系统表空间保留的。

**user\_name**

将拥有该表空间的用户名。如果省略，默认为执行该命令的用户。只有超级用户能创建表空间，但是它们能把表空间的拥有权赋予给非超级用户。

**directory**

要被用于表空间的目录。该目录必需存在（ `CREATE TABLESPACE` 将不创建它），应该为空，并且必须由瀚高数据库系统用户拥有。该目录必须用一个绝对路径指定。

**tablespace\_option**

要设置或者重置的表空间参数。当前，唯一可用的参数是 `seq_page_cost` 、 `random_page_cost` 以及 `effective_io_concurrency` 。为一个特定表空间设定其中一个值将覆盖规划器对该表空间中表页读取的常规代价估计，常规代价估计是由同名的配置参数所建立（见 `seq_page_cost` 、 `random_page_cost` 、 `effective_io_concurrency` ）。如果一个表空间位于一个比其他 I/O 子系统更慢或者更快的磁盘上，这些参数就能发挥作用。

**注解**

只有在支持符号链接的系统上才支持表空间。

`CREATE TABLESPACE` 不能在一个事务块内被执行。

**示例**

要在文件系统位置 `/data/dbs` 创建表空间 `dbspace` ，请首先使用操作系统工具创建目录并设置正确的所有权：

```bash
mkdir /data/dbs
chown postgres:postgres /data/dbs
```

然后在内部发出表空间创建命令瀚高数据库:

```sql
CREATE TABLESPACE dbspace LOCATION '/data/dbs';
```

要创建由不同数据库用户拥有的表空间，可用类似这样的命令：

```sql
CREATE TABLESPACE indexspace OWNER genevieve LOCATION '/data/indexes';
```

**兼容性**

CREATE TABLESPACE是一种瀚高数据库扩展。

**另见**

CREATE DATABASE, CREATE TABLE, CREATE INDEX, DROP TABLESPACE, ALTER TABLESPACE

## CREATE TEXT SEARCH CONFIGURATION

— 定义一个新的文本搜索配置

**大纲**

```sql
CREATE TEXT SEARCH CONFIGURATION name (

PARSER = parser_name \|

COPY = source_config

)
```

**描述**

CREATE TEXT SEARCH CONFIGURATION 创建一个新的文本搜索配置。一个文本搜索配置指定一个文本搜索解析器（ 它能把字符串解析成记号），外加一些词典（可被用来决定哪些记号是搜索 感兴趣的）。

如果只指定了解析器，那么新文本搜索配置最初没有从记号类型到词典的映射， 并且因此将忽略所有词。后续的ALTER TEXT SEARCH CONFIGURATION命令必须被用来创建映射以让该配置变得可用。 另一种方式是复制一个现有的文本搜索配置。

如果给定一个模式名称，则文本搜索配置会被创建在指定的模式中。否则它将会 被创建在当前模式中。

定义一个文本搜索配置的用户会成为其拥有者。

**参数**

name

要创建的文本搜索配置的名称。该名称可以被模式限定。

parser\_name

这个配置要使用的文本搜索解析器的名称。

source\_config

要复制的已有文本搜索配置的名称。

**注解**

PARSER和COPY选项是互斥的，因为当一个已有的配置被复制时，它的解析器选择也会被复制。

**兼容** 性

在SQL标准中没有 CREATE TEXT SEARCH CONFIGURATION语句。

**另见**

ALTER TEXT SEARCH CONFIGURATION, DROP TEXT SEARCH CONFIGURATION

## CREATE TEXT SEARCH DICTIONARY

— 定义一个新的文本搜索字典

**大纲**

```sql
CREATE TEXT SEARCH DICTIONARY name (

TEMPLATE = template

\[, option = value \[, \... \]\]

)
```

**描述**

CREATE TEXT SEARCH DICTIONARY创建一个 新的文本搜索字典。一个文本搜索字典指定一种识别搜索感兴趣或者不感兴趣 的单词的方法。一个字典依赖于一个文本搜索模板，后者指定了实际执行该工 作的函数。通常该字典提供一些控制该模板函数细节行为的选项。

如果给出了一个模式名称，那么该文本搜索字典会被创建在指定的模式中。 否则它会被创建在当前模式中。

定义文本搜索字典的用户将成为其拥有者。

**参数**

name

要创建的文本搜索字典的名称。该名称可以是模式限定的。

template

将定义这个字典基本行为的文本搜索模板的名称。

option

要为此字典设置的模板相关选项的名称。

value

用于模板相关选项的值。如果该值不是一个简单标识符或者数字，它必须 被加引用（你可以按照你所希望的总是对它加上引用）。

**示例**

下面的例子命令创建了一个基于 Snowball 的字典，它使用了非标准的 停用词列表。

```sql
CREATE TEXT SEARCH DICTIONARY my_russian (

template = snowball,

language = russian,

stopwords = myrussian

);
```

**兼容性**

在 SQL 标准中没有 CREATE TEXT SEARCH DICTIONARY语句。

**另见**

ALTER TEXT SEARCH DICTIONARY, DROP TEXT SEARCH DICTIONARY

## CREATE TEXT SEARCH PARSER

— 定义一个新的文本搜索解析器

**大纲**

```sql
CREATE TEXT SEARCH PARSER name (

START = start_function ,

GETTOKEN = gettoken_function ,

END = end_function ,

LEXTYPES = lextypes_function

\[, HEADLINE = headline_function \]

)
```

**描述**

CREATE TEXT SEARCH PARSER创建一个 新的文本搜索解析器。一个文本搜索解析器定义把文本字符串分解成记号 并且为记号分配类型（分类）的方法。一个解析器本身并不特别有用，但 是必须与一些要用于搜索的文本搜索字典一起被绑定到一个文本搜索配置 中。

如果给出了一个模式名称，那么文本搜索解析器将被创建在指定的模式中。 否则它会被创建在当前模式中。

只有超级用户才能使用 CREATE TEXT SEARCH PARSER（这是因为 错误的文本搜索定义可能会让服务器混淆甚至崩溃）。

**参数**

name

要创建的文本搜索解析器的名称。该名称可以是模式限定的。

start\_function

用于该解析器的开始函数的名称。

gettoken\_function

用于该解析器的取下一个记号的函数名称。

end\_function

用于该解析器的结束函数的名称。

lextypes\_function

用于该解析器的词法分析器函数（一个返回其产生的记号类型集合信息的函数）的名称。

headline\_function

用于该解析器的标题函数（一个对记号集合进行综述的函数）的名称。

如有必要，函数的名称可以被模式限定。参数类型没有给出， 因为函数的每个类型的参数列表无法被预先决定。除了标题函数之外， 所有函数都是必要的。

参数可以以任何顺序出现，而不是必须按照上面所展示的顺序。

**兼容性**

在 SQL 标准中没有 CREATE TEXT SEARCH PARSER语句。

**另见**

ALTER TEXT SEARCH PARSER, DROP TEXT SEARCH PARSER

## CREATE TEXT SEARCH TEMPLATE

— 定义一种新的文本搜索模板

**大纲**

```sql
CREATE TEXT SEARCH TEMPLATE name (

\[ INIT = init_function , \]

LEXIZE = lexize_function

)
```

**描述**

CREATE TEXT SEARCH TEMPLATE创建一个 新的文本搜索模板。文本搜索模板定义实现文本搜索字典的函数。一个模板 本身没什么用处，但是必须被实例化为一个字典来使用。字典通常指定要给 予模板函数的参数。

如果给出了一个模式名，文本搜索模板会被创建在指定模式中。否则它会被 创建在当前模式中。

必须成为超级用户以使用 CREATE TEXT SEARCH TEMPLATE。做出 这种限制是因为错误的模板定义会让服务器混淆甚至崩溃。将模板与字典 分隔开来的原因是模板中封装了定义字典的”不安全”方面。在 定义字典时可以被设置的参数对非特权用户是可以安全设置的，因此创建 字典不需要拥有特权来操作。

**参数**

name

要创建的额文本搜索模板的名称。该名称可以被模式限定。

init\_function

用于模板的初始化函数的名称。

lexize\_function

用于模板的分词函数的名称。

如有必要，函数名称可以被模式限定。参数类型没有给出，因为每一类 函数的参数列表是预先定义好的。分词函数是必需的，但是初始化函数 是可选的。

参数可以以任何顺序出现，而不是只能按照上文的顺序。

**兼容性**

在 SQL 标准中没有 CREATE TEXT SEARCH TEMPLATE语句。

**另见**

ALTER TEXT SEARCH TEMPLATE, DROP TEXT SEARCH TEMPLATE

## CREATE TRANSFORM

— 定义一个新的转换

**大纲**

```sql
CREATE \[ OR REPLACE \] TRANSFORM FOR type_name LANGUAGE lang_name (

FROM SQL WITH FUNCTION from_sql_function_name \[ (argument_type \[, \...\]) \],

TO SQL WITH FUNCTION to_sql_function_name \[ (argument_type \[, \...\]) \]

);
```

**简介**

CREATE TRANSFORM定义一种新的转换。 CREATE OR REPLACE TRANSFORM将 创建一种新的转换或者替换现有的定义。

一种转换指定了如何把一种数据类型适配到一种过程语言。例如，在用 PL/Python 编写一个使用hstore类型的函数时，PL/Python 没有关于如何在 Python 环境中表示hstore值的先验知识。 语言的实现通常默认会使用文本表示，但是在一些时候这很不方便，例如 有时可能用一个联合数组或者列表更合适。

一种转换指定了两个函数：

• 一个”from SQL”函数负责将类型从SQL环境转换到语言。这个函数将在该语言编写的一个函数的参数上调用。

• 一个”to SQL”函数负责将类型从语言转换到SQL环境。这个函数将在该语言编写的一个函数的返回值上调用。

没有必要同时提供这些函数。如果有一种没有被指定，将在必要时使用与语言相关的默认行为（为了完全阻止在一个方向上发生转换，你也可以写一个总是报错 的转换函数）。

要创建一种转换，你必须拥有该类型并且具有该类型上的

USAGE特权，拥有该语言上的USAGE特权，并且拥有 from-SQL 和 to-SQL 函数（如果指定了）及其上的EXECUTE特权。

**参数**

type\_name

该转换的数据类型的名称。

lang\_name

该转换的语言的名称。

from\_sql\_function\_name\[(argument\_type \[,...\])\]

将该类型从 SQL 环境转换到该语言的函数名。它必须接受一个 internal类型的参数并且返回类型internal。 实参将是该转换所适用的类型，并且该函数也应该被写成认为它是那种类型（ 但是不允许声明一个返回internal但没有至少一个 internal类型参数的 SQL层函数）。实际的返回值将与 语言的实现相关。如果没有指定参数列表，则函数名在该模式中必须唯一。

to\_sql\_function\_name\[(argument\_type \[,...\])\]

将该类型从语言转换到 SQL 环境的函数名。它必须接受一个 internal类型的参数并且返回该转换所适用的类型。实参值 将与语言的实现相关。如果没有指定参数列表，则函数名在该模式中必须唯一。

**注解**

使用DROP TRANSFORM移除转换。

**示例**

要为类型hstore和语言 plpythonu创建一种转换，先搞定该类型和语言：

```sql
CREATE TYPE hstore \...;

CREATE EXTENSION plpythonu;
```

然后创建需要的函数：

```sql
CREATE FUNCTION hstore_to_plpython(val internal) RETURNS internal

LANGUAGE C STRICT IMMUTABLE

AS \...;

CREATE FUNCTION plpython_to_hstore(val internal) RETURNS hstore

LANGUAGE C STRICT IMMUTABLE

AS \...;
```

最后创建转换把它们连接起来：

```sql
CREATE TRANSFORM FOR hstore LANGUAGE plpythonu (

FROM SQL WITH FUNCTION hstore_to_plpython(internal),

TO SQL WITH FUNCTION plpython_to_hstore(internal)

);
```

实际上，这些命令将被包裹在扩展中。

contrib小节包含了一些提供转换的扩展， 它们可以作为实际的例子。

**兼容性**

这种形式的CREATE TRANSFORM是一种瀚高数据库扩展。在 SQL标准中有一个CREATE TRANSFORM命令，但是它是用于把数据类型适配到 客户端语言。该用法不受 瀚高数据库支持。

**另见**

CREATE FUNCTION, CREATE LANGUAGE, CREATE TYPE, DROP TRANSFORM

## CREATE TRIGGER

— 定义一个新触发器

**大纲**

```sql
CREATE \[ CONSTRAINT \] TRIGGER name { BEFORE \| AFTER \| INSTEAD OF } { event

\[ OR \... \] }

ON table_name

\[ FROM referenced_table_name \]

\[ NOT DEFERRABLE \| \[ DEFERRABLE \] \[ INITIALLY IMMEDIATE \| INITIALLY

DEFERRED \] \]

\[ REFERENCING { { OLD \| NEW } TABLE \[ AS \] transition_relation_name }

\[ \... \] \]

\[ FOR \[ EACH \] { ROW \| STATEMENT } \]

\[ WHEN ( condition ) \]

EXECUTE { FUNCTION \| PROCEDURE } function_name ( arguments )
```

这里的event可以是下列之一：

```sql
INSERT

UPDATE \[ OF column_name \[, \... \] \]

DELETE

TRUNCATE
```

**描述**

CREATE TRIGGER创建一个新触发器。该触发器将被关联到指定的表、视图或者外部表并且在表上发生特定操作时将执行指定的函数function\_name。

该触发器可以被指定为在一行上尝试该操作之前触发（在约束被检查并且INSERT、UPDATE或者DELETE被尝试之前）；也可以在该操作完成之后触发（在约束被检查并且INSERT、UPDATE或者DELETE完成之后）；或者取代该操作（在对一个视图插入、更新或删除的情况中）。如果该触发器在事件之前触发或者取代事件，该触发器可以跳过对当前行的操作或者改变正在被插入的行（只对INSERT以及UPDATE操作）。如果该触发器在事件之后触发，所有更改（包括其他触发器的效果）对该触发器”可见”。

一个被标记为FOR EACH ROW的触发器会对该操作修改的每一行都调用一次。例如，一个影响 10 行的DELETE将导致在目标关系上的任何ON DELETE触发器被独立调用 10 次，也就是为每一个被删除的行调用一次。与此相反，一个被标记为FOR EACH STATEMENT的触发器只会为任何给定的操作执行一次，不管该操作修改多少行（特别地，一个修改零行的操作将仍会导致任何可用的FOR EACH STATEMENT触发器被执行）。

被指定为要触发INSTEAD OF触发器事件的触发器必须被标记为FOR EACH ROW，并且只能被定义在视图上。一个视图上的BEFORE和AFTER触发器必须被标记为FOR EACH STATEMENT。

此外，触发器可以被定义成为TRUNCATE触发，但只能是FOR EACH STATEMENT。

下面的表格总结了哪些触发器类型可以被用在表、视图和外部表上：

表 19.2 触发器类型

| **何时** | **事件** | **行级** | **语句级** |
| --- | --- | --- | --- |
| **BEFORE** | INSERT/UPDATE/DELETE | 表和外部表 | 表、视图和外部表 |
|  | TRUNCATE | — | 表 |
| **AFTER** | INSERT/UPDATE/DELETE | 表和外部表 | 表、视图和外部表 |
|  | TRUNCATE | — | 表 |
| **INSTEAD OF** | INSERT/UPDATE/DELETE | 视图 | — |
|  | TRUNCATE | — | — |

还有，一个触发器定义可以指定一个布尔的 `WHEN` 条件，它将被测试来看看该触发器是否应该被触发。在行级触发器中， `WHEN` 条件可以检查该行的列的新旧值。语句级触发器也可以有 `WHEN` 条件，尽管该特性对于它们不是很有用（因为条件不能引用表中的任何值）。

还有，一个触发器定义可以指定一个布尔的WHEN条件，它将被测试来看看该触发器是否应该被触发。在行级触发器中，WHEN条件可以检查该行的列的新旧值。语句级触发器也可以有WHEN条件，尽管该特性对于它们不是很有用（因为条件不能引用表中的任何值）。

如果有多个同种触发器被定义为相同事件触发，它们将按照名称的字母表顺序被触发。

当CONSTRAINT选项被指定，这个命令会创建一个约束触发器。这和一个常规触发器相同，不过触发该触发器的时机可以使用SET CONSTRAINTS调整。约束触发器必须是表上的AFTER ROW触发器。它们可以在导致触发器事件的语句末尾被引发或者在包含该语句的事务末尾被引发。在后一种情况中，它们被称作是被延迟。一个待处理的延迟触发器的引发也可以使用SET CONSTRAINTS立即强制发生。当约束触发器实现的约束被违背时，约束触发器应该抛出一个异常。

REFERENCING选项启用对传递关系的收集，传递关系是包括被当前SQL语句插入、删除或者修改的行的行集合。这个特性让触发器能看到该语句做的事情的全局视图，而不是一次只看到一行。仅对非约束触发器的AFTER触发器允许这个选项。此外，如果触发器是一个UPDATE触发器，则它不能指定column\_name列表。OLD TABLE仅可以被指定一次，并且只能为在UPDATE或DELETE事件上引发的触发器指定，它创建的传递关系包含有该语句更新或删除的所有行的前映像。类似地，NEW TABLE仅可以被指定一次，并且只能为在UPDATE或INSERT事件上引发的触发器指定，它创建的传递关系包含有该语句更新或插入的所有行的后映像。

SELECT不修改任何行，因此你无法创建SELECT触发器。规则和视图可以为需要SELECT触发器的问题提供可行的解决方案。

**参数**

name

给新触发器的名称。这必须与同一个表上的任何其他触发器相区别。名称不能是模式限定的 — 该触发器会继承它所在表的模式。对于一个约束触发器，这也是使用SET CONSTRAINTS修改触发器行为时要用到的名字。

BEFORE

AFTER

INSTEAD OF

决定该函数是要在事件之前、之后被调用还是会取代该事件。一个约束触发器也能被指定为AFTER。

event

INSERT、UPDATE、DELETE或者TRUNCATE之一，这指定了将要引发该触发器的事件。多个事件可以用OR指定，要求传递关系的时候除外。

对于UPDATE事件，可以使用下面的语法指定一个列的列表：

UPDATE OF column\_name1 \[, column\_name2... \]

只有当至少一个被列出的列出现在UPDATE命令的更新目标中时，或者如果列出的列之一是生成的列，而且依赖的列是UPDATE的目标，该触发器才会触发。

INSTEAD OF UPDATE事件不允许列的列表。在请求传递关系时，也不能指定列的列表。

table\_name

要使用该触发器的表、视图或外部表的名称（可能是模式限定的）。

referenced\_table\_name

约束引用的另一个表的名称（可能是模式限定的）。这个选项被用于外键约束并且不推荐用于一般的目的。这只能为约束触发器指定。

DEFERRABLE

NOT DEFERRABLE

INITIALLY IMMEDIATE

INITIALLY DEFERRED

该触发器的默认时机。这些约束选项的细节可参考CREATE TABLE文档。这只能为约束触发器指定。

REFERENCING

这个关键词紧接在一个或者两个关系名的声明之前，这些关系提供对触发语句的传递关系的访问。

OLD TABLE

NEW TABLE

这个子句指示接下来的关系名是用于前映像传递关系还是后映像传递关系。

transition\_relation\_name

在该触发器中这个传递关系要使用的（未限定）名称。

FOR EACH ROW

FOR EACH STATEMENT

这指定该触发器函数是应该为该触发器事件影响的每一行被引发一次，还是只为每个SQL 语句被引发一次。如果都没有被指定，FOR EACH STATEMENT会是默认值。约束触发器只能被指定为FOR EACH ROW。

condition

一个决定该触发器函数是否将被实际执行的布尔表达式。如果指定了WHEN，只有condition返回true时才会调用该函数。在FOR EACH ROW触发器中，WHEN条件可以分别写OLD.column\_name或者NEW.column\_name来引用列的新旧行值。当然，INSERT触发器不能引用OLD并且DELETE触发器不能引用NEW。

INSTEAD OF触发器不支持WHEN条件。

当前，WHEN表达式不能包含子查询。

注意对于约束触发器，对于WHEN条件的计算不会被延迟，而是直接在行更新操作被执行之后立刻发生。如果该条件计算得不到真，那么该触发器就不会被放在延迟执行的队列中。

function\_name

一个用户提供的函数，它被声明为不用参数并且返回类型trigger，当触发器引发时会执行该函数。

在CREATE TRIGGER的语法中，关键词FUNCTION和PROCEDURE是等效的，但是任何情况下被引用的函数必须是一个函数而不是过程。这里，关键词PROCEDURE的使用是有历史原因的并且已经被废弃。

arguments

一个可选的逗号分隔的参数列表，它在该触发器被执行时会被提供给该函数。参数是字符串常量。简单的名称和数字常量也可以被写在这里，但是它们将全部被转换成字符串。请检查该触发器函数的实现语言的描述来找出在函数内部如何访问这些参数，这可能与普通函数参数不同。

**注解**

要在一个表上创建一个触发器，用户必须具有该表上的TRIGGER特权。用户还必须具有在触发器函数上的EXECUTE特权。

使用DROP TRIGGER移除一个触发器。

当一个列相关的触发器（使用UPDATE OF column\_name语法定义的触发器）的列被列

为UPDATE命令的SET列表目标时，它会被触发。即便该触发器没有被引发，一个列的值也可能改变，因为BEFORE UPDATE触发器对行内容所作的改变不会被考虑。相反，一个诸如UPDATE... SET x = x...的命令将引发一个位于列x上的触发器，即便该列的值没有改变。

在一个BEFORE触发器中，WHEN条件正好在函数被或者将被执行之前被计算，因此使用WHEN与在触发器函数的开始测试同一个条件没有实质上的区别。特别注意该条件看到的NEW行是当前值，虽然可能已被早前的触发器所修改。还有，一个BEFORE触发器的WHEN条件不允许检查NEW行的系统列（例如ctid），因为那些列还没有被设置。

在一个AFTER触发器中，WHEN条件正好在行更新发生之后被计算，并且它决定一个事件是否要被放入队列以便在语句的末尾引发该触发器。因此当一个AFTER触发器的WHEN条件不返回真时，没有必要把一个事件放入队列或者在语句末尾重新取得该行。如果触发器只需要为一些行被引发，就能够显著地加快修改很多行的语句的速度。

在一些情况下，单一的SQL命令可能会引发多种触发器。例如，一个带有ON CONFLICT DO UPDATE子句的INSERT可能同时导致插入和更新操作，因此它将根据需要引发这两种触发器。提供给触发器的传递关系与它们的事件类型有关，因此INSERT触发器将只看到被插入的行，而UPDATE触发器将只看到被更新的行。

由外键强制动作导致的行更新或删除（例如ON UPDATE CASCADE或ON DELETE SET NULL）被当做导致它们的SQL命令的一部分。受影响的表上的相关触发器将被引发，这样就提供了另一种方法让SQL命令引发不直接匹配其类型的触发器。在简单的情况中，请求传递关系的触发器将在一个传递关系中看到由原始SQL命令在其表中做出的所有改变。不过，有些情况中一个请求传递关系的AFTER ROW触发器的存在将导致由单个SQL命令触发的外键强制动作被分成多步，每一步都有其自己的传递关系。在这种情况下，没创建一个传递关系集合都会引发存在的所有语句级触发器，确保那些触发器能够在一个传递关系中看到每个受影响的行一次，并且只看到一次。

只有当视图上的动作被一个行级INSTEAD OF触发器处理时才会引发视图上的语句级触发器。

如果动作被一个INSTEAD规则处理，那么该语句发出的任何语句都会代替提及该视图的原始语句执行，这样将被引发的触发器是替换语句中提及的表上的那些触发器。类似地，如果视图是自动可更新的，则该动作将被处理为把该语句自动重写成在视图基表上的一个动作，这样基表的语句级触发器就是要被引发的。

在分区表上创建一个行级触发器将导致在它所有的现有分区上创建相同的触发器，并且以后创建或者挂接的任何分区也将包含一个相同的触发器。分区表上的触发器只能是AFTER。

修改分区表或者带有继承子表的表会引发挂接到显式提及表的语句级触发器，但不会引发其分区或子表的语句级触发器。相反，行级触发器会在受影响的分区或子表上引发，即便它们在查询中没有被明确提及。如果一个语句级触发器用REFERENCING子句定义有传递关系，则来自所有受影响分区或子表中的行的前后映像都是可见的。在继承子表的情况中，行映像仅包括该触发器所附属的表中存在的列。当前，不能在分区或继承子表上定义带有传递关系的行级触发器。

**示例**

只要表accounts的一行即将要被更新时会执行函数check\_account\_update：

```sql
CREATE TRIGGER check_update

BEFORE UPDATE ON accounts

FOR EACH ROW

EXECUTE FUNCTION check_account_update();
```

下面的例子与上面一个例子相同，但是只在UPDATE命令指定要更新balance列时才执行该函数：

```sql
CREATE TRIGGER check_update

BEFORE UPDATE OF balance ON accounts

FOR EACH ROW

EXECUTE FUNCTION check_account_update();
```

这种形式只有列balance具有真正被改变的值时才执行该函数：

```sql
CREATE TRIGGER check_update

BEFORE UPDATE ON accounts

FOR EACH ROW

WHEN (OLD.balance IS DISTINCT FROM NEW.balance)

EXECUTE FUNCTION check_account_update();
```

调用一个函数来记录accounts的更新，但是只在有东西被改变时才调用：

```sql
CREATE TRIGGER log_update

AFTER UPDATE ON accounts

FOR EACH ROW

WHEN (OLD.\* IS DISTINCT FROM NEW.\*)

EXECUTE FUNCTION log_account_update();
```

为每一个要插入到视图底层表中的行执行函数view\_insert\_row：

```sql
CREATE TRIGGER view_insert

INSTEAD OF INSERT ON my_view

FOR EACH ROW

EXECUTE FUNCTION view_insert_row();
```

为每个语句执行函数check\_transfer\_balances\_to\_zero以确认transfer的行不会有净值增加：

```sql
CREATE TRIGGER transfer_insert

AFTER INSERT ON transfer

REFERENCING NEW TABLE AS inserted

FOR EACH STATEMENT

EXECUTE FUNCTION check_transfer_balances_to_zero();
```

为每一行执行函数check\_matching\_pairs以确认（同一个语句）同时对匹配对做了更改 ：

```sql
CREATE TRIGGER paired_items_update

AFTER UPDATE ON paired_items

REFERENCING NEW TABLE AS newtab OLD TABLE AS oldtab

FOR EACH ROW

EXECUTE FUNCTION check_matching_pairs();
```

**兼容性**

瀚高数据库中的CREATE TRIGGER语句实现了SQL标准的一个子集。目前缺少下列功能：

• 虽然AFTER触发器的传递表名是以标准的方式用REFERENCING子句指定，但REFERENCING子句中不能指定FOR EACH ROW触发器中用到的行变量。它们以依赖于编写该触发器函数的语言的方式可用，但是对任意一种语言来说是固定的。一些语言实际上的行为就像有包含OLD ROW AS OLD NEW ROW AS NEW的REFERENCING子句存在一样。

• 标准允许把传递表与和列相关的UPDATE触发器一起使用，那么应该在传递表中可见的行集合取决于该触发器的列列表。当前瀚高数据库没有实现这一点。

• 瀚高数据库只允许为被触发动作执行一个用户定义的函数。标准允许执行许多其他的 SQL命令作为被触发的动作，例如CREATE TABLE。这种限制可以很容易地通过创建一个执行想要的命令的用户定义函数来绕过。

SQL 指定多个触发器应该以被创建时间的顺序触发。瀚高数据库则使用名称顺序，这被认为更加方便。

SQL 指定级联删除上的BEFORE DELETE触发器在级联的DELETE完成之后引发。瀚高数据库的行为则是BEFORE DELETE总是在删除动作之前引发，即使是一个级联删除。这被认为更加一致。如果BEFORE触发器修改行或者在引用动作引起的更新期间阻止更新，这也是非标准行为。这能导致约束违背或者被存储的数据不遵从引用约束。

使用OR为一个单一触发器指定多个动作的能力是SQL标准的一个瀚高数据库扩展。

为TRUNCATE引发触发器的能力是SQL标准的一个瀚高数据库扩展，在视图上定义语句级触发器的能力也是一样。

CREATE CONSTRAINT TRIGGER是SQL标准的一个瀚高数据库扩展。

**参见**

ALTER TRIGGER, DROP TRIGGER, CREATE FUNCTION, SET CONSTRAINTS

## CREATE TYPE

— 定义一种新的数据类型

**大纲**

```sql
CREATE TYPE name AS

( \[ attribute_name data_type \[ COLLATE collation \] \[, \... \] \] )

CREATE TYPE name AS ENUM

( \[ \'label\' \[, \... \] \] )

CREATE TYPE name AS RANGE (

SUBTYPE = subtype

\[ , SUBTYPE_OPCLASS = subtype_operator_class \]

\[ , COLLATION = collation \]

\[ , CANONICAL = canonical_function \]

\[ , SUBTYPE_DIFF = subtype_diff_function \]

)

CREATE TYPE name (

INPUT = input_function,

OUTPUT = output_function

\[ , RECEIVE = receive_function \]

\[ , SEND = send_function \]

\[ , TYPMOD_IN = type_modifier_input_function \]

\[ , TYPMOD_OUT = type_modifier_output_function \]

\[ , ANALYZE = analyze_function \]

\[ , INTERNALLENGTH = { internallength \| VARIABLE } \]

\[ , PASSEDBYVALUE \]

\[ , ALIGNMENT = alignment \]

\[ , STORAGE = storage \]

\[ , LIKE = like_type \]

\[ , CATEGORY = category \]

\[ , PREFERRED = preferred \]

\[ , DEFAULT = default \]

\[ , ELEMENT = element \]

\[ , DELIMITER = delimiter \]

\[ , COLLATABLE = collatable \]

)

CREATE TYPE name
```

**描述**

CREATE TYPE在当前数据库中注册一种新的 数据类型。定义数据类型的用户将成为它的拥有者。

如果给定一个模式名，那么该类型将被创建在指定的模式中。否则它会被 创建在当前模式中。类型名称必须与同一个模式中任何现有的类型或者域 相区别（因为表具有相关的数据类型，类型名称也必须与同一个模式中任 何现有表的名字不同）。

如上面的语法所示，有五种形式的CREATE TYPE。 它们分别创建组合类型、枚举类型、 范围类型、基础类型或者 shell 类型。下文将依次讨论前四种形式。shell 类型仅仅 是一种用于后面要定义的类型的占位符，通过发出一个不带除类型名之外其 他参数的CREATE TYPE命令可以创建这种类型。在创建范围类型和基础类型时，需要 shell 类型作为一种向前引用。

**组合类型**

第一种形式的CREATE TYPE创建组合类型。 组合类型由一个属性名和数据类型的列表指定。如果属性的数据类型是可 排序的，也可以指定该属性的排序规则。组合类型本质上和表的行类型相 同，但是如果只想定义一种类型，使用 CREATE TYPE避免了创建一个实际的表。单独的组合类型也是很有用的，例如可以作为函数的参数或者返回类型。

为了能够创建组合类型，必须拥有在其所有属性类型上的 USAGE特权。

**枚举类型**

枚举类型需要 一个带引号的标签构成的列表，每一个标签长度必须不超过 NAMEDATALEN字节（在标准的 瀚高数据库编译中是 64 字节）。 可以创建具有零个标签的枚举类型，但是在使用ALTER TYPE 添加至少一个标签之前，不能使用这种类型来保存值。

**范围类型**

范围类型的subtype可以 是任何带有一个相关的B树操作符类（用来决定该范围类型值的顺序）的类型。 通常，子类型的默认B 树操作符类被用来决定顺序。要使用一种非默认操作符 类，可以用 subtype\_opclass指定它的名字。如果子类型是可排序的并且希望在该范围的顺序中使用一种非默认的 排序规则，可以用collation选项来指定。

可选的canonical函数 必须接受一个所定义的范围类型的参数，并且返回同样类型的一个值。在适 用时，它被用来把范围值转换成一种规范的形式。创建一个 canonical函数有点棘 手，因为必须在声明范围类型之前定义它。要这样做，必须首先创建一种 shell 类型，它是一种没有属性只有名称和拥有者的占位符类型。这可以通过 发出不带额外参数的命令CREATE TYPE name来完成。然后可以使用该 shell 类型作为 参数和结果来声明该函数，并且最终用同样的名称来声明范围类型。这会自动 用一种合法的范围类型替换 shell 类型项。

可选的subtype\_diff函数 必须接受两个subtype类型 的值作为参数，并且返回一个double precision值表示两个给定 值之间的差别。虽然这是可选的，但是提供这个函数会让该范围类型列上 GiST 索 引效率更高。

**基础类型**

第四种形式的CREATE TYPE创建一种新的 基本类型（标量类型）。为了创建一种新的基本类型，你必须是一个超级 用户（做这种限制的原因是一种错误的类型定义可能让服务器混淆甚至崩溃）。

参数可以以任意顺序出现（而不仅是按照上面所示的顺序），并且大部分 是可选的。在定义类型前，必须注册两个或者更多函数（使用CREATE FUNCTION）。支持函数 input\_function以及 output\_function 是必需的，而函数 receive\_function、 send\_function、 type\_modifier\_input\_function、 type\_modifier\_output\_function和analyze\_function 是可选的。通常来说这些函数必须是用 C 或者另外一种低层语言编写的。

input\_function将 类型的外部文本表达转换成为该类型定义的操作符和函数所使用的内部表达。 output\_function 执行反向的转换。输入函数可以被声明为有一个cstring 类型的参数，或者有三个类型分别为cstring、 oid、integer的参数。第一个参数是 以 C 字符串存在的输入文本，第二个参数是该类型自身的 OID（对于 数组类型则是其元素类型的 OID），第三个参数是目标列的 typmod（如果知道，不知道则将传递 -1）。输入函数必须 返回一个该数据类型本身的值。通常，一个输入函数应该被声明为 STRICT。 如果不是这样，在读到一个 NULL 输入值时，调用它时第一个参数会是 NULL。在这种情况下，该函数必须仍然返回NULL，除非它发生了错误（ 这种情况主要是想支持域输入函数，它们可能需要拒绝 NULL 输入）。 输出函数必须被声明为有一个新数据类型的参数。输出函数必须返回类型 cstring。对于 NULL 值不会调用输出函数。

T可选的receive\_function 会把类型的外部二进制表达转换成内部表达。如果没有提供这个函数， 该类型不能参与到二进制输入中。二进制表达转换成内部形式代价更低， 然而却更容易移植（例如，标准的整数数据类型使用网络字节序作为外 部二进制表达，而内部表达是机器本地的字节序）。接收函数应该执行 足够的检查以确保该值是有效的。接收函数可以被声明为有一个 internal类型的参数，或者有三个类型分别为 internal、oid、integer的参数。第一个参数是一个指向StringInfo缓冲区的 指针，其中保存着接收到的字节串。

其余可选的参数和文本输入函数的 相同。接收函数必须返回一个该数据类型本身的值。通常，一个接收函 数应该被声明为 STRICT。如果不是这样，在读到一个 NULL 输入值时，调用它时第一个参数会是 NULL。在这种情况下，该函数必须仍然返回 NULL，除非它发生了错误（这种情况主要是想支持域接收函数，它们 可能需要拒绝 NULL 输入）。类似地，可选的 send\_function将 内部表达转换成外部二进制表达。如果没有提供这个函数，该类型将不 能参与到二进制输出中。发送函数必须被声明为有一个新数据类型的参 数。发送函数必须返回类型bytea。对于 NULL 值不 会调用发送函数。

到这里你应该在疑惑输入和输出函数是如何能被声明为具有新类型的 结果或参数的？因为必须在创建新类型之前创建这两个函数。这个问题 的答案是，新类型应该首先被定义为一种shell type， 它是一种占位符类型，除了名称和拥有者之外它没有其他属性。这可以通过不带额外参数的命令CREATE TYPE name做到。然后用 C 写的 I/O 函数可以 被定义为引用这种 shell type。最后，用带有完整定义的 CREATE TYPE把该 shell type 替换为一个完全的、合 法的类型定义，之后新类型就可以正常使用了。

如果该类型支持修饰符（附加在类型声明上的可选约束，例如char(5)或者numeric(30,2)），则需要可选的type\_modifier\_input\_function 以及type\_modifier\_output\_function。 瀚高数据库允许用户定义的类型有一个或者 多个简单常量或者标识符作为修饰符。不过，为了存储在系统目录中，该信息必须 能被打包到一个非负整数值中。所声明的修饰符会被以cstring数组的形式 传递给type\_modifier\_input\_function。 它必须检查该值的合法性（如果值错误就抛出一个错误），如果值正确，要返回 一个非负integer值，它将被存储在”typmod”列中。如果类型没有type\_modifier\_input\_function 则类型修饰符将被拒绝。type\_modifier\_output\_function 把内部的整数 typmod 值转换回正确的形式用于用户显示。它必须返回一个 cstring值，该值就是追加到类型名称后的字符串。例如 numeric的函数可能会返回(30,2)。如果默认的显示格式 就是只把存储的 typmod 整数值放在圆括号内，则允许省略 type\_modifier\_output\_function。

可选的analyze\_function 为该数据类型的列执行与类型相关的统计信息收集。默认情况下，如果 该类型有一个默认的 B-树操作符类，ANALYZE将尝试用类型的”equals”和”less-than”操作符来收集统计信息。 这种行为对于非标量类型并不合适，因此可以通过指定一个自定义分析函数来 覆盖这种行为。分析函数必须被声明为有一个类型为internal的参 数，并且返回一个boolean结果。

虽然只有 I/O 函数和其他为该类型创建的函数才知道新类型的内部表达的细节，但是内部表达的一些属性必须被向 瀚高数据库声明。其中最重要的是 internallength。基本数据类型可以是定长的（这种情况下 internallength是一个正 整数）或者是变长的（把 internallength设置为 VARIABLE，在内部通过把typlen设置为 -1 表示）。 所有变长类型的内部表达都必须以一个 4 字节整数开始，它给出了这个值的总长度，长度域常常是被编码 过的，直接接受它是不明智的）。

可选的标志PASSEDBYVALUE表示这种数据类型的值需要 被传值而不是传引用。传值的类型必须是定长的，并且它们的内部表达不能超 过Datum类型（某些机器上是 4 字节，其他机器上是 8 字节）的 尺寸。

alignment参数指定数据类型的存储对齐要求。允许的值等同于以 1、2、4 或 8 字节边界对齐。注意 变长类型的 alignment 参数必须至少为 4，因为它们需要包含一个 int4作为它们的第一个组成部分。

storage参数允许 为变长数据类型选择存储策略（对定长类型只允许 plain）。plain指定该类型的数 据将总是被存储在线内并且不会被压缩。extended 指定系统将首先尝试压缩一个长的数据值，并且将在数据仍然太长的情 况下把值移出主表行。external允许值被移出主表， 但是系统将不会尝试对它进行压缩。main允许压缩， 但是不鼓励把值移出主表（如果没有其他办法让行的大小变得合适，具有 这种存储策略的数据项仍将被移出主表，但比起 extended以及external项来， 这种存储策略的数据项会被优先考虑保留在主表中）。

除plain之外所有的 storage值都暗示 该数据类型的函数能处理被TOAST 过的值。指定的值 仅仅是决定一种可 TOAST 数据类型的列的默认 TOAST存储策略，用户 可以使用ALTER TABLE SET STORAGE为列选取其他策略。

like\_type参数提供 了另一种方法来指定一种数据类型的基本表达属性：从某种现有的类型中拷贝。internallength、 passedbyvalue、 alignment和 storage的值会从指 定的类型中复制而来（也可以通过在LIKE子句中指定这些属 性的值来覆盖复制过来的值，不过通常并不这么做）。当新类型的低层 实现是以一种现有的类型为”载体”时，用这种方式指定表达特别有用。

category和 preferred参数可以被用来 帮助控制在混淆的情况下应用哪一种隐式造型。每一种数据类型都属于一个用 单个 ASCII 字符命名的分类，并且每一种类型可以是其所属分类中的 “首选”。当有助于解决重载函数或操作符时，解析器将优先 造型到首选类型（但是只能从同类的其他类型造型）。对于没有隐式造型到任意其他类型或者 从任意其他类型造型的类型，让这些设置保持默认即可。不过，对于一组 具有隐式造型的相关类型，把它们都标记为属于同一个类别并且选择一种 或两种”最常用”的类型作为该类别的首选通常是很有用的。在 把一种用户定义的类型增加到一个现有的内建类别（例如数字或者字符串 类型）中时， category参数特别 有用。不过，也可以创建新的全部是用户定义类型的类别。对这样的类别， 可选择除大写字母之外的任何 ASCII 字符。

如果用户希望该数据类型的列被默认为某种非空值，可以指定一个默认值。 默认值可以用DEFAULT关键词指定（这样一个默认值 可以被附加到一个特定列的显式DEFAULT子句覆盖）。

要指定一种类型是数组，用ELEMENT关键词指定该数组元素 的类型。例如，要定义一个 4 字节整数的数组（int4）， 应指定ELEMENT = int4。更多有关数组类型的细节请见下文。

要指定在这种类型数组的外部表达中分隔值的定界符，可以把delimiter设置为一个特定字符。默认 的定界符是逗号（,）。注意定界符是与数组元素类型相 关的，而不是数组类型本身相关。

如果可选的布尔参数 collatable为真，这种 类型的列定义和表达式可能通过使用COLLATE子句携带 有排序规则信息。在该类型上操作的函数的实现负责真正利用这些信息，仅把类型标记为可排序的并不会让它们自动地去使用这类信息。

**数组类型**

只要一种用户定义的类型被创建， 瀚高数据库会自动地创建一种相关的 数组类型，其名称由元素类型的名称前面加上一个下划线组成，并且如果长 度超过NAMEDATALEN字节会自动地被截断（如果 这样生成的名称与一种现有类型的名称冲突，该过程将会重复直到找到一个不冲突的名字）。这种隐式创建的数组类型是变长的并且使用内建的输入和 输出函数（array\_in以及array\_out）。该数组 类型会追随其元素类型的拥有者或所在模式的任何更改，并且在元素类型被 删除时也被删除。

如果系统会自动地创建正确的数组类型，你可能会很合情合理地问为什么 会有一个ELEMENT选项。使用ELEMENT 唯一有用的情况是：当你在创建一种定长类型，它正好在内部是一个多个 相同东西的数组，并且除了计划给该类型提供的整体操作之外，你想要允许用下标来直接访问这些东西。例如，类型point被表示 为两个浮点数，可以使用point\[0\]以及point\[1\] 来访问它们。注意，这种功能只适用于内部形式正好是一个相同定长域 序列的定长类型。可用下标访问的变长类型必须具有 array\_in以及array\_out使用的一般化的内部 表达。由于历史原因（即很明显是错的，但现在改已经太晚了），定长 数组类型的下标是从零开始的，而不是像变长数组那样。

**参数**

name

要创建的类型的名称（可以被模式限定）。

attribute\_name

组合类型的一个属性（列）的名称。

data\_type

要成为组合类型的一个列的现有数据类型的名称。

collation

要关联到组合类型的一列或者范围类型的现有排序规则的名称。

label

一个字符串，它表达与枚举类型的一个值相关的文本标签。

subtype

范围类型的元素类型的名称，范围类型表示的范围属于该类型。

subtype\_operator\_class

用于 subtype 的B 树操作符类的名称。

canonical\_function

范围类型的规范化函数的名称。

subtype\_diff\_function

用于 subtype 的差函数的名称。

input\_function

将数据从类型的外部文本形式转换为内部形式的函数名。

output\_function

将数据从类型的内部形式转换为外部文本形式的函数名。

receive\_function

将数据从类型的外部二进制形式转换成内部形式的函数名。

send\_function

将数据从类型的内部形式转换为外部二进制形式的函数名。

type\_modifier\_input\_function

将类型的修饰符数组转换为内部形式的函数名。

type\_modifier\_output\_function

将类型的修饰符的内部形式转换为外部文本形式的函数名。

analyze\_function

为该数据类型执行统计分析的函数名。

internallength

一个数字常量，它指定新类型的内部表达的字节长度。默认的假设是 它是变长的。

alignment

该数据类型的存储对齐需求。如果被指定，它必须是 char、int2、 int4或者double。默认是 int4。

storage

该数据类型的存储策略。如果被指定，必须是 plain、external、 extended或者main。默认是plain。

like\_type

与新类型具有相同表达的现有数据类型的名称。会从这个类型中复制 internallength、passedbyvalue、 alignment以及 storage的值（ 除非在这个CREATE TYPE命令的其他地方用显式说 明覆盖）。

category

这种类型的分类码（一个 ASCII 字符）。 默认是 “用户定义类型”的'U'。为了创建自定义分类， 你也可以选择其他 ASCII 字符。

preferred

如果这种类型是其类型分类中的优先类型则为真，否则为假。默认 为假。在一个现有类型分类中创建一种新的优先类型要非常小心， 因为这可能会导致行为上令人惊奇的改变。

default

数据类型的默认值。如果被省略，默认值是空。

element

被创建的类型是一个数组，这指定了数组元素的类型。

delimiter

在由这种类型组成的数组中值之间的定界符。

collatable

如果这个类型的操作可以使用排序规则信息，则为真。默认为假。

**注解**

由于一旦数据类型被创建，对该数据类型的使用就没有限制，创建一种基本类型 或者范围类型就等同于在类型定义中提到的函数上授予公共执行权限。对于在类 型定义中有用的函数来说这通常不是问题。但是如果设计一种类型时要求在转换 到外部形式或者从外部形式转换时使用”秘密”信息，你就应该三思而后行。

**示例**

这个例子创建了一种组合类型并且将其用在了一个函数定义中：

```sql
CREATE TYPE compfoo AS (f1 int, f2 text);

CREATE FUNCTION getfoo() RETURNS SETOF compfoo AS \$\$

SELECT fooid, fooname FROM foo

\$\$ LANGUAGE SQL;
```

这个例子创建了一个枚举类型并且将其用在一个表定义中：

```sql
CREATE TYPE bug_status AS ENUM (\'new\', \'open\', \'closed\');

CREATE TABLE bug (

id serial,

description text,

status bug_status

);
```

这个例子创建了一个范围类型：

```sql
CREATE TYPE float8_range AS RANGE (subtype = float8, subtype_diff = float8mi);
```

这个例子创建了基本数据类型box然后将它用在一个表定义中：

```sql
CREATE TYPE box;

CREATE FUNCTION my_box_in_function(cstring) RETURNS box AS \... ;

CREATE FUNCTION my_box_out_function(box) RETURNS cstring AS \... ;

CREATE TYPE box (

INTERNALLENGTH = 16,

INPUT = my_box_in_function,

OUTPUT = my_box_out_function

);

CREATE TABLE myboxes (

id integer,

description box

);
```

如果box的内部结构是四个 float4元素的一个数组，我们可能会使用：

```sql
CREATE TYPE box (

INTERNALLENGTH = 16,

INPUT = my_box_in_function,

OUTPUT = my_box_out_function,

ELEMENT = float4

);
```

这将允许用下标来访问一个 box 值的组件编号。否则该类型的行为和 前面的一样。

这个例子创建了一个大对象类型并且将它用在了一个表定义中：

```sql
CREATE TYPE bigobj (

INPUT = lo_filein, OUTPUT = lo_fileout,

INTERNALLENGTH = VARIABLE

);

CREATE TABLE big_objs (

id integer,

obj bigobj

);
```

**兼容性**

创建组合类型的第一种形式的CREATE TYPE命令符合SQL标准。其他的形式都是瀚高数据库扩展。SQL 标准中的CREATE TYPE语句也定义了其他瀚高数据库中没有实现的形式。

创建一种具有零个属性的组合类型的能力是一种瀚高数据库对标准的背离（类似于 CREATE TABLE中相同的情况）。

**另见**

ALTER TYPE, CREATE DOMAIN, CREATE FUNCTION, DROP TYPE

## CREATE USER

— 定义一个新的数据库角色

**大纲**

```sql
CREATE USER name [ [ WITH ] option [ ... ] ]
```

这里 `option` 可以是：

- `SUPERUSER` | `NOSUPERUSER`
- `CREATEDB` | `NOCREATEDB`
- `CREATEROLE` | `NOCREATEROLE`
- `INHERIT` | `NOINHERIT`
- `LOGIN` | `NOLOGIN`
- `REPLICATION` | `NOREPLICATION`
- `BYPASSRLS` | `NOBYPASSRLS`
- `CONNECTION LIMIT connlimit`
- `[ENCRYPTED] PASSWORD 'password'` | `PASSWORD NULL`
- `VALID UNTIL 'timestamp'`
- `IN ROLE role_name [, ...]`
- `IN GROUP role_name [, ...]`
- `ROLE role_name [, ...]`
- `ADMIN role_name [, ...]`
- `USER role_name [, ...]`
- `SYSID uid`

**描述**

CREATE USER现在是 CREATE ROLE的一个别名。唯一的区别是 CREATE USER中LOGIN 被作为默认值，而NOLOGIN是 CREATE ROLE的默认值。

**兼容性**

CREATE USER语句是一种瀚高数据库扩展。SQL 标准把用户的定义留给实现来解释。

**另见**

CREATE ROLE

## CREATE USER MAPPING

— 定义一个用户到一个外部服务器的新映射

**大纲**

```sql
CREATE USER MAPPING [IF NOT EXISTS] FOR { user_name | USER | CURRENT_USER | PUBLIC }
    SERVER server_name
    [ OPTIONS ( option 'value' [ , ... ] ) ]
```

**描述**

CREATE USER MAPPING定义一个用户 到一个外部服务器的新映射。一个用户映射通常会包含连接信息，外部数据包装器 会使用连接信息和外部服务器中包含的信息一起来访问一个外部数据源。

一个外部服务器的拥有者可以为任何服务器任何用户创建用户映射。还有， 如果一个用户被授予了服务器上的USAGE特权，该用户可以 为他们自己的用户名创建用户映射。

参数

IF NOT EXISTS

如果给定用户到给定外部服务器的映射已经存在，则不要抛出错误。 在这种情况下发出通知。请注意，不能保证现有的用户映射与要创建的映射完全相同。

user\_name

要映射到外部服务器的一个现有用户的名称。

CURRENT\_USER和USER匹配当前用户的名称。 当PUBLIC被指定时，一个所谓的公共映射会被创建，当没有 特定用户的映射可用时将会使用它。

server\_name

将为其创建用户映射的现有服务器的名称。

OPTIONS ( option 'value' \[,... \] )

这个子句指定用户映射的选项。这些选项通常定义该映射实际的用户名和 口令。选项名必须唯一。允许的选项名和值与该服务器的外部数据包装器 有关。

**示例**

为用户bob、服务器foo创建一个用户映射：

```sql
CREATE USER MAPPING FOR bob SERVER foo OPTIONS (user 'bob', password 'secret');
```

兼容性

CREATE USER MAPPING符合 ISO/IEC 9075-9 (SQL/MED)。

**另见**

ALTER USER MAPPING, DROP USER MAPPING, CREATE FOREIGN DATA WRAPPER, CREATE SERVER

## CREATE VIEW

— 定义一个新视图

**大纲**

```sql
CREATE [ OR REPLACE ] [ TEMP | TEMPORARY ] [ RECURSIVE ] VIEW name
    [ ( column_name [, ...] ) ]
    [ WITH ( view_option_name [= view_option_value] [, ...] ) ]
    AS query
    [ WITH [ CASCADED | LOCAL ] CHECK OPTION ]
```

**描述**

CREATE VIEW定义一个查询的视图。该视图不会被 物理上物质化。相反，在每一次有查询引用该视图时，视图的查询都会被运行。

CREATE OR REPLACE VIEW与之相似，但是如果 已经存在一个同名视图，该视图会被替换。新查询必须产生和现有试图查询相同 的列（也就是相同的列序、相同的列名、相同的数据类型），但是它可以在列表 的末尾加上额外的列。产生输出列的计算可以完全不同。

如果给定了一个模式名（例如CREATE VIEW myschema.myview...），那么该视图会被创建在指定的模式中。否则，它会 被创建在当前模式中。临时视图存在于一个特殊模式中，因此创建临时视图时不能 给定一个模式名。视图的名称不能与同一模式中任何其他视图、表、序列、索引或 外部表同名。

参数

TEMPORARY或者TEMP

如果被指定，视图被创建为一个临时视图。在当前会话结束时会自动 删掉临时视图。当临时视图存在时，具有相同名称的已有永久视图对 当前会话不可见，除非用模式限定的名称引用它们。

如果视图引用的任何表是临时的，视图将被创建为临时视图（不管有没有指定TEMPORARY）。

RECURSIVE

创建一个递归视图。语法CREATE RECURSIVE VIEW \[ schema. \] view\_name (column\_names) AS SELECT...; 等效于CREATE VIEW \[ schema. \] view\_name AS WITH RECURSIVE view\_name (column\_names) AS (SELECT...) SELECT column\_names FROM view\_name;

对于一个递归视图必须指定一个视图列名列表。

name

要创建的视图的名字（可以是模式限定的）。

column\_name

要用于视图列的名称列表，可选。如果没有给出，列名会根据查询 推导。

WITH ( view\_option\_name \[= view\_option\_value\] \[,... \] )

这个子句为视图指定一些可选的参数，支持下列参数：

check\_option (string)

这个参数可以是local或者cascaded，并且它 等效于指定 WITH \[ CASCADED | LOCAL \] CHECK OPTION（见下文）。 可以使用ALTER VIEW在一个现有视图上修改这个选项。

security\_barrier (boolean)

如果希望视图提供行级安全性，应该使用这个参数。

query

提供视图的行和列的一个SELECT或者 VALUES命令。

WITH \[ CASCADED | LOCAL \] CHECK OPTION

这个选项控制自动可更新视图的行为。这个选项被指定时，将检查该视图上的INSERT和UPDATE命令以确保新行满足 视图的定义条件（也就是，将检查新行来确保通过视图能看到它们）。如果新行 不满足条件，更新将被拒绝。如果没有指定CHECK OPTION， 会允许该视图上的INSERT和UPDATE命令 创建通过该视图不可见的行。支持下列检查选项：

LOCAL

只根据直接定义在该视图本身的条件检查新行。任何定义在底层基视图上的 条件都不会被检查（除非它们也指定了CHECK OPTION）。

CASCADED

会根据该视图和所有底层基视图上的条件检查新行。如果 CHECK OPTION被指定，并且没有指定 LOCAL和CASCADED，则会假定为 CASCADED。

CHECK OPTION不应该和RECURSIVE视图一起使用。

注意，只有在自动可更新的、没有INSTEAD OF触发器或者 INSTEAD规则的视图上才支持CHECK OPTION。 如果一个自动可更新的视图被定义在一个具有INSTEAD OF 触发器的基视图之上，那么LOCAL CHECK OPTION可以被 用来检查该自动可更新的视图之上的条件，但具有INSTEAD OF 触发器的基视图上的条件不会被检查（一个级联检查选项将不会级联到一个 触发器可更新的视图，并且任何直接定义在一个触发器可更新视图上的检查选项将被忽略）。如果该视图或者任何基础关系具有导致 INSERT或UPDATE命令被重写的 INSTEAD规则，那么在被重写的查询中将忽略所有检查选项， 包括任何来自于定义在带有INSTEAD规则的关系之上的自动 可更新视图的检查。

**注解**

使用DROP VIEW语句删除视图。

要小心视图列的名称和类型将会按照你想要的方式指定。例如：

```sql
CREATE VIEW vista AS SELECT 'Hello World';
```

是不好的形式，因为列名默认为?column?，而且列的数据类型默认为text，这可能不是用户想要的。视图结果中一个字符串更好的风格类似于这样：

```
CREATE VIEW vista AS SELECT text \'Hello World\' AS hello;
```

对视图中引用的表的访问由视图拥有者的权限决定。在某些情况下，这可以 被用来提供安全但是受限的底层表访问。不过，并非所有视图都对篡改是安全的。

在视图中调用的函数会被 同样对待，就好像是直接在使用该视图的查询中调用它们一样。因此，一个 视图的用户必须具有调用视图所使用的全部函数的权限。

当CREATE OR REPLACE VIEW被用在一个现有视图上时，只有该视图的定义 SELECT 规则被改变。其他包括拥有关系、权限和非 SELECT 规则在内的视图属性不会被更改。要替换视图，你必须拥有它（包括 作为拥有角色的一个成员）。

可更新视图

简单视图是自动可更新的：系统将允许在这类视图上以在常规表上相同的方式 使用INSERT、UPDATE以及 DELETE语句。如果一个视图满足以下条件，它就是自动 可更新的：

• 在该视图的FROM列表中刚好只有一项，并且它必须是一个表或者另一个可更新视图。

• 视图定义的顶层不能包含WITH、DISTINCT、 GROUP BY、HAVING、 LIMIT或者OFFSET子句。

• 视图定义的顶层不能包含集合操作（UNION、 INTERSECT或者EXCEPT）。

• 视图的选择列表不能包含任何聚集、窗口函数或者集合返回函数。

一个自动可更新的视图可以混合可更新列以及不可更新列。如果一个列是对底层基本关系中一个可更新列的简单引用，则它是可更新的。否则该列是只读的，并 且在一个INSERT或者UPDATE语句尝试对 它赋值时会报出一个错误。

如果视图是自动可更新的，系统将把视图上的任何INSERT、 UPDATE或者DELETE语句转换成在底层 基本关系上的对应语句。带有ON CONFLICT UPDATE子句的 INSERT语句已经被完全支持。

如果一个自动可更新视图包含一个WHERE条件，该条件会限制 基本关系的哪些行可以被该视图上的UPDATE以及 DELETE语句修改。不过，一个允许被UPDATE 修改的行可能让该行不再满足WHERE条件，并且因此也不再能 从视图中可见。类似地，一个INSERT命令可能插入不满足WHERE条件的基本关系行，并且因此从视图中也看不到这些行 （ON CONFLICT UPDATE可能会类似地影响无法通过该视图见到的现有行）。 CHECK OPTION可以被用来阻止INSERT和UPDATE命令创建这类从视图中无法看到的行。

如果一个自动可更新视图被标记了security\_barrier属性，那么 所有该属性的WHERE条件（以及任何使用标记为 LEAKPROOF的操作符的条件）将在该视图使用者的任何条件 之前计算。注意正因为这样，不会 被最终返回的行（因为它们不会通过用户的WHERE条件）可能仍会结束被锁定的状态。可以用EXPLAIN来查看 哪些条件被应用在关系层面（并且因此不锁定行）以及哪些不会被应用在关系层面。

一个更加复杂的不满足所有这些条件的视图默认是只读的：系统将不允许在 该视图上的插入、更新或者删除。可以通过在该视图上创建一个 INSTEAD OF触发器来获得可更新视图的效果，该触发器必须 把该视图上的尝试的插入等转换成其他表上合适的动作。更多信息请见CREATE TRIGGER。另一种可能性是创建规则（见 CREATE RULE），不过实际中触发器更容易理解和正确使用。

注意在视图上执行插入、更新或删除的用户必须具有该视图上相应的插入、 更新或删除特权。此外，视图的拥有者必须拥有底层基本关系上的相关特权， 但是执行更新的用户并不需要底层基本关系上的任何权限。

**示例**

创建一个由所有喜剧电影组成的视图：

```sql
SELECT \*

FROM films

WHERE kind = \'Comedy\';
```

创建的视图包含创建时film表中的列。尽管\* 被用来创建该视图，后来被加入到该表中的列不会成为该视图的组成部分。

创建带有LOCAL CHECK OPTION的视图：

```sql
CREATE VIEW universal_comedies AS

SELECT \*

FROM comedies

WHERE classification = \'U\'

WITH LOCAL CHECK OPTION;
```

这将创建一个基于comedies视图的视图，只显示 kind = 'Comedy'和classification = 'U'的电影。 如果新行没有classification = 'U'，在该视图中的任何 INSERT或UPDATE尝试将被拒绝， 但是电影的kind将不会被检查。

用CASCADED CHECK OPTION创建一个视图：

```sql
CREATE VIEW pg_comedies AS

SELECT \*

FROM comedies

WHERE classification = \'PG\'

WITH CASCADED CHECK OPTION;
```

这将创建一个检查新行的kind和classification 的视图。

创建一个由可更新列和不可更新列混合而成的视图：

```sql
CREATE VIEW comedies AS

SELECT f.\*,

country_code_to_name(f.country_code) AS country,

(SELECT avg(r.rating)

FROM user_ratings r

WHERE r.film_id = f.id) AS avg_rating

FROM films f

WHERE f.kind = \'Comedy\';
```

这个视图将支持INSERT、UPDATE 以及DELETE。所有来自于films表的列都将是可更新的，而计算列country和avg\_rating 将是只读的。

创建一个由数字 1 到 100 组成的递归视图：

```sql
CREATE RECURSIVE VIEW public.nums_1_100 (n) AS

VALUES (1)

UNION ALL

SELECT n+1 FROM nums_1_100 WHERE n \< 100;
```

注意在这个CREATE中尽管递归的视图名称是方案限定的，但它内部的自引用不是方案限定的。这是因为隐式创建的CTE的名称不能是方案限定的。

**兼容性**

CREATE OR REPLACE VIEW是一种 瀚高数据库的语言扩展。临时 视图的概念也是这样。WITH (... )子句也是一种扩展。

**另见**

ALTER VIEW, DROP VIEW, CREATE MATERIALIZED VIEW

## DEALLOCATE

— 释放一个预备语句

**大纲**

```sql
DEALLOCATE \[ PREPARE \] { name \| ALL }
```

**描述**

DEALLOCATE被用来释放一个之前 准备好的 SQL 语句。如果不显式地释放一个预备语句，会话结束 时会释放它。

更多关于预备语句的信息请见PREPARE。

**参数**

PREPARE

这个关键词会被忽略。

name

要释放的预备语句的名称。

ALL

释放所有预备语句。

**兼容性**

SQL 标准包括一个DEALLOCATE语句，但是只用于嵌入式 SQL。

**另见**

EXECUTE, PREPARE

## DECLARE

— 定义一个游标

**大纲**

```sql
DECLARE name [ BINARY ] [ INSENSITIVE ] [ [ NO ] SCROLL ]
    CURSOR [ { WITH | WITHOUT } HOLD ] FOR query
```

**描述**

DECLARE允许用户创建游标，游标可以被用来在大型查询暂停时检索少量的行。游标被创建后，可以用 `FETCH` 从中取得行。

> **注意：**
> 
> 这个页面描述在 SQL 命令层面上游标的用法。如果想要在 PL/pgSQL函数中使用游标，其规则是不同的。

**参数**

**name**

要创建的游标的名称。

**BINARY**

让游标返回二进制数据而不是返回文本格式数据。

**INSENSITIVE**

指示从游标中检索数据的过程不受游标创建之后在其底层表上发生的更新的影响。在瀚高数据库中，这是默认的行为。因此这个关键词没有实际效果，仅仅被用于兼容 SQL标准。

**SCROLL**  
**NO SCROLL**

`SCROLL` 指定游标可以用非顺序（例如，反向）的方式从中检索行。根据查询的执行计划的复杂度，指定 `SCROLL` 可能导致查询执行时间上的性能损失。 `NO SCROLL` 指定游标不能以非顺序的方式从中检索行。默认是允许在某些情况下滚动，但这和指定 `SCROLL` 不完全相同。详情请见 **注解** 。

**WITH HOLD**  
**WITHOUT HOLD**

`WITH HOLD` 指定该游标在创建它的事务提交之后还能被继续使用。 `WITHOUT HOLD` 指定该游标不能在创建它的事务之外使用。如果两者都没有指定，则默认为 `WITHOUT HOLD` 。

**query**

用于提供该游标返回的行的 `SELECT` 或者 `VALUES` 命令。

关键词 `BINARY` 、 `INSENSITIVE` 和 `SCROLL` 可以以任意顺序出现。

**注解**

普通游标以文本格式返回数据，这和 `SELECT` 产生的数据一样。

`BINARY` 选项指定游标应该以二进制格式返回数据。这减少了服务器和客户端的转换负担，但程序员需要付出更多工作来处理与平台相关的二进制数据格式。例如，如果一个查询从一个整数列中返回一个值一，用一个默认游标将得到一个字符串 `1` ，而使用一个二进制游标将得到该值的四字节内部表示（big-endian 大端字节顺序）。

使用二进制游标时应该小心。很多应用（包括 psql）还没有准备好处理二进制游标，它们仍然期待数据以文本格式到来。

> **注意：**
> 
> 当客户端应用使用”扩展查询”协议发出一个 `FETCH` 命令，绑定协议消息会指定使用文本还是二进制格式检索数据。这种选择会覆盖定义游标时指定的方式。因此在使用扩展查询协议时，这样一个二进制游标的概念实际是被废弃的 — 任何游标都可以被视作文本或者二进制。

除非指定了 `WITH HOLD` ，这个命令创建的游标只能在当前事务中使用。因此，没有 `WITH HOLD` 的 `DECLARE` 在事务块外是没有用的：游标只会生存到该语句结束。因此如果这种命令在事务块之外被使用，瀚高数据库会报告一个错误。定义事务块需要使用 `BEGIN` 和 `COMMIT` （或者 `ROLLBACK` ）。

如果指定了 `WITH HOLD` 并且创建游标的事务成功提交，在同一个会话中的后续事务中还能够继续访问该游标（但是如果创建事务被中止，游标会被移除）。一个用 `WITH HOLD` 创建的游标可以用一个显式的 `CLOSE` 命令关闭，或者会话结束时它也会被关闭。在当前的实现中，由一个被保持游标表示的行会被复制到一个临时文件或者内存区域中，这样它们才会在后续事务中保持可用。

当查询包括 `FOR UPDATE` 或 `FOR SHARE` 时，不能指定 `WITH HOLD` 。

在定义一个将被反向取元组的游标时，应该指定 `SCROLL` 选项。这是SQL标准所要求的。

不过，为了和早期版本兼容，如果游标的查询计划足够简单到支持它不需要额外的开销，瀚高数据库会允许在没有 `SCROLL` 的情况下反向取元组。不过，建议应用开发者不要依赖于从没有用 `SCROLL` 创建的游标中反向取元组。如果指定了 `NO SCROLL` ，那么任何情况下都不允许反向取元组。

当查询包括 `FOR UPDATE` 或 `FOR SHARE` 时，也不允许反向取元组。因此在这种情况下不能指定 `SCROLL` 。

> **小心：**
> 
> 如果可滚动和 `WITH HOLD` 游标调用了任何不稳定的函数，它们可能给出预期之外的结果。当重新取得一个之前取得过的行时，那些函数会被重新执行，这可能导致得到与第一次不同的结果。对这类情况的一种变通方法是，声明游标为 `WITH HOLD` 并且在从其中读取任何行之前提交事务。这将强制该游标的整个输出被物化在临时存储中，这样针对每一行只会执行一次不稳定函数。

如果游标的查询包括 `FOR UPDATE` 或者 `FOR SHARE` ，那么被返回的行会在它们第一次被取得时被锁定，这和带有这些选项的常规 `SELECT` 命令一样。此外，被返回的行将是最新的版本，因此这些选项提供了被 SQL 标准称为”敏感游标”的等效体（把 `INSENSITIVE` 与 `FOR UPDATE` 或者 `FOR SHARE` 一起指定是错误）。

> **小心：**
> 
> 如果游标要和 `UPDATE ... WHERE CURRENT OF` 或者 `DELETE ... WHERE CURRENT OF` 一起使用，通常推荐使用 `FOR UPDATE` 。使用 `FOR UPDATE` 可以阻止其他会话在行被取得和被更新之间修改行。如果没有 `FOR UPDATE` ，当行在游标创建后被更改后，一个后续的 `WHERE CURRENT OF` 命令将不会产生效果。
> 
> 另一个使用 `FOR UPDATE` 的原因是，如果没有它，当游标查询不符合 SQL 标准的”简单可更新”规则时，后续的 `WHERE CURRENT OF` 可能会失败（特别地，该游标必须只引用一个表并且没有使用分组或者 `ORDER BY` ）。不是简单可更新的游标可能成功也可能不成功，这取决于计划选择的细节。因此在最坏的情况下，应用可能会在测试时成功但是在生产中失败。如果指定了 `FOR UPDATE` ，则保证游标是可更新的。
> 
> 不把 `FOR UPDATE` 和 `WHERE CURRENT OF` 一起用的主要原因是，需要游标时可滚动的或者对于后续更新不敏感（也就是说，继续显示旧的数据）。如果这是你的需求，应密切关注上述警示。

SQL 标准只对嵌入式SQL中的游标做出了规定。瀚高数据库服务器没有为游标实现 `OPEN` 语句。当游标被声明时就被认为已经被打开。不过，ECPG（瀚高数据库的嵌入式 SQL 预处理器）支持标准 SQL 游标习惯，包括那些 `DECLARE` 和 `OPEN` 语句。

你可以通过查询 `pg_cursors` 系统视图可以看到所有可用的游标。

**示例**

声明一个游标：

```sql
DECLARE liahona CURSOR FOR SELECT * FROM films;
```

更多游标的例子请见 `FETCH` 。

**兼容性**

SQL 标准认为游标是否默认对底层数据的并发更新敏感是与实现相关的。在瀚高数据库中，默认游标对此是不敏感的，并且可以通过指定 `FOR UPDATE` 让它变得对此敏感。其他产品的行为可能有所不同。

SQL 标准只允许在嵌入式SQL和模块中使用游标。瀚高数据库允许以交互的方式使用游标。

二进制游标是一种瀚高数据库扩展。

**另见**

CLOSE, FETCH, MOVE

## DELETE

— 删除一个表的行

**大纲**

```sql
[ WITH [ RECURSIVE ] with_query [, ...] ]
DELETE FROM [ ONLY ] table_name [ * ] [ [ AS ] alias ]
    [ USING using_list ]
    [ WHERE condition | WHERE CURRENT OF cursor_name ]
    [ RETURNING * | output_expression [ [ AS ] output_name ] [, ...] ]
```

**描述**

DELETE从指定表中删除满足 `WHERE` 子句的行。如果 `WHERE` 子句没有出现，效果将会是删除表中的所有行。结果是一个合法的空表。

> **提示：**
> 
> `TRUNCATE` 提供移除表中所有行的快速机制。

有两种方式可以使用数据库中其他表中包含的信息来删除一个表的行：使用子选择或者在 `USING` 子句中指定额外的表。哪种技术更合适取决于特定的环境。

可选的 `RETURNING` 子句导致 `DELETE` 基于实际被删除的每一行计算并且返回值。任何使用被删除表列或者 `USING` 中提到的其他表的列的表达式都可以被计算。

`RETURNING` 列表的语法和 `SELECT` 的输出列表语法相同。

要从表中删除行，你必须具有其上的 `DELETE` 特权，以及 `USING` 子句中任何表以及其值在 `condition` 中被读取的表上的 `SELECT` 特权。

**参数**

**with\_query**

`WITH` 子句允许你指定一个或者多个子查询，在 `DELETE` 查询中可以用子查询的名字来引用它们。

**table\_name**

要从其中删除行的表名（可以是模式限定的）。如果在表名前指定 `ONLY` ，只会从提到的表中删除匹配的行。如果没有指定 `ONLY` ，还会删除该表的任何继承表中的匹配行。可选地，可以在表名后面指定 `*` 来显式指定要包括继承表。

**alias**

目标表的一个别名。提供别名时，它会完全隐藏该表的真实名称。例如，对于 `DELETE FROM foo AS f` ， `DELETE` 语句的剩余部分都会用 `f` 而不是 `foo` 来引用该表。

**using\_list**

一个表表达式的列表，它允许在 `WHERE` 条件中出现来自其他表的列。这和 `SELECT` 语句的 `FROM` 子句中指定的表列表相似。例如，可以指定表的别名。除非想要进行自连接，否则不要在 `using_list` 再写上目标表。

**condition**

一个返回boolean类型值的表达式。只有让这个表达式返回 `true` 的行才将被删除。

**cursor\_name**

要在 `WHERE CURRENT OF` 情况中使用的游标的名称。最近一次从这个游标中取出的行将被删除。该游标必须是 `DELETE` 的目标表上的非分组查询。注意不能在使用 `WHERE CURRENT OF` 的同时指定一个布尔条件。有关将游标用于 `WHERE CURRENT OF` 的更多信息请见 `DECLARE` 。

**output\_expression**

在每一行被删除后，会被 `DELETE` 计算并且返回的表达式。该表达式可以使用 `table_name` 以及 `USING` 中的表的任何列。写成 `*` 可以返回所有列。

**output\_name**

被返回列的名称。

**输出**

在成功完成时，一个 `DELETE` 命令会返回以下形式的命令标签：

```
DELETE count
```

`count` 是被删除行的数目。注意如果有一个 `BEFORE DELETE` 触发器抑制删除，那么该数目可能小于匹配 `condition` 的行数。如果 `count` 为 0，表示查询没有删除行（这并非一种错误）。

如果 `DELETE` 命令包含 `RETURNING` 子句，则结果会与包含有 `RETURNING` 列表中定义的列和值的 `SELECT` 语句结果相似，这些结果是在被该命令删除的行上计算得来。

**注解**

通过在 `USING` 子句中指定其他的表，瀚高数据库允许在 `WHERE` 条件中引用其他表的列。例如，要删除有一个给定制片人制作的所有电影，可以这样做：

```sql
DELETE FROM films USING producers
  WHERE producer_id = producers.id AND producers.name = 'foo';
```

这里实际发生的事情是在 `films` 和 `producers` 之间进行连接，然后删除所有成功连接的 `films` 行。这种语法不属于标准。更标准的方式是：

```sql
DELETE FROM films
  WHERE producer_id IN (SELECT id FROM producers WHERE name = 'foo');
```

在一些情况下，连接形式比子查询形式更容易书写或者执行更快。

**示例**

删除所有电影，但音乐剧除外：

```sql
DELETE FROM films WHERE kind <> 'Musical';
```

清空表 `films` ：

```sql
DELETE FROM films;
```

删除已完成的任务，返回被删除行的明细：

```sql
DELETE FROM tasks WHERE status = 'DONE' RETURNING *;
```

删除 `tasks` 中游标 `c_tasks` 当前位于其上的行：

```sql
DELETE FROM tasks WHERE CURRENT OF c_tasks;
```

**兼容性**

这个命令符合SQL标准，不过 `USING` 和 `RETURNING` 子句是瀚高数据库扩展，在 `DELETE` 中使用 `WITH` 也是扩展。

**参见**

TRUNCATE

## DISCARD

— 抛弃会话状态

**大纲**

```
DISCARD { ALL \| PLANS \| SEQUENCES \| TEMPORARY \| TEMP }
```

**描述**

DISCARD释放与一个数据库会话相关的内部资源。这个命令有助于部分或者完全重置该会话的状态。有几个子命令来释放不同类型的资源。DISCARD ALL变体把所有 其他形式都包含在内，并且还会重置额外的状态。

**参数**

PLANS

释放所有已缓存的查询计划，强制在下一次使用相关预备语句时重新做计划。

SEQUENCES

丢弃所有已缓存的序列相关的状态，包括 currval()/lastval()信息以及任何还未被nextval()返回的预分配的序列值（预分配序列值的描述请见 CREATE SEQUENCE）；

TEMPORARY or TEMP

删除当前会话中创建的所有临时表。

ALL

释放与当前会话相关的所有临时资源并且把会话重置为初始状态。 当前这和执行以下语句序列的效果相同：

```sql
SET SESSION AUTHORIZATION DEFAULT;

RESET ALL;

DEALLOCATE ALL;

CLOSE ALL;

UNLISTEN \*;

SELECT pg_advisory_unlock_all();

DISCARD PLANS;

DISCARD SEQUENCES;

DISCARD TEMP;
```

**注解**

DISCARD ALL不能在事务块内执行。

**兼容性**

DISCARD是一种瀚高数据库扩展。

## DO

— 执行一个匿名代码块

**大纲**

```sql
DO \[ LANGUAGE lang_name \] code
```

**描述**

DO执行一个匿名代码块，或者换句话说执行一个以一种过程语言编写的瞬时匿名函数。

代码块就好像是一个没有参数并且返回void的函数的函数体。它会被在一次时间内解析并且执行。

可选的LANGUAGE子句可以卸载代码块之前或者之后。

**参数**

code

要被执行的过程语言代码。就像在 CREATE FUNCTION中一样，必须把它指定为一个字符串。推荐使用一个美元引用的文本。

lang\_name

编写该代码的过程语言的名称。如果省略，默认为plpgsql。

**注解**

要使用的过程语言必须已经用CREATE EXTENSION安装在 当前数据库中。默认已经安装了plpgsql，但是其他语言没有被 安装。

用户必须拥有该过程语言的USAGE特权，如果该语言 是不可信的则必须是一个超级用户。这和创建一个该语言的函数对 特权的要求相同。

如果在事务块中执行DO，过程代码则无法执行事务控制语句。只有在自己的事务中执行DO时，才允许使用事务控制语句。

**示例**

把模式public中所有视图上的所有特权授予 给角色webuser：

```sql
DO \$\$DECLARE r record;

BEGIN

FOR r IN SELECT table_schema, table_name FROM information_schema.tables

WHERE table_type = \'VIEW\' AND table_schema = \'public\'

LOOP

EXECUTE \'GRANT ALL ON \' \|\| quote_ident(r.table_schema) \|\| \'.\' \|\|

quote_ident(r.table_name) \|\| \' TO webuser\';

END LOOP;

END\$\$;
```

**兼容性**

SQL 标准中没有DO语句。

**另见**

CREATE LANGUAGE

## DROP ACCESS METHOD

— 移除一种访问方法

**大纲**

```sql
DROP ACCESS METHOD \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

**简介**

DROP ACCESS METHOD移除一种现有的访问方法。只有超级用户能够删除访问方法。

**参数**

IF EXISTS

如果该访问方法不存在，则不会抛出错误。这种情况下会发出一个提示。

name

一种现有的访问方法的名称。

CASCADE

自动删除依赖于该访问方法的对象（例如操作符类、操作符族以及索引），并且接着删除所有依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该访问方法，则拒绝删除它。这是默认设置。

**示例**

删除访问方法heptree：

```sql
DROP ACCESS METHOD heptree;
```

**兼容性**

DROP ACCESS METHOD是一种瀚高数据库扩展。

**另见**

CREATE ACCESS METHOD

## DROP AGGREGATE

— 移除一个聚集函数

**大纲**

```sql
DROP AGGREGATE \[ IF EXISTS \] name ( aggregate_signature ) \[, \...\] \[ CASCADE \|

RESTRICT \]
```

这里aggregate\_signature是：

```
\* \|

\[ argmode \] \[ argname \] argtype \[ , \... \] \|

\[ \[ argmode \] \[ argname \] argtype \[ , \... \] \] ORDER BY \[ argmode \] \[ argname

\] argtype \[ , \... \]
```

**描述**

DROP AGGREGATE移除一个现有的 聚集函数。要执行这个命令，当前用户必须是该聚集函数的拥有者。

**参数**

IF EXISTS

如果该聚集不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有聚集函数的名称（可以是模式限定的）。

argmode

一个参数的模式：IN或VARIADIC。 如果被忽略，默认值是IN。

argname

一个参数的名称。注意DROP AGGREGATE 并不真正关心参数名称，因为决定聚集函数的身份时只需要参数数据类型。

argtype

该聚集函数所操作的一个输入数据类型。要引用一个零参数的聚集函数，写 \*来替代参数说明列表。要引用一个有序集聚集函数，在直接和 聚集参数说明之间写上ORDER BY。

CASCADE

自动删除依赖于该聚集函数的对象（例如使用它的视图），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该聚集函数，则拒绝删除它。这是默认值。

**注解**

ALTER AGGREGATE下描述了另一种引用有序集聚集的语法。

**示例**

要为类型integer移除聚集函数myavg：

```
DROP AGGREGATE myavg(integer);
```

要移除假想集聚集函数myrank，该函数接收一个排序列的 任意列表和直接参数的一个匹配的列表：

```
DROP AGGREGATE myrank(VARIADIC \"any\" ORDER BY VARIADIC \"any\");
```

要在一个命令中删除多个聚合函数：

```
DROP AGGREGATE myavg(integer), myavg(bigint);
```

**兼容性**

在 SQL 标准中没有DROP AGGREGATE语句。

**另见**

ALTER AGGREGATE, CREATE AGGREGATE

## DROP CAST

— 移除一个造型

**大纲**

```
DROP CAST \[ IF EXISTS \] (source_type AS target_type) \[ CASCADE \| RESTRICT \]
```

**描述**

DROP CAST移除一个之前定义好的造型。

要能删除一个造型，你必须拥有源数据类型或目标数据类型。这也是创建一个造型所要求的特权。

**参数**

IF EXISTS

如果该造型不存在则不要抛出一个错误，而是发出一个提示。

source\_type

该造型的源数据类型的名称。

target\_type

该造型的目标数据类型的名称。

CASCADE

RESTRICT

这些关键词没有任何效果，因为在造型上没有依赖性。

**示例**

要移除从类型text到类型int的造型：

```
DROP CAST (text AS int);
```

**兼容性**

DROP CAST命令符合 SQL 标准。

**另见**

CREATE CAST

## DROP COLLATION

— 移除一个排序规则

**大纲**

```
DROP COLLATION \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

描述

DROP COLLATION移除一个之前 定义好的排序规则。要能删除一个排序规则，你必须拥有它。

**参数**

IF EXISTS

如果该排序规则不存在则不要抛出一个错误，而是发出一个提示。

name

排序规则的名称。排序规则名称可以是模式限定的。

CASCADE

自动删除依赖于该排序规则的对象，然后删除所有 依赖于那些对象的对象

RESTRICT

如果有任何对象依赖于该排序规则，则拒绝删除它。这是默认值。

**示例**

要删除名为german的排序规则：

```
DROP COLLATION german;
```

**兼容性**

除了IF EXISTS选项之外， DROP COLLATION命令符合SQL标准。该选项是一个瀚高数据库扩展。

**另见**

ALTER COLLATION, CREATE COLLATION

## DROP CONVERSION

— 移除一个转换

**大纲**

```
DROP CONVERSION \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

**描述**

DROP CONVERSION移除一个之前定义好的 转换。要能删除一个转换，你必须拥有该转换。

**参数**

IF EXISTS

如果该转换不存在则不要抛出一个错误，而是发出一个提示。

name

转换的名称。转换名称可以是模式限定的。

CASCADE

RESTRICT

这些关键词没有任何效果，因为在转换上没有依赖性。

**示例**

要删除名为myname的转换：

```
DROP CONVERSION myname;
```

**兼容性**

在 SQL 标准中没有DROP CONVERSION语句， 但是有一个DROP TRANSLATION语句。还有 对应

的CREATE TRANSLATION语句，它与 瀚高数据库中的CREATE CONVERSION 语句相似。

**另见**

ALTER CONVERSION, CREATE CONVERSION

## DROP DATABASE

— 移除一个数据库

**大纲**

```
DROP DATABASE \[ IF EXISTS \] name
```

**描述**

DROP DATABASE移除一个数据库。它会 移除该数据库的系统目录项并且删除包含数据的文件目录。它只能由数据库 拥有者执行。还有，当你或者任何其他人已经连接到目标数据库时，它不能 被执行（连接到postgres或者任何其他数据库来发出这个命令）。

DROP DATABASE不能被撤销。请小心使用！

**参数**

IF EXISTS

如果该数据库不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的数据库的名称。

**注解**

DROP DATABASE不能在一个事务块内执行。

在连接到目标数据库时，这个命令不能被执行。因此，使用程序 dropdb会更方便，它是这个命令的一个包装器。

**兼容性**

SQL 标准中没有DROP DATABASE语句。

**另见**

CREATE DATABASE

## DROP DOMAIN

— 移除一个域

**大纲**

```
DROP DOMAIN \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

**描述**

DROP DOMAIN移除一个域。只有域的拥有者 才能移除它。

**参数**

IF EXISTS

如果该域不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有域的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该域的对象（例如表列），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该域，则拒绝删除它。这是默认值。

**示例**

要移除域box：

```
DROP DOMAIN box;
```

**兼容性**

除了IF EXISTS选项，这个命令符合 SQL 标准。该选项 是一个瀚高数据库扩展。

**另见**

CREATE DOMAIN, ALTER DOMAIN

## DROP EVENT TRIGGER

— 移除一个事件触发器

**大纲**

```
DROP EVENT TRIGGER \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

**描述**

DROP EVENT TRIGGER移除一个已有的 事件触发器。要执行这个命令，当前用户必须是事件触

发器的拥有者。

**参数**

IF EXISTS

如果该事件触发器不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的事件触发器的名称。

CASCADE

自动删除依赖于该触发器的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该触发器，则拒绝删除它。这是默认值。

**示例**

销毁触发器snitch：

```
DROP EVENT TRIGGER snitch;
```

**兼容性**

在 SQL 标准中没有DROP EVENT TRIGGER语句。

**另见**

CREATE EVENT TRIGGER, ALTER EVENT TRIGGER

## DROP EXTENSION

— 移除一个扩展

**大纲**

```
DROP EXTENSION \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

**描述**

DROP EXTENSION从数据库移除扩展。 删除一个扩展会导致其组成对象也被删除。

你必须拥有该扩展才能使用DROP EXTENSION。

参数

IF EXISTS

如果该扩展不存在则不要抛出一个错误，而是发出一个提示。

name

一个已安装扩展的名称。

CASCADE

自动删除依赖于该扩展的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该扩展（而不是它自己拥有的成员 对象和其他被列在同一个DROP命令中 的扩展），则拒绝删除它。这是默认值。

**示例**

要从当前数据库移除扩展hstore：

```
DROP EXTENSION hstore;
```

如果hstore的任何对象在该数据库库中 正在使用，例如有一个表的列是hstore类型，这个命令都将会失败。加上CASCADE选项可以强制 把这些依赖对象也移除。

**兼容性**

DROP EXTENSION是一个瀚高数据库扩展。

**另见**

CREATE EXTENSION, ALTER EXTENSION

## DROP FOREIGN DATA WRAPPER

— 移除一个外部数据包装器

**大纲**

```
DROP FOREIGN DATA WRAPPER \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

**描述**

DROP FOREIGN DATA WRAPPER 移除一个已有的外部数据包装器。要执行这个命令，当前用户必须是该外部数据包装器的拥有者。

**参数**

IF EXISTS

如果该外部数据包装器不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有外部数据包装器的名称。

CASCADE

自动删除依赖于该外部数据包装器的对象（例如服务器），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该外部数据包装器，则拒绝删除它。这是默认值。

**示例**

删除外部数据包装器dbi：

```
DROP FOREIGN DATA WRAPPER dbi;
```

**兼容性**

DROP FOREIGN DATA WRAPPER 符合 ISO/IEC 9075-9 (SQL/MED)。IF EXISTS子句是一个瀚高数据库扩展。

**另见**

CREATE FOREIGN DATA WRAPPER, ALTER FOREIGN DATA WRAPPER

## DROP FOREIGN TABLE

— 移除一个外部表

**大纲**

```
DROP FOREIGN TABLE \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

**描述**

DROP FOREIGN TABLE移除一个 外部表。只有一个外部表的拥有者才能移除它。

**参数**

IF EXISTS

如果该外部表不存在则不要抛出一个错误，而是发出一个提示。

name

要删除的外部表的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该外部表的对象（例如视图），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该外部表，则拒绝删除它。这是默认值。

**示例**

要销毁两个外部表films 和distributors：

```
DROP FOREIGN TABLE films, distributors;
```

**兼容性**

这个命令符合 ISO/IEC 9075-9 (SQL/MED)，不过该标准只允许每个命令 中删除一个外部表并且没有IF EXISTS选项。该选项是一个瀚高数据库扩展。

**另见**

ALTER FOREIGN TABLE, CREATE FOREIGN TABLE

## DROP FUNCTION

— 移除一个函数

**大纲**

```
DROP FUNCTION \[ IF EXISTS \] name \[ ( \[ \[ argmode \] \[ argname \] argtype

\[, \...\] \] ) \] \[, \...\]

\[ CASCADE \| RESTRICT \]
```

**描述**

DROP FUNCTION移除一个已有函数 的定义。要执行这个命令用户必须是该函数的拥有者。该函数的参数 类型必须被指定，因为多个不同的函数可能会具有相同的函数名和不同的参数列表。

**参数**

IF EXISTS

如果该函数不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有函数的名称（可以是模式限定的）。 如果未指定参数列表，则该名称在其模式中必须是唯一的。

argmode

一个参数的模式：IN、OUT、 INOUT或者VARIADIC。如果被忽略， 则默认为IN。注意DROP FUNCTION并不真正关心 OUT参数，因为决定函数的身份时只需要输入参数。 因此列出IN、INOUT和 VARIADIC参数足以。

argname

一个参数的名称。注意 DROP FUNCTION并不真正关心 参数名称，因为决定函数的身份时只需要参数的数据类型。

argtype

如果函数有参数，这是函数参数的数据类型（可以是模式限定的）。

ASCADE

自动删除依赖于该函数的对象（例如操作符和触发器），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该函数，则拒绝删除它。这是默认值。

**示例**

这个命令移除平方根函数：

```
DROP FUNCTION sqrt(integer);
```

在一个命令中删除多个函数：

```
DROP FUNCTION sqrt(integer), sqrt(bigint);
```

如果函数名称在其模式中是唯一的，则可以在不带参数列表的情况下引用它：

```
DROP FUNCTION update_employee_salaries;
```

请注意，这与

```
DROP FUNCTION update_employee_salaries();
```

不同，后者引用一个零个参数的函数，而第一个变体才可以引用具有任意数量参数的函数，包括零，只要该名称是唯一的。

**兼容性**

该命令符合SQL标准，使用这些瀚高数据库扩展：

• 该标准只允许每个命令删除一个函数。

• IF EXISTS选项

• 能够指定参数模式和名称

**另见**

CREATE FUNCTION, ALTER FUNCTION, DROP PROCEDURE, DROP ROUTINE

## DROP GROUP

— 移除一个数据库角色

**大纲**

```
DROP GROUP \[ IF EXISTS \] name \[, \...\]
```

**描述**

DROP GROUP现在是 DROP ROLE的一个别名。

**兼容性**

在 SQL 标准中没有DROP GROUP语句。

**另见**

DROP ROLE

## DROP INDEX

— 移除一个索引

**大纲**

```
DROP INDEX \[ CONCURRENTLY \] \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

**描述**

DROP INDEX从数据库系统中 移除一个已有的索引。要执行这个命令你必须是该索引的拥有者。

**参数**

CONCURRENTLY

删除索引并且不阻塞在索引基表上的并发选择、插入、更新和删除操作。一个 普通的DROP INDEX会要求该表上的排他锁，这样会阻塞 其他访问直至索引删除完成。通过这个选项，该命令会等待直至冲突事务完成。

在使用这个选项时有一些需要注意的事情。只能指定一个索引名称，并且不支持CASCADE选项（因此，一个支持UNIQUE或者 PRIMARY KEY约束的索引不能以这种方式删除）。还有，常规 的DROP INDEX命令可以在一个事务块内执行，而 DROP INDEX CONCURRENTLY不能。

对于临时表，DROP INDEX始终是非并发的，因为没有其他会话可以访问它们，而且丢弃非并发索引更加便宜。

IF EXISTS

如果该索引不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的索引的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该索引的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该索引，则拒绝删除它。这是默认值。

**示例**

这个命令将移除索引title\_idx：

```
DROP INDEX title_idx;
```

**兼容性**

DROP INDEX是一个 瀚高数据库语言扩展。在 SQL 标准中没有提供索引。

**另见**

CREATE INDEX

## DROP LANGUAGE

— 移除一个过程语言

**大纲**

```
DROP \[ PROCEDURAL \] LANGUAGE \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

**描述**

DROP LANGUAGE移除一个之前注册的过程语言 的定义。你必须是一个超级用户或者该语言的拥有者才能使用 DROP LANGUAGE。

**参数**

IF EXISTS

如果该语言不存在则不要抛出一个错误，而是发出一个提示。

name

一个已有过程语言的名称。为了向前兼容，这个名称可以用单引号包围。

CASCADE

自动删除依赖于该语言的对象（例如该语言中的函数），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该语言，则拒绝删除它。这是默认值。

**示例**

这个命令移除过程语言plsample：

```
DROP LANGUAGE plsample;
```

**兼容性**

在 SQL 标准中没有DROP LANGUAGE语句。

**另见**

ALTER LANGUAGE, CREATE LANGUAGE

## DROP MATERIALIZED VIEW

— 移除一个物化视图

大纲

```
DROP MATERIALIZED VIEW \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP MATERIALIZED VIEW删除一个 现有的物化视图。要执行这个命令你必须是该物化视图的拥有者。

参数

IF EXISTS

如果该物化视图不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的物化视图的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该物化视图的对象（例如其他物化视图或常规视图），然后删除所有依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该物化视图，则拒绝删除它。这是默认值。

示例

这个命令将移除名为order\_summary的物化视图：

```
DROP MATERIALIZED VIEW order_summary;
```

兼容性

DROP MATERIALIZED VIEW是一个瀚高数据库扩展。

另见

CREATE MATERIALIZED VIEW, ALTER MATERIALIZED VIEW, REFRESH MATERIALIZED VIEW

## DROP OPERATOR

— 移除一个操作符

大纲

```
DROP OPERATOR \[ IF EXISTS \] name ( { left_type \| NONE } , { right_type \|

NONE } ) \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP OPERATOR从数据库系统中 删除一个现有的操作符。要执行这个命令，你必须是该操作符的拥有者。

参数

IF EXISTS

如果该操作符不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有的操作符的名称（可以是模式限定的）。

left\_type

该操作符左操作数的数据类型，如果没有左操作数就写 NONE。

right\_type

该操作符右操作数的数据类型，如果没有右操作数就写 NONE。

CASCADE

自动删除依赖于该操作符的对象（例如使用它的视图），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该操作符，则拒绝删除它。这是默认值。

示例

为类型integer移除幂操作符 a^b：

```
DROP OPERATOR \^ (integer, integer);
```

为类型bit移除左一元按位补操作符 ~b：

```
DROP OPERATOR \~ (none, bit);
```

为类型bigint移除右一元阶乘操作符 x!：

```
DROP OPERATOR ! (bigint, none);
```

在一条命令中删除多个操作符：

```
DROP OPERATOR \~ (none, bit), ! (bigint, none);
```

兼容性

SQL 标准中没有DROP OPERATOR语句。

另见

CREATE OPERATOR, ALTER OPERATOR

## DROP OPERATOR CLASS

— 移除一个操作符类

大纲

```
DROP OPERATOR CLASS \[ IF EXISTS \] name USING index_method \[ CASCADE \| RESTRICT \]
```

描述

DROP OPERATOR CLASS删除一个现有的 操作符类。要执行这个命令，你必须是该操作符类的拥有者。

DROP OPERATOR CLASS不会删除任何被 该类引用的操作符或者函数。如果有索引依赖于该操作符类，你将需要指 定CASCADE来完成删除。

参数

IF EXISTS

如果该操作符类不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有的操作符类的名称（可以是模式限定的）。

index\_method

该操作符类适用的索引访问方法的名称。

CASCADE

自动删除依赖于该操作符类的对象（例如索引），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该操作符类，则拒绝删除它。这是默认值。

注解

DROP OPERATOR CLASS将不会删除包含该类的 操作符族，即使该族中已经没有任何成员（特别是由 CREATE OPERATOR CLASS隐式创建的族）。一个 空操作符族是无害的，但是为了整洁你可能希望用 DROP OPERATOR FAMILY移除该操作符族，或者 一开始就使用DROP OPERATOR FAMILY会更好。

示例

移除 B-树操作符类widget\_ops：

```
DROP OPERATOR CLASS widget_ops USING btree;
```

如果有任何使用该操作符类的索引存在，这个命令都不会成功。增加 CASCADE可以把这类索引与该操作符类一起删除。

兼容性

SQL 标准中没有DROP OPERATOR CLASS语句。

另见

ALTER OPERATOR CLASS, CREATE OPERATOR CLASS, DROP OPERATOR FAMILY

## DROP OPERATOR FAMILY

— 移除一个操作符族

大纲

```
DROP OPERATOR FAMILY \[ IF EXISTS \] name USING index_method \[ CASCADE \|

RESTRICT \]
```

描述

DROP OPERATOR FAMILY删除一个 现有的操作符族。要执行这个命令，你必须是该操作符族的拥有者。

DROP OPERATOR FAMILY包括删除 该族所包含的任何操作符类，但是它不会删除该族所引用的任何操作 符或函数。如果有任何依赖于该族中操作符类的索引存在，你将需要指定CASCADE来完成删除。

参数

IF EXISTS

如果该操作符族不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有操作符族的名称（可以是模式限定的）。

index\_method

该操作符族适用的索引访问方法的名称。

CASCADE

自动删除依赖于该操作符族的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该操作符族，则拒绝删除它。这是默认值。

示例

移除 B-树操作符族float\_ops：

```
DROP OPERATOR FAMILY float_ops USING btree;
```

如果有任何使用该族中操作符类的索引存在，这个命令都不会成功。增加 CASCADE可以把这类索引与该操作符族一起删除。

兼容性

SQL 标准中没有DROP OPERATOR FAMILY 语句。

另见

ALTER OPERATOR FAMILY, CREATE OPERATOR FAMILY, ALTER OPERATOR CLASS, CREATE

OPERATOR CLASS, DROP OPERATOR CLASS

## DROP OWNED

— 移除一个数据库角色拥有的数据库对象

大纲

```
DROP OWNED BY { name \| CURRENT_USER \| SESSION_USER } \[, \...\] \[ CASCADE \|

RESTRICT \]
```

描述

DROP OWNED删除当前数据库中被指定 角色之一拥有的所有对象。任何已被授予给给定角色在当前数据库中对 象上或者在共享对象（数据库、表空间）上的特权也将会被收回。

参数

name

其对象将被删除并且其特权将被收回的角色的名称。

CASCADE

自动删除依赖于受影响对象的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何其他数据库对象依赖于一个受影响的对象， 则拒绝删除一个角色所拥有的对象。这是默认值。

注解

DROP OWNED常常被用来为移除一个 或者多个角色做准备。因为DROP OWNED 只影响当前数据库中的对象，通常需要在包含将被移除角色所拥有的对象 的每一个数据库中都执行这个命令。

使用CASCADE选项可能导致这个命令递归去删除由其他 用户所拥有的对象。

REASSIGN OWNED命令是另一种选择，它可以把一个 或多个角色所拥有的所有数据库对象重新授予给其他角色。不过， REASSIGN OWNED不处理其他对象的特权。

角色所拥有的数据库、表空间将不会被移除。

兼容性

DROP OWNED命令是一个瀚高数据库扩展。

另见

REASSIGN OWNED, DROP ROLE

## DROP POLICY

— 从一个表移除一条行级安全性策略

大纲

```
DROP POLICY \[ IF EXISTS \] name ON table_name \[ CASCADE \| RESTRICT \]
```

描述

DROP POLICY从该表移除指定的策略。注意如果从 一个移除了最后一条策略并且该表的行级安全性仍被 ALTER TABLE启用，则默认的否定策略将被使用。 不管该表的策略存在与否，ALTER TABLE... DISABLE ROW LEVEL SECURITY都可以被用来禁用一个表的行级安全性。

参数

IF EXISTS

如果该策略不存在也不抛出一个错误。这种情况下会发出一个提示。

name

要删除的策略的名称。

table\_name

该策略所在的表的名称（可以被模式限定）。

CASCADE

RESTRICT

这些关键词不会产生效果，因为它们不依赖于策略。

示例

要在名为my\_table上删除策略p1：

```
DROP POLICY p1 ON my_table;
```

兼容性

DROP POLICY是一种瀚高数据库扩展。

另见

CREATE POLICY, ALTER POLICY

## DROP PROCEDURE

— 移除一个过程

大纲

```
DROP PROCEDURE \[ IF EXISTS \] name \[ ( \[ \[ argmode \] \[ argname \] argtype

\[, \...\] \] ) \] \[, \...\]

\[ CASCADE \| RESTRICT \]
```

简介

DROP PROCEDURE移除一个现有过程的定义。为了执行这个命令，用户必须是该过程的拥有者。该过程的参数类型必须指定，因为可能存在多个不同的过程具有相同名称和不同参数列表。

参数

IF EXISTS

如果该过程不存在也不抛出一个错误。这种情况下会发出一个提示。

name

现有过程的名称（可以是被方案限定的）。如果没有指定参数列表，则该名称在其所属的方案中必须是唯一的。

argmode

参数的模式：IN或者VARIADIC。如果省略，默认为IN。

argname

参数的名称。注意，其实DROP PROCEDURE并不在意参数名称，因为只需要参数的数据类型来确定过程的身份。

argtype

该过程如果有参数，参数的数据类型（可以是被方案限定的）。

CASCADE

自动删除依赖于该过程的对象，然后接着删除依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该过程，则拒绝删除它。这是默认选项。

示例

```
DROP PROCEDURE do_db_maintenance();
```

兼容性

这个命令符合SQL标准，不过瀚高数据库做了这些扩展：

• 标准仅允许每个命令删除一个过程。

• IF EXISTS选项

• 指定参数模式和名称的能力

另见

CREATE PROCEDURE, ALTER PROCEDURE, DROP FUNCTION, DROP ROUTINE

## DROP PUBLICATION

— 删除一个发布

大纲

```
DROP PUBLICATION \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP PUBLICATION从数据库中删除一个现有的发布。

发布只能被它自己的所有者或超级用户删除。

参数

IF EXISTS

如果发布不存在，不要抛出一个错误。在这种情况下发出一个提示。

name

现有发布的名称。

CASCADE

RESTRICT

这些关键词没有任何作用，因为发布没有依赖关系。

示例

删除一个发布：

```
DROP PUBLICATION mypublication;
```

兼容性

DROP PUBLICATION是一个瀚高数据库扩展。

又见

CREATE PUBLICATION, ALTER PUBLICATION

## DROP ROLE

— 移除一个数据库角色

大纲

```
DROP ROLE \[ IF EXISTS \] name \[, \...\]
```

描述

DROP ROLE移除指定的角色。要删除一个超级用户角色，你必须自己就是一个超级用户。要删除一个非超级用户角色，你必须具有CREATEROLE特权。

如果一个角色仍然被集簇中任何数据库中引用，它就不能被移除。如果尝试 移除将会抛出一个错误。在删除该角色前，你必须删除（或者重新授予所有 权）它所拥有的所有对象并且收回该已经授予给该角色的在其他对象上的特 权。REASSIGN OWNED和DROP OWNED 命令可以用于这个目的。

不过，没有必要移除涉及该角色的角色成员关系。 DROP ROLE会自动收回目标角色在其他角色中的成员 关系，以及其他角色在目标角色中的成员关系。其他角色不会被删除也不会被影响。

参数

IF EXISTS

如果该角色不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的角色的名称。

注解

瀚高数据库包括一个程序dropuser具有和这个命令完全相同的功能（事实 上它会调用这个命令），但是该程序可以从 shell 运行。

示例

要删除一个角色：

```
DROP ROLE jonathan;
```

兼容性

SQL 标准定义了DROP ROLE， 但是它只允许一次删除一个角色并且它指定了和 瀚高数据库不同的特权需求。

另见

CREATE ROLE, ALTER ROLE, SET ROLE

## DROP ROUTINE

— 删除一个例程

大纲

```
DROP ROUTINE \[ IF EXISTS \] name \[ ( \[ \[ argmode \] \[ argname \] argtype

\[, \...\] \] ) \] \[, \...\]

\[ CASCADE \| RESTRICT \]
```

简介

DROP ROUTINE删除一个现有例程的定义，它可以是一个聚集函数、一个普通函数或者过程。

有关参数的描述、更多的示例以及进一步的细节请参考DROP AGGREGATE、DROP FUNCTION以及DROP PROCEDURE。

示例

删除类型integer的例程foo：

```
DROP ROUTINE foo(integer);
```

不管foo是一个聚集、函数或是一个过程，这个命令都能起作用。

兼容性

这个命令符合SQL标准，不过瀚高数据库做了下面这些扩展：

• 标准仅允许每个命令删除一个例程。

• IF EXISTS选项

• 指定参数模式和名称的能力

• 聚集函数是一种扩展。

另见

DROP AGGREGATE, DROP FUNCTION, DROP PROCEDURE, ALTER ROUTINE

注意CREATE ROUTINE命令不存在。

## DROP RULE

— 移除一个重写规则

大纲

```
DROP RULE \[ IF EXISTS \] name ON table_name \[ CASCADE \| RESTRICT \]
```

描述

DROP RULE删除一个重写规则。

参数

IF EXISTS

如果该规则不存在则不要抛出一个错误，而是发出一个提示。

name

要删除的规则的名称。

table\_name

该规则适用的表或视图的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该规则的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该规则，则拒绝删除它。这是默认值。

示例

要删除重写规则newrule：

```
DROP RULE newrule ON mytable;
```

兼容性

DROP RULE是一个 瀚高数据库语言扩展，整个 查询重写系统也是这样。

另见

CREATE RULE, ALTER RULE

## DROP SCHEMA

— 移除一个模式

大纲

```
DROP SCHEMA \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP SCHEMA从数据库中移除模式。

一个模式只能由其拥有者或一个超级用户删除。注意即使拥有者不拥有 该模式中的某些对象，也能删除该模式（以及所有含有的对象）。

参数

IF EXISTS

如果该模式不存在则不要抛出一个错误，而是发出一个提示。

name

一个模式的名称。

CASCADE

自动删除包含在该模式中的对象（表、函数等），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果该模式含有任何对象，则拒绝删除它。这是默认值。

注解

使用CASCADE选项可能会使这条命令移除除 指定模式之外其他模式中的对象。

示例

要从数据库中移除模式mystuff及其中 所包含的对象：

```
DROP SCHEMA mystuff CASCADE;
```

兼容性

DROP SCHEMA完全符合 SQL 标准， 不过该标准只允许在每个命令中删除一个模式并且没有 IF EXISTS选项。该选项是一个瀚高数据库扩展。

另见

ALTER SCHEMA, CREATE SCHEMA

## DROP SEQUENCE

— 移除一个序列

大纲

```
DROP SEQUENCE \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP SEQUENCE移除序数生成器。 一个序列只能被其拥有者或超级用户删除。

参数

IF EXISTS

如果该序列不存在则不要抛出一个错误，而是发出一个提示。

name

一个序列的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该序列的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该序列，则拒绝删除它。这是默认值。

示例

要移除序列serial：

```
DROP SEQUENCE serial;
```

兼容性

DROP SEQUENCE符合 SQL标准，不过该标准只允许每个命令中删除一个 序列并且没有IF EXISTS选项。该选项是一个瀚高数据库扩展。

另见

CREATE SEQUENCE, ALTER SEQUENCE

## DROP SERVER

— 移除一个外部服务器描述符

大纲

```
DROP SERVER \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP SERVER移除一个现有的外部服务器 描述符。要执行这个命令，当前用户必须是该服务器的拥有者。

参数

IF EXISTS

如果该服务器不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有服务器的名称。

CASCADE

自动删除依赖于该服务器的对象（例如用户映射），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该服务器，则拒绝删除它。这是默认值。

示例

如果一个服务器foo存在则删除它：

```
DROP SERVER IF EXISTS foo;
```

兼容性

DROP SERVER符合 ISO/IEC 9075-9 (SQL/MED)。IF EXISTS子句是一个瀚高数据库扩展。

另见

CREATE SERVER, ALTER SERVER

## DROP STATISTICS

— 删除扩展统计

大纲

```
DROP STATISTICS \[ IF EXISTS \] name \[, \...\]
```

描述

DROP STATISTICS删除数据库中的统计对象。 只有统计对象的所有者、模式的所有者或超级用户可以删除统计对象。

参数

IF EXISTS

name

要删除的统计对象的名称（可以有模式修饰）。

示例

删除不同模式中的两个统计对象，如果不存在时不会失败：

```
DROP STATISTICS IF EXISTS

accounting.users_uid_creation,

public.grants_user_role;
```

兼容性

SQL标准中没有DROP STATISTICS命令。

又见

ALTER STATISTICS, CREATE STATISTICS

## DROP SUBSCRIPTION

— 删除一个订阅

大纲

```
DROP SUBSCRIPTION \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

描述

DROP SUBSCRIPTION删除数据库集群中的一个订阅。

只有超级用户才可以删除订阅。

如果订阅与复制槽相关联，就不能在事务块内部执行DROP SUBSCRIPTION。 (可以使用ALTER SUBSCRIPTION取消关联复制槽。)

参数

name

要删除的订阅的名称。

CASCADE

RESTRICT

这些关键词没有任何作用，因为订阅没有依赖关系。

注解

当删除与远程主机（正常状态）上的复制槽相关联的订阅时，DROP SUBSCRIPTION 将连接到远程主机，并尝试删除该复制槽，作为其操作的一部分。这是必要的， 以便释放远程主机上为订阅分配的资源。如果失败，因为远程主机不可访问， 或者因为远程复制槽不能被删除，或者复制槽不存在或从不存在， 则DROP SUBSCRIPTION命令将失败。要在这种情况下继续， 请执行ALTER SUBSCRIPTION... SET (slot\_name = NONE) 来解除复制槽与订阅的关联。之后，DROP SUBSCRIPTION 将不再尝试对远程主机执行任何操作。请注意，如果远程复制槽仍然存在， 则应手动删除该插槽；否则将继续保留WAL，最终可能导致磁盘空间不足。

如果订阅与复制槽相关联，那么不能在事务块内部执行DROP SUBSCRIPTION。

示例

删除一个订阅：

```
DROP SUBSCRIPTION mysub;
```

兼容性

DROP SUBSCRIPTION是一个瀚高数据库扩展。

又见

CREATE SUBSCRIPTION, ALTER SUBSCRIPTION

## DROP TABLE

— 移除一个表

大纲

```
DROP TABLE \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP TABLE从数据库移除表。只有表拥有者、 模式拥有者和超级用户能删除一个表。要清空一个表中的行但是不销毁该表， 可以使用DELETE或者TRUNCATE。

DROP TABLE总是移除目标表的任何索引、规则、 触发器和约束。不过，要删除一个被视图或者另一个表的外键约束所引用的表， 必须指定CASCADE（CASCADE将会把依赖的视图 也完全移除，但是对于外键它将只移除外键约束，而完全不会移除其他表）。

参数

IF EXISTS

如果该表不存在则不要抛出一个错误，而是发出一个提示。

name

要删除的表的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该表的对象（例如视图），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该表，则拒绝删除它。这是默认值。

示例

要销毁两个表films和 distributors：

```
DROP TABLE films, distributors;
```

兼容性

这个命令符合 SQL 标准，不过该标准只允许每个命令删除一个表并且没有 IF EXISTS选项。

该选项是一个瀚高数据库扩展。

另见

ALTER TABLE, CREATE TABLE

## DROP TABLESPACE

— 移除一个表空间

大纲

```
DROP TABLESPACE \[ IF EXISTS \] name
```

描述

DROP TABLESPACE从系统中移除一个表空间。

一个表空间只能被其拥有者或超级用户删除。在一个表空间能被删除前，其中 必须没有任何数据库对象。即使当前数据库中没有对象正在使用该表空间，也 可能有其他数据库的对象存在于其中。还有，如果该表空间被列在任何活动会 话的temp\_tablespaces设置中， DROP也可能会失败，因为可能有临时文件存在其中。

参数

IF EXISTS

如果该表空间不存在则不要抛出一个错误，而是发出一个提示。

name

一个表空间的名称。

注解

DROP TABLESPACE不能在一个事务块内执行。

示例

要从系统移除表空间mystuff：

```
DROP TABLESPACE mystuff;
```

兼容性

DROP TABLESPACE是一个瀚高数据库扩展。

另见

CREATE TABLESPACE, ALTER TABLESPACE

## DROP TEXT SEARCH CONFIGURATION

— 移除一个文本搜索配置

大纲

```
DROP TEXT SEARCH CONFIGURATION \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

描述

DROP TEXT SEARCH CONFIGURATION 删除一个现有的文本搜索配置。要执行这个命令，你必须

是该配置的拥有者。

参数

IF EXISTS

如果该文本搜索配置不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有文本搜索配置的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该文本搜索配置的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该文本搜索配置，则拒绝删除它。这是默认值。

示例

移除文本搜索配置my\_english：

```
DROP TEXT SEARCH CONFIGURATION my_english;
```

如果有任何在to\_tsvector调用中引用该配置的 索引存在，这个命令都不会成功。增加CASCADE 可以把这类索引与该文本搜索配置一起删除。

兼容性

SQL 标准中没有DROP TEXT SEARCH CONFIGURATION 语句。

另见

ALTER TEXT SEARCH CONFIGURATION, CREATE TEXT SEARCH CONFIGURATION

## DROP TEXT SEARCH DICTIONARY

— 移除一个文本搜索字典

大纲

```
DROP TEXT SEARCH DICTIONARY \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

描述

DROP TEXT SEARCH DICTIONARY删除一个 现有的文本搜索字典。要执行这个命令，你必须是该字典的拥有者。

参数

IF EXISTS

如果该文本搜索字典不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有文本搜索字典的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该文本搜索字典的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该文本搜索字典，则拒绝删除它。这是默认值。

示例

移除文本搜索字典english：

```
DROP TEXT SEARCH DICTIONARY english;
```

如果有任何使用该字典的文本搜索配置存在，这个命令都不会成功。增加 CASCADE可以把这类配置与字典一起删除。

兼容性

SQL 标准中没有DROP TEXT SEARCH DICTIONARY 语句。

另见

ALTER TEXT SEARCH DICTIONARY, CREATE TEXT SEARCH DICTIONARY

## DROP TEXT SEARCH PARSER

— 移除一个文本搜索解析器

大纲

```
DROP TEXT SEARCH PARSER \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

描述

DROP TEXT SEARCH PARSER删除一个 现有的文本搜索解析器。你必须作为一个超级用户来使用这个命令。

参数

IF EXISTS

如果该文本搜索解析器不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有文本搜索解析器的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该文本搜索解析器的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该文本搜索解析器，则拒绝删除它。这是默认值。

示例

移除文本搜索解析器my\_parser：

```
DROP TEXT SEARCH PARSER my_parser;
```

如果有任何使用该解析器的文本搜索配置存在，这个命令都不会成功。增加 CASCADE可以把这类配置与解析器一起删除。

兼容性

SQL 标准中没有DROP TEXT SEARCH PARSER 语句。

另见

ALTER TEXT SEARCH PARSER, CREATE TEXT SEARCH PARSER

## DROP TEXT SEARCH TEMPLATE

— 移除一个文本搜索模板

大纲

```
DROP TEXT SEARCH TEMPLATE \[ IF EXISTS \] name \[ CASCADE \| RESTRICT \]
```

描述

DROP TEXT SEARCH TEMPLATE删除一个 现有的文本搜索模板。你必须作为一个超级用户来使用这个命令。

参数

IF EXISTS

如果该文本搜索模板不存在则不要抛出一个错误，而是发出一个提示。

name

一个现有文本搜索模板的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该文本搜索模板的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该文本搜索模板，则拒绝删除它。这是默认值。

示例

移除文本搜索模板thesaurus：

```
DROP TEXT SEARCH TEMPLATE thesaurus;
```

如果有任何使用该模板的文本搜索字典存在，这个命令都不会成功。增加 CASCADE可以把这类字典与模板一起删除。

兼容性

SQL 标准中没有DROP TEXT SEARCH TEMPLATE 语句。

另见

ALTER TEXT SEARCH TEMPLATE, CREATE TEXT SEARCH TEMPLATE

## DROP TRANSFORM

— 移除转换

大纲

```
DROP TRANSFORM \[ IF EXISTS \] FOR type_name LANGUAGE lang_name \[ CASCADE \| RESTRICT \]
```

简介

DROP TRANSFORM移除一个之前定义的转换。

为了删除一种转换，你必须拥有该类型和语言。这些同样也是创建转换所需要的 特权。

参数

IF EXISTS

如果该转换不存在也不要抛出一个错误。这种情况下会发出一个提示。

type\_name

该转换的数据类型的名称。

lang\_name

该转换的语言的名称。

CASCADE

自动删除依赖于该转换的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该转换，则拒绝删除它。这是默认行为。

示例

要删除用于类型hstore和语言plpythonu 的转换：

```
DROP TRANSFORM FOR hstore LANGUAGE plpythonu;
```

兼容性

这种形式的DROP TRANSFORM是一种瀚高数据库扩展。详见 CREATE TRANSFORM。

另见

CREATE TRANSFORM

## DROP TRIGGER

— 移除一个触发器

大纲

```
DROP TRIGGER \[ IF EXISTS \] name ON table_name \[ CASCADE \| RESTRICT \]
```

描述

DROP TRIGGER移除一个现有的触发器定义。 要执行这个命令，当前用户必须是触发器基表的拥有者。

参数

IF EXISTS

如果该触发器不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的触发器的名称。

table\_name

定义了该触发器的表的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该触发器的对象，然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该触发器，则拒绝删除它。这是默认值。

示例

销毁表films上的触发器 if\_dist\_exists：

```
DROP TRIGGER if_dist_exists ON films;
```

兼容性

瀚高数据库中的 DROP TRIGGER语句与 SQL 标准不 兼容。在 SQL 标准中，不同表上也不能有同名的触发器，因此其 命令是简单的DROP TRIGGER name.

另见

CREATE TRIGGER

## DROP TYPE

— 移除一个数据类型

大纲

```
DROP TYPE \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP TYPE移除一种用户定义的数据类型。 只有一个类型的拥有者才能移除它。

参数

IF EXISTS

如果该类型不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的数据类型的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该类型的对象（例如表列、函数、操作符），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该类型，则拒绝删除它。这是默认值。

示例

要移除数据类型box：

```
DROP TYPE box;
```

兼容性

这个命令类似于 SQL 标准中的对应命令，但IF EXISTS子句 是一个瀚高数据库扩展。但要注意 瀚高数据库中 CREATE TYPE命令的很大部分以及数据类 型扩展机制都与 SQL 标准不同。

另见

ALTER TYPE, CREATE TYPE

## DROP USER

— 移除一个数据库角色

大纲

```
DROP USER \[ IF EXISTS \] name \[, \...\]
```

描述

DROP USER现在是 DROP ROLE另一种写法。

兼容性

DROP USER语句是一个瀚高数据库扩展。SQL 标准把 用户的定义留给具体实现自行解释。

另见

DROP ROLE

## DROP USER MAPPING

— 移除一个用于外部服务器的用户映射

大纲

```
DROP USER MAPPING \[ IF EXISTS \] FOR { user_name \| USER \| CURRENT_USER \| PUBLIC }

SERVER server_name
```

描述

DROP USER MAPPING从外部服务器移除 一个已有的用户映射。

一个外部服务器的拥有者可以为该服务器的任何用户删除用户映射。如果 该服务器上的USAGE特权被授予了一个用户，它也能删除 用于它们自己的用户名的用户映射。

参数

IF EXISTS

如果该用户映射不存在则不要抛出一个错误，而是发出一个提示。

user\_name

该映射的用户名。CURRENT\_USER 和USER匹配当前用户的名称。PUBLIC 被用来匹配系统中所有现存和未来的用户名。

server\_name

用户映射的服务器名。

示例

删除一个用户映射bob（服务器foo），如果它存在：

```
DROP USER MAPPING IF EXISTS FOR bob SERVER foo;
```

兼容性

DROP USER MAPPING符合 ISO/IEC 9075-9 (SQL/MED)。IF EXISTS子句是一个瀚高数据库扩展。

另见

CREATE USER MAPPING, ALTER USER MAPPING

## DROP VIEW

— 移除一个视图

大纲

```
DROP VIEW \[ IF EXISTS \] name \[, \...\] \[ CASCADE \| RESTRICT \]
```

描述

DROP VIEW删除一个现有的视图。要执行 这个命令你必须是该视图的拥有者。

参数

IF EXISTS

如果该视图不存在则不要抛出一个错误，而是发出一个提示。

name

要移除的视图的名称（可以是模式限定的）。

CASCADE

自动删除依赖于该视图的对象（例如其他视图），然后删除所有 依赖于那些对象的对象。

RESTRICT

如果有任何对象依赖于该视图，则拒绝删除它。这是默认值。

示例

这个命令将移除名为kinds的视图：

```
DROP VIEW kinds;
```

兼容性

这个命令符合 SQL 标准，不过该标准只允许在每个命令中删除一个视图 并且没有IF EXISTS选项。该选项是一个瀚高数据库扩展。

另见

ALTER VIEW, CREATE VIEW

## END

— 提交当前事务

大纲

```
END \[ WORK \| TRANSACTION \] \[ AND \[ NO \] CHAIN \]
```

描述

END提交当前事务。所有该事务做的更改便得 对他人可见并且被保证发生崩溃时仍然是持久的。这个命令是一种瀚高数据库扩展，它等效于 COMMIT。

参数

WORK

TRANSACTION

可选关键词，它们没有效果。

AND CHAIN

如果规定了AND CHAIN，则立即启动与刚完成事务具有相同事务特征(参见 SET TRANSACTION)的新事务。 否则，没有新事务被启动。

注解

使用ROLLBACK可以中止一个事务。

当不在一个事务中时发出END没有危害，但是会 产生一个警告消息。

示例

要提交当前事务并且让所有更改持久化：

```
END;
```

兼容性

END是一种瀚高数据库扩展，它提供和 COMMIT等效的功能，后者在 SQL 标准中指定。

另见

BEGIN, COMMIT, ROLLBACK

## EXECUTE

— 执行一个预备语句

大纲

```
EXECUTE name \[ ( parameter \[, \...\] ) \]
```

描述

EXECUTE被用来执行一个之前准备好的语句。 由于预备语句只在会话期间存在，该预备语句必须在当前会话中由一个更早 执行的PREPARE语句所创建。

如果创建预备语句的PREPARE语句指定了一些参数， 必须向EXECUTE语句传递一组兼容的参数，否则会 发生错误。注意（与函数不同）预备语句无法基于其参数的类型或者数量重载。 在一个数据库会话中，预备语句的名称必须唯一。

更多创建和使用预备语句的信息请见PREPARE。

参数

name

要执行的预备语句的名称。

parameter

给预备语句的参数的实际值。这必须是一个能得到与该参数数据类型（ 在预备语句创建时决定）兼容的值的表达式。

输出

EXECUTE返回的命令标签是预备语句的命令标签而不是 EXECUTE。

示例

在PREPARE文档的例子小节给出了例子。

兼容性

SQL 标准包括了一个EXECUTE语句， 但是只被用于嵌入式 SQL。这个版本的 EXECUTE语句也用了一种有点不同的语法。

另见

DEALLOCATE, PREPARE

## EXPLAIN

— 显示一个语句的执行计划

大纲

```
EXPLAIN \[ ( option \[, \...\] ) \] statement

EXPLAIN \[ ANALYZE \] \[ VERBOSE \] statement
```

这里 option可以是：

```
ANALYZE \[ boolean \]

VERBOSE \[ boolean \]

COSTS \[ boolean \]

SETTINGS \[ boolean \]

BUFFERS \[ boolean \]

TIMING \[ boolean \]

SUMMARY \[ boolean \]

FORMAT { TEXT \| XML \| JSON \| YAML }
```

描述

这个命令显示瀚高数据库计划器为提供的语句所生成的执行计划。该执行计划会显示将怎样扫描语句中引用的表 — 普通的顺序扫描、索引扫描等等 — 以及在引用多个表时使用何种连接算法来把来自每个输入表的行连接在一起。

显示中最重要的部分是估计出的语句执行代价，它是计划器对于该语句要运行多久的猜测（以任意的代价单位度量，但是习惯上表示取磁盘页面的次数）。事实上会显示两个数字：

在第一行能被返回前的启动代价，以及返回所有行的总代价。对于大部分查询来说总代价是最重要的，但是在一些情景中（如EXISTS中的子查询），计划器将选择更小的启动代价来代替最小的总代价（因为执行器将在得到一行后停止）。此外，如果你用一个LIMIT子句限制返回行的数量，计划器会在终端代价之间做出适当的插值来估计到底哪个计划是真正代价最低的。

ANALYZE选项导致该语句被实际执行，而不仅仅是被计划。那么实际的运行时间统计会被显示出来，包括在每个计划结点上花费的总时间（以毫秒计）以及它实际返回的行数。这对观察计划器的估计是否与实际相近很有用。

**重要：**

记住当使用了 `ANALYZE` 选项时语句会被实际执行。尽管 `EXPLAIN` 将丢弃 `SELECT` 所返回的任何输出，照例该语句的其他副作用还是会发生。如果你希望在 `INSERT` 、 `UPDATE` 、 `DELETE` 、 `CREATE TABLE AS` 或者 `EXECUTE` 上使用 `EXPLAIN ANALYZE` 而不希望它们影响你的数据，可以使用下面的方法：

```sql
BEGIN;
EXPLAIN ANALYZE ...;
ROLLBACK;
```

只有ANALYZE和VERBOSE选项能被指定，并且必须按照上述的顺序，不要把选项列表放在圆括号内。

参数

ANALYZE

执行命令并且显示实际的运行时间和其他统计信息。这个参数默认被设置为FALSE。

VERBOSE

显示关于计划的额外信息。特别是：计划树中每个结点的输出列列表、模式限定的表和函数名、总是把表达式中的变量标上它们的范围表别名，以及总是打印统计信息被显示的每个触发器的名称。这个参数默认被设置为FALSE。

COSTS

包括每一个计划结点的估计启动和总代价，以及估计的行数和每行的宽度。这个参数默认被设置为TRUE。

SETTINGS

包括有关配置参数的信息。具体来说，包括影响查询计划的选项，其值与内置默认值不同。此参数默认为FALSE。

BUFFERS

包括缓冲区使用的信息。特别是：共享块命中、读取、标记为脏和写入的次数、本地块命中、读取、标记为脏和写入的次数、以及临时块读取和写入的次数。一次命中表示避免了一次读取，因为需要的块已经在缓存中找到了。共享块包含着来自于常规表和索引的数据，本地块包含着来自于临时表和索引的数据，而临时块包含着在排序、哈希、物化计划结点和类似情况中使用的短期工作数据。脏块的数量表示被这个查询改变的之前未被修改块的数量，而写入块的数量表示这个后台在查询处理期间从缓存中替换出去的脏块的数量。为一个较高层结点显示的块数包括它的所有子结点所用到的块数。在文本格式中，只会打印非零值。只有当ANALYZE也被启用时，这个参数才能使用。它的默认被设置为FALSE。

TIMING

在输出中包括实际启动时间以及在每个结点中花掉的时间。反复读取系统时钟的负荷在某些系统上会显著地拖慢查询，因此在只需要实际的行计数而不是实际时间时，把这个参数设置为FALSE可能会有用。即便用这个选项关闭结点层的计时，整个语句的运行时间也总是会被度量。只有当ANALYZE也被启用时，这个参数才能使用。它的默认被设置为TRUE。

SUMMARY

在查询计划之后包含摘要信息（例如，总计的时间信息）。当使用ANALYZE 时默认包含摘要信息，但默认情况下不包含摘要信息，但可以使用此选项启用摘要信息。 使用EXPLAIN EXECUTE中的计划时间包括从缓存中获取计划所需的时间 以及重新计划所需的时间（如有必要）。

FORMAT

指定输出格式，可以是 TEXT、XML、JSON 或者 YAML。非文本输出包含和文本输出格式相同的信息，但是更容易被程序解析。这个参数默认被设置为TEXT。

boolean

指定被选中的选项是否应该被打开或关闭。可以写TRUE、ON或1来启用选项，

写FALSE、OFF或0禁用它。boolean值也能被忽略，在这种情况下会假定值为TRUE。

statement

你想查看其执行计划的任何SELECT、INSERT、UPDATE、DELETE、VALUES、EXECUTE、DECLARE、CREATE TABLE AS或者CREATE MATERIALIZED VIEW AS语句。

输出

这个命令的结果是为statement选中的计划的文本描述，可能还标注了执行统计信息。

注解

为了允许瀚高数据库查询计划器在优化查询时能做出合理的知情决策，查询中用到的所有表的pg\_statistic数据应该能保持为最新。通常这个工作会由autovacuum daemon负责自动完成。但是如果一个表最近在内容上有大量的改变，我们可能需要做一次手动的ANALYZE而不是等待 autovacuum 捕捉这些改变。

为了度量执行计划中每个节点的运行时成本，当前的EXPLAIN ANALYZE的当前实现为查询执行增加了性能分析开销。 这样，在一个查询上运行EXPLAIN ANALYZE有时候比正常执行该查询要慢很多。 开销的量取决于该查询的性质，以及使用的平台。最坏的情况会发生在那些自身执行时间很短的结点上，以及在那些具有相对较慢的有关时间的操作系统调用的机器上。

示例

有一个具有单个integer列和 10000 行的表，要显示在其上的一个简单查询的计划：

```
EXPLAIN SELECT \* FROM foo;

QUERY PLAN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Seq Scan on foo (cost=0.00..155.00 rows=10000 width=4)

(1 row)
```

这里有同样一个查询的 JSON 输出格式：

```
EXPLAIN (FORMAT JSON) SELECT \* FROM foo;

QUERY PLAN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\[ +

{ +

\"Plan\": { +

\"Node Type\": \"Seq Scan\",+

\"Relation Name\": \"foo\", +

\"Alias\": \"foo\", +

\"Startup Cost\": 0.00, +

\"Total Cost\": 155.00, +

\"Plan Rows\": 10000, +

\"Plan Width\": 4 +

} +

} +

\]

(1 row)
```

如果有一个索引，并且我们使用了一个带有可索引WHERE条件的查询，EXPLAIN可能会显示一个不同的计划：

```
EXPLAIN SELECT \* FROM foo WHERE i = 4;

QUERY PLAN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Index Scan using fi on foo (cost=0.00..5.98 rows=1 width=4)

Index Cond: (i = 4)

(2 rows)
```

这里是同一查询的 YAML 格式：

```
EXPLAIN (FORMAT YAML) SELECT \* FROM foo WHERE i=\'4\';

QUERY PLAN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\- Plan: +

Node Type: \"Index Scan\" +

Scan Direction: \"Forward\"+

Index Name: \"fi\" +

Relation Name: \"foo\" +

Alias: \"foo\" +

Startup Cost: 0.00 +

Total Cost: 5.98 +

Plan Rows: 1 +

Plan Width: 4 +

Index Cond: \"(i = 4)\"

(1 row)
```

XML 格式我们留给读者做练习。

这里是去掉了代价估计的同样一个计划：

```
EXPLAIN (COSTS FALSE) SELECT \* FROM foo WHERE i = 4;

QUERY PLAN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Index Scan using fi on foo

Index Cond: (i = 4)

(2 rows)
```

这里是一个使用聚集函数的查询的查询计划例子：

```
EXPLAIN SELECT sum(i) FROM foo WHERE i \< 10;

QUERY PLAN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Aggregate (cost=23.93..23.93 rows=1 width=4)

-\> Index Scan using fi on foo (cost=0.00..23.92 rows=6 width=4)

Index Cond: (i \< 10)

(3 rows)
```

这里是一个使用EXPLAIN EXECUTE显示预备查询的执行计划的例子：

```
PREPARE query(int, int) AS SELECT sum(bar) FROM test

WHERE id \> \$1 AND id \< \$2

GROUP BY foo;

EXPLAIN ANALYZE EXECUTE query(100, 200);

QUERY PLAN

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

HashAggregate (cost=9.54..9.54 rows=1 width=8) (actual time=0.156..0.161

rows=11 loops=1)

Group Key: foo

-\> Index Scan using test_pkey on test (cost=0.29..9.29 rows=50 width=8)

(actual time=0.039..0.091 rows=99 loops=1)

Index Cond: ((id \> \$1) AND (id \< \$2))

Planning time: 0.197 ms

Execution time: 0.225 ms

(6 rows)
```

当然，这里显示的有关数字取决于表涉及到的实际内容。还要注意这些数字甚至选中的查询策略，可能在瀚高数据库的不同版本之间变化，因为计划器可能被改进。此外，ANALYZE命令使用随机采样来估计数据统计。因此，在一次新的ANALYZE运行之后，代价估计可能会改变，即便是表中数据的实际分布没有改变也是如此。

兼容性

在 SQL 标准中没有定义EXPLAIN语句。

参见

ANALYZE

## FETCH

— 使用游标从查询中检索行

大纲

```
FETCH \[ direction \[ FROM \| IN \] \] cursor_name
```

其中 direction 可以为空或者以下之一：

```
NEXT

PRIOR

FIRST

LAST

ABSOLUTE count

RELATIVE count

count

ALL

FORWARD

FORWARD count

FORWARD ALL

BACKWARD

BACKWARD count

BACKWARD ALL
```

描述

FETCH从之前创建的一个游标中检索行。

游标具有一个相关联的位置，FETCH会用到该位置。 游标位置可能会位于查询结果的第一行之前、结果中任意行之上或者结果的最后一行之后。在被创建时，游标被定位在第一行之前。在取出一些行后，该游标被定位在最近被取出的行上。如果 FETCH运行超过了可用行的末尾，则该游标会被定位在最后一行之后（如果向后取，则是第一行之前）。 FETCH ALL或者FETCH BACKWARD ALL将总是让游标被定位于最后一行之后或者第一行之前。

NEXT、PRIOR、FIRST、 LAST、ABSOLUTE、RELATIVE 形式会在适当移动游标后取出一行。如果没有这样一行，将返回一个空结果，并且视情况将游标定位在第一行之前或者最后一行之后。

使用FORWARD和BACKWARD的形式会在 向前移动或者向后移动的方向上检索指定数量的行，然后将游标定位在 最后返回的行上（如果count超过可用的行数，则定位 在所有行之后或者之前）。

RELATIVE 0、FORWARD 0以及 BACKWARD 0都会请求检索当前行但不移动游标，也就是 重新取最近被取出的行。 只要游标没有被定位在第一行之前或者最后一行 之后，这种操作都会成功，否则不会返回任何行。

**注意：**

这个页面描述在 SQL 命令层面上对游标的使用。如果想要在 PL/pgSQL函数中使用游标，规则会有所不同。

参数

direction

direction 定义获取方向以及要取得的行数。它可以是下列之一：

NEXT

取出下一行。如果省略direction，这将是默认值。

PRIOR

取出当前位置之前的一行。

FIRST

取出该查询的第一行（和ABSOLUTE 1相同）。

LAST

取出该查询的最后一行（和ABSOLUTE -1相同）。

ABSOLUTE count

取出该查询的第count个行，如果count为负则是从尾部开始取出 第abs(count)个行。如果 count超出范围，将定位在第一行 之前或者最后一行之后。特别地，ABSOLUTE 0 会定位在第一行之前。

RELATIVE count

取出第count个后继行，如果count为负 则是取出前面的第abs(count)个行。RELATIVE 0重新取出当前行（如果有）。

count

取出接下来的count行（和 FORWARD count相同）。

ALL

取出所有剩余的行（和FORWARD ALL相同）。

FORWARD

取出下一行（和NEXT相同）。

FORWARD count

取出接下来的count行。 FORWARD 0重新取出当前行。

FORWARD ALL

取出所有剩下的行。

BACKWARD

取出当前行前面的一行（和PRIOR相同）。

BACKWARD count

取出前面的count行（反向扫描）。 BACKWARD 0会重新取出当前行。

BACKWARD ALL

取出所有当前位置之前的行（反向扫描）。

count

count 是一个可能带有符号的整数常量，它决定要取得的位置或者行数。对于 FORWARD和BACKWARD情况，指定一个负的 count等效于改变 FORWARDhe BACKWARD的意义。

cursor\_name

一个已打开游标的名称。

输出

如果成功完成，FETCH命令返回一个下面形式的命令标签：

FETCH count

count是取得的行数（可能 为零）。注意在psql中，命令标签将不会实际显示， 因为psql会显示被取得的行。

注解

如果想要使用FETCH的任意变体而不使用带有正计数的 FETCH NEXT或者FETCH FORWARD， 应该用SCROLL声明游标。对于简单查询， 瀚高数据库将允许从不带 SCROLL的游标中反向取得行，但最好不要依赖这种行为。 如果游标被声明为带有SCROLL，则不允许反向取得。

用ABSOLUTE取行并不比用相对移动快多少：不管则样， 底层实现都必须遍历所有的中间行。用负绝对值获取的情况更糟：必须读到 查询尾部来找到最后一行，并且接着从那里反向开始遍历。不过，回卷到查询 的开始（正如FETCH ABSOLUTE 0）是很快的。

DECLARE被用来定义游标。使用 MOVE可改变游标位置而不检索数据。

示例

下面的例子用一个游标遍历一个表：

```
BEGIN WORK;

\-- 建立一个游标：

DECLARE liahona SCROLL CURSOR FOR SELECT \* FROM films;

\-- 在游标 liahona 中取出前 5 行：

FETCH FORWARD 5 FROM liahona;

code \| title \| did \| date_prod \| kind \| len

\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\--

BL101 \| The Third Man \| 101 \| 1949-12-23 \| Drama \| 01:44

BL102 \| The African Queen \| 101 \| 1951-08-11 \| Romantic \| 01:43

JL201 \| Une Femme est une Femme \| 102 \| 1961-03-12 \| Romantic \| 01:25

P_301 \| Vertigo \| 103 \| 1958-11-14 \| Action \| 02:08

P_302 \| Becket \| 103 \| 1964-02-03 \| Drama \| 02:28

\-- 取出前面一行：

FETCH PRIOR FROM liahona;

code \| title \| did \| date_prod \| kind \| len

\-\-\-\-\-\--+\-\-\-\-\-\-\-\--+\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\--+\-\-\-\-\-\--

P_301 \| Vertigo \| 103 \| 1958-11-14 \| Action \| 02:08

\-- 关闭游标并且结束事务：

CLOSE liahona;

COMMIT WORK;
```

兼容性

SQL 标准只定义FETCH在嵌入式 SQL 中使用。这里描述的FETCH变体返回数据时就好像数据是 一个SELECT结果，而不是被放在主变量中。 除这一点之外，FETCH完全向上兼容于 SQL标准。

涉及FORWARD和BACKWARD的 FETCH形式，以及形式FETCH count和FETCH ALL（其中FORWARD是隐式的）都是瀚高数据库扩展。

SQL 标准只允许FROM在游标名之前。使用 IN的选项或者完全省去它们是一种扩展。

另见

CLOSE, DECLARE, MOVE

## GRANT

— 定义访问特权

大纲

```
GRANT { { SELECT \| INSERT \| UPDATE \| DELETE \| TRUNCATE \| REFERENCES \| TRIGGER }

\[, \...\] \| ALL \[ PRIVILEGES \] }

ON { \[ TABLE \] table_name \[, \...\]

\| ALL TABLES IN SCHEMA schema_name \[, \...\] }

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { { SELECT \| INSERT \| UPDATE \| REFERENCES } ( column_name \[, \...\] )

\[, \...\] \| ALL \[ PRIVILEGES \] ( column_name \[, \...\] ) }

ON \[ TABLE \] table_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { { USAGE \| SELECT \| UPDATE }

\[, \...\] \| ALL \[ PRIVILEGES \] }

ON { SEQUENCE sequence_name \[, \...\]

\| ALL SEQUENCES IN SCHEMA schema_name \[, \...\] }

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { { CREATE \| CONNECT \| TEMPORARY \| TEMP } \[, \...\] \| ALL \[ PRIVILEGES \] }

ON DATABASE database_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { USAGE \| ALL \[ PRIVILEGES \] }

ON DOMAIN domain_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { USAGE \| ALL \[ PRIVILEGES \] }

ON FOREIGN DATA WRAPPER fdw_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { USAGE \| ALL \[ PRIVILEGES \] }

ON FOREIGN SERVER server_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { EXECUTE \| ALL \[ PRIVILEGES \] }

ON { { FUNCTION \| PROCEDURE \| ROUTINE } routine_name \[ ( \[ \[ argmode \]

\[ arg_name \] arg_type \[, \...\] \] ) \] \[, \...\]

\| ALL { FUNCTIONS \| PROCEDURES \| ROUTINES } IN SCHEMA schema_name

\[, \...\] }

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { USAGE \| ALL \[ PRIVILEGES \] }

ON LANGUAGE lang_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { { SELECT \| UPDATE } \[, \...\] \| ALL \[ PRIVILEGES \] }

ON LARGE OBJECT loid \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { { CREATE \| USAGE } \[, \...\] \| ALL \[ PRIVILEGES \] }

ON SCHEMA schema_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { CREATE \| ALL \[ PRIVILEGES \] }

ON TABLESPACE tablespace_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]

GRANT { USAGE \| ALL \[ PRIVILEGES \] }

ON TYPE type_name \[, \...\]

TO role_specification \[, \...\] \[ WITH GRANT OPTION \]
```

其中role\_specification可以是：

```
\[ GROUP \] role_name

\| PUBLIC

\| CURRENT_USER

\| SESSION_USER

GRANT role_name \[, \...\] TO role_name \[, \...\] \[ WITH ADMIN OPTION \]
```

描述

GRANT命令由两种基本的变体：一种授予在一个数据库对象（表、列、视图、外部表、序列、数据库、外部数据包装器、外部服务器、函数、过程、过程语言、模式或表空间）上的特权，另一个授予一个角色中的成员关系。这些变体在很多方面都相似，但是也有很多不同，所以还是得分别描述它们。

在数据库对象上 GRANT

这种GRANT命令的变体将一个数据库对象上的指定特权交给一个或多个角色。如果有一些已经被授予，这些特权会被加入到它们之中。

关键词PUBLIC指示特权要被授予给所有角色，包括那些可能稍后会被创建的角色。PUBLIC可以被认为是一个被隐式定义的总是包含所有角色的组。任何特定角色都将具有直接授予给它的特权、授予给它作为成员所在的任何角色的特权以及被授予给PUBLIC的特权。

如果指定了WITH GRANT OPTION，特权的接收者可以接着把它授予给其他人。如果没有授权选项，接收者就不能这样做。授权选项不能被授予给PUBLIC。

没有必要把权限授予给一个对象的拥有者（通常就是创建该对象的用户）， 因为拥有者默认具有所有的特权（不过拥有者可能为了安全选择撤回一些 它们自己的特权）。

删除一个对象或者以任何方式修改其定义的权力是不被当作一个可授予特权的，它被固化在拥有者中，并且不能被授予和撤回（不过，相似地效果可以通过授予或者撤回在拥有该对象的角色中的成员关系来实现，见下文）。拥有者也隐式地拥有该对象的所有授权选项。

可能的权限是:

SELECT

INSERT

UPDATE

DELETE

TRUNCATE

REFERENCES

TRIGGER

CREATE

CONNECT

TEMPORARY

EXECUTE

USAGE

特定类型的权限。

TEMP

TEMPORARY的替代拼写。

ALL PRIVILEGES

授予对象的类型可用的所有权限。PRIVILEGES关键词在瀚高数据库中是可选的，尽管它是严格的 SQL 所需要的。

FUNCTION语法适用于简单函数、聚合函数和窗口函数，但不适用于过程；对过程使用PROCEDURE。 或者，使用ROUTINE来引用函数、聚合函数、窗口函数或过程而不管其精确类型。

还有一个选项，可以在一个或多个模式中对所有相同类型的对象授予特权。此功能当前仅支持表、序列、函数和过程。 ALL TABLES也会影响视图和外表，就像特定对象 GRANT命令。

ALL FUNCTIONS也会影响聚合和窗口函数，但不影响过程，就像特定对象GRANT命令一样。 使用 ALL ROUTINES 来包括过程。

角色上的 GRANT

GRANT命令的这种变体把一个角色中的成员关系授予一个或者多个其他角色。一个角色中的成员关系是有意义的，因为它会把授予给一个角色的特权带给该角色的每一个成员。

如果指定了WITH ADMIN OPTION，成员接着可以把该角色中的成员关系授予给其他用户，也可以撤回该角色中的成员关系。如果没有管理选项，普通用户就不能做这些工作。一个角色不被认为持有自身的WITH ADMIN OPTION，但是它可以从一个会话用户匹配该角色的数据库会话中授予或撤回自身中的成员关系。数据库超级用户能够授予或撤回任何角色中任何人的成员关系。具有CREATEROLE特权的角色能够授予或者撤回任何非超级用户角色中的成员关系。

和特权的情况不同，一个角色中的成员关系不能被授予PUBLIC。还要注意这种形式的命令不允许噪声词GROUP。

注解

REVOKE命令被用来撤回访问特权。

用户和组的概念已经被统一到一种单一类型的实体（被称为一个角色）。因此不再需要使用关键词GROUP来标识一个被授权者是一个用户或者一个组。在该命令中仍然允许GROUP，但是它只是一个噪音词而已。

如果一个用户持有特定列或者其所在的整个表的特权， 该用户可以在该列上执行SELECT、 INSERT等命令。在表层面上授予特权 然后对一列撤回该特权将不会按照你希望的运作： 表级别的授权不会受到列级别操作的影响。

当一个对象的非拥有者尝试GRANT该对象上的特权，如果该用户在该对象上什么特权都不拥有，该命令将立刻失败。只要有一些特权可用，该命令将继续，但是它将只授予那些用户具有授权选项的特权。如果不持有授权选项，GRANT ALL PRIVILEGES形式将发出一个警告消息。而如果不持有命令中特别提到的任何特权的授权选项，其他形式将会发出一个警告（原则上这些语句也适用于对象拥有者，但是由于拥有者总是被视为持有所有授权选项，因此这种情况不会发生）。

需要注意的是，数据库超级用户可以访问所有对象而不管对象特权的设置。这可与 Unix 系统中的root权力相提并论。对于root来说，除非绝对必要，使用一个超级用户来操作是不明智的。

如果一个超级用户选择发出一个GRANT或者REVOKE命令，该命令将被执行，好像它是由被影响对象的拥有者发出的一样。特别地，通过这样一个命令授予的特权将好像是由对象拥有者授予的一样（对于角色成员关系，该成员关系好像是由该角色本身授予的一样）。

GRANT以及REVOKE也可以由一个不是受影响对象拥有者的角色完成，不过该角色是拥有该对象的角色的一个成员，或者是在该对象上持有特权的WITH GRANT OPTION的角色的一个成员。

在这种情况下，特权将被记录为由实际拥有该对象的角色授予或者是由持有特权的WITH GRANT OPTION的角色授予。例如，如果表t1被角色g1拥有，u1是它的一个成员，那么u1可以把t1上的特权授予给u2，但是那些特权将好像是直接由g1授予的。角色g1的任何其他成员可以稍后撤回它们。

如果执行GRANT的角色间接地通过多于一条角色成员关系路径持有所需的特权，将不会指定哪一个包含它的角色将被记录为完成了该授权。在这样的情况中，最好使用SET ROLE来成为你想用其做GRANT的特定角色。

授予一个表上的权限不会自动地扩展权限给该表使用的任何序列，包括绑定在SERIAL列上的序列。序列上的权限必须被独立设置。

示例

把表films上的插入特权授予给所有用户：

```
GRANT INSERT ON films TO PUBLIC;
```

把视图kinds上的所有可用特权授予给用户manuel：

```
GRANT ALL PRIVILEGES ON kinds TO manuel;
```

注意虽然上述语句被一个超级用户或者kinds的拥有者执行时确实会授予所有特权，但是当由其他人执行时将只会授予那些执行者拥有授权选项的权限。

把角色admins中的成员关系授予给用户joe：

```
GRANT admins TO joe;
```

兼容性

根据 SQL 标准，ALL PRIVILEGES中的PRIVILEGES关键词是必须的。SQL 标准不支持在每个命令中设置超过一个对象上的特权。

瀚高数据库允许一个对象拥有者 撤回它们拥有的普通特权：例如，一个表拥有者可以通过撤回其自身拥有 的INSERT、UPDATE、DELETE 和TRUNCATE特权让该表对它们自己只读。根据 SQL 标准 这是不可能发生的。原因在于瀚高数据库认为拥有者的特权是由拥有者授予给它们自己的，因此它们也能够撤回它们。在 SQL 标准中，拥有者的特权是有一个假设的实体”\_SYSTEM”所授予 由于不是”\_SYSTEM”，拥有者就不能撤回这些权力。

根据 SQL 标准，授权选项可以被授予给PUBLIC， 瀚高数据库只支持把授权选项授予给角色。

SQL 标准提供了其他对象类型上的USAGE特权：字符集、排序规则、翻译。

在 SQL 标准中，序列只有一个USAGE特权，它控制NEXT VALUE FOR表达式的使用，该表达式等效于 瀚高数据库中的函数nextval。序列的特权SELECT和UPDATE是瀚高数据库扩展。应用序列的USAGE特权到currval函数也是一个瀚高数据库扩展（该函数本身也是）。

数据库、表空间、模式和语言上的特权都是瀚高数据库扩展。

参见

REVOKE, ALTER DEFAULT PRIVILEGES

## IMPORT FOREIGN SCHEMA

— 从一个外部服务器导入表定义

大纲

```
IMPORT FOREIGN SCHEMA remote_schema

\[ { LIMIT TO \| EXCEPT } ( table_name \[, \...\] ) \]

FROM SERVER server_name

INTO local_schema

\[ OPTIONS ( option \'value\' \[, \... \] ) \]
```

简介

IMPORT FOREIGN SCHEMA创建表示存在于 外部服务器上的表的外部表。新外部表将由发出该命令的用户所拥有并且用 匹配远程表的正确的列定义和选项创建。

默认情况下，存在于外部服务器上一个特定模式中的所有表和视图都会被导入。 根据需要，表的列表可以被限制到一个指定的子集，或者可以排除特定的表。 新外部表都被创建在一个必须已经存在的目标模式中。

要使用IMPORT FOREIGN SCHEMA，用户必 须具有外部服务器上的USAGE特权以及在目标模式上的CREATE特权。

参数

remote\_schema

要从哪个远程模式导入。一个远程模式的特定含义依赖于所使用的外部数据包装器。

LIMIT TO ( table\_name \[,...\] )

只导入匹配给定表名之一的外部表。外部模式中其他的表将被忽略。

EXCEPT ( table\_name \[,...\] )

把指定的外部表排除在导入之外。除了列在这里的表之外，外部模式 中存在的所有表都将被导入。

server\_name

要从哪个外部服务器导入。

local\_schema

被导入的外部表将创建在其中的模式。

OPTIONS ( option 'value' \[,...\] )

要在导入期间使用的选项。允许使用的选项名称和值与每一个外部数据包装器 有关。

示例

从服务器film\_server上的远程模式foreign\_films 中导入表定义，把外部表创建在本地模式films中：

```
IMPORT FOREIGN SCHEMA foreign_films

FROM SERVER film_server INTO films;
```

同上，但是只导入两个表actors和 directors（如果存在）：

```
IMPORT FOREIGN SCHEMA foreign_films LIMIT TO (actors, directors)

FROM SERVER film_server INTO films;
```

兼容性

IMPORT FOREIGN SCHEMA命令符合 SQL标准，不过OPTIONS 子句是一种瀚高数据库扩展。

另见

CREATE FOREIGN TABLE, CREATE SERVER

## INSERT

— 在一个表中创建新行

大纲

```
\[ WITH \[ RECURSIVE \] with_query \[, \...\] \]

INSERT INTO table_name \[ AS alias \] \[ ( column_name \[, \...\] ) \]

\[ OVERRIDING { SYSTEM \| USER } VALUE \]

{ DEFAULT VALUES \| VALUES ( { expression \| DEFAULT } \[, \...\] ) \[, \...\]

\| query }

\[ ON CONFLICT \[ conflict_target \] conflict_action \]

\[ RETURNING \* \| output_expression \[ \[ AS \] output_name \] \[, \...\] \]
```

其中 conflict\_target 可以是以下之一：

```
( { index_column_name \| ( index_expression ) } \[ COLLATE collation \]

\[ opclass \] \[, \...\] ) \[ WHERE index_predicate \]

ON CONSTRAINT constraint_name
```

并且 conflict\_action 是以下之一：

```
DO NOTHING

DO UPDATE SET { column_name = { expression \| DEFAULT } \|

( column_name \[, \...\] ) = \[ ROW \] ( { expression \| DEFAULT }

\[, \...\] ) \|

( column_name \[, \...\] ) = ( sub-SELECT )

} \[, \...\]

\[ WHERE condition \]
```

描述

INSERT将新行插入到一个表中。我们可以插入一个或者更多由值表达式指定的行，或者插入来自一个查询的零行或者更多行。

目标列的名称可以以任意顺序列出。如果没有给出列名列表，则有两种确定目标列的可能性。第一种是以被声明的顺序列出该表的所有列。另一种可能性是，如果VALUES 子句或者query只提供N个列，则以被声明的顺序列出该表的前 N列。VALUES 子句或者 query提供的值会被从左至右关联到这些显式或者隐式给出的目标列。

每一个没有出现在显式或者隐式列列表中的列都将被默认填充，如果为该列声明过默认值则用默认值填充，否则用空值填充。

如果任意列的表达式不是正确的数据类型，将会尝试自动类型转换。

ON CONFLICT可以用来指定发生唯一约束或者排除约束违背错误时的替换动作（见下文的ON CONFLICT 子句）。

可选的RETURNING子句让INSERT根据 实际被插入（如果使用了ON CONFLICT DO UPDATE子句， 可能是被更新）的每一行来计算和返回值。这主要用来获取由默认值提供的值，

例如一个序列号。不过，允许在其中包括使用该表列的任何表达式。 RETURNING列表的语法与SELECT的输出 列表的相同。只有被成功地插入或者更新的行才将被返回。例如，如果一行被锁定但由于不满足ON CONFLICT DO UPDATE... WHERE clause condition没有被更新，该行将 不被返回。

为了向表中插入，你必须具有其上的INSERT特权。 如果存在ON CONFLICT DO UPDATE子句，还要求该表上 的UPDATE特权。

如果一个列列表被指定，你只需要其中的列上的INSERT 特权。类似地，在指定了ON CONFLICT DO UPDATE时，你只 需要被列出要更新的列上的UPDATE特权。不过， ON CONFLICT DO UPDATE还要求其值被 ON CONFLICT DO UPDATE表达式或者 condition使用的列上的SELECT特权。

使用RETURNING子句需要RETURNING中提到的所有列的 SELECT权限。 如果使用query子句从查询中插入行， 则当然需要对查询中使用的任何表或列具有SELECT权限。

参数

- 插入

这个小节介绍了在只插入新行时可以使用的参数。 专门用于ON CONFLICT子句的参数会单独介绍。

with\_query

WITH子句允许指定一个或者更多子查询，在 INSERT查询中可以用名称引用这些子查询。

query （SELECT语句）也可以包含一个 WITH子句。在这种情况下 query中可以引用两组with\_query，但是第二个优先级更 高（因为它被嵌套更近）。

table\_name

一个已有表的名称（可以被模式限定）。

alias

table\_name 的替补名称。当提供了一个别名时，它会完全隐藏掉表的实际名称。 当ON CONFLICT DO UPDATE的目标是一个被排除的表时这特别有用，因为那将被当作表示要被插入行的特殊表的名称。

column\_name

名为table\_name的表中的一个列 的名称。如有必要，列名可以用一个子域名或者数组下标限定（指向 一个组合列的某些列中插入会让其他域为空）。当用 ON CONFLICT DO UPDATE引用一列时，不要在一个 目标列的说明中国包括表名。例如， INSERT INTO table\_name... ON CONFLICT DO UPDATE SET table\_name.col = 1是非法的（这遵循UPDATE 的一般行为）。

OVERRIDING SYSTEM VALUE

如果没有这个子句，为定义为GENERATED ALWAYS的标识列指定一个明确的值（不是DEFAULT）就是一种错误。这个子句推翻了这种限制。

OVERRIDING USER VALUE

如果指定这个子句，则会忽略提供给定义为GENERATED BY DEFAULT的标识列的值，并且应用默认的由序列生成的值。

例如，当在表之间拷贝值时，这个子句有能派上用场。INSERT INTO tbl2 OVERRIDING USER VALUE SELECT \* FROM tbl1将从tbl1中拷贝所有在tbl2中不是标识列的列，而tbl2中标识列的值将由与tbl2关联的序列产生。

DEFAULT VALUES

所有列都将被其默认值填充（例如这种形式下不允许OVERRIDING子句）。

expression

要赋予给相应列的表达式或者值。

DEFAULT

相应的列将被其默认值填充。

query

提供要被插入行的查询（SELECT语句）。 其语法描述请参考SELECT语句。

output\_expression

在每一行被插入或更新后由INSERT命令计算并且返回的 表达式。该表达式可以使用table\_name 指定的表中的任何列。写成\*可返回被插入或更新行的所有列。

output\_name

要用于被返回列的名称。

- ON CONFLICT 子句

可选的ON CONFLICT子句为出现唯一性违背或排除约束违背错误时提供另一种可供选择的动作。对于每一个要插入的行，不管是插入进行下去还是由conflict\_target 指定的一个仲裁者约束或者索引被违背，都会采取可供选择的conflict\_action。 ON CONFLICT DO NOTHING简单地把避免插入行。 ON CONFLICT DO UPDATE则会 更新与要插入的行冲突的已有行。

conflict\_target可以执行唯一索引推断。在执行推断时，它由一个或者多个index\_column\_name 列或者 index\_expression 表达式以及一个可选的 index\_predicate构成。所有刚好包含 conflict\_target指定的列/表达式的table\_name唯一索引（不管顺序）都会被推断为（选择为）仲裁者索引。如果指定了 index\_predicate，它必须满足仲裁者索引（也是推断过程的一个进一步的要求）。注意这意味着如果 有一个满足其他条件的非部分唯一索引（没有谓词的唯一索引）可用，它将被 推断为仲裁者（并且会被ON CONFLICT使用）。如果推断 尝试不成功，则会发生一个错误。

ON CONFLICT DO UPDATE保证一个原子的 INSERT或者 UPDATE结果。在没有无关错误的前提下，这两种 结果之一可以得到保证，即使在很高的并发度也能保证。这也可以被称作 UPSERT — “UPDATE 或 INSERT”。

conflict\_target

通过选择仲裁者索引来指定哪些行与 ON CONFLICT在其上采取可替代动作的行相冲突。要么执行唯一索引推断，要么显式命名一个 约束。对于ON CONFLICT DO NOTHING来说， 它对于指定一个conflict\_target是可选的。 在被省略时，与所有有效约束（以及唯一索引）的冲突都会被处理。对于 ON CONFLICT DO UPDATE，必须 提供一个conflict\_target。

conflict\_action

conflict\_action指定一个可替换的 ON CONFLICT动作。它可以是 DO NOTHING，也可以是一个指定在冲突情况下 要被执行的UPDATE动作细节的DO UPDATE子句。ON CONFLICT DO UPDATE中的SET和 WHERE子句能够使用该表的名称（或者别名） 访问现有的行，并且可以用特殊的被排除 表访问要插入的行。这个动作要求被排除 列所在目标表的任何列上的SELECT特权。

注意所有行级BEFORE INSERT触发器的效果都会 反映在被排除值中，因为那些效果可能会 让该行避免被插入。

index\_column\_name

一个table\_name列 的名称。它被用来推断仲裁者索引。它遵循CREATE INDEX格式。这要求 index\_column\_name 上的SELECT特权。

index\_expression

和index\_column\_name类似，但是 被用来推断出现在索引定义中的table\_name列（非简单列）上的 表达式。遵循CREATE INDEX格式。这要求 任何出现在index\_expression中的列上的 SELECT特权。

collation

指定时，强制相应的index\_column\_name或 index\_expression 使用一种特定的排序规则以便在推断期间能被匹配上。通常 会被省略，因为排序规则通常不会影响约束违背的发生。遵循 CREATE INDEX格式。

opclass

指定时，强制相应的index\_column\_name或 index\_expression 使用特定的操作符类以便在推断期间能被匹配上。通常会被省略， 因为相等语义在一种类型的操作符类 之间都是等价的，或者因为足以信任已定义的唯一索引具有适当的 相等定义。遵循CREATE INDEX格式。

index\_predicate

用于允许推断部分唯一索引。任何满足该谓词（不一定需要真的是 部分索引）的索引都能被推断。遵循CREATE INDEX格式。这要求任何出现在index\_predicate中的列上的SELECT特权。

constraint\_name

用名称显式地指定一个仲裁者约束， 而不是推断一个约束或者索引。

condition

一个能返回boolean值的表达式。只有让这个表达式返回 true的行才将被更新，不过在采用 ON CONFLICT DO UPDATE动作时所有的行都会被锁定。注意condition会被最后计算，即一个冲突 被标识为要更新的候选对象之后。

注意不支持把排除约束作为ON CONFLICT DO UPDATE的仲裁者。在所有的情况中，只支持NOT DEFERRABLE约束和 唯一索引作为仲裁者。

带有ON CONFLICT DO UPDATE子句的 INSERT是一种”确定性的” 语句。这表明不允许该命令影响任何单个现有行超过一次，如果发生则会 发生一个基数违背错误。要插入的行不应该在仲裁者索引或约束所限制的 属性上相重复。

> **注意：**
> 
> 当前不支持用分区表上的 `INSERT` 的 `ON CONFLICT DO UPDATE` 子句更新冲突行的分区键，因为那样会让行移动到新的分区中。

> **提示：**
> 
> 使用唯一索引推断通常比使用 `ON CONFLICT ON CONSTRAINT constraint_name` 直接提名一个约束更好。当底层索引被以重叠方式替换成另一个或多或少等效的索引时，推断将能继续正确地工作，例如在删除要被替换的索引之前使用 `CREATE UNIQUE INDEX ... CONCURRENTLY` 。

输出

成功完成时，INSERT命令会返回以下形式的命令标签：

INSERT oid count

count是被插入或更新的行数。 oid总是0（过去，如果count恰好为1， 并且目标表被声明为WITH OIDS，则它是分配给插入行的OID， 否则为0， 但现在已不再支持创建WITH OIDS表）。

如果INSERT命令包含RETURNING子句， 其结果会类似于包含RETURNING列表中定义的列和值的 SELECT语句，这些结果是由该命令在被插入或更新行上 计算得到。

注解

如果指定的表是一个分区表，每一行都会被路由到合适的分区并且插入其中。如果指定的表是一个分区，如果输入行之一违背该分区的约束则将发生错误。

示例

向films中插入一行：

```
INSERT INTO films VALUES

(\'UA502\', \'Bananas\', 105, \'1971-07-13\', \'Comedy\', \'82 minutes\');
```

在这个例子中，len列被省略并且因此会具有默认值：

```
INSERT INTO films (code, title, did, date_prod, kind)

VALUES (\'T_601\', \'Yojimbo\', 106, \'1961-06-16\', \'Drama\');
```

这个例子为日期列使用DEFAULT子句而不是指定一个值：

```
INSERT INTO films VALUES

(\'UA502\', \'Bananas\', 105, DEFAULT, \'Comedy\', \'82 minutes\');

INSERT INTO films (code, title, did, date_prod, kind)

VALUES (\'T_601\', \'Yojimbo\', 106, DEFAULT, \'Drama\');
```

插入一个完全由默认值构成的行：

```
INSERT INTO films DEFAULT VALUES;
```

用多行VALUES语法插入多个行：

```
INSERT INTO films (code, title, did, date_prod, kind) VALUES

(\'B6717\', \'Tampopo\', 110, \'1985-02-10\', \'Comedy\'),

(\'HG120\', \'The Dinner Game\', 140, DEFAULT, \'Comedy\');
```

这个例子从表tmp\_films中获得一些行插入到表 films中，两个表具有相同的列布局：

```
INSERT INTO films SELECT \* FROM tmp_films WHERE date_prod \< \'2004-05-07\';
```

这个例子插入数组列：

\-- 为 noughts-and-crosses 游戏创建一个空的 3x3 棋盘

```
INSERT INTO tictactoe (game, board\[1:3\]\[1:3\])

VALUES (1, \'{{\" \",\" \",\" \"},{\" \",\" \",\" \"},{\" \",\" \",\" \"}}\');
```

\-- 实际上可以不用上面例子中的下标

```
INSERT INTO tictactoe (game, board)

VALUES (2, \'{{X,\" \",\" \"},{\" \",O,\" \"},{\" \",X,\" \"}}\');
```

向表distributors中插入一行，返回由 DEFAULT子句生成的序号：

```
INSERT INTO distributors (did, dname) VALUES (DEFAULT, \'XYZ Widgets\')

RETURNING did;
```

增加为 Acme Corporation 管理账户的销售人员的销量，并且把整个被 更新的行以及当前时间记录到一个日志表中：

```
WITH upd AS (

UPDATE employees SET sales_count = sales_count + 1 WHERE id =

(SELECT sales_person FROM accounts WHERE name = \'Acme Corporation\')

RETURNING \*

)

INSERT INTO employees_log SELECT \*, current_timestamp FROM upd;
```

酌情插入或者更新新的 distributor。假设已经定义了一个唯一索引来约束 出现在did列中的值。注意，特殊的 excluded表被用来引用原来要插入的值：

```
INSERT INTO distributors (did, dname)

VALUES (5, \'Gizmo Transglobal\'), (6, \'Associated Computing, Inc\')

ON CONFLICT (did) DO UPDATE SET dname = EXCLUDED.dname;
```

插入一个 distributor，或者在一个被排除的行（具有一个匹配约束的列或者 会让行级前（或者后）插入触发器引发的列的行）存在时不处理要插入的行。 例子假设已经定义了一个唯一触发器来约束出现在did列 中的值：

```
INSERT INTO distributors (did, dname) VALUES (7, \'Redline GmbH\')

ON CONFLICT (did) DO NOTHING;
```

酌情插入或者更新新的 distributor。例子假设已经定义了一个唯一触发器来 约束出现在did列中的值。WHERE子句被用 来限制实际被更新的行（不过，任何没有被更新的已有行仍将被锁定）：

```
\-- 根据一个特定的 ZIP 编码更新 distributors

INSERT INTO distributors AS d (did, dname) VALUES (8, \'Anvil Distribution\')

ON CONFLICT (did) DO UPDATE

SET dname = EXCLUDED.dname \|\| \' (formerly \' \|\| d.dname \|\| \')\'

WHERE d.zipcode \<\> \'21201\';

\-- 直接在语句中命名一个约束（使用相关的索引来判断是否做

\-- DO NOTHING 动作）

INSERT INTO distributors (did, dname) VALUES (9, \'Antwerp Design\')

ON CONFLICT ON CONSTRAINT distributors_pkey DO NOTHING;
```

如果可能就插入新的 distributor，否则DO NOTHING。 例子假设已经定义了一个唯一索引，它约束让is\_active 布尔列为true的行子集上did列中的值：

```
\-- 这个语句可能推断出一个在 \"did\" 上带有谓词 \"WHERE is_active\"

\-- 的部分唯一索引，但是它可能也只是使用了 \"did\" 上的一个常规唯一约束

INSERT INTO distributors (did, dname) VALUES (10, \'Conrad International\')

ON CONFLICT (did) WHERE is_active DO NOTHING;
```

兼容性

INSERT符合SQL标准，不过 RETURNING子句是一种瀚高数据库扩展，在 INSERT中使用WITH也是， 用ON CONFLICT指定一个替代动作也是扩展。还有，标准不允许省略列名列表但不通过 VALUES子句或者query填充所有列的情况。

SQL标准指定只有存在一个总是会生成值的标识列时才能指定OVERRIDING SYSTEM VALUE。而瀚高数据库在任何情况下都允许这个子句，并且在不适用时会忽略它。

query子句可能的限制在 SELECT有介绍。

## LISTEN

— 监听一个通知

大纲

```
LISTEN channel
```

描述

LISTEN在名为channel的通知频道上将当前会话注册为一个监听者。如果当前会话已经被注册为这个通知频道的一个监听者，则什么也不会发生。

只要命令NOTIFY channel被调用（不管是在这个会话还是在另一个连接到同一数据库的会话中），所有当前正在该通知频道上监听的会话都会被通知，并且每一个会话将会接着通知连接到它的客户端应用。

可以使用UNLISTEN命令在一个给定通知频道上反注册一个会话。当会话结束时，它的监听注册会被自动清除。

一个客户端应用检测通知事件的必用方法取决于它使用的瀚高数据库应用编程接口。如果使用libpq库，应用会将LISTEN作为一个普通 SQL 命令发出，并且接着必须周期性地调用函数PQnotifies来查看是否接收到通知事件。其他诸如libpgtcl的接口提供了更高层次上的处理通知事件的方法。事实上，通过使用libpgtcl应用程序员甚至不必直接发出LISTEN或UNLISTEN。更多细节可参阅所使用的接口的文档。

NOTIFY包含了使用LISTEN和NOTIFY的更广泛的讨论。

参数

channel

一个通知频道的名称（任意标识符）。

注解

LISTEN在事务提交时生效。如果在一个后来被回滚的事务中执行了LISTEN或UNLISTEN，被监听的通知频道集合不会变化。

一个已经执行了LISTEN的事务不能为两阶段提交做准备。

示例

从psql中配置并执行一个监听/通知序列

```
LISTEN virtual;

NOTIFY virtual;

Asynchronous notification \"virtual\" received from server process with PID 8448.
```

兼容性

在 SQL 标准中没有LISTEN语句。

参见

NOTIFY, UNLISTEN

## LOAD

LOAD — 载入一个共享库文件

大纲

```
LOAD \'filename\'
```

描述

这个命令把一个共享库文件载入到瀚高数据库服务器 的地址空间中。如果该文件已经被载入，这个命令什么也不会做。只要调用 包含 C 函数的共享库文件中的一个函数，这些共享库文件就会被自动载入。 因此，一次显式的LOAD通常只在载入一个通过 “钩子”修改服务器行为而不是提供一组函数的库时需要。

库文件名通常只是一个裸文件名，在服务器的库搜索路径（由

dynamic\_library\_path设置）中寻找。或者， 它可以作为完整的路径名称给出。无论哪种情况，平台的标准共享库文件扩展名都可以省略。

非超级用户只能把LOAD应用在位于 $libdir/plugins/中的库文件 — 指定的 filename 必须正好以该字符串开始（确保在那里只安装了 “安全的”库是数据库管理员的责任）。

兼容性

LOAD是一种瀚高数据库扩展。

另见

CREATE FUNCTION

## LOCK

— 锁定一个表

大纲

```
LOCK \[ TABLE \] \[ ONLY \] name \[ \* \] \[, \...\] \[ IN lockmode MODE \] \[ NOWAIT \]
```

其中 lockmode 可以是以下之一：

```
ACCESS SHARE \| ROW SHARE \| ROW EXCLUSIVE \| SHARE UPDATE EXCLUSIVE

\| SHARE \| SHARE ROW EXCLUSIVE \| EXCLUSIVE \| ACCESS EXCLUSIVE
```

描述

LOCK TABLE获得一个表级锁，必要时会 等待任何冲突锁被释放。如果指定了NOWAIT， LOCK TABLE不会等待以获得想要的锁： 如果它不能立刻得到，该命令会被中止并且发出一个错误。一旦获取到， 该锁会被在当前事务中一直持有（没有UNLOCK TABLE命令，锁总是在事务结束时被释放）。

当一个视图被锁定时，出现在该视图定义查询中的所有关系也将被使用同样的锁模式递归地锁住。

在为引用表的命令自动获取锁时， 瀚高数据库总是尽可能使用最不严格的 锁模式。

提供LOCK TABLE是用于想要更严格 的锁定的情况。例如，假设一个应用运行一个READ COMMITTED 隔离级别的事务， 并且需要确保一个表中的数据在该事务的期间保持稳定。要实现这个目的， 必须在查询之前在表上获得SHARE锁模式。这将阻止并发的 数据更改并且确保该表的后续读操作会看到已提交数据的一个稳定视图， 因为SHARE锁模式与写入者所要求的 ROW EXCLUSIVE锁有冲突，并且你的 LOCK TABLE name IN SHARE MODE 语句将等待，直到任何并发持有ROW EXCLUSIVE模式锁的持有者提交或者回滚。因此，一旦得到锁，就不会有未提交的写入还没有解决。更进一步，在释放该锁之前，任何人都不能开始。

要在运行在REPEATABLE READ或SERIALIZABLE 隔离级别的事务中得到类似的效果，你必须在执行任何SELECT或者数据修改语句之前执行 LOCK TABLE语句。一个 REPEATABLE READ或者SERIALIZABLE事务的数据视图将在它的第一个SELECT或者数据修改语句开始时被冻结。

在该事务中稍后的一个LOCK TABLE仍将阻止并发写— 但它不会确保该事务读到的东西对应于最新的已提交值。

如果一个此类事务正要修改表中的数据，那么它应该使用 SHARE ROW EXCLUSIVE锁模式来取代 SHARE模式。这会保证一次只有一个此类事务运行。如果 不用这种模式，死锁就可能出现：两个事务可能都要求 SHARE模式，并且都不能获得 ROW EXCLUSIVE模式来真正地执行它们的更新（注意一个 事务所拥有的锁不会冲突，因此一个事务可以在它持有SHARE 模式时获得ROW EXCLUSIVE模式 — 但是如果有其他 人持有SHARE模式时则不能）。为了避免死锁，确保所有的 事务在同样的对象上以相同的顺序获得锁，并且如果在一个对象上涉及多 种锁模式，事务应该总是首先获得最严格的那种模式。

参数

name

要锁定的一个现有表的名称（可以是模式限定的）。如果在表名前指定了 ONLY，只有该表会被锁定。如果没有指定了 ONLY，该表和它所有的后代表（如果有）都会被锁定。可选地，在表名后指定\*来显式地表示把后代表包括在内。

命令LOCK TABLE a, b;等效于 LOCK TABLE a; LOCK TABLE b;。这些表会被按照在 LOCK TABLE中指定的顺序一个一个被锁定。

lockmode

锁模式指定这个锁和哪些锁冲突。

如果没有指定锁模式，那儿将使用最严格的模式ACCESS EXCLUSIVE。

NOWAIT

指定LOCK TABLE不等待任何冲突锁被释放： 如果所指定的锁不能立即获得，那么事务就会中止。

注解

LOCK TABLE... IN ACCESS SHARE MODE要求目标表上的SELECT特权。LOCK TABLE... IN ROW EXCLUSIVE MODE要求目标表上的INSERT、UPDATE、DELETE或TRUNCATE特权。所有其他形式的LOCK要求表级UPDATE、DELETE或TRUNCATE特权。

在该视图上执行锁定的用户必须具有该视图上相应的特权。此外视图的拥有者必须拥有底层基关系上的相关特权，但是执行锁定的用户不需要底层基关系上的任何权限。

LOCK TABLE在一个事务块外部没有用处：锁将只保持到语句完成。因此如果在一个事务块外部使用了LOCK，瀚高数据库会报告一个错误。使用BEGIN和COMMIT（或者ROLLBACK）定义一个事务块。

LOCK TABLE只处理表级锁，因此涉及到 ROW的模式名称在这里都是不当的。这些模式名称应该通常 被解读为用户在被锁定表中获取行级锁的意向。还有， ROW EXCLUSIVE模式是一个可共享的表锁。记住就 LOCK TABLE而言，所有的锁模式都具有相同的语义， 只有模式的冲突规则有所不同。

示例

在将要向一个外键表中执行插入时在主键表上获得一个 SHARE锁：

```
BEGIN WORK;

LOCK TABLE films IN SHARE MODE;

SELECT id FROM films

WHERE name = \'Star Wars: Episode I - The Phantom Menace\';

\-- 如果记录没有被返回就做 ROLLBACK

INSERT INTO films_user_comments VALUES

(\_id\_, \'GREAT! I was waiting for it for so long!\');

COMMIT WORK;
```

在将要执行一次删除操作前在主键表上取一个 SHARE ROW EXCLUSIVE锁：

```
BEGIN WORK;

LOCK TABLE films IN SHARE ROW EXCLUSIVE MODE;

DELETE FROM films_user_comments WHERE id IN

(SELECT id FROM films WHERE rating \< 5);

DELETE FROM films WHERE rating \< 5;

COMMIT WORK;
```

兼容性

在 SQL 标准中没有LOCK TABLE，SQL 标准中使用 SET TRANSACTION指定事务上的并发层次。

瀚高数据库也支持这样做，详见 SET TRANSACTION。

除ACCESS SHARE、ACCESS EXCLUSIVE和 SHARE UPDATE EXCLUSIVE锁模式之外， 瀚高数据库锁模式和 LOCK TABLE语法与 Oracle中的兼容。

## MOVE

— 定位一个游标

大纲

```
MOVE \[ direction \[ FROM \| IN \] \] cursor_name
```

其中direction可以为空或者以下之一：

```
NEXT

PRIOR

FIRST

LAST

ABSOLUTE count

RELATIVE count

count

ALL

FORWARD

FORWARD count

FORWARD ALL

BACKWARD

BACKWARD count

BACKWARD ALL
```

描述

MOVE重新定位一个游标而不检索任何数据。 MOVE的工作完全像 FETCH命令，但是它只定位游标并且不返回行。

用于MOVE命令的参数和 FETCH命令的一样，可参考 FETCH。

输出

成功完成时，MOVE命令返回的命令标签形式是

MOVE count

count是一个 具有同样参数的FETCH命令会返回的 行数（可能为零）。

示例

```
BEGIN WORK;

DECLARE liahona CURSOR FOR SELECT \* FROM films;

\-- 跳过前 5 行：

MOVE FORWARD 5 IN liahona;

MOVE 5

\-- 从游标 liahona 中取第 6 行：

FETCH 1 FROM liahona;

code \| title \| did \| date_prod \| kind \| len

\-\-\-\-\-\--+\-\-\-\-\-\-\--+\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\--+\-\-\-\-\-\--

P_303 \| 48 Hrs \| 103 \| 1982-10-22 \| Action \| 01:37

(1 row)

\-- 关闭游标 liahona 并且结束事务：

CLOSE liahona;

COMMIT WORK;
```

兼容性

在 SQL 标准中没有MOVE语句。

另见

CLOSE, DECLARE, FETCH

## NOTIFY

— 生成一个通知

大纲

```
NOTIFY channel \[ , payload \]
```

描述

NOTIFY命令发送一个通知事件以及一个可选的”载荷”字符串给每个正在监听的客户端应用，这些应用之前都在当前数据库中为指定的频道名执行过LISTEN channel。通知对所有用户都可见。

NOTIFY为访问同一个瀚高数据库数据库的进程集合提供了一种简单的进程间通讯机制。伴随着通知可以发送一个载荷字符串，通过使用数据库中的表从通知者向监听者传递额外的数据，也可以构建用于传输结构化数据的高层机制。

由一个通知事件传递给客户端的信息包括通知频道名称、发出通知的会话的服务器进程PID以及载荷字符串，如果载荷字符串没有被指定则它为空字符串。

将在一个给定数据库以及其他数据库中使用的频道名称由数据库设计者定义。通常，频道名称与数据库中某个表的名称相同，并且通知事件其实就意味着：”我改变了这个表，来看看改了什么吧”。但是NOTIFY和LISTEN命令并未强制这样的关联。例如，一个数据库设计者可以使用几个不同的频道名称来标志一个表上的不同种类的改变。另外，载荷字符串可以被用于多种不同的情况。

当NOTIFY被用来标志对一个特定表的改变时， 一种有用的编程技巧是把NOTIFY 放在一个由表更新触发的语句触发器中。在这种方式中，每当表被改变时 都将自动发生通知，并且应用程序员不可能会忘记发出通知。

NOTIFY以一些重要的方式与 SQL 事务互动。首先，如果一个NOTIFY在一个事务内执行，在事务被提交之前，该通知事件都不会被递送。这是合适的，因为如果该事务被中止，所有其中的命令都将不会产生效果，包括NOTIFY在内。但如果期望通知事件被立即递送，那这种行为就会令人不安。其次，如果一个监听会话收到了一个通知信号而它正在一个事务中，在该事务完成（提交或者中止）之前，该通知事件将不会被递送给它连接的客户端。同样，原因在于如果一个通知在一个事务内被递送且该事务后来被中止，我们会希望该通知能以某种方式被撤销 — 但是服务器一旦把通知发送给客户端就无法”收回它”。因此通知事件只能在事务之间递送。其中的要点是把NOTIFY用作实时信号的应用应该让它们事务尽可能短小。

如果从同一个事务多次用相同的载荷字符串对同一个频道名称发送通知，数据库服务器能决定只递送一个单一的通知。另一方面，带有不同载荷字符串的通知将总是作为不同的通知被递送。类似地，来自不同事务的通知将不会被折叠成一个通知。除了丢弃后来生成的重复通知实例之外，NOTIFY保证来自同一个事务的通知按照它们被发送的顺序被递送。还可以保证的是，来自不同事务的消息会按照其事务被提交的顺序递送。

一个执行NOTIFY的客户端自己也同时在监听同一个通知频道是很常见的事。在这种情况下，和所有其他监听会话一样，它会取回一个通知事件。根据应用的逻辑，这可能导致无用的工作，例如从自己刚刚写入的一个表中读出相同的更新。可以通过关注发出通知的服务器进程PID（在通知事件消息中提供）与自己的会话PID（可以从libpq得到）是否相同来避免这种额外的工作。当两者相同时，该通知事件就是当前会话自己发出的，所以可以忽略。

参数

channel

要对其发信号的通知频道的名称（任意标识符）。

payload

要通过通知进行沟通的”载荷”字符串。这必须是一个简单的字符串。在默认配置下，该字符串不能超过 8000 字节（如果需要发送二进制数据或者更多信息，最好是把它放在一个数据库表中并且发送该记录的键）。

注解

有一个队列保持着已经发送但是还没有被所有监听会话处理的通知。如果该队列被占满，调用NOTIFY的事务将在提交时失败。该队列非常大（标准安装中是 8GB）并且应该足以应付几乎每一种用例。不过，如果一个会话执行了NOTIFY并且接着长时间进入一个事务，不会发生清理操作。一旦该队列使用过半，你将在日志文件中看到警告，它指出哪个会话阻止了清理。在这种情况中，应该确保这个会话结束它的当前事务，这样清理才能够进行下去。

函数pg\_notification\_queue\_usage返回队列中当前被 待处理通知所占据的比例。

一个已经执行了NOTIFY的事务不能为两阶段提交做准备。

pg\_notify

要发送一个通知，你也能使用函数pg\_notify(text, text)。该函数采用频道名称作为第一个参数，而载荷则作为第二个参数。如果你需要使用非常量的频道名称和载荷，这个函数比NOTIFY命令更容易使用。

示例

从psql配置和执行一个监听/通知序列：

```
LISTEN virtual;

NOTIFY virtual;

Asynchronous notification \"virtual\" received from server process with PID 8448.

NOTIFY virtual, \'This is the payload\';

Asynchronous notification \"virtual\" with payload \"This is the payload\" received

from server process with PID 8448.

LISTEN foo;

SELECT pg_notify(\'fo\' \|\| \'o\', \'pay\' \|\| \'load\');

Asynchronous notification \"foo\" with payload \"payload\" received from server

process with PID 14728.
```

兼容性

在 SQL 标准中没有NOTIFY语句。

参见

LISTEN, UNLISTEN

## PREPARE

— 为执行准备一个语句

大纲

```
PREPARE name \[ ( data_type \[, \...\] ) \] AS statement
```

描述

PREPARE创建一个预备语句。预备语句是一种服务器端对象，它可以被用来优化性能。

当PREPARE语句被执行时，指定的语句会被解析、分析并且重写。当后续发出一个EXECUTE命令时，该预备语句会被规划并且执行。这种工作的划分避免了重复性的解析分析工作，不过允许执行计划依赖所提供的特定参数值。

预备语句可以接受参数：在执行时会被替换到语句中的值。在创建预备语句时，可以用位置引用参数，如$1、$2等。也可以选择性地指定参数数据类型的一个列表。当一个参数的数据类型没有被指定或者被声明为unknown时，其类型会从该参数第一次被引用的环境中推知（如果可能）。在执行该语句时，在EXECUTE语句中为这些参数指定实际值。更多有关于此的信息可参考EXECUTE。

预备语句只在当前数据库会话期间存在。当会话结束时，预备语句会消失，因此在重新使用之前必须重新建立它。这也意味着一个预备语句不能被多个数据库客户端同时使用。不过，每一个客户端可以创建它们自己的预备语句来使用。预备语句可以用DEALLOCATE命令手工清除。

当一个会话要执行大量类似语句时，预备语句可能会有最大性能优势。如果该语句很复杂（难于规划或重写），例如，如果查询涉及很多表的连接或者要求应用多个规则，性能差异将会特别明显。如果语句相对比较容易规划和重写，但是执行起来开销相对较大，那么预备语句的性能优势就不那么显著了。

参数

name

给这个特定预备语句的任意名称。它在一个会话中必须唯一并且后续将被用来执行或者清除一个之前准备好的语句。

data\_type

预备语句一个参数的数据类型。如果一个特定参数的数据类型没有被指定或者被指定为unknown，将从该参数第一次被引用的环境中推得。要在预备语句本身中引用参数，可以使用 $1、$2等。

statement

任何SELECT、INSERT、UPDATE、DELETE或者VALUES语句。

注解

可以使用generic plan或custom plan执行已准备好的语句。 通用计划在所有执行中都是相同的，而自定义计划是为特定执行所生成的，使用调用中给出的参数值。 使用通用计划可以避免计划开销，但在某些情况下，自定义计划的执行效率要高得多，因为规划器可以利用参数值的知识。 （当然，如果准备好的语句没有参数，则这是没有意义的，并且始终应使用通用计划。）

默认情况下（也就是当 plan\_cache\_mode 设定为 auto时），对已经准备好的具有参数的语句，服务器将自动选择使用通用或自定义计划。 当前的规则是，前五次执行都是使用自定义计划完成的，并且计算这些计划的平均估计成本。然后创建通用计划，并将其估计成本与自定义计划的平均成本相比较。 如果通用计划的成本没有比平均自定义计划成本高太多，那么后续执行将使用通用计划，以使重复的再看起来更可取。

这种探索式方法可以重写，强迫服务器使用通用或自定义计划，通过将plan\_cache\_mode分别设置为force\_generic\_plan或 force\_custom\_plan 。 如果通用计划的成本估计由于某种原因很不理想，则此设置主要很有用，尽管其实际成本远高于自定义计划的实际成本，可以选择此设置。

要检查瀚高数据库为一个预备语句使用的查询计划，可以使用EXPLAIN，例如：

EXPLAIN EXECUTE name(parameter\_values);

如果使用的是一个通用计划，它将包含参数符号$n，而一个定制计划则会把提供的参数值替换进去。

尽管预备语句主要是为了避免重复对语句进行解析分析以及规划，但是只要上一次使用该预备语句后该语句中用到的数据库对象发生了定义性（DDL）改变，瀚高数据库将会对该语句强制进行重新分析和重新规划。还有，如果search\_path的值发生变化，也将使用新的search\_path重新解析该语句。这些规则让预备语句的使用在语义上几乎等效于反复提交相同的查询文本，但是能在性能上获利（如果没有对象定义被改变，特别是如果最优计划保持不变时）。该语义等价性不完美的一个例子是：如果语句用一个未限定的名称引用表，并且之后在search\_path中更靠前的模式中创建了一个新的同名表，则不会发生自动的重解析，因为该语句使用的对象没有被改变。

不过，如果某些其他更改造成了重解析，后续使用中都会引用新表。

可以通过查询pg\_prepared\_statements系统视图来看到会话中所有可用的预备语句。

示例

为一个INSERT语句创建一个预备语句，然后执行它：

```
PREPARE fooplan (int, text, bool, numeric) AS

INSERT INTO foo VALUES(\$1, \$2, \$3, \$4);

EXECUTE fooplan(1, \'Hunter Valley\', \'t\', 200.00);
```

为一个SELECT语句创建一个预备语句，然后执行它：

```
PREPARE usrrptplan (int) AS

SELECT \* FROM users u, logs l WHERE u.usrid=\$1 AND u.usrid=l.usrid

AND l.date = \$2;

EXECUTE usrrptplan(1, current_date);
```

在这个示例中，第二个参数的数据类型没有被指定，因此会从使用$2的环境中推知。

兼容性

SQL 标准包括一个PREPARE语句，但是它只用于嵌入式 SQL。这个版本的PREPARE语句也使用了一种有些不同的语法。

另见

DEALLOCATE, EXECUTE

## PREPARE TRANSACTION

— 为两阶段提交准备当前事务

大纲

```
PREPARE TRANSACTION transaction_id
```

描述

PREPARE TRANSACTION为两阶段提交准备 当前事务。在这个命令之后，该事务不再与当前会话关联。相反，它的状态 被完全存储在磁盘上，并且有很高的可能性它会被提交成功（即便在请求提 交前发生数据库崩溃）。

一旦被准备好，事务稍后就可以分别用 COMMIT PREPARED 或者ROLLBACK PREPARED提交或者回滚。可以从任何 会话而不仅仅是执行原始事务的会话中发出这些命令。

从发出命令的会话的角度来看，PREPARE TRANSACTION不像ROLLBACK命令： 在执行它之后，就没有活跃的当前事务，并且该预备事务的效果也不再可见（ 如果该事务被提交，效果将重新变得可见）。

如果由于任何原因PREPARE TRANSACTION 命令失败，它会变成一个ROLLBACK：当前事务会被取消。

参数

transaction\_id

一个任意的事务标识符， COMMIT PREPARED或者ROLLBACK PREPARED 以后将用这个标识符来标识这个事务。该标识符必须写成一个字符串， 并且长度必须小于 200 字节。它也不能与任何当前已经准备好的事务的标识符相同。

注解

PREPARE TRANSACTION并不是设计为在应用或者交互式 会话中使用。它的目的是允许一个外部事务管理器在多个数据库或者其他事务性 来源之间执行原子的全局事务。除非你在编写一个事务管理器，否则你可能不会 用到PREPARE TRANSACTION。

这个命令必须在一个事务块中使用。事务块用BEGIN开始。

当前在已经执行过任何涉及到临时表或者会话的临时命名空间、创建带 WITH HOLD的游标或者执行 LISTEN、UNLISTEN或NOTIFY的 事务中，不允许PREPARE该事务。这些特性与当前会话绑定得太过紧密，所以对一个要被准备的事务来说没有什么用处。

如果用SET（不带LOCAL选项）修改过事务的 任何运行时参数，这些效果会持续到 PREPARE TRANSACTION之后，并且将不会被后续的任何 COMMIT PREPARED或 ROLLBACK PREPARED所影响。因此，在这一 方面PREPARE TRANSACTION的行为更像 COMMIT而不是ROLLBACK。

所有当前可用的准备好事务被列在 `pg_prepared_xacts` 系统视图中。

> **小心：**
> 
> 让一个事务处于准备好状态太久是不明智的。这将会干扰 `VACUUM` 回收存储的能力，并且在极限情况下可能导致数据库关闭以阻止事务 ID 回卷。还要记住，该事务会继续持有它已经持有的锁。该特性的设计用法是，只要一个外部事务管理器已经验证其他数据库也准备好了要提交，一个准备好的事务将被正常地提交或者回滚。
> 
> 如果没有建立一个外部事务管理器来跟踪准备好的事务并且确保它们被迅速地结束，最好禁用准备好事务特性（设置 `max_prepared_transactions` 为零）。
> 
> 这将防止意外地创建准备好事务，不然该事务有可能被忘记并且最终导致问题。

示例

为两阶段提交准备当前事务，使用foobar作为事务标识符：

```
PREPARE TRANSACTION \'foobar\';
```

兼容性

PREPARE TRANSACTION是一种瀚高数据库扩展。其意图是用于 外部事务管理系统，其中有些已经被标准涵盖（例如 X/Open XA）， 但是那些系统的 SQL 方面未被标准化。

另见

COMMIT PREPARED, ROLLBACK PREPARED

## REASSIGN OWNED

— 更改一个数据库角色拥有的数据库对象的拥有关系

大纲

```
REASSIGN OWNED BY { old_role \| CURRENT_USER \| SESSION_USER } \[, \...\]

TO { new_role \| CURRENT_USER \| SESSION_USER }
```

描述

REASSIGN OWNED指示系统把

old\_role们拥有 的任何数据库对象的拥有关系更改为new\_role。

参数

old\_role

一个角色的名称。这个角色在当前数据库中所拥有的 所有对象以及所有共享对象（数据库、表空间）的 所有权都将被重新赋予给 new\_role。

new\_role

将作为受影响对象的新拥有者的角色名称。

注解

REASSIGN OWNED经常被用来为移除一个 或者多个角色做准备。因为REASSIGN OWNED不影响其他数据库中的对象，通常需要在包含有 被删除的角色所拥有的对象的每一个数据库中都执行这个命令。

REASSIGN OWNED同时要求源角色和目标 角色上的成员资格。

DROP OWNED命令可以简单地删掉一个或者多个角色所拥有 的所有数据库对象。

REASSIGN OWNED命令不会影响授予给old\_roles的在它们不拥有的对象上的任何特权。 同样，它不会影响ALTER DEFAULT PRIVILEGES创建的默认特权。DROP OWNED可以回收那些特权。

兼容性

REASSIGN OWNED命令是一种瀚高数据库扩展。

另见

DROP OWNED, DROP ROLE, ALTER DATABASE

## REFRESH MATERIALIZED VIEW

— 替换一个物化视图的内容

大纲

```
REFRESH MATERIALIZED VIEW \[ CONCURRENTLY \] name

\[ WITH \[ NO \] DATA \]
```

描述

REFRESH MATERIALIZED VIEW完全替换一个 物化视图的内容。你必须是该物化视图的属主才能执行这个命令.旧的内容会被抛弃。如果指定了 WITH DATA（或者作为默认值），支持查询将被执行以 提供新的数据，并且会让物化视图将处于可扫描的状态。如果指定了 WITH NO DATA，则不会生成新数据并且会让物化视图 处于一种不可扫描的状态。

CONCURRENTLY和WITH NO DATA 不能被一起指定。

参数

CONCURRENTLY

对物化视图的刷新不阻塞在该物化视图上的并发选择。如果没有这个选项， 一次影响很多行的刷新将使用更少的资源并且更快结束，但是可能会阻塞 其他尝试从物化视图中读取的连接。这个选项在只有少量行被影响的情况 下可能会更快。

只有当物化视图上有至少一个UNIQUE索引（只用列名 并且包括所有行）时，才允许这个选项。也就是说，它不能是表达式索引或者包括WHERE子句。

当物化视图还未被填充时，这个选项不能被使用。

即使带有这个选项，对于任意一个物化视图一次也只能运行一个 REFRESH。

name

要刷新的物化视图的名称（可以被模式限定）。

注解

虽然用于未来的CLUSTER操作的默认索引会被保持， REFRESH MATERIALIZED VIEW不会基于这个属性排序产生 的行。如果希望数据在产生时排序，必须在支持查询中使用 ORDER BY子句。

示例

这个命令将使用物化视图order\_summary定义中的查询 来替换该物化视图的内容，并且让它处于一种可扫描的状态：

```
REFRESH MATERIALIZED VIEW order_summary;
```

这个命令将释放与物化视图annual\_statistics\_basis相关 的存储并且让它变成一种不可扫描的状态：

```
REFRESH MATERIALIZED VIEW annual_statistics_basis WITH NO DATA;
```

兼容性

REFRESH MATERIALIZED VIEW是一种瀚高数据库扩展。

另见

CREATE MATERIALIZED VIEW, ALTER MATERIALIZED VIEW, DROP MATERIALIZED VIEW

## REINDEX

— 重建索引

大纲

```
REINDEX \[ ( VERBOSE ) \] { INDEX \| TABLE \| SCHEMA \| DATABASE \| SYSTEM }

\[ CONCURRENTLY \] name
```

描述

REINDEX使用索引的表里存储的数据重建一个索引， 并且替换该索引的旧拷贝。有一些场景需要使用REINDEX：

• 一个索引已经损坏，并且不再包含合法数据。尽管理论上这不会发生， 实际上索引会因为软件缺陷或硬件失效损坏。 REINDEX提供了一种恢复方法。

• 一个索引变得”臃肿”，其中包含很多空的或者近乎为空的页面。瀚高数据库中的 B-树索引在特定的非 常规访问模式下可能会发生这种情况。REINDEX 提供了一种方法来减少索引的空间消耗，即制造一个新版本的索引，其中没有死亡页面。

• 修改了一个索引的存储参数（例如填充因子），并且希望确保这种修改完全 生效。

• 如果索引在用CONCURRENTLY选项创建失败，该索引保留为一个”invalid”。 这类索引是无用的，但是可以方便的用REINDEX来重建它们。注意，只有REINDEX INDEX可以在无效的索引上执行并发创建。

参数

INDEX

重新创建指定的索引。

TABLE

重新创建指定表的所有索引。如果该表有一个二级 “TOAST”表，它也会被重索引。

SCHEMA

重建指定方案的所有索引。如果这个方案中的一个表有次级的”TOAST”表，它也会被重建索引。共享系统目录上的索引也会被处理。这种形式的REINDEX不能在事务块内执行。

DATABASE

重新创建当前数据库内的所有索引。共享的系统目录上的索引也会被 处理。这种形式的REINDEX不能在一个事务块内执行。

SYSTEM

重新创建当前数据库中在系统目录上的所有索引。共享系统目录上的 索引也被包括在内。用户表上的索引则不会被处理。这种形式的 REINDEX不能在一个事务块内执行。

name

要被重索引的特定索引、表或者数据库的名字。索引和表名可以被 模式限定。当前，REINDEX DATABASE和 REINDEX SYSTEM只能重索引当前数据库，因此 它们的参数必须匹配当前数据库的名称。

CONCURRENTLY

使用此选项时，瀚高数据库将重建索引，而不在表上采取任何阻止并发插入、更新或删除的锁; 标准的索引重建将会锁定表上的写操作(而不是读操作)，直到它完成。 使用此选项—时，有几个事项需要注意；请参阅Rebuilding Indexes Concurrently。

对于临时表，REINDEX始终是非并发的，因为没有其他会话可以访问它们，并且非并发重新索引更便宜。

VERBOSE

在每个索引被重建时打印进度报告。

注解

如果怀疑一个用户表上的索引损坏，可以使用 REINDEX INDEX或者 REINDEX TABLE简单地重建该索引 或者表上的所有索引。

如果你需要从一个系统表上的索引损坏中恢复，就更困难一些。在 这种情况下，对系统来说重要的是没有使用过任何可疑的索引本身（ 实际上，这种场景中，你可能会发现服务器进程会在启动时立刻崩溃， 这是因为对于损坏的索引的依赖）。要安全地恢复，服务器必须用 -P选项启动，这将阻止它使用索引来进行系统 目录查找。

这样做的一种方法是关闭服务器，并且启动一个单用户的瀚高数据库服务器，在其命令行中包括-P选项。然后，可以发出 REINDEX DATABASE、REINDEX SYSTEM、 REINDEX TABLE或者REINDEX INDEX， 具体使用哪个命令取决于你想要重构多少东西。如果有疑问，可以使用REINDEX SYSTEM来选择重建数据库中的所有系统索引。 然后退出单用户服务器会话并且重启常规的服务器。更多关于如何与 单用户服务器接口交互的内容请见postgres参考页。

在另一种方法中，可以开始一个常规的服务器会话，在其命令行选项 中包括-P。这样做的方法与客户端有关，但是在 所有基于libpq的客户端中都可以在开始客户端 之前设置PGOPTIONS环境变量为-P。 注意虽然这种方法不要求用锁排斥其他客户端，在修复完成之前避免 其他用户连接到受损的数据库才是更加明智的。

REINDEX类似于删除索引并且重建索引，在其中索引内容会被从头开始建立。不过，锁定方面的考虑却相当不同。REINDEX会用锁排斥写，但不会排斥在索引的父表上的读。 它也会在被处理的索引上取得一个排他锁，该锁将会阻塞对该索引的使用尝试。 相反，DROP INDEX会暂时在附表上取得一个排他锁，阻塞 写和读。后续的CREATE INDEX会排斥写但不排斥读，由于该索引不存在，所以不会有读取它的尝试，这意味着不会有阻塞但是读操作可能被强制成昂贵的顺序扫描。

重索引单独一个索引或者表要求用户是该索引或表的拥有者。对方案或数据库重建索引要求是该方案或者数据库的拥有者。注意因此非超级用户有时无法重建其他用户拥有的表上的索引。不过，作为一种特例，当一个非超级用户发出REINDEX DATABASE、REINDEX SCHEMA或者REINDEX SYSTEM时，共享目录上的索引将被跳过，除非该用户拥有该目录（通常不会是这样）。当然，超级用户总是可以重建所有的索引。

不支持重建分区表的索引或者分区索引。不过可以单独为每个分区重建索引。

并行重建索引

重建索引可能会影响数据库的常规操作。通常瀚高数据库会锁定重建的表以防止写操作，并通过单次扫描表来执行整个索引构建。 其他事务仍可以读取表，但如果它们尝试在表中插入、更新或删除行，它们将被阻止，直到索引重建完成。 如果系统是实时生产数据库，这可能会产生严重影响。非常大的表可能需要几个小时才能编制索引，即使对于较小的表，索引重建也会锁定编写器，这些时间段对于生产系统来说是不可接受的。

瀚高数据库支持以最少的写入锁定来重建索引。此方法通过指定REINDEX的CONCURRENTLY选项来调用。 使用此选项时，瀚高数据库必须对需要重新生成的每个索引执行两次表扫描，并等待可能使用索引的所有现有事务的终止。 此方法需要比标准索引重建更大的工作量，并且需要相当长的时间才能完成，因为它需要等待可能修改索引的未完成的事务。 但是，由于它允许在重建索引时继续正常操作，此方法可用于在生产环境中重建索引。当然，重建索引所需的额外 CPU、内存和 I/O 负载可能会减慢其他操作的速度。

以下步骤发生在并发重建索引中。 每个步骤在单独的事务中运行。 如果要重建多个索引，则每个步骤在进入到下一步之前都要循环遍历所有索引。

1\. 新的临时索引定义将添加到目录pg\_index中。 此定义将用于替换旧索引。 一个SHARE UPDATE EXCLUSIVE会话级别的锁将放在要重建的索引以及其关联的表上，以防止处理时的任何模式修改。

2\. 为每个新索引完成生成索引的首个操作。 生成索引后，其标志pg\_index.indisready切换到”true”使其准备好插入，使其在执行生成的事务完成后对其他会话可见。 此步骤在每个索引的单独事务中完成。

3\. 然后执行第二个操作以添加在第一个操作运行时添加的元组。此步骤也在每个索引的单独事务中完成。

4\. 引用索引的所有约束都已更改以引用新的索引定义，并且索引名称也已经更改。 此时，pg\_index.indisvalid会为新索引切换到”true”，以及为旧索引切换到”false”，并且缓存无效会导致引用旧索引的所有会话失效。

5\. 旧索引有pg\_index.indisready切换到”false”以防止任何新的元组插入，在等待可能引用旧索引的查询之后完成。

6\. 旧索引被丢弃。索引和表的SHARE UPDATE EXCLUSIVE会话锁被释放。

如果在重建索引时出现问题，例如唯一索引中的唯一性冲突， REINDEX命令将失败，但会留下一个 “invalid”新索引，在已经存在的索引之外。 出于查询目的此索引将被忽略，因为它可能不完整;但是它仍将消耗更新开销。psql \\d命令将此类索引报告为 INVALID:

```
highgo=# \\d tab

Table \"public.tab\"

Column \| Type \| Modifiers

\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\--

col \| integer \|

Indexes:

\"idx\" btree (col)

\"idx_ccnew\" btree (col) INVALID
```

在这种情况下，推荐的恢复方法是删除无效索引，然后尝试重新执行REINDEX

CONCURRENTLY。 在处理期间创建的并发索引的名称以ccnew为后缀，如果它是一个我们未能删除的旧索引定义，后缀是ccold。 可以使用DROP INDEX删除无效索引，包括无效的toast索引。

常规索引创建允许在同一表上的其他常规索引创建同时发生，但在一个表上一次只能发生一个并发索引创建。在这两种情况下，不允许同时对表上其他类型的模式进行修改。 另一个区别是，常规REINDEX TABLE或REINDEX INDEX命令可以在事务块中执行，但REINDEX CONCURRENTLY不能执行。

REINDEX SYSTEM 不支持 CONCURRENTLY 因为系统目录不能并发重新索引。

此外，排除约束的索引不能并发重新编制索引。 如果此命令中直接命名了这样的索引，则会引发错误。 如果并发重新编制具有排除约束索引的表或数据库，将跳过这些索引。 （它可以不使用CONCURRENTLY选项来重新编制这样的索引）。

示例

重建单个索引：

```
REINDEX INDEX my_index;
```

重建表my\_table上的所有索引：

```
REINDEX TABLE my_table;
```

重建一个特定数据库中的所有索引，且不假设系统索引已经可用：

```
\$ export PGOPTIONS=\"-P\"

\$ psql broken_db

\...

broken_db=\> REINDEX DATABASE broken_db;

broken_db=\> \\q
```

重建表的索引，在重建索引过程中不阻止对相关关系进行读写操作：

```
REINDEX TABLE CONCURRENTLY my_broken_table;
```

兼容性

在 SQL 标准中没有REINDEX命令。

See Also

CREATE INDEX, DROP INDEX, reindexdb

## RELEASE SAVEPOINT

— 销毁一个之前定义的保存点

大纲

```
RELEASE \[ SAVEPOINT \] savepoint_name
```

描述

RELEASE SAVEPOINT销毁在当前事务 中之前定义的一个保存点。

销毁一个保存点会使得它不能再作为一个回滚点，但是它没有其他用户 可见的行为。它不会撤销在该保存点被建立之后执行的命令的效果（要 这样做，可见ROLLBACK TO SAVEPOINT）。当不再需要一个 保存点时销毁它允许系统在事务结束之前回收一些资源。

RELEASE SAVEPOINT也会销毁所有 在该保存点建立之后建立的保存点。

参数

savepoint\_name

要销毁的保存点的名称。

注解

指定一个不是之前定义的保存点名称是错误。

当事务处于中止状态时不能释放保存点。

如果多个保存点具有相同的名称，只有最近被定义的那个会被释放。

示例

建立并且销毁一个保存点：

```
BEGIN;

INSERT INTO table1 VALUES (3);

SAVEPOINT my_savepoint;

INSERT INTO table1 VALUES (4);

RELEASE SAVEPOINT my_savepoint;

COMMIT;
```

上述事务将插入 3 和 4。

兼容性

这个命令符合SQL标准。该标准指定关键词 SAVEPOINT是强制需要的，但 瀚高数据库允许省略。

另见

BEGIN, COMMIT, ROLLBACK, ROLLBACK TO SAVEPOINT, SAVEPOINT

## RESET

— 把一个运行时参数的值恢复到默认值

大纲

```
RESET configuration_parameter

RESET ALL
```

描述

RESET把运行时参数恢复到它们的默认值。 RESET是SET configuration\_parameter TO DEFAULT 的另一种写法。 详见SET。

默认值被定义为如果在当前会话中没有发出过SET， 参数必须具有的值。这个值的实际来源可能是一个编译在内部的默认值、 配置文件、命令行选项、或者针对每个数据库或者每个用户的默认设置。 这和把它定义成”在会话开始时该参数得到的值”有细微的差 别，因为如果该值来自于配置文件，它将被重置为现在配置文件所指定 的任何东西。

RESET的事务行为和SET相同： 它的效果会被事务回滚撤销。

参数

configuration\_parameter

一个可设置的运行时参数名称。可用的参数记录在 第 19 章以及 SET参考页中。

ALL

把所有可设置的运行时参数重置为默认值。

示例

把timezone配置变量设置为默认值：

```
RESET timezone;
```

兼容性

RESET是一种瀚高数据库扩展。

另见

SET, SHOW

## REVOKE

— 移除访问特权

大纲

```
REVOKE \[ GRANT OPTION FOR \]

{ { SELECT \| INSERT \| UPDATE \| DELETE \| TRUNCATE \| REFERENCES \| TRIGGER }

\[, \...\] \| ALL \[ PRIVILEGES \] }

ON { \[ TABLE \] table_name \[, \...\]

\| ALL TABLES IN SCHEMA schema_name \[, \...\] }

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ { SELECT \| INSERT \| UPDATE \| REFERENCES } ( column_name \[, \...\] )

\[, \...\] \| ALL \[ PRIVILEGES \] ( column_name \[, \...\] ) }

ON \[ TABLE \] table_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ { USAGE \| SELECT \| UPDATE }

\[, \...\] \| ALL \[ PRIVILEGES \] }

ON { SEQUENCE sequence_name \[, \...\]

\| ALL SEQUENCES IN SCHEMA schema_name \[, \...\] }

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ { CREATE \| CONNECT \| TEMPORARY \| TEMP } \[, \...\] \| ALL \[ PRIVILEGES \] }

ON DATABASE database_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ USAGE \| ALL \[ PRIVILEGES \] }

ON DOMAIN domain_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ USAGE \| ALL \[ PRIVILEGES \] }

ON FOREIGN DATA WRAPPER fdw_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ USAGE \| ALL \[ PRIVILEGES \] }

ON FOREIGN SERVER server_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ EXECUTE \| ALL \[ PRIVILEGES \] }

ON { { FUNCTION \| PROCEDURE \| ROUTINE } function_name \[ ( \[ \[ argmode \]

\[ arg_name \] arg_type \[, \...\] \] ) \] \[, \...\]

\| ALL { FUNCTIONS \| PROCEDURES \| ROUTINES } IN SCHEMA schema_name

\[, \...\] }

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ USAGE \| ALL \[ PRIVILEGES \] }

ON LANGUAGE lang_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ { SELECT \| UPDATE } \[, \...\] \| ALL \[ PRIVILEGES \] }

ON LARGE OBJECT loid \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ { CREATE \| USAGE } \[, \...\] \| ALL \[ PRIVILEGES \] }

ON SCHEMA schema_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ CREATE \| ALL \[ PRIVILEGES \] }

ON TABLESPACE tablespace_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ GRANT OPTION FOR \]

{ USAGE \| ALL \[ PRIVILEGES \] }

ON TYPE type_name \[, \...\]

FROM { \[ GROUP \] role_name \| PUBLIC } \[, \...\]

\[ CASCADE \| RESTRICT \]

REVOKE \[ ADMIN OPTION FOR \]

role_name \[, \...\] FROM role_name \[, \...\]

\[ CASCADE \| RESTRICT \]
```

描述

REVOKE命令收回之前从一个或者更多角色 授予的特权。关键词PUBLIC隐式定义的全部角色的组。

特权类型的含义见GRANT命令的描述。

注意任何特定角色拥有的特权包括直接授予给它的特权、从它作为其成员的 角色中得到的特权以及授予给PUBLIC的特权。因此，从PUBLIC收回SELECT特权并不一定会意味 着所有角色都会失去在该对象上的SELECT特权：那些直接被授 予的或者通过另一个角色被授予的角色仍然会拥有它。类似地，从一个用户收回SELECT后，如果PUBLIC或者另一个成员关系角色仍有SELECT权利，该用户还是可以使用 SELECT。

如果指定了GRANT OPTION FOR，只会回收该特权的授予选项，特权本身不被回收。否则，特权及其授予选项都会被回收。

如果一个用户持有一个带有授予选项的特权并且把它授予给了其他用户， 那么被那些其他用户持有的该特权被称为依赖特权。如果第一个用户持有 的该特权或者授予选项正在被收回且存在依赖特权，指定 CASCADE可以连带回收那些依赖特权，不指定则会 导致回收动作失败。这种递归回收只影响通过可追溯到该 REVOKE命令的主体的用户链授予的特权。因此，如果该特权经由其他用户授予给受影响用户，受影响用户可能实际上还 保留有该特权。

在回收一个表上的特权时，也会在该表的每一个列上自动回收对应的列 特权（如果有）。

在另一方面，如果一个角色已经被授予一个表上的 特权，那么从个别的列上回收同一个特权将不会生效。

在回收一个角色中的成员关系时，GRANT OPTION被改 称为ADMIN OPTION，但行为是类似的。也要注意这种 形式的命令不允许噪声词GROUP。

注解

用户只能回收由它直接授出的特权。例如，如果用户 A 已经把一个带有 授予选项的特权授予给了用户 B，并且用户 B 接着把它授予给了用户 C， 那么用户 A 无法直接从 C 收回该特权。反而，用户 A 可以从用户 B 收回 该授予选项并且使用CASCADE选项，这样该特权会被 依次从用户 C 回收。对于另一个例子，如果 A 和 B 都把同一个特权授予 给了 C，A 能够收回它们自己的授权但不能收回 B 的授权，因此 C 实际上 仍将拥有该特权。

当一个对象的非拥有者尝试REVOKE该对象上的特权时， 如果该用户在该对象上什么特权都不拥有，该命令会立刻失败。只要有某个 特权可用，该命令将继续，但是它只会收回那些它具有授予选项的特权。 如果没有持有授予选项，REVOKE ALL PRIVILEGES形式 将发出一个警告，而其他形式在没有持有该命令中特别提到的任何特权的 授予选项时就会发出警告（原则上，这些语句也适用于对象拥有者，但是 由于拥有者总是被认为持有所有授予选项，这些情况永远不会发生）。

如果一个超级用户选择发出一个GRANT或者 REVOKE命令，该命令就好像被受影响对象的拥有者发出 的一样被执行。因为所有特权最终来自于对象拥有者（可能是间接地通过 授予选项链），可以由超级用户收回所有特权，但是这可能需要前述的 CASCADE。

REVOKE也可以由一个并非受影响对象的拥有者的角色 完成，但是该角色应该是一个拥有该对象的角色的成员或者是一个在该对象 上拥有特权的WITH GRANT OPTION的角色的成员。 在这种情况中，该命令就好像被实际拥有该对象或者特权的 WITH GRANT OPTION的包含角色发出的一样被执行。 例如，如果表t1被角色g1拥有，而u1 是g1的一个成员，那么u1能收回t1上被记录为由g1授出的特权。这会包括由u1 以及由角色g1的其他成员完成的授予。

如果执行REVOKE的角色持有通过多于一条角色成员 关系路径间接得到的特权，其中哪一条包含将被用于执行该命令的 角色是没有被指明的。在这种情况中，最好使用 SET ROLE成为你想作为其身份执行 REVOKE的特定角色。如果无法做到这一点 可能会导致回收超过你预期的特权，或者根本回收不了任何东西。

示例

从 public 收回表films上的插入特权：

```
REVOKE INSERT ON films FROM PUBLIC;
```

从用户manuel收回视图 kinds上的所有特权：

```
REVOKE ALL PRIVILEGES ON kinds FROM manuel;
```

注意着实际意味着”收回所有我授出的特权”。

从用户joe收回角色admins中的成员关系：

```
REVOKE admins FROM joe;
```

兼容性

GRANT命令的兼容性注解同样适用于 REVOKE。根据标准，关键词 RESTRICT或CASCADE 是必要的，但是瀚高数据库默认假定为 RESTRICT。

另见

GRANT, ALTER DEFAULT PRIVILEGES

## ROLLBACK

— 中止当前事务

大纲

```
ROLLBACK \[ WORK \| TRANSACTION \] \[ AND \[ NO \] CHAIN \]
```

描述

ROLLBACK回滚当前事务并且导致 该事务所作的所有更新都被抛弃。

参数

WORK

TRANSACTION

可选关键词，没有效果。

AND CHAIN

如果指定了AND CHAIN，则立即启动与刚刚完成事务具有相同事务特征（参见SET TRANSACTION）的新事务。 否则，不会启动任何新事务。

注解

使用COMMIT可成功地终止一个事务。

在一个事务块之外发出ROLLBACK会发出一个警告并且不会有效果。 事务块之外的ROLLBACK AND CHAIN 是一个错误.

示例

要中止所有更改：

```
ROLLBACK;
```

兼容性

命令ROLLBACK符合 SQL 标准。窗体ROLLBACK TRANSACTION是一个瀚高数据库扩展。

另见

BEGIN, COMMIT, ROLLBACK TO SAVEPOINT

## ROLLBACK PREPARED

— 取消一个之前为两阶段提交准备好的事务

大纲

```
ROLLBACK PREPARED transaction_id
```

描述

ROLLBACK PREPARED回滚 一个处于准备好状态的事务。

参数

transaction\_id

要被回滚的事务的事务标识符。

注解

要回滚一个准备好的事务，你必须是原先执行该事务的同一个用户或者 是一个超级用户。但是你必须处在执行该事务的同一个会话中。

这个命令不能在一个事务块内被执行。准备好的事务会被立刻回滚。

pg\_prepared\_xacts 系统视图中列出了当前可用的所有准备好的事务。

示例

用事务标识符foobar回滚对应的事务：

```
ROLLBACK PREPARED \'foobar\';
```

兼容性

ROLLBACK PREPARED是一种瀚高数据库扩展。其意图是用于 外部事务管理系统，其中有些已经被标准涵盖（例如 X/Open XA）， 但是那些系统的 SQL 方面未被标准化。

另见

PREPARE TRANSACTION, COMMIT PREPARED

## ROLLBACK TO SAVEPOINT

— 回滚到一个保存点

大纲

```
ROLLBACK \[ WORK \| TRANSACTION \] TO \[ SAVEPOINT \] savepoint_name
```

描述

回滚在该保存点被建立之后执行的所有命令。该保存点保持有效并且可以在 以后再次回滚到它（如果需要）。

ROLLBACK TO SAVEPOINT隐式地销毁在所提及的保存点 之后建立的所有保存点。

参数

savepoint\_name

要回滚到的保存点。

注解

使用RELEASE SAVEPOINT销毁一个保存点而 不抛弃在它建立之后被执行的命令的效果。

指定一个没有被建立的保存点是一种错误。

相对于保存点，游标有一点非事务的行为。在保存点被回滚时，任何在该保存点 内被打开的游标将会被关闭。如果一个先前打开的游标在一个保存点内被FETCH或MOVE命令所影响，而该该保存点 后来又被回滚，那么该游标将保持FETCH使它指向的位置（也就是说由FETCH导致的游标动作不会被回滚）。回滚也不能 撤销关闭一个游标。不过，其他由游标查询导致的副作用（例如 被该查询所调用的易变函数的副作用） 可以被回滚，只要它们发生在一个后来被回滚的保存点期间。 如果一个游标的执行导致事务中止，它会被置于一种不能被执行的状态，这样当 事务被用ROLLBACK TO SAVEPOINT恢复后，该游标也不再能 被使用。

示例

要撤销在my\_savepoint建立后执行的命令的效果：

```
ROLLBACK TO SAVEPOINT my_savepoint;
```

游标位置不会受保存点回滚的影响：

```
BEGIN;

DECLARE foo CURSOR FOR SELECT 1 UNION SELECT 2;

SAVEPOINT foo;

FETCH 1 FROM foo;

?column?

\-\-\-\-\-\-\-\-\--

1

ROLLBACK TO SAVEPOINT foo;

FETCH 1 FROM foo;

?column?

\-\-\-\-\-\-\-\-\--

2

COMMIT;
```

兼容性

SQL标准指定关键词 SAVEPOINT是强制的，但是瀚高数据库和Oracle允许省略它。SQL 只允许WORK而 不是TRANSACTION作为ROLLBACK之后的噪声词。 还有，SQL 有一个可选的子句 AND \[ NO \] CHAIN，当前 瀚高数据库并不支持。在其他方面，这个命令符合 SQL 标准。

另见

BEGIN, COMMIT, RELEASE SAVEPOINT, ROLLBACK, SAVEPOINT

## SAVEPOINT

— 在当前事务中定义一个新的保存点

大纲

```
SAVEPOINT savepoint_name
```

描述

SAVEPOINT在当前事务中建立一个新保存点。

保存点是事务内的一种特殊标记，它允许所有在它被建立之后执行的命令被 回滚，把该事务的状态恢复到它处于保存点时的样子。

参数

savepoint\_name

给新保存点的名字。

注解

使用ROLLBACK TO SAVEPOINT回滚到一个保存点。 使用RELEASE SAVEPOINT销毁一个保存点，但保持在它被建立之后执行的命令的效果。

保存点只能在一个事务块内建立。可以在一个事务内定义多个保存点。

示例

要建立一个保存点并且后来撤销在它建立之后执行的所有命令的效果：

```
BEGIN;

INSERT INTO table1 VALUES (1);

SAVEPOINT my_savepoint;

INSERT INTO table1 VALUES (2);

ROLLBACK TO SAVEPOINT my_savepoint;

INSERT INTO table1 VALUES (3);

COMMIT;
```

上面的事务将插入值 1 和 3，但不会插入 2。

要建立并且稍后销毁一个保存点：

```
BEGIN;

INSERT INTO table1 VALUES (3);

SAVEPOINT my_savepoint;

INSERT INTO table1 VALUES (4);

RELEASE SAVEPOINT my_savepoint;

COMMIT;
```

上面的事务将插入 3 和 4。

兼容性

当建立另一个同名保存点时，SQL 要求之前的那个保存点自动被销毁。在 瀚高数据库中，旧的保存点会被保留，不过在进行 回滚或释放时只能使用最近的那一个（用 RELEASE SAVEPOINT释放较新的保存点将会 导致较旧的保存点再次变得可以被 ROLLBACK TO SAVEPOINT和 RELEASE SAVEPOINT访问）。在其他方面， SAVEPOINT完全符合 SQL。

另见

BEGIN, COMMIT, RELEASE SAVEPOINT, ROLLBACK, ROLLBACK TO SAVEPOINT

## SECURITY LABEL

— 定义或更改应用到一个对象的安全标签

大纲

```
SECURITY LABEL \[ FOR provider \] ON

{

TABLE object_name \|

COLUMN table_name.column_name \|

AGGREGATE aggregate_name ( aggregate_signature ) \|

DATABASE object_name \|

DOMAIN object_name \|

EVENT TRIGGER object_name \|

FOREIGN TABLE object_name

FUNCTION function_name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, \...\] \] ) \] \|

LARGE OBJECT large_object_oid \|

MATERIALIZED VIEW object_name \|

\[ PROCEDURAL \] LANGUAGE object_name \|

PROCEDURE procedure_name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, \...\] \] ) \] \|

PUBLICATION object_name \|

ROLE object_name \|

ROUTINE routine_name \[ ( \[ \[ argmode \] \[ argname \] argtype \[, \...\] \] ) \] \|

SCHEMA object_name \|

SEQUENCE object_name \|

SUBSCRIPTION object_name \|

TABLESPACE object_name \|

TYPE object_name \|

VIEW object_name

} IS \'label\'
```

其中 aggregate\_signature 是：

```
\* \|

\[ argmode \] \[ argname \] argtype \[ , \... \] \|

\[ \[ argmode \] \[ argname \] argtype \[ , \... \] \] ORDER BY \[ argmode \] \[ argname

\] argtype \[ , \... \]
```

描述

SECURITY LABEL对一个数据库对象应用一个安全 标签。可以把任意数量的安全标签（每个标签提供者对应一个）关联到一个给定 的数据库对象。标签提供者是使用函

数register\_label\_provider 注册自己的可装载模块。

+———————————————————————————+  
| 注意： |  
| |  
| register\_label\_provider不是一个 SQL 函数，它只能在被载入 到后端的 C代码中调用。 |  
+———————————————————————————+

标签提供者决定一个给定标签是否合法并且它是否可以被分配该标签给一个给定 对象。一个给定标签的含义也同样由标签提供者判断。 瀚高数据库没有对一个标签提供者是否必须或者如何解释 安全标签做出限定，它仅仅只是提供了一种机制来存储它们。实际上，这个功能是为了允许与基于标签的强制访问控制（MAC）系统集成（例如 SELinux）。这类系统会基于对象标签而不是传统的自主访问控制（DAC）概念（例如用户和组）做出所有访问控制决定。

参数

object\_name

table\_name.column\_name

aggregate\_name

function\_name

procedure\_name

routine\_name

要被贴上标签的对象的名称。表、聚集、域、外部表、函数、存储过程、例程、序列、类型和视图 的名称可以是模式限定的。

provider

这个标签相关联的提供者的名称。所提到的提供者必须已被载入并且必须赞同所提出的标签操作。如果正好只载入了一个提供者，可以出于简洁的需要忽略提供者的名称。

argmode

一个函数，存储过程或者聚集函数参数的模式：IN、OUT、 INOUT或者VARIADIC。如果被忽略，默认值会是 IN。注意SECURITY LABEL并不真正 关心OUT参数，因为判断函数的身份时只需要输入参数。因此列出 IN、INOUT和VARIADIC参数足矣。

argname

一个函数，存储过程或者聚集函数参数的名称。注意SECURITY LABEL 并不真正关心参数的名称，因为判断函数的身份时只需要参数的数据类型。

argtype

一个函数，存储过程或聚集函数参数的数据类型。

large\_object\_oid

大对象的 OID。

PROCEDURAL

这是一个噪声词。

label

写成一个字符串文本的新安全标签。如果写成NULL表示删除 原有的安全标签。

示例

下面的例子展示了如何更改一个表的安全标签。

```
SECURITY LABEL FOR selinux ON TABLE mytable IS

\'system_u:object_r:sepgsql_table_t:s0\';
```

兼容性

在 SQL 标准中没有SECURITY LABEL命令。

另见

sepgsql, src/test/modules/dummy\_seclabel

## SELECT

— 从一个表或视图检索行

大纲

```
\[ WITH \[ RECURSIVE \] with_query \[, \...\] \]

SELECT \[ ALL \| DISTINCT \[ ON ( expression \[, \...\] ) \] \]

\[ \* \| expression \[ \[ AS \] output_name \] \[, \...\] \]

\[ FROM from_item \[, \...\] \]

\[ WHERE condition \]

\[ GROUP BY grouping_element \[, \...\] \]

\[ HAVING condition \[, \...\] \]

\[ WINDOW window_name AS ( window_definition ) \[, \...\] \]

\[ { UNION \| INTERSECT \| EXCEPT } \[ ALL \| DISTINCT \] select \]

\[ ORDER BY expression \[ ASC \| DESC \| USING operator \] \[ NULLS { FIRST \|

LAST } \] \[, \...\] \]

\[ LIMIT { count \| ALL } \]

\[ OFFSET start \[ ROW \| ROWS \] \]

\[ FETCH { FIRST \| NEXT } \[ count \] { ROW \| ROWS } ONLY \]

\[ FOR { UPDATE \| NO KEY UPDATE \| SHARE \| KEY SHARE } \[ OF table_name

\[, \...\] \] \[ NOWAIT \| SKIP LOCKED \] \[\...\] \]
```

其中 from\_item 可以是以下之一：

```
\[ ONLY \] table_name \[ \* \] \[ \[ AS \] alias \[ ( column_alias \[, \...\] ) \] \]

\[ TABLESAMPLE sampling_method ( argument \[, \...\] ) \[ REPEATABLE

( seed ) \] \]

\[ LATERAL \] ( select ) \[ AS \] alias \[ ( column_alias \[, \...\] ) \]

with_query_name \[ \[ AS \] alias \[ ( column_alias \[, \...\] ) \] \]

\[ LATERAL \] function_name ( \[ argument \[, \...\] \] )

\[ WITH ORDINALITY \] \[ \[ AS \] alias \[ ( column_alias

\[, \...\] ) \] \]

\[ LATERAL \] function_name ( \[ argument \[, \...\] \] ) \[ AS \] alias

( column_definition \[, \...\] )

\[ LATERAL \] function_name ( \[ argument \[, \...\] \] ) AS ( column_definition

\[, \...\] )

\[ LATERAL \] ROWS FROM( function_name ( \[ argument \[, \...\] \] ) \[ AS

( column_definition \[, \...\] ) \] \[, \...\] )

\[ WITH ORDINALITY \] \[ \[ AS \] alias \[ ( column_alias

\[, \...\] ) \] \]

from_item \[ NATURAL \] join_type from_item \[ ON join_condition \| USING

( join_column \[, \...\] ) \]
```

并且 grouping\_element 可以是以下之一：

```
( )

expression

( expression \[, \...\] )

ROLLUP ( { expression \| ( expression \[, \...\] ) } \[, \...\] )

CUBE ( { expression \| ( expression \[, \...\] ) } \[, \...\] )

GROUPING SETS ( grouping_element \[, \...\] )

并且 with_query 是：

with_query_name \[ ( column_name \[, \...\] ) \] AS \[ \[ NOT \] MATERIALIZED \]

( select \| values \| insert \| update \| delete )

TABLE \[ ONLY \] table_name \[ \* \]
```

描述

SELECT从零或更多表中检索行。 SELECT的通常处理如下：

1\. WITH列表中的所有查询都会被计算。这些查询实际 充当了在FROM列表中可以引用的临时表。在 FROM中被引用多次的WITH查 询只会被计算一次，除非另有说明，否则NOT MATERIALIZED。 （见下文的WITH 子句）。

2\. FROM列表中的所有元素都会被计算（ FROM中的每一个元素都是一个真实表或者虚拟表）。 如果在FROM列表中指定了多于一个元素，它们会被交叉连接在一起（见下文的FROM 子句）。

3\. 如果指定了WHERE子句，所有不满足该条件的行都会被从输出中消除（见下文的WHERE 子句）。

4\. 如果指定了GROUP BY子句或者如果有聚集函数，输出会被组合成由在一个或者多个值上匹配的行构成的分组，并且在其上计算聚 集函数的结果。如果出现了HAVING子句，它会消除不 满足给定条件的分组（见下文的 GROUP BY 子句以及 HAVING 子句）。

5\. 对于每一个被选中的行或者行组，会使用SELECT 输出表达式计算实际的输出行（见下文的 SELECT 列表）。

6\. SELECT DISTINCT从结果中消除重复的行。 SELECT DISTINCT ON消除在所有指定表达式上匹 配的行。SELECT ALL（默认）将返回所有候选行， 包括重复的行（见下文的DISTINCT子句）。

7\. 通过使用操作符UNION、 INTERSECT和EXCEPT，多于 一个SELECT语句的输出可以被整合形成 一个结果集。UNION操作符返回位于一个或者两 个结果集中的全部行。INTERSECT操作符返回同时 位于两个结果集中的所有行。EXCEPT操作符返回 位于第一个结果集但不在第二个结果集中的行。在所有三种情况下， 重复行都会被消除（除非指定ALL）。可以增加噪 声词DISTINCT来显式地消除重复行。注意虽然 ALL是SELECT自身的默认行为， 但这里DISTINCT是默认行为（见下文的 UNION 子句、INTERSECT 子句以及 EXCEPT 子句）。

8\. 如果指定了ORDER BY子句，被返回的行会以指定的 顺序排序。如果没有给定ORDER BY，系统会以能最 快产生行的顺序返回它们（见下文的 ORDER BY 子句）。

9\. 如果指定了LIMIT（或FETCH FIRST） 或者OFFSET子句，SELECT 语句只返回结果行的一个子集（见下文的LIMIT 子句）。

10.如果指定了FOR UPDATE、 FOR NO KEY UPDATE、 FOR SHARE 或者FOR KEY SHARE， SELECT语句会把被选中的行锁定而不让并发 更新访问它们（见下文的锁定子句）。

你必须拥有在一个SELECT命令中使用的每一列上的 SELECT特权。FOR NO KEY UPDATE、 FORUPDATE、 FOR SHARE或者FOR KEY SHARE 还要求（对这样选中的每一个表至少一列的）UPDATE特权。

参数

- WITH 子句

WITH子句允许你指定一个或者多个在主查询中可以 其名称引用的子查询。在主查询期间子查询实际扮演了临时表或者视图 的角色。每一个子查询都可以是一个SELECT、 TABLE、VALUES、 INSERT、 UPDATE或者 DELETE语句。在WITH中书写 一个数据修改语句（INSERT、 UPDATE或者 DELETE）时，通常要包括一个 RETURNING子句。构成被主查询读取的临时表的是 RETURNING的输出，而不是该语句修改的 底层表。如果省略RETURNING，该语句仍会被执行，但是它 不会产生输出，因此它不能作为一个表从主查询引用。

对于每一个WITH查询，都必须指定一个名称（无需模 式限定）。可选地，可以指定一个列名列表。如果省略该列表，会从该子查 询中推导列名。

如果指定了RECURSIVE，则允许一个 SELECT子查询使用名称引用自身。 这样一个子查询的形式必须是non\_recursive\_term UNION \[ ALL | DISTINCT \] recursive\_term其中递归自引用必须出现在UNION的右手边。每个 查询中只允许一个递归自引用。不支持递归数据修改语句，但是 可以在一个数据查询语句中使用一个递归 SELECT查询的结果。

RECURSIVE的另一个效果是 WITH查询不需要被排序：一个查询可以引用另一个 在列表中比它靠后的查询（不过，循环引用或者互递归没有实现）。 如果没有RECURSIVE，WITH 查询只能引用在WITH列表中位置更前面的兄弟 WITH查询。

当WITH子句中有多个查询时，RECURSIVE应只编写一次，紧跟在WITH之后。 它适用于WITH子句中的所有查询，尽管它对不使用递归或前向引用的查询没有影响。

主查询以及WITH查询全部（理论上）在同一时间 被执行。这意味着从该查询的任何部分都无法看到 WITH中的一个数据修改语句的效果，不过可以读 取其RETURNING输出。如果两个这样的数据修改语句 尝试修改相同的行，结果将无法确定。

WITH查询的一个关键属性是，即使主查询多次引用它们，它们通常每次执行主查询只计算一次。 特别是，数据修改语句确保执行一次而且只执行一次，而与主查询是否读取它们的全部或任何输出无关。

但是，WITH查询可以标记为NOT MATERIALIZED以移除此保证。 在这种情况下，WITH查询可以折叠到主查询中，就好像它是主查询的FROM子句中的简单的sub-SELECT。 如果主查询多次引用WITH查询，则会导致重复计算;但是，如果每次此类使用只需要WITH查询的总输出中的几行，NOT MATERIALIZED可以通过允许查询联合优化来节省开销。 NOT MATERIALIZED被忽略，如果它被附加到一个递归的WITH查询，或者不是边际效应无关的（也就是说，不是包含非易失性函数的普通的SELECT）。

默认情况下，如果查询在主查询的FROM子句中仅一次使用，则边际效应无关的WITH查询将折叠到主查询中。 这允许在语义不可见的情况下两个查询级别的联合优化。 但是，通过将WITH查询标记为MATERIALIZED，可以防止此类折叠。 这可能很有用，例如，如果WITH查询被用作优化围栏，以防止规划者选择错误计划。 瀚高数据库v12版本之前没有做过这样的折叠，所以为旧版本编写的查询可能依赖于WITH作为优化围栏。

- FROM 子句

FROM子句为SELECT 指定一个或者更多源表。如果指定了多个源表，结果将是所有源表的 笛卡尔积（交叉连接）。但是通常会增加限定条件（通过 WHERE）来把返回的行限制为该笛卡尔积的一个小子集。

FROM子句可以包含下列元素：

table\_name

一个现有表或视图的名称（可以是模式限定的）。如果在表名前指定了 ONLY，则只会扫描该表。如果没有指定 ONLY，该表及其所有后代表（如果有）都会被扫描。可选地，可以在表名后指定\*来显式地指示包括后代表。

alias

一个包含别名的FROM项的替代名称。别名被用于 让书写简洁或者消除自连接中的混淆（其中同一个表会被扫描多 次）。当提供一个别名时，表或者函数的实际名称会被隐藏。例如，给定FROM foo AS f， SELECT的剩余部分就必须以 f而不是foo来引用这个 FROM项。如果写了一个别名，还可以写一个列别 名列表来为该表的一个或者多个列提供替代名称。

TABLESAMPLE sampling\_method ( argument \[,...\] ) \[ REPEATABLE ( seed ) \]

table\_name之后的 TABLESAMPLE子句表示应该用指定的 sampling\_method 来检索表中行的子集。这种采样优先于任何其他过滤器（例如 WHERE子句）。标准 瀚高数据库发布包括两种采样 方法：BERNOULLI和SYSTEM， 其他采样方法可以通过扩展安装在数据库中。

BERNOULLI以及SYSTEM采样方法都接受 一个参数，它表示要采样的表 的分数，表示为一个 0 到 100 之间的百分数。这个参数可以是任意的 实数值表达式（其他的采样方法可能接受更多或者不同的 参数）。这两种方法都返回一个随机选取的该表采样，其中包含了指定 百分数的表行。BERNOULLI方法扫描整个表并且 用指定的几率选择或者忽略行。SYSTEM方法会做 块层的采样，每个块都有指定的机会能被选中，被选中块中的所有行都 会被返回。在指定较小的采样百分数时，SYSTEM 方法要比BERNOULLI方法快很多，但是前者可能 由于聚簇效应返回随机性较差的表采样。

可选的REPEATABLE子句指定一个用于产生采样方法中随机数的种子数或表达式。种子值可以是任何非空浮点值。如果查询时表没有被更改，指定相同种子和argument值的两个查询将会选择该表相同的采样。但是不同的种子值通常将会产生不同的采样。如果没有给出REPEATABLE，则会基于一个系统产生的种子为每一个查询选择一个新的随机采样。注意有些扩展采样方法不接受REPEATABLE，并且将总是为每一次使用产生新的采样。

select

一个子-SELECT可以出现在FROM子句中。这就好像把它的输出创建为一个 存在于该SELECT命令期间的临时表。注意 子-SELECT必须用圆括号包围，并且 必须为它提供一个别名。也可以在这里使用一个VALUES命令。

with\_query\_name

可以通过写一个WITH查询的名称来引用它，就好像该查询的名称是一个表名（实际上，该WITH查询会 为主查询隐藏任何具有相同名称的真实表。如果必要，你可以使用带模式限定的方式以相同的名称来引用真实表）。可以像表一样，以同样的方式提供一个别名。

function\_name

函数调用可以出现在FROM子句中（对于返回结果 集合的函数特别有用，但是可以使用任何函数）。这就好像把该函数的 输出创建为一个存在于该SELECT命令期 间的临时表。当为该函数调用增加可选的 WITH ORDINALITY子句时，会在该函数 的输出列之后追加一个新的列来为每一行编号。

可以用和表一样的方式提供一个别名。如果写了一个别名，还可以写一个 列别名列表来为该函数的组合返回类型的一个或者多个属性提供替代名称，包括由ORDINALITY（如果有）增加的新列。

通过把多个函数调用包围在ROWS FROM(... )中可以把它们 整合在单个FROM-子句项中。这样一个项的输出是把每一个 函数的第一行串接起来，然后是每个函数的第二行，以此类推。如果有些 函数产生的行比其他函数少，则在缺失数据的地方放上空值，这样被返回 的总行数总是和产生最多行的函数一样。

如果函数被定义为返回record数据类型，那么必须出现一个 别名或者关键词AS，后面跟上形为 ( column\_name data\_type \[,... \])的列定义列表。列定义列表必须匹配该函数返回的列的实际 数量和类型。

在使用ROWS FROM(... )语法时，如果函数之一要求一个列 定义列表，最好把该列定义列表放在ROWS FROM(... )中该 函数的调用之后。当且仅当正好只有一个函数并且没有WITH ORDINALITY子句时，才能把列定义列表放在 ROWS FROM(... )结构后面。

要把ORDINALITY和列定义列表一起使用，你必须使用 ROWS FROM(... )语法，并且把列定义列表放在 ROWS FROM(... )里面。

join\_type

One of

• \[ INNER \] JOIN

• LEFT \[ OUTER \] JOIN

• RIGHT \[ OUTER \] JOIN

• FULL \[ OUTER \] JOIN

• CROSS JOIN

对于INNER和OUTER连接类型，必须指定 一个连接条件，即NATURAL、ON join\_condition或者 USING (join\_column \[,...\]) 之一（只能有一种）。其含义见下文。对于 CROSS JOIN，上述子句不能出现。

一个JOIN子句联合两个FROM项（ 为了方便我们称之为”表”，尽管实际上它们可以是任何类型 的FROM项）。如有必要可以使用圆括号确定嵌套的顺序。 在没有圆括号时，JOIN会从左至右嵌套。在任何情 况下，JOIN的联合比分隔FROM-列表 项的逗号更强。

CROSS JOIN和INNER JOIN 会产生简单的笛卡尔积，也就是与在FROM的顶层列出两个 表得到的结果相同，但是要用连接条件（如果有）约束该结果。 CROSS JOIN与INNER JOIN ON (TRUE)等效，也就是说条件不会移除任何行。这些连接类型只是一种 记号上的方便，因为没有什么是你用纯粹的FROM和 WHERE能做而它们不能做的。

LEFT OUTER JOIN返回被限制过的笛卡尔积 中的所有行（即所有通过了其连接条件的组合行），外加左手表中 没有相应的通过了连接条件的右手行的每一行的拷贝。通过在右手列中插入空值，这种左手行会被扩展为连接表的完整行。注意在决 定哪些行匹配时，只考虑JOIN子句自身的条件。之后 才应用外条件。

相反，RIGHT OUTER JOIN返回所有连接行，外加每 一个没有匹配上的右手行（在左端用空值扩展）。这只是为了记号 上的方便，因为你可以通过交换左右表把它转换成一个LEFT OUTER JOIN。

FULL OUTER JOIN返回所有连接行，外加每 一个没有匹配上的左手行（在右端用空值扩展），再外加每一个没有 匹配上的右手行（在左端用空值扩展）。

ON join\_condition

join\_condition 是一个会得到boolean类型值的表达式（类似于一个 WHERE子句），它说明一次连接中哪些行被认为 相匹配。

USING ( join\_column \[,...\] )

形式USING ( a, b,... )的子句是 ON left\_table.a = right\_table.a AND left\_table.b = right\_table.b...的简写。还有， USING表示每一对相等列中只有一个会被 包括在连接输出中。

NATURAL

NATURAL是一个USING列表的速记，该列表中提到两个表中具有匹配名称的所有的列。如果没有公共列名，则NATURAL等效于ON TRUE。

LATERAL

LATERAL关键词可以放在一个 子-SELECT FROM项前面。这允许该 子-SELECT引用FROM列表中在它之 前的FROM项的列（如果没有LATERAL，每一 个子-SELECT会被独立计算并且因此不能交叉引用 任何其他的FROM项）。

LATERAL也可以放在一个函数调用 FROM项前面，但是在这种情况下它只是一个噪声 词，因为在任何情况下函数表达式都可以引用在它之前的 FROM项。

LATERAL项可以出现在FROM列表 顶层，或者一个JOIN中。在后一种情况中，它也可以引用其作为右手端的JOIN左手端上的任何项。

当一个FROM项包含LATERAL交叉引用 时，计算会如此进行：对提供被交叉引用列的FROM项的每 一行或者提供那些列的多个FROM项的每一个行集，使用该 行或者行集的那些列值计算LATERAL项。结果行会与 计算得到它们的行进行通常的连接。对来自哪些列的源表的每一行或者行 集都会重复这样的步骤。

列的源表必须以INNER或者LEFT的方式连接到 LATERAL项，否则就没有用于为 LATERAL项计算每一个行集的良定行集。尽管 X RIGHT JOIN LATERAL Y这样的结构在语法上是合法的， 但实际上不允许用于在Y中引用 X。

- WHERE 子句

可选的WHERE子句的形式

WHERE condition

其中condition 是任一计算得到布尔类型结果的表达式。任何不满足 这个条件的行都会从输出中被消除。如果用一行的实际值替换其中的 变量引用后，该表达式返回真，则该行符合条件。

- GROUP BY 子句

可选的GROUP BY子句的形式

GROUP BY grouping\_element \[,...\]

GROUP BY将会把所有被选择的行中共享相同分组表达式 值的那些行压缩成一个行。一个被用在 grouping\_element中的 expression可以是输入列名、输出列 （SELECT列表项）的名称或序号或者由输入列 值构成的任意表达式。在出现歧义时，GROUP BY名称 将被解释为输入列名而不是输出列名。

如果任何GROUPING SETS、ROLLUP或者 CUBE作为分组元素存在，则GROUP BY子句 整体上定义了数个独立的分组集。其效果等效于在子 查询间构建一个UNION ALL，子查询带有分组集作为它们 的GROUP BY子句。

聚集函数（如果使用）会在组成每一个分组的所有行上进行计算，从而为每 一个分组产生一个单独的值（如果有聚集函数但是没有 GROUP BY子句，则查询会被当成是由所有选中行构成 的一个单一分组）。传递给每一个聚集函数的行集合可以通过在聚集函数调用附加一个FILTER子句来进一步过滤。当存在一个 FILTER子句时，只有那些匹配它的行才会被包括在该聚 集函数的输入中。

当存在GROUP BY子句或者任何聚集函数时， SELECT列表表达式不能引用非分组列（除非它出现在聚集函数中或者它函数依赖于分组列），因为这样做会导致返回 非分组列的值时会有多种可能的值。如果分组列是包含非分组列的表的主键（ 或者主键的子集），则存在函数依赖。

记住所有的聚集函数都是在HAVING子句或者 SELECT列表中的任何”标量”表达式之前被计算。 这意味着一个CASE表达式不能被用来跳过一个聚集表达式的计算。

当前，FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE和FOR KEY SHARE不能和 GROUP BY一起指定。

- HAVING 子句

可选的HAVING子句的形式

HAVING condition

其中condition与 WHERE子句中指定的条件相同。

HAVING消除不满足该条件的分组行。 HAVING与WHERE不同： WHERE会在应用GROUP BY之前过滤个体行，而HAVING过滤由 GROUP BY创建的分组行。 condition中引用 的每一个列必须无歧义地引用一个分组列（除非该引用出现在一个聚集 函数中或者该非分组列函数依赖于分组列。

即使没有GROUP BY子句，HAVING 的存在也会把一个查询转变成一个分组查询。这和查询中包含聚集函数但没有 GROUP BY子句时的情况相同。所有被选择的行都被认为是一个 单一分组，并且SELECT列表和 HAVING子句只能引用聚集函数中的表列。如果该 HAVING条件为真，这样一个查询将会发出一个单一行； 否则不返回行。

当前，FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE和FOR KEY SHARE不能与 HAVING一起指定。

- WINDOW 子句

可选的WINDOW子句的形式

WINDOW window\_name AS ( window\_definition ) \[,...\]

其中window\_name 是一个可以从OVER子句或者后续窗口定义中引用的名称。

window\_definition是

```
\[ existing_window_name \]

\[ PARTITION BY expression \[, \...\] \]

\[ ORDER BY expression \[ ASC \| DESC \| USING operator \] \[ NULLS { FIRST \| LAST } \]

\[, \...\] \]

\[ frame_clause \]
```

如果指定了一个existing\_window\_name， 它必须引用WINDOW列表中一个更早出现的项。新窗口将从 该项中复制它的划分子句以及排序子句（如果有）。在这种情况下，新窗口不能指定它自己的PARTITION BY子句，并且它只能在被复制 窗口没有ORDER BY的情况下指定该子句。新窗口总是使用它 自己的帧子句，被复制的窗口不必指定一个帧子句。

PARTITION BY列表元素的解释以 GROUP BY 子句元素的方式 进行，不过它们总是简单表达式并且绝不能是输出列的名称或编号。另一个区 别是这些表达式可以包含聚集函数调用，而这在常规GROUP BY 子句中是不被允许的。它们被允许的原因是窗口是出现在分组和聚集之后的。

类似地，ORDER BY列表元素的解释也以 ORDER BY 子句元素的方式进行， 不过该表达式总是被当做简单表达式并且绝不会是输出列的名称或编号。

可选的frame\_clause为依赖帧的窗口函数 定义窗口帧（并非所有窗口函数都依赖于帧）。

窗口帧是查询中 每一样（称为当前行）的相关行的集合。 frame\_clause可以是

```
{ RANGE \| ROWS \| GROUPS } frame_start \[ frame_exclusion \]

{ RANGE \| ROWS \| GROUPS } BETWEEN frame_start AND frame_end \[ frame_exclusion \]
```

之一，其中frame\_start和frame\_end可以是

```
UNBOUNDED PRECEDING

offset PRECEDING

CURRENT ROW

offset FOLLOWING

UNBOUNDED FOLLOWING
```

之一，并且frame\_exclusion可以是

```
EXCLUDE CURRENT ROW

EXCLUDE GROUP

EXCLUDE TIES

EXCLUDE NO OTHERS
```

之一。如果省略frame\_end，它会被默认为CURRENT ROW。限制是：

frame\_start不能是UNBOUNDED FOLLOWING， frame\_end不能是UNBOUNDED PRECEDING， 并且frame\_end的选择在上面of frame\_start以及frame\_end 选项的列表中不能早于 frame\_start的选择 — 例如RANGE BETWEEN CURRENT ROW AND offset PRECEDING是不被允许的。

默认的帧选项是RANGE UNBOUNDED PRECEDING，它和RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW相同。它把帧设置为从分区开始直到当前行的最后一个平级行（被该窗口的ORDER BY子句认为等价于当前行的行，如果没有ORDER BY则所有的行都是平级的）。通常，UNBOUNDED PRECEDING表从分区第一行开始的帧，类似地 UNBOUNDED FOLLOWING表示以分区最后一行结束的帧，不论是处于RANGE、ROWS或者GROUPS模式中。在ROWS模式中，CURRENT ROW表示以当前行开始或者结束的帧。而在RANGE或者GROUPS模式中它表示当前行在ORDER BY排序中的第一个 或者最后一个平级行开始或者结束的帧。offset PRECEDING和offset FOLLOWING选项的含义会随着帧模式而变化。在ROWS模式中，offset是一个整数，表示帧开始或者结束于当前行之前或者之后的那么多行处。在GROUPS模式中，offset是一个整数，表示真开始或者结束于当前行的平级组之前或者之后那么多个平级组处，其中平级组是一组根据窗口的ORDER BY子句等效的行。在RANGE模式中，offset选项的使用要求在窗口定义中正好有一个ORDER BY列。那么该帧包含的行的排序列值不超过offset且小于（对于PRECEDING）或者大于（对于FOLLOWING）当前行的排序列值。在这些情况中，offset表达式的数据类型取决于排序列的数据类型。对于数字排序列，它通常与排序列是相同类型，但对于datetime类型的排序列它是interval。在所有这些情况中，offset的值必须是非空和非负。此外，虽然offset并非必须是简单常量，但它不能包含变量、聚集函数或者窗口函数。

frame\_exclusion选项允许从帧中排除当前行周围的行，即便根据帧的起始选项来说它们应该被包含在帧中。EXCLUDE CURRENT ROW把当前行从帧中排除。EXCLUDE GROUP把当前行和它在排序上的平级行从帧中排除。EXCLUDE TIES从帧中排除当前行的任何平级行，但是不排除当前行本身。EXCLUDE NO OTHERS只是明确地指定不排除当前行或其平级行的默认行为。

注意，如果ORDER BY排序无法把行唯一地排序，则ROWS模式可能产生不可预测的结果。RANGE以及GROUPS模式的目的是确保在ORDER BY顺序中平等的行被同样对待：一个给定平级组中的所有行将在一个帧中或者被从帧中排除。

WINDOW子句的目的是指定出现在查询的 SELECT 列表或 ORDER BY 子句中的 窗口函数的行为。这些函数可以在它们的 OVER子句中用名称引用WINDOW 子句项。不过，WINDOW子句项不是必须被引用。 如果在查询中没有用到它，它会被简单地忽略。可以使用根本没有任何 WINDOW子句的窗口函数，因为窗口函数调用可 以直接在其OVER子句中指定它的窗口定义。不过，当多 个窗口函数都需要相同的窗口定义时， WINDOW子句能够减少输入。

当前，FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE和FOR KEY SHARE不能和 WINDOW一起被指定。

- SELECT 列表

SELECT列表（位于关键词 SELECT和FROM之间）指定构成 SELECT语句输出行的表达式。这些表达式 可以（并且通常确实会）引用FROM子句中计算得到的列。

正如在表中一样，SELECT的每一个输出列都有一个名称。 在一个简单的SELECT中，这个名称只是被用来标记要显 示的列，但是当SELECT是一个大型查询的一个子查询时，大型查询会把该名称看做子查询产生的虚表的列名。要指定用于输出列的名称，在该列的表达式后面写上 AS output\_name（ 你可以省略AS，但只能在期望的输出名称不匹配任何 瀚高数据库关键词（见附录 C）时省略。为了避免和未来增加的关键词冲突， 推荐总是写上AS或者用双引号引用输出名称）。如果你不指定列名， 瀚高数据库会自动选择一个名称。如果列的表达式是一个简单的列引用，那么被选择的名称就和该列的名称相同。在使用函数或者类型名称 的更复杂的情况中，系统可能会生成诸如?column?之类的名称。

一个输出列的名称可以被用来在ORDER BY以及 GROUP BY子句中引用该列的值，但是不能用于WHERE和HAVING子句（在其中 必须写出表达式）。

可以在输出列表中写\*来取代表达式，它是被选中 行的所有列的一种简写方式。还可以写 table\_name.\*，它 是只来自那个表的所有列的简写形式。在这些情况中无法用 AS指定新的名称，输出行的名称将和表列的名称相同。

根据 SQL 标准，输出列表中的表达式应该在应用DISTINCT、ORDER BY或者LIMIT之前计算。

在使用DISTINCT时显然必须这样做，否则就无法搞清到底在区分什么值。不过，在很多情况下如果先计算ORDER BY和LIMIT再计算输出表达式会很方便，特别是如果输出列表中包含任何volatile 函数或者代价昂贵的函数时尤其如此。通过这种行为，函数计算的顺序更加直观并且对于从未出现在输出中的行将不会进行计算。只要输出表达式没有被DISTINCT、ORDER BY或者GROUP BY引用，瀚高数据库实际将在排序和限制行数之后计算输出表达式（作为一个反例，SELECT f(x) FROM tab ORDER BY 1显然必须在排序之前计算f(x)）。包含有集合返回函数的输出表达式实际是在排序之后和限制行数之前被计算，这样LIMIT才能切断来自集合返回函数的输出。

- DISTINCT 子句

如果指定了SELECT DISTINCT，所有重复的行会被从结果集中移除（为每一组重复的行保留一行）。SELECT ALL则 指定相反的行为：所有行都会被保留，这也是默认情况。

SELECT DISTINCT ON ( expression \[,...\] ) 只保留在给定表达式上计算相等的行集合中的第一行。 DISTINCT ON表达式使用和 ORDER BY相同的规则（见上文）解释。注意，除非用ORDER BY来确保所期望的行出现在第一位，每一个集 合的”第一行”是不可预测的。例如：

```
SELECT DISTINCT ON (location) location, time, report

FROM weather_reports

ORDER BY location, time DESC;
```

为每个地点检索最近的天气报告。但是如果我们不使用 ORDER BY来强制对每个地点的时间值进行降序排序， 我们为每个地点得到的报告的时间可能是无法预测的。

DISTINCT ON表达式必须匹配最左边的 ORDER BY表达式。ORDER BY子句通常 将包含额外的表达式，这些额外的表达式用于决定在每一个 DISTINCT ON分组内行的优先级。

当前，FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE和FOR KEY SHARE不能和 DISTINCT一起使用。

- UNION 子句

UNION子句具有下面的形式：

```
select_statement UNION \[ ALL \| DISTINCT \] select_statement
```

select\_statement 是任何没有ORDER BY、LIMIT、 FOR NO KEY UPDATE、FOR UPDATE、FOR SHARE和FOR KEY SHARE子句的 SELECT语句（如果子表达式被包围在圆括号内， ORDER BY和LIMIT可以被附着到其上。如果没有 圆括号，这些子句将被应用到UNION的结果而不是右手边 的表达式上）。

UNION操作符计算所涉及的 SELECT语句所返回的行的并集。如果一行 至少出现在两个结果集中的一个内，它就会在并集中。作为 UNION两个操作数的 SELECT语句必须产生相同数量的列并且 对应位置上的列必须具有兼容的数据类型。

UNION的结果不会包含重复行，除非指定了 ALL选项。ALL会阻止消除重复（因此， UNION ALL通常显著地快于UNION， 尽量使用ALL）。可以写DISTINCT来 显式地指定消除重复行的行为。

除非用圆括号指定计算顺序， 同一个SELECT语句中的多个UNION操作符会从左至右计算。

当前，FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE和 FOR KEY SHARE不能用于UNION结果或者 UNION的任何输入。

- INTERSECT 子句

INTERSECT子句具有下面的形式：

```
select_statement INTERSECT \[ ALL \| DISTINCT \] select_statement
```

select\_statement 是任何没有ORDER BY, LIMIT、FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE以及FOR KEY SHARE子句的 SELECT语句。

INTERSECT操作符计算所涉及的 SELECT语句返回的行的交集。如果 一行同时出现在两个结果集中，它就在交集中。

INTERSECT的结果不会包含重复行，除非指定了 ALL选项。如果有ALL，一个在左表中有 m次重复并且在右表中有n 次重复的行将会在结果中出现 min(m,n) 次。 DISTINCT可以写DISTINCT来 显式地指定消除重复行的行为。

除非用圆括号指定计算顺序， 同一个SELECT语句中的多个 INTERSECT操作符会从左至右计算。 INTERSECT的优先级比 UNION更高。也就是说， A UNION B INTERSECT C将被读成A UNION (B INTERSECT C)。

当前，FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE和 FOR KEY SHARE不能用于INTERSECT结果或者 INTERSECT的任何输入。

- EXCEPT 子句

EXCEPT子句具有下面的形式：

```
select_statement EXCEPT \[ ALL \| DISTINCT \] select_statement
```

select\_statement 是任何没有ORDER BY、LIMIT、FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE以及FOR KEY SHARE子句的 SELECT语句。

EXCEPT操作符计算位于左 SELECT语句的结果中但不在右SELECT语句结果中的行集合。

EXCEPT的结果不会包含重复行，除非指定了ALL选项。如果有ALL，一个在左表中有 m次重复并且在右表中有 n次重复的行将会在结果集中出现 max(m-n,0) 次。 DISTINCT可以写DISTINCT来 显式地指定消除重复行的行为。

除非用圆括号指定计算顺序， 同一个SELECT语句中的多个 EXCEPT操作符会从左至右计算。EXCEPT的优先级与 UNION相同。

当前，FOR NO KEY UPDATE、FOR UPDATE、 FOR SHARE和 FOR KEY SHARE不能用于EXCEPT结果或者 EXCEPT的任何输入。

- ORDER BY 子句

可选的ORDER BY子句的形式如下：

```
ORDER BY expression \[ ASC \| DESC \| USING operator \] \[ NULLS { FIRST \| LAST } \]

\[, \...\]
```

ORDER BY子句导致结果行被按照指定的表达式排序。 如果两行按照最左边的表达式是相等的，则会根据下一个表达式比较它们， 依次类推。如果按照所有指定的表达式它们都是相等的，则它们被返回的 顺序取决于实现。

每一个expression 可以是输出列（SELECT列表项）的名称或者序号，它也可以是由输入列值构成的任意表达式。

序号指的是输出列的顺序（从左至右）位置。这种特性可以为不具有唯一 名称的列定义一个顺序。这不是绝对必要的，因为总是可以使用 AS子句为输出列赋予一个名称。

也可以在ORDER BY子句中使用任意表达式，包括没有出现在SELECT输出列表中的列。因此，下面的语句是合法的：

```
SELECT name FROM distributors ORDER BY code;
```

这种特性的一个限制是一个应用在UNION、 INTERSECT或EXCEPT子句结果上的 ORDER BY只能指定输出列名称或序号，但不能指定表达式。

如果一个ORDER BY表达式是一个既匹配输出列名称又匹配 输入列名称的简单名称，ORDER BY将把它解读成输出列名 称。这与在同样情况下GROUP BY会做出的选择相反。这种 不一致是为了与 SQL 标准兼容。

可以为ORDER BY子句中的任何表达式之后增加关键词 ASC（上升）DESC（下降）。如果没有指定， ASC被假定为默认值。或者，可以在USING 子句中指定一个特定的排序操作符名称。一个排序操作符必须是某个 B-树操作符族的小于或者大于成员。ASC通常等价于 USING <而DESC通常等价于 USING >（但是一种用户定义数据类型的创建者可以 准确地定义默认排序顺序是什么，并且它可能会对应于其他名称的操作符）。

如果指定NULLS LAST，空值会排在非空值之后；如果指定 NULLS FIRST，空值会排在非空值之前。如果都没有指定， 在指定或者隐含ASC时的默认行为是NULLS LAST， 而指定或者隐含DESC时的默认行为是 NULLS FIRST（因此，默认行为是空值大于非空值）。 当指定USING时，默认的空值顺序取决于该操作符是否为 小于或者大于操作符。

注意顺序选项只应用到它们所跟随的表达式上。例如 ORDER BY x, y DESC和 ORDER BY x DESC, y DESC是不同的。

字符串数据会被根据引用到被排序列上的排序规则排序。根据需要可以通过在expression中包括一个 COLLATE子句来覆盖，例如 ORDER BY mycolumn COLLATE "en\_US"。

- LIMIT 子句

LIMIT子句由两个独立的子句构成：

```
LIMIT { count \| ALL }

OFFSET start
```

count指定要返回 的最大行数，而start 指定在返回行之前要跳过的行数。在两者都被指定时，在开始计算要返回的 count行之前会跳过 start行。

如果count表达式计算 为 NULL，它会被当成LIMIT ALL，即没有限制。如果 start计算为 NULL，它会被当作OFFSET 0。

SQL:2008 引入了一种不同的语法来达到相同的结果， 瀚高数据库也支持它：

```
OFFSET start { ROW \| ROWS }

FETCH { FIRST \| NEXT } \[ count \] { ROW \| ROWS } ONLY
```

在这种语法中，标准要求start或count是一个文本常量、一个参数或者一个变量名。而作为一种 瀚高数据库的扩展，还允许其他的表达式，但通常需要被封闭在圆括号中以避免歧义。如果在一个

FETCH子句中省略 count，它的默认值为 1。

ROW和ROWS以及 FIRST和NEXT是噪声，它们不影响这些子句的效果。根据标准，如果都存在，OFFSET子句必须出现在FETCH子句之前。但是瀚高数据库更宽松，它允许两种顺序。

在使用LIMIT时，用一个ORDER BY子句把 结果行约束到一个唯一顺序是个好办法。否则你讲得到该查询结果行的 一个不可预测的子集 — 你可能要求从第 10 到第 20 行，但是在什么顺序下的第10到第20呢？除非指定ORDER BY，你是不知道顺序的。

查询规划器在生成一个查询计划时会考虑LIMIT，因此 根据你使用的LIMIT和OFFSET，你很可能 得到不同的计划（得到不同的行序）。所以，使用不同的 LIMIT/OFFSET值来选择一个查询结果的 不同子集将会给出不一致的结果，除非你 用ORDER BY强制一种可预测的结果顺序。这不是一个缺陷，它是 SQL 不承诺以任何特定顺序（除非使用 ORDER BY来约束顺序）给出一个查询结果这一事实造 成的必然后果。

如果没有一个ORDER BY来强制选择一个确定的子集， 重复执行同样的LIMIT查询甚至可能会返回一个表中行的不同子集。同样，这也不是一种缺陷，再这样一种情况下也无法 保证结果的确定性。

- 锁定子句

FOR UPDATE、FOR NO KEY UPDATE、 FOR SHARE和FOR KEY SHARE 是锁定子句，它们影响SELECT把行从表中取得时如何对它们加锁。

锁定子句的一般形式：

```
FOR lock_strength \[ OF table_name \[, \...\] \] \[ NOWAIT \| SKIP LOCKED \]
```

其中lock\_strength可以是

```
UPDATE

NO KEY UPDATE

SHARE

KEY SHARE
```

为了防止该操作等待其他事务提交，可使用NOWAIT或者 SKIP LOCKED选项。使用NOWAIT时，如果选中的行不能被立即锁定，该语句会报告错误而不是等待。使用 SKIP LOCKED时，无法被立即锁定的任何选中行都 会被跳过。跳过已锁定行会提供数据的一个不一致的视图，因此这不适合 于一般目的的工作，但是可以被用来避免多个用户访问一个类似队列的表 时出现锁竞争。注意NOWAIT和 SKIP LOCKED只适合行级锁 — 所要求的 ROW SHARE表级锁仍然会以常规的方式取得。如果想要不等待的表级锁，你可以先 使用带NOWAIT的LOCK。

如果在一个锁定子句中提到了特定的表，则只有来自于那些表的 行会被锁定，任何SELECT中用到的 其他表还是被简单地照常读取。一个没有表列表的锁定子句会影响 该语句中用到的所有表。如果一个锁定子句被应用到一个视图或者 子查询，它会影响在该视图或子查询中用到的所有表。不过，这些 子句不适用于主查询引用的WITH查询。如果你希望在一个WITH查询中发生行锁定，应该在该 WITH查询内指定一个锁定子句。

如果有必要对不同的表指定不同的锁定行为，可以写多个锁定子句。 如果同一个表在多于一个锁定子句中被提到（或者被隐式的影响到）， 那么会按照所指定的最强的锁定行为来处理它。类似地，如果在任何 影响一个表的子句中指定了NOWAIT，就会按照 NOWAIT的行为来处理该表。否则如果 SKIP LOCKED在任何影响该表的子句中被指定， 该表就会被按照SKIP LOCKED来处理。

如果被返回的行无法清晰地与表中的行保持一致，则不能使用锁定子句。 例如锁定子句不能与聚集一起使用。

当一个锁定子句出现在一个SELECT查询的顶层时， 被锁定的行正好就是该查询返回的行。在连接查询的情况下，被锁定 的行是那些对返回的连接行有贡献的行。此外，自该查询的快照起满足 查询条件的行将被锁定，如果它们在该快照后被更新并且不再满足 查询条件，它们将不会被返回。如果使用了LIMIT，只要已经返回的行数满足了限制，锁定就会停止（但注意被 OFFSET跳过的行将被锁定）。类似地，如果在一个游标 的查询中使用锁定子句，只有被该游标实际取出或者跳过的行才将被锁定。

当一个锁定子句出现在一个子-SELECT中时，被锁定行是那些该子查询返回给外层查询的行。这些被锁定的行的数量可能比 从子查询自身的角度看到的要少，因为来自外层查询的条件可能会被用 来优化子查询的执行。例如：

```
SELECT \* FROM (SELECT \* FROM mytable FOR UPDATE) ss WHERE col1 = 5;
```

将只锁定具有col1 = 5的行（虽然在子查询中并没有写上 该条件）。

早前的发行无法维持一个被之后的保存点升级的锁。例如，这段代码：

```
BEGIN;

SELECT \* FROM mytable WHERE key = 1 FOR UPDATE;

SAVEPOINT s;

UPDATE mytable SET \... WHERE key = 1;

ROLLBACK TO s;
```

> **小心：**
> 
> 一个运行在 `READ COMMITTED` 事务隔离级别并且使用 `ORDER BY` 和锁定子句的 `SELECT` 命令有可能返回无序的行。这是因为 `ORDER BY` 会被首先应用。该命令对结果排序，但是可能接着在尝试获得一个或者多个行上的锁时阻塞。一旦 `SELECT` 解除阻塞，某些排序列值可能已经被修改，从而导致那些行变成无序的（尽管它们根据原始列值是有序的）。根据需要，可以通过在子查询中放置 `FOR UPDATE/SHARE` 来解决之一问题，例如：
> 
> sql
> 
> ```
> SELECT * FROM (SELECT * FROM mytable FOR UPDATE) ss ORDER BY column1;
> ```
> 
> 注意这将导致锁定 `mytable` 的所有行，而顶层的 `FOR UPDATE` 只会锁定实际被返回的行。这可能会导致显著的性能差异，特别是把 `ORDER BY` 与 `LIMIT` 或者其他限制组合使用时。因此只有在并发更新排序列并且要求严格的排序结果时才推荐使用这种技术。
> 
> 在 `REPEATABLE READ` 或者 `SERIALIZABLE` 事务隔离级别上这可能导致一个序列化失败（SQLSTATE 是’40001’），因此在这些隔离级别下不可能收到无序行。

- TABLE 命令

命令

```
TABLE name
```

等价于

```
SELECT \* FROM name
```

它可以被用作一个顶层命令，或者用在复杂查询中以节省空间。只有 WITH、UNION、INTERSECT、EXCEPT、 ORDER BY、LIMIT、OFFSET、 FETCH以及FOR锁定子句可以用于 TABLE。不能使用WHERE子句和任何形式 的聚集。

示例

把表films与表 distributors连接：

```
SELECT f.title, f.did, d.name, f.date_prod, f.kind

FROM distributors d, films f

WHERE f.did = d.did

title \| did \| name \| date_prod \| kind

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\--

The Third Man \| 101 \| British Lion \| 1949-12-23 \| Drama

The African Queen \| 101 \| British Lion \| 1951-08-11 \| Romantic

\...
```

要对所有电影的len列求和并且用 kind对结果分组：

```
SELECT kind, sum(len) AS total FROM films GROUP BY kind;

kind \| total

\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\--

Action \| 07:34

Comedy \| 02:58

Drama \| 14:28

Musical \| 06:42

Romantic \| 04:38
```

要对所有电影的len列求和、对结果按照 kind分组并且显示总长小于 5 小时的分组：

```
SELECT kind, sum(len) AS total

FROM films

GROUP BY kind

HAVING sum(len) \< interval \'5 hours\';

kind \| total

\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\--

Comedy \| 02:58

Romantic \| 04:38
```

下面两个例子都是根据第二列（name）的内容来排序结果：

```
SELECT \* FROM distributors ORDER BY name;

SELECT \* FROM distributors ORDER BY 2;

did \| name

\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

109 \| 20th Century Fox

110 \| Bavaria Atelier

101 \| British Lion

107 \| Columbia

102 \| Jean Luc Godard

113 \| Luso films

104 \| Mosfilm

103 \| Paramount

106 \| Toho

105 \| United Artists

111 \| Walt Disney

112 \| Warner Bros.

108 \| Westward
```

接下来的例子展示了如何得到表distributors和 actors的并集，把结果限制为那些在每个表中以 字母 W 开始的行。只想要可区分的行，因此省略了关键词 ALL。

```
distributors: actors:

did \| name id \| name

\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-- \-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

108 \| Westward 1 \| Woody Allen

111 \| Walt Disney 2 \| Warren Beatty

112 \| Warner Bros. 3 \| Walter Matthau

\... \...

SELECT distributors.name

FROM distributors

WHERE distributors.name LIKE \'W%\'

UNION

SELECT actors.name

FROM actors

WHERE actors.name LIKE \'W%\';

name

Walt Disney

Walter Matthau

Warner Bros.

Warren Beatty

Westward

Woody Allen
```

这个例子展示了如何在FROM子句中使用函数， 分别使用和不使用列定义列表：

```
CREATE FUNCTION distributors(int) RETURNS SETOF distributors AS \$\$

SELECT \* FROM distributors WHERE did = \$1;

\$\$ LANGUAGE SQL;

SELECT \* FROM distributors(111);

did \| name

\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\--

111 \| Walt Disney

CREATE FUNCTION distributors_2(int) RETURNS SETOF record AS \$\$

SELECT \* FROM distributors WHERE did = \$1;

\$\$ LANGUAGE SQL;

SELECT \* FROM distributors_2(111) AS (f1 int, f2 text);

f1 \| f2

\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\--

111 \| Walt Disney
```

这里是带有增加的序数列的函数的例子：

```
SELECT \* FROM unnest(ARRAY\[\'a\',\'b\',\'c\',\'d\',\'e\',\'f\'\]) WITH ORDINALITY;

unnest \| ordinality

\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\--

a \| 1

b \| 2

c \| 3

d \| 4

e \| 5

f \| 6

(6 rows)
```

这个例子展示了如何使用简单的WITH子句：

```
WITH t AS (

SELECT random() as x FROM generate_series(1, 3)

)

SELECT \* FROM t

UNION ALL

SELECT \* FROM t

x

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

0.534150459803641

0.520092216785997

0.0735620250925422

0.534150459803641

0.520092216785997

0.0735620250925422
```

注意该WITH查询只被计算一次，这样我们得到的两个集合具有相同的三个随机值。

这个例子使用WITH RECURSIVE从一个只显示直接下属的表中寻找雇员 Mary 的所有下属（直接的或者间接的）以及他们的间接层数：

```
WITH RECURSIVE employee_recursive(distance, employee_name, manager_name) AS (

SELECT 1, employee_name, manager_name

FROM employee

WHERE manager_name = \'Mary\'

UNION ALL

SELECT er.distance + 1, e.employee_name, e.manager_name

FROM employee_recursive er, employee e

WHERE er.employee_name = e.manager_name

)

SELECT distance, employee_name FROM employee_recursive;
```

注意这种递归查询的典型形式：一个初始条件，后面跟着 UNION，然后是查询的递归部分。

要确保查询的递归部分最终将不返回任何行，否则该查询将无限循环。

这个例子使用LATERAL为manufacturers 表的每一行应用一个集合返回函数get\_product\_names()：

```
SELECT m.name AS mname, pname

FROM manufacturers m, LATERAL get_product_names(m.id) pname;
```

当前没有任何产品的制造商不会出现在结果中，因为这是一个内连接。 如果我们希望把这类制造商的名称包括在结果中，我们可以：

```
SELECT m.name AS mname, pname

FROM manufacturers m LEFT JOIN LATERAL get_product_names(m.id) pname ON true;
```

兼容性

当然，SELECT语句是兼容 SQL 标准的。 但是也有一些扩展和缺失的特性。

- 省略的FROM子句

瀚高数据库允许我们省略 FROM子句。一种简单的使用是计算简单表达式 的结果：

```
SELECT 2+2;

?column?

\-\-\-\-\-\-\-\-\--

4
```

某些其他SQL数据库需要引入一个假的 单行表放在该SELECT的 FROM子句中才能做到这一点。

注意，如果没有指定一个FROM子句，该查询就不能引用任何数据库表。例如，下面的查询是非法的：

SELECT distributors.\* WHERE distributors.name = 'Westward';

- 空SELECT列表

SELECT之后的输出表达式列表可以为空，这会产生一个零列的结果表。对 SQL 标准来说这不是合法的 语法。瀚高数据库允许它是为了与允许零列表保持一致。不过在使用DISTINCT时不允许空列表。

- 省略AS关键词

在 SQL 标准中，只要新列名是一个合法的列名（就是说与任何保留关键词不同）， 就可以省略输出列名之前的可选关键词AS。 瀚高数据库要稍微严格些：只要新列名匹配 任何关键词（保留或者非保留）就需要AS。推荐的习惯是使用 AS或者带双引号的输出列名来防止与未来增加的关键词可能的冲突。

在FROM项中，标准和 瀚高数据库都允许省略非保留 关键词别名之前的AS。但是由于语法的歧义，这无法 用于输出列名。

- ONLY和继承

在书写ONLY时，SQL 标准要求在表名周围加上圆括号，例如 SELECT \* FROM ONLY (tab1), ONLY (tab2) WHERE...。瀚高数据库认为这些圆括号是可选的。

瀚高数据库允许写一个拖尾的\*来 显式指定包括子表的非-ONLY行为。而标准则不允许这样。

（这些点同等地适用于所有支持ONLY选项的 SQL 命令）。

- TABLESAMPLE子句限制

当前只在常规表和物化视图上接受TABLESAMPLE子句。 根据 SQL 标准，应该可以把它应用于任何FROM项。

- FROM中的函数调用

瀚高数据库允许一个函数调用被直接写作 FROM列表的一个成员。在 SQL 标准中，有必要把这样一个函数 调用包裹在一个子-SELECT中。也就是说，语法 FROM func(...) alias 近似等价于 FROM LATERAL (SELECT func(...)) alias。 注意该LATERAL被认为是隐式的，这是因为标准对于 FROM中的一个UNNEST()项要求 LATERAL语义。瀚高数据库会把 UNNEST()和其他集合返回函数同样对待。

- GROUP BY和ORDER BY可用的名字空间

在 SQL-92 标准中，一个ORDER BY子句只能使用输出 列名或者序号，而一个GROUP BY子句只能使用基于输 入列名的表达式。瀚高数据库扩展了 这两种子句以允许它们使用其他的选择（但如果有歧义时还是使用标准的 解释）。瀚高数据库也允许两种子句 指定任意表达式。

注意出现在一个表达式中的名称将总是被当做输入列名而 不是输出列名。

SQL:1999 及其后的标准使用了一种略微不同的定义，它并不完全向后兼容 SQL-92。不过，在大部分的情况下， 瀚高数据库会以与 SQL:1999 相同的 方式解释ORDER BY或GROUP BY表达式。

- 函数依赖

只有当一个表的主键被包括在GROUP BY列表中时， 瀚高数据库才识别函数依赖（允许从GROUP BY中省略列）。SQL 标准指定了应该要识别 的额外情况。

- LIMIT和OFFSET

LIMIT和OFFSET子句是 瀚高数据库-特有的语法，在 MySQL也被使用。SQL:2008 标准已经 引入了具有相同功能的子句OFFSET... FETCH {FIRST|NEXT}...（如上文 LIMIT 子句中所示）。这种语法 也被IBM DB2使用（ Oracle编写的应用常常使用自动生成的 rownum列来实现这些子句的效果，这在 瀚高数据库中是没有的）。

- FOR NO KEY UPDATE、FOR UPDATE、FOR SHARE、FOR KEY SHARE

尽管 SQL 标准中出现了FOR UPDATE，但标准只允许它作为 DECLARE CURSOR的一个选项。瀚高数据库允许它出现在任何 SELECT查询以及子-SELECT中，但这是 一种扩展。FOR NO KEY UPDATE、FOR SHARE 以及FOR KEY SHARE变体以及NOWAIT 和SKIP LOCKED选项没有在标准中出现。

- WITH中的数据修改语句

瀚高数据库允许把INSERT、 UPDATE以及DELETE用作WITH 查询。这在 SQL 标准中是找不到的。

- 非标准子句

DISTINCT ON (... )是 SQL 标准的扩展。

ROWS FROM(... )是 SQL 标准的扩展。

WITH的MATERIALIZED 和 NOT MATERIALIZED 选项是SQL标准的扩展。

## SELECT INTO

— 从一个查询的结果定义一个新表

大纲

```
\[ WITH \[ RECURSIVE \] with_query \[, \...\] \]

SELECT \[ ALL \| DISTINCT \[ ON ( expression \[, \...\] ) \] \]

\* \| expression \[ \[ AS \] output_name \] \[, \...\]

INTO \[ TEMPORARY \| TEMP \| UNLOGGED \] \[ TABLE \] new_table

\[ FROM from_item \[, \...\] \]

\[ WHERE condition \]

\[ GROUP BY expression \[, \...\] \]

\[ HAVING condition \[, \...\] \]

\[ WINDOW window_name AS ( window_definition ) \[, \...\] \]

\[ { UNION \| INTERSECT \| EXCEPT } \[ ALL \| DISTINCT \] select \]

\[ ORDER BY expression \[ ASC \| DESC \| USING operator \] \[ NULLS { FIRST \|

LAST } \] \[, \...\] \]

\[ LIMIT { count \| ALL } \]

\[ OFFSET start \[ ROW \| ROWS \] \]

\[ FETCH { FIRST \| NEXT } \[ count \] { ROW \| ROWS } ONLY \]

\[ FOR { UPDATE \| SHARE } \[ OF table_name \[, \...\] \] \[ NOWAIT \] \[\...\] \]
```

描述

SELECT INTO创建一个新表并且用一个查询 计算得到的数据填充它。这些数据不会像普通的SELECT那样被返回给客户端。新表的列具有 和SELECT的输出列相关的名称和数据类型。

参数

TEMPORARY or TEMP

如果被指定，该表被创建为一个临时表。详见 CREATE TABLE。

UNLOGGED

如果被指定，该表被创建为一个不做日志的表。详见 CREATE TABLE。

new\_table

要创建的表的名字（可以是模式限定的）。

所有其他参数在SELECT中有详细描述。

注解

CREATE TABLE AS在功能上与 SELECT INTO相似。CREATE TABLE AS 是被推荐的语法，因为这种形式的SELECT INTO在ECPG 或PL/pgSQL中不可用，因为它们对 INTO子句的解释不同。此外， CREATE TABLE AS提供的功能是 SELECT INTO的超集。

与CREATE TABLE AS相比，SELECT INTO 不允许指定属性，就像带有USING method的表访问方法或者带有TABLESPACE tablespace\_name的表的表空间。 如果必要，使用CREATE TABLE AS。因此，为新表选择默认表访问方法。详细信息请参阅default\_table\_access\_method。

示例

创建一个只由来自films的最近项构成的 新表films\_recent：

```
SELECT \* INTO films_recent FROM films WHERE date_prod \>= \'2002-01-01\';
```

兼容性

SQL 标准使用SELECT INTO表示把值选择 到一个宿主程序的标量变量中，而不是创建一个新表。这实际上就是 ECPG（见第 35 章）和 PL/pgSQL（见第 42 章） 中的用法。 瀚高数据库使用 SELECT INTO的来表示表创建是有历史原因的。 最好在新代码中使用CREATE TABLE AS。

另见

CREATE TABLE AS

## SET

— 更改一个运行时参数

大纲

```
SET \[ SESSION \| LOCAL \] configuration_parameter { TO \| = } { value \| \'value\' \|

DEFAULT }

SET \[ SESSION \| LOCAL \] TIME ZONE { timezone \| LOCAL \| DEFAULT }
```

描述

SET命令更改运行时配置参数。很多服务器配置中列出的参数可以用 SET即时更改（但是有些需要超级用户 特权才能更改，并且还有一些在服务器或者会话启动之后不能被更改）。SET只影响当前会话所使用的值。

如果在一个事务内发出SET （或者等效的SET SESSION）而该事务后来 中止，在该事务被回滚时SET命令的效果会 消失。一旦所在的事务被提交，这些效果将会持续到会话结束（除非被另 一个SET所覆盖）。

SET LOCAL的效果只持续到当前事务结束， 不管事务是否被提交。一种特殊情况是在一个事务内 SET后面跟着 SET LOCAL： SET LOCAL值将会在该事务结束前一直可见， 但是之后（如果该事务被提交）SET值将会生效。

SET或SET LOCAL 的效果也会因为回滚到早于它们的保存点而消失。

如果在一个函数内使用SET LOCAL并且该函数 还有对同一变量的SET选项（见CREATE FUNCTION），在函数退出时 SET LOCAL命令的效果会消失。也就是说，该函数被调用时的值会被恢复。这允许用 SET LOCAL在函数内动态地或者重复地更改 一个参数，同时仍然能便利地使用SET选项来保存以及恢复调用 者的值。不过，一个常规的SET命令会覆盖它所在的任何函 数的SET选项，除非回滚，它的效果将一直保持。

参数

SESSION

指定该命令对当前会话有效（这是默认值）。

LOCAL

指定该命令只对当前事务有效。在COMMIT或者 ROLLBACK之后，会话级别的设置会再次生效。 在事务块外部发出这个参数会发出一个警告并且不会有效果。

configuration\_parameter

一个可设置运行时参数的名称。可用的参数被记录在 第 19 章和下文中。

value

参数的新值。根据特定的参数，值可以被指定为字符串常量、标识符、 数字或者以上构成的逗号分隔列表。写DEFAULT 可以指定把该参数重置成它的默认值（也就是说在当前会话中还没有 执行SET命令时它具有的值）。

除了服务器配置中记录的配置参数， 还有一些参数只能用SET命令设置 或者具有特殊的语法：

SCHEMA

SET SCHEMA 'value'是 SET search\_path TO value的一个别名。 使用这种语法只能指定一个模式。

NAMES

SET NAMES value是 SET client\_encoding TO value的一个别名。

SEED

为随机数生成器（函数random）设置 一个内部种子。允许的值是 -1 和 1 之间的浮点数，它会被乘上 231-1。

也可以通过调用函数setseed来设置种子：

SELECT setseed(value);

TIME ZONE

SET TIME ZONE value是 SET timezone TO value的一个别 名。语法SET TIME ZONE允许用于时区指定的特 殊语法。这里是合法值的例子：

'PST8PDT'

加州伯克利的时区。

'Europe/Rome'

意大利的时区。

\-7

UTC 以西 7 小时的时区（等效于 PDT）。正值则是 UTC 以东。

INTERVAL '-08:00' HOUR TO MINUTE

UTC 以西 8 小时的时区（等效于 PST）。

LOCAL

DEFAULT

把时区设置为你的本地时区（也就是说服务器的timezone默认值）。

以数字或区间给出的时区设置在内部被翻译成 POSIX 时区语法。例如，在SET TIME ZONE -7之后， SHOW TIME ZONE将会报告 <-07>+07。

注解

函数set\_config提供了等效的功能。此外，可以更新 pg\_settings 系统视图来执行与SET等效的工作。

示例

设置模式搜索路径：

```
SET search_path TO my_schema, public;
```

把日期风格设置为传统 POSTGRES的 “日在月之前”的输入习惯：

```
SET datestyle TO postgres, dmy;
```

设置时区为加州伯克利：

```
SET TIME ZONE \'PST8PDT\';
```

设置时区为意大利：

```
SET TIME ZONE \'Europe/Rome\';
```

兼容性

SET TIME ZONE扩展了 SQL 标准定义的语法。标准 只允许数字的时区偏移量而 瀚高数据库允许更灵活的时区说明。 所有其他SET特性都是瀚高数据库扩展。

另见

RESET, SHOW

## SET CONSTRAINTS

— 为当前事务设置约束检查时机

大纲

```
SET CONSTRAINTS { ALL \| name \[, \...\] } { DEFERRED \| IMMEDIATE }
```

描述

SET CONSTRAINTS设置当前事务内约束检查 的行为。IMMEDIATE约束在每个语句结束时被检查。 DEFERRED约束直到事务提交时才被检查。每个约束都有 自己的IMMEDIATE或DEFERRED模式。

在创建时，一个约束会被给定三种特性之一：DEFERRABLE INITIALLY DEFERRED、 DEFERRABLE INITIALLY IMMEDIATE或者 NOT DEFERRABLE。第三类总是 IMMEDIATE并且不会受到 SET CONSTRAINTS命令的影响。前两类在每个 事务开始时都处于指定的模式，但是它们的行为可以在一个事务内用 SET CONSTRAINTS更改。

带有一个约束名称列表的SET CONSTRAINTS 只更改那些约束（都必须是可延迟的）的模式。一个约束名称都可以是 模式限定的。如果没有指定模式名称，则当前的模式搜索路径将被用来寻找 第一个匹配的名称。SET CONSTRAINTS ALL 更改所有可延迟约束的模式。

当SET CONSTRAINTS把一个约束的模式从 DEFERRED改成IMMEDIATE时， 新模式会有追溯效果：任何还没有解决的数据修改（本来会在事务结束时 被检查）会转而在SET CONSTRAINTS命令 的执行期间被检查。如果任何这种约束被违背， SET CONSTRAINTS将会失败（并且不会改 变该约束模式）。这样，SET CONSTRAINTS可以被用来在一个事务中的特定点强制进 行约束检查。

当前，只有UNIQUE、PRIMARY KEY、 REFERENCES（外键）以及EXCLUDE 约束受到这个设置的影响。 NOT NULL以及CHECK约束总是在一行 被插入或修改时立即检查（不是在语句结束时）。没有被声明为DEFERRABLE的唯一和排除约束也会被 立刻检查。

被声明为”约束触发器”的触发器的引发也受到这个设置的控制 — 它们会在相关约束被检查的同时被引发。

注解

因为瀚高数据库并不要求约束名称在模式内唯一（但是在表内要求唯一），可能有多于一个约束匹配指定的约束名称。在这种情况下SET CONSTRAINTS将会在所有的匹配上操作。 对于一个非模式限定的名称，一旦在搜索路径中的某个模式中发现一个或者多个匹配，路径中后面的模式将不会被搜索。

这个命令只修改当前事务内约束的行为。在事务块外部发出这个命令会产生一个 警告并且也不会有任何效果。

兼容性

这个命令符合 SQL 标准中定义的行为，但有一点限制：在 瀚高数据库中，它不会应用在 NOT NULL和CHECK约束上。还有， 瀚高数据库会立刻检查非可延迟的 唯一约束，而不是按照标准建议的在语句结束时检查。

## SET ROLE

— 设置当前会话的当前用户标识符

大纲

```
SET \[ SESSION \| LOCAL \] ROLE role_name

SET \[ SESSION \| LOCAL \] ROLE NONE

RESET ROLE
```

描述

这个命令把当前 SQL 会话的当前用户标识符设置为 role\_name。 角色名可以写成一个标识符或者一个字符串。在 SET ROLE之后，对 SQL 命令的权限检查时就 好像该角色就是原先登录的角色一样。

当前会话用户必须是指定的 角色role\_name 的一个成员（如果会话用户是一个超级用户，则可以选择任何角色）。

SESSION和LOCAL修饰符发挥的作用和 常规的SET命令一样。

NONE和RESET形式把当前用户标识符 重置为当前会话用户标识符。这些形式可以由任何用户执行。

注解

使用这个命令可以增加特权或者限制特权。如果会话用户角色具有 INHERIT属性，则它会自动具有它能 SET ROLE到的所有角色的全部特权。在这种情况下 SET ROLE实际会删除所有直接分配给会话用户的特 权以及分配给会话用户作为其成员的其他角色的特权，只留下所提及 角色可用的特权。换句话说，如果会话用户没有 NOINHERIT属性，SET ROLE会删除 直接分配给会话用户的特权而得到所提及角色可用的特权。

特别地，当一个超级用户选择SET ROLE到一个非 超级用户角色时，它们会丢失其超级用户特权。

SET ROLE的效果堪比 SET SESSION AUTHORIZATION，但是涉及的特权检查 完全不同。还有，SET SESSION AUTHORIZATION决定 后来的SET ROLE命令可以使用哪些角色， 不过用 SET ROLE更改角色并不会改变后续 SET ROLE能够使用的角色集。

SET ROLE不会处理角色的ALTER ROLE 设置指定的会话变量。这只在登录期间发生。

SET ROLE不能在一个 SECURITY DEFINER函数中使用。

示例

```
SELECT SESSION_USER, CURRENT_USER;

session_user \| current_user

\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\--

peter \| peter

SET ROLE \'paul\';

SELECT SESSION_USER, CURRENT_USER;

session_user \| current_user

\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\--

peter \| paul
```

兼容性

瀚高数据库允许标识符 语法（"rolename"），而 SQL 标准要求 角色名被写成字符串。SQL不允许在事务中使用这个命令，而 瀚高数据库并不做此限 制，因为并没有原因需要这样做。和RESET语法 一样，SESSION和 LOCAL修饰符是一种瀚高数据库扩展。

另见

SET SESSION AUTHORIZATION

## SET SESSION AUTHORIZATION

— 设置当前会话的会话用户标识符和当前用户标识符

大纲

```
SET \[ SESSION \| LOCAL \] SESSION AUTHORIZATION user_name

SET \[ SESSION \| LOCAL \] SESSION AUTHORIZATION DEFAULT

RESET SESSION AUTHORIZATION
```

描述

这个命令把当前 SQL 会话的会话用户标识符和当前用户标识符设置为 user\_name。 用户名可以被写成一个标识符或者一个字符串。例如，可以使用这个 命令临时成为一个无特权用户并且稍后切换回来成为一个超级用户。

会话用户标识符初始时被设置为客户端提供的（可能已认证的）用户名。 当前用户标识符通常等于会话用户标识符，但是可能在 SECURITY DEFINER函数和类似机制的环境中临时更改。 也可以用SET ROLE更改它。当前用户标识符与 权限检查相关。

会话用户标识符只能在初始会话用户 已认证用户具有超级用户特权时被更改。 否则，只有该命令指定已认证用户名时才会被接受。

SESSION和LOCAL修饰符发挥的作用和常规 SET命令一样。

DEFAULT和RESET形式把会话用户标识符和 当前用户标识符重置为初始的已认证用户名。这些形式可以由任何用户执行。

注解

SET SESSION AUTHORIZATION不能在一个 SECURITY DEFINER函数中使用。

示例

```
SELECT SESSION_USER, CURRENT_USER;

session_user \| current_user

\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\--

peter \| peter

SET SESSION AUTHORIZATION \'paul\';

SELECT SESSION_USER, CURRENT_USER;

session_user \| current_user

\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\-\-\-\-\-\--

paul \| paul
```

兼容性

SQL 标准允许一些其他表达式出现在文本 user\_name的位置上，但是实际上这些 选项并不重要。瀚高数据库允许标 识符语法（"username"），而 SQL 标准不允许。 SQL 不允许在事务中使用这个命令，而 瀚高数据库并不做此限 制，因为并没有原因需要这样做。和RESET语法一样，SESSION和 LOCAL修饰符是一种瀚高数据库扩展。

标准把执行这个命令所需的特权留给实现定义。

另见

SET ROLE

## SET TRANSACTION

— 设置当前事务的特性

大纲

```
SET TRANSACTION transaction_mode \[, \...\]

SET TRANSACTION SNAPSHOT snapshot_id

SET SESSION CHARACTERISTICS AS TRANSACTION transaction_mode \[, \...\]

其中 transaction_mode 是下列之一：

ISOLATION LEVEL { SERIALIZABLE \| REPEATABLE READ \| READ COMMITTED \| READ

UNCOMMITTED }

READ WRITE \| READ ONLY

\[ NOT \] DEFERRABLE
```

描述

SET TRANSACTION命令设置当前 会话的特性。SET SESSION CHARACTERISTICS设置一个会话后续事务的默认 事务特性。在个体事务中可以用 SET TRANSACTION覆盖这些默认值。

可用的事务特性是事务隔离级别、事务访问模式（读/写或只读）以及 可延迟模式。此外，可以选择一个快照，不过只能用于当前事务而不能 作为会话默认值。

一个事务的隔离级别决定当其他事务并行运行时该事务能看见什么数据：

READ COMMITTED

一个语句只能看到在它开始前提交的行。这是默认值。

REPEATABLE READ

当前事务的所有语句只能看到这个事务中执行的第一个查询或者 数据修改语句之前提交的行。

SERIALIZABLE

当前事务的所有语句只能看到这个事务中执行的第一个查询或者 数据修改语句之前提交的行。如果并发的可序列化事务间的读写 模式可能导致一种那些事务串行（一次一个）执行时不可能出现 的情况，其中之一将会被回滚并且得到一个

serialization\_failure错误。

SQL 标准定义了一种额外的级别：READ UNCOMMITTED。在 瀚高数据库中READ UNCOMMITTED被视作 READ COMMITTED。

一个事务执行了第一个查询或者数据修改语句（SELECT、INSERT、DELETE、UPDATE、FETCH或 COPY）之后就无法更改事务隔离级别。

事务的访问模式决定该事务是否为读/写或者只读。读/写是默认值。 当一个事务为只读时，如果 SQL 命令 INSERT、UPDATE、 DELETE和COPY FROM 要写的表不是一个临时表，则它们不被允许。不允许 CREATE、ALTER以及 DROP命令。不允许COMMENT、 GRANT、REVOKE、 TRUNCATE。如果EXPLAIN ANALYZE 和EXECUTE要执行的命令是上述命令之一， 则它们也不被允许。这是一种高层的只读概念，它不能阻止所有对 磁盘的写入。

只有事务也是SERIALIZABLE以及 READ ONLY时，DEFERRABLE 事务属性才会有效。当一个事务的所有这三个属性都被选择时，该事务在 第一次获取其快照时可能会阻塞，在那之后它运行时就不会有 SERIALIZABLE事务的开销并且不会有任何牺牲或者 被一次序列化失败取消的风险。这种模式很适合于长时间运行的报表或者 备份。

SET TRANSACTION SNAPSHOT命令允许新的事务 使用与一个现有事务相同的快照运行。已经存在的事务必须已经把它的快照用pg\_export\_snapshot函数导出。该函数会返回一个快照标识符，SET TRANSACTION SNAPSHOT需要被给定一个快照标识符来指定要导入的快照。在这个命令中该标识符必须被写成一个字符串，例如 '000003A1-1'。 SET TRANSACTION SNAPSHOT只能在一个事务的 开始执行，并且要在该事务的第一个查询或者数据修改语句（ SELECT、 INSERT、DELETE、 UPDATE、FETCH或 COPY）之前执行。此外，该事务必须已经被设置 为SERIALIZABLE或者 REPEATABLE READ隔离级别（否则，该快照将被立刻抛弃， 因为READ COMMITTED模式会为每一个命令取一个新快照）。 如果导入事务使用了SERIALIZABLE隔离级别，那么导入快照 的事务必须也使用该隔离级别。还有，一个非只读可序列化事务不能导入来自只读 事务的快照。

注解

如果执行SET TRANSACTION之前没有 START TRANSACTION或者 BEGIN，它会发出一个警告并且不会有任何效果。

可以通过在BEGIN或者 START TRANSACTION中指定想要的transaction\_modes来省掉 SET TRANSACTION。但是在 SET TRANSACTION SNAPSHOT中该选项不可用。

会话默认的事务模式也可以通过设置配置参数default\_transaction\_isolation、default\_transaction\_read\_only和 default\_transaction\_deferrable来设置（实际上 SET SESSION CHARACTERISTICS只是用 SET设置这些变量的等效体）。这意味着可以通过配置文件、 ALTER DATABASE等方式设置默认值。

示例

要用一个已经存在的事务的同一快照开始一个新事务，首先要从该现有 事务导出快照。这将会返回快照标识符，例如：

```
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

SELECT pg_export_snapshot();

pg_export_snapshot

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

00000003-0000001B-1

(1 row)
```

然后在一个新开始的事务的开头把该快照标识符用在一个 SET TRANSACTION SNAPSHOT命令中：

```
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;

SET TRANSACTION SNAPSHOT \'00000003-0000001B-1\';
```

兼容性

SQL标准中定义了这些命令，不过 DEFERRABLE事务模式和 SET TRANSACTION SNAPSHOT形式除外，这两者是瀚高数据库扩展。

SERIALIZABLE是标准中默认的事务隔离级别。在 瀚高数据库中默认值是普通的 READ COMMITTED，但是你可以按上述的方式更改。

在 SQL 标准中，可以用这些命令设置一个其他的事务特性：诊断区域 的尺寸。这个概念与嵌入式 SQL 有关，并且因此没有在 瀚高数据库服务器中实现。

SQL 标准要求连续的transaction\_modes之间有逗号， 但是出于历史原因 瀚高数据库允许省略逗号。

## SHOW

— 显示一个运行时参数的值

大纲

```
SHOW name

SHOW ALL
```

描述

SHOW将显示运行时参数的当前设置。 这些变量可以使用SET语句、编辑 postgresql.conf配置参数、通过PGOPTIONS环境变量（使用 libpq或者基于libpq的应用时） 或者启动postgres服务器时通过命令行 标志设置。

参数

name

一个运行时参数的名称。此外，有一些可以

显示但不能设置的参数：

SERVER\_VERSION

显示服务器的版本号。

SERVER\_ENCODING

显示服务器端的字符集编码。当前，这个参数可以被显示 但不能被设置，因为该设置是在数据库创建时决定的。

LC\_COLLATE

显示数据库的排序规则（文本序）的区域设置。当前， 这个参数可以被显示但不能被设置，因为该设置是在 数据库创建时决定的。

LC\_CTYPE

显示数据库的字符分类的区域设置。当前， 这个参数可以被显示但不能被设置，因为该设置 是在数据库创建时决定的。

IS\_SUPERUSER

如果当前角色具有超级用户特权则为真。

ALL

显示所有配置参数的值，并带有描述。

示例

显示参数DateStyle的当前设置：

```
SHOW DateStyle;

DateStyle

\-\-\-\-\-\-\-\-\-\--

ISO, MDY

(1 row)
```

显示参数geqo的当前设置：

```
SHOW geqo;

geqo

\-\-\-\-\--

on

(1 row)
```

显示所有设置：

```
SHOW ALL;

name \| setting \| description

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--+\-\-\-\-\-\-\-\--

+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

allow_system_table_mods \| off \| Allows modifications of the structure

of \...

.

.

.

xmloption \| content \| Sets whether XML data in implicit

parsing \...

zero_damaged_pages \| off \| Continues processing past damaged page

headers.

(196 rows)
```

兼容性

SHOW命令是一种瀚高数据库扩展。

另见

SET, RESET

## START TRANSACTION

— 开始一个事务块

大纲

```
START TRANSACTION \[ transaction_mode \[, \...\] \]
```

其中 transaction\_mode 是下列之一：

```
ISOLATION LEVEL { SERIALIZABLE \| REPEATABLE READ \| READ COMMITTED \| READ UNCOMMITTED }

READ WRITE \| READ ONLY

\[ NOT \] DEFERRABLE
```

描述

这个命令开始一个新的事务块。如果指定了隔离级别、读写模式 或者可延迟模式，新的事务将会具有这些特性，就像执行了 SET TRANSACTION一样。这和 BEGIN命令一样。

参数

这些参数对于这个语句的含义可参考 SET TRANSACTION。

兼容性

在标准中，没有必要发出START TRANSACTION 来开始一个事务块：任何 SQL 命令会隐式地开始一个块。 瀚高数据库的行为可以被视作 在每个命令之后隐式地发出一个没有跟随在 START TRANSACTION（ 或者BEGIN）之后的 COMMIT并且因此通常被称作 “自动提交”。为了方便，其他关系型数据库系统也可能会 提供自动提交特性。

DEFERRABLE transaction\_mode 是一种瀚高数据库语言扩展。

SQL标准要求在连续的transaction\_modes之间有逗号， 但是由于历史原因瀚高数据库允许省略逗号。

另见

BEGIN, COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION

## TRUNCATE

— 清空一个表或者一组表

大纲

```
TRUNCATE \[ TABLE \] \[ ONLY \] name \[ \* \] \[, \... \]

\[ RESTART IDENTITY \| CONTINUE IDENTITY \] \[ CASCADE \| RESTRICT \]
```

描述

TRUNCATE可以从一组表中快速地移除所有行。 它具有和在每个表上执行无条件DELETE相同的效果，不过它会更快，因为它没有实际扫描表。此外，它会立刻回收磁盘空间， 而不是要求一个后续的VACUUM操作。在大表上 它最有用。

参数

name

要截断的表的名字（可以是模式限定的）。如果在表名前指定了ONLY，则只会截断该表。如果没有指定ONLY， 该表及其所有后代表（如果有）都会被截断。可选地，可以在表名后指定 \*来显式地包括后代表。

RESTART IDENTITY

自动重新开始被截断表的列所拥有的序列。

CONTINUE IDENTITY

不更改序列值。这是默认值。

CASCADE

自动截断所有对任一所提及表有外键引用的表以及任何由于CASCADE被加入到组中的表。

RESTRICT

如果任一表上具有来自命令中没有列出的表的外键引用，则拒绝截断。这是默认值。

注解

要截断一个表，你必须具有其上的TRUNCATE特权。

TRUNCATE在要操作的表上要求一个 ACCESS EXCLUSIVE锁，这会阻塞所有其他在该表上的并发操作。当指定RESTART IDENTITY时，任何需要被重新开始的序列也会被排他地锁住。如果要求表上的并发访问，那么 应该使用DELETE命令。

TRUNCATE不能被用在被其他表外键引用的表上， 除非那些表也在同一个命令中被阶段。这些情况中的可行性检查将会 要求表扫描，并且重点不是为了做扫描。CASCADE 选项可以被用来自动地包括所有依赖表 — 但使用它时要非常小心，否则你可能丢失数据！ 特别注意的是，当要被截断的表是一个分区时，兄弟节点分区不会受到影响，但是所有的引用表都发生级联，他们的分区也没有区别。

TRUNCATE将不会引发表上可能存在的任何ON DELETE触发器。但是它将会引发 ON TRUNCATE触发器。如果在这些表的任意一个上定义了ON TRUNCATE触发器，那么所有的BEFORE TRUNCATE触发器将在任何截断发生之前被引发，而所有AFTER TRUNCATE触发器将在最后 一次截断完成并且所有序列被重置之后引发。触发器将以表被处理的顺序被引发（首先是那些被列在命令中的，然后是由于级联被加入的）。

TRUNCATE不是 MVCC 安全的。截断之后， 如果并发事务使用的是一个在截断发生前取得的快照， 表将对这些并发事务呈现为空。

从表中数据的角度来说，TRUNCATE是事务安全的： 如果所在的事务没有提交，阶段将会被安全地回滚。

在指定了RESTART IDENTITY时，隐含的 ALTER SEQUENCE RESTART操作也会被事务性地完成。也就是说，如果所在事务没有提交，它们也将被回滚。这和 ALTER SEQUENCE RESTART的通常行为不同。注意如果 事务回滚前在被重启序列上还做了额外的序列操作，这些操作在序列上的效果 也将被回滚，但是它们在currval()上的效果不会被回滚。也就 是说，在事务之后，currval()将继续反映在失败事务内得到的 最后一个序列值，即使序列本身可能已经不再与此一致。这和失败事务之后 currval()的通常行为类似。

TRUNCATE当前不支持外部表。 这表示如果一个指定的表具有任何外部的后代表，这个命令将会失败。

示例

截断表bigtable和 fattable：

```
TRUNCATE bigtable, fattable;
```

做同样的事情，并且还重置任何相关联的序列发生器：

```
TRUNCATE bigtable, fattable RESTART IDENTITY;
```

截断表othertable，并且级联地截断任何通过 外键约束引用othertable的表：

```
TRUNCATE othertable CASCADE;
```

兼容性

SQL:2008 标准包括了一个TRUNCATE命令， 语法是TRUNCATE TABLE tablename。子句CONTINUE IDENTITY/RESTART IDENTITY 也出现在了该标准中，但是含义有些不同。这个命令的一些并发行为被标准 留给实现来定义，因此如果必要应该考虑上述注解并且与其他实现进行比较。

参见

DELETE

## UNLISTEN

— 停止监听一个通知

大纲

```
UNLISTEN { channel \| \* }
```

描述

UNLISTEN被用来移除一个已经存在的对 NOTIFY事件的注册。 UNLISTEN取消任何已经存在的把当前 瀚高数据库会话作为名为 channel的通知 频道的监听者的注册。特殊的通配符\*取消当前会话 的所有监听者注册。

NOTIFY包含有关LISTEN 和NOTIFY使用的更深入讨论。

参数

channel

一个通知频道的名称（任何标识符）。

\*

所有用于这个会话的当前监听注册都会被清除。

注解

你可以 unlisten 你没有监听的东西，不会出现警告或者错误。

在每一个会话末尾，会自动执行UNLISTEN \*。

一个已经执行了UNLISTEN的事务不能为 两阶段提交做准备。

示例

做一次注册：

```
LISTEN virtual;

NOTIFY virtual;
```

Asynchronous notification "virtual" received from server process with PID 8448.

一旦执行了UNLISTEN，进一步的NOTIFY 消息将被忽略：

```
UNLISTEN virtual;

NOTIFY virtual;

\-- no NOTIFY event is received
```

兼容性

SQL 标准中没有UNLISTEN命令。

另见

LISTEN, NOTIFY

## UPDATE

— 更新一个表的行

大纲

```
\[ WITH \[ RECURSIVE \] with_query \[, \...\] \]

UPDATE \[ ONLY \] table_name \[ \* \] \[ \[ AS \] alias \]

SET { column_name = { expression \| DEFAULT } \|

( column_name \[, \...\] ) = \[ ROW \] ( { expression \| DEFAULT } \[, \...\] )

\|

( column_name \[, \...\] ) = ( sub-SELECT )

} \[, \...\]

\[ FROM from_list \]

\[ WHERE condition \| WHERE CURRENT OF cursor_name \]

\[ RETURNING \* \| output_expression \[ \[ AS \] output_name \] \[, \...\] \]
```

描述

UPDATE更改满足条件的所有行中指定列 的值。只有要被修改的列需要在SET子句中提及， 没有被显式修改的列保持它们之前的值。

有两种方法使用包含在数据库其他表中的信息来修改一个表：使用子选择 或者在FROM子句中指定额外的表。这种技术只适合 特定的环境。

可选的RETURNING子句导致UPDATE 基于实际被更新的每一行计算并且返回值。任何使用该表的列以及 FROM中提到的其他表的列的表达式都能被计算。 计算时会使用该表的列的新（更新后）值。RETURNING 列表的语法和SELECT的输出列表相同。

你必须拥有该表上的UPDATE特权，或者至少拥有 要被更新的列上的该特权。如果任何一列的值需要被 expressions或者 condition读取， 你还必须拥有该列上的SELECT特权。

参数

with\_query

WITH子句允许你指定一个或者更多个在UPDATE中可用其名称引用的子查询。

table\_name

要更新的表的名称（可以是模式限定的）。如果在表名前指定了 ONLY，只会更新所提及表中的匹配行。如果没有指定 ONLY，任何从所提及表继承得到的表中的匹配行也会 被更新。可选地，在表名之后指定\*可以显式地指示要 把后代表也包括在内。

alias

目标表的一个替代名称。在提供了一个别名时，它会完全隐藏表的真实 名称。例如，给定UPDATE foo AS f， UPDATE语句的剩余部分必须用 f而不是foo来引用该表。

column\_name

table\_name 所指定的表的一列的名称。如果需要，该列名可以用一个子域名称或者 数组下标限定。不要在目标列的说明中包括表的名称 — 例如 UPDATE table\_name SET table\_name.col = 1是非法的。

expression

要被赋值给该列的一个表达式。该表达式可以使用该表中这一列或者 其他列的旧值。

DEFAULT

将该列设置为它的默认值（如果没有为它指定默认值表达式，默认值 将会为 NULL）。

sub-SELECT

一个SELECT子查询，它产生和在它之前的圆括号中列列表中 一样多的输出列。被执行时，该子查询必须得到不超过一行。如果它得到 一行，其列值会被赋予给目标列。如果它得不到行，NULL 值将被赋予给 目标列。该子查询可以引用被更新表中当前行的旧值。

from\_list

表表达式的列表，允许来自其他表的列出现在WHERE 条件和更新表达式中。这类似于可以在 SELECT语句的FROM 子句中指定的表列表。注意目标表不能出现在 from\_list中，除非你想做自连接（这种情况下它必须 以别名出现在from\_list中）。

condition

一个返回boolean类型值的表达式。让这个 表达式返回true的行将会被更新。

cursor\_name

要在WHERE CURRENT OF条件中使用的游标名。 要被更新的是从这个游标中最近取出的行。该游标必须是一个 在UPDATE目标表上的非分组查询。注意 WHERE CURRENT OF不能和一个布尔条件一起 指定。有关对游标使用WHERE CURRENT OF的 更多信息请见DECLARE。

output\_expression

在每一行被更新后，要被UPDATE命令计算并且返回 的表达式。该表达式可以使用

table\_name指定 的表或者FROM列出的表中的任何列名。写\* 可以返回所有列。

output\_name

用于一个被返回列的名称。

输出

成功完成时，一个UPDATE命令返回形如

UPDATE count

的命令标签。

count是被更新的行数， 包括值没有更改的匹配行。注意，当更新被一个BEFORE UPDATE 触发器抑制时，这个数量可能比匹配 condition的行数少。如果 count为零，没有行被该查 询更新（这不是一个错误）。

如果UPDATE命令包含一个RETURNING 子句，其结果将类似于一个包含RETURNING列表中定义的 列和值的SELECT语句（在被该命令更新的行上计算） 的结果。

注解

当存在FROM子句时，实际发生的是：目标表被连接到 from\_list中的表，并且该连接的每一个输出行表示对目标表的一个更新操作。在使用FROM 时，你应该确保该连接对每一个要修改的行产生至多一个输出行。换 句话说，一个目标行不应该连接到来自其他表的多于一行上。如果发 生这种情况，则只有一个连接行将被用于更新目标行，但是将使用哪 一行是很难预测的。

由于这种不确定性，只在一个子选择中引用其他表更安全，不过这种语句通常很难写并且也比使用连接慢。

在分区表的情况下，更新一行有可能导致它不再满足其所在分区的分区约束。此时，如果这个行满足分区树中某个其他分区的分区约束，那么这个行会被移动到那个分区。 如果没有这样的分区，则会发生错误。在后台，行的移动实际上是一次DELETE操作和一次INSERT操作。

在移动的行上的并发UPDATE或DELETE可能会收到序列化失败错误。 假设会话 1 正在分区键上执行UPDATE，同时，对可访问该行的并发会话 2 在此行上执行UPDATE或DELETE操作。 在这种情况下，会话 2 的UPDATE 或 DELETE将检测行移动并引发序列化失败错误（该错误始终返回 SQLSTATE 代码"40001"）。 如果发生这种情况，应用程序可能希望重试事务。 在通常情况下，表没有分区或没有行移动，会话 2 将标识新更新的行，并执行UPDATE/DELETE在此新行版本中。

请注意，虽然行可以从本地分区移动到外表分区（如果外数据包装器支持元组路由），但它们不能从外表分区移动到另一个分区。

示例

把表films的列kind 中的单词Drama改成Dramatic：

```
UPDATE films SET kind = \'Dramatic\' WHERE kind = \'Drama\';
```

在表weather的一行中调整温度项并且 把沉淀物重置为它的默认值：

```
UPDATE weather SET temp_lo = temp_lo+1, temp_hi = temp_lo+15, prcp = DEFAULT

WHERE city = \'San Francisco\' AND date = \'2003-07-03\';
```

执行相同的操作并且返回更新后的项：

```
UPDATE weather SET temp_lo = temp_lo+1, temp_hi = temp_lo+15, prcp = DEFAULT WHERE city = \'San Francisco\' AND date = \'2003-07-03\'

RETURNING temp_lo, temp_hi, prcp;
```

使用另一种列列表语法来做同样的更新：

```
UPDATE weather SET (temp_lo, temp_hi, prcp) = (temp_lo+1, temp_lo+15, DEFAULT)

WHERE city = \'San Francisco\' AND date = \'2003-07-03\';
```

为管理Acme Corporation账户的销售人员增加销售量，使用 FROM子句语法：

```
UPDATE employees SET sales_count = sales_count + 1 FROM accounts

WHERE accounts.name = \'Acme Corporation\'

AND employees.id = accounts.sales_person;
```

执行相同的操作，在 WHERE子句中使用子选择：

```
UPDATE employees SET sales_count = sales_count + 1 WHERE id =

(SELECT sales_person FROM accounts WHERE name = \'Acme Corporation\');
```

更新 accounts 表中的联系人姓名以匹配当前被分配的销售员：

```
UPDATE accounts SET (contact_first_name, contact_last_name) =

(SELECT first_name, last_name FROM salesmen

WHERE salesmen.id = accounts.sales_id);
```

可以用连接完成类似的结果：

```
UPDATE accounts SET contact_first_name = first_name,

contact_last_name = last_name

FROM salesmen WHERE salesmen.id = accounts.sales_id;
```

不过，如果salesmen.id不是一个唯一键， 第二个查询可能会给出令人意外的结果，然而如果有多个id匹配， 第一个查询保证会发生错误。还有，如果对于一个特定的 accounts.sales\_id项没有匹配，第一个查询将 把相应的姓名域设置为 NULL，而第二个查询完全不会更新该行。

更新一个统计表中的统计数据以匹配当前数据：

```
UPDATE summary s SET (sum_x, sum_y, avg_x, avg_y) =

(SELECT sum(x), sum(y), avg(x), avg(y) FROM data d

WHERE d.group_id = s.group_id);
```

尝试插入一个新库存项及其库存量。如果该项已经存在，则转而更新 已有项的库存量。要这样做并且不让整个事务失败，可以使用保存点：

```
BEGIN;

\-- 其他操作

SAVEPOINT sp1;

INSERT INTO wines VALUES(\'Chateau Lafite 2003\', \'24\');

\-- 假定上述语句由于未被唯一键失败，

\-- 那么现在我们发出这些命令：

ROLLBACK TO sp1;

UPDATE wines SET stock = stock + 24 WHERE winename = \'Chateau Lafite 2003\';

\-- 继续其他操作，并且最终

COMMIT;
```

更改表films中由游标c\_films 定位的行的kind列：

```
UPDATE films SET kind = \'Dramatic\' WHERE CURRENT OF c_films;
```

兼容性

这个命令符合SQL标准，不过 FROM和RETURNING子句是瀚高数据库扩展，把 WITH用于UPDATE也是扩展。

有些其他数据库系统提供了一个FROM选项，在其中在其中目标表可以在FROM中被再次列出。但 瀚高数据库不是这样解释 FROM的。在移植使用这种扩展的应用时要小心。

根据标准，一个目标列名的圆括号子列表的来源值可以是任意得到正确列数的行值 表达式。瀚高数据库只允许来源值是一个 行构造器或者一个子-SELECT。一个列的 被更新值可以在行构造器的情况中被指定为DEFAULT，但在子-SELECT的情况中不能这样做。

## VACUUM

— 垃圾收集并根据需要分析一个数据库

大纲

```
VACUUM \[ ( option \[, \...\] ) \] \[ table_and_columns \[, \...\] \]

VACUUM \[ FULL \] \[ FREEZE \] \[ VERBOSE \] \[ ANALYZE \] \[ table_and_columns \[, \...\] \]
```

其中option可以是下列之一：

```
FULL \[ boolean \]

FREEZE \[ boolean \]

VERBOSE \[ boolean \]

ANALYZE \[ boolean \]

DISABLE_PAGE_SKIPPING \[ boolean \]

SKIP_LOCKED \[ boolean \]

INDEX_CLEANUP \[ boolean \]

TRUNCATE \[ boolean \]
```

而table\_and\_columns是：

```
table_name \[ ( column_name \[, \...\] ) \]
```

描述

VACUUM收回由死亡元组占用的存储空间。在通常的瀚高数据库操作中，被删除或者被更新废弃的元组并没有在物理上从它们的表中移除，它们将一直存在直到一次VACUUM被执行。因此有必要周期性地做VACUUM，特别是在频繁被更新的表上。

在没有table\_and\_columns列表的情况下，VACUUM会处理当前用户具有清理权限的当前数据库中的每一个表和物化视图。如果给出一个列表，VACUUM可以只处理列表中的那些表。

VACUUM ANALYZE对每一个选定的表ANALYZE。这是两种命令的一种方便的组合形式，可以用于例行的维护脚本。其处理细节可参考ANALYZE。

简单的 VACUUM（不带FULL）简单地收回空间并使其可以被重用。这种形式的命令可以和表的普通读写操作并行，因为它不会获得一个排他锁。但是，这种形式中额外的空间并没有被还给操作系统（在大多数情况下），它仅仅被保留在同一个表中以备重用。VACUUM FULL将表的整个内容重写到一个新的磁盘文件中，并且不包含额外的空间，这使得没有被使用的空

间被还给操作系统。这种形式的命令更慢并且在其被处理时要求在每个表上保持一个排他锁。

当选项列表被包围在圆括号中时，选项可以被写成任何顺序。如果没有圆括号，选项必须严格按照上面所展示的顺序指定。

参数

FULL

选择”完全”清理，它可以收回更多空间，并且需要更长时间和表上的排他锁。这种方法还需要额外的磁盘空间，因为它会创建该表的一个新拷贝，并且在操作完成之前都不会释放旧的拷贝。通常这种方法只用于需要从表中收回数量庞大的空间时。

FREEZE

选择激进的元组”冻结”。指定FREEZE 等价于参数vacuum\_freeze\_min\_age和

vacuum\_freeze\_table\_age设置为0的

VACUUM。当表被重写时总是会执行激进的冻结，

因此指定FULL时这个选项是多余的。

VERBOSE

为每个表打印一份详细的清理活动报告。

ANALYZE

更新优化器用以决定最有效执行一个查询的方法的统计信息。

DISABLE\_PAGE\_SKIPPING

通常，VACUUM将基于可见性映射跳过页面。已知所有元组都被冻结的页面总是会被跳过，而那些所有元组对所有事务都可见的页面则可能会被跳过（除非执行的是激进的清理）。此外，除非在执行激进的清理时，一些页面也可能会被跳过，这样可避免等待其他页面完成对其使用。这个选项禁用所有的跳过页面的行为，其意图是只在可见性映射内容被怀疑时使用，这种情况只有在硬件或者软件问题导致数据库损坏时才会发生。

SKIP\_LOCKED

规定VACUUM在开始处理关系时不等待任何冲突锁被释放：如果关系不能立即锁定而不等待，则跳过关系。 请注意即使采用此选项，VACUUM在打开关系的索引时仍可能阻塞。

此外，VACUUM ANALYZE在从分区、继承子表和某些类型的外表获取示例行时，仍然可能阻塞。还有，虽然VACUUM通常处理指定分区表的所有分区，但如果分区表上的锁冲突，此选项将导致VACUUM跳过所有分区。

INDEX\_CLEANUP

规定VACUUM尝试删除指向死元组的索引条目。 这通常是所需的行为，并且是默认行为，除非将vacuum\_index\_cleanup 选项设置为 false，对要被清空的表。 如果需要尽快运行清空操作的话，将此选项设置为 false 可能很有用，例如，为了避免即将发生的事务ID回绕\[wraparound\]。但是，如果不定期执行索引清理，性能可能会受到影响，因为随着表的修改，索引将累积死元组，并且表本身将累积死行指针，在索引清理完成之前都无法删除。 此选项对于没有索引的表无效，如果使用 FULL 选项，则忽略此选项。

TRUNCATE

指定VACUUM尝试截断表末尾的任何空页，并允许将截断页的磁盘空间返回到操作系统。

这通常是所需的行为，并且是默认行为，除非将vacuum\_truncate选项设置为 false，对要被清空的表。 将此选项设置为false可能有助于避免ACCESS EXCLUSIVE锁定需要截断的表。如果使用FULL选项，则忽略此选项。

boolean

指定打开还是关闭所选选项。你可以写入TRUE、ON或1以启用该选项，以及FALSE、OFF或0来禁用它。 在TRUE被假定的情况下，boolean 值也可以被省略。

table\_name

要清理的表或物化视图的名称（可以有模式修饰）。如果指定的表示一个分区表，则它所有的叶子分区也会被清理。

column\_name

要分析的指定列的名称。缺省是所有列。如果指定了一个列的列表，则ANALYZE也必须被指定。

输出

如果声明了VERBOSE，VACUUM会发出进度消息来表明当前正在处理哪个表。各种有关这些表的统计信息也会打印出来。

注解

要清理一个表，操作者通常必须是表的拥有者或者超级用户。但是，数据库拥有者被允许清理他们的数据库中除了共享目录之外的所有表（对于共享目录的限制意味着一个真正的数据库范围的VACUUM只能被超级用户执行）。VACUUM将会跳过执行者不具备清理权限的表。

VACUUM不能在一个事务块内被执行。

对具有GIN索引的表，VACUUM（任何形式）也会通过将待处理索引项移动到主要GIN索引结构中的合适位置来完成任何待处理的索引插入。

我们建议经常清理活动的生产数据库（至少每晚一次），以保证移除失效的行。在增加或删除了大量行之后， 对受影响的表执行VACUUM ANALYZE命令是一个很好的做法。这样做将把最近的更改更新到系统目录，并且允许 瀚高数据库查询规划器在规划用户查询时做出更好的选择。

日常使用时，不推荐FULL选项，但在特殊情况时它会有用。一个例子是当你删除或者更新了一个表中的绝大部分行时，如果你希望在物理上收缩表以减少磁盘空间占用并且允许更快的表扫描，则该选项是比较合适的。VACUUM FULL通常会比简单VACUUM更多地收缩表。

VACUUM会导致I/O流量的大幅度增加，这可能导致其他活动会话性能变差。因此，有时建议使用基于代价的清理延迟特性。

瀚高数据库包括了一个”autovacuum”工具，它可以自动进行例行的清理维护。

示例

清理单一表onek，为优化器分析它并且打印出详细的清理活动报告：

```
VACUUM (VERBOSE, ANALYZE) onek;
```

兼容性

在SQL标准中没有VACUUM语句。

参见

vacuumdb

## VALUES

— 计算一个行集合

**大纲**

```
VALUES ( expression \[, \...\] ) \[, \...\]

\[ ORDER BY sort_expression \[ ASC \| DESC \| USING operator \] \[, \...\] \]

\[ LIMIT { count \| ALL } \]

\[ OFFSET start \[ ROW \| ROWS \] \]

\[ FETCH { FIRST \| NEXT } \[ count \] { ROW \| ROWS } ONLY \]
```

**描述**

VALUES计算由值表达式指定的一个行值或者 一组行值。更常见的是把它用来生成一个大型

命令内的”常量表”， 但是它也可以被独自使用。

当多于一行被指定时，所有行都必须具有相同数量的元素。结果表的列数据类型 由出现在该列的表达式的显式或者推导类型组合决定，决定的规则与UNION相同。

在大型的命令中，在语法上允许VALUES出现在 SELECT出现的任何地方。因为语法把它当做

一个 SELECT，可以为一个VALUES 命令使用ORDER BY、LIMIT（或者等效的FETCH FIRST）以及OFFSET子句。

**参数**

expression

要在结果表（行集合）中指定位置计算并且插入的一个常量或者表达式。 在一个出现于INSERT顶层的 VALUES列表中， expression可以被DEFAULT替代以表示应该插入目标列的默认值。 当VALUES出现在其他环境中时，不能使用 DEFAULT。

sort\_expression

一个指示如何排序结果行的表达式或者整型常量。这个表达式可以用column1、column2等来 引用该VALUES结果的列。详见 ORDER BY 子句。

operator

一个排序操作符。详见 ORDER BY 子句。

count

要返回的最大行数。详见 LIMIT 子句。

start

开始返回行之前要跳过的行数。详见 LIMIT 子句。

**注解**

应该避免具有大量行的VALUES列表，否则可能会 碰到内存不足失败或者很差的性能。出现在INSERT 中的VALUES是一种特殊情况（因为想要的列类型可以从INSERT的目标表得知，并且不需要通过扫描 该VALUES列表来推导），因此它可以处理比其他环境中更大的列表。

**示例**

一个纯粹的VALUES命令：

```
VALUES (1, \'one\'), (2, \'two\'), (3, \'three\');
```

这将返回一个具有两列、三行的表。它实际等效于：

```
SELECT 1 AS column1, \'one\' AS column2

UNION ALL

SELECT 2, \'two\'

UNION ALL

SELECT 3, \'three\';
```

更常用地，VALUES可以被用在一个大型 SQL 命令中。 在INSERT中最常用：

```
INSERT INTO films (code, title, did, date_prod, kind)

VALUES (\'T_601\', \'Yojimbo\', 106, \'1961-06-16\', \'Drama\');
```

在INSERT的环境中，一个VALUES列表 的项可以是DEFAULT来指示应该使用该列的默认值而不是 指定一个值：

```
INSERT INTO films VALUES

(\'UA502\', \'Bananas\', 105, DEFAULT, \'Comedy\', \'82 minutes\'),

(\'T_601\', \'Yojimbo\', 106, DEFAULT, \'Drama\', DEFAULT);
```

VALUES也可以被用在可以写子-SELECT 的地方，例如在一个FROM子句中：

```
SELECT f.\*

FROM films f, (VALUES(\'MGM\', \'Horror\'), (\'UA\', \'Sci-Fi\')) AS t (studio, kind)

WHERE f.studio = t.studio AND f.kind = t.kind;

UPDATE employees SET salary = salary \* v.increase

FROM (VALUES(1, 200000, 1.2), (2, 400000, 1.4)) AS v (depno, target, increase)

WHERE employees.depno = v.depno AND employees.sales \>= v.target;
```

注意当VALUES被用在一个FROM子句中时， 需要提供一个AS子句，与SELECT相同。不需要为所有的列用AS子句指定名称，但是那样做是一种好习惯（在瀚高数据库中，VALUES的默认列名是column1、column2等，但在其他数据库系统中可能会不同）。

当在INSERT中使用VALUES时，值都会被自动地强制为相应目标列的数据类型。当在其他环境中使用时，有必要指定正确的数据类型。如果项都是带引号的字符串常量，强制第一个就足以为所有项假设数据类型：

```
SELECT \* FROM machines

WHERE ip_address IN (VALUES(\'192.168.0.1\'::inet), (\'192.168.0.10\'),

(\'192.168.1.43\'));
```

> **提示：**
> 
> 对于简单的 `IN` 测试，最好使用 `IN` 的 list-of-scalars形式而不是写一个上面那样的 `VALUES` 查询。标量列表方法的书写更少并且常常更加高效。

**兼容性**

VALUES符合 SQL 标准。 LIMIT和OFFSET是瀚高数据库扩展，另见 SELECT。

**另见**

INSERT, SELECT