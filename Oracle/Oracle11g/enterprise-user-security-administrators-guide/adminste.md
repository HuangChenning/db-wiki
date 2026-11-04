---
title: Administering Enterprise User Security
book: "Enterprise User Security Administrator's Guide"
doc_id: E10744-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10744/adminste.htm
tags:
  - oracle
  - 11g
  - enterprise-user-security-administrators-guide
---

## 5 Administering Enterprise User Security

This chapter describes how to use Oracle Enterprise Manager to administer Enterprise User Security in Oracle Databases. This chapter contains the following topics:

## 5.1 Administering Identity Management Realms

An identity management realm is a subtree of directory entries, all of which are governed by the same administrative policies. A realm Oracle Context is a subtree in a directory identity management realm that contains the data used by any installed Oracle product that uses the directory.

You can set properties of an identity management realm using Oracle Internet Directory tools like the Oracle Internet Directory Self-Service Console.

The Oracle Enterprise Manager Database Control or Grid Control Web interface enables you to manage Enterprise User Security related entries in an identity management realm.

This section describes administering identity management realms for Enterprise User Security. It contains the following topics:

- Identity Management Realm Versions
- Setting Properties of an Identity Management Realm
- Setting the Default Database-to-Directory Authentication Type for an Identity Management Realm
- Managing Identity Management Realm Administrators
	Note:
	Do not create users within a realm Oracle Context.
	See Also:
	- ["How Oracle Internet Directory Implements Identity Management"](concepts.md) for a discussion about identity management realms and realm Oracle Contexts and how they are related to one another
	- ["About Enterprise User Security Directory Entries"](concepts.md) for a discussion on the Oracle Internet Directory entries that are used for Enterprise User Security

### 5.1.1 Identity Management Realm Versions

Enterprise User Security can only use an identity management realm supplied by Oracle Internet Directory 10g (9.0.4), or later, which ships with Oracle Application Server 10g (9.0.4), or later. You can manage Enterprise User Security directory entries in a version 9.0.4 (or later) identity management realm by using Oracle Enterprise Manager for Oracle Database 11g Release 2 (11.2).

### 5.1.2 Setting Properties of an Identity Management Realm

An identity management realm has a number of properties that can be viewed and managed by using Oracle Internet Directory tools like the Oracle Internet Directory Self-Service Console. These properties are described in Table 5-1.

Table 5-1 Identity Management Realm Properties

| Property | Description |
| --- | --- |
| Attribute for Login Name | Name of the directory attribute used to store login names. By default, login names are stored in the `uid` attribute, but they can be changed to correspond to your directory configuration. In previous releases, this was the `cn` attribute. |
| Attribute for Kerberos Principal Name | Name of the directory attribute used to store Kerberos principal names. By default, Kerberos principal names are stored in the `krbPrincipalName` directory attribute, but they can be changed to correspond to your directory configuration by changing `orclCommonKrbPrincipalAttribute` in the identity management realm. |
| User Search Base | Full distinguished name (DN) for the node at which enterprise users are stored in the directory. |
| Group Search Base | Full DN for the node at which user groups are stored for this identity management realm in the directory. |
| Version Compatibility | This property is no longer used. However, you should ensure that it is not set to `81000`, because release 8.1.7 and earlier databases cannot be in the same realm with Oracle Database 10g or later databases. |

Note:

Each identity management realm includes an `orcladmin` user who is the root user of that realm only. These realm-specific `orcladmin` users are represented by the directory entries `cn=orcladmin,cn=Users,``realm_DN`. Note that when you are logged in to Enterprise User Security administration tools as a realm-specific `orcladmin` user, then you can manage only directory objects for that realm. To manage objects in another realm, you must log in to administration tools as the `orcladmin` user for that realm.

#### 5.1.2.1 Setting Login Name, Kerberos Principal Name, User Search Base, and Group Search Base Identity Management Realm Attributes

Setting these identity management realm attributes enables the database to locate Enterprise User Security entries.

To set Login Name, Kerberos Principal Name, User Search Base, and Group Search Base identity management realm attributes:

1. Log in to the Oracle Internet Directory Self-Service Console.
	Enter the URL to access the Oracle Internet Directory Self-Service Console in a browser window. For example:
	```
	http://myhost1:7777/oiddas
	```
	Log in as the `orcladmin` user.
2. Click the Configuration tab. Click the Identity Management Realm subtab.
	The Directory Configuration page appears.
3. Enter the appropriate information into the available fields.
4. Click Submit to save your changes to the directory.

See Also:

[Oracle Identity Management Guide to Delegated Administration](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIMDA) for detailed information on using the Oracle Internet Directory Self-Service Console

### 5.1.3 Setting the Default Database-to-Directory Authentication Type for an Identity Management Realm

The initial value for the `LDAP_DIRECTORY_ACCESS` parameter is picked from the default database-to-directory authentication attribute setting at the realm level. This parameter is set on individual databases when they are registered in Oracle Internet Directory.

The Oracle Enterprise Manager Database Control or Grid Control interface enables you to set the authentication mechanism that the database uses to authenticate to Oracle Internet Directory. The authentication mechanism can be set to password or SSL.

To set the default database-to-directory authentication type for an identity management realm:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click OID Realm Administration.
	The OID Realm Administration page appears. The current DB-OID authentication method is displayed.
5. To change the current DB-OID authentication method, click Change.
	The Realm Configuration page appears.
6. Select Password or SSL under DB-OID Authentication.
7. If all the databases and clients in the realm are release 10g or higher, you can turn off the password verifiers feature. This feature is used by the directory to populate an additional password field for pre-10g databases. To turn off password verifiers, deselect Password Verifiers.
8. Click OK.

### 5.1.4 Managing Identity Management Realm Administrators

An identity management realm contains administrative groups that have varying levels of privileges. The administrative groups for an identity management realm, which pertain to Enterprise User Security, are defined in Table 5-2. For more information about these groups, see ["Administrative Groups"](concepts.md).

Table 5-2 Enterprise User Security Identity Management Realm Administrators

| Administrative Group | Definition |
| --- | --- |
| Oracle Database Registration Administrators  (OracleDBCreators) | Registers new databases in the realm. |
| Oracle Database Security Administrators  (OracleDBSecurityAdmins) | Has all privileges on the OracleDBSecurity directory subtree. Creates, modifies, and can read all Enterprise User Security directory objects. |
| Oracle Context Administrators  (OracleContextAdmins) | Has full access to all groups and entries within its associated realm. |
| User Security Administrators  (OracleUserSecurityAdmins) | Has relevant permissions necessary to administer security aspects for enterprise users in the directory. For example, OracleUserSecurityAdmins can modify user passwords. |

To manage identity management realm administrators:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click OID Realm Administration.
	The OID Realm Administration page appears. This page lists the Enterprise User Security related administrative groups in the identity management realm.
5. Select the administrative group that you wish to edit. Click Edit.
	The Edit page appears. It lists the directory users that are currently members of the group selected in the OID Realm Administration page.
6. To add a directory user to the group, click Add.
	The Select Users window appears.
7. Select the Search Base. The Search Base is the directory subtree that you wish to search for locating the user. Click Go.
8. Select the user that you wish to add as an administrator. Click Select.
	The user is added in the Edit page.
9. Click OK.

## 5.2 Administering Enterprise Users

This section describes how to use Oracle Internet Directory Self-Service Console and Oracle Enterprise Manager to administer enterprise users. It contains the following topics:

- Creating New Enterprise Users
- Setting Enterprise User Passwords
- Granting Enterprise Roles to Enterprise Users
- Granting Proxy Permissions to Enterprise Users
- Creating User-Schema Mappings for Enterprise Users
- Creating Label Authorizations for Enterprise Users

### 5.2.1 Creating New Enterprise Users

You can use Oracle Internet Directory tools like the Oracle Internet Directory Self-Service Console to create users in the directory.

Note:

Before creating new enterprise users, you must first define the user search base in the directory and also verify the user create base. See "Setting Login Name, Kerberos Principal Name, User Search Base, and Group Search Base Identity Management Realm Attributes"

To create new enterprise users:

1. Log in to the Oracle Internet Directory Self-Service Console.
	Enter the URL to access the Oracle Internet Directory Self-Service Console in a browser window. For example:
	```
	http://myhost1:7777/oiddas
	```
	Log in as the `orcladmin` user.
2. Click the Directory tab. Click the Users subtab.
	The Users page appears.
3. Click Create to create a new user.
	The Create User page appears.
4. Enter the appropriate user information in the Create User page. Click Submit to create a new enterprise user.

Note:

Note that if your users are authenticated to the database by using Kerberos credentials, and the `krbPrincipalName` attribute is not there, then see ["Task 1: Configure Oracle Internet Directory Self-Service Console to display the Kerberos principal name attribute"](configur.md) for information about how to configure this.

### 5.2.2 Setting Enterprise User Passwords

You can use Oracle Internet Directory Self-Service Console to set and maintain enterprise user passwords in Oracle Internet Directory.

The enterprise user password is used for:

- Directory logon
- Database logon, to databases that support password authentication for global users

To set the password for an enterprise user:

1. Log in to the Oracle Internet Directory Self-Service Console.
	Enter the URL to access the Oracle Internet Directory Self-Service Console in a browser window. For example:
	```
	http://myhost1:7777/oiddas
	```
	Log in as the `orcladmin` user.
2. Click the Directory tab. Click the Users subtab.
	The Users page appears.
3. Enter part of the enterprise user's user name (login name) or e-mail address in the Search field. Click Go.
	A list of all users who match your search criteria displays.
4. Select the user for whom you wish to create a new password. Click Edit.
	The Edit User page appears.
5. Enter the new password in the Password field. Confirm the password in the Confirm Password field. Click Submit.

### 5.2.3 Granting Enterprise Roles to Enterprise Users

Enterprise roles are directory objects that allow you to group global roles from various databases. You can assign enterprise roles to enterprise users, which gives them privileges across enterprise databases.

To grant enterprise roles to enterprise users:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Configure Enterprise Users.
	The Configure Enterprise Users page appears.
5. Select the Search Base in which the enterprise user is located. The search base is the subtree which contains the enterprise user entry. You can optionally enter the common name of the enterprise user in the Name field. Select User in the View box. Click Go.
	A list of users with matching criteria appears.
6. Select the enterprise user that you wish to configure. Click Configure.
	The Configure User page appears.
7. Click the Enterprise Roles tab.
8. Click Grant.
	The Select Enterprise Roles window appears.
9. Select the enterprise role that you wish to grant. Click Select.
10. Click OK in the Configure User page.

### 5.2.4 Granting Proxy Permissions to Enterprise Users

Proxy permissions allow an enterprise user to proxy a local database user, which means that the enterprise user can log in to the database as the local database user. You can grant proxy permissions to individual users or groups. Proxy permissions are especially useful for middle tier applications that operate across multiple databases as enterprise users.

Proxy permissions are created at the enterprise domain level. After creating a proxy permission for an enterprise domain, you can grant it to an enterprise user.

To grant proxy permissions to enterprise users:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Configure Enterprise Users.
	The Configure Enterprise Users page appears.
5. Select the Search Base in which the enterprise user is located. The search base is the subtree which contains the enterprise user entry. You can optionally enter the common name of the enterprise user in the Name field. Select User in the View box. Click Go.
	A list of users with matching criteria appears.
6. Select the enterprise user that you wish to configure. Click Configure.
	The Configure User page appears.
7. Click the Proxy Permissions tab.
8. Click Grant.
	The Select Proxy Permissions window appears.
9. Select the Proxy Permission to be granted. The proxy permission must have already been created for the enterprise domain. Click Select.
10. Click OK in the Configure User page.

### 5.2.5 Creating User-Schema Mappings for Enterprise Users

A user-schema mapping maps an enterprise user to a global database schema. When the enterprise user logs in to the database, he is connected to the mapped schema, by default.

To create a user-schema mapping:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Configure Enterprise Users.
	The Configure Enterprise Users page appears.
5. Select the Search Base in which the enterprise user is located. The search base is the subtree which contains the enterprise user entry. You can optionally enter the common name of the enterprise user in the Name field. Select User in the View box. Click Go.
	A list of users with matching criteria appears.
6. Select the enterprise user that you wish to configure. Click Configure.
	The Configure User page appears.
7. Click the User-Schema Mappings tab. All user-schema maps that apply to the user directly or indirectly are displayed.
	A user can be individually mapped to a schema. Alternatively, you can map a directory subtree containing multiple users to the database schema.
8. Click Create.
	The Create Mapping page is displayed.
9. Under the From section, select Users to map an individual enterprise user to a database schema. Alternatively, select Subtree to map a directory subtree containing multiple users.
10. Under To, select Database to map to a database schema. Select Domain to map to a schema common to all databases in the enterprise domain.
	You can have multiple databases in an enterprise domain that have a common schema name. When you map an enterprise user to such a schema, the enterprise user is automatically mapped to the individual schemas in each database contained in the domain.
11. If you selected Database in the preceding step, then select the name of the database that contains the schema. Next, enter the database schema name. You can also use the search icon to select the schema. You will be required to log in to the database to select the schema.
	If you selected Domain in the preceding step, then select the name of the domain and enter the common schema name in the Schema field.
12. Click Continue in the Create Mapping page.
13. Click OK in the Configure User page.

### 5.2.6 Creating Label Authorizations for Enterprise Users

An Oracle Label Security (OLS) policy stored in the directory can have multiple profiles associated with it. Each profile is a set of policy authorizations and privileges. These policy authorizations and privileges apply to all enterprise users who belong to the profile. You can assign a profile to an enterprise user.

To assign label authorizations to an enterprise user:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Configure Enterprise Users.
	The Configure Enterprise Users page appears.
5. Select the Search Base in which the enterprise user is located. The search base is the subtree which contains the enterprise user entry. You can optionally enter the common name of the enterprise user in the Name field. Select User in the View box. Click Go.
	A list of users with matching criteria appears.
6. Select the enterprise user that you wish to configure. Click Configure.
	The Configure User page appears.
7. Click the Label Authorizations tab.
	A list of all user profiles associated with the user is displayed.
8. Click Add.
	The Select User Profile window appears.
9. Select the user profiles that you want the user to be added to, and click Select. You can only select one profile per policy.
10. Click OK in the Configure User page.

## 5.3 Configuring User-Defined Enterprise Groups

User-defined enterprise groups help group together enterprise users that require the same roles or privileges across enterprise databases. Enterprise groups are stored in the directory.

### 5.3.1 Granting Enterprise Roles to User-Defined Enterprise Groups

Enterprise roles are directory objects that allow you to group global roles from various databases. You can assign an enterprise role to an enterprise group, which gives the group members privileges across enterprise databases.

To grant an enterprise role to an enterprise group:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Configure User Defined Enterprise Groups.
	The Configure Enterprise Groups page appears.
5. Select the Search Base in which the enterprise group is located. The search base is the subtree which contains the enterprise group entry. Optionally, enter the common name of the enterprise group in the Name field. Select Group in the View box. Click Go.
	A list of groups with matching criteria appears.
6. Select the enterprise group that you wish to configure. Click Configure.
	The Configure Group page appears.
7. Click the Enterprise Roles tab.
	A list of enterprise roles granted to the enterprise group is displayed.
8. Click Grant to grant a new enterprise role to the group.
	The Select Enterprise Roles window appears.
9. Select the enterprise roles that you wish to grant. Click Select.
10. Click OK in the Configure Group page.

## 5.4 Configuring Databases for Enterprise User Security

Enterprise User Security for databases registered with Oracle Internet Directory can be configured using Enterprise Manager. You can map users or subtrees to database schemas. You can also configure administrators in the directory that can modify schema mappings and enterprise domain membership of the database.

### 5.4.1 Creating User-Schema Mappings for a Database

A user-schema mapping maps an enterprise user to a global schema in the database. When the enterprise user logs in to the database, he is connected to the mapped schema, by default.

To create a user-schema mapping:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Configure Databases.
	The Configure Databases page appears. A list of databases registered in the identity management realm is displayed.
5. Select the database name. Click Configure.
	The Configure Database page appears.
6. Click the User-Schema Mappings tab. All user-schema maps created at the database level are displayed. User-schema maps created at the enterprise domain levels are not displayed here.
7. Click Create to create a new user-schema mapping for the database.
	The Create Mapping page is displayed.
8. Under the From section, select Users to map an individual enterprise user to a database schema. Alternatively, select Subtree to map a directory subtree containing multiple users. You can use the Search icon to search for the appropriate user or subtree.
9. Under the To section, enter the name of the Schema to which the user or subtree should be mapped. You can use the search icon to search for the appropriate schema in the database. You will be required to log in to the database to access the schema names.
10. Click Continue in the Create Mapping page.
11. Click OK in the Configure Database page.

### 5.4.2 Adding Administrators to Manage Database Schema Mappings

Directory users who are authorized to manage database schema mappings for a database can create or delete database schema mappings for the database.

To add administrators for managing database schema mappings:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Configure Databases.
	The Configure Databases page appears. A list of databases registered in the identity management realm is displayed.
5. Select the database name. Click Configure.
	The Configure Database page appears.
6. Click the Administrators tab. A list of administrators who can manage database schema mappings is displayed.
7. Click Add to add an administrator.
	The Select Users window appears.
8. Select the Search Base. The Search Base is the directory subtree that you wish to search for locating the user. Click Go.
9. Select the user that you wish to add as an administrator. Click Select.
	The user is added in the Configure Database page.
10. If you want the user to be able to add or remove other administrators, then select the Admin Group Owner check box corresponding to the added user.
11. Click OK.

## 5.5 Administering Enterprise Domains

Enterprise Domains are groups of databases that can share enterprise roles, proxy permissions, user-schema mappings, current user database links, and permitted authentication mechanisms. A database can belong to only one enterprise domain.

An enterprise domain can be thought of as an administrative domain, administered by the Domain Admins group for that domain. These administrators can add databases to the enterprise domain.

An identity management realm contains an enterprise domain called `OracleDefaultDomain`. `OracleDefaultDomain` is part of the realm when it is first created in the directory. When a new database is registered into a realm, it automatically becomes a member of `OracleDefaultDomain` in that realm. You can create and remove your own enterprise domains, but you must not remove `OracleDefaultDomain` from a realm.

This section describes how to use Oracle Enterprise Manager to administer enterprise domains in the directory. It contains the following topics:

- Creating an Enterprise Domain
- Adding Databases to an Enterprise Domain
- Creating User-Schema Mappings for an Enterprise Domain
- Configuring Enterprise Roles
- Configuring Proxy Permissions
- Configuring User Authentication Types and Enabling Current User Database Links
- Configuring Domain Administrators

### 5.5.1 Creating an Enterprise Domain

An enterprise domain is an administrative domain of databases that can share enterprise roles, proxy permissions, user-schema mappings, current user database links, and permitted authentication mechanisms.

If you do not want to use `OracleDefaultDomain`, then you can create a new enterprise domain in your identity management realm.

To create an enterprise domain:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Manage Enterprise Domains.
	The Manage Enterprise Domains page appears. This page lists the enterprise domains in the identity management realm.
5. Click Create to create a new enterprise domain.
	The Create Domain page appears.
6. Enter the name for the new enterprise domain in the Name field. Click OK.
	The new enterprise domain is added to the list of enterprise domains in the Enterprise Domains page.

### 5.5.2 Adding Databases to an Enterprise Domain

A member of the Domain Admins group can add databases to the enterprise domain. You can add databases to an enterprise domain from the Configure Domain page. You can also add databases from the Create Domain page, if you are creating a new enterprise domain.

Note:

The following restrictions apply to adding databases to an enterprise domain:
- You can add a database to an enterprise domain only if both the database and the enterprise domain exist in the same realm.
- A database cannot be added as a member of two different enterprise domains.

To add databases to an enterprise domain:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Manage Enterprise Domains.
	The Manage Enterprise Domains page appears. This page lists the enterprise domains in the identity management realm.
5. Select the enterprise domain that you wish to configure. Click Configure.
	The Configure Domain page appears.
6. Make sure that the Databases tab is selected. Click Add to add new databases to the enterprise domain.
	The Select Databases page appears. A list of databases, that are registered with the identity management realm, is displayed. You can add a database only if it is not part of any other enterprise domain.
7. Select the databases to add. Click Select.
8. Click OK in the Configure Domain page.

### 5.5.3 Creating User-Schema Mappings for an Enterprise Domain

A user-schema mapping maps an enterprise user to a global schema in the database. When the enterprise user logs in to the database, he is connected to the mapped schema, by default.

When you create a user-schema mapping for an enterprise domain, it applies to all databases in the domain. However, for the mapping to be effective in a database, that database must have a schema with the name used in the mapping.

To create a user-schema mapping for an enterprise domain:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Manage Enterprise Domains.
	The Manage Enterprise Domains page appears. This page lists the enterprise domains in the identity management realm.
5. Select the enterprise domain that you wish to configure. Click Configure.
	The Configure Domain page appears.
6. Click the User-Schema Mappings tab. All user-schema maps created at the domain level are displayed. User-schema maps created at database levels are not displayed here.
7. Click Create to create a new user-schema mapping for the domain.
	The Create Mapping page is displayed.
8. Under the From section, select Users to map an individual enterprise user to a database schema. Alternatively, select Subtree to map a directory subtree containing multiple users. You can use the Search icon to search for the appropriate user or subtree.
9. Under the To section, enter the name of the Schema to which the user or subtree should be mapped.
10. Click Continue in the Create Mapping page.
11. Click OK in the Configure Domain page.

### 5.5.4 Configuring Enterprise Roles

An [enterprise domain](glossary.md) within an identity management realm can contain multiple [enterprise role](glossary.md) s. An enterprise role is a set of Oracle role-based [authorization](glossary.md) s across one or more databases in an enterprise domain.

Enterprise roles allow you to group global roles from different databases that are part of the enterprise domain. Enterprise roles can be assigned to enterprise users.

To create enterprise roles:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Manage Enterprise Domains.
	The Manage Enterprise Domains page appears. This page lists the enterprise domains in the identity management realm.
5. Select the enterprise domain that you wish to configure. Click Configure.
	The Configure Domain page appears.
6. Click the Enterprise Roles tab.
7. Click Create to create a new enterprise role.
	The Create Enterprise Role page appears.
8. Enter a name for the enterprise role in the Name field. Click Continue.
	The new role is displayed in the Configure Domain page.

Next, you can configure the enterprise role that you just created. Configuring an enterprise role includes adding database global roles to the enterprise role and assigning the enterprise role to enterprise users or groups.

To add database global roles to the enterprise role:

1. Select the enterprise role that you just created in the Configure Domain page. Click Edit.
	The Edit Enterprise Role page is displayed.
2. Make sure that the DB Global Roles tab is selected. Click Add to add global roles from databases that are part of the enterprise domain.
	The Search and Select Database Global Roles page appears.
3. Select the Database that contains the global roles you wish to add. Log in to the selected database by supplying a User Name and Password. Click Go.
4. Select the global roles to add. Click Select.
	The selected roles appear in the Edit Enterprise Role page.
5. Repeat steps [^1] to [^2] for the other databases.

You can now assign the enterprise role to enterprise users or groups.

To assign the enterprise role to enterprise users or groups:

1. Click the Grantees tab in the Edit Enterprise Role page.
2. Click Add.
	The Select Users or Groups page is displayed.
3. Select the Search Base or the subtree that contains the user or group. Select User under View if you are granting the enterprise role to a user. Select Group under View, if you are granting the role to a group. Optionally, enter the common name of the user or group in the Name field. Click Go.
4. Select the users or groups to be granted the enterprise role. Click Select.
5. Click Continue in the Edit Enterprise Role page.
6. Click OK in the Configure Domain page.

### 5.5.5 Configuring Proxy Permissions

Proxy permissions are created at the enterprise domain level. Proxy permissions allow an enterprise user to proxy a local database user, which means that the enterprise user can log in to the database as the local database user. You can grant proxy permissions to individual enterprise users or groups. Proxy permissions are especially useful for middle tier applications that operate across multiple databases as enterprise users.

To create a proxy permission for an enterprise domain:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Manage Enterprise Domains.
	The Manage Enterprise Domains page appears. This page lists the enterprise domains in the identity management realm.
5. Select the enterprise domain that you wish to configure. Click Configure.
	The Configure Domain page appears.
6. Click the Proxy Permissions tab.
7. Click Create to create a new proxy permission.
	The Create Proxy Permission page appears.
8. Enter the name for the proxy permission in the Name field. Click Continue.
	The proxy permission appears in the Configure Domain page.

Next, you need to add target database users for the permission. You also need to grant the permission to enterprise users or groups, who can then proxy the target database users.

To add target database users for the proxy permission:

1. Select the proxy permission that you just created in the Configure Domain page. Click Edit.
	The Edit Proxy Permissions page appears.
2. Ensure that the Target DB Users tab is selected. Click Add.
	The Search and Select window appears. A list of all database users that have been altered to allow enterprise user proxy is displayed.
3. Select the target database users that you wish to proxy. Click Select.

You can now grant the proxy permission to enterprise users or groups.

To grant the proxy permission to an enterprise user or group:

1. Click the Grantees tab in the Edit Proxy Permission page.
2. Click Add.
	The Select Users or Groups window appears.
3. Select the Search Base or the subtree that contains the user or group. Select User under View if you are granting the proxy permission to a user. Select Group under View, if you are granting the proxy permission to a group. Optionally, enter the common name of the user or group in the Name field. Click Go.
4. Select the Users or Groups to grant them the proxy permission. Click Select.
5. Click Continue in the Edit Proxy Permission page.
6. Click OK in the Configure Domain page.

### 5.5.6 Configuring User Authentication Types and Enabling Current User Database Links

Enterprise users can be authenticated using password authentication, SSL authentication, or Kerberos authentication. You can set the authentication modes that are allowed for an enterprise domain using Enterprise Manager. You can also enable current user database links for databases in the enterprise domain. These links enable databases to trust each other to authenticate users.

To configure user authentication types and enable current user database links:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Manage Enterprise Domains.
	The Manage Enterprise Domains page appears. This page lists the enterprise domains in the identity management realm.
5. Select the enterprise domain that you wish to configure. Click Configure.
	The Configure Domain page appears.
6. Click the Configuration tab.
7. Under User Authentication Types Accepted, select the authentication types that you want to allow.
8. If you wish to enable current user database links for the domain, then select Enable Current User Database Links in this domain.
9. Click OK.

### 5.5.7 Configuring Domain Administrators

Domain administrators have full privileges in the domain. They can add or remove databases to the domain, create user-schema mappings, manage proxy permissions and modify domain configuration settings. You can add or remove domain administrators from Enterprise Manager.

To add an enterprise domain administrator:

1. Log in to Enterprise Manager.
2. Click the Server tab. Under the Security section, click Enterprise User Security.
	The Oracle Internet Directory Login page appears.
3. Enter the distinguished name (DN) of a directory user who can administer enterprise users in the User field. Enter the user password in the Password field. Click Login.
	The Enterprise User Security page appears.
4. Click Manage Enterprise Domains.
	The Manage Enterprise Domains page appears. This page lists the enterprise domains in the identity management realm.
5. Select the enterprise domain that you wish to configure. Click Configure.
	The Configure Domain page appears.
6. Click the Administrators tab. A list of administrators for the enterprise domain is displayed.
7. Click Add to add an administrator.
	The Select Users window appears.
8. Select the Search Base. The Search Base is the directory subtree that you wish to search for locating the user. Click Go.
9. Select the user that you wish to add as an administrator. Click Select.
	The user is added in the Configure Domain page.
10. If you want the user to be able to add or remove other administrators, then select the Admin Group Owner check box corresponding to the added user.
11. Click OK.

[^1]: Make sure that the DB Global Roles tab is selected. Click Add to add global roles from databases that are part of the enterprise domain.

The Search and Select Database Global Roles page appears.

[^undefined]: Select the Database that contains the global roles you wish to add. Log in to the selected database by supplying a User Name and Password. Click Go.

[^2]: Select the global roles to add. Click Select.

The selected roles appear in the Edit Enterprise Role page.

[^undefined]: Repeat steps 2 to 4 for the other databases.