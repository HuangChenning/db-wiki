---
title: "PLPython-Python过程语言"
book: "服务器编程指南"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceTwo10.html"
tags:
  - highgo
  - highgo-v9
  - server-programming-guide
---

## PL/Python - Python 过程语言

PL/Python 过程语言允许用 Python 语言编写瀚高数据库函数。

要在一个特定数据库中安装 PL/Python，请使用 `CREATE EXTENSION plpythonu` （另见第 14.1 节）。

> **提示：**
> 
> 如果把一种语言安装在 `template1` 中，所有后续创建的数据库都会自动安装该语言。

PL/Python 只是一种”不可信”语言，这意味着它没有提供任何方法来限制用户在其中的所作所为，并且因此被命名为 `plpythonu` 。如果未来开发出在 Python 中的安全执行机制，可能会出现一种可信的变体 `plpython` 。不可信 PL/Python 中函数的编写者必须注意该函数不能被用来做任何它不应该做的事情，因为它将能做以数据库管理员用户登录能做的事情。只有超级用户能够创建 `plpythonu` 等不可信语言中的函数。

> **注意：**
> 
> 源码包的用户必须在安装过程中特别地启用 PL/Python 的编译（更多信息请参考安装指导）。二进制包的用户可以在一个单独的子包中找到 PL/Python。

## Python 2 vs. Python 3

PL/Python 同时支持 Python 2 和 Python 3 两种语言变体（瀚高数据库安装指导可能包含了所支持的 Python 次版本的更精确的信息）。因为 Python 2 和 Python 3 语言变体在某些重要的方面并不兼容，PL/Python 使用了下列命名和转换模式以避免混淆它们：

- 名为 `plpython2u` 的瀚高数据库语言实现了基于 Python 2 语言变体的 PL/Python。
- 名为 `plpython3u` 的瀚高数据库语言实现了基于 Python 3 语言变体的 PL/Python。
- 名为 `plpythonu` 的语言实现了基于默认 Python 语言变体（当前是 Python 2）的 PL/Python（这种默认与任何本地 Python 安装所认为的”默认”无关，例如 `/usr/bin/python` ）。在遥远的未来，瀚高数据库的发布中可能会把这种默认语言变体改成 Python 3，这取决于 Python 社区迁移到 Python 3 的进度。

这种模式类似于 [PEP 394](https://www.python.org/dev/peps/pep-0394/) 中关于 `python` 命令的命名和转换的推荐。

到底是 Python 2 还是 Python 3 的 PL/Python 可用或是两者都可用，取决于编译配置或者被安装的包。

> **提示：**
> 
> 如果是编译安装，则取决于在安装期间找到的 Python 版本或者用 `PYTHON` 环境变量显式设置的版本，见第 16.4 节。要在一个安装中让两种变体的 PL/Python 都可用，源代码树必须被配置和编译两次。

这产生了下列的使用和迁移策略：

- 现有用户以及对 Python 3 不感兴趣的用户使用 `plpythonu` 语言并且在可预见的未来不必做出任何改变。我们推荐通过迁移到 Python 2.6/2.7 逐步地让代码”经得起未来的考验”以简化最终迁移到 Python 3 的工作。
- 对于代码严重依赖于 Python 2 并且不打算做改变的用户可以使用 `plpython2u` 语言。这将在很长时间内都有效，直到瀚高数据库完全删除掉对 Python 2 的支持。
- 想投入 Python 3 的怀抱的用户可以使用 `plpython3u` 语言，在当前的标准下这将一直有效。在遥远的未来，当 Python 3 成为默认以后，出于审美的原因，”3”可能会被移除。
- 想要构建一个只有 Python 3 的操作系统环境的冒险者们，可以更改 `pg_pltemplate` 的内容让 `plpythonu` 等价于 `plpython3u` ，记住这将会让他们的安装与世界的其他大部分东西都不兼容。

有关移植到 Python 3 的更多信息还可见文档 [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) 。

不允许在同一个会话中使用基于 Python 2 的 PL/Python 以及基于 Python 3 的 PL/Python，因为动态模块中的符号会冲突，这会导致瀚高数据库服务器进程的崩溃。在一个会话中有一个检查来阻止混淆 Python 的主版本，如果检测到不匹配会中断会话。不过，可以在同一个数据库中对不同的会话使用两种 PL/Python 变体。

## PL/Python 函数

PL/Python 中的函数通过标准的 `CREATE FUNCTION` 语法声明：

```sql
CREATE FUNCTION funcname (argument-list)
RETURNS return-type
AS $$
    # PL/Python 函数体
$$ LANGUAGE plpythonu;
```

函数体就是一个 Python 脚本。当函数被调用时，它的参数被当做列表 `args` 的元素传递，命名参数也被作为普通变量传递给 Python 脚本。使用命名参数通常可读性更好。Python 代码会以通常的方式返回结果，即使用 `return` 或者 `yield` （在结果集合语句的情况中）。如果没有提供一个返回值，Python 会返回默认的 `None` 。PL/Python 会把 Python 的 `None` 翻译成 SQL 空值。在一个过程中，Python 代码的结果必须是 `None` （通常实现为结束过程时不写 `return` 语句或者使用不带参数的 `return` ），否则将会发生错误。

例如，一个返回两个整数中较大的整数的函数可以定义为：

```sql
CREATE FUNCTION pymax (a integer, b integer)
RETURNS integer
AS $$
    if a > b:
        return a
    return b
$$ LANGUAGE plpythonu;
```

作为该函数定义给出的 Python 代码会被转换成一个 Python 函数。例如上面的代码会得到：

```python
def __plpython_procedure_pymax_23456():
    if a > b:
        return a
    return b
```

假定 23456 是瀚高数据库分配给这个函数的 OID。

参数被设置为全局变量。由于 Python 的可见范围规则，这会导致一种后果：在函数内不能把一个参数变量重新赋予给一个涉及该变量名称本身的表达式的值，除非在该代码块中重新声明该变量为全局的。例如，下面的代码无法工作：

```sql
CREATE FUNCTION pystrip(x text)
RETURNS text
AS $$
    x = x.strip()  # 错误
    return x
$$ LANGUAGE plpythonu;
```

因为对 `x` 的赋值让 `x` 成为了整个代码块的一个局部变量，并且因此该赋值操作右边的 `x` 引用的是一个还未赋值的局部变量 `x` ，而不是 PL/Python 函数的参数。通过使用 `global` 语句，可以让上面的代码正常工作：

```sql
CREATE FUNCTION pystrip(x text)
RETURNS text
AS $$
    global x
    x = x.strip()  # 现在好了
    return x
$$ LANGUAGE plpythonu;
```

但是不建议依赖于这类 PL/Python 的实现细节。最好把函数参数当作是只读。

## 数据值

一般来讲，PL/Python 的目标是提供在瀚高数据库和 Python 世界之间的一种”自然的”映射。这包括下面介绍的数据映射规则。

### 数据类型映射

在调用一个 PL/Python 函数时，它的参数会被从瀚高数据库的数据类型转换成相应的 Python 类型：

- 瀚高数据库的 `boolean` 被转换成 Python 的 `bool` 。
- 瀚高数据库的 `smallint` 和 `int` 被转换成 Python 的 `int` 。瀚高数据库的 `bigint` 和 `oid` 被转换成 Python 2 的 `long` 或者 Python 3 的 `int` 。
- 瀚高数据库的 `real` 和 `double` 被转换成 Python 的 `float` 。
- 瀚高数据库的 `numeric` 被转换成 Python 的 `Decimal` 。如果存在 `cdecimal` 包，则会从其中导入该类型。否则将使用来自标准库的 `decimal.Decimal` 。 `cdecimal` 比 `decimal` 要更快。不过，在 Python 3.3 以及更高的版本中， `cdecimal` 已经被整合到了标准库中（也是用 `decimal` 这个名字），因此也就不再有什么区别。
- 瀚高数据库的 `bytea` 被转换成 Python 的 `str` （Python 2）和 `bytes` （Python 3）。在 Python 2 中，串应该被当做没有任何字符编码的字节序列对待。
- 包括瀚高数据库字符串类型在内的所有其他数据类型会被转换成一个 Python 的 `str` 。在 Python 2 中，这个串将用瀚高数据库服务器编码；在 Python 3 中，它将和所有串一样使用 Unicode。
- 对于非标量数据类型，请见下文。

当一个 PL/Python 函数返回时，会按照下列规则把它的返回值转换成该函数声明的瀚高数据库返回数据类型：

- 当瀚高数据库返回类型是 `boolean` 时，返回值会被根据 Python 规则计算真假。也就是说，0 和空串是假，但是要特别注意 `'f'` 是真。
- 当瀚高数据库返回类型是 `bytea` 时，返回值会被使用相应的 Python 内建机制转换成串（Python 2）或者字节（Python 3），结果将被转换成 `bytea` 。
- 对于所有其他瀚高数据库返回类型，返回值被使用 Python 内建的 `str` 转换成一个串，并且结果会被传递给瀚高数据库数据类型的输入函数（如果该 Python 值是一个 `float` ，它会被用内建的 `repr` 而不是 `str` 转换，这是为了避免精度损失）。
- 当 Python 2 的串被传递给瀚高数据库时，它们被要求是瀚高数据库服务器编码。在当前服务器编码中不可用的串将会产生错误，但是并非所有的编码失配都能被检测到，因此当没有正确地将串编码时，垃圾数据仍然会产生。Unicode 串会被自动地转换为正确的编码，因此使用 Unicode 串更加安全并且更加方便。在 Python 3 中，所有串都是 Unicode 串。
- 对于非标量数据类型，请见下文。

注意所声明的瀚高数据库返回类型和实际返回对象的 Python 数据类型之间的逻辑失配不会被标志，无论怎样该值都会被转换。

### Null, None

如果一个 SQL 空值被传递给一个函数，该参数值将作为 Python 中的 `None` 出现。例如，第 14.2 节中展示的 `pymax` 的函数定义对于空值输入将会返回错误的回答。我们可以为函数定义增加 `STRICT` 让瀚高数据库做得更加合理：如果一个空值被传入，该函数将根本不会被调用，而只是自动地返回一个空结果。此外，我们可以在函数体中检查空输入：

```sql
CREATE FUNCTION pymax (a integer, b integer)
RETURNS integer
AS $$
    if (a is None) or (b is None):
        return None
    if a > b:
        return a
    return b
$$ LANGUAGE plpythonu;
```

如前所示，要从一个 PL/Python 函数返回一个 SQL 空值，可返回值 `None` 。不管该函数严格与否都可以这样做。

### 数组、列表

SQL 数组会被作为一个 Python 列表传递到 PL/Python 中。要从一个 PL/Python 函数中返回出一个 SQL 数组值，可返回一个 Python 列表：

```sql
CREATE FUNCTION return_arr()
RETURNS int[]
AS $$
    return [1, 2, 3, 4, 5]
$$ LANGUAGE plpythonu;

SELECT return_arr();
 return_arr  
-------------
 {1,2,3,4,5}
row
```

多维数组被当做嵌套的 Python 列表传入 PL/Python。例如，一个 2 维数组是一个列表的列表。

在把一个多维 SQL 数组从 PL/Python 函数返回出去时，每一层的内层列表都必须是相同的尺寸。例如：

```sql
CREATE FUNCTION test_type_conversion_array_int4(x int4[]) RETURNS int4[] AS $$
    plpy.info(x, type(x))
    return x
$$ LANGUAGE plpythonu;

SELECT * FROM test_type_conversion_array_int4(ARRAY[[1,2,3],[4,5,6]]);
INFO:  ([[1, 2, 3], [4, 5, 6]], <type 'list'>)
 test_type_conversion_array_int4 
---------------------------------
 {{1,2,3},{4,5,6}}
row
```

为了与瀚高数据库的 9.6 以及更低版本的向后兼容性，当不支持多维数组时，也接受元组之类的其他 Python 序列。不过，它们总是被当做一维数组，因为它们会和组合类型混淆。出于同样的原因，当一个组合类型被用在多维数组中时，它必须被表示为一个元组而不是一个列表。

注意在 Python 中，串是序列，这可能产生与 Python 程序员所熟悉的不同的效果：

```sql
CREATE FUNCTION return_str_arr()
RETURNS varchar[]
AS $$
    return "hello"
$$ LANGUAGE plpythonu;

SELECT return_str_arr();
 return_str_arr 
----------------
 {h,e,l,l,o}
row
```

### 组合类型

组合类型参数被作为 Python 映射传递给函数。映射的元素名称就是组合类型的属性名。如果被传递的行中有一个属性是空值，在映射中它的值是 `None` 。这里是一个例子：

```sql
CREATE TABLE employee (
    name text,
    salary integer,
    age integer
);

CREATE FUNCTION overpaid (e employee)
RETURNS boolean
AS $$
    if e["salary"] > 200000:
        return True
    if (e["age"] < 30) and (e["salary"] > 100000):
        return True
    return False
$$ LANGUAGE plpythonu;
```

有多种方式从一个 Python 函数返回行或者组合类型。下面的例子假设我们有：

```sql
CREATE TYPE named_value AS (
    name text,
    value integer
);
```

一个组合结果可以被返回为：

**序列类型** （一个元组或者列表，但不是集合，因为集合不能被索引）被返回的序列对象必须具有和组合结果类型的域个数相同的项。索引号为 0 的项被分配给组合类型的第一个域，为 1 的项给第二个域，以此类推。例如：

```sql
CREATE FUNCTION make_pair (name text, value integer)
RETURNS named_value
AS $$
    return ( name, value )
    # or alternatively, as tuple: return [ name, value ]
$$ LANGUAGE plpythonu;
```

要为任意列返回一个 SQL 空，应在对应的位置插入 `None` 。

当一个组合类型的数组被返回时，它不能被返回为列表，因为会弄不清该 Python 列表究竟是表示一个组合类型还是另一个数组维度。

**映射（字典）**

用列名作为键从映射中检索每一个结果类型列的值。例如：

```sql
CREATE FUNCTION make_pair (name text, value integer)
RETURNS named_value
AS $$
    return { "name": name, "value": value }
$$ LANGUAGE plpythonu;
```

任何额外的字典键/值对都会被忽略。丢失的键会被当做错误。要为任意列返回一个 SQL 空，应用相应的列名作为键插入 `None` 。

**对象** （任何提供方法 `__getattr__` 的对象）

这和映射的运作方式相同。例如：

```sql
CREATE FUNCTION make_pair (name text, value integer)
RETURNS named_value
AS $$
    class named_value:
        def __init__ (self, n, v):
            self.name = n
            self.value = v
    return named_value(name, value)

    # 或简单地
    class nv: pass
    nv.name = name
    nv.value = value
    return nv
$$ LANGUAGE plpythonu;
```

也支持具有 `OUT` 参数的函数。例如：

```sql
CREATE FUNCTION multiout_simple(OUT i integer, OUT j integer) AS $$
    return (1, 2)
$$ LANGUAGE plpythonu;

SELECT * FROM multiout_simple();
```

过程的输出参数会以同样的方式传回。例如：

```sql
CREATE PROCEDURE python_triple(INOUT a integer, INOUT b integer) AS $$
    return (a * 3, b * 3)
$$ LANGUAGE plpythonu;

CALL python_triple(5, 10);
```

### 集合返回函数

PL/Python 函数也能返回标量类型或者组合类型的集合。有多种方法可以做到这一点，因为被返回的对象在内部会被转变成一个迭代器。下面的例子假设我们有组合类型：

```sql
CREATE TYPE greeting AS (
    how text,
    who text
);
```

可从以下类型返回集合结果：

**序列类型** （元组、列表、集合）

```sql
CREATE FUNCTION greet (how text)
RETURNS SETOF greeting
AS $$
    # 把包含列表的元组返回为组合类型
    # 所有其他组合也能行
    return ( [ how, "World" ], [ how, "PostgreSQL" ], [ how, "PL/Python" ] )
$$ LANGUAGE plpythonu;
```

**迭代器** （任何提供 `__iter__` 以及 `next` 方法的对象）

```sql
CREATE FUNCTION greet (how text)
RETURNS SETOF greeting
AS $$
    class producer:
        def __init__ (self, how, who):
            self.how = how
            self.who = who
            self.ndx = -1

        def __iter__ (self):
            return self

        def next (self):
            self.ndx += 1
            if self.ndx == len(self.who):
                raise StopIteration
            return ( self.how, self.who[self.ndx] )

    return producer(how, [ "World", "PostgreSQL", "PL/Python" ])
$$ LANGUAGE plpythonu;
```

**发生器** （ `yield` ）

```sql
CREATE FUNCTION greet (how text)
RETURNS SETOF greeting
AS $$
    for who in [ "World", "PostgreSQL", "PL/Python" ]:
        yield ( how, who )
$$ LANGUAGE plpythonu;
```

也支持有 `OUT` 参数的集合返回函数（使用 `RETURNS SETOF record` ）。例如：

```sql
CREATE FUNCTION multiout_simple_setof(n integer, OUT integer, OUT integer)
RETURNS SETOF record AS $$
    return [(1, 2)] * n
$$ LANGUAGE plpythonu;

SELECT * FROM multiout_simple_setof(3);
```

## 共享数据

在对同一个函数的重复调用之间可用全局字典 `SD` 来存储私有数据。全局字典 `GD` 是公共数据，它对一个会话中的所有 Python 函数都可用，使用起来要小心。

在 Python 解释器中每一个函数都会得到自己的执行环境，因此来自 `myfunc` 的全局数据和函数参数对 `myfunc2` 不可用。例外是 `GD` 字典中的数据。

## 匿名代码块

PL/Python 也支持用 `DO` 语句调用的匿名代码块：

```sql
DO $$
    # PL/Python 代码
$$ LANGUAGE plpythonu;
```

匿名代码块没有参数，并且任何可能返回的值都会被丢弃。否则，其行为就像一个函数。

## 触发器函数

当函数被用作触发器时，字典 `TD` 包含触发器相关的值：

- **`TD["event"]`**
	包含字符串型的事件： `INSERT` 、 `UPDATE` 、 `DELETE` 或者 `TRUNCATE` 。
- **`TD["when"]`**
	包含 `BEFORE` 、 `AFTER` 或者 `INSTEAD OF` 之一。
- **`TD["level"]`**
	包含 `ROW` 或者 `STATEMENT` 。
- **`TD["new"]`**
- **`TD["old"]`**
	对于行级触发器，这些域的一个或者两个包含相应的触发器行，这取决于触发器事件是什么。
- **`TD["name"]`**
	包含触发器的名称。
- **`TD["table_name"]`**
	包含该触发器发生其上的表名。
- **`TD["table_schema"]`**
	包含该触发器发生其上的表所属的模式名。
- **`TD["relid"]`**
	包含该触发器发生其上的表的 OID。
- **`TD["args"]`**
	如果 `CREATE TRIGGER` 命令包括参数，它们可以通过 `TD["args"][0]` 至 `TD["args"][n-1]` 使用。

如果 `TD["when"]` 是 `BEFORE` 或者 `INSTEAD OF` 并且 `TD["level"]` 是 `ROW` ，可以从 Python 函数返回 `None` 或者 `"OK"` 来表示行没有被修改。返回 `"SKIP"` 可以中止事件，或者在 `TD["event"]` 为 `INSERT` 或 `UPDATE` 时可以返回 `"MODIFY"` 以表示已经修改了新行。否则返回值会被忽略。

## 数据库访问

PL/Python 语言模块会自动导入一个被称为 `plpy` 的 Python 模块。这个模块中的函数和常量在 Python 代码中可以用 `plpy.foo` 这样的方式访问。

### 数据库访问函数

`plpy` 模块提供了几个函数来执行数据库命令：

- **`plpy.execute(query [, max-rows])`**
	用一个查询字符串和一个可选的行限制参数调用 `plpy.execute` 会让该查询运行并且其结果会被以一个结果对象返回。
	结果对象模拟一个列表或者字典对象。可以用行号和列名来访问结果对象。例如：
	```python
	rv = plpy.execute("SELECT * FROM my_table", 5)
	```
	会从 `my_table` 中返回 5 行。如果 `my_table` 有一列是 `my_column` ，可以这样来访问它：
	```python
	foo = rv[i]["my_column"]
	```
	可以用内建的 `len` 函数获得返回的行数。
	结果对象有这些额外的方法：
	- `nrows()` - 返回被该命令处理的行数。注意这不一定与返回的行数相同。例如， `UPDATE` 命令将会设置这个值但是不返回任何行（除非使用 `RETURNING` ）。
		- `status()` - `SPI_execute()` 的返回值。
		- `colnames()` - 返回一个列名列表。
		- `coltypes()` - 返回列类型 OID 列表。
		- `coltypmods()` - 返回列的类型相关的类型修饰符列表。
	在来自于不产生结果集合的命令的结果对象上调用这些方法会产生异常，例如不带 `RETURNING` 的 `UPDATE` 或者 `DROP TABLE` 。但是在包含的行数为零的结果集合上使用这些方法是 OK 的。
	`__str__()` - 也定义了标准的 `__str__` 方法，例如可以使用 `plpy.debug(rv)` 来调试查询执行结果。
	结果对象可以被修改。
	注意调用 `plpy.execute` 将会导致整个结果集合被读入到内存中。只有当确信结果集相对比较小时才应使用这个函数。在取得大型结果时，如果不想冒着耗尽内存的风险，应使用 `plpy.cursor` 而不是 `plpy.execute` 。
- **`plpy.prepare(query [, argtypes])`**
- **`plpy.execute(plan [, arguments [, max-rows]])`**
	`plpy.prepare` 为一个查询准备执行计划。它的参数是一个查询串和一个参数类型列表（如果查询中有参数引用）。例如：
	```python
	plan = plpy.prepare("SELECT last_name FROM my_users WHERE first_name = $1", ["text"])
	```
	`text` 是要为 `$1` 传递的变量的类型。如果不想给查询传递任何参数，第二个参数就是可选的。
	在准备好一个语句后，可以使用函数 `plpy.execute` 的一种变体来运行它：
	```python
	rv = plpy.execute(plan, ["name"], 5)
	```
	把计划作为第一个参数传递（而不是查询字符串），并且把要替换到查询中的值列表作为第二个参数传递。如果查询不需要任何参数，则第二个参数是可选的。和前面一样，第三个参数是可选的，它用来指定行数限制。
	另外，你可以在计划对象上调用 `execute` 方法：
	```python
	rv = plan.execute(["name"], 5)
	```
	查询参数以及结果行域会按照第 45.3 节中所述在瀚高数据库和 Python 数据类型之间转换。
	在使用 PL/Python 模块准备一个计划时，它会被自动保存。其含义可以阅读 SPI 文档。为了有效在函数调用之间利用这种特性，需要使用一种持久化存储字典 `SD` 或者 `GD` 。例如：
	```sql
	CREATE FUNCTION usesavedplan() RETURNS trigger AS $$
	    if "plan" in SD:
	        plan = SD["plan"]
	    else:
	        plan = plpy.prepare("SELECT 1")
	        SD["plan"] = plan
	    # 函数的剩余部分
	$$ LANGUAGE plpythonu;
	```
- **`plpy.cursor(query)`**
- **`plpy.cursor(plan [, arguments])`**
	`plpy.cursor` 函数接受和 `plpy.execute` 相同的参数（行数限制除外）并且返回一个游标对象，它允许以较小的块来处理大型的结果集合。和 `plpy.execute` 一样（行数限制除外），既可以使用一个查询字符串，也可以使用带有参数列表的计划对象，或者 `cursor` 函数可以作为计划对象的一个方法来调用。
	游标对象提供了一种 `fetch` 方法，它接受一个整数参数并返回一个结果对象。每次调用 `fetch` ，返回的对象将包含下一批行，行数不会超过参数值。一旦所有的行都被消耗掉， `fetch` 会开始返回一个空的结果对象。游标对象也提供一种迭代器接口，它一次得到一行直到所有行被耗尽。用这种方法取得的数据不会被作为结果对象返回，而是以字典的形式返回，每一个字典对应于一个结果行。
	从一个大型表中以上述两种方式处理数据的例子：
	sql
	```
	CREATE FUNCTION count_odd_iterator() RETURNS integer AS $$
	    odd = 0
	    for row in plpy.cursor("select num from largetable"):
	        if row['num'] % 2:
	            odd += 1
	    return odd
	$$ LANGUAGE plpythonu;
	CREATE FUNCTION count_odd_fetch(batch_size integer) RETURNS integer AS $$
	    odd = 0
	    cursor = plpy.cursor("select num from largetable")
	    while True:
	        rows = cursor.fetch(batch_size)
	        if not rows:
	            break
	        for row in rows:
	            if row['num'] % 2:
	                odd += 1
	    return odd
	$$ LANGUAGE plpythonu;
	CREATE FUNCTION count_odd_prepared() RETURNS integer AS $$
	    odd = 0
	    plan = plpy.prepare("select num from largetable where num % $1 <> 0", ["integer"])
	    rows = list(plpy.cursor(plan, [2]))  # or: = list(plan.cursor([2]))
	    return len(rows)
	$$ LANGUAGE plpythonu;
	```
	游标会被自动丢弃掉。但是如果想要显式地释放游标所持有的所有资源，可使用 `close` 方法。一旦被关闭，就再也不能从游标中取得数据。

> **提示：**
> 
> 不要把 `plpy.cursor` 创建的游标对象与 [Python Database API specification](https://www.python.org/dev/peps/pep-0249/) 定义的 DB-API 游标弄混。除了名字之外，它们之间没有任何共同点。

### 捕捉错误

访问数据库的函数可能会碰到错误，这将导致函数中止并且产生异常。 `plpy.execute` 和 `plpy.prepare` 都能产生 `plpy.SPIError` 的一个子类的实例，这默认将终止该函数。通过使用 `try/except` 结构，这种错误可以像其他 Python 异常一样被处理。例如：

```sql
CREATE FUNCTION try_adding_joe() RETURNS text AS $$
    try:
        plpy.execute("INSERT INTO users(username) VALUES ('joe')")
    except plpy.SPIError:
        return "something went wrong"
    else:
        return "Joe added"
$$ LANGUAGE plpythonu;
```

产生的异常的实际类对应于特定的导致该错误的情况。可能的情况列表请参考表 A.1。模块 `plpy.spiexceptions` 为每一种瀚高数据库情况定义了一个异常类，并且根据情况的名称命名。例如： `division_by_zero` 变成 `DivisionByZero` ， `unique_violation` 变成 `UniqueViolation` ， `fdw_error` 变成 `FdwError` ，等等等等。这些异常类的每一种都是从 `SPIError` 继承而来。这种分离让处理特定错误更加容易，例如：

```sql
CREATE FUNCTION insert_fraction(numerator int, denominator int) RETURNS text AS
$$
    from plpy import spiexceptions
    try:
        plan = plpy.prepare("INSERT INTO fractions (frac) VALUES ($1 / $2)", ["int", "int"])
        plpy.execute(plan, [numerator, denominator])
    except spiexceptions.DivisionByZero:
        return "denominator cannot equal zero"
    except spiexceptions.UniqueViolation:
        return "already have that fraction"
    except plpy.SPIError, e:
        return "other error, SQLSTATE %s" % e.sqlstate
    else:
        return "fraction inserted"
$$ LANGUAGE plpythonu;
```

注意因为所有来自于 `plpy.spiexceptions` 模块的异常都继承自 `SPIError` ，一个处理它的 `except` 子句将捕捉任何数据库访问错误。

作为另一种处理不同错误情况的方法，可以捕捉 `SPIError` 异常并且在 `except` 块中通过查看异常对象的 `sqlstate` 属性来判断错误情况。这种属性是包含着 “SQLSTATE” 错误代码的一个字符串值。这种方法提供了近乎相同的功能。

## 显式子事务

按第 14.7.2 节中所述的从数据库访问导致的错误中恢复可能导致不好的情况：某些操作在其中一个操作失败之前已经成功，并且在从错误中恢复后这些操作的数据形成了一种不一致的状态。PL/Python 通过显式子事务的形式为这种问题提供了一套解决方案。

### 子事务上下文管理器

考虑一个实现在两个账户间进行转账的函数：

```sql
CREATE FUNCTION transfer_funds() RETURNS void AS $$
    try:
        plpy.execute("UPDATE accounts SET balance = balance - 100 WHERE account_name = 'joe'")
        plpy.execute("UPDATE accounts SET balance = balance + 100 WHERE account_name = 'mary'")
    except plpy.SPIError, e:
        result = "error transferring funds: %s" % e.args
    else:
        result = "funds transferred correctly"
    plan = plpy.prepare("INSERT INTO operations (result) VALUES ($1)", ["text"])
    plpy.execute(plan, [result])
$$ LANGUAGE plpythonu;
```

如果第二个 `UPDATE` 语句导致产生一个异常，这个函数将会报告该错误，但是第一个 `UPDATE` 的结果却不会被提交。换句话说，资金将从 Joe 的账户中收回，而不会转移到 Mary 的账户中。

为了避免这类问题，可以把 `plpy.execute` 包裹在显式子事务中。 `plpy` 模块提供了一种助手对象来管理用 `plpy.subtransaction()` 函数创建的显式子事务。这个函数创建的对象实现了 [上下文管理器接口](https://docs.python.org/library/stdtypes.html#context-manager-types) 。通过使用显式子事务，我们可以把函数写成：

```sql
CREATE FUNCTION transfer_funds2() RETURNS void AS $$
    try:
        with plpy.subtransaction():
            plpy.execute("UPDATE accounts SET balance = balance - 100 WHERE account_name = 'joe'")
            plpy.execute("UPDATE accounts SET balance = balance + 100 WHERE account_name = 'mary'")
    except plpy.SPIError, e:
        result = "error transferring funds: %s" % e.args
    else:
        result = "funds transferred correctly"
    plan = plpy.prepare("INSERT INTO operations (result) VALUES ($1)", ["text"])
    plpy.execute(plan, [result])
$$ LANGUAGE plpythonu;
```

注意仍需使用 `try/catch` 。否则异常会传播到 Python 栈的顶层并且将导致整个函数以一个瀚高数据库错误中止，这样不会有任何行被插入到 `operations` 表。子事务上下文管理器不会捕捉错误，它只确保在其范围内执行的所有数据库操作将被原子性地提交或者回滚。在任何类型的异常（并非只是数据库访问产生的错误）退出时，会发生子事务块回滚。在显式子事务块内部产生的常规 Python 异常也会导致子事务被回滚。

### 更旧的 Python 版本

Python 2.6 中默认可用的是使用 `with` 关键词的上下文管理器语法。如果 PL/Python 用的是一种较老的 Python 版本，仍然可以使用显式子事务，尽管不是那么透明。你可以使用别名 `enter` 和 `exit` 调用子事务管理器的 `__enter__` 和 `__exit__` 函数。转移资金的例子函数可以写成：

```sql
CREATE FUNCTION transfer_funds_old() RETURNS void AS $$
    try:
        subxact = plpy.subtransaction()
        subxact.enter()
        try:
            plpy.execute("UPDATE accounts SET balance = balance - 100 WHERE account_name = 'joe'")
            plpy.execute("UPDATE accounts SET balance = balance + 100 WHERE account_name = 'mary'")
        except:
            import sys
            subxact.exit(*sys.exc_info())
            raise
        else:
            subxact.exit(None, None, None)
    except plpy.SPIError, e:
        result = "error transferring funds: %s" % e.args
    else:
        result = "funds transferred correctly"
    plan = plpy.prepare("INSERT INTO operations (result) VALUES ($1)", ["text"])
    plpy.execute(plan, [result])
$$ LANGUAGE plpythonu;
```

> **注意：**
> 
> 尽管 Python 2.5 中实现了上下文管理器，要在那个版本中使用 `with` 语法，需要使用一个 future 语句。不过，由于实现细节的原因，不能在 PL/Python 函数中使用 future 语句。

## 事务管理

在从顶层调用的过程中或者从顶层调用的匿名代码块（ `DO` 命令）中，可以控制事务。要提交当前的事务，可调用 `plpy.commit()` 。要回滚当前事务，可调用 `plpy.rollback()` （注意不能通过 `plpy.execute` 或类似的函数运行 SQL 命令 `COMMIT` 或者 `ROLLBACK` 。这类工作必须用这些函数完成）。在事务结束以后，一个新的事务会自动开始，因此没有独立的函数用来开始新事务。

这里是一个例子：

```sql
CREATE PROCEDURE transaction_test1()
LANGUAGE plpythonu
AS $$
    for i in range(0, 10):
        plpy.execute("INSERT INTO test1 (a) VALUES (%d)" % i)
        if i % 2 == 0:
            plpy.commit()
        else:
            plpy.rollback()
$$;

CALL transaction_test1();
```

当一个显式的子事务处于活跃状态时，事务不能被结束。

## 实用函数

`plpy` 模块也提供了函数：

- `plpy.debug(msg, **kwargs)`
- `plpy.log(msg, **kwargs)`
- `plpy.info(msg, **kwargs)`
- `plpy.notice(msg, **kwargs)`
- `plpy.warning(msg, **kwargs)`
- `plpy.error(msg, **kwargs)`
- `plpy.fatal(msg, **kwargs)`

`plpy.error` 和 `plpy.fatal` 实际上会产生一个 Python 异常（如果没被捕捉），它会被传播到调用查询中导致当前事务或者子事务被中止。 `raise plpy.Error(msg)` 和 `raise plpy.Fatal(msg)` 分别等效于调用 `plpy.error(msg)` 和 `plpy.fatal(msg)` ，不过 `raise` 形式不允许传递关键词参数。其他函数只生成不同优先级的消息。一个特定优先级的消息是被报告给客户端、写入服务器日志还是两者都做，由 `log_min_messages` 和 `client_min_messages` 配置变量控制。

`msg` 参数被给定位一个位置参数。为了向后兼容，可以给出多于一个位置参数。在那种情况下，位置参数形成的元组的字符串表达将会变成报告给客户端的消息。

下列 keyword-only 参数会被接受：

- `detail`
- `hint`
- `sqlstate`
- `schema_name`
- `table_name`
- `column_name`
- `datatype_name`
- `constraint_name`

作为 keyword-only 参数传递的对象的字符串表达可以用来丰富报告给客户端的消息。例如：

```sql
CREATE FUNCTION raise_custom_exception() RETURNS void AS $$
    plpy.error("custom exception message",
               detail="some info about exception",
               hint="hint for users")
$$ LANGUAGE plpythonu;

=# SELECT raise_custom_exception();
ERROR:  plpy.Error: custom exception message
DETAIL:  some info about exception
HINT:  hint for users
CONTEXT:  Traceback (most recent call last):
  PL/Python function "raise_custom_exception", line 4, in <module>
    hint="hint for users")
PL/Python function "raise_custom_exception"
```

另一组工具函数是 `plpy.quote_literal(string)` 、 `plpy.quote_nullable(string)` 以及 `plpy.quote_ident(string)` 。它们等效于之前章节中描述的 内建引用函数 。在构建临时查询时它们能派上用场。

## 环境变量

某些 Python 解释器接受的环境变量也能被用来影响 PL/Python 行为。它们需要在主瀚高数据库服务器进程的环境中设置，例如在一个启动脚本中设置。可用的环境变量取决于 Python 的版本，细节可见 Python 文档。在编写这份文档时，下面的环境变量可以对 PL/Python 产生影响（假定有一个合适的 Python 版本）：

- `PYTHONHOME`
- `PYTHONPATH`
- `PYTHONY2K`
- `PYTHONOPTIMIZE`
- `PYTHONDEBUG`
- `PYTHONVERBOSE`
- `PYTHONCASEOK`
- `PYTHONDONTWRITEBYTECODE`
- `PYTHONIOENCODING`
- `PYTHONUSERBASE`
- `PYTHONHASHSEED`

（Python 的实现细节似乎超出了 PL/Python 的控制范围，某些列在 `python` 手册页上的环境变量只在命令行解释器中有效，但在嵌入式 Python 解释器中无效）。