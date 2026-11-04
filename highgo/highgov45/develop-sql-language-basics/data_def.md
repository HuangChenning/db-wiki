---
title: "4.数据定义"
book: "HGDB-SEE V4.5 SQL语言基础"
version: "V4.5"
source: "https://highgo.com/document/zh-cn/develop/data_def.html"
tags:
  - highgo
  - highgo-v45
  - develop-sql-language-basics
---

## 4\. 数据定义

## 4.1. 数据表

关系型数据库中的一个表就像纸上的一张表：它由行和列组成。列的数量和顺序是固定的，并且每一列拥有一个名字。

每一列都有一个数据类型。数据类型可以限制该列的取值。例如，一个被声明为数字类型的列将不会接受任何文本串，而存储在这样一列中的数据可以用来进行数学计算。

瀚高数据库包括多种内置数据类型，用户也可以定义自己的数据类型。大部分内置数据类型有着明确的名称和语义，详细信息可参考第八章。一些常用的数据类型是：用于整数的integer；可以用于分数的numeric；用于字符串的text，用于日期的date，用于一天内时间的time以及可以同时包含日期和时间的timestamp。

要创建一个表，我们要用到CREATE TABLE命令。在这个命令中 我们需要为新表至少指定一个名字、列的名字及数据类型。例如：

CREATE TABLE my\_first\_table (

first\_column text,

second\_column integer

);

这将创建一个名为my\_first\_table的表，该表有两个列。第一个列名为first\_column且数据类型为text；第二个列名为second\_column且数据类型为integer。表和列的名字遵循第 4.1.1 节中解释的标识符语法。类型名称通常也是标识符，但是也有些例外。

| **提示：** |
| --- |
| 当我们创建很多相关的表时，最好为表和列选择一致的命名模式。用单数或复数名词作为表名。 |

一个表能够拥有的列的数据是有限的，根据列的类型，这个限制介于250和1600之间。

如果我们不再需要一个表，我们可以通过使用DROP TABLE命令来移除它。例如：

DROP TABLE my\_first\_table;

DROP TABLE products;

尝试移除一个不存在的表会报错。但是在SQL脚本中，创建每个表之前先尝试删除该表的做法是很常见的，即使报错也会忽略，因此这样的脚本可以在表存在和不存在时都正常工作（可以使用DROP TABLE IF EXISTS来防止出现错误消息，但该语句并非标准SQL）。

如果需要修改一个已经存在的表，请参考本章稍后的第 4.6 节。

## 4.2. 默认值

一个列可以被分配一个默认值。当一个新行被创建且没有为该列指定值时，该列将被赋值为默认值。也可以使用命令显式指定该列使用其默认值（数据操作命令详见第 5 章）。

如果没有显式指定默认值，则默认值是空值。这是合理的，因为空值表示未知数据。

在一个表定义中，默认值被列在列的数据类型之后。例如：

CREATE TABLE products (

product\_no integer,

name text,

price numeric DEFAULT 9.99

);

默认值可以是一个表达式，它将在任何需要插入默认值的时候被实时计算（不是表创建时）。一个常见的例子是为一个timestamp列指定默认值为CURRENT\_TIMESTAMP，这样该列将得到行被插入时的时间。另一个常见的例子是为每一行生成一个“序列号” 。在瀚高数据库中可以按照如下方式实现：

CREATE TABLE products (

product\_no integer DEFAULT nextval(‘products\_product\_no\_seq’),

…

);

这里nextval()函数是从一个序列对象获取连续值（第 8.16 节）。

还有一种快速的方式：

CREATE TABLE products (

product\_no SERIAL,

…

);

SERIAL将在第 7.1.4 节进一步讨论。

## 4.3. 生成列

生成列是一种特殊的列，它总是从其他列计算而来。因此说，它对于列就像视图对于表一样。生成列有两种:存储列和虚拟列。存储生成列在写入(插入或更新)时计算，并且像普通列一样占用存储空间。虚拟生成列不占用存储空间并且在读取时进行计算。 如此看来，虚拟生成列类似于视图，存储生成列类似于物化视图(除了它总是自动更新之外)。

瀚高数据库目前只支持存储生成列。

在 CREATE TABLE中使用 GENERATED ALWAYS AS 子句可以创建一个生成列，例如:

CREATE TABLE people (

…,

height\_cm numeric,

height\_in numeric GENERATED ALWAYS AS (height\_cm / 2.54) STORED

);

必须指定关键字 STORED 以选择生成列的存储类型。更多细节请参见 CREATE TABLE 。

生成列不能被直接写入。在INSERT 或 UPDATE 命令中, 不能为生成列指定值, 但是可以指定关键字DEFAULT。

考虑列缺省情况和生成列之间的差异。如果没有提供其他值，列缺省情况下在行被首次插入时计算一次；生成列则在行每次改变时进行更新，并且不能被取代。生成表达式通常会引用其他列，列缺省情况下不能引用表的其他列。列缺省情况下可以使用易失性函数，例如random()或引用当前时间函数；而对于生成列是不允许的。

生成列和涉及生成列的表的定义有几个限制:

• 生成表达式只能使用不可变函数，并且不能使用子查询或以任何方式引用当前行以外的任何内容。

• 生成表达式不能引用另一个生成列。

• 生成表达式不能引用系统表，除了tableoid。

• 生成列不能具有列默认或标识定义。

• 生成列不能是分区键的一部分。

• 外部表可以有生成列。更多细节请参见 CREATE FOREIGN TABLE.

使用生成列的其他注意事项。

• 生成列保留着有别于其下层的基础列的访问权限。因此，可以对其进行排列以便于从生成列中读取特定的角色，而不是从下层基础列中读取。

• 从概念上讲，生成列在BEFORE 触发器运行后更新。 因此，BEFORE 触发器中的基础列所做的变更将反映到生成列中。但相反，不允许访问BEFORE触发器中的生成列。

## 4.4. 约束

数据类型是一种限制能够存储在表中数据类别的方法。但是对于很多应用来说，它们提供的约束太粗糙。例如，一个包含产品价格的列应该只接受正值。但是没有任何一种标准数据类型只接受正值。另一个问题是我们可能需要根据其他列或行来约束一个列中的数据。例如，在一个包含产品信息的表中，对于每个产品编号应该只有一行。

约束让我们能够根据我们的愿望来控制表中的数据。如果一个用户试图在一个列中保存违反约束的数据，命令会报错无法执行。即便是这个值来自于默认值，这个规则也同样适用。

### 4.4.1. 检查约束

检查约束是最普通的约束类型。它允许我们指定特定列中的值必须要满足一个布尔表达式。例如，产品价格只能为正数，我们可以使用：

CREATE TABLE products (

product\_no integer,

name text,

price numeric CHECK (price > 0)

);

约束定义就和默认值定义一样跟在数据类型之后。默认值和约束之间的顺序没有影响。检查约束由关键字CHECK以及其后的包围在圆括号中的表达式组成。检查约束表达式应该涉及到被约束的列，否则该约束也没什么实际意义。

我们也可以赋予约束一个独立的名称。这样错误消息会更明了，同时也可以在需要更改约束时引用该名称。语法为：

CREATE TABLE products (

product\_no integer,

name text,

price numeric CONSTRAINT positive\_price CHECK (price > 0)

);

要指定一个命名的约束，请在约束名称标识符前使用关键词CONSTRAINT，然后把约束定义放在标识符之后。

一个检查约束也可以引用多个列。例如我们存储一个普通价格和一个打折后的价格，而我们希望保证打折后的价格低于普通价格：

CREATE TABLE products (

product\_no integer,

name text,

price numeric CHECK (price > 0),

discounted\_price numeric CHECK (discounted\_price > 0),

CHECK (price > discounted\_price)

);

前两个约束看起来很相似。第三个则使用了一种新语法。它并没有依附在一个特定的列，而是作为一个独立的项出现在逗号分隔的列列表中。列定义和这种约束定义可以以混合出现在列表中。

我们将前两个约束称为列约束，而第三个约束称为表约束，因为它独立于任何一个列定义。列约束也可以写成表约束，但反过来不行，因为一个列约束只能引用它所依附的那个列（瀚高数据库并不强制要求这个规则，但是为了确保可移植性建议遵循该规则）。上述例子也可以写成：

CREATE TABLE products (

product\_no integer,

name text,

price numeric,

CHECK (price > 0),

discounted\_price numeric,

CHECK (discounted\_price > 0),

CHECK (price > discounted\_price)

);

甚至是：

CREATE TABLE products (

product\_no integer,

name text,

price numeric CHECK (price > 0),

discounted\_price numeric,

CHECK (discounted\_price > 0 AND price > discounted\_price)

);

表约束也可以指定约束名称：

CREATE TABLE products (

product\_no integer,

name text,

price numeric,

CHECK (price > 0),

discounted\_price numeric,

CHECK (discounted\_price > 0),

CONSTRAINT valid\_discount CHECK (price > discounted\_price)

);

需要注意的是，一个检查约束在其检查表达式值为真或空值时被满足。因为当任何操作数为空时大部分表达式将计算为空值，此时检查约束不会阻止将该列设置为空值。如果希望一个列不包含空值，可以使用下一节中的非空约束。

| **注意：** |
| --- |
| 瀚高数据库CHECK约束涉及的列必须包含在该表中，并且CHECK约束不能引用正在INSERT或者UPDATE行以外的其他行数据，否则可能出现数据库转储或重新加载失败。可以使用UNIQUE, EXCLUDE,或 FOREIGN KEY约束来进行跨行和跨表限制。如果想在插入行的时候对其他行进行一次性检查，而不是持续维护一致性，可以使用自定义 trigger 来实现这个功能。 |

### 4.4.2. 非空约束

非空约束用于限制列中不会有空值。语法示例：

CREATE TABLE products (

product\_no integer NOT NULL,

name text NOT NULL,

price numeric

);

非空约束总是被写成一个列约束。一个非空约束等价于创建一个检查约束CHECK (column\_name IS NOT NULL)，但在瀚高数据库中创建一个显式的非空约束效率更高。这种方式创建的非空约束的缺点是我们无法为它给予一个显式的名称。

当然，一个列可以有多个约束，只需要将这些约束挨个写出：

CREATE TABLE products (

product\_no integer NOT NULL,

name text NOT NULL,

price numeric NOT NULL CHECK (price > 0)

);

约束的顺序没有限制，因为并不需要决定约束被检查的顺序。

对于NOT NULL约束有一个相反的用法：NULL约束。 这是字段的默认约束，是NOT NULL约束的非值，代表该字段可以为空。 SQL 标准中不存在 NULL 约束，瀚高数据库支持该语法仅是为了和一些数据库做兼容，不推荐也不应该在常规操作中显式指定NULL约束。

### 4.4.3. 唯一约束

唯一约束保证在一列中或者一组列中保存的数据在表中所有行中是唯一的。写成列约束的语法是：

CREATE TABLE products (

product\_no integer UNIQUE,

name text,

price numeric

);

写成表约束的语法是：

CREATE TABLE products (

product\_no integer,

name text,

price numeric,

UNIQUE (product\_no)

);

要为一组列定义一个唯一约束，需要把它写作一个表级约束，列名用逗号分隔：

CREATE TABLE example (

a integer,

b integer,

c integer,

UNIQUE (a, c)

);

这指定这些列的组合值在整个表的范围内是唯一的，但其中任意一列的值并不需要是（一般也不是）唯一的。

为唯一约束命名：

CREATE TABLE products (

product\_no integer CONSTRAINT must\_be\_different UNIQUE,

name text,

price numeric

);

增加一个唯一约束会在约束中列出的列或列组上自动创建一个唯一B-tree索引。只覆盖某些行的唯一性限制不能被写为一个唯一约束，但可以通过创建一个唯一的部分索引来强制这种限制。

通常，如果表中有超过一行在约束所包括列上的值相同，将会违反唯一约束。但是两个空值被认为是不同的。这意味着即便存在一个唯一约束，也可以存储多个该列为空值的行。这种行为符合SQL标准，但某些SQL数据库可能不遵循该规则，所以在数据迁移时应注意这一点。

### 4.4.4. 主键

主键约束表示可以用作表中行的唯一标识符的一个列或者一组列。这要求那些值都是唯一的并且非空。因此，下面的两个表定义可接受的数据是相同的：

CREATE TABLE products (

product\_no integer UNIQUE NOT NULL,

name text,

price numeric

);

CREATE TABLE products (

product\_no integer PRIMARY KEY,

name text,

price numeric

);

主键也可以包含多个列，其语法和唯一约束相似：

CREATE TABLE example (

a integer,

b integer,

c integer,

PRIMARY KEY (a, c)

);

增加一个主键将自动在主键中列出的列或列组上创建一个唯一B-tree索引。并且会强制这些列被标记为NOT NULL。

一个表最多只能有一个主键（可以有任意数量的唯一和非空约束，它们可以达到和主键几乎一样的功能，但只能有一个被标识为主键）。关系数据库理论要求每一个表都要有一个主键。但瀚高数据库中并未强制要求这一点，但是建议遵循它。

主键对于文档和客户端应用都是有用的。例如，一个允许修改行值的 GUI 应用可能需要知道一个表的主键，以便能唯一地标识行。如果定义了主键，数据库系统也有多种方法来利用主键。例如，主键定义了外键要引用的默认目标列。

### 4.4.5. 外键

外键约束指定一列（或一组列）中的值必须匹配出现在另一个表中某些行的值。我们说这维持了两个关联表之间的引用完整性。

例如我们有一个使用过多次的产品表：

CREATE TABLE products (

product\_no integer PRIMARY KEY,

name text,

price numeric

);

让我们假设我们还有一个存储这些产品订单的表。我们希望保证订单表中只包含真正存在的产品的订单。因此我们在订单表中定义一个引用产品表的外键约束：

CREATE TABLE orders (

order\_id integer PRIMARY KEY,

product\_no integer REFERENCES products (product\_no),

quantity integer

);

现在就不可能创建包含不存在于产品表中的product\_no值（非空）的订单。

我们说在这种情况下，订单表是引用表而产品表是被引用表。相应地，也有引用和被引用列的说法。

我们也可以把上述命令简写为：

CREATE TABLE orders (

order\_id integer PRIMARY KEY,

product\_no integer REFERENCES products,

quantity integer

);

如果不指定列，则被引用表的主键将被用作被引用列。

一个外键也可以约束和引用一组列。同样的，它需要被写成表约束的形式。下面是一个例子：

CREATE TABLE t1 (

a integer PRIMARY KEY,

b integer,

c integer,

FOREIGN KEY (b, c) REFERENCES other\_table (c1, c2)

);

当然，被约束列的数量和类型应该匹配被引用列的数量和类型。

按照前面的方式，我们可以为一个外键约束命名。

一个表可以有超过一个的外键约束。这被用于实现表之间的多对多关系。例如我们有关于产品和订单的表，但我们现在希望一个订单能包含多种产品（这在上面的结构中是不允许的）。我们可以使用这种表结构：

CREATE TABLE products (

product\_no integer PRIMARY KEY,

name text,

price numeric

);

CREATE TABLE orders (

order\_id integer PRIMARY KEY,

shipping\_address text,

…

);

CREATE TABLE order\_items (

product\_no integer REFERENCES products,

order\_id integer REFERENCES orders,

quantity integer,

PRIMARY KEY (product\_no, order\_id)

);

注意在最后一个表中主键和外键之间有重叠。

以下表定义实现了不允许移除一个仍然被订单引用（通过order\_items）的产品，但是当移除一个订单时订单项也同时被移除：

CREATE TABLE products (

product\_no integer PRIMARY KEY,

name text,

price numeric

);

CREATE TABLE orders (

order\_id integer PRIMARY KEY,

shipping\_address text,

…

);

CREATE TABLE order\_items (

product\_no integer REFERENCES products ON DELETE RESTRICT,

order\_id integer REFERENCES orders ON DELETE CASCADE,

quantity integer,

PRIMARY KEY (product\_no, order\_id)

);

上述是常见的限制删除和级联删除功能。RESTRICT阻止删除一个被引用的行。NO ACTION表示在约束被检查时如果有任何引用行存在，则会抛出一个错误，这是我们没有指定任何东西时的默认行为（这两种选择的本质不同在于NO ACTION允许检查被推迟到事务的最后，而RESTRICT则不会）。CASCADE指定当一个被引用行被删除后，引用它的行也应该被自动删除。还有其他两种选项：SET NULL和SET DEFAULT。这些将导致在被引用行被删除后，引用行中的引用列被置为空值或它们的默认值。如果一个动作指定了SET DEFAULT，但是默认值不满足外键约束，操作将会失败。

与ON DELETE相似，同样有ON UPDATE可以用在一个被引用列被修改（更新）的情况，可选的动作相同。在这种情况下，CASCADE意味着被引用列的更新值应该被复制到引用行中。

正常情况下，如果一个引用行的任意一个引用列都为空，则它不需要满足外键约束。如果在外键定义中加入了MATCH FULL，一个引用行只有在它的所有引用列为空时才不需要满足外键约束（因此空和非空值的混合肯定会导致MATCH FULL约束失败）。如果不希望引用行能够避开外键约束，可将引用行声明为NOT NULL。

一个外键所引用的列必须是一个主键或者唯一约束列。这意味着被引用列总是拥有一个索引（位于主键或唯一约束之下的索引），因此在其上进行的一个引用行是否匹配的检查将会很高效。由于从被引用表中DELETE一行或者UPDATE一个被引用列将要求对引用表进行扫描以得到匹配旧值的行，在引用列上建立合适的索引也会大有益处。由于这种做法并不是必须的，而且创建索引也有很多种选择，所以外键约束的定义并不会自动在引用列上创建索引。

更多关于更新和删除数据的信息请见第 5 章。外键约束的语法描述请参考CREATE TABLE。

### 4.4.6. 排他约束

通过排他约束可以完成指定的列或表达式在指定运算符下数据的比较，运算结果返回true的将被禁止。例如：

CREATE TABLE tb1(

ID INT NOT NULL,

NAME TEXT,

AGE INT,

ADDRESS CHAR(50),

EXCLUDE USING gist

(NAME WITH =,

AGE WITH <>)

该约束对NAME进行等值比较，同时对AGE进行不等比较，如果满足NAME相同，AGE不相同则不允许插入。

INSERT INTO tb1 VALUES(1, ‘Zhang’, 30, ‘Beijing’ );–成功插入

INSERT INTO tb1 VALUES(2, ‘Zhang’, 30, ‘Shanghai’ );–成功插入

INSERT INTO tb1 VALUES(3, ‘Liu’, 40, ‘Jinan’ );–成功插入

INSERT INTO tb1 VALUES(2, ‘Zhang’, 33, ‘Dezhou’ );–插入失败

详见CREATE TABLE … CONSTRAINT … EXCLUDE。

增加一个排他约束将在约束声明所指定的类型上自动创建索引。

### 4.4.7. 约束开关

数据库支持约束开关功能，用户可通过执行SQL语句实现对约束的开启和禁用。

约束启用语法为:

ALTER TABLE table\_name ENABLE CONSTRAINT constraint\_name;

约束禁用开关：

ALTER TABLE table\_name DISABLE CONSTRAINT constraint\_name;

相应的，在系统表pg\_constraint的字段conenabled会记录约束的启用状态。

## 4.5. 系统列

每一个表都拥有一些由系统隐式定义的system columns。因此，这些列的名字不能像用户定义的列一样使用（注意这种限制与名称是否为关键字没有关系，即便用引号限定一个名称也无法绕过这种限制）。 事实上用户不需要关心这些列，只需要知道它们存在即可。

**tableoid**

包含这一行的表的OID。该列是特别为继承表（见第 4.10 节）和分区表（第4.11章节？）的查询而准备，因为如果没有它将很难知道某一行来自于哪个表。tableoid可以与pg\_class的oid列进行连接来获得表的名称。

**xmin**

插入该行版本的事务ID。行版本是该行的特殊版本，对一个逻辑行的每一次更新都将创建一个新的行版本。

**cmin**

插入事务中的命令标识符（从0开始）。

**xmax**

删除事务的事务ID，对于未删除的行版本该值为0。对于一个可见的行版本，该列值也可能为非零。这通常表示删除事务还没有提交，或者删除事务被回滚。

**cmax**

删除事务中的命令标识符，或者为0。

**ctid**

行版本在其表中的物理位置。注意尽管ctid可以被用来非常快速地定位行版本，但是一个行的ctid会在被更新或者被VACUUM FULL移动时改变。因此，ctid不能作为一个长期行标识符。应使用主键来标识逻辑行。

事务标识符是32位。在一个长期存在的数据库中事务ID会回卷，所以长期（超过10亿个事务）依赖事务ID的唯一性是不明智的。

命令标识符也是32位。这对一个事务中包含的SQL命令设置了一个硬极限：232（40亿）。注意该限制只是针对SQL命令的数目而不是被处理的行数。同样，只有真正修改了数据库内容的命令才会消耗一个命令标识符。

## 4.6. 修改表

使用ALTER TABLE命令对表的定义或者结构进行修改。支持的操作包括：

• 增加列

• 移除列

• 增加约束

• 移除约束

• 修改默认值

• 修改列数据类型

• 重命名列

• 重命名表

详细信息请参考ALTER TABLE命令。

### 4.6.1. 增加列

要增加一个列，可以使用如下命令：

ALTER TABLE products ADD COLUMN description text;

新列将被默认值填充（如果没有指定DEFAULT子句，则会填充空值）。

| **提示** |
| --- |
| 从 瀚高数据库V4.5开始，添加一个具有常量默认值的列不需要在执行ALTER TABLE 语句时更新表的每一行。相反，默认值将在下次访问该行时返回，并在表被重写时应用，从而使得ALTER TABLE即使在大表上执行也非常快。   但是，如果默认值是可变的（例如clock\_timestamp()），则每一行会在执行ALTER TABLE时更新。为避免潜在的长时间的更新操作，特别是如果你想要用大多数非默认值填充列，最好先添加没有默认值的列，再用 UPDATE插入正确的值，然后再添加需要的默认值。 |

也可以同时为列定义约束，语法：

ALTER TABLE products ADD COLUMN description text CHECK (description <> ‘’);

事实上CREATE TABLE中关于列的描述都可以应用在这里。无论如何，默认值必须满足给定的约束，否则ADD将会失败。也可以先将新列的值填充好，然后再增加约束（见后文）。

### 4.6.2. 移除列

为了移除一个列，使用如下的命令：

ALTER TABLE products DROP COLUMN description;

列中的数据将会消失。涉及到该列的表约束也会被移除。然而，如果该列被另一个表的外键所引用，瀚高数据库不会直接移除该约束。我们可以通过增加CASCADE来授权移除任何依赖于被删除列的所有东西：

ALTER TABLE products DROP COLUMN description CASCADE;

### 4.6.3. 增加约束

为了增加一个约束，可以使用表约束的语法，例如：

ALTER TABLE products ADD CHECK (name <> ‘’);

ALTER TABLE products ADD CONSTRAINT some\_name UNIQUE (product\_no);

ALTER TABLE products ADD FOREIGN KEY (product\_group\_id) REFERENCES

product\_groups;

要增加一个不能写成表约束的非空约束，可使用语法：

ALTER TABLE products ALTER COLUMN product\_no SET NOT NULL;

该约束会立即被检查，所以表中的数据必须在约束被增加之前就已经符合约束。

### 4.6.4. 移除约束

为了移除一个约束首先需要知道它的名称，可使用psql命令\\d加表名来查看约束名称。移除约束的命令为：

ALTER TABLE products DROP CONSTRAINT some\_name;

（如果处理的是自动生成的约束名称，如$2，别忘了用双引号使它变成一个合法的标识符。）

和移除一个列相似，如果需要移除一个被其他东西依赖的约束，也需要加上CASCADE。例如一个外键约束依赖于被引用列上的一个唯一或者主键约束。

上述方法可用于非空约束之外的所有约束类型。为了移除一个非空约束可以用：

ALTER TABLE products ALTER COLUMN product\_no DROP NOT NULL;

（非空约束是没有名称的，所以不能用第一种方式。）

### 4.6.5. 更改列的默认值

要为一个列设置一个新默认值，使用命令：

ALTER TABLE products ALTER COLUMN price SET DEFAULT 6.66;

注意这不会影响任何表中已经存在的行，它只是为未来的INSERT命令改变了默认值。

要移除默认值，使用：

ALTER TABLE products ALTER COLUMN price DROP DEFAULT;

这等同于将默认值设置为空值。相应的，试图删除一个未被定义的默认值并不会引发错误，因为默认值已经被隐式地设置为空值。

### 4.6.6. 修改列的数据类型

为了将一个列转换为一种不同的数据类型，使用如下命令：

ALTER TABLE products ALTER COLUMN price TYPE numeric(10,2);

只有当列中的每一个项都能隐式转换为新的类型时该操作才能成功。如果需要一种更复杂的转换，应该加上一个USING子句来指定应该如何把旧值转换为新值。

瀚高数据库将尝试把列的默认值转换为新类型，其他涉及到该列的任何约束也是一样。但是这些转换可能失败或者产生意想不到的结果。因此最好在修改类型之前先删除该列上所有的约束，然后在修改完类型后重新加上相应修改过的约束。

### 4.6.7. 重命名列

要重命名一个列：

ALTER TABLE products RENAME COLUMN product\_no TO product\_number;

### 4.6.8. 重命名表

要重命名一个表：

ALTER TABLE products RENAME TO items;

## 4.7. 模式

一个瀚高数据库集簇中包含一个或多个数据库。用户和用户组在整个集簇范围内共享。但除此之外没有其他数据在集簇内共享。任何给定的客户端连接只能访问在连接中指定的数据库中的数据。

| **注意：** |
| --- |
| 一个集簇的用户并不一定拥有访问集簇中每一个数据库的权限。用户名的共享意味着不可能在同一个集簇中出现重名的用户。 |

一个数据库包含一个或多个模式，模式中包含表。模式还包含其他类型的对象，包括数据类型、函数和操作符。相同的对象名称可以被用于不同的模式中，例如schema1和myschema都可以包含名为mytable的表。和数据库不同，模式并不是被严格地隔离：只要他们有足够的权限一个用户可以访问他们所连接的数据库中的所有模式内的对象。

合理使用模式可以达到如下目的：

• 允许多个用户使用一个数据库并且不会互相干扰。

• 将数据库对象组织成逻辑组以便更容易管理。

• 第三方应用的对象可以放在独立的模式中，这样它们就不会与其他对象的名称发生冲突。

模式类似于操作系统层的目录，但是模式不能嵌套。

### 4.7.1. 创建模式

要创建一个模式，可使用CREATE SCHEMA命令。例如：

CREATE SCHEMA myschema;

在一个模式中创建或访问对象，需要使用由模式名和表名构成的限定名，模式名和表名之间以点号分隔：

schema.table

在任何需要指定表名的地方都可以这样用，包括表修改命令和后续章节要讨论的数据访问命令（为了简洁我们在这里只谈到表，但是这种方式对其他类型的命名对象同样有效，例如类型和函数）。

还可以使用下面的形式指定表名：

database.schema.table

，但是目前该形式只是为了与SQL标准兼容。在瀚高数据库中如果写数据库的名称，必须是我们正在连接的数据库，不能指定其他数据库名称。

因此，如果要在myschema模式中创建一个表，可用：

CREATE TABLE myschema.mytable ( ·

…

);

要删除一个空模式（其中的所有对象已经被删除），可用：

DROP SCHEMA myschema;

要删除一个模式以及其中包含的所有对象，可用：

DROP SCHEMA myschema CASCADE;

详细信息请参考第 4.14 节。

创建一个由其他用户拥有的模式语法是：

CREATE SCHEMA schema\_name AUTHORIZATION user\_name;

上述示例中可以省略模式名称，在此种情况下模式名称将会使用用户名，参见第 4.9.6 节。

以pg\_开头的模式名是系统保留名称，用户无法创建。

### 4.7.2. 公共模式

在前面的小节中，我们创建的表都没有指定任何模式名称。默认情况下这些表（以及其他对象）会自动的被放入一个名为“public”的模式中。任何新数据库都包含一个这样的模式。因此，下面的命令是等效的：

CREATE TABLE products ( … );

以及：

CREATE TABLE public.products ( … );

### 4.7.3. 模式搜索路径

限定名写起来很冗长，通常不建议在应用中使用特定模式名称。因此，通常只用表的名称来引用表。系统将沿着一条搜索路径来决定该名称指的是哪个表。搜索路径是一个模式列表，按照列表中模式的顺序来搜索每个模式中是否存在该名称的表，第一个匹配到的表将作为真正被引用的表。如果在搜索路径中没有匹配到该表，即使在数据库的其他模式中存在匹配的表名数据库也会报错。

搜索路径中的第一个模式被称为当前模式。除了是第一个被匹配的模式，如果CREATE TABLE命令没有指定模式名，它也将作为新创建表所在的模式。

使用下面的命令显示当前搜索路径，：

SHOW search\_path;

在默认设置下这返回：

search\_path

\-#-#-#-#-#-#-#

“$user”, public

第一项说明一个和当前用户同名的模式会被搜索。如果不存在这个模式，该项将被忽略。第二项表示公共模式。

搜索路径中的第一个模式是创建新对象的默认存储位置。这就是默认情况下对象会被创建在公共模式中的原因。当对象在任何其他没有模式限定的环境中被引用（表修改、数据修改或查询命令）时，搜索路径将被遍历直到找到一个匹配对象。因此，在默认配置中，任何非限定访问将只能指向公共模式。

要把新模式放在搜索路径中，我们可以使用：

SET search\_path TO myschema,public;

设置成功后删除该表时不需要再指定模式名称：

DROP TABLE mytable;

同样，由于myschema是路径中的第一个元素，新对象会默认创建在该模式中。

我们也可以这样写：

SET search\_path TO myschema;

执行成功后会把公共模式从搜索路径中删除，此时如果未显式指定模式名称，系统不会再去访问公共模式。公共模式是默认存在的，也可以被删除。

其他操作模式搜索路径的方法请见第 8.25 节。

搜索路径对于数据类型名称、函数名称和操作符名称的作用与表名一样。数据类型和函数名称可以使用和表名完全相同的限定方式。如果我们需要在一个表达式中写一个限定的操作符名称，必须写成如下形式：

OPERATOR(schema.operator)

这是为了避免句法歧义。例如：

SELECT 3 OPERATOR(pg\_catalog.+) 4;

### 4.7.4. 模式和权限

默认情况下，用户不能访问不属于他们的模式中的任何对象。要允许这种行为，模式的拥有者必须在该模式上授予USAGE权限。为了允许用户使用方案中的对象，可能还需要根据对象授予额外的权限。

一个用户也可以被允许在其他某人的模式中创建对象。要允许这种行为，模式上的CREATE权限必须被授予。注意在默认情况下，所有人都拥有在public模式上的CREATE和USAGE权限。

这使得用户能够连接到一个给定数据库并在它的public模式中创建对象。回收这一特权的使用模式调用：

REVOKE CREATE ON SCHEMA public FROM PUBLIC;

（第一个“public”是方案，第二个“public”指的是“每一个用户”。第一种是一个标识符，第二种是一个关键词，所以两者的大小写不同。请回想第 3.1.1 节中的指导方针。）

### 4.7.5. 系统目录模式

除public和用户创建的模式之外，每一个数据库还包括一个pg\_catalog模式，它包含了系统表和所有内建的数据类型、函数以及操作符。pg\_catalog总是搜索路径的一个有效部分。如果没有在路径中显式地包括该模式，它将在路径中的模式之前被搜索。这保证了内建的名称总是能被找到。然而，如果我们希望用用户定义的名称重载内建的名称，可以显式的将pg\_catalog放在搜索路径的末尾。

由于系统表名称以pg\_开头，最好还是避免使用这样的名称，以避免和未来新版本中 可能出现的系统表名发生冲突。系统表将继续采用以pg\_开头的方式，这样它们不会 与非限制的用户表名称冲突。

### 4.7.6. 使用模式

模式能够以多种方式组织数据.secure schema usage pattern防止不受信任的用户更改其他用户查询的行为。 当数据库不使用安全模式使用方式时，希望安全地查询该数据库的用户将在每个会话开始时采取保护操作。 具体的说，他们将通过设置search\_path到空字符串或在其它情况下从search\_path中删除非超级用户可写的模式来开始每个会话。 默认配置可以很容易的支持一些使用方式。

• 将普通用户约束在其私有的方案中。要实现这一点，发出REVOKE CREATE ON SCHEMA public FROM PUBLIC，并且为每一个用户创建一个用其用户名命名的方案。 回想一下以$user开头的默认搜索路径，该路径解析为用户名。 因此，如果每个用户都有单独的模式，则默认情况下他们访问自己的模式。 在不受信任的用户已经登录的数据库中采用此模式后，请考虑审计名字类似于模式pg\_catalog中的对象的公共模式。 此方式是一种安全模式的使用方式，除非不受信任的用户是数据库所有者或拥有CREATEROLE权限，在这种情况下没有安全模式使用方式存在。

• 从默认搜索路径中删除公共模式，通过修改postgresql.conf或通过发出ALTER ROLE ALL SET search\_path =”$user”。 每一个都保留在公共模式中创建对象的能力，但是只有符合资格的名称才会选择这些对象。 虽然符合资格的表引用是可以的，但是要调用公共模式中的函数will be unsafe or unreliable。 如果在公共模式中创建函数或扩展，请改用第一个方式。 否则，与第一个模式一样，这是安全的，除非不受信任的用户是数据库所有者或拥有CREATEROLE权限。

• 保持默认。所有用户都隐式地访问公共模式。这模拟了方案根本不可用的情况，可以用于从无模式感知的世界平滑过渡。 但是，这绝不是一个安全的模式。只有当数据库仅有单个用户或者少数相互信任的用户时，才可以接受。

对于任何一种模式，为了安装共享的应用（所有人都要用其中的表，第三方提供的额外函数，等等），可把它们放在单独的方案中。记住授予适当的特权以允许其他用户访问它们。然后用户可以通过以方案名限定名称的方式来引用这些额外的对象，或者他们可以把额外的方案放在自己的搜索路径中。

### 4.7.7. 可移植性

在SQL标准中，在由不同用户拥有的同一个模式中的对象是不存在的。此外，某些实现不允许创建与拥有者名称不同名的模式。事实上，在那些仅实现了标准中基本模式支持的数据库中，模式和用户的概念是等同的。因此，很多用户认为限定名称实际上是由user\_name.table\_name组成的。如果我们为每一个用户都创建了一个模式，瀚高数据库实际也是这样认为的。

同样，在SQL标准中也没有public模式的概念。为了最大限度的与标准一致，我们不应使用（甚至是删除）public模式。

当然，某些SQL数据库系统可能根本没有实现方案，或者提供允许跨数据库访问的名字空 。

## 4.8. 继承

瀚高数据库实现了表继承，这对数据库设计者来说是一种有用的工具（SQL:1999及其后的版本定义了一种类型继承特性，但和这里介绍的继承有很大的不同）。

让我们从一个例子开始：假设我们要为城市建立一个数据模型。每一个州有很多城市，但是只有一个首府。我们希望能够快速地检索任何特定州的首府城市。这可以通过创建两个表来实现：一个用于州首府，另一个用于不是首府的城市。然而，当我们想要查看一个城市的数据（不管它是不是一个首府）时会发生什么？继承特性将有助于解决这个问题。我们可以将capitals表定义为继承自cities表：

CREATE TABLE cities (

name text,

population float,

altitude int -# in feet

);

CREATE TABLE capitals (

state char(2)

) INHERITS (cities);

在这种情况下，capitals表继承了它的父表cities的所有列。州首府还有一个额外的列state用来表示它所属的州。

在瀚高数据库中，一个表可以从0个或者多个其他表继承，而对一个表的查询则可以引用一个表的所有行或者该表的所有行加上它所有的后代表。默认情况是后一种行为。例如，下面的查询将查找所有海拔高于500尺的城市的名称，包括州首府：

SELECT name, altitude

FROM cities

WHERE altitude > 500;

对于来自瀚高数据库教程（见第 1.1 节）的例子数据，它将返回：

name | altitude

\-#-#-#-#-#-+-#-#-#-#-#

Las Vegas | 2164

Mariposa | 1953

Madison | 845

在另一方面，下面的查询将找到海拔超过500尺且不是州首府的所有城市：

SELECT name, altitude

FROM ONLY cities

WHERE altitude > 500;

name | altitude

\-#-#-#-#-#-+-#-#-#-#-#

Las Vegas | 2164

Mariposa | 1953

这里的ONLY关键词指示查询只被应用于cities上，而其他在继承层次中位于cities之下的其他表都不会被该查询涉及。很多我们已经讨论过的命令（如SELECT、UPDATE和DELETE）都支持ONLY关键词。

我们也可以在表名后写上一个\*来显式地将后代表包括在查询范围内：

SELECT name, altitude

FROM cities\*

WHERE altitude > 500;

写\*不是必需的，因为这种行为总是默认的。不过，为了兼容可以修改默认值的较老版本，现在仍然支持这种语法。

在某些情况下，我们可能希望知道一个特定行来自于哪个表。每个表中的系统列tableoid可以告诉我们行来自于哪个表：

SELECT c.tableoid, c.name, c.altitude

FROM cities c

WHERE c.altitude > 500;

将会返回：

tableoid | name | altitude

\-#-#-#-#-#+-#-#-#-#-#-+-#-#-#-#-#

139693 | Las Vegas | 2164

139693 | Mariposa | 1953

139698 | Madison | 845

（如果重新生成这个结果，可能会得到不同的OID数字。）通过与pg\_class进行连接可以看到实际的表名：

SELECT p.relname, c.name, c.altitude

FROM cities c, pg\_class p

WHERE c.altitude > 500 AND c.tableoid = p.oid;

将会返回：

relname | name | altitude

\-#-#-#-#-#+-#-#-#-#-#-+-#-#-#-#-#

cities | Las Vegas | 2164

cities | Mariposa | 1953

capitals | Madison | 845

另一种得到同样效果的方法是使用regclass别名类型，它将象征性地打印出表的 OID：

SELECT c.tableoid::regclass, c.name, c.altitude

FROM cities c

WHERE c.altitude > 500;

继承不会自动地将来自INSERT或COPY命令的数据传播到继承层次中的其他表中。在我们的例子中，下面的INSERT语句将会失败：

INSERT INTO cities (name, population, altitude, state)

VALUES (‘Albany’, NULL, NULL, ‘NY’);

我们也许希望数据能以某种方式被引入到capitals表中，但是这不会发生：INSERT总是向指定的表中插入。在某些情况下，可以通过使用一个规则（见第 40 章）来将插入动作重定向。但是这对上面的情况并没有帮助，因为cities表根本就不包含state列，因而这个命令将在触发规则之前就被拒绝。

父表上的所有检查约束和非空约束都将自动被它的后代所继承，除非显式地指定了NO INHERIT子句。其他类型的约束（唯一、主键和外键约束）则不会被继承。

一个表可以从多个父表继承，在这种情况下它拥有父表们所定义的列的并集。任何定义在子表上的列也会被加入其中。如果在这个集合中出现重名列，那么这些列将被“合并”，这样在子表中只会有一个这样的列。重名列能被合并的前提是这些列必须具有相同的数据类型，否则会导致错误。可继承的检查约束和非空约束会以类似的方式被合并。例如，如果合并成一个合并列的任一列定义被标记为非空，则该合并列会被标记为非空。如果检查约束的名称相同，则他们会被合并，但如果它们的条件不同则合并会失败。

表继承通常是在子表被创建时建立，使用CREATE TABLE语句的INHERITS子句。已经创建的表也可以增加父表，使用ALTER TABLE的INHERIT子句。要这样做，新的子表必须已经包括和父表相同名称和数据类型的列。子表还必须包括和父表相同的检查约束和检查表达式。相似地，继承关系也可以使用ALTER TABLE的 NO INHERIT选项从一个子表中移除。动态增加和移除继承链接可以用于实现表分区（见第 5.11 节）。

一种创建一个未来将被用做子表的新表的方法是在CREATE TABLE中使用LIKE子句。这将创建一个和源表具有相同列的新表。如果源表上定义了任何CHECK约束，LIKE的INCLUDING CONSTRAINTS选项可以用来让新的子表也包含和父表相同的约束。

当有任何一个子表存在时，父表不能被删除。当子表的列或者检查约束继承于父表时，它们也不能被删除或修改。如果希望移除一个表和它的所有后代，一种简单的方法是使用CASCADE选项删除父表（见第 5.14 节）。

ALTER TABLE将会把列的数据定义或检查约束上的任何变化沿着继承层次向下传播。同样，删除被其他表依赖的列只能使用CASCADE选项。ALTER TABLE对于重名列的合并和拒绝遵循与CREATE TABLE同样的规则。

继承的查询仅在父表上执行访问权限检查。例如，在cities表上授予UPDATE权限也隐含着通过cities访问时在capitals表中更新行的权限。这保留了数据在父表中的样子。但是如果没有额外的授权，则不能直接更新capitals表。 此规则的两个例外是TRUNCATE 和 LOCK TABLE，总是检查子表的权限，不管它们是直接处理还是通过在父表上执行的命令递归处理。

以类似的方式，父表的行安全性策略（见第 4.8 节）适用于继承查询期间来自于子表的行。 只有当子表在查询中被明确提到时，其策略（如果有）才会被应用，在那种情况下，附着在其父表上的任何策略都会被忽略。

外部表（见第 4.12 节）也可以是继承层次中的一部分，既可以作为父表也可以作为子表，就像常规表一样。如果一个外部表是继承层次的一部分，那么任何不被该外部表支持的操作也不被整个层次所支持。

### 4.8.1. 警告

注意并非所有的SQL命令都能在继承层次上执行。用于数据查询、数据修改或模式修改（例如SELECT、UPDATE、DELETE、大部分ALTER TABLE，但INSERT或ALTER TABLE … RENAME不在此列）的命令会默认将子表包含在内并且支持ONLY记号来排除子表。数据库维护的命令（如REINDEX、VACUUM）只工作在独立的、物理的表上并且不支持在继承层次上的递归。每个命令相应的行为请参见它们的参考页（SQL 命令）。

继承特性的一个严格的限制是索引（包括唯一约束）和外键约束值应用在单个表上而非它们的继承子女。在外键约束的引用端和被引用端都是这样。因此，按照上面的例子：

• 如果我们声明cities.name为UNIQUE或者PRIMARY KEY，这将不会阻止capitals表中拥有和cities中城市同名的行。而且这些重复的行将会默认显示在cities的查询中。事实上，capitals在默认情况下是根本不能拥有唯一约束的，因此能够包含多个同名的行。我们可以为capitals增加一个唯一约束，但这无法阻止相对于cities的重复。

• 相似地，如果我们指定cities.name REFERENCES某个其他表，该约束不会自动地传播到capitals。在此种情况下，我们可以在capitals上手工创建一个相同的REFERENCES约束。

• 指定另一个表的列REFERENCES cities(name)将允许其他表包含城市名称，但不会包含首府名称。此示例中不建议使用该方案。

## 4.9. 表分区

瀚高数据库支持基本的表分区。本小节介绍为何以及怎样把表分区作为数据库设计的一部分。

### 4.9.1. 概述

划分（分区）指的是将逻辑上的一个大表分成一些小的物理上的片。划分有很多益处：

• 在某些情况下查询性能能够显著提升，特别是当那些访问压力大的行被划分在一个分区或者少数几个分区时。划分可以取代索引的主导列、减小索引尺寸以及使索引中访问压力大的部分更有可能被放在内存中。

• 当查询或更新访问一个分区的大部分行时，可以通过该分区上的一个顺序扫描来取代分散到整个表上的索引和随机访问，这样可以改善性能。

• 如果批量操作的需求是在分区设计时就规划好的，则批量装载和删除可以通过增加或者删除分区来完成。执行ALTER TABLE DETACH PARTITION或者使用DROP TABLE删除一个分区远快于批量操作。这些命令也完全避免了批量DELETE导致的VACUUM开销。

• 很少使用的数据可以被迁移到便宜且较慢的存储介质上。

当一个表非常大时，划分所带来的好处是显而易见的。一个表何种情况下会从划分获益取决于应用，一般当表的尺寸超过了数据库服务器物理内存时，划分会为表带来好处。

瀚高数据库对下列划分形式提供支持：

**范围分区**

根据一个关键列或一组列将表划分为多个“范围”，不同的分区的范围之间没有重叠。例如，我们可以根据日期范围划分，或者根据特定业务对象的标识符划分。

**列表分区**

通过显式地列出每一个分区中出现的键值来划分表。

**哈希分区**

通过为每个分区指定模数和余数来对表进行分区。每个分区所持有的行都满足：分区键的值除以为其指定的模数将产生为其指定的余数。

如果你的应用需要使用上面所列之外的分区形式，可以使用诸如继承和UNION ALL视图之类的替代方法。这些方法很灵活，但是却缺少内置分区的一些性能优势。

### 4.9.2. 声明式划分

瀚高数据库提供了一种方法指定如何把一个表划分为分区的片段。被划分的表被称作分区表。这种说明由分区方法以及要被用作分区键的列或者表达式列表组成。

所有被插入到分区表的行将被基于分区键的值路由到分区中。每个分区都有一个由其分区边界定义的数据子集。当前支持的分区方法是范围、列表以及哈希。

分区本身也可能被定义为分区表，被称为子分区。分区可以有自己的与其他分区不同的索引、约束以及默认值。创建分区表及分区的更多细节请见CREATE TABLE。

不支持将常规表转换成分区表，反之亦然。不过，可以把一个包含数据的常规表或者分区表作为分区加入到另一个分区表，或者从分区表中移走一个分区并且把它变成一个独立的表。有关ATTACH PARTITION和DETACH PARTITION子命令的内容请见ALTER TABLE。

子分区在内部以继承的方式链接到分区表，不过无法对声明式分区表或其分区使用继承的某些特性（下文讨论）。例如，分区不能有除其所属分区表之外的父表，一个常规表也不能从分区表继承使得后者成为其父表。这意味着分区表及其分区不会参与到与常规表的继承关系中。由于分区表及其分区组成的分区层次仍然是一种继承层次，所有第 4.10 节中所述的继承的普通规则也适用，不过有一些例外，尤其是：

• 分区表的CHECK约束和NOT NULL约束总是会被其所有的分区所继承。不允许在分区表上创建标记为NO INHERIT的CHECK约束。

• 只要分区表中不存在分区，则支持使用ONLY仅在分区表上增加或者删除约束。一旦分区存在，那样做就会导致错误，因为当分区存在时是不支持仅在分区表上增加或删除约束的。

不过，分区表本身上的约束可以被增加（如果它们不出现在父表中）和删除。

• 由于分区表并不直接拥有任何数据，尝试在分区表上使用TRUNCATE

ONLY将总是返回错误。

• 分区不能有在父表中不存在的列。在使用CREATE TABLE创建分区时不能指定列，在事后使用ALTER TABLE时也不能为分区增加列。只有当表的列正好匹配父表时，才能使用ALTER TABLE … ATTACH PARTITION将它作为分区加入。

• 如果NOT NULL约束在父表中存在，那么就不能删除分区的列上对应的NOT NULL约束。

分区也可以是外部表，不过它们有一些普通表没有的限制，详情请见CREATE FOREIGN TABLE。

#### 4.9.2.1. 分区表分类

#### 4.9.2.1.1. 范围分区

在范围分区中，分区规则根据KEY按照不同的范围映射到不同的分区中，每个分区的范围都是由一个上限值和下限值来决定，这两个值是在创建分区表时定义的。

范围分区的KEY可由多个列（最多可由32个列）组成。值得一提的是，当KEY由多个列组成时，除了第一列的各分区约束范围之间不能重叠外，其他列的分区范围可以有重叠。

范围分区适用于组成KEY是连续的可以根据需要设定上下限的列。实际上，在分区表的应用中，范围分区是最普遍最常用的分区类型。

范围分区的KEY可以支持多个字段组成(最多32个字段)。

**语法**

创建分区语法一：

主表语法:

CREATE TABLE 表名 ( \[{ 列名称 数据\_类型} \[, … \] \] )

PARTITION BY RANGE ( \[{ 列名称 } \[, …\] \] );

参数说明：

RANGE关键字表示进行范围分区

RANGE后面跟的多个列是组成的KEY

分区语法:

CREATE TABLE 表名 PARTITION OF 主表 FOR VALUES

FROM{ ( 表达式 \[, …\] ) | MINVALUE } \[, …\]

TO { ( 表达式 \[, …\] ) | MAXVALUE } \[, …\]

\[ TABLESPACE 表空间名 \];

参数说明:

FROM … TO 表示分区的起始值和结束值。

MINVALUE / MAXVALUE\* 表示无限小值和无限大值。

默认FROM后面的值是包括值分区的约束内，TO后面的值不包括。

创建分区语法二：

CREATE TABLE table\_name ( column\_name TYPE ) PARTITION BY RANGE ( column\_name )

(

PARTITION partition\_name\_1 FOR VALUES FROM (lower\_bound) TO (upper\_bound),

PARTITION partition\_name\_2 FOR VALUES FROM (lower\_bound) TO (upper\_bound),

PARTITION partition\_name\_3 DEFAULT

/\* more partition definitions follow …\*/

);

范围分区语法二将主表分区与分区语法进行融合，在主表分区语法后面增加()括号，括号后的内容为具体的分区划分，使用关键字PARTITION指定分区的名字， FOR VALUES FORM…TO 设置分区的范围.

范围分区语法一和范围分区语法二相比较，语法二更加简洁。

示例

1. 单列作为KEY值

范围分区语法一：

create table test(n int) partition by range(n);

create table test\_1 partition of test for values from (MINVALUE) to (10);

create table test\_2 partition of test for values from (10) to (100);

create table test\_3 partition of test for values from (100) to (1000);

create table test\_4 partition of test for values from (1000) to (10000);

范围分区语法二：

create table test(n int) partition by range(n)

(

PARTITION test\_1 for values from (MINVALUE) to (10),

PARTITION test\_2 for values from (10) to (100),

PARTITION test\_3 for values from (100) to (1000),

PARTITION test\_4 for values from (1000) to (10000),

PARTITION test\_default DEFAULT

);

可以\\d+ test显示主表及分区有关信息：

highgo =# \\d+ test |

Partition key: RANGE (n)

Partitions:

test\_1 FOR VALUES FROM (MINVALUE) TO (10),

test\_2 FOR VALUES FROM (10) TO (100),

test\_3 FOR VALUES FROM (100) TO (1000),

test\_4 FOR VALUES FROM (1000) TO (10000)

\\d+ test\_2可以显示分区test\_2的内在约束关系：

highgo =# \\d+ test\_2

Partition of: test FOR VALUES FROM (10) TO (100)

Partition constraint: ((n IS NOT NULL) AND (n >= 10) AND (n < 100))

1. 多列作为KEY值,下面以2列作为KEY值为例：

范围分区语法一:

create table test(n1 int, n2 int) partition by range(n1, n2);

create table test\_1 partition of test for values from (0, 0) to (10, 100);

create table test\_2 partition of test for values from (10, 100) to (20, 200);

create table test\_3 partition of test for values from (20, 200) to (30, 300);

create table test\_4 partition of test for values from (30, 300) to (40, 400);

范围分区语法二:

create table test(n1 int, n2 int) partition by range(n1, n2)

(

PARTITION test\_1 for values from (0, 0) to (10, 100),

PARTITION test\_2 for values from (10, 100) to (20, 200),

PARTITION test\_3 for values from (20, 200) to (30, 300),

PARTITION test\_4 for values from (30, 300) to (40, 400),

PARTITION test\_default DEFAULT

);

同样\\d+ test 可以显示主表及分区信息：

highgo =# \\d+ test

Partition key: RANGE (n1, n2)

Partitions: test\_1 FOR VALUES FROM (0, 0) TO (10, 100),

test\_2 FOR VALUES FROM (10, 100) TO (20, 200),

test\_3 FOR VALUES FROM (20, 200) TO (30, 300),

test\_4 FOR VALUES FROM (30, 300) TO (40, 400)

\\d+ test\_2 显示分区test\_2的信息：

highgo=# \\d+ test\_2

Partition of: test FOR VALUES FROM (10, 100) TO (20, 200)

Partition constraint: ((n1 IS NOT NULL) AND

(n2 IS NOT NULL) AND

((n1 > 10) OR ((n1 = 10) AND (n2 >= 100))) AND

((n1 < 20) OR ((n1 = 20) AND (n2 < 200))))

需要注意的是，两列作为KEY的话，分区约束条件并不是单纯的10 =< n1 < 20 且 100 =< n2 < 200。这是一个组合约束条件。

#### 4.9.2.1.2. 列表分区

列表分区的KEY只能包含一个。

在列表分区中，分区规则是由KEY的一系列离散值组成。也就是向列表分区插入数据时，只有等于这些离散值时才会执行插入。

很明显，当KEY值是非连续的，离散的时候，比较适合使用列表分区。

**语法**

列表分区语法一:

创建主表语法：

CREATE TABLE 表名 ( \[{ 列名称 数据\_类型} \[, … \] \] ) PARTITION BY LIST( { 列名称 } );

参数说明：

LIST关键字表示进行列表分区。

LIST关键字后只能有一个字段。

创建分区语法：

CREATE TABLE 表名 PARTITION OF 主表 FOR VALUES

IN ( 表达式 \[, …\] ) \[ TABLESPACE 表空间名 \];

参数说明：

IN关键字表示列表分区约束的离散值。

列表分区语法二:

CREATE TABLE table\_name ( column\_name TYPE ) PARTITION BY LIST ( column\_name )

(

PARTITION partition\_name\_1 FOR VALUES IN ( list\_partition\_definition ),

PARTITION partition\_name\_2 FOR VALUES IN ( list\_partition\_definition ),

PARTITION partition\_name\_3 DEFAULT

/\* more partition definitions follow \*/

);

列表分区语法二融合列表分区的主表创建和分区创建两个语法，通过在主表创建后增加()括号，在括号内使用关键字PARTITION name FOR VALUES IN 进行列表划分。

比较列表分区语法一和二,语法二更简洁.

示例

列表分区语法一:

CREATE TABLE sales (product\_id int, saleroom int, province text) PARTITION BY LIST(province);

CREATE TABLE sales\_east PARTITION OF sales FOR VALUES IN (‘山东’,’江苏’,’上海’);

CREATE TABLE sales\_west PARTITION OF sales FOR VALUES IN (‘山西’,’陕西’,’四川’);

CREATE TABLE sales\_north PARTITION OF sales FOR VALUES IN (‘北京’,’河北’,’辽宁’);

CREATE TABLE sales\_south PARTITION OF sales FOR VALUES IN (‘广东’,’福建’);

列表分区语法二:

CREATE TABLE sales (product\_id int, saleroom int, province text) PARTITION BY LIST(province)

(

PARTITION sales\_east FOR VALUES IN (‘山东’,’江苏’,’上海’),

PARTITION sales\_west FOR VALUES IN (‘山西’,’陕西’,’四川’),

PARTITION sales\_north FOR VALUES IN (‘北京’,’河北’,’辽宁’),

PARTITION sales\_south FOR VALUES IN (‘广东’,’福建’),

PARTITION sales\_default DEFAULT

);

\\d+ sales；显示主表及分区信息：

highgo=# \\d+ sales

Partition key: LIST (province)

Partitions: sales\_east FOR VALUES IN (‘山东’, ‘江苏’, ‘上海’),

sales\_north FOR VALUES IN (‘北京’, ‘河北’, ‘辽宁’),

sales\_south FOR VALUES IN (‘广东’, ‘福建’),

sales\_west FOR VALUES IN (‘山西’, ‘陕西’, ‘四川’)

\\d+ sales\_east;显示分区约束信息：

highgo=# \\d+ sales\_east

Partition of: sales FOR VALUES IN (‘山东’, ‘江苏’, ‘上海’)

Partition constraint: ((province IS NOT NULL) AND (province = ANY (ARRAY\[‘山东’::text, ‘江苏’::text, ‘上海’::text\])))

Access method: heap

#### 4.9.2.1.3. 哈希分区

所谓哈希分区就是分区规则将分区创建的KEY根据内部的哈希运算结果然后映射到相应的分区中去。具体的映射关系为，插入数据的KEY值在进行哈希运算等算法后会返回一个序号值，然后拿该序号值和创建分区时给分区分配的序号值比较，相等则插入相应的分区。

哈希分区的KEY目前仅支持一个字段。

HASH分区适用于无法有效划分分区范围，即不适用于范围分区和列表分区的场景，比如由很长的字符串组成的ID号，并且查询时以ID做为查询条件之一，那么此时就比较合适对其进行哈希分区。哈希分区还有一个用途就是起到对数据进行平均分配到各个分区中的效果，特别是在大数据量且KEY值没有重复的情况下。

**语法**

Hash分区语法一:

创建主表：

CREATE TABLE table\_name ( column\_name data\_type )

PARTITION BY HASH ( { column\_name } )

参数说明：

table\_name：分区表主表名

column\_name：分区表字段，分区key值

创建哈希分区表子表:

CREATE TABLE table\_name PARTITION OF parent\_table

FOR VALUES

WITH ( MODULUS numeric\_literal, REMAINDER numeric\_literal )

参数：

table\_name：分区子表名

parent\_table: 分区父表名

numeric\_literal：分区key值

说明：

进行取模运算，insert\_value % modulus = remainder

MODULUS：分区数

REMAINDER：余数

Hash分区语法二:

CREATE TABLE table\_name ( column\_name TYPE ) PARTITION BY HASH ( column\_name )

(

PARTITION partition\_name\_1 FOR VALUES WITH ( hash\_partition\_definition ),

PARTITION partition\_name\_2 FOR VALUES WITH ( hash\_partition\_definition ),

/\* more partition definitions follow \*/

);

Hash分区语法二融合Hash分区语法一的主表创建和分区创建两个语法，通过在主表创建后增加()括号，在括号内使用关键字PARTITION name FOR VALUES WITH 进行Hash划分.

比较Hash分区语法一和二,语法二更简洁.

示例：

Hash分区语法一: 是否需要修改create table的语法？？

create table test\_hash(id int, date date) partition by hash(id);

create table test\_hash\_1 partition of test\_hash for values with(modulus 2, remainder 0);

create table test\_hash\_2 partition of test\_hash for values with(modulus 2, remainder 1);

Hash分区语法二:是否需要增加create table的语法

create table test\_hash(id int, date date) partition by hash(id)

(

PARTITION test\_hash\_1 FOR VALUES WITH (modulus 2, remainder 0 ),

PARTITION test\_hash\_2 FOR VALUES WITH (modulus 2, remainder 1 )

);

\\d+ test\_hash 显示主表及分区信息

Table “public.test\_hash”

Column | Type | Collation | Nullable | Default | Storage | Stats target | Description

——–+———+———–+———-+———+———+————–+————-

id | integer | | | | plain | |

date | date | | | | plain | |

Partition key: HASH (id)

Partitions: test\_hash\_1 FOR VALUES WITH (modulus 2, remainder 0),

test\_hash\_2 FOR VALUES WITH (modulus 2, remainder 1)

\\d+ test\_hash\_1

Table “public.test\_hash\_1”

Column | Type | Collation | Nullable | Default | Storage | Stats target | Description

——–+———+———–+———-+———+———+————–+————-

id | integer | | | | plain | |

date | date | | | | plain | |

Partition of: test\_hash FOR VALUES WITH (modulus 2, remainder 0)

Partition constraint: satisfies\_hash\_partition(‘16603’::oid, 2, 0, id)

insert into test\_hash select generate\_series(1, 10), current\_date;

select tableoid::regclass, \* from test\_hash;

tableoid | id | date

————-+—-+————

test\_hash\_1 | 3 | 2018-10-22

test\_hash\_1 | 4 | 2018-10-22

test\_hash\_1 | 7 | 2018-10-22

test\_hash\_1 | 10 | 2018-10-22

test\_hash\_2 | 1 | 2018-10-22

test\_hash\_2 | 2 | 2018-10-22

test\_hash\_2 | 5 | 2018-10-22

test\_hash\_2 | 6 | 2018-10-22

test\_hash\_2 | 8 | 2018-10-22

test\_hash\_2 | 9 | 2018-10-22

(10 rows)

注意：

该版本Hash分区表不支持混合多层嵌套模式，只允许Hash分区表嵌套Hash分区表。

#### 4.9.2.2. 例子

假定我们正在为一个大型的冰激凌公司构建数据库。该公司每天测量最高温度以及每个区域的冰激凌销售情况。概念上，我们想要一个这样的表：

CREATE TABLE measurement (

city\_id int not null,

logdate date not null,

peaktemp int,

unitsales int

);

我们知道大部分查询只会访问上周的、上月的或者上季度的数据，因为这个表的主要用途是为管理层准备在线报告。为了减少需要被存放的旧数据量，我们决定只保留最近3年的数据。在每个月的开始我们将去除掉最早的那个月的数据。在这种情况下我们可以使用分区技术来帮助我们满足对measurement表的所有不同需求。

要在这种情况下使用声明式分区，可采用下面的步骤：

\\1. 通过指定PARTITION BY子句把measurement表创建为分区表，该子句包括分区方法（这个例子中是RANGE）以及用作分区键的列列表。

CREATE TABLE measurement (

city\_id int not null,

logdate date not null,

peaktemp int,

unitsales int

) PARTITION BY RANGE (logdate);

可以考虑是否在分区键中使用多列进行范围分区。通常多列的范围分区会创建很多数据量较小的分区。另一方面，使用一个或者较少的列作为分区键创建的分区数量较少，但是分区粒度会比较粗。

\\2. 创建分区。每个分区的定义必须指定对应于父表的分区方法和分区键的边界。注意，如果指定的边界使得新分区的值会与已有分区中的值重叠，则会导致错误。向父表中插入无法映射到任何现有分区的数据将会导致错误，这种情况下应该手工增加一个合适的分区。

分区以普通瀚高数据库表（或者可能是外部表）的方式创建。可以为每个分区单独指定表空间和存储参数。

创建子分区时会自动为子分区表创建相应的约束。

CREATE TABLE measurement\_y2006m02 PARTITION OF measurement

FOR VALUES FROM (‘2006-02-01’) TO (‘2006-03-01’);

CREATE TABLE measurement\_y2006m03 PARTITION OF measurement

FOR VALUES FROM (‘2006-03-01’) TO (‘2006-04-01’);

…

CREATE TABLE measurement\_y2006m11 PARTITION OF measurement

FOR VALUES FROM (‘2006-11-01’) TO (‘2006-12-01’);

CREATE TABLE measurement\_y2006m12 PARTITION OF measurement

FOR VALUES FROM (‘2006-12-01’) TO (‘2008-01-01’)

TABLESPACE fasttablespace;

CREATE TABLE measurement\_y2008m01 PARTITION OF measurement

FOR VALUES FROM (‘2008-01-01’) TO (‘2008-02-01’)

WITH (parallel\_workers = 4)

TABLESPACE fasttablespace;

为了实现子分区，在创建分区的命令中指定PARTITION BY子句，例如：

CREATE TABLE measurement\_y2006m02 PARTITION OF measurement

FOR VALUES FROM (‘2006-02-01’) TO (‘2006-03-01’)

PARTITION BY RANGE (peaktemp);

在创建了measurement\_y2006m02的分区之后，任何被插入到measurement中且被映射到measurement\_y2006m02的数据（或者直接被插入到measurement\_y2006m02的数据，假定它满足这个分区的分区约束）将被基于peaktemp列进一步重定向到measurement\_y2006m02的一个分区。指定的分区键可以与父亲的分区键重叠，不过在指定子分区的边界时要注意它接受的数据集合是分区自身边界允许的数据集合的一个子集，系统不会对此进行检查。

\\3. 在分区表的键列上创建一个索引，还有其他需要的索引（键索引并不是必需的，但是大部分场景中建议使用）。这会自动在每个分区上创建一个索引，并且后来创建或者附着的任何分区也将会包含索引。

CREATE INDEX ON measurement (logdate);

\\4. 确保enable\_partition\_pruning配置参数在postgresql.conf中没有被禁用。如果被禁用，查询将不会按照想要的方式被优化。

在上面的例子中，我们会每个月创建一个新分区，因此写一个脚本来自动生成所需的DDL会更好。

#### 4.9.2.3. 分区维护

通常在初始定义分区表时建立的分区并非保持不变的。移除旧分区的数据并且为新数据周期性地增加新分区的需求比比皆是。分区的最大好处之一就是可以通过操作分区来达到这一目的。

移除旧数据最简单的选择是删除不再需要的分区：

DROP TABLE measurement\_y2006m02;

这可以非常快地删除数百万行记录，因为它不需要逐个删除每个记录。不过要注意上面的命令需要在父表上拿到ACCESS EXCLUSIVE锁。

另一种更推荐的方式是把分区从分区表中移除，但是保留它作为一个独立的表：

ALTER TABLE measurement DETACH PARTITION measurement\_y2006m02;

这允许在它被删除之前执行进一步的操作。例如，可以在这时候使用COPY、pg\_dump或类似工具对数据进行备份。也可以趁此机会在表上执行其他数据操作或者运行报表。

类似地，我们可以增加一个新分区来处理新数据。我们可以在分区表中创建一个空分区，就像上面创建的初始分区那样：

CREATE TABLE measurement\_y2008m02 PARTITION OF measurement

FOR VALUES FROM (‘2008-02-01’) TO (‘2008-03-01’)

TABLESPACE fasttablespace;

另外一种选择是，有时候在分区结构之外创建新表更加方便，然后将它作为一个合适的分区。这需要先对数据进行装载、检查和转换，然后再附加到分区表中：

CREATE TABLE measurement\_y2008m02

(LIKE measurement INCLUDING DEFAULTS INCLUDING CONSTRAINTS)

TABLESPACE fasttablespace;

ALTER TABLE measurement\_y2008m02 ADD CONSTRAINT y2008m02

CHECK ( logdate >= DATE ‘2008-02-01’ AND logdate < DATE ‘2008-03-01’ );

\\copy measurement\_y2008m02 from ‘measurement\_y2008m02’

\-# possibly some other data preparation work

ALTER TABLE measurement ATTACH PARTITION measurement\_y2008m02

FOR VALUES FROM (‘2008-02-01’) TO (‘2008-03-01’ );

在运行ATTACH PARTITION命令之前，推荐在要被附加的表上创建一个CHECK约束来匹配期望的分区约束条件。这样，系统将能够跳过扫描来验证隐式分区约束。 没有CHECK约束，将扫描表以验证分区约束，同时对该分区持有ACCESS EXCLUSIVE锁定，并在父表上持有SHARE UPDATE EXCLUSIVE锁。 在完成ATTACH PARTITION后，可能需要删除冗余的CHECK约束。

如上所述，可以在分区的表上创建索引，并自动将其应用于整个层次结构。 这非常便利，因为不仅现有分区增加了索引，而且将来创建的任何分区都将拥有索引。 一个限制是，在创建这样一个分区索引时，不能同时使用CONCURRENTLY限定符。 为了克服长时间锁，可以对分区表使用CREATE INDEX ON ONLY;这样的索引被标记为无效，并且分区不会自动应用该索引。分区上的索引可以使用CONCURRENTLY分别创建。然后使用ALTER INDEX.. ATTACH PARTITIONattached到父索引。 一旦所有分区的索引附加到父索引，父索引将自动标记为有效。 例如：

CREATE INDEX measurement\_usls\_idx ON ONLY measurement (unitsales);

CREATE INDEX measurement\_usls\_200602\_idx

ON measurement\_y2006m02 (unitsales);

ALTER INDEX measurement\_usls\_idx

ATTACH PARTITION measurement\_usls\_200602\_idx;

…

该技术也可以与UNIQUE 和PRIMARY KEY 约束一起使用; 当创建约束时隐式创建索引。例如:

ALTER TABLE ONLY measurement ADD UNIQUE (city\_id, logdate);

ALTER TABLE measurement\_y2006m02 ADD UNIQUE (city\_id, logdate);

ALTER INDEX measurement\_city\_id\_logdate\_key

ATTACH PARTITION measurement\_y2006m02\_city\_id\_logdate\_key;

…

#### 4.9.2.4. 限制

分区表有下列限制：

• 没有办法创建跨越所有分区的排他约束，只可能单个约束每个子分区。

• 分区表上的唯一约束必须包括所有分区键列。存在此限制是因为瀚高数据库只能每个分区中分别强制实施唯一性。

• 如果必要，必须在子分区上定义BEFORE ROW触发器，分区表上不需要。

• 不允许在同一个分区树中混杂临时关系和持久关系。因此，如果分区表是持久的，则其分区也必须是持久的，反之亦然。在使用临时关系时，分区数的所有成员都必须来自于同一个会话。

### 4.9.3. 使用继承实现

虽然内置的声明式分区适合于大部分常见的用例，但还是有一些场景需要更加灵活的方法。

分区可以使用表继承来实现，这能够带来一些声明式分区不支持的特性，例如：

• 对声明式分区来说，分区必须具有和分区表正好相同的列集合，而在表继承中，子表可以有父表中没有出现过的额外列。

• 表继承允许多继承。

• 声明式分区仅支持范围、列表以及哈希分区，而表继承允许数据按照用户的选择来划分（不过注意，如果约束排除不能有效地裁剪子表，查询性能可能会很差）。

• 在使用声明式分区时，一些操作比使用表继承时要求更长的持锁时间。例如，向分区表中增加分区或者从分区表移除分区要求在父表上取得一个ACCESS EXCLUSIVE锁，而在常规继承的情况下一个SHARE UPDATE EXCLUSIVE锁就足够了。

#### 4.9.3.1. 例子

我们使用上面用过的同一个measurement表。为了使用继承实现分区，可使用下面的步骤：

\\1. 创建“主”表，所有的“子”表都将从它继承。这个表将不包含数据。不要在这个表上定义任何检查约束，除非想让它们应用到所有的子表上。同样，在这个表上定义索引或者唯一约束也没有意义。对于我们的例子来说，主表是最初定义的measurement表。

\\2. 创建多个“子”表，每一个都从主表继承。通常，这些表将不会在从主表继承的列集合之外增加任何列。正如声明性分区那样，这些表就是普通的瀚高数据库表（或者外部表）。

CREATE TABLE measurement\_y2006m02 () INHERITS (measurement);

CREATE TABLE measurement\_y2006m03 () INHERITS (measurement);

…

CREATE TABLE measurement\_y2006m11 () INHERITS (measurement);

CREATE TABLE measurement\_y2006m12 () INHERITS (measurement);

CREATE TABLE measurement\_y2008m01 () INHERITS (measurement);

\\3. 为子表增加不重叠的表约束来定义每个分区允许的键值。

典型的例子是：

CHECK ( x = 1 )

CHECK ( county IN ( ‘Oxfordshire’, ‘Buckinghamshire’, ‘Warwickshire’ ))

CHECK ( outletID >= 100 AND outletID < 200 )

确保约束能保证不同子表允许的键值之间没有重叠。设置范围约束的常见错误：

CHECK ( outletID BETWEEN 100 AND 200 )

CHECK ( outletID BETWEEN 200 AND 300 )

这是错误的，因为不清楚键值200属于哪一个子表。

像下面这样创建子表会更好：

CREATE TABLE measurement\_y2006m02 (

CHECK ( logdate >= DATE ‘2006-02-01’ AND logdate < DATE ‘2006-03-01’ )

) INHERITS (measurement);

CREATE TABLE measurement\_y2006m03 (

CHECK ( logdate >= DATE ‘2006-03-01’ AND logdate < DATE ‘2006-04-01’ )

) INHERITS (measurement);

…

CREATE TABLE measurement\_y2006m11 (

CHECK ( logdate >= DATE ‘2006-11-01’ AND logdate < DATE ‘2006-12-01’ )

) INHERITS (measurement);

CREATE TABLE measurement\_y2006m12 (

CHECK ( logdate >= DATE ‘2006-12-01’ AND logdate < DATE ‘2008-01-01’ )

) INHERITS (measurement);

CREATE TABLE measurement\_y2008m01 (

CHECK ( logdate >= DATE ‘2008-01-01’ AND logdate < DATE ‘2008-02-01’ )

) INHERITS (measurement);

\\4. 对于每个子表，在键列上创建一个索引，以及任何想要的其他索引。

CREATE INDEX measurement\_y2006m02\_logdate ON measurement\_y2006m02 (logdate);

CREATE INDEX measurement\_y2006m03\_logdate ON measurement\_y2006m03 (logdate);

CREATE INDEX measurement\_y2006m11\_logdate ON measurement\_y2006m11 (logdate);

CREATE INDEX measurement\_y2006m12\_logdate ON measurement\_y2006m12 (logdate);

CREATE INDEX measurement\_y2008m01\_logdate ON measurement\_y2008m01 (logdate);

\\5. 我们希望我们的应用能够使用INSERT INTO measurement …并且数据将被重定向到合适的分区表。我们可以通过为主表附加一个合适的触发器函数来实现这一点。如果数据将只被增加到最后一个分区，我们可以使用一个非常简单的触发器函数：

CREATE OR REPLACE FUNCTION measurement\_insert\_trigger()

RETURNS TRIGGER AS $$

BEGIN

INSERT INTO measurement\_y2008m01 VALUES (NEW.\*);

RETURN NULL;

END;

$$

LANGUAGE plpgsql;

完成函数创建后，我们创建一个调用该触发器函数的触发器：

CREATE TRIGGER insert\_measurement\_trigger

BEFORE INSERT ON measurement

FOR EACH ROW EXECUTE FUNCTION measurement\_insert\_trigger();

我们必须在每个月重新定义触发器函数，这样它才会总是指向当前的子表。而触发器的定义则不需要被更新。

我们也可能希望插入数据时服务器会自动地定位应该加入数据的子表。我们可以通过一个更复杂的触发器函数来实现，例如：

CREATE OR REPLACE FUNCTION measurement\_insert\_trigger()

RETURNS TRIGGER AS $$

BEGIN

IF ( NEW.logdate >= DATE ‘2006-02-01’ AND

NEW.logdate < DATE ‘2006-03-01’ ) THEN

INSERT INTO measurement\_y2006m02 VALUES (NEW.\*);

ELSIF ( NEW.logdate >= DATE ‘2006-03-01’ AND

NEW.logdate < DATE ‘2006-04-01’ ) THEN

INSERT INTO measurement\_y2006m03 VALUES (NEW.\*);

…

ELSIF ( NEW.logdate >= DATE ‘2008-01-01’ AND

NEW.logdate < DATE ‘2008-02-01’ ) THEN

INSERT INTO measurement\_y2008m01 VALUES (NEW.\*);

ELSE

RAISE EXCEPTION ‘Date out of range. Fix the

measurement\_insert\_trigger() function!’;

END IF;

RETURN NULL;

END;

$$

LANGUAGE plpgsql;

触发器的定义和以前一样。注意每一个IF测试必须准确地匹配它的子表的CHECK约束。

当该函数比单月形式更加复杂时，并不需要频繁地更新它，因为可以在需要的时候提前加。

把插入重定向到一个合适的子表中的另一种不同方法是在主表上设置规则而不是触发器。

例如：

CREATE RULE measurement\_insert\_y2006m02 AS

ON INSERT TO measurement WHERE

( logdate >= DATE ‘2006-02-01’ AND logdate < DATE ‘2006-03-01’ )

DO INSTEAD

INSERT INTO measurement\_y2006m02 VALUES (NEW.\*);

…

CREATE RULE measurement\_insert\_y2008m01 AS

ON INSERT TO measurement WHERE

( logdate >= DATE ‘2008-01-01’ AND logdate < DATE ‘2008-02-01’ )

DO INSTEAD

INSERT INTO measurement\_y2008m01 VALUES (NEW.\*);

规则的开销比触发器大很多，但是这种开销是每个查询只有一次，而不是每行一次，因此这种方法可能对批量插入的情况有优势。不过，在大部分情况下，触发器方法性能更好。

注意COPY会忽略规则。如果想要使用COPY插入数据，则需要拷贝到正确的子表而不是直接放在主表中。COPY会引发触发器，因此在使用触发器方法时可以正常使用它。

规则方法的另一个缺点是，如果规则集合无法覆盖插入日期，则没有简单的方法能够强制产生错误，数据将会进入到主表中。

\\6. 确认constraint\_exclusion配置参数在postgresql.conf中没有被禁用，否则将会对子表进行不必要的访问。

如我们所见，一个复杂的表层次可能需要大量的DDL。在上面的例子中，我们可能为每个月创建一个新的子表，因此编写一个脚本来自动生成所需要的DDL可能会更好。

#### 4.9.3.2. 继承分区的维护

要快速移除旧数据，只需要简单地去掉不再需要的子表：

DROP TABLE measurement\_y2006m02;

要从继承层次表中去掉子表，但还作为一个普通表保留：

ALTER TABLE measurement\_y2006m02 NO INHERIT measurement;

要增加一个新子表来处理新数据，可以像上面创建的原始子表那样创建一个空的子表：

CREATE TABLE measurement\_y2008m02 (

CHECK ( logdate >= DATE ‘2008-02-01’ AND logdate < DATE ‘2008-03-01’ )

) INHERITS (measurement);

或者，用户可能想要创建新子表并且在将它加入到表层次之前填充它。这可以允许数据在附加到父表之前对数据进行装载、检查以及转换。

CREATE TABLE measurement\_y2008m02

(LIKE measurement INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE measurement\_y2008m02 ADD CONSTRAINT y2008m02

CHECK ( logdate >= DATE ‘2008-02-01’ AND logdate < DATE ‘2008-03-01’ );

\\copy measurement\_y2008m02 from ‘measurement\_y2008m02’

\-# possibly some other data preparation work

ALTER TABLE measurement\_y2008m02 INHERIT measurement;

#### 4.9.3.3. 提醒

下面的提醒适用于用继承实现的分区：

• 没有自动的方法验证所有的CHECK约束之间是否互斥。编写代码来产生子表以及创建和修改相关对象比手写命令更加安全。

• 索引和外键约束适用于单个表而不是其继承子级，因此它们有一些caveats 需要注意。

• 这里展示的模式假定行的键列值从不改变，或者说改变不足以让行移动到另一个分区。由于CHECK约束的存在，尝试那样做的UPDATE将会失败。如果需要处理那种情况，可以在子表上放置适当的更新触发器，但是会使结构管理更加复杂。

• 如果使用手工的VACUUM或者ANALYZE命令，不要忘记需要在每个子表上单独运行它们。命令：

ANALYZE measurement;

将只会处理主表。

• 带有ON CONFLICT子句的INSERT语句不太可能按照预期工作，因为只有在指定的目标关系而不是其子关系上发生冲突时才会采取ON CONFLICT行动。

• 将会需要触发器或者规则将行路由到想要的子表中，除非应用明确地知道分区的模式。编写触发器可能会很复杂，并且会比声明式分区在内部执行的步骤慢很多。

### 4.9.4. 分区裁剪

分区裁剪是一种提升声明式分区表性能的查询优化技术。例如：

SET enable\_partition\_pruning = on; -# the default

SELECT count(\*) FROM measurement WHERE logdate >= DATE ‘2008-01-01’;

如果没有分区裁剪，上面的查询将会扫描measurement表的每一个分区。如果启用了分区裁剪，规划器将会检查每个分区的定义并且检验该分区是否因为不包含符合查询WHERE子句的行而无需扫描。当规划器可以证实这一点时，它会把分区从查询计划中排除（裁剪）。

通过使用EXPLAIN命令和enable\_partition\_pruning配置参数，可以展示裁剪掉分区的计划与没有裁剪的计划之间的差别。对这种类型的表设置，一种典型的未优化计划是：

SET enable\_partition\_pruning = off;

EXPLAIN SELECT count(\*) FROM measurement WHERE logdate >= DATE ‘2008-01-01’;

QUERY PLAN

\-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

#-#-

Aggregate (cost=188.66..188.66 rows=1 width=8)

\-> Append (cost=0.00..181.05 rows=3085 width=0)

\-> Seq Scan on measurement\_y2006m02 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= ‘2008-01-01’::date)

\-> Seq Scan on measurement\_y2006m03 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= ‘2008-01-01’::date)

…

\-> Seq Scan on measurement\_y2006m11 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= ‘2008-01-01’::date)

\-> Seq Scan on measurement\_y2006m12 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= ‘2008-01-01’::date)

\-> Seq Scan on measurement\_y2008m01 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= ‘2008-01-01’::date)

某些或者全部的分区可能会使用索引扫描取代全表顺序扫描，但是这里的重点是该查询根本不需要扫描较老的分区。当我们启用分区裁剪时，我们会得到一个更便宜的计划：

SET enable\_partition\_pruning = on;

EXPLAIN SELECT count(\*) FROM measurement WHERE logdate >= DATE ‘2008-01-01’;

QUERY PLAN

\-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

#-#-

Aggregate (cost=36.65..36.66 rows=1 width=8)

\-> Seq Scan on measurement\_y2008m01 (cost=0.00..33.12 rows=616 width=0)

Filter: (logdate >= ‘2008-01-01’::date)

注意，分区裁剪仅由分区键隐式定义的约束所驱动，而不是由索引的存在驱动。因此，没有必要在键列上定义索引。是否需要为一个给定分区创建索引取决于预期的查询扫描该分区时会扫描大部分还是小部分。后一种情况下索引的帮助会比前者大。

不仅在给定查询的规划期间可以执行分区裁剪，在其执行期间也能执行分区裁剪。 这非常有用，因为如果子句中包含查询规划时值未知的表达式时，这可以裁剪掉更多的分区； 例如在PREPARE语句中定义的参数会使用从子查询拿到的值，或者嵌套循环连接内侧关系上的参数化值。 执行期间的分区裁剪可能在下列任何时刻执行：

• 在查询计划的初始化期间。对于执行的初始化阶段就已知值的参数，可以在这里执行分区裁剪。这个阶段中被裁剪掉的分区将不会显示在查询的EXPLAIN或EXPLAIN ANALYZE结果中。通过观察EXPLAIN输出的“Subplans Removed”属性，可以确定被裁剪掉的分区数。

• 在查询计划的实际执行期间。这里可以使用只有在实际查询执行时才能知道的值执行分区裁剪。这包括来自子查询的值以及来自执行时参数的值（例如来自于参数化嵌套循环连接的参数）。由于在查询执行期间这些参数的值可能会改变多次，所以只要分区裁剪使用到的执行参数发生改变，就会执行一次分区裁剪。要判断分区是否在这个阶段被裁剪，需要仔细地观察EXPLAIN ANALYZE输出中的loops属性。 对应于不同分区的子计划可以具有不同的值，这取决于在执行期间每个分区被裁剪的次数。如果每次都被裁剪，有些分区可能会显示为(never executed)。

| **注意：** |
| --- |
| 执行时间分区裁剪当前只针对Append和MergeAppend节点类型。暂不支持ModifyTable节点类型。 |

### 4.9.5. 分区和约束排除

约束排除是一种与分区裁剪类似的查询优化技术。虽然它主要被用于使用传统继承方法实现的分区上，但它也可以被用于其他目的，包括用于声明式分区。

约束排除以非常类似于分区裁剪的方式工作，不过它使用每个表的CHECK约束 — 这也是它得名的原因 — 而分区裁剪使用表的分区边界，分区边界仅存在于声明式分区的情况中。另一点不同之处是约束排除仅在规划时应用，在执行时不会尝试移除分区。

由于约束排除使用CHECK约束，这导致它比分区裁剪要慢，但有时候可以被当作一种优点加以利用：因为甚至可以在声明式分区的表上（在分区边界之外）定义约束，约束排除可能可以从查询计划中消去额外的分区。

constraint\_exclusion的默认（也是推荐的）设置不是on也不是off，而是一种被称为partition的中间设置，该参数值表示该技术仅被应用于可能工作在继承分区表上的查询。设置为on表示规划器检查所有查询中的CHECK约束，甚至是那些不太可能受益的简单查询。

约束排除需要注意以下几点：

• 约束排除仅适用于查询规划期间，而分区裁剪在查询执行期间也可以应用。

• 只有查询的WHERE子句包含常量（或者外部提供的参数）时，约束排除才能有效果。例如，针对一个非不变函数（如CURRENT\_TIMESTAMP）的比较不能被优化，因为规划器不知道该函数的值在运行时会落到哪个子表中。

• 保持分区约束简单化，否则规划器可能无法验证哪些子表可能不需要被访问。如前面的例子所示，对列表分区使用简单的等值条件，对范围分区使用简单的范围测试。建议分区约束应该仅包含分区列与使用B-树的可索引操作符的常量做比较，因为只有B-树的可索引列才允许出现在分区键中。

• 约束排除期间会检查父表的所有子表上的所有约束，因此大量的子表很可能明显地增加查询规划时间。因此，传统的基于继承的分区可以很好地处理上百个子表，但是不要尝试使用上千个子表。

### 4.9.6. 声明分区最佳实践

应该谨慎地选择如何划分表，因为查询规划和执行的性能可能会受到不良设计的负面影响。

最重要的设计决策之一是对数据进行分区的列。通常最佳选择最常出现在分区表上执行查询的 WHERE子句中的列。 WHERE子句项与分区键匹配并兼容，可用于裁剪不需要的分区。 但是，你可能会被迫根据PRIMARY KEY或UNIQUE约束的要求做出其他决策。 在规划分区策略时，删除不需要的数据也是需要考虑的一个因素。把一次删除的所有数据都放在单个分区中，这样可以相当快地分离整个分区。

选择表应该划分的分区数量也是一个重要的因素。没有足够的分区可能意味着索引太大，这可能导致缓存命中率很低。但是，将表划分为太多的分区也会导致问题。 在查询规划和执行期间，过多的分区可能意味着查询计划时间较长，内存消耗也更高。在选择如何划分表时，考虑将来可能发生的更改也很重要。 如，如果您选择为每个客户提供一个分区，而您目前只有少量的大客户，那么，如果几年后您发现自己有大量的小客户，那么就要考虑这种影响。在这种情况下，最好选择按HASH分区并且选择合理数量的分区，而不是尝试按 LIST 进行分区。

子分区可用于进一步划分预期会比其他分区更大的分区，尽管过多的子分区很容易导致大量分区，并可能导致前一段中提到的相同问题。

考虑查询计划和执行期间的分区开销也很重要。查询规划器通常能够很好地处理多达几千个分区的分区层次结构，前提是典型的查询允许查询规划器裁剪除了少量分区之外的所有分区。如果规划器执行分区裁剪后保留很多分区，规划时间会变长，内存消耗会更高。对于UPDATE 和 DELETE命令尤其如此。 担心拥有大量分区的另一个原因是，服务器的内存消耗可能会在一段时间内显著增加，特别是如果许多会话接触大量分区。 这是因为每个分区都需要将其元数据加载到需要它的每个会话的本地内存中。

对于数据仓库类型工作负载，建议使用比 OLTP 类型工作负载更多的分区数量。 通常，在数据仓库中，查询计划时间不太值得关注，因为大多数处理时间都花在查询执行期间。对于这两种类型的工作负载，尽早做出正确的决策非常重要，因为重新分区大量数据可能会非常缓慢。模拟预期工作负载通常有利于优化分区策略。永远不要假设更多的分区比更少的分区更好，反之亦然。

## 4.10. 外部数据

瀚高数据库实现了部分的SQL/MED规定，允许我们使用普通SQL查询来访问位于瀚高数据库之外的数据。这种数据被称为外部数据（注意这种用法不要和外键混淆，后者是数据库中的一种约束）。

外部数据可以在一个外部数据包装器的帮助下被访问。一个外部数据包装器是一个库，它可以与一个外部数据源通讯，并隐藏连接到数据源并获取数据源中的数据。

要访问外部数据，我们需要建立一个外部服务器对象，它根据它所支持的外部数据包装器所使用的一组选项定义了如何连接到一个特定的外部数据源。接着我们需要创建一个或多个外部表，它们定义了外部数据的结构。一个外部表可以在查询中像一个普通表一样地使用，但是在瀚高数据库服务器中外部表没有存储数据。不管使用什么外部数据包装器，瀚高数据库会要求外部数据包装器从外部数据源获取数据，或者在更新命令的情况下传送数据到外部数据源。

访问远程数据可能需要获取外部数据源的授权。这些信息通过一个用户映射提供。

更多信息请见 CREATE FOREIGN DATA WRAPPER、 CREATE SERVER、 CREATE USER MAPPING、CREATE FOREIGN TABLE、以及 IMPORT FOREIGN SCHEMA。

## 4.11. 其他数据库对象

表是一个关系型数据库结构中的核心对象，因为它们承载了我们的数据。但是它们并不是数据库中的唯一一种对象。有很多其他种类的对象可以被创建来使得数据的使用更加方便高效。在本章中不会详细讨论，具体的使用方法请参考对应章节内容：

• 视图

• 函数、过程和操作符

• 数据类型和域

• 触发器和重写规则。

## 4.12. 依赖跟踪

当我们创建一个涉及到很多具有外键约束、视图、触发器、函数等的表的复杂数据库结构时，我们隐式地创建了一张对象之间的依赖关系网。例如，具有一个外键约束的表依赖于它所引用的表。

为了保证整个数据库结构的完整性，瀚高数据库确保我们无法删除仍然被其他对象依赖的对象。例如，尝试删除第 4.4.5 节中的产品表会导致一个如下的错误消息，因为有订单表依赖于产品表：

DROP TABLE products;

ERROR: cannot drop table products because other objects depend on it

DETAIL: constraint orders\_product\_no\_fkey on table orders depends on table

products

HINT: Use DROP … CASCADE to drop the dependent objects too.

该错误消息包含了一个有用的提示：如果我们不想一个一个去删除所有的依赖对象，我们可以执行：

DROP TABLE products CASCADE;

这样所有的依赖对象都将被移除，同样依赖于它们的任何对象也会被递归删除。在这种情况下，订单表不会被移除，但是它的外键约束会被移除。

瀚高数据库中的几乎所有DROP命令都支持CASCADE。当然，其本质的区别随着对象的类型而不同。我们也可以用RESTRICT代替CASCADE来获得默认行为，它将阻止删除任何被其他对象依赖的对象。

| **注意：** |
| --- |
| 根据SQL标准，需要在DROP命令中明确指定RESTRICT或CASCADE。但没有哪个数据库系统真正强制了这个规则，但是不同的系统中两种默认行为都是可能的。 |

如果一个DROP命令列出了多个对象，只有当存在指定对象构成的组之外的依赖关系时才需要CASCADE。例如，如果发出命令DROP TABLE tab1, tab2且存在从tab2到tab1的外键引用，那么就不需要CASCADE即可成功执行。

对于用户定义的函数，瀚高数据库会追踪与函数外部可见性质相关的依赖性，例如它的参数和结果类型，但不追踪检查函数体才能知道的依赖性。例如，考虑这种情况：

CREATE TYPE rainbow AS ENUM (‘red’, ‘orange’, ‘yellow’,

‘green’, ‘blue’, ‘purple’);

CREATE TABLE my\_colors (color rainbow, note text);

CREATE FUNCTION get\_color\_note (rainbow) RETURNS text AS

‘SELECT note FROM my\_colors WHERE color = $1’

LANGUAGE SQL;

瀚高数据库将会注意到get\_color\_note函数依赖于rainbow类型：删掉该类型会强制删除该函数，因为该函数的参数类型就无法定义了。但是瀚高数据库不会认为get\_color\_note依赖于my\_colors表，因此即使该表被删除也不会删除这个函数。虽然这种方法有缺点，但是也有好处。如果该表丢失，这个函数在某种程度上仍然是有效的，但是执行它会导致错误。创建一个同名的新表可以重新使用该函数。

## 4.13. 数据分片

### 4.13.1. 概述

分片是在分布式数据库环境中将表划分为多个数据库服务器实例的行为，而分区是指在同一数据库服务器上划分表。分片也称为水平分区，它在一个或多个外部数据库服务器中保存数据以分散负载。在外部服务器上创建的表通常称为“分片”，并且通常通过本地数据库服务器上的外部数据包装器（FDW）处理程序（例如，postgres\_fdw扩展）进行访问。

在瀚高数据库系统中，WITH PUSHDOWN子句可用于创建外部分区表。该子句提供了在外部服务器上自动创建外部分区表的功能，而无需用户手动进行操作。

除了新的WITH PUSHDOWN子句外，数据分片还可能应用到另一个可选子句INCLUDE REMOTE，该子句可与现有的DROP FOREIGN TABLE子句一起使用，以自动删除外部服务器中的表，而无需用户手动删除它。此功能内置在postgres\_fdw扩展中，并且可以扩展到其他FDW。

### 4.13.2. WITH PUSHDOWN子句语法

WITH PUSHDOWN是一个可选子句，可以将其添加到现有CREATE FOREIGN TABLE语句的末尾，以在外部服务器上触发自动创建表。 此子句可以与外部表和分区的创建一起使用，并且不能与ALTER，UPDATE，DROP或INSERT子句。 以下各节概述了WITH PUSHDOWN的不同用例。

- 外部表创建

在外部表创建结束时使用WITH PUSHDOWN时，请考虑以下通用规则。

CREATE FOREIGN TABLE

IF NOT EXISTS table\_name ( column\_name TYPE ) SERVER server\_name

OPTIONS ( options ) WITH PUSHDOWN;

- 使用分区语法创建外部分区表

可以使用下列语法创建外部分区表，

相同的语法规则适用于其他分区类型，例如LIST和HASH。

/\* Partition by Range with PUSHDOWN \*/

/\* Same syntax rule applies to partition by List and Hash \*/

$ CREATE TABLE table\_name ( column\_name TYPE ) PARTITION BY RANGE ( column\_name )

(

PARTITION partition\_name\_1 FOR VALUES FROM (lower\_bound) TO (upper\_bound)

SERVER server\_name WITH PUSHDOWN,

PARTITION partition\_name\_2 FOR VALUES FRON (lower\_bound) TO (upper\_bound)

SERVER server\_name WITH PUSHDOWN,

PARTITION partition\_name\_3 DEFAULT SERVER server\_name WITH PUSHDOWN

/\* more partition definitions follow …\*/

);

- 使用分区语法创建外部子分区

可以使用以下语法创建外部子分区，

相同的语法规则适用于其他子分区类型，例如LIST和HASH。

/\* Sub Partition Creation with PUSHDOWN

$ CREATE TABLE table\_name ( column\_name TYPE ) PARTITION BY RANGE ( column\_name )

(

PARTITION partition\_name\_1 FOR VALUES FROM (lower\_bound) TO (upper\_bound) PARTITION BY RANGE( column\_name )

(

/\* Sub-Partition by RANGE \*/

PARTITION sub\_partition\_name\_1 FOR VALUES FROM (lower\_bound) TO

(upper\_bound) SERVER server\_name WITH PUSHDOWN,

PARTITION sub\_partition\_name\_2 FOR VALUES FROM (lower\_bound) TO

(upper\_bound) SERVER server\_name WITH PUSHDOWN,

PARTITION sub\_partition\_name\_3 SERVER server\_name WITH PUSHDOWN

/\* more sub partition definitions follow …\*/

)

/\* more partition definitions follow …\*/

);

### 4.13.3. INCLUDE REMOTE子句语法

INCLUDE REMOTE是一个可选子句，可以将其添加到现有DROP TABLE或DROP FOREIGN TABLE 语句的末尾，以触发外部服务器上的自动表删除。此子句可用于删除本地表和外部表，并且不能与ALTER，UPDATE，CREATE或INSERT子句一起使用。 以下各节概述了INCLUDE REMOTE的不同用例。

- 删除外部表

在DROP FOREIGN TABLE的末尾使用INCLUDE REMOTE时，请考虑以下一般规则：

DROP FOREIGN TABLE IF EXISTS table\_name INCLUDE REMOTE;

这个通用命令将删除本地和外部服务器中的table\_name。

- 删除外部分区表

要自动删除本地和外部分区表，用户可以遵循以下一般规则：

DROP TABLE table\_name INCLUDE REMOTE;

这将删除名为table\_name的本地表，以及在本地和外部服务器上创建的所有分区表。 外部分区表和外部服务器名称的列表，在执行查询时将打印为NOTICE。

如果用户创建包含外部子分区的表，则可以使用相同的规则删除该表以及在外部服务器上创建的所有子分区。

- 使用CASCADE删除外部分区表

如果用户尝试删除与其他表（例如视图）具有依赖性的外部或本地表，则将返回错误。 要解决此错误，用户可以先手动删除从属表，或者仅在查询语句中包括CASCADE子句以自动删除表及其从属关系。 根据下面的一般规则，CASCADE子句也可以与INCLUDE REMOTE子句一起使用：

DROP TABLE table\_name CASCADE INCLUDE REMOTE;

这将删除与table\_name相关的本地和外部服务器上的所有依赖表，然后删除本地和外部服务器上的table\_name及其关联的分区或子分区。

### 4.13.4. 本地数据库服务器上创建外部服务器对象

在使用新的WITH PUSHDOWN子句自动创建外部表之前，我们需要在本地数据库上定义代表外部服务器的服务器对象。作为示例，我们将定义2个服务器对象S1和S2，以表示2个外部服务器，在本节的其余部分中将引用它们。

创建服务器对象的过程可以分为以下步骤：

使用CREATE EXTENSION安装postgres\_fdw扩展请注意。

$ CREATE EXTENSION postgres\_fdw;

CREATE EXTENSION

- 接下来，我们将创建服务器对象S1和S2来表示2个外部服务器。

$ CREATE SERVER S1 FOREIGN DATA WRAPPER postgres\_fdw OPTIONS

(

dbname ‘highgo’,

host ‘172.17.0.3’

port ‘5333’

);

CREATE SERVER

$ CREATE SERVER S2 FOREIGN DATA WRAPPER postgres\_fdw OPTIONS

(

dbname ‘highgo’,

host ‘172.17.0.4’

port ‘5333’

);

CREATE SERVER

- 然后，我们将创建用户映射，将两个服务器对象的本地超级用户“highgo”映射到远程超级用户“highgo”。

$ CREATE USER MAPPING FOR highgo SERVER S1 OPTIONS ( user ‘highgo’ );

CREATE USER MAPPING

$ CREATE USER MAPPING FOR highgo SERVER S2 OPTIONS ( user ‘highgo’ );

CREATE USER MAPPING

- 最后，可以使用服务器对象S1和S2，我们将在接下来的内容中使用它们来说明WITH PUSHDOWN子句的便利性。
	### 4.13.5. 自动创建和删除外部表示例

在上一节中创建了服务器对象之后，我们可以在服务器对象S1上创建一个外部表。

$ CREATE FOREIGN TABLE

IF NOT EXISTS tf1\_f ( i INT, j VARCHAR ) SERVER S1

OPTIONS ( schema\_name ‘public’, table\_name ‘tf1\_data’ );

CREATE FOREIGN TABLE

上面的语句仅在本地数据库服务器上创建外部表，并且该表在外部服务器S1中尚不存在。如果我们尝试对该外部表进行数据操作，则会收到错误消息。

要在以S1表示的外部数据库服务器上自动创建外部表，请使用以下语法：

$ CREATE FOREIGN TABLE

IF NOT EXISTS tf1\_f ( i INT, j VARCHAR ) SERVER S1

OPTIONS ( schema\_name ‘public’, table\_name ‘tf1\_data’ )

WITH PUSHDOWN;

CREATE FOREIGN TABLE

WITH PUSHDOWN子句是可选的，并且在语句的末尾添加时，将在本地服务器上创建外部表tf1\_f，并在外部服务器上自动创建表tf1\_data。

请注意，上面的示例使用OPTION（table\_name’tf1\_data’）来说明我们在本地和外部服务器中都可以使用不同的表名。在这种情况下，插入到本地服务器上tf1\_f表中的数据将在外部服务器上的tf1\_data表中可用。

删除在上一个示例中创建的外部表：

$ DROP FOREIGN TABLE tf1\_f INCLUDE REMOTE;

NOTICE: Drop remote table ‘public.tf1\_data’ on foreign server ‘S1’

DROP FOREIGN TABLE

请注意，一行NOTICE将打印要删除的关系的名称并指示驻留的外部服务器对象。

基于同一示例，如果用户以后在依赖于表tf1\_f的名为view1的外部表上创建VIEW，则先前的DROP FOREIGN TABLE命令将因依赖关系而失败。 在这种情况下，我们可以使用CASCADE子句自动删除依赖关系和表。

$ DROP FOREIGN TABLE tf1\_f CASCADE INCLUDE REMOTE;

NOTICE: Drop remote table ‘public.tf1\_data’ on foreign server ‘S1’

NOTICE: drop cascades to view public.view1

DROP FOREIGN TABLE

请注意，将打印另一个NOTICE，以显示由于CASCADE子句而删除的依赖项。

### 4.13.6. 自动创建外部分区表和删除示例

WITH PUSHDOWN子句也可以与第3节中描述的新分区创建语法一起使用。请考虑以下2个示例，一个示例使用WITH PUSHDOWN子句，而另一个示例不使用。

$ CREATE TABLE prt\_com1\_f ( a INT ) PARTITION BY RANGE ( a )

(

PARTITION prt\_com1\_p1\_f FOR VALUES FROM (1) TO (10) SERVER S1,

PARTITION prt\_com1\_p2\_f FOR VALUES FRON (10) TO (20) SERVER S2,

PARTITION prt\_com1\_p3 DEFAULT

);

CREATE TABLE

上面的示例创建了3个分区表，其中prt\_com1\_p1\_f和prt\_com1\_p2\_f被声明为引用服务器对象S1和S2的外部表。这两个外部表仅在本地数据库服务器中创建，并且在服务S1和S2中尚不存在。

考虑在分区声明末尾添加了“ WITH PUSHDOWN”子句的相同示例。

$ CREATE TABLE prt\_com1\_f ( a INT ) PARTITION BY RANGE ( a )

(

PARTITION prt\_com1\_p1\_f FOR VALUES FROM (1) TO (10) SERVER S1 WITH PUSHDOWN,

PARTITION prt\_com1\_p2\_f FOR VALUES FRON (10) TO (20) SERVER S2 WITH PUSHDOWN,

PARTITION prt\_com1\_p3 DEFAULT

);

CREATE TABLE

上面的语句不仅将在本地数据库中创建prt\_com1\_p1\_f和prt\_com1\_p2\_f，还将在其相应的外部服务器S1和S2中创建它们。 这样就无需在外部服务器上手动创建相同的表。

删除在上一个示例中创建的外部分区表：

$ DROP TABLE prt\_com1\_f INCLUDE REMOTE;

NOTICE: Drop remote table ‘public.prt\_com1\_p2\_f’ on foreign server ‘S2’

NOTICE: Drop remote table ‘public.prt\_com1\_p1\_f’ on foreign server ‘S1’

DROP TABLE

该SQL语句将自动删除外部服务器上的本地表和分区以及分区表prt\_com1\_p2\_f和prt\_com1\_p2\_f。

基于同一示例，如果用户以后在分别依赖于表prt\_com1\_p2\_f和prt\_com1\_p2\_f的S1上名为view1的外部表上创建了VIEW，则先前的DROP TABLE命令将由于依赖而失败。 在这种情况下，我们将使用CASCADE子句自动删除外部服务器上的依赖项和分区表。

$ DROP TABLE prt\_com1\_f CASCADE INCLUDE REMOTE;

NOTICE: Drop remote table ‘public.prt\_com1\_p2\_f’ on foreign server ‘S2’

NOTICE: drop cascades to view public.view2

NOTICE: Drop remote table ‘public.prt\_com1\_p1\_f’ on foreign server ‘S1’

NOTICE: drop cascades to view public.view1

DROP TABLE

### 4.13.7. 自动创建外部子分区表和删除示例

考虑以下两个创建带有和不带有WITH PUSHDOWN子句的外部子分区的示例。

$ CREATE TABLE prt\_com4(a INT, b INT, c INT)

PARTITION BY RANGE( a )

(

PARTITION prt\_com4\_p1 FOR VALUES FROM (0) TO (100)

PARTITION BY RANGE( a )

(

PARTITION prt\_com4\_p1\_1 FOR VALUES FROM (0) TO (10) SERVER S1,

PARTITION prt\_com4\_p1\_2 FOR VALUES FROM (10) TO (20) SERVER S2,

PARTITION prt\_com4\_p1\_3 DEFAULT

)

);

CREATE TABLE

上面的示例创建3个分区表，其中prt\_com4\_p1\_1和prt\_com4\_p1\_2被声明为引用服务器对象S1和S2的外部表。 这两个外部表仅在本地数据库服务器中创建，并且在服务S1和S2中尚不存在。

考虑同一示例，在子分区声明的末尾添加了WITH PUSHDOWN子句。

$ CREATE TABLE prt\_com4(a INT, b INT, c INT)

PARTITION BY RANGE( a )

(

PARTITION prt\_com4\_p1 FOR VALUES FROM (0) TO (100)

PARTITION BY RANGE( a )

(

PARTITION prt\_com4\_p1\_1 FOR VALUES FROM (0) TO (10) SERVER S1

WITH PUSHDOWN,

PARTITION prt\_com4\_p1\_2 FOR VALUES FROM (10) TO (20) SERVER S2

WITH PUSHDOWN,

PARTITION prt\_com4\_p1\_3 DEFAULT

)

);

CREATE TABLE

上面的语句不仅会在本地数据库中创建prt\_com4\_p1\_1和prt\_com4\_p2\_2，还会在其相应的外部服务器S1和S2中创建它们。 这样就无需在外部服务器上手动创建相同的表。

删除在上一个示例中创建的外部子分区表：

$ DROP TABLE prt\_com4 INCLUDE REMOTE;

NOTICE: Drop remote table ‘public.prt\_com4\_p1\_2’ on foreign server ‘S2’

NOTICE: Drop remote table ‘public.prt\_com4\_p1\_1’ on foreign server ‘S1’

DROP TABLE

如果用户以后在依赖于prt\_com4\_p1\_1和prt\_com4\_p2\_2的S1上名为view1的外部表上创建了VIEW，则先前的DROP TABLE命令将因依赖关系而失败。 在这种情况下，我们将使用CASCADE子句自动删除外部服务器上表的依赖项和子分区表。

$ DROP TABLE prt\_com4 CASCADE INCLUDE REMOTE;

NOTICE: Drop remote table ‘public.prt\_com4\_p1\_2’ on foreign server ‘S2’

NOTICE: drop cascades to view public.view2

NOTICE: Drop remote table ‘public.prt\_com4\_p1\_1’ on foreign server ‘S1’

NOTICE: drop cascades to view public.view1

DROP TABLE

### 4.13.8. 常见的误用和误解

#### 4.13.8.1. 表和分区约束不受“ WITH PUSHDOWN”的影响

请考虑下面的SQL语句，该语句创建具有约束的外部分区：

$ CREATE TABLE prt\_com1\_f ( a INT ) PARTITION BY RANGE ( a )

(

PARTITION prt\_com1\_p1\_f (CONSTRAINT con\_prt\_com1\_p1 CHECK ( a!= 19 )) FOR VALUES FROM (1) TO (10) SERVER S1 WITH PUSHDOWN,

PARTITION prt\_com1\_p2\_f FOR VALUES FRON (10) TO (20) SERVER S2 WITH PUSHDOWN,

PARTITION prt\_com1\_p3 DEFAULT

);

CREATE TABLE

| **警告：** |
| --- |
| 定义的约束将仅存在于本地数据库服务器中，而不会通过“ WITH PUSHDOWN”子句传播到外部服务器。 这是预期的行为，将要求用户手动将约束添加到外部服务器。 |

#### 4.13.8.2. 不能在临时表上使用“ WITH PUSHDOWN”

考虑下面的SQL语句，该语句试图在临时表上执行“ WITH PUSHDOWN”。

CREATE TEMP TABLE prt\_com5(a INT, b INT, c INT) PARTITION BY RANGE(a)

(

PARTITION prt\_com5\_p1 FOR VALUES FROM (0) TO (100)

PARTITION BY RANGE(a)

(

PARTITION prt\_com5\_p1\_1 FOR VALUES FROM (0) TO (10) SERVER S1

WITH PUSHDOWN

)

);

ERROR: WITH PUSHDOWN is only allowed for permanent relations

| **警告：** |
| --- |
| 无法将“ WITH PUSHDOWN”应用于声明为“ TEMP”的表，如果在临时表上尝试下推将给出错误。 |

#### 4.13.8.3. 如果外部表已经存在，“ WITH PUSHDOWN”将返回错误

考虑下面的示例，在该示例中，我们尝试使用WITH PUSHDOWN子句连续两次将其创建为外部表，并在两者之间使用常规DROP TABLE子句。 第一次尝试将成功，第二次尝试将失败，因为WITH PUSHDOWN子句将不会创建表（如果已存在）。

$ CREATE TABLE prt\_com1\_f ( a INT ) PARTITION BY RANGE ( a )

(

PARTITION prt\_com1\_p1\_f FOR VALUES FROM (1) TO (10) SERVER S1 WITH PUSHDOWN,

PARTITION prt\_com1\_p2\_f FOR VALUES FRON (10) TO (20) SERVER S2 WITH PUSHDOWN

);

CREATE TABLE

/\* this will drop the local tables, not foreign \*/

$ DROP TABLE prt\_com1\_f;

DROP TABLE

$ CREATE TABLE prt\_com1\_f ( a INT ) PARTITION BY RANGE ( a )

(

PARTITION prt\_com1\_p1\_f FOR VALUES FROM (1) TO (10) SERVER S1 WITH PUSHDOWN,

PARTITION prt\_com1\_p2\_f FOR VALUES FRON (10) TO (20) SERVER S2 WITH PUSHDOWN

);

ERROR: Failed to execute CREATE TABLE on remote server

| **警告：** |
| --- |
| “ WITH PUSHDOWN ”将不会覆盖具有相同关系名称的远程表。 |

#### 4.13.8.4. 父分区表和子分区表不能同时为外部表

考虑下面的SQL语句，该语句试图使父分区和子分区同时处于外部。 这样做会由于使用不正确而导致给出错误消息。 在下面的示例中突出显示了导致错误的子句。

$ CREATE TABLE prt\_com4(a int, b int, c int) PARTITION BY RANGE(a)

(

PARTITION prt\_com4\_p1 FOR VALUES FROM (0) TO (100) SERVER S1

PARTITION BY RANGE(a)

(

PARTITION prt\_com4\_p1\_1 FOR VALUES FROM (0) TO (10) SERVER s1,

PARTITION prt\_com4\_p1\_2 FOR VALUES FROM (10) TO (20) SERVER s2,

PARTITION prt\_com4\_p1\_3 DEFAULT

),

PARTITION prt\_com4\_p2 FOR VALUES FROM (100) TO (200) SERVER S2

PARTITION BY LIST(b)

(

PARTITION prt\_com4\_p2\_1 FOR VALUES IN (1,2,3,4) SERVER s1,

PARTITION prt\_com4\_p2\_2 FOR VALUES IN (5,6,7,8) SERVER s2,

PARTITION prt\_com4\_p2\_3 DEFAULT

),

PARTITION prt\_com4\_p3 DEFAULT SERVER S1

PARTITION BY HASH(c)

(

PARTITION prt\_com4\_p3\_1 FOR VALUES WITH(MODULUS 3, REMAINDER 0),

PARTITION prt\_com4\_p3\_2 FOR VALUES WITH(MODULUS 3, REMAINDER 1),

PARTITION prt\_com4\_p3\_3 FOR VALUES WITH(MODULUS 3, REMAINDER 2)

)

);

ERROR: Partition table can not be a foreign table

| **警告：** |
| --- |
| 请注意，只有没有子子分区的分区才能被创建为“foreign”分区。 换句话说，只有位于分区层次结构树末尾的分区才可以设置为“foreign”。 它们的父分区不能设为“foreign”。 |