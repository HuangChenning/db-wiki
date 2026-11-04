---
title: "系统参数"
book: "MySQL兼容性"
version: "V9"
source: "https://www.highgo.com/document/v9/zh-cn/compatibility/compMySql7.html"
tags:
  - highgo
  - highgo-v9
  - compatibility-mysql
---

## 系统参数

## 兼容参数

说明

sql\_mode、div\_precision\_increment、max\_sort\_length、lower\_case\_table\_names 小节所述参数从V9.0.4开始支持；其他小节所述参数从V9.0.5开始支持。

### sql\_mode

当前服务器的SQL模式。

| 属性 | 描述 |
| --- | --- |
| 系统参数 | sql\_mode |
| 范围 | 全局，会话 |
| 可动态设置 | 是 |
| 类型 | Set |
| 默认值 | ONLY\_FULL\_GROUP\_BY   STRICT\_TRANS\_TABLES   NO\_ZERO\_IN\_DATE   NO\_ZERO\_DATE   ERROR\_FOR\_DIVISI   ON\_BY\_ZERO   NO\_AUTO\_CREATE\_USER   NO\_ENGINE\_SUBSTITUTION   ANSI\_QUOTES   PIPES\_AS\_CONCAT   REAL\_AS\_FLOAT |
| 有效值 | ALLOW\_INVALID\_DATES   ANSI\_QUOTES   ERROR\_FOR\_DIVISION\_BY\_ZERO   HIGH\_NOT\_PRECEDENCE   IGNORE\_SPACE   NO\_AUTO\_CREATE\_USER   NO\_AUTO\_VALUE\_ON\_ZERO   NO\_BACKSLASH\_ESCAPES   NO\_DIR\_IN\_CREATE   NO\_ENGINE\_SUBSTITUTION   NO\_FIELD\_OPTIONS   NO\_KEY\_OPTIONS   NO\_TABLE\_OPTIONS   NO\_UNSIGNED\_SUBTRACTION   NO\_ZERO\_DATE   NO\_ZERO\_IN\_DATE   ONLY\_FULL\_GROUP\_BY   PAD\_CHAR\_TO\_FULL\_LENGTH   PIPES\_AS\_CONCAT   REAL\_AS\_FLOAT   STRICT\_ALL\_TABLES   STRICT\_TRANS\_TABLES |
| 说明 | 以下值目前仅语法兼容：HIGH\_NOT\_PRECEDENCE   IGNORE\_SPACE   NO\_AUTO\_CREATE\_USER   NO\_BACKSLASH\_ESCAPES   NO\_DIR\_IN\_CREATE   NO\_ENGINE\_SUBSTITUTION   NO\_FIELD\_OPTIONS   NO\_KEY\_OPTIONS   NO\_TABLE\_OPTIONS   NO\_UNSIGNED\_SUBTRACTION   ONLY\_FULL\_GROUP\_BY   STRICT\_TRANS\_TABLES |

### div\_precision\_increment

此变量指示通过使用 / 运算符执行除法操作时，结果的小数位数增加的位数。默认值为 4。最小值和最大值分别为 0 和 30。

| 属性 | 描述 |
| --- | --- |
| 系统参数 | div\_precision\_increment |
| 范围 | 全局，会话 |
| 可动态设置 | 是 |
| 类型 | Integer |
| 默认值 | 4 |
| 最小值 | 0 |
| 最大值 | 30 |

### max\_sort\_length

用于排序数据值时的字节数。服务器仅使用每个值的前max\_sort\_length个字节，其余部分会被忽略。因此，对于GROUP BY、ORDER BY和DISTINCT操作，只有在前max\_sort\_length个字节之后才有所不同的值会被视为相等。增加max\_sort\_length的值可能需要同时增加sort\_buffer\_size的值。

| 属性 | 描述 |
| --- | --- |
| 系统变量 | max\_sort\_length |
| 范围 | 全局，会话 |
| 可动态设置 | 是 |
| 类型 | Integer |
| 默认值 | 1024 |
| 最小值 | 4 |
| 最大值 | 8388608 |
| 单位 | bytes |

### lower\_case\_table\_names

MySQL大小写参数。该参数决定使用哪种大小写方式：

- 设置为 0，表名按指定方式存储，比较时区分大小写；
- 设置为 1，表名在磁盘上以小写存储，比较时不区分大小写；
- 设置为 2，表名按给定方式存储，但比较时转换为小写。

| 属性 | 描述 |
| --- | --- |
| 系统变量 | lower\_case\_table\_names |
| 范围 | 全局 |
| 可动态设置 | 否 |
| 类型 | Integer |
| 默认值 (macOS) | 2 |
| 默认值 (Unix) | 0 |
| 默认值 (Windows) | 1 |
| 最小值 | 0 |
| 最大值 | 2在 Linux（以及其他类 Unix 系统）上，设置该值为 2 不受支持；服务器会强制将其值设为 0。 |

### sql\_quote\_show\_create

此变量如果启用（默认设置），服务器会在执行 SHOW CREATE TABLE 和 SHOW CREATE DATABASE 语句时为标识符添加引号。如果禁用，则不会添加引号。该选项默认启用，以便在复制时需要引号的标识符能够正常工作。

| 属性 | 描述 |
| --- | --- |
| 系统变量 | sql\_quote\_show\_create |
| 范围 | Global, Session |
| 可动态设置 | 是 |
| 类型 | Boolean |
| 默认值 | ON |

### auto\_increment\_increment

用于源到源复制，用于控制自增列值之间的间隔。若设为 0，其实际值会被自动调整为 1；若试图设为大于 65,535 或小于 0 的整数，则实际值会被强制设为  
65,535；若试图将设为非整数值，则会报错，且变量原值保持不变。

| 属性 | 描述 |
| --- | --- |
| 系统变量 | auto\_increment\_increment |
| 范围 | Global, Session |
| 可动态设置 | 是 |
| 类型 | Integer |
| 默认值 | 1 |
| 最小值 | 1 |
| 最大值 | 65535 |

### auto\_increment\_offset

用于源到源复制，用来决定 AUTO\_INCREMENT 列值的起始点。若设为 0，则其实际值会被自动调整为 1；若试图设为大于 65,535 或小于 0 的整数，则实际值会被强制设为 65,535；若试图设为非整数值，则会报错，且变量原值保持不变。

| 属性 | 描述 |
| --- | --- |
| 系统变量 | auto\_increment\_offset |
| 范围 | Global, Session |
| 可动态设置 | 是 |
| 类型 | Integer |
| 默认值 | 1 |
| 最小值 | 1 |
| 最大值 | 65535 |

注意

当 auto\_increment\_offset 的值大于 auto\_increment\_increment 的值时，auto\_increment\_offset 的值将被忽略。

### sha256\_password\_public\_key\_path

caching\_sha2\_password认证方式构建可信信道时使用的公钥地址。

### sha256\_password\_private\_key\_path

caching\_sha2\_password认证方式构建可信信道时使用的私钥地址。

## GUC参数

MySQL兼容特性相关的参数。除ivorysql.database\_mode之外，其他所有GUC参数均可在配置文件postgresql.conf中进行修改，也可通过命令行修改。

说明

ivorysql.compatible\_mode、ivorysql.database\_mode、mysql.listen\_addresses、mysql.port 小节所述参数从V9.0.4开始支持；其他小节所述参数从V9.0.5开始支持。

### ivorysql.compatible\_mode

| 属性 | 描述 |
| --- | --- |
| 参数类型 | String |
| 语法 | set ivorysql.compatible\_mode = pg \| mysql |
| 默认值 | mysql |
| 可修改 | 是 |
| 说明 | 设置兼容模式。当实例初始化为mysql兼容模式时，该参数可设置为pg或者mysql。通过mysql端口连接到数据库，该参数的默认值为mysql。 |

### ivorysql.database\_mode

| 属性 | 描述 |
| --- | --- |
| 参数类型 | String |
| 默认值 | oracle |
| 可修改 | 初始化实例时设置。实例初始化完成后，该参数的值不可修改，仅可通过show命令查看。 |
| 说明 | 数据库实例的兼容模式。 |

### mysql.listen\_addresses

| 属性 | 描述 |
| --- | --- |
| 参数类型 | String |
| 默认值 | localhost |
| 可修改 | 是 |
| 说明 | MySQL兼容模式服务IP |

### mysql.port

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Number |
| 默认值 | 3306 |
| 可修改 | 是 |
| 说明 | MySQL兼容模式服务端口号 |

### mysql.protocol\_type

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Enum |
| 默认值 | mysql |
| 可修改 | 是 |
| 说明 | MySQL兼容模式的协议类型，可选pg或mysql |

### mysql.default\_database

| 属性 | 描述 |
| --- | --- |
| 参数类型 | String |
| 默认值 | highgo |
| 可修改 | 建议在数据库安装完成后，首次使用之前配置。后续使用不建议修改。 |
| 说明 | MySQL兼容模式兼容MYSQL协议连接的默认数据库 |

### mysql.use\_mysql\_do

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Boolean |
| 默认值 | pg协议下默认false； mysql协议默认true |
| 可修改 | 初始化实例后不建议修改 |
| 说明 | 是否启用mysql的do命令 |

### mysql.at\_or\_atat

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Boolean |
| 默认值 | pg协议下默认false；mysql协议默认true |
| 可修改 | 初始化实例后不建议修改 |
| 说明 | 是否启用自定义变量功能 |

### mysql.cast\_to\_char

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Boolean |
| 默认值 | true |
| 可修改 | 初始化实例后不建议修改 |
| 说明 | 是否兼容mysql cast(xxx as char)语法 |

### mysql.enable\_mysql\_information\_schema

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Boolean |
| 默认值 | pg协议下默认false；mysql协议默认true |
| 可修改 | 初始化实例后不建议修改 |
| 说明 | 是否启用mysql的information\_schema |

### mysql.enable\_case\_switch

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Boolean |
| 默认值 | true |
| 可修改 | 初始化实例后不建议修改 |
| 说明 | mysql兼容模式下是否启用大小写转换功能 |

### mysql.mode\_pad\_char\_to\_full

| 属性 | 描述 |
| --- | --- |
| 参数类型 | Boolean |
| 默认值 | true |
| 可修改 | 初始化实例后不建议修改 |
| 说明 | 输出CHAR类型时，是否去掉尾部空格 |