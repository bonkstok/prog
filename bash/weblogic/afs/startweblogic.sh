#!/bin/bash
action=$1
alias date='date +"%Y-%M-%d-%H:%M:%S"'
domain="04RELT"
adminserver="AdminServer_$domain"
domain_home="/apps/oracle_test/Middleware/user_projects/domains/domain_$domain"
declare -a msservers=("MS_${domain}_01")
declare -A msports
msports=( ["MS_${domain}_01"]=6041 )
mslistenaddr=""

 #admlogfile_home="/apps/oracle/Middleware/Oracle_Home/user_projects/domains/$domain/$adminserver/logs"
logfile="/tmp/${domain}_${action}_start.log"
logfileout="/tmp/${domain}_${adminserver}.out"

admlistenaddr=""
admlistenport=5041
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

function checkManagedServersState
{
for msserver in ${msservers[*]} ; do
  mssocketcheck=$(netstat -tulpn 2> /dev/null | grep $mslistenaddr:${msports[$msserver]}| awk '{print $4}')
  if [[ "$mssocketcheck" == "$mslistenaddr:${msports[$msserver]}" ]] ; then
  echo "Managed server $msserver is running."
  else
  echo "Managed server $msserver is currently down."
  fi
done
}

function startAdminServer
{
admstate=$(checkAdminState)
if [[ "$admstate" == "running" ]] ; then
  echo "Admin server is already running. Skipping"
else
  if [[ -f "$domain_home/servers/$adminserver/security/boot.properties" ]] ; then
    cd "$domain_home/bin"
    pwd
    echo "starting $adminserver"
    nohup sh startWebLogic.sh 1> $logfileout 2>&1 &
    sleep 50
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
  while [[ $i -lt 10 && "$admstate" == "stopped" ]] ; do
    admstate=$(checkAdminState)
    if [[ "$i" -eq 0 ]] ; then # start the admin server
      echo "$(date) Starting admin server" >> $logfile
      i=$((i+1))
      startAdminServer
    else #when $i is not 0 just wait for the admin server to be in running tstate
      echo "$(date) Waiting for admin server to be in running state. Been waiting for $(($i*50)) seconds." >> $logfile
      echo "$(date) Admin state is:$admstate" >> $logfile
      echo "Sleeping...Waiting for $adminserver to be online."
      i=$((i+1))
      sleep 50
    fi
  done
else # if adminserver is running, continue
  #continue
  echo "$(date) Admin server is running, starting managed servers." >> $logfile
fi
if [[ "$admstate" == "running" ]] ; then
  for msserver in ${msservers[*]} ; do
    if [[ -f "$domain_home/servers/$adminserver/security/boot.properties" ]] ; then
      echo "$(date) Starting $msserver" >> $logfile
      cd "$domain_home/bin"
      pwd
      echo "starting $msserver $adminurl"
      nohup sh startManagedWebLogic.sh $msserver $adminurl > /tmp/start-${msserver} 2>&1 &
      echo "Started $msserver"
      echo "$(date) started $msserver" >> $logfile
    else
      echo "No boot.properties file has been found for $msserver." >> $logfile
      break
    fi
  done
else
  echo "Admin server did not start within the time given, exit." > $logfile
fi
}

#new log file entry:
echo "##################################" >> $logfile
echo "####### $(date) #######" >> $logfile
#main program
case $action in
  startall)
    startManagedServers
  ;;
  startadm)
    startAdminServer
  ;;
  startms)
    startManagedServers
  ;;
  statusms)
    checkManagedServersState
  ;;
  *)
    echo "Usage: $0 {startall | startadm | startms  | statusms }"
    echo "No parameter given." >> $logfile
esac
