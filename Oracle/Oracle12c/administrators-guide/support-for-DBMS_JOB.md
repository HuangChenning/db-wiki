---
title: "Database Administrator’s Guide"
book: "Database Administrator's Guide"
doc_id: E85760-09
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/admin/support-for-DBMS_JOB.html
tags:
  - oracle
  - 12c
  - administrators-guide
---

- Oracle Scheduler Replaces DBMS\_JOB  
	In Oracle Database 11g Release 2 (11.2), Oracle Scheduler replaces `DBMS_JOB`. Oracle Scheduler is more powerful and flexible than `DBMS_JOB`, which is a package used to schedule jobs. Although `DBMS_JOB` is still supported in Oracle Database 12c Release 2 (12.2) for backward compatibility, Oracle strongly recommends that you switch from `DBMS_JOB` to Oracle Scheduler.
- Moving from DBMS\_JOB to Oracle Scheduler  
	This section illustrates some examples of how you can take jobs created with the `DBMS_JOB` package and rewrite them using Oracle Scheduler, which you configure and control with the `DBMS_SCHEDULER` package.

**Parent topic:** [Appendixes](appendixes.md)

### A.1 Oracle Scheduler Replaces DBMS\_JOB

In Oracle Database 11g Release 2 (11.2), Oracle Scheduler replaces `DBMS_JOB`. Oracle Scheduler is more powerful and flexible than `DBMS_JOB`, which is a package used to schedule jobs. Although `DBMS_JOB` is still supported in Oracle Database 12c Release 2 (12.2) for backward compatibility, Oracle strongly recommends that you switch from `DBMS_JOB` to Oracle Scheduler.

- Configuring DBMS\_JOB  
	The `JOB_QUEUE_PROCESSES` initialization parameter specifies the maximum number of processes that can be created for the execution of jobs.
- Using Both DBMS\_JOB and Oracle Scheduler  
	`DBMS_JOB` and Oracle Scheduler (the Scheduler) use the same job coordinator to start job slaves.

**Parent topic:** Support for DBMS\_JOB

#### A.1.1 Configuring DBMS\_JOB

The `JOB_QUEUE_PROCESSES` initialization parameter specifies the maximum number of processes that can be created for the execution of jobs.

Beginning with Oracle Database 12c Release 2, `JOB_QUEUE_PROCESSES` defaults to 4000. The job coordinator process starts only as many job queue processes as are required, based on the number of jobs to run and available resources. You can set `JOB_QUEUE_PROCESSES` to a lower number to limit the number of job queue processes.

Setting `JOB_QUEUE_PROCESSES` to 0 disables `DBMS_JOB` jobs and `DBMS_SCHEDULER` jobs.

**Parent topic:** Oracle Scheduler Replaces DBMS\_JOB

#### A.1.2 Using Both DBMS\_JOB and Oracle Scheduler

`DBMS_JOB` and Oracle Scheduler (the Scheduler) use the same job coordinator to start job slaves.

You can use the `JOB_QUEUE_PROCESSES` initialization parameter to limit the number job slaves for both `DBMS_JOB` and the Scheduler.

If `JOB_QUEUE_PROCESSES` is 0, both `DBMS_JOB` and Oracle Scheduler jobs are disabled.

### A.2 Moving from DBMS\_JOB to Oracle Scheduler

This section illustrates some examples of how you can take jobs created with the `DBMS_JOB` package and rewrite them using Oracle Scheduler, which you configure and control with the `DBMS_SCHEDULER` package.

- Creating a Job  
	An example illustrates creating a job using the `DBMS_JOB` package and the `DBMS_SCHEDULER` package.
- Altering a Job  
	An example illustrates altering a job using the `DBMS_JOB` package and the `DBMS_SCHEDULER` package.
- Removing a Job from the Job Queue  
	An example illustrates removing a job using the `DBMS_JOB` package and the `DBMS_SCHEDULER` package.

**Parent topic:** Support for DBMS\_JOB

#### A.2.1 Creating a Job

An example illustrates creating a job using the `DBMS_JOB` package and the `DBMS_SCHEDULER` package.

The following example creates a job using `DBMS_JOB`:

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

The following is an equivalent statement using `DBMS_SCHEDULER`:

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

**Parent topic:** Moving from DBMS\_JOB to Oracle Scheduler

#### A.2.2 Altering a Job

An example illustrates altering a job using the `DBMS_JOB` package and the `DBMS_SCHEDULER` package.

The following example alters a job using `DBMS_JOB`:

```
BEGIN
 DBMS_JOB.WHAT(31, 'INSERT INTO employees VALUES (7935, ''TOM'', ''DOGAN'', 
   ''tom.dogan@examplecorp.com'', NULL, SYSDATE,''AD_PRES'', NULL,
   NULL, NULL, NULL);');
 COMMIT;
END;
/
```

This changes the action for `JOB1` to insert a different value.

The following is an equivalent statement using `DBMS_SCHEDULER`:

```
BEGIN
 DBMS_SCHEDULER.SET_ATTRIBUTE(
   name          => 'JOB1',
   attribute     => 'job_action',
   value         => 'INSERT INTO employees VALUES (7935, ''TOM'', ''DOGAN'', 
      ''tom.dogan@examplecorp.com'', NULL, SYSDATE, ''AD_PRES'', NULL,
      NULL, NULL, NULL);');
END;
/
```

**Parent topic:** Moving from DBMS\_JOB to Oracle Scheduler

#### A.2.3 Removing a Job from the Job Queue

An example illustrates removing a job using the `DBMS_JOB` package and the `DBMS_SCHEDULER` package.

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

**Parent topic:** Moving from DBMS\_JOB to Oracle Scheduler