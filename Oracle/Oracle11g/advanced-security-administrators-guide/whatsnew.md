---
title: "What's New in Oracle Advanced Security?"
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/whatsnew.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

This section describes new features of Oracle Advanced Security 11g Release 2 (11.2) and provides pointers to additional information.

## Oracle Database 11g Release 2 (11.2.0.4) New Features in Oracle Advanced Security

This release includes the following new features:

- Oracle Data Redaction for Masking Data
- Filtering for Secure Sockets Layer Certificates

### Oracle Data Redaction for Masking Data

This release includes Oracle Data Redaction, which gives you the ability to disguise (mask) data from low-privileged users or applications. For example, suppose you have the following credit card numbers:

- `5105 1051 0510 5100`
- `5111 1111 1111 1118`
- `5454 5454 5454 5454`

You can use Data Redaction to disguise the last four digits as follows:

- `5105 1051 0510 ****`
- `5111 1111 1111 ****`
- `5454 5454 5454 ****`

The data is redacted at run time, that is, it is hidden when the user accesses the page containing the data, but it is not hidden in the database. This enables the sensitive data to be processed normally, and it preserves the back-end referential integrity and constraints for the data. You have the option of redacting the data partially so that some of the original data is preserved (such as the last four digits of a credit card number), entirely by replacing it with a fixed value, or by replacing the data with an encrypted value. You also can easily apply Oracle Data Redaction policies throughout the databases in your enterprise.

See [Part I, "Oracle Data Redaction"](asopart1b.md) for more information.

### Filtering for Secure Sockets Layer Certificates

Starting with this release, you can use the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter in the `sqlnet.ora` file to select a Secure Sockets Layer certificate to be used automatically to authenticate clients. For example, suppose you have multiple certificates for a smart card but only one of the certificates has an extended key usage field of `client authentication`. In the application, a certificate chooser dialog box would appear, prompting the user to select the type of authentication. Because the type of authentication would always be for clients, the `SQLNET.SSL_EXTENDED_KEY_USAGE` parameter can enable the application to bypass this dialog box and automatically choose client authentication. As a result, the user has fewer steps to perform in a task, thereby making the user's job easier and more efficient.

See ["Step 3G: Specify the Certificate to Use for Authentication on the Client (Optional)"](asossl.md) for more information.

## Oracle Database 11g Release 2 (11.2.0.3) New Features in Oracle Advanced Security

This release includes the following new features:

- Support for SHA-2 Certificate Signatures
- Support for PIN and Multiple Certificates on Smart Card
- TDE Hardware Acceleration for Solaris

### Support for SHA-2 Certificate Signatures

This feature introduces support for SHA-2 (256-bit) signed certificates that are used by the database for network encryption and authentication.

These certificates are issued by a separate certificate authority (CA), and are exchanged between the database and a client when a secure database connection is being established.

### Support for PIN and Multiple Certificates on Smart Card

This feature introduces support for authenticating to the database using Common Access Cards (CAC, HSPD-12) that contain multiple certificates.

When a database user inserts a card containing one or more digital certificates into a card reader, the database attempts to intelligently select which certificate to read. If the database cannot determine which certificate to read, a selection box is presented on Windows clients. The user also must manually enter the correct PIN.

### TDE Hardware Acceleration for Solaris

Transparent Data Encryption (TDE) can automatically detect whether the database host machine includes specialized cryptographic silicon that accelerates the encryption and decryption processing. When detected, TDE uses the specialized silicon for cryptographic processing, accelerating the overall cryptographic performance significantly.

In prior releases, cryptographic hardware acceleration for TDE was only available on Intel Xeon, and only for Linux. Starting with release 11.2.0.3, it works with the current versions of Solaris 11 running on both SPARC T-Series and Intel Xeon.

## Oracle Database 11g Release 2 (11.2) New Features in Oracle Advanced Security

This release includes the following new features:

- Enhanced TDE Tablespace Encryption
- TDE Supports Intel Advanced Encryption Standard New Instructions (Intel AES-NI)
- Internet Protocol Version 6 (IPv6) Support
- Kerberos Enhancements

### Enhanced TDE Tablespace Encryption

Oracle Database 11g Release 2 (11.2) implements the following enhancements to TDE Tablespace Encryption:

- A unified master encryption key is used for both Transparent Data Encryption (TDE) Column Encryption and TDE Tablespace Encryption.
- The unified master encryption key can optionally be stored in a hardware security module. This enables you to use the TDE Tablespace Encryption feature along with hardware security modules.
- You can reset (`rekey`) the unified master encryption key. This provides enhanced security and helps meet security and compliance requirements.

See Also:

["Encrypting Entire Tablespaces"](asotrans.md)

### TDE Supports Intel Advanced Encryption Standard New Instructions (Intel AES-NI)

Transparent Data Encryption (TDE) now supports Intel AES-NI. Oracle Database 11g Release 2 (11.2) running on Intel Xeon 5600 series processor-based servers with Intel AES-NI shows a multifold increase in TDE encryption and decryption speed.

According to benchmark results, TDE shows a 10x speedup of AES encryption processing rate and an 8x speedup of decryption processing rate, using 256 bit keys, on Intel Xeon X5680 processor utilizing AES-NI as compared to Intel Xeon X5560 processor without AES-NI.

### Internet Protocol Version 6 (IPv6) Support

Oracle Advanced Security fully supports Internet Protocol Version 6 (IPv6) networks.

### Kerberos Enhancements

The Oracle Kerberos authentication mechanism now supports the Microsoft Windows Server 2003 constrained delegation feature. The middle tier can use the Kerberos adapter to authenticate to the Oracle Database without providing the user's forwarded Kerberos credentials.

A user can authenticate to the middle tier using a non-Kerberos authentication mechanism. The middle tier authenticates to the backend Oracle Database using the Kerberos authentication mechanism on behalf of the user.

See Also:

Microsoft documentation for more information on the Microsoft Windows Server 2003 constrained delegation feature

## Oracle Database 11g Release 1 (11.1) New Features in Oracle Advanced Security

This release includes the following new features:

- Enhanced Transparent Data Encryption
- Kerberos Authentication More Secure and Manageable

### Enhanced Transparent Data Encryption

Transparent Data Encryption enables you to encrypt data in columns without having to manage the encryption key. Businesses can protect sensitive data in their databases without having to make changes to their applications.

Oracle Advanced Security uses industry standard encryption algorithms including AES and 3DES to encrypt columns that have been marked for encryption. Key Management is handled by the database. SQL interfaces to Key Management hide the complexity of encryption.

You can now encrypt entire tablespaces using Tablespace Encryption. All objects created in the encrypted tablespace are automatically encrypted. See ["TDE Tablespace Encryption"](asotrans.md) in for more information.

Transparent Data Encryption now enables you to use a hardware security module (HSM) to store the master encryption key. This allows for enhanced security. See ["Using Hardware Security Modules with TDE"](asotrans.md) for more information.

See Also:

["Supported Encryption Algorithms"](asointro.md) for more information on the encryption algorithms that are supported.

[Chapter 8, "Securing Stored Data Using Transparent Data Encryption"](asotrans.md) for more information on implementing and using Transparent Data Encryption.

### Kerberos Authentication More Secure and Manageable

The Kerberos implementation now makes use of secure encryption algorithms like `3DES` and `AES` in place of `DES`. This makes using Kerberos more secure. The Kerberos authentication mechanism in Oracle Database now supports the following encryption types:

- `DES3-CBC-SHA` (`DES3` algorithm in `CBC` mode with `HMAC-SHA1` as checksum)
- `AES128-CTS` (`AES` algorithm with 128-bit key in `CTS` mode with `HMAC-SHA1` as checksum)
- `AES256-CTS` (`AES` algorithm with 256-bit key in `CTS` mode with `HMAC-SHA1` as checksum)

The Kerberos implementation has been enhanced to interoperate smoothly with Microsoft and MIT Key Distribution Centers.

The Kerberos prinicipal name can now contain more than 30 characters. It is no longer restricted by the number of characters allowed in a database user name.

Note:

In this release, the features of Multiplexing and Connection Pooling do not work with SSL transport. Refer to Oracle Database JDBC Developer's Guide and Reference for details of encryption support available in JDBC.