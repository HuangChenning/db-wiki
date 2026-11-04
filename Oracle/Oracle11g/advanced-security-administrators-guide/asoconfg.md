---
title: "Configuring Network Data Encryption and Integrity for Oracle Servers and Clients"
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/asoconfg.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## 9 Configuring Network Data Encryption and Integrity for Oracle Servers and Clients

This chapter describes how to configure native Oracle Net Services data [encryption](asogls.md) and [integrity](asogls.md) for Oracle Advanced Security. It contains the following topics:

## 9.1 Oracle Advanced Security Encryption

The purpose of a secure cryptosystem is to convert [plaintext](asogls.md) data into unintelligible [ciphertext](asogls.md) based on a key, in such a way that it is very hard (computationally infeasible) to convert ciphertext back into its corresponding plaintext without knowledge of the correct key. In a symmetric cryptosystem, the same key is used both for encryption and decryption of the same data. Oracle Advanced Security provides the Advanced Encryption Standard (AES) and 3DES symmetric cryptosystems for protecting the confidentiality of Oracle Net Services traffic.

This section describes data encryption algorithms available in the current release of Oracle Advanced Security:

- Advanced Encryption Standard
- Triple-DES Support
- Note:
	Prior to Release 8.1.7, Oracle Advanced Security provided three editions: Domestic, Upgrade, and Export each with different key lengths. This release now contains a complete complement of the available encryption algorithms and key lengths, previously only available in the Domestic edition. Users deploying prior versions of the product can obtain the Domestic edition for a specific product release.

### 9.1.1 Advanced Encryption Standard

Oracle Advanced Security supports the Federal Information Processing Standard (FIPS) encryption algorithm, Advanced Encryption Standard (AES). AES can be used by all U.S. government organizations and businesses to protect sensitive data over a network. This encryption algorithm defines three standard key lengths, which are 128-bit, 192-bit, and 256-bit. All versions operate in outer [Cipher Block Chaining (CBC)](asogls.md) mode.

### 9.1.2 Triple-DES Support

Oracle Advanced Security supports Triple-DES encryption (3DES), which encrypts message data with three passes of the DES algorithm. 3DES provides a high degree of message security, but with a performance penalty. The magnitude of the performance penalty depends on the speed of the processor performing the encryption. 3DES typically takes three times as long to encrypt a data block when compared to the standard DES algorithm.

3DES is available in two-key and three-key versions, with effective key lengths of 112-bits and 168-bits, respectively. Both versions operate in outer [Cipher Block Chaining (CBC)](asogls.md) mode.

Note:

3DES has been replaced by AES as the encryption algorithm of choice for commercial and government uses

## 9.2 Oracle Advanced Security Data Integrity

Encryption of network data provides data privacy so that unauthorized parties are not able to view plaintext data as it passes over the network. Oracle Advanced Security also provides protection against two forms of active attack. Table 9-1 provides information about these attacks.

Table 9-1 Two Forms of Attack

| Type of Attack | Explanation |
| --- | --- |
| Data modification attack | An unauthorized party intercepting data in transit, altering it, and retransmitting it is a data modification attack. For example, intercepting a $100 bank deposit, changing the amount to $10,000, and retransmitting the higher amount is a data modification attack. |
| Replay attack | Repetitively retransmitting an entire set of valid data is a replay attack, such as intercepting a $100 bank withdrawal and retransmitting it ten times, thereby receiving $1,000. |

### 9.2.1 Data Integrity Algorithms Supported

Oracle Advanced Security lets you select a keyed, sequenced implementation of the Secure Hash Algorithm (SHA-1) to protect against both of these forms of attack. Both of these hash algorithms create a checksum that changes if the data is altered in any way. This protection operates independently from the encryption process so you can enable data integrity with or without enabling encryption.

See Also:

"Configuring Integrity on the Client and the Server"

## 9.3 Diffie-Hellman Based Key Negotiation

Secure key distribution is difficult in a multiuser environment. Oracle Advanced Security uses the well known [Diffie-Hellman key negotiation algorithm](asogls.md) to perform secure key distribution for both encryption and data integrity.

When encryption is used to protect the security of encrypted data, keys must be changed frequently to minimize the effects of a compromised key. Accordingly, the Oracle Advanced Security key management function changes the session key with every session.

### 9.3.1 Authentication Key Fold-in

The purpose of Authentication Key Fold-in is to defeat a possible third-party attack (historically called the man-in-the-middle attack) on the Diffie-Hellman key negotiation. It strengthens the session key significantly by combining a shared secret, known only to the client and the server, with the original session key negotiated by Diffie-Hellman.

The client and the server begin communicating using the session key generated by Diffie-Hellman. When the client authenticates to the server, they establish a shared secret that is only known to both parties. Oracle Advanced Security combines the shared secret and the Diffie-Hellman session key to generate a stronger session key designed to defeat a man-in-the-middle attack.

Note:

The authentication key fold-in function is an imbedded feature of Oracle Advanced Security and requires no configuration by the system or network administrator.

## 9.4 How To Configure Data Encryption and Integrity

This section describes how to configure Oracle Advanced Security native Oracle Net Services encryption and integrity and presumes the prior installation of Oracle Net Services.

The network or security administrator sets up the encryption and integrity configuration parameters. The profile on client and server systems using data encryption and integrity (`sqlnet.ora` file) must contain some or all of the parameters listed in this section, under the following topics:

- About Activating Encryption and Integrity
- About Negotiating Encryption and Integrity
- Configuring Encryption and Integrity Parameters Using Oracle Net Manager
	See Also:
	[Chapter 13, "Configuring Secure Sockets Layer Authentication"](asossl.md), to configure the SSL feature for encryption, integrity, and authentication

### 9.4.1 About Activating Encryption and Integrity

In any network connection, it is possible for both the client and server to support more than one encryption algorithm and more than one integrity algorithm. When a connection is made, the server selects which algorithm to use, if any, from those algorithms specified in the `sqlnet.ora` files.

The server searches for a match between the algorithms available on both the client and the server, and picks the first algorithm in its own list that also appears in the client list. If one side of the connection does not specify an algorithm list, all the algorithms installed on that side are acceptable. The connection fails with error message `ORA-12650` if either side specifies an algorithm that is not installed.

Encryption and integrity parameters are defined by modifying a `sqlnet.ora` file on the clients and the servers on the network.

You can choose to configure any or all of the available Oracle Advanced Security encryption algorithms (Table 9-3), and the available integrity algorithm (SHA-1). Only one encryption algorithm and one integrity algorithm are used for each connect session.

Note:

Oracle Advanced Security selects the first encryption algorithm and the first integrity algorithm enabled on the client and the server. Oracle recommends that you select algorithms and key lengths in the order in which you prefer negotiation, choosing the strongest key length first.

See Also:

[Appendix A, "Data Encryption and Integrity Parameters"](asoappa.md)

### 9.4.2 About Negotiating Encryption and Integrity

To negotiate whether to turn on encryption or integrity, you can specify four possible values for the Oracle Advanced Security encryption and integrity configuration parameters. The four values are listed in the order of increasing security. The value `REJECTED` provides the minimum amount of security between client and server communications, and the value `REQUIRED` provides the maximum amount of network security:

- REJECTED
- ACCEPTED
- REQUESTED
- REQUIRED

The default value for each of the parameters is `ACCEPTED.`

Oracle Database servers and clients are set to `ACCEPT` encrypted connections out of the box. This means that you can enable the desired encryption and integrity settings for a connection pair by configuring just one side of the connection, server-side or client-side.

So, for example, if there are many Oracle clients connecting to an Oracle database, you can configure the required encryption and integrity settings for all these connections by making the appropriate sqlnet.ora changes at the server end. You do not need to implement configuration changes for each client separately.

#### 9.4.2.1 REJECTED

Select this value if you do not elect to enable the security service, even if required by the other side.

In this scenario, this side of the connection specifies that the security service is not permitted. If the other side is set to REQUIRED, the connection terminates with error message `ORA-12650`. If the other side is set to REQUESTED, ACCEPTED, or REJECTED, the connection continues without error and without the security service enabled.

#### 9.4.2.2 ACCEPTED

Select this value to enable the security service if required or requested by the other side.

In this scenario, this side of the connection does not require the security service, but it is enabled if the other side is set to REQUIRED or REQUESTED. If the other side is set to REQUIRED or REQUESTED, and an encryption or integrity algorithm match is found, the connection continues without error and with the security service enabled. If the other side is set to REQUIRED and no algorithm match is found, the connection terminates with error message `ORA-12650`.

If the other side is set to REQUESTED and no algorithm match is found, or if the other side is set to ACCEPTED or REJECTED, the connection continues without error and without the security service enabled.

#### 9.4.2.3 REQUESTED

Select this value to enable the security service if the other side permits it.

In this scenario, this side of the connection specifies that the security service is desired but not required. The security service is enabled if the other side specifies ACCEPTED, REQUESTED, or REQUIRED. There must be a matching algorithm available on the other side, otherwise the service is not enabled. If the other side specifies REQUIRED and there is no matching algorithm, the connection fails.

#### 9.4.2.4 REQUIRED

Select this value to enable the security service or preclude the connection.

In this scenario, this side of the connection specifies that the security service must be enabled. The connection fails if the other side specifies REJECTED or if there is no compatible algorithm on the other side.

Table 9-2 shows whether the security service is enabled, based on a combination of client and server configuration parameters. If either the server or client has specified REQUIRED, the lack of a common algorithm causes the connection to fail. Otherwise, if the service is enabled, lack of a common service algorithm results in the service being disabled.

Table 9-2 Encryption and Data Integrity Negotiations

| Client Setting | Server Setting | Encryption and Data Negotiation |
| --- | --- | --- |
| REJECTED | REJECTED | OFF |
| ACCEPTED | REJECTED | OFF |
| REQUESTED | REJECTED | OFF |
| REQUIRED | REJECTED | Connection fails |
| REJECTED | ACCEPTED | OFF |
| ACCEPTED | ACCEPTED | OFF <sup>Foot 1</sup> |
| REQUESTED | ACCEPTED | ON |
| REQUIRED | ACCEPTED | ON |
| REJECTED | REQUESTED | OFF |
| ACCEPTED | REQUESTED | ON |
| REQUESTED | REQUESTED | ON |
| REQUIRED | REQUESTED | ON |
| REJECTED | REQUIRED | Connection fails |
| ACCEPTED | REQUIRED | ON |
| REQUESTED | REQUIRED | ON |
| REQUIRED | REQUIRED | ON |

<sup>Footnote 1</sup> This value defaults to OFF. Cryptography and data integrity are not enabled until the user changes this parameter by using Oracle Net Manager or by modifying the `sqlnet.ora` file.

### 9.4.3 Configuring Encryption and Integrity Parameters Using Oracle Net Manager

You can set up or change encryption and integrity parameter settings using Oracle Net Manager. This section describes the following topics:

- Configuring Encryption on the Client and the Server
- Configuring Integrity on the Client and the Server
	See Also:
	- [Appendix A, "Data Encryption and Integrity Parameters"](asoappa.md), for valid encryption algorithms
	- Oracle Net Manager online help, for more detailed configuration information

#### 9.4.3.1 Configuring Encryption on the Client and the Server

Use Oracle Net Manager to configure encryption on the client and on the server (See Also ["Starting Oracle Net Manager"](asotools.md)). The steps to configure Oracle Net Manager are:

1. Navigate to the Oracle Advanced Security profile (For details, refer to ["Navigating to the Oracle Advanced Security Profile"](asotools.md)).
2. Click the Encryption tab.
3. Select CLIENT or SERVER option from the Integrity box.
4. From the Encryption Type list, select one of the following:
	- `REQUESTED`
		- `REQUIRED`
		- `ACCEPTED`
		- `REJECTED`
5. (Optional) In the Encryption Seed field, enter between 10 and 70 random characters. The encryption seed for the client should not be the same as that for the server.
6. Select an encryption algorithm in the Available Methods list. Move it to the Selected Methods list by choosing the right arrow (>). Repeat for each additional method you want to use.
7. Select File, Save Network Configuration. The `sqlnet.ora` file is updated.
8. Repeat this procedure to configure encryption on the other system. The `sqlnet.ora` file on the two systems should contain the following entries:
	- On the server:
		```
		SQLNET.ENCRYPTION_SERVER = [accepted | rejected | requested | required]
		SQLNET.ENCRYPTION_TYPES_SERVER = (valid_encryption_algorithm [,valid_encryption_algorithm])
		```
	- On the client:
		```
		SQLNET.ENCRYPTION_CLIENT = [accepted | rejected | requested | required]
		SQLNET.ENCRYPTION_TYPES_CLIENT = (valid_encryption_algorithm [,valid_encryption_algorithm])
		```

Valid encryption algorithms and their associated legal values are summarized by Table 9-3:

Table 9-3 Valid Encryption Algorithms

| Algorithm Name | Legal Value |
| --- | --- |
| RC4 256-bit key | RC4\_256 |
| RC4 128-bit key | RC4\_128 |
| RC4 56-bit key | RC4\_56 |
| RC4 40-bit key | RC4\_40 |
| AES 256-bit key | AES256 |
| AES 192-bit key | AES192 |
| AES 128-bit key | AES128 |
| 3-key 3DES | 3DES168 |
| 2-key 3DES | 3DES112 |
| DES 56-bit key | DES |
| DES 40-bit key | DES40 |

#### 9.4.3.2 Configuring Integrity on the Client and the Server

Use Oracle Net Manager to configure data integrity on the client and on the server.

See Also:

["Starting Oracle Net Manager"](asotools.md)

1. Navigate to the Oracle Advanced Security profile. (For details, refer to ["Navigating to the Oracle Advanced Security Profile"](asotools.md)) The Oracle Advanced Security tabbed window is displayed.
2. Click the Integrity tab.
3. Depending upon which system you are configuring, select the Server or Client from the Integrity box.
4. From the Checksum Level list, select one of the following checksum level values:
	- REQUESTED
		- REQUIRED
		- ACCEPTED
		- REJECTED
5. Select an integrity algorithm in the Available Methods list. Move it to the Selected Methods list by choosing the right arrow (>). Repeat for each additional method you want to use.
6. Select File, Save Network Configuration. The `sqlnet.ora` file is updated.
7. Repeat this procedure to configure integrity on the other system. The `sqlnet.ora` file on the two systems should contain the following entries:
	- On the server:
		```
		SQLNET.CRYPTO_CHECKSUM_SERVER = [accepted | rejected | requested | required]
		SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER = (valid_crypto_checksum_algorithm [,valid_crypto_checksum_algorithm])
		```
		- On the client:
		```
		SQLNET.CRYPTO_CHECKSUM_CLIENT = [accepted | rejected | requested | required]
		SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT = (valid_crypto_checksum_algorithm [,valid_crypto_checksum_algorithm])
		```

The valid integrity algorithm is SHA-1 and its associated legal value is `SHA1`.