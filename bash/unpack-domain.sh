#!/bin/bash
env=$1
domain=$2
jar_file="/tmp/$domain.jar"
oracle_home="/apps/oracle_$env"
if [[ -d $oracle_home ]]; then
  #oracle_home="$/apps/oracle_$env"
  echo "$oracle_home exists."
  echo "Chaning directory to $oracle_home/Middleware"
  cd $oracle_home/Middleware
  pwd
  if [[ -f $jar_file ]]; then
    #jar_file="/tmp/$domain.jar"
    echo "Unpack file $jar_file  exists, proceeding with unpack."
    $oracle_home/Middleware/oracle_common/common/bin/unpack.sh -domain="user_projects/domains/domain_$domain" -template=$jar_file
  else
    echo "$jar_file doesn't exist."
    echo "Exiting..."
    exit
  fi

else
  echo "$oracle_home doesn't exist."
  echo "Exiting..."
  exit
fi
