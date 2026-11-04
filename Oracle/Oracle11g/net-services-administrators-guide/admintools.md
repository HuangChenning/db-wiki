---
title: Managing Oracle Net Services
book: "Net Services Administrator's Guide"
doc_id: E41945-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e41945/admintools.htm
tags:
  - oracle
  - 11g
  - net-services-administrators-guide
---

## 7 Managing Oracle Net Services

This chapter introduces the various administration tools of Oracle Net Services. It discusses the main administration applications, [Oracle Enterprise Manager](glossary.md) and [Oracle Net Manager](glossary.md). It also introduces the command-line control utilities.

This chapter contains the following topics:

## Using the User Interface Tools

Oracle Net Services provides tools to help you perform configuration and administrative tasks. This section contains the following topics:

- Using Oracle Enterprise Manager to Configure Oracle Net Services
- Using Oracle Net Manager to Configure Oracle Net Services
- Deciding When to Use Oracle Enterprise Manager and Oracle Net Manager
- Using Oracle Net Configuration Assistant to Configure Network Components

### Using Oracle Enterprise Manager to Configure Oracle Net Services

Oracle Enterprise Manager enables you to configure Oracle Net Services for any Oracle home across multiple file systems. It also provides common administration functions for listeners. Oracle Enterprise Manager provides an integrated environment for configuring and managing Oracle Net Services.

You can use Oracle Enterprise Manager to configure and administer the following from multiple Oracle homes:

- Listeners: Configure listeners to receive client connections.
- Naming: Define [connect identifier](glossary.md) s and map them to [connect descriptor](glossary.md) s to identify the network location of a service. Oracle Net Manager supports configuration of connect descriptors in local `tnsnames.ora` files or a centralized directory service.
- File Location: Specify the file location of the Oracle Net configuration files.

See Also:

Oracle Enterprise Manager documentation set and online Help for information about using Oracle Enterprise Manager

#### Accessing the Net Services Administration Page

To access the Net Services Administration page using Oracle Enterprise Manager:

1. From the Login to Database page, enter the database credentials, and then click Login.
	The Database page appears.
2. In the General section, click the listener.
	The Listener Home page appears.
3. In the Related Links section, click Net Services Administration.
	The Net Services Administration page appears.

From the Net Services Administration page, you can administer the listeners, naming methods, preferences, and so on. The administration procedures are described in other chapters of this book.

### Using Oracle Net Manager to Configure Oracle Net Services

Oracle Net Manager enables you to configure Oracle Net Services for an Oracle home on a local client or server host.

You can use Oracle Net Manager to configure the following network components:

- Listeners: Create and configure listeners to receive client connections.
- Naming: Define [connect identifier](glossary.md) s and map them to [connect descriptor](glossary.md) s to identify the network location and identification of a service. Oracle Net Manager supports configuration of connect descriptors in local `tnsnames.ora` files or a centralized directory service.
- Naming Methods: Configure the ways connect identifiers are resolved to connect descriptors.
- Profiles: Configure preferences for enabling and configuring Oracle Net features on the client or server.

This section introduces the features of Oracle Net Manager. However, the primary documentation for using Oracle Net Manager is online Help. It contains the following topics:

- Starting Oracle Net Manager
- Navigating Oracle Net Manager
- Using Oracle Net Manager Wizards

#### Starting Oracle Net Manager

You can start Oracle Net Manager using the Oracle Enterprise Manager Console or as an independent application as follows:

- To start Oracle Net Manager from the Oracle Enterprise Manager console, select Service Management from the Tools menu, and then select Oracle Net Manager.
- To start Oracle Net Manager as standalone application, do the following:
	- On Linux, run `netmgr` from the `ORACLE_HOME/bin` directory.
		- On Microsoft Windows, select Programs from the Start menu, and then select Oracle - HOME\_NAME. Next, select Configuration and Migration Tools, and then Net Manager.

#### Navigating Oracle Net Manager

The Oracle Net Manager interface includes a toolbar and various menu options, as well as property sheets for configuring network components.

The navigator pane provides a tree view of network objects and the objects they contain, organized in folder hierarchy. You can expand and contract the folders to monitor or manage objects such as connect identifiers, listeners, and profiles. Click an object to make changes to it.

Table 7-1 lists the main folders in the navigator pane.

Table 7-1 Oracle Net Manager Navigator Pane Folders

| Folder | Description |
| --- | --- |
| Local | Displays networking elements configured in local configuration files:  - Net service names in the `tnsnames.ora` file - Listeners in the `listener.ora` file - Profile in the `sqlnet.ora` file |
| Directory | Displays connect identifiers configured in a directory server |

#### Using Oracle Net Manager Wizards

The Oracle Net Manager wizards provide step-by-step guidance for tasks. The wizards simplify complex tasks by guiding you through the tasks in manageable steps. The wizards are not intended to provide all configuration options. After you have completed a task with a wizard, use other components of Oracle Net Manager to modify the configuration.

The following topics describe the Oracle Net Manager wizards:

- Using the Net Service Name Wizard
- Using the Directory Server Migration Wizard

##### Using the Net Service Name Wizard

The Net Service Name wizard guides you through creating a basic net service name in a directory server or a `tnsnames.ora` file.

The following procedure describes how to start the Net Service Name wizard to create net service names:

1. In the navigator pane, select Directory or Local, and then select Service Naming.
2. Click the plus sign (+) on the toolbar, or select Create from the Edit menu.

See Also:

Oracle Net Manager online help for detailed information about using the Net Service Name wizard to create a net service name

##### Using the Directory Server Migration Wizard

If a `tnsnames.ora` file already exists, then its net service names can be exported to a directory server with the Directory Server Migration wizard.

The following procedure describes how to use the Directory Server Migration wizard:

1. Select Directory from the Command menu.
2. Select Export Net Service Names from the Oracle Net Manager menu.

### Deciding When to Use Oracle Enterprise Manager and Oracle Net Manager

In Oracle Database 11g, much of the functionality previously available only in Oracle Net Manager has been integrated with Oracle Enterprise Manager. Oracle Enterprise Manager provides the ability to manage configuration for multiple Oracle homes across multiple file systems. Oracle Net Manager only enables you to manage configuration for one Oracle home on a local host computer. Table 7-2 describes the key differences between the tools.

Table 7-2 Comparing Oracle Enterprise Manager and Oracle Net Manager

| User Interface Tool | Features |
| --- | --- |
| Oracle Enterprise Manager | - Configures the following features: 	\- Local naming (`tnsnames.ora` files) 	\- Directory naming 	\- Listeners - Provides Oracle home support across multiple file system - Provides the ability to search and sort local and directory naming entries - Export directory naming entries to a `tnsnames.ora` file - Performs the following administrative tasks for a selected listener: 	\- Show current status 	\- Change status 	\- Change tracing level settings 	\- Change logging settings 	\- Set connect-time failover and load balancing methods when there is more than one listener |
| Oracle Net Manager | - Configures the following features: 	\- Local naming (`tnsnames.ora` files) 	\- Directory naming 	\- Listeners 	\- Profiles - Provides Oracle home support for single host - Sets connect-time failover and load balancing methods when there is more than one listener |

Note:

When Automatic Diagnostic Repository (ADR) is enabled, any changes to the tracing and logging settings using Oracle Enterprise Manager are ignored by the system.

### Using Oracle Net Configuration Assistant to Configure Network Components

[Oracle Net Configuration Assistant](glossary.md) is provided to configure basic network components during installation, including:

- Listener names and protocol addresses
- Naming methods the client uses to resolve connect identifiers to connect descriptors
- Net service names in a `tnsnames.ora` file
- Directory server usage

Oracle Net Configuration Assistant runs automatically during software installation, as described in your Oracle installation guide. It can also be run after installation in standalone mode to configure naming methods, the listener, net service names in the `tnsnames.ora` file, and directory server usage.

To start Oracle Net Configuration Assistant do the following:

- On Linux and UNIX, run `netca` from the `ORACLE_HOME/bin` directory.
- On Microsoft Windows, select Programs from the Start menu, and then select Oracle - HOME\_NAME. Next, select Configuration and Migration Tools, and then Oracle Net Configuration Assistant.

See Also:

- Oracle Net Configuration Assistant online help
- [Oracle Grid Infrastructure Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e41961/toc.htm) for information on running Oracle Net Configuration Assistant in silent mode

Table 7-3 describes the configuration options on the Oracle Net Configuration Assistant Welcome page:

Table 7-3 Oracle Net Configuration Assistant

| Option | Description |
| --- | --- |
| Listener configuration | Create, modify, delete, or rename a listener. |
| Naming Methods configuration | Configure this computer to resolve connect identifiers to connect descriptor through one or more of following naming methods:  - Local naming - Directory naming - Easy Connect naming - External naming |
| Local Net Service Name configuration | Create, modify, delete, rename, or test connectivity of a connect descriptor stored in a local `tnsnames.ora` file. |
| Directory Usage Configuration | Configure a directory server for directory-enabled features. |

## About the OracleNetAdmins Group

To use Oracle Net Manager, you must be a member of the `OracleNetAdmins` group or the `OracleContextAdmins` group. Oracle Net Configuration Assistant establishes these access rights for these groups during Oracle Context creation.

The `OracleNetAdmins` group is owned by itself. Members of the `OracleNetAdmins` group have create, modify, and read access to Oracle Net objects and attributes. They can also add or delete members in the group, and add or delete groups to be owners of the `OracleNetAdmins` group.

The `OracleContextAdmins` group is a super-user group for Oracle Context. Members of the OracleContextAdmins group can add all supported types of entries to Oracle Context.

This section contains the following topics:

- Adding Users To the OracleNetAdmins Group
- Removing Users From the OracleNetAdmins Group
- Changing Ownership of the OracleNetAdmins Group

Note:

Members of the `OracleContextAdmins` groups can also add and delete members of the `OracleNetAdmins` group.

### Adding Users To the OracleNetAdmins Group

To add a user to the `OracleNetAdmins` group with `ldapmodify`, do the following:

1. Create an [LDIF](glossary.md) (Lightweight Directory Interchange Format) file that specifies that you want to add a user to the `OracleNetAdmins` group.
	You can use the following sample LDIF file. Use the appropriate DN for `cn=OracleNetAdmins` and the user that you want to add.
	```
	dn: cn=OracleNetAdmins,cn=OracleContext,...
	changetype: modify
	add: uniquemember
	uniquemember: DN of user being added to group
	```
2. Enter the following syntax at the command line to refresh the file:
	```
	$ ldapmodify -h directory_host
	 -p port
	 -D binddn
	 -q -f ldif_file
	```
	In the preceding command, directory\_host is the directory server host, port is the listening TCP/IP port for the directory server, binddn is the directory administrator or user DN, and ldif\_file is the input file name. If the port is not specified, then the default port of 389 is used. The `-q` option prompts for a single bind password to be entered.

### Removing Users From the OracleNetAdmins Group

To remove a user from the `OracleNetAdmins` group with `ldapmodify`, do the following:

1. Create an LDIF file that specifies that you want to delete a user to the `OracleNetAdmins` group.
	You can use the following sample LDIF file. Enter the appropriate DN for `cn=OracleNetAdmins` and the user that you want to delete.
	```
	dn: cn=OracleNetAdmins,cn=OracleContext,...
	changetype: modify
	delete: uniquemember
	uniquemember: DN of user being deleted from group
	```
2. Enter the following `ldapmodify` syntax at the command line to delete the user:
	```
	$ ldapmodify -h directory_host
	 -p port
	 -D binddn
	 -q -f ldif_file
	```
	In the preceding command, directory\_host is the directory server host, port is the listening TCP/IP port for the directory server, binddn is the directory administrator or user DN, and ldif\_file is the input file name. If the port is not specified, then the default port of 389 is used. The `-q` option prompts for a single bind password to be entered.

### Changing Ownership of the OracleNetAdmins Group

By default, the owner of the `OracleNetAdmins` group is the `OracleNetAdmins` group itself. Any member of the `OracleNetAdmins` group can add or delete other members from the `OracleNetAdmins` group. If you prefer another group to add or delete `OracleNetAdmins` members, then you can change the owner attribute of the `OracleNetAdmins` group to another group.

The owner cannot be an individual user entry but must be a group entry, and the group entry is one comprised of the LDAP schema object classes `GroupOfUniqueNames` and `orclPriviledgeGroup`.

To add a group as an owner of an `OracleNetAdmins` group, do the following:

1. Create an LDIF file, as follows:
	1. Specify the group you want to add as an owner.
		You can use the following sample LDIF file. Enter the appropriate DN for `cn=OracleNetAdmins` and the DN of the group that you want to add.
		```
		dn: cn=OracleNetAdmins,cn=OracleContext,... 
		    changetype: modify 
		    add: owner 
		    owner: DN of group to add
		```
		For example, the following LDIF syntax changes the ownership from the `OracleNetAdmins` group to another group named `cn=ExampleSecurityAdmins`. The group can be either inside or outside Oracle Context.
		```
		dn: cn=OracleNetAdmins,cn=OracleContext,... 
		     changetype: modify 
		     add: owner 
		     owner: cn=ExampleSecurityAdmins
		```
		2. Optionally, specify the group to delete as an owner.
		```
		dn: cn=OracleNetAdmins,cn=OracleContext,... 
		    changetype: modify 
		    delete: owner 
		    owner: DN of group to delete
		```
2. Enter the following syntax at the command line to refresh the file:
	```
	$ ldapmodify -h directory_host
	 -p port
	 -D binddn
	 -q -f ldif_file
	```
	In the preceding command, directory\_host is the directory server host, port is the listening TCP/IP port for the directory server, binddn is the directory administrator or user DN, and ldif\_file is the input file name. If the port is not specified, then the default port of 389 is used. The `-q` option prompts for a single bind password to be entered.

## Using Listener Control Utility to Administer the Listener

Oracle Net Services provides tools to help you start, stop, configure, and control each network component. The Listener Control utility enables you to administer the listener. The utility is started by the user that owns the Oracle installation, or a member of the designated group, and on the same machine where the listener is running. The basic syntax for this utility is as follows:

```
lsnrctl command
 [listener_name
]
```

For example, the following command starts a listener named `lsnr`:

```
lsnrctl START lsnr
```

You can also issue Listener Control utility commands at the `LSNRCTL>` program prompt. To obtain the prompt, enter `lsnrctl` with no arguments at the operating system command line. When you run `lsnrctl`, the utility is started, and you can enter the necessary commands from the program prompt.

For example:

```
lsnrctl
LSNRCTL> START lsnr
```

See Also:

- ["Customizing Oracle Net Listener Configuration"](listenercfg.md) for additional information about the listener
- [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/lsnrctl.htm#NETRF001) for additional information about the Listener Control utility

## Performing Common Network Tasks

Network configuration and administration tasks are described throughout this guide. The following tables list the common tasks, the tools associated with them, and points you to the topic in the guide that describes the task:

- Table 7-4, "Configuring Directory Server for Oracle Net Usage"
- Table 7-5, "Configuring Naming Methods"
- Table 7-6, "Migrating to Directory Naming"
- Table 7-7, "Configuring Profiles"
- Table 7-8, "Configuring Listeners"
- Table 7-9, "Administering Listeners"
- Table 7-10, "Configuring Oracle Connection Manager"

Table 7-4 shows the tasks for configuring directory server for Oracle Net.

Table 7-4 Configuring Directory Server for Oracle Net Usage

| Task | Tools to Perform Task | See Also |
| --- | --- | --- |
| Configure directory server usage. | Oracle Internet Directory Configuration Assistant | [Oracle Internet Directory Administrator's Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIDAG) |
| Add users to the `OracleNetAdmins` group. | ldapmodify | "About the OracleNetAdmins Group" |
| Authenticate with the directory. | Oracle Enterprise Manager  Oracle Net Manager | Online Help in Oracle Enterprise Manager  Choose Directory > Service Naming > How To > Change the Oracle Context in the online Help for Oracle Net Manager  [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e10744/getstrtd.htm#DBIMI236) |
| Change Oracle Context. | Oracle Net Manager | Online Help in Oracle Enterprise Manager  Choose Directory > Service Naming > How To > Set Authentication Credentials in the online Help for Oracle Net Manager |

Table 7-5 shows the tasks for configuring naming methods.

Table 7-5 Configuring Naming Methods

| Task | Tools to Perform Task | See Also |
| --- | --- | --- |
| Configure the local naming method. | Oracle Enterprise Manager  Oracle Net Manager  Oracle Net Configuration Assistant | ["Configuring the Local Naming Method"](naming.md) |
| Configure the directory naming method. | Oracle Enterprise Manager  Oracle Net Manager | ["Configuring the Directory Naming Method"](naming.md) |
| Configure the Easy Connect naming method. | Oracle Net Manager | ["Using the Easy Connect Naming Method"](naming.md) |
| Configure external naming methods. | Oracle Net Manager | ["Configuring External Naming Methods"](naming.md) |

Table 7-6 shows the tasks for migrating to directory naming.

Table 7-6 Migrating to Directory Naming

| Task | Tools to Perform Task | See Also |
| --- | --- | --- |
| Export from `tnsnames.ora` files. | Oracle Enterprise Manager  Oracle Net Manager | ["Exporting Directory Naming Entries to a tnsnames.ora File"](naming.md) |

Table 7-7 shows the tasks for configuring profiles.

Table 7-7 Configuring Profiles

| Task | Tools to Perform Task | See Also |
| --- | --- | --- |
| Prioritize naming methods. | Oracle Net Manager  Oracle Net Configuration Assistant | ["Prioritizing Naming Methods"](profile.md) |
| Configure a default domain that is automatically appended to any unqualified net service name. | Oracle Net Manager  Oracle Net Configuration Assistant | ["Specifying a Default Domain for Clients"](profile.md) |
| Route connection requests. | Oracle Net Manager  Oracle Net Configuration Assistant | ["Routing Connection Requests to a Process"](profile.md) |
| Configure access control. | Oracle Net Manager | ["Configuring Database Access Control"](profile.md) |
| Configure an [authentication method](glossary.md) available with [Oracle Advanced Security](glossary.md). | Oracle Net Manager | ["Configuring Oracle Advanced Security"](profile.md)  Choose Oracle Advanced Security > How To in the online help  [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) |
| Configure connect request timeouts. | Manual Configuration | ["Limiting Resource Consumption by Unauthorized Users"](performance.md) |

Table 7-8 shows the tasks for configuring listeners.

Table 7-8 Configuring Listeners

| Task | Tools to Perform Task | See Also |
| --- | --- | --- |
| Configure listening protocol addresses. | Oracle Enterprise Manager  Oracle Net Manager  Oracle Net Configuration Assistant | ["Configuring Listening Protocol Addresses"](listenercfg.md) |
| Configure dynamic service registration. | Automatic | ["Configuring Service Registration"](listenercfg.md) |
| Configure static service registration. | Oracle Enterprise Manager  Oracle Net Manager | ["Configuring Static Service Information"](listenercfg.md) |
| Configure password authentication. | Oracle Enterprise Manager  Oracle Net Manager | ["Configuring and Changing the Oracle Net Listener Password"](listenercfg.md) |
| Configure connect request timeouts. | Manual Configuration | ["Limiting Resource Consumption by Unauthorized Users"](performance.md) |

Table 7-9 shows the tasks for administering listeners.

Table 7-9 Administering Listeners

| Task | Tools to Perform Task | See Also |
| --- | --- | --- |
| Start and stop listeners. | Listener Control Utility | ["Starting and Stopping a Listener"](listenercfg.md) |
| View registered information. | Listener Control Utility | ["Monitoring Services of a Listener"](listenercfg.md) |

Table 7-10 shows the tasks for configuring Oracle Connection Manager.

Table 7-10 Configuring Oracle Connection Manager

| Task | Tools to Perform Task | See Also |
| --- | --- | --- |
| Configure session multiplexing. | Manual Configuration | ["Enabling Session Multiplexing"](cman.md) |
| Configure access control. | Manual Configuration | ["Enabling Access Control"](cman.md) |