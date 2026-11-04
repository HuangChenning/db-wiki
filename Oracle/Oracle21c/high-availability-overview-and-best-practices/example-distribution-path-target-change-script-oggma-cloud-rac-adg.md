---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/example-distribution-path-target-change-script-oggma-cloud-rac-adg.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Example Distribution Path Target Change Script

The following example script can be used to change a source Oracle GoldenGate deployment distribution path target address to reflect the new location of the receiver server after an Oracle Data Guard role transition. This example assumes the source Oracle GoldenGate deployment is configured in an MAA architecture with Data Guard, such that the distribution server can relocate between a primary and standby systems.

```
#!/bin/bash

# change_path_target.sh - changes the target host of a GG Distribution Path 
#   when the target moves between primary/standby systems.
# Example usage:
# ./change_path_target.sh <primary source VIP>:443 <standby source VIP>:443
# <path target VIP> <path name> <deployment name> <credentials file>

SOURCE1=$1      # PRIMARY Distribution Server VIP
SOURCE2=$2      # STANDBY Distribution Server VIP
TARGET=$3       # Distribution path target VIP
DPATH=$4        # Distribution path name
DEP=$5          # Deployment name
ACCESS=$6       # Config file containing the deployment credentials.
                # Example contents:
                # user = "oggadmin:<password>"

CONNECT=0

#echo "#${i} - \`date\`:"
LOGFILE=/tmp/ogg_dpatch_change.txt

result=$(curl -si -K
 $ACCESS https://$SOURCE1/$DEP/distsrvr/services/v2/sources/$DPATH
 -X GET| grep HTTP |  awk '{print $2}')

# Will return NULL of nginx not running, 502 if cannot contact server, 200 if 
# contact to server good, and others (404) for other bad reasons:

if [[ -z $result || $result -ne 200 ]]; then  # Managed to access the Distr Server
  echo "\`date\` - Couldn't contact Distribution Server at $SOURCE1
 Deployment $DEP ****" >> $LOGFILE
else # Try the other source host:
  echo "\`date\` - Got status of Distribution Server at $SOURCE1 Deployment
 $DEP ***"  >> $LOGFILE
  SOURCE=$SOURCE1
  CONNECT=1
fi

if [ $CONNECT -eq 1 ]; then
# For secure NGINX patch destination (wss)
  PAYLOAD='{"target":{"uri":"wss://'${TARGET}'/services/ggnorth/v2/targets?trail=bb"}}'
  curl -s -K $ACCESS https://$SOURCE/$DEP/distsrvr/services/v2/sources/$DPATH
 -X PATCH --data '{"status": "stopped"}'

# Set new target for path:
  curl -s -K $ACCESS https://$SOURCE/$DEP/distsrvr/services/v2/sources/$DPATH
 -X PATCH --data "$PAYLOAD"
  echo "\`date\` - Set path $DPATH on $SOURCE deployment $DEP:" >> $LOGFILE

  curl -s -K $ACCESS https://$SOURCE/$DEP/distsrvr/services/v2/sources/$DPATH
 -X GET | python -m json.tool | grep uri >> $LOGFILE
  curl -s -K $ACCESS https://$SOURCE/$DEP/distsrvr/services/v2/sources/$DPATH
 -X PATCH --data '{"status": "running"}'
  exit 0
else
  echo "\`date\` - ERROR: COULDN'T CHANGE DISTRIBUTION PATH ($DPATH) in Deployement
 $DEP at $SOURCE! ***" >> $LOGFILE
fi

# If here, means we couldn't connect to either Distribution Servers
exit 1
```