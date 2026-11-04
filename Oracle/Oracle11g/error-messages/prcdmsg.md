---
title: PRCD-01000 to PRCD-01246
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/prcdmsg.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 82 PRCD-01000 to PRCD-01246

PRCD-01000: Database {0} already exists

Cause: The specified database resource was already registered in Oracle Clusterware.

Action: No action is needed.

PRCD-01001: Database {0} does not exist

Cause: The specified database resource was not registered in Oracle Clusterware.

PRCD-01002: Database {0} is dependent upon server pool {1}

Cause: An attempt to remove the specified server pool failed because the server pool is in use.

Action: Remove the specified database before removing the server pool.

PRCD-01003: Service {0} already exists

Cause: The specified service was already created and registered in Oracle Clusterware.

Action: No action is needed.

PRCD-01004: Service {0} is dependent upon server pool {1}

Cause: An attempt to remove the specified server pool failed because the server pool is in use.

Action: Remove the specified service before removing the server pool.

PRCD-01005: Server pool {0} for the database {1} does not exist

Cause: The specified server pool used by the database was removed by force.

Action: Create the server pool using 'srvctl add srvpool'.

PRCD-01007: Failed to retrieve the database name

Cause: Failed in retrieving the DB\_NAME resource attribute.

Action: Review the accompanying error messages for details about the failure. Retry after resolving those issues.

PRCD-01008: Server parameter file does not exist for database {0}

Cause: Failed in retrieving the SPFILE resource attribute.

Action: Review the accompanying error messages for details about the failure. Retry after resolving those issues.

PRCD-01009: Failed to retrieve server parameter file of database {0}

Cause: Cannot retrieve the server parameter file for the specified database.

Action: Retry the request after ensuring that the CRS stack is running, the database resource has been configured, and the user has read permission on the database resource.

PRCD-01010: Failed to update server parameter file {0} of database {1}

Cause: Unable to update the server parameter file for the specified database.

Action: Retry the request after ensuring that the CRS stack is running, the database resource has been configured, and the user has update permission on the database resource.

PRCD-01011: Failed to identify whether this database {0} is a multi-instance database

Cause: Failed in retrieving the CLUSTER\_DATABASE resource attribute.

Action: Examine the accompanying error messages for details.

PRCD-01012: Failed to retrieve disk group list for database {0}.

Cause: Failed to retrieve the diskgroups from the start dependencies of the specified database.

Action: Examine the accompanying error messages for details. Create the diskgroup using sqlplus if the specified diskgroup does not exist. Mount the diskgroup in database which registers the diskgroup with Oracle Clusterware.

PRCD-01014: Failed to retrieve database domain of database {0}

Cause: Failed to get the domain of the specified database from its USR\_ORA\_DOMAIN attribute.

Action: Examine the accompanying error messages for details.

PRCD-01015: Combination of service cardinality {0} and TAF {1} is not allowed for service {2}

Cause: The specified service cardinality can not be used with the specified TAF policy.

Action: Change the cardinality or find a matching TAF policy. PRECONNECT can only be used with SINGLETON cardinality.

PRCD-01016: Failure encountered while accessing server pool {0} for database {1}

Cause: An attempt to look up the server pools referenced by the database SERVER\_POOLS attribute failed.

Action: Examine the accompanying error messages for details.

PRCD-01019: Failed to retrieve Oracle home of database {0}

Cause: An attempt to retrieve the TAF\_POLICY attribute of the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01020: Failed to retrieve TAF policy for service {0}

Cause: An attempt to retrieve the ORACLE\_HOME attribute of the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01021: Failed to update TAF policy {0} for service {1}

Cause: An attempt to set the TAF\_POLICY attribute of the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01022: Cannot add a second instance to a single instance database

Cause: Unable to add an instance to a single instance database.

Action: Multiple instances are not supported for a single instance database. Convert to a RAC database if multiple instances are desired.

PRCD-01023: An instance has already been added to node {0} for database {1}

Cause: Unable to add an instance to the database on the specified node because another instance has already been added to the node.

Action: Use 'srvctl modify instance' command to change the instance name on the specified node.

PRCD-01024: Failed to retrieve instance list for database {0}

Cause: An attempt to get the list of the instances for the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01025: Failed to create database {0}

Cause: An attempt to create Clusterware resources for the specified database failed. Either the request was issued by the wrong OS userid or a problem was detected inside Oracle Clusterware.

Action: Examine the accompanying error messages for details. Login in as the user of the Oracle Home to issue the command 'srvctl add database'.

PRCD-01026: Failed to create service {0} for database {1}

Cause: An attempt to create the specified service failed because the command 'srvctl add service' was not issued by the Oracle Home owner.

Action: Examine the accompanying error messages for details. Login in as the user of the Oracle Home to issue the command 'srvctl add service'.

PRCD-01027: Failed to retrieve database {0}

Cause: An attempt to get the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01028: Failed to retrieve service resource {0} for database {1}

Cause: An attempt to get the specified service failed.

Action: Examine the accompanying error messages for details.

PRCD-01029: Disk group {0} for database {1} does not exist

Cause: The disk group for the specified database does not exist.

Action: Use 'srvctl add diskgroup' to add the specified disk group.

PRCD-01030: Failed to determine whether the database {0} has cardinality

Cause: Failed to determine whether the specified database is cardinality based or not based on its VERSION attribute.

Action: Examine the accompanying error messages for details.

PRCD-01031: Failed to determine whether the service {0} has cardinality

Cause: Failed to check whether the specified service is cardinality based or not.

Action: Examine the accompanying error messages for details.

PRCD-01032: Failed to remove database resource {0}

Cause: Failed to remove the specified database.

Action: Examine the accompanying error messages for details.

PRCD-01033: The server pool of service {0} is different from the server pool of database {1}

Cause: The specified server pool is not the child of the database's server pool.

Action: Use a server pool which is the child of the database's server pool.

PRCD-01034: Database {0} is not a single instance database. It is a cluster database

Cause: The specified database is not a single instance database.

Action: Provide database name for a single instance database.

PRCD-01035: Database {0} is not a cluster database

Cause: The specified database is not a cluster database.

Action: Provide database name for a RAC database.

PRCD-01036: Failed to set Oracle home {0} for database {1}

Cause: An attempt to update Oracle home for the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01037: Failed to set Oracle home {0} for database {1} on node {2}

Cause: An attempt to update Oracle home for the specified database on the specified node failed.

Action: Examine the accompanying error messages for details.

PRCD-01038: Cannot create a RAC database {0} in a non cluster environment

Cause: Failed to create the specified RAC database because Oracle Clusterware is not installed and configured.

Action: Install and configure Oracle Clusterware before creating the RAC database.

PRCD-01039: Failed to retrieve database for service {0}

Cause: An attempt to get the database that the specified service depended on failed. This is an internal error.

Action: Contact Oracle Support Services.

PRCD-01040: Specified server pool {0} for {1} is already hosting an administrator-managed configuration for databases {2} and services {3}

Cause: Server pool is hosting administrator-managed databases and service.

Action: Specify a server pool that is not hosting an administrator-managed database and service.

PRCD-01041: The administrator-managed database {0} can have only one server pool {1}

Cause: Multiple server pools cannot be configured for an administrator-managed database

Action: Contact Oracle Support.

PRCD-01042: The database {1} is administrator-managed and a policy-managed service {0} cannot be created on it.

Cause: The specified database does not support policy-managed services.

Action: Provide a database which supports policy-managed services.

PRCD-01043: The service {0} is not a uniform or a singleton service and therefore it cannot be created as policy-managed service. This service can only be created as administrator-managed service using preferred, and optionally available instance lists.

Cause: The service to be created was an administrator-managed service and the database that the service depended on was a policy-managed database.

Action: Use perferred and available instance lists to create an adminstrator-managed service for an adminstrator-managed database.

PRCD-01044: Failed to retrieve the list of nodes where instances have been configured for database {0}

Cause: An attempt failed to get the list of nodes where the instances of the specified database were configured.

Action: Examine the accompanying error messages for details.

PRCD-01045: Database {0} is policy managed and does not support add instance option

Cause: The specified database does not support add instance option

Action: 1) Provide an administrator-managed database. -or- 2) For policy-managed database, add a server to a server pool which manages the database using 'srvctl modify srvpool' or 'srvctl relocate server'.

PRCD-01046: Database {0} is policy managed and does not support the remove instance option

Cause: The specified database does not support the remove instance option.

Action: 1) Provide an administrator-managed database. -or- 2) For policy-managed database, stop the database on a server and then remove that server from the server pool which manages the database using 'srvctl modify srvpool' or 'srvctl relocate server'.

PRCD-01047: Failed to retrieve list of services for database {0}

Cause: An attempt to get the list of services for the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01048: Cannot remove instance from the single instance database {0}

Cause: An attempt to remove the instance from the single instance database failed.

Action: Remove the database using 'srvctl remove database'.

PRCD-01049: Failed to update server pool {0} for database {1}

Cause: An attempt to update the specified server pool failed.

Action: Examine the accompanying error messages for details.

PRCD-01050: Failed to update auto start value of service {0}

Cause: An attempt to update the auto start value for the specified service failed.

Action: Examine the accompanying error messages for details.

PRCD-01051: Failed to add instance to database {0}

Cause: An attempt to add an instance to the specified database failed because the node of the instance is not a node of the cluster or other errors.

Action: Examine the accompanying error messages for details.

PRCD-01052: Failed to remove instance from database {0}

Cause: An attempt to remove the specified instance failed because the services depended on the instance or other errors.

Action: Examine the accompanying error messages for details.

PRCD-01053: Failed to retrieve the database instances providing service {0}

Cause: An attempt to get the database instances that provide the specified service failed.

Action: Examine the accompanying error messages for details.

PRCD-01054: Database name is null

Cause: The database name given by the user is null.

Action: Provide a valid database name that is not a null string.

PRCD-01055: Instance name is null

Cause: The instance name given by the user is null.

Action: Provide a valid instance name that is not a null string.

PRCD-01056: Database name {0} contains invalid characters

Cause: The supplied database name contains invalid characters.

Action: Supply a valid database name. The valid character set for database name is \[a-zA-Z0-9$#\_\].

PRCD-01057: Instance name {0} is not valid

Cause: The supplied instance name is not of the correct format.

Action: Supplied a valid instance name. The valid character set for instance name is \[a-zA-Z0-9\_-\].

PRCD-01058: Invalid server pool list {0} supplied for single instance database {1}

Cause: The server pool size was not one when creating a single instance database on a cluster.

Action: Use one server pool with only one server when creating the single instance database.

PRCD-01059: Instance name prefix {0} contains illegal characters

Cause: The supplied instance name prefix contained non-alphanumeric characters.

Action: Supply an instance name prefix that consists of alphanumeric characters a-z, A-Z, and 0-9.

PRCD-01060: Server pool has not been supplied for creating cluster service {0} for database {1}

Cause: No server pool argument has been supplied when configuring a cluster database.

Action: Supply an existing server pool when configuring a cluster database.

PRCD-01061: No database exists

Cause: No database has been configured.

Action: Configured database and retry.

PRCD-01062: Invalid service cardinality {0}

Cause: The service cardinality supplied is not valid.

Action: Supply a valid service cardinality.

PRCD-01063: Invalid service taf policy {0}

Cause: The service taf policy supplied is not valid.

Action: Supply a valid service taf policy.

PRCD-01064: Invalid database role {0}

Cause: The database role supplied is not valid.

Action: Supply a valid database role.

PRCD-01065: Invalid managment policy {0}

Cause: The management policy supplied is not valid.

Action: Supply a valid management policy. The management policy should be automatic or manual.

PRCD-01066: Invalid start option {0}

Cause: The start option supplied is not valid.

Action: Supply a valid start option.

PRCD-01067: Invalid stop option {0}

Cause: The stop option supplied is not valid.

Action: Supply a valid stop option.

PRCD-01068: Failed to modify instance {0} on node {1} for database {2}

Cause: The instance for the specified node does not exist on the database.

Action: Use srvctl add instance to add the per-X instance.

PRCD-01069: Failed to modify instance {0} on node {1} for database {2}

Cause: The instance for the specified node cannot not be updated.

Action: Make sure that the crs stack is up and running; the oracle user has the permission to modify the instance; and then retry.

PRCD-01070: Failed to retrieve startup options for database {0}

Cause: Unable to retrieve the startup options for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01071: Failed to update startup options for database {0}

Cause: Unable to update the startup options for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01072: Failed to retrieve stop options for database {0}

Cause: Unable to retrieve the stop options for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01073: Failed to update stop options for database {0}

Cause: Unable to update the stop options for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01074: Failed to retrieve the database role for database {0}

Cause: Unable to retrieve the database role for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01075: Failed to set the database role {1} for database {0}

Cause: Unable to update the database role for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01076: Failed to retrieve the management policy for database {0}

Cause: Unable to retrieve the management policy for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01077: Failed to update the management policy for database {0}

Cause: Unable to update the managment policy for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01078: Failed to update the db name {0} of database {1}

Cause: Unable to update the db name for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01079: Failed to update pullup for service {0}: {1}

Cause: Failed to update pullup modifier for the service.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01080: Failed to get attributes for service {0}

Cause: Failed to get attributes for the service.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01081: Failed to set attributes for service {0}

Cause: Failed to set attributes for the service.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01082: Failed to modify service {0}: Unsupported attribute {1}

Cause: Operation doesn't support modification of attribute.

Action: Fix your application.

PRCD-01083: Failed to modify service {0}

Cause: Failed to modify service.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01084: Failed to start service {0}

Cause: Failed to start the service.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01085: Failed to stop service {0}

Cause: Failed to stop the service.

Action: Make sure that the crs stack is up, the service is running and then retry.

PRCD-01086: Invalid rlb goal {0}

Cause: The rlb goal supplied is not valid.

Action: Supply a valid rlb goal.

PRCD-01087: Invalid failover type {0}

Cause: The failover type supplied is not valid.

Action: Supply a valid failover type.

PRCD-01088: Invalid connection load balancing goal {0}

Cause: The clb goal supplied is not valid.

Action: Supply a valid clb goal.

PRCD-01089: Invalid failover method {0}

Cause: The failover method supplied is not valid.

Action: Supply a valid failover method.

PRCD-01090: Failed to retrieve Oracle home of database {0} on node {1}

Cause: No Oracle home of the database has been set on the specified node.

Action: Set the Oracle home of the database on the specified node.

PRCD-01091: Failed to create database instance {0} for database {1}

Cause: Unable to create database instance for the specified instance name.

Action: Make sure that the local node can be used for creating a database instance; the instance name provided is valid. The valid character set for instance name is \[a-zA-Z0-9\_-\].

PRCD-01092: Failed to create database instance {0} for database {1} on node {2}

Cause: Unable to create database instance for the specified instance name and node name.

Action: Make sure that the specified node can be used to create a database; the instance name provided is valid. The valid character set for instance name is \[a-zA-Z0-9\_-\].

PRCD-01093: Failed to update the domain {0} of database {1}

Cause: Unable to update the domain for the database.

Action: Make sure that the crs stack is up and running and then retry.

PRCD-01094: Failed to create start dependency for database {0} on the ASM cluster filesystem where ACFS path {1} resides

Cause: Unable to modify the database resource to include a start dependency on the ASM cluster filesystem for the ACFS path.

Action: Make sure that the ASM instance is running, the OFS driver exists in the driver directory, and the underlying ofs devices are accessible.

PRCD-01095: Failed to retrieve databases for version 11.1 and earlier

Cause: Unable to read OCR configuration to get databases for version 11.1 and earlier

Action: Make sure that the Oracle clusterware is up and running and the primary group of the user running srvctl is the same as the primary group of the user who installed the Oracle clusterware home. Also, run 11.1 srvctl config to verify that the database configuration exists in OCR.

PRCD-01096: Failed to retrieve the database unique name

Cause: Unable to read the attribute value for database unique name.

Action: Make sure that the Oracle clusterware is up and running and then retry.

PRCD-01097: Failed to retrieve the active servers of server pool {0} for database {1}

Cause: Unable to read the active servers attribute value for the database underlying server pools.

Action: Make sure that the Oracle clusterware is up and running; the database underlying server pools exist; the user has the permission to access the database underlying server pools and then retry.

PRCD-01098: Failed to retrieve the configured servers of server pool {0} for database {1}

Cause: Unable to read the servers attribute value for the database underlying server pool.

Action: Make sure that the Oracle clusterware is up and running; the database underlying server pool exists and then retry.

PRCD-01099: {0} enum member has a constant value that cannot be changed to given value {1}

Cause: An attempt was made to change value of read-only valued enum member.

Action: Contact Oracle Support Services.

PRCD-01100: Invalid relocate option {0}

Cause: Supplied relocate option is unknown.

Action: Contact Oracle Support Services.

PRCD-01101: Failed to remove running instance {0} for database {1}

Cause: Unable to remove the instance configuration for the database because the instance was still running.

Action: Stop the running instance using srvctl stop instance command and then retry.

PRCD-01102: Failed to create preconnect service for service {0}

Cause: An attempt to register service failed due to failure to register its corresponding preconnect service.

Action: Contact Oracle Support Services.

PRCD-01103: Failed to retrieve the maximum cardinality for database {0}

Cause: Unable to query the number of servers in the server pool used to manage the database.

Action: Make sure that the Oracle clusterware is up and running; the database underlying server pool exists and then retry.

PRCD-01104: A source server must be specified to relocate cluster database {0}

Cause: Cluster database cannot be relocated without specifying source server to relocate instance from.

Action: Supply source and target servers for database relocation.

PRCD-01105: A source server must be specified to relocate service {0}

Cause: Cluster database service cannot be relocated without specifying source server to relocate service member from.

Action: Supply source and target servers for service relocation.

PRCD-01106: Failed remove service {0}: could not get data for its underlying server pool

Cause: Server pool data is not found.

Action: Make sure that the Oracle clusterware is up and running; the service underlying server pool exists.

PRCD-01107: Removed service {0} but failed to remove its underlying server pool {1}

Cause: Failed to remove the server pool.

Action: Make sure that the Oracle clusterware is running and remove the server pool manually.

PRCD-01108: Failed to identify whether database {0} is an administrator-managed database

Cause: Failed to get database attributes.

Action: Make sure that the Oracle clusterware is up and running; the database exists.

PRCD-01109: Failed to find administrator-managed service {0} of database {1} because the database is a policy-managed database.

Cause: The database does not support administrator-managed services.

Action: Provide an administrator-managed database and make sure that the service exists within that database.

PRCD-01110: Database {0} does not have instances {1}

Cause: The database does not have instances mentioned in the message.

Action: Make sure that database name is correct and the database has requested instances.

PRCD-01111: The type of service cardinality for this operation should be {1}, not {0}

Cause: This is an internal error.

Action: Contact Oracle Support Services.

PRCD-01112: Failed to get preferred instances of service {0}

Cause: The service does not exist or the Oracle clusterware is down.

Action: Make sure that the Oracle clusterware is up and running and the service exists.

PRCD-01113: Failed to modify service {0}

Cause: The service does not exist or the Oracle clusterware is down.

Action: Make sure that the Oracle clusterware is up and running and the service exists.

PRCD-01114: Failed to enable service {0} on one or more instances

Cause: The service does not exist or enabled on all database instances. The Oracle clusterware is down.

Action: make sure that the Oracle clusterware is up and running; the service exists and disabled on at least one database instance.

PRCD-01115: Failed to disable service {0} on one or more instances

Cause: The service does not exist or disabled on all database instances. The Oracle clusterware is down.

Action: Make sure that the Oracle clusterware is up and running; the service exists and enabled on at least one database instance.

PRCD-01116: Failed to get available instances of service {0}

Cause: The service does not exist or the Oracle clusterware is down.

Action: Make sure that the Oracle clusterware is up and running and the service exists.

PRCD-01117: Failed to modify service {0}, the service should have at least one preferred instance

Cause: An attempt was made to remove all preferred instances of the service.

Action: Make sure that there is at least one instance provided in the service preferred instance list.

PRCD-01118: Failed to set service {0} to {1} because it runs on more than one node

Cause: The service was running on more than one node.

Action: Make sure that the service is not running or running on one node only.

PRCD-01119: Failed to create database {0} because the database unique name matches that of database {1} in the first 8 characters

Cause: The database unique name is not unique in the first 8 characters. It is a requirement because the name is used to generate ORACLE\_SID.

Action: Ensure that the name supplied to either DBCA or srvctl during database creation is sufficiently unique, and retry the command.

PRCD-01120: The resource for database {0} could not be found.

Cause: The resource for the specified database name could not be found. Either the database name was misspelled or the database has not been created.

Action: Correct the database name spelling or use the 'srvctl add database' command to create the database configuration.

PRCD-01121: Specified server pool {0} for {1} is already hosting an administrator-managed configuration for database(s) {2}

Cause: Server pool is hosting administrator-managed databases.

Action: Specify a server pool that is not hosting an administrator-managed database.

PRCD-01122: Specified server pool {0} for {1} is already hosting an administrator-managed configuration for service(s) {2}

Cause: Server pool is hosting administrator-managed services.

Action: Specify a server pool that is not hosting an administrator-managed service.

PRCD-01123: Oracle Clusterware resource does not exist for ACFS filesystem of volume device {0}. A resource is required for the filesystem containing ACFS path {1}.

Cause: The resource for the filesystem did not exist for the database which has its dependency on the ACFS path. A resource is required for path used by the database on ACFS filesystems so that Oracle Clusterware can track the database's dependency on the filesystem. Database's dependent ACFS paths cannot be mounted via the ACFS registry.

Action: Add the resource with 'srvctl add filesystem'.

PRCD-01124: Failed to stop database {0} and its services

Cause: Attempt to stop the database has failed.

Action: Ensure that user attempting to stop the database has execute privileges on the database resource. Also, review the accompanying error messages for details about failure to stop database. Retry after resolving those issues or contact Oracle Support Services.

PRCD-01125: Failed to create dependency from database {0} to its Oracle home {1} that is located on the ASM cluster filesystem

Cause: An attempt to modify the database resource to include a stop dependency on the ASM cluster filesystem for the database's Oracle home failed.

Action: Make sure that the asm instance is running; the ACFS driver exists in the driver directory and the underlying ACFS devices are accessible.

PRCD-01126: Instance {0} cannot be removed because it is the only preferred instance for service(s) {1} for database {2}

Cause: An attempt was made to remove the instance which is the only preferred instance for specified services.

Action: Make sure that specified services have more than one preferred instance or modify services to not have the instance as a preferred instance.

PRCD-01127: Failed to verify if instance {0} is the only preferred instance for any service

Cause: An attempt to verify if the instance is the only preferred instance for any service failed.

Action: Make sure that the Oracle clusterware is up and running. Also, review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01128: Failed to remove all services configured for database {0}

Cause: An attempt to remove all services configured for database.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01129: Failed to start instance {0} for database {1}

Cause: An attempt to start an instance with the specified name failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01130: Failed to convert administrator-managed database {0} into a policy-managed database to use server pool {1}

Cause: An attempt to convert the database from an administrator-managed configuration to a policy-managed configuration failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01131: Failed to stop database {0} and its services on node(s) {1}

Cause: Attempt to stop the database on given nodes has failed.

Action: Ensure that user attempting to stop the database has execute privileges on the database resource. Also, review the accompanying error messages for details about failure to stop database. Retry after resolving those issues or contact Oracle Support Services.

PRCD-01132: Database {0} doesn't have defined service(s) {1}

Cause: An attempt to start/stop services on the given database failed.

Action: Make sure that every service you want to start or stop is configured for the given database.

PRCD-01133: Failed to start services for database {0}

Cause: An attempt to start given services on the given database failed because those service(s) are not configured for the database.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01134: Failed to find any listener defined for network {0}

Cause: An attempt to find listener(s) defined for specified network failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01135: There is no listener defined for network {0} to be used by service {1}

Cause: An attempt to create a service failed because provided network doesn't have listener to publish a service on that network.

Action: Make sure that the provided network has a listener.

PRCD-01136: Failed to retrieve type of the database {0}

Cause: An attempt to query the type of database has failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01137: Failed to retrieve online relocation timeout for RAC One Node database {0}

Cause: An attempt to query the current online relocation timeout for RAC One Node database has failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01138: Failed to set online relocation timeout to {0} for RAC One Node database {1}

Cause: An attempt to update the online relocation timeout for RAC One Node Database has failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01139: The current server {0} where RAC One Node database {1} is running is not in the given candidate server list {2}

Cause: An attempt to update the candidate servers of the server pool hosting RAC One Node Database has failed because current server where this database is running is not in the given candidate server list.

Action: Retry the operation after either including the current server where this database is running in the given candidate server list or stopping the database.

PRCD-01140: Failed to update candidate servers to {0} of the server pool hosting RAC One Node database {1}

Cause: An attempt to update the candidate servers of the server pool hosting RAC One Node Database has failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01141: The database {0} is not hosted by a server pool

Cause: An attempt to query the server pool for given database failed because this database is not hosted by a server pool. This is most likely due to a program calling cluster environment API in Oracle Restart environment.

Action: Examine the accompanying error messages for details and contact Oracle Support Services.

PRCD-01142: The {0} TAF policy is not valid for RAC One Node service {1}

Cause: A TAF policy other than BASIC or NONE was specified for RAC One Node service.

Action: Specify BASIC or NONE TAF policy and retry the operation.

PRCD-01143: The cardinality of {0} is not valid for RAC One Node database or service {1}

Cause: An invalid cardinality was specified for RAC One Node database or service.

Action: Specify a SINGLETON cardinality and retry the operation.

PRCD-01144: The {0} management policy is not valid for RAC One Node database {1}

Cause: A management policy other than AUTOMATIC was specified for RAC One Node database.

Action: Specify AUTOMATIC management policy and retry the operation.

PRCD-01145: {0} API is not supported on RAC One Node database environment

Cause: Internal error.

Action: Contact Oracle Support Services.

PRCD-01146: Database {0} is not a RAC One Node database

Cause: The specified database is not a RAC One Node database.

Action: Provide database name for a RAC One Node database.

PRCD-01147: The server pool {0} of administrator-managed database {1} has no candidate servers

Cause: Either no instance had been added to the database or this database's server pool was altered inapproprately.

Action: If no instance was added to the database yet, try to add an instance to this database, for example by using 'srvctl add instance' command, and then retry. Otherwise, contact Oracle Support Services.

PRCD-01148: Failed to convert the configuration of RAC One Node database {0} into its equivalent configuration for RAC database

Cause: Internal error.

Action: Review the accompanying error messages and contact Oracle Support Services.

PRCD-01149: AUTOMATIC management policy cannot be used for the service {0} when the database {1} is not AUTOMATIC

Cause: An attempt to create/modify a service failed because the management policy specified for the service is AUTOMATIC but the database's management policy is not AUTOMATIC.

Action: Make sure that the provided service's management policy is MANUAL or NORESTART when running 'srvctl add service' or 'srvctl modify service' command.

PRCD-01150: Failed to retrieve EDITION for service {0}

Cause: An attempt to retrieve the EDITION attribute of the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01151: Failed to convert the configuration of RAC One Node database {0} into its equivalent RAC database configuration because RAC One Node database is running on a different server {1} than the given target server {2}

Cause: A target server was specified that was different from the server where the RAC One Node database is running.

Action: Either supply the server where RAC One Node Database is running now as target server or stop the database and retry.

PRCD-01152: Failed to update instance name {0} for database {1}

Cause: An attempt to update instance name for the specified database failed.

Action: Examine the accompanying error messages for details.

PRCD-01153: Failed to convert the configuration of cluster database {0} into its equivalent RAC One Node database configuration

Cause: An attempt to convert the specified cluster database to RAC One Node database failed.

Action: Review the accompanying error messages and retry after resolving these errors or contact Oracle Support Services.

PRCD-01154: Failed to convert the configuration of cluster database {0} into its equivalent RAC One Node database configuration because cluster database is running on more than one server {1}

Cause: User attempted conversion of a cluster database to RAC One Node database that was running on more than one servers.

Action: Stop this database on all but one server and retry.

PRCD-01155: Failed to convert the configuration of cluster database {0} into its equivalent RAC One Node database configuration because cluster database has more than one server pool {1} to control its placement

Cause: User attempted conversion of a cluster database that had more than one server pool to control its placement.

Action: Update configuration of this database by either 'srvctl modify database' or if this database has services that are in their own respective server pool, then removing all but one of its services via 'srvctl remove service' and then retry.

PRCD-01156: Failed to convert the configuration of cluster database {0} into its equivalent configuration for RAC One Node database due to its services {1} having {2} TAF policy

Cause: This database has services that have TAF policy (e.g. PRECONNECT) that is not supported by RAC One Node Database.

Action: Either modify the TAF policy of these services to either BASIC or NONE using 'srvctl modify service' or remove these services using 'srvctl remove service' and then retry.

PRCD-01157: Failed to convert the configuration of cluster database {0} into its equivalent configuration for RAC One Node database because none of its services have {1} management policy

Cause: An attempt to convert a cluster database configuration into its equivalent configuration for RAC One Node database was rejected because all services of the given database have MANUAL management policy.

Action: Modify the management policy of at least one of these services to AUTOMATIC using 'srvctl modify service... -y AUTOMATIC' command and then retry.

PRCD-01158: Invalid database type {0}

Cause: The database type supplied is not valid.

Action: Supply a valid database type.

PRCD-01159: Target node must be specified when initiating an online relocation of administrator managed RAC One Node database {0}

Cause: The target node was not specified when requesting online relocation on administrator managed RAC One Node database.

Action: Use 'srvctl relocate database' command with -n option.

PRCD-01160: Online relocation request for RAC One Node database {0} was rejected because this database is not running

Cause: RAC One Node database was not running.

Action: Start the database by issuing the 'srvctl start database' command and then retry.

PRCD-01161: Online relocation failed for RAC One Node database {0}

Cause: Online relocation of the given database was unsuccessful.

Action: Either run 'srvctl relocate database -a' command to abort the online relocation or run 'srvctl relocate database -n' command to perform online relocation of the database to the given target node.

PRCD-01162: Invalid online relocation status {0}

Cause: This is an internal error.

Action: Review the accompanying error messages and contact Oracle Support Services.

PRCD-01163: Failed to modify database {0}

Cause: Failed to modify database.

Action: Make sure that the CRS stack is up and running and then retry.

PRCD-01164: An online relocation request for RAC One Node database {0} is already active

Cause: The given database has an already active online relocation request.

Action: Either specify another database in the 'srvctl relocate database' command or abort the in-progress request with 'srvctl relocate database -a' command.

PRCD-01165: An online relocation request for RAC One Node database {0} has failed

Cause: An online relocation request for the database has failed and the supplied target node was not the same as that in the failed request.

Action: Use 'srvctl status database' command to query the target node of the failed online relocation request. Either run 'srvctl relocate database -a' command to abort the failed request or 'srvctl relocate database -n' command with with the correct target node.

PRCD-01166: The supplied node {0} is not available in the {1} server pool

Cause: Supplied node was not in the Free server pool.

Action: Supply node from the Free server pool.

PRCD-01175: Failed to determine the status of the online relocation request for RAC One Node database {0}

Cause: Unable to determine the status of the online relocation request for given RAC One Node database.

Action: Examine the accompanying error messages for details.

PRCD-01176: Invalid online relocation state {0}

Cause: This is an internal error.

Action: Review the accompanying error messages and contact Oracle Support Services.

PRCD-01177: Failed to abort the online relocation request for RAC One Node database {0}

Cause: Failed to abort the online relocation of the RAC One Node database.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01178: A failed online relocation request for RAC One Node database {0} does not exist

Cause: The supplied RAC One Node database does not have a failed online relocation request.

Action: Supply a RAC One Node database that has a failed online relocation request.

PRCD-01179: The online relocation timeout value {0} is not within the range of between {1} and {2}

Cause: The specified online relocation timeout value was not within the required range.

Action: Supply a value within the required range.

PRCD-01180: Configuration of database {0} has already been upgraded to version {1}

Cause: The supplied database was already upgraded.

Action: Supply a database of a lower version.

PRCD-01181: Failed to upgrade configuration of services {0} to version {1}

Cause: Failed to upgrade the service configuration.

Action: Review the accompanying error messages. If you are unable to resolve the problem, contact Oracle Support Services.

PRCD-01182: Failed to upgrade configuration of database {0} to version {1}

Cause: Failed to upgrade the database configuration.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01183: Failed to upgrade configuration of service type to version {0}

Cause: Failed to upgrade the service type configuration.

Action: Review the accompanying error messages and contact Oracle Support Services.

PRCD-01184: Failed to upgrade configuration of database type to version {0}

Cause: Failed to upgrade the database type configuration.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01185: Failed to retrieve service resource {0} for non cluster database {1}

Cause: An attempt to get the specified service failed because the database provided is a single instance and not a cluster database.

Action: Make sure that Oracle Clusterware is configured, specify a service defined for cluster database, and then retry.

PRCD-01186: TAF policy 'PRECONNECT' cannot be used to add a service for single instance database {0}

Cause: Failed to create a service because provided TAF specification can not be used with a single instance database.

Action: Retry after removing 'PRECONNECT' TAF policy.

PRCD-01187: Failed to enable or disable service {0} on particular nodes for non-cluster single instance database {1}

Cause: An attempt to enable or disable the service on particular nodes for single instance database failed. Such enable or disable operations are not applicable to services defined for single instance databases in Oracle Restart.

Action: Specify a service defined for database which is running on cluster or do not specify nodes.

PRCD-01188: Failed to detect whether the standby database {0} supports the Data Guard protection mode

Cause: An attempt has failed to determine whether the standby database supports the configured Data Guard protection mode.

Action: Review the accompanying error messages for details about the failure and retry the command after resolving those issues.

PRCD-01189: Cannot update server pool to {0} for RAC One Node database service {1}

Cause: Attempt to update server pool of a RAC One Node database service was rejected because placement of this service is controlled by the server pool hosting the underlying database.

Action: Try updating the server pool controlling the placement of the database via 'srvctl modify database' command or its equivalent.

PRCD-01190: Cannot update server pool to {0} for single instance database service {1}

Cause: Attempt to update server pool of a single instance (non-RAC) database service was rejected because placement of this service is controlled by the server pool hosting the underlying database.

Action: Try updating the server pool controlling the placement of the database via 'srvctl modify database' command or its equivalent.

PRCD-01191: Cannot update server pool to {0} for database service {1}

Cause: Attempt to update server pool of database service was rejected because a subpool server pool was specified.

Action: Supply a first-level server pool that is not a subpool of any other server pool and retry the operation.

PRCD-01192: The cardinality {0} is not valid for single instance database service {1}

Cause: An invalid cardinality was specified for single instance (non-RAC) database.

Action: Retry after specifying a SINGLETON cardinality in 'srvctl modify service' command or its equivalent.

PRCD-01193: Service {0} defined for RAC One Node database {1} cannot be started on more than one node

Cause: An attempt to start the specified service failed because RAC One Node service cannot be started on more than one node.

Action: Retry after specifying one node to start the service on.

PRCD-01194: Failed to retrieve the version of database {0}

Cause: An attempt to retrieve the VERSION resource attribute has failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01195: Option to remove the target node was not allowed for aborting online relocation of policy-managed RAC One Node database {0}

Cause: Option -r was specified in a request to abort online relocation on policy managed RAC One Node database.

Action: Use 'srvctl relocate database -a' command without -r option.

PRCD-01196: 'PRECONNECT' TAF policy cannot be used to create service {0} on policy managed database {1}

Cause: Failed to create a service because a policy managed database cannot have service with PRECONNECT TAF policy.

Action: Retry after supplying 'BASIC' or 'NONE' TAF policy.

PRCD-01197: The database {0} is policy-managed and an administrator-managed service {1} cannot be created on it

Cause: The specified database does not support administrator-managed services.

Action: Provide a database which supports administrator-managed services.

PRCD-01198: Failed to add service {0} to database {1} because database is already at maximum services limit of {2}

Cause: Attempt to add a new service to database was rejected because database has already reached the maximum services limit.

Action: Retry after removing a service from this database via 'srvctl remove service' command, or contact Oracle Support Services.

PRCD-01199: The stop request on instance {0} of standby database {1} was rejected to prevent termination of the primary database

Cause: The attempt to stop this instance of the standby database was rejected because the configured Data Guard protection mode required this instance to be running to prevent termination of the primary database.

Action: Retry the stop request after stopping the primary database or downgrading the protection mode.

PRCD-01200: Configuration of database {0} has already been downgraded to version {1} for database {2}

Cause: The supplied database was already downgraded.

Action: Supply a database of a higher version.

PRCD-01201: Downgrade from current version {0} to version {1} is not supported for database {2}

Cause: An unsupported version was specified for downgrading the database.

Action: Check that the versions provided are correct.

PRCD-01202: Failed to downgrade configuration of services {0} to version {1}

Cause: A request to downgrade the service configuration failed.

Action: Review the accompanying error messages. If you are unable to resolve the problem, contact Oracle Support Services.

PRCD-01203: Failed to downgrade configuration of database {0} to version {1}

Cause: A request to downgrade the database configuration failed.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01204: Failed to update administrator-managed database {0} to use server pool {1}

Cause: Attempt to update administrator-managed database was rejected because administrator-managed database cannot be moved to another subpool.

Action: Retry after supplying a first-level server pool in 'srvctl modify database' command to convert administrator-managed database to policy-managed database.

PRCD-01205: Failed to update policy-managed database {0} to use server pools {1}

Cause: Attempt to update policy-managed database was rejected because specified server pools do not include all server pools hosting services of this database.

Action: Either include all server pools hosting services of this database in the supplied server pool list or specify one server pool to move all services into one server pool in 'srvctl modify database' command and retry.

PRCD-01206: Failed to retrieve preferred instance of service {0} of RAC One Node database {1}

Cause: Attempt to retrieve preferred instance of service belonging to RAC One Node database failed because database is either in failed online relocation state or undergoing online relocation.

Action: Check the status of online relocation via 'srvctl status database' command. If online relocation status is reported as active, then retry after online relocation completes. If online relocation status is reported as failed, then repair the configuration via 'srvctl relocate database... -a' command and then retry.

PRCD-01207: The start options {2} can not be used while starting service {0} and its database {1}

Cause: An attempt to start the service was rejected because the specified start options can not be used with service when the databse is not running.

Action: Remove the specified start options and then retry.

PRCD-01208: The start options {1} can not be used while starting services for database {0}

Cause: An attempt to start the services was rejected because the specified start options can not be used with services when the databse is not running.

Action: Remove the specified start options and then retry.

PRCD-01209: RAC One Node database {0} does not have enough servers in its server pool {1} to initiate an online relocation

Cause: Online relocation request was rejected because there were less than two servers in the server pool of the specified RAC One Node database.

Action: Make sure that the minimum and maximum size of the server pool are set properly.

PRCD-01210: The service name {0} cannot be same as the database default service name {1}

Cause: An attempt to create the service was rejected because the given service name is same as the database default service name.

Action: Retry after supplying a service name that is different than the database default service name.

PRCD-01211: Cannot start RAC One Node database {0} because a failure has occurred while trying to clean up an earlier failed online relocation

Cause: An attempt to start a RAC One Node database was rejected because a failure has occurred while trying to clean up an earlier failed online relocation.

Action: Use 'srvctl status database' command to query the target node of the failed online relocation process. Either run 'srvctl relocate database' with -a option or with -n option with the target node thus discovered.

PRCD-01212: An instance with name "{0}" already exists on node {1}

Cause: Unable to add an instance to the database on the specified node because an instance with the same name was found on another node.

Action: Use 'srvctl modify instance' command to change the name of the existing instance, or use a different instance name in the 'srvctl add instance -i \<inst>' command.

PRCD-01213: Service {0} of database {1} is still running

Cause: An attempt to remove RAC One Node service failed because the given service was still running.

Action: Stop the service and then retry the command.

PRCD-01214: Administrator-managed RAC database {0} has more than one instance

Cause: Failed to convert RAC database to RAC One Node database because there was more than one instance.

Action: Use 'srvct remove instance' command to remove all but one instance and then run 'srvctl convert database -c RACONENODE'.

PRCD-01215: Unable to downgrade RAC One Node database {0}

Cause: Failed to downgrade RAC One Node database to an earlier version because there was no RAC One Node specific configuration in the earlier version.

Action: None

PRCD-01222: Online relocation of database "{0}" failed but database was restored to its original state

Cause: Online relocation of the given database was unsuccessful, therefore the database was restored to its original state.

Action: See accompanying messages for online relocation failure.

PRCD-01223: The service name {0} contains illegal characters {1}

Cause: An attempt to create the service was rejected because the given service name contains illegal characters.

Action: Retry after supplying a service name that contains characters from its character set ({a-zA-Z0-9\_} for the base name, and {a-zA-Z0-9\_$#} for the domain name if needed)."

PRCD-01224: The {0} management policy is not valid for RAC One Node database service {1}

Cause: A management policy other than AUTOMATIC was specified for RAC One Node database service.

Action: Either specify AUTOMATIC management policy for this service or modify management policy of another service of this database to AUTOMATIC, such as via 'srvctl modify service' command, and then retry the current operation.

PRCD-01225: An attempt to remove service {0} of database {1} was rejected because this is the last service with {2} management policy. A RAC One Node database must have at least one service with {2} management policy.

Cause: An attempt was made to remove the last service of a RAC One Node database having AUTOMATIC management policy.

Action: Add another service with AUTOMATIC management policy, for example by using 'srvctl add service... -y AUTOMATIC' command, or modify the management policy of an existing service to AUTOMATIC, using 'srvctl modify service' command, before removing the given service.

PRCD-01226: Failed to retrieve ASM Cluster Filesystem resource {0} for database {1}.

Cause: The ASM Cluster Filesystem resource was not registered in Oracle Clusterware.

Action: Create the ASM Cluster Filesystem resource using 'srvctl add filesystem' command and then retry.

PRCD-01227: Failed to retrieve ASM Cluster Filesystem list for database {0}.

Cause: Failed to retrieve the ASM Cluster Filesystems of the specified database.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01228: Failed to convert administrator-managed RAC database {0} to RAC One Node database because the database had no instance added

Cause: Attempt to convert RAC database to RAC One Node database was rejected because database did not have any instance added.

Action: Use 'srvct add instance' command to add an instance and then run 'srvctl convert database -c RACONENODE'.

PRCD-01229: An attempt to access configuration of database {0} was rejected because its version {1} differs from the program version {2}. Instead run the program from {3}.

Cause: An attempt was made to access configuration of database that is of different version than that of the program.

Action: Make sure that database configuration version and the program version are same and then retry. For example, try the operation using srvctl from the ORACLE\_HOME mentioned in the error message.

PRCD-01230: Failed to modify database {0} to use server pool {1}

Cause: An attempt to modify the database to use the given server pool has failed.

Action: Review the accompanying error messages for details about the failure. For example, a failure could happen if the database owner does not have execute permissions on the given server pool. In this case, use 'srvctl config database -d <db\_unqiue\_name>' command to find out the database owner's username, create a server pool as that user, and then supply that server pool as argument when retrying the command.

PRCD-01231: Failed to upgrade configuration of database {0} to version {1} in new Oracle home {2}

Cause: Failed to upgrade the database configuration.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01232: Failed to upgrade configuration of database {0} because database version {1} is an unsupported version for upgrade

Cause: Version of the database was not supported for upgrade.

Action: None

PRCD-01233: Failed to downgrade configuration of database {0} to version {1} in new Oracle home {2}

Cause: Failed to downgrade the database configuration.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01234: Failed to downgrade configuration of database {0} to version {1} because the specified version is unsupported for downgrade

Cause: Specified version was not supported for downgrade.

Action: Specify a version that is 10.1 or later.

PRCD-01235: Unable to downgrade configuration of single instance database {0} to version {1}

Cause: Single instance database was specified.

Action: Remove the single instance database configuration. 11.2 Clusterware cannot manage pre-11.2 single instance databases.

PRCD-01236: Unable to downgrade configuration of RAC One Node database {0} to version {1}

Cause: RAC One Node database was specified.

Action: Convert the administrator-managed RAC One Node database to an administrator-managed RAC database using 'srvctl convert database' command and then retry.

PRCD-01237: Unable to downgrade configuration of policy-managed RAC database {0} to version {1}

Cause: Policy-managed RAC database was specified.

Action: Remove the 11.2 database configuration and use pre-11.2 srvctl to re-create the configuration.

PRCD-01238: Failed to get attributes for database {0}

Cause: Failed to get attributes for the database.

Action: Make sure that the CRS stack is up and running and then retry.

PRCD-01239: Failed to downgrade configuration of database {0} to version {1} because the database has dependency on ASM Cluster File System

Cause: Specified database was dependent on ASM Cluster File System.

Action: None

PRCD-01240: Unable to downgrade configuration of database {0} because its database role of {1} is not supported in version {2}

Cause: Database role of specified database was not supported in the specified version.

Action: Modify the database role using 'srvctl modify database' command and then retry this command.

PRCD-01241: Failed to upgrade configuration of database {0} to version {1} in new Oracle home {2}. Also failed to remove the internal server pool configuration.

Cause: Failed to upgrade the database configuration.

Action: Review the accompanying error messages for details about failure. Retry after resolving those issues.

PRCD-01242: Unable to convert RAC database {0} to RAC One Node database because the database had no service added

Cause: Attempt to convert RAC database to RAC One Node database was rejected because the database did not have any service configured. A RAC One Node database must always have one service.

Action: Use 'srvct add service' command to add a service and then run 'srvctl convert database -c RACONENODE'.

PRCD-01243: Failed to start instance {0} of database {1} because an instance having same name was already running on node {2}

Cause: An attempt to start an instance with the given name was rejected because another instance with same name was already running on another node.

Action: Either supply a different instance name or stop the running instance with the same name and then retry.

PRCD-01244: Failed to start service {0} of RAC One Node database {1} on the given node {2} because the database was running on node {3}

Cause: An attempt to start the specified service on the given node was rejected because RAC One Node database is running on a node different than the given node.

Action: Either omit the node option or supply the node where the database is running.

PRCD-01245: Addition of database version {0} is not allowed using srvctl version {1}

Cause: The versions of srvctl used and database to be created did not match.

Action: Use the same version of srvctl as database.

PRCD-01246: Online relocation of RAC One Node Data Guard standby database "{0}" was rejected because the database is in Data Guard maximum protection mode

Cause: An online relocation request was rejected because the specified database is operating in Data Guard maximum protection mode.

Action: Downgrade the protection mode to maximum availability and retry the online relocation.