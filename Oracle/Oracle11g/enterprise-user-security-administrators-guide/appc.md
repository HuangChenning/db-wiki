---
title: Integrating Enterprise User Security with Microsoft Active Directory
book: "Enterprise User Security Administrator's Guide"
doc_id: E10744-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/network.112/e10744/appc.htm
tags:
  - oracle
  - 11g
  - enterprise-user-security-administrators-guide
---

## C Integrating Enterprise User Security with Microsoft Active Directory

Enterprise users make use of Oracle Internet Directory, which is a part of the Oracle Identity Management infrastructure. If your organization uses a third party directory like Active Directory to store and manage user entries, then you can integrate it with Oracle Internet Directory to manage Enterprise User Security.

Kerberos authentication for enterprise users can make use of tickets issued by a kerberos Key Distribution Center (KDC) running on a Microsoft Windows domain controller.

This appendix lists the steps involved in integrating Enterprise User Security with Microsoft Active Directory using kerberos for authentication. It includes the following sections:

## C.1 Set Up Synchronization Between Active Directory and Oracle Internet Directory

Oracle components make use of Oracle Internet Directory for centralized security administration. Your organization might have a Microsoft Windows domain that uses Active Directory for centralized administration. You should set up synchronization between Oracle Internet Directory and Active Directory before you configure Enterprise User Security to work with Active Directory.

Synchronization profiles are used to synchronize the two directories. The profile contains configuration information required to synchronize the two directories. This includes direction of synchronization, mapping rules and formats, connection details of Microsoft Windows domain and the like. Mapping rules contain domain rules and attribute rules to map a domain and attributes in one directory to the other directory, optionally formatting the attributes.

See Also:

For step-by-step instructions on integrating Oracle Internet Directory with Microsoft Active Directory, refer to the [Oracle Identity Management Integration Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIMIG026)

## C.2 Set Up a Windows 2000 Domain Controller to Interoperate with Oracle Client

The following tasks must be performed on the Windows 2000 domain controller:

1. Create the Oracle Database Principal in Microsoft Active Directory
	This creates a new user for the database in Microsoft Active Directory.
2. Use the `ktpass` command-line utility to create a kerberos `keytab` file
	The `ktpass` utility is a part of the Windows 2000 Support Tools. The `keytab` file is required to use a Windows 2000 domain controller as a KDC.
3. Copy the `keytab` file created in the previous step to the computer on which the database server is installed

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asokerb.htm#ASOAG060) for a detailed listing of the preceding steps.

## C.3 Set Up Oracle Database to Interoperate with a Windows 2000 Domain Controller

The following task must be performed on the host computer where Oracle Database is installed:

- Update the `sqlnet.ora` file in the database with kerberos parameters

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asokerb.htm#ASOAG060) for a detailed description of the preceding step.

## C.4 Set Up Oracle Database Client to Interoperate with a Windows 2000 KDC

The following steps must be performed on the Oracle kerberos client:

1. Create client kerberos configuration files
	The client kerberos configuration files refer to the Windows 2000 domain controller as the kerberos KDC.
2. Specify kerberos parameters in the client `sqlnet.ora` file
	You can either manually update the file or use Oracle Net Manager utility.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asokerb.htm#ASOAG060) for a detailed listing of the preceding steps.

## C.5 Obtain an Initial Ticket for the Client

Before a client can connect to the database, the client must request for an initial ticket. The initial ticket identifies the client as having the rights to ask for additional service tickets. An initial ticket is requested using the `okinit` command.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asokerb.htm#ASOAG060) for more details on requesting an initial ticket with `okinit`.

## C.6 Configure Enterprise User Security for Kerberos Authentication

To configure Enterprise User Security for Kerberos Authentication, use the following steps:

1. Register the database in Oracle Internet Directory
	You can use Database Configuration Assistant for registering the database.
2. Configure Enterprise User Security Objects in the database and Oracle Internet Directory
	Create global schemas and global roles in the database. Also create enterprise roles in the enterprise domain. Configure user schema mappings for the enterprise domain, add global database roles to enterprise roles and grant enterprise roles to enterprise users for database access.
3. Configure the enterprise domain to accept kerberos authentication
	Use Oracle Enterprise Manager to enable kerberos authentication for your enterprise domain.
4. Connect as kerberos authenticated enterprise user.
	Launch SQL\*Plus and use the command, `connect /@` `net_service_name` to connect as a kerberos authenticated enterprise user.

See Also:

For detailed information on the preceding steps, refer to ["Configuring Enterprise User Security for Kerberos Authentication"](configur.md).