---
title: Rules Manager Types
book: PL/SQL Packages and Types Reference
doc_id: E40758-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/t_rlmobj.htm
tags:
  - oracle
  - 11g
  - pl-sql-packages-and-types-reference
---

## 258 Rules Manager Types

Note:

This functionality is deprecated with Oracle Database Release 11.2 and obsoleted with Release 12.1. For details regarding obsolescence, seeMy Oracle Support Note [ID 1244535.1](https://support.oracle.com/CSP/ui/flash.html#tab=KBHome%28page=KBHome&id=%28%29%29,%28page=KBNavigator&id=%28from=BOOKMARK&bmDocType=DESUPPORT&bmDocID=1244535.1&bmDocDsrc=KB&viewingMode=1143&bmDocTitle=Obsolescence%20Notice:%20Rules%20Manager%20Feature%20of%20Oracle%20Database%29%29)

Rules Manager contains one predefined type and a public synonym for this type.

See Also:

[Oracle Database Rules Manager and Expression Filter Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e14919/toc.htm) for more information.

This chapter contains the following topics:

- Using Rules Manager Types
- Summary of Rule Manager Types

---

## Using Rules Manager Types

This section contains topics that relate to using the Rules Manager Types.

- Security Model

---

### Security Model

The Oracle Database installation runs the `catrul.sql` script to load the `DBMS_RLMGR` package and create the required Rules Manager schema objects in the `EXFSYS` schema.

---

## Summary of Rule Manager Types

Table 258-1 describes the Rules Manager object type.

Table 258-1 Rules Manager Object Types

| Object Type Name | Description |
| --- | --- |
| RLM$EVENTIDS Object Type | Specifies a list of event identifiers to the `CONSUME_PRIM_EVENTS` procedure |

---

### RLM$EVENTIDS Object Type

The `RLM$EVENTIDS` defines a table of `VARCHAR2` values.

Syntax

```
CREATE OR REPLACE TYPE RLM$EVENTIDS is table of VARCHAR2(38);
```

Attributes

None.

Usage Notes

- `RLM$EVENTIDS` type passes a list of event identifiers to the `CONSUME_PRIM_EVENTS` procedure. These event identifiers are `ROWID` s for the corresponding events in the database and their values are available through the arguments of the action callback procedure and rule class results view columns, when the rule class is configured for `RULE` consumption policy

Examples

The following commands show the body of the action callback procedure for a rule class configured for `RULE` consumption policy. This demonstrates the use of `RLM$EVENTDIDS` type to consume the events before executing the action for the matched rules.

```
CREATE OR REPLACE PROCEDURE PromoAction (
      Flt        AddFlight, 
      Flt_EvtId  ROWID,    --- rowid for the fligt primitive event
      Car        AddRentalCar, 
      Car_EvtId  ROWID, 
      rlm$rule   TravelPromotions%ROWTYPE) is 
 evtcnsmd   NUMBER; 
BEGIN
 evtcnsmd := dbms_rlmgr.consume_prim_events(
              rule_class   => 'TravelPromotions',
              event_idents => RLM$EVENTIDS(Flt_EvtId, Car_EvtId));

 IF (evtcnsmd = 1) THEN 
   -- consume operation was successful; perform the action ---
   OfferPromotion (Flt.CustId, rlm$rule.PromoType, rlm$rule.OfferedBy);
 END IF;
END;
/
```