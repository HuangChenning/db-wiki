---
title: Support for DBMS_JOB in Oracle Database 11g Release 2
book: "Administrator's Guide"
doc_id: E25494-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e25494/appendix_a.htm
tags:
  - oracle
  - 11g
  - administrators-guide
---

## A Support for DBMS\_JOB in Oracle Database 11g Release 2

In this appendix:

- About DBMS\_JOB
- Moving from DBMS\_JOB to Oracle Scheduler

## About DBMS\_JOB

`DBMS_JOB` is a PL/SQL package that you use to schedule jobs. It is replaced by Oracle Scheduler, which is more powerful and flexible. Although Oracle recommends that you switch from `DBMS_JOB` to Oracle Scheduler, `DBMS_JOB` is still supported for backward compatibility.

### Configuring DBMS\_JOB

The `JOB_QUEUE_PROCESSES` initialization parameter specifies the maximum number of processes that can be created for the execution of jobs. Beginning with Oracle Database 11g Release 1, `JOB_QUEUE_PROCESSES` defaults to 1000. The job coordinator process starts only as many job queue processes as are required, based on the number of jobs to run and available resources. You can set `JOB_QUEUE_PROCESSES` to a lower number to limit the number of job queue processes.

Setting `JOB_QUEUE_PROCESSES` to 0 disables `DBMS_JOB` jobs and `DBMS_SCHEDULER` jobs.

### Using Both DBMS\_JOB and Oracle Scheduler

`DBMS_JOB` and Oracle Scheduler (the Scheduler) use the same job coordinator to start job slaves. You can use the `JOB_QUEUE_PROCESSES` initialization parameter to limit the number job slaves for both `DBMS_JOB` and the Scheduler.

If `JOB_QUEUE_PROCESSES` is 0, both `DBMS_JOB` and Oracle Scheduler jobs are disabled.

See Also:

- [Chapter 29, "Scheduling Jobs with Oracle Scheduler"](scheduse.md)
- ["Setting Scheduler Preferences"](schedadmin.md)
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams112.htm#REFRN10077) for more information about the `JOB_QUEUE_PROCESSES` initialization parameter

## Moving from DBMS\_JOB to Oracle Scheduler

This section illustrates some examples of how you can take jobs created with the `DBMS_JOB` package and rewrite them using Oracle Scheduler, which you configure and control with the `DBMS_SCHEDULER` package.

### Creating a Job

An example of creating a job using `DBMS_JOB` is the following:

```
VARIABLE jobno NUMBER;
BEGIN
 DBMS_JOB.SUBMIT(:jobno, 'INSERT INTO employees VALUES (7935, ''SALLY'',
   ''DOGAN'', ''sally.dogan@examplecorp.com'', NULL, SYSDATE, ''AD_PRES'', NULL, 
    NULL, NULL, NULL);', SYSDATE, 'SYSDATE+1');
 COMMIT;
END;
/
```

An equivalent statement using `DBMS_SCHEDULER` is the following:

```
BEGIN
 DBMS_SCHEDULER.CREATE_JOB(
   job_name          =>  'job1',
   job_type          =>  'PLSQL_BLOCK',
   job_action        =>  'INSERT INTO employees VALUES (7935, ''SALLY'',
     ''DOGAN'', ''sally.dogan@examplecorp.com'', NULL, SYSDATE,''AD_PRES'', NULL,
      NULL, NULL, NULL);',
   start_date        =>  SYSDATE,
   repeat_interval   =>  'FREQ = DAILY; INTERVAL = 1');
END;
/
```

### Altering a Job

An example of altering a job using `DBMS_JOB` is the following:

```
BEGIN
 DBMS_JOB.WHAT(31, 'INSERT INTO employees VALUES (7935, ''TOM'', ''DOGAN'', 
   ''tom.dogan@examplecorp.com'', NULL, SYSDATE,''AD_PRES'', NULL,
   NULL, NULL, NULL);',
 COMMIT;
END;
/
```

This changes the action for `JOB1` to insert a different value. An equivalent statement using `DBMS_SCHEDULER` is the following:

```
BEGIN
 DBMS_SCHEDULER.SET_ATTRIBUTE(
   name          => 'JOB1',
   attribute     => 'job_action',
   value         => 'INSERT INTO employees VALUES (7935, ''TOM'', ''DOGAN'', 
      ''tom.dogan@examplecorp.com'', NULL, SYSDATE, ''AD_PRES'', NULL,
      NULL, NULL, NULL);',
END;
/
```

### Removing a Job from the Job Queue

The following example removes a job using `DBMS_JOB`, where 14144 is the number of the job being run:

```
BEGIN
   DBMS_JOB.REMOVE(14144);
COMMIT;
END;
/
```

Using `DBMS_SCHEDULER`, you would issue the following statement instead:

```
BEGIN
   DBMS_SCHEDULER.DROP_JOB('myjob1');
END;
/
```

See Also:

- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_sched.htm#ARPLS72235) for more information about the `DBMS_SCHEDULER` package
- [Chapter 29, "Scheduling Jobs with Oracle Scheduler"](scheduse.md)