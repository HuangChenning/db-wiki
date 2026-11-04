---
title: PRKO-00371 to PRKO-09068
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prkomsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 76 PRKO-00371 to PRKO-09068

PRKO-00371: No option specified for "modify gns"

Cause: No option was specified for the "modify gns" command.

Action: Specify at least one option.

PRKO-00372: The "-{0}" option requires the specification of the "-{1}" option.

Cause: An option was specified which requires that another option to be specified at the same time.

Action: Specify the required option.

PRKO-00373: Invalid host name or address: "{0}".

Cause: The host name or address specified for the address on which GNS is to listen was not valid.

Action: Specify a valid host name or IP address. If an IP address is used, it must be one of the following:

1\. A valid IPv4 address (N.N.N.N);

2\. A valid IPv6 address (N\[:N\]\*).

PRKO-00374: The "-{0}" option may not be used with the "-{1}" option.

Cause: The two options may not be used together.

Action: Run srvctl with each option specified separately.

PRKO-00375: No option was specified for the GNS "modify" command.

Cause: An option was not specified for the modify command.

Action: Specify an option.

PRKO-00376: ASM not stopped: deprecated option '-i' is not allowed.

Cause: An attempt to stop ASM using srvctl specified the '-i' option.

Action: Use the '-n' option to specify the node where ASM instance should be stopped.

PRKO-00377: The "-{0}" option requires the specification of either the "-{1}" or the "-{2}" option.

Cause: An option was specified which requires that one of the other possible options to be specified at the same time.

Action: Specify the one of the other options.

PRKO-00378: Both "-{0}" and "-{1}" options may not be specified with the "-{2}" option.

Cause: An invalid combination of options was specified.

Action: Specify only one of the other possible options.

PRKO-00380: No other option is allowed when the "-l" option is specified.

Cause: If the "-l" option is specified, no other option may be given.

Action: Only specify the "-l" option.

PRKO-00381: Both "-g" and "-x" options are required to set server pool {0} for single instance database {1} on the cluster.

Cause: Option "-x" is not specified in 'srvctl modify database' command for a single instance database on the cluster.

Action: Specify both -g and -x options in 'srvctl modify database' and retry.

PRKO-00382: The number of candidate servers {0} in server pool {1} should be one for single instance database {2}

Cause: The server pool specified in 'srvctl modify database' command for a single instance database contains more than 1 candidate servers.

Action: Either modify the given server pool via 'srvctl modify srvpool' command to have only one candidate server specified via -x argument or specify another server pool that contains only one candidate server specified via -x argument.

PRKO-02000: Invalid command line syntax for a single instance database

Cause: user specified invalid command line syntax.

Action: Look at the usage provided for this command and specify all mandatory options.

PRKO-02001: Invalid command line syntax

Cause: The syntax of the command is incorrect.

Action: Look at the usage provided for this command and use the correct syntax.

PRKO-02002: Invalid command line option:

Cause: Invalid command line option was specified.

Action: Check the value printed along with the exception and specify the correct value.

PRKO-02003: Invalid command line option value:

Cause: Invalid command line option was specified.

Action: Check the value printed along with the exception and specify the correct value.

PRKO-02004: Repetition of command line option:

Cause: The command line option printed along with the exception was repeated.

Action: Delete the repeated command line option and try the command again.

PRKO-02005: Failure in getting Cluster Database Configuration for:

Cause: The specified database does not exist.

Action: Check the specified database name and try again.

PRKO-02006: Invalid node name: {0}

Cause: Unable to get the hostname for the given node/machine name.

Action: Check the node name and try again.

PRKO-02007: Invalid instance name: {0}

Cause: Unable to obtain the node name on which the instance name specified was running.

Action: Check the instance name specified and try again.

PRKO-02008: Invalid connect string:

Cause: The connect string specified was not in the format username/password \[as {SYSDBA|SYSOPER}\]

Action: Check the connect string and try again.

PRKO-02009: Invalid name/value string: {0}

Cause: The name value string should be of the form name = value

Action: check the input name/value pair and try again.

PRKO-02010: Invalid command specified on command line: {0}

Cause: The \<command> specified on the command line was not recognized.

Action: Valid commands are enable|disable|start|stop|relocate|status|add|remove|modify|getenv|setenv|unsetenv|config. Usage of srvctl is printed with this errori. Check the usage and specify a valid command.

PRKO-02011: Invalid object specified on command line: {0}

Cause: The \<object> specified on the command line was not recognized.

Action: Valid objects are database|instance|service|nodeapps|vip|network|asm|diskgroup|listener|srvpool|scan|scan\_listener|oc4j|home|filesystem|gns|cvu. Srvctl usage is printed along with this exception. Check the usage printed with this error and use a valid object.

PRKO-02012: {0} object is not supported in Oracle Restart

Cause: The \<object> specified on the command line was not a valid object for the Oracle Restart mode.

Action: Valid objects for Oracle Restart mode are database|service|asm|diskgroup|listener|home|ons. Srvctl usage is printed along with this exception. Check the usage printed with this error and use a valid object.

PRKO-02013: {0} object is not supported in Oracle Clusterware

Cause: The \<object> specified on the command line was not a valid object for the Oracle Clusterware mode.

Action: Valid objects for Oracle Clusterware are database|instance|service|nodeapps|vip|network|asm|diskgroup|listener| srvpool|scan|scan\_listener|oc4j|home|filesystem|gns|cvu. Srvctl usage is printed along with this exception. Check the usage printed with this error and use a valid object.

PRKO-02014: The -a option should be specified with -d <dbunique\_name> for 'srvctl config database' command

Cause: -a option was specified without the required -d option specifying for which database to retrieve configuration.

Action: To retrieve the full configuration of the database, specify both -d and -a option with the 'srvctl config database' command.

PRKO-02016: Database {0} has no services configured

Cause: 'srvctl config database' request found no services configured for the database.

Action: Use 'srvctl add service' command to configure services for the database and then retry.

PRKO-02017: Service {0} does not exist for database {1}.

Cause: The service being updated is not defined for the given database.

Action: If the service needs to be added don't use '-u' option in 'srvctl modify service' command. Option '-u' is for updating existing services.

PRKO-02018: No databases are configured

Cause: No databases were configured.

Action: Use 'srvctl add database' command to configure databases.

PRKO-02049: Invalid name-value string: {0}

Cause: The name=value string specified is not in valid format.

Action: The format for the string should be name=value. Check input and correct the error.

PRKO-02050: Error in enabling ASM instance on node {0}. {1}

Cause: ASM could not be enabled.

Action: Make sure that the node name is correct and that ASM exists on the specified node and it is not already enabled on the node. The current state of the ASM can be found using 'srvctl status asm' command. To check if ASM is configured or not, use 'srvctl config asm' command.

PRKO-02053: Error in disabling ASM instance on node {0}. {1}

Cause: ASM could not be disabled.

Action: Make sure that the node name is correct and that ASM exists on the specified node and it is not already disabled on the node. The current state of the ASM can be found using 'srvctl status asm' command. To check if ASM is configured or not, use 'srvctl config asm' command.

PRKO-02054: Invalid command line syntax, mandatory options are either {0} or {1}, but not both.

Cause: The command requires exactly one set of mandatory command line options. But either some options in one set were missing or the options from both sets were specified.

Action: Check the command line options entered and make sure that all the mandatory options in one set are specified.

PRKO-02056: Error occured while checking dependent resources on network {0}. Network was not removed.

Cause: An attempt made to check if any resources are dependent on the given network failed.

Action: Make sure that the network is up. Make sure that the user has sufficient permission to remove network. If force flag was not specified in the remove command then specify force flag and try the command again.

PRKO-02058: Scan name {0} cannot be the same as a cluster node name: {1}

Cause: Scan name is same as a cluster node name.

Action: Choose a different scan name and issue the command.

PRKO-02065: Only one server pool should be provided for a single instance database on a cluster

Cause: An attempt to create a single instance database failed because more than one server pool was specified.

Action: Provide only one server pool while creating the single instance database.

PRKO-02067: The size of server pool should be one for single instance database

Cause: An attempt to create a single instance database failed because a server pool with more than one server was specified.

Action: Provide a server pool with only one server while creating a single instance database.

PRKO-02069: OC4J could not be created as it already exists

Cause: A new OC4J instance could not be created, as there is an existing instance of OC4J.

Action: Only one instance of OC4J can exists at any given time.

PRKO-02070: OC4J creation failed

Cause: A new OC4J instance could not be added because of OC4J exception.

Action: Resolve the OC4J exception and then try the OC4J addition again.

PRKO-02072: OC4J is not configured

Cause: OC4J is not configured on the cluster.

Action: Check the exception printed with this message. If OC4J is not configured then OC4J instance can be created using 'srvctl add oc4j'. If there are other errors shown with this error then check the cause/action messages of underlying exception.

PRKO-02074: OC4J is still running. It must be stopped before removing.

Cause: 'srvctl remove oc4j' was issued while OC4J instance was running.

Action: Stop the oc4j instance using 'srvctl stop oc4j' and then try removing.

PRKO-02075: OC4J could not be removed

Cause: OC4J instance could not be removed because it does not exist.

Action: The current OC4J configuration can be checked using 'srvctl config oc4j' command. Make sure that OC4J instance is running on that port. If their are other underlying messages printed then check the cause/action for the underlying errors shown with this.

PRKO-02077: OC4J RMI port could not be modified

Cause: OC4J RMI port could not be modified.

Action: Make sure that OC4J instance exists and port is not in use by using the command 'srvctl config oc4j' and try again.

PRKO-02079: OC4J could not be started

Cause: The start of OC4J instance failed.

Action: Make sure that OC4J instance exists and is not already started.

PRKO-02081: OC4J failed to stop

Cause: The OC4J instance could not be stopped.

Action: Make sure that OC4J instance exists and are not already stopped.

PRKO-02082: Missing mandatory option {0}

Cause: The specified mandatory command option is missing.

Action: Use srvctl with the -h option to display option details for the command and make sure that all the mandatory options are specified.

PRKO-02087: OC4J could not be enabled

Cause: OC4J instance could not be enabled.

Action: Make sure that node name is correct and that OC4J instance exists and is not already enabled. The current state of the OC4J instance can be found using 'srvctl status oc4j' command. To check if OC4J instance is configured or not use 'srvctl config oc4j' command.

PRKO-02090: OC4J could not be disabled

Cause: OC4J instance could not be disabled.

Action: Make sure that Node name is correct and that OC4J instance exists and is not already disabled. The current state of the OC4J instance can be found using the srvtl status oc4j command. To check if OC4J instance is configured or not use 'srvctl config oc4j' command.

PRKO-02093: OC4J could not be relocated

Cause: OC4J instance could not be relocated to given node.

Action: If the node name was passed in the command line make sure that the node name is valid. Also make sure that 0C4J instance exists on the cluster and is running.

PRKO-02100: Cannot update service {0} because {1} is not administrator-managed

Cause: An attempt to update the service using "-u" option failed because this option can be used with administrator-managed databases only.

Action: Make sure that you provide correct options for 'srvctl add service' command.

PRKO-02102: Failed to create server pool {0}: {1}

Cause: An attempt to create the specified server pool failed because of the reason provided by the accompanying error.

Action: Examine the accompanying error messages for details.

PRKO-02103: The '-a' and '-r' options cannot both be supplied with '-u'

Cause: Command 'srvctl add service' with '-u' option failed because both options '-a' and '-r' were provided.

Action: Correct options and issue command again.

PRKO-02104: Option '-a' or '-r' should be supplied with '-u'

Cause: Command 'srvctl add service' with option '-u' failed because both it requires options '-a' or '-r' to be provided.

Action: Correct options and issue command again.

PRKO-02105: Option '-g' cannot be used with option '-r','-a' or '-P'

Cause: Incorrect usage of -g option.

Action: Correct options and issue command again.

PRKO-02106: There is no server pool associated with database {0}

Cause: Command 'srvctl add service' failed because the given database doesn't have an associated server pool.

Action: Oracle internal error. Contact customer support.

PRKO-02108: Command line options '-i' and '-n' cannot be used at the same time

Cause: Incorrect usage of -i and -n options.

Action: Correct options and issue command again.

PRKO-02109: Options '-e', '-i', or '-w' should be supplied with option '-c'

Cause: Incorrect usage of -e, -i and -w options.

Action: Correct options and issue command again.

PRKO-02110: Option '-c' cannot be used to create services with administrator-managed database {0}

Cause: Incorrect usage of -c option.

Action: Remove -c option and issue command again.

PRKO-02111: Invalid number {0} for command line option {1}

Cause: Invalid value was specified for the command line option that requires a number in a certain range.

Action: Check the value printed and specify a number within the required range.

PRKO-02112: Options '-x' and '-y' cannot be used to create RAC One Node database {0}

Cause: Incorrect usage of -x and -y options.

Action: Remove -x and -y options and issue command again.

PRKO-02115: OC4J is already disabled

Cause: OC4J instance could not be disabled because it is already disabled.

Action: If this is the expected state then this is not an error. If it is not then enable OC4J instance by using the 'srvctl enable oc4j' command.

PRKO-02116: OC4J is already enabled

Cause: OC4J instance could not be enabled because it is already enabled.

Action: If this is the expected state then this is not an error. If it is not then disable OC4J instance by using the 'srvctl disable oc4j' command.

PRKO-02117: Options '-g' and '-e' cannot be used together

Cause: Options -g and -e were used incorrectly.

Action: Correct options and issue command again.

PRKO-02118: Options '-g' and '-i' cannot be used together

Cause: Incorrect usage of -g and -i options.

Action: Correct options and issue command again.

PRKO-02119: Only one server pool can be specified with the -g option for a RAC One Node database

Cause: Incorrect number of serverpools was supplied with the -g option.

Action: Specify one server pool with the -g option and issue command again.

PRKO-02120: Options '-x' and '-y' cannot be used to modify RAC One Node database

Cause: Options -x and -y were used incorrectly.

Action: Remove -x and -y options and issue command again.

PRKO-02121: Options '-e' and '-w' cannot be used to modify a database that is not RAC One Node

Cause: Options -e and -w were used incorrectly.

Action: Remove -e and -w options and issue command again.

PRKO-02122: Database type can only be 'RAC' or 'RACONENODE

Cause: Incorrect database type was specified for 'srvctl convert database' command.

Action: Specify 'RAC' or 'RACONENODE' when running 'srvctl convert database' command.

PRKO-02126: Options '-n' and '-w' cannot both be used with options '-a' and '-r'

Cause: Options -n, -w, -a and -r were used incorrectly.

Action: Correct options and issue command again.

PRKO-02127: Either option '-e' or '-g' must be supplied for adding RAC One Node database

Cause: Options -e and -g were not specified when adding RAC One Node database.

Action: Use 'srvctl add database' command with either -e or -g option.

PRKO-02128: Specified cardinality {0} is not valid for policy-managed RAC One Node service {1}

Cause: Given cardinality was not applicable to RAC One Node service.

Action: Use 'srvctl add service' command without the -c option or specify SINGLETON value for the -c option.

PRKO-02129: Online relocation timeout value {0} is not within the range of {1} and {2}

Cause: Online relocation timeout value was not within the required range.

Action: Supply a value within the required range.

PRKO-02130: Supplied node {0} must be in the candidate list of the administrator-managed database {1}

Cause: The supplied node name was not in the candidate list of the administrator-managed database.

Action: Supply a node in the candidate list of the database and rerun 'srvctl start database' command.

PRKO-02131: Supplied node {0} must be in the server pool of the policy-managed database {1}

Cause: The supplied node name was not in the server pool of the policy-managed database.

Action: Supply a node from the server pool of the database and rerun 'srvctl start database' command.

PRKO-02132: Options '-g', '-r' and '-a' cannot be used to add services for RAC One Node database {0}

Cause: Failed to add specified service because provided options cannot be used to add a service for RAC One Node database.

Action: Use 'srvctl add service' command without options -g, -r or -a.

PRKO-02133: Options '-g', '-r' and '-a' cannot be used to modify services for RAC One Node database {0}

Cause: Failed to modify specified service because provided options cannot be used to modify a service for RAC One Node database.

Action: Use 'srvctl modify service' command without options -g, -r or -a.

PRKO-02134: 'srvctl add instance' command is not supported with RAC One Node databases

Cause: The specified database does not support 'srvctl add instance' command.

Action: Convert the RAC One Node database to a RAC database by using the 'srvctl convert database' command and then rerun 'srvctl add instance' command.

PRKO-02135: 'srvctl remove instance' command is not supported with RAC One Node databases

Cause: The one instance of the RAC One Node database cannot be removed by the 'srvctl remove instance' command.

Action: Run 'srvctl remove database' command.

PRKO-02136: 'srvctl start/stop/enable/disable/modify/status/setenv/getenv/unsetenv instance' commands are not supported with RAC One Node databases

Cause: The supplied instance command is not supported with RAC One Node database.

Action: Perform srvctl operations on the 'database' noun instead of 'instance' with a RAC One Node database.

PRKO-02137: Option '-n' should not be supplied to convert policy-managed RAC One Node database to RAC database

Cause: Failed to convert database because provided option cannot be used to convert policy-managed RAC One Node database.

Action: Use 'srvctl convert database' command without -n option.

PRKO-02138: Database {0} is not of RAC One Node database type

Cause: The supplied database was not a RAC One Node database.

Action: Run 'srvctl convert database' command with database of type RAC One Node.

PRKO-02139: Supplied nodes {0} should contain node {1} where database {1} is already running on

Cause: Supplied nodes did not include the node that the database was running on.

Action: Make sure given nodes include the node that the database is running on.

PRKO-02140: Option '-x' should be supplied when adding single instance database

Cause: Option -x was not supplied when adding single instance database.

Action: Supply -x option and issue command again.

PRKO-02141: Option '-r' requires option '-a'

Cause: Command 'srvctl relocate database' with option '-r' failed because it requires option '-a' to be provided.

Action: Correct options and issue command again.

PRKO-02142: Cannot start RAC One Node database when an online relocation request for the database is already active

Cause: Unable to start the supplied RAC One Node database because it already has an active online relocation request.

Action: Specify another database to start.

PRKO-02143: Cannot stop RAC One Node database when an online relocation request for the database is already active

Cause: Unable to stop the supplied RAC One Node database because it already has an active online relocation request.

Action: Either wait for the online relocation request to complete or specify another database to stop.

PRKO-02144: Option '-e' cannot be used with RAC One Node policy-managed database {0}

Cause: The -e option was specified to modify the candidate server list for RAC One Node policy-managed database.

Action: Either use 'srvctl modify srvpool' to modify the candidate server list or specify -g with 'srvctl modify database' to modify the server pool.

PRKO-02145: 'srvctl remove instance' command is not supported with single instance databases

Cause: The single instance database cannot be removed by the 'srvctl remove instance' command.

Action: Run 'srvctl remove database' command.

PRKO-02147: A 'srvctl add database' command specified the '-e', '-i' or '-w' option for a database that is not Oracle RAC One Node

Cause: A 'srvctl add database' command was issued that included either the '-e', '-i' or '-w' option but did not include a '-c' option specifying that the database being added was Oracle RAC One Node.These options are permitted only for Oracle RAC One Node databases.

Action: Either remove the '-e', '-i' or '-w' option or specify '-c' option with type Oracle RAC One Node.

PRKO-02148: Option '-n' must be supplied when running 'srvctl relocate database' for administrator managed RAC One Node database

Cause: Option -n was not specified when executing relocate on administrator managed RAC One Node database.

Action: Use 'srvctl relocate database' command with -n option.

PRKO-02149: Option '-i' cannot be used to modify instance name of a RAC database

Cause: Option -i in "srvctl modify database" command can be used to modify the instance name of a single instance database or instance name prefix of a RAC One Node database.

Action: Try 'srvctl modify instance' command.

PRKO-02156: Instance name {0} is not valid

Cause: The supplied instance name is not the correct format for RAC One Node database.

Action: Make sure that the instance name is of the format <instance\_name\_prefix>\_1 or <instance\_name\_prefix>\_2. Use 'crsctl modify resource' to correct the instance name.

PRKO-02157: Option '-i' should not specified to convert policy-managed RAC database to RAC One Node database

Cause: Failed to convert database because the provided option can not be used to convert policy-managed RAC database to RAC One Node database.

Action: Use 'srvctl convert database' command without -i option.

PRKO-02158: Option '-n' should not be specified to convert a RAC database to RAC One Node database

Cause: Failed to convert database because the provided option '-n' should not be supplied to convert RAC database to RAC One Node database.

Action: Use 'srvctl convert database' command without -n option.

PRKO-02159: Option '-i' should be specified to convert an administrator-managed RAC database to its equivalent RAC One Node database configuration

Cause: Failed to convert database because the option '-i' was not specified to convert administrator-managed RAC database to its equivalent RAC One Node database configuration.

Action: Use 'srvctl convert database' command with -i option.

PRKO-02160: Option '-w' should not be specified to convert a RAC One Node database to its equivalent RAC database configuration

Cause: Failed to convert database because option '-w' was specified to convert RAC One Node database to its equivalent RAC database configuration.

Action: Use 'srvctl convert database' command without -w option.

PRKO-02165: VIP does not exist on node(s): {0}

Cause: VIP was not configured on the nodes.

Action: Add VIP using 'srvctl add nodeapps' or 'srvctl add vip' and try this command again.

PRKO-02166: GSD does not exist on node(s): {0}

Cause: GSD was not configured on the nodes

Action: Add GSD using 'srvctl add nodeapps' and try this command again.

PRKO-02167: VIP {0} does not exist.

Cause: VIP with the specified name was not configured.

Action: Add VIP using 'srvctl add nodeapps' or 'srvctl add vip' and try this command again.

PRKO-02168: Node applications are still running on node:

Cause: Node applications are still running on node when a remove was attempted.

Action: Stop the node applications before removing them or use force flag when attempting removal.

PRKO-02172: Some or all node applications are not removed successfully on node:

Cause: Not all node applications were removed on the node.

Action: Make sure that all resources that depend on node applications are stopped before attempting to remove node applications. Also if force flag was not specified, reissue this command with the force flag specified.

PRKO-02173: Instance {0} is already a preferred instance for service {1}.

Cause: Given instance is already a preferred instance for the service.

Action: Specify an instance other than the preferred instances of this service.

PRKO-02174: Instance {0} is already an available instance for service {1}.

Cause: Given instance is already an available instance for the service.

Action: Specify an instance other than the available instances of this service.

PRKO-02175: Failed to remove service {0} because this is the last service of RAC One Node database {1}

Cause: An attempt was made to remove the last service of a RAC One Node

Action: Add another service, for example by using 'srvctl add service' command, before removing the given service. Otherwise, if you are trying to deconfigure database, then remove the database directly, for example by using 'srvctl remove database' command.

PRKO-02176: ONS daemon does not exist on node(s): {0}

Cause: ONS was not configured on the nodes.

Action: Add ONS using 'srvctl add nodeapps' command and try this command again.

PRKO-02182: eONS daemon does not exist on node(s): {0}

Cause: eONS was not configured on the nodes.

Action: Add eONS using 'srvctl add nodeapps' command and try this command again.

PRKO-02183: Node applications run on default network only. The netmask given {0} doesn't match default networks netmask {1}

Cause: The netmask given in the modify command doesn't match with default network's netmask.

Action: Modify the default network first using 'srvctl modify nodeapps -S \<options>' and then try modifying the VIP.

PRKO-02184: Node applications run on default network only. The interface given {0} doesn't match default networks interface {1}

Cause: The interface specified in the modify command doesn't match with default network's interface.

Action: Modify the default network's interface using 'srvctl modify nodeapps -S \<options>' and then try modifying the VIP.

PRKO-02185: The new VIP address given is same as the current VIP address

Cause: The VIP address given for modification is same as the current VIP. So there is nothing to modify.

Action: Check the VIP address you want to modify and specify the correct value.

PRKO-02186: The command line parameter host port list should be in the form \<host>\[:\<port>\]\[,\<host>:\[\<port>\]...\]

Cause: The command line parameter -t <host\_port\_list> was not in the format \<host>\[:\<port>\]\[,\<host>:\[\<port>\]...\] with port being numeric.

Action: Check the input and correct any error and try the command again.

PRKO-02187: The network resource has been modified successfully. VIP and other resources that depend on it might not start up unless they are modified

Cause: When underlying network resource has been modified the VIP should be updated to the new network resource. This is not a error and is just a status message.

Action: Use 'srvctl modify nodeapps -A \<options>' to update the VIP to the new network.

PRKO-02188: All the node applications already exist. They were not recreated.

Cause: 'srvctl add nodeapps' was attempted when all the node applications already existed.

Action: If you want to modify node applications you should use 'srvctl modify nodeapps' command.

PRKO-02190: VIP exists for node {0}, VIP name {1}

Cause: The VIP being added already exists.

Action: Check the input and if VIP needs to be modified use 'srvctl modify VIP' command.

PRKO-02199: Invalid address string:

Cause: VIP address being passed on the command line is not a valid address string.

Action: Address string should be of the format <name|ip>/\<netmask>/\[if1\[|if2...\]\]. Check the usage and correct the address format.

PRKO-02200: Invalid interface specified on command line: {0}

Cause: VIP address specification '-A <name|ip>/\<netmask>\[/if1\[|if2|...\]\]' or the network address specification '-S \<subnet>/\<netmask>\[/if1\[|if2|...\]\]' on the command line contained interfaces names, none of which exist on current node.

Action: Check the interfaces listed in the address string and make sure that they are enabled and are up. Use network interface names on the command line if there is more than one interfaces that connect to the same network.

PRKO-02207: Warning:-{0} option has been deprecated and will be ignored.

Cause: Deprecated option has been used in the command line. The option will be ignored.

Action: Check the documentation for the new syntax of the command.

PRKO-02208: {0} command has been deprecated and will be ignored.

Cause: The command being executed has been deprecated and will not do any action.

Action: Check the documentation for the commands supported by srvctl.

PRKO-02209: {0} command is not supported for configuration using server pool.

Cause: The given command failed because it isn't applicable to instances of policy managed-databases.

Action: Check the documentation on the commands that are applicable to policy-managed databases.

PRKO-02211: ASM listener was not found

Cause: Check the reported message, ASM listener may not exist.

Action: Use "srvctl modify asm -l <lsnr\_name>" to set the listener that ASM should register with.

PRKO-02214: Specified server pool {0} cannot be used to host single instance database {1}

Cause: An attempt to create a single instance database failed because the specified server pool had no configured candidate server.

Action: Use 'srvctl modify srvpool' with -n option to configure a candidate server for the server pool. Make sure that the candidate server name specified with the -n option matches that of the -x option in 'srvctl add database' command.

PRKO-02215: Specified server pool {0} has more than one candidate server

Cause: An attempt to create a single instance database failed because a server pool with more than one candidate server was specified.

Action: Provide a server pool with only one candidate server when creating a single instance database.

PRKO-02310: VIP does not exist on node {0}.

Cause: VIP was not configured on that node on which modification was attempted.

Action: VIP must be added using 'srvctl add nodeapps' command, before it can be modified.

PRKO-02313: VIP {0} does not exist.

Cause: An attempt was made to remove a VIP with the specified vipname. No such VIP was configured on the cluster.

Action: If this is the expected state then it is not an error. Check the status of VIPs using 'srvctl status vip' command. VIP must be added using 'srvctl add vip' command before it can be removed.

PRKO-02318: Target instance {0} already supports service {1}.

Cause: Given database instance already provides the given service.

Action: Specify an instance that is not a preferred or available instance for this service.

PRKO-02331: ONS daemon does not exist.

Cause: ONS daemon was not configured on this cluster.

Action: ONS daemon can be configured using the 'srvctl add nodeapps' command.

PRKO-02339: eONS daemon does not exist.

Cause: eONS daemon was not configured on this cluster.

Action: eONS daemon can be configured using the 'srvctl add nodeapps' command.

PRKO-02377: eONS already uses {0} as listening port. Nothing to modify.

Cause: The listening port specified in this command is already in use by eONS.

Action: Check the input and if the listening port needs to be changed then specify a different port.

PRKO-02380: VIP {0} is still running on node: {1}

Cause: VIP to be removed is still running on a node.

Action: Stop the VIP before attempting to remove it or retry the command with force flag.

PRKO-02381: VIP {0} is not removed successfully:

Cause: VIP remove action failed because VIP was running and force flag was not specified or an exception occurred during the removal.

Action: Make sure that any applications, like for example listener, that depend on VIP are down. Try using -f option to remove the VIP. If you use force option to remove VIP then any application that depends on this VIP will stop working. Look at the help message for the accompanying exception.

PRKO-02383: Network {0} is not removed successfully:

Cause: Since there were no VIPs hosted on the network an attempt was made to remove the network and network removal failed.

Action: Make sure that all other applications that depend on default network are stopped. If force flag was not specified then specify force flag and try the command again.

PRKO-02385: The specified hostname or address {0} cannot be resolved.

Cause: An invalid IP address or irresolvable hostname was specified.

Action: If IP address is specified then make sure that it is of legal length. If a host name is specified then make sure that the host name resolves to an IP address.

PRKO-02386: Netmask is missing in address string:

Cause: NETMASK is missing in the VIP address that was passed in the command string.

Action: VIP address is of form <ip\_or\_name>/\<netmask>\[/\<interface1>\[|\<interface2>...\]\]. Specify the netmask.

PRKO-02387: -n <node\_name> option has been deprecated.

Cause: -n <node\_name> has been deprecated in this release.

Action: Try to remove the usage of -n <node\_name> in the command.

PRKO-02388: Command line option {0} should be followed by a value.

Cause: The value needs to be specified by the command line option.

Action: Look at the usage and of the command and specify an appropriate value.

PRKO-02389: Invalid command line options. Neither -A nor -n can be specified with -S.

Cause: Invalid combination of options specified for add/modify node application command. -A is node-specific option and has to be used with -n option. -S option is a global option and it cannot be used with -A or -n option.

Action: Issue the command using either -A and -n together or -S without -A or -n.

PRKO-02390: -n <node\_name> option has been deprecated and is ignored.

Cause: -n <node\_name> option has been deprecated and is ignored from this release. It has no effect on the command.

Action: Remove the usage of -n <node\_name> from the command line.

PRKO-02391: Network resource {0},{1} already exists. Nothing to modify

Cause: The subnet specified is already the default subnet.

Action: Check the input and if the subnet needs to be modified then specify a different subnet.

PRKO-02392: eONS already uses {0} as Multicast address. Nothing to modify.

Cause: The Multicast address specified in this command is already in use by eONS.

Action: Check the input and if the Multicast address needs to be changed then specify a different address.

PRKO-02393: eONS already uses {0} as Multicast port. Nothing to modify.

Cause: The Multicast port specified in this command is already in use by eONS.

Action: Check the input and if the Multicast port needs to be changed then specify a different port.

PRKO-02394: ONS already uses {0} as port for local connections. Nothing to modify.

Cause: The modify node applications command failed because the ONS port for local connections is already used by ONS for local connections.

Action: Check the input and if the port used by ONS for local connections need to be modified specify a different address.

PRKO-02395: ONS already uses {0} as port for remote connections. Nothing to modify.

Cause: The modify node applications command failed because the ONS port for remote connections is already used by ONS for remote connections.

Action: Check the input and if the port used by ONS for remote connections need to be modified specify a different address.

PRKO-02396: The list of remote host/port ONS pairs matches the current list: {0}. Nothing to modify.

Cause: The modify node applications command failed because the remote host/port ONS pairs matches the current list.

Action: Check the input and if the remote host/port pairs need to be modified and specify a different host/port list.

PRKO-02405: Network resource does not exist on the cluster nodes.

Cause: Network resource does not exist on the cluster nodes.

Action: Node applications can be added by using 'srvctl add nodeapps' command.

PRKO-02409: GSD is already disabled on node(s): {0}

Cause: The disable node applications command failed because GSD was already disabled.

Action: If this is the expected state then this is not an error. If it is not then GSD can be enabled by 'srvctl enable nodeapps' command.

PRKO-02410: VIP is already disabled on node(s): {0}

Cause: The disable node applications command failed because VIP was already disabled.

Action: If this is the expected state then this is not an error. If it is not then VIP can be enabled by 'srvctl enable nodeapps' command.

PRKO-02411: Network resource is already disabled.

Cause: The disable node applications command failed because Network resource was already disabled.

Action: If this is the expected state then this is not an error. If it is not then Network resource can be enabled by 'srvctl enable nodeapps' command.

PRKO-02412: ONS is already disabled on node(s): {0}

Cause: The disable node applications command failed because ONS was already disabled.

Action: If this is the expected state then this is not an error. If it is not then ONS can be enabled by 'srvctl enable nodeapps' command.

PRKO-02413: eONS is already disabled on node(s): {0}

Cause: The disable node applications command failed because eONS was already disabled.

Action: If this is the expected state then this is not an error. If it is not then eONS can be enabled by 'srvctl enable nodeapps' command.

PRKO-02414: GSD is already enabled on node(s): {0}

Cause: The enable node applications command failed because GSD is already enabled.

Action: If this is the expected state then this is not an error. If it is not then GSD can be disabled by 'srvctl disable nodeapps' command.

PRKO-02415: VIP is already enabled on node(s): {0}

Cause: The enable node applications command failed because VIP is already enabled.

Action: If this is the expected state then this is not an error. If it is not then VIP can be disabled by 'srvctl disable nodeapps' command.

PRKO-02416: Network resource is already enabled.

Cause: The enable node applications command failed because Network resource is already enabled.

Action: If this is the expected state then this is not an error. If it is not then Network resource can be disabled by 'srvctl disable nodeapps' command.

PRKO-02417: ONS is already enabled on node(s): {0}

Cause: The enable node applications command failed because ONS is already enabled.

Action: If this is the expected state then this is not an error. If it is not then ONS can be disabled by 'srvctl disable nodeapps' command.

PRKO-02418: eONS is already enabled on node(s): {0}

Cause: The enable node applications command failed because eONS is already enabled.

Action: If this is the expected state then this is not an error. If it is not then eONS can be disabled by 'srvctl disable nodeapps' command.

PRKO-02419: GSD is already started on node(s): {0}

Cause: The start node applications command failed because GSD is already started.

Action: If this is the expected state then this is not an error. If it is not then GSD can be stopped by 'srvctl stop nodeapps' command.

PRKO-02420: VIP is already started on node(s): {0}

Cause: The start node applications command failed because VIP is already started.

Action: If this is the expected state then this is not an error. If it is not then VIP can be stopped by 'srvctl stop nodeapps' command.

PRKO-02421: Network resource is already started on node(s): {0}

Cause: The start node applications command failed because Network resource is already started.

Action: If this is the expected state then this is not an error. If it is not then Network resource can be stopped by 'srvctl stop nodeapps' command. Note that once started network resource cannot be stopped.

PRKO-02422: ONS is already started on node(s): {0}

Cause: The start node applications command failed because ONS is already started.

Action: If this is the expected state then this is not an error. If it is not then ONS can be stopped by 'srvctl stop nodeapps' command.

PRKO-02423: eONS is already started on node(s): {0}

Cause: The start node applications command failed because eONS is already started.

Action: If this is the expected state then this is not an error. If it is not then eONS can be stopped by 'srvctl stop nodeapps' command.

PRKO-02424: GSD is already stopped on node(s): {0}

Cause: The stop node applications command failed because GSD is already stopped.

Action: If this is the expected state then this is not an error. If it is not then GSD can be started by 'srvctl start nodeapps' command.

PRKO-02425: VIP is already stopped on node(s): {0}

Cause: The stop node applications command failed because VIP is already stopped.

Action: If this is the expected state then this is not an error. If it is not then VIP can be started by 'srvctl start nodeapps' command.

PRKO-02426: ONS is already stopped on node(s): {0}

Cause: The stop node applications command failed because ONS is already stopped.

Action: If this is the expected state then this is not an error. If it is not then ONS can be started by 'srvctl start nodeapps' command.

PRKO-02427: eONS is already stopped on node(s): {0}

Cause: The stop node applications command failed because eONS is already stopped.

Action: If this is the expected state then this is not an error. If it is not then eONS can be started by 'srvctl start nodeapps' command.

PRKO-02428: VIP is running on the node {0} and cannot be modified.

Cause: Modify nodeapps command failed because VIP being modified is running on a node.

Action: Stop the node application by issuing 'srvctl stop nodeapps' and retry the modify again.

PRKO-02429: -n <node\_name> should be specified with -A <name|ip>/netmask\[/if1\[|if2\]\] for modifying VIP.

Cause: If -n <node\_name> option is specified then -A option should also be specified for modifying VIP.

Action: If you want to modify the VIP then use specifiy both the -n and -A options. Otherwise remove the -n <node\_name> option and try command again.

PRKO-02430: -A <name|ip>/netmask\[/if1\[|if2\] should be specified with -n <node\_name> for modifying VIP.

Cause: -A \<options> has been specified for the modify nodeapps command without specifying which node VIP needs to be modified.

Action: Specify the node whose VIP needs to be modified by using -n option.

PRKO-02431: Warning: the -n option is obsolescent; 'srvctl remove vip' is preferred for removing per-node VIP resource

Cause: A 'srvctl remove nodeapps' command was issued with the -n option specifying one or more nodes. Support for this option will be removed in a future release, at which time you must use the preferred command 'srvctl remove vip -i <vip\_list>'.

Action: The command is processed normally and attempts to remove VIP resources for the specified node(s). This message is displayed only to alert you to a future change. Use 'srvctl remove nodeapps' to remove all node applications from the last node of the cluster.

PRKO-02438: Network resource does not exist.

Cause: Network resource to be started/stopped/modified/enabled/disabled does not exist.

Action: Network resource can be created using 'srvctl add nodeapps' command.

PRKO-02439: VIP does not exist.

Cause: VIP to be started/stopped/modified/enabled/disabled does not exist.

Action: VIP can be created using 'srvctl add nodeapps' command.

PRKO-02440: Network resource is already stopped.

Cause: The stop node applications command failed because network resource was already stopped.

Action: If this is the expected state then this is not an error. If it is not then network resource can be started by 'srvctl start nodeapps' command.

PRKO-02452: ONS already exists

Cause: A new instance of ONS daemon could not be created, as there is an existing instance of ONS.

Action: If this is the expected state then it is not an error. Use 'srvctl config ons' command to look at ONS daemon attributes and 'srvctl modify ons' command to modify ONS attributes.

PRKO-02453: eONS already exists

Cause: A new instance of eONS daemon could not be created, as there is an existing instance of eONS.

Action: If this is the expected state then it is not an error. Use 'srvctl config eons' command to see if eONS daemon is configured. Use 'srvctl modify eons' command to modify eONS attributes.

PRKO-02458: ONS does not exist

Cause: ONS daemon was not configured on this instance of Oracle Restart.

Action: Add ONS daemon using the 'srvctl add ons' command and try this command again.

PRKO-02463: eONS does not exist

Cause: eONS daemon was not configured on this instance of Oracle Restart.

Action: Add eONS daemon using the command 'srvctl add eons' command and try this command again.

PRKO-02465: ONS does not exist.

Cause: ONS daemon was not configured on this instance of Oracle Restart.

Action: ONS daemon can be configured using the 'srvctl add ons' command.

PRKO-02567: eONS daemon does not exist.

Cause: eONS daemon was not configured on this instance of Oracle Restart.

Action: eONS daemon can be configured using the 'srvctl add eons' command.

PRKO-02569: ONS is already started.

Cause: The 'srvctl start ons' command failed because the ONS daemon was already started.

Action: If this is the expected state then this is not an error. If it is not then ONS can be stopped by 'srvctl stop ons' command.

PRKO-02571: eONS is already started.

Cause: The 'srvctl start eons' command failed because the eONS daemon was already started.

Action: If this is the expected state then this is not an error. If it is not then eONS can be stopped by 'srvctl stop eons' command.

PRKO-02573: ONS daemon is already stopped.

Cause: The 'srvctl stop ons' command failed because the ONS daemon was already stopped.

Action: If this is the expected state then this is not an error. If it is not then ONS can be started by 'srvctl start ons' command.

PRKO-02575: eONS daemon is already stopped.

Cause: The 'srvctl stop eons' command failed because the eONS daemon was already stopped.

Action: If this is the expected state then this is not an error. If it is not then eONS can be started by 'srvctl start eons' command.

PRKO-02576: ONS is already enabled.

Cause: The 'srvctl enable ons' command failed because the ONS was already enabled.

Action: If this is the expected state then this is not an error. If it is not then ONS can be disabled by 'srvctl disable ons' command.

PRKO-02579: eONS is already enabled.

Cause: The 'srvctl enable eons' command failed because the eONS was already enabled.

Action: If this is the expected state then this is not an error. If it is not then eONS can be disabled by 'srvctl disable eons' command.

PRKO-02581: ONS is already disabled.

Cause: The 'srvctl disable ons' command failed because the ONS was already disabled.

Action: If this is the expected state then this is not an error. If it is not then ONS can be enabled by 'srvctl enable ons' command.

PRKO-02583: eONS is already disabled.

Cause: The 'srvctl disable eons' command failed because the eONS was already disabled.

Action: If this is the expected state then this is not an error. If it is not then eONS can be enabled by 'srvctl enable eons' command.

PRKO-02588: ONS daemon could not be removed because it is still running.

Cause: 'srvctl remove ons' command failed because ONS daemon was still running.

Action: Stop the ons daemon by using 'srvctl stop ons' command and then attempt to remove it. You can also use the force option to remove a running ons daemon.

PRKO-02589: eONS daemon could not be removed because it is still running.

Cause: 'srvctl remove eons' command failed because eONS daemon was still running.

Action: Stop the ons daemon by using 'srvctl stop eons' command and then attempt to remove it. You can also use the force option to remove a running eons daemon.

PRKO-02590: None of the ONS daemon parameters were modified.

Cause: The configuration of the ONS daemon has remained the same after the 'srvctl modify ons' command.

Action: Make sure that at least one of the optional modification parameters was specified on the command line. The current values of parameters of the ONS daemon can be found by using 'srvctl config ons' command. Specify at least one value different then current value while issuing the 'srvctl modify ons' command.

PRKO-02591: None of the eONS daemon parameters were modified.

Cause: The configuration of the eONS daemon has remained the same after the 'srvctl modify eons' command.

Action: Make sure that at least one of the optional modification parameters was specified on the command line. The current values of parameters of the eONS daemon can be found by using 'srvctl config eons' command. Specify at least one value different then current value while issuing the 'srvctl modify eons' command.

PRKO-02593: enable of GNS failed.

Cause: Enabling the GNS server failed.

Action: Examine the accompanying exception for details.

PRKO-02595: modify of GNS failed.

Cause: Modification the GNS server failed.

Action: Examine the accompanying exception for details.

PRKO-02597: disable of GNS failed.

Cause: Disabling the GNS server failed.

Action: Examine the accompanying exception for details.

PRKO-02599: relocation of GNS failed.

Cause: Relocation of the GNS server failed.

Action: Examine the accompanying exception for details.

PRKO-02601: removal of GNS failed.

Cause: Removal of the GNS server failed.

Action: Examine the accompanying exception for details.

PRKO-02603: addition of GNS failed.

Cause: The addition of the GNS server failed.

Action: Examine the accompanying exception for details.

PRKO-02604: GNS is already running

Cause: The GNS server is already running.

Action: Remove the GNS server first before trying to add it.

PRKO-02611: GNS VIP does not exist. Specify the {0} option to create one.

Cause: The attempt to add GNS failed because the VIP associated with it does not exist.

Action: Create the VIP.

PRKO-02621: The '-x \<node>' option cannot be used to create RAC database {0}

Cause: The '-x' option was supplied to create a single-instance database, along with '-c RAC' requesting a RAC database.

Action: Specify '-c SINGLE' with '-x \<node>'

PRKO-02700: The CVU resource is not configured

Cause: The CVU resource was not configured on the cluster or an unexpected error occurred while querying Clusterware for the CVU resource.

Action: If the CVU resource was not configured then a new resource can be created using 'srvctl add cvu' command. If the resource was configured, look at any accompanying error messages.

PRKO-02702: CVU is already disabled

Cause: CVU resource could not be disabled because it is already disabled.

Action: If this is the expected state then this is not an error.

PRKO-02703: CVU is already enabled

Cause: CVU resource could not be enabled because it is already enabled.

Action: If this is the expected state then this is not an error.

PRKO-02707: CVU resource must be stopped before removing

Cause: 'srvctl remove cvu' was issued while CVU instance was running.

Action: Stop the CVU resource using 'srvctl stop cvu' and then try removing.

PRKO-02708: Unable to convert RAC One Node database because it has an active online relocation request

Cause: Failed to convert RAC One Node database to RAC database because there was an active online relocation request for the database.

Action: Wait for the online relocation request to complete and then run 'srvctl convert database'.

PRKO-02709: Unable to convert RAC One Node database because it has a failed online relocation request

Cause: Failed to convert RAC One Node database to RAC database because there was a failed online relocation request for the database.

Action: Use 'srvctl status database' command to show the target node of the failed online relocation request process. Either run 'srvctl relocate database' with -a option or with -n option with the correct target node. Then run 'srvctl convert database'.

PRKO-02710: Option '-n' cannot be used to start RAC database {0}

Cause: The -n option was specified to start RAC database, but -n is only applicable to RAC One Node databases.

Action: Either use 'srvctl start instance' to start RAC database instance on the given node or use 'srvctl start database' without -n option to start the RAC database.

PRKO-03026: Only one instance can be listed in -i <inst\_name\_list> when -n option is specified

Cause: More than one instance was specified for -i option when both -i and -n options were used.

Action: Supply one instance name for -i option when using both -i and -n option.

PRKO-03031: Server pool {0} already exists

Cause: Command 'srvctl add serverpool' failed because the given server pool already exists.

Action: Make sure that the name of server pool is correct and a server pool with the given name doesn't exist.

PRKO-03032: Invalid instance name(s): {0}

Cause: Some of the supplied instance names do not exist in the database configuration.

Action: Please supply valid instance names and retry.

PRKO-03077: Failed to remove database {0}:

Cause: Failed to remove the database.

Action: Examine the accompanying message(s) for details of the error, and respond accordingly.

PRKO-03081: No such environment variable setting: {0}

Cause: The environment variable(s) does not exist for the specified resource.

Action: Supply a valid environment variable.

PRKO-03085: Volume device: {0}

Cause: Volume device label

Action: None

PRKO-03086: Mountpoint path: {0}

Cause: Mountpoint path label

Action: None

PRKO-03087: User: {0}

Cause: User label

Action: None

PRKO-03113: Administrator-managed database {1} can not support policy-managed service {0}.

Cause: The specified database does not support policy-managed services.

Action: Provide a database which supports policy-managed services.

PRKO-03114: Policy-managed database {1} can not support administrator-managed service {0}.

Cause: The specified database does not support administrator-managed services.

Action: Provide a database which supports administrator-managed services.

PRKO-03115: -P option cannot be used with policy-managed service {0}.

Cause: The -P option was specified for a policy-managed service.

Action: Use the -m option to specify failover processing for a policy-managed service.

PRKO-03116: '-g' or '-r' option should be provided

Cause: one of specified options should be provided.

Action: make sure that one of specified options is incuded into the command line.

PRKO-03117: Service {0} already exists in database {1}

Cause: The service being added already exists.

Action: If the service needs to be modified use 'srvctl modify service' command.

PRKO-03118: Failed to check if service {0} exists: {1}

Cause: Failed to get the servcie data.

Action: Make sure that Oracle Clusterware is active.

PRKO-03119: Database {0} cannot be started since it has no configured instances.

Cause: The specified database is an administrator-managed database and it cannot be started because no instances were configured.

Action: Use srvctl add instance command to configure the instance and then retry.

PRKO-03120: Database {0} cannot be stopped since it has no configured instances.

Cause: The specified database is an administrator-managed database and it could not be stopped because no instances were configured.

Action: Use srvctl add instance command to configure the instance and then retry.

PRKO-03121: -i option or -n option is required for starting an instance on the administrator-managed database {0}.

Cause: The specified database is an administrator-managed database and the srvctl start instance command requires the instance name or nodename to be specified.

Action: Use srvctl start instance command with either the -i or -n option to start the instance.

PRKO-03122: -i option or -n option is required for stopping an instance of database {0}

Cause: Neither the instance name nor the nodename was provided during 'srvctl stop instance' command invocation.

Action: Use 'srvctl stop instance' command with either the -i or -n option to specify which instance to stop.

PRKO-03125: Invalid value {0} for command line option {1}

Cause: Invalid value was specified for the command line option.

Action: Check the value printed and specify the correct value.

PRKO-03126: Invalid GNS logging level: "{0}"

Cause: The level of logging specified was not a positive integer.

Action: Specify a positive integer.

PRKO-03128: Unable to add database because the resource for diskgroup {0} could not be found. {1}

Cause: The resource for the specified disk group could not be found. Either the diskgroup name was misspelled or the diskgroup has not been mounted.

Action: Correct the diskgroup spelling or use sqlplus to create the diskgroup.

PRKO-03129: Unable to modify database because the resource for diskgroup {0} could not be found. {1}

Cause: The resource for the specified disk group could not be found. Either the diskgroup name was misspelled or the diskgroup has not been mounted.

Action: Correct the diskgroup spelling or use sqlplus to create the diskgroup.

PRKO-03130: Server pool {0} is internally managed as part of administrator-managed database configuration and therefore cannot be modified directly via srvpool object.

Cause: An attempt was made to alter configuration of an internally managed server pool that is hosting an administrator-managed configuration.

Action: Do not modify this server pool via srvpool object directly. Instead use srvctl add/remove instance or srvctl modify database/service to alter this server pool's configuration.

PRKO-03132: -i option or -n option is required for checking the status of an instance of database {0}

Cause: Neither the instance name nor the nodename was provided during 'srvctl status instance' command invocation.

Action: Use 'srvctl status instance' command with either the -i or -n option to check the status of the instance.

PRKO-03133: Database {0} has no instance on node {1}

Cause: Instance was not configured on the specified node.

Action: Both 'srvctl add instance' or 'srvctl modify instance' command can also be used to change inst-node mapping in administrator-managed db's. For policy-managed database, use either 'srvctl start instance' command with -n option to start the instance on the specified node or use 'srvctl modify instance' command to configure an instance for that node.

PRKO-03134: -n option cannot be specified in conjunction with -z option

Cause: -n and -z options were both provided during 'srvctl modify instance' command invocation.

Action: Use 'srvctl modify instance' command with either the -n or -z option to modify the node instance mapping of the database instance.

PRKO-03135: -z option cannot be used with administrator-managed database {0}

Cause: The -z option was specified in an attempt to remove node to instance mapping of administrator-managed database.

Action: Use 'srvctl remove instance' command to remove node instance mapping of administrator-managed database.

PRKO-03136: Option '-c' cannot be used with administrator-managed service {0}

Cause: The -c option was specified for administrator-managed service.

Action: Reissue the command without the -c option.

PRKO-03138: Node {0} does not belong to server pool {1} which defines nodes for service {2}

Cause: Node doesn't belong to the server pool which defines nodes which can be used to run the specified service.

Action: Supply a node which belongs to specified server pool.

PRKO-03139: Options '-i' and '-t' cannot be used with policy-managed service {0}

Cause: The -i and -t options were specified to relocate a policy-managed service.

Action: Use options -c and -n to relocate a service.

PRKO-03140: Options '-c' and '-n' cannot be used with administrator-managed service {0}

Cause: The -c and -n options were specified to relocate an administrator-managed service.

Action: Use options -i and -t to relocate a service.

PRKO-03141: Database {0} could not be removed because it was running

Cause: The 'srvctl remove database' command failed because the database was running.

Action: Stop the database by using 'srvctl stop database' command and then attempt to remove it. You can also use the force option to remove the running database.

PRKO-03142: Option '-i' cannot be used to enable/disable services for policy-managed database {0}

Cause: Policy-managed database services can only be enabled or disabled by node, not by instance.

Action: Use option -n \<node> to specify nodes on which to enable or disable services for this policy-managed database.

PRKO-03143: Options '-i', '-r', '-n' and '-a' cannot be used to modify policy-managed service {0}

Cause: Options -i, -r, -n and -a can be used to modify administrator-managed service only.

Action: Make sure that the service you are going to modify is an administrator-managed service.

PRKO-03144: Option '-a' requires options '-n' and '-i' to be provided

Cause: Option -a can not be used without options -n and -i.

Action: Make sure that options -n, -i and -a are provided according to 'srvctl modify service' syntax.

PRKO-03145: Option '-i' requires one of the options '-t', '-r' or '-n' to be set

Cause: Option -i can not be used without additional options.

Action: Make sure that required option is provided according to 'srvctl modify service' syntax.

PRKO-03146: Option '-i' is not provided

Cause: Options -t,-r, and -n requires option -i to be set.

Action: Make sure that required option is provided according to 'srvctl modify service' syntax.

PRKO-03147: Instance {0} cannot be removed because it is the only preferred instance for service(s) {1} for database {2}

Cause: An attempt was made to remove the instance which is the only preferred instance for specified services.

Action: Make sure that specified services have more than one preferred instance or modify services to not have the instance as a preferred instance.

PRKO-03148: Instance {0} does not support service {1}.

Cause: The given database instance is not defined as a preferred or available instance for the given service.

Action: Specify an instance that is defined as preferred or available instance for the given service.

PRKO-03149: The candidate server {0} of server pool {1} is different from the server {2} specified with the '-x' option

Cause: Specified server must be the candidate server of the specified server pool.

Action: Make sure that the server specified with '-x' option is the same as the candidate server of the given server pool.

PRKO-03150: The server pool(s) {0} specified with the '-g' cannot be used to add an administrator-managed database

Cause: A request to add an administrator-managed database specified the -g option.

Action: Use 'srvctl add database' without the '-g' option to add an administrator-managed database.

PRKO-03151: Option '-g' cannot have more than one specified server pool when converting an administrator-managed database to a policy-managed database

Cause: An attempt was made to convert an administrator-managed database to a policy-managed database by specifying more than one server pool.

Action: Make sure to specify only one server pool with the '-g' option when converting an administrator-managed database to a policy-managed database.

PRKO-03152: The server pool(s) {0} specified with the '-g' option are subpools of Generic and therefore cannot be used to modify the server pool value of a policy-managed database

Cause: The supplied server pools are meant for managing administrator-managed databases because they are subpools of Generic.

Action: Make sure that none of the supplied server pools are meant for managing administrator-managed database. Only supply server pools meant for managing policy-managed databases to the -g option of 'srvctl modify database' command. Use 'srvctl config srvpool' command to list the qualified server pools meant for managing policy managed databases.

PRKO-03153: -i option and/or -n option is required for starting an instance on the policy-managed database {0}.

Cause: The specified database is a policy-managed database and the 'srvctl start instance' command requires the instance name and/or nodename to be specified.

Action: Use 'srvctl start instance' command with either the -i or -n option or both -i and -n options to start the instance.

PRKO-03154: Both -i and -n options are specified for starting an instance on the administrator-managed database {0}.

Cause: The specified database is an administrator-managed database and the 'srvctl start instance' command requires either the instance name or nodename to be specified but not both.

Action: Use 'srvctl start instance' command with either the -i or -n option to start the instance.

PRKO-03155: Can not start the instance {0} on the specified node {1} because the node is assigned to another user configured instance {2}

Cause: The database specified on 'srvctl start instance' is policy managed and has another instance already configured on the nodename specified with the -n option.

Action: Either reformulate the 'srvctl start instance' command so that there is no conflict with configured instances' nodes, or use 'srvctl modify instance' to change configured instances' nodes.

PRKO-03160: Server pool {0} is internally managed as part of administrator-managed database configuration and therefore cannot be queried directly via srvpool object.

Cause: An attempt was made to query configuration of an internally managed server pool that is hosting an administrator-managed configuration.

Action: Do not query this server pool via srvpool object directly. Instead use srvctl config/status database/service command to query servers that are part of this pool's configuration.

PRKO-03161: Server pool {0} is internally managed as part of administrator-managed database configuration and therefore cannot be removed directly via srvpool object.

Cause: An attempt was made to remove configuration of an internally managed server pool that is hosting an administrator-managed configuration.

Action: Do not remove this server pool via srvpool object directly. Instead use srvctl remove service/database command to remove this server pool and any service/database hosted by the server pool.

PRKO-03162: The actions setenv, getenv, and unsetenv are not suppported for Single Client Access Name listener {0}

Cause: Failed to use srvctl setenv, getenv, and unsetenv listener command for specified Single Client Access Name Listener. The environment variables for Single Client Access Name Listener cannot be changed.

Action: Do not set, get, and unset environment variables for Single Client Access Name Listener.

PRKO-03163: Options '-u', '-r', '-a', '-g' and '-c' cannot be used to add service {0} for single instance database {1}

Cause: Failed to add specified service because provided options can not be used to add a service for single instance database.

Action: use 'srvctl add service' command without options -u, -r, -a, -g or -c.

PRKO-03164: Options '-r', '-f', '-n', '-i', '-t', '-a', '-c' and '-x' cannot be used to modify service {0} for single instance database {1}

Cause: Failed to modify specified service because provided options can not be used to modify a service for single instance database.

Action: Use 'srvctl modify service' command without options -r, -f, -n, -i, -t, -a, -c or -x.

PRKO-03165: Service {0} is defined for single instance database {1} and therefore cannot be relocated

Cause: Failed to relocate specified service because provided options can not be used to relocate a service for single instance database.

Action: Make sure that you issue 'srvctl relocate service' command for the service which is not defined for a single instance database.

PRKO-03166: Invalid GNS parameter: "{0}"

Cause: An invalid parameter value was specified.

Action: A parameter value must have the following format: \<name>:\<value>. The name may not contain a colon (":"). The value may not contain a comma (",").

PRKO-03167: EONS has been deprecated and ONS should be used to set and modify the local port for Enterprise Manager.

Cause: The command being executed has been deprecated and will not do any action.

Action: Use online help 'srvctl -h' or check the documentation for the commands supported by srvctl.

PRKO-03174: 'srvctl relocate service' command is not supported on RAC One Node database service {0}

Cause: An attempt was made to relocate a RAC One Node database service using 'srvctl relocate service' command.

Action: Use 'srvctl relocate database' command to relocate the RAC One Node database and its services to the target server.

PRKO-03175: TAF policy 'PRECONNECT' cannot be used to add a service for single instance database {0}

Cause: Failed to add specified service because provided TAF specification can not be used with a single instance database.

Action: Use 'srvctl add service' command without 'PRECONNECT' TAF policy.

PRKO-03176: Option '-g' cannot be used with administrator-managed service {0}

Cause: An attempt to change the server pool of service was rejected because the -g option cannot be used with administrator-managed service.

Action: Change the preferred and available instances of the service via 'srvctl modify service' command to manage placement of administrator-managed service.

PRKO-03226: Upgrade from version {0} to version {1} using 'srvctl upgrade model' command of version {2} is not supported

Cause: A 'srvctl upgrade model' command was issued for a version change that is other than an increase in patch set level.

Action: Check that the versions provided are correct.

PRKO-03229: Option '-i' cannot be used to enable or disable service(s) {0} for single instance database {1}

Cause: Failed to enable/disable specified service because its database is a single instance database.

Action: Make sure that you issue 'srvctl enable/disable service' command without option -i.

PRKO-03241: The '-o <oracle\_home>' option value "{0}" corresponds to a pathname that does not exist or is not a directory

Cause: The '-o <oracle\_home>' option value did not resolve to an existing directory pathname.

Action: Ensure that the '-o <oracle\_home>' option value correponds to an existing directory pathname.

PRKO-03242: The '-s <state\_file>' option value "{0}" is a directory

Cause: The '-s <state\_file>' option value resolved to an existing directory pathname instead of a file pathname.

Action: Ensure that the '-s <state\_file>' option value correponds to file.

PRKO-03243: The '-s <state\_file>' option value "{0}" is a file under a non-writable directory

Cause: The '-s <state\_file>' option value resolved to a non-writable pathname.

Action: Ensure that the state file parent directory has write permissions.

PRKO-03244: The '-s <state\_file>' option value "{0}" already exists

Cause: The '-s <state\_file>' option value resolved to an existing file pathname.

Action: Ensure that the '-s <state\_file>' option value corresponds to a non-existing file pathname.

PRKO-03245: Cannot determine the canonical path to the state file "{0}"

Cause: The '-s <state\_file>' option value specified a pathname for which the canonical path cannot be retrieved.

Action: Provide the absolute pathname for '-s <state\_file>' option value.

PRKO-03246: The '-s <state\_file>' option value "{0}" does not exist or cannot be read

Cause: The '-s <state\_file>' option value mapped to a non-existing or non-readable file pathname.

Action: Ensure that the '-s <state\_file>' option value corresponds to an existing readable file pathname.

PRKO-03249: Failed to add service {0} with PRECONNECT TAF policy because PRECONNECT TAF policy requires at least one available instance

Cause: Attempt to add a service with PRECONNECT TAF policy was rejected because no available instance was specified.

Action: Specify at least one available instance using -a option of 'srvctl add service' command if the service TAF policy is to be PRECONNECT.

PRKO-03251: Failed to relocate as relocation is not supported in Oracle Restart mode

Cause: Attempt to relocate failed as relocation is unsupported in Oracle Restart.

Action: Ensure you are in a cluster environment to relocate managed entities.

PRKO-03252: Failed to convert as convert action is not supported in Oracle Restart Mode

Cause: Attempt to convert failed as convert action is unsupported in Oracle Restart.

Action: Ensure you are in a cluster environment to convert managed entities.

PRKO-03253: An attempt to modify the OC4J port failed because OC4J is running. Use -f to force stop and restart of OC4J.

Cause: A request to modify the port number of OC4J was rejected because such modification requires OC4J to be stopped and restarted.

Action: Use '-f' option to force restart of OC4J.

PRKO-09059: Invalid command line options for listener. '-a' can not be specified with '-l'.

Cause: Invalid combination of options specified for listener command.

Action: Issue the command using either '-l <listener\_name>' or '-a'.

PRKO-09063: Single Client Access Name must start with a letter unless it is an IP address

Cause: A SCAN was supplied which did not begin with a letter, however SCAN names must begin with a letter.

Action: Supply a SCAN name that begins with a letter.

PRKO-09066: Invalid upgrade phase ''{0}'' for upgrade model command

Cause: An invalid value was specified for upgrade phase.

Action: Upgrade phase must be either 'first' or 'last'.

PRKO-09067: Invalid network server type ''{0}''

Cause: An invalid value was specified for network server type.

Action: Network server type must be 'static' or 'dhcp' or 'mixed'.

PRKO-09068: Invalid port number {0}

Cause: A supplied port number was not in the valid, non-privileged range 1024-65535.

Action: Specify a port number that is bigger than 1023.