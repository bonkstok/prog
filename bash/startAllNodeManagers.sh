#!/bin/bash
declare -a DOMAINS=("00OSBT" "01WPPT" "02DFDT" "03DIVT" "04RELT")
DOMAIN_HOME="/apps/oracle_test/Middleware/user_projects/domains/domain_"
START_NODEMANAGER="startNodeManager.sh"
echo "hey"
for domain in ${DOMAINS[*]}
do
  DOMAIN_DIR="${DOMAIN_HOME}${domain}"
  LOGFILE="/tmp/$domain.out"
  #echo "$DOMAIN_DIR"
  if [[ -d $DOMAIN_DIR ]]; then
    echo "Directory $DOMAIN_DIR found."
    #echo "Starting nodemanager for domain $domain"
    cd "$DOMAIN_DIR/bin"
    if [[ -f "$START_NODEMANAGER" ]]; then
     echo "Starting nodemanager for domain $domain"
     nohup sh $START_NODEMANAGER > $LOGFILE 2>&1 &
     echo "Sleeping for 20 seconds"
     sleep 20
    else
     echo "Could not find $START_NODEMANAGER for $domain"
     break
    fi
  else
    echo "Did not find a directory for domain $domain."
    break
  fi
done
