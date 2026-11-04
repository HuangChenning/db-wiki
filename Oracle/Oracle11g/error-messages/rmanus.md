---
title: RMAN-00201 to RMAN-20514
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/rmanus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 46 RMAN-00201 to RMAN-20514

RMAN-00201: Do you really want to execute the above repair (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00202: Do you want to open the database (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00203: Do you want to open resetlogs the database (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00204: Do you really want to delete the above objects (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00205: Do you really want to drop all backups and the database (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00206: Do you really want to drop the database (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00207: Do you really want to unregister the database (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00208: Want to unregister the database with target db\_unique\_name (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00209: Do you really want to change the above failures (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00210: Do you really want to catalog the above files (enter YES or NO)?

Cause: This is a user prompt.

Action: Answer the question to proceed.

RMAN-00211: Error occurred getting response - assuming NO response

Cause: An error occurred reading user response.

Action: No action is required, this is an informational message only.

RMAN-00212: "string" is an invalid response - please re-enter.

Cause: An incorrect response was entered.

Action: Enter a correct response.

RMAN-00550: parser package failed to load

Cause: lpmloadpkg() return an error indication.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-00551: initialization of parser package failed

Cause: The parser package initialization routine returned an error.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-00552: syntax error in command line arguments

Cause: The arguments supplied to RMAN could not be parsed, or no arguments were supplied at all.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-00553: internal recovery manager package failed to load

Cause: lpmloadpkg() return an error indication.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-00554: initialization of internal recovery manager package failed

Cause: The internal package initialization routine returned an error.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-00555: target database connect string must be specified

Cause: The TARGET parameter was not specified.

Action: Supply the necessary parameter.

RMAN-00556: could not open CMDFILE "string"

Cause: An error occurred when trying to open the file.

Action: Check that the file name was specified correctly and that the file exists and that the user running RMAN has read permission for the file.

RMAN-00557: could not open MSGLOG "string"

Cause: An error occurred when trying to open the file.

Action: Check that the file name was specified correctly and that the file exists and that the user running RMAN has write permission for the file.

RMAN-00558: error encountered while parsing input commands

Cause: The parser detected a syntax error.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-00562: username too long

Cause: The specified user name exceeds the maximum allowable username length.

Action: Correct the username.

RMAN-00563: password too long

Cause: The specified password exceeds the maximum allowable password length.

Action: Correct the password.

RMAN-00564: host data too long

Cause: The SQL\*NET host connect string exceeds the maximum allowable length.

Action: Correct the host string.

RMAN-00565: unable to read input file

Cause: An error occurred while trying to read from STDIN or from the CMDFILE.

Action: Ensure that the cmdfile is readable. The cmdfile must be a text file with 1 line per record.

RMAN-00566: could not open TRACE "string"

Cause: An error occurred when trying to open the file.

Action: Check that the file name was specified correctly and that the user running RMAN has write permission for the file.

RMAN-00567: Recovery Manager could not print some error messages

Cause: An error occurred while trying to print the error message stack.

Action: If the associated error message indicates a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-00568: user interrupt received

Cause: The user typed ^C or ATTN.

Action: No action is required.

RMAN-00569: =============== ERROR MESSAGE STACK FOLLOWS ===============

Cause: This message precedes an error message stack.

Action: The errors are printed in last-in first-out order. To interpret them correctly, read from the bottom to the top.

RMAN-00570: \*\*end-of-file\*\*

Cause: The end of an inline cmdfile was reached. This is just an informational message.

Action: No action is required.

RMAN-00571: ===========================================================

Cause: Displayed to highlight the error message stack.

Action: The errors are printed in last-in first-out order. To interpret them correctly, read from the bottom to the top.

RMAN-00572: waiting for DBMS\_PIPE input

Cause: This message is used only when the PIPE option was specified.

Action: enqueue some RMAN input into the pipe

RMAN-00573: DBMS\_PIPE.NEXT\_ITEM\_TIME returned unknown type code: number

Cause: This is an internal error.

Action: contact Oracle Support Services.

RMAN-00574: rman aborting due to errors reading/writing DBMS\_PIPE

Cause: RMAN was run with input/output being sent to DBMS\_PIPE. An error was encountered while reading from or writing to the pipe. This error should be preceded by information describing the error.

Action: RMAN terminates. Refer to the cause/action for the preceding errors.

RMAN-00575: timeout while trying to write to DBMS\_PIPE

Cause: d by death of the process that was talking to rman.

Action: RMAN will abort.

RMAN-00576: PIPE cannot be used with CMDFILE

Cause: The PIPE and CMDFILE options cannot be used together. When using the PIPE option, RMAN must obtain its input from the input pipe.

Action: Remove either the PIPE or CMDFILE option.

RMAN-00577: PIPE requires that TARGET be specified on the command line

Cause: The PIPE option obtains its input from, and writes its output to, an Oracle database pipe in the target database. Therefore, the target database connection must be specified on the command line, so that RMAN can connect to the target database to receive its input from the pipe.

Action: Specify the TARGET option on the RMAN command line.

RMAN-00578: pipe string is not private and owned by SYS

Cause: The pipe that RMAN needs to use for its input or output is either a public pipe or a private pipe that is not owned by SYS. This is a potential security problem, because it allows a non-SYS user to issue commands to RMAN or to retrieve the RMAN output.

Action: If you are attempting to put data on the RMAN input pipe prior to starting RMAN, so RMAN will process the data on the pipe as soon as it starts, you must be connected as SYS and you must first use the DBMS\_PIPE.CREATE\_PIPE function to explicitly create the pipe as a private pipe.

RMAN-00579: SCRIPT cannot be used with CMDFILE

Cause: The SCRIPT and CMDFILE options cannot be used together. When using the SCRIPT option, RMAN executes only the specified script.

Action: Remove either the SCRIPT or CMDFILE option.

RMAN-00600: internal error, arguments \[string\] \[string\] \[string\] \[string\] \[string\]

Cause: An internal error in recovery manager occurred.

Action: Contact Oracle Support Services.

RMAN-00601: fatal error in recovery manager

Cause: A fatal error has occurred.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-00700: SCRIPT requires that TARGET be specified on the command line

Cause: A SCRIPT option was included on the RMAN command line without a specified TARGET database.

Action: Specify the TARGET option on the RMAN command line.

RMAN-00701: SCRIPT requires that CATALOG be specified on the command line

Cause: A SCRIPT option was included on the RMAN command line without a specified CATALOG recovery catalog.

Action: Specify the CATALOG option on the RMAN command line.

RMAN-00702: The command has no syntax errors

Cause: This is an informational message only.

Action: No action is required.

RMAN-00703: The cmdfile has no syntax errors

Cause: This is an informational message only.

Action: No action is required.

RMAN-01006: error signaled during parse

Cause: An error was signaled during parsing.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-01007: at line number column number file: string

Cause: This is an informational message indicating the line and column where a syntax error was detected.

Action: No action is required.

RMAN-01008: the bad identifier was: string

Cause: This is an informational message indicating the identifier token that caused a syntax error.

Action: No action is required.

RMAN-01009: syntax error: found "string": expecting one of: "string"

Cause: A syntax error was signaled during parsing.

Action: Correct the input.

RMAN-02000: wrong message file version (msg number not found)

Cause: The rmanxx.msb file is not the correct version.

Action: Check that the installation was done correctly. The RMAN binary (executable, load module, whatever it is called on your O/S) and the rmanxx.msb file must be from the same version, release, and patch level.

RMAN-02001: unrecognized punctuation symbol "string"

Cause: An illegal punctuation character was encountered.

Action: Remove the illegal character.

RMAN-02002: unexpected end of input file reached

Cause: This is probably caused by failure to supply the closing quote for a quoted string.

Action: Correct the input.

RMAN-02003: unrecognized character: string

Cause: An input character that is neither an alpha, digit, or punctuation was encountered.

Action: Remove the character.

RMAN-02004: quoted string too big

Cause: A quoted string longer than 2000 bytes was encountered.

Action: This may be caused by a missing close quote. If so, add the missing quote, otherwise shorten the string.

RMAN-02005: token too big

Cause: A token longer than 1000 bytes was encountered

Action: Tokens must be separated by whitespace or punctuation. Either add the missing whitespace or punctuation, or shorten the token.

RMAN-02006: script line too long

Cause: a line longer than 500 bytes was encountered

Action: break the line up into shorter lines

RMAN-02007: Integer value overflow

Cause: Parser failed to convert input string to integer

Action: Acceptable values for integer are from 0 to 2147483648. Retry command using valid integer value.

RMAN-02008: no value exists for variable "string"

Cause: The RMAN variable specified was either undefined or null

Action: Verify that a proper value has been given to that variable.

RMAN-02009: unexpected end of command file reached

Cause: This is probably caused by failure to supply the closing brace for a stored script in a command file.

Action: Correct the input.

RMAN-03000: recovery manager compiler component initialization failed

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-03001: recovery manager command sequencer component initialization failed

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-03002: failure of string command at string

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-03003: command not implemented yet: string

Cause: The command is not implemented in the current release.

Action: Avoid using the command.

RMAN-03004: fatal error during execution of command

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-03008: error while performing automatic resync of recovery catalog

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-03009: failure of string command on string channel at string

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-03010: fatal error during library cache pre-loading

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-03011: Recovery Managerstring

Action: No action is required.

RMAN-03012: fatal error during compilation of command

Cause: A fatal error occurred during compilation of a command.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-03013: Copyright (c) 1995, 2003, Oracle Corporation. All rights reserved.

Action: No action is required.

RMAN-03014: implicit resync of recovery catalog failed

Cause: of the failure.

Action: No action is required.

RMAN-03015: error occurred in stored script string

Cause: This is an informational message only.

Action: No action is required.

RMAN-03017: recursion detected in stored script string

Cause: A stored script is calling itself or another script which calls itself.

Action: Remove the recursion.

RMAN-03018: asynchronous RPCs are working correctly

Cause: This is an informational message only.

Action: No action is required.

RMAN-03019: asynchronous RPCs are NOT working

Cause: The RPCTEST command has determined that RPCs are not executing asynchronously. Instead, they are blocking. This is caused by using a SQL\*NET driver that does not support non-blocking UPI.

Action: Try using a different SQL\*NET driver.

RMAN-03020: asynchronous RPC test will take 1 minute

Cause: This is an informational message only.

Action: No action is required.

RMAN-03023: executing command: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-03028: fatal error code for command string: number

Cause: Informational message. This precedes error 3012.

Action: No action is required.

RMAN-03029: echo set on

Cause: a SET ECHO ON command was issued

Action: No action is required.

RMAN-03030: echo set off

Cause: a SET ECHO OFF command was issued

Action: No action is required.

RMAN-03031: this option of set command needs to be used inside a run block

Cause: The option used with the SET command is not valid outside a run block.

Action: Change the SET command or place it inside a run block.

RMAN-03032: this option of set command needs to be used outside of a run block

Cause: The option used with the SET command is not valid inside of a run block.

Action: Change the SET command or place it outside a run block.

RMAN-03033: current log archived

Cause: "ALTER SYSTEM ARCHIVE LOG CURRENT" command completed successfully.

Action: None, this is an informational message.

RMAN-03034: LEVEL number is invalid. LEVEL must be between string and string

Cause: An invalid DEBUG LEVEL was used.

Action: Change the DEBUG LEVEL argument.

RMAN-03035: Debugging turned off

Cause: a DEBUG OFF command was issued

Action: No action is required.

RMAN-03036: Debugging set to level=number, types=string

Cause: a DEBUG command was issued

Action: No action is required.

RMAN-03037: Spooling started in log file: string

Cause: a SPOOL LOG TO... command was issued

Action: No action is required.

RMAN-03038: Spooling started in trace file: string

Cause: a SPOOL TRACE TO... command was issued

Action: No action is required.

RMAN-03039: Spooling for log turned off

Cause: a SPOOL LOG OFF command was issued

Action: No action is required.

RMAN-03040: Spooling for trace turned off

Cause: a SPOOL TRACE TO... command was issued

Action: No action is required.

RMAN-03042: error while analyzing automatic repair options

Cause: of the failure.

Action: No action is required.

RMAN-03090: Starting string at string

Cause: This is an informational message only.

Action: No action is required.

RMAN-03091: Finished string at string

Cause: This is an informational message only.

Action: No action is required.

RMAN-03098: stringRMAN-number: stringstring

Cause: This is the message prefix with a possible indentation.

Action: No action is required.

RMAN-03099: job cancelled at user request

Cause: The user interrupted the current job.

Action: None

RMAN-03999: Oracle error occurred while while converting a date: ORA-number: string

Cause: Internal error converting a date.

Action: Contact Oracle Support Services.

RMAN-04000: memory allocation failure

Cause: A memory allocation request could not be satisfied.

Action: Increase the amount of memory available to RMAN.

RMAN-04001: heap initialization failure

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04002: OCIPI failed, ORA-string

Cause: OCI process level initialization failed.

Action: This error should not normally occur.

RMAN-04003: OCIINIT failed

Cause: The call to OCIEnvInit failed.

Action: This error should not normally happen. Contact Oracle Customer Support.

RMAN-04004: error from recovery catalog database: string

Cause: Oracle error signaled by catalog database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04005: error from target database: string

Cause: Oracle error signaled by target database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04006: error from auxiliary database: string

Cause: Oracle error signaled by auxiliary database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04007: WARNING from recovery catalog database: string

Cause: Non fatal Oracle error signaled by catalog database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04008: WARNING from target database: string

Cause: Non fatal Oracle error signaled by target database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04009: WARNING from auxiliary database: string

Cause: Non fatal Oracle error signaled by auxiliary database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04010: target database Password:

Cause: No password was provided for the target database.

Action: Provide target database password.

RMAN-04011: recovery catalog database Password:

Cause: No password was provided for the recovery catalog database.

Action: Provide recovery catalog database password.

RMAN-04012: auxiliary database Password:

Cause: No password was provided for the auxiliary database.

Action: Provide auxiliary database password.

RMAN-04013: must connect before startup

Cause: A STARTUP command was attempted before connecting to the database.

Action: Connect to database before attempting STARTUP command.

RMAN-04014: startup failed: string

Cause: The database failed to startup.

Action: The cause of the failure is included in the error message. Correct the cause of the failure and retry the startup command.

RMAN-04015: error setting target database character set to string

Cause: An error was received while setting the session character set in the target database.

Action: This error should not normally happen. Contact Oracle Customer Support.

RMAN-04016: could not get OCI error handle

Cause: An error was received while initializing the OCI layer.

Action: This error should not normally happen. Contact Oracle Customer Support.

RMAN-04017: startup error description: string

Cause: of failure.

Action: No action is required.

RMAN-04020: target database name "string" does not match channel's name: "string"

Cause: The CONNECT clause in the ALLOCATE command has resulted in a connection to a database which is not the same as the one used to connect to the target database.

Action: Verify that the CONNECT string connects to the same database as the one specified in the TARGET connection for the CONNECT command.

RMAN-04021: target database DBID string does not match channel's DBID string

Cause: The CONNECT clause in the ALLOCATE command has resulted in a connection to a database which is not the same as the one used to connect to the target database.

Action: Verify that the CONNECT string connects to the same database as the one specified in the TARGET connection for the CONNECT command.

RMAN-04022: target database mount id string does not match channel's mount id string

Cause: The CONNECT clause in the ALLOCATE command has resulted in a connection to a database which is not the same as the one used to connect to the target database.

Action: Verify that the CONNECT string connects to the same database as the one specified in the TARGET connection for the CONNECT command.

RMAN-04024: starting Oracle instance without parameter file for retrieval of spfile

Cause: The instance could not be started because no default parameter file (either PFILE or SPFILE) could be found. The instance will be started in restricted mode with default parameters.

Action: None - this is an informational message.

RMAN-04025: unable to generate a temporary file

Cause: Creation of a temporary file failed. If could be that the system does not have enough resources (disk space, memory or similar).

Action: Verify and free some system resources memory and try again.

RMAN-04026: unable to open a temporary file: "string"

Cause: Opening of a temporary file failed. If could be that the system does not have enough resources (disk space, memory or similar).

Action: Verify and free some system resources memory and try again.

RMAN-04027: unable to write to a temporary file: "string"

Cause: Writing to a temporary file failed. If could be that the system does not have enough resources (disk space, memory or similar).

Action: Verify and free some system resources memory and try again.

RMAN-04031: initialization parameters used for automatic instance: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-04032: using contents of file string

Cause: The specified file was included as part of the auxiliary database parameter file. This is an informational message.

Action: No action is required.

RMAN-04033: cannot open auxiliary parameter file string

Cause: An auxiliary parameter file was specified with SET AUXILIARY INSTANCE PARAMETER FILE command but the specified file cannot be found.

Action: Set the parameter file to an existent file or retry the command without setting AUXILIARY INSTANCE PARAMETER FILE.

RMAN-04034: source recovery catalog database Password:

Cause: A password was not provided for the source recovery catalog database.

Action: Provide source recovery catalog database password.

RMAN-04035: error from source recovery catalog database: string

Cause: Oracle error signaled by source recovery catalog database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-04036: WARNING from source recovery catalog database: string

Cause: Nonfatal Oracle error signaled by source recovery catalog database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-05000: CONFIGURE AUXNAME required for datafile string

Cause: Either: -) The control file mounted by the auxiliary database does not have an entry for this datafile, therefore file name conversion is not possible. -) A COPY DATAFILE TO AUXNAME command was issued, but no auxname was set for this datafile.

Action: Use the CONFIGURE AUXNAME command to specify a file name that the auxiliary database can use as a restore destination.

RMAN-05001: auxiliary file name string conflicts with a file used by the target database

Cause: RMAN is attempting to use the specified file name as a restore destination in the auxiliary database, but this name is already in use by the target database.

Action: Use the CONFIGURE AUXNAME command to specify a name for the data file that does not conflict with a file name in use by the target db.

RMAN-05002: aborting Tablespace Point-in-Time Recovery

Cause: Previously encountered error(s) were issued which require corrective action.

Action: Resolve the error conditions, and then re-issue the RECOVER command.

RMAN-05003: Tablespace Point-in-Time Recovery is not allowed for tablespace string

Cause: The SYSTEM, SYSUAX or a tablespace containing rollback segments is not allowed in Tablespace Point-in-Time Recovery.

Action: Remove the indicated tablespace from the recovery set and retry the operation.

RMAN-05004: target database log mode is NOARCHIVELOG

Cause: An attempt was made to apply Tablespace Point-in-Time Recovery to a database that is in NOARCHIVELOG mode.

Action: If all required archived log files are available for Tablespace Point-in-Time Recovery, alter the target database log mode to ARCHIVELOG and retry the Tablespace Point-in-Time Recovery operation. Otherwise, Tablespace Point-in-Time Recovery cannot be applied to this database.

RMAN-05005: Tablespace Point-in-Time Recovery is not allowed for re-created tablespace string

Cause: The requested tablespace has been re-created and is not allowed in Point-in-Time Recovery.

Action: Remove the indicated tablespace from the recovery set and retry the operation.

RMAN-05006: cannot recover clone standby single tablespaces

Cause: Standby recover can only be performed for the whole database.

Action: Change the tablespace list to a database specification.

RMAN-05007: no channel allocated

Cause: A command was entered that requires a channel, and no channel is allocated.

Action: Use ALLOCATE CHANNEL before using the command

RMAN-05009: Block Media Recovery requires Enterprise Edition

Cause: The RECOVER...BLOCK command was specified.

Action: Remove the RECOVER...BLOCK command.

RMAN-05010: target database must be opened in READ WRITE mode for Tablespace Point-in-Time Recovery

Cause: The target database was not opened in read write mode.

Action: Open the database in read write mode.

RMAN-05011: auxiliary instance must be in NOMOUNT state for Tablespace Point-in-Time Recovery

Cause: The Auxiliary instance was not in NOMOUNT state.

Action: Open the auxiliary instance in NOMOUNT state.

RMAN-05013: auxiliary control file name string conflicts with a file used by the target database

Cause: RMAN is attempting to use the specified control file name for Tablespace Point-in-Time Recovery as a restore destination in the auxiliary database, but this name is already in use by the target database.

Action: Set control\_files parameter in the auxiliary instance to a name that does not conflict with a file name in use by the target database.

RMAN-05014: Tablespaces with undo segments were not found in recovery catalog

Cause: The recovery catalog did not have information about tablespaces with undo segments.

Action: Manually specify the tablespaces with undo segments in the optional UNDO tablespaces clause of the RECOVER command.

RMAN-05015: WARNING: not enough information in recovery catalog for specified point-in-time recovery

Cause: The recovery catalog did not have information about the tablespaces with undo segments at the specified Point-in-Time. This happened because the current recovery catalog was not in use at the specified Point-in-Time. A list of tablespaces with undo segments was supplied.

Action: RMAN assumes that the current set of tablespaces with undo segments is the same set that was in use at the specified Point-in-Time. If the set of tablespaces with undo segments changes, the recovery fails. If recovery fails, use the optional UNDO TABLESPACE clause of the RECOVER command to specify the correct set of tablespaces.

RMAN-05016: failover to previous backup

Cause: This is an informational message to indicate the RMAN could not successfully restore the files using the specified backups. An attempt was made to restore the datafile/archived logs/ control file/SPFILE using a previous existing backup.

Action: See accompanying additional error messages indicating the cause of the failover.

RMAN-05017: no copy of datafile number found to recover

Cause: A RECOVER COPY command was not able to proceed because no copy of indicated file was found to recover. Possible causes include the following:

1\. no copy of indicated file exists on disk that satisfy the criteria specified in the user's recover operands.

2\. copy of indicated datafile exists on disk but no incremental backup was found to apply to the datafile copy.

Action: One of the following:

1\. Use or correct TAG specification to recover a different datafile copy.

2\. Use BACKUP FOR RECOVER OF COPY command to create necessary incremental backup or copy.

RMAN-05018: some datafile copies cannot be recovered, aborting the RECOVER command

Cause: This error message can follow one or more RMAN-5017 or RMAN-5019 error messages.

Action: See RMAN-5017 or RMAN-5019 error messages documentation for more information.

RMAN-05019: WARNING: no channel of required type allocated to recover copy of datafile number

Cause: A RECOVER COPY command could not proceed because incremental backup sets exist on a device type that has not been allocated.

Action: Use the LIST command to determine which device type is needed, then allocate a channel of that type.

RMAN-05020: cannot specify AUXILIARY DESTINATION option for normal recovery

Cause: The AUXILIARY DESTINATION option was specified for a normal recovery. It is only allowed for Tablespace Point-in-Time Recovery.

Action: Remove the AUXILIARY DESTINATION option and re-run the RECOVER command.

RMAN-05021: this configuration cannot be changed for a BACKUP or STANDBY control file

Cause: The user attempted to modify the configuration which cannot be changed for a BACKUP or STANDBY control file while the mounted control file was either BACKUP or STANDBY. The following configurations can be changed only when connected to primary database instance that has CURRENT/CREATED control file type mounted: CONFIGURE RETENTION POLICY CONFIGURE EXCLUDE CONFIGURE ENCRYPTION CONFIGURE DB\_UNIQUE\_NAME

Action: Connect to primary database instance and execute the command.

RMAN-05022: TRANSPORT TABLESPACE may not be used with user-managed auxiliary instance

Cause: A user-managed auxiliary instance was specified.

Action: Retry the operation with an RMAN-managed auxiliary instance.

RMAN-05023: TABLESPACE DESTINATION required

Cause: A required TABLESPACE DESTINATION was not specified.

Action: Specify a TABLESPACE DESTINATION and retry the operation.

RMAN-05024: List of tablespaces presumed to have UNDO segments

Cause: Accompanying message to 5015.

Action: See action of message 5015.

RMAN-05025: Tablespace string

Cause: Accompanying message to 5015.

Action: See action of message 5015.

RMAN-05026: WARNING: presuming following set of tablespaces applies to specified point-in-time

Cause: RMAN assumes that the current set of tablespaces with undo segments is the same set that was in use at the specified Point-in-Time. If the set of tablespaces with undo segments changes, the recovery fails. If recovery fails, use the optional UNDO TABLESPACE clause of the RECOVER command to specify the correct set of tablespaces.

Action: RMAN assumes that the current set of tablespaces with undo segments is the same set that was in use at the specified Point-in-Time. If the set of tablespaces with undo segments changes, the recovery fails. If recovery fails, use the optional UNDO TABLESPACE clause of the RECOVER command to specify the correct set of tablespaces.

RMAN-05027: List of tablespaces expected to have UNDO segments

Cause: Accompanying message to 5026.

Action: See action of message 5026.

RMAN-05028: Tablespace string

Cause: Accompanying message to 5026.

Action: See action of message 5026.

RMAN-05029: UNDO TABLESPACE clause is only valid for Tablespace Point-in-Time Recovery

Cause: The UNDO TABLESPACE clause was specified for non-Tablespace Point-in-Time Recovery.

Action: Remove the UNDO TABLESPACE clause.

RMAN-05030: CLONE clause cannot be used with Tablespace Point-in-Time Recovery

Cause: The CLONE clause was specified for a Tablespace Point-in-Time Recovery.

Action: Remove the CLONE clause.

RMAN-05031: cannot specify UNDO TABLESPACE clause for normal recovery

Cause: The UNDO TABLESPACE clause was specified for a normal recovery. It is only allowed for Tablespace Point-in-Time Recovery.

Action: Remove the UNDO TABLESPACE clause and re-run the RECOVER command.

RMAN-05032: datafile string will be created automatically during restore operation

Cause: The specified datafile did not have an available backup.

Action: None. This is an informational message displayed for VALIDATE or PREVIEW option of the RESTORE command.

RMAN-05033: Media recovery start SCN is string

Cause: The above system change number (SCN) would be starting media recovery SCN, if the specified files are restored.

Action: None. This is an informational message displayed for PREVIEW option of the RESTORE command.

RMAN-05034: Recovery must be done beyond SCN string to clear datafile fuzziness

Cause: The above system change number (SCN) identifies the minimum SCN beyond which the media recovery must be performed on the specific datafile to clear the media recovery fuzziness for all datafile.

Action: None. This is an informational message displayed for PREVIEW option of the RESTORE command.

RMAN-05035: archived logs generated after SCN string not found in repository

Cause: The recovery catalog or target database control file did not have a record of archived logs containing the redo generated after the specified system change number (SCN).

Action: None. To avoid this message, perform a log switch if the database is in open mode.

RMAN-05036: FOR DB\_UNIQUE\_NAME option cannot be used for this configuration

Cause: An attempt was made to set the configuration which cannot be used with FOR DB\_UNIQUE\_NAME option.

Action: Remove FOR DB\_UNIQUE\_NAME option and execute the command.

RMAN-05037: FOR DB\_UNIQUE\_NAME option cannot be used in nocatalog mode

Cause: An attempt was made to set the remote configuration in nocatalog mode.

Action: Connect to recovery catalog and execute the command.

RMAN-05038: unable to determine UNTIL SCN for TRANSPORT

Cause: No archived logs were found in the control file.

Action: Add UNTIL clause to TRANSPORT command and retry.

RMAN-05039: One or more auxiliary set datafiles could not be removed

Cause: There was an error while performing Tablespace Point-in-Time Recovery. Some of the restored datafiles had OMF names and were not deleted.

Action: Manually remove the auxiliary set datafiles that were not removed.

RMAN-05040: List of tablespaces that have been dropped from the target database:

Cause: One or more tablespaces in the recovery set were not found in the control file of the target database.

Action: None. Informational message.

RMAN-05041: Error during export of metadata

Cause: Export of metadata received an error from Data Pump.

Action: This message is accompanied by other error message(s) indicating the cause of the error.

RMAN-05042: Error during import of metadata

Cause: Import of metadata received an error from Data Pump.

Action: This message is accompanied by other error message(s) indicating the cause of the error.

RMAN-05043: Tablespace string

Cause: Accompanying message to 5040.

Action: See Action of message 5040.

RMAN-05044: Performing export of metadata...

Cause: This is an informational message only.

Action: No action is required.

RMAN-05045: Performing import of metadata...

Cause: This is an informational message only.

Action: No action is required.

RMAN-05046: Export completed

Cause: This is an informational message only.

Action: No action is required.

RMAN-05047: Import completed

Cause: This is an informational message only.

Action: No action is required.

RMAN-05048: specified file name string conflicts with a file used by the target database

Cause: The specified file name was already in use by another datafile in the database.

Action: Use SET NEWNAME command to specify a different name for the datafile that does not conflict with a file name in use by the target database.

RMAN-05049: datafile string is an Oracle Managed File, DB\_CREATE\_FILE\_DEST not set at target

Cause: A Tablespace Point-in-Time Recovery was attempted but the datafile is an Oracle Managed File and DB\_FILE\_CREATE\_DEST is not currently set for the target database.

Action: Specify DB\_FILE\_CREATE\_DEST for the target database or provide a NEWNAME for the specified datafile.

RMAN-05050: flashing back control file to SCN string

Cause: RESTORE command was issued with a SET UNTIL clause and Flashback Database enabled. The control file was flashed back to the SET UNTIL time.

Action: This is an informational message only.

RMAN-05051: analyzing automatic repair options; this may take some time

Cause: This is an informational message only.

Action: No action is required.

RMAN-05052: Repair string is not compatible with this version of RMAN.

Cause: The specified repair was not compatible with this version of Recovery Manager (RMAN).

Action: Use a newer version of the RMAN executable.

RMAN-05053: AUXILIARY DESTINATION is only valid when using a RMAN-managed auxiliary instance

Cause: AUXILIARY DESTINATION clause was specified while using an user-managed auxiliary instance.

Action: Do not specify AUXILIARY DESTINATION clause and retry the operation or use a RMAN-managed auxiliary instance.

RMAN-05054: recover block operand string cannot be used to recover datafile

Cause: The specified operand could not be used with RECOVER datafile command.

Action: Delete the invalid operand and retry the command.

RMAN-05055: recover datafile operand string cannot be used to recover block

Cause: The specified operand could not be used with RECOVER block command.

Action: Delete the invalid operand and retry the command.

RMAN-05060: block specifier must be specified to recover block

Cause: Block Specifier was not specified in the command.

Action: Specify block specifier and resubmit the command.

RMAN-05061: analyzing automatic repair options complete

Cause: This is an informational message only.

Action: No action is required.

RMAN-05062: image copy needs no roll forward

Cause: The image copy that would be rolled forward by the RECOVER COPY command is already more recent than the specified UNTIL time or system change number (SCN).

Action: Usually this is the result of a recent OPEN RESETLOGS operation, and no action is needed, because the daily backup strategy will start rolling this copy forward after it becomes old enough to be eligible for rolling forward. To force the copy to be rolled forward, specify a more recent UNTIL time or system change number (SCN).

RMAN-05070: Running TRANSPORT\_SET\_CHECK on recovery set tablespaces

Cause: This is an informational message only.

Action: No action is required.

RMAN-05071: TRANSPORT\_SET\_CHECK completed successfully

Cause: This is an informational message only.

Action: No action is required.

RMAN-05072: TRANSPORT\_SET\_CHECK failed

Cause: SYS.TS\_PITR\_CHECK was not empty for recovery set tablespaces.

Action: Fix dependencies before attempting TSPITR again.

RMAN-05073: Tablespace string creation SCN string is ahead of point-in-time SCN string

Cause: The tablespace was found in the control file but the creation system change number (SCN) of the datafile(s) is after the specified point-in-time. This can happen if a previous tablespace point-in-time recovery was performed, for the tablespace.

Action: If a previous TSPITR has been performed drop the tablespace and retry the command. Otherwise, verify the name of the tablespace and/or the point-in-time and resubmit the command.

RMAN-05074: Tablespace string does not exist at specified point-in-time SCN string

Cause: The tablespace was found in the control file but the creation system change number (SCN) of the datafile(s) is after the specified point-in-time.

Action: Verify the name of the tablespace and/or the point-in-time and resubmit the command.

RMAN-05115: Cross-platform INSTANT RESTORE is not supported.

Cause: An instant restore was specified using a data file copy from a different platform.

Action: Specify a different data file copy that is formatted for the same platform where the restore is taking place.

RMAN-05116: feature was not enabled: string

Cause: The specified fature is not enabled.

Action: Do not attempt to use this feature.

RMAN-05500: the auxiliary database must be not mounted when issuing a DUPLICATE command

Cause: A DUPLICATE command was issued, but the auxiliary database is mounted.

Action: Dismount the auxiliary database.

RMAN-05501: aborting duplication of target database

Cause: Previously encountered errors require corrective action.

Action: Resolve the error conditions, and reissue the DUPLICATE command.

RMAN-05502: the target database must be mounted when issuing a DUPLICATE command

Cause: A DUPLICATE command was issued, but the target database control file is not mounted.

Action: Mount the target database control file by issuing ALTER DATABASE MOUNT via Enterprise Manager or Server Manager.

RMAN-05503: at least one auxiliary channel must be allocated to execute this command

Cause: No auxiliary channels were allocated.

Action: Allocate an auxiliary channel.

RMAN-05504: at least two redo log files or groups must be specified for this command

Cause: Only one redo log file or group was specified

Action: Specify at least one more redo log file or group

RMAN-05505: auxiliary file name conversion of 'string' exceeds maximum length of string

Cause: When the given file name is converted to the name used for the auxiliary database, the converted name is larger than the maximum allowed file name.

Action: Change initialization parameter DB\_FILE\_NAME\_CONVERT to convert to a valid file name.

RMAN-05506: error during recursive execution

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-05507: standby control file checkpoint (string) is more recent than duplication point-in-time (string)

Cause: A DUPLICATE FOR STANDBY command was issued, but the checkpoint of the control file is more recent than the last archived log or the specified point-in-time.

Action: If an explicit point-in-time was specified, change it to be at least the control file checkpoint; otherwise archive (and backup/copy) the current log.

RMAN-05510: Duplicate finished

Cause: This is an informational message only.

Action: No action is required.

RMAN-05511: Datafile string skipped by request

Cause: This is an informational message only.

Action: No action is required.

RMAN-05512: Tablespace string cannot be skipped from duplication

Cause: The SYSTEM and SYSAUX tablespaces were not included in the DUPLICATE DATABASE. They must be present.

Action: Remove the SYSTEM and/or SYSAUX tablespace from the SKIP list and retry the operation.

RMAN-05513: cannot duplicate, control file is not current or standby

Cause: Target database did not have a current or standby control file. DUPLICATE requires the target database to have a current or standby control file.

Action: Open database to make control file current or connect to a different database before retrying the command.

RMAN-05514: Tablespace string has undo information, cannot skip

Cause: All tablespaces that have undo information must be included in the duplication.

Action: Remove the specified tablespace from the SKIP list and retry the operation.

RMAN-05515: Duplicate for standby does not allow the use of SET UNTIL

Cause: A SET UNTIL clause was specified for the command.

Action: Remove the SET UNTIL clause and try again.

RMAN-05516: duplicate operand specified: string

Cause: The specified operand appears more than once in the same DUPLICATE option list

Action: Delete the duplicated operand.

RMAN-05517: tempfile string conflicts with file used by target database

Cause: RMAN attempted to use the specified tempfile as a restore destination in the auxiliary database, but this name was already in use by the target database.

Action: Use the SET NEWNAME FOR TEMPFILE command to specify a name for the indicated tempfile, making sure that the new name does not conflict with a file name in use by target database. Alternatively, use DB\_FILE\_NAME\_CONVERT and retry the command.

RMAN-05518: Automatically adding tablespace string

Cause: This is an informational message only.

Action: No action is required.

RMAN-05519: WARNING: tablespace string is always included when duplicating

Cause: The SYSTEM and SYSAUX tablespaces were included in the DUPLICATE TABLESPACE command. They were automatically included by the command and did not need to be explicitly named.

Action: To avoid this warning,, remove the SYSTEM and/or SYSAUX tablespace from the tablespaces list and retry the operation.

RMAN-05520: database name mismatch, auxiliary instance has string, command specified string

Cause: The database name specified in the initialization parameter was not the same as the database name provided in the DUPLICATE command.

Action: Correct the database name in the command or adjust the database name of the auxiliary instance.

RMAN-05521: DUPLICATE without CATALOG and TARGET not open requires that UNDO TABLESPACE is specified

Cause: A DUPLICATE was attempted when target database was not open without connection to a recovery catalog. It is necessary that the list of tablespaces with undo segments is provided with the UNDO TABLESPACE clause.

Action: Retry the command specifying the list of tablespaces with undo segments using the UNDO TABLESPACE clause.

RMAN-05522: Skipping tablespace string

Cause: This is an informational message only.

Action: No action is required.

RMAN-05523: Tablespace string is read only and SKIP READONLY was specified

Cause: Conflicting parameters were provided.

Action: Remove SKIP READONLY or remove read-only tablespace from list of tablespaces to duplicate.

RMAN-05524: Tablespace string is offline

Cause: It was not possible to duplicate offline tablespaces.

Action: Remove offline tablespace from list or online tablespace to duplicate it.

RMAN-05525: SKIP TABLESPACE cannot be used when using DUPLICATE TABLESPACE

Cause: A SKIP TABLESPACE clause was specified for the command.

Action: Remove the SKIP TABLESPACE clause and try again.

RMAN-05526: datafile number not processed because file is OFFLINE IMMEDIATE

Cause: A DUPLICATE command omitted processing the indicated datafile because it is offline immediate. The tablespace to which this datafile belongs will also not be included. See message 5528.

Action: None, informational message only.

RMAN-05527: Tablespace string has one or more OFFLINE IMMEDIATE datafiles

Cause: It was not possible to duplicate a tablespace who had offline immediate tablespaces.

Action: Remove offending tablespace from list or recover datafile which are offline immediate in the tablespace before attempting the command again.

RMAN-05528: datafile number not processed because file belongs to tablespace with one or more offline immediate datafile (string)

Cause: A DUPLICATE command omitted processing the indicated datafile because it is part of a tablespace that has offline immediate datafile. See message 5526.

Action: No action is required. This is an informational message only.

RMAN-05529: WARNING: DB\_FILE\_NAME\_CONVERT resulted in invalid ASM names; names changed to disk group only.

Cause: It was not possible to convert ASM Oracle Managed Files names using DB\_FILE\_NAME\_CONVERT parameter. RMAN changed these invalid names to the converted disk group name instead.

Action: No action is required. This is an informational message only. If the automatic change is incorrect, use one of the following options instead of using DB\_FILE\_NAME\_CONVERT for ASM Oracle Managed Files: 1) use RMAN command SET NEWNAME for each Oracle Managed File. 2) set DB\_CREATE\_FILE\_DEST initialization parameter in auxiliary instance and not specify DB\_FILE\_NAME\_CONVERT.

RMAN-05530: an UNTIL TIME or SCN cannot be specified with FROM ACTIVE DATABASE

Cause: A DUPLICATE with FROM ACTIVE DATABASE was specified along with either a SET UNTIL statment or UNTIL clause on the command. This is not supported. A DUPLICATE FROM ACTIVE DATABASE always creates a copy as of the current time.

Action: Check the statement and remove the use of UNTIL.

RMAN-05531: a mounted database cannot be duplicated while datafiles are fuzzy

Cause: A DUPLICATE with FROM ACTIVE DATABASE command was specified while the database was mounted or open read-only. Unless the database is open read/write, the datafiles cannot be fuzzy.

Action: Open the database read/write, then shutdown cleanly before mounting.

RMAN-05532: PASSWORD FILE specified without FROM ACTIVE DATABASE

Cause: The PASSWORD FILE clause of the DUPLICATE command was specified but the FROM ACTIVE DATABASE clause was not. A password file can only be duplicated if the FROM ACTIVE DATABSE clause has been used.

Action: Remove the PASSWORD FILE clause from the command, or perform an online duplicate of the database by specifying the FROM ACTIVE DATABASE clause.

RMAN-05533: string is not supported on string database

Cause: The specified command is not supported on this type of database. The type of database can be STANDBY, CLONE, or RAC.

Action: Do not use the specified command against this database.

RMAN-05534: WARNING: LOG\_FILE\_NAME\_CONVERT resulted in invalid ASM names; names changed to disk group only.

Cause: It was not possible to convert ASM Oracle Managed Files names using LOG\_FILE\_NAME\_CONVERT parameter. RMAN changed these invalid names to the converted disk group name instead.

Action: If the automatic change is incorrect, use one of the following options instead of using LOG\_FILE\_NAME\_CONVERT for ASM Oracle Managed Files: 1) Use the LOGFILE clause for online log files. 2) After DUPLICATE completes, create standby log files using the SQL ALTER DATABASE ADD STANDBY LOGFILE command.

RMAN-05535: WARNING: All redo log files were not defined properly.

Cause: It was not possible to define all the redo log files. This can occur when LOG\_FILE\_NAME\_CONVERT initialization parameter is defined but fails to match all the names or causes names to be created that are not in valid directories.

Action: Query the V$LOGFILE view to see what redo log files are defined after DUPLICATE has completed. Use the ALTER DATABASE RENAME FILE SQL command to correctly name the existing redo log files.

RMAN-05536: auxiliary logfile name string conflicts with a file used by the target database

Cause: RMAN attempted to use the specified logfile name as a standby redo log file in the auxiliary database, but this name was already in use by the target database.

Action: Use or alter LOG\_FILE\_NAME\_CONVERT so that unique logfile names can be generated. Or wait for the command to complete and create standby logfiles using the SQL ALTER DATABASE ADD STANDBY LOGFILE command.

RMAN-05537: DUPLICATE without TARGET connection when auxiliary instance is started with spfile cannot use SPFILE clause

Cause: A DUPLICATE was attempted when the auxiliary database was started with a server parameter file and the SPFILE sub-clause was specified. RMAN cannot restore the server parameter file if the auxiliary database is already started with a server parameter file.

Action: Start the auxiliary database with a client parameter file or do not specify SPFILE sub-clause and retry.

RMAN-05538: WARNING: implicitly using DB\_FILE\_NAME\_CONVERT

Cause: The duplicated SPFILE had DB\_FILE\_NAME\_CONVERT set and it has been used to produce datafile names for the new database.

Action: No action is required. This is an informational message only. If this behavior was not intended, then do not duplicate the server parameter file, or explicitly set DB\_FILE\_NAME\_CONVERT in the DUPLICATE command and retry the operation.

RMAN-05539: DUPLICATE TARGET DATABASE cannot be used without connecting to the TARGET

Cause: A DUPLICATE TARGET DATABASE was attempted and no connection to the TARGET database was established.

Action: Connect to TARGET or use DATABASE <db\_name> clause.

RMAN-05540: no archived logs found in repository for database string

Cause: Recovery catalog did not have archived log records for the specified database. If database is running in NOARCHIVELOG mode, then specify NOREDO.

Action: Specify NOREDO for NOARCHIVELOG databases. Cannot duplicate an ARCHIVELOG database unless the recovery catalog or target database control file has archived redo log information about it.

RMAN-05541: no archived logs found in target database

Cause: Target database was running in archived log mode, but control file did not have any archived log records.

Action: Archive current log before retrying command.

RMAN-05542: Only UNTIL TIME can be used with DUPLICATE without TARGET and CATALOG connections

Cause: A DUPLICATE without TARGET and CATALOG connections was attempted specifying an UNTIL clause that was not TIME based.

Action: Retry the command with an UNTIL TIME clause or without an UNTIL clause.

RMAN-05543: DUPLICATE without TARGET connection requires that DATABASE is specified

Cause: A DUPLICATE without TARGET connection was attempted without specifying the database to duplicate.

Action: Retry the command specifying the DATABASE to duplicate.

RMAN-05544: Cannot specify ACTIVE DATABASE when not connected to target database

Cause: DUPLICATE from ACTIVE DATABASE required a connection to the target database.

Action: Connect to target database or remove from ACTIVE DATABASE and retry the command.

RMAN-05545: WARNING: Until SCN string is ahead of SCN of last full resync of recovery catalog: string

Cause: The specified point-in-time for duplication without a target connection was ahead of the last time that the datafile information was resynced to the recovery catalog. Information about offline and read-only datafiles might be incorrect.

Action: If duplication fails due to incorrectly identified offline and/or read-only datafiles, specify a point-in-time before the last resync of the recovery catalog and retry the command. Or perform full resync of the target database and retry the command.

RMAN-05546: DUPLICATE without TARGET and CATALOG connections requires that BACKUP LOCATION is specified

Cause: A DUPLICATE without TARGET and CATALOG connections was attempted without specifying BACKUP LOCATION.

Action: Retry the command specifying a BACKUP LOCATION.

RMAN-05547: Checking that duplicated tablespaces are self-contained

Cause: This is an informational message only.

Action: No action is required.

RMAN-05548: The set of duplicated tablespaces is not self-contained

Cause: A DUPLICATE TABLESPACE has specified a set of tablespaces that cannot function independently.

Action: Retry the command without incomplete tablespaces or add other tablespaces to make the set self-contained.

RMAN-05549: The following SYS objects were found in skipped tablespaces

Cause: This is an informational message only.

Action: No action required.

RMAN-05550: TARGET database not open, cannot verify that set of tablespaces being duplicated does not have SYS objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-05551: Not connected to TARGET, cannot verify that set of tablespaces being duplicated does not have SYS objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-05552: Object string on tablespace string

Cause: A SYS object was found in one of the skipped tablespaces.

Action: Remove object if possible or include tablespace in duplicated tablespaces.

RMAN-05553: SYS objects in skipped tablespaces prevent duplication

Cause: Objects owned by SYS were found in the tablespaces that would not be duplicated.

Action: If using SKIP TABLESPACE, do not skip tablespaces that contain SYS objects. If using DUPLICATE TABLESPACE, make sure to specify all tablespaces containing SYS objects.

RMAN-05554: cannot specify INCARNATION when duplicating without TARGET and CATALOG connections

Cause: A DUPLICATE without TARGET and CATALOG connections was attempted when INCARNATION was also specified.

Action: Retry the command without specifying INCARNATION.

RMAN-05555: Not connected to TARGET or TARGET not open, cannot verify that subset of tablespaces is self-contained

Cause: This is an informational message only.

Action: No action is required.

RMAN-05556: not all datafiles have backups that can be recovered to SCN string

Cause: One or more datafiles being duplicated could not be restored as no available backups were found.

Action: Change the system change number (SCN) or make backups available for the specified datafiles and retry the command.

RMAN-05557: Target instance not started with server parameter file

Cause: SPFILE clause was used but target instance was not started with a server parameter file.

Action: Do not specify SPFILE clause, or restart target instance with server parameter file.

RMAN-05558: Must specify DB\_UNIQUE\_NAME with FOR STANDBY clause

Cause: A DUPLICATE FOR STANDBY... SPFILE command was issued but DB\_UNIQUE\_NAME was not provided for the standby database.

Action: Specify a DB\_UNIQUE\_NAME in the SPFILE clause for the standby database.

RMAN-05559: error converting parameter string, string larger than number

Cause: While attempting to apply a PARAMETER\_VALUE\_CONVERT to the specified parameter value, the resulting string exceeded the maximum length for a value.

Action: Change the PARAMETER\_VALUE\_CONVERT so that, when converting the parameter, the maximum lenght is not reached.

RMAN-05560: Using previous duplicated file string for datafile number with checkpoint SCN of string

Cause: A datafile copy from a previous duplicate attempt matching the duplicate name requested was found for the specified datafile and will be used instead of restoring the datafile from a backup.

Action: No action needed unless this behavior is not desire. In that case, either use a different name for the datafile or use NORESUME to avoid using previous datafile copies for all the datafiles.

RMAN-05561: CATALOG did not return information about tablespaces with undo segments

Cause: A DUPLICATE with no target connection was attempted, but the recovery catalog did not have information about the tablespaces with undo segments at the specified point in time. It is necessary that the list of tablespaces with undo segments is provided with the UNDO TABLESPACE clause.

Action: Retry the command specifying the list of tablespaces with undo segments using the UNDO TABLESPACE clause.

RMAN-05562: SPFILE backup not found for database string with DBID number created before string in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05563: SPFILE backup not found for database with DBID number created before string in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05564: SPFILE backup not found for database string created before string in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05565: SPFILE backup created before string not found in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05566: SPFILE backup not found for database string with DBID number in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05567: SPFILE backup not found for database with DBID number in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05568: SPFILE backup not found for database string in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05569: SPFILE backup not found in string

Cause: RMAN could not locate a backup of the SPFILE in the specified location.

Action: Provide a different location and retry the command.

RMAN-05570: Duplicate for standby does not allow the use of LOGFILE

Cause: A LOGFILE clause was specified for the command.

Action: Remove the LOGFILE clause and try again.

RMAN-05571: DORECOVER specified for non standby duplication

Cause: A DORECOVER clause was specified and the duplicate did not specify FOR STANDBY.

Action: Remove the DORECOVER clause or add FOR STANDBY and try again.

RMAN-05572: Controlfile backup not found for database string with DBID number created before string in string

Cause: RMAN could not locate a backup of the control file in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05573: CONTROLFILE backup not found for database with DBID number created before string in string

Cause: RMAN could not locate a backup of the control file in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05574: CONTROLFILE backup not found for database string created before string in string

Cause: RMAN could not locate a backup of the control file in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05575: CONTROLFILE backup created before string not found in string

Cause: RMAN could not locate a backup of the control file in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05576: CONTROLFILE backup not found for database string with DBID number in string

Cause: RMAN could not locate a backup of the control file in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05577: CONTROLFILE backup not found for database with DBID number in string

Cause: RMAN could not locate a backup of the control file in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05578: CONTROLFILE backup not found for database string in string

Cause: RMAN could not locate a backup of the control file in the specified location that satisfied the specified parameters.

Action: Change the parameters, or provide a different location and retry the command.

RMAN-05579: CONTROLFILE backup not found in string

Cause: RMAN could not locate a backup of the control file in the specified location.

Action: Provide a different location and retry the command.

RMAN-05580: Duplicate for standby does not allow the use of SKIP READONLY

Cause: A SKIP READONLY clause was specified for the command.

Action: Remove the SKIP READONLY clause and try again.

RMAN-05581: Duplicate for standby does not allow the use of SKIP TABLESPACE

Cause: A SKIP TABLESPACE clause was specified for the command.

Action: Remove the SKIP TABLESPACE clause and try again.

RMAN-05582: Duplicate for standby does not allow the use of OPEN RESTRICTED

Cause: An OPEN RESTRICTED clause was specified for the command.

Action: Remove the OPEN RESTRICTED clause and try again.

RMAN-05583: Duplicate for standby does not allow the use of TABLESPACE

Cause: A TABLESPACE clause was specified for the command.

Action: Remove the TABLESPACE clause and try again.

RMAN-05584: Duplicate for standby does not allow the use of NOREDO

Cause: A NOREDO clause was specified for the command.

Action: Remove the NOREDO clause and try again.

RMAN-05585: Duplicate for standby does not allow the use of UNDO TABLESPACE

Cause: A UNDO TABLESPACE clause was specified for the command.

Action: Remove the UNDO TABLESPACE clause and try again.

RMAN-05586: The following materialized objects were found in skipped tablespaces

Cause: This is an informational message only.

Action: No action required.

RMAN-05587: Materialized table string on tablespace string

Cause: A materialized table was found in one of the skipped tablespaces.

Action: Remove object if possible or include tablespace in duplicated tablespaces.

RMAN-05588: Materialized index string on tablespace string

Cause: A materialized index was found in one of the skipped tablespaces.

Action: Remove object if possible or include tablespace in duplicated tablespaces.

RMAN-05589: Materialized objects in skipped tablespaces prevent duplication

Cause: Materialized objects found in the tablespaces that would not be duplicated.

Action: If using SKIP TABLESPACE, do not skip tablespaces that contain materialized objects. If using DUPLICATE TABLESPACE, make sure to specify all tablespaces containing SYS objects.

RMAN-05590: Reenabling controlfile options for auxiliary database

Cause: This is an informational message only.

Action: No action is required.

RMAN-05591: Ignoring error, reattempt command after duplicate finishes

Cause: A sql error was received during the execution of command.

Action: Check the accompanying errors.

RMAN-05592: Dropping offline and skipped tablespaces

Cause: This is an informational message only.

Action: No action is required.

RMAN-05593: Could not drop tablespace string due to constraints, will reattempt removal after other tablespaces are removed

Cause: This is an informational message only.

Action: No action is required.

RMAN-05594: Could not drop tablespace string due to constraints

Cause: The tablespace failed to be dropped several times, no more attempts will be made.

Action: Drop the tablespace manually after duplicate finishes.

RMAN-05595: Leaving database unopened, as requested

Cause: User requested that the new database was not open.

Action: After the database is opened with resetlogs you might want to:

\- Catalog datafilecopies of readonly datafiles

\- Switch readonly datafiles to the cataloged datafilecopies

\- Online read only tablespaces

\- Drop skipped tablespaces

\- Enable supplemental logging

\- Enable force logging

\- Enable change tracking

RMAN-05596: Error while removing created server parameter file

Cause: Server parameter file was not deleted. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors. Remove file manually.

RMAN-05597: Database started with server parameter file and PFILE clause used in command

Cause: A PFILE clause was specified for duplicate command, but database was started with a server parameter file causing a conflict.

Action: Remove PFILE clause from command or restart database without using a server parameter file.

RMAN-05598: SPFILE and PFILE clause specified in command

Cause: SPFILE and PFILE clauses were specified for duplicate command causing a conflict.

Action: Remove either one of the clauses and retry the command.

RMAN-05599: PASSWORD clause is not needed when duplicating for standby database from active database

Cause: PASSWORD clause was specified when creating a standby database from active database. This is not needed, it is automatic.

Action: No action is required. This is an informational message only.

RMAN-05600: Cannot specify UNTIL clause when duplicating from active database

Cause: An UNTIL clause in the command or with a SET UNTIL was in effect for an active database duplication.

Action: Remove UNTIL clause and reattempt duplication.

RMAN-05601: Failed to restore original settings to server parameter file

Cause: An error was received while duplicating the database after the server parameter file was modified by RMAN. An attempt was made to restore original settings to the server parameter file, but the original error was such that it was not possible to restore the settings.

Action: Before reattempting database duplication, the server parameter file needs to be fixed manually with the original values.

RMAN-05602: restarting auxiliary database without server parameter file

Cause: This is an informational message only.

Action: No action is required.

RMAN-05621: password file location could not be found for the target database

Cause: The password file location did not exist for the target database instance.

Action: Set the password file location for the target database instance.

RMAN-05622: password file location could not be found for the auxiliary database

Cause: The password file location did not exist for the auxiliary database instance.

Action: Set the password file location for the auxiliary database instance.

RMAN-06000: could not open recovery manager library file: string

Cause: The "recover.bsq" file could not be opened.

Action: Check that the file was installed correctly and that the user running RMAN has authority to read the file.

RMAN-06001: error parsing job step library

Cause: A syntax error was encountered while parsing "recover.bsq".

Action: Ensure that the correct version of the file is installed and that it has not been modified in any way.

RMAN-06002: command not allowed when not connected to a recovery catalog

Cause: A command that is allowed only when a recovery catalog connect string was supplied was attempted.

Action: Avoid using the command, or restart RMAN and supply a recovery catalog connect string via the CATALOG parameter.

RMAN-06003: ORACLE error from target database: string

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-06004: ORACLE error from recovery catalog database: string

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-06005: connected to target database: string (DBID=string)

Cause: This is an informational message only.

Action: No action is required.

RMAN-06006: connected to target database: string (not mounted)

Cause: This is an informational message only.

Action: No action is required.

RMAN-06007: target database not mounted and db\_name not set in init.ora

Cause: The target database has not mounted the control file, and its "init.ora" file does not specify the DB\_NAME parameter.

Action: MOUNT the target database, or add the DB\_NAME parameter to its "init.ora" and restart the instance.

RMAN-06008: connected to recovery catalog database

Cause: This is an informational message only.

Action: No action is required.

RMAN-06009: using target database control file instead of recovery catalog

Cause: This is an informational message only.

Action: No action is required.

RMAN-06010: error while looking up datafile: string

Cause: An error occurred while looking up the specified datafile in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. Ensure that the file name is entered correctly. If the datafile was added recently, then a RESYNC CATALOG must be done to update the recovery catalog.

RMAN-06011: invalid level specified: number

Cause: An invalid incremental backup level was specified.

Action: Incremental backup level must be between 0 and 4.

RMAN-06012: channel: string not allocated

Cause: A RELEASE command was found for a channel identifier that was not yet allocated.

Action: Correct the channel identifier, or add an ALLOCATE CHANNEL command.

RMAN-06013: duplicate channel identifier found: string

Cause: A channel identifier was reused without first releasing the channel.

Action: Add a RELEASE CHANNEL command.

RMAN-06014: command not implemented yet: string

Cause: Not all commands are implemented for the beta release.

Action: Avoid using the command.

RMAN-06015: error while looking up datafile copy name: string

Cause: An error occurred while looking up the specified datafile copy name in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. Ensure that the file name is entered correctly. If the datafile copy was created when the recovery catalog was not available, then a RESYNC CATALOG must be done to update the recovery catalog.

RMAN-06016: duplicate backup operand specified: string

Cause: The specified operand appears more than once in the same backup specifier or backup command.

Action: Delete the duplicated operand.

RMAN-06017: initialization of parser failed

Cause: The parser package initialization routine returned an error.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-06018: duplicate operand specified in backup specification: string

Cause: A backup specification operand appears more than once in a backup specification.

Action: Delete the duplicate operand.

RMAN-06019: could not translate tablespace name "string"

Cause: An error occurred while looking up the specified tablespace name in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. Ensure that the tablespace is entered correctly. If the tablespace was added recently, then a RESYNC CATALOG must be done to update the recovery catalog.

RMAN-06020: connected to auxiliary database (not started)

Cause: This is an informational message only.

Action: No action is required.

RMAN-06021: FROM DATAFILECOPY/BACKUPSET may not be specified with archived logs

Cause: The FROM DATAFILECOPY/BACKUPSET option applies only to datafile and control file restores.

Action: Use this option only for datafile and control file restores.

RMAN-06022: invalid level specified for image copy: number

Cause: An invalid incremental backup level was specified for an image copy.

Action: Incremental backup level must be 0 for image copies.

RMAN-06023: no backup or copy of datafile number found to restore

Cause: A datafile, tablespace, or database restore could not proceed because no backup or copy of the indicated file was found. It may be the case that a backup or copy of this file exists but does not satisfy the criteria specified in the user's restore operands.

Action: None - this is an informational message. See message 6026 for further details.

RMAN-06024: no backup or copy of the control file found to restore

Cause: A control file restore could not proceed because no backup or copy of the control file was found. It may be the case that a backup or copy of this file exists but does not satisfy the criteria specified in the user's restore operands.

Action: None - this is an informational message. See message 6026 for further details.

RMAN-06025: no backup of archived log for thread number with sequence number and starting SCN of string found to restore

Cause: An archived log restore restore could not proceed because no backup of the indicated archived log was found. It may be the case that a backup of this file exists but does not satisfy the criteria specified in the user's restore operands.

Action: None - this is an informational message. See message 6026 for further details.

RMAN-06026: some targets not found - aborting restore

Cause: Some of the files specified for restore could not be found. Message 6023, 6024, or 6025 is also issued to indicate which files could not be found. Some common reasons why a file can not be restored are that there is no backup or copy of the file that is known to recovery manager, or there are no backups or copies that fall within the criteria specified on the RESTORE command, or some datafile copies have been made but not cataloged.

Action: The Recovery Manager LIST command can be used to display the backups and copies that Recovery Manager knows about. Select the files to be restored from that list.

RMAN-06027: no archived logs found that match specification

Cause: An archived log record specifier did not match any archived logs in the recovery catalog or target database control file.

Action: Resubmit the command with a different archived log record specifier. The Recovery Manager (RMAN) LIST command can be used to display all archived logs that RMAN knows about.

RMAN-06028: duplicate operand specified in restore specification: string

Cause: The CHANNEL, TAG, FROM, PARMS, VALIDATE, DEVICE TYPE, CHECK READONLY or DB\_UNIQUE\_NAME option was specified more than once in the restore command or in one of the restore specifications.

Action: Correct and resubmit the command.

RMAN-06029: the control file may be included only in a datafile backup set

Cause: The "include current/standby control file" option was specified for an archived log backup set.

Action: Use this option only for datafile backup sets.

RMAN-06030: the DELETE \[ALL\] INPUT option may not be used with a datafile backup set

Cause: The DELETE \[ALL\] INPUT option was specified for a backup that contains the current control file or datafile.

Action: Remove the option and resubmit the command.

RMAN-06031: could not translate database keyword

Cause: An error was received when calling DBMS\_RCVMAN

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-06032: at least 1 channel of TYPE DISK must be allocated to execute a COPY command

Cause: No channel of TYPE DISK was allocated.

Action: Allocate a channel of TYPE DISK and re-issue the command.

RMAN-06033: channel string not allocated

Cause: An rman command requests a specific channel, but the requested channel has not been allocated.

Action: ALLOCATE the channel, or correct the channel identifier.

RMAN-06034: at least 1 channel must be allocated to execute this command

Cause: No channels were allocated.

Action: ALLOCATE a channel.

RMAN-06035: wrong version of recover.bsq, expecting string, found string

Cause: The "recover.bsq" file is incompatible with the RMAN executable.

Action: Install the correct version of recover.bsq.

RMAN-06036: datafile number is already restored to file string

Cause: A SET NEWNAME command was issued to restore a datafile to a location other than the original datafile, and Recovery Manager determined that the best candidate for restoring the file is the datafile copy with the same name, therefore the file is already restored and no action need be taken.

Action: None - this is an informational message.

RMAN-06038: recovery catalog package detected an error

Cause: A call to DBMS\_RCVMAN returned an error.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-06039: SET NEWNAME command has not been issued for datafile string

Cause: A SWITCH command was specified for a datafile, but no destination was specified and no SET NEWNAME command has been previously issued for that file. An explicit file to switch to must be specified if no SET NEWNAME command has been issued.

Action: Correct and resubmit the SWITCH command.

RMAN-06040: control file is already restored to file string

Cause: The best candidate control file for restoration is the one that is named in the RESTORE CONTROLFILE command, hence no action need be taken.

Action: None - this is an informational message.

RMAN-06041: cannot switch file number to copy of file number

Cause: An attempt was made to switch a datafile to a copy of a different datafile.

Action: Correct and resubmit the SWITCH command.

RMAN-06042: PLUS ARCHIVELOG option is not supported with non-datafile backups

Cause: The PLUS ARCHIVELOG option was supplied but does not apply to this type of backup.

Action: Remove the PLUS ARCHIVELOG operand and re-enter the command.

RMAN-06043: TAG option not supported for archived log copies

Cause: The tag option was supplied but does not apply to this type of copy.

Action: Remove the TAG operand and re-enter the command

RMAN-06045: LEVEL option not supported for archived log or current/standby control file copies

Cause: The LEVEL option was supplied but does not apply to this type of copy.

Action: Remove the LEVEL operand and re-enter the command.

RMAN-06046: archived log name: string

Cause: An error occurred while translating an archived log name to its recovery catalog RECID/time stamp. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-06047: duplicate datafile number specified for restoration from copy

Cause: The indicated datafile was specified more than once in the same restore command.

Action: Correct and resubmit the RESTORE command.

RMAN-06048: duplicate control file specified for restoration from copy

Cause: The control file was specified more than once in the same RESTORE command.

Action: Correct and resubmit the RESTORE command.

RMAN-06049: CHECK LOGICAL option not supported for archived log or current/standby control file copies

Cause: The check logical option was supplied but does not apply to this type of copy.

Action: Remove the CHECK LOGICAL operand and re-enter the command

RMAN-06050: archived log for thread number with sequence number is already on disk as file string

Cause: An archived log which was requested to be restored (either explicitly or via a range specification) does not need to be restored because it already exists on disk.

Action: None - this is an informational message

RMAN-06051: DELETE INPUT option not implemented yet

Cause: This option was specified in a backup specification.

Action: Remove the DELETE INPUT option.

RMAN-06052: no parent backup or copy of datafile number found

Cause: An incremental backup at level 1 or higher could not find any parent backup or copy of the indicated datafile. A level 0 backup of the datafile will be taken automatically.

Action: This is an informational message only.

RMAN-06053: unable to perform media recovery because of missing log

Cause: This message is accompanied with another message identifying the missing log. The log would be needed to perform the media recovery, but the log is not on disk and no backup set containing the log is available.

Action: Determine if a backup set containing the log can be made available. If so, then use the CHANGE command to make the backup set available and retry the command. If not, then a point-in-time recovery up to the missing log is the only alternative.

RMAN-06054: media recovery requesting unknown archived log for thread string with sequence string and starting SCN of string

Cause: Media recovery is requesting a log whose existence is not recorded in the recovery catalog or target database control file.

Action: If a copy of the log is available, then add it to the recovery catalog and/or control file via a CATALOG command and then retry the RECOVER command. If not, then a point-in-time recovery up to the missing log is the only alternative and database can be opened using ALTER DATABASE OPEN RESETLOGS command.

RMAN-06055: could not find archived log with sequence string for thread string

Cause: A log which was on disk at the start of media recovery or which should have been restored from a backup set could not be found.

Action: Check the Recovery Manager message log to see if the log was restored by a previous job step. If so, then check the V$ARCHIVED\_LOG view to see if the log is listed in the control file. If so, then validate that the log exists on disk and is readable. If the log was not restored, or was restored but no record of the log exists in V$ARCHIVED\_LOG, then contact Oracle Support Services.

RMAN-06056: could not access datafile number

Cause: A backup or copy could not proceed because the datafile header could not be read or the header was not valid.

Action: Make the datafile accessible or skip it.

RMAN-06057: a standby control file cannot be included along with a current control file

Cause: "current control file" was specified along with "standby control file".

Action: Remove "current control file" or "standby control file" from backup specification.

RMAN-06058: a current control file cannot be included along with a standby control file

Cause: "standby control file" was specified along with "current control file".

Action: Remove "standby control file" or "current control file" from backup specification.

RMAN-06059: expected archived log not found, loss of archived log compromises recoverability

Cause: The archived log was not found. The recovery catalog or target database control file thinks it does exist. If the archived log has in fact been lost and there is no backup, then the database is no longer recoverable across the point-in-time covered by the archived log. This may occur because the archived log was removed by an outside utility without updating the recovery catalog or target database control file.

Action: If the archived log has been removed with an outside utility and the archived log has already been backed up, then you can synchronize the recovery catalog or target database control file by running CROSSCHECK ARCHIVELOG ALL. If the archived log has not been previously backed up, then you should take a full backup of the database and archived logs to preserve recoverability. Previous backups are not fully recoverable.

RMAN-06060: WARNING: skipping datafile compromises tablespace string recoverability

Cause: SKIP INACCESSIBLE or SKIP OFFLINE option resulted in skipping datafile during BACKUP. If the datafile has in fact been lost and there is no backup, then the tablespace is no longer recoverable without ALL archived logs since datafile creation. This may occur because the datafile was deleted by an outside utility or the datafile is made OFFLINE \[DROP\].

Action: If there is no backup of skipped datafile and the tablespace has to be recoverable without ALL archived logs since datafile creation, then you should make these datafile available for backup.

RMAN-06061: WARNING: skipping archived log compromises recoverability

Cause: SKIP INACCESSIBLE option resulted in skipping archived logs during BACKUP. If the archived log has in fact been lost and there is no backup, then the database is no longer recoverable across the point-in-time covered by the archived log. This may occur because archived log was removed by an outside utility without updating the recovery catalog or target database control file.

Action: If the archived log has been removed with an outside utility and the archived log has already been backed up, then you can synchronize the recovery catalog or target database control file by running CROSSCHECK ARCHIVELOG ALL. If the archived log has not been previously backed up, then you should take a full backup of the database and archived logs to preserve recoverability. Previous backups are not fully recoverable.

RMAN-06062: can not backup SPFILE because the instance was not started with SPFILE

Cause: A backup command requested a backup of the SPFILE, but no SPFILE was used to startup the instance.

Action: Create an SPFILE and re-start the instance using the SPFILE or modify the command.

RMAN-06063: DBID is not found in the recovery catalog

Cause: DBID is not found in the recovery catalog.

Action: Verify that the DBID is correct and restart the command.

RMAN-06064: creating datafile file number=string name=string

Cause: RESTORE/RECOVER command was issued and there were no backup available for the datafile.

Action: This is an informational message only.

RMAN-06065: The backup operand \[string\] conflicts with another specified operand.

Cause: The user attempted to use two (or more) conflicting operands within the same statement.

Action: Remove one or both of the conflicting operands.

RMAN-06066: the target database must be mounted when issuing a RECOVER command

Cause: A RECOVER command was issued, but the target database control file is not mounted.

Action: Mount the target database control file by issuing ALTER DATABASE MOUNT via Enterprise Manager or Server Manager.

RMAN-06067: RECOVER DATABASE required with a backup or created control file

Cause: The control file has been restored from a backup or was created via ALTER DATABASE CREATE CONTROLFILE.

Action: Use the RECOVER DATABASE command to perform the recovery.

RMAN-06068: recovery aborted because of missing datafiles

Cause: This error should be accompanied by one or more instances of message ORA-06094.

Action: Refer to message ORA-06094.

RMAN-06069: the file name for datafile string is missing in the control file

Cause: Media recovery of a backup control file added this datafile to the control file, but it does not set the file name because that is unsafe.

Action: If the datafile is on disk, then issue ALTER DATABASE RENAME to correct the control file. Otherwise, RESTORE the datafile, and then use SWITCH to make it known to the control file. If the tablespace containing this datafile will be dropped, then reissue the RECOVER command with a SKIP clause to skip recovery of this tablespace.

RMAN-06070: DBWR could not identify datafile string

Cause: DBWR could not find the specified datafile.

Action: Ensure that the datafile exists and is accessible.

RMAN-06071: could not open datafile string

Cause: An error was encountered when trying to open the specified datafile.

Action: Ensure that the datafile exists and is accessible.

RMAN-06073: file header is corrupt for datafile string

Cause: ORACLE detected a corruption in the file header. A media failure has probably occurred.

Action: RESTORE the datafile to a new location, then do a SWITCH, and then retry the RECOVER command.

RMAN-06074: file string is not an ORACLE datafile

Cause: The file header indicates that this file is not a datafile. The file may have been overlaid or corrupted.

Action: RESTORE the datafile to a new location, then do a SWITCH, and then retry the RECOVER command.

RMAN-06075: datafile string does not belong to this database

Cause: The file header indicates that this file belongs to some other ORACLE database.

Action: RESTORE the datafile to a new location, then do a SWITCH, and then retry the RECOVER command.

RMAN-06076: datafile string contains wrong datafile

Cause: The datafile header indicates the file contains a different datafile number.

Action: RESTORE the datafile, and then retry the RECOVER command.

RMAN-06077: datafile string is a different version than contained in the control file

Cause: The control file entry for this datafile specifies a different version of this datafile. Different versions of a datafile can exist when a tablespace is dropped, and a new tablespace is created which reuses the same datafile numbers.

Action: If the datafile is correct, the fix the control file by using the SWITCH command. Otherwise, RESTORE the correct version of this datafile and retry the RECOVER command.

RMAN-06078: the control file is older than datafile string

Cause: The control file appears to be older than the specified datafile, but it is not marked as a backup control file. This indicates that the control file has been replaced with an older version. This error does not occur when a backup control file which was created via Recovery Manager or the ALTER DATABASE BACKUP CONTROLFILE command is restored because such control files are marked as backups.

Action: RESTORE a control file and perform RECOVER DATABASE.

RMAN-06079: database must be mounted to perform recovery

Cause: A RECOVER command was issued, but the target database is not mounted.

Action: Issue ALTER DATABASE MOUNT.

RMAN-06080: SWITCH required for datafile string

Cause: The control file record for this datafile is for an older incarnation of the datafile. A SWITCH command must be issued to updated the control file before doing RECOVER.

Action: Issue SWITCH command then retry RECOVER.

RMAN-06081: error reading datafile header for datafile string, code string

Cause: X$KCVFH returned the specified code in the HXERR column when it was queried for the specified datafile.

Action: Ensure the datafile exists and is readable. Using a newer release of Recovery Manager may return a more meaningful error message. If you have no newer version of Recovery Manager, contact Oracle Support Services.

RMAN-06082: datafile copy tag string is ambiguous

Cause: The specified tag refers to multiple datafile copies belonging to different datafiles.

Action: Specify the datafile copy by file name rather than by tag.

RMAN-06083: error when loading stored script string

Cause: The recovery catalog database returned an error. This error explains the cause of the problem.

Action: Correct the problem and retry.

RMAN-06084: the target database may not be mounted when issuing REPLICATE

Cause: A REPLICATE command was issued, but the target database is already mounted.

Action: dismount the target database control file by issuing ALTER DATABASE CLOSE and ALTER DATABASE DISMOUNT via Enterprise Manager or Server Manager.

RMAN-06085: must use SET NEWNAME command to restore datafile string

Cause: A RESTORE command for the specified datafile could not find a destination name for the specified datafile.

Action: Add a SET NEWNAME command prior to the RESTORE command to specify the restore destination for this file.

RMAN-06086: offline files may only be skipped in a datafile backup set

Cause: The SKIP OFFLINE option was specified for an archived log backup set.

Action: Use this option only for datafile backup sets.

RMAN-06087: read-only files may only be skipped in a datafile backup set

Cause: The SKIP READONLY option was specified for an archived log backup set.

Action: Use this option only for datafile backup sets.

RMAN-06088: datafile copy string not found or out of sync with catalog

Cause: The indicated file is not found, or is found but is not the same file that the recovery catalog thinks it is. It is likely that some operation outside of Recovery Manager has altered the file, or that Recovery Manager has not resynced with the target database.

Action: Re-catalog the file and retry the operation.

RMAN-06089: archived log string not found or out of sync with catalog

Cause: The indicated file is not found, or is found but is not the same file that the recovery catalog thinks it is. It is likely that some operation outside of Recovery Manager has altered the file, or that Recovery Manager has not resynced with the target database.

Action: Re-catalog the file and retry the operation.

RMAN-06090: error while looking up control file copy: string

Cause: An error occurred while looking up the specified control file copy in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. Ensure that the file name is entered correctly. If the control file copy was created when the recovery catalog was not available, then a RESYNC CATALOG must be done to update the recovery catalog.

RMAN-06091: no channel allocated for maintenance (of an appropriate type)

Cause: A command was entered that requires a maintenance channel, and no maintenance channel is allocated, or none of the appropriate type.

Action: Use ALLOCATE CHANNEL FOR MAINTENANCE before deleting backup pieces, or using the CROSSCHECK or DELETE EXPIRED commands. Proxy copies require a non-DISK channel.

RMAN-06092: error while looking up backup piece

Cause: An error occurred while looking up the specified backup piece in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. Ensure that the name or key is entered correctly. If the backup piece was created when the recovery catalog was not available, then a RESYNC CATALOG must be done to update the recovery catalog.

RMAN-06093: recovery catalog contains obsolete version of datafile string

Cause: The specified datafile number was dropped and then reused. The control file mounted by the target database contains the newer version of the datafile, but the recovery catalog contains information about only the older version.

Action: Issue a RESYNC command to update the recovery catalog, then reissue the failing command. If the error persists, contact Oracle Support Services.

RMAN-06094: datafile string must be restored

Cause: A RECOVER command was issued, and the recovery catalog indicates the specified datafile should be part of the recovery, but this datafile is not listed in the control file, and cannot be found on disk.

Action: Issue a RESTORE command for this datafile, using the same UNTIL clause specified to the RECOVER command (if any), then reissue the RECOVER.

RMAN-06095: a backup control file must be restored to recover datafile string

Cause: The control file currently mounted by the target database contains a newer incarnation of the datafile than the recovery catalog indicates is appropriate for the Point-in-Time being recovered to.

Action: Restore the control file, using the same UNTIL clause specified on the failing RECOVER command, then reissue the command. If no control file can be restored, then you should issue a CREATE CONTROLFILE command.

RMAN-06096: SWITCH required for newname of datafile string to take effect

Cause: A SET NEWNAME was issued for this datafile, but no SWITCH command was issued before the RECOVER command.

Action: Issue a SWITCH command to make the newname take effect before doing RECOVER.

RMAN-06098: the target database must be mounted when issuing a BACKUP command

Cause: A BACKUP command was issued, but the target database control file is not mounted.

Action: Mount the target database control file by issuing ALTER DATABASE MOUNT via Enterprise Manager or Server Manager.

RMAN-06099: error occurred in source file: string, line: number

Cause: See accompanying error.

Action: See accompanying error.

RMAN-06100: no channel to restore a backup or copy of datafile number

Cause: A datafile, tablespace, or database restore could not proceed because the backup of the indicated file exists on a device type that was not allocated for restore.

Action: None - this is an informational message. See message 6026 for further details.

RMAN-06101: no channel to restore a backup or copy of the control file

Cause: A control file restore could not proceed because the backup of the indicated file exists on a device type that was not allocated for restore.

Action: None - this is an informational message. See message 6026 for further details.

RMAN-06102: no channel to restore a backup or copy of archived log for thread number with sequence number and starting SCN of string

Cause: An archived log restore restore could not proceed because the backup of the indicated file exists on a device type that was not allocated for restore.

Action: None - this is an informational message. See message 6026 for further details.

RMAN-06103: duplicate qualifier found in REPORT command: string

Cause: The indicated qualifier appears more than once in a REPORT qualifier list.

Action: delete the duplicate qualifier

RMAN-06105: duplicate qualifier found in LIST command: string

Cause: The indicated qualifier appears more than once in a LIST qualifier list.

Action: delete the duplicate qualifier

RMAN-06106: this command requires that target database be mounted

Cause: A command was issued that requires the target database to be mounted, but the target database is not mounted.

Action: Mount the target database control file by issuing ALTER DATABASE MOUNT via Enterprise Manager or Server Manager.

RMAN-06107: WARNING: control file is not current for REPORT NEED BACKUP DAYS

Cause: The REPORT NEED BACKUP DAYS command may report some files as requiring backups when they really do not, because the most current online status of the file is not known unless a current control file is mounted.

Action: No action is required, however, a current control file should be mounted, if possible, to get the most accurate REPORT output.

RMAN-06108: changed datafile copy unavailable

Cause: This is an informational message only.

Action: No action is required.

RMAN-06109: changed archived log unavailable

Cause: This is an informational message only.

Action: No action is required.

RMAN-06110: changed control file copy unavailable

Cause: This is an informational message only.

Action: No action is required.

RMAN-06111: changed backup piece unavailable

Cause: This is an informational message only.

Action: No action is required.

RMAN-06112: changed datafile copy available

Cause: This is an informational message only.

Action: No action is required.

RMAN-06113: changed archived log available

Cause: This is an informational message only.

Action: No action is required.

RMAN-06114: changed control file copy available

Cause: This is an informational message only.

Action: No action is required.

RMAN-06115: changed backup piece available

Cause: This is an informational message only.

Action: No action is required.

RMAN-06116: cannot crosscheck unavailable object

Cause: An attempt was made to crosscheck an object which is unavailable.

Action: Make object available and try again or don't crosscheck object.

RMAN-06117: cannot do DELETE EXPIRED on an object which is not expired

Cause: An attempt was made to DELETE EXPIRED an object which is not expired.

Action: Remove EXPIRED keyword, crosscheck object, or don't delete object.

RMAN-06118: a backup control file older than SCN string must be used for this recovery

Cause: An attempt was made to recover the database, but some files had no backup, and were not present in the control file at the beginning of the restore. This happens when the control file used during the recovery is a backup control file taken before the creation of some of the files that had no backup. In this situation, the control file that is used must be taken before the creation of all files that have no backup. This will enable RMAN to automatically re-create all of the files that had no backup.

Action: Restore a control file that was backed up before the specified system change number (SCN). The following RMAN commands can be used to do this: SET UNTIL SCN \<x>; (where \<x> is the SCN displayed in the message) RESTORE CONTROLFILE;

RMAN-06119: uncataloged datafile copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-06120: uncataloged archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-06121: uncataloged control file copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-06122: CHANGE.. UNCATALOG not supported for BACKUPSET

Cause: The CHANGE BACKUPSET.. UNCATALOG command was entered. The UNCATALOG operation is not supported with backup set.

Action: Use CHANGE BACKUPSET.. DELETE instead.

RMAN-06123: operation not supported without the recovery catalog or mounted control file

Cause: A command was used which requires a connection to a recovery catalog database or the target database to be mounted. The command cannot be used when no backup repository is available.

Action: If a recovery catalog database is available, then connect to the recovery catalog and retry the command, otherwise enter a different command.

RMAN-06124: error while looking up datafile copy key: number

Cause: An error occurred while looking up the specified datafile copy key in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure.

RMAN-06125: error while looking up archived log key: number

Cause: An error occurred while looking up the specified archived log key in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure.

RMAN-06126: skipping offline file string

Cause: The indicated file will not be included in the backup set because it is offline and the SKIP OFFLINE option was specified.

Action: No action is required.

RMAN-06127: skipping read-only file string

Cause: The indicated file will not be included in the backup set because it is read only and the SKIP READONLY option was specified.

Action: No action is required.

RMAN-06128: skipping inaccessible file string

Cause: The indicated file will not be included in the backup set because it could not be read, and the SKIP INACCESSIBLE option was specified.

Action: No action is required.

RMAN-06129: invalid reserved channel ID: string

Cause: The specified channel id is invalid. DELETE and DEFAULT are reserved channel names and may not be specified by users.

Action: Specify a different channel ID.

RMAN-06131: SKIP OFFLINE/READONLY only allowed with current control file

Cause: The SKIP OFFLINE and SKIP READONLY options are only permitted when the target database control file is current. When the target control file is not current, it is not possible to obtain a datafile's offline/read only status.

Action: Remove the skip option or mount a current control file on the target database.

RMAN-06132: cannot backup datafile string because it is not in the control file

Cause: A backup command was issued that includes the specified datafile, but the datafile is not listed in the control file. The control file is not current (it is a backup or a created control file).

Action: Recover the control file to make it current, then retry the backup command.

RMAN-06133: recovery catalog may have obsolete data for datafile string

Cause: A RESTORE UNTIL was issued, and the recovery catalog choose an older incarnation of the datafile than is listed in the control file.

Action: If the recovery catalog has correct data for the datafile, then restore a backup control file using the same UNTIL clause, then retry the datafile restore. Otherwise, restore a backup of the incarnation of the datafile listed in the control file.

RMAN-06134: host command complete

Cause: An operating system command has completed.

Action: None - this is an informational message.

RMAN-06135: error executing host command: string

Cause: A host command returned a non-zero return code.

Action: Correct the offending command.

RMAN-06136: ORACLE error from auxiliary database: string

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-06137: must have recovery catalog for REPORT SCHEMA AT TIME

Cause: A 'REPORT SCHEMA at\_clause' command was issued, but there is no recovery catalog database.

Action: If you are not using a recovery catalog, then you may only issue the 'REPORT SCHEMA' command with no at\_clause.

RMAN-06138: control file not mounted - must specify AT clause with REPORT command

Cause: A 'REPORT SCHEMA' with no at\_clause was issued, and there is no recovery catalog, and there is also no control file mounted at the target database, so there is no place to get the information about the current list of files comprising the database.

Action: Use a recovery catalog or mount a control file at the target database.

RMAN-06139: WARNING: control file is not current for REPORT SCHEMA

Cause: A 'REPORT SCHEMA' with no at\_clause was issued, and there is no recovery catalog, and the control file mounted by the target instance is not current, so the information about the current list of datafiles may not be current.

Action: Use a recovery catalog or mount a current control file.

RMAN-06140: cannot specify TAG option with LIST INCARNATION

Cause: The TAG option was specified with LIST INCARNATION. This is not permitted because there is no TAG associated with a database incarnation.

Action: Remove the TAG option and re-run the LIST command.

RMAN-06141: cannot specify ARCHIVELOG LIKE option with RESTORE

Cause: The ARCHIVELOG LIKE option was specified with RESTORE. This is not permitted because recovery catalog contains only those records that are not deleted from disk.

Action: Remove the ARCHIVELOG LIKE option and re-run the command.

RMAN-06142: DEVICE TYPE cannot be specified with this command

Cause: The DEVICE TYPE option was specified with a command that does not support it.

Action: Remove the DEVICE TYPE option and re-run the command.

RMAN-06143: LIKE may only be specified with COPY

Cause: The LIKE option was specified with a RMAN command. This is not permitted because only copies of datafiles, control files or archived logs have file names that may be tested with a LIKE operand.

Action: Remove the LIKE option and re-run the RMAN command.

RMAN-06144: FROM or UNTIL may not be specified with LIST INCARNATION

Cause: The FROM or UNTIL option was specified with LIST INCARNATION. This is not permitted because there is no time associated with a database incarnation.

Action: Remove the FROM or UNTIL option and re-run the LIST command.

RMAN-06145: control file is not current - obsolete file list may be incomplete

Cause: A CHANGE or REPORT command needs to compute the list of backups that are redundant and may be deleted. If the mounted control file is not current, it may not be possible to determine if a satisfactory backup exists for files which have been offline since the last OPEN RESETLOGS.

Action: No action need be taken - this is an informational message only. To ensure a complete report of obsolete backups, mount a current control file.

RMAN-06146: changes found for file number beyond offline SCN

Cause: A CHANGE or REPORT command needs to compute the list of backups that are redundant and may be deleted. A backup was found for a file which is shown as offline in the target database control file, but the backup contains changes beyond the system change number(SCN) when the file went offline. This is most likely because the target database control file is not really current, but is a restored copy of an older control file.

Action: Mount a current control file or a backup control file.

RMAN-06147: no obsolete backups found

Cause: A CHANGE or REPORT command could find no files that meet the specified criteria for obsoleteness.

Action: None - this is an informational message.

RMAN-06148: redundancy count must be greater than zero

Cause: The REDUNDANCY operand specified for a CHANGE or REPORT OBSOLETE command was zero.

Action: Specify a REDUNDANCY operand of 1 or greater.

RMAN-06150: auxiliary name for datafile number set to: string

Cause: This message is issued in response to a CONFIGURE AUXNAME command.

Action: None - this is an informational message.

RMAN-06151: datafile string creation SCN string

Cause: This is an informational message. It should be accompanied by other messages.

Action: None

RMAN-06153: validation failed for datafile copy

Cause: The CHANGE DATAFILECOPY VALIDATE command discovered that the datafile copy could not be found or no longer contains the same data, so its record was deleted from the recovery catalog or target database control file.

Action: None - this is an informational message.

RMAN-06154: validation succeeded for datafile copy

Cause: The CHANGE DATAFILECOPY VALIDATE command discovered that the datafile copy still matches its data in the recovery catalog or target database control file.

Action: None - this is an informational message.

RMAN-06155: validation failed for control file copy

Cause: The CHANGE CONTROLFILECOPY VALIDATE command discovered that the control file copy could not be found or no longer contains the same data, so its record was deleted from the recovery catalog or target database control file.

Action: None - this is an informational message.

RMAN-06156: validation succeeded for control file copy

Cause: The CHANGE CONTROLFILECOPY VALIDATE command discovered that the control file copy still matches its data in the recovery catalog or target database control file.

Action: None - this is an informational message.

RMAN-06157: validation failed for archived log

Cause: The CROSSCHECK ARCHIVELOG command determined that the archived log could not be found or no longer contained the same data, so its record was marked expired.

Action: None - this is an informational message.

RMAN-06158: validation succeeded for archived log

Cause: The CROSSCHECK ARCHIVELOG command or VALIDATE HEADER option determined that the archived log still matches its data.

Action: None - this is an informational message.

RMAN-06159: error while looking up backup set

Cause: An error occurred while looking up the specified backup set in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. Ensure that the key is entered correctly. If the backup set was created when the recovery catalog was not available, then a RESYNC CATALOG must be done to update the recovery catalog.

RMAN-06160: no backup pieces found for backup set key: number

Cause: No backup pieces for the requested backup set were found in the recovery catalog, or the target database control file.

Action: Specify an existing backup set.

RMAN-06161: error when inspecting auxiliary file name: string

Cause: This error is accompanied by other errors explaining the cause.

Action: Correct the auxiliary file name if it is wrong via the CONFIGURE AUXNAME command.

RMAN-06162: sql statement: string

Cause: This is the sql statement about to be executed for a SQL command.

Action: None, informational message only.

RMAN-06163: some datafiles cannot be recovered, aborting the RECOVER command

Cause: This message should be followed by one or more 6162 or 6164 messages.

Action: Check the accompanying errors.

RMAN-06164: WARNING: no channel of required type allocated to recover datafile number

Cause: A RECOVER command could not proceed because incremental backup sets or archived log backup sets exist on a device type that has not been allocated.

Action: Use the LIST command to determine which device type is needed, then allocate a channel of that type.

RMAN-06165: datafile string is too old to recover, restore a more recent copy

Cause: The archived logs and/or incremental backup sets required to recover the datafile do not exist, but a more recent backup of the datafile exists which can be recovered.

Action: Issue a RESTORE for the datafile, then reissue the RECOVER command.

RMAN-06166: datafile string cannot be recovered

Cause: Incremental backups or archived redo logs needed to recover the datafile cannot be found, and no recoverable full backup or datafile copy exists.

Action: Use the LIST command to see if there is a backup set or datafile copy that can be made AVAILABLE. If not, then the datafile is unrecoverable. If a full or datafile copy exists, then a Point-in-Time Recovery may be possible.

RMAN-06167: already connected

Cause: a CONNECT command was issued, but RMAN is already connected to the specified database.

Action: RMAN has no DISCONNECT command, so to connect to a different instance, exit RMAN and start it again.

RMAN-06168: no backup pieces with this tag found: string

Cause: A tag was used to specify a list of backup pieces, but no backup pieces with this tag could be found.

Action: Make sure the tag is specified correctly.

RMAN-06169: could not read file header for datafile string error reason string

Cause: The specified datafile could not be accessed. The reason codes are: 1 - file name is MISSINGxx in the control file 2 - file is offline 3 - file is not verified 4 - DBWR could not find the file 5 - unable to open file 6 - I/O error during read 7 - file header is corrupt 8 - file is not a datafile 9 - file does not belong to this database 10 - file number is incorrect 12 - wrong file version 15 - control file is not current

Action: If the error can be corrected, do so and retry the operation. The SKIP option can be used to ignore this error during a backup.

RMAN-06170: no control file copy found with offline range RECID string STAMP string datafile string

Cause: This offline range is needed for recovering the specified data file, but the offline range record has aged out of the current control file and no control file copy with the record could be accessed. At least 1 control file copy containing the offline range was found in the recovery catalog and was in AVAILABLE status.

Action: Query the RC\_CONTROLFILE\_COPY view for the names of all control file copies, then issue a CHANGE CONTROLFILECOPY... VALIDATE; command for them. Then reissue the RECOVER command.

RMAN-06171: not connected to target database

Cause: A command was issued but no connection to the target database has been established.

Action: Issue a CONNECT TARGET command to connect to the target database.

RMAN-06172: no AUTOBACKUP found or specified handle is not a valid copy or piece

Cause: A restore could not proceed because no AUTOBACKUP was found or specified handle is not a valid copy or backup piece. In case of restore from AUTOBACKUP, it may be the case that a backup exists, but it does not satisfy the criteria specified in the user's restore operands. In case of restore from handle, it may be the handle is not a backup piece or control file copy. In may be that it does not exist.

Action: Modify AUTOBACKUP search criteria or verify the handle.

RMAN-06173: SET NEWNAME command has not been issued for datafile string when restore auxiliary

Cause: Auxiliary type was specified for the control file, but no SET NEWNAME command has been previously issued for a datafile.

Action: Issue SET NEWNAME command for every datafile in the recovery set.

RMAN-06174: not connected to auxiliary database

Cause: An auxiliary command was issued but no connection to a auxiliary database has been established.

Action: Issue a CONNECT AUXILIARY command to connect to the auxiliary database.

RMAN-06175: deleted script: string

Cause: A DELETE SCRIPT command was executed.

Action: None, informational message only.

RMAN-06176: no recovery required; all files are read only or offline

Cause: A RECOVER DATABASE command does not need to recover any files because all of the files to be recovered are offline or read only. This can only occur when the SKIP clause includes the SYSTEM tablespace.

Action: None, informational message only

RMAN-06177: restore not done; all files read only, offline, or already restored

Cause: A RESTORE command does not need to restore any files, because all of the files to be restored are offline, read-only, or are already restored to their correct destinations.

Action: None, informational message only

RMAN-06178: datafile number not processed because file is offline

Cause: A RESTORE DATABASE or RECOVER DATABASE command omitted processing the indicated datafile because it is offline clean at the desired point-in-time.

Action: None, informational message only

RMAN-06179: datafile number not processed because file is read-only

Cause: A RESTORE DATABASE or RECOVER DATABASE command omitted processing the indicated datafile because it is part of a read-only tablespace at the desired point-in-time.

Action: None, informational message only

RMAN-06180: incremental backups require Enterprise Edition

Cause: A BACKUP command with INCREMENTAL LEVEL > 0 was specified.

Action: Use FULL, or INCREMENTAL LEVEL 0.

RMAN-06181: multiple channels require Enterprise Edition

Cause: Attempt to allocate more than 1 channel in a job.

Action: Remove all except one ALLOCATE CHANNEL command.

RMAN-06182: archived log string of thread string with sequence string larger than MAXSETSIZE

Cause: A BACKUP ARCHIVELOG command specified the MAXSETSIZE operand too low. The specified archived log is larger than MAXSETSIZE will allow.

Action: Increase MAXSETSIZE limit.

RMAN-06183: datafile or datafile copy string (file number string) larger than MAXSETSIZE

Cause: A BACKUP DATAFILE(copy) command specified the MAXSETSIZE operand too low. The specified datafile is larger than MAXSETSIZE will allow.

Action: Increase MAXSETSIZE limit.

RMAN-06184: duplicate object in backup specifier: string string

Cause: A backup command specifies the same datafile or copy of a data file multiple times.

Action: Eliminate the duplicates.

RMAN-06185: Recovery Manager incompatible with string database: RMAN number.number.number.number to number.number.number.number required

Cause: This version of recovery manager was incompatible with the indicated database or the DBMS\_BACKUP\_RESTORE package installed in the indicated database.

Action: If the database has been upgraded from an earlier version, ensure that the catxxxx.sql script has been run successfully. Re-install dbmsbkrs.sql and prvtbkrs.plb if necessary. Otherwise, use a version of RMAN within the range specified in the error message.

RMAN-06186: PL/SQL package string.string version string in string database is too old

Cause: The specified PL/SQL package is a version that is too old to work with this version of the Recovery Manager (RMAN).

Action: If the database indicated is CATALOG, then you can use the UPGRADE CATALOG command to upgrade the recovery catalog to the most current version. If the database is TARGET or AUXILIARY, then you must either upgrade the specified database or use an older version of RMAN.

RMAN-06187: control file copy string not found or out of sync with catalog

Cause: The indicated file is not found, or is found but is not the same file that the recovery catalog thinks it is. It is likely that some operation outside of Recovery Manager has altered the file, or that Recovery Manager has not resynced with the target database.

Action: Re-catalog the file and retry the operation.

RMAN-06188: cannot use command when connected to a mounted target database

Cause: An attempt was made to issue a command that can be used only when there is no connection to the target database or when the target database is not mounted.

Action: Dismount the database or restart RMAN and use the command before connecting to the target database.

RMAN-06189: current DBID number does not match target mounted database (number)

Cause: SET DBID was used to set a DBID that does not match the DBID of the database to which RMAN is connected.

Action: If the current operation is a restore to copy the database, do not mount the database. Otherwise, avoid using the SET DBID command, or restart RMAN.

RMAN-06190: PL/SQL package string.string version string in string database is not current

Cause: RMAN detected an old version of the specified package. RMAN will execute in backwards-compatible mode.

Action: No action is required, but certain features and bug-fixes may not be available when RMAN runs in backwards-compatible mode. If the database is CATALOG, then you can use the UPGRADE CATALOG command to upgrade the recovery catalog to the most current version. If the database is TARGET or AUXILIARY, then you must either upgrade the specified database or use an older version of RMAN. The files that must be run to upgrade the target or auxiliary database are dbmsrman.sql and prvtrman.plb.

RMAN-06191: PL/SQL package string.string version string in string database is too new

Cause: RMAN detected an incompatible version of the specified package.

Action: Use a newer version of recovery manager. Message 6439 indicates the minimum required version of recovery manager.

RMAN-06192: maximum value for MAXPIECESIZE or MAXSETSIZE must be between 1 Kb and 2048 Gb

Cause: Input size for MAXPIECESIZE or MAXSETSIZE was out of range.

Action: Specify a valid size and retry the command.

RMAN-06193: connected to target database (not started)

Cause: This is an informational message only.

Action: The database must be started before any other RMAN commands are issued.

RMAN-06194: target database instance not started

Cause: A command was issued that requires the target database instance be started.

Action: Issue a STARTUP command to start the instance.

RMAN-06195: auxiliary database not started

Cause: A command was issued that requires the auxiliary database instance be started.

Action: Issue a STARTUP AUXILIARY command.

RMAN-06196: Oracle instance started

Cause: A STARTUP command completed successfully.

Action: None, this is an informational message.

RMAN-06197: Total System Global Area string bytes

Cause: This is an informational message only.

Action: No action is required.

RMAN-06198: string string bytes

Cause: This is an informational message only.

Action: No action is required.

RMAN-06199: database mounted

Cause: This is an informational message only.

Action: No action is required.

RMAN-06200: Changed string objects to AVAILABLE status

Cause: This is an informational message only.

Action: No action is required.

RMAN-06201: Deleted string objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-06202: Deleted string EXPIRED objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-06203: Changed KEEP options for string objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-06204: Changed string objects to UNAVAILABLE status

Cause: This is an informational message only.

Action: No action is required.

RMAN-06205: Uncataloged string objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-06206: Crosschecked string objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-06207: WARNING: string objects could not be deleted for string channel(s) due

Cause: This is an informational message only.

Action: No action is required.

RMAN-06208: to mismatched status. Use CROSSCHECK command to fix status

Cause: This is an informational message only.

Action: No action is required.

RMAN-06209: List of failed objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-06210: List of Mismatched objects

Cause: This is an informational message only.

Action: No action is required.

RMAN-06211: ==========================

Cause: This is an informational message only.

Action: No action is required.

RMAN-06212: Object Type Filename/Handle

Cause: This is an informational message only.

Action: No action is required.

RMAN-06213: --------------- ---------------------------------------------------

Cause: This is an informational message only.

Action: No action is required.

RMAN-06214: string string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06215: List of objects that must perform same operation at other database

Cause: This is an informational message only.

Action: The specified list of objects were not accessible at connected target database. Re-run the CROSSCHECK command after connecting to database that has DB\_UNIQUE\_NAME displayed in output for the specified object.

RMAN-06216: WARNING: db\_unique\_name mismatch - string objects could not be updated

Cause: This is an informational message only.

Action: Run CROSSCHECK command after connecting to a primary or physical standby database that can access the specified objects.

RMAN-06217: not connected to auxiliary database with a net service name

Cause: A command that moves files from the target instance to the auxiliary instance was requested. Such a command requires a net service name be present in the connect string used to connect to the auxiliary instance.

Action: Issue a CONNECT AUXILIARY command and include a net serice name in the connect string. That service name must be valid on the target instance.

RMAN-06218: List of objects requiring same operation on database with db\_unique\_name string

Cause: This is an informational message only.

Action: The specified list of objects were not accessible by the target database. Re-run the same command after connecting to database that has DB\_UNIQUE\_NAME displayed in output for the specified object.

RMAN-06219: List of objects not associated with all known db\_unique\_names

Cause: This is an informational message only.

Action: The specified list of objects were not accessible by the target database. Re-run the same command after connecting to primary database or physical standby database that can access the specified objects.

RMAN-06220: Creating automatic instance, with SID='string'

Cause: No connection to the auxiliary instance was provided, but the command requires an auxiliary instance.

Action: No action is required unless you want to create a permanent database, in which case you should stop the command and re-run it, providing an auxiliary instance connection.

RMAN-06221: Removing automatic instance

Cause: RMAN is removing the automatic auxiliary instance that was created for this command.

Action: No action is required.

RMAN-06223: starting up automatic instance string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06224: Automatic instance created

Cause: This is an informational message only.

Action: No action is required.

RMAN-06225: shutting down automatic instance string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06226: Automatic instance removed

Cause: This is an informational message only.

Action: No action is required.

RMAN-06230: List of Stored Scripts in Recovery Catalog

Cause: This message is issued in response to a LIST SCRIPT NAMES command. The following fields are shown for each script that is stored in the recovery catalog: Header indicating to what database the script belongs. Script Name: name of the script. Description: comment associated with this script.

Action: No action is required.

RMAN-06238: List of Databases

Cause: This message is issued in response to a LIST DB\_UNIQUE\_NAME command. The following fields are shown for each database that is known to the recovery catalog: DB Key: This is the unique key which identifies this database in the recovery catalog. DB Name: The name of the database. DB ID: The database ID. This is a number which remains the same for the life of the database, even if the database name is changed. DB\_UNIQUE\_NAME: db\_unique\_name value for the database.

Action: No action is required.

RMAN-06246: List of Database Incarnations

Cause: This message is issued in response to a LIST INCARNATION OF DATABASE command. The following fields are shown for each database that is registered with the recovery catalog: DB Key: This is the unique key which identifies this database in the recovery catalog. Inc Key: This is the unique key which identifies this incarnation of the database in the recovery catalog. DB Name: The name of the database. DB ID: The database ID. This is a number which remains the same for the life of the database, even if the database name is changed. Status: 'YES' if this is the current incarnation of this database, otherwise 'NO'. Reset SCN: system change number (SCN) of the most recent RESETLOGS operation. Reset Time: Time of the most recent RESETLOGS operation.

Action: No action is required.

RMAN-06250: Report of files that need backup due to unrecoverable operations

Cause: An unlogged change (such as 'create table unrecoverable') has been made to this file, and the most recent backup of the file does not contain those changes.

Action: Take a backup of this file. If this file is lost before a backup is taken, then the unlogged modifications will be lost. The message indicates whether a full backup is required or whether a incremental backup will suffice.

RMAN-06263: string string string

Cause: This message is issued in response to the REPORT NEED BACKUP INCREMENTAL command, for those files which would use more than the specified number of incrementals during recovery.

Action: To reduce the number of incremental backups which would be used during recovery of this datafile, take a new full backup of this file now.

RMAN-06270: Report of files whose recovery needs more than number days of archived logs

Cause: This message is issued in response to the REPORT NEED BACKUP DAYS command for those files which need more than the specified number of days' archived logs for recovery.

Action: To reduce the number of log files needed for recovery of this datafile, take a new full or incremental backup now.

RMAN-06274: Report of files that must be backed up to satisfy number days recovery window

Cause: This message is issued in response to the REPORT NEED RECOVERY WINDOW OF n DAYS command for those files that must be backed up to satisfy specified retention policy.

Action: To satisfy specified recovery window for this datafile, take a new full or incremental backup now.

RMAN-06275: invalid number of days specified for report: string days

Cause: This message is issued in response to the REPORT NEED RECOVERY WINDOW OF n DAYS or REPORT NEED BACKUP DAYS n command when an invalid number of days was specified in input command.

Action: The number of days specified in REPORT command must be greater than zero.

RMAN-06280: Report of obsolete backups and copies

Cause: This message is issued in response to the REPORT OBSOLETE command. Each of the files listed is obsolete because it is more redundant than the level of redundancy specified in the REPORT command.

Action: Depending on your needs, you might need to take new backups.

RMAN-06290: Report of database schema for database with db\_unique\_name string

Cause: This message is issued in response to the REPORT SCHEMA command. The report shows the physical schema of the database at the indicated time. The following fields are shown for each datafile and tempfile: File: The file number. Size(MB): The size of the file in mega bytes. Tablespace: The name of the tablespace which contains this file. RB segs: YES if this file is part of a tablespace containing rollback segments, otherwise NO. Datafile/Tempfile Name: The file name. Maxsize(MB): Maximum file size to which file can be extended

Action: No action is required.

RMAN-06300: Report of files with less than number redundant backups

Cause: This message is issued when the REPORT NEED BACKUP REDUNDANCY command is used for those files which have less than the specified number of backups which can be used for recovery.

Action: Take another backup of the datafiles listed.

RMAN-06306: ====================

Cause: This message is issued in response to a LIST BACKUP DATABASE/TABLESPACE/DATAFILE command when some backups were taken with the PROXY option. If a recovery catalog is in use, then the information comes from the recovery catalog, otherwise it comes from the target database control file. The following fields are shown for each proxy datafile backup. Key: This is the unique key which identifies this proxy backup in the recovery catalog. This value can be used in a CHANGE command to change its status. If the target database control file is being used as the recovery catalog, then this field uniquely identifies this copy in the control file. File: The file number that this file was copied from. Status: This is the status of the file. Possible values are: A - Available U - Unavailable D - Deleted X - Expired Status 'U' will not be used if the target database control file is being used as the recovery catalog. Completion time: This is the date and time when the backup was created. This column will be printed in the default Oracle date format, unless overridden with a NLS\_DATE\_FORMAT environment variable. Ckp SCN: This is the checkpoint system change number (SCN) of the backup. The file contains all changes made at or before this SCN. Ckp time: This is the time that the file was last checkpointed. Handle: This is the media manager handle of the proxy backup.

Action: No action is required.

RMAN-06378: List of Backup Sets

Cause: This message is issued in response to a LIST BACKUP command.

Action: No action is required.

RMAN-06400: database opened

Cause: This is an informational message only.

Action: No action is required.

RMAN-06401: database is already started

Cause: A STARTUP command without the FORCE option was issued, but the target database is already started.

Action: Use the FORCE option if you want to restart the database.

RMAN-06402: Oracle instance shut down

Cause: This is an informational message only.

Action: No action is required.

RMAN-06403: could not obtain a fully authorized session

Cause: The most likely cause of this error is that one of the databases to which RMAN had previously connected is not started or has has been shutdown. Other error messages should identify exactly which database is the problem.

Action: Startup the database causing the problem.

RMAN-06404: database dismounted

Cause: This is an informational message only.

Action: No action is required.

RMAN-06405: database closed

Cause: This is an informational message only.

Action: No action is required.

RMAN-06406: deleted archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-06407: auxiliary instance file string deleted

Cause: This is an informational message only.

Action: No action is required.

RMAN-06408: recovery catalog upgraded to version string

Cause: This is an informational message issued by the UPGRADE CATALOG command. It indicates the version of the recovery catalog schema to which the recovery catalog was just upgraded. Note that this version number may not reflect the version number of your rman executable or target database, because the recovery catalog schema is not changed with each Oracle release.

Action: No action is required.

RMAN-06409: LIKE clause in LIST BACKUP OF ARCHIVELOG is not supported

Cause: LIST BACKUP OF ARCHIVELOG LIKE was used, which is not supported.

Action: Remove LIKE clause from command.

RMAN-06410: cannot use command when channels are allocated

Cause: An attempt was made to issue a command that can be used only when there are no allocated channels.

Action: Do not use the command, or de-allocate channels and use the command when no channels are allocated.

RMAN-06411: backup copies setting out of range (1-4): number

Cause: An attempt was made to set backup copies to an invalid value.

Action: Use a value in the specified range.

RMAN-06412: no proxy copy channel found

Cause: A proxy copy was started, but no allocated channel supports proxy copy. This could be because the media management software used by the target database does not support proxy copy, or because all of the allocated channels are of type DISK, which never support proxy copy.

Action: If this is a backup, then either allocate a non-disk channel, or do not use the PROXY option. If this is a restore, then a channel of the same type which created the proxy backup was allocated, but now does not support proxy copy. If proxy copy is no longer supported by the media management software at the target database, the CROSSCHECK or CHANGE commands should be used so that those backups will not be considered for further restores.

RMAN-06413: channel string does not support proxy copy

Cause: The channel which was specified for this backup or restore does not support proxy copy. This could be because the media management software used by the target database does not support proxy copy, or because the channel is of type DISK, which never supports proxy copy.

Action: If this is a backup, then either allocate a non-disk channel, or do not use the PROXY option. If this is a restore, then a channel of the same type which created the proxy backup was allocated, but now does not support proxy copy. If proxy copy is no longer supported by the media management software at the target database, the CROSSCHECK command should be used so that those backups will not be considered for further restores.

RMAN-06414: target database COMPATIBLE option does not support proxy copy

Cause: PROXY was specified, and the target database uses a media manager that supports proxy copy, but the COMPATIBLE initialization parameter of the target database must be 8.1.0 or greater to create proxy backups. If the database is downgraded to the earlier release that is specified in the COMPATIBLE parameter, then it will no longer be able to restore proxy backups.

Action: Either take a non-proxy backup or change the target database COMPATIBLE parameter.

RMAN-06415: file string cannot be proxy backed up

Cause: The PROXY option was specified, but the media management software used by the target database cannot back up the specified file using proxy copy. If PROXY ONLY was specified, then the backup is terminated. If PROXY was specified, then this file will be placed into a non-proxy backup set.

Action: Remove the ONLY option to place the files into a regular backup set, or contact the media management vendor if you believe that the media management software should support proxy copy of this file.

RMAN-06416: PROXY ONLY was specified and some files could not be proxy copied

Cause: PROXY ONLY was specified, and some of the files to be backed up could not be backed up by the media management software used by the target database. Message 6415 is issued for each file that cannot be proxy copied.

Action: Remove the ONLY option to place the files into a regular backup set, or contact the media management vendor if you believe that the media management software should support proxy copy of these files.

RMAN-06417: command not allowed when connected to a virtual private catalog

Cause: The command that was entered cannot be used while connected to a virtual private catalog.

Action: Connect to the base catalog and re-execute the command.

RMAN-06418: proxy incremental backups with level > 0 not supported

Cause: PROXY was specified for a non-level-zero incremental backup. Proxy backups may only be full or level 0 backups.

Action: Remove one of the conflicting options.

RMAN-06419: file string cannot be proxy restored from handle string

Cause: The media management software used by the target database indicated that it cannot restore the specified file from the specified backup handle.

Action: Consult the media management software documentation to find out why this restriction exists or contact the media management vendor.

RMAN-06420: some files could not be proxy restored - aborting restore

Cause: Some of the files to be restored could not be restored by the media management software used by the target database. Message 6419 is issued for each file that cannot be restored.

Action: Contact the media management vendor if you believe that the media management software should support proxy copy of these files. The CROSSCHECK or CHANGE commands can be used to remove these proxy copies from the catalog to prevent the RESTORE command from trying to restore from them.

RMAN-06421: sent command to channel: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06422: no channels found for SEND command

Cause: No channels with the specified names or device types were found. If no channel qualifiers were specified, then no channels were allocated.

Action: Specify a different channel type or allocate a channel of the desired type.

RMAN-06423: requested limit of number exceeds vendor limit of number

Cause: A command was used to set the backup piece size limit, but the media management software used by the target database cannot create backup pieces that large.

Action: Specify a smaller backup piece limit.

RMAN-06424: error while looking up proxy copy

Cause: An error occurred while looking up the specified proxy copy in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. Ensure that the name or key is entered correctly. If the proxy copy was created when the recovery catalog was not available, then a RESYNC CATALOG must be done to update the recovery catalog.

RMAN-06425: \<datafile pathname not available>

Cause: This is an informational message only.

Action: No action is required.

RMAN-06426: RECOVERY\_CATALOG\_OWNER role must be granted to user string

Cause: The CREATE CATALOG or UPGRADE CATALOG command was used, but the USERID that was supplied in the CATALOG connect string does not have the RECOVERY\_CATALOG\_OWNER role granted as a DEFAULT role.

Action: Grant the RECOVERY\_CATALOG\_OWNER role to the recovery catalog owner.

RMAN-06427: recovery catalog already exists

Cause: The CREATE CATALOG command cannot be used when the recovery catalog already exists.

Action: Use the UPGRADE CATALOG command to upgrade your recovery catalog to the most current release without losing any existing backup data. Use the DROP CATALOG command to remove an existing recovery catalog.

RMAN-06428: recovery catalog is not installed

Cause: A recovery catalog database connection has been made, but the recovery catalog tables and views have not been installed.

Action: If you mis-typed the recovery catalog owner USERID, then correct the USERID and reconnect to the recovery catalog. If this is the first time that you have signed on to Recovery Manager with this recovery catalog owner USERID, then use the CREATE CATALOG command to create the recovery catalog schema. Alternatively, exit RMAN and connect without specifying a recovery catalog connection.

RMAN-06429: string database is not compatible with this version of RMAN

Cause: The indicated database is not compatible with this version of the Recovery Manager (RMAN). Other messages have also been issued which detail the cause of the error.

Action: See the other messages. If the database is CATALOG, then you may be able to use the CREATE CATALOG or UPGRADE CATALOG commands to correct the problem. If the database is TARGET or AUXILIARY, then you must either upgrade the target database or use a newer version of the RMAN executable.

RMAN-06430: recovery catalog USERID cannot be SYS

Cause: A recovery catalog connection was made to USERID SYS. The recovery catalog must be created in a USERID other than SYS.

Action: Specify a different USERID in the CATALOG connect string.

RMAN-06431: recovery catalog created

Cause: This is an informational message issued by the CREATE CATALOG command.

Action: No action is required.

RMAN-06432: recovery catalog dropped

Cause: This is an informational message issued by the DROP CATALOG command.

Action: No action is required.

RMAN-06433: error installing recovery catalog

Cause: An error was received from the recovery catalog database while it was being installed. Another error message shows the error message from the server.

Action: The most common reasons for failure to install the recovery catalog are:

\- Lack of space in the recovery catalog database: allocate more space, use the DROP CATALOG command to remove any partially installed recovery catalog, and retry the command.

\- Object already exists: This is caused by a partial recovery catalog installation. Use the DROP CATALOG command to remove the partially installed recovery catalog and retry the command.

RMAN-06434: some errors occurred while removing recovery catalog

Cause: Some errors were received from the recovery catalog database while removing the recovery catalog.

Action: Correct the error(s) and retry the command. Note that Recovery Manager intercepts and ignores common errors, such as 'object not found', which can happen while removing a partially installed recovery catalog. Only serious errors will be displayed while removing the recovery catalog.

RMAN-06435: recovery catalog owner is string

Cause: This is an informational message issued by the UPGRADE CATALOG and DROP CATALOG commands.

Action: No action is required.

RMAN-06436: enter DROP CATALOG command again to confirm catalog removal

Cause: The DROP CATALOG command deletes the recovery catalog, rendering all database backups unusable, and should be used with care. The command must be entered twice to ensure that this is really what you want to do.

Action: If you really want to remove the recovery catalog, then enter the DROP CATALOG command again.

RMAN-06437: cannot drop catalog - catalog is newer than this RMAN

Cause: The DROP CATALOG command was entered, but the recovery catalog was created by a newer version of the Recovery Manager (RMAN). This version of RMAN may not be able to drop the entire recovery catalog.

Action: Use the version of RMAN which most recently created or upgraded the recovery catalog.

RMAN-06438: error executing package DBMS\_RCVMAN in string database

Cause: Recovery Manager requires the DBMS\_RCVMAN package in the SYS schema of the indicated database. Normally this package is installed during database creation. To re-create the package, run the files dbmsrman.sql and prvtrmns.plb.

Action: re-create the DBMS\_RCVMAN package in the SYS schema.

RMAN-06439: RMAN must be upgraded to version string to work with this package

Cause: This message indicates the minimum version of recovery manager required to use the package which was specified in message 6191.

Action: A newer version of RMAN must be used with this package.

RMAN-06440: virtual catalog dropped

Cause: This is an informational message issued by the DROP CATALOG command, when connected to a virtual private catalog. Note that dropping a virtual private catalog does not delete any data, because the catalog data is owned by the base catalog.

Action: No action is required.

RMAN-06441: cannot upgrade catalog - catalog is already newer than this RMAN

Cause: The recovery catalog is already at a version level that is greater than this version of the Recovery Manager. The UPGRADE CATALOG command is not needed.

Action: Either upgrade to a more recent Recovery Manager, or continue to use the current version. Message 6191 will be issued if the recovery catalog is too new to work with this version of Recovery Manager.

RMAN-06442: enter UPGRADE CATALOG command again to confirm catalog upgrade

Cause: The UPGRADE CATALOG command alters the recovery catalog schema. Although the recovery catalog is designed to be compatible with older versions of the Recovery Manager (RMAN), it is possible that an upgrade will remove support for older versions of RMAN.

Action: If you really want to upgrade the recovery catalog, then enter the UPGRADE CATALOG command again. If you are not going to use an older version of RMAN with this recovery catalog, then compatibility is not an issue. If you plan to also continue using an older version of RMAN with this recovery catalog then, before upgrading, consult the Migration Guide for the current Oracle release to determine if upgrading to the current version of the recovery catalog will remove support for older versions of RMAN.

RMAN-06443: error upgrading recovery catalog

Cause: An error was received from the recovery catalog database while upgrading the recovery catalog.

Action: Correct the error and retry the command. Note that the Recovery Manager intercepts and ignores common errors, such as 'column already exists,' which can happen if the recovery catalog has already been partially upgraded. Only serious errors will be displayed while upgrading the recovery catalog.

RMAN-06444: error creating string

Cause: During the CREATE CATALOG or UPGRADE CATALOG command, the indicated object could not be created due to errors.

Action: Make sure that the RECOVER.BSQ file has not been modified or damaged, and then if this error persists, contact Oracle support. If the error refers to one of the RMAN PL/SQL packages, connect to the recovery catalog owner and query the USER\_ERRORS view to find out the details of the compilation errors.

RMAN-06445: cannot connect to recovery catalog after NOCATALOG has been used

Cause: The CONNECT CATALOG command was used after the user had already specified the NOCATALOG option.

Action: Re-start rman if you wish to use a recovery catalog.

RMAN-06446: changed proxy copy unavailable

Cause: This is an informational message only.

Action: No action is required.

RMAN-06447: changed proxy copy available

Cause: This is an informational message only.

Action: No action is required.

RMAN-06448: uncataloged proxy copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-06449: deleted proxy copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-06450: crosschecked proxy copy: found to be 'string'

Cause: This is an informational message only.

Action: No action is required.

RMAN-06451: proxy copy handle=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06452: string package upgraded to version string

Cause: This is an informational message issued by the UPGRADE CATALOG command. It indicates the version to which the indicated package was just upgraded. Note that this version number may not reflect the version number of your rman executable or target database, because the recovery catalog packages are not changed with each Oracle release.

Action: No action is required.

RMAN-06453: RECOVERABLE may only be used with datafile objects

Cause: An attempt was made to use LIST... RECOVERABLE.. with OF CONTROLFILE or OF ARCHIVELOG.

Action: Remove the RECOVERABLE keyword and try again.

RMAN-06454: duplexed backups require Enterprise Edition

Cause: The SET COPIES or CONFIGURE BACKUP COPIES command was used to create more than one copy of each backup piece, but Enterprise Edition is not installed.

Action: Do not attempt to create more than one copy of each backup piece.

RMAN-06455: Tablespace Point-in-Time Recovery requires Enterprise Edition

Cause: Tablespace Point-in-Time Recovery was attempted, but Enterprise Edition is not installed.

Action: Do not attempt Tablespace Point-in-Time Recovery.

RMAN-06456: command is obsolete

Cause: This is an informational message only.

Action: No action is required.

RMAN-06457: UNTIL SCN (string) is ahead of last SCN in archived logs (string)

Cause: UNTIL SCN cannot be more than the last system change number (SCN) of the last archived log

Action: Check the UNTIL SCN.

RMAN-06458: AS COPY option cannot be used with RECOVERY FILES, RECOVERY AREA or DB\_RECOVERY\_FILE\_DEST

Cause: The RECOVERY FILES, RECOVERY AREA or DB\_RECOVERY\_FILE\_DEST was specified with AS COPY.

Action: Remove the AS COPY option and resubmit the command.

RMAN-06459: BACKUP <VALIDATE|DURATION> is not supported with PROXY

Cause: BACKUP <VALIDATE|DURATION> and PROXY were specified in the same backup command.

Action: Remove the incompatible option.

RMAN-06460: control file copy string cannot be backed up by proxy.

Cause: The PROXY option was specified, but proxy copy of control file is not supported. This file will be placed into a non-proxy backup set.

Action: No action required, this is an informational message.

RMAN-06461: current control file cannot be backed up by proxy.

Cause: The PROXY option was specified, but proxy copy of control file is not supported. This file will be placed into a non-proxy backup set.

Action: No action required, this is an informational message.

RMAN-06462: no backup sets found on device DISK that match specification

Cause: A backup set record specifier did not match an backup set on device DISK in the recovery catalog.

Action: Resubmit the command with a different backup set record specifier. The Recovery Manager (RMAN) LIST command can be used to display all backup sets that RMAN knows about.

RMAN-06463: Backup set key string cannot be backed up by proxy.

Cause: The PROXY option was specified, but proxy copy of backup set is not supported. This file will be placed into a non-proxy backup set.

Action: No action required, this is an informational message.

RMAN-06464: BACKUP BACKUPSET is not supported with VALIDATE option

Cause: BACKUP BACKUPSET and VALIDATE were specified in the same backup command.

Action: To VALIDATE BACKUPSET use 'validate' or 'restore validate' command.

RMAN-06465: configuration not implemented: string

Cause: The configuration is not implemented in the current release.

Action: Avoid using the command.

RMAN-06466: error parsing configuration string (string)

Cause: Unsupported configuration string is stored in recovery catalog or target database control file.

Action: Check compatibility matrix rman executable and target database and recover catalog. Use DBMS\_BACKUP\_RESTORE.DELETECONFIG to remove problematic configuration.

RMAN-06467: could not translate DBA: number

Cause: An error was received when calling DBMS\_RCVMAN

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-06468: Invalid Data Block Address: number

Cause: The DBA specified doesn't belong to the mentioned tablespace

Action: Check the DBA

RMAN-06469: could not translate corruption list

Cause: An error was received when calling DBMS\_RCVMAN

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-06470: DEVICE TYPE is supported only when automatic channels are used

Cause: The DEVICE TYPE option was specified with a BACKUP, RESTORE, RECOVER, DUPLICATE, CHANGE, VALIDATE, CROSSCHECK, or DELETE EXPIRED command. This option is allowed only when automatically allocated channels are used.

Action: Remove the DEVICE TYPE option and re-run the command. Or Remove all ALLOCATE commands and re-run the script so that channels are automatically allocated.

RMAN-06471: no configuration found to allocate channels for string

Cause: Device type configuration was not found in recovery catalog

Action: Setup device type configuration using configure command for required device type

RMAN-06472: channel id string is automatically allocated

Cause: Channel id was used on ALLOCATE/RELEASE command.

Action: Use other channel id that does not belong to reserved channel id's name space

RMAN-06473: SET DATABASE can only be used in case of DUPLICATE without TARGET connection

Cause: A SET DATABASE command was specified when connected to target database or not connected to an auxiliary instance.

Action: Specify the command only when not connected to a target database and when connected to an auxiliary instance in preparation to DUPLICATE without TARGET connection.

RMAN-06474: maintenance channels are not allocated

Cause: RELEASE CHANNEL was used without allocating any maintenance channels.

Action: Allocate maintenance channel before executing this command.

RMAN-06475: parallelism setting out of range (1-254): number

Cause: Parallelism for the device type in CONFIGURE PARALLELISM command is out of range

Action: Enter value of parallelism that are within the allowed range.

RMAN-06476: channel number out of range (1-254): number

Cause: Channel number entered in CONFIGURE CHANNEL command is out of range.

Action: Enter channel number within allowed range and retry the command. for this device and retry the command

RMAN-06477: configuration value length exceeds 1024

Cause: CONFIGURE CHANNEL command entered has configuration value greater than 1024 bytes.

Action: Reduce the length of CONFIGURE CHANNEL command options

RMAN-06478: WARNING: datafile copy 'string' cannot be found on disk

Cause: The CHANGE DATAFILECOPY AVAILABLE command was used, but the datafile copy cannot be found on disk.

Action: If the storage containing the datafile copy has been removed from the host, restore it and retry the command. If the datafile copy is permanently gone, then issue the CHANGE DATAFILECOPY DELETE command for this datafile.

RMAN-06479: WARNING: control file copy 'string' cannot be found on disk

Cause: The CHANGE CONTROLFILECOPY AVAILABLE command was used, but the control file copy cannot be found on disk.

Action: If the storage containing the control file copy has been removed from the host, restore it and retry the command. If the control file copy is permanently gone, then issue the CHANGE CONTROLFILECOPY DELETE command for this control file.

RMAN-06480: WARNING: archived log 'string' cannot be found on disk

Cause: The CHANGE ARCHIVELOG AVAILABLE command was used, but the archived log cannot be found on disk.

Action: If the storage containing the archived log has been removed from the host, restore it and retry the command. If the archived log is permanently gone, then issue the CHANGE ARCHIVELOG DELETE command for this archived log.

RMAN-06481: WARNING: backup piece 'string' cannot be found on the storage medium

Cause: The CHANGE BACKUPPIECE AVAILABLE command was used, but the backup piece cannot be found on the storage medium.

Action: If the storage containing the backup piece has been removed from the host, restore it and retry the command. If the backup piece is permanently gone, then issue the CHANGE BACKUPPIECE DELETE command for this backup piece.

RMAN-06482: WARNING: proxy copy 'string' cannot be found on the storage medium

Cause: The CHANGE PROXY AVAILABLE command was used, but the proxy copy cannot be found on disk.

Action: If the storage containing the proxy copy has been removed from the host, restore it and retry the command. If the proxy copy is permanently gone, then issue the CHANGE PROXY DELETE command for this proxy copy.

RMAN-06483: changed datafile copy expired

Cause: This is an informational message only.

Action: No action is required.

RMAN-06484: changed control file copy expired

Cause: This is an informational message only.

Action: No action is required.

RMAN-06485: changed archived log expired

Cause: This is an informational message only.

Action: No action is required.

RMAN-06486: changed backup piece expired

Cause: This is an informational message only.

Action: No action is required.

RMAN-06487: changed proxy copy expired

Cause: This is an informational message only.

Action: No action is required.

RMAN-06488: restore from AUTOBACKUP does not allow any other modifiers

Cause: A control file or SPFILE restore from AUTOBACKUP was attempted and other restore options were used.

Action: Do not specify any other options for the control file AUTOBACKUP restore.

RMAN-06489: no configuration found to allocate clone channel number for device type string

Cause: Target channel configuration could not be used for clone channel as it contains CONNECT option.

Action: Setup clone channel configuration using CONFIGURE CLONE command for required number and type of channels.

RMAN-06490: WARNING: limit of AUTOBACKUPS for the day has been reached

Cause: No more control file AUTOBACKUPS are possible in this day.

Action: This is a warning message, no action is required.

RMAN-06491: control file AUTOBACKUP format "string" contains more than one "string" format specifier

Cause: A CONTROLFILE AUTOBACKUP FORMAT cannot have more than one reserved format specifier.

Action: Specify only one reserved format specifier or use an alternative format.

RMAN-06492: control file AUTOBACKUP format "string" must specify a "string" format specifier

Cause: A reserved format specifier was not specified for the CONTROLFILE AUTOBACKUP FORMAT

Action: Add a specifier to the CONTROLFILE AUTOBACKUP FORMAT

RMAN-06493: only UNTIL TIME clause is allowed when performing a restore from AUTOBACKUP, found: string

Cause: For restoring a control file AUTOBACKUP only SET UNTIL TIME can be used. It is not possible to translate the others to a precise day.

Action: Specify SET UNTIL TIME to indicate the day to start the restore of a control file AUTOBACKUP.

RMAN-06494: string = string is out of range (string-string)

Cause: The specified parameter for restoring a control file AUTOBACKUP is out of the valid range.

Action: Change the parameter value to a valid number or do not specify it.

RMAN-06495: must explicitly specify DBID with SET DBID command

Cause: Restore of a control file AUTOBACKUP or ADVISE FAILURE was attempted when the database is not mounted.

Action: Specify the DBID of the database using SET DBID or mount the database.

RMAN-06496: must use the TO clause when the database is mounted or open

Cause: A control file restore was attempted when the database is mounted or open and no alternate destination was specified.

Action: Specify an alternate destination with the TO clause or dismount the database.

RMAN-06497: WARNING: control file is not current, control file AUTOBACKUP skipped

Cause: Control file AUTOBACKUP is not possible without a current control file.

Action: This is a warning message, no action is required.

RMAN-06498: skipping datafile string; already backed up string time(s)

Cause: The indicated datafile will not be included in the backup set. It is already backed up on the device requested and file is offline/read-only datafile. Use the FORCE option to override backup optimization.

Action: No action is required.

RMAN-06499: skipping archived log file string; already backed up string time(s)

Cause: The indicated log file will not be included in the backup set because it is already backed up on the device requested. Use FORCE option to override backup optimization.

Action: No action is required.

RMAN-06500: skipping backup set key string; already backed up string time(s)

Cause: The indicated backup set will not be copied because it is already backed up on the device requested. Use FORCE option to override backup optimization.

Action: No action is required.

RMAN-06501: skipping datafile string; already backed up on string

Cause: The indicated datafile will not be included in the backup set. It is already been backed up once, or before the since time specified.

Action: No action is required.

RMAN-06502: skipping archived log file string; already backed on string

Cause: The indicated log file will not be included in the backup set. It is already been backed up once, or before the since time specified.

Action: No action is required.

RMAN-06503: skipping backup set key string; already backed up on string

Cause: The indicated backup set will not be backed up. It has already been backed up on the device once, or before the since time specified.

Action: No action is required.

RMAN-06504: PROXY option with multiple backup copies is not supported

Cause: Multiple backup copies and PROXY option were specified in BACKUP command.

Action: Resolve the conflict.

RMAN-06505: specified DATABASE: string does not match previous DATABASE: string

Cause: SET DBID was used to set a DBID that translated into a database name that does not match newly specified database name or a previous SET DATABASE set a different database name.

Action: Verify that the correct DBID was specified or avoid using the SET DATABASE command.

RMAN-06506: the MAXSETSIZE option cannot be used with a backup backup set

Cause: The MAXSETSIZE option was specified for a backup backup set command.

Action: Remove the option and resubmit the command.

RMAN-06507: trying alternate file for archived log of thread number with sequence number

Cause: This is an informational message, appearing when an archived log was found out of sync with catalog database.

Action: No action is required.

RMAN-06508: MAXSETSIZE string KBYTES should be greater than block size string bytes

Cause: MAXSETSIZE configured or specified in backup command should be greater than database block size.

Action: Specify a larger MAXSETSIZE limit.

RMAN-06509: only SPFILE or control file can be restored from AUTOBACKUP

Cause: A datafile or archived log restore from AUTOBACKUP was attempted.

Action: Do not specify DATAFILE or ARCHIVELOG for restore from AUTOBACKUP.

RMAN-06510: RMAN retention policy is set to recovery window of number days

Cause: This is an informational message only.

Action: No action is required.

RMAN-06511: RMAN retention policy is set to redundancy number

Cause: This is an informational message only.

Action: No action is required.

RMAN-06512: copy will be obsolete on date string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06513: copy will never be obsolete

Cause: This is an informational message only.

Action: No action is required.

RMAN-06514: archived logs required to recover from this copy will not be kept

Cause: This is an informational message only.

Action: No action is required.

RMAN-06515: archived logs required to recover from this copy will expire when this copy expires

Cause: This is an informational message only.

Action: No action is required.

RMAN-06516: time specified in KEEP UNTIL clause must be be after today

Cause: KEEP UNTIL support only a future time.

Action: Correct the time and retry the command.

RMAN-06517: KEEP option is not supported for archived log backups

Cause: The KEEP option is not supported for archived logs.

Action: Either remove KEEP option and retry the command or don't specify archived logs for this backup.

RMAN-06518: backup will be obsolete on date string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06519: backup will never be obsolete

Cause: This is an informational message only.

Action: No action is required.

RMAN-06520: archived logs will not be kept or backed up

Cause: This is an informational message only.

Action: No action is required.

RMAN-06521: archived logs required to recover from this backup will expire when this backup expires

Cause: This is an informational message only.

Action: No action is required.

RMAN-06522: KEEP FOREVER option is not supported without the recovery catalog

Cause: The KEEP FOREVER option was used, but it requires a connection to a recovery catalog database. The KEEP FOREVER option cannot be used when the backup repository is the target database control file. This is because information about this backup cannot be permanently stored. (If information is stored just in the control file it will be aged out depending on CONTROL\_FILE\_RECORD\_KEEP\_TIME initialization parameter.)

Action: If a recovery catalog database is available, then connect to the recovery catalog and retry the command, otherwise use a different KEEP option. 6523, 1, "unused"

RMAN-06524: RMAN retention policy will be applied to the command

Cause: This is an informational message only.

Action: No action is required.

RMAN-06525: RMAN retention policy is set to none

Cause: Command DELETE OBSOLETE and REPORT OBSOLETE requires that either:

\* RMAN retention policy is not NONE or,

\* RMAN retention policy is specified with REPORT/DELETE command.

Action: Either configure RMAN retention policy with CONFIGURE command or specify it at the end of DELETE/REPORT command.

RMAN-06526: KEEP option cannot be used with incremental backup

Cause: The KEEP option was specified for a incremental backup.

Action: Remove the option and resubmit the command.

RMAN-06527: KEEP option is not supported for backup of backup sets

Cause: The KEEP option is not supported for backup of backup sets.

Action: Either remove KEEP option and retry the command or don't specify backup sets for this backup.

RMAN-06528: CHANGE... KEEP not supported for BACKUPPIECE

Cause: The CHANGE BACKUPPIECE... KEEP command was entered. KEEP attributes cannot be specified for backup pieces.

Action: Use CHANGE BACKUPSET... KEEP instead.

RMAN-06529: CHANGE... KEEP not supported for ARCHIVELOG

Cause: The CHANGE ARCHIVELOG... KEEP command was entered. KEEP attributes cannot be specified for archived logs.

Action: Use CHANGE BACKUPSET... KEEP instead.

RMAN-06530: CHANGE... KEEP LOGS not supported for backup set which contains archived logs

Cause: The CHANGE BACKUPSET... KEEP command was entered, but the BACKUPSET contains archived logs. Backup sets with archived logs cannot have KEEP attributes.

Action: Do not specify backup set with archived logs for the CHANGE BACKUPSET... KEEP command.

RMAN-06531: CHANGE... KEEP not supported for incremental BACKUPSET

Cause: The CHANGE BACKUPSET... KEEP command was entered, but the BACKUPSET is an incremental backup set. Incremental backup sets cannot have KEEP attributes.

Action: Do not specify a backup set with archived logs for the CHANGE BACKUPSET... KEEP command.

RMAN-06532: redundancy count must be greater than zero

Cause: The REDUNDANCY operand specified for the retention policy was zero.

Action: Specify a REDUNDANCY operand of 1 or greater.

RMAN-06533: KEEP... NOLOGS option cannot be used when datafiles are fuzzy

Cause: The KEEP... NOLOGS option was specified for a backup or copy of files in a fuzzy state. This kind of backup requires archived logs for recovery, so archived logs must be kept.

Action: Remove the KEEP... NOLOGS option or make sure the files are not in a fuzzy state and resubmit the command.

RMAN-06534: archived logs required to recover from this backup will be backed up

Cause: This is an informational message only. An archivelog backup will be created and kept so the specified backup can be recovered to a consistent state.

Action: No action is required.

RMAN-06535: LIST COPY OF SPFILE is not supported

Cause: LIST COPY OF SPFILE was used, which is not supported because SPFILE cannot have a copy.

Action: Remove SPFILE from the command.

RMAN-06536: BACKED UP... TIMES option is supported only for archived logs

Cause: The BACKUP UP... TIMES option was used as a qualifier. This option is supported only for archived logs.

Action: Remove the option and resubmit the command.

RMAN-06537: CHANGE... KEEP not supported for BACKUP

Cause: The CHANGE BACKUP... KEEP command was entered. KEEP attributes cannot be specified for copies and backup pieces in a single command.

Action: Use CHANGE BACKUPSET... KEEP instead.

RMAN-06538: The expected DB\_UNIQUE\_NAME is string, but found string

Cause: The is an informational message.

Action: Check other error messages associated with this message.

RMAN-06540: Tablespace string will be excluded from future whole database backups

Cause: This is an informational message only.

Action: No action is required.

RMAN-06541: Tablespace string will be included in future whole database backups

Cause: This is an informational message only.

Action: No action is required.

RMAN-06542: file string is excluded from whole database backup

Cause: The indicated file will not be included in the backup set because its tablespace is configured as excluded from backup.

Action: No action is required.

RMAN-06543: duplicate or conflicting LIST options: string and string

Cause: The indicated options conflict with each other or appear more than once in a LIST command.

Action: remove the duplicate/conflicting option from the command.

RMAN-06547: SYSTEM tablespace cannot be excluded from whole database backup

Cause: The SYSTEM tablespace must be included in whole database backup.

Action: Remove the SYSTEM tablespace from the CONFIGURE... EXCLUDE and retry the operation.

RMAN-06548: connected to auxiliary database: string (DBID=string)

Cause: This is an informational message only.

Action: No action is required.

RMAN-06549: connected to auxiliary database: string (not mounted)

Cause: This is an informational message only.

Action: No action is required.

RMAN-06550: clone database not mounted and db\_name not set in init.ora

Cause: The clone database "init.ora" file does not specify the DB\_NAME parameter.

Action: Add the DB\_NAME parameter to the clone database "init.ora" and restart the instance.

RMAN-06551: error while looking up datafile copy for file number: string

Cause: An error occurred while looking up the specified datafile copy in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure. If the datafile copy was created during a RESTORE with a new name, ensure that the RESTORE completed successfully.

RMAN-06552: newname for datafile number was set to NEW, but file was not restored

Cause: A SWITCH command was specified for a datafile, but the newname was set to NEW and the file was not restored. If newname is set to NEW, the file must be restored before issuing a SWITCH command.

Action: Correct and resubmit the SWITCH command.

RMAN-06553: DB\_CREATE\_FILE\_DEST must be set for SET NEWNAME... TO NEW

Cause: The SET NEWNAME... TO NEW option was specified but the OMF destination init parameter DB\_CREATE\_FILE\_DEST is not set.

Action: Supply a full name to the SET NEWNAME command or set DB\_CREATE\_FILE\_DEST at the target database.

RMAN-06554: WARNING: file string is in backup mode

Cause: A file which is being backed up or copied is in backup mode. RMAN will back up the file anyway, but files do not need to be put into backup mode before backing them up with RMAN.

Action: Use the ALTER TABLESPACE... END BACKUP statement, at the target database server, to take the files out of backup mode.

RMAN-06555: datafile string must be restored from backup created before string

Cause: An incomplete recovery session was started, but the file is in newer than the UNTIL TIME clause.

Action: Check the UNTIL TIME clause or restore the file from a sufficient old backup.

RMAN-06556: datafile string must be restored from backup older than SCN string

Cause: An incomplete recovery session was started, but the file is newer than the UNTIL clause.

Action: Check the UNTIL clause or restore the file from a sufficient old backup.

RMAN-06557: unable to restore archived log of thread number with sequence number

Cause: Restore of the specified archived log failed because the size of the archived log is larger than available disk space.

Action: One of the following: 1) Increase the MAXSIZE parameter and retry the command. 2) Free up disk space in the recovery area.

RMAN-06558: archived log size of number kb is bigger than available space of number kb

Cause: This message should be followed by one or more 6557 messages.

Action: Check the accompanying errors.

RMAN-06559: MAXSIZE must be larger than 1 kb

Cause: The MAXSIZE parameter is out of range.

Action: Specify a valid size and retry the command.

RMAN-06560: WARNING: backup set with key number will be read number times

Cause: This message should be followed by one or more 6562 messages.

Action: Check the accompanying messages.

RMAN-06561: available space must be larger than number kb

Cause: The recovery failed because it requires more disk space. One of the following could have caused this error: 1) The MAXSIZE option is used but is not large enough to restore files. 2) Files should be restored to recovery area, but available disk space is not large enough to restore files.

Action: One of the following: 1) Increase the MAXSIZE parameter and retry the command. 2) Free up disk space in the recovery area.

RMAN-06562: available space of number kb needed to avoid reading the backup set multiple times

Cause: A backup set is read more than once. Multiple reads of a backup set can slow restore performance. One of the following could have caused this: 1) The MAXSIZE option is used but is not large enough to restore files. 2) Files should be restored to a recovery area, but the available disk space is not large enough to restore files.

Action: One of the following: 1) Increase the MAXSIZE parameter and retry the command. 2) Free up disk space in the recovery area.

RMAN-06563: control file or SPFILE must be restored using FROM AUTOBACKUP

Cause: RESTORE CONTROLFILE or RESTORE SPFILE was specified without the FROM AUTOBACKUP option when RMAN is not connected to the recovery catalog.

Action: If the recovery catalog is available, connect to the recovery catalog and retry the restore. If the recovery catalog in not available, following is the procedure to restore control file or SPFILE:

1\. Specify the DBID of the database with the SET DBID command.

2\. If the AUTOBACKUP was created with non-default AUTOBACKUP format, then specify the AUTOBACKUP format using the SET CONTROLFILE AUTOBACKUP FORMAT command.

3\. If the backup was created with SBT device, then allocate an SBT channel using the ALLOCATE CHANNEL command.

4\. Restore control file or SPFILE by starting the RESTORE... FROM AUTOBACKUP command.

RMAN-06564: must use the TO clause when the instance is started with SPFILE

Cause: A restore of the SPFILE from AUTOBACKUP was attempted when the instance is started with SPFILE and no alternate destination was specified.

Action: Specify an alternate destination with the TO clause.

RMAN-06565: WARNING: string: sqlcode number was caught, automatic retry #number

Cause: The RMAN client caught a transient error and will automatically retry several times.

Action: No action required, this is an informational message.

RMAN-06566: target database incarnation not found in control file

Cause: RESETLOGS CHANGE# and/or time of the target database doesn't match any database incarnation in the control file.

Action: One of the following actions can be taken to resolve this error 1) Restore the control file from the incarnation. 2) To populate the new incarnation, inspect or restore an archived log/datafile/datafile copy/backup set from the target incarnation

RMAN-06567: connected to auxiliary database: string (DBID=string, not open)

Cause: This is an informational message only.

Action: No action is required.

RMAN-06568: connected to target database: string (DBID=string, not open)

Cause: This is an informational message only.

Action: No action is required.

RMAN-06569: DATABASE: string does not match previous DATABASE: string

Cause: SET DBID or SET DATABASE was used to specify the target database name which does not match specified database name in DUPLICATE command.

Action: Verify that the correct DBID or the correct DATABASE was specified or avoid specifying DATABASE in DUPLICATE command.

RMAN-06570: datafile number switched to datafile copy "string"

Cause: This message was issued in response to a SWITCH command.

Action: No action is required, this is an informational message.

RMAN-06571: datafile number does not have recoverable copy

Cause: The SWITCH command with the option TO COPY was specified but the datafile has no valid copy to switch to.

Action: Verify whether the datafile has a valid datafile copy.

RMAN-06572: database is open and datafile number is not offline

Cause: The SWITCH command with the option TO COPY was specified, but datafile is not offline and database is open.

Action: Either make sure the datafile is offline or the database must be mounted but not opened.

RMAN-06573: specified DBID: string does not match previous DBID: string

Cause: The DBID in the DUPLICATE command did not match the previously specified DBID in the SET DBID command.

Action: Verify that the correct DBID was specified or avoid using DBID in the DUPLICATE command.

RMAN-06575: platform id number found in datafile string header is not a valid platform id

Cause: The platform id found in the datafile header was not recognized.

Action: Verify that this is a valid datafile.

RMAN-06576: platform 'string' (number) found in header of datafile string does not match specified platform name 'string' (number)

Cause: The platform specified in the command did not match the platform found in the datafile header.

Action: Specify the correct platform name and retry the command.

RMAN-06577: FROM TAG option may only be used with datafile copies

Cause: The FROM TAG option was specified for datafiles.

Action: Remove the option and resubmit the command.

RMAN-06578: INCREMENTAL LEVEL > 0 must be specified with FOR RECOVER OF

Cause: The FOR RECOVER OF option was specified without specifying INCREMENTAL LEVEL > 0.

Action: Specify INCREMENTAL LEVEL > 0 and resubmit the command.

RMAN-06580: the string option cannot be used with AS COPY

Cause: The specified option was specified for a backup as copy command.

Action: Remove the option and resubmit the command.

RMAN-06581: option string not supported

Cause: This option was specified and it is not supported.

Action: Remove the specified option.

RMAN-06582: AS COPY option cannot be used when backing up backup sets

Cause: The backup set was specified with AS COPY.

Action: Remove the AS COPY option or remove the backup sets.

RMAN-06583: at least 1 channel of TYPE DISK must be allocated to use AS COPY option

Cause: No channel of TYPE DISK was allocated.

Action: Allocate a channel of TYPE DISK and re-issue the command or remove AS COPY.

RMAN-06584: WARNING: AS BACKUPSET option added due to allocation of multiple channel types

Cause: DISK and non DISK channels were allocated for a backup command. Configuration indicates to produce image copies to DISK, however due to the mixed channel types BACKUPSETS will be created on DISK.

Action: Do not allocate non DISK channels to produce image copies to DISK or allocate only non DISK channels to produce BACKUPSETS only.

RMAN-06585: no copy of datafile number found

Cause: An available datafile copy for the specified datafile could not be found.

Action: make sure that all specified datafiles have a copy available.

RMAN-06586: no copy of datafile number with tag string found

Cause: An available datafile copy for the specified datafile could not be found.

Action: make sure that all specified datafiles have a copy available.

RMAN-06587: one or more datafile copies were not found

Cause: This error message was accompanied by an additional error message or messages indicating the cause of the error.

Action: Follow the recommended actions of the additional error message or messages.

RMAN-06588: number of patterns (number) to DB\_FILE\_NAME\_CONVERT should be even

Cause: An uneven number of patterns was specified.

Action: Specify one more or one less pattern.

RMAN-06589: cannot specify DB\_FILE\_NAME\_CONVERT option without AS COPY

Cause: The DB\_FILE\_NAME\_CONVERT option was specified without AS COPY. This is not permitted for backup set backups where multiple files are combined into a set.

Action: Remove the DB\_FILE\_NAME\_CONVERT option and re-run the BACKUP command.

RMAN-06590: Tablespace string cannot be converted

Cause: The system tablespaces could not be transported to other platforms.

Action: Remove the specified tablespace from the CONVERT command and retry the operation.

RMAN-06593: platform name 'string' specified in FROM PLATFORM is not valid

Cause: The platform name was not recognized.

Action: Specify a valid platform name.

RMAN-06594: platform name 'string' specified in TO PLATFORM is not valid

Cause: The platform name was not recognized.

Action: Specify a valid platform name.

RMAN-06595: platform name 'string' does not match database platform name 'string'

Cause: The platform name specified did not match the name of the database performing the conversion.

Action: Specify the correct platform name.

RMAN-06596: string requires target database compatibility string, currently set to string

Cause: A command or option was used that requires a higher database compatibility than is currently set at the target database.

Action: Raise the compatibility of the database before attempting the command again.

RMAN-06597: conversion between platforms 'string' and 'string' is not implemented

Cause: Conversion of Oracle datafiles between the specified platforms was not supported.

Action: Do not do the conversion.

RMAN-06599: Tablespace string is not read-only

Cause: A conversion was attempted on a tablespace which is not read-only.

Action: Change the tablespace to read-only and retry the operation.

RMAN-06600: old RMAN configuration parameters:

Cause: This message is issued in response to a CONFIGURE command.

Action: No action is required, this is an informational message only.

RMAN-06601: new RMAN configuration parameters:

Cause: This message is issued in response to a CONFIGURE command.

Action: No action is required, this is an informational message only.

RMAN-06602: TO DESTINATION option can be used only for disk device

Cause: The TO DESTINATION option was specified for non-disk device.

Action: Remove the TO DESTINATION option and resubmit the command.

RMAN-06603: TO DESTINATION option must be specified with RECOVERY AREA, RECOVERY FILES or DB\_RECOVERY\_FILE\_DEST on disk device

Cause: RECOVERY FILES, RECOVERY AREA or DB\_RECOVERY\_FILE\_DEST option was specified in BACKUP command on disk device without specifying TO DESTINATION option.

Action: Specify TO DESTINATION option and retry the command.

RMAN-06604: new RMAN configuration parameters are successfully stored

Cause: This message is issued in response to a CONFIGURE command.

Action: No action is required, this is an informational message only.

RMAN-06605: old RMAN configuration parameters are successfully deleted

Cause: This message is issued in response to a CONFIGURE command.

Action: No action is required, this is an informational message only.

RMAN-06606: RMAN configuration parameters are successfully reset to default value

Cause: This message is issued in response to a CONFIGURE command.

Action: No action is required, this is an informational message only.

RMAN-06607: RMAN configuration parameters for database with db\_unique\_name string are:

Cause: This message is issued in response to a SHOW command.

Action: No action is required, this is an informational message only.

RMAN-06608: RMAN configuration has no stored or default parameters

Cause: This message is issued in response to a SHOW command.

Action: No action is required, this is an informational message only.

RMAN-06609: AS COPY can be configured only for disk device

Cause: The AS COPY option was specified for non-disk device.

Action: Remove the AS COPY option and resubmit the command.

RMAN-06610: For record type string RECIDS from number to number are re-used before resync

Cause: This messages is issued when the control file records were re-used before resyncing to catalog database.

Action: Increase control\_file\_keep\_record\_time setting or issue BACKUP command that it will generate fewer control file records, e.g., backup few tablespaces instead of the complete database in one BACKUP command.

RMAN-06611: Following RMAN configuration applied before deleting logs:

Cause: This message is issued in response to a DELETE command.

Action: No action is required, this is an informational message only.

RMAN-06612: Incompatible options were specified for archivelog deletion policy

Cause: Incompabitle options were specified on CONFIGURE ARCHIVELOG DELETION POLICY command.

Action: Remove incompabitle options and retry the command. BACKED UP option can be used individually or combined with SHIPPED or APPLIED option. Following are invalid combination of options: a) TO NONE cannot be used with other options b) SHIPPED ON STANDBY and SHIPPED ON ALL STANDBY cannot be used together. c) APPLIED ON STANDBY and APPLIED ON ALL STANDBY cannot be used together. d) SHIPPED and APPLIED cannot be used together.

RMAN-06613: Connect identifier for DB\_UNIQUE\_NAME string not configured

Cause: The connect identifier for the specified DB\_UNIQUE\_NAME initialization parameter was not configured.

Action: Do one of the following:

\- If the DB\_UNIQUE\_NAME belongs to a connected target database, then define the DB\_UNIQUE\_NAME parameter in LOG\_ARCHIVE\_DEST\_n at the remote database from where the resynchronization is performed. Otherwise, define DB\_UNIQUE\_NAME parameter in LOG\_ARCHIVE\_DEST\_n at the target database. Or,

\- Configure the appropriate connect identifier using the CONFIGURE DB\_UNIQUE\_NAME RMAN command and rerun the command.

RMAN-06614: DB\_UNIQUE\_NAME string is too long

Cause: The DB\_UNIQUE\_NAME initialization parameter string was too long.

Action: Configure the appropriate DB\_UNIQUE\_NAME initialization parameter string and re-run the command.

RMAN-06615: resyncing from database with DB\_UNIQUE\_NAME string

Cause: Resync was performed remotely for the specified DB\_UNIQUE\_NAME initialization parameter without connecting to it as target database. This type of remote resync has limitations. For example, RMAN output cannot be resynced. Please refer to RMAN documentation for a complete set of limitations.

Action: This is an informational message.

RMAN-06616: RMAN output not resynced for database with DB\_UNIQUE\_NAME string

Cause: V$RMAN\_OUTPUT contents were not rescyned when the RESYNC CATALOG FROM DB\_UNIQUE\_NAME command was executed."

Action: This is an informational message.

RMAN-06617: UNTIL TIME (string) is ahead of last NEXT TIME in archived logs (string)

Cause: UNTIL TIME was more than the last NEXT TIME of the last archived log.

Action: Check the UNTIL SCN.

RMAN-06700: error parsing text script in file string

Cause: Incorrect syntax or invalid commands were found.

Action: Fix text script and retry the command.

RMAN-06701: could not construct path for file: "string"

Cause: An error was encountered when trying to construct the full pathname for the specified file.

Action: Ensure that the path is correct.

RMAN-06702: could not initialize for input file: "string"

Cause: An error was encountered when trying to initialize the specified file for input.

Action: Ensure that the file exists.

RMAN-06703: could not open file: "string" (reason=string)

Cause: An error was encountered when trying to open the specified file.

Action: Ensure that the file has correct permissions.

RMAN-06705: text script line is too long (>1024)

Cause: A text script contained a line longer than the permitted maximum length.

Action: Split the line in smaller lines an retry the operation.

RMAN-06706: could not close file: "string" (reason=string)

Cause: An error was encountered when trying to close the specified file.

Action: Ensure that the file has correct permissions and still exists.

RMAN-06707: could not initialize for output file: "string"

Cause: An error was encountered when trying to initialize the specified file for output.

Action: Ensure that the file exists.

RMAN-06708: short write while writing file "string". Wrote string bytes instead of string bytes

Cause: An attempt was made to write to a file system that was full.

Action: Ensure that the file system has room for the file. Check system logs.

RMAN-06709: No scripts in recovery catalog

Cause: An attempt was made to list the scripts in the catalog, but no scripts could be found in the specified recovery catalog.

Action: No action required, this is an informational message only.

RMAN-06710: script string not found in catalog

Cause: An attempt was made to call a script that could not be found in the target database or as a global script in the specified catalog.

Action: Verify the script name and retry the command.

RMAN-06711: global scripts require a TARGET connection

Cause: Connection to a TARGET database was not specified.

Action: Provide a TARGET connection and retry the command.

RMAN-06716: skipping datafile number; already restored to file string

Cause: Recovery Manager determined that this file is already restored. Use FORCE option to override this optimization.

Action: No action required, this is an informational message only.

RMAN-06717: Could not delete auxiliary instance file string

Cause: Auxiliary instance file was not deleted. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-06724: backup not done; all files already backed up

Cause: A BACKUP command does not need to backup any files, because all of the files to backup are already backed up.

Action: No action required, this is an informational message only.

RMAN-06725: database not open: sort area size too small

Cause: sort area size too small to execute RMAN commands.

Action: open the database or increase sort\_area\_size.

RMAN-06726: could not locate archived log string

Cause: The specified archived log could not be found on any allocated channel.

Action: Allocate additional channels on other nodes of the cluster or, if the archived logs has been deleted, use the CROSSCHECK ARCHIVELOG command to correct the recovery catalog or target database control file entries.

RMAN-06727: could not locate datafile copy string

Cause: The specified datafile copy could not be found on any allocated channel.

Action: Allocate additional channels on other nodes of the cluster or if the datafile copy has been deleted, use the CROSSCHECK DATAFILECOPY command to correct the recovery catalog or target database control file entries.

RMAN-06728: could not locate control file copy string

Cause: The specified control file copy could not be found on any allocated channel.

Action: Allocate additional channels on other nodes of the cluster or if the control file copy has been deleted, use the CROSSCHECK CONTROLFILECOPY command to correct the recovery catalog or target database control file entries.

RMAN-06729: no backup of the SPFILE found to restore

Cause: A SPFILE restore could not proceed because no backup of the SPFILE was found. It may be the case that a backup of this file exists but does not satisfy the criteria specified in the user's restore operands.

Action: Modify options for the SPFILE restore.

RMAN-06730: no channel to restore a backup of the SPFILE

Cause: A SPFILE restore could not proceed because the backup on a device type that was not allocated for restore.

Action: No action required, this is an informational message only. See message 6026 for further details.

RMAN-06731: command string:string% complete, time left number:number:number

Cause: This is an informational message only.

Action: No action is required.

RMAN-06732: database dropped

Cause: This is an informational message only.

Action: No action is required.

RMAN-06733: database unregistered from the recovery catalog

Cause: This is an informational message only.

Action: No action is required.

RMAN-06737: database name "string" does not match target database name "string"

Cause: The UNREGISTER DATABASE command was used with a database name that does not match the name of the database to which RMAN is connected.

Action: Specify the correct database name or avoid specifying the database name when connected to the target database.

RMAN-06738: database name "string" is not unique in the recovery catalog

Cause: The UNREGISTER DATABASE command was used with a database name that is ambiguous.

Action: Use the SET DBID command to specify the database id and resolve the ambiguity.

RMAN-06739: database "string" is not found in the recovery catalog

Cause: The UNREGISTER DATABASE command was used with a database name that was not found in the recovery catalog.

Action: Make sure the database name specified in the DROP DATABASE command syntax is correct.

RMAN-06740: database name is not specified

Cause: The command failed because of the following:

o RMAN is not connected to the target database

o The database name is not specified in the command

o DBID is not set with the SET DBID command

Action: Any one of the following actions will fix the problem: o Connect to the target database o Specify database name o Set DBID with SET DBID command

RMAN-06741: database name is "string" and DBID is string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06742: platform name 'string' longer than number

Cause: The specified platform name exceeds the maximum allowable platform name.

Action: Correct the platform name.

RMAN-06743: specification does not match any backup set in the repository

Cause: The specified backup sets were not found in the recovery catalog or target database control file.

Action: Verify backup set existence and retry the command.

RMAN-06744: specification does not match any datafile copy in the repository

Cause: The specified datafile copies were not found in the recovery catalog or target database control file.

Action: Verify datafile copy existence and retry the command.

RMAN-06745: skipping datafile copy string; already backed up string time(s)

Cause: The indicated datafile copy was not included in the backup set because it was already backed up on the device requested.

Action: Use FORCE option to override backup optimization.

RMAN-06746: backup cancelled because there are no files to backup

Cause: There were no files or all files were skipped for this backup set, therefore no backup set was created.

Action: This message is informational only.

RMAN-06747: at least 1 channel of tertiary storage must be allocated to execute this command

Cause: The executed command requires a SBT channel, but no channels of type SBT were configured or allocated.

Action: ALLOCATE or CONFIGURE a SBT channel.

RMAN-06748: more than one channel types were allocated

Cause: RECOVERY FILES, RECOVERY AREA or DB\_RECOVERY\_FILE\_DEST option was specified in BACKUP command, but more than one channel types was used and no DEVICE TYPE or CHANNEL option was specified.

Action: Specify CHANNEL or DEVICE TYPE option and retry the command.

RMAN-06749: restore point string does not exist.

Cause: The specified restore point does not exists in v$restore\_point table of the target database.

Action: Check the name of restore point and retry the command.

RMAN-06750: SPFILE cannot be backed up by proxy.

Cause: The PROXY option was specified, but proxy copy of SPFILE is not supported. This file will be placed into a non-proxy backup set.

Action: No action required, this is an informational message only.

RMAN-06751: ASM file string cannot be proxy backed up.

Cause: The PROXY option was specified, but proxy copy of ASM file is not supported. This file will be placed into a non-proxy backup set.

Action: No action required, this is an informational message only.

RMAN-06752: error while looking up tempfile: string

Cause: An error occurred while looking up the specified tempfile in the recovery catalog or target database control file.

Action: This error is accompanied by other errors describing the reason for the failure; see those error messages for further information. One possible problem is that the tempfile name was not entered correctly.

RMAN-06753: tempfile not found in the repository

Cause: The specified tempfile is not found in the control file or recovery catalog.

Action: Make sure that the tempfile name is correct and retry

RMAN-06754: INCREMENTAL FROM SCN option is not supported with \[string\]

Cause: The INCREMENTAL FROM SCN option was supplied but does not apply to this type of backup.

Action: Remove the INCREMENTAL FROM SCN operand and re-enter the command.

RMAN-06755: WARNING: datafile string: incremental-start SCN is too recent; using checkpoint SCN string instead

Cause: The incremental-start sysetm change number (SCN) which was specified when starting an incremental datafile backup is greater than the datafile checkpoint SCN, which could cause some blocks to be missed.

Action: Specify a smaller incremental-start system change number (SCN).

RMAN-06756: cannot flashback database to non-guaranteed restore point string when flashback is off

Cause: The indicated restore point was not guaranteed and flashback was disabled. When flashback is disabled, Oracle can flashback only to guaranteed restore point.

Action: Specify a guaranteed restore point or turn on flashback and retry the command. the command.

RMAN-06757: DB\_UNIQUE\_NAME "string" does not match target database ("string")

Cause: The value specified in the FOR DB\_UNIQUE\_NAME option did not match the DB\_UNIQUE\_NAME parameter setting of the target database.

Action: Use the RMAN STARTUP command, with no parameter file option, to start the target database without a parameter file, then run the RESTORE SPFILE command again.

RMAN-06758: DB\_UNIQUE\_NAME is not unique in the recovery catalog

Cause: RMAN could not identify which SPFILE to restore for this target database, because the recovery catalog contained two or more different instances of this database, each with different DB\_UNIQUE\_NAME values.

Action: Use the FOR DB\_UNIQUE\_NAME option to specify the name of the instance whose parameter file you want to restore.

RMAN-06759: skipping datafile copies that are already backed up

Cause: Some datafile copies were not be backed up because they were already backed up on the device requested.

Action: No action is required. You can use the FORCE option to override backup optimization and force these files to be backed up.

RMAN-06760: skipping archived logs that are already backed up

Cause: Some archived logs were not be backed up because they were already backed up on the device requested.

Action: No action is required. You can use the FORCE option to override backup optimization and force these files to be backed up.

RMAN-06761: skipping backup sets that are already backed up

Cause: Some backup sets were not be backed up because they were already backed up on the device requested.

Action: No action is required. You can use the FORCE option to override backup optimization and force these files to be backed up.

RMAN-06762: ignoring encryption for proxy or image copies

Cause: This information message is displayed when the RMAN client is generating proxy or image copies and encryption was enabled for the input files.

Action: This is an informational message only.

RMAN-06763: specified encryption algorithm not supported

Cause: An encryption algorithm not supported by the database is specified during backup.

Action: Refer to contents of v$rman\_encryption\_algorithms view for the list of supported encryption algorithm. Specify a valid encryption algorithm and retry the command.

RMAN-06764: string

Cause: An error occurred when processing user request.

Action: None

RMAN-06765: Tablespace string will be encrypted in future backup sets

Cause: This is an informational message only.

Action: No action is required.

RMAN-06766: Tablespace string will not be encrypted in future backup sets

Cause: This is an informational message only.

Action: No action is required.

RMAN-06767: Tablespace string will default to database encryption configuration

Cause: This is an informational message only.

Action: No action is required.

RMAN-06768: duplicate or conflicting options are specified: string and string

Cause: An error occurred when processing the command because user specified two duplicate options or the two options are not allowed to be used together.

Action: Remove one of the above options and retry the command.

RMAN-06769: length of password must be greater than zero

Cause: Zero length password was specified for encrypted backups.

Action: Retry the command using a password with non-zero length.

RMAN-06770: backup encryption requires Enterprise Edition

Cause: The backup command tried to create encrypted backups, but Enterprise Edition is not installed.

Action: Do not create encrypted backups.

RMAN-06771: cannot do IMPORT CATALOG after NOCATALOG has been used

Cause: The IMPORT CATALOG command was used after the NOCATALOG option was already specified.

Action: Restart RMAN and connect to recovery catalog if you wish to IMPORT CATALOG.

RMAN-06772: cannot do IMPORT CATALOG before connecting to recovery catalog

Cause: The IMPORT CATALOG command was used before connecting to the recovery catalog.

Action: Connect to recovery catalog using CONNECT CATALOG command if you wish to IMPORT CATALOG.

RMAN-06773: connected to source recovery catalog database

Cause: This is an informational message only.

Action: No action is required.

RMAN-06774: must specify a TNS service name for source recovery catalog database

Cause: The connect string does not contain TNS service name. IMPORT CATALOG without TNS service name is not supported.

Action: Specify a service name and resubmit the command.

RMAN-06775: not connected to source recovery catalog database

Cause: IMPORT CATALOG command was issued but no connection to the source recovery catalog database has been established.

Action: Resubmit IMPORT CATALOG command with correct connect string.

RMAN-06776: source recovery catalog database not started

Cause: IMPORT CATALOG command was issued which requires the source recovery catalog to be open.

Action: Open the source recovery catalog database and re-submit the command.

RMAN-06777: ORACLE error from source recovery catalog database: string

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-06778: WARNING: string: sqlcode number was caught, automatic retry #string

Cause: The RMAN client caught a transient error during temporary resource allocate for IMPORT CATALOG command and will automatically retry several times.

Action: No action required, this is an informational message.

RMAN-06779: import validation complete

Cause: This is an informational message only.

Action: No action required.

RMAN-06780: database unregistered from the source recovery catalog

Cause: This is an informational message only.

Action: No action is required.

RMAN-06781: string package version string in source database is not of version string

Cause: The catalog schema version of the source recovery catalog is not the same as the target recovery catalog. The two catalog

Action: UPGRADE source recovery catalog schema and recovery catalog schema to same version and retry the command.

RMAN-06782: Datafile headers of locally managed datafiles need to be updated.

Cause: This is an informational message only.

Action: No action is required.

RMAN-06783: Update of datafile headers of locally managed datafiles finished.

Cause: This is an informational message only.

Action: No action is required.

RMAN-06784: One or more datafile headers of locally managed datafiles were not updated.

Cause: Errors prevented the update of one or more datafile headers.

Action: See trace file for details of the problem.

RMAN-06785: This operation might take some time.

Cause: This is an informational message only.

Action: No action is required.

RMAN-06786: could not read file header for datafile string to do FLASHBACK.

Cause: The indicated datafile header could not be read to do FLASHBACK DATABASE.

Action: If the database must be taken back in time then a restore and incomplete recovery must be performed.

RMAN-06787: WARNING: TAG string option is ignored; backups will be tagged with string

Cause: WITH TAG option and TAG option were used together. When WITH TAG option is used, all the backups created by the command will have tag specified with WITH TAG option.

Action: The TAG option can be removed to not display the message.

RMAN-06791: changed the DB\_UNIQUE\_NAME value from string to string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06792: database db\_unique\_name is "string", db\_name is "string" and DBID is string

Cause: UNREGISTER DB\_UNIQUE\_NAME or CHANGE DB\_UNIQUE\_NAME command was executed, hence RMAN displayed the database information for which DB\_UNIQUE\_NAME the metadata will be removed/renamed in the recovery catalog.

Action: No action required, this is an informational message only.

RMAN-06793: database with db\_unique\_name string unregistered from the recovery catalog

Cause: UNREGISTER DB\_UNIQUE\_NAME command was executed.

Action: No action required, this is an informational message only.

RMAN-06795: Flashback database logging is not on.

Cause: A FLASHBACK DATABASE command was tried but flashback database logging has not been enabled.

Action: Flashback database logging must be enabled via the ALTER DATABASE FLASHBACK ON command before a FLASHBACK DATABASE command can be tried. If the database must be taken back in time then a restore and incomplete recovery must be performed.

RMAN-06796: Not enough flashback database log data to do FLASHBACK.

Cause: There was not enough flashback database log data to do the FLASHBACK DATABASE.

Action: If the database must be taken back in time then a restore and incomplete recovery must be performed.

RMAN-06797: Grant succeeded.

Cause: This is an informational message issued in response to a GRANT command.

Action: No action required.

RMAN-06798: Revoke succeeded.

Cause: This is an informational message issued in response to a REVOKE command.

Action: No action required.

RMAN-06799: found eligible base catalog owned by string

Cause: When creating a virtual private catalog, an 11g base catalog was found, owned by the specified user, and the currently connected catalog user has been granted privileges on this catalog, and can therefore create a virtual private catalog using this base catalog. This is an informational message issued in response to a CREATE VIRTUAL CATALOG command.

Action: No action required.

RMAN-06800: found ineligible base catalog owned by string

Cause: When creating a virtual private catalog, an 11g base catalog was found, owned by the specified user, and the currently connected catalog user has not been granted any privileges on this catalog. This is an informational message issued in response to a CREATE VIRTUAL CATALOG command.

Action: No action required.

RMAN-06801: no base catalog found

Cause: When trying to create a virtual catalog, either no base catalog was found, or this user has no privilege to create a virtual catalog against any existing base catalog.

Action: Establish the correct privileges and re-create the virtual catalog.

RMAN-06802: too many eligible base catalogs found

Cause: When trying to create a virtual catalog, more than one base catalog was found that is eligible to be the base catalog for this virtual catalog.

Action: Revoke privileges so that the current catalog user has privileges on only one base catalog, then re-issue the CREATE VIRTUAL CATALOG command.

RMAN-06803: created virtual catalog against base catalog owned by string

Cause: A virtual private catalog was created, where the base catalog data is owned by the specified user. This is an informational message issued in response to a CREATE VIRTUAL CATALOG command.

Action: No action required.

RMAN-06804: Enter value for string:

Cause: This is a user prompt.

Action: Enter a substitution value to proceed.

RMAN-06805: SET NEWNAME command has not been issued for tempfile string

Cause: A SWITCH command was specified for a tempfile, but no destination was specified and no SET NEWNAME command has been previously issued for that file. An explicit file to switch to must be specified if no SET NEWNAME command has been issued.

Action: Correct and resubmit the SWITCH command.

RMAN-06806: compression algorithm 'string' of release string not found

Cause: An unsupported compression algorithm was specified for the backup.

Action: Query the V$RMAN\_COMPRESSION\_ALGORITHM view for the list of suppmrted compression algorithms. Specify a valid compression algorithm and retry the command.

RMAN-06807: compression algorithm 'string' of release string cannot be used because database compatibility is less than string

Cause: The compression algorithm is not supported because the current compatibility level of the database is too low.

Action: Query the V$RMAN\_COMPRESSION\_ALGORITHM view for the list of supported compression algorithms. Specify a valid compression algorithm and retry the command.

RMAN-06808: SECTION SIZE cannot be used when piece limit is in effect

Cause: The SECTION SIZE backup option was used together with the MAXPIECESIZE channel limit. These options are mutually exclusive, because they are independant methods of creating multiple backup pieces with one backup command.

Action: Use one option or the other, but not both.

RMAN-06809: compression algorithm 'string' of release string requires advanced compression option

Cause: The compression algorithm was not supported because it requires advanced compression option to be enabled.

Action: Enable advanced compression option by setting advanced\_compression\_option\_usable=true or specify a different compression algorithm.

RMAN-06810: specification does not match any datafile copy in the repository

Cause: No datafile copies were found that match specification in the recovery catalog or target database control file.

Action: Check the specifier.

RMAN-06811: specification does not match any control file copy in the repository

Cause: No control file copies were found that match specification in the recovery catalog or target database control file.

Action: Check the specifier.

RMAN-06812: specification does not match any backup in the repository

Cause: No backups were found that match specification in the recovery catalog or target database control file.

Action: Check the specifier.

RMAN-06818: WARNING: last archived log from primary database not recieved at standby database

Cause: An archived log was switched at the primary database during backup at the standby database and this log was not shipped to the standby database. The backup created at the standby database will need more logs to recover.

Action: Check whether the standby databse is configured correctly to recieve logs from the primary database.

RMAN-06819: current log archived at primary database

Cause: The ALTER SYSTEM ARCHIVE LOG CURRENT command completed successfully at the primary database because the connected target instance was a physical standby database. The switched archived logs were included in the backup so that the backed files could be recovered to a consistent point-in-time.

Action: None. This is an informational message.

RMAN-06820: WARNING: failed to archive current log at primary database

Cause: An attempt to switch the archived log at the primary database failed.

Action: Resolve the error messages associated with this message to avoid the warning.

RMAN-06898: recovery catalog is partially upgraded to string

Cause: The recovery catalog database was not completely upgraded to the specified version. Either there were some errors during execution of UPGRADE CATALOG or UPGRADE CATALOG was cancelled before completion.

Action: Execute UPGRADE CATALOG again.

RMAN-06899: updating recovery catalog with new database incarnation

Cause: The target database has a new incarnation that has not already been seen by the recovery catalog. This usually happens because a Point-in-Time Recovery was done. RMAN has made the necessary updates to the recovery catalog.

Action: This is an informational message only.

RMAN-06900: WARNING: unable to generate V$RMAN\_STATUS or V$RMAN\_OUTPUT row

Cause: The routine createRmanStatusRow() or createRmanOutputRow() could add new row into V$RMAN\_STATUS or V$RMAN\_OUTPUT.

Action: Check the associated error messages. If the associated error message indicates a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-06901: WARNING: disabling update of the V$RMAN\_STATUS and V$RMAN\_OUTPUT rows

Cause: Informational message only.

Action: No action required.

RMAN-06902: AS COMPRESSED BACKUPSET option cannot be used when backing up backup sets

Cause: The backup set was specified with AS COMPRESSED BACKUPSET.

Action: Remove the AS COMPRESSED BACKUPSET option.

RMAN-06903: backup of datafile string was cancelled

Cause: This is an informational message displayed when PARTIAL option of DURATION option was specified on the BACKUP command and backup could not be completed within the given duration time.

Action: Run the BACKUP command to backup cancelled files, or let the next backup window backup the cancelled files. It should be noted that the files that were skipped in the current job will be given preference to other files for next the BACKUP command with DURATION option.

RMAN-06904: backup of archived log for thread number with sequence number and starting SCN of string was cancelled

Cause: This is an informational message displayed when PARTIAL option of DURATION option was specified on the BACKUP command and backup could not be completed within the given duration time.

Action: Run BACKUP command to backup cancelled files, or let the next backup window backup the cancelled files. It should be noted that the files that were skipped in the current job will be given preference to other files for next the BACKUP command with DURATION option.

RMAN-06905: backup of backup set key number was cancelled

Cause: This is an informational message displayed when PARTIAL option of DURATION option was specified on the BACKUP command and backup could not be completed within the given duration time.

Action: Run BACKUP command to backup cancelled files, or let the next backup window backup the cancelled files. It should be noted that the files that were skipped in the current job will be given preference to other files for next the BACKUP command with DURATION option.

RMAN-06906: backup of control file was cancelled

Cause: This is an informational message displayed when PARTIAL option of DURATION option was specified on the BACKUP command and backup could not be completed within the given duration time.

Action: Run BACKUP command to backup cancelled files, or let the next backup window backup the cancelled files. It should be noted that the files that were skipped in the current job will be given preference to other files for next the BACKUP command with DURATION option.

RMAN-06907: MINIMIZE LOAD option not allowed for the specified input files

Cause: This option was specified in a backup command specification for BACKUP BACKUPSET or BACKUP CURRENT CONTROLFILE command.

Action: Remove the MINIMIZE LOAD option and retry the command.

RMAN-06908: WARNING: operation will not run in parallel on the allocated channels

Cause: RMAN allocated more than one channel for a job, but the job will not run in parallel on these channels because parallelism require Enterprise Edition.

Action: None

RMAN-06909: WARNING: parallelism require Enterprise Edition

Cause: RMAN allocated more than one channel for a job, but the job will not run in parallel on these channels because parallelism require Enterprise Edition.

Action: None

RMAN-06910: can not invoke parallel recovery for test recovery

Cause: Recover database was called with TEST and PARALLEL option

Action: Call recover database with either just the TEST or PARALLEL option

RMAN-06911: only one PARALLEL or NOPARALLEL clause may be specified

Cause: Recover database was called with PARALLEL and NOPARALLEL option

Action: Call recover database with either just the PARALLEL or NOPARALLEL option.

RMAN-06912: backup of spfile was cancelled

Cause: This is an informational message displayed when PARTIAL option of DURATION option was specified on the BACKUP command and backup could not be completed within the given duration time.

Action: Run BACKUP command to backup cancelled files, or let the next backup window backup the cancelled files. It should be noted that the files that were skipped in the current job will be given preference to other files for next the BACKUP command with DURATION option.

RMAN-06913: validate cancelled because there are no files to validate

Cause: All files for this validate command were skipped, therefore no files to validate.

Action: This message is informational only.

RMAN-06914: BLOCK string must be greater or equal to BLOCK string

Cause: The value of TO block number was less than the value of from block number.

Action: Increase the value of TO BLOCK past the value of from BLOCK and retry the command.

RMAN-06915: restore point string already exists

Cause: The specified restore point already exists on this database.

Action: Use LIST RESTORE POINT to see existing names and retry the command with a unique restore point name.

RMAN-06918: WARNING: allocated SBT channel to Oracle Availability Machine in NOCATALOG mode

Cause: Oracle Availability Machine might have run out of resources because congestion control could not be enabled in NOCATALOG mode.

Action: Use the CATALOG mode to connect RMAN to an Oracle Availability Machine instance.

RMAN-06920: database string is not open read-only

Cause: CONVERT DATABASE attempted on a database that was not open read-only.

Action: Open the database in read-only mode and retry the operation.

RMAN-06921: Convert database check failed

Cause: This database could not be transported because DBMS\_TDB.CHECK\_DB returned FALSE.

Action: None

RMAN-06922: External table string.string found in the database

Cause: An external table was found in the database.

Action: Redefine the table in the transported database.

RMAN-06923: Directory string.string found in the database

Cause: A directory object was found in the database.

Action: Redefine the directory in the transported database.

RMAN-06924: BFILE string.string found in the database

Cause: A BFILE was found in the database.

Action: Redefine the BFILE in the transported database.

RMAN-06925: BFILEs are used in the system, please redefine them in the transported database

Cause: BFILEs may or may not exist in the database. Automatically performed BFILE check failed because database was open read-only and could not allocate temporary space. This does not affect CONVERT DATABASE operation.

Action: Use DBMS\_TDB.CHECK\_EXTERNAL to perform BFILE check when the database is open in read/write mode.

RMAN-06926: User string with string privilege found in password file

Cause: Password file was used.

Action: Re-create the password file on the target platform using ORAPWD for the transported database.

RMAN-06927: Cannot specify NEW DATABASE clause more than once

Cause: NEW DATABASE clause specified more than once

Action: Remove redundant NEW DATABASE clause and retry the operation.

RMAN-06928: Cannot specify ON TARGET PLATFORM clause more than once

Cause: ON TARGET PLATFORM clause specified more than once

Action: Remove redundant ON TARGET PLATFORM clause and retry the operation.

RMAN-06929: Cannot specify TRANSPORT SCRIPT clause more than once

Cause: TRANSPORT SCRIPT clause specified more than once

Action: Remove redundant ON TARGET PLATFORM clause and retry the operation.

RMAN-06930: Cannot specify SKIP clause more than once

Cause: SKIP clause specified more than once

Action: Remove redundant SKIP clause and retry the operation.

RMAN-06931: Cannot specify FROM PLATFORM clause

Cause: CONVERT DATABASE command cannot use FROM PLATFORM clause.

Action: Change FROM PLATFORM clause and retry.

RMAN-06932: Database name 'string' longer than number

Cause: The specified database name exceeded the maximum allowable database name length.

Action: Correct the database name.

RMAN-06933: Transport script name too long

Cause: The specified transport script name exceeded the maximum allowable script name length.

Action: Correct the script name.

RMAN-06934: Format string too long

Cause: The specified format string exceeded the maximum allowable format string length.

Action: Correct the format string.

RMAN-06935: Convert script name too long

Cause: The specified convert script name exceeded the maximum allowable script name length.

Action: Correct the script name.

RMAN-06941: Database must be closed and mounted EXCLUSIVE and RESTRICTED.

Cause: DROP DATABASE was attempted while the database was open or not mounted EXCLUSIVE and RESTRICTED.

Action: Change the database state to mounted EXCLUSIVE and RESTRICTED.

RMAN-06942: OPTION number is invalid; OPTION must be between string and string

Cause: An invalid OPTION was used.

Action: Change the OPTION argument.

RMAN-06943: no automatic repair OPTION number was listed in ADVISE FAILURE

Cause: The OPTION specified was not one of the automatic repair options listed by ADVISE FAILURE or there were no options listed by the ADVISE FAILURE command.

Action: Change the OPTION argument or resubmit ADVISE FAILURE with a different set of failures.

RMAN-06944: contents of repair script:

Cause: This is an informational message only.

Action: No action is required.

RMAN-06945: no repair script present for REPAIRID string

Cause: REPAIRID option specified in the command was invalid or the repair script had been purged from Automated Diagnostic Repository.

Action: Retry REPAIR FAILURE command with a different OPTION number.

RMAN-06946: executing repair script

Cause: This is an informational message only.

Action: No action is required.

RMAN-06947: searching flashback logs for block images until SCN string

Cause: Starting the flashback log search for RECOVER...BLOCK command. The log is searched until the indicated system change number (SCN).

Action: None. This is an informational message displayed for RECOVER...BLOCK command.

RMAN-06948: searching flashback logs for block images

Cause: Starting the flashback log search for RECOVER...BLOCK command. The log is searched until the end of the log.

Action: None. This is an informational message displayed for RECOVER...BLOCK command.

RMAN-06949: finished flashback log search, restored string blocks

Cause: Flashback log search finished for RECOVER...BLOCK command.

Action: None. This is an informational message displayed for RECOVER...BLOCK command.

RMAN-06950: invalid validate option specified: string

Cause: The specified object was invalid with VALIDATE command.

Action: Delete the invalid operand.

RMAN-06951: repair failure complete

Cause: This is an informational message only.

Action: No action is required.

RMAN-06952: database needs to be restarted

Cause: The target database control file was missing.

Action: Restart the instance and repair the database.

RMAN-06953: no automatic repairs were listed by ADVISE FAILURE

Cause: There were no automatic repairs listed by the ADVISE FAILURE command.

Action: Choose a different failure, submit ADVISE FAILURE command, and then submit REPAIR FAILURE command.

RMAN-06954: REPAIR command must be preceded by ADVISE command in same session

Cause: The ADVISE command was not issued in the same session as the REPAIR command.

Action: Submit ADVISE command and then submit the REPAIR command in same session.

RMAN-06955: Network copies are only supported for image copies.

Cause: An attempt was made to specify BACKUP AUXILIARY FORMAT without specifying the AS COPY clause. A network copy is only supported with an image copy.

Action: Seek an alternate method of copying the desired files.

RMAN-06956: create datafile failed; retry after removing string from OS

Cause: An attempt was made to re-create a database file. This attempt failed.

Action: If the indicated file already exists, remove the file from operating system and retry the RMAN command.

RMAN-06957: finished standby search, restored string blocks

Cause: Standby search finished for RECOVER...BLOCK command.

Action: None. This is an informational message displayed for RECOVER...BLOCK command.

RMAN-06958: Executing: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06959: WARNING: repair completed but could not verify that failures were fixed by it

Cause: RMAN repair command successfully completed but could not check if the failures were fixed.

Action: Use LIST FAILURE command to verify repair results.

RMAN-06960: EXPDP> string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06961: IMPDP> string

Cause: This is an informational message only.

Action: No action is required.

RMAN-06962: Error received during export of metadata

Cause: Data Pump could not perform export of tablespace metadata.

Action: See accompanying datapump messages indicating the cause of the error.

RMAN-06963: Error received during import of metadata

Cause: Data Pump could not perform import of tablespace metadata.

Action: See accompanying datapump messages indicating the cause of the error.

RMAN-06964: option string cannot be used with string

Cause: Incompatible options were specified that caused the command to fail.

Action: Remove one of the options from the command and retry.

RMAN-06965: Datapump job has stopped

Cause: A Data Pump error has caused the job to stop.

Action: See accompanying datapump messages or look for a Data Pump trace file for the cause of the error.

RMAN-06966: Invalid release number string

Cause: An incorrectly formatted release number was specified.

Action: Specify a valid release number in n.n.n.n.n format.

RMAN-06967: finished primary search, recovered string blocks

Cause: Primary Database search finished for RECOVER...BLOCK command.

Action: None. This is an informational message displayed for RECOVER...BLOCK command.

RMAN-06970: NEWNAME 'string' for database must include %f or %U format

Cause: The newname in SET NEWNAME FOR DATABASE did not include a format specifier to produce different newnames for the datafiles.

Action: Include %f or %U in the newname or use SET NEWNAME FOR DATABASE TO NEW to ensure datafiles get different datafile names.

RMAN-06971: NEWNAME 'string' for tablespace must include %f or %U format

Cause: The newname in SET NEWNAME FOR TABLESPACE did not include a format specifier to produce different newnames for the datafiles.

Action: Include %f or %U in the newname or use SET NEWNAME FOR TABLESPACE... TO NEW to ensure datafiles get different datafile names.

RMAN-06980: The following errors need to be fixed before peforming this command

Cause: The tablespaces failed validation by DBMS\_TTS.TRANSPORT\_SET\_CHECK.

Action: Fix accompanying violations before attempting the command again.

RMAN-06981: Violation: string

Cause: This message was issued to show a violation obtained from the DBMS\_TTS.TRANSPORT\_SET\_CHECK.

Action: Fix violation before attempting the command again.

RMAN-07000: List of SPFILE Backups

Cause: This message is issued in response to a LIST BACKUP OF SPFILE command.

Action: No action is required.

RMAN-07025: string is not supported for foreign archived log

Cause: The specified option was not supported for foreign archived log.

Action: Do not use the specified command for foreign archived log.

RMAN-07200: no failures found that match specification

Cause: A failure specifier did not match any failures in the Automated Diagnostic Repository.

Action: Resubmit the command with a different failure specifier. You can use the LIST FAILURE ALL command in Recovery Manager to display all failures known to RMAN.

RMAN-07207: changed string failures to HIGH priority

Cause: This is an informational message only.

Action: No action is required.

RMAN-07208: changed string failures to LOW priority

Cause: This is an informational message only.

Action: No action is required.

RMAN-07209: closed string failures

Cause: This is an informational message only.

Action: No action is required.

RMAN-07210: new failures after most recent LIST FAILURE command

Cause: New failures were found since last LIST FAILURE command in this RMAN session.

Action: No action is required. This is an informational message only.

RMAN-07211: failure option not specified

Cause: ALL, CRITICAL, HIGH, LOW, or list of failure numbers was not specified.

Action: Specify a failure option and resubmit the command.

RMAN-07212: skipping failure string because it was CLOSED

Cause: The specified failure has been already closed, so ADVISE FAILURE or CHANGE FAILURE cannot be executed on this failure.

Action: This is an informational message only. No action is required.

RMAN-07213: Mandatory Manual Actions

Cause: This is an informational message only.

Action: No action is required.

RMAN-07215: Automated Repair Options

Cause: This is an informational message only.

Action: No action is required.

RMAN-07220: no manual actions available

Cause: This is an informational message only.

Action: No action is required.

RMAN-07222: =======================

Cause: This is an informational message only.

Action: No action is required.

RMAN-07251: Repair script: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-07252: ========================

Cause: This is an informational message only.

Action: No action is required.

RMAN-07253: ========================

Cause: This is an informational message only.

Action: No action is required.

RMAN-07255: priority change for failure string failed

Cause: An attempt was made to change the priority of a child failure.

Action: Specify the parent failure ID to change the child failure.

RMAN-07256: cannot change priority of child failure

Cause: An attempt was made to change the priority of child failure.

Action: This message should be followed by one or more 7255 messages.

RMAN-07259: string critical failures exist; cannot exclude from ADVISE FAILURE

Cause: ADVISE FAILURE was executed for HIGH or LOW priority failures when CRITICAL failures existed.

Action: Execute ADVISE FAILURE with the CRITICAL or ALL options.

RMAN-07262: no automatic repair options available

Cause: This is an informational message only.

Action: No action is required.

RMAN-07500: searching for all files that match the pattern string

Cause: This is an informational message only.

Action: No action is required.

RMAN-07501: searching for all files in the recovery area

Cause: This is an informational message only.

Action: No action is required.

RMAN-07502: List of Files Unknown to the Database

Cause: This message is issued in response to a CATALOG command.

Action: No action is required.

RMAN-07505: no files found to be unknown to the database

Cause: This is an informational message displayed by the CATALOG command. The command either found no files, or all files that matched the specified search pattern were already present in the target database control file.

Action: No action is required.

RMAN-07507: cataloging files...

Cause: This is an informational message only.

Action: No action is required.

RMAN-07508: cataloging done

Cause: This is an informational message only.

Action: No action is required.

RMAN-07509: List of Cataloged Files

Cause: This message is issued in response to a CATALOG command.

Action: No action is required.

RMAN-07513: List of Files Which Where Not Cataloged

Cause: This message is issued in response to a CATALOG command.

Action: No action is required.

RMAN-07514: =======================================

Cause: This is an informational message only.

Action: No action is required.

RMAN-07515: File Name: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-07516: Reason: Error reading

Cause: This is an informational message only.

Action: No action is required.

RMAN-07517: Reason: The file header is corrupted

Cause: Either the file is not an Oracle file or the file header is corrupted.

Action: Delete the file using OS utility.

RMAN-07518: Reason: Foreign database file DBID: string Database Name: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-07519: Reason: Error while cataloging. See alert.log.

Cause: This is an informational message only.

Action: No action is required.

RMAN-07520: Reason: Data pump dump file

Cause: This is an informational message only.

Action: No action is required.

RMAN-07521: cannot create recovery catalog in database version string; version string required

Cause: An attempt was made to use a version of the recovery catalog schema that was incompatible with the version of the database.

Action: Upgrade the catalog database to at least the required version or install the catalog schema in a different database which is of at least the required version.

RMAN-07522: CREATE TYPE privilege must be granted to user string

Cause: The CREATE CATALOG or UPGRADE CATALOG command was used, but the USERID that was supplied in the CATALOG connect string does not have the CREATE TYPE privilege granted.

Action: Grant CREATE TYPE privilege to the recovery catalog owner.

RMAN-07523: List of files in Recovery Area not managed by the database

Cause: This message was issued in response to a CATALOG RECOVERY AREA command.

Action: No action is required.

RMAN-07524: ==========================================================

Cause: This is an informational message only.

Action: No action is required.

RMAN-07525: Reason: File is not a supported file type in Recovery Area

Cause: This message should be accompanied by other message(s) indicating the name of file that was not supported in recovery area. Any file other than current control file, online log, archived log, RMAN backups and flashback log is not supported in recovery area. This is an informational message only.

Action: No action is required.

RMAN-07526: Reason: File is not an Oracle Managed File

Cause: This message should be accompanied by other message(s) indicating the name of file that was not a oracle managed file. This is an informational message only.

Action: No action is required.

RMAN-07527: Reason: File was not created using DB\_RECOVERY\_FILE\_DEST initialization parameter

Cause: This message should be accompanied by other message(s) indicating the name of file that was not created using DB\_RECOVERY\_FILE\_DEST initialization parameter. One of the following scenarios caused this error: 1) This is an archived log file and was created when the LOG\_ARCHIVE\_DEST\_n initialization parameter was set explicitly to recovery area location. For example, LOG\_ARCHIVE\_DEST\_1='location=+FRA' where '+FRA' was also your DB\_RECOVERY\_FILE\_DEST value. 2) This is an RMAN backup file and was created in a recovery area using the FORMAT option of the BACKUP command. 3) This is an online log file or current control file and was created prior to setting the recovery area. 4) This file fits none of the above scenarios and is not supported by the recovery area.

Action: All of following actions will resolve future occurrences of this error: 1) To create archived logs in recovery area, set the LOG\_ARCHIVE\_DEST\_n initialization parameter to 'location=USE\_DB\_RECOVERY\_FILE\_DEST'. Do not explicitly set the LOG\_ARCHIVE\_DEST\_n initialization parameter to a recovery area location. 2) To create RMAN backups in recovery area, do not use the FORMAT option of the BACKUP command. All of following actions will resolve current problem: 1) If this is an archived log file or an RMAN backup file, use the CATALOG command to re-catalog the files. 2) If this is an online log file or a current control file to be managed by the recovery area, re-create the file using the DB\_RECOVERY\_FILE\_DEST initialization parameter.

RMAN-07528: number of files not managed by recovery area is string, totaling string

Cause: This message should be accompanied by other message(s) indicating the list of files. Either the files listed are not known to the database or not managed by recovery area. The number and size of the files are shown. This is an informational message only.

Action: No action is required.

RMAN-07529: Reason: catalog is not supported for this file type

Cause: The CATALOG command encountered one or more files of types that cannot be cataloged. These file types include online redo logs, flashback logs, block change tracking files, and data pump files. This message will be accompanied by other messages indicating the names of the file's that could not be cataloged.

Action: No action is required.

RMAN-07530: Reason: This file type is not requested for cataloging

Cause: This is an informational message only.

Action: No action is required.

RMAN-08000: channel string: copied datafile string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08001: restore not complete

Cause: All of the backup pieces have been successfully applied, but DBMS\_BACKUP\_RESTORE package indicates that the restore conversation is not complete. This usually means that the backup set contained corrupt data.

Action: Restore the files from a different backup set, if possible. The Recovery Manager CHANGE BACKUPPIECE UNAVAILABLE can be used to prevent Recovery Manager from attempting to restore from the corrupt backup piece(s).

RMAN-08002: starting full resync of recovery catalog

Cause: This is an informational message only.

Action: No action is required.

RMAN-08003: channel string: reading from backup piece string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08004: full resync complete

Cause: This is an informational message only.

Action: No action is required.

RMAN-08005: new incarnation of database registered in recovery catalog

Cause: This is an informational message only.

Action: No action is required.

RMAN-08006: database registered in recovery catalog

Cause: This is an informational message only.

Action: No action is required.

RMAN-08007: channel string: copied datafile copy of datafile string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08008: channel string: starting full datafile backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08009: channel string: starting archived log backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08010: channel string: specifying datafile(s) in backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08011: including current control file in backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08012: including control file copy in backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08013: channel string: backup piece string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08014: channel string: specifying archived log(s) in backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08015: datafile string switched to datafile copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08016: channel string: starting datafile backup set restore

Cause: This is an informational message only.

Action: No action is required.

RMAN-08017: channel string: starting archived log restore to default destination

Cause: This is an informational message only.

Action: No action is required.

RMAN-08018: channel string: starting archived log restore to user-specified destination

Cause: This is an informational message only.

Action: No action is required.

RMAN-08019: channel string: restoring datafile string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08020: including standby control file in backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08021: channel string: restoring control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08022: channel string: restoring archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-08023: channel string: restored backup piece string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08025: channel string: copied control file copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08026: channel string: copied archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-08027: channel string: copied current control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08028: channel string: copy current control file failed

Cause: This is an informational message only.

Action: No action is required.

RMAN-08029: snapshot control file name set to default value: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08030: allocated channel: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08031: released channel: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08032: channel string: RECID string STAMP string does not match recovery catalog

Cause: The record that identifies the source file for a copy or backup database does not contain the same data as is stored in the recovery catalog.

Action: Perform a full resync and retry the operation. If the problem persists, then contact Oracle.

RMAN-08033: channel string: including datafile copy of datafile string in backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08034: full resync skipped, target database not mounted

Cause: This is an informational message only.

Action: No action is required.

RMAN-08035: partial resync skipped, target database not mounted

Cause: This is an informational message only.

Action: No action is required.

RMAN-08036: channel string: could not create control file record for string string

Cause: The record identifying the named file was no longer present in the target database control file, and repeated attempts to inspect the file were unsuccessful in creating the record. This could be because the circular-reuse section of the control file which holds information about the specified type of file is too small and there is other database activity which is causing the record to be overwritten before it can be used.

Action: Try increasing either the size of the control file circular-reuse section for this file type (datafile copy or archived log, as indicated in the error message, or the CONTROL\_FILE\_RECORD\_KEEP\_TIME initialization parameter. If neither of those remedies works then contact Oracle.

RMAN-08037: channel string: unexpected validation return code string

Cause: This is an internal error that should never be issued.

Action: Contact Oracle Support.

RMAN-08038: channel string: starting piece string at string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08039: channel string: starting incremental datafile backup set restore

Cause: This is an informational message only.

Action: No action is required.

RMAN-08040: full resync skipped, control file is not current or backup

Cause: This is an informational message only.

Action: No action is required.

RMAN-08041: partial resync skipped, control file is not current or backup

Cause: This is an informational message only.

Action: No action is required.

RMAN-08042: channel string: copied standby control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08043: channel string: copy standby control file failed

Cause: This is an informational message only.

Action: No action is required.

RMAN-08044: channel string: finished piece string at string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08045: channel string: finished piece string at string with string copies

Cause: This is an informational message only.

Action: No action is required.

RMAN-08046: channel string: starting compressed full datafile backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08047: channel string: starting compressed incremental level string datafile backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08048: channel string: starting incremental level string datafile backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08049: channel string: starting compressed archived log backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08050: cataloged datafile copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08051: cataloged archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-08052: cataloged control file copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08053: channel string: finished piece string at string with string copies and tag string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08054: starting media recovery

Cause: This is an informational message only.

Action: No action is required.

RMAN-08056: skipping datafile string because it has not changed

Cause: The specified datafile has not had its checkpoint advanced since the previous backup, therefore it does not need a new incremental backup.

Action: This is an informational message only.

RMAN-08057: channel string: backup cancelled because all files were skipped

Cause: All datafiles for this backup were skipped, therefore no backup is created.

Action: This is an informational message only.

RMAN-08058: replicating control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08059: media recovery failed

Cause: This is an informational message only.

Action: No action is required.

RMAN-08060: unable to find archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-08061: WARNING: change failure ID string failed due to error ORA-string

Cause: CHANGE FAILURE for the indicated failure ID encountered an error.

Action: See the indicated ORA error message for the cause of the error.

RMAN-08062: WARNING: cannot change priority of a critical failure string

Cause: An attempt was made to change priority of a failure with CRITICAL priority.

Action: No action is required.

RMAN-08063: Recovery catalog is down or not connected to catalog, trying to reconnect.

Cause: This is an informational message only.

Action: No action is required.

RMAN-08064: Reconnection with the recovery catalog is successful.

Cause: This is an informational message only.

Action: No action is required.

RMAN-08065: WARNING: Reconnection with the recovery catalog failed, switching to nocatalog mode.

Cause: RMAN failed to reconnect to the recovery catalog and switched to nocatalog mode.

Action: No action is required.

RMAN-08066: database reset to incarnation string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08070: deleted datafile copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08071: channel string: deleting archived log(s)

Cause: This is an informational message only.

Action: No action is required.

RMAN-08072: deleted control file copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08073: deleted backup piece

Cause: This is an informational message only.

Action: No action is required.

RMAN-08074: crosschecked backup piece: found to be 'string'

Cause: This is an informational message only.

Action: No action is required.

RMAN-08085: created script string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08086: replaced script string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08087: channel string: started backup set validation

Cause: This is an informational message only.

Action: No action is required.

RMAN-08088: applied offline range to datafile string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08089: channel string: specifying datafile(s) to restore from backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08090: channel string: starting proxy restore

Cause: This is an informational message only.

Action: No action is required.

RMAN-08091: channel string: specifying datafile(s) for proxy backup

Cause: This is an informational message only.

Action: No action is required.

RMAN-08092: channel string: specifying datafile copy of datafile string for proxy backup

Cause: This is an informational message only.

Action: No action is required.

RMAN-08093: specifying current control file for proxy backup

Cause: This is an informational message only.

Action: No action is required.

RMAN-08094: channel string: specifying datafile(s) for proxy restore

Cause: This is an informational message only.

Action: No action is required.

RMAN-08096: channel string: starting validation of datafile backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08097: channel string: starting validation of archived log backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08099: specifying standby control file for proxy backup

Cause: This is an informational message only.

Action: No action is required.

RMAN-08100: channel string: starting proxy validation

Cause: This is an informational message only.

Action: No action is required.

RMAN-08101: channel string: proxy validation complete

Cause: This is an informational message only.

Action: No action is required.

RMAN-08102: channel string: located backup piece: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08103: channel string: could not locate backup piece: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08104: channel string: input backup set: count=string, stamp=string, piece=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08105: channel string: backup cancelled because no pieces were found

Cause: All backup sets specified has no pieces. Therefore, no backup set is created.

Action: This is an informational message only.

RMAN-08106: channel string: restoring block(s)

Cause: This is an informational message only.

Action: No action is required.

RMAN-08107: skipping inaccessible backup set count=string STAMP=string

Cause: The indicated backup set will not be backed up because one or more pieces of the backup set could not be read, and the SKIP INACCESSIBLE option was specified.

Action: No action is required.

RMAN-08108: channel string: specifying block(s) to restore from backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08109: channel string: restored block(s) from backup piece string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08110: failover to next copy of backup piece

Cause: This is an informational message only.

Action: No action is required.

RMAN-08111: some blocks not recovered: See trace file for details

Cause: Some blocks not recovered due to errors.

Action: See trace file for details of the problem.

RMAN-08112: archived log failover was done on string, check alert log for more info

Cause: This is an informational message to indicate the server found a corrupted block in an archived log and had to switch to another copy of the same archived log in an alternate archived log destination to get corresponding un-corrupted block.

Action: If backup is done with delete input option, nothing needs to be done. Otherwise delete the archived log that has corrupted block(s) as recovery on applying this log would fail. Alert log contains name of the log that has corrupted block(s).

RMAN-08113: including current SPFILE in backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08114: channel string: restoring SPFILE to PFILE

Cause: This is an informational message only.

Action: No action is required.

RMAN-08115: channel string: restoring SPFILE

Cause: This is an informational message only.

Action: No action is required.

RMAN-08116: output file name is original SPFILE location

Cause: This is an informational message only.

Action: No action is required.

RMAN-08117: channel string: the AUTOBACKUP does not contain an SPFILE

Cause: The requested AUTOBACKUP does not contain a SPFILE. This is because the instance was not started with a SPFILE when the AUTOBACKUP was created.

Action: No action is required. RMAN will try three older AUTOBACKUPS before signaling ORA-19687.

RMAN-08118: WARNING: could not delete the following archived redo log

Cause: The routine deleteArchivedLog() could not delete an archived redo log on the target instance.

Action: Check the accompanying file specification and the associated error messages. The file specification indicates what archived redo log on the target instance RMAN was trying to delete and the error messages indicate why RMAN was unable to delete it. Resolve the problem by first confirming that the archived redo log in question has been backed up, do the deletion manually, and then do a crosscheck so that RMAN is aware of the deletion.

RMAN-08119: skipping backup piece handle string; already exists

Cause: A BACKUP command does not need to backup control file AUTOBACKUP pieces, because they already exists.

Action: This is an informational message, no action is required.

RMAN-08120: WARNING: archived log not deleted, not yet applied by standby

Cause: This is an informational message to alert the user that an archived log that should have been deleted was not as it has not been applied to the standby database. The next message identifies the archived log

Action: Archivelog can be deleted after it has been applied to standby database.

RMAN-08121: keep attributes for the backup are deleted

Cause: This is an informational message only.

Action: No action is required.

RMAN-08122: keep attributes for the backup are changed

Cause: This is an informational message only.

Action: No action is required.

RMAN-08123: keep attributes for the datafile/control file copy are deleted

Cause: This is an informational message only.

Action: No action is required.

RMAN-08124: keep attributes for the datafile/control file copy are changed

Cause: This is an informational message only.

Action: No action is required.

RMAN-08125: keep attributes for the proxy copy are deleted

Cause: This is an informational message only.

Action: No action is required.

RMAN-08126: keep attributes for the proxy copy are changed

Cause: This is an informational message only.

Action: No action is required.

RMAN-08127: cataloged backup piece

Cause: This is an informational message only.

Action: No action is required.

RMAN-08128: uncataloged backup piece

Cause: This is an informational message only.

Action: No action is required.

RMAN-08129: failover to piece handle=string tag=string

Cause: This is an informational message to indicate the server found a corrupted block in a piece and had to switch to another copy of piece to get corresponding un-corrupted block.

Action: See alert log for information on corruption block(s) and the name of the piece that has the corrupted block(s).

RMAN-08130: failover to copy on device type string

Cause: This is an informational message to indicate the RMAN could not successfully restore the database using the specified backups. An attempt was made to restore the datafiles/archived logs/ control file/SPFILE using the same backup set on a different device type.

Action: See accompanying additional error messages indicating the cause of the failover.

RMAN-08131: channel string: specifying datafile copies to recover

Cause: This is an informational message only.

Action: No action is required.

RMAN-08132: WARNING: cannot update recovery area reclaimable file list

Cause: This error should be accompanied by other errors giving the cause of failure to update reclaimable file list.

Action: Check the accompanying error.

RMAN-08133: channel string: the AUTOBACKUP does not contain a standby control file.

Cause: The requested AUTOBACKUP did not contain a standby control file.

Action: No action is required, RMAN will try three older AUTOBACKUPS before signaling ORA-19687.

RMAN-08135: some corrupt blocks found during conversion of file string

Cause: While converting the specified file from one platform to another, some corrupt blocks were discovered in the specified file. Details about the corruption have been written to a server trace file.

Action: If these corrupt blocks are unexpected, you may be able to use Block Media Recovery at the source database to fix the problem, then re-convert the files.

RMAN-08136: channel string: deleting incremental backup(s)

Cause: This is an informational message only.

Action: No Action Required.

RMAN-08137: WARNING: archived log not deleted, needed for standby or upstream capture process

Cause: An archived log that should have been deleted was not as it was required by upstream capture process or Data Guard. The next message identifies the archived log.

Action: This is an informational message. The archived log can be deleted after it is no longer needed. See the documentation for Data Guard to alter the set of active Data Guard destinations. See the documentation for Streams to alter the set of active streams.

RMAN-08138: WARNING: archived log not deleted - must create more backups

Cause: An archived log that should have been deleted was not as it it did not meet the user specified archive log deletion policy of number of backups required before deleting the logs.

Action: This is an informational message. The archived log can be deleted after more backups are created to satify archivelog deletion policy.

RMAN-08139: WARNING: archived redo log not deleted, needed for guaranteed restore point

Cause: An archived log that should have been deleted was not because it is required for guaranteed restore point.

Action: This is an informational message. The archived redo log can be deleted after backups are created or after deleting the guaranteed restore point that requires the log.

RMAN-08140: channel string: starting validation of datafile

Cause: This is an informational message only.

Action: No action is required.

RMAN-08141: channel string: specifying datafile(s) for validation

Cause: This is an informational message only.

Action: No action is required.

RMAN-08142: including standby control file for validation

Cause: This is an informational message only.

Action: No action is required.

RMAN-08143: including current control file for validation

Cause: This is an informational message only.

Action: No action is required.

RMAN-08144: channel string: validation complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08145: channel string: starting validation of archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-08146: channel string: specifying archived log(s) for validation

Cause: This is an informational message only.

Action: No action is required.

RMAN-08150: created global script string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08151: replaced global script string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08152: global script string written to file string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08153: deleted global script: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08154: deleted script: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08155: printing stored global script: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08156: printing stored script: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08157: script string written to file string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08158: executing script: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08159: executing global script: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08160: script commands will be loaded from file string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08161: contents of Memory Script:

Cause: This is an informational message only.

Action: No action is required.

RMAN-08162: executing Memory Script

Cause: This is an informational message only.

Action: No action is required.

RMAN-08163: validation succeeded for backup piece

Cause: The VALIDATE HEADER option determined that the backup piece still matches its data.

Action: None - this is an informational message.

RMAN-08164: validation succeeded for proxy copy

Cause: The VALIDATE HEADER option determined that the proxy copy still matches its data.

Action: None - this is an informational message.

RMAN-08165: could not locate proxy copy string

Cause: The specified proxy copy could not be found on proxy channel.

Action: If the proxy copy has been deleted, use the CROSSCHECK BACKUP command to correct the recovery catalog or target database control file entries.

RMAN-08166: validation succeeded for datafile copy and control file copy

Cause: The VALIDATE HEADER option discovered that the datafile copy and control file copy still matches its data in the recovery catalog or target database control file.

Action: None - this is an informational message.

RMAN-08167: WARNING: string encountered a piece that was in use

Cause: The backup piece is currently in use by another BACKUP, RESTORE or DELETE operation.

Action: Use LIST to determine if backup has been deleted. If not deleted, then check if any process is hung while accessing the piece and terminate them before retrying DELETE. If using SBT device, then check Media Manager as well. Alternatively, consider the command DELETE FORCE.

RMAN-08180: channel string: restore complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08181: media recovery complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08182: channel string: validation complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08183: channel string: block restore complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08184: added tempfile string to tablespace string in control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08185: renamed tempfile string to string in control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08186: tempfile string size altered in control file

Cause: One of tempfile size attributes AUTOEXTEND, MAXSIZE, NEXTSIZE was altered. This is an informational message only.

Action: No action is required.

RMAN-08187: WARNING: media recovery until SCN string complete

Cause: Media recovery was completed until the indicated system change number (SCN) because the database was in NOARCHIVELOG mode.

Action: This is an informational message only. No action is required.

RMAN-08190: validate found one or more corrupt blocks

Cause: Backup validate found that one or more blocks were corrupt in the specified datafiles. This message should be followed by 8191 message.

Action: Repair them at your earliest convenience.

RMAN-08191: See trace file string for details

Cause: This is an informational message only.

Action: No action is required.

RMAN-08300: Run SQL script string on the target platform to create database

Cause: This is an informational message only.

Action: No action is required.

RMAN-08301: Edit init.ora file string. This PFILE will be used to create the database on the target platform

Cause: This is an informational message only.

Action: No action is required.

RMAN-08302: Run RMAN script string on target platform to convert datafiles

Cause: This is an informational message only.

Action: No action is required.

RMAN-08303: To recompile all PL/SQL modules, run utlirp.sql and utlrp.sql on the target platform

Cause: This is an informational message only.

Action: Transport script invokes utlirp.sql and utlrp.sql.

RMAN-08304: To change the internal database identifier, use DBNEWID Utility

Cause: This is an informational message only.

Action: Transport script does not invoke DBNEWID Utility automatically.

RMAN-08305: channel string: starting to check datafiles

Cause: This is an informational message only.

Action: No action is required.

RMAN-08306: channel string: datafile checking complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08500: channel string: SID=string device type=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08501: output file name=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08503: piece handle=string comment=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08504: input archived log thread=string sequence=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08505: output file name=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08506: input file name=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08507: input datafile copy RECID=string STAMP=string file name=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08508: archived log destination=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08509: destination for restore of datafile string: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08510: archived log thread=string sequence=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08511: piece handle=string tag=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08512: waiting for snapshot control file enqueue

Cause: This is an informational message only.

Action: No action is required.

RMAN-08513: datafile copy file name=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08514: archived log file name=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08515: archived log file name=string thread=string sequence=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08516: control file copy file name=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08517: backup piece handle=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08518: channel string: scanning control file copy string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08519: channel string: scanning datafile copy string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08520: channel string: scanning archived log string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08521: offline range RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08522: input datafile file number=string name=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08523: restoring datafile string to string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08524: input control file copy name=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08525: backing up blocks string through string

Cause: This is an informational message only

Action: No action is required.

RMAN-08526: channel string: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08527: channel string: starting string proxy datafile backup at string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08528: channel string: proxy copy complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08529: proxy file handle=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08530: piece handle=string tag=string comment=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08531: channel string: proxy copy string is string in media management catalog

Cause: This is an informational message only.

Action: No action is required.

RMAN-08532: channel string: restoring block(s) from datafile copy string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08533: restoring blocks of datafile string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08534: channel string: control file restore from AUTOBACKUP complete

Cause: This is an informational message only.

Action: No action is required.

RMAN-08535: channel string: looking for AUTOBACKUP on day: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08536: channel string: AUTOBACKUP found: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08537: channel string: skipped, AUTOBACKUP already found

Cause: This is an informational message only.

Action: No action is required.

RMAN-08538: channel string: no AUTOBACKUP in string days found

Cause: This is an informational message only.

Action: No action is required.

RMAN-08539: backup set key=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08540: channel string: backup set complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08541: channel string: SPFILE restore from AUTOBACKUP complete

Cause: This is an informational message only.

Action: No action is required.

RMAN-08542: channel string: starting proxy archived log backup at string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08543: channel string: specifying archived log(s) for proxy backup

Cause: This is an informational message only.

Action: No action is required.

RMAN-08544: channel string: specifying archived log(s) for proxy restore

Cause: This is an informational message only.

Action: No action is required.

RMAN-08545: flashback command failed: See trace file for details

Cause: An attempt was made to issue a flashback command which failed due to errors. See trace file for details.

Action: See trace file for details of the problem.

RMAN-08546: channel string: AUTOBACKUP string found in the recovery area

Cause: This is an informational message only.

Action: No action is required.

RMAN-08547: channel string: no AUTOBACKUPS found in the recovery area

Cause: The recovery area does not have desired AUTOBACKUP.

Action: Check the option UNTIL TIME in case an existing AUTOBACKUP does satisfy the criteria specified in the restore command. Otherwise, verify the init.ora parameters DB\_RECOVERY\_FILE\_DEST and DB\_UNIQUE\_NAME to verify whether the recovery area location is set correctly. Note that the parameters can be specified as options to the restore command.

RMAN-08548: recovery area destination: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08549: database name (or database unique name) used for search: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08550: AUTOBACKUP search with format "string" not attempted because DBID was not set

Cause: Restore of a control file AUTOBACKUP was attempted without DBID being set.

Action: If you want to search for AUTOBACKUP with the indicated format, then specify the DBID of the database using SET DBID and retry the command.

RMAN-08551: recovering datafile copy file number=string name=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08552: backup and output file names are identical: string

Cause: The backup file name chosen was identical to output file name specified for a restore operation.

Action: This is an informational message only. RMAN will failover to next available backup.

RMAN-08553: channel string: restoring control file from AUTOBACKUP string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08554: channel string: restoring spfile from AUTOBACKUP string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08555: channel string: restoring section string of string

Cause: This is an informational message only

Action: No action is required.

RMAN-08556: channel string: backup piece complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08580: channel string: starting datafile copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08581: channel string: datafile copy complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08582: channel string: starting archived log copy

Cause: This is an informational message only.

Action: No action is required.

RMAN-08583: channel string: archived log copy complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08584: copying current control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08585: copying standby control file

Cause: This is an informational message only.

Action: No action is required.

RMAN-08586: output file name=string tag=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08587: input is copy of datafile string: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08588: converted datafile=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08589: channel string: starting datafile conversion

Cause: This is an informational message only.

Action: No action is required.

RMAN-08590: channel string: datafile conversion complete, elapsed time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08591: WARNING: invalid archived log deletion policy

Cause: An invalid ARCHIVELOG DELETION POLICY was supplied. The archived log deletion policy was APPLIED but there was no mandatory archived log destinations.

Action: One of the following: 1) Change archived log deletion policy using CONFIGURE command 2) Make one or more of standby destination as MANDATORY.

RMAN-08592: output file name=string tag=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08599: channel string: throttle time: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08600: ASM disk group to search: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08601: channel string: AUTOBACKUP string found in ASM disk group string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08602: channel string: no AUTOBACKUPS found in ASM disk group string

Cause: The specified ASM area does not have desired AUTOBACKUP.

Action: Check the option UNTIL TIME in case an existing AUTOBACKUP does satisfy the criteria specified in the restore command. Otherwise, verify the values used for the format of the CONFIGURE CONTROLFILE AUTOBACKUP FORMAT command and DB\_UNIQUE\_NAME to verify whether the ASM area location is set correctly. Note that the DB\_UNIQUE\_NAME can be specified as option to the restore command.

RMAN-08603: skipping string; file in use by another process

Cause: The indicated file was not included in the backup because it is part of another restore or delete operation.

Action: No action is required. Wait for the other operation to complete, then retry.

RMAN-08604: skipping string; file deleted from recovery area to reclaim disk space

Cause: The indicated file was not included in the backup because it was deleted from the recovery area to reclaim disk space for other operations.

Action: No action is required.

RMAN-08605: channel string: SID=string instance=string device type=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08606: WARNING: The change tracking file is invalid.

Cause: Backup found changed blocks that were not marked in the change tracking file. See alert log for more information.

Action: Do not use any of the incremental backups taken since the last full backup.

RMAN-08607: List of remote backup files

Cause: RESTORE command detected that one or more remote backup files were required to perform restore operation.

Action: Recall the media from remote site that contains the specified backup files before actual restore operation. The message should be accompanied with the list of remote backup files.

RMAN-08608: Initiated recall for the following list of remote backup files

Cause: This is an informational message displayed when the specified RECALL option of the RESTORE command detected that one or more remote backup files were required to perform the restore operation. The message indicated that RMAN had initiated the request on SBT channel to recall the remote backup files.

Action: No action required.

RMAN-08609: channel string: starting incremental datafile backup set

Cause: This is an informational message only.

Action: No action is required.

RMAN-08610: channel string: restoring datafile string to string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08611: channel string: piece handle=string tag=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08612: channel string: failover to duplicate backup on device string

Cause: This is an informational message to indicate the RMAN could not successfully restore the files using the specified backups. An attempt was made to restore the datafiles/archived logs/ control file/SPFILE using a previous existing backup.

Action: See accompanying additional error messages indicating the cause of the failover.

RMAN-08613: channel string: failover to piece handle=string tag=string

Cause: This is an informational message to indicate the server found a corrupted block in a backup piece and had to switch to another copy of the piece to get the same block.

Action: See alert log for information on corruption block(s) and the name of the backup piece that has the corrupted block(s).

RMAN-08614: channel string: errors found reading piece handle=string

Cause: This is an informational message to indicate the server found a corrupted block in a backup piece. Accompanying error will describe the action taken.

Action: See alert log for more information.

RMAN-08615: channel string

Cause: This is an informational message to indicate the server could not perform the restore due to the included errors. A least recent backup set will be used to perform the restore.

Action: See alert log for information on corruption block(s) and the name of the backup piece that has the corrupted block(s).

RMAN-08616: validating blocks string through string

Cause: This is an informational message only

Action: No action is required.

RMAN-08617: validation failed for foreign archived log

Cause: The CROSSCHECK FOREIGN ARCHIVELOG command determined that the foreign archived log could not be found or no longer contained the same data, so its record was marked expired.

Action: None - this is an informational message.

RMAN-08618: validation succeeded for foreign archived log

Cause: The CROSSCHECK FOREIGN ARCHIVELOG command determined that the foreign archived log still matches its data.

Action: None - this is an informational message.

RMAN-08619: foreign archived log file name=string RECID=string STAMP=string

Cause: This is an informational message only.

Action: No action is required.

RMAN-08620: uncataloged foreign archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-08621: deleted foreign archived log

Cause: This is an informational message only.

Action: No action is required.

RMAN-08629: waiting for resources on Oracle Availability Machine for string channels

Cause: The number of channels required to complete this operation was not available. Channels will be allocated when they become available.

Action: No action is required. This is an informational message only.

RMAN-08630: allocating the required resources on Oracle Availability Machine

Cause: The required resources were allocated on Oracle Availability Machine.

Action: No action is required. This is an informational message only.

RMAN-10000: error parsing target database connect string "string"

Cause: An invalid target connect string was supplied.

Action: Specify a valid connect string and re-run the job.

RMAN-10001: error parsing recovery catalog connect string "string"

Cause: An invalid recovery catalog connect string was supplied.

Action: Specify a valid connect string and re-run the job.

RMAN-10002: ORACLE error: string

Cause: The specified Oracle error was received. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-10003: unable to connect to target database

Cause: Recovery manager was unable to connect to the target database. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Ensure that that the target database is started, and that the connect string is valid.

RMAN-10004: unable to connect to recovery catalog

Cause: Recovery manager was unable to connect to the recovery catalog

Action: Ensure that that the recovery catalog is started, and that the connect string is valid. This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-10005: error opening cursor

Cause: An error was received while trying to open a cursor. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: If the associated Oracle error message indicates a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-10006: error running SQL statement: string

Cause: An error message was received while running the SQL statement shown.

Action: If the associated Oracle error message indicates a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-10007: error closing cursor

Cause: An error was received while trying to close a cursor. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: If the associated Oracle error message indicates a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-10008: could not create channel context

Cause: An error was received while trying create a channel context. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: If the associated Oracle error message indicates a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-10009: error logging off of Oracle

Cause: An error was received while disconnecting from Oracle. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: This is an informational message only.

RMAN-10010: error while checking for RPC completion

Cause: Recovery Manager's channel context had an error while checking to see if a remote procedure call had completed. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: If other error messages indicate a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-10011: synchronization error while polling for rpc number, action=string

Cause: Recovery Manager could not synchronize properly with a remote procedure call.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10012: KGU error: string

Cause: An error occurred while initializing the KGU subsystem

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10013: error initializing PL/SQL

Cause: An error occurred while initializing the PL/SQL subsystem.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10014: PL/SQL error number on line number column number: string

Cause: PL/SQL error

Action: The text of this message will be issued by the PL/SQL subsystem. See the PL/SQL error message manual.

RMAN-10015: error compiling PL/SQL program

Cause: An error occurred while compiling a PL/SQL program.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10018: error cleaning up channel context

Cause: An error was received during inter-step cleanup of a channel context.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10020: error initializing Recovery Manager execution layer

Cause: An error was received while initializing the Recovery Manager execution layer in preparation for running a job. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: If other error messages indicate a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-10022: error in system-dependent sleep routine

Cause: An error was received while waiting for a remote RPC to complete. The error occurred in the system-dependent sleep routine.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10023: RPC attempted to unrecognized package

Cause: The Recovery Manager internal RPC router received a package name that it could not understand.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10024: error setting up for rpc polling

Cause: The Recovery Manager could not create the RPC polling context which is required to test for RPC completion. This message should be accompanied by other error message(s) indicating the cause of the error.

Action: If other error messages indicate a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-10025: connection is already registered for events

Cause: The Recovery Manager could not enable the target database connection to test for RPC completion.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10026: network error number-number occurred registering connection

Cause: An network error occurred while attempting to register the target database connection to test for RPC completion.

Action: This is an internal error that should not be issued. The message numbers are issued by the Sql\*Net layer. Contact Oracle Support.

RMAN-10027: could not locate network layer context

Cause: Recovery Manager could not locate a necessary context area while attempting to register the target database connection to test for RPC completion.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10028: network error number-number occurred during remote RPC

Cause: An network error occurred while waiting for a remote RPC to complete.

Action: This is an internal error that should not be issued. The message numbers are issued by the Sql\*Net layer. Contact Oracle Support.

RMAN-10029: unexpected return code number from PL/SQL execution

Cause: PL/SQL returned an unexpected return code while executing one channel program.

Action: This is an internal error that should not be issued. Contact Oracle Support.

RMAN-10030: RPC call appears to have failed to start on channel string

Cause: An RPC to a target database instance was issued, but was not observed to start within 5 timeouts.

Action: This error is probably accompanied by other error messages giving the precise cause of the failure.

RMAN-10031: RPC Error: ORA-number occurred during call to string.string

Cause: An RPC to the target database or recovery catalog database encountered an error.

Action: This error is accompanied with the error message from the server where the error occurred.

RMAN-10032: unhandled exception during execution of job step number: string

Cause: An unhandled PL/SQL exception occurred during a job step.

Action: This error is accompanied by the error messages describing the exception.

RMAN-10033: error during compilation of job step number: string

Cause: PL/SQL detected a problem during the compilation of a job step

Action: This error message is accompanied by the error messages describing

RMAN-10034: unhandled exception during execution of job step number, error unknown

Cause: PL/SQL detected an unhandled exception during execution of a job step, but no further information available

Action: None

RMAN-10035: exception raised in RPC: string

Cause: A call to a remote package resulted in an exception.

Action: The exception should indicate what went wrong.

RMAN-10036: RPC call OK on channel string

Cause: This is just an informational message. It should be preceded by message 10030.

Action: No action is required.

RMAN-10037: RPC anomaly detected on channel string, UPINBLT=number

Cause: This is an debugging message and can be ignored.

Action: No action is required.

RMAN-10038: database session for channel string terminated unexpectedly

Cause: The database connection for the specified channel no longer exists. Either the session was terminated by some external means or the channel terminated because of an internal error.

Action: Check for an oracle trace file for detailed information on why the session terminated.

RMAN-10039: error encountered while polling for RPC completion on channel string

Cause: This error should be accompanied by other errors giving the cause of the polling error.

Action: Check the accompanying errors.

RMAN-10040: asynchronous support not detected, RMAN will run synchronously

Cause: The database connection does not support asynchronous operation, so RMAN will not multi-task work among multiple channels. Multiple channels can still be allocated, but they will not run work concurrently.

Action: Use a connection type that supports asynchronous operations.

RMAN-10041: Could not re-create polling channel context following failure.

Cause: The RPC polling context, which is required to test for RPC completion, failed and Recovery Manager could not re-create this channel. This message should be accompanied by other error messages indicating the cause of the error.

Action: If other error messages indicate a condition that can be corrected, do so, otherwise contact Oracle.

RMAN-11000: message number number not found in recovery manager message file

Cause: Recovery manager message file is out of date.

Action: Make sure that the recovery manager error message file is current and installed in the correct location.

RMAN-11001: Oracle Error: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-11002: could not open a cursor to the target database

Cause: This is an informational message only.

Action: No action is required.

RMAN-11003: failure during parse/execution of SQL statement: string

Cause: This is an informational message only.

Action: No action is required.

RMAN-11004: format requires %c when duplexing

Cause: SET\_DUPLEX=ON was specified, but %c was not part of the format.

Action: Include %c in format, or use %U.

RMAN-11005: conflicting media information for piece "string"

Cause: While restoring the specified backup piece, RMAN received conflicting information about the physical location of the piece from the Media Management software. This can cause poor restore performance.

Action: If RMAN does not parallelize the restore from all of the available channels, then you should contact the Media Management vendor.

RMAN-11006: WARNING: test recovery results: string

Cause: User called recover database with the test option

Action: None required

RMAN-12000: execution layer initialization failed

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-12001: could not open channel string

Cause: An ALLOCATE CHANNEL command could not be processed.

Action: This message should be accompanied by other error message(s) indicating the cause of the error.

RMAN-12005: error during channel cleanup

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-12007: cannot allocate more than number channels

Cause: The maximum number of RMAN channels has been exceeded. Note that one channel is reserved for RMAN.

Action: Allocate fewer channels. Contact Oracle if you have a need for more channels in a single job.

RMAN-12008: could not locate backup piece string

Cause: There was at least 1 backup set that could not be accessed by any of the allocated channels.

Action: Allocate additional channels on other nodes of the cluster

RMAN-12009: command aborted because some backup pieces could not be located

Cause: Same as 7008.

Action: Refer to 7008.

RMAN-12010: automatic channel allocation initialization failed

Cause: This message should be accompanied by other error message(s) indicating the cause of the error.

Action: Check the accompanying errors.

RMAN-12011: multiple records for default device type found in repository

Cause: Configuration for default device type was not consistent.

Action: Re-run CONFIGURE DEFAULT DEVICE TYPE command to set device type.

RMAN-12012: multiple records for string parallelism found in repository

Cause: Configuration for device parallelism was not consistent.

Action: Re-run CONFIGURE PARALLELISM command for device to set parallelism.

RMAN-12013: multiple records for string channel number found in repository

Cause: Configuration for the channel was not consistent.

Action: Re-run CONFIGURE CHANNEL command to configure this channel.

RMAN-12014: multiple records for default channel configuration for string found in repository

Cause: Configuration for the channel was not consistent.

Action: Re-run CONFIGURE CHANNEL command to configure the channel.

RMAN-12015: configuration for string channel number is ignored

Cause: This is an informational message only. Parallelism for the device is less than associated channel number.

Action: To use this configuration increase parallelism for this device. To clear this configuration use CONFIGURE CHANNEL... CLEAR command.

RMAN-12016: using channel string

Cause: This is an informational message only.

Action: No action is required.

RMAN-12017: could not locate pieces of backup set key string

Cause: Copies of the specified backup set key could not be accessed on any of the allocated channels.

Action: Allocate additional channels on other nodes of the cluster or, if the backup pieces has been deleted, use the CROSSCHECK BACKUP command to correct the recovery catalog or target database control file entries.

RMAN-12018: channel string disabled, job failed on it will be run on another channel

Cause: This is an informational message displayed whenever a retryable error occurs for the job and there are channels available to run this step.

Action: No action is required.

RMAN-12019: continuing other job steps, job failed will not be re-run

Cause: This is an informational message displayed whenever there is a non-retryable error occurred for the job.

Action: No action is required.

RMAN-12020: error on step filtered for normal output string

Cause: This message is added when stacking errors for failed jobs after channel failover was performed. It will be filtered from normal output.

Action: No action is required.

RMAN-20000: abnormal termination of job step

Cause: A job step encountered an error and could not recover. This error should be followed by other errors indicating the cause of the problem.

Action: Check the accompanying error.

RMAN-20001: target database not found in recovery catalog

Cause: target database is not found in the recovery catalog

Action: make sure that the target database is registered in the recovery recovery catalog

RMAN-20002: target database already registered in recovery catalog

Cause: target database is already registered in the recovery catalog

Action: if the target database is really registered, there is no need to register it again. Note that the recovery catalog enforces that all databases have a unique DBID. If the new database was created by copying files from an existing database, it will have the same DBID as the original database and cannot be registered in the same recovery catalog.

RMAN-20003: target database incarnation not found in recovery catalog

Cause: RESETLOGS CHANGE# and/or time of the target database doesn't match any database incarnation in the recovery catalog.

Action: if target database was opened with RESETLOGS option then use 'reset database' to register the new incarnation.

RMAN-20004: target database name does not match name in recovery catalog

Cause: name of the target database doesn't match the one stored in the recovery catalog

Action: This is an internal error.

RMAN-20005: target database name is ambiguous

Cause: two or more databases in the recovery catalog match this name

Action: None

RMAN-20006: target database name is missing

Cause: target database instance is not started or db\_name initialization parameter is not set

Action: startup the instance and make sure that db\_name parameter is set

RMAN-20009: database incarnation already registered

Cause: this incarnation is already registered in the recovery catalog

Action: No action is required.

RMAN-20010: database incarnation not found

Cause: database incarnation does not match any database incarnation in the recovery catalog

Action: specify a valid database incarnation key

RMAN-20011: target database incarnation is not current in recovery catalog

Cause: the database incarnation that matches the RESETLOGS CHANGE# and time of the mounted target database control file is not the current incarnation of the database

Action: If 'reset database to incarnation \<key>' was used to make an old incarnation current then restore the target database from a backup that matches the incarnation and mount it. You will need to do 'STARTUP NOMOUNT' before you can restore the control file using RMAN. Otherwise use 'reset database to incarnation \<key>' make the intended incarnation current in the recovery catalog.

RMAN-20012: not authorized to register new database

Action: Ask the catalog administrator to grant permission for you to register this database.

RMAN-20013: error upgrading virtual private catalog

Cause: An error occurred while automatically upgrading a virtual private catalog.

Action: Ensure that the virtual private catalog userid has all of the required privileges, such as being granted the RECOVERY\_CATALOG\_OWNER role.

RMAN-20014: virtual private catalog owner must be granted RECOVERY\_CATALOG\_OWNER role

Cause: An attempt was made to establish a virtual private RMAN catalog in a schema that is not granted the RECOVERY\_CATALOG\_OWNER role.

Action: Grant RECOVERY\_CATALOG\_OWNER to the virtual private catalog owner.

RMAN-20015: not authorized to share this catalog

Cause: You attempted to share a recovery catalog but were not authorized to do this by the catalog administrator.

Action: Ask the catalog administrator to grant permission for you to share this catalog.

RMAN-20016: virtual private catalog user cannot modify global scripts

Cause: A virtual private catalog user attempted to create, delete, or modify a global script. Virtual private catalog users cannot modify global scripts.

Action: Connect to the catalog owner userid and retry the global script operation.

RMAN-20017: illegal script update operation

Cause: An illegal script operation was performed.

Action: None

RMAN-20018: database not found in recovery catalog

Cause: An attempt was made to grant or revoke catalog access to a database whose name was not registered in the recovery catalog.

Action: Correct the database name and re-issue the GRANT or REVOKE command. If this is an attempt to grant or revoke access to a database that is not yet registered, then re-issue the command using the database ID of the desired database.

RMAN-20019: database name not unique in recovery catalog

Cause: An attempt was made to grant or revoke catalog access to a database whose name is not unique in the recovery catalog.

Action: Re-issue the command specifying the database ID of the desired database.

RMAN-20022: user not found

Cause: An attempt was made to grant a privilege to a user that does not exist.

Action: Reissue the command specifying a user that exists.

RMAN-20029: cannot make a snapshot control file

Cause: another operation that needs the snapshot control file is in progress

Action: try again later if necessary

RMAN-20030: resync in progress

Cause: this procedure cannot be called while a resync is in progress

Action: This is an internal error.

RMAN-20031: resync not started

Cause: this procedure can only be called in a resync

Action: This is an internal error.

RMAN-20032: checkpoint CHANGE# too low

Cause: the checkpoint change# is less than the one of the previous resync or the checkpoint change# is null

Action: make sure that the right control file is used

RMAN-20033: control file SEQUENCE# too low

Cause: the control file sequence is less than the one of the previous resync

Action: make sure that the right control file is used

RMAN-20034: resync not needed

Cause: the control file has not changed since the previous resync

Action: nothing since the recovery catalog is in sync

RMAN-20038: must specify FORMAT for CONVERT command

Cause: No FORMAT was specified when using CONVERT command.

Action: Resubmit the command using FORMAT clause.

RMAN-20039: format requires character when duplexing

Cause: SET\_DUPLEX=ON was specified, but %c was not part of the format.

Action: Include %c in format, or use %U.

RMAN-20045: must specify FORMAT for BACKUP INCREMENTAL FROM SCN command

Cause: No FORMAT was specified when using BACKUP INCREMENTAL FROM SCN command.

Action: Resubmit the command using FORMAT clause.

RMAN-20079: full resync from primary database is not done

Cause: Resync from standby detected that a full resync from primary database is required. One of the following events on primary database may have caused this error: 1) one or more tablespaces or datafiles were added 2) one or more tablespaces or datafiles were dropped 3) one or more datafiles status changed

Action: Perform full resync after connecting to primary database.

RMAN-20081: change stamp for the record

Cause: A record with same recid and stamp is already known to catalog.

Action: None. This error is automatically handled by RMAN client by changing the stamp in control file during resync.

RMAN-20108: control file for remote database cannot be updated

Cause: RESYNC CATALOG FROM DB\_UNIQUE\_NAME command was attempted, but the control file at the database with DB\_UNIQUE\_NAME needs to be resynced directly instead of through the current target.

Action: Directly connect as target to the remote database with the specified DB\_UNIQUE\_NAME and resync.

RMAN-20109: remote database has different database ID

Cause: Command RESYNC CATALOG FROM DB\_UNIQUE\_NAME was executed and the database ID of the remote database was different than the connected target database.

Action: The remote database should have the same database ID as the database connected as the target database. Fix the connect identifier for the remote database and retry the command.

RMAN-20201: datafile not found in the recovery catalog

Cause: The specified datafile is not found in the recovery catalog

Action: make sure that the datafile name is correct and that the recovery catalog is up-to-date

RMAN-20202: Tablespace not found in the recovery catalog

Cause: the specified tablespace is not found in the recovery catalog

Action: make sure that the tablespace name is correct and that the recovery catalog is up-to-date

RMAN-20203: translation in progress

Cause: this procedure can not be called when name translation is in progress

Action: This is an internal error.

RMAN-20204: translation not started

Cause: GETDATAFILE procedure was called before TRANSLATETABLESPACE

Action: This is an internal error.

RMAN-20205: incomplete UNTIL clause

Cause: The sequence# was NULL

Action: This is an internal error.

RMAN-20206: log sequence not found in the repository

Cause: The specified log sequence does not exists in log history of the current database incarnation

Action: check the thread# and sequence#

RMAN-20207: UNTIL TIME or RECOVERY WINDOW is before RESETLOGS time

Cause: UNTIL TIME and RECOVERY WINDOW cannot be less than the database creation time or RESETLOGS time.

Action: Check the UNTIL TIME or RECOVERY WINDOW. If the database needs to be restored to an old incarnation, use the RESET DATABASE TO INCARNATION command.

RMAN-20208: UNTIL CHANGE is before RESETLOGS change

Cause: UNTIL CHANGE cannot be less than the database RESETLOGS change.

Action: Check the UNTIL CHANGE. If the database needs to be restored to an old incarnation, use the RESET DATABASE TO INCARNATION command.

RMAN-20209: duplicate datafile name

Cause: Two datafiles have the same name

Action: This is an internal error.

RMAN-20211: FROM TIME is before RESETLOGS time

Cause: FROM TIME cannot be less than the database creation time or RESETLOGS time.

Action: Check the FROM TIME. If the database needs to be restored to an old incarnation, use the RESET DATABASE TO INCARNATION command.

RMAN-20212: UNTIL CHANGE is an orphan incarnation

Cause: Specified UNTIL CHANGE was an orphan incarnation.

Action: Check the UNTIL CHANGE or UNTIL RESTORE POINT. If the database needs to be restored or flashed back to an orphan incarnation, use the RESET DATABASE TO INCARNATION command.

RMAN-20215: backup set not found

Cause: The specified backup set key was not found in the recovery catalog or target database control file.

Action: Specify a different backup set key.

RMAN-20217: datafile not part of the database

Cause: the datafile does not exists or did not exist at until time/scn

Action: check the datafile name or number. This is an internal error. for restore database or tablespace.

RMAN-20218: datafile not found in repository

Cause: This is an internal error.

Action: Contact Oracle Support Services.

RMAN-20220: control file copy not found in the repository

Cause: The specified control file was not in the recovery catalog or target database control file or it was marked deleted.

Action: check the file name

RMAN-20221: ambiguous control file copy name

Cause: more than one control file copy in the recovery catalog match the specified name.

Action: None

RMAN-20222: datafile name not found in recovery catalog or is ambiguous

Cause: The specified datafile name is not the name of a datafile that is currently part of the target database, or an UNTIL clause has been specified and the file name was for a different datafile at the time specified by the UNTIL clause than it is now.

Action: Use a datafile number to specify the datafile you want to RESTORE or RECOVER.

RMAN-20223: DB\_UNIQUE\_NAME mismatch in snapshot control file

Cause: The DB\_UNIQUE\_NAME value in the snapshot control file was incorrect. This error can occur in Oracle RAC when the snapshot control file location is not shared across nodes and virtual IPs are setup in the remote database from where resynchronization is done using RESYNC CATALOG FROM DB\_UNIQUE\_NAME commnad.

Action: To avoid this error, one of the following actions can be taken: 1) Share the control file snapshot location. The snapshot location can be displayed by executing SHOW SNAPSHOT CONTROLFILE NAME at the RMAN prompt. 2) Do not use Virtual IPs in the service name used to define the connect identifiers. The connect identifiers can be displayed using SHOW DB\_UNIQUE\_NAME command at the RMAN prompt.

RMAN-20230: datafile copy not found in the repository

Cause: The specified datafile was not in the recovery catalog or target database control file or it was marked deleted.

Action: check the datafile copy name or key

RMAN-20231: ambiguous datafile copy name

Cause: more than one control file copy in the recovery catalog match the specified name.

Action: use the datafile copy key to uniquely specify the datafile copy

RMAN-20240: archived log not found in the repository

Cause: The specified archived log was not found in the recovery catalog or target database control file or it was marked deleted.

Action: check the archived log name or key

RMAN-20241: ambiguous archived log name

Cause: more than one archived log in the recovery catalog match the specified name

Action: use the archived log key to uniquely specify the archived log

RMAN-20242: specification does not match any archived log in the repository

Cause: No archived logs found that match specification in the recovery catalog or target database control file.

Action: check the archived log specifier

RMAN-20243: database db\_unique\_name is not known to the recovery catalog

Cause: the user specified DB\_UNIQUE\_NAME not known to the recovery catalog.

Action: change the database DB\_UNIQUE\_NAME to a known database value. To display list of known db\_unique\_names execute LIST DB\_UNIQUE\_NAME OF DATABASE

RMAN-20244: can not change currently connected database db\_unique\_name

Cause: the user specified currently connected DB\_UNIQUE\_NAME value to unregister.

Action: use the DB\_UNIQUE\_NAME other than connected target database's DB\_UNIQUE\_NAME value.

RMAN-20245: can not specify db\_unique\_name option in nocatalog mode

Cause: the user specified DB\_UNIQUE\_NAME in nocatalog mode.

Action: remove the DB\_UNIQUE\_NAME option from the command.

RMAN-20246: new db\_unique\_name is already known to the recovery catalog

Cause: the user specified known DB\_UNIQUE\_NAME value when renaming a DB\_UNIQUE\_NAME in the recovery catalog.

Action: change the database DB\_UNIQUE\_NAME to an known DB\_UNIQUE\_NAME value; or unregister the new DB\_UNIQUE\_NAME before renaming an old DB\_UNIQUE\_NAME value for a database. To display the list of all DB\_UNIQUE\_NAME for the databases LIST DB\_UNIQUE\_NAME OF DATABASE command can be executed.

RMAN-20247: specification does not match any foreign archived log in the repository

Cause: No foreign archived logs found that match specification in the recovery catalog or target database control file.

Action: check the foreign archived log specifier

RMAN-20250: offline range not found in the repository

Cause: The specified offline was not found in the recovery catalog or target database control file.

Action: check that recovery catalog is current

RMAN-20260: backup piece not found in the repository

Cause: The specified backup piece was not in the recovery catalog or target database control file or it was marked deleted.

Action: check the backup piece handle or key

RMAN-20261: ambiguous backup piece handle

Cause: more than one backup piece in the recovery catalog match the specified handle

Action: use the backup piece key to uniquely specify the backup piece

RMAN-20272: no parent backup found for the incremental backup

Cause: no available backup or copy that could be used as the parent of the incremental backup was found in the recovery catalog.

Action: take a level 0 backup or copy of the datafile first

RMAN-20280: too many device types

Cause: more than 8 device types were allocated

Action: make sure that the job allocates at most 8 different device types

RMAN-20298: DBMS\_RCVCAT package not compatible with the recovery catalog

Cause: The version of the recovery catalog tables does not work with this version of the DBMS\_RCVCAT package.

Action: Check that the recovery catalog packages and schema are installed correctly. The UPGRADE CATALOG command can be used to upgrade the recovery catalog tables and packages to the most current version.

RMAN-20299: DBMS\_RCVMAN package not compatible with the recovery catalog

Cause: The version of the recovery catalog tables does not work with this version of the DBMS\_RCVMAN package.

Action: Check that the recovery catalog packages and schema are installed correctly. The UPGRADE CATALOG command can be used to upgrade the recovery catalog tables and packages to the most current version.

RMAN-20310: proxy copy not found in the repository

Cause: The specified proxy copy was not in the recovery catalog or target database control file or it was marked deleted.

Action: check the proxy copy handle or key

RMAN-20311: ambiguous proxy copy handle

Cause: more than one proxy copy in the recovery catalog matches the specified handle

Action: use the proxy copy key to uniquely specify the proxy copy

RMAN-20401: script already exists

Cause: a CREATE SCRIPT was issued, but a script with the specified name already exists.

Action: use a different name or use REPLACE SCRIPT.

RMAN-20501: redo logs from parent database incarnation cannot be applied

Cause: A RESTORE or RECOVER of a datafile was requested, but recovery of the datafile would require applying redo logs that were generated before the most recent OPEN RESETLOGS.

Action: If a full backup or datafile copy from the current database incarnation exists, ensure that it is marked AVAILABLE, and that a channel of the correct device type is allocated. It may also be necessary to remove the FROM BACKUPSET or FROM DATAFILECOPY or FROM TAG operands if these have been specified.

RMAN-20502: DELETE EXPIRED cannot delete objects that exist - run CROSSCHECK

Cause: A DELETE EXPIRED command was run, but the object was actually found to exist. This means the recovery catalog or target database control file is out of sync with reality.

Action: Run CROSSCHECK.

RMAN-20503: DELETE cannot delete expired objects - run CROSSCHECK or DELETE EXPIRED

Cause: A DELETE command was run without EXPIRED option, but the object doesn't exist. This means the recovery catalog or target database control file is out of sync with reality.

Action: Run CROSSCHECK.

RMAN-20504: corruption list not found in recovery catalog

Cause: corruption list is empty

Action: make sure that one or more blocks are marked corrupted in v$copy\_corruption and v$backup\_corruption and recovery catalog is up-to-date.

RMAN-20505: create datafile during recovery

Cause: applying of archived log caused a create datafile redo-entry to to terminate recovery.

Action: none. This message is never displayed. RMAN automatically detects this case and creates the datafile.

RMAN-20506: no backup of archived log found

Cause: during the recover process, no backup was found from which the archived logs could be restored.

Action: this message should be followed by a list of missing archived logs. Please make the necessary archived log backups available and try again.

RMAN-20507: some targets are remote - aborting restore

Cause: during the restore process, one or more backup files were unavailable locally for the restore operation.

Action: This message should be accompanied with the list of remote backup files. Recall these backups from remote location and retry the RESTORE command.

RMAN-20508: temporary resource already in use

Cause: Temporary resource that was allocated for IMPORT CATALOG command was already in use.

Action: Retry IMPORT CATALOG command.

RMAN-20509: temporary resource not found

Cause: Temporary resource that was allocated for IMPORT CATALOG command was not found.

Action: Retry IMPORT CATALOG command.

RMAN-20510: database not found in source recovery catalog database

Cause: Database that was specified in IMPORT CATALOG command was not found in the source recovery catalog database.

Action: Make sure that the database is registered in the source recovery catalog database.

RMAN-20511: database name is ambiguous in source recovery catalog database

Cause: Two or more databases in the source recovery catalog database match this name.

Action: Use DBID option in IMPORT CATALOG command to specify the source database.

RMAN-20512: source database already registered in recovery catalog

Cause: Source database was already registered in the recovery catalog.

Action: If the source database is really registered, there is no need to register it again. Note that the recovery catalog enforces that all databases have a unique DBID. If the new database was created by copying files from an existing database, it will have the same DBID as the original database and cannot be registered in the same recovery catalog.

RMAN-20514: feature requires Availability Machine recovery catalog

Cause: The specified command required the Availability Machine recovery catalog.

Action: Connect to the Availability Machine recovery catalog and retry the command.