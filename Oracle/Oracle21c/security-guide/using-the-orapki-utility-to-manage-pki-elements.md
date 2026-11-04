---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/using-the-orapki-utility-to-manage-pki-elements.html
tags:
  - oracle
  - 21c
  - security-guide
---

You can use the `orapki` command line utility and sqlnet.ora parameters to manage public key infrastructure (PKI) elements.

- Uses of the orapki Utility  
	The `orapki` utility manages public key infrastructure (PKI) elements, such as wallets and certificate revocation lists, from the command line.
- orapki Utility Syntax  
	The `orapki` utility syntax specifies an Oracle wallet, a certificate revocation list, or a PKI digital certificate.
- Creating Signed Certificates for Testing Purposes  
	The `orapki` utility provides a convenient, lightweight way to create signed certificates for testing purposes.
- Viewing a Certificate  
	After you create a certificate, you can use the `orapki` utility to view it.
- Controlling MD5 and SHA-1 Certificate Use  
	You can use the `sqlnet.ora` file to control whether MD5 and SHA-1 signed certificates are accepted.
- Managing Oracle Wallets with orapki Utility  
	The `orapki` utility can create, view, modify wallets; it can add and export certificates and certificate requests.
- Management of Certificate Revocation Lists (CRLs) with orapki Utility  
	You must manage certificate revocation lists (CRLs) with the `orapki` utility.
- orapki Usage  
	Examples of `orapki` commands include creating wallets, user certificates, and wallets with self-signed certificates, and exporting certificates.
- orapki Utility Commands Summary  
	The `orapki` commands perform a variety of wallet, certificate revocation lists (CRL), and certificate management tasks.

**Parent topic:** [Appendixes](part_7.md)

### F.1 Uses of the orapki Utility

The `orapki` utility manages public key infrastructure (PKI) elements, such as wallets and certificate revocation lists, from the command line.

This way, you can automate these tasks by using scripts. Providing a way to incorporate the management of PKI elements into scripts makes it possible to automate many of the routine tasks of maintaining a PKI.

You can use the `orapki` command-line utility to perform the following tasks:

- Creating and viewing signed certificates for testing purposes
- Manage Oracle wallets (except for Transparent Data Encryption keystores):
	- Create and display Oracle wallets
		- Add and remove certificate requests
		- Add and remove certificates
		- Add and remove trusted certificates
- Manage certificate revocation lists (CRLs):
	- Renaming CRLs with a hash value for certificate validation
		- Uploading, listing, viewing, and deleting CRLs in Oracle Internet Directory

Note:

The use of PKI encryption with Transparent Data Encryption is deprecated. To configure Transparent Data Encryption, use the `ADMINISTER KEY MANAGEMENT` SQL statement.

### F.2 orapki Utility Syntax

The `orapki` utility syntax specifies an Oracle wallet, a certificate revocation list, or a PKI digital certificate.

The syntax of the `orapki` command-line utility is as follows:

```
orapki module command -parameter value
```

In this specification, `module` can be `wallet` (Oracle wallet), `crl` (certificate revocation list), or `cert` (PKI digital certificate). The available commands depend on the `module` you are using.

For example, if you are working with a `wallet`, then you can add a certificate or a key to the wallet with the `add` command. The following example adds the user certificate located at `/private/lhale/cert.txt` to the wallet located at `$ORACLE_HOME/wallet/ewallet.p12`:

```
orapki wallet add -wallet $ORACLE_HOME/wallet/ewallet.p12 -user_cert -cert /private/lhale/cert.txt
```

**Parent topic:** Managing Public Key Infrastructure (PKI) Elements

### F.3 Creating Signed Certificates for Testing Purposes

The `orapki` utility provides a convenient, lightweight way to create signed certificates for testing purposes.

- To create a signed certificate for testing purposes, use the `orapki cert create` command.
	```
	orapki cert create [-wallet wallet_location] -request certificate_request_location -cert certificate_location -validity number_of_days [-summary]
	```

This command creates a signed certificate from the certificate request. The `-wallet` parameter specifies the wallet containing the user certificate and private key that will be used to sign the certificate request. The `-validity` parameter specifies the number of days, starting from the current date, that this certificate will be valid. Specifying a certificate and certificate request is mandatory for this command.

**Parent topic:** Managing Public Key Infrastructure (PKI) Elements

### F.4 Viewing a Certificate

After you create a certificate, you can use the `orapki` utility to view it.

- To view a certificate, use the `orapki cert display` command.
	```
	orapki cert display -cert certificate_location [-summary | -complete]
	```

This command enables you to view a test certificate that you have created with `orapki`. You can choose either `-summary` or `-complete`, which determines how much detail the command will display. If you choose `-summary`, the command will display the certificate and its expiration date. If you choose `-complete`, it will display additional certificate information, including the serial number and public key.

**Parent topic:** Managing Public Key Infrastructure (PKI) Elements

### F.5 Controlling MD5 and SHA-1 Certificate Use

You can use the `sqlnet.ora` file to control whether MD5 and SHA-1 signed certificates are accepted.

To control whether the MD5 and SHA-1 signed certificates are accepted, you can edit the `sqlnet.ora` file to enable or disable their use.

Note:

MD5 is deprecated in this release. To transition your Oracle Database environment to use stronger algorithms, download and install the patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2).

1. Log in to the server where the Oracle database resides.
2. Edit the `sqlnet.ora` file.
	By default, the `sqlnet.ora` file is located in the `$ORACLE_HOME/dbs` directory or in the location set by the `TNS_ADMIN` environment variable.
3. Set the following parameters:
	- `ACCEPT_MD5_CERTS` controls the use of MD5 certificates. The default is `FALSE`. This parameter replaces the `ORACLE_SSL_ALLOW_MD5_CERT_SIGNATURES` environment variable.
		- `ACCEPT_SHA1_CERTS` controls the use of SHA-1 certificates. The default is `TRUE`.

**Parent topic:** Managing Public Key Infrastructure (PKI) Elements

### F.6 Managing Oracle Wallets with orapki Utility

The `orapki` utility can create, view, modify wallets; it can add and export certificates and certificate requests.

- About Managing Wallets with orapki  
	You should understand the `orapki` command-line utility syntax used to create and manage Oracle wallets.
- Creating, Viewing, and Modifying Wallets with orapki  
	You can use `orapki` to perform a range of management activities with Oracle wallets.
- Adding Certificates and Certificate Requests to Oracle Wallets with orapki  
	You can use the `orapki` utiltiy to perform a range of certificate-related tasks.
- Importing a User-Supplied or Trusted Certificate into an Oracle Wallet  
	You can add a user-supplied or trusted certificate to an Oracle wallet.
- Exporting Certificates and Certificate Requests from Oracle Wallets with orapki  
	You can use the `orapki` utility to export certificates and certificate requests from Oracle wallets.

**Parent topic:** Managing Public Key Infrastructure (PKI) Elements

#### F.6.1 About Managing Wallets with orapki

You should understand the `orapki` command-line utility syntax used to create and manage Oracle wallets.

You can use the `orapki` utility `wallet` module commands in scripts to automate the wallet creation process. For example, you can create PKCS#12 wallets and auto-login wallets. You can create auto-login wallets that are associated with PKCS#12 wallets or auto-login wallets that are local to the computer on which they were created and the user who created them. You can view wallets, modify wallet passwords, and convert wallets to use the AES256 algorithm.

Note:

The `-wallet` parameter is mandatory for all `wallet` module commands.

**Parent topic:** Managing Oracle Wallets with orapki Utility

#### F.6.2 Creating, Viewing, and Modifying Wallets with orapki

You can use `orapki` to perform a range of management activities with Oracle wallets.

- Creating a PKCS#12 Wallet  
	You can use the `orapki` utility to create a PKCS#12 Oracle wallet.
- Using OpenSSL to Create a PKCS#12 Wallet That Has a Certificate Chain  
	You can use the OpenSSL utility to create an PKCS#12 wallet so that it has a certificate chain.
- Creating an Auto-Login Wallet  
	You can use the `orapki` utility to create an auto-login wallet.
- Creating an Auto-Login Wallet That Is Associated with a PKCS#12 Wallet  
	You can create an auto-login wallet that is associated with a PKCS#12 wallet.
- Creating an Auto-Login Wallet That Is Local to the Computer and User Who Created It  
	The `orapki` utility can create an auto-login wallet that is local to the computer of the user who created it.
- Viewing a Wallet  
	You can use the `orapki` utility to view a wallet.
- Modifying the Password for a Wallet  
	You can use the `orapki` utility to modify the password of a wallet.
- Converting an Oracle Wallet to Use the AES256 Algorithm  
	By default, an Oracle wallet that was created with the `ADMINISTER KEY MANAGEMENT` or `ALTER SYSTEM` statement is encrypted with AES256.

**Parent topic:** Managing Oracle Wallets with orapki Utility

##### F.6.2.1 Creating a PKCS#12 Wallet

You can use the `orapki` utility to create a PKCS#12 Oracle wallet.

- To create an Oracle PKCS#12 wallet (`ewallet.p12`), use the `orapki wallet create` command.
	```
	orapki wallet create -wallet wallet_location [-pwd password]
	```

This command prompts you to enter and reenter a wallet password, if no password has been specified on the command line. It creates a wallet in the location specified for `-wallet`.

Note:

The default algorithm is AES256. For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password only when prompted to do so.

**Parent topic:** Creating, Viewing, and Modifying Wallets with orapki

##### F.6.2.2 Using OpenSSL to Create a PKCS#12 Wallet That Has a Certificate Chain

You can use the OpenSSL utility to create an PKCS#12 wallet so that it has a certificate chain.

1. For example:
	```
	cat root.cer sub.cer > ca.certs
	```
	In this example, `root.cer` is the root certificate.
2. Run `openssl` to create the PKCS#12 wallet.
	```
	openssl pkcs12 -export -nodes -certfile ca.certs -inkey user.key -in user.cer
	```
3. When prompted, provide a password for the wallet. Ensure that this password at at least 8 characters with an alphnumeric character mix.

For more information about how OpenSSL works with PKCS#12 wallets, visit [https://www.openssl.org/](https://www.openssl.org/) and search for "pkcs12".

**Parent topic:** Creating, Viewing, and Modifying Wallets with orapki

##### F.6.2.3 Creating an Auto-Login Wallet

You can use the `orapki` utility to create an auto-login wallet.

- To create an auto-login wallet (`cwallet.sso`), which does not need a password to open the wallet, use the `orapki wallet create` command.
	```
	orapki wallet create -wallet wallet_location -auto_login_only
	```

You can modify or delete the wallet without using a password. File system permissions provide the necessary security for such auto-login wallets.

You cannot move local auto-login wallets to another computer. They must be used on the host on which they are created.

Even though a local auto-login wallet does not need a password to open, you must supply the password for the associated PKCS#12 wallet in order to modify or delete the wallet. Any update to the PKCS#12 wallet also updates the associated auto-login wallet.

**Parent topic:** Creating, Viewing, and Modifying Wallets with orapki

##### F.6.2.4 Creating an Auto-Login Wallet That Is Associated with a PKCS#12 Wallet

You can create an auto-login wallet that is associated with a PKCS#12 wallet.

The auto-login wallet does not need a password to open.

However, you must supply the password for the associated PKCS#12 wallet in order to modify or delete the wallet. Any update to the PKCS#12 wallet also updates the associated auto-login wallet.

- To create an auto-login wallet (`cwallet.sso`) that is associated with a PKCS#12 wallet (`ewallet.p12`), use the `orapki wallet create` command.
	```
	orapki wallet create -wallet wallet_location -auto_login [-pwd wallet_password]
	```

This command creates a wallet with auto-login enabled (`cwallet.sso`) and associates it with a PKCS#12 wallet (`ewallet.p12`). The command prompts you to enter the password for the PKCS#12 wallet, if no password has been specified at the command line.

If the `wallet_location` already contains a PKCS#12 wallet, then auto-login is enabled for it. You must supply the password for the existing PKCS#12 wallet in order to enable auto-login for it.

If the `wallet_location` does not contain a PKCS#12 wallet, then a new PKCS#12 wallet is created. You must specify a password for the new PKCS#12 wallet.

If you want to turn the auto-login feature off for a PKCS#12 wallet, then use Oracle Wallet Manager.

##### F.6.2.5 Creating an Auto-Login Wallet That Is Local to the Computer and User Who Created It

The `orapki` utility can create an auto-login wallet that is local to the computer of the user who created it.

- To create a local auto-login wallet that is local to both the computer on which it is created and the user who created it, use the following command:
	```
	orapki wallet create -wallet wallet_location -auto_login_local [-pwd wallet_password]
	```

This command creates an auto-login wallet (`cwallet.sso`). It associates it with a PKCS#12 wallet (`ewallet.p12`). The command prompts you to enter the password for the PKCS#12 wallet, if no password has been specified at the command line.

**Parent topic:** Creating, Viewing, and Modifying Wallets with orapki

##### F.6.2.6 Viewing a Wallet

You can use the `orapki` utility to view a wallet.

- To view an Oracle wallet, use the `orapki wallet display` command.
	```
	orapki wallet display -wallet wallet_location
	```

This command displays the certificate requests, user certificates, and trusted certificates contained in the wallet, which must be a binary `PKCS12` file, with extension `.p12`. Other files will fail.

**Parent topic:** Creating, Viewing, and Modifying Wallets with orapki

##### F.6.2.7 Modifying the Password for a Wallet

You can use the `orapki` utility to modify the password of a wallet.

- To change the wallet password, use the `orapki wallet change_pwd` command.
	```
	orapki wallet change_pwd -wallet wallet_location [-oldpwd wallet_password ] [-newpwd wallet_password]
	```

This command changes the current wallet password to the new password. The command prompts you for the old and new passwords if no password is supplied at the command line.

Note:

For security reasons, Oracle recommends that you do not specify the password options at the command line. You should supply the password when prompted to do so.

**Parent topic:** Creating, Viewing, and Modifying Wallets with orapki

##### F.6.2.8 Converting an Oracle Wallet to Use the AES256 Algorithm

By default, an Oracle wallet that was created with the `ADMINISTER KEY MANAGEMENT` or `ALTER SYSTEM` statement is encrypted with AES256.

If you are using an older wallet that is encrypted with 3DES instead of AES256, then you can use the `orapki convert` command to convert the wallet to use the AES256 algorithm, which is stronger than an algorithm such as 3DES. Oracle wallets that are created with `orapki` are created with the AES256 algorithm by default.

- To change the wallet algorithm from 3DES to AES256, use the `orapki wallet convert` command.
	```
	orapki wallet convert -wallet wallet_file_directory [-pwd wallet_password] -compat_v12
	```
	In this specification:
	- `pwd` is the wallet password. If no password is provided, then a password prompt appears. For better security, enter the password at the prompt instead of entering it at the command line.
	- `compat_v12` performs the conversion from 3DES to AES256.
	You can check if the wallet has been converted from 3DES to AES356 by running the `openssl pkcs12` command. For example:
	```
	openssl pkcs12 -in sample/ewallet.p12 -info
	Enter Import Password: password
	```
	Output similar to the following appears. The `AES-256-CBC` value in the last line confirms that the wallet is encrypted with AES256.
	```
	MAC: sha1, Iteration 10000
	MAC length: 20, salt length: 8
	PKCS7 Encrypted data: PBES2, PBKDF2, AES-256-CBC, Iteration 10000, PRF hmacWithSHA256
	```

**Parent topic:** Creating, Viewing, and Modifying Wallets with orapki

#### F.6.3 Adding Certificates and Certificate Requests to Oracle Wallets with orapki

You can use the `orapki` utiltiy to perform a range of certificate-related tasks.

- Adding a Certificate Request to an Oracle Wallet  
	You can use the `orapki` utility to add certificates and certificate requests to Oracle wallets.
- Adding a Trusted Certificate to an Oracle Wallet  
	You can use the `orapki` utility to add trusted certificates to an Oracle wallet.
- Adding a Root Certificate to an Oracle Wallet  
	You can use the `orapki` utility to add a root certificate to an Oracle wallet.
- Adding a User Certificate to an Oracle Wallet  
	You can use the `orapki` utility to add a user certificate to an Oracle wallet.
- Verifying Credentials on the Hardware Device That Uses a PKCS#11 Wallet  
	You can verify credentials on the hardware device using the PKCS#11 wallet.
- Adding PKCS#11 Information to an Oracle Wallet  
	A wallet that contains PKCS#11 information can be used like any Oracle wallet.

**Parent topic:** Managing Oracle Wallets with orapki Utility

##### F.6.3.1 Adding a Certificate Request to an Oracle Wallet

You can use the `orapki` utility to add certificates and certificate requests to Oracle wallets.

- To add a certificate request to an Oracle wallet, use the `orapki wallet add` command.
	```
	orapki wallet add -wallet wallet_location -dn user_dn -keySize 512|1024|2048
	```

This command adds a certificate request to a wallet for the user with the specified distinguished name (`user_dn`). The request also specifies the requested certificate's key size (512, 1024, or 2048 bits). To sign the request, export it with the export option.

##### F.6.3.2 Adding a Trusted Certificate to an Oracle Wallet

You can use the `orapki` utility to add trusted certificates to an Oracle wallet.

- To add a trusted certificate to an Oracle wallet, use the `orapki wallet add` command.
	```
	orapki wallet add -wallet wallet_location -trusted_cert -cert certificate_location
	```

This command adds a trusted certificate, at the specified location (`-cert certificate_location`), to a wallet. You must add all trusted certificates in the certificate chain of a user certificate before adding a user certificate, or the command to add the user certificate will fail.

**Parent topic:** Adding Certificates and Certificate Requests to Oracle Wallets with orapki

##### F.6.3.3 Adding a Root Certificate to an Oracle Wallet

You can use the `orapki` utility to add a root certificate to an Oracle wallet.

- To add a root certificate to an Oracle wallet, use the `orapki wallet add` command.
	```
	orapki wallet add -wallet wallet_location -dn certificate_dn -keySize 512|1024|2048 -self_signed -validity number_of_days
	```

This command creates a new self-signed (root) certificate and adds it to the wallet. The `-validity` parameter (mandatory) specifies the number of days, starting from the current date, that this certificate will be valid. You can specify a key size for this root certificate (`-keySize`) of 512, 1024, or 2048 bits.

**Parent topic:** Adding Certificates and Certificate Requests to Oracle Wallets with orapki

##### F.6.3.4 Adding a User Certificate to an Oracle Wallet

You can use the `orapki` utility to add a user certificate to an Oracle wallet.

- To add a user certificate to an Oracle wallet, use the `orapki wallet add` command.
	```
	orapki wallet add -wallet wallet_location -user_cert -cert certificate_location
	```

This command adds the user certificate at the location specified with the `-cert` parameter to the Oracle wallet at the `wallet_location`. Before you add a user certificate to a wallet, you must add all the trusted certificates that make up the certificate chain. If all trusted certificates are not installed in the wallet before you add the user certificate, then adding the user certificate will fail.

Note:

For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password when prompted to do so.

**Parent topic:** Adding Certificates and Certificate Requests to Oracle Wallets with orapki

##### F.6.3.5 Verifying Credentials on the Hardware Device That Uses a PKCS#11 Wallet

You can verify credentials on the hardware device using the PKCS#11 wallet.

- To verify the credential details, use the `orapki wallet p11_verify` command.
	```
	orapki wallet p11_verify -wallet wallet_location [-pwd wallet_password]
	```

**Parent topic:** Adding Certificates and Certificate Requests to Oracle Wallets with orapki

##### F.6.3.6 Adding PKCS#11 Information to an Oracle Wallet

A wallet that contains PKCS#11 information can be used like any Oracle wallet.

The private keys are stored on a hardware device. The cryptographic operations are also performed on the device.

- To add PKCS#11 information to a wallet, use the `orapki wallet p11_add` command.
	```
	orapki wallet p11_add -wallet wallet_location -p11_lib pkcs11Lib 
	[-p11_tokenlabel tokenLabel] [-p11_tokenpw tokenPassphrase] 
	[-p11_certlabel certLabel] [-pwd wallet_password]
	```

In this specification:

- `wallet` specifies the wallet location.
- `p11_lib` specifies the path to the PKCS#11 library. This includes the library filename.
- `p11_tokenlabel` specifies the token or smart card used on the device. Use this when there are multiple tokens on the device. Token labels are set using vendor tools.
- `p11_tokenpw` specifies the password that is used to access the token. Token passwords are set using vendor tools.
- `p11_certlabel` is used to specify a certificate label on the token. Use this when a token contains multiple certificates. Certificate labels are set using vendor tools.
- `pwd` is used to specify the wallet password.

**Parent topic:** Adding Certificates and Certificate Requests to Oracle Wallets with orapki

#### F.6.4 Importing a User-Supplied or Trusted Certificate into an Oracle Wallet

You can add a user-supplied or trusted certificate to an Oracle wallet.

- To add a trusted certificate to an Oracle wallet, `orapki wallet add` with the `-trusted_cert` parameter.
	```
	orapki wallet add -wallet wallet_location [-pwd wallet_password] -trusted_cert -cert root_and/or_intermediate_certificate_file
	```
- To add a user-created certificate to an Oracle wallet, use `orapki wallet add` with the `-user_cert` parameter.
	```
	orapki wallet add -wallet wallet_location [-pwd wallet_password] -user_cert -cert user_certificate_file
	```

**Parent topic:** Managing Oracle Wallets with orapki Utility

#### F.6.5 Exporting Certificates and Certificate Requests from Oracle Wallets with orapki

You can use the `orapki` utility to export certificates and certificate requests from Oracle wallets.

- To export a certificate from an Oracle wallet, use the `orapki wallet export` command.
	```
	orapki wallet export -wallet wallet_location -dn certificate_dn -cert certificate_filename
	```

This command exports a certificate with the subject's distinguished name (`-dn`) from a wallet to a file that is specified by `-cert`.

To export a certificate request from an Oracle wallet, use the following command:

```
orapki wallet export -wallet wallet_location -dn certificate_request_dn -request certificate_request_filename
```

This command exports a certificate request with the subject's distinguished name (`-dn`) from a wallet to a file that is specified by `-request`.

**Parent topic:** Managing Oracle Wallets with orapki Utility

### F.7 Management of Certificate Revocation Lists (CRLs) with orapki Utility

You must manage certificate revocation lists (CRLs) with the `orapki` utility.

This utility creates a hashed value of the CRL issuer's name to identify the CRLs location in your system. If you do not use `orapki`, your Oracle server cannot locate CRLs to validate PKI digital certificates.

### F.8 orapki Usage

Examples of `orapki` commands include creating wallets, user certificates, and wallets with self-signed certificates, and exporting certificates.

- Example: Wallet with a Self-Signed Certificate and Export of the Certificate  
	The `orapki wallet add` command can create a wallet with a self-signed certificate; the `orapki wallet export` can export the certificate.
- Example: Creating a Wallet and a User Certificate  
	The `orapki` utility can create wallets and user certificates.

**Parent topic:** Managing Public Key Infrastructure (PKI) Elements

#### F.8.1 Example: Wallet with a Self-Signed Certificate and Export of the Certificate

The `orapki wallet add` command can create a wallet with a self-signed certificate; the `orapki wallet export` can export the certificate.

Example F-1 illustrates the steps to create a wallet with a self-signed certificate, view the wallet, and then export the certificate to a file.

Example F-1 Creating a Wallet with a Self-Signed Certificate and Exporting the Certificate

1. Create a wallet.
	For example:
	```
	orapki wallet create -wallet /private/user/orapki_use/root
	```
	The wallet is created at the location, `/private/user/orapki_use/root`.
2. Add a self-signed certificate to the wallet.
	```
	orapki wallet add -wallet /private/user/orapki_use/root -dn 
	'CN=root_test,C=US' -keysize 2048 -self_signed -validity 3650
	```
	This creates a self-signed certificate with a validity of 3650 days. The distinguished name of the subject is `CN=root_test,C=US`. The key size for the certificate is 2048 bits.
3. View the wallet.
	```
	orapki wallet display -wallet /private/user/orapki_use/root
	```
	This is used to view the certificate contained in the wallet.
4. Export the certificate.
	```
	orapki wallet export -wallet /private/user/orapki_use/root -dn 
	'CN=root_test,C=US' -cert /private/user/orapki_use/root/b64certificate.txt
	```
	This exports the self-signed certificate to the file, `b64certificate.txt`. Note that the distinguished name used is the same as in step 2.

**Parent topic:** orapki Usage

#### F.8.2 Example: Creating a Wallet and a User Certificate

The `orapki` utility can create wallets and user certificates.

Example F-2 illustrates miscellaneous tasks related to creating user certificates.

The following steps illustrate creating a wallet, creating a certificate request, exporting the certificate request, creating a signed certificate from the request for testing, viewing the certificate, adding a trusted certificate to the wallet and adding a user certificate to the wallet.

Example F-2 Creating a Wallet and a User Certificate

1. Create a wallet with auto-login enabled.
	For exmaple:
	```
	orapki wallet create -wallet /private/user/orapki_use/server -auto_login
	```
	This creates a wallet at `/private/user/orapki_use/server` with auto-login enabled.
2. Add a certificate request to the wallet.
	```
	orapki wallet add -wallet /private/user/orapki_use/server/ewallet.p12 -dn 'CN=server_test,C=US' -keysize 2048
	```
	This adds a certificate request to the wallet that was created (`ewallet.p12`). The distinguished name of the subject is `CN=server_test,C=US`. The key size specified is 2048 bits.
3. Export the certificate request to a file.
	```
	orapki wallet export -wallet /private/user/orapki_use/server -dn 'CN=server_test,C=US' -request /private/user/orapki_use/server/creq.txt
	```
	This exports the certificate request to the specified file, which is `creq.txt` in this case.
4. Create a signed certificate from the request for test purposes.
	```
	orapki cert create -wallet /private/user/orapki_use/root -request /private/user/orapki_use/server/creq.txt -cert /private/user/orapki_use/server/cert.txt -validity 3650
	```
	This creates a certificate, `cert.txt` with a validity of 3650 days. The certificate is created from the certificate request generated in the preceding step.
5. View the certificate.
	```
	orapki cert display -cert /private/user/orapki_use/server/cert.txt -complete
	```
	This displays the certificate generated in the preceding step. The `-complete` option enables you to display additional certificate information, including the serial number and public key.
6. Add a trusted certificate to the wallet.
	```
	orapki wallet add -wallet /private/user/orapki_use/server/ewallet.p12 -trusted_cert -cert /private/user/orapki_use/root/b64certificate.txt
	```
	This adds a trusted certificate, `b64certificate.txt` to the `ewallet.p12` wallet. You must add all trusted certificates in the certificate chain of a user certificate before adding a user certificate.
7. Add a user certificate to the wallet.
	```
	orapki wallet add -wallet /private/user/orapki_use/server/ewallet.p12 -user_cert -cert /private/user/orapki_use/server/cert.txt
	```
	This command adds the user certificate, `cert.txt` to the `ewallet.p12` wallet.

**Parent topic:** orapki Usage

### F.9 orapki Utility Commands Summary

The `orapki` commands perform a variety of wallet, certificate revocation lists (CRL), and certificate management tasks.

- orapki cert create  
	The `orapki cert create` command creates a signed certificate for testing purposes.
- orapki cert display  
	The `orapki cert display` command displays details of a specific certificate.
- orapki crl delete  
	The `orapki crl delete ` command deletes a certificate revocation list (CRL) from Oracle Internet Directory.
- orapki crl display  
	The `orapki crl display` command displays a specified certificate revocation list (CRL) that is stored in Oracle Internet Directory.
- orapki crl hash  
	The `orapki crl hash` command generates a hash value of the certificate revocation list (CRL) issuer to identify the CRL file system location for certificate validation.
- orapki crl list  
	The `orapki crl list` command displays a list of certificate revocation lists (CRLs) stored in Oracle Internet Directory.
- orapki crl upload  
	The `orapki crl upload` command uploads a certificate revocation list (CRL) to the CRL subtree in Oracle Internet Directory.
- orapki wallet add  
	The `orapki wallet add` command adds certificate requests and certificates to an Oracle wallet.
- orapki wallet convert  
	The `orapki wallet convert` command converts the 3DES algorithm in an Oracle wallet to use the AES256 algorithm.
- orapki wallet create  
	The `orapki wallet create` command creates an Oracle wallet or enables auto-login for an Oracle wallet.
- orapki wallet display  
	The `orapki wallet display` command displays the certificate requests, user certificates, and trusted certificates in an Oracle wallet.
- orapki wallet export  
	The `orapki wallet export` command exports certificate requests and certificates from an Oracle wallet.

**Parent topic:** Managing Public Key Infrastructure (PKI) Elements

#### F.9.1 orapki cert create

The `orapki cert create` command creates a signed certificate for testing purposes.

Syntax

```
orapki cert create [-wallet wallet_location] -request certificate_request_location -cert certificate_location -validity number_of_days [-summary]
```
- `wallet` specifies the wallet containing the user certificate and private key that will be used to sign the certificate request.
- `request` (mandatory) specifies the location of the certificate request for the certificate you are creating.
- `cert` (mandatory) specifies the directory location where the tool places the new signed certificate.
- `validity` (mandatory) specifies the number of days, starting from the current date, that this certificate will be valid.

**Parent topic:** orapki Utility Commands Summary

#### F.9.2 orapki cert display

The `orapki cert display` command displays details of a specific certificate.

Syntax

```
orapki cert display -cert certificate_location [-summary|-complete]
```
- `cert` specifies the location of the certificate you want to display.
- You can use either the `-summary` or the `-complete` parameter to display the following information:
	- `summary` displays the certificate and its expiration date
		- `complete` displays additional certificate information, including the serial number and public key

**Parent topic:** orapki Utility Commands Summary

#### F.9.3 orapki crl delete

The `orapki crl delete ` command deletes a certificate revocation list (CRL) from Oracle Internet Directory.

The user who deletes the CRLs from the directory by using `orapki` must be a member of the `CRLAdmins` (`cn=CRLAdmins,cn=groups,%s_OracleContextDN%`) directory group.

Prerequisites

None

Syntax

```
orapki crl delete -issuer issuer_name -ldap hostname:ssl_port -user username [-wallet wallet_location] [-summary]
```
- `issuer` specifies the name of the certificate authority (CA) who issued the CRL.
- `ldap` specifies the host name and SSL port for the directory where the CRLs are to be deleted. Note that this must be a directory SSL port (uploaded to Oracle Internet Directory) with no authentication.
- `user` specifies the user name of the directory user who has permission to delete CRLs from the CRL subtree in the directory.
- `wallet` (optional) specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to deleting it from the directory.
- `summary` is optional. It displays the CRL LDAP entry that was deleted.

#### F.9.4 orapki crl display

The `orapki crl display` command displays a specified certificate revocation list (CRL) that is stored in Oracle Internet Directory.

Syntax

```
orapki crl display -crl crl_location [-wallet wallet_location] [-summary|-complete]
```
- `crl` parameter specifies the location of the CRL in the directory. It is convenient to paste the CRL location from the list that displays when you use the `orapki crl list` command.
- `wallet` (optional) specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to displaying it.
- `summary ` and `complete` display the following information:
	- `summary` provides a listing that contains the CRL issuer's name and the CRL's validity period
		- `complete` provides a list of all revoked certificates that the CRL contains. Note that this option may take a long time to display, depending on the size of the CRL.

#### F.9.5 orapki crl hash

The `orapki crl hash` command generates a hash value of the certificate revocation list (CRL) issuer to identify the CRL file system location for certificate validation.

Syntax

```
orapki crl hash -crl crl_filename|URL [-wallet wallet_location] [-symlink|-copy] crl_directory [-summary]
```
- `crl` specifies the filename that contains the CRL or the URL where it can be found.
- `wallet` (optional) specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to uploading it to the directory.
- Depending on the operating system, use either the `-symlink` or the `-copy` parameter:
	- (UNIX) `symlink` creates a symbolic link to the CRL at the `crl_directory` location
		- (Windows) `copy` creates a copy of the CRL at the `crl_directory` location
- `summary` (optional) displays the CRL issuer's name.

**Parent topic:** orapki Utility Commands Summary

#### F.9.6 orapki crl list

The `orapki crl list` command displays a list of certificate revocation lists (CRLs) stored in Oracle Internet Directory.

Syntax

This is useful for browsing to locate a particular CRL to view or download to your local file system.

```
orapki crl list -ldap hostname:ssl_port
```

`ldap` specifies the host name and SSL port for the directory server from where you want to list CRLs. Note that this must be a directory SSL port with no authentication.

#### F.9.7 orapki crl upload

The `orapki crl upload` command uploads a certificate revocation list (CRL) to the CRL subtree in Oracle Internet Directory.

Note that you must be a member of the directory administrative group `CRLAdmins` (`cn=CRLAdmins,cn=groups,%s_OracleContextDN%`) to upload CRLs to the directory.

Syntax

```
orapki crl upload -crl crl_location -ldap hostname:ssl_port -user username [-wallet wallet_location] [-summary]
```
- `crl` specifies the directory location or the URL where the CRL is located that you are uploading to the directory.
- `ldap` specifies the host name and SSL port for the directory where you are uploading the CRLs. Note that this must be a directory SSL port with no authentication.
- `user` specifies the user name of the directory user who has permission to add CRLs to the CRL subtree in the directory.
- `wallet` specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. This is an optional parameter. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to uploading it to the directory.
- `summary` is optional. It displays the CRL issuer's name and the LDAP entry where the CRL is stored in the directory.

#### F.9.8 orapki wallet add

The `orapki wallet add` command adds certificate requests and certificates to an Oracle wallet.

Syntax

To add certificate requests:

```
orapki wallet add -wallet wallet_location -dn user_dn -keySize 512|1024|2048
```
- `wallet` specifies the location of the wallet to which you want to add a certificate request.
- `dn` specifies the distinguished name of the certificate owner.
- `keySize` specifies the key size for the certificate.
- To sign the request, export it with the export option.

To add trusted certificates:

```
orapki wallet add -wallet wallet_location -trusted_cert -cert certificate_location
```
- `trusted_cert` adds the trusted certificate, at the location specified with `-cert`, to the wallet.

To add root certificates:

```
orapki wallet add -wallet wallet_location -dn certificate_dn -keySize 512|1024|2048 -self_signed -validity number_of_days
```
- `self_signed` creates a root certificate.
- `validity` is mandatory. Use it to specify the number of days, starting from the current date, that this root certificate will be valid.

To add user certificates:

```
orapki wallet add -wallet wallet_location -user_cert -cert certificate_location
```
- `user_cert` adds the user certificate at the location specified with the `-cert` parameter to the wallet. Before you add a user certificate to a wallet, you must add all the trusted certificates that make up the certificate chain. If all trusted certificates are not installed in the wallet before you add the user certificate, then adding the user certificate will fail.

#### F.9.9 orapki wallet convert

The `orapki wallet convert` command converts the 3DES algorithm in an Oracle wallet to use the AES256 algorithm.

Note:

The 3DES112 and 3DES168 algorithms are deprecated in this release. To transition your Oracle Database environment to use stronger algorithms, download and install the patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2).

Syntax

```
orapki wallet convert -wallet wallet_location [-pwd wallet_password] [-compat_v12]
```
- `wallet` specifies a location for the new wallet or the location of the wallet for which you want to turn on auto-login.
- `pwd` is the wallet password.
- `compat_v12` performs the conversion from 3DES to AES256.

**Parent topic:** orapki Utility Commands Summary

#### F.9.10 orapki wallet create

The `orapki wallet create` command creates an Oracle wallet or enables auto-login for an Oracle wallet.

Syntax

```
orapki wallet create -wallet wallet_location [-auto_login|-auto_login_local]
```

The default algorithm is AES256.

- `wallet` specifies a location for the new wallet or the location of the wallet for which you want to turn on auto-login.
- `auto_login` creates an auto-login wallet, or it turns on automatic login for the wallet specified with the `-wallet` option.
- `auto_login_local` creates a local auto-login wallet, or it turns on local automatic login for the wallet specified with the `-wallet` option.

**Parent topic:** orapki Utility Commands Summary

#### F.9.11 orapki wallet display

The `orapki wallet display` command displays the certificate requests, user certificates, and trusted certificates in an Oracle wallet.

Syntax

```
orapki wallet display -wallet wallet_location
```
- `wallet` specifies a location for the wallet you want to open if it is not located in the current working directory.

**Parent topic:** orapki Utility Commands Summary

#### F.9.12 orapki wallet export

The `orapki wallet export` command exports certificate requests and certificates from an Oracle wallet.

Syntax

To export a certificate from an Oracle wallet:

```
orapki wallet export -wallet wallet_location -dn certificate_dn -cert certificate_filename
```
- `wallet` specifies the location of the wallet from which you want to export the certificate.
- `dn` specifies the distinguished name of the certificate.
- `cert` specifies the name of the file that contains the exported certificate.

To export a certificate request from an Oracle wallet:

```
orapki wallet export -wallet wallet_location -dn certificate_request_dn -request certificate_request_filename
```
- `request` specifies the name of the file that contains the exported certificate request.

**Parent topic:** orapki Utility Commands Summary