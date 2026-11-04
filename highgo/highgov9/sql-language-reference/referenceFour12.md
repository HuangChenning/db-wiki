---
title: "全文搜索"
book: "SQL语言参考手册"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/reference/referenceFour12.html"
tags:
  - highgo
  - highgo-v9
  - sql-language-reference
---

## 全文搜索

## 介绍

全文搜索（或者文本搜索）提供了确定满足一个查询的自然语言文档的能力，并可以选择将它们按照与查询的相关度排序。最常用的搜索类型是找到所有包含给定查询词的文档并按照它们与查询的相似性顺序返回它们。查询和相似性的概念非常灵活并且依赖于特定的应用。

最简单的搜索认为查询是一组词而相似性是查询词在文档中的频度。

文本搜索操作符已经在数据库中存在很多年了。瀚高数据库对文本数据类型提供了~、~\*、LIKE和ILIKE操作符，但是它们缺少现代信息系统所要求的很多基本属性：

• 即使对英语也缺乏语言的支持。正则表达式是不够的，因为它们不能很容易地处理派生词，例如satisfies和satisfy。你可能会错过包含satisfies的文档，尽管你可能想要在对于satisfy的搜索中找到它们。可以使用OR来搜索多个派生形式，但是这样做太罗嗦也容易出错（有些词可能有数千种派生）。

• 它们不提供对搜索结果的排序（排名），这使它们面对数以千计被找到的文档时变得无效。

• 它们很慢因为没有索引支持，因此它们必须为每次搜索处理所有的文档。

全文索引允许文档被预处理并且保存一个索引用于以后快速的搜索。预处理包括：将文档解析成记号。标识出多种类型的记号是有所帮助的，例如数字、词、复杂的词、电子邮件地址，这样它们可以被以不同的方式处理。原则上记号分类取决于相关的应用，但是对于大部分目的都可以使用一套预定义的分类。Highgo使用一个解析器来执行这个步骤。其中提供了一个标准的解析器，并且为特定的需要也可以创建定制的解析器。

将记号转换成词位。和一个记号一样，一个词位是一个字符串，但是它已经被正规化，这样同一个词的不同形式被变成一样。例如，正规化几乎总是包括将大写字母转换成小写形式，并且经常涉及移除后缀（例如英语中的s或es）。这允许搜索找到同一个词的变体形式，而不需要冗长地输入所有可能的变体。此外，这个步骤通常会消除停用词，它们是那些太普通的词，它们对于搜索是无用的（简而言之，记号是文档文本的原始片段，而词位是那些被认为对索引和搜索有用的词）。瀚高数据库使用词典来执行这个步骤。已经提供了多种标准词典，并且为特定的需要也可以创建定制的词典。

为搜索优化存储预处理好的文档。例如，每一个文档可以被表示为正规化的词位的一个有序数组。与词位一起，通常还想要存储用于近似排名的位置信息，这样一个包含查询词更”密集”区域的文档要比那些包含分散的查询词的文档有更高的排名。

词典允许对记号如何被正规化进行细粒度的控制。使用合适的词典，你可以：

• 定义不应该被索引的停用词。

• 使用Ispell把同义词映射到一个单一词。

• 使用一个分类词典把短语映射到一个单一词。

• 使用一个Ispell词典把一个词的不同变体映射到一种规范的形式。

• 使用Snowball词干分析器规则将一个词的不同变体映射到一种规范的形式。

我们提供了一种数据类型tsvector来存储预处理后的文档，还提供了一种类型tsquery来表示处理过的查询）。有很多函数和操作符可以用于这些数据类型，其中最重要的是匹配操作符@@，、。全文搜索可以使用索引来加速。

### 什么是一个文档？

一个document是在一个全文搜索系统中进行搜索的单元，例如，一篇杂志文章或电子邮件消息。文本搜索引擎必须能够解析文档并存储词位（关键词）与它们的父文档之间的关联。随后，这些关联会被用来搜索包含查询词的文档。

对于瀚高数据库中的搜索，一个文档通常是一个数据库表中一行内的一个文本形式的域，或者可能是这类域的一个组合（连接），这些域可能存储在多个表或者是动态获取。换句话说，一个文档可能从用于索引的不同部分构建，并且它可能被作为一个整体存储在某个地方。例如：

SELECT title || ' ' || author || ' ' || abstract || ' ' || body AS document

FROM messages

WHERE mid = 12;

SELECT m.title || ' ' || m.author || ' ' || m.abstract || ' ' || d.body AS

document

FROM messages m, docs d

WHERE mid = did AND mid = 12;

+——————————————————————————————–+  
| **注意：** |  
| |  
| 实际上在这些例子查询中，coalesce应该被用来防止一个单一NULL属性导致整个文档的一个NULL结果。 |  
+——————————————————————————————–+

另一种存储文档的可能性是作为文件系统中的简单文本文件。在这种情况下，数据库可以被用来存储全文索引并执行搜索，并且某些唯一标识符可以被用来从文件系统检索文档。但是，从数据库的外面检索文件要求超级用户权限或者特殊函数支持，因此这种方法通常不如把所有数据放在瀚高数据库内部方便。另外，把所有东西放在数据库内部允许方便地访问文档元数据来协助索引和现实。

对于文本搜索目的，每一个文档必须被缩减成预处理后的tsvector格式。搜索和排名被整个在一个文档的tsvector表示上执行 — 只有当文档被选择来显示给用户时才需要检索原始文本。我们因此经常把tsvector说成是文档，但是当然它只是完整文档的一种紧凑表示。

### 基本文本匹配

瀚高数据库中的全文搜索基于匹配操作符@@，它在一个tsvector（文档）匹配一个tsquery（查询）时返回true。哪种数据类型写在前面没有影响：

SELECT 'a fat cat sat on a mat and ate a fat rat'::tsvector @@ 'cat &

rat'::tsquery;

?column?

\----------

t

SELECT 'fat & cow'::tsquery @@ 'a fat cat sat on a mat and ate a fat

rat'::tsvector;

?column?

\----------

f

正如以上例子所建议的，一个tsquery并不只是一个未经处理的文本，顶多一个tsvector是这样。一个tsquery包含搜索术语，它们必须是已经正规化的词位，并且可以使用 AND 、OR、NOT 以及 FOLLOWED BY 操作符结合多个术语（语法详见第 8.11.2 节）。有几个函数to\_tsquery、plainto\_tsquery以及phraseto\_tsquery可用于将用户书写的文本转换为正确的tsquery，它们会主要采用正则化出现在文本中的词的方法。相似地，to\_tsvector被用来解析和正规化一个文档字符串。因此在实际上一个文本搜索匹配可能看起来更像：

SELECT to\_tsvector('fat cats ate fat rats') @@ to\_tsquery('fat & rat');

?column?

\----------

t

注意如果这个匹配被写成下面这样它将不会成功：

SELECT 'fat cats ate fat rats'::tsvector @@ to\_tsquery('fat & rat');

?column?

\----------

f

因为这里不会发生词rats的正规化。一个tsvector的元素是词位，它被假定为已经正规化好，因此rats不匹配rat。

@@操作符也支持text输出，它允许在简单情况下跳过从文本字符串到tsvector或tsquery的显式转换。可用的变体是：

tsvector @@ tsquery

tsquery @@ tsvector

text @@ tsquery

text @@ text

前两种我们已经见过。形式text @@ tsquery等价于to\_tsvector(x) @@ y。形式text @@ text等价于to\_tsvector(x) @@ plainto\_tsquery(y)。

在tsquery中，&（AND）操作符指定它的两个参数都必须出现在文档中才表示匹配。类似地，|（OR）操作符指定至少一个参数必须出现，而!（NOT）操作符指定它的参数不出现才能匹配。例如，查询fat &! rat匹配包含fat但不包含rat的文档。

在<->（FOLLOWED BY） tsquery操作符的帮助下搜索可能的短语，只有该操作符的参数的匹配是相邻的并且符合给定顺序时，该操作符才算是匹配。例如：

SELECT to\_tsvector('fatal error') @@ to\_tsquery('fatal <-> error');

?column?

\----------

t

SELECT to\_tsvector('error is not fatal') @@ to\_tsquery('fatal <-> error');

?column?

\----------

f

FOLLOWED BY 操作符还有一种更一般的版本，形式是\<N>，其中N是一个表示匹配词位位置之间的差。<1>和<->相同，而<2>允许刚好一个其他词位出现在匹配之间，以此类推。当有些词是停用词时，phraseto\_tsquery函数利用这个操作符来构造一个能够匹配多词短语的tsquery。例如：

SELECT phraseto\_tsquery('cats ate rats');

phraseto\_tsquery

\-------------------------------

'cat' <-> 'ate' <-> 'rat'

SELECT phraseto\_tsquery('the cats ate the rats');

phraseto\_tsquery

\-------------------------------

'cat' <-> 'ate' <2> 'rat'

一种有时候有用的特殊情况是，<0>可以被用来要求两个匹配同一个词的模式。

圆括号可以被用来控制tsquery操作符的嵌套。如果没有圆括号，|的计算优先级最低，然后从低到高依次是&、<->、!。

值得注意的是，当AND/OR/NOT操作符在一个FOLLOWED BY操作符的参数中时，它们表示与不在那些参数中时不同的含义，因为在FOLLOWED BY中匹配的准确位置是有意义的。例如，通常!x仅匹配在任何地方都不包含x的文档。但如果y不是紧接在一个x后面，!x <-> y就会匹配那个y，在文档中其他位置出现的x不会阻止匹配。另一个例子是，x & y通常仅要求x和y均出现在文档中的某处，但是(x & y) <-> z要求x和y在紧挨着z之前的同一个位置匹配。

因此这个查询的行为会不同于x <-> z & y <-> z，它将匹配一个含有两个单独序列x z以及y z的文档（这个特定的查询一点用都没有，因为x和y不可能在同一个位置匹配，但是对于前缀匹配模式之类的更复杂的情况，这种形式的查询就会有用武之地）。

### 配置

前述的都是简单的文本搜索例子。正如前面所提到的，全文搜索功能包括做更多事情的能力：跳过索引特定词（停用词）、处理同义词并使用更高级的解析，例如基于空白之外的解析。这个功能由文本搜索配置控制。瀚高数据库中有多种语言的预定义配置，并且你可以很容易地创建你自己的配置（psql的\\dF命令显示所有可用的配置）。

在安装期间一个合适的配置将被选择并且default\_text\_search\_config也被相应地设置在Highgo.conf中。如果你正在对整个集簇使用相同的文本搜索配置，你可以使用在Highgo.conf中使用该值。要在集簇中使用不同的配置但是在任何一个数据库内部使用同一种配置，使用ALTER DATABASE... SET。否则，你可以在每个会话中设置default\_text\_search\_config。

依赖一个配置的每一个文本搜索函数都有一个可选的regconfig参数，因此要使用的配置可以被显式指定。只有当这个参数被忽略时，default\_text\_search\_config才被使用。

为了让建立自定义文本搜索配置更容易，一个配置可以从更简单的数据库对象来建立。瀚高数据库的文本搜索功能提供了四类配置相关的数据库对象：

• 文本搜索解析器将文档拆分成记号并分类每个记号（例如，作为词或者数字）。

• 文本搜索词典将记号转变成正规化的形式并拒绝停用词。

• 文本搜索模板提供位于词典底层的函数（一个词典简单地指定一个模板和一组用于模板的参数）。

• 文本搜索配置选择一个解析器和一组用于将解析器产生的记号正规化的词典。

文本搜索解析器和模板是从低层 C 函数构建而来，因此它要求 C 编程能力来开发新的解析器和模板，并且还需要超级用户权限来把它们安装到一个数据库中（在Highgo发布的contrib/区域中有一些附加的解析器和模板的例子）。由于词典和配置只是对底层解析器和模板的参数化和连接，不需要特殊的权限来创建一个新词典或配置。创建定制词典和配置的例子将在本章稍后的部分给出。

## 表和索引

在前一节中的例子演示了使用简单常数字符串进行全文匹配。本节展示如何搜索表数据，以及可选择地使用索引。

### 搜索一个表

可以在没有一个索引的情况下做一次全文搜索。一个简单的查询将打印每一个行的title，这些行在其body域中包含词friend：

SELECT title

FROM pgweb

WHERE to\_tsvector('english', body) @@ to\_tsquery('english', 'friend');

这将还会找到相关的词例如friends和friendly，因为这些都被约减到同一个正规化的词位。

以上的查询指定要使用english配置来解析和正规化字符串。我们也可以忽略配置参数：

SELECT title

FROM pgweb

WHERE to\_tsvector(body) @@ to\_tsquery('friend');

这个查询将使用由default\_text\_search\_config设置的配置。

一个更复杂的例子是选择 10 个最近的文档，要求它们在title或body中包

含create和table：

SELECT title

FROM pgweb

WHERE to\_tsvector(title || ' ' || body) @@ to\_tsquery('create & table')

ORDER BY last\_mod\_date DESC

LIMIT 10;

为了清晰，我们忽略coalesce函数调用，它可能需要被用来查找在这两个域之中包含NULL的行。

尽管这些查询可以在没有索引的情况下工作，大部分应用会发现这种方法太慢了，除了偶尔的临时搜索。实际使用文本搜索通常要求创建一个索引。

### 创建索引

我们可以创建一个GIN索引来加速文本搜索：

CREATE INDEX pgweb\_idx ON pgweb USING GIN(to\_tsvector('english', body));

注意这里使用了to\_tsvector的双参数版本。只有指定了一个配置名称的文本搜索函数可以被用在表达式索引（第11.7节）中。这是因为索引内容必须是没有被default\_text\_search\_config影响的。如果它们被影响，索引内容可能会不一致因为不同的项可能包含被使用不同文本搜索配置创建的tsvector，并且没有办法猜测哪个是哪个。也没有可能正确地转储和恢复这样的一个索引。

由于to\_tsvector的双参数版本被使用在上述的索引中，只有一个使用了带有相同配置名的双参数版to\_tsvector的查询引用才能使用该索引。即，WHERE to\_tsvector('english', body) @@ 'a & b' 可以使用该索引，但WHERE to\_tsvector(body) @@ 'a & b'不能。这保证一个索引只能和创建索引项时所用的相同配置一起使用。

可以建立更复杂的表达式索引，在其中配置名被另一个列指定，例如：

CREATE INDEX pgweb\_idx ON pgweb USING GIN(to\_tsvector(config\_name, body));

这里config\_name是pgweb表中的一个列。这允许在同一个索引中有混合配置，同时记录哪个配置被用于每一个索引项。例如，如果文档集合包含不同语言的文档，这就可能会有用。同样，要使用索引的查询必须被措辞成匹配，例如

WHERE to\_tsvector(config\_name, body) @@ 'a & b'。

索引甚至可以连接列：

CREATE INDEX pgweb\_idx ON pgweb USING GIN(to\_tsvector('english', title || ' ' || body));

另一种方法是创建一个单独的tsvector列来保存to\_tsvector的输出。若要使此列与其源数据保持自动更新，用存储生成的列。这个例子是title和body的连接，使用coalesce来保证当其他域为NULL时一个域仍然能留在索引中：

ALTER TABLE pgweb

ADD COLUMN textsearchable\_index\_col tsvector

GENERATED ALWAYS AS (to\_tsvector('english', coalesce(title, '')

|| ' ' || coalesce(body, ''))) STORED;

然后我们创建一个GIN索引来加速搜索：

CREATE INDEX textsearch\_idx ON pgweb USING GIN(textsearchable\_index\_col);

现在我们准备好执行一个快速的全文搜索了：

SELECT title

FROM pgweb

WHERE textsearchable\_index\_col @@ to\_tsquery('create & table')

ORDER BY last\_mod\_date DESC

LIMIT 10;

单独列方法相对于表达式索引的一个优势在于，它不必为了利用索引而在查询中显式地指定文本搜索配置。如上述例子所示，查询可以依赖default\_text\_search\_config。另一个优势是搜索将会更快，因为它不必重做to\_tsvector调用来验证索引匹配（在使用 GiST 索引时这一点比使用 GIN 索引时更重要；）。表达式索引方法更容易建立，但是它要求更少的磁盘空间，因为tsvector表示没有被显式地存储下来。

## 空值文本搜索

要实现全文搜索必须要有一个从文档创建tsvector以及从用户查询创建tsquery的函数。而且我们需要一种有用的顺序返回结果，因此我们需要一个函数能够根据文档与查询的相关性比较文档。还有一点重要的是要能够很好地显示结果。瀚高数据库对所有这些函数都提供了支持。

### 解析文档

瀚高数据库提供了函数to\_tsvector将一个文档转换成tsvector数据类型。

to\_tsvector(\[ config regconfig, \] document text) returns tsvector

to\_tsvector把一个文本文档解析成记号，把记号缩减成词位，并且返回一个tsvector，它列出了词位以及词位在文档中的位置。文档被根据指定的或默认的文本搜索配置来处理。下面是一个简单例子：

SELECT to\_tsvector('english', 'a fat cat sat on a mat - it ate a fat rats');

to\_tsvector

\-----------------------------------------------------

'ate':9 'cat':3 'fat':2,11 'mat':7 'rat':12 'sat':4

在上面这个例子中我们看到，作为结果的tsvector不包含词a、on或it，词rats变成了rat，并且标点符号-被忽略了。

to\_tsvector函数在内部调用了一个解析器，它把文档文本分解成记号并且为每一种记号分配一个类型。对于每一个记号，会去查询一个词典列表，该列表会根据记号的类型而变化。第一个识别记号的词典产生一个或多个正规化的词位来表示该记号。例如，rats变成rat是因为一个词典识别到该词rats是rat的复数形式。一些词会被识别为停用词，这将导致它们被忽略，因为它们出现得太频繁以至于在搜索中起不到作用。在我们的例子中有a、on和it是停用词。如果在列表中没有词典能识别该记号，那它将也会被忽略。在这个例子中标点符号-就属于这种情况，因为事实上没有词典会给它分配记号类型（空间符号），即空间记号不会被索引。对于解析器、词典以及要索引哪些记号类型是由所选择的文本搜索配置（第 12.7 节）决定的。可以在同一个数据库中有多种不同的配置，并且有用于很多种语言的预定义配置。在我们的例子中，我们使用用于英语的默认配置english。

函数setweight可以被用来对tsvector中的项标注一个给定的权重，这里一个权重可以是四个字母之一：A、B、C或D。这通常被用来标记来自文档不同部分的项，例如标题对正文。稍后，这种信息可以被用来排名搜索结果。

因为to\_tsvector(NULL) 将返回NULL，不论何时一个域可能为空时，我们推荐使用coalesce。下面是我们推荐的从一个结构化文档创建一个tsvector的方法：

UPDATE tt SET ti =

setweight(to\_tsvector(coalesce(title,'')), 'A') ||

setweight(to\_tsvector(coalesce(keyword,'')), 'B') ||

setweight(to\_tsvector(coalesce(abstract,'')), 'C') ||

setweight(to\_tsvector(coalesce(body,'')), 'D');

这里我们已经使用了setweight在完成的tsvector标注每一个词位的来源，并且接着将标注过的tsvector值用tsvector连接操作符||合并在一起（第 12.4.1 节给出了关于这些操作符的细节）。

### 解析查询

瀚高数据库提供了函数to\_tsquery、plainto\_tsquery、phraseto\_tsquery以及websearch\_to\_tsquery用来把一个查询转换成tsquery数据类型。to\_tsquery提供了比plainto\_tsquery和phraseto\_tsquery更多的特性，但是它对其输入要求更加严格。websearch\_to\_tsquery是to\_tsquery的一个简化版本，它使用一种可选择的语法，类似于Web搜索引擎使用的语法。

to\_tsquery(\[ config regconfig, \] querytext text) returns tsquery

to\_tsquery从querytext创建一个tsquery值，该值由被tsquery操作符&（AND）、|（OR）、!（NOT）和<->（FOLLOWED BY）分隔的单个记号组成。 这些操作符可以使用圆括号分组。换句话说，to\_tsquery的输入必须已经遵循tsquery输入的一般规则，如第 8.11.2 节所述。区别在于基本的tsquery输入把记号当作表面值，而to\_tsquery 会使用指定的或者默认的配置把每一个记号正规化成一个词位，并且丢弃掉任何根据配置是停用词的记号。例如：

SELECT to\_tsquery('english', 'The & Fat & Rats');

to\_tsquery

\---------------

'fat' & 'rat'

和在基本tsquery输入中一样，权重可以被附加到每一个词位来限制它只匹配属于那些权重的tsvector词位。例如：

SELECT to\_tsquery('english', 'Fat | Rats:AB');

to\_tsquery

'fat' | 'rat':AB

同样，\*可以被附加到一个词位来指定前缀匹配：

SELECT to\_tsquery('supern:\*A & star:A\*B');

to\_tsquery

\--------------------------

'supern':\*A & 'star':\*AB

这样一个词位将匹配一个tsvector中的任意以给定字符串开头的词。

to\_tsquery也能够接受单引号短语。当配置包括一个会在这种短语上触发的分类词典时就是它的主要用处。在下面的例子中，一个分类词典含规则supernovae stars: sn：

SELECT to\_tsquery('''supernovae stars'' &!crab');

to\_tsquery

\---------------

'sn' &!'crab'

在没有引号时，to\_tsquery将为那些没有被 AND、OR 或者 FOLLOWED BY 操作符分隔的记号产生一个语法错误。

plainto\_tsquery(\[ config regconfig, \] querytext text) returns tsquery

plainto\_tsquery将未格式化的文本querytext转换成一个tsquery值。该文本被解析并被正规化，很像to\_tsvector，然后&（AND）布尔操作符被插入到留下来的词之间。

例子：

SELECT plainto\_tsquery('english', 'The Fat Rats');

plainto\_tsquery

\-----------------

'fat' & 'rat'

注意plainto\_tsquery不会识其输入中的tsquery操作符、权重标签或前缀匹配标签：

SELECT plainto\_tsquery('english', 'The Fat & Rats:C');

plainto\_tsquery

\---------------------

'fat' & 'rat' & 'c'

这里，所有输入的标点都被作为空间符号并且丢弃。

phraseto\_tsquery(\[ config regconfig, \] querytext text) returns tsquery

phraseto\_tsquery的行为很像plainto\_tsquery，不过前者会在留下来的词之间插入<- >（FOLLOWED BY）操作符而不是&（AND）操作符。还有，停用词也不是简单地丢弃掉，而是通过插入\<N>操作符（而不是<->操作符）来解释。在搜索准确的词位序列时这个函数很有用，因为 FOLLOWED BY 操作符不只是检查所有词位的存在性，还会检查词位的顺序。

例子：

SELECT phraseto\_tsquery('english', 'The Fat Rats');

phraseto\_tsquery

\------------------

'fat' <-> 'rat'

和plainto\_tsquery相似，phraseto\_tsquery函数不会识别其输入中的tsquery操作符、权重标签或者前缀匹配标签：

SELECT phraseto\_tsquery('english', 'The Fat & Rats:C');

phraseto\_tsquery

\-----------------------------

'fat' <-> 'rat' <-> 'c'

websearch\_to\_tsquery(\[ config regconfig, \] querytext text) returns tsquery

websearch\_to\_tsquery使用一种可供选择的语法从querytext创建一个tsquery值，这种语法中简单的未格式化文本是一个有效的查询。和plainto\_tsquery以及phraseto\_tsquery不同，它还识别特定的操作符。此外，这个函数绝不会报出语法错误，这就可以把原始的用户提供的输入用于搜索。支持下列语法：

• 无引号文本：不在引号中的文本将被转换成由&操作符分隔的词，就像被plainto\_tsquery处理过那样。

• "引号文本"：在引号中的文本将被转换成由<->操作符分隔的词，就像被phraseto\_tsquery处理过那样。

• OR：逻辑或将被转换成|操作符。

• -：逻辑非操作符，被转换成!操作符。

示例：

SELECT websearch\_to\_tsquery('english', 'The fat rats');

websearch\_to\_tsquery

\----------------------

'fat' & 'rat'

(1 row)

SELECT websearch\_to\_tsquery('english', '"supernovae stars" -crab');

websearch\_to\_tsquery

\----------------------------------

'supernova' <-> 'star' &!'crab'

(1 row)

SELECT websearch\_to\_tsquery('english', '"sad cat" or "fat rat"');

websearch\_to\_tsquery

\-----------------------------------

'sad' <-> 'cat' | 'fat' <-> 'rat'

(1 row)

SELECT websearch\_to\_tsquery('english', 'signal -"segmentation fault"');

websearch\_to\_tsquery

\---------------------------------------

'signal' &!( 'segment' <-> 'fault' )

(1 row)

SELECT websearch\_to\_tsquery('english', '""" )( dummy \\\\ query <->');

websearch\_to\_tsquery

\----------------------

'dummi' & 'queri'

(1 row)

### 排名搜索结果

排名处理尝试度量文档和一个特定查询的接近程度，这样当有很多匹配时最相关的那些可以被先显示。瀚高数据库提供了两种预定义的排名函数，它们考虑词法、临近性和结构信息；即，它们考虑查询词在文档中出现得有多频繁，文档中的词有多接近，以及词出现的文档部分有多重要。不过，相关性的概念是模糊的并且与应用非常相关。不同的应用可能要求额外的信息用于排名，例如，文档修改时间。内建的排名函数只是例子。你可以编写你自己的排名函数和/或把它们的结果与附加因素整合在一起来适应你的特定需求。

目前可用的两种排名函数是：

ts\_rank(\[ weights float4\[\], \] vector tsvector, query tsquery \[, normalization

integer \]) returns float4

基于向量的匹配词位的频率来排名向量。

ts\_rank\_cd(\[ weights float4\[\], \] vector tsvector, query tsquery \[, normalization

integer \]) returns float4

这个函数为给定文档向量和查询计算覆盖密度排名，该方法在 Clarke、Cormack 和Tudhope 于 1999 年在期刊 "Information Processing and Management" 上的文章"Relevance Ranking for One to Three Term Queries" 文章中有描述。覆盖密度类似于ts\_rank排名，不过它会考虑匹配词位相互之间的接近度。

这个函数要求词位的位置信息来执行其计算。因此它会忽略tsvector中任何”被剥离的”词位。如果在输入中有未被剥离的词位，结果将会是零（strip函数和tsvector中的位置信息的更多内容请见第 11.4.1 节）。

对这两个函数，可选的权重参数提供了为词实例赋予更多或更少权重的能力，这种能力是依据它们被标注的情况的。权重数组指定每一类词应该得到多重的权重，按照如下的顺序：

{D-权重, C-权重, B-权重, A-权重}

如果没有提供权重，那么将使用这些默认值：

{0.1, 0.2, 0.4, 1.0}

通常权重被用来标记来自文档特别区域的词，如标题或一个初始的摘要，这样它们可以被认为比来自文档正文的词更重要或更不重要。

由于一个较长的文档有更多的机会包含一个查询术语，因此考虑文档的尺寸是合理的，例如一个一百个词的文档中有一个搜索词的五个实例而零一个一千个词的文档中有该搜索词的五个实例，则前者比后者更相关。两种排名函数都采用一个整数正规化选项，它指定文档长度是否影响其排名以及如何影响。该整数选项控制多个行为，因此它是一个位掩码：你可以使用|指定一个或多个行为（例如，2|4）。

• 0（默认值）忽略文档长度

• 1 用 1 + 文档长度的对数除排名

• 2 用文档长度除排名

• 4 用长度之间的平均调和距离除排名（只被ts\_rank\_cd实现）

• 8 用文档中唯一词的数量除排名

• 16 用 1 + 文档中唯一词数量的对数除排名

• 32 用排名 + 1 除排名

如果多于一个标志位被指定，转换将根据列出的顺序被应用。

值得注意的是排名函数并不使用任何全局信息，因此它不可能按照某些时候期望地产生一个公平的正规化，从 1% 或 100%。正规化选项 32 （rank/(rank+1)）可以被应用来缩放所有的排名到范围零到一，但是当然这只是一个外观上的改变；它不会影响搜索结果的顺序。

这里是一个例子，它只选择十个最高排名的匹配：

SELECT title, ts\_rank\_cd(textsearch, query) AS rank

FROM apod, to\_tsquery('neutrino|(dark & matter)') query

WHERE query @@ textsearch

ORDER BY rank DESC

LIMIT 10;

title | rank

\-----------------------------------------------+----------

Neutrinos in the Sun | 3.1

The Sudbury Neutrino Detector | 2.4

A MACHO View of Galactic Dark Matter | 2.01317

Hot Gas and Dark Matter | 1.91171

The Virgo Cluster: Hot Plasma and Dark Matter | 1.90953

Rafting for Solar Neutrinos | 1.9

NGC 4650A: Strange Galaxy and Dark Matter | 1.85774

Hot Gas and Dark Matter | 1.6123

Ice Fishing for Cosmic Neutrinos | 1.6

Weak Lensing Distorts the Universe | 0.818218

这是相同的例子使用正规化的排名：

SELECT title, ts\_rank\_cd(textsearch, query, 32 /\* rank/(rank+1) \*/ ) AS rank

FROM apod, to\_tsquery('neutrino|(dark & matter)') query

WHERE query @@ textsearch

ORDER BY rank DESC

LIMIT 10;

title | rank

\-----------------------------------------------+-------------------

Neutrinos in the Sun | 0.756097569485493

The Sudbury Neutrino Detector | 0.705882361190954

A MACHO View of Galactic Dark Matter | 0.668123210574724

Hot Gas and Dark Matter | 0.65655958650282

The Virgo Cluster: Hot Plasma and Dark Matter | 0.656301290640973

Rafting for Solar Neutrinos | 0.655172410958162

NGC 4650A: Strange Galaxy and Dark Matter | 0.650072921219637

Hot Gas and Dark Matter | 0.617195790024749

Ice Fishing for Cosmic Neutrinos | 0.615384618911517

Weak Lensing Distorts the Universe | 0.450010798361481

排名可能会非常昂贵，因为它要求查询每一个匹配文档的tsvector，这可能会涉及很多I/O因而很慢。不幸的是，这几乎不可能避免，因为实际查询常常导致巨大数目的匹配。

### 加亮结果

要表示搜索结果，理想的方式是显示每一个文档的一个部分并且显示它是怎样与查询相关的。通常，搜索引擎显示文档片段时会对其中的搜索术语进行标记。Highgo提供了一个函数ts\_headline来实现这个功能。

ts\_headline(\[ config regconfig, \] document text, query tsquery \[, options text

\]) returns text ts\_headline接受一个文档和一个查询，并且从该文档返回一个引用，在其中来自查询的术语会被加亮。被用来解析该文档的配置可以用config指定；如果config被忽略，将会使用default\_text\_search\_config配置。

如果一个options字符串被指定，它必须由一个逗号分隔的列表组成，列表中是一个或多个option=value对。可用的选项是：

• StartSel、StopSel：用来定界文档中出现的查询词的字符串，这用来把它们与其他被引用的词区分开。如果这些字符串包含空格或逗号，你必须把它们加上双引号。

• MaxWords、MinWords：这些数字决定要输出的最长和最短 headline。

• ShortWord：长度小于等于这个值的词将被从一个 headline 的开头或结尾处丢掉。默认值三消除普通英语文章。

• HighlightAll：布尔标志，如果为true整个文档将被用作 headline，并忽略前面的三个参数。

• MaxFragments：要显示的文本引用或片段的最大数量。默认值零选择一种非片段倾向的headline 生成方法。一个大于零的值选择基于片段的 headline 生成。这种方法找到有尽可能多查询词的文本片段并且展开查询词周围的那些片段。结果是查询词会靠近每个片段的中间并且在其两侧都有词。每一个片段将是最多MaxWords并且长度小于等于ShortWord的词被从每个片段的开头或结尾丢弃。如果不是所有的查询词都在该文档中找到，文档中第一个MinWords的单一片段将被显示。

• FragmentDelimiter：当多于一个片段被显示时，片段将被这个字符串所分隔。

这些选项名称不区分大小写。任何未指定的选项将收到这些默认值：

StartSel=\<b>, StopSel=\</b>,

MaxWords=35, MinWords=15, ShortWord=3, HighlightAll=FALSE,

MaxFragments=0, FragmentDelimiter="... "

例如：

SELECT ts\_headline('english',

'The most common type of search

is to find all documents containing given query terms

and return them in order of their similarity to the

query.',

to\_tsquery('query & similarity'));

ts\_headline

\------------------------------------------------------------

containing given \<b>query\</b> terms

and return them in order of their \<b>similarity\</b> to the

\<b>query\</b>.

SELECT ts\_headline('english',

'The most common type of search

is to find all documents containing given query terms

and return them in order of their similarity to the

query.',

to\_tsquery('query & similarity'),

'StartSel = <, StopSel = >');

ts\_headline

\-------------------------------------------------------

containing given \<query> terms

and return them in order of their \<similarity> to the

\<query>.

ts\_headline使用原始文档，而不是一个tsvector摘要，因此它可能很慢并且应该被小心使用。

## 额外特性

这一节描述在文本搜索中有用的一些额外的函数和操作符。

### 操纵文档

第 11.3.1 节展示了未经处理的文本文档如何被转换成tsvector值。瀚高数据库也提供了用于操纵已经为tsvector形式的文档的函数和操作符。

tsvector || tsvector

tsvector连接操作符返回一个向量，它结合了作为参数给出的两个向量的词位和位置信息。位置和权重标签在连接期间被保留。出现在右手向量中的位置被使用左手向量中提到的最大位置进行偏移，这样结果几乎等于在两个原始文档字符串的连接上执行to\_tsvector的结果（这种等价不是完全的，因为从左手参数的尾端移除的任何停用词将会影响结果，而如果文本连接被使用它们就影响了右手参数中的词位位置）。

使用向量形式的连接而不是在应用to\_tsvector之前连接文本的一个优点是你可以使用不同配置来解析文档的不同小节。此外，因为setweight函数按照相同的方式标记给定向量的所有词位，如果你想把文档的不同部分标注不同的权重，你就有必要解析文本并且在连接之前做setweight。

setweight(vector tsvector, weight "char") returns tsvector

setweight返回输入向量的一个拷贝，其中每一个位置都被标注为给定的权

重：A、B、C或D（D是新向量的默认值并且并不会被显示在输出上）。向量被连接时会保留这些标签，允许来自文档的不同部分的词被排名函数给予不同的权重。

注意权重标签是应用到位置而不是词位。如果输入向量已经被剥离了位置，则setweight什么也不会做。

length(vector tsvector) returns integer

返回存储在向量中的词位数。

strip(vector tsvector) returns tsvector

返回一个向量，其中列出了和给定向量相同的词位，不过没有任何位置或者权重信息。

其结果通常比未被剥离的向量小很多，但是用处也小很多。和未被剥离的向量一样，相关度排名在已剥离的向量上也不起作用。此外，<->（FOLLOWED BY）tsquery操作符不会匹配已剥离的输入，因为它无法确定词位之间的距离。

表 8.42中有tsvector相关函数的完整列表。

### 操纵查询

第 11.3.2 节展示了未经处理的文本形式的查询如何被转换成tsquery值。Highgo也提供了用于操纵已经是tsquery形式的查询的函数和操作符。

tsquery && tsquery

返回用 AND 结合的两个给定查询。

tsquery || tsquery

返回用 OR 结合的两个给定查询。

!! tsquery

返回一个给定查询的反（NOT）。

tsquery <-> tsquery

返回一个查询，它用<->（FOLLOWED BY）tsquery操作符搜索两个紧跟的匹配，第一个匹配符合第一个给定的查询而第二个匹配符合第二个给定的查询。例如：

SELECT to\_tsquery('fat') <-> to\_tsquery('cat | rat');

?column?

\-----------------------------------

'fat' <-> 'cat' | 'fat' <-> 'rat'

tsquery\_phrase(query1 tsquery, query2 tsquery \[, distance integer \]) returns

tsquery

返回一个查询，它使用\<N> tsquery操作符搜索两个距离为distance个词位的匹配，第一个匹配符合第一个给定的查询而第二个匹配符合第二个给定的查询。例如：

SELECT tsquery\_phrase(to\_tsquery('fat'), to\_tsquery('cat'), 10);

tsquery\_phrase

\------------------

'fat' <10> 'cat'

numnode(query tsquery) returns integer

返回一个tsquery中的结点数（词位外加操作符）。要确定查询是否有意义或者是否只包含停用词时，这个函数有用，在前一种情况它返回 > 0，后一种情况返回 0。例子：

SELECT numnode(plainto\_tsquery('the any'));

NOTICE: query contains only stopword(s) or doesn't contain lexeme(s),

ignored

numnode

\---------

0

SELECT numnode('foo & bar'::tsquery);

numnode

\---------

3

querytree(query tsquery) returns text

返回一个tsquery中可以被用来搜索一个索引的部分。这个函数可用来检测不可被索引的查询，例如那些只包含停用词或者只有否定术语的查询。例如：

SELECT querytree(to\_tsquery('!defined'));

querytree

#### 查询重写

ts\_rewrite函数族在一个给定的tsquery中搜索一个目标子查询的出现，并且将每一次出现替换成一个替补子查询。本质上这个操作就是一个tsquery版本的子串替换。一个目标和替补的组合可以被看成是一个查询重写规则。一个这类重写规则的集合可以是一个强大的搜索助手。例如，你可以使用同义词扩展搜索（如，new york、big apple、nyc、gotham），或者收缩搜索来将用户导向某些特点主题。在这个特性和分类词典（第 12.6.4 节）有些功能重叠。但是，你可以随时修改一组重写规则而无需重索引，而更新一个分类词典则要求进行重索引才能生效。

ts\_rewrite (query tsquery, target tsquery, substitute tsquery) returns tsquery

这种形式的ts\_rewrite简单地应用一个单一重写规则：不管target出现在query中的那个地方，它都被substitute替代。例如：

SELECT ts\_rewrite('a & b'::tsquery, 'a'::tsquery, 'c'::tsquery);

ts\_rewrite

\------------

'b' & 'c'

ts\_rewrite (query tsquery, select text) returns tsquery

这种形式的ts\_rewrite接受一个开始query和一个 SQL select命令，它们以一个文本字符串的形式给出。select必须得到tsquery类型的两列。对于select结果的每一行，在当前query值中出现的第一列值（目标）被第二列值（替补）所替换。例如：

CREATE TABLE aliases (t tsquery PRIMARY KEY, s tsquery);

INSERT INTO aliases VALUES('a', 'c');

SELECT ts\_rewrite('a & b'::tsquery, 'SELECT t,s FROM aliases');

ts\_rewrite

\------------

'b' & 'c'

注意当多个重写规则被以这种方式应用时，应用的顺序很重要；因此在实际中你会要求源查询按某些排序键ORDER BY。

让我们考虑一个现实的天文学例子。我们将使用表驱动的重写规则扩展查询supernovae：

CREATE TABLE aliases (t tsquery primary key, s tsquery);

INSERT INTO aliases VALUES(to\_tsquery('supernovae'), to\_tsquery('supernovae| sn'));

SELECT ts\_rewrite(to\_tsquery('supernovae & crab'), 'SELECT \* FROM aliases');

ts\_rewrite

\---------------------------------

'crab' & ( 'supernova' | 'sn' )

我们可以通过只更新表来改变重写规则：

UPDATE aliases

SET s = to\_tsquery('supernovae|sn &!nebulae')

WHERE t = to\_tsquery('supernovae');

SELECT ts\_rewrite(to\_tsquery('supernovae & crab'), 'SELECT \* FROM aliases');

ts\_rewrite

\---------------------------------------------

'crab' & ( 'supernova' | 'sn' &!'nebula' )

当有很多重写规则时，重写可能会很慢，因为它要为为每一个可能的匹配检查每一条规则。

要过滤掉明显不符合的规则，我们可以为tsquery类型使用包含操作符。在下面的例子中，我们只选择那些可能匹配原始查询的规则：

SELECT ts\_rewrite('a & b'::tsquery,

'SELECT t,s FROM aliases WHERE ''a & b''::tsquery @> t');

ts\_rewrite

\------------

'b' & 'c'

### 用于自动更新的触发器

+———————————————————————–+  
| **注意：** |  
| |  
| 本节中描述的方法已被使用存储生成的列所淘汰，如 第 11.2.2 节中所述。 |  
+———————————————————————–+

当使用一个单独的列来存储你的文档的tsvector表示时，有必要创建一个触发器在文档内容列改变时更新tsvector列。两个内建触发器函数可以用于这个目的，或者你可以编写你自己的触发器函数。

tsvector\_update\_trigger(tsvector\_column\_name, config\_name, text\_column\_name

\[,... \])

tsvector\_update\_trigger\_column(tsvector\_column\_name, config\_column\_name, text\_column\_name

\[,... \])

这些触发器函数在CREATE TRIGGER命令中指定的参数控制下，自动从一个或多个文本列计算一个tsvector列。它们使用的一个例子是：

CREATE TABLE messages (

title text,

body text,

tsv tsvector

);

CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE

ON messages FOR EACH ROW EXECUTE FUNCTION

tsvector\_update\_trigger(tsv, 'pg\_catalog.english', title, body);

INSERT INTO messages VALUES('title here', 'the body text is here');

SELECT \* FROM messages;

title | body | tsv

\------------+-----------------------+----------------------------

title here | the body text is here | 'bodi':4 'text':5 'titl':1

SELECT title, body FROM messages WHERE tsv @@ to\_tsquery('title & body');

title | body

\------------+-----------------------

title here | the body text is here

在创建了这个触发器后，在title或body中的任何修改将自动地被反映到tsv中，不需要应用来操心同步的问题。

第一个触发器参数必须是要被更新的tsvector列的名字。第二个参数指定要被用来执行转换的文本搜索配置。对于tsvector\_update\_trigger，配置名被简单地用第二个触发器参数给出。如上所示，它必须是模式限定的，因此该触发器行为不会因为search\_path中的改变而改变。对于tsvector\_update\_trigger\_column，第二个触发器参数是另一个表列的名称，它必须是类型regconfig。这允许做一种逐行的配置选择。剩下的参数是文本列的名称（类型为text、varchar或char）。它们将按给定的顺序被包括在文档中。NULL 值将被跳过（但是其他列仍将被索引）。

这些内建触发器的一个限制是它们将所有输入列同样对待。要对列进行不同的处理 — 例如，使标题的权重和正文的不同 — 就需要编写一个自定义触发器。下面是用PL/pgSQL作为触发器语言的一个例子：

CREATE FUNCTION messages\_trigger() RETURNS trigger AS $$

begin

new.tsv:=

setweight(to\_tsvector('pg\_catalog.english', coalesce(new.title,'')), 'A')

||

setweight(to\_tsvector('pg\_catalog.english', coalesce(new.body,'')), 'D');

return new;

end

$$ LANGUAGE plpgsql;

CREATE TRIGGER tsvectorupdate BEFORE INSERT OR UPDATE

ON messages FOR EACH ROW EXECUTE FUNCTION messages\_trigger();

记住当在触发器内创建tsvector值时，显式地指定配置名非常重要，这样列的内容才不会被default\_text\_search\_config的改变所影响。如果不这样做很可能导致问题，例如在转储并重新载入之后搜索结果改变。

### 收集文档统计数据

ts\_stat被用于检查你的配置以及寻找候选的停用词。

ts\_stat(sqlquery text, \[ weights text, \]

OUT word text, OUT ndoc integer,

OUT nentry integer) returns setof record

sqlquery是一个文本值，它包含一个必须返回单一tsvector列的 SQL 查询。ts\_stat执行该查询并返回有关包含在该tsvector数据中的每一个可区分词位（词）的统计数据。返回的列是：

• word text — 一个词位的值

• ndoc integer — 词出现过的文档（tsvector）的数量

• nentry integer — 词出现的总次数

如果提供了权重，只有具有其中之一权重的出现才被计算在内。

例如，要在一个文档集合中查找十个最频繁的词：

SELECT \* FROM ts\_stat('SELECT vector FROM apod')

ORDER BY nentry DESC, ndoc DESC, word

LIMIT 10;

同样的要求，但是只计算以权重A或B出现的次数：

SELECT \* FROM ts\_stat('SELECT vector FROM apod', 'ab')

ORDER BY nentry DESC, ndoc DESC, word

LIMIT 10;

## 解析器

文本搜索解析器负责把未处理的文档文本划分成记号并且标识每一个记号的类型，而可能的类型集合由解析器本身定义。注意一个解析器完全不会修改文本 — 它简单地标识看似有理的词边界。因为这种有限的视野，对于应用相关的自定义解析器的需求就没有自定义字典那么强烈。目前瀚高数据库只提供了一种内建解析器，它已经被证实对很多种应用都适用。

内建解析器被称为pg\_catalog.default。它识别 23 种记号类型，如表 11.1所示。

+:——————–:+:————————–:+:—————————————————–:+  
| **别名** | **描述** | **例子** |  
+———————-+—————————-+——————————————————-+  
| asciiword | 单词，所有 ASCII 字母 | elephant |  
+———————-+—————————-+——————————————————-+  
| word | 单词，所有字母 | mañana |  
+———————-+—————————-+——————————————————-+  
| numword | 单词，字母和数字 | beta1 |  
+———————-+—————————-+——————————————————-+  
| asciihword | 带连字符的单词，所有 ASCII | up-to-date |  
+———————-+—————————-+——————————————————-+  
| hword | 带连字符的单词，所有字母 | lógico-matemática |  
+———————-+—————————-+——————————————————-+  
| numhword | 带连字符的单词，字母和数 | Highgo-beta1 |  
| | | |  
| | 字 | |  
+———————-+—————————-+——————————————————-+  
| hword\_asciipart | 带连字符的单词部分，所有 | Highgo in the context |  
| | | |  
| | ASCII | Highgo-beta1 |  
+———————-+—————————-+——————————————————-+  
| hword\_part | 带连字符的单词部分，所有 | lógico or matemática in the context lógico-matemática |  
| | | |  
| | 字母 | |  
+———————-+—————————-+——————————————————-+  
| hword\_numpart | 带连字符的单词部分，字母 | beta1 in the context |  
| | | |  
| | 和数字 | Highgo-beta1 |  
+———————-+—————————-+——————————————————-+  
| email | Email 地址 | [foo@example.com](mailto:foo@example.com) |  
+———————-+—————————-+——————————————————-+  
| protocol | 协议头部 | http:// |  
+———————-+—————————-+——————————————————-+  
| url | URL | example.com/stuff/ |  
| | | |  
| | | index.html |  
+———————-+—————————-+——————————————————-+  
| host | 主机 | example.com |  
+———————-+—————————-+——————————————————-+  
| url\_path | URL 路径 | /stuff/index.html, in the |  
| | | |  
| | | context of a URL |  
+———————-+—————————-+——————————————————-+  
| file | 文件或路径名 | /usr/local/foo.txt, if not within a URL |  
+———————-+—————————-+——————————————————-+  
| sfloat | 科学记数法 | -1.234e56 |  
+———————-+—————————-+——————————————————-+  
| float | 十进制记数法 | -1.234 |  
+———————-+—————————-+——————————————————-+  
| int | 有符号整数 | -1234 |  
+———————-+—————————-+——————————————————-+  
| uint | 无符号整数 | 1234 |  
+———————-+—————————-+——————————————————-+  
| version | 版本号 | 8.3.0 |  
+———————-+—————————-+——————————————————-+  
| tag | XML 标签 | \<a |  
| | | |  
| | | href="dictionaries.html"> |  
+———————-+—————————-+——————————————————-+  
| entity | XML 实体 | & |  
+———————-+—————————-+——————————————————-+  
| blank | 空格符号 | （其他不识别的任意空白或 |  
| | | |  
| | | 标点符号） |  
+———————-+—————————-+——————————————————-+

: 表 11.1 默认解析器的记号类型

+————————————————————————————————————————————————————————————————————+  
| **注意：** |  
| |  
| 解析器的一个”字母”的概念由数据库的区域设置决定，具体是lc\_ctype。只包含基本 ASCII 字母的词被报告为一个单独的记号类型，因为有时可以用来区别它们。在大部分欧洲语言中，记号类型word和asciiword应该被同样对待。 |  
| |  
| email不支持 RFC 5322 定义的所有合法 email 字符。具体来说，对 email 用户名被支持的非字母数字字符只有句点、破折号和下划线。 |  
+————————————————————————————————————————————————————————————————————+

解析器有可能从同一份文本得出相互覆盖的记号。例如，一个带连字符的词可能会被报告为一整个词或者多个部分：

SELECT alias, description, token FROM ts\_debug('foo-bar-beta1');

alias | description | token

\-----------------+------------------------------------------+---------------

numhword | Hyphenated word, letters and digits | foo-bar-beta1

hword\_asciipart | Hyphenated word part, all ASCII | foo

blank | Space symbols | -

hword\_asciipart | Hyphenated word part, all ASCII | bar

blank | Space symbols | -

hword\_numpart | Hyphenated word part, letters and digits | beta1

这种行为是值得要的，因为它允许对整个复合词和每个部分进行搜索。这里是另一个例子：

SELECT alias, description, token FROM ts\_debug(' [http://example.com/stuff/](http://example.com/stuff/)

index.html');

alias | description | token

\----------+---------------+------------------------------

protocol | Protocol head | http://

url | URL | example.com/stuff/index.html

host | Host | example.com

url\_path | URL path | /stuff/index.html

## 词典

词典被用来消除不被搜索考虑的词（stop words）、并被用来正规化词这样同一个词的不同派生形式将会匹配。一个被成功地正规化的词被称为一个词位。除了提高搜索质量，正规化和移除停用词减小了文档的tsvector表示的尺寸，因而提高了性能。正规化不会总是有语言上的意义并且通常依赖于应用的语义。

一些正规化的例子：

• 语言学的 - Ispell 词典尝试将输入词缩减为一种正规化的形式；词干分析器词典移除词的结尾

• URL位置可以被规范化来得到等效的 URL 匹配：

• [http://www.pgsql.ru/db/mw/index.html](http://www.pgsql.ru/db/mw/index.html)

• [http://www.pgsql.ru/db/mw/](http://www.pgsql.ru/db/mw/)

• [http://www.pgsql.ru/db/../db/mw/index.html](http://www.pgsql.ru/db/mw/index.html)

• 颜色名可以被它们的十六进制值替换，例如red, green, blue, magenta -> FF0000, 00FF00, 0000FF, FF00FF

• 如果索引数字，我们可以移除某些小数位来缩减可能的数字的范围，因此如果只保留小数点后两位，例如3.14159265359、3.1415926、3.14在正规化后会变得相同。

一个词典是一个程序，它接受一个记号作为输入，并返回：

• 如果输入的记号对词典是已知的，则返回一个词位数组（注意一个记号可能产生多于一个词位）

• 一个TSL\_FILTER标志被设置的单一词位，用一个新记号来替换要被传递给后续字典的原始记号（做这件事的一个字典被称为一个过滤字典）

• 如果字典知道该记号但它是一个停用词，则返回一个空数组

• 如果字典不识别该输入记号，则返回NULL

瀚高数据库为许多语言提供了预定义的字典。也有多种预定义模板可以被用于创建带自定义参数的新词典。每一种预定义词典模板在下面描述。如果没有合适的现有模板，可以创建新的；例子见Highgo发布的contrib/区域。

一个文本搜索配置把一个解析器和一组处理解析器输出记号的词典绑定在一起。对于每一中 器找到时，每一个词典都被按照顺序查询，知道某个词典将其识别为一个已知词。如果它被标识为一个停用词或者没有一个词典识别它，它将被丢弃并且不会被索引和用于搜索。通常，第一个返回非NULL输出的词典决定结果，并且任何剩下的词典都不会被查找；但是一个过滤词典可以将给定词替换为一个被修改的词，它再被传递给后续的词典。

配置一个词典列表的通用规则是将最狭窄、最特定的词典放在第一位，然后是更加通用的词典，以一个非常通用的词典结尾，像一个Snowball词干分析器或什么都识别的simple。例如，对于一个天文学相关的搜索（astro\_en 配置）我们可以把记号类型asciiword（ASCII词）绑定到一个天文学术语的分类词典、一个通用英语词典和一个Snowball英语词干分析器：

ALTER TEXT SEARCH CONFIGURATION astro\_en

ADD MAPPING FOR asciiword WITH astrosyn, english\_ispell, english\_stem;

一个过滤词典可以被放置在列表中的任意位置，除了在最后，因为过滤词典放在最后就等于无用。过滤词典可用于部分正规化词来简化后续词典的工作。例如，一个过滤词典可以被用来从音标字母中移除重音符号，就像unaccent模块所做的。

### 停用词

停用词是非常常用、在几乎每一个文档中出现并且没有任何区分度的词。因此，在全文搜索的环境中它们可以被忽略。例如，每一段英语文本都包含a和the等次，因此把它们存储在一个索引中是没有用处的。但是，停用词确实会影响在tsvector中的位置，这进而会影响排名：

SELECT to\_tsvector('english','in the list of stop words');

to\_tsvector

\----------------------------

'list':3 'stop':5 'word':6

缺失的位置 1、2、4 是因为停用词。文档的排名计算在使用和不使用停用词的情况下是很不同的：

SELECT ts\_rank\_cd (to\_tsvector('english','in the list of stop words'),

to\_tsquery('list & stop'));

ts\_rank\_cd

\------------

0.05

SELECT ts\_rank\_cd (to\_tsvector('english','list stop words'), to\_tsquery('list &

stop'));

ts\_rank\_cd

\------------

0.1

如何对待停用词是由指定词典决定的。例如，ispell词典首先正规化词并且查看停用词列表，而Snowball词干分析器首先检查停用词的列表。这种不同行为的原因是一冲降低噪声的尝试。

### 简单词典

simple词典模板的操作是将输入记号转换为小写形式并且根据一个停用词文件检查它。如果该记号在该文件中被找到，则返回一个空数组，导致该记号被丢弃。否则，该词的小写形式被返回作为正规化的词位。作为一种选择，该词典可以被配置为将非停用词报告为未识别，允许它们被传递给列表中的下一个词典。

下面是一个使用simple模板的词典定义的例子：

CREATE TEXT SEARCH DICTIONARY public.simple\_dict (

TEMPLATE = pg\_catalog.simple,

STOPWORDS = english

);

这里，english是一个停用词文件的基本名称。该文件的全名将是$SHAREDIR/tsearch\_data/ english.stop，其中$SHAREDIR表示Highgo安装的共享数据目录，通常是/usr/local/ share/Highgo（如果不确定，使用pg\_config --sharedir）。该文件格式是一个词的列表，每行一个。空行和尾部的空格都被忽略，并且大写也被折叠成小写，但是没有其他对该文件内容的处理。

现在我们能够测试我们的词典：

SELECT ts\_lexize('public.simple\_dict','YeS');

ts\_lexize

\-----------

{yes}

SELECT ts\_lexize('public.simple\_dict','The');

ts\_lexize

\-----------

{}

如果没有在停用词文件中找到，我们也可以选择返回NULL而不是小写形式的词。这种行为可以通过设置词典的Accept参数为false来选择。继续该例子：

ALTER TEXT SEARCH DICTIONARY public.simple\_dict ( Accept = false );

SELECT ts\_lexize('public.simple\_dict','YeS');

ts\_lexize

\-----------

SELECT ts\_lexize('public.simple\_dict','The');

ts\_lexize

\-----------

{}

在使用默认值Accept = true，只有把一个simple词典放在词典列表的尾部才有用，因为它将不会传递任何记号给后续的词典。相反，Accept = false只有当至少有一个后续词典的情况下才有用。

+——————————————————————————————————————————————————-+  
| **注意：** |  
| |  
| 大部分类型的词典依赖于配置文件，例如停用词文件。这些文件必须被存储为 UTF-8 编码。当它们被读入服务器时，如果存在不同，它们将被翻译成真实的数据库编码。 |  
+——————————————————————————————————————————————————-+

+————————————————————————————————————————————————————————————————————————————————+  
| **注意：** |  
| |  
| 通常，当一个词典配置文件第一次在数据库会话中使用时，数据库会话将只读取它一次。如果你修改了一个配置文件并且想强迫现有的会话取得新内容，可以在该词典上发出一个ALTER TEXT SEARCH DICTIONARY命令。这可以是一次”假”更新，它并不实际修改任何参数值。 |  
+————————————————————————————————————————————————————————————————————————————————+

### 同义词词典

这个词典模板被用来创建用于同义词替换的词典。不支持短语（使用分类词典模板。一个同义词词典可以被用来解决语言学问题，例如，阻止一个英语词干分析器词典把词”Paris”缩减成”pari”。在同义词词典中有一行Paris paris并把它放在english\_stem词典之前就足够了。例如：

SELECT \* FROM ts\_debug('english', 'Paris');

alias | description | token | dictionaries | dictionary | lexemes

\-----------+-----------------+-------+----------------+--------------+---------

asciiword | Word, all ASCII | Paris | {english\_stem} | english\_stem | {pari}

CREATE TEXT SEARCH DICTIONARY my\_synonym (

TEMPLATE = synonym,

SYNONYMS = my\_synonyms

);

ALTER TEXT SEARCH CONFIGURATION english

ALTER MAPPING FOR asciiword

WITH my\_synonym, english\_stem;

SELECT \* FROM ts\_debug('english', 'Paris');

alias | description | token | dictionaries | dictionary |

lexemes

\-----------+-----------------+-------+---------------------------+------------

+---------

asciiword | Word, all ASCII | Paris | {my\_synonym,english\_stem} | my\_synonym |

{paris}

synonym模板要求的唯一参数是SYNONYMS，它是其配置文件的基本名 — 上例中的my\_synonyms。该文件的完整名称将是$SHAREDIR/tsearch\_data/my\_synonyms.syn（其中$SHAREDIR表示数据库安装的共享数据目录）。该文件格式是每行一个要被替换的词，后面跟着它的同义词，用空白分隔。空行和结尾的空格会被忽略。

synonym模板还有一个可选的参数CaseSensitive，其默认值为false。

当CaseSensitive为false时，同义词文件中的词被折叠成小写，这和输入记号一样。当它为true时，词和记号将不会被折叠成小写，但是比较时就好像被折叠过一样。

一个星号（\*）可以被放置在配置文件中一个同义词的末尾。这表示该同义词是一个前缀。

当项被用在to\_tsvector()中时，星号会被忽略；当它被用在to\_tsquery()中时，结果将是一个带有前缀匹配标记器（见第 12.3.2 节）的查询项。例如，假设我们在$SHAREDIR/ tsearch\_data/synonym\_sample.syn中有这些项：

postgres pgsql

Highgo pgsql

postgre pgsql

gogle googl

indices index\*

那么我们将得到这些结果：

mydb=# CREATE TEXT SEARCH DICTIONARY syn (template=synonym,

synonyms='synonym\_sample');

mydb=# SELECT ts\_lexize('syn','indices');

ts\_lexize

\-----------

{index}

(1 row)

mydb=# CREATE TEXT SEARCH CONFIGURATION tst (copy=simple);

mydb=# ALTER TEXT SEARCH CONFIGURATION tst ALTER MAPPING FOR asciiword WITH syn;

mydb=# SELECT to\_tsvector('tst','indices');

to\_tsvector

\-------------

'index':1

(1 row)

mydb=# SELECT to\_tsquery('tst','indices');

to\_tsquery

\------------

'index':\*

(1 row)

mydb=# SELECT 'indexes are very useful'::tsvector;

tsvector

\---------------------------------

'are' 'indexes' 'useful' 'very'

(1 row)

mydb=# SELECT 'indexes are very useful'::tsvector @@

to\_tsquery('tst','indices');

?column?

\----------

t

(1 row)

### 分类词典

一个分类词典（有时被简写成TZ）是一个词的集合，其中包括了词与短语之间的联系，即广义词（BT）、狭义词（NT）、首选词、非首选词、相关词等。

基本上一个分类词典会用一个首选词替换所有非首选词，并且也可选择地保留原始术语用于索引。瀚高数据库分类词典的当前实现是同义词词典的一个扩展，并增加了短语支持。一个分类词典要求一个下列格式的配置文件：

\# this is a comment

sample word(s): indexed word(s)

more sample word(s): more indexed word(s)

...

其中冒号（:）符号扮演了一个短语及其替换之间的定界符。

一个分类词典使用一个子词典（在词典的配置中指定）在检查短语匹配之前正规化输入文本。只能选择一个子词典。如果子词典无法识别一个词，将报告一个错误。在这种情况下，你应该移除该词的使用或者让子词典学会这个词。你可以在一个被索引词的开头放上一个星号（\*）来跳过在其上应用子词典，但是所有采样词必须被子词典知道。

如果有多个短语匹配输入，则分类词典选择最长的那一个，并且使用最后的定义打破连结。

由子词典识别的特定停用词不能够被指定；改用?标记任何可以出现停用词的地方。例如，假定根据子词典a和the是停用词：

? one? two: swsw

匹配a one the two和the one a two；两者都将被swsw替换。

由于一个分类词典具有识别短语的能力，它必须记住它的状态并与解析器交互。一个分类词典使用这些任务来检查它是否应当处理下一个词或者停止累积。分类词典必须被小心地配置。例如，如果分类词典被分配只处理asciiword记号，则一个形如one 7的分类词典定义将不会工作，因为记号类型uint没有被分配给该分类词典。

+——————————————————————————————————————————————–+  
| **注意：** |  
| |  
| 在索引期间要用到分类词典，因此分类词典参数中的任何变化都要求重索引。对于大多数其他索引类型，例如增加或移除停用词等小改动都不会强制重索引。 |  
+——————————————————————————————————————————————–+

#### 分类词典配置

要定义一个新的分类词典，可使用thesaurus模板。例如：

CREATE TEXT SEARCH DICTIONARY thesaurus\_simple (

TEMPLATE = thesaurus,

DictFile = mythesaurus,

Dictionary = pg\_catalog.english\_stem

);

这里：

• thesaurus\_simple是新词典的名称

• mythesaurus是分类词典配置文件的基础名称（它的全名将是$SHAREDIR/tsearch\_data/ mythesaurus.ths，其中$SHAREDIR表示安装的共享数据目录）。

• pg\_catalog.english\_stem是要用于分类词典正规化的子词典（这里是一个 Snowball 英语词干分析器）。注意子词典将拥有它自己的配置（例如停用词），但这里没有展示。

现在可以在配置中把分类词典thesaurus\_simple绑定到想要的记号类型上，例如：

ALTER TEXT SEARCH CONFIGURATION russian

ALTER MAPPING FOR asciiword, asciihword, hword\_asciipart

WITH thesaurus\_simple;

#### 分类词典例子

考虑一个简单的天文学分类词典thesaurus\_astro，它包含一些天文学词组合：

supernovae stars: sn

crab nebulae: crab

下面我们创建一个词典并绑定一些记号类型到一个天文学分类词典以及英语词干分析器：

CREATE TEXT SEARCH DICTIONARY thesaurus\_astro (

TEMPLATE = thesaurus,

DictFile = thesaurus\_astro,

Dictionary = english\_stem

);

ALTER TEXT SEARCH CONFIGURATION russian

ALTER MAPPING FOR asciiword, asciihword, hword\_asciipart

WITH thesaurus\_astro, english\_stem;

现在我们可以看看它如何工作。ts\_lexize对于测试一个分类词典用处不大，因为它把它的输入看成是一个单一记号。我们可以用plainto\_tsquery和to\_tsvector，它们将把其输入字符串打断成多个记号：

SELECT plainto\_tsquery('supernova star');

plainto\_tsquery

\-----------------

'sn'

SELECT to\_tsvector('supernova star');

to\_tsvector

\-------------

'sn':1

原则上，如果你对参数加了引号，你可以使用to\_tsquery：

SELECT to\_tsquery('''supernova star''');

to\_tsquery

\------------

'sn'

注意在thesaurus\_astro中supernova star匹配supernovae stars，因为我们在分类词典定义中指定了english\_stem词干分析器。该词干分析器移除了e和s。

要和替补一样也索引原始短语，只要将它包含在定义的右手部分中：

supernovae stars: sn supernovae stars

SELECT plainto\_tsquery('supernova star');

plainto\_tsquery

\-----------------------------

'sn' & 'supernova' & 'star'

### Ispell 词典

Ispell词典模板支持词法词典，它可以把一个词的很多不同语言学的形式正规化成相同的词位。例如，一个英语Ispell词典可以匹配搜索词bank的词尾变化和词形变化，例如banking、banked、banks、banks'和bank's。

标准的瀚高数据库发布不包括任何Ispell配置文件。用于很多种语言的词典可以从Ispell1得到。此外，也支持一些更现代的词典文件格式 — MySpell2（OO < 2.0.1）和Hunspell3（OO >= 2.0.2）。一个很大的词典列表在OpenOffice Wiki4上可以得到。

要创建一个Ispell词典，执行这三步：

• 下载词典配置文件。OpenOffice扩展文件的扩展名是.oxt。有必要抽取.aff和.dic文件，把扩展改为.affix和.dict。对于某些词典文件，还需要使用下面的命令把字符转换成 UTF-8 编码（例如挪威语词典）：

iconv -f ISO\_8859-1 -t UTF-8 -o nn\_no.affix nn\_NO.aff

iconv -f ISO\_8859-1 -t UTF-8 -o nn\_no.dict nn\_NO.dic

• 拷贝文件到$SHAREDIR/tsearch\_data目录

• 用下面的命令把文件载入到 Highgo：

CREATE TEXT SEARCH DICTIONARY english\_hunspell (

TEMPLATE = ispell,

DictFile = en\_us,

AffFile = en\_us,

Stopwords = english);

这里，DictFile、AffFile和StopWords指定词典、词缀和停用词文件的基础名称。停用词文件的格式和前面解释的simple词典类型相同。其他文件的格式在这里没有指定，但是也可以从上面提到的网站获得。

Ispell 词典通常识别一个有限集合的词，这样它们后面应该跟着另一个更广义的词典；例如，一个 Snowball 词典，它可以识别所有东西。

Ispell的.affix文件具有下面的结构：

prefixes

flag \*A:

. > RE # As in enter > reenter

suffixes

flag T:

E > ST # As in late > latest

\[^AEIOU\]Y > -Y,IEST # As in dirty > dirtiest

\[AEIOU\]Y > EST # As in gray > grayest

\[^EY\] > EST # As in small > smallest

.dict文件具有下面的结构：

lapse/ADGRS

lard/DGRS

large/PRTY

lark/MRS

.dict文件的格式是：

basic\_form/affix\_class\_name

在.affix文件中，每一个词缀标志以下面的格式描述：

condition > \[-stripping\_letters,\] adding\_affix

这里的条件具有和正则表达式相似的格式。它可以使用分组\[...\]和\[^...\]。例如，\[AEIOU\]Y表示词的最后一个字母是"y"并且倒数第二个字母是"a"、"e"、"i"、"o"或

者"u"。\[^EY\]表示最后一个字母既不是"e"也不是"y"。

Ispell 词典支持划分复合词，这是一个有用的特性。注意词缀文件应该用compoundwords controlled语句指定一个特殊标志，它标记可以参与到复合格式中的词典词：

compoundwords controlled z

下面是挪威语的一些例子：

SELECT ts\_lexize('norwegian\_ispell', 'overbuljongterningpakkmesterassistent');

{over,buljong,terning,pakk,mester,assistent}

SELECT ts\_lexize('norwegian\_ispell', 'sjokoladefabrikk');

{sjokoladefabrikk,sjokolade,fabrikk}

MySpell格式是Hunspell格式的一个子集。Hunspell的.affix文件具有下面的结构：

PFX A Y 1

PFX A 0 re.

SFX T N 4

SFX T 0 st e

SFX T y iest \[^aeiou\]y

SFX T 0 est \[aeiou\]y

SFX T 0 est \[^ey\]

一个词缀类的第一行是头部。头部后面列出了词缀规则的域：

• 参数名（PFX 或者 SFX）

• 标志（词缀类的名称）

• 从该词的开始（前缀）或者结尾（后缀）剥离字符

• 增加词缀

• 和正则表达式格式类似的条件。

.dict文件看起来和Ispell的.dict文件相似：

larder/M

lardy/RT

large/RSPMYT

largehearted

+————————————————————————————————————–+  
| **注意：** |  
| |  
| MySpell 不支持复合词。Hunspell则对复合词有更好的支持。当前，瀚高数据库只实现了 Hunspell 中基本的复合词操作。 |  
+————————————————————————————————————–+

### Snowball 词典

Snowball词典模板基于 Martin Porter 的一个项目，他是流行的英语

Porter 词干分析算法的发明者。Snowball 现在对许多语言提供词干分析算法（详见Snowball 站点5）。每一个算法懂得按照其语言中的拼写，如何缩减词的常见变体形式为一个基础或词干。一个 Snowball 词典要求一个language参数来标识要用哪种词干分析器，并且可以选择地指定一个stopword文件名来给出一个要被消除的词列表（Highgo的标准停用词列表也是由 Snowball 项目提供的）。例如，有一个内建的定义等效于

CREATE TEXT SEARCH DICTIONARY english\_stem (

TEMPLATE = snowball,

Language = english,

StopWords = english

);

停用词文件格式和已经解释的一样。

一个Snowball词典识别所有的东西，不管它能不能简化该词，因此它应当被放置在词典列表的最后。把它放在任何其他词典前面是没有用处的，因为一个记号永远不会穿过它而进入到下一个词典。

## 配置例子

一个文本搜索配置指定了将一个文档转换成一个tsvector所需的所有选项：用于把文本分解成记号的解析器，以及用于将每一个记号转换成词位的词典。每一次to\_tsvector或to\_tsquery的调用都需要一个文本搜索配置来执行其处理。配置参数default\_text\_search\_config指定了默认配置的名称，如果忽略了显式的配置参数，文本搜索函数将会使用它。它可以在Highgo.conf中设置，或者使用SET命令为一个单独的会话设置。

有一些预定义的文本搜索配置可用，并且你可以容易地创建自定义的配置。为了便于管理文本搜索对象，可以使用一组SQL命令，并且有多个psql命令可以显示有关文本搜索对象的信息。

作为一个例子，我们将创建一个配置pg，从复制内建的english配置开始：

CREATE TEXT SEARCH CONFIGURATION public.pg ( COPY = pg\_catalog.english );

我们将使用一个瀚高数据库相关的同义词列表，并将它存储在$SHAREDIR/tsearch\_data/ pg\_dict.syn中。文件内容看起来像：

postgres pg

pgsql pg

Highgo pg

我们定义同义词词典如下：

CREATE TEXT SEARCH DICTIONARY pg\_dict (

TEMPLATE = synonym,

SYNONYMS = pg\_dict

);

接下来我们注册Ispell词典english\_ispell，它有其自己的配置文件：

CREATE TEXT SEARCH DICTIONARY english\_ispell (

TEMPLATE = ispell,

DictFile = english,

AffFile = english,

StopWords = english

);

现在我们可以在配置pg中建立词的映射：

ALTER TEXT SEARCH CONFIGURATION pg

ALTER MAPPING FOR asciiword, asciihword, hword\_asciipart,

word, hword, hword\_part

WITH pg\_dict, english\_ispell, english\_stem;

我们选择不索引或搜索某些内建配置确实处理的记号类型：

ALTER TEXT SEARCH CONFIGURATION pg

DROP MAPPING FOR email, url, url\_path, sfloat, float;

现在我们可以测试我们的配置：

SELECT \* FROM ts\_debug('public.pg', '

HighgoDB, the highly scalable, SQL compliant, open source object-relational

database management system, is now undergoing beta testing of the next

version of our software.

');

下一个步骤是设置会话让它使用新配置，它被创建在public模式中：

\=> \\dF

List of text search configurations

Schema | Name | Description

\---------+------+-------------

public | pg |

SET default\_text\_search\_config = 'public.pg';

SET

SHOW default\_text\_search\_config;

default\_text\_search\_config

\----------------------------

public.pg

## 测试和调试文本搜索

一个自定义文本搜索配置的行为很容易变得混乱。本节中描述的函数对于测试文本搜索对象有用。你可以测试一个完整的配置，或者独立测试解析器和词典。

### 配置测试

函数ts\_debug允许简单地测试一个文本搜索配置。

ts\_debug(\[ config regconfig, \] document text,

OUT alias text,

OUT description text,

OUT token text,

OUT dictionaries regdictionary\[\],

OUT dictionary regdictionary,

OUT lexemes text\[\])

returns setof record

ts\_debug显示document的每一个记号的信息，记号由解析器产生并由配置的词典处理过。该函数使用由config指定的配置，如果该参数被忽略则使用default\_text\_search\_config指定的配置。

ts\_debug为解析器在文本中标识的每一个记号返回一行。被返回的列是：

• alias text — 记号类型的短名称

• description text — 记号类型的描述

• token text — 记号的文本

• dictionaries regdictionary\[\] — 配置为这种记号类型选择的词典

• dictionary regdictionary — 识别该记号的词典，如果没有词典能识别则为NULL

• lexemes text\[\] — 识别该记号的词典产生的词位，如果没有词典能识别则为NULL；一个空数组（{}）表示该记号被识别为一个停用词

这里是一个简单的例子：

SELECT \* FROM ts\_debug('english','a fat cat sat on a mat - it ate a fat rats');

alias | description | token | dictionaries | dictionary | lexemes

\-----------+-----------------+-------+----------------+--------------+---------

asciiword | Word, all ASCII | a | {english\_stem} | english\_stem | {}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | fat | {english\_stem} | english\_stem | {fat}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | cat | {english\_stem} | english\_stem | {cat}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | sat | {english\_stem} | english\_stem | {sat}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | on | {english\_stem} | english\_stem | {}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | a | {english\_stem} | english\_stem | {}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | mat | {english\_stem} | english\_stem | {mat}

blank | Space symbols | | {} | |

blank | Space symbols | - | {} | |

asciiword | Word, all ASCII | it | {english\_stem} | english\_stem | {}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | ate | {english\_stem} | english\_stem | {ate}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | a | {english\_stem} | english\_stem | {}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | fat | {english\_stem} | english\_stem | {fat}

blank | Space symbols | | {} | |

asciiword | Word, all ASCII | rats | {english\_stem} | english\_stem | {rat}

为了一个更广泛的示范，我们先为英语语言创建一个public.english配置和 Ispell 词典：

CREATE TEXT SEARCH CONFIGURATION public.english ( COPY = pg\_catalog.english );

CREATE TEXT SEARCH DICTIONARY english\_ispell (

TEMPLATE = ispell,

DictFile = english,

AffFile = english,

StopWords = english

);

ALTER TEXT SEARCH CONFIGURATION public.english

ALTER MAPPING FOR asciiword WITH english\_ispell, english\_stem;

SELECT \* FROM ts\_debug('public.english','The Brightest supernovaes');

alias | description | token | dictionaries |

dictionary | lexemes

\-----------+-----------------+-------------+-------------------------------

+----------------+-------------

asciiword | Word, all ASCII | The | {english\_ispell,english\_stem} |

english\_ispell | {}

blank | Space symbols | | {} |

|

asciiword | Word, all ASCII | Brightest | {english\_ispell,english\_stem} |

english\_ispell | {bright}

blank | Space symbols | | {} |

|

asciiword | Word, all ASCII | supernovaes | {english\_ispell,english\_stem} |

english\_stem | {supernova}

在这个例子中，词Brightest被解析器识别为一个ASCII 词（别名asciiword）。对于这种记号类型，词典列表是english\_ispell和english\_stem。该词被english\_ispell识别，这个词典将它缩减为名词bright。词supernovaes对于english\_ispell词典是未知的，因此它被传递给下一个词典，并且幸运地是，它被识别了（实际上，english\_stem是一个 Snowball 词典，它识别所有的东西；这也是为什么它被放置在词典列表的尾部）。

词The被english\_ispell词典识别为一个停用词并且将不会被索引。空格也被丢弃，因为该配置没有为它们提供词典。

你可以通过显式地指定你想看哪些列来缩减输出的宽度：

SELECT alias, token, dictionary, lexemes

FROM ts\_debug('public.english','The Brightest supernovaes');

alias | token | dictionary | lexemes

\-----------+-------------+----------------+-------------

asciiword | The | english\_ispell | {}

blank | | |

asciiword | Brightest | english\_ispell | {bright}

blank | | |

asciiword | supernovaes | english\_stem | {supernova}

### 解析器测试

下列函数允许直接测试一个文本搜索解析器。

ts\_parse(parser\_name text, document text,

OUT tokid integer, OUT token text) returns setof record

ts\_parse(parser\_oid oid, document text,

OUT tokid integer, OUT token text) returns setof record

ts\_parse解析给定的document并返回一系列记录，每一个记录对应一个由解析产生的记号。

每一个记录包括一个tokid展示分配给记号的类型以及一个token展示记号的文本。例如：

SELECT \* FROM ts\_parse('default', '123 - a number');

tokid | token

\-------+--------

22 | 123

12 |

12 | -

1 | a

12 |

1 | number

ts\_token\_type(parser\_name text, OUT tokid integer,

OUT alias text, OUT description text) returns setof record

ts\_token\_type(parser\_oid oid, OUT tokid integer,

OUT alias text, OUT description text) returns setof record

ts\_token\_type返回一个表，该表描述指定解析器能够识别的每一种记号类型。对于每一种记号类型，该表给出了解析器用来标注该类型记号的整数tokid，还给出了在配置命令中命名该记号类型的alias，以及一个简短的description。例如：

SELECT \* FROM ts\_token\_type('default');

tokid | alias | description

\-------+-----------------+------------------------------------------

1 | asciiword | Word, all ASCII

2 | word | Word, all letters

3 | numword | Word, letters and digits

4 | email | Email address

5 | url | URL

6 | host | Host

7 | sfloat | Scientific notation

8 | version | Version number

9 | hword\_numpart | Hyphenated word part, letters and digits

10 | hword\_part | Hyphenated word part, all letters

11 | hword\_asciipart | Hyphenated word part, all ASCII

12 | blank | Space symbols

13 | tag | XML tag

14 | protocol | Protocol head

15 | numhword | Hyphenated word, letters and digits

16 | asciihword | Hyphenated word, all ASCII

17 | hword | Hyphenated word, all letters

18 | url\_path | URL path

19 | file | File or path name

20 | float | Decimal notation

21 | int | Signed integer

22 | uint | Unsigned integer

23 | entity | XML entity

### 词典测试

ts\_lexize函数帮助词典测试。

ts\_lexize(dict regdictionary, token text) returns text\[\]

如果输入的token是该词典已知的，则ts\_lexize返回一个词位数组；如果记号是词典已知的但是它是一个停用词，则返回一个空数组；或者如果它对词典是未知词，则返回NULL。

例子：

SELECT ts\_lexize('english\_stem', 'stars');

ts\_lexize

\-----------

{star}

SELECT ts\_lexize('english\_stem', 'a');

ts\_lexize

\-----------

{}

+———————————————————————–+  
| **注意：** |  
| |  
| ts\_lexize函数期望一个单一记号而不是文本。下面的情况会让它搞混： |  
| |  
| SELECT ts\_lexize('thesaurus\_astro','supernovae stars') is null; |  
| |  
|?column? |  
| |  
| ---------- |  
| |  
| t |  
| |  
| 分类词典thesaurus\_astro确实知道短语supernovae stars，但是ts\_lexize会 |  
| |  
| 失败，因为它无法解析输入文本而把它当做一个单一记号。可以使 |  
| |  
| 用plainto\_tsquery或to\_tsvector来测试分类词典，例如： |  
| |  
| SELECT plainto\_tsquery('supernovae stars'); |  
| |  
| plainto\_tsquery |  
| |  
| ----------------- |  
| |  
| 'sn' |  
+———————————————————————–+

## GIN 和 GiST 索引类型

有两种索引可以被用来加速全文搜索。注意全文搜索并非一定需要索引，但是在一个定期会被搜索的列上，通常需要有一个索引。

CREATE INDEX name ON table USING GIN(column);

创建一个基于 GIN（通用倒排索引）的索引。column必须是tsvector类型。

CREATE INDEX name ON table USING GIST(column);

创建一个基于 GiST（通用搜索树）的索引。column可以是tsvector或tsquery类型。

GIN 索引是更好的文本搜索索引类型。作为倒排索引，每个词（词位）在 其中都有一个索引项，其中有压缩过的匹配位置的列表。多词搜索可以找到 第一个匹配，然后使用该索引移除缺少额外词的行。GIN 索引只存储 tsvector值的词（词位），并且不存储它们的权重标签。因此， 在使用涉及权重的查询时需要一次在表行上的重新检查。

一个 GiST 索引是有损的，这表示索引可能产生假匹配，并且有必要检查真实的表行来消除这种假匹配（瀚高数据库在需要时会自动做这一步）。GiST 索引之所以是有损的，是因为每一个文档在索引中被表示为一个定长的签名。该签名通过哈希每一个词到一个 n 位串中的一个单一位来产生，通过将所有这些位 OR 在一起产生一个 n 位的文档签名。当两个词哈希到同一个位位置时就会产生假匹配。如果查询中所有词都有匹配（真或假），则必须检索表行查看匹配是否正确。

GiST 索引可以被覆盖，例如使用INCLUDE子句。 包含的列可以具有没有任何 GiST 操作符类的数据类型。 包含的属性将非压缩存储。

有损性导致的性能下降归因于不必要的表记录（即被证实为假匹配的记录）获取。因为表记录的随机访问是较慢的，这限制了 GiST 索引的可用性。假匹配的可能性取决于几个因素，特别是唯一词的数量，因此推荐使用词典来缩减这个数量。

注意GIN索引的构件时间常常可以通过增加maintenance\_work\_mem来改进，而GiST索引的构建时间则与该参数无关。

对大集合分区并正确使用 GIN 和 GiST 索引允许实现带在线更新的快速搜索。分区可以在数据库层面上使用表继承来完成，或者是通过将文档分布在服务器上并收集外部的搜索结果，例如通过外部数据访问。后者是可能的，因为排名函数只使用本地信息。

## psql支持

关于文本搜索配置对象的信息可以在psql中使用一组命令获得：

\\dF{d,p,t}\[+\] \[PATTERN\]

可选的+能产生更多细节。

可选参数PATTERN可以是一个文本搜索对象的名称，可以是模式限定的。如果PATTERN被忽略，则所有可见对象的信息都将被显示。PATTERN可以是一个正则表达式并且可以为模式和对象名称提供独立的模式。下面的例子展示了这些特性：

\=> \\dF \*fulltext\*

List of text search configurations

Schema | Name | Description

\--------+--------------+-------------

public | fulltext\_cfg |

\=> \\dF \*.fulltext\*

List of text search configurations

Schema | Name | Description

\----------+----------------------------

fulltext | fulltext\_cfg |

public | fulltext\_cfg |

可用的命令是：

\\dF\[+\] \[PATTERN\]

列出文本搜索配置（加上+得到更多细节）。

\=> \\dF russian

List of text search configurations

Schema | Name | Description

\------------+---------+------------------------------------

pg\_catalog | russian | configuration for russian language

\=> \\dF+ russian

Text search configuration "pg\_catalog.russian"

Parser: "pg\_catalog.default"

Token | Dictionaries

\-----------------+--------------

asciihword | english\_stem

asciiword | english\_stem

email | simple

file | simple

float | simple

host | simple

hword | russian\_stem

hword\_asciipart | english\_stem

hword\_numpart | simple

hword\_part | russian\_stem

int | simple

numhword | simple

numword | simple

sfloat | simple

uint | simple

url | simple

url\_path | simple

version | simple

word | russian\_stem

\\dFd\[+\] \[PATTERN\]

列出文本搜索词典（加上+得到更多细节）。

\=> \\dFd

List of text search dictionaries

Schema | Name | Description

\------------+-----------------

+-----------------------------------------------------------

pg\_catalog | arabic\_stem | snowball stemmer for arabic language

pg\_catalog | danish\_stem | snowball stemmer for danish language

pg\_catalog | dutch\_stem | snowball stemmer for dutch language

pg\_catalog | english\_stem | snowball stemmer for english language

pg\_catalog | finnish\_stem | snowball stemmer for finnish language

pg\_catalog | french\_stem | snowball stemmer for french language

pg\_catalog | german\_stem | snowball stemmer for german language

pg\_catalog | hungarian\_stem | snowball stemmer for hungarian language

pg\_catalog | indonesian\_stem | snowball stemmer for indonesian language

pg\_catalog | irish\_stem | snowball stemmer for irish language

pg\_catalog | italian\_stem | snowball stemmer for italian language

pg\_catalog | lithuanian\_stem | snowball stemmer for lithuanian language

pg\_catalog | nepali\_stem | snowball stemmer for nepali language

pg\_catalog | norwegian\_stem | snowball stemmer for norwegian language

pg\_catalog | portuguese\_stem | snowball stemmer for portuguese language

pg\_catalog | romanian\_stem | snowball stemmer for romanian language

pg\_catalog | russian\_stem | snowball stemmer for russian language

pg\_catalog | simple | simple dictionary: just lower case and check

for stopword

pg\_catalog | spanish\_stem | snowball stemmer for spanish language

pg\_catalog | swedish\_stem | snowball stemmer for swedish language

pg\_catalog | tamil\_stem | snowball stemmer for tamil language

pg\_catalog | turkish\_stem | snowball stemmer for turkish language

\\dFp\[+\] \[PATTERN\]

列出文本搜索解析器（加上+得到更多细节）。

\=> \\dFp

List of text search parsers

Schema | Name | Description

\------------+---------+---------------------

pg\_catalog | default | default word parser

\=> \\dFp+

Text search parser "pg\_catalog.default"

Method | Function | Description

\-----------------+----------------+-------------

Start parse | prsd\_start |

Get next token | prsd\_nexttoken |

End parse | prsd\_end |

Get headline | prsd\_headline |

Get token types | prsd\_lextype |

Token types for parser "pg\_catalog.default"

Token name | Description

\-----------------+------------------------------------------

asciihword | Hyphenated word, all ASCII

asciiword | Word, all ASCII

blank | Space symbols

email | Email address

entity | XML entity

file | File or path name

float | Decimal notation

host | Host

hword | Hyphenated word, all letters

hword\_asciipart | Hyphenated word part, all ASCII

hword\_numpart | Hyphenated word part, letters and digits

hword\_part | Hyphenated word part, all letters

int | Signed integer

numhword | Hyphenated word, letters and digits

numword | Word, letters and digits

protocol | Protocol head

sfloat | Scientific notation

tag | XML tag

uint | Unsigned integer

url | URL

url\_path | URL path

version | Version number

word | Word, all letters

(23 rows)

\\dFt\[+\] \[PATTERN\]

列出文本搜索模板（加上+得到更多细节）。

\=> \\dFt

List of text search templates

Schema | Name | Description

\------------+-----------

+-----------------------------------------------------------

pg\_catalog | ispell | ispell dictionary

pg\_catalog | simple | simple dictionary: just lower case and check for

stopword

pg\_catalog | snowball | snowball stemmer

pg\_catalog | synonym | synonym dictionary: replace word by its synonym

pg\_catalog | thesaurus | thesaurus dictionary: phrase by phrase substitution

## 限制

瀚高数据库的文本搜索特性的当前限制是：

• 每一个词位的长度必须小于 2K 字节

• 一个tsvector（词位 + 位置）的长度必须小于 1 兆字节

• 词位的数量必须小于 264

• tsvector中的位置值必须大于 0 并且小于 16,383

• \<N>（FOLLOWED BY）tsquery操作符中的匹配距离不能超过 16,384

• 每个词位不超过 256 个位置

• 一个tsquery中结点（词位 + 操作符）的个数必须小于 32,768

为了对比，Highgo 8.1 的文档包含 10,441 个唯一词，总数 335,420 个词，并且最频繁的词”Highgo”在 655 个文档中被提到 6,127 次。

另一个例子 — Highgo的邮件列表归档在 461,020 条消息的 57,491,343 个词位中包含 910,989 个唯一词。

## 中文分词检索

#### 中文全文检索

全文检索提供了确定满足一个查询的自然语言文档的能力，并可以选择将它们与查询的相关度排序。最常用的搜索类型是找到所有包含给定查询词的文档并按照它们与查询的相似性顺序返回它们。

文本搜索操作符已经在数据库中存在很多年了。瀚高数据库对文本数据类型提供了~、~\*、LIKE和ILIKE操作符，但是它们缺少现代信息系统所要求的很多基本属性：

- 对英语也缺乏很好的支持。正则表达式的处理能力不强，不能处理派生词，例如satisfies和satisfy。搜索satisfy的时候，会漏掉satisfies。
- 它们不提供对搜索结果的排序
- 它们没有索引的支持

#### 解决方案

HGDB的全文检索采用了二元分词方法，比如: ‘hello’二元分词后：’he el ll lo’。HGDB全文检索整体方案如下：

1、利用rum索引

2、仿照rum\_tsvector\_ops实现hgdb的zhfts\_text\_ops

3、采用二元分词，分词结果依然用tsvector保存

4、搜索条件采用tsquery的方式，支持&、|等关系符

5、tsvector和tsquery不出现在操作语句中，操作语句只有text类型

6、匹配操作符采用%,而不是@@

7、提供like：select \* from t1 body like ‘%hello’;

8、提供类似pg\_trgm的similarity，为相似度打分。

#### 使用方式

ENSION zhfts;

其次，在text类型的列上建立zhfts索引：

CREATE TABLE test\_rum(id int, message text);

CREATE INDEX rumidx ON test\_rum USING zhfts (message zhfts\_text\_ops);

插入数据：

INSERT INTO test\_rum VALUES (1,'我在青岛');

INSERT INTO test\_rum VALUES (2,'我在济南大明湖');

查询数据：

set enable\_seqscan=OFF;

select \* from test\_rum WHERE message % '青岛';

select \* from test\_rum WHERE message % '我在青岛';

#### 操作符

① 匹配符号 %

当要在表中的某一列搜索某个词时，需要使用百分号%来表示该搜索。百分号前面指定一个数据列，后面指定一个查询条件。

例如：

select \* from test\_rum WHERE message % '青岛';

百分号后面的查询条件可以是多个词，词与词之间可以是：与关系(&)，或关系(|)。

例如：

select \* from test\_rum WHERE message % '青岛 | 济南';

select \* from test\_rum WHERE message % '济南 & 大明湖';

一个词不能有空格，否则语法检查会报错，查询也不会执行。

如果需要查询多个词，必须使用逻辑符号（ “|“，”&”）来关联多个词。

② 相似比较 like

LIKE的引入，主要是为了在语法上支持非索引情况下的LIKE。

select \* from test\_rum WHERE message LIKE '青岛';

select \* from test\_rum WHERE message LIKE '%青岛';

在zhfts索引中，其处理方式类似与%。zhfts把搜索条件中的百分号%去掉，对剩余的文本做二元分词，把分词的结果作为key，搜索索引。

③ 相似度和order by <->

搜索中，搜索条件和某行的列数据匹配，则该行数据符合条件，会出现在搜索结果中。有些情况下，需要对搜索结果排序，相似度高的数据排列在前面，则需要使用：order by <->。

例如：

select \* from test\_rum WHERE message % '我在青岛' order by message <->'我在青岛';

其中，message <->'我在青岛'，会调用内置函数，计算2个参数之间的相似度，返回一个浮点数。数值越小，越相似。默认情况下，越相似的匹配就会排到前面。