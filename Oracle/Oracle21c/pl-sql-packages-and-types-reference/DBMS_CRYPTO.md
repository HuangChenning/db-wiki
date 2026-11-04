---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_CRYPTO.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 47 DBMS\_CRYPTO

`DBMS_CRYPTO` provides an interface to encrypt and decrypt stored data, and can be used in conjunction with PL/SQL programs running network communications. It provides support for several industry-standard encryption and hashing algorithms, including the Advanced Encryption Standard (AES) encryption algorithm. AES has been approved by the National Institute of Standards and Technology (NIST) to replace the Data Encryption Standard (DES).

Note:

- Starting from Oracle Database 21c Release, the use of `MD5` and `MD4` algorithms are deprecated.
- Starting from Oracle Database 21c Release, the use of `SHA-1` for `SQLNET` and `DBMS_CRYPTO` is deprecated.

Oracle recommends that you do not use deprecated values in new applications. Support for deprecated features is for backward compatibility only.

This chapter contains the following topics:

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG80084) for more information about using this package and about encrypting data in general.
- [What Is Oracle Wallet Manager?](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBIMI-GUID-E3E16C82-E174-4814-98D5-EADF1BCB3C37) for more information on Oracle Wallet Manager.

### 47.1 DBMS\_CRYPTO Overview

`DBMS_CRYPTO` contains basic cryptographic functions and procedures. To use this package correctly and securely, a general level of security expertise is assumed.

The `DBMS_CRYPTO` package enables encryption and decryption for common Oracle datatypes, including `RAW` and large objects (`LOB` s), such as images and sound. Specifically, it supports `BLOB` s and `CLOB` s. In addition, it provides Globalization Support for encrypting data across different database character sets. It also supports asymmetric key functions.

The following cryptographic algorithms are supported:

- Data Encryption Standard (DES), Triple DES (3DES, 2-key and 3-key)
- Advanced Encryption Standard (AES)
- MD5, MD4, SHA-1, and SHA-2 cryptographic hashes
- MD5, SHA-1, and SHA-2 Message Authentication Code (MAC)

Block cipher modifiers are also provided with `DBMS_CRYPTO`. You can choose from several padding options, including PKCS (Public Key Cryptographic Standard) #5, and from four block cipher chaining modes, including Cipher Block Chaining (CBC).

Table 47-1 summarizes the `DBMS_CRYPTO` package features.

Table 47-1 DBMS\_CRYPTO Features

| Package Feature | DBMS\_CRYPTO |
| --- | --- |
| Cryptographic algorithms | DES, 3DES, AES, 3DES\_2KEY |
| Padding forms | PKCS5, zeroes |
| Block cipher chaining modes | CBC, CFB, ECB, OFB |
| Cryptographic hash algorithms | MD5, MD4, SHA-1, SHA-2 (SHA-256, SHA-384, SHA-512) |
| Keyed hash (MAC) algorithms | HMAC\_MD5, HMAC\_SH1, HMAC\_SH256, HMAC\_SH384, HMAC\_SH512 |
| Cryptographic pseudo-random number generator | `RAW`, `NUMBER`, `BINARY_INTEGER` |
| Database types | `RAW`, `CLOB`, `BLOB` |

The `DBMS_CRYPTO` package replaces `DBMS_OBFUSCATION_TOOLKIT`, providing greater ease of use and support for a range of algorithms to accommodate new and existing systems. Specifically, `3DES_2KEY` are provided for backward compatibility. It is not recommended that you use these algorithms because they do not provide the same level of security as provided by 3DES, AES, MD5, SHA-1, or SHA-2.

### 47.2 DBMS\_CRYPTO Security Model

Oracle Database installs this package in the `SYS` schema. You can then grant package access to existing users and roles as needed.

### 47.3 DBMS\_CRYPTO Constants

The `DBMS_CRYPTO` package uses the constants listed and described in this topic.

Table 47-2 DBMS\_CRYPTO Constants

| Name | Type | Value | Description |
| --- | --- | --- | --- |
| `LEGACY_DEFAULT_IV` | `VARCHAR2(16)` | `0123456789ABCDEF` | If you did not provide the `IV` argument when creating a triple-DES ciphertext using the desupported `DBMS_OBFUSCATION_TOOLKIT`, then provide `IV` as `hextoraw(DBMS_CRYPTO.LEGACY_DEFAULT_IV)` when invoking `DBMS_CRYPTO` to decrypt the triple-DES ciphertext.  For example:  ``` plaintext := DBMS_CRYPTO.decrypt     (src => ciphertext_from_legacy_DES3Encrypt     ,typ => DBMS_CRYPTO.DES3_CBC_NONE     ,key => key_information     ,iv  => hextoraw(dbms_crypto.LEGACY_DEFAULT_IV)     ); ``` |
| `DES3_CBC_NONE` | `PLS_INTEGER` | `ENCRYPT_3DES + CHAIN_CBC + PAD_NONE` | If you are using `DBMS_CRYPTO` to decipher a triple-DES ciphertext that you created in the past using the desupported `DBMS_OBFUSCATION_TOOLKIT`, then set the `typ` argument of `DBMS_CRYPTO.decrypt` to the value `DBMS_CRYPTO.DES3_CBC_NONE` to ensure that the PKCS#5 padding is disabled.  For example:  ``` plaintext := DBMS_CRYPTO.decrypt     (src => ciphertext_from_legacy_DES3Encrypt     ,typ => DBMS_CRYPTO.DES3_CBC_NONE     ,key => key_information     ,iv  => hextoraw(DBMS_CRYPTO.LEGACY_DEFAULT_IV)     ); ``` |

### 47.4 DBMS\_CRYPTO Datatypes

Parameters for the `DBMS_CRYPTO` subprograms use these datatypes.

Table 47-3 DBMS\_CRYPTO Datatypes

| Type | Description |
| --- | --- |
| `BLOB` | A source or destination binary LOB |
| `CLOB` | A source or destination character LOB (excluding NCLOB) |
| `PLS_INTEGER` | Specifies a cryptographic algorithm type (used with BLOB, CLOB, and RAW datatypes) |
| `RAW` | A source or destination RAW buffer |

### 47.5 DBMS\_CRYPTO Algorithms

The DBMS\_CRYPTO package contains predefined cryptographic algorithms, modifiers, and cipher suites.

These are shown in the following tables.

Table 47-4 DBMS\_CRYPTO Cryptographic Hash Functions

| Name | Description |
| --- | --- |
| `HASH_MD4` | Produces a 128-bit hash, or message digest of the input message. |
| `HASH_MD5` | Also produces a 128-bit hash, but is more complex than MD4. |
| `HASH_SH1` | Secure Hash Algorithm (SHA-1). Produces a 160-bit hash. |
| `HASH_SH256` | SHA-2, produces a 256-bit hash. |
| `HASH_SH384` | SHA-2, produces a 384-bit hash. |
| `HASH_SH512` | SHA-2, produces a 512-bit hash. |

Table 47-5 DBMS\_CRYPTO MAC (Message Authentication Code) Functions

| Name | Description |
| --- | --- |
| `HMAC_MD5` | Same as MD5 hash function, except it requires a secret key to verify the hash value. |
| `HMAC_SH1` | Same as SHA hash function, except it requires a secret key to verify the hash value.  Complies with IETF RFC 2104 standard. |
| `HMAC_SH256` | Same as SHA-2 256-bit hash function, except it requires a secret key to verify the hash value. |
| `HMAC_SH384` | Same as SHA-2 384-bit hash function, except it requires a secret key to verify the hash value. |
| `HMAC_SH512` | Same as SHA-2 512-bit hash function, except it requires a secret key to verify the hash value. |

Table 47-6 DBMS\_CRYPTO Encryption Algorithms

| Name | Description |
| --- | --- |
| `ENCRYPT_DES` | Data Encryption Standard. Block cipher. Uses key length of 56 bits. |
| `ENCRYPT_3DES_2KEY` | Data Encryption Standard. Block cipher. Operates on a block 3 times with 2 keys. Effective key length of 112 bits. |
| `ENCRYPT_3DES` | Data Encryption Standard. Block cipher. Operates on a block 3 times. |
| `ENCRYPT_AES128` | Advanced Encryption Standard. Block cipher. Uses 128-bit key size. |
| `ENCRYPT_AES192` | Advanced Encryption Standard. Block cipher. Uses 192-bit key size. |
| `ENCRYPT_AES256` | Advanced Encryption Standard. Block cipher. Uses 256-bit key size. |

Table 47-7 DBMS\_CRYPTO Block Cipher Suites

| Name | Description |
| --- | --- |
| `DES_CBC_PKCS5` | ENCRYPT\_DES <sup>Foot 1</sup> + CHAIN\_CBC <sup>Foot 2</sup> + PAD\_PKCS5 <sup>Foot 3</sup> |
| `DES3_CBC_PKCS5` | `ENCRYPT_3DES` <sup>Foot 1</sup> + `CHAIN_CBC` <sup>Foot 2</sup> + PAD\_PKCS5 <sup>Foot 3</sup> |

<sup>Footnote 1</sup>

See Table 47-6

<sup>Footnote 2</sup>

See Table 47-8

<sup>Footnote 3</sup>

See Table 47-9

Table 47-8 DBMS\_CRYPTO Block Cipher Chaining Modifiers

| Name | Description |
| --- | --- |
| `CHAIN_ECB` | Electronic Codebook. Encrypts each plaintext block independently. |
| `CHAIN_CBC` | Cipher Block Chaining. Plaintext is XORed with the previous ciphertext block before it is encrypted. |
| `CHAIN_CFB` | Cipher-Feedback. Enables encrypting units of data smaller than the block size. |
| `CHAIN_OFB` | Output-Feedback. Enables running a block cipher as a synchronous stream cipher. Similar to CFB, except that n bits of the previous output block are moved into the right-most positions of the data queue waiting to be encrypted. |

Table 47-9 DBMS\_CRYPTO Block Cipher Padding Modifiers

| Name | Description |
| --- | --- |
| `PAD_PKCS5` | Provides padding which complies with the PKCS #5: Password-Based Cryptography Standard |
| `PAD_NONE` | Provides option to specify no padding. Caller must ensure that blocksize is correct, else the package returns an error. |
| `PAD_ZERO` | Provides padding consisting of zeroes |

### 47.6 DBMS\_CRYPTO Restrictions

The `VARCHAR2` datatype is not directly supported by `DBMS_CRYPTO`. Before you can perform cryptographic operations on data of the type `VARCHAR2`, you must convert it to the uniform database character set AL32UTF8, and then convert it to the `RAW` datatype. After performing these conversions, you can then encrypt it with the `DBMS_CRYPTO` package.

See Also:

DBMS\_CRYPTO Operational Notes for information about the conversion rules for converting datatypes.

### 47.7 DBMS\_CRYPTO Exceptions

The following table lists exceptions that have been defined for `DBMS_CRYPTO`.

Table 47-10 DBMS\_CRYPTO Exceptions

| Exception | Code | Description |
| --- | --- | --- |
| `CipherSuiteInvalid` | `28827` | The specified cipher suite is not defined. |
| `CipherSuiteNull` | `28829` | No value has been specified for the cipher suite to be used. |
| `KeyNull` | `28239` | The encryption key has not been specified or contains a `NULL` value. |
| `KeyBadSize` | `28234` | DES keys: Specified key size is too short. DES keys must be at least 8 bytes (64 bits).  AES keys: Specified key size is not supported. AES keys must be 128, 192, or 256 bits in length. |
| `DoubleEncryption` | `28233` | Source data was previously encrypted. |

### 47.8 DBMS\_CRYPTO Operational Notes

This section describes several DBMS\_CRYPTO operational notes.

- When to Use Encrypt and Decrypt Procedures or Functions
- When to Use Hash or Message Authentication Code (MAC) Functions
- About Generating and Storing Encryption Keys
- Conversion Rules

When to Use Encrypt and Decrypt Procedures or Functions

This package includes both `ENCRYPT` and `DECRYPT` procedures and functions. The procedures are used to encrypt or decrypt `LOB` datatypes (overloaded for `CLOB` and `BLOB` datatypes). In contrast, the `ENCRYPT` and `DECRYPT` functions are used to encrypt and decrypt `RAW` datatypes. Data of type `VARCHAR2` must be converted to `RAW` before you can use `DBMS_CRYPTO` functions to encrypt it.

When to Use Hash or Message Authentication Code (MAC) Functions

This package includes two different types of one-way hash functions: the `HASH` function and the `MAC` function. Hash functions operate on an arbitrary-length input message, and return a fixed-length hash value. One-way hash functions work in one direction only. It is easy to compute a hash value from an input message, but it is extremely difficult to generate an input message that hashes to a particular value. Note that hash values should be at least 128 bits in length to be considered secure.

You can use hash values to verify whether data has been altered. For example, before storing data, the user runs `DBMS_CRYPTO.HASH` against the stored data to create a hash value. On returning the stored data, the user can again run the hash function against it, using the same algorithm. If the second hash value is identical to the first one, then the data has not been altered. Hash values are similar to "file fingerprints" and are used to ensure data integrity.

The `HASH` function included with `DBMS_CRYPTO`, is a one-way hash function that you can use to generate a hash value from either `RAW` or `LOB` data. The `MAC` function is also a one-way hash function, but with the addition of a secret key. It works the same way as the `DBMS_CRYPTO.HASH` function, except only someone with the key can verify the hash value.

MACs can be used to authenticate files between users. They can also be used by a single user to determine if her files have been altered, perhaps by a virus. A user could compute the MAC of his files and store that value in a table. If the user did not use a MAC function, then the virus could compute the new hash value after infection and replace the table entry. A virus cannot do that with a MAC because the virus does not know the key.

About Generating and Storing Encryption Keys

The `DBMS_CRYPTO` package can generate random material for encryption keys, but it does not provide a mechanism for maintaining them. Application developers must take care to ensure that the encryption keys used with this package are securely generated and stored. Also note that the encryption and decryption operations performed by `DBMS_CRYPTO` occur on the server, not on the client. Consequently, if the key is sent over the connection between the client and the server, the connection must be protected by using network encryption. Otherwise, the key is vulnerable to capture over the wire.

Although `DBMS_CRYPTO` cannot generate keys on its own, it does provide tools you can use to aid in key generation. For example, you can use the `RANDOMBYTES` function to generate random material for keys.

When generating encryption keys for DES, it is important to remember that some numbers are considered weak and semiweak keys. Keys are considered weak or semiweak when the pattern of the algorithm combines with the pattern of the initial key value to produce ciphertext that is more susceptible to cryptanalysis. To avoid this, filter out the known weak DES keys. Lists of the known weak and semiweak DES keys are available on several public Internet sites.

See Also:

- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=DBSEG-GUID-6AD89576-526F-4D6B-A539-ADF4B840819F) for information about configuring network encryption and SSL
- RANDOMBYTES Function

Conversion Rules

- To convert `VARCHAR2` to `RAW`, use the `UTL_I18N.STRING_TO_RAW` function to perform the following steps:
	1. Convert `VARCHAR2` in the current database character set to `VARCHAR2` in the AL32UTF8 database character.
		2. Convert `VARCHAR2` in the AL32UTF8 database character set to `RAW`.
	Syntax example:
	```
	UTL_I18N.STRING_TO_RAW (string, 'AL32UTF8');
	```
- To convert `RAW` to `VARCHAR2`, use the `UTL_I18N.RAW_TO_CHAR` function to perform the following steps:
	1. Convert `RAW` to `VARCHAR2` in the AL32UTF8 database character set.
		2. Convert `VARCHAR2` in the AL32UTF8 database character set to `VARCHAR2` in the database character set you wish to use.
	Syntax example:
	```
	UTL_I18N.RAW_TO_CHAR (data, 'AL32UTF8');
	```
	See Also:
	[UTL\_I18N](UTL_I18N.md) for information about using the `UTL_I18N` PL/SQL package.
- If you want to store encrypted data of the `RAW` datatype in a `VARCHAR2` database column, then use `RAWTOHEX` or `UTL_ENCODE.BASE64_ENCODE` to make it suitable for `VARCHAR2` storage. These functions expand data size by 2 and 4/3, respectively.

### 47.9 DBMS\_CRYPTO Examples

The examples in this section demonstrate different types of PL/SQL coding using `DBMS_CRYPTO` functions.

Example 1: AES Encryption with Cipher Block Chaining and PKCS#5 Compliant Padding

This example shows PL/SQL block encrypting and decrypting pre-defined `input_string` using 256-bit AES algorithm with Cipher Block Chaining and PKCS#5 compliant padding.

```
DECLARE
   input_string       VARCHAR2 (200) :=  'Secret Message';
   output_string      VARCHAR2 (200);
   encrypted_raw      RAW (2000);             -- stores encrypted binary text
   decrypted_raw      RAW (2000);             -- stores decrypted binary text
   num_key_bytes      NUMBER := 256/8;        -- key length 256 bits (32 bytes)
   key_bytes_raw      RAW (32);               -- stores 256-bit encryption key
   encryption_type    PLS_INTEGER :=          -- total encryption type

                            DBMS_CRYPTO.ENCRYPT_AES256
                          + DBMS_CRYPTO.CHAIN_CBC
                          + DBMS_CRYPTO.PAD_PKCS5;

   iv_raw             RAW (16);

BEGIN
   DBMS_OUTPUT.PUT_LINE ( 'Original string: ' || input_string);
   key_bytes_raw := DBMS_CRYPTO.RANDOMBYTES (num_key_bytes);
   iv_raw        := DBMS_CRYPTO.RANDOMBYTES (16);
   encrypted_raw := DBMS_CRYPTO.ENCRYPT
      (
         src => UTL_I18N.STRING_TO_RAW (input_string,  'AL32UTF8'),
         typ => encryption_type,
         key => key_bytes_raw,
         iv  => iv_raw
      );

    -- The encrypted value "encrypted_raw" can be used here

    decrypted_raw := DBMS_CRYPTO.DECRYPT
      (
         src => encrypted_raw,
         typ => encryption_type,
         key => key_bytes_raw,
         iv  => iv_raw
      );

   output_string := UTL_I18N.RAW_TO_CHAR (decrypted_raw, 'AL32UTF8');

   DBMS_OUTPUT.PUT_LINE ('Decrypted string: ' || output_string); 
END;
```

Example 2: PKENCRYPTION and PKDECRYPTION Functions

```
DECLARE
  ip_str     VARCHAR (200) := 'Secret Message';
  op_str     VARCHAR (200);
  -- Use OpenSSL to generate the private and public key (2048 bit RSA key)
  -- openssl genrsa -out private.pem 2048
  -- openssl rsa -in private.pem -outform PEM -pubout -out public.pem
  pubkey    VARCHAR (2000) := ‘XXXX’;
  prvkey    VARCHAR (2000) := ‘YYYY’;
  enc_raw    RAW (2000);
  dec_raw    RAW (2000);
  eType      PLS_INTEGER := DBMS_CRYPTO.PKENCRYPT_RSA_PKCS1_OAEP;
  kType      PLS_INTEGER := DBMS_CRYPTO.KEY_TYPE_RSA;

BEGIN

  DBMS_OUTPUT.PUT_LINE('-------------------------------------------------');
  DBMS_OUTPUT.PUT_LINE('Original String := ' || ip_str);
  DBMS_OUTPUT.PUT_LINE('-------------------------------------------------');
  enc_raw:= DBMS_CRYPTO.PKENCRYPT
  (
    src        => UTL_I18N.STRING_TO_RAW(ip_str,'AL32UTF8'),
    pub_key    => UTL_I18N.STRING_TO_RAW( pubkey, 'AL32UTF8'),
    pubkey_alg => kType,
    enc_alg    => eType
  );

  dec_raw := DBMS_CRYPTO.PKDECRYPT
  (
    src        => enc_raw,
    prv_key    => UTL_I18N.STRING_TO_RAW( prvkey, 'AL32UTF8'),
    pubkey_alg => kType,
    enc_alg    => eType
  );
  op_str := UTL_I18N.RAW_TO_CHAR(dec_raw,'AL32UTF8');
  dbms_output.put_line('-------------------------------------------------');
  dbms_output.put_line('Decrypted String := ' || op_str);
  dbms_output.put_line('-------------------------------------------------');
end;
/
```

Example 3: SIGN and VERIFY Functions

```
DECLARE
  ip_str     VARCHAR2 (200) := 'Secret Message';
  -- Use OpenSSL to generate the private and public key (2048 bit RSA key)
  -- openssl genrsa -out private.pem 2048
  -- openssl rsa -in private.pem -outform PEM -pubout -out public.pem
  pubkey    VARCHAR (2000) := ‘XXXX’;
  prvkey    VARCHAR (2000) := ‘YYYY’; 
  sign_raw   RAW (2000);
  returnval  BOOLEAN := false;
  sType      PLS_INTEGER := DBMS_CRYPTO.SIGN_SHA224_RSA;
  kType      PLS_INTEGER := DBMS_CRYPTO.KEY_TYPE_RSA;
BEGIN
  sign_raw := DBMS_CRYPTO.SIGN
  (
   src        => UTL_I18N.STRING_TO_RAW(ip_str,'AL32UTF8'),
   prv_key    => UTL_I18N.STRING_TO_RAW( prvkey, 'AL32UTF8'),
   pubkey_alg => kType,
   sign_alg   => sType
  );
  returnval := DBMS_CRYPTO.VERIFY
  (
   src        => UTL_I18N.STRING_TO_RAW( ip_str,'AL32UTF8'),
   sign       => sign_raw,
   pub_key    => UTL_I18N.STRING_TO_RAW( pubkey, 'AL32UTF8'),
   pubkey_alg => kType,
   sign_alg   => sType
  );
  DBMS_OUTPUT.PUT_LINE('-------------------------------------------------');
  IF returnval THEN
    DBMS_OUTPUT.PUT_LINE('True');
  ELSE
    DBMS_OUTPUT.PUT_LINE('False');
  END IF;
  DBMS_OUTPUT.PUT_LINE('-------------------------------------------------');
END;
/
```

### 47.10 Summary of DBMS\_CRYPTO Subprograms

This table lists the `DBMS_CRYPTO` subprograms in alphabetical order and briefly describes them.

Table 47-11 DBMS\_CRYPTO Package Subprograms

| Subprogram | Description |
| --- | --- |
| DECRYPT Function | Decrypts `RAW` data using a stream or block cipher with a user supplied key and optional IV (initialization vector) |
| DECRYPT Procedures | Decrypts `LOB` data using a stream or block cipher with a user supplied key and optional IV |
| ENCRYPT Function | Encrypts `RAW` data using a stream or block cipher with a user supplied key and optional IV |
| ENCRYPT Procedures | Encrypts `LOB` data using a stream or block cipher with a user supplied key and optional IV |
| HASH Function | Applies one of the supported cryptographic hash algorithms (MD5, MD4, SHA-1, or SHA-2) to data.  Note:  Starting from Oracle Database 20c Release, the use of MD5, MD4, and SHA-1 are deprecated. Oracle recommends that you do not use deprecated values in new applications. Support for deprecated features is for backward compatibility only. |
| MAC Function | Applies Message Authentication Code algorithms (MD5, SHA-1, or SHA-2) to data to provide keyed message protection.  Note:  Starting from Oracle Database 20c Release, the use of MD5 and SHA-1 are deprecated. Oracle recommends that you do not use deprecated values in new applications. Support for deprecated features is for backward compatibility only. |
| PKDECRYPT Function | Decrypts `RAW` data using a private key assisted with key algorithm and encryption algorithm and returns decrypted data. |
| PKENCRYPT Function | Encrypts `RAW` data using a public key assisted with key algorithm and encryption algorithm and returns encrypted data |
| RANDOMBYTES Function | Returns a `RAW` value containing a cryptographically secure pseudo-random sequence of bytes, and can be used to generate random material for encryption keys |
| RANDOMINTEGER Function | Returns a random `BINARY_INTEGER` |
| RANDOMNUMBER Function | Returns a random 128-bit integer of the `NUMBER` datatype |
| SIGN Function | Signs `RAW` data using a private key assisted with key algorithm and sign algorithm, and returns a signature |
| VERIFY Function | Verifies `RAW` data using the signature, public key assisted with key algorithm, and sign algorithm. It returns `TRUE` if the signature was verified |

#### 47.10.1 DECRYPT Function

This function decrypts `RAW` data using a stream or block cipher with a user supplied key and optional IV (initialization vector).

Syntax

```
DBMS_CRYPTO.DECRYPT(
   src IN RAW,
   typ IN PLS_INTEGER,
   key IN RAW,
   iv  IN RAW DEFAULT NULL)
 RETURN RAW;
```

Pragmas

```
pragma restrict_references(decrypt,WNDS,RNDS,WNPS,RNPS);
```

Parameters

Table 47-12 DECRYPT Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | `RAW` data to be decrypted. |
| `typ` | Stream or block cipher type and modifiers to be used. |
| `key` | Key to be used for decryption. |
| `iv` | Optional initialization vector for block ciphers. Default is `NULL`. |

Usage Notes

- To retrieve original plaintext data, `DECRYPT` must be called with the same cipher, modifiers, key, and IV that was used to encrypt the data originally.
	See Also:
	" Usage Notes " for the `ENCRYPT` function for additional information about the ciphers and modifiers available with this package.
- If `VARCHAR2` data is converted to `RAW` before encryption, then it must be converted back to the appropriate database character set by using the `UTL_I18N` package.
	See Also:
	DBMS\_CRYPTO Operational Notes for a discussion of the `VARCHAR2` to `RAW` conversion rules

#### 47.10.2 DECRYPT Procedures

These procedures decrypt `LOB` data using a stream or block cipher with a user supplied key and optional IV (initialization vector).

Syntax

```
DBMS_CRYPTO.DECRYPT(
   dst IN OUT NOCOPY BLOB,
   src IN            BLOB,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);

DBMS_CRYPT.DECRYPT(
   dst IN OUT NOCOPY CLOB         CHARACTER SET ANY_CS,
   src IN            BLOB,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);
```

Pragmas

```
pragma restrict_references(decrypt,WNDS,RNDS,WNPS,RNPS);
```

Parameters

Table 47-13 DECRYPT Procedure Parameters

| Parameter Name | Description |
| --- | --- |
| dst | `LOB` locator of output data. The value in the output `LOB` < `dst` > will be overwritten. |
| `src` | `LOB` locator of input data. |
| `typ` | Stream or block cipher type and modifiers to be used. |
| `key` | Key to be used for decryption. |
| `iv` | Optional initialization vector for block ciphers. Default is all zeroes. |

#### 47.10.3 ENCRYPT Function

This function encrypts `RAW` data using a stream or block cipher with a user supplied key and optional IV (initialization vector).

Syntax

```
DBMS_CRYPTO.ENCRYPT(
   src IN RAW,
   typ IN PLS_INTEGER,
   key IN RAW,
   iv  IN RAW          DEFAULT NULL)
 RETURN RAW;
```

Pragmas

```
pragma restrict_references(encrypt,WNDS,RNDS,WNPS,RNPS);
```

Parameters

Table 47-14 ENCRYPT Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | `RAW` data to be encrypted. |
| `typ` | Stream or block cipher type and modifiers to be used. |
| `key` | Encryption key to be used for encrypting data. |
| `iv` | Optional initialization vector for block ciphers. Default is `NULL`. |

Usage Notes

- Block ciphers may be modified with chaining and padding type modifiers. The chaining and padding type modifiers are added to the block cipher to produce a cipher suite. Cipher Block Chaining (CBC) is the most commonly used chaining type, and PKCS #5 is the recommended padding type. See Table 47-8 and Table 47-9 for block cipher chaining and padding modifier constants that have been defined for this package.
- To improve readability, you can define your own package-level constants to represent the cipher suites you use for encryption and decryption. For example, the following example defines a cipher suite that uses DES, cipher block chaining mode, and no padding:
	```
	DES_CBC_NONE CONSTANT PLS_INTEGER := DBMS_CRYPTO.ENCRYPT_DES
	                                     + DBMS_CRYPTO.CHAIN_CBC
	                                     + DBMS_CRYPTO.PAD_NONE;
	```
	See Table 47-7 for the block cipher suites already defined as constants for this package.
- To encrypt `VARCHAR2` data, it should first be converted to the AL32UTF8 character set.
	See Also:
	The discussion of conversion rules under DBMS\_CRYPTO Operational Notes

#### 47.10.4 ENCRYPT Procedures

These procedures encrypt `LOB` data using a stream or block cipher with a user supplied key and optional IV (initialization vector).

Syntax

```
DBMS_CRYPTO.ENCRYPT(
   dst IN OUT NOCOPY BLOB,
   src IN            BLOB,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);

DBMS_CRYPTO.ENCRYPT(
   dst IN OUT NOCOPY BLOB,
   src IN            CLOB         CHARACTER SET ANY_CS,
   typ IN            PLS_INTEGER,
   key IN            RAW,
   iv  IN            RAW          DEFAULT NULL);
```

Pragmas

```
pragma restrict_references(encrypt,WNDS,RNDS,WNPS,RNPS);
```

Parameters

Table 47-15 ENCRYPT Procedure Parameters

| Parameter Name | Description |
| --- | --- |
| dst | `LOB` locator of output data. The value in the output `LOB` < `dst` > will be overwritten. |
| `src` | `LOB` locator of input data. |
| `typ` | Stream or block cipher type and modifiers to be used. |
| `key` | Encryption key to be used for encrypting data. |
| `iv` | Optional initialization vector for block ciphers. Default is `NULL`. |

Usage Notes

See [DBMS\_DEBUG Operational Notes](DBMS_DEBUG.md) for more information about the conversion rules for the `ENCRYPT` procedure.

#### 47.10.5 HASH Function

A one-way hash function takes a variable-length input string, the data, and converts it to a fixed-length (generally smaller) output string called a hash value. The hash value serves as a unique identifier (like a fingerprint) of the input data. You can use the hash value to verify whether data has been changed or not.

Note that a one-way hash function is a hash function that works in one direction. It is easy to compute a hash value from the input data, but it is hard to generate data that hashes to a particular value. Consequently, one-way hash functions work well to ensure data integrity. Refer to “When to Use Hash or Message Authentication Code (MAC) Functions” in DBMS\_CRYPTO Operational Notes for more information about using one-way hash functions.

This function applies to data one of the supported cryptographic hash algorithms listed in Table 47-4.

Syntax

```
DBMS_CRYPTO.Hash (
   src IN RAW,
   typ IN PLS_INTEGER)
 RETURN RAW;

DBMS_CRYPTO.Hash (
   src IN BLOB,
   typ IN PLS_INTEGER)
 RETURN RAW;

DBMS_CRYPTO.Hash (
   src IN CLOB CHARACTER SET ANY_CS,
   typ IN PLS_INTEGER)
 RETURN RAW;
```

Pragmas

```
pragma restrict_references(hash,WNDS,RNDS,WNPS,RNPS);
```

Parameters

Table 47-16 HASH Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | The source data to be hashed. |
| `typ` | The hash algorithm to be used. |

Usage Note

Oracle recommends that you use the SHA-1 (Secure Hash Algorithm) or SHA-2.

#### 47.10.6 MAC Function

This function applies Message Authentication Code (MAC) algorithms to data to provide keyed message protection.

A MAC is a key-dependent one-way hash function. MACs have the same properties as the one-way hash function described in HASH Function, but they also include a key. Only someone with the identical key can verify the hash. Also refer to “When to Use Hash or Message Authentication Code (MAC) Functions” in DBMS\_CRYPTO Operational Notes for more information about using MACs.

See Table 47-5 for a list of MAC algorithms that have been defined for this package.

Syntax

```
DBMS_CRYPTO.MAC (
   src IN RAW,
   typ IN PLS_INTEGER,
   key IN RAW)
 RETURN RAW;

DBMS_CRYPTO.MAC (
   src IN BLOB,
   typ IN PLS_INTEGER
   key IN RAW)
 RETURN RAW;

DBMS_CRYPTO.MAC (
   src IN CLOB CHARACTER SET ANY_CS,
   typ IN PLS_INTEGER
   key IN RAW)
 RETURN RAW;
```

Pragmas

```
pragma restrict_references(mac,WNDS,RNDS,WNPS,RNPS);
```

Parameters

Table 47-17 MAC Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | Source data to which MAC algorithms are to be applied. |
| `typ` | MAC algorithm to be used. |
| `key` | Key to be used for MAC algorithm. |

#### 47.10.7 PKDECRYPT Function

This function decrypts `RAW` data using a private key assisted with key algorithm and encryption algorithm and returns decrypted data.

Syntax

```
DBMS_CRYPTO.PKDECRYPT(
   src IN RAW,
   prv_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   enc_alg  IN BINARY_INTEGER)
 RETURN RAW;
```

Parameters

Table 47-18 PKDECRYPT Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | `RAW` data to be decrypted. |
| `prv_key` | Private key. |
| `pubkey_alg` | Specify the KEY\_TYPE\_RSA RSA key type. |
| `enc_alg` | Specify the algorithm PKENCRYPT\_RSA\_PKCS1\_OAEP, for RSA Public Key Cryptosystem with PKCS1 and OAEP padding. |

#### 47.10.8 PKENCRYPT Function

This function encrypts `RAW` data using a public key assisted with key algorithm and encryption algorithm and returns encrypted data.

Syntax

```
DBMS_CRYPTO.PKENCRYPT(
   src IN RAW,
   pub_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   enc_alg  IN BINARY_INTEGER)
 RETURN RAW;
```

Parameters

Table 47-19 PKENCRYPT Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | `RAW` data to be encrypted. |
| `pub_key` | Public key. |
| `pubkey_alg` | Specify the KEY\_TYPE\_RSA RSA key type. |
| `enc_alg` | Specify the algorithm PKENCRYPT\_RSA\_PKCS1\_OAEP, for RSA Public Key Cryptosystem with PKCS1 and OAEP padding. |

#### 47.10.9 RANDOMBYTES Function

This function returns a `RAW` value containing a cryptographically secure pseudo-random sequence of bytes, which can be used to generate random material for encryption keys.

Syntax

```
DBMS_CRYPTO.RANDOMBYTES (
   number_bytes IN POSITIVE)
 RETURN RAW;
```

Pragmas

```
pragma restrict_references(randombytes,WNDS,RNDS,WNPS,RNPS);
```

Parameters

Table 47-20 RANDOMBYTES Function Parameter

| Parameter Name | Description |
| --- | --- |
| `number_bytes` | The number of pseudo-random bytes to be generated. |

Usage Note

The `number_bytes` value should not exceed the maximum length of a `RAW` variable.

#### 47.10.10 RANDOMINTEGER Function

This function returns an integer in the complete range available for the Oracle `BINARY_INTEGER` datatype.

Syntax

```
DBMS_CRYPTO.RANDOMINTEGER
 RETURN BINARY_INTEGER;
```

Pragmas

```
pragma restrict_references(randominteger,WNDS,RNDS,WNPS,RNPS);
```

#### 47.10.11 RANDOMNUMBER Function

This function returns an integer in the Oracle `NUMBER` datatype in the range of \[0..2\*\*128-1\].

Syntax

```
DBMS_CRYPTO.RANDOMNUMBER
 RETURN NUMBER;
```

Pragmas

```
pragma restrict_references(randomnumber,WNDS,RNDS,WNPS,RNPS);
```

#### 47.10.12 SIGN Function

This function signs `RAW` data using a private key assisted with key algorithm and sign algorithm, and returns a signature.

Syntax

```
DBMS_CRYPTO.SIGN(
   src IN RAW,
   prv_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   sign_alg IN BINARY_INTEGER)
 RETURN RAW;
```

Parameters

Table 47-21 SIGN Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | `RAW` data to be signed. |
| `prv_key` | Private key. |
| `pubkey_alg` | Specify the KEY\_TYPE\_RSA RSA key type. |
| `sign_alg` | Specify one of the algorithms that are listed in the Usage Notes. |

Usage Notes

Table 47-22 SHA Hash Algorithms

| Hash Algorithm | Description |
| --- | --- |
| SIGN\_SHA1\_RSA | SHA1 hash function with RSA |
| SIGN\_SHA1\_RSA\_X931 | SHA1 hash function with RSA and X931 padding |
| SIGN\_SHA224\_RSA | SHA 224 bit hash function with RSA |
| SIGN\_SHA256\_RSA | SHA 256 bit hash function with RSA |
| SIGN\_SHA256\_RSA\_X931 | SHA 256 bit hash function with RSA and X931 padding |
| SIGN\_SHA384\_RSA | SHA 384 bit hash function with RSA |
| SIGN\_SHA384\_RSA\_X931 | SHA 384 bit hash function with RSA and X931 padding |
| SIGN\_SHA512\_RSA | SHA 512 bit hash function with RSA |
| SIGN\_SHA512\_RSA\_X931 | SHA 512 bit hash function with RSA and X931 padding |

#### 47.10.13 VERIFY Function

This function verifies `RAW` data using the signature, public key assisted with key algorithm, and sign algorithm. It returns `TRUE` if the signature was verified.

Syntax

```
DBMS_CRYPTO.VERIFY(
   src IN RAW,
   sign IN RAW,
   pub_key IN RAW,
   pubkey_alg IN BINARY_INTEGER,
   sign_alg  IN BINARY_INTEGER)
 RETURN BOOLEAN;
```

Parameters

Table 47-23 VERIFY Function Parameters

| Parameter Name | Description |
| --- | --- |
| `src` | `RAW` data to be verified. |
| `sign` | Message signature. |
| `pub_key` | Public key. |
| `pubkey_alg` | Specify the KEY\_TYPE\_RSA RSA key type. |
| `sign_alg` | Specify one of the algorithms that are listed the Usage Notes. |

Usage Notes

Table 47-24 SHA Hash Algorithms

| Hash Algorithm | Description |
| --- | --- |
| SIGN\_SHA1\_RSA | SHA hash function with RSA |
| SIGN\_SHA1\_RSA\_X931 | SHA hash function with RSA and X931 padding |
| SIGN\_SHA224\_RSA | SHA 224 bit hash function with RSA |
| SIGN\_SHA256\_RSA | SHA 256 bit hash function with RSA |
| SIGN\_SHA256\_RSA\_X931 | SHA 256 bit hash function with RSA and X931 padding |
| SIGN\_SHA384\_RSA | SHA 384 bit hash function with RSA |
| SIGN\_SHA384\_RSA\_X931 | SHA 384 bit hash function with RSA and X931 padding |
| SIGN\_SHA512\_RSA | SHA 512 bit hash function with RSA |
| SIGN\_SHA512\_RSA\_X931 | SHA 512 bit hash function with RSA and X931 padding |