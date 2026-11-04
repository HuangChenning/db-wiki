---
title: DGM-16900 to DGM-17017
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/dgmus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 41 DGM-16900 to DGM-17017

DGM-16900: Unable to initialize client

Cause: The client could not be initialized.

Action: This is an internal error. Contact Oracle Support Services.

DGM-16901: Unable to initialize environment

Cause: The database environment could not be allocated and initialized.

Action: This is an internal error. Contact Oracle Support Services.

DGM-16902: Unable to allocate handle

Cause: The database handle could not be allocated.

Action: This is an internal error. Contact Oracle Support Services.

DGM-16903: Unable to connect to database

Cause: The specified database was unreachable because it did not exist or was not started.

Action: Start the database or validate network connections and try again.

DGM-16904: Unable to set attribute

Cause: The server attributes could not be set.

Action: Check additional error messages.

DGM-16905: Failed.

Cause: The command failed to execute.

Action: Check additional error messages.

DGM-16906: Unable to accept commands: no memory

Cause: No memory was available for the attempted operation.

Action: Check your system and retry the command.

DGM-16909: Fatal error - quitting...

Cause: A fatal error was encountered.

Action: See additional error messages and/or contact Oracle Support Services.

DGM-16910: Unable to issue command to server

Cause: Command could not be issued to the server.

Action: See additional error messages and/or contact Oracle Support Services.

DGM-16912: Unrecognized command "string", try "help"

Cause: An unrecognized command was issued.

Action: Try again using a valid command.

DGM-16916: Missing site name, try "help"

Cause: The site name is missing from the command.

Action: Try the command again using correct syntax.

DGM-16934: start up instance "string" of database "string"

Cause: The operation completed successfully and requires a restart of the specified instance. DGMGRL attempted to restart the instance but was unable to.

Action: Start the specified instance manually.

DGM-16943: connect to instance "string" of database "string"

Cause: The operation required DGMGRL to connect to a specific instance to complete, but DGMGRL could not automatically connect to the given instance.

Action: Connect to the specified instance and issue the command again.

DGM-16944: Failover succeeded, new primary is "string"

Cause: The failover command completed successfully."

Action: No action is required.

DGM-16945: Syntax error before or at "string"

Cause: The command could not be processed because of a syntax error in the named token.

Action: Try the command again using valid syntax.

DGM-16946: Site "string" was not found

Cause: The named site could not be found.

Action: Try the command again using a valid site name.

DGM-16948: Unable to switchover, primary database is still "string"

Cause: The switchover operation could not be executed due to the errors reported with this error message. The primary role has not been changed.

Action: Correct the errors and try the SWITCHOVER command again.

DGM-16949: Object "string" was not found

Cause: The named object was not found.

Action: Try the command again using a valid database name.

DGM-16951: Unable to failover

Cause: The failover operation could not be executed due to the errors reported with this error message.

Action: Correct the errors and try the FAILOVER command again.

DGM-16952: Configuration details cannot be determined by DGMGRL

Cause: The broker configuration could not be found.

Action: 1) The Data Guard broker process (DMON) could not be contacted. Verify that the DMON process is running. 2) No broker configuration currently exists. You must create one. 3) You are connected to a standby database in the broker configuration that has either been disabled or deleted. While the standby is in this state, the details of the broker configuration are not available on the standby database. Connect to the primary database and reissue the command. 4) You are connected to a database in the broker configuration that must be reinstated or reinstantiated. While in this state, details of the broker configuration are not available. Either reinstate or reinstantiate the database and reissue the command, or connect to the primary database and reissue the command.

DGM-16953: XML document is too long

Cause: The length of the XML document exceeded the internal limit.

Action: This is an internal error. Contact Oracle Support Services.

DGM-16954: Unable to open and lock the Observer configuration file

Cause: The Observer configuration file cannot be opened or cannot be locked for exclusive access.

Action: Make sure the Observer has the correct operating system privileges to write the file and there is no other Observer that is using the same file. Try the command again.

DGM-16959: No response from broker server process

Cause: No response was received from the broker server process (DMON).

Action: The Data Guard broker process (DMON) is not available. Verify that the DMON process is running and retry the command.

DGM-16960: Status not available

Cause: The status could not be retrieved.

Action: The Data Guard broker process (DMON) is not available. Verify that the DMON process is running and retry the command.

DGM-16979: Unable to log on to the primary or standby database as SYSDBA

Cause: The username/password used by the observer to log on to the primary database and Fast-Start Failover target standby database does not have valid SYSDBA credentials.

Action: Make sure the primary database and Fast-start failover target database are using a remote login password file. Make sure the SYSDBA password is the same at both databases and that the SYSDBA password is used in the CONNECT command. Start the observer again.

DGM-16991: Two or more resources have the name "string"

Cause: The named resource exists on more than one site.

Action: Use the ON SITE clause and reissue the command.

DGM-16999: Instance "string" was not found

Cause: The named instance could not be found.

Action: Try the command again using a valid instance name.

DGM-17000: Two or more instances have the name "string"

Cause: The named instance exists on more than one database.

Action: Use the ON DATABASE clause and reissue the command.

DGM-17002: Primary database cannot be removed

Cause: The named database to be removed is the primary database.

Action: Remove the broker configuration instead.

DGM-17007: Unsupported platform, observer cannot start

Cause: The Observer was started on an operating system that does not support multi-threading.

Action: Start the Observer on an operating system that supports multi-threading.

DGM-17009: New primary database "string" is opening...

Cause: The Data Guard broker is opening the specified new primary database. The new primary database is ready to accept transactions once it is open.

Action: None

DGM-17016: failed to retrieve status for database "string"

Cause: DGMGRL could not retrieve the StatusReport property from the given database and thus could not report the database status.

Action: See accompanying messages for details.

DGM-17017: unable to determine configuration status

Cause: The Data Guard broker could not execute a health check at the moment, so the configuration status could not be determined.

Action: See accompanying messages for details.