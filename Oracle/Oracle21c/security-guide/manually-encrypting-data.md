---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/manually-encrypting-data.html
tags:
  - oracle
  - 21c
  - security-guide
---

- Security Problems That Encryption Does Not Solve  
	While there are many good reasons to encrypt data, there are many reasons not to encrypt data.
- Data Encryption Challenges  
	In cases where encryption can provide additional security, there are some associated technical challenges.
- Data Encryption Storage with the DBMS\_CRYPTO Package  
	The `DBMS_CRYPTO` package provides several ways to address security issues.
- Asymmetric Key Operations with the DBMS\_CRYPTO Package  
	The `DBMS_CRYPTO` package provides four functions that enable you to perform asymmetric key operations for encryption, decryption, signing, and verification.
- Using Ciphertexts Encrypted in OFB Mode in Oracle Database Release 11g  
	In Oracle Database Release 11g, ciphertexts configured to use output feedback (OFB) used electronic codebook (ECB) mode instead.
- Examples of Using the Data Encryption API  
	Examples of using the data encryption API include using the `DBMS_CRYPTO.SQL` procedure, encrypting AES 256-bit data, and encrypting BLOB data.
- Data Dictionary Views for Encrypted Data  
	Oracle Database provides data dictionary views to find information about encrypted data.

**Parent topic:** [Controlling Access to Data](part_3.md)

### 16.1 Security Problems That Encryption Does Not Solve

While there are many good reasons to encrypt data, there are many reasons not to encrypt data.

**Parent topic:** Manually Encrypting Data

#### 16.1.1 Principle 1: Encryption Does Not Solve Access Control Problems

When you encrypt data, you should be aware that encryption must not interfere with how you configure access control.

Most organizations must limit data access to users who need to see this data. For example, a human resources system may limit employees to viewing only their own employment records, while allowing managers of employees to see the employment records of subordinates. Human resource specialists may also need to see employee records for multiple employees.

Typically, you can use access control mechanisms to address security policies that limit data access to those with a need to see it. Oracle Database has provided strong, independently evaluated access control mechanisms for many years. It enables access control enforcement to a fine level of granularity through Virtual Private Database.

Because human resource records are considered sensitive information, it is tempting to think that all information should be encrypted for better security. However, encryption cannot enforce granular access control, and it may hinder data access. For example, an employee, his manager, and a human resources clerk may all need to access an employee record. If all employee data is encrypted, then all three must be able to access the data in unencrypted form. Therefore, the employee, the manager and the human resources clerk would have to share the same encryption key to decrypt the data. Encryption would, therefore, not provide any additional security in the sense of better access control, and the encryption might hinder the proper or efficient functioning of the application. An additional issue is that it is difficult to securely transmit and share encryption keys among multiple users of a system.

A basic principle behind encrypting stored data is that it must not interfere with access control. For example, a user who has the `SELECT` privilege on `emp` should not be limited by the encryption mechanism from seeing all the data he is otherwise allowed to see. Similarly, there is little benefit to encrypting part of a table with one key and part of a table with another key if users need to see all encrypted data in the table. In this case, encryption adds to the overhead of decrypting the data before users can read it. If access controls are implemented well, then encryption adds little additional security within the database itself. A user who has privileges to access data within the database has no more nor any less privileges as a result of encryption. Therefore, you should never use encryption to solve access control problems.

**Parent topic:** Security Problems That Encryption Does Not Solve

#### 16.1.2 Principle 2: Encryption Does Not Protect Against a Malicious Administrator

You can protect your databases against malicious database administrators by using other Oracle features, such as Oracle Database Vault.

Some organizations, concerned that a malicious user might gain elevated (database administrator) privileges by guessing a password, like the idea of encrypting stored data to protect against this threat.

However, the correct solution to this problem is to protect the database administrator account, and to change default passwords for other privileged accounts. The easiest way to break into a database is by using a default password for a privileged account that an administrator allowed to remain unchanged. One example is `SYS` / `CHANGE_ON_INSTALL`.

While there are many destructive things a malicious user can do to a database after gaining the `DBA` privilege, encryption will not protect against many of them. Examples include corrupting or deleting data, exporting user data to the file system to email the data back to himself to run a password cracker on it, and so on.

Some organizations are concerned that database administrators, typically having all privileges, are able to see all data in the database. These organizations feel that the database administrators should administer the database, but should not be able to see the data that the database contains. Some organizations are also concerned about concentrating so much privilege in one person, and would prefer to partition the DBA function, or enforce two-person access rules.

It is tempting to think that encrypting all data (or significant amounts of data) will solve these problems, but there are better ways to protect against these threats. For example, Oracle Database supports limited partitioning of `DBA` privileges. Oracle Database provides native support for `SYSDBA` and `SYSOPER` users. `SYSDBA` has all privileges, but `SYSOPER` has a limited privilege set (such as startup and shutdown of the database).

Furthermore, you can create smaller roles encompassing several system privileges. A `jr_dba` role might not include all system privileges, but only those appropriate to a junior database administrator (such as `CREATE TABLE`, `CREATE USER`, and so on).

Oracle Database also enables auditing the actions taken by `SYS` (or `SYS` -privileged users) and storing that audit trail in a secure operating system location. Using this model, a separate auditor who has root privileges on the operating system can audit all actions by `SYS`, enabling the auditor to hold all database administrators accountable for their actions.

You can also fine-tune the access and control that database administrators have by using Oracle Database Vault.

The database administrator function is a trusted position. Even organizations with the most sensitive data, such as intelligence agencies, do not typically partition the database administrator function. Instead, they manage their database administrators strongly, because it is a position of trust. Periodic auditing can help to uncover inappropriate activities.

Encryption of stored data must not interfere with the administration of the database, because otherwise, larger security issues can result. For example, if by encrypting data you corrupt the data, then you create a security problem, the data itself cannot be interpreted, and it may not be recoverable.

You can use encryption to limit the ability of a database administrator or other privileged user to see data in the database. However, it is not a substitute for managing the database administrator privileges properly, or for controlling the use of powerful system privileges. If untrustworthy users have significant privileges, then they can pose multiple threats to an organization, some of them far more significant than viewing unencrypted credit card numbers.

#### 16.1.3 Principle 3: Encrypting Everything Does Not Make Data Secure

A common error is to think that if encrypting some data strengthens security, then encrypting everything makes all data secure.

As the discussion of the previous two principles illustrates, encryption does not address access control issues well, and it is important that encryption not interfere with normal access controls. Furthermore, encrypting an entire production database means that all data must be decrypted to be read, updated, or deleted. Encryption is inherently a performance-intensive operation; encrypting all data will significantly affect performance.

Availability is a key aspect of security. If encrypting data makes data unavailable, or adversely affects availability by reducing performance, then encrypting everything will create a new security problem. Availability is also adversely affected by the database being inaccessible when encryption keys are changed, as good security practices require on a regular basis. When the keys are to be changed, the database is inaccessible while data is decrypted and reencrypted with a new key or keys.

There may be advantages to encrypting data stored off-line. For example, an organization may store backups for a period of 6 months to a year off-line, in a remote location. Of course, the first line of protection is to secure the facility storing the data, by establishing physical access controls. Encrypting this data before it is stored may provide additional benefits. Because it is not being accessed on-line, performance need not be a consideration. While an Oracle database does not provide this capability, there are vendors who provide encryption services. Before embarking on large-scale encryption of backup data, organizations considering this approach should thoroughly test the process. It is essential to verify that data encrypted before off-line storage can be decrypted and re-imported successfully.

**Parent topic:** Security Problems That Encryption Does Not Solve

### 16.2 Data Encryption Challenges

In cases where encryption can provide additional security, there are some associated technical challenges.

- Encrypted Indexed Data  
	Special difficulties arise when encrypted data is indexed.
- Generated Encryption Keys  
	Encrypted data is only as secure as the key used for encrypting it.
- Transmitted Encryption Keys  
	If the encryption key is to be passed by the application to the database, then you must encrypt it.
- Storing Encryption Keys  
	You can store encryption keys in the database or on an operating system.
- Importance of Changing Encryption Keys  
	Prudent security practice dictates that you periodically change encryption keys.
- Encryption of Binary Large Objects  
	Certain data types require more work to encrypt.

**Parent topic:** Manually Encrypting Data

#### 16.2.1 Encrypted Indexed Data

Special difficulties arise when encrypted data is indexed.

For example, suppose a company uses a national identity number, such as the U.S. Social Security number (SSN), as the employee number for its employees. The company considers employee numbers to be sensitive data, and, therefore, wants to encrypt data in the `employee_number` column of the `employees` table. Because `employee_number` contains unique values, the database designers want to have an index on it for better performance.

However, if `DBMS_CRYPTO` (or another mechanism) is used to encrypt data in a column, then an index on that column will also contain encrypted values. Although an index can be used for equality checking (for example, `SELECT * FROM emp WHERE employee_number = '987654321'`), if the index on that column contains encrypted values, then the index is essentially unusable for any other purpose. You should not encrypt indexed data.

Oracle recommends that you do not use national identity numbers as unique IDs. Instead, use the `CREATE SEQUENCE` statement to generate unique identity numbers. Reasons to avoid using national identity numbers are as follows:

- There are privacy issues associated with overuse of national identity numbers (for example, identity theft).
- Sometimes national identity numbers can have duplicates, as with U.S. Social Security numbers.

**Parent topic:** Data Encryption Challenges

#### 16.2.2 Generated Encryption Keys

Encrypted data is only as secure as the key used for encrypting it.

An encryption key must be securely generated using secure cryptographic key generation. Oracle Database provides support for secure random number generation, with the `RANDOMBYTES` function of `DBMS_CRYPTO`. `DBMS_CRYPTO` calls the secure random number generator (RNG) previously certified by RSA Security.

Note:

Do not use the `DBMS_RANDOM` package. The `DBMS_RANDOM` package generates pseudo-random numbers, which, as Randomness Recommendations for Security (RFC-1750) states that using pseudo-random processes to generate secret quantities can result in pseudo-security.

Be sure to provide the correct number of bytes when you encrypt a key value. For example, you must provide a 16-byte key for the `ENCRYPT_AES128` encryption algorithm.

**Parent topic:** Data Encryption Challenges

#### 16.2.3 Transmitted Encryption Keys

If the encryption key is to be passed by the application to the database, then you must encrypt it.

Otherwise, an intruder could get access to the key as it is being transmitted. Network data encryption protects all data in transit from modification or interception, including cryptographic keys.

#### 16.2.4 Storing Encryption Keys

You can store encryption keys in the database or on an operating system.

- About Storing Encryption Keys  
	Storing encryption keys is one of the most important, yet difficult, aspects of encryption.
- Storage of Encryption Keys in the Database  
	Storing encryption keys in the database does not always prevent a database administrator from accessing encrypted data.
- Storage of Encryption Keys in the Operating System  
	When you store encryption keys in an operating system flat file, you can make callouts from PL/SQL to retrieve these encryption keys.
- Users Managing Their Own Encryption Keys  
	Having the user supply the key assumes the user will be responsible with the key.
- Manual Encryption with Transparent Database Encryption and Tablespace Encryption  
	Transparent database encryption and tablespace encryption provide secure encryption with automatic key management for the encrypted tables and tablespaces.

**Parent topic:** Data Encryption Challenges

##### 16.2.4.1 About Storing Encryption Keys

Storing encryption keys is one of the most important, yet difficult, aspects of encryption.

To recover data encrypted with a symmetric key, the key must be accessible to an authorized application or user seeking to decrypt the data. At the same time, the key must be inaccessible to someone who is maliciously trying to access encrypted data that he is not supposed to see.

**Parent topic:** Storing Encryption Keys

##### 16.2.4.2 Storage of Encryption Keys in the Database

Storing encryption keys in the database does not always prevent a database administrator from accessing encrypted data.

An all-privileged database administrator could still access tables containing encryption keys. However, it can often provide good security against the casual curious user or against someone compromising the database file on the operating system.

As a trivial example, suppose you create a table (`EMP`) that contains employee data. You want to encrypt the employee Social Security number (SSN) stored in one of the columns. You could encrypt employee SSN using a key that is stored in a separate column. However, anyone with `SELECT` access on the entire table could retrieve the encryption key and decrypt the matching SSN.

While this encryption scheme seems easily defeated, with a little more effort you can create a solution that is much harder to break. For example, you could encrypt the SSN using a technique that performs some additional data transformation on the `employee_number` before using it to encrypt the SSN. This technique might be as simple as using an `XOR` operation on the `employee_number` and the birth date of the employee to determine the validity of the values.

As additional protection, PL/SQL source code performing encryption can be wrapped, (using the `WRAP` utility) which obfuscates (scrambles) the code. The `WRAP` utility processes an input SQL file and obfuscates the PL/SQL units in it. For example, the following command uses the `keymanage.sql` file as the input:

```
wrap iname=/mydir/keymanage.sql
```

A developer can subsequently have a function in the package call the `DBMS_CRYPTO` package calls with the key contained in the wrapped package.

Oracle Database enables you to obfuscate dynamically generated PL/SQL code. The `DBMS_DDL` package contains two subprograms that allow you to obfuscate dynamically generated PL/SQL program units. For example, the following block uses the `DBMS_DDL.CREATE_WRAPPED` procedure to wrap dynamically generated PL/SQL code.

```
BEGIN
......
SYS.DBMS_DDL.CREATE_WRAPPED(function_returning_PLSQL_code());
......
END;
```

While wrapping is not unbreakable, it makes it harder for an intruder to get access to the encryption key. Even in cases where a different key is supplied for each encrypted data value, you should not embed the key value within a package. Instead, wrap the package that performs the key management (that is, data transformation or padding).

An alternative to wrapping the data is to have a separate table in which to store the encryption key and to envelope the call to the keys table with a procedure. The key table can be joined to the data table using a primary key to foreign key relationship. For example, `employee_number` is the primary key in the `employees` table that stores employee information and the encrypted SSN. The `employee_number` column is a foreign key to the `ssn_keys` table that stores the encryption keys for the employee SSN. The key stored in the `ssn_keys` table can also be transformed before use (by using an `XOR` operation), so the key itself is not stored unencrypted. If you wrap the procedure, then that can hide the way in which the keys are transformed before use.

The strengths of this approach are:

- Users who have direct table access cannot see the sensitive data unencrypted, nor can they retrieve the keys to decrypt the data.
- Access to decrypted data can be controlled through a procedure that selects the encrypted data, retrieves the decryption key from the key table, and transforms it before it can be used to decrypt the data.
- The data transformation algorithm is hidden from casual snooping by wrapping the procedure, which obfuscates the procedure code.
- `SELECT` access to both the data table and the keys table does not guarantee that the user with this access can decrypt the data, because the key is transformed before use.

The weakness to this approach is that a user who has `SELECT` access to both the key table and the data table, and who can derive the key transformation algorithm, can break the encryption scheme.

The preceding approach is not infallible, but it is adequate to protect against easy retrieval of sensitive information stored in clear text.

##### 16.2.4.3 Storage of Encryption Keys in the Operating System

When you store encryption keys in an operating system flat file, you can make callouts from PL/SQL to retrieve these encryption keys.

However, if you store keys in the operating system and make callouts to it, then your data is only as secure as the protection on the operating system.

If your primary security concern is that the database can be broken into from the operating system, then storing the keys in the operating system makes it easier for an intruder to retrieve encrypted data than storing the keys in the database itself.

**Parent topic:** Storing Encryption Keys

##### 16.2.4.4 Users Managing Their Own Encryption Keys

Having the user supply the key assumes the user will be responsible with the key.

Considering that 40 percent of help desk calls are from users who have forgotten their passwords, you can see the risks of having users manage encryption keys. In all likelihood, users will either forget an encryption key, or write the key down, which then creates a security weakness. If a user forgets an encryption key or leaves the company, then your data is not recoverable.

If you do decide to have user-supplied or user-managed keys, then you need to ensure you are using native network encryption so that the key is not passed from the client to the server in the clear. You also must develop key archive mechanisms, which is also a difficult security problem. Key archives and backdoors create the security weaknesses that encryption is attempting to solve.

**Parent topic:** Storing Encryption Keys

##### 16.2.4.5 Manual Encryption with Transparent Database Encryption and Tablespace Encryption

Transparent database encryption and tablespace encryption provide secure encryption with automatic key management for the encrypted tables and tablespaces.

If the application requires protection of sensitive column data stored on the media, then these two types of encryption are a simple and fast way of achieving this.

#### 16.2.5 Importance of Changing Encryption Keys

Prudent security practice dictates that you periodically change encryption keys.

For stored data, this requires periodically unencrypting the data, and then reencrypting it with another well-chosen key.

You would most likely change the encryption key while the data is not being accessed, which creates another challenge. This is especially true for a Web-based application encrypting credit card numbers, because you do not want to shut down the entire application while you switch encryption keys.

**Parent topic:** Data Encryption Challenges

#### 16.2.6 Encryption of Binary Large Objects

Certain data types require more work to encrypt.

For example, Oracle Database supports storage of binary large objects (BLOBs), which stores very large objects (for example, multiple gigabytes) in the database. A BLOB can be either stored internally as a column, or stored in an external file.

### 16.3 Data Encryption Storage with the DBMS\_CRYPTO Package

The `DBMS_CRYPTO` package provides several ways to address security issues.

While encryption is not the ideal solution for addressing several security threats, it is clear that selectively encrypting sensitive data before storage in the database does improve security. Examples of such data could include credit card numbers and national identity numbers.

Oracle Database provides the PL/SQL package `DBMS_CRYPTO` to encrypt and decrypt stored data. This package supports several industry-standard encryption and hashing algorithms, including the Advanced Encryption Standard (AES) encryption algorithm. AES was approved by the National Institute of Standards and Technology (NIST) to replace the Data Encryption Standard (DES).

The `DBMS_CRYPTO` package enables encryption and decryption for common Oracle Database data types, including `RAW` and large objects (LOBs), such as images and sound. Specifically, it supports BLOBs and CLOBs. In addition, it provides Globalization Support for encrypting data across different database character sets.

The following cryptographic algorithms are supported:

- Advanced Encryption Standard (AES)
- SHA-2 Cryptographic Hash settings:
	- `HASH_SH256`
		- `HASH_SH384`
		- `HASH_SH512`
- SHA-2 Message Authentication Code (MAC)

Block cipher modifiers are also provided with `DBMS_CRYPTO`. You can choose from several padding options, including Public Key Cryptographic Standard (PKCS) #5, and from four block cipher chaining modes, including Cipher Block Chaining (CBC). Padding must be done in multiples of eight bytes.

Note:

- DES is no longer recommended by the National Institute of Standards and Technology (NIST).
- Usage of SHA-1 is more secure than MD5. (MD5 has been deprecated starting in Oracle Database 21c.)
	Starting with Oracle Database 21c, older encryption and hashing algorithms are deprecated. Deprecated algorithms include MD4, MD5, DES, 3DES, and RC4-related algorithms. Removing older, less secure cryptography algorithms prevents accidental use of these APIs. To meet your security requirements, Oracle recommends that you use more modern cryptography algorithms such as AES.
	Starting with Oracle Database 21c, older encryption and hashing algorithms are deprecated.
	As a consequence of this deprecation, Oracle recommends that you review your network encryption configuration to see if you have specified use of any of the deprecated algorithms. If any are found, then switch to using a more modern cipher, such as AES. See [Improving Native Network Encryption Security](configuring-secure-sockets-layer-authentication.md) for more information.
- Usage of SHA-2 is more secure than SHA-1.
- Keyed MD5 is not vulnerable.

Table 16-1 summarizes the `DBMS_CRYPTO` package features.

Table 16-1 DBMS\_CRYPTO Package Feature Summary

| Feature | DBMS\_CRYPTO Supported Functionality |
| --- | --- |
| Block cipher chaining modes | CBC, CFB, ECB, OFB |
| Cryptographic algorithms | AES |
| Cryptographic hash algorithms | SHA-1, SHA-2, HASH\_SH256, HASH\_SH384, HASH\_SH512 |
| Cryptographic pseudo-random number generator | `RAW`, `NUMBER`, `BINARY_INTEGER` |
| Database types | `RAW`, `CLOB`, `BLOB` |
| Keyed hash (MAC) algorithms | HMAC\_MD5, HMAC\_SH1, HMAC\_SH256, HMAC\_SH384, HMAC\_SH512 |
| Padding forms | PKCS5, zeroes |

Table 16-2 shows supported SHA hash functions, many of which can be used with RSA environments.

Table 16-2 SHA Hash Algorithms

| Hash Algorithm | Description |
| --- | --- |
| SIGN\_RSA\_PKCS1\_OAEP\_SHA256 | RSA with Public Key Cryptographic Standards, SHA 256 bit hash function and OAEP padding |
| SIGN\_SHA1\_ECDSA | SHA hash function with Elliptic Curve Digital Signature Algorithm |
| SIGN\_SHA1\_RSA | SHA hash function with RSA |
| SIGN\_SHA1\_RSA\_X931 | SHA hash function with RSA and X931 padding |
| SIGN\_SHA224\_ECDSA | SHA 224 bit hash function with Elliptic Curve Digital Signature Algorithm |
| SIGN\_SHA224\_RSA | SHA 224 bit hash function with RSA |
| SIGN\_SHA256\_ECDSA | SHA 256 bit hash function with Elliptic Curve Digital Signature Algorithm |
| SIGN\_SHA256\_RSA | SHA 256 bit hash function with RSA |
| SIGN\_SHA256\_RSA\_X931 | SHA 256 bit hash function with RSA and X931 padding |
| SIGN\_SHA384\_ECDSA | SHA 384 bit hash function with Elliptic Curve Digital Signature Algorithm |
| SIGN\_SHA384\_RSA | SHA 384 bit hash function with RSA |
| SIGN\_SHA384\_RSA\_X931 | SHA 384 bit hash function with RSA and X931 padding |
| SIGN\_SHA512\_ECDSA | SHA 512bit hash function with Elliptic Curve Digital Signature Algorithm |
| SIGN\_SHA512\_RSA | SHA 384 bit hash function with RSA |
| SIGN\_SHA512\_RSA\_X931 | SHA 384 bit hash function with RSA and X931 padding |

Table 16-3 shows supported encryption and decryption algorithms.

Table 16-3 Encryption and Decryption Algorithms

| Algorithm | Description |
| --- | --- |
| PKENCRYPT\_ECDH | Elliptic Curve Diffie Hellman |
| PKENCRYPT\_RSA\_PKCS1\_OAEP | RSA Public Key Cryptosystem with PKCS1 and OAEP padding |

Table 16-4 shows other supported algorithms.

Table 16-4 Other Algorithms

| Algorithm | Description |
| --- | --- |
| KEY\_TYPE\_RSA | RSA key type |
| SIGN\_ECDSA | Elliptic Curve Digital Signature Algorithm |

`DBMS_CRYPTO` supports a range of algorithms that accommodate both new and existing systems. Although 3DES\_2KEY and MD4 are provided for backward compatibility, you achieve better security using 3DES, AES, or SHA-1. Therefore, 3DES\_2KEY is not recommended.

The `DBMS_CRYPTO` package includes cryptographic checksum capabilities (MD5), which are useful for comparisons, and the ability to generate a secure random number (the `RANDOMBYTES` function). Secure random number generation is an important part of cryptography; predictable keys are easily guessed keys; and easily guessed keys may lead to easy decryption of data. Most cryptanalysis is done by finding weak keys or poorly stored keys, rather than through brute force analysis (cycling through all possible keys).

Note:

Do not use `DBMS_RANDOM`, because it is unsuitable for cryptographic key generation.

Key management is programmatic. That is, the application (or caller of the function) must supply the encryption key. This means that the application developer must find a way of storing and retrieving keys securely. The relative strengths and weaknesses of various key management techniques are discussed in the sections that follow. The DES algorithm itself has an effective key length of 56-bits.

**Parent topic:** Manually Encrypting Data

### 16.4 Asymmetric Key Operations with the DBMS\_CRYPTO Package

The `DBMS_CRYPTO` package provides four functions that enable you to perform asymmetric key operations for encryption, decryption, signing, and verification.

Asymmetric key operations (also called public key cryptography) use a public key and private key to encrypt and decrypt a message in order to protect it from unauthorized access.

The asymmetric key operation functions are as follows:

- `PKDECRYPT` decrypts `RAW` data using a private key assisted with key algorithm and encryption algorithm.
- `PKENCRYPT` encrypts `RAW` data using a public key assisted with key algorithm and encryption algorithm.
- `SIGN` signs `RAW` data using a private key assisted with key algorithm and sign algorithm
- `VERIFY` verifies `RAW` data using signature, public key assisted with key algorithm and sign algorithm.

### 16.5 Using Ciphertexts Encrypted in OFB Mode in Oracle Database Release 11g

In Oracle Database Release 11g, ciphertexts configured to use output feedback (OFB) used electronic codebook (ECB) mode instead.

In Oracle Database Release 11g, if you set the `DBMS_CRYPTO.CHAIN_OFB` block cipher chaining modifier to configure ciphertext encryption to use output feedback (OFB) mode, then due to Oracle Bug 13001552, the result is that the configuration used electronic codebook (ECB) mode erroneously. This bug has been fixed in Oracle Database Release 12c. Therefore, after an upgrade from Oracle Database release 11g to Release 12c, the ciphertexts that were encrypted using OFB mode in release 11g will no longer decrypt properly in the corrected OFB mode in Oracle Database Release 12c or later.

To remedy this problem:

1. Log in to the database as a user who has the `EXECUTE` privilege for the `DBMS_CRYPTO` PL/SQL package.
2. Decrypt the cyphertexts using the `DBMS_CRYPTO.CHAIN_ECB` block cipher chaining modifier.

The following example, `dbmscrypto11.sql`, shows the wrong behavior in Oracle Database Release 11g:

```
dbmscrypto11.sql:
set serveroutput on

declare
  l_mod_ofb pls_integer;
  l_mod_ecb pls_integer;
  v_key raw(32);
  v_iv  raw(16);
  v_test_in raw(16);
  v_ciphertext raw(16);
  v_test_out_ECB raw(16);
  v_test_out_OFB raw(16);
begin
  l_mod_ofb := dbms_crypto.ENCRYPT_AES256
       + dbms_crypto.CHAIN_OFB
       + DBMS_CRYPTO.PAD_NONE ;
  l_mod_ecb := dbms_crypto.ENCRYPT_AES256
       + dbms_crypto.CHAIN_ECB
       + DBMS_CRYPTO.PAD_NONE ;

  v_key := hextoraw
  ('603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4');
  v_iv :=   hextoraw('000102030405060708090A0B0C0D0E0F');
  v_test_in := hextoraw('6bc1bee22e409f96e93d7e117393172a');
  v_ciphertext := dbms_crypto.encrypt(src => v_test_in,
                                  TYP => l_mod_ofb,
                                  key => v_key,
                                  iv => v_iv);
  v_test_out_ECB := dbms_crypto.decrypt(src => v_ciphertext,
                                  TYP => l_mod_ecb,
                                  key => v_key,
                                  iv => v_iv);
  v_test_out_OFB := dbms_crypto.decrypt(src => v_ciphertext,
                                  TYP => l_mod_ofb,
                                  key => v_key,
                                  iv => v_iv);
  dbms_output.put_line
  ('Input plaintext                      : '||rawtohex(v_test_in));
  dbms_output.put_line
  ('11g: Ciphertext (encrypt in OFB mode): '||rawtohex(v_ciphertext));
  dbms_output.put_line
  ('11g: Output of decrypt in ECB mode   : '||rawtohex(v_test_out_ECB));
  dbms_output.put_line
  ('11g: Output of decrypt in OFB mode   : '||rawtohex(v_test_out_OFB));
end;
/
```

The resulting output is as follows:

```
SQL> @dbmscrypto11.sql

Input plaintext                      : 6BC1BEE22E409F96E93D7E117393172A
11g: Ciphertext (encrypt in OFB mode): F3EED1BDB5D2A03C064B5A7E3DB181F8
11g: Output of decrypt in ECB mode   : 6BC1BEE22E409F96E93D7E117393172A
11g: Output of decrypt in OFB mode   : 6BC1BEE22E409F96E93D7E117393172A
```

This output illustrates that in Oracle Database release 11g, OFB mode is wrongly ECB mode, and therefore decrypting in either OFB or ECB mode results in the correct plaintext.

The next example, `dbmscrypto12from11.sql`, shows that, after an upgrade from Oracle Database release 11g to release 12c, ECB mode and not OFB mode has to be used in order to properly decrypt a ciphertext encrypted in OFB mode in Release 11g.

```
dbmscrypto12from11.sql:
set serveroutput on

declare
  l_mod_ofb pls_integer;
  l_mod_ecb pls_integer;
  v_key raw(32);
  v_iv  raw(16);
  v_test_in raw(16);
  v_ciphertext11 raw(16);
  v_test_out_ECB raw(16);
  v_test_out_OFB raw(16);
begin
  l_mod_ofb := dbms_crypto.ENCRYPT_AES256
       + dbms_crypto.CHAIN_OFB
       + DBMS_CRYPTO.PAD_NONE ;
  l_mod_ecb := dbms_crypto.ENCRYPT_AES256
       + dbms_crypto.CHAIN_ECB
       + DBMS_CRYPTO.PAD_NONE ;

  v_key := hextoraw
  ('603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4');
  v_iv :=   hextoraw('000102030405060708090A0B0C0D0E0F');
  v_test_in := hextoraw('6bc1bee22e409f96e93d7e117393172a');
  v_ciphertext11 := hextoraw('F3EED1BDB5D2A03C064B5A7E3DB181F8');

  v_test_out_ECB := dbms_crypto.decrypt(src => v_ciphertext11,
                                  TYP => l_mod_ecb,
                                  key => v_key,
                                  iv => v_iv);
  v_test_out_OFB := dbms_crypto.decrypt(src => v_ciphertext11,
                                  TYP => l_mod_ofb,
                                  key => v_key,
                                  iv => v_iv);
  dbms_output.put_line
  ('Input plaintext (to 11g)             : '||rawtohex(v_test_in));
  dbms_output.put_line
  ('11g: Ciphertext (encrypt in OFB mode): '||rawtohex(v_ciphertext11));
  dbms_output.put_line
  ('12c: Output of decrypt in ECB mode   : '||rawtohex(v_test_out_ECB));
  dbms_output.put_line
  ('12c: Output of decrypt in OFB mode   : '||rawtohex(v_test_out_OFB));
end;
/
```

The resulting output is as follows:

```
SQL> @dbmscrypto12from11.sql
Input plaintext (to 11g)             : 6BC1BEE22E409F96E93D7E117393172A
11g: Ciphertext (encrypt in OFB mode): F3EED1BDB5D2A03C064B5A7E3DB181F8
12c: Output of decrypt in ECB mode   : 6BC1BEE22E409F96E93D7E117393172A
12c: Output of decrypt in OFB mode   : 4451EBE041EB29E191BBA0E9D67FAEB2
```

If you are preparing to upgrade from Oracle Database Release 11g to Release 12c, then edit any scripts that you may have in which OFB mode is specified so that the decrypt operations use ECB mode. This way, the scripts will work in both release 11g and release 12c and later, ensuring business continuity.

**Parent topic:** Manually Encrypting Data

### 16.6 Examples of Using the Data Encryption API

Examples of using the data encryption API include using the `DBMS_CRYPTO.SQL` procedure, encrypting AES 256-bit data, and encrypting BLOB data.

- Example: Data Encryption Procedure  
	The `DBMS_CRYPTO.SQL` PL/SQL program can be used to encrypt data.
- Example: AES 256-Bit Data Encryption and Decryption Procedures  
	You can use a PL/SQL block to encrypt and decrypt a predefined variable.
- Example: Encryption and Decryption Procedures for BLOB Data  
	You can encrypt BLOB data.

**Parent topic:** Manually Encrypting Data

#### 16.6.1 Example: Data Encryption Procedure

The `DBMS_CRYPTO.SQL` PL/SQL program can be used to encrypt data.

This example code performs the following actions:

- Encrypts a string (`VARCHAR2` type) using DES after first converting it into the `RAW` data type.
	This step is necessary because encrypt and decrypt functions and procedures in `DBMS_CRYPTO` package work on the `RAW` data type only.
- Shows how to create a 160-bit hash using SHA-1 algorithm.
- Demonstrates how MAC, a key-dependent one-way hash, can be computed using the MD5 algorithm. (Starting in Oracle Database release 21c, the MD5 algorithm has been deprecated.)

The `DBMS_CRYPTO.SQL` procedure follows:

```
DECLARE
    input_string     VARCHAR2(16) := 'tigertigertigert';
    raw_input        RAW(128) :=
UTL_RAW.CAST_TO_RAW(CONVERT(input_string,'AL32UTF8','US7ASCII'));
    key_string       VARCHAR2(8)  := 'scottsco';
    raw_key          RAW(128) :=
UTL_RAW.CAST_TO_RAW(CONVERT(key_string,'AL32UTF8','US7ASCII'));
    encrypted_raw    RAW(2048);
    encrypted_string VARCHAR2(2048);
    decrypted_raw    RAW(2048);
    decrypted_string VARCHAR2(2048); 
-- Begin testing Encryption: 
BEGIN
    dbms_output.put_line('> Input String                     : ' || 
    CONVERT(UTL_RAW.CAST_TO_VARCHAR2(raw_input),'US7ASCII','AL32UTF8'));
    dbms_output.put_line('> ========= BEGIN TEST Encrypt =========');
    encrypted_raw := dbms_crypto.Encrypt(
        src => raw_input, 
        typ => DBMS_CRYPTO.DES_CBC_PKCS5, 
        key => raw_key);
        dbms_output.put_line('> Encrypted hex value              : ' || 
        rawtohex(UTL_RAW.CAST_TO_RAW(encrypted_raw)));
decrypted_raw := dbms_crypto.Decrypt(
        src => encrypted_raw, 
        typ => DBMS_CRYPTO.DES_CBC_PKCS5, 
        key => raw_key);
    decrypted_string := 
    CONVERT(UTL_RAW.CAST_TO_VARCHAR2(decrypted_raw),'US7ASCII','AL32UTF8');
dbms_output.put_line('> Decrypted string output          : ' || 
        decrypted_string);
if input_string = decrypted_string THEN
    dbms_output.put_line('> String DES Encyption and Decryption successful');
END if;
dbms_output.put_line('');
dbms_output.put_line('> ========= BEGIN TEST Hash =========');
    encrypted_raw := dbms_crypto.Hash(
        src => raw_input, 
        typ => DBMS_CRYPTO.HASH_SH1);
dbms_output.put_line('> Hash value of input string       : ' || 
        rawtohex(UTL_RAW.CAST_TO_RAW(encrypted_raw)));
dbms_output.put_line('> ========= BEGIN TEST Mac =========');
    encrypted_raw := dbms_crypto.Mac(
        src => raw_input, 
        typ => DBMS_CRYPTO.HMAC_MD5, 
        key => raw_key);
dbms_output.put_line('> Message Authentication Code      : ' || 
        rawtohex(UTL_RAW.CAST_TO_RAW(encrypted_raw)));
dbms_output.put_line('');
dbms_output.put_line('> End of DBMS_CRYPTO tests  ');
END;
/
```

**Parent topic:** Examples of Using the Data Encryption API

#### 16.6.2 Example: AES 256-Bit Data Encryption and Decryption Procedures

You can use a PL/SQL block to encrypt and decrypt a predefined variable.

For the following example, the predefined variable is named `input_string` and it uses the AES 256-bit algorithm with Cipher Block Chaining and PKCS #5 padding:

```
declare
   input_string       VARCHAR2 (200) := 'Secret Message';
   output_string      VARCHAR2 (200);
   encrypted_raw      RAW (2000);             -- stores encrypted binary text
   decrypted_raw      RAW (2000);             -- stores decrypted binary text
   num_key_bytes      NUMBER := 256/8;        -- key length 256 bits (32 bytes)
   key_bytes_raw      RAW (32);               -- stores 256-bit encryption key 
   encryption_type    PLS_INTEGER :=          -- total encryption type
                            DBMS_CRYPTO.ENCRYPT_AES256
                          + DBMS_CRYPTO.CHAIN_CBC
                          + DBMS_CRYPTO.PAD_PKCS5;
begin
   DBMS_OUTPUT.PUT_LINE ('Original string: ' || input_string);
   key_bytes_raw := DBMS_CRYPTO.RANDOMBYTES (num_key_bytes);
   encrypted_raw := DBMS_CRYPTO.ENCRYPT
      (
         src => UTL_I18N.STRING_TO_RAW (input_string, 'AL32UTF8'),
         typ => encryption_type,
         key => key_bytes_raw
      );
    -- The encrypted value in the encrypted_raw variable can be used here:
   decrypted_raw := DBMS_CRYPTO.DECRYPT
      (
         src => encrypted_raw,
         typ => encryption_type,
         key => key_bytes_raw
      );
   output_string := UTL_I18N.RAW_TO_CHAR (decrypted_raw, 'AL32UTF8');
   DBMS_OUTPUT.PUT_LINE ('Decrypted string: ' || output_string);
end;
```

**Parent topic:** Examples of Using the Data Encryption API

#### 16.6.3 Example: Encryption and Decryption Procedures for BLOB Data

You can encrypt BLOB data.

The following sample PL/SQL program (`blob_test.sql`) shows how to encrypt and decrypt BLOB data. This example code does the following, and prints out its progress (or problems) at each step:

- Creates a table for the BLOB column
- Inserts the raw values into that table
- Encrypts the raw data
- Decrypts the encrypted data

The `blob_test.sql` procedure follows:

```
-- 1. Create a table for BLOB column:
create table table_lob (id number, loc blob);

-- 2. Insert 3 empty lobs for src/enc/dec:
insert into table_lob values (1, EMPTY_BLOB());
insert into table_lob values (2, EMPTY_BLOB());
insert into table_lob values (3, EMPTY_BLOB());

set echo on
set serveroutput on

declare
    srcdata    RAW(1000);
    srcblob    BLOB;
    encrypblob BLOB;
    encrypraw  RAW(1000);
    encrawlen  BINARY_INTEGER;
    decrypblob BLOB;
    decrypraw  RAW(1000);
    decrawlen  BINARY_INTEGER;
    
    leng       INTEGER;

begin
    
    -- RAW input data 16 bytes
    srcdata := hextoraw('6D6D6D6D6D6D6D6D6D6D6D6D6D6D6D6D');
    
    dbms_output.put_line('---');
    dbms_output.put_line('input is ' || srcdata);
    dbms_output.put_line('---');
    
    -- select empty lob locators for src/enc/dec
    select loc into srcblob from table_lob where id = 1;
    select loc into encrypblob from table_lob where id = 2;
    select loc into decrypblob from table_lob where id = 3;
    
    dbms_output.put_line('Created Empty LOBS');
    dbms_output.put_line('---');
    
    leng := DBMS_LOB.GETLENGTH(srcblob);
    IF leng IS NULL THEN
        dbms_output.put_line('Source BLOB Len NULL ');
    ELSE
        dbms_output.put_line('Source BLOB Len ' || leng);
    END IF;
    
    leng := DBMS_LOB.GETLENGTH(encrypblob);
    IF leng IS NULL THEN
        dbms_output.put_line('Encrypt BLOB Len NULL ');
    ELSE
        dbms_output.put_line('Encrypt BLOB Len ' || leng);
    END IF;
    
    leng := DBMS_LOB.GETLENGTH(decrypblob);
    IF leng IS NULL THEN
        dbms_output.put_line('Decrypt  BLOB Len NULL ');
    ELSE
        dbms_output.put_line('Decrypt BLOB Len ' || leng);
    END IF;
    
    -- 3. Write source raw data into blob:
    DBMS_LOB.OPEN (srcblob, DBMS_LOB.lob_readwrite);
    DBMS_LOB.WRITEAPPEND (srcblob, 16, srcdata);
    DBMS_LOB.CLOSE (srcblob);
    
    dbms_output.put_line('Source raw data written to source blob');
    dbms_output.put_line('---');
    
    leng := DBMS_LOB.GETLENGTH(srcblob);
    IF leng IS NULL THEN
        dbms_output.put_line('source BLOB Len NULL ');
    ELSE
        dbms_output.put_line('Source BLOB Len ' || leng);
    END IF;
    
    /*
    * Procedure Encrypt
    * Arguments: srcblob -> Source BLOB
    *            encrypblob -> Output BLOB for encrypted data
    *            DBMS_CRYPTO.AES_CBC_PKCS5 -> Algo : AES
    *                                         Chaining : CBC
    *                                         Padding : PKCS5
    *            256 bit key for AES passed as RAW
    *                ->
    hextoraw('000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F')
    *            IV (Initialization Vector) for AES algo passed as RAW
    *                -> hextoraw('00000000000000000000000000000000')
    */
    
    DBMS_CRYPTO.Encrypt(encrypblob,
                srcblob,
                DBMS_CRYPTO.AES_CBC_PKCS5,
                hextoraw ('000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F'),
                hextoraw('00000000000000000000000000000000'));
    
    
    dbms_output.put_line('Encryption Done');
    dbms_output.put_line('---');
    
    leng := DBMS_LOB.GETLENGTH(encrypblob);
    IF leng IS NULL THEN
        dbms_output.put_line('Encrypt BLOB Len NULL');
    ELSE
        dbms_output.put_line('Encrypt BLOB Len ' || leng);
    END IF;
    
    -- 4. Read encrypblob to a raw:
    encrawlen := 999;
    
    DBMS_LOB.OPEN (encrypblob, DBMS_LOB.lob_readwrite);
    DBMS_LOB.READ (encrypblob, encrawlen, 1, encrypraw);
    DBMS_LOB.CLOSE (encrypblob);
    
    dbms_output.put_line('Read encrypt blob to a raw');
    dbms_output.put_line('---');
    
    dbms_output.put_line('Encrypted data is (256 bit key) ' || encrypraw);
    dbms_output.put_line('---');
    
    /*
    * Procedure Decrypt
    * Arguments: encrypblob -> Encrypted BLOB to decrypt
    *            decrypblob -> Output BLOB for decrypted data in RAW
    *            DBMS_CRYPTO.AES_CBC_PKCS5 -> Algo : AES
    *                                         Chaining : CBC
    *                                         Padding : PKCS5
    *            256 bit key for AES passed as RAW (same as used during Encrypt)
    *                ->
    hextoraw('000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F')
    *            IV (Initialization Vector) for AES algo passed as RAW (same as
                 used during Encrypt)
    *                -> hextoraw('00000000000000000000000000000000')
    */
    
    DBMS_CRYPTO.Decrypt(decrypblob,
                encrypblob,
                DBMS_CRYPTO.AES_CBC_PKCS5,
                hextoraw
           ('000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F'),
                hextoraw('00000000000000000000000000000000'));
    
    leng := DBMS_LOB.GETLENGTH(decrypblob);
    IF leng IS NULL THEN
        dbms_output.put_line('Decrypt BLOB Len NULL');
    ELSE
        dbms_output.put_line('Decrypt BLOB Len ' || leng);
    END IF;
    
    -- Read decrypblob to a raw
    decrawlen := 999;
    
    DBMS_LOB.OPEN (decrypblob, DBMS_LOB.lob_readwrite);
    DBMS_LOB.READ (decrypblob, decrawlen, 1, decrypraw);
    DBMS_LOB.CLOSE (decrypblob);
    
    dbms_output.put_line('Decrypted data is (256 bit key) ' || decrypraw);
    dbms_output.put_line('---');
    
    DBMS_LOB.OPEN (srcblob, DBMS_LOB.lob_readwrite);
    DBMS_LOB.TRIM (srcblob, 0);
    DBMS_LOB.CLOSE (srcblob);
    
    DBMS_LOB.OPEN (encrypblob, DBMS_LOB.lob_readwrite);
    DBMS_LOB.TRIM (encrypblob, 0);
    DBMS_LOB.CLOSE (encrypblob);
    
    DBMS_LOB.OPEN (decrypblob, DBMS_LOB.lob_readwrite);
    DBMS_LOB.TRIM (decrypblob, 0);
    DBMS_LOB.CLOSE (decrypblob);
    
end;
/

truncate table table_lob;
drop table table_lob;
```

**Parent topic:** Examples of Using the Data Encryption API

### 16.7 Data Dictionary Views for Encrypted Data

Oracle Database provides data dictionary views to find information about encrypted data.

Table 16-5 Data Dictionary Views That Display Information about Encrypted Data

| View | Description |
| --- | --- |
| `ALL_ENCRYPTED_COLUMNS` | Describes encryption algorithm information for all encrypted columns in all tables accessible to the user |
| `DBA_ENCRYPTED_COLUMNS` | Describes encryption algorithm information for all encrypted columns in the database |
| `USER_ENCRYPTED_COLUMNS` | Describes encryption algorithm information for all encrypted columns in all tables in the schema of the user |
| `V$ENCRYPTED_TABLESPACES` | Displays information about the current pluggable database (PDB) tablespaces that are encrypted |
| `V$ENCRYPTION_WALLET` | Displays information on the status of the wallet and the wallet location for Transparent Data Encryption; applies to the current PDB only |
| `V$RMAN_ENCRYPTION_ALGORITHMS` | Displays supported encryption algorithms for the current PDB |