#!/bin/bash
declare -a DOMAINS=("00OSBT" "01WPPT" "02DFDT" "03DIVT" "04RELT")
DOMAIN_HOME="/apps/oracle_test/Middleware/user_projects/domains/domain_"
START_ADMINSERVER="startWebLogic.sh"
echo "hey"
for domain in ${DOMAINS[*]}
do
  DOMAIN_DIR="${DOMAIN_HOME}${domain}"
  LOGFILE="/tmp/StartAdmin_$domain.out"
  #echo "$DOMAIN_DIR"
  if [[ -d $DOMAIN_DIR ]]; then
    echo "Directory $DOMAIN_DIR found."
    #echo "Starting nodemanager for domain $domain"
    cd "$DOMAIN_DIR/bin"
    if [[ -f "$START_ADMINSERVER" ]]; then
     echo "Checking whether or not boot.properties for $DOMAIN has been configured..."
     if [[ -f "$DOMAIN_DIR/servers/AdminServer_$domain/security/boot.properties" ]]; then
       echo "Starting AdminServer for domain $domain"
       nohup sh $START_ADMINSERVER > $LOGFILE 2>&1 &
       echo "Sleeping for 120 seconds"
       sleep 120
     else
       echo "boot.properties for $domain has not been set. Exiting..."
       break
     fi
    else
     echo "Could not find $START_ADMINSERVER for $domain"
     break
    fi
  else
    echo "Did not find a directory for domain $domain."
    break
  fi
done
