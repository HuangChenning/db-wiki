---
title: DBMS_AQADM
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_aqadm.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 23 DBMS\_AQADM

The `DBMS_AQADM` package provides procedures to manage Oracle Streams Advanced Queuing (AQ) configuration and administration information.

See Also:

- [Oracle Streams Advanced Queuing User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e11013/aq_admin.htm#ADQUE0800)
- [Chapter 244, "Oracle Streams AQ TYPEs"](t_aq.md) for information about the `TYPE` s to use with `DBMS_AQADM`

This chapter contains the following topics:

---

## Using DBMS\_AQADM

This section contains the following topics.

- Constants

---

### Constants

When using enumerated constants, such as `INFINITE`, `TRANSACTIONAL`, or `NORMAL_QUEUE`, the symbol must be specified with the scope of the packages defining it. All types associated with the administrative interfaces must be prepended with `DBMS_AQADM`. For example: `DBMS_AQADM.NORMAL_QUEUE`.

Table 23-1 Enumerated Types in the Administrative Interface

| Parameter | Options |
| --- | --- |
| `retention` | `0`, `1`, `2`...`INFINITE` |
| `message_grouping` | `TRANSACTIONAL`, `NONE` |
| `queue_type` | `NORMAL_QUEUE`, `EXCEPTION_QUEUE`, `NON_PERSISTENT_QUEUE` |

See Also:

For more information on the Java classes and data structures used in both `DBMS_AQ` and `DBMS_AQADM`, see the [DBMS\_AQ](d_aq.md) package.

---

## Subprogram Groups

This DBMS\_AQADM package is made up of the following subprogram groups:

- Queue Table Subprograms
- Privilege Subprograms
- Queue Subprograms
- Subscriber Subprograms
- Notification Subprograms
- Propagation Subprograms
- Oracle Streams AQ Agent Subprograms
- Alias Subprograms

---

### Queue Table Subprograms

Table 23-2 Queue Table Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_QUEUE\_TABLE Procedure | Alters the existing properties of a queue table |
| CREATE\_QUEUE\_TABLE Procedure | Creates a queue table for messages of a predefined type |
| DROP\_QUEUE\_TABLE Procedure | Drops an existing queue table |
| ENABLE\_JMS\_TYPES Procedure | A precondition for the enqueue of JMS types and XML types |
| MIGRATE\_QUEUE\_TABLE Procedure | Upgrades an 8.0-compatible queue table to an 8.1-compatible or higher queue table, or downgrades an 8.1-compatible or higher queue table to an 8.0-compatible queue table |
| PURGE\_QUEUE\_TABLE Procedure | Purges messages from queue tables |

---

### Privilege Subprograms

Table 23-3 Privilege Subprograms

| Subprograms | Description |
| --- | --- |
| GRANT\_QUEUE\_PRIVILEGE Procedure | Grants privileges on a queue to users and roles |
| GRANT\_SYSTEM\_PRIVILEGE Procedure | Grants Oracle Streams AQ system privileges to users and roles |
| REVOKE\_QUEUE\_PRIVILEGE Procedure | Revokes privileges on a queue from users and roles |
| REVOKE\_SYSTEM\_PRIVILEGE Procedure | Revokes Oracle Streams AQ system privileges from users and roles |

---

### Queue Subprograms

Table 23-4 Queue Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_QUEUE Procedure | Alters existing properties of a queue |
| CREATE\_NP\_QUEUE Procedure | Creates a nonpersistent `RAW` queue |
| CREATE\_QUEUE Procedure | Creates a queue in the specified queue table |
| DROP\_QUEUE Procedure | Drops an existing queue |
| QUEUE\_SUBSCRIBERS Function | Returns the subscribers to an 8.0-compatible multiconsumer queue in the PL/SQL index by table collection type `DBMS_AQADM.AQ$_subscriber_list_t` |
| START\_QUEUE Procedure | Enables the specified queue for enqueuing or dequeuing |
| STOP\_QUEUE Procedure | Disables enqueuing or dequeuing on the specified queue |

---

### Subscriber Subprograms

Table 23-5 Subscriber Subprograms

| Subprograms | Description |
| --- | --- |
| ADD\_SUBSCRIBER Procedure | Adds a default subscriber to a queue |
| ALTER\_SUBSCRIBER Procedure | Alters existing properties of a subscriber to a specified queue |
| REMOVE\_SUBSCRIBER Procedure | Removes a default subscriber from a queue |

---

### Notification Subprograms

Table 23-6 Notification Subprograms

| Subprograms | Description |
| --- | --- |
| GET\_WATERMARK Procedure | Retrieves the value of watermark set by the `SET_WATERMARK` `Procedure` |
| SET\_WATERMARK Procedure | Used for Oracle Streams AQ notification to specify and limit memory use |

---

### Propagation Subprograms

Table 23-7 Propagation Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_PROPAGATION\_SCHEDULE Procedure | Alters parameters for a propagation schedule |
| DISABLE\_PROPAGATION\_SCHEDULE Procedure | Disables a propagation schedule |
| ENABLE\_PROPAGATION\_SCHEDULE Procedure | Enables a previously disabled propagation schedule |
| SCHEDULE\_PROPAGATION Procedure | Schedules propagation of messages from a queue to a destination identified by a specific database link |
| UNSCHEDULE\_PROPAGATION Procedure | Unschedules previously scheduled propagation of messages from a queue to a destination identified by a specific database link |
| VERIFY\_QUEUE\_TYPES Procedure | Verifies that the source and destination queues have identical types |

---

### Oracle Streams AQ Agent Subprograms

Table 23-8 Oracle Streams AQ Agent Subprograms

| Subprograms | Description |
| --- | --- |
| ALTER\_AQ\_AGENT Procedure | Alters an agent registered for Oracle Streams AQ Internet access, and an Oracle Streams AQ agent that accesses secure queues |
| CREATE\_AQ\_AGENT Procedure | Registers an agent for Oracle Streams AQ Internet access using HTTP/SMTP protocols, and creates an Oracle Streams AQ agent to access secure queues |
| DISABLE\_DB\_ACCESS Procedure | Revokes the privileges of a specific database user from an Oracle Streams AQ Internet agent |
| DROP\_AQ\_AGENT Procedure | Drops an agent that was previously registered for Oracle Streams AQ Internet access |
| ENABLE\_DB\_ACCESS Procedure | Grants an Oracle Streams AQ Internet agent the privileges of a specific database user |

---

### Alias Subprograms

Table 23-9 Alias Subprograms

| Subprograms | Description |
| --- | --- |
| ADD\_ALIAS\_TO\_LDAP Procedure | Creates an alias for a queue, agent, or a JMS ConnectionFactory in LDAP |
| DEL\_ALIAS\_FROM\_LDAP Procedure | Drops an alias for a queue, agent, or JMS ConnectionFactory in LDAP |

---

## Summary of DBMS\_AQADM Subprograms

Table 23-10 DBMS\_AQADM Package Subprograms

| Subprograms | Description |
| --- | --- |
| ADD\_ALIAS\_TO\_LDAP Procedure | Creates an alias for a queue, agent, or a JMS ConnectionFactory in LDAP |
| ADD\_SUBSCRIBER Procedure | Adds a default subscriber to a queue |
| ALTER\_AQ\_AGENT Procedure | Alters an agent registered for Oracle Streams AQ Internet access, and an Oracle Streams AQ agent that accesses secure queues |
| ALTER\_PROPAGATION\_SCHEDULE Procedure | Alters parameters for a propagation schedule |
| ALTER\_QUEUE Procedure | Alters existing properties of a queue |
| ALTER\_QUEUE\_TABLE Procedure | Alters the existing properties of a queue table |
| ALTER\_SUBSCRIBER Procedure | Alters existing properties of a subscriber to a specified queue |
| CREATE\_AQ\_AGENT Procedure | Registers an agent for Oracle Streams AQ Internet access using HTTP/SMTP protocols, and creates an Oracle Streams AQ agent to access secure queues |
| CREATE\_NP\_QUEUE Procedure | Creates a nonpersistent `RAW` queue |
| CREATE\_QUEUE Procedure | Creates a queue in the specified queue table |
| CREATE\_QUEUE\_TABLE Procedure | Creates a queue table for messages of a predefined type |
| DEL\_ALIAS\_FROM\_LDAP Procedure | Drops an alias for a queue, agent, or JMS ConnectionFactory in LDAP |
| DISABLE\_DB\_ACCESS Procedure | Revokes the privileges of a specific database user from an Oracle Streams AQ Internet agent |
| DISABLE\_PROPAGATION\_SCHEDULE Procedure | Disables a propagation schedule |
| DROP\_AQ\_AGENT Procedure | Drops an agent that was previously registered for Oracle Streams AQ Internet access |
| DROP\_QUEUE Procedure | Drops an existing queue |
| DROP\_QUEUE\_TABLE Procedure | Drops an existing queue table |
| ENABLE\_DB\_ACCESS Procedure | Grants an Oracle Streams AQ Internet agent the privileges of a specific database user |
| ENABLE\_JMS\_TYPES Procedure | A precondition for the enqueue of JMS types and XML types |
| ENABLE\_PROPAGATION\_SCHEDULE Procedure | Enables a previously disabled propagation schedule |
| GET\_WATERMARK Procedure | Retrieves the value of watermark set by the `SET_WATERMARK` `Procedure` |
| GRANT\_QUEUE\_PRIVILEGE Procedure | Grants privileges on a queue to users and roles |
| GRANT\_SYSTEM\_PRIVILEGE Procedure | Grants Oracle Streams AQ system privileges to users and roles |
| MIGRATE\_QUEUE\_TABLE Procedure | Upgrades an 8.0-compatible queue table to an 8.1-compatible or higher queue table, or downgrades an 8.1-compatible or higher queue table to an 8.0-compatible queue table |
| PURGE\_QUEUE\_TABLE Procedure | Purges messages from queue tables |
| QUEUE\_SUBSCRIBERS Function | Returns the subscribers to an 8.0-compatible multiconsumer queue in the PL/SQL index by table collection type `DBMS_AQADM.AQ$_subscriber_list_t` |
| REMOVE\_SUBSCRIBER Procedure | Removes a default subscriber from a queue |
| REVOKE\_QUEUE\_PRIVILEGE Procedure | Revokes privileges on a queue from users and roles |
| REVOKE\_SYSTEM\_PRIVILEGE Procedure | Revokes Oracle Streams AQ system privileges from users and roles |
| SCHEDULE\_PROPAGATION Procedure | Schedules propagation of messages from a queue to a destination identified by a specific database link |
| SET\_WATERMARK Procedure | Used for Oracle Streams AQ notification to specify and limit memory use |
| START\_QUEUE Procedure | Enables the specified queue for enqueuing or dequeuing |
| STOP\_QUEUE Procedure | Disables enqueuing or dequeuing on the specified queue |
| UNSCHEDULE\_PROPAGATION Procedure | Unschedules previously scheduled propagation of messages from a queue to a destination identified by a specific database link |
| VERIFY\_QUEUE\_TYPES Procedure | Verifies that the source and destination queues have identical types |

---

### ADD\_ALIAS\_TO\_LDAP Procedure

This procedure creates an alias for a queue, agent, or a JMS ConnectionFactory in LDAP. The alias will be placed directly under the database server's distinguished name in LDAP hierarchy.

Syntax

```
DBMS_AQADM.ADD_ALIAS_TO_LDAP(
   alias          IN VARCHAR2,
   obj_location   IN VARCHAR2);
```

Parameters

Table 23-11 ADD\_ALIAS\_TO\_LDAP Procedure Parameters

| Parameter | Description |
| --- | --- |
| `alias` | Name of the alias. Example: `west_shipping.` |
| `obj_location` | The distinguished name of the object (queue, agent or connection factory) to which `alias` refers. |

Usage Notes

This method can be used to create aliases for queues, agents, and JMS ConnectionFactory objects. These object must exist before the alias is created. These aliases can be used for JNDI lookup in JMS and Oracle Streams AQ Internet access.

---

### ADD\_SUBSCRIBER Procedure

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

Table 23-12 ADD\_SUBSCRIBER Procedure Parameters

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

---

### ALTER\_AQ\_AGENT Procedure

This procedure alters an agent registered for Oracle Streams AQ Internet access. It is also used to alter an Oracle Streams AQ agent that accesses secure queues.

See Also:

[Oracle Streams Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e17069/toc.htm) for information about secure queues

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

Table 23-13 ALTER\_AQ\_AGENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `agent_name` | Specifies the username of the Oracle Streams AQ Internet agent. |
| `certification_location` | Agent's certificate location in LDAP (default is `NULL`). If the agent is allowed to access Oracle Streams AQ through SMTP, then its certificate must be registered in LDAP. For access through HTTP, the certificate location is not required. |
| `enable_http` | `TRUE` means the agent can access Oracle Streams AQ through HTTP. `FALSE` means the agent cannot access Oracle Streams AQ through HTTP. |
| `enable_smtp` | `TRUE` means the agent can access Oracle Streams AQ through SMTP (e-mail). `FALSE` means the agent cannot access Oracle Streams AQ through SMTP. |
| `enable_anyp` | `TRUE` means the agent can access Oracle Streams AQ through any protocol (HTTP or SMTP). |

---

### ALTER\_PROPAGATION\_SCHEDULE Procedure

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

Table 23-14 ALTER\_PROPAGATION\_SCHEDULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | Name of the source queue whose messages are to be propagated, including the schema name. If the schema name is not specified, then it defaults to the schema name of the user. |
| `destination` | Destination database link. Messages in the source queue for recipients at this destination are propagated. If it is `NULL`, then the destination is the local database and messages are propagated to other queues in the local database. The length of this field is currently limited to 128 bytes, and if the name is not fully qualified, then the default domain name is used. |
| `duration` | Duration of the propagation window in seconds. A `NULL` value means the propagation window is forever or until the propagation is unscheduled. |
| `next_time` | Date function to compute the start of the next propagation window from the end of the current window. If this value is `NULL`, then propagation is stopped at the end of the current window. For example, to start the window at the same time every day, `next_time` should be specified as `SYSDATE` `+` `1` `-` `duration/86400`. |
| `latency` | Maximum wait, in seconds, in the propagation window for a message to be propagated after it is enqueued. The default value is 60. Caution: if latency is not specified for this call, then latency will over-write any existing value with the default value.  For example, if the latency is 60 seconds and there are no messages to be propagated during the propagation window, then messages from that queue for the destination are not propagated for at least 60 more seconds. It will be at least 60 seconds before the queue will be checked again for messages to be propagated for the specified destination. If the latency is 600, then the queue will not be checked for 10 minutes and if the latency is 0, then a job queue process will be waiting for messages to be enqueued for the destination and as soon as a message is enqueued it will be propagated. |
| `destination_queue` | Name of the target queue to which messages are to be propagated in the form of a `dblink` |

---

### ALTER\_QUEUE Procedure

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

Table 23-15 ALTER\_QUEUE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `queue_name` | Name of the queue that is to be altered |
| `max_retries` | Limits the number of times a dequeue with `REMOVE` mode can be attempted on a message. The maximum value of `max_retries` is 2\*\*31 -1.  A message is moved to an exception queue if `RETRY_COUNT` is greater than `MAX_RETRIES`. `RETRY_COUNT` is incremented when the application issues a rollback after executing the dequeue. If a dequeue transaction fails because the server process dies (including `ALTER` `SYSTEM` `KILL` `SESSION`) or `SHUTDOWN` `ABORT` on the instance, then `RETRY_COUNT` is not incremented.  Note that `max_retries` is supported for all single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| `retry_delay` | Delay time in seconds before this message is scheduled for processing again after an application rollback. The default is `NULL`, which means that the value will not be altered.  Note that `retry_delay` is supported for single consumer queues and 8.1-compatible or higher multiconsumer queues but not for 8.0-compatible multiconsumer queues. |
| `retention_time` | Retention time in seconds for which a message is retained in the queue table after being dequeued. The default is `NULL`, which means that the value will not be altered. |
| `auto_commit` | `TRUE` causes the current transaction, if any, to commit before the `ALTER_QUEUE` operation is carried out. The `ALTER_QUEUE` operation become persistent when the call returns. This is the default. `FALSE` means the operation is part of the current transaction and becomes persistent only when the caller enters a commit.  Caution: This parameter has been deprecated. |