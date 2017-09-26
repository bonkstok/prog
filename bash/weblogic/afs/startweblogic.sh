#!/bin/bash
alias date='date +"%Y-%M-%d-%H:%M:%S"'
adminserver=AdminServer
domain=E1_Apps
domain_home="/apps/oracle/Middleware/Oracle_Home/user_projects/domains/$domain"
declare -a msservers=("AC920_SU444V1121" "DV920_SU444V1121" "PY920_SU444V1121")
declare -A msports
msports=( ["AC920_SU444V1121"]=7005 ["DV920_SU444V1121"]=7007 ["PY920_SU444V1121"]=7006 )
mslistenaddr="10.207.49.7"

logfile="/tmp/${domain}_${adminserver}.log"
logfileout="/tmp/${domain}_${adminserver}.out"

admlistenaddr="10.207.49.7"
admlistenport=7001
admlistensocket=${admlistenaddr}:${admlistenport}
adminurl="t3://$admlistensocket"

function checkAdminState
{
admsocketcheck=$(netstat -tulpn 2> /dev/null | grep $admlistensocket | awk '{print $4}')
if [[ "$admsocketcheck" == "$admlistensocket" ]] ; then
  echo "running"
else
  echo "stopped"
fi
}

function checkManagedState
{
msserver=$1
mssocketcheck=$(netstat -tulpn 2> /dev/null | grep $mslistenaddr:${msports[$msserver]}| awk '{print $4}')
echo "$mssocketcheck"
if [[ "$mssocketcheck" == "$mslistenaddr:${msports[$msserver]}" ]] ; then
  #echo "$msserver -> socket $mssocketcheck."
  echo "running"
else
  echo "stopped"
fi
}



function startAdminServer
{
admstate=$(checkAdminState)
if [[ "$admstate" == "running" ]] ; then
  echo "Admin server is already running. Skipping"
else
  if [[ -f "$domain_home/servers/$adminserver/security/boot.properties" ]] ; then
    echo "$(date) Starting admin server" >> $logfile
    cd "$domain_home/bin"
    pwd
    #nohup sh startWebLogic.sh 1> $logfileout 2>&1 &
  else
    echo "$(date) No boot.properties file has been found, exiting" >> $logfile
  fi
fi
}

function startManagedServers
{
admstate=$(checkAdminState)
i=0
#whuke kiio najeb
if [[ "$admstate" == "stopped" ]] ; then
  while [[ $i -lt 10 && "$admstate" == "running" ]] ; do
    admstate=$(checkAdminState)
    if [[ "$i" -eq 0 ]] ; then # start the admin server
      echo "$(date) Starting admin server" >> $logfile
      i=$((i+1))
      sleep 5
    else #when $i is not 0 just wait for the admin server to be in running tstate
      echo "$(date) Waiting for admin server to be in running state. Been waiting for $(($i*5)) seconds." >> $logfile
      echo "$(date) Admin state is:$admstate" >> $logfile
      i=$((i+1))
      sleep 5
    fi
  done
else # if adminserver is running, continue
  #continue
  echo "$(date) Admin server is running, starting managed servers." >> $logfile
fi
echo "here i am"
echo "$admstate"
if [[ "$admstate" == "running" ]] ; then
  for msserver in ${msservers[*]} ; do
    echo "Starting $msserver"
  done
else
  echo "Admin server did not start within the time given, exit." > $logfile
fi
}

#new log file entry:
echo "####### $(date) #######" >> $logfile
#checkManagedState "AC920_SU444V1121"
startManagedServers
