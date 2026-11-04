---
title: "UTL_FILE 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/utl_file-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

UTL\_FILE 包为 PL/SQL 程序提供读和写操作系统数据文件的功能。它提供一套严格的使用标准操作系统文件 I/O 方式：open、put、 get 和 close 操作。

当用户想读取或写一个数据文件的时候，可以使用 FOPEN 来返回文件句柄。这个文件句柄将用于随后在文件上的所有操作。例如，过程 PUT\_LINE 写 text 字符串和行终止符到一个已打开的文件句柄，以及使用 GET\_LINE 来读取指定文件句柄的一行到提供的缓存。

## 24.1 数据类型

UTL\_FILE 定义了一种 FILE\_TYPE 记录类型。FILE\_TYPE 类型是 UTL\_FILE 专有类型。用户不能引用和改变该记录的内容。FILE\_TYPE 记录类型定义如下：

**语法如下：**

```
TYPE FILE_TYPE IS RECORD (
    ID                INTEGER, 
    DATATYPE        INTEGER,
    BYTE_MODE        BOOLEAN
);
```

**参数详解**

- ID 需要处理的外部文件句柄。
- DATATYPE 文件的类型：1 表示 CHAR 、2 表示 NCHAR、3 表示 binary。
- BYTE\_MODE 文件打开后的类型：TRUE 表示二进制模式；FALSE 表示文本模式。

## 24.2 相关方法

UTL\_FILE 包中的 23 个过程和函数详细介绍如下：

> **注意**
> 
> UTL\_FILE包只能访问目录对象中的数据文件，并且执行文件操作的用户必须具有针对当前目录对象的相关操作权限。  
> UTL\_FILE包不支持打开ASM文件系统上的路径。

以下详细介绍各过程和函数：

1. FCLOSE

关闭一个已打开文件。

**语法如下：**

```
PROCEDURE FCLOSE(
    FILE    IN OUT        FILE_TYPE
);
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。
2. FCLOSE\_ALL

关闭在这个会话里打开的所有文件。可用作紧急情况下清理程序，比如，当 PL/SQL 存在异常时。在 FCLOSE\_ALL 之前打开的所有文件都无法进一步读或写。

**语法如下：**

```
PROCEDURE FCLOSE_ALL;
```
3. FCOPY

把一个文本文件中指定的连续的行数据拷贝到另外一个文件中。源文件需要以可读模式打开。

**语法如下：**

```
PROCEDURE FCOPY(
    SRC_LOCATION    IN        VARCHAR(128),
    SRC_FILENAME    IN        VARCHAR(128), 
    DEST_LOCATION    IN        VARCHAR(128), 
    DEST_FILENAME    IN        VARCHAR(128), 
    START_LINE        IN        INTEGER        DEFAULT 1,
    END_LINE        IN        INTEGER        DEFAULT NULL
);
```

**参数详解**

- SRC\_LOCATION 源文件所在的目录对象名。
- SRC\_FILENAME 被拷贝的源文件名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。SRC\_LOCATION 与 SRC\_FILENAME 拼成的路径串总长度不能超过 256。
- DEST\_LOCATION 新创建的目标文件所在的目录对象名。
- DEST\_FILENAME 源文件的新名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。DEST\_LOCATION 与 DEST\_FILENAME 拼成的路径串总长度不能超过 256。
- START\_LINE 拷贝的起始行，缺省为文件的第 1 行。
- END\_LINE 拷贝的终止行，缺省为 NULL，即为文件的最后一行。
4. FFLUSH

以物理写入的方式将待定的数据写入到文件句柄所指定的文件中。通常地，待写入文件的数据是存放在缓冲区中的。FFLUSH 程序强制将缓冲区中的数据写入到文件中。数据必须以换行符结束。

**语法如下：**

```
PROCEDURE FFLUSH(
    FILE    IN        FILE_TYPE
) ;
```

**参数详解**

- FILE 由 FOPEN 调用，返回的文件句柄。
5. FGETATTR

读取并返回磁盘文件的属性。

**语法如下：**

```
PROCEDURE FGETATTR(
    LOCATION        IN          VARCHAR(128),
    FILENAME        IN          VARCHAR(128),
    FEXISTS            OUT         BOOLEAN,
    FILE_LENGTH        OUT         NUMBER,
    BLOCKSIZE        OUT         NUMBER
);
```

**参数详解**

- LOCATION 源文件所在的目录对象名。
- FILENAME 被检查的文件名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。LOCATION 与 FILENAME 拼成的路径串总长度不能超过 256。
- FEXISTS 文件是否存在，存在为 1，不存在为 0。
- FILE\_LENGTH 文件的长度（字节），若文件不存在，则长度为 NULL。
- BLOCKSIZE 文件系统中数据块的大小（字节），若文件不存在，则长度为 NULL。
6. FGETPOS

指定文件中当前相对位置偏移量（字节）。

语法如下：

```
FUNCTION  FGETPOS(

    FILE        IN        FILE_TYPE

)RETURN INTEGER;
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。

**返回值**

返回值 FGETPOS 以字节的方式返回一个打开文件相对位置偏移量。如果文件未打开则发生异常。如果当前位置在文件的最开始，则返回 0。

**注意事项：**

如果文件以 byte 的模式打开，那么会发生 INVALID OPERATION。

7. FOPEN

打开指定文件并返回一个文件句柄。FOPEN 不支持访问数据库内建文件（归档日志和联机日志除外），例如 dmarch.ini。

**语法如下：**

```
FUNCTION FOPEN(
    LOCATION        IN         VARCHAR(128),
    FILENAME         IN         VARCHAR(128),
    OPEN_MODE        IN         VARCHAR(128),
    MAX_LINESIZE     IN         INTEGER         DEFAULT 1024
)RETURN FILE_TYPE;
```

**参数详解**

- LOCATION 源文件所在的目录对象名。
- FILENAME 文件名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。在 UNIX 系统中，文件名不能包含转义符：“/”。LOCATION 与 FILENAME 拼成的路径串总长度不能超过 256。
- OPEN\_MODE 文件打开模式。包括：r 只读模式；w 写模式；a 附加模式；rb 只读打开一个二进制文件，只允许读；wb 只写打开或建立一个二进制文件，只允许写数据；ab 追加打开一个二进制文件，并在文件末尾写数据。当以“a”或“ab”的方式打开文件时，若该文件不存在，则以“w”的方式创建该文件。
- MAX\_LINESIZE 文件每行最大的字符数，包括换行符。最小为 1，最大为 32767。

**注意事项：**

目录对象名和文件名必须加上引号；对文件的访问和操作需要满足目录对象的权限控制要求。

8. FREMOVE

在有足够权限的情况下，从目录中删除一个文件。

**语法如下：**

```
PROCEDURE FREMOVE(
    LOCATION     IN         VARCHAR(128),  
    FILENAME     IN         VARCHAR(128)
);
```

**参数详解**

- location 被删除文件所在的目录对象名。
- filename 被删除文件名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。location 与 filename 拼成的路径串总长度不能超过 256。

**注意事项：**

FREMOVE 存储过程不会在删除文件之前验证权限，但是操作系统会验证文件和目录对象名称的正确性。没有权限，或者文件和目录对象名称不正确，则返回删除失败信息。

9. FRENAME

修改一个文件的名称。

**语法如下：**

```
PROCEDURE FRENAME(
    SRC_LOCATION      IN         VARCHAR(128), 
    SRC_FILENAME      IN         VARCHAR(128), 
    DEST_LOCATION     IN         VARCHAR(128), 
    DEST_FILENAME     IN         VARCHAR(128), 
    OVERWRITE         IN         BOOLEAN         DEFAULT FALSE
);
```

**参数详解**

- SRC\_LOCATION 要改名文件所在的目录对象名。
- SRC\_FLIENAME 要改名的源文件名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。SRC\_LOCATION 与 SRC\_FILENAME 拼成的路径串总长度不能超过 256。
- DEST\_LOCATION 改名后文件所在的目录对象名。
- DEST\_FILENAME 修改后的新名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。DEST\_LOCATION 与 DEST\_FILENAME 拼成的路径串总长度不能超过 256。
- OVERWRITE 设置是否能够重写。如果设置为“true”，则在 SRC\_LOCATION 目录中覆盖任何名为 DEST\_FILENAME 的文件。若设置为“false”，就会产生异常。缺省为 FALSE。
10. FSEEK

根据指定的字节数，调整文件指针前进或后退。

**语法如下：**

```
PROCEDURE FSEEK(
    FILE                  IN         FILE_TYPE,  
    ABSOLUTE_OFFSET     IN         INTEGER         DEFAULT NULL,
    RELATIVE_OFFSET     IN         INTEGER         DEFAULT NULL
);
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。
- ABSOLUTE\_OFFSET 要寻找的字节的绝对路径，默认为 NULL。
- RELATIVE\_OFFSET 指针前进或后退的字节数。用正整数表示向前查找，负整数表示向后查找。

**注意事项：**

使用 FSEEK，可以读取先前的行而不用关闭文件再重新打开。但是你必须知道要跳过的字符数。

该存储过程根据 relative\_offset 参数指定的字节数进行查找。

如果在指定字节数之前就已经到达了文件的开头，那么文件指针指定在文件开头。如果在指定字节数之前就已经到达了文件的尾部，那么 INVALID\_OFFSET 错误就会发生。

以 RB 方式打开的文件，支持通过 FSEEK 设置偏移；以其余二进制模式打开的文件，使用 FSEEK 时会发生 INVALID OPERATION 异常。

当 ABSOLUTE\_OFFSET 不为 0 时，设置 RELATIVE\_OFFSET 不为 0 不生效，即如需使用相对偏移，需要将 ABSOLUTE\_OFFSET 参数置为 0。

11. GET\_LINE

读取指定文件的一行到提供的缓存。读取的文本不包括该行的终结符，或者直到文件的末尾，或者到指定的长度。并且不能超过 FOPEN 时指定的 MAX\_LINESIZE。

**语法如下：**

```
PROCEDURE  GET_LINE(
    FILE            IN          FILE_TYPE,
    BUFFER          OUT         VARCHAR,
    LEN             IN          INTEGER         DEFAULT NULL
);
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。
- BUFFER 接收数据文件中行读的数据缓冲区。
- LEN 从文件中读取的字节数。默认情况为 NULL，NULL 表示读取的字节数为 MAX\_LINESIZE。

**注意事项：**

如果该行不匹配缓冲区，则发生 READ\_ERROR 异常。如果到文件结束了仍没有文本读取，发生 NO\_DATA\_FOUND 异常。如果 file 是以 byte 模式打开的，则产生 INVALID\_OPERATION 异常。

由于行的结束符不被读取，读取空行则返回空字符串。

缓冲区最大大小为 32767 字节，除非 FOPEN 指定了更小的值。如果未指定，默认值为 1024。

12. GET\_RAW

从文件中读取二进制字符串，并将文件指针向前调整读取的字节数。GET\_RAW 函数忽略掉行结束符。

**语法如下：**

```
PROCEDURE GET_RAW(
    FILE          IN          FILE_TYPE,
    BUFFER        OUT         VARBINARY,
    LEN           IN          INTEGER         DEFAULT NULL
);
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。
- BUFFER 接收从文件中读取的数据行的缓冲区。
- LEN 从文件中读取的字节数。默认情况为 NULL，NULL 表示读取的字节数为 MAX\_LINESIZE。

**注意事项：**

如果子程序读取超过文件末尾，那么将产生 NO\_DATA\_FOUND 的异常。程序在执行循环时应该允许捕获这个异常。

13. IS\_OPEN

判断文件句柄指定的文件是否已打开，如果已打开则返回 1，否则返回 0。不保证用户在尝试使用该文件句柄时没有操作系统的权限。

**语法如下：**

```
FUNCTION  IS_OPEN(
    FILE         IN         FILE_TYPE
)RETURN BOOLEAN;
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。
14. NEW\_LINE

在当前位置输出一个或多个行终止符。

**语法如下：**

```
PROCEDURE NEW_LINE(
    FILE          IN         FILE_TYPE,  
    LINES         IN         INTEGER         DEFAULT 1
);
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。
- LINES 写入文件的行终结符数量。

**异常：**

INVALID\_FILEHANDLE

INVALID\_OPERATION

WRITE\_ERROR

15. PUT

把缓冲区中的文本字符写入到数据文件。文件必须是以写模式打开的。UTL\_FILE.PUT 输出数据时不会附加行终止符。使用 NEW\_LINE 来添加行结束符或者使用 PUT\_LINE 来写一行带有结束符的数据。

**语法如下：**

```
PROCEDURE PUT(
    FILE          IN         FILE_TYPE,   
    BUFFER        IN         VARCHAR
);
```

**参数详解**

- FILE 通过 FOPEN 调用，返回的活动文件句柄。
- BUFFER 包含要写入文件的数据缓存。

**注意事项：**

如果 FOPEN 没有指定一个更小的值，BUFFER 参数的最大值将是 32767。如果未指定，FOPEN 默认的行最大值为 1024。连续调用 PUT 的总和在没有缓冲区刷页的情况下不能超过 32767。

**异常：**

INVALID\_FILEHANDLE

INVALID\_OPERATION

WRITE\_ERROR

16. PUT\_LINE

把缓冲区中的文本字符串写入数据文件，同时输出一个与系统有关的行终止符。

**语法如下：**

```
PROCEDURE PUT_LINE(
    FILE          IN         FILE_TYPE,  
    BUFFER        IN         VARCHAR,  
    AUTOFLUSH     IN         BOOLEAN         DEFAULT FALSE
);
```

**参数详解**

- FILE 由 FOPEN 返回的文件句柄。
- BUFFER 包含要写入文件的数据缓存。
- AUTOFLUSH 数据写完后，自动清理缓冲区。

**注意事项：**

缓区大小最大为 32767。

如果文件有 BYTE 模式打开，则产生 INVALID\_OPERATION 异常。

**异常：**

INVALID\_FILEHANDLE

INVALID\_OPERATION

WRITE\_ERROR

17. PUT\_RAW

接收输入的原始数据并将其写入缓存。

**语法如下：**

```
PROCEDURE PUT_RAW(
    FILE          IN         FILE_TYPE,  
    BUFFER        IN         VARBINARY,   
    AUTOFLUSH     IN         BOOLEAN  DEFAULT FALSE
);
```

**参数详解**

- FILE 由 FOPEN 返回的文件句柄。
- BUFFER 包含要写入文件的数据缓存；
- AUTOFLUSH 数据写完后，自动清理缓冲区。

**注意事项：**

通过设置第三个参数可以使缓冲区自动冲刷。

BUFFER 最大值为 32767。

18. PUTF

以一个模版样式输出至多 5 个字符串，类似 C 语言中的 printf()。

**语法如下：**

```
PROCEDURE PUTF(
    FILE         IN         FILE_TYPE,  
    FORMAT       IN         VARCHAR,  
    ARG1         IN         VARCHAR         DEFAULT NULL,
    ARG2         IN         VARCHAR         DEFAULT NULL,
    ARG3         IN         VARCHAR         DEFAULT NULL,
    ARG4         IN         VARCHAR         DEFAULT NULL,
    ARG5         IN         VARCHAR         DEFAULT NULL
);
```

**参数详解**

- FILE 由 FOPEN 返回的文件句柄。
- FORMAT 决定格式的格式串。格式串可使用以下样式：
	1）%s 格式符。在格式串中最多可以识别 5 个格式符 %s，且格式符 %s 会被后面的参数依次填充，如果此时没有足够的参数，没有对应参数的 %s 会被忽视，不被写入文件；当格式符 %s 超过 5 个时，超出 5 个的部分不会被视为格式符，而会被识别为字符串"%s"直接写入文件（对于其余不是 %s 或\\n 的格式符也会直接作为字符串写入文件）；
	2）\\n 换行符。在格式串中没有个数限制。
- ARGn 可选的 5 个参数，最多 5 个（n 为参数编号）。

**注意事项：**

如果文件以 byte 模式打开，返回 INVALID\_OPERATION 错误。

%s，\\n 与 c 语言中的类似。

19. FOPEN\_NCHAR

打开指定 UTF8 格式文件并返回一个文件句柄。FOPEN\_NCHAR 不支持访问数据库内建文件，例如 DMARCH.INI。

**语法如下：**

```
FUNCTION FOPEN_NCHAR (
    LOCATION        IN         VARCHAR(128),
    FILENAME         IN         VARCHAR(128),
    OPEN_MODE        IN         VARCHAR(128),
    MAX_LINESIZE     IN         INTEGER         DEFAULT 1024
);
```

**参数详解**

- LOCATION 源文件所在的目录对象名。
- FILENAME 文件名称。若参数中包含路径，则直接忽略路径，只获取最后的文件名称。在 UNIX 系统中，文件名不能包含转义符：“/”。 LOCATION 与 FILENAME 拼成的路径串总长度不能超过 256。
- OPEN\_MODE 文件打开模式。包括：R 只读模式；W 写模式；A 附加模式；RB 只读打开一个二进制文件，只允许读；WB 只写打开或建立一个二进制文件，只允许写数据；AB 追加打开一个二进制文件，并在文件末尾写数据。当以“A”或“AB”的方式打开文件时，若该文件不存在，则以“W”的方式创建该文件。
- MAX\_LINESIZE 文件每行最大的字符数，包括换行符。取值范围为 1~32767，缺省为 1024。

**注意事项：**

目录对象名和文件名必须加上引号；对文件的访问和操作需要满足目录对象的权限控制要求；FOPEN\_NCHAR 以 UTF8 格式打开文件，读写需调用带 NCHAR 的读写过程。

20. GET\_LINE\_NCHAR

读取指定的 UTF8 格式文件中的一行到指定的缓存。读取的文本不包括该行的终结符，当读取到文件的末尾，或者到指定的长度时结束读取，并且不能超过 FOPEN\_NCHAR 时指定的 MAX\_LINESIZE。

**语法如下：**

```
PROCEDURE GET_LINE_NCHAR (
    FILE            IN          FILE_TYPE,
    BUFFER          OUT         VARCHAR,
    LEN             IN          INTEGER         DEFAULT NULL
);
```

**参数详解**

- FILE 通过 FOPEN\_NCHAR 调用，返回的活动文件句柄。
- BUFFER 接收数据文件中行读的数据缓冲区。
- LEN 从文件中读取的字节数。默认情况为 NULL，NULL 表示读取的字节数为 MAX\_LINESIZE。

**注意事项：**

如果该行不匹配缓冲区，则发生 READ\_ERROR 异常。如果到文件结束了仍没有读取文本，则发生 NO\_DATA\_FOUND 异常。如果 FILE 是以 BYTE 模式打开的，则发生 INVALID\_OPERATION 异常。

由于行的结束符不被读取，读取空行则返回空字符串。

缓冲区最大大小为 32767 字节，除非 FOPEN\_NCHAR 指定了更小的值。如果未指定，缺省值为 1024。

21. PUT\_NCHAR

把缓冲区中的文本字符以 UTF8 格式写入到数据文件。文件必须是以写模式打开的。UTL\_FILE.PUT\_NCHAR 输出数据时不会附加行终止符。可以使用 NEW\_LINE 来添加行结束符或者使用 PUT\_LINE\_NCHAR 来写一行带有结束符的数据。

**语法如下：**

```
PROCEDURE PUT_NCHAR (
    FILE          IN         FILE_TYPE,  
    BUFFER        IN         VARCHAR
);
```

**参数详解**

- FILE 通过 FOPEN\_NCHAR 调用，返回的活动文件句柄。
- BUFFER 包含要写入文件的数据缓存。

**注意事项：**

如果 FOPEN\_NCHAR 中没有指定一个更小的值，BUFFER 参数的最大值将是 32767；如果 FOPEN\_NCHAR 中未指定 FOPEN\_NCHAR，默认的行最大值为 1024。连续调用 PUT\_NCHAR 的总和在没有缓冲区刷页的情况下不能超过 32767。

**异常：**

INVALID\_FILEHANDLE

INVALID\_OPERATION

WRITE\_ERROR

22. PUT\_LINE\_NCHAR

把缓冲区中的文本字符串以 UTF8 格式写入数据文件，同时输出一个与系统有关的行终止符。

**语法如下：**

```
PROCEDURE PUT_LINE_NCHAR (
    FILE          IN         FILE_TYPE,  
    BUFFER        IN         VARCHAR,   
    AUTOFLUSH     IN         BOOLEAN         DEFAULT FALSE
);
```

**参数详解**

- FILE 由 FOPEN\_NCHAR 返回的文件句柄。
- BUFFER 包含要写入文件的数据缓存。
- AUTOFLUSH 数据写完后，是否自动清理缓冲区。缺省为 false。

**注意事项：**

缓区大小最大为 32767。

如果文件以 BYTE 模式打开，则产生 INVALID\_OPERATION 异常。

**异常：**

INVALID\_FILEHANDLE

INVALID\_OPERATION

WRITE\_ERROR

23. PUTF\_NCHAR

以一个模版样式并用 UTF8 格式输出至多 5 个字符串，类似 C 语言中的 PRINTF()。

**语法如下：**

```
PROCEDURE PUTF_NCHAR (
    FILE         IN         FILE_TYPE,  
    FORMAT       IN         VARCHAR,   
    ARG1         IN         VARCHAR         DEFAULT NULL,
    ARG2         IN         VARCHAR         DEFAULT NULL,
    ARG3         IN         VARCHAR         DEFAULT NULL,
    ARG4         IN         VARCHAR         DEFAULT NULL,
    ARG5         IN         VARCHAR         DEFAULT NULL
);
```

**参数详解**

- FILE 由 FOPEN\_NCHAR 返回的文件句柄。
- FORMAT 决定格式的格式串。格式串可使用以下样式：
	1）%s 格式符。在格式串中最多可以识别 5 个格式符 %s，且格式符 %s 会被后面的参数依次填充，如果此时没有足够的参数，没有对应参数的 %s 会被忽视，不被写入文件；当格式符 %s 超过 5 个时，超出 5 个的部分不会被视为格式符，而会被识别为字符串"%s"直接写入文件（对于其余不是 %s 或\\n 的格式符也会直接作为字符串写入文件）；
	2）\\n 换行符。在格式串中没有个数限制。

**注意事项：**

如果文件以 BYTE 模式打开，返回 INVALID\_OPERATION 错误。

%s，\\n 与 C 语言中的类似。

## 24.3 错误处理

错误、异常情况释义：

1. invalid\_patH：无效路径名
2. invalid\_mode：无效文件模式名
3. invalid\_filehandle：无效文件处理
4. write\_error：写入错误
5. file\_open：打开文件失败
6. charsetmismatch：字符集不匹配
7. invalid\_offset：无效偏移
8. read\_error：读文件失败
9. internal\_error：内部错误
10. invalid\_filename：无效文件名
11. access\_denied：拒绝访问
12. rename\_failed：重命名失败
13. delete\_failed：删除失败

## 24.4 举例说明

首先在路径 e:\\utl\_file\_temp 下创建文件 u12345.tmp。文件的内容为：

```
THIS IS LINE 1.
THIS IS LINE 2.
THIS IS LINE 3.
THIS IS LINE 4.
THIS IS LINE 5.
```

登录 SYSDBA 用户，使用包内的过程和函数之前，如果还未创建过系统包，请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'UTL_FILE');
```

创建用户 USER01，创建目录对象 DIR01，该目录对应的文件路径为 e:\\utl\_file\_temp，并将该目录对象的读写权限授予用户 USER01。另外还要将创建存储过程的权限授予用户 USER01，该权限在示例 3 中将会用到。

```
CREATE USER USER01 IDENTIFIED BY "USER01_psd";
CREATE DIRECTORY DIR01 AS 'E:\UTL_FILE_TEMP';
GRANT READ ON DIRECTORY DIR01 TO USER01;
GRANT WRITE ON DIRECTORY DIR01 TO USER01;
GRANT CREATE PROCEDURE TO USER01;
```

登录用户 USER01，首先执行下述语句，然后即可执行下面 3 个示例。

```
SET SERVEROUTPUT ON; --PRINT需要设置这条语句，才能打印出消息
```

例 1 使用 GET\_LINE 过程读文件

```
DECLARE
    V1 VARCHAR2(8186);
    F1 UTL_FILE.FILE_TYPE;
BEGIN
//本例子中 MAX_LINESIZE小于 GET_LINE的长度要求，所以返回的字节数小于等于256
 F1 :=UTL_FILE.FOPEN('DIR01','u12345.tmp','R',256);
  UTL_FILE.GET_LINE(F1,V1,32767);
  print 'get_line:'||v1;
  UTL_FILE.FCLOSE(F1);
//FOPEN的MAX_LINESIZE 是NULL ，NULL即为默认的1024，所以返回的字节数小于等于1024
  F1 UTL_FILE.FOPEN('DIR01','u12345.tmp','R');   
  UTL_FILE.GET_LINE(F1,V1,32767);
  print 'get_line:'||v1;
  UTL_FILE.FCLOSE(F1);
  
 //GET_LINE 未指定字节数, 所以默认为 NULL1024，NULL即为1024
  F1 :=   UTL_FILE.FOPEN('DIR01','u12345.tmp','R');
  UTL_FILE.GET_LINE(F1,V1);
  print 'get_line:'||v1;
  UTL_FILE.FCLOSE(F1);
END;
/
```

每个过程都是输出第一行，这个例子的结果如下所示:

```
GET LINE: THIS IS LINE 1.
GET LINE: THIS IS LINE 1.
GET LINE: THIS IS LINE 1.
```

例 2 使用 PUTF 过程向文件尾部添加内容。

```
DECLARE
    HANDLE UTL_FILE.FILE_TYPE;
    MY_WORLD VARCHAR2(4) := 'ZORK';
BEGIN
    HANDLE :=UTL_FILE.FOPEN('DIR01','u12345.tmp','A');
    UTL_FILE.PUTF(HANDLE,'\nHELLO, WORLD!\nI COME FROM %s WITH %s.\n',MY_WORLD,'GREETINGS FOR ALL EARTHLINGS');
    UTL_FILE.FFLUSH(HANDLE);
    UTL_FILE.FCLOSE(HANDLE);
END;
/
```

该例子在 u12345.tmp 文件的末尾添加了如下内容：

```
HELLO, WORLD!
I COME FROM ZORK WITH GREETINGS FOR ALL EARTHLINGS.
```

例 3 使用 GET\_RAW 过程从 DIR01 目录下的 u12345.tmp 文件中读取原始信息。

首先，将 u12345.tmp 文件中的内容写为：HELLO WORLD!

```
DECLARE
   HANDLE UTL_FILE.FILE_TYPE;
BEGIN
   HANDLE := UTL_FILE.FOPEN('DIR01','u12345.tmp','W');
   UTL_FILE.PUT(HANDLE,'HELLO WORLD!');
   UTL_FILE.FFLUSH(HANDLE);
   UTL_FILE.FCLOSE(HANDLE);
END;
/
```

然后创建一个存储过程，使用 GET\_RAW 读取 u12345.tmp 文件中的原始信息。

```
CREATE OR REPLACE PROCEDURE GETRAW(N IN VARCHAR2) IS
    H     UTL_FILE.FILE_TYPE;
    BUF   BLOB;
    AMNT  CONSTANT BINARY_INTEGER := 32767;
BEGIN
    H := UTL_FILE.FOPEN('DIR01', N, 'R', 32767);
    UTL_FILE.GET_RAW(H, BUF, AMNT);
    PRINT 'THIS IS THE RAW DATA:';
    SELECT BUF;
    UTL_FILE.FCLOSE (H);
END;
/
```

过程建好后，运行如下语句：

```
begin
    getraw('u12345.tmp');
end;
/
```

输出结果为：

```
THIS IS THE RAW DATA:

行号     BUF   
---------- --------------------------
1          0X48454C4C4F20574F524C4421
```