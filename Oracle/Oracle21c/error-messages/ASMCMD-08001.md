---
title: Database Error Messages
book: Database Error Messages
doc_id: F30283-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/errmg/ASMCMD-08001.html
tags:
  - oracle
  - 21c
  - error-messages
---

ASMCMD-08001: diskgroup 'string' does not exist or is not mounted

Cause: An operation failed because the diskgroup specified did not exist or was not mounted by the current Oracle Automatic Storage Management (Oracle ASM) instance.

Action: Verify that the diskgroup name specified is valid, that the diskgroup exists, and that the diskgroup is mounted by the current Oracle ASM instance.

ASMCMD-08002: entry 'string' does not exist in directory 'string'

Cause: The specified path contained elements that did not exist.

Action: Specify an existing Oracle ASM file path.

ASMCMD-08003: command disallowed by current instance type

Cause: ASMCMD was connected to an instance with an instance type other than Oracle Automatic Storage Management (Oracle ASM).

Action: Ensure you are connecting to an instance whose INSTANCE\_TYPE parameter is Oracle ASM.

ASMCMD-08004: Oracle ASM file path 'string' contains an invalid alias name

Cause: The path specified contained an invalid alias name.

Action: Specify a valid path.

ASMCMD-08005: directory 'string' is ambiguous

Cause: The directory on which the command was executed translated to multiple matches.

Action: Specify a unique directory string.

ASMCMD-08006: entry 'string' does not refer to an existing directory

Cause: The 'cd' command failed as the specified path did not exist.

Action: Specify an existing Oracle ASM file path.

ASMCMD-08007: unclosed single quotation mark

Cause: The input did not contain a closing single quotation mark.

Action: Close the single quotation mark properly.

ASMCMD-08008: both source 'string' and target 'string' cannot be from remote instances

Cause: The 'copy' command specified both source and target files that were on remote instances.

Action: Either the source file or the target file can be on the remote instance, but not both.

ASMCMD-08009: more than one source file specified, one of which is remote

Cause: The 'copy' command specified multiple source files, at least one of which was remote.

Action: When there are multiple source files, all of them must be on the local node only.

ASMCMD-08010: user name is not specified in remote instance connect string 'string'

Cause: The user name was not specified in the remote instance connect string.

Action: Specify the user name in the remote instance connect string.

ASMCMD-08011: instance identifier is not specified in the remote instance connect string 'string'

Cause: An instance identifier was not specified in the remote instance connect string.

Action: Specify an instance identifier in the remote instance connect string.

ASMCMD-08012: cannot determine file type for file

Cause: The file type was incompatible with the copy operation.

Action: Specify file types which are supported by Oracle Automatic Storage Management (Oracle ASM) such as CONTROLFILE, DATAFILE, etc.

ASMCMD-08013: cannot determine logical block size for file 'string'

Cause: During the copy operation, the logical block size of the indicated file could not be determined. The file is corrupted or it is an internal error.

Action: Ensure that the source and destination files are valid and retry. If the source and destination files are valid, contact Oracle Support Services.

ASMCMD-08014: file 'string' does not exist

Cause: The file specified did not exist or is a directory.

Action: Specify a file that exists and make sure it is not a directory.

ASMCMD-08015: child 'string' cannot be on remote instance

Cause: The 'setsparseparent' command specified a child file that was on a remote instance.

Action: The child file cannot be on a remote instance.

ASMCMD-08016: copy source 'string' and target 'string' failed

Cause: The 'copy' command was not successful.

Action: Examine the accompanying error messages for details.

ASMCMD-08017: setting parent of child 'string' to new parent 'string' failed

Cause: The 'setsparseparent' command was not successful.

Action: Examine the accompanying error messages for details.

ASMCMD-08018: more than one child file specified, one of which is remote

Cause: The 'setsparseparent' command specified multiple child files, at least one of which was remote.

Action: When there are multiple child files, all of them must be on the local node only.

ASMCMD-08019: parent 'string' cannot be on remote instance

Cause: The 'setsparseparent' command specified a parent file that was on a remote instance.

Action: The parent file cannot be on a remote instance.

ASMCMD-08020: could not write into trace file

Cause: Writing to the trace file failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08021: password cannot contain the following characters $%%^&\*()'" or tab

Cause: Invalid characters were found in the specified password.

Action: Supply a password which does not contain $%%^&\*()'" or tab.

ASMCMD-08022: unknown command 'string' specified

Cause: An unknown command was specified.

Action: Enter a valid command; 'asmcmd help' will list valid commands.

ASMCMD-08023: copying password file using Oracle ASM requires software version 'string' or later on host 'string'

Cause: A request to copy a password file was issued to an Oracle Automatic Storage Management (Oracle ASM) instance whose version did not support that operation.

Action: Upgrade Oracle ASM to version 12.1 or later.

ASMCMD-08024: file number could not be determined for alias name 'string'

Cause: The attempt to determine the file number for the specified alias was unsuccessful.

Action: Ensure that the discovery string corresponds to disks for the specified disk group. The specified alias name may not be valid; ensure that it exists. If an ASM system file name was passed, then use the --sys\_filename option.

ASMCMD-08025: Invalid file name specified. Absolute path name is required when there is no connection to Oracle ASM instance.

Cause: The specified file name did not begin with '+'. It is therefore treated as a relative path name which requires a connection to Oracle Automatic Storage Management.

Action: Specify an absolute path name for the file you wish to extract. Absolute path names begin with '+diskgroup'.

ASMCMD-08026: Password file 'string' is in use. Use the force option.

Cause: A password file was specified, but it is used by other resources.

Action: Use the force option to share the given password file with other resources.

ASMCMD-08027: Password file 'string' already exists. Use the force option to overwrite.

Cause: An attempt to create a password file failed because it already existed.

Action: Use the force option to overwrite an existing password file.

ASMCMD-08028: Password file 'string' is associated with 'string' already. Use the force option.

Cause: A password file was specified for a CRS resource, which already has a password file associated with it.

Action: Use the force option to associate new password file.

ASMCMD-08029: Cannot change diskgroup redundancy from 'string' to 'string'

Cause: The disk group redundancy must be either NORMAL or HIGH to perform this operation.

Action: Try again with a NORMAL or HIGH redundancy disk group.

ASMCMD-08030: file 'string' specified with 'sparse\_merge\_end' cannot be on remote instance

Cause: The 'copy' command with the 'sparse\_merge\_end' option specified a file that was on a remote instance.

Action: The file cannot be on a remote instance.

ASMCMD-08031: more than one file specified with 'sparse\_merge\_begin' option

Cause: The 'copy' command specified multiple files with the 'sparse\_merge\_begin' option.

Action: Multiple files cannot be specified with the 'sparse\_merge\_begin' option.

ASMCMD-08032: target 'string' cannot be on remote instance

Cause: The 'copy' command with the 'sparse\_merge\_begin' and 'sparse\_merge\_end' options specified a target file that was on a remote instance.

Action: The target file cannot be on a remote instance.

ASMCMD-08033: failure merging sparse files 'string' through 'string' to target 'string'

Cause: The 'copy' command with the 'sparse\_merge\_begin' and 'sparse\_merge\_end' options was not successful.

Action: Examine the accompanying error messages for details.

ASMCMD-08034: sparse merge copy operation failure due to incorrect command syntax

Cause: The 'copy' command with the 'sparse\_merge\_begin' and 'sparse\_merge\_end' options was not successful due to incorrect command syntax.

Action: Check command line help for the correct syntax.

ASMCMD-08035: file specified with sparse\_merge\_begin and sparse\_merge\_end are the same - 'string'

Cause: The 'copy' command specified same files for both the 'sparse\_merge\_begin' and 'sparse\_merge\_end' options.

Action: Make sure files specified with the 'sparse\_merge\_begin' and 'sparse\_merge\_end' options are different.

ASMCMD-08036: file 'string' specified with 'sparse\_merge\_begin' cannot be on remote instance

Cause: The 'copy' command with the 'sparse\_merge\_begin' option specified a file that was on a remote instance.

Action: The file cannot be on a remote instance.

ASMCMD-08037: invalid system alias root path name 'string'

Cause: An invalid system alias root path name was specified.

Action: Ensure that the 'dest\_dbname' option is a non-null, begins with an alphabetic character, and follows up with alphanumeric characters, underscore (\_), number sign (#), or dollar sign ($), if dest\_dbname is longer than one character.

ASMCMD-08038: invalid path to ASM system file name 'string'

Cause: An invalid file path to an ASM system file name was specified.

Action: Ensure that the provided ASM file name is not an alias, and that it points to an existing file. An ASM system file name follows the format name.<file\_number>.incarnation.

ASMCMD-08039: disk group 'string' does not match with the disk group in the file path 'string'

Cause: The specified disk group and the disk group in the file path were different.

Action: Ensure that the provided disk group is the same as the disk group in the file path. If you use a relative path, then ensure that you are inside the desired disk group.

ASMCMD-08040: no disks found from disk group 'string' in the discovery string 'string'

Cause: No disks from the given disk group were found in the specified discovery string.

Action: Ensure that the provided discovery string exists and that it contains disks from the specified disk group.

ASMCMD-08041: The 'credverify' command cannot be executed; Oracle ASM is not running on the cluster.

Cause: The specified command does not allow client access mode. Oracle ASM was not running on the local cluster.

Action: Ensure that Oracle ASM is running on the local cluster by issuing the command 'srvctl status asm'.

ASMCMD-08042: no credentials in OCR

Cause: There were no credentials in the Oracle Cluster Registry (OCR).

Action: Execute the 'credfix' command to create a working credential.

ASMCMD-08043: more than one credential in OCR

Cause: There was more than one credential in the Oracle Cluster Registry (OCR) when there should have only been one.

Action: Execute the 'credfix' command. This keeps the newest working credential and deletes the older ones.

ASMCMD-08044: more than one credential in the password file

Cause: The password file had more than one credential when there should have only been one.

Action: Execute the 'credfix' command. This keeps the newest working credential and deletes the older ones.

ASMCMD-08045: no credentials in the password file

Cause: The password file had no credentials when there should be one.

Action: Execute the 'credfix' command to create a working credential.

ASMCMD-08046: credentials in the password file and Oracle Cluster Registry (OCR) do not match

Cause: The OCR and password file had mismatching credentials.

Action: Execute the 'credfix' command to make the credentials match.

ASMCMD-08047: cannot connect with credentials for user string

Cause: The credentials stored for the specified user could not be used to connect."

Action: Execute the 'credfix' command to create a working credential.

ASMCMD-08048: no credentials in OLR on node (string

Cause: There were no credentials in the Oracle Local Registry (OLR)."

Action: Execute the 'credfix' command to import credentials to OLR.

ASMCMD-08049: more than one credential in OLR on node string

Cause: There was more than one credential in the Oracle Local Registry (OLR).

Action: Execute the 'credfix' command to delete extra credentials.

ASMCMD-08050: credentials inconsistent on OCR and OLR on node string

Cause: The credentials in the Oracle Cluster Registry (OCR) and Oracle Local Registry (OLR) did not match.

Action: Execute the 'credfix' command to create matching credentials.

ASMCMD-08051: failed to execute internal operation, see accompanying error messages or alert log.

Cause: There was a failure executing an internal operation.

Action: Try running the 'credverify' or 'credfix' command again, and examine the alert log for more information. Contact Oracle Support Services if not resolved.

ASMCMD-08052: failed to create new credentials

Cause: The call to ASMCMD 'addcrscreds' command failed.

Action: Rerun the command with '-v info' specified, and examine the ASMCMD trace files. Contact Oracle Support Services if not resolved.

ASMCMD-08053: could not import credentials to node string

Cause: The call to ASMCMD 'credimport' command failed.

Action: Rerun the command with '-v info' specified, and examine the ASMCMD trace files. Contact Oracle Support Services if not resolved.

ASMCMD-08054: could not delete Cluster Ready Services (CRS) credentials for user string

Cause: The call to ASMCMD 'delcrscreds' command failed.

Action: Rerun the command with '-v info' specified, and examine the ASMCMD trace files. Contact Oracle Support Services if not resolved.

ASMCMD-08055: failed to perform remote operation, see accompanying error messages

Cause: There was a failure executing an operation using SSH or 'cluutil'.

Action: Contact Oracle Support Services.

ASMCMD-08056: Platform string is not supported for 'credverify' or 'credfix' commands. The supported platforms are string.

Cause: Commands 'credverify' or 'credfix' could not be executed. The 'credverify' and 'credfix' commands require SSH capability. This is only supported for certain platforms.

Action: Contact Oracle Support Services.

ASMCMD-08057: cannot connect using credentials in OLR on node string

Cause: The credentials in Oracle Local Registry (OLR) did not work or match with Oracle Cluster Registry (OCR)."

Action: Execute the 'credfix' command to import working credentials to the OLR.

ASMCMD-08058: The 'credverify' or 'credfix' commands must be run on a node with a local ASM instance.

Cause: There was an error executing the 'credverify' or 'credfix' command. These commands were run on a node without a local ASM instance.

Action: Run the 'credverify' or 'credfix' commands on a node with a local ASM instance.

ASMCMD-08059: The ORACLE\_SID parameter is not set.

Cause: The ORACLE\_SID parameter was not set.

Action: Set the ORACLE\_SID parameter.

ASMCMD-08060: SSH equivalency is not set up between all nodes in the cluster.

Cause: SSH equivalency was not set up between the nodes in the cluster.

Action: Set up SSH equivalency for the 'credverify' or 'credfix' commands to work.

ASMCMD-08061: The ORACLE\_HOME parameter is not set.

Cause: The ORACLE\_HOME parameter was not set.

Action: Set the ORACLE\_HOME parameter.

ASMCMD-08062: ASM root credential domain does not exist in node string.

Cause: The Oracle Automatic Storage Management (Oracle ASM) root credential domain did not exist on the specified node.

Action: Execute the command 'credfix --root' as a root user.

ASMCMD-08063: Oracle High Availability Services is not running on nodes string.

Cause: Oracle High Availability Services was not running on the listed nodes.

Action: Execute 'crsctl start has' on all of the listed nodes in order for the 'credverify' and 'credfix' commands to work.

ASMCMD-08064: ASM root credential domain does not exist on Oracle Cluster Registry (OCR).

Cause: The root credential domain did not exist on the OCR.

Action: Execute the command 'credfix --root' as a root user.

ASMCMD-08065: The command 'credfix --root' must be run as a root user.

Cause: The command 'credfix --root' was not run as root.

Action: Execute the command 'credfix -root' as a root user.

ASMCMD-08066: The command 'credfix' needs the --root flag to fix existing issues.

Cause: The command 'credfix' ran without the '--root' flag.

Action: Execute the command 'credfix --root --giuser giuser' as a root user to fix existing issues.

ASMCMD-08067: Oracle Flex ASM is not enabled.

Cause: Oracle Flex ASM was not enabled.

Action: Execute the command 'credfix --root' to enable Oracle Flex ASM.

ASMCMD-08068: The command 'credfix --root' must be run with option '--giuser giuser' specified.

Cause: The command 'credfix --root' was run without the option '--giuser giuser' specified.

Action: Execute the command 'credfix --root --giuser giuser'.

ASMCMD-08069: The Oracle Automatic Storage Management (Oracle ASM) credential domain has incorrect permissions.

Cause: The Oracle ASM credential domain did not have the correct permissions for a Grid user.

Action: Execute the command 'credfix --root --giuser giuser' as a root user.

ASMCMD-08070: Invalid file name specified 'string'. Absolute path name is required for operating system files.

Cause: The specified file was not an absolute operating system path. Operating system paths must be absolute path names.

Action: Specify an absolute path name for the operating system file.

ASMCMD-08071: invalid '--local' option for source path and destination path

Cause: An attempt was made to use the '--local' option when either copying a file from one ASM disk group to another or from one operating system file path to another.

Action: Remove the '--local' option or specify a different source or destination file.

ASMCMD-08072: encountered operating system error string when opening file string

Cause: The operating system file could not be opened because of an internal operating system error.

Action: Check the root cause of the operating system error and try the process again.

ASMCMD-08073: encountered operating system error string when closing file string

Cause: The operating system file could not be closed because of an internal operating system error.

Action: Check the root cause of the operating system error and try the process again.

ASMCMD-08074: The Oracle Automatic Storage Management (Oracle ASM) credential domain did not exist on the node.

Cause: The Oracle Automatic Storage Management (Oracle ASM) did not exist on the specified node.

Action: Process the command 'credfix' to fix the credentials.

ASMCMD-08075: The Oracle Automatic Storage Management (Oracle ASM) credential domain did not exist on the Oracle Cluster Registry (OCR).

Cause: The Oracle Automatic Storage Management (Oracle ASM) credential domain did not exist on the OCR.

Action: Process the command 'credfix' to fix the credentials.

ASMCMD-08076: 'credverify' or 'credfix' cannot proceed due to incorrect Oracle ASM listener setup

Cause: A connection to Oracle Automatic Storage Management (Oracle ASM) failed as a result of an incorrect Oracle ASM listener setup. The credentials may not be incorrect.

Action: Ensure that the Oracle ASM listener is running, and then try processing 'credverify' or 'credfix' again.

ASMCMD-08102: no connection to Oracle ASM; command requires Oracle ASM to run

Cause: A command that requires Oracle Automatic Storage Management (Oracle ASM) processing was issued but there was no connection to an Oracle ASM instance.

Action: Start the Oracle ASM instance and retry the command.

ASMCMD-08103: failed to connect to ASM; ASMCMD running in non-connected mode, ORACLE\_SID='string'

Cause: An attempt to connect to Oracle Automatic Storage Management (Oracle ASM) was made using ORACLE\_SID='%(1)s' but the connection failed.

Action: Check the accompanying error messages in case the operation fails. If Oracle ASM is required, then start the ASM instance and retry the command.

ASMCMD-08201: Oracle ASM not available\\n string

Cause: During a copy operation, connection to the Oracle Automatic Storage Management (Oracle ASM) instance on the remote node failed.

Action: Check ASMCMD alert log for more information.

ASMCMD-08202: internal error: string

Cause: There was an internal error.

Action: Contact Oracle Support Services.

ASMCMD-08203: The executable 'string' failed its execution.

Cause: An issue occurred when executing the binary, which could be a signal, a coredump, or an error return code from the binary.

Action: Check accompanying error messages in the alert log.

ASMCMD-08303: invalid SPFILE 'string'

Cause: The specified server parameter file did not have a valid file type, a valid file size, or a valid block size.

Action: Specify a valid server parameter file.

ASMCMD-08304: invalid ORACLE ASM SPFILE 'string'

Cause: The specified ORACLE ASM SPFILE did not have a valid file type.

Action: Specify a valid ORACLE ASM SPFILE.

ASMCMD-08305: GPNPTOOL executable not found at 'string'

Cause: The GPNPTOOL executable was not found at the indicated location.

Action: Contact Oracle Support Services.

ASMCMD-08306: could not edit the GPnP profile

Cause: A 'gpnptool edit' command failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08307: could not sign the GPnP profile

Cause: A 'gpnptool sign' command failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08308: -f option cannot be used when Oracle Clusterware stack is up

Cause: The force option was supplied when the Oracle Clusterware stack was up.

Action: Remove the force option and retry.

ASMCMD-08309: could not check the status of cluster

Cause: The command 'crsctl check css' failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08310: could not get the GPnP profile sequence number

Cause: An error occurred while retrieving the sequence number of the GPnP profile.

Action: Examine the accompanying error messages for details.

ASMCMD-08313: CRSCTL executable not found at 'string'

Cause: The CRSCTL executable was not found at the indicated location.

Action: Contact Oracle Support Services.

ASMCMD-08314: could not set the disk string

Cause: The command 'srvctl modify asm -d diskstring' failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08315: could not determine the mode in which Oracle Clusterware is running

Cause: The command 'crsctl status resource ora.crsd -init -g' failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08316: SRVCTL executable not found at 'string'

Cause: The SRVCTL executable was not found at the indicated location.

Action: Contact Oracle Support Services.

ASMCMD-08317: could not get the Oracle ASM disk string

Cause: The command 'srvctl config asm' to get the Oracle Automatic Storage Management (Oracle ASM) disk string failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08318: environment variable 'string' not set

Cause: The environment variable HOSTNAME was not set before running this command.

Action: Set the variable HOSTNAME and retry.

ASMCMD-08319: could not locate the GPnP profile

Cause: The Grid Plug and Play (GPnP) profile did not exist.

Action: Contact Oracle Support Services.

ASMCMD-08320: destination cannot be an alias directory when the source is a fully qualified ASM file name

Cause: The destination for the copy was an ASM alias directory and the provided SPFILE source path was a fully qualified ASM file name.

Action: When providing a fully qualified ASM file name as the SPFILE source, provide either the disk group name only or an ASM alias name as the destination path.

ASMCMD-08402: operation was not performed on the file string

Cause: Altering the diskgroup to change the owner, group, or permissions failed.

Action: Examine the accompanying error messages for details.

ASMCMD-08406: cannot accept null password

Cause: A null password was passed.

Action: A non-null password must be entered.

ASMCMD-08409: 'chmod' operation not allowed for string

Cause: A 'chmod' command specified the write-only permission.

Action: Specify a permission other than write-only and retry the command.

ASMCMD-08410: invalid KEYSTORE FILE 'string'

Cause: The specified keystore file did not have a valid file type, a valid file size, or a valid block size.

Action: Specify a valid keystore file.

ASMCMD-08411: operations on a KEYSTORE file require the SYSASM privilege

Cause: An attempt to copy a keystore file was made without the SYSASM privilege.

Action: Retry the operation as a SYSASM user.

ASMCMD-08552: invalid diskgroup name 'string'

Cause: An invalid diskgroup name was specified.

Action: Ensure that the command's -G option has a non-null value passed and has only alphanumeric characters.

ASMCMD-08554: invalid volume name 'string'

Cause: An invalid volume name was specified.

Action: Ensure that the volume name is a non-null value and has only alphanumeric characters.

ASMCMD-08557: diskgroup 'string' volume 'string' not found

Cause: The specified diskgroup or volume was not found.

Action: Specify a valid diskgroup and volume.

ASMCMD-08558: invalid size multiplier specified

Cause: An invalid size multiplier was specified.

Action: Specify a numeric volume size terminating in 'K', 'k', 'M', 'm', 'G', 'g', T',or 't'.

ASMCMD-08559: invalid size specified

Cause: The size specified contained a valid size multiplier but contained other non-numeric characters.

Action: Specify a numeric volume size terminating in 'K', 'k', 'M', 'm', 'G', 'g', T',or 't'.

ASMCMD-08601: could not create the analyze directory

Cause: An internally issued 'mkdir' command failed to create the analyze directory.

Action: Examine the accompanying error messages for details.

ASMCMD-08602: time stamp format is not recognized

Cause: The format for time stamp was invalid.

Action: Specify a time stamp in the following format: Mon Sep 19 19:56:15 2011.

ASMCMD-08603: invalid value specified for 'tracedirectory'

Cause: The specified trace directory did not exist.

Action: Supply a valid trace directory which contains the set of logs and trace files that need to be analyzed.

ASMCMD-08604: Start time is later than end time. Please specify end time later than start time.

Cause: Inconsistent values for --startime and --endtime options.

Action: Please specify the value of --endtime option later than the value of --starttime option

ASMCMD-08605: cannot read the event list file.\\n

Cause: The event list file did not exist or could not be read

Action: Check if the file asmevents.xml exists under $ORACLE\_HOME/lib and you have read permissions.

ASMCMD-08606: invalid disk group name 'string'.

Cause: The disk group name specified contained special characters.

Action: Ensure that the disk group name specified only contains alphanumeric characters and underscores.

ASMCMD-08608: invalid value for 'string' option: string

Cause: The provided value was not valid for the specified option.

Action: Correct the value and retry the command.

ASMCMD-08609: file group 'string' does not exist

Cause: The specified file group name did not exist.

Action: Specify the name of an existing file group.

ASMCMD-08610: cannot access 'string', no such XML file

Cause: The specified file did not exist.

Action: Specify the name of an existing file.

ASMCMD-08611: cannot read 'string', permission denied

Cause: The permission to read the specified file or directory was not granted.

Action: Grant read permission for the file or directory and retry the command.

ASMCMD-08612: failed to create member cluster 'string' because plugging in the GIMR PDB from a directory requires configuring the GIMR component

Cause: An attempt to configure the indicated member cluster failed because the Grid Infrastructure Management Repository (GIMR) component was not specified.

Action: Retry the command specifying the '--gimr' option.

ASMCMD-09345: could not open intermediate file 'string'\\n

Cause: During Oracle Automatic Storage Management (Oracle ASM) metadata backup operation, an attempt to open the intermediate file failed.

Action: Supply an existing file that can be read and written to by the current user.

ASMCMD-09347: invalid intermediate file 'string'

Cause: The intermediate file did not begin with string '@diskgroup\_set' or there was an error while evaluating the file contents.

Action: Ensure that the intermediate file begins with '@diskgroup\_set' or contact Oracle Support Services.

ASMCMD-09349: diskgroup 'string' not discovered by Oracle ASM instance; skipping...

Cause: A non-existent diskgroup was specified during execution of the 'md\_backup' command.

Action: Specify a valid diskgroup and retry the command.

ASMCMD-09350: diskgroup 'string' not mounted by Oracle ASM instance; skipping...

Cause: The diskgroup specified was not mounted in an Oracle Automatic Storage Management (Oracle ASM) instance.

Action: Mount the diskgroup in the Oracle ASM instance and retry the command.

ASMCMD-09351: Oracle ASM instance has no diskgroup mounted

Cause: Oracle Automatic Storage Management (Oracle ASM) instance had no diskgroups mounted.

Action: Mount the diskgroups to be backed up and retry the command.

ASMCMD-09352: CREATE DISKGROUP failed\\nstring

Cause: SQL command execution failed.

Action: Fix the error in the SQL command and retry the command.

ASMCMD-09353: ADD or ALTER TEMPLATE failed\\nstring

Cause: SQL command execution failed.

Action: Fix the error in the SQL command and retry the command.

ASMCMD-09354: ADD ALIAS failed\\nstring

Cause: SQL command execution failed.

Action: Fix the error in the SQL command and retry the command.

ASMCMD-09355: could not find information for diskgroup 'string' in backup file

Cause: Information about the diskgroup specified was not present in the backup file.

Action: Check that the correct diskgroup name and the backup file are specified and retry the command.

ASMCMD-09356: backup file 'string' is either empty or cannot be interpreted

Cause: Incorrect backup file was specified.

Action: Specify a non-empty backup file.

ASMCMD-09357: file with name 'string' already exists

Cause: The specified file already exists.

Action: Change the file name and retry the command.

ASMCMD-09358: source and target files are the same - 'string'

Cause: The source and target file were the same.

Action: Make sure the source and target files are different.

ASMCMD-09359: invalid diskgroup name 'string' specified in override options

Cause: The old diskgroup name specified in the override options was not found in the backup file.

Action: Correct the diskgroup name and retry the command.

ASMCMD-09360: ADD or ALTER ATTRIBUTE failed\\nstring

Cause: SQL command execution failed.

Action: Fix the error in the SQL command and retry the command.

ASMCMD-09361: backup version not supported\\nstring

Cause: The COMPATIBLE.ASM value of the diskgroup in the backup file was greater than the Oracle Automatic Storage Management (Oracle ASM) instance version executing the command.

Action: Upgrade the Oracle ASM instance and retry the command.

ASMCMD-09362: ADD or ALTER VOLUME failed\\nstring

Cause: SQL command execution failed.

Action: Fix the error in the SQL command and retry the command.

ASMCMD-09363: disk group containing auxiliary volume not found

Cause: Disk recovery log did not exist.

Action: Use the --silent option to create volume with no recovery log disk group. Use the --full or -G option and restore disk recovery log.

ASMCMD-09364: volume device for VOLUME: 'string' in DG: 'string' does not exist

Cause: Volume was not restored or was not listed for restore.

Action: Create volume with the given volume name in the given disk group.

ASMCMD-09365: failed to make file system\\nstring

Cause: The command execution failed.

Action: Fix the error in the mkfs command.

ASMCMD-09366: invalid user name 'string' specified for string

Cause: The specified user name did not exist on the host.

Action: Create a local system user with the specified user.

ASMCMD-09367: invalid group name 'string' specified for string

Cause: The specified group name did not exist on the host.

Action: Create a local system group with the specified group.

ASMCMD-09368: ACFS is not loaded

Cause: ACFS was not loaded.

Action: Contact Oracle Support Services.

ASMCMD-09369: Could not open file 'string'

Cause: During Oracle Automatic Storage Management (Oracle ASM) metadata scan operation, an attempt to open the output file failed.

Action: Supply a non existing file that can be written to by the current user.

ASMCMD-09370: cannot read the Oracle ACFS list file

Cause: The Oracle Automatic Storage Management Cluster File System (Oracle ACFS) list file did not exist or could not be read.

Action: Check if the file asmcmdambracfs.xml exists under $ORACLE\_HOME/lib and that you have read permissions.

ASMCMD-09371: disk 'string' does not exist in diskgroup 'string'

Cause: The disk specified was not part of the diskgroup.

Action: Correct the disk name and retry the command. The disk name must match the NAME column in the V$ASM\_DISK view.

ASMCMD-09372: physical blocks string-string do not map to a valid Oracle ASM file

Cause: The physical blocks specified were not part of any Oracle Automatic Storage Management (Oracle ASM) file.

Action: Correct the range of the physical block numbers and retry the command.

ASMCMD-09373: not all physical blocks submitted for remapping

Cause: An attempt to submit all of the physical blocks for remapping failed.

Action: Examine the accompanying error messages for details.

ASMCMD-09374: KFED executable not found at 'string'

Cause: The KFED executable was not found at the indicated location.

Action: Run these commmands if using Oracle 10.2 or later: cd $ORACLE\_HOME/rdbms/lib make -f ins\_rdbms.mk ikfed Run these commmands if using Oracle 10.1: cd $ORACLE\_HOME/rdbms/lib mv ssskfeded.o sskfeded.o make -f ins\_rdbms.mk $ORACLE\_HOME/rdbms/lib/kfed mv kfed../../bin/ Verify that $ORACLE\_HOME/bin/kfed exists and has the execute permission bit set.

ASMCMD-09375: error occurred when executing\\n string\\n\\nstring

Cause: The 'lsdsk' command was not successful.

Action: Fix the error indicated in the accompanying messages and retry the command.

ASMCMD-09378: scanning of disk headers is supported on UNIX platforms only

Cause: The 'lsdsk' command failed because scanning of disk headers is supported on UNIX platforms only.

Action: Start the Oracle Automatic Storage Management instance and retry the command without the -I option.

ASMCMD-09381: 'remap' command requires Oracle ASM software version string or later.

Cause: The Oracle Automatic Storage Management (Oracle ASM) instance did not support the 'remap' command.

Action: Upgrade the Oracle ASM instance and retry the command.

ASMCMD-09382: physical blocks string-string map to an unmirrored file

Cause: Oracle Automatic Storage Management (Oracle ASM) couldnot remap an unmirrored file.

Action: Specify physical blocks which map to a mirrored file.

ASMCMD-09383: 'mapextent' command requires Oracle ASM software version string or later

Cause: The Oracle Automatic Storage Management (Oracle ASM) instance did not support the 'mapextent' command.

Action: Upgrade the Oracle ASM instance and retry the command.

ASMCMD-09384: 'mapau' command requires Oracle ASM software version string or later

Cause: The current Oracle Automatic Storage Management (Oracle ASM) version did not support this command.

Action: Upgrade to 11g Release 2 or a later version.

ASMCMD-09385: 'lsblk' command requires Oracle ASM software version string or later

Cause: The current version of Oracle Automatic Storage Management (Oracle ASM) instance did not support this command.

Action: Upgrade Oracle ASM to 12.2 or a later version and retry the command.

ASMCMD-09386: 'chblk' command requires Oracle ASM software version string or later

Cause: The current version of Oracle Automatic Storage Management (Oracle ASM) instance did not support this command.

Action: Upgrade Oracle ASM to 12.2 or a later version and retry the command.

ASMCMD-09390: invalid XML tag 'string'

Cause: An invalid XML tag was specified.

Action: Check the value of the tag to ensure it is valid and retry.

ASMCMD-09391: invalid XML file

Cause: Certain parameters were not defined or had invalid values in the file.

Action: Check whether the required parameters are defined in the file and retry.

ASMCMD-09392: provided XML file cannot be read

Cause: The provided XML file could not be read.

Action: Check reading permissions on the XML file and retry.

ASMCMD-09395: error parsing XML file: string

Cause: An error occurred while parsing the XML file.

Action: Contact Oracle Support Services.

ASMCMD-09398: element string is empty

Cause: No disks were found in the element.

Action: Add disks to this element and retry.

ASMCMD-09399: argument 'string' is not a valid number

Cause: A numeric value was expected in the argument.

Action: Change the argument to a numeric value.

ASMCMD-09401: command syntax error

Cause: Incorrect command syntax was specified.

Action: Refer to the command line help or to the documentation to determine the correct syntax and options.

ASMCMD-09412: Invalid option: string

Cause: An invalid option was specified.

Action: Refer to the command line help or to the documentation to determine the correct syntax and options.

ASMCMD-09450: missing '--dbuniquename' or '--asm' option for password file located on a diskgroup

Cause: When trying to update the CRSD resource for a password file located on a diskgroup, the '--dbuniquename' parameter or the '--asm' option was not specified.

Action: Execute the command again with the '--dbuniquename' parameter if the password file is a database password file. If the password file is an ASM password file, then execute the command with '--asm' option.

ASMCMD-09451: 'orapwd' executable was not found at 'string'

Cause: 'orapwd' executable was not found at the location.

Action: Ensure that the executable is present at the location and executable permissions are set.

ASMCMD-09452: The password file was not found at 'string' or the path specified does not exist.

Cause: The password file could not be located at the specified path or the path to the password file did not exist.

Action: Ensure that the path specified is valid and that the password file is present at that location.

ASMCMD-09453: failed to register password file as a CRS resource

Cause: An internally issued 'srvctl' command to register the password file as a CRS resource failed.

Action: Ensure that the user has enough privileges to run srvctl commands and respond based on the accompanying error messages.

ASMCMD-09454: could not create new password file

Cause: An internally issued 'orapwd' command to create the password file failed.

Action: Respond based on the accompanying error messages.

ASMCMD-09455: location for the new password file was not valid

Cause: An invalid path was specified to create the password file. ASMCMD can be used to create password files only on disk groups.

Action: Specify a location on a disk group for the password file and make sure the disk group is mounted.

ASMCMD-09456: password file should be located on an ASM disk group

Cause: An invalid path for the password file was specified. The password file should be located on an ASM disk group.

Action: Specify a valid location on a disk group for the password file and make sure the disk group is mounted.

ASMCMD-09457: an internally issued srvctl command failed with errors

Cause: An internally issued 'srvctl' command failed. The location of the password file could not be retrieved from the Cluster Ready Services (CRS) resource.

Action: Respond based on the accompanying error messages.

ASMCMD-09458: user tried to move a password file within Operating System file system

Cause: ASMCMD 'pwmove' or 'pwcopy' was used to move a password file to a different location on an Operating System file system. This action is not supported by the command.

Action: Ensure that ASMCMD pwmove and pwcopy commands are not used to move password files within OS filesystems.

ASMCMD-09459: user tried to move or copy a password file to the same location in the disk group

Cause: ASMCMD 'pwmove' or 'pwcopy' command was used to move or copy a password file to the same location in the disk group. This action is not supported by the command.

Action: Ensure that ASMCMD pwmove and pwcopy commands are not used to move or copy password files to the same location within the disk group.

ASMCMD-09460: ASMCMD 'string' command was used on a file which is not a password file

Cause: This particular ASMCMD command was used on a file which is not a password file. This command supports only operations on password files.

Action: Ensure that the file specified is a password file.

ASMCMD-09461: invalid password file 'string'

Cause: The specified password file did not have a valid file type, a valid file size, or a valid block size.

Action: Specify a valid password file.

ASMCMD-09462: could not delete password file

Cause: An internally issued 'orapwd' command to delete the password file failed.

Action: Respond based on the accompanying error messages.

ASMCMD-09463: operation failed due to lack of write permissions

Cause: An ASMCMD command failed because the user lacks write permissions necessary for the operation. Either the target directory or file does not have write permissions or the target already exists and cannot be overwritten.

Action: Specify a different target or modify the permissions for the target.

ASMCMD-09464: invalid format for password file

Cause: The specified format for the password file was not valid.

Action: Specify a valid format for the password file, for example, 12 or 12.2.

ASMCMD-09470: ASM proxy instance unavailable

Cause: An ASM proxy instance was detected but was not ONLINE.

Action: Start the 'ora.proxy\_asm' resource.

ASMCMD-09471: cannot enable or disable volumes

Cause: Could not communicate with the ASM proxy.

Action: Start the 'ora.proxy\_asm' resource.

ASMCMD-09472: failed to connect to the ASM proxy

Cause: An ONLINE ASM proxy was detected but the connection failed.

Action: Contact Oracle Support Services.

ASMCMD-09473: volume STATE will show as REMOTE

Cause: An ASM proxy instance was detected but was not ONLINE. An Oracle Flex ASM instance cannot display the volume state.

Action: This error is informational only.

ASMCMD-09474: volume statistics cannot be queried

Cause: An ASM proxy instance was detected but was not ONLINE. An Oracle Flex ASM instance cannot display the volume statistics.

Action: Start the 'ora.proxy\_asm' resource.

ASMCMD-09475: ASM proxy SID not found

Cause: An ONLINE ASM proxy was found but the SID could not be determined.

Action: Contact Oracle Support Services.

ASMCMD-09476: failed to create the Cluster Manifest File for member cluster 'string'

Cause: Creation of the Cluster Manifest File for the member cluster failed.

Action: Enable Oracle Flex ASM. Refer to Oracle Automatic Storage Management Administrator's Guide for configuring Oracle Flex ASM. Ensure that the user has write access permission on the Cluster Manifest File. Retry the command.

ASMCMD-09477: delete member cluster 'string' failed

Cause: Deletion of the member cluster failed.

Action: Deinstall the member cluster using the procedure documented in the Oracle Clusterware documentation and retry the command.

ASMCMD-09478: Create or delete member cluster 'string' failed because the Domain Services Cluster is in 'string' state.

Cause: An attempt to configure or deconfigure the indicated member cluster was rejected because the Domain Services Cluster was in the middle of upgrading or patching.

Action: Retry the command when the Domain Services Cluster is in 'Normal' state.

ASMCMD-09479: invalid GUID 'string' specified

Cause: The operation was rejected because the supplied Globally Unique Identifier (GUID) was syntactically invalid.

Action: Retry the command specifying the Globally Unique Identifier (GUID) as a text string of 32 hexadecimal digits (0-f) without a hyphen (-) character or the hexadecimal literal prefix (0x). Refer to the command inline help or product documentation for more information.

ASMCMD-09480: There are too many connection strings for Oracle Flex ASM.

Cause: While fetching connection strings for Oracle Flex ASM, there were too many connection strings.

Action: Run the 'lsnrctl' command to see all are valid ASM end points, or try again later.

ASMCMD-09481: There are no connection strings available for Oracle Flex ASM.

Cause: While fetching connection strings for Oracle Flex ASM, there were no connection strings available.

Action: Make sure ASM is running and is registered.

ASMCMD-09482: Unknown error happened while fetching connection strings for FlexASM

Cause: While fetching connection string for FlexASM, unknown error reported.

Action: Check ASM is running and is registered and retry.

ASMCMD-09485: Operations on the ASM SPFILE require the SYSASM privilege.

Cause: An attempt to modify the ASM SPFILE was made without the SYSASM privilege.

Action: Retry the operation as a SYSASM user.

ASMCMD-09487: 'string' cannot be run with 'string' privilege

Cause: Command was executed with lower privilege

Action: Retry with appropriate privilege.

ASMCMD-09488: operations on member cluster require SYSASM privilege

Cause: An attempt was made to create or delete a member cluster without the SYSASM privilege.

Action: Retry the operation as a SYSASM user.

ASMCMD-09490: member cluster 'string' is not configured

Cause: The specified member cluster was not configured.

Action: Execute the 'asmcmd lscc' command to list all of the configured member clusters. Reexecute the command with a member cluster name that is configured.

ASMCMD-09491: failed to list the configured member clusters

Cause: A failure occurred while attempting to display the member cluster configuration. The accompanying error message provides the details.

Action: Examine the accompanying error message, address the reported issue and retry the operation.

ASMCMD-09492: The configuration for member cluster 'string' is inconsistent between components 'string' and 'string'.

Cause: There were multiple member clusters identified by the indicated name with mismatched versions or GUIDs.

Action: Deinstall one of the member clusters, and deconfigure using a component-specific method. Create the member cluster with a different name using the 'asmcmd mkcc' command with the required components. Install and configure the new member cluster.

ASMCMD-09493: The 'string' feature is not supported on this operating system.

Cause: The command was rejected because the indicated feature is not supported on this operating system.

Action: Refer to the command inline help or product documentation for more information.

ASMCMD-09494: failed to create component 'string' credentials for member cluster 'string'

Cause: A failure occurred while attempting to create credentials for the member cluster.

Action: Examine the accompanying error message, address the reported issue, and retry the operation. If there are no accompanying error messages, contact Oracle Support Services.

ASMCMD-09495: Directory 'string' does not exist.

Cause: An attempt was made to access a nonexistent directory."

Action: Retry the operation with a directory that exists.

ASMCMD-09496: The Cluster Manifest File 'string' does not contain any components.

Cause: A Cluster Manifest File that does not contain any components was provided.

Action: Provide a valid Cluster Manifest File and retry the operation.

ASMCMD-09497: File 'string' is not a Cluster Manifest File.

Cause: The file provided was not a Cluster Manifest File.

Action: Provide a valid Cluster Manifest File and retry the operation.

ASMCMD-09498: The command is only supported on the Domain Services Cluster.

Cause: An attempt was made to run a command that is only supported on the Domain Services Cluster.

Action: Rerun the command on the Domain Services Cluster.

ASMCMD-09499: invalid member cluster version 'string'

Cause: An attempt to create a configuration for a member cluster failed because an invalid cluster version was provided for the cluster.

Action: Retry the operation, providing a valid member cluster version in the required format (%u.%u.%u.%u.%u).

ASMCMD-09500: member cluster version 'string' is incompatible with Domain Services Cluster version 'string'

Cause: The specified member cluster version was not supported by the Domain Services Cluster.

Action: Upgrade or downgrade the Domain Services Cluster to a version that is compatible with the member cluster version and retry the operation. Install a member cluster using a supported version. Refer to product documentation for a complete list of supported releases.

ASMCMD-09501: Clear timestamp for OS trail type requires RAC instance number

Cause: There was no RAC instance number specified to clear timestamp for OS trailtype

Action: Specify the RAC Instance number for OS trail type.

ASMCMD-09502: Set timestamp for OS trail type requires RAC instance number

Cause: RAC instance number was not specified while OS trail type was specified.

Action: Provide a RAC instance number for OS trail type for set timestamp operation.

ASMCMD-09511: failed to obtain required AFD disk string from Oracle Local Repository

Cause: The AFD disk string required for this operation could not be retrieved from the Oracle Local Repository (OLR).

Action: Check that Oracle Clusterware is properly configured using 'ocrcheck -local'. Ensure that ASMCMD afd\_dsset command is used to set AFD disk string before retrieving the value.

ASMCMD-09512: failed to update AFD disk string in Oracle Local Repository.

Cause: An error occurred while setting AFD disk string.

Action: Check that Oracle Clusterware is properly configured using 'ocrcheck -local'.

ASMCMD-09513: ASM disk label set operation failed.\\n

Cause: An error occurred while setting the ASM label.

Action: Examine the accompanying error messages and correct the problem indicated, then retry the afd\_label operation.

ASMCMD-09514: ASM disk label clear operation failed.\\n

Cause: An error occurred while clearing the ASM label.

Action: Examine the accompanying error messages and correct the problem indicated, then retry the afd\_unlabel operation.

ASMCMD-09515: KFOD executable not found at 'string'

Cause: The KFOD executable was not found at the indicated location.

Action: Contact Oracle Support Services.

ASMCMD-09516: AFDTOOL executable not found at 'string'

Cause: The AFDTOOL executable was not found at the indicated location.

Action: Contact Oracle Support Services.

ASMCMD-09517: AFDROOT executable not found at 'string'

Cause: The AFDROOT executable was not found at the indicated location.

Action: Contact Oracle Support Services.

ASMCMD-09518: AFDDRIVERSTATE executable not found at 'string'

Cause: The AFDDRIVERSTATE executable was not found at the indicated location.

Action: Contact Oracle Support Services.

ASMCMD-09519: ASMLib is present with ASM disk string 'string'; command requires default ASM disk string

Cause: An attempt was made to configure AFD when ASMLib was present. To configure AFD when ASMLib is present, the ASM disk string needs to be a default string. Otherwise, when the Oracle Clusterware stack is restarted, the AFD devices cannot be discovered.

Action: Use a SQL command or ASMCMD command to set the ASM disk string to be default empty string. Refer to the product documentation and follow the procedure to configure AFD.

ASMCMD-09520: AFD is not 'string'

Cause: The Oracle ASM Filter Driver (AFD) was either not supported, not installed, or not loaded.

Action: If attempting to pre-label the devices, then use the --init option. Otherwise, contact Oracle Support Services.

ASMCMD-09521: AFD is already configured

Cause: AFD was already configured and loaded on the node.

Action: Run the command when AFD is not configured. Refer to the product documentation and follow the procedure to configure AFD.

ASMCMD-09522: Insufficient permission to execute the command. Require privileged user

Cause: A non-privileged user attempted to execute a command requiring privileges.

Action: Issue the command again as a privileged user.

ASMCMD-09523: command cannot be used when Oracle Clusterware stack is up

Cause: The command was executed when the Oracle Clusterware stack was up.

Action: Stop Oracle Clusterware using 'crsctl stop crs' command and retry.

ASMCMD-09524: AFD configuration failed 'string'

Cause: The afd\_configure command was not successful.

Action: Examine the accompanying error messages, correct the problem indicated and then retry the command. Check ASMCMD alert log for more information.

ASMCMD-09525: AFD deconfiguration failed 'string'

Cause: The afd\_deconfigure command was not successful.

Action: Examine the accompanying error messages, correct the problem indicated and then retry the command. Check ASMCMD alert log for more information.

ASMCMD-09526: The AFD state is 'string' and filtering is 'string' on host 'string'

Cause: User requested to retrieve the status of AFD on the node.

Action: Note the status of AFD and its filtering mode.

ASMCMD-09527: AFD is loaded, but resource ora.driver.afd does not exist

Cause: The command was executed with AFD loaded on the node but its OHASD resource ora.driver.afd did not exist.

Action: Forcibly configure AFD using the 'ASMCMD afd\_configure -f' command.

ASMCMD-09528: disk 'string' does not exist

Cause: The disk specified did not exist.

Action: Specify a disk that exists.

ASMCMD-09529: The executable 'string' is either not found or non-executable in the\\nlocation(s) string

Cause: The executable file is either not found or non executable in the specified location(s). It must be available in any one of the specified location(s).

Action: Contact Oracle Support Services.

ASMCMD-09530: The AFD state is 'string'

Cause: User requested to retrieve the status of AFD.

Action: Note the status of AFD. AFD is functional if the state is LOADED.

ASMCMD-09531: External redundancy disk groups cannot contain sites.

Cause: The tag site was not compatible with the external redundancy disk groups.

Action: Do not use site tags when the command is applied to an external disk group.

ASMCMD-09532: command cannot be used when Oracle Clusterware stack is down

Cause: The command was executed when the Oracle Clusterware stack was down.

Action: Start Oracle Clusterware using 'crsctl start crs' command and retry.

ASMCMD-09533: resource ora.driver.afd does not exist

Cause: The command was executed when OHASD resource ora.driver.afd did not exist.

Action: Verify the status of AFD using the 'ASMCMD afd\_state' command.

ASMCMD-09534: Discovery string is not provided.

Cause: The discovery string was not provided and the stamp operation was not permitted.

Action: Provide a discovery string adding the option '--dscstr' to the command 'asmcmd stamp'.

ASMCMD-09535: Failure group label is not provided.

Cause: An attempt was made to stamp a site label without providing a failure group label.

Action: Provide a failure group label adding the option '--failgroup' to the command 'asmcmd stamp'.

ASMCMD-09536: The site label 'string' is invalid.

Cause: An invalid site label was supplied.

Action: Specify a site name which is at least one character but no more than 15 characters in length. A site name consists of alphanumeric characters plus the hyphen character (a..z, A..Z, 0..9, -). It cannot begin with a numeric character. It cannot begin or end with the hyphen (-) character.

ASMCMD-09537: The failure group label 'string' is invalid.

Cause: An invalid failure group label was supplied.

Action: Specify a failure group label that is a valid SQL identifier. It must be at least one character in length but no more than 30 characters in length. It must begin with a letter and is composed of letters, digits, and the underscore (\_) character.

ASMCMD-09538: The disk label 'string' is invalid.

Cause: An invalid disk label was supplied.

Action: Specify a disk label that is a valid SQL identifier. It must be at least one character in length but no more than 23 characters in length. It must begin with a letter and is composed of letters, digits, and the underscore (\_) character.

ASMCMD-09539: No disks were discovered using the string 'string'.

Cause: The supplied discovery string did not match any disk.

Action: Provide a valid discovery string.

ASMCMD-09540: Disks are managed by AFD or ASMLIB.

Cause: An attempt was made to stamp the disk label on disks that are managed by Oracle ASM Filter Driver (AFD) or ASMLIB."

Action: Provide a discovery string for disks that are not managed by AFD or ASMLIB, or do not provide the disk label, and retry the command.

ASMCMD-09541: Disk string belongs to mounted disk group string.

Cause: An attempt was made to stamp a disk that belongs to a mounted disk group.

Action: Dismount the disk group and retry the command.

ASMCMD-09542: Disk string is member of disk group string and ASMCMD is not connected to an instance.

Cause: An attempt was made to stamp a disk that is a member of an ASM disk group, and ASMCMD was not connected to an ASM instance to verify if that disk group was mounted.

Action: Connect ASMCMD to an ASM instance and retry the command.

ASMCMD-09543: cannot rename the site and the failgroup for a disk

Cause: An attempt was made to rename the site and the failgroup for a disk. The operation was not permitted because these options are mutually exclusive, since the failgroup can be renamed only if the disk group redundancy is external and the site cannot be renamed if the disk group redundancy is external.

Action: Provide only one of the two options: 'site' or 'failgroup'.

ASMCMD-09544: The command is not supported on a member cluster.

Cause: An attempt was made to run a command that was not supported on a member cluster.

Action: Rerun the command on the storage server.

ASMCMD-09545: The installed AFD drivers are not correct for this operating system.

Cause: A request to retrieve the status of Oracle ASM Filter Driver (AFD) was made. The installed AFD drivers and the current running operating system were not compatible.

Action: Contact Oracle Support Services.

ASMCMD-09546: Insufficient permission to execute the command. The command requires an Oracle Grid Infrastructure user.

Cause: An attempt was made to execute a command by a user who was not an Oracle Grid Infrastructure user.

Action: Rerun the command as an Oracle Grid Infrastructure user.

ASMCMD-09547: Oracle Automatic Storage Management (Oracle ASM) disk unmanage operation failed.

Cause: An error occurred while attempting to remove a disk from Oracle ASM Filter Driver (Oracle ASMFD).

Action: Examine the accompanying error messages and correct the problem.

ASMCMD-09601: ASM Client Cluster creation failed because the access mode specified is invalid.

Cause: An invalid access mode was supplied in an attempt to create an ASM Client Cluster.

Action: Rerun the command by specifying the correct access mode.

ASMCMD-09602: The command is not supported on a Domain Services Cluster.

Cause: An attempt was made to run a command that was not supported on a Domain Services Cluster.

Action: Contact Oracle Support Services.

ASMCMD-09603: The command is not supported on a Standalone Cluster.

Cause: An attempt was made to run a command that was not supported on a Standalone Cluster.

Action: Refer to the command line help or to the documentation or Contact Oracle Support Services

ASMCMD-09604: The command is only supported on a Cluster that has ASM configured locally.

Cause: An attempt was made to run a command that is only supported on the Cluster that has ASM configured locally.

Action: Rerun the command on the Cluster that has ASM configured locally.