#!/bin/bash
adminserver=AdminServer
domain=jvv
domain_home="/apps/oracle/wlserver/user_projects/domains/$domain"
declare -a msservers=("MS1")
logfile="/tmp/${domain}_${adminserver}.log"

listenaddr=""
listenport=7001
listensocket=${listenaddr}:${listenport}
adminurl="t3://$listensocket"

#dynamic variables
#socketcheck=$(netstat -tulpn | grep :$listenport | awk '{print $4}')
pid=$(netstat -tulpn | grep :$listenport | awk '{print $7}' | awk -F "/" '{print $1}')




function checkAdminState
{
#checking if server is up.
socketcheck=$(netstat -tulpn | grep :$listenport | awk '{print $4}')
if [[ "$socketcheck" == "$listensocket" ]] ; then
  echo "running"

else
  echo "stopped"
  #start adminserver before the managed servers..
fi
}

function startServers
{
if [[ $(checkAdminState) == "stopped" ]] ; then
  echo "Starting admin server first."
fi
if [[ $(checkAdminState) == "running" ]] ; then
  echo "Admin server is running, starting managed servers.."
  for mserver in ${msservers[*]} ; do
    echo "starting managed server $mserver"
    echo "$domain_home/bin/startManagedServer.sh $mserver $adminurl"
  done
else
  startAdminServer
  while [[ $(checkAdminState) == "stopped" ]] ; do
    echo "The state is: $(checkAdminState)"
    sleep 10
  done
  startServers
fi
}

function startAdminServer
{
cd $domain_home/bin
pwd
nohup sh startWebLogic.sh > $logfile 2>&1 &
echo "Started admin server for domain $domain."
}


adminState=$(checkAdminState)
echo "$adminState"
startServers
