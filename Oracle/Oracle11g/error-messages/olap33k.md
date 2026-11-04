---
title: ORA-33000 to ORA-37999
book: Error Messages
doc_id: E17766-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e17766/olap33k.htm
tags:
  - oracle
  - 11g
  - error-messages
---

## 20 ORA-33000 to ORA-37999

ORA-33000: (AGOPEN00) AGGMAP workspace object cannot be accessed because it was compiled by a more recent version of string.

Cause: The AGGMAP was already compiled by a more recent version of the product than was being used to execute this command.

Action: Recompile the AGGMAP in the current version.

ORA-33002: (XSAGDNGL00) In AGGMAP workspace object, the FLOOR argument of number must be less than the CEILING argument of number.

Cause: The user specified a floor argument greater than the ceiling argument.

Action: Adjust the floor and ceiling arguments so that the floor is less than the ceiling. OBSOLETE, please remove this

ORA-33003: (XSAGDIMDROP) workspace object, to be transformed during data load, must be a base dimension and not otherwise referenced in the AGGMAP.

Action: Remove the conflicting reference or specify a valid object

ORA-33004: (XSAGDNGL01) workspace object is not a relationship array.

Cause: A RELATION clause in the AGGMAP named a workspace object that is not a relation.

Action: Name a valid self-relation in the RELATION statement.

ORA-33005: (XSAGDIMBREAK) Invalid breakout for dimension workspace object.

Cause: The user specified something that was not a valid dimension or relation on a BREAKOUTDIM line in an aggmap. This might be because the object was not a valid relation, was not over the specified dimension or was multidimensional

Action: Use a valid relation instead

ORA-33006: (XSAGDNGL02) The relation workspace object is not related to itself.

Cause: A relation was named in a RELATION clause of the AGGMAP that is not a self-relation.

Action: Name a valid self-relation in the RELATION statement.

ORA-33008: (XSAGDNGL03) The relation workspace object is not a relation over a base dimension of AGGMAP workspace object.

Cause: A relation was named in a RELATION clause of the AGGMAP that is not a relation for a base dimension of the AGGMAP.

Action: Name a valid self-relation in the RELATION statement, that is, one that has a dimension that dimensions the AGGMAP.

ORA-33009: (XSAGDNGLPREC) In AGGMAP workspace object, PRECOMPUTE may only be specified either for the entire AGGMAP or for individual RELATION statements.

Cause: PRECOMPUTE was specified both as a line in the AGGMAP and on at least one of the RELATION lines, or it was specified more than once as a line of the AGGMAP.

Action: Remove either the PRECOMPUTE line, or the PRECOMPUTE specification for all of the RELATION lines.

ORA-33010: (XSAGDNGL04) Relation workspace object is duplicated in the AGGMAP workspace object.

Cause: Two RELATION statements in the AGGMAP reference the same relation object.

Action: Remove the duplicate RELATION statement.

ORA-33012: (XSAGDNGL05) AGGMAP workspace object contains invalid syntax.

Cause: A line in the AGGMAP contains invalid syntax.

Action: Change the line to have valid syntax.

ORA-33014: (XSAGDNGL06) In AGGMAP workspace object, variable operator workspace object cannot be dimensioned by rollup dimension workspace object.

Cause: Operator variables cannot have the rollup dimension as one of their base dimensions.

Action: Modify the definition of the operator variable so that the current rollup dimension is not one of its bases.

ORA-33016: (XSAGDNGL07) In AGGMAP workspace object, workspace object is not a valid operator or variable name.

Cause: An invalid argument was supplied to the OPERATOR clause in the relation statement.

Action: Fix the OPERATOR clause so that it specifies either a valid variable name or a valid operator.

ORA-33018: (XSAGDNGL08) In AGGMAP workspace object, the data type of workspace object must be TEXT, not string.

Cause: An operator variable was supplied whose data type is not TEXT.

Action: Change the operator clause to reference a TEXT variable.

ORA-33022: (XSAGDNGL10) The measure dimension workspace object must be a TEXT or ID base dimension that does not dimension AGGMAP workspace object, but is in the same analytic workspace.

Cause: A MEASUREDIM was supplied in the AGGMAP that was not acceptable.

Action: Modify the MEASUREDIM clause to specify a valid dimension.

ORA-33024: (XSAGDNGL11) AGGMAP workspace object contains duplicate information.

Cause: The aggmap contains multiple instances of a clause that can only be specified once.

Action: Remove the extra clause.

ORA-33026: (XSAGDNGL12) In AGGMAP workspace object, workspace object is not a valid valueset.

Cause: A line in the AGGMAP contains an invalid element where a valid valueset is required.

Action: Change the line to have a valid valueset.

ORA-33028: (XSAGDNGL13) In AGGMAP workspace object, workspace object should be scalar, not a dimensioned valueset.

Cause: A line in the AGGMAP contains a dimensioned valueset where a scalared valueset is required.

Action: Change the line to have a scalar valueset.

ORA-33030: (XSAGDNGL14) In AGGMAP workspace object, you can have either a single independent PROTECT statement or PROTECT statements in your RELATION statements.

Cause: The AGGMAP either specified multiple PROTECT statements not on a RELATION line, or specified PROTECT statements both independently and on RELATION lines.

Action: Correct the AGGMAP to have valid syntax.

ORA-33032: (XSAGDNGL15) In AGGMAP workspace object, VALUESET workspace object must be in extra dimensions of the relation.

Cause: The RELATION phrase contains a VALUESET which is not over the extra dimension of the RELATION.

Action: Correct the RELATION phrase to contain a valueset over the extra dimension or not to contain any valueset.

ORA-33034: (XSAGDNGL16) In AGGMAP workspace object, VALUESET workspace object in PRECOMPUTE phrase must be in the self dimension of the relation.

Cause: The precompute phrase contains a valueset which is not over the self dimension of the relation.

Action: Correct the relation phrase to contain a valueset over the self dimension or not to contain any valueset.

ORA-33036: (XSAGDNGL17) ARGS option workspace object must be a TEXT variable.

Cause: An ARGS value had a non-text data type.

Action: Use a text variable for ARGS.

ORA-33038: (XSAGDNGL18) In AGGMAP workspace object, RELATION workspace object contains hierarchy dimensions that are also dimensions of the AGGMAP.

Cause: Hierarchy dimensions(extra dimensions) of a RELATION in the AGGMAP are base dimensions of the AGGMAP.

Action: Correct the RELATION not to have hierarchy dimensions(extra dimensions) which are also base dimensions of the AGGMAP.

ORA-33040: (XSAGDNGL19) In AGGMAP workspace object, VALUESETS workspace object and workspace object are both over the same hierarchy dimension.

Cause: Two or more different VALUESETs over the same hierarchy dimension are used in the AGGMAP.

Action: Use the same VALUESET for two RELATION phrases or use two different VALUESETs over two different hierachy dimensions.

ORA-33042: (XSAGDNGL20) In AGGMAP workspace object, VALUESET workspace object must qualify all relations dimensioned by workspace object.

Cause: A VALUESET over a hierarchy dimension qualifies some RELATIONs but not all RELATIONs dimensioned by the same hierarchy dimension.

Action: Use the same VALUESET to qualify all the RELATIONs dimensioned by the same hierarchy dimension.

ORA-33044: (XSAGDNGL21) AGGREGATE operator string requires a WEIGHTBY clause, but the ARGS clause in AGGMAP workspace object did not specify one.

Cause: The user used an operator which needs weight values but not provided the weight values.

Action: Provide weight values using a WEIGHTBY cluase.

ORA-33045: (XSAGDNGL51) The AGGREGATE operator string does not require a weight, but ARGS clause in AGGMAP workspace object specified workspace object as a weight.

Cause: The ARGS variable specified a weight even though one is not needed.

Action: Modify the ARGS variable so that it does not specify a weight for that operation.

ORA-33046: (XSAGDNGL22) In AGGMAP workspace object, you can specify only one SCREENBY clause.

Cause: The AGGMAP contained multiple SCREENBY clauses.

Action: Remove one of the SCREENBY clauses from the AGGMAP.

ORA-33048: (XSAGDNGL23) In AGGMAP workspace object, the relation workspace object and the relation workspace object are both over the same base dimension.

Cause: The AGGMAP contains incompatible RELATION statements.

Action: Remove one of the RELATION statements from the AGGMAP.

ORA-33050: (XSAGDNGL24) AGGMAP workspace object cannot be used to aggregate workspace object, because it is defined in a different analytic workspace.

Cause: The user attempted to aggregate a variable in another analytic workspace.

Action: Create an AGGMAP in the other analytic workspace to aggregate that variable.

ORA-33052: (XSAGDNGL25) AGGMAP workspace object is a dimensioned AGGMAP; it can only be used to aggregate like-dimensioned variables.

Cause: The user attempted to aggregate a variable with different dimensions than the AGGMAP. This is only possible with undimensioned AGGMAPs.

Action: Create a new undimensioned AGGMAP.

ORA-33058: (XSAGDNGL28) In AGGMAP workspace object, error code string is greater than the maximum error code of number.

Cause: The user specified an invalid ERRORMASK value.

Action: Remove the invalid value from the ERRORMASK list.

ORA-33060: (XSAGDNGL29) In AGGMAP workspace object, the value for the ERRORLOG MAX option must be greater than 0.

Cause: The user specified an ERRORLOG MAX of 0 or a negative number.

Action: Adjust the AGGMAP so that it uses a positive number.

ORA-33062: (XSAGDNGL30) In ALLOCMAP workspace object, WEIGHTBY option workspace object must be a numerical VARIABLE or FORMULA.

Cause: The WEIGHTBY clause requires numerical VARIABLE or FORMULA but the user used invalid objects.

Action: Correct the WEIGHTBY cluase to use a valid numerical VARIABLE or FORMULA.

ORA-33064: (XSAGDNGL31) In AGGMAP workspace object, the hierarchy dimension QDR workspace object cannot refer to the related dimension of the relation.

Cause: The user specified an invalid hierarchy dimension qualified data reference.

Action: Adjust the AGGMAP so that it uses a valid dimension value qualified data reference.

ORA-33066: (XSAGDNGL32) In AGGMAP workspace object, the hierarchy dimension QDR workspace object must be a hierarchy dimension of the relation.

Cause: The user specified an invalid qualified data reference for the hierarchy dimension.

Action: Adjust the AGGMAP so that it uses a valid dimension value qualified data reference.

ORA-33068: (XSAGDNGL33) In AGGMAP workspace object, the hierarchy dimension QDR over dimension workspace object must specify a positive dimension offset.

Cause: The user specified an invalid qualified data reference for the hierarchy dimension.

Action: Adjust the AGGMAP so that it uses a valid dimension value qualified data reference.

ORA-33070: (XSAGDNGL34) In AGGMAP workspace object, all QDRs of dimension workspace object must map to the same dimension position.

Cause: The user specified two conflicting hierarchy dimension qualified data references.

Action: Adjust the AGGMAP so that it uses a consistent qualified data reference.

ORA-33072: (XSAGDNGL35) In AGGMAP workspace object, the hierarchy dimension QDR over dimension workspace object must be specified for every relation dimensioned by that hierarchy dimension.

Cause: Multiple dimensions share the same hierarchy dimension, but it is only qualified within a subset of the AGGMAP relations.

Action: Adjust the AGGMAP so that it uses consistent qualified data references.

ORA-33074: (XSAGDNGL36) In AGGMAP workspace object, the offset number is not a valid offset into dimension workspace object.

Cause: The hierarchy dimension offset is an invalid dimension position.

Action: Adjust the AGGMAP so that it uses valid qualified data references.

ORA-33076: (XSAGDNGL37) In AGGMAP workspace object, the value 'number' is not a valid value of dimension workspace object.

Cause: The hierarchy dimension offset is an invalid dimension position.

Action: Adjust the AGGMAP so that it uses valid qualified data references.

ORA-33078: (XSAGDNGL39) In AGGMAP workspace object, the hierarchy dimension QDR workspace object must refer to a dimension.

Cause: The user specified an invalid qualified data reference for the hierarchy dimension.

Action: Adjust the AGGMAP so that it uses a valid dimension value qualified data reference.

ORA-33080: (XSAGDNGL40) In AGGMAP workspace object, you cannot reference dimension workspace object with both a RELATION statement and a DIMENSION statement.

Cause: The user included both RELATION and DIMENSION statements in the AGGMAP referring to the same AGGMAP.

Action: Remove one of the conflicting clauses.

ORA-33082: (XSAGDNGL41) In AGGMAP workspace object, the non-dimensioned valueset workspace object must have a parent QDR in its VALUESET statement over the VALUESET's base dimension.

Cause: The VALUESET statement specified a scalar valueset but did not include a qualified data reference to specify the parent.

Action: Add a qualified data reference specifying the parent to the VALUESET statement.

ORA-33084: (XSAGDNGL42) In AGGMAP workspace object, you cannot qualify the dimensioned valueset workspace object.

Cause: The VALUESET line referred to a dimensioned valueset.

Action: Use a non-dimensioned valueset to limit the status of the dimensioned one.

ORA-33086: (XSAGINIT01) AGGMAP workspace object cannot be dimensioned by a conjoint dimension.

Cause: The specified AGGMAP was dimensioned by a conjoint dimension.

Action: Use the CHGDFN command to change the conjoint to a composite dimension.

ORA-33092: (XSAGCOMP04) number is not the name of a MODEL in any attached analytic workspace.

Cause: An invalid model name was attached to an AGGMAP.

Action: Remove the model from the AGGMAP or create a model with that name.

ORA-33094: (XSAGGMAPLIST01) Your expression uses too much execution space. Eliminate recursion or reduce the levels of nesting.

Cause: formulas likely refer to each other recursively or with a great deal of depth.

Action: eliminate recursion and flatten formula trees.

ORA-33098: (APABBR01) A value of '%V' is not valid for the workspace object option.

Cause: An inappropriate value was specified for the named option.

Action: Set a legal value for the option.

ORA-33100: (APABBR02) Value 'number' is not valid for the workspace object option.

Cause: An inappropriate value was specified for the named option.

Action: Set a legal value for the option.

ORA-33141: (XSAWFREEZE1) The analytic workspace string is already frozen.

Cause: Attempting to freeze an AW when it is already frozen

Action: Thaw the AW before freezing it again.

ORA-33143: (XSAWFREEZE2) The analytic workspace string must be attached RW or RX.

Cause: The AW must be updatable to change the freeze state

Action: Reattach AW before freezing or thawing it again.

ORA-33145: (XSAWFREEZE3) Cannot rollback analytic workspace string; generations are in use.

Cause: One or more generations due to be destroyed as part of a rollback to freeze command are currently in use.

Action: Get sessions using those generations to detach the AW.

ORA-33147: (XSAWFREEZE4) The analytic workspace string is not frozen.

Cause: You are attempting to "rollback to freeze" an AW that is not frozen.

Action: Only execute this command on a frozen AW.

ORA-33213: (CINSERT06) The target position for MAINTAIN ADD or MAINTAIN MOVE cannot fall in the range of session-only values.

Cause: The user specified a BEFORE or AFTER clause specifying a position in the range of SESSION dimension values.

Action: Do not use a position clause, or specify a position before the first SESSION value.

ORA-33214: (CINSERT02) The workspace object dimension is too large.

Cause: The dimension has too many values.

Action: Deleted values can still take up space in the dimension and cause this error. Try removing the deleted values by exporting the dimension to EIF and reimporting it with the REPLACE DELETE option.

ORA-33215: (CINSERT07) You cannot add session-only values to the workspace object dimension.

Cause: The user tried to add a SESSION dimension value while a spreadsheet spreadsheet cursor was open.

Action: Try adding the SESSION value while the cursor is not active.

ORA-33217: (CINSERT20) Custom member values cannot be added to concat dimension workspace object, or to any of its bases, because it is not defined as UNIQUE.

Cause: Only UNIQUE concat dimensions can have custom member values.

Action: Use the CHGDFN command to change the concat dimension to UNIQUE and retry.

ORA-33218: (CINSERT04) %K is not a valid value for the workspace object dimension. Values for this dimension can have at most number significant digits after rounding to number decimal places.

Cause: The user attempted to insert a value that had too many digits into a NUMBER dimension. For instance, the user might have tried to insert the value 99999 (5 digits) into a dimension with data type NUMBER(4).

Action: Use a smaller number for the dimension value, or define a new dimension with a larger precision and replace the old dimension with the new one.

ORA-33219: (CINSERT05) %K cannot be added to workspace object because it is already a value of the dependent UNIQUE concat dimension workspace object, from leaf dimension workspace object.

Cause: A value cannot be added to a dimension if it conflicts with an existing value in a unique concat dimension containing this dimension.

Action: The concat(s) causing the conflict could be CHGDFNed to NOT UNIQUE, or either of the duplicate values could be renamed to make them UNIQUE.

ORA-33223: (CMOVE03) You cannot move a session-only dimension value.

Cause: The user named a SESSION dimension value in the MAINTAIN MOVE command.

Action: Do not try to MAINTAIN MOVE session-only dimension values.

ORA-33247: (CRENAME03) %K is already a value of the dependent UNIQUE concat dimension workspace object, from leaf dimension workspace object.

Cause: A value cannot be renamed in a dimension if the new value conflicts with an existing value in a unique concat dimension containing this dimension.

Action: The concat(s) causing the conflict could be CHGDFNed to NOT UNIQUE, or either of the duplicate values could be changed to make them UNIQUE.

ORA-33260: (DIMSHOW01) Partition number does not exist.

Cause: The DIMSHOW command specified a nonexistent partition.

Action: Specify the name of an existing partition, or remove the PARTITION qualification from the DIMSHOW command.

ORA-33261: (DIMSHOW02) A partition name may be specified only for a partitioned variable.

Cause: A PARTITION qualification was provided for an object other than a partitioned variable.

Action: Remove the PARTITION qualification.

ORA-33262: (DBERR01) Analytic workspace string does not exist.

Cause: The analytic workspace requested does not seem to be in the current database

Action: Check that you are in the correct schema and have access to the requested AW.

ORA-33263: Could not create analytic workspace string

Cause: A serious error was encountered while trying to set up the tables for the named analytic workspace. Possibilities include a tablespace that can't be written to, corrupted metadata about which AWs exist, bogus tables with names the code expects to be able to use, or the remains of a partially removed AW.

Action: There should be another error on the error stack. Consult it to determine what is causing the problem and remove that table.

ORA-33265: (DBERRBSZ) Analytic workspace string cannot be opened. Tablespace blocksize number does not match database cache size number.

Cause: The blocksize of the containing tablespace didn't match database cache size.

Action: Change either size to make them consistent, or set olap\_page\_pool\_size to 0 to allow automatic OLAP pool management when compatibility is greater than 10.2.

ORA-33267: (DBERRRLS) Analytic workspace string cannot be accessed because it has fine-grained access control applied to it

Cause: An attempt was made to access the specified analytic workspace's LOB table. The OLAP option detected the table had fine-grained security applied to it. The OLAP option requires full access to this table to operate correctly.

Action: Remove the fine-grained access control.

ORA-33268: (DBERRTHW) Analytic workspace string cannot be attached with the THAW option because it was frozen with the NOTHAW option

Cause: An attempt to attach the AW using the thaw option was made; the AW was frozen using the NOTHAW option.

Action: Either attempt the command again without the THAW option.

ORA-33269: while operating on 'string'

Cause: Error is raised to inform user what object was being worked on when an error occurred during the creation of an AW. It should always be signaled with 33263

Action: See error#33263

ORA-33270: (DBERR05) Analytic workspace string already exists.

Cause: The AW CREATE command was passed the name of an analytic workspace that already exists

Action: Specify a different name.

ORA-33271: simulated paging error

Cause: This is an internal error that should never be seen

Action: Contact Oracle technical support

ORA-33273: (XSCHKRLS01) Analytic workspace string has open cursors and cannot be detached.

Cause: A session attempted to detach an analytic workspace while there are cursors open against it.

Action: Close the open cursor before attempting to close the analytic workspace.

ORA-33274: (DBERR07) Timed out while trying to lock analytic workspace string for string.

Cause: A lock operation that was supposed to happen very quickly was taking too long. It can be due to another session being stopped while holding that lock, another session crashing while holding that lock, or an internal error.

Action: If another session is stopped, resume that session to let it release the lock. If another session has crashed, wait for a few minutes while PMON or SMON process is recovering that lock. Contact Oracle OLAP Support if none of the situations above apply.

ORA-33275: Autonomous transaction query of an UPDATEd analytic workspace is not supported

Cause: The user made attempt to reference an anayltic workspace that has uncommited updates within an autonomous query.

Action: Either COMMIT or ROLLBACK your uncommited changes, or don't use an autonomous transaction.

ORA-33278: (DBERR09) Analytic workspace string cannot be attached in RW or EXCLUSIVE mode until the changes made and updated in MULTI mode are committed or rolled back.

Cause: There are still changes to this analytic workspace that were updated and not committed when the workspace was attached in MULTI mode.

Action: Either try attaching the workspace is RO or MULTI mode or commit or roll back the transaction before trying to attach the workspace in RW or EXCLUSIVE mode.

ORA-33280: (DBERR10) Analytic workspace string cannot be attached in MULTI mode until the changes made and updated in RW or EXCLUSIVE mode are committed or rolled back.

Cause: There are still changes to this analytic workspace that were updated and not committed when the workspace was attached in RW or EXCLUSIVE mode.

Action: Either try attaching the workspace is RO, RW, or EXCLUSIVE mode or commit or roll back the transaction before trying to attach the workspace in MULTI mode.

ORA-33282: (DBERR11) Cannot wait for analytic workspace string to become available since doing so would cause a deadlock.

Cause: Trying to wait for the workspace to become available caused a deadlock.

Action: Release an analytic workspace that some other user might be waiting for before proceeding to attach this analytic workspace in this mode.

ORA-33284: (DBERR12) Analytic workspace string cannot be opened in MULTI mode before converting it by the latest version of string.

Cause: The AW is stored in 9i format.

Action: Convert the AW to a later format

ORA-33288: (DBERR15) Another user has incompatible access to analytic workspace string, and the wait timeout has expired.

Cause: An attempt to access an analytic workspace conflicted with another user's access, and the timeout specified has elapsed.

Action: Wait until the conflicting user is done.

ORA-33290: (DBERR17) Analytic workspace string cannot be attached in the mode you requested because another user has it attached in an incompatible mode.

Cause: An attempt to access an analytic workspace conflicted with another user's access, and no timeout was specified

Action: Wait until the conflicting user is done.

ORA-33291: (DBERRSYNC) Analytic workspace string cannto be attached RW until a RESYNC command has brought it up to the current generation.

Cause: Another session has updated the analytic workspace since it was attached in the current session.

Action: Execute a RESYNC AW command to bring the analytic workspace up to the most recent version.

ORA-33292: (DBERR18) Insufficient permissions to access analytic workspace string using the specified access mode.

Cause: You do not have sufficient permissions to access this analytic workspace in the desired mode.

Action: Ask the owner of the schema or OLAP DBA to grant you sufficient permissions to access the {SCHEMA}.AW${AWNAME} table (for example, SCOTT.AW$FOO table).

ORA-33293: Please use the OLAP command AW TRUNCATE to truncate this table.

Cause: This table is part of an analytic workspace, and the OLAP option needs to control the truncation of the table.

Action: use the OLAP option to truncate the table.

ORA-33295: (DBERR20) An attached analytic workspace is blocking this command.

Cause: A table cannot be dropped because an analytic workspace based on this table is being attached.

Action: Look up the session in question in GV$AW\_OLAP and kill it.

ORA-33296: (DBERR21) Analytic workspace string can only be attached RO while tablespace string is READONLY.

Cause: The underlying tablespace of the analytic workspace is in READONLY status.

Action: Attach the analytic workspace in RO mode or alter the tablespace.

ORA-33297: (DBERR22) Analytic workspace string cannot be opened because it was last modified by an incompatible version of string.

Cause: The user attempted to attach an old OLAP Services analytic workspace that cannot be converted by this version of OLAP Services.

Action: Either create a new analytic workspace or try using a version of OLAP Services compatible with the one that created this analytic workspace.

ORA-33298: (AWUPG01) Analytic workspace string is already in the newest format allowed by the current compatibility setting

Cause: User ran the DBMS\_AW.CONVERT procedure on an analytic workspace that was created in or previously upgraded to the current compatibility mode.

Action: If upgrading the analytic workspace is necessary, upgrade the database instance and then re-run DBMS\_AW.CONVERT. If the new features offered by upgrading the analytic workspace are not required, then no action is needed.

ORA-33299: Please use DBMS\_AW.AW\_RENAME to rename this table.

Cause: This table is part of an analytic workspace, and the OLAP option needs to control the rename of the table.

Action: use the OLAP option to rename the table.

ORA-33302: (DBVALID01) SEVERE ERROR: Record number multiply used.

Cause: The AW VALIDATE command has detected an error in the structure of the analytic workspace. This error will result in the corruption of one or more objects

Action: Export what you can of the analytic workspace.

ORA-33304: (DBVALID02) Note: Record number was allocated but not used. This can result in wasted space.

Cause: This is a benign message. The AW VALIDATE command found an analytic workspace has some inaccessible space.

Action: Either nothing, or export and recreate the analytic workspace

ORA-33305: (DBVALID06) Note: Record number was allocated but not used. This can result in wasted space. (PS number)

Cause: This is a benign message. The AW VALIDATE command found an analytic workspace has some inaccessible space.

Action: Either nothing, or export and recreate the analytic workspace

ORA-33306: (DBVALID03) The AW VALIDATE command cannot be used with read-only analytic workspace string.

Cause: The AW VALIDATE command does not support read-only access.

Action: Attach the analytic workspace read/write and try again.

ORA-33308: (DBVALID04) SEVERE ERROR: Record number used but not allocated

Cause: The AW VALIDATE command has detected a problem that will result in corruption of the analytic workspace. There is no corruption yet.

Action: Export and recreate the analytic workspace.

ORA-33309: (DBVALID05) SEVERE ERROR: Record number used but not allocated (PS number)

Cause: The AW VALIDATE command has detected a problem that will result in corruption of the analytic workspace. There is no corruption yet.

Action: Export and recreate the analytic workspace.

ORA-33313: (DELDENT05) workspace object cannot be deleted because it is the target of an external partition of a partitioned variable.

Cause: User attempted to delete a variable, but some partitioned variable was defined to use that variable as the target of one of its external partitions.

Action: DELETE the partitioned variable or CHGDFN DROP PARTITION the the external partition from the partitioned variable, then delete the target variable.

ORA-33315: (XSDELDENTANON) You cannot delete workspace object while looping over unnamed composite workspace object.

Cause: While looping over the named anonymous composite, an attempt was made to delete an object which is dimensioned by it.

Action: Delete the object outside of a loop over the dimension.

ORA-33332: (DSSEXIST01) Use the AW command to establish a current analytic workspace. Then start your current activity again.

Cause: There is no currently active analytic workspace. The command that generated the error requires an active analytic workspace to operate on.

Action: Execute an AW ATTACH or AW CREATE command to establish an active workspace.

ORA-33334: (DSSEXIST04) Analytic workspace string is not attached.

Cause: The specified analytic workspace is currently not attached to the session, or the name is misspelled.

Action: Attach the analytic workspace with the AW ATTACH command, or correct the spelling of the name.

ORA-33336: (DSSEXIST04A) Analytic workspace string is not attached.

Cause: The specified analytic workspace is currently not attached to the session, or the name is misspelled.

Action: Attach the analytic workspace with the AW ATTACH command, or correct the spelling of the name.

ORA-33338: (DSSEXIST05) You cannot specify the EXPTEMP analytic workspace.

Cause: The command requires a non-temporary analytic workspace to operate on.

Action: Specify an analytic workspace other than EXPTEMP.

ORA-33339: You cannot detach analytic workspace string. It is in use by an API branch.

Cause: The OLAP API is in a branch, and you are not allowed to detach the AW while the branch is active.

Action: End the branch before detaching the AW.

ORA-33413: (EIFMAKEF01) You cannot export compressed composite workspace object because one of its bases has limited status or a PERMIT READ restriction.

Cause: Export of a compressed composite to an EIF file or lob failed because one or more of the bases had some values that were not in the current status. This can be caused either by a LIMIT command or a PERMIT READ restriction on the dimension.

Action: Either set the base dimensions' statuses to ALL and remove their PERMIT READ programs, or export using the NOAGGR keyword.

ORA-33425: (EIFMAKEF15) CAUTION: Exporting NTEXT objects using string for the EIF file character set can cause loss of data. To preserve all NTEXT data, export using the UTF8 character set for the EIF file.

Cause: The user exported an object with data type NTEXT, but the EIF file that will result from the EXPORT command is not written in Unicode. Because no non-Unicode file can represent all possible Unicode data, it is possible that some data will be lost when converting from the Unicode NTEXT object to the EIF file. The EIF file will be written in the character set indicated by the "nls\_charset" argument of the EXPORT command, or, if no such argument is present, in the database character set.

Action: If the user is certain that the contents of the NTEXT object can be represented in the specified character set, then no action is necessary. Otherwise, the user can add "nls\_charset 'UTF8'" to the EXPORT command string. This will result in the EIF file being written in UTF8 Unicode, which can represent all the data contained in NTEXT objects.

ORA-33427: (EIFMAKEF16) CAUTION: NTEXT object workspace object will be exported with type TEXT.

Cause: User attempted to export an object whose data type is NTEXT, but but the EIFVERSION option indicates a version of Express / Oracle OLAP that does not support the NTEXT data type. The object will be exported as a TEXT object instead.

Action: No action needed.

ORA-33429: (EIFMAKEF17) CAUTION: NTEXT expression will be exported with type TEXT.

Cause: User attempted to export an expression whose data type is NTEXT, but but the EIFVERSION option indicates a version of Express / Oracle OLAP that does not support the NTEXT data type. The expression will be exported as a TEXT object instead.

Action: No action needed.

ORA-33443: (ESDREAD14) Discarding compiled code for workspace object because analytic workspace string is not attached.

Cause: A program used an analytic workspace name in a qualified object name. The named analytic workspace is not attached at program run time.

Action: No action necessary. The program will be automatically recompiled. It is likely that the recompile will fail with an appropriate exception code, in which case the signaled condition should be corrected and the program re-run.

ORA-33445: (ESDREAD15) Discarding compiled code for workspace object because workspace object and workspace object, which were not partition-dependent when the code was compiled, are now partition-dependent.

Cause: Two variables are "partition-dependent" if they share any external partition target variables, or if one is the target of an external partition of the other. If object names referred to non-partition-dependent variables at compile time but refer to partition-dependent variables in the run-time context, the OLAP DML program, formula, or model will be automatically recompiled.

Action: None needed.

ORA-33447: (ESDREAD16) Discarding compiled code for workspace object because workspace object and workspace object, which were partition-dependent when the code was compiled, are now not partition-dependent.

Cause: Two variables are "partition-dependent" if they share any external partition target variables, or if one is the target of an external partition of the other. If object names referred to partition-dependent variables at compile time but refer to non-partition-dependent variables in the run-time context, the OLAP DML program, formula, or model will be automatically recompiled.

Action: None needed.

ORA-33448: (ESDREAD04) Discarding compiled code for workspace object because number now has string data, whereas it had string data when the code was compiled.

Cause: The datatype of the specified variable has changed.

Action: None needed.

ORA-33449: (ESDREAD17) Discarding compiled code for workspace object because the partition method or partition dimension of number has changed since it was compiled.

Cause: The partitioning method (LIST, RANGE, or CONCAT) or the partition dimension of the partition template is sufficiently different from what it was when the code was compiled that the code must be recompiled.

Action: None needed.

ORA-33450: (ESDREAD05) Discarding compiled code for workspace object because number now has more or fewer dimensions than it had when the code was compiled.

Cause: The dimensionality of the specified object has changed.

Action: None needed.

ORA-33452: (ESDREAD06) Discarding compiled code for workspace object because number is now dimensioned by workspace object. It was dimensioned by workspace object when the code was compiled.

Cause: The dimensionality of the specified object has changed.

Action: None needed.

ORA-33454: (ESDREAD07) Discarding compiled code for workspace object because number is now string workspace object, whereas it was string workspace object when the code was compiled.

Cause: The specified object has changed.

Action: None needed.

ORA-33456: (ESDREAD08) Discarding compiled code for workspace object because number is a(n) string, which string did not expect to find in a compiled program.

Cause: The type of the specified object has changed.

Action: None needed.

ORA-33458: (ESDREAD09) Discarding compiled code for workspace object because number is now type string, whereas it was type string when the code was compiled.

Cause: The type of the specified object has changed.

Action: None needed.

ORA-33460: (ESDREAD10) Discarding compiled code for workspace object because object workspace object is not in analytic workspace string.

Cause: The specified object is not in the same analytic workspace it was in when the compiled object was compiled.

Action: None needed.

ORA-33462: (ESDREAD10A) Discarding compiled code for workspace object because object number is not in analytic workspace string.

Cause: The specified object was not in the same analytic workspace it was when the compiled object was compiled

Action: None needed.

ORA-33468: (ESDREAD13) Discarding compiled code for workspace object because number is no longer a surrogate of dimension workspace object.

Cause: When the compiled code was saved, the specified object was a surrogate of a certain dimension. Now the specified object is a surrogate of a different dimension.

Action: No action needed; program automatically recompiles.

ORA-33557: (MAINTCHK01) You cannot string values of dimension workspace object during a loop over it.

Cause: User tried to insert or delete a value of the specified dimension while some loop over that dimension was active. The loop could be an explicit FOR or ACROSS loop, or a natural expression evaluation or OLAP\_TABLE loop. Also, it could be a loop over the dimension itself or over a derived dimension (like a composite or partition template) or dimension alias that includes it. The insert or delete could be explicitly caused by the MAINTAIN command. It is also possible that the user attempted to assign a value to a variable or partition dimensioned by a composite during a loop over that composite using a qualified data reference (QDR), and that the exception was generated by the engine's attempt to insert a new position in the composite to hold the new value.

Action: Move the dimension maintenance or QDR-based variable assignment outside the dimension loop.

ORA-33558: (LOCKCHECK01) The status or contents of the workspace object dimension cannot be changed while the LOCK\_LANGUAGE\_DIMS option is set to value.

Cause: A LIMIT or MAINTAIN was attempted on the named language dimension while the boolean option LOCK\_LANGUAGE\_DIMS was set to YES.

Action: SET LOCK\_LANGUAGE\_DIMS to NO and retry the MAINTAIN or LIMIT.

ORA-33625: (FRASSIGN02) You cannot use the APPEND keyword with concat dimension workspace object.

Cause: User used the APPEND keyword on a CONCAT target in a FILEREAD, SQL FETCH or SQL SELECT command.

Action: APPENDing a value to one of the CONCATs leaves automatically appends to the CONCAT.

ORA-33733: (xsILPMLTPreOp01) The analytic workspace string cannot be REVERTed or RESYNCed while the string program is active.

Cause: The AW REVERT and AW RESYNC commands cannot be used on an analytic workspace that contains a running program.

Action: Execute the command without running the specified program.

ORA-33883: (MAKEDCL36) You cannot use the string attribute when you define an EXTERNAL partition with an existing target.

Cause: User gave the TEMPORARY keyword in the definition of an external partition whose target variable was previously defined.

Action: Any storage characteristics of the external partition are determined by the target variable. These attributes should be set when the target is defined, not when the external partition is defined.

ORA-33911: (MAKEDCL29) You cannot define a string in analytic workspace string because it has not been upgraded to version string.

Cause: User attempted to define an object that requires a certain compatibility setting in an AW that has not been upgraded to that compatibility level.

Action: Make sure that the database is running in the appropriate compatibility mode, and upgrade the AW.

ORA-33918: (MAKEDCL33) You cannot define a surrogate of dimension workspace object because it is a string.

Cause: Not all kinds of dimensions can have surrogates. The user attempted to define a surrogate of a prohibited kind of dimension.

Action: Do not attempt to define a surrogate on this dimension.

ORA-33920: (MAKEDCL34) The string SURROGATE must have one of the following data types: ID, NTEXT, TEXT, NUMBER, DATETIME, TIMESTAMP, or INTEGER.

Cause: The user attempted to define a surrogate without specifying a valid data type.

Action: Specify the data type (ID, NTEXT, TEXT, NUMBER, or INTEGER) in the definition of the surrogate.

ORA-33922: (MAKEDCL35) You cannot define a surrogate of dimension workspace object because it is a time dimension.

Cause: The user attempted to define a surrogate on a dimension that has type DAY, WEEK, MONTH, or YEAR.

Action: Do not attempt to define a surrogate on this dimension.

ORA-33998: (MODCOMP12) You cannot use both workspace object and workspace object as model dimensions, because workspace object is a surrogate of workspace object.

Cause: The user attempted to include both a dimension and its surrogate in the DIMENSION statement of a model.

Action: Use either the dimension or the surrogate in the DIMENSION statement of the model, but not both.

ORA-34000: (MODCOMP13) You cannot use both workspace object and workspace object as model dimensions, because they are both surrogates of dimension workspace object.

Cause: The user attempted to include two dimension surrogates of the same dimension in the DIMENSION statement of a model.

Action: Use either of the two surrogates in the DIMENSION statement of the model, but not both.

ORA-34001: (MODCOMP14) Concat leaf dimension workspace object already is used in a DIMENSION statement, either explicitly or as a leaf of another concat dimension.

Cause: Either two concat dimensions which share a common leaf dimension, or a concat and one of its leaves where both specified in the DIMENSION statement(s).

Action: Do not specify overlapping concat dimensions, or any leaves of specified concat dimensions.

ORA-34019: (MSCGADD03) workspace object is not a LIST PARTITION TEMPLATE.

Cause: User attempted to MAINTAINT ADD or DELETE a list value from a RANGE or CONCAT partition template.

Action: Partitioning in a RANGE or CONCAT partition template cannot be changed using the MAINTAIN command.

ORA-34021: (MSCGADD04) You must specify a partition when maintaining PARTITION TEMPLATE workspace object.

Cause: User attempted to MAINTAINT ADD or DELETE a list value from a LIST partition template, but didn't specify which partition to add to or delete from.

Action: Specify the partition: maintain (template) add to partition (partitionname) (values) or maintain (template) delete from partition (partitionname) (values)

ORA-34059: (MSEXECUT12) You cannot delete non session-only dimension values from unique concat dimension workspace object.

Cause: The user tried to apply MAINTAIN DELETE to a non-SESSION value.

Action: Only use MAINTAIN DELETE to remove SESSION values from a concat dimension.

ORA-34061: (MSEXECUT11) Session-only values cannot be added to non-unique concat dimension workspace object, or any of its base dimensions.

Cause: Only UNIQUE concat dimensions can have custom member values.

Action: Use the CHGDFN command to change the concat dimension to UNIQUE and retry.

ORA-34141: (MXCGPUT00) You cannot use the ASSIGN keyword with DIMENSION workspace object.

Cause: User used the ASSIGN keyword on a DIMENSION target in a FILEREAD, SQL FETCH or SQL SELECT command.

Action: To create a new dimension value in a FILEREAD, SQL FETCH or SQL SELECT command, use the APPEND keyword.

ORA-34143: (MXCGPUT02) You cannot assign values to SURROGATE workspace object because it is type INTEGER.

Cause: The user attempted to assign a value to a dimension surrogate whose data type is INTEGER. INTEGER surrogates, like INTEGER dimensions, cannot have values assigned to them. They can only be referenced by position.

Action: Do not attempt to assign values to an INTEGER surrogate. Values will automatically appear and disappear from the INTEGER surrogate as positions are added to or removed from the underlying dimension.

ORA-34145: (MXCGPUT03) You cannot use the APPEND keyword with SURROGATE workspace object.

Cause: User used the APPEND keyword on a SURROGATE target in a FILEREAD, SQL FETCH or SQL SELECT command.

Action: To assign a value to a SURROGATE in a FILEREAD, SQL FETCH or SQL SELECT command, use the ASSIGN keyword.

ORA-34164: (MXCGVAR01) A dimension used to define a local string variable cannot be located. Execution cannot continue.

Cause: A local relation or valueset has become invalid, most probably because an object used by the currently executing program has been deleted.

Action: This is an internal error that should be referred to Oracle technical support.

ORA-34177: (MXCHGDCL19) number cannot be deleted because one or more partitioned variables instantiate it.

Cause: User attempted to CHGDFN DELETE a partition template, but some partitioned variable had data in the partition specified for deletion.

Action: Drop the partitions that are causing the problem, then retry.

ORA-34179: (MXCHGDCL20) workspace object is not a PARTITION TEMPLATE.

Cause: User specified an object that is not a partition template where a partition template is required.

Action: Supply the name of a partition template.

ORA-34181: (MXCHGDCL21) workspace object is not a partitioned VARIABLE.

Cause: User specified an object that is not a partitioned variable in a place where a partitioned variable is required.

Action: Supply the name of a partitioned variable.

ORA-34183: (MXCHGDCL22) Partition number already exists.

Cause: User attempted to ADD a partition that already existed to a partitioned variable.

Action: None required - the partition already exists.

ORA-34210: (MXCHGDCL18) You cannot change workspace object to a dimension composite because one or more surrogates has been defined for it.

Cause: The user attempted to redefine a conjoint dimension as a composite, but the conjoint has one or more surrogates defined. A dimension that has surrogates cannot be redefined as a composite.

Action: Either delete all surrogates for the dimension, or do not attempt to redefine the dimension as a composite.

ORA-34243: (MXDCL11) You can only use the string keyword when defining a COMPOSITE.

Cause: User supplied the COMPRESSED keyword when defining an object that was not a COMPOSITE.

Action: If the intent is to create a compressed composite, make sure that the object type is COMPOSITE. Otherwise, remove the COMPRESSED keyword from the command string and rerun.

ORA-34260: (MXDCL25) You cannot use number to dimension a string because it is, or involves, a dimension composite. Use the composite's bases instead.

Cause: The user attempted to use a COMPOSITE in the dimension list of an object that does not allow for such dimensions.

Action: Use the base dimensions of the COMPOSITE in the dimension list.

ORA-34276: (MXDCL33) (Precision, Scale) arguments can only be used with a NUMBER variable or dimension.

Cause: The user attempted to use NUMBER(Precision) or NUMBER(Precision, Scale) as the datatype in a definition for some object other than a DIMENSION or VARIABLE, such as a FORMULA or PROGRAM. This error can also be produced in cases where a NUMBER data type is not allowed at all.

Action: Use the NUMBER type without specifying a precision or scale. If a NUMBER data type is not allowed at all, this fix will only change the exception message to something more specific.

ORA-34279: (MXDCL37) CONCAT can only be used when defining a DIMENSION.

Cause: The CONCAT keyword was used incorrectly.

Action: Retry the command without the CONCAT keyword.

ORA-34286: (MXDCL53) workspace object cannot be used in this context because it is a string.

Cause: User specified a dimension composite, conjoint, or partition template in a place where that kind of dimension is not allowed. For instance, a relation cannot be dimensioned by a composite, and only a variable can dimensioned by a partition template.

Action: Usually, the offending dimension can be replaced with its bases. For instance, a relation cannot be dimensioned by a a composite of PRODUCT and GEOG, but it can be dimensioned by both PRODUCT and GEOG instead.

ORA-34296: (MXDCL36) A NUMBER dimension must be defined with a fixed precision and scale, using the form NUMBER(precision) or NUMBER(precision, scale).

Cause: The user attempted to define a NUMBER dimension without specifying a precision. The proper format for declaring a number dimension is NUMBER(Precision) or NUMBER(Precision, Scale). NUMBER with no precision or scale is not allowed.

Action: Use NUMBER(Precision) or NUMBER(Precision, Scale) to specify the datatype of a NUMBER dimension.

ORA-34342: (MXDSS01) IMPORTANT: Analytic workspace string is read-only. Therefore, you will not be able to use the UPDATE command to save changes to it.

Cause: This is an informational message that reminds you that you may not save changes to the specified analytic workspace.

Action: None, unless it was desired to save changes to the analytic workspace. In that case, detach and reattach the analytic workspace read-write.

ORA-34344: (MXDSS03) Analytic workspace string is not attached.

Cause: The command attempted to operate on an analytic workspace that is not currently attached, or the name of the analytic workspace is misspelled.

Action: Attach the analytic workspace or correct the spelling.

ORA-34346: (MXDSS04) The string analytic workspace cannot be detached.

Cause: The specified analytic workspace is an internal workspace and may not be detached by the user.

Action: Specify a different analytic workspace to detach.

ORA-34348: (MXDSS05) string is used only for internal purposes and cannot be accessed as an analytic workspace.

Cause: The command attempted to operate on an internal analytic workspace used by the system.

Action: Specify a different analytic workspace.

ORA-34350: (MXDSS06) string is an open analytic workspace.

Cause: The specified analytic workspace is currently in use.

Action: The desired action requires an analytic workspace that is not currently in use.

ORA-34357: (MXDSS10) string is not an alias of analytic workspace string.

Cause: User attempted to use AW UNALIAS on a non-existent alias.

Action: Make sure that the command specified the correct analytic workspace and alias. The alias must have been assigned (using AW ALIAS) during the current session and must not have been removed by a previous AW UNALIAS or AW DETACH command.

ORA-34358: (MXDSS14) number other users reading

Cause: Used for AW LIST output formatting when %d > 1

Action: None

ORA-34359: (MXDSS11) string appears twice in the alias list.

Cause: User included the same name twice in the alias list of an AW ALIAS or AW UNALIAS command.

Action: Remove the duplicate name and try again.

ORA-34360: (MXDSS15) number other users writing

Cause: Used for AW LIST output formatting when %d > 1

Action: None

ORA-34361: (MXDSS12) number other user reading

Cause: Used for AW LIST output formatting when %d == 1

Action: None

ORA-34363: (MXDSS13) number other user writing

Cause: Used for AW LIST output formatting when %d == 1

Action: None

ORA-34374: (MXDSS27) string is not a valid analytic workspace name. Analytic workspace names must be 26 characters or less, can contain only letters, digits, and underscores, and cannot begin with a digit.

Cause: a specified AW or ALIAS name was too long or contained invalid characters.

Action: verify that AW name meets the specified criteria.

ORA-34376: (MXDSS28) string is not a valid analytic workspace name. Analytic workspace names must be 26 characters or less, can contain only letters, digits, underscores, and dollar signs, and cannot begin with a digit or dollar sign.

Cause: a specified AW or ALIAS name was too long or contained invalid characters.

Action: verify that AW name meets the specified criteria.

ORA-34481: (MXMAINT07) You cannot string values of PARTITION TEMPLATE workspace object.

Cause: User attempted to use the MAINTAIN command with some keyword other than ADD or DELETE on a partition template.

Action: It is not possible to MAINTAIN a partition template, except to add or delete values of a partition list.

ORA-34487: (MXMAINT08) You cannot string values of non-unique concat dimension workspace object.

Cause: The specified MAINTAIN operation can only be applied to UNQUE concats.

Action: Use the CHGDFN command to change the concat dimension to UNIQUE and retry.

ORA-34489: (MXMAINT06) You cannot maintain workspace object because it is a SURROGATE.

Cause: The user attempted to use the MAINTAIN command on a dimension surrogate. The MAINTAIN command can only be used with real dimensions, not surrogates.

Action: Use the MAINTAIN command to modify the underlying dimension of the surrogate instead.

ORA-34514: (MXOPERR) You cannot string string data in the expression that begins with 'string'.

Cause: The user attempted an invalid operation.

Action: None

ORA-34647: (MXSQL18) The text expression in a CURSOR FOR TEXT declaration cannot be NA.

Cause: The text for the SELECT expression in a CURSOR FOR TEXT declaration was evaluated at compile time as NA.

Action: Specify a text expression that is not NA at the time the program containing the SQL DECLARE is compiled.

ORA-34656: (MXSQL24) Additional WHERE clause conditions with CURRENT OF \<cursor name> syntax

Cause: A SQL UPDATE or DELETE statement tried to use the CURRENT of \<cursor name> syntax with a WHERE clause containing multiple conditions.

Action: When using the CURRENT OF \<cursor name> syntax make sure it is the only condition in the WHERE clause.

ORA-34658: (MXSQL25) The words CURSOR FOR TEXT must be followed by a compile-time text expression specifying a SELECT command.

Cause: A SQL DECLARE \<csr> CURSOR FOR TEXT command lacked a text expression, or the expression was otherwise invalid.

Action: Specify a single text expression that can be evaluated at compile time to yield a SELECT statement

ORA-34719: (NLSCHARSET03) Character data loss in NTEXT/TEXT conversion

Cause: When character set conversion happens between TEXT and NTEXT either implicitly or explicitly, some characters are lost due to no mapping characters in the destination character set.

Action: Make sure all the characters can be mapped to destination character set or set NLS\_NCHAR\_CONV\_EXCP to be FALSE. Note: This message is the OLAP equivalent of ORA-12713.

ORA-34722: (NLSCHARSET05) CAUTION: Character data loss in character set conversion from string to string

Cause: Some operation required a string to be converted into a different character set, but the string contained characters that didn't exist in the new character set.

Action: Choose different character sets.

ORA-34726: (NLSCHARSET06) CAUTION: String truncated during character set conversion from string to string

Cause: Some operation required a string to be converted into a different character set. The string required more bytes in the new encoding, and exceeded some byte limit on its allowable length, causing some characters to be removed from the end of the string.

Action: If the byte limit is due to using the ID datatype, consider using the CHAR datatype instead. If the byte limit is due to the limit of 4000 bytes per line of CHAR data, break the long line up into multiple lines.

ORA-34731: (NLSSORT01) 'number' is not a valid NLS\_SORT specification.

Cause: An unrecognized NLS\_SORT value was specified in the SORT command or the SORT, SORTLINES or UNIQUELINES function.

Action: Specify a supported NLS\_SORT value.

ORA-34738: (NOUPDATE) A severe problem has been detected. Analytic workspace operations have been disabled.

Cause: A previous fatal error has marked the session so that it cannot perform any UPDATEs

Action: Start a new session

ORA-34761: (NXHANDLEALLO) A decimal overflow occurred during an ALLOCATE operation. The results are not reliable.

Cause: While performing an ALLOCATE, a decimal overflow occurred

Action: Correct the data or use a higher precision datatype

ORA-34796: (OCI08) SQL host variable number cannot be bound.

Cause: The data type of the host variable is not supported.

Action: Specify only variables of supported types as host variable names.

ORA-34802: (OCI11) OLAP OCI operation caused ROLLBACK past an UPDATE of an attached analytic workspace. Current operation canceled.

Cause: ROLLBACK past the UPDATE of one of the attached Analytic Workspaces was called. The current operation is aborted, and the Analytic Workspace detached.

Action: Change the called SQL procedure to avoid the ROLLBACK

ORA-34804: (OCI12) The value of SQL host variable number is too long. Use the WIDE keyword for columns that may exceed number bytes.

Cause: The host variable had a text value longer than the maximum SQL VARCHAR length

Action: Use the WIDE keyword in the host variable specification, e.g.:WIDE OLAP\_object\_name

ORA-34805: (OCI13) Statement number must have at least one host variable.

Cause: Statements prepared with DIRECT=YES must have at least one host variable.

Action: Add a host variable to the prepared statements declaration.

ORA-34806: (OCI14) Statement number can only be executed within an ACROSS command.

Cause: Statements prepared with DIRECT=YES must be executed in an ACROSS command.

Action: Execute the statement within an ACROSS command.

ORA-34840: (OPCREATE01) The string option must be declared with datatype string.

Cause: An attempt was made to declare the option with the wrong datatype.

Action: Declare the option with the correct datatype.

ORA-34841: (OPCREATE02) The string option must be declared with the READONLY attribute.

Cause: An attempt was made to declare the option without the READONLY attribute.

Action: Declare the option READONLY.

ORA-34871: (PERMIT06) Session-only value 'value' of workspace object has been deleted because a PERMIT change has revealed a duplicate value.

Cause: Execution of a PERMIT command revealed a permanent dimension or surrogate value having the same name as the SESSION value.

Action: If the SESSION value is still needed, add it with a different name.

ORA-34896: (PPMONTHS00) At least 12 month names must be given. Only number were provided.

Cause: There must be at least one name for each month. Not enough names were provided.

Action: Provide at least 12 names.

ORA-34897: (PPMONTHS01) Blank lines are not allowed in the MONTHNAMES option.

Cause: There is at least one blank line in the string populating the MONTHNAMES option. We do not allow blank month names.

Action: Remove the blank line(s) from the string.

ORA-34900: (PPWKDAYS00) At least 7 day names must be given. Only number were provided.

Cause: There must be at least one name for each day. Not enough names were provided.

Action: Make sure there are at least 7 names in the string.

ORA-34901: (PPWKDAYS01) Blank lines are not allowed in the DAYNAMES option.

Cause: There is at least one blank line in the string populating the DAYNAMES option. We do not allow blank day names.

Action: Remove the blank line(s) from the string.

ORA-35016: (QFCHECK00) The analytic workspace and EIF file definitions of workspace object have a mismatched type.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35017: (QFCHECK06) The Analytic Workspace and EIF file definitions of workspace object have different partitioning methods.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35018: (QFCHECK01) The analytic workspace and EIF file definitions of workspace object have a mismatched data type.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35019: (QFCHECK07) The Analytic Workspace and EIF file definitions of workspace object have different partition dimensions.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35020: (QFCHECK02) The analytic workspace and EIF file definitions of workspace object have mismatched dimensioning.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35021: (QFCHECK08) The EIF file definition of workspace object has some partitions that are not present in the existing Analytic Workspace object.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35022: (QFCHECK03) The analytic workspace and EIF file definitions of workspace object have a mismatched relation.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35023: (QFCHECK09) The analytic workspace and EIF file definitions of workspace object have incompatible partition definitions.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35024: (QFCHECK04) The analytic workspace and EIF file definitions of workspace object have mismatched time dimension attributes.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35026: (QFCHECK05) The analytic workspace and EIF file definitions of workspace object have a mismatched ALIASOF dimension.

Cause: Importing from an EIF file or LOB into an existing Analytic Workspace object failed because the definition of the existing object was too different from the definition of the object in the EIF file or LOB.

Action: Import the object into an Analytic Workspace that does not already contain an object with the same name.

ORA-35031: (QFSVNS00) The IMPORT command has terminated because of a defect in the EIF file.

Cause: The EIF file contains a compressed composite with defective aggregation data.

Action: Recreate the EIF file using the NOAGGR keyword.

ORA-35062: (QFGET01) Duplicate files found for extension number number of EIF file string.

Cause: IMPORT searched the directories specified in EIFEXTENSIONPATH and found two EIF extension files with the same name (differing at most by the case used in the final name component.

Action: Delete, rename or move any files that are not to be read by IMPORT.

ORA-35066: (QFGET03) Extension number number is missing for EIF file string.

Cause: IMPORT searched the directories specified in EIFEXTENSIONPATH and could not find the appropriately numbered extension file.

Action: Move the missing file into one of the searched directories.

ORA-35071: (QFHEAD06) EIF file string cannot be imported because analytic workspace string has not been upgraded to version string.

Cause: User attempted to import from an EIF file that was created by a newer version of the product into an AW that was created by a older version of the product.

Action: Make sure that the compatibility mode parameter in the init.ora of the importing instance specifies a version that is at least as high as the parameter was in the exporting instance. Then, convert the AW to the latest storage format and reexecute the import command. Alternatively, change the EIFVERSION option of the exporting instance to a lower number, recreate the EIF file, and import the new file.

ORA-35074: (QFHEAD02) EIF file string cannot be read by this version of string.

Cause: The EIF file was created with an internal version number indicating it may contain objects that are not compatible with the current Oracle OLAP version, or the EIF file is in an obsolete format.

Action: If possible, set EIFVERSION in the exporting instance to a lower number, recreate the EIF file, and import the new file.

ORA-35076: (QFHEAD04) CAUTION: The textual data in EIF file string is encoded in a character set that is not recognized by this version of string.

Cause: IMPORT could not recognize the character set specification in the EIF file.

Action: Check the imported text data. If it was not imported correctly, recreate the EIF file with a character set supported by the current Oracle version.

ORA-35078: (QFHEAD05) An EIF extension file header for string is not in the correct format.

Cause: An EIF extension file in multi-file IMPORT did not contain correct header information.

Action: Check to be sure that EIFEXTENSIONPATH is set correctly and that all the extension files for the current IMPORT were created by the same EXPORT command as the main EIF file.

ORA-35095: (QFSVNS01) One or more imported values of fixed-width dimension workspace object have been truncated.

Cause: The data in the EIF file was exported from a dimension with wider values than the target dimension will accommodate.

Action: Change the definition of the target dimension, or check to be sure that multiple values from the target dimension have not become identical during the import process. This could cause data loss as data from later dimension values overstores data imported earlier.

ORA-35106: (REGRESS00) The regression was not calculated because of a linear relationship between your independent variables.

Cause: The values of the specified independent variables are not independent. For example, one may be a multiple of the other.

Action: Chose independent variables whose values are truly independent of one another.

ORA-35171: you may not signal error number string with the SIGNAL command

Cause: The user attempted to explicitly signal an invalid error number with the OLAP DML SIGNAL command

Action: Signal another error number

ORA-35180: (SNSYN103) The format of the OUTFILE command is: OUTFILE \[APPEND\] {EOF | TRACEFILE | filename \[NOCACHE\] \[NLS\_CHARSET name\]}

Cause: The user specified incorrect syntax for the OUTFILE command.

Action: None

ORA-35276: (SNSYN163) The format of the ALLOCATE command is: ALLOCATE varname \[SOURCE svarname\] \[BASIS bvarname \[ACROSS dimname\]\] \[TARGET tvarname \[TARGETLOG logvarname\]\] \[USING aggmap\]

Cause: The user used incorrect syntax for the ALLOCATE command.

Action: Correct the calling syntax.

ORA-35280: (SNSYN165) The format of the AGGREGATE command is: AGGREGATE varname1 \[varname2 varname3...\] \[USING aggmap-name\] \[COUNTVAR intvar-name1 \[intvar-name2 intvar-name3...\]\] \[FUNCDATA\] \[FORCEORDER\] \[PARALLEL #\] \[{FROM|FROMVAR} fromname \[, fromname2...\]\]

Cause: The user used incorrect syntax for the AGGREGATE command.

Action: Correct the calling syntax.

ORA-35282: (SNSYN166) The format of the AGGREGATE function is: AGGREGATE(varname \[USING aggmap-name\] \[COUNTVAR intvar-name\] \[FORCECALC\] \[FORCEORDER\] \[{FROM|FROMVAR} fromname \[, fromname2...\]\])

Cause: The user used incorrect syntax for the AGGREGATE function.

Action: Correct the calling syntax.

ORA-35561: (XSRWLD01) Object workspace object is not a valid target.

Cause: An invalid object was specified as a target.

Action: Choose a valid object as a target.

ORA-35562: (SQLIMP01) The SQL IMPORT command will produce number columns of output, but you have provided number host variables in your INTO clause.

Cause: The expression is the source query do not match the targets in the INTO clause.

Action: Make sure the the expressions in the source query match the targets in the INTO clause.

ORA-35563: (XSRWLD17) Multiple values exist for an attribute of this dimension member.

Cause: Multiple source table rows containing different values for a dimension attribute were found. Only the first of the multiple rows has been loaded.

Action: Fix the mapping or remove the rows with conflicting attribute values.

ORA-35564: (XSRWLD02) Cannot convert from the string type to the string type.

Cause: Conversion from source to target is not allowed

Action: Choose a different target datatype

ORA-35565: (XSRWLD03) For object workspace object only APPEND, MATCH or ASSIGN may be used.

Cause: An incorrect setting was applied to the target

Action: For DIMENSIONs use APPEND or MATCH, for SURROGATEs use ASSIGN.

ORA-35566: (XSRWLD04) Object workspace object cannot be used with QDRs

Cause: A QDR was placed on a target dimension

Action: Remove the QDR on the target dimension

ORA-35568: (SQLIMP03) The datatype of variable number should be INTEGER, LONGINTEGER or SHORTINTEGER.

Cause: The target variable was not INTEGER, LONGINTEGER or SHORTINTEGER.

Action: The target variable must be INTEGER, LONGINTEGER or SHORTINTEGER.

ORA-35569: (XSRWLD05) An error was encountered in converting data string to string in column number.

Cause: The data could not be converted to the target datatype.

Action: Ensure the source data is valid for the target datatype.

ORA-35570: (XSRWLD06) A column value is not a valid member of its target dimension.

Cause: The source value for a dimension is not an existing member of the dimension.

Action: Ensure the column value is an existing member of its target dimension.

ORA-35571: (XSRWLD07) The maximum number of load errors has occurred. No changes from this step were committed to the database.

Cause: The number of load errors exceeded the specified maximum.

Action: Fix the load errors, or increase the maximum number allowed and rerun the load.

ORA-35572: (XSRWLD08) A column value is not a valid member of its related dimension.

Cause: The source data for a relation is not a member of the related dimension.

Action: Ensure the source data is a valid member of the related dimension.

ORA-35573: (XSRWLD09) An incoming dimension value is null.

Cause: A source value for a dimension is null.

Action: Ensure the source data for the dimension is not null.

ORA-35578: (SQLOUT11) SQL cursor 'number' cannot be used with CURRENT OF \<cursor name> syntax

Cause: The CURRENT OF \<cursor> syntax in the WHERE clause tried to use a cursor that was not declared with the FOR UPDATE \[ of \<column name> \] SQL syntax.

Action: Add the FOR UPDATE \[ OF \<column name> \] SQL syntax to the cursor specified.

ORA-35580: (XSRWLD10) An incoming column contains a data type mismatch.

Cause: The data could not be converted to the target datatype.

Action: Ensure the source data is valid for the target datatype.

ORA-35581: (XSRWLD11) You do not have permission to write this value of the target.

Cause: You do not have sufficient permissions to write to the specified target.

Action: Ask the owner of the schema or OLAP DBA to grant you sufficient permissions.

ORA-35582: (XSRWLD12) Cannot change the level of dimension member "number" from "number" to "number" within a single load.

Cause: A dimension member is mapped to more than one level.

Action: Change the mapping so that each dimension member is mapped to only one level.

ORA-35583: (XSRWLD13) Cannot change the level of a dimension member within a single load.

Cause: A dimension member is mapped to more than one level.

Action: Change the mapping so that each dimension member is mapped to only one level.

ORA-35585: (XSRWLD14) This SQL query generated rejected records.

Cause: Rejected records were generated by this query.

Action: Locate the records that were rejected and resolve the rejection (for example, data, mapping, and so on).

ORA-35587: (SQLOUT20) The nesting of table functions and SQL commands has exceeded the maximum of number levels.

Cause: The nesting of table functions with the PREDMLCMD token populated with an OLAP DML expression that use the embedded SQL support to access another table function which contains a table functions with the PREDMLCMD token filled in with an OLAP DML expression that uses the embedded SQL support.

Action: Reduce the level of nesting between table functions and OLAP DML embedded SQL support.

ORA-35588: (XSRWLD15) Cannot change the parent of existing dimension member "number" from "number" to "number" in LOAD RETAIN mode.

Cause: An attempt was made to change the parent of an existing dimension member in LOAD RETAIN mode.

Action: Fix the mapping or use LOAD NOSYNCH mode.

ORA-35589: (XSRWLD16) Cannot change the parent of an existing dimension member in LOAD RETAIN mode.

Cause: An attempt was made to change the parent of an existing dimension member in LOAD RETAIN mode.

Action: Fix the mapping or use LOAD NOSYNCH mode.

ORA-35749: (VCHEX01) 'character' is not a valid hexadecimal digit.

Cause: The text being converted contains an invalid hexadecimal digit.

Action: Replace the character with a digit in the range 0-9 or A-F.

ORA-35756: (VCTODT02) 'number' is not a valid date because number is out of range for a year.

Cause: n'%1p'

Action: None

ORA-35810: (XSINPUTERR) The command has requested more input than was supplied in the command string.

Cause: The command required input that was not supplied in the string.

Action: Reexecute the command with the required input.

ORA-35917: (XSHIDE05) You cannot HIDE model workspace object because the analytic workspace in which it is defined has not been upgraded to version string.

Cause: User attempted to apply the HIDE command to a model in an AW that has not been upgraded to the necessary compatibility level.

Action: Make sure that the database is running in the appropriate compatibility mode, and upgrade the AW.

ORA-35952: (XSSPFC01) The string dimension workspace object and the string dimension workspace object must have the same number of values in status for SPFCEXEC method number.

Cause: This method requires the named dimensions to have the same number of values in status, but the user provided statuses of different lengths.

Action: Relimit the dimensions so that their status lengths are the same.

ORA-36017: (XSHIERCK10) The definition of hierarchy workspace object over number in level number is not star consistent. The collision parents include number.

Cause: The definition of the hierarchy was not star consistent.

Action: Change the definition of the hierarchy.

ORA-36018: (XSHIERCK02) The format of the HIERCHECK command is: HIERCHECK relation \[STATUS|NOSTATUS|valueset\] \[MULTIPATH\] \[CONSISTENT\] \[{BALANCED|STAR\_CONSISTENT} levelrelation\] Or HIERCHECK aggmap \[MULTIPATH\] \[CONSISTENT\]

Cause: The wrong object type was specified.

Action: Change the object to a RELATION or AGGMAP.

ORA-36019: (XSHIERCK11) The format of the HIERSHAPE function is: HIERSHAPE(relation\[(qdr)\] {level|ragged|skiplevel|regular} USING levelrel \[INHIERARCHY inhvs\] LEVELORDER levelvs)

Cause: The wrong object type or the wrong object definition was specified.

Action: Change the object type or use the correct object definition.

ORA-36020: (XSHIERCK03) The definition of hierarchy workspace object over number is inconsistent.

Cause: The definition of the hierarchy was inconsistent.

Action: Change the definition of the hierarchy.

ORA-36021: (XSHIERCK12) The format of the HIERCHECK function is: HIERCHECK(relation \[STATUS|NOSTATUS|valueset\] \[MULTIPATH\] \[CONSISTENT\] \[{BALANCED|STAR\_CONSISTENT} levelrelation\]) Or HIERCHECK(aggmap \[MULTIPATH\] \[CONSISTENT\])

Cause: The wrong object type was specified.

Action: Change the object to a RELATION or AGGMAP.

ORA-36022: (XSHIERCK04) Valuesets specified in the HIERCHECK command must be scalar. workspace object is dimensioned.

Cause: The HIERCHECK command specified a dimensioned valueset.

Action: Specify a scalar valueset in its place.

ORA-36024: (XSHIERCK05) Valueset workspace object must contain values of one of the extra dimensions of relation workspace object.

Cause: The HIERCHECK command specified a valueset over an invalid dimension.

Action: Specify a valueset containing values of one of the self-relation's extra dimensions (the dimensions in the relation's dimension list, minus the self-related dimension itself).

ORA-36025: (XSHIERCK06) The level dimension of the level relation workspace object is the same as the relation dimension workspace object.

Cause: The level dimension was the same as the relation dimension.

Action: Change the definition of the level relation.

ORA-36026: (XSHIERCK07) Level relation workspace object is not dimensioned by relation dimension workspace object.

Cause: The level relation was not dimensioned by the relation dimension.

Action: Change the definition of the level relation.

ORA-36027: (XSHIERCK08) Hierarchy workspace object is not balanced.

Cause: The current hierarchy was not balanced.

Action: Change the hierarchy to balanced.

ORA-36028: (XSHIERCK09) Hierarchy workspace object has multiple paths from number to number.

Cause: The current hierarchy had multiple paths.

Action: Remove multiple paths from the hierarchy.

ORA-36034: (XSMHIERCK00) One or more loops have been detected in relationship workspace object over workspace object. The last number of the items are number.

Cause: A relation was used that had loops in it. There were more items involved than could be reported.

Action: Correct the relation so that it does not contain loops.

ORA-36035: (XSMHIERCKREL) One or more loops have been detected in workspace object. number items involved are number.

Cause: A relation was used that had loops in it.

Action: Correct the relation so that it does not contain loops.

ORA-36036: (XSMHIERCK01) One or more loops have been detected in relationship workspace object over workspace object. The number items involved are number.

Cause: A relation was used that had loops in it.

Action: Correct the relation so that it does not contain loops.

ORA-36145: (SETPROP01) The property "%1" cannot be set for measure "%2".

Cause: A property name was given that is not one of the allowed properties to be set.

Action: Specify one of the legal property names.

ORA-36154: (XSMXAGGR01) workspace object is not a data variable.

Cause: An object was specified on the Aggregate command line that was not a variable

Action: Specify a variable instead

ORA-36155: (XSMXAGGRFROM) workspace object must be a variable or formula of a similar data type to workspace object to be used with FROM, or a TEXT variable or formula to be used with FROMVAR.

Cause: The user specified an illegal variable for use with FROM or FROMVAR on the AGGREGATE command line

Action: Specify a legal variable instead

ORA-36157: (XSMXAGGRCOMMIT) To use the AUTOCOMMIT keyword, you must also specify the AUTOUPDATE keyword.

Cause: The user specified AUTOCOMMIT but not AUTOUPDATE on the AGGREGATE command line, which is illegal

Action: Either also specify AUTOUPDATE or don't specify AUTOCOMMIT

ORA-36160: (XSMXAGGR04) You cannot use string on scalar VARIABLE workspace object.

Cause: The user tried to run the AGGREGATE or AGGCOUNT command or function on a scalar variable.

Action: Specify a dimensioned variable instead

ORA-36161: (XSAGGRRUVCV) Aggregation variable workspace object cannot have itself as a COUNTVAR.

Cause: The user specified the same variable as both an aggregation variable and a COUNTVAR

Action: Specify a different COUNTVAR

ORA-36162: (XSMXAGGR05) COUNTVAR variable workspace object must be of type INTEGER, not string.

Cause: The user specified a non-INTEGER variable as a COUNTVAR for aggregation

Action: Redefine the COUNTVAR to be an INTEGER

ORA-36164: (XSMXAGGR07) When using the COUNTVAR clause, the number of variables to be aggregated (number) must match the number of COUNTVAR variables (number).

Cause: The user specified a COUNTVAR clause to the AGGREGATE command, but the number of COUNTVAR variables specified did not match the number of variables to be aggregated

Action: Specify a separate COUNTVAR for each variable

ORA-36165: (XSAGGCNTPROP) Variable workspace object cannot have both an AGGCOUNT and the $COUNTVAR property.

Cause: An attempt was made to add the $COUNTVAR property to a variable which already had an AGGCOUNT, or vice versa.

Action: Delete the already existing $COUNTVAR property or AGGCOUNT first.

ORA-36166: (XSMXAGGR08) workspace object is not a VARIABLE.

Cause: An attempt was made to perform an AGGREGATE or other action on an object which is not a variable.

Action: Specify a variable instead.

ORA-36167: (XSAGGRFORM) workspace object is an illegal AGGMAP for aggregating a FORMULA.

Cause: The user attempted to aggregate a FORMULA using an AGGMAP that is not valid for aggregating FORMULAs. The AGGMAP must specify PRECOMPUTE(NA) for all relation lines and must not specify any caching.

Action: Correct the AGGMAP so it is legal for aggregating a FORMULA.

ORA-36168: (XSMXAGGR10) COUNTVAR variable workspace object must have the same dimensionality as workspace object

Cause: The user specified a COUNTVAR variable which is missing at least one dimension of the aggregation variable

Action: Specify a COUNTVAR variable which has at least as many base dimensions as the aggregation variable

ORA-36170: (XSMXAGGR12) The data type of the WEIGHT workspace object must be numeric or BOOLEAN, not string.

Cause: The user specified a WEIGHT variable or formula which wasn't numeric or boolean

Action: Specify a numerical or boolean weight instead

ORA-36174: (XSMXAGGR23) workspace object must be either a VARIABLE, a RELATION or a FORMULA.

Cause: The user specified something that was not a variable, a relation or a formula as a weight for AGGREGATE

Action: Specify a valid variable, relation or formula instead

ORA-36176: (XSMXAGGR25) Relation workspace object must be a one-dimensional self-relation to be used as a weight for AGGREGATE.

Cause: The user specified an illegal relation as a weight. The relation might have been multidimensional, not a self-relation, or not a relation over one of the bases of the aggregation variable.

Action: Specify a valid self relation over one of the bases of the aggregation variable.

ORA-36178: (XSAGGR01) To be used with AGGREGATE, AGGMAP workspace object must be declared with the AGGMAP command.

Cause: The user used the ALLOCMAP command to define the AGGMAP, so the AGGMAP can only be used with the ALLOCATE command, or the AGGMAP has no contents attached to it.

Action: Use the AGGMAP command to define the AGGMAP.

ORA-36179: (XSNOAGM) No AGGMAP was specified for VARIABLE workspace object.

Cause: The user used the AGGREGATE command without specifying an AGGMAP on the command line, with a variable which had no $AGGMAP property.

Action: Specify an AGGMAP on the AGGREGATE command line, or add the $AGGMAP property to the variable in question.

ORA-36180: (XSAGGR08) AGGREGATE cannot function because there is a permission clause associated with variable workspace object.

Cause: When using AGGREGATE, only simple permissions and permissions on base dimensions are valid.

Action: Remove the permissions clause from the variable causing problems.

ORA-36181: A VARIABLE cannot have both the $AGGREGATE\_FROM and $AGGREGATE\_FROMVAR properties applied to it.

Cause: The user attempted to add both the $AGGREGATE\_FROM and $AGGREGATE\_FROMVAR properties to a single variable.

Action: Remove the existing property before applying the new one.

ORA-36182: (XSAGGR09) Could not locate a value for variable number in measure dimension workspace object.

Cause: A measure dimension was supplied in the AGGMAP, but a position for the variable was not found in it.

Action: Add a position for the variable in the measure dimension.

ORA-36184: (XSAGGR10) You do not have sufficient permissions for the variable workspace object.

Cause: The user lacked the permissions necessary for the aggregation variable.

Action: Remove the restricting permissions from the variable or base dimension.

ORA-36185: (XSAGGR11) workspace object does not have any AGGCOUNT information.

Cause: User attempted an operation (such as the AVERAGE aggregation operator or the AGGCOUNT function) that requires a variable to have AGGCOUNT information on a variable that does not.

Action: Define the variable using the WITH AGGCOUNT clause, or use the CHGDFN ADD AGGCOUNT command to enable AGGCOUNT for the variable.

ORA-36188: (XSAGGR16) AGGREGATE read a value less than 1 out of COUNTVAR variable workspace object. Either the values of the COUNTVAR variable are stored improperly, or there is problem in AGGREGATE. If no one has modified the values in this COUNTVAR, contact Oracle customer support.

Cause: Either someone improperly changed the COUNTVAR variable, or AGGREGATE has an error.

Action: Set the COUNTVAR variable to NA before starting AGGREGATE. If you previously set the COUNTVAR variable to NA, then contact Oracle OLAP technical support.

ORA-36198: (XSAGGR33) Cannot aggregate over COMPRESSED COMPOSITE workspace object using AGGMAP workspace object because the operator variable with more than 1 line dimensions is not supported for bases of a COMPRESSED COMPOSITE.

Cause: The user specified an aggregation the operator variable with more than 1 line dimensions that is not supported by COMPRESSED COMPOSITES.

Action: Use a MODEL for the calculation, or use an uncompressed COMPOSITE.

ORA-36200: (XSAGGR34) AGGREGATE operator string requires a WEIGHTBY clause, but ARGS variable workspace object did not specify one.

Cause: The given operator requires a WEIGHT specification, but the ARGS variable did not supply one.

Action: Modify the ARGS variable to specify a weight for the operation.

ORA-36201: (XSAGGR35) Cannot aggregate workspace object(partition workspace object) because the subpartition is itself partitioned.

Cause: Attempted to aggregate an intermediate partition of a variable with nested partitioning.

Action: rerun the aggregate command seperately for each ultimate partition or just for the variable as a whole

ORA-36202: (XSAGOP01) 'number' is not a valid aggregation operator.

Cause: An invalid string was provided for an aggregation operator.

Action: Check the spelling of the operator to make sure you are specifying a valid one.

ORA-36204: (XSAGOP04N) In AGGMAP workspace object, the NAOPERATOR string must be HFIRST, HLAST or HEVEN.

Cause: An invalid NAOPERATOR was specified.

Action: Specify HFIRST, HLAST or HEVEN.

ORA-36206: (XSAGOP04R) In AGGMAP workspace object, REMOPERATOR string must be MIN, MAX, FIRST, LAST, HFIRST or HLAST.

Cause: An invalid REMOPERATOR was specified.

Action: Specify one of the legal operators.

ORA-36208: (XSAGOP05N) In AGGMAP workspace object, you can only specify NAOPERATOR string with the PROPORTIONAL or EVEN operators, not string.

Cause: The user specified an NAOPERATOR when you were not using PROPORTIONAL or EVEN.

Action: Remove the NAOPERATOR clause from the RELATION line.

ORA-36210: (XSAGOP05R) In AGGMAP workspace object, you can only specify the REMOPERATOR string with the PROPORTIONAL, EVEN, or HEVEN operators, not string.

Cause: The user specified a REMOPERATOR without using PROPORTIONAL, EVEN, or HEVEN.

Action: Remove the REMOPERATOR clause from the RELATION line.

ORA-36212: (XSAGOP06) In AGGMAP workspace object, you can only specify the MIN, MAX, FLOOR, and CEILING arguments while using the PROPORTIONAL operator, not string.

Cause: The user specified MIN, MAX, FLOOR, or CEILING when using an operator other than PROPORTIONAL.

Action: Remove the incorrect argument from the RELATION line.

ORA-36220: (XSLPDSC01) All dimensions in LIST number are also in the IGNORE clause.

Cause: One of the dimension lists in the dimension loop descriptor had no base dimensions except those in the IGNORE list. This leaves no dimensions for looping over.

Action: Fix the dimension loop descriptor.

ORA-36221: (XSLPDSC02) LIST number and LIST number have different base dimensions.

Cause: The base dimensions of the dimension lists given in the loop descriptor do not match.

Action: Ensure that each dimension list has the same set of looping base dimensions. If necessary, use IGNORE within a lists to discard base dimensions that should not be looped.

ORA-36222: (XSLPDSC03) duplicate IGNORE or DENSE information for dimension workspace object

Cause: An IGNORE or DENSE list in a dimension loop descriptor included the dimension twice, included two different valuesets of the dimension, or includes the dimension and a valueset of the dimension.

Action: Only use the dimension or a valueset of the dimension once in an IGNORE or DENSE list.

ORA-36223: (XSLPDSC04) object workspace object in IGNORE or DENSE list has illegal type

Cause: An IGNORE or DENSE list in a dimension loop descriptor included and object that was not a dimension or a valueset, was a conjoint dimension, or was a dimensioned valueset.

Action: Only use simple dimensions and undimensioned valuesets in the IGNORE or DENSE list.

ORA-36224: (XSLPDSC05) workspace object is not a loop dimension

Cause: An IGNORE or DENSE list in a dimension loop descriptor referenced a dimension (or a valueset of a dimension) that was not a base dimension of the loop dimension list.

Action: Remove the dimension or valueset from the IGNORE or DENSE list.

ORA-36225: (XSLPDSC06) A LOOP AGGMAP list must contain an aggmap object, followed by one or more variables and/or dimensions.

Cause: An invalid AGGMAP list was specified. Either to few objects were specified, or an incorrect type of object was used.

Action: Specify a valid AGGMAP list consisting of an aggmap object, followed by one or more variables and/or dimensions.

ORA-36226: (XSLPDSC07) The syntax of the $LOOP property on formula workspace object is incorrect.

Cause: Unrecognized contents in the $LOOP property of a formula in the table function measure list.

Action: Restrict the contents of the $LOOP property to valid elements (other than OPTIMIZED and MEASURES) of the table function LOOP directive.

ORA-36230: (XSANALYZ00) object workspace object cannot be used in the ANALYZE command

Cause: An object that cannot be analyzed was used in the ANALYZE command.

Action: Analyze VARIABLES, RELATIONS, DIMENSIONS, or SURROGATES.

ORA-36231: (XSANALYZ01) object workspace object cannot be used in the INHIERARCHY clause

Cause: An invalid INHIERARCHY object was referenced.

Action: Use either a VALUESET or boolean VARIABLE.

ORA-36232: (XSANALYZ02) a level list was specified when a language dimension was present

Cause: A level list dimension was specified when a language dimension was present.

Action: Remove the USING clause.

ORA-36233: (XSANALYZ03) the dimensionality of object workspace object does not match the ANALYZE command

Cause: The dimensionality of the object did not match the ANALYZE command syntax used.

Action: Match the ANALYZE syntax to the dimensionality of the specified object.

ORA-36234: (XSANALYZ04) all objects in the current status of the NAME dimension must have the same dimensionality when used with the ANALYZE command

Cause: The dimensionality of at least one of the objects listed in the NAME dimension does not match the rest of the objects.

Action: Make sure all objects listed in the NAME dimension have the same dimensionality.

ORA-36235: (XSANALYZ05) the database compatibility must be 11.0.0.0 or higher

Cause: The compatibe mode is not 11.0.0.0 or higher

Action: Make sure the compatible mode is 11.0.0.0 or higher

ORA-36236: (XSANALYZ06) the AW format must be 11.0.0.0 or higher to use the ANALYZE command

Cause: The AW version is less than 11.0.0.0

Action: Make sure the compatible mode is 11.0.0.0 or higher and upgrade the AW

ORA-36237: (XSANALYZ07) analytic workspace string.string must be attached RW or EXCLUSIVE mode

Cause: The analytic workspace was already attached RO or MULTI mode.

Action: Detach the analytic workspace.

ORA-36238: (XSANALYZ08) object string.string does not exist

Cause: The object name does not exist

Action: Check the spelling and case of the object name

ORA-36258: (XSAGINFO00) When the AGGMAPINFO function is called, workspace object must be an AGGMAP.

Cause: The AGGMAPINFO function was called with an object that is not an AGGMAP.

Action: Modify the call to AGGMAPINFO to specify an AGGMAP object.

ORA-36260: (XSAGHIERPART00) Aggregating from partition %J to partition %J over hierarchy workspace object creates an increase in sparsity.

Cause: In the partition creation / aggmap creation a situation developed such that when aggregating over a particular dimension of the aggmap a partition boundary was crossed such that the sparsity of the target partition included dimensions that were not in the sparsity of the source partition. Since the process of aggregation always densifies rather than sparsifying this is an extremely suboptimal design and it is not supported by the aggregate system.

Action: Set up your partitioning such that for any partition boundary the source and target partitions of the aggregation will always move towards denser partitions. For any child (c) and any parent (p) where (c) and (p) are in different partitions it must be the case that the parent partition contains no dimension in the composite that the child partition does not contain in its composite.

ORA-36261: (XSAGPARTDEP00) Can not Aggregate PARTITION TEMPLATE %J because the path of aggregation would recursively enter partition %J.

Cause: The partitioning scheme was such that while aggregating there exists a cell (m) such that both one of its descendants and one of its ancestors are both in the referenced partition, while (m) is in a different partition.

Action: Change the partitioning scheme.

ORA-36266: (XSCGMDLAGG00) Invalid context for the AGGREGATION function

Cause: The AGGREGATION function was used outside of the MODEL context.

Action: Use AGGREGATION only in a model.

ORA-36267: (XSCGMDLAGG09) workspace object has no dimensions, so it cannot have a qualified data reference.

Cause: A dimension qualification was specified for a valueset with no dimensions.

Action: Remove the qualification.

ORA-36268: (XSCGMDLAGG01) 'string' is not a valid dimension value.

Cause: The AGGREGATION parameter list included a value that does not exist in the MODEL dimension that contains the target of the AGGREGATION

Action: Specify only values from the appropriate MODEL dimension

ORA-36269: (XSCGMDLAGG10) 'workspace object' does not exist or is not a dimension.

Cause: A nonexistent or invalid object was specified as a QDR dimension.

Action: Specify existing dimensions only.

ORA-36270: (XSCGMDLAGG03) The parameter list for the AGGREGATION function includes duplicate values.

Cause: One or more duplicate values appeared in the AGGREGATION parameter list.

Action: Remove the duplication.

ORA-36271: (XSCGMDLAGG11) workspace object is not in the dimension list of valueset workspace object.

Cause: A QDR dimension was specified that does not appear in the valueset's dimension list.

Action: Specify only dimensions in the valueset's dimension list.

ORA-36272: (XSCGMDLAGG04) 'workspace object' is not a valid operator for the AGGREGATION function.

Cause: An invalid AGGREGATION operator was specified.

Action: Correct the invalid operator.

ORA-36273: (XSCGMDLAGG12) Dimension workspace object appears more than once in the QDR.

Cause: A dimension was specified more than once in the QDR.

Action: Remove the duplication.

ORA-36274: (XSCGMDLAGG05) The operator used in this equation needs a weight variable.

Cause: An invalid weight variable was specified.

Action: Correct the invalid weight variable.

ORA-36275: (XSCGMDLAGG13) string is not a valid workspace object.

Cause: A value was specified that does not exist in the QDR dimension.

Action: Specify an existing value.

ORA-36276: (XSCGMDLAGG06) The current operator does not need a weight variable.

Cause: A weight variable was specified in a context that does not support it.

Action: Remove the weight variable.

ORA-36278: (XSCGMDLAGG07) workspace object does not exist or is not valueset.

Cause: A nonexistent or invalid object was specified where a valueset is required.

Action: Specify an existing valueset only.

ORA-36280: (XSCGMDLAGG08) Valueset workspace object does not contain values of any dimension of the current model.

Cause: AGGREGATION specified a valueset of a dimension not listed in a DIMENSION statement for the current model.

Action: Add the valueset's dimension to the model's DIMENSION list, or choose a different valueset.

ORA-36290: (EIFMAKEF14) You cannot export object workspace object, because EIFVERSION is set to number. That version does not support string strings.

Cause: The user tried to export a NUMBER dimension to an EIF file with the EIFVERSION option set to a number less than 80000. Versions previous to that eversion do not support NUMBER dimensions.

Action: A NUMBER dimension cannot be used in a version of older than 9.2.0. If

ORA-36312: (PHYS00) workspace object must be a dimension, dimensioned variable or relation.

Cause: The user specified an invalid OLAP object while attempting to use the PHYSICAL function

Action: Specify a valid object

ORA-36313: (PHYS03) The VALUE option of PHYSICAL cannot be applied to a variable.

Cause: the VALUE argument to PHYSICAL was supplied for a variable.

Action: remove VALUE or specify a relation or dimension.

ORA-36314: (PHYS01) workspace object must be a dimension, relation or variable.

Cause: The user specified an invalid OLAP object while attempting to use the PHYSICAL command

Action: Specify a valid object

ORA-36315: (PHYS04) You must specify the VALUE option for scalar relation workspace object.

Cause: The VALUE argument to PHYSICAL was omitted for a scalar relation

Action: specify VALUE or choose a dimensioned relation

ORA-36316: (PHYS02) Relation workspace object must be a single-dimensional relation that relates one INTEGER dimension to another.

Cause: The user specified an invalid relation while attempting to use the PHYSICAL command

Action: Specify a valid relation

ORA-36340: (SNSYN130) The format of the PARTITIONCHECK function is: PARTITIONCHECK(aggmap, partition\_template)

Cause: Bad syntax

Action: Correct syntax

ORA-36342: (SNSYN200) The format of the CLEAR command is: CLEAR \[ ALL | STATUS \] \[ AGGREGATES | CHANGES | PRECOMPUTES | NONPRECOMPUTES | CACHE \] FROM var1 \[var2, var3...\] \[USING aggmap\]

Cause: The syntax for the CLEAR command was invalid.

Action: Modify your syntax using the correct format.

ORA-36376: (XSAGZERO) AGGREGATE attempted to divide by zero. Set DIVIDEBYZERO to YES if you want NA to be returned as the result of a division by zero.

Cause: A calculation in the current AGGREGATE command attempted to divide by zero as a result of an AVERAGE, WAVERAGE, HAVERAGE or HWAVERAGE operation.

Action: Either fix the data, or set DIVIDEBYZERO to YES to return NA instead of signaling an error.

ORA-36378: (XSAGTHRWEIGHT) While running AGGREGATE with multiple threads, the weight variable workspace object specified by your ARGS variable workspace object must exist in the same analytic workspace as your AGGMAP workspace object.

Cause: While running AGGREGATE in threaded mode, you attempted to specify a WEIGHT variable in another analytic workspace.

Action: Use a weight variable from the same analytic workspace as the aggmap and rollup variable.

ORA-36380: (AGGRECURSE) AGGREGATE was called recursively, which is not allowed.

Cause: A model, NATRIGGER, or other object called the AGGREGATE function or command while another AGGREGATE function or command was already in progress.

Action: Modify your objects so that they do not need to have two AGGREGATE commands or functions executing at once.

ORA-36389: (XSAGPARTDEP01) Can not aggregate from PARTITION number into PARTITION number due to increasing sparsity along DIMENSION %J.

Cause: The user is attempting to use partitions as a means of sparsity control, however they have set up their partitions in a manner that simply makes no sense. It is a simple fact that during aggregation data becomes more dense, not less dense, and yet their partitions indicate the opposite.

Action: Modify the partition template add the specified dimension into the source composite, or removing it from the target composite.

ORA-36391: (XSMXCLEA01) When CLEAR is used with the STATUS keyword or an AGGMAP, workspace object must be dimensioned identically to workspace object.

Cause: The user specified objects whose dimensionality didn't match

Action: Break up the CLEAR command into multiple commands where the dimensionality of the objects matches

ORA-36392: (XSMXCLEA02) When using CLEAR with the PRECOMPUTES or NONPRECOMPUTES options, you must specify an AGGMAP.

Cause: The user didn't specify an AGGMAP with the CLEAR command.

Action: specify an aggmap by adding a USING phrase to the CLEAR command, or attach a '$AGGMAP' property to the variable.

ORA-36393: (XSMXCLEA03) When using the AGGREGATES, CHANGES or CACHE options, you must specify the ALL keyword.

Cause: The user didn't use the ALL keyword when using CHANGES or CACHE.

Action: Specify the ALL keyword.

ORA-36394: (XSMXCLEA04) When using CLEAR on the AGGMAP workspace object, CACHE is the only valid directive.

Cause: The user attempted to CLEAR an AGGMAP using a directive other than CACHE.

Action: Amend the CLEAR line to only use the CACHE keyword with AGGMAPs.

ORA-36395: (XSMXCLEA05) To CLEAR ALL AGGREGATES from workspace object, you must specify an AGGMAP.

Cause: The CLEAR command could not determine how the variable was aggregated because the variable is not dimensioned by a compressed composite.

Action: Specify an aggmap by adding a USING phrase to the CLEAR command, or attach a '$AGGMAP' property to the variable.

ORA-36397: (XSSPROPNA) The value of property string cannot be NA.

Cause: The user tried to set a system-reserved property on an OLAP object to NA

Action: Set the property to a non-NA value

ORA-36398: (XSSPROP01) Property name 'number' is invalid because only system-reserved property names can begin with '$'.

Cause: The user attempted to add a property which starts with $ but is not a reserved property name

Action: Remove the $ from the property name

ORA-36399: (XSSPROPDTYPE) The data type of property string must be string.

Cause: The user tried to set a system-reserved property on an OLAP object to a value with an illegal datatype

Action: Set the property with the proper datatype

ORA-36400: (XSSPROP02) workspace object is not a valid variable name.

Cause: Not a valid variable name

Action: Change to a valid variable name

ORA-36401: (XSSPROPOTYPE) Property string may only be applied to objects of type string.

Cause: The user applied a reserved property name to an incorrect object type

Action: Apply the property to the correct object

ORA-36402: (XSSPROP03) The property '$string' requires a leading "$" because it is a system-reserved property name.

Cause: The user tried to specify a property name which is reserved, but did not use a leading $

Action: Either add a leading $ or choose another property name

ORA-36403: (XSBADSPROP) number is an illegal value for system-reserved property string on workspace object.

Cause: The user tried to specify an illegal value for a special property

Action: Specify a legal value.

ORA-36404: (XSSPROP04) Property string cannot be applied to an undimensioned (scalar) TEMPORARY variable.

Cause: The user applied a reserved property name to an incorrect object type

Action: Apply the property to the correct object

ORA-36405: (XSSPROP05) Property ignored for object workspace object:

Cause: A property was ignored during import.

Action: Refer to the message that follows this one and correct the error it describes.

ORA-36406: (VCACHE00) 'number' is an invalid value for the VARCACHE option. The only permissible values are 'SESSION', 'VARIABLE', and 'NONE'.

Cause: The user tried to assign an invalid value to the VARCACHE option

Action: Assign one of the valid values

ORA-36410: (VCACHE03) 'number' is an invalid value for the $VARCACHE property. The only permissible values are 'DEFAULT', 'SESSION', 'VARIABLE', and 'NONE'.

Cause: The user tried to assign an invalid value to the $VARCACHE property on a variable

Action: Assign one of the valid values

ORA-36608: (XSAGHOVERFLOW) The depth of the hierarchies encountered while processing a composite dimension in AGGREGATE caused a counter overflow.

Cause: The depth of the hierarchies that are part of a composite exceeded 4 billion levels during the merge.

Action: Reduce the number of levels in the hierarchies, reduce the number of dimensions in the composite, or do not aggregate over all dimensions at once.

ORA-36610: (XSLMS00) Unable to locate a message file for OLAP message: value

Cause: An internal OLAP DML program in the EXPRESS Analytic Workspace failed to retrieve a user message.

Action: Contact support.

ORA-36612: (XSLMS01) invalid OLAP message number: value

Cause: An internal OLAP DML program in the EXPRESS Analytic Workspace attempted to retrieve a non-existent message.

Action: Contact support.

ORA-36616: (XSAGMODHIER01) There is a cycle formed by MODEL workspace object and other embedded or containing models with the same dimension, workspace object.

Cause: Inclusion of a dynamic model formed a cycle in the named dimension.

Action: Edit the models involving this dimension to remove the cycle.

ORA-36617: (XSAGMODHIER02) There is a self-cycle equation in MODEL workspace object.

Cause: The model for relation modification included a self-cycle equation.

Action: Remove the self-cycle equation from the model.

ORA-36618: (XSAGMODDIM00) workspace object is not a valid dynamic model for AGGMAP.

Cause: The model failed one of the following tests: 1) only one dimension (aside from LAG/LEAD dimensions); 2) assignment to dimension values only; 3) a single simple solution block; 4) no time-series functions with variable step values.

Action: Edit the model so that it conforms to the above requirements.

ORA-36620: (XSAGMODDIM01) MODEL workspace object cannot find the matching embedded model.

Cause: AGGMAP ADD model could not find the matching embedded model.

Action: Add the matching embedded model to the AGGMAP.

ORA-36621: (XSAGMODDIM02) You cannot AGGREGATE the individual partition using static model workspace object because a partition dimension or its deriver workspace object appears in the equation of the step or simultaneous block.

Cause: An attempt was made to AGGREGATE the individual partition using the static model with the partition dimension in the equation of the step or simultaneous block.

Action: AGGREGATE the variable instead of the individual partition.

ORA-36622: (XSAGMODLIST00) workspace object cannot be added to the AGGMAP workspace object because it is not a valid MODEL.

Cause: An object specified in AGGMAP ADD was not a model.

Action: Specify the name of a model.

ORA-36626: (XSAGMODLIST02) MODEL workspace object was skipped because there is already a MODEL by that name attached to AGGMAP workspace object.

Cause: An attempt was made to add the same model to the AGGMAP twice.

Action: None required.

ORA-36628: (XSAGMODLIST03) MODEL workspace object could not be added to AGGMAP workspace object.

Cause: The dimension of the model did not match a hierarchy of the aggmap.

Action: Add a RELATION statement to the AGGMAP for that dimension.

ORA-36630: (XSDUNION00) An empty base dimension list was specified in the concat dimension definition.

Cause: An empty concat dimension list was specified.

Action: Specify a valid list of dimensions when defining a concat dimension.

ORA-36632: (XSDUNION01) The concat dimension workspace object is not currently defined as UNIQUE.

Cause: Attempt was made to CHGDFN a concat, which is already non-unique, to NOT UNIQUE.

Action: Since the concat is already non-unique, this command is unnecessary.

ORA-36634: (XSDUNION02) INTEGER dimension workspace object cannot be used as a concat dimension base.

Cause: The user cannot specify INTEGER base dimensions when defining a concat dimension.

Action: Change the datatype of the INTEGER base dimension, or omit it from the concat.

ORA-36635: (XSDUNION03) The base dimension workspace object has an invalid datatype for use in a UNIQUE concat definition.

Cause: Base dimensions of a unique concat must have TEXT or ID datatypes.

Action: Specify a valid list of dimensions when defining a unique concat dimension.

ORA-36636: (XSDUNION04) The unique concat dimension workspace object cannot be changed to NOT UNIQUE, because it is a base of at least one other unique concat dimension.

Cause: A non-unique concat dimension cannot be used as a base of a dependent unique concat.

Action: CHGDFN any dependent unique concat dimensions to NOT UNIQUE and retry.

ORA-36637: (XSDUNION05) The concat dimension cannot be defined as UNIQUE because it has a non-unique concat base dimension workspace object.

Cause: A non-unique concat dimension cannot be used as a base of a dependent unique concat.

Action: CHGDFN any non-unique concat base dimensions to UNIQUE and retry.

ORA-36638: (XSDUNION17) Concat dimension workspace object cannot be changed to UNIQUE because it has a non-unique concat base dimension workspace object.

Cause: A non-unique concat dimension cannot be used as a base of a dependent unique concat.

Action: CHGDFN any non-unique concat base dimensions to UNIQUE and retry.

ORA-36639: (XSDUNION18) UNIQUE cannot be applied to this concat dimension because leaves workspace object and workspace object share the value number.

Cause: Unique concat base dimensions cannot contain duplicate values.

Action: Use MAINTAIN RENAME to change one of the duplicate values and retry.

ORA-36640: (XSDUNION19) Concat dimension workspace object cannot be changed to UNIQUE because base dimension workspace object does not have a TEXT or ID datatype.

Cause: Base dimensions of a unique concat must have TEXT or ID datatypes.

Action: None

ORA-36641: (XSDUNION20) The concat dimension must be defined as UNIQUE because base dimension workspace object contains custom member values.

Cause: The UNIQUE keyword was not specified in the concat dimension definition, and is required if any of its base dimensions contain custom member values.

Action: Define the concat as UNIQUE, or remove all base custom member values.

ORA-36642: (XSDUNION06) Concat dimension list contains duplicate leaf dimension workspace object.

Cause: Duplicate concat leaf dimension was found.

Action: Remove duplicate concat base dimensions and retry.

ORA-36643: (XSDUNION21) Concat dimension workspace object cannot be changed to NOT UNIQUE because it contains custom member values.

Cause: Only UNIQUE concat dimensions can have custom member values or base dimensions which contain custom member values.

Action: Remove all custom member values from the concat and all of its bases, and retry.

ORA-36644: (XSDUNION07) Concat dimension workspace object contains a previously detected leaf dimension.

Cause: Concat dimension contains a previously detected leaf dimension.

Action: None

ORA-36646: (XSDUNION08) Only concat dimensions can be redefined as UNIQUE. workspace object is not a concat dimension.

Cause: UNIQUE keyword was used with an invalid object.

Action: Retry without the UNIQUE keyword.

ORA-36648: (XSDUNION09) Concat dimension workspace object is already defined as UNIQUE.

Cause: Attempt to change a concat dimension to UNIQUE, but it is already UNIQUE.

Action: None

ORA-36650: (XSDUNION10) Concat dimension workspace object cannot be changed to UNIQUE. Leaves workspace object and workspace object share the value number.

Cause: Unique concat base dimensions cannot contain duplicate values.

Action: Use MAINTAIN RENAME to change one of the duplicate values and retry.

ORA-36652: (XSDUNION11) workspace object is not a string type dimension.

Cause: The CHGDFN BASE ADD command is only valid for concat dimensions.

Action: None

ORA-36664: (XSDPART02) You must specify a partitioning method and one or more partition dimensions when defining a PARTITION TEMPLATE.

Cause: User tried to define a PARTITION TEMPLATE without a PARTITION BY clause.

Action: Add a PARTITION BY clause.

ORA-36665: (XSDPART03) workspace object is not in the dimension list of the PARTITION TEMPLATE.

Cause: While defining a partition template, user attempted to specify a partition dimension that is not a dimension of the partition template itself.

Action: Choose a partition dimension from among the dimensions of the partition template.

ORA-36666: (XSDPART04) workspace object is not a concat dimension.

Cause: User tried to define a partition template with PARTITION BY CONCAT(... dim...) where dim is not a concat dimension.

Action: Only concat dimensions can serve as partition dimensions with CONCAT partitioning. Choose a different partition dimension.

ORA-36667: (XSDPART05) string is not a legal CONCAT partition.

Cause: User attempted to use RANGE or LIST syntax in defining a CONCAT partition template.

Action: Use CONCAT partition syntax.

ORA-36668: (XSDPART06) string is not a legal RANGE partition.

Cause: User attempted to use CONCAT or LIST syntax in defining a RANGE partition template.

Action: Use RANGE partition syntax.

ORA-36669: (XSDPART07) string is not a legal LIST partition.

Cause: User attempted to use RANGE or CONCAT syntax in defining a LIST partition template.

Action: Use LIST partition syntax.

ORA-36670: (XSDPART08) workspace object is an INTEGER or NTEXT dimension, or contains an INTEGER or NTEXT dimension. INTEGER and NTEXT dimensions cannot be used as partition dimensions.

Cause: User attempted to define a partition template partitioned by an INTEGER or NTEXT dimension or a concat containing an NTEXT leaf.

Action: Either pick a different partition dimension, or redefine the dimension to use a different datatype.

ORA-36671: (XSDPART09) Leaves of workspace object have different datatypes. A partition dimension cannot have more than one datatype when RANGE partitioning is used.

Cause: User attempted to define a range partition template with a concat partition dimension, and the concat had two leaf dimensions with different datatypes.

Action: Pick a different partition dimension.

ORA-36672: (XSDPART10) A RANGE or LIST PARTITION TEMPLATE can only have a single partition dimension.

Cause: User attempted to define a RANGE or LIST partition template with more than one partition dimension.

Action: Remove all but one of the dimensions from the PARTITION BY RANGE(...) or PARTITION BY LIST(...) clause of the partition template definition.

ORA-36673: (XSDPART11) Use simple leaf values to identify concat dimension values in a VALUES LESS THAN clause, rather than the <LEAF: VALUE> format.

Cause: When defining a RANGE partition template with a concat dimension for the partition dimension, the user attempted to define a range using the <LEAF: VALUE> format of a concat dimension value.

Action: Use just the leaf value. Instead of "VALUES LESS THAN <leaf: value>", just say, "VALUES LESS THAN value".

ORA-36674: (XSDPART12) Invalid dimension value starting at string.

Cause: When defining a RANGE or LIST partition template, the user specified an invalid value in a VALUES LESS THAN or VALUES clause. An "invalid value" can be one of two things: a value whose datatype does not match the partition dimension's datatype, or a non-constant value.

Action: Modify the offending VALUES LESS THAN or VALUES phrase.

ORA-36676: (XSDPART14) Missing dimension list for string.

Cause: User attempted to define a CONCAT partition template, and didn't supply a list of dimensions for one of the partition definitions.

Action: Give a dimension list for each partition.

ORA-36677: (XSDPART15) Duplicate value in value lists of number and number

Cause: In a LIST PARTITION TEMPLATE definition, a value appeared in more than one value list, or more than once within a single value list.

Action: List each value only once.

ORA-36678: (XSDPART16) workspace object is missing from one or more partition dimension lists.

Cause: In the definition of a partition template, one of the partitions had a dimension list that did not contain all the dimensions of the partition template.

Action: Add the offending dimension to the partition's dimension list, or delete it from the partition template's dimension list. If using CONCAT partitioning and the missing dimension is a partition dimension, add to the partition dimension list any leaf of the partition dimension or any concat of leaves of the partition dimension.

ORA-36679: (XSDPART17) workspace object contains a leaf (workspace object) that is not part of the partition dimension workspace object.

Cause: In the definition of a CONCAT partition template, one of the partitions was dimensioned by a dimension that is "concat-related" to a partition dimension, meaning it shares some leaves with the partition dimension, but it contained some leaves that are not in the partition dimension.

Action: Either modify the dimensionality of the partition template to include a concat dimension that contains all the desired leaves, or pick a different dimension for the partition.

ORA-36680: (XSDPART18) workspace object is not a dimension of the PARTITION TEMPLATE.

Cause: In the definition of a partition template, one of the partitions was dimensioned by a dimension that was not given in the dimension list of the partition template.

Action: Remove the offending dimension from the partition's dimension list, or add it to the partition template's dimension list.

ORA-36681: (XSDPART19) Partitions string and string are out of order.

Cause: In the definition of a range partition template, a partition with a lower range boundary was listed after a partition with a higher range boundary.

Action: Alter the order of the partition definition list.

ORA-36682: (XSDPART20) Partition name string appears twice.

Cause: User gave a list of AW partitions in which some partition name appeared twice.

Action: Remove all but the first instance of the partition name from the list.

ORA-36683: (XSDPART21) Partition string dimensioned by more than one composite.

Cause: It is illegal to define a partition template in which one of the partitions is dimensioned by more than one composite.

Action: Make sure that the partition template being defined has at most one composite per partition.

ORA-36684: (XSDPART22) You cannot rename values of DIMENSION workspace object because it is the partition dimension of RANGE PARTITION TEMPLATE workspace object

Cause: User attempted to rename a value of a dimension that serves as the partition dimension of some RANGE or LIST partition template.

Action: It is not possible to rename values in such a dimension without deleting all RANGE and LIST partition templates that are partitioned by it.

ORA-36685: (XSDPART23) Only CONCAT partition templates can be subpartitioned.

Cause: User attempted to define a RANGE or LIST partition template with one or more partitions dimensioned by another partition template.

Action: Use only regular dimensions and composites to dimension each partition of the RANGE or LIST template.

ORA-36686: (XSDPART24) Value number is not in partition number.

Cause: User attempted to reorganize a list partition template by removing a value from some partition's list, but the value was not in the list.

Action: Ensure that the given values match the given partition.

ORA-36687: (XSDPART25) You cannot use compressed composite workspace object to dimension multiple partitions of the partition template, because its dimension list includes the PARTITION BY dimension workspace object.

Cause: The specified PARTITION BY dimension also occurred in the dimension list of a compressed composite used to dimension multiple partitions.

Action: Ensure that no PARTITION BY dimension occurs among the bases of the compressed composite used to dimension multiple partitions.

ORA-36688: (NTEXTCNV00) Error during conversion from TEXT to NTEXT.

Cause: An unknown character set conversion error occurred when converting a TEXT value to an NTEXT value.

Action: Unknown.

ORA-36691: (NTEXTCNV02) Invalid escape sequence in argument to UNISTR function: string.

Cause: The user called the UNISTR function on a string that had an invalid escape sequence. The only valid escape sequences in UNISTR are 1.) an escape-escape sequence, and 2.) an escape, followed by exactly four hexadecimal digits.

Action: Make sure that all escape sequences in UNISTR arguments are exactly four hexadecimal digits. To represent codepoints whose value is less than 0x1000, use preceding zeros. WRONG: 0x10; RIGHT: 0x0010.

ORA-36692: (XSRELGID24) A level relation must be specified for the GROUPSET and ROLLUP options of GROUPINGID.

Cause: level relation was not specified.

Action: Specify a level relation.

ORA-36693: (XSRELGID25) INHIERARCHY cannot be specified with the GROUPSET and ROLLUP options of GROUPINGID.

Cause: INHIERARCHY option was specified.

Action: Remove INHIERARCHY option.

ORA-36694: (XSRELTBL01) The value cannot be added to dimension workspace object.

Cause: Unknown.

Action: Check the context and permission for dimension maintenance.

ORA-36695: (XSRELGID26) The length of GID dimension status is number. The length of LEVEL dimension status is number.

Cause: GID dimension status did not match LEVEL dimension status.

Action: Change either GID dimension status or LEVEL dimension status.

ORA-36696: (XSRELTBL02) QDR dimension workspace object should not be the related dimension of the relation.

Cause: An ineligible dimension was specified in the Qualified Data Reference

Action: Do not attempt to qualify this dimension.

ORA-36698: (XSRELTBL03) QDR dimension workspace object should be in the dimension list that dimensions the relation.

Cause: The named dimension was not in the relation's dimension list.

Action: Select only dimensions that are in the relation's dimension list.

ORA-36700: (XSRELTBL04) Dimension workspace object cannot be qualified more than once.

Cause: The same dimension was specified more than once in the QDR.

Action: Specify each QDR dimension only once.

ORA-36702: (XSRELTBL05) The format of the HIERHEIGHT function is: HIERHEIGHT(relation \[,\] level) level >= 1.

Cause: The HIERHEIGHT function was specified incorrectly.

Action: Make sure the format is correct.

ORA-36704: (XSRELTBL06) workspace object should be dimensioned by workspace object.

Cause: The level relation is not dimensioned by the source relation dimension.

Action: Make sure the level relation has the correct definition.

ORA-36706: (XSRELTBL07) workspace object should be dimensioned by workspace object and one level dimension.

Cause: The destination relation has the wrong definition.

Action: Make sure the destination relation has the correct dimensions.

ORA-36708: (XSMXALLOC00) Variable workspace object must be dimensioned to be used by the ALLOCATE command.

Cause: The user supplied an undimensioned (scalar) variable to the ALLOCATE command.

Action: Use a dimensioned variable.

ORA-36710: (XSMXALLOC01) TARGETLOG variable workspace object must be dimensioned identically to TARGET variable workspace object.

Cause: The user attempted to execute ALLOCATE with mismatched TARGET and TARGETLOG variables

Action: Use TARGET and TARGETLOG variables with matching dimensionality.

ORA-36712: (XSMXALLOC02) Relation workspace object must be a one-dimensional self-relation to be used as a SOURCE or BASIS with ALLOCATE.

Cause: The user specified an invalid source or basis relation on the ALLOCATE command line.

Action: Modify the relation to be a one-dimensional self-relation.

ORA-36714: (XSMXALLOC03) TARGETLOG variable workspace object must have the same data type as TARGET variable workspace object.

Cause: The user specified a TARGETLOG variable that had a different data type from the TARGET variable.

Action: Use TARGETLOG and TARGET variables with an identical data type.

ORA-36718: (XSALLOC00) You do not have the necessary permissions to use AGGMAP workspace object.

Cause: The user did not have sufficient permissions to run the ALLOCATE command

Action: Change to a user ID with the appropriate permissions, or use objects that you have permission to use.

ORA-36720: (XSALLOC01) To be used with ALLOCATE, your AGGMAP workspace object must be defined with the ALLOCMAP command.

Cause: The user used the AGGMAP command to define the AGGMAP, so either the AGGMAP can only be used with the AGGREGATE command, or the AGGMAP has no contents attached to it.

Action: Use the ALLOCMAP command to define the AGGMAP.

ORA-36722: (XSALLOC02) In AGGMAP workspace object, you specified an NA or ZERO sourceval but supplied formula workspace object as your source for ALLOCATE.

Cause: The user requested that source values be modified during the allocation, but that is not possible when using a formula source.

Action: Either use a VARIABLE source or remove the SOURCEVAL specification for your ALLOCMAP.

ORA-36726: (XSALERR00) The character 'character' is not a valid format specifier for the ALLOCATE error log.

Cause: The user specified an invalid formatter in the ALLOCERRLOGHEADER or ALLOCERRLOGFORMAT options.

Action: Correct the option to have a valid format.

ORA-36728: (XSALERR01) While performing the ALLOCATE command with AGGMAP workspace object, the error logging limit of number was exceeded.

Cause: The user specified an ERRORLOG MAX value in the ALLOCMAP, but more errors were encountered while performing the allocation.

Action: Either set ERRORLOG NOSTOP, reduce the allocation errors, or increase the ERRORLOG MAX setting

ORA-36735: A value exceeded the MAX specification

Cause:.

Action: None

ORA-36740: A CHILDLOCK was detected in your valueset

Cause:.

Action: None

ORA-36761: (XSLANGDM01) Analytic workspace string already contains a dimension (%J) with the string property.

Cause: An attempt was made to apply this property to more than one dimension in the AW.

Action: Remove the property from the named dimension and try the command again.

ORA-36762: (XSLANGDM02) You cannot modify the string property of %J because analytic workspace string is attached in MULTI mode.

Cause: An attempt was made to add or delete a $DEFAULT\_LANGUAGE property in an AW attached in multiwriter mode.

Action: Attach the AW in a different mode.

ORA-36763: (XSAGGCNTMOVE01) Aggregation variable workspace object cannot have itself as an AGGCOUNT.

Cause: An attempt was made to turn a variable into its own AGGCOUNT.

Action: Select a different AGGCOUNT variable.

ORA-36764: (XSAGGCNTMOVE02) AGGCOUNT variable workspace object must be of type INTEGER, not string.

Cause: An attempt was made to create a non-INTEGER AGGCOUNT.

Action: Select an INTEGER AGGCOUNT variable.

ORA-36765: (XSAGGCNTMOVE03) A string aggregation variable cannot have a string AGGCOUNT.

Cause: The specified AGGCOUNT variable did not have the same permanence as the aggregation variable.

Action: Select an AGGCOUNT variable with the same TEMPORARY or PERMANENT attribute as the aggregation variable.

ORA-36766: (XSAGGCNTMOVE04) workspace object cannot be used as an AGGCOUNT because it has an AGGCOUNT.

Cause: The specified AGGCOUNT variable had its own AGGCOUNT

Action: Select a different variable, or remove the AGGCOUNT using CHGDFN.

ORA-36767: (XSAGGCNTMOVE05) workspace object cannot be used as an AGGCOUNT while there are permissions applied to it.

Cause: The specified AGGCOUNT variable had its own permissions distinct from those on the aggregation variable.

Action: Select a different AGGCOUNT variable, or remove the permissions. In some cases this may require an UPDATE before the command can succeed.

ORA-36768: (XSAGGCNTMOVE06) An aggregation variable and its AGGCOUNT must have the same base dimensions.

Cause: An AGGCOUNT variable was specified with different base dimensions than the aggregation variable.

Action: Select an AGGCOUNT variable with exactly the same base dimensions as the aggregation variable.

ORA-36778: (XSPGTRLOW) The amount of available temporary storage is still low. Free some temporary storage immediately. You can do so, for example, by UPDATING or DETACHING an analytic workspace.

Cause: Ran out of temporary tablespace storage.

Action: Increase the amount of temporary tablespace storage.

ORA-36779: (XSPGPOOLOUT) Invalid parameter value. Olap\_page\_pool\_size must be between must be between 2097152 and 2147483647. Olap\_page\_pool\_size remain unmodified.

Cause: Specified value for olap\_page\_pool\_size out of range.

Action: None

ORA-36800: (XSTBLFUNC00) The OLAP\_TABLE function can only have a single LOOP statement within the LIMITMAP

Cause: The OLAP table function given used more than one LOOP statement.

Action: It is currently impossible to specify more than one LOOP composite, either remove one of the statements (and loop densely over relevant dimensions), or create a new composite that encompasses both loops and have a single loop statement refer to that.

ORA-36802: (XSTBLFUNC01) The OLAP\_TABLE function must contain a DATAMAP that executes a FETCH command or a LIMITMAP.

Cause: There is no limitmap on the table function and either the datamap does not contain a fetch, or it errored before the fetch was called.

Action: Check the datamap for errors, make sure that it executes a fetch statement, if it is not intended to execute the fetch then make sure that the table function has a valid limitmap.

ORA-36804: (XSTBLFUNC02) The OLAP\_TABLE function encountered an error while parsing the LIMITMAP.

Cause: Invalid LIMITMAP syntax, or the name resolution failure of an ANALYTIC WORSKPACE OBJECT.

Action: Check the syntax of the limit map, check that the OLAP\_TABLE function refers to a valid analytic workspace, check that all analytic workspace objects within the limitmap actually exist within the analytic workspace

ORA-36806: (XSTBLFUNC03) The OLAP\_TABLE function refers to an invalid ADT attribute: string.

Cause: The limitmap refers to a matching of ADT attribute to AW object, but the ADT attribute is not an element of the specified ADT table. Most commonly this is a typo.

Action: Add the attribute to the ADT, correct the LIMITMAP, or remove the reference from the LIMITMAP.

ORA-36808: (XSTBLFUNC04) The OLAP\_TABLE function LEVELREL clause cannot declare number ADT fields from number AW fields.

Cause: The limitmap has a levelrel clause which has a different number of values in the list to the right of the FROM than it has to the left.

Action: Change the limitmap so that there is a 1:1 mapping of adt and aw elements.

ORA-36810: (XSTBLFUNC05) Analytic workspace object number does not exist.

Cause: The limitmap refers to a non-existent aw object.

Action: Change the limitmap or define the object

ORA-36812: (XSTBLFUNC06) Invalid Syntax at '?'.

Cause: The limitmap has a question mark character outside the context of a string.

Action: Fix the limitmap

ORA-36814: (XSTBLFUNC07) The datatype of the column used in the ROW2CELL clause of a LIMITMAP must be RAW(16).

Cause: Datatype of column used in ROW2CELL clause of a LIMITMAP is not RAW(16).

Action: Change datatype to RAW(16).

ORA-36815: (XSTBLFUNC08) The OLAP\_TABLE has attempted to use an AW single row function with the aw\_attach parameter set to DURATION QUERY.

Cause: The OLAP\_TABLE aw\_attach parameter was set to DURATION QUERY.

Action: Change the OLAP\_TABLE aw\_attach parameter to DURATION SESSION.

ORA-36816: (XSTBLFUNC09) The workspace object dimension is of datatype string which does not support custom member upserts.

Cause: Custom members were attempted to be added via an upsert to a dimension that does not support them

Action: Disable the AW Hash optimization for this query

ORA-36817: (XSTBLFUNC10) The LIMITMAP LOOP clause specifies an invalid type of object. workspace object must be a DIMENSION or COMPOSITE.

Cause: An invalid type of object was specified in the LOOP clause.

Action: Correct the LOOP clause.

ORA-36818: (XSTBLFUNC11) A LIMITMAP DIMENSION clause specifies an invalid type of object. workspace object must be a DIMENSION.

Cause: An invalid type of object was specified in the DIMENSION clause.

Action: Correct the DIMENSION clause.

ORA-36819: (XSTBLFUNC12) workspace object cannot be used in a LIMITMAP string clause.

Cause: An invalid type of object was specified in a LIMITMAP clause.

Action: Correct the LIMITMAP clause.

ORA-36820: (XSLMINFO00) The LIMITMAPINFO function encountered an error while parsing the LIMITMAP.

Cause: Invalid LIMITMAP syntax.

Action: Correct the syntax of the limit map.

ORA-36821: (XSJPUSH00) An error occurred while attempting to push a join of 2 AW tables.

Cause: Unknown.

Action: Re-execute the query with parameter \_optimizer\_aw\_join\_push\_enabled = FALSE.

ORA-36825: (XSTBLFUNC13) An error occurred expanding the cube\_name argument in the OLAP table function

Cause: Incorrect metadata or invalid cube name

Action: Correct the metadata.

ORA-36826: (XSTBLFUNC14) OLAP C Looper is disabled by event 37395

Cause: init.ora event 37395 includes level 8 which disables the OLAP C looper

Action: Remove event level 8 and use explicit FETCH function for OLAP\_TABLE

ORA-36830: (XSLMGEN00) Object string.string does not exist

Cause: The object does not exist

Action: Check view token for errors

ORA-36831: (XSLMGEN01) View token cannot be NA

Cause: A NA was passed as the view token

Action: Pass in a valid view token

ORA-36832: (XSLMGEN02) View token cannot be greater than 4000 bytes

Cause: A view token was greater than 4000 bytes

Action: Pass in a view token less than 4000 bytes

ORA-36833: (XSLMGEN03) View token cannot be blank

Cause: A blank was passed as the view token

Action: Pass in a valid view token

ORA-36834: (XSLMGEN04) Column tag is greater than 30 bytes

Cause: A value greater than 30 bytes was passed as the column tag

Action: Pass in a column tag of 30 bytes or less

ORA-36835: (XSLMGEN05) Dimension string.string hierarchy string level string is missing a COLUMNNAME property value

Cause: The COLUMNNAME property has no value

Action: Add a value to COLUMNNAME property

ORA-36836: (XSLMGEN06) The dimensionality of object string.string is different than the view token

Cause: The dimensionality of the cube does not match the view token

Action: Check view token for unrelated hierarchies clauses

ORA-36837: (XSLMGEN07) Object owner string is different than string

Cause: The object owners are different

Action: Make the object owners match

ORA-36838: (XSLMGEN08) Dimension string.string attribute string is missing a COLUMNNAME property value

Cause: The COLUMNNAME property has no value

Action: Add a value to COLUMNNAME property

ORA-36839: (XSLMGEN09) Cube string.string measure string is missing a COLUMNNAME property value

Cause: The COLUMNNAME property has no value

Action: Add a value to COLUMNNAME property

ORA-36840: (XSLMGEN10) Cube string.string has no measures

Cause: The cube has no measures

Action: Add a measure to the cube

ORA-36841: (XSLMGEN11) Dimension string.string was not found

Cause: The view token referenced a dimension that does not exist

Action: Pass in a dimension that does exist

ORA-36842: (XSLMGEN12) Hierarchy string.string.string was not found

Cause: The view token referenced a hierarchy that does not exist

Action: Pass in a hierarchy that does exist

ORA-36843: (XSLMGEN13) Dimension string.string hierarchy string is missing a PHYSICALNAME property value

Cause: The property PHYSICALNAME has no value

Action: Populate the property PHYSICALNAME with a value

ORA-36844: (XSLMGEN14) Dimension string.string is missing a string property value

Cause: The dimension is missing a required property

Action: Check dimension property values

ORA-36845: (XSLMGEN15) Owner is greater than 30 bytes

Cause: The owner passed is greater than 30 bytes

Action: Pass in an owner that is 30 bytes or less

ORA-36846: (XSLMGEN16) AW name is greater than 30 bytes

Cause: The AW name passed is greater than 30 bytes

Action: Pass in an AW name that is 30 bytes or less

ORA-36847: (XSLMGEN17) AW name is blank

Cause: The AW name passed is blank

Action: Pass in an AW name that has a value

ORA-36848: (XSLMGEN18) Object name string is different than string

Cause: The object names are different

Action: Make the object names match

ORA-36849: (XSLMGEN19) AW owner does not match View token owner

Cause: The AW owner does not match the View token owner

Action: Match AW ower to View token object owner

ORA-36850: (XSLMGEN20) View token string is not correct

Cause: The view token is not correct

Action: Check view token syntax for errors

ORA-36861: (XSTFRC01) SQL Cache ID parameter is invalid or missing.

Cause: SQL Cache ID parameter is required to identify SQL cache to query

Action: Supply a valid SQL Cache ID. Normally, users should not call OLAP Random Access Cursor table function themselves and therefore should not encounter this error.

ORA-36862: (XSTFRC02) Column number for this SQL Cache must be between 1 and number. Specified column number number is invalid.

Cause: Column Map references a column number that is greater than the maximum column number in SQL Cache

Action: Reference a correct column number. Normally, users should not call OLAP Random Access Cursor table function themselves and therefore should not encounter this error.

ORA-36871: (XSFTDSC01) Object string cannot be used to define a column in a LIMITMAP.

Cause: The object cannot define a column in LIMITMAP most likely because it is of a wrong type such as, for example, a Worksheet.

Action: Remove the reference from the LIMITMAP.

ORA-36872: (XSTFDSC02) Column type specifier cannot be used when the table function data type is specified.

Cause: Column type can only be used with implicitly-specified table functions

Action: Remove column type from reference from the LIMITMAP or remove the explicit table function data type specification.

ORA-36873: (XSTFDSC03) Column type must be specified explicitly.

Cause: Missing column type specification.

Action: Please, make sure to specify a column type in COLUMN MAP. Normally, users should not call OLAP Random Access Cursor table function themselves and therefore should not encounter this error.

ORA-36874: (XSTFDSC04) Expression string cannot be used to define a column in a LIMITMAP.

Cause: The expression cannot define a column in LIMITMAP most likely because it is of a wrong type such as, for example, a Worksheet.

Action: Remove the reference from the LIMITMAP.

ORA-36875: (XSTFDSC05) LIMITMAP is missing or is not a string literal.

Cause: Table functions that have an automatic ADT require LIMITMAP to be a string literal.

Action: Either specify ADT for the table function or specify LIMITMAP as a string literal.

ORA-36876: (XSTFDSC06) The column datatype string is not supported in OLAP table functions.

Cause: The object type layer does not support column datatype.

Action: Use a supported column datatype.

ORA-36881: (XSSRF00) The OLAP DML ROW2CELL function can only be used in a LIMITMAP.

Cause: Using the ROW2CELL function outside of the LIMITMAP.

Action: Remove use of the ROW2CELL function.

ORA-36882: (XSSRF01) The second parameter of an AW single row function cannot be NULL.

Cause: The second parameter of the AW single row function was NULL

Action: Pass a valid OLAP DML expression as the second parameter of the AW single row function

ORA-36883: (XSSRF02) The first parameter of an AW single row function cannot be NULL.

Cause: The first parameter of the AW single row function was NULL

Action: Make sure the column specified in the LIMITMAP ROW2CELL clause is the first parameter of the AW single row function.

ORA-36884: (XSSRF03) The value of the first parameter of the AW single row function is incorrect.

Cause: The column specified in the LIMITMAP ROW2CELL clause was not the first parameter of the AW single row function.

Action: Make sure the column specified in the LIMITMAP ROW2CELL clause is the first parameter of the AW single row function.

ORA-36885: (XSSRF04) Error rewriting OLAP DML expression. Column name too big

Cause: The column name specified in the OLAP DML expression was larger than 30 bytes.

Action: Make sure the column name specified in the OLAP DML expression is less than or equal to 30 bytes.

ORA-36886: (XSSRF05) Error rewritting OLAP DML expression. Rewritten expression is greater than number bytes

Cause: The rewritten OLAP DML expression was larger than the output buffer.

Action: Create a smaller OLAP DML expression.

ORA-36887: (XSSRF06) Error rewriting OLAP DML expression. Column name string is not a valid ADT column.

Cause: The column name passes does not exist.

Action: Only reference columns that exist.

ORA-36902: (XSAGDNGL43) In AGGMAP workspace object, the MODEL workspace object is not a model over a base dimension of the AGGMAP.

Cause: Model may include equations others than dimension values, or blocks other than simple blocks.

Action: Make sure model only includes the simple blocks with dimension values.

ORA-36904: (XSAGDNGL44) In AGGMAP workspace object, RELATION workspace object occurs after a dynamic model. The dynamic model must be the last calculation within the AGGMAP.

Cause: Before the current relation, dynamic model exists.

Action: Make sure the dynamic model is the last statement.

ORA-36910: (XSAGDNGL47) In AGGMAP workspace object, DYNAMIC MODEL workspace object can only edit the top level of its matching relation hierarchy.

Cause: The model attempted to edit a child node in the relation hierarchy.

Action: Remove this attempt from the model definition.

ORA-36912: (XSAGDNGL48) In AGGMAP workspace object, MODEL workspace object cannot be simultaneous.

Cause: The aggmap contained a simultaneous model.

Action: Change the model definition so that it is no longer simultaneous.

ORA-36913: (XSAGDNGL49) In AGGMAP workspace object, LOAD\_STATUS object workspace object must be an undimensioned VALUESET over the relation dimension.

Action: Change the aggmap definition so that it doesn't refer to an invalid object

ORA-36914: (XSAGDNGL50) In AGGMAP workspace object, LOAD\_STATUS valueset workspace object contains both a child and its ancestor.

Cause: The LOAD\_STATUS valueset is not allowed to contain both a dimension value and an ancestor of that value.

Action: Perform a limit remove ancestors on the valueset and confirm that the result matches the intended load.

ORA-36920: (XSVPMVTOPART01) workspace object cannot become anonymous because it has properties.

Cause: The OLAP DML command would result in a named object becoming an anonymous object, but the object had one or more properties associated with it.

Action: Remove the properties using the PROPERTY command. In some cases an UPDATE may be required before the command can proceed.

ORA-36921: (XSVPMVTOPART02) workspace object and workspace object are not in the same analytic workspace.

Cause: The OLAP DML command requires certain objects to be in the same analytic workspace, and the command string specified objects from two different analytic workspaces.

Action: If more than one analytic workspace is attached to the session, make sure that the object names given in the command are unique across all attached analytic workspaces. Use qualified object names (QON's) if necessary.

ORA-36922: (XSVPMVTOPART03) workspace object is the target of an external partition of a partitioned variable.

Cause: An attempt was made to perform some prohibited operation on a variable which is itself a partition of some other variable.

Action: If desired, use the CHGDFN command to DROP the partition from the partitioned variable, and then run the command again.

ORA-36923: (XSVPMVTOPART04) workspace object is not a LIST or RANGE PARTITION TEMPLATE.

Cause: The user ran a command that only operates on a LIST or RANGE partition template (or a variable dimensioned by a LIST or RANGE partition template) on some other kind of analytic workspace object.

Action: Rerun the command on a LIST or RANGE partition template or a variable dimensioned by a LIST or RANGE partition template.

ORA-36924: (XSVPMVTOPART05) workspace object is not in a COMPOSITE.

Cause: The OLAP DML command expected that the variable would be dimensioned by a composite containing the specified dimension, the specified dimension within a composite.

Action: Rerun the command on some variable is dimensioned by a composite containing the specified dimension.

ORA-36930: Cannot start a recursive call to Oracle OLAP because a ROLLBACK past an UPDATE to an attached analytic workspace has been performed.

Cause: ROLLBACK past the UPDATE of one of the attached Analytic Workspaces was called. A recursive Oracle OLAP call cannot be made until the control returns to the initial OLAP call and the affected Analytic Workspaces detached.

Action: Change the called SQL procedure to avoid the ROLLBACK

ORA-36950: (XSFCAST22) The list of string values cannot have more than number members. You supplied number.

Cause: There are more than the maximum number of OFFSET or PERIODICITY values.

Action: Remove some of the values.

ORA-36951: (XSFCAST28) The ALLOCLAST parameter cannot be set to YES unless PERIODICITY specifies more than one cycle.

Cause: ALLOCLAST was set to YES when PERIODICITY specified a single value rather than a list of nested cycles.

Action: Set ALLOCLAST to FALSE (the default), or specify more than one value for PERIODICITY (in the form of a parenthesized list).

ORA-36952: (XSFCAST23) You cannot specify a cycle number when querying the string forecasting option.

Cause: A cycle number was specified in a call to FCQUERY to retrieve forecast data not related to a cycle.

Action: Remove the cycle specification from the call to FCQUERY.

ORA-36954: (XSFCAST24) The cycle number must be between 1 and number. You specified number.

Cause: A cycle number less than 1 or greater than the maximum value was specified in a call to FCQUERY.

Action: Specify a number in the indicated range.

ORA-36956: (XSFCAST25) There are only number PERIODICITY values. You cannot specify more OFFSET values.

Cause: More OFFSET values were specified than PERIODICITY values.

Action: Supply only as many OFFSETs as there are PERIODICITY values.

ORA-36958: (XSFCAST26) The OFFSET value for cycle number cannot be greater than the cycle's PERIODICITY, which is number. You specified number.

Cause: The OFFSET for a cycle exceeded the PERIODICITY for that cycle.

Action: Supply an OFFSET less than or equal to the PERODICITY for the corresponding cycle.

ORA-36960: (XSFCAST27) The value of the string expression must be an odd number. You specified number.

Cause: An even number was given for an option that requires an odd number.

Action: Supply an odd number or let the option default.

ORA-36961: Oracle OLAP is not available.

Cause: The user attempted to utilize functionality found only in Oracle OLAP, but OLAP has not been enabled in the executable.

Action: Install the Oracle OLAP option

ORA-36962: (XSRELTBL08) string is not a valid workspace object.

Cause: The specified value does not exist in the dimension.

Action: Specify an existing value of the dimension.

ORA-36963: (XSRELTBL16) INHIERARCHY object workspace object should be a valid valueset or boolean variable.

Cause: Invalid valueset or variable was specified.

Action: Specify a valid valueset or variable.

ORA-36964: (XSRELTBL09) workspace object is not a valid level relation.

Cause: The specified level relation was not consistent with the parentage hierarchy.

Action: Fix one or both of the relations involved so that all parents are at a higher level than their children.

ORA-36965: (XSRELTBL17) Invalid LEVELORDER valueset workspace object.

Cause: Invalid LEVELORDER valueset was specified.

Action: Specify a valid valueset.

ORA-36966: (XSRELTBL10) workspace object must be a dimension.

Cause: The qualified object must be a dimensions.

Action: Remove the named object from the QDR.

ORA-36967: (XSRELTBL18) Invalid INHIERARCHY valueset workspace object.

Cause: Invalid valueset was specified.

Action: Specify a valid valueset.

ORA-36968: (XSRELTBL11) Invalid relation workspace object.

Cause: Non-object or an object other than a RELATION was specified as source or destination.

Action: Specify RELATION objects.

ORA-36969: (XSRELTBL19) Merged family relation cannot take INHIERARCHY option.

Cause: INHIERARCHY option was specified.

Action: Remove INHIERARCHY option.

ORA-36970: (XSRELTBL12) workspace object must be a self-relation.

Cause: The specified source relation was not a self-relation.

Action: Specify a self-relation as the source.

ORA-36971: (XSRELTBL19) Merged family relation cannot take LEVELORDER option.

Cause: LEVELORDER option was specified.

Action: Remove LEVELORDER option.

ORA-36972: (XSRELTBL13) Relation workspace object must be dimensioned by workspace object.

Cause: Destination relation is not dimensioned by source relation dimension.

Action: Give a correct destination relation.

ORA-36974: (XSRELTBL14) workspace object is not a BOOLEAN variable dimensioned by all the dimensions of the hierarchy.

Cause: The named variable had either the wrong data type or the wrong dimensions.

Action: Specify a BOOLEAN variable dimensioned by all the dimensions of the hierarchy.

ORA-36975: (XSRELTBL15) You must specify a USING clause naming a relation with same level dimension as LEVELORDER valueset workspace object.

Cause: USING was omitted from the HIERHEIGHT command, or specified a relation containing values of a different dimension than the LEVELORDER valueset.

Action: Provide a USING clause naming a relation containing values from the correct level dimension. --------------------------------------------------------------

ORA-36976: (XSRELGID00) Invlid GROUPINGID destination relation or variable workspace object.

Cause: Non-Object or invalid relation or invlid variable.

Action: Specify the valid relation or variable.

ORA-36977: (XSRELGID17) The GROUPINGID command does not support hierarchies with more than 126 levels.

Cause: The user specified a hierarchy with more than 126 levels.

Action: Decrease the number of levels in the hierarchy.

ORA-36978: (XSRELGID01) workspace object must be a self-relation.

Cause: Source relation is not a self-relation.

Action: Specify a self-relation as the source relation.

ORA-36979: (XSRELGID18) Property number can only be set by the GROUPINGID command.

Cause: You tried to set the $GID\_DEPTH property.

Action: Stop to set the $GID\_DEPTH property.

ORA-36980: (XSRELGID02) Variable workspace object must have a numeric data type.

Cause: The destination variable does not have a numeric data type.

Action: Make sure the variable is numeric.

ORA-36981: (XSRELGID19) The format of the GROUPINGID function is: GROUPINGID(gidrel1 \[gidrel2\]...)

Cause: Bad syntax

Action: Correct syntax

ORA-36982: (XSRELGID03) The destination variable/relation workspace object must be dimensioned by all dimensions of the source relation workspace object that have more than one value in status.

Cause: Destination variable/relation does not have enough dimensionality to hold the result from the multi-dimensional source relation.

Action: Either limit the status of hierarchy dimensions or redefine the destination variable/relation with the extended dimensionality

ORA-36983: (XSRELGID20) The groupingid relation workspace object repeats.

Cause: The groupingid relation repeated.

Action: Remove the duplicated groupingid relation.

ORA-36985: (XSRELGID21) The source relation can be omitted only when using both surrogate GID and level order valueset.

Cause: Source relation was not specified.

Action: Specify the source relation or both surrogate gid and level order valueset.

ORA-36986: (XSRELGID05) Relation workspace object must be dimensioned by workspace object.

Cause: The destination relation is not dimensioned by the dimension of the source relation.

Action: Redefine the destination relation or choose another relation with the correct dimensionality.

ORA-36988: (XSRELGID06) The related dimension of relation workspace object must be of type NUMBER.

Cause: The related dimension of the destination relation has the wrong data type.

Action: Redefine the destination relation or choose another relation whose related dimension is of type NUMBER.

ORA-36989: (XSRELGID23) GROUPSET and ROLLUP options in GROUPINGID require the destination relation.

Cause: Either variable or surrrogate dimension was specified as destination.

Action: Specify the destination relation.

ORA-36990: (XSRELGID07) The level relation workspace object should be dimensioned by a level dimension.

Cause: The level relation is not dimensioned by a level dimension.

Action: Redefine the level relation or choose another relation with the correct dimensionality.

ORA-36991: (XSRELGID08) The level relation and level order valueset provide inconsistent level mappings.

Cause: There is a conflict between the hierarchy/level relation and the level order valueset.

Action: Choose objects that do not conflict.

ORA-36992: (XSRELGID09) A level relation is needed to produce a surrogate dimension gid.

Cause: A level relation was not specified.

Action: Specify a level relation.

ORA-36993: (XSRELGID10) OBJECT workspace object must be a VARIABLE, RELATION, or a numeric SURROGATE DIMENSION based on the level dimension workspace object.

Cause: not a surrogate dimension, or the surrogate dimension is not based on the level dimension.

Action: modify/change the surrogate dimension.

ORA-36994: (XSRELGID11) The SURROGATE DIMENSION workspace object must be numeric.

Cause: The surrogate dimension is not numeric

Action: Change the surrogate dimension as numeric

ORA-36995: (XSRELGID12) There are duplicate values in the surrogate dimension gid. Use the levelorder option to resolve the ambiguity.

Cause: more than 1 hierarchies in the current computing scope.

Action: use inhierarchy to limit

ORA-36996: (XSRELGID13) Valueset workspace object should be defined over dimension workspace object.

Cause: Valueset doesn't match the dimension

Action: Change the valueset's dimension

ORA-36997: (XSRELGID14) For variable or relation grouping ids, a level relation is needed when a level order valueset is specified.

Cause: no level relation exists with level order valueset.

Action: provide the level relation.

ORA-36998: (XSRELGID15) LEVEL ORDER VALUESET workspace object and LEVEL RELATION workspace object have the different level dimensions.

Cause: either level order valueset or level relation has wrong level dimension.

Action: choose the correct level dimension

ORA-36999: (XSRELGID16) OBJECT workspace object is not a surrogate dimension, a source relation must be specified when creating any non-surrogate grouping id.

Cause: use variable/relation gid without providing the source relation

Action: use the surrogate or provide the source relation

ORA-37000: (NOTALIAS00) workspace object is not an ALIAS DIMENSION of workspace object.

Cause: The user specified an object which is not alias dimension of the first dimension

Action: Specify an alias dimension of the first dimension

ORA-37001: You have one or more attached but unupdated analytic workspaces.

Cause: The user has attempted to shut down OLAP, but they have active analytic workspaces whose changes have not been saved.

Action: Either issue the update command to update the AWs, or pass TRUE as the force parameter to dbms\_aw.shutdown()

ORA-37002: Oracle OLAP failed to initialize. Please contact Oracle OLAP technical support.

Cause: A severe error occurred while initializing OLAP.

Action: Contact support (and possibly OLAP development) for help in debugging the issue.

ORA-37003: (AWLISTALL01) number readers

Cause: used in AW(LISTALL) output formatting when %d is 0

Action: None

ORA-37004: (AWLISTALL02) number reader

Cause: used in AW(LISTALL) output formatting when %d is 1

Action: None

ORA-37005: (AWLISTALL03) number readers

Cause: used in AW(LISTALL) output formatting when %d is > 1

Action: None

ORA-37006: (AWLISTALL04) number writers

Cause: used in AW(LISTALL) output formatting when %d is 0

Action: None

ORA-37007: (AWLISTALL05) number writer

Cause: used in AW(LISTALL) output formatting when %d is 1

Action: None

ORA-37008: (AWLISTALL06) number writers

Cause: used in AW(LISTALL) output formatting when %d is > 1

Action: None

ORA-37010: (XSACQUIRE\_DIFFAW) When using the CONSISTENT WITH clause, all objects must come from the same analytic workspace.

Cause: The ACQUIRE command cannot keep objects from several workspaces consistent with each other

Action: Omit the CONSISTENT WITH clause or make sure all objects being acquired belong to the same analytic workspace.

ORA-37011: (XSACQUIRE\_LOCKED) Object workspace object is locked by another user.

Cause: Could not acquire (or acquire consistent) the object, since it is locked by another user

Action: Try to acquire this object later

ORA-37012: (XSACQUIRE\_TIMEOUT) Object workspace object is locked by another user and the WAIT timed out.

Cause: Could not acquire (or acquire consistent) the object for a while, since it is locked by another user

Action: Try to acquire this object later

ORA-37013: (XSACQUIRE\_DEADLOCK) Cannot wait to acquire object workspace object, since doing so would cause a deadlock.

Cause: Waiting to acquire the object would cause a deadlock

Action: Release some other object that another user is waiting for and try to acquire this object again.

ORA-37014: (XSACQUIRE\_ACQUIRED) Object workspace object is already acquired.

Cause: The object is already acquired

Action: Do not try to acquire this object again

ORA-37015: (XSACQUIRE\_YNRESYNC) Object workspace object is ambiguously listed to be acquired both with and without RESYNC.

Cause: The object is listed in with resync list and no resync list. Such usage is ambiguous as to the user's intent on preserving or not preserving private changes.

Action: Do not list the object both with and without RESYNC

ORA-37016: (XSACQUIRE01) You must specify objects to acquire for the ACQUIRE command.

Cause: A list of objects to acquire with or without resync is missing

Action: Specify the list of objects to acquire

ORA-37018: (XSACQUIRE03) Multiwriter operations are not supported for object workspace object.

Cause: Multiwriter presently does not work for this object type

Action: Attach the AW in RW or EXCLUSIVE modes to modify this object.

ORA-37020: (XSMULTI01) Analytic workspace string is not in MULTI mode.

Cause: The workspace for an object is not in multiwriter mode. Hence, no multiwriter operations are allowed on the objects in the workspace

Action: Attach the workspace in the multiwriter mode or do not use multiwriter commands with it.

ORA-37021: (XSMULTI02) Object workspace object is not acquired.

Cause: The object must be acquired for this multiwriter operation

Action: Do not use this multiwriter operation on an object that is not acquired

ORA-37023: (XSMLTUPD01) Object workspace object cannot be updated without dimension workspace object.

Cause: One cannot update an object if it is dimensioned by a maintained dimension without updating that dimension or if the object is a relation and the dimension is its target.

Action: Include the maintained dimension in the update list

ORA-37026: (XSMLTRESYNC01) Object workspace object cannot be resynced without dimension workspace object.

Cause: One cannot resync an object if it is dimensioned by a maintained dimension without updating that dimension or if the object is a relation and the dimension is its target.

Action: Include the maintained dimension in the update list

ORA-37027: (XSMLTRESYNC02) Object workspace object cannot be resynced without modified object workspace object because they share a modified composite dimension.

Cause: When one resyncs an object that is dimensioned by a composite dimension, the composite dimension is resynced automatically, dropping all new tuples. This cannot be done, however, if the automatic resync of the composite dimension might cause data in an object that shares the composite dimension to become NA.

Action: Resync both objects together. Alternatively, you can try to acquire the other object (that will ensure that the composite dimension is locked in the latest generation and will not be resynced when resyncing the first object), resync the first object, and release the other object.

ORA-37028: (XSMLTRESYNC03) Object workspace object cannot be resynced without modified object workspace object because they share a modified dimension map.

Cause: When one resyncs an object that is dimensioned by a dimension map, the dimension map is resynced automatically, dropping all changes. This cannot be done, however, if the automatic resync of the dimension map might cause data in an object that shares the dimension map to become NA.

Action: Resync both objects together. Alternatively, you can try to acquire the other object (that will ensure that the dimensions map is locked in the latest generation and will not be resynced when resyncing the first object), resync the first object, and release the other object.

ORA-37030: (XSMLTMAINT01) You cannot maintain workspace object because it is not ACQUIRED.

Cause: One cannot maintain a dimension in a multiwriter AW if it is not acquired.

Action: Acquire the dimension first.

ORA-37031: (XSMLTMAINT02) You cannot DELETE values of dimension workspace object in MULTI mode.

Cause: DELETE is allowed in multiwriter mode only for SESSION dimension members

Action: Attach the AW in a R/W mode and perform the DELETE operation

ORA-37032: (XSMLTMAINT03) You cannot MAINTAIN partition template workspace object in MULTI mode.

Cause: User attempted to add or remove values from a LIST partition template's lists while the AW containing the partition template was attached in multiwriter mode.

Action: Do the maintenance in read only or read-write mode.

ORA-37035: (XSMLTDCL01) You can only DEFINE SESSION objects in analytic workspace string because it is attached in MULTI mode.

Cause: Persistent object definition in multiwriter mode is not allowed.

Action: Do all persistent object definitions in read-write mode.

ORA-37036: (XSMLTDCL02) You cannot DELETE objects in analytic workspace string because it is attached in MULTI mode.

Cause: One cannot delete objects in an analytic workspace attached in MULTI mode.

Action: Do all object in read-only or read-write mode.

ORA-37037: (XSMLTDCL03) You cannot RENAME objects in analytic workspace string because it is attached in MULTI mode.

Cause: One cannot rename objects in an analytic workspace attached in MULTI mode.

Action: Do all persistent object maintenance in read-write mode.

ORA-37038: (XSMLTDCL04) You cannot change definitions of objects in analytic workspace string because it is attached in MULTI mode.

Cause: One cannot used CHGDFN command on objects in an analytic workspace attached in MULTI mode.

Action: Do all persistent object maintenance in read-write mode.

ORA-37039: (XSMLTDCL05) You cannot maintain triggers in analytic workspace string because it is attached in MULTI mode.

Cause: One cannot use TRIGGER command on objects in an analytic workspace attached in MULTI mode.

Action: Do all persistent object maintenance in read-write mode.

ORA-37040: (XSACQUIRE\_DEP\_LOCKED) Composite, concat, dimension map, or internal partition workspace object is locked by another user.

Cause: Some object required locking a composite, concat, dimension map, or internal partition, which is locked by another user

Action: Try to acquire this object later

ORA-37041: (XSACQUIRE\_DEP\_TIMEOUT) Composite, concat, dimension map, or internal partition workspace object is locked by another user and the WAIT timed out.

Cause: Some object required locking a composite, concat, dimension map, or internal partition, which could not be locked for a while, since it is locked by another user

Action: Try to acquire this object later

ORA-37042: (XSACQUIRE\_DEP\_DEADLOCK) Cannot wait to acquire composite, concat, dimension map, or internal partition workspace object, since doing so would cause a deadlock.

Cause: Some object required locking a composite, concat, dimension map, or internal partition, which would cause a deadlock

Action: Release some other object that another user is waiting for and try to acquire this object again.

ORA-37043: (XSACQUIRE\_DEP\_OLDGEN) Composite, concat, dimension map, or internal partition workspace object cannot be locked, since another user has committed a new one already.

Cause: Some object required locking a composite, concat, dimension map, or internal partition in the present generation, which is not possible, since a newer generation already exists.

Action: Try to acquire the main object with resync

ORA-37044: (XSACQUIRE\_OLDGEN) Cannot acquire object workspace object without resync.

Cause: Could not acquire the object without resync because another user has committed a newer version of it already.

Action: Try to acquire this object with resync parameter

ORA-37050: (XSMLTDCL06) You cannot use the RELATION command with workspace object because analytic workspace string is attached in MULTI mode.

Cause: One cannot use the RELATION command on objects in an analytic workspace attached in MULTI mode.

Action: Change the default relation when the analytic workspace is attached in RW or Exclusive mode.

ORA-37060: (XSMCSESS08) number is not a valid custom member in dimension workspace object.

Cause: No custom member or invalid custom member

Action: Create the custom member or use the correct custom member

ORA-37069: You may not execute a parallel OLAP operation against the EXPRESS AW.

Cause: A parallel OLAP command attempted to execute against EXPRESS.

Action: Contact Oracle support. Users should not see this message.

ORA-37070: You may not execute OLAP DML programs in a parallel query session.

Cause: The user attempted to execute a DML program inside of a parallel query session, perhaps in parallel aggregate

Action: Adjust the job so that a program does no need to be executed, or disable parallelism

ORA-37071: You may not execute a parallel OLAP operation against updated but uncommitted AW string.

Cause: The user attempted to use a parallel feature against an AW which they updated but which has not been committed

Action: Commit the current changes

ORA-37072: (XSMCSESS00) Object workspace object has the wrong type.

Cause: The object is not of the object type specified in the APPLY clause

Action: Specify the correct object type

ORA-37073: (XSMCSESS01) Applied relation workspace object must be dimensioned by dimension workspace object.

Cause: Applied relation has the different dimension from the dimension currently being maintained

Action: Maintain relation dimension

ORA-37074: (XSMCSESS02) Variable workspace object has no default aggmap.

Cause: The applied variable has no default aggmap

Action: Use variable with the default aggmap or aggmap directly

ORA-37075: (XSMCSESS03) You cannot rename a session-only dimension value.

Cause: The user tried to apply MAINTAIN RENAME to a SESSION value.

Action: Delete the old value and add a new one with the desired name.

ORA-37076: (XSMCSESS04) workspace object is not the type of dimension that can have session-only values. Valid types are TEXT, NTEXT, ID, NUMBER, and CONCAT with the UNIQUE attribute.

Cause: The user tried to add a SESSION value to a dimension type that does not support SESSION values.

Action: Use a dimension of one of the listed types.

ORA-37077: (XSMCSESS05) Object workspace object is specified more than once.

Cause: The same object name was given more than once in the apply clause or in the step dimension list.

Action: Remove the repetitions.

ORA-37078: (XSMCSESS06) The dimension being maintained (workspace object) cannot also be used as a step dimension.

Cause: The dimension being maintained was named as a step dimension.

Action: Remove this dimension from the list of step dimensions.

ORA-37079: (XSMCSESS07) Aggmap workspace object cannot be used for AGGREGATE.

Cause: The current aggmap may be for ALLOCATE

Action: Choose the correct aggmap for AGGREGATE only.

ORA-37080: Advice requested for hierarchy with too many levels

Cause: A request was made for advice on a hierarchy with more levels than are supported.

Action: Only request advice for hierarchies with less than 32 levels.

ORA-37082: Invalid percent

Cause: A request was made for advice with an illegal percent value.

Action: Request between 0 and 100 percent precomputation.

ORA-37083: Invalid object string

Cause: A request was made for advice with an illegal object name.

Action: Request using valid object names.

ORA-37084: Output valueset string must match string's dimensionality

Cause: A request was made for advice for a relation with different dimensionality from the output valueset.

Action: Request using objects that have the same dimensionality.

ORA-37086: string is not a valueset

Cause: An operation was attempted that supports only valuesets as precompute expressions in an aggmap, yet a different kind of precompute expression was used.

Action: Replace this limit expression with an equivalent valueset and retry the operation. General precompute expressions are deprecated.

ORA-37093: (XSOBJORG\_BAD\_CUBE) invalid property "string" specified for cube "string.string"

Cause: Either the specified cube did not have an AW organization, or the specified property did not apply to cubes.

Action: Specify a property that applies to cubes and a cube with an AW organization.

ORA-37094: (XSOBJORG\_BAD\_DIM) invalid property "string" specified for dimension "string.string"

Cause: Either the specified dimension did not have an AW organization, or the specified property did not apply to dimensions.

Action: Specify a property that applies to dimensions and a dimension with an AW organization.

ORA-37095: (XSOBJORG\_BAD\_MEAS) invalid property "string" specified for measure "string.string.string"

Cause: Either the specified measure did not have an AW organization, or the specified property did not apply to measures.

Action: Specify a property that applies to measures and a measure with an AW organization.

ORA-37096: (XSOBJORG\_BAD\_ATTR) invalid property "string" specified for base attribute "string.string.string"

Cause: Either the specified base attribute did not have an AW organization, or the specified property did not apply to base attribute.

Action: Specify a property that applies to base attributes and a base attribute with an AW organization.

ORA-37097: (XSOBJORG\_BAD\_DIM\_LEVEL) invalid property "string" specified for dimension level "string.string.string"

Cause: Either the specified dimension level did not have an AW organization, or the specified property did not apply to dimension levels.

Action: Specify a property that applies to dimension levels and a dimension level with an AW organization.

ORA-37098: (XSOBJORG\_BAD\_MODEL) invalid property "string" specified for dimension calculation model "string.string.string"

Cause: Either the specified dimension calculation model did not have an AW organization, or the specified property di not apply to dimension calculation models.

Action: Specify a property that applies to dimension calculation models and a dimension calculation model with an AW organization.

ORA-37099: (XSOBJORG\_BAD\_DIMALITY) invalid property "string" specified for dimensionality "string.string.string"

Cause: Either the specified dimensionality did not have an AW organization, or the specified property did not apply to dimensionalities.

Action: Specify a property that applies to dimensionalities and a dimensionality with an AW organization.

ORA-37100: (XSUNCOMMITTED) You have one or more updated but uncommitted analytic workspaces.

Cause: The user has attempted to shut down OLAP, but they have active analytic workspaces whose changes have not been saved.

Action: Issue the commit command. ---- 37101 - 37110 are reserved for partitioned variables ----

ORA-37101: (XSVPART01) Partitioning information can only be given for variables dimensioned by a PARTITION TEMPLATE.

Cause: User attempted to define or reference an AW object with the "all internal" phrase or internal / external partition list, but the object was not a variable, was not dimensioned by a partition template, or was an already existing target of an external partition.

Action: Eliminate phrases specific to partitioned variables from the definition string, or dimension the variable by a partition template.

ORA-37102: (XSVPART02) Invalid partition name string.

Cause: The user gave an invalid partition name. When defining a partitioned variable, this message indicates that the partition name does not exist in the partition template. In any other context, it indicates that the partitioned variable or partition template does not have a partition with the given name.

Action: Supply a valid partition name.

ORA-37103: (XSVPART03) The dimensionality or datatype of workspace object does not match the dimensionality or datatype of the partition.

Cause: User attempted to define a partitioned variable with an external partition, but the target of the external partition had incorrect dimensionality or datatype.

Action: Pick a different target variable. The target variable must be dimensioned by exactly the same dimensions, composites, and partition templates, in the same order, as are specified in the partition template, and must have the exact same datatype (including width, precision, and scale) as the partitioned variable itself.

ORA-37104: (XSVPART04) A partitioned variable must be dimensioned by a single partition template only.

Cause: User attempted to define a partitioned variable with more than one partition templates, or a partition template and one or more other dimensions, in the dimension list.

Action: Use only a partition template in the dimension list of the variable. All dimensions of the variable must be included in the definition of the partition template.

ORA-37105: (XSVPART05) Only variables dimensioned by a CONCAT PARTITION TEMPLATE can have string partitions.

Cause: User attempted to create an external partition on a partitioned variable, but the variable was dimensioned by a RANGE or LIST partition template.

Action: Declare the partition INTERNAL instead of EXTERNAL, or use a CONCAT partition template in place of the RANGE or LIST partition template.

ORA-37106: (XSVPART06) Invalid partition name number.

Cause: The user gave an invalid partition name.

Action: Supply a valid partition name.

ORA-37107: (XSVPART07) Attempt to write to non-existent partition of workspace object.

Cause: Some action attempted to write data to a partitioned variable, but the variable didn't have a partition for that data. This can result from a partition template that does not assign all possible dimension values to some subcube, or from a partitioned variable that does not have a partition for one of the partitions defined by the partition template.

Action: Make sure that the cell being written is assigned to some partition by the partition template, and that the variable has an actual partition associated with the partition of the template. Use the CHGDFN template DEFINE... command to define new partitions within the template, and the CHGDFN variable ADD... command to add new partitions to the variable. Alternatively, the PARTWRITEERR can be set to false, in which case data being written to a non-existent partition will be silently discarded.

ORA-37108: (XSVPART08) workspace object has an AGGCOUNT, but workspace object does not.

Cause: An attempt was made to add a partition to a partitioned variable. Either the partition was defined WITH AGGCOUNT and the partitioned variable was not, or the partitioned variable was defined WITH AGGCOUNT and the partition was not.

Action: Use CHGDFN ADD AGGCOUNT or CHGDFN DROP AGGCOUNT to either add or remove an AGGCOUNT from either the partition or the partitioned variable.

ORA-37109: (XSVPART09) Partition workspace object and its parent variable workspace object cannot both be specified.

Cause: Partition and its parent partition were operated upon together.

Action: Remove the partition from the object list.

ORA-37111: Unable to load the OLAP API sharable library: (string)

Cause: This happens if: (1) the OLAP API sharable library is missing. (2) a sharable library upon which the OLAP API sharable library depends is missing. (3) the OLAP API sharable library is the wrong version.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Customer Support.

ORA-37112: OLAP API requires Oracle 9.2 or later

Cause: The version of the OLAP API jar files that you used requires Oracle version 9.2 or later.

Action: Ensure that the URL with which the JDBC connection was opened is correct. If the RDBMS instance is running in compatibility mode for a version older than 9.2, it must be upgraded to at least 9.2.0.0.0 to be used with this version of the OLAP API.

ORA-37113: OLAP API initialization error: (string)

Cause: OLAP API initialization failed.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Customer Support.

ORA-37114: OLAP API bootstrap error: (string)

Cause: OLAP API bootstrapping failed.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Customer Support.

ORA-37115: New OLAP API history is not allowed

Cause: If there are active OLAP API sessions, it is not allowed to start a new OLAP API history by setting \_olapi\_history\_retention parameter to true.

Action: Wait until all active OLAP API sessions terminate before resetting \_olapi\_history\_retention parameter to true.

ORA-37116: OLAP API table function error: (string)

Cause: OLAP API table function failed.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Customer Support.

ORA-37117: olapi history retention has been disabled

Cause: Under certain circumstances, for example, when the database is read only, olapi history retention is not possible because it requires updating persistent tables from time to time. If olapi history retention has been disabled, setting \_olapi\_history\_retention parameter to true has no effect.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Customer Support.

ORA-37118: The OLAP API library was not preloaded.

Cause: In shared-server mode, the OLAP API library should be loaded during process initialization to ensure that the C++ virtual table addresses are identical in all shared-server processes. The OLAP API session was executing in a process in which the library had not been loaded.

Action: Set option \_XSOLAPI\_LOAD\_AT\_PROCESS\_START to SHARED\_SERVER or ALWAYS, restart the instance, and try again.

ORA-37119: Incompatible OLAP API library load address

Cause: The OLAP API session was executing in a process in which the OLAP API sharable library was loaded which was at a different address than the process in which the OLAP API session originated.

Action: Set option \_XSOLAPI\_LOAD\_AT\_PROCESS\_START to ALWAYS, restart the instance, and try again.

ORA-37120: expression string is null

Cause: expression parser received a null string for syntax analysis.

Action: Prepare a non-null and well-formed MDX query string and try again.

ORA-37121: AW Spreadsheet invalidated

Cause: While this cursor was open, a command was issued that changed the underlying data to become inconsistent.

Action: Perform the query again, avoid performing dimension maintenance and cache clears during spreadsheet processing.

ORA-37122: AW Session cache disabled

Cause: A SQL Spreadsheet was attempted while the AW Session cache was disabled.

Action: Enable the session cache and perform the query again.

ORA-37123: (XSCCOMP17) Can not AGGREGATE workspace object(partition number) because it depends on unaggregated compressed partition number.

Cause: attempted to use a feature not supported by CC's in the current AW format

Action: Remove the unsupported feature from the aggmap, or upgrade the AW

ORA-37124: (XSCCOMP16) COMPRESSED COMPOSITES with string are not supported in analytic workspace string because it has not been upgraded to version string.

Cause: attempted to use a feature not supported by CC's in the current AW format

Action: Remove the unsupported feature from the aggmap, or upgrade the AW

ORA-37126: (XSCCOMP01) The COMPRESSED COMPOSITE workspace object can only be used as a base of a single variable.

Cause: The user attempted to DEFINE a variable dimensioned by a COMPRESSED COMPOSITE, but that COMPRESSED COMPOSITE is already being used by another VARIABLE.

Action: Create a second COMPRESSED COMPOSITE for the second VARIABLE or add a measure dimension to the first variable.

ORA-37127: (XSCCOMP02) The COMPRESSED COMPOSITE workspace object must be last in the dimension list.

Cause: The user attempted to DEFINE a variable dimensioned by a COMPRESSED COMPOSITE, but gave a slower varying dimension in the dimension list.

Action: Put the COMPRESSED COMPOSITE last in the dimension list when defining the VARIABLE.

ORA-37128: (XSCCOMP20) The partition template workspace object has already used the COMPRESSED COMPOSITE workspace object.

Cause: The COMPRESSED COMPOSITE specified for either a variable or partition template is already in use in another partition template.

Action: Define a different COMPRESSED COMPOSITE.

ORA-37129: (XSCCOMP04) Cannot aggregate over COMPRESSED COMPOSITE workspace object using AGGMAP workspace object. All static MODEL statements must precede all RELATION statements over the bases of the COMPRESSED COMPOSITE.

Cause: The AGGMAP was defined with a MODEL statement after a RELATION statement over a base of the COMPRESSED COMPOSITE.

Action: Change the AGGMAP so that the MODEL statements appear before the RELATION statements.

ORA-37130: (XSCCOMP05) Cannot aggregate over COMPRESSED COMPOSITE workspace object using AGGMAP workspace object because you must specify AGGINDEX OFF when there is a PRECOMPUTE clause on a RELATION over base workspace object.

Cause: A PRECOMPUTE clause was specified in the AGGMAP for a RELATION over a base of a COMPRESSED COMPOSITE, but AGGINDEX was ON

Action: Remove the PRECOMPUTE clause from the AGGMAP, or add AGGINDEX OFF

ORA-37131: (XSCCOMP06) Cannot aggregate over COMPRESSED COMPOSITE workspace object using AGGMAP workspace object because the OPERATOR string is not supported for bases of a COMPRESSED COMPOSITE.

Cause: The user specified an aggregation OPERATOR that is not supported by COMPRESSED COMPOSITES.

Action: Use a MODEL for the calculation, or use an uncompressed COMPOSITE.

ORA-37132: (XSCCOMP07) Incremental aggregation over the dense DIMENSION workspace object is not supported when aggregating a VARIABLE dimensioned by a COMPRESSED COMPOSITE.

Cause: The status of the specified dimension did not include all detail cells.

Action: Add all detail cells to the status of the dimension and reissue the AGGREGATE command.

ORA-37133: (XSCCOMP08) You cannot write into an aggregated VARIABLE dimensioned by a COMPRESSED COMPOSITE. Use the CLEAR AGGREGATES command to reenable write access.

Cause: The user attempted to store a value into to a variable dimensioned by a compressed composite, and the variable had previously been precomputed using the AGGREGATE command. Once the AGGREGATE command is run on a variable dimensioned by a compressed composite, it becomes read-only until the computed values are removed with the CLEAR command.

Action: Run the CLEAR AGGREGATES command to remove the computed values from the variable and then rerun the failed operation. Note that CLEAR AGGREGATES will remove all the data computed during the last AGGREGATE command on this variable.

ORA-37134: (XSCCOMP09) You cannot add new values to workspace object because it includes positions for precomputed aggregate values.

Cause: The user attempted to create a new position in a compressed composite, either directly (using MAINTAIN MERGE or MAINTAIN ADD) or by storing a value into the variable dimensioned by the compressed composite. This is not allowed when the variable has been precomputed using the AGGREGATE command. Once the AGGREGATE command is run on a variable dimensioned by a compressed composite, the compressed composite becomes read-only until the computed values are removed with the CLEAR command.

Action: Run the CLEAR AGGREGATES command to remove the computed values from the variable and then rerun the failed operation. Note that CLEAR AGGREGATES will remove all the data computed during the last AGGREGATE command on this variable.

ORA-37135: (XSCCOMP19) The COMPRESSED COMPOSITE workspace object in the current defined partition template should be unique or global.

Cause: The COMPRESSED COMPOSITE was neither unique nor global. Unique means each subpartition should have different COMPRESSED COMPOSITEs; Global means all subpartitions should use the same COMPRESSED COMPOSITE if they use any COMPRESSED COMPOSITE.

Action: Redefine the partition template.

ORA-37136: (XSCCOMP11) Cannot ROLLUP dimension workspace object which is a base of COMPRESSED COMPOSITE workspace object, use AGGREGATE instead.

Cause: The user ran ROLLUP on a variable dimensioned by a COMPRESSED COMPOSITE.

Action: Instead of using ROLLUP, generate an aggmap and use AGGREGATE

ORA-37137: (XSCCOMP12) You cannot CHGDFN workspace object because it is a COMPRESSED COMPOSITE.

Cause: The user tried to CHGDFN a compressed composite

Action: If the change is desired then delete the old composite and create a new one.

ORA-37138: (XSCCOMP13) You cannot delete values from workspace object because it is an aggregated COMPRESSED COMPOSITE.

Cause: The user tried to MAINTAIN DELETE from an aggregated COMPRESSED COMPOSITE.

Action: In order to perform this sort of maintenance the composite must first be cleared. This can be done by running the CLEAR AGGREGATES command on the variable dimensioning the composite. Note that this will remove all data computed during the last AGGREGATE command.

ORA-37139: (XSCCOMP14) Cannot AGGREGATE workspace object using AGGMAP workspace object because you can not AGGREGATE a variable dimensioned by a COMPRESSED COMPOSITE using an AGGMAP with a PROTECT clause.

Cause: The user tried to AGGREGATE a variable dimensioned by a COMPRESSED COMPOSITE with an AGGMAP that included a PROTECT clause.

Action: Modify the aggmap or create a new aggmap that does not include a PROTECT clause and reaggregate.

ORA-37140: (XSCCOMP15) Cannot AGGREGATE partitioned variable workspace object using AGGMAP workspace object because you cannot use the base of a COMPRESSED COMPOSITE as a partition dimension.

Cause: The user tried to run aggregate on a partitioned variable with a partition dimension that is a base of a COMPRESSED COMPOSITE.

Action: Repartition the data, drop the partition dimension from the aggmap, or don't use COMPRESSED COMPOSITES.

ORA-37141: (XSSQLMDQ01) Invalid host variable syntax for MDQUERY procedure.

Cause: The schema and analytic workspace name for the MDQUERY cursor declaration were incorrectly specified.

Action: Specify the schema and awname as a host variable name preceded by a colon, or as a text literal string of the form 'SCHEMA.AWNAME' or '\*.\*' (quotes optional).

ORA-37142: (XSSQLMDQ02) Invalid host variable data type for MDQUERY procedure: string expected.

Cause: The user specified a host variable that was not of the correct type.

Action: Choose a different host variable.

ORA-37143: (XSSQLMDQ03) string is not a valid analytic workspace name.

Cause: The user specified an analytic workspace name not qualified by a schema name, or one or both components of the name exceed the maximum length

Action: Specify a schema-qualified analytic workspace name with components no longer than 30 characters long.

ORA-37144: (MDQUERY01) string is not a valid metadata object type for MDQUERY.

Cause: The user specified an unrecognized first argument to MDQUERY

Action: Specify a recognized object type (CUBE or DIMENSION)

ORA-37145: (XSTTS\_PLAT) Cannot transport analytic workspace across platforms.

Cause: The user attempted to transport a tablespace containing an analytic workspace from one platform to another.

Action: Use export/import to move an analytic workspace across platforms.

ORA-37146: (XSCCOMP18) The variable workspace object is already dimensioned by the COMPRESSED COMPOSITE workspace object.

Cause: An attempt was made to define the partition template dimensioned by the COMPRESSED COMPOSITE which had dimensioned the variable.

Action: Define the second COMPRESSED COMPOSITE.

ORA-37147: (XSCCOMP21) The variable workspace object must be in the current operation group of the COMPRESSED COMPOSITE workspace object.

Cause: The variable dimensioned by the COMPRESSED COMPOSITE was not in the object list of the current operation group. For AGGREGATE, all variables dimensioned by the same COMPRESSED COMPOSITE also must use the same aggmap

Action: Add the variable into the object list of the current operation group.

ORA-37148: (XSCCOMP22) workspace object is an aggregated COMPRESSED COMPOSITE.

Cause: Defined the variable or partition template with the aggregated COMPRESSED COMPOSITE.

Action: Clear the COMPRESSED COMPOSITE or use a new COMPRESSED COMPOSITE

ORA-37149: (XSCCOMP23) Individual partitions of the variable dimensiond by workspace object cannot be aggregated separately.

Cause: An attempt was made to aggregate partitions of a variable dimensioned by a global COMPRESSED COMPOSITE partition template.

Action: Aggregate the partitioned variable dimensioned by the global COMPRESSED COMPOSITE.

ORA-37150: line string, column string, string

Cause: expression syntax error was found in expression query string.

Action: Check the error message details and make the corrections.

ORA-37151: expression parser initialization error

Cause: expression parser initialization failed

Action: Please report this to Oracle Support Services.

ORA-37152: MDX query error: (string)

Cause: An exception occurred while MDX query was processed.

Action: Check the error message details and try again.

ORA-37153: unknown exception caught: (case string)

Cause: An unknown exception was caught while MDX query was processed.

Action: Please report it to Oracle Support Services.

ORA-37154: OLAP API initialization error: (case string)

Cause: OLAP API initialization failed.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Support Services.

ORA-37155: OLAP API bootstrap error: (case string)

Cause: OLAP API bootstraping failed.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Support Services.

ORA-37156: (string)

Cause: unknown

Action: Check the error message details.

ORA-37157: expression syntax error was found in expression string but error text was missing

Cause: This happened because the message file was missing.

Action: Make sure that the message file xsous.msb is located in $ORACLE\_HOME/olap/mesg and rerun your expression query.

ORA-37158: Bad clob or varray IN-args: (case string)

Cause: When in clob or varray mode, the PL/SQL mappings of OLAP API's IDL interface methods were executed blindly with null clob/varray or non-null clob/varray containing garbages.

Action: Do not blindly execute them as doing so does not make sense unless you understand how OLAP API works internally.

ORA-37159: C++ virtual table addresses become invalid due to session migration in shared server mode.

Cause: Exec-shield is the primary reason that caused this error in shared server mode. When exec-shield is turned on, there is no way to ensure that the C++ virtual table addresses are identical in all shared-server processes.

Action: Set option \_XSOLAPI\_FIX\_VPTRS to TRUE, restart the instance, and try again.

ORA-37160: OLAP object does not exist

Cause: The specified OLAP object did not exist.

Action: Use an existing OLAP object instead.

ORA-37161: invalid privilege specified for OLAP object

Cause: An attempt was made to grant or revoke an invalid privilege on an OLAP object.

Action: Specify a valid privilege.

ORA-37162: OLAP error

Cause: An exception was raised by OLAP code.

Action: Check error messages and correct any reported problems.

ORA-37163: cannot delete or truncate AW with dependent CUBES or CUBE DIMENSIONS

Cause: User attempted to delete or truncate an AW which currently has a CUBE or CUBE DIMENSION defined over it

Action: Drop the corresponding CUBE or CUBE DIMENSION before deleting the AW

ORA-37164: The current SQL statement does not support this OLAP object

Cause: The OLAP object is not supported in the current SQL statement.

Action: Use a valid SQL command on the OLAP object.

ORA-37165: cannot use EIF IMPORT into a non-empty Analytic Workspace (string.string)

Cause: An attempt was made to use EIF IMPORT to populate a non-empty Analytic Workspace.

Action: Ensure that the target Analytic Workspace is empty before populating it with EIF IMPORT.

ORA-37166: (XSOQ\_BAD\_OBJ) OLAP object "string.string" does not exist

Cause: The specified OLAP object did not exist.

Action: Use an existing OLAP object instead.

ORA-37167: (XSOQ\_BAD\_SUBOBJ) OLAP object "string.string.string" does not exist

Cause: The specified OLAP object did not exist.

Action: Use an existing OLAP object instead.

ORA-37168: (XSOBJORG\_UNSUPP\_OBJ) unsupported OLAP object "string.string" for OBJORG function

Cause: The specified OLAP object was of a type that is not supported by the OBJORG function.

Action: Specify an OLAP object of a type that the OBJORG function supports.

ORA-37169: (XSOBJORG\_UNSUPP\_SUBOBJ) unsupported OLAP object "string.string.string" for OBJORG function

Cause: The specified OLAP object was of a type that is not supported by the OBJORG function.

Action: Specify an OLAP object of a type that the OBJORG function supports.

ORA-37170: (XSOBJORG\_NA) The top-level object name argument to the OBJORG function cannot be NA.

Cause: You passed NA as the second argument to the OBJORG function.

Action: Pass the name of the top-level object instead.

ORA-37171: dimension sources not specified

Cause: The user passed an empty or null collection to DBMS\_AW.ADVISE\_SPARSITY

Action: Specify a valid set of dimension sources

ORA-37172: illegal dimension type

Cause: The user specified an invalid member of the DIMTYPE field in the dimension sources argument

Action: Specify one of the valid enumerated values in DBMS\_AW

ORA-37173: null dimension source data

Cause: The user specified NULL for one of the members of the dimension sources argument

Action: Specify a value

ORA-37174: source SQL must be a SELECT statement

Cause: The user specified an INSERT, UPDATE, DELETE or other type of SQL statement

Action: Specify a SQL SELECT statement instead

ORA-37175: column string is not a column of source data

Cause: A dimension column was specified which did not exist in the input data

Action: Specify one of the columns of the input data

ORA-37176: argument string is not valid for the sparsity advisor

Cause: An invalid argument was passed to the advisor

Action: Specify a TABLE, VIEW or SELECT statement instead

ORA-37177: column string does not have any leaf values

Cause: The specified dimension column or fact table did not contain any leaf values

Action: Populate the source data

ORA-37178: column string has no values

Cause: The specified dimension column did not contain any values

Action: Populate the source data

ORA-37179: expected at least one column for dimension string, got string

Cause: Not enough columns were specified for the dimension

Action: Specify more source columns, or change the dimension to another type

ORA-37180: expected exactly one column for dimension string, got string

Cause: Expected a single source column for the dimension. Either none or more than one was specified.

Action: Specify exactly one column, or change the dimension to another type

ORA-37181: expected exactly string columns for dimension string, got string

Cause: Expected a certain number of source columns for the dimension. Either none or the wrong number of columns was specified.

Action: Specify the right number of columns, or change the dimension to another type

ORA-37182: you may only specify one dimension to partition

Cause: The user passed a DIMENSION\_SOURCE\_T to ADVISE\_SPARSITY which specified partitioning on more than one dimension

Action: Remove all but one of the partitioning requests

ORA-37183: illegal value string for PARTBY

Cause: The user passed a value other than PARTBY\_DEFAULT, PARTBY\_NONE or PARTBY\_FORCE to DBMS\_AW.ADVISE\_SPARSITY \*Acton: Supply a legal value instead

Action: None

ORA-37184: illegal value string for ADVMODE

Cause: The user passed a value other than ADVICE\_DEFAULT, ADVICE\_FAST or ADVICE\_FULL to DBMS\_AW.ADVISE\_SPARSITY \*Acton: Supply a legal value instead

Action: None

ORA-37185: length of string (string) exceeds maximum (string)

Cause: The user passed an excessively long value

Action: Specify a legal value

ORA-37186: null child value for parent (string) found in parent-child hierarchy

Cause: While reading values for a parent-child hierarchy, a NULL child value was found for a non-NULL parent

Action: Correct the source table or SQL to return value parent and child pairs.

ORA-37187: null parent and child pair found in parent-child hierarchy

Cause: While reading values for a parent-child hierarchy, a row was retrieved which had both null child and parent values.

Action: Correct the source table or SQL to return value parent and child pairs.

ORA-37188: unexpected null result while querying string

Cause: While querying the input fact table, the sparsity advisor unexpectedly got no results, possibly due to changes being made during operation.

Action: Retry the operation ensuring that the data is not changed while the sparsity advisor is running / Errors from 37200 - 37399 are reserved for events

ORA-37400: analytic workspace does not exist

Cause: The user attempted to create an OLAP MV or Table on an AW that does not exist.

Action: Specify a valid AW in the ORGANIZATION CUBE clause

ORA-37401: you may not perform this operation on a system analytic workspace

Cause: The user attempted to create a CUBE MV or Table on a system-created AW.

Action: Specify a valid AW in the ORGANIZATION CUBE clause

ORA-37402: analytic workspace object does not exist

Cause: The user attempted to create a CUBE MV or Table mapping to an object that does not exist in the AW.

Action: Specify a valid AW object name in the ORGANIZATION CUBE clause.

ORA-37403: invalid analytic workspace object type

Cause: The user attempted to create a CUBE MV or Table mapping to an object that is not the correct type.

Action: Specify a valid AW object name in the ORGANIZATION CUBE clause.

ORA-37404: Create table as select disallowed for CUBE ORGANIZED tables

Cause: User attempted to create a CUBE ORGANIZED table by doing a create table as select.

Action: Do a create table followed by an insert as select

ORA-37405: unknown ORGANIZATION CUBE keyword

Cause: An unknown keyword was encountered while parsing the ORGANIZATION CUBE clause

Action: Correct the ORGANIZATION CUBE syntax

ORA-37406: invalid option for a CUBE ORGANIZED table

Cause: An attempt to specify one or more options for a CUBE ORGANIZED table such as: \[NO\]CACHE, NO LOGGING, CLUSTER, (NO)COMPRESS

Action: Remove the illegal option(s)

ORA-37407: invalid column type for a CUBE ORGANIZED table

Cause: A illegal column type is specified in a CUBE ORGANIZED table.

Action: Do not use column types such as LONG, LOB

ORA-37408: Truncate table disallowed for CUBE ORGANIZED tables

Cause: User attempted to perform a TRUNCATE operation on a CUBE ORGANIZED table

Action: Remove data with DELETE or drop the table and recreate it

ORA-37409: cannot delete or truncate AW used by CUBE ORGANIZED table

Cause: User attempted to delete or truncate an AW which currently has a CUBE ORGANIZED table or MV defined over it

Action: Drop the corresponding table or MV before deleting the AW

ORA-37410: cannot delete or modify AW object referenced by CUBE ORGANIZED table

Cause: User attempted to delete, chgdfn, or otherwise modify an object referenced by a CUBE ORGANIZED table or MV

Action: Drop the corresponding table or MV before manipulating the object

ORA-37411: invalid object type

Cause: User referenced an invalid object type

Action: Use an appropriate object

ORA-37412: column not mapped by ORGANIZATION CUBE clause

Cause: Not all columns in the table or MV definition were mapped in the ORGANIZATION CUBE clause

Action: Make sure that all columns are mapped

ORA-37413: column referenced multiple times in ORGANIZATION CUBE clause

Cause: The same column name was referenced multiple times inside of the ORGANIZATION CUBE clause

Action: Supply unique mappings for each column

ORA-37414: dimension without mapping or hierarchy in ORGANIZATION CUBE clause

Cause: A dimension was listed in the ORGANIZATION CUBE clause but no mapping information was supplied

Action: Provide either a column mapping or hierarchy for the dimension

ORA-37415: AW schema must match TABLE or MATERIALIZED VIEW schema

Cause: An ORGANIZATION CUBE table or MV on top of an existing AW must be created in the same schema as the AW

Action: Create the new object in the same schema as the AW

ORA-37416: multiple GROUPING IDs found for ORGANIZATION CUBE

Cause: Multiple GROUPING IDs for the ORGANIZATION CUBE TABLE or MATERIALIZED VIEW

Action: Remove the duplicates

ORA-37417: variable does not have an AGGCOUNT

Cause: A COUNT clause was specified in the ORGANIZATION CUBE description for a variable that does not have an AGGCOUNT

Action: chgdfn the variable to include an AGGCOUNT

ORA-37418: detail query cannot be derived

Cause: If an ORANIZATION CUBE MV is to automatically derive its loading clause, then its definition query cannot contain set operators (eg UNION ALL), a HAVING clause, START WITH or a SQL MODEL clause. The definition query contains these or other unsupported syntax.

Action: Use an explicit ORGANIZATION CUBE clause, or simplify the defining query.

ORA-37419: ORGANIZATION CUBE clause not allowed in explain mview

Cause: User tries to explain mview on a CREATE MATERIALIZED VIEW statement that contains a ORGANIZATION CUBE clause.

Action: Remove the ORGANIZATION CUBE clause from the CREATE MATERIALIZED MATERIALIZED VIEW statement.

ORA-37420: unsupported feature with CUBE ORGANIZED materialized view

Cause: User attempts operations such as creating a mv log on an CUBE ORGANIZED MATERIALIZED VIEW.

Action: Do not do that.

ORA-37421: specified pseudocolumn is not supported by CUBE ORGANIZED tables

Cause: The pseudocolumn ORA\_ROWSCN was referenced with a CUBE ORGANIZED table.

Action: Remove the ORA\_ROWSCN reference.

ORA-37521: (HASHSCAN00) Dimension string contains duplicate values. Please contact Oracle OLAP Technical Support.

Cause: The named dimension contains duplicate values.

Action: Contact Technical Support for instructions.

ORA-37522: (HASHSCAN01) You must specify the name of an existing TEXT or NTEXT dimension.

Cause: the \_HASHSCAN program was invoked with an invalid argument

Action: Provide a text expression yielding the name of an existing TEXT dimension

ORA-37527: (XSCHGDFN01) SESSION values of dimension string are being automatically deleted.

Cause: When using CHGDFN to rebuild the hash index of a TEXT or NTEXT dimension, SESSION values were encountered.

Action: Recreate the SESSION values after the CHGDFN command completes. Information about the deleted values has been written to the trace file.

ORA-37530: (XSCCLOAD01) When aggregating between compressed partitions the base dimensions of workspace object did not match the base dimensions of workspace object.

Cause: When aggregating a partitioned variable the dimensionality of any compressed partitions should be identical.

Action: Delete the upper partition and redefine it with a composite that matches the lower partition. If it is dependent on multiple partitions with varying sparsity you must first unify the the sparsity of the source partitions.

ORA-37531: (XSCCLOAD02) When aggregating between compressed partitions the source partitions were aggregated with a different AGGMAP, or the RELATIONS have changed since the source partitions were aggregated.

Cause: When aggregation crosses partition boundaries within a compressed variable the individual partitions must all be aggregated using a similar aggmap over the same unaltered relations.

Action: Modify the aggmap for the upper partition to more exactly match the aggmap of the source partitions, or if the aggmap is already similar, re-aggregate the source partitions to pick up any changes to the relations.

ORA-37541: Hierarchy element DIMENSION\_MEMBER can aggregate into element MEMBER\_ANCESTOR through multiple paths.

Cause: When a low level hierarchy element can reach an aggregate element by more than one path through the hierarchy, it is said to have multiple paths. The danger is that the value of the low level hierarchy element will have its value counted multiple times (once per path) in the total of the aggregate element.

Action: Eliminate multiple paths from the hierarchy.

ORA-37542: DIMENSION\_MEMBER makes hierarchy HIERARCHY1 unbalanced.

Cause: A hierarchy is balanced if: 1) All members of a level are at the same depth from the root of the hierarchy and 2) All the members in different levels are at different depths from the root of the hierarchy.

Action: Fix the hierarchy so that it is balanced. This is often done by looking for nulls in the middle levels of a hierarchy.

ORA-37543: Hierarchy member DIMENSION\_MEMBER is inconsistent across HIERARCHY1 and HIERARCHY2.

Cause: Two hierarchies are inconsistent when members that appear in both hierarchies have different ultimate leaves.

Action: This problem is usually resolved by defining a new dimension member for the secondary hierarchy, or fixing the hierarchy table so that the definitions of the member match across hierarchies.

ORA-37544: Dimension members DIMENSION\_MEMBER and MEMBER\_ANCESTOR make this dimension star inconsistent.

Cause: A dimension is "star consistent" when it can be represented in a star schema table. This requires that a hierarchy level map to a single underlying column. If a level is shared across one or more hierarchies, it must have the same set of members in each hierarchy (to share a column).

Action: Create a different level for the secondary hierarchy. This provides a separate level column for each hierarchy.

ORA-37545: DIMENSION\_MEMBER is part of a hierarchy loop.

Cause: A hierarchy has loops when the ancestor of a dimension member uses that member as its parent. Note that some loops are created across hierarchies. For example, in hierarchy 1, dimension member A is the parent of B, B is the parent of C and in hierarchy 2, C is that parent of A forms a hierarchy loop.

Action: Change the hierarchies so that the loop is eliminated or move the problem hierarchy to a different dimension.

ORA-37546: (XSHIERSP00) Levelorder valueset is empty.

Cause: An empty levelorder valueset was specified for the HIERSHAPE function.

Action: specify a non-empty levelorder valueset.

ORA-37547: (XSHIERSP01) DIMENSION\_MEMBER has no level associated with it.

Cause: DIMENSION\_MEMBER did not have an associated level. Level based hierarchies must have a level for every dimension member.

Action: Add level assignments for all dimension members in the hierarchy.

ORA-37548: (XSHIERSP02) DIMENSION\_MEMBER is not specified as a member of HIERARCHY1.

Cause: When a dimension member is part of a hierarchy, it appears in the INHIER valueset associated with the hierarchy. This dimension member is missing from this value set and thus should not be part of this hierarchy.

Action: Alter the hierarchy's membership to include the specified dimension member.

ORA-37549: (XSHIERSP03) The level of DIMENSION\_MEMBER is not lower than the level of MEMBER\_ANCESTOR.

Cause: A dimension member has a parent that is lower or on the same level as this member according to the levelorder valueset.

Action: Fix the child and/or parent levels so that every dimension member has a parent whose level is higher than the level of this member.

ORA-37550: (XSHIERSP04) The level of MEMBER\_ANCESTOR is not one level above DIMENSION\_MEMBER.

Cause: A dimension member has a parent that is not one level above the level of this member according to the levelorder valueset.

Action: Fix the child and/or parent levels so that every dimension member has a parent whose level is one level above the level of this member according to the levelorder.

ORA-37551: (XSHIERSP05) Leaf value DIMENSION\_MEMBER is not on the same level as the rest of leaf dimension values.

Cause: The detail or leaf values of this hierarchy must all have the same level. This member is on a different level than most of the leaf values.

Action: Fix DIMENSION\_MEMBER's level so that all leaves are on the same level.

ORA-37552: (XSHIERSP06) DIMENSION\_MEMBER is associated with a level not found in the levelorder valueset.

Cause: DIMENSION\_MEMBER must have an associated level that is found in the levelorder valueset so that we can figure out DIMENSION\_MEMBER's level depth.

Action: Fix DIMENSION\_MEMBER's associated level.

ORA-37553: A cycle between number and number has been detected in relation workspace object over workspace object.

Cause: A relation was used that had loops in it.

Action: Correct the relation so that it does not contain loops.

ORA-37554: A cycle between number and number has been detected in relation workspace object.

Cause: A relation was used that had loops in it.

Action: Correct the relation so that it does not contain loops.

ORA-37560: lob locator invalid for specified log target

Cause: A lob locator was passed as a target to DBMS\_CUBE\_LOG.ENABLE, but the log\_target was not DBMS\_CUBE\_LOG.TARGET\_LOB

Action: Specify LOG\_TARGET\_LOB as the log\_target, or specify a valid location instead

ORA-37561: unknown logging type

Cause: An invalid log\_type was specified

Action: Specify a valid logging type from the DBMS\_CUBE\_LOG package

ORA-37562: unknown logging target

Cause: An invalid log\_target was specified

Action: Specify a valid logging target from the DBMS\_CUBE\_LOG package

ORA-37563: invalid log verbosity

Cause: An invalid log\_verbosity was specified

Action: Specify a valid logging verbosity from the DBMS\_CUBE\_LOG package

ORA-37564: unknown log table version

Cause: Could not determine the version of the specified logging table

Action: Specify a valid target table, or use DBMS\_CUBE\_LOG.TABLE\_CREATE to create one

ORA-37565: invalid parameter for specified log type

Cause: The log\_type specified does not support the specified parameter, for instance, DBMS\_CUBE\_LOG.MAX\_ERRORS is not valid for

Action: Specify a valid log\_type / log\_param combination

ORA-37566: invalid log location

Cause: The specified log location is in an invalid format. For file targets it must be of the form 'directory\_alias/filename'

Action: Specify a valid log location

ORA-37567: log location not specified

Cause: The log location was not specified for a log target which requires one

Action: Specify a valid log location

ORA-37568: invalid log parameter

Cause: An invalid log\_param was passed to dbms\_cube\_log.set\_parameter or get\_parameter

Action: Specify a valid parameter

ORA-37569: invalid log parameter value

Cause: An invalid value was passed to dbms\_cube\_log.set\_parameter

Action: Specify a valid value

ORA-37570: invalid log specification

Cause: An invalid logging specification was supplied to DBMS\_CUBE\_LOG.SET\_LOG\_SPEC

Action: Correct the syntax being supplied

ORA-37571: invalid SQL ID

Cause: Either the SQL ID supplied was invalid or no associated logging information was captured.

Action: Specify a valid SQL ID.

ORA-37572: invalid ID

Cause: An invalid ID was supplied for the given SQL ID.

Action: Specify a valid ID for that SQL ID.

ORA-37573: no limits logged

Cause: There were no corresponding OLAP filters to the supplied information.

Action: Specify predicates on the original query or specify a new SQL ID or ID.

ORA-37574: error logging to table "string.string"

Cause: An error occurerd attempting to write log records to the named table.

Action: Make sure the user has permissions to write to the table.

ORA-37575: Invalid cube operations log component, "string".

Cause: Invalid cube operations log component value.

Action: Provide a valid cube operations log component or accept the default value by leaving the parameter unspecified.

ORA-37576: Invalid cube operations log handle id.

Cause: An invalid cube operations log handle id was specified. No oplog handle found for oplogHandleId parameter.

Action: Provide a valid cube operations log handle id for oplogHandleId. Use DBMS\_CUBE\_LOG.START\_OPLOG to get a valid handle id.

ORA-37577: Invalid cube operations log message name.

Cause: Cube operations log message name value is NULL.

Action: Provide a valid non-null cube operations log message name.

ORA-37578: Invalid cube operations log operation value.

Cause: Cube operation log operations value is NULL.

Action: Provide a valid non-null cube operations log operation value.

ORA-37580: The EXPRESS AW does not exist.

Cause: The EXPRESS AW does not exist.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Support Services.

ORA-37581: The EXPRESS AW has not been properly installed.

Cause: The EXPRESS AW has not been properly installed.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Support Services.

ORA-37582: The EXPRESS AW version string is different than the Oracle version string.

Cause: The EXPRESS AW version does not match the current Oracle version.

Action: Ensure that Oracle is properly installed with the OLAP option. If the RDBMS has been patched, review the patch log for errors. If the problem persists, report it to Oracle Support Services.

ORA-37600: (XSPGERRPERMDETACH) Ran out of tablespace storage while updating analytic workspace string

Cause: Ran out of lob segment space.

Action: Increase tablespace storage. AW may need to be detached.

ORA-37601: (XSPGERRTEMP) Ran out of temporary storage while writing to analytic workspace with ID=number. Free some temporary storage immediately. You can do so, for example, by DETACHING an analytic workspace.

Cause: Ran out of temporary tablespace storage.

Action: Increase the amount of temporary tablespace storage.

ORA-37602: (XSPGERRTEMPUSER) Ran out of temporary storage while writing to analytic workspace string. Free some temporary storage immediately. You can do so, for example, by DETACHING an analytic workspace.

Cause: Ran out of temporary tablespace storage.

Action: Increase the amount of temporary tablespace storage.

ORA-37603: (XSPGERRTEMPSYSTEM) Ran out of temporary storage while writing to a system temporary analytic workspace. Free some temporary storage immediately. You can do so, for example, by DETACHING an analytic workspace.

Cause: Ran out of temporary tablespace storage.

Action: Increase the amount of temporary tablespace storage.

ORA-37604: (XSPGERRPQUPD) Parallel updating analytic workspace string failed

Cause: Unexpected error occurred to parallel update servers.

Action: Check the error underneath and act accordingly. AW may need to be detached.

ORA-37605: error during OLAP AW UPDATE

Cause: An error occurred during the UPDATE process

Action: Refer to the next error in the error stack