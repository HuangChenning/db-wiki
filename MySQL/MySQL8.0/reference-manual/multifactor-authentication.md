---
title: "8.2.18 Multifactor Authentication"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/multifactor-authentication.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 8.2.18 Multifactor Authentication

Authentication involves one party establishing its identity to the satisfaction of a second party. Multifactor authentication (MFA) is the use of multiple authentication values (or “factors”) during the authentication process. MFA provides greater security than one-factor/single-factor authentication (1FA/SFA), which uses only one authentication method such as a password. MFA enables additional authentication methods, such as authentication using multiple passwords, or authentication using devices like smart cards, security keys, and biometric readers.

MySQL 8.0.27 and higher includes support for multifactor authentication. This capability includes forms of MFA that require up to three authentication values. That is, MySQL account management supports accounts that use 2FA or 3FA, in addition to the existing 1FA support.

When a client attempts a connection to the MySQL server using a single-factor account, the server invokes the authentication plugin indicated by the account definition and accepts or rejects the connection depending on whether the plugin reports success or failure.

For an account that has multiple authentication factors, the process is similar. The server invokes authentication plugins in the order listed in the account definition. If a plugin reports success, the server either accepts the connection if the plugin is the last one, or proceeds to invoke the next plugin if any remain. If any plugin reports failure, the server rejects the connection.

The following sections cover multifactor authentication in MySQL in more detail.

#### Elements of Multifactor Authentication Support

Authentication factors commonly include these types of information:

- Something you know, such as a secret password or passphrase.
- Something you have, such as a security key or smart card.
- Something you are; that is, a biometric characteristic such as a fingerprint or facial scan.

The “something you know” factor type relies on information that is kept secret on both sides of the authentication process. Unfortunately, secrets may be subject to compromise: Someone might see you enter your password or fool you with a phishing attack, a password stored on the server side might be exposed by a security breach, and so forth. Security can be improved by using multiple passwords, but each may still be subject to compromise. Use of the other factor types enables improved security with less risk of compromise.

Implementation of multifactor authentication in MySQL comprises these elements:

- The [`authentication_policy`](server-system-variables.md) system variable controls how many authentication factors can be used and the types of authentication permitted for each factor. That is, it places constraints on [`CREATE USER`](create-user.md) and [`ALTER USER`](alter-user.md) statements with respect to multifactor authentication.
- [`CREATE USER`](create-user.md) and [`ALTER USER`](alter-user.md) have syntax enabling multiple authentication methods to be specified for new accounts, and for adding, modifying, or dropping authentication methods for existing accounts. If an account uses 2FA or 3FA, the `mysql.user` system table stores information about the additional authentication factors in the `User_attributes` column.
- To enable authentication to the MySQL server using accounts that require multiple passwords, client programs have [`--password1`](connection-options.md), [`--password2`](connection-options.md), and [`--password3`](connection-options.md) options that permit up to three passwords to be specified. For applications that use the C API, the `MYSQL_OPT_USER_PASSWORD` option for the [`mysql_options4()`](https://docs.oracle.com/cd/E17952_01/c-api-8.0-en/mysql-options4.html) C API function enables the same capability.
- The server-side `authentication_fido` plugin (deprecated) enables authentication using devices. This server-side FIDO authentication plugin is included only in MySQL Enterprise Edition distributions. It is not included in MySQL community distributions. However, the client-side `authentication_fido_client` plugin (deprecated) is included in all distributions, including community distributions. This enables clients from any distribution to connect to accounts that use `authentication_fido` to authenticate on a server that has that plugin loaded. See [Section 8.4.1.11, “FIDO Pluggable Authentication”](fido-pluggable-authentication.md).
- `authentication_fido` also enables passwordless authentication, if it is the only authentication plugin used by an account. See [FIDO Passwordless Authentication](fido-pluggable-authentication.md).
- Multifactor authentication can use non-FIDO MySQL authentication methods, the FIDO authentication method, or a combination of both.
- These privileges enable users to perform certain restricted multifactor authentication-related operations:
	- A user who has the [`AUTHENTICATION_POLICY_ADMIN`](privileges-provided.md) privilege is not subject to the constraints imposed by the [`authentication_policy`](server-system-variables.md) system variable. (A warning does occur for statements that otherwise would not be permitted.)
	- The [`PASSWORDLESS_USER_ADMIN`](privileges-provided.md) privilege enables creation of passwordless-authentication accounts and replication of operations on them.

#### Configuring the Multifactor Authentication Policy

The [`authentication_policy`](server-system-variables.md) system variable defines the multifactor authentication policy. Specifically, it defines how many authentication factors accounts may have (or are required to have) and the authentication methods that can be used for each factor.

The value of [`authentication_policy`](server-system-variables.md) is a list of 1, 2, or 3 comma-separated elements. Each element in the list corresponds to an authentication factor and can be an authentication plugin name, an asterisk (`*`), empty, or missing. (Exception: Element 1 cannot be empty or missing.) The entire list is enclosed in single quotes. For example, the following [`authentication_policy`](server-system-variables.md) value includes an asterisk, an authentication plugin name, and an empty element:

```
authentication_policy = '*,authentication_fido,'
```

An asterisk (`*`) indicates that an authentication method is required but any method is permitted. An empty element indicates that an authentication method is optional and any method is permitted. A missing element (no asterisk, empty element, or authentication plugin name) indicates that an authentication method is not permitted. When a plugin name is specified, that authentication method is required for the respective factor when creating or modifying an account.

The default [`authentication_policy`](server-system-variables.md) value is `'*,,'` (an asterisk and two empty elements), which requires a first factor, and optionally permits second and third factors. The default [`authentication_policy`](server-system-variables.md) value is thus backward compatible with existing 1FA accounts, but also permits creation or modification of accounts to use 2FA or 3FA.

A user who has the [`AUTHENTICATION_POLICY_ADMIN`](privileges-provided.md) privilege is not subject to the constraints imposed by the [`authentication_policy`](server-system-variables.md) setting. (A warning occurs for statements that otherwise would not be permitted.)

[`authentication_policy`](server-system-variables.md) values can be defined in an option file or specified using a [`SET         GLOBAL`](set-variable.md) statement:

```
SET GLOBAL authentication_policy='*,*,';
```

There are several rules that govern how the [`authentication_policy`](server-system-variables.md) value can be defined. Refer to the [`authentication_policy`](server-system-variables.md) system variable description for a compete account of those rules. The following table provides several [`authentication_policy`](server-system-variables.md) example values and the policy established by each.

**Table 8.11 Example authentication\_policy Values**

| authentication\_policy Value | Effective Policy |
| --- | --- |
| `'*'` | Permit only creating or altering accounts with one factor. |
| `'*,*'` | Permit only creating or altering accounts with two factors. |
| `'*,*,*'` | Permit only creating or altering accounts with three factors. |
| `'*,'` | Permit creating or altering accounts with one or two factors. |
| `'*,,'` | Permit creating or altering accounts with one, two, or three factors. |
| `'*,*,'` | Permit creating or altering accounts with two or three factors. |
| ``'*,*`auth_plugin`*'`` | Permit creating or altering accounts with two factors, where the first factor can be any authentication method, and the second factor must be the named plugin. |
| ``'*`auth_plugin`*,*,'`` | Permit creating or altering accounts with two or three factors, where the first factor must be the named plugin. |
| ``'*`auth_plugin`*,'`` | Permit creating or altering accounts with one or two factors, where the first factor must be the named plugin. |
| ``'*`auth_plugin`*,*`auth_plugin`*,*`auth_plugin`*'`` | Permits creating or altering accounts with three factors, where the factors must use the named plugins. |

#### Getting Started with Multifactor Authentication

By default, MySQL uses a multifactor authentication policy that permits any authentication plugin for the first factor, and optionally permits second and third authentication factors. This policy is configurable; for details, see Configuring the Multifactor Authentication Policy.

Note

It is not permitted to use any internal credential storage plugins (`caching_sha2_password` or `mysql_native_password`) for factor 2 or 3.

Suppose that you want an account to authenticate first using the `caching_sha2_password` plugin, then using the `authentication_ldap_sasl` SASL LDAP plugin. (This assumes that LDAP authentication is already set up as described in [Section 8.4.1.7, “LDAP Pluggable Authentication”](ldap-pluggable-authentication.md), and that the user has an entry in the LDAP directory corresponding to the authentication string shown in the example.) Create the account using a statement like this:

```
CREATE USER 'alice'@'localhost'
  IDENTIFIED WITH caching_sha2_password
    BY 'sha2_password'
  AND IDENTIFIED WITH authentication_ldap_sasl
    AS 'uid=u1_ldap,ou=People,dc=example,dc=com';
```

To connect, the user must supply two passwords. To enable authentication to the MySQL server using accounts that require multiple passwords, client programs have [`--password1`](connection-options.md), [`--password2`](connection-options.md), and [`--password3`](connection-options.md) options that permit up to three passwords to be specified. These options are similar to the [`--password`](connection-options.md) option in that they can take a password value following the option on the command line (which is insecure) or if given without a password value cause the user to be prompted for one. For the account just created, factors 1 and 2 take passwords, so invoke the [**mysql**](mysql.md) client with the [`--password1`](mysql-command-options.md) and [`--password2`](mysql-command-options.md) options. [**mysql**](mysql.md) prompts for each password in turn:

```
$> mysql --user=alice --password1 --password2
Enter password: (enter factor 1 password)
Enter password: (enter factor 2 password)
```

Suppose you want to add a third authentication factor. This can be achieved by dropping and recreating the user with a third factor or by using [``ALTER USER         *`user`* ADD         *`factor`*``](alter-user.md) syntax. Both methods are shown below:

```
DROP USER 'alice'@'localhost';
  
CREATE USER 'alice'@'localhost'
  IDENTIFIED WITH caching_sha2_password
    BY 'sha2_password'
  AND IDENTIFIED WITH authentication_ldap_sasl
    AS 'uid=u1_ldap,ou=People,dc=example,dc=com'
  AND IDENTIFIED WITH authentication_fido;
```

``ADD *`factor`*`` syntax includes the factor number and `FACTOR` keyword:

```
ALTER USER 'alice'@'localhost' ADD 3 FACTOR IDENTIFIED WITH authentication_fido;
```

[``ALTER USER         *`user`* DROP         *`factor`*``](alter-user.md) syntax permits dropping a factor. The following example drops the third factor (`authentication_fido`) that was added in the previous example:

```
ALTER USER 'alice'@'localhost' DROP 3 FACTOR;
```

[``ALTER USER         *`user`* MODIFY         *`factor`*``](alter-user.md) syntax permits changing the plugin or authentication string for a particular factor, provided that the factor exists. The following example modifies the second factor, changing the authentication method from `authentication_ldap_sasl` to `authetication_fido`:

```
ALTER USER 'alice'@'localhost' MODIFY 2 FACTOR IDENTIFIED WITH authentication_fido;
```

Use [`SHOW CREATE USER`](show-create-user.md) to view the authentication methods defined for an account:

```
SHOW CREATE USER 'u1'@'localhost'\G
*************************** 1. row ***************************
CREATE USER for u1@localhost: CREATE USER \`u1\`@\`localhost\` 
IDENTIFIED WITH 'caching_sha2_password' AS 'sha2_password' 
AND IDENTIFIED WITH 'authentication_fido' REQUIRE NONE 
PASSWORD EXPIRE DEFAULT ACCOUNT UNLOCK PASSWORD HISTORY 
DEFAULT PASSWORD REUSE INTERVAL DEFAULT PASSWORD REQUIRE 
CURRENT DEFAULT
```