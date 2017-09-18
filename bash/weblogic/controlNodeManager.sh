#!/bin/bash
declare -a DOMAINS=("00OSBT" "01WPPT" "02DFDT" "03DIVT" "04RELT")
declare -A nm_ports
#nm_ports=( ["00OSBT"]=5550 ["01WPPT"]=5551 ["02DFDT"]=5552 ["03DIVT"]=5553 ["04RELT"]=5554 )
#echo "${nm_ports[$1]}"
domain=$1
action=$2
#domain_bin="/apps/oracle_test/Middleware/user_projects/domains/domain_$domain/bin"
found=0

find_port="netstat -tulpn 2> /dev/null | grep 5550 | awk '{print $4}' | awk -F ':' '{print $2}'"
#checking if domain is valid
for i in ${DOMAINS[*]}; do
  if [[ "$i" == "$domain" ]];then
    found=1
  else
   # echo echo "$domain is not valid"
    continue
  fi
done

if [[ "$found" -eq "1" ]] || [[ "$domain" == "all" ]];then
  echo "$domain is valid."
else
  echo "INVALID DOMAIN! Exiting..."
  exit
fi

#functions to start and stop
function stopnm {
  LOGFILE="/tmp/$1.out"
  domain_bin="/apps/oracle_test/Middleware/user_projects/domains/domain_$1/bin"
  echo "Stopping nodemanager for $1"
  if [[ -d $domain_bin ]];then
    cd $domain_bin
    echo "stopping"
    nohup sh stopNodeManager.sh > $LOGFILE 2>&1 &
  else
    echo "Did not find bin directory for domain $domain"
  fi

}

function startnm {
  LOGFILE="/tmp/$1.out"
  domain_bin="/apps/oracle_test/Middleware/user_projects/domains/domain_$1/bin"
  echo "Starting nodemanager for $1"
  if [[ -d $domain_bin ]];then
    echo "Starting"
    cd $domain_bin
    nohup sh startNodeManager.sh > $LOGFILE 2>&1 &
  else
   echo "Did not find bin directory for domain $domain"
  fi

}

function stopallnm {

for i in ${DOMAINS[*]}; do
 stopnm $i
 sleep 5
done

}

function startallnm {

for i in ${DOMAINS[*]}; do
 startnm $i
 sleep 15
done

}

case $action in
  start)
    startnm
    ;;
  stop)
    stopnm
    ;;
  stopall)
    stopallnm
    ;;
  startall)
    startallnm
   ;;
  *)
    echo "Usage: $0 domain  {start|stop|stopall|startall}"
esac
