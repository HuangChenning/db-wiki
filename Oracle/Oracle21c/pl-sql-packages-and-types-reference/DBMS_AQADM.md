---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_AQADM.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 25 DBMS\_AQADM

The `DBMS_AQADM` package provides procedures to manage Oracle Database Advanced Queuing (AQ) configuration and administration information.

This chapter contains the following topics:

### 25.1 DBMS\_AQADM Security Model

Initially, only `SYS` and `SYSTEM` have execution privilege for the procedures in `DBMS_AQADM` and `DBMS_AQ`. Users who have been granted `EXECUTE` rights to `DBMS_AQ` and `DBMS_AQADM` are able to create, manage, and use queues in their own schemas. The `MANAGE_ANY` AQ system privilege is used to create and manage queues in other schemas and can be granted and revoked through `DBMS_AQADM.GRANT_SYSTEM_PRIVILEGE` and `DBMS_AQADM.REVOKE_SYSTEM_PRIVILEGE` respectively. Starting from Oracle Database 12c Release 2, `MANAGE_ANY` privilege will not allow access to `SYS` owned queues by users other than `SYS`.

User Roles

The database administrator has the option of granting the system privileges `ENQUEUE_ANY` and `DEQUEUE_ANY`, exercising `DBMS_AQADM.GRANT_SYSTEM_PRIVILEGE` and `DBMS_AQADM.REVOKE_SYSTEM_PRIVILEGE` directly to a database user, if you want the user to have this level of control.

The application developer gives rights to a queue by granting and revoking privileges at the object level by exercising `DBMS_AQADM.GRANT_QUEUE_PRIVILEGE` and `DBMS_AQADM.REVOKE_QUEUE_PRIVILEGE`. Starting from Oracle Database 12c Release 2, `ENQUEUE_ANY` and `DEQUEUE_ANY` privileges will not allow access to `SYS` owned queues by users other than `SYS`.

See Also:

- [DBMS\_AQ](DBMS_AQ.md).
- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE2564) for more information on queue privileges and access control.

Security Required for Propagation

Propagation jobs are owned by `SYS`, but the propagation occurs in the security context of the queue table owner. Previously propagation jobs were owned by the user scheduling propagation, and propagation occurred in the security context of the user setting up the propagation schedule. The queue table owner must be granted `EXECUTE` privileges on the `DBMS_AQADM` package. Otherwise, the Oracle Database snapshot processes do not propagate and generate trace files with the error identifier `SYS.DBMS_AQADM` not defined. Private database links owned by the queue table owner can be used for propagation. The username specified in the connection string must have `EXECUTE` access on the `DBMS_AQ` and `DBMS_AQADM` packages on the remote database.

See Also:

[Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE2567) for more information on security required for propagation.

Queue Table Migration

The `MIGRATE_QUEUE_TABLE` procedure requires that the `EXECUTE` privilege on `DBMS_AQADM` be granted to the queue table owner, who is probably an ordinary queue user. If you do not want ordinary queue users to be able to create and drop queues and queue tables, add and delete subscribers, and so forth, then you must revoke the `EXECUTE` privilege as soon as the migration is done.

See Also:

- " MIGRATE\_QUEUE\_TABLE Procedure."
- [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADQUE2706) for more information on granting Oracle Database Advanced Queuing system privileges.

### 25.2 DBMS\_AQADM Constants

When using enumerated constants, such as `INFINITE`, `TRANSACTIONAL`, or `NORMAL_QUEUE`, the symbol must be specified with the scope of the packages defining it. All types associated with the administrative interfaces must be prepended with `DBMS_AQADM`. For example: `DBMS_AQADM.NORMAL_QUEUE`.

Table 25-1 Enumerated Types in the Administrative Interface

| Parameter | Options |
| --- | --- |
| `retention` | `0`, `1`, `2`...`INFINITE` |
| `message_grouping` | `TRANSACTIONAL`, `NONE` |
| `queue_type` | `NORMAL_QUEUE`, `EXCEPTION_QUEUE`, `NON_PERSISTENT_QUEUE` |

See Also:

For more information on the Java classes and data structures used in both `DBMS_AQ` and `DBMS_AQADM`, see the [DBMS\_AQ](DBMS_AQ.md) package.

### 25.3 DBMS\_AQADM Subprogram Groups

This section lists and describes the DBMS\_AQADM subprogram groups.

This DBMS\_AQADM package is made up of the following subprogram groups:

- Queue Table Subprograms
- Privilege Subprograms
- Queue Subprograms
- Subscriber Subprograms
- Propagation Subprograms
- Miscellaneous Subprograms
- Oracle Database Advanced Queuing Agent Subprograms
- Alias Subprograms

#### 25.3.1 DBMS\_AQADM Queue Table Subprograms

This section lists and describes the DBMS\_AQADM Queue Table subprograms.

Table 25-2 Queue Table Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_QUEUE\_TABLE Procedure | Alters the existing properties of a queue table |
| CREATE\_QUEUE\_TABLE Procedure | Creates a queue table for messages of a predefined type |
| DROP\_QUEUE\_TABLE Procedure | Drops an existing queue table |
| ENABLE\_JMS\_TYPES Procedure | A precondition for the enqueue of JMS types and XML types |
| MIGRATE\_QUEUE\_TABLE Procedure | Upgrades an 8.0-compatible queue table to an 8.1-compatible or higher queue table, or downgrades an 8.1-compatible or higher queue table to an 8.0-compatible queue table |
| PURGE\_QUEUE\_TABLE Procedure | Purges messages from queue tables |

#### 25.3.2 DBMS\_AQADM Privilege Subprograms

This sections lists and describes the DBMS\_AQADM Privilege subprograms.

Table 25-3 Privilege Subprograms

| Subprograms | Description |
| --- | --- |
| GRANT\_QUEUE\_PRIVILEGE Procedure | Grants privileges on a queue to users and roles |
| GRANT\_SYSTEM\_PRIVILEGE Procedure | Grants Oracle Database Advanced Queuing system privileges to users and roles |
| REVOKE\_QUEUE\_PRIVILEGE Procedure | Revokes privileges on a queue from users and roles |
| REVOKE\_SYSTEM\_PRIVILEGE Procedure | Revokes Oracle Database Advanced Queuing system privileges from users and roles |

#### 25.3.3 DBMS\_AQADM Queue Subprograms

This sections lists and describes the DBMS\_AQADM Queue subprograms.

Table 25-4 Queue Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_QUEUE Procedure | Alters existing properties of a queue |
| CREATE\_NP\_QUEUE Procedure | Creates a nonpersistent `RAW` queue |
| CREATE\_QUEUE Procedure | Creates a queue in the specified queue table |
| CREATE\_SHARDED\_QUEUE Procedure | Creates a queue and its queue table for a sharded queue all together. |
| DROP\_SHARDED\_QUEUE Procedure | Drops an existing sharded queue from the database queuing system |
| ALTER\_SHARDED\_QUEUE Procedure | Alters an sharded queue in the database queuing system |
| CREATE\_EXCEPTION\_QUEUE Procedure | Creates an exception queue for a sharded queue |
| DROP\_QUEUE Procedure | Drops an existing queue |
| QUEUE\_SUBSCRIBERS Function | Returns the subscribers to an 8.0-compatible multiconsumer queue in the PL/SQL index by table collection type `DBMS_AQADM.AQ$_subscriber_list_t` |
| START\_QUEUE Procedure | Enables the specified queue for enqueuing or dequeuing |
| STOP\_QUEUE Procedure | Disables enqueuing or dequeuing on the specified queue |

#### 25.3.4 DBMS\_AQADM Subscriber Subprograms

This sections lists and describes the DBMS\_AQADM Subscriber subprograms.

Table 25-5 Subscriber Subprograms

| Subprograms | Description |
| --- | --- |
| ADD\_SUBSCRIBER Procedure | Adds a default subscriber to a queue |
| ALTER\_SUBSCRIBER Procedure | Alters existing properties of a subscriber to a specified queue |
| REMOVE\_SUBSCRIBER Procedure | Removes a default subscriber from a queue |

#### 25.3.5 DBMS\_AQADM Propagation Subprograms

This section lists and describes the DBMS\_AQADM propagation subprograms.

Table 25-6 Propagation Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_PROPAGATION\_SCHEDULE Procedure | Alters parameters for a propagation schedule |
| DISABLE\_PROPAGATION\_SCHEDULE Procedure | Disables a propagation schedule |
| ENABLE\_PROPAGATION\_SCHEDULE Procedure | Enables a previously disabled propagation schedule |
| SCHEDULE\_PROPAGATION Procedure | Schedules propagation of messages from a queue to a destination identified by a specific database link |
| UNSCHEDULE\_PROPAGATION Procedure | Unschedules previously scheduled propagation of messages from a queue to a destination identified by a specific database link |
| VERIFY\_QUEUE\_TYPES Procedure | Verifies that the source and destination queues have identical types |

#### 25.3.6 DBMS\_AQADM Miscellaneous Subprograms

This section lists and describes the DBMS\_AQADM miscellaneous subprograms.

Table 25-7 Miscellaneous Subprograms

| Subprograms | Description |
| --- | --- |
| GET\_QUEUE\_PARAMETER Procedure | Used to get different parameters for sharded queues at queue or database level. |
| GET\_MAX\_STREAMS\_POOL Procedure | Retrieves the value of Oracle Database Advanced Queuing maximum streams pool memory limit |
| GET\_MIN\_STREAMS\_POOL Procedure | Retrieves the value of Oracle Database Advanced Queuing minimum streams pool memory limit |
| GET\_WATERMARK Procedure | Retrieves the value of watermark set by the `SET_WATERMARK` Procedure |
| SET\_QUEUE\_PARAMETER Procedure | Used to set different parameters for sharded queues at queue or database level. |
| SET\_MAX\_STREAMS\_POOL Procedure | Used for Oracle Database Advanced Queuing to specify and limit maximum streams pool memory use |
| SET\_MIN\_STREAMS\_POOL Procedure | Used for Oracle Database Advanced Queuing to specify and limit minimum streams pool memory use |
| SET\_WATERMARK Procedure | Used for Oracle Database Advanced Queuing notification to specify and limit memory use |
| UNSET\_QUEUE\_PARAMETER Procedure | Used to unset different parameters for sharded queues at queue or database level. |

#### 25.3.7 DBMS\_AQADM Agent Subprograms

This section lists and describes the DBMS\_AQADM agent subprograms.

Table 25-8 Oracle Streams AQ Agent Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_AQ\_AGENT Procedure | Alters an agent registered for Oracle Database Advanced Queuing Internet access, and an Oracle Database Advanced Queuing agent that accesses secure queues |
| CREATE\_AQ\_AGENT Procedure | Registers an agent for Oracle Database Advanced Queuing Internet access using HTTP/SMTP protocols, and creates an Oracle Database Advanced Queuing agent to access secure queues |
| DISABLE\_DB\_ACCESS Procedure | Revokes the privileges of a specific database user from an Oracle Database Advanced Queuing Internet agent |
| DROP\_AQ\_AGENT Procedure | Drops an agent that was previously registered for Oracle Database Advanced Queuing Internet access |
| ENABLE\_DB\_ACCESS Procedure | Grants an Oracle Database Advanced Queuing Internet agent the privileges of a specific database user |

#### 25.3.8 DBMS\_AQADM Alias Subprograms

This section lists and describes the DBMS\_AQADM alias subprograms.

Table 25-9 Alias Subprograms

| Subprograms | Description |
| --- | --- |
| ADD\_ALIAS\_TO\_LDAP Procedure | Creates an alias for a queue, agent, or a JMS ConnectionFactory in LDAP |
| DEL\_ALIAS\_FROM\_LDAP Procedure | Drops an alias for a queue, agent, or JMS ConnectionFactory in LDAP |

### 25.4 Summary of DBMS\_AQADM Subprograms

This section lists and describes the DBMS\_AQADM package subprograms.

Table 25-10 DBMS\_AQADM Package Subprograms

| Subprograms | Description |
| --- | --- |
| ADD\_ALIAS\_TO\_LDAP Procedure | Creates an alias for a queue, agent, or a JMS ConnectionFactory in LDAP |
| ADD\_SUBSCRIBER Procedure | Adds a default subscriber to a queue |
| ALTER\_AQ\_AGENT Procedure | Alters an agent registered for Oracle Database Advanced Queuing Internet access, and an Oracle Database Advanced Queuing agent that accesses secure queues |
| ALTER\_PROPAGATION\_SCHEDULE Procedure | Alters parameters for a propagation schedule |
| ALTER\_QUEUE Procedure | Alters existing properties of a queue |
| ALTER\_QUEUE\_TABLE Procedure | Alters the existing properties of a queue table |
| ALTER\_SHARDED\_QUEUE Procedure | Provides user the ability to alter the `cache_hint` and comment for the sharded queue  Starting with Oracle Database 20c, sharded queues are deprecated and will be desupported in a futur release. Use Transactional Event Queues(TEQ) instead. |
| ALTER\_SUBSCRIBER Procedure | Alters existing properties of a subscriber to a specified queue |
| ALTER\_TRANSACTIONAL\_EVENT\_QUEUE Procedure | Provides user the ability to alter the `cache_hint` and comment for the TEQ queue |
| CREATE\_AQ\_AGENT Procedure | Registers an agent for Oracle Database Advanced Queuing Internet access using HTTP/SMTP protocols, and creates an Oracle Database Advanced Queuing agent to access secure queues |
| CREATE\_NP\_QUEUE Procedure | Creates a nonpersistent `RAW` queue |
| CREATE\_QUEUE Procedure | Creates a queue in the specified queue table |
| CREATE\_SHARDED\_QUEUE Procedure | Creates a queue and its queue table for a sharded queue all together.  Starting with Oracle Database 20c, sharded queues are deprecated and will be desupported in a futur release. Use Transactional Event Queues(TEQ) instead. |
| CREATE\_EXCEPTION\_QUEUE Procedure | Creates an exception queue.  Starting with Oracle Database 20c, sharded queues are deprecated and will be desupported in a futur release. Use Transactional Event Queues(TEQ) instead. |
| CREATE\_EQ EXCEPTION\_QUEUE Procedure | Creates an exception queue. |
| CREATE\_TRANSACTIONAL\_EVENT\_QUEUE Procedure | Creates a queue and its queue table for a Transactional Event Queue (TEQ). |
| CREATE\_QUEUE\_TABLE Procedure | Creates a queue table for messages of a predefined type |
| DEL\_ALIAS\_FROM\_LDAP Procedure | Drops an alias for a queue, agent, or JMS ConnectionFactory in LDAP |
| DISABLE\_DB\_ACCESS Procedure | Revokes the privileges of a specific database user from an Oracle Database Advanced Queuing Internet agent |
| DISABLE\_PROPAGATION\_SCHEDULE Procedure | Disables a propagation schedule |
| DROP\_AQ\_AGENT Procedure | Drops an agent that was previously registered for Oracle Database Advanced Queuing Internet access |
| DROP\_QUEUE Procedure | Drops an existing queue |
| DROP\_SHARDED\_QUEUE Procedure | Drops an existing sharded queue from the database queuing system  Starting with Oracle Database 20c, sharded queues are deprecated and will be desupported in a futur release. Use Transactional Event Queues(TEQ) instead. |
| DROP\_TRANSACTIONAL\_EVENT\_QUEUE Procedure | Drops an existing TEQ queue from the database queuing system |
| DROP\_QUEUE\_TABLE Procedure | Drops an existing queue table |
| ENABLE\_DB\_ACCESS Procedure | Grants an Oracle Database Advanced Queuing Internet agent the privileges of a specific database user |
| ENABLE\_JMS\_TYPES Procedure | A precondition for the enqueue of JMS types and XML types |
| ENABLE\_PROPAGATION\_SCHEDULE Procedure | Enables a previously disabled propagation schedule |
| GET\_MAX\_STREAMS\_POOL Procedure | Retrieves the value of Oracle Database Advanced Queuing maximum streams pool memory limit |
| GET\_MIN\_STREAMS\_POOL Procedure | Retrieves the value of Oracle Database Advanced Queuing minimum streams pool memory limit |
| GET\_QUEUE\_PARAMETER Procedure | Used to get different parameters for sharded queues at queue or database level. |
| GET\_WATERMARK Procedure | Retrieves the value of watermark set by the `SET_WATERMARK` Procedure |
| GRANT\_QUEUE\_PRIVILEGE Procedure | Grants privileges on a queue to users and roles |
| GRANT\_SYSTEM\_PRIVILEGE Procedure | Grants Oracle Database Advanced Queuing system privileges to users and roles |
| MIGRATE\_QUEUE\_TABLE Procedure | Upgrades an 8.0-compatible queue table to an 8.1-compatible or higher queue table, or downgrades an 8.1-compatible or higher queue table to an 8.0-compatible queue table |
| PURGE\_QUEUE\_TABLE Procedure | Purges messages from queue tables |
| QUEUE\_SUBSCRIBERS Function | Returns the subscribers to an 8.0-compatible multiconsumer queue in the PL/SQL index by table collection type `DBMS_AQADM.AQ$_subscriber_list_t` |
| REMOVE\_SUBSCRIBER Procedure | Removes a default subscriber from a queue |
| REVOKE\_QUEUE\_PRIVILEGE Procedure | Revokes privileges on a queue from users and roles |
| REVOKE\_SYSTEM\_PRIVILEGE Procedure | Revokes Oracle Database Advanced Queuing system privileges from users and roles |
| SCHEDULE\_PROPAGATION Procedure | Schedules propagation of messages from a queue to a destination identified by a specific database link |
| SET\_QUEUE\_PARAMETER Procedure | Used to set different parameters for sharded queues at queue or database level. |
| SET\_MAX\_STREAMS\_POOL Procedure | Used for Oracle Database Advanced Queuing to specify and limit maximum streams pool memory use |
| SET\_MIN\_STREAMS\_POOL Procedure | Used for Oracle Database Advanced Queuing to specify and limit minimum streams pool memory use |
| SET\_WATERMARK Procedure | Used for Oracle Database Advanced Queuing notification to specify and limit memory use |
| START\_QUEUE Procedure | Enables the specified queue for enqueuing or dequeuing |
| STOP\_QUEUE Procedure | Disables enqueuing or dequeuing on the specified queue |
| UNSCHEDULE\_PROPAGATION Procedure | Unschedules previously scheduled propagation of messages from a queue to a destination identified by a specific database link |
| UNSET\_QUEUE\_PARAMETER Procedure | Used to unset different parameters for sharded queues at queue or database level. |
| VERIFY\_QUEUE\_TYPES Procedure | Verifies that the source and destination queues have identical types |

#### 25.4.1 ADD\_ALIAS\_TO\_LDAP Procedure

This procedure creates an alias for a queue, agent, or a JMS ConnectionFactory in LDAP. The alias will be placed directly under the database server's distinguished name in LDAP hierarchy.

Syntax

```
DBMS_AQADM.ADD_ALIAS_TO_LDAP(
   alias          IN VARCHAR2,
   obj_location   IN VARCHAR2);
```

Parameters

Table 25-11 ADD\_ALIAS\_TO\_LDAP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `alias` | Name of the alias. Example: `west_shipping.` |
| `obj_location` | The distinguished name of the object (queue, agent or connection factory) to which `alias` refers. |

Usage Notes

This method can be used to create aliases for queues, agents, and JMS ConnectionFactory objects. These object must exist before the alias is created. These aliases can be used for JNDI lookup in JMS and Oracle Database Advanced Queuing Internet access.

#### 25.4.2 ADD\_SUBSCRIBER Procedure

This procedure adds a default subscriber to a queue.

Syntax

```
DBMS_AQADM.ADD_SUBSCRIBER (
   queue_name      IN    VARCHAR2,
   subscriber      IN    sys.aq$_agent,
   rule            IN    VARCHAR2 DEFAULT NULL,
   transformation  IN    VARCHAR2 DEFAULT NULL
   queue_to_queue  IN    BOOLEAN DEFAULT FALSE,
   delivery_mode   IN    PLS_INTEGER DEFAULT DBMS_AQADM.PERSISTENT);
```

Parameters

Table 25-12 ADD\_SUBSCRIBER Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | Name of the queue. |
| `subscriber` | Agent on whose behalf the subscription is being defined. |
| `rule` | A conditional expression based on the message properties, the message data properties and PL/SQL functions. A rule is specified as a Boolean expression using syntax similar to the `WHERE` clause of a SQL query. This Boolean expression can include conditions on message properties, user data properties (object payloads only), and PL/SQL or SQL functions (as specified in the where clause of a SQL query). Currently supported message properties are `priority` and `corrid`.  To specify rules on a message payload (object payload), use attributes of the object type in clauses. You must prefix each attribute with `tab`.`user_data` as a qualifier to indicate the specific column of the queue table that stores the payload. The rule parameter cannot exceed 4000 characters. |
| `transformation` | Specifies a transformation that will be applied when this subscriber dequeues the message. The source type of the transformation must match the type of the queue. If the subscriber is remote, then the transformation is applied before propagation to the remote queue. |
| `queue_to_queue` | If `TRUE`, propagation is from queue-to-queue. |
| `delivery_mode` | The administrator may specify one of `DBMS_AQADM`.`PERSISTENT`, `DBMS_AQADM`.`BUFFERED`, or `DBMS_AQADM`.`PERSISTENT_OR_BUFFERED` for the delivery mode of the messages the subscriber is interested in. This parameter will not be modifiable by `ALTER_SUBSCRIBER`. |

Usage Notes

A program can enqueue messages to a specific list of recipients or to the default list of subscribers. This operation only succeeds on queues that allow multiple consumers. This operation takes effect immediately, and the containing transaction is committed. Enqueue requests that are executed after the completion of this call will reflect the new behavior.

Any string within the rule must be quoted:

```
rule   => 'PRIORITY <= 3 AND CORRID =  ''FROM JAPAN'''
```

Note that these are all single quotation marks.

#### 25.4.3 ALTER\_AQ\_AGENT Procedure

This procedure alters an agent registered for Oracle Database Advanced Queuing Internet access. It is also used to alter an Oracle Database Advanced Queuing agent that accesses secure queues.

Syntax

```
DBMS_AQADM.ALTER_AQ_AGENT (
  agent_name                IN VARCHAR2,
  certificate_location      IN VARCHAR2 DEFAULT NULL,
  enable_http               IN BOOLEAN DEFAULT FALSE,
  enable_smtp               IN BOOLEAN DEFAULT FALSE,
  enable_anyp               IN BOOLEAN DEFAULT FALSE )
```

Parameters

Table 25-13 ALTER\_AQ\_AGENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `agent_name` | Specifies the username of the Oracle Database Advanced Queuing Internet agent. |
| `certification_location` | Agent's certificate location in LDAP (default is `NULL`). If the agent is allowed to access Oracle Database Advanced Queuing through SMTP, then its certificate must be registered in LDAP. For access through HTTP, the certificate location is not required. |
| `enable_http` | `TRUE` means the agent can access Oracle Database Advanced Queuing through HTTP. `FALSE` means the agent cannot access Oracle Database Advanced Queuing through HTTP. |
| `enable_smtp` | `TRUE` means the agent can access Oracle Database Advanced Queuing through SMTP (e-mail). `FALSE` means the agent cannot access Oracle Database Advanced Queuing through SMTP. |
| `enable_anyp` | `TRUE` means the agent can access Oracle Database Advanced Queuing through any protocol (HTTP or SMTP). |

#### 25.4.4 ALTER\_PROPAGATION\_SCHEDULE Procedure

This procedure alters parameters for a propagation schedule.

Syntax

```
DBMS_AQADM.ALTER_PROPAGATION_SCHEDULE ( 
   queue_name           IN    VARCHAR2, 
   destination          IN    VARCHAR2 DEFAULT NULL,
   duration             IN    NUMBER   DEFAULT NULL, 
   next_time            IN    VARCHAR2 DEFAULT NULL, 
   latency              IN    NUMBER   DEFAULT 60,
   destination_queue    IN    VARCHAR2 DEFAULT NULL);
```

Parameters

Table 25-14 ALTER\_PROPAGATION\_SCHEDULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. |
| `destination` | Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is `NULL`, then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. |
| `duration` | Duration of the propagation window in seconds. A `NULL` value means the propagation window is forever or until the propagation is unscheduled. |
| `next_time` | Date function to compute the start of the next propagation window from the end of the current window. If this value is `NULL`, then propagation is stopped at the end of the current window. For example, to start the window at the same time every day, `next_time` should be specified as `SYSDATE` `+` `1` `-` `duration/86400`. |
| `latency` | Maximum wait, in seconds, in the propagation window for a message to be propagated after it is enqueued. The default value is 60. Caution: if latency is not specified for this call, then latency will over-write any existing value with the default value.  For example, if the latency is 60 seconds and there are no messages to be propagated during the propagation window, then messages from that queue for the destination are not propagated for at least 60 more seconds. It will be at least 60 seconds before the queue will be checked again for messages to be propagated for the specified destination. If the latency is 600, then the queue will not be checked for 10 minutes and if the latency is 0, then a job queue process will be waiting for messages to be enqueued for the destination and as soon as a message is enqueued it will be propagated. |
| `destination_queue` | Name of the target queue to which messages are to be propagated in the form of a `dblink` |

#### 25.4.5 ALTER\_QUEUE Procedure

This procedure alters existing properties of a queue. The parameters `max_retries`, `retention_time`, and `retry_delay` are not supported for nonpersistent queues.

Syntax

```
DBMS_AQADM.ALTER_QUEUE (
   queue_name        IN    VARCHAR2,
   max_retries       IN    NUMBER   DEFAULT NULL,
   retry_delay       IN    NUMBER   DEFAULT NULL,
   retention_time    IN    NUMBER   DEFAULT NULL,
   auto_commit       IN    BOOLEAN  DEFAULT TRUE,
   comment           IN    VARCHAR2 DEFAULT NULL);
```

Parameters

Table 25-15 ALTER\_QUEUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | Name of the queue that is to be altered |
| `max_retries` | Limits the number of times a dequeue with `REMOVE` mode can be attempted on a message. The maximum value of `max_retries` is 2\*\*31 -1.  A message is moved to an exception queue if `RETRY_COUNT` is greater than `MAX_RETRIES`. `RETRY_COUNT` is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including `ALTER` `SYSTEM` `KILL` `SESSION`) or `SHUTDOWN` `ABORT` on the instance, then `RETRY_COUNT` is not incremented.  Note that `max_retries` is supported for all single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| `retry_delay` | Delay time in seconds before this message is scheduled for processing again after an application rollback. The default is `NULL`, which means that the value will not be altered.  Note that `retry_delay` is supported for single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| `retention_time` | Retention time in seconds for which a message is retained in the queue table after being dequeued. The default is `NULL`, which means that the value will not be altered. |
| `auto_commit` | `TRUE` causes the current transaction, if any, to commit before the `ALTER_QUEUE ` operation is carried out. The `ALTER_QUEUE ` operation become persistent when the call returns. This is the default. `FALSE` means the operation is part of the current transaction and becomes persistent only when the caller enters a commit.  Caution: This parameter has been deprecated. |