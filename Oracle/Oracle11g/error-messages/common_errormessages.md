---
title: INS-30001 to INS-35000
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/common_errormessages.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 122 INS-30001 to INS-35000

INS-30001: The string password is empty.

Cause: The string password should not be empty.

Action: Provide a non-empty password.

INS-30002: The string password and string confirm password are not same.

Cause: The string password and string confirm password should be the same.

Action: Ensure that string password and string confirm password are the same.

INS-30003: The string password length is too long.

Cause: The string password length cannot exceed string characters.

Action: Provide a password lesser than string characters.

INS-30004: The string password entered is invalid.

Cause: Passwords may contain only alphanumeric characters from the chosen database character set, underscore (\_), dollar sign ($), or pound sign (#).

Action: Provide a password as per recommendations.

INS-30005: The string password entered is missing recommended characters.

Cause: The string password entered is missing recommended characters. Oracle recommends that passwords contain at least one string.

Action: Provide a password which contains at least one string.

INS-30006: The password specified is too short.

Cause: Oracle recommends that the string password entered should be at least string characters in length.

Action: Provide a password which is at least string characters in length.

INS-30007: Unable to get the raw device partition size.

Cause: Unexpected error occurred while trying to get the raw device partition size.

Action: Refer to the logs for more details.

INS-30008: Refer to the logs for more details.

Cause: Unexpected error occurred while trying to get the FS device partition size.

Action: Refer to the logs for more details.

INS-30009: Unable to get the FS partition free space size

Cause: Unable to get the FS partition free space size

Action: Unable to get the FS partition free space size

INS-30010: Unable to get the file system type.

Cause: Unexpected error occurred while trying to get the file system type.

Action: Refer to the logs for more details.

INS-30011: The string password entered does not conform to the Oracle recommended standards.

Cause: Oracle recommends that the password entered should be at least string characters in length, contain at least 1 uppercase character, 1 lower case character and 1 digit \[0-9\].

Action: Provide a password that conforms to the Oracle recommended standards.

INS-30013: Unable to check whether the partition is raw.

Cause: Unexpected error occurred while trying to check whether the partition is raw.

Action: Refer to the logs for more details.

INS-30014: Unable to check whether the location specified is on CFS

Cause: The location specified might not have the required permissions.

Action: Provide a location which has the appropriate required permissions.

INS-30015: An error occurred during setting permission.

Cause: Unexpected error occurred during setting permission.

Action: Refer to the logs for more details.

INS-30016: Unable to load the install inventory.

Cause: Unable to lock or read the install inventory.

Action: Check the permissions on the inventory location.

INS-30017: Install inventory does not exist.

Cause: Install inventory does not exist.

Action: Ensure that the install inventory exists.

INS-30018: Unable to get all the previously installed Oracle Home locations.

Cause: Error occurred while retrieving the oracle home locations.

Action: Check if the existing inventory location is accessible.

INS-30020: Unable to get the default oradata location.

Cause: Unexpected error occurred while trying to get the default oradata location.

Action: Refer to the logs for more details.

INS-30021: Unable to get Oracle RAC databases info.

Cause: Unexpected error occurred while trying to get RAC databases info.

Action: Refer to the logs for more details.

INS-30022: Unable to get SIDs and DB Homes on remote nodes.

Cause: Unexpected error occurred while trying to get SIDs and DB Homes on remote nodes.

Action: Refer to the logs for more details.

INS-30023: Unable to get SIDs and DB Homes on node string.

Cause: Unexpected error occurred while trying to get SIDs and DB Homes on node string.

Action: Refer to the logs for more details.

INS-30042: IO Exception occurred.

Cause: IO Exception occurred.

Action: Refer to the logs for more details.

INS-30043: The Grid Infrastructure home string does not exist or is empty.

Cause: Installer has detected Grid Infrastructure home (string) registered in the Inventory. But the home location does not exist or is empty.

Action: Check if the location specified is a valid Grid Infrastructure home. If not unregister the home from inventory using deinstall procedures.

INS-30044: Create Install Session Exception.

Cause: Refer to the logs for more details.

Action: Refer to the logs for more details.

INS-30045: Unable to find the specified Oracle Home.

Cause: Refer to the logs for more details.

Action: Refer to the logs for more details.

INS-30046: Unable to find product in Oracle Inventory.

Cause: Refer to the logs for more details.

Action: Refer to the logs for more details.

INS-30047: Multiple versions of the product were found.

Cause: Refer to the logs for more details.

Action: Refer to the logs for more details.

INS-30048: Incorrect format used in the given cluster configuration file.

Cause: The content of cluster configuration file do not conform to the format recommended.

Action: Ensure that the contents of the cluster configuration file conform to the expected format.

INS-30049: The given cluster configuration file could not be read.

Cause: Unexpected error while reading the given cluster configuration file.

Action: Ensure that the given cluster configuration file exists and has the read permissions.

INS-30051: Failed while checking for string directory existence on remote node (string) using SRVM API.

Cause: User equivalence may not be setup between the local node and the remote nodes or sufficient file permissions are not set.

Action: Setup user equivalence or ensure sufficient file permissions are set.

INS-30052: Check for free disk space across nodes failed.

Cause: Unexpected error occurred while trying to check free disk space across nodes.

Action: Refer to the logs or contact Oracle Support Services. Note for advanced users: Launch the installer by passing the following flag '-ignoreInternalDriverError'.

INS-30053: Check for shared partitions across nodes failed.

Cause: Unexpected error occurred while trying to get shared partitions across nodes.

Action: Refer to the logs or contact Oracle Support Services. Note for advanced users: Launch the installer by passing the following flag '-ignoreInternalDriverError'.

INS-30054: Check for file system type across nodes failed.

Cause: Unexpected error while detecting file system type across nodes.

Action: Refer to the logs or contact Oracle Support Services.

INS-30060: Check for group existence failed.

Cause: Unexpected error occurred while trying to check for group existence.

Action: Refer to the logs or contact Oracle Support Services. Note for advanced users: Launch the installer by passing the following flag '-ignoreInternalDriverError'.

INS-30070: There are processes running in the currently selected Oracle Home.

Cause: Software is already running from the home selected for the install.

Action: Shutdown the following processes before continuing: string

INS-30071: An error occured while trying to determine the running processes or services.

Cause: A runtime error

Action: Refer to the logs or contact Oracle Support Services.

INS-30072: There are services running from the currently selected Oracle Home.

Cause: Files that need to be reinstalled or upgraded in this home are currently in use by running services.

Action: Please stop the following services before continuing: string

INS-30073: There is software running from the currently selected Oracle Home.

Cause: Files that need to be reinstalled or upgraded in this home are currently in use by one or more applications.

Action: Please close any running applications before continuing.

INS-30080: string did not resolve to an IP address. Provide alternative name that resolves to an IP address.

Cause: n/a

Action: n/a

INS-30081: string could not be resolved using TCP/IP host name lookup. Provide valid name that can be resolvable using TCP/IP host name lookup.

Cause: n/a

Action: n/a

INS-30090: Check for connectivity across all nodes through the interface string has failed.

Cause: Unexpected error while checking connectivity of nodes through the interface.

Action: Refer to the logs or contact Oracle Support Services.

INS-30100: Insufficient disk space on the selected location (string).

Cause: Specified location is on a volume without enough disk space on nodes: string.

Action: Choose a location that has enough space (minimum of stringMB) or free up space on the existing volume.

INS-30110: Installer has failed to perform status check on Oracle Clusterware configured.

Cause: Unexpected error occurred while trying to perform status check on existing Oracle Clusterware.

Action: Refer to the logs or contact Oracle Support Services. Note for advanced users: Launch the installer by passing the following flag '-ignoreInternalDriverError'.

INS-30120: Specified file (string) doesnt exist.

Cause: n/a

Action: n/a

INS-30131: Initial setup required for the execution of installer validations failed.

Cause: Failed to access the temporary location.

Action: Ensure that the current user has required permissions to access the temporary location.

INS-30132: Initial setup required for the execution of installer validations failed on nodes: string

Cause: Indicated nodes were not reachable or failed to access the temporary location on the indicated nodes.

Action: Ensure that all the indicated nodes are reachable and current user has required permissions to access the temporary location on all the indicated nodes.

INS-30140: n/a

Cause: n/a

Action: n/a

INS-30141: n/a

Cause: n/a

Action: n/a

INS-30501: Automatic Storage Management software is not configured on this system.

Cause: Prior to configuring a database to use Automatic Storage Management (ASM), you must install and configure Grid Infrastructure, which includes ASM software.

Action: Grid Infrastructure can be installed from the separate installation media included in your media pack. Alternatively, it can be downloaded separately from Electronic Product Delivery (EPD) or the Oracle Technology Network (OTN). This is typically installed as a separate operating system user than the Oracle database and may have been installed by your system administrator. See the installation guide for more details.

INS-30502: No ASM disk group found.

Cause: There were no disk groups managed by the ASM instance string.

Action: Use Automatic Storage Management Configuration Assistant to add disk groups.

INS-30503: Unknown ASM disk group.

Cause: There was no disk groups named string managed by ASM instance string

Action: Enter a valid existing ASM disk group or use Automatic Storage Management Configuration Assistant to add the desired ASM disk group.

INS-30504: Missing ASM disk group name.

Cause: ASM disk group name was not entered in the text field.

Action: Enter a valid ASM disk group name.

INS-30505: Invalid disk group name.

Cause: A disk group name specified was invalid. It must start with an alphabetic character, and consist of up to 30 characters which are alphabetic, numeric, or the characters $,# and \_.

Action: Enter a valid disk group name containing only alphanumeric characters and possibly a few special characters allowed by your platform.

INS-30506: Invalid redundancy level.

Cause: Redundancy level was invalid.

Action: Choose and complete a valid redundancy level: Normal or External.

INS-30507: Empty ASM disk group.

Cause: No disks were selected from a managed ASM disk group.

Action: Select appropriate number of disks from a managed ASM disk group.

INS-30508: Invalid ASM disks.

Cause: The disks string were not valid.

Action: Please choose or enter valid ASM disks.

INS-30509: Insufficient space available in the selected disk group.

Cause: Insufficient space available in the selected disk group. At least, string MB of space is required.

Action: Use Automatic Storage Management Configuration Assistant to add more disks to the selected disk group or create a new disk group with as least string MB of space.

INS-30510: Insufficient number of ASM disks selected.

Cause: The number of disks selected were insufficient for the selected redundancy level.

Action: For a disk group with redundancy level 'string', at least 'string' disks are recommended.

INS-30511: An older ASM instance was found.

Cause: Automatic Storage Management (ASM) string instance is found.

Action: Upgrade the existing ASM instance to version string.

INS-30512: Automatic Storage Management software is not configured on this cluster.

Cause: Prior to configuring a cluster database to use Automatic Storage Management (ASM), you must configure ASM software in the Grid Infrastructure home.

Action: Grid Infrastructure installation on this cluster was only configured to run Oracle Clusterware. You will need to go back to the Grid Infrastructure home and configure ASM for storing database. Grid Infrastructure is typically installed as a separate operating system user than the Oracle database and may have been installed by your system administrator. See the installation guide for more details.

INS-30513: ASM not running on one or more nodes in the cluster.

Cause: The following nodes did not have an ASM instance running on them. Node list: string

Action: Before creating a database that uses ASM on all of the nodes chosen for this installation, you should extend the ASM cluster of instances using the Add Instance procedure to the desired set of nodes. Node list: string

INS-30514: The ASM diskgroup name has exceeded string characters.

Cause: The ASM diskgroup name has exceeded string characters.

Action: Specify diskgroupname lesser than string characters.

INS-30515: Insufficient space available in the selected disks.

Cause: Insufficient space available in the selected Disks. At least, string MB of free space is required.

Action: Choose additional disks such that the total size should be at least string MB.

INS-30516: Please specify unique disk groups.

Cause: Installer has detected that the diskgroup name provided already exists on the system.

Action: Specify different disk group.

INS-30517: Automatic Storage Management software is not configured on this system.

Cause: n/a

Action: n/a

INS-30518: Invalid Disk Discovery Path specified.

Cause: The Disk Discovery Path specified is invalid. Disk Discovery Path must not contain $, \\\\ or? characters.

Action: Ensure Disk Discovery Path provided does not contain $, \\\\ or? characters.

INS-30519: Allocation unit size can only be one of the following value set string.

Cause: The allocation unit size (AU Size) is set to an invalid number.

Action: Set the allocation unit size be one of the following value set string.

INS-30520: Incorrect Disk Group name specified.

Cause: The Disk Group name specified is incorrect. Disk Group name cannot be a SQL reserved word.

Action: Enter a Disk Group name that is not a SQL reserved word.

INS-30601: File access permissions error encountered.

Cause: File access permissions error encountered.

Action: Ensure proper file access permissions are granted.

INS-30602: ASM access denied.

Cause: A connection to the Automatic Storage Management (ASM) instance on this system could not be established.

Action: To ensure a proper connection, the operating system user performing this installation must be a member of the OSDBA group of the ASM instance. See the installation guide for more information on the proper system setup required for running ASM and database instances as separate operating system users. Refer to Oracle error description for ORA-01031 for additional details.

INS-30603: CRS is not running on local node.

Cause: Cluster Ready Services (CRS) on the local node was not running.

Action: Perform a CRS, Grid Infrastructure, installation and configuration.

INS-30604: Required drivers are not found to perform the operation.

Cause: Required drivers were not found to perform the operation.

Action: Ensure that all required drivers were installed.

INS-30605: ASM instance seems to be down.

Cause: ASM instance was down.

Action: Bring up ASM in order to proceed.

INS-30606: Partially cleaned ASM home is found.

Cause: Directories or files or both were missing.

Action: Clean up ASM home and reinstall ASM.

INS-30607: No ASM found on the box.

Cause: n/a

Action: n/a

INS-30701: The partition is invalid.

Cause: The partition provided was not available on the system.

Action: Provide a partition that is available on the system.

INS-32001: No value has been given for the Password field.

Cause: A value was not specified for the Password field.

Action: Choose a nonempty password.

INS-32002: Invalid password.

Cause: The password entered in the Confirm Password field did not match the password entered in the Password field.

Action: Enter the same password in both Password and Confirm Password fields for confirmation purposes.

INS-32008: Oracle base location cant be same as the user home directory.

Cause: The specified Oracle base is same as the user home directory.

Action: Provide an Oracle base location other than the user home directory.

INS-32010: String contains invalid characters.

Cause: The specified string contained one or more invalid characters.

Action: Choose a string containing only alphanumeric characters and a few additional characters that are allowed for your platform.

INS-32011: The string that you have specified contains the space character.

Cause: The string you entered contains the space character.

Action: Please choose a string containing only alphanumeric, and a few additional characters that are allowed for your platform.

INS-32012: Unable to create directory: string.

Cause: Either proper permissions were not granted to create the directory or there was no space left in the volume.

Action: Check your permission on the selected directory or choose another directory.

INS-32013: The string location is empty.

Cause: The string location was empty.

Action: Specify a path for string location.

INS-32015: The location specified for string is invalid.

Cause: The specified location cannot be used for string. Either the specified location is not found on the system or is detected to be a file.

Action: Specify a valid location for string.

INS-32016: The selected Oracle home contains directories or files.

Cause: The selected Oracle home contained directories or files.

Action: To start with an empty Oracle home, either remove its contents or choose another location.

INS-32017: Invalid path specified for string

Cause: Path specified for string contains one or more folders which exceeds maximum folder name length.

Action: Specify the location which contains folders name length not more than string characters.

INS-32018: The selected Oracle home is outside of Oracle base.

Cause: The Oracle home selected was outside of Oracle base.

Action: Oracle recommends installing Oracle software within the Oracle base directory. Adjust the Oracle home or Oracle base accordingly.

INS-32021: Insufficient disk space on this volume for the selected Oracle home.

Cause: The selected Oracle home was on a volume without enough disk space.

Action: Choose a location for Oracle home that has enough space (minimum of stringMB) or free up space on the existing volume.

INS-32022: Grid infrastructure software for a cluster installations must not be under an Oracle base directory.

Cause: Grid infrastructure for a cluster installations assign root ownership to all parent directories of the Grid home location. As a result, ownership of all named directories in the software location path are changed to root, creating permissions errors for all subsequent installations into the same Oracle base.

Action: Specify software location outside of an Oracle base directory for grid infrastructure for a cluster installations.

INS-32024: The specified location for Oracle base is invalid.

Cause: The specified Oracle base location is identical to an existing Oracle home location.

Action: Specify a location for Oracle base which is not an existing Oracle home.

INS-32025: The chosen installation conflicts with software already installed in the given Oracle home.

Cause: The chosen installation conflicted with software already installed in the given Oracle home.

Action: Install into a different Oracle home.

INS-32026: The Software Location specified should not be under Oracle base location.

Cause: Grid Infrastructure for a Cluster installation will assign root ownership to all parent directories of Oracle Clusterware software location. As a result, all named directories in the software location path will acquire root ownership. This may create problems for subsequent installations into the same Oracle base.

Action: Specify software location outside of Oracle base.

INS-32027: The ORACLE\_HOME environment variable is currently set and this value is not same as the specified path for software location. This will impact the proper configuration of software.

Cause: n/a

Action: n/a

INS-32030: Invalid location for Central Inventory.

Cause: The Central Inventory location provided was empty.

Action: Provide a valid location for the inventory.

INS-32031: Invalid inventory location.

Cause: Inventory location was invalid.

Action: Specify a valid inventory location.

INS-32033: Central Inventory location is not writable.

Cause: Central Inventory location was not writable.

Action: Ensure that the inventory location is writable.

INS-32034: Invalid characters specified for the inventory directory.

Cause: The inventory directory contained one or more invalid characters.

Action: The inventory directory can contain only alphanumeric, hyphen, and underscore characters.

INS-32035: Unable to create a new central inventory directory: string.

Cause: The central inventory location provided is not empty.

Action: Please provide another location for the inventory, or clean up the current location.

INS-32036: User home directory is not recommended as inventory location

Cause: User home directory has been chosen as inventory directory. Oracle recommends that the inventory directory is not users home directory, because members of inventory group will be given write permission to the inventory directory.

Action: Choose a directory other than users home as inventory location.

INS-32037: The operating system group specified for central inventory (oraInventory) ownership is invalid.

Cause: No value specified for central inventory (oraInventory) ownership group.

Action: Specify an operating system group whose members should have write permission to the central inventory directory (oraInventory).

INS-32038: The operating system group specified for central inventory (oraInventory) ownership is invalid.

Cause: User performing installation is not a member of the operating system group specified for central inventory(oraInventory) ownership.

Action: Specify an operating system group that the installing user is a member of. All the members of this operating system group will have write permission to the central inventory directory (oraInventory).

INS-32039: Inappropriate file permissions for inventory location.

Cause: The current user and current group do not match with the user and group of inventory location.

Action: Ensure that the file user and group are same as the installer user and install group respectively.

INS-32052: Oracle base and Oracle home locations are same.

Cause: Oracle base and Oracle home locations were same.

Action: Oracle base and Oracle home locations cannot be same. Oracle recommends installing Oracle software within the Oracle base directory. Adjust the Oracle home or Oracle base accordingly.

INS-32053: The specified Oracle home name already exists.

Cause: The Oracle home name specified on the command line corresponded to an existing Oracle home name in the Central Inventory.

Action: Choose another Oracle home name. Abort this installation session and try again.

INS-32054: The Central Inventory string is located on a shared file system.

Cause: The Central Inventory string was located on a shared file system.

Action: Oracle recommends placing this Central Inventory on a local file system that is not shared by other systems, because it is a server-specific inventory of the installation on this server. Oracle strongly recommends that you move the Central Inventory to a local disk so that installations from other servers do not corrupt the Central Inventory for this server.

INS-32055: The Central Inventory is located in the Oracle base.

Cause: The Central Inventory is located in the Oracle base.

Action: Oracle recommends placing this Central Inventory in a location outside the Oracle base directory.

INS-32060: Insufficient permissions granted to create directory string on node string.

Cause: Insufficient write permissions were granted to create this directory on the specified node.

Action: Ensure that you have the required write permissions. Alternatively, you may want to choose another location.

INS-32061: The selected ASM disk group is invalid.

Cause: An invalid or non-existent ASM disk group has been selected.

Action: Ensure that the selected ASM disk group exists.

INS-32062: Unable to create string at the specified location.

Cause: The string location provided is not absolute path.

Action: Please provide absolute location for the string.

INS-32066: Microsoft Transaction Services (MTS) port is blank or containing non-numeric character.

Cause: The MTS port text field is either empty or containing non-numeric characters

Action: Provide a valid value for MTS port.

INS-32067: The value you have entered for Microsoft Transaction Services (MTS) Port, string, is already in use.

Cause: Refer to the error message for details.

Action: Specify a valid port number.

INS-32068: The value specified for Microsoft Transaction Services (MTS) Port number, string, is out of valid range.

Cause: The value you have entered for the MTS Port is out of the valid range.

Action: Enter a MTS Port number between 1024 and 65535.

INS-32075: At least one product language need to selected

Cause: No product language selected for installation.

Action: Select at least one product language for installation.

INS-32076: English cannot be removed from the selected languages list.

Cause: An attempt was made to remove English from the selected languages list.

Action: Select English as one of the selected product languages.

INS-32077: The following selected languages are not supported; string

Cause: Not all selected product languages are supported.

Action: Refer to the sample response file for more information.

INS-32090: Software installation was unsuccessful.

Cause: Refer the log files for details.

Action: Refer to the logs or contact Oracle Support Services.

INS-32091: Software installation was successful. But some configuration assistants failed, were cancelled or skipped.

Cause: n/a

Action: n/a

INS-32101: My Oracle Support username is empty.

Cause: My Oracle Support username cannot be empty..

Action: Provide a valid My Oracle Support username.

INS-32102: My Oracle Support password is empty.

Cause: My Oracle Support password cannot be empty..

Action: Provide a valid My Oracle Support password.

INS-32103: Connection to My Oracle Support could not be established.

Cause: Credentials provided may be invalid, or there may be a network connection issue.

Action: Check the My Oracle Support credentials. Also check the proxy setting and authentication credentials, and the network connection.

INS-32104: The installer is unable to locate the software updates in the specified directory.

Cause: The installer is unable to locate the software updates in the specified directory.

Action: For software updates to work in offline mode, the downloaded updates must be in a particular path location format. Refer to your installation manual for details.

INS-32105: n/a

Cause: n/a

Action: n/a

INS-32106: n/a

Cause: n/a

Action: n/a

INS-32107: n/a

Cause: n/a

Action: n/a

INS-32108: n/a

Cause: n/a

Action: n/a

INS-32109: Failed to retrieve the updates from My Oracle Support.

Cause: The My Oracle Support credentials you provided may not have download privileges, or there may be a network or proxy authentication issue.

Action: Provide credentials with download privileges. Also check the network connection and, if you have a proxy realm, your proxy credentials.

INS-32110: Failed to retrieve the updates from My Oracle Support.

Cause: This may be due to a network connection problem or a missing patch on My Oracle Support.

Action: Check the connection to My Oracle Support or contact Oracle Support Services.

INS-32111: The patch download location provided is empty.

Cause: The patch download location cannot be empty.

Action: Provide the location where the updates have been downloaded.

INS-32112: Unable to retrieve the details from the downloaded metadata.

Cause: The downloaded metadata for software updates is not properly formatted.

Action: Refer to the logs or contact Oracle Support Services.

INS-32113: Unable to read the updates location.

Cause: n/a

Action: n/a

INS-32114: Check the My Oracle Support user name.

Cause: The user name provided is invalid. It either contains invalid characters or does not follow the standard e-mail address format.

Action: Specify an e-mail address that is consistent with RFC 2822 and RFC 2821 format.

INS-32115: Insufficient space in the download location provided.

Cause: The location provided does not have space for downloading all the updates.

Action: Choose a location with enough space or free up space on the existing volume.

INS-32117: My Oracle Support credentials provided does not have download privileges.

Cause: My Oracle Support credentials provided does not have download privileges.

Action: Provide My Oracle Support credentials with download privileges in order to check for latest updates.