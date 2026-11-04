---
title: DBMS_OBFUSCATION_TOOLKIT
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_obtool.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 96 DBMS\_OBFUSCATION\_TOOLKIT

`DBMS_OBFUSCATION_TOOLKIT` enables an application to encrypt data using either the Data Encryption Standard (DES) or the Triple DES algorithms.

Note:

`DBMS_OBFUSCATION_TOOLKIT` is deprecated. `DBMS_CRYPTO` is intended to replace the `DBMS_OBFUSCATION_TOOLKIT`, providing greater ease of use and support for a range of algorithms to accommodate new and existing systems. See [Chapter 39, "DBMS\_CRYPTO"](d_crypto.md) for more information.

This chapter contains the following topics:

- Using DBMS\_OBFUSCATION\_TOOLKIT
	- Overview
		- Security Model
		- Operational Notes
- Summary of DBMS\_OBFUSCATION Subprograms

---

## Using DBMS\_OBFUSCATION\_TOOLKIT

---

### Overview

The Data Encryption Standard (DES), also known as the Data Encryption Algorithm (DEA) by the American National Standards Institute (ANSI) and DEA-1 by the International Standards Organization (ISO), has been a worldwide encryption standard for over 20 years. The banking industry has also adopted DES-based standards for transactions between private financial institutions, and between financial institutions and private individuals. DES will eventually be replaced by a new Advanced Encryption Standard (AES).

DES is a symmetric key cipher; that is, the same key is used to encrypt data as well as decrypt data. DES encrypts data in 64-bit blocks using a 56-bit key. The DES algorithm ignores 8 bits of the 64-bit key that is supplied; however, you must supply a 64-bit key to the algorithm.

Triple DES (3DES) is a far stronger cipher than DES; the resulting ciphertext (encrypted data) is much harder to break using an exhaustive search: 2\*\*112 or 2\*\*168 attempts instead of 2\*\*56 attempts. Triple DES is also not as vulnerable to certain types of cryptanalysis as is DES.

---

### Security Model

Oracle installs this package in the `SYS` schema. You can then grant package access to existing users and roles as needed. The package also grants access to the `PUBLIC` role so no explicit grant needs to be done.

---

### Operational Notes

Note:

MD5 calls do not work in the Oracle 11g Release 2 (11.2.0.4).
- Key Management
- Storing the Key in the Database
- Storing the Key in the Operating System
- User-Supplied Keys

#### Key Management

Key management, including both generation and secure storage of cryptographic keys, is one of the most important aspects of encryption. If keys are poorly chosen or stored improperly, then it is far easier for a malefactor to break the encryption. Rather than using an exhaustive key search attack (that is, cycling through all the possible keys in hopes of finding the correct decryption key), cryptanalysts typically seek weaknesses in the choice of keys, or the way in which keys are stored.

Key generation is an important aspect of encryption. Typically, keys are generated automatically through a random-number generator. Provided that the random number generation is cryptographically secure, this can be an acceptable form of key generation. However, if random numbers are not cryptographically secure, but have elements of predictability, the security of the encryption may be easily compromised.

The `DBMS_OBFUSCATION_TOOLKIT` package includes tools for generating random material that can be used for encryption keys, but it does not provide a mechanism for maintaining them. Care must be taken by the application developer to ensure the secure generation and storage of encryption keys used with this package. Furthermore, the encryption and decryption done by the `DBMS_OBFUSCATION_TOOLKIT` takes place on the server, not the client. If the key is passed over the connection between the client and the server, the connection must be protected by using network encryption. Otherwise, the key is vulnerable to capture over the wire. See [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for information about configuring and using network encryption for Oracle Net.

Key storage is one of the most important, yet difficult aspects of encryption and one of the hardest to manage properly. To recover data encrypted with a symmetric key, the key must be accessible to the application or user seeking to decrypt data. The key needs to be easy enough to retrieve that users can access encrypted data when they need to without significant performance degradation. The key also needs to be secure enough that it is not easily recoverable by unauthorized users trying to access encrypted data that they are not supposed to see.

The three options available are:

- Store the key in the database
- Store the key in the operating system
- Have the user manage the key

#### Storing the Key in the Database

Storing the keys in the database cannot always provide bullet-proof security if you are trying to protect data against the DBA accessing encrypted data (since an all-privileged DBA can access tables containing encryption keys), but it can provide security against the casual snooper, or against someone compromising the database files on the operating system. Furthermore, the security you can obtain by storing keys in the database does not have to be bullet-proof in order to be extremely useful.

For example, suppose you want to encrypt an employee's social security number, one of the columns in table EMP. You could encrypt each employee's SSN using a key which is stored in a separate column in EMP. However, anyone with SELECT access on the EMP table could retrieve the encryption key and decrypt the matching social security number. Alternatively, you could store the encryption keys in another table, and use a package to retrieve the correct key for the encrypted data item, based on a primary key-foreign key relationship between the tables.

You can envelope both the `DBMS_OBFUSCATION_TOOLKIT` package and the procedure to retrieve the encryption keys supplied to the package. Furthermore, the encryption key itself could be transformed in some way (for example, XORed with the foreign key to the EMP table) so that the key itself is not stored in easily recoverable form.

Oracle recommends using the wrap utility of PL/SQL to obfuscate the code within a PL/SQL package itself that does the encryption. That prevents people from breaking the encryption by looking at the PL/SQL code that handles keys, calls encrypting routines, and so on. In other words, use the wrap utility to obfuscate the PL/SQL packages themselves. This scheme is secure enough to prevent users with `SELECT` access to `EMP` from reading unencrypted sensitive data, and a DBA from easily retrieving encryption keys and using them to decrypt data in the `EMP` table. It can be made more secure by changing encryption keys regularly, or having a better key storage algorithm (so the keys themselves are encrypted, for example).

#### Storing the Key in the Operating System

Storing keys in a flat file in the operating system is another option. You can make callouts from PL/SQL, which you can use to retrieve encryption keys. If you store keys in a file and make callouts to retrieve the keys, the security of your encrypted data is only as secure as the protection of the key file on the operating system. Of course, a user retrieving keys from the operating system would have to be able to either access the Oracle database files (to decrypt encrypted data), or be able to gain access to the table in which the encrypted data is stored as a legitimate user.

#### User-Supplied Keys

If you ask a user to supply the key, it is crucial that you use network encryption, such as that provided by Oracle Advanced Security, so the key is not passed from client to server in the clear. The user must remember the key, or your data is not recoverable.

---

## Summary of DBMS\_OBFUSCATION Subprograms

Table 96-1 DBMS\_OBFUSCATION Package Subprograms

| Subprogram | Description |
| --- | --- |
| DES3DECRYPT Procedures and Functions | Generates the decrypted form of the input data |
| DES3ENCRYPT Procedures and Functions | Generates the encrypted form of the input data by passing it through the Triple DES encryption algorithm |
| DES3GETKEY Procedures and Functions | Takes a random value and uses it to generate an encryption key, using Triple DES |
| DESDECRYPT Procedures and Functions | Generates the decrypted form of the input data |
| DESENCRYPT Procedures and Functions | Generates the encrypted form of the input data |
| DESGETKEY Procedures and Functions | Takes a random value and uses it to generate an encryption key |
| MD5 Procedures and Functions | Generates MD5 hashes of data |

---

### DES3DECRYPT Procedures and Functions

These subprograms generate the decrypted form of the input data.

For a discussion of the initialization vector that you can use with this procedure, see the section, "DES3ENCRYPT Procedures and Functions".

Syntax

```
DBMS_OBFUSCATION_TOOLKIT.DES3DECRYPT(
   input             IN   RAW,
   key               IN   RAW,
   decrypted_data    OUT  RAW,
   which             IN   PLS_INTEGER  DEFAULT TwoKeyMode
   iv                IN   RAW          DEFAULT NULL);

DBMS_OBFUSCATION_TOOLKIT.DES3DECRYPT(
   input_string      IN   VARCHAR2,
   key_string        IN   VARCHAR2,
   decrypted_string  OUT  VARCHAR2,
   which             IN   PLS_INTEGER  DEFAULT TwoKeyMode
   iv_string         IN   VARCHAR2     DEFAUTL NULL);

DBMS_OBFUSCATION_TOOLKIT.DES3DECRYPT(
   input         IN  RAW,
   key           IN  RAW,
   which         IN  PLS_INTEGER DEFAULT TwoKeyMode
   iv            IN  RAW         DEFAULT NULL)
  RETURN RAW;

DBMS_OBFUSCATION_TOOLKIT.DES3DECRYPT(
   input_string  IN  VARCHAR2,
   key_string    IN  VARCHAR2,
   which         IN  PLS_INTEGER DEFAULT TwoKeyMode
   iv_string     IN  VARCHAR2    DEFAULT NULL) 
  RETURN VARCHAR2;
```

Parameters

Table 96-2 DES3DECRYPT Parameters for Raw Data

| Parameter | Description |
| --- | --- |
| `input` | Data to be decrypted |
| `key` | Decryption key |
| `decrypted_data` | Decrypted data |
| `which` | If = 0, (default), then TwoKeyMode is used. If = 1, then ThreeKeyMode is used. |
| `iv` | Initialization vector |
| `input_string` | String to be decrypted |
| `key_string` | Decryption key string |
| `decrypted_string` | Decrypted string |
| `iv_string` | Initialization vector |

Usage Notes

If the input data or key given to the `DES3DECRYPT` procedure is empty, then the procedure raises the error `ORA-28231 "Invalid input to Obfuscation toolkit."`

If the input data given to the `DES3DECRYPT` procedure is not a multiple of 8 bytes, the procedure raises the error `ORA-28232 "Invalid input size for Obfuscation toolkit."` `ORA-28233` is NOT applicable for the `DES3DECRYPT` function.

If the key length is missing or is less than 8 bytes, then the procedure raises the error `ORA-28234 "Key length too short."` Note that if larger keys are used, extra bytes are ignored. So a 9-byte key will not generate an exception.

If an incorrect value is specified for the `WHICH` parameter, `ORA-28236 "Invalid Triple DES mode"` is generated. Only the values 0 (`TwoKeyMode`) and 1 (`ThreeKeyMode`) are valid.

Restrictions

You must supply a single key of either 128 bits for a 2-key implementation (of which only 112 are used), or a single key of 192 bits for a 3-key implementation (of which 168 bits are used). Oracle automatically truncates the supplied key into 56-bit lengths for decryption. This key length is fixed and cannot be altered.

Note:

Both the key length limitation and the prevention of multiple encryption passes are requirements of U.S. regulations governing the export of cryptographic products.

---

### DES3ENCRYPT Procedures and Functions

These subprograms generate the encrypted form of the input data by passing it through the Triple DES (3DES) encryption algorithm.

Oracle's implementation of 3DES supports either a 2-key or 3-key implementation, in outer cipher-block-chaining (CBC) mode.

Syntax

```
DBMS_OBFUSCATION_TOOLKIT.DES3Encrypt(
   input           IN     RAW,
   key             IN     RAW,
   encrypted_data  OUT    RAW,
   which           IN     PLS_INTEGER  DEFAULT TwoKeyMode
   iv              IN     RAW          DEFAULT NULL);

DBMS_OBFUSCATION_TOOLKIT.DES3Encrypt(
   input_string      IN     VARCHAR2,
   key_string        IN     VARCHAR2,
   encrypted_string  OUT    VARCHAR2,
   which             IN     PLS_INTEGER  DEFAULT TwoKeyMode
   iv_string         IN     VARCHAR2     DEFAULT NULL);

DBMS_OBFUSCATION_TOOLKIT.DES3Encrypt(
   input        IN RAW,
   key          IN RAW,
   which        IN PLS_INTEGER DEFAULT TwoKeyMode
   iv           IN RAW         DEFAULT NULL)
  RETURN RAW;

DBMS_OBFUSCATION_TOOLKIT.DES3Encrypt(
   input_string  IN VARCHAR2,
   key_string    IN VARCHAR2,
   which         IN PLS_INTEGER DEFAULT TwoKeyMode
   iv_string     IN VARCHAR2    DEFAULT NULL)
  RETURN VARCHAR2;
```

Parameters

Table 96-3 DES3ENCRYPT Parameters Procedure and Function

| Parameter | Description |
| --- | --- |
| `input` | Data to be encrypted. |
| `key` | Encryption key. |
| `encrypted_data` | Encrypted data. |
| `which` | If = 0, (default), then `TwoKeyMode` is used. If = 1, then `ThreeKeyMode` is used. |
| iv | Initialization vector. |
| `input_string` | String to be encrypted. |
| `key_string` | Encryption key string. |
| `encrypted_string` | Encrypted string. |
| iv\_string | Initialization vector. |

Usage Notes

If you are using Oracle's 3DES interface with a 2-key implementation, you must supply a single key of 128 bits as an argument to the `DES3ENCRYPT` procedure. With a 3-key implementation, you must supply a single key of 192 bits. Oracle then breaks the supplied key into two 64-bit keys. As with DES, the 3DES algorithm throws away 8 bits of each derived key. However, you must supply a single 128-bit key for the 2-key 3DES implementation or a single 192-bit key for the 3-key 3DES implementation; otherwise the package will raise an error. The `DES3ENCRYPT` procedure uses the 2-key implementation by default.

You also have the option of providing an initialization vector (IV) with the `DES3ENCRYPT` procedure. An IV is a block of random data prepended to the data you intend to encrypt. The IV has no meaning. It is there to make each message unique. Prepending an IV to your input data avoids starting encrypted blocks of data with common header information, which may give cryptanalysts information they can use to decrypt your data.

If the input data or key given to the PL/SQL `DES3ENCRYPT` procedure is empty, then the procedure raises the error `ORA-28231 "Invalid input to Obfuscation toolkit."`

If the input data given to the `DES3ENCRYPT` procedure is not a multiple of 8 bytes, the procedure raises the error `ORA-28232 "Invalid input size for Obfuscation toolkit."`

If you try to double encrypt data using the `DES3ENCRYPT` procedure, then the procedure raises the error `ORA-28233 "Double encryption not supported."`

If the key length is missing or is less than 8 bytes, then the procedure raises the error `ORA-28234 "Key length too short."` Note that if larger keys are used, extra bytes are ignored. So a 9-byte key will not generate an exception.

If an incorrect value is specified for the `which` parameter, `ORA-28236 "Invalid Triple DES mode"` is generated. Only the values 0 (`TwoKeyMode`) and 1 (`ThreeKeyMode`) are valid.

Restrictions

The `DES3ENCRYPT` procedure has two restrictions. The first is that the DES key length for encryption is fixed at 128 bits (for 2-key DES) or 192 bits (for 3-key DES); you cannot alter these key lengths.

The second is that you cannot execute multiple passes of encryption using 3DES. (Note: the 3DES algorithm itself encrypts data multiple times; however, you cannot call the `DES3ENCRYPT` function itself more than once to encrypt the same data using 3DES.)

Note:

Both the key length limitation and the prevention of multiple encryption passes are requirements of U.S. regulations governing the export of cryptographic products.

---

### DES3GETKEY Procedures and Functions

These subprograms take a random value and uses it to generate an encryption key. For Triple DES, you specify the mode so that the returned key has the proper length.

Syntax

```
DBMS_OBFUSCATION_TOOLKIT.DES3GetKey(
   which        IN   PLS_INTEGER DEFAULT TwoKeyMode,
   seed         IN   RAW,
   key          OUT  RAW);

DBMS_OBFUSCATION_TOOLKIT.DES3GetKey(
   which        IN   PLS_INTEGER DEFAULT TwoKeyMode,
   seed_string  IN   VARCHAR2,
   key          OUT  VARCHAR2);

DBMS_OBFUSCATION_TOOLKIT.DES3GetKey(
   which  IN  PLS_INTEGER DEFAULT TwoKeyMode,
   seed   IN  RAW)
 RETURN RAW;

DBMS_OBFUSCATION_TOOLKIT.DES3GetKey(
   which        IN  PLS_INTEGER DEFAULT TwoKeyMode,
   seed_string  IN  VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 96-4 DES3GETKEY Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `which` | If = 0, (default), then `TwoKeyMode` is used. If = 1, then `ThreeKeyMode` is used. |
| `seed` | A value at least 80 characters long. |
| `key` | Encryption key. |
| `seed_string` | A value at least 80 characters long. |
| `key` | Encryption key. |

---

### DESDECRYPT Procedures and Functions

These subprograms generate the decrypted form of the input data.

Syntax

```
DBMS_OBFUSCATION_TOOLKIT.DESDecrypt(
   input             IN   RAW,
   key               IN   RAW,
   decrypted_data    OUT  RAW);

DBMS_OBFUSCATION_TOOLKIT.DESDecrypt(
   input_string      IN   VARCHAR2,
   key_string        IN   VARCHAR2,
   decrypted_string  OUT  VARCHAR2);

DBMS_OBFUSCATION_TOOLKIT.DESDecrypt(
   input            IN  RAW,
   key              IN  RAW)
  RETURN RAW;

DBMS_OBFUSCATION_TOOLKIT.DESDecrypt(
   input_string     IN  VARCHAR2,
   key_string       IN  VARCHAR2)
  RETURN VARCHAR2;
```

Parameters

Table 96-5 DESDECRYPT Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `input` | Data to be decrypted. |
| `key` | Decryption key. |
| `decrypted_data` | Decrypted data. |
| `input_string` | String to be decrypted. |
| `key_string` | Decryption key string. |
| `decrypted_string` | Decrypted string. |

Usage Notes

If the input data or key given to the PL/SQL `DESDECRYPT` function is empty, then Oracle raises `ORA error 28231 "Invalid input to Obfuscation toolkit."`

If the input data given to the `DESDECRYPT` function is not a multiple of 8 bytes, Oracle raises `ORA error 28232 "Invalid input size for Obfuscation toolkit."`

If the key length is missing or is less than 8 bytes, then the procedure raises the error `ORA-28234 "Key length too short."` Note that if larger keys are used, extra bytes are ignored. So a 9-byte key will not generate an exception.

Note:

`ORA-28233` is not applicable to the `DESDECRYPT` function.

Restrictions

The DES key length for encryption is fixed at 64 bits (of which 56 bits are used); you cannot alter this key length.

Note:

The key length limitation is a requirement of U.S. regulations governing the export of cryptographic products.

---

### DESENCRYPT Procedures and Functions

These subprograms generate the encrypted form of the input data.

Syntax

```
DBMS_OBFUSCATION_TOOLKIT.DESEncrypt(
   input            IN    RAW,
   key              IN    RAW,
   encrypted_data   OUT   RAW);

DBMS_OBFUSCATION_TOOLKIT.DESEncrypt(
   input_string     IN    VARCHAR2,
   key_string       IN    VARCHAR2,
   encrypted_string OUT   VARCHAR2);

DBMS_OBFUSCATION_TOOLKIT.DESEncrypt(
   input         IN  RAW,
   key           IN  RAW)
  RETURN RAW;

DBMS_OBFUSCATION_TOOLKIT.DESEncrypt(
   input_string  IN  VARCHAR2,
   key_string    IN  VARCHAR2)
  RETURN VARCHAR2;
```

Parameters

Table 96-6 DESENCRYPT Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `input` | Data to be encrypted. |
| `key` | Encryption key. |
| `encrypted_data` | Encrypted data. |
| `input_string` | String to be encrypted. |
| `key_string` | Encryption key string. |
| `encrypted_string` | Encrypted string. |

Usage Notes

The DES algorithm encrypts data in 64-bit blocks using a 56-bit key. The DES algorithm throws away 8 bits of the supplied key (the particular bits which are thrown away is beyond the scope of this documentation). However, when using the algorithm, you must supply a 64-bit key or the package will raise an error.

If the input data or key given to the PL/SQL DESEncrypt procedure is empty, then the procedure raises the error ORA-28231 "Invalid input to Obfuscation toolkit".

If the input data given to the `DESENCRYPT` procedure is not a multiple of 8 bytes, the procedure raises the error `ORA-28232 "Invalid input size for Obfuscation toolkit."`

If you try to double-encrypt data using the `DESENCRYPT` procedure, then the procedure raises the error `ORA-28233 "Double encryption not supported."`

If the key length is missing or is less than 8 bytes, then the procedure raises the error `ORA-28234 "Key length too short."` Note that if larger keys are used, extra bytes are ignored. So a 9-byte key will not generate an exception.

Restrictions

The `DESENCRYPT` procedure has the following restrictions:

- The DES key length for encryption is fixed at 56 bits; you cannot alter this key length.
- You cannot execute multiple passes of encryption. That is, you cannot re-encrypt previously encrypted data by calling the function twice.
	Note:
	Both the key length limitation and the prevention of multiple encryption passes are requirements of U.S. regulations governing the export of cryptographic products.

---

### DESGETKEY Procedures and Functions

These subprograms take a random value and use it to generate an encryption key.

Syntax

```
DBMS_OBFUSCATION_TOOLKIT.DESGetKey(
   seed         IN   RAW,
   key          OUT  RAW);

DBMS_OBFUSCATION_TOOLKIT.DESGetKey(
   seed_string  IN   VARCHAR2,
   key          OUT  VARCHAR2);

DBMS_OBFUSCATION_TOOLKIT.DESGetKey(
   seed IN RAW)
 RETURN RAW;

DBMS_OBFUSCATION_TOOLKIT.DESGetKey(
   seed_string IN VARCHAR2)
 RETURN VARCHAR2;
```

Parameters

Table 96-7 DESGETKEY Procedure and Function Parameters

| Parameter | Description |
| --- | --- |
| `seed` | A value at least 80 characters long. |
| `key` | Encryption key. |
| `seed_string` | A value at least 80 characters long. |
| `key` | Encryption key. |

---

### MD5 Procedures and Functions

These subprograms generate MD5 hashes of data. The MD5 algorithm ensures data integrity by generating a 128-bit cryptographic message digest value from given data.

Syntax

```
DBMS_OBFUSCATION_TOOLKIT.MD5(
   input            IN   RAW,
   checksum         OUT  raw_checksum);

DBMS_OBFUSCATION_TOOLKIT.MD5(
   input_string     IN   VARCHAR2,
   checksum_string  OUT  varchar2_checksum);

DBMS_OBFUSCATION_TOOLKIT.MD5(
   input         IN  RAW)
  RETURN raw_checksum;

DBMS_OBFUSCATION_TOOLKIT.MD5(
   input_string  IN  VARCHAR2)
  RETURN varchar2_checksum;
```

Parameters

Table 96-8 MD5 Procedure and Function Parameters

| Parameter Name | Description |
| --- | --- |
| `input` | Data to be hashed |
| `checksum` | 128-bit cryptographic message digest |
| `input_string` | String to be hashed |
| `checksum_string` | 128-bit cryptographic message digest |