---
title: orapki Utility
book: "Advanced Security Administrator's Guide"
doc_id: E40393-10
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e40393/asoappf.htm
tags:
  - oracle
  - 11g
  - advanced-security-administrators-guide
---

## E orapki Utility

The `orapki` utility is provided to manage public key infrastructure (PKI) elements, such as wallets and certificate revocation lists, from the command line. This enables you to automate these tasks using scripts. Providing a way to incorporate the management of PKI elements into scripts makes it possible to automate many of the routine tasks of maintaining a PKI.

The following topics are included in this appendix:

## E.1 orapki Utility Overview

This command-line utility can be used to perform the following tasks:

- Creating and viewing signed certificates for testing purposes
- Manage Oracle wallets:
	- Create and display Oracle wallets
		- Add and remove certificate requests
		- Add and remove certificates
		- Add and remove trusted certificates
- Manage certificate revocation lists (CRLs):
	- Renaming CRLs with a hash value for certificate validation
		- Uploading, listing, viewing, and deleting CRLs in Oracle Internet Directory

### E.1.1 orapki Utility Syntax

The basic syntax of the `orapki` command-line utility is as follows:

```
orapki module command -parameter value
```

where `module` can be `wallet` (Oracle wallet), `crl` (certificate revocation list), or `cert` (PKI digital certificate). The available commands depend on the `module` you are using. For example, if you are working with a `wallet`, then you can add a certificate or a key to the wallet with the `add` command. The following example adds the user certificate located at `/private/lhale/cert.txt` to the wallet located at $ORACLE\_HOME/wallet/ewallet.p12:

```
orapki wallet add -wallet $ORACLE_HOME/wallet/ewallet.p12 -user_cert -cert /private/lhale/cert.txt
```

## E.2 Creating Signed Certificates for Testing Purposes

The `orapki` utility provides a convenient, lightweight way to create signed certificates for testing purposes.

To create a signed certificate for testing purposes, use the following command:

```
orapki cert create [-wallet wallet_location] -request certificate_request_location -cert certificate_location -validity number_of_days [-summary]
```

This command creates a signed certificate from the certificate request. The `-wallet` parameter specifies the wallet containing the user certificate and private key that will be used to sign the certificate request. The `-validity` parameter specifies the number of days, starting from the current date, that this certificate will be valid. Specifying a certificate and certificate request is mandatory for this command.

To view a certificate, use the following command:

```
orapki cert display -cert certificate_location [-summary | -complete]
```

This command enables you to view a test certificate that you have created with `orapki`. You can choose either `-summary` or `-complete`, which determines how much detail the command will display. If you choose `-summary`, the command will display the certificate and its expiration date. If you choose `-complete`, it will display additional certificate information, including the serial number and public key.

## E.3 Managing Oracle Wallets with orapki Utility

The following sections describe the syntax used to create and manage Oracle wallets with the `orapki` command-line utility. You can use these `orapki` utility `wallet` module commands in scripts to automate the wallet creation process.

- Creating, Viewing, and Modifying Wallets with orapki
- Adding Certificates and Certificate Requests to Oracle Wallets with orapki
- Exporting Certificates and Certificate Requests from Oracle Wallets with orapki

Note:

The `-wallet` parameter is mandatory for all `wallet` module commands.

### E.3.1 Creating, Viewing, and Modifying Wallets with orapki

This section contains the following topics:

- Creating a PKCS#12 Wallet
- Creating an Auto Login Wallet
- Viewing a Wallet
- Modifying the Password for a Wallet

#### E.3.1.1 Creating a PKCS#12 Wallet

To create an Oracle PKCS#12 wallet (`ewallet.p12`), use the following command:

```
orapki wallet create -wallet wallet_location [-pwd password]
```

This command prompts you to enter and reenter a wallet password, if no password has been specified on the command line. It creates a wallet in the location specified for `-wallet`.

Note:

For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password when prompted to do so.

#### E.3.1.2 Creating an Auto Login Wallet

To create an auto login wallet (`cwallet.sso`) that does not need a password, use the following command:

```
orapki wallet create -wallet wallet_location -auto_login_only
```

This command creates an auto login wallet (`cwallet.sso`) that does not need a password to open. You can also modify or delete the wallet without using a password. File system permissions provide the necessary security for such auto login wallets.

You can also create an auto login wallet that is associated with a PKCS#12 wallet. The auto login wallet does not need a password to open. However, you must supply the password for the associated PKCS#12 wallet in order to modify or delete the wallet. Any update to the PKCS#12 wallet also updates the associated auto login wallet.

To create an auto login wallet (`cwallet.sso`) that is associated with a PKCS#12 wallet (`ewallet.p12`), use the following command:

```
orapki wallet create -wallet wallet_location -auto_login [-pwd password]
```

This command creates a wallet with auto login enabled (`cwallet.sso`) and associates it with a PKCS#12 wallet (`ewallet.p12`). The command prompts you to enter the password for the PKCS#12 wallet, if no password has been specified at the command line.

Note:

For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password when prompted to do so.

If the `wallet_location` already contains a PKCS#12 wallet, then auto login is enabled for it. You must supply the password for the existing PKCS#12 wallet in order to enable auto login for it.

If the `wallet_location` does not contain a PKCS#12 wallet, then a new PKCS#12 wallet is created. You must specify a password for the new PKCS#12 wallet.

If you wish to turn the auto login feature off for a PKCS#12 wallet, then use Oracle Wallet Manager.

You can also choose to create a local auto login wallet. Local auto login wallets cannot be moved to another computer. They must be used on the host on which they are created.

A local auto login wallet does not need a password to open. However, you must supply the password for the associated PKCS#12 wallet in order to modify or delete the wallet. Any update to the PKCS#12 wallet also updates the associated auto login wallet.

To create a local auto login wallet, use the following command:

```
orapki wallet create -wallet wallet_location -auto_login_local [-pwd password]
```

This command creates an auto login wallet (`cwallet.sso`) that is local to both the computer on which it is created and the user who created it. It associates it with a PKCS#12 wallet (`ewallet.p12`). The command prompts you to enter the password for the PKCS#12 wallet, if no password has been specified at the command line.

Note:

For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password when prompted to do so.

#### E.3.1.3 Viewing a Wallet

To view an Oracle wallet, use the following command:

```
orapki wallet display -wallet wallet_location
```

This command displays the certificate requests, user certificates, and trusted certificates contained in the wallet, which must be a binary `PKCS12` file, with extension `.p12`. Other files will fail.

#### E.3.1.4 Modifying the Password for a Wallet

To change the wallet password, use the following command:

```
orapki wallet change_pwd -wallet wallet_location [-oldpwd password ] [-newpwd password]
```

This command changes the current wallet password to the new password. The command prompts you for the old and new passwords if no password is supplied at the command line.

Note:

For security reasons, Oracle recommends that you do not specify the password options at the command line. You should supply the password when prompted to do so.

### E.3.2 Adding Certificates and Certificate Requests to Oracle Wallets with orapki

To add a certificate request to an Oracle wallet, use the following command:

```
orapki wallet add -wallet wallet_location -dn user_dn -keySize 512|1024|2048
```

This command adds a certificate request to a wallet for the user with the specified distinguished name (`user_dn`). The request also specifies the requested certificate's key size (512, 1024, or 2048 bits). To sign the request, export it with the export option.

See Also:

"Exporting Certificates and Certificate Requests from Oracle Wallets with orapki" for more information

To add a trusted certificate to an Oracle wallet, use the following command:

```
orapki wallet add -wallet wallet_location -trusted_cert -cert
certificate_location
```

This command adds a trusted certificate, at the specified location (`-cert certificate_location`), to a wallet. You must add all trusted certificates in the certificate chain of a user certificate before adding a user certificate, or the command to add the user certificate will fail.

To add a root certificate to an Oracle wallet, use the following command:

```
orapki wallet add -wallet wallet_location -dn certificate_dn -keySize 512|1024|2048 -self_signed -validity number_of_days
```

This command creates a new self-signed (root) certificate and adds it to the wallet. The `-validity` parameter (mandatory) specifies the number of days, starting from the current date, that this certificate will be valid. You can specify a key size for this root certificate (`-keySize`) of 512, 1024, or 2048 bits.

To add a user certificate to an Oracle wallet, use the following command:

```
orapki wallet add -wallet wallet_location -user_cert -cert certificate_location
```

This command adds the user certificate at the location specified with the `-cert` parameter to the Oracle wallet at the `wallet_location`. Before you add a user certificate to a wallet, you must add all the trusted certificates that make up the certificate chain. If all trusted certificates are not installed in the wallet before you add the user certificate, then adding the user certificate will fail.

To add PKCS#11 information to a wallet

You can use a wallet containing PKCS#11 information like any Oracle wallet. The private keys are stored on a hardware device. The cryptographic operations are also performed on the device.

Use the following command to add PKCS#11 information to a wallet:

```
orapki wallet p11_add -wallet wallet_location -p11_lib pkcs11Lib 
[-p11_tokenlabel tokenLabel] [-p11_tokenpw tokenPassphrase] 
[-p11_certlabel certLabel] [-pwd password]
```

The parameters have the following meaning:

- `-wallet` specifies the wallet location.
- `-p11_lib` specifies the path to the PKCS#11 library. This includes the library filename.
- `-p11_tokenlabel` specifies the token or smart card used on the device. Use this when there are multiple tokens on the device. Token labels are set using vendor tools.
- `-p11_tokenpw` specifies the password that is used to access the token. Token passwords are set using vendor tools.
- `-p11_certlabel` is used to specify a certificate label on the token. Use this when a token contains multiple certificates. Certificate labels are set using vendor tools.
- `-pwd` is used to specify the wallet password.

Note:

For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password when prompted to do so.

You can verify credentials on the hardware device using the PKCS#11 wallet. Use the following command for this purpose:

```
orapki wallet p11_verify -wallet wallet_location [-pwd password]
```

Note:

For security reasons, Oracle recommends that you do not specify the password at the command line. You should supply the password when prompted to do so.

### E.3.3 Exporting Certificates and Certificate Requests from Oracle Wallets with orapki

To export a certificate from an Oracle wallet, use the following command:

```
orapki wallet export -wallet wallet_location -dn certificate_dn -cert certificate_filename
```

This command exports a certificate with the subject's distinguished name (`-dn`) from a wallet to a file that is specified by `-cert`.

To export a certificate request from an Oracle wallet, use the following command:

```
orapki wallet export -wallet wallet_location -dn certificate_request_dn -request certificate_request_filename
```

This command exports a certificate request with the subject's distinguished name (`-dn`) from a wallet to a file that is specified by `-request`.

## E.4 Managing Certificate Revocation Lists (CRLs) with orapki Utility

CRLs must be managed with `orapki`. This utility creates a hashed value of the CRL issuer's name to identify the CRLs location in your system. If you do not use `orapki`, your Oracle server cannot locate CRLs to validate PKI digital certificates. For detailed information about using `orapki` to manage CRLs refer to ["Certificate Revocation List Management"](asossl.md).

## E.5 orapki Usage Examples

This section includes examples of some of the `orapki` commands discussed in the preceding sections.

Example E-1 illustrates the steps to create a wallet with a self-signed certificate and export the certificate to a file.

Example E-1 Create a Wallet with a Self-Signed Certificate and Export the Certificate

The following steps illustrate creating a wallet, adding a self-signed certificate to it, viewing the wallet and exporting the certificate:

1. Create a wallet
	```
	orapki wallet create -wallet /private/user/orapki_use/root
	```
	The wallet is created at the location, `/private/user/orapki_use/root`.
2. Add a self-signed certificate to the wallet
	```
	orapki wallet add -wallet /private/user/orapki_use/root -dn 
	'CN=root_test,C=US' -keysize 2048 -self_signed -validity 3650
	```
	This creates a self-signed certificate with a validity of 3650 days. The distinguished name of the subject is `CN=root_test,C=US`. The key size for the certificate is 2048 bits.
3. View the wallet
	```
	orapki wallet display -wallet /private/user/orapki_use/root
	```
	This is used to view the certificate contained in the wallet.
4. Export the certificate
	```
	orapki wallet export -wallet /private/user/orapki_use/root -dn 
	'CN=root_test,C=US' -cert /private/user/orapki_use/root/b64certificate.txt
	```
	This exports the self-signed certificate to the file, `b64certificate.txt`. Note that the distinguished name used is the same as in step 2.

Example E-2 illustrates miscellaneous tasks related to creating user certificates.

Example E-2 Create a Wallet and a User Certificate

The following steps illustrate creating a wallet, creating a certificate request, exporting the certificate request, creating a signed certificate from the request for testing, viewing the certificate, adding a trusted certificate to the wallet and adding a user certificate to the wallet.

1. Create a wallet with auto login enabled
	```
	orapki wallet create -wallet /private/user/orapki_use/server -auto_login
	```
	This creates a wallet at `/private/user/orapki_use/server` with auto login enabled.
2. Add a certificate request to the wallet
	```
	orapki wallet add -wallet /private/user/orapki_use/server -dn 'CN=server_test,C=US' -keysize 2048
	```
	This adds a certificate request to the wallet that was created. The distinguished name of the subject is `CN=server_test,C=US`. The key size specified is 2048 bits.
3. Export the certificate request to a file
	```
	orapki wallet export -wallet /private/user/orapki_use/server -dn 'CN=server_test,C=US' -request /private/user/orapki_use/server/creq.txt
	```
	This exports the certificate request to the specified file, which is `creq.txt` in this case.
4. Create a signed certificate from the request for test purposes
	```
	orapki cert create -wallet /private/user/orapki_use/root -request /private/user/orapki_use/server/creq.txt -cert /private/user/orapki_use/server/cert.txt -validity 3650
	```
	This creates a certificate, `cert.txt` with a validity of 3650 days. The certificate is created from the certificate request generated in the preceding step.
5. View the certificate
	```
	orapki cert display -cert /private/user/orapki_use/server/cert.txt -complete
	```
	This displays the certificate generated in the preceding step. The `-complete` option enables you to display additional certificate information, including the serial number and public key.
6. Add a trusted certificate to the wallet
	```
	orapki wallet add -wallet /private/user/orapki_use/server -trusted_cert -cert /private/user/orapki_use/root/b64certificate.txt
	```
	This adds a trusted certificate, `b64certificate.txt` to the wallet. You must add all trusted certificates in the certificate chain of a user certificate before adding a user certificate.
7. Add a user certificate to the wallet
	```
	orapki wallet add -wallet /private/user/orapki_use/server -user_cert -cert /private/user/orapki_use/server/cert.txt
	```
	This adds the user certificate, `cert.txt` to the wallet.

## E.6 orapki Utility Commands Summary

This section lists and describes the following `orapki` commands:

- orapki cert create
- orapki cert display
- orapki crl delete
- orapki crl display
- orapki crl hash
- orapki crl list
- orapki crl upload
- orapki wallet add
- orapki wallet create
- orapki wallet display
- orapki wallet export

### E.6.1 orapki cert create

The following sections describe this command.

#### E.6.1.1 Purpose

Use the `orapki cert create` command to create a signed certificate for testing purposes.

#### E.6.1.2 Syntax

```
orapki cert create [-wallet wallet_location] -request certificate_request_location -cert certificate_location -validity number_of_days [-summary]
```
- The `-wallet` parameter specifies the wallet containing the user certificate and private key that will be used to sign the certificate request.
- The `-request` parameter (mandatory) specifies the location of the certificate request for the certificate you are creating.
- The `-cert` parameter (mandatory) specifies the directory location where the tool places the new signed certificate.
- The `-validity` parameter (mandatory) specifies the number of days, starting from the current date, that this certificate will be valid.

### E.6.2 orapki cert display

The following sections describe this command.

#### E.6.2.1 Purpose

Use the `orapki cert display` command to display details of a specific certificate.

#### E.6.2.2 Syntax

```
orapki cert display -cert certificate_location [-summary|-complete]
```
- The `-cert` parameter specifies the location of the certificate you want to display.
- You can use either the `-summary` or the `-complete` parameter to display the following information:
	- `-summary` displays the certificate and its expiration date
		- `-complete` displays additional certificate information, including the serial number and public key

### E.6.3 orapki crl delete

The following sections describe this command.

#### E.6.3.1 Purpose

Use the `orapki crl delete` command to delete CRLs from Oracle Internet Directory. Note that the user who deletes CRLs from the directory by using `orapki` must be a member of the `CRLAdmins` (`cn=CRLAdmins,cn=groups,%s_OracleContextDN%`) directory group.

#### E.6.3.2 Prerequisites

None

#### E.6.3.3 Syntax

```
orapki crl delete -issuer issuer_name -ldap hostname:ssl_port -user username [-wallet wallet_location] [-summary]
```
- The `-issuer` parameter specifies the name of the certificate authority (CA) who issued the CRL.
- The `-ldap` parameter specifies the host name and SSL port for the directory where the CRLs are to be deleted. Note that this must be a directory SSL port with no authentication.
	See Also:
	Refer to ["Uploading CRLs to Oracle Internet Directory"](asossl.md) for more information about this port.
- The `-user` parameter specifies the user name of the directory user who has permission to delete CRLs from the CRL subtree in the directory.
- The `-wallet` parameter (optional) specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to deleting it from the directory.
- The `-summary` parameter is optional. Using it causes the tool to print the CRL LDAP entry that was deleted.

### E.6.4 orapki crl display

The following sections describe this command.

#### E.6.4.1 Purpose

Use the `orapki crl display` command to display specific CRLs that are stored in Oracle Internet Directory.

#### E.6.4.2 Syntax

```
orapki crl display -crl crl_location [-wallet wallet_location] [-summary|-complete]
```
- The `-crl` parameter specifies the location of the CRL in the directory. It is convenient to paste the CRL location from the list that displays when you use the `orapki crl list` command. Refer to "orapki crl list"
- The `-wallet` parameter (optional) specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to displaying it.
- Choosing either the `-summary` or the `-complete` parameters displays the following information:
	- `-summary` provides a listing that contains the CRL issuer's name and the CRL's validity period
		- `-complete` provides a list of all revoked certificates that the CRL contains. Note that this option may take a long time to display, depending on the size of the CRL.

### E.6.5 orapki crl hash

The following sections describe this command.

#### E.6.5.1 Purpose

Use the `orapki crl hash` command to generate a hash value of the certificate revocation list (CRL) issuer to identify the location of the CRL in the file system for certificate validation.

#### E.6.5.2 Syntax

```
orapki crl hash -crl crl_filename|URL [-wallet wallet_location] [-symlink|-copy] crl_directory [-summary]
```
- The `-crl` parameter specifies the filename that contains the CRL or the URL where it can be found.
- The `-wallet` parameter (optional) specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to uploading it to the directory.
- Depending on the operating system, use either the `-symlink` or the `-copy` parameter:
	- (UNIX) use `-symlink` to create a symbolic link to the CRL at the `crl_directory` location
		- (Windows) use `-copy` to create a copy of the CRL at the `crl_directory` location
- The `-summary` parameter (optional) causes the tool to display the CRL issuer's name.

### E.6.6 orapki crl list

The following sections describe this command.

#### E.6.6.1 Purpose

Use the `orapki crl list` command to display a list of CRLs stored in Oracle Internet Directory. This is useful for browsing to locate a particular CRL to view or download to your local file system.

#### E.6.6.2 Syntax

```
orapki crl list -ldap hostname:ssl_port
```

The `-ldap` parameter specifies the host name and SSL port for the directory server from where you want to list CRLs. Note that this must be a directory SSL port with no authentication.

Tip:

["Uploading CRLs to Oracle Internet Directory"](asossl.md) for more information about this port

### E.6.7 orapki crl upload

The following sections describe this command.

#### E.6.7.1 Purpose

Use the `orapki crl upload` command to upload certificate revocation lists (CRLs) to the CRL subtree in Oracle Internet Directory. Note that you must be a member of the directory administrative group `CRLAdmins` (`cn=CRLAdmins,cn=groups,%s_OracleContextDN%`) to upload CRLs to the directory.

#### E.6.7.2 Syntax

```
orapki crl upload -crl crl_location -ldap hostname:ssl_port -user username [-wallet wallet_location] [-summary]
```
- The `-crl` parameter specifies the directory location or the URL where the CRL is located that you are uploading to the directory.
- The `-ldap` parameter specifies the host name and SSL port for the directory where you are uploading the CRLs. Note that this must be a directory SSL port with no authentication.
	See Also:
	["Uploading CRLs to Oracle Internet Directory"](asossl.md) for more information about this port
- The `-user` parameter specifies the user name of the directory user who has permission to add CRLs to the CRL subtree in the directory.
- The `-wallet` parameter specifies the location of the wallet that contains the certificate of the certificate authority (CA) who issued the CRL. This is an optional parameter. Using it causes the tool to verify the validity of the CRL against the CA's certificate prior to uploading it to the directory.
- The `-summary` parameter is also optional. Using it causes the tool to display the CRL issuer's name and the LDAP entry where the CRL is stored in the directory.

### E.6.8 orapki wallet add

The following sections describe this command.

#### E.6.8.1 Purpose

Use the `orapki wallet add` command to add certificate requests and certificates to an Oracle wallet.

#### E.6.8.2 Syntax

To add certificate requests, use the following command:

```
orapki wallet add -wallet wallet_location -dn user_dn -keySize 512|1024|2048
```
- The `-wallet` parameter specifies the location of the wallet to which you want to add a certificate request.
- The `-dn` parameter specifies the distinguished name of the certificate owner.
- The `-keySize` parameter specifies the key size for the certificate.
- To sign the request, export it with the export option. Refer to "orapki wallet export"

To add trusted certificates, use the following command:

```
orapki wallet add -wallet wallet_location -trusted_cert -cert certificate_location
```
- The `-trusted_cert` parameter causes the tool to add the trusted certificate, at the location specified with `-cert`, to the wallet.

To add root certificates, use the following command:

```
orapki wallet add -wallet wallet_location -dn certificate_dn -keySize 512|1024|2048 -self_signed -validity number_of_days
```
- The `-self_signed` parameter causes the tool to create a root certificate.
- The `-validity` parameter is mandatory. Use it to specify the number of days, starting from the current date, that this root certificate will be valid.

To add user certificates, use the following command:

```
orapki wallet add -wallet wallet_location -user_cert -cert certificate_location
```
- The `-user_cert` parameter causes the tool to add the user certificate at the location specified with the `-cert` parameter to the wallet. Before you add a user certificate to a wallet, you must add all the trusted certificates that make up the certificate chain. If all trusted certificates are not installed in the wallet before you add the user certificate, then adding the user certificate will fail.

### E.6.9 orapki wallet create

The following sections describe this command.

#### E.6.9.1 Purpose

Use the `orapki wallet create` command to create an Oracle wallet or to set auto login on for an Oracle wallet.

#### E.6.9.2 Syntax

```
orapki wallet create -wallet wallet_location [-auto_login|-auto_login_local]
```
- The `-wallet` parameter specifies a location for the new wallet or the location of the wallet for which you want to turn on auto login.
- The `-auto_login` parameter creates an [auto login wallet](asogls.md), or it turns on automatic login for the wallet specified with the `-wallet` option.
- The `-auto_login_local` parameter creates a local auto login wallet, or it turns on local automatic login for the wallet specified with the `-wallet` option.

### E.6.10 orapki wallet display

The following sections describe this command.

#### E.6.10.1 Purpose

Use the `orapki wallet display` command to view the certificate requests, user certificates, and trusted certificates in an Oracle wallet.

#### E.6.10.2 Syntax

```
orapki wallet display -wallet wallet_location
```
- The `-wallet` parameter specifies a location for the wallet you want to open if it is not located in the current working directory.

### E.6.11 orapki wallet export

The following sections describe this command.

#### E.6.11.1 Purpose

Use the `orapki wallet export` command to export certificate requests and certificates from an Oracle wallet.

#### E.6.11.2 Syntax

To export a certificate from an Oracle wallet, use the following command:

```
orapki wallet export -wallet wallet_location -dn certificate_dn -cert certificate_filename
```
- The `-wallet` parameter specifies the location of the wallet from which you want to export the certificate.
- The `-dn` parameter specifies the distinguished name of the certificate.
- The `-cert` parameter specifies the name of the file that contains the exported certificate.

To export a certificate request from an Oracle wallet, use the following command:

```
orapki wallet export -wallet wallet_location -dn certificate_request_dn -request certificate_request_filename
```
- The `-request` parameter specifies the name of the file that contains the exported certificate request.