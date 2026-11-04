---
title: PL/SQL Packages and Types Reference
book: Database PL/SQL Packages and Types Reference
doc_id: F31492-25
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_SCHEDULER.html
tags:
  - oracle
  - 21c
  - pl-sql-packages-and-types-reference
---

## 157 DBMS\_SCHEDULER

The `DBMS_SCHEDULER` package provides a collection of scheduling functions and procedures that can be called from any PL/SQL program.

This chapter contains the following topics:

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN034) for more information regarding how to use `DBMS_SCHEDULER`

### 157.1 DBMS\_SCHEDULER Deprecated Subprograms

Oracle recommends that you do not use deprecated subprograms in new applications. Support for deprecated features is for backward compatibility only

The following subprograms are deprecated with Oracle Database 12c Release 1 (12.1):

- CREATE\_CREDENTIAL Procedure
- DROP\_CREDENTIAL Procedure

### 157.2 DBMS\_SCHEDULER Security Model

The `DBMS_SCHEDULER` package ignores privileges granted on scheduler objects, such as jobs or chains, through roles. Object privileges must be granted directly to the user.

### 157.3 DBMS\_SCHEDULER Rules and Limits

These rules apply when using the `DBMS_SCHEDULER` package.

- Only `SYS` can perform actions on objects in the `SYS` schema.
- Several of the procedures accept comma-delimited lists of object names. If you provide a list of names, then the Scheduler stops executing the list at the first object that returns an error. Therefore, the Scheduler does not perform the tasks needed for the remaining objects on the list.
	For example, consider the statement `DBMS_SCHEDULER.STOP_JOB ('job1, job2, job3, sys.jobclass1, sys.jobclass2, sys.jobclass3');`
	If `job3` cannot be stopped, then the jobs that follow it, `jobclass1`, `jobclass2`, and `jobclass3` cannot be stopped. The jobs that preceded `job3`, `job1` and `job2`, are stopped.
- Performing an action on an object that does not exist returns a PL/SQL exception stating that the object does not exist.

### 157.4 DBMS\_SCHEDULER Operational Notes

The Scheduler uses a rich calendaring syntax to enable you to define repeating schedules, such as "every Tuesday and Friday at 4:00 p.m." or "the second Wednesday of every month." This calendaring syntax is used in calendaring expressions in the `repeat_interval` argument of a number of package subprograms. Evaluating a calendaring expression results in a set of discrete timestamps.

See [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/arpls&id=ADMIN10040) for examples of the calendaring syntax.

Calendaring Syntax

This section starts with the calendaring syntax. It is followed by descriptions of various parts of the syntax.

In the calendaring syntax, \* means 0 or more.

```
repeat_interval = regular_schedule | combined_schedule
 
regular_schedule = frequency_clause
[";" interval_clause] [";" bymonth_clause] [";" byweekno_clause]
[";" byyearday_clause] [";" bydate_clause] [";" bymonthday_clause]
[";" byday_clause] [";" byhour_clause] [";" byminute_clause]
[";" bysecond_clause] [";" bysetpos_clause] [";" include_clause]
[";" exclude_clause] [";" intersect_clause][";" periods_clause]
[";" byperiod_clause]
```
```
frequency_clause = "FREQ" "=" ( predefined_frequency | user_defined_frequency )
predefined_frequency = "YEARLY" | "MONTHLY" | "WEEKLY" | "DAILY" | 
   "HOURLY" | "MINUTELY" | "SECONDLY"
user_defined_frequency = named_schedule

interval_clause = "INTERVAL" "=" intervalnum
   intervalnum = 1 through 99
bymonth_clause = "BYMONTH" "=" monthlist
   monthlist = month ( "," month)*
   month = numeric_month | char_month
   numeric_month = 1 | 2 | 3 ...  12
   char_month = "JAN" | "FEB" | "MAR" | "APR" | "MAY" | "JUN" |
   "JUL" | "AUG" | "SEP" | "OCT" | "NOV" | "DEC"
byweekno_clause = "BYWEEKNO" "=" weeknumber_list
   weeknumber_list = weeknumber ( "," weeknumber)*
   weeknumber = [minus] weekno
   weekno = 1 through 53
byyearday_clause = "BYYEARDAY" "=" yearday_list
   yearday_list = yearday ( "," yearday)*
   yearday = [minus] yeardaynum
   yeardaynum = 1 through 366
bydate_clause = "BYDATE" "=" date_list
   date_list = date ( "," date)*
   date = [YYYY]MMDD [ offset | span ]
bymonthday_clause = "BYMONTHDAY" "=" monthday_list
   monthday_list = monthday ( "," monthday)*
   monthday = [minus] monthdaynum
   monthdaynum = 1 through 31
byday_clause = "BYDAY" "=" byday_list
   byday_list = byday ( "," byday)*
   byday = [weekdaynum] day
   weekdaynum = [minus] daynum
   daynum = 1 through 53 /* if frequency is yearly */
   daynum = 1 through 5  /* if frequency is monthly */
   day = "MON" | "TUE" | "WED" | "THU" | "FRI" | "SAT" | "SUN"
BYTIME clause:  BYTIME=[hour_minute_second_list|minute_second_list]
   hour_minute_second_list: hh24mmss, .., hh24mmss
   minute_second_list: mmss, .. mmss
byhour_clause = "BYHOUR" "=" hour_list
   hour_list = hour ( "," hour)*
   hour = 0 through 23
byminute_clause = "BYMINUTE" "=" minute_list
   minute_list = minute ( "," minute)*
   minute = 0 through 59
bysecond_clause = "BYSECOND" "=" second_list
   second_list = second ( "," second)*
   second = 0 through 59
bysetpos_clause = "BYSETPOS" "=" setpos_list
   setpos_list = setpos ("," setpos)*
   setpos = [minus] setpos_num
   setpos_num = 1 through 9999

include_clause = "INCLUDE" "=" schedule_list
exclude_clause = "EXCLUDE" "=" schedule_list
intersect_clause = "INTERSECT" "=" schedule_list
schedule_list = schedule_clause ("," schedule_clause)*
schedule_clause = named_schedule [ offset ]
named_schedule = [schema "."] schedule
periods_clause = "PERIODS" "=" periodnum
byperiod_clause = "BYPERIOD" "=" period_list
period_list = periodnum ("," periodnum)*
periodnum = 1 through 100

offset = ("+" | "-") ["OFFSET:"] duration_val
span = ("+" | "-" | "^") "SPAN:" duration_val
duration_val = dur-weeks | dur_days
dur_weeks = numofweeks "W"
dur_days = numofdays "D"
numofweeks = 1 through 53
numofdays = 1 through 376
minus = "-"

combined_schedule = schedule_list
```

Table 157-1 Values for repeat\_interval

| Name | Description |
| --- | --- |
| `FREQ` | This specifies the type of recurrence. It must be specified. The possible predefined frequency values are YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, and SECONDLY. Alternatively, specifies an existing schedule to use as a user-defined frequency. |
| `INTERVAL` | This specifies a positive integer representing how often the recurrence repeats. The default is 1, which means every second for secondly, every day for daily, and so on. The maximum value is 99. |
| `BYMONTH` | This specifies which month or months you want the job to execute in. You can use numbers such as 1 for January and 3 for March, as well as three-letter abbreviations such as FEB for February and JUL for July. |
| `BYWEEKNO` | This specifies the week of the year as a number. It follows ISO-8601, which defines the week as starting with Monday and ending with Sunday; and the first week of a year as the first week, which is mostly within the Gregorian year. The first week is equivalent to the following two variants: the week that contains the first Thursday of the Gregorian year; and the week containing January 4th.  The ISO-8601 week numbers are integers from 1 to 52 or 53; parts of week 1 may be in the previous calendar year; parts of week 52 may be in the following calendar year; and if a year has a week 53, parts of it must be in the following calendar year.  As an example, in the year 1998, the ISO week 1 began on Monday December 29th, 1997; and the last ISO week (week 53) ended on Sunday January 3rd, 1999. So December 29th, 1997, is in the ISO week 1998-01, and January 1st, 1999, is in the ISO week 1998-53.  `byweekno` is only valid for YEARLY.  Examples of invalid specifications are `"FREQ=YEARLY; BYWEEKNO=1; BYMONTH=12"` and `"FREQ=YEARLY;BYWEEKNO=53;BYMONTH=1"`. |
| `BYYEARDAY` | This specifies the day of the year as a number. Valid values are 1 to 366. An example is 69, which is March 10 (31 for January, 28 for February, and 10 for March). 69 evaluates to March 10 for non-leap years and March 9 in leap years. -2 will always evaluate to December 30th independent of whether it is a leap year. |
| `BYDATE` | This specifies a list of dates, where each date is of the form `[YYYY]MMDD`. A list of consecutive dates can be generated by using the `SPAN` modifier, and a date can be adjusted with the `OFFSET` modifier. An example of a simple `BYDATE` clause follows:  `BYDATE=0115,0315,0615,0915,1215,20060115`  The following `SPAN` example is equivalent to `BYDATE=0110,0111,0112,0113,0114`, which is a span of 5 days starting at 1/10:  `BYDATE=0110+SPAN:5D`  The plus sign in front of the `SPAN` keyword indicates a span starting at the supplied date. The minus sign indicates a span ending at the supplied date, and the "^" sign indicates a span of `n` days or weeks centered around the supplied date. If `n` is an even number, it is adjusted up to the next odd number.  Offsets adjust the supplied date by adding or subtracting `n` days or weeks. `BYDATE=0205-OFFSET:2W` is equivalent to `BYDATE=0205-14D` (the `OFFSET:` keyword is optional), which is also equivalent to `BYDATE=0122`. |
| `BYMONTHDAY` | This specifies the day of the month as a number. Valid values are 1 to 31. An example is 10, which means the 10th day of the selected month. You can use the minus sign (-) to count backward from the last day, so, for example, `BYMONTHDAY=-1` means the last day of the month and `BYMONTHDAY=-2` means the next to last day of the month. |
| `BYDAY` | This specifies the day of the week from Monday to Sunday in the form MON, TUE, and so on. Using numbers, you can specify the 26th Friday of the year, if using a YEARLY frequency, or the 4th THU of the month, using a MONTHLY frequency. Using the minus sign, you can say the second to last Friday of the month. For example, `-1 FRI` is the last Friday of the month. |
| `BYHOUR` | This specifies the hour on which the job is to run. Valid values are 0 to 23. As an example, 10 means 10 a.m. |
| `BYMINUTE` | This specifies the minute on which the job is to run. Valid values are 0 to 59. As an example, 45 means 45 minutes past the chosen hour. |
| `BYSECOND` | This specifies the second on which the job is to run. Valid values are 0 to 59. As an example, 30 means 30 seconds past the chosen minute. |
| `BYSETPOS` | This selects one or more items, by position, in the list of timestamps that result after the whole calendaring expression is evaluated. It is useful for requirements such as running a job on the last workday of the month. Rather than attempting to express this with the other `BY` clauses, you can code the calendaring expression to evaluate to a list of every workday of the month, and then add the `BYSETPOS` clause to select only the last item of that list. Assuming that workdays are Monday through Friday, the syntax would then be:  ``` FREQ=MONTHLY; BYDAY=MON,TUE,WED,THU,FRI; BYSETPOS=-1 ```  Valid values are 1 through 9999. A negative number selects an item from the end of the list (-1 is the last item, -2 is the next to last item, and so on) and a positive number selects from the front of the list. The `BYSETPOS` clause is always evaluated last. `BYSETPOS` is only supported with the `MONTHLY` and `YEARLY` frequencies.  The `BYSETPOS` clause is applied to the list of timestamps once per frequency period. For example, when the frequency is defined as `MONTHLY`, the Scheduler determines all valid timestamps for the month, orders that list, and then applies the `BYSETPOS` clause. The Scheduler then moves on to the next month and repeats the procedure. Assuming a start date of Jun 10, 2004, the example evaluates to: Jun 30, Jul 30, Aug 31, Sep 30, Oct 29, and so on. |
| `INCLUDE` | This includes one or more named schedules in the calendaring expression. That is, the set of timestamps defined by each included named schedule is added to the results of the calendaring expression. If an identical timestamp is contributed by both an included schedule and the calendaring expression, it is included in the resulting set of timestamps only once. The named schedules must have been defined with the `CREATE_SCHEDULE` procedure.  This clause only works on a full day and therefore cannot be used with `BYHOUR`, `BYMIN`, and `BYSECOND`. |
| `EXCLUDE` | This excludes one or more named schedules from the calendaring expression. That is, the set of timestamps defined by each excluded named schedule is removed from the results of the calendaring expression. The named schedules must have been defined with the `CREATE_SCHEDULE` procedure.  This clause only works on a full day and therefore cannot be used with `BYHOUR`, `BYMIN`, and `BYSECOND`. |
| `INTERSECT` | This specifies an intersection between the calendaring expression results and the set of timestamps defined by one or more named schedules. Only the timestamps that appear both in the calendaring expression and in one of the named schedules are included in the resulting set of timestamps.  For example, assume that the named schedule `last_sat` indicates the last Saturday in every month, and that for the year 2005, the only months where the last day of the month is also a Saturday are April and December. Assume also that the named schedule `end_qtr` indicates the last day of each quarter in 2005:  ``` 3/31/2005, 6/30/2005, 9/30/2005, 12/31/2005 ```  These calendaring expressions result in the dates that follow:  ``` 3/31/2005, 4/30/2005, 6/30/2005, 9/30/2005, 12/31/2005 ``` ``` FREQ=MONTHLY; BYMONTHDAY=-1; INTERSECT=last_sat,end_qtr ```  In this example, the terms `FREQ=MONTHLY; BYMONTHDAY=-1` indicate the last day of each month.  This clause only works on a full day and therefore cannot be used with `BYHOUR`, `BYMIN`, and `BYSECOND`. |
| `PERIODS` | This identifies the number of periods that together form one cycle of a user-defined frequency. It is used in the `repeat_interval` expression of the schedule that defines the user-defined frequency. It is mandatory when the `repeat_interval` expression in the main schedule contains a `BYPERIOD` clause. The following example defines the quarters of a fiscal year.  ``` FREQ=YEARLY;BYDATE=0301,0601,0901,1201;PERIODS=4 ``` |
| `BYPERIOD` | This selects periods from a user-defined frequency. For example, if a main schedule names a user-defined frequency schedule that defines the fiscal quarters shown in the previous example, the clause `BYPERIOD=2,4` in the main schedule selects the 2nd and 4th fiscal quarters. |

Combining Schedules

There are two ways to combine schedules:

- Using a combined schedule expression, which is a list of individual schedules
	For example, to create a schedule for all company holidays, you provide a list of individual schedules, where each schedule in the list defines a single holiday. The Scheduler evaluates each individual schedule, and then returns a union of the timestamps returned by each individual schedule.
- Embedding other schedules into the main schedule using `include`, `exclude`, and `intersect` clauses
	With this method, the embedded schedules inherit certain attributes from the main schedule.
	- Timestamps generated by the `INCLUDE` clause that fall into periods that are skipped by the main schedule are ignored. This is the case when the main schedule skips periods due to the `INTERVAL` clause, the `BYPERIOD` clause, or the `BYMONTH` clause for `freq=monthly`.
		- Days that are added by the `INCLUDE` clause follow the hourly/minutely/secondly execution pattern of the main schedule.
		- When the `INCLUDE` clause is present, no date-specific defaults are retrieved from the start date (but time-specific defaults can be). (See " Start Dates and Repeat Intervals ", later in this section.) For example, a `repeat_interval` of `FREQ=MONTHLY;INCLUDE=HOLIDAY` executes only on holidays and not on the month/day defaults retrieved from the start date.
	The following is an example:
	```
	BEGIN
	dbms_scheduler.create_schedule('embed_sched', repeat_interval =>
	  'FREQ=YEARLY;BYDATE=0130,0220,0725');
	dbms_scheduler.create_schedule('main_sched', repeat_interval =>
	  'FREQ=MONTHLY;INTERVAL=2;BYMONTHDAY=15;BYHOUR=9,17;INCLUDE=embed_sched');
	END;
	/
	```
	In this example, the dates 1/30, 2/20, and 7/25 are added to the main schedule. However, the Scheduler does not include dates that fall in months that are skipped by the `INTERVAL` clause. If the start date of the main schedule is 1/1/2005, then 2/20 is not added. On the dates that are added, the embedded schedule follows the execution pattern of the main schedule: jobs are executed at 9:00 a.m. and 5:00 p.m. on 1/30 and 7/25. If the embedded schedule does not itself have a start date, it inherits the start date from the main schedule.

User-Defined Frequencies

Instead of using predefined frequencies like `DAILY`, `WEEKLY`, `MONTHLY`, and so on, you can create your own frequencies by creating a schedule that returns the start date of each period. For example, the following `repeat_interval` expression is used in a schedule named `fiscal_year` that defines the start of each quarter in a fiscal year:

```
FREQ=YEARLY;BYDATE=0301,0601,0901,1201;PERIODS=4
```

To return the last Wednesday of every quarter, you create a schedule (the "main schedule") that uses the `fiscal_year` schedule as a user-defined frequency:

```
FREQ=fiscal_year;BYDAY=-1WED
```

Periods in a user-defined frequency do not have to be equal in length. In the main schedule, the `BYSETPOS` clause and numbered weekdays are recalculated based on the size of each period. To select dates in specific periods, you must use the `BYPERIOD` clause in the main schedule. To enable this, the schedule that is used as the user-defined frequency must include a `PERIODS` clause, and it must set its start date appropriately. The first date returned by this schedule is used as the starting point of period 1.

As another example, assuming work days are Monday through Friday, to get the last work day of the 2nd and 4th quarters of the fiscal year, the `repeat_interval` clause in the main schedule is the following:

```
FREQ=fiscal_year;BYDAY=MON,TUE,WED,THU,FRI;BYPERIOD=2,4;BYSETPOS=-1
```

Start Dates and Repeat Intervals

The Scheduler retrieves the date and time from the job or schedule start date and incorporates them as defaults into the `repeat_interval`. For example, if the specified frequency is yearly and there is no `BYMONTH` or `BYMONTHDAY` clause in the repeat interval, then the month and day that the job runs on are retrieved from the start date. Similarly, if frequency is monthly but there is no `BYMONTHDAY` clause in the repeat interval, then the day of the month that the job runs on is retrieved from the start date. If present, `BYHOUR`, `BYMINUTE`, and `BYSECOND` defaults are also retrieved from the start date, and used if those clauses are not specified. Note that if the `INCLUDE`, `EXCLUDE`, or `INTERSECT` clauses are present, no date-related defaults are retrieved from the start date, but time-related defaults are.The following are some examples:

```
start_date:      4/15/05 9:00:00
repeat_interval: freq=yearly
```

is expanded internally to:

```
freq=yearly;bymonth=4;bymonthday=15;byhour=9;byminute=0;bysecond=0
```

The preceding schedule executes on 04/15/05 9:00:00, 04/15/06 9:00:00, 04/15/07 9:00:00, and so on.

For the next example, assume that schedule `S1` has a `repeat_interval` of `FREQ=YEARLY;BYDATE=0701`.

```
start_date:      01/20/05 9:00:00
repeat_interval: freq=yearly;include=S1
```

is expanded internally to:

```
freq=yearly;byhour=9;byminute=0;bysecond=0;include=S1
```

Because an `INCLUDE` clause is present, date-related information is not retrieved from the start date. However, time-specific information is, so the preceding schedule executes on 07/01/05 9:00:00, 07/01/06 9:00:00, 07/01/08 9:00:00, and so on.

General Rules

When using a calendaring expression, consider the following rules:

- For a regular schedule (as opposed to a combined schedule), the calendar string must start with the frequency clause. All other clauses are optional and can be put in any order.
- All clauses are separated by a semicolon, and each clause can be present at most once, with the exception of the `include`, `exclude`, and `intersect` clauses.
- Spaces are allowed between syntax elements and the strings are case-insensitive.
- The list of values for a specific `BY` clause do not need to be ordered.
- When not enough `BY` clauses are present to determine what the next date is, this information is retrieved from the start date. For example, `"FREQ=YEARLY"` with a start date of 02/15/2003 becomes `"FREQ=YEARLY;BYMONTH=FEB; BYMONTHDAY=15"`, which means every year on the 15th of February.
	`"FREQ=YEARLY;BYMONTH=JAN,JUL"` with start date 01/21/2003 becomes `"FREQ=YEARLY;BYMONTH=JAN,JUL;BYMONTHDAY=21",` which means every year on January 21 and July 21.
- The `byweekno` clause is only allowed if the frequency is `YEARLY`. It cannot be used with other frequencies. When it is present, it will return all days in that week number. If you want to limit it to specific days within the week, you have to add a `BYDAY` clause. For example, `"FREQ=YEARLY;BYWEEKNO=2"` with a start date of 01/01/2003 will return:
	```
	01/06/2003, 01/07/2003, 01/08/2003, 01/09/2003, 01/10/2003, 01/11/2003, 01/12/2003, 01/05/2004, 01/06/2004, 01/07/2004, .... and so on.
	```
	Note that when the `byweekno` clause is used, it is possible that the dates returned are from a year other than the current year. For example, if returning dates for the year 2004 and the calendar string is `"FREQ=YEARLY;BYWEEKNO=1,53"` for the specified week numbers in 2004, it will return the dates:
	```
	12/29/03, 12/30/03, 12/31/03, 01/01/04, 01/02/04, 01/03/04, 01/04/04, 12/27/04, 12/28/04, 12/29/04, 12/30/04, 12/31/04, 01/01/05, 01/02/05
	```
- For those `BY` clauses that do not have a consistent range of values, you can count backward by putting a "-" in front of the numeric value. For example, specifying `BYMONTHDAY=31` will not give you the last day of every month, because not every month has 31 days. Instead, `BYMONTHDAY=-1` will give you the last day of the month.
	This is not supported for `BY` clauses that are fixed in size. In other words, `BYMONTH`, `BYHOUR`, `BYMINUTE`, and `BYSECOND` are not supported.
- The basic values for the `BYDAY` clause are the days of the week. When the frequency is `YEARLY`, or `MONTHLY`, you are allowed to specify a positive or negative number in front of each day of the week. In the case of `YEARLY`, `BYDAY=40MON`, indicates the 40th Monday of the year. In the case of `MONTHLY, BYDAY=-2SAT`, indicates the second to last Saturday of the month.
	Note that positive or negative numbers in front of the weekdays are not supported for other frequencies and that in the case of yearly, the number ranges from -53... -1, 1... 53, whereas for the monthly frequency it is limited to -5... -1, 1... 5.
	If no number is present in front of the weekday it specifies, every occurrence of that weekday in the specified frequency.
- The first day of the week is Monday.
- Repeating jobs with frequencies smaller than daily follow their frequencies exactly across daylight savings adjustments. For example, suppose that a job is scheduled to repeat every 3 hours, the clock is moved forward from 1:00 a.m. to 2:00 a.m., and the last time the job ran was midnight. Its next scheduled time will be 4:00 a.m. Thus, the 3 hour period between subsequent job runs is retained. The same applies when the clock is moved back. This behavior is not the case for repeating jobs that have frequencies of daily or larger. For example, if a repeating job is supposed to be executed on a daily basis at midnight, it will continue to run at midnight if the clock is moved forward or backward. When the execution time of such a daily (or larger frequency) job happens to fall inside a window where the clock is moved forward, the job executes at the end of the window.
- The calendaring syntax does not allow you to specify a time zone. Instead the Scheduler retrieves the time zone from the `start_date` argument. If jobs must follow daylight savings adjustments, then you must specify a region name for the time zone of the `start_date`. For example specifying the `start_date` time zone as ' `US/Eastern` ' in New York ensures that daylight saving adjustments are automatically applied. If instead, the time zone of the `start_date` is set to an absolute offset, such as ' `-5:00` ', then daylight savings adjustments are not followed and your job execution is off by an hour for half the year.
- When `start_date` is `NULL`, the Scheduler determines the time zone for the repeat interval as follows:
	1. It checks whether or not the session time zone is a region name. The session time zone can be set by either:
		- Issuing an `ALTER` `SESSION` statement, for example:
			```
			SQL> ALTER SESSION SET time_zone = 'Asia/Shanghai';
			```
				- Setting the `ORA_SDTZ` environment variable.
		2. If the session time zone is an absolute offset instead of a region name, the Scheduler uses the value of the `DEFAULT_TIMEZONE` Scheduler attribute. For more information, see the SET\_SCHEDULER\_ATTRIBUTE Procedure.
		3. If the `DEFAULT_TIMEZONE` attribute is `NULL`, the Scheduler uses the time zone of `systimestamp` when the job or window is enabled.

BYSETPOS Clause Rules

The following are rules for the `BYSETPOS` clause.

- The `BYSETPOS` clause is the last clause to be evaluated. It is processed after all other `BY` clauses and the `INCLUDE`, `EXCLUDE` and `INTERSECT` clauses have been evaluated.
- The `INTERVAL` clause does not change the size of the period to which the `BYSETPOS` clause is applied. For example, when the frequency is set to monthly and interval is set to 3, the list of timestamps to which `BYSETPOS` is applied is generated from a month, not a quarter. The only impact of the `INTERVAL` clause is to cause months to be skipped. However, you can still select the second to last workday of the quarter like this:
	```
	FREQ=MONTHLY;INTERVAL=3;BYDAY=MON,TUE,WED,THU,FRI;BYSETPOS=-2
	```
	provided that you set the start date in the right month. This example returns the next to last workday of a month, and repeats once a quarter.
- To get consistent results, the set to which `BYSETPOS` is applied is determined from the beginning of the frequency period independently of when the evaluation occurs. Whether the Scheduler evaluates
	```
	FREQ=MONTHLY;BYDAY=MON,TUE,FRI;BYSETPOS=1,3
	```
	on 01/01/2004 or 01/15/2004, in both cases the expression evaluates to Friday 01/02/2004, and Tuesday 01/06/2004. The only difference is that when the expression is evaluated on 01/15/2004, the Scheduler determines that there are no matches in January because the timestamps found are in the past, and it moves on to the matches in the next month, February.

BYDATE Clause Rules

The following are rules for the `BYDATE` clause.

- If dates in the `BYDATE` clause do not have their optional year component, the job runs on those dates every year.
- The job execution times on the included dates are derived from the `BY` clauses in the calendaring expression. For example, if `repeat_interval` is defined as
	```
	freq=daily;byhour=8,13,18;byminute=0;bysecond=0;bydate=0502,0922
	```
	then the execution times on 05/02 and 09/22 are 8:00 a.m., 1:00 p.m., and 6:00 p.m.

EXCLUDE Clause Rules

Excluded dates without a time component are 24 hour periods. All timestamps that fall on an excluded date are removed. In the following example, `jan_fifteen` is a named schedule that resolves to the single date of 01/15:

```
freq=monthly;bymonthday=15,30;byhour=8,13,18;byminute=0;bysecond=0;
     exclude=jan_fifteenth
```

In this case, all three instances of the job are removed for 01/15.

OFFSET Rules

You can adjust the dates of individual named schedules by adding positive offsets to them. For example, to execute `JOB2` exactly 15 days after every occurrence of `JOB1`, add `+OFFSET:15D` to the schedule of `JOB1`, as follows:

```
BEGIN
dbms_scheduler.create_schedule('job2_schedule', repeat_interval =>
  'job1_schedule+OFFSET:15D');
END;
/
```

Note that negative offsets to named schedules are not supported.

Example 157-1 Putting It All Together

This example demonstrates the use of user-defined frequencies, spans, offsets, and the `BYSETPOS` and `INCLUDE` clauses. (Note that the `OFFSET:` keyword is optional in an offset clause.)

Many companies in the retail industry share the same fiscal year. The fiscal year starts on the Sunday closest to February 1st, and subsequent quarters start exactly 13 weeks later. The fiscal year schedule for the retail industry can be defined as the following:

```
begin
 dbms_scheduler.create_schedule('year_start', repeat_interval=>
       'FREQ=YEARLY;BYDATE=0201^SPAN:1W;BYDAY=SUN');
 dbms_scheduler.create_schedule('retail_fiscal_year',
        to_timestamp_tz('15-JAN-2005 12:00:00','DD-MON-YYYY HH24:MI:SS'),
         'year_start,year_start+13w,year_start+26w,year_start+39w;periods=4');
end;
/
```

The following schedule can be used to execute a job on the 5th day off in the 2nd and the 4th quarters of the retail industry. This assumes that Saturday and Sunday are off days as well as the days in the existing `holiday` schedule.

```
begin
 dbms_scheduler.create_schedule('fifth_day_off', repeat_interval=>
  'FREQ=retail_fiscal_year;BYDAY=SAT,SUN;INCLUDE=holiday;
    BYPERIOD=2,4;BYSETPOS=5');
end;
/
```

### 157.5 DBMS\_SCHEDULER Data Structures

The `DBMS_SCHEDULER` package defines `OBJECT` types and `TABLE` types.

#### 157.5.1 DBMS\_SCHEDULER JOBARG Object Type

This type is used by the `JOB` and `JOBATTR` object types. It represents a job argument in a batch of job arguments.

Syntax

```
TYPE jobarg IS OBJECT (
   arg_position         NUMBER,
   arg_text_value       VARCHAR2(4000),
   arg_anydata_value    ANYDATA,
   arg_operation        VARCHAR2(5));
```

Attributes

Table 157-2 JOBARG Object Type Attributes

| Attribute | Description |
| --- | --- |
| `arg_position` | Position of the argument |
| `arg_text_value` | Value of the argument if the type is `VARCHAR2` |
| `arg_anydata_value` | Value of the argument if the type is `AnyData` |
| `arg_operation` | Type of the operation:  - `SET` - `RESET` |

JOBARG Constructor Function

This constructor function constructs a job argument. It is overloaded to construct job arguments with different types of values.

Syntax

Constructs a job argument with a text value.

```
constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_value           IN VARCHAR2)
   RETURN SELF AS RESULT;
```

Constructs a job argument with an `AnyData` value.

```
constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_value           IN ANYDATA)
   RETURN SELF AS RESULT;
```

Constructs a job argument with a `NULL` value.

```
constructor function jobarg (
   arg_position        IN POSITIVEN,
   arg_reset           IN BOOLEAN DEFAULT FALSE)
   RETURN SELF AS RESULT;
```

Parameters

Table 157-3 JOBARG Constructor Function Parameters

| Parameter | Description |
| --- | --- |
| `arg_position` | Position of the argument |
| `arg_value` | Value of the argument |
| `arg_reset` | If `arg_reset` is `TRUE`, then the argument at that position is reset.  Setting `arg_reset` to `FALSE` (which is the default) will create an argument with a NULL value. |

JOBARG\_ARRAY Table Type

Syntax

```
TYPE jobarg_array IS TABLE OF jobarg;
```

#### 157.5.2 JOBARG\_ARRAY Table Type

The `jobarg_array` type is a table of `jobarg`.

Syntax

```
TYPE jobarg_array IS TABLE OF jobarg;
```

#### 157.5.3 DBMS\_SCHEDULER JOB\_DEFINITION Object Type

This type is used by the `CREATE_JOBS` procedure and represents a job in a batch of jobs.

Syntax

```
TYPE job_definition IS OBJECT (
  job_name                       VARCHAR2(100),
  job_class                      VARCHAR2(32),
  job_style                      VARCHAR2(11),
  program_name                   VARCHAR2(100),
  job_action                     VARCHAR2(4000),
  job_type                       VARCHAR2(20),
  schedule_name                  VARCHAR2(65),
  repeat_interval                VARCHAR2(4000),
  schedule_limit                 INTERVAL DAY TO SECOND,
  start_date                     TIMESTAMP WITH TIME ZONE,
  end_date                       TIMESTAMP WITH TIME ZONE,
  event_condition                VARCHAR2(4000),
  queue_spec                     VARCHAR2(100),
  number_of_arguments            NUMBER,
  arguments                      SYS.JOBARG_ARRAY,
  job_priority                   NUMBER,
  job_weight                     NUMBER,
  max_run_duration               INTERVAL DAY TO SECOND,
  max_runs                       NUMBER,
  max_failures                   NUMBER,
  logging_level                  NUMBER,
  restartable                    VARCHAR2(5),
  stop_on_window_close           VARCHAR2(5),
  raise_events                   NUMBER,
  comments                       VARCHAR2(240),
  auto_drop                      VARCHAR2(5),
  enabled                        VARCHAR2(5),
  follow_default_timezone        VARCHAR2(5),
  parallel_instances             VARCHAR2(5),
  aq_job                         VARCHAR2(5),
  instance_id                    NUMBER,
  credential_name                VARCHAR2(65),
  destination                    VARCHAR2(4000),
  database_role                  VARCHAR2(20),
  allow_runs_in_restricted_mode  VARCHAR2(5);
  restart_on_recovery            BOOLEAN;
  restart_on_failure             BOOLEAN;)
```

Object Attributes

Table 157-4 provides brief descriptions of the attributes of the `JOB_DEFINITION` object type. For more complete information about these attributes, see the " CREATE\_JOB Procedure " and the " SET\_ATTRIBUTE Procedure ".

Table 157-4 JOB\_DEFINITION Object Types

| Attribute | Description |
| --- | --- |
| `job_name` | Name of the job |
| `job_class` | Name of the job class |
| `job_style` | Style of the job:  - `REGULAR` - `LIGHTWEIGHT` - `IN_MEMORY_RUNTIME` - `IN_MEMORY_FULL` |
| `program_name` | Name of the program that the job runs |
| `job_action` | Inline action of the job. This is either the code for an anonymous PL/SQL block or the name of a stored procedure, external executable, or chain. |
| `job_type` | Job action type (' `PLSQL_BLOCK` ', ' `STORED_PROCEDURE` ', ' `EXECUTABLE` ', ' `CHAIN` ', ' `EXTERNAL_SCRIPT` ', ' `SQL_SCRIPT` ', and ' `BACKUP_SCRIPT` ') |
| `schedule_name` | Name of the schedule that specifies when the job has to execute |
| `repeat_interval` | Inline time-based schedule |
| `schedule_limit` | Maximum delay time between scheduled and actual job start before a job run is canceled |
| `start_date` | Start date and time of the job |
| `end_date` | End date and time of the job |
| `event_condition` | Event condition for event-based jobs |
| `queue_spec` | File watcher name or queue specification for event-based jobs |
| `number_of_arguments` | Number of job arguments |
| `arguments` | Array of job arguments |
| `job priority` | Job priority |
| `job_weight` | \*\*\* Deprecated in Oracle Database 11gR2. Do not change the value of this attribute from the default, which is 1.  Weight of the job for parallel execution. |
| `max_run_duration` | Maximum run duration of the job |
| `max_runs` | Maximum number of runs before the job is marked as completed |
| `max_failures` | Maximum number of failures tolerated before the job is marked as broken |
| `logging_level` | Job logging level |
| `restartable` | Indicates whether the job is restartable (`TRUE`) or not (`FALSE`) |
| `stop_on_window_close` | Indicates whether the job is stopped when the window that it runs in ends (`TRUE`) or not (`FALSE`). Equivalent to the `stop_on_window_close` job attribute described in the SET\_ATTRIBUTE Procedure. |
| `raise_events` | State changes that raise events |