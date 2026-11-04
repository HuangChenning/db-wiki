---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/connection-retry-logic-examples.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Connection Retry Logic Examples

Reference code examples for reconnection logic.

Simple Retry

```
Connection jdbcConnection = getConnection();
int iterationCount = 0;
int maxIterations = 10;
for (int i = 0; i < maxIterations, i++)) {
    try {
        // apply the raise (DML + commit):
        giveRaiseToAllEmployees(jdbcConnection, i * 5);
        // no exception, the procedure completed:
        iterationCount++;
        Thread.sleep(1000);
    } catch (SQLRecoverableException recoverableException) {
        // Get a new connection only if the error was recoverable.     
        System.out.println("SQLRecoverableException on iteration " + iterationCount )
        System.out.println("DB Connection lost - will attempt to get a new connection to continue with the other iterations")

        // IF its OK to lose this work and move onto the next 
        // iteration you could now try to get a new connection
        // This depends on what the code is doing; in many use
        // cases you must stop working, in others you can proceed
        // after logging a message to a log file
        // In our example, we assume we can proceed with the rest
        // of the loop if possible.
        // Using Transaction Guard, we can know if the work
        // committed and move on safely (covered in another example).
        try {
            jdbcConnection.close(); // close old  connection: 
            System.out.println("Connection closed - getting a new one")
            jdbcConnection = getConnection(); // reconnect to continue with other iterations
        } catch (Exception ex) {
           System.out.println("Unable to close or get a new connection - giving up")
           throw ex;
        } 
    } catch (SQLException nonRecoverableException) {
       // This is not a recoverable exception, so give up
       System.out.println("SQL UN-recoverable exception...give up the rest of the iterations")
       throw nonRecoverableException;        
    }
}
```

Connection Retry Logic with Transaction Guard

```
Connection jdbcConnection = getConnection();
boolean isJobDone = false;
while (!isJobDone) {
    try {
        // apply the raise (DML + commit):
        giveRaiseToAllEmployees(jdbcConnection, 5);
        // no exception, the procedure completed:
        isJobDone = true;
    } catch (SQLRecoverableException recoverableException) {
        // Retry only if the error was recoverable.            
        try {
            jdbcConnection.close(); // close old  connection: 
        } catch (Exception ex) {} // pass through other exceptions
        Connection newJDBCConnection = getConnection(); // reconnect to allow retry
        // Use Transacton Guard to force last request: committed or uncommitted
        LogicalTransactionId ltxid
            = ((OracleConnection) jdbcConnection).getLogicalTransactionId();
        isJobDone = getTransactionOutcome(newJDBCConnection, ltxid);
        jdbcConnection = newJDBCConnection;
    }
}

void giveRaiseToAllEmployees(Connection conn, int percentage) throws SQLException {
    Statement stmt = null;
    try {
        stmt = conn.createStatement();
        stmt.executeUpdate("UPDATE emp SET sal=sal+(sal*" + percentage + "/100)");
    } catch (SQLException sqle) {
        throw sqle;
    } finally {
        if (stmt != null)
            stmt.close();
    }
    // At the end of the request we commit our changes:
    conn.commit(); // commit can succeed but the commit outcome is lost
}

/**
 * GET_LTXID_OUTCOME_WRAPPER wraps DBMS_APP_CONT.GET_LTXID_OUTCOME
 */
private static final String GET_LTXID_OUTCOME_WRAPPER =
    "DECLARE PROCEDURE GET_LTXID_OUTCOME_WRAPPER(" +
    "  ltxid IN RAW," +
    "  is_committed OUT NUMBER ) " +
    "IS " +
    "  call_completed BOOLEAN; " +
    "  committed BOOLEAN; " +
    "BEGIN " +
    "  DBMS_APP_CONT.GET_LTXID_OUTCOME(ltxid, committed, call_completed); " +
    "  if committed then is_committed := 1;  else is_committed := 0; end if; " +
    "END; " +
    "BEGIN GET_LTXID_OUTCOME_WRAPPER(?,?); END;";

/**
 * getTransactionOutcome returns true if the LTXID committed or false otherwise. 
 * note that this particular version is not considering user call completion  
 */
boolean getTransactionOutcome(Connection conn, LogicalTransactionId ltxid)
throws SQLException {
    boolean committed = false;
    CallableStatement cstmt = null;
    try {
        cstmt = conn.prepareCall(GET_LTXID_OUTCOME_WRAPPER);
        cstmt.setObject(1, ltxid); // use this starting in 12.1.0.2
        cstmt.registerOutParameter(2, OracleTypes.BIT);
        cstmt.execute();
        committed = cstmt.getBoolean(2);
    } catch (SQLException sqlexc) {
        throw sqlexc;
    } finally {
        if (cstmt != null)
            cstmt.close();
    }
    return committed;
}
```

Oracle Call Interface (OCI) applications; how to determine if an error is recoverable:

```
OCIError *errhp;
sb4 errcode = 0;
text errbuf[512];
boolean recoverableError;

(void) OCIErrorGet((dvoid *)errhp, (ub4) 1, (text *) NULL, &errcode,
                    errbuf, (ub4) sizeof(errbuf), OCI_HTYPE_ERROR);

/* check if error is recoverable */
OCIAttrGet((void *)errhp, OCI_HTYPE_ERROR,
           (dvoid *)&recoverableError,(ub4 *)0,
           (ub4)OCI_ATTR_ERROR_IS_RECOVERABLE, errhp);
```