---
title: Database PL/SQL Language Reference
book: Database PL/SQL Language Reference
doc_id: E96448-09
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/updating-rows-records.html
tags:
  - oracle
  - 19c
  - pl-sql-language-reference
---

## Updating Rows with Records

The PL/SQL extension to the SQL `UPDATE` statement lets you update one or more table rows with a record.

The record must represent a row of the table. For more information, see " [UPDATE Statement Extensions](UPDATE-statement-extensions.md) ".

For restrictions on updating table rows with a record, see " [Restrictions on Record Inserts and Updates](restrictions-record-inserts-and-updates.md) ".

To efficiently update a set of rows with a collection of records, put the `UPDATE` statement inside a `FORALL` statement. For information about the `FORALL` statement, see " [FORALL Statement](bulk-sql-and-bulk-binding.md) ".

Example 5-55 Updating Rows with Record

This example updates the first three weeks of the table `schedule` (defined in [Example 5-54](inserting-records-tables.md)) by putting the new values in a record and updating the first three rows of the table with that record.

```
DECLARE
  default_week  schedule%ROWTYPE;
BEGIN
  default_week.Mon := 'Day Off';
  default_week.Tue := '0900-1800';
  default_week.Wed := '0900-1800';
  default_week.Thu := '0900-1800';
  default_week.Fri := '0900-1800';
  default_week.Sat := '0900-1800';
  default_week.Sun := 'Day Off';
 
  FOR i IN 1..3 LOOP
    default_week.week    := i;
  
    UPDATE schedule
    SET ROW = default_week
    WHERE week = i;
  END LOOP;
END;
/
 
SELECT * FROM schedule;
```

Result:

```
WEEK MON       TUE       WED       THU       FRI       SAT       SUN
---- --------- --------- --------- --------- --------- --------- ---------
   1 Day Off   0900-1800 0900-1800 0900-1800 0900-1800 0900-1800 Day Off
   2 Day Off   0900-1800 0900-1800 0900-1800 0900-1800 0900-1800 Day Off
   3 Day Off   0900-1800 0900-1800 0900-1800 0900-1800 0900-1800 Day Off
   4 0800-1700 0800-1700 0800-1700 0800-1700 0800-1700 Day Off   Day Off
   5 0800-1700 0800-1700 0800-1700 0800-1700 0800-1700 Day Off   Day Off
   6 0800-1700 0800-1700 0800-1700 0800-1700 0800-1700 Day Off   Day Off
```