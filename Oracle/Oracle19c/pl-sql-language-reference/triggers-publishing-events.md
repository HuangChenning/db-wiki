---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/triggers-publishing-events.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Triggers for Publishing Events

To use a trigger to publish an event, create a trigger that:

- Has the event as its triggering event
- Invokes the appropriate subprograms in the `DBMS_AQ` package, which provides an interface to Oracle Advanced Queuing (AQ)
	For information about the `DBMS_AQ` package, see [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ARPLS004).
	For information about AQ, see [Oracle Database Advanced Queuing User's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/lnpls&id=ADQUE1400).

By enabling and disabling such triggers, you can turn event notification on and off. For information about enabling and disabling triggers, see " [Trigger Enabling and Disabling](trigger-enabling-and-disabling.md) ".

How Triggers Publish Events

When the database detects an event, it fires all enabled triggers that are defined on that event, except:

- Any trigger that is the target of the triggering event.
	For example, a trigger for all `DROP` events does not fire when it is dropped itself.
- Any trigger that was modified, but not committed, in the same transaction as the triggering event.
	For example, if a recursive DDL statement in a system trigger modifies another trigger, then events in the same transaction cannot fire the modified trigger.

When a trigger fires and invokes AQ, AQ publishes the event and passes to the trigger the publication context and specified attributes. The trigger can access the attributes by invoking event attribute functions.

The attributes that a trigger can specify to AQ (by passing them to AQ as `IN` parameters) and then access with event attribute functions depends on the triggering event, which is either a database event or a client event.

Note:

- A trigger always behaves like a definer rights (DR) unit. The trigger action of an event runs as the definer of the action (as the definer of the package or function in callouts, or as owner of the trigger in queues). Because the owner of the trigger must have `EXECUTE` privileges on the underlying queues, packages, or subprograms, this action is consistent. For information about DR units, see " [Invoker's Rights and Definer's Rights (AUTHID Property)](invokers-rights-and-definers-rights-authid-property.md) ".
- The database ignores the return status from callback functions for all events. For example, the database does nothing with the return status from a `SHUTDOWN` event.

Topics

### Event Attribute Functions

By invoking system-defined event attribute functions in Table 9-5, a trigger can retrieve certain attributes of the triggering event. Not all triggers can invoke all event attribute functions—for details, see " Event Attribute Functions for Database Event Triggers " and " Event Attribute Functions for Client Event Triggers ".

Note:

- In earlier releases, you had to access these functions through the `SYS` package. Now Oracle recommends accessing them with their public synonyms (the names starting with `ora_` in the first column of Table 9-5).
- The function parameter `ora_name_list_t` is defined in package `DBMS_STANDARD` as:
	```
	TYPE ora_name_list_t IS TABLE OF VARCHAR2(2*(ORA_MAX_NAME_LEN+2)+1);
	```

Table 9-5 System-Defined Event Attributes

| Attribute | Return Type and Value | Example |
| --- | --- | --- |
| ``` ora_client_ip_address ``` | `VARCHAR2`: IP address of client in `LOGON` event when underlying protocol is TCP/IP | ``` DECLARE   v_addr VARCHAR2(11); BEGIN   IF (ora_sysevent = 'LOGON') THEN     v_addr := ora_client_ip_address;   END IF; END; / ``` |
| ``` ora_database_name ``` | `VARCHAR2(50)`: Database name | ``` DECLARE   v_db_name VARCHAR2(50); BEGIN   v_db_name := ora_database_name; END; / ``` |
| ``` ora_des_encrypted_password ``` | `VARCHAR2`: DES-encrypted password of user being created or altered | ``` IF (ora_dict_obj_type = 'USER') THEN   INSERT INTO event_table   VALUES (ora_des_encrypted_password); END IF; ``` |
| ``` ora_dict_obj_name ``` | `VARCHAR2(128)`: Name of dictionary object on which DDL operation occurred | ``` INSERT INTO event_table  VALUES ('Changed object is ' \|\|         ora_dict_obj_name); ``` |
| ``` ora_dict_obj_name_list ( name_list OUT ora_name_list_t ) ``` | `PLS_INTEGER`: Number of object names modified in event  `OUT` parameter: List of object names modified in event | ``` DECLARE   name_list ora_name_list_t;   number_modified PLS_INTEGER; BEGIN   IF (ora_sysevent='ASSOCIATE STATISTICS') THEN     number_modified :=      ora_dict_obj_name_list(name_list);   END IF; END; ``` |
| ``` ora_dict_obj_owner ``` | `VARCHAR2(128)`: Owner of dictionary object on which DDL operation occurred | ``` INSERT INTO event_table VALUES ('object owner is' \|\|          ora_dict_obj_owner); ``` |
| ``` ora_dict_obj_owner_list ( owner_list OUT ora_name_list_t ) ``` | `PLS_INTEGER`: Number of owners of objects modified in event  `OUT` parameter: List of owners of objects modified in event | ``` DECLARE   owner_list ora_name_list_t;   number_modified PLS_INTEGER; BEGIN   IF (ora_sysevent='ASSOCIATE STATISTICS') THEN     number_modified :=       ora_dict_obj_name_list(owner_list);   END IF; END; ``` |
| ``` ora_dict_obj_type ``` | `VARCHAR2(20)`: Type of dictionary object on which DDL operation occurred | ``` INSERT INTO event_table VALUES ('This object is a ' \|\|          ora_dict_obj_type); ``` |
| ``` ora_grantee ( user_list OUT ora_name_list_t ) ``` | `PLS_INTEGER`: Number of grantees in grant event  `OUT` parameter: List of grantees in grant event | ``` DECLARE   user_list ora_name_list_t;   number_of_grantees PLS_INTEGER; BEGIN   IF (ora_sysevent = 'GRANT') THEN     number_of_grantees :=       ora_grantee(user_list);   END IF; END; ``` |
| ``` ora_instance_num ``` | `NUMBER`: Instance number | ``` IF (ora_instance_num = 1) THEN   INSERT INTO event_table VALUES ('1'); END IF; ``` |
| ``` ora_is_alter_column ( column_name IN VARCHAR2 ) ``` | `BOOLEAN`: `TRUE` if specified column is altered, `FALSE` otherwise | ``` IF (ora_sysevent = 'ALTER' AND   ora_dict_obj_type = 'TABLE') THEN      alter_column := ora_is_alter_column('C'); END IF; ``` |
| ``` ora_is_creating_nested_table ``` | `BOOLEAN`: `TRUE` if current event is creating nested table, `FALSE` otherwise | ``` IF (ora_sysevent = 'CREATE' AND   ora_dict_obj_type = 'TABLE' AND   ora_is_creating_nested_table) THEN     INSERT INTO event_table     VALUES ('A nested table is created'); END IF; ``` |
| ``` ora_is_drop_column ( column_name IN VARCHAR2 ) ``` | `BOOLEAN`: `TRUE` if specified column is dropped, `FALSE` otherwise | ``` IF (ora_sysevent = 'ALTER' AND   ora_dict_obj_type = 'TABLE') THEN     drop_column := ora_is_drop_column('C'); END IF; ``` |
| ``` ora_is_servererror ( error_number IN VARCHAR2 ) ``` | `BOOLEAN`: `TRUE` if given error is on error stack, `FALSE` otherwise | ``` IF ora_is_servererror(error_number) THEN   INSERT INTO event_table   VALUES ('Server error!!'); END IF; ``` |
| ``` ora_login_user ``` | `VARCHAR2(128)`: Login user name | ``` SELECT ora_login_user FROM DUAL; ``` |
| ``` ora_partition_pos ``` | `PLS_INTEGER`: In `INSTEAD` `OF` trigger for `CREATE` `TABLE`, position in SQL text where you can insert `PARTITION` clause | ``` -- Retrieve ora_sql_txt into  sql_text variable v_n := ora_partition_pos; v_new_stmt := SUBSTR(sql_text,1,v_n - 1)               \|\| ' ' \|\| my_partition_clause               \|\| ' ' \|\| SUBSTR(sql_text, v_n)); ``` |
| ``` ora_privilege_list ( privilege_list OUT ora_name_list_t ) ``` | `PLS_INTEGER`: Number of privileges in grant or revoke event  `OUT` parameter: List of privileges granted or revoked in event | ``` DECLARE   privilege_list ora_name_list_t;   number_of_privileges PLS_INTEGER; BEGIN   IF (ora_sysevent = 'GRANT' OR       ora_sysevent = 'REVOKE') THEN     number_of_privileges :=       ora_privilege_list(privilege_list);   END IF; END; ``` |
| ``` ora_revokee ( user_list OUT ora_name_list_t ) ``` | `PLS_INTEGER`: Number of revokees in revoke event  `OUT` parameter: List of revokees in event | ``` DECLARE   user_list ora_name_list_t;   number_of_users PLS_INTEGER; BEGIN   IF (ora_sysevent = 'REVOKE') THEN     number_of_users := ora_revokee(user_list);   END IF; END; ``` |
| ``` ora_server_error ( position IN PLS_INTEGER ) ``` | `NUMBER`: Error code at given position on error stack <sup>Foot 1</sup> | ``` INSERT INTO event_table VALUES ('top stack error ' \|\|          ora_server_error(1)); ``` |
| ``` ora_server_error_depth ``` | `PLS_INTEGER`: Number of error messages on error stack | ``` n := ora_server_error_depth; -- Use n with functions such as ora_server_error ``` |
| ``` ora_server_error_msg ( position IN PLS_INTEGER ) ``` | `VARCHAR2`: Error message at given position on error stack <sup>Foot 1</sup> | ``` INSERT INTO event_table VALUES ('top stack error message' \|\|         ora_server_error_msg(1)); ``` |
| ``` ora_server_error_num_params ( position IN PLS_INTEGER ) ``` | `PLS_INTEGER`: Number of strings substituted into error message (using format like `%s`) at given position on error stack <sup>Foot 1</sup> | ``` n := ora_server_error_num_params(1); ``` |
| ``` ora_server_error_param ( position IN PLS_INTEGER, param IN PLS_INTEGER ) ``` | `VARCHAR2`: Matching substitution value (`%s`, `%d`, and so on) in error message at given position and parameter number <sup>Foot 1</sup> | ``` -- Second %s in "Expected %s, found %s": param := ora_server_error_param(1,2); ``` |
| ``` ora_sql_txt ( sql_text OUT ora_name_list_t ) ``` | `PLS_INTEGER`: Number of elements in PL/SQL table  `OUT` parameter: SQL text of triggering statement (broken into multiple collection elements if statement is long) | ``` CREATE TABLE event_table (col VARCHAR2(2030));  DECLARE   sql_text ora_name_list_t;   n PLS_INTEGER;   v_stmt VARCHAR2(2000); BEGIN   n := ora_sql_txt(sql_text);    FOR i IN 1..n LOOP     v_stmt := v_stmt \|\| sql_text(i);   END LOOP;    INSERT INTO event_table VALUES ('text of     triggering statement: ' \|\| v_stmt); END; ``` |
| ``` ora_sysevent ``` | `VARCHAR2(20)`: Name of triggering event, as given in syntax | ``` INSERT INTO event_table VALUES (ora_sysevent); ``` |
| ``` ora_with_grant_option ``` | `BOOLEAN`: `TRUE` if privileges are granted with `GRANT` option, `FALSE` otherwise | ``` IF (ora_sysevent = 'GRANT' AND   ora_with_grant_option = TRUE) THEN     INSERT INTO event_table      VALUES ('with grant option'); END IF; ``` |
| ``` ora_space_error_info ( error_number OUT NUMBER, error_type OUT VARCHAR2, object_owner OUT VARCHAR2, table_space_name OUT VARCHAR2, object_name OUT VARCHAR2, sub_object_name OUT VARCHAR2 ) ``` | `BOOLEAN`: `TRUE` if error is related to out-of-space condition, `FALSE` otherwise  `OUT` parameters: Information about object that caused error | ``` IF (ora_space_error_info (      eno,typ,owner,ts,obj,subobj) = TRUE) THEN   DBMS_OUTPUT.PUT_LINE('The object '\|\| obj      \|\| ' owned by ' \|\| owner \|\|      ' has run out of space.'); END IF; ``` |

<sup>Footnote 1</sup>

Position 1 is the top of the stack.

### Event Attribute Functions for Database Event Triggers

Table 9-6 summarizes the database event triggers that can invoke event attribute functions. For more information about the triggering events in Table 9-6, see " [database\_event](CREATE-TRIGGER-statement.md) ".

Table 9-6 Database Event Triggers

| Triggering Event | When Trigger Fires | WHEN Conditions | Restrictions | Transaction | Attribute Functions |
| --- | --- | --- | --- | --- | --- |
| ``` AFTER STARTUP ``` | When database is opened. | None allowed | Trigger cannot do database operations. | Starts a separate transaction and commits it after firing the triggers. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ``` |
| ``` BEFORE SHUTDOWN ``` | Just before server starts shutdown of an instance.  This lets the cartridge shutdown completely. For abnormal instance shutdown, this trigger might not fire. | None allowed | Trigger cannot do database operations. | Starts separate transaction and commits it after firing triggers. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ``` |
| ``` AFTER DB_ROLE_CHANGE ``` | When database is opened for first time after role change. | None allowed | None | Starts separate transaction and commits it after firing triggers. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ``` |
| ``` AFTER SERVERERROR ``` | With condition, whenever specified error occurs. Without condition, whenever any error occurs.  Trigger does not fire for errors listed in " [database\_event](CREATE-TRIGGER-statement.md) ". | `ERRNO` = `eno` | Depends on error. | Starts separate transaction and commits it after firing triggers. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_server_error ora_is_servererror ora_space_error_info ``` |

### Event Attribute Functions for Client Event Triggers

Table 9-7 summarizes the client event triggers that can invoke event attribute functions. For more information about the triggering events in Table 9-7, see " [ddl\_event](CREATE-TRIGGER-statement.md) " and " [database\_event](CREATE-TRIGGER-statement.md) ".

Note:

If a client event trigger becomes the target of a DDL operation (such as `CREATE` `OR` `REPLACE` `TRIGGER`), then it cannot fire later during the same transaction.

Table 9-7 Client Event Triggers

| Triggering Event | When Trigger Fires | WHEN Conditions | Restrictions | Transaction | Attribute Functions |
| --- | --- | --- | --- | --- | --- |
| ``` BEFORE ALTER  AFTER ALTER ``` | When catalog object is altered | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent  ora_login_user ora_instance_num ora_database_name ora_dict_obj_type  ora_dict_obj_name ora_dict_obj_owner ora_des_encrypted_password  (for ALTER USER events) ora_is_alter_column  (for ALTER TABLE events) ora_is_drop_column  (for ALTER TABLE events) ``` |
| ``` BEFORE DROP  AFTER DROP ``` | When catalog object is dropped | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_type ora_dict_obj_name ora_dict_obj_owner ``` |
| ``` BEFORE ANALYZE  AFTER ANALYZE ``` | When `ANALYZE` statement is issued | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ``` |
| ``` BEFORE ASSOCIATE STATISTICS  AFTER ASSOCIATE STATISTICS ``` | When `ASSOCIATE` `STATISTICS` statement is issued | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ora_dict_obj_name_list ora_dict_obj_owner_list ``` |
| ``` BEFORE AUDIT  AFTER AUDIT  BEFORE NOAUDIT  AFTER NOAUDIT ``` | When `AUDIT` or `NOAUDIT` statement is issued | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ``` |
| ``` BEFORE COMMENT  AFTER COMMENT ``` | When object is commented | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ``` |
| ``` BEFORE CREATE  AFTER CREATE ``` | When catalog object is created | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent  ora_login_user ora_instance_num ora_database_name ora_dict_obj_type  ora_dict_obj_name ora_dict_obj_owner ora_is_creating_nested_table  (for CREATE TABLE events) ``` |
| ``` BEFORE DDL  AFTER DDL ``` | When most SQL DDL statements are issued. Not fired for `ALTER` `DATABASE`, `CREATE` `CONTROLFILE`, `CREATE` `DATABASE`, and DDL issued through the PL/SQL subprogram interface, such as creating an advanced queue. | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ``` |
| ``` BEFORE DISASSOCIATE STATISTICS  AFTER DISASSOCIATE STATISTICS ``` | When `DISASSOCIATE` `STATISTICS` statement is issued | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ora_dict_obj_name_list ora_dict_obj_owner_list ``` |
| ``` BEFORE GRANT  AFTER GRANT ``` | When `GRANT` statement is issued | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ora_grantee ora_with_grant_option ora_privilege_list ``` |
| ``` BEFORE LOGOFF ``` | At start of user logoff | Simple conditions on `UID` and `USER` | DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ``` |
| ``` AFTER LOGON ``` | After successful user logon | Simple conditions on `UID` and `USER` | DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Starts separate transaction and commits it after firing triggers. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_client_ip_address ``` |
| ``` BEFORE RENAME  AFTER RENAME ``` | When `RENAME` statement is issued | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_owner ora_dict_obj_type ``` |
| ``` BEFORE REVOKE  AFTER REVOKE ``` | When `REVOKE` statement is issued | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ora_revokee ora_privilege_list ``` |
| ``` AFTER SUSPEND ``` | After SQL statement is suspended because of out-of-space condition.  (Trigger must correct condition so statement can be resumed.) | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_server_error ora_is_servererror ora_space_error_info ``` |
| ``` BEFORE TRUNCATE  AFTER TRUNCATE ``` | When object is truncated | Simple conditions on type and name of object, `UID`, and `USER` | Trigger cannot do DDL operations on object that caused event to be generated.  DDL on other objects is limited to compiling an object, creating a trigger, and creating, altering, and dropping a table. | Fires triggers in current transaction. | ``` ora_sysevent ora_login_user ora_instance_num ora_database_name ora_dict_obj_name ora_dict_obj_type ora_dict_obj_owner ``` |