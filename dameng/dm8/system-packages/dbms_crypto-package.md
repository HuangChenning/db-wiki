---
title: "DBMS_CRYPTO 包"
book: "DM8 系统包使用手册"
version: "DM8"
source: https://eco.dameng.com/document/dm/zh-cn/pm/dbms_crypto-package.html
tags:
  - dameng
  - dm8
  - system-packages
---

DBMS\_CRYPTO 包提供加密和解密数据的接口，支持几种工业标准的分组加密、流加密算法和散列算法。分组加密算法包括 Advanced Encryption Standard(AES)、Data Encryption Standard(DES)；流加密算法包括 RC4；散列算法包括 MD5、SHA-1、SHA-256、SHA-384、SHA-512。

## 39.1 相关方法

DBMS\_CRYPTO 包中包含的过程和函数如下详细介绍：

1. HASH

对 VARBINARY、BLOB、CLOB 数据进行散列。

**语法如下：**

```
FUNCTION HASH(
    SRC               IN        VARBINARY/BLOB/CLOB,
    TYPE            IN        INT
) RETURN VARBINARY;
```

**参数详解**

- SRC 输入参数，需要散列的数据。数据类型可以为 VARBINARY、BLOB 或 CLOB。如果 SRC 为空，则返回值和输出参数均为空。
- TYPE 输入参数，使用的算法，可选值 HASH\_MD5、HASH\_SH1、HASH\_SH256、HASH\_SH384、HASH\_SH512。HASH\_MD5 表示 MD5 信息摘要算法，HASH\_SH1 表示安全散列算法 1（SHA-1），HASH\_SH256 表示安全散列算法 2（SHA-256），HASH\_SH384 表示安全散列算法 2（SHA-384），HASH\_SH512 表示安全散列算法 2（SHA-512）。

**返回值**

散列后的 varbinary 数据。

2. ENCRYPT

对 VARBINARY 数据进行加密。

**语法如下：**

```
FUNCTION EnCRYPT(
    SRC       IN   varbinary,
    TYP       IN   PLS_INTEGER,
    KEY       IN   varbinary,
    IV        IN   varbinary DEFAULT NULL
) RETURN varbinary;
```

**参数详解**

- SRC 输入参数，需要加密的数据。如果 SRC 为空，则返回值和输出参数均为空。
- TYP 输入参数，使用的算法，不能为空。支持分组加密算法和流加密算法。
	1）使用分组加密算法时必须同时指定加密算法、工作模式、填充模式。书写规则为：加密算法 + 工作模式 + 填充模式。

分组加密算法：ENCRYPT\_DES、ENCRYPT\_3DES、ENCRYPT\_3DES\_2KEY、ENCRYPT\_AES128、ENCRYPT\_AES192、ENCRYPT\_AES256。

分组加密算法的工作模式：CHAIN\_ECB、CHAIN\_CBC、CHAIN\_CFB、CHAIN\_OFB。

分组加密算法的填充模式：填充 PAD\_PKCS5、不填充 PAD\_NONE。是否填充由算法决定。以\_NOPAD 结尾的非填充算法名须选 PAD\_NONE 模式，其余填充算法均选 PAD\_PKCS5 模式。

2）使用流加密算法，仅指定算法名即可。流加密算法：ENCRYPT\_RC4。

- KEY 输入参数，加密使用的 KEY，不能为空。KEY 长度必须足够，大于等于算法所需密钥长度，超出长度部分忽略，长度不足将会报错处理。算法的 KEY 值可通过 V$CIPHERS 视图 KH\_SIZE 列获取。需要注意的是，对于 ENCRYPT\_RC4 算法而言，由于其是流式加密算法，密钥长度可变，不存在长度不足的情况，故其 KH\_SIZE 作为默认值，仅供参考。
- IV 输入参数，加密使用的初始向量，缺省为空。IV 值的大小为所使用加密算法的分组大小，可通过 V$CIPHERS 视图 BLOCK\_SIZE 列获取。IV 长度不足时，将报错处理；IV 长度大于等于 BLOCK\_SIZE 时，均取值 BLOCK\_SIZE。工作模式为 CHAIN\_ECB 的加密算法不会用到 IV 参数，因此不对 IV 参数值进行校验。

**返回值**

加密后的 VARBINARY 数据

3. ENCRYPT

对 BLOB、CLOB 数据进行加密。

**语法如下：**

```
PROCEDURE ENCRYPT(
    DST             IN OUT NOCOPY     BLOB,
    SRC             IN                 BLOB/CLOB,
    TYP             IN                 PLS_INTEGER,
    KEY             IN                 VARBINARY,
    IV                 IN                 VARBINARY DEFAULT NULL
);
```

**参数详解**

- DST 输入输出参数，加密后的数据。
- SRC 输入参数，需要加密的数据。如果 SRC 为空，则返回值和输出参数均为空。
- TYP 输入参数，使用的算法，不能为空。用法和 ENCRYPT 方法的 TYP 一样。
- EKY 输入参数，加密使用的 KEY，不能为空。用法和 ENCRYPT 方法的 KEY 一样。
- IV 输入参数，加密使用的 IV，默认为空。用法和 ENCRYPT 方法的 IV 一样。

**返回值**

无

4. DECRYPT

对 VARBINARY 数据进行解密。

**语法如下：**

```
FUNCTION DECRYPT(
    SRC             IN         VARBINARY,
    TYP             IN         PLS_INTEGER,
    KEY             IN         VARBINARY,
    IV                 IN         VARBINARY DEFAULT NULL
) RETURN VARBINARY;
```

**参数详解**

- SRC 输入参数，需要解密的数据。如果 SRC 为空，则返回值和输出参数均为空。
- TYP 输入参数，使用算法，不能为空。
- KEY 输入参数，解密使用的 KEY，不能为空。
- IV 输入参数，解密使用的 IV，默认为空。

**返回值**

解密后的 VARBINARY 数据。

5. DECRYPT

对 BLOB、CLOB 数据进行解密。

**语法如下：**

```
PROCEDURE DECRYPT(
    DST             IN OUT NOCOPY     BLOB/CLOB,
    SRC             IN                 BLOB/CLOB,
    TYP             IN                 PLS_INTEGER,
    KEY             IN                 VARBINARY,
    IV                 IN                 VARBINARY DEFAULT NULL
);
```

**参数详解**

- DST 输入输出参数，解密后的数据。和 SRC 输入参数的类型保持一致。
- SRC 输入参数，需要解密的数据。如果 SRC 为空，则返回值和输出参数均为空。
- TYP 输入参数，使用算法，不能为空。
- KEY 输入参数，解密使用的 KEY，不能为空。
- IV 输入参数，解密使用的 IV，默认为空。

**返回值**

无

## 39.2 使用说明

使用 DBMS\_CRYPTO 包时，指定的加密算法须存在于数据库中。可以通过查询系统视图 V$CIPHERS 获得。例如：算法名、KEY、工作模式、填充模式、分组长度等。

## 39.3 举例说明

使用包内的过程和函数之前，如果还未创建过系统包。请先调用系统过程创建系统包。

```
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_CRYPTO');
SP_CREATE_SYSTEM_PACKAGES (1,'DBMS_OUTPUT');
SP_CREATE_SYSTEM_PACKAGES(1,'UTL_I18N');
SET SERVEROUTPUT ON;  //DBMS_OUTPUT.PUT_LINE需要设置这条语句，才能打印出消息
```

例 1 分别使用 MD5 散列算法、SHA-1 算法对 VARBINARY 类型数据进行散列。

```
DECLARE 
    RAW_INPUT VARBINARY(128) := '74696765727469676572746967657274'; 
    MD5_RAW VARBINARY(2048); 
    SHA1_RAW VARBINARY(2048);  
BEGIN 
    DBMS_OUTPUT.PUT_LINE('> ========= BEGIN TEST RAW DATA ========='); 
    DBMS_OUTPUT.PUT_LINE('> RAW INPUT       : ' ||            RAW_INPUT); 
    MD5_RAW := DBMS_CRYPTO.HASH(RAW_INPUT, DBMS_CRYPTO.HASH_MD5); 
    DBMS_OUTPUT.PUT_LINE('> MD5 HASH       : ' ||              MD5_RAW); 
    SHA1_RAW := DBMS_CRYPTO.HASH(RAW_INPUT, DBMS_CRYPTO.HASH_SH1); 
    DBMS_OUTPUT.PUT_LINE('> SHA1 HASH         : ' ||             SHA1_RAW);   
END; 
/
```

结果如下：

```
> ========= BEGIN TEST RAW DATA =========
> RAW INPUT                     : 74696765727469676572746967657274
> MD5 HASH                      : 831F2AA79221A0F8F330E43A76B53323
> SHA1 HASH                     : 7E48985200C8255A8F7BFF840F9D1F2397A6C65A
```

例 2 使用 DES+ECB+PKCS5 算法对 VARBINARY 类型数据进行加解密。

```
CREATE OR REPLACE FUNCTION ENCRYPT_FUNCTION (V_STR VARCHAR2, V_KEY VARCHAR2)
    RETURN VARCHAR2 
AS 
    V_KEY_RAW      RAW (24);
    V_STR_RAW      RAW (2000);
    V_RETURN_STR   VARCHAR2 (2000);
    V_TYPE         PLS_INTEGER;
BEGIN 
    V_KEY_RAW := UTL_I18N.STRING_TO_RAW (V_KEY, 'GBK');
    V_STR_RAW := UTL_I18N.STRING_TO_RAW (V_STR, 'GBK');
    V_TYPE := 
          DBMS_CRYPTO.ENCRYPT_DES
        + DBMS_CRYPTO.CHAIN_ECB
        + DBMS_CRYPTO.PAD_PKCS5;
    V_STR_RAW := 
        DBMS_CRYPTO.ENCRYPT (SRC => V_STR_RAW, TYP => V_TYPE, KEY => V_KEY_RAW);
    V_RETURN_STR := RAWTOHEX (V_STR_RAW);
    RETURN V_RETURN_STR; 
END;
/

CREATE OR REPLACE FUNCTION DECRYPT_FUNCTION (V_STR VARCHAR2, V_KEY VARCHAR2)
    RETURN VARCHAR2
AS
    V_KEY_RAW      RAW (24);
    V_STR_RAW      RAW (2000);
    V_RETURN_STR   VARCHAR2 (2000);
    V_TYPE         PLS_INTEGER;
BEGIN
    V_KEY_RAW := UTL_I18N.STRING_TO_RAW (V_KEY, 'GBK');
    V_STR_RAW := HEXTORAW (V_STR);
    V_TYPE :=
          DBMS_CRYPTO.ENCRYPT_DES
        + DBMS_CRYPTO.CHAIN_ECB
        + DBMS_CRYPTO.PAD_PKCS5;
    V_STR_RAW :=
        DBMS_CRYPTO.DECRYPT (SRC => V_STR_RAW, TYP => V_TYPE, KEY => V_KEY_RAW);
    V_RETURN_STR := UTL_I18N.RAW_TO_CHAR (V_STR_RAW, 'GBK');
    RETURN V_RETURN_STR;
END;
/

CREATE TABLE C1
(
    A        VARCHAR2 (2000),
    SNAME    VARCHAR2 (10),
    B        INT,
    C        INT NULL,
    D        INT
);
INSERT INTO C1 (A,
                SNAME,
                B,
                C,
                D)
     VALUES (ENCRYPT_FUNCTION ('加密数据列1', 'ASDASD_123456789'),
             'A',
             102,
             104,
             1);
SELECT DECRYPT_FUNCTION(A, 'ASDASD_123456789') FROM C1;
```

结果如下：

```
SELECT DECRYPT_FUNCTION(A, 'ASDASD_123456789') FROM C1;

行号       DECRYPT_FUNCTION(A,'ASDASD_123456789')
---------- --------------------------------------
1          加密数据列1
```

例 3 使用 DES+ECB+PKCS5 算法对 CLOB 类型数据进行加解密。

```
--创建存储过程COMPUTEXORHASH，用于将KEY转换为固定16字节长度的KEY
CREATE OR REPLACE PROCEDURE COMPUTEXORHASH(
    INPUT_STR  IN   VARCHAR2,
    RESULT  IN OUT  BINARY(16)
)
AS
I INT DEFAULT 1;
LEN INT;
POS INT;
CHAR_CODE BYTE;
CURR_BYTE BYTE;
NEW_BYTE BYTE;
BEGIN
    LEN := LENGTH(INPUT_STR);
    RESULT := 0X00000000000000000000000000000000;
    WHILE I <= LEN LOOP
        CHAR_CODE := ASCII(SUBSTRING(INPUT_STR, I));
        POS := ((I - 1) % 16) * 2 + 1;
        CURR_BYTE := UNHEX(SUBSTRING(RESULT, POS, 2));
        NEW_BYTE := CURR_BYTE ^ CHAR_CODE;
        RESULT := HEXTORAW(CONCAT(SUBSTRING(RESULT, 1, POS - 1),
                                    CHARTOBIN(CHAR(NEW_BYTE)),
                                    SUBSTRING(RESULT, POS + 2)));
        I := I + 1;
    END LOOP;
END;
/

--自定义加密函数，使用DES+ECB+PKCS5算法对CLOB类型数据进行加密
CREATE OR REPLACE FUNCTION ENCRYPT_DM (
V_STR_RAW CLOB,
V_KEY VARCHAR2
)RETURN VARBINARY
AS
V_KEY_RAW VARBINARY;
V_RETURN_STR BLOB;
V_TYPE PLS_INTEGER;
BEGIN
    COMPUTEXORHASH(V_KEY, V_KEY_RAW);
    V_TYPE :=
          DBMS_CRYPTO.ENCRYPT_DES
        + DBMS_CRYPTO.CHAIN_ECB
        + DBMS_CRYPTO.PAD_PKCS5;
    CALL DBMS_CRYPTO.ENCRYPT (DST => V_RETURN_STR,
                                  SRC => V_STR_RAW,
                                  TYP => V_TYPE,
                                  KEY => V_KEY_RAW);
    RETURN V_RETURN_STR;
END;
/

--自定义解密函数，使用DES+ECB+PKCS5算法对CLOB类型数据进行解密
CREATE OR REPLACE FUNCTION DECRYPT_DM (
V_STR_RAW BLOB,
V_KEY VARCHAR2
)RETURN VARCHAR2
AS
V_KEY_RAW VARBINARY;
V_RETURN_STR CLOB;
V_TYPE PLS_INTEGER;
BEGIN
    COMPUTEXORHASH(V_KEY, V_KEY_RAW);
    V_TYPE :=
          DBMS_CRYPTO.ENCRYPT_DES
        + DBMS_CRYPTO.CHAIN_ECB
        + DBMS_CRYPTO.PAD_PKCS5;
    CALL DBMS_CRYPTO.DECRYPT (DST => V_RETURN_STR,
                                   SRC => V_STR_RAW,
                                   TYP => V_TYPE,
                                   KEY => V_KEY_RAW);
    RETURN V_RETURN_STR;
END;
/
```

使用自定义函数 ENCRYPT\_DM 加密数据：

```
SELECT ENCRYPT_DM('加密数据','AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB');

行号     ENCRYPT_DM('加密数据','AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB')
---------- -----------------------------------------------------------------
1          0XE6B158239EB3AA89B21C053F63AEF2B8
```

使用自定义函数 DECRYPT\_DM 解密数据：

```
SELECT DECRYPT_DM(ENCRYPT_DM('加密数据','AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB'), 'AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB');

行号     DECRYPT_DM(ENCRYPT_DM('加密数据','AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB'),'AAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB')
-------------------------------------------------------------------------------
1          加密数据
```