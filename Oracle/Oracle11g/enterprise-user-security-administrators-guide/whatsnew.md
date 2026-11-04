---
title: "What's New in Enterprise User Security?"
book: "Enterprise User Security Administrator's Guide"
doc_id: E10744-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10744/whatsnew.htm
tags:
  - oracle
  - 11g
  - enterprise-user-security-administrators-guide
---

This section describes new features of Enterprise User Security and provides pointers to additional information. New features information from the previous releases is also retained to help users who are migrating to the current release.

The following sections describe the new features in Enterprise User Security:

## Oracle Database 11g New Features in Enterprise User Security

Enterprise User Security 11g includes the following new feature:

Enterprise User Security can now be managed using the graphical user interface (GUI) provided by Oracle Enterprise Manager. Oracle Enterprise Manager can be used to conveniently configure enterprise users, groups, roles, domains, and so on.

See Also:

[Chapter 2, "Getting Started with Enterprise User Security"](getstrtd.md)

## Oracle Database 10g Release 2 (10.2) New Features in Enterprise User Security

Enterprise User Security 10g Release 2 (10.2) includes the following new features:

- Enterprise User Security 10g Release 2 (10.2) includes new functionality for sharing `sqlnet.ora` files among multiple databases. Databases can share a single `sqlnet.ora` file while maintaining separate wallets. This makes Enterprise User Security configuration easier and improves Secure Sockets Layer (SSL) usability. See ["Sharing Wallets and sqlnet.ora Files Among Multiple Databases"](configur.md) for more information.
- Password policies are created for every identity management realm in Oracle Internet Directory. These policies apply to all enterprise users who reside in the realm. Password policies include settings for password complexity, minimum password length, and the like. They also include account lockout and password expiration settings. Enterprise User Security honors the realm wide password policies which are set in Oracle Internet Directory.
	The database communicates with Oracle Internet Directory when authenticating an enterprise user. It checks to see whether the user's account is locked, disabled, expired, or about to expire. It displays appropriate warnings or error messages in these cases.
	See Also:
	["Password Policies"](concepts.md) for more information on password policies and their management
- The Distinguished Name (DN) in the user certificate no longer needs to match the DN in Oracle Internet Directory. This feature is useful if your public key infrastructure (PKI) certificate authority does not support the use of two common names (cn) in the DN. This also enables you to restructure your Directory without requiring new certificates for users or databases. See ["Configuring Enterprise User Security for SSL Authentication"](configur.md) for more information.

Enterprise User Security 10g Release 2 (10.2) also introduces several new proxying features that enhance both security and ease of use:

- Proxy permissions for specific enterprise users (or lists of enterprise users) can now be created and stored in Oracle Internet Directory. Formerly, proxy permissions could be granted only to a shared schema, necessarily enabling any enterprise user in that shared schema to proxy as the target user.
- Establishing a proxy session results in a single-user session. Formerly, switching from the original connected session to proxy as the target user created a second, independent session, with the first one also remaining active.
- Proxy access is now possible through SQLPLUS as well as Oracle Call Interface (OCI). Formerly, proxy access could be established only through OCI.

New proxying features are described in ["Enterprise User Proxy"](concepts.md).

## Oracle Database 10g Release 1 (10.1) New Features in Enterprise User Security

Enterprise User Security 10g Release 1 (10.1) included the following new features:

- Kerberos Authenticated Enterprise Users
	Kerberos-based authentication to the database is available for users managed in an LDAP directory. This includes Oracle Internet Directory or any other third-party directory that is synchronized to work with Oracle Internet Directory by using the Directory Integration Platform. To use this feature, all directory users, including those synchronized from third-party directories, must include the Kerberos principal name attribute (`krbPrincipalName` attribute).
	See Also:
	["Configuring Enterprise User Security for Kerberos Authentication"](configur.md) for configuration details
- Public key infrastructure (PKI) Credentials No Longer Required for Database-to-Oracle Internet Directory Connections
	In this release, a database can bind to Oracle Internet Directory by using password/SASL-based authentication, eliminating the overhead of setting up PKI credentials for the directory and multiple databases. SASL (Simple Authentication and Security Layer) is a standard defined in the Internet Engineering Task Force RFC 2222. It is a method for adding authentication support to connection-based protocols such as LDAP.
	See Also:
	["Configuring Enterprise User Security for Password Authentication"](configur.md) for configuration details
- Support for User Management in Third-Party LDAP Directories
	In the current release of Enterprise User Security, you can store and manage your users and their passwords in third-party LDAP directories. This feature is made possible with
	- Directory Integration Platform, which automatically synchronizes third-party directories with Oracle Internet Directory, and
		- Oracle Database recognition of standard password verifiers, which is also new in this release.