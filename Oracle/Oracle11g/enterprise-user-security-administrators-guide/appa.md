---
title: Using the User Migration Utility
book: "Enterprise User Security Administrator's Guide"
doc_id: E10744-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10744/appa.htm
tags:
  - oracle
  - 11g
  - enterprise-user-security-administrators-guide
---

## A Using the User Migration Utility

This chapter describes the User Migration Utility. You can use it to perform bulk migrations of database users to an LDAP directory, where they can be stored and managed centrally as enterprise users. It contains the following topics:

## A.1 Benefits of Migrating Local or External Users to Enterprise Users

Migrating from a database user model to an enterprise user model provides solutions to administrative, security, and usability challenges in an enterprise environment. In an enterprise user model, all user information is moved to an LDAP directory service.

Enterprise user security provides the ability to easily and securely manage enterprise wide users by providing the following benefits:

- Centralized storage of user credentials, roles, and privileges in an LDAP version 3-compliant directory server
- Provides the infrastructure to enable single sign-on using X.509v3-compliant certificates, typically deployed where end-to-end SSL is required
- Enhanced security through more timely maintenance and fewer user passwords
	The centralization of user information inherent in the enterprise user model makes it easier to manage. Security administrators can perform necessary maintenance changes to user information immediately, thereby maintaining better control over access to critical network resources. In addition, users find the enterprise user model easier to use because they have fewer passwords to remember. So, they are less likely to choose easily guessed passwords or to write them down where others can copy them.
	See Also:
	["Introduction to Enterprise User Security"](concepts.md) for detailed conceptual information about enterprise user security

## A.2 Introduction to the User Migration Utility

The User Migration Utility is a command-line utility that enables enterprise user administrators to move their users from a local database model to an enterprise user model. You can easily migrate thousands of local and external database users to an enterprise user environment in an LDAP directory where they can be managed from a central location. The utility connects to the database using the Oracle JDBC OCI driver.

Enterprise user administrators can select for migration any combination of the following user subsets in a database:

- - List of users specified on the command line or in a file
		- All external users
		- All global users

In addition, enterprise user administrators can specify values for utility parameters that determine how the users are migrated such as

- - Where to put the migrated users in the LDAP directory tree
		- Map a user with multiple accounts on various databases to a single directory user entry

The following sections explain the migration process and the changes that occur to user schemas.

Note:

After external users are migrated, their external authentication and authorization mechanisms are replaced by directory-based mechanisms. New passwords are randomly generated for migrated users if they are mapped to newly created directory entries.

### A.2.1 Bulk User Migration Process Overview

Bulk user migration is a two-phase process. In Phase One, you start the migration process by populating user information into an interface database table. Enterprise user administrators then verify that the information is accurate before completing the migration with Phase Two, which commits the changes to the database and the directory. The process is described in the following steps:

- Step 1: (Phase One) Preparing for the Migration
- Step 2: Verify User Information
- Step 3: (Phase Two) Completing the Migration

#### A.2.1.1 Step 1: (Phase One) Preparing for the Migration

In the first part of the migration process, the utility checks if the `ORCL_GLOBAL_USR_MIGRATION_DATA` interface table exists in the enterprise user administrator's schema. If it exists, then the administrator can choose to reuse the table (clearing its contents), reuse the table and its contents, or re-create the table. Phase One can be run multiple times, each time adding to the interface table. If the table does not exist, then the utility creates it in the administrator's schema. The interface table is populated with information about the migrating users from the database and the directory. The command-line options used determine what information populates this table.

Note:

The utility will not create the interface table in the `SYS` schema.

#### A.2.1.2 Step 2: Verify User Information

This is an intermediate step to allow the enterprise user administrator to verify that the user information is correct in the interface table before committing the changes to the database and the directory.

#### A.2.1.3 Step 3: (Phase Two) Completing the Migration

After the interface table user information is checked, Phase Two begins. The utility retrieves the information from the table and updates the directory and the database.

Depending on whether directory entries exist for migrating users, the utility creates random passwords as follows:

- If migrating users are being mapped to newly created directory entries, then the utility generates random passwords, which are used as credentials for both the database and directory.
- If migrating users are being mapped to existing directory entries with unset database passwords, then the utility generates random database passwords only.

In either case, after generating the required random passwords, the utility then stores them in the `DBPASSWORD` and `DIRPASSWORD` interface table columns. The enterprise user administrator can read these passwords from the interface table and inform migrating users.

See Also:

"User Migration Utility Parameters" for a list of command-line options and their descriptions

### A.2.2 About the ORCL\_GLOBAL\_USR\_MIGRATION\_DATA Table

This is the interface table which is populated with information about the migrating users during Phase One of the bulk user migration process. The information that populates this table is pulled from the database and checked against existing entries in the directory. If there is corresponding information in the directory, then that is marked in the table for that user. After enterprise user administrators verify the information in this table, changes are made to the directory and the database in Phase Two.

Caution:

The `ORCL_GLOBAL_USR_MIGRATION_DATA` interface table contains very sensitive information. Access to it should be tightly controlled using database privileges.

The table columns are listed in Table A-1.

Table A-1 ORCL\_GLOBAL\_USR\_MIGRATION\_DATA Table Schema

| Column Name | Data Type | Null | Description |
| --- | --- | --- | --- |
| `USERNAME` (Primary Key) | VARCHAR2(30) | NOT NULL | Database user name |
| `OLD_SCHEMA_TYPE` | VARCHAR2(10) | \- | Old schema type in the database before migration |
| `PASSWORD_VERIFIER` | VARCHAR2(30) | \- | Not used |
| `USERDN` | VARCHAR2(4000) | \- | Distinguished Name (DN) of the user in the directory (new or existing) |
| `USERDN_EXIST_FLAG` | CHAR(1) | \- | Flag indicating whether the DN already exists in the directory |
| `SHARED_SCHEMA` | VARCHAR2(30) | \- | Shared schema name, if users are to be mapped to a shared schema during phase two |
| `MAPPING_TYPE` | VARCHAR2(10) | \- | Mapping type (database or domain) |
| `MAPPING_LEVEL` | VARCHAR2(10) | \- | Mapping level (entry or subtree) |
| `CASCADE_FLAG` | CHAR(1) | \- | Cascade flag used when dropping a user (for shared schema mapping only) |
| `DBPASSWORD_EXIST_FLAG` | CHAR(1) | \- | Flag indicating whether the database password verifier already exists in the directory for this user |
| `DBPASSWORD` | VARCHAR2(30) | \- | Randomly generated database password verifiers to be stored in the directory |
| `DIRPASSWORD` | VARCHAR2(30) | \- | Randomly generated directory password for new entries |
| `PHASE_COMPLETED` | VARCHAR2(10) | \- | Information about the phase that has been completed successfully |
| `NEEDS_ATTENTION_FLAG` | CHAR(1) | \- | Flag indicating whether the row contains abnormalities that require administrator attention |
| `ATTENTION_DESCRIPTION` | VARCHAR2(100) | \- | Textual hint for the administrator if the attention flag is set |
| `KERBEROS_PNAME` | VARCHAR2(30) | \- | Kerberos Principal Name for external kerberos users |

#### A.2.2.1 Which Interface Table Column Values Can Be Modified Between Phase One and Phase Two?

After running phase one of the utility, if necessary, enterprise user administrators can change the interface table columns listed in Table A-2.

Table A-2 Interface Table Column Values That Can Be Modified Between Phase One and Phase Two

| Column Name | Valid Values | Restrictions |
| --- | --- | --- |
| `USERDN` | DN of user | If this value is changed, then the administrator should verify that the `USERDN_EXIST_FLAG` and the `DBPASSWORD_EXIST_FLAG` values are set accordingly. |
| `USERDN_EXIST_FLAG` | `T` / `F` | If the `USERDN` column value changes, then this column value should also change to reflect the new `USERDN` status. |
| `DBPASSWORD_EXIST_FLAG` | `T` / `F` | If the `USERDN` column value changes, then this column value should also change to reflect whether a database password exists for the new `USERDN`. |
| `SHARED_SCHEMA` | Shared schema name | Specify only if a shared schema exists in the database. |
| `MAPPING_TYPE` | `DB` / `DOMAIN` | Set this value only if `SHARED_SCHEMA` is not set to `NULL`. |
| `MAPPING_LEVEL` | `ENTRY` / `SUBTREE` | Set this value only if `SHARED_SCHEMA` is not set to `NULL`. |
| `CASCADE_FLAG` | `T` / `F` | Set this value only if `SHARED_SCHEMA` is not set to `NULL`. If this column is set to true (`T`), then the users' schema objects are forcibly deleted. If this column is set to false (`F`), then the administrator must delete all user schema objects before going into Phase Two. |
| `PHASE_COMPLETED` | `ZERO` / `ONE` / `TWO` | If the administrator can resolve the conflicts or ambiguities specified with the `NEEDS_ATTENTION_FLAG`, then this column value can be changed to `ONE` so phase two can be run with the utility. |

### A.2.3 Migration Effects on Users' Old Database Schemas

If shared schema mapping is not used, then users retain their old database schemas. If shared schema mapping is used, then users' local schemas are dropped from the database, and they are mapped to a shared schema that the enterprise user administrator creates for this purpose before performing the migration. When migrated users own database objects in their old local database schemas, administrators can specify that the schema and objects are not to be dropped by setting the `CASCADE` parameter to `NO`. When the `CASCADE` parameter is set to `NO`, users who own database objects in their old local schemas do not migrate successfully so their objects are not dropped.

If some users want to retain the objects in their local database schemas and be mapped to a shared schema, then the administrator can manually migrate those objects to the shared schema before performing the bulk user migration. However, when objects are migrated to a shared schema, they are shared among all users who share that new schema.

Table A-3 summarizes the effects of setting the `MAPSCHEMA` and `CASCADE` parameters.

Table A-3 Effects of Choosing Shared Schema Mapping with CASCADE Options

| MAPSCHEMA Parameter Setting | CASCADEParameter Setting | User MigrationSuccessful? | User SchemaObjects Dropped? |
| --- | --- | --- | --- |
| PRIVATE | NO (default setting) | Yes | No |
| SHARED | NO | Yes <sup>Foot 1</sup> | No |
| SHARED | YES | Yes <sup>Foot 2</sup> | Yes |

<sup>Footnote 1</sup> Users migrate successfully only if they do not own objects in their old database schemas; otherwise, they fail.

<sup>Footnote 2</sup> Users migrate successfully, and their old database schemas are dropped.

See Also:

"User Migration Utility Parameters" for detailed information about the `MAPSCHEMA`, `CASCADE`, and other parameters that can be used with this utility

### A.2.4 Migration Process

Enterprise users are defined and managed in the directory and can be authenticated to the database either with a password or with a certificate. Users who authenticate with a password require an Oracle Database password, which is stored in the directory. Users who authenticate with a certificate must have a valid X.509 v3 certificate.

This utility performs the following steps during migration:

1. Selects the users from the database for migration.
2. Creates corresponding user entries or uses existing entries in the directory.
3. Creates new database passwords and copies the corresponding verifiers to the directory for migrating users.
4. Puts the schema mapping information for the migrating users' entries in the directory. (optional)
5. Drops or alters the migrating users' local database schemas. (optional)
	Note:
	In the current release, the utility migrates users with certificate-based authentication and makes them ready for password authentication. Previously, SSL-based authenticated users were required to reset their Oracle Database passwords. User wallets are not created as part of this process.
	See Also:
	[The chapter about Oracle Wallet Manager](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asowalet.htm#ASOAG160) in Oracle Database Advanced Security Administrator's Guide for information about creating, managing, and using Oracle wallets

## A.3 Prerequisites for Performing Migration

The User Migration Utility is automatically installed in the following location when you install Oracle Database Client:

```
$ORACLE_HOME/rdbms/bin/umu
```

The following sections describe what programs must be running and what user privileges are required to successfully migrate users with the User Migration Utility.

### A.3.1 Required Database Privileges

To successfully use this utility, enterprise user administrators must have the following database privileges:

- ALTER USER
- DROP USER
- CREATE TABLE
- SELECT\_CATALOG\_ROLE

These privileges enable the enterprise user administrator to alter users, drop users, look at dictionary views, and create the interface table that is used by this utility.

### A.3.2 Required Directory Privileges

In addition to the required database privileges, enterprise user administrators must have the directory privileges which allow them to perform the following tasks:

- Create entries in the directory under the specified user base and Oracle context location
- Browse the user entries under the search bases

### A.3.3 Required Setup to Run the User Migration Utility

Perform the following steps before using the User Migration Utility:

1. Ensure that the directory server is running with SSL enabled for no authentication.
2. Ensure that the database server is running with encryption and integrity enabled.
3. Ensure that the database listener has a TCP listening end point.
4. Create an identity management realm in the directory, if it does not already exist.
5. Create the parent context for the user entries in the directory, if it does not already exist. The default (and recommended) location is in the `orclcommonusercreatebase` subtree in the common container in the Oracle Context.
6. Set up directory access for the database Oracle home by using Oracle Net Configuration Assistant to create an `ldap.ora` file. Note that the `ldap.ora` file must include the identity management realm DN so the utility can locate the correct administrative context. The utility searches for this file under `$LDAP_ADMIN`, `$ORACLE_HOME/ldap/admin`, `$TNS_ADMIN`, `$ORACLE_HOME/network/admin`, and, finally, the Domain Name System (DNS) server, if you are using DNS discovery. (See [Oracle Internet Directory Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIDAG) for information about DNS server discovery.)
	Note:
	- If you plan to use shared schema mapping when migrating users, then you must create the shared schema before running this utility.
	- The same `ldap.ora` file must be used for both Phase One and Phase Two of a user migration.
	See Also:
	- [Chapter 4, "Enterprise User Security Configuration Tasks and Troubleshooting"](configur.md) for detailed information about setting up enterprise user authentication after the user migration is finished
	- [Oracle Internet Directory Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIDAG)

## A.4 User Migration Utility Command-Line Syntax

To perform a bulk migration of database users to enterprise users, use the following syntax:

```
umu parameter1 parameter2 ...
```

For parameters that take a single value use the following syntax:

```
keyword=value
```

For parameters that take multiple values, use a colon (:) to separate the values as in the following syntax:

```
keyword=value1:value2:...
```

Example A-1 shows the syntax used to run the utility through both phases of the bulk user migration process.

Example A-1 User Migration Utility Command-Line Syntax

```
umu PHASE=ONE
```
```
DBADMIN=dba_username:password
ENTADMIN=enterprise_admin_DN:password
USERS=[ALL_GLOBAL | ALL_EXTERNAL | LIST | FILE]
DBLOCATION=database_host:database_port:database_sid
DIRLOCATION=ldap_directory_host:ldap_directory_port
USERSLIST=username1:username2:username3:...
USERSFILE=filename
MAPSCHEMA=[PRIVATE | SHARED]:schema_name
MAPTYPE=[DB | DOMAIN]:[ENTRY | SUBTREE]
CASCADE=[YES | NO]
CONTEXT=user_entries_parent_location
LOGFILE=filename
PARFILE=filename
KREALM=EXAMPLE.COM
```
```
umu PHASE=TWO
```
```
DBADMIN=dba_username:password
ENTADMIN=enterprise_admin_DN:password
DBLOCATION=database_host:database_port:database_sid
DIRLOCATION=ldap_directory_host:ldap_directory_port
LOGFILE=filename
PARFILE=filename
```

Note:

If the enterprise user administrator does not specify the mandatory parameters on the command line, then the utility will prompt the user for those parameters interactively.

See Also:

- "User Migration Utility Parameters" for a complete list of all available parameters and detailed information about them
- "User Migration Utility Usage Examples" for examples of typical utility uses

## A.5 Accessing Help for the User Migration Utility

To display the command-line syntax for using the User Migration Utility, enter the following command at the system prompt:

```
umu HELP=YES
```

While the `HELP` parameter is set to `YES`, the utility cannot run.

## A.6 User Migration Utility Parameters

The following sections list the available parameter keywords and the values that can be used with them when running this utility. The keywords are not case-sensitive.

### A.6.1 Keyword: HELP

| Attribute | Description |
| --- | --- |
| Valid Values: | `YES` or `NO` (These values are not case-sensitive.) |
| Default Setting: | `NO` |
| Syntax Examples: | `HELP=YES` |
| Description: | This keyword is used to display Help for the utility. `YES` displays the complete command-line syntax. To run a command, set the value to `NO`, or do not specify a value for the parameter to accept the default. |
| Restrictions: | None |

### A.6.2 Keyword: PHASE

| Attribute | Description |
| --- | --- |
| Valid Values: | `ONE` or `TWO` (These values are not case-sensitive.) |
| Default Setting: | `ONE` |
| Syntax Examples: | `PHASE=ONE`  `PHASE=TWO` |
| Description: | Indicates the phase for the utility. If it is `ONE`, then the utility populates the interface table with the information specified in the command-line arguments and the existing user entries in the directory. If it is `TWO`, then the utility uses the information that is available in the interface table and updates the directory and the database. |
| Restrictions: | None |

### A.6.3 Keyword: DBLOCATION

| Attribute | Description |
| --- | --- |
| Valid Values: | host:port:sid |
| Default Setting: | No default setting |
| Syntax Examples: | `DBLOCATION=my_oracle.us.example.com:7777:ora902` |
| Description: | Provides the host name, port number, and SID for the database instance |
| Restrictions: | - This parameter is mandatory. - The value for this parameter must be the same for both Phase One and Phase Two. - The database should be configured for encryption and integrity. |

### A.6.4 Keyword: DIRLOCATION

| Attribute | Description |
| --- | --- |
| Valid Values: | host:port |
| Default Setting: | This value is automatically populated from the `ldap.ora` file by default. |
| Syntax Examples: | `DIRLOCATION=my_oracle.us.example.com:636` |
| Description: | Provides the host name and port number for the directory server where the LDAP server is running on SSL with no authentication |
| Restrictions: | The value for this parameter must be the same for both Phase One and Phase Two. |

### A.6.5 Keyword: DBADMIN

| Attribute | Description |
| --- | --- |
| Valid Values: | username:password |
| Default Setting: | No default setting |
| Syntax Examples: | `DBADMIN=system:manager` |
| Description: | User name and password for the database administrator with the required privileges for connecting to the database |
| Restrictions: | - This parameter is mandatory. - The `username` value for this parameter must be the same for both Phase One and Phase Two. |

### A.6.6 Keyword: ENTADMIN

| Attribute | Description |
| --- | --- |
| Valid Values: | userDN:password |
| Default Setting: | No default setting |
| Syntax Examples: | `ENTADMIN=cn=janeadmin,dc=acme,dc=com:Easy2rem` |
| Description: | User Distinguished Name (UserDN) and the directory password for the enterprise directory administrator with the required privileges for logging in to the directory. UserDN can also be specified within double quotation marks (""). |
| Restrictions: | This parameter is mandatory. |

### A.6.7 Keyword: USERS

| Attribute | Description |
| --- | --- |
| Valid Values: | value1:value2...  Values can be:  - `ALL_EXTERNAL` to select all external users, including those who use Kerberos and RADIUS authentication - `ALL_GLOBAL` to select all global users - `LIST` to specify users on the command line with "Keyword: USERSLIST" - `USERSFILE` for selecting users from the file that is specified with the "Keyword: USERSFILE"  This parameter takes multiple values. Separate values with a colon (:).  (These values are not case-sensitive.) |
| Default Setting: | No default setting |
| Syntax Examples: | - `USERS=ALL_EXTERNAL:ALL_GLOBAL` 	This usage instructs the utility to migrate all external users and all global users. - `USERS=ALL_EXTERNAL:FILE` 	This usage instructs the utility to migrate all external users and all users specified in `USERSFILE`. |
| Description: | Specifies which users are to be migrated. If multiple values are specified for this parameter, then the utility uses the union of these sets of users. |
| Restrictions: | This parameter is mandatory for Phase One only, and it is ignored in Phase Two. |

### A.6.8 Keyword: USERSLIST

| Attribute | Definition |
| --- | --- |
| Valid Values: | user1:user2:...  Separate user names with a colon (:). |
| Default Setting: | No default setting |
| Syntax Examples: | `USERSLIST=jdoe:tchin:adesai` |
| Description: | Specifies a list of database users for migration. The users in this list are migrated with other users specified with the `USERS` parameter. |
| Restrictions: | This optional parameter is effective only when `LIST` is specified with the `USERS` parameter. |

### A.6.9 Keyword: USERSFILE

| Attribute | Definition |
| --- | --- |
| Valid Values: | File name and path |
| Default Setting: | No default setting |
| Syntax Examples: | `USERSFILE=/home/orahome/userslist/hr_users.txt` |
| Description: | Specifies a file that contains a list of database users (one user listed for each line) for migration. The users in this file are migrated with other users specified with the `USERS` parameter. |
| Restrictions: | This optional parameter is effective only when `FILE` is specified with the `USERS` parameter. |

### A.6.10 Keyword: KREALM

| Attribute | Description |
| --- | --- |
| Valid Values: | kerberos realm |
| Default Setting: | No default setting |
| Syntax Examples: | KREALM=EXAMPLE.COM |
| Description: | Kerberos REALM for external kerberos users, which will usually be the domain name of the database server.If this parameter is not specified, then all external users who are considered for migration are assumed to be non-Kerberos. |
| Restrictions: | - This parameter is valid only for Phase One. |

### A.6.11 Keyword: MAPSCHEMA

| Attribute | Description |
| --- | --- |
| Valid Values: | schema\_type:schema\_name  Schema type can be:  - `PRIVATE` 	Retains users' old local schemas. Schema name is ignored when schema type is `PRIVATE`. No mapping entries are created in the directory. - `SHARED` 	Maps users to a shared schema. Mapping entries are created in the directory. Schema name specifies the shared schema name. During shared schema mapping, whether users' local schemas are dropped from the database is determined by the "Keyword: CASCADE" setting.  (These values are not case-sensitive.) |
| Default Setting: | `PRIVATE` |
| Syntax Examples: | `MAPSCHEMA=SHARED:HR_ALL` |
| Description: | Specifies whether the utility populates the interface table with schema mapping information. |
| Restrictions: | - See the `SHARED` option under Valid Values. - This parameter is valid only for Phase One. |

### A.6.12 Keyword: MAPTYPE

| Attribute | Description |
| --- | --- |
| Valid Values: | mapping\_type:mapping\_level  Mapping type can be:  - `DB` - `DOMAIN`  Mapping level can be:  - `ENTRY` - `SUBTREE`  Separate mapping type from mapping level with a colon (:).  (These values are not case-sensitive.) |
| Default Setting: | `DB:ENTRY` |
| Syntax Examples: | `MAPTYPE=DOMAIN:SUBTREE` |
| Description: | Specifies the type of schema mapping that is to be applied when "Keyword: MAPSCHEMA" is set to `SHARED`. If `DB` is specified as the mapping type, then the utility creates a mapping in the directory for the database. If `DOMAIN` is specified as the mapping type, then the utility creates a mapping in the directory for the domain containing the database. For domain mapping, the utility determines the domain that contains the database by an LDAP search in the relevant Oracle context. |
| Restrictions: | This parameter is effective only when `MAPSCHEMA` is set to `SHARED`. |

See Also:

"About Using the SUBTREE Mapping Level Option" for more information about using this mapping level option

### A.6.13 Keyword: CASCADE

| Attribute | Description |
| --- | --- |
| Valid Values: | - `NO` 	When users are mapped to a shared schema, the utility tries to drop their local schemas from the database. If this parameter is set to NO, then users are migrated only if they do not own objects in their local schema. Users who own objects in their old local schemas do not migrate. An error message is logged in the migration log file for such users. - `YES` 	If this parameter is set to YES, then all users' schema objects are dropped along with their local schemas when they are migrated. Privileges and roles that were previously granted to the users are also revoked.  (These values are not case-sensitive.) |
| Default Setting: | `NO` |
| Syntax Examples: | `CASCADE=YES` |
| Description: | Specifies whether a user's local schema is dropped when the user is mapped to a shared schema |
| Restrictions: | This parameter is effective only when `MAPSCHEMA` is set to `SHARED`. |

### A.6.14 Keyword: CONTEXT

| Attribute | Description |
| --- | --- |
| Valid Values: | Distinguished Name (DN) of the parent for user entries. This is the same as the user search base or user create base in an Oracle Internet Directory identity management realm.  Parent DN can also be specified within double quotation marks (""). |
| Default Setting: | Value set in orclCommonUserCreateBase attribute under cn=Common of Oracle Context  Refer to [Figure 1-3, "Related Entries in a Realm Oracle Context"](concepts.md) for a directory information tree diagram that shows an Oracle Context. |
| Syntax Examples: | `CONTEXT="c=Users, c=us"` |
| Description: | Specifies the DN of the parent entry under which user entries are created in the directory if there is no directory entry that matches the userID for the user |
| Restrictions: | This parameter is valid only for phase one. |

### A.6.15 Keyword: LOGFILE

| Attribute | Description |
| --- | --- |
| Valid Values: | File name and path |
| Default Setting: | $ORACLE\_HOME `/network/log/umu.log` |
| Syntax Examples: | `LOGFILE=home/orahome/network/log/filename.log` |
| Description: | Specifies the log file where details about the migration for each user are written |
| Restrictions: | None |

### A.6.16 Keyword: PARFILE

| Attribute | Description |
| --- | --- |
| Valid Values: | File name and path |
| Default Setting: | No default setting |
| Syntax Examples: | `PARFILE=home/orahome/network/usr/par.txt` |
| Description: | Specifies a text file containing a list of parameters intended for use in a user migration. Each parameter must be listed on a separate line in the file. If a parameter is specified both in the parameter file and on the command line, then the one specified on the command line takes precedence. |
| Restrictions: | None |

## A.7 User Migration Utility Usage Examples

The following sections contain examples of the syntax for some typical uses of this utility.

### A.7.1 Migrating Users While Retaining Their Own Schemas

To migrate users while retaining their old database schemas, set the `MAPSCHEMA` parameter to `PRIVATE`, which is the default setting. For example, to migrate users `scott1`, `scott2`, and all external database users, retaining their old schemas, to the directory at `c=Users, c=us` with the newly generated database and directory passwords, use the syntax shown in Example A-2.

Note:

All external users being migrated are considered non-Kerberos by default. For existing Kerberos users, you can have the utility set their Kerberos principal name attribute in Oracle Internet Directory after migration. To do this, specify the `KREALM` parameter on the command line by using the Kerberos `REALM` value. For example, if the Kerberos `REALM` value is `EXAMPLE.COM`, then you would enter `KREALM=EXAMPLE.COM`. Once you do this, those users with names of the form `user` @ `kerberos_realm` are considered Kerberos users. In Oracle Internet Directory, their Kerberos principal names are set by using their database user names.

See Also: "Keyword: KREALM"

Example A-2 Migrating Users with MAPSCHEMA=PRIVATE (Default)

```
umu PHASE=ONE
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
USERS=ALL_EXTERNAL:LIST
USERSLIST=scott1:scott2
DIRLOCATION=machine2:636
CONTEXT="c=Users,c=us"
ENTADMIN="cn=janeadmin":Easy2rem
```
```
umu PHASE=TWO
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
DIRLOCATION=machine2:636
ENTADMIN="cn=janeadmin":Easy2rem
```

After Phase One is completed successfully, the interface table is populated with the user migration information. Then, the enterprise user administrator can review the table to confirm its contents. Because no value was specified for the `MAPSCHEMA` parameter, the utility runs Phase One using the default value, `PRIVATE`, so all users' old database schemas and objects are retained.

### A.7.2 Migrating Users and Mapping to a Shared Schema

To migrate users and map them to a new shared schema, dropping their old database schemas, set the `MAPSCHEMA` parameter to `SHARED`. The shared schema must already exist, or the enterprise user administrator must create it before running the utility with this parameter setting. In the following example, users `scott1`, `scott2`, and all external database users are migrated to the directory at `c=Users, c=us` with newly generated database and directory passwords, while mapping all migrated users to a new shared schema in the database.

Use the syntax shown in Example A-3 to run the migration process with `MAPSCHEMA` set to `SHARED`.

Example A-3 Migrating Users with MAPSCHEMA=SHARED

```
umu PHASE=ONE
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
USERS=ALL_EXTERNAL:LIST
USERSLIST=scott1:scott2
MAPSCHEMA=SHARED:schema_32
DIRLOCATION=machine2:636
CONTEXT="c=Users, c=us"
ENTADMIN="cn=janeadmin":Easy2rem
```
```
umu PHASE=TWO
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
DIRLOCATION=machine2:636
ENTADMIN="cn=janeadmin":Easy2rem
```

After Phase One is completed successfully, the interface table is populated with the user migration information. Then, the administrator can review the table to confirm its contents. Users `scott1`, `scott2`, and the external users are assigned new randomly generated database and directory passwords. Because no value was specified for the `CASCADE` parameter, the utility runs Phase One using the default value, `NO`, which means that migrating users who own database objects in their old database schemas will fail and their schemas will not be automatically dropped. To determine which users have failed, review the log file that is located at `$ORACLE_HOME/network/log/umu.log` by default.

#### A.7.2.1 Mapping Users to a Shared Schema Using Different CASCADE Options

The `CASCADE` parameter setting determines whether users' old database schemas are automatically dropped when mapping to a shared schema during migration. `CASCADE` can be used only when `MAPSCHEMA` is set to `SHARED`.

##### A.7.2.1.1 Mapping Users to a Shared Schema with CASCADE=NO

By default, the `CASCADE` parameter is set to `NO`. This setting means that when mapping migrating users to a shared schema, users who own database objects in their old schemas are not migrated. For users who do not own database objects, their old database schemas are automatically dropped, and they are mapped to the new shared schema.

See Also:

Example A-3 for a syntax example to map users to a shared schema with `CASCADE` set to `NO`. Note that because `NO` is the default setting for `CASCADE`, this parameter does not have to be specified in the utility command syntax

##### A.7.2.1.2 Mapping Users to a Shared Schema with CASCADE=YES

If it is known that no migrating users own database objects or want to retain the objects that they own in their old database schemas, then setting the `CASCADE` parameter to `YES` automatically drops all users' schemas and schema objects and maps them to the new shared schema. Example A-4 shows the syntax to use when setting `CASCADE` to `YES`. In this example, users `scott1`, `scott2`, and all external database users are migrated to the directory at `c=Users, c=us`, while mapping all migrating users to a new shared schema in the database.

Example A-4 Migrating Users with Shared Schema Mapping and CASCADE=YES

```
umu PHASE=ONE
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
USERS=ALL_EXTERNAL:LIST
USERSLIST=scott1:scott2
MAPSCHEMA=SHARED:schema_32
CASCADE=YES
DIRLOCATION=machine2:636
CONTEXT="c=Users, c=us"
ENTADMIN="cn=janeadmin":Easy2rem
```
```
umu PHASE=TWO
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
DIRLOCATION=machine2:636
ENTADMIN="cn=janeadmin":Easy2rem
```

After Phase One is completed successfully, the interface table is populated with the user migration information. Then, the administrator can review the table to confirm its contents. Because the `CASCADE` parameter is set to YES, all migrated users' old database schemas are automatically dropped, including those who own database objects.

Caution:

If you set the `CASCADE` parameter to `YES`, then Oracle recommends that enterprise user administrators back up the database or take an export dump of the users being migrated before running this utility. Then, if migrated users want their old database objects, then they can retrieve them from the export dump.

#### A.7.2.2 Mapping Users to a Shared Schema Using Different MAPTYPE Options

When `MAPSCHEMA` is set to `SHARED`, the mapping type can be set by specifying a value for the `MAPTYPE` parameter. This parameter takes two values, which are mapping type and mapping level.

Mapping type can be set at `DB`, for database, or `DOMAIN`, for enterprise domain. When mapping type `DB` is specified, the mapping is applied only to the database where the shared schema is stored. When `DOMAIN` is specified as the mapping type, the mapping is applied to the enterprise domain that contains the database where the shared schema is stored and also applies to all databases in that domain.

Mapping level can be set to `ENTRY` or `SUBTREE`. When `ENTRY` is specified, users are mapped to the shared schema using their full distinguished name (DN). This results in one mapping for each user. When `SUBTREE` is specified, groups of users who share part of their DNs are mapped together. This results in one mapping for user groups already grouped under some common root in the directory tree. Example A-5 shows the syntax to use when using the `MAPTYPE` parameter. In this example, users `scott1`, `scott2`, and all external database users are migrated to the directory at `c=Users, c=us`, while mapping all migrated users to a new shared schema in the database. In this example, the mapping will apply to the enterprise domain that contains the database, and the mapping will be performed at the entry level, resulting in a mapping for each user.

Example A-5 Migrating Users with Shared Schema Mapping Using the MAPTYPE Parameter

```
umu PHASE=ONE
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
USERS=ALL_EXTERNAL:LIST
USERSLIST=scott1:scott2
MAPSCHEMA=SHARED:schema_32
MAPTYPE=DOMAIN:ENTRY
DIRLOCATION=machine2:636
CONTEXT="c=Users, c=us"
ENTADMIN="cn=janeadmin":welcome
```
```
umu PHASE=TWO
```
```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
DIRLOCATION=machine2:636
ENTADMIN="cn=janeadmin":welcome
```

##### A.7.2.2.1 About Using the SUBTREE Mapping Level Option

If a user (`scott`, for example) who is being migrated will have future user entries in a subtree under it, then it makes sense to create a subtree level mapping from this user entry (`cn=scott`) to a schema. However, the database does not interpret the user to be in the subtree so the mapping does not apply to `scott` himself. For example, if you are migrating the user `scott` with the DN `cn=scott,o=acme`, and you choose `SUBTREE` as the mapping level when you run the utility, then a new mapping is created from `cn=scott,o=acme` to the shared schema, but the user `scott` is not mapped to that schema. Only new users who are created under the `scott` directory entry are mapped to the shared schema. Consequently, the `SUBTREE` mapping level should only be specified when user directory entries are placed under other user directory entries, which would be an unusual directory configuration.

If you want an arbitrary subtree user to be mapped to a single shared schema with only one mapping entry, then you must use Oracle Enterprise Manager to create that mapping.

See Also:

["Creating User-Schema Mappings for an Enterprise Domain"](adminste.md) for information about using Oracle Enterprise Manager

### A.7.3 Migrating Users Using the PARFILE, USERSFILE, and LOGFILE Parameters

It is possible to enter user information and User Migration Utility parameters into a text file and pass the information and parameters to the utility using the `PARFILE` and `USERSFILE` parameters. The `LOGFILE` parameter sets the directory path for the log file where details about the migration for each user are written.

The `PARFILE` parameter tells the utility where a text file is located that contains the parameters for a bulk user migration. The `USERSFILE` parameter works like the `PARFILE` parameter, except that it contains database users instead of parameters. The parameters and users lists contain one parameter or user for each line. The `LOGFILE` parameter tells the utility where to write the system events that occur during a user migration, such as errors. Use the `USERSFILE` parameter during Phase One of the migration process. The `PARFILE` and `LOGFILE` parameters can be used in both phases.

Example A-6 shows the syntax for a typical parameter text file to migrate users `scott1`, `scott2`, and all external database users, while retaining their old schemas, to the directory at `c=Users, c=us`. In this example, a log of migration events is written to the file `errorfile1` in the directory where the utility is run. If another location is desired, then include the path with the file name.

Example A-6 Parameter Text File (par.txt) to Use with the PARFILE Parameter

```
DBLOCATION=machine1:1521:ora_sid
DBADMIN=system:manager
USERS=ALL_EXTERNAL:LIST:FILE
USERSLIST=scott1:scott2
USERSFILE=usrs.txt
DIRLOCATION=machine2:636
CONTEXT="c=Users, c=us"
ENTADMIN="cn=janeadmin":Easy2rem
LOGFILE=errorfile1
```

Example A-7 shows the syntax for a typical users list text file.

Example A-7 Users List Text File (usrs.txt) to Use with the USERSFILE Parameter

```
user1
user2
user3
```

To run Phase One of the migration process with these parameters and users list text files, use the syntax shown in Example A-8.

Example A-8 Migrating Users Using the PARFILE, USERSFILE, and LOGFILE Parameters

```
umu PHASE=ONE
```
```
DBADMIN=system:manager
PARFILE=par.txt
LOGFILE=errorfile2
```

Note:

Although the `LOGFILE` parameter is specified twice, once in the parameter text file as `errorfile1` (shown in Example A-6) and once on the command line as `errorfile2` (shown in Example A-8), command-line parameters take precedence over those specified inside the parameter file. Consequently, in Example A-8, the log file will be written to `errorfile2` because that value is specified on the command line.

## A.8 Troubleshooting Using the User Migration Utility

Migration failures are reported to the enterprise user administrator with error messages and log messages. The following sections describe common error and log messages and what administrators can do to resolve them.

See Also:

"Summary of User Migration Utility Error and Log Messages" for an alphabetical listing of error and log messages and links to where they are described in this section

### A.8.1 Common User Migration Utility Error Messages

When the utility encounters any error while running, it displays an error message and stops running. The following sections describe these messages and explain how to resolve the errors:

- Resolving Error Messages Displayed for Both Phases
- Resolving Error Messages Displayed for Phase One

#### A.8.1.1 Resolving Error Messages Displayed for Both Phases

The following error messages may be displayed while the utility is running either Phase One or Phase Two of the migration:

- Attribute value missing:: orclCommonNicknameAttribute
- Database connection failure
- Database error: < database\_error\_message >
- Database not in any domain:: DB-NAME = < database\_name >
- Database not registered with the directory:: DB-NAME = < dbName >
- Directory connection failure
- Directory error:: < directory\_error\_message >
- Multiple entries found:: uniqueMember = < database\_DN >

Attribute value missing:: orclCommonNicknameAttribute

Cause: The nickname attribute is not set in the directory in the root identity management realm.

Action: Use Oracle Internet Directory Self-Service Console to set the nickname attribute for the identity management realm.

Database connection failure

Cause: The utility was unable to connect to the database.

Action: Perform these steps:
1. Check the database status to determine whether it is configured for encryption and integrity.
2. Check the privileges and credentials of the enterprise user administrator who is running the utility.

Database error: < database\_error\_message >

Cause: The utility encountered a database error.

See Also:

[Oracle Database Error Messages](https://docs.oracle.com/cd/E11882_01/server.112/e17766/toc.htm) for information about resolving database error messages

Database not in any domain:: DB-NAME = < database\_name >

Cause: The database is not a member of any enterprise domain.

Action: Use Oracle Enterprise Manager to add the database to an enterprise domain in the directory.

Database not registered with the directory:: DB-NAME = < dbName >

Cause: There is no entry for the database in the Oracle Context that the ldap.ora file points to.

Action: Use Database Configuration Assistant to register the database in the directory.

Directory connection failure

Cause: The utility was unable to connect to the directory.

Action: Perform these steps:
1. Check the directory server status to determine whether the directory server port is configured for SSL with no authentication.
2. Check the privileges and credentials of the enterprise user administrator who is running the utility.

Directory error:: < directory\_error\_message >

Cause: The utility encountered a directory error.

See Also:

[Oracle Internet Directory Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIDAG) information about resolving error messages for Oracle Internet Directory

Multiple entries found:: uniqueMember = < database\_DN >

Cause: The database belongs to more than one enterprise domain in the directory.

Action: Use Oracle Enterprise Manager to ensure that the database belongs to only one enterprise domain.

#### A.8.1.2 Resolving Error Messages Displayed for Phase One

While the utility is running Phase One of the migration, syntax or other types of errors may occur. The following error messages may be displayed while the utility is running Phase One of the migration:

- Argument missing or duplicated:: < parameter >
- Database object missing:: SHARED-SCHEMA = <shared\_schema\_name >
- Error reading file:: < file\_name >:: < io\_error\_message >
- Error reading file:: PARFILE = < file\_name >:: < io\_error\_message>
- Getting local host name failed
- Interface table creation in SYS schema not allowed
- Invalid argument or value:: < argument >
- Invalid arguments for the phase
- [Invalid value:: < user > \[ USERSFILE \]](#i635980)
- [Invalid value:: < user > \[ USERSFILE \] { = = DBADMIN }](#i635984)
- [Invalid value:: < user > \[ USERSLIST \]](#i635988)
- [Invalid value:: < user > \[ USERSLIST \] { = = DBADMIN }](#i635992)
- Logging failure:: < io\_error\_message >
- No entry found:: CONTEXT = < context >

Argument missing or duplicated:: < parameter >

Cause: Syntax error. A parameter is missing or has been entered multiple times.

Action: Check the usage syntax.

Database object missing:: SHARED-SCHEMA = <shared\_schema\_name >

Cause: The shared schema is not present in the database.

Action: Create the shared schema.

Error reading file:: < file\_name >:: < io\_error\_message >

Cause: Syntax error. The utility cannot read the file that contains the users list that is specified in the USERSFILE parameter.

Action: Perform these steps:
1. Check to ensure that the file exists.
2. Check to ensure that the file has the correct permissions so the utility can read it.

Error reading file:: PARFILE = < file\_name >:: < io\_error\_message>

Cause: Syntax error. The utility cannot read the file that contains the list of parameters that is specified in the PARFILE parameter.

Action: Perform these steps:
1. Check to ensure that the file exists.
2. Check to ensure that the file has the correct permissions so the utility can read it.

Getting local host name failed

Cause: Syntax error. The utility is unable to read the local host name for the database location or the directory location.

Action: Explicitly enter the host name information with the `DBLOCATION` and `DIRLOCATION` parameters.

See Also:

- "Keyword: DBLOCATION"
- "Keyword: DIRLOCATION"

for information about how to use these parameters

Interface table creation in SYS schema not allowed

Cause: The interface table cannot be created in the `SYS` schema.

Action: Specify another user in the `DBADMIN` parameter.

See Also:

"Keyword: DBADMIN" for information about setting the `DBADMIN` parameter

Invalid argument or value:: < argument >

Cause: Syntax error. The argument name or value has been entered incorrectly.

Action: Check the usage syntax.

See Also:

- "User Migration Utility Command-Line Syntax"
- "Accessing Help for the User Migration Utility"
- "User Migration Utility Parameters"

for information about using the command-line syntax for this utility

Invalid arguments for the phase

Cause: Syntax error. This occurs when you have used a command-line argument that is only intended for Phase One, but you are running Phase Two.

Action: Check the usage syntax.

Invalid value:: < user > \[ USERSFILE \]

Cause: Syntax error. The user that is specified in this error message is invalid because he is not a user in the database that is specified in the `DBLOCATION` parameter.

Action: Remove the invalid user from the file that is specified with the `USERSFILE` parameter.

Invalid value:: < user > \[ USERSFILE \] { = = DBADMIN }

Cause: Syntax error. The file that is specified in the `USERSFILE` parameter contains the user who is running the migration utility.

Action: Remove that user from the file.

Invalid value:: < user > \[ USERSLIST \]

Cause: Syntax error. The user that is specified in this error message is invalid because they are not a user in the database that is specified in the `DBLOCATION` parameter.

Action: Remove the invalid user from the `USERSLIST` parameter.

Invalid value:: < user > \[ USERSLIST \] { = = DBADMIN }

Cause: Syntax error. The `USERSLIST` parameter contains the user who is running the migration utility.

Action: Remove that user from the `USERSLIST` parameter.

Logging failure:: < io\_error\_message >

Cause: Syntax error. The utility cannot find the log file or it cannot open the file to write to it.

Action: Perform these steps:
1. Check to ensure that the log file exists.
2. Check to ensure that the log file has the correct permissions so the utility can write information to it.

No entry found:: CONTEXT = < context >

Cause: The `CONTEXT` entry is not present in the directory.

Action: Perform one of the following steps:
- Use the directory management tool or the LDAP command-line utility to create an entry in the directory for the context value.
- Specify another valid context value.

#### A.8.1.3 Resolving Error Messages Displayed for Phase Two

Most of the error messages that you encounter while running this utility occur in Phase One. After Phase One has completed successfully, and while Phase Two is running, the following error may occur:

Database object missing:: TABLE = ORCL\_GLOBAL\_USR\_MIGRATION\_DATA

Cause: The utility cannot find the interface table.

Action: Perform one of the following steps:
- Run Phase One of the utility to create the interface table.
- Check to ensure that the user who is specified in the `DBADMIN` parameter is the same user who was specified for that parameter for Phase One.

### A.8.2 Common User Migration Utility Log Messages

Typically, log messages are written to the log file for each user who is migrated, whether the user was migrated successfully or not. The following sections describe these messages and explain how to resolve the errors:

#### A.8.2.1 Common Log Messages for Phase One

While the utility is running Phase One of the migration, messages that indicate that a user's information has not been successfully populated in the interface table may be written to the log file. After the utility completes Phase One, review the log file to check for the following messages:

- Multiple entries found:: < nickname\_attribute > = < username >
- No entry found:: < nickname\_attribute > = < username >:: Entry found: DN = < dn >

Multiple entries found:: < nickname\_attribute > = < username >

Cause: The nickname attribute matches multiple users or the user matches with multiple nickname attributes.

Action: Resolve the multiple matches and run the utility again for the users whose log file entry displayed this message.

No entry found:: < nickname\_attribute > = < username >:: Entry found: DN = < dn >

Cause: No entry was found for the nickname matching, but an entry already exists for the DN in the directory.

Action: Specify a different DN for the user.

#### A.8.2.2 Common Log Messages for Phase Two

While the utility is running Phase Two of the migration, messages that indicate that a user has not successfully migrated may be written to the log file. After the utility completes Phase Two, review the log file to check for the following messages:

- Attribute exists:: orclPassword
- Attribute value missing:: orclPassword
- Database object missing:: SHARED-SCHEMA = < shared\_schema >
- Entry found:: DN = < user\_DN >
- Invalid value:: <interface\_table\_column\_name> = < interface\_table\_column\_value >
- No entry found:: DN = < user\_DN >

Attribute exists:: orclPassword

This message typically occurs with the message `Invalid value::<column_name>=<column_value>`.

Cause: The entry already contains a value for the `orclPassword` attribute.

Action: Check the `DBPASSWORD_EXIST_FLAG` column in the interface table for a `T/F` value that correctly reflects whether a database password exists for this user.

Attribute value missing:: orclPassword

This message typically occurs with the message `Invalid value::<column_name>=<column_value>`.

Cause: The `orclPassword` attribute of this user's entry has a null value.

Action: Check the `DBPASSWORD_EXIST_FLAG` column in the interface table for a `T/F` value that correctly reflects whether a database password exists for this user.

Database object missing:: SHARED-SCHEMA = < shared\_schema >

Cause: The shared schema that was specified for this user does not exist in the database.

Action: Perform one of the following steps:
- Check to ensure that the correct shared schema was specified for this user. If the shared schema name was incorrectly specified, then edit the `SHARED_SCHEMA` column of the interface table and run Phase Two of the utility for this user again.
- Create the shared schema in the database and run Phase Two of the utility for this user again.

Entry found:: DN = < user\_DN >

This message typically occurs with the message `Invalid value::<column_name>=<column_value>`.

Cause: An entry already exists for the specified user DN.

Action: Check the `USERDN_EXIST_FLAG` column in the interface table for a `T/F` value that correctly reflects whether a user entry already exists in the directory for this DN.

Invalid value:: <interface\_table\_column\_name> = < interface\_table\_column\_value >

Cause: The value in the interface table column for this user is invalid. Typically, this message is accompanied by additional log messages for this user.

Action: Check to ensure that the correct value has been entered for this user.

No entry found:: DN = < user\_DN >

This message typically occurs with the message `Invalid value::<column_name>=<column_value>`.

Cause: The entry for the DN is missing in the directory.

Action: Check the `USERDN_EXIST_FLAG` column in the interface table for a `T/F` value that correctly reflects whether a user entry already exists in the directory for this DN.

### A.8.3 Summary of User Migration Utility Error and Log Messages

Table A-4 and Table A-5 list all of the error and log messages in alphabetical order and provides links to the section in this chapter that describes the message and how to resolve it.

Table A-4 Alphabetical Listing of User Migration Utility Error Messages

| User Migration Utility Error Message | Phase |
| --- | --- |
| Argument missing or duplicated:: < parameter > | 1 |
| Attribute value missing:: orclCommonNicknameAttribute | Both |
| Database connection failure | Both |
| Database error: < database\_error\_message > | Both |
| Database not in any domain:: DB-NAME = < database\_name > | Both |
| Database not registered with the directory:: DB-NAME = < dbName > | Both |
| Database object missing:: SHARED-SCHEMA = <shared\_schema\_name > | 1 |
| Database object missing:: TABLE = ORCL\_GLOBAL\_USR\_MIGRATION\_DATA | 2 |
| Directory connection failure | Both |
| Directory error:: < directory\_error\_message > | Both |
| Error reading file:: < file\_name >:: < io\_error\_message > | 1 |
| Error reading file:: PARFILE = < file\_name >:: < io\_error\_message> | 1 |
| Getting local host name failed | 1 |
| Interface table creation in SYS schema not allowed | 1 |
| Invalid argument or value:: < argument > | 1 |
| Invalid arguments for the phase | 1 |
| [Invalid value:: < user > \[ USERSFILE \]](#i635980) | 1 |
| [Invalid value:: < user > \[ USERSFILE \] { = = DBADMIN }](#i635984) | 1 |
| [Invalid value:: < user > \[ USERSLIST \]](#i635988) | 1 |
| [Invalid value:: < user > \[ USERSLIST \] { = = DBADMIN }](#i635992) | 1 |
| Logging failure:: < io\_error\_message > | 1 |
| Multiple entries found:: uniqueMember = < database\_DN > | Both |
| No entry found:: CONTEXT = < context > | 1 |

Table A-5 Alphabetical Listing of User Migration Utility Log Messages

| User Migration Utility Log Message | Phase |
| --- | --- |
| Attribute exists:: orclPassword | 2 |
| Attribute value missing:: orclPassword | 2 |
| Database object missing:: SHARED-SCHEMA = < shared\_schema > | 2 |
| Entry found:: DN = < user\_DN > | 2 |
| Invalid value:: <interface\_table\_column\_name> = < interface\_table\_column\_value > | 2 |
| Multiple entries found:: < nickname\_attribute > = < username > | 1 |
| No entry found:: DN = < user\_DN > | 2 |
| No entry found:: < nickname\_attribute > = < username >:: Entry found: DN = < dn > | 1 |