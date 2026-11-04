---
title: INS-35001 to INS-40000
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/dbinstaller_errormessages.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 123 INS-35001 to INS-40000

INS-35011: E-mail address cannot be empty.

Cause: E-mail address for database management using e-mail notifications was empty.

Action: Specify an e-mail address for notification functions.

INS-35012: Outgoing main (SMTP) server cannot be empty.

Cause: The value for the outgoing main (SMTP) server is empty. You must provide a SMTP server to enable database management with e-mail notifications.

Action: Specify an outgoing main (SMTP) server for e-mail notifications.

INS-35013: Check e-mail address.

Cause: Either the e-mail address provided contains invalid characters, or it does not follow the standard e-mail address format.

Action: Specify an e-mail address that is consistent with RFC 2822 and RFC 2821 format.

INS-35014: Outgoing mail (SMTP) server is invalid.

Cause: The provided outgoing mail (SMTP) server was not valid. You must specify a valid SMTP server to enable database management with e-mail notifications.

Action: Specify an outgoing mail (SMTP) server for e-mail notifications.

INS-35015: Recovery location cannot be empty.

Cause: The database recovery backup location was empty.

Action: Specify a path for the database recovery backup location.

INS-35016: User name cannot be empty.

Cause: The database recovery user name text field was empty.

Action: Provide the user name permitted to perform database recovery.

INS-35017: Password cannot be empty.

Cause: The database recovery password was empty.

Action: Enter a password for database recovery.

INS-35019: Invalid value specified for Management Service field.

Cause: The installer was unable to detect an agent home corresponding to the URL in the Management Service field.

Action: Specify a valid URL for Management Service field that has a corresponding agent configured on the host.

INS-35020: Invalid value specified for Management Service field.

Cause: No value specified for Management Service field.

Action: Specify a valid Management service URL.

INS-35021: Backup and recovery location is on a file system that is not shared across the cluster.

Cause: The database backup and recovery area is not located on a shared file system.

Action: Enter a backup and recovery area that is located on a shared file system.

INS-35022: The location string you selected is on an Oracle ASM Cluster File System (ACFS).

Cause: Installer has detected that the active version of Grid Infrastructure is prior to version 12.1. Hence, you cannot use ACFS that is configured on Grid Infrastructure prior to version 12.1, as storage for backup and recovery files.

Action: Specify an ASM diskgroup, or any other supported shared storage location, or location on ACFS that is configured on Grid Infrastructure whose version is 12.1 or above.

INS-35071: Global database name cannot be left blank.

Cause: The Global database name was left blank.

Action: Specify a value for the Global database name.

INS-35072: The SID cannot be left blank.

Cause: The Oracle system identifier (SID) was left blank.

Action: Specify a value for Oracle system identifier (SID).

INS-35073: Invalid global database name.

Cause: The value given for the name portion of Global database name exceeds 30 characters. The maximum length is 30 characters.

Action: Enter a legal Global database name not exceeding 30 characters.

INS-35074: The specified SID is already in use.

Cause: The specified SID was already registered in the oratab file (string) on the server. The oratab file is used by Oracle products to detect existing database instances.

Action: Specify a unique Oracle system identifier (SID).

INS-35075: The specified SID is already in use.

Cause: The Oracle system identifier (SID) given was already in use.

Action: Specify a unique Oracle system identifier (SID).

INS-35076: The specified SID exceeds the number of characters allowed.

Cause: The length of the Oracle system identifier (SID) on Linux and UNIX platforms either exceeded 12 characters for single-instance installations or 8 characters for Oracle RAC installations.

Action: Specify an Oracle system identifier (SID) shorter than 12 characters for single-instance installation or 8 characters for Oracle RAC installation.

INS-35077: The specified SID exceeds the number of characters allowed.

Cause: The length of the Oracle system identifier (SID) on Windows platforms either exceeded string characters for single-instance installations or string characters for Oracle RAC installations.

Action: Specify a Windows Oracle system identifier (SID) shorter than string characters for a single-instance installation or string characters for an Oracle RAC installation.

INS-35081: The ORACLE\_HOME environment variable is currently set.

Cause: The ORACLE\_HOME environment variable was already set. This prevents proper use of multiple Oracle homes and, as it is not required for any Oracle products to function, it will be unset in your environment.

Action: The ORACLE\_HOME environment variable will be unset automatically.

INS-35082: Global database name did not begin with an alphabetic character.

Cause: The global database name began with a character that was not an alphabetic character.

Action: Specify a global database name that begins with an alphabetic character.

INS-35083: The specified domain of the Global database name exceeds 128 characters.

Cause: The domain portion entered for Global database name exceeded 128 characters.

Action: Specify a domain for the Global database name that is less than 128 characters in length.

INS-35084: The specified global database name contains invalid characters.

Cause: The specified domain portion of the global database name contained invalid characters.

Action: Specify a global database name that contains only alphanumeric, underscore (\_), pound (#) and period (.) characters.

INS-35085: Invalid value specified for string.

Cause: The string derived from string contains one or more invalid characters.

Action: Remove the invalid characters (string) from the string or select Advanced install flow to be able to specify different string

INS-35086: Invalid value specified for Global Database Name.

Cause: Database name cannot be empty.

Action: Enter a legal Global Database Name not exceeding 30 characters.

INS-35087: Invalid value specified for SID

Cause: The system identifier (SID) that you entered begins with a non-alphabetic character.

Action: Enter a SID that begins with an alphabetic character.

INS-35088: The specified Global database name exceeds string characters.

Cause: The name and domain portion entered for Global database name exceeded string characters.

Action: Specify the Global database name that is less than string characters in length.

INS-35089: The specified domain of the Global database name exceeds string characters.

Cause: The domain portion entered for Global database name exceeded string characters.

Action: Specify a domain for the Global database name that is less than string characters in length.

INS-35090: The service name provided for RAC One is empty.

Cause: The service name provided for RAC One is empty.

Action: Provide a value for the RAC One service name.

INS-35091: The service name provided for RAC One did not begin with an alphabetic character.

Cause: The service name provided for RAC One began with a character that was not an alphabetic character.

Action: Provide a service name which begins with an alphabetic character.

INS-35092: The service name provided for RAC One cannot be the same as the global database name.

Cause: The service name provided for RAC One cannot be the same as the global database name.

Action: Provide a service name that is different from the global database name.

INS-350923: Invalid value provided for the RAC One service name.

Cause: The service name provided for RAC One may contain invalid characters.

Action: Provide a service name that consists of alphanumeric or underscore (\_) characters.

INS-350924: Invalid value provided for Oracle RAC One service name.

Cause: The domain portion in the Oracle RAC One service name may contain invalid characters.

Action: Provide a service name whose network domain consists of alphanumeric characters or \_ or $ or #.

INS-350925: The specified domain of the Oracle RAC One service name exceeds 128 characters.

Cause: The domain portion entered for Oracle RAC One service name exceeded 128 characters.

Action: Specify a domain for the Oracle RAC One service name that is less than 128 characters in length.

INS-35171: Target database memory (stringMB) exceeds at least one of the selected nodes available shared memory (string MB).

Cause: The total available shared memory on at least one of the selected nodes (string MB) was less than the chosen target database memory (string MB).

Action: Enter a value for the target database memory less than string MB.

INS-35172: Target database memory (stringMB) exceeds the systems available shared memory ({0}MB).

Cause: The total available shared memory on the system (string MB) was less than the chosen target database memory (string MB).

Action: Enter a value for target database memory that is less thanstring MB.

INS-35173: Invalid value for allocated memory.

Cause: The allocated memory specified was greater than or equal to the total memory available on the system.

Action: Enter a value less than the total available memory on the system for target database memory.

INS-35174: A minimum of stringMB (string% of total physical memory) is required.

Cause: Allocated memory was less than the required memory.

Action: Enter a memory value larger than string MB.

INS-35175: No value given for the allocated memory of the database.

Cause: A value was not specified for the allocated memory of the database.

Action: Specify a value for the allocated memory of the database. This corresponds to the oracle.install.db.config.starterdb.memoryLimit variable in the response file.

INS-35176: Invalid value for allocated memory.

Cause: The allocated memory specified was greater than 3GB.

Action: Enter a value less than 3GB for target database memory.

INS-35205: Specified data file storage location is invalid.

Cause: The data file storage location for Oracle Real Application Clusters was not on a shared file system.

Action: Specify a location on a shared file system to place the data files.

INS-35206: Directory is already in use.

Cause: The specified directory for the database files was already in use by the Global database name that was provided.

Action: Either change the location or go to the previous screen and change the Global database name.

INS-35207: The location string you selected is on an Oracle ASM Cluster File System (ACFS).

Cause: Oracle does not recommend placing Oracle Database files on ACFS. Oracle recommends that you place database files directly on the underlying Oracle ASM disk groups, as this provides optimal database performance.

Action: Specify a location that is not on ACFS.

INS-35208: The location string you selected is on an Oracle ASM Cluster File System (ACFS).

Cause: Installer has detected that the active version of Grid Infrastructure is prior to version 12.1. Hence, you cannot use ACFS that is configured on Grid Infrastructure prior to version 12.1, as shared storage for Oracle RAC.

Action: Specify an ASM diskgroup, or any other supported shared storage location, or location on ACFS that is configured on Grid Infrastructure whose version is 12.1 or above.

INS-35209: Selected storage type is not valid

Cause: You cannot use file system storage with Standard Edition Oracle Real Application Clusters databases.

Action: Choose Oracle Automatic Storage Management for database storage.

INS-35210: Installing a database with storage on Oracle Automatic Storage Management (Oracle ASM) is not supported on this system.

Cause: Oracle Database 11g Release 2 and later supports Oracle ASM only on 64-bit Windows operating systems.

INS-35255: Invalid password.

Cause: One of the Database Administrative account password was either CHANGE\_ON\_INSTALL or MANAGER or DBSNMP or SYSMAN.

Action: Enter a password that is not a former default password for these administrative users, such as CHANGE\_ON\_INSTALL, MANAGER, DBSNMP or SYSMAN.

INS-35256: The password for account string is not allowed to be string.

Cause: The administrative account password you entered was string which is not allowed for string user.

Action: Enter a password that is not a former default password for the string administrative user account.

INS-35341: The installation user is not a member of the following groups: string

Cause: The installation user account must be a member of all groups required for installation.

Action: Ensure that the installation user is a member of the system privileges operating system groups you selected.

INS-35342: The specified group for Database Operator (OSOPER) may not be defined in the system.

Cause: The OS group you specified as the OSOPER group may not be configured on the server, or in the Network Information Service (NIS).

Action: Check the group name you selected, and specify a different group, or create the group on the server or in the Network Information Service.

INS-35351: Inconsistent versions detected.

Cause: The active version of Oracle Clusterware detected on the system(string) was lower than the version of Oracle Database that you were attempting to install(string). This is not supported.

Action: Upgrade Oracle Clusterware to version string or later.

INS-35352: There are no disk groups selected for storage and backup.

Cause: There were no disk groups selected for storage and backup.

Action: Select at least one disk group for storage and backup.

INS-35354: The system on which you are attempting to install Oracle RAC is not part of a valid cluster.

Cause: Before you can install Oracle RAC, you must install Oracle Grid Infrastructure on all servers (Oracle Clusterware and Oracle ASM) to create a cluster.

Action: Oracle Grid Infrastructure is not installed. Install it either from the separate installation media included in your media pack, or install it by downloading it from Electronic Product Delivery (EPD) or the Oracle Technology Network (OTN). Oracle Grid Infrastructure normally is installed by a different operating system user than the one used for Oracle Database. It may need to be installed by your system administrator. See the installation guide for more details.

INS-35355: The node string specified in response file is not part of the Oracle Clusterware detected.

Cause: The node list for the Oracle RAC database specified in the response file does not match the configuration stored in the OCR.

Action: Please specify a valid node or add this node string to the cluster.

INS-35356: Oracle recommends that you install the database on all nodes that are part of the Oracle Grid Infrastructure cluster.

Cause: All Oracle Grid Infrastructure nodes were not selected for installing Oracle RAC.

Action: Oracle recommends that you deploy Oracle Real Application Clusters across all Oracle Grid Infrastructure cluster nodes.

INS-35357: Oracle RAC is not supported on this system.

Cause: Oracle Database 11g Release 2 and later supports Oracle RAC only on 64-bit Windows operating systems.

Action: Choose the option to install a single instance database on this system.

INS-35358: Oracle RAC is not supported on this system.

Cause: Oracle Database 11g Release 2 and later supports Oracle RAC only on 64-bit Windows operating systems.

Action: Migrate your existing Oracle RAC installation to a 64-bit Windows platform before upgrading it.

INS-35359: Only one node is selected for database creation.

Cause: Only one node is selected for database creation. To protect a database against node or instance failure, at least two nodes should be selected.

Action: Provide at least two nodes for database creation.

INS-35360: No nodes are specified for RAC One Node install.

Cause: No nodes are specified for RAC One Node install.

Action: Specify the nodes on which RAC One Node install has to be done.

INS-35361: One or more selected nodes that are part of the cluster are down.

Cause: One or more selected nodes that are part of the cluster cannot be reached

Action: Ensure that all the selected nodes are reachable.

INS-35371: Oracle RAC databases not detected.

Cause: The installer could not detect any Oracle Real Application Clusters databases that could be upgraded.

Action: None

INS-35372: Oracle RAC databases not detected.

Cause: The installer could not detect any Oracle Real Application Clusters databases that could be upgraded on the selected nodes.

Action: None

INS-35373: Single-instance database not detected

Cause: The installer could not detect a single-instance database that could be upgraded.

Action: None

INS-35375: The installer detects an older version of Oracle ASM on the system. If you intend to upgrade a database using Oracle ASM for storage, then you must first upgrade Oracle ASM. Refer to Oracle Grid Infrastructure Installation Guide for further information.

Cause: An earlier release version of Oracle Automatic Storage Management (Oracle ASM) is detected on the server.

Action: To upgrade Oracle ASM, refer to installation guides for information about Oracle Grid Infrastructure upgrade.

INS-35376: Passsword cannot be empty for the ASMSNMP user.

Cause: The ASMSNMP user password was not specified.

Action: Provide a password for the ASMSNMP user in the password field.

INS-35377: An earlier release version of Oracle Automatic Storage Management (Oracle ASM) exists on this system. If you intend to upgrade an earlier release database that uses Oracle ASM to Oracle Database 11g Release 2, then the upgrade will fail on 32-bit systems.

Cause: Oracle Database 11g Release 2 and later supports Oracle ASM only on 64-bit Windows operating systems.

Action: Migrate database storage from Oracle ASM to a file system before upgrading, or migrate earlier release databases versions that use Oracle ASM storage to 64-bit Windows systems. See the upgrade guide for additional information.

INS-35378: The installer has detected that the configured Oracle Restart software is a release version earlier than the database release you want to install. Oracle Restart must be the same release or a later release than Oracle Database.

Cause: The active Oracle Restart release detected on the system (string) is an earlier release than the Oracle Database release to which you want to upgrade (string).

Action: Upgrade Oracle Restart software to version string or later.

INS-35379: The installer has detected that configured Oracle Restart software is not upgraded to current install version.

Cause: The active version of Oracle Restart detected on the system (string) is earlier than the version of Oracle Database that you are attempting to upgrade to (string).

Action: Upgrade Oracle Restart software to version string or later.

INS-35421: This option installs a single-instance database only.

Cause: You have chosen to perform a Desktop class install on a cluster. This option will not install Oracle RAC.

Action: If you want to install Oracle RAC, then choose to perform a Server class install.

INS-35422: The installer has detected that configured Oracle Restart software is not upgraded to current install version. This database installation does not register the database with lower version of High Availability service.

Cause: The active version of Oracle Restart detected on the system(string) is lower than the version of Oracle Database that you are attempting to install to (string).

Action: Upgrade Oracle Restart software to version string or later.

INS-35423: The installer has detected that Oracle Clusterware is not running on local node.

Cause: You have chosen to install Oracle RAC when Oracle Clusterware stack is not running on the local node.

Action: Start the Oracle Clusterware stack by running the following command as the root user from the Oracle Clusterware home (Grid home): /bin/crsctl start crs. When the Oracle Clusterware stack is running, restart the installer and continue with the Oracle RAC installation.

INS-35431: Invalid Location Specified for Oracle home.

Cause: The installer detects that the location you specified for the Oracle home is under an Oracle ASM Cluster File System (ACFS) mount point that is not registered with Oracle Grid Infrastructure on this server.

Action: Oracle Database homes can only be placed on ACFS locations registered with Oracle Grid Infrastructure software. Specify a different location for the Oracle home, or register this location with Oracle Grid Infrastructure software.

INS-35432: The installer has detected that the software location you have specified contains Oracle Database software version string. Oracle recommends that when upgrading to string, you perform an installation of the software into a new Oracle home and then upgrade the database using the new software binaries.

Cause: The installer has detected that the software location you have specified contains Oracle Database software version string.

Action: Perform an out-of-place upgrade. Out-of-place upgrades allow you to perform the upgrade with less downtime and more stability, due to the non-destructive nature of the software installation. You can perform the upgrade and maintain the existing Oracle home location by taking a backup of the prior release Oracle home before upgrading, and moving the prior release binaries to a different location before installing the new binaries into the existing Oracle home location. Refer to the documentation for a precise set of steps to follow in this case.

INS-35433: The installer has detected that the specified location string is on an Oracle ASM Cluster File System that is not registered as a resource in Oracle Grid Infrastructure.

Cause: The specified location string is on an Oracle ASM Cluster File System that is not registered as a resource in Oracle Grid Infrastructure.

Action: Register the Oracle ASM Cluster File System location that you want to use with Oracle Grid Infrastructure.

INS-35461: Standard Edition One (SE One) not supported for this installation.

Cause: Standard Edition One (SE One) is not supported for Oracle Real Application Clusters database installation.

Action: Select a different Install Edition.

INS-35462: Personal Edition not supported for this installation.

Cause: You selected an Install Edition that is not supported for UNIX or Linux operating systems, and for Oracle RAC installations.

Action: Select a different Install Edition.