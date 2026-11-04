---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: E96136-19
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/managing-security-for-a-multitenant-environment.html
tags:
  - oracle
  - 19c
  - multitenant-administrators-guide
---

## 18 Managing Security for a Multitenant Environment

You can manage common and local users and roles for a multitenant environment by using SQL\*Plus and Oracle Enterprise Manager.

- Managing Commonly and Locally Granted Privileges  
	In a multitenant environment, privileges can be granted commonly for an entire CDB or application container, or granted locally to a specific PDB.
- Managing Common Roles and Local Roles  
	A common role is a role that is created in the root; a local role is created in a PDB.
- Restricting Operations on PDBs Using PDB Lockdown Profiles  
	You can use PDB lockdown profiles in a multitenant environment to restrict sets of user operations in pluggable databases (PDBs).
- Configuring Operating System Users for a PDB  
	The `DBMS_CREDENTIAL.CREATE_CREDENTIAL` procedure configures user accounts to be operating system users for a pluggable database (PDB).
- Using Application Contexts in a Multitenant Environment  
	An application context stores user identification that can enable or prevent a user from accessing data in the database.
- Using Oracle Virtual Private Database in a Multitenant Environment  
	Oracle Virtual Private Database (VPD) enables you to filter users who access data.
- Using Transport Layer Security in a Multitenant Environment  
	Transport Layer Security (TLS) can be used in a multitenant environment for application containers.
- Oracle Data Redaction in a Multitenant Environment  
	In a multitenant environment, Oracle Data Redaction policies apply only to the objects within the current pluggable database (PDB).
- Overview of Auditing in a Multitenant Environment  
	Auditing is the monitoring and recording of configured database actions, from both database users and nondatabase users. Nondatabase users are application users who are recognized in the database using the `CLIENT_IDENTIFIER` attribute.

**Parent topic:** [Administering a Multitenant Environment](managing-a-multitenant-environment.md)

### Managing Commonly and Locally Granted Privileges

In a multitenant environment, privileges can be granted commonly for an entire CDB or application container, or granted locally to a specific PDB.

- How the Oracle Multitenant Option Affects Privileges  
	In a multitenant environment, all users, including common users, can exercise their privileges only within the current container.
- About Commonly and Locally Granted Privileges  
	In a multitenant environment, both common users and local users can grant privileges to one another.
- How Commonly Granted System Privileges Work  
	Users can exercise system privileges only within the PDB in which they were granted.
- How Commonly Granted Object Privileges Work  
	Object privileges on common objects applies to the object as well as all associated links on this common object.
- Granting or Revoking Privileges to Access a PDB  
	You can grant and revoke privileges for PDB access in a multitenant environment.
- Example: Granting a Privilege in a Multitenant Environment  
	You can use the GRANT statement to grant privileges in a multitenant environment.
- Enabling Common Users to View CONTAINER\_DATA Object Information  
	Common users can view information about `CONTAINER_DATA` objects in the root or for data in specific PDBs.

**Parent topic:** Managing Security for a Multitenant Environment

#### How the Oracle Multitenant Option Affects Privileges

In a multitenant environment, all users, including common users, can exercise their privileges only within the current container.

However, a user connected to the root can perform certain operations that affect other pluggable databases (PDBs). These operations include `ALTER PLUGGABLE DATABASE`, `CREATE USER`, `CREATE ROLE`, and `ALTER USER`. The common user must possess the commonly granted privileges that enable these operations. A common user connected to the root can see metadata pertaining to PDBs by way of the container data objects (for example, multitenant container database (CDB) views and `V$` views) in the root, provided that the common user has been granted privileges required to access these views and his `CONTAINER_DATA` attribute has been set to allow seeing data about various PDBs. The common user cannot query tables or views in a PDB.

Common users cannot exercise their privileges across other PDBs. They must first switch to the PDB that they want, and then exercise their privileges from there. To switch to a different container, the common user must have the `SET CONTAINER` privilege. The `SET CONTAINER` privilege must be granted either commonly or in the container to which the user is attempting to switch. Alternatively, the common user can start a new database session whose initial current container is the container this user wants, relying on the `CREATE SESSION` privilege in that PDB.

Be aware that commonly granted privileges may interfere with the security configured for individual PDBs. For example, suppose an application PDB database administrator wants to prevent any user in the PDB from modifying a particular application common object. A privilege (such as `UPDATE`) granted commonly to `PUBLIC` or to a common user or common role on the object would circumvent the PDB database administrator’s intent.

#### About Commonly and Locally Granted Privileges

In a multitenant environment, both common users and local users can grant privileges to one another.

Privileges by themselves are neither common nor local. How the privileges are applied depends on whether the privilege is granted commonly or granted locally.

For commonly granted privileges:

- A privilege that is granted commonly can be used in every existing and future container.
- Only common users can grant privileges commonly, and only if the grantee is common.
- A common user can grant privileges to another common user or to a common role.
- The grantor must be connected to the root and must specify `CONTAINER=ALL` in the `GRANT` statement.
- Both system and object privileges can be commonly granted. (Object privileges become actual only with regard to the specified object.)
- When a common user connects to or switches to a given container, this user's ability to perform various activities (such as creating a table) is controlled by privileges granted commonly as well as privileges granted locally in the given container.
- Do not grant privileges to `PUBLIC` commonly.

For locally granted privileges:

- A privilege granted locally can be used only in the container in which it was granted. When the privilege is granted in the root, it applies only to the root.
- Both common users and local users can grant privileges locally.
- A common user and a local user can grant privileges to other common or local roles.
- The grantor must be connected to the container and must specify `CONTAINER=CURRENT` in the `GRANT` statement.
- Any user can grant a privilege locally to any other user or role (both common and local) or to the `PUBLIC` role.

#### How Commonly Granted System Privileges Work

Users can exercise system privileges only within the PDB in which they were granted.

For example, if a system privilege is locally granted to a common user `A` in a PDB `B`, user `A` can exercise that privilege only while connected to PDB `B`.

System privileges can apply in the root and in all existing and future PDBs if the following requirements are met:

- The system privilege grantor is a common user and the grantee is a common user, a common role, or the `PUBLIC` role. Do not commonly grant system privileges to the `PUBLIC` role, because this in effect makes the system privilege available to all users.
- The system privilege grantor possesses the `ADMIN OPTION` for the commonly granted privilege
- The `GRANT` statement must contain the `CONTAINER=ALL` clause.

The following example shows how to commonly grant a privilege to the common user `c##hr_admin`.

```
CONNECT SYSTEM 
Enter password: password
Connected.

GRANT CREATE ANY TABLE TO c##hr_admin CONTAINER=ALL;
```

#### How Commonly Granted Object Privileges Work

Object privileges on common objects applies to the object as well as all associated links on this common object.

These links include all metadata links, data links (previously called object links), or extended data links that are associated with it in the root and in all PDBs belonging to the container (including future PDBs) if certain requirements are met.

These requirements are as follows:

- The object privilege grantor is a common user and the grantee is a common user, a common role, or the `PUBLIC` role.
- The object privilege grantor possesses the commonly granted `GRANT OPTION` for the privilege
- The `GRANT` statement contains the `CONTAINER=ALL` clause.

The following example shows how to grant an object privilege to the common user `c##hr_admin` so that he can select from the `DBA_PDBS` view in the CDB root or in any of the associated PDBs that he can access.

```
CONNECT SYSTEM
Enter password: password
Connected.

GRANT SELECT ON DBA_OBJECTS TO c##hr_admin 
CONTAINER=ALL;
```

**Parent topic:** Managing Commonly and Locally Granted Privileges

#### Granting or Revoking Privileges to Access a PDB

You can grant and revoke privileges for PDB access in a multitenant environment.

To grant a privilege in a multitenant environment:

- Include the `CONTAINER` clause in the `GRANT` or `REVOKE` statement.

Setting `CONTAINER` to `ALL` applies the privilege to all existing and future containers; setting it to `CURRENT` applies the privilege to the local container only. Omitting the `CONTAINER` clause applies the privilege to the local container. If you issue the `GRANT` statement from the root and omit the `CONTAINER` clause, then the privilege is applied locally.

#### Example: Granting a Privilege in a Multitenant Environment

You can use the GRANT statement to grant privileges in a multitenant environment.

Example 18-1 shows how to commonly grant the `CREATE TABLE` privilege to common user `c##hr_admin` so that this user can use this privilege in all existing and future containers.

Example 18-1 Granting a Privilege in a Multitenant Environment

```
CONNECT SYSTEM
Enter password: password
Connected.

GRANT CREATE TABLE TO c##hr_admin CONTAINER=ALL;
```

**Parent topic:** Managing Commonly and Locally Granted Privileges

#### Enabling Common Users to View CONTAINER\_DATA Object Information

Common users can view information about `CONTAINER_DATA` objects in the root or for data in specific PDBs.

- Viewing Data About the Root, CDB, and PDBs While Connected to the Root  
	You can restrict view information for the `X$` table and the `V$`, `GV$` and `CDB_*` views when common users perform queries.
- Enabling Common Users to Query Data in Specific PDBs  
	You can enable common users to access data pertaining to specific PDBs by adjusting the users’ `CONTAINER_DATA` attribute.

**Parent topic:** Managing Commonly and Locally Granted Privileges

##### Viewing Data About the Root, CDB, and PDBs While Connected to the Root

You can restrict view information for the `X$` table and the `V$`, `GV$` and `CDB_*` views when common users perform queries.

The `X$` table and these views contain information about the application root and its associated application PDBs or, if you are connected to the CDB root, the entire CDB.

Restricting this information is useful when you do not want to expose sensitive information about other PDBs. To enable this functionality, Oracle Database provides these tables and views as container data objects. You can find if a specific table or view is a container data object by querying the `TABLE_NAME`, `VIEW_NAME`, and `CONTAINER_DATA` columns of the `USER_` | `DBA_` | `ALL_VIEWS` | `TABLES` dictionary views.

To find information about the default (user-level) and object-specific `CONTAINER_DATA` attributes:

1. In SQL\*Plus or SQL Developer, log in to the root.
2. Query the `CDB_CONTAINER_DATA` data dictionary view.
	For example:
	```
	COLUMN USERNAME FORMAT A13
	COLUMN DEFAULT_ATTR FORMAT A7
	COLUMN OWNER FORMAT A11
	COLUMN OBJECT_NAME FORMAT A11
	COLUMN ALL_CONTAINERS FORMAT A3
	COLUMN CONTAINER_NAME FORMAT A10
	COLUMN CON_ID FORMAT A6
	SELECT USERNAME, DEFAULT_ATTR, OWNER, OBJECT_NAME, 
	       ALL_CONTAINERS, CONTAINER_NAME, CON_ID 
	FROM   CDB_CONTAINER_DATA 
	ORDER BY OBJECT_NAME;
	USERNAME    DEFAULT OWNER OBJECT_NAME ALL CONTAINERS CON_ID
	----------- ------- ----- ----------- --- ---------- ------
	C##HR_ADMIN N       SYS   V$SESSION   N   CDB$ROOT        1
	C##HR_ADMIN N       SYS   V$SESSION   N   SALESPDB        1
	C##HR_ADMIN Y                         N   HRPDB           1
	C##HR_ADMIN Y                         N   CDB$ROOT        1
	DBSNMP      Y                         Y                   1
	SYSTEM      Y                         Y                   1
	```

##### Enabling Common Users to Query Data in Specific PDBs

You can enable common users to access data pertaining to specific PDBs by adjusting the users’ `CONTAINER_DATA` attribute.

To enable common users to access data about specific PDBs:

- Issue the `ALTER USER` statement in the root.

Example 18-2 Setting the CONTAINER\_DATA Attribute

This example shows how to issue the `ALTER USER` statement to enable the common user `c##hr_admin` to view information pertaining to the `CDB$ROOT`, `SALES_PDB`, and `HRPDB` containers in the `V$SESSION` view (assuming this user can query that view).

```
CONNECT SYSTEM
Enter password: password
Connected.

ALTER USER c##hr_admin
SET CONTAINER_DATA = (CDB$ROOT, SALESPDB, HRPDB) 
FOR V$SESSION CONTAINER=CURRENT;
```

In this specification:

- `SET CONTAINER_DATA` lists containers, data pertaining to which can be accessed by the user.
- `FOR V$SESSION ` specifies the `CONTAINER_DATA` dynamic view, which common user `c##hr_admin` will query.
- `CONTAINER = CURRENT` must be specified because when you are connected to the root, `CONTAINER=ALL` is the default for the `ALTER USER` statement, but modification of the `CONTAINER_DATA` attribute must be restricted to the root.

If you want to enable user `c##hr_admin` to view information that pertains to the `CDB$ROOT`, `SALES_PDB`, `HRPDB` containers in all `CONTAINER_DATA` objects that this user can access, then omit `FOR V$SESSION`. For example:

```
ALTER USER c##hr_admin
SET CONTAINER_DATA = (CDB$ROOT, SALESPDB, HRPDB) 
CONTAINER=CURRENT;
```

### Managing Common Roles and Local Roles

A common role is a role that is created in the root; a local role is created in a PDB.

- About Common Roles and Local Roles  
	In a multitenant environment, database roles can be specific to a PDB or used throughout the entire system container or application container.
- How Common Roles Work  
	Common roles are visible in the root and in every PDB of a container within which they are defined in a multitenant environment.
- How the PUBLIC Role Works in a Multitenant Environment  
	All privileges that Oracle grants to the `PUBLIC` role are granted locally.
- Privileges Required to Create, Modify, or Drop a Common Role  
	Only common users who have the commonly granted `CREATE ROLE`, `ALTER ROLE`, and `DROP ROLE` privileges can create, alter, or drop common roles.
- Rules for Creating Common Roles  
	When you create a common role, you must follow special rules.
- Creating a Common Role  
	You can use the `CREATE ROLE` statement to create a common role.
- Rules for Creating Local Roles  
	To create a local role, you must follow special rules.
- Creating a Local Role  
	You can use the `CREATE ROLE` statement to create a role.
- Role Grants and Revokes for Common Users and Local Users  
	Role grants and revokes apply only to the scope of access of the common user or the local user.

**Parent topic:** Managing Security for a Multitenant Environment

#### About Common Roles and Local Roles

In a multitenant environment, database roles can be specific to a PDB or used throughout the entire system container or application container.

A common role is a role whose identity and (optional) password are created in the root of a container and will be known in the root and in all existing and future PDBs belonging to that container.

A local role exists in only one PDB and can only be used within this PDB. It does not have any commonly granted privileges.

Note the following:

- Common users can both create and grant common roles to other common and local users.
- You can grant a role (local or common) to a local user or role only locally.
- If you grant a common role locally, then the privileges of that common role apply only in the container where the role is granted.
- Local users cannot create common roles, but they can grant them to common and other local users.
- The `CONTAINER = ALL` clause is the default when you create a common role in the CDB root or an application root.

#### How Common Roles Work

Common roles are visible in the root and in every PDB of a container within which they are defined in a multitenant environment.

A privilege can be granted commonly to a common role if:

- The grantor is a common user.
- The grantor possesses the commonly granted `ADMIN OPTION` for the privilege that is being granted.
- The `GRANT` statement contains the `CONTAINER=ALL` clause.

If the common role contains locally granted privileges, then these privileges apply only within the PDB in which they were granted to the common role. A local role cannot be granted commonly.

For example, suppose the CDB common user `c##hr_mgr` has been commonly granted the `DBA` role. This means that user `c##hr_mgr` can use the privileges associated with the `DBA` role in the root and in every PDB in the multitenant environment. However, if the CDB common user `c##hr_mgr` has only been locally granted the `DBA` role for the `hr_pdb` PDB, then this user can only use the `DBA` role's privileges in the `hr_pdb` PDB.

**Parent topic:** Managing Common Roles and Local Roles

#### How the PUBLIC Role Works in a Multitenant Environment

All privileges that Oracle grants to the `PUBLIC` role are granted locally.

This feature enables you to revoke privileges or roles that have been granted to the `PUBLIC` role individually in each PDB as needed. If you must grant any privileges to the `PUBLIC` role, then grant them locally. Never grant privileges to `PUBLIC` commonly.

#### Privileges Required to Create, Modify, or Drop a Common Role

Only common users who have the commonly granted `CREATE ROLE`, `ALTER ROLE`, and `DROP ROLE` privileges can create, alter, or drop common roles.

Common users can also create local roles, but these roles are available only in the PDB in which they were created.

**Parent topic:** Managing Common Roles and Local Roles

#### Rules for Creating Common Roles

When you create a common role, you must follow special rules.

The rules are as follows:

- Ensure that you are in the correct root. For the creation of common roles, you must be in the correct root, either the CDB root or the application root. You cannot create common roles from a PDB. To check if you are in the correct root, run one of the following:
	- To confirm that you are in the CDB root, you can issue the `show_con_name` command. The output should be `CDB$ROOT`.
		- To confirm that you are in an application root, verify that the following query returns `YES`:
		```
		SELECT APPLICATION_ROOT FROM V$PDBS WHERE CON_ID=SYS_CONTEXT('USERENV', 'CON_ID');
		```
		- Ensure that the name that you give the common role starts with the value of the COMMON\_USER\_PREFIX parameter (which defaults to C##). Note that this requirement does not apply to the names of existing Oracle-supplied roles, such as `DBA` or `RESOURCE`.
- Optionally, set the CONTAINER clause to ALL. As long as you are in the root, if you omit the `CONTAINER = ALL` clause, then by default the role is created as a common role for the CDB root or the application root.

**Parent topic:** Managing Common Roles and Local Roles

#### Creating a Common Role

You can use the `CREATE ROLE` statement to create a common role.

1. Connect to the root of the CDB or the application container in which you want to create the common role.
	For example:
	```
	CONNECT SYSTEM
	Enter password: password
	Connected.
	```
2. Run the `CREATE ROLE` statement with the `CONTAINER` clause set to `ALL`.
	For example:
	```
	CREATE ROLE c##sec_admin IDENTIFIED BY password CONTAINER=ALL;
	```

#### Rules for Creating Local Roles

To create a local role, you must follow special rules.

These rules are as follows:

- You must be connected to the PDB in which you want to create the role, and have the `CREATE ROLE` privilege.
- The name that you give the local role must not start with the value of the `COMMON_USER_PREFIX` parameter (which defaults to `C##`).
- You can include `CONTAINER=CURRENT` in the `CREATE ROLE` statement to specify the role as a local role. If you are connected to a PDB and omit this clause, then the `CONTAINER=CURRENT` clause is implied.
- You cannot have common roles and local roles with the same name. However, you can use the same name for local roles in different PDBs. To find the names of existing roles, query the `CDB_ROLES` and `DBA_ROLES` data dictionary views.

**Parent topic:** Managing Common Roles and Local Roles

#### Creating a Local Role

You can use the `CREATE ROLE` statement to create a role.

1. Connect to the PDB in which you want to create the local role.
	For example:
	```
	CONNECT SYSTEM@hrpdb
	Enter password: password
	Connected.
	```
2. Run the `CREATE ROLE` statement with the `CONTAINER` clause set to `CURRENT`.
	For example:
	```
	CREATE ROLE sec_admin CONTAINER=CURRENT;
	```

#### Role Grants and Revokes for Common Users and Local Users

Role grants and revokes apply only to the scope of access of the common user or the local user.

Common users can grant and revoke common roles to and from other common users. A local user can grant a common role to any user in a PDB, including common users, but this grant applies only within the PDB.

The following example shows how to grant the common user `c##sec_admin` the `AUDIT_ADMIN` common role for use in all containers.

```
CONNECT SYSTEM
Enter password: password
Connected.

GRANT AUDIT_ADMIN TO c##sec_admin CONTAINER=ALL;
```

Similarly, the next example shows how local user `aud_admin` can grant the common user `c##sec_admin` the `AUDIT_ADMIN` common role for use within the `hrpdb` PDB.

```
CONNECT aud_admin@hrpdb
Enter password: password
Connected.

GRANT AUDIT_ADMIN TO c##sec_admin CONTAINER=CURRENT;
```

This example shows how a local user `aud_admin` can revoke a role from another user in a PDB. If you omit the `CONTAINER` clause, then `CURRENT` is implied.

```
CONNECT aud_admin@hrpdb
Enter password: password
Connected.

REVOKE sec_admin FROM psmith CONTAINER=CURRENT;
```

**Parent topic:** Managing Common Roles and Local Roles

### Restricting Operations on PDBs Using PDB Lockdown Profiles

You can use PDB lockdown profiles in a multitenant environment to restrict sets of user operations in pluggable databases (PDBs).

- About PDB Lockdown Profiles  
	A PDB lockdown profile is a named set of features that controls a group of operations.
- Default PDB Lockdown Profiles  
	Oracle Database provides a set of default PDB lockdown profiles that you can customize for your site requirements.
- Creating a PDB Lockdown Profile  
	To create a PDB lockdown profile, you must have the `CREATE LOCKDOWN PROFILE` system privilege.
- Enabling or Disabling a PDB Lockdown Profile  
	To enable or disable a PDB lockdown profile, use the `PDB_LOCKDOWN` initialization parameter
- Dropping a PDB Lockdown Profile  
	To drop a PDB lockdown profile, you must have the `DROP LOCKDOWN PROFILE` system privilege and be logged into the CDB or application root.

**Parent topic:** Managing Security for a Multitenant Environment

#### About PDB Lockdown Profiles

A PDB lockdown profile is a named set of features that controls a group of operations.

In some cases, you can enable or disable operations individually. For example, a PDB lockdown profile can contain settings to disable specific clauses that come with the `ALTER SYSTEM` statement.

PDB lockdown profiles restrict user access to the functionality the features provided, similar to resource limits that are defined for users. As the name suggests, you use PDB lockdown profiles in a CDB, for an application container, or for a PDB or application PDB. You can create custom profiles to accommodate the requirements of your site. PDB profiles enable you to define custom security policies for an application. In addition, you can create a lockdown profile that is based on another profile, called a **base profile**. You can configure this profile to be dynamically updated when the base profile is modified, or configure it to be static (unchanging) when the base profile is updated. Lockdown profiles are designed for both Oracle Cloud and on-premises environments.

When identities are shared between PDBs, elevated privileges may exist. You can use lockdown profiles to prevent this elevation of privileges. Identities can be shared in the following situations:

- At the operating system level, when the database interacts with operating system resources such as files or processes
- At the network level, when the database communicates with other systems, and network identity is important
- Inside the database, as PDBs access or create common objects or they communicate across container boundaries using features such as database links

The features that use shared identifies and that benefit from PDB lockdown profiles are in the following categories:

- Network access features. These are operations that use the network to communicate outside the PDB. For example, the PL/SQL packages `UTL_TCP`, `UTL_HTTP`, `UTL_MAIL`, `UTL_SNMP`, `UTL_INADDR`, and `DBMS_DEBUG_JDWP` perform these kinds of operations. Currently, ACLs are used to control this kind of access to share network identity.
- Common user or object access. These are operations in which a local user in the PDB can proxy through common user accounts or access objects in a common schema. These kinds of operations include adding or replacing objects in a common schema, granting privileges to common objects, accessing common directory objects, granting the `INHERIT PRIVILEGES` role to a common user, and manipulating a user proxy to a common user.
- Operating System access. For example, you can restrict access to the `UTL_FILE` or `DBMS_FILE_TRANSFER` PL/SQL packages.
- Connections. For example, you can restrict common users from connecting to the PDB or you can restrict a local user who has the `SYSOPER` administrative privilege from connecting to a PDB that is open in restricted mode.

The general procedure for creating a PDB lockdown profile is to first create it in the CDB root or the application root using the `CREATE LOCKDOWN PROFILE` statement, and then use the `ALTER LOCKDOWN PROFILE` statement to add the restrictions.

To enable a PDB lockdown profile, you can use the `ALTER SYSTEM` statement to set the `PDB_LOCKDOWN` parameter. You can find information about existing PDB lockdown profiles by connecting to CDB or application root and querying the `DBA_LOCKDOWN_PROFILES` data dictionary view. A local user can find the contents of a PDB lockdown parameter by querying the `V$LOCKDOWN_RULES` dynamic data dictionary view.

**Parent topic:** Restricting Operations on PDBs Using PDB Lockdown Profiles

#### Default PDB Lockdown Profiles

Oracle Database provides a set of default PDB lockdown profiles that you can customize for your site requirements.

By default, most of these profiles are empty. They are designed to be a placeholder or template for you to configure, depending on your deployment requirements.

Detailed information about these profiles is as follows:

- `PRIVATE_DBAAS` incorporates restrictions that are suitable for private Cloud Database-as-a-Service (DBaaS) deployments. These restrictions are:
	- Must have the same database administrator for each PDB
		- Different users permitted to connect to the database
		- Different applications permitted
	`PRIVATE_DBAAS` permits users to connect to the PDBs but prevents them from using Oracle Database administrative features.
- `SAAS` incorporates restrictions that are suitable for Software-as-a-Service (SaaS) deployments. These restrictions are:
	- Must have the same database administrator for each PDB
		- Different users permitted to connect to the database
		- Must use the same application
	The `SAAS` lockdown profile is more restrictive than the `PRIVATE_DBAAS` profile. Users can be different, but the application code is the same; users are prevented from directly connecting and must connect only through the application; and users are not granted the ability to perform any administrative features.
- `PUBLIC_DBAAS` incorporates restrictions that are suitable for public Cloud Database-as-a-Service (DBaaS) deployments. The restrictions are as follows:
	- Different DBAs in each PDB
		- Different users
		- Different applications
	The `PUBLIC_DBAAS` lockdown profile is the most restrictive of the lockdown profiles.

**Parent topic:** Restricting Operations on PDBs Using PDB Lockdown Profiles

#### Creating a PDB Lockdown Profile

To create a PDB lockdown profile, you must have the `CREATE LOCKDOWN PROFILE` system privilege.

After you create the lockdown profile, you can add restrictions before enabling it.

1. Connect to the CDB root or the application root as a user who has the `CREATE LOCKDOWN PROFILE` system privilege.
	For example, to connect to the CDB root:
	```
	CONNECT c##sec_admin
	Enter password: password
	```
2. Run the `CREATE LOCKDOWN PROFILE` statement to create the profile by using the following syntax:
	```
	CREATE LOCKDOWN PROFILE profile_name
	[FROM static_base_profile | INCLUDING dynamic_base_profile];
	```
	In this specification:
	- `profile_name` is the name that you assign the lockdown profile. You can find existing names by querying the `PROFILE_NAMES` column of the `DBA_LOCKDOWN_PROFILES` data dictionary view.
	- `FROM static_base_profile` creates a new lockdown profile by using the values from an existing profile. Any subsequent changes to the base profile will not affect the new profile.
	- `INCLUDING dynamic_base_profile` also creates a new lockdown profile by using the values from an existing base profile, except that this new lockdown profile will inherit the `DISABLE STATEMENT` rules that comprise the base profile, as well as any subsequent changes to the base profile. If rules that are explicitly added to the new profile conflict with the rules in the base profile, then the rules in the base profile take precedence. For example, an `OPTION_VALUE` clause in the base profile takes precedence over the `OPTION_VALUE` clause in the new profile.
	The following two PDB lockdown profile statements demonstrate how the inheritance works:
	```
	CREATE LOCKDOWN PROFILE hr_prof INCLUDING PRIVATE_DBAAS;
	CREATE LOCKDOWN PROFILE hr_prof2 FROM hr_prof;
	```
	In the first statement, `hr_prof` inherits any changes made to the `PRIVATE_DBAAS` base profile. If a new statement is enabled for `PRIVATE_DBAAS`, then it is enabled for `hr_prof`. In the second statement, in contrast, when `hr_prof` changes, then `hr_prof2` does not change because it is independent of its base profile.
3. Run the `ALTER LOCKDOWN PROFILE` statement to provide restrictions for the profile.
	For example:
	```
	ALTER LOCKDOWN PROFILE hr_prof DISABLE STATEMENT  = ('ALTER SYSTEM');
	ALTER LOCKDOWN PROFILE hr_prof ENABLE STATEMENT = ('ALTER SYSTEM') clause = ('flush shared_pool');
	ALTER LOCKDOWN PROFILE hr_prof DISABLE FEATURE = ('XDB_PROTOCOLS');
	```
	In the preceding example:
	- `DISABLE STATEMENT  = ('ALTER SYSTEM')` disables the use of all `ALTER SYSTEM` statements for the PDB.
	- `ENABLE STATEMENT = ('ALTER SYSTEM') clause = ('flush shared_pool')` enables only the use of the `FLUSH_SHARED_POOL` clause for `ALTER SYSTEM`.
	- `DISABLE FEATURE = ('XDB_PROTOCOLS')` prohibits the use of the XDB protocols (FTP, HTTP, HTTPS) by this PDB
	After you create a PDB lockdown profile, you are ready to enable it by using the `ALTER SYSTEM SET PDB_LOCKDOWN` SQL statement.

#### Enabling or Disabling a PDB Lockdown Profile

To enable or disable a PDB lockdown profile, use the `PDB_LOCKDOWN` initialization parameter

You can use `ALTER SYSTEM SET PDB_LOCKDOWN` to enable a lockdown profile in any of the following contexts:

- CDB (affects all PDBs)
- Application root (affects all application PDBs in the container)
- Application PDB
- PDB

Note:

It is not necessary to restart the instance to enable the profile. When the `ALTER SYSTEM SET PDB_LOCKDOWN` statement completes, the profile rules take effect immediately.

When you set `PDB_LOCKDOWN` in the CDB root, every PDB and application root inherits this setting unless `PDB_LOCKDOWN` is set at the container level. To disable lockdown profiles, set `PDB_LOCKDOWN` to null. If you set this parameter to null in the CDB root, then lockdown profiles are disabled for all PDBs except those that explicitly set a profile within the PDB.

A CDB common user who has been commonly granted the `SYSDBA` administrative privilege or the `ALTER SYSTEM` system privilege can set `PDB_LOCKDOWN` only to a lockdown profile that was created in the CDB root. An application common user with the application common `SYSDBA` administrative privilege or the `ALTER SYSTEM` system privilege can set `PDB_LOCKDOWN` only to a lockdown profile created in an application root.

1. Log in to the desired container as a user who has the commonly granted `ALTER SYSTEM` or commonly granted `SYSDBA` privilege.
	For example, to enable the profile for all PDBs, log in to the CDB root:
	```
	CONNECT c##sec_admin
	Enter password: password
	```
2. Run the `ALTER SYSTEM SET PDB_LOCKDOWN` statement.
	For example, the following statement enables the lockdown profile named `hr_prof` for all PDBs:
	```
	ALTER SYSTEM SET PDB_LOCKDOWN = hr_prof;
	```
	The following statement resets the `PDB_LOCKDOWN` parameter:
	```
	ALTER SYSTEM RESET PDB_LOCKDOWN;
	```
	This variation of the preceding statement includes the `SCOPE` clause::
	```
	ALTER SYSTEM RESET PDB_LOCKDOWN SCOPE = BOTH;
	```
	The following statement disables all lockdown profiles in the CDB except those that are explicitly set at the PDB level:
	```
	ALTER SYSTEM SET PDB_LOCKDOWN = '' SCOPE = BOTH;
	```
	To find the names of PDB lockdown profiles, query the `PROFILE_NAME` column of the `DBA_LOCKDOWN_PROFILES` data dictionary view.
3. Optionally, review information about the profiles by querying `DBA_LOCKDOWN_PROFILES`.
	For example, run the following query:
	```
	SET LINESIZE 150
	COL PROFILE_NAME FORMAT a20
	COL RULE FORMAT a20
	COL CLAUSE FORMAT a25
	SELECT PROFILE_NAME, RULE, CLAUSE, STATUS FROM CDB_LOCKDOWN_PROFILES;
	```
	Sample output appears below:
	```
	PROFILE_NAME      RULE                 CLAUSE                    STATUS
	----------------- -------------------- ------------------------- -------
	HR_PROF           XDB_PROTOCOLS                                  DISABLE
	HR_PROF           ALTER SYSTEM                                   DISABLE
	HR_PROF           ALTER SYSTEM         FLUSH SHARED_POOL         ENABLE
	HR_PROF2                                                         EMPTY
	PRIVATE_DBAAS                                                    EMPTY
	PUBLIC_DBAAS                                                     EMPTY
	SAAS                                                             EMPTY
	```

**Parent topic:** Restricting Operations on PDBs Using PDB Lockdown Profiles

#### Dropping a PDB Lockdown Profile

To drop a PDB lockdown profile, you must have the `DROP LOCKDOWN PROFILE` system privilege and be logged into the CDB or application root.

You can find the names of existing PDB lockdown profiles by querying the `DBA_LOCKDOWN_PROFILES` data dictionary view.

1. Connect to the CDB root or the application root as a user who has the `DROP LOCKDOWN PROFILE` system privilege.
	For example, to connect to the CDB root:
	```
	CONNECT c##sec_admin
	Enter password: password
	```
2. Run the `DROP LOCKDOWN_PROFILE` statement.
	For example:
	```
	DROP LOCKDOWN PROFILE hr_prof2;
	```
3. Optionally, review the current list of profiles by querying `DBA_LOCKDOWN_PROFILES`.
	For example, run the following query:
	```
	SET LINESIZE 150
	COL PROFILE_NAME FORMAT a20
	COL RULE FORMAT a20
	COL CLAUSE FORMAT a25
	SELECT PROFILE_NAME, RULE, CLAUSE, STATUS FROM CDB_LOCKDOWN_PROFILES;
	```
	Sample output appears below:
	```
	PROFILE_NAME      RULE                 CLAUSE                    STATUS
	----------------- -------------------- ------------------------- -------
	HR_PROF           XDB_PROTOCOLS                                  DISABLE
	HR_PROF           ALTER SYSTEM                                   DISABLE
	HR_PROF           ALTER SYSTEM         FLUSH SHARED_POOL         ENABLE
	PRIVATE_DBAAS                                                    EMPTY
	PUBLIC_DBAAS                                                     EMPTY
	SAAS                                                             EMPTY
	```

**Parent topic:** Restricting Operations on PDBs Using PDB Lockdown Profiles

### Configuring Operating System Users for a PDB

The `DBMS_CREDENTIAL.CREATE_CREDENTIAL` procedure configures user accounts to be operating system users for a pluggable database (PDB).

- About Configuring Operating System Users for a PDB  
	Instead the `oracle` operating system user, you can set a specific user account to be the operating system user for that PDB.
- Configuring an Operating System User for a PDB  
	The `DBMS_CREDENTIAL.CREATE_CREDENTIAL` procedure can set an operating system user for a PDB.
- Setting the Default Credential in a PDB  
	You can set the database property `DEFAULT_CREDENTIAL` for a specified PDB.

**Parent topic:** Managing Security for a Multitenant Environment

#### About Configuring Operating System Users for a PDB

Instead the `oracle` operating system user, you can set a specific user account to be the operating system user for that PDB.

If you do not set a specific user to be the operating system user for the PDB, then by default the PDB uses the `oracle` operating system user. For the root, you can use the `oracle` operating system user when you must interact with the operating system.

For better security, Oracle recommends that you set a unique operating system user for each PDB in a multitenant environment. Doing so helps to ensure that operating system interactions are performed as a less powerful user than the `oracle` operating system user, and helps to protect data that belongs to one PDB from being accessed by users who are connected to other PDBs.

**Parent topic:** Configuring Operating System Users for a PDB

#### Configuring an Operating System User for a PDB

The `DBMS_CREDENTIAL.CREATE_CREDENTIAL` procedure can set an operating system user for a PDB.

1. Log in to the database instance root as a user who has the `EXECUTE` privilege for the `DBMS_CREDENTIAL` PL/SQL package and the `ALTER SYSTEM` system privilege.
	For example:
	```
	sqlplus c##sec_admin
	Enter password: password
	```
2. Run the `DBMS_CREDENTIAL.CREATE_CREDENTIAL` procedure to create an Oracle credential for the operating system user.
	For example, to set the credential for a user named `os_admin`:
	```
	BEGIN 
	 DBMS_CREDENTIAL.CREATE_CREDENTIAL (
	    credential_name => 'PDB1_OS_USER',
	    username        => 'os_admin',
	    password        => 'password');
	END;
	/
	```
3. Connect to the PDB for which the operating system user will be used.
	For example:
	```
	CONNECT cc##sec_admin@hrpdb
	Enter password: password
	```
	To find the available PDBs, run the `show pdbs` command. To check the current PDB, run the show `con_name` command.
4. Set the `PDB_OS_CREDENTIAL` initialization parameter for the user whose credential was set in Step 2.
	For example:
	```
	ALTER SYSTEM SET PDB_OS_CREDENTIAL = PDB1_OS_USER SCOPE = SPFILE;
	```
	The `PDB_OS_CREDENTIAL` parameter is a static parameter, so you must set it using the `SCOPE = SPFILE` clause.
5. ```
	SHUTDOWN IMMEDIATE
	STARTUP
	```

**Parent topic:** Configuring Operating System Users for a PDB

#### Setting the Default Credential in a PDB

You can set the database property `DEFAULT_CREDENTIAL` for a specified PDB.

A default credential is useful when importing files from an object store into a PDB. If you do not specify a credential name when using `impdp`, then Oracle Data Pump and the object store module can use the `DEFAULT_CREDENTIAL` object to retrieve the user name and password. When running `impdp` without specifying a credential, you must prefix the dump file name with `DEFAULT_CREDENTIAL:`.

To set the default credential:

1. Log in to a PDB with administrator privileges.
2. Use an `ALTER DATABASE` statement to set the default credential.
	For example, enter the following statement to set the credential to `SYSTEM.HR_CRED`.
	```
	ALTER DATABASE PROPERTY SET DEFAULT_CREDENTIAL = 'SYSTEM.HR_CRED';
	```

Example 18-3 Importing Data into a PDB Using the Default Credential

This example assumes that a default credential exists. The following command imports data from an object store, prefacing the URL with the string `DEFAULT_CREDENTIAL`:

```
impdp hr@pdb1 table_exists_action=replace \
  dumpfile=DEFAULT_CREDENTIAL:https://example.com/ostore/obucket/myt.dmp
```

See Also:

- " [Using Data Pump to Move Data Into a CDB](using-database-utilities-in-a-cdb.md) "
- [Oracle Database Utilities](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=GUID-D11E340E-14C6-43B8-AB09-6335F0C1F71B) to learn about Data Pump Import

**Parent topic:** Configuring Operating System Users for a PDB

### Using Application Contexts in a Multitenant Environment

An application context stores user identification that can enable or prevent a user from accessing data in the database.

- What Is an Application Context?  
	An **application context** is a set of name-value pairs that Oracle Database stores in memory.
- Application Contexts in a Multitenant Environment  
	Where you create an application in a multitenant environment determines where you must create the application context.

**Parent topic:** Managing Security for a Multitenant Environment

#### What Is an Application Context?

An **application context** is a set of name-value pairs that Oracle Database stores in memory.

The context has a label called a **namespace** (for example, `empno_ctx` for an application context that retrieves employee IDs). This context enables Oracle Database to find information about both database and nondatabase users during authentication.

Inside the context are the name-value pairs (an associative array): the name points to a location in memory that holds the value. An application can use the application context to access session information about a user, such as the user ID or other user-specific information, or a client ID, and then securely pass this data to the database.

You can then use this information to either permit or prevent the user from accessing data through the application. You can use application contexts to authenticate both database and non-database users.

#### Application Contexts in a Multitenant Environment

Where you create an application in a multitenant environment determines where you must create the application context.

If an application is installed in the application root or CDB root, then it becomes accessible across the application container or system container and associated application PDBs. You will need to create a common application context in this root.

When you create a common application context for use with an application container, note the following:

- You can create application contexts in a multitenant environment by setting the `CONTAINER` clause in the `CREATE CONTEXT` SQL statement. For example, to create a common application context in the application root, you must execute `CREATE CONTEXT` with `CONTAINER` set to `ALL`. To create the application context in a PDB, set `CONTAINER` to `CURRENT`.
- You cannot use the same name for a local application context for a common application context. You can find the names of existing application contexts by running the following query:
	```
	SELECT OBJECT_NAME FROM DBA_OBJECTS WHERE OBJECT_TYPE ='CONTEXT';
	```
- The PL/SQL package that you create to manage a common application context must be a common PL/SQL package. That is, it must exist in the application root or CDB root. If you create the application context for a specific PDB, then you must store the associated PL/SQL package in that PDB.
- The name-value pairs that you set under a common session application context from an application container or a system container for a common application context are not accessible from other application containers or system containers when a common user accesses a different container.
- The name-value pairs that you set under a common global application context from an application container or a system container, are accessible only within the same container in the same user session.
- An application can retrieve the value of an application context whether it resides in the application root, the CDB root, or a PDB.
- During a plug-in operation of a PDB into a CDB or an application container, if the name of the common application context conflicts with a PDB’s local application context, then the PDB must open in restricted mode. A database administrator would then need to correct the conflict before opening the PDB in normal mode.
- During an unplug operation, a common application context retains its common semantics, so that later on, if the PDB is plugged into another CDB where a common application context with the same name exists, it would continue to behave like a common object. If a PDB is plugged into an application container or a system container, where the same common application context does not exist, then it behaves like a local object.

To find if an application context is a local application context or an application common application context, query the `SCOPE` column of the `DBA_CONTEXT` or `ALL_CONTEXT` data dictionary view.

### Using Oracle Virtual Private Database in a Multitenant Environment

Oracle Virtual Private Database (VPD) enables you to filter users who access data.

- What Is Oracle Virtual Private Database?  
	Oracle Virtual Private Database (VPD) creates security policies to control database access at the row and column level.
- Oracle Virtual Private Database in a Multitenant Environment  
	You can create Virtual Private Database policies in an application root for use throughout any associated application PDBs.

**Parent topic:** Managing Security for a Multitenant Environment

#### What Is Oracle Virtual Private Database?

Oracle Virtual Private Database (VPD) creates security policies to control database access at the row and column level.

Note:

Oracle Database release 12c introduced Real Application Security (RAS) to supersede VPD. Oracle recommends that you use RAS for new projects that require row and column level access controls for their applications.

Essentially, Oracle Virtual Private Database adds a dynamic `WHERE` clause to a SQL statement that is issued against the table, view, or synonym to which an Oracle Virtual Private Database security policy was applied.

Oracle Virtual Private Database enforces security, to a fine level of granularity, directly on database tables, views, or synonyms. Because you attach security policies directly to these database objects, and the policies are automatically applied whenever a user accesses data, there is no way to bypass security.

When a user directly or indirectly accesses a table, view, or synonym that is protected with an Oracle Virtual Private Database policy, Oracle Database dynamically modifies the SQL statement of the user. This modification creates a `WHERE` condition (called a predicate) returned by a function implementing the security policy. Oracle Database modifies the statement dynamically, transparently to the user, using any condition that can be expressed in or returned by a function. You can apply Oracle Virtual Private Database policies to `SELECT`, `INSERT`, `UPDATE`, `INDEX`, and `DELETE` statements.

For example, suppose a user performs the following query:

```
SELECT * FROM OE.ORDERS;
```

The Oracle Virtual Private Database policy dynamically appends the statement with a `WHERE` clause. For example:

```
SELECT * FROM OE.ORDERS 
 WHERE SALES_REP_ID = 159;
```

In this example, the user can only view orders by Sales Representative 159.

If you want to filter the user based on the session information of that user, such as the ID of the user, then you can create the `WHERE` clause to use an application context. For example:

```
SELECT * FROM OE.ORDERS 
 WHERE SALES_REP_ID = SYS_CONTEXT('USERENV','SESSION_USER');
```

Note:

Oracle Virtual Private Database does not support filtering for DDLs, such as `TRUNCATE` or `ALTER TABLE` statements.

#### Oracle Virtual Private Database in a Multitenant Environment

You can create Virtual Private Database policies in an application root for use throughout any associated application PDBs.

The CDB restriction applies to shared context sensitive policies and views related to Virtual Private Database policies as well. You cannot create a Virtual Private Database policy for an entire multitenant environment.

With regard to application containers, you can create Virtual Private Database policies to protect application common objects by applying the common policy to all PDBs that belong to the application root. In other words, when you install an application in the application root, all the common Virtual Private Database policies that protect the common objects will be applied to and immediately enforced for all PDBs in the application container.

Note the following:

- You can only create the common Virtual Private Database policy and its associated PL/SQL function in the application root and only attach it to application common objects. If the function is not in the same location as the policy, then an error is raised at runtime.
- A Virtual Private Database policy that is applied to common objects is considered a common policy that will be automatically enforced in PDBs that belong to the application container when it accesses the application common objects from application PDBs.
- Application common Virtual Private Database policies can only protect application common objects.
- A Virtual Private Database policy that is applied to application common objects in the application root and is applied to all application PDBs is considered a common Virtual Private Database policy. A policy that is applied to a local database table and enforced in one PDB is considered a local Virtual Private Database policy.
	For example, if policy `VPD_P1` is applied to the application common table `T1` in the application root, then it is a considered to be a common policy. It will be enforced in each application PDB. If a policy named `VPD_P1` is applied to a local table called `T1` in `PDB1`, then it is considered a local policy, which means that it affects only `PDB1`. If a policy called `VPD_P1` is applied to a local table `T1` in the application root, then it is still considered a local policy because it affects only the application root. This concept applies to other operations, such as enabling, disabling, and removing Virtual Private Database policies.
- Application common Virtual Private Database policies only protect application common objects, while local Virtual Private Database policies only protect local objects.
- If you are using application contexts, then ensure common database session-based application contexts and common global application context objects are used in the common Virtual Private Database configuration.
- Application container Virtual Private Database policies are stored in the application root. PDBs store only local policies. If you plug a PDB into the application container, then the common policies are not converted to local policies. Instead, Oracle Database loads them from the application root and enforces them in the local PDB when the policies access common objects in the local PDB.

### Using Transport Layer Security in a Multitenant Environment

Transport Layer Security (TLS) can be used in a multitenant environment for application containers.

If you want to use Transport Layer Security (TLS) in a multitenant environment for an application container, then you must ensure that each PDB is able to use its own wallet with its own certificates for TLS authentication.

- Because there is no individual `sqlnet.ora` file for each PDB, place the wallet in a subdirectory of the `wallet` directory where the name of the subdirectory is the GUID of the PDB that uses the wallet.
	For example, suppose the `WALLET_LOCATION` parameter in `sqlnet.ora` is set as follows:
	```
	(SOURCE=(METHOD=FILE)(METHOD_DATA=
	   (DIRECTORY=/home/oracle/wallet)))
	```
	Place each PDB’s wallet in the `/home/oracle/wallet/PDB_GUID` directory. You can find the existing PDBs and their GUIDs by querying the `DBA_PDBS` data dictionary view.
	If the `WALLET_LOCATION` parameter is not specified, then you must place the PDB wallet in a leaf subdirectory of the default wallet path where the name of the subdirectory is the GUID of the PDB, and the name of the leaf subdirectory is `wallet`. For example:
	```
	$ORACLE_BASE/admin/db_unique_name/PDB_GUID/wallet
	```
	Or if the `ORACLE_BASE` environment variable is not set, then you can use the Oracle home:
	```
	$ORACLE_HOME/admin/db_unique_name/PDB_GUID/wallet
	```
	These default locations correspond to the default that is used by Oracle Enterprise User Security to locate wallets for authentication to LDAP.

### Oracle Data Redaction in a Multitenant Environment

In a multitenant environment, Oracle Data Redaction policies apply only to the objects within the current pluggable database (PDB).

You cannot create a Data Redaction policy for a multitenant container database (CDB). This is because the objects for which you create Data Redaction policies typically reside in a PDB. If you have the `SYSDBA` privilege, then you can list all the PDBs in a CDB by running the `SHOW PDBS` command.

As with the CDB root, you cannot create Data Redaction policies in an application root.

**Parent topic:** Managing Security for a Multitenant Environment

### Overview of Auditing in a Multitenant Environment

Auditing is the monitoring and recording of configured database actions, from both database users and nondatabase users. Nondatabase users are application users who are recognized in the database using the `CLIENT_IDENTIFIER` attribute.

You can base auditing on individual actions, such as the type of SQL statement executed, or on combinations of data that can include the user name, application, time, and so on. You can configure auditing for both successful and failed activities, and include or exclude specific users from the audit. In a multitenant environment, you can audit individual actions of the pluggable database (PDB) or individual actions in the entire multitenant container database (CDB).

Auditing is enabled by default. Audit records are written to the unified audit trail in a uniform format and are made available through the `UNIFIED_AUDIT_TRAIL` view.

- Unified Auditing in a Multitenant Environment  
	You can use unified auditing in a multitenant environment.
- Example: Auditing the DBA Role in a Multitenant Environment  
	The `CREATE AUDIT POLICY` statement can audit roles in a multitenant environment.
- Unified Audit Policies or AUDIT Settings in a Multitenant Environment  
	In a multitenant environment, you can create unified audit policies for individual PDBs and in the root.
- Fine-Grained Auditing in a Multitenant Environment  
	You can create fine-grained audit policies in the CDB root, application root, CDB PDBs, and application PDBs.

**Parent topic:** Managing Security for a Multitenant Environment

#### Unified Auditing in a Multitenant Environment

You can use unified auditing in a multitenant environment.

You can apply audit settings to individual PDBs or to the CDB, depending on the type of policy. In a multitenant environment, each PDB, including the root, has its own unified audit trail.

Audit settings in a multitenant environment affect the following areas:

- Unified audit policies created with the CREATE AUDIT POLICY and AUDIT statements: You can create policies for both the root and individual PDBs.
- Audit records written to the syslog: On UNIX platforms, you can set the `UNIFIED_AUDIT_COMMON_SYSTEMLOG` initialization parameter in the CDB root to enable certain unified audit trail columns to be written to SYSLOG. On both Windows and UNIX, you can set the `UNIFIED_AUDIT_SYSTEMLOG` parameter in both the root and PDB level.
- Fine-grained audit policies: You can create policies for individual PDBs only, not the root.
- Purging the audit trail: You can perform purge operations for both the root and individual PDBs.

#### Example: Auditing the DBA Role in a Multitenant Environment

The `CREATE AUDIT POLICY` statement can audit roles in a multitenant environment.

The following example shows how to audit a predefined common role `DBA` in a multitenant environment.

Example 18-4 Auditing the DBA Role in a Multitenant Environment

```
CREATE AUDIT POLICY role_dba_audit_pol 
 ROLES DBA
 CONTAINER = ALL;

AUDIT POLICY role_dba_audit_pol;
```

**Parent topic:** Overview of Auditing in a Multitenant Environment

#### Unified Audit Policies or AUDIT Settings in a Multitenant Environment

In a multitenant environment, you can create unified audit policies for individual PDBs and in the root.

- About Local, CDB Common, and Application Common Audit Policies  
	An audit policy can be either a local audit policy, a CDB common audit policy, or an application common audit policy.
- Traditional Auditing in a Multitenant Environment  
	In traditional auditing (not unified auditing), the `AUDIT` and `NOAUDIT` statements can audit statements and privileges in a multitenant environment.
- Configuring a Local Unified Audit Policy or Common Unified Audit Policy  
	The `CONTAINER` clause is specific to multitenant environment use for the `CREATE AUDIT POLICY` statement.
- Example: Local Unified Audit Policy  
	The CREATE AUDIT POLICY statement can create a local unified audit policy in either the root or a PDB.
- Example: CDB Common Unified Audit Policy  
	The CREATE AUDIT POLICY statement can create a CDB common unified audit policy.
- Example: Application Common Unified Audit Policy  
	For application container common unified audit policies, you can audit action options and system privilege options, and refer to common objects and roles.
- How Local or Common Audit Policies or Settings Appear in the Audit Trail  
	You can query unified audit policy views from either the root or the PDB in which the action occurred.

**Parent topic:** Overview of Auditing in a Multitenant Environment

##### About Local, CDB Common, and Application Common Audit Policies

An audit policy can be either a local audit policy, a CDB common audit policy, or an application common audit policy.

This applies to both unified audit policies and policies that are created using the `AUDIT` SQL statement.

- Local audit policy. This type of policy can exist in either the root (CDB or application) or the PDB (CDB or application). A local audit policy that exists in the root can contain object audit options for both local and common objects. Both local and common users who have been granted the `AUDIT_ADMIN` role can enable local policies: local users from their PDBs and common users from the root or the PDB to which they have privileges. You can enable a local audit policy for both local and common users and roles.
	You can create local audit policies for application local objects and application local roles, as well as system action options and system privilege options. You cannot enforce a local audit policy for a common user across all containers, nor can you enforce a common audit policy for a local user.
- CDB common audit policy. This type of policy is available to all PDBs in the multitenant environment. Only common users who have been granted the `AUDIT_ADMIN` role can create and maintain common audit policies. You can enable common audit policies only for common users. You must create common audit policies only in the root. This type of policy can contain object audit options of only common objects, and be enabled only for common users. You can enable a common audit policy for common users and roles only.
	You cannot enforce a common audit policy for a local user across all containers.
- Application common audit policy. Similar to CDB common audit policies, this type of policy is available to all PDBs in the multitenant environment. You can create common audit policies for application common objects and application common roles, as well as system action options and system privilege options. You can only create this type of policy in the application root container, but you can enable it on both application common users and CDB common users. If you want to audit objects, then ensure that these objects are application common objects. You can determine whether an object is an application common object by querying the `SHARING` column of the `DBA_OBJECTS` data dictionary view.

By default, audit policies are local to the current PDB, for both CDB and application scenarios.

The following table explains how audit policies apply in different multitenant environments.

Table 18-1 How Audit Policies Apply to the CDB Root, Application Root, and Individual PDBs

| Audit Option Type | CDB Root | Application Root | Individual PDB |
| --- | --- | --- | --- |
| Common audit statement or audit policy | Applies to CDB common users | Applies to CDB common users | Applies to CDB common users |
| Application container common audit statement or audit policy | Not applicable | - Applies to CDB common users and are valid for the current application container only - Applies to application container common users | - Applies to CDB common users and are valid for this application container only - Applies to application common users |
| Local audit statement or audit policy | Local configurations not allowed | Local configurations not allowed | - Applies to CDB common users - Applies to application common users |

**Parent topic:** Unified Audit Policies or AUDIT Settings in a Multitenant Environment

##### Traditional Auditing in a Multitenant Environment

In traditional auditing (not unified auditing), the `AUDIT` and `NOAUDIT` statements can audit statements and privileges in a multitenant environment.

To configure the audit policy to be either a local audit policy or a common audit policy, you must include the `CONTAINER` clause, as you normally do for other SQL creation or modification statements. If you want to audit an application container, then you can audit SQL statement and system privileges performed by local and common users and roles. The audit record will be created in the container in which the action was performed.

- If you want to apply the `AUDIT` or `NOAUDIT` statement to the current CDB or application PDB, then in this PDB, you must set `CONTAINER` to `CURRENT`. For example:
	```
	AUDIT DROP ANY TABLE BY SYSTEM BY ACCESS CONTAINER = CURRENT;
	```
- If you want to apply the `AUDIT` or `NOAUDIT` statement to the entire multitenant environment, then in the CDB root, then you must set `CONTAINER` to `ALL`. For an application container, you would set it in the application root. For example:
	```
	AUDIT DROP ANY TABLE BY SYSTEM BY ACCESS CONTAINER = ALL;
	```

To find if a traditional audit option is designed for use in an application container, perform a join query with the `DBA_OBJ_AUDIT_OPTS` and `DBA_OBJECTS` data dictionary views, by using the `OWNER` and `OBJECT_NAME` columns in both views, and the `APPLICATION` column in `DBA_OBJECTS`.

See Also:

Oracle Database SQL Language Reference for more information about the traditional [`AUDIT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF01107) and [`NOAUDIT`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/multi&id=SQLRF01607) SQL statements

**Parent topic:** Unified Audit Policies or AUDIT Settings in a Multitenant Environment

##### Configuring a Local Unified Audit Policy or Common Unified Audit Policy

The `CONTAINER` clause is specific to multitenant environment use for the `CREATE AUDIT POLICY` statement.

To create a local or common (CDB or application) unified audit policy in either the CDB environment or an application container environment, include the `CONTAINER` clause in the `CREATE AUDIT POLICY` statement.

- Use the following syntax to create a local or common unified audit policy:
	```
	CREATE AUDIT POLICY policy_name
	 action1 [,action2 ]
	 [CONTAINER = {CURRENT | ALL}];
	```

In this specification:

- `CURRENT` sets the audit policy to be local to the current PDB.
- `ALL` makes the audit policy a common audit policy, that is, available to the entire multitenant environment.

For example, for a common unified audit policy:

```
CREATE AUDIT POLICY dict_updates 
 ACTIONS UPDATE ON SYS.USER$, 
  DELETE ON SYS.USER$, 
  UPDATE ON SYS.LINK$, 
  DELETE ON SYS.LINK$ 
  CONTAINER = ALL;
```

Note the following:

- You can set the `CONTAINER` clause for the `CREATE AUDIT POLICY` statement but not for `ALTER AUDIT POLICY` or `DROP AUDIT POLICY`. If you want to change the scope of an existing unified audit policy to use this setting, then you must drop and re-create the policy.
- For `AUDIT` statements, you can set the `CONTAINER` clause for audit settings only if you have an Oracle database that has not been migrated to the Release 12.x and later audit features. You cannot use the `CONTAINER` clause in an `AUDIT` statement that is used to enable a unified audit policy.
- If you are in a PDB, then you can only set the `CONTAINER` clause to `CURRENT`, not `ALL`. If you omit the setting while in the PDB, then the default is `CONTAINER = CURRENT`.
- If you are in the root, then you can set the `CONTAINER` clause to either `CURRENT` if you want the policy to apply to the root only, or to `ALL` if you want the policy to apply to the entire CDB. If you omit the `CONTAINER` clause, then default is `CONTAINER = CURRENT`.
- For objects:
	- Common audit policies can have common objects only and local audit policies can have both local objects and common objects.
		- You cannot set `CONTAINER` to `ALL` if the objects involved are local. They must be common objects.
- For privileges:
	- You can set the `CONTAINER` to `CURRENT` (or omit the `CONTAINER` clause) if the user accounts involved are a mixture of local and common accounts. This creates a local audit configuration that applies only to the current PDB.
		- You cannot set `CONTAINER` to `ALL` if the users involved are local users. They must be common users.
		- If you set `CONTAINER` to `ALL` and do not specify a user list (using the `BY` clause in the `AUDIT` statement), then the configuration applies to all common users in each PDB.
- For application containers, you can run a common unified audit policy from the application container script that is used for application install, upgrade, patch, and uninstall operations. To do so:
	1. Create a common unified audit policy in the application container root, and set this policy to `CONTAINER = ALL`. Alternatively, you can include this policy in the script that is described in this next step.
		2. Create a custom version of the script you normally would use to install, upgrade, patch, or uninstall Oracle Database.
		3. Within this script, include the SQL statements that you want to audit within the following lines:
		```
		ALTER PLUGGABLE DATABASE APPLICATION BEGIN INSTALL
		List SQL statements here. Separate each statement with a semi-colon.
		ALTER PLUGGABLE DATABASE APPLICATION END INSTALL
		```
		If you include the unified audit policy in the script, then ensure that you include both the `CREATE AUDIT POLICY` and `AUDIT POLICY` statements.
	After the audit policy is created and enabled, all user access to the application common objects is audited irrespective of whether the audit policy is defined in the database or from the script.
- To audit application install, upgrade, patch, and uninstall operations locally in an application root or an application PDB, follow a procedure similar to the preceding procedure for common unified audit policies, but synchronize the application PDB afterward. For example:
	```
	ALTER PLUGGABLE DATABASE APPLICATION application_name SYNC;
	```

##### Example: Local Unified Audit Policy

The CREATE AUDIT POLICY statement can create a local unified audit policy in either the root or a PDB.

When you create a local unified audit policy in the root, it only applies to the root and not across the multitenant environment.

The following example shows a local unified audit policy that has been created by the common user `c##sec_admin` from a PDB and applied to common user `c##hr_admin`.

Example 18-5 Local Unified Audit Policy

```
CONNECT c##sec_admin@hrpdb
Enter password: password
Connected.

CREATE AUDIT POLICY table_privs
 PRIVILEGES CREATE ANY TABLE, DROP ANY TABLE
 CONTAINER = CURRENT;

AUDIT POLICY table_privs BY c##hr_admin;
```

**Parent topic:** Unified Audit Policies or AUDIT Settings in a Multitenant Environment

##### Example: CDB Common Unified Audit Policy

The CREATE AUDIT POLICY statement can create a CDB common unified audit policy.

Example 18-6 shows a common unified audit policy that has been created by the common user `c##sec_admin` from the root and applied to common user `c##hr_admin`.

Example 18-6 Common Unified Audit Policy

```
CONNECT c##sec_admin
Enter password: password
Connected.

CREATE AUDIT POLICY admin_pol
 ACTIONS CREATE TABLE, ALTER TABLE, DROP TABLE
 ROLES c##hr_mgr, c##hr_sup
 CONTAINER = ALL;

AUDIT POLICY admin_pol BY c##hr_admin;
```

**Parent topic:** Unified Audit Policies or AUDIT Settings in a Multitenant Environment

##### Example: Application Common Unified Audit Policy

For application container common unified audit policies, you can audit action options and system privilege options, and refer to common objects and roles.

You can create the application common audit policy only from the application root, and enable the policy for both application common users and CDB common users.

The following example shows how to create a policy that audits the application common user `SYSTEM` for the application container `app_pdb`. The audit policy audits `SELECT` actions on the `SYSTEM.utils_tab` table and on `DROP TABLE` actions on any of the PDBs in the container database, including the CDB root. The policy also audits the use of the `SELECT ANY TABLE` system privilege across all containers.

Example 18-7 Application Common Unified Audit Policy

```
CONNECT c##sec_admin@app_pdb
Enter password: password
Connected.

CREATE AUDIT POLICY app_pdb_admin_pol
 ACTIONS SELECT ON hr_app_cdb.utils_tab, DROP TABLE
 PRIVILEGES SELECT ANY TABLE
 CONTAINER = ALL;

AUDIT POLICY app_pdb_admin_pol by SYSTEM, c##hr_admin;
```

In the preceding example, setting `CONTAINER` to `ALL` applies the policy only to all the relevant object accesses in the application root and on all the application PDBs that belong to the application root. It does not apply the policy outside this scope.

**Parent topic:** Unified Audit Policies or AUDIT Settings in a Multitenant Environment

##### How Local or Common Audit Policies or Settings Appear in the Audit Trail

You can query unified audit policy views from either the root or the PDB in which the action occurred.

You can perform the following types of queries:

- Audit records from all PDBs. The audit trail reflects audited actions that have been performed in the PDBs. For example, if user `lbrown` in `PDB1` performs an action that has been audited by either a common or a local audit policy, then the audit trail will capture this action. The `DBID` column in the `UNIFIED_AUDIT_TRAIL` data dictionary view indicates the PDB in which the audited action takes place and to which the policy applies. If you want to see audit records from all PDBs, you should query the `CDB_UNIFIED_AUDIT_TRAIL` data dictionary view from the root.
- Audit records from common audit policies. This location is where the common audit policy results in an audit record. The audit record can be generated anywhere in the multitenant environment—the root or the PDBs, depending on where the action really occurred. For example, the common audit policy `fga_pol` audits the `EXECUTE` privilege on the `DBMS_FGA` PL/SQL package, and if this action occurs in `PDB1`, then the audit record is generated in `PDB1` and not in the root. Hence, the audit record can be seen in PDB1.
	You can query the `UNIFIED_AUDIT_TRAIL` data dictionary view for the policy from either the root or a PDB if you include a `WHERE` clause for the policy name (for example, `WHERE UNIFIED_AUDIT_POLICIES = 'FGA_POL'`).

The following example shows how to find the results of a common unified audit policy:

```
CONNECT c##sec_admin
Enter password: password
Connected.

SELECT DBID, ACTION_NAME, OBJECT_SCHEMA, OBJECT_NAME FROM CDB_UNIFIED_AUDIT_TRAIL WHERE DBUSERNAME = 'c##hr_admin';
46892-1
DBID        ACTION_NAME  OBJECT_SCHEMA  OBJECT_NAME
----------- -----------  -------------  -----------
653916017   UPDATE       HR             EMPLOYEES
653916018   UPDATE       HR             JOB_HISTORY
653916017   UPDATE       HR             JOBS
```

**Parent topic:** Unified Audit Policies or AUDIT Settings in a Multitenant Environment

#### Fine-Grained Auditing in a Multitenant Environment

You can create fine-grained audit policies in the CDB root, application root, CDB PDBs, and application PDBs.

Note the following general rules about fine-grained audit policies in a multitenant environment:

- You cannot create fine-grained audit policies on `SYS` objects.
- You cannot create fine-grained audit policies, either local or application common, for extended data link objects.
- When you create a fine-grained audit policy in the CDB root, the policy cannot be applied to all PDBs. It only applies to objects within the CDB root. (In other words, there is no such thing as a common fine-grained audit policy for the CDB root.) If you want to create a fine-grained audit policy to audit a common object’s access in all the PDBs, then you must explicitly create that policy in each PDB and then enable it on the common objects that is accessible in the PDB.
- When you create a fine-grained audit policy in a PDB, it applies only to objects within the PDB.
- You can create application common fine-grained audit policies only if you are connected to the application root and only within the `BEGIN` / `END` block. If you are connected to the application root and create the fine-grained audit policy outside the `BEGIN` / `END` block, then the fine-grained audit policy is created in the application root.
- You cannot create application common fine-grained audit policies on local PDB objects.
- If the application common fine-grained audit policy has a handler, then this handler must be owned by either an application common user or a CDB common user.
- You can create an application fine-grained audit policy on local (PDB) objects and CDB common objects. Because the policy is local to its container, the object on which the policy is defined is audited only in the particular container where the policy is defined. For example, if you create a fine-grained audit policy in the `hr_pdb` PDB, the object for which you create this policy must exist in the `hr_pdb` PDB.
- You cannot create local fine-grained audit policies in an application PDB on object linked and extended data link objects. On metadata-linked objects are allowed in the fine-grained audit policy.
- Application root local policies are allowed for all application common objects.
- When you create a fine-grained audit policy as a common audit policy in an application root, it will be effective in each PDB that belongs to this application root. Therefore, any access to the application common object and CDB common object (on which the application common fine-grained audit policy is defined) from the application PDB is audited in the fine-grained audit trail in that application PDB.
- When you create scripts for application install, upgrade, patch, or uninstall operations, you can include SQL statements within the `ALTER PLUGGABLE DATABASE app_name BEGIN INSTALL` and `ALTER PLUGGABLE DATABASE app_name END INSTALL` blocks to perform various operations. You can include fine-grained audit policy statements only within these blocks.
- You can only enable, disable, or drop application common fine-grained audit policies from the application root, and from within a `ALTER PLUGGABLE DATABASE app_name BEGIN INSTALL` and `ALTER PLUGGABLE DATABASE app_name END INSTALL` block in a script.