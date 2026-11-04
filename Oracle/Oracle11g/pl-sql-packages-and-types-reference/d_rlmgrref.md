---
title: DBMS_RLMGR
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_rlmgrref.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 124 DBMS\_RLMGR

Note:

This functionality is deprecated with Oracle Database Release 11.2 and obsoleted with Release 12.1. For details regarding obsolescence, seeMy Oracle Support Note [ID 1244535.1](https://support.oracle.com/CSP/ui/flash.html#tab=KBHome%28page=KBHome&id=%28%29%29,%28page=KBNavigator&id=%28from=BOOKMARK&bmDocType=DESUPPORT&bmDocID=1244535.1&bmDocDsrc=KB&viewingMode=1143&bmDocTitle=Obsolescence%20Notice:%20Rules%20Manager%20Feature%20of%20Oracle%20Database%29%29)

The `DBMS_RLMGR` package contains various procedures to create and manage rules and rule sessions by the Rules Manager.

See Also:

[Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/toc.htm) for more information.

This chapter contains the following topic:

- Using DBMS\_RLMGR
- Summary of Rules Manager Subprograms

---

## Using DBMS\_RLMGR

This section contains topics that relate to using the Rules Manager `DBMS_RLMGR` package.

- Security Model

---

### Security Model

The Oracle Database installation runs the `catrul.sql` script to load the `DBMS_RLMGR` package and create the required Rules Manager schema objects in the `EXFSYS` Schema.

`DBMS_RLMGR` is an `EXFSYS` -owned package compiled with `AUTHID CURRENT_USER`. Any `DBMS_RLMGR` subprogram called from an anonymous PL/SQL block is run using the privileges of the current user.

A user must be granted `CONNECT` and `RESOURCE` roles, `EXECUTE` privilege on `DBMS_LOCK`, and `CREATE VIEW` privilege to use this package.

For successful creation of a rule class, you must have sufficient privileges to create views, object types, tables, packages, and procedures.

The owner of the rule class always has privileges to drop a rule class, process rules in a rule class, add rules and delete rules from a rules class. Only the owner of the rule class can drop a rule class and this privilege cannot be granted to another user. Rule class privileges cannot be revoked from the owner of the rule class.

A user who is not the owner of the rule class must be granted appropriate types of privileges to perform certain tasks. The types of privileges that can be granted are:

- `PROCESS RULES`: A user with `PROCESS RULES` privilege on a rule class can process the rules in the rule class using the `PROCESS_RULES` procedure or the `ADD_EVENT` procedure. Also, the user with this privilege can select from the corresponding rule class results view.
- `ADD RULE`: A user with `ADD RULE` privilege on a rule class can add rules to a rule class. Alternatively, the owner of the rule class can grant the `INSERT` privilege on one rule class table to other users.
- `DELETE RULE`: A user with `DELETE RULE` privilege on a rule class can delete rules from a rule class. Alternatively, the owner of the rule class can grant the `DELETE` privilege on one rule class table to other users.
- `ALL`: Granting the `ALL` privilege on a rule class is equivalent to granting all the above privileges on the rule class to the user.

A user must have the `EXECUTE` privilege on the primitive event types associated with a rule class before that user can make use of the corresponding rule class results view.

The owner of the rule class can add the rules using `SQL INSERT` statement on the rule class table (that shares the same name as the rule class). Note that the owner of the rule class can also grant direct DML privileges on the rule class table to other users. When you use the schema extended name for the rule class, the user must have the `ADD RULE` privilege on the rule class to add a rule to the rule class.

The owner of the rule class can use an `SQL DELETE` statement on one rule class table to delete a rule. When you use the schema extended name for the rule class, the user must have the `DELETE RULE` privilege on the rule class.

When the schema extended name is used for the rule class, the user must have `PROCESS RULES` privilege on the rule class.

A user must have `EXECUTE` privilege on the `CTX_DDL` package for successful synchronization of the text indexes using the `DBMS_RLMGR.SYNC_TEXT_INDEXES` procedure.

The `USER_RLMGR_PRIVILEGES` view lists privileges of the current user for the rule classes.

---

## Summary of Rules Manager Subprograms

Table 124-1 describes the subprograms in the `DBMS_RLMGR` package.

All the values and names passed to the procedures defined in the `DBMS_RLMGR` package are case insensitive unless otherwise mentioned. To preserve the case, enclose the values with double quotation marks.

Table 124-1 DBMS\_RLMGR Package Subprograms

| Subprogram | Description |
| --- | --- |
| ADD\_ELEMENTARY\_ATTRIBUTE Procedures | Adds the specified attribute to the event structure and the Expression Filter attribute set |
| ADD\_EVENT Procedure | Adds an event to a rule class in an active session |
| ADD\_FUNCTIONS Procedure | Adds a Function, a Type, or a Package to the approved list of functions with an event structure and to the Expression Filter attribute set |
| ADD\_RULE Procedure | Adds a rule to the rule class |
| CONDITION\_REF Function | Retrieves the primitive rule condition reference from a rule condition for composite events |
| CONSUME\_EVENT Function | Consumes an event using its identifiers and prepares the corresponding rule for action execution |
| CONSUME\_PRIM\_EVENTS Function | Consumes one or more primitive events with all or none semantics |
| CREATE\_CONDITIONS\_TABLE Procedure | Creates a repository for the primitive rule conditions that can be shared by multiple rules from the same or different rule classes |
| CREATE\_EVENT\_STRUCT Procedure | Creates an event structure |
| CREATE\_EXPFIL\_INDEXES Procedure | Creates expression filter indexes for the rule class if the default indexes have been dropped |
| CREATE\_INTERFACE Procedure | Creates a rule class interface package to directly operate on the rule class |
| CREATE\_RULE\_CLASS Procedure | Creates a rule class |
| DELETE\_RULE Procedure | Deletes a rule from a rule class |
| DROP\_CONDITIONS\_TABLE Procedure | Drops the conditions table |
| DROP\_EVENT\_STRUCT Procedure | Drops an event structure |
| DROP\_EXPFIL\_INDEXES Procedure | Drops Expression Filter indexes for the rule conditions |
| DROP\_INTERFACE Procedure | Drops the rule class interface package |
| DROP\_RULE\_CLASS Procedure | Drops a rule class |
| EXTEND\_EVENT\_STRUCT Procedure | Adds an attribute to the primitive event structure |
| GET\_AGGREGATE\_VALUE Function | Retrieves the aggregate value computed for a collection event |
| GRANT\_PRIVILEGE Procedure | Grants a privilege on a rule class to another user |
| PROCESS\_RULES Procedure | Process the rules for a given event |
| PURGE\_EVENTS Procedure | Resets the rule class by removing all the events associated with the rule class and purging any state information pertaining to rules matching some events |
| RESET\_SESSION Procedure | Starts a new rule session within a database session |
| REVOKE\_PRIVILEGE Procedure | Revokes a privilege on a rule class from a user |
| SYNC\_TEXT\_INDEXES Procedure | Synchronizes the indexes defined to process the predicates involving the `CONTAINS` operator in rule conditions |

---

### ADD\_ELEMENTARY\_ATTRIBUTE Procedures

This procedure adds the specified attribute to an event structure, which is also the Expression Filter attribute set. The procedure is overloaded. The different functionality of each form of syntax is presented along with the definitions.

Syntax

Adds the specified elementary attribute to the attribute set:

```
DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
              event_struct   IN   VARCHAR2,
              attr_name      IN   VARCHAR2,
              attr_type      IN   VARCHAR2,
              attr_defvl     IN   VARCHAR2 default NULL);
```

Identifies the elementary attributes that are table aliases and adds them to the event structure:

```
DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
              event_struct   IN   VARCHAR2,
              attr_name      IN   VARCHAR2,
              tab_alias      IN   rlm$table_alias);
```

Allows addition of text attributes to the attribute set:

```
DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
              event_struct   IN   VARCHAR2,
              attr_name      IN   VARCHAR2,
              attr_type      IN   VARCHAR2,
              text_pref      IN   EXF$TEXT);
```

Parameters

Table 124-2 ADD\_ELEMENTARY\_ATTRIBUTE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `event_struct` | Name of the event structure or attribute set to which this attribute is added |
| `attr_name` | Name of the elementary attribute to be added. No two attributes in a set can have the same name. |
| `attr_type` | Datatype of the attribute. This argument accepts any standard SQL datatype or the name of an object type that is accessible to the current user. |
| `tab_alias` | The type that identifies the database table to which the attribute is aliased |
| `attr_defv1` | Default value for the elementary attribute |
| `text_pref` | Text preferences such as LEXER and WORDLIST specification |

Usage Notes

- This procedure adds an elementary attribute to an event structure. The event structure is internally managed as the Expression Filter attribute set. If the event structure was originally created from an existing object type, then additional attributes cannot be added.
	Elementary attributes cannot be added to an attribute set that is already assigned to a column storing expressions, which is equivalent to an event structure that is used for a rule class.
- One or more, or all elementary attributes in an attribute set can be table aliases. If an elementary attribute is a table alias, then the value assigned to the elementary attribute is a `ROWID` from the corresponding table. An attribute set with one or more table alias attributes cannot be created from an existing object type. For more information about table aliases, see [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_app_a.htm#EXPRN111).
- You cannot add elementary attributes to an attribute set that is already assigned to a column storing expressions.
- See the section on defining attribute sets in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN011) for more information about adding elementary attributes.
- Related views: `USER_EXPFIL_ATTRIBUTE_SETS` and `USER_EXPFIL_ATTRIBUTES`.
- This procedure with a text preference bound to the `text_pref` argument creates a text attribute in the attribute set. The data type for such an attribute should be a `VARCHAR2` or a `CLOB`. The preferences specified for a text attribute are used to process the predicates involving `CONTAINS` operator on the attributes. The valid preferences are those that are valid in the `PARAMETERS` clause of `CTXRULE` index creation. See [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) for the syntax.

Examples

The following command adds two elementary attributes to an attribute set:

```
BEGIN
  DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
                       EVENT_STRUCT => 'HRAttrSet',
                       ATTR_NAME => 'HRREP',
                       attr_type => 'VARCHAR2'); 
  DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
                       EVENT_STRUCT => 'HRAttrSet',
                       ATTR_NAME => 'DEPT',
                       TAB_ALIAS => RLM$TABLE_ALIAS('DEPT')); 
END;
```

The following commands create an attribute set with each hotel reservation including some additional information, described as the `AddlInfo` attribute of `CLOB` data type. Rule conditions specified for this event structure can include text predicates on this attribute.

```
BEGIN
  DBMS_RLMGR.CREATE_EVENT_STRUCT (EVENT_STRUCT => 'AddFlight'); 
  DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
                       EVENT_STRUCT => 'AddHotel',
                       ATTR_NAME => 'CustId',
                       ATTR_TYPE => 'NUMBER'); 
  DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
                       EVENT_STRUCT => 'AddHotel',
                       ATTR_NAME => 'Type',
                       ATTR_TYPE => 'VARCHAR2(20)'); 
  . . . 
  DBMS_RLMGR.ADD_ELEMENTARY_ATTRIBUTE (
                       EVENT_STRUCT => 'AddHotel',
                       ATTR_NAME => 'AddlInfo',
                       ATTR_TYPE => 'CLOB',
                       TEXT_PREF => EXF$TEXT('LEXER hotelreserv_lexer')); 
END;
```

---

### ADD\_EVENT Procedure

This procedure adds a primitive event to a rule class in an active rule session. The procedure is overloaded. The different functionality of each form of syntax is presented along with the definitions.

Syntax

Adds a string representation of the primitive event instance to a rule class:

```
DBMS_RLMGR.ADD_EVENT (
   rule_class      IN VARCHAR2,
   event_inst      IN VARCHAR2,
   event_type      IN VARCHAR2 default null);
```

Adds an AnyData representation of the primitive event instance to a rule class:

```
DBMS_RLMGR.ADD_EVENT (
   rule_class      IN VARCHAR2,
   event_inst      IN sys.AnyData);
```

Parameters

Table 124-3 ADD\_EVENT Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class. A schema extended rule class name can be used to refer to a rule class that does not belong to the current schema. |
| `event_inst` | String or AnyData representation of the event instance being added to the rule class |
| `event_type` | Type of event instance assigned to the `event_inst` argument when the string representation of the event instance is used for a rule class configured for composite events |

Usage Notes

- This procedure is used to add a primitive or a simple event to a rule class within an active rule session. By default, a rule session is the same as the database session. Optionally, multiple (sequential) rule sessions can be started within a database session by using the `RESET_SESSION` or `PROCESS_RULES` procedures.
- When the rule class is configured for simple events (consisting of only one primitive event structure), the `event_type` argument for the `ADD_EVENT` procedure can be ignored. Also, when the AnyData format of the event instance is passed, the event type information is embedded in the AnyData instance. In all other cases, the name of the primitive event structure being added to the rule class should be assigned to the `event_type` argument.
- For a valid event instance, the `ADD_EVENT` procedure processes the rules in the rule class and captures the results in the rule class results view (configured at the time of rule class creation). These results are preserved until the end of the rule session.When schema extended name is used for the rule class, you should have `PROCESS` `RULES` privilege on the rule class. See the GRANT\_PRIVILEGE Procedure for additional information. The value specified for the `event_type` argument is always resolved in the rule class owner's schema and should not use schema extended names. When a composite event structure is configured with a table alias primitive event type, the name of the corresponding table should be assigned to the `event_type` argument.

Examples

The following commands add two events to the `CompTravelPromo` rule class that is configured for two types of primitive events (`AddFlight` and `AddRentalCar`).

```
BEGIN
 DBMS_RLMGR.ADD_EVENT(rule_class => 'CompTravelPromo',
                     event_inst =>
                        AddFlight.getVarchar(987, 'Abcair', 'Boston',
                                         'Orlando', '01-APR-2003', '08-APR-2003'),
                     event_type => 'AddFlight');

DBMS_RLMGR.ADD_EVENT(rule_class => 'Scott.CompTravelPromo',
                     event_inst =>
                        AnyData.convertObject(
                                        AddRentalCar(987, 'Luxury', '03-APR-2003',
                                                     '08-APR-2003', NULL)));
END;/
```

---

### ADD\_FUNCTIONS Procedure

This procedure adds a user-defined function, package, or type representing a set of functions to the event structure, which is also the Expression Filter attribute set.

Syntax

```
DBMS_RLMGR.ADD_FUNCTIONS (
   event_struct   IN   VARCHAR2,
   funcs_name     IN   VARCHAR2);
```

Parameters

Table 124-4 ADD\_FUNCTIONS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `event_struct` | Name of the event structure to which the functions are added |
| `funcs_name` | Name of a function, package, or type (representing a function set) or its synonyms |

Usage Notes

- By default, an attribute set implicitly allows references to all Oracle Database-supplied SQL functions for use in the rule conditions. If the expression set refers to a user-defined function, the expression set must be explicitly added to the attribute set.
- The `ADD_FUNCTIONS` procedure adds a user-defined function or a package (or type) representing a set of functions to the attribute set. Any new or modified expressions are validated using this list.
- You can specify the function or the package name with a schema extension. If you specify a function name without a schema extension, only such references in the rule condition are considered valid. You can restrict the conditional expression to use a synonym to a function or a package by adding the corresponding synonym to the attribute set. This preserves the portability of the expression set to other schemas.
- See the section on defining attribute sets in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_expconcepts.htm#EXPRN011) for more information about adding functions to an attribute set.
- Related views: [`USER_EXPFIL_ATTRIBUTE_SETS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN056) and [`USER_EXPFIL_ASET_FUNCTIONS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN054)

Examples

The following command adds two functions to the attribute set:

```
BEGIN 
  DBMS_RLMGR.ADD_FUNCTIONS (attr_set   => 'Car4Sale', 
                             funcs_name => 'HorsePower');
  DBMS_RLMGR.ADD_FUNCTIONS (attr_set   => 'Car4Sale', 
                             funcs_name => 'Scott.CrashTestRating');
END;
/
```

---

### ADD\_RULE Procedure

This procedure adds new rules to a rule class.

Syntax

```
DBMS_RLMGR.ADD_RULE (
   rule_class      IN  VARCHAR2,
   rule_id         IN  VARCHAR2,
   rule_cond       IN  VARCHAR2,
   actprf_nml      IN  VARCHAR2 DEFAULT NULL,
   actprf_vall     IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 124-5 ADD\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class. A schema extended rule class name can be used to refer to a rule class that does not belong to the current schema. |
| `rule_id` | Unique identifier for the rule within the rule class |
| `rule_cond` | The condition for the rule. The condition uses the variables defined in the rule class's event structure. |
| `actprf_nml` | The list of action preference names for which values will be assigned through the `actprf_vall` argument |
| `actprf_vall` | The list of action preference values for the names list assigned to the `actprf_nml` argument |

Usage Notes

- This procedure is used to add new rules to the rule class. The rule condition passed to the `ADD_RULE` procedure is validated using the event structure associated with the rule class. The action preferences names list is a subset of action preference categories configured during rule class creation.
- When schema extended name is used for the rule class, you should have `ADD` `RULE` privilege on the rule class. See the GRANT\_PRIVILEGE Procedure for more information.
- Alternately, the owner of the rule class can add the rules using SQL `INSERT` statement on the rule class table (that shares the same name as the rule class). Note that the owner of the rule class can also grant direct DML privileges on the rule class table to other users.
	Note:
	The `AUTOCOMMIT` property of the rule class is ignored if the new rules are added using the SQL `INSERT` statement instead of the `ADD_RULE` procedure.
- See the CREATE\_RULE\_CLASS Procedure procedure for the structure of the rule class table.

Examples

The following command adds a rule to the rule class.

```
BEGIN
DBMS_RLMGR.ADD_RULE (
           rule_class => 'CompTravelPromo',
           rule_id => 'AB_AV_FL',
           rule_cond =>
             '<condition>
                 <and join="Flt.CustId = Car.CustId">
                    <object name="Flt">
                      Airline=''Abcair'' and ToCity=''Orlando''
                    </object>
                    <object name="Car">
                      CarType = ''Luxury''
                    </object>
                  </and>
               </condition>' ,
             actprf_nml => 'PromoType, OfferedBy',
             actprf_vall => '''RentalCar'', ''Acar''');
END;
```

With proper privileges, the following SQL `INSERT` statement can be used to add the rule to the rule class.

```
INSERT INTO CompTravelPromo (rlm$ruleid, rlm$rulecond, PromoType, OfferedBy)
  VALUES ('AB_AV_FL',
          '<condition>
             <and join="Flt.CustId = Car.CustId">
               <object name="Flt">
                   Airline=''Abcair'' and ToCity=''Orlando''
               </object>
               <object name="Car">
                   CarType = ''Luxury''
               </object>
             </and>
           </condition>',
          'RentalCar','Acar');
```

---

### CONDITION\_REF Function

This function retrieves the primitive rule condition reference from a rule condition for composite events.

Syntax

```
DBMS_RLMGR.CONDITION_REF (
     rule_cond IN   VARCHAR2,
     eventnm   IN   VARCHAR2) 
  RETURN VARCHAR2;
```

Parameters

Table 124-6 CONDITION\_REF Function Parameters

| Parameter | Description |
| --- | --- |
| `rule_cond` | Rule condition in XML format |
| `eventnm` | Name of the event for which the reference should be retrieved |

Usage Notes

- For a rule condition in XML format, with a root `<condition>` element, this function retrieves the reference to a shared conditional expression on a particular primitive event.
- Use this function in a query operating on the rule class table to find all the references to a given primitive rule condition. To speed-up such queries, one or more functional indexes are defined on the `rlm$rulecond` column of the rule class table using this function signature. In order to make use of the index for a lookup query, the value assigned to the `eventnm` argument should be case sensitive.

Examples

The following command joins the rule class table with the primitive conditions table to identify all the rule conditions that have references to the shareable primitive conditions (the query uses a functional index defined on the `rlm$rulecond` column). This query identifies all the rule conditions that refer to any shared conditions stored in the `FlightConditions` table.

```
select ctp.rlm$ruleid from CompTravelPromo ctp, FlightConditions fc
where dbms_rlmgr.condition_ref(ctp.rlm$rulecond, 'FLT') = fc.rlm$condid;
```

---

### CONSUME\_EVENT Function

This function consumes an event and prepares the corresponding rule for action execution. This is required only when the action (or rule execution) is carried by the user's application and not in the callback.

Syntax

```
DBMS_RLMGR.CONSUME_EVENT (
   rule_class       IN VARCHAR2,
   event_ident      IN VARCHAR2) 
 RETURN NUMBER;
```

Parameters

Table 124-7 CONSUME\_EVENT Function Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class. A schema extended rule class name can be used to refer to a rule class that does not belong to the current schema. |
| `event_ident` | Event identifier obtained from the corresponding rule class results view (or arguments of the action callback procedure in the case of rule class configured for `RULE` based consumption policy) |

Returns

The function returns:

- `1` -- If the event is successfully consumed.
- `0` -- If the event is expired (owing to duration policy) or consumed by another session prior to this call.

Usage Notes

- When an `EXCLUSIVE` consumption policy is set for the events in a rule class, an event must be deleted from the system immediately after the rule it matched is executed (action is executed). When the rule action is carried in the rule class callback procedure by calling the `PROCESS_RULES` procedure, the rule manager automatically handles the consumption of the events. However, when you request the results from matching events with rules in a rule class results view using the `ADD_EVENT` procedure, you should take appropriate action to indicate the exact rule-event combination that is to be used for rule execution. The `CONSUME_EVENT` function performs the required housekeeping services when the unique identifier for the event used in a rule execution is passed in.
- Because there could be a time lag between fetching the rule class matching results and the execution of the user initiated action, the application must execute the action only if the `CONSUME_EVENT` call succeeds in consuming the event. This avoids any race condition with parallel sessions trying to consume the same events. When the event is successfully consumed, this call returns `1`. In all other cases, it returns `0`. A return value of `0` implies that the event is already consumed by another session and hence it is not available for this session.
- The `CONSUME_EVENT` function deletes the events configured with `EXCLUSIVE` consumption policy and does nothing for events configured for 4 consumption policy.
- Unlike the `EXCLUSIVE` and `SHARED` consumption policies, which are determined at the rule class level, you use a `RULE` consumption policy to determine the consumption of an event on a rule by rule basis. That is a subset of the rules in a rule class may be configured such that when they are matched, the event is deleted from the system. At the same time the other set of rules could leave the event in the system even after executing the corresponding action. In this scenario, the action callback procedure implemented by the application developer can call `CONSUME_EVENT` function (with appropriate arguments) to conditionally consume the event for certain rules. Also see the use of CONSUME\_PRIM\_EVENTS Function for rule classes configured for `RULE` consumption policy

Examples

The following commands identify an event that is used for a rule execution and consumes it using its identifier.

```
var eventid VARCHAR(40);
var evtcnsmd NUMBER;

BEGIN
  SELECT rlm$eventid INTO :eventid FROM MatchingPromos WHERE rownum < 2;

  -- carry the required action for a rule matched by the above event --
  :evtcnsmd := DBMS_RLMGR.CONSUME_EVENT(rule_class  => 'TravelPromotion',
                                        event_ident => :eventid);
END;
```

---

### CONSUME\_PRIM\_EVENTS Function

This function consumes a set of primitive events with all or nothing semantics in the case of a rule class configured with `RULE` based consumption policy.

Syntax

```
DBMS_RLMGR.CONSUME_PRIM_EVENTS (
   rule_class       IN VARCHAR2,
   event_idents     IN RLM$EVENTIDS) 
 RETURN NUMBER;
```

Parameters

Table 124-8 CONSUME\_PRIM\_EVENTS Function Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class. A schema extended rule class name can be used to refer to a rule class that does not belong to the current schema. |
| `event_ident` | Event identifiers obtained from the corresponding rule class results view or the arguments of the action callback procedure |

Returns

The function returns:

- `1` -- If all the events, the identifiers for which are passed in, are successfully consumed.
- `0` -- If one or more primitive event could not be consumed.

Usage Notes

- When you configure the rule class for `RULE` based consumption policy, it uses the `CONSUME_PRIM_EVENTS` function to consume one or more primitive events that constitute a composite event. This operation succeeds only when all the events passed in are still valid and are available for consumption. Any user initiated action must be implemented after checking the return value of the `CONSUME_PRIM_EVENTS` call.

Examples

The following commands show the body of the action callback procedure for a rule class configured for `RULE` consumption policy. This demonstrates the use of `CONSUME_PRIM_EVENTS` function to consume the events before executing the action for the matched rules.

```
create or replace procedure PromoAction (
      Flt        AddFlight, 
      Flt_EvtId  ROWID,    --- rowid for the flight primitive event
      Car        AddRentalCar, 
      Car_EvtId  ROWID, 
      rlm$rule   TravelPromotions%ROWTYPE) is 
  evtcnsmd   NUMBER; 
BEGIN
  evtcnsmd := DBMS_RLMGR.CONSUME_PRIM_EVENTS(
                    rule_class   => 'TravelPromotions',
                    event_idents => RLM$EVENTIDS(Flt_EvtId, Car_EvtId));

  if (evtcnsmd = 1) then 
    -- consume operation was successful; perform the action ---
    OfferPromotion (Flt.CustId, rlm$rule.PromoType, rlm$rule.OfferedBy);
  end if;
END;
/
```

---

### CREATE\_CONDITIONS\_TABLE Procedure

This procedure creates a conditions table, which is a repository for the primitive rule conditions that can be shared by multiple rules from the same or different rule classes. The procedure is overloaded. The different functionality of each form of syntax is presented along with the definitions.

Syntax

Creates a conditions table to store shareable primitive conditions defined for a primitive event.

```
DBMS_RLMGR.CREATE_CONDITIONS_TABLE (
     cond_table    IN  VARCHAR2,
     pevent_struct IN  VARCHAR2,
     stg_clause    IN  VARCHAR2 DEFAULT NULL);
```

Creates a conditions table to store shareable primitive conditions defined for a relational table identified through table aliases.

```
DBMS_RLMGR.CREATE_CONDITIONS_TABLE (
     cond_table    IN  VARCHAR2,
     tab_alias     IN  rlm$table_alias,
     stg_clause    IN  VARCHAR2 DEFAULT NULL);
```

Parameters

Table 124-9 CREATE\_CONDITIONS\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `pevent_struct` | Primitive event structure for which the shareable primitive rule conditions are defined |
| `cond_table` | Name of the table storing the primitive rule conditions |
| `stg_clause` | Storage clause for the conditions table |
| `tab_alias` | Type that identifies the database table for which the shareable primitive rule conditions are defined |

Usage Notes

- This procedure creates a relational table to store the primitive rule conditions that can be shared by multiple rules. It creates the table with the user specified name and it has a `VARCHAR2` column to store the unique identifier for each primitive rule condition (`rlm$condid`), an expression data type column to store the conditional expressions (`rlm$condition`), and a `VARCHAR2` column to store the descriptions for the primitive rule conditions in plain text (`rlm$conddesc`).
- Once it creates the table, the primitive rule condition can be added or modified using standard DML operations on the conditions table. The conditions table is configured to validate the primitive rule conditions (in the `rlm$condition` column) using the primitive event structure specified for the `pevent_struct` argument.
- A rule class configured with a primitive event structure can include some rule conditions that refer to rows in the conditions table using corresponding identifiers.

Examples

The following command creates a conditions table that can store shareable primitive rule conditions for the `AddRentalCar` event structure:

```
BEGIN
  DBMS_RLMGR.CREATE_CONDITIONS_TABLE (
    cond_table    => 'FlightConditions',
    pevent_struct => 'AddFlight', 
    stg_clause    => 'TABLESPACE TBS_1');
END;
/
```

---

### CREATE\_EVENT\_STRUCT Procedure

This procedure creates an event structure.

Syntax

```
DBMS_RLMGR.CREATE_EVENT_STRUCT  (
   event_struct  IN  VARCHAR2);
```

Parameters

Table 124-10 CREATE\_EVENT\_ STRUCT Procedure Parameter

| Parameter | Description |
| --- | --- |
| `event_struct` | Name of the event structure to be created in the current schema |

Usage Notes

- This procedure creates a dummy event structure in the current schema. One or more attributes can be added to this event structure using the `ADD_ELEMENTARY_ATTRIBUTE` procedure.

Examples

The following command creates the event structure.

```
BEGIN  DBMS_RLMGR.CREATE_EVENT_STRUCT(event_struct => 'AddFlight');
END;
```

---

### CREATE\_EXPFIL\_INDEXES Procedure

This procedure creates expression filter indexes for the rule class if the default indexes have been dropped. If a representative set of rules is stored in the rule class table, the indexes can be tuned for these expressions by collecting statistics.

Syntax

```
DBMS_RLMGR.CREATE_EXPFIL_INDEXES  (
   rule_class  IN  VARCHAR2,
   coll_stats  IN  VARCHAR2 default 'NO');
```

Parameters

Table 124-11 CREATE\_EXPFIL\_INDEXES Procedure Parameter

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class |
| `coll_stats` | To collect expression statistics for building the indexes |

Usage Notes

- Expression filter indexes are used to identify the rule conditions in a rule class for appropriate events. The default indexes created at the time of rule class creation assume that all types of predicates (equality, inequality, and so forth) involving scalar attributes in an event structure are equally likely. The performance of a rule class can be improved by tuning the expression filter indexes for a specific workload. This is achieved either by collecting statistics on a representative workload or by identifying the most common predicate constructs with some domain knowledge.
- The default expression filter indexes created for the rule class can be dropped using the `DBMS_RLMGR.DROP_EXPFIL_INDEXES` procedure. Once the indexes are dropped, they can be recreated using the `DBMS_RLMGR.CREATE_EXPFIL_INDEXES` procedure. When the `coll_stats` argument of the `CREATE_EXPFIL_INDEXES` procedure is set to `YES`, rule condition statistics are collected for the most common predicate constructs and the indexes are created using these statistics. Alternately, a domain expert can manually set the index parameters by identifying the most common and discriminating predicate constructs and then create the indexes with these parameters. Note that the index parameters can be set for each of the primitive event structures associated with the rule class. The index parameters can be assigned to the event structure (which is also the Expression Filter attribute set) using the `DBMS_EXPFIL.DEFAULT_INDEX_PARAMETERS` procedure. When the `coll_stats` argument of the `CREATE_EXPFIL_INDEXES` procedure is set to `NO`, the expression filter indexes created for the rule class make use of the default index parameters associated with each primitive event structure. (See the chapter on indexing expressions in [Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_indexexpressions.htm#EXPRN018) for additional information on tuning the Expression Filter indexes for better performance).
- Related view: [`USER_EXPFIL_DEF_INDEX_PARAMS`](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/exprn_views.htm#EXPRN057)

Examples

The following commands collect the statistics for the rules defined in the `CompTravelPromo` rule class and create the expression filter indexes that are based on the most common predicates in the set.

```
BEGIN
DBMS_RLMGR.CREATE_EXPFIL_INDEXES (rule_class => 'CompTravelPromo',
                                  coll_stats => 'yes');
END;
/
```

This is an Expression Filter tuning example where the domain knowledge is used to assign specific index parameters. The following commands associate specific index parameters to the `AddFlight` event structure such that the expression filter index created for corresponding expressions are optimized accordingly. The subsequent `CREATE_EXPFIL_INDEXES` step makes use of these index parameters.

```
BEGIN
  DBMS_EXPFIL.DEFAULT_INDEX_PARAMETERS('AddFlight',
    exf$attribute_list (
       exf$attribute (attr_name => 'Airline',
                      attr_oper => exf$indexoper('='),
                      attr_indexed => 'TRUE'),
       exf$attribute (attr_name => 'ToCity',
                      attr_oper => exf$indexoper('='),
                      attr_indexed => 'TRUE'),
       exf$attribute (attr_name => 'Depart',
                      attr_oper => exf$indexoper('=','<','>','>=','<='),
                      attr_indexed => 'FALSE') 
    )
  );
  -- create the indexes after assigning the index parameters --
  DBMS_RLMGR.CREATE_EXPFIL_INDEXES (rule_class => 'CompTravelPromo'); 
END; 
/
```

---

### CREATE\_INTERFACE Procedure

This procedure creates a rule class interface package that can be used to directly operate on the rule class for efficiency and ease of use.

Syntax

```
DBMS_RLMGR.CREATE_INTERFACE  (
   rule_class   IN  VARCHAR2,
   interface_nm IN  VARCHAR2);
```

Parameters

Table 124-12 CREATE\_INTERFACE Procedure Parameter

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class for which the interface package is created |
| `interface_nm` | Name of the PL/SQL package that acts as the interface to the rule application |

Usage Notes

- The common set of `DBMS_RLMGR` procedures used for runtime operations such as processing the rules for some events, consuming the events and resetting the session make use of the rule class name passed in as one of the arguments and associate them to the corresponding operations on the rule class. You can the overhead involved in this step by creating a rule class interface package that is used to directly operate on the rule class.
- The rule class interface package is a PL/SQL package that has procedures or functions to process rules (`PROCESS_RULES`), add event (`ADD_EVENT`), consume events (`CONSUME_EVENT`, `CONSUME_PRIM_EVENTS`) and reset rule session (`RESET_SESSION`). The operational characteristics of these procedures and functions are the same as those of `DBMS_RLMGR` procedures and functions with matching names with two exceptions. Since the rule class interface package is created for a specific rule class, the rule class name is implicit and it need not be passed in as an argument to the procedures and functions of the rule class interface package. Additionally, the rule class interface package has separate `PROCESS_RULES` and `ADD_EVENT` procedures to accept each primitive event type configured with the rule class. This is in contrast to the same procedures in the `DBMS_RLMGR` package, which are generalized to accept the event instances only as a `VARCHAR` or an `AnyData` instance.

Examples

The following commands create the rule class interface package for the `CompTravelPromo` rule class.

```
BEGIN
  DBMS_RLMGR.CREATE_INTERFACE  (rule_class   => 'CompTravelPromo',
                                interface_nm => 'TravelPromoRules'); 
END;
```

The following commands make use of the interface created in previous step to process the rules for an instance of `AddFlight` event.

```
BEGIN
  TravelPromoRules.process_rules (event_inst => 
            AddFlight(987, 'Abcair', 'Boston', 'Orlando',
                                    '01-APR-2009', '08-APR-2009'); 
END;
```

---

### CREATE\_RULE\_CLASS Procedure

This procedure creates a rule class.

Syntax

```
DBMS_RLMGR.CREATE_RULE_CLASS  (
   rule_class      IN  VARCHAR2,
   event_struct    IN  VARCHAR2,
   action_cbk      IN  VARCHAR2,
   actprf_spec     IN  VARCHAR2  default null,
   rslt_viewnm     IN  VARCHAR2  default null,
   rlcls_prop      IN  VARCHAR2  default <simple/>);
```

Parameters

Table 124-13 CREATE\_RULE\_CLASS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class to be created in the current schema |
| `event_struct` | Name of the object type or an Expression Filter attribute set in the current schema that represents the event structure for the rule class |
| `action_cbk` | Name of the action callback procedure to be created for the rule class |
| `actprf_spec` | Specification (name and SQL datatype pairs) for the action preferences associated with the rule class |
| `rlst_viewnm` | Name of rule class results view that lists the matching events and rules within a session. A view with this name is created in the current schema. |
| `rlcls_prop` | XML document for setting the rule class properties. By default, the rule class created is for simple events (non-composite). |

Usage Notes

- For successful creation of a rule class, you must have sufficient privileges to create views, object types, tables, packages, and procedures.
- This command creates the rule class and its dependent objects in the user's schema. For this operation to succeed the name specified for the event structure must refer to an existing object type or an Expression Filter attribute set in the user's schema. When an object type is used for an event structure, the `CREATE_RULE_CLASS` procedure implicitly creates an attribute set for the object type. In the case of a rule class configured for composite events, the previous procedure also creates attribute sets for the object types that are directly embedded in the event structure's object type (or the attribute set). A maximum of 32 embedded objects (and or or table aliases) can be specified with an event structure that is used for a composite rule class. The types of dependent objects created with this procedure and their structure depend on the properties of the rule class and its event structure. The minimum set of dependent objects created for a rule class is as follows:
	- Rule class table – A rule class table that shares the name of the rule class is created in the user's schema to store the rule definitions (rule identifiers, rule conditions, rule descriptions, and action preferences). This table implicitly has four columns, `rlm$ruleid`, `rlm$rulecond`, `rlm$enabled`, and `rlm$ruledesc` to store the rule identifiers, rule conditions, rule states, and rule descriptions respectively. In addition to these four columns, the rule class table has few columns according to the action preference specification for the rule class. For example, if a TravelPromotion rule class uses 'PromoType `VARCHAR` (20), OfferedBy `VARCHAR` (20)' as its action preference specification (assigned to `actpref_spec` argument), the rule class table is created with the following structure.
		```
		TABLE TravelPromotion (
		      rlm$ruleid VARCHAR(100),     -- rule identifier column --
		      PromoType VARCHAR(20),       -- action preference 1 --
		      OfferedBy VARCHAR(20),       -- action preference 2 --
		      rlm$rulecond VARCHAR(4000),  -- rule condition –-
		      rlm$ruledesc VARCHAR(1000),  -- rule description --
		      rlm$enabled CHAR(1));        -- rule status --
		```
		The rule class table structure varies from one rule class to another based on the exact list of action preference categories specified for the rule class.
		- Action Callback Procedure – You create the skeleton for the action callback procedure with the given name in the user's schema and it is associated with the rule class. During rule evaluation, the callback procedure is called for each matching rule and event. You must implement the body of the action callback procedure to perform the appropriate action for each rule. The exact action for a rule can be determined based on the event that matched the rule and rule definition along with its action preferences. This information is passed to the action callback procedure through its arguments. Hence, the argument list for the action callback procedure depends on the event structure associated with the rule class and the rule class itself.
		In the case of a rule class configured for simple events (`<simple/>` assigned to the properties of the rule class), the event that matches a rule is passed through a `rlm$event` argument that is declared to be of the same type as the event structure. Additionally, the rule definitions are passed to the action callback procedure using an `rlm$rule` argument that is declared as ROWTYPE of the corresponding rule class table. For example, the structure of the `PromoAction` action callback procedure created for a `TravelPromotion` rule class configured for a simple (non-composite) `AddFlight` event structure is as follows:
		```
		PROCEDURE PromoAction (rlm$event AddFlight,
		                       rlm$rule TravlePromotion%ROWTYPE);
		```
		In the case of a rule class created for composite events (`<composite/>` assigned to the properties of the rule class), the action callback procedure is created to pass each primitive event as a separate argument. For example, the `CompPromoAction` action callback procedure created for a rule class `CompTravelPromo` configured for a composite event with `AddFlight` and `AddRentalCar` primitive events are shown as follows:
		```
		-- composite event structure --
		TYPE TSCompEvent (Flt AddFlight,
		                  Car AddRentalCar);
		-- corresponding action callback procedure --
		PROCEDURE PromoAction (Flt AddFlight,
		                       Car AddRentalCar,
		                       rlm$rule CompTravelPromo%ROWTYPE)
		```
		The action callback procedure includes additional arguments when the rule class is configured for the `RULE` consumption policy or when the rule class is enabled for one or more collection events. The arguments in these cases include the identifiers for the events (`ROWID` data type) in addition to the event instances. You can use these event identifiers to further operate on the matched rules. For example, in the case of the rule class configured for rule consumption, the event identifiers are used to consume the events with `DBMS_RLMGR.CONSUME_PRIM_EVENTS` function. In the case of rule class enabled for collection events, the same identifiers for the collection events can be used to fetch specific aggregate values with the `DBMS_RLMGR.GET_AGGREGATE_VALUE` function.
		- Rule class results view – A view to display the results from matching some events with rules is created in the same schema as the rule class. By default, this view is created with a system-generated name. Optionally, the rule class creator can specify a name for this view with the `rlst_viewnm` argument of the `CREATE_RULE_CLASS` procedure. When the events are added to the rule manager within a rule session using the `ADD_EVENT` procedure, the list of matching events and rules are displayed in the rule class results view.
		The structure of the view defined for the rule class results depends on the event structure and the action preferences configured with the rule class. Minimally, the view has three columns to display the system generated event identifier (`rlm$evenetid`), the identifier of the rule it matches (`rlm$ruleid`), and the rule condition (rlm$rulecond). Additionally, it has columns to display the event information and the rule action preferences.
		In the case of a rule class configured for simple events, the event information is displayed as rlm$event that is declared to be of the event structure type. So, a `MatchingPromos` view created for the `TravelPromotion` rule class configured for a simple `AddFlight` event structure is as follows:
		```
		VIEW MatchingPromos (
		    rlm$eventid ROWID,
		    rlm$event AddFlight,
		    rlm$ruleid VARCHAR(100),
		    PromoType VARCHAR(30), -- action preference 1 --
		    OffredBy VARCHAR(30), -- action preference 2 --
		    rlm$rulecond VARCHAR(4000),
		    rlm$ruledesc VARCHAR(1000)
		);
		```
		In the case of a rule class configured for composite events, the primitive events matching a rule are displayed separately using corresponding columns. For the above `CompTravelPromo` rule class, a `MatchingCompPromos` view is created with the following structure.
		```
		VIEW MatchingCompPromos (
		    rlm$eventid ROWID,
		    Flt AddFlight,
		    Car AddRentalCar,
		    rlm$ruleid VARCHAR(100),
		    PromoType VARCHAR(30),   -- action preference 1 --
		    OffredBy VARCHAR(30),    -- action preference 2 --
		    rlm$rulecond VARCHAR(4000),
		    rlm$ruledesc VARCHAR(1000)
		);
		```
		The values from the rlm$eventid column are used to enforce rule class consumption policies when the corresponding rule is executed. See the CONSUME\_EVENT Function for more information.

Examples

The following commands create a rule class for simple events (of `AddFlight` type).

```
CREATE or REPLACE TYPE AddFlight AS OBJECT (
                  CustId NUMBER,
                  Airline VARCHAR(20),
                  FromCity VARCHAR(30),
                  ToCity VARCHAR(30),
                  Depart DATE,
                  Return DATE);
BEGIN
  DBMS_RLMGR.CREATE_RULE_CLASS (
              rule_class   => 'TravelPromotion', -- rule class name --
              event_struct => 'AddFlight', -- event struct name --
              action_cbk    => 'PromoAction', -- callback proc name –-
              rslt_viewnm   => 'MatchingPromos', -- results view --
              actprf_spec   => 'PromoType VARCHAR(20),
                              OfferedBy VARCHAR(20)');
END;
```

The following commands create a rule class for composite events consisting of two primitive events (`AddFlight` and `AddRentalCar`).

```
CREATE or REPLACE TYPE TSCompEvent (Flt AddFlight,
                                    Car AddRentalCar);
BEGIN
  DBMS_RLMGR.CREATE_RULE_CLASS (
              rule_class    => 'CompTravelPromo', -- rule class name --
              event_struct  => 'TSCompEvent', -- event struct name --
              action_cbk    => 'CompPromoAction', -- callback proc name –-
              rslt_viewnm   => 'MatchingCompPromos', -- results view --
              actprf_spec   => 'PromoType VARCHAR(20),
                              OfferedBy VARCHAR(20)',
              properties    => '<composite/>');
END;
```

---

### DELETE\_RULE Procedure

This procedure deletes a rule from a rule class.

Syntax

```
DBMS_RLMGR.DELETE_RULE (
   rule_class    IN    VARCHAR2,
   rule_id       IN    VARCHAR2);
```

Parameters

Table 124-14 DELETE\_RULE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class. A schema extended rule class name can be used to refer to a rule class that does not belong to the current schema. |
| `rule_id` | Identifier for the rule to be deleted |

Usage Notes

- Use this procedure to delete a rule from the rule class. The identifier for the rule to be deleted can be obtained by querying the rule class table (that shares the same name as the rule class). Alternately, the owner of the rule class can use a SQL `DELETE` statement on one rule class table to delete a rule.When you use the schema extended name for the rule class, you must have the `DELETE` `RULE` privilege on the rule class. See the GRANT\_PRIVILEGE Procedure for more information.
	Note:
	`AUTOCOMMIT` property of the rule class is ignored if the rules are deleted with the SQL `DELETE` statement instead of the `DELETE_RULE` procedure.
- See the CREATE\_RULE\_CLASS Procedure for the structure of the rule class table.

Examples

The following command deletes a rule from the rule class.

```
BEGIN
  DBMS_RLMGR.DELETE_RULE (
           rule_class  => 'CompTravelPromo',
           rule_id     => 'AB_AV_FL');
END;
```

Alternately, you can issue the following SQL `DELETE` statement to delete the above rule from the rule class.

```
DELETE FROM CompTravelPromo WHERE rlm$ruleid = 'AB_AV_FL';
```

---

### DROP\_CONDITIONS\_TABLE Procedure

This procedure drops the conditions table.

Syntax

```
DBMS_RLMGR.DROP_CONDITIONS_TABLE (
     cond_table IN   VARCHAR2);
```

Parameters

Table 124-15 DROP\_CONDITIONS\_TABLE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `cond_table` | Name of conditions table in the user schema |

Usage Notes

- This procedure drops the table that stores the shareable conditional expressions. If one of the conditional expressions in this table is used to form a rule condition in a rule class, the drop operation fails with an appropriate error.

Examples

The following command drops the conditions table:

```
BEGIN
  DBMS_RLMGR.DROP_CONDITIONS_TABLE (cond_table => 'FlightConditions');
END;
/
```

---

### DROP\_EVENT\_STRUCT Procedure

This procedure drops an event structure.

Syntax

```
DBMS_RLMGR.DROP_EVENT_STRUCT  (
   event_struct  IN  VARCHAR2);
```

Parameters

Table 124-16 DROP\_EVENT\_ STRUCT Procedure Parameter

| Parameter | Description |
| --- | --- |
| `event_struct` | Name of event structure in the current schema |

Usage Notes

- This procedure drops the event structure from the current schema. This drops all the dependent objects created to manage the event structure.

Examples

The following command drops the event structure.

```
BEGIN  DBMS_RLMGR.DROP_EVENT_STRUCT(event_struct => 'AddFlight');
END;
```

---

### DROP\_EXPFIL\_INDEXES Procedure

This procedure drops the expression filter indexes created for a rule class.

Syntax

```
DBMS_RLMGR.DROP_EXPFIL_INDEXES  (
   rule_class  IN  VARCHAR2);
```

Parameters

Table 124-17 DROP\_EXPFIL\_INDEXES Procedure Parameter

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class |

Usage Notes

This procedure drops all the expression filter indexes associated with a rule class. You can recreate the indexes using the `DBMS_RLMGR.CREATE_EXPFIL_INDEXES` call.

Examples

The following command drops the expression filter indexes created for the `CompTravelPromo` rule class.

```
BEGIN
DBMS_RLMGR.DROP_EXPFIL_INDEXES (rule_class => 'CompTravelPromo');
END;
/
```

---

### DROP\_INTERFACE Procedure

This procedure drops the rule class interface package created for a rules application.

Syntax

```
DBMS_RLMGR.DROP_INTERFACE  (
   interface_nm  IN  VARCHAR2);
```

Parameters

Table 124-18 DROP\_INTERFACE Procedure Parameter

| Parameter | Description |
| --- | --- |
| `interface_nm` | Name of the PL/SQL package that acts as the interface to the rule application |

Usage Notes

This procedure drops the rule class interface package created with the `DBMS_RLMGR.CREATE_INTERFACE` call.

Examples

The following command drops the rule class interface package `TravelPromoRules`.

```
BEGIN
  DBMS_RLMGR.DROP_INTERFACE (interface_nm => 'TravelPromoRules' 
END;
```

---

### DROP\_RULE\_CLASS Procedure

This procedure drops a rule class.

Syntax

```
DBMS_RLMGR.DROP_RULE_CLASS  (
   rule_class  IN  VARCHAR2);
```

Parameters

Table 124-19 DROP\_RULE\_CLASS Procedure Parameter

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of rule class in the current schema |

Usage Notes

- This procedure drops the rule class from the current schema. This drops all the dependent objects created to manage the rule class. Because an event structure in a user's schema can be shared across multiple rule classes, the event structure is not dropped with this command. You must use the `DROP_EVENT_STRUCTURE` procedure for the composite event as well as the individual primitive events to cleanup unused event structures.

Examples

The following command drops the rule class.

```
BEGIN  DBMS_RLMGR.DROP_RULE_CLASS(rule_class => 'CompTravelPromo');
END;
```

---

### EXTEND\_EVENT\_STRUCT Procedure

This is used to extend the primitive event structure used by one or more rule classes by adding a new attribute.

Syntax

```
DBMS_RLMGR.EXTEND_EVENT_STRUCT (
          event_struct    IN   VARCHAR2, 
          attr_name       IN   VARCHAR2, 
          attr_type       IN   VARCHAR2, 
          attr_defvl      IN   VARCHAR2 default NULL);
```

Parameters

Table 124-20 EXTEND\_EVENT\_ STRUCT Procedure Parameter

| Parameter | Description |
| --- | --- |
| `event_struct` | Name of the event structure to which this attribute is added |
| `attr_name` | Name of the elementary attribute to be added. No two attributes in a set can have the same name. |
| `attr_type` | Data type of the attribute. This argument accepts any standard SQL data type or the name of an object type that is accessible to the current user. |
| `attr_defvl` | Default value for the elementary attribute |

Usage Notes

- This procedure extends a primitive event structure already associated with a rule class to include a new attribute. You can use this procedure mostly to migrate a fully developed rules application to use extended event structures and you should not use it in the place of the `ADD_ELEMENTARY_ATTRIBUTE` call. Unlike the `ADD_ELEMENTARY_ATTRIBUTE` call, which builds an event structure one attribute at a time, the `EXTEND_EVENT_STRUCT` call evolves the object type associated with the event structure to include the new attributes and performs some maintenance operations on the dependent objects.
- The usage of the `EXTEND_EVENT_STRUCT` call is similar to that of the `ADD_ELEMENTARY_ATTRIBUTE` call with the same set of arguments. Table alias attributes and attributes of text and spatial data types cannot be added to the event structure using the `EXTEND_EVENT_STRUCT` call.

Examples

The following commands add an attribute to the `AddRentalCar` event structure that is used by the `CompTravelPromo` rule class.

```
BEGIN 
  DBMS_RLMGR.EXTEND_EVENT_STRUCT (
        event_struct   => 'AddRentalCar',  
        attr_name      => 'PrefMemberId',
        attr_type      => 'VARCHAR2(30)'); 
END;
```

---

### GET\_AGGREGATE\_VALUE Function

This function retrieves the aggregate value computed for a collection event.

Syntax

```
DBMS_RLMGR.GRANT_PRIVILEGE  (
   rule_class      IN  VARCHAR2,
   event_ident     IN  VARCHAR2,
   aggr_func       IN  VARCHAR2) RETURN VARCHAR2;
```

Parameters

Table 124-21 GET\_AGGREGATE\_VALUE Function Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class for the collection event |
| `event_ident` | System-generated identifier for the collection event |
| `aggr_func` | Signature for the aggregate value to be retrieved |

Usage Notes

- When a rule condition with `collection` construct matches a set of events, an instance representing the collection event and a system-generated identifier for the collection event are passed into the action callback procedure. This event identifier can be used to fetch any aggregate values that are computed as part of the collection event evaluation.
- Within a collection construct in a rule condition, the aggregate functions can be included in the `HAVING` clause or in the `COMPUTE` clause. For example, the following rule condition computes three aggregate values for `sum(amount)`, `count(*)`, and `max(amount)`. At the time of action execution, these values can be obtained using the identifier for the collection event that represents all the instances of `BankTransaction` with the same `subjectId` (the attribute on which the events are grouped).
	```
	<condition>
	   <collection name="bank" groupby="subjectId"
	               having="sum(amount) > 10000"
	               compute="max(amount), count(*)"/>
	</condition>
	```
- The signature for the aggregate function is bound to the `aggr_func` argument of the `GET_AGGREGATE_VALUE` function to fetch the specific aggregate value. If the value is a `NUMBER` or a `DATE` data type, it returns the equivalent `VARCHAR` representation. It returns a `NULL` value if an attempt was made to fetch an aggregate value that is never computed as part of the collection event.

Examples

The following example shows a sample implementation of the action callback procedure that prints the computed aggregate values as part of action execution. In this particular case, the `BankTransaction` primitive event is enabled for collections.

```
CREATE OR REPLACE PROCEDURE LAWENFORCEMENTCBK (
   bank                 banktransaction,
   bankcollid           rowid,
   transport            transportation,
   fldrpt               fieldreport,
   rlm$rule             LawEnforcementRC%ROWTYPE) IS
   aggrval              VARCHAR(30); 
begin
  dbms_ouput.put_line('Mathing Rule :'||rlm$rule.rlm$ruleid||chr(10)); 
  
  if (bank is not null) then
   dbms_ouput.put_line('-->Bank Transactions by ('||bank.subjectId||')'||chr(10);

   aggrval := dbms_rlmgr.get_aggregate_value(rule_class  =>'LawEnforcementRC',
                                             event_ident => bankcollid,
                                             aggr_func   => 'sum(amount)');
   if (aggrval is not null) then
     dbms_ouput.put_line('---> Sum of the amounts is :'||aggrval||chr(10));
   end if;
   . . .
  end if; 
end;
```

---

### GRANT\_PRIVILEGE Procedure

This procedure grants privileges on a rule class to another user.

Syntax

```
DBMS_RLMGR.GRANT_PRIVILEGE  (
   rule_class      IN  VARCHAR2,
   priv_type       IN  VARCHAR2,
   to_user         IN  VARCHAR2);
```

Parameters

Table 124-22 GRANT\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class in the current schema |
| `priv_type` | Type of rule class privilege to be granted |
| `to_user` | User to whom the privilege is to be granted |

Usage Notes

- This procedure grants appropriate privileges to a user who is not the owner of the rule class. The types of privileges that can be granted to a user are:
	- `PROCESS` `RULES`: A user with `PROCESS` `RULES` privilege on a rule class can process the rules in the rule class using the `PROCESS_RULES` procedure or the `ADD_EVENT` procedure. Also, the user with this privilege can select from the corresponding rule class results view.
		- `ADD` `RULE`: A user with `ADD` `RULE` privilege on a rule class can add rules to a rule class. Alternatively, the owner of the rule class can grant the `INSERT` privilege on one rule class table to other users.
		- `DELETE` RULE: A user with `DELETE` `RULE` privilege on a rule class can delete rules from a rule class. Alternatively, the owner of the rule class can grant the `DELETE` privilege on one rule class table to other users.
		- `ALL`: Granting the `ALL` privilege on a rule class is equivalent to granting all the above privileges on the rule class to the user.
- The owner of the rule class always has privileges to drop a rule class, process rules in a rule class, add rules and delete rules from a rules class. Only the owner of the rule class can drop a rule class and this privilege cannot be granted to another user.
- You must have the `EXECUTE` privilege on the primitive event types associated with a rule class before you make use of the corresponding rule class results view.

Examples

The following command grants `PROCESS` `RULES` privilege on TravelPromo rule class to the user `SCOTT`.

```
BEGIN
  DBMS_RLMGR.GRANT_PRIVILEGE(rule_class => 'TravelPromo',
                             priv_type => 'PROCESS RULES',
                             to_user => 'SCOTT');
END;
```

---

### PROCESS\_RULES Procedure

This procedure processes the rules for a given event. The procedure is overloaded. The different functionality of each form of syntax is presented along with the definitions.

Syntax

Processes the rules for a string representation of the event instance being added to the rule class:

```
DBMS_RLMGR.PROCESS_RULES  (
   rule_class    IN  VARCHAR2,
   event_inst    IN  VARCHAR2,
   event_type    IN  VARCHAR2 default null);
```

Processes the rules for an AnyData representation of the event instance being added to the rule class:

```
DBMS_RLMGR.PROCESS_RULES  (
   rule_class    IN  VARCHAR2,
   event_inst    IN  sys.AnyData);
```

Parameters

Table 124-23 PROCESS\_RULES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class. A schema extended rule class name can be used to refer to a rule class that does not belong to the current schema. |
| `event_inst` | String or AnyData representation of the event instance being added to the rule class |
| `event_type` | Type of event instance assigned to the `event_inst` argument when the string representation of the event instance is used for a rule class configured for composite events |

Usage Notes

- This procedure is used to process the rules in a rule class for an event instance assigned to the `event_inst` argument.
- In the case of a rule class configured for simple events (non-composite), the event instance is an instantiation of the corresponding event structure. The rules are evaluated (conclusively) for this event and the corresponding action callback procedure is called for each matching rule. If the event does not match any rule, no further action is performed. If the event matches two or more rules, the ordering clause configured for the rule class is used to order them accordingly to invoke the action callback procedure. If the rule class is configured for `EXCLUSIVE` consumption policy, once the first rule in this order is executed (and the corresponding action callback procedure is called), the rest of the rules that matched the event are ignored.
- In the case of a rule class configured for composite events, the event instance assigned to the `event_inst` argument is an instantiation of one of the primitive type within the composite event. When the instance is represented as a string, the corresponding type name should be assigned to the `event_type` argument. The `PROCESS_RULES` call on a rule class configured for composite events performs various actions depending on the state of the rule class and the kind of rules in the rule class. Note the following.
	- The rules operating only on the primitive event passed in are evaluated conclusively and the action callback procedure is called for the matching rules, as described in previous paragraph.
		- In the case of a rule operating on more than one primitive event, the event instance passed through `PROCESS_RULES` procedure could match only a part of the rule.
		- If there are other primitive event instances that matches the rest of the rule, the current event instance is combined with the other instances to form a complete composite event that matches a rule in the rule class. So, the event instance assigned to the `event_inst` argument of the `PROCESS_RULES` procedure could be combined with various other primitive events (previously processed) to evaluate one or more rules conclusively. The action callback procedure for the rule class is called for each such combination of primitive events (composite event) and the rule. The ordering clause for the rule class and the consumption policy for the primitive events in taken into account while invoking the action callback procedure.
				- If there is no other primitive event that matches the rest of the rule, the current event instance and its (incremental) evaluation results are recorded in the database. These results are preserved until either the event is consumed or deleted from the system owing to the duration policy used for the rule class.

Examples

The following command processes the rules in the `TravelPromotion` rule class for the given events.

```
BEGIN
  DBMS_RLMGR.PROCESS_RULES (
               rule_class => 'TravelPromotion',
               event_inst =>
                 AddFlight.getVarchar(987, 'Abcair', 'Boston', 'Orlando',
                                      '01-APR-2003', '08-APR-2003'));
END;
```

The following commands process the rules in the `CompTravelPromo` rule class for the two primitive events shown.

```
BEGIN
  DBMS_RLMGR.PROCESS_RULES(
               rule_class => 'CompTravelPromo',
               event_inst =>
                 AddFlight.getVarchar(987, 'Abcair', 'Boston', 'Orlando',
                                      '01-APR-2003', '08-APR-2003'),
               event_type => 'AddFlight');
  DBMS_RLMGR.PROCESS_RULES(
               rule_class => 'Scott.CompTravelPromo',
               event_inst =>
                  AnyData.convertObject(AddRentalCar(987, 'Luxury', '03-APR-2003',
                                        '08-APR-2003', NULL)));
END;
```

---

### PURGE\_EVENTS Procedure

This procedure resets the incremental state maintained by the rule class by removing all the events associated with the rule class and purging any state information pertaining to rules matching some events.

Syntax

```
DBMS_RLMGR.PURGE_EVENTS (
     rule_class IN   VARCHAR2);
```

Parameters

Table 124-24 PURGE\_EVENTS Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of rule class in the current schema |

Usage Notes

- Use this procedure while developing rules applications using Rules Manager. You can test the rules defined in the rule class with hypothetical events and then remove all these events by issuing this procedure call. This call cleans up all the events in the events repository and purges any partial state information associated with the matching rules.

Examples

The following command removes the events associated with the `CompTravelPromo` rule class:

```
BEGIN
  DBMS_RLMGR.PURGE_EVENTS (rule_class => 'CompTravelPromo');
END;
/
```

---

### RESET\_SESSION Procedure

This procedure starts a new session and thus discards the results in the rule class results view.

Syntax

```
DBMS_RLMGR.RESET_SESSION  (
   rule_class  IN  VARCHAR2);
```

Parameters

Table 124-25 RESET\_SESSION Procedure Parameter

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of rule class. A schema extended rule class name can be used to refer to a rule class that does not belong to the current schema. |

Usage Notes

- When you use the `ADD_EVENT` procedure to add events to the rule class, the results from matching rules with events are recorded in the rule class results view. By default, these results are reset at the end of the database session. Alternately, you can use the RESET\_SESSION Procedure to reset and start a new rule session within a database session.This procedure is only applicable while using ADD\_EVENT Procedure to evaluate the rules.

Examples

The following command resets a rule class session.

```
BEGIN  DBMS_RLMGR.RESET_SESSION(
             rule_class => 'CompTravelPromo');
END;
```

---

### REVOKE\_PRIVILEGE Procedure

This procedure revokes privileges on a rule class from another user.

Syntax

```
DBMS_RLMGR.REVOKE_PRIVILEGE  (
   rule_class      IN  VARCHAR2,
   priv_type       IN  VARCHAR2,
   from_user       IN  VARCHAR2);
```

Parameters

Table 124-26 REVOKE\_PRIVILEGE Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class in the current schema |
| `priv_type` | Type of rule class privilege to be revoked |
| `from_user` | User from whom the privilege is to be revoked |

Usage Notes

- This procedure revokes appropriate privileges from a user. The types of privileges that can be revoked are the same as the types listed in the description of the GRANT\_PRIVILEGE Procedure. Rule class privileges cannot be revoked from the owner of the rule class.

Examples

The following command revokes `PROCESS` `RULES` privilege on `TravelPromo` rule class from the user `SCOTT`.

```
BEGIN
  DBMS_RLMGR.REVOKE_PRIVILEGE(rule_class  => 'TravelPromo',
                              priv_type   => 'PROCESS RULES',
                              from_user   => 'SCOTT');
END;
```

---

### SYNC\_TEXT\_INDEXES Procedure

This procedure synchronizes the indexes defined to process the predicates involving the `CONTAINS` operator in rule conditions.

Syntax

```
DBMS_RLMGR.SYNC_TEXT_INDEXES (
     rule_class IN   VARCHAR2);
```

Parameters

Table 124-27 SYNC\_TEXT\_INDEXES Procedure Parameters

| Parameter | Description |
| --- | --- |
| `rule_class` | Name of the rule class in the current schema |

Usage Notes

- When a rule class is configured for events with one or more text attributes, the text predicates in the corresponding rule conditions are processed using `CTXRULE` indexes. Unlike other types of indexes (bitmap for scalar and XML predicates or spatial for spatial predicates) used to process other types of predicates in the rule conditions, the `CTXRULE` indexes are not transactional in nature. That is, if the text predicates in a rule condition are modified in a database transaction, the new predicates are not automatically reflected in the corresponding `CTXRULE` index. This could result in inconsistent results while matching events with the rule conditions. All the `CTXRULE` indexes associated with a rule class can be synchronized with the latest rule conditions using this procedure.
	You must have `EXECUTE` privilege on the `CTX_DDL` package for successful synchronization of the text indexes.

Examples

The following command synchronizes any text indexes associated `CompTravelPromo` rule class:

```
BEGIN
  DBMS_RLMGR.SYNC_TEXT_INDEXES (rule_class => 'CompTravelPromo');
END;
/
```