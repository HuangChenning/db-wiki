---
title: "数据定义"
book: "SQL语言参考手册"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceFour5.html"
tags:
  - highgo
  - highgo-v9
  - sql-language-reference
---

## 数据定义

本章包含了如何创建用来保存数据的数据库结构。在一个关系型数据库中，原始数据被存储在表中，因此本章的主要工作就是解释如何创建和修改表，以及哪些特性可以控制何种数据会被存储在表中。接着，我们讨论表如何被组织成模式，以及如何将权限分配给表。最后，我们将将简短地介绍其他一些影响数据存储的特性，例如继承、表分区、视图、函数和触发器。

## 表基础

关系型数据库中的一个表非常像纸上的一张表：它由行和列组成。列的数量和顺序是固定的，并且每一列拥有一个名字。行的数目是变化的，它反映了在一个给定时刻表中存储的数据量。SQL并不保证表中行的顺序。当一个表被读取时，表中的行将以非特定顺序出现，除非明确地指定需要排序。这些将在第 5 章介绍。此外，SQL不会为行分配唯一的标识符，因此在一个表中可能会存在一些完全相同的行。这是SQL之下的数学模型导致的结果，但并不是所期望的。稍后在本章中我们将看到如何处理这种问题。

每一列都有一个数据类型。数据类型约束着一组可以分配给列的可能值，并且它为列中存储的数据赋予了语义，这样它可以用于计算。例如，一个被声明为数字类型的列将不会接受任何文本串，而存储在这样一列中的数据可以用来进行数学计算。反过来，一个被声明为字符串类型的列将接受几乎任何一种的数据，它可以进行如字符串连接的操作但不允许进行数学计算。

瀚高数据库包括了相当多的内建数据类型，可以适用于很多应用。用户也可以定义他们自己的数据类型。大部分内建数据类型有着显而易见的名称和语义，所以我们将它们的详细解释放在第 8 章中。一些常用的数据类型是：用于整数的integer；可以用于分数的numeric；用于字符串的text，用于日期的date，用于一天内时间的time以及可以同时包含日期和时间的timestamp。

要创建一个表，我们要用到CREATE TABLE命令。在这个命令中 我们需要为新表至少指定一个名字、列的名字及数据类型。例如：

CREATE TABLE my\_first\_table (

first\_column text,

second\_column integer

);

这将创建一个名为my\_first\_table的表，它拥有两个列。第一个列名为first\_column且数据类型为text；第二个列名为second\_column且数据类型为integer。表和列的名字遵循第 4.1.1 节中解释的标识符语法。类型名称通常也是标识符，但是也有些例外。注意列的列表由逗号分隔并被圆括号包围。

当然，前面的例子是非常不自然的。通常，我们为表和列赋予的名称都会表明它们存储着什么类别的数据。因此让我们再看一个更现实的例子：

CREATE TABLE products (

product\_no integer,

name text,

price numeric

);

（numeric类型能够存储小数部分，典型的例子是金额。）

| 提示： |
| --- |
| 当我们创建很多相关的表时，最好为表和列选择一致的命名模式。例如，一种选择是用单数或复数名词作为表名，每一种都受到一些理论家支持。 |

一个表能够拥有的列的数据是有限的，根据列的类型，这个限制介于250和1600之间。但是，极少会定义一个接近这个限制的表，即便有也是一个值的商榷的设计。

如果我们不再需要一个表，我们可以通过使用DROP TABLE命令来移除它。例如：

DROP TABLE my\_first\_table;

DROP TABLE products;

尝试移除一个不存在的表会引起错误。然而，在SQL脚本中在创建每个表之前无条件地尝试移除它的做法是很常见的，即使发生错误也会忽略之，因此这样的脚本可以在表存在和不存在时都工作得很好（如果你喜欢，可以使用DROP TABLE IF EXISTS变体来防止出现错误消息，但这并非标准SQL）。

如果我们需要修改一个已经存在的表，请参考本章稍后的第 4.6 节。

利用到目前为止所讨论的工具，我们可以创建一个全功能的表。本章的后续部分将集中于为表定义增加特性来保证数据完整性、安全性或方便。如果你希望现在就去填充你的表，你可以跳过这些直接去第 5 章。

## 默认值

一个列可以被分配一个默认值。当一个新行被创建且没有为某些列指定值时，这些列将会被它们相应的默认值填充。一个数据操纵命令也可以显式地要求一个列被置为它的默认值，而不需要知道这个值到底是什么（数据操纵命令详见第 5 章）。

如果没有显式指定默认值，则默认值是空值。这是合理的，因为空值表示未知数据。

在一个表定义中，默认值被列在列的数据类型之后。例如：

CREATE TABLE products (

product\_no integer,

name text,

price numeric DEFAULT 9.99

);

默认值可以是一个表达式，它将在任何需要插入默认值的时候被实时计算（不是表创建时）。一个常见的例子是为一个timestamp列指定默认值为CURRENT\_TIMESTAMP，这样它将得到行被插入时的时间。另一个常见的例子是为每一行生成一个”序列号” 。这在瀚高数据库可以按照如下方式实现：

CREATE TABLE products (

product\_no integer DEFAULT nextval('products\_product\_no\_seq'),

...

);

这里nextval()函数从一个序列对象第 8.16 节）。还有一种特别的速写：

CREATE TABLE products (

product\_no SERIAL,

...

);

SERIAL速写将在第 7.1.4 节进一步讨论。

## 生成列

生成的列是一个特殊的列，它总是从其他列计算而来。因此说，它对于列就像视图对于表一样。生成列有两种:存储列和虚拟列。 存储生成列在写入(插入或更新)时计算，并且像普通列一样占用存储空间。虚拟生成列不占用存储空间并且在读取时进行计算。 如此看来，虚拟生成列类似于视图，存储生成列类似于物化视图(除了它总是自动更新之外)。

瀚高数据库目前只实现了存储生成列。

建立一个生成列，在 CREATE TABLE中使用 GENERATED ALWAYS AS 子句, 例如:

CREATE TABLE people (

...,

height\_cm numeric,

height\_in numeric GENERATED ALWAYS AS (height\_cm / 2.54) STORED

);

必须指定关键字 STORED 以选择存储类型的生成列。更多细节请参见 CREATE TABLE 。

生成列不能被直接写入. 在INSERT 或 UPDATE 命令中, 不能为生成列指定值, 但是可以指定关键字DEFAULT。

考虑列缺省情况和生成列之间的差异。 如果没有提供其他值，列缺省情况下在行被首次插入时计算一次;生成列则在行每次改变时进行更新，并且不能被取代。 列缺省情况下不能引用表的其他列；生成表达式通常会这样做。 列缺省情况下可以使用易失性函数，例如random()或引用当前时间函数; 而对于生成列这是不允许的。

生成列和涉及生成列的表的定义有几个限制:

• 生成表达式只能使用不可变函数，并且不能使用子查询或以任何方式引用当前行以外的任何内容。

• 生成表达式不能引用另一个生成列。

• 生成表达式不能引用系统表，除了 tableoid。

• 生成列不能具有列默认或标识定义。

• 生成列不能是分区键的一部分。

• 外部表可以有生成列. 更多细节请参见 CREATE FOREIGN TABLE.

使用生成列的其他注意事项。

• 生成列保留着有别于其下层的基础列的访问权限。因此，可以对其进行排列以便于从生成列中读取特定的角色，而不是从下层基础列。

• 从概念上讲，生成列在BEFORE 触发器运行后更新。 因此，BEFORE 触发器中的基础列所做

## 约束

数据类型是一种限制能够存储在表中数据类别的方法。但是对于很多应用来说，它们提供的约束太粗糙。例如，一个包含产品价格的列应该只接受正值。但是没有任何一种标准数据类型只接受正值。另一个问题是我们可能需要根据其他列或行来约束一个列中的数据。例如，在一个包含产品信息的表中，对于每个产品编号应该只有一行。

到目前为止，SQL允许我们在列和表上定义约束。约束让我们能够根据我们的愿望来控制表中的数据。如果一个用户试图在一个列中保存违反一个约束的数据，一个错误会被抛出。即便是这个值来自于默认值定义，这个规则也同样适用。

### 检查约束

一个检查约束是最普通的约束类型。它允许我们指定一个特定列中的值必须要满足一个布尔表达式。例如，为了要求正值的产品价格，我们可以使用：

CREATE TABLE products (

product\_no integer,

name text,

price numeric CHECK (price > 0)

);

如你所见，约束定义就和默认值定义一样跟在数据类型之后。默认值和约束之间的顺序没有影响。一个检查约束有关键字CHECK以及其后的包围在圆括号中的表达式组成。检查约束表达式应该涉及到被约束的列，否则该约束也没什么实际意义。

我们也可以给与约束一个独立的名称。这会使得错误消息更为清晰，同时也允许我们在需要更改约束时能引用它。语法为：

CREATE TABLE products (

product\_no integer,

name text,

price numeric CONSTRAINT positive\_price CHECK (price > 0)

);

要指定一个命名的约束，请在约束名称标识符前使用关键词CONSTRAINT，然后把约束定义放在标识符之后（如果没有以这种方式指定一个约束名称，系统将会为我们选择一个）。

一个检查约束也可以引用多个列。例如我们存储一个普通价格和一个打折后的价格，而我们希望保证打折后的价格低于普通价格：

CREATE TABLE products (

product\_no integer,

name text,

price numeric CHECK (price > 0),

discounted\_price numeric CHECK (discounted\_price > 0),

CHECK (price > discounted\_price)

);

前两个约束看起来很相似。第三个则使用了一种新语法。它并没有依附在一个特定的列，而是作为一个独立的项出现在逗号分隔的列列表中。列定义和这种约束定义可以以混合的顺序出现在列表中。

我们将前两个约束称为列约束，而第三个约束为表约束，因为它独立于任何一个列定义。列约束也可以写成表约束，但反过来不行，因为一个列约束只能引用它所依附的那一个列（瀚高数据库并不强制要求这个规则，但是如果我们希望表定义能够在其他数据库系统中工作，那就应该遵循它）。上述例子也可以写成：

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

这只是口味的问题。

表约束也可以用列约束相同的方法来指定名称：

CREATE TABLE products (

product\_no integer,

name text,

price numeric,

CHECK (price > 0),

discounted\_price numeric,

CHECK (discounted\_price > 0),

CONSTRAINT valid\_discount CHECK (price > discounted\_price)

);

需要注意的是，一个检查约束在其检查表达式值为真或空值时被满足。因为当任何操作数为空时大部分表达式将计算为空值，所以它们不会阻止被约束列中的控制。为了保证一个列不包含控制，可以使用下一节中的非空约束。

| 注意： |
| --- |
| 瀚高数据库不支持引用表数据以外的要检查的新增或更新的行的CHECK约束。虽然违反此规则的CHECK约束在简单测试中看起来能工作，它不能保证数据库不会达到约束条件为假(false)的状态（由于涉及的其他行随后发生了更改）。将导致数据库转储和重新加载失败。 即使完整的数据库状态与约束一致，重新加载也可能失败，因为行未按照满足约束的顺序加载。 如果可能的话，使用UNIQUE, EXCLUDE,或 FOREIGN KEY约束以表示跨行和跨表限制。如果你希望的是在插入行时的时候对其他行进行一次性检查，而不是持续维护的一致性保证，一个自定义的 trigger 可以用于实现这个功能。（此方法避免了转储/重新加载问题，因为pg\_dump不会重新安装触发器直到重新加载数据之后，因此不会在转储/重新加载期间强制执行检查。）瀚高数据库假定CHECK约束的条件是不可变的，也就是说，它们始终为同一输入行提供相同的结果。这个假设是仅在插入或更新行时,而不是在其他时间检查CHECK约束的原因。（上面关于不引用其他表数据的警告实际上是此限制的特殊情况。）打破此假设的常见方法的一个示例是在 CHECK表达式中引用用户定义的函数，然后更改该函数的行为。 瀚高数据库不会禁止那样，但它不会注意到现在的表。 |

### 非空约束

一个非空约束仅仅指定一个列中不会有空值。语法例子：

CREATE TABLE products (

product\_no integer NOT NULL,

name text NOT NULL,

price numeric

);

一个非空约束总是被写成一个列约束。一个非空约束等价于创建一个检查约束CHECK (column\_name IS NOT NULL)，但在瀚高数据库中创建一个显式的非空约束更高效。这种方式创建的非空约束的缺点是我们无法为它给予一个显式的名称。

当然，一个列可以有多于一个的约束，只需要将这些约束一个接一个写出：

CREATE TABLE products (

product\_no integer NOT NULL,

name text NOT NULL,

price numeric NOT NULL CHECK (price > 0)

);

约束的顺序没有关系，因为并不需要决定约束被检查的顺序。

NOT NULL约束有一个相反的情况：NULL约束。这并不意味着该列必须为空，进而肯定是无用的。相反，它仅仅选择了列可能为空的默认行为。SQL标准中并不存在NULL约束，因此它不能被用于可移植的应用中（瀚高数据库中加入它是为了和某些其他数据库系统兼容）。但是某些用户喜欢它，因为它使得在一个脚本文件中可以很容易的进行约束切换。例如，初始时我们可以：

CREATE TABLE products (

product\_no integer NULL,

name text NULL,

price numeric NULL

);

然后可以在需要的地方插入NOT关键词。

| 提示： |
| --- |
| 在大部分数据库中多数列应该被标记为非空。 |

### 唯一约束

唯一约束保证\\在一列中或者一组列中保存的数据在表中所有行间是唯一的。写成一个列约束的语法是：

CREATE TABLE products (

product\_no integer UNIQUE,

name text,

price numeric

);

写成一个表约束的语法是：

CREATE TABLE products (

product\_no integer,

name text,

price numeric,

UNIQUE (product\_no)

);

当写入表约束时。

要为一组列定义一个唯一约束，把它写作一个表级约束，列名用逗号分隔：

CREATE TABLE example (

a integer,

b integer,

c integer,

UNIQUE (a, c)

);

这指定这些列的组合值在整个表的范围内是唯一的，但其中任意一列的值并不需要是（一般也不是）唯一的。

我们可以通常的方式为一个唯一索引命名：

CREATE TABLE products (

product\_no integer CONSTRAINT must\_be\_different UNIQUE,

name text,

price numeric

);

增加一个唯一约束会在约束中列出的列或列组上自动创建一个唯一B-tree索引。只覆盖某些行的唯一性限制不能被写为一个唯一约束，但可以通过创建一个唯一的部分索引来强制这种限制。

通常，如果表中有超过一行在约束所包括列上的值相同，将会违反唯一约束。但是在这种比较中，两个空值被认为是不同的。这意味着即便存在一个唯一约束，也可以存储多个在至少一个被约束列中包含空值的行。这种行为符合SQL标准，但我们听说一些其他SQL数据库可能不遵循这个规则。所以在开发需要可移植的应用时应注意这一点。

### 主键

一个主键约束表示可以用作表中行的唯一标识符的一个列或者一组列。这要求那些值都是唯一的并且非空。因此，下面的两个表定义接受相同的数据：

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

主键也可以包含多于一个列，其语法和唯一约束相似：

CREATE TABLE example (

a integer,

b integer,

c integer,

PRIMARY KEY (a, c)

);

增加一个主键将自动在主键中列出的列或列组上创建一个唯一B-tree索引。并且会强制这些列被标记为NOT NULL。

一个表最多只能有一个主键（可以有任意数量的唯一和非空约束，它们可以达到和主键几乎一样的功能，但只能有一个被标识为主键）。关系数据库理论要求每一个表都要有一个主键。但瀚高数据库中并未强制要求这一点，但是最好能够遵循它。

主键对于文档和客户端应用都是有用的。例如，一个允许修改行值的 GUI 应用可能需要知道一个表的主键，以便能唯一地标识行。如果定义了主键，数据库系统也有多种方法来利用主键。例如，主键定义了外键要引用的默认目标列。

### 外键

一个外键约束指定一列（或一组列）中的值必须匹配出现在另一个表中某些行的值。我们说这维持了两个关联表之间的引用完整性。

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

因为如果缺少列的列表，则被引用表的主键将被用作被引用列。

一个外键也可以约束和引用一组列。照例，它需要被写成表约束的形式。下面是一个例子：

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

...

);

CREATE TABLE order\_items (

product\_no integer REFERENCES products,

order\_id integer REFERENCES orders,

quantity integer,

PRIMARY KEY (product\_no, order\_id)

);

注意在最后一个表中主键和外键之间有重叠。

我们知道外键不允许创建与任何产品都不相关的订单。但如果一个产品在一个引用它的订单创建之后被移除会发生什么？SQL允许我们处理这种情况。直观上，我们有几种选项：

• 不允许删除一个被引用的产品

• 同时也删除引用产品的订单

• 其他？

为了说明这些，让我们在上面的多对多关系例子中实现下面的策略：当某人希望移除一个仍然被一个订单引用（通过order\_items）的产品时 ，我们组织它。如果某人移除一个订单，订单项也同时被移除：

CREATE TABLE products (

product\_no integer PRIMARY KEY,

name text,

price numeric

);

CREATE TABLE orders (

order\_id integer PRIMARY KEY,

shipping\_address text,

...

);

CREATE TABLE order\_items (

product\_no integer REFERENCES products ON DELETE RESTRICT,

order\_id integer REFERENCES orders ON DELETE CASCADE,

quantity integer,

PRIMARY KEY (product\_no, order\_id)

);

限制删除或者级联删除是两种最常见的选项。RESTRICT阻止删除一个被引用的行。NO ACTION表示在约束被检察时如果有任何引用行存在，则会抛出一个错误，这是我们没有指定任何东西时的默认行为（这两种选择的本质不同在于NO ACTION允许检查被推迟到事务的最后，而RESTRICT则不会）。CASCADE指定当一个被引用行被删除后，引用它的行也应该被自动删除。还有其他两种选项：SET NULL和SET DEFAULT。这些将导致在被引用行被删除后，引用行中的引用列被置为空值或它们的默认值。注意这些并不会是我们免于遵守任何约束。例如，如果一个动作指定了SET DEFAULT，但是默认值不满足外键约束，操作将会失败。

与ON DELETE相似，同样有ON UPDATE可以用在一个被引用列被修改（更新）的情况，可选的动作相同。在这种情况下，CASCADE意味着被引用列的更新值应该被复制到引用行中。

正常情况下，如果一个引用行的任意一个引用列都为空，则它不需要满足外键约束。如果在外键定义中加入了MATCH FULL，一个引用行只有在它的所有引用列为空时才不需要满足外键约束（因此空和非空值的混合肯定会导致MATCH FULL约束失败）。如果不希望引用行能够避开外键约束，将引用行声明为NOT NULL。

一个外键所引用的列必须是一个主键或者被唯一约束所限制。这意味着被引用列总是拥有一个索引（位于主键或唯一约束之下的索引），因此在其上进行的一个引用行是否匹配的检查将会很高效。由于从被引用表中DELETE一行或者UPDATE一个被引用列将要求对引用表进行扫描以得到匹配旧值的行，在引用列上建立合适的索引也会大有益处。由于这种做法并不是必须的，而且创建索引也有很多种选择，所以外键约束的定义并不会自动在引用列上创建索引。

更多关于更新和删除数据的信息请见第 5 章。外键约束的语法描述请参考CREATE TABLE。

### 排他约束

排他约束保证如果将任何两行的指定列或表达式使用指定操作符进行比较，至少其中一个操作符比较将会返回否或空值。语法是：

CREATE TABLE circles (

c circle,

EXCLUDE USING gist (c WITH &&)

);

详见CREATE TABLE... CONSTRAINT... EXCLUDE。

增加一个排他约束将在约束声明所指定的类型上自动创建索引。

### 约束开关

数据库支持约束开关功能，用户可通过执行SQL语句实现对约束的开启和禁用。

约束启用语法为:

ALTER TABLE table\_name ENABLE CONSTRAINT constraint\_name;

约束禁用开关：

ALTER TABLE table\_name DISABLE CONSTRAINT constraint\_name;

相应的，在系统表pg\_constraint的字段conenabled会记录约束的启用状态。

## 系统列

每一个表都拥有一些由系统隐式定义的system columns。因此，这些列的名字不能像用户定义的列一样使用（注意这种限制与名称是否为关键词没有关系，即便用引号限定一个名称也无法绕过这种限制）。 事实上用户不需要关心这些列，只需要知道它们存在即可。

tableoid

包含这一行的表的OID。该列是特别为从继承层次（见第 4.10 节）中选择的查询而准备，因为如果没有它将很难知道一行来自于哪个表。tableoid可以与pg\_class的oid列进行连接来获得表的名称。

xmin

插入该行版本的事务身份（事务ID）。一个行版本是一个行的一个特别版本，对一个逻辑行的每一次更新都将创建一个新的行版本。

cmin

插入事务中的命令标识符（从0开始）。

xmax

删除事务的身份（事务ID），对于未删除的行版本为0。对于一个可见的行版本，该列值也可能为非零。这通常表示删除事务还没有提交，或者一个删除尝试被回滚。

cmax

删除事务中的命令标识符，或者为0。

ctid

行版本在其表中的物理位置。注意尽管ctid可以被用来非常快速地定位行版本，但是一个行的ctid会在被更新或者被VACUUM FULL移动时改变。因此，ctid不能作为一个长期行标识符。 应使用主键来标识逻辑行。

事务标识符也是32位量。在一个历时长久的数据库中事务ID同样会绕回。但如果采取适当的维护过程，这不会是一个致命的问题。但是，长期（超过10亿个事务）依赖事务ID的唯一性是不明智的。

命令标识符也是32位量。这对一个事务中包含的SQL命令设置了一个硬极限：232（40亿）。

在实践中，该限制并不是问题 — 注意该限制只是针对SQL命令的数目而不是被处理的行数。

同样，只有真正 修改了数据库内容的命令才会消耗一个命令标识符。

## 修改表

当我们已经创建了一个表并意识到犯了一个错误或者应用需求发生改变时，我们可以移除表并重新创建它。但如果表中已经被填充数据或者被其他数据库对象引用（例如有一个外键约束），这种做法就显得很不方便。因此，瀚高数据库提供了一族命令来对已有的表进行修改。注意这和修改表中所包含的数据是不同的，这里要做的是对表的定义或者说结构进行修改。

利用这些命令，我们可以：

• 增加列

• 移除列

• 增加约束

• 移除约束

• 修改默认值

• 修改列数据类型

• 重命名列

• 重命名表

所有这些动作都由ALTER TABLE命令执行，其参考页面中包含更详细的信息。

### 增加列

要增加一个列，可以使用这样的命令：

ALTER TABLE products ADD COLUMN description text;

新列将被默认值所填充（如果没有指定DEFAULT子句，则会填充空值）。

提示

从瀚高数据库v4.5开始，添加一个具有常量默认值的列不再意味着在执

行ALTER TABLE 语句时需要更新表的每一行。 相反，默认值将在下次访问该行时返回，并在表被重写时应用，从而使得ALTER TABLE即使在大表上也非常快。

但是，如果默认值是可变的（例如clock\_timestamp()），则每一行需要被ALTER TABLE被执行时计算的值更新。 为避免潜在的长时间的更新操作，特别是如果你想要用大多数非默认值填充列，那么最好添加没有默认值的列，再用 UPDATE插入正确的值，然后按照下面所述添加任何期望的默认值。

也可以同时为列定义约束，语法：

ALTER TABLE products ADD COLUMN description text CHECK (description <> '');

事实上CREATE TABLE中关于一列的描述都可以应用在这里。记住不管怎样，默认值必须满足给定的约束，否则ADD将会失败。也可以先将新列正确地填充好，然后再增加约束（见后文）。

### 移除列

为了移除一个列，使用如下的命令：

ALTER TABLE products DROP COLUMN description;

列中的数据将会消失。涉及到该列的表约束也会被移除。然而，如果该列被另一个表的外键所引用，瀚高数据库不会安静地移除该约束。我们可以通过增加CASCADE来授权移除任何依赖于被删除列的所有东西：

ALTER TABLE products DROP COLUMN description CASCADE;

### 增加约束

为了增加一个约束，可以使用表约束的语法，例如：

ALTER TABLE products ADD CHECK (name <> '');

ALTER TABLE products ADD CONSTRAINT some\_name UNIQUE (product\_no);

ALTER TABLE products ADD FOREIGN KEY (product\_group\_id) REFERENCES

product\_groups;

要增加一个不能写成表约束的非空约束，可使用语法：

ALTER TABLE products ALTER COLUMN product\_no SET NOT NULL;

该约束会立即被检查，所以表中的数据必须在约束被增加之前就已经符合约束。

### 移除约束

为了移除一个约束首先需要知道它的名称。如果在创建时已经给它指定了名称，那么事情就变得很容易。否则约束的名称是由系统生成的，我们必须先找出这个名称。psql的命令\\d表名将会对此有所帮助，其他接口也会提供方法来查看表的细节。因此命令是：

ALTER TABLE products DROP CONSTRAINT some\_name;

（如果处理的是自动生成的约束名称，如$2，别忘了用双引号使它变成一个合法的标识符。）

和移除一个列相似，如果需要移除一个被某些别的东西依赖的约束，也需要加上CASCADE。

一个例子是一个外键约束依赖于被引用列上的一个唯一或者主键约束。

这对除了非空约束之外的所有约束类型都一样有效。为了移除一个非空约束可以用：

ALTER TABLE products ALTER COLUMN product\_no DROP NOT NULL;

（回忆一下，非空约束是没有名称的，所以不能用第一种方式。）

### 更改列的默认值

要为一个列设置一个新默认值，使用命令：

ALTER TABLE products ALTER COLUMN price SET DEFAULT 6.66;

注意这不会影响任何表中已经存在的行，它只是为未来的INSERT命令改变了默认值。

要移除任何默认值，使用：

ALTER TABLE products ALTER COLUMN price DROP DEFAULT;

这等同于将默认值设置为空值。相应的，试图删除一个未被定义的默认值并不会引发错误，因为默认值已经被隐式地设置为空值。

### 修改列的数据类型

为了将一个列转换为一种不同的数据类型，使用如下命令：

ALTER TABLE products ALTER COLUMN price TYPE numeric(10,2);

只有当列中的每一个项都能通过一个隐式造型转换为新的类型时该操作才能成功。如果需要一种更复杂的转换，应该加上一个USING子句来指定应该如何把旧值转换为新值。

瀚高数据库将尝试把列的默认值转换为新类型，其他涉及到该列的任何约束也是一样。但是这些转换可能失败或者产生奇特的结果。因此最好在修改类型之前先删除该列上所有的约束，然后在修改完类型后重新加上相应修改过的约束。

### 重命名列

要重命名一个列：

ALTER TABLE products RENAME COLUMN product\_no TO product\_number;

### 重命名表

要重命名一个表：

ALTER TABLE products RENAME TO items;

## 权限

一旦一个对象被创建，它会被分配一个所有者。所有者通常是执行创建语句的角色。对于大部分类型的对象，初始状态下只有所有者（或者超级用户）能够对该对象做任何事情。为了允许其他角色使用它，必须分配权限。

有多种不同的权限：SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES、TRIGGER、CREATE、CONNECT、TEMPORARY、EXECUTE以

及USAGE。可以应用于一个特定对象的权限随着对象的类型（表、函数等）而不同。 有关这些权限含义的更多详细信息请参阅下文。后续的章节将介绍如何使用这些权限。

修改或销毁一个对象的权力通常是只有所有者才有的权限。

一个对象可以通过该对象类型相应的ALTER命令来重新分配所有者，例如

ALTER TABLE table\_name OWNER TO new\_owner;

超级用户总是可以做到这点，普通角色只有同时是对象的当前所有者（或者是拥有角色的一个成员）以及新拥有角色的一个成员时才能做同样的事。

要分配权限，可以使用GRANT命令。例如，如果joe是一个已有角色，而accounts是一个已有表，更新该表的权限可以按如下方式授权：

GRANT UPDATE ON accounts TO joe;

用ALL取代特定权限会把与对象类型相关的所有权限全部授权。

一个特殊的名为PUBLIC的”角色”可以用来向系统中的每一个角色授予一个权限。同时，在数据库中有很多用户时可以设置”组”角色来帮助管理权限。

为了撤销一个权限，使用REVOKE 命令：

REVOKE ALL ON accounts FROM PUBLIC;

对象拥有者的特殊权限（即执行DROP、GRANT、REVOKE等的权力）总是隐式地属于拥有者，并且不能被授予或撤销。但是对象拥有者可以选择撤销他们自己的普通权限，例如把一个表变得对他们自己和其他人只读。

一般情况下，只有对象拥有者（或者超级用户）可以授予或撤销一个对象上的权限。但是可以在授予权限时使用”with grant option”来允许接收人将权限转授给其他人。如果后来授予选项被撤销，则所有从接收人那里获得的权限（直接或者通过授权链获得）都将被撤销。

更多详情请见GRANT和REVOKE参考页。

The available privileges are:

SELECT

允许 SELECT 从任何列、或特定的列、表、视图、物化视图、或其他类似表格的对象。

也允许使用 COPY TO. 还需要这个权限来引用UPDATE 或 DELETE中现有的列值。 对于序列，这个权限还允许使用currval 函数。对于大对象，此权限允许读取对象。

INSERT

允许将新行的

INSERT 加入表、视图等等。 可以在特定列上授予，在这种情

况下INSERT命令中只有那些列可以被分配（其他列将因此而收到默认值）。 还允许使用COPY FROM。

UPDATE

允许 UPDATE 更新任何列、或指定列、表、视图等等。 (实际上，任何有效的UPDATE命令也需要SELECT权限，因为它必须引用表列来确定要更新的行，和/或计算列的新值。)

SELECT... FOR UPDATE和SELECT... FOR SHARE除了SELECT权限外，还需要至少一列上的这个权限。 对于序列，这个权限允许使用 nextval 和 setval 函数。对于大对象，此权限允许写入或截断对象。

DELETE

允许

DELETE 从表、视图等等中删除行. (实际上，任何有效的DELETE命令也需要SELECT权限，因为它必须引用表列来确定要删除的行。)

TRUNCATE

允许在表、视图等等上 TRUNCATE 。

REFERENCES

允许创建引用表或表的特定列的外键约束。

TRIGGER

允许在表、视图等等上创建触发器。

CREATE

对于数据库，允许在数据库中创建新的模式和发布。

对于模式，允许在模式中创建新对象。要重命名现有对象，你必须拥有对象 and所包含模式的此权限。

对于表空间，允许在表空间中创建表、索引和临时文件，并允许创建将表空间作为默认表空间的数据库。（注意，撤销此特权不会更改已有对象的位置。）

CONNECT

允许受让者连接到数据库。此权限在连接启动时进行检查(加之pg\_hba.conf施加的任何约束).

TEMPORARY

允许在使用数据库时创建临时表。

EXECUTE

允许调用函数或过程，包括使用在函数之上实现的任何运算符。这是适用于函数和过程的唯一权限类型。

USAGE

对于程序语言，允许使用语言来创建该语言的函数。 这是适用于过程语言的唯一权限类型。

对于模式，允许访问模式中包含的对象（假设对象自己的权限要求也已得到满足）。 从本质上讲，这允许受让者”look up”模式中的对象。如果没有此权限，仍可以看到对象名称，例如通过查询系统目录。 此外，在撤消此权限后，现有会话可能还具有以前执行过此查找的语句，因此这不是阻止对象访问的彻底安全的方法。

对于序列, 允许使用currval 和 nextval 函数.

对于类型和域，允许在创建表、函数和其他模式对象时使用类型或域。 （注意，此权限不控制类型的全部 “usage” ，例如查询中出现的类型的值。 它仅防止创建依赖于类型的对象。 此权限的主要目的是控制哪些用户可以对类型创建依赖项，这可能会防止所有者以后更改类型。 ）

对于外部数据包装器，允许使用外部数据包装器创建新服务器。

对于外部服务器，允许使用服务器创建外部表。受让者还可以创建、更改或删除与该服务器关联的自己的用户映射。

其他命令所需的权限罗列在相应命令的参考页上。

在创建对象时，瀚高数据库默认将某些类型对象的权限授予PUBLIC。 默认情况下，在表、表列、序列、外部数据包装器、外部服务器、大型对象、模式或表空间上，不向PUBLIC授予权限。 对于其他类型的对象，授予 PUBLIC的默认权限如下所示： 针对数据库的CONNECT和TEMPORARY（创建临时表）权限; 针对函数和程序的EXECUTE权限;以及针对语言和数据类型（包括域）的USAGE权限。 当然，对象所有者可以REVOKE默认权限和特别授予的权限。 （为了最大程度的安全性，在创建对象的同一事务中发出REVOKE;那么就没有其他用户能够使用该对象的窗口。） 此外，可以使用ALTER DEFAULT PRIVILEGES命令取代这些默认权限设置。

表4.1显示了ACL（访问控制列表）值中用于这些权限类型的单字母缩写。

**表 4.1 ACL 权限缩写**

| 权限 | 缩写 | 适用对象类型 |
| --- | --- | --- |
| SELECT | r (“读”) | LARGE OBJECT, SEQUENCE, TABLE (and table-like objects), table column |
| INSERT | a (“增补”) | TABLE, table column |
| UPDATE | w (“写”) | LARGE OBJECT, SEQUENCE, TABLE, table column |
| DELETE | d | TABLE |
| TRUNCATE | D | TABLE |
| REFERENCES | x | TABLE, table column |
| TRIGGER | t | TABLE |
| CREATE | C | DATABASE, SCHEMA, TABLESPACE |
| CONNECT | c | DATABASE |
| TEMPORARY | T | DATABASE |
| EXECUTE | X | FUNCTION, PROCEDURE |
| USAGE | U | DOMAIN, FOREIGN DATA WRAPPER, FOREIGN SERVER, LANGUAGE, SCHEMA, SEQUENCE, TYPE |

表 4.2 使用上面所示的缩写总结了每种类型 SQL 对象可用的权限。它还显示可用于检查每种对象类型的特权设置的 psql 命令。

**表 4.2 访问权限摘要**

| 对象类型 | 所有权限 | 默认 PUBLIC 权限 | psql 命令 |
| --- | --- | --- | --- |
| DATABASE | CTc | Tc | \\l |
| DOMAIN | U | U | \\dD+ |
| FUNCTION or PROCEDURE | X | X | \\df+ |
| FOREIGN DATA WRAPPER | U | none | \\dew+ |
| FOREIGN SERVER | U | none | \\des+ |
| LANGUAGE | U | U | \\dL+ |
| LARGE OBJECT | rw | none | — |
| SCHEMA | UC | none | \\dn+ |
| SEQUENCE | rwU | none | \\dp |
| TABLE (and table like objects) | arwdDxt | none | \\dp |
| Table column | arwx | none | \\dp |
| TABLESPACE | C | none | \\db+ |
| TYPE | U | U | \\dT+ |

已授予特定对象的权限显示为aclitem项的列表，其中每个aclitem项描述了特定授予者授予给一个被授与者的权限。 例如，calvin=r\*w/hobbes 指明角色calvin具有SELECT（r）权限和授予选项（\*）以及不可授予权限UPDATE（w），均由角色hobbes授予。 如果calvin对 由其他授予人授予的同一对象也具有一些权限，那将显示为单独的aclitem条目。 aclitem中的空受赠方字段代表PUBLIC。

例如，假设用户miriam创建了表mytable并且:

GRANT SELECT ON mytable TO PUBLIC;

GRANT SELECT, UPDATE, INSERT ON mytable TO admin;

GRANT SELECT (col1), UPDATE (col1) ON mytable TO miriam\_rw;

则 psql的 \\dp 命令将显示:

\=> \\dp mytable

Access privileges

Schema | Name | Type | Access privileges | Column privileges |

Policies

\-#-#-#-#+-#-#-#-#-+-#-#-#-+-#-#-#-#-#-#-#-#-#-#-#-+-#-#-#-#-#-#-#-#-#-#-#-+-#-#-

#-#-#

public | mytable | table | miriam=arwdDxt/miriam+| col1: +|

| | | =r/miriam +| miriam\_rw=rw/miriam |

| | | admin=arw/miriam | |

(1 row)

如果”Access privileges”列对于给定对象为空，则表示该对象具有默认权限（也就是说，它在相关系统目录中的权限条目为空）。 默认权限始终包含所有者的所有权限，并且可以包括 PUBLIC 的一些权限，具体取决于对象类型，如上所述。 对象上的第一个GRANT或REVOKE将实例化默认权限（例如，生成miriam\_arwdDxt/ miriam），然后根据指定的请求修改它们。 类似的，只有具有非默认特权的列的条目才显示在”Column privileges”中。（注意：为此目的，”default privileges”始终表示对象类型的内置缺省权限。其权限受ALTER DEFAULT PRIVILEGES 命令影响的对象将始终显示一个显式权限条目，其中包含 ALTER。）

注意所有者的隐式授予选项没有在访问权限显示中标记。仅当授予选项被显式授予给某人时才会出现\*。

## 行安全性策略

除可以通过GRANT使用 SQL 标准的 特权系统之外，表还可以具有 行安全性策略，它针对每一个用户限制哪些行可以 被普通的查询返回或者可以被数据修改命令插入、更新或删除。

这种 特性也被称为行级安全性。默认情况下，表不具有 任何策略，这样用户根据 SQL 特权系统具有对表的访问特权，对于 查询或更新来说其中所有的行都是平等的。

当在一个表上启用行安全性时（使用 ALTER TABLE... ENABLE ROW LEVEL SECURITY），所有对该表选择行或者修改行的普通访问都必须被一条 行安全性策略所允许（不过，表的拥有者通常不服从行安全性策略）。如果 表上不存在策略，将使用一条默认的否定策略，即所有的行都不可见或者不能被修改。应用在整个表上的操作不服从行安全性，例如TRUNCATE和 REFERENCES。

行安全性策略可以针对特定的命令、角色或者两者。一条策略可以被指定为 适用于ALL命令，或者SELECT、 INSERT、UPDATE、或者DELETE。 可以为一条给定策略分配多个角色，并且通常的角色成员关系和继承规则也适用。

要指定哪些行根据一条策略是可见的或者是可修改的，需要一个返回布尔结果的表达式。

对于每一行，在计算任何来自用户查询的条件或函数之前，先会计 算这个表达式（这条规则的唯一例外是leakproof函数， 它们被保证不会泄露信息，优化器可能会选择在行安全性检查之前应用这类 函数）。使该表达式不返回true的行将不会被处理。可以指定 独立的表达式来单独控制哪些行可见以及哪些行被允许修改。策略表达式会作 为查询的一部分运行并且带有运行该查询的用户的特权，但是安全性定义者函数 可以被用来访问对调用用户不可用的数据。

具有BYPASSRLS属性的超级用户和角色在访问一个表时总是 可以绕过行安全性系统。表拥有者通常也能绕过行安全性，不过表拥有者 可以选择用ALTER TABLE... FORCE ROW LEVEL SECURITY来服从行安全性。

启用和禁用行安全性以及向表增加策略是只有表拥有者具有的特权。

策略的创建可以使用CREATE POLICY命令，策略的修改 可以使用ALTER POLICY命令，而策略的删除可以使用 DROP POLICY命令。要为一个给定表启用或者禁用行安全性，可以使用ALTER TABLE命令。

每一条策略都有名称并且可以为一个表定义多条策略。由于策略是表相关的，一个表的每一条策略都必须有一个唯一的名称。不同的表可以拥有相同名称的策略。

当多条策略适用于一个给定的查询时，会把它们用OR（对宽容性策略，默认的策略类型）或者AND（对限制性策略）组合在一起。这和给定角色拥有它作为成员的所有角色的特权的规则类似。宽容性策略和限制性策略在下文将会进一步讨论。

作为一个简单的例子，这里是如何在account关系上 创建一条策略以允许只有managers角色的成员能访问行， 并且只能访问它们账户的行：

CREATE TABLE accounts (manager text, company text, contact\_email text);

ALTER TABLE accounts ENABLE ROW LEVEL SECURITY;

CREATE POLICY account\_managers ON accounts TO managers

USING (manager = current\_user);

上面的策略隐含地提供了一个与其该约束适用于被一个命令选择的行（这样一个经理不能SELECT、UPDATE或者DELETE属于其他经理的已有行）以及被一个命令修改的行（这样属于其他经理的行不能通过INSERT或者UPDATE创建）。

如果没有指定角色或者使用了特殊的用户名PUBLIC， 则该策略适用于系统上所有的用户。

要允许所有用户访问users 表中属于他们自己的行，可以使用一条简单的策略：

CREATE POLICY user\_policy ON users

USING (user\_name = current\_user);

这个例子的效果和前一个类似。

为了对增加到表中的行使用与可见行不同的策略，可以组合多条策略。这一对策略将允许所有用户查看users表中的所有行，但只能修改他们自己的行：

CREATE POLICY user\_sel\_policy ON users

FOR SELECT

USING (true);

CREATE POLICY user\_mod\_policy ON users

USING (user\_name = current\_user);

在一个SELECT命令中，这两条规则被用OR组合在一起，最终的效应就是所有的行都能被选择。在其他命令类型中，只有第二条策略适用，这样其效果就和以前相同。

也可以用ALTER TABLE命令禁用行安全性。禁用行安全性 不会移除定义在表上的任何策略，它们只是被简单地忽略。然后该表中的所有 行都是可见的并且可修改，服从于标准的 SQL特权系统。

下面是一个较大的例子，它展示了这种特性如何被用于生产环境。表 passwd模拟了一个Unix 口令文件：

\-# 简单的口令文件例子

CREATE TABLE passwd (

user\_name text UNIQUE NOT NULL,

pwhash text,

uid int PRIMARY KEY,

gid int NOT NULL,

real\_name text NOT NULL,

home\_phone text,

extra\_info text,

home\_dir text NOT NULL,

shell text NOT NULL

);

CREATE ROLE admin; -# 管理员

CREATE ROLE bob; -# 普通用户

CREATE ROLE alice; -# 普通用户

\-# 填充表

INSERT INTO passwd VALUES

('admin','xxx',0,0,'Admin','111-222-3333',null,'/root','/bin/dash');

INSERT INTO passwd VALUES

('bob','xxx',1,1,'Bob','123-456-6890',null,'/home/bob','/bin/zsh');

INSERT INTO passwd VALUES

('alice','xxx',2,1,'Alice','098-665-4321',null,'/home/alice','/bin/zsh');

\-# 确保在表上启用行级安全性

ALTER TABLE passwd ENABLE ROW LEVEL SECURITY;

\-# 创建策略

\-# 管理员能看见所有行并且增加任意行

CREATE POLICY admin\_all ON passwd TO admin USING (true) WITH CHECK (true);

\-# 普通用户可以看见所有行

CREATE POLICY all\_view ON passwd FOR SELECT USING (true);

\-# 普通用户可以更新它们自己的记录，但是限制普通用户可用的 shell

CREATE POLICY user\_mod ON passwd FOR UPDATE

USING (current\_user = user\_name)

WITH CHECK (

current\_user = user\_name AND

shell IN ('/bin/bash','/bin/sh','/bin/dash','/bin/zsh','/bin/tcsh')

);

\-# 允许管理员有所有普通权限

GRANT SELECT, INSERT, UPDATE, DELETE ON passwd TO admin;

\-# 用户只在公共列上得到选择访问

GRANT SELECT

(user\_name, uid, gid, real\_name, home\_phone, extra\_info, home\_dir, shell)

ON passwd TO public;

\-# 允许用户更新特定行

GRANT UPDATE

(pwhash, real\_name, home\_phone, extra\_info, shell)

ON passwd TO public;

对于任意安全性设置来说，重要的是测试并确保系统的行为符合预期。 使用上述的例子，下面展示了权限系统工作正确：

\-# admin 可以看到所有的行和域

highgo=> set role admin;

SET

highgo=> table passwd;

user\_name | pwhash | uid | gid | real\_name | home\_phone | extra\_info |

home\_dir | shell

\-#-#-#-#-#-+-#-#-#-#+-#-#-+-#-#-+-#-#-#-#-#-+-#-#-#-#-#-#-#+-#-#-#-#-#-#+-#-#-#-

#-#-#-+-#-#-#-#-#-

admin | xxx | 0 | 0 | Admin | 111-222-3333 | | /root

| /bin/dash

bob | xxx | 1 | 1 | Bob | 123-456-6890 | | /home/

bob | /bin/zsh

alice | xxx | 2 | 1 | Alice | 098-665-4321 | | /home/

alice | /bin/zsh

(3 rows)

\-# 测试 Alice 能做什么

highgo=> set role alice;

SET

highgo=> table passwd;

ERROR: permission denied for relation passwd

highgo=> select user\_name,real\_name,home\_phone,extra\_info,home\_dir,shell from

passwd;

user\_name | real\_name | home\_phone | extra\_info | home\_dir | shell

\-#-#-#-#-#-+-#-#-#-#-#-+-#-#-#-#-#-#-#+-#-#-#-#-#-#+-#-#-#-#-#-#-+-#-#-#-#-#-

admin | Admin | 111-222-3333 | | /root | /bin/dash

bob | Bob | 123-456-6890 | | /home/bob | /bin/zsh

alice | Alice | 098-665-4321 | | /home/alice | /bin/zsh

(3 rows)

highgo=> update passwd set user\_name = 'joe';

ERROR: permission denied for relation passwd

\-# Alice 被允许更改她自己的 real\_name，但不能改其他的

highgo=> update passwd set real\_name = 'Alice Doe';

UPDATE 1

highgo=> update passwd set real\_name = 'John Doe' where user\_name = 'admin';

UPDATE 0

highgo=> update passwd set shell = '/bin/xx';

ERROR: new row violates WITH CHECK OPTION for "passwd"

highgo=> delete from passwd;

ERROR: permission denied for relation passwd

highgo=> insert into passwd (user\_name) values ('xxx');

ERROR: permission denied for relation passwd

\-# Alice 可以更改她自己的口令；行级安全性会悄悄地阻止更新其他行

highgo=> update passwd set pwhash = 'abc';

UPDATE 1

目前为止所有构建的策略都是宽容性策略，也就是当多条策略都适用时会被适用”OR”布尔操作符组合在一起。而宽容性策略可以被用来仅允许在预计情况中对行的访问，这比将宽容性策略与限制性策略（记录必须通过这类策略并且它们会被”AND”布尔操作符组合起来）组合在一起更简单。在上面的例子之上，我们增加一条限制性策略要求通过一个本地Unix套接字连接过来的管理员访问passwd表的记录：

CREATE POLICY admin\_local\_only ON passwd AS RESTRICTIVE TO admin

USING (pg\_catalog.inet\_client\_addr() IS NULL);

然后，由于这条限制性规则的存在，我们可以看到从网络连接进来的管理员将无法看到任何记录：

\=> SELECT current\_user;

current\_user

\-#-#-#-#-#-#-#

admin

(1 row)

\=> select inet\_client\_addr();

inet\_client\_addr

\-#-#-#-#-#-#-#-#-#

126.0.0.1

(1 row)

\=> SELECT current\_user;

current\_user

\-#-#-#-#-#-#-#

admin

(1 row)

\=> TABLE passwd;

user\_name | pwhash | uid | gid | real\_name | home\_phone | extra\_info | home\_dir

| shell

\-#-#-#-#-#-+-#-#-#-#+-#-#-+-#-#-+-#-#-#-#-#-+-#-#-#-#-#-#+-#-#-#-#-#-#+-#-#-#-#-

#+-#-#-#-

(0 rows)

\=> UPDATE passwd set pwhash = NULL;

UPDATE 0

参照完整性检查（例如唯一或逐渐约束和外键引用）总是会绕过行级安全性以 保证数据完整性得到维护。在开发模式和行级安全性时必须小心避免 “隐通道”通过这类参照完整性检查泄露信息。

在某些环境中确保行安全性没有被应用很重要。例如，在做备份时，如果 行安全性悄悄地导致某些行被从备份中忽略掉，这会是灾难性的。在这类 情况下，你可以设置row\_security配置参数为 off。这本身不会绕过行安全性，它所做的是如果任何结果会 被一条策略过滤掉，就会抛出一个错误。然后错误的原因就可以被找到并且修复。

在上面的例子中，策略表达式只考虑了要被访问的行中的当前值。这是最简 单并且表现最好的情况。如果可能，最好设计行安全性应用以这种方式工作。 如果需要参考其他行或者其他表来做出策略的决定，可以在策略表达式中通过 使用子-SELECT或者包含SELECT的函数来实现。不过要注意这类访问可能会导致竞争条件，在不小心的情况下这可能 会导致信息

泄露。作为一个例子，考虑下面的表设计：

\-# 特权组的定义

CREATE TABLE groups (group\_id int PRIMARY KEY,

group\_name text NOT NULL);

INSERT INTO groups VALUES

(1, 'low'),

(2, 'medium'),

(5, 'high');

GRANT ALL ON groups TO alice; -# alice 是管理员

GRANT SELECT ON groups TO public;

\-# 用户的特权级别的定义

CREATE TABLE users (user\_name text PRIMARY KEY,

group\_id int NOT NULL REFERENCES groups);

INSERT INTO users VALUES

('alice', 5),

('bob', 2),

('mallory', 2);

GRANT ALL ON users TO alice;

GRANT SELECT ON users TO public;

\-# 保存要被保护的信息的表

CREATE TABLE information (info text,

group\_id int NOT NULL REFERENCES groups);

INSERT INTO information VALUES

('barely secret', 1),

('slightly secret', 2),

('very secret', 5);

ALTER TABLE information ENABLE ROW LEVEL SECURITY;

\-# 对于安全性 group\_id 大于等于一行的 group\_id 的用户，

\-# 这一行应该是可见的/可更新的

CREATE POLICY fp\_s ON information FOR SELECT

USING (group\_id <= (SELECT group\_id FROM users WHERE user\_name =

current\_user));

CREATE POLICY fp\_u ON information FOR UPDATE

USING (group\_id <= (SELECT group\_id FROM users WHERE user\_name =

current\_user));

\-# 我们只依赖于行级安全性来保护信息表

GRANT ALL ON information TO public;

现在假设alice希望更改”有一点点秘密” 的信息，但是觉得mallory不应该看到该行中的新内容，因此她这样做：

BEGIN;

UPDATE users SET group\_id = 1 WHERE user\_name = 'mallory';

UPDATE information SET info = 'secret from mallory' WHERE group\_id = 2;

COMMIT;

这看起来是安全的，没有窗口可供mallory看到 “对 mallory 保密”的字符串。不过，这里有一种 竞争条件。如果mallory正在并行地做：

SELECT \* FROM information WHERE group\_id = 2 FOR UPDATE;

并且她的事务处于READ COMMITTED模式，她就可能看到 “s对 mallory 保密”的东西。如果她的事务在alice 做完之后就到达信息行，这就会发生。它会阻塞等待 alice的事务提交，然后拜FOR UPDATE子句所赐 取得更新后的行内容。不过，对于来自users的隐式 SELECT，它不会取得一个已更新的行， 因为子-SELECT没有FOR UPDATE，相反 会使用查询开始时取得的快照读取users行。因此， 策略表达式会测试mallory的特权级别的旧值并且允许她看到被更新的行。

有多种方法能解决这个问题。一种简单的答案是在行安全性策略中的 子-SELECT里使用SELECT... FOR SHARE。 不过，这要求在被引用表（这里是users）上授予 UPDATE特权给受影响的用户，这可能不是我们想要的（ 但是另一条行安全性策略可能被应用来阻止它们实际使用这个特权，或者 子-SELECT可能被嵌入到一个安全性定义者函数中）。还有，在被引用的表上过多并发地使用行共享锁可能会导致性能问题，特别是表更新比较频繁时。另一种解决方案（如果被引用表上的更新 不频繁就可行）是在更新被引用表时对它取一个排他锁，这样就没有并发事务能够检查旧的行值了。或者我们可以在提交对被引用表的更新之后、在做依赖于新安全性情况的更改之前等待所有并发事务结束。

更多细节请见CREATE POLICY 和ALTER TABLE。

## 模式

一个瀚高数据库数据库集簇中包含一个或更多命名的数据库。用户和用户组被整个集簇共享，但没有其他数据在数据库之间共享。任何给定客户端连接只能访问在连接中指定的数据库中的数据。

| 注意： |
| --- |
| 一个集簇的用户并不必拥有访问集簇中每一个数据库的权限。用户名的共享意味着不可能在同一个集簇中出现重名的不同用户，例如两个数据库中都有。 |

一个数据库包含一个或多个命名模式，模式中包含着表。模式还包含其他类型的命名对象，包括数据类型、函数和操作符。相同的对象名称可以被用于不同的模式中二不会出现冲突，例如schema1和myschema都可以包含名为mytable的表。和数据库不同，模式并不是被严格地隔离：一个用户可以访问他们所连接的数据库中的所有模式内的对象，只要他们有足够的权限。

下面是一些使用方案的原因：

• 允许多个用户使用一个数据库并且不会互相干扰。

• 将数据库对象组织成逻辑组以便更容易管理。

• 第三方应用的对象可以放在独立的模式中，这样它们就不会与其他对象的名称发生冲突。

模式类似于操作系统层的目录，但是模式不能嵌套。

### 创建模式

要创建一个模式，可使用CREATE SCHEMA命令，并且给出选择的模式名称。例如：

CREATE SCHEMA myschema;

在一个模式中创建或访问对象，需要使用由模式名和表名构成的限定名，模式名和表名之间以点号分隔：

schema.table

在任何需要一个表名的地方都可以这样用，包括表修改命令和后续章节要讨论的数据访问命令（为了简洁我们在这里只谈到表，但是这种方式对其他类型的命名对象同样有效，例如类型和函数）。

事实上，还有更加通用的语法：

database.schema.table

也可以使用，但是目前它只是在形式上与SQL标准兼容。如果我们写一个数据库名称，它必须是我们正在连接的数据库。

因此，如果要在一个新模式中创建一个表，可用：

CREATE TABLE myschema.mytable (

...

);

要删除一个为空的模式（其中的所有对象已经被删除），可用：

DROP SCHEMA myschema;

要删除一个模式以及其中包含的所有对象，可用：

DROP SCHEMA myschema CASCADE;

有关于此的更一般的机制请参见第 4.14 节。

我们常常希望创建一个由其他人所拥有的模式（因为这是将用户动作限制在良定义的名字空间中的方法之一）。其语法是：

CREATE SCHEMA schema\_name AUTHORIZATION user\_name;

我们甚至可以省略模式名称，在此种情况下模式名称将会使用用户名，参见第 4.9.6 节。

以pg\_开头的模式名被保留用于系统目的，所以不能被用户所创建。

### 公共模式

在前面的小节中，我们创建的表都没有指定任何模式名称。默认情况下这些表（以及其他对象）会自动的被放入一个名为”public”的模式中。任何新数据库都包含这样一个模式。因此，下面的命令是等效的：

CREATE TABLE products (... );

以及：

CREATE TABLE public.products (... );

### 模式搜索路径

限定名写起来很冗长，通常最好不要把一个特定模式名拉到应用中。因此，表名通常被使用非限定名来引用，它只由表名构成。系统将沿着一条搜索路径来决定该名称指的是哪个表，搜索路径是一个进行查看的模式列表。 搜索路径中第一个匹配的表将被认为是所需要的。如果在搜索路径中没有任何匹配，即使在数据库的其他模式中存在匹配的表名也将会报告一个错误。

在不同方案中创建命名相同的对象的能力使得编写每次都准确引用相同对象的查询变得复杂。这也使得用户有可能更改其他用户查询的行为，不管是出于恶意还是无意。由于未经限定的名称在查询中以及在瀚高数据库内部的广泛使用，在search\_path中增加一个方案实际上是信任所有在该方案中具有CREATE特权的用户。在你运行一个普通查询时，恶意用户可以在你的搜索路径中的以方案中创建能够夺取控制权并且执行任意SQL函数的对象，而这些事情就像是你在执行一样。

搜索路径中的第一个模式被称为当前模式。除了是第一个被搜索的模式外，如果CREATE TABLE命令没有指定模式名，它将是新创建表所在的模式。

要显示当前搜索路径，使用下面的命令：

SHOW search\_path;

在默认设置下这将返回：

search\_path

\-#-#-#-#-#-#-#

"$user", public

第一个元素说明一个和当前用户同名的模式会被搜索。如果不存在这个模式，该项将被忽略。第二个元素指向我们已经见过的公共模式。

搜索路径中的第一个模式是创建新对象的默认存储位置。这就是默认情况下对象会被创建在公共模式中的原因。当对象在任何其他没有模式限定的环境中被引用（表修改、数据修改或查询命令）时，搜索路径将被遍历直到一个匹配对象被找到。因此，在默认配置中，任何非限定访问将只能指向公共模式。

要把新模式放在搜索路径中，我们可以使用：

SET search\_path TO myschema,public;

（我们在这里省略了$user，因为我们并不立即需要它）。然后我们可以删除该表而无需使用方案进行限定：

DROP TABLE mytable;

同样，由于myschema是路径中的第一个元素，新对象会被默认创建在其中。

我们也可以这样写：

SET search\_path TO myschema;

这样我们在没有显式限定时再也不必去访问公共模式了。公共模式没有什么特别之处，它只是默认存在而已，它也可以被删除。

其他操作模式搜索路径的方法请见第 8.25 节。

搜索路径对于数据类型名称、函数名称和操作符名称的作用与表名一样。数据类型和函数名称可以使用和表名完全相同的限定方式。如果我们需要在一个表达式中写一个限定的操作符名称，我们必须写成一种特殊的形式：

OPERATOR(schema.operator)

这是为了避免句法歧义。例如：

SELECT 3 OPERATOR(pg\_catalog.+) 4;

实际上我们通常都会依赖于搜索路径来查找操作符，因此没有必要去写如此”丑陋”的东西。

### 模式和权限

默认情况下，用户不能访问不属于他们的方案中的任何对象。要允许这种行为，模式的拥有者必须在该模式上授予USAGE权限。为了允许用户使用方案中的对象，可能还需要根据对象授予额外的权限。

一个用户也可以被允许在其他某人的模式中创建对象。要允许这种行为，模式上的CREATE权限必须被授予。注意在默认情况下，所有人都拥有在public模式上的CREATE和USAGE权限。

这使得用户能够连接到一个给定数据库并在它的public模式中创建对象。回收这一特权的使用模式调用：

REVOKE CREATE ON SCHEMA public FROM PUBLIC;

（第一个”public”是方案，第二个”public”指的是”每一个用户”。第一种是一个标识符，第二种是一个关键词，所以两者的大小写不同。请回想第 3.1.1 节中的指导方针。）

### 系统目录模式

除public和用户创建的模式之外，每一个数据库还包括一个pg\_catalog模式，它包含了系统表和所有内建的数据类型、函数以及操作符。pg\_catalog总是搜索路径的一个有效部分。如果没有在路径中显式地包括该模式，它将在路径中的模式之前被搜索。这保证了内建的名称总是能被找到。然而，如果我们希望用用户定义的名称重载内建的名称，可以显式的将pg\_catalog放在搜索路径的末尾。

由于系统表名称以pg\_开头，最好还是避免使用这样的名称，以避免和未来新版本中 可能出现的系统表名发生冲突。系统表将继续采用以pg\_开头的方式，这样它们不会 与非限制的用户表名称冲突。

### 使用模式

模式能够以多种方式组织数据.secure schema usage pattern防止不受信任的用户更改其他用户查询的行为。 当数据库不使用安全模式使用方式时，希望安全地查询该数据库的用户将在每个会话开始时采取保护操作。 具体的说，他们将通过设置search\_path到空字符串或在其它情况下从search\_path中删除非超级用户可写的模式来开始每个会话。 默认配置可以很容易的支持一些使用模式。

• 将普通用户约束在其私有的方案中。要实现这一点，发出REVOKE CREATE ON SCHEMA public FROM PUBLIC，并且为每一个用户创建一个用其用户名命名的方案。 回想一下以$user开头的默认搜索路径，该路径解析为用户名。 因此，如果每个用户都有单独的模式，则默认情况下他们访问自己的模式。 在不受信任的用户已经登录的数据库中采用此模式后，请考虑审计名字类似于模式pg\_catalog中的对象的公共模式。 此方式是一种安全模式的使用方式，除非不受信任的用户是数据库所有者或拥有CREATEROLE权限，在这种情况下没有安全模式使用方式存在。

• 从默认搜索路径中删除公共模式，通过修改Highgo.conf或通过发出ALTER ROLE ALL SET search\_path ="$user"。 每一个都保留在公共模式中创建对象的能力，但是只有符合资格的名称才会选择这些对象。 虽然符合资格的表引用是可以的，但是要调用公共模式中的函数will be unsafe or unreliable。 如果在公共模式中创建函数或扩展，请改用第一个方式。 否则，与第一个模式一样，这是安全的，除非不受信任的用户是数据库所有者或拥有CREATEROLE权限。

• 保持默认。所有用户都隐式地访问公共模式。这模拟了方案根本不可用的情况，可以用于从无模式感知的世界平滑过渡。 但是，这绝不是一个安全的模式。只有当数据库仅有单个用户或者少数相互信任的用户时，才可以接受。

对于任何一种模式，为了安装共享的应用（所有人都要用其中的表，第三方提供的额外函数，等等），可把它们放在单独的方案中。记住授予适当的特权以允许其他用户访问它们。然后用户可以通过以方案名限定名称的方式来引用这些额外的对象，或者他们可以把额外的方案放在自己的搜索路径中。

### 可移植性

在SQL标准中，在由不同用户拥有的同一个模式中的对象是不存在的。此外，某些实现不允许创建与拥有者名称不同名的模式。事实上，在那些仅实现了标准中基本模式支持的数据库中，模式和用户的概念是等同的。因此，很多用户认为限定名称实际上是由user\_name.table\_name组成的。如果我们为每一个用户都创建了一个模式，瀚高数据库实际也是这样认为的。

同样，在SQL标准中也没有public模式的概念。为了最大限度的与标准一致，我们不应使用（甚至是删除）public模式。

当然，某些SQL数据库系统可能根本没有实现方案，或者提供允许跨数据库访问的名字空 。

## 继承

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

另一种得到同样效果的方法是使用regclass别名类型， 它将象征性地打印出表的 OID：

SELECT c.tableoid::regclass, c.name, c.altitude

FROM cities c

WHERE c.altitude > 500;

继承不会自动地将来自INSERT或COPY命令的数据传播到继承层次中的其他表中。在我们的例子中，下面的INSERT语句将会失败：

INSERT INTO cities (name, population, altitude, state)

VALUES ('Albany', NULL, NULL, 'NY');

我们也许希望数据能被以某种方式被引入到capitals表中，但是这不会发生：INSERT总是向指定的表中插入。在某些情况下，可以通过使用一个规则（见第 40 章）来将插入动作重定向。但是这对上面的情况并没有帮助，因为cities表根本就不包含state列，因而这个命令将在触发规则之前就被拒绝。

父表上的所有检查约束和非空约束都将自动被它的后代所继承，除非显式地指定了NO INHERIT子句。其他类型的约束（唯一、主键和外键约束）则不会被继承。

一个表可以从超过一个的父表继承，在这种情况下它拥有父表们所定义的列的并集。任何定义在子表上的列也会被加入到其中。如果在这个集合中出现重名列，那么这些列将被”合并”，这样在子表中只会有一个这样的列。重名列能被合并的前提是这些列必须具有相同的数据类型，否则会导致错误。可继承的检查约束和非空约束会以类似的方式被合并。例如，如果合并成一个合并列的任一列定义被标记为非空，则该合并列会被标记为非空。如果检查约束的名称相同，则他们会被合并，但如果它们的条件不同则合并会失败。

表继承通常是在子表被创建时建立，使用CREATE TABLE语句的INHERITS子句。一个已经被创建的表也可以另外一种方式增加一个新的父亲关系，使用ALTER TABLE的INHERIT变体。要这样做，新的子表必须已经包括和父表相同名称和数据类型的列。子表还必须包括和父表相同的检查约束和检查表达式。相似地，一个继承链接也可以使用ALTER TABLE的 NO INHERIT变体从一个子表中移除。动态增加和移除继承链接可以用于实现表划分（见第 5.11 节）。

一种创建一个未来将被用做子女的新表的方法是在CREATE TABLE中使用LIKE子句。这将创建一个和源表具有相同列的新表。如果源表上定义有任何CHECK约束，LIKE的INCLUDING CONSTRAINTS选项可以用来让新的子表也包含和父表相同的约束。

当有任何一个子表存在时，父表不能被删除。当子表的列或者检查约束继承于父表时，它们也不能被删除或修改。如果希望移除一个表和它的所有后代，一种简单的方法是使用CASCADE选项删除父表（见第 5.14 节）。

ALTER TABLE将会把列的数据定义或检查约束上的任何变化沿着继承层次向下传播。同样，删除被其他表依赖的列只能使用CASCADE选项。ALTER TABLE对于重名列的合并和拒绝遵循与CREATE TABLE同样的规则。

继承的查询仅在附表上执行访问权限检查。例如，在cities表上授予UPDATE权限也隐含着通过cities访问时在capitals表中更新行的权限。 这保留了数据（也）在父表中的样子。但是如果没有额外的授权，则不能直接更新capitals表。 此规则的两个例外是TRUNCATE 和 LOCK TABLE，总是检查子表的权限，不管它们是直接处理还是通过在父表上执行的那些命令递归处理。

以类似的方式，父表的行安全性策略（见第 4.8 节）适用于继承查询期间来自于子表的行。 只有当子表在查询中被明确提到时，其策略（如果有）才会被应用，在那种情况下，附着在其父表上的任何策略都会被忽略。

外部表（见第 4.12 节）也可以是继承层次 中的一部分，即可以作为父表也可以作为子表，就像常规表一样。如果 一个外部表是继承层次的一部分，那么任何不被该外部表支持的操作也不被整个层次所支持。

### 警告

注意并非所有的SQL命令都能工作在继承层次上。用于数据查询、数据修改或模式修改（例如SELECT、UPDATE、DELETE、大部分ALTER TABLE的变体，但INSERT或ALTER TABLE... RENAME不在此列）的命令会默认将子表包含在内并且支持ONLY记号来排除子表。负责数据库维护和调整的命令（如REINDEX、VACUUM）只工作在独立的、物理的表上并且不支持在继承层次上的递归。每个命令相应的行为请参见它们的参考页（SQL 命令）。

继承特性的一个严肃的限制是索引（包括唯一约束）和外键约束值应用在单个表上而非它们的继承子女。在外键约束的引用端和被引用端都是这样。因此，按照上面的例子：

• 如果我们声明cities.name为UNIQUE或者PRIMARY KEY，这将不会阻止capitals表中拥有和cities中城市同名的行。而且这些重复的行将会默认显示在cities的查询中。事实上，capitals在默认情况下是根本不能拥有唯一约束的，并且因此能够包含多个同名的行。我们可以为capitals增加一个唯一约束，但这无法阻止相对于cities的重复。

• 相似地，如果我们指定cities.name REFERENCES某个其他表，该约束不会自动地传播到capitals。在此种情况下，我们可以变通地在capitals上手工创建一个相同的REFERENCES约束。

• 指定另一个表的列REFERENCES cities(name)将允许其他表包含城市名称，但不会包含首府名称。这对于这个例子不是一个好的变通方案。

某些未为继承层次结构实现的功能是为声明性分区实现的。在决定使用旧继承进行分区是否对应用程序有用时，需要非常小心。

## 表分区

瀚高数据库支持基本的表划分。本小节介绍为何以及怎样把划分实现为数据库设计的一部分。

### 概述

划分指的是将逻辑上的一个大表分成一些小的物理上的片。划分有很多益处：

• 在某些情况下查询性能能够显著提升，特别是当那些访问压力大的行在一个分区或者少数几个分区时。划分可以取代索引的主导列、减小索引尺寸以及使索引中访问压力大的部分更有可能被放在内存中。

• 当查询或更新访问一个分区的大部分行时，可以通过该分区上的一个顺序扫描来取代分散到整个表上的索引和随机访问，这样可以改善性能。

• 如果批量操作的需求是在分区设计时就规划好的，则批量装载和删除可以通过增加或者去除分区来完成。执行ALTER TABLE DETACH PARTITION或者使用DROP TABLE删除一个分区远快于批量操作。这些命令也完全避免了批量DELETE导致的VACUUM开销。

• 很少使用的数据可以被迁移到便宜且较慢的存储介质上。

当一个表非常大时，划分所带来的好处是非常值得的。一个表何种情况下会从划分获益取决于应用，一个经验法则是当表的尺寸超过了数据库服务器物理内存时，划分会为表带来好处。

瀚高数据库对下列分区形式提供了内建支持：

范围划分

表被根据一个关键列或一组列划分为”范围”，不同的分区的范围之间没有重叠。例如，我们可以根据日期范围划分，或者根据特定业务对象的标识符划分。

列表划分

通过显式地列出每一个分区中出现的键值来划分表。

哈希分区

通过为每个分区指定模数和余数来对表进行分区。每个分区所持有的行都满足：分区键的值除以为其指定的模数将产生为其指定的余数。

如果你的应用需要使用上面所列之外的分区形式，可以使用诸如继承和UNION ALL视图之类的替代方法。这些方法很灵活，但是却缺少内建声明式分区的一些性能优势。

### 声明式划分

瀚高数据库提供了一种方法指定如何把一个表划分成称为分区的片段。被划分的表被称作分区表。这种说明由分区方法以及要被用作分区键的列或者表达式列表组成。

所有被插入到分区表的行将被基于分区键的值路由到分区中。每个分区都有一个由其分区边界定义的数据子集。当前支持的分区方法是范围、列表以及哈希。

分区本身也可能被定义为分区表，这种用法被称为子分区。分区可以有自己的与其他分区不同的索引、约束以及默认值。创建分区表及分区的更多细节请见CREATE TABLE。

无法把一个常规表转换成分区表，反之亦然。不过，可以把一个包含数据的常规表或者分区表作为分区加入到另一个分区表，或者从分区表中移走一个分区并且把它变成一个独立的表。有关ATTACH PARTITION和DETACH PARTITION子命令的内容请见ALTER TABLE。

个体分区在内部以继承的方式链接到分区表，不过无法对声明式分区表或其分区使用继承的某些一般特性（下文讨论）。例如，分区不能有除其所属分区表之外的父表，一个常规表也不能从分区表继承使得后者成为其父表。这意味着分区表及其分区不会参与到与常规表的继承关系中。由于分区表及其分区组成的分区层次仍然是一种继承层次，所有第 4.10 节中所述的继承的普通规则也适用，不过有一些例外，尤其是：

• 分区表的CHECK约束和NOT NULL约束总是会被其所有的分区所继承。不允许在分区表上创建标记为NO INHERIT的CHECK约束。

• 只要分区表中不存在分区，则支持使用ONLY仅在分区表上增加或者删除约束。一旦分区存在，那样做就会导致错误，因为当分区存在时是不支持仅在分区表上增加或删除约束的。

不过，分区表本身上的约束可以被增加（如果它们不出现在父表中）和删除。

• 由于分区表并不直接拥有任何数据，尝试在分区表上使用TRUNCATE

ONLY将总是返回错误。

• 分区不能有在父表中不存在的列。在使用CREATE TABLE创建分区时不能指定列，在事后使用ALTER TABLE时也不能为分区增加列。只有当表的列正好匹配父表时，才能使用ALTER TABLE... ATTACH PARTITION将它作为分区加入。

• 如果NOT NULL约束在父表中存在，那么就不能删除分区的列上的对应的NOT NULL约束。

分区也可以是外部表，不过它们有一些普通表没有的限制，详情请见CREATE FOREIGN TABLE。

更新行的分区键可能导致它满足另一个不同的分区的分区边界，进而被移动到那个分区中。

#### 分区表分类

##### 范围分区

在范围分区中，分区规则根据KEY按照不同的范围映射到不同的分区中，每个分区的范围都是由一个上限值和下限值来决定，这两个值是在创建分区表时定义的。

范围分区的KEY可由多个列（最多可由32个列）组成。值得一提的是，当KEY由多个列组成时，除了第一列的各分区约束范围之间不能重叠外，其他列的分区范围可以有重叠。

范围分区适用于组成KEY是连续的，可以根据需要设定上下限的列。实际上，在分区表的应用中，范围分区是最普遍，最常用的分区类型。

> 范围分区的KEY可以支持多个字段组成(最多32个字段)。
> 
> **语法**

创建分区语法一：

主表语法:

CREATE TABLE 表名 ( \[{ 列名称 数据\_类型} \[,... \] \] )

PARTITION BY RANGE ( \[{ 列名称 } \[,...\] \] );

参数说明：

> RANGE关键字表示进行范围分区
> 
> RANGE后面跟的多个列是组成的KEY

分区语法:

CREATE TABLE 表名 PARTITION OF 主表 FOR VALUES

FROM{ ( 表达式 \[,...\] ) | MINVALUE } \[,...\]

TO { ( 表达式 \[,...\] ) | MAXVALUE } \[,...\]

\[ TABLESPACE 表空间名 \];

参数说明:

> FROM... TO 表示分区的起始值和结束值。
> 
> MINVALUE / MAXVALUE 表示无限小值和无限大值。
> 
> 默认FROM后面的值是包括值分区的约束内，TO后面的值不包括。
> 
> 创建分区语法二：

CREATE TABLE table\_name ( column\_name TYPE ) PARTITION BY RANGE ( column\_name )

(

PARTITION partition\_name\_1 FOR VALUES FROM (lower\_bound) TO (upper\_bound),

PARTITION partition\_name\_2 FOR VALUES FROM (lower\_bound) TO (upper\_bound),

PARTITION partition\_name\_3 DEFAULT

/\* more partition definitions follow...\*/

);

> 范围分区语法二将主表分区与分区语法进行融合，在主表分区语法后面增加()括号，括号后的内容为具体的分区划分，使用关键字PARTITION指定分区的名字， FOR VALUES FORM...TO 设置分区的范围.

范围分区语法一和范围分区语法二相比较，语法二更加简洁。

> 示例

1. 单列作为KEY值

> 范围分区语法一：

create table test(n int) partition by range(n);

create table test\_1 partition of test for values from (MINVALUE) to (10);

create table test\_2 partition of test for values from (10) to (100);

create table test\_3 partition of test for values from (100) to (1000);

create table test\_4 partition of test for values from (1000) to (10000);

> 范围分区语法二：

create table test(n int) partition by range(n)

(

PARTITION test\_1 for values from (MINVALUE) to (10),

PARTITION test\_2 for values from (10) to (100),

PARTITION test\_3 for values from (100) to (1000),

PARTITION test\_4 for values from (1000) to (10000),

PARTITION test\_default DEFAULT

);

可以\\d+ test显示主表及分区有关信息：

highgo=# \\d+ test |

Partition key: RANGE (n)

Partitions:

test\_1 FOR VALUES FROM (MINVALUE) TO (10),

test\_2 FOR VALUES FROM (10) TO (100),

test\_3 FOR VALUES FROM (100) TO (1000),

test\_4 FOR VALUES FROM (1000) TO (10000)

\\d+ test\_2可以显示分区test\_2的内在约束关系：

highgo=# \\d+ test\_2

Partition of: test FOR VALUES FROM (10) TO (100)

Partition constraint: ((n IS NOT NULL) AND (n >= 10) AND (n < 100))

2. 多列作为KEY值,下面以2列作为KEY值为例：

> 范围分区语法一:

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

highgo=# \\d+ test

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

##### 列表分区

列表分区的KEY只能包含一个。

在列表分区中，分区规则是由KEY的一系列离散值组成。也就是向列表分区插入数据时，只有等于这些离散值时才会执行插入。

很明显，当KEY值是非连续的，离散的时候，创建分区表比较适合列表分区。

**语法**

列表分区语法一:

创建主表语法：

CREATE TABLE 表名 ( \[{ 列名称 数据\_类型} \[,... \] \] )

PARTITION BY LIST( { 列名称 } );

参数说明：

> LIST关键字表示进行列表分区。
> 
> LIST关键字后只能有一个字段。

创建分区语法：

CREATE TABLE 表名 PARTITION OF 主表 FOR VALUES

IN ( 表达式 \[,...\] ) \[ TABLESPACE 表空间名 \];

参数说明：

> IN关键字表示列表分区约束的离散值。

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

CREATE TABLE sales\_east PARTITION OF sales FOR VALUES IN ('山东','江苏','上海');

CREATE TABLE sales\_west PARTITION OF sales FOR VALUES IN ('山西','陕西','四川');

CREATE TABLE sales\_north PARTITION OF sales FOR VALUES IN ('北京','河北','辽宁');

CREATE TABLE sales\_south PARTITION OF sales FOR VALUES IN ('广东','福建');

> 列表分区语法二:

CREATE TABLE sales (product\_id int, saleroom int, province text) PARTITION BY LIST(province)

(

PARTITION sales\_east FOR VALUES IN ('山东','江苏','上海'),

PARTITION sales\_west FOR VALUES IN ('山西','陕西','四川'),

PARTITION sales\_north FOR VALUES IN ('北京','河北','辽宁'),

PARTITION sales\_south FOR VALUES IN ('广东','福建'),

PARTITION sales\_default DEFAULT

);

\\d+ sales；显示主表及分区信息：

highgo=# \\d+ sales

Partition key: LIST (province)

Partitions: sales\_east FOR VALUES IN ('山东', '江苏', '上海'),

sales\_north FOR VALUES IN ('北京', '河北', '辽宁'),

sales\_south FOR VALUES IN ('广东', '福建'),

sales\_west FOR VALUES IN ('山西', '陕西', '四川')

\\d+ sales\_east;显示分区约束信息：

highgo=# \\d+ sales\_east

Partition of: sales FOR VALUES IN ('山东', '江苏', '上海')

Partition constraint: ((province IS NOT NULL) AND

(province = ANY (ARRAY\['山东'::text, '江苏'::text, '上海'::text\])))

##### 哈希分区

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

Hash分区语法一:

create table test\_hash(id int, date date) partition by hash(id);

create table test\_hash\_1 partition of test\_hash for values with(modulus 2, remainder 0);

create table test\_hash\_2 partition of test\_hash for values with(modulus 2, remainder 1);

Hash分区语法二:

create table test\_hash(id int, date date) partition by hash(id)

(

PARTITION test\_hash\_1 FOR VALUES WITH (modulus 2, remainder 0 ),

PARTITION test\_hash\_2 FOR VALUES WITH (modulus 2, remainder 1 )

);

\\d+ test\_hash 显示主表及分区信息

Table "public.test\_hash"

Column | Type | Collation | Nullable | Default | Storage | Stats target | Description

\--------+---------+-----------+----------+---------+---------+--------------+-------------

id | integer | | | | plain | |

date | date | | | | plain | |

Partition key: HASH (id)

Partitions: test\_hash\_1 FOR VALUES WITH (modulus 2, remainder 0),

test\_hash\_2 FOR VALUES WITH (modulus 2, remainder 1)

\\d+ test\_hash\_1

Table "public.test\_hash\_1"

Column | Type | Collation | Nullable | Default | Storage | Stats target | Description

\--------+---------+-----------+----------+---------+---------+--------------+-------------

id | integer | | | | plain | |

date | date | | | | plain | |

Partition of: test\_hash FOR VALUES WITH (modulus 2, remainder 0)

Partition constraint: satisfies\_hash\_partition('16603'::oid, 2, 0, id)

insert into test\_hash select generate\_series(1, 10), current\_date;

select tableoid::regclass, \* from test\_hash;

tableoid | id | date

\-------------+----+------------

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

#### 例子

假定我们正在为一个大型的冰激凌公司构建数据库。该公司每天测量最高温度以及每个区域的冰激凌销售情况。概念上，我们想要一个这样的表：

CREATE TABLE measurement (

city\_id int not null,

logdate date not null,

peaktemp int,

unitsales int

);

我们知道大部分查询只会访问上周的、上月的或者上季度的数据，因为这个表的主要用途是为管理层准备在线报告。为了减少需要被存放的旧数据量，我们决定只保留最近3年的数据。在每个月的开始我们将去除掉最早的那个月的数据。在这种情况下我们可以使用分区技术来帮助我们满足对measurement表的所有不同需求。

要在这种情况下使用声明式分区，可采用下面的步骤：

1\. 通过指定PARTITION BY子句把measurement表创建为分区表，该子句包括分区方法（这个例子中是RANGE）以及用作分区键的列列表。

CREATE TABLE measurement (

city\_id int not null,

logdate date not null,

peaktemp int,

unitsales int

) PARTITION BY RANGE (logdate);

你可能需要决定在分区键中使用多列进行范围分区。当然，这通常会导致较大数量的分区，其中每一个个体都比较小。另一方面，使用较少的列可能会导致粗粒度的分区策略得到较少数量的分区。如果条件涉及这些列中的一部分或者全部，访问分区表的查询将不得不扫描较少的分区。例如，考虑一个使用列lastname和firstname（按照这样的顺序）作为分区键进行范围分区的表。

2\. 创建分区。每个分区的定义必须指定对应于父表的分区方法和分区键的边界。注意，如果指定的边界使得新分区的值会与已有分区中的值重叠，则会导致错误。向父表中插入无法映射到任何现有分区的数据将会导致错误，这种情况下应该手工增加一个合适的分区。

分区以普通瀚高数据库表（或者可能是外部表）的方式创建。可以为每个分区单独指定表空间和存储参数。

没有必要创建表约束来描述分区的分区边界条件。相反，只要需要引用分区约束时，分区约束会自动地隐式地从分区边界说明中生成。

CREATE TABLE measurement\_y2006m02 PARTITION OF measurement

FOR VALUES FROM ('2006-02-01') TO ('2006-03-01');

CREATE TABLE measurement\_y2006m03 PARTITION OF measurement

FOR VALUES FROM ('2006-03-01') TO ('2006-04-01');

...

CREATE TABLE measurement\_y2006m11 PARTITION OF measurement

FOR VALUES FROM ('2006-11-01') TO ('2006-12-01');

CREATE TABLE measurement\_y2006m12 PARTITION OF measurement

FOR VALUES FROM ('2006-12-01') TO ('2008-01-01')

TABLESPACE fasttablespace;

CREATE TABLE measurement\_y2008m01 PARTITION OF measurement

FOR VALUES FROM ('2008-01-01') TO ('2008-02-01')

WITH (parallel\_workers = 4)

TABLESPACE fasttablespace;

为了实现子分区，在创建分区的命令中指定PARTITION BY子句，例如：

CREATE TABLE measurement\_y2006m02 PARTITION OF measurement

FOR VALUES FROM ('2006-02-01') TO ('2006-03-01')

PARTITION BY RANGE (peaktemp);

在创建了measurement\_y2006m02的分区之后，任何被插入到measurement中且被映射到measurement\_y2006m02的数据（或者直接被插入到measurement\_y2006m02的数据，假定它满足这个分区的分区约束）将被基于peaktemp列进一步重定向到measurement\_y2006m02的一个分区。指定的分区键可以与父亲的分区键重叠，不过在指定子分区的边界时要注意它接受的数据集合是分区自身边界允许的数据集合的一个子集，系统不会尝试检查事情情况是否如此。

3\. 在分区表的键列上创建一个索引，还有其他需要的索引（键索引并不是必需的，但是大部分场景中它都能很有帮助）。这会自动在每个分区上创建一个索引，并且后来创建或者附着的任何分区也将会包含索引。

CREATE INDEX ON measurement (logdate);

4\. 确保enable\_partition\_pruning配置参数在Highgo.conf中没有被禁用。如果被禁用，查询将不会按照想要的方式被优化。

在上面的例子中，我们会每个月创建一个新分区，因此写一个脚本来自动生成所需的DDL会更好。

#### 分区维护

通常在初始定义分区表时建立的分区并非保持静态不变。移除旧分区的数据并且为新数据周期性地增加新分区的需求比比皆是。分区的最大好处之一就是可以通过操纵分区结构来近乎瞬时地执行这类让人头痛的任务，而不是物理地去除大量数据。

移除旧数据最简单的选择是删除掉不再需要的分区：

DROP TABLE measurement\_y2006m02;

这可以非常快地删除数百万行记录，因为它不需要逐个删除每个记录。不过要注意上面的命令需要在父表上拿到ACCESS EXCLUSIVE锁。

另一种通常更好的选项是把分区从分区表中移除，但是保留它作为一个独立的表：

ALTER TABLE measurement DETACH PARTITION measurement\_y2006m02;

这允许在它被删除之前在其数据上执行进一步的操作。例如，这通常是一种使用COPY、pg\_dump或类似工具备份数据的好时候。这也是把数据聚集成较小的格式、执行其他数据操作或者运行报表的好时机。

类似地，我们可以增加一个新分区来处理新数据。我们可以在分区表中创建一个空分区，就像上面创建的初始分区那样：

CREATE TABLE measurement\_y2008m02 PARTITION OF measurement

FOR VALUES FROM ('2008-02-01') TO ('2008-03-01')

TABLESPACE fasttablespace;

另外一种选择是，有时候在分区结构之外创建新表更加方便，然后将它作为一个合适的分区。这允许先对数据进行装载、检查和转换，然后再让它们出现在分区表中：

CREATE TABLE measurement\_y2008m02

(LIKE measurement INCLUDING DEFAULTS INCLUDING CONSTRAINTS)

TABLESPACE fasttablespace;

ALTER TABLE measurement\_y2008m02 ADD CONSTRAINT y2008m02

CHECK ( logdate >= DATE '2008-02-01' AND logdate < DATE '2008-03-01' );

\\copy measurement\_y2008m02 from 'measurement\_y2008m02'

\-# possibly some other data preparation work

ALTER TABLE measurement ATTACH PARTITION measurement\_y2008m02

FOR VALUES FROM ('2008-02-01') TO ('2008-03-01' );

在运行ATTACH PARTITION命令之前，推荐在要被挂接的表上创建一个CHECK约束来匹配期望的分区约束。 这样，系统将能够跳过扫描来验证隐式分区约束。 没有CHECK约束，将扫描表以验证分区约束，同时对该分区持有ACCESS EXCLUSIVE锁定，并在父表上持有SHARE UPDATE EXCLUSIVE锁。 在完成ATTACH PARTITION后，可能需要删除冗余CHECK约束。

如上所述，可以在分区的表上创建索引，并自动将其应用于整个层次结构。 这非常便利，因为不仅现有分区将变为索引，而且将来创建的任何分区都将变为索引。 一个限制是，在创建这样一个分区索引时，不可能同时使用CONCURRENTLY限定符。 为了克服长时间锁，可以对分区表使用CREATE INDEX ON ONLY;这样的索引被标记为无效，并且分区不会自动应用该索引。 分区上的索引可以使用CONCURRENTLY分别的创建。 然后使用ALTER INDEX.. ATTACH PARTITIONattached到父索引。 一旦所有分区的索引附加到父索引，父索引将自动标记为有效。 例如：

CREATE INDEX measurement\_usls\_idx ON ONLY measurement (unitsales);

CREATE INDEX measurement\_usls\_200602\_idx

ON measurement\_y2006m02 (unitsales);

ALTER INDEX measurement\_usls\_idx

ATTACH PARTITION measurement\_usls\_200602\_idx;

...

该技术也可以与UNIQUE 和PRIMARY KEY 约束一起试用; 当创建约束时隐式创建索引。例如:

ALTER TABLE ONLY measurement ADD UNIQUE (city\_id, logdate);

ALTER TABLE measurement\_y2006m02 ADD UNIQUE (city\_id, logdate);

ALTER INDEX measurement\_city\_id\_logdate\_key

ATTACH PARTITION measurement\_y2006m02\_city\_id\_logdate\_key;

...

#### 限制

分区表有下列限制：

• 没有办法创建跨越所有分区的排除约束，只可能单个约束每个叶子分区。

• 分区表上的惟一约束必须包括所有分区键列。存在此限制是因为瀚高数据库只能每个分区中分别强制实施唯一性。

• 如果必要，必须在个体分区上定义BEFORE ROW触发器，分区表上不需要。

• 不允许在同一个分区树中混杂临时关系和持久关系。因此，如果分区表是持久的，则其分区也必须是持久的，反之亦然。在使用临时关系时，分区数的所有成员都必须来自于同一个会话。

### 使用继承实现

虽然内建的声明式分区适合于大部分常见的用例，但还是有一些场景需要更加灵活的方法。

分区可以使用表继承来实现，这能够带来一些声明式分区不支持的特性，例如：

• 对声明式分区来说，分区必须具有和分区表正好相同的列集合，而在表继承中，子表可以有父表中没有出现过的额外列。

• 表继承允许多继承。

• 声明式分区仅支持范围、列表以及哈希分区，而表继承允许数据按照用户的选择来划分（不过注意，如果约束排除不能有效地剪枝子表，查询性能可能会很差）。

• 在使用声明式分区时，一些操作比使用表继承时要求更长的持锁时间。例如，向分区表中增加分区或者从分区表移除分区要求在父表上取得一个ACCESS EXCLUSIVE锁，而在常规继承的情况下一个SHARE UPDATE EXCLUSIVE锁就足够了。

#### 例子

我们使用上面用过的同一个measurement表。为了使用继承实现分区，可使用下面的步骤：

1\. 创建”主”表，所有的”子”表都将从它继承。这个表将不包含数据。不要在这个表上定义任何检查约束，除非想让它们应用到所有的子表上。同样，在这个表上定义索引或者唯一约束也没有意义。对于我们的例子来说，主表是最初定义的measurement表。

2\. 创建数个”子”表，每一个都从主表继承。通常，这些表将不会在从主表继承的列集合之外增加任何列。正如声明性分区那样，这些表就是普通的瀚高数据库表（或者外部表）。

CREATE TABLE measurement\_y2006m02 () INHERITS (measurement);

CREATE TABLE measurement\_y2006m03 () INHERITS (measurement);

...

CREATE TABLE measurement\_y2006m11 () INHERITS (measurement);

CREATE TABLE measurement\_y2006m12 () INHERITS (measurement);

CREATE TABLE measurement\_y2008m01 () INHERITS (measurement);

3\. 为子表增加不重叠的表约束来定义每个分区允许的键值。

典型的例子是：

CHECK ( x = 1 )

CHECK ( county IN ( 'Oxfordshire', 'Buckinghamshire', 'Warwickshire' ))

CHECK ( outletID >= 100 AND outletID < 200 )

确保约束能保证不同子表允许的键值之间没有重叠。设置范围约束的常见错误：

CHECK ( outletID BETWEEN 100 AND 200 )

CHECK ( outletID BETWEEN 200 AND 300 )

这是错误的，因为不清楚键值200属于哪一个子表。

像下面这样创建子表会更好：

CREATE TABLE measurement\_y2006m02 (

CHECK ( logdate >= DATE '2006-02-01' AND logdate < DATE '2006-03-01' )

) INHERITS (measurement);

CREATE TABLE measurement\_y2006m03 (

CHECK ( logdate >= DATE '2006-03-01' AND logdate < DATE '2006-04-01' )

) INHERITS (measurement);

...

CREATE TABLE measurement\_y2006m11 (

CHECK ( logdate >= DATE '2006-11-01' AND logdate < DATE '2006-12-01' )

) INHERITS (measurement);

CREATE TABLE measurement\_y2006m12 (

CHECK ( logdate >= DATE '2006-12-01' AND logdate < DATE '2008-01-01' )

) INHERITS (measurement);

CREATE TABLE measurement\_y2008m01 (

CHECK ( logdate >= DATE '2008-01-01' AND logdate < DATE '2008-02-01' )

) INHERITS (measurement);

4\. 对于每个子表，在键列上创建一个索引，以及任何想要的其他索引。

CREATE INDEX measurement\_y2006m02\_logdate ON measurement\_y2006m02 (logdate);

CREATE INDEX measurement\_y2006m03\_logdate ON measurement\_y2006m03 (logdate);

CREATE INDEX measurement\_y2006m11\_logdate ON measurement\_y2006m11 (logdate);

CREATE INDEX measurement\_y2006m12\_logdate ON measurement\_y2006m12 (logdate);

CREATE INDEX measurement\_y2008m01\_logdate ON measurement\_y2008m01 (logdate);

5\. 我们希望我们的应用能够使用INSERT INTO measurement...并且数据将被重定向到合适的分区表。我们可以通过为主表附加一个合适的触发器函数来实现这一点。如果数据将只被增加到最后一个分区，我们可以使用一个非常简单的触发器函数：

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

我们也可能希望插入数据时服务器会自动地定位应该加入数据的子表。我们可以通过一个更复杂的触发器函数来实现之，例如：

CREATE OR REPLACE FUNCTION measurement\_insert\_trigger()

RETURNS TRIGGER AS $$

BEGIN

IF ( NEW.logdate >= DATE '2006-02-01' AND

NEW.logdate < DATE '2006-03-01' ) THEN

INSERT INTO measurement\_y2006m02 VALUES (NEW.\*);

ELSIF ( NEW.logdate >= DATE '2006-03-01' AND

NEW.logdate < DATE '2006-04-01' ) THEN

INSERT INTO measurement\_y2006m03 VALUES (NEW.\*);

...

ELSIF ( NEW.logdate >= DATE '2008-01-01' AND

NEW.logdate < DATE '2008-02-01' ) THEN

INSERT INTO measurement\_y2008m01 VALUES (NEW.\*);

ELSE

RAISE EXCEPTION 'Date out of range. Fix the

measurement\_insert\_trigger() function!';

END IF;

RETURN NULL;

END;

$$

LANGUAGE plpgsql;

触发器的定义和以前一样。注意每一个IF测试必须准确地匹配它的子表的CHECK约束。

当该函数比单月形式更加复杂时，并不需要频繁地更新它，因为可以在需要的时候提前加。

| 注意： |
| --- |
| 在实践中，如果大部分插入都会进入最新的子表，最好先检查它。为了简洁，我们为触发器的检查采用了和本例中其他部分一致的顺序。 |

把插入重定向到一个合适的子表中的另一种不同方法是在主表上设置规则而不是触发器。

例如：

CREATE RULE measurement\_insert\_y2006m02 AS

ON INSERT TO measurement WHERE

( logdate >= DATE '2006-02-01' AND logdate < DATE '2006-03-01' )

DO INSTEAD

INSERT INTO measurement\_y2006m02 VALUES (NEW.\*);

...

CREATE RULE measurement\_insert\_y2008m01 AS

ON INSERT TO measurement WHERE

( logdate >= DATE '2008-01-01' AND logdate < DATE '2008-02-01' )

DO INSTEAD

INSERT INTO measurement\_y2008m01 VALUES (NEW.\*);

规则的开销比触发器大很多，但是这种开销是每个查询只有一次，而不是每行一次，因此这种方法可能对批量插入的情况有优势。不过，在大部分情况下，触发器方法将提供更好的性能。

注意COPY会忽略规则。如果想要使用COPY插入数据，则需要拷贝到正确的子表而不是直接放在主表中。COPY会引发触发器，因此在使用触发器方法时可以正常使用它。

规则方法的另一个缺点是，如果规则集合无法覆盖插入日期，则没有简单的方法能够强制产生错误，数据将会无声无息地进入到主表中。

6\. 确认constraint\_exclusion配置参数在Highgo.conf中没有被禁用，否则将会不必要地访问子表。

如我们所见，一个复杂的表层次可能需要大量的DDL。在上面的例子中，我们可能为每个月创建一个新的子表，因此编写一个脚本来自动生成所需要的DDL可能会更好。

#### 继承分区的维护

要快速移除旧数据，只需要简单地去掉不再需要的子表：

DROP TABLE measurement\_y2006m02;

要从继承层次表中去掉子表，但还是把它当做一个表保留：

ALTER TABLE measurement\_y2006m02 NO INHERIT measurement;

要增加一个新子表来处理新数据，可以像上面创建的原始子表那样创建一个空的子表：

CREATE TABLE measurement\_y2008m02 (

CHECK ( logdate >= DATE '2008-02-01' AND logdate < DATE '2008-03-01' )

) INHERITS (measurement);

或者，用户可能想要创建新子表并且在将它加入到表层次之前填充它。这可以允许数据在被父表上的查询可见之前对数据进行装载、检查以及转换。

CREATE TABLE measurement\_y2008m02

(LIKE measurement INCLUDING DEFAULTS INCLUDING CONSTRAINTS);

ALTER TABLE measurement\_y2008m02 ADD CONSTRAINT y2008m02

CHECK ( logdate >= DATE '2008-02-01' AND logdate < DATE '2008-03-01' );

\\copy measurement\_y2008m02 from 'measurement\_y2008m02'

\-# possibly some other data preparation work

ALTER TABLE measurement\_y2008m02 INHERIT measurement;

#### 提醒

下面的提醒适用于用继承实现的分区：

• 没有自动的方法啊验证所有的CHECK约束之间是否互斥。编写代码来产生子表以及创建和修改相关对象比手写命令要更加安全。

• 索引和外键约束适用于单个表而不是其继承子级，因此它们有一些caveats 需要注意。

• 这里展示的模式假定行的键列值从不改变，或者说改变不足以让行移动到另一个分区。由于CHECK约束的存在，尝试那样做的UPDATE将会失败。如果需要处理那种情况，可以在子表上放置适当的更新触发器，但是那会使对结构的管理更加复杂。

• 如果使用手工的VACUUM或者ANALYZE命令，不要忘记需要在每个子表上单独运行它们。这样的命令：

ANALYZE measurement;

将只会处理主表。

• 带有ON CONFLICT子句的INSERT语句不太可能按照预期工作，因为只有在指定的目标关系而不是其子关系上发生唯一违背时才会采取ON CONFLICT行动。

• 将会需要触发器或者规则将行路由到想要的子表中，除非应用明确地知道分区的模式。编写触发器可能会很复杂，并且会比声明式分区在内部执行的元组路由慢很多。

### 分区剪枝

分区剪枝是一种提升声明式分区表性能的查询优化技术。例如：

SET enable\_partition\_pruning = on; -# the default

SELECT count(\*) FROM measurement WHERE logdate >= DATE '2008-01-01';

如果没有分区剪枝，上面的查询将会扫描measurement表的每一个分区。如果启用了分区剪枝，规划器将会检查每个分区的定义并且检验该分区是否因为不包含符合查询WHERE子句的行而无需扫描。当规划器可以证实这一点时，它会把分区从查询计划中排除（剪枝）。

通过使用EXPLAIN命令和enable\_partition\_pruning配置参数，可以展示剪枝掉分区的计划与没有剪枝的计划之间的差别。对这种类型的表设置，一种典型的未优化计划是：

SET enable\_partition\_pruning = off;

EXPLAIN SELECT count(\*) FROM measurement WHERE logdate >= DATE '2008-01-01';

QUERY PLAN

\-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

#-#-

Aggregate (cost=188.66..188.66 rows=1 width=8)

\-> Append (cost=0.00..181.05 rows=3085 width=0)

\-> Seq Scan on measurement\_y2006m02 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= '2008-01-01'::date)

\-> Seq Scan on measurement\_y2006m03 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= '2008-01-01'::date)

...

\-> Seq Scan on measurement\_y2006m11 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= '2008-01-01'::date)

\-> Seq Scan on measurement\_y2006m12 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= '2008-01-01'::date)

\-> Seq Scan on measurement\_y2008m01 (cost=0.00..33.12 rows=616

width=0)

Filter: (logdate >= '2008-01-01'::date)

某些或者全部的分区可能会使用索引扫描取代全表顺序扫描，但是这里的重点是根本不需要扫描较老的分区来回答这个查询。当我们启用分区剪枝时，我们会得到一个便宜很多的计划，而它能给出相同的答案：

SET enable\_partition\_pruning = on;

EXPLAIN SELECT count(\*) FROM measurement WHERE logdate >= DATE '2008-01-01';

QUERY PLAN

\-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

#-#-

Aggregate (cost=36.65..36.66 rows=1 width=8)

\-> Seq Scan on measurement\_y2008m01 (cost=0.00..33.12 rows=616 width=0)

Filter: (logdate >= '2008-01-01'::date)

注意，分区剪枝仅由分区键隐式定义的约束所驱动，而不是由索引的存在驱动。因此，没有必要在键列上定义索引。是否需要为一个给定分区创建索引取决于预期的查询扫描该分区时会扫描大部分还是小部分。后一种情况下索引的帮助会比前者大。

不仅在给定查询的规划期间可以执行分区剪枝，在其执行期间也能执行分区剪枝。 这非常有用，因为如果子句中包含查询规划时值未知的表达式时，这可以剪枝掉更多的分区； 例如在PREPARE语句中定义的参数会使用从子查询拿到的值，或者嵌套循环连接内侧关系上的参数化值。 执行期间的分区剪枝可能在下列任何时刻执行：

• 在查询计划的初始化期间。对于执行的初始化阶段就已知值的参数，可以在这里执行分区剪枝。这个阶段中被剪枝掉的分区将不会显示在查询的EXPLAIN或EXPLAIN ANALYZE结果中。通过观察EXPLAIN输出的”Subplans Removed”属性，可以确定被剪枝掉的分区数。

• 在查询计划的实际执行期间。这里可以使用只有在实际查询执行时才能知道的值执行分区剪枝。这包括来自子查询的值以及来自执行时参数的值（例如来自于参数化嵌套循环连接的参数）。由于在查询执行期间这些参数的值可能会改变多次，所以只要分区剪枝使用到的执行参数发生改变，就会执行一次分区剪枝。要判断分区是否在这个阶段被剪枝，需要仔细地观察EXPLAIN ANALYZE输出中的loops属性。 对应于不同分区的子计划可以具有不同的值，这取决于在执行期间每个分区被修剪的次数。 如果每次都被剪枝，有些分区可能会显示为(never executed)。

| 注意： |
| --- |
| 执行时间分区裁剪当前只针对Append和MergeAppend节点类型。它还没有为ModifyTable节点类型实现，但有可能会在将来发布的 Highgo中更改。 |

### 分区和约束排除

约束排除是一种与分区剪枝类似的查询优化技术。虽然它主要被用于使用传统继承方法实现的分区上，但它也可以被用于其他目的，包括用于声明式分区。

约束排除以非常类似于分区剪枝的方式工作，不过它使用每个表的CHECK约束 — 这也是它得名的原因 — 而分区剪枝使用表的分区边界，分区边界仅存在于声明式分区的情况中。另一点不同之处是约束排除仅在规划时应用，在执行时不会尝试移除分区。

由于约束排除使用CHECK约束，这导致它比分区剪枝要慢，但有时候可以被当作一种优点加以利用：因为甚至可以在声明式分区的表上（在分区边界之外）定义约束，约束排除可能可以从查询计划中消去额外的分区。

constraint\_exclusion的默认（也是推荐的）设置不是on也不是off，而是一种被称为partition的中间设置，这会导致该技术仅被应用于可能工作在继承分区表上的查询。on设置导致规划器检查所有查询中的CHECK约束，甚至是那些不太可能受益的简单查询。

下列提醒适用于约束排除：

• 约束排除仅适用于查询规划期间，和分区裁剪不同，在查询执行期间也可以应用。

• 只有查询的WHERE子句包含常量（或者外部提供的参数）时，约束排除才能有效果。例如，针对一个非不变函数（如CURRENT\_TIMESTAMP）的比较不能被优化，因为规划器不知道该函数的值在运行时会落到哪个子表中。

• 保持分区约束简单化，否则规划器可能无法验证哪些子表可能不需要被访问。如前面的例子所示，对列表分区使用简单的等值条件，对范围分区使用简单的范围测试。一种好的经验规则是分区约束应该仅包含分区列与常量使用B-树的可索引操作符的比较，因为只有B-树的可索引列才允许出现在分区键中。

• 约束排除期间会检查父表的所有子表上的所有约束，因此大量的子表很可能明显地增加查询规划时间。因此，传统的基于继承的分区可以很好地处理上百个子表，不要尝试使用上千个子表。

### 声明分区最佳实践

应该谨慎地选择如何划分表，因为查询规划和执行的性能可能会受到不良设计的负面影响。

最重要的设计决策之一是列或者如和对数据进行分区的。 通常最佳选择是按列或列集合进行分区，这些列最常出现在分区表上执行的查询的 WHERE子句中。 WHERE子句项与分区键匹配并兼容，可用于裁剪不需要的分区。 但是，你可能会被迫根据PRIMARY KEY或UNIQUE约束的要求做出其他决策。 在规划分区策略时，删除不需要的数据也是需要考虑的一个因素。 可以相当快地分离整个分区，因此采用这样方式设计分区策略可能是有益的，既把一次删除的所有数据都放在单个分区中。

选择表应该划分的分区的目标数量也是一个重要的决策。 没有足够的分区可能意味着索引仍然太大，数据位置仍然较差，这可能导致缓存命中率很低。 但是，将表划分为太多的分区也会导致问题。 在查询规划和执行期间，过多的分区可能意味着查询计划时间较长，内存消耗也更高。 在选择如何划分表时，考虑将来可能发生的更改也很重要。 例如，如果您选择为每个客户提供一个分区，而您目前只有少量的大客户，那么，如果几年后您发现自己有大量的小客户，那么就要考虑这种影响。 在这种情况下，最好选择按HASH分区并且选择合理数量的分区，而不是尝试按 LIST 进行分区，并希望客户数量的增长不会超出按数据分区的实际范围。

子分区可用于进一步划分预期会比其他分区更大的分区，尽管过多的子分区很容易导致大量分区，并可能导致前一段中提到的相同问题。

考虑查询计划和执行期间的分区开销也很重要。 查询规划器通常能够很好地处理多达几千个分区的分区层次结构，前提是典型的查询允许查询规划器裁剪除了少量分区之外的所有分区。 规划器执行分区修剪后保留更多分区时，规划时间会变长，内存消耗会更高。对于UPDATE 和 DELETE命令尤其如此。 担心拥有大量分区的另一个原因是，服务器的内存消耗可能会在一段时间内显著增加，特别是如果许多会话接触大量分区。 这是因为每个分区都需要将其元数据加载到接触它的每个会话的本地内存中。

对于数据仓库类型工作负载，使用比 OLTP 类型工作负载更多的分区数量很有意义。 通常，在数据仓库中，查询计划时间不太值得关注，因为大多数处理时间都花在查询执行期间。 对于这两种类型的工作负载，尽早做出正确的决策非常重要，因为重新分区大量数据可能会非常缓慢。 模拟预期工作负载通常有利于优化分区策略。永远不要假设更多的分区比更少的分区更好，反之亦然。

## 外部数据

瀚高数据库实现了部分的SQL/MED规定，允许我们使用普通SQL查询来访问位于瀚高数据库之外的数据。这种数据被称为外部数据（注意这种用法不要和外键混淆，后者是数据库中的一种约束）。

外部数据可以在一个外部数据包装器的帮助下被访问。一个外部数据包装器是一个库，它可以与一个外部数据源通讯，并隐藏连接到数据源和从它获取数据的细节。

要访问外部数据，我们需要建立一个外部服务器对象，它根据它所支持的外部数据包装器所使用的一组选项定义了如何连接到一个特定的外部数据源。接着我们需要创建一个或多个外部表，它们定义了外部数据的结构。一个外部表可以在查询中像一个普通表一样地使用，但是在瀚高数据库服务器中外部表没有存储数据。不管使用什么外部数据包装器，瀚高数据库会要求外部数据包装器从外部数据源获取数据，或者在更新命令的情况下传送数据到外部数据源。

访问远程数据可能需要在外部数据源的授权。这些信息通过一个用户映射提供，它基于当前的瀚高数据库角色提供了附加的数据例如用户名和密码。

更多信息请见 CREATE FOREIGN DATA WRAPPER、 CREATE SERVER、 CREATE USER MAPPING、CREATE FOREIGN TABLE、以及 IMPORT FOREIGN SCHEMA。

## 其他数据库对象

表是一个关系型数据库结构中的核心对象，因为它们承载了我们的数据。但是它们并不是数据库中的唯一一种对象。有很多其他种类的对象可以被创建来使得数据的使用和刮泥更加方便或高效。在本章中不会讨论它们，但是我们在会给出一个列表：

• 视图

• 函数、过程和操作符

• 数据类型和域

• 触发器和重写规则。

## 依赖跟踪

当我们创建一个涉及到很多具有外键约束、视图、触发器、函数等的表的复杂数据库结构时，我们隐式地创建了一张对象之间的依赖关系网。例如，具有一个外键约束的表依赖于它所引用的表。

为了保证整个数据库结构的完整性，瀚高数据库确保我们无法删除仍然被其他对象依赖的对象。例如，尝试删除第 4.4.5 节中的产品表会导致一个如下的错误消息，因为有订单表依赖于产品表：

DROP TABLE products;

ERROR: cannot drop table products because other objects depend on it

DETAIL: constraint orders\_product\_no\_fkey on table orders depends on table

products

HINT: Use DROP... CASCADE to drop the dependent objects too.

该错误消息包含了一个有用的提示：如果我们不想一个一个去删除所有的依赖对象，我们可以执行：

DROP TABLE products CASCADE;

这样所有的依赖对象将被移除，同样依赖于它们的任何对象也会被递归删除。在这种情况下，订单表不会被移除，但是它的外键约束会被移除。之所以在这里会停下，是因为没有什么依赖着外键约束（如果希望检查DROP... CASCADE会干什么，运行不带CASCADE的DROP并阅读DETAIL输出）。

瀚高数据库中的几乎所有DROP命令都支持CASCADE。当然，其本质的区别随着对象的类型而不同。我们也可以用RESTRICT代替CASCADE来获得默认行为，它将阻止删除任何被其他对象。

| 注意： |
| --- |
| 根据SQL标准，在DROP命令中指定RESTRICT或CASCADE是被要求的。但没有哪个数据库系统真正强制了这个规则，但是不同的系统中两种默认行为都是可能的。 |

如果一个DROP命令列出了多个对象，只有在存在指定对象构成的组之外的依赖关系时才需要CASCADE。例如，如果发出命令DROP TABLE tab1, tab2且存在从tab2到tab1的外键引用，那么就不需要CASCADE即可成功执行。

对于用户定义的函数，瀚高数据库会追踪与函数外部可见性质相关的依赖性，例如它的参数和结果类型，但不追踪检查函数体才能知道的依赖性。例如，考虑这种情况：

CREATE TYPE rainbow AS ENUM ('red', 'orange', 'yellow',

'green', 'blue', 'purple');

CREATE TABLE my\_colors (color rainbow, note text);

CREATE FUNCTION get\_color\_note (rainbow) RETURNS text AS

'SELECT note FROM my\_colors WHERE color = $1'

LANGUAGE SQL;

瀚高数据库将会注意到get\_color\_note函数依赖于rainbow类型：删掉该类型会强制删除该函数，因为该函数的参数类型就无法定义了。但是瀚高数据库不会认为get\_color\_note依赖于my\_colors表，因此即使该表被删除也不会删除这个函数。虽然这种方法有缺点，但是也有好处。如果该表丢失，这个函数在某种程度上仍然是有效的，但是执行它会导致错误。创建一个同名的新表将允许该函数重新有效。

## 数据分片

### 概述

分片是在分布式数据库环境中将表划分为多个数据库服务器实例的行为，而分区是指在同一数据库服务器上划分表。分片也称为水平分区，它在一个或多个外部数据库服务器中保存数据以分散负载。在外部服务器上创建的表通常称为”分片”，并且通常通过本地数据库服务器上的外部数据包装器（FDW）处理程序（例如，postgres\_fdw扩展）进行访问。

在瀚高数据库系统中，WITH PUSHDOWN子句可用于创建外部分区表。该子句提供了在外部服务器上自动创建外部分区表的功能，而无需用户手动进行操作。

除了新的WITH PUSHDOWN子句外，数据分片还可能应用到另一个可选子句INCLUDE REMOTE，该子句可与现有的DROP FOREIGN TABLE子句一起使用，以自动删除外部服务器中的表，而无需用户手动删除它。此功能内置在postgres\_fdw扩展中，并且可以扩展到其他FDW。

### WITH PUSHDOWN子句语法

WITH PUSHDOWN是一个可选子句，可以将其添加到现有CREATE FOREIGN TABLE SQL语句的末尾，以在外部服务器上触发自动表创建。 此子句可以与外部表和分区的创建一起使用，并且不能与ALTER，UPDATE，DROP或INSERT子句。 以下各节概述了WITH PUSHDOWN的不同用例。

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

/\* more partition definitions follow...\*/

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

/\* more sub partition definitions follow...\*/

)

/\* more partition definitions follow...\*/

);

### INCLUDE REMOTE子句语法

INCLUDE REMOTE是一个可选子句，可以将其添加到现有DROP TABLE或DROP FOREIGN TABLE SQL语句的末尾，以触发外部服务器上的自动表删除。 此子句可用于删除本地表和外部表，并且不能与ALTER，UPDATE，CREATE或INSERT子句一起使用。 以下各节概述了INCLUDE REMOTE的不同用例。

- 删除外部表

在DROP FOREIGN TABLE的末尾使用INCLUDE REMOTE时，请考虑以下一般规则：

DROP FOREIGN TABLE IF EXISTS table\_name INCLUDE REMOTE;

这个通用命令将删除名为本地和外部服务器中的table\_name。

- 删除外部分区表

要自动删除本地和外部分区表，用户可以遵循以下一般规则：

DROP TABLE table\_name INCLUDE REMOTE;

这将删除名为table\_name的本地表，以及在本地和外部服务器上创建的所有分区表。 外部分区表和外部服务器名称的列表，在执行查询时将打印为NOTICE。

如果用户创建包含外部子分区的表，则可以使用相同的规则删除该表以及在外部服务器上创建的所有子分区。

- 使用CASCADE删除外部分区表

如果用户尝试删除与其他表（例如视图）具有依赖性的外部或本地表，则将返回错误。 要解决此错误，用户可以先手动删除从属表，或者仅在查询语句中包括CASCADE子句以自动删除表及其从属关系。 根据下面的一般规则，CASCADE子句也可以与INCLUDE REMOTE子句一起使用：

DROP TABLE table\_name CASCADE INCLUDE REMOTE;

这将删除与table\_name相关的本地和外部服务器上的所有依赖表，然后删除本地和外部服务器上的table\_name及其关联的分区或子分区。

### 本地数据库服务器上创建外部服务器对象

在使用新的WITH PUSHDOWN子句自动创建外部表之前，我们需要在本地数据库上定义代表外部服务器的服务器对象。 作为示例，我们将定义2个服务器对象S1和S2，以表示2个外部服务器，在本节的其余部分中将引用它们。

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

- 然后，我们将创建用户映射，将两个服务器对象的本地超级用户” highgo”映射到远程超级用户” highgo”。

$ CREATE USER MAPPING FOR highgo SERVER S1 OPTIONS ( user ‘highgo’ );

CREATE USER MAPPING

$ CREATE USER MAPPING FOR highgo SERVER S2 OPTIONS ( user ‘highgo’ );

CREATE USER MAPPING

- 最后，可以使用服务器对象S1和S2，我们将在接下来的部分中使用它们来说明WITH PUSHDOWN子句的便利性。