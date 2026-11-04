---
title: "函数和操作符"
book: "SQL语言参考手册"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceFour9.html"
tags:
  - highgo
  - highgo-v9
  - sql-language-reference
---

## 函数和操作符

瀚高数据库为内建的数据类型提供了大量的函数和操作符。 用户也可以定义它们自己的函数和操作符， 如第 V 部分所述。psql命令\\df和\\do可以分别被用于显示所有可用的函数和操作符的列表。

如果你关心移植性，那么请注意，我们在本章描述的大多数函数和操作符， 除了最琐碎的算术和比较操作符以及一些做了明确标记的函数以外，都没有在SQL标准里声明。某些这种扩展的功能也出现在许多其它SQL数据库管理系统中，并且在很多情况下多个实现的这种功能是相互兼容的和一致的。本章也并没有穷尽一切信息；一些附加的函数在本手册的相关小节里出现。

## 逻辑操作符

常用的逻辑操作符有：

AND

OR

NOT

SQL使用三值的逻辑系统，包括真、假和null，null表示”未知”。观察下面的真值表：

| a | b | a AND b | a OR b |
| --- | --- | --- | --- |
| TRUE | TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE | TRUE |
| TRUE | NULL | NULL | TRUE |
| FALSE | FALSE | FALSE | FALSE |
| FALSE | NULL | FALSE | NULL |

| a | NOT a |
| --- | --- |
| TRUE | FALSE |
| FALSE | TRUE |
| NULL | NULL |

操作符AND和OR是可交换的，也就是说，你可以交换左右操作数而不影响结果。

## 比较函数和操作符

常见的比较操作符都可用，如表8.1所示。

**表 8.1 比较操作符**

| 操作符 | 描述 |
| --- | --- |
| < | 小于 |
| \> | 大于 |
| <= | 小于等于 |
| \>= | 大于等于 |
| \= | 等于 |
| <> or!= | 不等于 |

| 注意： |
| --- |
| !=操作符在分析器阶段被转换成<>。不能把!=和<>操作符实现为做不同的事。 |

比较操作符可以用于所有可以比较的数据类型。所有比较操作符都是双目操作符，它们返回boolean类型；类似于1 < 2 < 3的表达式是非法的（因为没有<操作符可以比较一个布尔值和3）。

如表8.2所示，也有一些比较谓词。它们的行为和操作符很像，但是具有 SQL 标准所要求的特殊语法。

**表 8.2 比较谓词**

| 谓词 | 描述 |
| --- | --- |
| a BETWEEN x AND y | 在x和y之间 |
| a NOT BETWEEN x AND y | 不在x和y之间 |
| a BETWEEN SYMMETRIC x AND y | 在对比较值排序后位于x和y之间 |
| a NOT BETWEEN SYMMETRIC x AND y | 在对比较值排序后不位于x和y之间 |
| a IS DISTINCT FROM b | 不等于，空值被当做一个普通值 |
| a IS NOT DISTINCT FROM b | 等于，空值被当做一个普通值 |
| expression IS NULL | 是空值 |
| expression IS NOT NULL | 不是空值 |
| expression ISNULL | 是空值（非标准语法） |
| expression NOTNULL | 不是空值（非标准语法） |
| boolean\_expression IS TRUE | 为真 |
| boolean\_expression IS NOT TRUE | 为假或未知 |
| boolean\_expression IS FALSE | 为假 |
| boolean\_expression IS NOT FALSE | 为真或者未知 |
| boolean\_expression IS UNKNOWN | 值为未知 |
| boolean\_expression IS NOT UNKNOWN | 为真或者为假 |

BETWEEN谓词可以简化范围测试：

a BETWEEN x AND y

等效于

a >= x AND a <= y

注意BETWEEN认为终点值是包含在范围内的。 NOT BETWEEN可以做相反比较：

a NOT BETWEEN x AND y

等效于

a < x OR a > y

BETWEEN SYMMETRIC和BETWEEN相似，不过BETWEEN SYMMETRIC不要求AND左边的参数小于或等于右边的参数。如果左参数不是小于等于右参数，这两个参数会自动被交换，这样总是会应用一个非空范围。

当有一个输入为空时，普通的比较操作符会得到空（表示”未知”），而不是真或假。例如，7 = NULL得到空，7 <> NULL也一样。如果这种行为不合适，可以使用IS \[ NOT \]

DISTINCT FROM谓词：

a IS DISTINCT FROM b

a IS NOT DISTINCT FROM b

对于非空输入，IS DISTINCT FROM和<>操作符一样。不过，如果两个输入都为空，它会返回假。而如果只有一个输入为空，它会返回真。类似地，IS NOT DISTINCT FROM对于非空输入的行为与=相同，但是当两个输入都为空时它返回真，并且当只有一个输入为空时返回假。因此，这些谓词实际上把空值当作一种普通数据值而不是”unknown”。

要检查一个值是否为空，使用下面的谓词：

expression IS NULL

expression IS NOT NULL

或者等效，但并不标准的谓词：

expression ISNULL

expression NOTNULL

不要写expression = NULL，因为NULL是不”等于”NULL的（控制代表一个未知的值，因此我们无法知道两个未知的数值是否相等）。

| 提示： |
| --- |
| 有些应用可能要求表达式expression = NULL在expression得出空值时返回真。我们强烈建议这样的应用修改成遵循 SQL 标准。但是，如果这样修改不可能完成，那么我们可以使用配置变量transform\_null\_equals。如果打开它，瀚高数据库将把x = NULL子句转换成x IS NULL。 |

如果expression是行值，那么当行表达式本身为非空值或者行的所有域为非空时IS NULL为真。由于这种行为，IS NULL和IS NOT NULL并不总是为行值表达式返回反转的结果，特别是，一个同时包含 NULL 和非空值的域将会对两种测试都返回假。在某些情况下，写成row IS DISTINCT FROM NULL或者row IS NOT DISTINCT FROM NULL会更好，它们只会检查整个行值是否为空而不需要在行的域上做额外的测试。

布尔值也可以使用下列谓词进行测试：

boolean\_expression IS TRUE

boolean\_expression IS NOT TRUE

boolean\_expression IS FALSE

boolean\_expression IS NOT FALSE

boolean\_expression IS UNKNOWN

boolean\_expression IS NOT UNKNOWN

这些谓词将总是返回真或假，从来不返回空值，即使操作数是空也如此。空值输入被当做逻辑值”未知”。 请注意实际上IS UNKNOWN和IS NOT UNKNOWN分别与IS NULL和IS NOT NULL相同， 只是输入表达式必须是布尔类型。

如表8.3中所示，也有一些比较相关的函数可用。

**表 8.3 比较函数**

| 函数 | 描述 | 例子 | 例子结果 |
| --- | --- | --- | --- |
| num\_nonnulls(VARIADIC "any") | 返回非空参数的数量 | num\_nonnulls(1, NULL, 2) | 2 |
| num\_nulls(VARIADIC "any") | 返回空参数的数量 | num\_nulls(1, NULL,2) | 1 |

## 数学函数和操作符

瀚高数据库为很多类型提供了数学操作符。对于那些没有标准数学表达的类型（如日期/时间类型），我们将在后续小节中描述实际的行为。

表8.4展示了所有可用的数学操作符。

**表 8.4 数学操作符**

| 操作符 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- |
| + | 加 | 2 + 3 | 5 |
| \- | 减 | 2 - 3 | \-1 |
| \* | 乘 | 2 \* 3 | 6 |
| / | 除（整数除法截断结果） | 4 / 2 | 2 |
| % | 模（取余） | 5 % 4 | 1 |
| ^ | 指数（从左至右结合） | 2.0 ^ 3.0 | 8 |
| \|/ | 平方根 | \|/ 25.0 | 5 |
| \|\|/ | 立方根 | \|\|/ 27.0 | 3 |
| ! | 阶乘 | 5! | 120 |
| !! | 阶乘（前缀操作符） | !! 5 | 120 |
| @ | 绝对值 | @ -5.0 | 5 |
| & | 按位与 | 91 & 15 | 11 |
| \| | 按位或 | 32 \| 3 | 35 |
| # | 按位异或 | 17 # 5 | 20 |
| ~ | 按位求反 | ~1 | \-2 |
| << | 按位左移 | 1 << 4 | 16 |
| \>> | 按位右移 | 8 >> 2 | 2 |

按位操作操作符只能用于整数数据类型，而其它的操作符可以用于全部数字数据类型。按位操作的操作符还可以用于位串类型bit和bit varying， 如表 8.14所示。

表 8.5显示了可用的数学函数。在该表中，dp表示double precision。这些函数中有许多都有多种不同的形式，区别是参数不同。除非特别指明，任何特定形式的函数都返回和它的参数相同的数据类型。 处理double precision数据的函数大多数是在宿主系统的 C 库基础上实现的；因此，边界情况下的准确度和行为是根据宿主系统而变化的。

**表 8.5 数学函数**

| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| abs(x) | （和输入相同） | 绝对值 | abs(-17.4) | 17.4 |
| cbrt(dp) | dp | 立方根 | cbrt(27.0) | 3 |
| ceil(dp or numeric) | （和输入相同） | 不小于参数的最近的整数 | ceil(-42.8) | \-42 |
| ceiling(dp or numeric) | 和输入相同） | 不小于参数的最近的整数（ceil的别名） | ceiling(-95.3) | \-95 |
| degrees(dp) | dp | 把弧度转为角度 | degrees(0.5) | 28.6478897565412 |
| div(y numeric,x numeric) | numeric | y/x的整数商 | div(9,4) | 2 |
| exp(dp or numeric) | （和输入相同） | 指数 | exp(1.0) | 2.71828182845905 |
| floor(dp or numeric) | （和输入相同） | 不大于参数的最近的整数 | floor(-42.8) | 43 |
| ln(dp or numeric) | （和输入相同） | 自然对数 | ln(2.0) | 0.693147180559945 |
| log(dp or numeric) | （和输入相同） | 以10为底的对数 | log(100.0) | 2 |
| log10(dp or numeric) | （和输入相同） | 以10为底的对数 | log10(100.0) | 2 |
| log(b numeric, x numeric) | numeric | 以b为底的对数 | log(2.0, 64.0) | 6.0000000000 |
| mod(y, x) | （和参数类型相同） | y/x的余数 | mod(9,4) | 1 |
| pi() | dp | “π”常数 | pi() | 3.14159265358979 |
| power(a dp, b dp) | dp | 求a的b次幂 | power(9.0, 3.0) | 729 |
| power(a numeric,b numeric) | numeric | 求a的b次幂 | power(9.0, 3.0) | 729 |
| radians(dp) | dp | 把角度转为弧度 | radians(45.0) | 0.785398163397448 |
| round(dp or numeric) | （和输入相同） | 圆整为最接近的整数 | round(42.4) | 42 |
| round(v numeric, s int) | numeric | 圆整为s位小数数字 | round(42.4382, 2) | 42.44 |
| scale(numeric) | integer | 参数的精度（小数点后的位数） | scale(8.41) | 2 |
| sign(dp or numeric) | （和输入相同） | 参数的符号（-1,0,+1） | sign(-8.4) | \-1 |
| sqrt(dp or numeric) | （和输入相同） | 平方根 | sqrt(2.0) | 1.4142135623731 |
| trunc(dp or numeric) | （和输入相同） | 截断（向零靠近） | trunc(42.8) | 42 |
| trunc(v numeric, s int) | numeric | 截断为s位小数位置的数字 | trunc(42.4382, 2 | 42.43 |
| width\_bucket(op dp,b1 dp,b2 dp,count int) | int | 返回一个桶号，这个桶是在一个柱状图中operand将被分配的那个桶，该柱状图有count个散布在范围b1到b2上的等宽桶。对于超过该范围的输入，将返回0或者count+1。 | width\_bucket(5.35,0.024, 10.06,5) |  |
| width\_bucket(op numeric,b1 numeric,b2 numeric,count int) | int | 返回一个桶号，这个桶是在一个柱状图中operand将被分配的那个桶，该柱状图有count个散布在范围b1到b2上的等宽桶。对于超过该范围的输入，将返回0或者count+1。 | width\_bucket(5.35, 0.024, 10.06, 5) |  |
| width\_bucket(operand anyelement,thresholds anyarray) | int | 返回一个桶号，这个桶是在给定数组中operand 将被分配的桶，该数组列出了桶的下界。对于一个低于第一个下界的输入返回 0。thresholds数组必须被排好序， 最小的排在最前面，否则将会得到意想不到的结果。 | width\_bucket(now(),array\[‘yesterday’,’today’,’tomorrow’\]::timestamptz\[\]) |  |

表 8.6展示了用于产生随机数的函数。

**表 8.6 随机函数**

| 函数 | 返回类型 | 描述 |
| --- | --- | --- |
| random() | dp | 范围 0.0 <= x < 1.0 中的随机值 |
| setseed(dp) | void | 为后续的random()调用设置种子（值为于 -1.0 和 1.0 之间，包括边界值） |

random()函数使用了一个简单的线性共轭算法。 它的速度很快，但不适合于密码学应用；

关于更安全的替代方案，请参阅 pgcrypto模块。 如果setseed()被调用，那么当前会话中的后续random()调用的结果可以通过使用相同的参数重新发布setseed()来重复。

表 8.7显示了可用的三角函数。所有这些函数都有类型为double precision的参数和返回类型。每一种三角函数都有两个变体，一个以弧度度量角，另一个以角度度量角。

**表 8.7 三角函数**

| 函数（弧度） | 函数（角度） | 描述 |
| --- | --- | --- |
| acos(x) | acosd(x) | 反余弦 |
| asin(x) | asind(x) | 反正弦 |
| atan(x) | atand(x) | 反正切 |
| atan2(y, x) | atan2d(y, x) | y/x的反正切 |
| cos(x) | cosd(x) | 余弦 |
| cot(x) | cotd(x) | 余切 |
| sin(x) | sind(x) | 正弦 |
| tan(x) | tand(x) | 正切 |

| 注意： |
| --- |
| 另一种使用以角度度量的角的方法是使用早前展示的单位转换函数radians()和degrees()。不过，使用基于角度的三角函数更好，因为这类方法能避免sind(30)等特殊情况下的舍入偏差。 |

表 8.8显示的是 可用的双曲函数。 所有这些函数接收参数，并返回类型为double precision的值。

**表 8.8 双曲函数**

| 函数 | 描述 | 举例 | 结果 |
| --- | --- | --- | --- |
| sinh(x) | 双曲正弦 | sinh(0) | 0 |
| cosh(x) | 双曲余弦 | cosh(0) | 1 |
| tanh(x) | 双曲切线 | tanh(0) | 0 |
| asinh(x) | 反双曲正弦 | asinh(0) | 0 |
| acosh(x) | 反双曲余弦 | acosh(1) | 0 |
| atanh(x) | 反双曲切线 | atanh(0) | 0 |

## 字符串函数和操作符

本节描述了用于检查和操作字符串值的函数和操作符。在这个环境中的串包括所有类型character、character varying和text的值。除非另外说明，所有下面列出的函数都可以处理这些类型，不过要小心的是，在使用character类型的时候， 它有自动填充空白的潜在影响。有些函数还可以处理位串类型。

SQL定义了一些字符串函数，它们使用关键字，而不是逗号来分隔参数。详情请见表 8.9，瀚高数据库也提供了这些函数使用正常函数调用语法的版本（见表 8.10）。

| 注意： |
| --- |
| 字符串串接操作符（\|\|）接受非字符串输入，只要至少一个输入是一种字符串类型，如表 8.9所示。对于其他情况，如果你需要复制之前的行为，可以为text插入一个显式强制措施。 |

**表 8.9 SQL字符串函数和操作符**

| 函数 | 返回类型 | 描述 | 例子 | 结果 |
| --- | --- | --- | --- | --- |
| string \|\| string | text | 串接 | 'High' \|\| 'Go' | HighGo |
| string \|\| non string 或non string \|\| string | text | 使用一个非字符串输入的串接 | 'Value: ' \|\| 42 | Value：42 |
| bit\_length(string) | int | 串中的位数 | bit\_length('jose') | 32 |
| char\_length(string) 或character\_length(string) | int | 串中的位数 | char\_length('jose') | 4 |
| lower(string) | text | 将字符串转换为小写形式 | lower('TOM') | tom |
| octet\_length(string) | int | 串中的字节数 | octet\_length('jose') | 4 |
| overlay(string placing string from int \[for int\]) | text | 替换子串 | overlay('Txxxxas' placing 'hom' from 2 for 4) | Thomas |
| position(substring in string) | int | 定位指定子串 | position('om' in 'Thomas') | 3 |
| substring(string \[from int\] \[for int\]) | text | 提取子串 | substring('Thomas' from 2 for 3) |  |
| substring(string from pattern) | text | 提取匹配POSIX正则表达式的子串。模式匹配详情见第 8.7 节。 | substring('Thomas' from '...$') |  |
| substring(string from pattern for escape) | text | 提取匹配SQL正则表达式的子串。模式匹配详情见第 8.7 节。 | substring('Thomas' from '%#"o\_a#"\_' for '#' |  |
| trim(\[leading \| trailing \| both\] \[characters\] from string) | text | 从string的开头、结尾或者两端（both是默认值）移除只包含characters（默认是一个空格）中字符的最长字符串。 | trim(both 'xyz' from 'yxTomxx') | Tom |
| trim(\[leading \| trailing \| both\] \[from\] string \[,characters\] ) | text | trim()的非标准版本。 | trim(both from 'xTomxx', 'x') | Tom |
| upper(string) | text | 将字符串转换成大写形式。 | upper('tom') | TOM |

还有额外的串操作函数可以用，它们在表 8.10中列出。它们有些在内部用于实现表 9.9列出的SQL标准字符串函数。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| ascii(string) | int | 参数第一个字符的ASCII代码。对于UTF8返回该字符的Unicode代码点。对于其他多字节编码，该参 数必须是一个 ASCII字符。 | ascii(‘x’) | 120 |
| btrim(string text \[, characters text\]) | text | 从string的开头或结尾删除最长 的只包含characters（默认是一个空格） 的串 | btrim(‘xyxtrimyyx’, ‘xyz’) | trim |
| chr(int) | text | 给定代码的字符。对于UTF8该参数被视作一个 Unicode代码点。对于其他多字节编码该参数必须指定一个ASCII字符。NULL (0) 字符不被允许，因 为文本数据类型不能存储这种字节。 | chr(65) | A |
| concat(str “any” \[, str “any” \[, …\] \]) | text | 串接所有参数的文本表示。NULL 参数被忽略。 | concat(‘abcde’, 2, NULL, 22) | abcde222 |
| concat\_ws(sep text, str “any” \[, str “any” \[, …\] \]) | text | 将除了第一个参数外的其他参数 用分隔符串接在一起。第一个参数被用作分隔符字符串。NULL 参 数被忽略。 | concat\_ws(‘,’, ‘abcde’, 2, NULL, 22) | abcde,2,22 |
| convert(string bytea, src\_encoding name, dest\_encoding name) | bytea | 将字符串转换 为dest\_encoding。 原始编码由src\_encoding指 定。string在这 个编码中必须可 用。转换可以使用CREATE CONVERSION定 义。也有一些预 定义的转换。可 用的转换请 见表 8.11。 | convert(‘text\_in\_utf8’, ‘UTF8’, ‘LATIN1’) | 用Latin-1 encoding (ISO 8859-1) 表示 的text\_in\_utf8 |
| convert\_from(string bytea, src\_encoding name) | text | 将字符串转换为 数据库编码。原 始编码由src\_encoding指 定。string在这 个编码中必须可 用。 | convert\_from(‘text\_in\_utf8’, ‘UTF8’) | 用当前数据库编 码表示 的text |
| convert\_to(string text, dest\_encoding name) | bytea | 将字符串转换 为dest\_encoding | convert\_to(‘some text’, ‘UTF8’) | 用UTF8编码表达 的some text |
| decode(string text, format text) | bytea | 从string中的文本表达解码二进制数 据。format的选项和encode中的一样。 | decode(‘MTIzAAE=’, ‘base64’) | 3132330001 |
| encode(data bytea, format text) | text | 将二进制数据编码成一个文本表达。支持的格式有：base64、hex、escape。escape将 零字节和高位组字节转换为八进制序列（\\nnn）和双写的反斜 线。 | encode(‘123\\000\\001’, ‘base64’) | TIzAAE |
| format(formatstr text \[, formatarg “any” \[, …\] \]) | text | 根据一个格式字符串格式化参数。该函数和C函数sprintf相似。 见第 8.4.1 节 | format(‘Hello %s, %1$s’, ‘World’) | Hello World, World |
| initcap(string) | text | 将每一个词的第一个字母转换为大写形式并把剩下的字母转换为小写形式。词是由非字母数字字 符分隔的字母数字字符的序列。 | initcap(‘hi THOMAS’) | Hi Thomas |
| left(str text, n int) | text | 返回字符串中的前n个字符。当n为负时，将返回除了最后\|n\|个 字符之外的所有字符。 | left(‘abcde’, 2) | ab |
| length(string) | int | string中的字符数 | length(‘jose’) | 4 |
| length(string bytea, encoding name ) | text | string在给定编码中的字符 数。string必须在这个编码中有效。 | length(‘jose’, ‘UTF8’) | 4 |
| lpad(string text, length int \[,fill text\]) | text | 将string通过前置字符fill（默认是一个空格）填充到长度length。如果string已经长于length，则它 被（从右边）截断。 | lpad(‘hi’, 5, ‘xy’) | xyxhi |
| ltrim(string text \[, characters text\]) | text | 从string的开头删除最长的只包含characters（默认是一个空格）的串 | ltrim(‘zzzytest’, ‘xyz’) | test |
| md5(string) | text | 计算string的 MD5 哈希，返回十六进制的结果 | md5(‘abc’) | 900150983cd24fb0 d6963f7d28e17f72 |
| parse\_ident(qualified\_identifier text \[, strictmode boolean DEFAULT true \] ) | text\[\] | 把qualified\_identifier分成一个标识符数组，移除单个标识符上的任何引号。默认情况下，最后一个标识符后面的多余字符会被当做错误。但是如果第二个参数 为false，那么这一类多余的字符会被忽略（这种行为对于解析函数之类的对象名 称有用）。注意这个函数不会截断超长标识符。 如果想要进行截断，可以把结果转换成name\[\]。 | parse\_ident(‘“SomeSchema”.someTable’) | {SomeSchema,sometable} |
| pg\_client\_encoding() | name | 当前的客户端编码名字 | pg\_client\_encoding() | SQL\_ASCII |
| quote\_ident(string text) | text | 将给定字符串返回成合适的引用形式，使它可以在一个SQL语句字 符串中被用作一个标识符。只有需要时才会加上引号（即，如果 字符串包含非标识符字符或可能是大小写折叠的）。嵌入的引号会被正确地双写。 | quote\_ident(‘Foo bar’) | “Foo bar” |
| quote\_literal(string text) | text | 将给定字符串返回成合适的引用形式，使它可以在一个SQL语句字符串中被用作一 个字符串文字。嵌入的引号会被正确地双写。注意quote\_literal对空输入返回空；如果参数可能为空，quote\_nullable通常更合适。 | quote\_literal(E’O 'Reilly’) | ‘Reilly’ |
| quote\_literal(value anyelement) | text | 强迫给定值为文本并且接着将它用引号包围作为一个文本。嵌入的单引号和反斜线被正确的双 写。 | quote\_literal() | 42.5’ |
| quote\_nullable(string text) | text | 将给定字符串返回成合适的引用形式，使它可以在一个SQL语句字符串中被用作一 个字符串文字；或者，如果参数为空，返回NULL。嵌入的引号会被正确地双写。请参 见例 42.1 | quote\_nullable(NULL) | NULL |
| quote\_nullable(value anyelement) | text | 强迫给定值为文本并且接着将它用引号包围作为一个文本；或者，如果参数为空，返回NULL。 嵌入的单引号和反斜线被正确的双写。 | quote\_nullable(42.5) | ‘42.5’ |
| regexp\_match(string text, pattern text \[, flags text\]) | text\[\] | 返回一个POSIX正 则表达式 与string的第一个匹配得到的子串。更多信息请见第 8.7.3 节 | regexp\_match(‘foobarbequebaz’, ‘(bar)(beque)’) | ‘barbequebaz’ |
| regexp\_matches(string text, pattern text \[, flags text\]) | setof text\[\] | 返回一个POSIX正则表达式与string匹配得到的子串。更多信息请 见第 8.7.3 节。 | regexp\_matches(‘foobarbequebaz’, ‘ba.’, ‘g’) | Foobar{baz} (2 rows) |
| regexp\_replace(string text, pattern text, replacement text \[, flags text\]) |  | 替换匹配一个 POSIX正则表达式 的子串。详 见第 8.7.3 节 | regexp\_replace(‘Thomas’, ‘.\[mN\]a.’, ‘M’) | Thomas |
| regexp\_split\_to\_array(string text, pattern text \[, flags text \]) | text\[\] | 使用一个POSIX正 则表达式作为分 隔符划 分string。详 见第8.7.3 节 | regexp\_split\_to\_array(‘hello world’, ‘\\s+’) | array(‘hello) |
| regexp\_split\_to\_table(string text, pattern text \[, flags text\]) | setof text | 使用一个POSIX正 则表达式作为分 隔符划 分string。详 见第 8.7.3 节 | regexp\_split\_to\_table(‘hello world’, ‘\\s+’) | Tableworld (2 rows) |
| repeat(string text, number int) | text | 重复string指定 的number次 | repeat(‘Pg’, 4) | PgPgPgPg |
| replace(string text, from text, to text) | text | 将string中出现的所有子 串from替换为子串to | replace(‘abcdefabcdef’, ‘cd’, ‘XX’) |  |
| reverse(str) | text | 返回反转的字符串。 | reverse(‘abcde’) | edcba |
| right(str text, n int) | text | 返回字符串中的最后n个字符。如果n为负，返回除 最前面的\|n\|个字符外的所有字符。 | right(‘abcde’, 2) | de |
| rpad(string text, length int \[,fill text\]) | text | 将string通过增加字符fill（默认为一个空格）填充到长度length。如 果string已经长于length则它会被截断。 | rpad(‘hi’, 5, ‘xy’) | hixyx |
| rtrim(string text \[, characters text\]) | text | 从string的结尾删除最长的只包含characters（默认是一个空格）的串 | rtrim(‘testxxzx’, ‘xyz’) | test |
| split\_part(string text, delimiter text, field int) | text | 按delimiter划分string并返回给定域（从1开始 计算） | split\_part(‘abc ~~@~~ def ~~@~~ ghi’, ‘ ~~@~~ ‘, 2) |  |
| strpos(string, substring) | int | 指定子串的位置 （和position(substring in string)相同，但是注意相反的参数顺序） | strpos(‘high’, ‘ig’) | 2 |
| substr(string, from \[, count\]) | text |  | 提取子串 （与substring(string from from for count)相同） | substr(‘alphabet’, 3, 2) ph |
| starts\_with(string, prefix) | bool | 如果string以prefix开 始则返回真。 | starts\_with(‘alphabet’, ‘alph’) |  |
| to\_ascii(string text \[,encoding text\]) | text | 将string从另一个编码转换到 ASCII（只支持 从LATIN1、LATIN2、LATIN9和WIN1250编 码的转换） | to\_ascii(‘Karel’)Karel |  |
| to\_hex(number int or bigint) | text | 将number转换到它等效的十六进制表示 | to\_hex(2147483647)7fffffff |  |
| translate(string text, from text, to text) | text | string中任何匹配from集合中一个字符的字符会 被替换成to集合中的相应字符。如果from比to长，from中 的额外字符会被删除。 | translate(‘12345’, ‘143’, ‘ax’) | a2x5 |

: 表 8.10 其他字符串函数

concat、concat\_ws和format函数是可变的，因此可以把要串接或格式化的值作为一个标记了VARIADIC关键字的数组进行传递（见第 37.5.5 节）。数组的元素被当作函数的独立普通参数一样处理。如果可变数组参数为 NULL，concat和concat\_ws返回 NULL，但format把NULL 当作一个零元素数组。

还可以参阅第 8.20 节中的string\_agg。

| **转换名** | **源编码** | **目标编码** |
| --- | --- | --- |
| ascii\_to\_mic | SQL\_ASCII | MULE\_INTERNAL |
| ascii\_to\_utf8 | SQL\_ASCII | UTF8 |
| big5\_to\_euc\_tw | BIG5 | EUC\_TW |
| big5\_to\_mic | BIG5 | MULE\_INTERNAL |
| big5\_to\_utf8 | BIG5 | UTF8 |
| euc\_cn\_to\_mic | EUC\_CN | MULE\_INTERNAL |
| euc\_cn\_to\_utf8 | EUC\_CN | UTF8 |
| euc\_jp\_to\_mic | EUC\_JP | MULE\_INTERNAL |
| euc\_jp\_to\_sjis | EUC\_JP | SJIS |
| euc\_jp\_to\_utf8 | EUC\_JP | UTF8 |
| euc\_kr\_to\_mic | EUC\_KR | MULE\_INTERNAL |
| euc\_kr\_to\_utf8 | EUC\_KR | UTF8 |
| euc\_tw\_to\_big5 | EUC\_TW | BIG5 |
| euc\_tw\_to\_mic | EUC\_TW | MULE\_INTERNAL |
| euc\_tw\_to\_utf8 | EUC\_TW | UTF8 |
| gb18030\_to\_utf8 | GB18030 | UTF8 |
| gbk\_to\_utf8 | GBK |  |
| iso\_8859\_10\_to\_utf8 | LATIN6 |  |
| iso\_8859\_13\_to\_utf8 | LATIN7 |  |
| iso\_8859\_14\_to\_utf8 | LATIN8 |  |
| iso\_8859\_15\_to\_utf8 | LATIN9 |  |
| iso\_8859\_16\_to\_utf8 | LATIN10 |  |
| iso\_8859\_1\_to\_mic | LATIN1 | MULE\_INTERNAL |
| iso\_8859\_1\_to\_utf8 | LATIN1 | UTF8 |
| iso\_8859\_2\_to\_mic | LATIN2 | MULE\_INTERNAL |
| iso\_8859\_2\_to\_utf8 | LATIN2 | UTF8 |
| iso\_8859\_3\_to\_mic | LATIN3 | MULE\_INTERNAL |
| iso\_8859\_3\_to\_utf8 | LATIN3 | UTF8 |
| iso\_8859\_4\_to\_mic | LATIN4 | MULE\_INTERNAL |
| iso\_8859\_4\_to\_utf8 | LATIN4 | UTF8 |
| iso\_8859\_5\_to\_koi8\_r | ISO\_8859\_5 | KOI8R |
| iso\_8859\_5\_to\_mic | ISO\_8859\_5 | MULE\_INTERNAL |
| iso\_8859\_5\_to\_utf8 | ISO\_8859\_5 | UTF8 |
| iso\_8859\_6\_to\_utf8 | ISO\_8859\_6 | UTF8 |
| iso\_8859\_7\_to\_utf8 | ISO\_8859\_7 | UTF8 |
| iso\_8859\_8\_to\_utf8 | ISO\_8859\_8 | UTF8 |
| iso\_8859\_9\_to\_utf8 | LATIN5 | UTF8 |
| johab\_to\_utf8 | JOHAB | UTF8 |
| koi8\_r\_to\_iso\_8859\_5 | KOI8R | ISO\_8859\_5 |
| koi8\_r\_to\_mic | KOI8R | MULE\_INTERNAL |
| koi8\_r\_to\_utf8 | KOI8R | UTF8 |
| koi8\_u\_to\_utf8 | KOI8U | UTF8 |
| mic\_to\_ascii | MULE\_INTERNAL | SQL\_ASCII |
| mic\_to\_big5 | MULE\_INTERNAL | BIG5 |
| mic\_to\_euc\_cn | MULE\_INTERNAL | EUC\_CN |
| mic\_to\_euc\_jp | MULE\_INTERNAL | EUC\_JP |
| mic\_to\_euc\_kr | MULE\_INTERNAL | EUC\_KR |
| mic\_to\_euc\_tw | MULE\_INTERNAL | EUC\_TW |
| mic\_to\_iso\_8859\_1 | MULE\_INTERNAL | LATIN1 |
| mic\_to\_iso\_8859\_2 | MULE\_INTERNAL | LATIN2 |
| mic\_to\_iso\_8859\_3 | MULE\_INTERNAL | LATIN3 |
| mic\_to\_iso\_8859\_4 | MULE\_INTERNAL | LATIN4 |
| mic\_to\_iso\_8859\_5 | MULE\_INTERNAL | ISO\_8859\_5 |
| mic\_to\_koi8\_r | MULE\_INTERNAL | KOI8R |
| mic\_to\_sjis | MULE\_INTERNAL | SJIS |
| sjis\_to\_euc\_jp | SJIS | EUC\_JP |
| sjis\_to\_mic | SJIS | MULE\_INTERNAL |
| sjis\_to\_utf8 | SJIS | UTF8 |
| uhc\_to\_utf8 | UHC | UTF8 |
| utf8\_to\_ascii | UTF8 | SQL\_ASCII |
| utf8\_to\_big5 | UTF8 | BIG5 |
| utf8\_to\_euc\_cn | UTF8 | EUC\_CN |
| utf8\_to\_euc\_jp | UTF8 | EUC\_JP |
| utf8\_to\_euc\_kr | UTF8 | EUC\_KR |
| utf8\_to\_euc\_tw | UTF8 | EUC\_TW |
| utf8\_to\_gb18030 | UTF8 | GB18030 |
| utf8\_to\_gbk | UTF8 | GBK |
| utf8\_to\_iso\_8859\_1 | UTF8 | LATIN1 |
| utf8\_to\_iso\_8859\_10 | UTF8 | LATIN6 |
| utf8\_to\_iso\_8859\_13 | UTF8 | LATIN7 |
| utf8\_to\_iso\_8859\_14 | UTF8 | LATIN8 |
| utf8\_to\_iso\_8859\_15 | UTF8 | LATIN9 |
| utf8\_to\_iso\_8859\_16 | UTF8 | LATIN10 |
| utf8\_to\_iso\_8859\_2 | UTF8 | LATIN2 |
| utf8\_to\_iso\_8859\_3 | UTF8 | LATIN3 |
| utf8\_to\_iso\_8859\_4 | UTF8 | LATIN4 |
| utf8\_to\_iso\_8859\_5 | UTF8 | ISO\_8859\_5 |
| utf8\_to\_iso\_8859\_6 | UTF8 | ISO\_8859\_6 |
| utf8\_to\_iso\_8859\_7 | UTF8 | ISO\_8859\_7 |
| utf8\_to\_iso\_8859\_8 | UTF8 | ISO\_8859\_8 |
| utf8\_to\_iso\_8859\_9 | UTF8 | LATIN5 |
| utf8\_to\_johab | UTF8 | JOHAB |
| utf8\_to\_koi8\_r | UTF8 | KOI8R |
| utf8\_to\_koi8\_u | UTF8 | KOI8U |
| utf8\_to\_sjis | UTF8 | SJIS |
| utf8\_to\_uhc | UTF8 | UHC |
| euc\_jis\_2004\_to\_utf8 | EUC\_JIS\_2004 | UTF8 |
| utf8\_to\_euc\_jis\_2004 | UTF8 | EUC\_JIS\_2004 |
| shift\_jis\_2004\_to\_utf8 | SHIFT\_JIS\_2004 | UTF8 |
| utf8\_to\_shift\_jis\_2004 | UTF8 | SHIFT\_JIS\_2004 |
| euc\_jis\_2004\_to\_shift\_jis\_2004 | EUC\_JIS\_2004 | SHIFT\_JIS\_2004 |
| shift\_jis\_2004\_to\_euc\_jis\_2004 | SHIFT\_JIS\_2004 | EUC\_JIS\_2004 |

: 表 8.11 内建转换

转换名遵循一种标准命名模式：将全部非字母数字字符替换为下划线的源编码的官方名称，后面跟上\_to\_，最后是按照相似方式处理过的目标编码名称。因此，名称可能会不同于习惯的编码名称。

### format

函数format根据一个格式字符串产生格式化的输出，其形式类似于 C 函数sprintf。

format(formatstr text \[, formatarg "any" \[,...\] \])

formatstr是一个格式字符串，它指定了结果应该如何被格式化。格式字符串中的文本被直接复制到结果中，除了使用格式说明符的地方。格式说明符在字符串中扮演着占位符的角色，它定义后续的函数参数如何被格式化及插入到结果中。每一个formatarg参数会被根据其数据类型的常规输出规则转换为文本，并接着根据格式说明符被格式化和插入到结果字符串中。

格式说明符由一个%字符开始并且有这样的形式

%\[position\]\[flags\]\[width\]type

其中的各组件域是：

position（可选）

一个形式为n$的字符串，其中n是要打印的参数的索引。索引 1 表示formatstr之后的第一个参数。如果position被忽略，默认会使用序列中的下一个参数。

flags（可选）

控制格式说明符的输出如何被格式化的附加选项。当前唯一支持的标志是一个负号（-），它将导致格式说明符的输出会被左对齐（left-justified）。除非width域也被指定，否者这个域不会产生任何效果。

width（可选）

指定用于显示格式说明符输出的最小字符数。输出将被在左部或右部（取决于-标志）用空格填充以保证充满该宽度。太小的宽度设置不会导致输出被截断，但是会被简单地忽略。宽度可以使用下列形式之一指定：一个正整数；一个星号（\*）表示使用下一个函数参数作为宽度；或者一个形式为\*n$的字符串表示使用第n个函数参数作为宽度。

如果宽度来自于一个函数参数，则参数在被格式说明符的值使用之前就被消耗掉了。如果宽度参数是负值，结果会在长度为abs(width)的域中被左对齐（如果-标志被指定）。

type（必需）

格式转换的类型，用于产生格式说明符的输出。支持下面的类型：

• s将参数值格式化为一个简单字符串。一个控制被视为一个空字符串。

• I将参数值视作 SQL 标识符，并在必要时用双写引号包围它。如果参数为空，将会是一个错误（等效于quote\_ident）。

• L将参数值引用为 SQL 文字。一个空值将被显示为不带引号的字符串NULL（等效于quote\_nullable）。

除了以上所述的格式说明符之外，要输出一个文字形式的%字符，可以使用特殊序列%%。

下面有一些基本的格式转换的例子：

SELECT format('Hello %s', 'World');

结果：Hello World

SELECT format('Testing %s, %s, %s, %%', 'one', 'two', 'three');

结果：Testing one, two, three, %

SELECT format('INSERT INTO %I VALUES(%L)', 'Foo bar', E'O\\'Reilly');

结果：INSERT INTO "Foo bar" VALUES('O''Reilly')

SELECT format('INSERT INTO %I VALUES(%L)', 'locations', 'C:\\Program Files');

结果：INSERT INTO locations VALUES(E'C:\\\\Program Files')

下面是使用width域和-标志的例子：

SELECT format('|%10s|', 'foo');

结果：| foo|

SELECT format('|%-10s|', 'foo');

结果：|foo |

SELECT format('|%\*s|', 10, 'foo');

结果：| foo|

SELECT format('|%\*s|', -10, 'foo');

结果：|foo |

SELECT format('|%-\*s|', 10, 'foo');

结果：|foo |

SELECT format('|%-\*s|', -10, 'foo');

结果：|foo |

这些例子展示了position域的例子：

SELECT format('Testing %3$s, %2$s, %1$s', 'one', 'two', 'three');

结果：Testing three, two, one

SELECT format('|%\*2$s|', 'foo', 10, 'bar');

结果：| bar|

SELECT format('|%1$\*2$s|', 'foo', 10, 'bar');

结果：| foo|

不同于标准的 C 函数sprintf，瀚高数据库的format函数允许将带有或者不带有position域的格式说明符被混在同一个格式字符串中。一个不带有position域的格式说明符总是使用最后一个被消耗的参数的下一个参数。另外，format函数不要求所有函数参数都被用在格式字符串中。例如：

SELECT format('Testing %3$s, %2$s, %s', 'one', 'two', 'three');

结果：Testing three, two, three

对于安全地构造动态 SQL 语句，%I和%L格式说明符特别有用。

## 二进制串函数和操作符

本节描述那些检查和操作类型为bytea的值的函数和操作符。

SQL定义了一些使用关键字而不是逗号来分割参数的串函数。详情请见表 8.12。瀚高数据库也提供了这些函数使用常规函数调用语法的版本（参阅表 8.13）。

| 注意： |
| --- |
| 本页中显示的示例结果假设服务器参数bytea\_output被设置为escape格式。 |

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| string \|\| string | bytea | 串连接 | ‘\\High’::bytea \|\| ‘\\047go\\ \\000’::bytea | \\High’go\\000 |
| octet\_length(string) | int | 二进制串中的字 节数 | octet\_length(‘jo \\000se’::bytea) | 5 |
| overlay(string placing string from int \[for int\]) | bytea | 替换子串 | overlay(‘Th \\000omas’::bytea placing ‘\\002\\003’::bytea from 2 for 3) | T\\002\\003mas |
| position(substring in string) | int | 指定子串的位置 | position(‘\\000om’ in ‘Th \\000omas’::bytea) | ‘::bytea |
| substring(string \[from int\] \[for int\]) | bytea | 提取子串 | substring(‘Th \\000omas’::bytea from 2 for 3) | h\\000o |
| trim(\[both\] bytes from string) | bytea | 从string的开头或结尾删除只包含出现在bytes中字节的最长串 | trim(‘\\000\\001’::bytea from ‘\\000Tom \\001’::bytea) |  |

: 表 8.12 SQL二进制串函数和操作符

还有一些二进制串处理函数可以使用，在表 8.13列出。 其中有一些是在内部使用，用于实现表 8.12列出的 SQL 标准串函数。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| btrim(string bytea, bytes bytea) | bytea | 从string的开头或结尾删除只由出现在bytes中字节组成的最长串 | btrim(‘\\000trim \\001’::bytea, ‘\\000\\001’::bytea) | trim |
| decode(string text, format text) | bytea | 从string中的文 本表示解码二进 制数据。format的参数和在encode中 一样。 | decode(‘123\\000456’, ‘escape’) | 000456 |
| encode(data bytea, format text) | text | 将二进制数据编 码为一个文本表 示。支持的格式有：base64、hex、escape。escape将 零字节和高位组 字节转换为八进 制序列（\\nnn） 和双反斜线。 | encode(‘123\\000456’::bytea, ‘escape’) | ::bytea, |
| get\_bit(string, offset) | int | 从串中抽取位 | get\_bit(‘Th \\000omas’::bytea, 45) | 1 |
| get\_byte(string, offset) | int | 从串中抽取字节 | get\_byte(‘Th \\000omas’::bytea, 4) | 109 |
| length(string) | int | 二进制串的长度 | length(‘jo \\000se’::bytea) | 5 |
| md5(string) | text | 计算string的MD5哈希码，以十六进制形式返回结 果 | md5(‘Th \\000omas’::bytea) | 8ab2d3c9689aaf18 b4958c334c82d8b1 |
| set\_bit(string, offset, newvalue) | bytea | 设置串中的位 | set\_bit(‘Th \\000omas’::bytea, 45, 0) | Th\\000omAs |
| set\_byte(string, offset, newvalue) | bytea | 设置串中的字节 | set\_byte(‘Th \\000omas’::bytea, 4, 64) | Th\\000o@as |
| sha224(bytea) | bytea | SHA-224哈希 | sha224(‘abc’) | \\x23097d223405d8228642a477bda2 55b32aadbce4bda0b3f7e36c9da7 |
| sha256(bytea) | bytea | SHA-256哈希 | sha256(‘abc’) | \\xba7816bf8f01cfea414140de5dae2223 b00361a396177a9cb410ff61f20015 |
| sha384(bytea) | bytea | SHA-384哈希 | sha384(‘abc’) | \\xcb00753f45a35e8bb5a03d699ac65007 272c32ab0eded1631a8b605a43ff5bed 8086072ba1e7cc2358baeca134c825 |
| sha512(bytea) | bytea | SHA-512哈希 | sha512(‘abc’) | \\xddaf35a193617abacc417349ae204131 12e6fa4e89a97ea20a9eeee64b55d39a 2192992a274fc1a836ba3c23a3feebbd 454d4423643ce80e2a9ac94fa54ca4 |

: 表 8.13 其他二进制串函数

get\_byte和set\_byte把一个二进制串中的一个字节计数为字节 0。get\_bit和set\_bit在每一个字节中从右边起计数位；例如位 0 是第一个字节的最低有效位，而位 15 是第二个字节的最高有效位。

注意由于历史原因，函数md5返回的是一个十六进制编码的text值，而SHA-2函数返回类型bytea。可以使用函数encode和decode在两者之间转换，例如encode(sha256('abc'), 'hex')可以得到一个十六进制编码的文本表示。

参见第 8.20 节中的聚集函数string\_agg以及第 34.4 节中的大对象函数。

## 位串函数和操作符

本节描述用于检查和操作位串的函数和操作符，也就是操作类型为bit和bit varying的值的函数和操作符。除了常用的比较操作符之外，还可以使用表 9.14里显示的操作符。&、|和#的位串操作数必须等长。在移位的时候，保留原始的位串的的长度，如例子所示。

| **操作符** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- |
| \|\| | 连接 | B’10001’ \|\| B’011’ | 10001011 |
| & | 按位与 | B’10001’ & B’01101’ | 00001 |
| \| | 按位或 | B’10001’ \| B’01101’ | 11101 |
| # | 按位异或 | B’10001’ # B’01101’ | 11100 |
| ~ | 按位求反 | ~ B’10001’ | 01110 |
| << | 按位左移 | B’10001’ << 3 | 01000 |
| \>> | 按位右移 | B’10001’ >> 2 | 00100 |

: 表 8.14 位串操作符

下面的SQL标准函数除了可以用于字符串之外，也可以用于位串： length、 bit\_length、octet\_length、 position、 substring、 overlay。

下面的函数除了可以用于二进制串之外，也可以用于位串： get\_bit、 set\_bit。 当使用于一个位串时，这些函数将串的第一（最左）位计数为位 0。

另外，我们可以在整数和bit之间来回转换。一些例子：

44::bit(10) 0000101100

44::bit(3) 100

cast(-44 as bit(12)) 111111010100

'1110'::bit(4)::integer 14

请注意，如果只是转换为”bit”，意思是转换成bit(1)，因此只会转换整数的最低有效位。

| 注意： |
| --- |
| 把一个整数转换成bit(n)将拷贝整数的最右边的n位。 把一个整数转换成比整数本身长的位串，就会在最左边扩展符号。 |

## 模式匹配

瀚高数据库提供了三种独立的实现模式匹配的方法：SQL LIKE操作符、更近一些的SIMILAR TO操作符（SQL:1999 里添加进来的）和POSIX-风格的正则表达式。除了这些基本的”这个串匹配这个模式吗？”操作符外，还有一些函数可用于提取或替换匹配子串并在匹配位置分离一个串。

| **提示：** |
| --- |
| 如果你的模式匹配的要求超出了这些，请考虑用 Perl 或 Tcl 写一个用户定义的函数。 |

| 注意： |
| --- |
| 虽然大部分的正则表达式搜索都能被很快地执行，但是正则表达式仍可能被人为地弄成需要任意长的时间和任意量的内存进行处理。要当心从不怀好意的来源接受正则表达式搜索模式。如果必须这样做，建议加上语句超时限制。   使用SIMILAR TO模式的搜索具有同样的安全性危险， 因为SIMILAR TO提供了很多和 POSIX-风格正则表达式相同的能力。LIKE搜索比其他两种选项简单得多，因此在使用 不怀好意的模式来源时要更安全些。 |

这三种类型的模式匹配算子都不支持非确定性拼贴。 如果需要的话，可以在表达式中应用不同的拼贴来绕过这个限制。

### LIKE

string LIKE pattern \[ESCAPE escape-character\]

string NOT LIKE pattern \[ESCAPE escape-character\]

如果该string匹配了提供的pattern，那么LIKE表达式返回真（和预期的一样，如果LIKE返回真，那么NOT LIKE表达式返回假， 反之亦然。一个等效的表达式是NOT (string LIKE pattern)）。

如果pattern不包含百分号或者下划线，那么该模式只代表它本身的串；这时候LIKE的行为就象等号操作符。在pattern里的下划线 （\_）代表（匹配）任何单个字符； 而一个百分号（%）匹配任何零或更多个字符的序列。

一些例子：

'abc' LIKE 'abc' true

'abc' LIKE 'a%' true

'abc' LIKE '\_b\_' true

'abc' LIKE 'c' false

LIKE模式匹配总是覆盖整个串。因此，要匹配在串内任何位置的序列，该模式必须以百分号开头和结尾。

要匹配文本的下划线或者百分号，而不是匹配其它字符， 在pattern里相应的字符必须前导逃逸字符。缺省的逃逸字符是反斜线，但是你可以用ESCAPE子句指定一个不同的逃逸字符。 要匹配逃逸字符本身，写两个逃逸字符。

| 注意： |
| --- |
| 如果你关掉了standard\_conforming\_strings，你在文串常量中写的任何反斜线都需要被双写。详见第 4.1.2.1 节。 |

请注意反斜线在串文本里已经有特殊含义了，所以如果你写一个 包含反斜线的模式常量，那你就要在 SQL 语句里写两个反斜线。 因此，写一个匹配单个反斜线的模式实际上要在语句里写四个反斜线。 你可以通过用 ESCAPE 选择一个不同的逃逸字符 来避免这样；这样反斜线就不再是 LIKE 的特殊字符了。 但仍然是字符文本分析器的特殊字符，所以你还是需要两个反斜线。) 我们也可以通过写ESCAPE ''的方式不选择逃逸字符，这样可以有效地禁用逃逸机制，但是没有办法关闭下划线和百分号在模式中的特殊含义。

关键字ILIKE可以用于替换LIKE， 它令该匹配根据活动区域成为大小写无关。这个不属于 SQL标准而是一个瀚高数据库扩展。

操作符~~等效于LIKE， 而~~\*对应ILIKE。 还有!~~和!~~\*操作符分别代表NOT LIKE和NOT ILIKE。所有这些操作符都是瀚高数据库特有的。

在仅需要从字符串的开始部分搜索的情况，还有前缀操作符^@和相应的starts\_with函数可以使用。

### SIMILAR TO正则表达式

string SIMILAR TO pattern \[ESCAPE escape-character\]

string NOT SIMILAR TO pattern \[ESCAPE escape-character\]

SIMILAR TO操作符根据自己的模式是否匹配给定串而返回真或者假。 它和LIKE非常类似，只不过它使用 SQL 标准定义的正则表达式理解模式。SQL 正则表达式是在LIKE标记和普通的正则表达式标记的奇怪的杂交。

类似LIKE，SIMILAR TO操作符只有在它的模式匹配整个串的时候才能成功；这一点和普通的正则表达式的行为不同，在普通的正则表达式里，模式匹配串的任意部分。和LIKE类似的地方还有，SIMILAR TO使用\_和%作为分别代表任意单个字符和任意串的通配符（这些可以比得上 POSIX 正则表达式里的.和.\*）。

除了这些从LIKE借用的功能之外，SIMILAR TO支持下面这些从 POSIX 正则表达式借用的模式匹配元字符：

• |表示选择（两个候选之一）。

• \*表示重复前面的项零次或更多次。

• +表示重复前面的项一次或更多次。

•?表示重复前面的项零次或一次。

• {m}表示重复前面的项刚好m次。

• {m,}表示重复前面的项m次或更多次。

• {m,n}表示重复前面的项至少m次并且不超过n次。

• 可以使用圆括号()把多个项组合成一个逻辑项。

• 一个方括号表达式\[...\]声明一个字符类，就像 POSIX 正则表达式一样。

注意点号（.）不是SIMILAR TO的一个元字符。

和LIKE一样，反斜线禁用所有这些元字符的特殊含义；当然我们也可以用ESCAPE指定一个不同的逃逸字符。

一些例子：

'abc' SIMILAR TO 'abc' true

'abc' SIMILAR TO 'a' false

'abc' SIMILAR TO '%(b|d)%' true

'abc' SIMILAR TO '(b|c)%' false

带有三个参数的substring函数可以提取匹配SQL正则表达式模式的子字符串。 该函数可以按照SQL99语法编写。

substring(string from pattern for escape-character)

或作为一个普通的三参数函数:

substring(string, pattern, escape-character)

与SIMILAR TO一样，指定的模式必须与整个数据字符串匹配，否则函数失败并返回空值。 为了表示匹配的数据子字符串的模式中，模式中应该包含两个转义字符的出现，并在后面加上一个双引号(")。 匹配成功后，将返回与这些分隔符之间的模式部分匹配的文本。

转义-双引号分隔符实际上是 将子字符串的模式分成三个独立的 正则表达式；例如，竖条 (|) 三节中的任何一节只影响到该节。 此外，第一节和第三种正则表达式的定义是为了匹配关于有多少数据字符串符合哪种模式。 (在POSIX术语中，第一和第三种正则表达式被强行规定为非贪婪)。

作为对SQL标准的扩展，瀚高数据库只允许有一个转义双引号分隔符，在这种情况下，第三个正则表达式被视为空；或者没有分隔符，在这种情况下，第一个和第三个正则表达式被视为空。

一些例子，使用#"定界返回串：

substring('foobar' from '%#"o\_b#"%' for '#') oob

substring('foobar' from '#"o\_b#"%' for '#') NULL

### POSIX正则表达式

表 8.15列出了所有可用于 POSIX 正则表达式模式匹配的操作符。

| **操作符** | **描述** | **例子** |
| --- | --- | --- |
| ~ | 匹配正则表达式，大小写敏 感 | ‘thomas’ ~ ‘.*thomas.*‘ |
| ~\* | 匹配正则表达式，大小写不 敏感 | ‘thomas’ ~\* ‘.*Thomas.*‘ |
| !~ | 不匹配正则表达式，大小写 敏感 | ‘thomas’!~ ‘.*Thomas.*‘ |
| !~\* | 不匹配正则表达式，大小写 不敏感 | ‘thomas’!~\* ‘.*vadim.*‘ |

: 表 8.15 正则表达式匹配操作符

POSIX正则表达式提供了比LIKE和SIMILAR TO操作符更强大的含义。许多 Unix 工具，例如egrep、sed或awk使用一种与我们这里描述的类似的模式匹配语言。

正则表达式是一个字符序列，它是定义一个串集合 （一个正则集）的缩写。 如果一个串是正则表达式描述的正则集中的一员时， 我们就说这个串匹配该正则表达式。 和LIKE一样，模式字符准确地匹配串字符， 除非在正则表达式语言里有特殊字符 — 不过正则表达式用的 特殊字符和LIKE用的不同。 和LIKE模式不一样的是，正则表达式允许匹配串里的任何位置，除非该正则表达式显式地挂接在串的开头或者结尾。

一些例子：

'abc' ~ 'abc' true

'abc' ~ '^a' true

'abc' ~ '(b|d)' true

'abc' ~ '^(b|c)' false

POSIX模式语言的详细描述见下文。

带两个参数的substring函数，即substring(string from pattern)，提供了抽取一个匹配 POSIX 正则表达式模式的子串的方法。如果没有匹配它返回空值，否则就是文本中匹配模式的那部分。 但是如果该模式包含任何圆括号，那么将返回匹配第一对子表达式（对应第一个左圆括号的） 的文本。如果你想在表达式里使用圆括号而又不想导致这个例外，那么你可以在整个表达式外边放上一对圆括号。 如果你需要在想抽取的子表达式前有圆括号，参阅后文描述的非捕获性圆括号。

一些例子：

substring('foobar' from 'o.b') oob

substring('foobar' from 'o(.)b') o

regexp\_replace函数提供了将匹配 POSIX 正则表达式模式的子串替换为新文本的功能。 它的语法是

regexp\_replace(source,

pattern,

replacement \[, flags \])。

如果没有匹配pattern，那么返回不加修改的source串。 如果有匹配，则返回的source串里面的匹配子串将被replacement串替换掉。replacement串可以包含\\n， 其中\\n是 1 到 9， 表明源串里匹配模式里第n个圆括号子表达式的子串应该被插入， 并且它可以包含\\&表示应该插入匹配整个模式的子串。如果你需要放一个文字形式的反斜线在替换文本里，那么写\\\\。flags参数是一个可选的文本串，它包含另个或更多单字母标志，这些标志可以改变函数的行为。标志i指定大小写无关的匹配，而标志g指定替换每一个匹配的子串而不仅仅是第一个。支持的标志（但不是g）在表 9.23中描述。

一些例子：

regexp\_replace('foobarbaz', 'b..', 'X')

fooXbaz

regexp\_replace('foobarbaz', 'b..', 'X', 'g')

fooXX

regexp\_replace('foobarbaz', 'b(..)', 'X\\1Y', 'g')

fooXarYXazY

regexp\_match返回一个文本数组，它包含一个POSIX正则表达式模式与一个字符串第一个匹配所得到的子串。其语法是regexp\_match(string, pattern \[, flags \])。如果没有匹配，则结果为NULL。如果找到一个匹配并且pattern不包含带括号的子表达式，那么结果是一个单一元素的文本数组，其中包含匹配整个模式的子串。如果找到一个匹配并且pattern含有带括号的子表达式，那么结果是一个文本数组，其中第n个元素是与pattern的第n个圆括号子表达式匹配的子串（”非捕获”圆括号不计入在内，详见下文）。flags参数是一个可选的文本字符串，它包含零个或者更多个可以改变该函数行为的单字母标志。所支持的标志在表 9.23中介绍。

一些例子：

SELECT regexp\_match('foobarbequebaz', 'bar.\*que');

regexp\_match

\--------------

{barbeque}

(1 row)

SELECT regexp\_match('foobarbequebaz', '(bar)(beque)');

regexp\_match

\--------------

{bar,beque}

(1 row)

在通常情况下，人们只是想要的大整个匹配的子串或者NULL（没有匹配），可以写成这样

SELECT (regexp\_match('foobarbequebaz', 'bar.\*que'))\[1\];

regexp\_match

\--------------

barbeque

(1 row)

regexp\_matches函数返回一个文本数组的集合，其中包含着一个POSIX正则表达式模式与一个字符串匹配得到的子串。它和regexp\_match具有相同的语法。如果没有匹配，这个函数不会返回行。如果有一个匹配并且给定了g标志，则返回一行。如果有N个匹配并且给定了g标志，则返回N行。每一个返回的行都是一个文本数组，其中含有整个匹配的子串或者匹配pattern的圆括号子表达式的子串，这和上面对regexp\_match的介绍一样。regexp\_matches接受表 9.23中展示的所有标志，外加令它返回所有匹配而不仅仅是第一个匹配的g标志。

一些例子：

SELECT regexp\_matches('foo', 'not there');

regexp\_matches

\----------------

(0 rows)

SELECT regexp\_matches('foobarbequebazilbarfbonk', '(b\[^b\]+)(b\[^b\]+)', 'g');

regexp\_matches

\----------------

{bar,beque}

{bazil,barf}

(2 rows)

| **提示：** |
| --- |
| 在大部分情况下，regexp\_matches()应该与g标志一起使用，因为如果只是想要第一个匹配，使用regexp\_match()会更加简单高效。 |

regexp\_split\_to\_table把一个 POSIX 正则表达式模式当作一个定界符来分离一个串。它的语法形式是regexp\_split\_to\_table(string,

pattern \[,flags \])。如果没有与pattern的匹配，该函数返回string。如果有至少有一个匹配，对每一个匹配它都返回从上一个匹配的末尾（或者串的开头）到这次匹配开头之间的文本。当没有更多匹配时，它返回从上一次匹配的末尾到串末尾之间的文本。flags参数是一个可选的文本串，它包含零个或更多单字母标志，这些标识可以改变该函数的行为。regexp\_split\_to\_table能支持的标志在表 9.23中描述。

regexp\_split\_to\_array函数的行为和regexp\_split\_to\_table相同，不过regexp\_split\_to\_array会把它的结果以一个text数组的形式返回。它的语法是regexp\_split\_to\_array(string,pattern \[,flags \])。这些参数和regexp\_split\_to\_table的相同。

一些例子：

SELECT foo FROM regexp\_split\_to\_table('the quick brown fox jumps over the lazy

dog', '\\s+') AS foo;

foo

\-------

the

quick

brown

fox

jumps

over

the

lazy

dog

(9 rows)

SELECT regexp\_split\_to\_array('the quick brown fox jumps over the lazy dog', '\\s

+');

regexp\_split\_to\_array

\-----------------------------------------------

{the,quick,brown,fox,jumps,over,the,lazy,dog}

(1 row)

SELECT foo FROM regexp\_split\_to\_table('the quick brown fox', '\\s\*') AS foo;

foo

\-----

t

h

e

q

u

i

c

k

b

r

o

w

n

f

o

x

(16 rows)

正如上一个例子所示，正则表达式分离函数会忽略零长度的匹配，这种匹配发生在串的开头或结尾或者正好发生在前一个匹配之后。这和正则表达式匹配的严格定义是相悖的，后者由regexp\_match和regexp\_matches实现，但是通常前者是实际中最常用的行为。其他软件系统如Perl也使用相似的定义。

#### 正则表达式细节

瀚高数据库的正则表达式是使用 Henry Spencer 写的一个包来实现的。下面的正则表达式的大部分描述都是从他的手册页中逐字拷贝过来的。

正则表达式（RE），在POSIX 1003.2 中定义， 它有两种形式：扩展的RE或者是 ERE（大概地说就是那些在egrep里的），基本的RE或者是BRE（大概地说就是那些在ed里的）。瀚高数据库支持两种形式，并且还实现了一些POSIX标准中没有但是在类似 Perl 或者Tcl 这样的语言中得到广泛应用的一些扩展。使用了那些非POSIX扩展的RE叫高级RE， 或者本文档里说的ARE。ARE 几乎完全是 ERE 的超集，但是 BRE 有几个符号上的不兼容（以及更多的限制）。我们首先描述 ARE 和 ERE 形式， 描述那些只适用于 ARE 的特性，然后描述BRE 的区别是什么。

| 注意： |
| --- |
| 瀚高数据库初始时总是推测一个正则表达式遵循 ARE 规则。但是，可以通过为 RE 模式预置一个embedded option来选择限制更多的 ERE 或 BRE 规则，如第 8.7.3.4 节中所述。这对为期望准确的POSIX 1003.2 规则的应用提供兼容性很有用。 |

一个正则表达式被定义为一个或更多分支，它们之间被|分隔。只要能匹配其中一个分支的东西都能匹配正则表达式。

一个分支是一个或多个量化原子或者约束连接而成。一个原子匹配第一个，然后后面的原子匹配第二个， 以此类推；一个空分支匹配空串。

一个量化原子是一个原子， 后面可能跟着一个量词。没有量词的时候，它匹配一个原子，有量词的时候，它可以匹配若干个原子。一个原子可以是在表 8.16里面显示的任何可能。

可能的量词和它们的含义在表 8.17里显示。

一个约束匹配一个空串，但只是在满足特定条件下才匹配。 约束可以在能够使用原子的地方使用，只是它不能跟着量词。简单的约束在表8.18里显示； 更多的约束稍后描述。

| **原子** | **描述** |
| --- | --- |
| (re) | （其中re是任何正则表达式） 匹配一个 对re的匹配，匹配将为可能的报告被记下 |
| (?:re) | 同上，但是匹配不会为了报告而被记下 （一 个“非捕获”圆括号集） （只对 ARE） |
| . | 匹配任意单个字符 |
| \[chars\] | 一个方括号表达式， 匹配chars中的任意一 个（详见第 8.7.3.2 节） |
| \\k | （其中k是一个非字母数字字符） 匹配一个 被当作普通字符看待的特定字符， 例如，\\ \\匹配一个反斜线字符 |
| \\c | 其中c是一个字母数字 （可能跟着其它字 符），它是一个逃逸， 参阅第8.7.3.3 节（仅对 ARE； 在 ERE 和 BRE中，它匹配c） |
| { | 如果后面跟着一个字符，而不是数字， 那么 就匹配左花括弧{；如果跟着一个数字， 那 么它是range的开始（见下文） |
| x | 其中x是一个没有其它意义的单个字符，则匹配该字符 |

: 表 8.16 正则表达式原子

RE 不能以反斜线（\\）结尾。

| 注意： |
| --- |
| 如果你关掉了standard\_conforming\_strings，任何你写在文字串常量中的反斜线都需要被双写。详见第 4.1.2.1 节。 |

| **量词** | **匹配** |
| --- | --- |
| \* | 一个由原子的 0 次或更多次匹配组成的序列 |
| + | 一个由原子的 1 次或更多次匹配组成的序列 |
| ? | 一个由原子的 0 次或 1 次匹配组成的序列 |
| {m} | 一个由原子的正好m次匹配组成的序列 |
| {m,} | 一个由原子的m次或更多次匹配组成的序列 |
| {m,n} | 一个由原子的从m次到n次（包括）匹配组成的序列；m不能超过n |
| \*? | \*的非贪婪版本 |
| +? | +的非贪婪版本 |
| ?? | ?的非贪婪版本 |
| {m}? | {m}的非贪婪版本 |
| {m,}? | {m,}的非贪婪版本 |
| {m,n}? | {m,n}的非贪婪版本 |

: 表 8.17 正则表达式量词

使用{...}的形式被称作范围。一个范围内的数字m和n都是无符号十进制整数，允许的数值从 0 到 255（包含）。

非贪婪的量词（只在 ARE 中可用）匹配对应的正常 （贪婪）模式，区别是它寻找最少的匹配，而不是最多的匹配。详见第 8.7.3.5 节

| **注意：** |
| --- |
| 一个量词不能紧跟在另外一个量词后面，例如\*\*是非法的。量词不能作为表达式或者子表达式的开头，也不能跟在^或者\|后面。 |

| **约束** | **描述** |
| --- | --- |
| ^ | 串开头的匹配 |
| $ | 串末尾的匹配 |
| (?=re) | 在匹配re的子串开始的任何点的positive lookahead匹配（只对 ARE） |
| (?!re) | 在匹配re的子串开始的任何点的negative lookahead匹配（只对 ARE） |
| (?<=re) | 只要有一个点上有一个子串匹配re端， positive lookbehind就在这个点上匹配（只对 ARE） |
| (?<!re) | 只要有一个点上没有子串匹配re端， negative lookbehind就在这个点上匹配（只对 ARE） |

: 表 8.18 正则表达式约束

lookahead 和 lookbehind 约束不能包含后引用 （参阅第 8.7.3.3 节），并且其中的所有圆括号 都被认为是非捕获的。

#### 方括号表达式

方括号表达式是一个包围在\[\]中的字符列表。它通常匹配列表中的任意单个字符（但见下文）。 如果列表以^开头，它匹配任意单个不在该列表参与部分中的字符。如果该列表中两个字符用-隔开， 那它就是那两个字符（包括在内）之间的所有字符范围的缩写，例如，在 ASCII中\[0-9\]匹配任何十进制数字。两个范围共享一个端点是非法的，例如，a-c-e。范围与字符集关系密切， 可移植的程序应该避免依靠它们。

想在列表中包含文本\]，可以让它做列表的首字符（如果使用了^，需要放在其后）。想在列表中包含文本-，可以让它做列表的首字符或者尾字符，或者一个范围的第二个端点。 想在列表中把文本-当做范围的起点， 把它用\[.和.\]包围起来，这样它就成为一个排序元素（见下文）。 除了这些字符本身、一些用\[的组合（见下段）以及逃逸（只在 ARE 中有效）以外，所有其它特殊字符在方括号表达式里都失去它们的特殊含义。特别是，在 ERE 和 BRE 规则下\\不是特殊的，但在 ARE 里，它是特殊的（引入一个逃逸）。

在一个方括号表达式里，一个排序元素（一个字符、一个被当做一个单一字符排序的多字符序列或者一个表示上面两种情况的排序序列名称） 包含在\[.和.\]里面的时候表示该排序元素的字符序列。该序列被当做该方括号列表 的一个单一元素。这允许一个包含多字符排序元素的方括号表达式去匹配多于一个字符，例如，如果排序序列包含一个ch排序元素， 那么 RE \[\[.ch.\]\]\*c匹配chchcc的头五个字符。

| **注意：** |
| --- |
| 瀚高数据库当前不支持多字符排序元素。这些信息描述了将来可能有的行为。 |

在方括号表达式里，包围在\[=和=\]里的排序元素是一个等价类， 代表等效于那一个的所有排序元素的字符序列，包括它本身（如果没有其它等效排序元素，那么就好象封装定界符是\[.和.\]）。例如，如果o和^是一个等价类的成员，那么\[\[=o=\]\]、\[\[=^=\]\]和\[o^\]都是同义的。一个等价类不能是一个范围的端点。

在方括号表达式里，在\[:和:\]里面封装的字符类的名字代表属于该类的所有字符的列表。

字符类不能作为范围的端点使用。POSIX标准定义了这些字符类的名称： alnum (字符和数字), alpha (字符), blank (空格和制表符tab), cntrl (控制符), digit (数位数), graph (空格除外可打印字符), lower (小写字母), print (包含空格可打印字符), punct (标点符号), space (空白), upper (大写字母), 和 xdigit (十六进制数). 对于7位ASCII字符集中的字符来说，这些标准字符类的行为在不同平台上一般是一致的。一个给定的非ASCII字符是否被认为属于这些类别中的一个，取决于正则表达式函数或运算符使用的collation，或者默认情况下取决于数据库的LC\_CTYPE locale设置。非ASCII字符的分类在不同的平台上会有不同的分类，即使是在类似命名的locale中也是如此。 (但C locale从不认为任何非ASCII字符属于上述任何一类)。除了这些标准字符类之外，瀚高数据库定义了ascii字符类，它完全包含7位ASCII字符集。

方括号表达式里有两个特例：方括号表达式\[\[:<:\]\]和\[\[:>:\]\]是约束，分别匹配一个单词开头和结束的空串。 单词定义为一个单词字符序列，前面和后面都没有其它单词字符。单词字符是一个alnum字符（和如上所述POSIX字符类中定义的一样） 或者一个下划线。这是一个扩展，兼容POSIX 1003.2， 但那里面并没有说明， 而且在准备移植到其他系统里去的软件里一定要小心使用。通常下文描述的约束逃逸更好些（它们并非更标准，但是更容易键入）。

#### 正则表达式逃逸

逃逸是以\\开头，后面跟着一个字母数字字符得特殊序列。 逃逸有好几种变体：字符项、类缩写、约束逃逸以及后引用。在 ARE 里， 如果一个\\后面跟着一个字母数字，但是并未组成一个合法的逃逸， 那么它是非法的。在 ERE 中没有逃逸：在方括号表达式之外，一个后面跟着字母数字字符的\\只是表示该字符是一个普通的字符，而且在一个方括号表达式里，\\是一个普通的字符（后者实际上在 ERE 和ARE 不兼容）。

字符项逃逸用于便于我们在 RE 中声明那些不可打印的或其他习惯的字符。它们显示在表 8.19中。

类缩写逃逸用来提供一些常用的字符类缩写。它们显示在表8.20中。

约束逃逸是一个约束，如果满足特定的条件，它匹配该空串。它们显示在表 8.21中。

后引用（\\n）匹配数字\\n指定的被前面的圆括号子表达式匹配的同一个串 （参阅表 8.22）。例如，(\[bc\])\\1匹配bb或者cc，但是不匹配bc或者cb。RE 中子表达式必须完全在后引用前面。子表达式以它们的先导圆括号的顺序编号。

非捕获圆括号并不定义子表达式。

| **逃逸** | **描述** |
| --- | --- |
| \\a | 警告（响铃）字符，和 C 中一样 |
| \\b | 退格，和 C 中一样 |
| \\B | 反斜线（\\）的同义词，用来减少双写反斜线 |
| \\cX | （其中X是任意字符）低序5位和X相同的字符，它的其他位都是零 |
| \\e | 排序序列名为ESC的字符，如果无法做到该字符为八进制值 033 |
| \\f | 换页，和 C 中一样 |
| \\n | 新行，和 C 中一样 |
| \\r | 回车，和 C 中一样 |
| \\t | 水平制表符，和 C 中一样 |
| \\uwxyz | （其中wxyz正好是四个十六进制位）十六进 制值为0xwxyz的字符 |
| \\Ustuvwxyz | （其中stuvwxyz正好是八个十六进制位）十 六进制值为0xstuvwxyz的字符 |
| \\v | 垂直制表符，和 C 中一样 |
| \\xhhh | （其中hhh是十六进制位的任意序列）十六进制值为0xhhh的字符（一个单一字符，不管用了多少个十六进制位） |
| \\0 | 值为0（空字节）的字符 |
| \\xy | （其中xy正好是两个八进制位，并且不是一 个后引用）八进制值为0xy的字符 |
| \\xyz | （其中xyz正好是三个八进制位，并且不是一个后引用）八进制值为0xyz的字符 |

: 表 8.19 正则表达式字符项逃逸

十六进制位是0-9、a-f和A-F。八进制位是0-7。

指定 ASCII 范围（0-127）之外的值的数字字符项转义的含义取决于数据库编码。 当编码是UTF-8 时，转义值等价于 Unicode 代码点，例如 \\u1234表示字符U+1234。对于其他多字节编码， 字符项转义通常只是指定该字符的字节值的串接。如果该转义值不对应数据库编码中的任何合法字符，将不会发生错误，但是它不会匹配任何数据。

字符项逃逸总是被当作普通字符。例如，\\135是 ASCII 中的\]， 但\\135并不终止一个方括号表达式。

| **逃逸** | **描述** |
| --- | --- |
| \\d | \[\[:digit:\]\] |
| \\s | \[\[:space:\]\] |
| \\w | \[\[:alnum:\]\_\]（注意下划线是被包括的） |
| \\D | \[^\[:digit:\]\] |
| \\S | \[^\[:space:\]\] |
| \\W | \[^\[:alnum:\]\_\] （注意下划线是被包括的） |

: 表 8.20 正则表达式类缩写逃逸

在方括号表达式里，\\d、\\s和\\w会失去它们的外层方括号，而\\D、\\S和 \\W是非法的（也就是说，例如\[a-c\\d\]等效于\[a-c\[:digit:\]\]。同样\[a-c\\D\]等效于 \[a-c^\[:digit:\]\]的，也是非法的）。

| **逃逸** | **描述** |
| --- | --- |
| \\A | 只在串开头匹配（与^的不同请参 见第 9.7.3.5 节） |
| \\m | 只在一个词的开头匹配 |
| \\M | 只在一个词的末尾匹配 |
| \\y | 只在一个词的开头或末尾匹配 |
| \\Y | 只在一个词的不是开头或末尾的点上匹配 |
| \\Z | 只在串的末尾匹配（与$的不同请参 见第 8.7.3.5 节） |

: 表 8.21 正则表达式约束逃逸

一个词被定义成在上面\[\[:<:\]\]和\[\[:>:\]\]中的声明。在方括号表达式里，约束逃逸是非法的。

| **逃逸** | **描述** |
| --- | --- |
| \\m | （其中m是一个非零位）一个到第m个子表达式的后引用 |
| \\mnn | （其中m是一个非零位，并且nn是一些更多的位，并且十六进制值mnn不超过目前能看到的封闭捕获圆括号的数目）一个到第mnn个子表达式的后引用 |

: 表 8.22 正则表达式后引用

| **注意：** |
| --- |
| 在八进制字符项逃逸和后引用之间有一个历史继承的歧义存在，这个歧义是通过下面的启发式规则解决的，像上面描述地那样。前导零总是表示这是一个八进制逃逸。 而单个非零数字，如果没有跟着任何其它位，那么总是被认为后引用。 一个多位的非零开头的序列也被认为是后引用，只要它出现在合适的子表达式后面 （也就是说，在后引用的合法范围中的数），否则就被认为是一个八进制。 |

| **注意：** |
| --- |
| 在八进制字符项逃逸和后引用之间有一个历史继承的歧义存在，这个歧义是通过下面的启发式规则解决的，像上面描述地那样。前导零总是表示这是一个八进制逃逸。 而单个非零数字，如果没有跟着任何其它位，那么总是被认为后引用。 一个多位的非零开头的序列也被认为是后引用，只要它出现在合适的子表达式后面 （也就是说，在后引用的合法范围中的数），否则就被认为是一个八进制。 |

#### 正则表达式元语法

除了上面描述的主要语法之外，还有几种特殊形式和杂项语法。

如果一个 RE 以\*\*\*:开头，那么剩下的 RE 都被当作 ARE（这在瀚高数据库中通常是无效的，因为 RE 被假定为 ARE，但是如果 ERE 或 BRE 模式通过flags参数被指定为一个正则表达式函数时，它确实能产生效果）。如果一个 RE 以\*\*\*=开头， 那么剩下的 RE 被当作一个文本串，所有的字符都被认为是一个普通字符。

一个 ARE 可以以嵌入选项开头：一个序列(?xyz)（这里的xyz是一个或多个字母字符）声明影响剩余 RE 的选项。 这些选项覆盖任何前面判断的选项 — 特别地，它们可以覆盖一个正则表达式操作符隐含的大小写敏感的行为，或者覆盖flags参数中的正则表达式函数。可用的选项字母在表8.23中显示。注意这些同样的选项字母也被用在正则表达式函数的flags参数中。

| **选项** | **描述** |
| --- | --- |
| b | RE的剩余部分是一个BRE |
| c | 大小写敏感的匹配（覆盖操作符类型） |
| e | RE的剩余部分是一个ERE |
| i | 大小写不敏感的匹配（见第8.7.3.5 节）（覆盖操作符类型） |
| m | n的历史原因的同义词 |
| n | 新行敏感的匹配（见第8.7.3.5 节 |
| p | 部分新行敏感的匹配（见第8.7.3.5 节） |
| q | RE的剩余部分是一个文字（“quoted”） 串，全部是普通字符 |
| s | 非新行敏感的匹配（默认） |
| t | 紧语法（默认，见下文） |
| w | 逆部分新行敏感（“怪异”）的匹配 （见第 8.7.3.5 节） |
| x | 扩展语法（见下文） |

: 表 8.23 ARE 嵌入选项字母

嵌入选项在)终止序列时发生作用。它们只在 ARE 的开始处起作用 （在任何可能存在的\*\*\*:控制器后面）。

除了通常的（紧）RE 语法（这种情况下所有字符都有效）， 还有一种扩展语法，可以通过声明嵌入的x选项获得。在扩展语法里，RE 中的空白字符被忽略，就像那些在#和其后的新行（或 RE 的末尾）之间的字符一样。这样就允许我们给一个复杂的 RE 分段和注释。不过这个基本规则有三种例外：

• 空白字符或前置了\\的#将被保留

• 方括号表达式里的空白或者#将被保留

• 在多字符符号里面不能出现空白和注释，例如(?:

为了这个目的，空白是空格、制表符、新行和任何属于空白字符类的字符。

最后，在 ARE 里，方括号表达式外面，序列(?#ttt)（其中ttt是任意不包含一个))的文本）是一个注释， 它被完全忽略。同样，这样的东西是不允许出现在多字符符号的字符中间的，例如 (?:。这种注释更像是一种历史产物而不是一种有用的设施，并且它们的使用已经被废弃 ；请使用扩展语法来替代。

如果声明了一个初始的\*\*\*=控制器，那么所有这些元语法扩展都不能使用，因为这样表示把用户输入当作一个文字串而不是 RE 对待。

#### 正则表达式匹配规则

在 RE 可以在给定串中匹配多于一个子串的情况下， RE 匹配串中最靠前的那个子串。如果 RE 可以匹配在那个位置开始 的多个子串，要么是取最长的子串，要么是最短的，具体哪种， 取决于 RE 是贪婪的还是非贪婪的。

一个 RE 是否贪婪取决于下面规则：

• 大多数原子以及所有约束，都没有贪婪属性（因为它们毕竟无法匹配个数变化的文本）。

• 在一个 RE 周围加上圆括号并不会改变其贪婪性。

• 带一个固定重复次数量词 （{m}或者{m}?） 的量化原子和原子自身具有同样的贪婪性（可能是没有）。

• 一个带其他普通的量词（包括{m,n}中m等于n的情况）的量化原子是贪婪的（首选最长匹配）。

• 一个带非贪婪量词（包括{m,n}?中m等于 n的情况）的量化原子是非贪婪的（首选最短匹配）。

• 一个分支 — 也就是说，一个没有顶级|操作符的 RE — 和它里面的第一个有贪婪属性的量化原子有着同样的贪婪性。

• 一个由|操作符连接起来的两个或者更多分支组成的 RE 总是贪婪的。

上面的规则所描述的贪婪属性不仅仅适用于独立的量化原子， 而且也适用于包含量化原子的分支和整个 RE。这里的意思是， 匹配是按照分支或者整个 RE 作为一个整体匹配最长或者最短的可能子串。 一旦整个匹配的长度确定，那么匹配任意特定子表达式的部分就基于该子表达式的贪婪属性进行判断，在 RE 里面靠前的子表达式的优先级高于靠后的子表达式。

一个相应的例子：

SELECT SUBSTRING('XY1234Z', 'Y\*(\[0-9\]{1,3})');

结果：123

SELECT SUBSTRING('XY1234Z', 'Y\*?(\[0-9\]{1,3})');

结果：1

在第一个例子里，RE 作为整体是贪婪的，因为Y\*是贪婪的。它可以匹配从Y开始的东西，并且它匹配从这个位置开始的最长的串， 也就是，Y123。输出是这里的圆括号包围的部分，或者说是123。在第二个例子里， RE 总体上是一个非贪婪的 RE，因为Y\*?是非贪婪的。它可以匹配从Y开始的最短的子串，也就是说Y1。子表达式\[0-9\]{1,3}是贪婪的，但是它不能修改总体匹配长度的决定； 因此它被迫只匹配1。

简而言之，如果一个 RE 同时包含贪婪和非贪婪的子表达式，那么总的匹配长度要么是尽可能长，要么是尽可能短，这取决于给整个 RE 赋予的属性。给子表达式赋予的属性只影响在这个匹配里，各个子表达式之间相互允许”吃掉”的多少。

量词{1,1}和{1,1}?可以分别用于在一个子表达式或者整个 RE 上强制贪婪或者非贪婪。当需要整个 RE 具有不同于从其元素中推导出的贪婪属性时，这很有用。例如，假设我们尝试将一个包含一些数字的 字符串分隔成数字以及在它们之前和之后的部分，我们可能会尝试这样做：

SELECT regexp\_matches('abc01234xyz', '(.\*)(\\d+)(.\*)');

Result: {abc0123,4,xyz}

这不会有用：第一个.\*是贪婪的，因此它会”吃掉” 尽可能多的字符而留下\\d+去匹配在最后一个可能位置上的最后一个数字。我们可能会通过让它变成非贪婪来修复：

SELECT regexp\_matches('abc01234xyz', '(.\*?)(\\d+)(.\*)');

Result: {abc,0,""}

这也不会有用：因为现在 RE 作为整体来说是非贪婪的，因此它会尽快结束全部的匹配。我们可以通过强制 RE 整体是贪婪的来得到我们想要的：

SELECT regexp\_matches('abc01234xyz', '(?:(.\*?)(\\d+)(.\*)){1,1}');

Result: {abc,01234,xyz}

独立于 RE 的组件的贪婪性之外控制 RE 的整体贪婪性为处理变长模式提供了很大的灵活性。

在决定更长或者更短的匹配时，匹配长度是以字符衡量的，而不是排序元素。一个空串会被认为比什么都不匹配长。例如：bb\*匹配abbbc的中间三个字符；(week|wee)(night| knights)匹配weeknights的所有十个字符； 而(.\*).\*匹配 abc的时候，圆括号包围的子表达式匹配所有三个字符；当(a\*)\*被拿来匹配bc时，整个 RE 和圆括号子表达式都匹配一个空串。

如果声明了大小写无关的匹配，那么效果就好像所有大小写区别在字母表中消失了。如果在多个情况中一个字母以一个普通字符的形式出现在方括号表达式外面，那么它实际上被转换成 一个包含大小写的方括号表达式，也就是说，x 变成 \[xX\]。 如果它出现在一个方括号表达式里面，那么它的所有大小写的同族都被加入方括号表达式中，也就是说，x变成\[xX\]。

当它出现在一个方括号表达式内时，它的所有大小写副本都被加入到方括号表达式中，例如， \[x\]会变成\[xX\]，而\[^x\]会变成\[^xX\]。

如果指定了新行敏感的匹配，.和使用^的方括号表达式 将永远不会匹配新行字符（这样，匹配就绝对不会跨越新行，除非 RE 显式地安排了这样的情况）并且^和$除了分别匹配串开头和结尾之外，还将分别匹配新行后面和前面的空串。但是 ARE 逃逸\\A和\\Z仍然只匹配串的开头和结尾。

如果指定了部分新行敏感的匹配，那么它影响.和方括号表达式，这个时候和新行敏感的匹配一样，但是不影响^和$。

如果指定了逆新行敏感匹配，那么它影响^和$，其作用和在新行敏感的匹配里一样，但是不影响.和方括号表达式。这个并不是很有用，只是为了满足对称性而提供的。

#### 限制和兼容性

在这个实现里，对 RE 的长度没有特别的限制。但是，那些希望高移植性的程序应该避免使用长度超过 256 字节的 RE，因为 POSIX 兼容 的实现可以拒绝接受这样的 RE。

ARE 实际上和 POSIX ERE 不兼容的唯一的特性是在方括号表达式里\\并不失去它特殊的含义。所有其它 ARE 特性都使用在 POSIX ERE 里面是非法或者是未定义、未声明效果的语法；

指示器的\*\*\*就是在 POSIX 的 BRE 和 ERE 之外的语法。

许多 ARE 扩展都是从 Perl 那里借来的（但是有些被做了修改来清理它们），以及一些 Perl 里没有出现的扩展。要注意的不兼容性包括\\b、\\B、对结尾的新行缺乏特别的处理、对那些被新行敏感匹配的东西附加的补齐方括号表达式、在 lookahead/lookbehind 约束里对圆括号和后引用的限制以及最长/最短匹配（而不是第一匹配）的语义。

#### 基本正则表达式

BRE 在几个方面和 ERE 不太一样。在 BRE 中，|、+和?都是普通字符并且没有与它们功能等价的东西。范围的定界符是\\{和\\}， 因为 {和}本身是普通字符。嵌套的子表达式的圆括号是\\(和\\)，因为(和)自身是普通字符。除非在 RE 开头或者是圆括号子表达式开头，^都是一个普通字符。 除非在 RE 结尾或者是圆括号子表达式的结尾，$是一个普通字符。如果\*出现在 RE 开头或者是圆括号封装的子表达式开头 （前面可能有^），那么它是个普通字符。最后，可以用单数字的后引用，\\<和\\>分别是\[\[:<:\]\]和\[\[:>:\]\]的同义词；在 BRE 中没有其它可用的逃逸。

#### 与XQuery的区别 (LIKE\_REGEX)

从SQL:2008开始，SQL标准中包含了一个LIKE\_REGEX操作符，它根据XQuery正则表达式标准执行模式匹配。 瀚高数据库还没有实现这个操作符，但是你可以使用regexp\_match()函数获得非常类似的行为，因为XQuery正则表达式非常接近于上面描述的ARE语法。

与现有的基于POSIX的 正则表达式功能和XQuery正则表达式包括。

• 不支持XQuery字符类减法。 这个功能的一个例子是使用下面的例子，只匹配英文辅音。\[a-z-\[aeiou\]\]。

• XQuery字符类速记c。 不支持C、i和I。

• 不支持使用p{UnicodeProperty}或反过来的P{UnicodeProperty}的XQuery字符类元素。

• POSIX根据当前的locale来解释字符类，如/w (见表 9.20)(你可以通过在操作符或函数中附加一个COLLATE子句来控制)。 XQuery通过引用Unicode字符属性来指定这些类，因此只有遵循Unicode规则的locale才能获得等效的行为。

• SQL标准（而不是XQuery本身）试图满足更多的需求。”newline的变体”比POSIX的变体。 上面描述的对新行敏感的匹配选项只考虑ASCII NL (n)是新行，但SQL会让我们把CR (r)、CRLF (r/n)，以及一些Unicode唯一的字符，如LINE SEPARATOR (U+2028)也视为新行。值得注意的是，.和s应该算作一个字符，而不是按照 SQL的规定算作两个字符。

• 在表 9.19中描述的字符输入转义中，XQuery只支持n、r和t。

• XQuery不支持\[::name:\]\]语法，不支持括号表达式中的字符类。

• XQuery没有 lookahead 或 lookbehind 约束，也没有任何在 表 8.21.

• 第 9.7.3.4 节中描述的metasyntax形式在XQuery中不存在。

• 由XQuery定义的正则表达式标志字母与POSIX的选项字母相关，但不一样。 表 8.23）。

虽然i和q选项的行为是一样的，但其他的选项却不一样。

• XQuery的s（允许点匹配换行）和m（允许^和$在换行处匹配）标志提供了与POSIX的n相同的行为。p和w标志，但它们与POSIX的s和m标志的行为不匹配。特别要注意的是，点匹配-newline是POSIX中的默认行为，但不是XQuery。

• XQuery的x（忽略模式中的空格）标志与POSIX的扩展模式标志明显不同。 POSIX的x标

## 数据类型格式化函数

瀚高数据库格式化函数提供一套强大的工具用于把各种数据类型 （日期/时间、整数、浮点、数字） 转换成格式化的字符串以及反过来从格式化的字符串转换成指定的数据类型。表8.24列出了这些函数。这些函数都遵循一个公共的调用规范： 第一个参数是待格式化的值，而第二个是一个定义输出或输入格式的模板。

| **函数** | **返回类型** | **描述** | **例子** |
| --- | --- | --- | --- |
| to\_char(timestamp, text) | text | 把时间戳转成字符串 | to\_char(current\_timestamp, ‘HH12:MI:SS’) |
| to\_char(interval, text) |  | 把间隔转成字符串 | to\_char(interval ‘15h 2m 12s’, ‘HH24:MI:SS’) |
| to\_char(int, text) |  | 把整数转成字符串 | to\_char(125, ‘999’) |
| to\_char(double precision, text) |  | 把实数或双精度转成字符串 | to\_char(125.8::real, ‘999D9’) |
| to\_char(numeric, text) |  | 把数字转成字符串 | to\_char(-125.8, ‘999D99S’) |
| to\_date(text,text) | date | 把字符串转成日期 | to\_date(‘05 Dec 2000’, ‘DD Mon YYYY’) |
| to\_number(text, text) | numeric | 把字符串转成数字 | to\_number(‘12,454.8-‘, ‘99G999D9S’) |
| to\_timestamp(text, text) | timestamp with time zone | 把字符串转成时间戳 | to\_timestamp(‘05 Dec 2000’, ‘DD Mon YYYY’) |

: 表 8.24 格式化函数

| 注意： |
| --- |
| 还有一个单一参数的to\_timestamp函数，请见表 8.31 。 |

| 提示： |
| --- |
| to\_timestamp和to\_date存在的目的是为了处理无法用简单造型转换的输入格式。对于大部分标准的日期/时间格式，简单地把源字符串造型成所需的数据类型是可以的，并且简单很多。类似地，对于标准的数字表示形式，to\_number也是没有必要的。 |

在一个to\_char输出模板串中，一些特定的模式可以被识别并且被替换成基于给定值的被恰当地格式化的数据。任何不属于模板模式的文本都简单地照字面拷贝。同样，在一个输入模板串里（对其他函数），模板模式标识由输入数据串提供的值。如果在模板字符串中有不是模板模式的字符，输入数据字符串中的对应字符会被简单地跳过（不管它们是否等于模板字符串字符）。

表 8.25展示了可以用于格式化日期和时间值的模版。

| **模式** | **描述** |
| --- | --- |
| HH | 一天中的小时 （01-12） |
| HH12 | 一天中的小时 （01-12） |
| HH24 | 一天中的小时 （00-23） |
| MI | 分钟 （00-59）minute (00-59) |
| SS | 秒（00-59） |
| MS | 毫秒（000-999） |
| US | 微秒（000000-999999） |
| SSSS | 午夜后的秒（0-86399） |
| AM, am, PM or pm | 正午指示器（不带句号） |
| A.M., a.m., P.M. or p.m. | 正午指示器（带句号） |
| Y,YYY | 带逗号的年（4 位或者更多位） |
| YYYY | 年（4 位或者更多位） |
| YYY | 年的后三位 |
| YY | 年的后两位 |
| Y | 年的最后一位 |
| IYYY | ISO 8601 周编号方式的年（4 位或更多位） |
| IYY | ISO 8601 周编号方式的年的最后 3 位 |
| IY | ISO 8601 周编号方式的年的最后 2 位 |
| I | ISO 8601 周编号方式的年的最后一位 |
| BC, bc, AD或者ad | 纪元指示器（不带句号） |
| B.C., b.c., A.D.或者a.d. | 纪元指示器（带句号） |
| MONTH | 全大写形式的月名（空格补齐到 9 字符） |
| Month | 全首字母大写形式的月名（空格补齐到 9 字 符） |
| month | 全小写形式的月名（空格补齐到 9 字符） |
| MON | 简写的大写形式的月名（英文 3 字符，本地 化长度可变） |
| Mon | 简写的首字母大写形式的月名（英文 3 字 符，本地化长度可变） |
| mon | 简写的小写形式的月名（英文 3 字符，本地 化长度可变） |
| MM | 月编号（01-12） |
| DAY | 全大写形式的日名（空格补齐到 9 字符） |
| Day | 全首字母大写形式的日名（空格补齐到 9 字 符） |
| day | 全小写形式的日名（空格补齐到 9 字符） |
| DY | 简写的大写形式的日名（英语 3 字符，本地 化长度可变） |
| Dy | 简写的首字母大写形式的日名（英语 3 字 符，本地化长度可变） |
| dy | 简写的小写形式的日名（英语 3 字符，本地 化长度可变） |
| DDD | 一年中的日（001-366） |
| IDDD | ISO 8601 周编号方式的年中的日（001-371，年的第 1 日时第一个 ISO 周的周一） |
| DD | 月中的日（01-31） |
| D | 周中的日，周日（1）到周六（7） |
| ID | 周中的 ISO 8601 日，周一（1）到周日（7） |
| W | 月中的周（1-5）（第一周从该月的第一天开 始） |
| WW | 年中的周数（1-53）（第一周从该年的第一 天开始） |
| IW | ISO 8601 周编号方式的年中的周数（01 - 53；新的一年的第一个周四在第一周） |
| CC | 世纪（2 位数）（21 世纪开始于 2001-01-01） |
| J | 儒略日（从午夜 UTC 的公元前 4714 年 11 月 24 日开始的整数日数） |
| Q | 季度（to\_date和to\_timestamp会忽略） |
| RM | 大写形式的罗马计数法的月（I-XII；I 是 一月） |
| rm | 小写形式的罗马计数法的月（i-xii；i 是 一月） |
| TZ | 大写形式的时区缩写（仅在to\_char中支持） |
| tz | 小写形式的时区缩写（仅在to\_char中支持） |
| TZH | 时区的小时 |
| TZM | 时区的分钟 |
| OF | 从UTC开始的时区偏移（仅在to\_char中支 持） |

: 表 8.25 用于日期/时间格式化的模板模式

修饰语可以被应用于模板模式来修改它们的行为。例如，FMMonth就是带着FM修饰语的Month模式。表8.26展示了可用于日期/时间格式化的修饰语模式。

| **修饰语** | **描述** | **例子** |
| --- | --- | --- |
| FM prefix | 填充模式（抑制前导零和填 充的空格） | FMMonth |
| TH suffix | 大写形式的序数后缀 | DDTH, e.g., 12TH |
| th suffix | 小写形式的序数后缀 | DDth, e.g., 12th |
| FX prefix | 固定的格式化全局选项（见 使用须知） | FX Month DD Day |
| TM prefix | 翻译模式（基于lc\_time打印本地化的日和月名） | TMMonth |
| SP suffix | 拼写模式（未实现） | DDSP |

: 表 8.26 用于日期/时间格式化的模板模式修饰语

日期/时间格式化的使用须知：

• FM抑制前导的零或尾随的空白， 否则会把它们增加到输入从而把一个模式的输出变成固定宽度。在瀚高数据库中，FM只修改下一个声明，而在 Oracle 中，FM影响所有随后的声明，并且重复的FM修饰语将触发填充模式开和关。

• TM不包括结尾空白。to\_timestamp和to\_date会忽略TM修饰语。

• to\_timestamp和to\_date跳过了输入字符串开头和日期和时间值周围的多个空格，除非使用了FX选项。 例如，to\_to\_timestamp(' 2000 JUN', 'YYYMON')和to\_timestamp('2000 - JUN', 'YYY-MON')都能工作，但to\_timestamp('2000 JUN', 'FXYYYY-MON') 返回一个错误，因为to\_timestamp只期望一个空格。FX必须指定为模板中的第一个项目。

• to\_timestamp和to\_date的模板字符串中的分隔符（一个空格或非字母/非数字字符）与输入字符串中的任何一个分隔符相匹配，或者被跳过，除非使用了FX选项。例如，to\_to\_timestamp('2000JUN', 'YYY///MON')和to\_timestamp('2000/JUN', 'YYY/ MON')可以工作，但to\_timestamp('2000/JUN', 'YYYY/MON')返回一个错误，因为输入字符串中的分隔符数量超过了模板中的分隔符数量。

如果指定了FX，模板字符串中的分隔符正好与输入字符串中的一个字符匹配。 但要注意的是，输入字符串中的字符不需要与模板字符串中的分隔符相同。例如，to\_timestamp('2000/JUN', 'FXYYYY MON')可以工作，但是to\_timestamp('2000/JUN', 'FXYYYY MON')返回错误，因为模板字符串中的第二个空格会消耗掉输入字符串中的字母J。

• TZH模板模式可以匹配一个有符号的数字。如果没有FX选项，减号可能是模糊的，可能被解释为分隔符。这种模棱两可的问题可以通过以下方式解决。 如果模板字符串中TZH前的分隔符的数量小于输入字符串中减号前的分隔符数量，则减号被解释为TZH的一部分。否则，减号被认为是值之间的分隔符。例如，to\_timestamp(''2000 -10', 'YYY TZH')与-10匹配，但to\_timestamp('2000 -10', 'YYYY TZH')匹配10到TZH。

• 在to\_char模板里可以有普通文本，并且它们会被照字面输出。你可以把一个子串放到双引号里强迫它被解释成一个文本，即使它里面包含模板模式也如此。例如，在'"Hello Year "YYYY'中，YYYY将被年份数据代替，但是Year中单独的Y不会。

在to\_date、to\_number以及to\_timestamp中，文本和双引号字符串会导致跳过该字符串中所包含的字符数量，例如"XX"会跳过两个输入字符（不管它们是不是XX）。

| 提示： |
| --- |
| 在瀚高安全版数据库4.5之前，可以使用非字母或非数字字符跳过输入字符串中的任意文本。例如，to\_timestamp('2000y6m1d', 'yyyyy-MM-DD')以前是有效的。 现在，你只能使用字母字符来实现这个目的。 例如，to\_timestamp(''2000y6m1d', 'yyyytMMtDDt')和to\_timestamp('2000y6m1d', 'yyyyy"y"MM"m"DD"d"')跳过y、m和d。 |

• 如果你想在输出里有双引号，那么你必须在它们前面放反斜线，例如 '\\"YYYY Month\\"'。

不然，在双引号字符串外面的反斜线就不是特殊的。在双引号字符串内，反斜线会导致下一个字符被取其字面形式，不管它是什么字符（但是这没有特殊效果，除非下一个字符是一个双引号或者另一个反斜线）。

• 在to\_timestamp和to\_date中，如果年份格式声明少于四位（如YYY）并且提供的年份少于四位，年份将被调整为最接近于 2020 年，例如95会变成 1995。

• 在to\_timestamp和to\_date中，在处理超过4位数的年份时，YYYY转换具有限制。你必须在YYYY后面使用一些非数字字符或者模板， 否则年份总是被解释为 4 位数字。例如（对于 20000 年）：to\_date('200001131', 'YYYYMMDD')将会被解释成一个 4 位数字的年份，而不是在年份后使用一个非数字分隔符，像to\_date('20000-1131', 'YYYY MMDD')或to\_date('20000Nov31', 'YYYYMonDD')。

• 在to\_timestamp和to\_date中，CC（世纪）字段会被接受，但是如果有YYY、YYYY或者Y,YYY字段则会忽略它。如果CC与YY或Y一起使用，则结果被计算为指定世纪中的那一年。如果指定了世纪但是没有指定年，则会假定为该世纪的第一年。

• 在to\_timestamp和to\_date中，工作日名称或编号（DAY、D以及相关的字段类型）会被接受，但会为了计算结果的目的而忽略。季度（Q）字段也是一样。

• 在to\_timestamp和to\_date中，一个 ISO 8601 周编号的日期（与一个格里高利日期相区别）可以用两种方法之一被指定为to\_timestamp和to\_date：

• 年、周编号和工作日：例如to\_date('2006-42-4', 'IYYY-IW-ID')返回日期2006-10-19。如果你忽略工作日，它被假定为 1（周一）。

• 年和一年中的日：例如to\_date('2006-291', 'IYYY-IDDD')也返回2006-10-19。

尝试使用一个混合了 ISO 8601 周编号和格里高利日期的域来输入一个日期是无意义的，并且将导致一个错误。在一个 ISO 周编号的年的环境下，一个”月”或”月中的日”的概念没有意义。在一个格里高利年的环境下，ISO 周没有意义。用户应当避免混合格里高利。

| **注意：** |
| --- |
| 虽然to\_date将会拒绝混合使用格里高利和 ISO 周编号日期的域， to\_char却不会，因为YYYY-MM-DD (IYYY-IDDD) 这种输出格式也会有用。但是避免写类似IYYY-MM-DD的东西，那会得到在 起始年附近令人惊讶的结果（详见第 8.9.1 节）。 |

• 在to\_timestamp中，毫秒（MS）和微秒（US）域都被用作小数点后的秒位。例如to\_timestamp('12.3', 'SS.MS')不是 3 毫秒, 而是 300，因为该转换把它看做 12+ 0.3 秒。这意味着对于格式SS.MS而言，输入值12.3、12.30和12.300指定了相同数目的毫秒。要得到三毫秒，你必须使用 12.003，转换会把它看做 12 + 0.003 = 12.003 秒。

下面是一个更复杂的例子∶to\_timestamp('15:12:02.020.001230',

'HH24:MI:SS.MS.US')是 15 小时、12 分钟和 2 秒 + 20 毫秒 + 1230微秒 = 2.021230 秒。

• to\_char(..., 'ID')的一周中日的编号匹配extract(isodow from...)函数，但是to\_char(..., 'D')不匹配extract(dow from...)的日编号。

• to\_char(interval)格式化HH和HH12为显示在一个 12 小时的时钟上，即零小时和 36 小时输出为12，而HH24会输出完整的小时值，对于间隔它可以超过 23.

表 8.27展示了可以用于格式化数字值的模版模式。

| **模式** | **描述** |
| --- | --- |
| 9 | 数位（如果无意义可以被删除） |
| 0 | 数位（即便没有意义也不会被删除） |
| . (period) | 小数点 |
| , (comma) | 分组（千）分隔符 |
| PR | 尖括号内的负值 |
| S | 带符号的数字（使用区域） |
| L | 货币符号（使用区域） |
| D | 小数点（使用区域） |
| G | 分组分隔符（使用区域） |
| MI | 在指定位置的负号（如果数字 < 0） |
| PL | 在指定位置的正号（如果数字 > 0） |
| SG | 在指定位置的正/负号 |
| RN | 罗马数字（输入在 1 和 3999 之间） |
| TH or th | 序数后缀 |
| V | 移动指定位数（参阅注解） |
| EEEE | 科学记数的指数 |

: 表 8.27 用于数字格式化的模板模式

数字格式化的用法须知：

• 0指定一个总是被打印的数位，即便它包含前导/拖尾的零。9也指定一个数位，但是如果它是前导零则会被空格替换，而如果是拖尾零并且指定了填充模式则它会被删除（对于to\_number()来说，这两种模式字符等效）。

• 模式字符S、L、D以及G表示当前locale定义的负号、货币符号、小数点以及数字分隔符字符（见lc\_monetary和lc\_numeric）。不管locale是什么，模式字符句号和逗号就表示小数点和数字分隔符。

• 对于to\_char()的模式中的一个负号，如果没有明确的规定，将为该负号保留一列，并且它将被锚接到（出现在左边）那个数字。如果S正好出现在某个9的左边，它也将被锚接到那个数字。

• 使用SG、PL或MI格式化的符号并不挂在数字上面； 例如，to\_char(-12, 'MI9999')生成'- 12'，而to\_char(-12, 'S9999')生成 ' -12'。（Oracle 里的实现不允许在9前面使用MI，而是要求9在MI前面。）

• TH不会转换小于零的数值，也不会转换小数。

• 在to\_number中，如果没有使用L或TH之类的非数据模板模式，相应数量的输入字符会被跳过，不管它们是否匹配模板模式，除非它们是数据字符（也就是数位、负号、小数点或者逗号）。例如，TH会跳过两个非数据字符。

• 带有to\_char的V会把输入值乘上10^n，其中n是跟在V后面的位数。带有to\_number的V以类似的方式做除法。to\_char和to\_number不支持使用结合小数点的V（例如，不允许99.9V99）。

• EEEE（科学记数法）不能和任何其他格式化模式或修饰语（数字和小数点模式除外）组合在一起使用，并且必须位于格式化字符串的最后（例如8.99EEEE是一个合法的模式）。

某些修饰语可以被应用到任何模板来改变其行为。例如，FM99.99是带有FM修饰语的99.99模式。

表 8.28中展示了用于数字格式化模式修饰语。

| **修饰语** | **描述** | **例子** |
| --- | --- | --- |
| FM prefix | 填充模式（抑制拖尾零和填充的空白） | FM99.99 |
| TH suffix | 大写序数后缀 | 999TH |
| th suffix | 小写序数后缀 | 999th |

: 表 8.28 用于数字格式化的模板模式修饰语

表 8.29展示了一些使用to\_char函数的例子。

| **表达式** | **结果** |
| --- | --- |
| to\_char(current\_timestamp, ‘Day, DD HH12:MI:SS’) | ‘Tuesday, 06 05:39:18’ |
| to\_char(current\_timestamp, ‘FMDay, FMDD HH12:MI:SS’) | ‘Tuesday, 6 05:39:18’ |
| to\_char(-0.1, ‘99.99’) | ‘ -.10’ |
| to\_char(-0.1, ‘FM9.99’) | ‘-.1’ |
| to\_char(-0.1, ‘FM90.99’) | ‘-0.1’ |
| to\_char(0.1, ‘0.9’) | ‘ 0.1’ |
| to\_char(12, ‘9990999.9’) | ‘ 0012.0’ |
| to\_char(12, ‘FM9990999.9’) | ‘0012.’ |
| to\_char(485, ‘999’) | ‘ 485’ |
| to\_char(-485, ‘999’) | ‘-485’ |
| to\_char(485, ‘9 9 9’) | ‘ 4 8 5’ |
| to\_char(1485, ‘9,999’) | ‘ 1,485’ |
| to\_char(1485, ‘9G999’) | ‘ 1 485’ |
| to\_char(148.5, ‘999.999’) | ‘ 148.500’ |
| to\_char(148.5, ‘FM999.999’) | ‘148.5’ |
| to\_char(148.5, ‘FM999.990’) | ‘148.500’ |
| to\_char(148.5, ‘999D999’) | ‘ 148,500’ |
| to\_char(3148.5, ‘9G999D999’) | ‘ 3 148,500’ |
| to\_char(-485, ‘999S’) | ‘485-‘ |
| to\_char(-485, ‘999MI’) | ‘485-‘ |
| to\_char(485, ‘999MI’) | ‘485 ‘ |
| to\_char(485, ‘FM999MI’) | ‘485’ |
| to\_char(485, ‘PL999’) | ‘+485’ |
| to\_char(485, ‘SG999’) | ‘+485’ |
| to\_char(-485, ‘SG999’) | ‘-485’ |
| to\_char(-485, ‘9SG99’) | ‘4-85’ |
| to\_char(-485, ‘999PR’) | ‘<485>’ |
| to\_char(485, ‘L999’) | ‘DM 485’ |
| to\_char(485, ‘RN’) | ‘ CDLXXXV’ |
| to\_char(485, ‘FMRN’) | ‘CDLXXXV’ |
| to\_char(5.2, ‘FMRN’) | ‘V’ |
| to\_char(482, ‘999th’) | ‘ 482nd’ |
| to\_char(485, ‘“Good number:”999’) | ‘Good number: 485’ |
| to\_char(485.8, ‘“Pre:”999” Post:”.999’) | Pre: 485 Post:.800’ |
| to\_char(12, ‘99V999’) | ‘ 12000’ |
| to\_char(12.4, ‘99V999’) | ‘ 12400’ |
| to\_char(12.45, ‘99V9’) | ‘ 125’ |
| to\_char(0.0004859, ‘9.99EEEE’) | ‘ 4.86e-04’ |

| **表达式** | **结果** |
| --- | --- |
| to\_char(current\_timestamp, ‘Day, DD HH12:MI:SS’) | ‘Tuesday, 06 05:39:18’ |
| to\_char(current\_timestamp, ‘FMDay, FMDD HH12:MI:SS’) | ‘Tuesday, 6 05:39:18’ |
| to\_char(-0.1, ‘99.99’) | ‘ -.10’ |
| to\_char(-0.1, ‘FM9.99’) | ‘-.1’ |
| to\_char(-0.1, ‘FM90.99’) | ‘-0.1’ |
| to\_char(0.1, ‘0.9’) | ‘ 0.1’ |
| to\_char(12, ‘9990999.9’) | ‘ 0012.0’ |
| to\_char(12, ‘FM9990999.9’) | ‘0012.’ |
| to\_char(485, ‘999’) | ‘ 485’ |
| to\_char(-485, ‘999’) | ‘-485’ |
| to\_char(485, ‘9 9 9’) | ‘ 4 8 5’ |
| to\_char(1485, ‘9,999’) | ‘ 1,485’ |
| to\_char(1485, ‘9G999’) | ‘ 1 485’ |
| to\_char(148.5, ‘999.999’) | ‘ 148.500’ |
| to\_char(148.5, ‘FM999.999’) | ‘148.5’ |
| to\_char(148.5, ‘FM999.990’) | ‘148.500’ |
| to\_char(148.5, ‘999D999’) | ‘ 148,500’ |
| to\_char(3148.5, ‘9G999D999’) | ‘ 3 148,500’ |
| to\_char(-485, ‘999S’) | ‘485-‘ |
| to\_char(-485, ‘999MI’) | ‘485-‘ |
| to\_char(485, ‘999MI’) | ‘485 ‘ |
| to\_char(485, ‘FM999MI’) | ‘485’ |
| to\_char(485, ‘PL999’) | ‘+485’ |
| to\_char(485, ‘SG999’) | ‘+485’ |
| to\_char(-485, ‘SG999’) | ‘-485’ |
| to\_char(-485, ‘9SG99’) | ‘4-85’ |
| to\_char(-485, ‘999PR’) | ‘<485>’ |
| to\_char(485, ‘L999’) | ‘DM 485’ |
| to\_char(485, ‘RN’) | ‘ CDLXXXV’ |
| to\_char(485, ‘FMRN’) | ‘CDLXXXV’ |
| to\_char(5.2, ‘FMRN’) | ‘V’ |
| to\_char(482, ‘999th’) | ‘ 482nd’ |
| to\_char(485, ‘“Good number:”999’) | ‘Good number: 485’ |
| to\_char(485.8, ‘“Pre:”999” Post:”.999’) | Pre: 485 Post:.800’ |
| to\_char(12, ‘99V999’) | ‘ 12000’ |
| to\_char(12.4, ‘99V999’) | ‘ 12400’ |
| to\_char(12.45, ‘99V9’) | ‘ 125’ |
| to\_char(0.0004859, ‘9.99EEEE’) | ‘ 4.86e-04’ |

: 表 8.29 to\_char例子

## 时间/日期函数和操作符

表 8.31展示了可用于处理日期/时间值的函数，其细节在随后的小节中描述。表 9.30演示了基本算术操作符 （+、\*等）的行为。

所有下文描述的接受time或timestamp输入的函数和操作符实际上都有两种变体： 一种接收time with time zone或timestamp with time zone， 另外一种接受time without time zone或者 timestamp without time zone。为了简化，这些变种没有被独立地展示。此外，+和\*操作符都是可交换的操作符对（例如，date + integer 和 integer + date）；我们只显示其中一个。

| **操作符** | **例子** | **结果** |
| --- | --- | --- |
| + | date ‘2001-09-28’ + integer ‘7’ | date ‘2001-10-05’ |
| + | date ‘2001-09-28’ + interval ‘1 hour’ | timestamp ‘2001-09-28 01:00:00’ |
| + | date ‘2001-09-28’ + time ‘03:00’ | timestamp ‘2001-09-28 03:00:00’ |
| + | interval ‘1 day’ + interval ‘1 hour’ | interval ‘1 day 01:00:00’ |
| + | timestamp ‘2001-09-28 01:00’ + interval ‘23 hours’ | timestamp ‘2001-09-29 00:00:00’ |
| + | time ‘01:00’ + interval ‘3 hours’ | time ‘04:00:00’ |
| \- | \- interval ‘23 hours’ | interval ‘-23:00:00’ |
| \- | date ‘2001-10-01’ - date ‘2001-09-28’ | integer ‘3’ (days) |
| \- | date ‘2001-10-01’ - integer ‘7’ | date ‘2001-09-24’ |
| \- | date ‘2001-09-28’ - interval ‘1 hour’ | timestamp ‘2001-09-27 23:00:00’ |
| \- | time ‘05:00’ - time ‘03:00’ | interval ‘02:00:00’ |
| \- | time ‘05:00’ - interval ‘2 hours’ | time ‘03:00:00’ |
| \- | timestamp ‘2001-09-28 23:00’ - interval ‘23 hours’ | timestamp ‘2001-09-28 00:00:00’ |
| \- | interval ‘1 day’ - interval ‘1 hour’ | interval ‘1 day -01:00:00’ |
| \- | timestamp ‘2001-09-29 03:00’ - timestamp ‘2001-09-27 12:00’ | interval ‘1 day 15:00:00’ |
| \* | 900 \* interval ‘1 second’ | interval ‘00:15:00’ |
| \* | 21 \* interval ‘1 day’ | interval ‘21 days’ |
| \* | double precision ‘3.5’ \* interval ‘1 hour’ | interval ‘03:30:00’ |
| / | interval ‘1 hour’ / double precision ‘1.5’ | interval ‘00:40:00’ |

: 表 8.30 日期/时间操作符

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| age(timestamp, timestamp) | interval | 减去参数，生成 一个使用年、月 （而不是只用 日）的“符号 化”的结果 | age(timestamp ‘2001-04-10’, timestamp ‘1957-06-13’) | 43 年 9 月 27 日 |
| age(timestamp) | interval | 从current\_date（在午夜）减去 | age(timestamp ‘1957-06-13’) | 43 years 8 mons 3 days |
| clock\_timestamp() | timestamp with time zone | 当前日期和时间 （在语句执行期 间变化）； 见第 8.9.4 节 |  |  |
| current\_date | date | 当前日期； 见第8.9.4 节 |  |  |
| current\_time | time with time zone | 当前时间（一天 中的时间）； 见第 8.9.4 节 |  |  |
| current\_timestamp | timestamp with time zone | 当前日期和时间 （当前事务开始 时）； 见第 8.9.4 节 |  |  |
| date\_part(text, timestamp) | double precision | 获得子域（等价 于extract）； 见第 8.9.1 节 | date\_part(‘hour’, timestamp’2001-02-16 20:38:40’) | 20 |
| date\_part(text, interval) | interval) double precision | 获得子域（等价于extract）； 见第 8.9.1 节 | date\_part(‘month’, interval ‘2 years 3 months’) |  |
| date\_trunc(text, timestamp) | timestamp | 截断到指定精 度； 见第 8.9.2 节 | date\_trunc(‘hour’, timestamp ‘2001-02-16 20:38:40’) | 2001-02-16 20:00:00 |
| date\_trunc(text, timestamp with time zone, text) | timestamp with time zone | 在指定的时区截 断到指定的精 度；参见 第 8.9.2 节 | date\_trunc(‘day’, timestamptz ‘2001-02-16 20:38:40+00’, ‘Australia/ Sydney’) | 2001-02-16 13:00:00+00 |
| date\_trunc(text, interval) | interval | 截断到指定精 度； 见第8.9.2 节 | date\_trunc(‘hour’, interval ‘2 days 3 hours 40 minutes’) | 2 days 03:00:00 |
| extract(field from timestamp) | double precision | 获得子域； 见第 8.9.1 节 | extract(hour from timestamp ‘2001-02-16 20:38:40’) | 20 |
| extract(field from interval) | double precision | 获得子域； 见第 8.9.1 节 | extract(month from interval ‘2 years 3 months’) | 3 |
| isfinite(date) | boolean | 测试有限日期 （不是+/-无限） | isfinite(date ‘2001-02-16’) | true |
| isfinite(timestamp) | boolean | 测试有限日期 （不是+/-无限） | isfinite(timestamp ‘2001-02-16 21:28:30’) | true |
| isfinite(interval) | boolean | 测试有限间隔 | isfinite(interval ‘4 hours’) | true |
| justify\_days(interval) | interval | 调整间隔这样30天时间周期可以表示为月 | justify\_days(interval ‘35 days’) | 1 mon 5 days |
| justify\_hours(interval) | interval | 调整间隔这样24小时时间周期可以表示为日 | justify\_hours(interval ‘27 hours’) | 1 day 03:00:00 |
| justify\_interval(interval) | interval | 使用justify\_days和justify\_hours调整间隔，使用额外的符号调整 | justify\_interval | 9 days 23:00:00 |
| localtime | time | 当前时间（一天中的时间）；见第 8.9.4 节 |  |  |
| localtimestamp | timestamp | 当前日期和时间（当前事务的开始）；见第 8.9.4 节 |  |  |
| make\_date(year int, month int, day int) | date | 从年、月、日域创建日期 | make\_date(2013, 7, 15) | 2013-07-15 |
| make\_interval(years int DEFAULT 0, months int DEFAULT 0, weeks int DEFAULT 0, days int DEFAULT 0, hours int DEFAULT 0, mins int DEFAULT 0, secs double precision DEFAULT 0.0) | interval | 从年、月、周、 日、时、分、秒 域创建 interval | make\_interval(days => 10) | 10 days |
| make\_time(hour int, min int, sec double precision) | time | 从时、分、秒域创建时间 | make\_time(8, 15, 23.5) | 08:15:23.5 |
| make\_timestamp(year int, month int, day int, hour int, min int, sec double precision) | timestamp | 从年、月、日、时、分、秒域创建时间戳 | make\_timestamp(2013, 7, 15, 8, 15, 23.5) | 2013-07-15 08:15:23.5 |
| make\_timestamptz(year int, month int, day int, hour int, min int, sec double precision, \[ timezone text\]) | timestamp with | 从年、月、日、时、分、秒域创建带时区的时间戳。如果没有指 定timezone， 则使用当前时区。 | make\_timestamptz(2013, 7, 15, 8, 15, 23.5) | 2013-07-15 08:15:23.5+01 |
| now() | timestamp with time zone | 当前日期和时间（当前事务的开始）； 见第 8.9.4 节 |  |  |
| statement\_timestamp() | timestamp with time zone | 当前日期和时间（当前事务的开始）； 见第 8.9.4 节 |  |  |
| timeofday() | text | 当前日期和时间 （像clock\_timestamp，但是作为一 个text字符串）；见第 8.9.4 节 |  |  |
| transaction\_timestamp() | timestamp with time zone | time zone 当前日期和时间 （当前事务的开 始）； 见第 8.9.4 节 |  |  |
| to\_timestamp(double precision) | timestamp with time zone | 把 Unix 时间 （从 1970-01-01 00:00:00+00 开 始的秒）转换成 timestamp | to\_timestamp(1284352323) | 2010-09-13 04:32:03+00 |

: 表 8.31 日期/时间函数

除了这些函数以外，还支持 SQL 操作符OVERLAPS：

(start1, end1) OVERLAPS (start2, end2)

(start1, length1) OVERLAPS (start2, length2)

这个表达式在两个时间域（用它们的端点定义）重叠的时候得到真，当它们不重叠时得到假。端点可以用一对日期、时间或者时间戳来指定；或者是用一个后面跟着一个间隔的日期、时间或时间戳来指定。当一对值被提供时，起点或终点都可以被写在前面，OVERLAPS会自动地把较早的值作为起点。每一个时间段被认为是表示半开的间隔start <= time

< end，除非start和end相等，这种情况下它表示单个时间实例。例如这表示两个只有一个共同端点的时间段不重叠。

SELECT (DATE '2001-02-16', DATE '2001-12-21') OVERLAPS

(DATE '2001-10-30', DATE '2002-10-30');

结果：true

SELECT (DATE '2001-02-16', INTERVAL '100 days') OVERLAPS

(DATE '2001-10-30', DATE '2002-10-30');

结果：false

SELECT (DATE '2001-10-29', DATE '2001-10-30') OVERLAPS

(DATE '2001-10-30', DATE '2001-10-31');

结果：false

SELECT (DATE '2001-10-30', DATE '2001-10-30') OVERLAPS

(DATE '2001-10-30', DATE '2001-10-31');

结果：true

当把一个interval值添加到timestamp with time zone上（或从中减去）时， days 部分会按照指定的天数增加或减少timestamp with time zone的日期。 对于横跨夏令时的变化（当会话的时区被设置为可识别DST的时区时），这意味着interval '1 day'并 不一定等于interval '24 hours'。例如，当会话的时区设置为CST7CDT时，timestamp with time zone '2005-04-02 12:00-07' + interval '1 day' 的结果是timestamp with time zone '2005-04-03 12:00-06'，而将interval '24 hours'增加到相同的初始timestamp with time zone的结果 则是timestamp with time zone '2005-04-03 13:00-06'， 因为CST7CDT时区在2005-04-03 02:00有一个夏令时变更。

注意age返回的月数域可能有歧义，因为不同的月份有不同的天数。 瀚高数据库的方法是当计算部分月数时，采用两个日期中较早的月。例如：age('2004-06-01', '2004-04-30')使用4月份得到1 mon 1 day，而用5月分时会得到1 mon 2 days，因为5月有31天，而4月只有30天。

日期和时间戳的减法也可能会很复杂。执行减法的一种概念上很简单的方法是，使用 EXTRACT(EPOCH FROM...)把每个值都转换成秒数，然后执行减法， 这样会得到两个值之间的秒数。这种方法将会适应每个月中天数、 时区改变和夏令时调整。使用”-“操作符的日期或时间 戳减法会返回值之间的天数（24小时）以及时/分/秒，也会做同样的调整。 age函数会返回年、月、日以及时/分/秒，执行按域的减法，然后对 负值域进行调整。下面的查询展示了这些方法的不同。例子中的结果由 timezone = 'US/Eastern'产生，这使得两个使用的日期之间存在着夏令时的变化：

SELECT EXTRACT(EPOCH FROM timestamptz '2013-07-01 12:00:00') -

EXTRACT(EPOCH FROM timestamptz '2013-03-01 12:00:00');

Result: 10537200

SELECT (EXTRACT(EPOCH FROM timestamptz '2013-07-01 12:00:00') -

EXTRACT(EPOCH FROM timestamptz '2013-03-01 12:00:00'))

/ 60 / 60 / 24;

Result: 121.958333333333

SELECT timestamptz '2013-07-01 12:00:00' - timestamptz '2013-03-01 12:00:00';

Result: 121 days 23:00:00

SELECT age(timestamptz '2013-07-01 12:00:00', timestamptz '2013-03-01

12:00:00');

Result: 4 mons

### EXTRACT, date\_part

EXTRACT(field FROM source)

extract函数从日期/时间值中抽取子域，例如年或者小时等。source必须是一个类型 timestamp、time或interval的值表达式（类型为date的表达式将被造型为 timestamp，并且因此也可以被同样使用）。field是一个标识符或者字符串，它指定从源值中抽取的域。extract函数返回类型为double precision的值。 下列值是有效的域名字∶

century

世纪

SELECT EXTRACT(CENTURY FROM TIMESTAMP '2000-12-16 12:21:13');

结果：20

SELECT EXTRACT(CENTURY FROM TIMESTAMP '2001-02-16 20:38:40');

结果：21

第一个世纪从 0001-01-01 00:00:00 AD 开始， 尽管那时候人们还不知道这是第一个世纪。这个定义适用于所有使用格里高利历法的国家。其中没有 0 世纪，我们直接从公元前 1 世纪到公元 1 世纪。 如果你认为这个不合理，那么请把抱怨发给：罗马圣彼得教堂，梵蒂冈，教皇收。

day

对于timestamp值，是（月份）里的日域（1-31）；对于interval值，是日数

SELECT EXTRACT(DAY FROM TIMESTAMP '2001-02-16 20:38:40');

结果：16

SELECT EXTRACT(DAY FROM INTERVAL '40 days 1 minute');

结果：40

decade

年份域除以10

SELECT EXTRACT(DECADE FROM TIMESTAMP '2001-02-16 20:38:40');

结果：200

dow

一周中的日，从周日（0）到周六（6）

SELECT EXTRACT(DOW FROM TIMESTAMP '2001-02-16 20:38:40');

结果：5

请注意，extract的一周中的日和to\_char(..., 'D')函数不同。

doy

一年的第几天（1 -365/366）

SELECT EXTRACT(DOY FROM TIMESTAMP '2001-02-16 20:38:40');

结果：47

epoch

对于timestamp with time zone值， 是自 1970-01-01 00:00:00 UTC 以来的秒数（结果可能是负数）； 对于date and timestamp值，是自本地时间 1970-01-01 00:00:00 以来的描述；对于interval值，它是时间间隔的总秒数。

SELECT EXTRACT(EPOCH FROM TIMESTAMP WITH TIME ZONE '2001-02-16

20:38:40.12-08');

结果：982384720.12

SELECT EXTRACT(EPOCH FROM INTERVAL '5 days 3 hours');

结果：442800

不能用to\_timestamp把一个 epoch 值转换回成时间戳：

SELECT to\_timestamp(982384720.12);

Result: 2001-02-17 04:38:40.12+00

hour

小时域（0 - 23）

SELECT EXTRACT(HOUR FROM TIMESTAMP '2001-02-16 20:38:40');

结果：20

isodow

一周中的日，从周一（1）到周日（7）

SELECT EXTRACT(ISODOW FROM TIMESTAMP '2001-02-18 20:38:40');

结果：7

除了周日，这和dow相同。这符合ISO 8601 中一周中的日的编号。

isoyear

日期所落在的ISO 8601 周编号的年（不适用于间隔）

SELECT EXTRACT(ISOYEAR FROM DATE '2006-01-01');

结果：2005

SELECT EXTRACT(ISOYEAR FROM DATE '2006-01-02');

结果：2006

每一个ISO 8601 周编号的年都开始于包含1月4日的那一周的周一，在早的1月或迟的12

月中ISO年可能和格里高利年不同。更多信息见week域。

microseconds

秒域，包括小数部分，乘以 1,000,000。请注意它包括全部的秒

SELECT EXTRACT(MICROSECONDS FROM TIME '17:12:28.5');

结果：28500000

millennium

千年

SELECT EXTRACT(MILLENNIUM FROM TIMESTAMP '2001-02-16 20:38:40');

结果：3

19xx的年份在第二个千年里。第三个千年从 2001 年 1 月 1 日开始。

milliseconds

秒域，包括小数部分，乘以 1000。请注意它包括完整的秒。

SELECT EXTRACT(MILLISECONDS FROM TIME '17:12:28.5');

结果：28500

minute

分钟域（0 - 59）

SELECT EXTRACT(MINUTE FROM TIMESTAMP '2001-02-16 20:38:40');

结果：38

month

对于timestamp值，它是一年里的月份数（1 - 12）； 对于interval值，它是月的数目，然后对 12 取模（0 - 11）

SELECT EXTRACT(MONTH FROM TIMESTAMP '2001-02-16 20:38:40');

结果：2

SELECT EXTRACT(MONTH FROM INTERVAL '2 years 3 months');

结果：3

SELECT EXTRACT(MONTH FROM INTERVAL '2 years 13 months');

结果：1

quarter

该天所在的该年的季度（1 - 4）

SELECT EXTRACT(QUARTER FROM TIMESTAMP '2001-02-16 20:38:40');

结果：1

second

秒域，包括小数部分（0 - 591）

SELECT EXTRACT(SECOND FROM TIMESTAMP '2001-02-16 20:38:40');

结果：40

SELECT EXTRACT(SECOND FROM TIME '17:12:28.5');

结果：28.5

timezone

与 UTC 的时区偏移，以秒记。正数对应 UTC 东边的时区，负数对应 UTC 西边的时区（从技术上来看，瀚高数据库不使用 UTC，因为其中不处理闰秒）。

timezone\_hour

时区偏移的小时部分。

timezone\_minute

时区偏移的分钟部分。

week

该天在所在的ISO 8601 周编号的年份里是第几周。根据定义， 一年的第一周包含该年的 1月 4 日并且 ISO 周从星期一开始。换句话说，一年的第一个星期四在第一周。

在 ISO 周编号系统中，早的 1 月的日期可能位于前一年的第五十二或者第五十三周，而迟的 12 月的日期可能位于下一年的第一周。例如， 2005-01-01位于 2004 年的第五十三周，并且2006-01-01位于 2005 年的第五十二周，而2012-12-31位于 2013 年的第一周。我们推荐把isoyear域和week一起使用来得到一致的结果。

SELECT EXTRACT(WEEK FROM TIMESTAMP '2001-02-16 20:38:40');

结果：7

year

年份域。要记住这里没有0 AD，所以从AD年里抽取BC年应该小心处理。

SELECT EXTRACT(YEAR FROM TIMESTAMP '2001-02-16 20:38:40');

结果：2001

| **注意：** |
| --- |
| 当输入值为 +/-Infinity 时，extract对于单调增的域（epoch、julian、year、isoyear、decade、century以及millennium）返回+/-Infinity。对于其他域返回 NULL。 |

extract函数主要的用途是做计算性处理。对于用于显示的日期/时间值格式化，参阅第 8.8 节。

在传统的Ingres上建模的date\_part函数等价于SQL标准函数extract：

date\_part('field', source)

请注意这里的field参数必须是一个串值，而不是一个名字。有效的date\_part域名和extract相同。

SELECT date\_part('day', TIMESTAMP '2001-02-16 20:38:40');

结果：16

SELECT date\_part('hour', INTERVAL '4 hours 3 minutes');

结果：4

### date\_trunc

date\_trunc函数在概念上和用于数字的trunc函数类似。

date\_trunc(field, source \[, time\_zone \]) source是类型timestamp或interval的值表达式（类型date和time的值都分别被自动转换成timestamp, timestamp with time zone,或者interval）。field选择对输入值选用什么样的精度进行截断。返回的值是timestamp, timestamp with time zone,类型或者所有小于选定的 精度的域都设置为零（或者一，对于日期和月份）的interval。

field的有效值是∶

microseconds

milliseconds

second

minute

hour

day

week

month

quarter

year

decade

century

millennium

当输入值的类型为timestamp with time zone时。截断是针对特定时区进行的。 例如，截断为day，产生的值是是该区域的午夜。默认情况下，截断是在以下方面进行的到当前的TimeZone设置，但在当前的 可以提供可选的time\_zone参数。以指定不同的时区。可以指定时区名称 第 8.5.3 节中描述的任何一种方式。

当处理timestamp without time zone 或interval输入时，不能指定时区。 这些总是按表面值来处理。

示例 (假设当地时区为 America/New\_York):

SELECT date\_trunc('hour', TIMESTAMP '2001-02-16 20:38:40');

结果：2001-02-16 20:00:00

SELECT date\_trunc('year', TIMESTAMP '2001-02-16 20:38:40');

结果：2001-01-01 00:00:00

SELECT date\_trunc('day', TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40+00');

Result: 2001-02-16 00:00:00-05

SELECT date\_trunc('day', TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40+00',

'Australia/Sydney');

Result: 2001-02-16 08:00:00-05

SELECT date\_trunc('hour', INTERVAL '3 days 02:47:33');

Result: 3 days 02:00:00

### AT TIME ZONE

AT TIME ZONE把时间戳without time zone转换成时间戳with time zone或者反过来，并且把time值转换成不同的时区。表8.32展示了它的变体。

| **表达式** | **返回类型** | **描述** |
| --- | --- | --- |
| timestamp without time zone AT TIME ZONE zone | timestamp with time zone | 把给定的不带时区的时间戳 当作位于指定时区的时间对 待 |
| timestamp with time zone AT TIME ZONE zone | timestamp without time zone | 把给定的带时区的时间戳转 换到新的时区，不带时区指 定 |
| time with time zone AT TIME ZONE zone | time with time zone | 把给定的带时区的时间转换 到新时区 |

: 表 8.32 AT TIME ZONE变体

在这些表达式里，我们需要的时区zone可以指定为文本串（例如，'America/Los\_Angeles'）或者一个间隔 （例如，INTERVAL '-08:00'）。 在文本情况下，可用的时区名字可以用第 8.5.3 节中描述的任何方式指定。

例子（假设本地时区是America/Los\_Angeles）：

SELECT TIMESTAMP '2001-02-16 20:38:40' AT TIME ZONE 'America/Denver';

Result: 2001-02-16 19:38:40-08

SELECT TIMESTAMP WITH TIME ZONE '2001-02-16 20:38:40-05' AT TIME ZONE 'America/

Denver';

Result: 2001-02-16 18:38:40

SELECT TIMESTAMP '2001-02-16 20:38:40-05' AT TIME ZONE 'Asia/Tokyo' AT TIME ZONE

'America/Chicago';

Result: 2001-02-16 05:38:40

第一个例子给缺少时区的值加上了时区，并且显示了使用当前TimeZone设置的值。第二个例子把带有时区值的时间戳移动到指定的时区，并且返回不带时区的值。这允许存储和显示不同于当前TimeZone设置的值。第三个例子把东京时间转换成芝加哥时间。把time值转换成其他时区会使用当前活跃的时区规则，因为没有提供日期。

函数timezone(zone, timestamp)等效于 SQL 兼容的结构timestamp AT TIME ZONE zone。

### 当前日期/时间

瀚高数据库提供了许多返回当前日期和时间的函数。这些 SQL 标准的函数全部都按照当前事务的开始时刻返回值：

CURRENT\_DATE

CURRENT\_TIME

CURRENT\_TIMESTAMP

CURRENT\_TIME(precision)

CURRENT\_TIMESTAMP(precision)

LOCALTIME

LOCALTIMESTAMP

LOCALTIME(precision)

LOCALTIMESTAMP(precision)

CURRENT\_TIME和CURRENT\_TIMESTAMP传递带有时区的值；LOCALTIME和LOCALTIMESTAMP传递的值不带时区。

CURRENT\_TIME、CURRENT\_TIMESTAMP、LOCALTIME和 LOCALTIMESTAMP可以有选择地接受一个精度参数， 该精度导致结果的秒域被园整为指定小数位。如果没有精度参数，结果将被给予所能得到的全部精度。

一些例子：

SELECT CURRENT\_TIME;

结果：14:39:53.662522-05

SELECT CURRENT\_DATE;

结果：2001-12-23

SELECT CURRENT\_TIMESTAMP;

结果：2001-12-23 14:39:53.662522-05

SELECT CURRENT\_TIMESTAMP(2);

结果：2001-12-23 14:39:53.66-05

SELECT LOCALTIMESTAMP;

结果：2001-12-23 14:39:53.662522

因为这些函数全部都按照当前事务的开始时刻返回结果，所以它们的值在事务运行的整个期间内都不改变。 我们认为这是一个特性：目的是为了允许一个事务在”当前”时间上有一致的概念， 这样在同一个事务里的多个修改可以保持同样的时间戳。

| 注意： |
| --- |
| 许多其它数据库系统可能会更频繁地推进这些值。 |

瀚高数据库同样也提供了返回当前语句开始时间的函数， 它们会返回函数被调用时的真实当前时间。这些非 SQL 标准的函数列表如下：

transaction\_timestamp()

statement\_timestamp()

clock\_timestamp()

timeofday()

now()

transaction\_timestamp()等价于CURRENT\_TIMESTAMP，但是其命名清楚地反映了它的返回值。statement\_timestamp()返回当前语句的开始时刻（更准确的说是收到 客户端最后一条命令的时间）。statement\_timestamp()和transaction\_timestamp()在一个事务的第一条命令期间返回值相同，但是在随后的命令中却不一定相同。 clock\_timestamp()返回真正的当前时间，因此它的值甚至在同一条 SQL 命令中都会变化。

和clock\_timestamp()相似，timeofday()也返回真实的当前时间，但是它的结果是一个格式化的text串，而不是timestamp with time zone值。now()是瀚高数据库的一个传统，等效于transaction\_timestamp()。

所有日期/时间类型还接受特殊的文字值now，用于指定当前的日期和时间（重申，被解释为当前事务的开始时刻）。 因此，下面三个都返回相同的结果：

SELECT CURRENT\_TIMESTAMP;

SELECT now();

SELECT TIMESTAMP 'now'; -- 对于和 DEFAULT 一起使用是不正确的

| **提示：** |
| --- |
| 在创建表期间指定一个DEFAULT子句时，你不会希望使用第三种形式。系统将在分析这个常量的时候把now转换为一个timestamp， 这样需要默认值时就会得到创建表的时间！而前两种形式要到实际使用缺省值的时候才被计算， 因为它们是函数调用。因此它们可以给出每次插入行的时刻。 |

### 延时执行

下面的这些函数可以用于让服务器进程延时执行：

pg\_sleep(seconds)

pg\_sleep\_for(interval)

pg\_sleep\_until(timestamp with time zone)

pg\_sleep让当前的会话进程休眠seconds 秒以后再执行。seconds是一个double precision类型的值，所以可以指定带小数的秒数。pg\_sleep\_for是针对用 interval指定的较长休眠时间的函数。pg\_sleep\_until 则可以用来休眠到一个指定的时刻唤醒。例如：

SELECT pg\_sleep(1.5);

SELECT pg\_sleep\_for('5 minutes');

SELECT pg\_sleep\_until('tomorrow 03:00');

| **注意：** |
| --- |
| 有效的休眠时间间隔精度是平台相关的，通常 0.01 秒是通用值。休眠延迟将至少持续指定的时长，也有可能由于服务器负荷而比指定的时间长。特别地， pg\_sleep\_until并不保证能刚好在指定的时刻被唤醒，但它不会在比指定时刻早的时候醒来。 |

| 警告： |
| --- |
| 请确保在调用pg\_sleep或者其变体时，你的会话没有持有不必要 的锁。否则其它会话可能必须等待你的休眠会话，因而减慢整个系统速度。 |

## 枚举支持函数

对于枚举类型(在第 7.7 节中描述）， 有一些函数允许更清洁的编码，而不需要为一个枚举类型硬写特定的值。它们被列在表8.33中。本例假定一个枚举类型被创建为：

CREATE TYPE rainbow AS ENUM ('red', 'orange', 'yellow', 'green', 'blue',’purple');

| **函数** | **描述** | **例子** | **例子结果** |
| --- | --- | --- | --- |
| enum\_first(anyenum) | 返回输入枚举类型的 第一个值 | enum\_first(null::rainbow) re | bow |
| enum\_last(anyenum) | 返回输入枚举类型的最后一个值 | enum\_last(null::rainbow) | purple |
| enum\_range(anyenum) | 将输入枚举类型的所有值作为一个有序的数组返回 | enum\_range(null::rainbow) | {red,orange,yellow,green,blue,purp |
| enum\_range(anyenum, anyenum) | 以一个数组返回在给定两个枚举值之间的范围。值必须来自相同的枚举类型。 如果第一个参数为空，其结果将从枚举类型的第一个值开始。如果 第二参数为空，其结果将以枚举类型的最后一个值结束。 | enum\_range(‘orange’::rainbow, ‘green’::rainbow) | {orange,yellow,green} |
| enum\_range(NULL, ‘green’::rainbow) | {red,orange,yellow,green} |  |  |
| enum\_range(‘orange’::rainbow, NULL) | {orange,yellow,green,blue,purple} |  |  |

: 表 8.33 枚举支持函数

请注意，除了双参数形式的enum\_range外， 这些函数忽略传递给它们的具体值，它们只关心声明的数据类型。 空值或类型的一个特定值可以通过，并得到相同的结果。这些函数更多地被用于一个表列或函数参数，而不是一个硬写的类型名，如例子中所建议。

## 几何函数和操作符

几何类型point、box、 lseg、line、path、 polygon和circle有一大堆本地支持函数和操作符，如表 8.34、表 8.35和表 8.36中所示。

| **注意：** |
| --- |
| 请注意”same as”操作符（~=），表示point、box、polygon和circle类型的一般相等概念。这些类型中的某些还有一个=操作符，但是=只比较相同的面积。其它的标量比较操作符 （<=等等）也是为这些类型比较面积。 |

| **操作符** | **描述** | **例子** |
| --- | --- | --- |
| + | 平移 | box ‘((0,0),(1,1))’ + point ‘(2.0,0)’ |
| \- | 平移 | box ‘((0,0),(1,1))’ - point ‘(2.0,0)’ |
| \* | 缩放/旋转 | box ‘((0,0),(1,1))’ \* point ‘(2.0,0)’ |
| / | 缩放/旋转 | box ‘((0,0),(2,2))’ / point ‘(2.0,0)’ |
| # | 相交的点或方框 | box ‘((1,-1),(-1,1))’ # box ‘((1,1),(-2,-2))’ |
| # | 路径或多边形中的点数 | \# path ‘((1,0),(0,1), (-1,0))’ |
| @-@ | 长度或周长 | @-@ path ‘((0,0),(1,0))’ |
| @@ | 中心 | @@ circle ‘((0,0),10)’ |
| ## | 第二个操作数上最接近第一 个操作数的点 | point ‘(0,0)’ ## lseg ‘((2,0),(0,2))’ |
| <-> | 距离 | circle ‘((0,0),1)’ <-> circle ‘((5,0),1)’ |
| && | 是否重叠？（只要有一个公 共点这就为真） | box ‘((0,0),(1,1))’ && box ‘((0,0),(2,2))’ |
| << | 是否严格地在左侧？ | circle ‘((0,0),1)’ << circle ‘((5,0),1)’ |
| \>> | 是否严格地在右侧 | circle ‘((5,0),1)’ >> circle ‘((0,0),1)’ |
| &< | 没有延展到右边？ | box ‘((0,0),(1,1))’ &< box ‘((0,0),(2,2))’ |
| &> | 没有延展到左边？ | box ‘((0,0),(3,3))’ &> box ‘((0,0),(2,2))’ |
| <<\| | 严格在下？ | box ‘((0,0),(3,3))’ <<\| box ‘((3,4),(5,5))’ |
| \|>> | 严格在上？ | box ‘((3,4),(5,5))’ \|>> box ‘((0,0),(3,3))’ |
| &<\| | 没有延展到上面？ | box ‘((0,0),(1,1))’ &<\| box ‘((0,0),(2,2))’ |
| \|&> | 没有延展到下面？ | box ‘((0,0),(3,3))’ \|&> box ‘((0,0),(2,2))’ |
| <^ | 在下面（允许相切）？ | circle ‘((0,0),1)’ <^ circle ‘((0,5),1)’ |
| \>^ | 在上面（允许相切）？ | circle ‘((0,5),1)’ >^ circle ‘((0,0),1)’ |
| ?# | 相交？ | lseg ‘((-1,0),(1,0))’?# box ‘((-2,-2),(2,2))’ |
| ?- | 水平？ | ?- lseg ‘((-1,0),(1,0))’ |
| ?- | 水平对齐？ | point ‘(1,0)’?- point ‘(0,0)’ |
| ?\| | 垂直？ | ?\| lseg ‘((-1,0),(1,0))’ |
| ?\| | 垂直对齐？ | point ‘(0,1)’?\| point ‘(0,0)’ |
| ?-\| | 相互垂直？ | lseg ‘((0,0),(0,1))’?-\| lseg ‘((0,0),(1,0))’ |
| ?\|\| | 平行？ | lseg ‘((-1,0),(1,0))’?\|\| lseg ‘((-1,2),(1,2))’ |
| @> | 包含？ | circle ‘((0,0),2)’ @> point ‘(1,1)’ |
| <@ | 包含在内或在上？ | point ‘(1,1)’ <@ circle ‘((0,0),2)’ |
| ~= | 相同？ | polygon ‘((0,0),(1,1))’ ~= polygon ‘((1,1),(0,0))’ |

: 表 8.34 几何操作符

| **注意：** |
| --- |
| 在瀚高数据库之前，包含操作符@>和<@被分别称为~和@。 这些名字仍然可以使用，但是已被废除并且最终将被移除。 |

| **函数** | **返回类型** | **描述** | **例子** |
| --- | --- | --- | --- |
| area(object) | double precision | 面积 | area(box ‘((0,0), (1,1))’) |
| center(object) | point | 中心 | center(box’((0,0), (1,2))’) |
| diameter(circle) | double precision | 圆的直径 | diameter(circle ‘((0,0),2.0)’) |
| height(box) | double precision | 方框的垂直尺寸 | height(box’((0,0), (1,1))’) |
| isclosed(path) | boolean | 一个封闭路径？ | isclosed(path ‘((0,0),(1,1), (2,0))’) |
| isopen(path) | boolean | 一个开放路径？ | isopen(path ‘\[(0,0),(1,1), (2,0)\]’) |
| length(object) | double precision | 长度 | length(path ‘((-1,0),(1,0))’) |
| npoints(path) | int | 点数 | npoints(path ‘\[(0,0),(1,1), (2,0)\]’) |
| npoints(polygon) | int | 点数 | npoints(polygon ‘((1,1),(0,0))’) |
| pclose(path) | path | 将路径转换成封闭的 | pclose(path ‘\[(0,0),(1,1), (2,0)\]’) |
| popen(path) | path | 将路径转换成开放 | popen(path ‘((0,0), (1,1),(2,0))’) |
| radius(circle) | double precision | 圆的半径 | radius(circle ‘((0,0),2.0)’) |
| width(box) | double precision | 方框的水平尺寸 | width(box ‘((0,0), (1,1))’) |

: 表 8.35 几何函数

| **函数** | **返回类型** | **描述** | **例子** |
| --- | --- | --- | --- |
| box(circle) | box | 圆到方框 | box(circle’((0,0),2.0)’) |
| box(point) | box | 点到空方框 | box(point ‘(0,0)’) |
| box(point, point) | box | 点到方框 | box(point ‘(0,0)’, point ‘(1,1)’) |
| box(polygon) | box | 多边形到方框 | box(polygon’((0,0),(1,1), (2,0))’) |
| bound\_box(box, box) | box | 方框到外包框 | bound\_box(box’((0,0),(1,1))’, box ‘((3,3), (4,4))’) |
| circle(box) | circle | 方框到圆 | circle(box ‘((0,0), (1,1))’) |
| circle(point, double precision) | circle | 中心和半径到圆 | circle(point ‘(0,0)’, 2.0) |
| circle(polygon) | circle | 多边形到圆 | circle(polygon ‘((0,0),(1,1), (2,0))’) |
| line(point, point) | line | 点到线 | line(point ‘(-1,0)’, point ‘(1,0)’) |
| lseg(box) | lseg | 方框对角线到线段 | lseg(box ‘((-1,0), (1,0))’) |
| lseg(point, point) | lseg | 点到线段 | lseg(point ‘(-1,0)’, point ‘(1,0)’) |
| path(polygon) | path | 多边形到路径 | path(polygon ‘((0,0),(1,1), (2,0))’) |
| point(double precision, double precision) | point | 构造点 | point(23.4, -44.5) |
| point(box) | point | 方框的中心 | point(box ‘((-1,0), (1,0))’) |
| point(circle) | point | 圆的中心 | point(circle ‘((0,0),2.0)’) |
| point(lseg) | point | 线段的中心 | point(lseg’((-1,0),(1,0))’) |
| point(polygon) | point | 多边形的中心 | point(polygon ‘((0,0),(1,1), (2,0))’) |
| polygon(box) | polygon | 方框到4点多边形 | polygon(box ‘((0,0),(1,1))’) |
| polygon(circle) | polygon | 圆到12点多边形 | polygon(circle ‘((0,0),2.0)’) |
| polygon(npts, circle) | polygon | 点到npts点多边形 | polygon(12, circle ‘((0,0),2.0)’) |
| polygon(path) | polygon | 路径到多边形 | polygon(path ‘((0,0),(1,1), (2,0))’) |

: 表 8.36 几何类型转换函数

我们可以把一个point的两个组成数字当作具有索引 0 和 1 的数组访问。例如，如果t.p是一个point列，那么SELECT p\[0\] FROM t检索 X 座标而 UPDATE t SET p\[1\] =...改变 Y 座标。同样，box或者lseg类型的值可以当作两个point值的数组值看待。

函数area可以用于类型box、circle和path。area函数操作path数据类型的时候， 只有在path的点没有交叉的情况下才可用。例如，path

'((0,0),(0,1),(2,1),(2,2),(1,2),(1,0),(0,0))'::PATH是不行的， 而下面的视觉上相同的 path '((0,0),(0,1),(1,1),(1,2),(2,2),(2,1),(1,1),(1,0),(0,0))'::PATH就可以。 如果交叉和不交叉的path概念让你疑惑，那么把上面两个path都画在一张图纸上，你就明白了。

## 网络地址函数和操作符

表8.37展示了可以用于cidr和 inet类型的操作符。 操作符<<、<<=、 >>、>>=和 &&测试用于子网包含。它们只考虑两个地址的网 络部分（忽略任何主机部分），然后判断其中一个网络部分是等于另外一个或者是 另外一个的子网。

| **操作符** | **描述** | **例子** |
| --- | --- | --- |
| < | 小于 | inet ‘192.168.1.5’ < inet ‘192.168.1.6’ |
| <= | 小于等于 | inet ‘192.168.1.5’ <= inet ‘192.168.1.5’ |
| \= | 等于 | inet ‘192.168.1.5’ = inet ‘192.168.1.5’ |
| \>= | 大于等于 | inet ‘192.168.1.5’ >= inet ‘192.168.1.5’ |
| \> | 大于 | inet ‘192.168.1.5’ > inet ‘192.168.1.4’ |
| <> | 不等于 | inet ‘192.168.1.5’ <> inet ‘192.168.1.4’ |
| << | 被包含在内 | inet ‘192.168.1.5’ << inet ‘192.168.1/24’ |
| <<= | 被包含在内或等于 | inet ‘192.168.1/24’ <<= inet ‘192.168.1/24’ |
| \>> | 包含 | inet ‘192.168.1/24’ >> inet ‘192.168.1.5’ |
| \>>= | 包含或等于 | inet ‘192.168.1/24’ >>= inet ‘192.168.1/24’ |
| && | 包含或者被包含contains or is contained by | inet ‘192.168.1/24’ && inet ‘192.168.1.80/28’ |
| ~ | 按位 NOT | ~ inet ‘192.168.1.6’ |
| & | 按位 AND | inet ‘192.168.1.6’ & inet ‘0.0.0.255’ |
| \| | 按位 OR | inet ‘192.168.1.6’ \| inet ‘0.0.0.255’ |
| + | 加 | inet ‘192.168.1.6’ + 25 |
| \- | 减 | inet ‘192.168.1.43’ - 36 |
| \- | 减 | inet ‘192.168.1.43’ - inet ‘192.168.1.19’ |

: 表 8.37 cidr和inet操作符

表 8.38展示了所有可以用于cidr和inet类型的函数。函数abbrev、host和text主要是为了提供可选的显示格式用的。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| abbrev(inet) | text | 缩写显示格式文本 | abbrev(inet ‘10.1.0.0/16’) | 10.1.0.0/16 |
| abbrev(cidr) | text | 缩写显示格式文本 | abbrev(cidr ‘10.1.0.0/16’) | 10.1/16 |
| broadcast(inet) | inet | 网络广播地址 | broadcast(‘192.168.1.5/24’) | 192.168.1.255/24 |
| family(inet) | int | 抽取地址族；4为 IPv4， 6为 IPv6 | family(‘::1’) | 6 |
| host(inet) | text | 抽取 IP 地址为文本 | host(‘192.168.1.5/24’) | 192.168.1.5/24 |
| hostmask(inet) | inet | 为网络构造主机掩码 | hostmask(‘192.168.23.20/30’) | 192.168.23.20 |
| masklen(inet) | int | 抽取网络掩码长度 | masklen(‘192.168.1.5/24’) | 192.168.1.5 |
| netmask(inet) | inet | 为网络构造网络掩码 | netmask(‘192.168.1.5/24’) | 255.255.255.0 |
| network(inet) | cidr | 抽取地址的网络部分 | network(‘192.168.1.5/24’) | 192.168.1.0/24 |
| set\_masklen(inet, int) | inet | 为inet值设置网络掩码长度 | set\_masklen(‘192.168.1.5/24’, 16) | 192.168.1.5/16 |
| set\_masklen(cidr, int) | cidr | 为cidr值设置网络掩码长度 | set\_masklen(‘192.168.1.0/24’::cidr, 16) | 192.168.1.0 |
| text(inet) | text | 抽取 IP 地址和网络掩码长度为 文本 | text(inet ‘192.168.1.5’) | 192.168.1.5/32 |
| inet\_same\_family(inet, inet) | boolean | 地址是来自于同一个家族吗？ | inet\_same\_family(‘192.168.1.5/24’, ‘::1’) | 192.168.1.5/24 |
| inet\_merge(inet, inet) | cidr | 包括给定网络的最小网络 | inet\_merge(‘192.168.1.5/24’, ‘192.168.2.5/24’) | 192.168.0.0/22 |

: 表 8.38 cidr和inet函数

任何cidr值都能够被隐式或显式地转换为inet值， 因此上述能够操作inet值的函数也同样能够操作cidr值（也有独立的用于inet和cidr的函数，因为它的行为应当和这两种情况不同）。inet值也可以转换为cidr值。完成时，该网络掩码右侧的任何位都将无声地转换为零以获得一个有效的cidr值。另外，你还可以使用常规的造型语法将一个文本字符串转换为inet或cidr值：例如，inet(expression)或colname::cidr。

表 8.39展示了可以用于macaddr类型的函数。 函数trunc(macaddr)返回一个 MAC 地址，该地址的最后三个字节设置为零。这样可以把剩下的前缀与一个制造商相关联。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| trunc(macaddr) | macaddr | 设置最后3个字节为零 | trunc(macaddr ‘12:34:56:78:90:ab’) | 12:34:56:00:00:00 |

: 表 8.39 macaddr函数

macaddr类型还支持标准关系操作符 （>、<=等） 用于编辑次序，并且按位算术操作符（~、&和|）用于 NOT、AND 和 OR。

表 8.40中展示了可以用于macaddr8类型的函数。函数trunc(macaddr8)返回一个后五个字节设置为零的MAC地址。这可以被用来为一个制造商关联一个前缀。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| trunc(macaddr8) | macaddr8 | 设置最后五个字节为零 | trunc(macaddr8 ‘12:34:56:78:90:ab;cd:ef’) | 12:34:56:00:00:00:00:00 |
| macaddr8\_set7bit(macaddr8) | macaddr8 | 设置第7位为一，也被称为修改版 的EUI-64，用于内含在IPv6地址中 | macaddr8\_set7bit(macaddr8 ‘00:34:56:ab;cd:ef’) | 02:34:56:ff:fe:ab;cd:ef |

: 表 8.40 macaddr8函数

macaddr8类型也支持用于排序的标准关系操作符（>、<=等）以及用于NOT、AND和OR的位运算操作符（~、&和|）。

## 文本搜索函数和操作符

表 8.41、 表 8.42和 表8.43总结了为全文搜索提供的函数和操作符。瀚高数据库的文本搜索功能的详细解释可参考第 11 章。

| **操作符** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| @@ | boolean | tsvector匹 配tsquery吗？ | to\_tsvector(‘fat cats ate rats’) @@ to\_tsquery(‘cat & rat’) | t |
| @@@ | boolean | @@的已废弃同义 词 | to\_tsvector(‘fat cats ate rats’) @@@to\_tsquery(‘cat & rat’) | t |
| \|\| | tsvector | 连接tsvector | ‘a:1 b:2’::tsvector \|\| ‘c:1 d:2 b:3’::tsvector | ‘a’:1 ‘b’:2,5 ‘c’:3 ‘d’:4 |
| && | tsquery | 将tsquery用 AND连接起来 | ‘fat \| rat’::tsquery && ‘cat’::tsquery | ( ‘fat’ \| ‘rat’ ) & ‘cat’ |
| \|\| | tsquery | 将tsquery用 OR连接起来 | ‘fat \| rat’::tsquery \|\| ‘cat’::tsquery | ( ‘fat’ \| ‘rat’ ) \| ‘cat’ |
| !! | tsquery | 对一个tsquery取反 | !! ‘cat’::tsquery | !’cat’ |
| <-> | tsquery | tsquery后面跟 着tsquery | to\_tsquery(‘fat’) <-> to\_tsquery(‘rat’) | fat’ <-> ‘rat’ |
| @> | boolean | tsquery包含另一个？ | ‘cat’::tsquery @> ‘cat & rat’::tsquery | f |
| <@ | boolean | tsquery被包含？ | ‘cat’::tsquery <@ ‘cat & rat’::tsquery | t |

: 表 8.41 文本搜索操作符

| **注意：** |
| --- |
| tsquery的包含操作符只考虑两个查询中的词位，而忽略组合操作符。 |

除了显示在表中的操作符，还定义了tsvector和tsquery类型的普通B-tree比较操作符（=、<等）。它们对于文本搜索不是很有用，但是允许使用。例如，建在这些类型列上的唯一索引。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| array\_to\_tsvector(text\[\]) | tsvector | 把词位数组转换成tsvector | array\_to\_tsvector(‘{fat,cat,rat}’::text\[\]) | ‘cat’ ‘fat’ ‘rat’ |
| get\_current\_ts\_config() | regconfig | 获得默认文本搜索配置 | get\_current\_ts\_config() | english |
| length(tsvector) | integer | tsvector中的词位数 | length(‘fat:2,4 cat:3 rat:5A’::tsvector) | 3 |
| numnode(tsquery) | integer | tsquery中词位外加操作符的数目 | numnode(‘(fat & rat) \| cat’::tsquery) | 5 |
| plainto\_tsquery(\[ config regconfig, \] query text) | tsquery | 产生tsquery但忽略标点符号 | plainto\_tsquery(‘english’, ‘The Fat Rats’) | ‘fat’ & ‘rat’ |
| phraseto\_tsquery(\[ config regconfig, \] query text) | tsquery | 产生忽略标点搜索短语的tsquery | phraseto\_tsquery(‘english’, ‘The Fat Rats’) | ‘fat’ <-> ‘rat’ |
| websearch\_to\_tsquery(\[ config regconfig, \] query text) | tsquery | 从一个Web搜索风格的查询产 生tsquery | websearch\_to\_tsquery(‘english’, ‘“fat rat” or rat’) | ‘fat’ <-> ‘rat’ \| ‘rat |
| querytree(query tsquery) | text | 获得一个tsquery的可索引部分 | querytree(‘foo &! bar’::tsquery) | ‘foo’ |
| setweight(vector tsvector, weight “char”) | tsvector | 获得一个tsquery的可索引部分 | querytree(‘foo &! bar’::tsquery) | ‘foo’ |
| setweight(vector tsvector, weight “char”) | tsvector | 为vector的每一个元素分配权重 | setweight(‘fat:2,4 cat:3 rat:5B’::tsvector, ‘A’) | ‘cat’:3A ‘fat’:2A,4A ‘rat’:5A |
| setweight(vector tsvector, weight “char”, lexemes text\[\]) | tsvector | 为lexemes中列出的vector的元素分配权重 | setweight(‘fat:2,4 cat:3 rat:5B’::tsvector, ‘A’, ‘{cat,rat}’) | ‘cat’:3A ‘fat’:2,4 ‘rat’:5A |
| strip(tsvector) | tsvector | 从tsvector中移除位置和权重 | strip(‘fat:2,4 cat:3 rat:5A’::tsvector) | ‘cat’ ‘fat’ ‘rat’ |
| to\_tsquery(\[ config regconfig, \] query text) | tsquery | 规范化词并转换成tsquery |  |  |
| to\_tsvector(\[ config regconfig, \] document text) | tsvector | 缩减文档文本成tsvector | to\_tsvector(‘english’, ‘The Fat Rats’) | ‘fat’:2 ‘rat’:3 |
| to\_tsvector(\[ config regconfig, \] document json(b)) | tsvector | 把该文档中的每个字符串值缩减成一个tsvector，然后将它们按在文档中的顺序串接起来形成一个tsvector | to\_tsvector(‘english’, ‘{“a”: “The Fat Rats”}’::json) | ‘fat’:2 ‘rat’:3 |
| json(b)\_to\_tsvector(\[ config regconfig, \] document json(b), filter json(b)) | tsvector | 把filter指定的文档中的每个值缩减为一 个tsvector，然后把它们按照文档中的顺序串接起来形成一 个tsvector。filter是 一个jsonb数组，它列举哪些种类的元素需要被包括在结果tsvector中。filter的 可能值是”string”（包 括所有字符串值） 、”numeric”（包括所有字符串格式的数字值）、 “boolean” （包 括所有字符串格 式”true”/ “false”的布尔值）、 “key”（包括所有键）或 者”all”（包括上述所有）。这些值可以被组合在 一起，例如用来包括所有的字符串和数字值。 | json\_to\_tsvector(‘english’, ‘{“a”: “The Fat Rats”, “b”: 123}’::json, ‘\[“string”, “numeric”\]’) | ‘123’:5 ‘fat’:2 ‘rat’:3 |
| ts\_delete(vector tsvector, lexeme text) | tsvector | 从vector中移除给定的lexeme | ts\_delete(‘fat:2,4 cat:3 rat:5A’::tsvector, ‘fat’) | ‘cat’:3 ‘rat’:5A |
| ts\_delete(vector tsvector, lexemes text\[\]) | tsvector | 从vector中移除lexemes中词位的任何出现 | ts\_delete(‘fat:2,4 cat:3 rat:5A’::tsvector, ARRAY\[‘fat’,’rat’\]) | cat’:3 |
| ts\_filter(vector tsvector, weights “char”\[\]) | tsvector | 从vector中只选择带有给定权重的元素 | ts\_filter(‘fat:2,4 cat:3b rat:5A’::tsvector, ‘{a,b}’) | ‘cat’:3B ‘rat’:5A |
| ts\_headline(\[ config regconfig, \] document text, query tsquery \[, options text \]) | text | 显示一个查询匹配 | ts\_headline(‘x y z’, ‘z’::tsquery) | x y **z** |
| ts\_headline(\[ config regconfig, \] document json(b), query tsquery \[, options text \]) | text | 显示一个查询匹配 | ts\_headline(‘{“a”:”x y z”}’::json, ‘z’::tsquery) | {“a”:”x y **z** “} |
| ts\_rank(\[ weights float4\[\], \] vector tsvector, query tsquery \[,normalization integer \]) | float4 | 为查询排名文档 | ts\_rank(textsearch, query) | 0.818 |
| ts\_rank\_cd(\[ weights float4\[\], \] vector tsvector, query tsquery \[, normalization integer \]) | float4 | 使用覆盖密度为查询排名文档 | ts\_rank\_cd(‘{0.1, 0.2, 0.4, 1.0}’, textsearch, query) | 2.01317 |
| ts\_rewrite(query tsquery, target tsquery, substitute tsquery) | tsquery | 在查询内用substitute替换target | ts\_rewrite(‘a & b’::tsquery, ‘a’::tsquery, ‘foo\| bar’::tsquery) | ‘b’ & ( ‘foo’ \| ‘bar’ ) |
| ts\_rewrite(query tsquery, select text) | tsquery | 使用来自一个SELECT的目标和替换者进行替换 | SELECT ts\_rewrite(‘a & b’::tsquery, ‘SELECT t,s FROM aliases’) | ‘b’ & ( ‘foo’ \| ‘bar’ ) |
| tsquery\_phrase(query1 tsquery, query2 tsquery) | tsquery | 制造搜索后面跟着query2的query1的 查询（和<->操作 符相同） | tsquery\_phrase(to\_tsquery(‘fat’), to\_tsquery(‘cat’)) | fat’ <-> ‘cat’ |
| tsquery\_phrase(query1 tsquery, query2 tsquery, distance integer) | tsquery | 制造查询来搜索在query1后面最大距 离distance上跟着query2 的情况 | tsquery\_phrase(to\_tsquery(‘fat’), to\_tsquery(‘cat’), 10) | fat’ <10> ‘cat’ |
| tsvector\_to\_array(tsvector) | text\[\] | 把tsvector转换为词位数组 | tsvector\_to\_array(‘fat:2,4 cat:3 rat:5A’::tsvector) | cat,fat,rat} |
| tsvector\_update\_trigger() | trigger | 用于自动tsvector列更新的触发器函数 | CREATE TRIGGER … tsvector\_update\_trigger(tsvcol, ‘pg\_catalog.swedish’, title, body) |  |
| tsvector\_update\_trigger\_column() | trigger | 用于自动tsvector列更新的触发器函数 | CREATE TRIGGER … tsvector\_update\_trigger\_column(tsvcol, configcol, title, body) |  |
| unnest(tsvector, OUT lexeme text, OUT positions smallint\[\], OUT weights text) | setof record | 把一个 tsvector 扩展成一组行 | unnest(‘fat:2,4 cat:3 rat:5A’::tsvector) | (cat,{3}, {D}) … |

: 表 8.42 文本搜索函数

| **注意：** |
| --- |
| 所有接受一个可选的regconfig参数的文本搜索函数在该参数被忽略时，使用由default\_text\_search\_config指定的配置。 |

表 8.43中的函数被单独列出，因为它们通常不被用于日常的文本搜索操作。 它们有助于开发和调试新的文本搜索配置。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| ts\_debug(\[ config regconfig, \] document text, OUT alias text, OUT description text, OUT token text, OUT dictionaries regdictionary\[\], OUT dictionary regdictionary, OUT lexemes text\[\]) | setof record | 测试一个配置 | ts\_debug(‘english’, ‘The Brightest supernovaes’) | (asciiword,”Word, all ASCII”,The, {english\_stem},english\_stem, {}). |
| ts\_lexize(dict regdictionary, token text) | text\[\] | 测试一个字典 | ts\_lexize(‘english\_stem’, ‘stars’) | sh\_ste |
| ts\_parse(parser\_name text, document text, OUT tokid integer, OUT token text) | setof record | 测试一个解析器 | ts\_parse(‘default’, ‘foo - bar’) | (1,foo) … |
| ts\_parse(parser\_oid oid, document text, OUT tokid integer, OUT token text) | setof record | 测试一个解析器 | ts\_parse(3722, ‘foo - bar’) | (1,foo) … |
| ts\_token\_type(parser\_name text, OUT tokid integer, OUT alias text, OUT description text) | setof record | 获得解析器定义的记号类型 | ts\_token\_type(‘default’) | (1,asciiword,”Word, all ASCII”) … |
| ts\_token\_type(parser\_oid oid, OUT tokid integer, OUT alias text, OUT description text) | setof record | 获得解析器定义的记号类型 | ts\_token\_type(3722) | (1,asciiword,”Word, all ASCII”) … |
| ts\_stat(sqlquery text, \[ weights text, \] OUT word text, OUT ndoc integer, OUT nentry integer) | setof record | 获得一个tsvector列的统计 | ts\_stat(‘SELECT vector from apod’) | (foo,10,15) … |

: 表 8.43 文本搜索调试函数

## XML 函数

本节中描述的函数以及类函数的表达式都在类型xml的值上操作。类型xml的详细信息请参见第7.13 节。用于在值和类型xml之间转换的类函数的表达式xmlparse和xmlserialize记录在这里，而不是在本节中。

使用大部分这些函数要求瀚高数据库使用了configure --with-libxml进行编译。

### 产生 XML 内容

有一组函数和类函数的表达式可以用来从 SQL 数据产生 XML 内容。它们特别适合于将查询结果格式化成 XML 文档以便于在客户端应用中处理。

#### xmlcomment

xmlcomment(text)

函数xmlcomment创建了一个 XML 值，它包含一个使用指定文本作为内容的 XML 注释。该文本不包含”--“或者也不会以一个”-“结尾，这样结果的结构是一个合法的 XML 注释。如果参数为空，结果也为空。

例子：

SELECT xmlcomment('hello');

xmlcomment

\--------------

<!--hello-->

#### xmlconcat

xmlconcat(xml\[,...\])

函数xmlconcat将由单个 XML 值组成的列表串接成一个单独的值，这个值包含一个 XML 内容片断。空值会被忽略，只有当没有参数为非空时结果才为空。

例子：

SELECT xmlconcat('\<abc/>', '\<bar>foo\</bar>');

xmlconcat

\----------------------

\<abc/>\<bar>foo\</bar>

如果 XML 声明存在，它们会按照下面的方式被组合。如果所有的参数值都有相同的 XML 版本声明，该版本将被用在结果中，否则将不使用版本。如果所有参数值有独立声明值”yes”，那么该值将被用在结果中。如果所有参数值都有一个独立声明值并且至少有一个为”no”，则”no”被用在结果中。否则结果中将没有独立声明。如果结果被决定要要求一个独立声明但是没有版本声明，将会使用一个版本 1.0 的版本声明，因为 XML 要求一个 XML 声明要包含一个版本声明。编码声明会被忽略并且在所有情况中都会被移除。

例子：

SELECT xmlconcat('<?xml version="1.1"?>\<foo/>', '<?xml version="1.1"

standalone="no"?>\<bar/>');

xmlconcat

\-----------------------------------

<?xml version="1.1"?>\<foo/>\<bar/>

#### xmlelement

xmlelement(name name \[, xmlattributes(value \[AS attname\] \[,... \])\] \[,content,...\])

表达式xmlelement使用给定名称、属性和内容产生一个 XML 元素。

例子：

SELECT xmlelement(name foo);

xmlelement

\------------

\<foo/>

SELECT xmlelement(name foo, xmlattributes('xyz' as bar));

xmlelement

\------------------

\<foo bar="xyz"/>

SELECT xmlelement(name foo, xmlattributes(current\_date as bar), 'cont', 'ent');

xmlelement

\-------------------------------------

\<foo bar="2007-01-26">content\</foo>

不是合法 XML 名字的元素名和属性名将被逃逸，逃逸的方法是将违反的字符用序列\_xHHHH\_替换，其中HHHH是被替换字符的 Unicode 代码点的十六进制表示。例如：

SELECT xmlelement(name "foo$bar", xmlattributes('xyz' as "a&b"));

xmlelement

\----------------------------------

<foo\_x0024\_bar a\_x0026\_b="xyz"/>

如果属性值是一个列引用，则不需要指定一个显式的属性名，在这种情况下列的名字将被默认用于属性的名字。在其他情况下，属性必须被给定一个显式名称。因此这个例子是合法的：

CREATE TABLE test (a xml, b xml);

SELECT xmlelement(name test, xmlattributes(a, b)) FROM test;

但是下面这些不合法：

SELECT xmlelement(name test, xmlattributes('constant'), a, b) FROM test;

SELECT xmlelement(name test, xmlattributes(func(a, b))) FROM test;

如果指定了元素内容，它们将被根据其数据类型格式化。如果内容本身也是类型xml，就可以构建复杂的 XML 文档。例如：

SELECT xmlelement(name foo, xmlattributes('xyz' as bar),

xmlelement(name abc),

xmlcomment('test'),

xmlelement(name xyz));

xmlelement

\----------------------------------------------

\<foo bar="xyz">\<abc/><!--test-->\<xyz/>\</foo>

其他类型的内容将被格式化为合法的 XML 字符数据。这意味着字符 <,>, 和 & 将被转换为实体。二进制数据（数据类型bytea）将被表示成base64 或十六进制编码，具体取决于配置参数xmlbinary的设置。为了使瀚高数据库的映射与SQL:2006及以后的SQL:2006中指定的映射保持一致，个别数据类型的特殊行为将不断发展，正如第 D.3.1.3 节中讨论的那样。

#### xmlforest

xmlforest(content \[AS name\] \[,...\])

表达式xmlforest使用给定名称和内容产生一个元素的 XML 森林（序列）。

例子：

SELECT xmlforest('abc' AS foo, 123 AS bar);

xmlforest

\------------------------------

\<foo>abc\</foo>\<bar>123\</bar>

SELECT xmlforest(table\_name, column\_name)

FROM information\_schema.columns

WHERE table\_schema = 'pg\_catalog';

xmlforest

\-------------------------------------------------------------------------------------------

<table\_name>pg\_authid</table\_name><column\_name>rolname</column\_name>

<table\_name>pg\_authid</table\_name><column\_name>rolsuper</column\_name>

...

如我们在第二个例子中所见，如果内容值是一个列引用，元素名称可以被忽略，这种情况下默认使用列名。否则，必须指定一个名字。

如上文xmlelement所示，非法 XML 名字的元素名会被逃逸。相似地，内容数据也会被逃逸来产生合法的 XML 内容，除非它已经是一个xml类型。

注意如果 XML 森林由多于一个元素组成，那么它不是合法的 XML 文档，因此在xmlelement中包装xmlforest表达式会有用处。

#### xmlpi

xmlpi(name target \[, content\])

表达式xmlpi创建一个 XML 处理指令。如果存在内容，内容不能包含字符序列?>。

例子：

SELECT xmlpi(name php, 'echo "hello world";');

xmlpi

\-----------------------------

<?php echo "hello world";?>

#### xmlroot

xmlroot(xml, version text | no value \[, standalone yes|no|no value\])

表达式xmlroot修改一个 XML 值的根结点的属性。如果指定了一个版本，它会替换根节点的版本声明中的值；如果指定了一个独立设置，它会替换根节点的独立声明中的值。

SELECT xmlroot(xmlparse(document '<?xml version="1.1"?>\<content>abc\</content>'),

version '1.0', standalone yes);

xmlroot

\----------------------------------------

<?xml version="1.0" standalone="yes"?>

\<content>abc\</content>

#### xmlagg

xmlagg(xml)

和这里描述的其他函数不同，函数xmlagg是一个聚集函数。它将聚集函数调用的输入值串接起来，非常像xmlconcat所做的事情，除了串接是跨行发生的而不是在单一行的多个表达式上发生。聚集表达式的更多信息请见第 9.20 节。

例子：

u为了决定串接的顺序，可以为聚集调用增加一个ORDER BY子句，如第 4.2.7 节中所述。例如：

SELECT xmlagg(x ORDER BY y DESC) FROM test;

xmlagg

\<bar/>\<foo>abc\</foo>

我们推荐在以前的版本中使用下列非标准方法，并且它们在特定情况下仍然有用：

SELECT xmlagg(x) FROM (SELECT \* FROM test ORDER BY y DESC) AS tab;

xmlagg

\----------------------

\<bar/>\<foo>abc\</foo>

### XML 谓词

这一节描述的表达式检查xml值的属性。

#### IS DOCUMENT

xml IS DOCUMENT

如果参数 XML 值是一个正确的 XML 文档，则IS DOCUMENT返回真，如果不是则返回假（即它是一个内容片断），或者是参数为空时返回空。文档和内容片断之间的区别请见第 7.13 节。

#### IS NOT DOCUMENT

xml IS NOT DOCUMENT

如果参数中的XML值是一个正确的XML文档，那么表达式IS NOT DOCUMENT返回假，否则返回真（也就是说它是一个内容片段），如果参数为空则返回空。

#### XMLEXISTS

XMLEXISTS(text PASSING \[BY { REF | VALUE }\] xml \[BY { REF | VALUE }\])

函数xmlexists评价一个XPath 1.0表达式(第一个参数)，以传递的XML值作为其上下文项。 如果评价的结果产生一个空节点集，该函数返回false，如果产生任何其他值，则返回 true。 如果任何参数为空，则函数返回null。 作为上下文项传递的非空值必须是一个XML文档，而不是内容片段或任何非XML值。

例子：

SELECT xmlexists('//town\[text() = ''Toronto''\]' PASSING BY VALUE

'\<towns>\<town>Toronto\</town>\<town>Ottawa\</town>\</towns>');

xmlexists

\------------

t

(1 row)

BY REF和BY VALUE子句在瀚高数据库中被接受，但在第 D.3.2 节中被忽略。在SQL标准中，xmlexists函数评估XML查询语言中的表达式，但瀚高数据库只允许使用XPath 1.0表达式，在第 D.3.1 节中讨论过。

#### xml\_is\_well\_formed

xml\_is\_well\_formed(text)

xml\_is\_well\_formed\_document(text)

xml\_is\_well\_formed\_content(text)

这些函数检查一个text串是不是一个良构的 XML，返回一个布尔结果。xml\_is\_well\_formed\_document检查一个良构的文档，而xml\_is\_well\_formed\_content检查良构的内容。如果xmloption配置参数被设置为DOCUMENT，xml\_is\_well\_formed会做第一个函数的工作；如果配置参数被设置为CONTENT，xml\_is\_well\_formed会做第二个函数的工作。这意味着xml\_is\_well\_formed对于检查一个到类型xml的简单造型是否会成功非常有用，而其他两个函数对于检查XMLPARSE的对应变体是否会成功有用。

例子：

SET xmloption TO DOCUMENT;

SELECT xml\_is\_well\_formed('<>');

xml\_is\_well\_formed

\--------------------

f

(1 row)

SELECT xml\_is\_well\_formed('\<abc/>');

xml\_is\_well\_formed

\--------------------

t

(1 row)

SET xmloption TO CONTENT;

SELECT xml\_is\_well\_formed('abc');

xml\_is\_well\_formed

\--------------------

t

(1 row)

SELECT xml\_is\_well\_formed\_document('<pg:foo xmlns:pg=" [http://www.highgo.com/](http://www.highgo.com/)

stuff">bar</pg:foo>');

xml\_is\_well\_formed\_document

\-----------------------------

t

(1 row)

SELECT xml\_is\_well\_formed\_document('<pg:foo xmlns:pg=" [http://www.highgo.com/](http://www.highgo.com/)

stuff">bar</my:foo>');

xml\_is\_well\_formed\_document

\-----------------------------

f

(1 row)

最后一个例子显示了这些检查也包括名字空间是否正确地匹配。

### 处理 XML

要处理数据类型xml的值， 瀚高数据库提供了函数xpath和xpath\_exists，它们计算 XPath表达式以及XMLTABLE表函数。

#### xpath

xpath(xpath, xml \[, nsarray\])

函数xpath在 XML 值 xml上计算 XPath 1.0 表达式xpath (a text value)。它返回一个 XML值的数组，该数组对应于该 XPath 表达式产生的结点集合。如果该 XPath 表达式返回一个标量值而不是一个结点集合，将会返回一个单一元素的数组。

第二个参数必须是一个良构的 XML 文档。特殊地，它必须有一个单一根结点元素。

该函数可选的第三个参数是一个名字空间映射的数组。这个数组应该是一个二维text数组，其第二轴长度等于2（即它应该是一个数组的数组，其中每一个都由刚好 2 个元素组成）。

每个数组项的第一个元素是名字空间的名称（别名），第二个元素是名字空间的 URI。并不要求在这个数组中提供的别名和在 XML 文档本身中使用的那些名字空间相同（换句话说，在 XML 文档中和在xpath函数环境中，别名都是本地的）。

例子：

SELECT xpath('/my:a/text()', '<my:a xmlns:my=" [http://example.com\\"\\>test\\](http://example.com/%22/%3Etest/) </my:a>',

ARRAY\[ARRAY\['my', ' [http://example.com\\'\\\]\\\]](http://example.com/'/]/]));

xpath

\--------

{test}

(1 row)

要处理默认（匿名）命名空间，做这样的事情：

SELECT xpath('//mydefns:b/text()', '\<a xmlns=" [http://example.com\\"\\>\\](http://example.com/%22/%3E/) \<b>test\</b></

a>',

ARRAY\[ARRAY\['mydefns', ' [http://example.com\\'\\\]\\\]](http://example.com/'/]/]));

xpath

\--------

{test}

(1 row)

#### xpath\_exists

xpath\_exists(xpath, xml \[, nsarray\])

函数xpath\_exists是xpath函数的一种特殊形式。这个函数不是返回满足 XPath 1.0 表达式的单一 XML 值，它返回一个布尔值表示查询是否被满足(具体来说，它是否产生了空节点集以外的任何值)。这个函数等价于标准的XMLEXISTS谓词，不过它还提供了对一个名字空间映射参数的支持。

例子：

SELECT xpath\_exists('/my:a/text()', '<my:a xmlns:my=" [http://example.com\\"\\>test\\](http://example.com/%22/%3Etest/) </

my:a>',

ARRAY\[ARRAY\['my', ' [http://example.com\\'\\\]\\\]](http://example.com/'/]/]));

xpath\_exists

\--------------

t

(1 row)

#### xmltable

xmltable( \[XMLNAMESPACES(namespace uri AS namespace name\[,...\]), \]

row\_expression PASSING \[BY { REF | VALUE }\] document\_expression \[BY

{ REF | VALUE }\]

COLUMNS name { type \[PATH column\_expression\]

\[DEFAULT default\_expression\] \[NOT NULL | NULL\]

| FOR ORDINALITY }

\[,...\]

)

xmltable函数基于给定的XML值产生一个表、一个抽取行的XPath过滤器以及一个列定义集合。

可选的XMLNAMESPACES子句是一个逗号分隔的名字空间列表。它指定文档中使用的XML名字空间极其别名。当前不支持默认的名字空间说明。

所需的row\_expression参数是一个XPath 1.0表达式，通过传递document\_expression作为其上下文项，得到一组XML节点。这些节点就是xmltable转换为输出行的内容。如果document\_expression为空，或者row\_expression产生空节点集或节点集以外的任何值，则不会产生行。

document\_expression提供了上下文。row\_expression的项。它必须是一个格式良好的XML文档；不接受片段/森林。BY REF和BY VALUE子句如上文所讨论的那样，被接受但被忽略了。第 D.3.2 节。在SQL标准中，xmltable函数评估XML查询语言中的表达式。但瀚高数据库只允许使用XPath 1.0的表达式，正如在第 D.3.1 节。

强制需要的COLUMNS子句指定输出表中的列列表。如果COLUMNS子句被省略，每一项描述一个列。格式请见上面的语法综述。列名和类型是必需的，路径、默认值以及为空性子句是可选的。

被标记为FOR ORDINALITY的列将按照从row\_expression的结果节点集中检索到的节点的顺序，从1开始，填充行号。最多只能有一个列被标记为FOR ORDINALITY。

| 注意： |
| --- |
| XPath 1.0 并没有为节点集中的节点指定顺序，因此依赖特定结果顺序的代码将取决于实现。 |

列的column\_expression是一个XPath 1.0表达式，它对每一行都要进行求值，并以row\_expression结果中的当前节点作为其上下文项，以找到列的值。 如果没有给出column\_expression，那么列名被用作隐式路径。

如果一个列的XPath表达式返回一个非XML值（在XPath 1.0中仅限于string、boolean或 double），而该列的瀚高数据库类型不是xml，那么该列将被设置为将值的字符串表示法分配给瀚高数据库类型。 (如果值是布尔值，如果输出列的类型类别是数字，那么它的字符串表示方式将被认为是1或0，否则true或 false。)

如果一个列的XPath表达式返回一个非空的XML节点集，并且该列的瀚高数据库类型是xml，那么如果该列是文档或内容形式的，那么该列将被精确地分配表达式结果。分配给xml输出列的非XML结果会产生内容，一个带有结果字符串值的单个文本节点。分配给任何其他类型的列的XML结果不能有一个以上的节点，否则会产生错误。如果正好有一个节点，则该列将被设置为将该节点的字符串值（如XPath 1.0 string函数定义的那样）分配给瀚高数据库类型。

一个XML元素的字符串值是字符串值的协整，按文档的顺序。该元素中包含的所有文本节点及其子节点。字符串 元素的值是一个没有下级文本节点的元素的值是一个 空字符串（不是NULL）。任何xsi:nil属性都会被忽略。请注意，两个非文本之间的text()节点只用空格，而两个非文本 元素，并且保留了text()上的前导白格。节点不被扁平化。XPath 1.0中的string函数可以参考XPath 1.0中的 定义其他XML节点类型和非XML值的字符串值的规则。

这里介绍的转换规则并不完全是SQL标准中的转换规则，如第 D.3.1.3 节中讨论的那样。

如果路径表达式为给定行返回一个空节点集（通常情况下，当它不匹配时），该列将被设置为NULL，除非指定了default\_expression；然后使用评价该表达式产生的值。

列可能会被标记为NOT NULL。如果一个NOT NULL列的column\_expression不匹配任何东西并且没有DEFAULT或者default\_expression也计算为空，则会报告一个错误。

default\_expression，而不是在调用xmltable时立即被评价，而是在每次需要列的默认值时，都会被评价。 如果表达式符合稳定或不可更改的条件，则可以跳过重复评价。 这意味着，你可以在default\_expression中使用像nextval这样的不稳定函数。

例子：

CREATE TABLE xmldata AS SELECT

xml $$

\<ROWS>

\<ROW id="1">

<COUNTRY\_ID>AU</COUNTRY\_ID>

<COUNTRY\_NAME>Australia</COUNTRY\_NAME>

\</ROW>

\<ROW id="5">

<COUNTRY\_ID>JP</COUNTRY\_ID>

<COUNTRY\_NAME>Japan</COUNTRY\_NAME>

<PREMIER\_NAME>Shinzo Abe</PREMIER\_NAME>

\<SIZE unit="sq\_mi">145935\</SIZE>

\</ROW>

\<ROW id="6">

<COUNTRY\_ID>SG</COUNTRY\_ID>

<COUNTRY\_NAME>Singapore</COUNTRY\_NAME>

\<SIZE unit="sq\_km">697\</SIZE>

\</ROW>

\</ROWS>

$$ AS data;

SELECT xmltable.\*

FROM xmldata,

XMLTABLE('//ROWS/ROW'

PASSING data

COLUMNS id int PATH '@id',

ordinality FOR ORDINALITY,

"COUNTRY\_NAME" text,

country\_id text PATH 'COUNTRY\_ID',

size\_sq\_km float PATH 'SIZE\[@unit = "sq\_km"\]',

size\_other text PATH

'concat(SIZE\[@unit!="sq\_km"\], " ", SIZE\[@unit!

\="sq\_km"\]/@unit)',

premier\_name text PATH 'PREMIER\_NAME' DEFAULT 'not

specified');

id | ordinality | COUNTRY\_NAME | country\_id | size\_sq\_km | size\_other |

premier\_name

\----+------------+--------------+------------+------------+--------------

+---------------

1 | 1 | Australia | AU | | | not

Specified

5 | 2 | Japan | JP | | 145935 sq\_mi |

Shinzo Abe

6 | 3 | Singapore | SG | 697 | | not

specified

接下来的例子展示了多个text()节点的串接、列名用作XPath过滤器的用法以及对空格、XML注释和处理指令的处理：

CREATE TABLE xmlelements AS SELECT

xml $$

\<root>

\<element> Hello<!-- xyxxz -->2a2<?aaaaa?> <!--x--> bbb\<x>xxx\</x>CC </

element>

\</root>

$$ AS data;

SELECT xmltable.\*

FROM xmlelements, XMLTABLE('/root' PASSING data COLUMNS element text);

element

\----------------------

Hello2a2 bbbxxxCC

下面的例子展示了如何使用XMLNAMESPACES子句指定用在XML文档以及XPath表达式中的名字空间列表：

WITH xmldata(data) AS (VALUES ('

\<example xmlns=" [http://example.com/myns\\](http://example.com/myns/) “ xmlns:B=" [http://example.com/b\\"\\>](http://example.com/b/%22/%3E)

\<item foo="1" B:bar="2"/>

\<item foo="3" B:bar="4"/>

\<item foo="4" B:bar="5"/>

\</example>'::xml)

)

SELECT xmltable.\*

FROM XMLTABLE(XMLNAMESPACES(' [http://example.com/myns\\](http://example.com/myns/) ‘ AS x,

' [http://example.com/b\\](http://example.com/b/) ‘ AS "B"),

'/x:example/x:item'

PASSING (SELECT data FROM xmldata)

COLUMNS foo int PATH '@foo',

bar int PATH '@B:bar');

foo | bar

\-----+-----

1 | 2

3 | 4

4 | 5

(3 rows)

### 将表映射到 XML

下面的函数将会把关系表的内容映射成 XML 值。它们可以被看成是 XML 导出功能：

table\_to\_xml(tbl regclass, nulls boolean, tableforest boolean, targetns text)

query\_to\_xml(query text, nulls boolean, tableforest boolean, targetns text)

cursor\_to\_xml(cursor refcursor, count int, nulls boolean,

tableforest boolean, targetns text)

每一个函数的返回值都是xml。

table\_to\_xml映射由参数tbl传递的命名表的内容。regclass类型接受使用常见标记标识表的字符串，包括可选的模式限定和双引号。query\_to\_xml执行由参数query传递的查询并且映射结果集。cursor\_to\_xml从cursor指定的游标中取出指定数量的行。如果需要映射一个大型的表，我们推荐这种变体，因为每一个函数都是在内存中构建结果值的。

如果tableforest为假，则结果的 XML 文档看起来像这样：

\<tablename>

\<row>

\<columnname1>data\</columnname1>

\<columnname2>data\</columnname2>

\</row>

\<row>

...

\</row>

...

\</tablename>

如果tableforest为真，结果是一个看起来像这样的 XML 内容片断：

\<tablename>

\<columnname1>data\</columnname1>

\<columnname2>data\</columnname2>

\</tablename>

\<tablename>

...

\</tablename>

...

如果没有表名可用，在映射一个查询或一个游标时，在第一种格式中使用串table，在第二种格式中使用row。

这几种格式的选择由用户决定。第一种格式是一个正确的 XML 文档，它在很多应用中都很重要。如果结果值要被重组为一个文档，第二种格式在cursor\_to\_xml函数中更有用。前文讨论的产生 XML 内容的函数（特别是xmlelement）可以被用来把结果修改成符合用户的要求。

数据值会被以前文的函数xmlelement中描述的相同方法映射。

参数nulls决定空值是否会被包含在输出中。如果为真，列中的空值被表示为： \<columnname xsi:nil="true"/>

其中xsi是 XML 模式实例的 XML 名字空间前缀。一个合适的名字空间声明将被加入到结果值中。如果为假，包含空值的列将被从输出中忽略掉。

参数targetns指定想要的结果的 XML 名字空间。如果没有想要的特定名字空间，将会传递一个空串。

下面的函数返回 XML 模式文档，这些文档描述上述对应函数所执行的映射：

table\_to\_xmlschema(tbl regclass, nulls boolean, tableforest boolean, targetns

text)

query\_to\_xmlschema(query text, nulls boolean, tableforest boolean, targetns

text)

cursor\_to\_xmlschema(cursor refcursor, nulls boolean, tableforest boolean,

targetns text)

最重要的是相同的参数被传递来获得匹配的 XML 数据映射和 XML 模式文档。

下面的函数产生 XML 数据映射和对应的 XML 模式，并把产生的结果链接在一起放在一个文档（或森林）中。在要求自包含和自描述的结果是它们非常有用：

table\_to\_xml\_and\_xmlschema(tbl regclass, nulls boolean, tableforest boolean,

targetns text)

query\_to\_xml\_and\_xmlschema(query text, nulls boolean, tableforest boolean,

targetns text)

另外，下面的函数可用于产生相似的整个模式或整个当前数据库的映射：

schema\_to\_xml(schema name, nulls boolean, tableforest boolean, targetns text)

schema\_to\_xmlschema(schema name, nulls boolean, tableforest boolean, targetns

text)

schema\_to\_xml\_and\_xmlschema(schema name, nulls boolean, tableforest boolean,

targetns text)

database\_to\_xml(nulls boolean, tableforest boolean, targetns text)

database\_to\_xmlschema(nulls boolean, tableforest boolean, targetns text)

database\_to\_xml\_and\_xmlschema(nulls boolean, tableforest boolean, targetns text)

注意这些函数可能产生很多数据，它们都需要在内存中被构建。在请求大型模式或数据库的内容映射时，可以考虑分别映射每一个表，甚至通过一个游标来映射。

一个模式内容映射的结果看起来像这样：

\<schemaname>

table1-mapping

table2-mapping

...

\</schemaname>

其中一个表映射的格式取决于上文解释的tableforest参数。

一个数据库内容映射的结果看起来像这样：

\<dbname>

\<schema1name>

...

\</schema1name>

\<schema2name>

...

\</schema2name>

...

\</dbname>

其中的模式映射如上所述。

作为一个使用这些函数产生的输出的例子，图 9.1展示了一个 XSLT 样式表，它将table\_to\_xml\_and\_xmlschema的输出转换为一个包含表数据的扁平转印的 HTML 文档。以一种相似的方式，这些函数的结果可以被转换成其他基于 XML 的格式。

图8.1. 转换 SQL/XML 输出到 HTML 的 XSLT 样式表

<?xml version="1.0"?>

<xsl:stylesheet version="1.0"

xmlns:xsl=" [http://www.w3.org/1999/XSL/Transform\\](http://www.w3.org/1999/XSL/Transform/) “

xmlns:xsd=" [http://www.w3.org/2001/XMLSchema\\](http://www.w3.org/2001/XMLSchema/) “

xmlns=" [http://www.w3.org/1999/xhtml\\](http://www.w3.org/1999/xhtml/) “

\>

<xsl:output method="xml"

doctype-system=" [http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\\](http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd/) “

doctype-public="-//W3C/DTD XHTML 1.0 Strict//EN"

indent="yes"/>

<xsl:template match="/\*">

<xsl:variable name="schema" select="//xsd:schema"/>

<xsl:variable name="tabletypename"

select="$schema/xsd:element\[@name=name(current())\]/@type"/>

<xsl:variable name="rowtypename"

select="$schema/xsd:complexType\[@name=$tabletypename\]/

xsd:sequence/xsd:element\[@name='row'\]/@type"/>

\<html>

\<head>

\<title><xsl:value-of select="name(current())"/>\</title>

\</head>

\<body>

\<table>

\<tr>

<xsl:for-each select="$schema/xsd:complexType\[@name=$rowtypename\]/

xsd:sequence/xsd:element/@name">

\<th><xsl:value-of select="."/>\</th>

</xsl:for-each>

\</tr>

<xsl:for-each select="row">

\<tr>

<xsl:for-each select="\*">

\<td><xsl:value-of select="."/>\</td>

</xsl:for-each>

\</tr>

</xsl:for-each>

\</table>

\</body>

\</html>

</xsl:template>

</xsl:stylesheet>

## JSON 函数和操作符

本节描述:

• 用于处理和创建JSON数据的函数和运算器

• SQL/JSON路径语言

要了解有关SQL/JSON标准的更多信息，请参阅\[sqltr-19075-6\]。有关瀚高数据库中支持的 JSON类型的详细信息，见第 7.14 节.

### 处理和创建JSON数据

表 8.44展示了可以用于 JSON 数据类型（见第 7.14 节）的操作符。

| **操作符** | **右操作数类型** | **返回类型** | **描述** | **例子** | **例子结果** |
| --- | --- | --- | --- | --- | --- |
| \-> | int | json or jsonb | 获得 JSON 数组元素（索引从 0 开始，负整数从末尾开 始计） | ‘\[{“a”:”foo”}, {“b”:”bar”}, {“c”:”baz”}\]’::json- >2 | {“c”:”baz”} |
| \-> | text | json or jsonb | 通过键获得 JSON 对象域 | ‘{“a”: {“b”:”foo”}}’::json- >’a’ | {“b”:”foo”} |
| \->> | int | text | 以text形式获 得 JSON 数组 元素 | ‘\[1,2,3\]’::json- >>2 | 3 |
| \->> | text | text | 以text形式获 得 JSON 对象 域 | ‘{“a”:1,”b”:2}’::json- >>’b’ | 2 |
| #> | text\[\] | json or jsonb | 获取在指定路 径的 JSON 对 象 | ‘{“a”: {“b”: {“c”: “foo”}}}’::json#>’{a,b}’ | {“c”: “foo”} |
| #>> | text\[\] | text | 以text形式获 取在指定路径 的 JSON 对象 | ‘{“a”: \[1,2,3\],”b”: \[4,5,6\]}’::json#>>’{a,2}’ | 3 |

: 表 8.44 json和jsonb 操作符

| 注意： |
| --- |
| 对json和jsonb类型，这些操作符都有其并行变体。 域/元素/路径抽取操作符返回与其左手输入（json或jsonb） 相同的类型，不过那些被指定为返回text的除外，它们的返回值会被强制为文本。如果该 JSON 输入没有匹配请求的正确结构（例如那样的元素不存在） ，这些域/元素/路径抽取操作符会返回 NULL 而不是失败。接受整数 JSON 数组下标的域/元素/路径抽取操作符都支持表示从数组末尾开始的负值下标形式。 |

表 8.1中展示的标准比较操作符只对 jsonb有效，而不适合json。它们遵循在第 7.14.4 节中给出的 B 树操作规则。

如表 8.45中所示，还存在一些只适合 jsonb的操作符。这些操作符中的很多可以用jsonb操作符类索引。jsonb包含和存在语义的完整描述可参见第 7.14.3 节。第 7.14.4 节描述了如何用这些操作符来有效地索引jsonb数据。

| **操作符** | **右操作数类型** | **描述** | **例子** |
| --- | --- | --- | --- |
| @> | jsonb | 左边的 JSON 值是否 在顶层包含右边的 JSON 路径/值项？ | ‘{“a”:1, “b”:2}’::jsonb @> ‘{“b”:2}’::jsonb |
| <@ | jsonb | 左边的 JSON 路径/值项是否被包含在右边的 JSON 值的顶层？ | ‘{“b”:2}’::jsonb <@ ‘{“a”:1, “b”:2}’::jsonb |
| ? | text | 键/元素字符串是否存在于 JSON 值的顶 层？ | ‘{“a”:1, “b”:2}’::jsonb? ‘b’ |
| ?\| | text\[\] | 这些数组字符串中的 任何一个是否做为顶 层键存在？ | ‘{“a”:1, “b”:2, “c”:3}’::jsonb?\| array\[‘b’, ‘c’\] |
| ?& | text\[\] | 是否所有这些数组字 符串都作为顶层键存 在？ | ‘\[“a”, “b”\]’::jsonb?& array\[‘a’, ‘b’\] |
| \|\| | jsonb | 把两个jsonb值串接成一个新的jsonb值 | ‘\[“a”, “b”\]’::jsonb \|\| ‘\[“c”, “d”\]’::jsonb |
| \- | text | 从左操作数删除键/值对或者string 元素。键/值对基于它们的键值来匹配。 | ‘{“a”: “b”}’::jsonb - ‘a’ |
| \- | text\[\] | 从左操作数中删除多 个键/值对或者string元素。键/值 对基于它们的键值来 匹配。 | ‘{“a”: “b”, “c”: “d”}’::jsonb - ‘{a,c}’::text\[\] |
| \- | integer | 删除具有指定索引 （负值表示倒数）的 数组元素。如果 顶层容器不是数组则抛出一个错误。 | ‘\[“a”, “b”\]’::jsonb - 1 |
| #- | text\[\] | 删除具有指定路径的 域或者元素（对于 JSON 数组，负值 表 示倒数） | ‘\[“a”, {“b”:1}\]’::jsonb #- ‘{1,b}’ |
| @? | jsonpath | JSON路径是否返回指 定的JSON值的任何项目？ | ‘{“a”: \[1,2,3,4,5\]}’::jsonb @? ‘$.a\[\*\]? (@ > 2)’ |
| @@ | jsonpath | 返回指定的JSON路径谓词检查结果。只考虑结果的第一项。 如果结果不是布尔值，那么返回 null 。 | ‘{“a”: \[1,2,3,4,5\]}’::jsonb @@ ‘$.a\[\*\] > 2’ |

: 表 8.45 额外的jsonb操作符

| **注意：** |
| --- |
| 操作符将其每一个操作数的顶层的元素串接起来。它不会递归操作。例如，如果两个操作数都是具有公共域名称的对象，结果中的域值将只是来自右手操作数的值。 如，如果两个操作数都是具有公共域名称的对象，结果中的域值将 只是来自右手操作数的值。 |

| **注意：** |
| --- |
| @?和@@@操作符会抑制以下错误：缺乏对象字段或数组元素、意外的JSON项类型和数字错误。当搜索不同结构的JSON文档集合时，这种行为可能会有帮助。 |

表 8.46展示了可用于创建 json 和 jsonb值的函数（没有用于 jsonb的与row\_to\_json和array\_to\_json等价的函数。不过，to\_jsonb函数 提供了这些函数的很大一部分相同的功能）。

| **函数** | **描述** |
| --- | --- |
| to\_json(anyelement) to\_jsonb(anyelement) | 把该值返回为json或 者jsonb。数组和组合会被（递归）转换成 数组和对象；对于不是数组和组合的值，如果有从该类型到json的造型，造型函数将被用来执行该转换；否则将产生一个标量值。对于任何不是数字、布尔、空值的标量类型，将使用文本表达，在这种风格下它是一个合法 的 json或 者jsonb值 |
| array\_to\_json(anyarray \[, pretty\_bool\]) | 把数组作为一个 JSON 数组返回。一个 瀚高数据库 多维数组 会成为一个数组 的 JSON 数组。如 果pretty\_bool为真， 将在 第 1 维度的元素之间增加换行。 |
| row\_to\_json(record \[, pretty\_bool\]) | 把行作为一个 JSON 对象返回。如果pretty\_bool为真，将在第1层元素之间增加换行。 |
| json\_build\_array(VARIADIC “any”) jsonb\_build\_array(VARIADIC “any”) | 从一个可变参数列表构造一个可能包含异质类型的 JSON 数组 |
| json\_build\_object(VARIADIC “any”) jsonb\_build\_object(VARIADIC “any”) | 从一个可变参数列表构造一个 JSON 对象。通过转换，该参数列表由交替出现的键和值构成。 |
| json\_object(text\[\]) jsonb\_object(text\[\]) | 从一个文本数组构造 一个 JSON 对象。该数组必须可以是具有偶数个成员的一维数组（成员被当做交替出现的键/值对），或者是一个二维数组（每一个内部数组刚好有 2 个元素，可以被看做是键/值对）。 |
| json\_object(keys text\[\], values text\[\]) jsonb\_object(keys text\[\], values text\[\]) | json\_object的这种形式从两个独立的数组得到键/值对。在其他方面和一个参数的形式相同。 |

表 8.46 JSON 创建函数

| **注意：** |
| --- |
| array\_to\_json和row\_to\_json与to\_json 具有相同的行为，不过它们提供了更好的打印选项。针对to\_json所描述的行为同样也适用于由其他 JSON 创建函数转换的每个值。 |

| **注意：** |
| --- |
| hstore扩展有一个从hstore到json 的造型，因此通过 JSON 创建函数转换的hstore值将被表示为 JSON 对象，而不是原始字符串值。 |

表 8.47展示了可用来处理json 和jsonb值的函数。

| **函数** | **返回值** | **描述** | **例子** | **例子结果** |
| --- | --- | --- | --- | --- |
| json\_array\_length(json) jsonb\_array\_length(jsonb) | Int | 返回最外层 JSON 数组中的元素数 量。 | json\_array\_length(‘\[1,2,3, {“f1”:1,”f2”: \[5,6\]},4\]’) | 5 |
| json\_each(json) jsonb\_each(jsonb) | setof key text, value json setof key text, value jsonb | 扩展最外层的 JSON 对象成为一 组键/值对。 | select \* from json\_each(‘{“a”:”foo”, “b”:”bar”}’) | key \| value —–+——- a \| “foo” b \| “bar |
| json\_each\_text(json) jsonb\_each\_text(jsonb) | setof key text, value text | 扩展最外层的 JSON 对象成为一 组键/值对。返回值将是text类 型。 | select \* from json\_each\_text(‘{“a”:”foo”, “b”:”bar”}’) | key \| value —–+——-a \| foo b \| bar |
| json\_extract\_path(from\_json json, VARIADIC path\_elems text\[\]) jsonb\_extract\_path(from\_json jsonb, VARIADIC path\_elems text\[\]) | jsonb | 返回 由path\_elems指 向的 JSON 值 （等效于#>操作 符） | json\_extract\_path(‘{“f2”: {“f3”:1},”f4”: {“f5”:99,”f6”:”foo”}}’,’f4’) | {“f5”:99,”f6”:”foo”} |
| json\_extract\_path\_text(from\_json json, VARIADIC path\_elems text\[\]) jsonb\_extract\_path\_text(from\_json jsonb, VARIADIC path\_elems text\[\]) |  | 以text返回 由path\_elems指 向的 JSON 值 （等效于#>>操作 符）。 | json\_extract\_path\_text(‘{“f2”: {“f3”:1},”f4”: {“f5”:99,”f6”:”foo”}}’,’f4’, ‘f6’) |  |
| json\_object\_keys(json) jsonb\_object\_keys(jsonb) | text | 返回最外层 JSON 对象中的键集 合。 | json\_object\_keys(‘{“f1”:”abc”,”f2”: {“f3”:”a”, “f4”:”b”}}’) | json\_object\_keys —————— f1 f2 |
| json\_populate\_record(base anyelement, from\_json json) jsonb\_populate\_record(base anyelement, from\_json jsonb) | anyelement | 扩展from\_json中 的对象成一个 行，它的列匹配 由base定义的记 录类型（见下文 的注释）。 | select \* from json\_populate\_record(null::myrowtype, ‘{“a”: 1, “b”: \[“2”, “a b”\], “c”: {“d”: 4, “e”: “a b c”}}’) | a\| c —+———– +————- 1 \| {2,”a b”} \| (4,”a b c”) |
| json\_populate\_recordset(base anyelement, from\_json json) jsonb\_populate\_recordset(base anyelement, from\_json jsonb) | anyelement | 扩展from\_json中 最外的对象数组 为一个集合，该 集合的列匹配 由base定义的记 录类型。 | select \* from json\_populate\_recordset(null::myrowtype, ‘\[{“a”:1,”b”:2}, {“a”:3,”b”:4}\]’) | a\| b —+— 1 \| 2 3 \| 4 |
| json\_array\_elements(json) jsonb\_array\_elements(jsonb) | setof json setof jsonb | 把一个 JSON 数 组扩展成一个 JSON 值的集合。 | select \* from json\_array\_elements(‘\[1,true, \[2,false\]\]’) | alue ———– 1 true \[2,false\] |
| json\_array\_elements\_text(json) jsonb\_array\_elements\_text(jsonb) | setof json setof jsonb | 把一个 JSON 数 组扩展成一 个text值集合。 | select \* from json\_array\_elements\_text(‘\[“foo”, “bar”\]’) | ———– foo bar |
| son\_typeof(json) jsonb\_typeof(jsonb) | text | 把最外层的 JSON 值的类型作为一 个文本字符串返 回。可能的类型 是： object、array、string、number、 boolean以 及null。 | son\_typeof(‘-123.4’) | number |
| json\_to\_record(json) jsonb\_to\_record(jsonb | record | 从一个 JSON 对 象（见下文的注 解）构建一个任 意的记录。正如 所有返回record 的函数一样，调 用者必须用一 个AS子句显式地 定义记录的结 构。 | select \* from json\_to\_record(‘{“a”:1,”b”: \[1,2,3\],”c”: \[1,2,3\],”e”:”bar”,”r”: {“a”: 123, “b”: “a b c”}}’) as x(a int, b text, c int\[\], d text, r myrowtype) | c \| d \| r —+——— +———+— +————— 1 \| \[1,2,3\] \| {1,2,3} \| \| (123,”a b c”) |
| json\_to\_recordset(json) jsonb\_to\_recordset(jsonb) | record | 从一个 JSON 对 象数组（见下文 的注解）构建一 个任意的记录集 合。正如所有返 回record 的函数 一样，调用者必 须用一个AS子句 显式地定义记录 的结构。 | select \* from json\_to\_recordset(‘\[{“a”:1,”b”:”foo”}, {“a”:”2”,”c”:”bar”}\]’) as x(a int, b text); | a \| b —+—– 1 \| foo 2 \| |
| json\_strip\_nulls(from\_json json) jsonb\_strip\_nulls(from\_json jsonb) | jsonb | 返回from\_json， 其中所有具有空 值的 对象域都被 省略。其他空值 不动。 | json\_strip\_nulls(‘\[{“f1”:1,”f2”:null},2,null,3 | \[{“f1”:1,”f2”:null}, |
| jsonb\_set(target jsonb, path text\[\], new\_value jsonb\[,create\_missing boolean\]) | jsonb | 返回target，其 中由 path指定的 节用 new\_value替换， 如果 path指定的 项不存在并且 create\_missing为 真（默认为 true）则加上 new\_value。正如 面向路径的 操作 符一样，出现 在path中的 负整 数表示从 JSON 数组的末尾开始 数。 | jsonb\_set(‘\[{“f1”:1,”f2”:null},2,null,3\]’, ‘{0,f1}’,’\[2,3,4\]’, false) jsonb\_set(‘\[{“f1”:1,”f2”:null},2\]’, ‘{0,f3}’,’\[2,3,4\] | {“f1”: \[2,3,4\],”f2”:null},2,null,3\] \[{“f1”: 1, “f2”: null, “f3”: \[2, 3, 4\]}, 2\] |
| sonb\_insert(target jsonb, path text\[\], new\_value jsonb\[, insert\_after boolean\]) | jsonb | 返回被插入 了new\_value的target。 如果path指定 的target节在一 个 JSONB 数组中，new\_value将 被插入到目标之 前（insert\_after为false， 默认情况）或者 之后 （insert\_after为 真）。如 果path指定 的target节在一 个 JSONB 对象 内，则只有 当target不存在 时才插 入new\_value。对 于面向路径的操 作符来说，出现 在path中的负整 数表示从 JSON 数组的末尾开始 计数。 | jsonb\_insert(‘{“a”: \[0,1,2\]}’, ‘{a, 1}’, ‘“new\_value”‘) jsonb\_insert(‘{“a”: \[0,1,2\]}’, ‘{a, 1}’, ‘“new\_value”‘, true) | {“a”: \[0, “new\_value”, 1, 2\]} {“a”: \[0, 1, “new\_value”, 2\]} |
| jsonb\_pretty(from\_json jsonb) | text | 把from\_json返回 成一段 缩进后的 JSON 文本。 | jsonb\_pretty(‘\[{“f1”:1,”f2”:null},2,null,3\]’) | \[ { “f1”: 1, “f2”: null }, 2, null, 3 \] |
| jsonb\_path\_exists(target jsonb, path jsonpath \[, vars jsonb \[, silent bool\]\]) | targe | 检查JSON路径是 否为指定的JSON 值返回任何项 目。 | jsonb\_path\_exists(‘{“a”: \[1,2,3,4,5\]}’, ‘$.a\[\*\]? (@ >= $min && @ <= $max)’, ‘{“min”:2,”max”:4}’) | Ture |
| jsonb\_path\_match(target jsonb, path jsonpath \[, vars jsonb \[, silent bool\]\]) | Bool | 返回指定的JSON 路径谓词检查结 果。 只考虑结果 的第一项。 如果 结果不是布尔 值，则返 回null。 | jsonb\_path\_match(‘{“a”: \[1,2,3,4,5\]}’, ‘exists($.a\[\*\]? (@ >= $min && @ <= $max))’, ‘{“min”:2,”max”:4}’) | ture |
| jsonb\_path\_query(target jsonb, path jsonpath \[, vars jsonb \[, silent bool\]\]) | jsonb | 获取指定的JSON 值的JSON路径返 回的所有JSON 项。 | select \* from jsonb\_path\_query(‘{“a”: \[1,2,3,4,5\]}’, ‘$.a\[\*\]? (@ >= $min && @ <= $max)’, ‘{“min”:2,”max”:4}’) | jsonb\_path\_query —————— 2 3 4 |
| jsonb\_path\_query\_array(target jsonb, path jsonpath \[, vars jsonb \[, silent bool\]\]) | jsonb | 获取指定JSON路 径返回的所有 JSON项，并将结 果封装成数组。 | jsonb\_path\_query\_array(‘{“a”: \[1,2,3,4,5\]}’, ‘$.a\[\*\]? (@ >= $min && @ <= $max)’, ‘{“min”:2,”max”:4}’) | \[2, 3, 4\] |
| jsonb\_path\_query\_first(target jsonb, path jsonpath \[, vars jsonb \[, silent bool\]\]) | jsonb | 获取指定的JSON 值的第一个JSON 路径返回的JSON 项。 如果没有结 果，则返 回NULL。 | jsonb\_path\_query\_first(‘{“a”: \[1,2,3,4,5\]}’, ‘$.a\[\*\]? (@ >= $min && @ <= $max)’, ‘{“min”:2,”max”:4}’) | 2 |

: 表 8.47 JSON 处理

| **注意：** |
| --- |
| 很多这些函数和操作符将把 JSON 字符串中的 Unicode 转义转换成合适的单一字符。如果输入类型是jsonb，这就没有问题，因为该转换已经完成了。但是对于json 输入，这可能会导致抛出一个错误（如第 7.14 节所述）。 |

| **注意：** |
| --- |
| 函数 json\[b\]populate\_record,   json\[b\]populate\_recordset,   json\[b\]to\_record and json\[b\]to\_recordset   对JSON对象或对象数组进行操作，并提取与输出行类型的列名匹配的键相关的值。不对应于任何输出列名的对象字段将被忽略，不匹配任何对象字段的输出列将被填充为空。要将JSON值转换为输出列的SQL类型，需要依次应用以下规则:   • 在所有情况下，JSON空值都会被转换为SQL空值。   • 如果输出列的类型为json或jsonb，那么JSON值就会被完全复制。   • 如果输出的列是复合（行）类型，而JSON值是JSON对象，则通过递归应用这些规则，将该对象的字段转换为输出行类型的列。   • 同样，如果输出列是一个数组类型，而JSON值是一个JSON数组，则通过递归应用这些规则将JSON数组的元素转换为输出数组的元素。   • 否则，如果JSON值是一个字符串的字段，则该字符串的内容被送入列的数据类型的输入转换函数。   • 否则，将JSON值的普通文本表示方式送入该列的数据类型的输入转换函数。 虽然这些函数的例子使用了常量，但典型的用法是在FROM子句中引用一个表，并使用其中的json或jsonb列作为函数的参数。然后，提取的键值可以被引用到查询的其他部分，比如WHERE子句和目标列表。用这种方式提取多个值，比用每键操作符分别提取多个值可以提高性能 |

| 注意： |
| --- |
| jsonb\_set和jsonb\_insert的path参数中除最后一项之外的所有项都必须存在于target中。如果create\_missing为假，jsonb\_set的path参数的所有项都必须存在。如果这些条件不满足，则返回的target不会被改变。如果最后的路径项是一个对象键，在它不存在且给定了新值的情况下会创建它。如果最后的路径项是一个数组索引，为正值则表示从左边开始计数，为负值表示从右边开始计数 - -1表示最右边的元素，以此类推。如果该项超过范围 -array\_length.. array\_length -1 并且 create\_missing 为真，则该项为负时把新值加载数组的开始处，而该项为正时把新值加在数组的末尾处。 |

| **注意：** |
| --- |
| 不要把json\_typeof函数的null返回值与 SQL 的 NULL弄混。 虽然调用json\_typeof('null'::json)将会返回null，但调用 json\_typeof(NULL::json)将会返回一个 SQL 的 NULL。 |

| 注意： |
| --- |
| 如果json\_strip\_nulls的参数在任何对象中包含重复的域名称， 结果在语义上可能有所不同，具体取决于它们发生的顺序。这不是 jsonb\_strip\_nulls的一个问题，因为jsonb值不能具有重复的对象域名称。 |

| 注意： |
| --- |
| jsonb\_path\_exists、jsonb\_path\_match、jsonb\_path\_query、jsonb\_path\_query\_array。   和 jsonb\_path\_query\_first函数有可选的vars和silent参数。   如果指定了vars参数，它提供了一个包含命名的变量的对象，要替换到jsonpath表达式中。如果指定了silent参数，并且具有true值，那么这些函数将抑制与@?和@@操作符相同的错误。 |

也可参见第 8.20 节了解聚集函数json\_agg，它可以把记录值聚集成 JSON。还有聚集函数json\_object\_agg，它可以把值对聚集成一个 JSON 对象。还有它们的jsonb等效体，jsonb\_agg和jsonb\_object\_agg.

### SQL/JSON路径语言

SQL/JSON路径表达式指定了要从JSON数据中检索的项目，类似于SQL访问XML时使用的XPath表达式。在瀚高数据库中，路径表达式作为jsonpath数据类型实现，可以使用第 8.14.6 节中描述的任何元素。

JSON查询函数和操作符将提供的路径表达式传递给路径引擎进行评估。如果表达式与被查询的JSON数据匹配，则返回相应的SQL/JSON项。路径表达式是用SQL/JSON路径语言编写的，也可以包括算术表达式和函数。查询函数将提供的表达式视为文本字符串，所以必须用单引号括起来。

一个路径表达式由jsonpath数据类型允许的元素序列组成。路径表达式从左至右进行评估，但你可以使用括号来改变操作顺序。如果评价成功，则会产生一个SQL/JSON项的序列（SQL/ JSON序列），并将评价结果返回给完成指定计算的JSON查询函数。

要引用要查询的JSON数据（context项），请在路径表达式中使用$符号。后面可以有一个或多个accessor操作符，它可以逐级递减JSON结构中的上下文项的内容。下面的每一个操作符都涉及到上一个评估步骤的结果。

例如，假设你有一些来自GPS追踪器的JSON数据，你想对其进行解析，例如:

{

"track": {

"segments": \[

{

"location": \[ 47.763, 13.4034 \],

"start time": "2018-10-14 10:05:14",

"HR": 73

},

{

"location": \[ 47.706, 13.2635 \],

"start time": "2018-10-14 10:39:21",

"HR": 135

}

\]

}

}

要检索可用的轨迹段，需要使用.key访问器操作符来检索前面所有的JSON对象。

'$.track.segments'

如果要检索的项目是一个数组的元素，你必须使用\[\*\]操作符来取消这个数组的嵌套。例如，下面的路径将返回所有可用的轨道段的位置坐标。

'$.track.segments\[\*\].location'

要只返回第一段的坐标，可以在\[\]访问器操作符中指定相应的下标。请注意，SQL/JSON数组是0相关的:

'$.track.segments\[0\].location'

每个路径评估步骤的结果可以由一个或多个jsonpath操作符和第 9.15.2.3 节中列出的方法处理。每个方法名称前必须有一个点。例如，你可以得到一个数组大小:

'$.track.segments.size()'

关于在路径表达式中使用jsonpath操作符和方法的更多示例，请参见 第 9.15.2.3 节.

在定义路径时，你还可以使用一个或多个过滤表达式，其工作原理类似于SQL中的WHERE子句。一个过滤表达式以问号开头，并在括号中提供一个条件:

? (condition)

筛选表达式必须在应用于路径评估步骤之后立即指定。这个步骤的结果被过滤，只包括那些满足所提供条件的项。SQL/JSON定义了三值逻辑，所以条件可以是true、false或unknown。unknown值的作用与SQL的NULL相同，可以用is unknown谓词来测试。进一步的路径评估步骤只使用那些过滤表达式返回true的项目。

在表 9.49中列出了可以在过滤表达式中使用的函数和操作符。要过滤的路径评价结果由@变量表示。要引用存储在较低嵌套层的JSON元素，可以在@之后添加一个或多个访问符操作符。

假设你想检索所有心率值大于130的心率值。你可以用下面的表达式来实现:

'$.track.segments\[\*\].HR? (@ > 130)'

如果要得到带有这样的值的段的起始时间，需要在返回起始时间之前过滤掉不相关的段，所以过滤表达式应用于上一步，条件中使用的路径不同:

'$.track.segments\[\*\]? (@.HR > 130)."start time"'

如果需要，你可以在同一个嵌套层上使用多个过滤表达式。例如，下面的表达式选择所有包含有相关坐标和高心率值的位置的位置段，并选择了以下表达式:

'$.track.segments\[\*\]? (@.location\[1\] < 13.4)? (@.HR > 130)."start time"'

也允许使用不同嵌套级别的过滤表达式。下面的例子首先按位置过滤所有的段，然后返回这些段的高心率值，如果可用的话:

'$.track.segments\[\*\]? (@.location\[1\] < 13.4).HR? (@ > 130)'

你也可以在彼此之间嵌套过滤表达式:

'$.track? (exists(@.segments\[\*\]? (@.HR > 130))).segments.size()'

该表达式返回轨道的大小，如果它包含任何具有高心跳值的片段，则返回轨道的大小，否则返回空序列。

瀚高数据库的SQL/JSON路径语言的实现与SQL/JSON标准有以下偏差。

•.datetime()项方法还没有实现，这主要是因为不可变的jsonpath函数和操作符不能引用会话时区，而这是在一些日期时间操作中使用的。

• 路径表达式可以是一个布尔谓词，尽管SQL/JSON标准只允许在过滤器中使用谓词。 这对于实现@@操作符是必要的。例如，下面的jsonpath表达式在瀚高数据库中有效。

'$.track.segments\[\*\].HR < 70'

• 第 9.15.2.2 节中描述的like\_regex过滤器中使用的正则表达式模式的解释有一些小的差异。

#### 严格和宽松模式

当你查询JSON数据时，路径表达式可能与实际的JSON数据结构不匹配。试图访问一个对象或数组元素中不存在的成员，会导致结构错误。SQL/JSON路径表达式有两种模式来处理结构性错误。

• lax (默认值) — 路径引擎隐式地将被查询的数据适应指定的路径。任何剩余的结构性错误都会被压制并转换为空的SQL/JSON序列。

• 严格的—如果发生结构性错误，则会提出错误。

宽松模式方便了JSON文档结构和路径的匹配。如果JSON数据不符合预期的模式，那么就会使用JSON表达式。如果一个操作项不符合特定操作的要求。它可以被自动包装成一个SQL/ JSON数组，或者通过 将其元素转换为SQL/JSON序列，然后再执行这个操作。此外，比较操作者会自动解开他们的运算子在宽松模式下，所以你可以比较SQL/JSON数组中的开箱即用。一个大小为1的数组被认为等于它的唯一元素。自动解包并不是只有在以下情况下才会执行。

• 路径表达式包含type()或size()方法，这些方法分别返回数组中的类型和元素数量。

• 被查询的JSON数据包含嵌套数组。在这种情况下，只有最外层的数组被解包，而所有内部数组保持不变。因此，在每个路径评估步骤中，隐式解包只能往下走一层。

例如，在查询上面列出的GPS数据时，可以抽象出它在使用宽松模式时存储了一个数组段的事实。

'lax $.track.segments.location'

在严格模式下，指定的路径必须与被查询的JSON文档的结构完全匹配才能返回一个SQL/JSON项，所以使用这个路径表达式会导致错误。为了得到与宽松模式下相同的结果，你必须显式地解包segments数组。

'strict $.track.segments\[\*\].location'

#### 正则表达式

SQL/JSON路径表达式允许用like\_regex过滤器将文本匹配到正则表达式。 例如，下面的SQL/JSON路径查询将对数组中所有以英文元音开头的字符串进行大小写匹配。

'$\[\*\]? (@ like\_regex "^\[aeiou\]" flag "i")'

可选的flag字符串可以包括一个或多个字符i，用于不区分大小写的匹配，m允许^和$在换行处匹配，s允许. 匹配一个新行，而q引用整个模式（将行为还原为简单的子串匹配）。

SQL/JSON标准借用了正则表达式的定义。LIKE\_REGEX操作符，而该操作符又使用了 XQuery标准。 瀚高数据库目前不支持 LIKE\_REGEX运算符。 因此。 like\_regex 过滤器是用 POSIX正则表达式引擎在 第 9.7.3 节。 这导致了各种小的 与标准SQL/JSON行为的差异，这些差异在 第 9.7.3.8 节。但是，请注意，这里所描述的旗帜-字母不兼容的问题不适用于SQL/ JSON，因为它将XQuery标志字母转换为 匹配POSIX引擎的期望值。

请记住，like\_regex的模式参数是一个JSON路径字符串字段，根据第 8.14.6 节中给出的规则编写。 这特别意味着，你想在正则表达式中使用的任何反斜线必须是双倍的。例如，要匹配只包含数字的字符串。

'$? (@ like\_regex "^\\\\d+$")'

#### SQL/JSON路径操作符和方法

表 8.48显示了jsonpath中的操作符和方法。 表 8.49显示了可用的过滤器表达式元素。

| **运算符和方法** | **描述** | **JSON举例** | **Query举例** | **结果** |
| --- | --- | --- | --- | --- |
| \+ (unary) | 加号运算符，可 对SQL/JSON序列进行迭代。 | {“x”: \[2.85, -14.7, -9.4\]} | \+ $.x.floor() | 2, -15, -10 |
| \- (unary) | 对SQL/JSON序列 进行迭代的减法 运算器 | {“x”: \[2.85, -14.7, -9.4\]} | \- $.x.floor() | \-2, 15, 10 |
| \+ (binary) | 加号 | \[2\] | 2 + $\[0\] | 4 |
| \- (binary) | 减号 | \[2\] | 4 - $\[0\] | 2 |
| \* | 乘号 | \[4\] | 2 \* $\[0\] | 8 |
| / | 除号 | \[8\] | $\[0\] / 2 | 4 |
| % | 取模 | \[32\] | $\[0\] % 10 | 2 |
| type() | SQL/JSON项的类型 | \[1, “2”, {}\] | $\[\*\].type() | “number”, “string”, “object” |
| size() | SQL/JSON项的大小 | {“m”: \[11, 15\]} | $.m.size() | 2 |
| double() | 由SQL/JSON数字或字符串转换而来的近似浮点数 | {“len”: “1.9”} | $.len.double() \* 2 | 3.8 |
| ceiling() | 大于或等于SQL/ JSON数的最近整数 | {“h”: 1.3} | $.h.ceiling() | 2 |
| floor() | 小于或等于SQL/ JSON数的最近整数 | {“h”: 1.3} | $.h.floor() | 1 |
| abs() | SQL/JSON号的绝对值 | {“z”: -0.3} | $.z.abs() | 0.3 |
| keyvalue() | 对象的键-值对的序列，用包含三个字段的数组来表示。 (“key”, “value”, 和 “id”). “id” 是 键-值对所属对象的唯一标识符。 | {“x”: “20”, “y”: 32} | $.keyvalue() | {“key”: “x”, “value”: “20”, “id”: 0}, {“key”: “y”, “value”: 32, “id”: 0}\*\*\*\* |

: 表 8.48 jsonpath 运算符和方法

| **值/谓语** | **描述** | **JSON举例** | **Query举例** | **结果** |
| --- | --- | --- | --- | --- |
| \== | 等号运算符 | \[1, 2, 1, 3\] | $\[\*\]? (@ == 1) | 1, 1 |
| != | 不等号运算符 | \[1, 2, 1, 3\] | $\[\*\]? (@!= 1) | 2, 3 |
| <> | 不等号运算符 (same as!=) | \[1, 2, 1, 3\] | $\[\*\]? (@ <> 1) | 2, 3 |
| < | 小于运算符 | \[1, 2, 3\] | $\[\*\]? (@ < 2) | 1 |
| <= | 小于等于运算符 | \[1, 2, 3\] | $\[\*\]? (@ <= 2) | 1, 2 |
| \> | 大于号运算符 | \[1, 2, 3\] | $\[\*\]? (@ > 2) | 3 |
| \>= | 大于等于运算符 | \[1, 2, 3\] | $\[\*\]? (@ >= 2) | 2, 3 |
| true | Value used to perform comparison with JSON true literal | \[{“name”: “John”, “parent”: false}, {“name”: “Chris”, “parent”: true}\] | $\[\*\]? (@.parent == true) | {“name”: “Chris”, “parent”: true} |
| false | Value used to perform comparison with JSON false literal | \[{“name”: “John”, “parent”: false}, {“name”: “Chris”, “parent”: true}\] | $\[\*\]? (@.parent == false) | {“name”: “John”, “parent”: false} |
| null | Value used to perform comparison with JSON null value | \[{“name”: “Mary”, “job”: null}, {“name”: “Michael”, “job”: “driver”}\] | $\[\*\]? (@.job == null).name | “Mary” |
| && | 布尔与 | \[1, 3, 7\] | $\[\*\]? (@ > 1 && @ < 5) | 3 |
| \|\| | 布尔或 | \[1, 3, 7\] | $\[\*\]? (@ < 1 \|\| @ > 5) | 7 |
| ! | 布尔非 | \[1, 3, 7\] | $\[\*\]? (!(@ < 5)) | 7 |
| like\_regex | 测试第一个操作项是否与第二个操作项给出的正则表达式相匹配，可选择用flag字符串描述的修改（见第 8.15.2.2 节）。 | \[“abc”, “abd”, “aBdC”, “abdacb”, “babc”\] | $\[\*\]? (@ like\_regex “^ab.\*c” flag “i”) | “abc”, “aBdC”, “abdacb” |
| starts with | 测试第二个执行项是否是第一个执行项的初始子串。 | \[“John Smith”, “Mary Stone”, “Bob Johnson”\] | $\[\*\]? (@ starts with “John”) | “John Smith” |
| exists | 测试一个路径表达式是否至少匹配一个SQL/JSON 项。 | {“x”: \[1, 2\], “y”: \[2, 4\]} | strict $.\*? (exists (@? (@\[\*\] > 2))) | 2, 4 |
| is unknown | 测试一个布尔条件是否是 unknown | \[-1, 2, 7, “infinity”\] | $\[\*\]? ((@ > 0) is unknown) | “infinity” |

: 表 8.49 jsonpath 筛选表达式元素

## 序列操作函数

本节描述用于操作序列对象的函数，序列对象也被称为序列生成器或者就是序列。序列对象都是用CREATE SEQUENCE创建的特殊的单行表。序列对象通常用于为表的行生成唯一的标识符。表 8.50中列出的这些序列函数，可以为我们从序列对象中获取连续的序列值提供了简单的、多用户安全的方法。

| **函数** | **返回类型** | **描述** |
| --- | --- | --- |
| currval(regclass) | bigint | 返回最近一次用nextval获取的指定序列的值 |
| lastval() | bigint | 返回最近一次用nextval获取的任何序列的值 |
| nextval(regclass) |  | 递增序列并返回新值 |
| setval(regclass, bigint) |  | 设置序列的当前值 |
| setval(regclass, bigint, boolean) |  | 设置序列的当前值以 及is\_called标志 |

: 表 8.50 序列函数

将要由序列函数调用操作的序列是用一个regclass参数声明的，它只是序列在pg\_class系统表里面的 OID。不过，你不需要手工查找 OID， 因为regclass数据类型的输入转换器会帮你做这件事情。只要写出用单引号包围的序列名字即可，因此它看上去像文本常量。为了和普通SQL名字处理兼容，这个字串将转换成小写形式，除非在序列名字周围包含双引号。

因此：

nextval('foo') 操作序列foo

nextval('FOO') 操作序列foo

nextval('"Foo"') 操作序列Foo

必要时序列名可以用模式限定∶

nextval('myschema.foo') 操作myschema.foo

nextval('"myschema".foo') 同上

nextval('foo') 在搜索路径中查找foo

参阅第 7.19 节获取有关regclass的更多信息。

| 注意： |
| --- |
| 当你把一个序列函数的参数写成一个无修饰的文字串，那么它将变成类型为regclass的常量。因为这只是一个 OID，它将跟踪最初标识的序列，而不管后面是否改名、模式变化等等。 这种”早期绑定”的行为通常是列默认值和视图中引用的序列所需要的。 但是有时候你可能想要”延迟绑定”，其中序列的引用是在运行时解析的。要得到延迟绑定的行为，我们可以强制常量被存储为text常量，而不是regclass：nextval('foo'::text) foo在运行时查找当然，序列函数的参数也可以是表达式。如果它是一个文本表达式，那么隐式的转换将导致运行时的查找。 |

可用的序列函数有∶

nextval

递增序列对象到它的下一个值并且返回该值。这个动作是自动完成的： 即使多个会话并发执行nextval，每个进程也会安全地收到一个唯一的序列值。

如果一个序列对象是用默认参数创建的，连续的nextval调用将会返回从 1 开始的连续的值。其他的行为可以通过在CREATE SEQUENCE命令中使用特殊参数来获得；详见该命令的参考页。

| 重要： |
| --- |
| 为了避免阻塞从同一个序列获取序号的并发事务，nextval操作从来不会被回滚。也就是说，一旦一个值被取出就视同被用掉并且不会被再次返回给调用者，即便调用该操作的外层事务后来中止或者调用查询后来没有使用取得的值也是这样。例如一个带有ON CONFLICT子句的INSERT会计算要被插入的元组，其中可能就包括调用nextval，然后才会检测到导致它转向ON CONFLICT规则的冲突。这种情况就会在已分配值的序列中留下未被使用的”空洞”。因此，瀚高数据库的序列对象不能被用来得到”无间隙”的序列。 |

这个函数要求序列上的USAGE或者UPDATE特权。

currval

在当前会话中返回最近一次nextval取到的该序列的值（如果在本会话中从未在该序列上调用过nextval，那么会报告一个错误）。请注意因为此函数返回一个会话本地的值，不论其它会话是否在当前会话之后执行过nextval，它都能给出一个可预测的回答。

这个函数要求序列上的USAGE或者SELECT特权。

lastval

返回当前会话里最近一次nextval返回的值。 这个函数等效于currval，只是它不用序列名作为参数， 它会引用当前会话里面最近一次被应用的序列的nextval。如果当前会话还没有调用过nextval，那么调用lastval会报错。

这个函数要求上一次使用的序列上的USAGE或者SELECT特权。

setval

重置序列对象的计数器值。双参数的形式设置序列的last\_value域为指定值并且将其is\_called域设置为true，表示下一次nextval将在返回值之前递增该序列。currval报告的值也被设置为指定的值。在三参数形式里，is\_called可以设置为true或false。true具有和双参数形式相同的效果。如果你把它设置为false，那么下一次nextval将返回指定的值，而从随后的nextval才开始递增该序列。此外，在这种情况中currval报告的值不会被改变。 例如：

SELECT setval('foo', 42); 下一次nextval会返回 43

SELECT setval('foo', 42, true); 同上

SELECT setval('foo', 42, false); 下一次nextval将返回 42

setval返回的结果就是它的第二个参数的值。

| **重要：** |
| --- |
| 因为序列是非事务的，setval造成的改变不会由于事务的回滚而撤销。 |

这个函数要求序列上的UPDATE特权。

## 条件表达式

本节描述在瀚高数据库中可用的SQL兼容的条件表达式。

| **提示：** |
| --- |
| 如果你的需求超过这些条件表达式的能力，你可能会希望用一种更富表现力的编程语言写一个服务器端函数。 |

| 注意： |
| --- |
| 尽管COALESCE、GREATEST和LEAST在语法上类似于函数，但它们不是普通的函数，因此不能使用显式VARIADIC数组参数。 |

### CASE

SQL CASE表达式是一种通用的条件表达式，类似于其它编程语言中的 if/else 语句：

CASE WHEN condition THEN result

\[WHEN...\]

\[ELSE result\]

END

CASE子句可以用于任何表达式可以出现的地方。每一个condition是一个返回boolean结果的表达式。如果结果为真，那么CASE表达式的结果就是符合条件的result，并且剩下的CASE表达式不会被处理。如果条件的结果不为真，那么以相同方式搜寻任何随后的WHEN子句。如果没有WHEN condition为真，那么CASE表达式的值就是在ELSE子句里的result。如果省略了ELSE子句而且没有条件为真，结果为空。

例子：

SELECT \* FROM test;

a

\---

1

2

3

SELECT a,

CASE WHEN a=1 THEN 'one'

WHEN a=2 THEN 'two'

ELSE 'other'

END

FROM test;

a | case

\---+-------

1 | one

2 | two

3 | other

所有result表达式的数据类型都必须可以转换成单一的输出类型。 参阅第 10.5 节获取细节。

下面这个”简单”形式的CASE表达式是上述通用形式的一个变种：

CASE expression

WHEN value THEN result

\[WHEN...\]

\[ELSE result\]

END

第一个expression会被计算，然后与所有在WHEN子句中的每一个value对比，直到找到一个相等的。如果没有找到匹配的，则返回在ELSE子句中的result（或者控制）。 这类似于C里的switch语句。

上面的例子可以用简单CASE语法来写：

SELECT a,

CASE a WHEN 1 THEN 'one'

WHEN 2 THEN 'two'

ELSE 'other'

END

FROM test;

a | case

\---+-------

1 | one

2 | two

3 | other

CASE表达式并不计算任何无助于判断结果的子表达式。例如，下面是一个可以避免被零除错误的方法：

SELECT... WHERE CASE WHEN x <> 0 THEN y/x > 1.5 ELSE false END;

| 注意： |
| --- |
| 如第 4.2.14 节中所述，在有几种情况中一个表达式的子表达式会被计算多次，因此”CASE只计算必要的表达式”这一原则并非不可打破。例如一个常量子表达式1/0通常将会在规划时导致一次除零错误，即便它位于一个执行时永远也不会进入的CASE分支时也是如此。 |

### COALESCE

COALESCE(value \[,...\])

COALESCE函数返回它的第一个非空参数的值。当且仅当所有参数都为空时才会返回空。它常用于在为显示目的检索数据时用缺省值替换空值。例如：

SELECT COALESCE(description, short\_description, '(none)')...

如果description不为空，这将会返回它的值，否则如果short\_description非空则返回short\_description的值，如果前两个都为空则返回(none)。

和CASE表达式一样，COALESCE将不会 计算无助于判断结果的参数；也就是说，在第一个非空参数右边的参数不会被计算。这个 SQL 标准函数提供了类似于NVL和IFNULL的能力，它们被用在某些其他数据库系统中。

### NULLIF

NULLIF(value1, value2)

当value1和value2相等时，NULLIF返回一个空值。 否则它返回value1。 这些可以用于执行前文给出的COALESCE例子的逆操作：

SELECT NULLIF(value, '(none)')...

在这个例子中，如果value是(none)，将返回空值，否则返回value的值。

### GREATEST和LEAST

GREATEST(value \[,...\])

LEAST(value \[,...\])

GREATEST和LEAST函数从一个任意的数字表达式列表里选取最大或者最小的数值。 这些表达式必须都可以转换成一个普通的数据类型，它将会是结果类型 （参阅第 10.5 节获取细节）。列表中的 NULL 数值将被忽略。只有所有表达式的结果都是 NULL 的时候，结果才会是 NULL。

请注意GREATEST和LEAST都不是 SQL 标准，但却是很常见的扩展。某些其他数据库让它们在任何参数为 NULL 时返回 NULL，而不是在所有参数都为 NULL 时才返回 NULL。

## 数组函数和操作符

表 8.51显示了可以用于数组类型的操作符。

| **操作符** | **描述** |
| --- | --- |
| \= | 等于 |
| <> | 不等于 |
| < | 小于 |
| \> | 大于 |
| <= | 小于等于 |
| \>= | 大于等于 |
| @> | 包含 |
| <@ | 被包含 |
| && | 重叠（具有公共元素） |
| \|\| | 数组和数组串接 |
| \|\| | 数组和数组串接 |
| \|\| | 元素到数组串接 |
| \|\| | 数组到元素串接 |

: 表 8.51 数组操作符

数组排序操作符（<、>=等）对数组内容进行逐个元素的比较，使用默认的元素数据类型的 B-tree比较函数，并根据第一个差值进行排序。 多维数组的元素按照行序进行访问（最后的下标变化最快）。如果两个数组的内容相同但维数不等，那么维度信息中的第一个不同将决定排序顺序。

数组包含操作符（<@和@>）认为，如果一个数组的每一个元素出现在另一个数组中，那么这个数组就被包含在另一个数组中。重复数组不做特殊处理，因此ARRAY\[1\]和ARRAY\[1,1\]分别被认为包含了另一个数组。

参阅第 7.15 节获取有关数组操作符行为的更多细节。有关哪些操作符支持被索引的操作，请参阅第 10.2 节。

表 8.52展示了可以用于数组类型的函数。 参阅第 7.15 节获取更多信息以及使用这些函数的例子。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| array\_append(anyarray, anyelement) | array | 向一个数组的末端追加一个元素 | array\_append(ARRAY\[1,2\], 3) | \[1,2,3\] |
| array\_cat(anyarray, anyarray) | array | 连接两个数组 | array\_cat(ARRAY\[1,2,3\], ARRAY\[4,5\]) | {1,2,3,4,5} |
| array\_ndims(anyarray ) | int | 返回数组的维度 数 | array\_ndims(ARRAY\[\[1,2,3\], \[4,5,6\]\]) |  |
| array\_dims(anyarray) | text | 返回数组的维度 的文本表示 | array\_dims(ARRAY\[\[1,2,3\], \[4,5,6\]\]) | \[1:2\]\[1:3\] |
| array\_fill(anyelement, int\[\], \[, int\[\]\]) | array | 返回一个用提供 的值和维度初始 化好的数组，可 以选择下界不为 1 | array\_fill(7, ARRAY\[3\], ARRAY\[2\]) | \[2:4\]={7,7,7} |
| array\_length(anyarray, int) | int | 返回被请求的数 组维度的长度 | array\_length(array\[1,2,3\], 1) | 3 |
| array\_lower(anyarray, int) | int | 返回被请求的数 组维度的下界 | array\_lower(‘\[0:2\]={1,2,3}’::int\[\], 1) | 0 |
| array\_position(anyarray, anyelement \[, int\]) | array | 返回在该数组中 从第三个参数指 定的元素开始或 者 第一个元素开 始（数组必须是一维的）、第二 个参数的 第一次 出现的下标 | array\_position(ARRAY\[‘sun’,’mon’,’tue’,’wed’,’thu’,’fri’,’sat’\], ‘mon’) | 2 |
| array\_positions(anyarray, anyelement) | Int\[\] | 返回在第一个参 数给定的数组 （数组必须是一 维的）中， 第二 个参数所有出现 位置的下标组成 的数组 | array\_positions(ARRAY\[‘A’,’A’,’B’,’A’\], ‘A’) | {1,2,4} |
| array\_prepend(anyelement, anyarray) | array | 向一个数组的首 部追加一个元素 | array\_prepend(1, ARRAY\[2,3\]) | {1,2,3} |
| array\_remove(anyarray, anyelement) | array | 从数组中移除所 有等于给定值的 所有元素（数组 必须是一维的） | array\_remove(ARRAY\[1,2,3,2\], 2) | {3} |
| array\_replace(anyarray, anyelement, anyelement) | array | 将每一个等于给 定值的数组元素 替换成一个新值 | array\_replace(ARRAY\[1,2,5,4\], 5, 3) |  |
| array\_to\_string(anyarray, text \[, text\]) | array | 使用提供的定界 符和可选的空串 连接数组元素 | array\_to\_string(ARRAY\[1, 2, 3, NULL, 5\], ‘,’, ‘\*’) |  |
| array\_upper(anyarray, int) | int | 返回被请求的数 组维度的上界 | array\_upper(ARRAY\[1,8,3,7\], 1) | 4 |
| cardinality(anyarray int ) | int | 返回数组中元素 的总数，如果数 组为空则返回 0 | cardinality(ARRAY\[\[1,2\], \[3,4\]\]) | 4 |
| string\_to\_array(text, text \[, text\]) | Text\[\] | 使用提供的定界 符和可选的空串 将字符串划分成 数组元素 | string\_to\_array(‘xx ~~^~~ yy ~~^~~ zz’, ‘ ~~^~~ ‘, ‘yy’) |  |
| unnest(anyarray) | setof anyelement | 将一个数组扩展 成一组行 | unnest(ARRAY\[1,2\]) | 12 (2 rows) |
| unnest(anyarray, anyarray \[, …\]) | setof anyelement, anyelement \[, …\] | 把多维数组（可 能是不同类型） 扩展成一个行的 集合。 这只允许 用在 FROM 子句 中，见 第 6.2.1.4 节 | unnest(ARRAY\[1,2\] ARRAY\[‘foo’,’bar’,’baz’\]) | 1 foo 2 bar NULL baz (3 rows) |

: 表 8.52 数组函数

在array\_position和array\_positions中， 每一个数组元素都使用IS NOT DISTINCT FROM 语义与要搜索的值比较。

在array\_position中，如果值没有找到则返回 NULL。

在array\_positions中，只有当数组为 NULL时才返回NULL，如果该值没有在该数组中找到则返回一个空数组。

在string\_to\_array中，如果定界符参数为 NULL，输入字符串中的每一个字符将变成结果数组中的一个独立元素。如果定界符是一个空串，则整个输入字符串被作为一个单一元素的数组返回。否则输入字符串会被在每一个出现定界符字符串的位置分裂。

在string\_to\_array中，如果空值串参数被忽略或者为 NULL，输入中的子串不会被替换成 NULL。在array\_to\_string中，如果空值串参数被忽略或者为 NULL，该数组中的任何空值元素会被简单地跳过并且不会在输出串中被表示。

也可参见第 8.20 节了解用于数组的聚集函数array\_agg。

## 范围函数和操作符

范围类型的概述请见第 7.17 节。

表 8.53展示了范围类型可用的操作符。

| **操作符** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- |
| \= | 等于 | int4range(1,5) = ‘\[1,4\]’::int4range | t |
| <> | 不等于 | numrange(1.1,2.2) <> numrange(1.1,2.3) | t |
| < | 小于 | int4range(1,10) < int4range(2,3) | t |
| \> | 大于 | int4range(1,10) > int4range(1,5) | t |
| <= | 小于等于 | numrange(1.1,2.2) <= numrange(1.1,2.2) | t |
| \>= | 大于等于 | numrange(1.1,2.2) >= numrange(1.1,2.0) | t |
| @> | 包含范围 | int4range(2,4) @> int4range(2,3) | t |
| @> | 包含元素 | ‘\[2011-01-01,2011-03-01)’::tsrange @> ‘2011-01-10’::timestamp | t |
| <@ | 范围被包含 | int4range(2,4) <@ int4range(1,7) | t |
| <@ | 元素被包含 | 42 <@ int4range(1,7) | t |
| && | 重叠（有公共点） | int8range(3,7) && int8range(4,12) | t |
| << | 严格左部 | int8range(1,10) << int8range(100,110) | t |
| \>> | 严格右部 | int8range(50,60) >> int8range(20,30) | t |
| &< | 不超过右部 | int8range(1,20) &< int8range(18,20) | t |
| &> | 不超过左部 | int8range(7,20) &> int8range(5,10) | t |
| \-\|- | 相邻 | numrange(1.1,2.2) -\|- numrange(2.2,3.3) | t |
| + | 并 | numrange(5,15) + numrange(10,20) | \[5,20) |
| \* | 交 | int8range(5,15) \* int8range(10,20) | \[10,15) |
| \- | 差 | int8range(5,15) - int8range(10,20) | \[5,10) |

: 表 8.53 范围操作符

简单比较操作符<、 >、<=和 >=首先比较下界，并且只有在下界相等时才比较上界。这些比较通常对范围不怎么有用，但是还是提供它们以便能够在范围上构建B树索引。

当涉及一个空范围时，左部/右部/相邻操作符总是返回假；即一个空范围被认为不在任何其他范围前面或者后面。

如果结果范围可能需要包含两个分离的子范围，并和差操作符将会失败，因为这样的范围无法被表示。

表 8.54显示可用于范围类型的函数。

| **函数** | **返回类型** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- | --- |
| lower(anyrange) | 范围的元素类型 | 范围的下界 | lower(numrange(1.1,2.2)) |  |
| upper(anyrange) | 范围的元素类型 | 范围的上界 | upper(numrange(1.1,2.2)) |  |
| isempty(anyrange) | boolean | 范围为空？ | isempty(numrange(1.1,2.2)) | false |
| lower\_inc(anyrange) | boolean | 下界包含在内？ | lower\_inc(numrange(1.1,2.2)) | true |
| upper\_inc(anyrange) | boolean | 上界包含在内？ | upper\_inc(numrange(1.1,2.2)) | false |
| lower\_inf(anyrangen) | boolean | 下界无限？ | lower\_inf(‘(,)’::daterange) | true |
| upper\_inf(anyrange) | boolean | 上界无限？ | upper\_inf(‘(,)’::daterange) | true |
| range\_merge(anyrange, anyrange) | anyrange | 包含两个给定范 围的最小范围 | range\_merge(‘\[1,2)’::int4range, ‘\[3,4)’::int4range) | 1,4 |

: 表 8.54 范围函数

如果范围为空或者被请求的界是无限的，lower和upper函数返回空值。函数lower\_inc、upper\_inc、lower\_inf和upper\_inf对一个空范围全部返回假。

## 聚集函数

聚集函数从一个输入值的集合计算出一个单一值。内建的通用聚集函数在表 9.55中列出，而统计性聚集在表8.56中列出。内建的组内有序集聚集函数在表 9.57中列出，而内建的组内假想集聚集在表8.58中列出。与聚集函数紧密相关的分组操作在表 9.59中列出。第 4.2.7 节中会解释针对聚集函数的特殊语法考虑。额外的介绍信息请参考第 2.7 节

| **函数** | **参数类型** | **返回类型** | **部分模式** | **描述** |
| --- | --- | --- | --- | --- |
| array\_agg(expression) | 任何非数组类型 | 参数类型的数组 | No | 输入值（包括 空）被连接到一个数组 |
| array\_agg(expression) | 任意数组类型 | 和参数数据类型相同 | No | 输入数组被串接到一个更高维度的数组中 （输入必须都具有相同的维度并且不能为空或者 NULL） |
| avg(expression) | smallint, int, bigint、real、double precision、numeric或interva | 对于任何整数类 型参数 是numeric，对于 一个浮点参数 是double precision，否则 和参数数据类型 相同 | Yes | 所有非空输入值 的平均值（算术 平均） |
| bit\_and(expression) | smallint、int、bigint | 与参数数据类型 或bit 相同 | Yes | 所有非空输入值 的按位与，如果 没有非空值则结 果是空值 |
| bit\_or(expression) | smallint, int, bigint, or bit | 与参数数据类型 相同 | Yes | 所有非空输入值 的按位或，如果 没有非空值则结 果是空值 |
| bool\_and(expression) | bool | bool | Yes | 如果所有输入值 为真则结果为 真，否则为假 |
| bool\_or(expression) | bool | bool | Yes | 至少一个输入值 为真时结果为 真，否则为假 |
| count(\*) |  | bigint | Yes | 输入的行数 |
| count(expression) | any | bigint | Yes | expression值非 空的输入行的数 目 |
| every(expression) | bool | bool | Yes | 等价于bool\_and |
| json\_agg(expression) | any | json | No | 将值，包含空 值，聚集成一个 JSON 数组 |
| jsonb\_agg(expression) | any | jsonb | No | 把值，包含空 值，聚合成一个 JSON 数组 |
| json\_object\_agg(name, value) | (any, any) | json | No | 将名字/值对聚集 成一个 JSON 对 象，值可以为 空，但不能是名 字。 |
| jsonb\_object\_agg(name, value) | (any, any) | jsonb | No | 把名字/值对聚合 成一个 JSON 对 象，值可以为 空，但不能是名 字。 |
| max(expression) | 任意数组、数 字、串、日期/时 间、网络或者枚 举类型，或者这 些类型的数组 | 与参数数据类型 相同 | Yes | 所有非空输入值 中expression的 最大值 |
| min(expression) | 任意数组、数 字、串、日期/时 间、网络或者枚 举类型，或者这 些类型的数组 | 与参数数据类型 相同 | Yes | 所有非空输入值 中expression的 最小值 |
| string\_agg(expression, delimiter) | (text, text) 或 (bytea, bytea) | 与参数数据类型 相同 | No | 非空输入值连接 成一个串，用定 界符分隔 |
| sum(expression) | smallint、int、 bigint、real、double precision、numeric、 interval或money | 对smallint或int参 数是bigint， 对bigint参数 是numeric，否则 和参数数据类型 相同 | Yes | 所有非空输入值 的expression的 和 |
| xmlagg(expression) | xml | xml | No | 连接 非空 XML 值（参 见第 8.14.1.7 节） |

: 表 8.55 通用聚集函数

请注意，除了count以外，这些函数在没有行被选中时返回控制。尤其是sum函数在没有输入行时返回空值，而不是零，并且array\_agg在这种情况返回空值而不是一个空数组。必要时可以用coalesce把空值替换成零或一个空数组。

支持部分模式的聚集函数有资格参与到各种优化中，例如并行聚集。

| 注意： |
| --- |
| 布尔聚集bool\_and和bool\_or对应于标准的 SQL 聚集every和any或some。而对于any 和some，似乎在标准语法中有一个歧义：SELECT b1 = ANY((SELECT b2 FROM t2...)) FROM t1...;   如果子查询返回一行有一个布尔值的结果，这里的ANY可以被认为是引入一个子查询，或者是作为一个聚集函数。因而标准的名称不能指定给这些聚集。 |

| **注意：** |
| --- |
| 在把count聚集应用到整个表上时，习惯于使用其他 SQL 数据管理系统的用户可能会对它的性能感到失望。一个如下的查询：   SELECT count(\*) FROM sometable;   将会要求与整个表大小成比例的工作：瀚高数据库将需要扫描整个表或者整个包含表中所有行的索引。 |

与相似的用户定义的聚集函数一样，聚集函数array\_agg、 json\_agg、jsonb\_agg、json\_object\_agg、jsonb\_object\_agg、string\_agg和xmlagg会依赖输入值的顺序产生有意义的不同结果值。这个顺序默认是不用指定的，但是可以在聚集调用时使用ORDER BY子句进行控制，如第 4.2.7 节中所示。作为一种选择，从一个排序号的子查询来提供输入值通常会有帮助。例如：

SELECT xmlagg(x) FROM (SELECT x FROM test ORDER BY y DESC) AS tab;

注意如果外面的查询层次包含额外的处理（例如连接），这种方法可能会失败，因为这可能导致子查询的输出在计算聚集之前被重新排序。

表8.56展示了通常被用在统计分析中的聚集函数（这些被隔离出来是为了不和常用聚集混淆）。其中描述提到了N，它表示对应于所有非空输入表达式的输入行的数目。在所有情况中，如果计算是无意义的，将会返回空值，例如当N为零。

| **函数** | **参数类型** | **返回类型** | **部分模式** | **描述** |
| --- | --- | --- | --- | --- |
| array\_agg(expression) | 任何非数组类型 | 参数类型的数组 | No | 输入值（包括 空）被连接到一个数组 |
| array\_agg(expression) | 任意数组类型 | 和参数数据类型相同 | No | 输入数组被串接到一个更高维度的数组中 （输入必须都具有相同的维度并且不能为空或者 NULL） |
| avg(expression) | smallint, int, bigint、real、double precision、numeric或interva | 对于任何整数类 型参数 是numeric，对于 一个浮点参数 是double precision，否则 和参数数据类型 相同 | Yes | 所有非空输入值 的平均值（算术 平均） |
| bit\_and(expression) | smallint、int、bigint | 与参数数据类型 或bit 相同 | Yes | 所有非空输入值 的按位与，如果 没有非空值则结 果是空值 |
| bit\_or(expression) | smallint, int, bigint, or bit | 与参数数据类型 相同 | Yes | 所有非空输入值 的按位或，如果 没有非空值则结 果是空值 |
| bool\_and(expression) | bool | bool | Yes | 如果所有输入值 为真则结果为 真，否则为假 |
| bool\_or(expression) | bool | bool | Yes | 至少一个输入值 为真时结果为 真，否则为假 |
| count(\*) |  | bigint | Yes | 输入的行数 |
| count(expression) | any | bigint | Yes | expression值非 空的输入行的数 目 |
| every(expression) | bool | bool | Yes | 等价于bool\_and |
| json\_agg(expression) | any | json | No | 将值，包含空 值，聚集成一个 JSON 数组 |
| jsonb\_agg(expression) | any | jsonb | No | 把值，包含空 值，聚合成一个 JSON 数组 |
| json\_object\_agg(name, value) | (any, any) | json | No | 将名字/值对聚集 成一个 JSON 对 象，值可以为 空，但不能是名 字。 |
| jsonb\_object\_agg(name, value) | (any, any) | jsonb | No | 把名字/值对聚合 成一个 JSON 对 象，值可以为 空，但不能是名 字。 |
| max(expression) | 任意数组、数 字、串、日期/时 间、网络或者枚 举类型，或者这 些类型的数组 | 与参数数据类型 相同 | Yes | 所有非空输入值 中expression的 最大值 |
| min(expression) | 任意数组、数 字、串、日期/时 间、网络或者枚 举类型，或者这 些类型的数组 | 与参数数据类型 相同 | Yes | 所有非空输入值 中expression的 最小值 |
| string\_agg(expression, delimiter) | (text, text) 或 (bytea, bytea) | 与参数数据类型 相同 | No | 非空输入值连接 成一个串，用定 界符分隔 |
| sum(expression) | smallint、int、 bigint、real、double precision、numeric、 interval或money | 对smallint或int参 数是bigint， 对bigint参数 是numeric，否则 和参数数据类型 相同 | Yes | 所有非空输入值 的expression的 和 |
| xmlagg(expression) | xml | xml | No | 连接 非空 XML 值（参 见第 8.14.1.7 节） |

: 表 8.56 用于统计的聚集函数

表 8.57展示了一些使用 有序集聚集语法的聚集函数。这些函数有时也被称为 “逆分布”函数。

| **函数** | **直接参数类型** | **聚集参数类型** | **返回类型** | **部分模式** | **描述** |
| --- | --- | --- | --- | --- | --- |
| mode() WITHIN GROUP (ORDER BY sort\_expression) |  | 任何可排序类 型 | 与排序表达式 相同 | No | 返回最频繁的 输入值（如果 有多个频度相 同的值就选第 一个） |
| percentile\_cont(fraction) WITHIN GROUP (ORDER BY sort\_expression) | double precision | double precision或 者interval | 与排序表达式 相同 | No | 连续百分率： 返回一个对应 于排序中指定 分数的值，如 有必要就在相 邻的输入项之 间插值 |
| percentile\_cont(fractions) WITHIN GROUP(ORDER BY sort\_expression) | (fractions) precision\[\] | double precision或 者interval | 排序表达式的 类型的数组 | No | 多重连续百分 率：返回一个 匹配fractions参 数形状的结果 数组， 其中 每一个非空元 素都用对应于 那个百分率的 值替换 |
| percentile\_disc(fraction) WITHIN GROUP (ORDER BY sort\_expression) | double(fractions) | 一种可排序类 型 | 与排序表达式 相同 | No | 离散百分率： 返回第一个在 排序中位置等 于或者超过指 定分数的输入 值 |
| percentile\_disc(fractions) WITHIN GROUP (ORDER BY sort\_expression) | (fractions) precision\[\] | 任何可排序类 型 | 排序表达式的 类型的数组 | No | 多重离散百分 率：返回一个 匹配fractions参 数形状的结果 数组， 其中 每一个非空元 素都用对应于 那个百分率的 输入值替换 |

: 表 8.57 有序集聚集函数

所有列在表 8.57中的聚集会忽略它们的已排序输入中的空值。对那些有一个fraction参数的聚集来说，该分数值必须位于 0 和 1 之间，否则会抛出错误。不过，一个空分数值会产生一个空结果。

每个列在表 8.58中的聚集都与一个定义在第 8.21 节中的同名窗口函数相关联。

在每种情况中，聚集结果的计算方法是：假设根据args构建的”假想”行已经被增加到从sorted\_args计算得到的已排序行分组中， 然后用相关联的窗口函数针对该行返回的值就是聚集的结果。

| **函数** | **直接参数类型** | **聚集参数类型** | **返回类型** | **部分模式** | **描述** |
| --- | --- | --- | --- | --- | --- |
| rank(args) WITHIN GROUP (ORDER BY sorted\_args) | VARIADIC “any” | VARIADIC “any” | bigint | No | 假想行的排 名，为重复的 行留下间隔 |
| dense\_rank(args) WITHIN GROUP (ORDER BY sorted\_args) | VARIADIC “any” | VARIADIC “any” | bigint | No | 假想行的排 名，不留间隔 |
| percent\_rank(args) WITHIN GROUP (ORDER BY sorted\_args) | VARIADIC “any” | VARIADIC “any” | double precision | No | 假想行的相对 排名，范围从 0 到 1 |
| cume\_dist(args) WITHIN GROUP(ORDER BY sorted\_args) | VARIADIC “any” | VARIADIC “any” | double precision | No | 假想行的相对 排名，范围从 1/N 到 1 |

: 表 8.58 假想集聚集函数

对于这些假想集聚集的每一个，args中给定的直接参数列表必须匹配sorted\_args中给定的聚集参数的数量和类型。与大部分的内建聚集不同，这些聚集并不严格，即它们不会丢弃包含空值的输入行。空值的排序根据ORDER BY子句中指定的规则进行。

| **函数** | **返回类型** | **描述** |
| --- | --- | --- |
| GROUPING(args…) | integer | 整数位掩码指示哪些参数不 被包括在当前分组集合中 |

: 表 8.59 分组操作

分组操作用来与分组集合（见第 6.2.4 节）共同来区分结果行。GROUPING操作的参数并不会被实际计算，但是它们必须准确地匹配在相关查询层次的GROUP BY子句中给定的表达式。 最右边参数指派的位是最低有效位，如果对应的表达式被包括在产生结果行的分组集合的分组条件中则每一位是 0，否则是 1。例如：

\=> SELECT \* FROM items\_sold;

make | model | sales

\-------+-------+-------

Foo | GT | 10

Foo | Tour | 20

Bar | City | 15

Bar | Sport | 5

(4 rows)

\=> SELECT make, model, GROUPING(make,model), sum(sales) FROM items\_sold GROUP BY

ROLLUP(make,model);

make | model | grouping | sum

\-------+-------+----------+-----

Foo | GT | 0 | 10

Foo | Tour | 0 | 20

Bar | City | 0 | 15

Bar | Sport | 0 | 5

Foo | | 1 | 30

Bar | | 1 | 20

| | 3 | 50

(7 rows)

## 窗口函数

窗口函数提供在与当前查询行相关的行集合上执行计算的能力。有关这个特性的介绍请见第 2.5 节。 语法细节则请见第 4.2.8 节。

表 8.60列出了内建的窗口函数。注意必须使用窗口函数的语法调用这些函数；一个OVER子句是必需的。

在这些函数之外，任何内建的或者用户定义的通用或者统计性聚集（即非有序集和假想集聚集）都可以被用作一个窗口函数，内建聚集的列表请见第 8.20 节。仅当聚集函数调用后面跟着一个OVER子句时，聚集函数才会像窗口函数那样工作，否则它们会按非窗口聚集的方式运行并且为整个集合返回一个单一行。

| **函数** | **返回类型** | **描述** |
| --- | --- | --- |
| row\_number() | bigint | 当前行在其分区中的行号， 从1计 |
| rank() | bigint | 带间隙的当前行排名； 与该 行的第一个同等行 的row\_number相同 |
| dense\_rank() | bigint | 不带间隙的当前行排名； 这 个函数计数同等组 |
| percent\_rank() | double precision | 当前行的相对排名： (rank- 1) / (总行数 - 1) |
| cume\_dist() | double precision | 累积分布：(在当前行之前或 者平级的分区行数) / 分区行总数 |
| ntile(num\_buckets integer) | integer | 从1到参数值的整数范围，尽可能等分分区 |
| lag(value anyelement \[, offset integer \[, default anyelement \]\]) | 和value的类型相同 | 返回value，它在分区内当前 行的之前offset个位置的行 上计算；如果没有这样的 行，返回default替代（必须和value类型相 同）。offset和default都是根据当前行计算的结果。如果忽略它们，则offset默认是1，default默认是空值 |
| lead(value anyelement \[, offset integer \[, default anyelement \]\]) | 和value类型相同 | 返回value，它在分区内当前 行的之后offset个位置的行 上计算；如果没有这样的 行，返回default替代（必须 和value类型相 同）。offset和default都是 根据当前行计算的结果。如 果忽略它们，则offset默认 是1，default默认是空值 |
| first\_value(value any) | same type as value | 返回在窗口帧中第一行上计 算的value |
| last\_value(value any) | 和value类型相同 | 返回在窗口帧中最后一行上 计算的value |
| nth\_value(value any, nth integer) | 和value类型相同 | 返回在窗口帧中第nth行（行 从1计数）上计算的value； 没有这样的行则返回空值 |

: 表 8.60 通用窗口函数

在表 8.60中列出的所有函数都依赖于相关窗口定义的ORDER BY子句指定的排序顺序。仅考虑ORDER BY列时不能区分的行被称为是同等行。定义的这四个排名函数（包括 cume\_dist），对于任何两个同等行的答案相同。

注意first\_value、last\_value和nth\_value只考虑”窗口帧”内的行，它默认情况下包含从分区的开始行直到当前行的最后一个同等行。这对last\_value可能不会给出有用的结果，有时对nth\_value也一样。你可以通过向OVER子句增加一个合适的帧声明（RANGE或GROUPS）来重定义帧。关于帧声明的更多信息请参考第 4.2.8 节。

当一个聚集函数被用作窗口函数时，它将在当前行的窗口帧内的行上聚集。 一个使用ORDER BY和默认窗口帧定义的聚集产生一种”运行时求和”类型的行为，这可能是或者不是想要的结果。为了获取在整个分区上的聚集，忽略ORDER BY或者使用ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING。 其它窗口帧声明可以用来获得其它的效果。

| 注意： |
| --- |
| SQL 标准为lead、lag、first\_value、last\_value和nth\_value定义了一个RESPECT NULLS或IGNORE NULLS选项。 这在瀚高数据库中没有实现：行为总是与标准的默认相同，即RESPECT NULLS。 同样，标准中用于nth\_value的FROM FIRST或FROM LAST选项没有实现：只有支持默认的FROM FIRST行为（你可以通过反转ORDER BY的排序达到FROM LAST的结果）。 |

cume\_dist计算小于等于当前行及其平级行的分区行所占的分数，而percent\_rank计算小于当前行的分区行所占的分数，假定当前行不存在于该分区中。

## 子查询表达式

本节描述瀚高数据库中可用的SQL兼容的子查询表达式。所有本节中成文的表达式都返回布尔值（真/假）结果。

### EXISTS

EXISTS (subquery)

EXISTS的参数是一个任意的SELECT语句， 或者说子查询。系统对子查询进行运算以判断它是否返回行。如果它至少返回一行，那么EXISTS的结果就为”真”； 如果子查询没有返回行，那么EXISTS的结果是”假”。

子查询可以引用来自周围的查询的变量，这些变量在该子查询的任何一次计算中都起常量的作用。

这个子查询通常只是运行到能判断它是否可以返回至少一行为止， 而不是等到全部结束。

在这里写任何有副作用的子查询都是不明智的（例如调用序列函数）；这些副作用是否发生是很难判断的。

因为结果只取决于是否会返回行，而不取决于这些行的内容， 所以这个子查询的输出列表通常是无关紧要的。一个常用的编码习惯是用EXISTS(SELECT 1 WHERE...)的形式写所有的EXISTS测试。不过这条规则有例外，例如那些使用INTERSECT的子查询。

下面这个简单的例子类似在col2上的一次内联接，但是它为每个 tab1的行生成最多一个输出，即使存在多个匹配tab2的行也如此∶

SELECT col1

FROM tab1

WHERE EXISTS (SELECT 1 FROM tab2 WHERE col2 = tab1.col2);

### IN

expression IN (subquery)

右手边是一个圆括弧括起来的子查询， 它必须正好只返回一个列。左手边表达式将被计算并与子查询结果逐行进行比较。 如果找到任何等于子查询行的情况，那么IN的结果就是”真”。 如果没有找到相等行，那么结果是”假”（包括子查询没有返回任何行的情况）。

请注意如果左手边表达式得到空值，或者没有相等的右手边值， 并且至少有一个右手边行得到空值，那么IN结构的结果将是空值，而不是假。这个行为是遵照 SQL 处理空值的一般规则的。

和EXISTS一样，假设子查询将被完成运行完全是不明智的。

row\_constructor IN (subquery)

这种形式的IN的左手边是一个行构造器， 如第 4.2.13 节中所述。 右手边是一个圆括弧子查询，它必须返回和左手边返回的行中表达式所构成的完全一样多的列。 左手边表达式将被计算并与子查询结果逐行进行比较。如果找到任意相等的子查询行，则IN的结果为”真”。如果没有找到相等行， 那么结果为”假”（包括子查询不返回行的情况）。

通常，表达式或者子查询行里的空值是按照 SQL 布尔表达式的一般规则进行组合的。 如果两个行对应的成员都非空并且相等，那么认为这两行相等；如果任意对应成员为非空且不等，那么这两行不等； 否则这样的行比较的结果是未知（空值）。如果所有行的结果要么是不等， 要么是空值，并且至少有一个空值，那么IN的结果是空值。

### NOT IN

expression NOT IN (subquery)

右手边是一个用圆括弧包围的子查询，它必须返回正好一个列。左手边表达式将被计算并与子查询结果逐行进行比较。 如果只找到不相等的子查询行（包括子查询不返回行的情况），那么NOT IN的结果是”真”。 如果找到任何相等行，则结果为”假”。

请注意如果左手边表达式得到空值，或者没有相等的右手边值， 并且至少有一个右手边行得到空值，那么NOT IN结构的结果将是空值，而不是真。这个行为是遵照 SQL 处理空值的一般规则的。

和EXISTS一样，假设子查询会完全结束是不明智的。

row\_constructor NOT IN (subquery)

这种形式的NOT IN的左手边是一个行构造器， 如第 4.2.13 节中所述。 右手边是一个圆括弧子查询，它必须返回和左手边返回的行中表达式所构成的完全一样多的列。 左手边表达式将被计算并与子查询结果逐行进行比较。如果找到不等于子查询行的行，则NOT IN的结果为”真”。如果找到相等行， 那么结果为”假”（包括子查询不返回行的情况）。

通常，表达式或者子查询行里的空值是按照 SQL 布尔表达式的一般规则进行组合的。 如果两个行对应的成员都非空并且相等，那么认为这两行相等；如果任意对应成员为非空且不等，那么这两行不等； 否则这样的行比较的结果是未知（空值）。如果所有行的结果要么是不等， 要么是空值，并且至少有一个空值，那么NOT IN的结果是空值。

### ANY/SOME

expression operator ANY (subquery)

expression operator SOME (subquery)

这种形式的右手边是一个圆括弧括起来的子查询， 它必须返回正好一个列。左手边表达式将被计算并使用给出的 操作符对子查询结果逐行进行比较。如果获得任何真值结果，那么ANY的结果就是”真”。 如果没有找到真值结果，那么结果是”假”（包括子查询没有返回任何行的情况）。

SOME是ANY的同义词。IN等价于= ANY。

请注意如果没有任何成功并且至少有一个右手边行为该操作符结果生成空值， 那么ANY结构的结果将是空值，而不是假。 这个行为是遵照 SQL 处理空值布尔组合的一般规则制定的。

和EXISTS一样，假设子查询将被完全运行是不明智的。

row\_constructor operator ANY (subquery)

row\_constructor operator SOME (subquery)

这种形式的左手边是一个行构造器，如第 4.2.13 节所述。右手边是一个圆括弧括起来的子查询， 它必须返回和左手边列表给出的表达式一样多的列。左手边表达式将被计算并使用给出的操作符对子查询结果逐行进行比较。如果比较为任何子查询行返回真，则ANY的结果为”真”。如果比较对每一个子查询行都返回假，则结果为”假”（包括子查询不返回行的情况）。如果比较不对任何行返回真并且至少对一行返回 NULL，则结果为 NULL。

关于行构造器比较的详细含义请见第 8.23.5 节.

### ALL

expression operator ALL (subquery)

ALL 的这种形式的右手边是一个圆括弧括起来的子查询， 它必须只返回一列。左手边表达式将被计算并使用给出的 操作符对子查询结果逐行进行比较。该操作符必须生成布尔结果。 如果所有行得到真（包括子查询没有返回任何行的情况），ALL的结果就是”真”。如果没有存在任何假值结果，那么结果是”假”。如果比较为任何行都不返回假并且对至少一行返回 NULL，则结果为 NULL。

NOT IN等价于<> ALL。

和EXISTS一样，假设子查询将被完全运行是不明智的。

row\_constructor operator ALL (subquery)

ALL的这种形式的左手边是一个行构造器，如第 4.2.13 节所述。 右手边是一个圆括弧括起来的子查询，它必须返回和左手边行中表达式一样多的列。 左手边表达式将被计算并使用给出的 操作符对子查询结果逐行进行比较。如果对所有子查询行该比较都返回真，那么ALL的结果就是”真”（包括子查询没有返回任何行的情况）。如果对任何子查询行比较返回假，则结果为”假”。如果比较对任何子查询行都不返回假并且对至少一行返回 NULL，则结果为 NULL。

关于行构造器比较的详细含义请见第 8.23.5 节.

### 单一行比较

row\_constructor operator (subquery)

左手边是一个行构造器，如第 4.2.13 节所述。 右手边是一个圆括弧括起来的子查询，该查询必须返回和左手边行中表达式数目完全一样的列。 另外，该子查询不能返回超过一行的数量（如果它返回零行，那么结果就是空值）。 左手边被计算并逐行与右手边的子查询结果行比较。

关于行构造器比较的详细含义请见第 8.23.5 节。

## 行和数组比较

本节描述几个特殊的结构，用于在值的组之间进行多重比较。这些形式语法上和前面一节的子查询形式相关，但是不涉及子查询。 这种形式涉及的数组子表达式是瀚高数据库的扩展； 其它的是SQL兼容的。所有本节记录的表达式形式都返回布尔（Boolean）结果（真/假）。

### IN

expression IN (value \[,...\])

右手边是一个圆括弧包围的标量列表。如果左手边表达式的结果等于任何右手边表达式中的一个，结果为”真”。它是下面形式的缩写

expression = value1

OR

expression = value2

OR

...

请注意如果左手边表达式得到空值，或者没有相等的右手边值并且至少有一个右手边的表达式得到空值，那么IN结构的结果将为空值，而不是假。这符合 SQL 处理空值的布尔组合的一般规则。

### NOT IN

expression NOT IN (value \[,...\])

右手边是一个圆括弧包围的标量列表。如果左手边表达式的结果不等于所有右手边表达式，结果为”真”。它是下面形式的缩写

expression <> value1

AND

expression <> value2

AND

...

请注意如果左手边表达式得到空值，或者没有相等的右手边值并且至少有一个右手边的表达式得到空值，那么NOT IN结构的结果将为空值， 而不是我们可能天真地认为的真值。这符合 SQL 处理空值的布尔组合的一般规则。

| 提示： |
| --- |
| x NOT IN y在所有情况下都等效于NOT (x IN y)。但是，在处理空值的时候，用NOT IN比用IN更可能迷惑新手。最好尽可能用正逻辑来表达你的条件。 |

### ANY/SOME (array)

expression operator ANY (array expression)

expression operator SOME (array expression)

右手边是一个圆括弧包围的表达式，它必须得到一个数组值。左手边表达式被计算并且使用给出的操作符对数组的每个元素进行比较，这个操作符必须得到布尔结果。如果得到了任何真值结果，那么ANY的结果是”真”。 如果没有找到真值结果（包括数组只有零个元素的情况），那么结果是”假”。

如果数组表达式得到一个空数组，ANY的结果将为空值。如果左手边的表达式得到空值，ANY通常是空值（尽管一个非严格比较操作符可能得到一个不同的结果）。另外，如果右手边的数组包含任何空值元素或者没有得到真值比较结果，ANY的结果将是空值而不是假（再次，假设是一个严格的比较操作符）。这符合 SQL 对空值的布尔组合的一般规则。

SOME是ANY的同义词。

### ALL (array)

expression operator ALL (array expression)

右手边是一个圆括弧包围的表达式，它必须得到一个数组值。左手边表达式将被计算并使用给出的操作符与数组的每个元素进行比较，这个操作符必须得到一个布尔结果。如果所有比较都得到真值结果，那么ALL的结果是 “真”（包括数组只有零个元素的情况）。如果有任何假值结果，那么结果是”假”。

如果数组表达式得到一个空数组，ALL的结果将为空值。如果左手边的表达式得到空值，ALL通常是空值（尽管一个非严格比较操作符可能得到一个不同的结果）。另外，如果右手边的数组包含任何空值元素或者没有得到假值比较结果，ALL的结果将是空值而不是真（再次，假设是一个严格的比较操作符）。这符合 SQL 对空值的布尔组合的一般规则。

### 行构造器比较

row\_constructor operator row\_constructor

每一边都是一个行构造器，如第 4.2.13 节所述。两个行值必须具有相同数量的域。每一边被计算并且被逐行比较。当操作符是 =、 <>、 < <=、 >、 >=时，允许进行行构造器比较。

每一个行元素必须是具有一个默认 B 树操作符类的类型，否则尝试比较会产生一个错误。

\=和<>情况略有不同。如果两行的所有对应成员都是非空且相等则这两行被认为相等；如果任何对应成员是非空但是不相等则这两行不相等；否则行比较的结果为未知（空值）。

对于<、<=、>和>=情况，行元素被从左至右比较，在找到一处不等的或为空的元素对就立刻停下来。如果这一对元素都为空值，则行比较的结果为未知（空值）；否则这一对元素的比较结果决定行比较的结果。例如，ROW(1,2,NULL) < ROW(1,3,0)得到真，而不是空值，因为第三对元素并没有被考虑。

row\_constructor IS DISTINCT FROM row\_constructor

这个结构与<>行比较相似，但是它对于空值输入不会得到空值。任何空值被认为和任何非空值不相等（有区别），并且任意两个空值被认为相等（无区别）。因此结果将总是为真或为假，永远不会是空值。

row\_constructor IS NOT DISTINCT FROM row\_constructor

这个结构与=行比较相似，但是它对于空值输入不会得到空值。任何空值被认为和任何非空值不相等（有区别），并且任意两个空值被认为相等（无区别）。因此结果将总是为真或为假，永远不会是空值。

### 组合类型比较

record operator record

SQL 规范要求在结果依赖于比较两个 NULL 值或者一个 NULL 与一个非 NULL 时逐行比较返回 NULL。瀚高数据库只有在比较两个行构造器（如第 9.23.5 节）的结果或者比较一个行构造器与一个子查询的输出时才这样做（如第 9.22 节中所述）。在其他比较两个组合类型值的环境中，两个 NULL 域值被认为相等，并且一个 NULL 被认为大于一个非 NULL。为了得到组合类型的一致的排序和索引行为，这样做是必要的。

每一边都会被计算并且它们会被逐行比较。当操作符是 =、 <>、 <、 <=、 >或者 >=时或者具有与这些类似的语义时，允许组合类型的比较（更准确地说，如果一个操作符是一个 B 树操作符类的成员，或者是一个 B 树操作符类的=成员的否定词，它就可以是一个行比较操作符）。 上述操作符的行为与用于行构造器（见第 9.23.5 节）的IS \[ NOT \] DISTINCT FROM相同。

为了支持包含无默认 B 树操作符类的元素的行匹配，为组合类型比较定义了下列操作符：

\*=、 \*<>、 \*<、 \*<=、 \*>以及 \*>=。 这些操作符比较两行的内部二进制表达。即使两行用相等操作符的比较为真，两行也可能 具有不同的二进制表达。行在这些比较操作符之下的排序是决定性的，其他倒没什么意义。 这些操作符在内部被用于物化视图并且可能对其他如复制之类的特殊功能有用，但是它们并不打算用在书写查询这类普通用途中。

## 集合返回函数

本节描述那些可能返回多于一行的函数。目前这个类中被使用最广泛的是级数生成函数，如表 8.61和表 8.62所述。其他更特殊的集合返回函数在本手册的其他地方描述。 组合多集合返回函数的方法可见第 6.2.1.4 节。

| **函数** | **参数类型** | **返回类型** | **描述** |
| --- | --- | --- | --- |
| generate\_series(start, stop) | int、bigint或者numeric | setof int、setof bigint或者setof numeric（与参数类型相同） | 产生一系列值，从start到stop，步长 为 1 |
| generate\_series(start, stop, step) | int、bigint或者numeric | setof int、setof bigint或者setof numeric（与参数类型相同） | 产生一系列值，从start到stop，步长 为step |
| generate\_series(start, stop, step interval) | timestamp或timestamp with time zone | setof timestamp或setof timestamp with time zone（和参数类型相同） | 产生一系列值， 从start到stop，步长 为step |

: 表 8.61 级数生成函数

当step为正时，如果start大于stop则返回零行。相反，当step为负时，如果start小于stop则返回零行。对于NULL输入也会返回零行。step为零是一个错误。下面是一些例子：

SELECT \* FROM generate\_series(2,4);

generate\_series

\-----------------

2

3

4

(3 rows)

SELECT \* FROM generate\_series(5,1,-2);

generate\_series

\-----------------

5

3

1

(3 rows)

SELECT \* FROM generate\_series(4,3);

generate\_series

\-----------------

(0 rows)

SELECT generate\_series(1.1, 4, 1.3);

generate\_series

\-----------------

1.1

2.4

3.7

(3 rows)

\-- 这个例子依赖于日期+整数操作符

SELECT current\_date + s.a AS dates FROM generate\_series(0,14,7) AS s(a);

dates

\------------

2004-02-05

2004-02-12

2004-02-19

(3 rows)

SELECT \* FROM generate\_series('2008-03-01 00:00'::timestamp,

'2008-03-04 12:00', '10 hours');

generate\_series

\---------------------

2008-03-01 00:00:00

2008-03-01 10:00:00

2008-03-01 20:00:00

2008-03-02 06:00:00

2008-03-02 16:00:00

2008-03-03 02:00:00

2008-03-03 12:00:00

2008-03-03 22:00:00

2008-03-04 08:00:00

(9 rows)

| **函数** | **返回类型** | **描述** |
| --- | --- | --- |
| generate\_subscripts(array anyarray, dim int) | setof int | 生成一个级数组成给定数组 的下标。 |
| generate\_subscripts(array anyarray, dim int, reverse boolean) | setof int | 生成一个级数组成给定数组 的下标。当reverse为真，级 数以逆序返回。 |

: 表 8.62 下标生成函数

generate\_subscripts是一个快捷函数，它为给定数组的指定维度生成一组合法的下标。对于不具有请求维度的数组返回零行，对于 NULL 数组也返回零行（但是会对 NULL 数组元素返回合法的下标）。下面是一些例子：

\-- 基本使用

SELECT generate\_subscripts('{NULL,1,NULL,2}'::int\[\], 1) AS s;

s

\---

1

2

3

4

(4 rows)

\-- 表示一个数组，下标和被下标的值需要一个子查询

SELECT \* FROM arrays;

a

\--------------------

{-1,-2}

{100,200,300}

(2 rows)

SELECT a AS array, s AS subscript, a\[s\] AS value

FROM (SELECT generate\_subscripts(a, 1) AS s, a FROM arrays) foo;

array | subscript | value

\---------------+-----------+-------

{-1,-2} | 1 | -1

{-1,-2} | 2 | -2

{100,200,300} | 1 | 100

{100,200,300} | 2 | 200

{100,200,300} | 3 | 300

(5 rows)

\-- 平面化一个 2D 数组

CREATE OR REPLACE FUNCTION unnest2(anyarray)

RETURNS SETOF anyelement AS $$

select $1\[i\]\[j\]

from generate\_subscripts($1,1) g1(i),

generate\_subscripts($1,2) g2(j);

$$ LANGUAGE sql IMMUTABLE;

CREATE FUNCTION

SELECT \* FROM unnest2(ARRAY\[\[1,2\],\[3,4\]\]);

unnest2

\---------

1

2

3

4

(4 rows)

当FROM子句中的一个函数后面有WITH ORDINALITY时，输出中会追加一个bigint列，它的值从1开始并且该函数输出的每一行加1。这在unnest()之类的集合返回函数中最有用。

\-- set returning function WITH ORDINALITY

SELECT \* FROM pg\_ls\_dir('.') WITH ORDINALITY AS t(ls,n);

ls | n

\-----------------+----

pg\_serial | 1

pg\_twophase | 2

postmaster.opts | 3

pg\_notify | 4

Highgo.conf | 5

pg\_tblspc | 6

logfile | 7

base | 8

postmaster.pid | 9

pg\_ident.conf | 10

global | 11

pg\_xact | 12

pg\_snapshots | 13

pg\_multixact | 14

PG\_VERSION | 15

pg\_wal | 16

pg\_hba.conf | 17

pg\_stat\_tmp | 18

pg\_subtrans | 19

(19 rows)

## 系统信息函数和运算符

表 8.63展示了多个可以抽取会话和系统信息的函数。

除了本节列出的函数，还有一些与统计系统相关的函数也提供系统信息。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| current\_catalog | name | 当前数据库名（SQL 标准中称作“目录”） |
| current\_database() | name | 当前数据库名 |
| current\_query() | text | 当前正在执行的查询的文 本，和客户端提交的一样 （可能包含多于一个语句） |
| current\_role | name | 等效于current\_user |
| current\_schema\[()\] | name | 当前模式名 |
| current\_schemas(boolean) | name\[\] | 搜索路径中的模式名，可以 选择是否包含隐式模式 |
| current\_user | name | 当前执行上下文的用户名 |
| inet\_client\_addr() | inet | 远程连接的地址 |
| inet\_client\_port() | int | 远程连接的端口 |
| inet\_server\_addr() | inet | 本地连接的地址 |
| inet\_server\_port() | int | 本地连接的端口 |
| pg\_backend\_pid() | int | 与当前会话关联的服务器进 程的进程 ID |
| pg\_blocking\_pids(int) | int\[\] | 阻塞指定服务器进程ID获得 锁的进程 ID |
| pg\_conf\_load\_time() | timestamp with time zone | 配置载入时间 |
| pg\_current\_logfile(\[text\]) | text | 当前日志收集器在使用的主 日志文件名或者所要求格式 的日志的文件名 |
| pg\_my\_temp\_schema() | oid | 会话的临时模式的 OID，如果没有则为 0 |
| pg\_is\_other\_temp\_schema(oid) | boolean | 模式是另一个会话的临时模 式吗？ |
| pg\_jit\_available() | boolean | 这个会话中JIT编译是否可用（见第 31 章）？如果jit被设置为假，则返回false。 |
| pg\_listening\_channels() | setof text | 会话当前正在监听的频道名 称 |
| pg\_notification\_queue\_usage() | double | 异步通知队列当前被占用的 分数（0-1） |
| pg\_postmaster\_start\_time() | timestamp with time zone | 服务器启动时间 |
| pg\_safe\_snapshot\_blocking\_pids( int) | ( int\[\]int) | 阻止指定服务器进程ID获取安全快照的进程ID |
| pg\_trigger\_depth() | int | 瀚高数据库触发器的当前嵌套层次（如果没有调用则为 0，直接或间接，从一个触发器内部开始） |
| session\_user | name | 会话用户名 |
| user | name | 等价于current\_user |
| version() | text | 瀚高数据库版本信息。机器可读的版本还可见server\_version\_num。 |
| cgw\_version() | text | 返回license文件的版本信息。 |
| cgwdb\_version() | text | 返回产品的软著信息。 |
| build\_version() | text | 返回产品的详细版本信息。 |

: 表 8.63 会话信息函数

| **注意：** |
| --- |
| current\_catalog、current\_role、current\_schema、current\_user、session\_user和user在 SQL里有特殊的语意状态： 它们被调用时结尾不要跟着园括号（在瀚高数据库中，圆括号可以有选择性地被用于current\_schema，但是不能和其他的一起用）。 |

session\_user通常是发起当前数据库连接的用户，不过sysdba用户可以用SET SESSION AUTHORIZATION修改这个设置。current\_user是用于权限检查的用户标识。通常， 它总是等于会话用户，但是可以被SET ROLE改变。它也会在函数执行的过程中随着属性SECURITY DEFINER的改变而改变。在 Unix 的说法里，那么会话用户是”真实用户”，而当前用户是”有效用户”。current\_role以及user是current\_user的同义词（SQL标准在current\_role和current\_user之间做了区分，但瀚高数据库不区分，因为它把用户和角色统一成了一种实体）。

current\_schema返回在搜索路径中的第一个模式名（如果搜索路径是空则返回空值）。 如果创建表或者其它命名对象时没有声明目标模式，那么它将是被用于这些对象的模式。current\_schemas(boolean)返回一个在搜索路径中出现的所有模式名的数组。布尔选项决定pg\_catalog这样的隐式包含的系统模式是否包含在返回的搜索路径中。

| **注意：** |
| --- |
| 搜索路径可以在运行时修改。命令是：SET search\_path TO schema \[, schema,...\] |

inet\_client\_addr返回当前客户端的 IP 地址，inet\_client\_port返回它的端口号。

inet\_server\_addr返回接受当前连接的服务器的 IP 地址，而inet\_server\_port返回对应的端口号。如果连接是通过 Unix 域套接字进行的，那么所有这些函数都返回 NULL。

pg\_blocking\_pids返回一个进程 ID 的数组，数组中的进程中的会话阻塞了指定进程 ID 所代表的服务器进程，如果指定的服务器进程不存在或者没有被阻塞则返回空数组。如果一个进程持有与另一个进程加锁请求冲突的锁（硬锁），或者前者正在等待一个与后者加锁请求冲突的锁并且前者在该锁的等待队列中位于后者的前面（软锁），则前者会阻塞后者。在使用并行查询时，这个函数的结果总是会列出客户端可见的进程 ID（即pg\_backend\_pid的结果），即便实际的锁是由工作者进程所持有或者等待也是如此。

这样造成的后果是，结果中可能会有很多重复的 PID。还要注意当一个预备事务持有一个冲突锁时，这个函数的结果中它将被表示为一个为零的进程 ID。对这个函数的频繁调用可能对数据库性能有一些影响，因为它需要短时间地独占访问锁管理器的共享状态。

pg\_conf\_load\_time返回服务器配置文件最近被载入的timestamp with time zone（如果当前会话在那时就已经存在，这个值将是该会话自己重新读取配置文件的时间，因此在不同的会话中这个读数会有一点变化。如果不是这样，这个值就是 postmaster 进程重读配置文件的时间）。

pg\_current\_logfile以text类型返回当前被日志收集器使用的日志文件的路径。该路径包括log\_directory目录和日志文件名。日志收集必须被启用，否则返回值为NULL。当多个日志文件存在并且每一个都有不同的格式时，不带参数调用pg\_current\_logfile会返回这样的文件的路径：在所有的文件中，没有任何文件的格式在列表stderr、csvlog中排在这个文件的格式前面。如果没有任何日志文件有上述格式，则返回NULL。要请求一种特定的文件格式，可以以text将csvlog或者stderr作为可选参数的值。当所请求的日志格式不是已配置的log\_destination时，会返回NULL。pg\_current\_logfile反映了current\_logfiles文件的内容。

pg\_my\_temp\_schema返回当前会话临时模式的 OID，如果没有使用临时模式（因为它没有创建任何临时表）则返回零。如果给定的 OID 是另一个会话的临时模式的 OID，则pg\_is\_other\_temp\_schema返回真（这是有用的，例如，要将其他会话的临时表从一个目录显示中排除）。

pg\_listening\_channels返回当前会话正在监听的异步通知频道的名称的集合。pg\_notification\_queue\_usage返回等待处理的通知占可用的通知空间的比例，它是一个 0-1 范围内的double值。详见LISTEN和NOTIFY。

pg\_postmaster\_start\_time返回服务器启动的timestamp with time zone。

pg\_safe\_snapshot\_blocking\_pids一个进程ID的数组，它们代表阻止指定进程ID对应的服务器进程获取安全快照的会话，如果没有这类服务器进程或者它没有被阻塞，则会返回一个空数组。一个运行着SERIALIZABLE事务的会话会阻止SERIALIZABLE READ ONLY DEFERRABLE事务获取快照，直到后者确定避免拿到任何谓词锁是安全的。更多有关可序列化以及可延迟事务的信息请参考第 13.2.3 节。频繁调用这个函数可能会对数据库性能产生一些影响，因为它需要短时间访问谓词锁管理器的共享状态。

version返回一个描述瀚高数据库服务器版本的字符串。你也可以从server\_version或者一个机器可读的版本server\_version\_num得到这个信息。软件开发者应该使用server\_version\_num或者 PQserverVersion ，而不必解析文本形式的版本。

表 8.64列出那些允许用户编程查询对象访问权限的函数。参阅第 5.7 节获取更多有关权限的信息。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| has\_any\_column\_privilege(user, table, privilege) | boolean | 用户有没有表中任意列上的权限 |
| has\_any\_column\_privilege(table, privilege) | boolean | 当前用户有没有表中任意列上的权限 |
| has\_column\_privilege(user, table, column, privilege) | boolean | 用户有没有列的权限 |
| has\_column\_privilege(table, column, privilege) | boolean | 当前用户有没有列的权限 |
| has\_database\_privilege(user, database, privilege) | boolean | 用户有没有数据库的权限 |
| has\_database\_privilege(database, privilege) | boolean | 当前用户有没有数据库的权限 |
| has\_foreign\_data\_wrapper\_privilege(user, fdw, privilege) | boolean | 用户有没有外部数据包装器上的权限 |
| has\_foreign\_data\_wrapper\_privilege(fdw, privilege) | boolean | 当前用户有没有外部数据包装器上的权限 |
| has\_function\_privilege(user, function, privilege) | boolean | 用户有没有函数上的权限 |
| has\_function\_privilege(function, privilege) | boolean | 当前用户有没有函数上的权限 |
| has\_language\_privilege(user, language, privilege) | boolean | 用户有没有语言上的权限 |
| has\_language\_privilege(language, privilege) | boolean | 当前用户有没有语言上的权限 |
| has\_schema\_privilege(user, schema, privilege) | boolean | 用户有没有模式上的权限 |
| has\_schema\_privilege(schema, privilege) | boolean | 当前用户有没有模式上的权限 |
| has\_sequence\_privilege(user, sequence, privilege) | boolean | 用户有没有序列上的权限 |
| has\_sequence\_privilege(sequence, privilege) | boolean | 当前用户有没有序列上的权限 |
| has\_server\_privilege(user, server, privilege) | boolean | 用户有没有外部服务器上的权限 |
| has\_server\_privilege(server, privilege) | boolean | 当前用户有没有外部服务器上的权限 |
| has\_table\_privilege(user, table, privilege) | boolean | 用户有没有表上的权限 |
| has\_table\_privilege(table, privilege) | boolean | 当前用户有没有表上的权限 |
| has\_tablespace\_privilege(user, tablespace, privilege) | boolean | 用户有没有表空间上的权限 |
| has\_tablespace\_privilege(tablespace, privilege) | boolean | 当前用户有没有表空间上的权限 |
| has\_type\_privilege(user, type, privilege) | boolean | 用户有没有类型的特权 |
| has\_type\_privilege(type, privilege) | boolean | 当前用户有没有类型的特权 |
| pg\_has\_role(user, role, privilege) | boolean | 用户有没有角色上的权限 |
| pg\_has\_role(role, privilege) | boolean | 当前用户有没有角色上的权限 |
| row\_security\_active(table) | boolean | 当前用户是否在表上开启了行级安全性 |

: 表 8.64 访问权限查询函数

has\_table\_privilege判断一个用户是否可以用某种特定的方式访问一个表。 该用户可以通过名字或者 OID （pg\_authid.oid） 来指定，也可以用public表示 PUBLIC 伪角色。如果省略该参数，则使用current\_user。 该表可以通过名字或者 OID 指定（因此，实际上有六种has\_table\_privilege的变体，我们可以通过它们的参数数目和类型来区分它们） 。如果用名字指定，那么在必要时该名字可以是模式限定的。所希望的权限类型是用一个文本串来指定的，它必须是下面的几个值之一：

SELECT、INSERT、UPDATE、DELETE、TRUNCATE、REFERENCES或TRIGGER。WITH

GRANT OPTION可以被选择增加到一个权限类型来测试是否该权限是使用转授选项得到。另外，可以使用逗号分隔来列出多个权限类型，在这种情况下只要具有其中之一的权限则结果为真（权限字符串的大小写并不重要，可以在权限名称之间出现额外的空白，但是在权限名内部不能有空白）。一些例子：

SELECT has\_table\_privilege('myschema.mytable', 'select');

SELECT has\_table\_privilege('joe', 'mytable', 'INSERT, SELECT WITH GRANT OPTION');

has\_sequence\_privilege检查一个用户是否能以某种特定方式访问一个序列。它的参数可能性和has\_table\_privilege相似。所希望测试的访问权限类型必须是下列之一：USAGE、SELECT或UPDATE。

has\_any\_column\_privilege检查一个用户是否能以特定方式访问一个表的任意列。其参数可能性和has\_table\_privilege类似，除了所希望的访问权限类型必须是下面值的某种组合：SELECT、INSERT、UPDATE或REFERENCES。注意在表层面上具有这些权限的任意一个都会隐式地把它授权给表中的每一列，因此如果has\_table\_privilege对同样的参数返回真则has\_any\_column\_privilege将总是返回真。但是如果在至少一列上有一个该权限的列级授权，has\_any\_column\_privilege也会成功。

has\_column\_privilege检查一个用户是否能以特定方式访问一个列。它的参数可能性与has\_table\_privilege类似，并且列还可以使用名字或者属性号来指定。希望的访问权限类型必须是下列值的某种组合：SELECT、INSERT、UPDATE或REFERENCES。注意在表级别上具有这些权限中的任意一种将会隐式地把它授予给表上的每一列。

has\_database\_privilege检查一个用户是否能以特定方式访问一个数据库。它的参数可能性类似

has\_table\_privilege。希望的访问权限类型必须是以下值的某种组

合：CREATE、CONNECT、TEMPORARY或TEMP（等价于TEMPORARY）。

has\_function\_privilege检查一个用户是否能以特定方式访问一个函数。其参数可能性类似has\_table\_privilege。在用一个文本串而不是 OID 指定一个函数时，允许的输入和regprocedure数据类型一样（参阅 第7.19 节）。希望的访问权限类型必须是EXECUTE。

一个例子：

SELECT has\_function\_privilege('joeuser', 'myfunc(int, text)', 'execute');

has\_foreign\_data\_wrapper\_privilege检查一个用户是否能以特定方式访问一个外部数据包装器。它的参数可能性类似于has\_table\_privilege。希望的访问权限类型必须是USAGE。

has\_language\_privilege检查一个用户是否可以以某种特定的方式访问一个过程语言。 其参数可能性类似 has\_table\_privilege。希望的访问权限类型必须是USAGE。

has\_schema\_privilege检查一个用户是否可以以某种特定的方式访问一个模式。 其参数可能性类似 has\_table\_privilege。希望的访问权限类型必须是CREATE或USAGE。

has\_server\_privilege检查一个用户是否可以以某种特定的方式访问一个外部服务器。 其参数可能性类似 has\_table\_privilege。希望的访问权限类型必须是USAGE。

has\_tablespace\_privilege检查一个用户是否可以以某种特定的方式访问一个表空间。其参数可能性类似 has\_table\_privilege。希望的访问权限类型必须是CREATE。

has\_type\_privilege检查一个用户是否能以特定的方式访问一种类型。其参数的可能性类同于has\_table\_privilege。在用字符串而不是 OID 指定类型时，允许的输入和regtype数据类型相同（见第 8.19 节）。期望的访问特权类型必须等于USAGE。

pg\_has\_role检查一个用户是否可以以某种特定的方式访问一个角色。其参数可能性类似 has\_table\_privilege，除了public不能被允许作为一个用户名。希望的访问权限类型必须是下列值的某种组合：MEMBER或USAGE。MEMBER表示该角色中的直接或间接成员关系（即使用SET ROLE的权力），而USAGE表示不做SET ROLE的情况下该角色的权限是否立即可用。

row\_security\_active检查在 current\_user的上下文和环境中是否为指定的 表激活了行级安全性。表可以用名称或者 OID 指定。

表 8.66 显示了aclitem类型的可用操作符，它是访问权限的目录表示。 有关如何读取访问权限值的信息，请参阅 第 5.7 节。

| **操作符** | **描述** | **例子** | **结果** |
| --- | --- | --- | --- |
| \= | equal | ‘calvin=r *w/ hobbes’::aclitem = ‘calvin=r* w\*/ hobbes’::aclitem | f |
| @> | 包含元素 | ‘{calvin=r *w/ hobbes,hobbes=r* w\*/ postgres}’::aclitem\[\] @> ‘calvin=r\*w/ hobbes’::aclitem | t |
| ~ | 包含元素 | ‘{calvin=r *w/ hobbes,hobbes=r* w\*/ postgres}’::aclitem\[\] ~ ‘calvin=r\*w/ hobbes’::aclitem | t |

: 表 8.65 aclitem Operators

表 8.66 显示了一些额外的函数来管理aclitem类型。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| acldefault(type, ownerId) | aclitem\[\] | 获取属于ownerId的对象的默认访问权限。 |
| aclexplode(aclitem\[\]) | setof record | 获取 aclitem 数组为元组 |
| makeaclitem(grantee, grantor, privilege, grantable) | aclitem | 从输入中建立一个aclitem。 |

: 表 8.66 aclitem Functions

acldefault返回属于角色ownerId的type类型的对象的内置默认访问权限。 这些代表了当对象的ACL条目为空时将被假定的访问权限。 (默认的访问权限在第 5.7 节中描述了)。 type参数是一个 CHAR: 'c' for COLUMN, 'r' for TABLE 和类表对象, 's' for SEQUENCE, 'd' for DATABASE, 'f' for FUNCTION 或者 PROCEDURE, 'l' for LANGUAGE, 'L' for LARGE OBJECT, 'n' for SCHEMA, 't' for TABLESPACE, 'F' for FOREIGN DATA WRAPPER, 'S' for FOREIGN SERVER, 'T' for TYPE 或者 DOMAIN.

aclexplode返回一个aclitem数组作为行集。输出的列是grantor oid, grantee oid (0 for PUBLIC), 被授权为 text (SELECT,...) 以及权限是否可以被授予boolean。makeaclitem执行反向操作。

表 9.67展示了决定是否一个特定对象在当前模式搜索路径中可见的函数。例如，如果一个表所在的模式在当前搜索路径中并且在它之前没有出现过相同的名字，这个表就被说是可见的。这等价于在语句中表可以被用名称引用但不加显式的模式限定。要列出所有可见表的名字：

SELECT relname FROM pg\_class WHERE pg\_table\_is\_visible(oid);

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_collation\_is\_visible(collation\_oid ) | boolean | 排序规则在搜索路径中可见吗？ |
| pg\_conversion\_is\_visible(conversion\_oid ) | boolean | 转换在搜索路径中可见吗？ |
| pg\_function\_is\_visible(function\_oid ) | boolean | 函数在搜索路径中可见吗？ |
| pg\_opclass\_is\_visible(opclass\_oid) | boolean | 操作符类在搜索路径中可见吗？ |
| pg\_operator\_is\_visible(operator\_oid) | boolean | 操作符在搜索路径中可见吗？ |
| pg\_opfamily\_is\_visible(opclass\_oid) | boolean | 操作符族在搜索路径中可见吗？ |
| pg\_statistics\_obj\_is\_visible(boolean stat\_oid) | boolean | 是搜索路径中的统计信息对象 |
| pg\_table\_is\_visible(table\_oid) | boolean | 表在搜索路径中可见吗？ |
| pg\_ts\_config\_is\_visible(config\_oid ) | boolean | 文本搜索配置在搜索路径中可见吗？ |
| pg\_ts\_dict\_is\_visible(dict\_oid ) | boolean | 文本搜索字典在搜索路径中可见吗？ |
| pg\_ts\_parser\_is\_visible(parser\_oid ) | boolean | 文本搜索解析器在搜索路径中可见吗？ |
| pg\_ts\_template\_is\_visible(template\_oid ) | boolean | 文本搜索模板在搜索路径中可见吗？ |
| pg\_type\_is\_visible(type\_oid) | boolean | 类型（或域）在搜索路径中可见吗？ |

: 表 8.67 模式可见性查询函数

每一个函数对一种数据库对象执行可见性检查。注意pg\_table\_is\_visible也可被用于视图、物化视图、索引、序列和外部表，pg\_function\_is\_visible也能被用于过程和聚集，pg\_type\_is\_visible也可以被用于域。对于函数和操作符，如果在路径中更早的地方没有出现具有相同名称和参数数据类型的对象，该对象在搜索路径中是可见的。对于操作符类，名称和相关的索引访问方法都要考虑。

所有这些函数都要求用对象 OID 来标识将被检查的对象。如果你想用名称来测试一个对象，使用 OID 别名类型（regclass、regtype、regprocedure、regoperator、regconfig或regdictionary）将会很方便。例如：

SELECT pg\_type\_is\_visible('myschema.widget'::regtype);

注意以这种方式测试一个非模式限定的类型名没什么意义 — 如果该名称完全能被识别，它必须是可见的。

表8.68列出了从系统目录抽取信息的函数。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| format\_type(type\_oid, typemod) | text | 获得一个数据类型的 SQL 名 字 |
| pg\_get\_constraintdef(constraint\_oid ) | text | 获得一个约束的定义 |
| pg\_get\_constraintdef(constraint\_oid, pretty\_bool) | text | 获得一个约束的定义 |
| pg\_get\_expr(pg\_node\_tree, relation\_oid) | text | 反编译一个表达式的内部形式，假定其中的任何 Var 指向由第二个参数指示的关系 |
| pg\_get\_expr(pg\_node\_tree, relation\_oid, pretty\_bool) | text | 反编译一个表达式的内部形式，假定其中的任何 Var 指向由第二个参数指示的关系 |
| pg\_get\_functiondef(func\_oid) | text | 获得一个函数或过程的定义 |
| pg\_get\_function\_arguments(func\_oid ) | text | 获得一个函数或过程定义的参数列表（带有默认值） |
| pg\_get\_function\_identity\_arguments( func\_oid) | text | 获得标识一个函数或过程的参数列表（不带默认值） |
| pg\_get\_function\_result(func\_oid ) | text | 获得函数的RETURNS子句（对过程返回空） |
| pg\_get\_indexdef(index\_oid) | text | 获得索引的CREATE INDEX命令 |
| pg\_get\_indexdef(index\_oid, column\_no, pretty\_bool) | text | 获得索引的CREATE INDEX命令，或者当column\_no为非零 时只得到一个索引列的定义 |
| pg\_get\_keywords() | setof record | 获得 SQL 关键字的列表及其分类 |
| pg\_get\_ruledef(rule\_oid) | text | 获得规则的CREATE RULE命令 |
| pg\_get\_ruledef(rule\_oid, pretty\_bool) | text | 获得规则的CREATE RULE命令 |
| pg\_get\_serial\_sequence(table\_name, column\_name) | text | 获得一个序列列或标识列使用的序列的名称 |
| pg\_get\_statisticsobjdef(statobj\_oid ) | text | 为扩展的统计信息对象得到CREATE STATISTICS命令 |
| pg\_get\_triggerdef(trigger\_oid) | text | 获得触发器的CREATE \[ CONSTRAINT \] TRIGGER命令 |
| pg\_get\_triggerdef(trigger\_oid, pretty\_bool) | text | 获得触发器的CREATE \[ CONSTRAINT \] TRIGGER命令 |
| pg\_get\_userbyid(role\_oid) | name | 获得给定 OID 指定的角色名 |
| pg\_get\_viewdef(view\_name) | text | 获得视图或物化视图的底 层SELECT命令（已废弃） |
| pg\_get\_viewdef(view\_name, pretty\_bool) | text | 获得视图或物化视图的底 层SELECT命令（已废弃） |
| pg\_get\_viewdef(view\_oid) | text | 获得视图或物化视图的底 层SELECT命令 |
| pg\_get\_viewdef(view\_oid, pretty\_bool) | text | 获得视图或物化视图的底 层SELECT命令 |
| pg\_get\_viewdef(view\_oid, wrap\_column\_int) | text | 获得视图或物化视图的底 层SELECT命令；带域的行被包装成指定的列数，并隐含了优质打印 |
| pg\_index\_column\_has\_property(index\_oid, column\_no, prop\_name) | boolean | 测试一个索引列是否有指定的性质 |
| pg\_index\_has\_property(index\_oid, prop\_name) | boolean | 测试一个索引是否有指定的性质 |
| pg\_indexam\_has\_property(am\_oid, prop\_name) | boolean | 测试一个索引访问方法是否有指定的性质 |
| pg\_options\_to\_table(reloptions) | setof record | 获得存储选项的名称/值对的集合 |
| pg\_tablespace\_databases(tablespace\_oid ) | setof oid | 获得在该表空间中有对象的数据库的 OID 的集合 |
| pg\_tablespace\_location(tablespace\_oid ) | text | 获得这个表空间所在的文件系统的路径 |
| pg\_typeof(any) | regtype | 获得任意值的数据类型 |
| collation for (any) | text | 获得该参数的排序规则 |
| to\_regclass(rel\_name) | regclass | 得到指定关系的 OID |
| to\_regproc(func\_name) | regproc | 得到指定函数的 OID |
| to\_regprocedure(func\_name) | regprocedure | 得到指定函数的 OID |
| to\_regoper(operator\_name) | regoper | 得到指定操作符的 OID |
| to\_regoperator(operator\_name) | regoperator | 得到指定操作符的 OID |
| to\_regtype(type\_name) | regtype | 得到指定类型的 OID |
| to\_regnamespace(schema\_name) | regnamespace | 得到指定模式的 OID |
| to\_regrole(role\_name) | regrole | 得到指定角色的 OID |

: 表 8.68 系统目录信息函数

format\_type返回一个数据类型的 SQL 名称，它由它的类型 OID 标识并且可能是一个类型修饰符。如果不知道相关的修饰符，则为类型修饰符传递 NULL。

pg\_get\_keywords返回一组记录描述服务器识别的 SQL 关键字。word列包含关键字。catcode列包含一个分类码：U为未被预定，C 为列名，T类型或函数名，R为预留。catdesc列包含一个可能本地化的描述分类的字符串。

pg\_get\_constraintdef、pg\_get\_indexdef、pg\_get\_ruledef、pg\_get\_statisticsobjdef和pg\_get\_triggerdef分别重建一个约束、索引、规则、扩展统计对象或触发器的创建命令（注意这是一个反编译的重构，而不是命令的原始文本）。pg\_get\_expr反编译一个表达式的内部形式，例如一个列的默认值。在检查系统目录内容时有用。如果表达式可能包含 Var，在第二个参数中指定它们引用的关系的 OID；如果不会出现 Var，第二个参数设置为 0 即可。pg\_get\_viewdef重构定义一个视图的SELECT查询。这些函数的大部分都有两种变体，一种可以可选地”优质打印”结果。优质打印的格式可读性更强，但是默认格式更可能被未来版本的瀚高数据库以相同的方式解释。在转出目的中避免使用优质打印输出。为优质打印参数传递假将得到和不带该参数的变体相同的结果。

pg\_get\_functiondef为一个函数返回一个完整的CREATE OR REPLACE FUNCTION语句。pg\_get\_function\_arguments返回一个函数的参数列表，形式按照它们出现在CREATE FUNCTION中的那样。pg\_get\_function\_result类似地返回函数的合适的RETURNS子句。pg\_get\_function\_identity\_arguments返回标识一个函数必要的参数列表，形式和它们出现在ALTER FUNCTION中的一样。这种形式忽略默认值。

pg\_get\_serial\_sequence返回与一个列相关联的序列的名称，如果与列相关联的序列则返回 NULL。如果该列是一个标识列，相关联的序列是为该标识列内部创建的序列。对于使用序列类型之一（serial、smallserial、bigserial）创建的列，它是为那个序列列定义创建的序列。在后一种情况中，这种关联可以用ALTER SEQUENCE OWNED BY修改或者移除（该函数可能应该已经被pg\_get\_owned\_sequence调用，它当前的名称反映了它通常被serial或bigserial列使用）。第一个输入参数是一个带可选模式的表名，第二个参数是一个列名。因为第一个参数可能是一个模式和表，它不能按照一个双引号包围的标识符来对待，意味着它默认情况下是小写的。而第二个参数只是一个列名，将被当作一个双引号包围的来处理并且会保留其大小写。函数返回的值会被适当地格式化以便传递给序列函数（参见第 8.16 节）。一种典型的用法是为标识列或者序列列读取当前值，例如：

SELECT currval(pg\_get\_serial\_sequence('sometable', 'id'));

pg\_get\_userbyid抽取给定 OID 的角色的名称。

pg\_index\_column\_has\_property、pg\_index\_has\_property和pg\_indexam\_has\_property返回指定的索引列、索引或者索引访问方法是否具有指定性质。如果性质的名称找不到或者不适用于特定的对象，亦或者 OID 或者列号不表示合法的对象，则返回NULL。列的性质可参见表 8.69，索引的性质可参见表 8.70，访问方法的性质可参见表 8.71（注意扩展访问方法可以为其索引定义额外的性质）。

| **名称** | **描述** |
| --- | --- |
| asc | 在向前扫描时列是按照升序排列吗？ |
| desc | 在向前扫描时列是按照降序排列吗？ |
| nulls\_first | 在向前扫描时列排序会把空值排在前面吗？ |
| nulls\_last | 在向前扫描时列排序会把空值排在最后吗？ |
| orderable | 列具有已定义的排序顺序吗？ |
| distance\_orderable | 列能否通过一个“distance”操作符（例 如ORDER BY col <-> constant）有序地扫 描？ |
| returnable | 列值是否可以通过一次只用索引扫描返回？ |
| search\_array | 列是否天然支持col = ANY(array)搜索？ |
| search\_nulls | 列是否支持IS NULL和IS NOT NULL搜索？ |

: 表 8.69 索引列属性

| **名称** | **描述** |
| --- | --- |
| clusterable | 索引是否可以用于CLUSTER命令？ |
| index\_scan | 索引是否支持普通扫描（非位图）？ |
| bitmap\_scan | 索引是否支持位图扫描？ |
| backward\_scan | 在扫描中扫描方向能否被更改（为了支持游 标上无需物化的FETCH BACKWARD）？ |

: 表 8.70 索引性质

| **名称** | **描述** |
| --- | --- |
| can\_order | 访问方法是否支持ASC、DESC以及CREATE INDEX中的有关关键词？ |
| can\_unique | 访问方法是否支持唯一索引？ |
| can\_multi\_col | 访问方法是否支持多列索引？ |
| can\_exclude | 访问方法是否支持排除约束？ |
| can\_include | 访问方法是否支持CREATE INDEX的INCLUDE子句？ |

: 表 8.71 索引访问方法性质

当传入pg\_class.reloptions或pg\_attribute.attoptions时，pg\_options\_to\_table返回存储选项名称/值对（option\_name/option\_value）的集合。

pg\_tablespace\_databases允许一个表空间被检查。它返回一组数据库的 OID，这些数据库都有对象存储在该表空间中。如果这个函数返回任何行，则该表空间为非空并且不能被删除。为了显示该表空间中的指定对象，你将需要连接到pg\_tablespace\_databases标识的数据库并且查询它们的pg\_class目录。

pg\_typeof返回传递给它的值的数据类型的 OID。这在检修或者动态构建 SQL 查询时有用。

函数被声明为返回regtype，它是一个 OID 别名类型（见第 8.19 节）；这表明它和一个用于比较目的的 OID 相同，但是作为一个类型名称显示。例如：

SELECT pg\_typeof(33);

pg\_typeof

\-----------

integer

(1 row)

SELECT typlen FROM pg\_type WHERE oid = pg\_typeof(33);

typlen

\--------

4

(1 row)

表达式collation for返回传递给它的值的排序规则。例子：

SELECT collation for (description) FROM pg\_description LIMIT 1;

pg\_collation\_for

\------------------

"default"

(1 row)

SELECT collation for ('foo' COLLATE "de\_DE");

pg\_collation\_for

\------------------

"de\_DE"

(1 row)

值可能被加上引号并且变成模式限定的。如果从参数表达式得不到排序规则，则返回一个空值。如果参数不是一个可排序的数据类型，则抛出一个错误。

to\_regclass、to\_regproc、to\_regprocedure,

to\_regoper、to\_regoperator、to\_regtype、to\_regnamespace和to\_regrole函数把关系、函数、操作符、类型、模式和角色的名称（以text给出）分别转换成、regclass、regproc、regprocedure、regoper、regoperator、regtype、regnamespace和regrole对象。这些函数与 text 转换的不同在于它们不接受数字 OID，并且在名称无法找到时不会抛出错误而是返回空。对于to\_regproc和to\_regoper，如果给定名称匹配多个对象时返回空。

表 8.72列出了与数据库对象标识和定位有关的函数。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_describe\_object(catalog\_id, object\_id, object\_sub\_id) | text | 得到一个数据库对象的描述 |
| pg\_identify\_object(catalog\_id oid, object\_id oid, object\_sub\_id integer) | type text, schema text, name text, identity text | 得到一个数据库对象的标识 |
| pg\_identify\_object\_as\_address(catalog\_id oid, object\_id oid, object\_sub\_id integer) |  | 得到一个数据库对象的地址的外部表示 |
| pg\_get\_object\_address(type text, name text\[\], args text\[\]) | class\_id oid, object\_id oid, object\_sub\_id int32 | 从一个数据库对象的内部表示得到它的地址 |

: 表 8.72 对象信息和定位函数

pg\_describe\_object返回由目录OID、对象OID以及子对象ID（例如表中的一个列号，当子对象引用了一整个对象时其ID为零）指定的数据库对象的文本描述。这种描述是为了人类可读的，并且可能是被翻译过的，具体取决于服务器配置。这有助于确定一个存储在pg\_depend目录中的对象的标识。

pg\_identify\_object返回一行，其中包含有足以唯一标识 由目录 OID、对象 OID 和一个（可能为零的）子对象 ID 指定的数据库对象的信息。 该信息是共机器读取的，并且不会被翻译。type标识数据库对象 的类型；schema是该对象所属的模式名，如果对象类型不属于 模式则为NULL；如果名称（加上方案名，如果相关）足以唯一标识对象，则name就是对象的名称（必要时会被加上引号），否则为NULL；identity是完整的对象标识， 它会表现为与对象类型相关的精确格式，并且如有必要，该格式中的每个部分都会 被模式限定。

pg\_identify\_object\_as\_address返回一行，其中包含有 足以唯一标识由目录 OID、对象OID 和一个（可能为零的）子对象 ID 指定的数据 库对象的信息。返回的信息独立于当前服务器，也就是说，它可以被用来在另一个 服务器中标识一个具有相同命名的对象。type标识数据库对象 的类型；object\_names和object\_args是文本数组，它们一起 构成了对对象的引用。这三个值可以被传递给 pg\_get\_object\_address以获得该对象的内部地址。这个函数是 pg\_get\_object\_address的逆函数。

pg\_get\_object\_address返回一行，其中包含有足以唯一 标识由类型、对象名和参数数组指定的数据库对象的信息。返回值可以被用在诸如 pg\_depend等系统目录中并且可以被传递给 pg\_identify\_object或pg\_describe\_object等其他 系统函数。class\_id是包含该对象的系统目录 OID； objid是对象本身的 OID，而 objsubid是子对象 ID，如果没有则为零。这个函数是 pg\_identify\_object\_as\_address的逆函数。

表 8.73中展示的函数抽取注释，注释是由COMMENT命令在以前存储的。如果对指定参数找不到注释，则返回空值。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| col\_description(table\_oid, column\_number) | text | 为一个表列获得注释 |
| obj\_description(object\_oid, catalog\_name) | text | 为一个数据库对象获得注释 |
| obj\_description(object\_oid) | text | 为一个数据库对象获得注释 （已被废弃） |
| shobj\_description(object\_oid, catalog\_name) | text | 为一个共享数据库对象获得 注释 |

: 表 8.73 注释信息函数

col\_description为一个表列返回注释，该表列由所在表的 OID 和它的列号指定（obj\_description不能被用在表列，因为表列没有自己的 OID）。

obj\_description的双参数形式返回一个由其 OID 和所在系统目录名称指定的数据库对象的注释。例如obj\_description(123456,'pg\_class')将会检索出 OID 为123456的表的注释。obj\_description的单参数形式只要求对象 OID。它已经被废弃，因为无法保证 OID 在不同系统目录之间是唯一的；这样可能会返回错误的注释。

shobj\_description用起来就像obj\_description，但是前者是用于检索共享对象上的注释。

某些系统目录对于一个集簇中的所有数据库是全局的，并且其中的对象的描述也是全局存储的。

表 8.74中展示的函数以一种可导出的形式提供了服务器事务信息。这些函数的主要用途是判断在两个快照之间哪些事务被提交。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| txid\_current() | bigint | 获得当前事务 ID，如果当前 事务没有 ID 则分配一个新的 ID |
| txid\_current\_if\_assigned() | bigint | 与txid\_current()相同，但 是在事务没有分配ID时是返 回空值而不是分配一个新的 事务ID |
| txid\_current\_snapshot() | txid\_snapshot | 获得当前快照 |
| txid\_snapshot\_xip(txid\_snapshot ) | setof bigint | 获得快照中正在进行的事务 ID |
| txid\_snapshot\_xmax(txid\_snapshot) | bigint | 获得快照的xmax |
| txid\_snapshot\_xmin(txid\_snapshot) | bigint | 获得快照的xmin |
| txid\_visible\_in\_snapshot(bigint, txid\_snapshot) | bigint | 事务 ID 在快照中可见吗？（不能用于子事务 ID） |

: 表 8.74 事务 ID 和快照

内部事务 ID 类型（xid）是 32 位宽并且每 40 亿个事务就会回卷。但是，这些函数导出一种 64 位格式，它被使用一个”世代”计数器，这样在一个安装的生命期内不会回卷。这些函数使用的数据类型txid\_snapshot存储了在一个特定时刻有关事务 ID 可见性的信息。它的成分在表 8.75中描述。

| **名称** | **描述** |
| --- | --- |
| xmin | 仍然活动的最早的事务 ID （txid）。所有更早的事务要么已经被提交并且可见，要么已经被回滚并且死亡。 |
| xmax | 第一个还未分配的 txid。所有大于等于它的 txid 在快照的时刻还没有开始，并且因此是 不可见的。 |
| xip\_list | 在快照时刻活动的 txid。这个列表只包括那些位于xmin和xmax之间的活动 txid；可能 有活动的超过xmax的 txid。一个满足xmin <= txid < xmax并且不在这个列表中的 txid 在快照时刻已经结束，并且因此根据其 提交状态要么可见要么死亡。该列表不包括子事务的 txid。 |

: 表 8.75 快照成分

txid\_snapshot的文本表示是xmin:xmax:xip\_list。例如10:20:10,14,15表示xmin=10, xmax=20, xip\_list=10, 14, 15。

txid\_status(bigint)报告一个近期事务的提交状态。当一个应用和数据库服务器的连接在COMMIT正在进行时断开，应用可以用它来判断事务是提交了还是中止了。一个事务的状态将被报告为in progress、committed或者aborted，前提是该事务的发生时间足够近，这样系统才会保留它的提交状态。如果事务太老，则系统中不会留下对该事务的引用并且提交状态信息也已经被抛弃，那么这个函数将会返回NULL。注意，预备事务会被报告为in progress，如果应用需要判断该txid是否是一个预备事务，应用必须检查pg\_prepared\_xacts。

表 8.76中展示的函数提供了有关于已经提交事务的信息。这些函数主要提供有关事务何时被提交的信息。只有当 track\_commit\_timestamp配置选项被启用时它们才能 提供有用的数据，并且只对已提交事务提供数据。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_xact\_commit\_timestamp(xid) | timestamp with time zone | 得到一个事务的提交时间戳 |
| pg\_last\_committed\_xact() | xid xid, timestamp timestamp with time zone | 得到最后一个已提交事务的事务 ID 和提交时间戳 |

: 表 8.76 已提交事务信息

表 8.77中所展示的函数能打印initdb期间初始化的信息，例如系统目录版本。它们也能显示有关预写式日志和检查点处理的信息。这些信息是集簇范围内的，不与任何特定的一个数据库相关。对于同一种来源，它们返回和pg\_controldata大致相同的信息，不过其形式更适合于SQL函数。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_control\_checkpoint() | record | 返回有关当前检查点状态的 信息。 |
| pg\_control\_system() | record | 返回有关当前控制文件状态 的信息。 |
| pg\_control\_init() | record | 返回有关集簇初始化状态的 信息。 |
| pg\_control\_recovery() | record | 返回有关恢复状态的信息。 |

: 表 8.77 控制数据函数

pg\_control\_checkpoint返回一个表8.78中所示的记录

| **列名** | **数据类型** |
| --- | --- |
| checkpoint\_location | pg\_lsn |
| redo\_lsn | pg\_lsn |
| redo\_wal\_file | text |
| timeline\_id | integer |
| prev\_timeline\_id | integer |
| full\_page\_writes | boolean |
| next\_xid | text |
| next\_oid | oid |
| next\_multixact\_id | xid |
| next\_multi\_offset | xid |
| oldest\_xid | xid |
| oldest\_xid\_dbid | oid |
| oldest\_active\_xid | xid |
| oldest\_multi\_xid | xid |
| oldest\_multi\_dbid | oid |
| oldest\_commit\_ts\_xid | xid |
| newest\_commit\_ts\_xid | xid |
| checkpoint\_time | timestamp with time zone |

: 表 8.78 pg\_control\_checkpoint列

pg\_control\_system返回一个表 8.79中所示的记录

| **列名** | **数据类型** |
| --- | --- |
| pg\_control\_version | integer |
| catalog\_version\_no | integer |
| system\_identifier | bigint |
| pg\_control\_last\_modified | timestamp with time zone |

: 表 8.79 pg\_control\_system列

pg\_control\_init返回一个表8.80中所示的记录

| **列名** | **数据类型** |
| --- | --- |
| max\_data\_alignment | integer |
| database\_block\_size | integer |
| blocks\_per\_segment | integer |
| wal\_block\_size | integer |
| bytes\_per\_wal\_segment | integer |
| max\_identifier\_length | integer |
| max\_index\_columns | integer |
| max\_toast\_chunk\_size | integer |
| large\_object\_chunk\_size | integer |
| float4\_pass\_by\_value | integer |
| float8\_pass\_by\_value | integer |
| data\_page\_checksum\_version | integer |

: 表 8.80 pg\_control\_init列

pg\_control\_recovery返回一个表8.81中所示的记录

| **列名** | **数据类型** |
| --- | --- |
| min\_recovery\_end\_lsn | pg\_lsn |
| min\_recovery\_end\_timeline | integer |
| backup\_start\_lsn | pg\_lsn |
| backup\_end\_lsn | pg\_lsn |
| end\_of\_backup\_record\_required | boolean |

: 表 8.81 pg\_control\_recovery列

## 系统管理函数

这一节描述的函数被用来控制和监视一个瀚高数据库安装。

### 配置设定函数

表 8.82展示了那些可以用于查询以及修改运行时配置参数的函数。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| current\_setting(setting\_name \[, missing\_ok \]) | text | 获得设置的当前值 |
| set\_config(setting\_name, new\_value, is\_local) | text | 设置一个参数并返回新值 |

: 表 8.82 配置设定函数

current\_setting得到setting\_name设置的当前值。它对应于SQL命令SHOW。一个例子：

SELECT current\_setting('datestyle');

current\_setting

\-----------------

ISO, MDY

(1 row)

如果没有名为setting\_name的设置，除非提供missing\_ok并且其值为true，current\_setting会抛出错误。

set\_config将参数setting\_name设置为new\_value。如果 is\_local设置为true，那么新值将只应用于当前事务。 如果你希望新值应用于当前会话，那么应该使用false。 它等效于 SQL命令 SET。例如：

SELECT set\_config('log\_statement\_stats', 'off', false);

set\_config

\------------

off

(1 row)

### 服务器信号函数

在表8.83中展示的函数向其它服务器进程发送控制信号。默认情况下这些函数只能被sysdba用户使用，但是如果需要，可以利用GRANT把访问特权授予给其他用户。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_cancel\_backend(pid int) | boolean | 取消一个后端的当前查询。 如果调用角色是被取消后端 的拥有者角色的成员或者调用角色已经被授予pg\_signal\_backend，这也是允许的，不过只有sysdba用户才能取消sysdba用户的后端。 |
| pg\_reload\_conf() | boolean | 导致服务器进程重载它们的配置文件 |
| pg\_rotate\_logfile() | boolean | 切换服务器的日志文件 |
| pg\_terminate\_backend(pid int) | boolean | 中止一个后端。如果调用角色是被取消后端的拥有者角色的成员或者调用角色已经被授予pg\_signal\_backend， 这也是允许的，不过只有超级用户才能取消sysdba用户的后端。 |

: 表 8.83 服务器信号函数

这些函数中的每一个都在成功时返回true，并且在失败时返回false。

pg\_cancel\_backend和pg\_terminate\_backend向由进程 ID 标识的后端进程发送信号（分别是SIGINT或SIGTERM）。一个活动后端的进程 ID可以从pg\_stat\_activity视图的pid列中找到，或者通过在服务器上列出postgres进程（在 Unix 上使用ps）得到。一个活动后端的角色可以在pg\_stat\_activity视图的usename列中找到。

pg\_reload\_conf给服务器发送一个SIGHUP信号， 导致所有服务器进程重载配置文件。

pg\_rotate\_logfile给日志文件管理器发送信号，告诉它立即切换到一个新的输出文件。这个函数只有在内建日志收集器运行时才能工作，因为否则就不存在日志文件管理器子进程。

subprocess.

### 备份控制函数

表 8.84中展示的函数可以辅助制作在线备份。这些函数不能在恢复期间执行（非排他性的pg\_start\_backup，非排他性的pg\_stop\_backup，pg\_is\_in\_backup、pg\_backup\_start\_time和pg\_wal\_lsn\_diff除外）。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_create\_restore\_point(name text) | pg\_lsn | 为执行恢复创建一个命名点 （默认只限于sysdba用户，但 是可以授予其他用户 EXECUTE 特权来执行该函数） |
| pg\_current\_wal\_flush\_lsn() | pg\_lsn | 得到当前的预写式日志刷写 位置 |
| pg\_current\_wal\_insert\_lsn() | pg\_lsn | 获得当前预写式日志插入位 置 |
| pg\_current\_wal\_lsn() | pg\_lsn | 获得当前预写式日志写入位 置 |
| pg\_start\_backup(label text \[, fast boolean \[, exclusive boolean \]\]) | pg\_lsn | 准备执行在线备份（默认只 限于sysdba用户或者复制角 色，但是可以授予其他用户 EXECUTE 特权来执行该函数） |
| pg\_stop\_backup() | pg\_lsn | 完成执行排他的在线备份 （默认只限于sysdba用户或者 复制角色，但是可以授予其 他用户 EXECUTE 特权来执行 该函数） |
| pg\_stop\_backup(exclusive boolean) | setof record | 结束执行排他或者非排他的 在线备份 （默认只限于sysdba 用户，但是可以授予其他用 户 EXECUTE 特权来执行该函 数） |
| pg\_is\_in\_backup() | bool | 如果一个在线排他备份仍在 进行中则为真。 |
| pg\_backup\_start\_time() | timestamp with time zone | 获得一个进行中的在线排他 备份的开始时间 |
| pg\_switch\_wal() | pg\_lsn | 强制切换到一个新的预写式 日志文件（默认只限于sysdba 用户，但是可以授予其他用 户 EXECUTE 特权来执行该函 数） |
| pg\_walfile\_name(lsn text) | pg\_lsn | 转换预写式日志位置字符串 为文件名 |
| pg\_walfile\_name\_offset(lsn text) | pg\_lsn, integer | 转换预写式日志位置字符串 为文件名以及文件内的十进 制字节偏移 |
| pg\_wal\_lsn\_diff(lsn pg\_lsn, lsn pg\_lsn) | numeric | 计算两个预写式日志位置间 的差别 |

: 表 8.84 备份控制函数

pg\_start\_backup接受一个参数，这个参数可以是备份的任意用户定义的标签（通常这是备份转储文件将被存储的名字）。当被用在排他模式中时，该函数向数据库集簇的数据目录写入一个备份标签文件（backup\_label）和一个表空间映射文件（tablespace\_map，如果在pg\_tblspc/目录中有任何链接），执行一个检查点，然后以文本方式返回备份的起始预写式日志位置。用户可以忽略这个结果值，但是为了可能需要的场合我们还是提供该值。 当在非排他模式中使用时，这些文件的内容会转而由pg\_stop\_backup函数返回，并且应该由调用者写入到备份中去。

highgo=# select pg\_start\_backup('label\_goes\_here');

pg\_start\_backup

\-----------------

0/D4445B8

(1 row)

第二个参数是可选的，其类型为boolean。如果为true，它指定尽快执行pg\_start\_backup。

这会强制一个立即执行的检查点，它会导致 I/O 操作的峰值，拖慢任何并发执行的查询。

在一次排他备份中，pg\_stop\_backup会移除标签文件以及pg\_start\_backup创建的tablespace\_map文件（如果存在）。在一次非排他备份中，backup\_label和tablespace\_map的内容会包含在该函数返回的结果中，并且应该被写入到该备份的文件中（这些内容不在数据目录中）。有一个可选的boolean类型的第二参数。

如果为假，pg\_stop\_backup将在备份完成后立即返回而不等待WAL被归档。这种行为仅对独立监控WAL归档的备份软件有用。否则，让备份一致所要求的WAL可能会丢失，进而让备份变得毫无用处。当这个参数被设置为真时，在启用归档的前提下pg\_stop\_backup将等待WAL被归档，在后备服务器上，这意味只有archive\_mode = always时才会等待。如果主服务器上的写活动很低，在主服务器上运行pg\_switch\_wal以触发一次即刻的段切换会很有用。

当在主服务器上执行时，该函数还在预写式日志归档区里创建一个备份历史文件。这个历史文件包含给予pg\_start\_backup的标签、备份的起始与终止预写式日志位置以及备份的起始和终止时间。返回值是备份的终止预写式日志位置（同样也可以被忽略）。在记录结束位置之后，当前预写式日志插入点被自动地推进到下一个预写式日志文件，这样结束的预写式日志文件可以立即被归档来结束备份。

pg\_switch\_wal移动到下一个预写式日志文件，允许当前文件被归档（假定你正在使用连续归档）。返回值是在甘冈完成的预写式日志文件中结束预写式日志位置 + 1。如果从上一次预写式日志切换依赖没有预写式日志活动，pg\_switch\_wal不会做任何事情并且返回当前正在使用的预写式日志文件的开始位置。

pg\_create\_restore\_point创建一个命名预写式日志记录，它可以被用作恢复目标，并且返回相应的预写式日志位置。这个给定的名字可以用于recovery\_target\_name来指定恢复要进行到的点。避免使用同一个名称创建多个恢复点，因为恢复会停止在第一个匹配名称的恢复目标。

pg\_current\_wal\_lsn以上述函数所使用的相同格式显示当前预写式日志的写位置。类似地，pg\_current\_wal\_insert\_lsn显示当前预写式日志插入点，而pg\_current\_wal\_flush\_lsn显示当前预写式日志的刷写点。在任何情况下，插入点是预写式日志的”逻辑”终止点，而写入位置是已经实际从服务器内部缓冲区写出的日志的终止点，刷写位置则是被确保写入到持久存储中的日志的终止点。写入位置是可以从服务器外部检查的终止点，对那些关注归档部分完成预写式日志文件的人来说，这就是他们需要的位置。插入和刷写点主要是为了服务器调试目的而存在的。这些都是只读操作并且不需要sysdba用户权限。

你可以使用pg\_walfile\_name\_offset从任何上述函数的结果中抽取相应的预写式日志文件名称以及字节偏移。例如：

highgo=# SELECT \* FROM pg\_walfile\_name\_offset(pg\_stop\_backup());

file\_name | file\_offset

\--------------------------+-------------

00000001000000000000000D | 4039624

(1 row)

相似地，pg\_walfile\_name只抽取预写式日志文件名。当给定的预写式日志位置正好在一个预写式日志文件的边界，这些函数都返回之前的预写式日志文件的名称。这对管理预写式日志归档行为通常是所希望的行为，因为前一个文件是当前需要被归档的最后一个文件。

pg\_wal\_lsn\_diff以字节数计算两个预写式日志位置之间的差别。它可以和pg\_stat\_replication或表8.84中其他的函数一起使用来获得复制延迟。

### 恢复控制函数

表8.85中展示的函数提供有关后备机当前状态的信息。这些函数可以在恢复或普通运行过程中被执行。

| 名称 | 返回类型 | 描述 |
| --- | --- | --- |
| pg\_is\_in\_recovery() | bool | 如果恢复仍在进行中，为真。 |
| pg\_last\_wal\_receive\_lsn() | pg\_lsn | 获得最后一个收到并由流复制同步到磁盘的预写式日志位置。当流复制在进行时，这将单调增加。如果恢复已经完成，这将保持静止 在恢复过程中收到并同步到磁盘的最后一个 WAL 记录。 如果流复制被禁用，或者还没有被启动，该函数返回NULL。 |
| pg\_last\_wal\_replay\_lsn() | pg\_lsn | 获得恢复过程中被重放的最后一个预写式日志位置。当流复制在进行中时，这将单调增加。如果恢复已经完成，这将保持静止在恢复过程中被应用的最后一个 WAL记录。如果服务器被正常启动而没有恢复，该函数返回NULL。 |
| pg\_last\_xact\_replay\_timestamp() | p() timestamp with time zone | 获得恢复过程中被重放的最后一个事务的时间戳。这是在主机上产生的事务的提交或中止 WAL 记录的时间。如果在恢复过程中没有事务被重放，这个函数返回 NULL。 否则，如果恢复仍在进行这将单调增加。如果恢复已经完成，则这个值会保持静止在恢复过程中最后一个被应用的事务。如果服务器被正 常启动而没有恢复，该函数返回 NULL。 |

: 表 8.85 恢复信息函数

表8.86中展示的函数空值恢复的进程。这些函数只能在恢复过程中被执行。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_is\_wal\_replay\_paused() | bool | 如果恢复被暂停，为真。 |
| pg\_promote(wait boolean DEFAULT true, wait\_seconds integer DEFAULT 60) | boolean | 促进物理备用服务器。 当wait设置为true（默认值）时，该函数将等待晋升完成或wait\_seconds秒，如果晋升成功，则返回true，否则返回false。如果wait被设置为false，则会返回true。函数在发送后立即返回true。SIGUSR1给postmaster触发推广。此功能默认只限于sysdba用户，但其他用户 可以被授予EXECUTE来运行函数。 |
| pg\_wal\_replay\_pause() | void | 立即暂停恢复（默认仅限于sysdba用户, 但是可以授予其他用户EXECUTE 特权来执行该函数）。 |
| pg\_wal\_replay\_resume() | void | 如果恢复被暂停，重启之（默认仅限于sysdba用户，但是可以授予其他用户 EXECUTE特权来执行该函数）。 |

: 表 8.86 恢复控制函数

在恢复被暂停时，不会有进一步的数据库改变被应用。如果在热备模式，所有新的查询将看到数据库的同一个一致快照，并且在恢复被继续之前不会有更多查询冲突会产生。

如果流复制被禁用，暂停状态可以无限制地继续而不出问题。在流复制进行时，WAL 记录将继续被接收，最后将会填满可用的磁盘空间，取决于暂停的持续时间、WAL 的产生率和可用的磁盘空间。

### 快照同步函数

瀚高数据库允许数据库会话同步它们的快照。一个快照决定对于正在使用该快照的事务哪些数据是可见的。当两个或者更多个会话需要看到数据库中的相同内容时，就需要同步快照。

如果两个会话独立开始其事务，就总是有可能有某个第三事务在两个START TRANSACTION命令的执行之间提交，这样其中一个会话就可以看到该事务的效果而另一个则看不到。

为了解决这个问题，瀚高数据库允许一个事务导出它正在使用的快照。只要导出的事务仍然保持打开，其他事务可以导入它的快照，并且因此可以保证它们可以看到和第一个事务看到的完全一样的数据库视图。但是注意这些事务中的任何一个对数据库所作的更改对其他事务仍然保持不可见，和未提交事务所作的修改一样。因此这些事务是针对以前存在的数据同步，而对由它们自己所作的更改则采取正常的动作。

如表 8.87中所示，快照通过pg\_export\_snapshot函数导出，并且通过SET TRANSACTION命令导入。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_export\_snapshot() | text | 保存当前快照并返回它的标识符 |

: 表 8.87 快照同步函数

函数pg\_export\_snapshot保存当前的快照并且返回一个text串标识该快照。该字符串必须被传递（到数据库外）给希望导入快照的客户端。直到导出快照的事务的末尾，快照都可以被导入。如果需要，一个事务可以导出多于一个快照。注意这样做只在 READ COMMITTED事务中有用，因为在REPEATABLE READ和更高隔离级别中，事务在它们的生命期中都使用同一个快照。一旦一个事务已经导出了任何快照，它不能使用PREPARE TRANSACTION。

关于如何使用一个已导出快照的细节请见SET TRANSACTION.

### 复制函数

表8.88中展示的函数用于控制以及与复制特性交互。复制原点函数的使用仅限于sysdba用户。 复制槽的函数只限于sysdba用户和拥有REPLICATION权限的用户。

第 8.26.3 节、 第8.26.4 节和 第8.26.5 节 中描述的函数也与复制相关。

| **函数** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_create\_physical\_replication\_slot(slot\_name name \[,immediately\_reserve boolean \]) | (slot\_name name, xlog\_position pg\_lsn) | 创建一个新的名为slot\_name的物理复制槽。 第二个参数是可选的，当它为true时，立即为这个物理槽指定要被保留的LSN。否则该LSN会被保留在来自一个流复制客户端的第一个连接上。来自一个物理槽的流改变只可能出现在使用流复制协议时 — 见第 52.4 节。当可选的第三参数temporary被设置为真时，指定那个槽不会被持久地存储在磁盘上并且仅对当前会话的使用有意。临时槽也会在发生任何错时被释放。这个函数对应于复制协议命令CREATE\_REPLICATION\_SLOT … PHYSICAL。 |
| pg\_drop\_replication\_slot(slot\_name name) | void | 丢弃名为slot\_name的物理或逻辑复制槽。 和复制协议命令DROP\_REPLICATION\_SLOT相同。对于逻辑槽，在连接到在其中创建该槽的同一个数据库时，必须调用这个函数。 |
| pg\_create\_logical\_replication\_slot(slot\_name name, plugin name) | (slot\_name name, lsn pg\_l） | 使用输出插件plugin创建一个名为 slot\_name的新逻辑（解码）复制槽。当可选的第三参数temporary被设置为真时，指定那个槽不会被持久地存储在磁盘上并且仅对当前会话的使用有意义。临时槽也会在发生任何错误时被释放。对这个函数的调用与复制协议命令CREATE\_REPLICATION\_SLOT … LOGICAL具有相同的效果。 |
| pg\_copy\_physical\_replication\_slot(src\_slot\_name name, dst\_slot\_name name \[, temporary boolean\]) | (slot\_name name, lsn pg\_lsn) | 将一个名为src\_slot\_name的现有物理复制槽复制到一个名为dst\_slot\_name的物理复制槽。被复制的物理槽开始从与源槽相同的LSN开始保留WAL。temporary是可选的。如果省略了temporary，则使用与源槽相同的值。 |
| pg\_copy\_logical\_replication\_slot(src\_slot\_name name, dst\_slot\_name name \[, temporary boolean \[, plugin name\]\]) | (slot\_name name, lsn pg\_lsn) | 复制一个名为src\_slot\_name的现有逻辑复制槽。到一个名为dst\_slot\_name的逻辑复制槽。同时改变输出插件和持久性。被复制的逻辑槽开始来自与源逻辑槽相同的LSN。这两个 temporary和plugin是可选的。如果省略了temporary或plugin。使用与源逻辑槽相同的值。 |
| pg\_logical\_slot\_get\_changes(slot\_name name, upto\_lsn pg\_lsn, upto\_nchanges int, VARIADIC options text\[\]) | (lsn pg\_lsn, xid xid, data text) | 返回槽slot\_name中的改变，从上一次已经被消费的点开始返回。 如果upto\_lsn和upto\_nchanges为NULL，逻辑解码将一 直继续到 WAL 的末尾。如果upto\_lsn为非 NULL，解码将只包括那些在指 定LSN 之前提交的事务。如果upto\_nchanges为非 NULL，解码将在其产生的行数超过指定值后停止。不过要注意， 被返回的实际行数可能更大，因为对这个限制的检查只会在增加了解码每个新的提交事务产生 的行之后进行。 |
| pg\_logical\_slot\_peek\_changes(slot\_name name, upto\_lsn pg\_lsn, upto\_nchanges int, VARIADIC options text\[\]) | (lsn text, xid xid, data text) | 行为就像pg\_logical\_slot\_get\_changes()函数， 不过改变不会被消费， 即在未来的调用中还会返回这些改变。 |
| pg\_logical\_slot\_get\_binary\_changes(slot\_name name, upto\_lsn pg\_lsn, upto\_nchanges int, VARIADIC options text\[\]) | (lsn pg\_lsn, xid xid, data bytea) | 行为就像pg\_logical\_slot\_get\_changes()函数， 不过改变会以bytea返回。 |
| pg\_logical\_slot\_peek\_binary\_changes(slot\_name name, upto\_lsn pg\_lsn, upto\_nchanges int, VARIADIC options text\[\]) | (lsn pg\_lsn, xid xid, data bytea) | 行为就像pg\_logical\_slot\_get\_changes()函数， 不过改变会以bytea返回并且这些改变不会被消费，即在未来的调用中还会返回这些改变。 |
| pg\_replication\_slot\_advance(slot\_name name, upto\_lsn pg\_lsn) | (slot\_name name, end\_lsn pg\_lsn） | 将复制槽的当前确认的位置提前到名为slot\_name的复制槽的当前确认位置。该槽不会向后移动，也不会移动到当前插入位置之外。返回该槽的名称和它被推进到的真实位置。 如果有任何推进，则在后续的检查点中写出更新后的槽的信息。如果发生崩溃，该槽位可能会返回到之前的位置。 |
| pg\_replication\_origin\_create(node\_name text) | oid | 用给定的外部名称创建一个复制源，并且返回分配给它的内部 id。 |
| pg\_replication\_origin\_drop(node\_name text) | void | 删除一个之前创建的复制源，包括任何相关的重放进度 |
| pg\_replication\_origin\_oid(node\_name text) | oid | 用名称查找复制源并且返回内部 id。如果没有找到则抛出错误。 |
| pg\_replication\_origin\_session\_setup(node\_name text) | void | 把当前会话标记为正在从给定的源进行重放，允许重放进度被跟踪。使用pg\_replication\_origin\_session\_reset可以取消 标记。只有之前没有源被配置时才能使用。 |
| pg\_replication\_origin\_session\_reset() | bool | 当前会话中是否已经配置了一个复制源？ |
| pg\_replication\_origin\_session\_progress(flush bool) | pg\_lsn | 返回当前会话中配置的复制源的重放位置。参数 flush决定对应的本地事务是否被确保 已经刷入磁盘。 |
| pg\_replication\_origin\_xact\_setup(origin\_lsn pg\_lsn, origin\_timestamp timestamptz) | void | 标记当前事务为正在重放一个已经在给定的LSN 和时间戳提交的事务。只有当之前已经用pg\_replication\_origin\_session\_setup()配置过 一个复制源时才能被调用。 |
| pg\_replication\_origin\_xact\_reset() | void | 把给定节点的复制进度设置为给定的位置。这主要用于配置更改或者类似 操作之后设置初始位置或者新位置。 注意这个函数的不当使用可能会导致 不一致的复制数据。 |
| pg\_replication\_origin\_progress(node\_name text, flush bool) | pg\_lsn | 返回给定复制元的重放位置。参数 flush决定对应的本地事务是否被确保 已经刷入磁盘。 |
| pg\_logical\_emit\_message(transactional bool, prefix text, content text) | pg\_lsn | 发出文本形式的逻辑解码消息。这可以被用来通过 WAL向逻辑解码插件传递一般消息。参数transactional指定该消息是否应该是当前事务的一部分或者当逻辑解码读到该记录时该消息是否应该被立刻写入并且解码。prefix是逻辑解码插件用来识别它们感兴趣的消息的文本前缀。content是消息的文本。 |
| pg\_logical\_emit\_message(transactional bool, prefix text, content bytea) | nsactional | 发出二进制逻辑解码消息。这可以被用来通过WAL向逻辑解码插件传递一般性消息。 参数transactional指定该消息是否应该成为当前事务的一部分或者是否应该在逻辑解码过程读到该记录时立刻进行写入和解码。参数prefix是一个逻辑解码插使用的文本前缀，逻辑解码插件用它来识别感兴趣的消息。参数content是消息的二进制内容。 |

: 表 8.88 复制函数

### 数据库对象管理函数

表 8.89中展示的函数计算数据库对象使用的磁盘空间。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_column\_size(any) | int | 存储一个特定值（可能压缩过）所需的字节数 |
| pg\_database\_size(oid) | bigint | 指定 OID 的数据库使用的磁盘空间 |
| pg\_database\_size(name) | bigint | 指定名称的数据库使用的磁盘空间 |
| pg\_indexes\_size(regclass) | bigint | 附加到指定表的索引所占的总磁盘空间 |
| pg\_relation\_size(relation regclass, fork text) | bigint | 指定表或索引的指定分叉 （’main’、’fsm’、’vm’或’init’）使用的磁盘空间 |
| pg\_relation\_size(relation regclass) | bigint | pg\_relation\_size(…,’main’)的简写 |
| pg\_size\_bytes(text) | bigint | 把人类可读格式的带有单位的尺寸转换成字节数 |
| pg\_size\_pretty(bigint) | text | 将表示成一个 64位整数的字节尺寸转换为带尺寸单位的人类可读格式 |
| pg\_size\_pretty(numeric) | text | 将表示成一个数字值的字节尺寸转换为带尺寸单位的人类可读格式 |
| pg\_table\_size(regclass) | bigint | 被指定表使用的磁盘空间，排除索引（但包括 TOAST、空闲空间映射和可见性映射） |
| pg\_tablespace\_size(oid) | bigint | 指定 OID 的表空间使用的磁盘空间 |
| pg\_tablespace\_size(name) | bigint | 指定名称的表空间使用的磁盘空间 |
| pg\_total\_relation\_size(regclass ) | bigint | 指定表所用的总磁盘空间，包括所有的索引和TOAST数据 |

: 表 8.89 数据库对象尺寸函数

pg\_column\_size显示用于存储任意独立数据值的空间。

pg\_total\_relation\_size接受一个表或 TOAST 表的 OID 或名称，并返回该表所使用的总磁盘空间，包括所有相关的索引。这个函数等价于pg\_table\_size + pg\_indexes\_size。

pg\_table\_size接受一个表的 OID 或名称，并返回该表所需的磁盘空间，但是排除索引（TOAST 空间、空闲空间映射和可见性映射包含在内）

pg\_indexes\_size接受一个表的 OID 或名称，并返回附加到该表的所有索引所使用的全部磁盘空间。

pg\_database\_size以及pg\_tablespace\_size接受数据库或者表空间的OID或者名称，并且返回它们使用的磁盘空间。要使用pg\_database\_size，用户必须具有指定数据库上的CONNECT权限（默认情况下已经被授予）或者是pg\_read\_all\_stats角色的一个成员。要使用pg\_tablespace\_size，用户必须具有指定表空间上的CREATE权限或者是pg\_read\_all\_stats角色的一个成员，除非该表空间是当前数据库的默认表空间。

pg\_relation\_size接受一个表、索引或 TOAST 表的 OID 或者名称，并且返回那个关系的一个分叉所占的磁盘空间的字节尺寸（注意 对于大部分目的，使用更高层的函数pg\_total\_relation\_size 或者pg\_table\_size会更方便，它们会合计所有分叉的尺寸）。

如果只得到一个参数，它会返回该关系的主数据分叉的尺寸。提供第二个参数 可以指定要检查哪个分叉：

• 'main'返回该关系主数据分叉的尺寸。

• 'fsm'返回与该关系相关的空闲空间映射（见 第 68.3 节）的尺寸。

• 'vm'返回与该关系相关的可见性映射（见 第 68.4 节）的尺寸。

• 'init'返回与该关系相关的初始化分叉（如 果有）的尺寸。

pg\_size\_pretty可以用于把其它函数之一的结果格式化成一种人类易读的格式，可以根据情况使用字节、kB、MB、GB 或者 TB。

pg\_size\_bytes可以被用来从人类可读格式的字符串得到其中所表示的字节数。其输入可能带有的单位包括字节、kB、MB、GB 或者 TB，并且对输入进行解析时是区分大小写的。如果没有指定单位，会假定单位为字节。

| 注意： |
| --- |
| 函数pg\_size\_pretty和pg\_size\_bytes所使用的单位 kB、MB、GB 和 TB 是用2 的幂而不是 10 的幂来定义，因此 1kB 是 1024 字节，1MB 是 10242 = 1048576 字节，以此类推。 |

上述操作表和索引的函数接受一个regclass参数，它是该表或索引在pg\_class系统目录中的OID。你不必手工去查找该 OID，因为regclass数据类型的输入转换器会为你代劳。只写包围在单引号内的表名，这样它看起来像一个文字常量。为了与普通SQL名称的处理相兼容，该字符串将被转换为小写形式，除非其中在表名周围包含双引号。

如果一个 OID 不表示一个已有的对象并且被作为参数传递给了上述函数，将会返回 NULL。

表 8.90中展示的函数帮助标识数据库对象相关的磁盘文件。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_relation\_filenode(relation regclass) | oid | 指定关系的文件结点号 |
| pg\_relation\_filepath(relation regclass) | text | 指定关系的文件路径名 |
| pg\_filenode\_relation(tablespace oid, filenode oid) | regclass | 查找与给定的表空间和文件节点相关的关系 |

: 表 8.90 数据库对象定位函数

pg\_relation\_filenode接受一个表、索引、序列或 TOAST 表的 OID 或名称，返回当前分配给它的”filenode”号。文件结点是关系的文件名的基本组件（详见第 68.1 节）。对于大多数表结果和pg\_class.relfilenode相同，但是对于某些系统目录relfilenode为零，并且必须使用此函数获取正确的值。 如果传递一个没有存储的关系（如视图），此函数将返回 NULL。

pg\_relation\_filepath与pg\_relation\_filenode类似，但是它返回关系的整个文件路径名（相对于数据库集簇的数据目录PGDATA）。

pg\_filenode\_relation是pg\_relation\_filenode的反向函数。给定一个”tablespace” OID以及一个 “filenode”，它会返回相关关系的 OID。对于一个在数据库的默认表空间中的表，该表空间可以指定为 0。

表8.91列出了用来管理排序规则的函数。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_collation\_actual\_version(oid) |  | 返回来自操作系统的排序规则的实际版本 |
| pg\_import\_system\_collations(schema regnamespace) | integer | 导入操作系统排序规则 |

: 表 8.91 排序规则管理函数

pg\_collation\_actual\_version返回当前安装在操作系统中的该排序规则对象的实际版本。

如果这个版本与pg\_collation.collversion中的值不同，则依赖于该排序规则的对象可能需要被重建。还可以参考ALTER COLLATION。

pg\_import\_system\_collations基于在操作系统中找到的所有locale在系统目录pg\_collation中加入排序规则。这是initdb会使用的函数。如果后来在操作系统上安装了额外的locale，可以再次运行这个函数加入新locale的排序规则。匹配pg\_collation中现有项的locale将被跳过（但是这个函数不会移除以在操作系统中不再存在的locale为基础的排序规则对象）。schema参数通常是pg\_catalog，但这不是一种要求，排序规则也可以被安装到其他的方案中。该函数返回其创建的新排序规则对象的数量。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_partition\_tree(regclass) | setof record | 列出一个分区树中的表或索引的相关信息。给定的分区表或分区索引，每张表有一行分区。 提供的信息包括分区的名称，它的直系父级的名称，一个布尔值，表示该分区是否是一个叶子，以及一个整数，表示它在层次结构中的级别。level的值从0开始，表示输入表或索引作为分区树的根，1表示其分区，2表示其分区，以此类推。 |
| pg\_partition\_ancestors(regclass) | setof regclass | 列出给定分区的祖先关系，包括分区本身。 |
| pg\_partition\_root(regclass) | regclass | R返回给定关系所属的分区树的最上层父节点。 |

: 表 8.92 分区信息函数

要检查第4.11.2.1 节中描述的measurement表中的数据的总大小，可以使用下面的查询:

\=# SELECT pg\_size\_pretty(sum(pg\_relation\_size(relid))) AS total\_size

FROM pg\_partition\_tree('measurement');

total\_size

\------------

24 kB

(1 row)

### 索引维护函数

表 8.93展示了可用于 索引维护任务的函数。这些函数不能在恢复期间执行。只有sysdba用户以及给定索引的拥有者才能是用这些函数。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| brin\_summarize\_new\_values(index regclass) | integer | 对还没有建立概要的页面范围建立概要 |
| brin\_summarize\_range(index regclass, blockNumber bigint) | integer | 如果还没有对覆盖给定块的页面范围建立概要，则对其建立概要 |
| brin\_desummarize\_range(index regclass, blockNumber bigint) | integer | 如果覆盖给定块的页面范围已经建立有概要，则去掉概要 |
| gin\_clean\_pending\_list(index regclass) | higint | 把 GIN 待处理列表项移动到主索引结构中 |

: 表 8.93 索引维护函数

brin\_summarize\_new\_values接收一个 BRIN 索引的 OID 或者名称作为参数并且检查该索引以找到基表中当前还没有被该索引汇总的页面范围。对任意一个这样的范围，它将通过扫描那些表页面创建一个新的摘要索引元组。它会返回被插入到该索引的新页面范围摘要的数量。brin\_summarize\_range做同样的事情，不过它只对覆盖给定块号的范围建立概要。

gin\_clean\_pending\_list接受一个 GIN 索引的 OID 或者名字，并且通过把指定索引的待处理列表中的项批量移动到主 GIN 数据结构来清理该索引的待处理列表。它会返回从待处理列表中移除的页数。注意如果其参数是一个禁用fastupdate选项构建的 GIN 索引，那么不会做清理并且返回值为 0，因为该索引根本没有待处理列表。

### 通用文件访问函数

表8.94中展示的函数提供了对数据库服务器所在机器上的文件的本地访问。只能访问数据库集簇目录以及log\_directory中的文件，除非用户被授予了角色pg\_read\_server\_files。

使用相对路径访问集簇目录里面的文件，以及匹配 log\_directory配置设置的路径访问日志文件。

注意向用户授予pg\_read\_file()或者相关函数上的EXECUTE特权，函数会允许他们读取服务器上该数据库能读取的任何文件并且这些读取动作会绕过所有的数据库内特权检查。这意味着，除了别的之外，具有这种访问的用户能够读取pg\_authid表中包含着认证信息的内容，也能读取数据库中的任意文件。因此，授予对这些函数的访问应该要很仔细地考虑。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_ls\_dir(dirname text \[, missing\_ok boolean, include\_dot\_dirs boolean\]) | setof text | 列出目录中的内容。默认仅限于sysdba用户使用，但是可以给其他用户授予EXECUTE让他们运行这个函数。 |
| pg\_ls\_logdir() | setof record | 列出日志目录中文件的名称、尺寸以及最后修改时间。访问被授予给pg\_monitor角色的成员，并且可以被授予给其他非超级用户角色。 |
| pg\_ls\_waldir() | setof record | 列出WAL目录中文件的名称、尺寸以及最后修改时间。访问被授予给pg\_monitor角色的成员，并且可以被授予给其他非sysdba用户角色。 |
| pg\_ls\_archive\_statusdir() | setof record | 列出WAL存档状态目录中文件的名称、大小和最后一次修改时间。访问权限只授予pg\_monitor角色的成员，也可以授予其他非sysdba用户角色 |
| pg\_ls\_tmpdir(\[tablespace oid\]) | setof record | 为tablespace列出临时目录中文件的名称、大小和最后一次修改时间。 如果没有提供tablespace，则在临时目录中的 pg\_default表空间被使用。 pg\_monitor角色的成员可以访问，其他非管理员用户角色也可以访问 |
| pg\_read\_file(filename text \[, offset bigint, length bigint \[, missing\_ok boolean\] \]) | text | 返回一个文本文件的内容。默认仅限于sysdba用户使用，但是可以给其他用户授予EXECUTE让他们运行这个函数。 |
| pg\_read\_binary\_file(filename text \[, offset bigint, length bigint \[, missing\_ok boolean\] \]) | bytea | 返回一个文件的内容。默认仅限于sysdba用户使用，但是可以给其他用户授予EXECUTE让他们运行这个函数。 |
| pg\_stat\_file(filename text\[, missing\_ok boolean\]) | record | 返回关于一个文件的信息。默认仅限于sysdba用户使用，但是可以给其他用户授予EXECUTE让他们运行这个函数。 |

: 表 8.94 通用文件访问函数

这些函数中的某些有一个可选的missing\_ok参数， 它指定文件或者目录不存在时的行为。

如果为true，函数会返回 NULL（pg\_ls\_dir除外，它返回一个空结果集）。如果为false，则发生一个错误。默认是 false。

pg\_ls\_dir返回指定目录中所有文件（以及目录和其他特殊文件）的名称。include\_dot\_dirs指示结果集中是否包括 “.”和”..”。默认是排除它们（false），但是当missing\_ok为true时把它们包括在内是 有用的，因为可以把一个空目录与一个不存在的目录区分开。

pg\_ls\_logdir返回日志目录中每个文件的名称、尺寸以及最后的修改时间（mtime）。默认情况下，只有sysdba用户以及pg\_monitor角色的成员能够使用这个函数。可以使用GRANT把访问授予给其他人。

pg\_ls\_waldir返回预写式日志（WAL）目录中每个文件的名称、尺寸以及最后的修改时间（mtime）。默认情况下，只有sysdba用户以及pg\_monitor角色的成员能够使用这个函数。可以使用GRANT把访问授予给其他人。

pg\_ls\_archive\_statusdir返回WAL归档状态目录pg\_wal/archive\_status中每个文件的名称、大小和最后一次修改时间（mtime）。默认情况下，只有sysdba用户和pg\_monitor角色的成员才能使用此函数。可使用GRANT授权其他用户访问。

pg\_ls\_tmpdir返回指定的tablespace临时文件目录中每个文件的名称、大小和最后一次修改时间（mtime）。如果没有提供tablespace，则使用pg\_default表空间。默认情况下，只有sysdba用户和pg\_monitor角色的成员才能使用这个函数。可使用GRANT授权其他用户访问。

pg\_read\_file返回一个文本文件的一部分，从给定的offset开始，返回最多length字节（如果先到达文件末尾则会稍短）。如果offset为负，它相对于文件的末尾。如果offset和length被忽略，整个文件都被返回。从文件中读的字节被使用服务器编码解释成一个字符串；如果它们在编码中不合法则抛出一个错误。

pg\_read\_binary\_file与pg\_read\_file相似，除了前者的结果是一个bytea值；相应地，不会执行编码检查。通过与convert\_from函数结合，这个函数可以用来读取一个指定编码的文件：

SELECT convert\_from(pg\_read\_binary\_file('file\_in\_utf8.txt'), 'UTF8');

pg\_stat\_file返回一个记录，其中包含文件尺寸、最后访问时间戳、最后修改时间戳、最后文件状态改变时间戳（只支持 Unix 平台）、文件创建时间戳和一个boolean指示它是否为目录。通常的用法包括：

SELECT \* FROM pg\_stat\_file('filename');

SELECT (pg\_stat\_file('filename')).modification;

### 咨询锁函数

表8.95中展示的函数管理咨询锁。有关正确使用这些函数的细节请参考第 12.3.5 节。

| **名称** | **返回类型** | **描述** |
| --- | --- | --- |
| pg\_advisory\_lock(key bigint) | void | 获得排他会话级别咨询锁 |
| pg\_advisory\_lock(key1 int, key2 int) | void | 获得排他会话级别咨询锁 |
| pg\_advisory\_lock\_shared(key bigint) | void | 获得共享会话级别咨询锁 |
| pg\_advisory\_lock\_shared(key1 int, key2 int) | void | 获得共享会话级别咨询锁 |
| pg\_advisory\_unlock(key bigint) | boolean | 释放一个排他会话级别咨询 锁 |
| pg\_advisory\_unlock(key1 int, key2 int) | boolean | 释放一个排他会话级别咨询 锁 |
| pg\_advisory\_unlock\_all() | void | 释放当前会话持有的所有会 话级别咨询锁 |
| pg\_advisory\_unlock\_shared(key bigint) | boolean | 释放一个共享会话级别咨询锁 |
| pg\_advisory\_unlock\_shared(key1 int, key2 int) | boolean | 释放一个共享会话级别咨询锁 |
| pg\_advisory\_xact\_lock(key bigint) | void | 获得排他事务级别咨询锁 |
| pg\_advisory\_xact\_lock(key1 int, key2 int) | void | 获得排他事务级别咨询锁 |
| pg\_advisory\_xact\_lock\_shared(key bigint) | void | 获得共享事务级别咨询锁 |
| pg\_advisory\_xact\_lock\_shared(key1 int, key2 int) | void | 获得共享事务级别咨询锁 |
| pg\_try\_advisory\_lock(key bigint) | boolean | 如果可能，获得排他会话级别咨询锁 |
| pg\_try\_advisory\_lock(key1 int, key2 int) | boolean | 如果可能，获得排他会话级别咨询锁 |
| pg\_try\_advisory\_lock\_shared(key bigint) | boolean | 如果可能，获得共享会话级别咨询锁 |
| pg\_try\_advisory\_lock\_shared(key1 int, key2 int) | boolean | 如果可能，获得共享会话级别咨询锁 |
| pg\_try\_advisory\_xact\_lock(key bigint) | boolean | 如果可能，获得排他事务级 别咨询锁 |
| pg\_try\_advisory\_xact\_lock(key1 int, key2 int) | boolean | 如果可能，获得排他事务级别咨询锁 |
| pg\_try\_advisory\_xact\_lock\_shared(key bigint) | boolean | 如果可能，获得共享事务级别咨询锁 |
| pg\_try\_advisory\_xact\_lock\_shared(key1 int, key2 int) | boolean | 如果可能，获得共享事务级别咨询锁 |

: 表 8.95 咨询锁函数

pg\_advisory\_lock锁住一个应用定义的资源，可以使用一个单一64位键值或两个32位键值标识（注意这些两个键空间不重叠）。如果另一个会话已经在同一个资源标识符上持有了一个锁，这个函数将等待直到该资源变成可用。该锁是排他的。多个锁请求会入栈，因此如果同一个资源被锁住三次，则它必须被解锁三次来被释放给其他会话使用。

pg\_advisory\_lock\_shared的工作和pg\_advisory\_lock相同，不过该锁可以与其他请求共享锁的会话共享。只有想要排他的锁请求会被排除。

pg\_try\_advisory\_lock与pg\_advisory\_lock相似，不过该函数将不会等待锁变为可用。它要么立刻获得锁并返回true，要么不能立即获得锁并返回false。

pg\_try\_advisory\_lock\_shared的工作和pg\_try\_advisory\_lock相同，不过它尝试获得一个共享锁而不是一个排他锁。

pg\_advisory\_unlock将会释放之前获得的排他会话级别咨询锁。如果锁被成功释放，它返回true。如果锁没有被持有，它将返回false并且额外由服务器报告一个 SQL 警告。

pg\_advisory\_unlock\_shared的工作和pg\_advisory\_unlock相同，除了它释放一个共享的会话级别咨询锁。

pg\_advisory\_unlock\_all将释放当前会话所持有的所有会话级别咨询锁（这个函数隐式地在会话末尾被调用，即使客户端已经不雅地断开）。

pg\_advisory\_xact\_lock的工作和pg\_advisory\_lock相同，不过锁是在当前事务的末尾被自动释放的并且不能被显式释放。

pg\_advisory\_xact\_lock\_shared的工作和pg\_advisory\_lock\_shared相同，除了锁是在当前事务的末尾自动被释放的并且不能被显式释放。

pg\_try\_advisory\_xact\_lock的工作和pg\_try\_advisory\_lock相同，不过锁（若果获得）是在当前事务的末尾被自动释放的并且不能被显式释放。

pg\_try\_advisory\_xact\_lock\_shared的工作和pg\_try\_advisory\_lock\_shared相同，不过锁（若果获得）是在当前事务的末尾被自动释放的并且不能被显式释放。

## 触发器函数

当前瀚高数据库提供一个内建的触发器函数suppress\_redundant\_updates\_trigger， 它将阻止任何不会实际更改行中数据的更新发生，这与正常的行为不管数据是否改变始终执行更新相反（这是正常的行为，使得更新运行速度更快，因为不需要检查，并在某些情况下也是有用的）。

理想的情况下，你通常应该避免运行实际上并没有改变记录中数据的更新。 冗余更新会花费大量不必要的时间，尤其是如果有大量索引要改变， 并将最终不得不清理被死亡行占用的空间。但是，在客户端代码中检测这种情况并不总是容易的，甚至不可能做到。 而写表达式来检测它们容易产生错误。作为替代，使用suppress\_redundant\_updates\_trigger可以跳过不改变数据的更新。 但是，你需要小心使用它。触发器需要很短但不能忽略的时间来处理每条记录，所以如果大多数被一个更新影响的记录确实被更改，此触发器的使用将实际上使更新运行得更慢。

suppress\_redundant\_updates\_trigger函数可以像这样被加到一个表：

CREATE TRIGGER z\_min\_update

BEFORE UPDATE ON tablename

FOR EACH ROW EXECUTE FUNCTION suppress\_redundant\_updates\_trigger();

在大部分情况下，你可能希望在最后为每行触发这个触发器。考虑到触发器是按照名字顺序被触发，你需要选择一个位于该表所有其他触发器之后的触发器名字。

有关创建触发器的更多信息请参考CREATE TRIGGER。

## 事件触发器函数

瀚高数据库提供了这些助手函数来从 事件触发器检索信息。

### 在命令结束处捕捉更改

当在一个ddl\_command\_end事件触发器的函数中调用时，pg\_event\_trigger\_ddl\_commands返回被每一个用户动作 执行的DDL命令的列表。如果在其他任何环境中 调用这个函数，会发生错误。 pg\_event\_trigger\_ddl\_commands为每一个被执行的基本命令返回一行，某些只有一个单一 SQL 句子的命令可能会返回多于一行。这个函数返回下面的列：

---

```
**名称**               **类型**                       **描述**

    classid                oid                       对象所属的目录的 OID

     objid                 oid                       对象本身的 OID

   objsubid              integer                     对象的子-id（例如列的属性号）

  command_tag             text                       命令标签

  object_type             text                       对象的类型

  schema_name             text                       该对象所属的模式的名称（如果有），如果没有则为NULL。没有引号。

object_identity           text     对象标识的文本表现形式，用模式限定。如果必要，出现在该标识中的每一个标识符都会被引用。

 in_extension             bool                       如果该命令是一个扩展脚本的一部分则为真

    command          pg_ddl_command    以内部格式表达的该命令的一个完整表现形式。这不能被直接输出， 但是可以把它传递给其                                          他函数来得到有关于该命令不同部分的信息。
```

---

: 表 8.96 pg\_event\_trigger\_ddl\_commands返回列

### 处理被 DDL 命令删除的对象

pg\_event\_trigger\_dropped\_objects返回其sql\_drop事件中命令所删除的所有对象的列表。

如果在任何其他环境中被调用，pg\_event\_trigger\_dropped\_objects将抛出一个错误。pg\_event\_trigger\_dropped\_objects返回下列列：

---

```
**名称**         **类型**                                                                       **描述**

   classid            oid                                                                   对象所属的目录的 OID

    objid             oid                                                                      对象本身的 OID

  objsubid          integer                                                              对象的子ID（如列的属性号）

  original           bool                                                             如果这是删除中的一个根对象则为真

   normal            bool                                                     指示在依赖图中有一个普通依赖关系指向该对象的标志

is_temporary         bool                                                              如果该对象是一个临时对象则为真

 object_type         text                                                                        对象的类型

 schema_name         text                                                 对象所属模式的名称（如果存在）；否则为NULL。不应用引用。

 object_name         text                    如果模式和名称的组合能被用于对象的一个唯一标识符，则是对象的名称；否则是NULL。不应用引用，并且 称不是模式限定的。
 object_identity       text                                     对象身份的文本表现，模式限定的。每一个以及所有身份中出现的标识符在必要时加引号。
 address_names      text\[\]      一个数组，它可以和object_type及address_args 一起通过pg_get_object_address()函数在一台包含有 同类相同名称对象的远程服务器上重建该对象地址。

address_args       text\[\]                    上述address_names的补充。
```

---

: 表 8.97 pg\_event\_trigger\_dropped\_objects返回列

pg\_event\_trigger\_dropped\_objects可以被这样用在一个事件触发器中：

CREATE FUNCTION test\_event\_trigger\_for\_drops()

RETURNS event\_trigger LANGUAGE plpgsql AS $$

DECLARE

obj record;

BEGIN

FOR obj IN SELECT \* FROM pg\_event\_trigger\_dropped\_objects()

LOOP

RAISE NOTICE '% dropped object: % %.% %',

tg\_tag,

obj.object\_type,

obj.schema\_name,

obj.object\_name,

obj.object\_identity;

END LOOP;

END

$$;

CREATE EVENT TRIGGER test\_event\_trigger\_for\_drops

ON sql\_drop

EXECUTE FUNCTION test\_event\_trigger\_for\_drops();

### 处理表重写事件

表 8.98 中所示的函数提供刚刚被调用过table\_rewrite 事件的表的信息。如果在任何其他环境中调用，会发生错误。

---

```
**名称**                   **返回类型**                            **描述**

pg_event_trigger_table_rewrite_oid()         oid                            要被重写的表的ID。 pg_event_trigger_table_rewrite_reason()      int        解释重写原因的原因代码。这些代码的确切含义在单独的文档中。
```

---

: 表 8.98 表重写信息

可以在一个这样的事件触发器中使用 pg\_event\_trigger\_table\_rewrite\_oid函数：

CREATE FUNCTION test\_event\_trigger\_table\_rewrite\_oid()

RETURNS event\_trigger

LANGUAGE plpgsql AS

$$

BEGIN

RAISE NOTICE 'rewriting table % for reason %',

pg\_event\_trigger\_table\_rewrite\_oid()::regclass,

pg\_event\_trigger\_table\_rewrite\_reason();

END;

$$;

CREATE EVENT TRIGGER test\_table\_rewrite\_oid

ON table\_rewrite

EXECUTE FUNCTION test\_event\_trigger\_table\_rewrite\_oid();

## Statistics Information Functions

瀚高数据库提供了一个函数来检查使用CREATE STATISTICS命令定义的复杂统计。

### 检查MCV列表

pg\_mcv\_list\_items返回存储在多列MCV列表中的所有项目的列表，并返回以下列:

---

```
**名称**                **类型**                **描述**

     index                    int            MCV 列表中的项目索引

    values                 text\[\]           存储在MCV项目中的值

     nulls                boolean\[\]          标识NULL值的标志

   frequency           double precision          MCV项目的频率

base_frequency         double precision        MCV项目的基本频率
```

---

: 表 8.99 pg\_mcv\_list\_items返回列

pg\_mcv\_list\_items函数可以这样使用:

SELECT m.\* FROM pg\_statistic\_ext join pg\_statistic\_ext\_data on (oid = stxoid),

pg\_mcv\_list\_items(stxdmcv) m WHERE stxname = 'stts';

pg\_mcv\_list的值只能从pg\_statistic\_ext\_data.stxdmcv列中获得。