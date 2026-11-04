---
title: CLSGN-00000 to CLSGN-32767
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/clsgnus.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 57 CLSGN-00000 to CLSGN-32767

CLSGN-00000: no error

Cause: Operation was successful.

Action: No action needed.

CLSGN-00003: unknown command: "string"

Cause: The command entered was invalid.

Action: Specify a valid command.

CLSGN-00018: parameter has no default value.

Cause: An attempt was made to reset the value of a parameter for which there is no default value.

Action: Specify a parameter which has a default value.

CLSGN-00023: "string" is only available in interactive mode.

Cause: An attempt was made to run or get help for a command from the command line which is available only in interactive mode.

Action: Change to interactive mode to run the command.

CLSGN-00024: Server abort exception caught - shutting down.

Cause: Informational message that the server is aborting.

Action: Examine the alert log and trace files to determine the reason(s) why the abort is occurring.

CLSGN-00025: Creation of name object for configuration file "string" failed.

Cause: It was not possible to create a name object for the configuration file.

Action: Examine the rest of the stack for the exact reason.

CLSGN-00026: Configuration file "string" does not exist.

Cause: The configuration file specifed could not be found.

Action: Specify a file that exists.

CLSGN-00027: Initialization of object for configuration file "string" failed.

Cause: It was not possible to create a file object for the specified file.

Action: Examine the rest of the error stack for the exact reason.

CLSGN-00028: Open of configuration file "string" failed.

Cause: The open of the configuration file failed.

Action: Examine the rest of the error stack for the exact reason.

CLSGN-00029: Read of configuration file "string" failed.

Cause: A read of the configuration file failed.

Action: Examine the rest of the error stack for the exact reason.

CLSGN-00030: Close of configuration file "string" failed.

Cause: It was not possible to close the configuration file.

Action: Examine the rest of the error stack for the exact reason.

CLSGN-00031: Server failed to start: string

Cause: The GNS server failed to start due to an error encountered by the server.

Action: Examine the message that accompanies this one for details. Also, take a look at the server log files for more information.

CLSGN-00032: Unexpected end of line found in record "string".

Cause: The line ended unexpectedly. For example, the line might have ended before the end of a quoted string was found.

Action: Specify a correctly formatted line.

CLSGN-00033: Too few arguments for value of parameter "string" Minimum: number

Cause: Not enough arguments were specified for a parameter.

Action: Specify the required number of arguments.

CLSGN-00034: Too many arguments for value of parameter "string" Maximum: number

Cause: The number of arguments specified for a parameter was greater than maximum allowed.

Action: Specify the required number of arguments.

CLSGN-00035: Record "string" contains too few fields. Minimum: number. Specified: number.

Cause: The entry for a parameter in the configuration file does not contain the required number of fields.

Action: Correct the entry to have the required number of fields.

CLSGN-00036: Record "string" contains too many fields. Maximum: number. Specified: number.

Cause: The entry for a parameter in the configuration file contains more than the maximum number of fields.

Action: Correct the entry to have the required number of fields.

CLSGN-00039: invalid value for floating point parameter: "string": "string"

Cause: The value specified for a floating point parameter was not floating point.

Action: Specify a correct value.

CLSGN-00040: invalid value for integer parameter: "string": "string"

Cause: The value specified for an integer parameter was not an integer.

Action: Specify a correct value, either decimal or hexadecimal. Hexadecimal values start with the string "0x".

CLSGN-00041: invalid value for boolean parameter "string": "string"

Cause: The value specified for a boolean parameter was not a boolean value.

Action: Specify a correct value. Correct values include: TRUE/FALSE, YES/NO, ON/OFF, and 1/0.

CLSGN-00043: invalid configuration method: "string"

Cause: An unknown type was specified for the method used to store configuration information.

Action: Specify a valid type.

CLSGN-00044: no file name specified.

Cause: No name was specified for a configuration method which uses a file as the repository.

Action: Specify a file name.

CLSGN-00045: initialization failed: string

Cause: The initialization of GNS failed.

Action: Please examine the accompanying message for the exact reason.

CLSGN-00046: no value found for parameter "string".

Cause: A value was not specified for the parameter.

Action: Specify a parameter.

CLSGN-00047: multiple values found for parameter "string".

Cause: Multiple values were specified for a parameter.

Action: Specify a single value.

CLSGN-00048: type mismatch "string". Expected: string Actual: string.

Cause: The type of the value specified for a parameter does not match the required type.

Action: Change the type of the parameter.

CLSGN-00049: unknown parameter: "string".

Cause: The specified parameter is not supported.

Action: Specify a supported parameter.

CLSGN-00050: failure to convert parameter value "string" to "string".

Cause: The attempt to convert the string value for a parameter failed.

Action: Specify a value of the correct type.

CLSGN-00051: unsupported query type: "string"

Cause: The query type passed in is not supported by GNS.

Action: Specify a supported query type.

CLSGN-00052: Initialization of OCR at level number failed. string

Cause: Initialization of OCR to the specified level failed.

Action: Examine the error message to determine what occurred.

CLSGN-00054: Invalid IP address: string

Cause: The IP address specified is neither in the v4 or v6 format.

Action: Specify a correct address.

CLSGN-00056: Unable to resolve host name "string"

Cause: No entry was found in GNS or the system for the specified host.

Action: Specify a valid machine.

CLSGN-00057: Invalid process type specified.

Cause: The caller specified a process type which is not known.

Action: Specify a valid type.

CLSGN-00058: Invalid number of arguments specified: number.

Cause: The client program sent the wrong number of arguments over for a command.

Action: This error should not ordinarily be seen. Contact Oracle Customer Support.

CLSGN-00059: Unknown command: number.

Cause: The server received an unknown command from the client.

Action: This error should never happen. If it does, contact Oracle Customer Support.

CLSGN-00060: Conversion of string value "string" failed with error number.

Cause: The value of a parameter sent over from the client to number failed.

Action: Specify a valid parameter value.

CLSGN-00061: Internal error.

Cause: An unexpected error occurred. The rest of the error stack contains details about the error.

Action: This error should never happen. If it does, contact Oracle Customer Support.

CLSGN-00062: Server spawn failed: could not access subdirectory string under string.

Cause: The server process could not be spawned because the directory where the program resides could not be located or accessed.

Action: Make sure that the server directory exists and can be accessed by the user starting the program.

CLSGN-00063: Server spawn failed: executable not accessible: directory: string file: string

Cause: The server program could not be accessed.

Action: Make sure the server executable exists and can be accessed by the user starting the program.

CLSGN-00064: spawn of server string failed.

Cause: The client was unable to start the server process.

Action: More details about the failure can be found in messages that follow.

CLSGN-00065: Unable to create backup for configuration file string

Cause: The GNS server was unable to create a backup configuration file.

Action: Check the permissions in the configuration directory. Make sure that the GNS process is permitted to create files there.

CLSGN-00066: Service advertisement initialization failed.

Cause: GNS failed when tried to initialize the Resource Discovery subsystem.

Action: Examine the message following this one. It will indicate the cause. If it is a number, consult rdret.h.

CLSGN-00067: Service advertisement termination failed.

Cause: GNS failed while trying to shut down the Resource Discovery subsystem.

Action: Examine the message following this one. It will indicate the cause. If it is a number, consult rdret.h.

CLSGN-00068: Service advertisement stop failed.

Cause: GNS encountered an error when it tried to stop the advertisement of its service.

Action: Examine the message following this one. It will indicate the cause. If it is a number, consult rdret.h.

CLSGN-00069: Service registration failed.

Cause: GNS was unable to register itself with Resource Discovery.

Action: Examine the message following this one. It will indicate the cause. If it is a number, consult rdret.h.

CLSGN-00070: Service location failed.

Cause:. If it is a number, consult rdret.h. Also, make sure that the server process has been started.

Action: Examine the message following this one for a possible

CLSGN-00071: Transport initialization failed.

Cause: GNS was unable to initialize the transport that it was used to communicate between the client and server.

Action: The message following indicates the exact error that occurred.

CLSGN-00072: Connection to server failed.

Cause: GNS was unable to initialize the transport that it was used to communicate between the client and server.

Action: The message following indicates the exact error that occurred.

CLSGN-00073: Send failed

Cause: GNS was unable to send data either from the client to the server or from the server to the client.

Action: The message following indicates the exact error that occurred.

CLSGN-00074: Wait for client connection failed

Cause: An error occurred while the server was waiting for a connection from the client.

Action: The message following indicates the exact error that occurred.

CLSGN-00075: Receive failed.

Cause: GNS was unable to receive data from its peer process.

Action: The message following indicates the exact error that occurred.

CLSGN-00076: string Packet ignored: string.

Cause: The packet was ignored by the server because it was invalid. This may be caused by another process sending malformed packets.

Action: Use system tools to determine if a non-GNS process is sending data to the server.

CLSGN-00077: Invalid DNS message received.

Cause: The GNS server received a message from the master DNS server which was not of the correct format. This could be due to an error by the server or because a malicious process is sending the GNS server invalid packets.

Action: The error is informational and should not ordinarily be visible to a user. If it is seen, contact Oracle Customer Support.

CLSGN-00078: No space in packet buffer. Length: number. Remaining: number

Cause: The GNS server was unable to add data to the packet that it was going to send to the DNS server because an internal buffer ran out of room.

Action: This error should ordinarily not be visible to users. If it appears, contact Oracle Customer Support.

CLSGN-00079: Bonjour initialization failed.

Cause: The function called to initialize Bonjour for use by GNS failed.

Action: Examine the accompanying Bonjour error and take corrective action.

CLSGN-00080: Wait for a DNS server request failed.

Cause: The GNS server attempted to wait for a request to arrive from the DNS server.

Action: This error should ordinarily not be visible to users. If it appears, contact Oracle Customer Support.

CLSGN-00081: The GNS service is not running.

Cause: The GNS service could not be contacted because it is not running.

Action: Start the GNS service.

CLSGN-00082: The GNS service is already running.

Cause: An attempt was made to start the GNS service, but it was already running.

Action: Shut down the GNS service before trying to start it.

CLSGN-00083: Invalid option: "string"

Cause: An unknown option was specified either to a client program or the server.

Action: Specify a supported option.

CLSGN-00084: Invalid trace level: "string"

Cause: The value specified for the trace level was not a number.

Action: Specify a number for the trace level.

CLSGN-00085: An argument must be specified for the "string" option.

Cause: An argument was not specified for the specified option.

Action: Provide an argument for the option.

CLSGN-00086: Service location initialization failed.

Cause: The GNS client failed when it tried to initialize the Resource Discovery subsystem.

Action: Examine the message following this one. It will indicate the cause. If it is a number, consult rdret.h.

CLSGN-00087: Listen on endpoint "string" failed.

Cause: The server was unable to listen for requests on the specified endpoint.

Action: The accompanying GIPC error should be examined for the exact error.

CLSGN-00088: Listen on string port number failed due to a lack of privileges.

Cause: The server was unable to listen on the specified port because it does not have privilege to do so. On Linux and Unix systems, this can occur because the server is not running as the root user.

Action: Run the server as a user with the needed privileges.

CLSGN-00089: Not enough arguments specified for the "string" option. Number specified: number. Minimum number: number.

Cause: Enough arguments were not specified for a command.

Action: Specify the minimum number of arguments.

CLSGN-00090: Too many arguments specified for the "string" option. Number specified: number Maximum number: number.

Cause: Too many arguments arguments specified for a command.

Action: Specify the required number of arguments.

CLSGN-00093: Server failed during start up.

Cause: The GNS server started but later terminated unexpectedly.

Action: Examine the trace and log files for the reason.

CLSGN-00094: DNS service query failed: string.

Cause: The name resolution component was unable to start a query for names of hosts in the cluster.

Action: The following error will detail exactly what occurred. Also, examine the log files for other information.

CLSGN-00095: Invalid IP address for name "string": "string"

Cause: An attempt was made to register an IP address which was in the incorrect format.

Action: Change the address to be in the correct format.

CLSGN-00096: Connection to the mDNS server failed: string.

Cause: An attempt to perform an operation on an address failed because it was not possible to connect to the mDNS server.

Action: Ensure that the server is up and try the operation again.

CLSGN-00097: Advertisement of "string" failed.

Cause: An attempt to advertise an address or create an alias failed.

Action: Examine the accompanying message for more details as to the reason.

CLSGN-00098: Name already exists.

Cause: An attempt to advertise an address or create an alias failed because the name already exists.

Action: Either delete the record and use a different name.

CLSGN-00099: Multicast DNS server not running.

Cause: GNS was unable to send a query to the multicast DNS server because it is not running.

Action: Start the multicast DNS server.

CLSGN-00100: The alias "string" already exists.

Cause: The specified alias already exists.

Action: Specify an alias which does not exist.

CLSGN-00101: The alias "string" does not exist.

Cause: An alias for a host could not be found.

Action: Specify an alias which exists.

CLSGN-00102: The host name "string" does not exist.

Cause: A host with the specified name could not be found.

Action: Specify a host name which exists.

CLSGN-00105: Server terminated with error.

Cause: GNS terminated with an unexpected error.

Action: See the accompanying exception stack for more information.

CLSGN-00106: Getting information about interfaces failed.

Cause: GNS did not have the privilege to obtain information about the interfaces available on the host.

Action: Consult the documentation about the operating system to determine the privileges needed.

CLSGN-00107: Getting information about interface "string" failed.

Cause: GNS did not have the privilege to obtain information about the given interface.

Action: Consult the documentation about the operating system to determine the privileges needed.

CLSGN-00109: No interfaces available.

Cause: GNS was unable to find any interfaces on which it can listen for requests. This error is likely caused by the incorrect specification of the list of interfaces on which GNS is not to listen. Alternatively, it may be caused by an error in system configuration.

Action: Correct the list of prohibited interfaces if it was set incorrectly. If this is not the case, check the system configuration.

CLSGN-00110: One or threads failed - check log.

Cause: One or more GNS failed unexpectedly.

Action: Check the log file to determine the exact reasons.

CLSGN-00111: Acquisition of privileges needed to perform operation failed.

Cause: An attempt to acquire the privileges needed failed.

Action: Examine the attached message for more details.

CLSGN-00112: Platform initialization failed.

Cause: GNS was unable to initialize the layer the provides system-specific services.

Action: Examine the accompanying message for details.

CLSGN-00115: Authentication failed due to network failure.

Cause: The authentication of the client to the server failed due to a failure in sending or receiving authentication data.

Action: Examine the log or trace files to determine the exact error.

CLSGN-00116: Authentication operation timed out

Cause: The authentication of the client to the server failed because one of the processes did not send its data in time.

Action: The accompanying reason has details about the reason.

CLSGN-00117: Authentication protocol failure.

Cause: The client program did not send to the server the data in the format that it was expecting.

Action: Try the connection again using an Oracle-approved client.

CLSGN-00118: Client was rejected: string.

Cause: The client was not allowed to connect to the GNS server.

Action: Examine the trace and log files for the specific reason.

CLSGN-00120: Creation of configuration file "string" failed.

Cause: The creation of the new version of the configuration file failed.

Action: Examine the rest of the error stack for the exact reason.

CLSGN-00121: Trace level set to number.

Cause: This is an information message to indicate that the trace level was set.

Action: No action is needed.

CLSGN-00122: Dynamic messaging initalization failed - error number

Cause: The facility used to control the GNS server dynamically failed.

Action: This error should not be seen in normal use. Contact Oracle Customer Support if it appears.

CLSGN-00127: Privileged user "string" does not exist.

Cause: The user which GNS is to run as in order to run operations which require special privileges does not exist.

Action: Specify a user which does exist on the host. This user must have the ability to listen for requests from the DNS server.

CLSGN-00128: Unprivileged user "string" does not exist.

Cause: The user which GNS is to run as in order to perform operations which do not require special privileges does not exist.

Action: Specify a user which exists.

CLSGN-00129: Privileged group "string" does not exist.

Cause: The group to which a user must belong in order to perform administrative operations does not exist.

Action: Specify a group which exists on the host.

CLSGN-00130: no privileges to access OCR key "string".

Cause: It was not possible to retrieve the specified key from OCR because the user does not have the required privileges.

Action: Either run the command as a user which has the required privileges or configure OCR to allow retrieval of the key.

CLSGN-00131: no privileges to get value for OCR key "string".

Cause: It was not possible to retrieve the specified value from OCR because the user does not have the required privileges.

Action: Either run the command as a user which has the required privileges or configure OCR to allow retrieval of the key.

CLSGN-00132: user "string" not authorized to run command.

Cause: A user tried to run a command but has no permission to do so.

Action: Run the command as a user which has the proper privileges.

CLSGN-00133: Exception received: string

Cause: An exception occurred on the server process.

Action: Examine the exception for details.

CLSGN-00134: Invalid host name: "string".

Cause: The name of the host to be used for a GNS operation was not valid. The name may have no domain or be qualified with the name of subdomain serviced by GNS.

Action: Specify a correct host name.

CLSGN-00135: Mandatory parameter "string" is not configured.

Cause: A value was not configured for a mandatory parameter.

Action: Configure a value in the parameter repository.

CLSGN-00136: Query for a host address failed.

Cause: An address was not found for the specified host.

CLSGN-00138: No thread names specified.

Cause: The command requires at least one thread name to be specified.

Action: Specify at least one thread name.

CLSGN-00139: Invalid thread name "string"

Cause: The name of the thread was unknown to GNS.

Action: Specify a valid thread name.

CLSGN-00140: OCR key "string" does not exist.

Cause: The specified key cannot be found in the Oracle Cluster Registry.

Action: Specify a key that exists This exception often happens when trying to retrieve a configuration parameter.

CLSGN-00141: The address "string" already exists.

Cause: A mapping for a address to a host already exists.

Action: Specify an address which does not exist.

CLSGN-00142: Open of OCR key "string" failed.

Cause: An error occurred while trying to open the root OCR used by GNS.

Action: Examine the accompanying exceptions for more information about the error. This error may be caused by mis-configuration.

CLSGN-00143: Subdomain "string" already exists.

Cause: An attempt was made to create a GNS subdomain which already exists.

Action: Specify a subdomain which does not exist.

CLSGN-00144: Subdomain "string" does not exist.

Cause: The specified GNS subdomain does not exist.

Action: Specify a subdomain which exists.

CLSGN-00145: The host "string" already exists.

Cause: The specified host already exists.

Action: Specify an host which does not exist.

CLSGN-00146: Address "string" for name "string" does not exist.

Cause: The specified host address does not exist.

Action: Specify a host address which exists.

CLSGN-00147: Address "string" for name "string" is not serviced by GNS.

Cause: The specified address is not served by GNS.

Action: Specify a different address or change the subnet mask used by GNS.

CLSGN-00149: Host address "string" does not exist.

Cause: The specified address is not known to GNS.

Action: Specify a valid address.

CLSGN-00150: Alias "string" is invalid.

Cause: The name of the alias to be advertised was not valid. The name may have no domain or be qualified with the name of subdomain serviced by GNS.

Action: Specify a correct alias.

CLSGN-00151: Host domain "string" does not match GNS subdomain "string"

Cause: The domain specified for the host does not specify the subdomain served by GNS.

Action: Either specify the correct domain or just specify the name of the houst.

CLSGN-00152: Self-check failed.

Cause: The self-check performed by GNS at initialization time failed.

Action: Check the accompanying exceptions and the log and trace files for details as to why it failed. Also verify that DNS has been configured so that it contains a "forwarders" clause which contains the domain used by GNS and the IP address on which the GNS server is listening.

CLSGN-00153: Length of subdomain "string": string exceeds the maximum: string.

Cause: The name specified for the subdomain to be served by GNS is longer than the maximum.

Action: Specify a shorter subdomain name.

CLSGN-00154: Invalid subdomain: "string"

Cause: The name of the subdomain does not conform to Internet standards. It must meet the following requirments:

1\. Only alphanumeric characters, periods are hyphens are allowed;

2\. It must start and end with an alphanumeric character;

3\. Consecutive periods are not allowed. In addition, the subdomain must not end with with ".local" as it is reserved for multicast DNS.

Action: Specify a subdomain in the correct format.

CLSGN-00155: trace level number is less than the minimum number - ignoring.

Cause: The trace level specified is lower than the minimum supported.

Action: Specify a valid trace level.

CLSGN-00156: trace level number is greater than the maximum number. Using the maximum value instead.

Cause: The trace level specified is greater than the maximum supported.

Action: Specify a valid trace level.

CLSGN-00158: Initialization or shut down in progress.

Cause: GNS was unable to process a command because it is either starting up or shutting down.

Action: If the server is starting up, try the command again in a few seconds. The server is shutting down, try the command again after the server has restarted.

CLSGN-00161: Failed to set GNS trace level: string.

Cause: The call to set the trace level on the GNS server failed.

Action: Examine the accompanying error message for details.

CLSGN-00162: Name "string" and address "string" will not be advertised due to configuration change.

Cause: When GNS attempted to advertise a name and address upon re-start, it failed because the address can no longer be serviced. This can happen if the subnet used by GNS was changed between the time that GNS was stopped and it was started.

Action: If this result was expected, the error can be ignored. Otherwise, the subnet needs to be changed in OCR and GNS needs to be stopped and re-started.

CLSGN-00163: connection with Cluster Synchronization Services failed. Error: number.

Cause: GNS was unable to contact Cluster Synchronization Services in order to retrieve the name of the cluster.

Action: This error is most probably caused by the Cluster Synchronization Services daemon being down. If the daemon is running, contact Oracle Customer Support and provide them with the error code.

CLSGN-00164: Failed to retrieve cluster name: Error: number.

Cause: GNS was unable to get the name of the cluster from Cluster Synchronization Services.

Action: This error is most probably caused by the Cluster Synchronization Services daemon being down. If the daemon is running, contact Oracle Customer Support and provide them with the error code.

CLSGN-00165: Running as user "string" which is not privileged.

Cause: GNS is not running as a privileged user e.g. root.

Action: Start GNS as a privileged user.

CLSGN-00166: Creation of OCR key "string" failed. string

Cause: GNS was unable to create the specified OCR key.

Action: Examine the accompanying error for details about what occurred. This error may be caused by mis-configuration.

CLSGN-00167: Operation is unsupported.

Cause: An operation was attempted which is not currently supported by GNS.

Action: Do not attempt the operation.

CLSGN-00168: Name advertisement or alias re-creation failed.

Cause: When GNS starts, it re-creates the advertisements and aliases that existed when it was shut down. The attempt to re-create an advertisement or alias failed.

Action: This error should not occur in normal use. Contact Oracle Customer Support.

CLSGN-00169: Spawn of thread "string" failed.

Cause: GNS was unable to spawn a thread. This may be due to low system resources.

Action: If the memory or processes in use on the system are too high, reduce one or both and restart GNS. If this is not the case, contact Oracle Customer Support.

CLSGN-00170: Thread "string" failed on startup.

Cause: A GNS thread failed when it tried to start.

Action: Examine the alert log and and trace file (if any) for details about the error.

CLSGN-00171: Invalid alias "string" specified for name "string"

Cause: The name of the alias to be advertised was not valid. The name must have no domain or be qualified with the name of subdomain serviced by GNS.

Action: Specify an alias whose name is in the correct format.

CLSGN-00172: Domain given in alias "string" for name "string" does not match GNS domain "string".

Cause: The domain specified for an alias does not match the domain serviced by GNS.

Action: Either specify the correct domain or do not specify a domain and GNS will use its domain as the default.

CLSGN-00173: GNS has not been configured.

Cause: An operation on GNS failed because GNS has not configured.

Action: Configure GNS and retry the operation.

CLSGN-00174: Packet replay detected - dropping connection.

Cause: GNS received a duplicate packet from a client. The connection was dropped as a consequence.

Action: Examine the trace file for details. It is possible that a malicious user is attempting to send an invalid packet to GNS.

CLSGN-00175: Invalid packet received - dropping connection.

Cause: The packet was ignored by the server because it was invalid. This may be caused by another process sending malformed packets. This error is usually accompanied by another error which describes the exact error that occurred.

Action: Use system tools to determine if a non-GNS process is sending data to the server.

CLSGN-00176: Packet security check failed.

Cause: The check of the security attributes of a packet failed.

Action: Check the trace file for details about the failure. It is possible that a malicious user is attempting to send an invalid packet to GNS.

CLSGN-00177: Invalid packet type received.

Cause: GNS received a packet whose type is unknown.

Action: Check the trace file for details about the failure. It is possible that a malicious user is attempting to send an invalid packet to GNS.

CLSGN-00178: Resolution of name "string" failed.

Cause: GNS failed to retrieve the address of the specified name.

Action: Check to make sure that an address for the name has been registered with GNS. If it is configured, check to make sure that DNS has been properly configured.

CLSGN-00179: No forwarded query received from DNS for name in "string" domain, check DNS configuration

Cause: A query was not forwarded from DNS to GNS for a name in the subdomain that it services.

Action: Check the configuration of DNS. Make sure that it contains the required forwarding directive contained in the following message.

CLSGN-00180: If BIND is being used and the zone is being forwarded, the entry will likely look like the following:

Cause: This message is displayed when the GNS self-check fails.

Action: Ensure that the configuration of DNS has the entry listed in the message that follows this one.

CLSGN-00182: string Unable to resolve self-check name.

Cause: This is an informational message which accompanies other messages describing a self-check failure.

Action: Examine the accompanying error messages for more information as to the cause of the problem.

CLSGN-00183: Number of retries exceeded maximum: number.

Cause: An operation failed after the maximum number of retries.

Action: Examine the accompanying message(s) for the reasons to why this error occurred.

CLSGN-00184: Operation has to be retried.

Cause: An operation failed because it could not be performed at this time and should be tried again later\`.

Action: Examine the accompanying message(s) for details about the operation that was performed.

CLSGN-00185: Invalid argument.

Cause: An argument was passed to a function which was incorrect. In the case of a string, for example, a string will be invalid if it is null or has a zero length.

Action: Supply a valid argument.

CLSGN-00186: Insufficient privileges.

Cause: The user attempted an operation for which he or she does not have sufficient privileges.

Action: Either have the system administrator grant the needed privileges or re-try the operation as a user which has the needed privileges.

CLSGN-00187: Listening address "string" is not on the public network.

Cause: The address specified as the address on which GNS is to listen is not on the public network.

Action: Specify a different address which is on the public network.

CLSGN-00188: The value for parameter "string": number may only be from number to number.

Cause: The value for a parameter is outside the range of permitted values.

Action: Specify a value within the range.

CLSGN-00190: No records found for "string".

Cause: No records could be found for the specified name in GNS.

Action: Specify a name which exists in GNS.

CLSGN-00191: No records registered.

Cause: A query was made for the names registered in GNS but none were found.

Action: Re-run the query after names have been advertised.

CLSGN-00192: string Open of OCR key "string" failed. string

Cause: GNS was unable to open the specified OCR key.

Action: Examine the accompanying error for details about what occurred.

CLSGN-00193: Deletion of OCR key "string" failed. string

Cause: GNS was unable to delete the specified OCR key.

Action: Examine the accompanying error for details about what occurred.

CLSGN-00194: Time needed for resolution of name "string": string ms exceeded threshold of string ms

Cause: Name resolution took longer than the expected time.

Action: This may indicate a problem in the network or DNS configuration and should be investigated by each administrator.

CLSGN-00196: Self-check succeeded after previous failure.

Cause: This is an informational message which indicates that the self-check succeeded after having failed previously.

Action: No action required.

CLSGN-00197: string Self-check failed due to failure in name resolution.

Cause: The self-check failed because it was not possible to resolve the self-check name into the address used for reference.

Action: Examine the errors that follow the message for further information as to the cause.

CLSGN-00201: string first self-check name resolution failed.

Cause: GNS was unable to resolve the name that it uses for the self-check the first time after it started.

Action: Examine the logs for more information about the error.

CLSGN-00202: string first self-check failed.

Cause: GNS was unable run the self-check the first time after it started.

Action: Examine the logs for more information about the error.

CLSGN-00205: string self-check failed while in "recovery" state.

Cause: The self-check had previously succeeded after a failure but has failed again.

Action: Examine the logs for more information about the failure.

CLSGN-00206: Creation of a network endpoint failed.

Cause: The creation of a listening endpoint failed.

Action: Examine the accompanying error stack for more information about the error.

CLSGN-00207: Creation of a network endpoint failed due to lack of permissions.

Cause: The creation of a listening endpoint failed because the server did not have the needed permissions.

Action: Examine the accompanying error stack for more information about the error.

CLSGN-00208: Network endpoint "string" already in use.

Cause: The creation of an endpoint failed because another process is using it.

Action: If another GNS instance is running, this error is expected. Otherwise, terminate the process using the address or start GNS on another node.

CLSGN-00209: Listen for DNS requests failed. IP address string port number is in use.

Cause: Listening for requests from the DNS server(s) failed because another process is using the address.

Action: If another GNS instance is running, this error is expected. Otherwise, terminate the process using the address or start GNS on another node.

CLSGN-00210: failed to get value for OCR key "string". string

Cause: It was not possible to retrieve the specified value from OCR.

Action: Examine the accompanying error stack for more information about the error.

CLSGN-00211: OCR batch operation failed. string

Cause: Setting a set of Oracle Cluster Registry (OCR) key values failed.

Action: Examine the accompanying error messages for more information about the error.

CLSGN-32767: Internal error.

Cause: An unexpected error occurred.

Action: Examine the message(s) that accompany this one for details about the error and contact Oracle Customer Support.