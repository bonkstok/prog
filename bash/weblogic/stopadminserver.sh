#!/bin/bash
adminserver=AdminServer
domain=jvv
domain_home="/apps/oracle/wlserver/user_projects/domains/$domain"
logfile="/tmp/shutdown_${domain}_${adminserver}.log"

admlistenaddr="192.168.242.172"
admlistenport=7001
admlistensocket=${admlistenaddr}:${admlistenport}
admurl="t3://$listensocket"
admpid=$(netstat -tulpn | grep $admlistensocket| awk '{print $7}' | awk -F "/" '{print $1}')

#functions
function checkAdminState
{
socketcheck=$(netstat -tulpn | grep $admlistensocket | awk '{print $4}')
if [[ "$socketcheck" == "$admlistensocket" ]] ; then
  echo "running"
else
  echo "stopped"
fi
}

function killAdminServer
{
admstate=$(checkAdminState)
i=0
if [[ "$admstate" == "running" ]] ; then
  while [[ $i -lt 10 && "$admstate" == "running" ]] ; do
    admstate=$(checkAdminState)
    if [[ "$i" -eq 0 ]] ; then
      echo "Stopping weblogic instance."
      cd "$domain_home/bin"
      nohup sh stopWebLogic.sh > $logfile 2>&1 &
      i=$((i+1))
      sleep 5
    else
      echo "Waiting for weblogic instance to kill"
      i=$((i+1))
      sleep 5
    fi
  done
  echo "Killing weblogic instance with forece."
  echo $admpid
  echo "kill -9 $admpid"

else
  echo "stopped"
fi
}


#main program
killAdminServer
