---
title: Security Guide
book: Database Security Guide
doc_id: F31285-18
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dbseg/introduction-to-oracle-database-security.html
tags:
  - oracle
  - 21c
  - security-guide
---

Oracle Database provides a rich set of default security features to manage user accounts, authentication, privileges, application security, encryption, network traffic, and auditing.

- About Oracle Database Security  
	Use Oracle Database's security features to reduce risk and protect data from theft, destruction, or misuse.
- Additional Oracle Database Security Products  
	In addition to the security resources that are available in a default database installation, Oracle Database provides several other database security products.

### 1.1 About Oracle Database Security

Use Oracle Database's security features to reduce risk and protect data from theft, destruction, or misuse.

A few popular areas to focus security efforts on include:

- User accounts. When a schema is created, it comes with a local database user account that has privileges in that schema. When you create user accounts, you can secure them in a variety of ways. You can also create password profiles and resource limits to better secure password policies for your site. Oracle Database provides a set of predefined schemas that provide database functionality and other predefined schemas with administrative privileges.
- Authentication methods. Oracle Database provides several ways to configure authentication for users and database administrators. For example, you can authenticate users on the database level, from the operating system, and on the network, and for multitier, global users, and application servers. If you use Microsoft Active Directory, you can authenticate and authorize Microsoft Active Directory users with the database directly.
	You can configure your databases to use strong authentication with Oracle authentication adapters that support various third-party authentication services with digital certificates. Oracle Database provides the following strong authentication support:
	- Centralized authentication and single sign-on.
		- Kerberos
		- Remote Authentication Dial-in User Service (RADIUS)
		- Certificate-based authentication
- Privileges and roles. You can use privileges and roles to restrict user access to data in the following ways:
	- Creating and granting privileges and roles to users or other roles
		- Performing privilege analysis to find information about how privileges are used in your site
		- Configure definer's rights and invoker's rights for your applications
		- Manage fine-grained access in PL/SQL packages and types
		- Use Enterprise Manager to manage security
- Application security. The first step to creating a database application is to ensure that it you have properly incorporated application security into your application security policies.
- User session information using application context. An application context is a name-value pair that holds the session information. You can retrieve session information about a user, such as the user name or terminal, and restrict database and application access for that user based on this information.
- Classify and protect data in different categories. You can create Transparent Sensitive Data Protection policies to find all table columns in a database that hold sensitive data (such as credit card or Social Security numbers), classify this data, and then create a policy that protects this data as a whole for a given class.
- Network data encryption. You can use Transport Layer Security (TLS) and native network encryption to encrypt data as it travels on the network to prevent unauthorized access to that data. You can configure native Oracle Net Services data encryption for both servers and clients.
- Thin JDBC client network configuration. You can configure thin Java Database Connectivity (JDBC) clients to securely connect to Oracle databases.
- Auditing database activities. Auditing provides the most accurate record of any database activity, not just from connections that take place over the wire but also through direct local logins, recursive SQL, dynamic SQLs, and stored procedures. Database auditing involves creating and enabling unified audit policies to track activities such as user actions, schema changes, logon events. Unified auditing further enables you to audit selectively by adding various conditions including application context values and simple built-in functions. This helps you to reduce the volume of your audit data, and at the same time helping you detect malicious activities in a timely manner.

**Parent topic:** Introduction to Oracle Database Security

### 1.2 Additional Oracle Database Security Products

In addition to the security resources that are available in a default database installation, Oracle Database provides several other database security products.

These products are as follows:

- Oracle Advanced Security enables you to protect sensitive data by using Transparent Data Encryption and Oracle Data Redaction.
- Oracle Label Security applies classification labels to data, allowing you to filter user access to data at the row level.
- Oracle Database Vault provides fine-grained access control to your sensitive data, including protecting data from privileged users. For example, you can restrict database administrators from having access to employee information such as salaries.
- Oracle Data Safe enables you to analyze the sensitivity and risks of data in your Oracle databases, and based on these findings, create policies that mask sensitive data, create and monitor security controls, assess user security, and monitor user activity.
- Oracle Enterprise User Security enables you to manage user security at the enterprise level.
- Oracle Enterprise Manager Data Masking and Subsetting Pack can irreversibly replace the original sensitive data with fictitious data so that production data can be shared safely with IT developers or offshore business partners.
- Oracle Audit Vault and Database Firewall collects database audit data from sources such as Oracle Database audit trail tables, database operating system audit files, and database redo logs. Using Oracle Audit Vault and Database Firewall, you can create alerts on suspicious activities, and create reports on the history of privileged user changes, schema modifications, and even data-level access.
- Oracle Key Vault enables you to accelerate security and encryption deployments by centrally managing encryption keys, Oracle wallets, Java keystores, and credential files. It is optimized for Oracle wallets, Java keystores, and Oracle Advanced Security Transparent Data Encryption (TDE) master keys. Oracle Key Vault supports the OASIS KMIP standard. The full-stack, security-hardened software appliance uses Oracle Linux and Oracle Database technology for security, availability, and scalability, and can be deployed on your choice of compatible hardware.

In addition to these products, you can find the latest information about Oracle Database security, such as new products and important information about security patches and alerts, by visiting the Security Technology Center on Oracle Technology Network at

[`http://www.oracle.com/technetwork/topics/security/whatsnew/index.html`](http://www.oracle.com/technetwork/topics/security/whatsnew/index.html)

**Parent topic:** Introduction to Oracle Database Security