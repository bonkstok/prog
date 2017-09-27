 #!/bin/bash
action=$1
alias date='date +"%Y-%M-%d-%H:%M:%S"'
adminserver=AdminServer
domain=E1_Apps
domain_home="/apps/oracle/Middleware/Oracle_Home/user_projects/domains/$domain"
declare -a msservers=("AC920_SU444V1121" "DV920_SU444V1121" "PY920_SU444V1121")
declare -A msports
msports=( ["AC920_SU444V1121"]=7005 ["DV920_SU444V1121"]=7007 ["PY920_SU444V1121"]=7006 )
mslistenaddr="10.207.49.7"

 #admlogfile_home="/apps/oracle/Middleware/Oracle_Home/user_projects/domains/$domain/$adminserver/logs"
logfile="/tmp/${domain}_${adminserver}_stop.log"
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
if [[ "$admstate" == "stopped" ]] ; then
  echo "Admin server is already stopped. Skipping"
else
  if [[ -f "$domain_home/servers/$adminserver/security/boot.properties" ]] ; then
    echo "$(date) Stopping admin server" >> $logfile
    cd "$domain_home/bin"
    pwd
    #nohup sh stopWebLogic.sh 1> $logfileout 2>&1 &
    sleep 2
  else
    echo "$(date) No boot.properties file has been found, exiting" >> $logfile
  fi
fi
}

function stopManagedServers
{
i=0
#whuke kiio najeb
for msserver in ${msservers[*]} ; do
  msstate=$(checkManagedState $msserver)
  if [[  "$msstate"  == "running" ]] ; then
     #echo "$mslistenaddr:${msports[$msserver]}"
     echo "running"
  else
     echo "stopped"
  fi
done
}
#new log file entry:
echo "####### $(date) #######" >> $logfile
echo "####### Shutting down##" >> $logfile

case $action in
  stopall)
    stopManagedServers
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
