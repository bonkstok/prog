#!/bin/bash
action=$1
alias date='date +"%Y-%M-%d-%H:%M:%S"'
domain="04RELT"
adminserver="AdminServer_$domain"
domain_home="/apps/oracle_test/Middleware/user_projects/domains/domain_$domain"
declare -a msservers=("MS_${domain}_01")
declare -A msports
msports=( ["MS_${domain}_01"]=6041 )
mslistenaddr="10.206.51.103"

 #admlogfile_home="/apps/oracle/Middleware/Oracle_Home/user_projects/domains/$domain/$adminserver/logs"
logfile="/tmp/${domain}_${action}_stop.log"
logfileout="/tmp/${domain}_${adminserver}.out"

admlistenaddr="10.206.51.103"
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

function stopAdminServer
{
admstate=$(checkAdminState)
if [[ "$admstate" == "running" ]] ; then
  echo "Admin server is already stopped. Skipping"
  i=0
  while [[ "$admstate" == "running" && "$i" -lt 10 ]] ; do
    if [[ "$i" -eq 0 && -f "$domain_home/servers/$adminserver/security/boot.properties" ]] ; then
      admstate=$(checkAdminState)
      echo "$(date) Stopping $adminserver. Attempt:$i" >> $logfile
      i=$(($i+1))
      cd "$domain_home/bin"
    #nohup sh stopManagedWebLogic.sh $msserver $adminurl >
      nohup sh stopWebLogic.sh > /tmp/stop-$adminserver 2>&1 &
      echo "Stopped $adminserver."
      sleep 20
    else
      echo "$(date) Waiting for $adminserver to be shutdown. Attempt:$i - Waiting for $(($i*20)) seconds." >> $logfile
      i=$((i+1))
      sleep 20
    fi
  done
else
  echo "Admin server is already stopped. Skipping"
fi
}

function stopManagedServers
{
#whuke kiio najeb
for msserver in ${msservers[*]} ; do
  i=0
  msstate=$(checkManagedState $msserver)
  while [[  "$msstate"  == "running" && $i -lt 10 ]] ; do
     #echo "$mslistenaddr:${msports[$msserver]}"
     #echo "running"
     msstate=$(checkManagedState $msserver)
     if [[ "$i" -eq 0 && -f "$domain_home/servers/$msserver/security/boot.properties" ]] ; then
       echo "$(date) Stopping $msserver. Attempt:$i" >> $logfile
       i=$((i+1))
       cd "$domain_home/bin"
       nohup sh stopManagedWebLogic.sh $msserver $adminurl > /tmp/stop-${msserver} 2>&1 &
       echo "Stopped $msserver."
       sleep 20
     else
       echo "$(date) Waiting for $msserver to be shutdown. Attempt:$i - Waiting for $(($i*20)) seconds." >> $logfile
       i=$((i+1))
       sleep 20
     fi
  done
  if [[  "$msstate"  == "running" ]] ; then
    echo "$(date) $msserver is still running after 200 seconds. Forcing $msserver to be shutdown." >> $logfile
    mspid=$(netstat -tulpn 2> /dev/null | grep $mslistenaddr:${msports[$msserver]} | awk '{print $7}' | awk -F "/" '{print $1}')
    kill -9 $mspid
    echo "$(date) Killed $msserver with PID $mspid" >> $logfile
  else
    continue
  fi
done
}
#new log file entry:
echo "##################################" >> $logfile
echo "####### $(date) #######" >> $logfile

case $action in
  stopall)
    stopManagedServers
    stopAdminServer
  ;;
  stopadm)
    stopAdminServer
  ;;
  stopms)
    stopManagedServers
  ;;
  statusms)
    checkManagedServersState
  ;;
  *)
    echo "Usage: $0 {stopall | stopadm | stopms | statusms }"
    echo "No parameter given." >> $logfile
esac
